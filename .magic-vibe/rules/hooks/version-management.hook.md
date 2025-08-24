---
type: documentation_update
trigger: generated
priority: 5
enabled: true
---

# Version Management Hook for Documentation Generation

This hook automatically manages version tracking and updates when documentation is generated or updated.

```bash
#!/bin/bash

# Version Management for Documentation Generation
VERSION_FILE=".vscode/rules/.magic-vibe/version.json"
DOCS_EN_README="docs/en/README.md"
DOCS_RU_README="docs/ru/README.md"
MAIN_README="README.md"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
READABLE_TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

echo "🔄 Running version management for documentation generation..."

# Function to get version from JSON file
get_version() {
    local type=$1
    local field=$2
    if [ -f "$VERSION_FILE" ]; then
        python3 -c "
import json
try:
    with open('$VERSION_FILE', 'r') as f:
        data = json.load(f)
    print(data.get('$type', {}).get('$field', 'unknown'))
except:
    print('unknown')
"
    else
        echo "unknown"
    fi
}

# Function to update version in JSON file
update_version() {
    local type=$1
    local field=$2
    local value=$3
    
    if [ ! -f "$VERSION_FILE" ]; then
        echo "⚠️ Version file not found: $VERSION_FILE"
        return 1
    fi
    
    python3 -c "
import json
try:
    with open('$VERSION_FILE', 'r') as f:
        data = json.load(f)
    
    if '$type' not in data:
        data['$type'] = {}
    
    data['$type']['$field'] = '$value'
    
    with open('$VERSION_FILE', 'w') as f:
        json.dump(data, f, indent=2)
    print('✅ Updated $type.$field to $value')
except Exception as e:
    print(f'❌ Error: {e}')
"
}

# Update documentation metadata
update_version "documentation" "last_updated" "$TIMESTAMP"
update_version "task_magic" "last_hook_execution" "$TIMESTAMP"

# Get current versions for display
project_version=$(get_version "project" "version")
doc_version=$(get_version "documentation" "version")
task_magic_version=$(get_version "task_magic" "system_version")
generation_count=$(get_version "documentation" "generation_count")

# Update main documentation README files with current version info
if [ -f "$DOCS_EN_README" ]; then
    # Update English documentation version info
    sed -i "s/Documentation Version.*$/Documentation Version](https:\/\/img.shields.io\/badge\/Docs-v${doc_version}-green.svg)](..\/)/g" "$DOCS_EN_README"
    sed -i "s/Project Version.*$/Project Version](https:\/\/img.shields.io\/badge\/Project-v${project_version}-blue.svg)](https:\/\/github.com\/zigenzoog\/template-ai-rules\/releases)/g" "$DOCS_EN_README"
    sed -i "s/Magic Vibe.*$/Magic Vibe](https:\/\/img.shields.io\/badge\/Task%20Magic-v${task_magic_version}-orange.svg)](..\/\.vscode\/rules\/\.task-magic\/)/g" "$DOCS_EN_README"
    
    # Update version information section
    sed -i "s/- \*\*Documentation Version:\*\* .*/- **Documentation Version:** ${doc_version}/g" "$DOCS_EN_README"
    sed -i "s/- \*\*Project Version:\*\* .*/- **Project Version:** ${project_version}/g" "$DOCS_EN_README"
    sed -i "s/- \*\*Magic Vibe System:\*\* .*/- **Magic Vibe System:** v${task_magic_version}/g" "$DOCS_EN_README"
    sed -i "s/- \*\*Last Updated:\*\* .*/- **Last Updated:** ${READABLE_TIMESTAMP}/g" "$DOCS_EN_README"
    
    # Update footer
    sed -i "s/\*Documentation Version: v.* |/\*Documentation Version: v${doc_version} |/g" "$DOCS_EN_README"
    sed -i "s/| Project Version: v.*\*/| Project Version: v${project_version}\*/g" "$DOCS_EN_README"
    sed -i "s/\*Last Updated: .* |/\*Last Updated: ${READABLE_TIMESTAMP} |/g" "$DOCS_EN_README"
    sed -i "s/| Generation Count: .*\*/| Generation Count: ${generation_count}\*/g" "$DOCS_EN_README"
    
    echo "✅ Updated English documentation version info"
fi

if [ -f "$DOCS_RU_README" ]; then
    # Update Russian documentation version info
    sed -i "s/Версия документации.*$/Версия документации](https:\/\/img.shields.io\/badge\/Докс-v${doc_version}-green.svg)](..\/)/g" "$DOCS_RU_README"
    sed -i "s/Версия проекта.*$/Версия проекта](https:\/\/img.shields.io\/badge\/Проект-v${project_version}-blue.svg)](https:\/\/github.com\/zigenzoog\/template-ai-rules\/releases)/g" "$DOCS_RU_README"
    sed -i "s/Magic Vibe.*$/Magic Vibe](https:\/\/img.shields.io\/badge\/Task%20Magic-v${task_magic_version}-orange.svg)](..\/\.vscode\/rules\/\.task-magic\/)/g" "$DOCS_RU_README"
    
    # Update version information section (Russian)
    sed -i "s/- \*\*Версия документации:\*\* .*/- **Версия документации:** ${doc_version}/g" "$DOCS_RU_README"
    sed -i "s/- \*\*Версия проекта:\*\* .*/- **Версия проекта:** ${project_version}/g" "$DOCS_RU_README"
    sed -i "s/- \*\*Система Magic Vibe:\*\* .*/- **Система Magic Vibe:** v${task_magic_version}/g" "$DOCS_RU_README"
    sed -i "s/- \*\*Последнее обновление:\*\* .*/- **Последнее обновление:** ${READABLE_TIMESTAMP}/g" "$DOCS_RU_README"
    
    # Update footer (Russian)
    sed -i "s/\*Версия документации: v.* |/\*Версия документации: v${doc_version} |/g" "$DOCS_RU_README"
    sed -i "s/| Версия проекта: v.*\*/| Версия проекта: v${project_version}\*/g" "$DOCS_RU_README"
    sed -i "s/\*Последнее обновление: .* |/\*Последнее обновление: ${READABLE_TIMESTAMP} |/g" "$DOCS_RU_README"
    sed -i "s/| Номер генерации: .*\*/| Номер генерации: ${generation_count}\*/g" "$DOCS_RU_README"
    
    echo "✅ Updated Russian documentation version info"
fi

echo "🏁 Version management completed successfully"
echo "📊 Current Status:"
echo "   📋 Project Version: v${project_version}"
echo "   📖 Documentation Version: v${doc_version}"
echo "   🔧 Magic Vibe System: v${task_magic_version}"
echo "   📈 Generation Count: ${generation_count}"
echo "   ⏰ Last Updated: ${READABLE_TIMESTAMP}"
```
