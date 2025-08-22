---
description: This document outlines the SASS/SCSS coding style guide to be followed by AI agents. It ensures consistency, readability, and maintainability of the codebase.
globs:
  - "**/*.{sass,scss,css}"
alwaysApply: false
---

# SASS/SCSS Coding Style Guide

This guide provides a set of rules and best practices for writing SASS/SCSS code. Adhering to these guidelines will help maintain a clean, scalable, and collaborative codebase.

## 1. Syntax and Formatting

- **Syntax**: Use the SCSS syntax (`.scss`), not the original Sass syntax (`.sass`).
- **Indentation**: Use 2 or 4 spaces for indentation. Do not use tabs.
- **Line Breaks**: Add a new line after each ruleset.
- **Semicolons**: End every declaration with a semicolon.

```scss
// Good
.element {
  color: #fff;
  background-color: #000;
}

// Bad
.element{color:#fff;background-color:#000}
```

## 2. File Structure (7-1 Pattern)

Organize your Sass files into a structured architecture. The 7-1 pattern is a widely-used standard that keeps your project organized and scalable.

- `base/`: Boilerplate code, type definitions, and resets.
- `components/`: Styles for individual components (buttons, forms, etc.).
- `layout/`: Styles for the main layout sections (header, footer, grid).
- `pages/`: Page-specific styles.
- `themes/`: Styles for different themes.
- `utils/`: Global variables, functions, mixins, and placeholders.
- `vendors/`: Third-party CSS files.

And a single `main.scss` file to import all of them.

```scss
// main.scss
@import 'utils/variables';
@import 'utils/mixins';

@import 'base/reset';
@import 'base/typography';

@import 'components/buttons';
@import 'components/forms';

@import 'layout/header';
@import 'layout/footer';

@import 'pages/home';
```

## 3. Naming Conventions (BEM)

Use the Block, Element, Modifier (BEM) methodology for naming your classes. This makes your CSS more readable and easier to understand.

- **Block**: A standalone component (e.g., `.card`).
- **Element**: A part of a block (e.g., `.card__title`).
- **Modifier**: A different state or version of a block or element (e.g., `.card--dark`, `.card__title--large`).

```scss
.card {
  // Block
  border-radius: 8px;

  &__title {
    // Element
    font-size: 1.5rem;

    &--large {
      // Modifier
      font-size: 2rem;
    }
  }

  &--dark {
    // Modifier
    background-color: #333;
    color: #fff;
  }
}
```

## 4. Nesting

Limit nesting to a maximum of **3 levels**. Over-nesting leads to overly specific CSS selectors that are hard to override and maintain.

```scss
// Good
.card {
  .card__header {
    .card__title {
      // Max level of nesting
    }
  }
}

// Bad: Avoid this
.section {
  .container {
    .row {
      .col {
        .card {
          // ...
        }
      }
    }
  }
}
```

## 5. Variables

Use variables for colors, fonts, spacing, and other reusable values. This makes your code easier to maintain and update. Prefix variables with their type (e.g., `$color-`, `$font-`, `$spacing-`).

```scss
// utils/_variables.scss
$color-primary: #007bff;
$color-secondary: #6c757d;

$font-family-base: 'Helvetica Neue', Arial, sans-serif;
$font-size-base: 16px;

$spacing-unit: 8px;
```

## 6. Mixins

Use mixins to create reusable chunks of CSS. They are particularly useful for vendor prefixes or complex properties.

```scss
// utils/_mixins.scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  @include flex-center;
}
```

## 7. Functions

Use functions for logic and calculations. Functions should be pure, meaning they always return the same output for the same input.

```scss
// utils/_functions.scss
@function spacing($multiplier) {
  @return $spacing-unit * $multiplier;
}

.element {
  padding: spacing(2); // 16px
}
```

## 8. Extend/Placeholders

Prefer using placeholder selectors (`%`) with `@extend` over mixins when you need to share the exact same set of styles across multiple selectors. This produces more efficient CSS by grouping selectors.

```scss
// Good: Use placeholders
%message {
  padding: 10px;
  border: 1px solid #ccc;
}

.success {
  @extend %message;
  border-color: green;
}

.error {
  @extend %message;
  border-color: red;
}

// Bad: Using a mixin here would duplicate the code
@mixin message-mixin {
  padding: 10px;
  border: 1px solid #ccc;
}
```

## 9. Comments

- Use `//` for single-line comments. They are removed during compilation.
- Use `/* ... */` for multi-line comments that you want to appear in the final CSS output (e.g., for documentation or licensing).
- Write clear and concise comments to explain complex or non-obvious code.

```scss
// This is a single-line comment.

/*
 * This is a multi-line comment that will
 * appear in the compiled CSS file.
 */
```

## 10. Linting

Use a linter like [Stylelint](https://stylelint.io/) to enforce these rules automatically. This helps catch errors and maintain a consistent coding style across the project.
