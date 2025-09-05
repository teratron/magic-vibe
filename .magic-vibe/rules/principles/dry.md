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
> **Dependencies:** `@rules/principles/kiss.md`, `@rules/principles/solid.md`

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
    base_cost = weight * 0.5 + distance * 0.1
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
def test_calculate_tax():
    assert calculate_tax(100, 0.08) == 8.0
    assert calculate_tax(0, 0.08) == 0.0
    assert calculate_tax(100, 0) == 0.0

def test_validate_email_format():
    assert validate_email_format("user@example.com") == True
    assert validate_email_format("invalid-email") == False
    assert validate_email_format("") == False
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
# ✅ Good: Secure shared validation
def sanitize_input(user_input, max_length=255):
    """Sanitize user input with consistent security rules."""
    if not isinstance(user_input, str):
        raise TypeError("Input must be string")
    
    sanitized = user_input.strip()[:max_length]
    # Remove potentially dangerous characters
    return re.sub(r'[<>"\']', '', sanitized)

def hash_password(password, salt=None):
    """Hash password using consistent security standards."""
    import hashlib
    import secrets
    
    if salt is None:
        salt = secrets.token_hex(16)
    
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}:{hashed.hex()}"
```

### 5.2. Performance Through DRY

```python
# ✅ Good: Cached shared calculations
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_complex_formula(x, y, z):
    """Expensive calculation with caching."""
    return (x ** 2 + y ** 2 + z ** 2) ** 0.5

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

*Last Updated: 2025-01-XX | File Size: ~12KB | Status: Active*
