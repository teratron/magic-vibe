# Development Principles

This directory contains comprehensive guides for fundamental software development principles that should be applied during AI-assisted code generation and development.

## Available Principles

### 1. Object-Oriented Programming (OOP)

**File:** `oop.md`  
**Description:** Comprehensive guide covering the four fundamental OOP principles:

- Encapsulation
- Inheritance  
- Polymorphism
- Abstraction

Includes practical examples, best practices, and common anti-patterns to avoid.

### 2. SOLID Design Principles

**File:** `solid.md`  
**Description:** Detailed coverage of all five SOLID principles:

- **S**ingle Responsibility Principle (SRP)
- **O**pen/Closed Principle (OCP)
- **L**iskov Substitution Principle (LSP)
- **I**nterface Segregation Principle (ISP)
- **D**ependency Inversion Principle (DIP)

Each principle includes examples, implementation guidelines, and testing strategies.

### 3. DRY Principle (Don't Repeat Yourself)

**File:** `dry.md`  
**Description:** Guide for eliminating code duplication and promoting reusability:

- Code duplication identification and elimination
- Configuration and knowledge centralization
- Template patterns and utility functions
- When NOT to apply DRY (avoiding over-abstraction)

### 4. KISS Principle (Keep It Simple, Stupid)

**File:** `kiss.md`  
**Description:** Principles for writing simple, clear, and maintainable code:

- Simplicity guidelines and best practices
- Avoiding over-engineering and unnecessary complexity
- Clear naming conventions and readable code structure
- Balance between simplicity and functionality

### 5. YAGNI Principle (You Aren't Gonna Need It)

**File:** `yagni.md`  
**Description:** Guide for avoiding premature feature implementation:

- Focus on current requirements vs. speculative features
- Avoiding over-flexible configurations
- Incremental development approaches
- When to add complexity vs. when to keep it simple

## Usage

Each principle file is designed to be referenced by AI coding assistants and follows the standardized rule format:

```markdown
---
description: Brief description of the principle.
globs:
alwaysApply: true
---

# Principle Name

Whenever you use this rule, start your message with the following:
"Applying [Principle] principle..."
```

## Integration

These principles work together and complement each other:

- **OOP + SOLID**: Provide structure for object-oriented design
- **DRY + KISS**: Balance reusability with simplicity  
- **YAGNI + KISS**: Prevent over-engineering and unnecessary complexity
- **SOLID + DRY**: Promote maintainable and reusable code architecture

All principles include validation checklists, code examples, testing guidelines, and integration strategies with other development practices.
