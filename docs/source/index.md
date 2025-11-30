# nox-mcp

[![GitHub](https://img.shields.io/badge/GitHub-rvforest%2Fnox--mcp-blue?logo=github)](https://github.com/rvforest/nox-mcp)
[![PyPI](https://img.shields.io/pypi/v/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
[![Python Versions](https://img.shields.io/pypi/pyversions/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that enables AI assistants to run [nox](https://nox.thea.codes/) sessions.

## What is nox-mcp?

nox-mcp bridges the gap between AI assistants and your project's automation tasks. It exposes your nox sessions—tests, linting, builds, and more—as tools that AI assistants can discover and execute.

**Key features:**

- **Discover sessions** — List all available nox sessions with descriptions
- **Run sessions** — Execute sessions by name, tags, or keyword expressions
- **Filter by Python version** — Override the default Python version for any session
- **Structured output** — Returns JSON responses for easy parsing

## Quick Example

Once configured, you can ask your AI assistant:

> "What nox sessions are available in this project?"

The assistant calls `nox_list_sessions` and returns something like:

```json
[
  {"session": "tests", "python": "3.11", "description": "Run the test suite"},
  {"session": "lint", "python": "3.11", "description": "Run linters"},
  {"session": "docs", "python": "3.11", "description": "Build documentation"}
]
```

Then ask:

> "Run the tests with Python 3.12"

And the assistant executes `nox_run_session(sessions=["tests"], python="3.12")`.

## Getting Started

```{toctree}
:maxdepth: 2

getting_started/installation
getting_started/quickstart
```

## API Reference

```{toctree}
:maxdepth: 2

apidocs/index
```

## Development

```{toctree}
:maxdepth: 2

development/contributing
```
