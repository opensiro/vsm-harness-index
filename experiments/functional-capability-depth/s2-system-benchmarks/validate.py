#!/usr/bin/env python3
"""Validate the experimental S2 benchmark coverage/gap record."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COVERAGE = HERE / "coverage.json"
OBSERVATIONS = HERE / "observations.json"
PROXY_LINKS = HERE / "proxy_links.json"
BENCHMARK_MAP = HERE.parent / "vsm-benchmark-family-map" / "map.json"
SYSTEM_OBSERVATIONS = HERE.parent / "system-observations"

COVERAGE_CLASSES = {
    "direct-scaffolded",
    "native-proxy",
    "framework-scaffolded",
    "candidate-boundary-unresolved",
    "candidate-no-results",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
EXPECTED_PROXY_PROJECTIONS = {
    "autogen-magentic-one-native-proxy-s2": "autogen-agentchat",
    "squad-marble-native-proxy-s2": "squad",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def assessment_fields(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    if not path.exists():
        fail(f"missing canonical assessment for {harness_id}")
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        fail(f"assessment {path} has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def observation_by_id(observations: list[dict], observation_id: str) -> dict:
    matches = [row for row in observations if row.get("observation_id") == observation_id]
    if len(matches) != 1:
        fail(f"expected exactly one S2 observation {observation_id!r}")
    return matches[0]


def validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:
    proxy_links = json.loads(PROXY_LINKS.read_text(encoding="utf-8"))
    if not isinstance(proxy_links, list):
        fail("proxy_links.json must contain a list")
    if coverage.get("proxy_projection_count") != len(proxy_links):
        fail("proxy_projection_count does not match proxy_links.json")

    projections: dict[str, dict] = {}
    for projection in proxy_links:
        if not isinstance(projection, dict):
            fail("every S2 proxy projection must be an object")
        projection_id = projection.get("projection_id")
        if not isinstance(projection_id, str) or not projection_id:
            fail("every S2 proxy projection requires projection_id")
        if projection_id in projections:
            fail(f"duplicate S2 proxy projection_id: {projection_id}")
        projections[projection_id] = projection

        if projection.get("function") != "S2":
            fail(f"{projection_id}: function must be S2")
        if projection.get("benchmark_fit") != "proxy":
            fail(f"{projection_id}: benchmark_fit must remain proxy")
        if projection.get("system_compatibility") != "native-system":
            fail(f"{projection_id}: proxy projection must remain native-system")

        harness_id = projection.get("canonical_harness_id")
        if not isinstance(harness_id, str) or not harness_id:
            fail(f"{projection_id}: canonical_harness_id required")
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{projection_id}: canonical assessment is not included")
        current_s2 = fields.get("autonomy_s2")
        if current_s2 in {None, "—", "?"}:
            fail(f"{projection_id}: canonical system no longer establishes S2")
        if projection.get("canonical_state_at_review") != current_s2:
            fail(
                f"{projection_id}: canonical S2 state drifted from projection "
                f"{projection.get('canonical_state_at_review')!r} to {current_s2!r}"
            )

        raw_record = projection.get("raw_record")
        if not isinstance(raw_record, str) or not raw_record.startswith("../system-observations/"):
            fail(f"{projection_id}: raw_record must point to shared system-observations")
        raw_path = (HERE / raw_record).resolve()
        if raw_path.parent != SYSTEM_OBSERVATIONS.resolve() or not raw_path.exists():
            fail(f"{projection_id}: raw observation record missing or outside shared directory")
        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        if raw.get("canonical_harness_id") != harness_id:
            fail(f"{projection_id}: raw record canonical_harness_id mismatch")
        raw_ids = {
            row.get("observation_id")
            for row in raw.get("observations", [])
            if isinstance(row, dict)
        }
        requested_ids = projection.get("raw_observation_ids")
        if not isinstance(requested_ids, list) or not requested_ids:
            fail(f"{projection_id}: raw_observation_ids required")
        if any(not isinstance(value, str) or not value for value in requested_ids):
            fail(f"{projection_id}: invalid raw_observation_ids")
        missing = set(requested_ids) - raw_ids
        if missing:
            fail(f"{projection_id}: raw observation ids missing from shared record: {sorted(missing)}")

    if {key: projections[key].get("canonical_harness_id") for key in projections} != EXPECTED_PROXY_PROJECTIONS:
        fail("S2 native proxy projection set drift")

    expected_cases = {
        "autogen-magentic-one-native-proxy-s2": "autogen-magentic-one-native-proxy",
        "squad-marble-native-proxy-s2": "squad-marble-native-proxy",
    }
    for projection_id, case_id in expected_cases.items():
        projection = projections[projection_id]
        case = by_id.get(case_id)
        if case is None:
            fail(f"missing coverage case for {projection_id}: {case_id}")
        if case.get("coverage_class") != "native-proxy":
            fail(f"{case_id}: coverage_class must remain native-proxy")
        if case.get("canonical_harness_id") != projection.get("canonical_harness_id"):
            fail(f"{case_id}: canonical linkage differs from proxy projection")
        if case.get("proxy_projection_ref") != f"proxy_links.json#{projection_id}":
            fail(f"{case_id}: proxy_projection_ref drift")
        if case.get("raw_observation_ref") != projection.get("raw_record"):
            fail(f"{case_id}: raw_observation_ref drift")


def validate_nool_observation(observations: list[dict]) -> None:
    observation = observation_by_id(observations, "nool-trackd-scaleup1-contention-2026-08-21")
    expected = {
        "function": "S2",
        "benchmark_id": "nool-fleet-coordination",
        "benchmark_fit": "direct",
        "boundary_class": "benchmark-defined-agent-fleet",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "benchmark-scaffolded",
        "benchmark_artifact_revision": "126d69b5921be71daffd38c70ec4aa77252b4f39",
        "result_artifact": "results/trackc/fleet_runs.jsonl",
        "result_manifest": "results/replications/MANIFEST.md",
        "model": "claude-sonnet-5",
        "worker_count": 10,
        "ticket_count": 20,
        "nool_version": "6.14.1",
    }
    for field, value in expected.items():
        if observation.get(field) != value:
            fail(f"Nool direct S2 observation {field} drift: {observation.get(field)!r}")

    git_runs = observation.get("git_uncoordinated_runs")
    coordinated_runs = observation.get("coordinated_runs")
    if not isinstance(git_runs, list) or len(git_runs) != 2:
        fail("Nool direct S2 observation must retain two uncoordinated primary replicates")
    if not isinstance(coordinated_runs, list) or len(coordinated_runs) != 2:
        fail("Nool direct S2 observation must retain two coordinated primary replicates")
    if [(row.get("run_id"), row.get("accepted"), row.get("clean_merges")) for row in git_runs] != [
        ("fleet_git_fleet_9a6eb70f", 1, 14),
        ("fleet_git_fleet_803f2288", 13, 13),
    ]:
        fail("Nool direct S2 uncoordinated primary results drift")
    if [(row.get("run_id"), row.get("accepted"), row.get("clean_merges")) for row in coordinated_runs] != [
        ("fleet_nool_fleet_cb7ccf72", 19, 20),
        ("fleet_nool_fleet_2a51582f", 19, 20),
    ]:
        fail("Nool direct S2 coordinated primary results drift")
    if observation.get("excluded_variant", {}).get("run_id") != "fleet_nool_fleet_16e2e1b0":
        fail("Nool direct S2 excluded gate-hole variant drift")
    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(source) for source in sources):
        fail("Nool direct S2 observation must retain immutable HTTPS provenance")


def validate_specification_gap_observation(observations: list[dict]) -> None:
    observation = observation_by_id(observations, "specification-gap-recovery-2026-03")
    expected = {
        "function": "S2",
        "benchmark_id": "specification-gap-recovery",
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "benchmark-defined-two-worker-integration",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "benchmark-scaffolded",
        "benchmark_artifact_revision": "b64059f3ee5cab9b71b834c7b5acc597791880d5",
        "result_artifact": "data/conflict_results/",
        "experiment_artifact": "scripts/conflict_experiment.py",
        "model": "claude-sonnet-4-20250514",
        "task_count": 53,
        "worker_count": 2,
    }
    for field, value in expected.items():
        if observation.get(field) != value:
            fail(f"Specification Gap direct S2 observation {field} drift: {observation.get(field)!r}")

    conditions = observation.get("recovery_conditions")
    if not isinstance(conditions, list):
        fail("Specification Gap recovery_conditions must be a list")
    actual = [(row.get("condition"), row.get("pass_rate")) for row in conditions]
    expected_conditions = [
        ("blind_l3_no_conflict_report", 0.527),
        ("guided_l3_with_conflict_report", 0.527),
        ("spec_only_l0_no_conflict_report", 0.889),
        ("resolve_l0_with_conflict_report", 0.823),
    ]
    if actual != expected_conditions:
        fail("Specification Gap recovery condition results drift")
    if observation.get("single_agent_l0_ceiling") != 0.883:
        fail("Specification Gap single-agent L0 ceiling drift")
    if observation.get("reported_effects") != {
        "full_specification_vs_blind_pp": 36.2,
        "conflict_report_at_l3_pp": 0.0,
    }:
        fail("Specification Gap reported effects drift")
    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(source) for source in sources):
        fail("Specification Gap observation must retain immutable HTTPS provenance")


def main() -> None:
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    benchmark_map = json.loads(BENCHMARK_MAP.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S2":
        fail("coverage function must be S2")
    if not isinstance(observations, list):
        fail("observations.json must contain a list")
    if len(observations) != 2:
        fail("S2 observations.json must contain exactly two direct non-canonical observations")
    if coverage.get("direct_observation_count") != len(observations):
        fail("direct_observation_count does not match observations.json")
    if coverage.get("canonical_direct_observation_count") != 0:
        fail("S2 canonical_direct_observation_count must remain 0")

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    reviewed_direct_s2 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S2" and entry.get("fit") == "direct"
    }
    expected_direct_s2 = {
        "dpbench",
        "stale-semantic-coordination",
        "nool-fleet-coordination",
        "twining-conflict-resolution",
        "specification-gap-recovery",
        "cooperbench-team-harness",
    }
    if reviewed_direct_s2 != expected_direct_s2:
        fail(f"unexpected committed direct-S2 benchmark map: {sorted(reviewed_direct_s2)}")
    if coverage.get("direct_benchmark_family_count") != len(reviewed_direct_s2):
        fail("direct_benchmark_family_count does not match reviewed direct-S2 map")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be a non-empty list")

    seen: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen:
            fail(f"duplicate case_id: {case_id}")
        seen.add(case_id)
        by_id[case_id] = case

        if case.get("coverage_class") not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if case.get("admitted") is not False:
            fail(f"{case_id}: coverage case must remain non-canonical/non-primary")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")

        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources:
            fail(f"{case_id}: primary_sources required")
        if any(not valid_https(source) for source in sources):
            fail(f"{case_id}: all primary_sources must be https URLs")

        harness_id = case.get("canonical_harness_id")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment is not included")

            if harness_id == "langgraph":
                if fields.get("autonomy_s2") != "—":
                    fail("LangGraph negative control no longer has S2=—; review coverage semantics")
            elif case["coverage_class"] == "native-proxy":
                if fields.get("autonomy_s2") in {None, "—", "?"}:
                    fail(f"{case_id}: native-proxy system does not currently establish S2")

    stale = by_id.get("stale-semantic-coordination-direct-scaffolded")
    if stale is None:
        fail("missing STALE direct-S2 coverage case")
    if stale.get("benchmark_fit") != "direct":
        fail("STALE must remain direct S2 at its benchmark-defined boundary")
    if stale.get("coverage_class") != "direct-scaffolded":
        fail("STALE coverage class drift")
    if stale.get("system_compatibility") != "benchmark-scaffolded":
        fail("STALE must remain benchmark-scaffolded")
    if stale.get("canonical_harness_id") is not None:
        fail("STALE must not claim canonical harness S2 ownership")

    nool = by_id.get("nool-fleet-coordination-direct-scaffolded")
    if nool is None:
        fail("missing Nool fleet direct-S2 coverage case")
    if nool.get("benchmark_fit") != "direct" or nool.get("coverage_class") != "direct-scaffolded":
        fail("Nool fleet coordination must remain direct-scaffolded S2 evidence")
    if nool.get("system_compatibility") != "benchmark-scaffolded":
        fail("Nool fleet coordination must remain benchmark-scaffolded")
    if nool.get("canonical_harness_id") is not None:
        fail("Nool fleet observation must not acquire a canonical harness id")
    if nool.get("review_ref") != "126d69b5921be71daffd38c70ec4aa77252b4f39":
        fail("Nool fleet benchmark review_ref drift")
    if nool.get("observation_ref") != "observations.json#nool-trackd-scaleup1-contention-2026-08-21":
        fail("Nool fleet coverage/observation linkage drift")

    twining = by_id.get("twining-conflict-resolution-direct-scaffolded")
    if twining is None:
        fail("missing Twining conflict-resolution direct-S2 coverage case")
    if twining.get("benchmark_fit") != "direct" or twining.get("coverage_class") != "direct-scaffolded":
        fail("Twining conflict-resolution must remain direct-scaffolded S2 evidence")
    if twining.get("system_compatibility") != "benchmark-scaffolded":
        fail("Twining conflict-resolution must remain benchmark-scaffolded")
    if twining.get("canonical_harness_id") is not None:
        fail("Twining conflict-resolution must not acquire a canonical harness id")
    if twining.get("review_ref") != "b6a4d5e5890c5617376ba5c8fb7a628014296663":
        fail("Twining benchmark review_ref drift")
    if twining.get("result_harness_ref") != "63004a1f7697c64a78bc9c83b6cafd461887bc75":
        fail("Twining committed-result harness ref drift")
    if "observation_ref" in twining:
        fail("Twining must not acquire an observation_ref without a new provenance review")

    specification_gap = by_id.get("specification-gap-recovery-direct-scaffolded")
    if specification_gap is None:
        fail("missing Specification Gap direct-S2 coverage case")
    if specification_gap.get("benchmark_fit") != "direct" or specification_gap.get("coverage_class") != "direct-scaffolded":
        fail("Specification Gap recovery must remain direct-scaffolded S2 evidence")
    if specification_gap.get("system_compatibility") != "benchmark-scaffolded":
        fail("Specification Gap recovery must remain benchmark-scaffolded")
    if specification_gap.get("canonical_harness_id") is not None:
        fail("Specification Gap recovery must not acquire a canonical harness id")
    if specification_gap.get("review_ref") != "b64059f3ee5cab9b71b834c7b5acc597791880d5":
        fail("Specification Gap review_ref drift")
    if specification_gap.get("observation_ref") != "observations.json#specification-gap-recovery-2026-03":
        fail("Specification Gap coverage/observation linkage drift")

    cooperbench = by_id.get("cooperbench-team-harness-direct-scaffolded")
    if cooperbench is None:
        fail("missing CooperBench team-harness direct-S2 coverage case")
    if cooperbench.get("benchmark_fit") != "direct" or cooperbench.get("coverage_class") != "direct-scaffolded":
        fail("CooperBench team harness must remain direct-scaffolded S2 evidence")
    if cooperbench.get("system_compatibility") != "benchmark-scaffolded":
        fail("CooperBench team harness must remain benchmark-scaffolded")
    if cooperbench.get("canonical_harness_id") is not None:
        fail("CooperBench team harness must not acquire a canonical harness id")
    if cooperbench.get("review_ref") != "63b9d44d9f39a02fccf5bf0052db48a917a011fd":
        fail("CooperBench review_ref drift")
    if "observation_ref" in cooperbench:
        fail("CooperBench must not acquire an observation_ref without a new provenance review")

    validate_nool_observation(observations)
    validate_specification_gap_observation(observations)
    validate_proxy_links(coverage, by_id)

    representative = coverage.get("representative_canonical_s2_systems_inspected")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S2 cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative S2 cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"representative {harness_id}: assessment not included")
        if fields.get("autonomy_s2") in {None, "—", "?"}:
            fail(f"representative {harness_id}: current canonical assessment does not establish S2")

    print("ok: S2 coverage gap validated")
    print(f"reviewed direct S2 families: {len(reviewed_direct_s2)}")
    print(f"direct observations: {len(observations)}")
    print(f"canonical direct observations: {coverage.get('canonical_direct_observation_count')}")
    print(f"native proxy projections: {coverage.get('proxy_projection_count')}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S2 systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
