---
description: This rule explains how the agent should use the memory system to find context of the project.
globs:
alwaysApply: false
---

# AI Memory System

Whenever you use this rule, start your message with the following:

"Checking Magic Vibe memory..."

This project utilizes a memory system located in the `.magic-vibe/ai/memory/` directory to store a history of completed, failed, or superseded work, providing valuable context for ongoing development.
It archives both tasks and plans.

## Structure

The memory system consists of:

### Task Archive

- **`.magic-vibe/ai/memory/tasks/`**: This directory contains the full Markdown files (`task{id}_{descriptive_name}.md`) of tasks that have been archived (status: `completed` or `failed`). These files retain the original details, descriptions, and test strategies defined when the task was active.
- **`.magic-vibe/ai/memory/TASKS_LOG.md`**: This is an append-only Markdown file that serves as a chronological log of when tasks were archived. Each entry summarizes the archived task, including its ID, Title, final Status, Dependencies, and the Description extracted from the task file at the time of archival.

### Hook Log

- **`.magic-vibe/ai/memory/HOOKS_LOG.md`**: An append-only log file that records the execution of every hook. It provides a detailed, structured trace of all automated actions, including timestamps, success/failure status, commands executed, and their output. This is essential for debugging the automation system.

### Plan Archive

- **`.magic-vibe/ai/memory/plans/`**: This directory contains the full Markdown files of PRDs (both global `PLANS.md` versions and feature plans like `plan-{feature-name}.md`) that have been archived. Plans might be archived when they are completed (all associated features are implemented and stable), deprecated (the feature or project direction is abandoned), or superseded by a newer version of the plan.
- **`.magic-vibe/ai/memory/PLANS_LOG.md`**: This is an append-only Markdown file that serves as a chronological log of when plans were archived. Each entry should summarize the archived plan, including its **full path within the `.magic-vibe/ai/memory/plans/` directory** (e.g., `.magic-vibe/ai/memory/plans/plan-old-feature.md`), a version or date stamp, the reason for archival (e.g., Completed, Deprecated, Superseded), and a brief description or title of the plan.
- **Log Entry Format Example for PLANS_LOG.md:**

  ```markdown
  - **Archived Plan:** `.magic-vibe/ai/memory/plans/plan-old-feature.md`
    - **Archived On:** YYYY-MM-DD HH:MM:SS
    - **Reason:** Deprecated
    - **Title:** PRD: Old Feature
    - **Original File (Optional):** {.magic-vibe/ai/plans/features/plan-old-feature.md}
  ```

## Directory and File Management

When working with the memory system, the agent **must** adhere to the safe file system operation practices outlined in the `@tasks.md` rule. This includes checking for file/directory existence before operations, using `mv` for archival, and safely appending to log files. This ensures a consistent and safe approach across the entire Magic Vibe system.

## Directory Structure

```yaml
.magic-vibe/ai/
  memory/         # Parent directory for archive
    tasks/        # Archive for completed/failed task files
    plans/        # Archive for completed/failed plan files
    TASKS_LOG.md  # Append-only log of archived tasks
    PLANS_LOG.md  # Append-only log of archived plans
    HOOKS_LOG.md  # Append-only log of all hook executions
```

## Purpose and Usage

The memory system serves as the project's historical record of development activity and planning managed by the AI task system.

**When to Consult Memory:**

- **Understanding Past Implementations & Plans:** Before starting a new task or planning a new feature, consult the memory (`TASKS_LOG.md`, `PLANS_LOG.md`, and relevant archived files) to understand how similar or dependent features were built and planned.
- **Avoiding Redundancy:** Check if a similar task, requirement, or plan has been addressed previously.
- **Planning Related Features:** Review past tasks and plans for a feature to inform the planning and task breakdown of new, related features.
- **Investigating Failed Tasks:** If a task failed previously, reviewing its archived file (including the `error_log` in the YAML) can provide context.
- **Historical Context of Decisions:** Archived plans provide a snapshot of the project's goals, requirements, and intended direction at a particular point in time.

**How to Consult Memory:**

1. **Start with the Logs:** Read `.magic-vibe/ai/memory/TASKS_LOG.md` and `.magic-vibe/ai/memory/PLANS_LOG.md` to get a chronological overview of archived items. Identify potentially relevant tasks or plans based on their titles, descriptions, and reasons for archival.
2. **Dive into Archived Files:** If a log entry suggests an item is highly relevant, read the full archived file from its respective directory (`.magic-vibe/ai/memory/tasks/` or `.magic-vibe/ai/memory/plans/`) to get the complete details.

By leveraging this historical context, the AI can make more informed decisions, maintain consistency, and work more efficiently on the project.
