---
description: KISS (Keep It Simple, Stupid) principle guide for writing simple, clear, and maintainable code that AI agents can easily understand and generate.
globs:
alwaysApply: true
---

# KISS Principle

> **Magic Vibe Rule: Keep It Simple, Stupid**  
> **Category:** Principles  
> **Priority:** High  
> **File Size:** ~8KB (AI-optimized)  
> **Dependencies:** `principles/dry.md`, `principles/yagni.md`

KISS (Keep It Simple, Stupid) principle guide for writing simple, clear, and maintainable code that AI agents can easily understand and generate.

## 1. Implementation Guidelines

### 1.1. Core KISS Concept

**Definition:** Simplicity should be a key goal in design, and unnecessary complexity should be avoided.

**Key Aspects:**

- **Readability**: Code should be easy to read and understand
- **Minimal Complexity**: Use the simplest approach that works
- **Clear Intent**: The purpose of code should be obvious
- **Maintainability**: Simple code is easier to maintain and modify

### 1.2. Simplicity Guidelines

**Prefer Clear, Descriptive Names:**

```python
# ❌ Bad: Unclear names
def calc_pmt(p, r, n):
    return p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

# ✅ Good: Clear names
def calculate_monthly_payment(principal, rate, payments):
    """Calculate monthly payment for a loan."""
    factor = (1 + rate) ** payments
    return principal * (rate * factor) / (factor - 1)
```

**Keep Functions Small and Focused:**

```python
# ❌ Bad: Large function with mixed responsibilities
def process_order(order_data):
    # validation, calculation, saving, emailing - too much!
    pass

# ✅ Good: Single-purpose functions
def validate_order_data(order_data):
    """Validate order data."""
    pass

def process_order(order_data):
    """Process order workflow."""
    validate_order_data(order_data)
    return save_order(order_data)
```

**Avoid Over-Engineering:**

```python
# ❌ Bad: Complex patterns for simple needs
class AbstractFactoryBuilderSingleton:
    pass

# ✅ Good: Simple solution
def format_user_name(first, last):
    return f"{first} {last}".strip()
```

## 2. Change Management Protocols

### 2.1. Refactoring Complex Code

**Simplification Process:**

1. **Identify complexity hotspots** - Long functions, deep nesting, unclear names
2. **Extract focused functions** - Single responsibility principle
3. **Simplify control flow** - Early returns, guard clauses
4. **Use standard libraries** - Avoid reinventing common functionality

### 2.2. Code Review Guidelines

**KISS Validation Checklist:**

- Function length < 20 lines
- Nesting depth < 3 levels  
- Clear, descriptive names
- Single responsibility per function
- Standard library usage where possible

### 2.3. Complexity Metrics

**Measurable Targets:**

- **Cyclomatic Complexity**: < 10 per function
- **Lines of Code**: < 20 per function
- **Parameter Count**: < 5 per function
- **Nesting Depth**: < 3 levels

## 3. Communication Standards

### 3.1. Naming Conventions

```python
# ✅ Good: Self-documenting names
def calculate_monthly_payment(principal, rate, months):
    return principal * (rate * (1 + rate) ** months) / ((1 + rate) ** months - 1)

def is_valid_email(email):
    return '@' in email and '.' in email

def get_active_users():
    return [user for user in users if user.status == 'active']
```

### 3.2. Comment Guidelines

```python
# ✅ Good: Explain why, not what
def apply_bulk_discount(total, item_count):
    if item_count >= 10:
        return total * 0.9  # Encourage bulk orders
    return total
```

### 3.3. Documentation Standards

**Keep documentation simple and focused:**

- **Purpose**: What the function does
- **Parameters**: Input requirements  
- **Returns**: Output description
- **Example**: Simple usage case

## 4. Quality Assurance Framework

### 4.1. Testing Simple Code

```python
# Simple function
def calculate_tax(amount, rate):
    """Calculate tax for given amount and rate."""
    return amount * rate

# Simple test
def test_calculate_tax():
    assert calculate_tax(100, 0.1) == 10
    assert calculate_tax(0, 0.1) == 0
    assert calculate_tax(100, 0) == 0
```

