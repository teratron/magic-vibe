---
description: Universal development principles that AI agents should apply across all programming languages, frameworks, and project types to ensure high-quality, maintainable code.
globs: "*.md"
alwaysApply: true
priority: 5
---

# Development Principles Index

This directory contains universal development principles that AI agents should apply consistently across all programming languages, frameworks, and project types. These principles form the foundation of quality software development practices.

## Available Development Principles

- **Object-Oriented Programming:** `@principles/oop.md` - Encapsulation, inheritance, polymorphism, and abstraction principles
- **SOLID Design Principles:** `@principles/solid.md` - Five fundamental principles for maintainable object-oriented design
- **DRY Principle:** `@principles/dry.md` - "Don't Repeat Yourself" - eliminating code duplication and ensuring single source of truth
- **KISS Principle:** `@principles/kiss.md` - "Keep It Simple, Stupid" - maintaining simplicity and avoiding unnecessary complexity
- **YAGNI Principle:** `@principles/yagni.md` - "You Ain't Gonna Need It" - implementing only what is currently needed

## Principle Application Hierarchy

Development principles are applied with the following priority:

### 1. Universal Application (Priority 5)

All principles apply to every piece of code, regardless of:

- Programming language
- Framework or library choice
- Project size or complexity
- Development methodology
- Team structure

### 2. Principle Precedence Order

When principles conflict, apply this resolution hierarchy:

1. **KISS (Simplicity)** - Prefer simpler solutions
2. **YAGNI (Necessity)** - Only implement what's needed now
3. **DRY (Maintainability)** - Eliminate duplication while keeping it simple
4. **SOLID (Structure)** - Apply design principles that don't violate simplicity
5. **OOP (Organization)** - Use OOP concepts where they add clear value

### 3. Context-Sensitive Application

Principles should be adapted to project context:

- **Small Projects:** Emphasize KISS and YAGNI over complex SOLID implementations
- **Large Projects:** Apply full SOLID principles with careful DRY implementation
- **Legacy Code:** Prioritize KISS when refactoring, gradually introduce other principles
- **New Development:** Apply all principles from the start with proper balance

## Core Principle Interactions

Understanding how principles work together:

### Synergistic Relationships

- **DRY + SOLID:** Well-structured code naturally reduces duplication
- **KISS + YAGNI:** Simple solutions for current needs only
- **OOP + SOLID:** Object-oriented design following SOLID principles
- **KISS + DRY:** Simple abstractions that eliminate duplication

### Potential Conflicts

- **DRY vs KISS:** Over-abstraction can complicate simple solutions
- **SOLID vs YAGNI:** Complex design patterns for future needs vs current simplicity
- **OOP vs KISS:** Over-engineering object hierarchies vs straightforward solutions

### Conflict Resolution Strategies

1. **Favor Current Needs:** When in doubt, choose the solution that serves current requirements simply
2. **Measure Complexity:** If a principle adds significant complexity, reconsider its application
3. **Consider Team Experience:** Apply principles that the team can maintain effectively
4. **Review and Refactor:** Start simple, refactor to apply more principles as needs emerge

## AI Agent Implementation Guidelines

### Code Generation

When generating code, AI agents should:

1. **Start with KISS and YAGNI**
   - Generate the simplest solution that meets current requirements
   - Avoid speculative features or over-engineering

2. **Apply DRY Strategically**
   - Extract common functionality into reusable components
   - Avoid premature abstraction that adds unnecessary complexity

3. **Use OOP When Beneficial**
   - Apply encapsulation to hide implementation details
   - Use inheritance and polymorphism for clear conceptual relationships
   - Favor composition over inheritance when appropriate

4. **Follow SOLID Principles in Design**
   - Single Responsibility: Each class/function has one reason to change
   - Open/Closed: Open for extension, closed for modification
   - Liskov Substitution: Subclasses should be substitutable for their base classes
   - Interface Segregation: Clients shouldn't depend on interfaces they don't use
   - Dependency Inversion: Depend on abstractions, not concretions

### Code Review and Refactoring

When reviewing or improving code:

1. **Identify Principle Violations**
   - Look for code duplication (DRY violations)
   - Find overly complex solutions (KISS violations)
   - Spot unnecessary features (YAGNI violations)
   - Analyze design issues (SOLID violations)

2. **Prioritize Improvements**
   - Address KISS and YAGNI issues first
   - Then tackle DRY problems
   - Finally, improve SOLID compliance and OOP structure

3. **Maintain Backward Compatibility**
   - Apply principles without breaking existing functionality
   - Refactor incrementally to reduce risk
   - Test thoroughly after each principle-based improvement

## Measurable Standards

AI agents should enforce these quantifiable standards:

### Code Structure

- **Functions:** Maximum 20 lines (KISS principle)
- **Files:** Maximum 300 lines (KISS principle)
- **Classes:** Single responsibility (SOLID SRP)
- **Methods:** One clear purpose (SOLID SRP)

### Code Quality

- **Duplication:** No identical code blocks > 3 lines (DRY principle)
- **Complexity:** Cyclomatic complexity < 10 per function (KISS principle)
- **Abstraction:** Maximum 3 levels of inheritance (OOP best practices)
- **Dependencies:** Minimize coupling between modules (SOLID DIP)

### Documentation

- **Purpose:** Every class/function has clear purpose documentation
- **Principles:** Document which principles guided design decisions
- **Trade-offs:** Explain any principle conflicts and resolutions

## Integration with Other Rules

Development principles integrate with other Magic Vibe rules:

### Language Rules

- Principles guide language-specific implementations
- Language rules provide concrete ways to apply principles
- Together they ensure principled, idiomatic code

### Framework Rules

- Principles inform framework usage patterns
- Framework rules show principle application in specific contexts
- Combined they prevent framework-specific anti-patterns

### Workflow Rules

- Principles guide development process decisions
- Workflow rules enforce principle adherence through automation
- Together they create quality-focused development practices

## Continuous Improvement

Principle application should evolve:

### Learning and Adaptation

1. **Monitor Outcomes:** Track how principle application affects code quality
2. **Gather Feedback:** Collect team feedback on principle effectiveness
3. **Adjust Emphasis:** Modify principle priorities based on project needs
4. **Update Standards:** Refine measurable standards based on experience

### Knowledge Sharing

1. **Document Decisions:** Record principle-based design decisions
2. **Share Examples:** Provide concrete examples of principle application
3. **Train Teams:** Educate team members on principle benefits and trade-offs
4. **Review Regularly:** Conduct periodic reviews of principle adherence

This ensures that development principles remain practical, valuable, and effectively applied across all Magic Vibe implementations.
