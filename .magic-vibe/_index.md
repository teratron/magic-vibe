---
description: Development guidelines and standards for Magic Vibe system creators and maintainers.
globs:
alwaysApply: true
---

# Magic Vibe System Creator Guidelines

> **⚠️ CRITICAL AI AGENT NOTICE ⚠️**
>
> **THIS FILE IS FOR MAGIC VIBE SYSTEM DEVELOPERS ONLY**
>
> If you are an AI agent helping a user with their project:
>
> - **DO NOT** apply these rules to user projects
> - **DO NOT** use this file for project development guidance
> - **USE ONLY** `@rules/` directory for project development
> - This file contains **internal system development standards**
> - **IGNORE** this file unless explicitly working on Magic Vibe system itself
>
> **For project development, use:** `rules/core/`, `rules/languages/`, `rules/frameworks/`, `rules/workflows/`, `rules/principles/`
>
> **For Magic Vibe System Developers and Maintainers**

These are the foundational rules for creating, maintaining, and evolving the Magic Vibe system itself. If you're developing the Magic Vibe framework, these guidelines ensure consistency, quality, and maintainability.

## 1. System Architecture Principles

### 1.1. Pure Rule-Based System

**Magic Vibe Philosophy:**

- **Markdown-First:** All operational guidance via `.md` files
- **No Executable Dependencies:** Avoid shell scripts, Python scripts, etc.
- **Platform Agnostic:** Rules work across all operating systems
- **AI-Parseable:** Focus on content AI agents can understand and apply

**What Belongs in Magic Vibe:**

- ✅ Rule definitions (`.md` files)
- ✅ Configuration examples (code blocks within `.md`)
- ✅ Validation patterns (described in markdown)
- ✅ Code snippets and templates (embedded in rules)
- ❌ Executable scripts (`.sh`, `.ps1`, `.py`, `.js`)
- ❌ Standalone configuration files (`.json`, `.yaml`, `.toml`)
- ❌ Binary tools or utilities
- ❌ Platform-specific automation

**Principle:** Everything AI needs should be in markdown rules

### 1.2. Directory Structure and Separation

**Core Magic Vibe System (Rule-Based):**

- `rules/` - Pure markdown rule files (AI operational)
- `docs/` - Human documentation (informational)
- `ai/` - Generated workspace (dynamic, to be created)
- `README.md` - System overview (informational)
- `_index.md` - Creator guidelines (internal)

**Development Support (Optional):**

- `tools/` - Development utilities and scripts (creator-only)
  - Version management scripts
  - Validation utilities  
  - Build and deployment helpers
  - **NOT for AI agents or user projects**

**Foundation vs. Generated Workspace:**

- `.magic-vibe/` = **Foundation System** (template, rules, docs)
- `.magic-vibe/ai/` = **Generated Workspace** (initially empty, populated during use, to be created)
- Never mix template logic with generated content

**Rule vs. Documentation vs. Tools:**

- `rules/` = **Active operational rules** for AI agents and developers
- `docs/` = **Informational content** for human understanding only
- `tools/` = **Development utilities** for Magic Vibe creators only
- AI agents MUST NOT use `docs/` or `tools/` for operational decisions

### 1.3. Component Classification

**Active Components (AI Operational):**

- `rules/` - Rule discovery and application
- `ai/` - Dynamic workspace generation
- `README.md` - System overview with operational context

**Informational Components (Human Reference):**

- `docs/` - Human-readable documentation
- `_index.md` - Creator guidelines and internal documentation

**Development Support (Creator-Only):**

- `tools/` - Development utilities and automation scripts
- Version management, validation tools, build helpers

**CRITICAL:** AI Agent Restrictions

- AI agents MUST NEVER use `docs/` or `tools/` content for operational decisions
- These directories are strictly prohibited for development guidance or code generation
- Only `rules/` should guide AI behavior in user projects

### 1.3. Template vs. Production Distinction

**Template Repository (This Project):**

- Contains demonstration examples and full documentation
- Shows complete system capabilities
- Includes populated `ai/` directory for reference (to be created)

**Production Projects (User Projects):**

- `ai/` directory should be initially empty or minimal
- Only foundational `.magic-vibe/` system copied
- Workspace populated dynamically during actual usage
- Clean separation between template and active workspace

### 1.4. Responsibility Separation Principle

