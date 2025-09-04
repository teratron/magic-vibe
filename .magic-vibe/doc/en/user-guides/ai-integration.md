# AI Agent Integration

Learn how to work effectively with AI coding assistants using Magic Vibe system.

## Overview

Magic Vibe is specifically designed to enhance AI-assisted development by providing:

- **Structured Context**: Clear, organized project information
- **Automatic Rule Application**: AI applies relevant standards without manual intervention
- **Consistent Workflows**: Standardized processes across different AI tools
- **Enhanced Communication**: Clear guidance and expectations for AI agents

## Supported AI Assistants

### Primary Support

Magic Vibe works seamlessly with:

- **Cursor**: AI-first code editor with advanced context understanding
- **Windsurf**: Collaborative AI coding platform
- **VS Code + AI Extensions**: GitHub Copilot, CodeWhisperer, etc.
- **Qoder**: Advanced AI coding assistant
- **Trae**: AI-powered development environment
- **Kiro**: Intelligent code completion and generation

### Configuration by Editor

#### Cursor Setup

```bash
# Rename or create Cursor configuration
mv .vscode .cursor
# or
mkdir .cursor
cp .magic-vibe/rules/core/* .cursor/
```

#### Windsurf Setup

```bash
# Configure for Windsurf
mv .vscode .windsurf
# Include Magic Vibe rules
cp .magic-vibe/rules/_index.md .windsurf/
```

#### VS Code Setup

```bash
# Keep existing .vscode or create new
mkdir -p .vscode
# Add Magic Vibe context
echo "# Magic Vibe Integration" >> .vscode/settings.json
```

## Working with AI Agents

### Initialization Pattern

When starting a new session with an AI assistant:

```text
Initialize Magic Vibe system for this project:
1. Analyze the codebase for languages and frameworks
2. Load relevant rules from .magic-vibe/rules/
3. Check current plans and tasks status
4. Report active configuration and applied rules
```

### Context References

Use @-tag references for specific guidance:

```text
@.magic-vibe/rules/core/tasks.md help me create a new task for user authentication
```

```text
@.magic-vibe/rules/languages/typescript.md ensure this code follows TypeScript best practices
```

```text
@.magic-vibe/ai/plans/2025-09-04-auth-system.md continue work on the authentication plan
```

### Automatic Rule Application

AI assistants automatically apply rules when:

- Generating new code
- Reviewing existing code
- Making architectural decisions
- Creating documentation
- Setting up project structure

## Communication Patterns

### Effective AI Prompts

#### Plan Creation

```text
@.magic-vibe/rules/core/plans.md create a comprehensive plan for implementing user authentication with the following requirements:
- OAuth 2.0 integration
- JWT token management
- Role-based access control
- Password reset functionality
```

#### Task Management

```text
@.magic-vibe/rules/core/tasks.md break down the authentication plan into specific development tasks, ensuring proper dependencies and realistic estimates
```

#### Code Generation

```text
Using @.magic-vibe/rules/languages/typescript.md and @.magic-vibe/rules/frameworks/react.md, implement a login component with form validation and error handling
```

#### Progress Updates

```text
Update task TASK-2025-001 with progress on JWT implementation - token generation is complete, working on validation middleware
```

### Context Maintenance

Keep AI context current:

#### Session Start

```text
Load current Magic Vibe project status including:
- Active plans and their progress
- Current task assignments
- Recent completions and blockers
- Applied rules and standards
```

#### Regular Updates

```text
Refresh Magic Vibe context with latest changes:
- Check for completed tasks
- Update plan statuses
- Review any new blockers or dependencies
```

#### Session End

```text
Archive session progress to Magic Vibe:
- Update task statuses
- Log progress notes
- Identify next priorities
```

## AI Workflow Patterns

### Feature Development Workflow

1. **Planning Phase**

   ```text
   @.magic-vibe/rules/core/plans.md create a plan for [feature name]
   ```

2. **Task Generation**

   ```text
   @.magic-vibe/rules/core/tasks.md generate tasks from the [feature] plan
   ```

3. **Implementation**

   ```text
   Start working on task [TASK-ID] applying relevant language and framework rules
   ```

4. **Validation**

   ```text
   @.magic-vibe/rules/core/tasks.md validate completion of task [TASK-ID]
   ```

5. **Integration**

   ```text
   Update plan progress and check for next available tasks
   ```

