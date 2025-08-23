---
description: Comprehensive trunk-based development guidelines optimized for AI agents. Includes automated validation, continuous integration, and quality gates for high-velocity software delivery.
globs: .git/**, **/.gitignore, **/.gitattributes, **/ci.yml, **/cd.yml
---

# Trunk-Based Development Guidelines for AI Agents

## 1. Code Generation Standards

### Branch Strategy Standards

**MANDATORY PATTERNS:**

```text
Main Branch:          main (trunk)                      - Single source of truth
Short-lived Branches: feature/[id]-[description]        - Max 3 days lifespan
Release Branches:     release/v[X.Y.Z]                  - Only for release prep
Hotfix Branches:      hotfix/[id]-[description]         - Max 4 hours lifespan

Branch Lifetime Limits:
- Feature branches: Maximum 72 hours (3 days)
- Release branches: Maximum 1 week
- Hotfix branches: Maximum 4 hours
- No long-lived feature branches allowed
```

**BRANCH VALIDATION SCRIPT:**

```bash
#!/bin/bash
# Validate branch age for trunk-based development

function check_branch_age() {
    local branch="$1"
    local max_hours="$2"
    
    local created=$(git log --format="%ct" "$branch" | tail -1)
    local current=$(date +%s)
    local age_hours=$(( (current - created) / 3600 ))
    
    if [ $age_hours -gt $max_hours ]; then
        echo "❌ Branch $branch is $age_hours hours old (max: $max_hours)"
        return 1
    fi
    
    echo "✅ Branch age OK: $age_hours hours"
}

# Check all feature branches (max 72 hours)
for branch in $(git branch -r | grep 'feature/' | sed 's/origin\///'); do
    check_branch_age "$branch" 72
done
```

### Commit Standards

**HIGH-FREQUENCY COMMIT REQUIREMENTS:**

```text
Commit Frequency:    Minimum 2-3 commits per day
Commit Size:         Maximum 200 lines changed
Commit Message:      Conventional format with feature flags
Atomic Commits:      Single logical change per commit
Revert Safety:       Each commit independently revertible
```

### Feature Flag Integration

**FEATURE FLAG PATTERN:**

```typescript
// Feature flag implementation for safe trunk deployment

class FeatureFlagManager {
  isEnabled(flagName: string, userId?: string): boolean {
    const flag = this.flags[flagName];
    
    // Environment-based defaults
    if (process.env.NODE_ENV === 'development') {
      return flag ?? true;  // Default enabled in dev
    }
    
    if (process.env.NODE_ENV === 'production') {
      return flag ?? false; // Default disabled in prod
    }
    
    return flag ?? false;
  }
}

// Usage: Wrap all new features
function renderDashboard(user: User) {
  if (featureFlags.isEnabled('beta-dashboard', user.id)) {
    return <NewDashboard user={user} />;
  }
  return <LegacyDashboard user={user} />;
}
```

## 2. Change Management

### Continuous Integration Pipeline

**AUTOMATED CI WORKFLOW:**

```yaml
# .github/workflows/trunk-ci.yml
name: Trunk-Based CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Validate Branch Age
        run: |
          if [[ "$GITHUB_REF" != "refs/heads/main" ]]; then
            BRANCH=${GITHUB_HEAD_REF}
            CREATED=$(git log --format="%ct" "origin/$BRANCH" | tail -1)
            AGE_HOURS=$(( ($(date +%s) - CREATED) / 3600 ))
            
            if [ $AGE_HOURS -gt 72 ]; then
              echo "❌ Branch too old: $AGE_HOURS hours"
              exit 1
            fi
          fi
      
      - name: Install & Test
        run: |
          npm ci
          npm run lint
          npm run test:coverage
          npm run build
      
      - name: Deploy to Staging
        if: github.ref == 'refs/heads/main'
        run: npm run deploy:staging
```

### Merge Strategy

