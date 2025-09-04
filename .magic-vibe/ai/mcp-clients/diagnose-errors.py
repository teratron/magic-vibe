#!/usr/bin/env python3
"""
MCP Error Diagnosis and Recovery System

This script provides comprehensive error analysis and recovery mechanisms
for failed MCP client connections and task executions.
"""

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

class McpErrorDiagnostic:
    """Provides comprehensive MCP error analysis and recovery suggestions."""
    
    def __init__(self, task_id: str, error: str):
        self.task_id = task_id
        self.error = error
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
    
    def analyze_error(self) -> Dict[str, Any]:
        """Analyze the error and provide diagnostic information."""
        error_analysis = {
            'taskId': self.task_id,
            'originalError': self.error,
            'analysisTimestamp': datetime.utcnow().isoformat() + 'Z',
            'errorCategory': self._categorize_error(),
            'rootCause': self._identify_root_cause(),
            'affectedClients': self._identify_affected_clients(),
            'recommendedActions': self._get_recovery_actions(),
            'systemDiagnostics': self._perform_system_diagnostics()
        }
        
        return error_analysis
    
    def _categorize_error(self) -> str:
        """Categorize the error based on patterns."""
        error_lower = self.error.lower()
        
        if any(keyword in error_lower for keyword in ['connection', 'connect', 'timeout', 'unreachable']):
            return 'connection_error'
        elif any(keyword in error_lower for keyword in ['permission', 'access', 'denied', 'unauthorized']):
            return 'permission_error'
        elif any(keyword in error_lower for keyword in ['not found', '404', 'missing']):
            return 'resource_not_found'
        elif any(keyword in error_lower for keyword in ['syntax', 'json', 'parse', 'format']):
            return 'format_error'
        elif any(keyword in error_lower for keyword in ['memory', 'limit', 'resource']):
            return 'resource_exhaustion'
        elif any(keyword in error_lower for keyword in ['ssl', 'tls', 'certificate']):
            return 'security_error'
        else:
            return 'unknown_error'
    
    def _identify_root_cause(self) -> str:
        """Identify the likely root cause of the error."""
        error_category = self._categorize_error()
        
        root_causes = {
            'connection_error': 'MCP server may be down, network issues, or incorrect server configuration',
            'permission_error': 'Insufficient permissions or invalid credentials for MCP server access',
            'resource_not_found': 'MCP server endpoint or required resources are missing',
            'format_error': 'Invalid configuration format or corrupted data structures',
            'resource_exhaustion': 'System resources (memory, CPU, file handles) are exhausted',
            'security_error': 'SSL/TLS configuration issues or certificate problems',
            'unknown_error': 'Error pattern not recognized, requires manual investigation'
        }
        
        return root_causes.get(error_category, 'Unknown root cause')
    
    def _identify_affected_clients(self) -> List[str]:
        """Identify which MCP clients are affected by the error."""
        affected_clients = []
        
        mcp_clients = self.config.get('mcpClients', {})
        for client_name, client_info in mcp_clients.items():
            if client_info.get('status') == 'unhealthy' or client_info.get('status') == 'failed':
                affected_clients.append(client_name)
        
        # If no specific clients are marked as failed, assume all are affected
        if not affected_clients and mcp_clients:
            affected_clients = list(mcp_clients.keys())
        
        return affected_clients
    
    def _get_recovery_actions(self) -> List[str]:
        """Get recommended recovery actions based on error category."""
        error_category = self._categorize_error()
        
        recovery_actions = {
            'connection_error': [
                'Check MCP server status and availability',
                'Verify network connectivity and firewall settings',
                'Restart MCP servers if necessary',
                'Implement retry mechanism with exponential backoff',
                'Check server logs for additional error details'
            ],
            'permission_error': [
                'Verify MCP server credentials and API keys',
                'Check file system permissions for MCP server access',
                'Ensure proper environment variables are set',
                'Review server access control configurations',
                'Check user account permissions and roles'
            ],
            'resource_not_found': [
                'Verify MCP server endpoints and URLs',
                'Check if required MCP server tools are installed',
                'Ensure MCP server configuration files exist',
                'Validate server capability declarations',
                'Check server registration and discovery'
            ],
            'format_error': [
                'Validate JSON configuration file syntax',
                'Check for proper data type conversions',
                'Verify MCP protocol message formats',
                'Review encoding and character set issues',
                'Regenerate configuration files if corrupted'
            ],
            'resource_exhaustion': [
                'Monitor system resource usage (CPU, memory, disk)',
                'Increase system resource limits if possible',
                'Implement connection pooling and cleanup',
                'Optimize MCP client initialization timing',
                'Add resource monitoring and alerting'
            ],
            'security_error': [
                'Check SSL/TLS certificate validity and expiration',
                'Verify certificate chain and trust store',
                'Update security protocols and cipher suites',
                'Review firewall and security group settings',
                'Check for certificate authority issues'
            ],
            'unknown_error': [
                'Enable detailed debug logging for MCP clients',
                'Collect comprehensive error logs and stack traces',
                'Review recent system and configuration changes',
                'Test MCP connections in isolation',
                'Consult MCP server documentation and community'
            ]
        }
        
        return recovery_actions.get(error_category, ['Manual investigation required'])
    
    def _perform_system_diagnostics(self) -> Dict[str, Any]:
        """Perform system-level diagnostics."""
        diagnostics = {
            'pythonVersion': sys.version,
            'workingDirectory': os.getcwd(),
            'environmentVariables': self._get_relevant_env_vars(),
            'fileSystemStatus': self._check_filesystem(),
            'networkConnectivity': self._check_network(),
            'mcpServerStatus': self._check_mcp_servers()
        }
        
        return diagnostics
    
    def _get_relevant_env_vars(self) -> Dict[str, str]:
        """Get relevant environment variables."""
        relevant_vars = [
            'DB_CONNECTION_STRING', 'GITHUB_TOKEN', 'API_KEY', 'API_BASE_URL',
            'ALLOWED_PATHS', 'MCP_LOG_LEVEL', 'PATH', 'PYTHONPATH'
        ]
        
        return {var: os.getenv(var, 'Not set') for var in relevant_vars}
    
    def _check_filesystem(self) -> Dict[str, Any]:
        """Check filesystem status and permissions."""
        filesystem_status = {
            'mcpClientsDir': os.path.exists('.magic-vibe/ai/mcp-clients'),
            'taskConfigExists': os.path.exists(self.config_path),
            'writePermissions': os.access('.magic-vibe/ai/mcp-clients', os.W_OK),
            'diskSpace': 'Unable to check'  # Could add actual disk space check
        }
        
        return filesystem_status
    
    def _check_network(self) -> Dict[str, Any]:
        """Check basic network connectivity."""
        network_status = {
            'localhost': self._test_connection('127.0.0.1', 80),
            'internetAccess': self._test_connection('8.8.8.8', 53),
            'dnsResolution': 'Unable to check'  # Could add DNS check
        }
        
        return network_status
    
    def _test_connection(self, host: str, port: int) -> bool:
        """Test basic network connection."""
        try:
            import socket
            sock = socket.create_connection((host, port), timeout=5)
            sock.close()
            return True
        except Exception:
            return False
    
    def _check_mcp_servers(self) -> Dict[str, str]:
        """Check status of configured MCP servers."""
        server_status = {}
        
        mcp_clients = self.config.get('mcpClients', {})
        for client_name, client_info in mcp_clients.items():
            command = client_info.get('config', {}).get('command', 'unknown')
            server_status[client_name] = f"Command: {command}, Status: {client_info.get('status', 'unknown')}"
        
        return server_status
    
    def generate_diagnostic_report(self):
        """Generate comprehensive diagnostic report."""
        logger.info(f"Generating diagnostic report for task {self.task_id}")
        
        try:
            error_analysis = self.analyze_error()
            
            # Save diagnostic report
            report_path = f".magic-vibe/ai/mcp-clients/{self.task_id}/diagnostic-report.json"
            with open(report_path, 'w') as f:
                json.dump(error_analysis, f, indent=2)
            
            logger.info(f"Diagnostic report saved to {report_path}")
            
            # Log key findings
            logger.info(f"Error category: {error_analysis['errorCategory']}")
            logger.info(f"Root cause: {error_analysis['rootCause']}")
            logger.info(f"Affected clients: {error_analysis['affectedClients']}")
            
            return error_analysis
            
        except Exception as e:
            logger.error(f"Failed to generate diagnostic report: {e}")
            return None

def main():
    """Main entry point for MCP error diagnosis."""
    parser = argparse.ArgumentParser(description='Diagnose MCP client errors')
    parser.add_argument('--task-id', required=True, help='Task ID')
    parser.add_argument('--error', required=True, help='Error message')
    
    args = parser.parse_args()
    
    # Create diagnostic manager
    diagnostic = McpErrorDiagnostic(args.task_id, args.error)
    
    try:
        # Generate diagnostic report
        report = diagnostic.generate_diagnostic_report()
        
        if report:
            logger.info(f"Error diagnosis completed for task {args.task_id}")
        else:
            logger.error(f"Error diagnosis failed for task {args.task_id}")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Unexpected error during diagnosis: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()