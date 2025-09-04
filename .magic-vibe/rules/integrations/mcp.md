---
description: Model Context Protocol (MCP) integration rules for AI agents to connect with external systems, tools, and data sources using standardized protocols.
globs: "mcp.json,mcp.yaml,mcp-server.py,mcp-client.js,*.mcp.*"
alwaysApply: false
priority: 3
---

# Model Context Protocol (MCP) Integration Rules

Model Context Protocol (MCP) is an open standard that defines a universal client-server protocol for connecting AI agents with external capabilities and data sources. Think of it as "USB-C for AI" - a standardized way to enable AI agents to interact with tools, databases, APIs, and services.

## Core MCP Concepts

### Protocol Components

- **Host**: The user-facing AI application (LLM, IDE, or custom agent)
- **Client**: Component within the host that manages MCP server communication
- **Server**: Lightweight component exposing external capabilities via MCP protocol

### MCP Capabilities

- **Tools**: Executable functions (file operations, API calls, database queries)
- **Resources**: Data sources (documents, vector databases, knowledge bases)
- **Prompts**: Reusable prompt templates and instruction sets
- **Sampling**: Server requests to host for specific computations or reasoning

## MCP Server Development

### Server Structure

```python
# mcp-server.py
from mcp import McpServer, Tool, Resource
from mcp.types import TextContent, ImageContent

class CustomMcpServer(McpServer):
    def __init__(self):
        super().__init__("custom-server", "1.0.0")
        self.register_tools()
        self.register_resources()
    
    def register_tools(self):
        @self.tool("search_files")
        async def search_files(query: str, path: str = ".") -> str:
            """Search for files containing specific content."""
            try:
                results = self._search_implementation(query, path)
                return f"Found {len(results)} files matching '{query}'"
            except Exception as e:
                return f"Error searching files: {str(e)}"
        
        @self.tool("execute_query")
        async def execute_query(sql: str, database: str) -> str:
            """Execute SQL query against specified database."""
            return self._safe_query_execution(sql, database)
    
    def register_resources(self):
        @self.resource("documentation")
        async def get_documentation(uri: str) -> Resource:
            """Provide access to project documentation."""
            content = self._load_documentation(uri)
            return Resource(
                uri=uri,
                content=TextContent(text=content),
                mimeType="text/markdown"
            )

if __name__ == "__main__":
    server = CustomMcpServer()
    server.run()
```

