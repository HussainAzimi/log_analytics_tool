import pytest
from src.queries import run_query

def test_run_query_dispatch(sample_events):
    """Verifies the Strategy Pattern: dispatching by string name."""
    res = run_query("error_count", sample_events)
    assert res == 2

def test_suspicious_activity_short_circuit(sample_events):
    """Verifies the use of the 'any' built-in."""
    # Should return True because of the 'Suspicious' message in sample data
    assert run_query("contains_suspicious_activity", sample_events) is True

def test_unknown_query_raises_keyerror():
    """Ensures API safety for invalid query names."""
    with pytest.raises(KeyError):
        run_query("non_existent_query", [])