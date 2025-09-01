---
description: SOLID principles guide for software design and AI code generation to ensure maintainable and scalable code.
globs:
alwaysApply: true
---

# SOLID Principles

Whenever you use this rule, start your message with the following:

"Applying SOLID principles..."

This rule ensures that all AI-generated code follows the five SOLID principles of object-oriented design to create maintainable, flexible, and extensible software.

## Overview of SOLID

**SOLID** is an acronym for five design principles:

- **S** - Single Responsibility Principle (SRP)
- **O** - Open/Closed Principle (OCP)
- **L** - Liskov Substitution Principle (LSP)
- **I** - Interface Segregation Principle (ISP)
- **D** - Dependency Inversion Principle (DIP)

## 1. Single Responsibility Principle (SRP)

**Definition:** A class should have only one reason to change, meaning it should have only one job or responsibility.

**Implementation Guidelines:**

- Each class should focus on a single concern
- Separate data access, business logic, and presentation
- Split large classes with multiple responsibilities
- Use composition to combine single-purpose classes

**Code Examples:**

```python
# ❌ Bad: Multiple responsibilities
class UserManager:
    def create_user(self, user_data):
        # Validation logic
        if not user_data.get('email'):
            raise ValueError("Email required")
        
        # Database logic
        self.db.insert('users', user_data)
        
        # Email logic
        self.send_welcome_email(user_data['email'])
        
        # Logging logic
        self.log_user_creation(user_data)

# ✅ Good: Single responsibilities
class UserValidator:
    def validate(self, user_data):
        if not user_data.get('email'):
            raise ValueError("Email required")
        if not user_data.get('name'):
            raise ValueError("Name required")

class UserRepository:
    def __init__(self, database):
        self.db = database
    
    def save(self, user):
        return self.db.insert('users', user)

class EmailService:
    def send_welcome_email(self, email):
        # Email sending logic
        pass

class UserService:
    def __init__(self, validator, repository, email_service, logger):
        self.validator = validator
        self.repository = repository
        self.email_service = email_service
        self.logger = logger
    
    def create_user(self, user_data):
        self.validator.validate(user_data)
        user = self.repository.save(user_data)
        self.email_service.send_welcome_email(user_data['email'])
        self.logger.log_user_creation(user_data)
        return user
```

```typescript
// ✅ Good: TypeScript SRP example
interface PaymentProcessor {
    processPayment(amount: number, method: string): Promise<boolean>;
}

interface PaymentLogger {
    logTransaction(transactionId: string, amount: number): void;
}

interface PaymentValidator {
    validateAmount(amount: number): boolean;
    validatePaymentMethod(method: string): boolean;
}

class StripePaymentProcessor implements PaymentProcessor {
    async processPayment(amount: number, method: string): Promise<boolean> {
        // Only handles Stripe payment processing
        return true;
    }
}

class PaymentTransactionLogger implements PaymentLogger {
    logTransaction(transactionId: string, amount: number): void {
        // Only handles logging
        console.log(`Transaction ${transactionId}: $${amount}`);
    }
}
```

## 2. Open/Closed Principle (OCP)

**Definition:** Software entities should be open for extension but closed for modification.

**Implementation Guidelines:**

- Use abstractions (interfaces/abstract classes) for extensibility
- Implement new functionality by adding new classes, not modifying existing ones
- Use Strategy, Observer, and other design patterns
- Favor composition and dependency injection

**Code Examples:**

```python
# ✅ Good: Open for extension, closed for modification
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

class BuyOneGetOneDiscount(DiscountCalculator):
    def calculate_discount(self, amount: float) -> float:
        # New discount type added without modifying existing code
        return amount * 0.5

class Order:
    def __init__(self, amount: float, discount_calculator: DiscountCalculator):
        self.amount = amount
        self.discount_calculator = discount_calculator
    
    def get_final_amount(self) -> float:
        discount = self.discount_calculator.calculate_discount(self.amount)
        return self.amount - discount
```

