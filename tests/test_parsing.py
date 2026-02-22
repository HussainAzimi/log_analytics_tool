import pytest
from datetime import datetime
from src.log_model import LogEvent, LogParseError
from src.pipeline import parse_events

def test_log_event_creation():
    """Tests the OO Model initialization and formatting."""
    ts = datetime.fromisoformat("2026-02-03T13:25:10")
    event = LogEvent(ts, "INFO", "auth", "Login", {"user_id": "42"})
    assert str(event) == "[INFO] auth: Login"

def test_parse_valid_line():
    """Tests that a standard log string parses into a correct object."""
    line = ["2026-02-03T13:25:10 | INFO | auth | Login | user_id=42"]
    events = list(parse_events(line))
    assert len(events) == 1
    assert events[0].service == "auth"
    assert events[0].meta["user_id"] == "42"

def test_parse_malformed_line():
    """Tests that LogParseError is raised with the original line included."""
    bad_line = "This is not a log line"
    with pytest.raises(LogParseError) as excinfo:
        list(parse_events([bad_line]))
    assert "Malformed line" in str(excinfo.value)
    assert bad_line in str(excinfo.value)