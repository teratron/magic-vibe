---
description: Comprehensive code quality guidelines for AI agents. These rules ensure high-quality code generation, review, and modification practices.
globs: 
---

# Code Quality Guidelines for AI Agents

## 1. Code Generation Standards

### Completeness Requirements

**MUST PROVIDE:**

- Complete, immediately runnable code
- All necessary imports and dependencies
- Proper error handling and validation
- Type annotations where supported by the language
- Comprehensive documentation for public APIs

**VALIDATION CHECKLIST:**

- [ ] Code compiles/runs without errors
- [ ] All dependencies are declared
- [ ] Error paths are handled appropriately
- [ ] Security best practices are followed
- [ ] Performance considerations are addressed

### Code Structure Standards

**FUNCTION QUALITY:**

- Maximum 20 lines per function (preferred)
- Single responsibility principle strictly enforced
- Pure functions when possible (no side effects)
- Descriptive names that explain purpose
- Early returns to reduce nesting

**FILE ORGANIZATION:**

- Maximum 300 lines per file
- Logical grouping of related functionality
- Consistent import ordering
- Clear separation of concerns

## 2. Code Review and Modification

### Information Verification

**ALWAYS:**

- Verify information before presenting solutions
- Cross-reference with official documentation
- Test proposed changes in context
- Validate assumptions against provided code

**NEVER:**

- Make assumptions without evidence
- Speculate about implementation details
- Provide untested code snippets

### Change Management

**FILE-BY-FILE APPROACH:**

- Make changes to one file at a time
- Provide complete context for each change
- Allow for iterative feedback and corrections
- Group related changes within the same file

**PRESERVATION PRINCIPLES:**

- Maintain existing code structure and patterns
- Preserve unrelated functionalities
- Keep existing coding style consistent
- Retain original logic unless explicitly changing it

### Edit Quality Standards

**SINGLE-CHUNK EDITS:**

- Provide all changes for a file in one operation
- Include sufficient context for understanding
- Use precise line-by-line modifications
- Avoid multi-step instructions for the same file

**CHANGE PRECISION:**

- Only modify what's explicitly requested
- Don't add unrequested features or optimizations
- Preserve existing comments and documentation
- Maintain original variable and function names unless changing them is the goal

## 3. Communication Standards

### Professional Communication

**AVOID:**

- Unnecessary apologies in code or comments
- "Understanding" feedback in documentation
- Confirmations for information already provided
- Summaries of changes unless requested

**FOCUS ON:**

- Clear, factual explanations
- Actionable guidance
- Specific technical details
- Direct problem-solving

### Documentation Practices

**CODE COMMENTS:**

- Explain "why" not "what"
- Document complex algorithms and business logic
- Include examples for public APIs
- Update comments when changing code

**TECHNICAL WRITING:**

- Use active voice
- Be concise and specific
- Include code examples where helpful
- Provide clear instructions

## 4. Quality Assurance

### Pre-Submission Validation

**MANDATORY CHECKS:**

- [ ] Syntax validation passed
- [ ] No compilation errors
- [ ] All imports resolve correctly
- [ ] Error handling is comprehensive
- [ ] Performance impact assessed
- [ ] Security vulnerabilities addressed

### Testing Requirements

**INCLUDE WITH CODE:**

- Unit tests for new functions
- Integration tests for modified workflows
- Edge case and error condition tests
- Performance tests for critical paths

**TEST QUALITY:**

- Clear, descriptive test names
- Comprehensive test coverage
- Independent, repeatable tests
- Proper setup and teardown

## 5. Security and Performance

### Security Checklist

**INPUT VALIDATION:**

- Sanitize all user inputs
- Use parameterized queries
- Implement proper authentication checks
- Validate file uploads and downloads

**SENSITIVE DATA:**

- Never log passwords, tokens, or PII
- Use secure communication protocols
- Implement proper access controls
- Handle errors without exposing system details

### Performance Guidelines

**OPTIMIZATION PRINCIPLES:**

- Profile before optimizing
- Use appropriate data structures
- Minimize database queries
- Implement caching strategically
- Handle large datasets efficiently

**RESOURCE MANAGEMENT:**

- Close resources properly
- Avoid memory leaks
- Use lazy loading when appropriate
- Implement proper connection pooling

## 6. Language-Specific Quality Standards

### Universal Principles

**NAMING CONVENTIONS:**

- Follow language-specific naming standards
- Use meaningful, searchable names
- Avoid abbreviations unless standard
- Include units in variable names when relevant

**ERROR HANDLING:**

- Use language-appropriate exception types
- Provide meaningful error messages
- Implement proper logging
- Handle edge cases gracefully

### Code Style Consistency

**FORMATTING:**

- Use consistent indentation
- Follow established formatting rules
- Maintain line length limits
- Use whitespace meaningfully

**PATTERNS:**

- Follow established design patterns
- Use language idioms appropriately
- Implement consistent interfaces
- Apply SOLID principles

## 7. Continuous Improvement

### Refactoring Guidelines

**REFACTOR WHEN:**

- Functions exceed 30 lines
- Code is duplicated 3+ times
- Complexity becomes unmanageable
- Performance issues are identified
- Security vulnerabilities are found

**REFACTORING PROCESS:**

- Ensure tests pass before refactoring
- Make small, incremental changes
- Verify functionality after each change
- Update documentation accordingly

### Code Review Process

**REVIEW CRITERIA:**

- Functionality correctness
- Code readability and maintainability
- Performance implications
- Security considerations
- Test coverage adequacy

**FEEDBACK QUALITY:**

- Provide specific, actionable suggestions
- Include code examples for improvements
- Explain reasoning behind recommendations
- Prioritize issues by severity

## 8. AI-Specific Best Practices

### Code Generation

**WHEN GENERATING CODE:**

- Always include necessary imports
- Provide complete, working examples
- Include error handling by default
- Add type annotations where supported
- Generate accompanying tests when appropriate

### Code Analysis

**WHEN REVIEWING CODE:**

- Check for common security vulnerabilities
- Identify performance bottlenecks
- Verify adherence to coding standards
- Suggest specific improvements
- Validate test coverage

### Learning and Adaptation

**CONTINUOUSLY:**

- Learn from codebase patterns
- Adapt to project-specific conventions
- Update knowledge based on feedback
- Improve suggestions over time
- Stay current with best practices
