---
description: Defines how hooks (triggers) work in the Task Magic system, allowing automated actions to be executed at specific points in the task lifecycle.
globs:
alwaysApply: false
---

# Task Magic Hooks

Hooks are special triggers in the Task Magic system that allow you to define automated actions that should occur at specific points in the task lifecycle.
They provide a way to extend the system's functionality and integrate with other tools and workflows.

## Hook Types

The Task Magic system supports the following hook types:

1. **Task Creation Hooks**: Triggered when a new task is created.
2. **Task Status Change Hooks**: Triggered when a task's status changes (e.g., from `pending` to `inprogress` or from `inprogress` to `completed`).
3. **Task Archival Hooks**: Triggered when a task is archived.
4. **Plan Creation Hooks**: Triggered when a new plan is created.
5. **Plan Update Hooks**: Triggered when an existing plan is updated.

## Hook Configuration

Hooks are defined in a `.ai/hooks/` directory in your project. Each hook is a separate file with a `.hook.md` extension. The file should contain:

1. **YAML Frontmatter**:

    ```yaml
    ---
    type: [hook type]
    trigger: [specific trigger event]
    priority: [numeric priority]
    enabled: [true/false]
    ---
    ```

2. **Hook Description**: A brief description of what the hook does.
3. **Hook Action**: The action to be performed when the hook is triggered. This can be:
   - A shell command to execute
   - A script to run
   - An AI agent instruction
   - A notification to send

## Example Hooks

### Git Commit Hook

```markdown
---
type: task_status_change
trigger: completed
priority: 10
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
