---
description: Comprehensive C++ programming guidelines optimized for AI agents. Includes measurable standards, automated validation, and quality checklists for generating robust, maintainable code.
globs: /**/*.c, /**/*.cpp, /**/*.h, /**/*.hpp, /**/*.cxx, /**/*.cc, CMakeLists.txt, *.cmake, conanfile.txt, Makefile
alwaysApply: false
---

# C++ Programming Guidelines for AI Agents

## 1. Code Generation Standards

### Measurable Complexity Limits

**MANDATORY STANDARDS:**

- Functions: Maximum 20 lines (preferred), 30 lines (absolute max)
- Classes: Maximum 300 lines, 10 public methods, 10 properties  
- Files: Maximum 500 lines (implementation), 200 lines (headers)
- Cyclomatic complexity: Maximum 10 per function
- Nesting depth: Maximum 3 levels

**NAMING CONVENTIONS:**

```text
Classes/Structs:     PascalCase          (EmailValidator, UserAccount)
Functions/Methods:   camelCase           (validateEmail, getUserById)
Variables:           camelCase           (userEmail, accountBalance)
Constants:           SCREAMING_SNAKE     (MAX_RETRY_COUNT, DEFAULT_TIMEOUT)
Files:               snake_case          (email_validator.h, user_account.cpp)
Namespaces:          snake_case          (core_utils, network_client)
```

**TYPE SAFETY REQUIREMENTS:**

```cpp
// ✅ Always specify return types explicitly
auto calculateTotal(const std::vector<double>& prices) -> double {
    return std::accumulate(prices.begin(), prices.end(), 0.0);
}

// ✅ Use strong typing for domain concepts
class UserId {
public:
    explicit UserId(int id) : value_(id) {}
    int getValue() const { return value_; }
private:
    int value_;
};

// ❌ Avoid primitive obsession
void processUser(int id, std::string name); // Bad
void processUser(const UserId& id, const UserName& name); // Good
```

## 2. Change Management

### Atomic Commit Standards

**COMMIT VALIDATION CHECKLIST:**

```bash
# Mandatory checks before any commit
☐ Build passes: cmake --build build/
☐ Tests pass: ctest --test-dir build/
☐ Static analysis: clang-tidy src/**/*.cpp
☐ Format check: clang-format --dry-run --Werror
☐ Memory check: valgrind --leak-check=full
```

**BACKWARD COMPATIBILITY:**

```cpp
// ✅ Maintain API compatibility with deprecation
namespace v1 {
    [[deprecated("Use v2::EmailValidator instead")]]
    class LegacyEmailValidator {
        bool validate(const std::string& email);
    };
}

namespace v2 {
    class EmailValidator {
        ValidationResult validate(const EmailAddress& email);
    };
}
```

## 3. Communication Standards

### Documentation Requirements

**DOXYGEN TEMPLATE:**

```cpp
/**
 * @brief Validates email address according to RFC 5322
 * 
 * @param email Email address to validate (must not be empty)
 * @return ValidationResult with success status and error details
 * @throws std::invalid_argument if email is null
 * 
 * @example
 * auto result = validator.validate("user@example.com");
 * if (result.isValid()) { /* process */ }
 * 
 * @since version 2.1.0
 */
ValidationResult validate(const std::string& email);
```

**ERROR COMMUNICATION:**

```cpp
struct ValidationResult {
    bool isValid;
    std::string errorMessage;
    size_t errorPosition;
    
    static ValidationResult success() {
        return {true, "", 0};
    }
    
    static ValidationResult failure(const std::string& message, size_t pos = 0) {
        return {false, message, pos};
    }
};
```

## 4. Quality Assurance

### Testing Standards

**UNIT TEST STRUCTURE:**

```cpp
TEST_F(EmailValidatorTest, ShouldReturnTrueWhenEmailIsValid) {
    // Arrange
    const std::string validEmail = "user@example.com";
    
    // Act
    const auto result = validator_->validate(validEmail);
    
    // Assert
    EXPECT_TRUE(result.isValid);
    EXPECT_EQ(result.errorMessage, "");
}
```

**COVERAGE REQUIREMENTS:**

- Minimum 80% line coverage
- 100% coverage for public APIs
- All error paths must be tested
- Include edge cases and boundary conditions

**CODE REVIEW CHECKLIST:**

