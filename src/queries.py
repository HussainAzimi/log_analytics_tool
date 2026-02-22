from __future__ import annotations
from typing import Iterable, Iterator, Callable, Any
from collections import Counter
from .log_model import LogEvent
from .pipeline import count, filter_level

def top_services_by_errors(events: Iterable[LogEvent], n: int = 3):
    errs = filter_level(events, "ERROR")
    c = Counter(e.service for e in errs)
    return c.most_common(n)

def contains_suspicious_activity(events: Iterable[LogEvent]) -> bool:
    return any("Suspicious" in e.message for e in events)

def error_count(events: Iterable[LogEvent]) -> int:
    return count(filter_level(events, "ERROR"))

# Eager Implementation (Comprehension)
# Appropriate for small datasets where we need to transform data and keep it in memory 
# for multiple lookups or immediate display.
def get_service_summary(events: Iterable[LogEvent]) -> dict[str, str]:
    return {e.service: e.level for e in events}


# Lazy Implementation (Generator Expression)
# Appropriate for large-scale streaming where we only need to iterate once. 
# It saves memory by not storing the entire list of results.
def stream_error_messages(events: Iterable[LogEvent]) -> Iterator[str]:
    return {e.message for e in events if e.level == "ERROR"}

QUERIES: dict[str, Callable[..., Any]] = {
    "top_services_by_errors": top_services_by_errors,
    "contains_suspicious_activity": contains_suspicious_activity,
    "error_count": error_count,
    "service_summary": get_service_summary,
    "stream_errors": stream_error_messages,
}

def run_query(name: str, events: Iterable[LogEvent], **kwargs) -> Any:
    try:
        return QUERIES[name](events, **kwargs)
    except KeyError as e:
        raise KeyError(f"Unknown query: {name}") from e
    





