# FSD Principle

> **Magic Vibe Rule: Feature-Sliced Design Architecture**  
> **Category:** Principles  
> **Priority:** High  
> **File Size:** ~9KB (AI-optimized)  
> **Dependencies:** `@rules/principles/solid.md`, `@rules/principles/dry.md`

Feature-Sliced Design (FSD) architectural methodology for building scalable frontend applications. Organizes code by business features with strict layer hierarchy and AI-optimized validation patterns.

## 1. Implementation Guidelines

### 1.1. Layer Hierarchy (Top → Bottom)

**6-Layer Structure:**

1. **App** - Application initialization, routing, global providers
2. **Pages** - Complete page components and routing logic
3. **Widgets** - Large UI blocks delivering complete use cases
4. **Features** - Reusable business feature implementations
5. **Entities** - Business domain models and logic
6. **Shared** - Reusable utilities and common components

```text
src/
├── app/           # Application layer
│   ├── providers/ # Global providers
│   └── router/    # Routing configuration
├── pages/         # Pages layer
│   └── home/      # Page slice
│       ├── ui/    # Page UI components
│       └── model/ # Page state logic
├── widgets/       # Widgets layer
│   └── header/    # Widget slice
│       ├── ui/    # Widget UI
│       └── model/ # Widget logic
├── features/      # Features layer
│   └── auth/      # Feature slice
│       ├── ui/    # Feature UI
│       ├── model/ # Feature logic
│       └── api/   # Feature API
├── entities/      # Entities layer
│   └── user/      # Entity slice
│       ├── ui/    # Entity UI components
│       ├── model/ # Entity state/logic
│       └── api/   # Entity API
└── shared/        # Shared layer
    ├── ui/        # Shared UI components
    ├── api/       # Shared API utilities
    └── lib/       # Shared libraries
```

### 1.2. Import Rules (Critical)

**Layer Dependency Rule:** Higher layers can ONLY import from lower layers.

```typescript
// ✅ Valid imports (top → bottom flow)
// In pages/home/ui/HomePage.tsx
import { LoginForm } from "features/auth/ui";        // Pages → Features
import { UserCard } from "entities/user/ui";         // Pages → Entities
import { Button } from "shared/ui/button";           // Pages → Shared

// ❌ Invalid imports (violate hierarchy)
// In features/auth/ui/LoginForm.tsx
import { HomePage } from "pages/home/ui";            // Features → Pages
import { Header } from "widgets/header/ui";          // Features → Widgets
import { PostForm } from "features/posts/ui";        // Feature → Feature
```

### 1.3. Segment Standards

**Required Segments:**

- **ui/** - UI components and visual presentation
- **model/** - Business logic, state management, types
- **api/** - Backend interactions and data fetching
- **lib/** - Slice-specific utilities
- **config/** - Configuration and feature flags

```typescript
// Entity structure example: entities/user/
export { UserCard, UserAvatar } from "./ui";
export { userModel, type User } from "./model";
export { userAPI } from "./api";
```

## 2. Change Management Protocols

### 2.1. Migration Strategy

**Incremental FSD Migration:**

1. **Foundation** (Week 1): Create `shared/` and `app/` layers
2. **Distribution** (Week 2-3): Move UI to `pages/` and `widgets/`
3. **Extraction** (Week 4+): Extract `entities/` and `features/`

```typescript
// Before: Mixed concerns
const UserProfile = () => {
  const [user, setUser] = useState(null);
  const fetchUser = async (id) => { /* API */ };
  return <div>{/* Complex UI */}</div>;
};

// After: FSD-compliant
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
```

### 2.2. Validation Metrics

**Compliance Targets:**

- **Layer Compliance**: 100% of imports follow hierarchy
- **Slice Independence**: 0 same-layer imports
- **File Size**: Max 300 lines per file
- **Function Size**: Max 20 lines per function

## 3. Communication Standards

### 3.1. Naming Conventions

```typescript
// Layer naming (lowercase, kebab-case)
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

## 4. Quality Assurance Framework

### 4.1. ESLint Configuration

```javascript
// .eslintrc.js - FSD compliance rules
module.exports = {
  extends: ["@typescript-eslint/recommended"],
  plugins: ["boundaries"],
  settings: {
    "boundaries/elements": [
      { "type": "app", "pattern": "src/app/**/*" },
      { "type": "pages", "pattern": "src/pages/**/*" },
      { "type": "widgets", "pattern": "src/widgets/**/*" },
      { "type": "features", "pattern": "src/features/**/*" },
      { "type": "entities", "pattern": "src/entities/**/*" },
      { "type": "shared", "pattern": "src/shared/**/*" }
    ]
  },
  rules: {
    "boundaries/element-types": ["error", {
      "default": "disallow",
      "rules": [
        { "from": ["app"], "allow": ["pages", "widgets", "features", "entities", "shared"] },
        { "from": ["pages"], "allow": ["widgets", "features", "entities", "shared"] },
        { "from": ["widgets"], "allow": ["features", "entities", "shared"] },
        { "from": ["features"], "allow": ["entities", "shared"] },
        { "from": ["entities"], "allow": ["shared"] },
        { "from": ["shared"], "allow": [] }
      ]
    }]
  }
};
```

## 5. Security & Performance Guidelines

### 5.1. Security Implementation

```typescript
// shared/api/baseAPI.ts
export const secureAPI = {
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
const AuthFeature = lazy(() => import("features/auth"));

// Code splitting at feature level
const UserWidget = lazy(() => import("widgets/user-profile"));

// Shared performance utilities
// shared/lib/performance.ts
export const debounce = (fn, delay) => { /* implementation */ };
export const memoize = (fn) => { /* implementation */ };
```

## 6. Integration & Compatibility

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

## 7. Monitoring & Maintenance

### 7.1. Architecture Evolution Tracking

```text
# .fsd/migration-log.md
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

### 7.2. Maintenance Guidelines

**Regular Reviews:**

- Weekly FSD compliance assessment
- Monthly architecture health checks
- Quarterly refactoring planning
- Tool updates and best practice reviews

## 8. AI Agent Optimization

### 8.1. AI-Assisted Code Generation

**AI Prompt Template:**

"Generate a feature slice for user authentication following FSD architecture.
Include `ui/`, `model/`, and `api/` segments with proper TypeScript types.
Ensure imports only reference `entities/` and `shared/` layers."

Expected output structure:

```text
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

### 8.2. AI Validation Rules

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

### 8.3. Quick Reference

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

---

**Magic Vibe FSD Principles v2.1.0** - Scalable frontend architecture

*Last Updated: 2025-01-XX | File Size: ~9KB | Status: Active*
