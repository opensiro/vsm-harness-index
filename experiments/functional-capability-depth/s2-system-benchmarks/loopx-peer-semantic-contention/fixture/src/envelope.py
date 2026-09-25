from __future__ import annotations


def make_response(status: int) -> dict[str, int]:
    return {"status": status}
