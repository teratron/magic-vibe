---
description: Comprehensive TypeScript guidelines optimized for AI agents. Includes type safety, modern patterns, performance optimization, and testing strategies for enterprise-grade TypeScript applications.
globs: /**/*.ts, /**/*.tsx, /**/*.d.ts
---

# TypeScript Development Guidelines for AI Agents

## 1. Type System Fundamentals

### Core Type Safety Principles

**MANDATORY REQUIREMENTS:**

- Enable strict mode in `tsconfig.json` (`strict: true`)
- Maximum function length: 20 lines
- Maximum file length: 300 lines
- Zero tolerance for `any` types in production code
- All public APIs must have explicit return types

**TYPE DEFINITIONS:**

```typescript
// ✅ Good - Interface for object shapes
interface User {
  readonly id: string
  name: string
  email: string
  roles: Role[]
  createdAt: Date
  updatedAt: Date
}

// ✅ Good - Type for unions and computed types
type UserRole = 'admin' | 'editor' | 'viewer'
type UserWithoutDates = Omit<User, 'createdAt' | 'updatedAt'>
type PartialUser = Partial<Pick<User, 'name' | 'email'>>

// ❌ Bad - Using any
type BadUser = {
  id: any // Never use any!
  data: any // Use unknown instead
}

// ✅ Good - Use unknown for uncertain types
type ApiResponse<T> = {
  data: T
  metadata: unknown // Will be validated at runtime
  status: number
}
```

### Advanced Type Patterns

**UTILITY TYPES USAGE:**

```typescript
// Built-in utility types
type CreateUserRequest = Pick<User, 'name' | 'email'>
type UpdateUserRequest = Partial<Pick<User, 'name' | 'email'>>
type UserKeys = keyof User
type RequiredUser = Required<User>

// Custom utility types
type NonEmptyArray<T> = [T, ...T[]]
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object ? DeepReadonly<T[P]> : T[P]
}

// Conditional types for complex scenarios
type ApiEndpoint<T extends string> = T extends `/${infer Path}` 
  ? Path 
  : never

type ExtractArrayType<T> = T extends (infer U)[] ? U : never
```

### Generic Type Constraints

```typescript
// ✅ Good - Proper generic constraints
interface Repository<T extends { id: string }> {
  findById(id: string): Promise<T | null>
  create(data: Omit<T, 'id'>): Promise<T>
  update(id: string, data: Partial<T>): Promise<T>
  delete(id: string): Promise<void>
}

// ✅ Good - Multiple generic constraints
function mergeObjects<
  T extends Record<string, unknown>,
  U extends Record<string, unknown>
>(obj1: T, obj2: U): T & U {
  return { ...obj1, ...obj2 }
}

// ✅ Good - Conditional generic types
type ApiResult<T, E extends Error = Error> = {
  success: true
  data: T
} | {
  success: false
  error: E
}
```

## 2. Naming Conventions and Code Organization

### Naming Standards

**REQUIRED CONVENTIONS:**

```typescript
// Types and Interfaces - PascalCase
interface UserProfile {}
type DatabaseConnection = {}
class ApiClient {}
enum UserStatus {}

// Variables and Functions - camelCase
const currentUser = ref<User | null>(null)
const isLoading = ref(false)
function getUserById(id: string) {}
const handleSubmit = async () => {}

// Constants - SCREAMING_SNAKE_CASE
const MAX_RETRY_ATTEMPTS = 3
const API_BASE_URL = 'https://api.example.com'
const DEFAULT_TIMEOUT_MS = 5000

// Boolean prefixes for clarity
const isValid = true
const hasPermission = false
const canEdit = computed(() => user.value?.role === 'admin')
const shouldRender = ref(false)

// Event handlers
const handleClick = (event: MouseEvent) => {}
const onSubmit = (data: FormData) => {}
const onError = (error: Error) => {}
```

### File Organization Structure

**DIRECTORY STRUCTURE:**

```text
src/
├── types/
│   ├── api.ts          # API-related types
│   ├── user.ts         # User domain types
│   ├── common.ts       # Shared utility types
│   └── index.ts        # Barrel exports
├── services/
│   ├── api.ts
│   ├── auth.ts
│   └── index.ts
├── utils/
│   ├── validation.ts
│   ├── formatting.ts
│   └── index.ts
└── components/
    ├── common/
    └── features/
```

**BARREL EXPORTS PATTERN:**

