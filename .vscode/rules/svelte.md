---
description: Comprehensive Svelte development guidelines optimized for AI agents. Includes measurable standards, automated validation, and quality checklists for building modern, performant web applications.
globs: /**/*.svelte, src/**/*.ts, src/**/*.js, /**/*.config.js, /**/*.config.ts
---

# Svelte Development Guidelines for AI Agents

## 1. Code Generation Standards

### Component Complexity Limits

**MEASURABLE STANDARDS:**

- Components: Maximum 200 lines per `.svelte` file
- Functions: Maximum 20 lines (preferred), 30 lines (absolute max)
- Script blocks: Maximum 150 lines per component
- Template blocks: Maximum 100 lines of markup
- CSS blocks: Maximum 50 lines per component
- Props: Maximum 10 props per component
- Reactive statements: Maximum 15 per component

**COMPONENT STRUCTURE TEMPLATE:**

```svelte
<script lang="ts">
  // 1. Imports (external first, then local)
  import { onMount, createEventDispatcher } from 'svelte';
  import type { User } from './types';
  
  // 2. Props with TypeScript types
  export let user: User;
  export let isLoading = false;
  export let onSave: (user: User) => Promise<void> = async () => {};
  
  // 3. Event dispatcher
  const dispatch = createEventDispatcher<{
    userUpdated: User;
    error: string;
  }>();
  
  // 4. Local state
  let isEditing = false;
  let errorMessage = '';
  
  // 5. Reactive declarations (max 15)
  $: isValid = user.name.length > 0 && user.email.includes('@');
  $: canSave = isValid && !isLoading;
  
  // 6. Functions (max 20 lines each)
  async function handleSave() {
    if (!canSave) return;
    
    try {
      await onSave(user);
      dispatch('userUpdated', user);
      isEditing = false;
    } catch (error) {
      errorMessage = error.message;
      dispatch('error', error.message);
    }
  }
  
  // 7. Lifecycle
  onMount(() => {
    // Initialize component
  });
</script>

<!-- Template (max 100 lines) -->
<div class="user-card" class:editing={isEditing}>
  <header class="user-card__header">
    <h2>{user.name}</h2>
    <button on:click={() => isEditing = !isEditing} disabled={isLoading}>
      {isEditing ? 'Cancel' : 'Edit'}
    </button>
  </header>
  
  {#if isEditing}
    <form on:submit|preventDefault={handleSave}>
      <input bind:value={user.name} placeholder="Name" required />
      <input bind:value={user.email} type="email" placeholder="Email" required />
      
      {#if errorMessage}
        <div class="error" role="alert">{errorMessage}</div>
      {/if}
      
      <button type="submit" disabled={!canSave}>
        {isLoading ? 'Saving...' : 'Save'}
      </button>
    </form>
  {:else}
    <div class="user-info">
      <p>Email: {user.email}</p>
    </div>
  {/if}
</div>

<!-- Styles (max 50 lines, component-scoped) -->
<style>
  .user-card {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1rem;
    max-width: 400px;
  }
  
  .user-card__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .error {
    color: var(--error-color, #e53e3e);
    font-size: 0.875rem;
    margin: 0.5rem 0;
  }
</style>
```

### Naming Conventions

**MANDATORY PATTERNS:**

```text
Components:          PascalCase          (UserCard.svelte, EmailValidator.svelte)
Variables/Functions: camelCase           (userName, handleSubmit, isLoading)
CSS Classes:         BEM or kebab-case   (.user-card, .user-card__title)
Props:               camelCase           (userId, onSubmit, isDisabled)
Stores:              camelCase           (userStore, authStore)
Events:              camelCase           (userUpdated, formSubmitted)
```

## 2. Change Management

### Component Versioning

**BACKWARD COMPATIBILITY:**

```svelte
<!-- Version 2.0 - With backward compatibility -->
<script>
  // New structured prop (preferred)
  export let user: { name: string; email: string } | undefined = undefined;
  
  // Legacy prop with deprecation warning
  export let userName: string | undefined = undefined;
  
  // Maintain compatibility
  $: if (userName && !user) {
    console.warn('userName prop is deprecated. Use user object instead.');
    user = { name: userName, email: '' };
  }
</script>
```

### Atomic Changes

**COMMIT SCOPE GUIDELINES:**

```text
Single Component:     One .svelte file + test + story
Feature Addition:     Component + store + types + tests
Bug Fix:             Minimal change with regression test
Refactoring:         Extract components, no behavior change
```

## 3. Communication Standards

### Component Documentation

**DOCUMENTATION TEMPLATE:**