```text
Automated:
☐ Build successful (zero warnings)
☐ All tests pass
☐ Code coverage ≥ 80%
☐ Static analysis clean
☐ Memory leaks check

Manual:
☐ Functions ≤ 20 lines
☐ Classes ≤ 300 lines
☐ Single responsibility
☐ Meaningful names
☐ No magic numbers
☐ Proper error handling
```

## 5. Security and Performance

### Security Standards

**INPUT VALIDATION:**

```cpp
template<typename T>
class SecureInput {
public:
    explicit SecureInput(T value) {
        validate(value);
        value_ = std::move(value);
    }
    const T& get() const { return value_; }
    
private:
    T value_;
    void validate(const T& value); // Implement validation logic
};

// Usage
void processUserEmail(const std::string& email) {
    try {
        SecureInput<std::string> secureEmail(email);
        doProcessEmail(secureEmail.get());
    } catch (const std::exception& e) {
        logSecurityIncident(email, e.what());
        throw;
    }
}
```

**MEMORY SAFETY:**

```cpp
// ✅ Use smart pointers for automatic memory management
class ResourceManager {
public:
    std::unique_ptr<Resource> createResource() {
        return std::make_unique<Resource>();
    }
    
    std::shared_ptr<Cache> getSharedCache() {
        static auto cache = std::make_shared<Cache>();
        return cache;
    }
};

// ✅ RAII for resource management
class FileHandler {
public:
    explicit FileHandler(const std::string& filename);
    ~FileHandler();
    
    // Rule of Five
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
    FileHandler(FileHandler&& other) noexcept;
    FileHandler& operator=(FileHandler&& other) noexcept;
};
```

### Performance Standards

**ALGORITHMIC COMPLEXITY:**

```text
Search Operations:    O(log n) or better
Sort Operations:      O(n log n) or better
Insert/Delete:        O(log n) for ordered, O(1) average for hash
Space Complexity:     O(n) or better
Memory Allocation:    Minimize in hot paths
```

**OPTIMIZATION PATTERNS:**

```cpp
// ✅ Use containers efficiently
class OptimizedUserStore {
public:
    void addUser(User user) {
        if (users_.capacity() < users_.size() + 1) {
            users_.reserve(users_.size() * 2);
        }
        const auto userId = user.getId();
        users_.emplace_back(std::move(user));
        userIndex_[userId] = users_.size() - 1;
    }
    
private:
    std::vector<User> users_;                    // Sequential storage
    std::unordered_map<UserId, size_t> userIndex_; // O(1) lookup
};
```

## 6. Language-Specific Standards

### Modern C++ Features (C++17/20/23)

**MANDATORY MODERN FEATURES:**

```cpp
// ✅ Use structured bindings
auto [success, value, error] = parseInput(userInput);

// ✅ Use if-init statements
if (auto result = validateInput(data); result.isValid()) {
    processValidData(result.getValue());
}

// ✅ Use std::optional for nullable values
std::optional<User> findUserById(UserId id) {
    const auto it = users_.find(id);
    return (it != users_.end()) ? std::make_optional(it->second) : std::nullopt;
}

// ✅ Use concepts for type constraints (C++20)
template<typename T>
concept Serializable = requires(T t) {
    { t.serialize() } -> std::convertible_to<std::string>;
};
```

### Standard Library Usage

**CONTAINER SELECTION:**

```text
Sequential Access:           std::vector (default)
Frequent Insert/Delete:      std::deque, std::list
Unique Elements:             std::set, std::unordered_set
Key-Value Mapping:           std::map, std::unordered_map
Optional Values:             std::optional
Type-Safe Unions:            std::variant
String Operations:           std::string, std::string_view
```

**CONCURRENCY STANDARDS:**

```cpp
// ✅ Thread-safe design patterns
class ThreadSafeCache {
public:
    void put(const std::string& key, std::string value) {
        std::unique_lock lock(mutex_);
        cache_[key] = std::move(value);
    }
    
    std::optional<std::string> get(const std::string& key) const {
        std::shared_lock lock(mutex_);
        const auto it = cache_.find(key);
        return (it != cache_.end()) ? std::make_optional(it->second) : std::nullopt;
    }
    
private:
    mutable std::shared_mutex mutex_;
    std::unordered_map<std::string, std::string> cache_;
};

// ✅ Atomic operations for simple counters
class MetricsCollector {
public:
    void incrementRequests() {
        requestCount_.fetch_add(1, std::memory_order_relaxed);
    }
    
private:
    std::atomic<uint64_t> requestCount_{0};
};
```

