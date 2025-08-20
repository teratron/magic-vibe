---
description: Defines how the agent should discover and execute automated hooks (triggers) at specific points in the plan and task lifecycle.
globs:
  - .ai/hooks/**/*.hook.md
alwaysApply: false
---

# AI Hook Execution Rule

Whenever you use this rule, start your message with the following:

"Checking Task Magic hooks..."

This rule specifies the technical details for how an AI agent should discover, interpret, and execute automated hooks within the Task Magic system. Hooks allow for automated actions, such as running scripts or sending notifications, to be triggered by events like task completion or plan creation.

## Core Concepts

1. **Event-Driven Automation:** Hooks are actions that run automatically when a specific event occurs in the system (e.g., a task's status changes to `completed`).
2. **File-Based Definition:** Each hook is defined in its own Markdown file (`.hook.md`) located in the `.ai/hooks/` directory.
3. **Agent Responsibility:** The AI agent is solely responsible for detecting trigger events during its workflow, finding the corresponding hook files, and executing their defined actions.

## Directory Structure

All hook definition files **must** be located in the `.ai/hooks/` directory. The agent should check for the existence of this directory before attempting to find hooks.

```yaml
.ai/
  hooks/                                # Parent directory for all hook definitions
    commit-on-complete.hook.md          # Example: A hook that runs on task completion
    notify-on-fail.hook.md              # Example: A hook that sends a notification
    ...                                 # Other .hook.md files
```

## Hook File Format

Each hook is a Markdown file with a `.hook.md` extension. The file consists of YAML frontmatter for configuration and a Markdown body containing the hook's description and the action to be executed.

### YAML Frontmatter

The frontmatter defines the hook's behavior and trigger conditions.

```markdown
---
# The type of event that can trigger this hook.
# See "Hook Events and Triggers" section for all possible values.
type: task_status_change

# The specific event that triggers the action.
# For 'task_status_change', this is the new status (e.g., 'completed', 'failed').
# For other types, this might be 'created' or 'updated'.
trigger: completed

# Execution priority. Lower numbers execute first.
# Hooks with the same priority are executed in alphabetical order of their filenames.
priority: 10

# Whether the hook is active. The agent MUST ignore hooks where this is 'false'.
enabled: true
---
```

### Auto Git Commit on Task Completion

This hook automatically creates a git commit when a task is marked as completed, using the Conventional Commits format.

The commit type (`feat`, `fix`, `chore`, etc.) is dynamically determined by the `commit_type` property in the task's YAML frontmatter. If the property is not set, it defaults to `chore`. The task's `feature` property is used as the commit scope.

```bash
COMMIT_TYPE="{{task.commit_type}}"
COMMIT_SCOPE="{{task.feature}}"
git commit -am "${COMMIT_TYPE:-chore}(${COMMIT_SCOPE:-tasks}): {{task.title}} (task #{{task.id}})"
```

### Notification Hook

```markdown
---
type: task_status_change
trigger: failed
priority: 5
enabled: true
---
```

## Task Failure Notification

This hook sends a notification when a task is marked as failed:

```bash
echo "Task {{task.id}} - {{task.title}} has failed. See error log for details." | mail -s "Task Failure Alert" team@example.com
```

### Hook Variables

The following variables are available for use in hook actions:

- `{{task.id}}`: The ID of the task
- `{{task.title}}`: The title of the task
- `{{task.status}}`: The current status of the task
- `{{task.previous_status}}`: The previous status of the task (for status change hooks)
- `{{task.path}}`: The path to the task file
- `{{plan.id}}`: The ID of the associated plan
- `{{plan.title}}`: The title of the associated plan
- `{{plan.path}}`: The path to the plan file

### Hook Execution Order

Hooks are executed in order of priority (lower numbers execute first). If multiple hooks have the same priority, they are executed in alphabetical order by filename.

### Disabling Hooks

You can disable a hook by setting `enabled: false` in its YAML frontmatter. You can also disable all hooks by setting the `TASK_MAGIC_HOOKS_ENABLED` environment variable to `false`.

### Best Practices

1. **Keep hooks simple**: Each hook should do one thing well.
2. **Use descriptive filenames**: Name your hook files in a way that clearly indicates what they do.
3. **Set appropriate priorities**: Consider the order in which hooks should execute.
4. **Handle errors gracefully**: Make sure your hook actions can handle errors and won't break the Task Magic system if they fail.
5. **Document your hooks**: Include a clear description of what each hook does and when it should be triggered.
