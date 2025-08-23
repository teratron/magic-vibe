---
description: Comprehensive Conventional Commits guidelines optimized for AI agents. Includes validation patterns, automated formatting, and quality standards for consistent commit history.
globs:
---

# Conventional Commits Guidelines for AI Agents

## 1. Core Specification Standards

### Message Structure Requirements

**MANDATORY FORMAT:**

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**VALIDATION RULES:**

- Type: REQUIRED, lowercase, max 10 characters
- Scope: OPTIONAL, lowercase, parentheses-wrapped, max 20 characters
- Description: REQUIRED, 10-72 characters, imperative mood, no period
- Body: OPTIONAL, wrap at 72 characters, separated by blank line
- Footer: OPTIONAL, follows git trailer format

### Primary Commit Types

**SEMANTIC VERSION IMPACT:**

```text
fix:     → PATCH version (bug fixes)
feat:    → MINOR version (new features)
BREAKING CHANGE → MAJOR version (breaking changes)
```

**EXTENDED TYPES:**

```text
build:    Changes to build system or dependencies
ci:       Changes to CI configuration and scripts
docs:     Documentation only changes
perf:     Performance improvements
refactor: Code changes that neither fix bugs nor add features
style:    Code style changes (formatting, missing semi-colons)
test:     Adding or modifying tests
chore:    Maintenance tasks, tooling changes
revert:   Reverting previous commits
```

## 2. AI-Specific Formatting Rules

### Type Selection Matrix

**DECISION TREE FOR AI AGENTS:**

```text
Code changes that:
├── Fix bugs or errors → fix
├── Add new functionality → feat
├── Improve performance → perf
├── Restructure without changing behavior → refactor
├── Add/modify tests → test
├── Update documentation → docs
├── Change build process → build
├── Update CI/CD → ci
├── Code formatting only → style
└── Maintenance tasks → chore
```

### Scope Guidelines

**RECOMMENDED SCOPES BY PROJECT TYPE:**

```text
Web Applications:
- api, auth, ui, db, config, middleware
- components, pages, utils, services

Libraries:
- core, utils, types, parser, validator
- client, server, common

Microservices:
- user-service, payment-service, notification
- gateway, proxy, cache

Monorepos:
- packages/core, apps/web, tools/cli
- workspace, deps, scripts
```

### Description Writing Standards

**FORMAT REQUIREMENTS:**

- Use imperative mood: "add", "fix", "update", not "added", "fixed", "updated"
- Start with lowercase letter
- No trailing period
- Be specific and descriptive
- Maximum 72 characters
- Minimum 10 characters

**GOOD vs BAD EXAMPLES:**

```text
✅ Good:
feat(auth): add JWT token validation middleware
fix(api): resolve null pointer exception in user endpoint
perf(db): optimize user query with database indexing
docs(readme): update installation instructions for Docker

❌ Bad:
feat: stuff                           # Too vague
Fixed the bug                         # Wrong tense, no type
feat: added new feature that does...  # Wrong tense, too long
FEAT: ADD USER LOGIN                  # Wrong case
```

## 3. Advanced Commit Patterns

### Breaking Changes

**BREAKING CHANGE FORMATS:**

```text
# Method 1: Using ! notation
feat(api)!: remove deprecated v1 endpoints

# Method 2: Using footer
feat(api): update user authentication system

BREAKING CHANGE: remove support for legacy token format

# Method 3: Both (recommended for clarity)
feat(api)!: update user authentication system

BREAKING CHANGE: remove support for legacy token format.
Migration guide available at docs/migration.md
```

### Multi-line Commit Bodies

**BODY FORMATTING RULES:**

```text
feat(payment): add subscription billing system

Implement recurring payment processing with the following features:
- Monthly and yearly subscription plans
- Automatic renewal with email notifications
- Pro-rated upgrades and downgrades
- Integration with Stripe webhooks for real-time updates

The system supports both individual and team subscriptions with
different pricing tiers based on usage limits.

Closes #234
Reviewed-by: @team-lead
Tested-by: @qa-engineer
```

### Footer Conventions

**STANDARD FOOTERS:**

```text
Closes #123                    # Issue closure
Fixes #456                     # Bug fix reference
Resolves #789                  # General resolution
Refs #101                      # General reference
Reviewed-by: @username         # Code review
Tested-by: @username           # Testing verification
Signed-off-by: Name <email>    # Legal sign-off
Co-authored-by: Name <email>   # Collaboration
BREAKING CHANGE: description   # Breaking change
```

## 4. Validation and Quality Assurance

### Automated Validation Patterns

**REGEX PATTERNS FOR VALIDATION:**

```regex
# Commit message format
^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\(.+\))?!?: .{10,72}$

# Type validation
^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)$

# Scope validation (optional, alphanumeric + hyphens)
^[a-z0-9-]+$

# Description validation (10-72 chars, no period at end)
^[a-z].{9,71}[^.]$
```

**VALIDATION CHECKLIST:**

- [ ] Type is from approved list
- [ ] Scope follows naming conventions (if present)
- [ ] Description is 10-72 characters
- [ ] Description uses imperative mood
- [ ] Description starts with lowercase
- [ ] Description has no trailing period
- [ ] Body is properly formatted (if present)
- [ ] Footers follow git trailer format (if present)
- [ ] Breaking changes are properly indicated

