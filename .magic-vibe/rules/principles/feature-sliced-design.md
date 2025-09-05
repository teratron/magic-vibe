---
description: Feature-Sliced Design (FSD) architectural methodology for building scalable and maintainable frontend applications with AI-optimized guidelines.
globs:
  - "src/**/*"
  - "app/**/*"
  - "pages/**/*"
  - "shared/**/*"
  - "entities/**/*"
  - "features/**/*"
  - "widgets/**/*"
alwaysApply: false
---

# Feature-Sliced Design (FSD) Architecture Guide

Feature-Sliced Design (FSD) is an architectural methodology for scaffolding frontend applications that organizes code by business features rather than technical layers. This guide provides AI-optimized rules for implementing FSD architecture with measurable standards and automated validation.

## 1. Code Generation Standards

### 1.1. Layer Structure Requirements

Follow the standardized 7-layer hierarchy (top to bottom):

1. **App** - Application initialization, routing, global providers
2. **Pages** - Complete page components and routing logic
3. **Widgets** - Large UI blocks delivering complete use cases
4. **Features** - Reusable business feature implementations
5. **Entities** - Business domain models and logic
6. **Shared** - Reusable utilities and common components

```text
src/
├── app/                    # Application layer
│   ├── providers/         # Global providers
│   ├── router/           # Routing configuration
│   └── styles/           # Global styles
├── pages/                 # Pages layer
│   ├── home/             # Page slice
│   │   ├── ui/           # Page UI components
│   │   └── model/        # Page state logic
│   └── profile/          # Another page slice
├── widgets/              # Widgets layer
│   ├── header/           # Widget slice
│   │   ├── ui/           # Widget UI
│   │   ├── model/        # Widget logic
│   │   └── api/          # Widget API calls
├── features/             # Features layer
│   ├── auth/             # Feature slice
│   │   ├── ui/           # Feature UI
│   │   ├── model/        # Feature logic
│   │   └── api/          # Feature API
├── entities/             # Entities layer
│   ├── user/             # Entity slice
│   │   ├── ui/           # Entity UI components
│   │   ├── model/        # Entity state/logic
│   │   └── api/          # Entity API
└── shared/               # Shared layer
    ├── ui/               # Shared UI components
    ├── api/              # Shared API utilities
    ├── lib/              # Shared libraries
    └── config/           # Configuration
```

### 1.2. Import Rules and Dependencies

**Critical Rule**: Higher layers can only import from lower layers.

```typescript
// ✅ Valid imports (top to bottom flow)
// In pages/home/ui/HomePage.tsx
import { LoginForm } from "features/auth/ui";        // Pages → Features
import { UserCard } from "entities/user/ui";         // Pages → Entities
import { Button } from "shared/ui/button";           // Pages → Shared

// ❌ Invalid imports (violate hierarchy)
// In features/auth/ui/LoginForm.tsx
import { HomePage } from "pages/home/ui";            // Features → Pages (forbidden)
import { Header } from "widgets/header/ui";          // Features → Widgets (forbidden)

// ❌ Invalid same-layer imports
// In features/auth/ui/LoginForm.tsx
import { PostForm } from "features/posts/ui";        // Feature → Feature (forbidden)
```

### 1.3. Segment Organization Standards

Each slice contains standardized segments:

- **ui/** - UI components and visual presentation
- **model/** - Business logic, state management, types
- **api/** - Backend interactions and data fetching
- **lib/** - Slice-specific utilities and helpers
- **config/** - Configuration and feature flags

```typescript
// Entity structure example: entities/user/
export { UserCard, UserAvatar } from "./ui";
export { userModel, type User } from "./model";
export { userAPI } from "./api";
```

## 2. Change Management Protocols

### 2.1. Incremental Migration Strategy

For existing codebases, follow this AI-guided migration sequence:

1. **Foundation Setup** (Priority 1):
   - Create `shared/` and `app/` layers first
   - Move common utilities to `shared/lib/`
   - Establish global providers in `app/providers/`

2. **UI Distribution** (Priority 2):
   - Distribute existing UI between `pages/` and `widgets/`
   - Accept temporary import violations during this phase
   - Focus on logical grouping over perfect compliance

3. **Domain Extraction** (Priority 3):
   - Extract business entities to `entities/` layer
   - Create reusable features in `features/` layer
   - Resolve import violations systematically

### 2.2. Refactoring Guidelines

When refactoring code to FSD:

```typescript
// Before: Mixed concerns in single file
// src/components/UserProfile.tsx
const UserProfile = () => {
  const [user, setUser] = useState(null);
  const fetchUser = async (id) => { /* API call */ };
  return <div>{/* Complex UI */}</div>;
};

// After: FSD-compliant structure
// entities/user/model/userModel.ts
export const userModel = {
  state: atom(null),
  fetchUser: async (id) => { /* API logic */ }
};

// entities/user/ui/UserProfile.tsx
export const UserProfile = () => {
  const user = useAtom(userModel.state);
  return <div>{/* Focused UI */}</div>;
};

