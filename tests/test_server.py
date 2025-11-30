import subprocess
from unittest.mock import MagicMock, patch

import pytest
from fastmcp.exceptions import ToolError
from nox_mcp.server import nox_list_sessions, nox_run_session

# Access the underlying functions from the FunctionTool wrappers
_nox_list_sessions = nox_list_sessions.fn
_nox_run_session = nox_run_session.fn


@patch("nox_mcp.server.shutil.which")
@patch("nox_mcp.server.subprocess.run")
def test_nox_list_sessions(mock_run, mock_which):
    mock_which.return_value = "/usr/bin/nox"
    mock_run.return_value = MagicMock(
        stdout='[{"session": "test"}]', returncode=0
    )
    result = _nox_list_sessions()
    assert isinstance(result, list)
    assert result == [{"session": "test"}]
    mock_run.assert_called_once_with(
        ["/usr/bin/nox", "--list", "--json"],
        capture_output=True,
        text=True,
        check=True,
        timeout=30,
    )


@patch("nox_mcp.server.shutil.which")
@patch("nox_mcp.server.subprocess.run")
def test_nox_run_session(mock_run, mock_which):
    mock_which.return_value = "/usr/bin/nox"
    mock_run.return_value = MagicMock(
        stdout="Success", stderr="", returncode=0
    )

    result = _nox_run_session(sessions=["test"], python="3.10")
    # structured output
    assert isinstance(result, dict)
    assert result["stdout"] == "Success"
    assert result["exit_code"] == 0
    
    expected_cmd = ["/usr/bin/nox", "-s", "test", "-p", "3.10"]
    mock_run.assert_called_once_with(
        expected_cmd,
        capture_output=True,
        text=True,
        check=False,
        timeout=300,
    )

@patch("nox_mcp.server.shutil.which")
def test_nox_not_found(mock_which):
    mock_which.return_value = None
    with pytest.raises(ToolError):
        _nox_list_sessions()
    with pytest.raises(ToolError):
        _nox_run_session()


@patch("nox_mcp.server.shutil.which")
def test_invalid_session_name(mock_which):
    mock_which.return_value = "/usr/bin/nox"
    with pytest.raises(ToolError):
        _nox_run_session(sessions=["bad;name"])  # invalid characters


@patch("nox_mcp.server.shutil.which")
@patch("nox_mcp.server.subprocess.run")
def test_nox_run_timeout(mock_run, mock_which):
    mock_which.return_value = "/usr/bin/nox"
    mock_run.side_effect = subprocess.TimeoutExpired(cmd=["nox"], timeout=1)
    with pytest.raises(ToolError):
        _nox_run_session(sessions=["test"], timeout=1)
