---
type: git_push
trigger: before
priority: 1
enabled: true
---

# Run Tests Before Pushing

This hook acts as a quality gate, ensuring that all project tests pass before the agent is allowed to push code to the remote repository.

If the test command fails (returns a non-zero exit code), the agent MUST abort the `git push` operation.

```bash
# This command should be adapted to the project's testing framework
# e.g., 'npm test', 'pytest', 'go test ./...', etc.
npm test
```