## 7. Continuous Improvement

### Refactoring Guidelines

**REFACTORING TRIGGERS:**

```text
Function Length:        > 20 lines → Extract smaller functions
Class Size:            > 300 lines → Split responsibilities  
Parameter Count:       > 4 parameters → Use parameter objects
Cyclomatic Complexity: > 10 → Simplify control flow
Duplicated Code:       > 3 occurrences → Extract common functionality
Deep Nesting:          > 3 levels → Use early returns
```

**PERFORMANCE MONITORING:**

```cpp
#include <benchmark/benchmark.h>

// Micro-benchmarks for critical functions
static void BM_EmailValidation(benchmark::State& state) {
    EmailValidator validator;
    const std::string testEmail = "user@example.com";
    
    for (auto _ : state) {
        auto result = validator.validate(testEmail);
        benchmark::DoNotOptimize(result);
    }
}
REGISTER_BENCHMARK(BM_EmailValidation);
```

## 8. AI-Specific Best Practices

### Code Generation Validation

**PRE-GENERATION CHECKLIST:**

```text
Requirement Analysis:
☐ Understand business requirements completely
☐ Identify input/output specifications
☐ Determine error handling requirements
☐ Consider performance constraints
☐ Identify security requirements

Design Decisions:
☐ Choose appropriate design patterns
☐ Select optimal data structures
☐ Plan for testability
☐ Consider future extensibility
☐ Minimize dependencies
```

**POST-GENERATION VALIDATION:**

```bash
#!/bin/bash
# Automated validation script for AI-generated code

echo "🔨 Building code..."
cmake --build build/ --target all

echo "🧪 Running tests..."
ctest --test-dir build/ --output-on-failure

echo "🔍 Static analysis..."
clang-tidy src/**/*.cpp

echo "🎨 Format check..."
clang-format --dry-run --Werror src/**/*.{cpp,h}

echo "🛡️ Security scan..."
cppcheck --enable=all src/

echo "💾 Memory check..."
valgrind --leak-check=full ./build/tests

echo "✅ All validations passed!"
```

### Error Recovery Patterns

**ROBUST ERROR HANDLING:**

```cpp
#include <expected> // C++23

// Use std::expected for recoverable errors
std::expected<ProcessingResult, std::error_code> 
processData(const InputData& data) {
    try {
        if (!data.isValid()) {
            return std::unexpected(ProcessingError::InvalidInput);
        }
        
        auto result = performOperation(data);
        if (!result.has_value()) {
            return std::unexpected(result.error());
        }
        
        return ProcessingResult{result.value()};
        
    } catch (const std::bad_alloc&) {
        return std::unexpected(ProcessingError::InsufficientMemory);
    }
}
```

### Quality Metrics

**AUTOMATED QUALITY GATES:**

```text
Code Quality Metrics:
• Cyclomatic Complexity: ≤ 10 per function
• Function Length: ≤ 20 lines
• Class Size: ≤ 300 lines
• Test Coverage: ≥ 80%
• Static Analysis: Zero violations
• Memory Leaks: Zero detected
• Build Warnings: Zero allowed
• Performance Regression: < 5% degradation
```

**CONTINUOUS VALIDATION:**

```cpp
// Example validation in CI/CD pipeline
class QualityGate {
public:
    struct Metrics {
        double testCoverage;
        int cyclomaticComplexity;
        int functionLength;
        int buildWarnings;
        bool hasMemoryLeaks;
    };
    
    bool passesQualityGate(const Metrics& metrics) {
        return metrics.testCoverage >= 0.80 &&
               metrics.cyclomaticComplexity <= 10 &&
               metrics.functionLength <= 20 &&
               metrics.buildWarnings == 0 &&
               !metrics.hasMemoryLeaks;
    }
};
```

---

## Summary

These guidelines provide AI agents with:

1. **Measurable Standards**: Clear numeric limits for code complexity
2. **Automated Validation**: Scripts and checklists for quality assurance
3. **Security Focus**: Built-in security patterns and validation
4. **Performance Optimization**: Guidelines for efficient code generation
5. **Modern C++**: Leverage latest language features effectively
6. **Continuous Improvement**: Refactoring triggers and monitoring
7. **Error Recovery**: Robust error handling patterns
8. **Quality Gates**: Automated quality validation metrics

Follow these guidelines to generate production-ready, maintainable, and secure C++ code that meets enterprise standards.
