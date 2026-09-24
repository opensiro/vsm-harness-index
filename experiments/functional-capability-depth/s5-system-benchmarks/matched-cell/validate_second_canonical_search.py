#!/usr/bin/env python3
"""Fail-closed validator for the targeted second-canonical S5 search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S5 = HERE.parent
EXPERIMENT = S5.parent
ROOT = EXPERIMENT.parents[1]

SEARCH_PATH = HERE / "second-canonical-search.json"
COVERAGE_PATH = S5 / "coverage.json"
CANONICAL_OBSERVATIONS_PATH = S5 / "canonical_observations.json"
BASELINES_PATH = EXPERIMENT / "primary-baselines.json"

EXPECTED_CANDIDATES = {
    "headcount": ("9cbf34005e3e8a980a6af9b55eb226bd926a62b3", "A", "no-published-direct-result", "actual-execution-result"),
    "henterprise": ("0bd56397676462e216f92b5b7800919a3597a99a", "A", "no-published-direct-result", "actual-execution-result"),
    "thclaws": ("cd700937a71a391f052438d139b7b1c5a6456755", "P", "mechanism-only-no-runtime-parent-result", "legitimate-deployment-parent-result"),
    "masters-of-ai-harness": ("3f5c4846a2f7ecdf48198d6d1116204132e967a5", "C(P)", "mechanism-only-no-accepted-identity-result", "accepted-parent-identity-change-result"),
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    require(lines and lines[0].strip() == "---", f"missing assessment frontmatter: {path}")
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    raise SystemExit(f"unterminated assessment frontmatter: {path}")


search = load(SEARCH_PATH)
coverage = load(COVERAGE_PATH)
canonical = load(CANONICAL_OBSERVATIONS_PATH)
baselines = load(BASELINES_PATH)

require(search["schema_version"] == 1, "second-canonical search schema_version drift")
require(search["status"] == "experimental-non-normative", "second-canonical search status drift")
require(search["tracking_issue"] == 582, "second-canonical search tracking issue drift")
require(search["searched_at"] == "2026-09-25", "second-canonical search date drift")
require(
    search["search_scope"] == "remaining-representative-canonical-s5-cohort",
    "second-canonical search scope drift",
)

expected_state = search["expected_current_state"]
require(coverage["direct_family_count"] == expected_state["direct_benchmark_families"] == 1, "S5 direct family state drift")
require(
    coverage["composed_direct_observation_count"] == expected_state["composed_direct_observations"] == 1,
    "S5 composed observation state drift",
)
require(
    coverage["canonical_direct_observation_count"] == expected_state["canonical_direct_observations"] == 1,
    "S5 canonical observation count changed; reopen second-canonical search",
)
require(
    baselines["functions"]["S5"]["status"] == expected_state["s5_primary_baseline"] == "gap",
    "S5 primary state changed; reopen second-canonical search",
)

require(len(canonical) == 1, "second-canonical search assumes exactly one admitted canonical S5 observation")
anchor = search["current_anchor"]
observation = canonical[0]
for field in (
    "canonical_harness_id",
    "canonical_review_revision",
    "ownership_mode_observed",
    "comparison_class",
):
    require(anchor[field] == observation[field], f"second-canonical anchor {field} drift")
require(anchor["observation_id"] == observation["observation_id"], "second-canonical anchor observation_id drift")
require(anchor["canonical_s5_state"] == observation["canonical_s5_state"], "second-canonical anchor S5 state drift")

candidates = search.get("candidates")
require(isinstance(candidates, list) and len(candidates) == 4, "second-canonical search must retain four candidates")
actual_ids = {row["canonical_harness_id"] for row in candidates}
require(actual_ids == set(EXPECTED_CANDIDATES), f"second-canonical candidate set drift: {actual_ids!r}")

coverage_status = {
    row["harness_id"]: row["benchmark_status"]
    for row in coverage["representative_canonical_s5_systems"]
}
require(
    coverage_status.get("ouroboros") == "direct-native-descriptive-observation",
    "Ouroboros canonical anchor disappeared from S5 coverage",
)

for row in candidates:
    harness_id = row["canonical_harness_id"]
    expected_ref, expected_s5, expected_disposition, expected_gate = EXPECTED_CANDIDATES[harness_id]
    require(row["canonical_review_revision"] == expected_ref, f"{harness_id}: search ref drift")
    require(row["canonical_s5_state"] == expected_s5, f"{harness_id}: recorded S5 state drift")
    require(row["disposition"] == expected_disposition, f"{harness_id}: search disposition drift")
    require(row["blocking_gate"] == expected_gate, f"{harness_id}: blocking gate drift")
    require(isinstance(row.get("surfaces_reviewed"), list) and row["surfaces_reviewed"], f"{harness_id}: reviewed surfaces missing")
    require(isinstance(row.get("finding"), str) and len(row["finding"]) >= 80, f"{harness_id}: finding too weak")
    require(isinstance(row.get("reopen_when"), str) and len(row["reopen_when"]) >= 80, f"{harness_id}: reopen condition missing")

    assessment = ROOT / "assessments" / f"{harness_id}.md"
    fm = frontmatter(assessment)
    require(fm.get("status") == "included", f"{harness_id}: canonical assessment no longer included")
    require(fm.get("review_ref") == expected_ref, f"{harness_id}: canonical assessment ref changed; redo targeted search")
    require(fm.get("autonomy_s5") == expected_s5, f"{harness_id}: canonical S5 state changed; redo targeted search")

    expected_coverage_status = "candidate-native-no-direct-results"
    require(
        coverage_status.get(harness_id) == expected_coverage_status,
        f"{harness_id}: S5 coverage now contains a direct result; reopen second-canonical search",
    )

require(
    "No second canonical direct S5 observation was admitted" in search["conclusion"],
    "second-canonical search conclusion drift",
)
require(search.get("non_claim"), "second-canonical search must retain scoped non-claim")

print("second canonical S5 search closure validation passed")
