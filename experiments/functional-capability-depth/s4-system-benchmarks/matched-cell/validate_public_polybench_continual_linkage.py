#!/usr/bin/env python3
"""Validate canonical Continual Harness linkage for the public PolyBench S4 preflight."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DATA = HERE / "public-polybench-continual-linkage.json"
DOC = HERE / "PUBLIC-POLYBENCH-CONTINUAL-LINKAGE.md"
PRIOR = HERE / "public-polybench-paper-controls.json"
ASSESSMENT = ROOT / "assessments" / "continual-harness.md"
CATALOG = ROOT / "data" / "catalog.psv"
PRIMARY_BASELINES = HERE.parents[1] / "primary-baselines.json"

EXPECTED_GATES = {
    "paper-level-comparison-controls": "satisfied",
    "canonical-continual-system-identity": "satisfied",
    "canonical-continual-s4-ownership": "satisfied",
    "evaluated-row-implementation-binding": "blocked",
    "immutable-evaluated-revision-binding": "not_reached",
    "native-s4-path-in-evaluated-row": "not_reached",
    "matched-canonical-s4-cell": "not_reached",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")


def valid_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def main() -> None:
    data = load_json(DATA)
    if not isinstance(data, dict):
        fail("linkage artifact must contain an object")
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if data.get("status") != "experimental-non-normative":
        fail("status must remain experimental-non-normative")
    if data.get("tracking_issue") != 547:
        fail("tracking_issue must remain #547")
    if data.get("refines_preflight") != "public-polybench-paper-controls.json":
        fail("v3 artifact must refine the #538 paper-controls artifact")
    if data.get("candidate_cell_id") != "adaptive-auto-harness-polybench-continual-harness-linkage-v3":
        fail("candidate_cell_id drift")
    if data.get("preflight_disposition") != "blocked":
        fail("linkage preflight must remain blocked until evaluated implementation binding is recovered")
    if data.get("execution_authorized") is not False:
        fail("public-evidence linkage preflight must not authorize execution")
    if data.get("primary_baseline_after_preflight") != "gap":
        fail("linkage preflight must preserve S4 primary gap")
    if data.get("evidence_mode") != "public-results-only":
        fail("evidence_mode must remain public-results-only")
    if data.get("results") is not None:
        fail("linkage preflight must not invent or duplicate result rows")

    prior = load_json(PRIOR)
    if prior.get("tracking_issue") != 538 or prior.get("preflight_disposition") != "blocked":
        fail("historical #538 paper-controls artifact was rewritten or lost")
    if prior.get("candidate_cell_id") != "adaptive-auto-harness-polybench-public-baselines-paper-controls-v2":
        fail("historical #538 candidate identity drift")

    paper_row = data.get("paper_row")
    if not isinstance(paper_row, dict):
        fail("paper_row object required")
    if paper_row.get("paper") != "https://arxiv.org/abs/2606.01770":
        fail("paper binding drift")
    if paper_row.get("reported_method_label") != "Continual Harness":
        fail("reported method label drift")
    if paper_row.get("benchmark") != "PolyBench":
        fail("benchmark binding drift")
    if paper_row.get("paper_level_solver_policy") != "Claude Sonnet 4.6 for all experiments unless specified":
        fail("solver policy drift")
    if paper_row.get("paper_level_evolver_policy") != "Claude Opus 4.6":
        fail("evolver policy drift")
    if paper_row.get("paper_level_solver_temperature") != 0.0 or paper_row.get("paper_level_evolver_temperature") != 0.0:
        fail("paper temperatures must remain zero")
    if paper_row.get("paper_level_polybench_batch_size") != 100:
        fail("PolyBench batch size drift")
    for flag in ("paper_level_common_chronological_order", "paper_level_common_temporal_reveal"):
        if paper_row.get(flag) is not True:
            fail(f"paper control {flag} must remain true")

    candidate = data.get("canonical_candidate")
    if not isinstance(candidate, dict):
        fail("canonical_candidate object required")
    expected_candidate = {
        "harness_id": "continual-harness",
        "repository": "https://github.com/sethkarten/continual-harness",
        "assessment_ref": "assessments/continual-harness.md",
        "review_revision": "bbab97ad73e460b7cd7c08527d10ced30cc03fbe",
        "status": "included",
        "s4_state": "A",
        "catalog_position": 235,
    }
    for key, expected in expected_candidate.items():
        if candidate.get(key) != expected:
            fail(f"canonical candidate {key} drift")

    assessment_text = ASSESSMENT.read_text(encoding="utf-8")
    expected_frontmatter = {
        "harness_id": "continual-harness",
        "repository": "https://github.com/sethkarten/continual-harness",
        "review_ref": "bbab97ad73e460b7cd7c08527d10ced30cc03fbe",
        "status": "included",
        "autonomy_s4": "A",
    }
    for key, expected in expected_frontmatter.items():
        if frontmatter_value(assessment_text, key) != expected:
            fail(f"canonical assessment {key} no longer matches linkage record")

    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="|"))
    matches = [row for row in rows if row.get("harness_id") == "continual-harness"]
    if len(matches) != 1:
        fail("catalog must contain exactly one continual-harness row")
    row = matches[0]
    if row.get("catalog_position") != "235":
        fail("continual-harness catalog position drift")
    if row.get("review_ref") != "bbab97ad73e460b7cd7c08527d10ced30cc03fbe":
        fail("continual-harness catalog review_ref drift")

    provenance = data.get("provenance_search")
    if not isinstance(provenance, dict):
        fail("provenance_search object required")
    if provenance.get("adaptive_harness_public_mirror_revision") != "c1ea7d60c009519f5c037f7db9d47e97063bb353":
        fail("AdaptiveHarness mirror revision drift")
    if provenance.get("a_evolve_public_pr_revision") != "e4f70b949989e0abf08532e8223cb9eab447e971":
        fail("A-Evolve inspected pre-release revision drift")
    for flag in (
        "continual_upstream_polybench_reference_found",
        "continual_upstream_adaptive_auto_harness_reference_found",
        "continual_upstream_a_evolve_reference_found",
        "continual_baseline_path_found_in_inspected_a_evolve_pr_tree",
        "comparison_result_artifacts_committed_in_public_release",
    ):
        if provenance.get(flag) is not False:
            fail(f"{flag} must remain false until new primary evidence is explicitly reviewed")

    gates = data.get("gates")
    if not isinstance(gates, list):
        fail("gates must be a list")
    gate_by_id: dict[str, dict] = {}
    for gate in gates:
        if not isinstance(gate, dict):
            fail("gate entries must be objects")
        gate_id = gate.get("gate_id")
        if not isinstance(gate_id, str) or not gate_id:
            fail("gate_id required")
        if gate_id in gate_by_id:
            fail(f"duplicate gate_id: {gate_id}")
        gate_by_id[gate_id] = gate
        finding = gate.get("finding")
        if not isinstance(finding, str) or len(finding.strip()) < 60:
            fail(f"{gate_id}: substantive finding required")
        sources = gate.get("primary_sources")
        if not isinstance(sources, list) or not sources or any(not valid_https(source) for source in sources):
            fail(f"{gate_id}: valid HTTPS primary_sources required")
    if set(gate_by_id) != set(EXPECTED_GATES):
        fail("linkage gate set drift")
    for gate_id, expected in EXPECTED_GATES.items():
        if gate_by_id[gate_id].get("status") != expected:
            fail(f"{gate_id}: expected status {expected}")

    blocker = gate_by_id["evaluated-row-implementation-binding"]
    if "Do not admit" not in str(blocker.get("blocking_effect", "")):
        fail("row-binding blocker must explicitly forbid canonical capability admission")

    doc = DOC.read_text(encoding="utf-8") if DOC.exists() else ""
    for phrase in (
        "canonical Continual Harness identity: satisfied",
        "canonical Continual Harness S4 ownership: satisfied",
        "row -> implementation/revision binding: blocked",
        "matched canonical S4 cell: not admitted",
        "S4 primary baseline: gap",
    ):
        if phrase not in doc:
            fail(f"linkage document missing required statement: {phrase}")

    baselines = load_json(PRIMARY_BASELINES)
    s4 = baselines.get("functions", {}).get("S4", {}) if isinstance(baselines, dict) else {}
    if s4.get("status") != "gap":
        fail("Continual Harness linkage preflight is valid only while S4 primary remains gap")

    non_claim = data.get("non_claim")
    if not isinstance(non_claim, str) or len(non_claim.strip()) < 180:
        fail("explicit linkage non-claim required")

    print("ok: canonical Continual Harness PolyBench linkage preflight validated")
    print("paper-level matching: satisfied")
    print("canonical Continual Harness S4 identity: satisfied")
    print("blocking gate: evaluated-row-implementation-binding")
    print("matched canonical S4 cell: not admitted")
    print("S4 primary baseline: gap")


if __name__ == "__main__":
    main()
