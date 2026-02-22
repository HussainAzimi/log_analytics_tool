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
        if not line.strip():
            continue
        try:
            # Split the 4 main fields by pipe and strip whitespace
            parts = [p.strip() for p in line.split("|")]           
            ts_str, level, service = parts[0], parts[1], parts[2]

            # Handle message and meta based on the number of pipes
            meta = {}
            if len(parts) >= 5:
                message = parts[3]
                kv_section = parts[4]
                for pair in kv_section.split(","):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        meta[k.strip()] = v.strip()
            else:
                message = parts[3]
       
            yield LogEvent(
                timestamp=datetime.fromisoformat(ts_str),
                level=level,
                service=service,
                message=message,
                meta=meta
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
