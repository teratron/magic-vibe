---
description: KISS (Keep It Simple, Stupid) principle guide for writing simple, clear, and maintainable code.
globs:
alwaysApply: true
---

# KISS Principle (Keep It Simple, Stupid)

Whenever you use this rule, start your message with the following:

"Applying KISS principle..."

This rule ensures that code is written with simplicity as the primary goal. Simple code is easier to understand, maintain, debug, and extend. The KISS principle advocates for the simplest solution that solves the problem effectively.

## Core KISS Concept

**Definition:** Simplicity should be a key goal in design, and unnecessary complexity should be avoided.

**Key Aspects:**

- **Readability**: Code should be easy to read and understand
- **Minimal Complexity**: Use the simplest approach that works
- **Clear Intent**: The purpose of code should be obvious
- **Maintainability**: Simple code is easier to maintain and modify

## Simplicity Guidelines

### 1. Prefer Clear, Descriptive Names

```python
# ❌ Bad: Unclear, abbreviated names
def calc_pmt(p, r, n):
    return p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

def proc_usr_data(d):
    if d['t'] == 'a':
        return d['v'] * 1.1
    elif d['t'] == 'b':
        return d['v'] * 0.9
    return d['v']

# ✅ Good: Clear, descriptive names
def calculate_monthly_payment(principal, monthly_rate, num_payments):
    """Calculate monthly payment for a loan using the standard formula."""
    if monthly_rate == 0:
        return principal / num_payments
    
    factor = (1 + monthly_rate) ** num_payments
    return principal * (monthly_rate * factor) / (factor - 1)

def process_user_data(user_data):
    """Process user data based on account type."""
    account_type = user_data['account_type']
    base_value = user_data['value']
    
    if account_type == 'premium':
        return base_value * 1.1  # 10% bonus
    elif account_type == 'basic':
        return base_value * 0.9  # 10% reduction
    else:
        return base_value  # Standard rate
```

### 2. Keep Functions Small and Focused

```python
# ❌ Bad: Large, complex function
def process_order(order_data):
    # Validate order
    if not order_data.get('customer_id'):
        raise ValueError("Customer ID required")
    if not order_data.get('items'):
        raise ValueError("Order must have items")
    for item in order_data['items']:
        if not item.get('product_id'):
            raise ValueError("Product ID required")
        if item.get('quantity', 0) <= 0:
            raise ValueError("Quantity must be positive")
    
    # Calculate total
    subtotal = 0
    for item in order_data['items']:
        product = get_product(item['product_id'])
        if not product:
            raise ValueError(f"Product {item['product_id']} not found")
        if product['stock'] < item['quantity']:
            raise ValueError(f"Insufficient stock for {product['name']}")
        subtotal += product['price'] * item['quantity']
    
    # Apply discounts
    discount = 0
    customer = get_customer(order_data['customer_id'])
    if customer['type'] == 'premium':
        discount = subtotal * 0.1
    elif customer['loyalty_points'] > 1000:
        discount = subtotal * 0.05
    
    # Calculate tax
    tax_rate = get_tax_rate(customer['state'])
    tax = (subtotal - discount) * tax_rate
    
    # Create order record
    order = {
        'customer_id': order_data['customer_id'],
        'items': order_data['items'],
        'subtotal': subtotal,
        'discount': discount,
        'tax': tax,
        'total': subtotal - discount + tax,
        'status': 'pending'
    }
    
    # Save to database
    order_id = save_order(order)
    
    # Update inventory
    for item in order_data['items']:
        update_product_stock(item['product_id'], -item['quantity'])
    
    # Send confirmation email
    send_order_confirmation(customer['email'], order)
    
    return order_id

# ✅ Good: Broken down into focused functions
def validate_order_data(order_data):
    """Validate that order data contains required fields."""
    if not order_data.get('customer_id'):
        raise ValueError("Customer ID required")
    
    if not order_data.get('items'):
        raise ValueError("Order must have items")
    
    for item in order_data['items']:
        validate_order_item(item)

def validate_order_item(item):
    """Validate a single order item."""
    if not item.get('product_id'):
        raise ValueError("Product ID required")
    
    if item.get('quantity', 0) <= 0:
        raise ValueError("Quantity must be positive")

def calculate_order_subtotal(items):
    """Calculate subtotal for order items."""
    subtotal = 0
    for item in items:
        product = get_product(item['product_id'])
        if not product:
            raise ValueError(f"Product {item['product_id']} not found")
        
        if product['stock'] < item['quantity']:
            raise ValueError(f"Insufficient stock for {product['name']}")
        
        subtotal += product['price'] * item['quantity']
    
    return subtotal

def calculate_discount(customer, subtotal):
    """Calculate discount based on customer type and loyalty."""
    if customer['type'] == 'premium':
        return subtotal * 0.1
    elif customer['loyalty_points'] > 1000:
        return subtotal * 0.05
    return 0

def process_order(order_data):
    """Process a customer order through the complete workflow."""
    validate_order_data(order_data)
    
    customer = get_customer(order_data['customer_id'])
    subtotal = calculate_order_subtotal(order_data['items'])
    discount = calculate_discount(customer, subtotal)
    
    tax_rate = get_tax_rate(customer['state'])
    tax = (subtotal - discount) * tax_rate
    
    order = create_order_record(order_data, subtotal, discount, tax)
    order_id = save_order(order)
    
    update_inventory_for_order(order_data['items'])
    send_order_confirmation(customer['email'], order)
    
    return order_id
```

