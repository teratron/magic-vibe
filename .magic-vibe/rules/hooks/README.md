# Hook System Rules

Hook system rules that enable automated actions and event-driven workflow automation for AI agents in the Magic Vibe system.

## Available Rules

- **[Hooks Management](../core/hooks.md)** - Complete hook system implementation guide for AI agents

## Hook Architecture

The Magic Vibe system uses a dual-level hook architecture:

### System-Wide Hooks

- **Location:** `.magic-vibe/rules/hooks/*.hook.md`
- **Purpose:** Core functionality for all users and projects
- **Examples:** Documentation generation, version management, quality gates

### User Template Hooks  

- **Location:** `.magic-vibe/ai/hooks/*.hook.md`
- **Purpose:** Customizable examples for project-specific automation
- **Examples:** Test execution, notifications, deployment triggers

## Auto-Execution

AI agents automatically execute hooks when trigger events occur during Magic Vibe operations, ensuring consistent workflow automation across all projects.

## Integration

Hook rules work seamlessly with all Magic Vibe components including task management, planning, version control, and documentation generation.
