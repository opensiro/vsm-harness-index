#!/usr/bin/env python3
"""Validate the experimental direct-S4 benchmark coverage layer."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"
COVERAGE = HERE / "coverage.json"
BENCHMARK_OBSERVATIONS = HERE / "benchmark_observations.json"
CANONICAL_OBSERVATIONS = HERE / "canonical_observations.json"

DIRECT_S4 = {
    "a-evolve-harness-evolution",
    "skillevolbench",
    "evoharnessbench-self-evolving",
}
COVERAGE_CLASSES = {
    "direct-composed",
    "task-solver-not-adaptation-owner",
    "proxy-scaffolded",
    "proxy-observation-specific",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    if not path.exists():
        fail(f"missing canonical assessment: {harness_id}")
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"assessment {harness_id} has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def main() -> None:
    benchmark_map = json.loads(MAP.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))
    canonical_observations = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S4":
        fail("coverage function must be S4")

    direct_s4 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S4" and entry.get("fit") == "direct"
    }
    if direct_s4 != DIRECT_S4:
        fail(f"unexpected direct S4 benchmark map: {sorted(direct_s4)}")

    skilllearn = [
        entry for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S4" and entry.get("benchmark_id") == "skilllearnbench"
    ]
    if len(skilllearn) != 1 or skilllearn[0].get("fit") != "proxy":
        fail("SkillLearnBench must remain proxy pending a stricter future-transfer review")

    if not isinstance(benchmark_observations, list):
        fail("benchmark_observations.json must contain a list")
    if not isinstance(canonical_observations, list):
        fail("canonical_observations.json must contain a list")
    if canonical_observations:
        fail("first direct-S4 pass expects canonical direct registry to remain empty")

    if coverage.get("direct_benchmark_family_count") != len(DIRECT_S4):
        fail("direct_benchmark_family_count mismatch")
    if coverage.get("composed_direct_observation_count") != len(benchmark_observations):
        fail("composed_direct_observation_count mismatch")
    if coverage.get("canonical_direct_observation_count") != len(canonical_observations):
        fail("canonical_direct_observation_count mismatch")

    if len(benchmark_observations) != 3:
        fail("expected exactly three reviewed composed direct S4 evidence records")

    observation_ids: set[str] = set()
    observed_families: set[str] = set()
    for obs in benchmark_observations:
        observation_id = obs.get("observation_id")
        if not isinstance(observation_id, str) or not observation_id:
            fail("benchmark observation requires observation_id")
        if observation_id in observation_ids:
            fail(f"duplicate observation_id: {observation_id}")
        observation_ids.add(observation_id)

        if obs.get("function") != "S4":
            fail(f"{observation_id}: function must be S4")
        benchmark_id = obs.get("benchmark_id")
        if benchmark_id not in DIRECT_S4:
            fail(f"{observation_id}: benchmark is not reviewed direct S4")
        observed_families.add(benchmark_id)
        if obs.get("benchmark_fit") != "direct":
            fail(f"{observation_id}: benchmark_fit must be direct")
        if obs.get("canonical_harness_id") is not None:
            fail(f"{observation_id}: composed evidence must not claim canonical_harness_id")
        if obs.get("canonical_system_eligible") is not False:
            fail(f"{observation_id}: composed evidence must be canonical-ineligible")
        if obs.get("system_compatibility") != "benchmark-scaffolded":
            fail(f"{observation_id}: composed evidence must remain benchmark-scaffolded")
        sources = obs.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{observation_id}: invalid primary_sources")

    if observed_families != DIRECT_S4:
        fail("benchmark observations must cover every reviewed direct S4 family exactly once")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be non-empty")
    seen_cases: set[str] = set()
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen_cases:
            fail(f"duplicate case_id: {case_id}")
        seen_cases.add(case_id)
        if case.get("coverage_class") not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if case.get("admitted_to_canonical_registry") is not False:
            fail(f"{case_id}: coverage case must remain non-admitted")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{case_id}: invalid primary_sources")

        harness_id = case.get("canonical_harness_id")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment not included")
            if case.get("coverage_class") == "task-solver-not-adaptation-owner":
                if fields.get("autonomy_s4") != "—":
                    fail(
                        f"{case_id}: negative-control task solver no longer has S4=—; "
                        "review the boundary before retaining this case"
                    )

    representative = coverage.get("representative_canonical_s4_systems_inspected")
    states = coverage.get("canonical_states_at_review")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S4 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative cohort")
    if not isinstance(states, dict) or set(states) != set(representative):
        fail("canonical_states_at_review must match representative cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{harness_id}: assessment not included")
        current = fields.get("autonomy_s4")
        if current in {None, "—", "?"}:
            fail(f"{harness_id}: current canonical assessment does not establish S4")
        if current != states[harness_id]:
            fail(f"{harness_id}: S4 state drifted from {states[harness_id]!r} to {current!r}")

    print("ok: S4 benchmark coverage validated")
    print(f"reviewed direct S4 families: {len(direct_s4)}")
    print(f"composed direct evidence records: {len(benchmark_observations)}")
    print(f"canonical direct observations: {len(canonical_observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S4 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
