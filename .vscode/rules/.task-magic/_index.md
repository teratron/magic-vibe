---
description:
globs:
alwaysApply: true
---

# Task Magic System Overview

Whenever you use this rule, start your message with the following:

"Accessing Task Magic system overview..."

The Task Magic system is a file-based project management and AI agent operational framework designed to plan features, manage development tasks, and maintain a memory of past work.
It consists of three main components, each governed by its own detailed rule file:

1. **Plans (`@plans.md`)**:
    - **Purpose**: Defines how Product Requirements Documents (PRDs) are created and structured for the overall project and specific features.
    - **Location**: PRDs are stored in `.ai/plans/`, with feature-specific plans in `.ai/plans/features/`.
    - **Key File**: A global `PLANS.md` is mandatory in `.ai/plans/`.
    - **Details**: For plan creation, fully review [plans.md](md:.vscode/rules/.task-magic/plans.md)
2. **Tasks (`@tasks.md`)**:
    - **Purpose**: Governs the creation, management, and lifecycle of individual development tasks.
    - **Active Tasks**: All active tasks reside in `.ai/tasks/` as `task{id}_name.md` files.
    - **Master View**: A master checklist, `.ai/TASKS.md`, mirrors the status of tasks in the `.ai/tasks/` directory and must be kept synchronized.
    - **Details**: For task creation, fully review [tasks.md](md:.vscode/rules/.task-magic/tasks.md)
3. **Memory (`@memory.md`)**:
    - **Purpose**: Archives completed and failed tasks to provide historical context.
    - **Location**: Archived task files are stored in `.ai/memory/tasks/`.
    - **Log File**: A chronological log of archived tasks is maintained in `.ai/memory/TASKS_LOG.md`.
    - **Details**: For storing to memory, full review [memory.md](md:.vscode/rules/.task-magic/memory.md)

This interconnected system allows for structured project development, from high-level planning to task execution and historical review, primarily managed through Markdown files and defined agent responsibilities.
