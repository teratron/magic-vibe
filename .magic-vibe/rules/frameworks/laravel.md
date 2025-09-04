---
description: Laravel framework development rules for PHP web applications with MVC architecture, Eloquent ORM, and modern PHP practices.
globs: "artisan,composer.json,app/**/*.php,routes/**/*.php,database/**/*.php,resources/views/**/*.blade.php"
alwaysApply: false
priority: 3
---

# Laravel Framework Rules

Laravel development standards for building robust, scalable web applications with PHP.

## Core Laravel Principles

### MVC Architecture

- **Models:** Eloquent ORM for database interactions
- **Views:** Blade templating engine with reusable components
- **Controllers:** Thin controllers with business logic in services
- **Routes:** RESTful routing with resource controllers

### Service Container & Dependency Injection

```php
// Bind services in AppServiceProvider
public function register(): void
{
    $this->app->bind(UserRepositoryInterface::class, EloquentUserRepository::class);
    $this->app->singleton(CacheService::class);
}

// Inject dependencies in constructors
class UserController extends Controller
{
    public function __construct(
        private readonly UserRepositoryInterface $userRepository,
        private readonly CacheService $cache
    ) {}
}
```

## Eloquent ORM Best Practices

### Model Design

```php
class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    protected $fillable = ['name', 'email', 'email_verified_at'];
    
    protected $hidden = ['password', 'remember_token'];
    
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
            'settings' => 'json',
        ];
    }
    
    // Relationships
    public function posts(): HasMany
    {
        return $this->hasMany(Post::class);
    }
    
    // Scopes
    public function scopeActive(Builder $query): void
    {
        $query->where('is_active', true);
    }
}
```

### Query Optimization

```php
// Use eager loading to prevent N+1 queries
$users = User::with(['posts', 'profile'])->get();

// Use chunks for large datasets
User::chunk(100, function (Collection $users) {
    foreach ($users as $user) {
        // Process user
    }
});

// Use database transactions
DB::transaction(function () {
    User::create($userData);
    Profile::create($profileData);
});
```

## Request Handling

### Form Requests

```php
class StoreUserRequest extends FormRequest
{
    public function authorize(): bool
    {
        return auth()->user()->can('create-users');
    }
    
    public function rules(): array
    {
        return [
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'email', 'unique:users'],
            'password' => ['required', 'min:8', 'confirmed'],
        ];
    }
    
    public function messages(): array
    {
        return [
            'email.unique' => 'This email is already registered.',
        ];
    }
}
```

### API Resources

```php
class UserResource extends JsonResource
{
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'created_at' => $this->created_at->toISOString(),
            'posts' => PostResource::collection($this->whenLoaded('posts')),
        ];
    }
}
```

## Service Layer Pattern

### Service Classes

```php
class UserService
{
    public function __construct(
        private readonly UserRepositoryInterface $userRepository,
        private readonly EmailService $emailService
    ) {}
    
    public function createUser(array $data): User
    {
        DB::beginTransaction();
        
        try {
            $user = $this->userRepository->create($data);
            $this->emailService->sendWelcomeEmail($user);
            
            DB::commit();
            return $user;
        } catch (Exception $e) {
            DB::rollBack();
            throw new UserCreationException('Failed to create user', 0, $e);
        }
    }
}
```

## Testing Standards

### Feature Tests

```php
class UserControllerTest extends TestCase
{
    use RefreshDatabase;
    
    public function test_user_can_be_created(): void
    {
        $userData = [
            'name' => 'John Doe',
            'email' => 'john@example.com',
            'password' => 'password123',
            'password_confirmation' => 'password123',
        ];
        
        $response = $this->post('/api/users', $userData);
        
        $response->assertStatus(201)
                ->assertJsonStructure(['data' => ['id', 'name', 'email']]);
                
        $this->assertDatabaseHas('users', [
            'email' => 'john@example.com',
        ]);
    }
}
```

### Unit Tests

```php
class UserServiceTest extends TestCase
{
    public function test_creates_user_with_valid_data(): void
    {
        $userRepository = Mockery::mock(UserRepositoryInterface::class);
        $emailService = Mockery::mock(EmailService::class);
        
        $userData = ['name' => 'John', 'email' => 'john@test.com'];
        $user = new User($userData);
        
        $userRepository->shouldReceive('create')
                      ->once()
                      ->with($userData)
                      ->andReturn($user);
                      
        $emailService->shouldReceive('sendWelcomeEmail')
                    ->once()
                    ->with($user);
        
        $service = new UserService($userRepository, $emailService);
        $result = $service->createUser($userData);
        
        $this->assertEquals($user, $result);
    }
}
```

## Security Best Practices

### Authentication & Authorization

```php
// Use Laravel Sanctum for API authentication
Route::middleware('auth:sanctum')->group(function () {
    Route::apiResource('users', UserController::class);
});

// Policy-based authorization
class UserPolicy
{
    public function update(User $user, User $targetUser): bool
    {
        return $user->id === $targetUser->id || $user->hasRole('admin');
    }
}

// Controller authorization
public function update(UpdateUserRequest $request, User $user): JsonResponse
{
    $this->authorize('update', $user);
    // Update logic
}
```

