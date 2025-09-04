---
description: Go (Golang) programming language standards and best practices for AI agents, covering syntax, idioms, error handling, concurrency, and Go-specific development patterns.
globs: 
  - "**/*.go"
  - "**/go.mod"
  - "**/go.sum"
  - "**/Dockerfile"
alwaysApply: false
---

# Go (Golang) Programming Standards

This document defines comprehensive Go programming standards for AI agents to ensure idiomatic, efficient, and maintainable Go code following established community conventions and best practices.

## 1. Code Generation Standards

### Project Structure

Follow standard Go project layout:

```text
project/
├── cmd/                    # Main applications
│   └── myapp/
│       └── main.go
├── internal/               # Private application code
│   ├── handler/
│   ├── service/
│   └── repository/
├── pkg/                    # Public library code
├── api/                    # API definitions (OpenAPI, Protocol Buffers)
├── web/                    # Web application assets
├── configs/                # Configuration files
├── scripts/                # Scripts for build, install, analysis
├── test/                   # Additional external test apps and data
├── docs/                   # Design and user documents
├── tools/                  # Supporting tools
├── examples/               # Examples for your applications
├── third_party/            # External helper tools
├── go.mod                  # Module definition
├── go.sum                  # Module checksums
├── Makefile               # Build automation
└── README.md              # Project documentation
```

### Package Organization

```go
// Good: Clear package organization
package user

import (
    "context"
    "fmt"
    "log"
    
    "github.com/project/internal/repository"
    "github.com/project/pkg/validator"
    
    "github.com/gorilla/mux"
    "github.com/lib/pq"
)

// Group imports: standard library, internal packages, external packages
```

### Naming Conventions

```go
// Package names: lowercase, single word, descriptive
package user
package httputil
package stringutil

// Constants: CamelCase or UPPER_CASE for exported
const (
    MaxRetries = 3
    TimeoutSeconds = 30
    DEFAULT_BUFFER_SIZE = 1024
)

// Variables: camelCase or CamelCase for exported
var (
    config Config
    Logger *log.Logger
)

// Functions: CamelCase for exported, camelCase for private
func NewUser() *User { }
func (u *User) GetName() string { }
func validateEmail(email string) bool { }

// Types: CamelCase for exported, camelCase for private
type User struct { }
type userRepository struct { }

// Interfaces: -er suffix when possible
type Reader interface { }
type Writer interface { }
type UserValidator interface { }
```

## 2. Change Management

### Error Handling

```go
// Good: Explicit error handling
func processUser(id int) (*User, error) {
    user, err := repository.GetUser(id)
    if err != nil {
        return nil, fmt.Errorf("failed to get user %d: %w", id, err)
    }
    
    if err := validateUser(user); err != nil {
        return nil, fmt.Errorf("user validation failed: %w", err)
    }
    
    return user, nil
}

// Custom error types for better error handling
type ValidationError struct {
    Field string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation error in field %s: %s", e.Field, e.Message)
}

// Error wrapping for context
func saveUser(user *User) error {
    if err := repository.Save(user); err != nil {
        return fmt.Errorf("failed to save user %s: %w", user.Name, err)
    }
    return nil
}
```

### Version Control Integration

```go
// Version information should be injected at build time
var (
    Version   = "dev"
    BuildTime = "unknown"
    GitCommit = "unknown"
)

// Build with: go build -ldflags "-X main.Version=1.0.0"
```

### Dependency Management

```bash
# Initialize module
go mod init github.com/username/project

# Add dependencies
go get github.com/gorilla/mux@v1.8.0
go get -u github.com/stretchr/testify

# Tidy dependencies
go mod tidy

# Vendor dependencies (if needed)
go mod vendor
```

## 3. Communication Standards

### Documentation

```go
// Package documentation appears before package declaration
// Package user provides user management functionality.
//
// This package handles user creation, validation, and persistence
// operations with support for various authentication methods.
package user

// Exported functions must have documentation
// NewUser creates a new user with the given name and email.
// It returns an error if the email format is invalid.
func NewUser(name, email string) (*User, error) {
    // Implementation
}

// Exported types must have documentation
// User represents a system user with authentication capabilities.
type User struct {
    // ID is the unique identifier for the user
    ID int `json:"id"`
    // Name is the user's display name
    Name string `json:"name" validate:"required"`
    // Email must be a valid email address
    Email string `json:"email" validate:"required,email"`
}
```

### API Design

