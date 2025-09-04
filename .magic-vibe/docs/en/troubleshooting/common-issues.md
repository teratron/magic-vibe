# Troubleshooting Common Issues

This guide helps you resolve the most frequent issues encountered when using Magic Vibe.

## Installation Issues

### Magic Vibe Directory Not Created

**Problem**: The `.magic-vibe` directory is missing or incomplete.

**Symptoms**:

- AI assistant doesn't recognize Magic Vibe system
- "Directory not found" errors
- Missing essential files

**Solutions**:

1. **Check Directory Structure**

   ```bash
   ls -la .magic-vibe/
   ```

2. **Recreate Structure**

   ```bash
   mkdir -p .magic-vibe/ai/{plans,tasks,memory,hooks}
   mkdir -p .magic-vibe/rules
   mkdir -p .magic-vibe/doc
   ```

3. **Create Essential Files**

   ```bash
   touch .magic-vibe/ai/PLANS.md
   touch .magic-vibe/ai/TASKS.md
   touch .magic-vibe/ai/memory/TASKS_LOG.md
   ```

4. **Verify Permissions**

   ```bash
   # Unix/macOS
   chmod -R 755 .magic-vibe/
   
   # Windows - ensure you have write permissions
   ```

### Git Conflicts with Magic Vibe Files

**Problem**: Git conflicts when committing Magic Vibe files.

**Symptoms**:

- Merge conflicts in `.magic-vibe/` files
- Git refuses to commit Magic Vibe changes
- "File is in the way" errors

**Solutions**:

1. **Check Git Status**

   ```bash
   git status .magic-vibe/
   ```

2. **Add Magic Vibe to Git**

   ```bash
   git add .magic-vibe/
   git commit -m "Add Magic Vibe system"
   ```

3. **Resolve Conflicts**

   ```bash
   # For task files, keep both versions and merge manually
   git checkout --ours .magic-vibe/ai/TASKS.md
   git checkout --theirs .magic-vibe/ai/TASKS.md
   # Then manually merge the content
   ```

4. **Update .gitignore (if needed)**

   ```gitignore
   # Optional: exclude temporary files
   .magic-vibe/ai/memory/temp_*
   .magic-vibe/.cache/
   ```

## AI Integration Issues

### AI Assistant Doesn't Recognize Rules

**Problem**: AI doesn't apply Magic Vibe rules automatically.

**Symptoms**:

- Rules not being followed
- No rule discovery feedback
- AI generates non-compliant code

**Solutions**:

1. **Explicit Rule Reference**

   ```text
   @.magic-vibe/rules/_index.md analyze this project and apply relevant rules
   ```

2. **Check Rule Files**

   ```bash
   ls -la .magic-vibe/rules/
   ```

3. **Verify Rule Format**
   - Ensure rules follow 8-section structure
   - Check markdown syntax
   - Validate file naming conventions

4. **Manual Rule Application**

   ```text
   @.magic-vibe/rules/core/tasks.md help me with task management
   ```

### Context Not Maintained Between Sessions

**Problem**: AI loses project context between conversations.

**Symptoms**:

- Repeating explanations
- Forgetting project details
- Inconsistent rule application

**Solutions**:

1. **Initialize Context**

   ```text
   Read the current Magic Vibe project status and refresh context
   ```

2. **Reference Active Files**

   ```text
   @.magic-vibe/ai/PLANS.md @.magic-vibe/ai/TASKS.md show current project status
   ```

3. **Update Memory Files**

   ```bash
   # Ensure memory files are current
   ls -la .magic-vibe/ai/memory/
   ```

4. **Restart with Context**

   ```text
   Initialize Magic Vibe for this project and load all current plans and tasks
   ```

## Rule System Issues

### Rule Conflicts

**Problem**: Multiple rules provide conflicting guidance.

**Symptoms**:

- Contradictory AI suggestions
- Inconsistent code generation
- Rule application errors

**Solutions**:

1. **Check Rule Hierarchy**

   ```text
   @.magic-vibe/rules/_index.md show me the current rule priority order
   ```

2. **Identify Conflicts**
   - Review applied rules
   - Check for contradictory requirements
   - Identify overlapping rule categories

