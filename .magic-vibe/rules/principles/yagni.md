---
description: YAGNI (You Aren't Gonna Need It) principle guide for avoiding over-engineering and unnecessary features.
globs:
alwaysApply: true
---

# YAGNI Principle (You Aren't Gonna Need It)

Whenever you use this rule, start your message with the following:

"Applying YAGNI principle..."

This rule ensures that features and code are only implemented when they are actually needed, not when you think they might be needed in the future. YAGNI prevents over-engineering and keeps codebases lean and maintainable.

## Core YAGNI Concept

**Definition:** Don't implement functionality until you actually need it, even if you think you'll need it in the future.

**Key Aspects:**

- **Current Requirements**: Focus only on what's needed now
- **Avoid Speculation**: Don't build for hypothetical future needs
- **Incremental Development**: Add features when they become necessary
- **Reduced Complexity**: Less code means fewer bugs and easier maintenance

## Common YAGNI Violations

### 1. Over-Flexible Configurations

```python
# ❌ Bad: Over-engineered configuration system
class DatabaseConfiguration:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.database = "myapp"
        self.username = "user"
        self.password = "password"
        self.ssl_mode = "prefer"
        self.connection_timeout = 30
        self.read_timeout = 60
        self.write_timeout = 60
        self.pool_size = 10
        self.max_overflow = 20
        self.pool_recycle = 3600
        self.pool_pre_ping = True
        self.isolation_level = "READ_COMMITTED"
        self.autocommit = False
        self.encoding = "utf-8"
        self.timezone = "UTC"
        # ... 20 more configuration options that might never be used

# ✅ Good: Simple configuration for current needs
class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.database = "myapp"
        self.username = "user"
        self.password = "password"
    
    # Add more options only when actually needed
```

### 2. Premature Abstraction

```python
# ❌ Bad: Abstract base classes for unclear future needs
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, method): pass
    
    @abstractmethod
    def refund_payment(self, transaction_id, amount): pass
    
    @abstractmethod
    def validate_payment_method(self, method): pass
    
    @abstractmethod
    def get_supported_currencies(self): pass
    
    @abstractmethod
    def calculate_fees(self, amount, method): pass
    
    @abstractmethod
    def schedule_payment(self, amount, method, date): pass  # Not needed yet
    
    @abstractmethod
    def create_payment_plan(self, total, installments): pass  # Not needed yet

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount, method):
        # Implementation
        pass
    
    def refund_payment(self, transaction_id, amount):
        # Implementation
        pass
    
    # Forced to implement methods we don't need yet
    def schedule_payment(self, amount, method, date):
        raise NotImplementedError("Not implemented yet")
    
    def create_payment_plan(self, total, installments):
        raise NotImplementedError("Not implemented yet")

# ✅ Good: Simple implementation for current needs
class PaymentService:
    def __init__(self, stripe_api_key):
        self.stripe_api_key = stripe_api_key
    
    def process_payment(self, amount, payment_method):
        """Process payment using Stripe."""
        # Direct implementation for current needs
        pass
    
    def refund_payment(self, transaction_id, amount):
        """Process refund using Stripe."""
        # Direct implementation
        pass

# Add abstraction only when we actually need multiple payment processors
```

### 3. Over-Generalized Functions

```python
# ❌ Bad: Over-generalized for unclear future needs
def process_data(data, processor_type='default', options=None, 
                transformers=None, validators=None, filters=None,
                output_format='json', cache_enabled=True, 
                async_mode=False, batch_size=100, retry_count=3):
    """
    Universal data processor that can handle any type of data processing.
    Most of these parameters will never be used.
    """
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

# Add more specific processing functions only when needed
```

### 4. Unnecessary Feature Flags

```python
# ❌ Bad: Too many speculative feature flags
class FeatureFlags:
    ENABLE_NEW_DASHBOARD = True
    ENABLE_ADVANCED_SEARCH = False
    ENABLE_RECOMMENDATION_ENGINE = False  # Might never be built
    ENABLE_SOCIAL_LOGIN = False  # Not in current roadmap
    ENABLE_DARK_MODE = False  # Nice to have someday
    ENABLE_MOBILE_APP_INTEGRATION = False  # Uncertain future
    ENABLE_ANALYTICS_TRACKING = True
    ENABLE_A_B_TESTING = False  # Might need later
    ENABLE_CHAT_SUPPORT = False  # Under consideration
    # ... 20 more flags for features that might never exist

# ✅ Good: Feature flags only for features in development
class FeatureFlags:
    ENABLE_NEW_DASHBOARD = True  # Currently being rolled out
    ENABLE_ANALYTICS_TRACKING = True  # Currently in use

# Add new flags only when you start working on the feature
```

## YAGNI Best Practices

### 1. Implement for Current Stories

```python
# ✅ Good: Implement exactly what the current user story requires
class User:
    def __init__(self, email, password):
        self.email = email
        self.password_hash = hash_password(password)
        self.created_at = datetime.now()
    
    def verify_password(self, password):
        return verify_password_hash(password, self.password_hash)

class UserService:
    def create_user(self, email, password):
        user = User(email, password)
        return self.user_repository.save(user)
    
    def authenticate_user(self, email, password):
        user = self.user_repository.find_by_email(email)
        if user and user.verify_password(password):
            return user
        return None

# Don't add methods like reset_password(), update_profile(), etc. 
# until they're actually needed
```

### 2. Refactor When Requirements Change

```python
# Start simple
class OrderService:
    def create_order(self, user_id, items):
        order = Order(user_id, items)
        return self.order_repository.save(order)

# When email notification is actually needed, then add it
class OrderService:
    def __init__(self, order_repository, email_service):
        self.order_repository = order_repository
        self.email_service = email_service  # Added when needed
    
    def create_order(self, user_id, items):
        order = Order(user_id, items)
        saved_order = self.order_repository.save(order)
        
        # Added email notification when requirement came up
        self.email_service.send_order_confirmation(saved_order)
        return saved_order
```

### 3. Avoid Premature Optimization

```python
# ❌ Bad: Premature caching and optimization
class UserService:
    def __init__(self):
        self.cache = {}  # Added "just in case"
        self.connection_pool = ConnectionPool(size=100)  # Over-sized
    
    def get_user(self, user_id):
        # Complex caching logic before knowing if it's needed
        if user_id in self.cache:
            return self.cache[user_id]
        
        user = self.user_repository.find_by_id(user_id)
        self.cache[user_id] = user  # Cache everything
        return user

# ✅ Good: Simple implementation first
class UserService:
    def get_user(self, user_id):
        return self.user_repository.find_by_id(user_id)

# Add caching only when performance becomes an actual problem
```

### 4. Database Design

```sql
-- ❌ Bad: Over-designed schema for uncertain futures
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    occupation VARCHAR(100),
    company VARCHAR(100),
    avatar_url VARCHAR(500),
    bio TEXT,
    preferences JSON,
    social_links JSON,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE,
    is_premium BOOLEAN DEFAULT FALSE,
    subscription_expires TIMESTAMP
    -- Many fields that might never be used
);

-- ✅ Good: Minimal schema for current needs
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Add columns only when features require them
```

## When to Add Complexity

### 1. Clear, Immediate Requirements

```python
# ✅ Add complexity when requirement is clear and current
class OrderService:
    def create_order(self, user_id, items, shipping_address):
        # Shipping address is required NOW for current sprint
        order = Order(user_id, items, shipping_address)
        return self.order_repository.save(order)
```

### 2. Multiple Current Use Cases

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

### 3. Proven Performance Requirements

```python
# ✅ Add caching when you have actual performance problems
class ProductService:
    def __init__(self):
        self.cache = {}  # Added because of measured performance issues
    
    def get_product(self, product_id):
        if product_id in self.cache:
            return self.cache[product_id]
        
        product = self.product_repository.find_by_id(product_id)
        self.cache[product_id] = product
        return product
```

## Testing YAGNI Code

### Test What Exists, Not What Might Exist

```python
class TestUserService:
    def test_create_user(self):
        user_service = UserService()
        user = user_service.create_user("test@example.com", "password123")
        
        assert user.email == "test@example.com"
        assert user.verify_password("password123")
        assert user.created_at is not None

    def test_authenticate_user_success(self):
        user_service = UserService()
        user_service.create_user("test@example.com", "password123")
        
        authenticated_user = user_service.authenticate_user("test@example.com", "password123")
        assert authenticated_user is not None

    def test_authenticate_user_failure(self):
        user_service = UserService()
        
        authenticated_user = user_service.authenticate_user("test@example.com", "wrong_password")
        assert authenticated_user is None

# Don't write tests for features that don't exist yet
```

## Documentation and YAGNI

### Document What Exists

```python
class UserService:
    """
    Service for basic user operations.
    
    Currently supports:
    - User creation
    - User authentication
    
    Note: Password reset, profile updates, and other features 
    will be added when required.
    """
    
    def create_user(self, email: str, password: str) -> User:
        """Create a new user account."""
        pass
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password."""
        pass

# Don't document methods that don't exist
```

## Validation Checklist

Before implementing any feature, ask:

- [ ] Is this feature required for the current user story/sprint?
- [ ] Do we have specific requirements for this functionality?
- [ ] Is this being added "just in case" or for actual current needs?
- [ ] Would the system work without this feature for now?
- [ ] Are we solving a problem that actually exists?
- [ ] Is this based on speculation about future needs?
- [ ] Can this be added later when actually needed?
- [ ] Does this add unnecessary complexity?
- [ ] Are we over-engineering the solution?
- [ ] Is this the simplest solution that works for current needs?

## Integration with Other Principles

YAGNI complements:

- **KISS principle**: Avoiding unnecessary features keeps code simple
- **DRY principle**: Less code means less duplication to worry about
- **SOLID principles**: Simpler code is easier to make SOLID
- **OOP principles**: Focus on core objects and their actual responsibilities

## Common YAGNI Challenges

### 1. "But What If..." Scenarios

```python
# ❌ Bad: Implementing for hypothetical scenarios
def calculate_price(base_price, discount=0, tax_rate=0.08, 
                  currency='USD', exchange_rate=1.0,
                  member_discount=0, seasonal_discount=0,
                  bulk_discount=0, loyalty_points=0):
    # Complex calculation for scenarios that may never happen
    pass

# ✅ Good: Implement for actual current scenario
def calculate_price(base_price, tax_rate=0.08):
    """Calculate price with tax for current needs."""
    return base_price * (1 + tax_rate)

# Add parameters only when those scenarios become real requirements
```

### 2. Framework Over-Selection

```python
# ❌ Bad: Choosing complex framework for simple needs
# Using heavyweight ORM for simple CRUD operations
# Using microservices architecture for small application
# Using complex state management for simple app state

# ✅ Good: Choose simple solutions for current needs
# Use simple database queries for basic operations
# Use monolithic architecture until scale requires separation
# Use simple variables/objects for straightforward state management
```

Remember: YAGNI doesn't mean never plan ahead or write extensible code. It means don't implement features until you actually need them. Focus on making the current requirements work well, and add complexity only when real requirements demand it.
