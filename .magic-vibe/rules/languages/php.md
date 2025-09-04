---
description: PHP programming language standards and best practices for AI agents, covering modern PHP syntax, object-oriented patterns, PSR standards, and security practices.
globs: 
  - "**/*.php"
  - "**/composer.json"
  - "**/composer.lock"
  - "**/phpunit.xml"
  - "**/psalm.xml"
  - "**/phpstan.neon"
alwaysApply: false
---

# PHP Programming Standards

This document defines comprehensive PHP programming standards for AI agents to ensure modern, secure, and maintainable PHP code following PSR standards and community best practices.

## 1. Code Generation Standards

### Project Structure

Follow modern PHP project layout with PSR-4 autoloading:

```text
project/
├── src/                    # Source code (PSR-4 namespace)
│   ├── Controller/
│   ├── Model/
│   ├── Service/
│   ├── Repository/
│   └── Exception/
├── tests/                  # Test files
│   ├── Unit/
│   ├── Integration/
│   └── Feature/
├── public/                 # Public web files
│   └── index.php
├── config/                 # Configuration files
├── resources/              # Resources (views, assets)
│   ├── views/
│   └── assets/
├── storage/                # Storage and cache
│   ├── logs/
│   └── cache/
├── vendor/                 # Composer dependencies
├── composer.json           # Dependency management
├── composer.lock           # Locked dependency versions
├── phpunit.xml            # PHPUnit configuration
├── psalm.xml              # Psalm static analysis
├── .env                   # Environment variables
└── README.md              # Project documentation
```

### PSR Standards Compliance

```php
<?php

declare(strict_types=1);

namespace App\Service;

use App\Model\User;
use App\Repository\UserRepositoryInterface;
use App\Exception\UserNotFoundException;
use Psr\Log\LoggerInterface;

/**
 * User service handles user-related business logic.
 *
 * @package App\Service
 */
final class UserService
{
    public function __construct(
        private readonly UserRepositoryInterface $userRepository,
        private readonly LoggerInterface $logger
    ) {
    }

    /**
     * Find user by ID with validation.
     *
     * @param int $id User identifier
     * @return User Found user instance
     * @throws UserNotFoundException When user is not found
     */
    public function findById(int $id): User
    {
        if ($id <= 0) {
            throw new \InvalidArgumentException('User ID must be positive integer');
        }

        $user = $this->userRepository->findById($id);
        
        if ($user === null) {
            $this->logger->warning('User not found', ['user_id' => $id]);
            throw new UserNotFoundException("User with ID {$id} not found");
        }

        return $user;
    }
}
```

### Naming Conventions

```php
<?php

// Classes: PascalCase
class UserService { }
class PaymentProcessor { }
class DatabaseConnection { }

// Methods and properties: camelCase
public function getUserData(): array { }
public function processPayment(): bool { }
private $userName;
private $lastLoginTime;

// Constants: UPPER_SNAKE_CASE
public const MAX_LOGIN_ATTEMPTS = 3;
public const DEFAULT_TIMEOUT = 30;

// Interfaces: Suffix with Interface
interface UserRepositoryInterface { }
interface PaymentGatewayInterface { }

// Abstract classes: Prefix with Abstract
abstract class AbstractController { }
abstract class AbstractRepository { }

// Traits: Suffix with Trait
trait TimestampableTrait { }
trait ValidatableTrait { }

// Exceptions: Suffix with Exception
class UserNotFoundException extends \Exception { }
class ValidationException extends \Exception { }
```

## 2. Change Management

### Type Declarations

```php
<?php

declare(strict_types=1);

class UserService
{
    // Property type declarations
    private readonly UserRepositoryInterface $repository;
    private array $cache = [];
    private ?User $currentUser = null;

    // Method parameter and return types
    public function createUser(
        string $name,
        string $email,
        array $metadata = []
    ): User {
        // Implementation
    }

    // Union types (PHP 8.0+)
    public function processInput(string|int $input): bool
    {
        return match (gettype($input)) {
            'string' => $this->processString($input),
            'integer' => $this->processInteger($input),
            default => false,
        };
    }

    // Nullable return types
    public function findUser(int $id): ?User
    {
        return $this->repository->find($id);
    }
}
```

### Error Handling

