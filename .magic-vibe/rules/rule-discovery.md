---
description: AI Agent Rule Discovery System - Automated context detection and rule application for dynamic project adaptation.
globs: 
alwaysApply: true
priority: 1
---

# AI Agent Rule Discovery System

Whenever you use this rule, start your message with the following:

"Initializing Magic Vibe rule discovery..."

This document defines how AI agents should automatically discover and apply the appropriate rules based on project context, enabling dynamic adaptation to different programming languages, frameworks, and workflows.

## Discovery Algorithm Overview

The rule discovery system operates in four phases:

1. **Project Scanning** - Analyze project structure and files
2. **Context Detection** - Identify languages, frameworks, and workflows
3. **Rule Selection** - Choose applicable rules based on detected context
4. **Rule Application** - Apply rules in priority order with conflict resolution

## Phase 1: Project Scanning

### File System Analysis

```bash
# Scan for programming languages (first 50 files to avoid performance issues)
find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx" -o -name "*.jsx" -o -name "*.cpp" -o -name "*.hpp" -o -name "*.rs" -o -name "*.go" -o -name "*.php" -o -name "*.java" -o -name "*.c" -o -name "*.h" \) | head -50

# Scan for package managers and build files
find . -maxdepth 3 -type f \( -name "package.json" -o -name "requirements.txt" -o -name "Cargo.toml" -o -name "CMakeLists.txt" -o -name "pyproject.toml" -o -name "go.mod" -o -name "composer.json" -o -name "pom.xml" \)

# Scan for framework indicators
find . -maxdepth 3 -type f \( -name "next.config.*" -o -name "vue.config.*" -o -name "svelte.config.*" -o -name "tailwind.config.*" -o -name "vite.config.*" \)

# Scan for workflow indicators
find . -maxdepth 2 -type d \( -name ".git" -o -name ".github" -o -name ".gitlab" \)
find . -maxdepth 3 -type f \( -name ".gitignore" -o -name ".pre-commit-config.yaml" -o -name "tox.ini" -o -name "pytest.ini" \)
```

### Configuration File Analysis

Priority files to analyze for context detection:

| File               | Language/Framework    | Information Extracted                      |
|--------------------|-----------------------|--------------------------------------------|
| `package.json`     | JavaScript/TypeScript | Dependencies, scripts, framework detection |
| `requirements.txt` | Python                | Package dependencies                       |
| `pyproject.toml`   | Python                | Modern Python project configuration        |
| `Cargo.toml`       | Rust                  | Dependencies and project metadata          |
| `CMakeLists.txt`   | C++                   | Build configuration and dependencies       |
| `go.mod`           | Go                    | Module dependencies                        |
| `composer.json`    | PHP                   | Package dependencies                       |
| `composer.json`    | PHP                   | Package dependencies                       |

## Phase 2: Context Detection

### Language Detection Logic

```python
def detect_languages(project_files):
    language_scores = {}
    
    # File extension mapping
    extensions = {
        '.py': 'python',
        '.js': 'javascript', 
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.jsx': 'javascript',
        '.cpp': 'cpp',
        '.hpp': 'cpp',
        '.rs': 'rust',
        '.go': 'go',
        '.php': 'php',
        '.java': 'java',
        '.c': 'c',
        '.h': 'c'
    }
    
    # Count files by extension
    for file_path in project_files:
        ext = get_extension(file_path)
        if ext in extensions:
            lang = extensions[ext]
            language_scores[lang] = language_scores.get(lang, 0) + 1
    
    # Boost scores for config files
    config_boosts = {
        'package.json': ['javascript', 'typescript'],
        'requirements.txt': ['python'],
        'pyproject.toml': ['python'],
        'Cargo.toml': ['rust'],
        'CMakeLists.txt': ['cpp'],
        'go.mod': ['go'],
        'composer.json': ['php']
    }
    
    for config_file, languages in config_boosts.items():
        if config_file in project_files:
            for lang in languages:
                language_scores[lang] = language_scores.get(lang, 0) + 10
    
    # Return languages sorted by score
    return sorted(language_scores.items(), key=lambda x: x[1], reverse=True)
```

### Framework Detection Logic

