#!/usr/bin/env python3
"""Validate the refined paper-level controls for the public PolyBench matched-S4 preflight."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DATA = HERE / "public-polybench-paper-controls.json"
DOC = HERE / "PUBLIC-POLYBENCH-PAPER-CONTROLS.md"
PRIOR = HERE / "public-polybench-preflight.json"
PRIMARY_BASELINES = HERE.parents[1] / "primary-baselines.json"

EXPECTED_GATES = {
    "public-cross-method-comparison": "satisfied",
    "common-task-stream-order": "satisfied",
    "common-solver-evolver-model-policy": "satisfied",
    "common-result-surface": "satisfied",
    "native-baseline-implementation-provenance": "blocked",
    "immutable-upstream-revision-binding": "not_reached",
    "canonical-s4-linkage": "not_reached",
    "ordinary-s4-regulator-freeze": "not_reached",
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


def main() -> None:
    data = load_json(DATA)
    if not isinstance(data, dict):
        fail("paper-controls artifact must contain an object")
    if data.get("schema_version") != 1:
        fail("schema_version must be 1")
    if data.get("status") != "experimental-non-normative":
        fail("status must remain experimental-non-normative")
    if data.get("tracking_issue") != 538:
        fail("tracking_issue must remain #538")
    if data.get("refines_preflight") != "public-polybench-preflight.json":
        fail("refined artifact must point to the #534 preflight")
    if data.get("candidate_cell_id") != "adaptive-auto-harness-polybench-public-baselines-paper-controls-v2":
        fail("candidate_cell_id drift")
    if data.get("preflight_disposition") != "blocked":
        fail("refined preflight must remain blocked until implementation provenance is recovered")
    if data.get("execution_authorized") is not False:
        fail("blocked public-evidence preflight must not authorize execution")
    if data.get("primary_baseline_after_preflight") != "gap":
        fail("refined preflight must preserve S4 primary gap")
    if data.get("evidence_mode") != "public-results-only":
        fail("evidence_mode must remain public-results-only")
    if data.get("results") is not None:
        fail("refined preflight must not duplicate or invent result rows")

    # Historical #534 artifact must remain present and blocked rather than being rewritten.
    prior = load_json(PRIOR)
    if prior.get("tracking_issue") != 534 or prior.get("preflight_disposition") != "blocked":
        fail("historical #534 preflight was rewritten or lost")
    if prior.get("candidate_cell_id") != "adaptive-auto-harness-polybench-public-baselines-v1":
        fail("historical #534 candidate identity drift")

    paper = data.get("paper")
    if not isinstance(paper, dict):
        fail("paper object required")
    if paper.get("url") != "https://arxiv.org/abs/2606.01770":
        fail("paper binding drift")
    if paper.get("solver_model_policy") != "Claude Sonnet 4.6 for all experiments unless specified":
        fail("solver model policy drift")
    if paper.get("evolver_model_policy") != "Claude Opus 4.6":
        fail("evolver model policy drift")
    if paper.get("solver_temperature") != 0.0 or paper.get("evolver_temperature") != 0.0:
        fail("paper temperatures must remain zero")
    if paper.get("polybench_batch_size") != 100:
        fail("PolyBench batch size drift")
    for flag in ("common_batch_loop", "common_temporal_reveal_gate", "common_chronological_task_order", "native_tool_calling"):
        if paper.get(flag) is not True:
            fail(f"paper control {flag} must remain true")
    if paper.get("reported_results_source") != "corresponding results.jsonl files":
        fail("paper results-source statement drift")

    release = data.get("release_provenance")
    if not isinstance(release, dict):
        fail("release_provenance object required")
    if release.get("public_mirror_revision") != "c1ea7d60c009519f5c037f7db9d47e97063bb353":
        fail("public mirror revision drift")
    if release.get("initial_public_release_revision") != "b5fcd95f61190e8158c01506fc73be576dfbc4f8":
        fail("initial release revision drift")
    if release.get("results_committed") is not False:
        fail("public release must remain recorded as excluding results")
    if release.get("comparison_implementations_shipped") is not False:
        fail("comparison implementations must remain recorded as unshipped")
    if release.get("gepa_dependency_spec") != "gepa>=0.1.0":
        fail("GEPA dependency evidence drift")
    for field in ("public_mirror_repository", "mirror_declared_canonical_lineage"):
        if not valid_https(release.get(field)):
            fail(f"{field}: valid HTTPS source required")

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
        fail("paper-control gate set drift")
    for gate_id, expected in EXPECTED_GATES.items():
        if gate_by_id[gate_id].get("status") != expected:
            fail(f"{gate_id}: expected status {expected}")

    blocker = gate_by_id["native-baseline-implementation-provenance"]
    if "not shipped" not in blocker["finding"]:
        fail("implementation provenance blocker lost released-code evidence")
    if "Do not promote" not in str(blocker.get("blocking_effect", "")):
        fail("implementation provenance blocker must explicitly forbid promotion")

    doc = DOC.read_text(encoding="utf-8") if DOC.exists() else ""
    for phrase in (
        "same tasks/models/schedule/metrics",
        "native baseline implementation/revision provenance: blocked",
        "execution authorized: no",
        "S4 primary baseline: gap",
        "gepa>=0.1.0",
    ):
        if phrase not in doc:
            fail(f"paper-controls document missing required statement: {phrase}")

    baselines = load_json(PRIMARY_BASELINES)
    s4 = baselines.get("functions", {}).get("S4", {}) if isinstance(baselines, dict) else {}
    if s4.get("status") != "gap":
        fail("refined public PolyBench preflight is valid only while S4 primary remains gap")

    non_claim = data.get("non_claim")
    if not isinstance(non_claim, str) or len(non_claim.strip()) < 140:
        fail("explicit refined non-claim required")

    print("ok: refined public PolyBench paper controls validated")
    print("paper-level model/task/schedule matching: satisfied")
    print("blocking gate: native-baseline-implementation-provenance")
    print("execution authorized: no")
    print("S4 primary baseline: gap")


if __name__ == "__main__":
    main()
