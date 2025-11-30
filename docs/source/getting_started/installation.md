# Installation

## Requirements

- Python 3.10 or higher
- [nox](https://nox.thea.codes/) installed and available in your PATH
- An MCP-compatible client (e.g., Claude Desktop, VS Code with GitHub Copilot)

## Install from PyPI

```bash
pip install nox-mcp
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install nox-mcp
```

## Verify Installation

After installation, verify that the `nox-mcp` command is available:

```bash
nox-mcp --help
```

You should also ensure nox is installed:

```bash
nox --version
```

## Next Steps

Once installed, see the {doc}`quickstart` guide to configure your MCP client.
