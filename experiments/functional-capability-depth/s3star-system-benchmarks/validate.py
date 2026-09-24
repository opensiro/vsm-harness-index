#!/usr/bin/env python3
"""Validate the experimental direct-S3* benchmark coverage layer."""

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

COMPOSED_DIRECT_S3STAR = {"truecall-runtime-verification", "swe-review", "harness-bench-adversarial-review"}
DIRECT_S3STAR = COMPOSED_DIRECT_S3STAR | {"appliedscientist-iterative-review", "data-to-paper-review-revision"}
EXPECTED_OBSERVATION_IDS = {
    "truecall-tau2-retail-silent-failure-2026-06",
    "swe-review-generate-review-revise-2026-07",
    "harness-bench-pilot4-review-revise-reverify-2026-07",
}
CANONICAL_OBSERVATION_ID = "appliedscientist-iterative-review-2026-09"
CANONICAL_DIRECT_HARNESS = "appliedscientist"
CANONICAL_REVIEW_REF = "762824fd41598370e75588861b48991b0a9fd784"
DATA_TO_PAPER_OBSERVATION_ID = "data-to-paper-review-revision-2024"
DATA_TO_PAPER_HARNESS = "data-to-paper"
DATA_TO_PAPER_REVIEW_REF = "81df14c4b9600466e645c3b2b336cc54daa3df3a"

COVERAGE_CLASSES = {
    "direct-composed",
    "direct-native",
    "native-proxy",
    "external-wrapper-not-native",
    "proxy-scaffolded",
    "capability-label-not-s3star",
    "candidate-native-no-direct-results",
}
SYSTEM_COMPATIBILITY = {
    "native-system",
    "adapter-preserved",
    "benchmark-scaffolded",
    "unclear",
}
REQUIRED_CASE_IDS = {
    "truecall-tau2-direct-composed",
    "swe-review-direct-composed",
    "harness-bench-adversarial-review-direct-composed",
    "swe-agent-swebench-native-proxy-s3star",
    "codex-truecall-external-wrapper",
    "auditbench-proxy-scaffolded",
    "harnessaudit-trajectory-audit-proxy-scaffolded",
    "silentprobe-self-monitoring-negative-control",
    "pawbench-self-verification-label-not-s3star",
    "codex-guardian-native-no-direct-results",
    "omnigent-polly-reviewer-native-no-direct-results",
    "thclaws-team-audit-native-no-direct-results",
    "reigen-verification-native-no-direct-results",
    "redteam-adversarial-review-native-no-direct-results",
    "appliedscientist-native-s3star-direct",
    "data-to-paper-native-s3star-direct",
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


def validate_canonical_observation(observation: dict) -> None:
    if observation.get("observation_id") != CANONICAL_OBSERVATION_ID:
        fail("unexpected canonical direct S3* observation_id")
    if observation.get("function") != "S3*":
        fail("canonical observation function must be S3*")
    if observation.get("benchmark_id") != "appliedscientist-iterative-review":
        fail("AppliedScientist canonical observation benchmark linkage drift")
    if observation.get("benchmark_fit") != "direct":
        fail("AppliedScientist canonical observation must remain direct")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("AppliedScientist result must remain first-party-reported")
    if observation.get("boundary_class") != "canonical-native-system":
        fail("AppliedScientist observation must retain canonical-native-system boundary")
    if observation.get("canonical_harness_id") != CANONICAL_DIRECT_HARNESS:
        fail("AppliedScientist canonical_harness_id drift")
    if observation.get("canonical_system_eligible") is not True:
        fail("AppliedScientist observation must remain canonical-system eligible")
    if observation.get("system_compatibility") != "native-system":
        fail("AppliedScientist observation must remain native-system")
    if observation.get("canonical_review_revision") != CANONICAL_REVIEW_REF:
        fail("AppliedScientist canonical review ref drift")

    fields = assessment_fields(CANONICAL_DIRECT_HARNESS)
    if fields.get("status") != "included":
        fail("AppliedScientist canonical assessment must remain included")
    if fields.get("autonomy_s3_star") != "A":
        fail("AppliedScientist no longer establishes canonical S3*=A")
    if fields.get("review_ref") != CANONICAL_REVIEW_REF:
        fail("AppliedScientist assessment review_ref drift")

    expected_counts = {
        "paper_count": 30,
        "rejected_paper_count": 25,
        "borderline_paper_count": 5,
        "revision_rounds": 5,
        "reported_execution_weaknesses_total": 150,
        "reported_execution_weaknesses_resolved": 128,
        "reported_idea_weaknesses_total": 18,
        "reported_idea_weaknesses_resolved": 2,
    }
    for field, expected in expected_counts.items():
        if observation.get(field) != expected:
            fail(f"AppliedScientist reported field drift: {field}")
    if observation.get("reported_execution_weakness_resolution_rate") != 0.853:
        fail("AppliedScientist execution-weakness resolution-rate drift")
    if observation.get("reported_idea_weakness_resolution_rate") != 0.111:
        fail("AppliedScientist idea-weakness resolution-rate drift")
    if observation.get("comparison_class") != "within-system-guidance-comparison":
        fail("AppliedScientist comparison class drift")

    audit_loop = observation.get("audit_loop")
    if not isinstance(audit_loop, list) or len(audit_loop) < 6:
        fail("AppliedScientist observation must preserve the full review-correct-re-review loop")
    loop_text = " ".join(audit_loop)
    for phrase in ("fresh Reviewer", "feedback becomes guidance", "submitted to another fresh independent review"):
        if phrase not in loop_text:
            fail(f"AppliedScientist audit-loop closure drift: {phrase}")

    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str) or CANONICAL_REVIEW_REF not in limitation:
        fail("AppliedScientist provenance limitation must retain the pinned review ref")
    if "not independently reproduced" not in limitation:
        fail("AppliedScientist provenance limitation must preserve non-reproduction boundary")
    if "does not expose an explicit repository URL" not in limitation:
        fail("AppliedScientist publication/repository binding caveat must remain explicit")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(s) for s in sources):
        fail("AppliedScientist observation requires publication plus pinned first-party code sources")
    if "https://arxiv.org/abs/2609.14738" not in sources:
        fail("AppliedScientist observation must retain the publication source")
    if not any(CANONICAL_REVIEW_REF in source for source in sources if "github.com" in source):
        fail("AppliedScientist observation must retain pinned repository evidence")


