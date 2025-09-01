# Template AI-Rules

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI-Optimized](https://img.shields.io/badge/AI-Optimized-brightgreen.svg)](https://github.com/zigenzoog/template-ai-rules)
[![Version](https://img.shields.io/badge/Version-1.0-blue.svg)](https://github.com/zigenzoog/template-ai-rules/releases)

> **Comprehensive configuration and rule template repository designed for AI-powered code editors and agents**

A standardized set of development guidelines, workflows, and best practices optimized for AI-assisted development tools including Cursor, Windsurf, Trae, Kiro, Qoder and other AI coding agents.

## 🚀 Quick Start

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zigenzoog/template-ai-rules.git
   cd template-ai-rules
   ```

2. **Configure for your AI editor:**

   ```bash
   # For Cursor IDE
   mv .vscode .cursor
   
   # For Windsurf
   mv .vscode .windsurf
   
   # For other AI editors
   mv .vscode .your-editor-name
   ```

3. **Copy to your project:**

   ```bash
   cp -r .cursor /path/to/your/project/
   # or
   cp -r .windsurf /path/to/your/project/
   ```

### Supported AI Editors

- **VS Code** (`.vscode`)
- **Cursor** (`.cursor`)
- **Windsurf** (`.windsurf`)
- **Trae** (`.trae`)
- **Kiro** (`.kiro`)
- **Qoder** (`.qoder`)
- **VS Code with AI extensions** (`.vscode`)
- **Any AI-powered editor** (custom naming)

## 📋 Rule Categories

### 🎯 Task Management System

**[Magic Vibe System](.magic-vibe/rules/)** - Comprehensive workflow management framework for AI agents:

- **[English Documentation](.magic-vibe/rules/README.md)** - Complete system guide
- **[Russian Documentation](.magic-vibe/rules/README.ru.md)** - Полное руководство системы

- **[System Overview](.magic-vibe/rules/_index.md)** - Complete system documentation
- **[Workflow Management](.magic-vibe/rules/workflow.md)** - Process management
- **[Task Definition & Tracking](.magic-vibe/rules/tasks.md)** - Task system rules
- **[Project Planning](.magic-vibe/rules/plans.md)** - Planning strategies
- **[Memory & Context](.magic-vibe/rules/memory.md)** - Context management
- **[Task Expansion](.magic-vibe/rules/expand.md)** - Scalability patterns
- **[Event Automation](.magic-vibe/rules/hooks.md)** - Hook system
- **[Version Management](.magic-vibe/rules/versioning.md)** - Automated versioning
- **[Development Principles](.magic-vibe/rules/principles/)** - OOP, SOLID, DRY, KISS, YAGNI

### 🏗️ Language & Framework Rules

**[AI-Optimized Development Standards](.vscode/rules/)** - Technology-specific rules for consistent code generation:

#### Version Control & Workflows

- **[GitFlow](.vscode/rules/gitflow.md)** - Comprehensive GitFlow workflow with automation
- **[Trunk-Based Development](.vscode/rules/trunk-based-development.md)** - High-velocity development practices
- **[Commit Messages](.vscode/rules/commit-messages.md)** - Conventional commit standards

#### Code Quality & Best Practices

- **[Clean Code](.vscode/rules/clean-code.md)** - Fundamental clean coding principles
- **[Code Quality](.vscode/rules/code-quality.md)** - AI-specific quality standards

### 💻 Programming Languages

#### Systems Programming

- **[C++](.vscode/rules/cpp.md)** - Modern C++ standards (C++17/20/23)
- **[Rust](.vscode/rules/rust.md)** - Memory-safe systems programming

#### Application Development

- **[Python](.vscode/rules/python.md)** - Python best practices and patterns
- **[TypeScript](.vscode/rules/typescript.md)** - Type-safe JavaScript development

### 🌐 Web Development Frameworks

#### Frontend Frameworks

- **[React](.vscode/rules/react.md)** - Modern React development patterns
- **[Vue](.vscode/rules/vue.md)** - Vue.js composition API and best practices
- **[Svelte](.vscode/rules/svelte.md)** - Svelte/SvelteKit development guidelines
- **[Next.js](.vscode/rules/nextjs.md)** - Full-stack React framework

#### Styling & UI

- **[Tailwind CSS](.vscode/rules/tailwindcss.md)** - Utility-first CSS framework
- **[Sass](.vscode/rules/sass.md)** - Advanced CSS preprocessing

#### Backend Development

- **[FastAPI](.vscode/rules/fastapi.md)** - Modern Python web framework
- **[Database](.vscode/rules/database.md)** - Database design and optimization

## ✨ Key Features

### 🤖 AI-Optimized Guidelines

- **8-Section Structure**: Code Generation, Change Management, Communication, Quality Assurance, Security & Performance, Language-Specific Standards, Continuous Improvement, AI-Specific Best Practices
- **Measurable Standards**: Clear metrics (20-line functions, 300-line files, 90% test coverage)
- **Actionable Checklists**: Step-by-step validation and implementation guides
- **Automated Validation**: Scripts and tools for quality enforcement

### 🔒 Security & Performance

- **Built-in Security Patterns**: Input validation, XSS prevention, dependency scanning
- **Performance Optimization**: Bundle size limits, lazy loading, caching strategies
- **Monitoring Integration**: Performance tracking and alerting
- **Error Recovery**: Automated rollback and incident response

### 🔄 Workflow Automation

- **CI/CD Integration**: Automated pipelines and quality gates
- **Git Hooks**: Pre-commit validation and enforcement
- **Feature Flags**: Safe deployment and gradual rollouts
- **Testing Frameworks**: Comprehensive testing strategies

## 📊 Quality Standards

All rules include:

- ✅ **Measurable Metrics**: Specific limits and thresholds
- 🔍 **Validation Scripts**: Automated checking tools
- 📝 **Code Examples**: Working implementations
- 🧪 **Testing Requirements**: Coverage and quality standards
- 🔐 **Security Guidelines**: Best practices and patterns
- ⚡ **Performance Targets**: Optimization requirements
- 📚 **Documentation**: Comprehensive guides and examples

## 🛠️ Advanced Configuration

### Custom Rule Sets

Create custom combinations of rules for specific project types:

```bash
# Full-stack TypeScript project
cp .vscode/rules/typescript.md .vscode/rules/react.md .vscode/rules/nextjs.md .vscode/rules/tailwindcss.md ./project-rules/

# Python API project
cp .vscode/rules/python.md .vscode/rules/fastapi.md .vscode/rules/database.md ./project-rules/

# Systems programming
cp .vscode/rules/cpp.md .vscode/rules/rust.md ./project-rules/
```

### Integration Examples

#### GitHub Actions

```yaml
# .github/workflows/ai-validation.yml
name: AI Code Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run AI Quality Gates
        run: ./scripts/validate-ai-code.sh
```

#### Pre-commit Hooks

```bash
# Install AI-optimized pre-commit hooks
cp .vscode/scripts/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit
```

## 🎯 Use Cases

### For AI Coding Assistants

- **Code Generation**: Generate compliant, tested code
- **Code Review**: Automated quality assessment
- **Refactoring**: Safe, pattern-based improvements
- **Documentation**: Consistent, comprehensive docs

### For Development Teams

- **Onboarding**: Standardized practices for new team members
- **Quality Assurance**: Consistent code quality across projects
- **Security**: Built-in security best practices
- **Performance**: Optimization guidelines and monitoring

### For Project Management

- **Workflow Standardization**: Consistent development processes
- **Quality Metrics**: Measurable quality indicators
- **Risk Mitigation**: Automated validation and rollback
- **Team Collaboration**: Shared standards and practices

## 🔧 Troubleshooting

### Common Issues

1. **Editor not recognizing rules**:

   ```bash
   # Ensure correct directory naming
   ls -la | grep -E '\.(cursor|windsurf|vscode)'
   ```

2. **Validation scripts failing**:

   ```bash
   # Check script permissions
   chmod +x scripts/*.sh
   ```

3. **Rule conflicts**:

   ```bash
   # Validate rule consistency
   ./scripts/validate-rules.sh
   ```

## 📈 Metrics & Analytics

Track the effectiveness of your AI-assisted development:

- **Code Quality**: Automated quality scoring
- **Development Velocity**: Deployment frequency and lead time
- **Error Rates**: Bug detection and resolution metrics
- **Security**: Vulnerability scanning and compliance
- **Performance**: Application and development workflow performance

## 🤝 Contributing

We welcome contributions to improve the template-ai-rules project:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-improvement`)
3. **Follow** the established rule patterns
4. **Test** your changes with AI editors
5. **Submit** a pull request

### Development Guidelines

- Follow the 8-section structure for all new rules
- Include measurable standards and validation scripts
- Provide working code examples
- Test with multiple AI editors
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [AI Coding Best Practices](https://github.com/ai-coding-practices)
- [Clean Code Guidelines](https://github.com/clean-code-guidelines)
- [Development Workflow Templates](https://github.com/workflow-templates)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/zigenzoog/template-ai-rules/issues)
- **Discussions**: [GitHub Discussions](https://github.com/zigenzoog/template-ai-rules/discussions)
- **Documentation**: [Wiki](https://github.com/zigenzoog/template-ai-rules/wiki)

---

Made with ❤️ for the AI development community
