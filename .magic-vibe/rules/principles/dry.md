---
description: DRY (Don't Repeat Yourself) principle guide for eliminating code duplication and promoting code reusability.
globs:
alwaysApply: true
---

# DRY Principle (Don't Repeat Yourself)

Whenever you use this rule, start your message with the following:

"Applying DRY principle..."

This rule ensures that code duplication is minimized and knowledge is expressed in a single, authoritative place within the system. DRY promotes maintainability, reduces bugs, and improves code clarity.

## Core DRY Concept

**Definition:** Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**Key Aspects:**

- **Code Duplication**: Avoid repeating the same logic
- **Knowledge Duplication**: Don't duplicate business rules or constants
- **Process Duplication**: Eliminate repeated workflows or procedures
- **Documentation Duplication**: Single source of truth for specifications

## Types of Duplication to Avoid

### 1. Code Duplication

```python
# ❌ Bad: Repeated validation logic
class UserController:
    def create_user(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email is required")
        if '@' not in user_data.get('email', ''):
            raise ValueError("Invalid email format")
        if len(user_data.get('password', '')) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        # Create user logic
    
    def update_user(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email is required")
        if '@' not in user_data.get('email', ''):
            raise ValueError("Invalid email format")
        if user_data.get('password') and len(user_data.get('password', '')) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        # Update user logic

# ✅ Good: Extracted validation logic
class UserValidator:
    @staticmethod
    def validate_email(email):
        if not email:
            raise ValueError("Email is required")
        if '@' not in email:
            raise ValueError("Invalid email format")
    
    @staticmethod
    def validate_password(password):
        if password and len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
    
    @classmethod
    def validate_user_data(cls, user_data, require_password=True):
        cls.validate_email(user_data.get('email'))
        if require_password or user_data.get('password'):
            cls.validate_password(user_data.get('password'))

class UserController:
    def create_user(self, user_data):
        UserValidator.validate_user_data(user_data, require_password=True)
        # Create user logic
    
    def update_user(self, user_data):
        UserValidator.validate_user_data(user_data, require_password=False)
        # Update user logic
```

### 2. Configuration Duplication

```python
# ❌ Bad: Scattered configuration
class DatabaseService:
    def connect(self):
        host = "localhost"
        port = 5432
        database = "myapp"
        # Connection logic

class CacheService:
    def connect(self):
        host = "localhost"  # Duplicated
        port = 6379
        # Connection logic

# ✅ Good: Centralized configuration
class Config:
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 5432
    DATABASE_NAME = "myapp"
    
    CACHE_HOST = "localhost"
    CACHE_PORT = 6379
    
    # Alternative: Load from environment or config file
    @classmethod
    def from_env(cls):
        import os
        cls.DATABASE_HOST = os.getenv('DB_HOST', 'localhost')
        cls.DATABASE_PORT = int(os.getenv('DB_PORT', '5432'))
        # ... other config

class DatabaseService:
    def connect(self):
        host = Config.DATABASE_HOST
        port = Config.DATABASE_PORT
        database = Config.DATABASE_NAME
        # Connection logic

class CacheService:
    def connect(self):
        host = Config.CACHE_HOST
        port = Config.CACHE_PORT
        # Connection logic
```

### 3. Logic Duplication

```typescript
// ❌ Bad: Duplicated business logic
class OrderService {
    calculateTotal(items: OrderItem[]): number {
        let subtotal = 0;
        for (const item of items) {
            subtotal += item.price * item.quantity;
        }
        
        const tax = subtotal * 0.08; // 8% tax
        const shipping = subtotal > 100 ? 0 : 10; // Free shipping over $100
        
        return subtotal + tax + shipping;
    }
}

class InvoiceService {
    generateInvoice(items: OrderItem[]): Invoice {
        let subtotal = 0;
        for (const item of items) {
            subtotal += item.price * item.quantity;
        }
        
        const tax = subtotal * 0.08; // Duplicated tax calculation
        const shipping = subtotal > 100 ? 0 : 10; // Duplicated shipping logic
        
        const total = subtotal + tax + shipping;
        
        return new Invoice(subtotal, tax, shipping, total);
    }
}

// ✅ Good: Extracted business logic
class PricingCalculator {
    static TAX_RATE = 0.08;
    static FREE_SHIPPING_THRESHOLD = 100;
    static STANDARD_SHIPPING_COST = 10;
    
    static calculateSubtotal(items: OrderItem[]): number {
        return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }
    
    static calculateTax(subtotal: number): number {
        return subtotal * this.TAX_RATE;
    }
    
    static calculateShipping(subtotal: number): number {
        return subtotal >= this.FREE_SHIPPING_THRESHOLD ? 0 : this.STANDARD_SHIPPING_COST;
    }
    
    static calculateTotal(items: OrderItem[]): {
        subtotal: number;
        tax: number;
        shipping: number;
        total: number;
    } {
        const subtotal = this.calculateSubtotal(items);
        const tax = this.calculateTax(subtotal);
        const shipping = this.calculateShipping(subtotal);
        
        return {
            subtotal,
            tax,
            shipping,
            total: subtotal + tax + shipping
        };
    }
}

class OrderService {
    calculateTotal(items: OrderItem[]): number {
        return PricingCalculator.calculateTotal(items).total;
    }
}

class InvoiceService {
    generateInvoice(items: OrderItem[]): Invoice {
        const pricing = PricingCalculator.calculateTotal(items);
        return new Invoice(pricing.subtotal, pricing.tax, pricing.shipping, pricing.total);
    }
}
```

## DRY Techniques and Patterns

### 1. Extract Functions/Methods

```python
# ❌ Bad: Repeated formatting logic
def display_user_info(user):
    full_name = f"{user.first_name} {user.last_name}".strip()
    email_display = user.email.lower()
    phone_display = f"({user.phone[:3]}) {user.phone[3:6]}-{user.phone[6:]}" if len(user.phone) == 10 else user.phone
    print(f"Name: {full_name}, Email: {email_display}, Phone: {phone_display}")

def format_user_for_export(user):
    full_name = f"{user.first_name} {user.last_name}".strip()
    email_display = user.email.lower()
    phone_display = f"({user.phone[:3]}) {user.phone[3:6]}-{user.phone[6:]}" if len(user.phone) == 10 else user.phone
    return f"{full_name},{email_display},{phone_display}"

# ✅ Good: Extracted formatting functions
class UserFormatter:
    @staticmethod
    def format_full_name(user):
        return f"{user.first_name} {user.last_name}".strip()
    
    @staticmethod
    def format_email(email):
        return email.lower()
    
    @staticmethod
    def format_phone(phone):
        if len(phone) == 10:
            return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        return phone
    
    @classmethod
    def get_formatted_user_data(cls, user):
        return {
            'name': cls.format_full_name(user),
            'email': cls.format_email(user.email),
            'phone': cls.format_phone(user.phone)
        }

def display_user_info(user):
    data = UserFormatter.get_formatted_user_data(user)
    print(f"Name: {data['name']}, Email: {data['email']}, Phone: {data['phone']}")

def format_user_for_export(user):
    data = UserFormatter.get_formatted_user_data(user)
    return f"{data['name']},{data['email']},{data['phone']}"
```

### 2. Use Templates and Higher-Order Functions

```python
# ✅ Good: Template pattern for similar operations
class BaseRepository:
    def __init__(self, db_connection, table_name):
        self.db = db_connection
        self.table_name = table_name
    
    def find_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        return self.db.execute(query, (id,))
    
    def find_by_field(self, field_name, value):
        query = f"SELECT * FROM {self.table_name} WHERE {field_name} = %s"
        return self.db.execute(query, (value,))
    
    def create(self, data):
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table_name} ({fields}) VALUES ({placeholders})"
        return self.db.execute(query, tuple(data.values()))

class UserRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection, 'users')
    
    def find_by_email(self, email):
        return self.find_by_field('email', email)

class ProductRepository(BaseRepository):
    def __init__(self, db_connection):
        super().__init__(db_connection, 'products')
    
    def find_by_sku(self, sku):
        return self.find_by_field('sku', sku)
```

### 3. Configuration and Constants

```python
# ✅ Good: Centralized constants and configuration
class AppConstants:
    # Validation constants
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 128
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Business rules
    FREE_SHIPPING_THRESHOLD = 100
    TAX_RATE = 0.08
    MAX_CART_ITEMS = 50
    
    # Error messages
    INVALID_EMAIL_MSG = "Please enter a valid email address"
    WEAK_PASSWORD_MSG = f"Password must be at least {MIN_PASSWORD_LENGTH} characters"
    CART_FULL_MSG = f"Cart cannot contain more than {MAX_CART_ITEMS} items"
    
    # API endpoints
    USER_API_BASE = "/api/v1/users"
    PRODUCT_API_BASE = "/api/v1/products"
    ORDER_API_BASE = "/api/v1/orders"

class ValidationMessages:
    @staticmethod
    def password_too_short():
        return AppConstants.WEAK_PASSWORD_MSG
    
    @staticmethod
    def cart_item_limit_exceeded():
        return AppConstants.CART_FULL_MSG
```

### 4. Utility Classes and Helper Functions

```typescript
// ✅ Good: Reusable utility functions
class DateUtils {
    static formatDate(date: Date, format: string = 'YYYY-MM-DD'): string {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        
        return format
            .replace('YYYY', year.toString())
            .replace('MM', month)
            .replace('DD', day);
    }
    
    static addDays(date: Date, days: number): Date {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    }
    
    static isWeekend(date: Date): boolean {
        const day = date.getDay();
        return day === 0 || day === 6; // Sunday or Saturday
    }
}

class StringUtils {
    static capitalize(str: string): string {
        return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    }
    
    static truncate(str: string, maxLength: number, suffix: string = '...'): string {
        if (str.length <= maxLength) return str;
        return str.substring(0, maxLength - suffix.length) + suffix;
    }
    
    static kebabCase(str: string): string {
        return str
            .replace(/([a-z])([A-Z])/g, '$1-$2')
            .replace(/[\s_]+/g, '-')
            .toLowerCase();
    }
}

class ValidationUtils {
    static isValidEmail(email: string): boolean {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    static isStrongPassword(password: string): boolean {
        return password.length >= 8 &&
               /[A-Z]/.test(password) &&
               /[a-z]/.test(password) &&
               /\d/.test(password) &&
               /[!@#$%^&*]/.test(password);
    }
}
```

## Advanced DRY Patterns

### 1. Generic Repository Pattern

```python
from typing import TypeVar, Generic, List, Optional
from abc import ABC, abstractmethod

T = TypeVar('T')

class Repository(Generic[T], ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        pass
    
    @abstractmethod
    def save(self, entity: T) -> T:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass

class SQLRepository(Repository[T]):
    def __init__(self, db_connection, table_name: str, entity_class):
        self.db = db_connection
        self.table_name = table_name
        self.entity_class = entity_class
    
    def find_by_id(self, id: int) -> Optional[T]:
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        result = self.db.execute(query, (id,))
        return self.entity_class(**result) if result else None
    
    def find_all(self) -> List[T]:
        query = f"SELECT * FROM {self.table_name}"
        results = self.db.execute_all(query)
        return [self.entity_class(**row) for row in results]
    
    def save(self, entity: T) -> T:
        # Implementation for save
        pass
    
    def delete(self, id: int) -> bool:
        query = f"DELETE FROM {self.table_name} WHERE id = %s"
        return self.db.execute(query, (id,)) > 0

# Usage
user_repository = SQLRepository(db_connection, 'users', User)
product_repository = SQLRepository(db_connection, 'products', Product)
```

### 2. Decorator Pattern for Cross-Cutting Concerns

```python
from functools import wraps
import time
import logging

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def handle_exceptions(exception_type=Exception, default_return=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                logging.error(f"Error in {func.__name__}: {str(e)}")
                return default_return
        return wrapper
    return decorator

def cache_result(ttl_seconds=300):
    cache = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            current_time = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

# Usage
class UserService:
    @log_execution_time
    @handle_exceptions(ValueError, None)
    @cache_result(ttl_seconds=600)
    def get_user_profile(self, user_id: int):
        # Implementation
        pass
```

### 3. Strategy Pattern for Algorithm Reuse

```python
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List) -> List:
        pass

class QuickSort(SortingStrategy):
    def sort(self, data: List) -> List:
        if len(data) <= 1:
            return data
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return self.sort(left) + middle + self.sort(right)

class MergeSort(SortingStrategy):
    def sort(self, data: List) -> List:
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List, right: List) -> List:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class DataProcessor:
    def __init__(self, sorting_strategy: SortingStrategy):
        self.sorting_strategy = sorting_strategy
    
    def process_data(self, data: List) -> List:
        # Common preprocessing
        cleaned_data = [x for x in data if x is not None]
        
        # Use strategy for sorting
        sorted_data = self.sorting_strategy.sort(cleaned_data)
        
        # Common postprocessing
        return sorted_data
```

## When NOT to Apply DRY

### 1. Coincidental Duplication

```python
# ❌ Bad: Over-applying DRY to coincidental similarity
def calculate_user_age(birth_date):
    return (datetime.now() - birth_date).days // 365

def calculate_product_shelf_life(manufacture_date):
    return (datetime.now() - manufacture_date).days // 365

# These happen to look similar but represent different business concepts
# Don't extract a common function just because they're similar

# ✅ Good: Keep them separate as they represent different concepts
def calculate_user_age(birth_date):
    """Calculate user's age in years"""
    return (datetime.now() - birth_date).days // 365

def calculate_product_age_days(manufacture_date):
    """Calculate how many days since product was manufactured"""
    return (datetime.now() - manufacture_date).days
```

### 2. Premature Abstraction

```python
# ❌ Bad: Creating abstraction too early
class GenericProcessor:
    def process(self, data, config):
        # Overly generic method that tries to handle everything
        if config.type == 'user':
            # User-specific logic
            pass
        elif config.type == 'product':
            # Product-specific logic
            pass
        # This will become unwieldy as more types are added

# ✅ Good: Create specific processors first, extract common patterns later
class UserProcessor:
    def process(self, user_data):
        # Specific user processing logic
        pass

class ProductProcessor:
    def process(self, product_data):
        # Specific product processing logic
        pass

# Extract common patterns only after they emerge naturally
```

## Testing DRY Code

### Testing Extracted Functions

```python
class TestUserValidator:
    def test_validate_email_valid(self):
        # Test the extracted validation logic
        try:
            UserValidator.validate_email("test@example.com")
        except ValueError:
            pytest.fail("Valid email should not raise exception")
    
    def test_validate_email_invalid(self):
        with pytest.raises(ValueError, match="Invalid email format"):
            UserValidator.validate_email("invalid-email")
    
    def test_validate_email_empty(self):
        with pytest.raises(ValueError, match="Email is required"):
            UserValidator.validate_email("")

class TestPricingCalculator:
    def test_calculate_subtotal(self):
        items = [
            OrderItem(price=10.0, quantity=2),
            OrderItem(price=5.0, quantity=3)
        ]
        assert PricingCalculator.calculate_subtotal(items) == 35.0
    
    def test_calculate_tax(self):
        assert PricingCalculator.calculate_tax(100.0) == 8.0
    
    def test_free_shipping_threshold(self):
        assert PricingCalculator.calculate_shipping(100.0) == 0
        assert PricingCalculator.calculate_shipping(99.0) == 10
```

## Documentation and DRY

### Single Source of Truth for Documentation

```python
class APIEndpoints:
    """
    Centralized API endpoint definitions.
    This serves as the single source of truth for all API routes.
    """
    
    # User endpoints
    USERS_BASE = "/api/v1/users"
    USER_BY_ID = f"{USERS_BASE}/{{user_id}}"
    USER_PROFILE = f"{USER_BY_ID}/profile"
    
    # Product endpoints
    PRODUCTS_BASE = "/api/v1/products"
    PRODUCT_BY_ID = f"{PRODUCTS_BASE}/{{product_id}}"
    PRODUCT_REVIEWS = f"{PRODUCT_BY_ID}/reviews"
    
    @classmethod
    def get_user_url(cls, user_id: int) -> str:
        return cls.USER_BY_ID.format(user_id=user_id)
    
    @classmethod
    def get_product_url(cls, product_id: int) -> str:
        return cls.PRODUCT_BY_ID.format(product_id=product_id)

# Usage in different parts of the application
class UserService:
    def get_user(self, user_id: int):
        url = APIEndpoints.get_user_url(user_id)
        # Make API call

class TestUserAPI:
    def test_get_user_endpoint(self):
        expected_url = APIEndpoints.get_user_url(123)
        # Test against the same URL definition
```

## Metrics and Validation

### Code Duplication Detection

Tools to identify duplication:

- **Python**: `pylint` with duplication detection
- **JavaScript/TypeScript**: `jscpd`, `eslint-plugin-sonarjs`
- **General**: SonarQube, PMD, CodeClimate

### Validation Checklist

Before completing any code, verify:

- [ ] No repeated code blocks longer than 3-5 lines
- [ ] Constants and configuration are centralized
- [ ] Business logic is not duplicated across methods/classes
- [ ] Validation rules are defined in single locations
- [ ] Error messages are centralized and reusable
- [ ] Database queries follow patterns and use templates
- [ ] API endpoints and routes are defined centrally
- [ ] Formatting and transformation logic is extracted
- [ ] Similar algorithms are abstracted appropriately
- [ ] Documentation doesn't repeat implementation details

## Performance Considerations

### DRY and Performance Trade-offs

```python
# Sometimes DRY can impact performance
class MetricsCollector:
    def __init__(self):
        self._cache = {}
    
    def get_user_metrics(self, user_id: int) -> UserMetrics:
        # For frequently called methods, consider caching
        if user_id in self._cache:
            return self._cache[user_id]
        
        metrics = self._calculate_user_metrics(user_id)
        self._cache[user_id] = metrics
        return metrics
    
    def _calculate_user_metrics(self, user_id: int) -> UserMetrics:
        # Expensive calculation that should be cached
        pass
```

## Integration with Other Principles

DRY complements:

- **SOLID principles**: Through proper abstraction and single responsibility
- **OOP principles**: Through inheritance and polymorphism
- **KISS principle**: By eliminating redundant complexity
- **YAGNI principle**: By not duplicating unused functionality

Remember: DRY is about eliminating duplication of knowledge and intent, not just code. Focus on reducing conceptual duplication while maintaining code clarity and maintainability.
