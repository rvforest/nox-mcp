import json
import logging
import re
import shutil
import subprocess
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from fastmcp.server.middleware.error_handling import ErrorHandlingMiddleware

logger = logging.getLogger(__name__)

# allow simple name tokens for sessions and tags (alphanumeric, -, _)
VALID_NAME = re.compile(r"^[A-Za-z0-9_-]+$")

mcp = FastMCP(
    "nox",
    instructions="""
    A Model Context Protocol server for running nox sessions.
    Useful for projects that use nox for test automation and development tasks.

    Nox is a Python automation tool for running tests, linting, and other
    development tasks in isolated environments. This server allows you to
    discover and execute nox sessions in any project that has a noxfile.py.

    Typical workflow:
    1. Use nox_list_sessions to discover available sessions
    2. Use nox_run_session to execute one or more sessions

    The server requires 'nox' to be installed and available in PATH.
    """,
    mask_error_details=True,
)

# Add a simple error-handling middleware (good default for development)
mcp.add_middleware(ErrorHandlingMiddleware(include_traceback=False))


@mcp.tool()
def nox_list_sessions(timeout: int = 30) -> List[Dict[str, Any]]:
    """
    List all available nox sessions.

    Use this tool to discover which nox sessions are available in the current
    project before running them. Returns structured session data including
    session names, Python versions, and descriptions.

    Returns:
        A list of session objects, each containing session metadata like
        'session' (name), 'python' (version), and 'description'.

    Example response:
        [{"session": "tests", "python": "3.11", "description": "Run tests"}]
    """
    nox_path = shutil.which("nox")
    if not nox_path:
        raise ToolError("'nox' executable not found in PATH.")

    try:
        result = subprocess.run(
            [nox_path, "--list", "--json"],
            capture_output=True,
            text=True,
            check=True,
            timeout=timeout,
        )
        # parse JSON into Python objects for structured responses
        return json.loads(result.stdout or "[]")
    except subprocess.CalledProcessError as e:
        logger.error("nox --list failed: %s", e.stderr)
        raise ToolError("Error running 'nox --list'") from e
    except subprocess.TimeoutExpired as e:
        logger.error("nox --list timed out: %s", str(e))
        raise ToolError("nox --list timed out") from e
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON returned by nox --list: %s", str(e))
        raise ToolError("Invalid JSON returned by nox --list") from e


@mcp.tool()
def nox_run_session(
    sessions: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    keywords: Optional[str] = None,
    python: Optional[str] = None,
    timeout: int = 300,
) -> Dict[str, Any]:
    """
    Run nox sessions.

    Use this tool to execute one or more nox sessions in the current project.
    You can filter sessions by name, tags, or keywords. Use nox_list_sessions
    first to discover available sessions.

    Args:
        sessions: List of session names to run (e.g., ["tests", "lint"]).
            Session names must contain only alphanumeric characters, hyphens,
            or underscores.
        tags: List of tags to filter sessions (e.g., ["ci", "quick"]).
            Only sessions matching these tags will run.
        keywords: A keyword expression to filter sessions (e.g., "test and not slow").
            Uses Python expression syntax for matching session names.
        python: Python version to run sessions with (e.g., "3.11", "3.12").
            Overrides the session's default Python version.
        timeout: Maximum seconds to wait for nox to complete. Defaults to 300.

    Returns:
        A dictionary with 'exit_code' (0 = success), 'stdout', and 'stderr'
        from the nox command execution.

    Example:
        Run tests with Python 3.11:
        nox_run_session(sessions=["tests"], python="3.11")
    """
    nox_path = shutil.which("nox")
    if not nox_path:
        raise ToolError("'nox' executable not found in PATH.")

    # Validate inputs to prevent unexpected content passed to subprocess
    for s in sessions or []:
        if not VALID_NAME.match(s):
            raise ToolError(f"Invalid session name: {s}")
    for t in tags or []:
        if not VALID_NAME.match(t):
            raise ToolError(f"Invalid tag: {t}")

    command = [nox_path]
    if sessions:
        command.append("-s")
        command.extend(sessions)

    if tags:
        command.append("-t")
        command.extend(tags)

    if keywords:
        command.extend(["-k", keywords])

    if python:
        command.extend(["-p", python])

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,  # Don't raise on non-zero, return full output to the caller
            timeout=timeout,
        )

        return {
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    except subprocess.TimeoutExpired as e:
        logger.error("nox run timed out: %s", str(e))
        raise ToolError("nox run timed out") from e
    except Exception as e:
        logger.exception("Unexpected error running nox: %s", str(e))
        raise ToolError("Unexpected error running nox") from e


if __name__ == "__main__":
    mcp.run()
