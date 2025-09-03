---
description: Optimized clean code guidelines for AI agents. These rules ensure code quality, maintainability, and consistency when AI generates, modifies, or reviews code.
globs: 
---

# Clean Code Guidelines for AI Agents

## 1. Constants and Configuration

**MUST DO:**

- Always replace magic numbers with named constants: `const MAX_RETRY_ATTEMPTS = 3` instead of `3`
- Use SCREAMING_SNAKE_CASE for constants: `API_TIMEOUT_MS`, `DEFAULT_PAGE_SIZE`
- Place constants at module top or in dedicated config files
- Include units in constant names when applicable: `TIMEOUT_SECONDS`, `BUFFER_SIZE_KB`

**AVOID:**

- Hard-coded values scattered throughout code
- Unclear constant names like `LIMIT` or `SIZE`

## 2. Naming Conventions

**MUST DO:**

- Use descriptive, searchable names: `getUserById()` not `getUser()`
- Follow language conventions: camelCase for JS/TS, snake_case for Python
- Use verbs for functions: `calculateTotal()`, `validateInput()`
- Use nouns for variables: `userAccount`, `responseData`
- Use boolean prefixes: `isValid`, `hasPermission`, `canAccess`

**AVOID:**

- Single letter variables except for short loops
- Abbreviations: use `configuration` not `config`
- Mental mapping: `d` for days, `u` for user

## 3. Function Design

**MUST DO:**

- Keep functions under 20 lines when possible
- One responsibility per function - if you use "and" in the name, split it
- Use pure functions when possible (no side effects)
- Return early to reduce nesting levels
- Use descriptive parameter names

**FUNCTION SIZE LIMITS:**

- Simple functions: 1-10 lines
- Complex functions: 10-20 lines
- Refactor if exceeding 30 lines

## 4. Code Organization

**MUST DO:**

- Group related functionality in modules/classes
- Order functions by abstraction level (high-level first)
- Keep files under 300 lines
- Use consistent folder structure
- Separate concerns: data, business logic, presentation

**FILE STRUCTURE:**

1. Imports/includes
2. Constants
3. Types/interfaces
4. Main functionality
5. Helper functions
6. Exports

## 5. Error Handling

**MUST DO:**

- Use specific error types, not generic exceptions
- Provide meaningful error messages with context
- Handle errors at appropriate levels
- Log errors with sufficient detail for debugging
- Use early returns for error conditions

**EXAMPLE:**

```javascript
// Good
if (!userId) {
  throw new ValidationError('User ID is required for profile update');
}

// Bad
if (!userId) {
  throw new Error('Invalid input');
}
```

## 6. Comments and Documentation

**WHEN TO COMMENT:**

- Why decisions were made, not what code does
- Complex algorithms or business rules
- Public APIs and interfaces
- Workarounds or non-obvious implementations
- TODO items with context and dates

**AVOID:**

- Comments that repeat the code
- Commented-out code (use version control)
- Outdated comments

## 7. Testing Requirements

**MUST INCLUDE:**

- Unit tests for all public functions
- Integration tests for critical paths
- Edge case and error condition tests
- Clear test descriptions that explain the scenario

**TEST NAMING:**

- `should_return_error_when_user_not_found()`
- `should_calculate_correct_total_with_discount()`

## 8. Performance Considerations

**MUST DO:**

- Avoid premature optimization
- Use appropriate data structures (Map vs Object, Set vs Array)
- Minimize API calls and database queries
- Handle large datasets efficiently (pagination, streaming)
- Cache expensive computations when appropriate

## 9. Security Guidelines

**ALWAYS:**

- Validate and sanitize all inputs
- Use parameterized queries to prevent SQL injection
- Never log sensitive data (passwords, tokens, PII)
- Handle authentication and authorization properly
- Use HTTPS for all external communications

## 10. Code Review Checklist

**BEFORE COMMITTING:**

- [ ] All functions have single responsibility
- [ ] No magic numbers or hard-coded values
- [ ] Meaningful variable and function names
- [ ] Proper error handling implemented
- [ ] Tests cover new functionality
- [ ] No commented-out code
- [ ] Documentation updated if needed
- [ ] Performance impact considered

## 11. Refactoring Triggers

**REFACTOR WHEN YOU SEE:**

- Functions longer than 30 lines
- Repeated code blocks (3+ times)
- Deep nesting (3+ levels)
- Long parameter lists (5+ parameters)
- Complex conditional logic
- God classes/modules doing too much

## 12. AI-Specific Guidelines

**WHEN GENERATING CODE:**

- Always include necessary imports/dependencies
- Provide complete, runnable examples
- Include error handling in generated functions
- Add type annotations where supported
- Generate accompanying tests when requested
- Follow the existing codebase patterns and style
- Validate generated code syntax before presenting