def validate_data_to_paper_observation(observation: dict) -> None:
    if observation.get("observation_id") != DATA_TO_PAPER_OBSERVATION_ID:
        fail("unexpected data-to-paper canonical observation_id")
    if observation.get("function") != "S3*" or observation.get("benchmark_fit") != "direct":
        fail("data-to-paper canonical observation must remain direct S3*")
    if observation.get("benchmark_id") != "data-to-paper-review-revision":
        fail("data-to-paper benchmark linkage drift")
    if observation.get("evidence_source_class") != "first-party-reported":
        fail("data-to-paper result must remain first-party-reported")
    if observation.get("boundary_class") != "canonical-native-system":
        fail("data-to-paper observation must retain canonical-native-system boundary")
    if observation.get("canonical_harness_id") != DATA_TO_PAPER_HARNESS:
        fail("data-to-paper canonical_harness_id drift")
    if observation.get("canonical_system_eligible") is not True:
        fail("data-to-paper observation must remain canonical-system eligible")
    if observation.get("system_compatibility") != "native-system":
        fail("data-to-paper observation must remain native-system")
    if observation.get("canonical_review_revision") != DATA_TO_PAPER_REVIEW_REF:
        fail("data-to-paper canonical review ref drift")
    if observation.get("comparison_class") != "descriptive-only":
        fail("data-to-paper observation must remain descriptive-only")
    if observation.get("published_example_count") != 1:
        fail("data-to-paper published example count drift")
    if observation.get("published_example_reference") != "Figure 2B / Supplementary Run A5":
        fail("data-to-paper published example reference drift")
    if observation.get("aggregate_s3star_metric_reported") is not False:
        fail("data-to-paper must not acquire an invented aggregate S3* metric")

    fields = assessment_fields(DATA_TO_PAPER_HARNESS)
    if fields.get("status") != "included":
        fail("data-to-paper canonical assessment must remain included")
    if fields.get("autonomy_s3_star") != "A":
        fail("data-to-paper no longer establishes canonical S3*=A")
    if fields.get("review_ref") != DATA_TO_PAPER_REVIEW_REF:
        fail("data-to-paper assessment review_ref drift")

    audit_loop = observation.get("audit_loop")
    if not isinstance(audit_loop, list) or len(audit_loop) < 6:
        fail("data-to-paper observation must preserve full reviewer-correct-review closure")
    loop_text = " ".join(audit_loop)
    for phrase in ("separate role-inverted Reviewer", "transferred back into the performer", "concludes only after the product passes"):
        if phrase not in loop_text:
            fail(f"data-to-paper audit-loop closure drift: {phrase}")

    limitation = observation.get("provenance_limitation")
    if not isinstance(limitation, str) or DATA_TO_PAPER_REVIEW_REF not in limitation:
        fail("data-to-paper provenance limitation must retain pinned review ref")
    if "not independently reproduced" not in limitation:
        fail("data-to-paper provenance limitation must preserve non-reproduction boundary")
    if "does not bind Supplementary Run A5 to the exact canonical review revision" not in limitation:
        fail("data-to-paper historical run/revision caveat must remain explicit")

    sources = observation.get("primary_sources")
    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(s) for s in sources):
        fail("data-to-paper observation requires publication plus pinned first-party code sources")
    if "https://doi.org/10.1056/AIoa2400555" not in sources:
        fail("data-to-paper observation must retain the publication source")
    if not any(DATA_TO_PAPER_REVIEW_REF in source for source in sources if "github.com" in source):
        fail("data-to-paper observation must retain pinned repository evidence")
    metric_note = observation.get("metric_note")
    if not isinstance(metric_note, str) or "does not report an aggregate S3*-specific" not in metric_note:
        fail("data-to-paper no-score boundary must remain explicit")