```typescript
// ✅ Good: TypeScript OCP with Strategy pattern
interface ShippingStrategy {
    calculateCost(weight: number, distance: number): number;
    getEstimatedDelivery(): number; // days
}

class StandardShipping implements ShippingStrategy {
    calculateCost(weight: number, distance: number): number {
        return weight * 0.5 + distance * 0.1;
    }
    
    getEstimatedDelivery(): number {
        return 7;
    }
}

class ExpressShipping implements ShippingStrategy {
    calculateCost(weight: number, distance: number): number {
        return weight * 1.0 + distance * 0.2;
    }
    
    getEstimatedDelivery(): number {
        return 2;
    }
}

class ShippingCalculator {
    constructor(private strategy: ShippingStrategy) {}
    
    calculate(weight: number, distance: number): {cost: number, days: number} {
        return {
            cost: this.strategy.calculateCost(weight, distance),
            days: this.strategy.getEstimatedDelivery()
        };
    }
    
    // Can change strategy without modifying this class
    setStrategy(strategy: ShippingStrategy): void {
        this.strategy = strategy;
    }
}
```

## 3. Liskov Substitution Principle (LSP)

**Definition:** Objects of a superclass should be replaceable with objects of a subclass without breaking the application.

**Implementation Guidelines:**

- Derived classes must be substitutable for their base classes
- Preserve the contract defined by the base class
- Don't strengthen preconditions or weaken postconditions
- Avoid throwing new exceptions in derived classes

**Code Examples:**

```python
# ❌ Bad: Violates LSP
class Bird:
    def fly(self):
        return "Flying high!"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates LSP

# ✅ Good: Follows LSP
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "Flying high!"
    
    def make_sound(self):
        return "Chirp!"

class Penguin(Bird):
    def move(self):
        return "Swimming gracefully!"
    
    def make_sound(self):
        return "Squawk!"

class Eagle(FlyingBird):
    def move(self):
        return "Soaring majestically!"

# Both can be used interchangeably as Bird
def bird_sanctuary(birds: list[Bird]):
    for bird in birds:
        print(f"Bird moves: {bird.move()}")
        print(f"Bird sounds: {bird.make_sound()}")
```

```python
# ✅ Good: Rectangle/Square LSP-compliant design
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height
    
    def area(self) -> float:
        return self._width * self._height

class Square(Shape):
    def __init__(self, side: float):
        self._side = side
    
    @property
    def side(self) -> float:
        return self._side
    
    def area(self) -> float:
        return self._side ** 2

# Factory pattern to create shapes
class ShapeFactory:
    @staticmethod
    def create_rectangle(width: float, height: float) -> Shape:
        if width == height:
            return Square(width)
        return Rectangle(width, height)
```

## 4. Interface Segregation Principle (ISP)

**Definition:** No client should be forced to depend on methods it does not use.

**Implementation Guidelines:**

- Create specific, focused interfaces
- Split large interfaces into smaller, cohesive ones
- Use role-based interfaces
- Avoid fat interfaces with unrelated methods

**Code Examples:**

```python
# ❌ Bad: Fat interface
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass

class Robot(Worker):
    def work(self):
        return "Robot working"
    
    def eat(self):
        raise NotImplementedError("Robots don't eat")  # Forced to implement
    
    def sleep(self):
        raise NotImplementedError("Robots don't sleep")  # Forced to implement

# ✅ Good: Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        return "Human working"
    
    def eat(self):
        return "Human eating"
    
    def sleep(self):
        return "Human sleeping"

class Robot(Workable):
    def work(self):
        return "Robot working"
    # Only implements what it needs
```

```typescript
// ✅ Good: TypeScript ISP example
interface Readable {
    read(): string;
}

interface Writable {
    write(data: string): boolean;
}

interface Executable {
    execute(): void;
}

// Clients only depend on what they need
class TextFile implements Readable, Writable {
    read(): string {
        return "File content";
    }
    
    write(data: string): boolean {
        // Write implementation
        return true;
    }
}

class Script implements Readable, Executable {
    read(): string {
        return "Script content";
    }
    
    execute(): void {
        // Execution logic
    }
}

class ReadOnlyDocument implements Readable {
    read(): string {
        return "Document content";
    }
    // Doesn't need to implement write or execute
}
```

## 5. Dependency Inversion Principle (DIP)

**Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Implementation Guidelines:**

- Depend on abstractions, not concretions
- Use dependency injection
- Create interfaces for external dependencies
- Invert control flow through abstractions

**Code Examples:**