### 4.2. Complexity Prevention

**Early Warning Signs:**

- Functions longer than 20 lines
- More than 3 levels of nesting
- Complex boolean expressions
- Multiple responsibilities in one function
- Hard-to-name variables/functions

### 4.3. Automated Validation

```bash
# Use complexity analysis tools
flake8 --max-complexity=10 *.py
pylint --max-line-length=80 *.py
```

## 5. Security & Performance Guidelines

### 5.1. Simple Security Practices

```python
# ✅ Good: Simple validation and authentication
def validate_email(email):
    return '@' in email and '.' in email.split('@')[1]

def require_authentication(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper
```

### 5.2. Performance Through Simplicity

```python
# ✅ Good: Simple and efficient
def get_active_users(users):
    return [user for user in users if user.status == 'active']

def calculate_total(items):
    return sum(item.price * item.quantity for item in items)
```

## 6. Integration & Compatibility

### 6.1. API Design Simplicity

```python
# ✅ Good: Simple API design
class UserService:
    def get_user(self, user_id):
        """Get user by ID."""
        return self.db.get_user(user_id)
    
    def create_user(self, user_data):
        """Create new user."""
        validate_user_data(user_data)
        return self.db.save_user(user_data)
    
    def update_user(self, user_id, updates):
        """Update existing user."""
        user = self.get_user(user_id)
        updated_user = {**user, **updates}
        return self.db.save_user(updated_user)
```

### 6.2. Framework Integration

**Simple patterns work across frameworks:**

- Pure functions for business logic
- Clear separation of concerns
- Standard error handling
- Consistent naming conventions

### 6.3. Database Simplicity

```python
# ✅ Good: Simple database operations
class UserRepository:
    def find_by_id(self, user_id):
        return self.db.execute("SELECT * FROM users WHERE id = ?", [user_id])
    
    def find_by_email(self, email):
        return self.db.execute("SELECT * FROM users WHERE email = ?", [email])
    
    def save(self, user):
        return self.db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            [user.name, user.email]
        )
```

## 7. Monitoring & Maintenance

### 7.1. Simple Logging

```python
import logging

logger = logging.getLogger(__name__)

def process_order(order):
    """Process order with simple logging."""
    logger.info(f"Processing order {order.id}")
    
    try:
        result = validate_and_save_order(order)
        logger.info(f"Order {order.id} processed successfully")
        return result
    except Exception as e:
        logger.error(f"Failed to process order {order.id}: {e}")
        raise
```

### 7.2. Metrics and Monitoring

**Simple metrics to track:**

- Function execution time
- Error rates
- Code complexity scores
- Test coverage percentage

### 7.3. Maintenance Guidelines

**Regular simplification:**

- Review functions over 20 lines
- Refactor complex conditionals
- Replace custom code with standard libraries
- Update documentation to match simplified code

## 8. AI Agent Optimization

### 8.1. AI-Friendly Code Patterns

```python
# ✅ Good: Clear patterns for AI generation
def calculate_discount(total, customer_type):
    """Calculate discount based on customer type."""
    discount_rates = {
        'premium': 0.1,
        'standard': 0.05,
        'new': 0.0
    }
    return total * discount_rates.get(customer_type, 0.0)

def validate_required_fields(data, required_fields):
    """Validate that all required fields are present."""
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
```

### 8.2. Code Generation Guidelines

**For AI agents generating code:**

- Prefer explicit over implicit
- Use descriptive variable names
- Keep functions focused on single tasks
- Include docstrings for all functions
- Use type hints where beneficial

### 8.3. Pattern Recognition

**Common simple patterns AI can recognize:**

- Input validation functions
- Data transformation functions
- CRUD operations
- Configuration loading
- Error handling wrappers

### 8.4. Complexity Avoidance

**AI agents should avoid:**