```php
<?php

// Custom exceptions with context
class ValidationException extends \Exception
{
    public function __construct(
        private readonly array $errors,
        string $message = 'Validation failed',
        int $code = 0,
        ?\Throwable $previous = null
    ) {
        parent::__construct($message, $code, $previous);
    }

    public function getErrors(): array
    {
        return $this->errors;
    }
}

// Exception handling with logging
class UserController
{
    public function create(Request $request): Response
    {
        try {
            $user = $this->userService->create($request->getData());
            return new JsonResponse($user->toArray(), 201);
        } catch (ValidationException $e) {
            $this->logger->info('Validation failed', [
                'errors' => $e->getErrors(),
                'input' => $request->getData()
            ]);
            return new JsonResponse(['errors' => $e->getErrors()], 400);
        } catch (\Throwable $e) {
            $this->logger->error('Unexpected error in user creation', [
                'exception' => $e->getMessage(),
                'trace' => $e->getTraceAsString()
            ]);
            return new JsonResponse(['error' => 'Internal server error'], 500);
        }
    }
}
```

### Version Control Integration

```bash
# Composer dependency management
composer install --no-dev --optimize-autoloader

# Code quality tools
composer require --dev phpunit/phpunit
composer require --dev psalm/psalm
composer require --dev phpstan/phpstan
composer require --dev friendsofphp/php-cs-fixer

# Git hooks for quality checks
#!/bin/sh
# .git/hooks/pre-commit
./vendor/bin/php-cs-fixer fix --dry-run --diff
./vendor/bin/psalm
./vendor/bin/phpunit
```

## 3. Communication Standards

### Documentation

```php
<?php

/**
 * User management service.
 *
 * Handles user creation, validation, and business logic operations.
 * Implements user domain rules and coordinates with repository layer.
 *
 * @package App\Service
 * @author Development Team
 * @since 1.0.0
 */
class UserService
{
    /**
     * Create new user with validation.
     *
     * Validates user data according to business rules and creates
     * new user entity. Sends welcome email and logs the action.
     *
     * @param array $userData User data array
     * @return User Created user instance
     * @throws ValidationException When validation fails
     * @throws \RuntimeException When user creation fails
     * 
     * @example
     * $user = $service->createUser([
     *     'name' => 'John Doe',
     *     'email' => 'john@example.com'
     * ]);
     */
    public function createUser(array $userData): User
    {
        // Implementation
    }
}
```

### API Design

```php
<?php

// RESTful API controller
class UserApiController
{
    /**
     * @Route("/api/users", methods={"POST"})
     */
    public function create(Request $request): JsonResponse
    {
        $validator = new UserValidator();
        $data = json_decode($request->getContent(), true);
        
        if (!$validator->validate($data)) {
            return new JsonResponse([
                'errors' => $validator->getErrors()
            ], 400);
        }
        
        try {
            $user = $this->userService->create($data);
            
            return new JsonResponse([
                'data' => $user->toArray(),
                'message' => 'User created successfully'
            ], 201);
        } catch (\Exception $e) {
            return new JsonResponse([
                'error' => 'Failed to create user'
            ], 500);
        }
    }

    /**
     * @Route("/api/users/{id}", methods={"GET"})
     */
    public function show(int $id): JsonResponse
    {
        try {
            $user = $this->userService->findById($id);
            
            return new JsonResponse([
                'data' => $user->toArray()
            ]);
        } catch (UserNotFoundException $e) {
            return new JsonResponse([
                'error' => 'User not found'
            ], 404);
        }
    }
}
```

## 4. Quality Assurance

### Testing Standards

```php
<?php

use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\MockObject\MockObject;

class UserServiceTest extends TestCase
{
    private UserService $userService;
    private UserRepositoryInterface|MockObject $userRepository;
    private LoggerInterface|MockObject $logger;

    protected function setUp(): void
    {
        $this->userRepository = $this->createMock(UserRepositoryInterface::class);
        $this->logger = $this->createMock(LoggerInterface::class);
        $this->userService = new UserService($this->userRepository, $this->logger);
    }

    /**
     * @dataProvider validUserDataProvider
     */
    public function testCreateUserWithValidData(array $userData, array $expected): void
    {
        $this->userRepository
            ->expects($this->once())
            ->method('save')
            ->willReturn(new User($expected));

        $result = $this->userService->create($userData);

        $this->assertInstanceOf(User::class, $result);
        $this->assertEquals($expected['email'], $result->getEmail());
    }

    public function validUserDataProvider(): array
    {
        return [
            'standard user' => [
                ['name' => 'John Doe', 'email' => 'john@example.com'],
                ['id' => 1, 'name' => 'John Doe', 'email' => 'john@example.com']
            ],
            'user with special characters' => [
                ['name' => 'José María', 'email' => 'jose@example.com'],
                ['id' => 2, 'name' => 'José María', 'email' => 'jose@example.com']
            ]
        ];
    }

    public function testFindByIdThrowsExceptionWhenUserNotFound(): void
    {
        $this->userRepository
            ->expects($this->once())
            ->method('findById')
            ->with(999)
            ->willReturn(null);

        $this->expectException(UserNotFoundException::class);
        $this->expectExceptionMessage('User with ID 999 not found');

        $this->userService->findById(999);
    }
}
```