3. **Resolve Manually**

   ```text
   For this task, prioritize @.magic-vibe/rules/languages/python.md over general coding rules
   ```

4. **Update Rule Priorities**
   - Edit rule files to clarify precedence
   - Add conflict resolution notes
   - Document decision rationale

### Rules Not Being Applied

**Problem**: Specific rules are ignored during development.

**Symptoms**:

- Code doesn't follow established patterns
- Missing required components
- Quality standards not enforced

**Solutions**:

1. **Explicit Rule Invocation**

   ```text
   @.magic-vibe/rules/languages/typescript.md ensure this code follows TypeScript best practices
   ```

2. **Check Rule Validity**
   - Verify rule file syntax
   - Ensure proper section structure
   - Validate rule logic

3. **Update Rule Content**
   - Add specific examples
   - Clarify requirements
   - Include validation criteria

## Task Management Issues

### Tasks Not Updating Status

**Problem**: Task status doesn't reflect actual progress.

**Symptoms**:

- Completed tasks still show "In Progress"
- Status changes not saved
- Inconsistent task tracking

**Solutions**:

1. **Manual Status Update**

   ```text
   @.magic-vibe/rules/core/tasks.md update task TASK-001 status to completed
   ```

2. **Check Task File Format**

   ```markdown
   **Status**: Completed  # Ensure correct format
   ```

3. **Verify File Permissions**

   ```bash
   ls -la .magic-vibe/ai/tasks/
   chmod 644 .magic-vibe/ai/tasks/*.md
   ```

4. **Refresh Task Index**

   ```text
   Regenerate the TASKS.md index file from current task files
   ```

### Task Dependencies Not Working

**Problem**: Dependent tasks don't recognize prerequisites.

**Symptoms**:

- Tasks start before prerequisites complete
- Dependency warnings ignored
- Incorrect task sequencing

**Solutions**:

1. **Check Dependency Format**

   ```markdown
   ### Prerequisites
   - TASK-001: Authentication Setup (Completed)
   - TASK-002: Database Schema (In Progress)
   ```

2. **Validate Task IDs**
   - Ensure consistent task ID format
   - Check for typos in references
   - Verify task file names

3. **Update Dependencies**

   ```text
   @.magic-vibe/rules/core/tasks.md fix dependencies for task TASK-003
   ```

## Performance Issues

### Slow Rule Discovery

**Problem**: Magic Vibe takes too long to analyze project.

**Symptoms**:

- Long delays before rule application
- Timeout errors during analysis
- System becomes unresponsive

**Solutions**:

1. **Reduce Project Scope**

   ```bash
   # Add to .gitignore to exclude large directories
   node_modules/
   build/
   dist/
   .next/
   ```

2. **Clear Cache**

   ```bash
   rm -rf .magic-vibe/.cache/  # If cache directory exists
   ```

3. **Incremental Analysis**

   ```text
   Analyze only the src/ directory for rule discovery
   ```

4. **Optimize Rule Files**
   - Remove unused rules
   - Simplify complex rule logic
   - Reduce rule file sizes

### Memory Usage Issues

**Problem**: Magic Vibe consumes too much system resources.

**Symptoms**:

- High memory usage
- System slowdown
- Editor becomes unresponsive

**Solutions**:

1. **Archive Old Data**

   ```bash
   # Move old tasks to memory
   mv .magic-vibe/ai/tasks/2024-* .magic-vibe/ai/memory/
   ```

2. **Clean Memory Files**

   ```bash
   # Remove old log files
   find .magic-vibe/ai/memory/ -name "*.log" -mtime +30 -delete
   ```

3. **Limit Active Items**
   - Keep only current plans active
   - Archive completed tasks regularly
   - Reduce concurrent task count

## File System Issues

### Permission Denied Errors

**Problem**: Cannot read or write Magic Vibe files.

**Symptoms**:

- "Permission denied" errors
- Cannot create new files
- Updates not saved

**Solutions**:

1. **Check File Permissions**

   ```bash
   # Unix/macOS
   ls -la .magic-vibe/
   chmod -R 755 .magic-vibe/
   
   # Windows - run as administrator or check folder permissions
   ```

2. **Fix Ownership**

   ```bash
   # Unix/macOS
   sudo chown -R $USER:$USER .magic-vibe/
   ```

