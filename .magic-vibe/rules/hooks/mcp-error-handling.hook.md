---
description: MCP error handling and recovery hook that manages failed MCP connections and provides fallback mechanisms for failed tasks.
type: task_status_change
trigger: failed
priority: 20
enabled: true
---

### MCP Error Handling and Recovery

This hook manages MCP client errors, provides diagnostic information, and implements recovery strategies when a task fails.

```bash
# MCP Error Handling and Recovery
TASK_ID="{{task.id}}"
ERROR_LOG="{{task.error_log}}"

# Check if MCP configuration exists for this task
if [ -f ".magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json" ]; then
    
    # Log error details
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) - Task $TASK_ID failed with MCP integration. Error: $ERROR_LOG" >> .magic-vibe/ai/mcp-clients/error.log
    
    # Execute error diagnostic script if exists
    if [ -f ".magic-vibe/ai/mcp-clients/diagnose-errors.py" ]; then
        python .magic-vibe/ai/mcp-clients/diagnose-errors.py --task-id=$TASK_ID --error="$ERROR_LOG"
    fi
    
    # Gracefully disconnect all MCP clients
    if [ -f ".magic-vibe/ai/mcp-clients/emergency-cleanup.py" ]; then
        python .magic-vibe/ai/mcp-clients/emergency-cleanup.py --task-id=$TASK_ID
    fi
    
    # Update MCP config with error information
    python3 << EOF
import json
import os
from datetime import datetime

config_path = ".magic-vibe/ai/mcp-clients/$TASK_ID/mcp-config.json"
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    config['failedAt'] = datetime.utcnow().isoformat() + 'Z'
    config['errorLog'] = '$ERROR_LOG'
    config['finalStatus'] = 'failed'
    
    if 'errors' not in config:
        config['errors'] = []
    
    config['errors'].append({
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'error': '$ERROR_LOG',
        'taskId': '$TASK_ID'
    })
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
EOF
    
    # Archive failed task MCP data for analysis
    mkdir -p .magic-vibe/ai/memory/mcp-failures
    cp -r ".magic-vibe/ai/mcp-clients/$TASK_ID" ".magic-vibe/ai/memory/mcp-failures/"
    
    # Generate failure report
    if [ -f ".magic-vibe/ai/mcp-clients/generate-failure-report.py" ]; then
        python .magic-vibe/ai/mcp-clients/generate-failure-report.py --task-id=$TASK_ID --failure-path=.magic-vibe/ai/memory/mcp-failures/$TASK_ID
    fi
    
    # Cleanup active MCP resources
    rm -rf ".magic-vibe/ai/mcp-clients/$TASK_ID"
fi
```
