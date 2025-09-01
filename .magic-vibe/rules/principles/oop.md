---
description: Object-Oriented Programming (OOP) principles guide for AI code generation and development practices.
globs:
alwaysApply: true
---

# Object-Oriented Programming (OOP) Principles

Whenever you use this rule, start your message with the following:

"Applying OOP principles..."

This rule ensures that all AI-generated code follows fundamental Object-Oriented Programming principles to create maintainable, scalable, and reusable code.

## Core OOP Principles

### 1. Encapsulation

**Definition:** Bundle data and methods that operate on that data within a single unit (class) while hiding internal implementation details.

**Implementation Guidelines:**

- Use private/protected access modifiers appropriately
- Provide public interfaces through getter/setter methods when needed
- Hide internal state and implementation details
- Group related functionality within the same class

**Code Examples:**

```python
# ✅ Good: Proper encapsulation
class BankAccount:
    def __init__(self, initial_balance: float):
        self._balance = initial_balance  # Protected attribute
        self._transaction_history = []   # Private data
    
    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposit: +{amount}")
            return True
        return False
    
    def get_balance(self) -> float:
        return self._balance
    
    # Internal helper method
    def _log_transaction(self, transaction: str):
        self._transaction_history.append(transaction)

# ❌ Bad: No encapsulation
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance  # Public access to sensitive data
```

```typescript
// ✅ Good: TypeScript encapsulation
class UserService {
    private users: Map<string, User> = new Map();
    private readonly maxUsers = 1000;
    
    public addUser(user: User): boolean {
        if (this.users.size >= this.maxUsers) {
            return false;
        }
        this.users.set(user.id, user);
        return true;
    }
    
    public getUser(id: string): User | null {
        return this.users.get(id) || null;
    }
    
    private validateUser(user: User): boolean {
        return user.id && user.email;
    }
}
```

### 2. Inheritance

**Definition:** Create new classes based on existing classes, inheriting their properties and methods while adding or modifying functionality.

**Implementation Guidelines:**

- Use inheritance to model "is-a" relationships
- Prefer composition over inheritance when appropriate
- Follow the Liskov Substitution Principle
- Use abstract classes and interfaces for shared contracts

**Code Examples:**

```python
# ✅ Good: Proper inheritance hierarchy
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
    
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    def sleep(self) -> str:
        return f"{self.name} is sleeping"

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "Canine")
        self.breed = breed
    
    def make_sound(self) -> str:
        return "Woof!"
    
    def fetch(self) -> str:
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def __init__(self, name: str, indoor: bool):
        super().__init__(name, "Feline")
        self.indoor = indoor
    
    def make_sound(self) -> str:
        return "Meow!"
```

### 3. Polymorphism

**Definition:** Allow objects of different types to be treated uniformly through a common interface.

**Implementation Guidelines:**

- Implement method overriding in derived classes
- Use interfaces and abstract methods for contracts
- Enable runtime method resolution
- Support duck typing where appropriate

**Code Examples:**

```python
# ✅ Good: Polymorphism in action
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

# Polymorphic usage
def print_shape_info(shapes: list[Shape]):
    for shape in shapes:
        print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```

### 4. Abstraction

**Definition:** Hide complex implementation details while exposing only essential features through simplified interfaces.

**Implementation Guidelines:**

- Use abstract classes and interfaces
- Hide implementation complexity
- Provide clear, simple public APIs
- Focus on what an object does, not how it does it

**Code Examples:**

```python
# ✅ Good: Abstraction with clear interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, payment_method: str) -> bool:
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> bool:
        pass

class StripePaymentProcessor(PaymentProcessor):
    def __init__(self, api_key: str):
        self._stripe_client = self._initialize_stripe(api_key)
    
    def process_payment(self, amount: float, payment_method: str) -> bool:
        # Complex Stripe-specific implementation hidden
        return self._stripe_client.charge(amount, payment_method)
    
    def refund_payment(self, transaction_id: str, amount: float) -> bool:
        # Complex refund logic hidden
        return self._stripe_client.refund(transaction_id, amount)
    
    def _initialize_stripe(self, api_key: str):
        # Private implementation detail
        pass
```

## Advanced OOP Patterns

### Composition Over Inheritance

**Principle:** Favor object composition over class inheritance to achieve greater flexibility.

```python
# ✅ Good: Using composition
class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class GPS:
    def get_location(self):
        return "Current location: 40.7128, -74.0060"

class Car:
    def __init__(self, engine: Engine, gps: GPS):
        self.engine = engine  # Composition
        self.gps = gps       # Composition
    
    def start_journey(self):
        engine_status = self.engine.start()
        location = self.gps.get_location()
        return f"{engine_status}. {location}"
```

