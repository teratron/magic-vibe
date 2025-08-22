---
description: Comprehensive Next.js 14+ guidelines optimized for AI agents. Includes App Router, Server Components, TypeScript, performance optimization, and modern patterns.
globs: /**/*.tsx, /**/*.ts, src/**/*.ts, src/**/*.tsx
---

# Next.js Development Guidelines for AI Agents

## 1. Project Architecture Standards

### App Router Structure (Next.js 13+)

**MANDATORY STRUCTURE:**

```text
app/
├── globals.css
├── layout.tsx         # Root layout
├── page.tsx           # Home page
├── loading.tsx        # Global loading UI
├── error.tsx          # Global error UI
├── not-found.tsx      # 404 page
├── (auth)/            # Route groups
│   ├── login/
│   │   └── page.tsx
│   └── register/
│       └── page.tsx
├── dashboard/
│   ├── layout.tsx     # Nested layout
│   ├── page.tsx
│   ├── loading.tsx
│   └── users/
│       └── [id]/
│           └── page.tsx
components/
├── ui/                # Reusable UI components
├── forms/             # Form components
└── providers/         # Context providers
lib/
├── utils.ts
├── validations.ts
└── db.ts
```

### File Naming Conventions

- **Pages**: `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`
- **Components**: PascalCase (`UserProfile.tsx`)
- **Utilities**: camelCase (`formatDate.ts`)
- **Directories**: kebab-case (`user-settings/`)

## 2. Component Architecture

### Server vs Client Components

```typescript
// ✅ Good - Server Component (default)
export default async function UserList() {
  const users = await getUsers() // Direct DB access
  
  return (
    <div>
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  )
}

// ✅ Good - Client Component when needed
'use client'

import { useState } from 'react'

interface SearchProps {
  onSearch: (query: string) => void
}

export function SearchForm({ onSearch }: SearchProps) {
  const [query, setQuery] = useState('')
  
  return (
    <form onSubmit={(e) => {
      e.preventDefault()
      onSearch(query)
    }}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search users..."
      />
    </form>
  )
}
```

### Layout Patterns

```typescript
// app/layout.tsx - Root Layout
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Providers>
          <Header />
          <main className="min-h-screen">
            {children}
          </main>
          <Footer />
        </Providers>
      </body>
    </html>
  )
}

// app/dashboard/layout.tsx - Nested Layout
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        {children}
      </div>
    </div>
  )
}
```

## 3. Data Fetching Patterns

### Server Components Data Fetching

```typescript
// ✅ Good - Direct data fetching in Server Components
export default async function PostPage({ 
  params 
}: { 
  params: { id: string } 
}) {
  const post = await getPost(params.id)
  
  if (!post) {
    notFound()
  }
  
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  )
}

// lib/api.ts
export async function getPost(id: string) {
  try {
    const post = await db.post.findUnique({
      where: { id },
      include: { author: true }
    })
    return post
  } catch (error) {
    console.error('Failed to fetch post:', error)
    throw new Error('Failed to load post')
  }
}
```

### Client-Side Data Fetching

```typescript
'use client'

import useSWR from 'swr'

interface User {
  id: string
  name: string
  email: string
}

const fetcher = (url: string) => fetch(url).then(res => res.json())

export function UserProfile({ userId }: { userId: string }) {
  const { data: user, error, isLoading } = useSWR<User>(
    `/api/users/${userId}`,
    fetcher
  )
  
  if (error) return <div>Failed to load user</div>
  if (isLoading) return <div>Loading...</div>
  if (!user) return <div>User not found</div>
  
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  )
}
```

## 4. API Routes and Server Actions

### API Route Handlers

```typescript
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { z } from 'zod'

const CreateUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
})

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { name, email } = CreateUserSchema.parse(body)
    
    const user = await createUser({ name, email })
    
    return NextResponse.json(user, { status: 201 })
  } catch (error) {
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Invalid input', details: error.errors },
        { status: 400 }
      )
    }
    
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    )
  }
}

export async function GET() {
  try {
    const users = await getUsers()
    return NextResponse.json(users)
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    )
  }
}
```

