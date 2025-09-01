---
description: Comprehensive overview of the Magic Vibe system, its components, and their interactions.
globs:
alwaysApply: true
---

# Magic Vibe System Overview

Whenever you use this rule, start your message with the following:

"Accessing Magic Vibe system overview..."

The Magic Vibe system is a file-based project management and AI agent operational framework designed to plan features, manage development tasks, and maintain a memory past work.
It consists of several components, each governed by its own detailed rule file. Use the specified rule for each action.

## Core System Components

1. **To Create or Update a Plan (PRD):**
    - **Use Rule:** `@plans.md`
    - **Action:** Generate or modify PRD files in `.magic-vibe/ai/plans/`. This is the first step for defining new features.
2. **To Create or Manage Tasks:**
    - **Use Rule:** `@tasks.md`
    - **Action:** Break down plans into actionable tasks. Create, update status, and manage dependencies of task files in `.magic-vibe/ai/tasks/`. Keep `.magic-vibe/ai/TASKS.md` synchronized.
3. **To Archive Old Tasks/Plans:**
    - **Use Rule:** `@memory.md`
    - **Action:** Move completed/failed items from active directories (`.magic-vibe/ai/tasks/`, `.magic-vibe/ai/plans/`) to the archive (`.magic-vibe/ai/memory/`) and update the corresponding log files.
4. **To Handle Automated Actions (Hooks):**
    - **Use Rule:** `@hooks.md`
    - **Action:** After performing a key action (like changing a task status or creating a plan), check for and execute any corresponding scripts defined in `.magic-vibe/ai/hooks/`. This rule defines all possible trigger events.
5. **To Decide if a Task is too big:**
    - **Use Rule:** `@expand.md`
    - **Action:** Analyze a task's complexity. If it's too large, use this rule to get a recommendation on how to split it into smaller sub-tasks.
6. **To Manage Versions:**
    - **Use Rule:** `@versioning.md`
    - **Action:** Handle automatic versioning for both project and documentation. The system automatically increments documentation versions on task completion and manages project versions through manual commands.

## Development Principles & Guidelines

1. **To Apply Object-Oriented Programming Principles:**
    - **Use Rule:** `@principles/oop.md`
    - **Action:** Ensure code follows fundamental OOP principles including encapsulation, inheritance, polymorphism, and abstraction.
2. **To Apply SOLID Design Principles:**
    - **Use Rule:** `@principles/solid.md`
    - **Action:** Follow the five SOLID principles (SRP, OCP, LSP, ISP, DIP) for maintainable and flexible software design.
3. **To Apply DRY Principle:**
    - **Use Rule:** `@principles/dry.md`
    - **Action:** Eliminate code duplication and ensure single source of truth for knowledge and logic.
4. **To Apply KISS Principle:**
    - **Use Rule:** `@principles/kiss.md`
    - **Action:** Keep code simple, clear, and maintainable by avoiding unnecessary complexity.
5. **To Apply YAGNI Principle:**
    - **Use Rule:** `@principles/yagni.md`
    - **Action:** Implement only what is currently needed, avoiding over-engineering and speculative features.
