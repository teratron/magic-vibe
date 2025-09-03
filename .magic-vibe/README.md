# Magic Vibe System

[![Magic Vibe](https://img.shields.io/badge/Magic%20Vibe-v2.1.0-orange.svg)](./.magic-vibe/)
[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)
[![Russian](https://img.shields.io/badge/Язык-Русский-red.svg)](README.ru.md)

> **Comprehensive AI Agent Workflow Management System with Dynamic Rule Discovery**

**Magic Vibe** is a file-based project management and AI agent operational framework designed to plan features, manage development tasks, and provide intelligent rule discovery for programming languages, frameworks, and workflows.

## 🎯 System Architecture

Magic Vibe now features a **dual-architecture system**:

### Core Magic Vibe System (`.magic-vibe/`)

File-based project management with intelligent rule discovery:

1. **Plans (`.magic-vibe/ai/plans/`)**:
   - Product Requirements Documents (PRDs) for feature definition
   - Global project overview and detailed feature specifications
   - AI-assisted plan generation and management

2. **Tasks (`.magic-vibe/ai/tasks/` & `.magic-vibe/ai/TASKS.md`)**:
   - Individual work items broken down from plans
   - Status tracking (pending, in progress, completed)
   - Dependency management and priority handling

3. **Memory (`.magic-vibe/ai/memory/`)**:
   - Archived completed and failed tasks/plans
   - Historical project knowledge base
   - AI learning and reference system

4. **Automated Hooks (`.magic-vibe/rules/hooks/` & `.magic-vibe/ai/hooks/`)**:
   - System-wide hooks for core functionality
   - User template hooks for project-specific automation
   - Event-driven workflow automation

### Dynamic Rule Discovery System (`.magic-vibe/rules/`)

Automatically detects project context and applies relevant rules:

- **Core Rules** (`@core/`) - Essential Magic Vibe functionality (always applied)
- **Language Rules** (`@languages/`) - Programming language-specific standards
- **Framework Rules** (`@frameworks/`) - Framework-specific patterns and practices
- **Workflow Rules** (`@workflows/`) - Development process standards
- **Development Principles** (`@principles/`) - Universal coding principles

## 🚀 Key Features

### Intelligent Context Detection

- **Automatic Language Detection:** Scans file extensions, config files, and project structure
- **Framework Recognition:** Identifies React, Vue, Next.js, FastAPI, and more
- **Workflow Analysis:** Detects Git patterns, CI/CD setup, and quality tools
- **Smart Rule Application:** Applies relevant rules based on detected context

### Comprehensive Rule Coverage

- **4 Programming Languages:** Python, TypeScript/JavaScript, C++, Rust
- **6+ Frameworks:** React, Vue, Next.js, FastAPI, TailwindCSS, Svelte
- **5 Workflow Standards:** Git, Trunk-based Development, Clean Code, Quality Assurance
- **5 Development Principles:** OOP, SOLID, DRY, KISS, YAGNI

### Rule Priority and Conflict Resolution

- **Hierarchical Application:** Core > Language > Framework > Workflow > Principles
- **Specificity Wins:** More specific rules override general ones
- **Intelligent Composition:** Rules complement rather than conflict
- **Transparent Resolution:** All conflicts documented and resolved systematically

## 📁 Directory Structure

```text
.magic-vibe/
├── rules/                      # Rule discovery system
│   ├── core/                    # Essential Magic Vibe rules (always applied)
│   │   ├── tasks.md             # Task management
│   │   ├── plans.md             # Planning and PRDs
│   │   ├── hooks.md             # Automation system
│   │   └── ...                  # Other core rules
│   ├── languages/               # Programming language rules
│   │   ├── python.md            # Python standards
│   │   ├── typescript.md        # TypeScript/JavaScript
│   │   └── ...                  # C++, Rust, etc.
│   ├── frameworks/              # Framework-specific rules
│   │   ├── react.md             # React patterns
│   │   ├── nextjs.md            # Next.js conventions
│   │   └── ...                  # Vue, FastAPI, etc.
│   ├── workflows/               # Development workflows
│   │   ├── gitflow.md           # Git workflows
│   │   ├── clean-code.md        # Code quality
│   │   └── ...                  # Other workflows
│   ├── principles/              # Development principles
│   ├── hooks/                   # System-wide automation hooks
│   └── _index.md               # Rule discovery overview
└── ai/                         # Active project workspace
    ├── tasks/                   # Current task files
    ├── plans/                   # Current plan files
    ├── hooks/                   # User template hooks
    └── memory/                  # Archived items
```

## 🤖 Working with AI Agents

Magic Vibe is designed for seamless AI agent integration:

### Automatic Rule Discovery

AI agents automatically:

1. **Scan Project Context:** Detect languages, frameworks, and workflows
2. **Select Applicable Rules:** Choose relevant rules based on project analysis
3. **Apply Rule Hierarchy:** Execute rules in priority order with conflict resolution
4. **Report Active Rules:** Inform users which rules are being applied

### Manual Rule Guidance

For specific control, use @-tags:

- `@.magic-vibe/rules/core/tasks.md` - Core task management
- `@.magic-vibe/rules/languages/python.md` - Python-specific rules
- `@.magic-vibe/rules/frameworks/react.md` - React development patterns
- `@.magic-vibe/rules/workflows/clean-code.md` - Code quality standards

### Context Integration

- **Automatic Context:** `_index.md` files provide system overviews
- **On-demand Rules:** Specific rule files loaded when relevant
- **Dynamic Adaptation:** Rules adapt to project changes and growth

## 🚀 Getting Started

### 1. Initialize Magic Vibe Structure

```bash
# AI agents will create these automatically, or create manually:
mkdir -p .magic-vibe/ai/{plans,tasks,memory,hooks}
touch .magic-vibe/ai/PLANS.md
touch .magic-vibe/ai/TASKS.md
touch .magic-vibe/ai/memory/TASKS_LOG.md
```

### 2. Let AI Discover Your Project

```text
Initialize Magic Vibe system for this project
```

***AI will scan and report detected languages, frameworks, and applicable rules***

### 3. Create Your First Plan

```text
@.magic-vibe/rules/core/plans.md create a plan for user authentication
```

### 4. Generate Tasks from Plans

```text
@.magic-vibe/rules/core/tasks.md generate tasks for the authentication plan
```

### 5. Start Development

```text
Start working on the first authentication task
```

***AI will apply relevant language and framework rules automatically***

## 🔗 Integration with VS Code Rules

Magic Vibe complements existing `.vscode/rules/` systems:

- **Unified Standards:** Consistent rules across AI editors
- **Template Compatibility:** Works with Cursor, Windsurf, and other AI IDEs
- **Migration Support:** Smooth transition from .vscode-based rules
- **Cross-Editor Portability:** Rules work across different development environments

## 📚 Documentation

- **English:** [README.md](README.md) (this file)
- **Russian:** [README.ru.md](README.ru.md)
- **Rule Categories:**
  - [Core Rules](rules/core/README.md)
  - [Language Rules](rules/languages/README.md)
  - [Framework Rules](rules/frameworks/README.md)
  - [Workflow Rules](rules/workflows/README.md)
  - [Development Principles](rules/principles/README.md)

---

***Magic Vibe System v2.1.0** - Intelligent AI Agent Workflow Management*

*Based on [Task Magic](https://github.com/iannuttall/task-magic) with comprehensive enhancements for modern AI-assisted development.*