```typescript
// types/index.ts
export type { User, UserRole, UserProfile } from './user'
export type { ApiResponse, ApiError, ApiEndpoint } from './api'
export type { ValidationError, FormData } from './common'

// Import usage
import type { User, ApiResponse } from '@/types'
```

## 3. Function Design and Implementation

### Function Type Definitions

**EXPLICIT RETURN TYPES:**

```typescript
// ✅ Good - Explicit return types for public functions
export async function fetchUser(id: string): Promise<User | null> {
  try {
    const response = await api.get<ApiResponse<User>>(`/users/${id}`)
    return response.data.data
  } catch (error) {
    if (error instanceof ApiError && error.status === 404) {
      return null
    }
    throw error
  }
}

// ✅ Good - Function overloads for complex scenarios
function processData(input: string): string
function processData(input: number): number
function processData(input: string[]): string[]
function processData(input: string | number | string[]): unknown {
  if (typeof input === 'string') {
    return input.trim().toLowerCase()
  }
  if (typeof input === 'number') {
    return Math.round(input * 100) / 100
  }
  return input.map(item => item.trim().toLowerCase())
}

// ✅ Good - Higher-order function typing
type EventHandler<T> = (event: T) => void | Promise<void>
type AsyncValidator<T> = (value: T) => Promise<ValidationResult>

function createValidator<T>(
  validator: AsyncValidator<T>
): (value: T) => Promise<boolean> {
  return async (value: T) => {
    const result = await validator(value)
    return result.isValid
  }
}
```

### Error Handling Patterns

**CUSTOM ERROR TYPES:**

```typescript
// ✅ Good - Domain-specific error classes
export class ValidationError extends Error {
  constructor(
    message: string,
    public readonly field: string,
    public readonly code: string
  ) {
    super(message)
    this.name = 'ValidationError'
  }
}

export class ApiError extends Error {
  constructor(
    message: string,
    public readonly status: number,
    public readonly endpoint: string
  ) {
    super(message)
    this.name = 'ApiError'
  }
}

// ✅ Good - Result type pattern
type Result<T, E extends Error = Error> = 
  | { success: true; data: T }
  | { success: false; error: E }

async function safeApiCall<T>(
  operation: () => Promise<T>
): Promise<Result<T, ApiError>> {
  try {
    const data = await operation()
    return { success: true, data }
  } catch (error) {
    if (error instanceof ApiError) {
      return { success: false, error }
    }
    return { 
      success: false, 
      error: new ApiError('Unknown error', 500, 'unknown') 
    }
  }
}
```

## 4. Advanced Type Patterns and Guards

### Discriminated Unions

```typescript
// ✅ Good - Discriminated union for state management
type LoadingState = 
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: unknown }
  | { status: 'error'; error: string }

// ✅ Good - Type guards for runtime checking
function isSuccessState(state: LoadingState): state is Extract<LoadingState, { status: 'success' }> {
  return state.status === 'success'
}

function isErrorState(state: LoadingState): state is Extract<LoadingState, { status: 'error' }> {
  return state.status === 'error'
}

// Usage with type narrowing
function handleState(state: LoadingState) {
  if (isSuccessState(state)) {
    // TypeScript knows state.data exists
    console.log(state.data)
  } else if (isErrorState(state)) {
    // TypeScript knows state.error exists
    console.error(state.error)
  }
}
```

### Advanced Type Validation

```typescript
// ✅ Good - Runtime type validation
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    'name' in value &&
    'email' in value &&
    typeof (value as any).id === 'string' &&
    typeof (value as any).name === 'string' &&
    typeof (value as any).email === 'string'
  )
}

// ✅ Good - Schema validation with libraries
import { z } from 'zod'

const UserSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1).max(100),
  email: z.string().email(),
  roles: z.array(z.enum(['admin', 'editor', 'viewer'])),
  createdAt: z.date(),
  updatedAt: z.date()
})

type User = z.infer<typeof UserSchema>

// Validation function
function validateUser(data: unknown): Result<User, ValidationError> {
  const result = UserSchema.safeParse(data)
  if (result.success) {
    return { success: true, data: result.data }
  }
  return { 
    success: false, 
    error: new ValidationError(
      result.error.message, 
      'user', 
      'VALIDATION_FAILED'
    ) 
  }
}
```

## 5. Class and Object-Oriented Patterns

### Class Design Standards