```svelte
<!--
 @component UserCard
 @description Displays user information with edit functionality
 
 @props
 - user: User - User object with id, name, and email
 - isLoading?: boolean - Shows loading state
 - onSave?: (user: User) => Promise<void> - Save handler
 
 @events
 - userUpdated: User - Fired when user is updated
 - error: string - Fired when error occurs
 
 @example
 <UserCard 
   user={{ id: '1', name: 'John', email: 'john@example.com' }}
   on:userUpdated={handleUpdate}
 />
-->
```

**TYPE DEFINITIONS:**

```typescript
// types.ts
export interface User {
  /** Unique identifier */
  id: string;
  /** User's display name (2-50 characters) */
  name: string;
  /** Valid email address */
  email: string;
}

export interface UserCardEvents {
  userUpdated: User;
  error: { message: string; code: string };
}
```

## 4. Quality Assurance

### Testing Standards

**COMPONENT TEST STRUCTURE:**

```typescript
// UserCard.test.ts
import { render, screen, fireEvent } from '@testing-library/svelte';
import UserCard from './UserCard.svelte';

const mockUser = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com'
};

describe('UserCard Component', () => {
  it('should display user information', () => {
    render(UserCard, { props: { user: mockUser } });
    
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('Email: john@example.com')).toBeInTheDocument();
  });
  
  it('should enter edit mode when edit button clicked', async () => {
    render(UserCard, { props: { user: mockUser } });
    
    await fireEvent.click(screen.getByRole('button', { name: /edit/i }));
    
    expect(screen.getByDisplayValue('John Doe')).toBeInTheDocument();
  });
});
```

**COVERAGE REQUIREMENTS:**

```text
Component Coverage:   ≥ 85% (statements, branches, functions)
Store Coverage:       ≥ 90% (all actions and derived states)
Utility Coverage:     ≥ 95% (pure functions)
Integration Coverage: ≥ 70% (component + store interactions)
```

## 5. Security and Performance

### Security Standards

**XSS PREVENTION:**

```svelte
<script>
  import { sanitizeHtml } from '../utils/security';
  
  export let userContent: string;
  
  // Sanitize user-generated content
  $: safeContent = sanitizeHtml(userContent);
</script>

<!-- ✅ Safe HTML rendering -->
<div class="user-content">
  {@html safeContent}
</div>

<!-- ❌ Never do this -->
<div>{@html userInput}</div>  <!-- Direct HTML injection -->
```

**INPUT VALIDATION:**

```svelte
<script>
  import { z } from 'zod';
  
  const userSchema = z.object({
    name: z.string().min(2).max(50),
    email: z.string().email()
  });
  
  export let user: User;
  let validationErrors: Record<string, string> = {};
  
  $: isValid = validateUser(user);
  
  function validateUser(userData: User) {
    try {
      userSchema.parse(userData);
      validationErrors = {};
      return true;
    } catch (error) {
      // Handle validation errors
      return false;
    }
  }
</script>
```

### Performance Standards

**BUNDLE SIZE LIMITS:**

```text
Component Bundle:     < 50KB gzipped per route
Total Initial Load:   < 300KB gzipped
Component Chunks:     < 20KB gzipped each
```

**OPTIMIZATION PATTERNS:**

```svelte
<!-- ✅ Lazy loading -->
<script>
  let HeavyComponent;
  let shouldLoad = false;
  
  async function loadComponent() {
    if (!HeavyComponent && shouldLoad) {
      const module = await import('./HeavyComponent.svelte');
      HeavyComponent = module.default;
    }
  }
</script>

{#if HeavyComponent}
  <svelte:component this={HeavyComponent} />
{:else if shouldLoad}
  <div class="loading">Loading...</div>
{/if}

<!-- ✅ Virtual scrolling for large lists -->
<script>
  import { VirtualList } from '@sveltejs/svelte-virtual-list';
  
  export let items: Item[];
</script>

{#if items.length > 100}
  <VirtualList {items} itemHeight={60} let:item>
    <ItemComponent {item} />
  </VirtualList>
{:else}
  {#each items as item (item.id)}
    <ItemComponent {item} />
  {/each}
{/if}
```

## 6. Language-Specific Standards

### SvelteKit Integration

**PAGE COMPONENT:**

```svelte
<!-- src/routes/users/[id]/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types';
  import UserCard from '$lib/components/UserCard.svelte';
  import { page } from '$app/stores';
  
  export let data: PageData;
  
  $: user = data.user;
  $: userId = $page.params.id;
</script>

<svelte:head>
  <title>{user.name} - User Profile</title>
</svelte:head>

<main>
  <UserCard {user} />
</main>
```

**LOAD FUNCTION:**

