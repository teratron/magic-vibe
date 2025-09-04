---
description: MCP client cleanup and resource management hook that properly disconnects all MCP clients and logs execution results when a task completes.
type: task_status_change
trigger: completed
priority: 15
enabled: true
---

### MCP Client Cleanup and Results Collection

This hook manages MCP client disconnection, collects execution results, and archives task-specific MCP data when a task completes.

```bash
# MCP Client Cleanup and Results Collection
TASK_ID="{{task.id}}"
TASK_STATUS="{{task.status}}"

# Check if MCP configuration exists for this task
if [ -f ".magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json" ]; then
    
    # Execute cleanup script if exists
    if [ -f ".magic-vibe/ai/mcp-clients/cleanup-clients.py" ]; then
        python .magic-vibe/ai/mcp-clients/cleanup-clients.py --task-id=$TASK_ID --status=$TASK_STATUS
    fi
    
    # Archive MCP execution data
    mkdir -p .magic-vibe/ai/memory/mcp-executions
    
    # Add completion timestamp to config
    python3 << EOF
import json
import os
from datetime import datetime

config_path = ".magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json"
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    config['completedAt'] = datetime.utcnow().isoformat() + 'Z'
    config['finalStatus'] = '$TASK_STATUS'
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
EOF
    
    # Move task MCP data to memory archive
    mv ".magic-vibe/ai/mcp-clients/$TASK_ID" ".magic-vibe/ai/memory/mcp-executions/"
    
    # Log completion
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) - Completed MCP orchestration for task $TASK_ID with status: $TASK_STATUS" >> .magic-vibe/ai/mcp-clients/orchestration.log
    
    # Generate MCP execution summary
    if [ -f ".magic-vibe/ai/mcp-clients/generate-summary.py" ]; then
        python .magic-vibe/ai/mcp-clients/generate-summary.py --task-id=$TASK_ID --archive-path=.magic-vibe/ai/memory/mcp-executions/$TASK_ID
    fi
fi
```
