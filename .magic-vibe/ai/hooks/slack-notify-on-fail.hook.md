---
type: task_status_change
trigger: failed
priority: 10
enabled: true
---

# Slack Notification on Task Failure

This hook sends a notification to a specified Slack channel when a task's status is changed to `failed`.

It requires a `SLACK_WEBHOOK_URL` environment variable to be set with the incoming webhook URL for your Slack workspace.

```bash
# Check if the webhook URL is set
if [ -z "$SLACK_WEBHOOK_URL" ]; then
  echo "Error: SLACK_WEBHOOK_URL environment variable is not set. Cannot send Slack notification."
  exit 1
fi

# Prepare the JSON payload using Slack Block Kit for better formatting
JSON_PAYLOAD=$(cat <<EOF
{
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": ":x: Task Failed: {{task.title}}",
        "emoji": true
      }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Task ID:*\n`{{task.id}}`" },
        { "type": "mrkdwn", "text": "*File:*\n`{{task.path}}`" }
      ]
    },
    { "type": "divider" },
    { "type": "section", "text": { "type": "mrkdwn", "text": "*Reason for Failure:*\n```{{task.error_log}}```" } }
  ]
}
EOF
)

# Send the notification using curl
curl -X POST -H 'Content-type: application/json' --data "$JSON_PAYLOAD" "$SLACK_WEBHOOK_URL"
```