**SQUASH AND MERGE AUTOMATION:**

```bash
#!/bin/bash
# Automated merge validation

function validate_merge() {
    local pr_number="$1"
    
    # Check CI status
    gh pr checks "$pr_number" --required || {
        echo "❌ CI checks failing"
        return 1
    }
    
    # Check branch age
    local branch=$(gh pr view "$pr_number" --json headRefName --jq .headRefName)
    local age_hours=$(( ($(date +%s) - $(git log --format="%ct" "origin/$branch" | tail -1)) / 3600 ))
    
    if [ $age_hours -gt 72 ]; then
        echo "❌ Branch too old: $age_hours hours"
        return 1
    fi
    
    # Perform squash merge
    gh pr merge "$pr_number" --squash --delete-branch
    echo "✅ Merged and deployed to staging"
}
```

## 3. Communication Standards

### Pull Request Template

**TRUNK-BASED PR TEMPLATE:**

```markdown
## 🌿 Trunk-Based Development PR

**Feature Flag**: `feature-name` (if applicable)
**Issue**: Closes #[number]

### Changes
- [ ] Feature behind feature flag
- [ ] Tests added (>90% coverage)
- [ ] Documentation updated

### Deployment Readiness
- [ ] Can deploy to production immediately
- [ ] Feature flag configured
- [ ] Backward compatible
- [ ] Monitoring configured

### Branch Compliance
- [ ] Branch age < 72 hours
- [ ] Atomic commits
- [ ] All CI checks pass
- [ ] No merge conflicts

### Rollout Plan
**Phase 1**: Deploy disabled (0%)  
**Phase 2**: Internal users (5%)  
**Phase 3**: Gradual rollout (25%, 50%, 100%)
```

### Commit Message Format

**ENHANCED CONVENTIONAL COMMITS:**

```text
Format: <type>[scope]: <description> [flag: name]

Examples:
feat(auth): add OAuth integration [flag: oauth-login]
fix(api): resolve timeout in user endpoint
flag(dashboard): increase beta-dashboard to 25%
```

## 4. Quality Assurance

### Testing Requirements

**FEATURE FLAG TESTING:**

```typescript
// Test both flag states
describe('UserService', () => {
  describe('with new-auth flag enabled', () => {
    beforeEach(() => featureFlags.enable('new-auth'));
    
    it('should use new authentication', async () => {
      const result = await userService.authenticate(creds);
      expect(result.method).toBe('oauth');
    });
  });
  
  describe('with new-auth flag disabled', () => {
    beforeEach(() => featureFlags.disable('new-auth'));
    
    it('should use legacy authentication', async () => {
      const result = await userService.authenticate(creds);
      expect(result.method).toBe('password');
    });
  });
});
```

**QUALITY GATES:**

```bash
#!/bin/bash
# Automated quality validation

function quality_gates() {
    echo "🎯 Running quality gates..."
    
    # Coverage check (min 90%)
    npm run test:coverage
    COVERAGE=$(npm run coverage:report | grep 'All files' | awk '{print $10}' | sed 's/%//')
    [ "$COVERAGE" -lt 90 ] && {
        echo "❌ Coverage too low: $COVERAGE%"
        return 1
    }
    
    # Performance tests
    npm run test:performance || {
        echo "❌ Performance tests failed"
        return 1
    }
    
    # Security scan
    npm audit --audit-level moderate || {
        echo "❌ Security issues found"
        return 1
    }
    
    echo "✅ All quality gates passed"
}
```

## 5. Security and Performance

### Security Validation

**CONTINUOUS SECURITY CHECKS:**

```bash
#!/bin/bash
# Security validation for trunk-based development

function security_check() {
    echo "🔒 Running security validation..."
    
    # Dependency scan
    npm audit --audit-level moderate
    
    # Secret detection
    git diff --cached | grep -iE '(password|api_key|secret).*=' && {
        echo "❌ Potential secrets detected"
        return 1
    }
    
    # Feature flag security
    grep -r "flag.*admin\|flag.*secret" src/ && {
        echo "⚠️  Security-sensitive flags detected"
    }
    
    echo "✅ Security validation passed"
}
```