### Interface Segregation in Practice

```python
# ✅ Good: Specific interfaces
class Readable(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

class Writable(ABC):
    @abstractmethod
    def write(self, data: str) -> bool:
        pass

class FileHandler(Readable, Writable):
    def read(self) -> str:
        # Implementation
        pass
    
    def write(self, data: str) -> bool:
        # Implementation
        pass
```

## Language-Specific OOP Guidelines

### Python OOP Best Practices

- Use `@property` decorators for computed attributes
- Implement `__str__` and `__repr__` methods
- Use `@classmethod` and `@staticmethod` appropriately
- Follow PEP 8 naming conventions

### TypeScript/JavaScript OOP Best Practices

- Use TypeScript interfaces for type safety
- Implement proper access modifiers
- Use readonly properties when appropriate
- Leverage generics for type flexibility

### C++ OOP Best Practices

- Use RAII (Resource Acquisition Is Initialization)
- Implement rule of three/five/zero
- Use virtual destructors in base classes
- Prefer smart pointers for memory management

## Common OOP Anti-Patterns to Avoid

### 1. God Object

```python
# ❌ Bad: God object with too many responsibilities
class UserManager:
    def create_user(self): pass
    def authenticate_user(self): pass
    def send_email(self): pass
    def generate_report(self): pass
    def manage_database(self): pass
    def handle_payments(self): pass
```

### 2. Inappropriate Inheritance

```python
# ❌ Bad: Square inheriting from Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):  # Violates Liskov Substitution Principle
    def __init__(self, side):
        super().__init__(side, side)
```

### 3. Excessive Coupling

```python
# ❌ Bad: Tight coupling
class EmailService:
    def __init__(self):
        self.database = MySQLDatabase()  # Tight coupling
        self.logger = FileLogger()       # Tight coupling
```

## Testing OOP Code

### Unit Testing Guidelines

- Mock dependencies and external services
- Test public interfaces, not private implementation
- Use dependency injection for testability
- Create test doubles for complex objects

```python
# ✅ Good: Testable OOP design
class OrderService:
    def __init__(self, payment_processor: PaymentProcessor, 
                 email_service: EmailService):
        self.payment_processor = payment_processor
        self.email_service = email_service
    
    def process_order(self, order: Order) -> bool:
        if self.payment_processor.process_payment(order.total):
            self.email_service.send_confirmation(order.customer_email)
            return True
        return False

# Test with mocks
def test_process_order():
    mock_payment = Mock(spec=PaymentProcessor)
    mock_email = Mock(spec=EmailService)
    service = OrderService(mock_payment, mock_email)
    
    mock_payment.process_payment.return_value = True
    result = service.process_order(test_order)
    
    assert result is True
    mock_email.send_confirmation.assert_called_once()
```

## Documentation Requirements

### Class Documentation

- Document class purpose and responsibilities
- Describe public methods and their contracts
- Include usage examples
- Document any thread-safety considerations

### Method Documentation

- Specify parameters and return types
- Document side effects
- Include preconditions and postconditions
- Provide examples for complex methods

## Performance Considerations

### Object Creation

- Use object pooling for expensive objects
- Consider lazy initialization
- Implement caching where appropriate
- Monitor memory usage in inheritance hierarchies

### Method Calls

- Be aware of virtual method call overhead
- Use final/sealed classes when inheritance isn't needed
- Consider inlining for frequently called methods

## Validation Checklist

Before completing any OOP implementation, verify:

- [ ] Classes have single, well-defined responsibilities
- [ ] Encapsulation is properly implemented
- [ ] Inheritance relationships are logical and follow LSP
- [ ] Polymorphism is used effectively
- [ ] Abstraction levels are appropriate
- [ ] No God objects or inappropriate coupling
- [ ] Public interfaces are clean and minimal
- [ ] Code is testable with clear dependencies
- [ ] Documentation is complete and accurate
- [ ] Performance implications are considered

## Integration with Other Principles

OOP principles work together with:

- **SOLID principles** (especially SRP, OCP, LSP, ISP)
- **DRY principle** through inheritance and composition
- **KISS principle** by keeping class interfaces simple
- **YAGNI principle** by not over-engineering class hierarchies

**Remember:** Good OOP design creates code that is maintainable, extensible, and easy to understand while avoiding common pitfalls and anti-patterns.
