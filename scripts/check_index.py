#!/usr/bin/env python3
"""Validate assessment sources and prove that committed CSV indexes are reproducible."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import tempfile
from pathlib import Path


def load_upserter(path: Path):
    spec = importlib.util.spec_from_file_location("upsert_harness", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load upserter: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_renderer(path: Path):
    spec = importlib.util.spec_from_file_location("render_readme", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load renderer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    default_upserter = repo.parent / "vsm-skills" / "skills" / "assess-vsm-harness" / "scripts" / "upsert_harness.py"
    parser = argparse.ArgumentParser()
    parser.add_argument("--upserter", type=Path, default=default_upserter)
    args = parser.parse_args()
    upserter = load_upserter(args.upserter.resolve())
    artifacts = sorted((repo / "data" / "assessments").glob("**/*.json"))
    if not artifacts:
        raise SystemExit("no assessment artifacts found")
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
    catalog_by_id = {row["harness_id"]: row for row in catalog}
    for row in included:
        upserter.validate_vsm_tldr(
            row["vsm_tldr"].replace("\\n", "\n"),
            f"catalog[{row['harness_id']}].vsm_tldr",
        )
    for artifact in artifacts:
        data = json.loads(artifact.read_text(encoding="utf-8"))
        harness = data["harness"]
        catalog_row = catalog_by_id.get(harness["harness_id"])
        if catalog_row is None:
            raise SystemExit(f"assessment missing from catalog: {harness['harness_id']}")
        if harness["catalog_position"] != int(catalog_row["catalog_position"]):
            raise SystemExit(f"assessment catalog_position is stale: {harness['harness_id']}")
    with tempfile.TemporaryDirectory() as temporary:
        output = Path(temporary)
        for artifact in artifacts:
            upserter.upsert(upserter.load_artifact(artifact), output)
        for name in ("harnesses.csv", "harness-metrics.csv"):
            if (repo / "data" / name).read_bytes() != (output / name).read_bytes():
                raise SystemExit(f"data/{name} is stale; regenerate with assess-vsm-harness")
    tldr = (repo / "TLDR.md").read_text(encoding="utf-8")
    renderer = load_renderer(repo / "scripts" / "render_readme.py")
    if renderer.render_tldr_document(repo) != tldr:
        raise SystemExit("TLDR.md is stale; run scripts/render_readme.py")
    entries = sorted((repo / "entries").glob("*.md"))
    for entry in entries:
        if f"entries/{entry.name}" not in tldr:
            raise SystemExit(f"entry missing from TLDR table: {entry.name}")
    print(
        f"Validated {len(included)} included and {len(excluded)} excluded catalog row(s), "
        f"{len(artifacts)} assessment artifact(s), and {len(entries)} detailed entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