def main() -> None:
    benchmark_map = json.loads(MAP.read_text(encoding="utf-8"))
    coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
    benchmark_observations = json.loads(BENCHMARK_OBSERVATIONS.read_text(encoding="utf-8"))
    canonical_observations = json.loads(CANONICAL_OBSERVATIONS.read_text(encoding="utf-8"))

    if coverage.get("schema_version") != 1:
        fail("coverage schema_version must be 1")
    if coverage.get("function") != "S3*":
        fail("coverage function must be S3*")

    if not isinstance(benchmark_observations, list) or not benchmark_observations:
        fail("benchmark_observations.json must contain at least one composed direct observation")
    if not isinstance(canonical_observations, list):
        fail("canonical_observations.json must contain a list")

    direct_s3star = {
        entry["benchmark_id"]
        for entry in benchmark_map.get("entries", [])
        if entry.get("function") == "S3*" and entry.get("fit") == "direct"
    }
    if direct_s3star != DIRECT_S3STAR:
        fail(f"unexpected direct S3* benchmark map: {sorted(direct_s3star)}")

    if coverage.get("direct_benchmark_family_count") != len(direct_s3star):
        fail("direct_benchmark_family_count mismatch")
    if coverage.get("composed_direct_observation_count") != len(benchmark_observations):
        fail("composed_direct_observation_count mismatch")
    if coverage.get("canonical_direct_observation_count") != len(canonical_observations):
        fail("canonical_direct_observation_count mismatch")

    if len(canonical_observations) != 2:
        fail("expected exactly two canonical direct S3* observations")
    canonical_by_id = {obs.get("observation_id"): obs for obs in canonical_observations}
    expected_canonical_ids = {CANONICAL_OBSERVATION_ID, DATA_TO_PAPER_OBSERVATION_ID}
    if set(canonical_by_id) != expected_canonical_ids:
        fail(f"unexpected canonical S3* observation set: {sorted(canonical_by_id)}")
    validate_canonical_observation(canonical_by_id[CANONICAL_OBSERVATION_ID])
    validate_data_to_paper_observation(canonical_by_id[DATA_TO_PAPER_OBSERVATION_ID])

    declared_classes = set(coverage.get("coverage_classes", []))
    if declared_classes != COVERAGE_CLASSES:
        fail("coverage_classes vocabulary drift")

    observation_ids: set[str] = set()
    observations_by_id: dict[str, dict] = {}
    observed_families: set[str] = set()
    for obs in benchmark_observations:
        if obs.get("function") != "S3*":
            fail("benchmark observation function must be S3*")
        benchmark_id = obs.get("benchmark_id")
        if benchmark_id not in direct_s3star:
            fail("benchmark observation does not use a reviewed direct S3* family")
        observed_families.add(benchmark_id)
        if obs.get("benchmark_fit") != "direct":
            fail("composed benchmark observation must remain direct")
        if obs.get("boundary_class") != "composed-system":
            fail("direct benchmark observation must preserve composed-system boundary")
        if obs.get("canonical_harness_id") is not None:
            fail("composed benchmark observation must not claim canonical_harness_id")
        if obs.get("canonical_system_eligible") is not False:
            fail("composed benchmark observation must be ineligible for canonical registry")
        if obs.get("system_compatibility") != "benchmark-scaffolded":
            fail("composed benchmark observation must remain benchmark-scaffolded")
        observation_id = obs.get("observation_id")
        if not isinstance(observation_id, str) or not observation_id:
            fail("benchmark observation requires observation_id")
        if observation_id in observation_ids:
            fail(f"duplicate observation_id: {observation_id}")
        observation_ids.add(observation_id)
        observations_by_id[observation_id] = obs
        sources = obs.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{observation_id}: invalid primary_sources")
        interpretation = obs.get("vsm_interpretation")
        if not isinstance(interpretation, str) or len(interpretation.strip()) < 40:
            fail(f"{observation_id}: explicit VSM interpretation required")

    if observation_ids != EXPECTED_OBSERVATION_IDS:
        fail(f"unexpected composed S3* observation set: {sorted(observation_ids)}")
    if observed_families != COMPOSED_DIRECT_S3STAR:
        fail("composed S3* observations must cover exactly the reviewed composed direct families")

    truecall = observations_by_id["truecall-tau2-retail-silent-failure-2026-06"]
    if truecall.get("benchmark_id") != "truecall-runtime-verification":
        fail("TrueCall observation benchmark linkage drift")
    if truecall.get("reviewed_system_revision") != "3b1d8ce253ad6d9908936f844bf5e0255785e8b9":
        fail("TrueCall reviewed revision drift")
    if truecall.get("reported_detection_rate") != 1.0:
        fail("TrueCall reviewed published detection rate changed")
    if truecall.get("reported_false_positive_count") != 0:
        fail("TrueCall reviewed false-positive count changed")

    swe_review = observations_by_id["swe-review-generate-review-revise-2026-07"]
    if swe_review.get("benchmark_id") != "swe-review":
        fail("SWE-Review observation benchmark linkage drift")
    if swe_review.get("reviewed_system_revision") != "95b652e095e5ac8f16f08ae52fd3b26513c56097":
        fail("SWE-Review reviewed revision drift")
    if swe_review.get("benchmark_instances") != 1384:
        fail("SWE-Review benchmark instance count drift")
    if swe_review.get("source_issue_count") != 500 or swe_review.get("quality_tiers") != 3:
        fail("SWE-Review benchmark construction fields drift")
    if swe_review.get("reported_initial_resolve_rate_percent") != 27.5:
        fail("SWE-Review initial resolve-rate example drift")
    if swe_review.get("reported_iterative_resolve_rate_percent") != 56.9:
        fail("SWE-Review iterative resolve-rate example drift")
    if swe_review.get("reported_absolute_gain_percentage_points") != 29.4:
        fail("SWE-Review reported absolute gain drift")
    audit_loop = swe_review.get("audit_loop")
    if not isinstance(audit_loop, list) or len(audit_loop) < 5:
        fail("SWE-Review direct observation must preserve full review-revise-reverify loop")
    if "SWE-bench" not in str(swe_review.get("reverification_surface")):
        fail("SWE-Review observation must preserve independent SWE-bench re-verification")

    harness_bench = observations_by_id["harness-bench-pilot4-review-revise-reverify-2026-07"]
    if harness_bench.get("benchmark_id") != "harness-bench-adversarial-review":
        fail("harness-bench observation benchmark linkage drift")
    if harness_bench.get("reviewed_system_revision") != "f2fb12cc28ac90dce6eba873788b5632d6fc5431":
        fail("harness-bench reviewed revision drift")
    for field in (
        "reported_reviewed_runs",
        "reported_request_changes_runs",
        "reported_revision_runs",
        "post_revision_build_green_runs",
        "post_revision_visible_green_runs",
        "post_revision_holdout_pass_runs",
        "post_revision_success_runs",
    ):
        if harness_bench.get(field) != 2:
            fail(f"harness-bench Pilot 4 closure count drift: {field}")
    harness_loop = harness_bench.get("audit_loop")
    if not isinstance(harness_loop, list) or len(harness_loop) < 6:
        fail("harness-bench observation must preserve review-revise-reverify loop")
    if "held-out verification" not in " ".join(harness_loop):
        fail("harness-bench observation must preserve independent held-out re-verification")
    if "clean-room" not in str(harness_bench.get("publisher_boundary_note")):
        fail("harness-bench must preserve clean-room/non-Telos-native boundary")

    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("coverage cases must be non-empty")
    seen_cases: set[str] = set()
    by_id: dict[str, dict] = {}
    for case in cases:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            fail("case_id is required")
        if case_id in seen_cases:
            fail(f"duplicate case_id: {case_id}")
        seen_cases.add(case_id)
        by_id[case_id] = case

        coverage_class = case.get("coverage_class")
        if coverage_class not in COVERAGE_CLASSES:
            fail(f"{case_id}: invalid coverage_class")
        if case.get("system_compatibility") not in SYSTEM_COMPATIBILITY:
            fail(f"{case_id}: invalid system_compatibility")
        if coverage_class == "direct-native":
            if case.get("admitted_to_canonical_registry") is not True:
                fail(f"{case_id}: direct-native coverage must be admitted")
        elif case.get("admitted_to_canonical_registry") is not False:
            fail(f"{case_id}: non-direct-native coverage case must remain non-admitted")
        if not isinstance(case.get("finding"), str) or len(case["finding"].strip()) < 40:
            fail(f"{case_id}: explicit finding required")
        sources = case.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(s) for s in sources):
            fail(f"{case_id}: invalid primary_sources")

        harness_id = case.get("canonical_harness_id")
        if harness_id is not None:
            fields = assessment_fields(harness_id)
            if fields.get("status") != "included":
                fail(f"{case_id}: canonical assessment not included")
            if fields.get("autonomy_s3_star") in {None, "—", "?"}:
                fail(f"{case_id}: referenced canonical system no longer establishes S3*")

        if coverage_class == "candidate-native-no-direct-results":
            if harness_id is None:
                fail(f"{case_id}: native-no-results candidate requires canonical_harness_id")
            if case.get("system_compatibility") != "native-system":
                fail(f"{case_id}: native-no-results candidate must be native-system")
            if case.get("benchmark_fit") != "candidate-direct":
                fail(f"{case_id}: native-no-results candidate must retain candidate-direct fit")

    missing_cases = REQUIRED_CASE_IDS - seen_cases
    if missing_cases:
        fail(f"required S3* search cases missing: {sorted(missing_cases)}")

    for case_id in ("truecall-tau2-direct-composed", "swe-review-direct-composed", "harness-bench-adversarial-review-direct-composed"):
        case = by_id[case_id]
        if case.get("benchmark_fit") != "direct":
            fail(f"{case_id}: direct composed fit drift")
        if case.get("coverage_class") != "direct-composed":
            fail(f"{case_id}: direct composed coverage class drift")
        if case.get("system_compatibility") != "benchmark-scaffolded":
            fail(f"{case_id}: direct composed system compatibility drift")
        if case.get("canonical_harness_id") is not None:
            fail(f"{case_id}: direct composed evidence must not claim canonical harness ownership")

    direct_native = by_id["appliedscientist-native-s3star-direct"]
    if direct_native.get("benchmark_fit") != "direct":
        fail("AppliedScientist native S3* case must remain direct")
    if direct_native.get("coverage_class") != "direct-native":
        fail("AppliedScientist native S3* coverage class drift")
    if direct_native.get("system_compatibility") != "native-system":
        fail("AppliedScientist direct S3* case must remain native-system")
    if direct_native.get("canonical_harness_id") != CANONICAL_DIRECT_HARNESS:
        fail("AppliedScientist direct S3* canonical linkage drift")
    if direct_native.get("observation_ref") != f"canonical_observations.json#{CANONICAL_OBSERVATION_ID}":
        fail("AppliedScientist direct S3* observation_ref drift")

    pawbench = by_id["pawbench-self-verification-label-not-s3star"]
    if pawbench.get("coverage_class") != "capability-label-not-s3star":
        fail("PawBench Self_Verification negative-control class drift")
    if pawbench.get("canonical_harness_id") is not None:
        fail("PawBench capability-label negative control must not claim one canonical S3* owner")
    if pawbench.get("benchmark_fit") != "not-direct-S3star":
        fail("PawBench Self_Verification negative-control fit drift")

    silentprobe = by_id["silentprobe-self-monitoring-negative-control"]
    if silentprobe.get("coverage_class") != "proxy-scaffolded":
        fail("SilentProbe self-monitoring negative-control class drift")
    if silentprobe.get("benchmark_fit") != "not-direct-S3star":
        fail("SilentProbe must remain non-direct S3* evidence")
    if silentprobe.get("system_compatibility") != "benchmark-scaffolded":
        fail("SilentProbe must remain benchmark-scaffolded")
    if silentprobe.get("canonical_harness_id") is not None:
        fail("SilentProbe self-monitoring evidence must not claim canonical S3* ownership")

    expected_native_no_results = {
        "codex-guardian-native-no-direct-results": "codex",
        "omnigent-polly-reviewer-native-no-direct-results": "omnigent",
        "thclaws-team-audit-native-no-direct-results": "thclaws",
        "reigen-verification-native-no-direct-results": "reigen",
        "redteam-adversarial-review-native-no-direct-results": "redteam",
    }
    for case_id, harness_id in expected_native_no_results.items():
        case = by_id[case_id]
        if case.get("canonical_harness_id") != harness_id:
            fail(f"{case_id}: canonical linkage drift")

    representative = coverage.get("representative_canonical_s3star_systems_inspected")
    states = coverage.get("canonical_states_at_review")
    if not isinstance(representative, list) or not representative:
        fail("representative canonical S3* cohort is required")
    if len(representative) != len(set(representative)):
        fail("duplicate harness_id in representative cohort")
    if not isinstance(states, dict):
        fail("canonical_states_at_review must be an object")
    if set(states) != set(representative):
        fail("canonical_states_at_review keys must match representative cohort")

    for harness_id in representative:
        fields = assessment_fields(harness_id)
        if fields.get("status") != "included":
            fail(f"{harness_id}: assessment not included")
        current = fields.get("autonomy_s3_star")
        if current in {None, "—", "?"}:
            fail(f"{harness_id}: current canonical assessment does not establish S3*")
        if current != states[harness_id]:
            fail(f"{harness_id}: S3* state drifted from reviewed value {states[harness_id]!r} to {current!r}")

    print("ok: S3* benchmark coverage validated")
    print(f"reviewed direct S3* families: {len(direct_s3star)}")
    print(f"composed direct observations: {len(benchmark_observations)}")
    print(f"canonical direct observations: {len(canonical_observations)}")
    print(f"coverage cases: {len(cases)}")
    print(f"representative canonical S3* systems inspected: {len(representative)}")


if __name__ == "__main__":
    main()
