# Contributing

Thank you for your interest in contributing to nox-mcp!

## Development Setup

### Prerequisites

- Python 3.10+
- Git
- [uv](https://docs.astral.sh/uv/) package manager

### Clone and Install

```bash
git clone https://github.com/rvforest/nox-mcp.git
cd nox-mcp
uv sync
```

This creates a virtual environment and installs all dependencies.

### Pre-commit Hooks (Optional)

Install pre-commit hooks to run checks before each commit:

```bash
uv run pre-commit install
```

## Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and add tests

3. Run tests:
   ```bash
   uv run nox -s test
   ```

4. Run all quality checks:
   ```bash
   uv run nox -s check
   ```

5. Commit and push your changes

6. Open a pull request on GitHub

## Common Commands

| Command | Description |
|---------|-------------|
| `uv run nox -s test` | Run the test suite |
| `uv run nox -s check` | Run all linting and type checks |
| `uv run nox -s format` | Format code with Ruff |
| `uv run nox -s lint` | Check linting issues |
| `uv run nox -s types` | Run pyrefly type checking |
| `uv run nox -s docs` | Build documentation |
| `uv run nox -s livedocs` | Live preview documentation |
| `uv run nox -s coverage` | Run tests with coverage report |

## Code Standards

### Style

We use [Ruff](https://github.com/astral-sh/ruff) for formatting and linting. Format your code with:

```bash
uv run nox -s format
```

### Type Hints

All public functions and methods must have type hints:

```python
def example_function(param1: str, param2: int) -> bool:
    """Example function with type hints."""
    return len(param1) > param2
```

### Docstrings

Use [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for all public APIs:

```python
def example_function(param1: str, param2: int) -> bool:
    """Brief description of the function.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ValueError: When param1 is empty.
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    return len(param1) > param2
```

## Testing

Tests live in the `tests/` directory and use [pytest](https://docs.pytest.org/). Run specific tests with:

```bash
uv run pytest tests/test_server.py -v
```

## Documentation

Documentation is built with Sphinx. To preview changes locally:

```bash
uv run nox -s livedocs
```

Then visit `http://localhost:8000`.

## Getting Help

- Open an [issue on GitHub](https://github.com/rvforest/nox-mcp/issues)
- Check existing issues for similar questions

Thank you for contributing!
