# Core Rules Reference

This guide covers the essential Magic Vibe core rules that form the foundation of the system.

## Overview

Core rules in Magic Vibe provide the fundamental functionality that makes the system work effectively with AI agents. These rules are always applied regardless of project type and serve as the foundation for all other rule categories.

## Core Rule Categories

### 1. Task Management (`tasks.md`)

**Purpose**: Defines how tasks are created, managed, and tracked throughout the project lifecycle.

**Key Features**:

- Task structure and formatting standards
- Status tracking and lifecycle management
- Dependency management and validation
- Progress reporting and completion criteria

**Usage**:

```text
@.magic-vibe/rules/core/tasks.md create a task for implementing user authentication API
```

**Applied When**:

- Creating new tasks
- Updating task status
- Managing task dependencies
- Validating task completion

### 2. Plan Management (`plans.md`)

**Purpose**: Governs the creation and management of Product Requirements Documents (PRDs) and feature plans.

**Key Features**:

- 8-section plan structure enforcement
- Plan-to-task breakdown guidelines
- Progress tracking and milestone management
- Stakeholder communication standards

**Usage**:

```text
@.magic-vibe/rules/core/plans.md create a comprehensive plan for user management system
```

**Applied When**:

- Creating new feature plans
- Breaking down large initiatives
- Tracking plan progress
- Managing plan dependencies

### 3. Memory Management (`memory.md`)

**Purpose**: Defines how project knowledge is captured, stored, and retrieved for future reference.

**Key Features**:

- Archival strategies for completed items
- Knowledge retention and categorization
- Historical context maintenance
- Learning and pattern recognition

**Usage**:

```text
@.magic-vibe/rules/core/memory.md archive completed authentication tasks and extract lessons learned
```

**Applied When**:

- Completing tasks or plans
- Archiving project artifacts
- Building project knowledge base
- Learning from past experiences

### 4. Workflow Management (`workflow.md`)

**Purpose**: Establishes the overall development workflow and process integration patterns.

**Key Features**:

- Development process standardization
- Integration with external tools
- Quality gates and validation checkpoints
- Continuous improvement practices

**Usage**:

```text
@.magic-vibe/rules/core/workflow.md establish development workflow for the new feature
```

**Applied When**:

- Setting up project workflows
- Integrating with CI/CD systems
- Defining quality processes
- Establishing team procedures

### 5. Hook System (`hooks.md`)

**Purpose**: Manages automation and event-driven processes within the Magic Vibe system.

**Key Features**:

- Event trigger definitions
- Automation script standards
- Integration point management
- Custom hook development guidelines

**Usage**:

```text
@.magic-vibe/rules/core/hooks.md set up automated task status updates on git commits
```

**Applied When**:

- Setting up automation
- Responding to project events
- Integrating with external systems
- Creating custom workflows

### 6. Context Management (`context.md`)

**Purpose**: Defines how project context is maintained and shared across AI interactions.

**Key Features**:

- Context preservation strategies
- Cross-session continuity
- Information prioritization
- Context optimization techniques

**Usage**:

```text
@.magic-vibe/rules/core/context.md maintain project context for AI collaboration
```

**Applied When**:

- Starting new AI sessions
- Sharing context between team members
- Optimizing AI interactions
- Managing large project contexts

### 7. Quality Assurance (`quality.md`)

**Purpose**: Establishes quality standards and validation processes for all Magic Vibe artifacts.

**Key Features**:

- Quality metrics and thresholds
- Validation checklists
- Review processes
- Continuous quality improvement

**Usage**:

```text
@.magic-vibe/rules/core/quality.md validate the quality of completed tasks and plans
```

**Applied When**:

- Reviewing task completion
- Validating plan quality
- Establishing quality gates
- Improving processes

### 8. Communication (`communication.md`)

**Purpose**: Standardizes communication patterns between AI agents, team members, and stakeholders.

**Key Features**:

- Communication protocols
- Status reporting standards
- Notification guidelines
- Documentation practices

**Usage**:

```text
@.magic-vibe/rules/core/communication.md generate status report for stakeholders
```

**Applied When**:

- Reporting project status
- Communicating with stakeholders
- Documenting decisions
- Sharing progress updates

## Rule Integration Patterns

### Sequential Application

Core rules are applied in sequence based on the development phase:

1. **Planning Phase**: `plans.md` → `context.md`
2. **Task Creation**: `tasks.md` → `workflow.md`
3. **Development**: `tasks.md` → `quality.md` → `hooks.md`
4. **Completion**: `quality.md` → `memory.md` → `communication.md`

### Parallel Application

