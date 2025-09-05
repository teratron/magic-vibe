# Feature-Sliced Design Example

This example demonstrates a typical FSD project structure for an e-commerce application.

## Project Structure

```
src/
├── app/                           # Application layer
│   ├── providers/                # Global providers (theme, auth, etc.)
│   │   ├── with-router.tsx
│   │   ├── with-store.tsx
│   │   └── index.ts
│   ├── styles/                   # Global styles
│   │   ├── globals.css
│   │   └── reset.css
│   └── main.tsx                  # Application entry point
│
├── pages/                        # Pages layer
│   ├── home/                     # Home page slice
│   │   ├── ui/
│   │   │   ├── HomePage.tsx
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── product-catalog/          # Product catalog page slice
│   │   ├── ui/
│   │   │   ├── ProductCatalogPage.tsx
│   │   │   ├── ProductGrid.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── useProductCatalog.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   └── checkout/                 # Checkout page slice
│       ├── ui/
│       │   ├── CheckoutPage.tsx
│       │   └── index.ts
│       ├── model/
│       │   ├── checkoutStore.ts
│       │   └── index.ts
│       └── index.ts
│
├── widgets/                      # Widgets layer
│   ├── header/                   # Header widget slice
│   │   ├── ui/
│   │   │   ├── Header.tsx
│   │   │   ├── Navigation.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── navigationModel.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── product-card/             # Product card widget slice
│   │   ├── ui/
│   │   │   ├── ProductCard.tsx
│   │   │   ├── ProductImage.tsx
│   │   │   └── index.ts
│   │   └── index.ts
│   └── shopping-cart/            # Shopping cart widget slice
│       ├── ui/
│       │   ├── ShoppingCart.tsx
│       │   ├── CartItem.tsx
│       │   └── index.ts
│       ├── model/
│       │   ├── cartStore.ts
│       │   └── index.ts
│       └── index.ts
│
├── features/                     # Features layer
│   ├── auth/                     # Authentication feature slice
│   │   ├── ui/
│   │   │   ├── LoginForm.tsx
│   │   │   ├── SignupForm.tsx
│   │   │   ├── LogoutButton.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── authStore.ts
│   │   │   ├── authTypes.ts
│   │   │   └── index.ts
│   │   ├── api/
│   │   │   ├── authAPI.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── add-to-cart/              # Add to cart feature slice
│   │   ├── ui/
│   │   │   ├── AddToCartButton.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── addToCartModel.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   └── product-search/           # Product search feature slice
│       ├── ui/
│       │   ├── SearchBar.tsx
│       │   ├── SearchResults.tsx
│       │   └── index.ts
│       ├── model/
│       │   ├── searchStore.ts
│       │   └── index.ts
│       ├── api/
│       │   ├── searchAPI.ts
│       │   └── index.ts
│       └── index.ts
│
├── entities/                     # Entities layer
│   ├── user/                     # User entity slice
│   │   ├── ui/
│   │   │   ├── UserAvatar.tsx
│   │   │   ├── UserProfile.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── userTypes.ts
│   │   │   ├── userStore.ts
│   │   │   └── index.ts
│   │   ├── api/
│   │   │   ├── userAPI.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── product/                  # Product entity slice
│   │   ├── ui/
│   │   │   ├── ProductInfo.tsx
│   │   │   ├── ProductPrice.tsx
│   │   │   └── index.ts
│   │   ├── model/
│   │   │   ├── productTypes.ts
│   │   │   ├── productHelpers.ts
│   │   │   └── index.ts
│   │   ├── api/
│   │   │   ├── productAPI.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   └── order/                    # Order entity slice
│       ├── ui/
│       │   ├── OrderSummary.tsx
│       │   ├── OrderStatus.tsx
│       │   └── index.ts
│       ├── model/
│       │   ├── orderTypes.ts
│       │   ├── orderHelpers.ts
│       │   └── index.ts
│       ├── api/
│       │   ├── orderAPI.ts
│       │   └── index.ts
│       └── index.ts
│
└── shared/                       # Shared layer
    ├── ui/                       # Shared UI components
    │   ├── button/
    │   │   ├── Button.tsx
    │   │   ├── Button.module.css
    │   │   └── index.ts
    │   ├── input/
    │   │   ├── Input.tsx
    │   │   ├── Input.module.css
    │   │   └── index.ts
    │   ├── modal/
    │   │   ├── Modal.tsx
    │   │   ├── Modal.module.css
    │   │   └── index.ts
    │   └── index.ts
    ├── api/                      # Shared API utilities
    │   ├── base.ts              # Base API configuration
    │   ├── types.ts             # Common API types
    │   ├── interceptors.ts      # Request/response interceptors
    │   └── index.ts
    ├── lib/                      # Shared libraries
    │   ├── hooks/               # Custom React hooks
    │   │   ├── useLocalStorage.ts
    │   │   ├── useDebounce.ts
    │   │   └── index.ts
    │   ├── utils/               # Utility functions
    │   │   ├── formatters.ts
    │   │   ├── validators.ts
    │   │   └── index.ts
    │   ├── constants/           # Application constants
    │   │   ├── routes.ts
    │   │   ├── api-endpoints.ts
    │   │   └── index.ts
    │   └── index.ts
    └── config/                   # Configuration
        ├── env.ts               # Environment variables
        ├── theme.ts             # Theme configuration
        └── index.ts
```