```typescript
// ✅ Good - Proper class structure with TypeScript
export class UserService {
  constructor(
    private readonly repository: Repository<User>,
    private readonly logger: Logger
  ) {}

  async createUser(userData: CreateUserRequest): Promise<User> {
    this.logger.info('Creating user', { userData })
    
    const validation = validateUser(userData)
    if (!validation.success) {
      throw validation.error
    }

    return this.repository.create({
      ...userData,
      id: crypto.randomUUID(),
      createdAt: new Date(),
      updatedAt: new Date()
    })
  }

  async findUser(id: string): Promise<User | null> {
    if (!id) {
      throw new ValidationError('User ID is required', 'id', 'REQUIRED')
    }
    
    return this.repository.findById(id)
  }
}

// ✅ Good - Abstract base classes
abstract class BaseRepository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>
  abstract create(data: Omit<T, 'id'>): Promise<T>
  
  protected validateId(id: string): void {
    if (!id || typeof id !== 'string') {
      throw new ValidationError('Invalid ID format', 'id', 'INVALID_FORMAT')
    }
  }
}
```

### Interface Segregation

```typescript
// ✅ Good - Small, focused interfaces
interface Readable<T> {
  read(id: string): Promise<T | null>
}

interface Writable<T> {
  write(data: T): Promise<T>
}

interface Deletable {
  delete(id: string): Promise<void>
}

// Compose interfaces as needed
interface Repository<T> extends Readable<T>, Writable<T>, Deletable {}

interface ReadOnlyRepository<T> extends Readable<T> {}
```

## 6. Async/Await and Promise Patterns

### Modern Async Patterns

```typescript
// ✅ Good - Proper async/await with error handling
export class ApiClient {
  private readonly baseURL: string
  private readonly timeout: number = 5000

  constructor(baseURL: string) {
    this.baseURL = baseURL
  }

  async get<T>(endpoint: string): Promise<ApiResponse<T>> {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), this.timeout)

    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })

      clearTimeout(timeoutId)

      if (!response.ok) {
        throw new ApiError(
          `HTTP ${response.status}: ${response.statusText}`,
          response.status,
          endpoint
        )
      }

      const data = await response.json() as ApiResponse<T>
      return data
    } catch (error) {
      clearTimeout(timeoutId)
      
      if (error instanceof ApiError) {
        throw error
      }
      
      if (error.name === 'AbortError') {
        throw new ApiError('Request timeout', 408, endpoint)
      }
      
      throw new ApiError('Network error', 0, endpoint)
    }
  }

  // ✅ Good - Parallel async operations
  async getUserWithProfile(userId: string): Promise<UserWithProfile> {
    const [user, profile] = await Promise.all([
      this.get<User>(`/users/${userId}`),
      this.get<Profile>(`/users/${userId}/profile`)
    ])

    return {
      ...user.data,
      profile: profile.data
    }
  }

  // ✅ Good - Sequential async with proper error handling
  async createUserWithProfile(
    userData: CreateUserRequest,
    profileData: CreateProfileRequest
  ): Promise<UserWithProfile> {
    const userResult = await this.post<User>('/users', userData)
    
    try {
      const profileResult = await this.post<Profile>(
        `/users/${userResult.data.id}/profile`, 
        profileData
      )
      
      return {
        ...userResult.data,
        profile: profileResult.data
      }
    } catch (error) {
      // Cleanup: delete the created user if profile creation fails
      await this.delete(`/users/${userResult.data.id}`).catch(() => {
        // Log cleanup failure but don't throw
        console.error('Failed to cleanup user after profile creation error')
      })
      
      throw error
    }
  }
}
```

## 7. Testing Strategies

### Unit Testing Patterns

```typescript
// ✅ Good - Comprehensive test types
import { describe, it, expect, vi, beforeEach } from 'vitest'
import type { MockedFunction } from 'vitest'

interface MockRepository extends Repository<User> {
  findById: MockedFunction<Repository<User>['findById']>
  create: MockedFunction<Repository<User>['create']>
}

describe('UserService', () => {
  let userService: UserService
  let mockRepository: MockRepository
  let mockLogger: Logger

  beforeEach(() => {
    mockRepository = {
      findById: vi.fn(),
      create: vi.fn(),
      delete: vi.fn()
    }
    
    mockLogger = {
      info: vi.fn(),
      error: vi.fn(),
      warn: vi.fn()
    }
    
    userService = new UserService(mockRepository, mockLogger)
  })

  describe('createUser', () => {
    it('should create user with valid data', async () => {
      const userData: CreateUserRequest = {
        name: 'John Doe',
        email: 'john@example.com'
      }
      
      const expectedUser: User = {
        id: expect.any(String),
        ...userData,
        roles: [],
        createdAt: expect.any(Date),
        updatedAt: expect.any(Date)
      }
      
      mockRepository.create.mockResolvedValue(expectedUser)
      
      const result = await userService.createUser(userData)
      
      expect(result).toEqual(expectedUser)
      expect(mockRepository.create).toHaveBeenCalledWith(
        expect.objectContaining(userData)
      )
    })

    it('should throw ValidationError for invalid data', async () => {
      const invalidData = { name: '', email: 'invalid-email' }
      
      await expect(userService.createUser(invalidData))
        .rejects
        .toThrow(ValidationError)
    })
  })
})
```

