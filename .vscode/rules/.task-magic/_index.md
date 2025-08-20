---
description:
globs:
alwaysApply: true
---

# Task Magic System Overview

Whenever you use this rule, start your message with the following:

"Accessing Task Magic system overview..."

The Task Magic system is a file-based project management and AI agent operational framework designed to plan features, manage development tasks, and maintain a memory opast work.
It consists of several components, each governed by its own detailed rule file. Use the specified rule for each action.

## Core Components & Actions

1. **To Create or Update a Plan (PRD):**
    - **Use Rule:** `@plans.md`
    - **Action:** Generate or modify PRD files in `.ai/plans/`. This is the first step for defining new features.
2. **To Create or Manage Tasks:**
    - **Use Rule:** `@tasks.md`
    - **Action:** Break down plans into actionable tasks. Create, update status, and manage dependencies of task files in `.ai/tasks/`. Keep `.ai/TASKS.md` synchronized.
3. **To Archive Old Tasks/Plans:**
    - **Use Rule:** `@memory.md`
    - **Action:** Move completed/failed items from active directories (`.ai/tasks/`, `.ai/plans/`) to the archive (`.ai/memory/`) and update the corresponding log files.
4. **To Handle Automated Actions (Hooks):**
    - **Use Rule:** `@hooks.md`
    - **Action:** After performing a key action (like changing a task status or creating a plan), check for and execute any corresponding scripts defined in `.ai/hooks/`. This rule defines all possible trigger events.
5. **To Decide if a Task is too big:**
    - **Use Rule:** `@expand.md`
    - **Action:** Analyze a task's complexity. If it's too large, use this rule to get a recommendation on how to split it into smaller sub-tasks.
