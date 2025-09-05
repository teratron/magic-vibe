# Magic Vibe Development Tools

> **⚠️ DEVELOPMENT UTILITIES - NOT FOR AI AGENTS**

This directory contains development utilities and scripts for **Magic Vibe system creators** only. These tools are NOT part of the core Magic Vibe rule system and should NOT be used by AI agents for project development.

## Purpose

These tools support Magic Vibe system development and maintenance:

- **Version Management**: Scripts for project versioning
- **Validation Tools**: Development-time validation utilities  
- **Build Helpers**: System build and deployment scripts
- **Quality Assurance**: Internal testing and validation

## Tool Categories

### Version Management

- `version-manager.sh` - Project and documentation version management

### Validation Tools

- `validate-fsd.sh` - FSD compliance validation (Bash)
- `validate-fsd.ps1` - FSD compliance validation (PowerShell)

## Usage Guidelines

### For Magic Vibe Creators

- Use these tools during system development
- Run validation scripts before committing changes
- Maintain cross-platform compatibility

### For AI Agents

- **DO NOT** reference these tools in project development
- **DO NOT** suggest these scripts to users
- **USE ONLY** `@rules/` directory for operational guidance

## Tool Development Standards

When creating new tools:

1. **Platform Support**: Provide both `.sh` (Unix) and `.ps1` (Windows) versions
2. **Documentation**: Include clear usage instructions
3. **Error Handling**: Implement robust error checking
4. **Isolation**: Keep tools independent of each other
5. **Testing**: Validate on multiple platforms

## Integration with Magic Vibe

These tools complement but do not replace the core Magic Vibe system:

- **Core System**: `@rules/` - AI operational rules
- **Documentation**: `@docs/` - Human reference
- **Tools**: `@tools/` - Development utilities (this directory)

Tools may reference and validate rules but should never be required for rule application.