### Code Quality Tools

```bash
# PHPUnit testing
./vendor/bin/phpunit --coverage-html coverage

# Static analysis with Psalm
./vendor/bin/psalm --show-info=true

# Static analysis with PHPStan
./vendor/bin/phpstan analyse src tests --level=8

# Code style fixing
./vendor/bin/php-cs-fixer fix --rules=@PSR12

# Security scanning
composer audit
```

## 5. Security and Performance

### Security Best Practices

```php
<?php

class UserController
{
    // Input validation and sanitization
    public function create(Request $request): Response
    {
        $data = $request->validated(); // Use framework validation
        
        // Sanitize input
        $data['name'] = filter_var($data['name'], FILTER_SANITIZE_STRING);
        $data['email'] = filter_var($data['email'], FILTER_SANITIZE_EMAIL);
        
        // Validate email format
        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            throw new ValidationException(['email' => 'Invalid email format']);
        }
        
        return $this->userService->create($data);
    }

    // SQL injection prevention
    public function search(string $query): array
    {
        $stmt = $this->pdo->prepare(
            'SELECT * FROM users WHERE name LIKE :query OR email LIKE :query'
        );
        
        $stmt->execute(['query' => '%' . $query . '%']);
        
        return $stmt->fetchAll(\PDO::FETCH_ASSOC);
    }

    // CSRF protection
    public function update(Request $request, int $id): Response
    {
        if (!$request->hasValidCsrfToken()) {
            throw new SecurityException('Invalid CSRF token');
        }
        
        // Process update
    }

    // Rate limiting
    public function login(Request $request): Response
    {
        $rateLimiter = new RateLimiter();
        $key = 'login_' . $request->getClientIp();
        
        if ($rateLimiter->tooManyAttempts($key, 5)) {
            throw new TooManyAttemptsException('Too many login attempts');
        }
        
        // Process login
        $rateLimiter->hit($key);
    }
}
```

### Performance Optimization

```php
<?php

// Database query optimization
class UserRepository
{
    // Eager loading to prevent N+1 queries
    public function getUsersWithProfiles(): array
    {
        return $this->db->query('
            SELECT u.*, p.bio, p.avatar 
            FROM users u 
            LEFT JOIN profiles p ON u.id = p.user_id
        ')->fetchAll();
    }

    // Pagination for large datasets
    public function getPaginated(int $page, int $limit = 20): array
    {
        $offset = ($page - 1) * $limit;
        
        $stmt = $this->db->prepare('
            SELECT * FROM users 
            ORDER BY created_at DESC 
            LIMIT :limit OFFSET :offset
        ');
        
        $stmt->bindValue(':limit', $limit, \PDO::PARAM_INT);
        $stmt->bindValue(':offset', $offset, \PDO::PARAM_INT);
        $stmt->execute();
        
        return $stmt->fetchAll();
    }

    // Query result caching
    public function getById(int $id): ?User
    {
        $cacheKey = "user_{$id}";
        
        if ($cached = $this->cache->get($cacheKey)) {
            return $cached;
        }
        
        $user = $this->findUserById($id);
        
        if ($user) {
            $this->cache->set($cacheKey, $user, 3600); // 1 hour
        }
        
        return $user;
    }
}

// Memory optimization
class DataProcessor
{
    // Generator for large datasets
    public function processLargeDataset(string $filename): \Generator
    {
        $handle = fopen($filename, 'r');
        
        while (($line = fgets($handle)) !== false) {
            yield trim($line);
        }
        
        fclose($handle);
    }

    // Batch processing
    public function processBatch(array $items, int $batchSize = 100): void
    {
        $batches = array_chunk($items, $batchSize);
        
        foreach ($batches as $batch) {
            $this->processBatchItems($batch);
            
            // Free memory between batches
            gc_collect_cycles();
        }
    }
}
```

## 6. Language-Specific Standards

### Modern PHP Features

```php
<?php

// PHP 8+ features usage
class UserService
{
    // Constructor property promotion
    public function __construct(
        private readonly UserRepositoryInterface $repository,
        private readonly EventDispatcherInterface $dispatcher,
    ) {
    }

    // Named arguments
    public function createUser(array $data): User
    {
        return new User(
            name: $data['name'],
            email: $data['email'],
            createdAt: new \DateTimeImmutable(),
        );
    }

    // Match expressions
    public function getUserStatus(User $user): string
    {
        return match ($user->getStatus()) {
            UserStatus::ACTIVE => 'User is active',
            UserStatus::INACTIVE => 'User is inactive',
            UserStatus::BANNED => 'User is banned',
            UserStatus::PENDING => 'User is pending verification',
            default => 'Unknown status',
        };
    }

    // Nullsafe operator
    public function getUserCountry(User $user): ?string
    {
        return $user->getProfile()?->getAddress()?->getCountry();
    }

    // Attributes (PHP 8+)
    #[Route('/users', methods: ['POST'])]
    #[RequireRole('admin')]
    public function createUser(Request $request): Response
    {
        // Implementation
    }
}

// Enums (PHP 8.1+)
enum UserStatus: string
{
    case ACTIVE = 'active';
    case INACTIVE = 'inactive';
    case BANNED = 'banned';
    case PENDING = 'pending';

    public function getLabel(): string
    {
        return match ($this) {
            self::ACTIVE => 'Active User',
            self::INACTIVE => 'Inactive User',
            self::BANNED => 'Banned User',
            self::PENDING => 'Pending Verification',
        };
    }
}
```