**⚠️ AI AGENT ATTENTION:** This section defines what AI agents should and should NOT use.

**Creator Rules (`_index.md`) - INTERNAL ONLY:**

- Guidelines for Magic Vibe system development
- Architectural decisions and maintenance standards
- System evolution and integration patterns
- Internal development workflow
- **AI AGENTS: DO NOT APPLY TO USER PROJECTS**

**User Rules (`rules/`) - FOR PROJECT DEVELOPMENT:**

- Operational rules for project development
- AI agent guidance for code generation
- Language, framework, and workflow standards
- End-user development practices
- **AI AGENTS: USE THESE FOR USER PROJECTS**

### 1.5. Hierarchical Rule System

**Rule Priority Order:**

1. **Core Rules** (`rules/core/`) - Highest priority, always applied
2. **Language Rules** (`rules/languages/`) - Language-specific standards
3. **Framework Rules** (`rules/frameworks/`) - Framework patterns
4. **Workflow Rules** (`rules/workflows/`) - Process standards
5. **Principles** (`rules/principles/`) - Universal guidelines

## 2. Rule Development Standards

### 2.1. Magic Vibe 8-Section Rule Format

Every rule file MUST follow this structure:

```markdown
---
description: Clear, actionable description of what this rule covers
globs: "*.{ext1,ext2}" # File patterns this rule applies to
alwaysApply: false # Whether to apply regardless of context
---

# Rule Title

## 1. Overview
## 2. Standards
## 3. Implementation
## 4. Validation
## 5. Examples
## 6. Anti-patterns
## 7. Integration
## 8. Metrics
```

### 2.2. Measurable Metrics Requirement

Every rule MUST include specific, measurable criteria:

```markdown
## 8. Metrics

**Quality Thresholds:**
- Function length: ≤ 20 lines
- File length: ≤ 300 lines
- Test coverage: ≥ 90%
- Cyclomatic complexity: ≤ 10

**Performance Targets:**
- Build time: ≤ 30 seconds
- Hot reload: ≤ 2 seconds
```

### 2.3. New Rule Creation Protocol

**Before Creating a New Rule:**

1. **Check Existing Rules:** Ensure no overlap with current rule set
2. **Determine Category:** Core/Language/Framework/Workflow/Principle
3. **Define Scope:** Specific file patterns and use cases
4. **Plan Integration:** How it works with existing rules

**Rule Creation Checklist:**

- [ ] Follows 8-section format
- [ ] Includes measurable metrics
- [ ] Contains working code examples (in markdown)
- [ ] Shows antipatterns
- [ ] Documents integration points
- [ ] Tested with AI agents
- [ ] Reviewed for conflicts
- [ ] **NO README.md files in rule directories**
- [ ] **NO executable scripts in rule directories**

**New Rule Template:**

```bash
# Create new rule structure
mkdir -p .magic-vibe/rules/{category}
touch .magic-vibe/rules/{category}/{rule-name}.md
# Rules contain validation patterns in markdown format
# Executable tools go in tools/ if needed
```

### 2.4. File Size Optimization for AI Performance

**Critical:** AI Token Limitations

AI agents have strict limitations that affect rule file design:

**Recommended File Sizes:**

- **Rule Files:** Maximum 15KB (≈ 3,750 tokens)
- **Core Rules:** Maximum 20KB (≈ 5,000 tokens)
- **Index Files:** Maximum 25KB (≈ 6,250 tokens)
- **Example Files:** Maximum 10KB (≈ 2,500 tokens)

**Token Calculation:**

- **1 KB ≈ 250 tokens** (rough estimate)
- **1 token ≈ 4 characters** (average for English)

**Why Size Matters:**

- **Context Window Limits:** GPT-4: ~128K tokens, Claude: ~200K tokens
- **Processing Speed:** Smaller files = faster analysis
- **Memory Efficiency:** Reduces AI agent memory usage
- **Parsing Accuracy:** AI better understands focused content

**File Size Guidelines:**

```markdown
## Size Category Limits

| File Type       | Max Size | Max Tokens | Purpose                        |
|-----------------|----------|------------|--------------------------------|
| Core Rules      | 20KB     | 5,000      | Essential system functionality |
| Language Rules  | 15KB     | 3,750      | Language-specific standards    |
| Framework Rules | 15KB     | 3,750      | Framework patterns             |
| Workflow Rules  | 12KB     | 3,000      | Process definitions            |
| Principle Rules | 15KB     | 3,750      | Development principles         |
| Index Files     | 25KB     | 6,250      | System overviews               |
| Examples        | 10KB     | 2,500      | Code demonstrations            |
```

