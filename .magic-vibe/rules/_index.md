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

## ⚠️ Critical Component Classification

**AI Agents must distinguish between Active and Informational components:**

### 🤖 Active Components (AI Interactive)

- **`@rules/`** - PRIMARY: Rule discovery system (THIS directory)
- **`@ai/`** - Generated workspace for active project management  
- **`@version-manager.sh`** - Version automation utility

### 📚 Informational Components (Human-Only)

- **`@docs/`** - PROHIBITED: Human documentation (DO NOT USE for development)
- **`@README.md`** - LIMITED: System introduction only

**Rule:** AI agents must NEVER use `@docs/` content for operational decisions or development guidance. Use only `@rules/` for all Magic Vibe functionality.

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
6. **To Apply Feature-Sliced Design:**
    - **Use Rule:** `@principles/feature-sliced-design.md`
    - **Action:** Organize frontend applications using layer-based architecture (app/pages/widgets/features/entities/shared) with strict import hierarchy.

## AI Agent Rule Discovery Protocol

**Initialization Message:** "Initializing Magic Vibe rule discovery..."

AI agents should follow this protocol for dynamic rule application:

### 1. Project Analysis Phase

Scan project files to detect:

**Programming Languages (by file extensions):**

```bash
# Scan first 50 files to avoid performance issues
find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" \) | head -50
```

**Frameworks (by dependencies and config files):**

- `package.json` → React, Vue, Next.js, TailwindCSS
- `requirements.txt` → FastAPI, Django, Flask
- `composer.json` → Laravel
- Config files: `next.config.*`, `vue.config.*`, `tailwind.config.*`

**Workflow Patterns (by project structure):**

- `.git` directory → Git workflows
- `.github/workflows` → GitHub Actions
- Quality tools: `.eslintrc.*`, `.pre-commit-config.yaml`

### 2. Rule Selection Phase

Based on detected context, automatically include:

| Detection | Rule Applied | Priority |
|-----------|--------------|----------|
| **Always** | `@core/*.md` | 1 (Highest) |
| **Python files** | `@languages/python.md` | 2 |
| **TypeScript files** | `@languages/typescript.md` | 2 |
| **React dependencies** | `@frameworks/react.md` | 3 |
| **FastAPI dependencies** | `@frameworks/fastapi.md` | 3 |
| **Git repository** | `@workflows/gitflow.md` | 4 |
| **Quality tools** | `@workflows/code-quality.md` | 4 |
| **Always** | `@principles/*.md` | 5 (Lowest) |

### 3. Rule Application Phase

Apply rules in priority order:

1. **Core system rules** (highest priority, always applied)
2. **Language-specific rules**
3. **Framework-specific rules**
4. **Workflow rules**
5. **Development principles** (lowest priority, but always applied)

### 4. Conflict Resolution Phase

When rules conflict:

- **Specificity Wins:** More specific rules override general ones
- **Priority Order:** Higher priority categories override lower priority  
- **Composition:** Combine complementary rules when possible
- **Documentation:** Log conflicts and resolutions in task notes

### Example Output

```text
Initializing Magic Vibe rule discovery...

Project Analysis:
- Languages: Python (25 files), TypeScript (12 files)
- Frameworks: FastAPI, React
- Workflows: Git, trunk-based development, code quality

Applying Rules (12 total):
✓ Core (7): tasks, plans, hooks, memory, expand, versioning, workflow
✓ Languages (2): python.md, typescript.md  
✓ Frameworks (2): fastapi.md, react.md
✓ Workflows (3): trunk-based-development.md, code-quality.md, commit-messages.md
✓ Principles (5): oop.md, solid.md, dry.md, kiss.md, yagni.md

Active Rule Set: 19 rules loaded and ready
```
