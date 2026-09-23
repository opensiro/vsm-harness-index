#!/usr/bin/env python3
"""Validate the experimental direct-S5 benchmark gap and primary-search coverage."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAP_PATH = HERE.parent / "vsm-benchmark-family-map" / "map.json"
BASELINES_PATH = HERE.parent / "primary-baselines.json"
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

EXPECTED_COVERAGE_CLASSES = {
    "proxy",
    "unsuitable",
    "protocol-not-benchmark",
    "governance-process-not-harness-benchmark",
    "candidate-native-mechanism-not-benchmark",
    "candidate-native-no-direct-results",
}

REQUIRED_FOLLOWUP_CASES = {
    "constitutional-agent-governance-amendment-mechanism": (
        "candidate-native-mechanism-not-benchmark",
        "368717cb50b70826412f85022d23b3fd8a0dec77",
    ),
    "agent-parliament-ratified-amendment-process": (
        "governance-process-not-harness-benchmark",
        None,
    ),
    "mac-constitution-optimization-proxy": (
        "proxy",
        "76aea7ce2cd95e46cfcf015a70895fdc267a0f4f",
    ),
    "cmag-fixed-constitution-governance-proxy": ("proxy", None),
    "gps-bench-policy-analysis-not-organizational-s5": ("unsuitable", None),
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


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
    baselines = json.loads(BASELINES_PATH.read_text(encoding="utf-8"))

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

    s5_baseline = (baselines.get("functions") or {}).get("S5") or {}
    if s5_baseline.get("status") != "gap":
        fail("primary-baselines.json must preserve S5 status=gap")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != EXPECTED_COVERAGE_CLASSES:
        fail(f"S5 coverage_classes vocabulary drift: {sorted(declared_classes)}")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")

    seen_ids: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        if not isinstance(case, dict):
            fail("every S5 coverage case must be an object")
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("every S5 coverage case requires case_id")
        if case_id in seen_ids:
            fail(f"duplicate S5 coverage case_id: {case_id}")
        seen_ids.add(case_id)
        by_id[case_id] = case

        classification = case.get("classification")
        if classification not in EXPECTED_COVERAGE_CLASSES - {"candidate-native-no-direct-results"}:
            fail(f"{case_id}: invalid S5 coverage classification {classification!r}")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{case_id}: primary_sources must be non-empty HTTPS URLs")
        finding = case.get("finding")
        if not isinstance(finding, str) or len(finding.strip()) < 40:
            fail(f"{case_id}: explicit finding required")

    for case_id, (expected_class, expected_ref) in REQUIRED_FOLLOWUP_CASES.items():
        case = by_id.get(case_id)
        if case is None:
            fail(f"missing required S5 primary-search case: {case_id}")
        if case.get("classification") != expected_class:
            fail(f"{case_id}: expected classification {expected_class}")
        if expected_ref is not None and case.get("review_ref") != expected_ref:
            fail(f"{case_id}: review_ref drift")

    constitutional = by_id["constitutional-agent-governance-amendment-mechanism"]
    if "constitutional-agent-governance" not in constitutional["primary_sources"][0]:
        fail("constitutional-agent-governance case must retain first-party repository provenance")

    parliament = by_id["agent-parliament-ratified-amendment-process"]
    if parliament.get("classification") != "governance-process-not-harness-benchmark":
        fail("Agent Parliament must remain governance-process evidence, not a harness benchmark")
    if not any("parliament.hermanity.dev/laws/constitution" in source for source in parliament["primary_sources"]):
        fail("Agent Parliament case must retain the public constitutional record")

    mac = by_id["mac-constitution-optimization-proxy"]
    if not any("MAC-Multi-Agent-Constitution-Learning" in source for source in mac["primary_sources"]):
        fail("MAC case must retain first-party repository provenance")
    if not any("2603.15968" in source for source in mac["primary_sources"]):
        fail("MAC case must retain paper provenance")

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
    for row in anchors:
        if row.get("benchmark_status") != "candidate-native-no-direct-results":
            fail(f"{row.get('harness_id')}: canonical S5 anchor must remain candidate-native-no-direct-results")

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

    requirements = coverage.get("missing_direct_benchmark_requirements")
    if not isinstance(requirements, list) or len(requirements) < 6:
        fail("missing_direct_benchmark_requirements must preserve the full direct + baseline gate")
    if not any("matched" in str(item).lower() and "canonical" in str(item).lower() for item in requirements):
        fail("missing direct requirements must include matched canonical-harness comparison")

    print(
        f"ok: {len(cases)} S5 coverage cases, "
        f"{len(EXPECTED_CANONICAL)} canonical native-path gaps, "
        "0 direct families, 0 canonical observations, primary gap preserved"
    )


if __name__ == "__main__":
    main()