**Content Optimization Strategies:**

1. **Prioritize Essential Information:**
   - Focus on actionable guidance
   - Remove verbose explanations
   - Use concise language

2. **Structure for Scanning:**
   - Use bullet points over paragraphs
   - Employ tables for data
   - Implement clear headings

3. **Code Block Efficiency:**
   - Show minimal working examples
   - Avoid redundant code
   - Use comments sparingly

4. **Cross-Reference Instead of Duplicate:**
   - Reference other rules instead of repeating
   - Use rule/file.md references
   - Link related concepts

**File Size Monitoring:**

```bash
# Check file sizes during development
find .magic-vibe/rules -name "*.md" -exec wc -c {} + | sort -n

# Alert for oversized files (>25KB)
find .magic-vibe/rules -name "*.md" -size +25k
```

**When Files Become Too Large:**

1. **Split by Logical Sections:**
   - Core functionality vs. advanced features
   - Basic patterns vs. complex examples
   - Different use cases or scenarios

2. **Create Sub-rules:**
   - `react.md` → `react-basic.md` + `react-advanced.md`
   - `python.md` → `python-core.md` + `python-frameworks.md`

3. **Extract Examples:**
   - Move large code examples to separate files
   - Reference examples from main rule
   - Keep examples focused and minimal

**AI Agent Performance Impact:**

- **Files < 10KB:** Optimal performance, fast processing
- **Files 10-20KB:** Good performance, normal processing
- **Files 20-30KB:** Acceptable performance, slower processing  
- **Files > 30KB:** Poor performance, may cause issues

**Current Magic Vibe Status:**

```markdown
✅ _index.md: 8.5KB (Optimal)
✅ Most rule files: <15KB (Good)
⚠️ Monitor: Some principle files approaching 15KB
```

**Validation in Rules (Recommended):**

- **Patterns:** Describe validation patterns in markdown
- **Examples:** Show correct and incorrect code examples
- **Linting Config:** Include configuration examples (ESLint, TSConfig, etc.)
- **CI/CD Patterns:** Provide GitHub Actions examples

**Development Tools (Optional):**

- **Executable Scripts:** Place in `tools/` directory if needed
- **Cross-platform Support:** Provide both `.sh` and `.ps1` versions
- **Creator Use Only:** Never reference tools in rules for user projects

## 3. Dynamic Rule Discovery Standards

### 3.1. Project Context Analysis

**Automatic Detection Protocol:**

1. **File Extension Scanning:** Detect programming languages by file patterns
2. **Dependency Analysis:** Parse package.json, requirements.txt, Cargo.toml, etc.
3. **Configuration Detection:** Identify framework configs (next.config.js, vue.config.js)
4. **Structure Analysis:** Recognize project patterns and conventions
5. **Workflow Detection:** Git patterns, CI/CD files, quality tools

**Context Reporting:**

```markdown
# Example AI Agent Report

Detected Context:
- Languages: TypeScript, Python
- Frameworks: React, FastAPI
- Workflows: Git Flow, Clean Code
- Principles: SOLID, FSD

Applying Rules:
- @rules/languages/typescript.md
- @rules/frameworks/react.md
- @rules/frameworks/fastapi.md
- @rules/workflows/gitflow.md
- @rules/principles/solid.md
- @rules/principles/feature-sliced-design.md
```

### 3.2. Context Detection Patterns

**File Extension Detection:**

```markdown
globs:
  - "src/**/*.{js,jsx,ts,tsx}" # React/TypeScript
  - "**/*.py" # Python
  - "**/*.go" # Go
```

**Package Detection:**

```markdown
# Auto-apply when these dependencies are found:
# package.json: "react", "@types/react"
# requirements.txt: "fastapi", "django"
# Cargo.toml: [dependencies] section
```

### 3.2. Rule Conflict Resolution

**Specificity Hierarchy:**

1. More specific rules override general ones
2. Meta-frameworks override base frameworks
3. Project-specific rules override system rules
4. Explicit user rules override auto-detected rules