### Input Validation & Sanitization

```php
// Always validate input
$request->validate([
    'content' => ['required', 'string', 'max:1000'],
    'category_id' => ['required', 'exists:categories,id'],
]);

// Use mass assignment protection
protected $fillable = ['title', 'content', 'category_id'];
protected $guarded = ['id', 'user_id', 'created_at'];
```

## Performance Optimization

### Caching

```php
// Cache expensive queries
$popularPosts = Cache::remember('popular_posts', 3600, function () {
    return Post::with('author')
              ->where('views', '>', 1000)
              ->orderBy('views', 'desc')
              ->take(10)
              ->get();
});

// Cache tags for invalidation
Cache::tags(['posts', 'popular'])->put('popular_posts', $posts, 3600);
Cache::tags(['posts'])->flush(); // Invalidate all post-related cache
```

### Queue Jobs

```php
class SendWelcomeEmail implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;
    
    public function __construct(
        private readonly User $user
    ) {}
    
    public function handle(EmailService $emailService): void
    {
        $emailService->sendWelcomeEmail($this->user);
    }
    
    public function failed(Throwable $exception): void
    {
        Log::error('Failed to send welcome email', [
            'user_id' => $this->user->id,
            'error' => $exception->getMessage(),
        ]);
    }
}
```

## Database Management

### Migrations

```php
// Create migration with proper structure
public function up(): void
{
    Schema::create('posts', function (Blueprint $table) {
        $table->id();
        $table->string('title');
        $table->text('content');
        $table->foreignId('user_id')->constrained()->onDelete('cascade');
        $table->foreignId('category_id')->constrained();
        $table->boolean('is_published')->default(false);
        $table->timestamp('published_at')->nullable();
        $table->timestamps();
        
        $table->index(['is_published', 'published_at']);
        $table->fullText(['title', 'content']);
    });
}
```

### Factories & Seeders

```php
class UserFactory extends Factory
{
    protected $model = User::class;
    
    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'email' => fake()->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => Hash::make('password'),
        ];
    }
}

// Use in tests and seeding
User::factory()->count(50)->create();
```

## API Development

### Resource Controllers

```php
class PostController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $posts = Post::query()
            ->when($request->search, fn($q) => $q->where('title', 'like', "%{$request->search}%"))
            ->when($request->category, fn($q) => $q->where('category_id', $request->category))
            ->with(['author', 'category'])
            ->paginate(15);
            
        return PostResource::collection($posts)->response();
    }
    
    public function store(StorePostRequest $request): JsonResponse
    {
        $post = Post::create($request->validated());
        
        return new PostResource($post->load(['author', 'category']));
    }
}
```

## Error Handling

### Custom Exceptions

```php
class UserNotFoundException extends Exception
{
    public function render(Request $request): JsonResponse
    {
        return response()->json([
            'error' => 'User not found',
            'message' => $this->getMessage(),
        ], 404);
    }
}

// Global exception handler
public function render($request, Throwable $exception): Response
{
    if ($request->expectsJson()) {
        return $this->handleApiException($request, $exception);
    }
    
    return parent::render($request, $exception);
}
```

## Artisan Commands

### Custom Commands

```php
class ImportUsersCommand extends Command
{
    protected $signature = 'users:import {file : CSV file path}';
    protected $description = 'Import users from CSV file';
    
    public function handle(): int
    {
        $file = $this->argument('file');
        
        if (!file_exists($file)) {
            $this->error('File not found');
            return Command::FAILURE;
        }
        
        $this->info('Starting import...');
        $bar = $this->output->createProgressBar();
        
        // Import logic with progress bar
        
        $this->info('Import completed successfully');
        return Command::SUCCESS;
    }
}
```

## Configuration Management

### Environment Configuration

```php
// Use config() helper for all configuration
$apiKey = config('services.stripe.key');
$cacheTtl = config('cache.default_ttl', 3600);

// Type-safe configuration
class ApiConfig
{
    public function __construct(
        public readonly string $stripeKey,
        public readonly int $rateLimitPerMinute,
        public readonly bool $debugMode,
    ) {}
    
    public static function fromConfig(): self
    {
        return new self(
            stripeKey: config('services.stripe.key'),
            rateLimitPerMinute: config('api.rate_limit', 60),
            debugMode: config('app.debug', false),
        );
    }
}
```

## Code Quality Standards

### Code Organization

- Follow PSR-12 coding standards
- Use meaningful class and method names
- Keep controllers thin, move business logic to services
- Use type declarations for all parameters and return types
- Document complex business logic with PHPDoc

### Performance Guidelines

- Use eager loading to prevent N+1 queries
- Implement proper caching strategies
- Use database indexes for frequently queried columns
- Optimize large data processing with chunks and queues
- Monitor and profile application performance regularly

### Security Checklist

- Validate and sanitize all input data
- Use parameterized queries (Eloquent handles this)
- Implement proper authentication and authorization
- Protect against CSRF attacks (enabled by default)
- Use HTTPS in production environments
- Keep dependencies updated and scan for vulnerabilities