### 3. Avoid Over-Engineering

```python
# ❌ Bad: Over-engineered for simple requirement
class AbstractFactoryBuilderSingleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def create_builder(self, builder_type):
        factory = self.get_factory(builder_type)
        return factory.create_builder()
    
    def get_factory(self, factory_type):
        # Complex factory selection logic
        pass

class UserDataProcessorBuilder:
    def __init__(self):
        self.processor = UserDataProcessor()
    
    def with_validation(self):
        self.processor.add_validator(GenericValidator())
        return self
    
    def with_transformation(self):
        self.processor.add_transformer(GenericTransformer())
        return self
    
    def build(self):
        return self.processor

# Usage for simple requirement: validate and transform user data
factory = AbstractFactoryBuilderSingleton()
builder = factory.create_builder('user_data')
processor = builder.with_validation().with_transformation().build()
result = processor.process(user_data)

# ✅ Good: Simple, direct approach
def validate_user_data(user_data):
    """Validate user data fields."""
    if not user_data.get('email'):
        raise ValueError("Email is required")
    if not user_data.get('name'):
        raise ValueError("Name is required")

def transform_user_data(user_data):
    """Transform user data to standard format."""
    return {
        'email': user_data['email'].lower().strip(),
        'name': user_data['name'].strip(),
        'created_at': datetime.now()
    }

def process_user_data(user_data):
    """Validate and transform user data."""
    validate_user_data(user_data)
    return transform_user_data(user_data)

# Simple usage
result = process_user_data(user_data)
```

### 4. Use Standard Libraries and Patterns

```python
# ❌ Bad: Reinventing the wheel
def custom_sort(items, key_func=None, reverse=False):
    """Custom sorting implementation"""
    # Complex custom sorting algorithm
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            item1_key = key_func(items[i]) if key_func else items[i]
            item2_key = key_func(items[j]) if key_func else items[j]
            
            should_swap = (item1_key > item2_key) if not reverse else (item1_key < item2_key)
            if should_swap:
                items[i], items[j] = items[j], items[i]
    return items

def custom_datetime_formatter(dt, format_type):
    """Custom date formatting"""
    if format_type == 'iso':
        return f"{dt.year}-{str(dt.month).zfill(2)}-{str(dt.day).zfill(2)}"
    elif format_type == 'us':
        return f"{dt.month}/{dt.day}/{dt.year}"
    # ... more custom formatting

# ✅ Good: Using standard libraries
from datetime import datetime

def sort_users_by_name(users):
    """Sort users by name using standard library."""
    return sorted(users, key=lambda user: user['name'])

def format_date(date, format_string='%Y-%m-%d'):
    """Format date using standard datetime formatting."""
    return date.strftime(format_string)

# Usage
sorted_users = sort_users_by_name(users)
formatted_date = format_date(datetime.now(), '%m/%d/%Y')
```

### 5. Simplify Control Flow

```python
# ❌ Bad: Complex nested conditions
def calculate_shipping_cost(order):
    if order.get('items'):
        if len(order['items']) > 0:
            total_weight = 0
            for item in order['items']:
                if item.get('weight'):
                    total_weight += item['weight']
            
            if total_weight > 0:
                if order.get('customer'):
                    if order['customer'].get('type'):
                        if order['customer']['type'] == 'premium':
                            if total_weight > 10:
                                return 0  # Free shipping
                            else:
                                return 5  # Reduced shipping
                        else:
                            if total_weight > 20:
                                return 10  # Standard shipping
                            else:
                                return 15  # Higher rate for light items
    return 25  # Default expensive shipping

# ✅ Good: Simplified, early returns
def calculate_shipping_cost(order):
    """Calculate shipping cost based on order weight and customer type."""
    # Early validation
    if not order.get('items'):
        return 25
    
    total_weight = sum(item.get('weight', 0) for item in order['items'])
    if total_weight == 0:
        return 25
    
    customer_type = order.get('customer', {}).get('type', 'standard')
    
    # Premium customer shipping
    if customer_type == 'premium':
        return 0 if total_weight > 10 else 5
    
    # Standard customer shipping
    return 10 if total_weight > 20 else 15
```