```go
// RESTful API patterns
type UserHandler struct {
    service UserService
}

// HTTP handler with proper error responses
func (h *UserHandler) CreateUser(w http.ResponseWriter, r *http.Request) {
    var req CreateUserRequest
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        http.Error(w, "Invalid JSON", http.StatusBadRequest)
        return
    }
    
    user, err := h.service.CreateUser(r.Context(), req)
    if err != nil {
        switch err := err.(type) {
        case *ValidationError:
            http.Error(w, err.Error(), http.StatusBadRequest)
        default:
            http.Error(w, "Internal server error", http.StatusInternalServerError)
        }
        return
    }
    
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(user)
}
```

## 4. Quality Assurance

### Testing Standards

```go
// Table-driven tests
func TestValidateEmail(t *testing.T) {
    tests := []struct {
        name    string
        email   string
        wantErr bool
    }{
        {
            name:    "valid email",
            email:   "user@example.com",
            wantErr: false,
        },
        {
            name:    "invalid email",
            email:   "invalid-email",
            wantErr: true,
        },
        {
            name:    "empty email",
            email:   "",
            wantErr: true,
        },
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            err := validateEmail(tt.email)
            if (err != nil) != tt.wantErr {
                t.Errorf("validateEmail() error = %v, wantErr %v", err, tt.wantErr)
            }
        })
    }
}

// Benchmark tests
func BenchmarkValidateEmail(b *testing.B) {
    email := "user@example.com"
    for i := 0; i < b.N; i++ {
        validateEmail(email)
    }
}

// Example tests for documentation
func ExampleUser_GetDisplayName() {
    user := &User{Name: "John Doe", Email: "john@example.com"}
    fmt.Println(user.GetDisplayName())
    // Output: John Doe
}
```

### Code Quality Tools

```bash
# Formatting
go fmt ./...

# Linting
golangci-lint run

# Vetting
go vet ./...

# Testing with coverage
go test -race -coverprofile=coverage.out ./...
go tool cover -html=coverage.out

# Security scanning
gosec ./...

# Dependency vulnerability check
govulncheck ./...
```

## 5. Security and Performance

### Security Best Practices

```go
// Input validation and sanitization
func validateUserInput(input string) error {
    if len(input) > 255 {
        return errors.New("input too long")
    }
    
    // Sanitize HTML
    sanitized := html.EscapeString(input)
    if sanitized != input {
        return errors.New("invalid characters in input")
    }
    
    return nil
}

// SQL injection prevention
func getUserByEmail(db *sql.DB, email string) (*User, error) {
    query := "SELECT id, name, email FROM users WHERE email = $1"
    row := db.QueryRow(query, email)
    
    var user User
    err := row.Scan(&user.ID, &user.Name, &user.Email)
    if err != nil {
        return nil, err
    }
    
    return &user, nil
}

// Secrets management
func getDBConnectionString() string {
    host := os.Getenv("DB_HOST")
    if host == "" {
        log.Fatal("DB_HOST environment variable not set")
    }
    
    password := os.Getenv("DB_PASSWORD")
    if password == "" {
        log.Fatal("DB_PASSWORD environment variable not set")
    }
    
    return fmt.Sprintf("host=%s password=%s", host, password)
}
```

### Performance Optimization

```go
// Efficient string building
func buildQuery(fields []string) string {
    var builder strings.Builder
    builder.WriteString("SELECT ")
    
    for i, field := range fields {
        if i > 0 {
            builder.WriteString(", ")
        }
        builder.WriteString(field)
    }
    
    builder.WriteString(" FROM users")
    return builder.String()
}

// Memory-efficient slice operations
func filterUsers(users []User, predicate func(User) bool) []User {
    result := users[:0] // Reuse underlying array
    for _, user := range users {
        if predicate(user) {
            result = append(result, user)
        }
    }
    return result
}

// Context-aware operations
func processUserWithTimeout(ctx context.Context, userID int) error {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()
    
    done := make(chan error, 1)
    go func() {
        // Simulate heavy operation
        time.Sleep(2 * time.Second)
        done <- nil
    }()
    
    select {
    case err := <-done:
        return err
    case <-ctx.Done():
        return ctx.Err()
    }
}
```

## 6. Language-Specific Standards

### Concurrency Patterns

```go
// Worker pool pattern
func processItems(items []Item) error {
    const numWorkers = 10
    itemChan := make(chan Item, len(items))
    errorChan := make(chan error, len(items))
    
    // Start workers
    var wg sync.WaitGroup
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for item := range itemChan {
                if err := processItem(item); err != nil {
                    errorChan <- err
                    return
                }
            }
        }()
    }
    
    // Send items to workers
    for _, item := range items {
        itemChan <- item
    }
    close(itemChan)
    
    // Wait for completion
    go func() {
        wg.Wait()
        close(errorChan)
    }()
    
    // Check for errors
    for err := range errorChan {
        if err != nil {
            return err
        }
    }
    
    return nil
}

// Pipeline pattern
func pipeline(input <-chan int) <-chan int {
    output := make(chan int)
    go func() {
        defer close(output)
        for n := range input {
            output <- n * 2
        }
    }()
    return output
}
```