- Deep inheritance hierarchies
- Complex design patterns for simple problems
- Premature optimization
- Over-abstraction
- Magic numbers and strings

---

**Magic Vibe KISS Principle v2.1.0** - Simplicity for AI and humans

***Last Updated:** 2025-01-XX | **File Size:** ~8KB | **Status:** Active*

```python
def send(self, message: str, device_id: str) -> bool:
        # Push notification logic
        pass

class NotificationService:
    def **init**(self):
        self.email_sender = EmailSender()
        self.sms_sender = SMSSender()
        self.push_sender = PushSender()

    def send_notification(self, message: str, recipient: str, method: str, urgent: bool = False):
        if urgent:
            message = f"URGENT: {message}"
        
        if method == 'email':
            return self.email_sender.send(message, recipient)
        elif method == 'sms':
            return self.sms_sender.send(message, recipient)
        elif method == 'push':
            return self.push_sender.send(message, recipient)
        else:
            raise ValueError(f"Unknown notification method: {method}")
```

## Language-Specific KISS Guidelines

### Python KISS

```python
# ✅ Use Python's built-in functions and idioms
# List comprehensions for simple transformations
squared_numbers = [x**2 for x in numbers if x > 0]

# Dict comprehensions for simple mappings
user_names = {user.id: user.name for user in users}

# Use enumerate instead of manual indexing
for index, item in enumerate(items):
    print(f"{index}: {item}")

# Use zip for parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Simple exception handling
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Operation failed: {e}")
    result = default_value
```

### TypeScript KISS

```typescript
// ✅ Use TypeScript features for simplicity
interface User {
    id: string;
    name: string;
    email: string;
}

// Simple type guards
function isUser(obj: any): obj is User {
    return obj && typeof obj.id === 'string' && typeof obj.name === 'string';
}

// Use optional chaining and nullish coalescing
const userName = user?.profile?.name ?? 'Unknown';

// Simple async/await instead of promise chains
async function fetchUserData(id: string): Promise<User | null> {
    try {
        const response = await fetch(`/users/${id}`);
        return response.ok ? await response.json() : null;
    } catch {
        return null;
    }
}

// Use array methods for transformations
const activeUsers = users
    .filter(user => user.isActive)
    .map(user => ({ id: user.id, name: user.name }));
```

## Testing Simple Code

### Simple Test Structure

```python
class TestOrderCalculations:
    def test_calculate_subtotal_single_item(self):
        # Arrange
        items = [OrderItem(product_id="1", quantity=2, price=10.0)]

        # Act
        subtotal = calculate_subtotal(items)
        
        # Assert
        assert subtotal == 20.0
    
    def test_calculate_subtotal_multiple_items(self):
        items = [
            OrderItem(product_id="1", quantity=2, price=10.0),
            OrderItem(product_id="2", quantity=1, price=5.0)
        ]
        
        subtotal = calculate_subtotal(items)
        
        assert subtotal == 25.0
    
    def test_calculate_subtotal_empty_list(self):
        subtotal = calculate_subtotal([])
        assert subtotal == 0.0

```

## Documentation for Simple Code

### Clear, Concise Documentation

```python
def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate monthly loan payment.
    
    Args:
        principal: Loan amount in dollars
        annual_rate: Annual interest rate as decimal (e.g., 0.05 for 5%)
        years: Loan term in years
    
    Returns:
        Monthly payment amount in dollars
    
    Example:
        >>> calculate_monthly_payment(100000, 0.05, 30)
        536.82
    """
    if annual_rate == 0:
        return principal / (years * 12)
    
    monthly_rate = annual_rate / 12
    num_payments = years * 12
    
    factor = (1 + monthly_rate) ** num_payments
    return principal * (monthly_rate * factor) / (factor - 1)
```

## Common Complexity Anti-Patterns

### 1. Unnecessary Abstraction

