from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DispatchRecord:
    target: str
    status: int


def dispatch(target: str, status: int) -> DispatchRecord:
    """Build the normalized record returned by the fixture dispatcher."""
    return DispatchRecord(target=target, status=status)