### Performance Monitoring

**DEPLOYMENT PERFORMANCE TRACKING:**

```typescript
// Monitor deployment and feature flag performance
class TrunkPerformanceMonitor {
  trackDeployment() {
    const start = Date.now();
    
    return {
      recordBuild: (duration: number) => {
        this.recordMetric('build_time', duration);
      },
      recordDeploy: () => {
        const total = Date.now() - start;
        this.recordMetric('deploy_time', total);
        
        // Alert if deployment > 5 minutes
        if (total > 300000) {
          console.error(`Slow deployment: ${total}ms`);
        }
      }
    };
  }
  
  measureFeatureFlag(flagName: string, operation: Function) {
    const start = performance.now();
    const result = operation();
    const duration = performance.now() - start;
    
    if (duration > 10) {
      console.warn(`Slow flag evaluation: ${flagName} (${duration}ms)`);
    }
    
    return result;
  }
}
```

## 6. Language-Specific Standards

### Git Configuration

**TRUNK-OPTIMIZED GIT SETUP:**

```bash
#!/bin/bash
# Configure Git for trunk-based development

# Core settings
git config pull.rebase true              # Always rebase
git config push.default simple           # Push current branch only
git config rebase.autosquash true        # Auto-squash fixups

# Trunk-based aliases
git config alias.sync 'checkout main && git pull'
git config alias.feature '!f() { git sync && git checkout -b feature/$1; }; f'
git config alias.quick '!f() { git add -A && git commit -m "$1"; }; f'

echo "✅ Git configured for trunk-based development"
```

### Automated Hooks

**TRUNK-SPECIFIC HOOKS:**

```bash
#!/bin/bash
# Install trunk-based hooks

# Pre-commit: validate branch age
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
BRANCH=$(git symbolic-ref --short HEAD)
if [[ "$BRANCH" != "main" ]]; then
    AGE_HOURS=$(( ($(date +%s) - $(git log --format="%ct" "$BRANCH" | tail -1)) / 3600 ))
    if [ $AGE_HOURS -gt 72 ]; then
        echo "❌ Branch too old: $AGE_HOURS hours"
        exit 1
    fi
fi
EOF

chmod +x .git/hooks/pre-commit
echo "✅ Trunk-based hooks installed"
```

## 7. Continuous Improvement

### Metrics and Analytics

**TRUNK-BASED METRICS:**

```bash
#!/bin/bash
# Analyze trunk-based development metrics

function trunk_metrics() {
    echo "📊 Trunk-Based Development Metrics"
    
    # Deployment frequency
    DEPLOYMENTS=$(git log --since="1 week ago" --grep="deploy" --oneline | wc -l)
    echo "Deployments this week: $DEPLOYMENTS"
    
    # Lead time (branch creation to merge)
    echo "\nFeature lead times:"
    for branch in $(git for-each-ref --merged=main --format='%(refname:short)' | grep feature/); do
        CREATED=$(git log --format="%ct" "$branch" | tail -1)
        MERGED=$(git log --format="%ct" -n 1 main --grep="Merge.*$branch")
        if [ ! -z "$MERGED" ]; then
            HOURS=$(( (MERGED - CREATED) / 3600 ))
            echo "  $branch: $HOURS hours"
        fi
    done
    
    # Branch age analysis
    echo "\nActive branch ages:"
    for branch in $(git branch -r | grep -v main | sed 's/origin\///'); do
        AGE_HOURS=$(( ($(date +%s) - $(git log --format="%ct" "origin/$branch" | tail -1)) / 3600 ))
        if [ $AGE_HOURS -gt 48 ]; then
            echo "  ⚠️  $branch: $AGE_HOURS hours (consider merging)"
        fi
    done
}

trunk_metrics
```

