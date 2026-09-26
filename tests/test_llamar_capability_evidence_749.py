import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
REVIEW_REF = "d2b74cac79a0f070d87a150712f8e2ae174920be"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError(f"missing front matter: {path}")
    out = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


def contains_canonical_id(value, harness_id: str) -> bool:
    if isinstance(value, dict):
        if value.get("canonical_harness_id") == harness_id:
            return True
        return any(contains_canonical_id(v, harness_id) for v in value.values())
    if isinstance(value, list):
        return any(contains_canonical_id(v, harness_id) for v in value)
    return False


class LLaMARCapabilityEvidence749Test(unittest.TestCase):
    def test_canonical_anchor_and_public_evidence_classification(self):
        assessment = frontmatter(ROOT / "assessments" / "llamar.md")
        self.assertEqual(assessment.get("status"), "included")
        self.assertEqual(assessment.get("review_ref"), REVIEW_REF)
        self.assertEqual(assessment.get("autonomy_s2"), "A")
        self.assertEqual(assessment.get("autonomy_s3"), "A")
        self.assertEqual(assessment.get("autonomy_s3_star"), "—")
        self.assertEqual(assessment.get("autonomy_s4"), "—")
        self.assertEqual(assessment.get("autonomy_s5"), "—")

        raw = load(EXP / "system-observations" / "llamar.json")
        self.assertEqual(raw.get("canonical_harness_id"), "llamar")
        self.assertEqual(raw.get("canonical_review_ref"), REVIEW_REF)
        self.assertEqual(raw.get("canonical_states_at_review"), {"S2": "A", "S3": "A"})
        relation = raw["published_implementation"]["canonical_revision_match"]
        self.assertEqual(
            relation,
            "first-party-published-artifacts-co-located-at-current-review-ref-run-revision-unknown",
        )

        observations = {row["observation_id"]: row for row in raw["observations"]}
        self.assertEqual(
            set(observations),
            {
                "llamar-mapthor-module-ablation-gpt4v",
                "llamar-agent-count-interference-mapthor-sar",
            },
        )

        ablation = observations["llamar-mapthor-module-ablation-gpt4v"]
        self.assertEqual(ablation.get("kind"), "native-mechanism-ablation")
        self.assertEqual(ablation.get("benchmark"), "MAP-THOR")
        self.assertEqual(ablation.get("model"), "GPT-4V")
        self.assertEqual(
            ablation.get("arms"),
            [
                {"modules": ["Actor"], "success_rate": 0.33, "transport_rate": 0.67, "coverage": 0.91, "balance": 0.59},
                {"modules": ["Planner", "Actor", "Verifier"], "success_rate": 0.45, "transport_rate": 0.78, "coverage": 0.92, "balance": 0.69},
                {"modules": ["Planner", "Actor", "Corrector"], "success_rate": 0.67, "transport_rate": 0.91, "coverage": 0.97, "balance": 0.84},
                {"modules": ["Planner", "Actor", "Corrector", "Verifier"], "success_rate": 0.66, "transport_rate": 0.91, "coverage": 0.97, "balance": 0.82},
            ],
        )
        self.assertIn("proxy evidence", ablation.get("non_claim", ""))
        self.assertIn("do not isolate a pure S3", ablation.get("non_claim", ""))

        disturbance = observations["llamar-agent-count-interference-mapthor-sar"]
        self.assertEqual(disturbance.get("kind"), "native-disturbance-characterization")
        mapthor = {row["agents"]: row for row in disturbance["mapthor"]}
        self.assertEqual(mapthor[3]["success_rate"], 0.70)
        self.assertEqual(mapthor[4]["success_rate"], 0.68)
        self.assertEqual(mapthor[5]["success_rate"], 0.62)
        self.assertIn("block", disturbance.get("reported_disturbance", ""))
        self.assertIn("not an S2 attenuation treatment", disturbance.get("non_claim", ""))

    def test_s2_remains_non_admitted(self):
        delta = load(
            EXP
            / "s2-system-benchmarks"
            / "post-closure-deltas"
            / "llamar-2026-09-26.json"
        )
        self.assertEqual(delta.get("tracking_issue"), 749)
        self.assertEqual(delta.get("canonical_harness_id"), "llamar")
        self.assertEqual(delta.get("canonical_state_at_review"), "A")
        self.assertEqual(delta.get("canonical_review_ref"), REVIEW_REF)
        self.assertEqual(delta.get("result_surface_review"), "no-direct-s2-result")
        self.assertFalse(delta.get("capability_counts_changed"))
        self.assertFalse(delta.get("observation_registry_mutated"))
        self.assertFalse(delta.get("primary_baseline_changed"))
        self.assertFalse(delta.get("reopen_condition_satisfied"))

        s2_observations = load(EXP / "s2-system-benchmarks" / "observations.json")
        self.assertFalse(contains_canonical_id(s2_observations, "llamar"))
        s2_closure = load(
            EXP / "s2-system-benchmarks" / "matched-cell" / "s2-primary-search-closure.json"
        )
        self.assertEqual(s2_closure.get("primary_baseline"), "gap")
        self.assertEqual(s2_closure.get("disposition"), "evidence-backed-gap")

    def test_s3_is_proxy_only_and_primary_stays_gap(self):
        projections = load(EXP / "s3-system-benchmarks" / "proxy_links.json")
        rows = {row["projection_id"]: row for row in projections}
        self.assertIn("llamar-mapthor-native-proxy-s3", rows)
        projection = rows["llamar-mapthor-native-proxy-s3"]
        self.assertEqual(projection.get("canonical_harness_id"), "llamar")
        self.assertEqual(projection.get("canonical_state_at_review"), "A")
        self.assertEqual(projection.get("benchmark_fit"), "proxy")
        self.assertEqual(projection.get("system_compatibility"), "native-system")
        self.assertEqual(projection.get("raw_record"), "../system-observations/llamar.json")
        self.assertEqual(projection.get("raw_observation_ids"), ["llamar-mapthor-module-ablation-gpt4v"])
        self.assertIn("does not create a matched S3 primary baseline", projection.get("non_claim", ""))

        coverage = load(EXP / "s3-system-benchmarks" / "coverage.json")
        self.assertEqual(coverage.get("proxy_projection_count"), 2)
        cases = {row["case_id"]: row for row in coverage["cases"]}
        case = cases["llamar-mapthor-native-proxy-s3"]
        self.assertEqual(case.get("benchmark_fit"), "proxy")
        self.assertEqual(case.get("coverage_class"), "native-proxy")
        self.assertEqual(case.get("canonical_harness_id"), "llamar")
        self.assertFalse(case.get("admitted"))
        self.assertIn("llamar", coverage.get("representative_canonical_s3_systems_inspected", []))

        direct_observations = load(EXP / "s3-system-benchmarks" / "observations.json")
        self.assertFalse(contains_canonical_id(direct_observations, "llamar"))
        s3_closure = load(
            EXP / "s3-system-benchmarks" / "matched-cell" / "s3-primary-search-closure.json"
        )
        self.assertEqual(s3_closure.get("primary_baseline"), "gap")
        self.assertEqual(s3_closure.get("disposition"), "evidence-backed-gap")


if __name__ == "__main__":
    unittest.main()
