#!/usr/bin/env python3
"""Independent validation for the treatment coordinator's typed result."""

from __future__ import annotations

import json
import sys


ALLOWED = {"parallel", "a_then_b", "b_then_a"}


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"invalid coordinator result JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(payload, dict):
        print("coordinator result must be one JSON object", file=sys.stderr)
        return 2
    classification = payload.get("classification")
    if classification not in ALLOWED:
        print(
            "classification must be exactly one of: " + ", ".join(sorted(ALLOWED)),
            file=sys.stderr,
        )
        return 1
    print(classification)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
