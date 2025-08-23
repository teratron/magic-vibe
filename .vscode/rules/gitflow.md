---
description: Comprehensive GitFlow workflow guidelines optimized for AI agents. Includes automated validation, branching strategies, and quality gates for enterprise-grade version control.
globs: .git/**, **/.gitignore, **/.gitattributes
---

# GitFlow Workflow Guidelines for AI Agents

## 1. Code Generation Standards

### Branch Naming Conventions

**MANDATORY PATTERNS:**

```text
Feature Branches:    feature/[issue-id]-[description]     (feature/123-user-auth)
Bugfix Branches:     bugfix/[issue-id]-[description]      (bugfix/456-login-fix)
Hotfix Branches:     hotfix/v[X.Y.Z]                     (hotfix/v1.2.1)
Release Branches:    release/v[X.Y.Z]                    (release/v1.3.0)
Experiment Branches: experiment/[description]             (experiment/new-auth)
```

**VALIDATION SCRIPT:**

```bash
#!/bin/bash
# Branch name validation
BRANCH_NAME=$(git symbolic-ref --short HEAD)
VALID_PATTERN="^(feature|bugfix|hotfix|release|experiment)/[a-zA-Z0-9._-]+$"

if [[ ! $BRANCH_NAME =~ $VALID_PATTERN ]]; then
    echo "❌ Invalid branch name: $BRANCH_NAME"
    echo "✅ Valid: feature/123-description, hotfix/v1.2.1"
    exit 1
fi
```

### Commit Message Standards

**CONVENTIONAL COMMITS FORMAT:**

```text
Structure: <type>[scope]: <description>

Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore
Scope: Optional component name (auth, api, ui)
Description: 10-72 characters, imperative mood

Examples:
feat(auth): add JWT token validation
fix(api): resolve null pointer exception
docs(readme): update installation guide
```

**AUTOMATED VALIDATION:**

```bash
#!/bin/bash
# commit-msg hook
COMMIT_MSG=$(cat $1)
PATTERN="^(feat|fix|docs|style|refactor|perf|test|build|ci|chore)(\(.+\))?!?: .{10,72}$"

if [[ ! $COMMIT_MSG =~ $PATTERN ]]; then
    echo "❌ Invalid commit format!"
    echo "✅ Use: type(scope): description"
    exit 1
fi
```

## 2. Change Management

### Branch Lifecycle Management

**MAIN BRANCHES:**

```text
main:     Production-ready code, tagged releases only
develop:  Integration branch, latest development changes

Protection Rules:
- No direct commits
- Require PR reviews (main: 2, develop: 1)
- Require status checks to pass
- Enforce branch up-to-date
```

**FEATURE WORKFLOW:**

```bash
#!/bin/bash
# Automated feature workflow

function create_feature() {
    local issue_id=$1
    local description=$2
    
    git checkout develop
    git pull origin develop
    git checkout -b "feature/${issue_id}-${description}"
    git push -u origin "feature/${issue_id}-${description}"
    
    echo "✅ Created: feature/${issue_id}-${description}"
}

function finish_feature() {
    local branch=$(git symbolic-ref --short HEAD)
    
    # Validation
    if [[ ! $branch =~ ^feature/ ]]; then
        echo "❌ Not on feature branch"
        exit 1
    fi
    
    # Pre-merge checks
    npm test && npm run lint && npm run build
    
    echo "✅ Ready for PR: $branch → develop"
}
```

**RELEASE WORKFLOW:**

```bash
#!/bin/bash
# Release management

function create_release() {
    local version=$1
    
    git checkout develop
    git pull origin develop
    git checkout -b "release/v${version}"
    
    # Update version files
    echo "${version}" > VERSION
    git add VERSION
    git commit -m "chore(release): bump to v${version}"
    git push -u origin "release/v${version}"
}

function finish_release() {
    local version=$(git symbolic-ref --short HEAD | sed 's/release\/v//')
    
    # Merge to main
    git checkout main
    git merge --no-ff "release/v${version}"
    git tag "v${version}"
    git push origin main --tags
    
    # Merge back to develop
    git checkout develop
    git merge --no-ff "release/v${version}"
    git push origin develop
    
    # Cleanup
    git branch -d "release/v${version}"
    git push origin --delete "release/v${version}"
}
```

## 3. Communication Standards

### Pull Request Templates

**FEATURE PR TEMPLATE:**

```markdown
## 🚀 Feature: [Brief Description]

**Issue**: Closes #[number]
**Type**: Feature | Bugfix | Enhancement

### Changes
- [ ] Added component X
- [ ] Updated API Y
- [ ] Modified schema Z

### Testing
- [ ] Unit tests added
- [ ] Integration tests pass
- [ ] Manual testing done

### Checklist
- [ ] Code reviewed
- [ ] No debug code
- [ ] Documentation updated
- [ ] Breaking changes noted
```