### Quality Metrics

**COMMIT QUALITY STANDARDS:**

```text
Excellent (9-10):
- Clear, specific description
- Appropriate type and scope
- Includes relevant context in body
- References issues/PRs
- Follows all conventions

Good (7-8):
- Clear description
- Correct type
- Follows basic conventions
- Minor formatting issues

Acceptable (5-6):
- Understandable description
- Correct type
- Some convention violations

Poor (1-4):
- Vague or unclear description
- Wrong type or missing type
- Major convention violations
```

## 5. Context-Specific Guidelines

### Bug Fix Commits

**BUG FIX PATTERN:**

```text
fix(scope): resolve specific issue description

Detailed explanation of:
- What was broken
- Root cause analysis
- How the fix addresses the issue
- Any side effects or considerations

Fixes #issue-number
Tested-by: @tester
```

**EXAMPLES:**

```text
fix(auth): resolve token expiration edge case
fix(api): handle null values in user profile endpoint
fix(ui): correct responsive layout on mobile devices
fix(db): resolve connection timeout in high-load scenarios
```

### Feature Addition Commits

**FEATURE PATTERN:**

```text
feat(scope): add specific feature description

Detailed description of:
- New functionality added
- User benefits
- Implementation approach
- Configuration or setup required

Closes #feature-request
Reviewed-by: @reviewer
```

**EXAMPLES:**

```text
feat(auth): add two-factor authentication support
feat(api): implement user preference management
feat(ui): add dark mode theme toggle
feat(search): implement fuzzy search with highlighting
```

### Refactoring Commits

**REFACTORING PATTERN:**

```text
refactor(scope): improve specific component/function

Explanation of:
- Code structure improvements
- Performance benefits
- Maintainability gains
- No functional changes made

No functional changes to user-facing features.
```

**EXAMPLES:**

```text
refactor(utils): extract common validation functions
refactor(api): simplify error handling middleware
refactor(ui): consolidate button component variants
refactor(db): optimize query structure for better performance
```

## 6. Automation and Tooling

### Git Hooks Integration

**COMMIT-MSG HOOK EXAMPLE:**

```bash
#!/bin/sh
# .git/hooks/commit-msg

commit_regex='^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\(.+\))?!?: .{10,72}$'

if ! grep -qE "$commit_regex" "$1"; then
    echo "Invalid commit message format!"
    echo "Format: <type>[scope]: <description>"
    echo "Types: build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test"
    exit 1
fi
```

### Automated Changelog Generation

**CHANGELOG MAPPING:**

```text
feat     → Features
fix      → Bug Fixes
perf     → Performance Improvements
docs     → Documentation
refactor → Code Refactoring
test     → Tests
build    → Build System
ci       → Continuous Integration
style    → Code Style
chore    → Maintenance
revert   → Reverts
```

### Release Automation

**SEMANTIC VERSION RULES:**

```markdown
Patch (x.x.X):
- fix: bug fixes
- perf: performance improvements
- docs: documentation updates
- style: code formatting
- test: test updates
- chore: maintenance

Minor (x.X.x):
- feat: new features
- refactor: code restructuring

Major (X.x.x):
- Any commit with BREAKING CHANGE
- Any commit with ! after type/scope
```

## 7. AI-Specific Implementation Guidelines

### Code Generation Requirements

**WHEN GENERATING COMMITS:**

- Always analyze the actual code changes to determine correct type
- Include specific scope based on modified files/components
- Write clear, descriptive messages in imperative mood
- Add appropriate footers for issue references
- Include body text for complex changes
- Validate format before suggesting commit message

### Commit Message Templates

**TEMPLATE SELECTION BASED ON CHANGE TYPE:**

```text
Bug Fix Template:
fix({{scope}}): {{description}}

{{explanation of fix}}

Fixes #{{issue_number}}

New Feature Template:
feat({{scope}}): {{description}}

{{feature details and benefits}}

Closes #{{issue_number}}

Refactoring Template:
refactor({{scope}}): {{description}}

{{explanation of improvements}}

No functional changes.

Breaking Change Template:
{{type}}({{scope}})!: {{description}}

{{detailed explanation}}

BREAKING CHANGE: {{breaking change description}}
```

### Quality Assurance Checklist

**PRE-COMMIT VALIDATION:**

- [ ] Commit type matches actual changes made
- [ ] Scope accurately reflects affected component
- [ ] Description is clear and specific
- [ ] Message follows conventional commit format
- [ ] Breaking changes are properly marked
- [ ] Issue/PR references are included
- [ ] Commit represents atomic, logical change
- [ ] Message will be useful for future debugging

### Common Anti-Patterns to Avoid

**NEVER DO:**

- Use vague descriptions like "fix stuff" or "update code"
- Mix multiple unrelated changes in one commit
- Use wrong tense ("added" instead of "add")
- Exceed character limits for description
- Forget to mark breaking changes
- Use uppercase for type or scope
- Include implementation details in description
- Make commits that don't represent logical units of work

**ALWAYS DO:**

- Make atomic commits that represent single logical changes
- Use specific, descriptive language
- Follow imperative mood consistently
- Include context in body for complex changes
- Reference related issues and PRs
- Validate format before committing
- Consider the audience who will read the commit history
- Use consistent scoping conventions throughout the project
