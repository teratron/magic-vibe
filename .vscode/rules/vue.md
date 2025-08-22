---
description: Comprehensive Vue.js guidelines optimized for AI agents. Includes best practices, code patterns, performance optimization, and testing strategies for modern Vue 3 applications.
globs: /**/*.vue, /**/*.ts, /**/*.js, components/**/*
---

# Vue.js Development Guidelines for AI Agents

## 1. Component Architecture Standards

### Component Structure Requirements

**MUST USE:**

- Composition API with `<script setup>` syntax (Vue 3.2+)
- TypeScript for all components and composables
- Single File Components (SFC) with proper organization
- Maximum 300 lines per component file
- Maximum 20 lines per computed/method function

**FILE STRUCTURE TEMPLATE:**

```vue
<template>
  <!-- Keep template clean and readable -->
</template>

<script setup lang="ts">
// 1. Imports (external libraries first, then internal)
// 2. Props and emits definitions
// 3. Reactive state
// 4. Computed properties
// 5. Methods and event handlers
// 6. Lifecycle hooks
// 7. Watchers
</script>

<style scoped>
/* Component-specific styles */
</style>
```

### Component Design Principles

**SINGLE RESPONSIBILITY:**

- One component = one purpose
- Break complex components into smaller, focused ones
- Extract reusable logic into composables
- Keep components under 100 lines when possible

**EXAMPLE - Good Component Structure:**

```vue
<template>
  <div class="user-profile">
    <UserAvatar :user="user" @click="showProfile" />
    <UserInfo :user="user" :editable="canEdit" />
    <LoadingSpinner v-if="isLoading" />
  </div>
</template>

<script setup lang="ts">
interface Props {
  userId: string
  readonly?: boolean
}

interface Emits {
  profileClick: [user: User]
  editComplete: [user: User]
}

const props = withDefaults(defineProps<Props>(), {
  readonly: false
})

const emit = defineEmits<Emits>()

const { user, isLoading, updateUser } = useUser(props.userId)
const { canEdit } = usePermissions()

const showProfile = () => {
  emit('profileClick', user.value)
}
</script>
```

## 2. Composition API Best Practices

### Reactive State Management

**PREFER:**

- `ref()` for primitive values
- `reactive()` for objects and arrays
- `computed()` for derived state
- `readonly()` for immutable data

**REACTIVITY PATTERNS:**

```typescript
// ✅ Good - Proper reactivity
const count = ref(0)
const user = reactive({ name: '', email: '' })
const doubleCount = computed(() => count.value * 2)

// ❌ Bad - Losing reactivity
const { name } = reactive({ name: '' }) // Destructuring loses reactivity
let localCount = count.value // Assignment loses reactivity
```

### Composables Design

**NAMING CONVENTION:**

- Prefix with `use`: `useUser`, `useAPI`, `useValidation`
- Return consistent structure with refs and functions
- Include loading states and error handling

**COMPOSABLE TEMPLATE:**

```typescript
export function useUser(userId: Ref<string>) {
  const user = ref<User | null>(null)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const fetchUser = async () => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await api.getUser(userId.value)
      user.value = response.data
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Unknown error'
    } finally {
      isLoading.value = false
    }
  }

  watchEffect(() => {
    if (userId.value) {
      fetchUser()
    }
  })

  return {
    user: readonly(user),
    isLoading: readonly(isLoading),
    error: readonly(error),
    refetch: fetchUser
  }
}
```

## 3. Props and Events Management

### Props Definition Standards

**REQUIRED STRUCTURE:**

```typescript
// ✅ Comprehensive props definition
interface Props {
  // Required props
  userId: string
  items: Array<Item>
  
  // Optional props with defaults
  maxItems?: number
  showHeader?: boolean
  variant?: 'primary' | 'secondary' | 'danger'
  
  // Complex object props
  config?: {
    sortable: boolean
    filterable: boolean
  }
}

const props = withDefaults(defineProps<Props>(), {
  maxItems: 10,
  showHeader: true,
  variant: 'primary',
  config: () => ({ sortable: false, filterable: false })
})
```

### Event Emission Standards

**EMIT DEFINITIONS:**

