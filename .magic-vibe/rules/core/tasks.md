# Task Management System

> **Magic Vibe Rule: AI Task Management**  
> **Category:** Core  
> **Priority:** High  
> **File Size:** ~11KB (AI-optimized)  
> **Dependencies:** `@rules/core/plans.md`, `@rules/core/memory.md`

Comprehensive task management system for AI agents with file-based workflows, dependency tracking, and automated status synchronization across Magic Vibe ecosystem.

## 1. Implementation Guidelines

### 1.1. Core Architecture

**System Components:**

1. **Active Tasks:** `.magic-vibe/ai/tasks/` - All current task files
2. **Master Overview:** `.magic-vibe/ai/TASKS.md` - Human-readable checklist
3. **Archive System:** `.magic-vibe/ai/memory/tasks/` - Completed/failed tasks
4. **Archive Log:** `.magic-vibe/ai/memory/TASKS_LOG.md` - Persistent history

### 1.2. File Naming Conventions

**Top-level Tasks:**

```text
task_{id}_{descriptive_name}.md
```

**Sub-tasks:**

```text
task_{parent_id}.{sub_id}_{descriptive_name}.md
```

**Examples:**

- `task_42_implement_user_auth.md`
- `task_42.1_create_user_model.md`
- `task_42.2_implement_login_api.md`

### 1.3. Task File Structure

```yaml
---
id: 42                        # Unique ID (numeric or "42.1")
title: 'Task Title'           # Human-readable title
status: pending               # pending|inprogress|completed|failed
priority: medium              # critical|high|medium|low
feature: Feature Name         # Logical grouping
commit_type: feat             # Conventional commit type
dependencies: [3, 5.2]        # Task ID dependencies
assigned_agent: null          # Current agent (null if unassigned)
created_at: "2025-01-05T10:00:00Z"   # UTC timestamp
started_at: null              # Set when status -> inprogress
completed_at: null            # Set when status -> completed/failed
error_log: null               # Error reason if failed
---

## Description
(Brief summary for TASKS.md display)

## Details
(Specific requirements and implementation steps)

## Test Strategy
(Verification and testing approach)
```

### 1.4. ID Generation Algorithm

**Top-level Task IDs:**

1. List files in `.magic-vibe/ai/tasks/` and `.magic-vibe/ai/memory/tasks/`
2. Extract numeric IDs from `task_{id}_{name}.md` pattern
3. Next ID = highest existing ID + 1 (start at 1 if none found)

**Sub-task IDs:**

1. Filter files matching `task_{parent_id}.{sub_id}_{name}.md`
2. Extract sub_id numbers for specific parent
3. Next sub_id = highest existing sub_id + 1 (start at 1 if none found)

### 1.5. Priority System

- **critical:** Essential for core functionality, blocks multiple tasks
- **high:** Key features, important fixes, blocks several tasks
- **medium:** Standard development work (default)
- **low:** Nice-to-have improvements, cosmetic fixes

## 2. Change Management Protocols

### 2.1. Status Lifecycle Management

**Status Flow:** `pending` → `inprogress` → `completed|failed`

**Required Updates:**

1. **Start Task:** Update YAML (`status`, `assigned_agent`, `started_at`) + TASKS.md icon
2. **Complete Task:** Update YAML (`status`, `completed_at`, `assigned_agent: null`) + TASKS.md icon
3. **Fail Task:** Update YAML (`status`, `error_log`, `completed_at`) + TASKS.md icon

### 2.2. Dependency Validation

**Before Starting Task:**

- Verify all dependencies have `status: completed`
- Check both active and archived task directories
- Block task start if dependencies unmet

### 2.3. Synchronization Requirements

**Critical Rule:** Keep `.magic-vibe/ai/TASKS.md` perfectly synchronized with task file statuses

**Update Triggers:**

- Task creation
- Status changes
- Task archival
- Bulk operations

## 3. Communication Standards

### 3.1. TASKS.md Format

```markdown
- [ICON] **ID {id}: {Title}** (Priority: {priority}){STATUS_NOTE}

> Dependencies: {dep_id1}, {dep_id2} (if exists)
> {Description}
```

**Icons:**

- `[ ]` Pending
- `[-]` In Progress  
- `[x]` Completed
- `[!]` Failed

