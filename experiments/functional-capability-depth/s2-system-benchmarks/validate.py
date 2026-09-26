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
    "direct-native-noncanonical",
    "direct-native-canonical",
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
EXPECTED_OBSERVATION_IDS = {
    "nool-trackd-scaleup1-contention-2026-08-21",
    "specification-gap-recovery-2026-03",
    "codecrdt-parallel-convergence-2025-10",
    "grit-synthetic-merge-contention-2026-04",
    "agentroom-parallel-merge-t4-sonnet46-2026-08",
    "squad-shared-state-conflict-attenuation-2026-03",
    "thclaws-team-workspace-interference-attenuation-2026",
}
EXPECTED_CANONICAL_OBSERVATION_IDS = {
    "squad-shared-state-conflict-attenuation-2026-03",
    "thclaws-team-workspace-interference-attenuation-2026",
}
EXPECTED_DIRECT_S2 = {
    "dpbench",
    "stale-semantic-coordination",
    "nool-fleet-coordination",
    "twining-conflict-resolution",
    "specification-gap-recovery",
    "cooperbench-team-harness",
    "codecrdt-observation-coordination",
    "grit-merge-contention",
    "agentroom-concurrent-coding",
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


def require_fields(row: dict, expected: dict[str, object], label: str) -> None:
    for field, value in expected.items():
        if row.get(field) != value:
            fail(f"{label} {field} drift: {row.get(field)!r}")


def require_sources(row: dict, minimum: int, label: str, required: set[str] | None = None) -> None:
    sources = row.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < minimum:
        fail(f"{label} must retain at least {minimum} public sources")
    if any(not valid_https(source) for source in sources):
        fail(f"{label} must retain HTTPS provenance")
    if required is not None and not required.issubset(set(sources)):
        fail(f"{label} lost required immutable provenance")


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

        if projection.get("function") != "S2" or projection.get("benchmark_fit") != "proxy":
            fail(f"{projection_id}: proxy semantics drift")
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
            fail(f"{projection_id}: canonical S2 state drift")

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

    actual = {key: projections[key].get("canonical_harness_id") for key in projections}
    if actual != EXPECTED_PROXY_PROJECTIONS:
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
    row = observation_by_id(observations, "nool-trackd-scaleup1-contention-2026-08-21")
    require_fields(row, {
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
    }, "Nool direct S2 observation")
    git_runs = row.get("git_uncoordinated_runs")
    coordinated_runs = row.get("coordinated_runs")
    if [(r.get("run_id"), r.get("accepted"), r.get("clean_merges")) for r in git_runs or []] != [
        ("fleet_git_fleet_9a6eb70f", 1, 14),
        ("fleet_git_fleet_803f2288", 13, 13),
    ]:
        fail("Nool direct S2 uncoordinated primary results drift")
    if [(r.get("run_id"), r.get("accepted"), r.get("clean_merges")) for r in coordinated_runs or []] != [
        ("fleet_nool_fleet_cb7ccf72", 19, 20),
        ("fleet_nool_fleet_2a51582f", 19, 20),
    ]:
        fail("Nool direct S2 coordinated primary results drift")
    if row.get("excluded_variant", {}).get("run_id") != "fleet_nool_fleet_16e2e1b0":
        fail("Nool direct S2 excluded gate-hole variant drift")
    require_sources(row, 4, "Nool direct S2 observation")


def validate_specification_gap_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "specification-gap-recovery-2026-03")
    require_fields(row, {
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
    }, "Specification Gap direct S2 observation")
    expected_conditions = [
        ("blind_l3_no_conflict_report", 0.527),
        ("guided_l3_with_conflict_report", 0.527),
        ("spec_only_l0_no_conflict_report", 0.889),
        ("resolve_l0_with_conflict_report", 0.823),
    ]
    actual = [(r.get("condition"), r.get("pass_rate")) for r in row.get("recovery_conditions", [])]
    if actual != expected_conditions:
        fail("Specification Gap recovery condition results drift")
    if row.get("single_agent_l0_ceiling") != 0.883:
        fail("Specification Gap single-agent L0 ceiling drift")
    if row.get("reported_effects") != {
        "full_specification_vs_blind_pp": 36.2,
        "conflict_report_at_l3_pp": 0.0,
    }:
        fail("Specification Gap reported effects drift")
    require_sources(row, 4, "Specification Gap observation")


