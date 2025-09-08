---
description: DRY (Don't Repeat Yourself) principle guide for eliminating code duplication and promoting code reusability.
globs:
alwaysApply: true
---

# DRY Principle

> **Magic Vibe Rule: Don't Repeat Yourself**  
> **Category:** Principles  
> **Priority:** High  
> **File Size:** ~12KB (AI-optimized)  
> **Dependencies:** `principles/kiss.md`, `principles/solid.md`

DRY (Don't Repeat Yourself) principle guide for eliminating code duplication and promoting code reusability. Essential for AI agents to generate maintainable, efficient code.

## 1. Implementation Guidelines

### 1.1. Core DRY Concept

**Definition:** Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**Key Aspects:**

- **Code Duplication**: Avoid repeating the same logic
- **Knowledge Duplication**: Don't duplicate business rules or constants
- **Process Duplication**: Eliminate repeated workflows or procedures
- **Documentation Duplication**: Single source of truth for specifications

### 1.2. Types of Duplication to Avoid

**Code Duplication:**

```python
# ❌ Bad: Repeated validation logic

class UserController:
    def create_user(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email is required")
        if '@' not in user_data.get('email', ''):
            raise ValueError("Invalid email format")
        # Create logic

    def update_user(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email is required")
        if '@' not in user_data.get('email', ''):
            raise ValueError("Invalid email format")
        # Update logic

# ✅ Good: Extracted validation

class UserValidator:
    @staticmethod
    def validate_email(email):
        if not email:
            raise ValueError("Email is required")
        if '@' not in email:
            raise ValueError("Invalid email format")

class UserController:
    def create_user(self, user_data):
        UserValidator.validate_email(user_data.get('email'))
        # Create logic

    def update_user(self, user_data):
        UserValidator.validate_email(user_data.get('email'))
        # Update logic
```

**Configuration Duplication:**

```python
# ❌ Bad: Scattered constants
class DatabaseService:
    def connect(self):
        host = "localhost"
        port = 5432

class CacheService:
    def connect(self):
        host = "localhost"  # Duplicated

# ✅ Good: Centralized config
class Config:
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 5432
    CACHE_HOST = "localhost"
    CACHE_PORT = 6379

class DatabaseService:
    def connect(self):
        host = Config.DATABASE_HOST
        port = Config.DATABASE_PORT
```

### 1.3. Extraction Strategies

**Function Extraction:**

```python
# Extract common operations into reusable functions

def calculate_tax(amount, rate=0.08):
    return amount * rate

def format_currency(amount):
    return f"${amount:.2f}"

def validate_positive_number(value, field_name):
    if value <= 0:
        raise ValueError(f"{field_name} must be positive")
```

## 2. Change Management Protocols

### 2.1. Refactoring Duplicated Code

**DRY Refactoring Process:**

1. **Identify Duplication** - Use static analysis tools
2. **Extract Common Logic** - Create shared functions/classes  
3. **Centralize Configuration** - Move constants to config files
4. **Validate Changes** - Ensure all references work correctly

### 2.2. Prevention Strategies

**Code Review Checklist:**

- Check for repeated patterns
- Verify single source of truth for business rules
- Ensure configuration is centralized
- Look for copy-paste patterns

### 2.3. Duplication Detection

**Automated Tools:**

```bash
# Use duplication detection tools
flake8 --select=F401,F402 *.py  # Import duplication
pylint --disable=all --enable=duplicate-code *.py
```

## 3. Communication Standards

### 3.1. Naming Conventions

```python
# ✅ Good: Clear, reusable function names

def calculate_shipping_cost(weight, distance, express=False):
    """Calculate shipping cost based on weight and distance."""
    base_cost = weight *0.5 + distance* 0.1
    return base_cost * 1.5 if express else base_cost

def validate_email_format(email):
    """Validate email format using standard pattern."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def format_phone_number(phone):
    """Format phone number to standard display format."""
    digits = re.sub(r'\D', '', phone)
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
```

### 3.2. Documentation Standards

**Shared Logic Documentation:**

- Document purpose and usage
- Specify parameters and return values
- Include usage examples
- Note any dependencies or side effects

### 3.3. API Consistency

```python
# ✅ Good: Consistent API patterns
class DataProcessor:
    def process_user_data(self, data):
        return self._process_data(data, 'user')
    
    def process_order_data(self, data):
        return self._process_data(data, 'order')
    
    def _process_data(self, data, data_type):
        """Common processing logic for all data types."""
        validated_data = self._validate_data(data, data_type)
        return self._transform_data(validated_data, data_type)
```

## 4. Quality Assurance Framework

### 4.1. Testing Shared Code

```python
# Test reusable components thoroughly

class TestUserValidator:
    def test_validate_email_required(self):
        validator = UserValidator()
        with pytest.raises(ValueError, match="Email is required"):
            validator.validate({'name': 'John'})

    def test_validate_email_format(self):
        validator = UserValidator()
        with pytest.raises(ValueError, match="Invalid email format"):
            validator.validate_email("invalid-email")
        
        # Valid email should not raise exception
        validator.validate_email("test@example.com")
```

### 4.2. Duplication Metrics

**Key Metrics to Track:**

- **Code Duplication Percentage**: < 5% of codebase
- **Shared Function Usage**: Track reuse frequency
- **Configuration Centralization**: Single config source per environment
- **Copy-Paste Detection**: Automated scanning results

### 4.3. Quality Gates

```python
# Automated quality checks
def check_duplication_threshold(codebase_path):
    """Check if code duplication exceeds threshold."""
    duplication_percentage = analyze_duplication(codebase_path)
    if duplication_percentage > 5:
        raise QualityGateError(f"Duplication {duplication_percentage}% exceeds 5% threshold")
```

## 5. Security & Performance Guidelines

### 5.1. Secure Shared Components

```python
# Secure shared components implementation would go here
pass
```

### 5.2. Performance Through DRY

```python
# ✅ Good: Shared validation logic

def validate_user_data(user_data):
    """Validate user data with comprehensive checks."""
    required_fields = ['email', 'name']
    for field in required_fields:
        if not user_data.get(field):
            raise ValueError(f"{field} is required")

    if not is_valid_email(user_data['email']):
        raise ValueError("Invalid email format")

def is_valid_email(email):
    """Check if email format is valid."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### 5.3. Reusable Configuration Management

```python
# ✅ Good: Reusable configuration management
class ConfigManager:
    _instance = None
    _config = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get(self, key, default=None):
        return self._config.get(key, default)
    
    def set(self, key, value):
        self._config[key] = value
```

### 5.4. Shared Error Handling

```python
# ✅ Good: Shared error handling

class APIError(Exception):
    """Base API error class."""
    def **init**(self, message, status_code=500):
        super().**init**(message)
        self.status_code = status_code

def handle_api_errors(func):
    """Decorator for consistent error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError as e:
            raise APIError(str(e), 400)
        except Exception as e:
            raise APIError("Internal server error", 500)
    return wrapper
```

### 5.5. Shared Logging Configuration

```python
# ✅ Good: Shared logging configuration
import logging

def setup_logger(name, level=logging.INFO):
    """Create and configure a logger with consistent settings."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

# Usage
logger = setup_logger(__name__)
```

### 5.6. Shared Utility for Data Transformation

```python
# ✅ Good: Shared utility for data transformation

def transform_to_dict(obj):
    """Convert object to dictionary representation."""
    if hasattr(obj, '**dict**'):
        return obj.**dict**
    elif isinstance(obj, dict):
        return obj
    else:
        return {'value': obj}

def deep_merge_dicts(dict1, dict2):
    """Deep merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
```

### 5.7. Shared Database Connection Pool

```python
# ✅ Good: Shared database connection pool
from contextlib import contextmanager

class DatabasePool:
    _instance = None
    _connections = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @contextmanager
    def get_connection(self):
        # Simplified connection management
        conn = self._create_connection()
        try:
            yield conn
        finally:
            self._release_connection(conn)
    
    def _create_connection(self):
        # Connection creation logic
        pass
    
    def _release_connection(self, conn):
        # Connection release logic
        pass
```

### 5.8. Shared Caching Mechanism

```python
# ✅ Good: Shared caching mechanism

from functools import lru_cache
import time

class Cache:
    def **init**(self, max_size=128):
        self._cache = {}
        self._max_size = max_size
        self._access_times = {}

    def get(self, key):
        if key in self._cache:
            self._access_times[key] = time.time()
            return self._cache[key]
        return None
    
    def set(self, key, value):
        if len(self._cache) >= self._max_size:
            # Remove least recently used item
            lru_key = min(self._access_times, key=self._access_times.get)
            del self._cache[lru_key]
            del self._access_times[lru_key]
        
        self._cache[key] = value
        self._access_times[key] = time.time()
```

### 5.9. Shared Authentication Utilities

```python
# ✅ Good: Shared authentication utilities
import hashlib
import secrets

def hash_password(password, salt=None):
    """Hash password using secure method."""
    if salt is None:
        salt = secrets.token_hex(16)
    
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}:{hashed.hex()}"

def verify_password(password, hashed_password):
    """Verify password against hash."""
    salt, hash_part = hashed_password.split(':')
    return hash_password(password, salt).split(':')[1] == hash_part
```

### 5.10. Cached Shared Calculations

```python
# ✅ Good: Cached shared calculations

from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_complex_formula(x, y, z):
    """Expensive calculation with caching."""
    return (x **2 + y** 2 + z **2)** 0.5

# ✅ Good: Shared database connections

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## 6. Integration & Compatibility

### 6.1. Shared Libraries

```python
# ✅ Good: Reusable utility library
class DateUtils:
    @staticmethod
    def format_date(date, format_string='%Y-%m-%d'):
        return date.strftime(format_string)
    
    @staticmethod
    def parse_date(date_string, format_string='%Y-%m-%d'):
        from datetime import datetime
        return datetime.strptime(date_string, format_string)

class StringUtils:
    @staticmethod
    def slugify(text):
        return re.sub(r'[^\w\s-]', '', text.lower()).strip().replace(' ', '-')
    
    @staticmethod
    def truncate(text, length, suffix='...'):
        return text[:length] + suffix if len(text) > length else text
```

### 6.2. Framework Integration

**Shared Components Across Frameworks:**

- Database access layers
- Validation utilities
- Configuration management
- Logging utilities
- Error handling patterns

### 6.3. API Standardization

```python
# ✅ Good: Consistent API responses

def create_api_response(data=None, error=None, status_code=200):
    """Standard API response format."""
    return {
        'success': error is None,
        'data': data,
        'error': error,
        'timestamp': datetime.utcnow().isoformat()
    }
```

## 7. Monitoring & Maintenance

### 7.1. Shared Component Monitoring

```python
import logging

# Centralized logging configuration
def setup_logging(service_name):
    """Configure logging for any service."""
    logging.basicConfig(
        level=logging.INFO,
        format=f'%(asctime)s - {service_name} - %(levelname)s - %(message)s'
    )
    return logging.getLogger(service_name)

# Usage tracking for shared components
def track_usage(component_name, operation):
    """Track usage of shared components."""
    logger = logging.getLogger('component_usage')
    logger.info(f"Component: {component_name}, Operation: {operation}")
```

### 7.2. Maintenance Guidelines

**Regular DRY Maintenance:**

- Review code for new duplication patterns
- Update shared libraries for new requirements
- Consolidate similar functions
- Remove unused shared components

### 7.3. Versioning Shared Components

```python
# Version shared utilities for backward compatibility

class ConfigV1:
    VERSION = "1.0.0"
    # Legacy configuration

class ConfigV2:
    VERSION = "2.0.0"
    # New configuration with migration support

    @classmethod
    def migrate_from_v1(cls, v1_config):
        # Migration logic
        pass
```

## 8. AI Agent Optimization

### 8.1. AI-Friendly DRY Patterns

```python
# ✅ Good: Clear patterns for AI recognition
def create_validator(field_name, validation_type):
    """Factory function for creating field validators."""
    validators = {
        'email': lambda x: '@' in x and '.' in x.split('@')[1],
        'phone': lambda x: len(re.sub(r'\D', '', x)) == 10,
        'required': lambda x: x is not None and x != ''
    }
    
    validator = validators.get(validation_type)
    if not validator:
        raise ValueError(f"Unknown validation type: {validation_type}")
    
    def validate(value):
        if not validator(value):
            raise ValueError(f"Invalid {field_name}: {value}")
        return True
    
    return validate

# Usage that AI can easily generate
email_validator = create_validator('email', 'email')
phone_validator = create_validator('phone', 'phone')
```

### 8.2. Code Generation Guidelines

**For AI agents applying DRY:**

- Identify repeated patterns before generating code
- Use existing shared functions when available
- Extract common logic into reusable components
- Maintain consistent naming and structure

### 8.3. Pattern Recognition

**Common DRY patterns AI should recognize:**

- Validation functions
- Data transformation utilities
- Configuration management
- Error handling wrappers
- Logging patterns

### 8.4. Refactoring Assistance

**AI can help with DRY by:**

- Detecting code duplication
- Suggesting extraction opportunities
- Generating shared utility functions
- Maintaining consistency across modules

---

**Magic Vibe DRY Principle v2.1.0** - Eliminate duplication, enhance maintainability

**Last Updated:** 2025-09-08 | **File Size:** ~12KB | **Status:** Active