## 4. Version Management Standards

### 4.1. Semantic Versioning

**Project Versioning:**

- MAJOR: Breaking changes to rule structure or API
- MINOR: New rules, features, or non-breaking enhancements
- PATCH: Bug fixes, documentation updates, minor improvements

**Documentation Versioning:**

- Auto-increment on task completion (via hooks)
- Manual increment for major documentation overhauls
- Track generation count for AI usage metrics

### 4.2. Version Automation

**Automated Triggers:**

```bash
# Auto-increment docs version when tasks complete
./version-manager.sh auto-docs

# Manual project version updates
./version-manager.sh bump-project minor
```

## 5. Documentation Standards

### 5.1. Multilingual Support

**Required Languages:**

- English (primary, for code and technical content)
- Russian (secondary, for human-readable explanations)

**File Structure:**

```text
docs/
├── en/ # English documentation
├── ru/ # Russian documentation
└── README.md # Overview in both languages
```

### 5.2. Documentation Types

**System Documentation (`@docs/`):**

- Human-readable explanations
- Architecture diagrams
- Usage tutorials
- Contributing guidelines

**Operational Documentation (within rules):**

- Implementation examples
- Validation scripts
- Integration patterns
- Measurable metrics

**CRITICAL:** No `README.md` Files in `@rules/`

- **DO NOT** create README.md files within @rules/ directories
- README.md files create information noise for AI agents
- Use only main @README.md and @docs/ for explanatory content
- Keep @rules/ focused purely on operational rule files
- AI agents should focus on .md rule files, not documentation files

## 6. Quality Assurance

### 6.1. Rule Testing Requirements

**Validation Testing:**

- Every rule must have working validation scripts
- Scripts must run on Windows (PowerShell) and Unix (Bash)
- Integration tests for rule conflict resolution

**Example Testing:**

- All code examples must be syntactically correct
- Examples must demonstrate both correct and incorrect patterns
- Integration examples must work with specified tech stacks

### 6.2. AI Agent Compatibility

**Optimization for AI:**

- Rules must be structured for easy parsing
- Examples must be complete and runnable
- Context must be explicit (no implicit assumptions)
- Measurable criteria for validation

## 7. Integration Patterns

### 7.1. Cross-Rule Integration

**Complementary Rules:**

- Language + Framework (e.g., TypeScript + React)
- Framework + Workflow (e.g., Next.js + Git Flow)
- Principles + Implementation (e.g., SOLID + OOP)

**Conflict Prevention:**

- Use `@rules/_index.md` for rule discovery coordination
- Document known conflicts and resolution strategies
- Provide override mechanisms for edge cases

### 7.2. Editor Integration

**Multi-IDE Support:**

- Editor-agnostic rule structure
- Standard `@` reference syntax
- No IDE-specific dependencies in core rules

## 8. Maintenance and Evolution

### 8.1. Regular Review Cycles

**Monthly Reviews:**

- Rule effectiveness metrics
- AI agent feedback analysis
- Community usage patterns
- Conflict resolution improvements

**Quarterly Updates:**

- New language/framework support
- Rule structure optimizations
- Version management improvements
- Documentation enhancements

### 8.2. Community Contributions

**Contribution Guidelines:**

- All new rules must follow 8-section format
- Include validation scripts and examples
- Provide both English and Russian documentation
- Test with multiple AI agents for compatibility

**Review Process:**

1. Technical review for rule structure compliance
2. Validation script testing on multiple platforms
3. AI agent compatibility testing
4. Community feedback integration
5. Documentation review and translation

### 8.3. Validation Standards

**Validation in Rules (Recommended):**

- **Patterns:** Describe validation patterns in markdown
- **Examples:** Show correct and incorrect code examples
- **Linting Config:** Include configuration examples (ESLint, TSConfig, etc.)
- **CI/CD Patterns:** Provide GitHub Actions examples

**Development Tools (Optional):**

- **Executable Scripts:** Place in `@tools/` directory if needed
- **Cross-platform Support:** Provide both `.sh` and `.ps1` versions
- **Creator Use Only:** Never reference tools in rules for user projects

---

**Magic Vibe** System Creator Guidelines v1.0.0

*These guidelines ensure the Magic Vibe system remains consistent, maintainable, and effective for AI-assisted development across all supported platforms and use cases.*
