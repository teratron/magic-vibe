# YAGNI Principle

> **Magic Vibe Rule: You Aren't Gonna Need It**  
> **Category:** Principles  
> **Priority:** High  
> **File Size:** ~12KB (AI-optimized)  
> **Dependencies:** `@rules/principles/kiss.md`, `@rules/principles/dry.md`

YAGNI (You Aren't Gonna Need It) principle guide for avoiding over-engineering and unnecessary features. Essential for AI agents to focus on current requirements without speculative implementation.

## 1. Implementation Guidelines

### 1.1. Core YAGNI Concept

**Definition:** Don't implement functionality until you actually need it, even if you think you'll need it in the future.

**Key Aspects:**

- **Current Requirements**: Focus only on what's needed now
- **Avoid Speculation**: Don't build for hypothetical future needs
- **Incremental Development**: Add features when they become necessary
- **Reduced Complexity**: Less code means fewer bugs and easier maintenance

### 1.2. Common YAGNI Violations

**Over-Flexible Configurations:**

```python

# ❌ Bad: Over-engineered configuration

class DatabaseConfiguration:
    def **init**(self):
        self.host = "localhost"
        self.port = 5432
        self.ssl_mode = "prefer"
        self.connection_timeout = 30
        self.pool_size = 10
        self.max_overflow = 20
        # ... 20 more options that might never be used

# ✅ Good: Simple configuration for current needs

class DatabaseConfig:
    def **init**(self):
        self.host = "localhost"
        self.port = 5432
        self.database = "myapp"
        self.username = "user"
        self.password = "password"

    # Add more options only when actually needed
```

**Premature Abstraction:**

```python
# ❌ Bad: Abstract classes for unclear future needs
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, method): pass
    
    @abstractmethod
    def schedule_payment(self, amount, method, date): pass  # Not needed yet
    
    @abstractmethod
    def create_payment_plan(self, total, installments): pass  # Not needed yet

# ✅ Good: Simple implementation for current needs
class PaymentService:
    def __init__(self, stripe_api_key):
        self.stripe_api_key = stripe_api_key
    
    def process_payment(self, amount, payment_method):
        """Process payment using Stripe."""
        # Direct implementation for current needs
        pass

# Add abstraction only when multiple payment processors are needed
```

### 1.3. Over-Generalized Functions

```python
# ❌ Bad: Over-generalized for unclear future needs

def process_data(data, processor_type='default', options=None,
                transformers=None, validators=None, filters=None,
                output_format='json', cache_enabled=True,
                async_mode=False, batch_size=100, retry_count=3):
    # Complex implementation handling all possible scenarios
    pass

# ✅ Good: Specific function for current need

def validate_user_data(user_data):
    """Validate user registration data."""
    if not user_data.get('email'):
        raise ValueError("Email is required")
    if not user_data.get('password'):
        raise ValueError("Password is required")
    return True

def transform_user_data(user_data):
    """Transform user data to database format."""
    return {
        'email': user_data['email'].lower(),
        'password_hash': hash_password(user_data['password']),
        'created_at': datetime.now()
    }
```

### 1.4. When to Add Complexity

**Clear, Immediate Requirements:**

```python
# ✅ Add complexity when requirement is clear and current
class OrderService:
    def create_order(self, user_id, items, shipping_address):
        # Shipping address is required NOW for current sprint
        order = Order(user_id, items, shipping_address)
        return self.order_repository.save(order)
```

**Multiple Current Use Cases:**

```python
# ✅ Add abstraction when you have multiple actual implementations
class NotificationService:
    def __init__(self, email_sender, sms_sender):
        self.email_sender = email_sender  # Both needed NOW
        self.sms_sender = sms_sender      # Both needed NOW
    
    def send_notification(self, message, recipient, method):
        if method == 'email':
            self.email_sender.send(message, recipient)
        elif method == 'sms':
            self.sms_sender.send(message, recipient)
```

## 2. Change Management Protocols

### 2.1. Incremental Development

**YAGNI Refactoring Process:**

1. **Start Simple** - Implement minimal viable solution
2. **Add When Needed** - Extend functionality based on real requirements
3. **Refactor Gradually** - Improve code as new needs emerge
4. **Remove Unused Code** - Clean up speculative implementations

### 2.2. Feature Evolution

```python
# Start simple

class OrderService:
    def create_order(self, user_id, items):
        order = Order(user_id, items)
        return self.order_repository.save(order)

# When email notification is actually needed, add it

class OrderService:
    def **init**(self, order_repository, email_service):
        self.order_repository = order_repository
        self.email_service = email_service  # Added when needed

    def create_order(self, user_id, items):
        order = Order(user_id, items)
        saved_order = self.order_repository.save(order)
        self.email_service.send_order_confirmation(saved_order)
        return saved_order
```

### 2.3. Database Schema Evolution

```sql
-- Start with minimal schema
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Add columns only when features require them
ALTER TABLE users ADD COLUMN first_name VARCHAR(100);
```

## 3. Communication Standards

### 3.1. Documentation Guidelines

```python
class UserService:
    """
    Service for basic user operations.
    
    Currently supports:
    - User creation
    - User authentication
    
    Note: Additional features will be added when required.
    """
    
    def create_user(self, email: str, password: str) -> User:
        """Create a new user account."""
        pass
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password."""
        pass

# Don't document methods that don't exist
```

### 3.2. Requirements Communication

**Clear Requirement Definition:**

- Document only current, confirmed requirements
- Avoid speculative "what if" scenarios
- Focus on immediate business value
- Update documentation as requirements evolve

### 3.3. Code Review Standards

**YAGNI Code Review Questions:**

- Is this feature required for current sprint?
- Are we solving an actual existing problem?
- Can this be simplified further?
- Are we adding complexity for uncertain future needs?

## 4. Quality Assurance Framework

### 4.1. Test What Exists

```python
class TestUserService:
    def test_create_user(self):
        user_service = UserService()
        user = user_service.create_user("<test@example.com>", "password123")

        assert user.email == "test@example.com"
        assert user.verify_password("password123")
        assert user.created_at is not None

    def test_authenticate_user_success(self):
        user_service = UserService()
        user_service.create_user("test@example.com", "password123")
        
        authenticated_user = user_service.authenticate_user("test@example.com", "password123")
        assert authenticated_user is not None

# Don't write tests for features that don't exist yet
```

### 4.2. YAGNI Validation Checklist

**Before implementing any feature, ask:**

- [ ] Is this feature required for the current user story?
- [ ] Do we have specific requirements for this functionality?
- [ ] Is this being added "just in case"?
- [ ] Would the system work without this feature for now?
- [ ] Are we solving a problem that actually exists?
- [ ] Can this be added later when actually needed?

### 4.3. Code Quality Metrics

**YAGNI Compliance Metrics:**

- **Feature Utilization**: Track which features are actually used
- **Code Coverage**: Focus on testing implemented features
- **Complexity Score**: Measure unnecessary complexity
- **Refactoring Frequency**: Track when features are added/removed

## 5. Security & Performance Guidelines

### 5.1. Avoid Premature Optimization

```python
# ❌ Bad: Premature caching and optimization
class UserService:
    def __init__(self):
        self.cache = {}  # Added "just in case"
        self.connection_pool = ConnectionPool(size=100)  # Over-sized

# ✅ Good: Simple implementation first
class UserService:
    def get_user(self, user_id):
        return self.user_repository.find_by_id(user_id)

# Add caching only when performance becomes an actual problem
```

### 5.2. Security Implementation

```python
# ✅ Implement security for current needs
class AuthService:
    def authenticate(self, email, password):
        user = self.user_repository.find_by_email(email)
        if user and self.verify_password(password, user.password_hash):
            return self.create_session(user)
        raise AuthenticationError("Invalid credentials")

# Don't add OAuth, 2FA, etc. until actually required
```

## 6. Integration & Compatibility

### 6.1. Simple Framework Integration

```python
# ✅ Start with simple integration
class APIController:
    def __init__(self, user_service):
        self.user_service = user_service
    
    def create_user(self, request):
        try:
            user = self.user_service.create_user(request.email, request.password)
            return {'success': True, 'user_id': user.id}
        except ValueError as e:
            return {'success': False, 'error': str(e)}

# Add middleware, validation, serialization only when needed
```

### 6.2. Third-Party Integration

```python
# ✅ Direct integration for current needs
class EmailService:
    def __init__(self, smtp_config):
        self.smtp_config = smtp_config
    
    def send_welcome_email(self, user_email):
        # Direct SMTP implementation
        pass

# Add email service abstraction only when multiple providers needed
```

## 7. Monitoring & Maintenance

### 7.1. Feature Usage Monitoring

```python
# Track what features are actually used
class FeatureUsageTracker:
    def track_feature_usage(self, feature_name, user_id):
        # Simple logging for current needs
        logger.info(f"Feature {feature_name} used by {user_id}")

# Add complex analytics only when business requires it
```

### 7.2. Code Maintenance

**Regular YAGNI Reviews:**

- Monthly review of unused code
- Quarterly assessment of speculative features
- Remove features that haven't been used
- Simplify over-engineered solutions

### 7.3. Refactoring Strategy

**Incremental Improvement:**

- Refactor when adding new features
- Simplify complex code during bug fixes
- Extract abstractions when second use case appears
- Remove dead code during regular maintenance

## 8. AI Agent Optimization

### 8.1. AI-Friendly YAGNI Patterns

```python
# ✅ Clear patterns for AI recognition
class SimpleUserService:
    """Minimal user service for current requirements only."""
    
    def create_user(self, email: str, password: str) -> User:
        """Create user - implements only current requirement."""
        return User(email=email, password_hash=hash_password(password))
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user - basic implementation."""
        user = self.find_user_by_email(email)
        if user and verify_password(password, user.password_hash):
            return user
        return None
    
    # NOTE: Add methods only when requirements emerge
```

### 8.2. AI Code Generation Guidelines

**For AI agents applying YAGNI:**

- Generate minimal viable implementations
- Avoid adding "convenience" methods without requirements
- Focus on current user story requirements
- Don't implement abstract base classes prematurely
- Keep configuration simple and focused

### 8.3. Anti-Patterns Recognition

**AI should avoid generating:**

- Over-flexible configuration systems
- Premature abstractions
- Speculative feature flags
- Unused optional parameters
- Complex inheritance hierarchies for single use cases

### 8.4. YAGNI Validation for AI

**AI agents must verify:**

- [ ] Each feature addresses current requirements
- [ ] No speculative "future-proofing" code
- [ ] Configuration includes only necessary options
- [ ] Tests cover implemented features only
- [ ] Documentation matches actual implementation

---

**Magic Vibe YAGNI Principle v2.1.0** - Lean, focused development

**Last Updated:** 2025-09-08 | **File Size:** ~12KB | **Status:** Active*