```typescript
// src/routes/users/[id]/+page.ts
import type { PageLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageLoad = async ({ params, fetch }) => {
  const response = await fetch(`/api/users/${params.id}`);
  
  if (!response.ok) {
    throw error(404, 'User not found');
  }
  
  const user = await response.json();
  return { user };
};
```

### Store Patterns

**TYPED STORE:**

```typescript
// stores/userStore.ts
import { writable, derived } from 'svelte/store';

interface UserState {
  users: User[];
  isLoading: boolean;
  error: string | null;
}

const { subscribe, set, update } = writable<UserState>({
  users: [],
  isLoading: false,
  error: null
});

export const userStore = {
  subscribe,
  
  async loadUsers() {
    update(state => ({ ...state, isLoading: true }));
    
    try {
      const response = await fetch('/api/users');
      const users = await response.json();
      update(state => ({ ...state, users, isLoading: false }));
    } catch (error) {
      update(state => ({ ...state, error: error.message, isLoading: false }));
    }
  },
  
  reset() {
    set({ users: [], isLoading: false, error: null });
  }
};

// Derived stores
export const activeUsers = derived(
  userStore,
  $userStore => $userStore.users.filter(user => user.isActive)
);
```

## 7. Continuous Improvement

### Refactoring Guidelines

**REFACTORING TRIGGERS:**

```text
Component Size:       > 200 lines → Split into smaller components
Function Length:      > 20 lines → Extract utility functions
Prop Count:          > 10 props → Use prop objects
Reactive Statements: > 15 → Move to derived stores
CSS Lines:           > 50 → Extract to external stylesheet
```

**PERFORMANCE MONITORING:**

```svelte
<script>
  import { dev } from '$app/environment';
  
  // Performance monitoring in development
  if (dev) {
    onMount(() => {
      console.time('ComponentMount');
      return () => console.timeEnd('ComponentMount');
    });
  }
</script>
```

## 8. AI-Specific Best Practices

### Code Generation Validation

**PRE-GENERATION CHECKLIST:**

```text
Requirement Analysis:
☐ Component purpose clearly defined
☐ Props and events specified
☐ State management approach chosen
☐ Accessibility requirements identified
☐ Performance constraints understood

Design Decisions:
☐ Component structure follows template
☐ Naming conventions applied
☐ TypeScript types defined
☐ Error handling planned
☐ Testing strategy outlined
```

**POST-GENERATION VALIDATION:**

```bash
#!/bin/bash
# Automated validation for AI-generated Svelte code

echo "🔨 Building Svelte app..."
npm run build

echo "🧪 Running component tests..."
npm run test

echo "🔍 Linting Svelte files..."
npm run lint

echo "🎨 Checking format..."
npm run format:check

echo "📱 Accessibility check..."
npm run test:a11y

echo "✅ All validations passed!"
```

### Quality Metrics

**AUTOMATED QUALITY GATES:**

```text
Code Quality:
• Component size: ≤ 200 lines
• Function length: ≤ 20 lines
• Props count: ≤ 10 per component
• Test coverage: ≥ 85%
• Bundle size: < 50KB gzipped
• Build warnings: Zero allowed
• Accessibility: WCAG AA compliant
• Performance: Lighthouse score > 90
```

### Error Recovery Patterns

**ROBUST ERROR HANDLING:**

```svelte
<script>
  import { createEventDispatcher } from 'svelte';
  
  const dispatch = createEventDispatcher();
  
  let error = null;
  let retryCount = 0;
  const MAX_RETRIES = 3;
  
  async function handleOperation() {
    try {
      error = null;
      await performOperation();
    } catch (err) {
      error = err.message;
      
      if (retryCount < MAX_RETRIES) {
        retryCount++;
        setTimeout(handleOperation, 1000 * retryCount);
      } else {
        dispatch('error', { error: err, retryCount });
      }
    }
  }
</script>

{#if error && retryCount >= MAX_RETRIES}
  <div class="error-state">
    <p>Something went wrong: {error}</p>
    <button on:click={() => { retryCount = 0; handleOperation(); }}>
      Try Again
    </button>
  </div>
{/if}
```

---

## Summary

These guidelines provide AI agents with:

1. **Measurable Standards**: Clear limits for component complexity
2. **Structured Templates**: Consistent component organization
3. **Type Safety**: TypeScript integration patterns
4. **Testing Framework**: Comprehensive testing strategies
5. **Security Practices**: XSS prevention and input validation
6. **Performance Optimization**: Bundle size and rendering efficiency
7. **SvelteKit Integration**: Modern full-stack patterns
8. **Quality Assurance**: Automated validation and monitoring

Follow these guidelines to generate production-ready, maintainable, and performant Svelte applications.
