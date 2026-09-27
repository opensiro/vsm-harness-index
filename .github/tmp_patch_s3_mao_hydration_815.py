from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments/functional-capability-depth/s3-system-benchmarks/validate.py"
text = PATH.read_text(encoding="utf-8")

# MAO must enter validation as the physical derived row. validate_mao_observation
# checks projection minimality first, then hydrates the effective evidence view.
call_old = '''    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])\n'''
if call_old not in text:
    raise SystemExit("S3 MAO validation call anchor drift")

hydrate_old = '''    raw_harness = record.get("canonical_harness_id")\n    if effective.get("canonical_harness_id") != raw_harness:\n        fail(f"{oid}: canonical_harness_id raw/derived drift")\n    if raw_harness:\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    return effective\n'''
hydrate_new = '''    raw_harness = record.get("canonical_harness_id")\n    if effective.get("canonical_harness_id") != raw_harness:\n        fail(f"{oid}: canonical_harness_id raw/derived drift")\n    if raw_harness:\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    if oid == MAO_OBSERVATION_ID:\n        effective["benchmark_artifact_revision"] = record.get("canonical_review_ref")\n        if "comparison_class" not in effective and isinstance(raw.get("comparison_design"), str):\n            effective["comparison_class"] = raw["comparison_design"]\n    return effective\n'''
if hydrate_old not in text:
    raise SystemExit("S3 hydrate alias anchor drift")
text = text.replace(hydrate_old, hydrate_new, 1)

start_old = '''def validate_mao_observation(observation: dict) -> None:\n    if observation.get("observation_id") != MAO_OBSERVATION_ID:\n        fail("Multi-Agent Orchestration observation_id drift")\n'''
start_new = '''def validate_mao_observation(observation: dict) -> None:\n    if observation.get("observation_id") != MAO_OBSERVATION_ID:\n        fail("Multi-Agent Orchestration observation_id drift")\n    derived = observation\n    for key in (\n        "baseline_arm",\n        "supervisor_arm",\n        "reported_completion_gain_percentage_points",\n        "reported_routing_accuracy_gain_percentage_points",\n    ):\n        if key in derived:\n            fail(f"Multi-Agent Orchestration derived record duplicates neutral numeric payload: {key}")\n    observation = hydrate_s3_projection(derived)\n'''
if start_old not in text:
    raise SystemExit("S3 MAO validator start anchor drift")
text = text.replace(start_old, start_new, 1)

old_absence = '''    for key in (\n        "baseline_arm",\n        "supervisor_arm",\n        "reported_completion_gain_percentage_points",\n        "reported_routing_accuracy_gain_percentage_points",\n    ):\n        if key in observation:\n            fail(f"Multi-Agent Orchestration derived record duplicates neutral numeric payload: {key}")\n    raw = load_raw_observation("multi-agent-orchestration.json", MAO_OBSERVATION_ID)\n'''
new_absence = '''    raw = load_raw_observation("multi-agent-orchestration.json", MAO_OBSERVATION_ID)\n'''
if old_absence not in text:
    raise SystemExit("S3 MAO duplicate-payload check anchor drift")
text = text.replace(old_absence, new_absence, 1)

prov_old = '''    limitation = observation.get("provenance_limitation")\n    if not isinstance(limitation, str) or MAO_UNRESOLVED_RUN_SHA not in limitation:\n        fail("Multi-Agent Orchestration provenance limitation lost unresolved SHA")\n    if "not relabeled as an independently reproduced run" not in limitation:\n        fail("Multi-Agent Orchestration non-reproduction boundary lost")\n'''
prov_new = '''    limitation = observation.get("provenance_limitation")\n    if not isinstance(limitation, str) or "no longer resolves publicly" not in limitation:\n        fail("Multi-Agent Orchestration provenance limitation lost unresolved-run boundary")\n    if "committed result artifact" not in limitation or "canonical review revision" not in limitation:\n        fail("Multi-Agent Orchestration provenance anchor boundary lost")\n    raw_record = json.loads((RAW_OBSERVATIONS / "multi-agent-orchestration.json").read_text(encoding="utf-8"))\n    implementation_note = (raw_record.get("published_implementation") or {}).get("note")\n    if not isinstance(implementation_note, str) or "not relabeled as an independently reproduced" not in implementation_note:\n        fail("Multi-Agent Orchestration non-reproduction boundary lost")\n'''
if prov_old not in text:
    raise SystemExit("S3 MAO provenance validation anchor drift")
text = text.replace(prov_old, prov_new, 1)

PATH.write_text(text, encoding="utf-8")
print("patched MAO S3 validation: check derived minimality first, then hydrate neutral evidence")
