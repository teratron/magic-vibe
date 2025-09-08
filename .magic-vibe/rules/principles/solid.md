# SOLID Principles

> **Magic Vibe Rule: SOLID Design Principles**  
> **Category:** Principles  
> **Priority:** High  
> **File Size:** ~9KB (AI-optimized)  
> **Dependencies:** `@rules/principles/kiss.md`, `@rules/principles/dry.md`

SOLID principles guide for creating maintainable, flexible, and extensible code. Essential for AI agents generating scalable object-oriented designs.

**SOLID Acronym:**

- **S** - Single Responsibility Principle (SRP)
- **O** - Open/Closed Principle (OCP)
- **L** - Liskov Substitution Principle (LSP)
- **I** - Interface Segregation Principle (ISP)
- **D** - Dependency Inversion Principle (DIP)

## 1. Implementation Guidelines

### 1.1. Single Responsibility Principle (SRP)

**Definition:** A class should have only one reason to change - one job or responsibility.

```python
# ❌ Bad: Multiple responsibilities
class UserManager:
    def create_user(self, user_data):
        # Validation, database, email, logging - too much!
        if not user_data.get('email'):
            raise ValueError("Email required")
        self.db.insert('users', user_data)
        self.send_welcome_email(user_data['email'])

# ✅ Good: Single responsibilities
class UserValidator:
    def validate(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email required")

class UserRepository:
    def save(self, user):
        return self.db.insert('users', user)

class UserService:
    def __init__(self, validator, repository, email_service):
        self.validator = validator
        self.repository = repository
        self.email_service = email_service
    
    def create_user(self, user_data):
        self.validator.validate(user_data)
        user = self.repository.save(user_data)
        self.email_service.send_welcome_email(user_data['email'])
        return user
```

### 1.2. Open/Closed Principle (OCP)

**Definition:** Open for extension, closed for modification.

```python
# ✅ Good: Extensible without modification
from abc import ABC, abstractmethod

class DiscountCalculator(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass

class PercentageDiscount(DiscountCalculator):
    def __init__(self, percentage: float):
        self.percentage = percentage
    
    def calculate_discount(self, amount: float) -> float:
        return amount * (self.percentage / 100)

class FixedAmountDiscount(DiscountCalculator):
    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount
    
    def calculate_discount(self, amount: float) -> float:
        return min(self.fixed_amount, amount)

# New discount types can be added without modifying existing code
class BuyOneGetOneDiscount(DiscountCalculator):
    def calculate_discount(self, amount: float) -> float:
        return amount * 0.5
```

### 1.3. Liskov Substitution Principle (LSP)

**Definition:** Objects of a superclass should be replaceable with objects of subclasses.

```python
# ✅ Good: LSP-compliant design
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    def area(self) -> float:
        return self._width * self._height

class Square(Shape):
    def __init__(self, side: float):
        self._side = side
    
    def area(self) -> float:
        return self._side ** 2

# Both can be used interchangeably as Shape
def calculate_total_area(shapes: list[Shape]) -> float:
    return sum(shape.area() for shape in shapes)
```

### 1.4. Interface Segregation Principle (ISP)

**Definition:** No client should be forced to depend on methods it doesn't use.

```python
# ✅ Good: Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Human working"
    
    def eat(self):
        return "Human eating"

class Robot(Workable):
    def work(self):
        return "Robot working"
    # Only implements what it needs
```

### 1.5. Dependency Inversion Principle (DIP)

**Definition:** Depend on abstractions, not concretions.

```python
# ✅ Good: Dependency inversion
class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(DatabaseInterface):
    def save(self, data):
        # MySQL implementation
        pass

class UserService:
    def __init__(self, database: DatabaseInterface):
        self.database = database  # Depends on abstraction
    
    def create_user(self, user_data):
        return self.database.save(user_data)

# Dependency injection
mysql_db = MySQLDatabase()
user_service = UserService(mysql_db)  # Can easily switch databases
```

## 2. Change Management Protocols

### 2.1. SOLID Refactoring Process

**Refactoring Guidelines:**

1. **Identify Violations** - Use static analysis tools
2. **Extract Responsibilities** - Split multi-purpose classes
3. **Create Abstractions** - Define interfaces for extensibility
4. **Inject Dependencies** - Replace hard-coded dependencies
5. **Validate Changes** - Ensure substitutability works

### 2.2. Code Review Checklist

**SOLID Validation:**

- [ ] Each class has single responsibility
- [ ] New features extend without modification
- [ ] Subclasses are substitutable for base classes
- [ ] Interfaces are focused and specific
- [ ] Dependencies are injected, not hard-coded

## 3. Communication Standards

### 3.1. SOLID Documentation

**Clear Interface Documentation:**

