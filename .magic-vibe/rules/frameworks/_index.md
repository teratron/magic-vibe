---
description: Framework-specific rules for AI agents to apply when working with projects using specific frameworks or libraries.
globs: "*.md"
alwaysApply: false
---

# Framework Rules Index

This directory contains framework-specific rules that AI agents should apply when working with projects using specific frameworks or libraries.

## Available Framework Rules

- **React:** `@frameworks/react.md` - React component patterns, hooks, state management, JSX standards
- **Vue.js:** `@frameworks/vue.md` - Vue 3 composition API, component structure, state management
- **Next.js:** `@frameworks/nextjs.md` - Next.js app router, SSR/SSG patterns, API routes, file conventions
- **FastAPI:** `@frameworks/fastapi.md` - FastAPI development patterns, async programming, API design
- **TailwindCSS:** `@frameworks/tailwindcss.md` - Utility-first CSS framework patterns and best practices
- **Svelte:** `@frameworks/svelte.md` - Svelte component patterns, reactivity, SvelteKit integration
- **SASS/SCSS:** `@frameworks/sass.md` - SASS/SCSS coding style guide, BEM methodology, file organization
- **Database:** `@frameworks/database.md` - Database best practices with Prisma and Supabase integration
- **Laravel:** `@frameworks/laravel.md` - Laravel framework development with MVC architecture, Eloquent ORM, and modern PHP practices

## Rule Application

AI agents automatically detect frameworks by analyzing:

1. **Package Dependencies:** Dependencies listed in `package.json`, `requirements.txt`, `Cargo.toml`, etc.
2. **Import Statements:** Framework-specific import patterns and module usage
3. **Configuration Files:** Framework config files like `next.config.js`, `vue.config.js`, `svelte.config.js`
4. **Directory Structures:** Framework-specific folder patterns and file conventions
5. **Build Tools:** Framework-specific build configurations and tooling

## Framework Detection Priority

When multiple frameworks are detected, apply rules in this order:

1. **Primary Application Framework:** React, Vue, Angular, Svelte
2. **Meta-Frameworks:** Next.js, Nuxt.js, SvelteKit, Remix
3. **Backend Frameworks:** FastAPI, Express, Django, Flask
4. **Utility Frameworks:** TailwindCSS, styled-components, Material-UI
5. **Testing Frameworks:** Jest, Vitest, Cypress, Playwright

## Framework Ecosystem Integration

Frameworks often work together in a stack:

- **Frontend + Meta-framework:** React + Next.js, Vue + Nuxt.js
- **Frontend + Styling:** React + TailwindCSS, Vue + Vuetify
- **Backend + Frontend:** FastAPI + React, Django + Vue
- **Full-stack:** Next.js (full-stack), SvelteKit (full-stack)

## Integration Guidelines

Framework rules should be applied consistently while respecting the framework ecosystem:

- Meta-framework rules take precedence over base framework rules
- Styling framework rules supplement but don't override component framework rules
- Backend framework rules are independent but can inform API design for frontend frameworks
- Testing framework rules complement but don't override application framework testing patterns

## Conflict Resolution

When framework rules conflict:

1. **Specificity Wins:** More specific framework rules override general ones
2. **Ecosystem Respect:** Follow the intended framework ecosystem patterns
3. **Meta-framework Priority:** Meta-frameworks (Next.js, Nuxt.js) override base frameworks
4. **Documentation Required:** Document conflicts and decisions in task notes
