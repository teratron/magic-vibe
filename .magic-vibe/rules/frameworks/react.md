---
description: Actionable rules and best practices for building modern, performant, and maintainable React applications.
globs:
  - "src/**/*.{js,jsx,ts,tsx}"
---

# React Coding Style Guide

This guide provides actionable rules for writing clean, efficient, and maintainable React code. Follow these guidelines to ensure consistency and high quality in your components and applications.

## 1. Component Design

### 1.1. Use Functional Components with Hooks

Always prefer functional components with Hooks over class components. They are more concise, easier to read, and promote better code reuse.

```tsx
// Good: Functional component
import React, { useState } from 'react';

interface GreetingProps {
  name: string;
}

const Greeting: React.FC<GreetingProps> = ({ name }) => {
  const [greeting, setGreeting] = useState(`Hello, ${name}`);

  return <div>{greeting}</div>;
};

// Bad: Class component
import React, { Component } from 'react';

class Greeting extends Component<{ name: string }, { greeting: string }> {
  constructor(props) {
    super(props);
    this.state = { greeting: `Hello, ${props.name}` };
  }

  render() {
    return <div>{this.state.greeting}</div>;
  }
}
```

### 1.2. Keep Components Small and Focused (Single Responsibility Principle)

Each component should have a single responsibility. If a component does too much, break it down into smaller, more manageable components.

```tsx
// Good: Small, focused components
const UserProfile = ({ user }) => (
  <div>
    <UserAvatar src={user.avatarUrl} />
    <UserInfo name={user.name} bio={user.bio} />
  </div>
);

// Bad: Monolithic component
const UserProfile = ({ user }) => (
  <div>
    <img src={user.avatarUrl} alt={user.name} className="avatar" />
    <h2>{user.name}</h2>
    <p>{user.bio}</p>
    {/* ...more logic and rendering */}
  </div>
);
```

### 1.3. Use TypeScript for Prop Types

Define component props using TypeScript interfaces for type safety and better developer experience.

```tsx
// Good: Using a TypeScript interface for props
interface UserAvatarProps {
  src: string;
  alt: string;
  size?: number;
}

const UserAvatar: React.FC<UserAvatarProps> = ({ src, alt, size = 50 }) => (
  <img src={src} alt={alt} width={size} height={size} />
);
```

## 2. Hooks

### 2.1. Follow the Rules of Hooks

- Only call Hooks at the top level.
- Only call Hooks from React function components or custom Hooks.

### 2.2. Extract Reusable Logic into Custom Hooks

If you find yourself repeating logic across multiple components (e.g., data fetching, subscriptions), extract it into a custom hook.

```tsx
// Good: Custom hook for data fetching
const useUserData = (userId: string) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data))
      .finally(() => setLoading(false));
  }, [userId]);

  return { user, loading };
};

// Usage in a component
const UserPage = ({ userId }) => {
  const { user, loading } = useUserData(userId);
  if (loading) return <div>Loading...</div>;
  return <UserProfile user={user} />;
};
```

### 2.3. Specify Correct Dependency Arrays

Always provide a dependency array to `useEffect`, `useCallback`, and `useMemo`. Include all values from the component scope that are used inside the hook.

```tsx
// Good: Correct dependency array
useEffect(() => {
  document.title = `User: ${userName}`;
}, [userName]);

// Bad: Missing dependency array, will run on every render
useEffect(() => {
  document.title = `User: ${userName}`;
});
```

## 3. State Management

### 3.1. Choose the Right State Management Tool

- **`useState`**: For simple, local component state.
- **`useReducer`**: For complex state logic within a single component or a small group of related components.
- **`Context API`**: For sharing state that is considered "global" for a tree of React components, like theme or user authentication.
- **External Libraries (Redux, Zustand)**: For complex, application-wide state that is accessed and modified by many components. Only use when necessary.

### 3.2. Avoid Prop Drilling

If you are passing props down through many levels of components, consider using the Context API or a state management library.

```tsx
// Good: Using Context to avoid prop drilling
const ThemeContext = React.createContext('light');

const App = () => (
  <ThemeContext.Provider value="dark">
    <Toolbar />
  </ThemeContext.Provider>
);

const Toolbar = () => <ThemedButton />;

const ThemedButton = () => {
  const theme = useContext(ThemeContext);
  return <button className={`theme-${theme}`}>Click Me</button>;
};
```

## 4. Performance

### 4.1. Memoize Expensive Computations and Components

- **`useMemo`**: Memoize the result of an expensive calculation.
- **`useCallback`**: Memoize a function definition so it isn't recreated on every render.
- **`React.memo`**: Prevent a component from re-rendering if its props have not changed.

```tsx
// Good: Using useMemo and React.memo
const SortedList = React.memo(({ items }) => {
  const sortedItems = useMemo(() => {
    console.log('Sorting items...');
    return [...items].sort();
  }, [items]);

  return <ul>{sortedItems.map(item => <li key={item}>{item}</li>)}</ul>;
});
```

### 4.2. Use `key` Props Correctly in Lists

Use a stable and unique identifier for the `key` prop when rendering lists. Avoid using the array index as a key, especially for dynamic lists.

```tsx
// Good: Using a stable ID as a key
users.map((user) => <User key={user.id} user={user} />);

// Bad: Using the array index as a key
users.map((user, index) => <User key={index} user={user} />);
```

## 5. Code Organization

### 5.1. Structure Files by Feature or Component

Group related files together. For example, a `UserProfile` component might have its own directory with the component file, styles, and tests.

```text
/components
  /UserProfile
    - UserProfile.tsx
    - UserProfile.module.css
    - UserProfile.test.tsx
    - index.ts (exports UserProfile)
```

### 5.2. Use Absolute Imports

Configure absolute imports in your `tsconfig.json` or `jsconfig.json` to avoid long relative paths.

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": "src"
  }
}
```

```tsx
// Good: Absolute import
import { UserProfile } from 'components/UserProfile';

// Bad: Relative import
import { UserProfile } from '../../../../components/UserProfile';
```