### Server Actions

```typescript
// lib/actions.ts
'use server'

import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createUser(formData: FormData) {
  const name = formData.get('name') as string
  const email = formData.get('email') as string
  
  // Validate input
  if (!name || !email) {
    throw new Error('Name and email are required')
  }
  
  try {
    const user = await db.user.create({
      data: { name, email }
    })
    
    revalidatePath('/users')
    redirect(`/users/${user.id}`)
  } catch (error) {
    throw new Error('Failed to create user')
  }
}

// Usage in component
export function CreateUserForm() {
  return (
    <form action={createUser}>
      <input name="name" placeholder="Name" required />
      <input name="email" type="email" placeholder="Email" required />
      <button type="submit">Create User</button>
    </form>
  )
}
```

## 5. Performance Optimization

### Image Optimization

```typescript
import Image from 'next/image'

// ✅ Good - Optimized image usage
export function UserAvatar({ user }: { user: User }) {
  return (
    <Image
      src={user.avatar || '/default-avatar.jpg'}
      alt={`${user.name}'s avatar`}
      width={40}
      height={40}
      className="rounded-full"
      priority={user.isCurrentUser} // For above-fold images
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k="
    />
  )
}
```

### Dynamic Imports and Code Splitting

```typescript
// ✅ Good - Dynamic component loading
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('./HeavyChart'), {
  loading: () => <div>Loading chart...</div>,
  ssr: false // Client-side only
})

const AdminPanel = dynamic(() => import('./AdminPanel'), {
  loading: () => <div>Loading admin panel...</div>
})

export function Dashboard({ isAdmin }: { isAdmin: boolean }) {
  return (
    <div>
      <HeavyChart />
      {isAdmin && <AdminPanel />}
    </div>
  )
}
```

### Streaming and Suspense

```typescript
// ✅ Good - Streaming UI with Suspense
import { Suspense } from 'react'

export default function PostPage({ params }: { params: { id: string } }) {
  return (
    <div>
      <Suspense fallback={<PostSkeleton />}>
        <PostContent id={params.id} />
      </Suspense>
      <Suspense fallback={<CommentsSkeleton />}>
        <Comments postId={params.id} />
      </Suspense>
    </div>
  )
}

async function PostContent({ id }: { id: string }) {
  const post = await getPost(id) // This can be slow
  return <article>{post.content}</article>
}

async function Comments({ postId }: { postId: string }) {
  const comments = await getComments(postId) // This can also be slow
  return (
    <div>
      {comments.map(comment => (
        <div key={comment.id}>{comment.text}</div>
      ))}
    </div>
  )
}
```

## 6. Form Handling and Validation

### Server-Side Form Validation

```typescript
// lib/validations.ts
import { z } from 'zod'

export const CreatePostSchema = z.object({
  title: z.string().min(1, 'Title is required').max(100),
  content: z.string().min(10, 'Content must be at least 10 characters'),
  tags: z.array(z.string()).max(5, 'Maximum 5 tags allowed')
})

// lib/actions.ts
'use server'

export async function createPost(formData: FormData) {
  const rawData = {
    title: formData.get('title'),
    content: formData.get('content'),
    tags: formData.getAll('tags')
  }
  
  const validationResult = CreatePostSchema.safeParse(rawData)
  
  if (!validationResult.success) {
    return {
      errors: validationResult.error.flatten().fieldErrors
    }
  }
  
  try {
    const post = await db.post.create({
      data: validationResult.data
    })
    
    revalidatePath('/posts')
    redirect(`/posts/${post.id}`)
  } catch (error) {
    return {
      errors: { root: ['Failed to create post'] }
    }
  }
}
```

### Client-Side Form with React Hook Form

```typescript
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'

type CreatePostForm = z.infer<typeof CreatePostSchema>