```typescript
interface Emits {
  // Payload events
  update: [value: string]
  select: [item: Item, index: number]
  
  // State change events
  loading: [isLoading: boolean]
  error: [error: Error | null]
  
  // User interaction events
  click: [event: MouseEvent]
  submit: [formData: FormData]
}

const emit = defineEmits<Emits>()

// Usage
const handleSelect = (item: Item, index: number) => {
  emit('select', item, index)
}
```

## 4. State Management with Pinia

### Store Structure Standards

**STORE TEMPLATE:**

```typescript
export const useUserStore = defineStore('user', () => {
  // State
  const users = ref<User[]>([])
  const currentUser = ref<User | null>(null)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  // Getters (computed)
  const userCount = computed(() => users.value.length)
  const activeUsers = computed(() => 
    users.value.filter(user => user.isActive)
  )

  // Actions
  const fetchUsers = async () => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await api.getUsers()
      users.value = response.data
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to fetch users'
      throw err
    } finally {
      isLoading.value = false
    }
  }

  const addUser = async (userData: CreateUserData) => {
    const user = await api.createUser(userData)
    users.value.push(user)
    return user
  }

  // Cleanup
  const resetStore = () => {
    users.value = []
    currentUser.value = null
    error.value = null
  }

  return {
    // State (readonly)
    users: readonly(users),
    currentUser: readonly(currentUser),
    isLoading: readonly(isLoading),
    error: readonly(error),
    
    // Getters
    userCount,
    activeUsers,
    
    // Actions
    fetchUsers,
    addUser,
    resetStore
  }
})
```

## 5. Performance Optimization

### Component Optimization

**LAZY LOADING:**

```typescript
// Route-level code splitting
const UserDashboard = defineAsyncComponent(
  () => import('./components/UserDashboard.vue')
)

// Conditional component loading
const HeavyChart = defineAsyncComponent({
  loader: () => import('./components/HeavyChart.vue'),
  loadingComponent: LoadingSpinner,
  errorComponent: ErrorMessage,
  delay: 200,
  timeout: 3000
})
```

**COMPUTED VS METHODS:**

```typescript
// ✅ Use computed for derived state
const filteredItems = computed(() => 
  items.value.filter(item => item.isActive)
)

// ❌ Don't use methods for derived state in templates
const getFilteredItems = () => 
  items.value.filter(item => item.isActive)
```

### Rendering Optimization

**v-show vs v-if Guidelines:**

```vue
<template>
  <!-- Use v-if for rarely toggled content -->
  <ExpensiveComponent v-if="shouldRenderExpensive" />
  
  <!-- Use v-show for frequently toggled content -->
  <div v-show="isVisible" class="toggle-content">
    Content that toggles frequently
  </div>
  
  <!-- Always use keys for dynamic lists -->
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">
      {{ item.name }}
    </li>
  </TransitionGroup>
</template>
```

## 6. Form Handling and Validation

### Form Management Pattern

```typescript
interface FormData {
  email: string
  password: string
  confirmPassword: string
}

const useForm = () => {
  const formData = reactive<FormData>({
    email: '',
    password: '',
    confirmPassword: ''
  })

  const errors = reactive<Partial<Record<keyof FormData, string>>>({})
  const isSubmitting = ref(false)

  const validateField = (field: keyof FormData) => {
    switch (field) {
      case 'email':
        errors.email = !formData.email.includes('@') 
          ? 'Valid email required' : ''
        break
      case 'password':
        errors.password = formData.password.length < 8 
          ? 'Password must be at least 8 characters' : ''
        break
      case 'confirmPassword':
        errors.confirmPassword = formData.password !== formData.confirmPassword 
          ? 'Passwords must match' : ''
        break
    }
  }

  const validateForm = () => {
    Object.keys(formData).forEach(key => 
      validateField(key as keyof FormData)
    )
    return Object.values(errors).every(error => !error)
  }

  const submitForm = async () => {
    if (!validateForm()) return
    
    isSubmitting.value = true
    try {
      await api.submitForm(formData)
      // Handle success
    } catch (error) {
      // Handle error
    } finally {
      isSubmitting.value = false
    }
  }

  const resetForm = () => {
    Object.keys(formData).forEach(key => {
      formData[key as keyof FormData] = ''
    })
    Object.keys(errors).forEach(key => {
      delete errors[key as keyof FormData]
    })
  }

  return {
    formData,
    errors: readonly(errors),
    isSubmitting: readonly(isSubmitting),
    validateField,
    submitForm,
    resetForm
  }
}
```

