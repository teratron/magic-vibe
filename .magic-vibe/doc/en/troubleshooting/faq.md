# Frequently Asked Questions

Common questions and answers about Magic Vibe system.

## General Questions

### What is Magic Vibe?

**Q**: What exactly is Magic Vibe and how does it differ from other development tools?

**A**: Magic Vibe is an intelligent AI agent workflow management framework that provides:

- **File-based project management** for plans and tasks
- **Dynamic rule discovery** that automatically detects and applies relevant coding standards
- **AI-optimized structure** designed specifically for AI coding assistants
- **Cross-editor compatibility** working with Cursor, Windsurf, VS Code, and other AI editors

Unlike traditional project management tools, Magic Vibe is specifically designed for AI-assisted development workflows.

### How does Magic Vibe work with AI assistants?

**Q**: How does my AI coding assistant understand and use Magic Vibe?

**A**: Magic Vibe integrates with AI assistants through:

- **@-tag references** to specific rule files (e.g., `@.magic-vibe/rules/core/tasks.md`)
- **Automatic context detection** based on project analysis
- **Structured markdown files** that AI can easily understand and follow
- **Clear rule hierarchies** that prevent conflicts and ensure consistent application

### Is Magic Vibe free to use?

**Q**: What are the licensing and cost implications of using Magic Vibe?

**A**: Magic Vibe is completely free and open-source under the MIT license. You can:

- Use it in personal and commercial projects
- Modify it for your specific needs
- Distribute your modifications
- No subscription fees or usage limits

## Installation and Setup

### What are the system requirements?

**Q**: What do I need to run Magic Vibe?

**A**: Minimum requirements:

- Any operating system (Windows, macOS, Linux)
- Git version 2.20+
- A text editor (preferably with AI assistance)
- 50MB free disk space
- Basic familiarity with markdown files

### Can I use Magic Vibe with my existing project?

**Q**: How do I add Magic Vibe to a project that already has code and configuration?

**A**: Yes! Magic Vibe is designed for easy integration:

1. **Backup existing configurations**:

   ```bash
   cp -r .vscode .vscode.backup
   ```

2. **Install Magic Vibe**:

   ```bash
   mkdir -p .magic-vibe/ai/{plans,tasks,memory,hooks}
   ```

3. **Let AI analyze your project**:

   ```text
   Initialize Magic Vibe for this existing project and analyze the codebase
   ```

Magic Vibe will detect your existing technologies and apply relevant rules automatically.

### Which AI editors are supported?

**Q**: Can I use Magic Vibe with my preferred AI coding assistant?

**A**: Magic Vibe supports all major AI editors:

- **Cursor** (`.cursor`)
- **Windsurf** (`.windsurf`)
- **VS Code** with AI extensions (`.vscode`)
- **Qoder** (`.qoder`)
- **Trae** (`.trae`)
- **Kiro** (`.kiro`)
- **Any AI-powered editor** (custom directory naming)

The system is editor-agnostic and works through standard markdown files.

## Rules and Standards

### How does rule discovery work?

**Q**: How does Magic Vibe automatically detect which rules to apply?

**A**: Magic Vibe uses intelligent context detection:

1. **Language Detection**: Scans file extensions (`.py`, `.ts`, `.js`, etc.)
2. **Framework Recognition**: Analyzes config files (`package.json`, `requirements.txt`)
3. **Build Tool Detection**: Identifies build systems (`Makefile`, `CMakeLists.txt`)
4. **Dependency Analysis**: Reviews project dependencies
5. **Pattern Matching**: Recognizes common project structures

Rules are then applied in priority order: Core → Language → Framework → Workflow → Principles.

### Can I create custom rules?

**Q**: How do I add my own coding standards and practices?

**A**: Yes! Create custom rules by:

1. **Adding custom rule files**:

   ```bash
   mkdir .magic-vibe/rules/custom
   ```

2. **Following the 8-section structure**:
   - Code Generation
   - Change Management  
   - Communication
   - Quality Assurance
   - Security & Performance
   - Language-Specific Standards
   - Continuous Improvement
   - AI-Specific Best Practices

3. **Referencing your custom rules**:

   ```text
   @.magic-vibe/rules/custom/my-company-standards.md apply company coding standards
   ```

### What happens when rules conflict?

**Q**: How does Magic Vibe handle conflicting rules?

**A**: Magic Vibe uses a sophisticated conflict resolution system:

- **Specificity Wins**: More specific rules override general ones
- **Hierarchy Priority**: Core rules take precedence over principles
- **Composition over Replacement**: Rules complement rather than replace each other
- **Explicit Override**: You can manually specify rule precedence
- **Documentation**: All conflicts are logged and explained

## Plans and Tasks

### What's the difference between plans and tasks?

**Q**: How do plans and tasks relate to each other?

**A**:

**Plans** are high-level Product Requirements Documents (PRDs) that:

- Define feature requirements and specifications
- Provide business context and objectives
- Follow an 8-section structure
- Can span weeks or months

**Tasks** are specific, actionable work items that:

- Break down plans into implementable pieces
- Have clear acceptance criteria
- Typically take hours to days
- Track progress and dependencies

### How do I break down a large feature?

**Q**: What's the best way to decompose complex features into manageable tasks?

**A**: Follow this approach:

1. **Create a comprehensive plan** first using:

   ```text
   @.magic-vibe/rules/core/plans.md create a plan for [feature name]
   ```

2. **Generate tasks from the plan**:

   ```text
   @.magic-vibe/rules/core/tasks.md generate tasks from the [feature] plan
   ```

