---
description: Programming language-specific rules for AI agents to apply when working with projects in specific languages.
globs: "*.md"
alwaysApply: false
---

# Language Rules Index

This directory contains programming language-specific rules that AI agents should apply when working with projects in specific languages.

## Available Language Rules

- **Python:** `@languages/python.md` - Python development standards, PEP compliance, testing with pytest
- **TypeScript:** `@languages/typescript.md` - TypeScript/JavaScript development, type safety, modern ECMAScript
- **C++:** `@languages/cpp.md` - Modern C++ standards, memory management, performance optimization
- **Rust:** `@languages/rust.md` - Rust development patterns, ownership, error handling, cargo workflows

## Rule Application

AI agents automatically detect the primary programming language(s) in a project and apply the corresponding rules. Detection is based on:

1. **File Extensions:** `.py`, `.ts`, `.js`, `.cpp`, `.hpp`, `.rs`, etc.
2. **Project Configuration Files:** `package.json`, `Cargo.toml`, `requirements.txt`, `pyproject.toml`, etc.
3. **Build System Files:** `CMakeLists.txt`, `setup.py`, `tsconfig.json`, etc.
4. **Directory Structures:** Language-specific folder patterns and conventions

## Detection Priority

When multiple languages are detected in a project:
1. **Primary Language:** The language with the most source files
2. **Configuration Language:** Languages with build/config files present
3. **Imported Languages:** Languages used in dependencies or modules

## Integration with Core Rules

Language rules are applied alongside core Magic Vibe rules and should complement, not override, the core task management and workflow systems. Language-specific standards enhance the base development practices defined in the core rules.

## Conflict Resolution

If language rules conflict with each other or core rules:
- More specific language rules take precedence over general ones
- Language rules supplement but don't override core Magic Vibe functionality
- When multiple languages conflict, prioritize the primary project language
- Document any unresolved conflicts in task notes for human review