```python
def detect_frameworks(package_files, import_patterns):
    frameworks = []
    
    # Package.json dependency analysis
    if 'package.json' in package_files:
        deps = parse_package_json_dependencies(package_files['package.json'])
        
        # React detection
        if 'react' in deps:
            frameworks.append('react')
            
        # Next.js detection
        if 'next' in deps:
            frameworks.append('nextjs')
            
        # Vue detection
        if 'vue' in deps or '@vue/core' in deps:
            frameworks.append('vue')
            
        # Svelte detection
        if 'svelte' in deps or '@sveltejs/kit' in deps:
            frameworks.append('svelte')
            
        # TailwindCSS detection
        if 'tailwindcss' in deps:
            frameworks.append('tailwindcss')
    
    # Requirements.txt analysis for Python
    if 'requirements.txt' in package_files:
        reqs = parse_requirements(package_files['requirements.txt'])
        
        # FastAPI detection
        if 'fastapi' in reqs:
            frameworks.append('fastapi')
            
        # Django detection
        if 'django' in reqs:
            frameworks.append('django')
            
        # Flask detection
        if 'flask' in reqs:
            frameworks.append('flask')
    
    # Composer.json analysis for PHP
    if 'composer.json' in package_files:
        composer_deps = parse_composer_dependencies(package_files['composer.json'])
        
        # Laravel detection
        if 'laravel/framework' in composer_deps or 'laravel/laravel' in composer_deps:
            frameworks.append('laravel')
    
    # Configuration file detection
    config_frameworks = {
        'next.config.js': 'nextjs',
        'vue.config.js': 'vue',
        'svelte.config.js': 'svelte',
        'tailwind.config.js': 'tailwindcss'
    }
    
    for config_file, framework in config_frameworks.items():
        if config_file in package_files:
            if framework not in frameworks:
                frameworks.append(framework)
    
    return frameworks
```

### Workflow Detection Logic

```python
def detect_workflows(project_structure, git_info):
    workflows = []
    
    # Git workflow detection
    if '.git' in project_structure:
        workflows.append('git')
        
        # Analyze branch patterns
        if git_info.get('branch_count', 0) > 3:
            workflows.append('gitflow')
        else:
            workflows.append('trunk-based-development')
    
    # CI/CD detection
    if '.github/workflows' in project_structure:
        workflows.append('github-actions')
        
    if '.gitlab-ci.yml' in project_structure:
        workflows.append('gitlab-ci')
    
    # Quality tools detection
    quality_files = {
        '.pre-commit-config.yaml': 'pre-commit',
        'tox.ini': 'tox',
        'pytest.ini': 'pytest',
        '.eslintrc.*': 'eslint',
        'prettier.config.*': 'prettier'
    }
    
    for file_pattern, tool in quality_files.items():
        if any(file_matches_pattern(f, file_pattern) for f in project_structure):
            workflows.append('code-quality')
            break
    
    # Always include clean-code principles
    workflows.append('clean-code')
    
    return workflows
```

## Phase 3: Rule Selection

### Rule Selection Matrix

| Context Type               | Detection Method                     | Rule Applied                            | Priority    |
|----------------------------|--------------------------------------|-----------------------------------------|-------------|
| **Core System**            | Always                               | `@core/*.md`                            | 1 (Highest) |
| **Python Project**         | `.py` files, `requirements.txt`      | `@languages/python.md`                  | 2           |
| **TypeScript Project**     | `.ts/.tsx` files, `tsconfig.json`    | `@languages/typescript.md`              | 2           |
| **C++ Project**            | `.cpp/.hpp` files, `CMakeLists.txt`  | `@languages/cpp.md`                     | 2           |
| **Rust Project**           | `.rs` files, `Cargo.toml`            | `@languages/rust.md`                    | 2           |
| **Go Project**             | `.go` files, `go.mod`                | `@languages/go.md`                      | 2           |
| **PHP Project**            | `.php` files, `composer.json`        | `@languages/php.md`                     | 2           |
| **React Project**          | `react` in dependencies              | `@frameworks/react.md`                  | 3           |
| **Next.js Project**        | `next` in dependencies               | `@frameworks/nextjs.md`                 | 3           |
| **Vue Project**            | `vue` in dependencies                | `@frameworks/vue.md`                    | 3           |
| **FastAPI Project**        | `fastapi` in requirements            | `@frameworks/fastapi.md`                | 3           |
| **TailwindCSS**            | `tailwindcss` in dependencies        | `@frameworks/tailwindcss.md`            | 3           |
| **Laravel Project**        | `laravel/framework` in composer.json | `@frameworks/laravel.md`                | 3           |
| **Git Repository**         | `.git` directory                     | `@workflows/gitflow.md`                 | 4           |
| **Trunk-based**            | Single main branch                   | `@workflows/trunk-based-development.md` | 4           |
| **Code Quality**           | Linting/formatting tools             | `@workflows/code-quality.md`            | 4           |
| **Clean Code**             | Always                               | `@workflows/clean-code.md`              | 4           |
| **Commit Standards**       | Git repository                       | `@workflows/commit-messages.md`         | 4           |
| **Development Principles** | Always                               | `@principles/*.md`                      | 5 (Lowest)  |

### Automatic Rule Selection Function