// features/user-management/ui/UserProfilePage.tsx
export const UserProfilePage = () => {
  return (
    <div>
      <UserProfile />
      <UserActions />
    </div>
  );
};
```

### 2.3. Validation Metrics

- **Layer Compliance**: 100% of imports must follow layer hierarchy
- **Slice Independence**: 0 same-layer imports between slices
- **File Size Limits**: Maximum 300 lines per file
- **Function Complexity**: Maximum 20 lines per function

## 3. Communication Standards

### 3.1. Naming Conventions

Follow FSD naming standards for clarity:

```typescript
// Layer naming (lowercase, kebab-case for folders)
src/pages/user-profile/
src/features/post-creation/
src/entities/blog-post/

// Slice naming (business domain focused)
entities/user/          # Not entities/user-data/
features/auth/          # Not features/authentication-flow/
widgets/sidebar/        # Not widgets/left-panel/

// Segment naming (standardized)
ui/                     # Never views/, components/
model/                  # Never store/, state/
api/                    # Never services/, requests/
```

### 3.2. Documentation Requirements

Each slice must include:

```typescript
// entities/user/index.ts
/**
 * User entity - manages user data and operations
 * 
 * Public API:
 * - UserCard: Display user information
 * - UserAvatar: User profile picture component
 * - userModel: User state management
 * - userAPI: User data fetching operations
 * 
 * Dependencies: shared/ui, shared/api
 * Used by: features/auth, widgets/header, pages/profile
 */
export { UserCard, UserAvatar } from "./ui";
export { userModel } from "./model";
export { userAPI } from "./api";
```

### 3.3. Team Communication Protocols

- **Architecture Decisions**: Document layer violations and resolutions
- **Code Reviews**: Validate FSD compliance using automated tools
- **Onboarding**: Use FSD terminology in discussions and documentation

## 4. Quality Assurance Framework

### 4.1. Automated Validation Rules

Implement ESLint rules for FSD compliance:

```javascript
// .eslintrc.js
module.exports = {
  rules: {
    "boundaries/element-types": [2, {
      default: "disallow",
      rules: [
        { from: "app", allow: ["pages", "widgets", "features", "entities", "shared"] },
        { from: "pages", allow: ["widgets", "features", "entities", "shared"] },
        { from: "widgets", allow: ["features", "entities", "shared"] },
        { from: "features", allow: ["entities", "shared"] },
        { from: "entities", allow: ["shared"] },
        { from: "shared", allow: [] }
      ]
    }]
  }
};
```

### 4.2. Testing Standards

Structure tests following FSD layers:

```typescript
// features/auth/__tests__/auth.test.ts
describe("Auth Feature", () => {
  test("login flow integration", () => {
    // Test complete feature functionality
  });
});

// entities/user/__tests__/userModel.test.ts
describe("User Entity Model", () => {
  test("user state updates", () => {
    // Test entity business logic
  });
});
```

### 4.3. Code Quality Metrics

- **Cohesion Score**: Measure related functionality grouping within slices
- **Coupling Score**: Measure dependencies between layers
- **Business Alignment**: Validate slice names match domain terminology
- **Test Coverage**: Minimum 90% coverage per slice

## 5. Security & Performance Guidelines

### 5.1. Security Considerations

```typescript
// shared/api/baseAPI.ts
export const secureAPI = {
  // Centralized security configuration
  baseURL: process.env.API_URL,
  withCredentials: true,
  validateResponse: (response) => {
    // Response validation logic
  }
};

// features/auth/api/authAPI.ts
import { secureAPI } from "shared/api";

export const authAPI = {
  login: (credentials) => 
    secureAPI.post("/auth/login", sanitizeInput(credentials))
};
```

### 5.2. Performance Optimization

```typescript
// Lazy loading by layers
const HomePage = lazy(() => import("pages/home"));
const UserWidget = lazy(() => import("widgets/user-profile"));

// Code splitting at feature level
const AuthFeature = lazy(() => import("features/auth"));

// Shared utilities for performance
// shared/lib/performance.ts
export const debounce = (fn, delay) => { /* implementation */ };
export const memoize = (fn) => { /* implementation */ };
```

### 5.3. Bundle Optimization

- **Layer-based Code Splitting**: Split bundles by FSD layers
- **Shared Dependencies**: Minimize duplicate code in shared layer
- **Dynamic Imports**: Use dynamic imports for large features/widgets
- **Performance Budget**: Maximum 250KB per layer bundle

## 6. Language-Specific Standards

### 6.1. TypeScript Integration

```typescript
// shared/types/index.ts
export interface BaseEntity {
  id: string;
  createdAt: Date;
  updatedAt: Date;
}

// entities/user/model/types.ts
import { BaseEntity } from "shared/types";

export interface User extends BaseEntity {
  name: string;
  email: string;
  role: UserRole;
}

// Type exports following FSD structure
export type { User, UserRole } from "./types";
```

### 6.2. React-Specific Patterns

```typescript
// features/auth/ui/LoginForm.tsx
import { useAuthModel } from "../model";
import { Button } from "shared/ui/button";

