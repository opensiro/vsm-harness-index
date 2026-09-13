#!/usr/bin/env python3
"""Validate the standalone catalog and its rendered TLDR projection."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path

from validate_tldr import validate_rows


def load_renderer(path: Path):
    spec = importlib.util.spec_from_file_location("render_tldr", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load renderer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    with (repo / "data" / "catalog.psv").open(encoding="utf-8", newline="") as handle:
        catalog = list(csv.DictReader(handle, delimiter="|"))
    positions = [int(row["catalog_position"]) for row in catalog]
    if positions != list(range(1, len(catalog) + 1)):
        raise SystemExit("catalog positions must be ordered, unique, and contiguous from 1")
    if len({row["harness_id"] for row in catalog}) != len(catalog):
        raise SystemExit("catalog harness_id values must be unique")
    if len({row["repository"] for row in catalog}) != len(catalog):
        raise SystemExit("catalog repositories must be unique")
    sort_keys = [(row["repository_created_at"], row["repository"]) for row in catalog]
    if sort_keys != sorted(sort_keys):
        raise SystemExit("catalog must be sorted by repository_created_at and repository")
    included = [row for row in catalog if row.get("tldr_status") == "included"]
    excluded = [row for row in catalog if row.get("tldr_status") == "excluded-no-agentic-vsm"]
    if len(included) + len(excluded) != len(catalog):
        raise SystemExit("every catalog row must have a recognized tldr_status")
    if any(row["vsm_tldr"] for row in excluded):
        raise SystemExit("excluded catalog rows must not carry fingerprints")
    tldrs = [row["vsm_tldr"] for row in included]
    if len(set(tldrs)) != len(tldrs):
        raise SystemExit("included catalog VSM TL;DR values must be unique")
    if any(len(row.get("review_ref", "")) != 40 for row in catalog):
        raise SystemExit("every catalog row must pin a 40-character review_ref")
    if any(not row.get("reviewed_at") for row in catalog):
        raise SystemExit("every catalog row must record reviewed_at")
    validate_rows(catalog)
    tldr = (repo / "TLDR.md").read_text(encoding="utf-8")
    renderer = load_renderer(repo / "scripts" / "render_tldr.py")
    if renderer.render_tldr_document(repo) != tldr:
        raise SystemExit("TLDR.md is stale; run scripts/render_tldr.py")
    print(f"Validated {len(included)} included and {len(excluded)} excluded catalog row(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