3. **Verify Disk Space**

   ```bash
   df -h .  # Check available disk space
   ```

### File Corruption

**Problem**: Magic Vibe files become corrupted or unreadable.

**Symptoms**:

- Malformed markdown content
- AI cannot parse files
- Syntax errors in generated content

**Solutions**:

1. **Restore from Git**

   ```bash
   git checkout HEAD -- .magic-vibe/ai/TASKS.md
   ```

2. **Validate File Format**

   ```bash
   # Check for invalid characters
   cat -A .magic-vibe/ai/TASKS.md
   ```

3. **Recreate Corrupted Files**

   ```text
   @.magic-vibe/rules/core/tasks.md recreate the TASKS.md file from individual task files
   ```

## Integration Issues

### Editor-Specific Problems

**Problem**: Magic Vibe doesn't work properly with specific AI editors.

**Symptoms**:

- Editor doesn't recognize configurations
- Rules not applied automatically
- Context switching issues

**Solutions**:

1. **Check Editor Configuration**

   ```bash
   # Ensure correct directory naming
   ls -la | grep -E '\.(cursor|windsurf|vscode|qoder)'
   ```

2. **Copy Configurations**

   ```bash
   # Copy Magic Vibe rules to editor directory
   cp .magic-vibe/rules/core/* .cursor/
   ```

3. **Restart Editor**
   - Close and reopen the editor
   - Reload the workspace
   - Clear editor cache if available

### CI/CD Integration Issues

**Problem**: Magic Vibe doesn't work in automated environments.

**Symptoms**:

- CI/CD pipelines fail
- Automation scripts error
- Missing dependencies in build environment

**Solutions**:

1. **Check Build Environment**

   ```yaml
   # In CI/CD configuration
   - name: Verify Magic Vibe
     run: |
       ls -la .magic-vibe/
       test -f .magic-vibe/ai/PLANS.md
   ```

2. **Add Dependencies**

   ```yaml
   # Ensure required tools are available
   - name: Install dependencies
     run: |
       apt-get update
       apt-get install -y git
   ```

3. **Set Permissions**

   ```yaml
   - name: Fix permissions
     run: chmod -R 755 .magic-vibe/
   ```

## Getting Additional Help

### Diagnostic Information

When seeking help, provide:

1. **System Information**

   ```bash
   # Operating system and version
   uname -a
   
   # Git version
   git --version
   
   # Editor information
   # (specific to your AI editor)
   ```

2. **Magic Vibe Status**

   ```bash
   # Directory structure
   find .magic-vibe -type f | head -20
   
   # File sizes
   du -sh .magic-vibe/*
   
   # Recent changes
   git log --oneline .magic-vibe/ | head -5
   ```

3. **Error Details**
   - Exact error messages
   - Steps to reproduce
   - Expected vs actual behavior
   - Recent changes made

### Support Channels

- **GitHub Issues**: [Report bugs and issues](https://github.com/teratron/magic-vibe/issues)
- **GitHub Discussions**: [Ask questions and share ideas](https://github.com/teratron/magic-vibe/discussions)
- **Documentation**: [Browse complete documentation](../README.md)

### Self-Diagnosis Script

Create a diagnostic script:

```bash
#!/bin/bash
# .magic-vibe/diagnose.sh

echo "Magic Vibe Diagnostic Report"
echo "============================"
echo "Date: $(date)"
echo "System: $(uname -a)"
echo ""

echo "Directory Structure:"
find .magic-vibe -type f | head -20
echo ""

echo "File Status:"
ls -la .magic-vibe/ai/
echo ""

echo "Git Status:"
git status .magic-vibe/ --porcelain
echo ""

echo "Recent Activity:"
git log --oneline .magic-vibe/ | head -5
echo ""

echo "Permissions:"
ls -la .magic-vibe/
echo ""

echo "Disk Usage:"
du -sh .magic-vibe/*
echo ""

echo "Diagnostic complete!"
```

Run with:

```bash
chmod +x .magic-vibe/diagnose.sh
./.magic-vibe/diagnose.sh
```

---

Most Magic Vibe issues can be resolved with these troubleshooting steps. For persistent problems, please use the support channels with diagnostic information.
