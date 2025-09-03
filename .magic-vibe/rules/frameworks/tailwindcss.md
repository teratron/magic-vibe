---
description: Defines rules and best practices for using Tailwind CSS when writing HTML and components.
globs:
  - "**/*.{html,js,jsx,ts,tsx,vue,svelte}"
  - "tailwind.config.{js,ts}"
alwaysApply: false
---

# Tailwind CSS Usage Rules

This document contains a set of rules and recommendations for the AI agent on how to effectively use the Tailwind CSS framework. The goal is to create clean, maintainable, and consistent code.

When starting to work with files containing Tailwind classes, always begin your response with the phrase:

"Applying Tailwind CSS rules for quality code..."

## 1. Utility-First Philosophy

Always prefer using Tailwind's utility classes directly in the HTML markup instead of writing custom CSS.

- **INCORRECT (creating a custom class):**

  ```css
  .custom-button {
    background-color: #3b82f6;
    color: white;
    padding: 8px 16px;
    border-radius: 4px;
  }
  ```

  ```html
  <button class="custom-button">Click me</button>
  ```

- **CORRECT (composing utility classes):**

  ```html
  <button class="bg-blue-500 text-white font-bold py-2 px-4 rounded">
    Click me
  </button>
  ```

- **BEST PRACTICE (using `@apply` or `@extend`):**

  ```css
  /* Use @apply for complex styles that are reused */
  .custom-button {
    @apply bg-blue-500 text-white font-bold py-2 px-4 rounded;
  }
  ```

  ```scss
  /* Or use @extend for complex styles that are reused */
  .custom-button {
    @extend .bg-blue-500, .text-white, .font-bold, .py-2, .px-4, .rounded;
  }
  ```

  ```html
  <button class="custom-button">Click me</button>
  ```

## 2. Class Order

To improve readability and consistency, arrange classes in the following order, grouped by their purpose:

1. **Layout & Position**: `block`, `flex`, `grid`, `position`, `top`, `right`, `bottom`, `left`, `z-index`
2. **Box Model**: `w-*`, `h-*`, `p-*`, `m-*`, `border`
3. **Typography**: `font-*`, `text-*`, `leading-*`
4. **Backgrounds & Colors**: `bg-*`, `text-*` (color), `border-*` (color)
5. **States & Transitions**: `hover:*`, `focus:*`, `transition`, `duration-*`
6. **Responsive Prefixes**: `sm:*`, `md:*`, `lg:*` should come at the end of the style group they belong to.

**Example:**

```html
<div class="relative z-10 block w-full p-4 m-2 bg-white border rounded-lg shadow-md sm:w-1/2 lg:w-1/3 hover:bg-gray-100">
  <!-- ... -->
</div>
```

## 3. Responsive Design

Use prefixes (`sm:`, `md:`, `lg:`, `xl:`, `2xl:`) to apply styles at different screen sizes. Apply a "mobile-first" approach: style for mobile first, then override for larger screens.

```html
<!-- Full width on mobile, 50% on tablets (sm), and 33.3% on desktops (lg) -->
<div class="w-full sm:w-1/2 lg:w-1/3">
  <!-- ... -->
</div>
```

## 4. States

Use state prefixes (`hover:`, `focus:`, `active:`, `disabled:`, `group-hover:`) to style elements based on their state.

```html
<button class="bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50">
  Save
</button>
```

## 5. Dark Mode

Use the `dark:` prefix to apply styles in dark mode.

```html
<div class="bg-white dark:bg-gray-800 text-black dark:text-white">
  <!-- ... -->
</div>
```

## 6. Arbitrary Values

Use the square bracket notation `[...]` only in rare cases where the desired value is not available in `tailwind.config.js`. Always prefer values from the theme.

- **AVOID:**

  ```html
  <div class="top-[117px]">...</div>
  ```

- **PREFER (if possible):**
  Use the closest value from the theme (`top-28` is `112px`, `top-32` is `128px`) or add a new value to `tailwind.config.js`.

## 7. Configuration with `tailwind.config.js`

- **Study `tailwind.config.js`**: Before starting, familiarize yourself with the configuration file, especially the `theme.extend` sections. Use the colors, fonts, spacing, and other values defined there.
- **Don't duplicate values**: Do not use arbitrary values for colors or spacing that are already defined in the theme.

## 8. Dynamic Classes and PurgeCSS/JIT

To ensure the Tailwind JIT compiler can detect and include all necessary classes in the final CSS bundle, **never create class names by concatenating strings**.

- **INCORRECT (JIT won't see the class):**

  ```javascript
  // React/JS
  const color = 'blue';
  const className = `text-${color}-500`; // JIT cannot scan this
  return <div className={className}>...</div>;
  ```

- **CORRECT (JIT sees the full class names):**

  ```javascript
  // React/JS
  const colorClasses = {
    blue: 'text-blue-500',
    red: 'text-red-500',
  };
  const color = 'blue';
  return <div className={colorClasses[color]}>...</div>;
  ```

  This way, the full class name strings are present in the file and can be detected by the scanner.

## 9. Component Abstraction

If a specific set of utility classes is repeated multiple times, do not use the `@apply` directive to create a new CSS class. Instead, create a reusable component (e.g., in React, Vue, Svelte).

- **INCORRECT (`@apply`):**

  ```css
  /* DO NOT DO THIS IN COMPONENTS */
  .btn-primary {
    @apply bg-blue-500 text-white font-bold py-2 px-4 rounded;
  }
  ```

  ```jsx
    // Button.jsx (React)
    function Button({ children, ...props }) {
      return (
        <button
          className="btn-primary"
          {...props}
        >
          {children}
        </button>
      );
    }
  ```

- **CORRECT (creating a component):**

  ```jsx
  // Button.jsx (React)
  function Button({ children, ...props }) {
    return (
      <button
        className="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
        {...props}
      >
        {children}
      </button>
    );
  }
  ```

- **BEST PRACTICES (creating a component using multiple components, use `@apply` or `@extend`):**

  ```css
  .btn-primary {
    @apply bg-blue-500 text-white font-bold py-2 px-4 rounded;
  }
  ```

  ```scss
  .btn-primary {
    @extend .bg-blue-500, .text-white, .font-bold, .py-2, .px-4, .rounded;
  }

  ```jsx
  // Form.jsx (React)
  function Form() {
    return (
      <button className="btn-primary">Ok</button>
      <button className="btn-primary">Cancel</button>
    );
  }
  ```