```python
# ❌ Bad: High-level module depends on low-level module
class MySQLDatabase:
    def save(self, data):
        # MySQL-specific implementation
        pass

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency
    
    def create_user(self, user_data):
        self.database.save(user_data)

# ✅ Good: Dependency inversion
class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass
    
    @abstractmethod
    def find(self, criteria):
        pass

class MySQLDatabase(DatabaseInterface):
    def save(self, data):
        # MySQL implementation
        pass
    
    def find(self, criteria):
        # MySQL find implementation
        pass

class PostgreSQLDatabase(DatabaseInterface):
    def save(self, data):
        # PostgreSQL implementation
        pass
    
    def find(self, criteria):
        # PostgreSQL find implementation
        pass

class UserService:
    def __init__(self, database: DatabaseInterface):
        self.database = database  # Depends on abstraction
    
    def create_user(self, user_data):
        self.database.save(user_data)
    
    def find_user(self, criteria):
        return self.database.find(criteria)

# Dependency injection
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()
user_service = UserService(mysql_db)  # Can easily switch databases
```

```typescript
// ✅ Good: TypeScript DIP with dependency injection
interface Logger {
    log(message: string, level: string): void;
}

interface EmailService {
    sendEmail(to: string, subject: string, body: string): Promise<boolean>;
}

class ConsoleLogger implements Logger {
    log(message: string, level: string): void {
        console.log(`[${level}] ${message}`);
    }
}

class FileLogger implements Logger {
    log(message: string, level: string): void {
        // Write to file
    }
}

class SMTPEmailService implements EmailService {
    async sendEmail(to: string, subject: string, body: string): Promise<boolean> {
        // SMTP implementation
        return true;
    }
}

class NotificationService {
    constructor(
        private logger: Logger,
        private emailService: EmailService
    ) {}
    
    async sendWelcomeNotification(userEmail: string): Promise<void> {
        try {
            const success = await this.emailService.sendEmail(
                userEmail,
                "Welcome!",
                "Welcome to our service!"
            );
            
            if (success) {
                this.logger.log(`Welcome email sent to ${userEmail}`, "INFO");
            } else {
                this.logger.log(`Failed to send email to ${userEmail}`, "ERROR");
            }
        } catch (error) {
            this.logger.log(`Error sending email: ${error}`, "ERROR");
        }
    }
}

// Dependency injection container usage
const logger = new ConsoleLogger();
const emailService = new SMTPEmailService();
const notificationService = new NotificationService(logger, emailService);
```

## Advanced SOLID Patterns

### Combining Multiple Principles

```python
# Example combining all SOLID principles
class OrderProcessor:
    """
    SRP: Only handles order processing orchestration
    OCP: Open for extension through new payment/shipping strategies
    LSP: All payment processors are substitutable
    ISP: Separate interfaces for different concerns
    DIP: Depends on abstractions, not concretions
    """
    
    def __init__(self, 
                 payment_processor: PaymentProcessor,
                 shipping_calculator: ShippingCalculator,
                 inventory_service: InventoryService,
                 notification_service: NotificationService):
        self._payment_processor = payment_processor
        self._shipping_calculator = shipping_calculator
        self._inventory_service = inventory_service
        self._notification_service = notification_service
    
    def process_order(self, order: Order) -> OrderResult:
        # Orchestrate the order processing
        if not self._inventory_service.is_available(order.items):
            return OrderResult.insufficient_inventory()
        
        shipping_cost = self._shipping_calculator.calculate(order)
        total_cost = order.subtotal + shipping_cost
        
        if self._payment_processor.process_payment(total_cost, order.payment_method):
            self._inventory_service.reserve_items(order.items)
            self._notification_service.send_confirmation(order.customer)
            return OrderResult.success(order.id)
        
        return OrderResult.payment_failed()
```

### Factory Pattern with SOLID

```python
class PaymentProcessorFactory:
    """Factory following OCP and DIP"""
    
    @staticmethod
    def create_processor(processor_type: str, config: dict) -> PaymentProcessor:
        processors = {
            'stripe': lambda: StripePaymentProcessor(config['api_key']),
            'paypal': lambda: PayPalPaymentProcessor(config['client_id']),
            'square': lambda: SquarePaymentProcessor(config['access_token'])
        }
        
        if processor_type not in processors:
            raise ValueError(f"Unknown processor type: {processor_type}")
        
        return processors[processor_type]()
```

