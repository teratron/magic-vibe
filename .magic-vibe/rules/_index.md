---
description: Comprehensive overview of the Magic Vibe system, its components, and their interactions with dynamic rule discovery.
globs:
alwaysApply: true
---

# Magic Vibe System Overview

Whenever you use this rule, start your message with the following:

"Accessing Magic Vibe system overview..."

The Magic Vibe system is a file-based project management and AI agent operational framework designed to plan features, manage development tasks, and maintain a memory past work.
It consists of several components, each governed by its own detailed rule file. The system now includes dynamic rule discovery for programming languages, frameworks, and workflows.

## Core System Components

1. **To Create or Update a Plan (PRD):**
    - **Use Rule:** `@core/plans.md`
    - **Action:** Generate or modify PRD files in `.magic-vibe/ai/plans/`. This is the first step for defining new features.
2. **To Create or Manage Tasks:**
    - **Use Rule:** `@core/tasks.md`
    - **Action:** Break down plans into actionable tasks. Create, update status, and manage dependencies of task files in `.magic-vibe/ai/tasks/`. Keep `.magic-vibe/ai/TASKS.md` synchronized.
3. **To Archive Old Tasks/Plans:**
    - **Use Rule:** `@core/memory.md`
    - **Action:** Move completed/failed items from active directories (`.magic-vibe/ai/tasks/`, `.magic-vibe/ai/plans/`) to the archive (`.magic-vibe/ai/memory/`) and update the corresponding log files.
4. **To Handle Automated Actions (Hooks):**
    - **Use Rule:** `@core/hooks.md`
    - **Action:** After performing a key action (like changing a task status or creating a plan), check for and execute any corresponding scripts defined in `.magic-vibe/rules/hooks/` and `.magic-vibe/ai/hooks/`. This rule defines all possible trigger events.
5. **To Decide if a Task is too big:**
    - **Use Rule:** `@core/expand.md`
    - **Action:** Analyze a task's complexity. If it's too large, use this rule to get a recommendation on how to split it into smaller sub-tasks.
6. **To Manage Versions:**
    - **Use Rule:** `@core/versioning.md`
    - **Action:** Handle automatic versioning for both project and documentation. The system automatically increments documentation versions on task completion and manages project versions through manual commands.
7. **To Manage Workflow Processes:**
    - **Use Rule:** `@core/workflow.md`
    - **Action:** Handle overall workflow management and process coordination across the Magic Vibe system.

## Dynamic Rule Discovery System

The Magic Vibe system automatically detects project context and applies relevant rules:

### Language-Specific Rules

When working with specific programming languages, the system automatically applies:

- **Python Projects:** `@languages/python.md`
- **TypeScript/JavaScript:** `@languages/typescript.md`
- **C++ Projects:** `@languages/cpp.md`
- **Rust Projects:** `@languages/rust.md`
- **Go Projects:** `@languages/go.md`
- **PHP Projects:** `@languages/php.md`

### Framework-Specific Rules

For framework-based development:

- **React Applications:** `@frameworks/react.md`
- **Vue.js Applications:** `@frameworks/vue.md`
- **Next.js Projects:** `@frameworks/nextjs.md`
- **FastAPI Projects:** `@frameworks/fastapi.md`
- **TailwindCSS:** `@frameworks/tailwindcss.md`
- **Svelte Applications:** `@frameworks/svelte.md`
- **SASS/SCSS Styling:** `@frameworks/sass.md`
- **Database Integration:** `@frameworks/database.md`
- **Laravel Framework:** `@frameworks/laravel.md`

### Workflow Rules

For development process management:

- **Git Workflow:** `@workflows/gitflow.md`
- **Trunk-Based Development:** `@workflows/trunk-based-development.md`
- **Commit Messages:** `@workflows/commit-messages.md`
- **Clean Code Practices:** `@workflows/clean-code.md`
- **Code Quality Standards:** `@workflows/code-quality.md`

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

## AI Agent Rule Discovery Protocol

AI agents should follow this protocol for dynamic rule application:

1. **Project Analysis:** Scan project files to detect:
   - Programming languages (by file extensions)
   - Frameworks (by package.json, requirements.txt, Cargo.toml, etc.)
   - Existing workflow patterns (by .git, CI/CD files)

2. **Rule Selection:** Based on detected context, automatically include:
   - Relevant language rules from `@languages/`
   - Applicable framework rules from `@frameworks/`
   - Appropriate workflow rules from `@workflows/`
   - Core Magic Vibe rules from `@core/`
   - Universal principles from `@principles/`

3. **Rule Precedence:** Apply rules in order:
   - Core system rules (highest priority)
   - Language-specific rules
   - Framework-specific rules
   - Workflow rules
   - Development principles (lowest priority, but always applied)

4. **Conflict Resolution:** When rules conflict:
   - More specific rules override general ones
   - Later rules in the precedence chain override earlier ones
   - Document conflicts in task notes for human review