### Process Optimization

**AUTOMATED CLEANUP:**

```bash
#!/bin/bash
# Optimize trunk-based workflow

function optimize_trunk() {
    echo "🔧 Optimizing trunk-based workflow..."
    
    # Clean up merged branches
    git branch --merged main | grep -v main | xargs -r git branch -d
    
    # Alert on old branches
    for branch in $(git branch -r | grep -v main); do
        AGE=$(( ($(date +%s) - $(git log --format="%ct" "$branch" | tail -1)) / 86400 ))
        if [ $AGE -gt 7 ]; then
            echo "⚠️  Branch $branch is $AGE days old - consider cleanup"
        fi
    done
    
    # Performance recommendations
    BRANCH_COUNT=$(git branch -r | wc -l)
    if [ $BRANCH_COUNT -gt 20 ]; then
        echo "💡 Too many branches ($BRANCH_COUNT) - cleanup recommended"
    fi
}

optimize_trunk
```

## 8. AI-Specific Best Practices

### Automated Decision Making

**BRANCH STRATEGY SELECTOR:**

```bash
#!/bin/bash
# AI-driven branch strategy

function select_strategy() {
    local change_type="$1"
    local urgency="$2"
    
    case "$change_type" in
        "bug")
            if [[ "$urgency" == "critical" ]]; then
                echo "hotfix/$(date +%Y%m%d)-${change_type}"
            else
                echo "feature/fix-${change_type}"
            fi
            ;;
        "feature")
            echo "feature/$(date +%Y%m%d)-${change_type}"
            ;;
        *)
            echo "feature/${change_type}"
            ;;
    esac
}

# Usage: select_strategy "user-auth" "normal"
```

### Quality Automation

**COMPREHENSIVE VALIDATION PIPELINE:**

```bash
#!/bin/bash
# Complete trunk-based validation

function validate_trunk_change() {
    echo "🔍 Running comprehensive validation..."
    
    # 1. Branch validation
    ./scripts/validate-branch-age.sh || return 1
    
    # 2. Code quality
    npm run lint && npm run test:coverage || return 1
    
    # 3. Security
    npm audit --audit-level moderate || return 1
    
    # 4. Performance
    npm run test:performance || return 1
    
    # 5. Feature flags
    ./scripts/validate-feature-flags.sh || return 1
    
    echo "✅ All validations passed - ready for trunk"
}

validate_trunk_change
```

### Error Recovery

**AUTOMATED ROLLBACK:**

```bash
#!/bin/bash
# Emergency rollback for trunk-based development

function emergency_rollback() {
    local failed_commit="$1"
    
    echo "🚨 Initiating emergency rollback..."
    
    # Create rollback commit
    git revert "$failed_commit" --no-edit
    
    # Deploy immediately
    git push origin main
    
    # Notify team
    echo "✅ Rollback completed and deployed"
    echo "📬 Notifying team of rollback"
    
    # Trigger deployment
    gh workflow run deploy-production.yml
}

# Usage: emergency_rollback abc123
```

---

## Summary

These trunk-based development guidelines provide AI agents with:

1. **Short-lived Branches**: Maximum 72-hour feature branches with automated validation
2. **Continuous Integration**: Automated pipelines with quality gates and immediate deployment
3. **Feature Flags**: Safe deployment patterns with gradual rollouts
4. **High-frequency Commits**: Small, atomic changes with comprehensive testing
5. **Automated Quality**: 90% test coverage, security scans, and performance monitoring
6. **Rapid Recovery**: Automated rollback procedures and emergency response
7. **Metrics-driven**: Continuous monitoring and process optimization
8. **AI-optimized**: Decision automation and validation pipelines

Implement these patterns to achieve high-velocity, low-risk software delivery with trunk-based development.