**HOTFIX PR TEMPLATE:**

```markdown
## 🚨 Hotfix: [Critical Issue]

**Severity**: Critical | High
**Issue**: Fixes #[number]

### Problem
[Describe production issue]

### Solution
[How this fixes it]

### Risk Assessment
- **Risk**: Low | Medium | High
- **Rollback Plan**: [Strategy]

### Verification
- [ ] Fix verified in staging
- [ ] Performance impact minimal
- [ ] Security reviewed
```

## 4. Quality Assurance

### Automated Quality Gates

**CI PIPELINE:**

```yaml
# .github/workflows/quality-gates.yml
name: Quality Gates
on:
  pull_request:
    branches: [main, develop]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate Branch
        run: |
          BRANCH="${GITHUB_HEAD_REF}"
          if [[ ! $BRANCH =~ ^(feature|bugfix|hotfix|release)/ ]]; then
            exit 1
          fi
      
      - name: Validate Commits
        run: |
          git log --format="%s" origin/${{ github.base_ref }}..HEAD | \
          while read msg; do
            if [[ ! $msg =~ ^(feat|fix|docs|style|refactor|perf|test|build|ci|chore) ]]; then
              echo "Invalid: $msg"
              exit 1
            fi
          done
      
      - name: Run Tests
        run: |
          npm ci
          npm run test:coverage
          npm run lint
          npm run build
```

**BRANCH PROTECTION:**

```bash
#!/bin/bash
# Setup branch protection
REPO="owner/repo"

# Protect main
curl -X PUT \
  -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/$REPO/branches/main/protection" \
  -d '{
    "required_status_checks": {"strict": true, "contexts": ["validate"]},
    "enforce_admins": true,
    "required_pull_request_reviews": {"required_approving_review_count": 2},
    "restrictions": null
  }'
```

## 5. Security and Performance

### Security Standards

**PRE-COMMIT SECURITY:**

```bash
#!/bin/bash
# Security validation

function check_secrets() {
    SECRET_PATTERNS=(
        "password.*=.*['\"].*['\"]"     # password="secret"
        "api[_-]?key.*=.*['\"].*['\"]"    # api_key="key"
        "['\"][A-Za-z0-9]{32,}['\"]"    # Long strings
    )
    
    for pattern in "${SECRET_PATTERNS[@]}"; do
        if git diff --cached | grep -iE "$pattern"; then
            echo "❌ Potential secret detected"
            exit 1
        fi
    done
}

function audit_dependencies() {
    npm audit --audit-level moderate
    if [ $? -ne 0 ]; then
        echo "❌ Security vulnerabilities found"
        exit 1
    fi
}

check_secrets
audit_dependencies
```

### Performance Monitoring

**REPOSITORY HEALTH:**

```bash
#!/bin/bash
# Repo performance analysis

function analyze_health() {
    echo "📊 Repository Health"
    
    # Size analysis
    REPO_SIZE=$(du -sh .git | cut -f1)
    echo "Size: $REPO_SIZE"
    
    # Large files
    git rev-list --objects --all | \
        git cat-file --batch-check | \
        awk '$3 > 10485760 {print $3/1024/1024 " MB " $2}' | \
        head -5
    
    # Branch analysis
    ACTIVE_BRANCHES=$(git branch -r | wc -l)
    echo "Active branches: $ACTIVE_BRANCHES"
    
    if [ $ACTIVE_BRANCHES -gt 20 ]; then
        echo "⚠️  Consider branch cleanup"
    fi
}

analyze_health
```

## 6. Language-Specific Standards

### Git Configuration

**OPTIMAL SETTINGS:**

```bash
#!/bin/bash
# Git config for GitFlow

# Core settings
git config core.autocrlf input
git config core.safecrlf warn
git config merge.conflictstyle diff3
git config pull.rebase true
git config push.default simple
git config push.followTags true

# GitFlow aliases
git config alias.feature '!f() { git checkout develop && git pull && git checkout -b feature/$1; }; f'
git config alias.release '!f() { git checkout develop && git pull && git checkout -b release/v$1; }; f'
git config alias.hotfix '!f() { git checkout main && git pull && git checkout -b hotfix/v$1; }; f'

echo "✅ Git optimized for GitFlow"
```

### Hook Installation

**AUTOMATED HOOKS:**

```bash
#!/bin/bash
# Install validation hooks

# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
npm run lint
npm run test:unit
EOF

# Commit-msg hook
cat > .git/hooks/commit-msg << 'EOF'
#!/bin/bash
source ./scripts/validate-commit.sh "$1"
EOF

chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/commit-msg

echo "✅ GitFlow hooks installed"
```

