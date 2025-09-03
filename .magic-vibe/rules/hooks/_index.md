---
description: Hook system rules that define automated actions and event-driven workflow automation for AI agents in the Magic Vibe system.
globs: "*.hook.md"
alwaysApply: true
priority: 2
---

# Hook System Rules Index

This directory contains the core hook system rules that enable automated actions and event-driven workflow automation in the Magic Vibe system. These rules define how AI agents should discover, execute, and manage hooks.

## Available Hook System Rules

- **Hooks Management:** `@core/hooks.md` - Complete hook system implementation guide for AI agents
- **System-wide Hooks:** `.magic-vibe/rules/hooks/*.hook.md` - Core functionality hooks for all users
- **User Template Hooks:** `.magic-vibe/ai/hooks/*.hook.md` - Customizable example hooks for project-specific needs

## Hook System Architecture

The Magic Vibe hook system operates on two levels:

### System-Wide Hooks (`.magic-vibe/rules/hooks/`)

- **Purpose:** Core functionality for all users and rule systems
- **Scope:** Essential automation that should work across all projects
- **Examples:** Documentation generation, version management, quality gates
- **Maintenance:** Maintained as part of the Magic Vibe core system

### User Template Hooks (`.magic-vibe/ai/hooks/`)

- **Purpose:** Customizable examples for project-specific needs
- **Scope:** Project-specific automation patterns and templates
- **Examples:** Test execution, notifications, deployment triggers
- **Maintenance:** User-customizable and project-specific

## Hook Event Types

AI agents should recognize and handle these hook event types:

| Event Type | Trigger Conditions | Common Use Cases |
|------------|-------------------|------------------|
| `task_creation` | New task file created | Task validation, assignment notifications |
| `task_status_change` | Task status updated | Progress tracking, completion actions |
| `task_archival` | Task moved to memory | Cleanup, documentation generation |
| `plan_creation` | New plan file created | Plan validation, stakeholder notifications |
| `plan_update` | Existing plan modified | Change tracking, approval workflows |
| `git_commit` | After git commit | Code quality checks, documentation updates |
| `git_push` | Before/after git push | Deployment triggers, quality gates |
| `documentation_update` | Docs generated/updated | Version tracking, publication workflows |
| `project_milestone` | Major milestone reached | Reporting, celebration, planning |

## Hook Execution Protocol

AI agents must follow this execution protocol:

### 1. Event Detection

- Monitor Magic Vibe operations for trigger events
- Identify the specific event type and context
- Gather relevant data (task info, file paths, etc.)

### 2. Hook Discovery

- Scan `.magic-vibe/rules/hooks/` for system-wide hooks
- Scan `.magic-vibe/ai/hooks/` for user template hooks
- Filter hooks by event type and trigger conditions

### 3. Execution Order

- Sort hooks by priority (lower numbers execute first)
- Execute system-wide hooks before user hooks
- Process hooks with same priority alphabetically by filename

### 4. Variable Substitution

Replace template variables in hook commands:

- `{{task.id}}` - Task identifier
- `{{task.title}}` - Task title
- `{{task.status}}` - Current task status
- `{{plan.title}}` - Plan title
- `{{git.commit_hash}}` - Git commit hash
- And other context-specific variables

### 5. Error Handling

- Log hook execution results
- Handle failures gracefully
- For `before` triggers (e.g., git_push), failures should block the action
- For `after` triggers, log errors and continue

## Hook File Format

All hook files must follow this structure:

```yaml
---
description: Clear description of what this hook does
type: event_type (e.g., task_status_change)
trigger: specific_trigger (e.g., completed)
priority: number (lower executes first)
enabled: true/false
---
```

Followed by:

- Human-readable title and description
- Single fenced code block with shell command

## Integration with Magic Vibe Core

Hook system integration points:

- **Task Management:** Hooks trigger on task lifecycle events
- **Plan Management:** Hooks activate during plan creation and updates
- **Version Control:** Git-related hooks enhance development workflows
- **Documentation:** Hooks automate documentation generation and updates
- **Quality Assurance:** Hooks enforce quality gates and standards

## Best Practices for AI Agents

### Hook Development

1. **Single Purpose:** Each hook should perform one specific action
2. **Idempotent:** Hooks should be safe to run multiple times
3. **Error Resilient:** Handle failures gracefully without breaking workflows
4. **Well Documented:** Clear descriptions and usage examples

### Hook Management

1. **Priority Planning:** Assign priorities to control execution order
2. **Dependency Management:** Consider hook interactions and dependencies
3. **Testing:** Test hooks in isolation and as part of workflows
4. **Monitoring:** Log hook execution for debugging and optimization

### Performance Considerations

1. **Efficiency:** Keep hook execution time minimal
2. **Resource Usage:** Monitor system resource consumption
3. **Scalability:** Design hooks to work with projects of any size
4. **Caching:** Cache results when appropriate to improve performance

## Rule Application

Hook system rules are applied automatically when:

- AI agents detect trigger events during Magic Vibe operations
- Rules are referenced via `@core/hooks.md` in AI agent contexts
- Hook files are created or modified in the system
- Integration testing requires hook system validation

This ensures consistent and reliable automated workflow management across all Magic Vibe implementations.