### Type Testing

```typescript
// ✅ Good - Type-level testing
type AssertEqual<T, U> = T extends U ? (U extends T ? true : false) : false
type Assert<T extends true> = T

// Test type utilities
type _TestUserWithoutDates = Assert<
  AssertEqual<UserWithoutDates, Omit<User, 'createdAt' | 'updatedAt'>>
>

type _TestPartialUser = Assert<
  AssertEqual<PartialUser, Partial<Pick<User, 'name' | 'email'>>>
>

// Test discriminated unions
type _TestLoadingState = Assert<
  AssertEqual<
    Extract<LoadingState, { status: 'success' }>['data'],
    unknown
  >
>
```

## 8. Performance and Optimization

### Type-Level Performance

```typescript
// ✅ Good - Efficient type operations
// Use mapped types instead of intersection for better performance
type OptimizedUpdate<T> = {
  [K in keyof T]?: T[K]
}

// ❌ Bad - Expensive type operations
type ExpensiveType<T> = T extends any[] 
  ? T[number] extends infer U 
    ? U extends object 
      ? { [K in keyof U]: ExpensiveType<U[K]> }
      : U
    : never
  : T

// ✅ Good - Lazy evaluation with conditional types
type LazyEvaluation<T> = T extends infer U ? ProcessType<U> : never
```

### Runtime Performance

```typescript
// ✅ Good - Efficient type guards
const isString = (value: unknown): value is string => 
  typeof value === 'string'

const isArrayOf = <T>(
  value: unknown, 
  guard: (item: unknown) => item is T
): value is T[] => 
  Array.isArray(value) && value.every(guard)

// ✅ Good - Memoized computed types
const memoizedValidator = memoize((schema: string) => {
  return createValidator(schema)
})
```

## 9. Configuration and Tooling

### TSConfig Standards

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "skipLibCheck": false,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "removeComments": false,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/types": ["src/types"],
      "@/utils": ["src/utils"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

### ESLint TypeScript Rules

```json
{
  "extends": [
    "@typescript-eslint/recommended",
    "@typescript-eslint/recommended-requiring-type-checking"
  ],
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/prefer-readonly": "warn",
    "@typescript-eslint/prefer-nullish-coalescing": "error",
    "@typescript-eslint/prefer-optional-chain": "error"
  }
}
```

## 10. AI-Specific Guidelines

### Code Generation Requirements

**WHEN GENERATING TYPESCRIPT CODE:**

- Always include explicit return types for public functions
- Use strict type checking (no `any` types)
- Include comprehensive error handling with custom error types
- Generate accompanying unit tests with proper type mocking
- Add JSDoc comments for complex type definitions
- Follow consistent naming conventions throughout

### Quality Assurance Checklist

**PRE-SUBMISSION VALIDATION:**

- [ ] TypeScript compilation passes with zero errors
- [ ] All functions have explicit return types
- [ ] No `any` types used (prefer `unknown`)
- [ ] Error handling includes custom error types
- [ ] Unit tests cover all public methods
- [ ] Type guards used for runtime validation
- [ ] Performance considerations addressed
- [ ] Security vulnerabilities checked

### Common TypeScript Anti-Patterns to Avoid

**NEVER DO:**

- Use `any` type in production code
- Ignore TypeScript compiler errors
- Use type assertions without proper validation
- Create overly complex type definitions that hurt performance
- Mix JavaScript patterns with TypeScript without proper typing
- Forget to handle Promise rejections in async functions
- Use `Function` type instead of proper function signatures

**ALWAYS DO:**

- Leverage TypeScript's type system for compile-time safety
- Use discriminated unions for complex state management
- Implement proper error boundaries with typed error handling
- Create reusable type utilities for common patterns
- Use generics to create flexible, type-safe APIs
- Write type guards for runtime type validation
