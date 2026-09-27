#!/usr/bin/env python3
"""Validate the neutral public-evidence <-> system observation registry."""

from __future__ import annotations

from collections import Counter

from render_registry import RegistryError, collect_rows


def main() -> None:
    try:
        rows = collect_rows()
    except RegistryError as exc:
        raise SystemExit(f"error: {exc}") from exc

    if not rows:
        raise SystemExit("error: neutral system-observation registry is empty")

    systems = Counter(row.system_name for row in rows)
    source_classes = Counter(row.evidence_source_class for row in rows)
    compatibility = Counter(row.system_compatibility for row in rows)
    canonical_rows = sum(bool(row.canonical_harness_id) for row in rows)

    print("ok: neutral public-evidence system registry validated")
    print(f"raw observations: {len(rows)}")
    print(f"systems: {len(systems)}")
    print(f"canonical-linked observations: {canonical_rows}")
    print(
        "provenance classes: "
        + ", ".join(f"{key}={value}" for key, value in sorted(source_classes.items()))
    )
    print(
        "system compatibility: "
        + ", ".join(f"{key}={value}" for key, value in sorted(compatibility.items()))
    )
    print("VSM-function attribution: not required by raw registry validation")


if __name__ == "__main__":
    main()