### 3.2. Archive Log Format

```markdown
- Archived **ID {id}: {Title}** (Status: {status}) on {timestamp}

> Dependencies: {deps} (if exists)
> {Description}
```

### 3.3. User Command Interpretation

**Common Commands:**

- "Show tasks" → Display TASKS.md content
- "Start next task" → Find first pending task, validate dependencies
- "Complete task {id}" → Update status, run hooks, generate docs
- "Archive completed" → Move completed/failed tasks to memory

## 4. Quality Assurance Framework

### 4.1. File System Safety

**Mandatory Procedures:**

- Check file existence before operations
- Use `mv` commands for archiving (never simulate with edit+delete)
- Validate directory paths before file operations
- Generate timestamps with: `date -u +"%Y-%m-%dT%H:%M:%SZ"`

### 4.2. Testing Integration

**Test Strategy Validation:**

- ALWAYS check for `## Test Strategy` section before task completion
- If found: Ask user "Run tests or mark complete based on verification?"
- If none: Proceed to completion
- Remove debug logging before marking complete

### 4.3. Data Integrity

**Synchronization Validation:**

- TASKS.md must mirror task file statuses exactly
- Dependencies must reference existing tasks
- Archive operations must preserve task data
- Timestamps must be consistent across related operations

## 5. Security & Performance Guidelines

### 5.1. Access Control

**File Permissions:**

- Task files: Read/write for agents
- Archive files: Read-only after archival
- Log files: Append-only operations

### 5.2. Performance Optimization

**Batch Operations:**

- Group related status updates
- Single timestamp for batch archives
- Minimize file system operations
- Use efficient file listing and parsing

### 5.3. Data Validation

**Input Sanitization:**

- Validate task IDs format
- Check dependency references
- Verify status transition rules
- Sanitize file names for cross-platform compatibility

## 6. Integration & Compatibility

### 6.1. Hook System Integration

**Hook Triggers:**

- `task_creation`: After new task files created
- `task_status_change`: On status updates (inprogress/completed/failed)
- `task_archival`: After moving tasks to memory
- `git_commit`: Chain triggered by other hooks

### 6.2. Documentation System

**Auto-Generated Docs:**

- English: `docs/en/task-{id}-{feature}.md`
- Russian: `docs/ru/task-{id}-{feature}.md`
- Triggered by completion hooks
- Includes implementation details, API changes, usage examples

### 6.3. Cross-System Compatibility

**Platform Requirements:**

- POSIX-compliant file operations
- UTF-8 encoding for all text files
- Cross-platform timestamp formats
- Shell-agnostic command execution

## 7. Monitoring & Maintenance

### 7.1. System Health Checks

**Regular Validations:**

- Task file format compliance
- TASKS.md synchronization accuracy
- Archive integrity verification
- Dependency graph validation

### 7.2. Performance Monitoring

**Key Metrics:**

- Task completion rates
- Average task duration
- Dependency resolution efficiency
- File operation performance

### 7.3. Maintenance Procedures

**Cleanup Operations:**

- Periodic archive organization
- Broken dependency resolution
- Orphaned file cleanup
- Log file rotation

## 8. AI Agent Optimization

### 8.1. Command Processing

**Agent Workflow:**

1. Parse user command intent
2. Validate current system state
3. Check dependencies and permissions
4. Execute operations with error handling
5. Update all synchronized files
6. Trigger relevant hooks
7. Provide status feedback

### 8.2. Error Handling

**Failure Recovery:**

- Graceful degradation on file system errors
- Clear error messages for dependency issues
- Rollback capabilities for failed operations
- User guidance for manual resolution

### 8.3. Efficiency Guidelines

**AI Optimization:**

- Minimize redundant file reads
- Batch similar operations
- Cache frequently accessed data
- Use structured data for parsing
- Prioritize human-readable outputs

### 8.4. Context Preservation

**State Management:**

- Maintain task context across operations
- Preserve user intent during complex workflows
- Track operation history for debugging
- Support incremental progress tracking

---

**Magic Vibe Task System v2.1.0** - AI-optimized workflow management

*For detailed sub-task creation: `@rules/core/expand.md`*  
*For workflow diagrams: `@rules/core/workflow.md`*
