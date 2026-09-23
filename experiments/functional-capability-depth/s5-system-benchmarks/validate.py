#!/usr/bin/env python3
"""Validate the experimental direct-S5 benchmark gap layer."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAP_PATH = HERE.parent / "vsm-benchmark-family-map" / "map.json"
COVERAGE_PATH = HERE / "coverage.json"
OBSERVATIONS_PATH = HERE / "canonical_observations.json"

EXPECTED_S5_MAP = {
    "agentgovbench": "unsuitable",
    "rolecde": "proxy",
    "agent-valuebench": "proxy",
    "agentcity": "proxy",
    "cgst-framework": "proxy",
}

EXPECTED_CANONICAL = {
    "headcount": "A",
    "henterprise": "A",
    "ouroboros": "A(P)",
    "thclaws": "P",
    "masters-of-ai-harness": "C(P)",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"missing frontmatter: {path}")
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    fail(f"unterminated frontmatter: {path}")


def main() -> None:
    coverage = json.loads(COVERAGE_PATH.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS_PATH.read_text(encoding="utf-8"))
    benchmark_map = json.loads(MAP_PATH.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S5":
        fail("coverage function must be S5")
    if coverage.get("direct_family_count") != 0:
        fail("S5 direct_family_count must remain 0")
    if coverage.get("canonical_direct_observation_count") != 0:
        fail("canonical_direct_observation_count must remain 0")
    if observations != []:
        fail("canonical_observations.json must remain empty while no direct S5 family exists")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")
    case_ids = [case.get("case_id") for case in cases if isinstance(case, dict)]
    if len(case_ids) != len(set(case_ids)):
        fail("duplicate S5 coverage case_id")

    s5_entries = [entry for entry in benchmark_map.get("entries", []) if entry.get("function") == "S5"]
    direct = [entry for entry in s5_entries if entry.get("fit") == "direct"]
    if direct:
        fail(f"benchmark-family map unexpectedly contains direct S5 entries: {[e.get('benchmark_id') for e in direct]}")

    actual_map = {entry.get("benchmark_id"): entry.get("fit") for entry in s5_entries}
    for benchmark_id, expected_fit in EXPECTED_S5_MAP.items():
        actual_fit = actual_map.get(benchmark_id)
        if actual_fit != expected_fit:
            fail(f"S5 map mismatch for {benchmark_id}: expected {expected_fit}, got {actual_fit}")

    anchors = coverage.get("representative_canonical_s5_systems")
    if not isinstance(anchors, list):
        fail("representative_canonical_s5_systems must be a list")
    declared = {row.get("harness_id"): row.get("expected_state") for row in anchors if isinstance(row, dict)}
    if declared != EXPECTED_CANONICAL:
        fail(f"canonical anchor declaration mismatch: {declared!r}")

    for harness_id, expected_state in EXPECTED_CANONICAL.items():
        path = ROOT / "assessments" / f"{harness_id}.md"
        if not path.exists():
            fail(f"missing canonical assessment: {path}")
        fm = frontmatter(path)
        if fm.get("status") != "included":
            fail(f"{harness_id}: expected status included, got {fm.get('status')!r}")
        actual_state = fm.get("autonomy_s5")
        if actual_state != expected_state:
            fail(f"{harness_id}: expected autonomy_s5={expected_state}, got {actual_state!r}")

    print(
        f"ok: {len(cases)} S5 coverage cases, "
        f"{len(EXPECTED_CANONICAL)} canonical anchors, "
        "0 direct families, 0 canonical observations"
    )


if __name__ == "__main__":
    main()
