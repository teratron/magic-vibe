---
type: plan_creation
trigger: created
priority: 15
enabled: true
---

# Project Documentation Update on Plan Creation

This hook updates the main project documentation index when a new plan is created.

```bash
# Update project documentation index
echo "Updating project documentation index for new plan: {{plan.title}}"

# Create docs directory structure if it doesn't exist
mkdir -p docs/en docs/ru

# Update English documentation index
cat >> "docs/en/README.md" << 'EOF'

## {{plan.title}}

**Plan File:** {{plan.path}}  
**Created:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")

[Plan description and details will be populated here]

EOF

# Update Russian documentation index
cat >> "docs/ru/README.md" << 'EOF'

## {{plan.title}}

**Файл плана:** {{plan.path}}  
**Создан:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")

[Описание и детали плана будут добавлены здесь]

EOF

echo "Project documentation index updated for plan: {{plan.title}}"
```