def validate_codecrdt_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "codecrdt-parallel-convergence-2025-10")
    require_fields(row, {
        "function": "S2",
        "benchmark_id": "codecrdt-observation-coordination",
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "product-defined-parallel-coding-team",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
        "benchmark_artifact_revision": "8fa5a307062025c900e9de27696f4e804a0a7809",
        "result_artifact": "evaluation/evaluation_results/checkpoint.json",
        "result_report": "evaluation/evaluation_results/evaluation_report.yaml",
        "environment_artifact": "evaluation/evaluation_results/environment_info.json",
        "objective_metrics_artifact": "evaluation/evaluation_results/objective_metrics.csv",
        "model": "Claude Sonnet 4.5",
        "task_count": 6,
        "runs_per_task_per_mode": 50,
        "total_evaluations": 600,
        "sequential_runs": 300,
        "parallel_runs": 300,
    }, "CodeCRDT direct S2 observation")
    if row.get("environment") != {
        "platform": "Linux",
        "architecture": "aarch64",
        "python_version": "3.12.3",
        "temperature": 0.0,
        "random_seed": 42,
        "max_concurrent_requests": 1,
    }:
        fail("CodeCRDT environment provenance drift")
    props = row.get("reported_parallel_properties", {})
    if props.get("convergence_rate") != 1.0 or props.get("merge_failures") != 0:
        fail("CodeCRDT descriptive convergence/merge-failure report drift")
    if "5-10%" not in str(props.get("semantic_conflicts", "")):
        fail("CodeCRDT residual semantic-conflict limitation must remain explicit")
    if "does not include a matched uncoordinated-parallel arm" not in str(row.get("comparison_limitation", "")):
        fail("CodeCRDT must remain descriptive-only without an uncoordinated-parallel control")
    require_sources(row, 6, "CodeCRDT observation")


def validate_grit_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "grit-synthetic-merge-contention-2026-04")
    require_fields(row, {
        "function": "S2",
        "benchmark_id": "grit-merge-contention",
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "product-defined-parallel-coding-coordination",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "native-system",
        "comparison_class": "partially-matched",
        "benchmark_artifact_revision": "a2c48735e0a16c49ca1541c4865fce438c479405",
        "result_artifact": "tests/gen_graph.py",
        "protocol_artifact": "scripts/sweep/bench.sh",
        "experiment": "synthetic merge-contention sweep",
        "date": "2026-04-06",
        "agent_counts": [1, 2, 5, 10, 20, 50],
        "rounds_per_iteration": 5,
        "iterations": 5,
    }, "Grit direct S2 observation")
    if row.get("reported_raw_git_failures_per_iteration") != [
        [0, 5, 20, 43, 84, 175],
        [0, 5, 20, 42, 85, 175],
        [0, 5, 20, 43, 83, 175],
        [0, 5, 20, 44, 83, 175],
        [0, 5, 20, 44, 82, 175],
    ]:
        fail("Grit committed raw-git failure arrays drift")
    if row.get("reported_raw_git_conflicts_per_iteration") != [
        [0, 39, 88, 99, 136, 175],
        [0, 38, 85, 88, 129, 175],
        [0, 37, 77, 85, 122, 175],
        [0, 37, 63, 88, 126, 175],
        [0, 38, 85, 89, 136, 175],
    ]:
        fail("Grit committed raw-git conflict arrays drift")
    if row.get("reported_grit_failures") != [0, 0, 0, 0, 0, 0]:
        fail("Grit reported zero-failure series drift")
    expected_rates = {"1": 0.0, "2": 0.5, "5": 0.8, "10": 0.864, "20": 0.834, "50": 0.7}
    if row.get("reported_mean_raw_git_failure_rates") != expected_rates:
        fail("Grit mean raw-git failure rates drift")
    if row.get("reported_mean_grit_failure_rates") != {key: 0.0 for key in expected_rates}:
        fail("Grit mean Grit failure rates drift")
    if "gitignored" not in str(row.get("provenance_limitation", "")):
        fail("Grit observation must retain missing raw-run-ledger limitation")
    if "partially matched" not in str(row.get("comparison_limitation", "")):
        fail("Grit observation must remain partially matched")
    require_sources(row, 4, "Grit observation")