## 7. TypeScript Integration

### Component Type Safety

```typescript
// Define component ref types
const modalRef = ref<InstanceType<typeof Modal>>()
const inputRef = ref<HTMLInputElement>()

// Template ref with proper typing
const focusInput = () => {
  inputRef.value?.focus()
}

// Event handler typing
const handleSubmit = (event: Event) => {
  event.preventDefault()
  const form = event.target as HTMLFormElement
  const formData = new FormData(form)
  // Process form data
}
```

### Global Type Definitions

```typescript
// types/global.d.ts
declare global {
  interface User {
    id: string
    name: string
    email: string
    roles: Role[]
  }

  interface ApiResponse<T> {
    data: T
    message: string
    status: number
  }
}
```

## 8. Testing Standards

### Component Testing Template

```typescript
import { mount } from '@vue/test-utils'
import { describe, it, expect, vi } from 'vitest'
import UserProfile from './UserProfile.vue'

describe('UserProfile', () => {
  const defaultProps = {
    userId: 'user-123'
  }

  it('should render user information correctly', async () => {
    const wrapper = mount(UserProfile, {
      props: defaultProps
    })

    // Wait for async operations
    await wrapper.vm.$nextTick()

    expect(wrapper.find('[data-testid="user-name"]').text())
      .toBe('John Doe')
  })

  it('should emit profileClick when avatar is clicked', async () => {
    const wrapper = mount(UserProfile, {
      props: defaultProps
    })

    await wrapper.find('[data-testid="avatar"]').trigger('click')

    expect(wrapper.emitted('profileClick')).toBeTruthy()
    expect(wrapper.emitted('profileClick')?.[0]).toEqual([expect.any(Object)])
  })
})
```

### Composable Testing

```typescript
import { describe, it, expect } from 'vitest'
import { useCounter } from './useCounter'

describe('useCounter', () => {
  it('should increment count correctly', () => {
    const { count, increment } = useCounter()
    
    expect(count.value).toBe(0)
    increment()
    expect(count.value).toBe(1)
  })
})
```

## 9. Routing and Navigation

### Route Configuration

```typescript
const routes = [
  {
    path: '/users',
    name: 'UserList',
    component: () => import('./views/UserList.vue'),
    meta: {
      requiresAuth: true,
      roles: ['admin', 'user']
    }
  },
  {
    path: '/users/:id',
    name: 'UserDetail', 
    component: () => import('./views/UserDetail.vue'),
    props: route => ({ userId: route.params.id }),
    beforeEnter: (to, from, next) => {
      // Route-specific guard
      if (validateUserId(to.params.id)) {
        next()
      } else {
        next('/404')
      }
    }
  }
]
```

## 10. Build and Development Setup

### Vite Configuration

```typescript
// vite.config.ts
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@/components': path.resolve(__dirname, './src/components')
    }
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['vue', 'vue-router', 'pinia'],
          ui: ['@/components/ui']
        }
      }
    }
  }
})
```

## 11. AI-Specific Guidelines

### Code Generation Requirements

**WHEN GENERATING VUE COMPONENTS:**

- Always use TypeScript with proper type definitions
- Include comprehensive props and emits interfaces
- Add data-testid attributes for testing
- Generate accompanying unit tests
- Include proper error handling and loading states

### Component Analysis Checklist

**BEFORE SUBMITTING CODE:**

- [ ] Component follows single responsibility principle
- [ ] Props are properly typed with interfaces
- [ ] Emits are defined with proper payloads
- [ ] Composables return readonly state where appropriate
- [ ] Error handling is comprehensive
- [ ] Performance optimizations are applied
- [ ] Tests cover main functionality
- [ ] TypeScript compilation passes without errors

### Common Vue Anti-Patterns to Avoid

**NEVER DO:**

- Mutate props directly
- Use `any` type in TypeScript
- Access `$parent` or `$children`
- Use global event bus for component communication
- Mix Options API and Composition API in the same component
- Forget to handle loading and error states in async operations
