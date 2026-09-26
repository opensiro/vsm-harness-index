#!/usr/bin/env python3
"""Fail-closed validator for the current S2 matched-canonical search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2 = HERE.parent
EXPERIMENT = S2.parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


search = load(HERE / "s2-matched-canonical-search-closure.json")
primary = load(HERE / "s2-primary-search-closure.json")
coverage = load(S2 / "coverage.json")
observations = load(S2 / "observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(search["schema_version"] == 1, "S2 matched-canonical closure schema drift")
require(search["tracking_issue"] == 696, "S2 matched-canonical tracking issue drift")
require(search["status"] == "experimental-non-normative", "S2 matched-canonical status drift")
require(search["function"] == "S2", "S2 matched-canonical function drift")
require(search["scope"] == "current-public-evidence", "S2 matched-canonical scope drift")
require(
    search["disposition"] == "no-materially-matched-canonical-cell",
    "S2 matched-canonical disposition drift",
)
require(search["primary_baseline"] == "gap", "S2 matched-canonical closure must preserve gap")
require(primary.get("matched_canonical_search_issue") == 696, "S2 primary closure lost matched search pointer")
require(primary["primary_baseline"] == "gap", "S2 primary closure no longer records gap")
require(search["reviewed_at"] == primary["reviewed_at"], "S2 matched search/primary review date drift")
require(search["reviewed_at"] == coverage["reviewed_at"], "S2 matched search/coverage review date drift")
require(baselines["functions"]["S2"]["status"] == "gap", "S2 primary baseline unexpectedly selected")

expected_depth = search["current_evidence_depth"]
primary_depth = primary["evidence_depth"]
require(expected_depth["direct_benchmark_families"] == primary_depth["direct_benchmark_families"], "S2 matched search direct-family depth drift")
require(expected_depth["direct_observations"] == primary_depth["direct_observations"], "S2 matched search observation depth drift")
require(expected_depth["canonical_direct_observations"] == primary_depth["canonical_direct_observations"], "S2 matched search canonical observation depth drift")
require(expected_depth["native_proxy_projections"] == primary_depth["native_proxy_projections"], "S2 matched search proxy depth drift")
require(coverage["direct_benchmark_family_count"] == expected_depth["direct_benchmark_families"], "S2 coverage direct-family drift")
require(coverage["direct_observation_count"] == expected_depth["direct_observations"], "S2 coverage observation drift")
require(coverage["canonical_direct_observation_count"] == expected_depth["canonical_direct_observations"], "S2 coverage canonical observation drift")
require(coverage["proxy_projection_count"] == expected_depth["native_proxy_projections"], "S2 coverage proxy drift")

observation_rows = {row["observation_id"]: row for row in observations}
anchors = {row["canonical_harness_id"]: row for row in search["canonical_direct_anchors"]}
require(set(anchors) == {"squad", "thclaws"}, "S2 matched search canonical anchor set drift")
expected_anchors = {
    "squad": (
        "squad-shared-state-conflict-attenuation-2026-03",
        "2099faf51c08a912c359209447011b06decf0565",
    ),
    "thclaws": (
        "thclaws-team-workspace-interference-attenuation-2026",
        "cd700937a71a391f052438d139b7b1c5a6456755",
    ),
}
for harness_id, (observation_id, review_ref) in expected_anchors.items():
    anchor = anchors[harness_id]
    require(anchor["observation_id"] == observation_id, f"{harness_id}: matched-search observation drift")
    require(anchor["canonical_assessment_ref"] == review_ref, f"{harness_id}: matched-search review ref drift")
    require(anchor["comparison_class"] == "descriptive-only", f"{harness_id}: matched-search comparison class drift")
    require(observation_id in observation_rows, f"{harness_id}: canonical S2 observation missing")
    observation = observation_rows[observation_id]
    require(observation.get("canonical_harness_id") == harness_id, f"{harness_id}: canonical observation identity drift")
    require(observation.get("canonical_system_eligible") is True, f"{harness_id}: canonical observation eligibility drift")
    require(observation.get("canonical_assessment_ref") == review_ref, f"{harness_id}: canonical observation ref drift")
    require(observation.get("comparison_class") == "descriptive-only", f"{harness_id}: canonical observation became matched without reopening search")

routes = {row["route_id"]: row for row in search["reviewed_matched_routes"]}
require(
    set(routes)
    == {
        "mao-bench",
        "cooperbench-team-harness",
        "cross-framework-orchestration-benchmarks",
        "merge-resolution-model-benchmarks",
        "verification-fault-injection-benchmarks",
    },
    "S2 matched-search route set drift",
)
require(routes["mao-bench"]["repository"] == "rachitpareek/multi-agent-orchestration-evals", "MAO-Bench repository drift")
require(routes["mao-bench"]["review_ref"] == "3343fe1cf5a24211023a69374d31df3d6711b613", "MAO-Bench reviewed ref drift")
require(routes["mao-bench"]["status"] == "no-published-multi-orchestrator-results", "MAO-Bench blocker drift")
require(routes["cooperbench-team-harness"]["repository"] == "cooperbench/CooperBench", "CooperBench repository drift")
require(routes["cooperbench-team-harness"]["review_ref"] == "63b9d44d9f39a02fccf5bf0052db48a917a011fd", "CooperBench reviewed ref drift")
require(routes["cooperbench-team-harness"]["status"] == "unchanged-provenance-blocker", "CooperBench blocker drift")
require(
    routes["cross-framework-orchestration-benchmarks"]["status"]
    == "benchmark-authored-or-no-direct-s2-disturbance",
    "cross-framework matched-route classification drift",
)
require(
    routes["merge-resolution-model-benchmarks"]["status"] == "single-resolver-not-s2-organization",
    "merge-resolution matched-route classification drift",
)
require(
    routes["verification-fault-injection-benchmarks"]["status"] == "different-vsm-function",
    "verification matched-route classification drift",
)

require(isinstance(search.get("reopen_when"), list) and search["reopen_when"], "S2 matched search lost reopen conditions")
require(isinstance(search.get("do_not_reopen_for"), list) and search["do_not_reopen_for"], "S2 matched search lost anti-churn conditions")
require(
    any("Opensiro-operated" in item for item in search["do_not_reopen_for"]),
    "S2 matched search must not reopen for Opensiro-operated reproduction",
)
require(search.get("non_claim"), "S2 matched search lost non-claim boundary")

print("S2 matched-canonical search closure validation passed")
