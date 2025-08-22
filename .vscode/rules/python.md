---
description: Python best practices for modern software development, including guidelines for package management with pip, Poetry, and uv.
globs: /**/*.py, src/**/*.py, tests/**/*.py, pyproject.toml, requirements.txt
---

# Python Development Guidelines

## 1. Project Structure

- **Layout**: Use a `src` layout (`src/your_package_name`).
- **Tests**: Place tests in a top-level `tests/` directory.
- **Configuration**: Manage environment-specific settings in a `config/` directory or via environment variables. Use a `.env` file for local development.
- **Static & Templates**: For web applications, store static files in `static/` and templates in `templates/`.

## 2. Dependency Management

When managing dependencies, adhere to the conventions of the package manager used in the project.

### **`pip` with `requirements.in` and `pip-tools`**

- **Source File**: Define abstract dependencies in `requirements.in`.
- **Lock File**: Generate a `requirements.txt` lock file using `pip-compile requirements.in`.
- **Installation**: Install dependencies using `pip install -r requirements.txt`.
- **Development Dependencies**: Manage development dependencies in a separate `requirements-dev.in`.

### **`Poetry`**

- **Configuration**: Define all project metadata and dependencies in `pyproject.toml`.
- **Lock File**: Use the `poetry.lock` file to ensure deterministic builds.
- **Installation**: Install dependencies with `poetry install`.
- **Dependency Management**: Add dependencies using `poetry add <package>` and for development, `poetry add --group dev <package>`.
- **Virtual Environment**: Let Poetry manage the virtual environment automatically.

### **`uv` (as a `pip` replacement)**

- **Virtual Environment**: Create and manage virtual environments with `uv venv`.
- **Installation**: Use `uv pip install -r requirements.txt` for faster installations.
- **Compilation**: Use `uv pip compile requirements.in -o requirements.txt` to generate lock files.
- **Workflow**: `uv` can be used as a high-performance drop-in replacement for `pip` and `pip-tools`.

## 3. Code Style & Formatting

- **Formatter**: Use **Black** for uncompromising code formatting.
- **Import Sorting**: Use **isort** to automatically sort and format imports.
- **Linting**: Use **Ruff** or **Flake8** for linting to catch common errors and style issues.
- **Naming Conventions (PEP 8)**:
  - `snake_case` for functions, methods, and variables.
  - `PascalCase` for classes.
  - `UPPER_SNAKE_CASE` for constants.
- **Line Length**: Keep lines under 88 characters (Black's default).
- **Imports**: Prefer absolute imports (`from my_project.module import my_function`) over relative ones.

## 4. Type Hinting

- **Coverage**: Provide type hints for all function signatures (arguments and return values).
- **Clarity**: Use the `typing` module for complex types (`List`, `Dict`, `Tuple`, `Callable`).
- **Optionality**: Use `Optional[str]` or, in Python 3.10+, the more concise `str | None`.
- **Generics**: Use `TypeVar` for creating generic functions and classes.

## 5. Web Frameworks (Flask/FastAPI)

- **Application Factory**: Use the factory pattern (`create_app`) to initialize your application.
- **Blueprints/Routers**: Organize routes into logical groups using Blueprints (Flask) or APIRouters (FastAPI).
- **Dependencies**: Use a dependency injection framework where appropriate (e.g., FastAPI's `Depends`).

## 6. Database

- **ORM**: Use **SQLAlchemy ORM** for database interactions.
- **Migrations**: Manage database schema changes with **Alembic**.
- **Models**: Define database models in a dedicated `models/` or `db/` directory.
- **Session Management**: Use a session scope that is tied to the request lifecycle.

## 7. Testing

- **Framework**: Use **pytest** as the primary testing framework.
- **Fixtures**: Use `pytest.fixture` to provide reusable setup and teardown logic.
- **Mocking**: Use `pytest-mock` or `unittest.mock` for mocking objects and functions.
- **Coverage**: Measure test coverage with `pytest-cov`. Aim for high coverage on critical business logic.
- **Organization**: Mirror the `src` directory structure in your `tests` directory.

## 8. Security

- **Input Sanitization**: Never trust user input. Sanitize and validate all incoming data.
- **Secrets Management**: Load secrets from environment variables. Do not hardcode credentials.
- **Dependencies**: Regularly scan dependencies for vulnerabilities using tools like `pip-audit` or `safety`.

## 9. Development Workflow

- **Virtual Environments**: Always work inside a virtual environment (`.venv`).
- **Pre-commit Hooks**: Use `pre-commit` to run linters, formatters, and tests before each commit.
- **CI/CD**: Implement a CI/CD pipeline to automate testing, building, and deployment.
