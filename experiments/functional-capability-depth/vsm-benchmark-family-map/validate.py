#!/usr/bin/env python3
"""Validate the experimental VSM function -> benchmark-family map."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
MAP_PATH = ROOT / "map.json"

FUNCTIONS = {"S1", "S2", "S3", "S3*", "S4", "S5"}
FITS = {"direct", "proxy", "unsuitable", "unknown"}
SYSTEM_LINKAGE = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
    "observation-specific",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> None:
    data = json.loads(MAP_PATH.read_text(encoding="utf-8"))

    if data.get("schema_version") != 1:
        fail("schema_version must be 1")

    if set(data.get("fit_vocabulary", [])) != FITS:
        fail("fit_vocabulary does not match validator vocabulary")

    declared_compat = set(data.get("system_compatibility_vocabulary", []))
    expected_declared = SYSTEM_LINKAGE - {"observation-specific"}
    if declared_compat != expected_declared:
        fail("system_compatibility_vocabulary does not match validator vocabulary")

    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        fail("entries must be a non-empty list")

    seen_pairs: set[tuple[str, str]] = set()
    seen_functions: set[str] = set()

    required = {
        "function",
        "benchmark_id",
        "benchmark_name",
        "fit",
        "primary_source",
        "evaluated_object",
        "evaluation_mode",
        "system_linkage",
        "non_claim",
    }

    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            fail(f"entry {index} must be an object")

        missing = required - entry.keys()
        if missing:
            fail(f"entry {index} missing fields: {sorted(missing)}")

        function = entry["function"]
        benchmark_id = entry["benchmark_id"]
        fit = entry["fit"]
        linkage = entry["system_linkage"]

        if function not in FUNCTIONS:
            fail(f"entry {index} has invalid function: {function!r}")
        if fit not in FITS:
            fail(f"entry {index} has invalid fit: {fit!r}")
        if linkage not in SYSTEM_LINKAGE:
            fail(f"entry {index} has invalid system_linkage: {linkage!r}")
        if not isinstance(benchmark_id, str) or not benchmark_id.strip():
            fail(f"entry {index} benchmark_id must be non-empty")
        if not valid_https_url(entry["primary_source"]):
            fail(f"entry {index} primary_source must be an https URL")

        for field in ("benchmark_name", "evaluated_object", "evaluation_mode", "non_claim"):
            if not isinstance(entry[field], str) or not entry[field].strip():
                fail(f"entry {index} {field} must be non-empty")

        pair = (function, benchmark_id)
        if pair in seen_pairs:
            fail(f"duplicate function/benchmark pair: {pair}")
        seen_pairs.add(pair)
        seen_functions.add(function)

        if fit == "unsuitable" and len(entry["non_claim"].strip()) < 20:
            fail(f"entry {index} unsuitable mapping needs an explicit non-claim")

    missing_functions = FUNCTIONS - seen_functions
    if missing_functions:
        fail(f"missing VSM functions: {sorted(missing_functions)}")

    direct_by_function = {
        function: sum(
            1
            for entry in entries
            if entry["function"] == function and entry["fit"] == "direct"
        )
        for function in sorted(FUNCTIONS)
    }

    print(f"ok: {len(entries)} reviewed benchmark mappings")
    print("direct coverage:")
    for function, count in direct_by_function.items():
        print(f"  {function}: {count}")


if __name__ == "__main__":
    main()