```python
def select_applicable_rules(project_context):
    selected_rules = []
    
    # Core rules (always apply)
    core_rules = [
        "@core/tasks.md",
        "@core/plans.md", 
        "@core/hooks.md",
        "@core/memory.md",
        "@core/expand.md",
        "@core/versioning.md",
        "@core/workflow.md"
    ]
    selected_rules.extend(core_rules)
    
    # Language-specific rules
    language_map = {
        'python': "@languages/python.md",
        'typescript': "@languages/typescript.md",
        'javascript': "@languages/typescript.md",  # Use TypeScript rules for JS
        'cpp': "@languages/cpp.md",
        'rust': "@languages/rust.md",
        'go': "@languages/go.md",
        'php': "@languages/php.md"
    }
    
    for language, score in project_context.languages:
        if language in language_map and score > 0:
            selected_rules.append(language_map[language])
    
    # Framework-specific rules
    framework_map = {
        'react': "@frameworks/react.md",
        'vue': "@frameworks/vue.md",
        'nextjs': "@frameworks/nextjs.md",
        'fastapi': "@frameworks/fastapi.md",
        'tailwindcss': "@frameworks/tailwindcss.md",
        'svelte': "@frameworks/svelte.md",
        'laravel': "@frameworks/laravel.md"
    }
    
    for framework in project_context.frameworks:
        if framework in framework_map:
            selected_rules.append(framework_map[framework])
    
    # Workflow rules
    workflow_map = {
        'git': "@workflows/gitflow.md",
        'trunk-based-development': "@workflows/trunk-based-development.md",
        'github-actions': "@workflows/gitflow.md",  # Enhance git workflow
        'code-quality': "@workflows/code-quality.md",
        'clean-code': "@workflows/clean-code.md"
    }
    
    for workflow in project_context.workflows:
        if workflow in workflow_map:
            rule = workflow_map[workflow]
            if rule not in selected_rules:
                selected_rules.append(rule)
    
    # Commit message standards (if git present)
    if any('git' in w for w in project_context.workflows):
        selected_rules.append("@workflows/commit-messages.md")
    
    # Development principles (always apply)
    principle_rules = [
        "@principles/oop.md",
        "@principles/solid.md",
        "@principles/dry.md",
        "@principles/kiss.md",
        "@principles/yagni.md"
    ]
    selected_rules.extend(principle_rules)
    
    return selected_rules
```

## Phase 4: Rule Application

### Application Order and Precedence

Rules are applied in strict priority order:

1. **Core System Rules** (Priority 1) - Essential Magic Vibe functionality
2. **Language Rules** (Priority 2) - Programming language standards  
3. **Framework Rules** (Priority 3) - Framework-specific patterns
4. **Workflow Rules** (Priority 4) - Development process standards
5. **Principle Rules** (Priority 5) - Universal development principles

### Conflict Resolution Strategy

When rules conflict, apply this resolution hierarchy:

1. **Specificity Rule:** More specific rules override general ones
   - Framework-specific > Language-specific > General workflow
   - Project-specific configuration > Default templates

2. **Priority Rule:** Higher priority categories override lower priority
   - Core > Language > Framework > Workflow > Principles

3. **Composition Rule:** When possible, combine rather than override
   - Language + Framework rules should complement each other
   - Workflow rules should enhance, not replace, technical rules

4. **Documentation Rule:** Always document conflicts and resolutions
   - Log which rules were applied
   - Note any conflicts and how they were resolved
   - Provide rationale for rule selection decisions

### Example Rule Application Output

```text
Initializing Magic Vibe rule discovery...

Project Analysis Results:
- Languages: Python (25 files), TypeScript (12 files)
- Frameworks: FastAPI, React
- Workflows: Git repository, trunk-based development, code quality tools

Applying Rules (12 total):
✓ Core Rules (7): tasks, plans, hooks, memory, expand, versioning, workflow
✓ Language Rules (2): python.md, typescript.md  
✓ Framework Rules (2): fastapi.md, react.md
✓ Workflow Rules (3): trunk-based-development.md, code-quality.md, commit-messages.md
✓ Principle Rules (5): oop.md, solid.md, dry.md, kiss.md, yagni.md

Active Rule Set: 19 rules loaded and ready for application
```

## Implementation Guidelines for AI Agents

### Initialization Process

1. **First Project Interaction:**
   - Run complete project scan
   - Detect and cache project context
   - Load and apply all relevant rules
   - Report active rule set to user

2. **Subsequent Interactions:**
   - Use cached context unless significant changes detected
   - Monitor for new files or configuration changes
   - Re-scan if project structure changes significantly

3. **Context Change Detection:**
   - New language files added
   - Framework dependencies modified
   - Configuration files changed
   - Git workflow patterns altered

### Performance Optimization

- **Limit Scan Depth:** Maximum 3 directory levels for config files
- **File Count Limits:** Analyze first 50 source files per language
- **Caching Strategy:** Cache context detection results per session
- **Incremental Updates:** Update context only when changes detected

### Error Handling

- **Graceful Degradation:** If rule discovery fails, apply core rules only
- **Fallback Strategy:** Use previous context if new detection fails
- **User Notification:** Inform user of any rule discovery issues
- **Manual Override:** Allow users to manually specify rule context

## Integration with Magic Vibe Core

The rule discovery system integrates with core Magic Vibe functionality:

- **Task Creation:** Apply detected rules when creating new tasks
- **Plan Development:** Consider project context in planning phases
- **Hook Execution:** Context influences which hooks are relevant
- **Documentation:** Auto-generate context-aware documentation
- **Version Management:** Track rule changes alongside project versions