### Code Review Workflow

1. **Context Loading**

   ```text
   @.magic-vibe/rules/languages/[language].md review this code for compliance with standards
   ```

2. **Quality Assessment**

   ```text
   @.magic-vibe/rules/workflows/code-quality.md assess code quality and suggest improvements
   ```

3. **Security Review**

   ```text
   @.magic-vibe/rules/workflows/security.md check for security vulnerabilities and best practices
   ```

### Debugging Workflow

1. **Problem Analysis**

   ```text
   Using project context from Magic Vibe, analyze this error and suggest solutions
   ```

2. **Rule Consultation**

   ```text
   @.magic-vibe/rules/[relevant-rule].md check debugging approaches for this technology
   ```

3. **Solution Implementation**

   ```text
   Implement fix following Magic Vibe standards and update relevant task progress
   ```

## Advanced AI Integration

### Custom Prompts

Create project-specific AI prompts:

```markdown
# .magic-vibe/ai/prompts/code-generation.md

## Code Generation Standards for This Project

When generating code for this project:
1. Always reference @.magic-vibe/rules/languages/[language].md
2. Follow @.magic-vibe/rules/frameworks/[framework].md patterns
3. Include comprehensive error handling
4. Add appropriate logging and monitoring
5. Update related tests and documentation
6. Reference the current task context
```

### AI Hooks

Automate AI interactions:

```markdown
# .magic-vibe/ai/hooks/auto_task_update.md

## Automatic Task Updates

When AI completes work:
1. Identify related task ID from context
2. Update task progress in appropriate file
3. Check acceptance criteria completion
4. Flag any blockers or dependencies
5. Suggest next logical steps
```

### Context Optimization

Optimize AI context for better performance:

#### Context Prioritization

1. **Current Task**: Immediate work context
2. **Related Plan**: High-level feature context
3. **Applied Rules**: Relevant standards and practices
4. **Recent History**: Previous decisions and changes

#### Context Pruning

```text
Focus AI context on:
- Current sprint/milestone items
- Active plan and related tasks
- Recently modified code areas
- Immediate dependencies and blockers
```

## Multi-AI Coordination

### Team AI Scenarios

When multiple AI assistants work on the same project:

1. **Shared Context**

   ```text
   Load Magic Vibe project state to maintain consistency with other AI agents
   ```

2. **Work Coordination**

   ```text
   Check current task assignments to avoid conflicts with other AI work
   ```

3. **Progress Synchronization**

   ```text
   Update Magic Vibe with progress to keep all AI agents informed
   ```

### Handoff Protocols

When transferring work between AI sessions:

```text
Prepare Magic Vibe handoff summary:
- Current task status and progress
- Next immediate priorities
- Any blockers or dependencies
- Key decisions made in this session
- Recommended next actions
```

## Troubleshooting AI Integration

### Common Issues

#### AI Doesn't Recognize Rules

```text
Explicitly load Magic Vibe rules: @.magic-vibe/rules/_index.md analyze and apply project rules
```

#### Context Loss Between Sessions

```text
Reinitialize Magic Vibe context: Load current project status including plans, tasks, and applied rules
```

#### Inconsistent Rule Application

```text
Clarify rule priority: For this task, prioritize @.magic-vibe/rules/languages/[language].md over general practices
```

### Best Practices

1. **Always Initialize**: Start each AI session with Magic Vibe context loading
2. **Use Explicit References**: Reference specific rule files when needed
3. **Update Progress**: Keep task and plan status current
4. **Maintain Context**: Regularly refresh AI understanding of project state
5. **Document Decisions**: Record important architectural and design choices

## Performance Optimization

### Efficient Context Usage

- **Lazy Loading**: Load only relevant rules for current work
- **Targeted References**: Use specific rule files rather than broad context
- **Progressive Context**: Build context incrementally as needed
- **Context Cleanup**: Remove outdated or irrelevant context regularly

### AI Response Optimization

- **Clear Prompts**: Specific, actionable requests
- **Contextual References**: Include relevant Magic Vibe file references
- **Structured Requests**: Use consistent prompt patterns
- **Iterative Refinement**: Build on previous AI responses

---

Magic Vibe transforms AI-assisted development from ad-hoc interactions to structured, consistent, and highly productive workflows. The key is leveraging the system's organizational structure to provide clear context and guidance to AI assistants.
