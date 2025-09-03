---
description: Development workflow and process rules that AI agents should apply to maintain code quality and development standards.
globs: "*.md"
alwaysApply: false
---

# Workflow Rules Index

This directory contains development workflow and process rules that AI agents should apply to maintain code quality and development standards across all projects.

## Available Workflow Rules

- **Git Workflow:** `@workflows/gitflow.md` - Git branching strategies, merge practices, collaboration patterns
- **Trunk-Based Development:** `@workflows/trunk-based-development.md` - Continuous integration patterns, short-lived branches
- **Commit Messages:** `@workflows/commit-messages.md` - Conventional commit format, standards, and automation
- **Clean Code:** `@workflows/clean-code.md` - Code quality, readability standards, and maintainability practices
- **Code Quality:** `@workflows/code-quality.md` - Quality assurance, testing standards, and validation processes

## Rule Application

Workflow rules are applied based on:

1. **Project Setup:** Presence of `.git` directory, CI/CD configurations
2. **Team Collaboration:** Multi-contributor projects, branching patterns
3. **Project Size:** Small personal projects vs. large team projects
4. **Existing Patterns:** Current workflow indicators and established practices
5. **Quality Requirements:** Testing needs, deployment strategies

## Workflow Integration Patterns

### Git-Based Workflows
- **Feature Branch Workflow:** Suitable for small to medium teams
- **Gitflow:** Comprehensive branching model for larger projects
- **Trunk-Based Development:** High-velocity development with CI/CD
- **GitHub Flow:** Simplified workflow for continuous deployment

### Quality Assurance Workflows
- **Code Review Process:** Pull request workflows and review standards
- **Automated Testing:** CI/CD integration with test automation
- **Code Quality Gates:** Linting, formatting, and quality metrics
- **Documentation Standards:** Inline docs, README files, API documentation

### Development Process Workflows
- **Task Management:** Integration with issue tracking and project management
- **Release Management:** Versioning, tagging, and release processes
- **Deployment Workflows:** Staging, production deployment patterns
- **Monitoring and Feedback:** Error tracking, performance monitoring

## Application Guidelines

Workflow rules should be applied consistently across all projects regardless of language or framework:

1. **Universal Standards:** Core workflow practices apply to all development
2. **Scalable Processes:** Workflows should scale with project complexity
3. **Team Coordination:** Support both individual and team development
4. **Tool Integration:** Work with common development tools and platforms
5. **Continuous Improvement:** Support iterative process enhancement

## Precedence and Conflicts

When workflow rules conflict with language or framework rules:
1. **Process Over Implementation:** Workflow rules define the "how" of development
2. **Language/Framework Specifics:** Technical rules adapt to workflow requirements
3. **Project Context:** Consider team size, timeline, and quality requirements
4. **Documentation Required:** Document workflow decisions and adaptations

## Integration with Magic Vibe Core

Workflow rules complement Magic Vibe core functionality:
- **Task Management:** Workflow rules inform how tasks should be executed
- **Planning:** Development workflows influence plan structure and timing
- **Hooks:** Workflow events can trigger automated actions
- **Memory:** Workflow artifacts contribute to project knowledge base
- **Versioning:** Workflow rules inform version management strategies