### Interface Design

```go
// Small, focused interfaces
type Reader interface {
    Read([]byte) (int, error)
}

type Writer interface {
    Write([]byte) (int, error)
}

// Interface composition
type ReadWriter interface {
    Reader
    Writer
}

// Accept interfaces, return concrete types
func ProcessData(r Reader) (*ProcessedData, error) {
    // Implementation
    return &ProcessedData{}, nil
}
```

### Memory Management

```go
// Efficient slice allocation
func processLargeDataset(size int) []Result {
    // Pre-allocate with known capacity
    results := make([]Result, 0, size)
    
    for i := 0; i < size; i++ {
        result := processItem(i)
        results = append(results, result)
    }
    
    return results
}

// Pool pattern for object reuse
var bufferPool = sync.Pool{
    New: func() interface{} {
        return make([]byte, 0, 1024)
    },
}

func processWithBuffer() {
    buffer := bufferPool.Get().([]byte)
    defer bufferPool.Put(buffer[:0]) // Reset slice but keep capacity
    
    // Use buffer
}
```

## 7. Continuous Improvement

### Code Metrics

- **Cyclomatic Complexity:** Maximum 10 per function
- **Function Length:** Maximum 50 lines, prefer 20 lines
- **File Length:** Maximum 500 lines, prefer 300 lines
- **Test Coverage:** Minimum 80%, target 90%
- **Import Depth:** Maximum 5 levels

### Performance Benchmarks

```go
// Performance testing
func BenchmarkProcessUser(b *testing.B) {
    user := &User{ID: 1, Name: "Test", Email: "test@example.com"}
    
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        processUser(user)
    }
}

// Memory allocation tracking
func BenchmarkMemoryAllocation(b *testing.B) {
    b.ReportAllocs()
    for i := 0; i < b.N; i++ {
        data := make([]byte, 1024)
        _ = data
    }
}
```

### Code Review Checklist

- [ ] Follows Go formatting (gofmt)
- [ ] No golangci-lint warnings
- [ ] Proper error handling with context
- [ ] Thread-safe concurrent code
- [ ] Appropriate use of interfaces
- [ ] Comprehensive test coverage
- [ ] Performance considerations addressed
- [ ] Security vulnerabilities checked
- [ ] Documentation for exported symbols
- [ ] Follows established project patterns

## 8. AI-Specific Best Practices

### Code Generation Guidelines

1. **Always check for existing Go modules** before creating new ones
2. **Use standard library first** before adding external dependencies
3. **Generate idiomatic Go code** following community conventions
4. **Include comprehensive error handling** in all generated code
5. **Add appropriate tests** for all generated functions

### Integration Patterns

```go
// Configuration management
type Config struct {
    Server   ServerConfig   `yaml:"server"`
    Database DatabaseConfig `yaml:"database"`
    Redis    RedisConfig    `yaml:"redis"`
}

func LoadConfig(path string) (*Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return nil, fmt.Errorf("failed to read config file: %w", err)
    }
    
    var config Config
    if err := yaml.Unmarshal(data, &config); err != nil {
        return nil, fmt.Errorf("failed to parse config: %w", err)
    }
    
    return &config, nil
}

// Graceful shutdown
func (s *Server) Shutdown(ctx context.Context) error {
    done := make(chan error, 1)
    go func() {
        done <- s.httpServer.Shutdown(ctx)
    }()
    
    select {
    case err := <-done:
        return err
    case <-ctx.Done():
        return ctx.Err()
    }
}
```

### Build and Deployment

```dockerfile
# Multi-stage Docker build
FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main ./cmd/app

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/main .
CMD ["./main"]
```

```makefile
# Makefile for Go projects
.PHONY: build test lint fmt vet clean

build:
 go build -o bin/app ./cmd/app

test:
 go test -race -coverprofile=coverage.out ./...

lint:
 golangci-lint run

fmt:
 go fmt ./...

vet:
 go vet ./...

clean:
 rm -rf bin/
 go clean -testcache

install-tools:
 go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
 go install golang.org/x/vuln/cmd/govulncheck@latest
```

This comprehensive Go standard ensures AI agents generate high-quality, idiomatic, secure, and maintainable Go code following established community practices and modern development standards.
