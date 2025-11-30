# nox-mcp

<!--
[![PyPI - Downloads](https://img.shields.io/pypi/dm/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
[![PyPI - License](https://img.shields.io/pypi/l/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
[![GitHub](https://img.shields.io/badge/GitHub-rvforest%2Fnox-mcp-blue?logo=github)](https://github.com/rvforest/nox-mcp)
[![Read the Docs](https://img.shields.io/readthedocs/nox-mcp)](https://nox-mcp.readthedocs.io)

[![Checks](https://img.shields.io/github/check-runs/rvforest/nox-mcp/main)](https://github.com/rvforest/nox-mcp/actions/workflows/run-checks.yaml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/rvforest/nox-mcp/graph/badge.svg?token=JXB4LR2241)](https://codecov.io/gh/rvforest/nox-mcp)

[![PyPI](https://img.shields.io/pypi/v/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
[![Python Versions](https://img.shields.io/pypi/pyversions/nox-mcp.svg)](https://pypi.org/project/nox-mcp/)
-->

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that enables AI assistants to run [nox](https://nox.thea.codes/) sessions. This allows LLMs to discover and execute your project's test, lint, build, and other automation tasks.

## Features

- **Discover sessions** — List all available nox sessions with descriptions and Python versions
- **Run sessions** — Execute sessions by name, tags, or keyword expressions
- **Filter by Python version** — Override the default Python version for any session
- **Structured output** — Returns JSON responses for easy parsing by AI tools

## Installation

Requires Python 3.10+ and [nox](https://nox.thea.codes/) installed in your PATH.

```bash
pip install nox-mcp
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install nox-mcp
```

## Quick Start

### Configure your MCP client

Add nox-mcp to your MCP client configuration. For example, in Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nox": {
      "command": "nox-mcp"
    }
  }
}
```

Or if using uvx:

```json
{
  "mcpServers": {
    "nox": {
      "command": "uvx",
      "args": ["nox-mcp"]
    }
  }
}
```

### Available Tools

Once configured, your AI assistant can use these tools:

#### `nox_list_sessions`

List all available nox sessions in the current project.

```
Returns: List of session objects with name, python version, and description
```

#### `nox_run_session`

Run one or more nox sessions.

| Parameter | Type | Description |
|-----------|------|-------------|
| `sessions` | list[str] | Session names to run (e.g., `["tests", "lint"]`) |
| `tags` | list[str] | Filter sessions by tags |
| `keywords` | str | Keyword expression (e.g., `"test and not slow"`) |
| `python` | str | Python version override (e.g., `"3.12"`) |
| `timeout` | int | Max seconds to wait (default: 300) |

## Example Workflow

1. Ask your AI assistant: *"What nox sessions are available?"*
2. The assistant calls `nox_list_sessions` and shows you the options
3. Ask: *"Run the tests with Python 3.12"*
4. The assistant calls `nox_run_session(sessions=["tests"], python="3.12")`

## Requirements

- Python 3.10+
- [nox](https://nox.thea.codes/) installed and available in PATH
- An MCP-compatible client (Claude Desktop, etc.)

## Development

```bash
# Clone the repository
git clone https://github.com/rvforest/nox-mcp.git
cd nox-mcp

# Install dependencies
uv sync

# Run tests
uv run nox -s test

# Run all checks
uv run nox -s check
```

## License

MIT License — see [LICENSE](LICENSE) for details.