```python
# ❌ Bad: Over-abstraction for simple operations
class StringOperationFactory:
    @staticmethod
    def create_operation(operation_type):
        operations = {
            'uppercase': UppercaseOperation(),
            'lowercase': LowercaseOperation(),
            'capitalize': CapitalizeOperation()
        }
        return operations.get(operation_type)

class StringOperation(ABC):
    @abstractmethod
    def execute(self, text: str) -> str:
        pass

class UppercaseOperation(StringOperation):
    def execute(self, text: str) -> str:
        return text.upper()

# ✅ Good: Simple, direct approach
def format_text(text: str, format_type: str) -> str:
    """Format text according to specified type."""
    formats = {
        'uppercase': text.upper,
        'lowercase': text.lower,
        'capitalize': text.capitalize
    }
    
    formatter = formats.get(format_type)
    if not formatter:
        raise ValueError(f"Unknown format type: {format_type}")
    
    return formatter()
```

### 2. Feature Creep in Functions

```python
# ❌ Bad: Function doing too many things
def send_email(to, subject, body, cc=None, bcc=None, attachments=None, 
               priority='normal', track_opens=False, schedule_time=None,
               template_id=None, merge_vars=None, custom_headers=None):
    # Complex email sending with many features
    pass

# ✅ Good: Simple function with clear purpose
def send_simple_email(to: str, subject: str, body: str) -> bool:
    """Send a simple email message."""
    # Simple email sending logic
    pass

def send_email_with_attachments(to: str, subject: str, body: str, 
                              attachments: List[str]) -> bool:
    """Send email with file attachments."""
    # Email with attachments logic
    pass

class EmailScheduler:
    def schedule_email(self, email_data: dict, send_time: datetime) -> str:
        """Schedule an email to be sent later."""
        # Scheduling logic
        pass
```

## Performance and KISS

### Simple Performance Optimizations

```python
# ✅ Simple caching for expensive operations
_calculation_cache = {}

def expensive_calculation(input_value: str) -> float:
    """Perform expensive calculation with simple caching."""
    if input_value in _calculation_cache:
        return _calculation_cache[input_value]
    
    result = perform_complex_calculation(input_value)
    _calculation_cache[input_value] = result
    return result

# ✅ Simple database query optimization
def get_user_orders(user_id: str, limit: int = 10) -> List[Order]:
    """Get user orders with simple pagination."""
    query = """
        SELECT id, total, created_at 
        FROM orders 
        WHERE user_id = %s 
        ORDER BY created_at DESC 
        LIMIT %s
    """
    return database.fetch_all(query, (user_id, limit))
```

## Validation Checklist

Before completing any code, verify:

- [ ] Function names clearly describe what they do
- [ ] Functions are focused on single responsibilities
- [ ] No unnecessary abstraction layers
- [ ] Standard library functions are used when available
- [ ] Control flow is straightforward with minimal nesting
- [ ] Error handling is clear and specific
- [ ] Data structures are as simple as possible
- [ ] Comments explain "why" not "what"
- [ ] No premature optimization
- [ ] Code can be understood by team members

## Integration with Other Principles

KISS complements:

- **DRY principle**: Simple code is easier to deduplicate
- **SOLID principles**: Simplicity makes SOLID easier to apply
- **OOP principles**: Simple classes and methods are more maintainable
- **YAGNI principle**: Avoiding unnecessary features keeps code simple

## When Simplicity Goes Too Far

### Avoid Over-Simplification

```python
# ❌ Too simple: Doesn't handle edge cases
def divide(a, b):
    return a / b  # Will crash on division by zero

# ✅ Appropriately simple: Handles important edge cases
def safe_divide(a: float, b: float) -> float:
    """Divide two numbers safely."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# ❌ Too simple: Inadequate for production use
def hash_password(password):
    return password[::-1]  # Just reverse the string

# ✅ Appropriately simple: Secure but not overly complex
import hashlib
import secrets

def hash_password(password: str) -> str:
    """Hash password using secure methods."""
    salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}:{hashed.hex()}"
```

**Remember:** KISS is about finding the sweet spot between oversimplification and unnecessary complexity. The goal is code that is as simple as possible while still being correct, secure, and maintainable.