export const LoginForm = () => {
  const { login, isLoading } = useAuthModel();
  
  return (
    <form onSubmit={login}>
      <Button loading={isLoading}>Login</Button>
    </form>
  );
};

// features/auth/model/useAuthModel.ts
export const useAuthModel = () => {
  // Feature-specific state management
};
```

### 6.3. State Management Integration

```typescript
// entities/user/model/userStore.ts (Redux Toolkit)
export const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    setUser: (state, action) => {
      state.current = action.payload;
    }
  }
});

// features/auth/model/authModel.ts (Zustand)
export const useAuthStore = create((set) => ({
  isAuthenticated: false,
  login: () => set({ isAuthenticated: true })
}));
```

## 7. Continuous Improvement Protocols

### 7.1. Architecture Evolution

```typescript
// .fsd/migration-log.md
## Migration Progress
- ✅ App layer established
- ✅ Shared utilities moved
- 🟡 Pages layer in progress (60% complete)
- ❌ Features extraction pending
- ❌ Entities definition needed

## Import Violations
- pages/home → widgets/header (3 instances)
- features/auth → features/posts (1 instance)
```

### 7.2. Monitoring and Metrics

Track FSD compliance metrics:

```javascript
// scripts/fsd-metrics.js
const metrics = {
  layerCompliance: calculateLayerCompliance(),
  sliceIndependence: validateSliceImports(),
  businessAlignment: checkDomainNaming(),
  codeHealth: analyzeCodeQuality()
};
```

### 7.3. Refactoring Strategies

- **Weekly Reviews**: Assess FSD compliance in code reviews
- **Automated Checks**: Run architecture validation in CI/CD
- **Training Updates**: Keep team updated on FSD best practices
- **Tool Evolution**: Update tooling to support FSD patterns

## 8. AI-Specific Best Practices

### 8.1. AI-Assisted Code Generation

When generating FSD-compliant code:

```typescript
// AI Prompt Template:
// "Generate a feature slice for user authentication following FSD architecture.
// Include ui/, model/, and api/ segments with proper TypeScript types.
// Ensure imports only reference entities/ and shared/ layers."

// Expected output structure:
features/auth/
├── ui/
│   ├── LoginForm.tsx
│   ├── LogoutButton.tsx
│   └── index.ts
├── model/
│   ├── authStore.ts
│   ├── types.ts
│   └── index.ts
├── api/
│   ├── authAPI.ts
│   └── index.ts
└── index.ts
```

### 8.2. Automated Validation Integration

```typescript
// AI-readable validation config
export const fsdValidationRules = {
  maxFileLines: 300,
  maxFunctionLines: 20,
  requiredSegments: ["ui", "model"],
  optionalSegments: ["api", "lib", "config"],
  forbiddenImports: {
    "features/*": ["pages/*", "widgets/*", "features/*"],
    "entities/*": ["features/*", "widgets/*", "pages/*"],
    "shared/*": ["entities/*", "features/*", "widgets/*", "pages/*"]
  }
};
```

### 8.3. Context-Aware Code Suggestions

AI agents should consider:

- **Layer Context**: Suggest appropriate imports based on current layer
- **Business Domain**: Recommend slice names matching business terminology
- **Dependency Flow**: Validate import suggestions against FSD hierarchy
- **Pattern Recognition**: Identify common FSD patterns in existing code

```typescript
// AI Context Hints
/*
 * Current layer: features/
 * Available imports: entities/*, shared/*
 * Forbidden imports: pages/*, widgets/*, features/*
 * Suggested patterns: business logic in model/, UI in ui/
 */
```

### 8.4. Migration Assistance

AI-guided migration prompts:

```typescript
// Migration Helper Prompts
const migrationPrompts = {
  identifyLayer: "Analyze this component and suggest appropriate FSD layer placement",
  extractEntity: "Extract business logic into entities/ layer with proper segments",
  refactorFeature: "Refactor this functionality into a reusable feature slice",
  validateStructure: "Check FSD compliance and suggest improvements"
};
```

---

## Validation Checklist

- [ ] All imports follow layer hierarchy (top → bottom only)
- [ ] No same-layer imports between slices
- [ ] Segments use standardized names (ui, model, api, lib, config)
- [ ] Business domain terminology in slice names
- [ ] Maximum 300 lines per file
- [ ] Maximum 20 lines per function
- [ ] ESLint FSD rules configured and passing
- [ ] Test coverage ≥ 90% per slice
- [ ] Documentation includes public API and dependencies
- [ ] Performance budgets maintained per layer

## Quick Reference

**Layer Import Rules:**

- App → Pages, Widgets, Features, Entities, Shared ✅
- Pages → Widgets, Features, Entities, Shared ✅
- Widgets → Features, Entities, Shared ✅
- Features → Entities, Shared ✅
- Entities → Shared ✅
- Shared → (none) ✅

**Common Violations:**

- Features importing from Features ❌
- Entities importing from Features ❌
- Shared importing from any upper layer ❌
- Using non-standard segment names ❌
