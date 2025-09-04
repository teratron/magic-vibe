#!/usr/bin/env python3
"""
MCP Client Initialization and Management System

This script initializes multiple MCP clients based on task requirements and manages
their lifecycle throughout task execution.
"""

import asyncio
import json
import os
import sys
import argparse
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class McpClientManager:
    """Manages multiple MCP client connections for task execution."""
    
    def __init__(self, task_id: str, config_path: str):
        self.task_id = task_id
        self.config_path = config_path
        self.clients: Dict[str, Any] = {}
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self):
        """Load task configuration and determine required MCP clients."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {self.config_path}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            sys.exit(1)
    
    async def detect_required_clients(self) -> List[Dict[str, Any]]:
        """
        Analyze task requirements and detect which MCP clients are needed.
        This method scans task details and feature requirements to determine
        the appropriate MCP servers to connect to.
        """
        required_clients = []
        
        # Check for database requirements
        if self._requires_database():
            required_clients.append({
                'name': 'database',
                'type': 'database',
                'command': 'python',
                'args': ['mcp-database-server.py'],
                'env': {
                    'DB_CONNECTION_STRING': os.getenv('DB_CONNECTION_STRING', ''),
                    'DB_READ_ONLY': 'true',
                    'DB_TIMEOUT': '30'
                }
            })
        
        # Check for filesystem requirements
        if self._requires_filesystem():
            required_clients.append({
                'name': 'filesystem',
                'type': 'filesystem',
                'command': 'python',
                'args': ['mcp-filesystem-server.py'],
                'env': {
                    'ALLOWED_PATHS': os.getenv('ALLOWED_PATHS', os.getcwd()),
                    'MAX_FILE_SIZE': '10485760'  # 10MB
                }
            })
        
        # Check for GitHub integration requirements
        if self._requires_github():
            required_clients.append({
                'name': 'github',
                'type': 'github',
                'command': 'npx',
                'args': ['@modelcontextprotocol/server-github'],
                'env': {
                    'GITHUB_PERSONAL_ACCESS_TOKEN': os.getenv('GITHUB_TOKEN', '')
                }
            })
        
        # Check for API integration requirements
        if self._requires_api():
            required_clients.append({
                'name': 'api',
                'type': 'api',
                'command': 'python',
                'args': ['mcp-api-server.py'],
                'env': {
                    'API_BASE_URL': os.getenv('API_BASE_URL', ''),
                    'API_KEY': os.getenv('API_KEY', ''),
                    'RATE_LIMIT': '100'
                }
            })
        
        return required_clients
    
    def _requires_database(self) -> bool:
        """Check if task requires database access."""
        feature = self.config.get('feature', '').lower()
        title = self.config.get('taskTitle', '').lower()
        
        db_keywords = ['database', 'sql', 'query', 'migration', 'schema', 'data']
        return any(keyword in feature or keyword in title for keyword in db_keywords)
    
    def _requires_filesystem(self) -> bool:
        """Check if task requires filesystem access."""
        feature = self.config.get('feature', '').lower()
        title = self.config.get('taskTitle', '').lower()
        
        fs_keywords = ['file', 'directory', 'upload', 'download', 'storage', 'import', 'export']
        return any(keyword in feature or keyword in title for keyword in fs_keywords)
    
    def _requires_github(self) -> bool:
        """Check if task requires GitHub integration."""
        feature = self.config.get('feature', '').lower()
        title = self.config.get('taskTitle', '').lower()
        
        github_keywords = ['github', 'repository', 'commit', 'branch', 'pr', 'pull request']
        return any(keyword in feature or keyword in title for keyword in github_keywords)
    
    def _requires_api(self) -> bool:
        """Check if task requires external API access."""
        feature = self.config.get('feature', '').lower()
        title = self.config.get('taskTitle', '').lower()
        
        api_keywords = ['api', 'rest', 'endpoint', 'service', 'integration', 'webhook']
        return any(keyword in feature or keyword in title for keyword in api_keywords)
    
    async def initialize_client(self, client_config: Dict[str, Any]) -> bool:
        """Initialize a single MCP client connection."""
        try:
            # Import MCP client libraries
            from mcp.client import Client
            from mcp.client.stdio import StdioClientTransport
            
            logger.info(f"Initializing MCP client: {client_config['name']}")
            
            # Create transport
            transport = StdioClientTransport({
                'command': client_config['command'],
                'args': client_config['args'],
                'env': {**os.environ, **client_config.get('env', {})}
            })
            
            # Create client
            client = Client({
                'name': f"task-{self.task_id}-{client_config['name']}",
                'version': "1.0.0"
            }, {
                'capabilities': {
                    'tools': {},
                    'resources': {}
                }
            })
            
            # Connect
            await client.connect(transport)
            
            # Store client reference
            self.clients[client_config['name']] = {
                'client': client,
                'transport': transport,
                'config': client_config,
                'connected_at': datetime.utcnow().isoformat() + 'Z',
                'status': 'connected'
            }
            
            logger.info(f"Successfully connected to MCP server: {client_config['name']}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize MCP client {client_config['name']}: {e}")
            
            # Log error to task config
            self.config.setdefault('errors', []).append({
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'client': client_config['name'],
                'error': str(e),
                'type': 'connection_failed'
            })
            
            return False
    
    async def initialize_all_clients(self):
        """Initialize all required MCP clients for the task."""
        required_clients = await self.detect_required_clients()
        
        if not required_clients:
            logger.info(f"No MCP clients required for task {self.task_id}")
            return
        
        logger.info(f"Initializing {len(required_clients)} MCP clients for task {self.task_id}")
        
        # Initialize clients concurrently
        tasks = [self.initialize_client(client_config) for client_config in required_clients]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Update configuration with client information
        self.config['mcpClients'] = {
            name: info for name, info in self.clients.items()
            if isinstance(info, dict)
        }
        
        # Remove client objects for JSON serialization
        client_configs = {}
        for name, info in self.clients.items():
            client_configs[name] = {
                'config': info['config'],
                'connected_at': info['connected_at'],
                'status': info['status']
            }
        
        self.config['mcpClients'] = client_configs
        self.config['activeConnections'] = list(self.clients.keys())
        
        # Save updated configuration
        self.save_config()
        
        successful_connections = sum(1 for result in results if result is True)
        logger.info(f"Successfully initialized {successful_connections}/{len(required_clients)} MCP clients")
    
    def save_config(self):
        """Save updated configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
    
    async def health_check(self):
        """Perform health check on all active MCP clients."""
        logger.info("Performing MCP client health check")
        
        for name, client_info in self.clients.items():
            try:
                client = client_info['client']
                # Attempt to list tools as a health check
                tools = await client.list_tools()
                logger.info(f"MCP client {name} is healthy ({len(tools)} tools available)")
                
            except Exception as e:
                logger.warning(f"MCP client {name} health check failed: {e}")
                client_info['status'] = 'unhealthy'
                client_info['last_error'] = str(e)
    
    async def cleanup(self):
        """Cleanup all MCP client connections."""
        logger.info("Cleaning up MCP client connections")
        
        for name, client_info in self.clients.items():
            try:
                if 'client' in client_info:
                    await client_info['client'].disconnect()
                logger.info(f"Disconnected MCP client: {name}")
            except Exception as e:
                logger.error(f"Error disconnecting MCP client {name}: {e}")
        
        self.clients.clear()

async def main():
    """Main entry point for MCP client initialization."""
    parser = argparse.ArgumentParser(description='Initialize MCP clients for task execution')
    parser.add_argument('--task-id', required=True, help='Task ID')
    parser.add_argument('--config-path', required=True, help='Path to task configuration file')
    parser.add_argument('--health-check', action='store_true', help='Perform health check after initialization')
    
    args = parser.parse_args()
    
    # Create MCP client manager
    manager = McpClientManager(args.task_id, args.config_path)
    
    try:
        # Initialize all required MCP clients
        await manager.initialize_all_clients()
        
        # Perform health check if requested
        if args.health_check:
            await manager.health_check()
        
        logger.info(f"MCP client initialization completed for task {args.task_id}")
        
    except Exception as e:
        logger.error(f"MCP client initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())