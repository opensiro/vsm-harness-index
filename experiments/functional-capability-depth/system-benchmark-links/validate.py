#!/usr/bin/env python3
"""Validate the non-normative system↔benchmark evidence registry."""

from __future__ import annotations

import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REGISTRY = HERE / "links.jsonl"

EVIDENCE_MODES = {
    "external-run",
    "externally-checked-submission",
    "system-maintained",
    "published-secondary",
}
PUBLISHER_RELATIONS = {
    "independent-third-party",
    "benchmark-project-related",
    "system-maintainer",
    "unclear",
}
BOUNDARY_MATCHES = {"exact", "partial", "unclear"}
REVISION_MATCHES = {"exact", "version-known", "date-bounded", "unknown"}

REQUIRED_TOP_LEVEL = {
    "record_id",
    "harness_id",
    "canonical_repository",
    "assessment_ref",
    "benchmark",
    "observation",
    "provenance",
    "identity",
    "comparability_group",
    "notes",
}


def fail(message: str) -> None:
    raise SystemExit(message)


def frontmatter(path: pathlib.Path) -> dict[str, str]:
    if not path.exists():
        fail(f"missing canonical assessment: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def main() -> None:
    records = []
    for lineno, raw in enumerate(REGISTRY.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"links.jsonl:{lineno}: invalid JSON: {exc}")
        missing = REQUIRED_TOP_LEVEL - record.keys()
        if missing:
            fail(f"links.jsonl:{lineno}: missing fields: {sorted(missing)}")
        records.append((lineno, record))

    if not records:
        fail("links.jsonl contains no records")

    ids: set[str] = set()
    assessment_cache: dict[str, dict[str, str]] = {}

    for lineno, record in records:
        record_id = record["record_id"]
        if record_id in ids:
            fail(f"links.jsonl:{lineno}: duplicate record_id: {record_id}")
        ids.add(record_id)

        harness_id = record["harness_id"]
        if harness_id not in assessment_cache:
            assessment_cache[harness_id] = frontmatter(ROOT / "assessments" / f"{harness_id}.md")
        fm = assessment_cache[harness_id]

        if fm.get("harness_id") != harness_id:
            fail(f"links.jsonl:{lineno}: canonical harness_id mismatch for {harness_id}")
        if fm.get("repository") != record["canonical_repository"]:
            fail(f"links.jsonl:{lineno}: canonical repository drift for {harness_id}")
        if fm.get("review_ref") != record["assessment_ref"]:
            fail(f"links.jsonl:{lineno}: assessment_ref drift for {harness_id}")

        provenance = record["provenance"]
        if provenance.get("evidence_mode") not in EVIDENCE_MODES:
            fail(f"links.jsonl:{lineno}: invalid evidence_mode")
        if provenance.get("publisher_relation") not in PUBLISHER_RELATIONS:
            fail(f"links.jsonl:{lineno}: invalid publisher_relation")

        identity = record["identity"]
        if identity.get("boundary_match") not in BOUNDARY_MATCHES:
            fail(f"links.jsonl:{lineno}: invalid boundary_match")
        if identity.get("revision_match") not in REVISION_MATCHES:
            fail(f"links.jsonl:{lineno}: invalid revision_match")

        benchmark = record["benchmark"]
        if not benchmark.get("id") or not benchmark.get("name") or not benchmark.get("source_url"):
            fail(f"links.jsonl:{lineno}: incomplete benchmark identity")
        if not str(benchmark["source_url"]).startswith("https://"):
            fail(f"links.jsonl:{lineno}: benchmark source_url must use https")

        observation = record["observation"]
        if not observation.get("harness_label") or not observation.get("metric"):
            fail(f"links.jsonl:{lineno}: incomplete observation identity")
        if observation.get("value") is None:
            fail(f"links.jsonl:{lineno}: initial registry requires an explicit metric value")

    counts: dict[str, int] = {}
    for _, record in records:
        counts[record["harness_id"]] = counts.get(record["harness_id"], 0) + 1

    print(f"ok: {len(records)} observations across {len(counts)} canonical systems")
    print("systems:", ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))


if __name__ == "__main__":
    main()