### 6. Clear Error Handling

```typescript
// ❌ Bad: Complex error handling
async function fetchUserData(userId: string) {
    try {
        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('User not found');
            } else if (response.status === 401) {
                throw new Error('Unauthorized');
            } else if (response.status === 403) {
                throw new Error('Forbidden');
            } else if (response.status >= 500) {
                throw new Error('Server error');
            } else {
                throw new Error('Unknown error');
            }
        }
        
        try {
            const data = await response.json();
            if (data && typeof data === 'object') {
                if (data.id && data.name && data.email) {
                    return data;
                } else {
                    throw new Error('Invalid user data structure');
                }
            } else {
                throw new Error('Invalid response format');
            }
        } catch (jsonError) {
            throw new Error('Failed to parse response');
        }
    } catch (networkError) {
        if (networkError.message.includes('fetch')) {
            throw new Error('Network error');
        } else {
            throw networkError;
        }
    }
}

// ✅ Good: Simplified error handling
async function fetchUserData(userId: string): Promise<User> {
    const response = await fetch(`/api/users/${userId}`);
    
    if (!response.ok) {
        const errorMessages = {
            404: 'User not found',
            401: 'Unauthorized access',
            403: 'Access forbidden',
        };
        
        const message = errorMessages[response.status] || `Server error (${response.status})`;
        throw new Error(message);
    }
    
    const userData = await response.json();
    return userData as User;
}

// Usage with simple error handling
try {
    const user = await fetchUserData('123');
    console.log(user);
} catch (error) {
    console.error('Failed to fetch user:', error.message);
}
```

## Simplicity Patterns

### 1. Guard Clauses for Early Returns

```python
# ✅ Good: Using guard clauses
def process_payment(payment_data):
    """Process payment with clear validation flow."""
    if not payment_data:
        raise ValueError("Payment data is required")
    
    if payment_data.get('amount', 0) <= 0:
        raise ValueError("Amount must be positive")
    
    if not payment_data.get('payment_method'):
        raise ValueError("Payment method is required")
    
    if not payment_data.get('customer_id'):
        raise ValueError("Customer ID is required")
    
    # Main processing logic here
    return process_validated_payment(payment_data)
```

### 2. Simple Data Structures

```python
# ❌ Bad: Over-complex data structure
class OrderItemContainer:
    def __init__(self):
        self._items = {}
        self._metadata = {}
        self._relations = {}
    
    def add_item(self, item_id, item_data, metadata=None, relations=None):
        self._items[item_id] = item_data
        if metadata:
            self._metadata[item_id] = metadata
        if relations:
            self._relations[item_id] = relations
    
    def get_item_with_context(self, item_id):
        return {
            'item': self._items.get(item_id),
            'metadata': self._metadata.get(item_id),
            'relations': self._relations.get(item_id)
        }

# ✅ Good: Simple data structure
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    price: float
    name: str = ""
    
    @property
    def total_price(self) -> float:
        return self.quantity * self.price

class Order:
    def __init__(self, customer_id: str):
        self.customer_id = customer_id
        self.items: List[OrderItem] = []
    
    def add_item(self, item: OrderItem):
        self.items.append(item)
    
    def get_total(self) -> float:
        return sum(item.total_price for item in self.items)
```

### 3. Composition Over Complex Inheritance

```python
# ❌ Bad: Complex inheritance hierarchy
class BaseNotification:
    def send(self): pass

class EmailNotification(BaseNotification):
    def send(self): pass

class SMSNotification(BaseNotification):
    def send(self): pass

class PushNotification(BaseNotification):
    def send(self): pass

class UrgentEmailNotification(EmailNotification):
    def send(self): pass

class UrgentSMSNotification(SMSNotification):
    def send(self): pass

# ... many more combinations

# ✅ Good: Simple composition
class EmailSender:
    def send(self, message: str, recipient: str) -> bool:
        # Email sending logic
        pass

class SMSSender:
    def send(self, message: str, phone: str) -> bool:
        # SMS sending logic
        pass

class PushSender:
    def send(self, message: str, device_id: str) -> bool:
        # Push notification logic
        pass

class NotificationService:
    def __init__(self):
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

Remember: KISS is about finding the sweet spot between oversimplification and unnecessary complexity. The goal is code that is as simple as possible while still being correct, secure, and maintainable.