Some core rules work together simultaneously:

- `tasks.md` + `workflow.md`: Task execution within process guidelines
- `quality.md` + `communication.md`: Quality reporting and stakeholder updates
- `context.md` + `memory.md`: Context preservation and knowledge management

## Core Rule Standards

### 8-Section Structure

All core rules follow the standard Magic Vibe structure:

1. **Code Generation**: How the rule affects code creation
2. **Change Management**: Impact on project changes
3. **Communication**: Stakeholder and team communication
4. **Quality Assurance**: Quality standards and validation
5. **Security & Performance**: Security and performance considerations
6. **Language-Specific Standards**: Technology-specific guidance
7. **Continuous Improvement**: Learning and optimization
8. **AI-Specific Best Practices**: AI collaboration patterns

### Measurable Standards

Core rules include specific, measurable criteria:

- Task completion times: 80% within estimates
- Plan accuracy: 90% of tasks completed as planned
- Quality metrics: Minimum 85% acceptance rate
- Response times: Context updates within 1 minute

### Validation Scripts

Each core rule includes validation mechanisms:

```bash
# Example: Task validation script
.magic-vibe/scripts/validate-tasks.sh
.magic-vibe/scripts/validate-plans.sh
.magic-vibe/scripts/validate-quality.sh
```

## Working with Core Rules

### Explicit Rule Application

Reference specific core rules when needed:

```text
@.magic-vibe/rules/core/tasks.md create a new task for API endpoint development

@.magic-vibe/rules/core/plans.md update the authentication plan with OAuth requirements

@.magic-vibe/rules/core/quality.md validate the completion criteria for this milestone
```

### Automatic Rule Application

Core rules are automatically applied during:

- Project initialization
- Task creation and management
- Plan development and tracking
- Quality validation processes
- Context management operations

### Custom Core Rule Extensions

Extend core rules for project-specific needs:

```markdown
# .magic-vibe/rules/custom/enhanced-tasks.md

# Enhanced Task Management

## Extension of Core Task Rules

This rule extends @.magic-vibe/rules/core/tasks.md with:
- Company-specific task categories
- Enhanced estimation techniques
- Custom validation criteria
- Integration with internal tools

## Additional Requirements

- All tasks must include security impact assessment
- Performance implications must be documented
- Accessibility considerations required for UI tasks
```

## Integration with Other Rule Categories

### Language Rules Integration

Core rules work with language-specific rules:

```text
@.magic-vibe/rules/core/tasks.md + @.magic-vibe/rules/languages/python.md
= Task management with Python-specific requirements
```

### Framework Rules Integration

Core rules enhance framework-specific patterns:

```text
@.magic-vibe/rules/core/quality.md + @.magic-vibe/rules/frameworks/react.md
= Quality assurance with React-specific standards
```

### Workflow Rules Integration

Core rules integrate with development workflows:

```text
@.magic-vibe/rules/core/workflow.md + @.magic-vibe/rules/workflows/gitflow.md
= Magic Vibe workflow with GitFlow integration
```

## Best Practices

### Core Rule Usage

1. **Always Initialize**: Start with core rule context
2. **Layer Gradually**: Add specific rules on top of core foundation
3. **Validate Consistently**: Use core quality rules throughout
4. **Archive Systematically**: Follow core memory management practices

### Performance Optimization

1. **Lazy Loading**: Load core rules as needed
2. **Context Caching**: Cache frequently used core rule context
3. **Selective Application**: Apply only relevant core rules
4. **Progressive Enhancement**: Build complexity gradually

### Team Coordination

1. **Shared Understanding**: Ensure team knows core rules
2. **Consistent Application**: Apply core rules uniformly
3. **Regular Reviews**: Periodically review core rule effectiveness
4. **Continuous Improvement**: Update core rules based on experience

## Troubleshooting Core Rules

### Common Issues

#### Core Rules Not Applied

```text
@.magic-vibe/rules/core/_index.md verify core rule application and report status
```

#### Conflicting Core Rules

```text
Show me any conflicts between core rules and suggest resolution strategies
```

#### Performance Issues

```text
Optimize core rule application for better performance in this project
```

### Diagnostic Commands

```text
# Check core rule status
@.magic-vibe/rules/core/_index.md show current core rule application status

# Validate core rule compliance
@.magic-vibe/rules/core/quality.md validate all core rule implementations

# Optimize core rule performance
@.magic-vibe/rules/core/context.md optimize core rule context for this project
```

---

Core rules provide the essential foundation for effective Magic Vibe usage. Understanding and properly applying these rules ensures consistent, high-quality project management and AI collaboration across all development activities.
