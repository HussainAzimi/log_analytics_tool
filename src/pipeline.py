from __future__ import annotations
from datetime import datetime
from typing import Iterable, Iterator
from .log_model import LogEvent, LogParseError


def read_lines(path: str) -> Iterator[str]:
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")

def parse_events(lines: Iterable[str]) -> Iterator[LogEvent]:
    for line in lines:
        try:
            ts, level, service, msg, *rest = line.split("|")
            meta = {}
            if rest:
              for pair in rest[0].split(","):
                if not pair:
                    continue
            k, v = pair.split("=", 1)
            meta[k] = v
            yield LogEvent(
                timestamp=datetime.fromisoformat(ts),
                level=level,
                service=service,
                message=msg,
                meta=meta,
            )
        except Exception as e:
            raise LogParseError(f"Malformed line: {line!r}") from e
        
def filter_level(events: Iterable[LogEvent], level: str) -> Iterator[LogEvent]:
        for e in events:
            if e.level == level:
                yield e

def filter_service(events: Iterable[LogEvent], service: str) -> Iterator[LogEvent]:
        for e in events:
            if e.service == service:
                yield e

def map_messages(events: Iterable[LogEvent]) -> Iterator[str]:
    for e in events:
        yield e.message
        
def count(items: Iterable[object]) -> int:
    return sum(1 for _ in items)
