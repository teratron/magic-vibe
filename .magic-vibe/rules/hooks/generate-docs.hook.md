---
description: This hook automatically generates or updates project documentation when a task is completed. Documentation is generated in English as the primary language and Russian as a secondary language.
type: task_status_change
trigger: completed
priority: 20
enabled: true
---

# Auto Documentation Generation on Task Completion

```bash
# Generate documentation based on completed task
echo "Generating documentation for task {{task.id}}: {{task.title}}"

# Version management
VERSION_FILE=".vscode/rules/.magic-vibe/version.json"

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
        echo "Version file not found: $VERSION_FILE"
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
except Exception as e:
    print(f'Error: {e}')
"
}

# Function to increment version number
increment_version() {
    local version=$1
    IFS='.' read -ra VERSION_PARTS <<< "$version"
    local major=${VERSION_PARTS[0]:-0}
    local minor=${VERSION_PARTS[1]:-0}
    local patch=${VERSION_PARTS[2]:-0}
    patch=$((patch + 1))
    echo "${major}.${minor}.${patch}"
}

# Update documentation version
current_doc_version=$(get_version "documentation" "version")
new_doc_version=$(increment_version "$current_doc_version")
update_version "documentation" "version" "$new_doc_version"
update_version "documentation" "last_auto_generation" "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Get version info for documentation
project_version=$(get_version "project" "version")
task_magic_version=$(get_version "task_magic" "system_version")

# Create docs directory if it doesn't exist
mkdir -p docs/en docs/ru

# Generate English documentation
cat > "docs/en/task-{{task.id}}-{{task.feature}}.md" << 'EOF'
# {{task.title}}

**Task ID:** {{task.id}}  
**Feature:** {{task.feature}}  
**Status:** {{task.status}}  
**Type:** {{task.commit_type}}

## Version Information

**Project Version:** ${project_version}  
**Documentation Version:** ${new_doc_version}  
**Magic Vibe System:** v${task_magic_version}  
**Generated:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")

## Overview

This documentation was automatically generated upon completion of task {{task.id}}.

## Implementation Details

[This section should be populated with implementation details from the task]

## Testing

[This section should be populated with test results and verification steps]

## Usage

[This section should be populated with usage instructions if applicable]

---

*Generated automatically by Magic Vibe system*
EOF

# Generate Russian documentation
cat > "docs/ru/task-{{task.id}}-{{task.feature}}.md" << 'EOF'
# {{task.title}}

**ID задачи:** {{task.id}}  
**Функциональность:** {{task.feature}}  
**Статус:** {{task.status}}  
**Тип:** {{task.commit_type}}

## Информация о версии

**Версия проекта:** ${project_version}  
**Версия документации:** ${new_doc_version}  
**Система Magic Vibe:** v${task_magic_version}  
**Сгенерировано:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")

## Обзор

Данная документация была автоматически сгенерирована при завершении задачи {{task.id}}.

## Детали реализации

[Этот раздел должен быть заполнен деталями реализации из задачи]

## Тестирование

[Этот раздел должен быть заполнен результатами тестирования и шагами верификации]

## Использование

[Этот раздел должен быть заполнен инструкциями по использованию, если применимо]

---

*Автоматически сгенерировано системой Magic Vibe v${task_magic_version}*
EOF

echo "Documentation generated successfully for task {{task.id}} - Documentation version: ${new_doc_version}"
```