export function CreatePostForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm<CreatePostForm>({
    resolver: zodResolver(CreatePostSchema)
  })
  
  const onSubmit = async (data: CreatePostForm) => {
    const formData = new FormData()
    Object.entries(data).forEach(([key, value]) => {
      if (Array.isArray(value)) {
        value.forEach(item => formData.append(key, item))
      } else {
        formData.append(key, value)
      }
    })
    
    await createPost(formData)
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register('title')}
        placeholder="Post title"
      />
      {errors.title && (
        <p className="text-red-500">{errors.title.message}</p>
      )}
      
      <textarea
        {...register('content')}
        placeholder="Post content"
      />
      {errors.content && (
        <p className="text-red-500">{errors.content.message}</p>
      )}
      
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Creating...' : 'Create Post'}
      </button>
    </form>
  )
}
```

## 7. Error Handling and Loading States

### Error Boundaries

```typescript
// app/error.tsx - Route-level error boundary
'use client'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  )
}

// app/not-found.tsx
export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h2>404 - Page Not Found</h2>
      <p>The page you're looking for doesn't exist.</p>
      <Link href="/" className="mt-4 text-blue-500">
        Go back home
      </Link>
    </div>
  )
}
```

### Loading States

```typescript
// app/loading.tsx - Route-level loading
export default function Loading() {
  return (
    <div className="animate-pulse">
      <div className="h-8 bg-gray-200 rounded mb-4"></div>
      <div className="h-4 bg-gray-200 rounded mb-2"></div>
      <div className="h-4 bg-gray-200 rounded mb-2"></div>
    </div>
  )
}
```

## 8. Authentication and Middleware

### Authentication with Next-Auth

```typescript
// lib/auth.ts
import NextAuth from 'next-auth'
import GoogleProvider from 'next-auth/providers/google'

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!
    })
  ],
  callbacks: {
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.sub!
      }
      return session
    }
  }
})

// middleware.ts
import { auth } from '@/lib/auth'

export default auth((req) => {
  const { pathname } = req.nextUrl
  
  // Protected routes
  if (pathname.startsWith('/dashboard')) {
    if (!req.auth) {
      return Response.redirect(new URL('/login', req.url))
    }
  }
})

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
}
```

## 9. Testing Strategies

### Component Testing

```typescript
// __tests__/components/UserProfile.test.tsx
import { render, screen } from '@testing-library/react'
import { UserProfile } from '@/components/UserProfile'

const mockUser = {
  id: '1',
  name: 'John Doe',
  email: 'john@example.com'
}

describe('UserProfile', () => {
  it('renders user information correctly', () => {
    render(<UserProfile user={mockUser} />)
    
    expect(screen.getByText('John Doe')).toBeInTheDocument()
    expect(screen.getByText('john@example.com')).toBeInTheDocument()
  })
})
```

## 10. AI-Specific Guidelines

### Code Generation Requirements

**WHEN GENERATING NEXT.JS CODE:**

- Always use TypeScript with strict type checking
- Prefer Server Components unless interactivity is needed
- Include proper error handling and loading states
- Generate accompanying tests for components
- Use proper SEO meta tags and structured data
- Follow App Router conventions strictly

### Quality Checklist

**PRE-SUBMISSION VALIDATION:**

- [ ] Components follow Server/Client component rules
- [ ] All pages have proper TypeScript interfaces
- [ ] Error boundaries and loading states implemented
- [ ] Forms include both client and server validation
- [ ] Images use Next.js Image component with optimization
- [ ] API routes have proper error handling
- [ ] Performance optimizations applied (dynamic imports, Suspense)
- [ ] Tests cover main functionality

### Common Anti-Patterns to Avoid

**NEVER DO:**

- Use `useEffect` for data fetching in Server Components
- Forget 'use client' directive for interactive components
- Skip error boundaries and loading states
- Use regular `<img>` instead of Next.js `<Image>`
- Fetch data in Client Components when Server Components can do it
- Ignore TypeScript errors or use `any` types
