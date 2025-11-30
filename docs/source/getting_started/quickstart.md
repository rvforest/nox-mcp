# Quick Start

This guide shows you how to configure nox-mcp with your MCP client.

## Configure Your MCP Client

### Claude Desktop

Add nox-mcp to your Claude Desktop configuration file.

**Configuration file locations:**
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "nox": {
      "command": "nox-mcp"
    }
  }
}
```

If you prefer to run without installing globally, use `uvx`:

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

### VS Code with GitHub Copilot

Add to your VS Code settings or MCP configuration:

```json
{
  "mcp": {
    "servers": {
      "nox": {
        "command": "nox-mcp"
      }
    }
  }
}
```

## Available Tools

Once configured, your AI assistant has access to these tools:

### `nox_list_sessions`

Lists all available nox sessions in the current project.

**Returns:** A list of session objects, each containing:
- `session`: Session name
- `python`: Python version
- `description`: Session description

### `nox_run_session`

Runs one or more nox sessions.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `sessions` | `list[str]` | Session names to run (e.g., `["tests", "lint"]`) |
| `tags` | `list[str]` | Filter sessions by tags |
| `keywords` | `str` | Keyword expression (e.g., `"test and not slow"`) |
| `python` | `str` | Python version override (e.g., `"3.12"`) |
| `timeout` | `int` | Max seconds to wait (default: 300) |

**Returns:** A dictionary with `exit_code`, `stdout`, and `stderr`.

## Example Workflow

1. **Discover available sessions:**
   > "What nox sessions can I run in this project?"

2. **Run tests:**
   > "Run the test suite"

3. **Run with specific Python version:**
   > "Run tests with Python 3.12"

4. **Run multiple sessions:**
   > "Run both lint and tests"

5. **Filter by keywords:**
   > "Run all sessions that match 'test' but not 'slow'"
