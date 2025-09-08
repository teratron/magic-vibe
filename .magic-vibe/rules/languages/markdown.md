---
description: Magic Vibe system documentation relies on Markdown. This rule establishes standards for creating clear, consistent, and AI-optimized Markdown files.
globs:
  - "**/*.md"
alwaysApply: true
---

# Magic Vibe Rule: Markdown Documentation Standards

> **Magic Vibe Rule: Markdown Documentation Standards**  
> **Category:** Language  
> **Priority:** High  
> **File Size:** ~15KB (AI-optimized)

Magic Vibe system documentation relies on Markdown. This rule establishes standards for creating clear, consistent, and AI-optimized Markdown files.

## 1. Implementation Guidelines

### 1.1. File Structure Standards

Every Magic Vibe Markdown file must follow this structure:

```markdown

```

### 1.2. Header Hierarchy

Use strict header hierarchy for AI parsing:

```markdown
\# [H1: Document Title (only one per file)]
## H2: Main Sections (8 sections for Magic Vibe rules)
### H3: Subsections
#### H4: Detailed breakdowns
##### H5: Implementation details (rarely used)
```

### 1.3. Metadata Block Requirements

Every rule file must include:

```markdown
> **Magic Vibe Rule:** [Descriptive Rule Name]  
> **Category:** [Appropriate category]  
> **Priority:** [Impact level]  
> **File Size:** ~[X]KB (AI-optimized)
> **Dependencies:** [Optional - related rules]
> **AI Restrictions:** [Optional - specific limitations]
```

### 1.4. Code Block Standards

Use language-specific syntax highlighting:

```markdown
<!-- Good examples -->
```typescript
const example: string = "TypeScript code";
```

```python
def example() -> str:
    return "Python code"
```

```bash
# Shell commands
npm install package-name
```

```json
{
  "config": "JSON configuration"
}
```

```text
<!-- For generic text content without specific language -->
Generic content, configuration formats, or mixed syntax
```

<!-- NEVER use blocks without language specification -->

```text
// This triggers MD040 warning - always specify language
```

### 1.5. Link and Reference Standards

Use consistent linking patterns:

```markdown
<!-- Internal Magic Vibe references -->
- `core/tasks.md` - Core task management
- `languages/typescript.md` - TypeScript rules
- `.magic-vibe/ai/TASKS.md` - Current tasks

