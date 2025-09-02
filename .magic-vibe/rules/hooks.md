---
description: Defines how the agent should discover and execute automated hooks (triggers) at specific points in the plan, task, and git lifecycle.
globs: hooks/**/*.hook.md
alwaysApply: false
---

# AI Hook Execution Rule

Whenever you use this rule, start your message with the following:

"Checking Magic Vibe hooks..."

This rule specifies the technical details for how an AI agent should discover, interpret, and execute automated hooks within the Magic Vibe system. Hooks allow for automated actions, such as running scripts or sending notifications, to be triggered by events like task completion or plan creation.

## Core Concepts

1. **Event-Driven Automation:** Hooks are actions that run automatically when a specific event occurs in the system (e.g., a task's status changes to `completed`).
2. **Dual Directory System:** The Magic Vibe system uses two directories for hooks:
   - **System hooks** (`.magic-vibe/rules/hooks/`) - Core functionality for all users
   - **User template hooks** (`.magic-vibe/ai/hooks/`) - Customizable templates for specific projects
3. **File-Based Definition:** Each hook is defined in its own Markdown file (`.hook.md`) with YAML frontmatter for configuration.
4. **Agent Responsibility:** The AI agent is solely responsible for detecting trigger events during its workflow, finding the corresponding hook files from both directories, and executing their defined actions.

## Directory Structure

The Magic Vibe system uses two distinct directories for hook files, each serving a different purpose:

### System-Wide Hooks (`.magic-vibe/rules/hooks/`)

This directory contains **system-wide hooks** that are common to all users and essential for the overall operation of the Magic Vibe rule system. These hooks are:

- Part of the core system functionality
- Shared across all project implementations
- Maintained as part of the template repository
- Should not be modified by end users

```yaml
.magic-vibe/rules/
  hooks/                           # System-wide hooks directory
    comprehensive-docs.hook.md     # Core documentation generation
    generate-docs.hook.md          # Basic documentation automation
    update-project-docs.hook.md    # Project documentation updates
    version-management.hook.md     # Version tracking system
    ...                            # Other system hooks
```

### User Template Hooks (`.magic-vibe/ai/hooks/`)

This directory contains **user template hooks** that serve as examples and templates for custom user implementations. These hooks are:

- Templates and examples for user customization
- Project-specific implementations
- Can be modified, extended, or replaced by users
- Provide starting points for common automation patterns

```yaml
.magic-vibe/ai/
  hooks/                          # User template hooks directory
    run-tests-before-push.hook.md # Example: Quality gate hook
    slack-notify-on-fail.hook.md  # Example: Notification hook
    ...                           # Other template hooks
```

### Hook Discovery Priority

The AI agent should check for hooks in **both directories** with the following priority:

1. **System hooks** (`.magic-vibe/rules/hooks/`) are processed first
2. **User hooks** (`.magic-vibe/ai/hooks/`) are processed second
3. Hooks with the same priority are executed in alphabetical order within each directory

## Hook File Format

Each hook is a Markdown file with a `.hook.md` extension. The file consists of YAML frontmatter for configuration and a Markdown body containing the hook's description and the action to be executed.

### YAML Frontmatter

The frontmatter defines the hook's behavior and trigger conditions.

```yaml
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

### Markdown Body

The body of the file should contain:

1. A clear, human-readable title (H3 or similar).
2. A short description of what the hook does.
3. A **single** fenced code block containing the shell command to be executed. The agent will use the `run_terminal_cmd` tool to execute this command.

## Hook Events and Triggers

The agent must check for hooks whenever one of the following primary events occurs:

| `type` (in YAML)       | `trigger` (in YAML)                            | When to Check                                                                                                                                                  |
|------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `task_creation`        | `created`                                      | Immediately after a new task file (`task...md`) is successfully created in `.magic-vibe/ai/tasks/`.                                                            |
| `task_status_change`   | `pending`, `inprogress`, `completed`, `failed` | Immediately after a task's `status` field is changed in its YAML frontmatter.                                                                                  |
| `task_archival`        | `archived`                                     | Immediately after a task file is successfully moved from `.magic-vibe/ai/tasks/` to `.magic-vibe/ai/memory/tasks/`.                                            |
| `plan_creation`        | `created`                                      | Immediately after a new plan file (`plan-...md` or `plan-{id}-...md` or `PLANS.md`) is successfully created in `.magic-vibe/ai/plans/`.                        |
| `plan_update`          | `updated`                                      | Immediately after an existing plan file in `.magic-vibe/ai/plans/` is successfully modified.                                                                   |
| `git_commit`           | `after`                                        | Immediately after the agent successfully executes a `git commit` command.                                                                                      |
| `git_push`             | `before`, `after`                              | `before`: Immediately before the agent executes a `git push` command. A failing hook should stop the push. `after`: Immediately after a successful `git push`. |
| `documentation_update` | `generated`, `updated`                         | `generated`: After automatic documentation generation. `updated`: After manual documentation updates.                                                          |
| `project_milestone`    | `reached`                                      | When a significant project milestone is completed (multiple related tasks finished).                                                                           |

## Available Variables

When executing a hook's action, the agent **must** replace the following placeholder variables in the command string with the actual values from the event's context.

| Variable               | Description                                                   | Example Value                             | Available for...         |
|------------------------|---------------------------------------------------------------|-------------------------------------------|--------------------------|
| `{{task.id}}`          | The full ID of the task (e.g., `42` or `42.1`).               | `42.1`                                    | `task_*` events          |
| `{{task.title}}`       | The title of the task.                                        | `Implement User Login API`                | `task_*` events          |
| `{{task.status}}`      | The **current** status of the task.                           | `completed`                               | `task_*` events          |
| `{{task.commit_type}}` | The `commit_type` from the task's YAML (e.g., `feat`, `fix`). | `feat`                                    | `task_*` events          |
| `{{task.feature}}`     | The `feature` from the task's YAML.                           | `User Authentication`                     | `task_*` events          |
| `{{task.path}}`        | The full path to the task file.                               | `.magic-vibe/ai/tasks/task_42.1_login.md` | `task_*` events          |
| `{{plan.title}}`       | The title of the plan.                                        | `PRD: User Authentication`                | `plan_*` events          |
| `{{plan.path}}`        | The full path to the plan file.                               | `.magic-vibe/ai/plans/plan-42-auth.md`    | `plan_*` events          |
| `{{git.commit_hash}}`  | The full SHA hash of the latest commit.                       | `a1b2c3d4...`                             | `git_commit`, `git_push` |
| `{{git.branch}}`       | The current branch name.                                      | `feature/user-auth`                       | `git_commit`, `git_push` |
| `{{git.remote}}`       | The remote name for a push (e.g., `origin`).                  | `origin`                                  | `git_push`               |

**Note:** Variables are only available for their specified event types. For example, `task.*` variables are only available for `task_*` events.

## Agent Responsibilities: The Hook Execution Workflow

The agent **must** follow this precise workflow whenever a trigger event occurs:

1. **Identify Trigger Event:** Recognize that an action you just performed is a trigger event (e.g., "I have just changed the status of task `42.1` to `completed`" or "I am about to run `git push`").
2. **Discover Hooks:**
    - Check if the `.magic-vibe/rules/hooks/` directory exists. If it exists, list all files ending in `.hook.md` within it.
    - Check if the `.magic-vibe/ai/hooks/` directory exists. If it exists, list all files ending in `.hook.md` within it.
    - Combine both lists of hook files for processing.
3. **Filter and Sort Hooks:**
    - For each `.hook.md` file found in both directories:
        - Read the file content.
        - Parse its YAML frontmatter.
        - **Filter:** Keep only the hooks where `enabled: true` AND the `type` and `trigger` values exactly match the event that just occurred.
    - **Sort:** Sort the remaining, valid hooks in ascending order based on their `priority`. If priorities are equal, process system hooks (`.magic-vibe/rules/hooks/`) before user hooks (`.magic-vibe/ai/hooks/`), then sort alphabetically by filename within each directory.
4. **Execute Hooks in Order:**
    - For each sorted hook:
        - **Extract Action:** Get the shell command from the fenced code block in the hook's Markdown body.
        - **Substitute Variables:** Replace all `{{...}}` placeholders in the command string with the corresponding values from the context of the event.
        - **Execute:** Use the `run_terminal_cmd` tool to execute the final command string.
        - **Handle Errors:** If a hook command fails, log the error. For `before` triggers (like `git_push`), a failure **must** prevent the subsequent action (e.g., the `git push` command should not be executed). For other triggers, the agent should log the error and continue to the next hook.

## Example Hooks

### System Hook Example: Auto Git Commit on Task Completion

**File: `.magic-vibe/rules/hooks/commit-on-complete.hook.md`**

```yaml
---
description: Automatically commits changes to the repository when a task is marked as completed.
type: task_status_change
trigger: completed
priority: 10
enabled: true
---
```

### Auto Git Commit on Task Completion

This hook automatically creates a git commit when a task is marked as completed.

```bash
COMMIT_TYPE="{{task.commit_type}}"
COMMIT_SCOPE="{{task.feature}}"
git commit -am "${COMMIT_TYPE:-chore}(${COMMIT_SCOPE:-tasks}): {{task.title}} (task #{{task.id}})"
```

### User Template Hook Example: Notification Hook

**File: `.magic-vibe/ai/hooks/notify-on-fail.hook.md`**

```yaml
---
description: Notifies the team when a task fails.
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

### System Hook Example: Documentation Generation Hook

**File: `.magic-vibe/rules/hooks/generate-docs.hook.md`**

```yaml
---
description: Automatically generates project documentation in multiple languages when a task is completed.
type: task_status_change
trigger: completed
priority: 20
enabled: true
---
```

## Auto Documentation Generation

This hook automatically generates project documentation when a task is completed:

```bash
# Create docs directory structure
mkdir -p docs/en docs/ru

# Generate English documentation
cat > "docs/en/task-{{task.id}}-{{task.feature}}.md" << 'EOF'
# {{task.title}}

**Task ID:** {{task.id}}  
**Feature:** {{task.feature}}  
**Status:** {{task.status}}  
**Type:** {{task.commit_type}}

## Implementation Details

[Generated from task completion]

---

*Auto-generated by Magic Vibe*
EOF

# Generate Russian documentation
cat > "docs/ru/task-{{task.id}}-{{task.feature}}.md" << 'EOF'
# {{task.title}}

**Task ID:** {{task.id}}  
**Feature:** {{task.feature}}  
**Status:** {{task.status}}  
**Type:** {{task.commit_type}}

## Implementation Details

[Generated from task completion]

---

*Auto-generated by Magic Vibe*
EOF
```

## Hook Execution Order

Hooks are executed in order of priority (lower numbers execute first). If multiple hooks have the same priority, they are executed in alphabetical order by filename.

## Disabling Hooks

You can disable a hook by setting `enabled: false` in its YAML frontmatter. You can also disable all hooks by setting the `TASK_MAGIC_HOOKS_ENABLED` environment variable to `false`.

## Best Practices

### For System Hooks (`.magic-vibe/rules/hooks/`)

1. **Keep system-wide functionality**: Only include hooks that are essential for the Magic Vibe system operation.
2. **Maintain compatibility**: Ensure system hooks work across different project types and configurations.
3. **Use conservative priorities**: System hooks should typically use lower priority numbers (execute first).
4. **Document thoroughly**: System hooks should have comprehensive documentation since they affect all users.

### For User Template Hooks (`.magic-vibe/ai/hooks/`)

1. **Provide clear examples**: Template hooks should demonstrate common automation patterns.
2. **Keep templates simple**: Each template hook should do one thing well and be easy to understand.
3. **Include customization notes**: Document how users should modify the templates for their needs.
4. **Use descriptive filenames**: Name template files to clearly indicate their purpose and usage.

### General Hook Guidelines

1. **Set appropriate priorities**: Consider the order in which hooks should execute, with system hooks typically having precedence.
2. **Handle errors gracefully**: Make sure hook actions can handle errors and won't break the Magic Vibe system if they fail.
3. **Use environment variables**: For user-specific configuration (like API keys), use environment variables with clear documentation.
4. **Test hook interactions**: Ensure hooks work correctly when multiple hooks are triggered by the same event.
