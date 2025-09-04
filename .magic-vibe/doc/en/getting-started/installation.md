# Installation Guide

This guide provides detailed instructions for installing and configuring Magic Vibe in your development environment.

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Git**: Version 2.20 or higher
- **Storage**: 50MB free space for Magic Vibe files
- **Memory**: 512MB RAM (minimal impact on system resources)

### Recommended Setup

- **AI Code Editor**: Cursor, Windsurf, VS Code with AI extensions
- **Terminal**: PowerShell (Windows), Zsh/Bash (macOS/Linux)
- **Node.js**: v16+ (for JavaScript/TypeScript projects)
- **Python**: 3.8+ (for Python projects)

## Installation Methods

### Method 1: Direct Clone (Recommended)

Clone the Magic Vibe template repository:

```bash
# Clone the template
git clone https://github.com/teratron/magic-vibe.git temp-magic-vibe

# Copy Magic Vibe to your project
cp -r temp-magic-vibe/.magic-vibe /path/to/your/project/

# Clean up
rm -rf temp-magic-vibe
```

### Method 2: Manual Setup

Create the Magic Vibe structure manually:

```bash
# Navigate to your project
cd /path/to/your/project

# Create directory structure
mkdir -p .magic-vibe/{ai/{plans,tasks,memory,hooks},rules,doc}

# Create essential files
touch .magic-vibe/ai/PLANS.md
touch .magic-vibe/ai/TASKS.md
touch .magic-vibe/ai/memory/TASKS_LOG.md

# Copy rules from template (if available)
# curl -L https://github.com/teratron/magic-vibe/archive/main.zip | unzip -
```

### Method 3: Package Manager (Future)

```bash
# NPM (planned)
npm install -g magic-vibe-cli
magic-vibe init

# Homebrew (planned)
brew install magic-vibe
magic-vibe init
```

## AI Editor Configuration

### Cursor IDE

```bash
# If you have .vscode folder, rename it
mv .vscode .cursor

# Or create new Cursor configuration
mkdir .cursor
cp .magic-vibe/rules/core/* .cursor/
```

### Windsurf

```bash
# Configure for Windsurf
mv .vscode .windsurf
# or
mkdir .windsurf
cp .magic-vibe/rules/core/* .windsurf/
```

### VS Code with AI Extensions

```bash
# Keep existing .vscode or create new
mkdir -p .vscode
cp .magic-vibe/rules/core/* .vscode/
```

### Other AI Editors

```bash
# For Qoder, Trae, Kiro, etc.
mkdir .{editor-name}
cp .magic-vibe/rules/core/* .{editor-name}/
```

## Project Integration

### Existing Projects

For projects with existing code:

1. **Backup Current Configuration**

   ```bash
   cp -r .vscode .vscode.backup  # If exists
   cp -r .gitignore .gitignore.backup
   ```

2. **Install Magic Vibe**

   ```bash
   # Follow Method 1 or 2 above
   ```

3. **Merge Configurations**

   ```bash
   # Manually merge any existing AI configurations
   # with Magic Vibe rules
   ```

### New Projects

For new projects:

1. **Initialize Git Repository**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Install Magic Vibe**

   ```bash
   # Follow installation method above
   ```

3. **Create Initial Plan**

   ```bash
   # Use AI assistant to create first plan
   ```

## Configuration

### Basic Configuration

Create `.magic-vibe/config.json` (optional):

```json
{
  "version": "2.1.0",
  "project": {
    "name": "Your Project Name",
    "type": "web-app",
    "languages": ["typescript", "python"],
    "frameworks": ["react", "fastapi"]
  },
  "rules": {
    "autoDetect": true,
    "strictMode": false,
    "customRules": []
  },
  "integrations": {
    "git": true,
    "cicd": true,
    "hooks": true
  }
}
```

### Git Integration

Add Magic Vibe to your `.gitignore` (optional):

```gitignore
# Magic Vibe (optional - usually you want to track these)
# .magic-vibe/ai/memory/
# .magic-vibe/ai/hooks/user_*
```

### Environment Variables

Set up environment variables (optional):

```bash
# Windows (PowerShell)
$env:MAGIC_VIBE_AUTO_DETECT = "true"
$env:MAGIC_VIBE_STRICT_MODE = "false"

# macOS/Linux (Bash/Zsh)
export MAGIC_VIBE_AUTO_DETECT=true
export MAGIC_VIBE_STRICT_MODE=false
```

## Verification

### Check Installation

Verify Magic Vibe is properly installed:

```bash
# Check directory structure
ls -la .magic-vibe/

# Verify essential files exist
ls -la .magic-vibe/ai/
ls -la .magic-vibe/rules/
```

### Test AI Integration

Test with your AI assistant:

```text
Check if Magic Vibe is properly installed in this project
```

Expected response should include:

- Magic Vibe system detected
- Project analysis results
- Applied rules summary

### Validate Rules

Check rule discovery:

```text
@.magic-vibe/rules/_index.md show me the current rule status
```

## Troubleshooting Installation

### Common Issues

1. **Permission Denied**

   ```bash
   # Fix permissions (Unix/macOS)
   chmod -R 755 .magic-vibe/
   
   # Windows - run as administrator
   ```

2. **Directory Already Exists**

   ```bash
   # Backup and reinstall
   mv .magic-vibe .magic-vibe.backup
   # Reinstall Magic Vibe
   ```

3. **Git Conflicts**

   ```bash
   # Resolve git conflicts
   git add .magic-vibe/
   git commit -m "Add Magic Vibe system"
   ```

### Validation Script

Create validation script `.magic-vibe/validate.sh`:

```bash
#!/bin/bash
echo "Magic Vibe Installation Validation"
echo "=================================="

# Check directories
if [ -d ".magic-vibe/ai" ]; then
    echo "✅ AI workspace directory exists"
else
    echo "❌ AI workspace directory missing"
fi

if [ -d ".magic-vibe/rules" ]; then
    echo "✅ Rules directory exists"
else
    echo "❌ Rules directory missing"
fi

# Check essential files
if [ -f ".magic-vibe/ai/PLANS.md" ]; then
    echo "✅ PLANS.md exists"
else
    echo "❌ PLANS.md missing"
fi

if [ -f ".magic-vibe/ai/TASKS.md" ]; then
    echo "✅ TASKS.md exists"
else
    echo "❌ TASKS.md missing"
fi

echo "Installation validation complete!"
```

Run validation:

```bash
chmod +x .magic-vibe/validate.sh
./.magic-vibe/validate.sh
```

## Next Steps

After successful installation:

1. 📖 Read the [Quick Start Guide](quick-start.md)
2. 🏗️ Learn about [System Architecture](../core-concepts/architecture.md)
3. 📝 Create your [First Plan](../user-guides/plans.md)
4. ⚙️ Set up [Automation Hooks](../user-guides/hooks.md)

## Uninstallation

To remove Magic Vibe:

```bash
# Remove Magic Vibe directory
rm -rf .magic-vibe/

# Remove editor configurations (optional)
rm -rf .cursor/  # or .windsurf/, .qoder/, etc.

# Clean git history (optional)
git filter-branch --tree-filter 'rm -rf .magic-vibe' HEAD
```

---

Magic Vibe is now ready to enhance your AI-assisted development workflow!