def validate_agentroom_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "agentroom-parallel-merge-t4-sonnet46-2026-08")
    require_fields(row, {
        "function": "S2",
        "benchmark_id": "agentroom-concurrent-coding",
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "paper-defined-concurrent-coding-team",
        "canonical_harness_id": None,
        "canonical_system_eligible": False,
        "system_compatibility": "native-system",
        "comparison_class": "partially-matched",
        "paper": "https://arxiv.org/abs/2608.23740",
        "paper_version": "v1",
        "paper_date": "2026-08-24",
        "model": "Sonnet 4.6",
        "worker_count": 2,
        "task": "T4 financial ledger",
        "task_budget_seconds": 600,
    }, "AgentRoom direct S2 observation")
    if "benchmark_artifact_revision" in row:
        fail("AgentRoom must not invent a source repository revision")
    if row.get("budget_fair_analysis_pool_seconds") != [30, 700]:
        fail("AgentRoom budget-fair analysis pool drift")
    control, treatment, comparison = row.get("control"), row.get("treatment"), row.get("reported_comparison")
    if not all(isinstance(x, dict) for x in (control, treatment, comparison)):
        fail("AgentRoom control/treatment/comparison records must remain objects")
    if (control.get("condition"), control.get("mean_quality"), control.get("n"), control.get("sigma")) != ("parallel-merge", 0.456, 12, 0.178):
        fail("AgentRoom parallel-merge control result drift")
    if (treatment.get("condition"), treatment.get("mean_quality"), treatment.get("n"), treatment.get("sigma")) != ("AgentRoom", 0.669, 14, 0.140):
        fail("AgentRoom treatment result drift")
    if comparison != {"mean_difference": 0.213, "welch_t": 3.35, "p_value": 0.003}:
        fail("AgentRoom reported comparison drift")
    if "full AgentRoom coordination bundle" not in row.get("comparison_limitation", ""):
        fail("AgentRoom bundle-treatment limitation must remain explicit")
    if "no software revision" not in row.get("provenance_limitation", ""):
        fail("AgentRoom paper-only provenance limitation must remain explicit")
    if "404" not in row.get("source_repository_status_at_review", ""):
        fail("AgentRoom source-repository availability status must remain explicit")
    require_sources(row, 2, "AgentRoom direct observation", {
        "https://arxiv.org/abs/2608.23740",
        "https://arxiv.org/abs/2608.23740v1",
    })


def validate_squad_canonical_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "squad-shared-state-conflict-attenuation-2026-03")
    expected = {
        "function": "S2",
        "benchmark_id": None,
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-squad-project-team",
        "canonical_harness_id": "squad",
        "canonical_system_eligible": True,
        "canonical_assessment_ref": "2099faf51c08a912c359209447011b06decf0565",
        "canonical_state_at_review": "A",
        "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
    }
    require_fields(row, expected, "Squad canonical direct S2 observation")
    fields = assessment_fields("squad")
    if fields.get("status") != "included" or fields.get("review_ref") != expected["canonical_assessment_ref"]:
        fail("Squad canonical assessment anchor drift")
    if fields.get("autonomy_s2") != "A":
        fail("Squad canonical S2 state drift")
    if row.get("operational_commits") != [
        "34925f2f5bec49742216ab9dd93c756fbe1aa8c9",
        "e7e6255aa84e04993d568a10331bf9da6661b478",
        "6e304ec6d2f1d385226fba074a1192a3eab7b5cb",
    ]:
        fail("Squad operational evidence lineage drift")
    require_sources(row, 5, "Squad canonical direct observation")


