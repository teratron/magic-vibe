#!/usr/bin/env python3
"""
MCP Client Cleanup and Disconnection System

This script handles graceful disconnection of MCP clients and cleanup of resources
when tasks complete or fail.
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

class McpClientCleanup:
    """Handles cleanup and disconnection of MCP clients."""
    
    def __init__(self, task_id: str, status: str):
        self.task_id = task_id
        self.status = status
        self.config_path = f".magic-vibe/ai/mcp-clients/{task_id}/mcp-config.json"
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self):
        """Load task configuration."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            logger.warning(f"Configuration file not found: {self.config_path}")
            self.config = {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file: {e}")
            self.config = {}
    
    async def disconnect_clients(self):
        """Disconnect all active MCP clients."""
        active_connections = self.config.get('activeConnections', [])
        
        if not active_connections:
            logger.info(f"No active MCP connections found for task {self.task_id}")
            return
        
        logger.info(f"Disconnecting {len(active_connections)} MCP clients for task {self.task_id}")
        
        # Update each client's status
        mcp_clients = self.config.get('mcpClients', {})
        for client_name in active_connections:
            if client_name in mcp_clients:
                mcp_clients[client_name]['disconnected_at'] = datetime.utcnow().isoformat() + 'Z'
                mcp_clients[client_name]['status'] = 'disconnected'
                mcp_clients[client_name]['final_task_status'] = self.status
                
                logger.info(f"Marked MCP client {client_name} as disconnected")
        
        # Clear active connections
        self.config['activeConnections'] = []
        self.config['disconnectedAt'] = datetime.utcnow().isoformat() + 'Z'
        
        # Save updated configuration
        self.save_config()
    
    def collect_execution_metrics(self):
        """Collect and summarize execution metrics."""
        metrics = {
            'taskId': self.task_id,
            'finalStatus': self.status,
            'startedAt': self.config.get('startedAt'),
            'completedAt': datetime.utcnow().isoformat() + 'Z',
            'clientConnections': {},
            'totalClients': 0,
            'successfulConnections': 0,
            'failedConnections': 0,
            'errors': self.config.get('errors', [])
        }
        
        mcp_clients = self.config.get('mcpClients', {})
        metrics['totalClients'] = len(mcp_clients)
        
        for client_name, client_info in mcp_clients.items():
            client_metrics = {
                'name': client_name,
                'type': client_info.get('config', {}).get('type', 'unknown'),
                'status': client_info.get('status', 'unknown'),
                'connected_at': client_info.get('connected_at'),
                'disconnected_at': client_info.get('disconnected_at'),
                'duration_seconds': self._calculate_duration(
                    client_info.get('connected_at'),
                    client_info.get('disconnected_at')
                )
            }
            
            metrics['clientConnections'][client_name] = client_metrics
            
            if client_info.get('status') == 'connected':
                metrics['successfulConnections'] += 1
            else:
                metrics['failedConnections'] += 1
        
        # Save metrics
        metrics_path = f".magic-vibe/ai/mcp-clients/{self.task_id}/execution-metrics.json"
        try:
            with open(metrics_path, 'w') as f:
                json.dump(metrics, f, indent=2)
            logger.info(f"Execution metrics saved to {metrics_path}")
        except Exception as e:
            logger.error(f"Failed to save execution metrics: {e}")
        
        return metrics
    
    def _calculate_duration(self, start_time: Optional[str], end_time: Optional[str]) -> Optional[float]:
        """Calculate duration between two ISO timestamps."""
        if not start_time or not end_time:
            return None
        
        try:
            start = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            end = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            return (end - start).total_seconds()
        except Exception:
            return None
    
    def generate_cleanup_summary(self):
        """Generate a summary of the cleanup process."""
        summary = {
            'taskId': self.task_id,
            'cleanupTimestamp': datetime.utcnow().isoformat() + 'Z',
            'finalStatus': self.status,
            'mcpClientsDisconnected': len(self.config.get('mcpClients', {})),
            'errorsEncountered': len(self.config.get('errors', [])),
            'cleanupSuccess': True
        }
        
        # Save cleanup summary
        summary_path = f".magic-vibe/ai/mcp-clients/{self.task_id}/cleanup-summary.json"
        try:
            with open(summary_path, 'w') as f:
                json.dump(summary, f, indent=2)
            logger.info(f"Cleanup summary saved to {summary_path}")
        except Exception as e:
            logger.error(f"Failed to save cleanup summary: {e}")
            summary['cleanupSuccess'] = False
        
        return summary
    
    def save_config(self):
        """Save updated configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
    
    def cleanup_temporary_files(self):
        """Clean up temporary files and resources."""
        task_dir = Path(f".magic-vibe/ai/mcp-clients/{self.task_id}")
        
        # Remove temporary files but keep configuration and metrics
        temp_patterns = ['*.tmp', '*.log', '*.pid', 'temp_*']
        
        for pattern in temp_patterns:
            for temp_file in task_dir.glob(pattern):
                try:
                    temp_file.unlink()
                    logger.info(f"Removed temporary file: {temp_file}")
                except Exception as e:
                    logger.warning(f"Failed to remove temporary file {temp_file}: {e}")
    
    async def perform_cleanup(self):
        """Perform complete cleanup process."""
        logger.info(f"Starting MCP client cleanup for task {self.task_id}")
        
        try:
            # Disconnect all MCP clients
            await self.disconnect_clients()
            
            # Collect execution metrics
            metrics = self.collect_execution_metrics()
            
            # Generate cleanup summary
            summary = self.generate_cleanup_summary()
            
            # Clean up temporary files
            self.cleanup_temporary_files()
            
            logger.info(f"MCP client cleanup completed successfully for task {self.task_id}")
            return True
            
        except Exception as e:
            logger.error(f"MCP client cleanup failed for task {self.task_id}: {e}")
            return False

async def main():
    """Main entry point for MCP client cleanup."""
    parser = argparse.ArgumentParser(description='Cleanup MCP clients after task completion')
    parser.add_argument('--task-id', required=True, help='Task ID')
    parser.add_argument('--status', required=True, help='Final task status')
    
    args = parser.parse_args()
    
    # Create cleanup manager
    cleanup_manager = McpClientCleanup(args.task_id, args.status)
    
    try:
        # Perform cleanup
        success = await cleanup_manager.perform_cleanup()
        
        if success:
            logger.info(f"MCP client cleanup completed successfully for task {args.task_id}")
            sys.exit(0)
        else:
            logger.error(f"MCP client cleanup failed for task {args.task_id}")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Unexpected error during cleanup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())