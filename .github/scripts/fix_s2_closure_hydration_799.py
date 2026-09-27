from pathlib import Path

path = Path('experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/validate_s2_primary_search_closure.py')
text = path.read_text(encoding='utf-8')

anchor = 'ROOT = EXPERIMENT.parents[1]\n'
assert anchor in text
text = text.replace(anchor, anchor + 'SYSTEM_OBSERVATIONS = EXPERIMENT / "system-observations"\n', 1)

helper_anchor = '\ndef assessment_fields(harness_id: str) -> dict[str, str]:\n'
assert helper_anchor in text
helper = '''\ndef hydrate_raw_observation(row: dict) -> dict:\n    ref = row.get("raw_observation_ref")\n    if ref is None:\n        return row\n    require(isinstance(ref, str) and ref.startswith("../system-observations/") and "#" in ref, f"{row.get('observation_id')}: invalid raw observation ref")\n    path_part, raw_id = ref.split("#", 1)\n    raw_path = (S2 / path_part).resolve()\n    require(raw_path.parent == SYSTEM_OBSERVATIONS.resolve() and raw_path.is_file(), f"{row.get('observation_id')}: raw observation missing")\n    record = load(raw_path)\n    matches = [candidate for candidate in record.get("observations", []) if candidate.get("observation_id") == raw_id]\n    require(len(matches) == 1 and raw_id == row.get("observation_id"), f"{row.get('observation_id')}: raw observation identity drift")\n    hydrated = dict(matches[0])\n    hydrated.update(row)\n    return hydrated\n\n\ndef assessment_fields(harness_id: str) -> dict[str, str]:\n'''
text = text.replace(helper_anchor, helper, 1)

old = 'observations = load(S2 / "observations.json")\n'
assert old in text
text = text.replace(old, old + 'observations = [hydrate_raw_observation(row) for row in observations]\n', 1)
path.write_text(text, encoding='utf-8')
