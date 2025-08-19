# Task Magic

**Task Magic** is a file-based system.
This means all your project plans, tasks, and history are stored in plain text files (mostly Markdown) right in your project's `.ai/` directory.
This makes it easy to version control, track changes, and for AI agents to read and understand your project.

*Based on this repository: [Task Magic](https://github.com/iannuttall/task-magic).*

## How it works

There are three main parts to Task Magic:

1. **Plans (`.ai/plans/`)**:
    - **Purpose**: This is where you define the "what" and "why" of your project or specific features. Think of these as your Product Requirements Documents (PRDs).
    - **Key files**:
      - `.ai/plans/PLANS.md`: A global overview of your entire project. It should be a concise summary and index, linking to more detailed feature plans.
      - `.ai/plans/features/plan-{feature-name}.md`: Detailed PRDs for each specific feature you're building. This is where the AI will look for specifics when generating tasks.

    - **AI interaction**: AI agents use these plans to understand the scope and requirements, helping to generate tasks.
2. **Tasks (`.ai/tasks/` & `.ai/TASKS.md`)**:
    - **Purpose**: This is where the actual work items live. AI agents (or you) can break down plans into individual, manageable tasks.
    - **Key files & structure**:
      - `.ai/tasks/task{id}_{descriptive_name}.md`: Each task gets its own Markdown file. It includes details like status (pending, in progress, completed), priority, dependencies, a description, and how to test it.
      - `.ai/TASKS.md`: This is your master checklist. It's a human-friendly overview of all tasks in the `.ai/tasks/` directory, showing their status at a glance. **This file and the individual task files are kept in sync by the AI.**
    - **AI interaction**: AI agents can create tasks from plans, update their status as they work on them, and help you manage dependencies.
3. **Memory (`.ai/memory/`)**:
    - **Purpose**: Completed and failed tasks, as well as old plans, are archived here. This provides a valuable history for the AI to learn from and for you to reference.
    - **Key files**:
      - `.ai/memory/tasks/`: Archived task files.
      - `.ai/memory/TASKS_LOG.md`: A log of when tasks were archived.
      - `.ai/memory/plans/`: Archived plan files.
      - `.ai/memory/PLANS_LOG.md`: A log for archived plans.
    - **AI interaction**: The AI can consult the memory to understand how similar things were done in the past, or why a certain approach was taken.

## Working with AI agents

Task Magic is designed to work closely with AI agents. Here's how rules and context are handled:

- **Automatic context (`_index.md` files)**:
  - File named `_index.md` (like the one in `.vscode/rules/.task-magic/_index.md`) provide a high-level overview of a system or a set of rules.
  - These `_index.md` files are **automatically included in the AI's context** when you're working within a project that uses them. This gives the AI a foundational understanding without you needing to do anything extra.
- **On-demand rules (other `.md` or `.mdc` rule files)**:
  - Other rule files (e.g., `tasks.md`, `plans.md` located in `.vscode/rules/.task-magic/`) define specific behaviors or knowledge for the AI.
  - Each of these rule files has a `description` in its header. The AI agent (Cursor/Windsurf) can read these descriptions and **decide dynamically whether a specific rule is relevant** to your current request or the task it's performing.
  - If the AI deems a rule relevant, it will "fetch" and use that rule.
- **Your role: Guiding the AI with @-tags**:
  - While the agent is usually pretty good at figuring out which rules to use, you can manually tag the rules you want to use.
  - **For best results, @-tag specific rule files or directories in your prompts.** For example:
    - `@.vscode/rules/.task-magic/tasks.md create tasks for this feature`
    - `@.vscode/rules/.task-magic/plans.md generate a plan for X`
    - `@TASKS.md what is the status of my project?` (to refer to the main task checklist)
    - `@.ai/plans/features/plan-my-cool-feature.md can you review this plan?`
  - This helps ensure the AI looks at the exact information you want it to.

## Getting started

1. **Initialize `.ai/` structure**: If these directories don't exist, the AI will typically create them as needed when you ask it to create a plan or task. You can also create them manually.
    - `.ai/plans/PLANS.md` (start with a simple project title and overview)
    - `.ai/TASKS.md` (can start with just `# Project Tasks`)
    - `.ai/memory/TASKS_LOG.md` (can start with `# Task Archive Log`)
2. **Create a plan**: Ask your AI assistant to create a new feature plan using the planning rule (e.g., `@.vscode/rules/.task-magic/plans.md create a plan for user authentication`).
3. **Generate tasks**: Once a plan is ready, ask the AI to generate tasks from it (e.g., `@.vscode/rules/.task-magic/tasks.md generate tasks for the plan-user-authentication.md`).
4. **Work on tasks**: Tell the AI to start working on tasks. It will update `.ai/TASKS.md` and the individual task files as it progresses.
5. **Archive**: Periodically, ask the AI to archive completed or failed tasks to keep your active task list clean.

By using Task Magic, you get a structured, AI-friendly way to manage your projects, ensuring both you and your AI assistants are always on the same page.