## 7. Continuous Improvement

### Workflow Metrics

**ANALYTICS:**

```bash
#!/bin/bash
# GitFlow analytics

function workflow_metrics() {
    echo "📊 Workflow Metrics"
    
    # Feature branch lifecycle
    echo "\nActive features:"
    git for-each-ref --format='%(refname:short) (%(committerdate:relative))' refs/remotes/origin/feature/
    
    # Release frequency
    echo "\nRecent releases:"
    git tag --sort=-version:refname | head -5
    
    # Hotfix frequency
    echo "\nRecent hotfixes:"
    git log --grep="hotfix" --oneline --since="3 months ago"
    
    # Branch health
    OLD_BRANCHES=$(git for-each-ref --format='%(refname:short) %(committerdate)' refs/remotes/origin/feature/ | \
                   awk '$2 < "'$(date -d '2 weeks ago' '+%Y-%m-%d')'" {print $1}')
    
    if [ ! -z "$OLD_BRANCHES" ]; then
        echo "\n⚠️  Stale branches (>2 weeks):"
        echo "$OLD_BRANCHES"
    fi
}

workflow_metrics
```

## 8. AI-Specific Best Practices

### Automated Decision Making

**BRANCH STRATEGY SELECTOR:**

```bash
#!/bin/bash
# AI-driven branch selection

function select_branch_strategy() {
    local change_type="$1"
    local urgency="$2"
    local scope="$3"
    
    case "$change_type" in
        "bug")
            if [[ "$urgency" == "critical" ]]; then
                echo "hotfix/v$(get_next_patch_version)"
            else
                echo "bugfix/${change_type}"
            fi
            ;;
        "feature")
            if [[ "$scope" == "breaking" ]]; then
                echo "feature/breaking-${change_type}"
            else
                echo "feature/${change_type}"
            fi
            ;;
        *)
            echo "feature/${change_type}"
            ;;
    esac
}

function get_next_patch_version() {
    local latest_tag=$(git describe --tags --abbrev=0)
    local version_parts=(${latest_tag//v/})
    local patch=$((${version_parts[2]} + 1))
    echo "${version_parts[0]}.${version_parts[1]}.${patch}"
}
```

### Quality Gates

**AUTOMATED VALIDATION:**

```bash
#!/bin/bash
# Complete validation pipeline

function validate_change() {
    echo "🔍 Running comprehensive validation..."
    
    # 1. Branch name validation
    ./scripts/validate-branch-name.sh
    
    # 2. Commit message validation
    git log --format="%s" -n 1 | ./scripts/validate-commit-format.sh
    
    # 3. Code quality
    npm run lint
    npm run test:coverage
    
    # 4. Security checks
    npm audit
    ./scripts/check-secrets.sh
    
    # 5. Performance checks
    npm run build
    ./scripts/check-bundle-size.sh
    
    echo "✅ All validations passed"
}

validate_change
```

### Error Recovery

**AUTOMATED ROLLBACK:**

```bash
#!/bin/bash
# Emergency rollback procedures

function emergency_rollback() {
    local failed_release="$1"
    
    echo "🚨 Initiating emergency rollback for $failed_release"
    
    # Find previous stable release
    local previous_release=$(git tag --sort=-version:refname | grep -A1 "$failed_release" | tail -1)
    
    if [ -z "$previous_release" ]; then
        echo "❌ No previous release found"
        exit 1
    fi
    
    # Create rollback branch
    git checkout main
    git checkout -b "hotfix/rollback-to-${previous_release}"
    git reset --hard "$previous_release"
    
    # Update version
    local new_version=$(get_next_patch_version)
    echo "$new_version" > VERSION
    git add VERSION
    git commit -m "fix: rollback to stable release $previous_release"
    
    echo "✅ Rollback branch created: hotfix/rollback-to-${previous_release}"
    echo "📋 Next steps:"
    echo "   1. Test rollback in staging"
    echo "   2. Create PR to main"
    echo "   3. Deploy to production"
}
```

---

## Summary

These GitFlow guidelines provide AI agents with:

1. **Automated Validation**: Scripts for branch names, commits, and quality gates
2. **Structured Workflows**: Clear procedures for features, releases, and hotfixes
3. **Security Integration**: Built-in secret detection and dependency scanning
4. **Performance Monitoring**: Repository health and workflow analytics
5. **Quality Assurance**: Comprehensive CI/CD pipelines and testing
6. **Error Recovery**: Automated rollback and emergency procedures
7. **Metrics & Analytics**: Workflow performance and optimization insights
8. **AI-Specific Tools**: Decision-making algorithms and automated processes

Implement these guidelines to achieve consistent, secure, and efficient GitFlow workflows across all projects.