def validate_thclaws_canonical_observation(observations: list[dict]) -> None:
    row = observation_by_id(observations, "thclaws-team-workspace-interference-attenuation-2026")
    expected = {
        "function": "S2",
        "benchmark_id": None,
        "benchmark_fit": "direct",
        "evidence_source_class": "first-party-reported",
        "boundary_class": "canonical-thclaws-agent-teams",
        "canonical_harness_id": "thclaws",
        "canonical_system_eligible": True,
        "canonical_assessment_ref": "cd700937a71a391f052438d139b7b1c5a6456755",
        "canonical_state_at_review": "A",
        "system_compatibility": "native-system",
        "comparison_class": "descriptive-only",
    }
    require_fields(row, expected, "thClaws canonical direct S2 observation")
    fields = assessment_fields("thclaws")
    if fields.get("status") != "included":
        fail("thClaws canonical assessment no longer included")
    if fields.get("review_ref") != expected["canonical_assessment_ref"]:
        fail("thClaws canonical assessment ref drift")
    if fields.get("autonomy_s2") != "A":
        fail("thClaws canonical S2 state drift")
    if row.get("operational_commits") != [
        "a64d1ff47f5c4ca7361087dc5e771b2a18422e4d",
        "db0efe8a6f5ba49da0bafeba84ae4835a09a946b",
    ]:
        fail("thClaws operational evidence lineage drift")
    if row.get("operational_issues") != [125, 200, 202]:
        fail("thClaws operational issue lineage drift")
    if "257 commits" not in str(row.get("subsequent_operation", "")):
        fail("thClaws canonical-lineage ancestry statement drift")
    require_sources(row, 6, "thClaws canonical direct observation", {
        "https://github.com/thClaws/thClaws/commit/a64d1ff47f5c4ca7361087dc5e771b2a18422e4d",
        "https://github.com/thClaws/thClaws/issues/125",
        "https://github.com/thClaws/thClaws/commit/db0efe8a6f5ba49da0bafeba84ae4835a09a946b",
        "https://github.com/thClaws/thClaws/blob/cd700937a71a391f052438d139b7b1c5a6456755/crates/core/src/tools/bash.rs",
        "https://github.com/thClaws/thClaws/issues/200",
        "https://github.com/thClaws/thClaws/issues/202",
    })


def require_case(by_id: dict[str, dict], case_id: str, expected: dict[str, object]) -> dict:
    case = by_id.get(case_id)
    if case is None:
        fail(f"missing S2 coverage case: {case_id}")
    require_fields(case, expected, f"coverage case {case_id}")
    return case


