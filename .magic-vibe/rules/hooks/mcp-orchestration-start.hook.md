---
description: Multi-MCP client task system hook for orchestrating multiple Model Context Protocol connections and managing distributed task execution.
type: task_status_change
trigger: inprogress
priority: 5
enabled: true
---

# Multi-MCP Client Orchestration Hook

This hook initializes and manages multiple MCP client connections when a task requiring external system integration starts.

```bash
# Multi-MCP Client Task Orchestration
TASK_ID="{{task.id}}"
TASK_TITLE="{{task.title}}"
FEATURE="{{task.feature}}"

# Create MCP clients directory structure
mkdir -p .magic-vibe/ai/mcp-clients/$TASK_ID

# Initialize MCP configuration for the task
cat > .magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json << 'EOF'
{
  "taskId": "{{task.id}}",
  "taskTitle": "{{task.title}}",
  "feature": "{{task.feature}}",
  "mcpClients": {},
  "activeConnections": [],
  "executionLog": [],
  "startedAt": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

# Log task orchestration start
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) - Started MCP orchestration for task {{task.id}}: {{task.title}}" >> .magic-vibe/ai/mcp-clients/orchestration.log

# Execute MCP client initialization script if exists
if [ -f ".magic-vibe/ai/mcp-clients/init-clients.py" ]; then
    python .magic-vibe/ai/mcp-clients/init-clients.py --task-id={{task.id}} --config-path=.magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json
fi
```
