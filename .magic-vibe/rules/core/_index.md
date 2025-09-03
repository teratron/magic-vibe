---
description: Core Magic Vibe system rules that provide essential functionality for AI agent task management and workflow coordination.
globs: "*.md"
alwaysApply: true
---

# Core Rules Index

This directory contains the core Magic Vibe system rules that provide essential functionality for AI agent task management and workflow coordination. These rules form the foundation of the Magic Vibe system and are always applied.

## Available Core Rules

- **Tasks:** `@core/tasks.md` - Task creation, management, status tracking, and lifecycle coordination
- **Plans:** `@core/plans.md` - Product Requirements Document (PRD) creation and feature planning
- **Hooks:** `@core/hooks.md` - Automated action system for event-driven workflow automation
- **Memory:** `@core/memory.md` - Archive management for completed tasks, plans, and project history
- **Expand:** `@core/expand.md` - Task complexity analysis and decomposition guidelines
- **Versioning:** `@core/versioning.md` - Project and documentation version management
- **Workflow:** `@core/workflow.md` - Overall workflow coordination and process management

## Core System Responsibilities

### Task Management (`@core/tasks.md`)
- Create and manage individual development tasks
- Track task status and dependencies
- Maintain task synchronization with TASKS.md file
- Handle task lifecycle from creation to completion or archival

### Planning (`@core/plans.md`)
- Generate Product Requirements Documents (PRDs)
- Define feature specifications and requirements
- Coordinate plan-to-task breakdown
- Maintain plan versioning and updates

### Automation (`@core/hooks.md`)
- Execute automated actions based on system events
- Coordinate between system-wide and user-specific hooks
- Handle trigger event detection and hook execution
- Manage hook priority and conflict resolution

### Archive Management (`@core/memory.md`)
- Archive completed and failed tasks/plans
- Maintain project history and knowledge base
- Organize archived items for future reference
- Support knowledge retrieval and learning

### Task Analysis (`@core/expand.md`)
- Analyze task complexity and scope
- Provide decomposition recommendations
- Guide task sizing and estimation
- Support hierarchical task structures

### Version Control (`@core/versioning.md`)
- Manage project version tracking
- Coordinate documentation versioning
- Handle automated version increments
- Support release management workflows

### Process Coordination (`@core/workflow.md`)
- Coordinate overall Magic Vibe system processes
- Manage workflow state and transitions
- Handle cross-component integration
- Support system-wide configuration and settings

## Application Priority

Core rules have the highest priority in the Magic Vibe system:
1. **Always Applied:** Core rules are mandatory for all Magic Vibe operations
2. **Foundation Layer:** Other rule categories build upon core functionality
3. **System Integrity:** Core rules ensure system consistency and reliability
4. **Cross-Project:** Core rules work across all project types and contexts

## Integration with Other Rule Categories

Core rules provide the foundation that other rule categories extend:
- **Language Rules:** Apply language-specific practices within core task management
- **Framework Rules:** Implement framework patterns using core planning and task structure
- **Workflow Rules:** Enhance core processes with specific development workflows
- **Principle Rules:** Guide core rule implementation with development best practices

## System Dependencies

Core rules manage critical Magic Vibe directories and files:
- `.magic-vibe/ai/tasks/` - Active task files
- `.magic-vibe/ai/plans/` - Active plan files  
- `.magic-vibe/ai/memory/` - Archived items
- `.magic-vibe/rules/hooks/` - System hooks
- `.magic-vibe/ai/hooks/` - User hooks
- `.magic-vibe/ai/TASKS.md` - Task index file