def main() -> None:
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    benchmark_map = json.loads(BENCHMARK_MAP.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1 or coverage.get("function") != "S2":
        fail("coverage schema/function drift")
    if coverage.get("reviewed_at") != "2026-09-26":
        fail("S2 coverage review date drift")
    if not isinstance(observations, list):
        fail("observations.json must contain a list")
    observation_ids = {row.get("observation_id") for row in observations if isinstance(row, dict)}
    if len(observations) != 7 or observation_ids != EXPECTED_OBSERVATION_IDS:
        fail(f"S2 observation set drift: {sorted(str(value) for value in observation_ids)}")
    if coverage.get("direct_observation_count") != 7:
        fail("S2 direct_observation_count must remain 7")
    canonical_observations = [row for row in observations if row.get("canonical_system_eligible") is True]
    canonical_ids = {row.get("observation_id") for row in canonical_observations}
    if coverage.get("canonical_direct_observation_count") != 2 or canonical_ids != EXPECTED_CANONICAL_OBSERVATION_IDS:
        fail(f"S2 canonical direct observation set drift: {sorted(str(value) for value in canonical_ids)}")

    if set(coverage.get("coverage_classes", [])) != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    reviewed_direct_s2 = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S2" and entry.get("fit") == "direct"
    }
    if reviewed_direct_s2 != EXPECTED_DIRECT_S2:
        fail(f"unexpected committed direct-S2 benchmark map: {sorted(reviewed_direct_s2)}")
    if coverage.get("direct_benchmark_family_count") != len(EXPECTED_DIRECT_S2):
        fail("direct_benchmark_family_count does not match reviewed direct-S2 map")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or len(cases) != 24:
        fail("S2 coverage must retain exactly 24 reviewed cases")
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in by_id:
            fail(f"duplicate case_id: {case_id}")
        by_id[case_id] = case
        if case.get("coverage_class") not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if case.get("admitted") is not False:
            fail(f"{case_id}: coverage case must remain non-primary")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")
        require_sources(case, 1, f"coverage case {case_id}")

        harness_id = case.get("canonical_harness_id")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment is not included")
            if harness_id == "langgraph":
                if fields.get("autonomy_s2") != "—":
                    fail("LangGraph negative control no longer has S2=—; review coverage semantics")
            elif case.get("coverage_class") == "native-proxy":
                if fields.get("autonomy_s2") in {None, "—", "?"}:
                    fail(f"{case_id}: native-proxy system does not currently establish S2")
            elif case.get("coverage_class") == "direct-native-canonical":
                if fields.get("autonomy_s2") != case.get("canonical_state_at_review"):
                    fail(f"{case_id}: canonical S2 state drift")
                if fields.get("review_ref") != case.get("canonical_review_ref"):
                    fail(f"{case_id}: canonical assessment ref drift")

    require_case(by_id, "dpbench-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
    })
    require_case(by_id, "stale-semantic-coordination-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
    })
    require_case(by_id, "nool-fleet-coordination-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
        "review_ref": "126d69b5921be71daffd38c70ec4aa77252b4f39",
        "observation_ref": "observations.json#nool-trackd-scaleup1-contention-2026-08-21",
    })
    twining = require_case(by_id, "twining-conflict-resolution-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
        "review_ref": "b6a4d5e5890c5617376ba5c8fb7a628014296663",
        "result_harness_ref": "63004a1f7697c64a78bc9c83b6cafd461887bc75",
    })
    if "observation_ref" in twining:
        fail("Twining must not acquire an observation_ref without a new provenance review")
    require_case(by_id, "specification-gap-recovery-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
        "review_ref": "b64059f3ee5cab9b71b834c7b5acc597791880d5",
        "observation_ref": "observations.json#specification-gap-recovery-2026-03",
    })
    cooperbench = require_case(by_id, "cooperbench-team-harness-direct-scaffolded", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-scaffolded",
        "system_compatibility": "benchmark-scaffolded",
        "canonical_harness_id": None,
        "review_ref": "63b9d44d9f39a02fccf5bf0052db48a917a011fd",
    })
    if "observation_ref" in cooperbench:
        fail("CooperBench must not acquire an observation_ref without a new provenance review")
    require_case(by_id, "codecrdt-observation-driven-direct-native-noncanonical", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-native-noncanonical",
        "system_compatibility": "native-system",
        "canonical_harness_id": None,
        "review_ref": "8fa5a307062025c900e9de27696f4e804a0a7809",
        "observation_ref": "observations.json#codecrdt-parallel-convergence-2025-10",
    })
    require_case(by_id, "grit-merge-contention-direct-native-noncanonical", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-native-noncanonical",
        "system_compatibility": "native-system",
        "canonical_harness_id": None,
        "review_ref": "a2c48735e0a16c49ca1541c4865fce438c479405",
        "observation_ref": "observations.json#grit-synthetic-merge-contention-2026-04",
    })
    agentroom = require_case(by_id, "agentroom-concurrent-coding-direct-native-noncanonical", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-native-noncanonical",
        "system_compatibility": "native-system",
        "canonical_harness_id": None,
        "paper": "https://arxiv.org/abs/2608.23740",
        "observation_ref": "observations.json#agentroom-parallel-merge-t4-sonnet46-2026-08",
    })
    if "review_ref" in agentroom:
        fail("AgentRoom coverage must not invent a source repository revision")
    require_case(by_id, "squad-shared-state-conflict-direct-native-canonical", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-native-canonical",
        "system_compatibility": "native-system",
        "canonical_harness_id": "squad",
        "canonical_state_at_review": "A",
        "canonical_review_ref": "2099faf51c08a912c359209447011b06decf0565",
        "observation_ref": "observations.json#squad-shared-state-conflict-attenuation-2026-03",
    })
    require_case(by_id, "thclaws-team-workspace-interference-direct-native-canonical", {
        "benchmark_fit": "direct",
        "coverage_class": "direct-native-canonical",
        "system_compatibility": "native-system",
        "canonical_harness_id": "thclaws",
        "canonical_state_at_review": "A",
        "canonical_review_ref": "cd700937a71a391f052438d139b7b1c5a6456755",
        "observation_ref": "observations.json#thclaws-team-workspace-interference-attenuation-2026",
    })

    validate_nool_observation(observations)
    validate_specification_gap_observation(observations)
    validate_codecrdt_observation(observations)
    validate_grit_observation(observations)
    validate_agentroom_observation(observations)
    validate_squad_canonical_observation(observations)
    validate_thclaws_canonical_observation(observations)
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