### Autoloading and Namespaces

```php
<?php

// composer.json autoloading configuration
{
    "autoload": {
        "psr-4": {
            "App\\": "src/",
            "App\\Tests\\": "tests/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "App\\Tests\\": "tests/"
        }
    }
}

// Proper namespace usage
namespace App\Service\User;

use App\Model\User;
use App\Repository\UserRepositoryInterface;
use App\Event\UserCreated;
use App\Exception\{UserNotFoundException, ValidationException};
use Psr\Log\LoggerInterface;

class UserManagementService
{
    // Implementation
}
```

## 7. Continuous Improvement

### Code Metrics

- **Cyclomatic Complexity:** Maximum 10 per method
- **Method Length:** Maximum 30 lines, prefer 15 lines
- **Class Length:** Maximum 400 lines, prefer 200 lines
- **Test Coverage:** Minimum 80%, target 90%
- **PSR Compliance:** 100% PSR-12 compliance

### Performance Benchmarks

```php
<?php

// Benchmarking class
class PerformanceBenchmark
{
    public function benchmarkUserCreation(): float
    {
        $start = microtime(true);
        
        for ($i = 0; $i < 1000; $i++) {
            $user = new User("User {$i}", "user{$i}@example.com");
        }
        
        return microtime(true) - $start;
    }

    public function benchmarkDatabaseQuery(): float
    {
        $start = microtime(true);
        
        $users = $this->userRepository->findAll();
        
        return microtime(true) - $start;
    }
}
```

### Code Review Checklist

- [ ] PSR-12 coding standards compliance
- [ ] Type declarations for all parameters and returns
- [ ] Proper exception handling with specific exceptions
- [ ] Input validation and sanitization
- [ ] SQL injection prevention
- [ ] Comprehensive unit tests
- [ ] Performance considerations
- [ ] Security vulnerabilities check
- [ ] Documentation for public methods
- [ ] Follows SOLID principles

## 8. AI-Specific Best Practices

### Code Generation Guidelines

1. **Always use strict types** (`declare(strict_types=1)`)
2. **Implement proper error handling** with specific exceptions
3. **Follow PSR standards** (PSR-4, PSR-12, PSR-7)
4. **Use modern PHP features** (8.0+ syntax when possible)
5. **Include comprehensive tests** for all generated code

### Integration Patterns

```php
<?php

// Configuration management
class ConfigManager
{
    private array $config;

    public function __construct(string $configPath)
    {
        if (!file_exists($configPath)) {
            throw new \RuntimeException("Config file not found: {$configPath}");
        }

        $this->config = require $configPath;
    }

    public function get(string $key, mixed $default = null): mixed
    {
        return $this->config[$key] ?? $default;
    }
}

// Dependency injection container
class Container
{
    private array $bindings = [];
    private array $instances = [];

    public function bind(string $abstract, \Closure $concrete): void
    {
        $this->bindings[$abstract] = $concrete;
    }

    public function singleton(string $abstract, \Closure $concrete): void
    {
        $this->bind($abstract, function () use ($abstract, $concrete) {
            if (!isset($this->instances[$abstract])) {
                $this->instances[$abstract] = $concrete();
            }
            return $this->instances[$abstract];
        });
    }

    public function resolve(string $abstract): mixed
    {
        if (!isset($this->bindings[$abstract])) {
            throw new \RuntimeException("No binding found for {$abstract}");
        }

        return $this->bindings[$abstract]();
    }
}
```

### Build and Deployment

```bash
# Composer optimization
composer install --no-dev --optimize-autoloader --classmap-authoritative

# OPcache configuration (php.ini)
opcache.enable=1
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=2
opcache.fast_shutdown=1

# Docker deployment
FROM php:8.2-fpm-alpine

RUN docker-php-ext-install pdo pdo_mysql opcache

COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader

COPY . .

EXPOSE 9000
CMD ["php-fpm"]
```

This comprehensive PHP standard ensures AI agents generate high-quality, secure, performant, and maintainable PHP code following modern PHP practices and PSR standards.