## Testing SOLID Code

### Unit Testing Guidelines

```python
class TestUserService:
    def setup_method(self):
        # Mock dependencies (DIP makes this easy)
        self.mock_validator = Mock(spec=UserValidator)
        self.mock_repository = Mock(spec=UserRepository)
        self.mock_email_service = Mock(spec=EmailService)
        self.mock_logger = Mock(spec=Logger)
        
        self.user_service = UserService(
            self.mock_validator,
            self.mock_repository,
            self.mock_email_service,
            self.mock_logger
        )
    
    def test_create_user_success(self):
        # Arrange
        user_data = {'email': 'test@example.com', 'name': 'Test User'}
        expected_user = User(id=1, email='test@example.com', name='Test User')
        
        self.mock_validator.validate.return_value = None
        self.mock_repository.save.return_value = expected_user
        
        # Act
        result = self.user_service.create_user(user_data)
        
        # Assert
        assert result == expected_user
        self.mock_validator.validate.assert_called_once_with(user_data)
        self.mock_repository.save.assert_called_once_with(user_data)
        self.mock_email_service.send_welcome_email.assert_called_once()
        self.mock_logger.log_user_creation.assert_called_once()
```

## Common SOLID Violations and Fixes

### SRP Violations

```python
# ❌ Bad: God class
class OrderManager:
    def validate_order(self): pass
    def calculate_tax(self): pass
    def process_payment(self): pass
    def send_email(self): pass
    def update_inventory(self): pass
    def generate_invoice(self): pass

# ✅ Good: Separate responsibilities
class OrderValidator: pass
class TaxCalculator: pass
class PaymentProcessor: pass
class EmailService: pass
class InventoryService: pass
class InvoiceGenerator: pass
```

### OCP Violations

```python
# ❌ Bad: Modifying existing code for new requirements
class ShippingCalculator:
    def calculate_cost(self, shipping_type, weight, distance):
        if shipping_type == "standard":
            return weight * 0.5 + distance * 0.1
        elif shipping_type == "express":
            return weight * 1.0 + distance * 0.2
        elif shipping_type == "overnight":  # Added by modifying existing code
            return weight * 2.0 + distance * 0.5

# ✅ Good: Extension without modification
class ShippingCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy
    
    def calculate_cost(self, weight, distance):
        return self.strategy.calculate(weight, distance)
```

## Performance Considerations

### SOLID and Performance

- Abstraction layers can introduce overhead
- Use dependency injection containers wisely
- Consider object creation costs
- Profile and optimize critical paths
- Balance flexibility with performance requirements

### Optimization Strategies

```python
# Use dependency injection containers for expensive objects
class DIContainer:
    def __init__(self):
        self._instances = {}
        self._factories = {}
    
    def register_singleton(self, interface, implementation):
        self._factories[interface] = lambda: implementation
    
    def get(self, interface):
        if interface not in self._instances:
            self._instances[interface] = self._factories[interface]()
        return self._instances[interface]
```

## Validation Checklist

Before completing any SOLID implementation, verify:

- [ ] **SRP**: Each class has a single, well-defined responsibility
- [ ] **OCP**: New functionality can be added without modifying existing code
- [ ] **LSP**: Derived classes can replace base classes without breaking functionality
- [ ] **ISP**: Interfaces are focused and clients only depend on methods they use
- [ ] **DIP**: High-level modules depend on abstractions, not concrete implementations
- [ ] Dependencies are injected rather than hard-coded
- [ ] Code is easily testable with mocked dependencies
- [ ] Abstractions are stable and well-defined
- [ ] No circular dependencies exist
- [ ] Performance implications are considered and acceptable

## Integration with Other Principles

SOLID principles complement:

- **OOP principles**: Provide structure for encapsulation, inheritance, polymorphism
- **DRY principle**: Through proper abstraction and inheritance
- **KISS principle**: By creating focused, single-purpose components
- **YAGNI principle**: By avoiding over-engineering while maintaining flexibility

Remember: SOLID principles help create maintainable, flexible, and testable code that can evolve with changing requirements while minimizing the risk of introducing bugs.