<!-- External references -->
- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark Spec](https://commonmark.org/)

<!-- Cross-references within document -->
See [Implementation Guidelines](#1-implementation-guidelines)
```

### 1.6. List Formatting

Use consistent list formatting:

```markdown
<!-- Ordered lists for sequential steps -->
1. First step
2. Second step
   - Sub-item
   - Another sub-item
3. Third step

<!-- Unordered lists for non-sequential items -->
- Feature A
- Feature B
  - Sub-feature B1
  - Sub-feature B2
- Feature C

<!-- Task lists for actionable items -->
- [x] Completed task
- [ ] Pending task
- [ ] Another pending task
```

## 2. Change Management Protocols

### 2.1. File Size Management

**Critical AI Performance Requirements:**

- **Target Size:** 5-12KB per file (optimal for AI agents)
- **Maximum Size:** 15KB (hard limit for performance)
- **Token Calculation:** ~4 characters = 1 token, 15KB ≈ 3,750 tokens
- **Oversized Files:** Require immediate restructuring

### 2.2. Content Updates

When updating Markdown files:

```markdown

```

### 2.3. Breaking Changes

Document breaking changes clearly:

```markdown
## ⚠️ BREAKING CHANGES (v2.1.0)

### Changed Behavior
- Header structure now requires 8 sections for rules
- Metadata blocks are now mandatory

### Migration Path
1. Update existing files to include metadata blocks
2. Restructure content into 8 sections
3. Validate with `validate-markdown.ps1`
```

### 2.4. Deprecation Process

Mark deprecated content:

```markdown
## Deprecated Features

> **⚠️ DEPRECATED:** This section will be removed in v3.0.0
> **Migration:** Use [new approach](#new-section) instead

~~Old content that is deprecated~~
```

## 3. Communication Standards

### 3.1. Tone and Style

- **Clear and Direct:** Avoid ambiguous language
- **Action-Oriented:** Use imperative mood for instructions
- **Consistent Terminology:** Use Magic Vibe vocabulary consistently
- **Professional:** Maintain professional tone throughout

### 3.2. AI Agent Communication

Structure content for AI parsing:

```markdown
<!-- Good: Clear instruction format -->
### 3.2.1. Implementation Steps

Follow these steps to implement authentication:

1. **Install Dependencies:**
   
   ```bash
   npm install express-session passport
   ```

2. **Configure Session:**

   ```typescript
   app.use(session({
     secret: process.env.SESSION_SECRET,
     resave: false
   }));
   ```

3. **Validate Implementation:** Run tests to ensure functionality

```


### 3.3. User Communication

Provide clear guidance for developers:

```markdown
<!-- User-facing instructions -->
## Getting Started

To apply this rule:

1. **For AI Agents:** Reference `languages/markdown.md`
2. **For Developers:** Follow the implementation guidelines below
3. **For Validation:** Use provided validation scripts
```

### 3.4. Cross-Rule Communication

Reference other Magic Vibe rules:

```markdown
<!-- Clear rule dependencies -->
**Dependencies:**

- `core/workflow.md` - For file size optimization
- `workflows/clean-code.md` - For writing standards
- `principles/kiss.md` - For communication principles
```

## 4. Quality Assurance Framework

### 4.1. Validation Rules

Implement automated validation:

```markdown
# PowerShell validation script example
function Test-MarkdownStructure {
    param([string]$FilePath)
    
    $content = Get-Content $FilePath -Raw
    
    # Check for required metadata block
    if ($content -notmatch '> \*\*Magic Vibe Rule:\*\*') {
        Write-Error "Missing Magic Vibe metadata block"
        return $false
    }
    
    # Check for 8-section structure
    $sections = ($content | Select-String '^## \d+\.' -AllMatches).Matches
    if ($sections.Count -ne 8) {
        Write-Error "Rule must have exactly 8 sections, found $($sections.Count)"
        return $false
    }
    
    # Check file size
    $size = (Get-Item $FilePath).Length
    if ($size -gt 15KB) {
        Write-Warning "File size ($([math]::Round($size/1KB, 1))KB) exceeds recommended limit"
    }
    
    return $true
}
```

### 4.2. Content Quality Standards

- **Grammar:** Use tools like Grammarly or built-in spell checkers
- **Consistency:** Maintain consistent terminology and formatting
- **Completeness:** Ensure all 8 sections are properly developed
- **Accuracy:** Verify all code examples work correctly

**MD040 Compliance:** Always specify language for fenced code blocks

```markdown
<!-- GOOD: Language specified -->
``typescript
const config = { api: true };
```

```text
Generic configuration or mixed content
```

<!-- BAD: No language specified - triggers MD040 warning -->
```markdown

```

### 4.3. Accessibility Standards

```markdown
<!-- Good: Descriptive alt text for images -->
![Magic Vibe System Architecture](./images/architecture.png "Complete overview of Magic Vibe system components and their relationships")

<!-- Good: Clear table headers -->
| Rule Type | File Size Limit | Priority |
|-----------|-----------------|----------|
| Core      | 10KB            | High     |
| Language  | 8KB             | Medium   |
| Framework | 12KB            | Medium   |
```

### 4.4. Testing Standards

Test documentation with real scenarios:

```markdown
<!-- Test scenarios for rule validation -->
## Testing Checklist

- [ ] File follows 8-section structure
- [ ] Metadata block is complete and accurate
- [ ] All code examples execute successfully
- [ ] File size is within limits (5-15KB)
- [ ] Links and references work correctly
- [ ] AI agents can parse content effectively
```

## 5. Security & Performance Guidelines

### 5.1. Sensitive Information Handling

```markdown
<!-- Good: Environment variable usage -->
```bash
export API_KEY=${API_KEY}
```

<!-- Bad: Hardcoded secrets -->
```bash
export API_KEY="sk-abc123..."  # NEVER DO THIS
```

<!-- Sanitized examples -->
```json
{
  "database": {
    "host": "localhost",
    "user": "app_user",
    "password": "***REDACTED***"
  }
}
```

### 5.2. Performance Optimization

**File Size Optimization:**

- Use concise language without losing clarity
- Combine related examples into single code blocks
- Remove redundant explanations
- Optimize table structures

```markdown
<!-- Optimized table format -->
| Type | Size | Priority | Notes |
|------|------|----------|-------|
| Core | 10KB | High | Essential rules only |
| Lang | 8KB | Med | Language-specific |
| Framework | 12KB | Med | Framework patterns |

<!-- Instead of multiple separate tables -->
```

### 5.3. Loading Performance

Structure for progressive loading:

```markdown
<!-- Front-load critical information -->
\# Document Structure Example

### Quick Start (Essential)
[Most important information first]

### Detailed Configuration (Optional)
[Additional details for advanced users]

### Advanced Customization (Expert)
[Complex configurations for specific cases]
```

## 6. Integration & Compatibility

### 6.1. Magic Vibe System Integration

Ensure compatibility with Magic Vibe components:

```markdown
<!-- Integration with task system -->
**Task Integration:**
- Reference tasks using: `.magic-vibe/ai/TASKS.md#task-id`
- Create tasks with: `core/tasks.md` guidance

<!-- Integration with plans -->
**Plan Integration:**
- Reference plans using: `.magic-vibe/ai/plans/feature-name.md`
- Create plans with: `core/plans.md` guidance
```

### 6.2. Tool Compatibility

Ensure Markdown works across tools:

```markdown
<!-- CommonMark compatibility -->
- Use standard Markdown syntax
- Avoid tool-specific extensions
- Test across VS Code, Obsidian, GitHub

<!-- GitHub Flavored Markdown support -->
- [ ] Task lists
- `@username` mentions (where appropriate)
- #123 issue references (for external projects)
```

### 6.3. Cross-Platform Compatibility

```markdown
<!-- File path handling -->
<!-- Good: Platform-agnostic paths -->
See `rules/core/tasks.md` for guidance

<!-- Avoid: Platform-specific paths -->
See `rules\core\tasks.md` for guidance (Windows-specific)
```

### 6.4. Editor Compatibility

Optimize for AI editors:

```markdown
<!-- AI-friendly structure -->
### Clear Section Headers
Content organized in logical blocks

**Bold emphasis** for key concepts
`Code references` for technical terms

<!-- Avoid complex formatting that confuses AI -->
```

## 7. Monitoring & Maintenance

### 7.1. Regular Review Process

```markdown
<!-- Monthly review checklist -->
## Maintenance Schedule

### Monthly Reviews
- [ ] Check file sizes for optimization opportunities
- [ ] Validate all external links
- [ ] Review and update code examples
- [ ] Test AI agent compatibility

### Quarterly Reviews  
- [ ] Full content audit for accuracy
- [ ] Update deprecated information
- [ ] Collect feedback from AI agent usage
- [ ] Performance optimization review
```

### 7.2. Metrics and Analytics

Track document effectiveness:

```markdown
<!-- Key metrics to monitor -->
**Performance Metrics:**
- File size trend analysis
- AI agent parsing success rate
- User feedback on clarity
- Time to understand content

**Quality Metrics:**
- Grammar and spelling accuracy
- Code example success rate
- Cross-reference validity
- Compliance with Magic Vibe standards
```

### 7.3. Version Control Strategy

```markdown
<!-- Git workflow for documentation -->
## Documentation Workflow

1. **Feature Branch:** Create branch for documentation updates
2. **Draft Changes:** Make incremental improvements
3. **Validation:** Run validation scripts
4. **Review:** Get feedback from team/community
5. **Merge:** Integrate after validation passes
```

### 7.4. Feedback Integration

```markdown
<!-- Feedback collection methods -->
**Feedback Sources:**
- AI agent error reports
- User issue reports
- Community suggestions
- Performance monitoring data

**Response Process:**
1. Categorize feedback by priority
2. Plan updates in maintenance cycles
3. Implement changes systematically
4. Validate improvements
```

## 8. AI Agent Optimization

### 8.1. Parsing Optimization

Structure content for AI comprehension:

```markdown
<!-- AI-optimized formatting -->
### 8.1.1. Clear Information Hierarchy

**Purpose:** What this section accomplishes
**Implementation:** How to implement the guidelines
**Validation:** How to verify correct implementation
**Examples:** Practical code examples

<!-- Consistent patterns for AI parsing -->
```

### 8.2. Token Efficiency

Optimize for AI token usage:

```markdown
<!-- Efficient information density -->
**Token Calculation Formula:**
- 1 token ≈ 4 characters (English)
- 15KB file ≈ 3,750 tokens
- Target: 2,500-3,000 tokens per file

**Optimization Strategies:**
- Use bullet points over long paragraphs
- Combine related examples
- Remove redundant explanations
- Use tables for structured data
```

### 8.3. Context Preservation

Maintain context for AI agents:

```markdown
<!-- Self-contained sections -->
Each section should be understandable independently while maintaining document flow.

<!-- Clear references -->
When referencing other sections: "As described in [Section 2.1](#21-file-size-management)"

<!-- Explicit relationships -->
**Prerequisites:** Understanding of Markdown basics
**Dependencies:** Magic Vibe core system knowledge
**Outputs:** Properly formatted Magic Vibe documentation
```

### 8.4. AI Restriction Guidelines

```markdown
<!-- AI agent behavioral guidance -->
**AI Agent Restrictions:**
- NEVER modify this rule file without creator approval
- ALWAYS validate Markdown syntax before suggesting changes
- MUST follow file size limits strictly
- SHOULD reference this rule when creating new Markdown files

**AI Agent Capabilities:**
- CAN create new Markdown files following these standards
- CAN suggest improvements to existing Markdown files
- CAN validate Markdown structure and format
- CAN optimize content for better AI parsing
```

---

**Magic Vibe Markdown Rules v2.1.0** - Foundation for all Magic Vibe documentation

***Last Updated:** 2025-01-XX | **File Size:** ~8KB | **Status:** Active*
