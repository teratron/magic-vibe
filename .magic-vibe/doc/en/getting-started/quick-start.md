# Quick Start Guide

Get started with Magic Vibe in under 5 minutes! This guide will help you set up the system and create your first plan and tasks.

## Prerequisites

- A code editor with AI assistance (Cursor, Windsurf, VS Code, etc.)
- Git installed on your system
- Basic familiarity with markdown files

## Step 1: Initialize Magic Vibe

Create the Magic Vibe directory structure in your project:

```bash
# Create the basic structure
mkdir -p .magic-vibe/ai/{plans,tasks,memory,hooks}

# Create essential files
touch .magic-vibe/ai/PLANS.md
touch .magic-vibe/ai/TASKS.md
touch .magic-vibe/ai/memory/TASKS_LOG.md
```

## Step 2: Let AI Discover Your Project

Ask your AI assistant:

```text
Initialize Magic Vibe system for this project and analyze the codebase
```

The AI will:

- Scan your project for languages and frameworks
- Report detected technologies
- Apply relevant rules automatically
- Set up the initial workspace

## Step 3: Create Your First Plan

Create a plan for a new feature:

```text
@.magic-vibe/rules/core/plans.md create a plan for user authentication system
```

This will generate a Product Requirements Document (PRD) in `.magic-vibe/ai/plans/`

## Step 4: Generate Tasks

Break down your plan into actionable tasks:

```text
@.magic-vibe/rules/core/tasks.md generate tasks from the authentication plan
```

Tasks will be created in `.magic-vibe/ai/tasks/` and tracked in `TASKS.md`

## Step 5: Start Development

Begin working on your first task:

```text
Start working on the first authentication task
```

The AI will automatically apply relevant language and framework rules.

## What Happens Next?

Magic Vibe will now:

- ✅ **Track Progress**: Monitor task completion and plan advancement
- ✅ **Apply Rules**: Automatically use relevant coding standards
- ✅ **Manage Context**: Maintain project knowledge and history
- ✅ **Automate Workflows**: Handle routine development tasks
- ✅ **Ensure Quality**: Apply best practices and validation

## Common First Steps

### Explore Applied Rules

See which rules are active for your project:

```text
Show me which Magic Vibe rules are currently applied to this project
```

### Check Project Status

View your current plans and tasks:

```text
Show me the current project status from Magic Vibe
```

### Customize Settings

Adjust system behavior:

```text
Help me configure Magic Vibe settings for my team workflow
```

## Next Steps

- 📖 Read [System Architecture](../core-concepts/architecture.md) to understand how Magic Vibe works
- 📝 Learn [Task Management](../core-concepts/task-management.md) for advanced task workflows
- 🔧 Explore [AI Integration](../user-guides/ai-integration.md) for better AI assistant collaboration
- ⚙️ Set up [Hook System](../user-guides/hooks.md) for automation

## Need Help?

- **Issues**: Check [Common Issues](../troubleshooting/common-issues.md)
- **Questions**: See [FAQ](../troubleshooting/faq.md)
- **Support**: Visit [GitHub Issues](https://github.com/teratron/magic-vibe/issues)

---

**Congratulations!** 🎉 You now have Magic Vibe running in your project. The system will help you maintain high-quality code while working efficiently with AI assistants.
