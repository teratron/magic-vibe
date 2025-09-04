---
description: Integration protocol rules for AI agents to connect with external systems, services, and standardized protocols.
globs: "*.md"
alwaysApply: false
---

# Integration Rules Index

This directory contains integration protocol rules that AI agents should apply when working with external systems, standardized protocols, and service integrations.

## Available Integration Rules

- **MCP (Model Context Protocol):** `@integrations/mcp.md` - Universal protocol for AI agents to connect with external tools, data sources, and services

## Rule Application

AI agents automatically detect integration requirements based on:

1. **Configuration Files:** `mcp.json`, `mcp.yaml`, API configuration files
2. **Project Dependencies:** Integration libraries and SDKs in package manifests
3. **Environment Variables:** Service credentials and endpoint configurations
4. **Documentation:** Integration setup guides and API references

## Integration Categories

### Protocol Standards

- **MCP (Model Context Protocol)**: Standardized client-server protocol for AI agent integrations
- **Future Protocols**: Space reserved for emerging AI integration standards

### Service Integrations

- Database connections and query interfaces
- External API integrations and authentication
- File system and storage service access
- Communication and notification services

## Detection Priority

When multiple integration protocols are detected:

1. **Protocol Standards**: Standardized protocols (MCP) take precedence
2. **Service-Specific**: Custom integrations for specific services
3. **Legacy Systems**: Backward compatibility integrations

## Integration with Core Rules

Integration rules work alongside Magic Vibe core rules and complement language and framework-specific rules. They provide the infrastructure layer that enables AI agents to access external capabilities safely and efficiently.

## Security and Performance

All integration rules emphasize:

- Secure authentication and authorization
- Input validation and sanitization
- Rate limiting and timeout management
- Error handling and graceful degradation
- Performance monitoring and optimization
