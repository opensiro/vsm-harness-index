#!/usr/bin/env python3
"""Fail-closed validator for the current public-evidence S5 primary-search closure."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S5 = HERE.parent
EXPERIMENT = S5.parent
ROOT = EXPERIMENT.parents[1]
ASSESSMENTS = ROOT / "assessments"
POSITIVE_S5 = {"A", "P", "A(P)", "C(P)"}

EXPECTED_FULL_COHORT = {
    "ouroboros": ("86806ee123ce8e26cc063cc1a618f975eea64f26", "A(P)"),
    "headcount": ("9cbf34005e3e8a980a6af9b55eb226bd926a62b3", "A"),
    "henterprise": ("0bd56397676462e216f92b5b7800919a3597a99a", "A"),
    "argus-agent": ("746f76b7a74a1217507c9ee348eecd3b782f7c92", "P"),
    "loopx": ("ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f", "P"),
    "thclaws": ("cd700937a71a391f052438d139b7b1c5a6456755", "P"),
    "marveen": ("b3f6574a76488b3367b26684f9065acca695a00f", "P"),
    "paperclip": ("352153b5edf02ff4262210c7bd5bfa94bcf37c7c", "P"),
    "squad": ("2099faf51c08a912c359209447011b06decf0565", "P"),
    "kadath": ("db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef", "P"),
    "exo": ("6164288895a5851b2118492c880fb37b543e2ac6", "A(P)"),
    "omniharness": ("fd71e375ff626ae99537163edd3d14b16100d786", "P"),
    "agentos": ("1e9921837385b8218774955b699d949c233e52ea", "P"),
    "cowagent": ("7c55a61e1bccb82c99d97a4a436f598c079f7c9d", "A(P)"),
    "pibot": ("350bf2c8263f31bcda33789c819329bb56f14c00", "P"),
    "wasp": ("8282a76f57aa4d0b7f2071321f064b26be942024", "C(P)"),
    "qwenpaw": ("8af8b6e31a837a0e19ee6c9fffaf1c6b44b5f9ec", "P"),
    "masters-of-ai-harness": ("3f5c4846a2f7ecdf48198d6d1116204132e967a5", "C(P)"),
    "tevarn": ("e5e8e204ca2baf8ff671104ab6bf5529d40213ef", "P"),
    "shep": ("a874b3238fd01ebdbafc11015cccd9a63ed6e2f2", "P"),
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


closure = load(HERE / "s5-primary-search-closure.json")
cohort = load(HERE / "full-canonical-cohort-review.json")
coverage = load(S5 / "coverage.json")
benchmark_observations = load(S5 / "benchmark_observations.json")
canonical_observations = load(S5 / "canonical_observations.json")
baselines = load(EXPERIMENT / "primary-baselines.json")

require(closure["schema_version"] == 1, "S5 closure schema_version drift")
require(closure["status"] == "experimental-non-normative", "S5 closure status drift")
require(closure["tracking_issue"] == 569, "S5 closure tracking issue drift")
require(closure["cohort_reconciliation_issue"] == 621, "S5 full-cohort reconciliation issue drift")
require(closure["disposition"] == "evidence-backed-gap", "S5 closure disposition drift")
require(closure["primary_baseline"] == "gap", "S5 closure must preserve gap")
require(closure["closure_scope"] == "current-public-evidence", "S5 closure scope drift")
require(closure["reviewed_at"] == coverage["reviewed_at"] == cohort["reviewed_at"], "S5 review date drift")
require(closure["full_cohort_review_artifact"] == "full-canonical-cohort-review.json", "S5 full-cohort artifact pointer drift")

expected = closure["evidence_depth"]
require(len(coverage["cases"]) == expected["reviewed_cases"], "S5 reviewed case count drift")
require(coverage["direct_family_count"] == expected["direct_benchmark_families"], "S5 direct family count drift")
require(coverage["composed_direct_observation_count"] == expected["composed_direct_observations"], "S5 composed observation count drift")
require(coverage["canonical_direct_observation_count"] == expected["canonical_direct_observations"], "S5 canonical observation count drift")
require(len(coverage["representative_canonical_s5_systems"]) == expected["representative_canonical_s5_systems"], "S5 representative anchor subset drift")
require(closure["required_direct_chain"] == coverage["direct_benchmark_requirements"], "S5 direct criterion drift")
require(coverage["primary_baseline_additional_requirements"] == [closure["primary_additional_requirement"]], "S5 primary additional requirement drift")

# Full current canonical S5-positive cohort.
require(cohort["schema_version"] == 1, "full S5 cohort schema_version drift")
require(cohort["status"] == "experimental-non-normative", "full S5 cohort status drift")
require(cohort["tracking_issue"] == 621, "full S5 cohort tracking issue drift")
require(cohort["scope"] == "full-current-canonical-s5-positive-cohort", "full S5 cohort scope drift")
require(cohort["direct_chain"] == closure["required_direct_chain"], "full S5 cohort direct-chain drift")
rows = cohort.get("systems")
require(isinstance(rows, list) and len(rows) == 20, "full S5 cohort must contain exactly 20 current positive-S5 systems")
by_id = {row.get("canonical_harness_id"): row for row in rows}
require(len(by_id) == len(rows), "full S5 cohort contains duplicate or missing harness ids")
require(set(by_id) == set(EXPECTED_FULL_COHORT), f"full S5 cohort identity drift: {set(by_id)!r}")

# Derive the positive cohort independently from all included assessments. This
# fails when a new positive S5 system is admitted or an existing state/ref
# changes, forcing a new public-evidence reconciliation transaction.
derived_positive: dict[str, tuple[str, str]] = {}
for path in ASSESSMENTS.glob("*.md"):
    fm = frontmatter(path)
    if fm.get("status") != "included":
        continue
    state = fm.get("autonomy_s5")
    if state not in POSITIVE_S5:
        continue
    harness_id = fm.get("harness_id")
    require(harness_id, f"positive-S5 assessment missing harness_id: {path}")
    derived_positive[harness_id] = (fm.get("review_ref", ""), state)

require(derived_positive == EXPECTED_FULL_COHORT, f"current canonical positive-S5 cohort changed; redo issue #621 reconciliation: {derived_positive!r}")

for harness_id, (expected_ref, expected_state) in EXPECTED_FULL_COHORT.items():
    row = by_id[harness_id]
    require(row.get("canonical_review_revision") == expected_ref, f"{harness_id}: cohort review ref drift")
    require(row.get("canonical_s5_state") == expected_state, f"{harness_id}: cohort S5 state drift")
    require(isinstance(row.get("repository"), str) and row["repository"].startswith("https://github.com/"), f"{harness_id}: repository provenance missing")
    finding = row.get("finding")
    require(isinstance(finding, str) and len(finding) >= 100, f"{harness_id}: public-evidence finding too weak")
    if harness_id == "ouroboros":
        require(row.get("disposition") == "direct-observation", "Ouroboros must remain the direct canonical S5 anchor")
    else:
        require(row.get("disposition") == "no-direct-public-result", f"{harness_id}: unexpected full-cohort disposition")
        require(isinstance(row.get("blocking_gate"), str) and row["blocking_gate"], f"{harness_id}: blocking gate missing")
        require(isinstance(row.get("reopen_when"), str) and len(row["reopen_when"]) >= 80, f"{harness_id}: reopen condition missing")

counts = cohort["counts"]
expected_counts = {
    "canonical_s5_positive_systems": 20,
    "direct_canonical_observations": 1,
    "no_direct_public_result": 19,
    "unresolved": 0,
}
require(counts == expected_counts, f"full S5 cohort counts drift: {counts!r}")
require(closure["full_cohort_state"] == expected_counts, f"S5 closure/full-cohort state drift: {closure['full_cohort_state']!r}")
require(cohort["current_direct_anchor"] == "ouroboros", "full S5 cohort direct anchor drift")

routes = {route["route_id"]: route["status"] for route in closure["reviewed_route_classes"]}
require(routes == {
    "direct-composed-membership-authority": "direct-composed-not-canonical-primary",
    "canonical-native-parent-governed-policy-change": "single-system-descriptive-only",
    "fixed-policy-enforcement-and-governance": "not-direct-s5",
    "value-and-policy-reasoning-proxies": "proxy",
    "live-constitutional-governance-processes": "process-not-harness-benchmark",
    "parent-escalation-protocol": "protocol-not-benchmark",
    "native-constitutional-mechanism": "mechanism-not-benchmark",
    "constitution-policy-optimization": "authority-not-established",
}, f"S5 closure route-state drift: {routes!r}")

case_ids = {case["case_id"] for case in coverage["cases"]}
for required_case in {
    "govsim-selfgovern-membership-authority-direct-composed",
    "ouroboros-parent-governed-policy-change-direct-canonical",
    "agentgovbench-enforcement-not-authority",
    "agent-parliament-ratified-amendment-process",
    "hem-parent-escalation-protocol",
    "constitutional-agent-governance-amendment-mechanism",
    "mac-constitution-optimization-proxy",
    "cmag-fixed-constitution-governance-proxy",
}:
    require(required_case in case_ids, f"S5 closure lost required reviewed case: {required_case}")

require(len(benchmark_observations) == 1, "S5 closure expects one direct composed observation")
require(benchmark_observations[0]["benchmark_id"] == "govsim-selfgovern", "S5 composed observation drift")
require(len(canonical_observations) == 1, "S5 closure expects one canonical direct observation")
canonical = canonical_observations[0]
require(canonical["canonical_harness_id"] == "ouroboros", "S5 canonical observation identity drift")
require(canonical["ownership_mode_observed"] == "parent-governed", "Ouroboros observation must remain parent-governed")
require(canonical["comparison_class"] == "descriptive-only", "Ouroboros observation must remain descriptive-only")
require(by_id["ouroboros"].get("canonical_review_revision") == canonical["canonical_review_revision"], "Ouroboros cohort/observation ref drift")

s5_baseline = baselines["functions"]["S5"]
require(s5_baseline["status"] == "gap", "S5 primary was selected without matched multi-canonical evidence")
require([row["benchmark_id"] for row in s5_baseline["reviewed_direct_families"]] == ["govsim-selfgovern"], "S5 gap metadata lost GovSim-SelfGovern identity")
require(len(closure["reopen_when"]) >= 3, "S5 closure must retain explicit reopen conditions")
require(len(closure["do_not_reopen_for"]) >= 4, "S5 closure must retain anti-churn conditions")
require("20-system canonical S5-positive cohort" in cohort["conclusion"], "full S5 cohort conclusion drift")
require(cohort.get("non_claim"), "full S5 cohort must retain temporal non-claim")

print("S5 primary-search closure validation passed: full current 20-system canonical S5 cohort reconciled; primary gap preserved")
