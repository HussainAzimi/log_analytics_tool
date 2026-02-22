# tests/conftest.py
import pytest
from datetime import datetime
from src.log_model import LogEvent

@pytest.fixture
def sample_events():
    return [
        LogEvent(datetime.now(), "INFO", "auth", "User login"),
        LogEvent(datetime.now(), "ERROR", "billing", "Failed"),
        LogEvent(datetime.now(), "ERROR", "auth", "Bad password"),
        LogEvent(datetime.now(), "WARN", "auth", "Suspicious activity"),
    ]