```python
class PaymentProcessor(ABC):
    """Process payment transactions.
    
    Contract:
    - Must validate payment method before processing
    - Must return boolean indicating success/failure
    - Must not modify payment data
    - Must handle network failures gracefully
    """
    
    @abstractmethod
    def process_payment(self, amount: float, method: str) -> bool:
        """Process payment and return success status.
        
        Args:
            amount: Payment amount (must be > 0)
            method: Payment method ('card', 'paypal', etc.)
            
        Returns:
            True if payment successful, False otherwise
            
        Raises:
            ValueError: If amount <= 0 or invalid method
        """
        pass
```

## 4. Quality Assurance Framework

### 4.1. SOLID Testing Strategies

```python
# Test single responsibilities independently
class TestUserValidator:
    def test_validate_email_required(self):
        validator = UserValidator()
        with pytest.raises(ValueError, match="Email required"):
            validator.validate({'name': 'John'})

# Test substitutability (LSP)
class TestShapeSubstitution:
    @pytest.mark.parametrize("shape_class,args", [
        (Rectangle, (5, 10)),
        (Square, (5,))
    ])
    def test_shape_area_calculation(self, shape_class, args):
        shape = shape_class(*args)
        area = shape.area()
        assert isinstance(area, (int, float))
        assert area > 0
```

### 4.2. SOLID Metrics

**Quality Metrics:**

- **SRP Compliance**: Functions < 20 lines, single purpose
- **OCP Compliance**: Extension points identified and used
- **LSP Compliance**: Substitution tests pass
- **ISP Compliance**: Interface methods < 10, focused
- **DIP Compliance**: Dependency injection coverage > 90%

## 5. Security & Performance Guidelines

### 5.1. Secure SOLID Design

```python
# Secure dependency injection
class SecureUserService:
    def __init__(self, 
                 validator: UserValidator,
                 repository: UserRepository,
                 hasher: PasswordHasher):
        self._validator = validator
        self._repository = repository
        self._hasher = hasher
    
    def create_user(self, user_data):
        self._validator.validate(user_data)
        user_data['password'] = self._hasher.hash(user_data['password'])
        return self._repository.save(user_data)
```

## 6. Integration & Compatibility

### 6.1. Framework Integration

```python
# SOLID patterns work across frameworks
class OrderProcessor:
    def __init__(self, 
                 payment_processor: PaymentProcessor,
                 inventory_service: InventoryService):
        self._payment_processor = payment_processor
        self._inventory_service = inventory_service
    
    def process_order(self, order: Order) -> OrderResult:
        if not self._inventory_service.is_available(order.items):
            return OrderResult.insufficient_inventory()
        
        if self._payment_processor.process_payment(order.total, order.payment_method):
            self._inventory_service.reserve_items(order.items)
            return OrderResult.success(order.id)
        
        return OrderResult.payment_failed()
```

## 7. Monitoring & Maintenance

### 7.1. SOLID Compliance Monitoring

```python
# Monitor SOLID compliance with metrics
class SOLIDMetrics:
    def analyze_class(self, class_obj):
        return {
            'srp_score': self._check_single_responsibility(class_obj),
            'method_count': len([m for m in dir(class_obj) if not m.startswith('_')]),
            'dependency_count': self._count_dependencies(class_obj)
        }
```

### 7.2. Refactoring Guidelines

**Regular SOLID Reviews:**

- Monthly code review for SOLID compliance
- Identify classes with multiple responsibilities
- Extract interfaces for better abstraction
- Review dependency injection usage

## 8. AI Agent Optimization

### 8.1. AI-Friendly SOLID Patterns

```python
# Clear patterns for AI code generation
class PaymentProcessorFactory:
    """Factory following OCP and DIP principles."""
    
    @staticmethod
    def create_processor(processor_type: str, config: dict) -> PaymentProcessor:
        processors = {
            'stripe': lambda: StripePaymentProcessor(config['api_key']),
            'paypal': lambda: PayPalPaymentProcessor(config['client_id'])
        }
        
        if processor_type not in processors:
            raise ValueError(f"Unknown processor type: {processor_type}")
        
        return processors[processor_type]()

# AI can easily recognize and generate SOLID patterns
class BaseService(ABC):
    """Template for service classes following SOLID."""
    
    @abstractmethod
    def process(self, data):
        pass
    
    def validate_input(self, data):
        """Common validation logic."""
        if not data:
            raise ValueError("Data is required")
```

### 8.2. Pattern Recognition

**SOLID patterns AI should recognize:**

- Repository pattern (DIP)
- Strategy pattern (OCP)
- Factory pattern (SRP + OCP)
- Interface segregation (ISP)
- Dependency injection (DIP)

### 8.3. Validation Checklist

**AI agents must verify:**

- [ ] Each class has single responsibility
- [ ] Extensions don't modify existing code
- [ ] Subclasses are substitutable
- [ ] Interfaces are client-specific
- [ ] Dependencies are injected

---

**Magic Vibe SOLID Principles v2.1.0** - Maintainable object-oriented design

**Last Updated:** 2025-09-08 | **File Size:** ~9KB | **Status:** Active*
