
from src.pipeline import filter_level, count

def test_filter_is_lazy(sample_events):
    """PROVE LAZINESS: result should be an iterator, not a list."""
    result = filter_level(sample_events, "ERROR")
    assert hasattr(result, "__next__"), "Filter must return an iterator for laziness"
    assert not isinstance(result, list), "Filter should not materialize a list"

def test_streaming_count():
    """Tests the sum(1 for...) logic."""
    # Create a generator that can only be read once
    gen = (i for i in range(5))
    assert count(gen) == 5

def test_filter_logic(sample_events):
    """Verifies that filter correctly narrows the stream."""
    result = list(filter_level(sample_events, "ERROR"))
    assert len(result) == 2
    assert all(e.level == "ERROR" for e in result)