3. **Review and refine** the generated tasks:
   - Ensure tasks are atomic (can't be meaningfully broken down)
   - Verify clear acceptance criteria
   - Check realistic time estimates
   - Validate dependency relationships

### Can multiple people work on the same plan?

**Q**: How does Magic Vibe support team collaboration?

**A**: Yes! Magic Vibe supports team workflows through:

- **Shared Plans**: Plans visible to all team members
- **Task Assignment**: Clear ownership and responsibility
- **Dependency Tracking**: Understanding of task relationships
- **Progress Visibility**: Real-time status updates
- **Git Integration**: Full version control and history
- **Standardized Format**: Consistent structure across team

## Integration and Workflow

### How does Magic Vibe integrate with Git?

**Q**: How does version control work with Magic Vibe files?

**A**: Magic Vibe is designed for Git integration:

- **All files are trackable**: Markdown files work perfectly with Git
- **Commit integration**: Link commits to task IDs
- **Branch workflows**: Create branches tied to plans or tasks
- **Merge strategies**: Resolve conflicts in plan and task files
- **History preservation**: Full audit trail of project evolution

### Can I use Magic Vibe with CI/CD?

**Q**: How do I integrate Magic Vibe with my automated pipelines?

**A**: Yes! Common CI/CD integrations include:

1. **Task validation**:

   ```yaml
   - name: Validate Magic Vibe structure
     run: test -f .magic-vibe/ai/PLANS.md
   ```

2. **Progress automation**:

   ```yaml
   - name: Update task status on deployment
     run: ./scripts/update-task-status.sh
   ```

3. **Quality gates**:

   ```yaml
   - name: Check plan completion
     run: ./scripts/validate-plan-completion.sh
   ```

### Does Magic Vibe work offline?

**Q**: Can I use Magic Vibe without internet connectivity?

**A**: Absolutely! Magic Vibe is designed for offline use:

- All data stored locally in your project
- No external API calls required
- Works entirely through file system
- AI assistants can work with local context
- Git integration works offline

## Performance and Scaling

### How does Magic Vibe perform with large projects?

**Q**: Will Magic Vibe slow down my development on large codebases?

**A**: Magic Vibe is optimized for performance:

- **Lazy loading**: Rules loaded only when relevant
- **Incremental analysis**: Only scans changed files
- **Efficient storage**: Lightweight markdown files
- **Caching**: Context detection results cached
- **Parallel processing**: Multiple rule categories applied simultaneously

For very large projects:

- Use `.gitignore` to exclude large directories from analysis
- Archive old plans and tasks regularly
- Focus rule discovery on specific directories

### How many plans and tasks can I have?

**Q**: Are there limits on the number of plans and tasks I can create?

**A**: No hard limits! Magic Vibe scales based on:

- **File system capacity**: Limited only by available disk space
- **Git performance**: Large repositories may slow Git operations
- **AI context limits**: Very large context may impact AI performance

**Best practices for scaling**:

- Archive completed items to memory
- Use hierarchical plan structures
- Break large plans into smaller sub-plans
- Regular cleanup of temporary files

## Troubleshooting

### Magic Vibe isn't working with my AI assistant

**Q**: My AI doesn't seem to recognize or use Magic Vibe rules. What's wrong?

**A**: Common solutions:

1. **Explicit rule reference**:

   ```text
   @.magic-vibe/rules/_index.md analyze this project and apply relevant rules
   ```

2. **Check file structure**:

   ```bash
   ls -la .magic-vibe/
   ```

3. **Verify rule format**: Ensure rules follow the 8-section structure

4. **Restart with context**:

   ```text
   Initialize Magic Vibe for this project and load current status
   ```

### Files are not being created or updated

**Q**: Magic Vibe seems to work but files aren't being saved. What should I check?

**A**: Check these common issues:

1. **File permissions**:

   ```bash
   chmod -R 755 .magic-vibe/
   ```

2. **Disk space**:

   ```bash
   df -h .
   ```

3. **Directory structure**:

   ```bash
   mkdir -p .magic-vibe/ai/{plans,tasks,memory}
   ```

4. **Git conflicts**: Resolve any pending merge conflicts

## Best Practices

### What are the recommended workflows?

**Q**: What's the most effective way to use Magic Vibe in my daily development?

**A**: Recommended workflow:

1. **Start with a plan** for any significant feature
2. **Generate tasks** from approved plans
3. **Work on tasks sequentially**, respecting dependencies
4. **Update progress regularly** as you work
5. **Complete tasks** with proper validation
6. **Archive finished items** to maintain clean workspace

### How often should I update plans and tasks?

**Q**: What's the right frequency for maintaining Magic Vibe files?

**A**: Update frequency recommendations:

- **Task progress**: Update at least daily during active work
- **Plan status**: Weekly reviews and updates as needed
- **Dependencies**: Immediately when blockers are identified or resolved
- **Memory archival**: Monthly cleanup of completed items
- **Rule updates**: As needed when standards change

### Should I commit Magic Vibe files to Git?

**Q**: Which Magic Vibe files should be version controlled?

**A**: Recommended Git strategy:

**Always commit**:

- Plans and PRDs (`.magic-vibe/ai/plans/`)
- Active tasks (`.magic-vibe/ai/tasks/`)
- Plan and task indices (`PLANS.md`, `TASKS.md`)
- Custom rules (`.magic-vibe/rules/custom/`)

**Optionally commit**:

- Memory files (`.magic-vibe/ai/memory/`) - useful for team history
- User hooks (`.magic-vibe/ai/hooks/user_*`) - if team-specific

**Don't commit**:

- Temporary files (`.magic-vibe/.temp/`)
- Cache files (`.magic-vibe/.cache/`)
- Personal editor settings

---

Have a question not covered here? [Ask in GitHub Discussions](https://github.com/teratron/magic-vibe/discussions) or [check the full documentation](../README.md).
