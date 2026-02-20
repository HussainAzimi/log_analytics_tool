from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Iterable, Iterator, Callable


ALLOWED_LEVELS = {"DEBUG", "INFO", "WARN", "ERROR"}

class LogParseError(ValueError):
    pass

@dataclass(frozen=True)
class LogEvent:
    timestamp: datetime
    level: str
    service: str
    message: str
    meta: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.level not in ALLOWED_LEVELS:
            raise ValueError(f"Invalid level: {self.level}")
        
    def __str__(self) -> str:
        return f"[{self.level}] {self.service}: {self.message}"
    
    def __repr__(self) -> str:
        return f"[{self.level}] {self.service}: {self.message}"
    
  