### Configuration File

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "python",
      "args": ["mcp-filesystem-server.py"],
      "env": {
        "ALLOWED_PATHS": "/workspace,/home/user/projects"
      }
    },
    "database": {
      "command": "mcp-database-server",
      "args": ["--config", "db-config.json"],
      "env": {
        "DB_CONNECTION_STRING": "${DB_URL}"
      }
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## MCP Client Integration

### Client Implementation

```javascript
// mcp-client.js
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';

class McpClient {
    constructor() {
        this.clients = new Map();
    }

    async connectToServer(serverName, command, args = []) {
        try {
            const transport = new StdioClientTransport({
                command,
                args,
                env: process.env
            });

            const client = new Client({
                name: `client-${serverName}`,
                version: "1.0.0"
            }, {
                capabilities: {
                    tools: {},
                    resources: {}
                }
            });

            await client.connect(transport);
            this.clients.set(serverName, client);
            
            console.log(`Connected to MCP server: ${serverName}`);
            return client;
        } catch (error) {
            console.error(`Failed to connect to ${serverName}:`, error);
            throw error;
        }
    }

    async callTool(serverName, toolName, args = {}) {
        const client = this.clients.get(serverName);
        if (!client) {
            throw new Error(`No client connected for server: ${serverName}`);
        }

        try {
            const result = await client.callTool({
                name: toolName,
                arguments: args
            });
            return result;
        } catch (error) {
            console.error(`Tool call failed: ${toolName}`, error);
            throw error;
        }
    }

    async getResource(serverName, uri) {
        const client = this.clients.get(serverName);
        if (!client) {
            throw new Error(`No client connected for server: ${serverName}`);
        }

        try {
            const resource = await client.readResource({ uri });
            return resource;
        } catch (error) {
            console.error(`Resource access failed: ${uri}`, error);
            throw error;
        }
    }
}
```

## Security Best Practices

### Server Security

```python
# Secure server implementation
import os
from pathlib import Path
from typing import List, Optional

class SecureMcpServer(McpServer):
    def __init__(self, allowed_paths: List[str]):
        super().__init__("secure-server", "1.0.0")
        self.allowed_paths = [Path(p).resolve() for p in allowed_paths]
    
    def _validate_path(self, path: str) -> bool:
        """Validate that path is within allowed directories."""
        try:
            resolved_path = Path(path).resolve()
            return any(
                resolved_path.is_relative_to(allowed) 
                for allowed in self.allowed_paths
            )
        except Exception:
            return False
    
    def _sanitize_sql(self, sql: str) -> str:
        """Basic SQL sanitization - use proper ORM in production."""
        dangerous_keywords = ['DROP', 'DELETE', 'UPDATE', 'INSERT', 'ALTER']
        sql_upper = sql.upper()
        for keyword in dangerous_keywords:
            if keyword in sql_upper:
                raise ValueError(f"Dangerous SQL keyword detected: {keyword}")
        return sql
    
    @tool("safe_file_read")
    async def safe_file_read(self, path: str) -> str:
        """Safely read file content with path validation."""
        if not self._validate_path(path):
            raise ValueError(f"Access denied: path outside allowed directories")
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
```

### Environment Configuration

```bash
# .env file for MCP servers
MCP_LOG_LEVEL=INFO
MCP_ALLOWED_PATHS="/workspace,/home/user/projects"
MCP_MAX_FILE_SIZE=10485760  # 10MB
MCP_TIMEOUT_SECONDS=30
MCP_RATE_LIMIT_PER_MINUTE=100

# Database access (if applicable)
MCP_DB_READ_ONLY=true
MCP_DB_QUERY_TIMEOUT=15
MCP_DB_MAX_ROWS=1000
```

## Framework Integration

### LangChain Integration

```python
from langchain.tools import BaseTool
from langchain.agents import AgentExecutor
from mcp import McpClient

class McpTool(BaseTool):
    name: str
    description: str
    mcp_client: McpClient
    server_name: str
    tool_name: str
    
    def _run(self, **kwargs) -> str:
        try:
            result = self.mcp_client.call_tool(
                self.server_name, 
                self.tool_name, 
                kwargs
            )
            return str(result)
        except Exception as e:
            return f"MCP tool error: {str(e)}"

# Create MCP-powered agent
mcp_tools = [
    McpTool(
        name="file_search",
        description="Search for files in the project",
        mcp_client=mcp_client,
        server_name="filesystem",
        tool_name="search_files"
    ),
    McpTool(
        name="database_query",
        description="Execute read-only database queries",
        mcp_client=mcp_client,
        server_name="database",
        tool_name="execute_query"
    )
]
```

### CrewAI Integration

```python
from crewai import Agent, Task, Crew
from crewai.tools import BaseTool

class McpCrewTool(BaseTool):
    name: str = "mcp_tool"
    description: str = "Access external systems via MCP"
    
    def __init__(self, mcp_client: McpClient, server_name: str, tool_name: str):
        super().__init__()
        self.mcp_client = mcp_client
        self.server_name = server_name
        self.tool_name = tool_name
    
    def _run(self, **kwargs):
        return self.mcp_client.call_tool(
            self.server_name, 
            self.tool_name, 
            kwargs
        )

# Create specialized agents with MCP tools
researcher = Agent(
    role='Research Analyst',
    goal='Gather and analyze information from various sources',
    tools=[
        McpCrewTool(mcp_client, "filesystem", "search_files"),
        McpCrewTool(mcp_client, "github", "search_repositories")
    ]
)
```

## IDE and Editor Integration

### VS Code Extension

```typescript
// vscode-mcp-extension.ts
import * as vscode from 'vscode';
import { McpClient } from './mcp-client';

export class McpExtension {
    private mcpClient: McpClient;
    
    constructor(context: vscode.ExtensionContext) {
        this.mcpClient = new McpClient();
        this.initializeServers();
        this.registerCommands(context);
    }
    
    private async initializeServers() {
        const config = vscode.workspace.getConfiguration('mcp');
        const servers = config.get<any>('servers', {});
        
        for (const [name, serverConfig] of Object.entries(servers)) {
            await this.mcpClient.connectToServer(
                name, 
                serverConfig.command, 
                serverConfig.args
            );
        }
    }
    
    private registerCommands(context: vscode.ExtensionContext) {
        const searchCommand = vscode.commands.registerCommand(
            'mcp.searchFiles', 
            async () => {
                const query = await vscode.window.showInputBox({
                    prompt: 'Enter search query'
                });
                
                if (query) {
                    const result = await this.mcpClient.callTool(
                        'filesystem', 
                        'search_files', 
                        { query }
                    );
                    
                    vscode.window.showInformationMessage(
                        `Search completed: ${result}`
                    );
                }
            }
        );
        
        context.subscriptions.push(searchCommand);
    }
}
```

## Testing and Validation

### Server Testing

```python
import pytest
import asyncio
from mcp.test_utils import MockTransport

@pytest.mark.asyncio
async def test_mcp_server_tools():
    server = CustomMcpServer()
    transport = MockTransport()
    
    # Test tool registration
    tools = await server.list_tools()
    assert "search_files" in [tool.name for tool in tools]
    
    # Test tool execution
    result = await server.call_tool("search_files", {
        "query": "test",
        "path": "./test_directory"
    })
    
    assert "Found" in result
    assert "files matching" in result

@pytest.mark.asyncio
async def test_mcp_client_connection():
    client = McpClient()
    
    # Test server connection
    await client.connectToServer(
        "test-server", 
        "python", 
        ["test-mcp-server.py"]
    )
    
    # Test tool call
    result = await client.callTool("test-server", "ping", {})
    assert result is not None
```

### Integration Testing

```python
def test_mcp_langchain_integration():
    """Test MCP integration with LangChain agents."""
    mcp_tool = McpTool(
        name="test_tool",
        description="Test MCP tool",
        mcp_client=test_mcp_client,
        server_name="test-server",
        tool_name="test_function"
    )
    
    result = mcp_tool.run(test_param="test_value")
    assert result is not None
    assert "error" not in result.lower()
```

## Monitoring and Debugging

### Logging Configuration

```python
import logging
from mcp.logging import setup_mcp_logging

# Configure MCP logging
setup_mcp_logging(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mcp-server.log'),
        logging.StreamHandler()
    ]
)

class MonitoredMcpServer(McpServer):
    def __init__(self):
        super().__init__("monitored-server", "1.0.0")
        self.logger = logging.getLogger(__name__)
        self.call_count = 0
        self.error_count = 0
    
    async def call_tool(self, name: str, arguments: dict):
        self.call_count += 1
        self.logger.info(f"Tool call: {name} (total calls: {self.call_count})")
        
        try:
            result = await super().call_tool(name, arguments)
            return result
        except Exception as e:
            self.error_count += 1
            self.logger.error(f"Tool error: {name} - {str(e)}")
            raise
```

## Best Practices

### Development Guidelines

1. **Server Design**:
   - Keep servers lightweight and focused on specific capabilities
   - Implement proper error handling and validation
   - Use async/await for I/O operations
   - Provide clear tool descriptions and parameter documentation

2. **Security Considerations**:
   - Validate all inputs and file paths
   - Implement rate limiting and timeout mechanisms
   - Use environment variables for sensitive configuration
   - Follow principle of least privilege for system access

3. **Performance Optimization**:
   - Cache frequently accessed resources
   - Implement connection pooling for database servers
   - Use streaming for large data transfers
   - Monitor and log performance metrics

4. **Error Handling**:
   - Provide meaningful error messages
   - Implement graceful degradation
   - Log errors with sufficient context
   - Handle network timeouts and connection failures

### Code Quality Standards

- Follow MCP protocol specifications strictly
- Write comprehensive tests for all tools and resources
- Document all server capabilities and usage examples
- Implement proper logging and monitoring
- Use type hints and proper error handling
- Maintain backward compatibility when updating servers

This MCP integration enables AI agents to seamlessly connect with external systems while maintaining security, performance, and reliability standards essential for production environments.