## Import Examples

### Valid Imports (Following FSD Hierarchy)

```typescript
// ✅ pages/home/ui/HomePage.tsx
import { Header } from "widgets/header";           // Pages → Widgets
import { ProductSearch } from "features/product-search"; // Pages → Features  
import { UserProfile } from "entities/user";       // Pages → Entities
import { Button } from "shared/ui";                // Pages → Shared

// ✅ features/auth/ui/LoginForm.tsx  
import { User } from "entities/user";              // Features → Entities
import { Input, Button } from "shared/ui";         // Features → Shared
import { authAPI } from "../api";                  // Same slice import

// ✅ entities/user/model/userStore.ts
import { apiClient } from "shared/api";            // Entities → Shared
import { User } from "./userTypes";                // Same slice import
```

### Invalid Imports (Violating FSD Rules)

```typescript
// ❌ features/auth/ui/LoginForm.tsx
import { HomePage } from "pages/home";             // Features → Pages (forbidden)
import { Header } from "widgets/header";           // Features → Widgets (forbidden)
import { ProductSearch } from "features/product-search"; // Feature → Feature (forbidden)

// ❌ entities/user/model/userStore.ts  
import { LoginForm } from "features/auth";         // Entities → Features (forbidden)
import { Header } from "widgets/header";           // Entities → Widgets (forbidden)

// ❌ shared/api/base.ts
import { User } from "entities/user";              // Shared → Entities (forbidden)
import { authAPI } from "features/auth";           // Shared → Features (forbidden)
```

## Validation Commands

Run FSD compliance validation:

```bash
# Using bash script (Linux/Mac)
./validate-fsd.sh

# Using PowerShell script (Windows)
.\validate-fsd.ps1

# With verbose output
.\validate-fsd.ps1 -Verbose

# Check specific project directory  
.\validate-fsd.ps1 -ProjectPath "./my-project"
```

## AI Agent Integration

When working with FSD projects, AI agents should:

1. **Detect FSD Structure**: Recognize src/ directory with FSD layers
2. **Enforce Import Rules**: Validate imports follow layer hierarchy
3. **Suggest Correct Layer**: Recommend appropriate layer for new code
4. **Generate Compliant Code**: Create code following FSD patterns
5. **Validate Architecture**: Check compliance using validation scripts

## Benefits of This Structure

- **Scalability**: Easy to add new features without affecting existing code
- **Maintainability**: Clear separation of concerns and dependencies
- **Team Collaboration**: Standardized structure improves onboarding
- **Code Reusability**: Shared components and utilities are easily accessible
- **Business Alignment**: Feature-based organization matches business requirements