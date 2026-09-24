#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('experiments/functional-capability-depth')
S3 = ROOT / 's3star-system-benchmarks'
REVIEW_REF = '762824fd41598370e75588861b48991b0a9fd784'
BENCHMARK_ID = 'appliedscientist-iterative-review'
OBSERVATION_ID = 'appliedscientist-iterative-review-2026-09'
CASE_ID = 'appliedscientist-native-s3star-direct'


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


# Direct-family map.
map_path = ROOT / 'vsm-benchmark-family-map' / 'map.json'
benchmark_map = json.loads(map_path.read_text())
if not any(e.get('benchmark_id') == BENCHMARK_ID for e in benchmark_map['entries']):
    entry = {
        'function': 'S3*',
        'benchmark_id': BENCHMARK_ID,
        'benchmark_name': 'AppliedScientist iterative scientific review-revision',
        'fit': 'direct',
        'primary_source': 'https://arxiv.org/abs/2609.14738',
        'evaluated_object': 'canonical AppliedScientist scientific-revision system in which a separate fresh reviewer independently audits each manuscript, returns feedback into Scientist code/experiment/manuscript revision, and reviews the subsequent revision again',
        'evaluation_mode': 'execution-grounded-research',
        'system_linkage': 'native-canonical-observation',
        'non_claim': 'This is a first-party-reported within-system canonical S3* observation; it is not an independently reproduced run at the pinned Git revision and does not create a matched cross-harness S3* primary baseline.',
    }
    insert_at = next(i for i, e in enumerate(benchmark_map['entries']) if e.get('function') == 'S4')
    benchmark_map['entries'].insert(insert_at, entry)
write_json(map_path, benchmark_map)

# First canonical direct S3* observation.
obs_path = S3 / 'canonical_observations.json'
observations = json.loads(obs_path.read_text())
other = [o for o in observations if o.get('observation_id') != OBSERVATION_ID]
if other:
    raise SystemExit(f'unexpected pre-existing canonical S3* observations: {other!r}')
if not observations:
    observations = [{
        'observation_id': OBSERVATION_ID,
        'function': 'S3*',
        'benchmark_id': BENCHMARK_ID,
        'benchmark_fit': 'direct',
        'evidence_source_class': 'first-party-reported',
        'boundary_class': 'canonical-native-system',
        'canonical_harness_id': 'appliedscientist',
        'canonical_system_eligible': True,
        'system_compatibility': 'native-system',
        'canonical_review_revision': REVIEW_REF,
        'publication_id': 'arXiv:2609.14738',
        'publication_version_at_review': 'v2',
        'paper_count': 30,
        'rejected_paper_count': 25,
        'borderline_paper_count': 5,
        'revision_rounds': 5,
        'comparison_class': 'within-system-guidance-comparison',
        'revision_conditions': [
            'human-initialized reviewer-guided revision',
            'AI-initialized reviewer-guided revision',
            'autonomous fixed-prompt self-revision',
        ],
        'audit_loop': [
            'Scientist produces a revised implementation, experiments and manuscript',
            'a separate fresh Reviewer sees only the current manuscript and independently searches literature',
            'Reviewer emits weaknesses, suggestions and a new evaluation without memory of prior feedback or scores',
            'review feedback becomes guidance for the next Scientist revision',
            'Scientist edits code, runs experiments, analyzes results and revises the manuscript',
            'the new manuscript is submitted to another fresh independent review',
        ],
        'reported_execution_weaknesses_total': 150,
        'reported_execution_weaknesses_resolved': 128,
        'reported_execution_weakness_resolution_rate': 0.853,
        'reported_idea_weaknesses_total': 18,
        'reported_idea_weaknesses_resolved': 2,
        'reported_idea_weakness_resolution_rate': 0.111,
        'external_validation_surface': 'Stanford Reviewer scores saved human-initialized versions independently and is never shown to the Scientist; it is supporting validation, not the native S3* owner.',
        'comparison_scope_note': 'The paper compares reviewer-guided revision with fixed-prompt self-revision inside AppliedScientist. The weakness-resolution counts are aggregate closure evidence for the native review-guided loop, not a matched cross-harness S3* score.',
        'provenance_limitation': f'The public AppliedScientist repository at canonical review ref {REVIEW_REF} is first-party and implements the same Scientist-to-separate-Reviewer-to-correction-to-fresh-review architecture described in the publication. The fetched publication HTML does not expose an explicit repository URL binding the reported experimental runs to that exact Git commit. Preserve this result as first-party-reported; it is not independently reproduced at the pinned revision.',
        'vsm_interpretation': 'The canonical assessment independently establishes S3*=A for AppliedScientist. The publication directly exercises that native complementary-audit organization: a separate fresh reviewer gathers independent evidence, returns concrete findings into the Scientist current revision loop, and the corrected artifact is reviewed again. The result is therefore direct native S3* capability evidence, while one within-system result remains insufficient for a matched cross-harness primary baseline.',
        'primary_sources': [
            'https://arxiv.org/abs/2609.14738',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-scientist/.claude/CLAUDE.md',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-scientist/scripts/submit_for_review.sh',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-reviewer/review_api.py',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-reviewer/prompts/paper_reviewer_instruction_template.md',
        ],
    }]
write_json(obs_path, observations)

# Coverage case and canonical cohort.
cov_path = S3 / 'coverage.json'
coverage = json.loads(cov_path.read_text())
if coverage.get('composed_direct_observation_count') != 3:
    raise SystemExit('unexpected composed S3* observation count')
coverage['direct_benchmark_family_count'] = 4
coverage['canonical_direct_observation_count'] = 1
if 'direct-native' not in coverage['coverage_classes']:
    coverage['coverage_classes'].insert(1, 'direct-native')
if not any(c.get('case_id') == CASE_ID for c in coverage['cases']):
    coverage['cases'].append({
        'case_id': CASE_ID,
        'benchmark': 'AppliedScientist iterative scientific review-revision',
        'benchmark_fit': 'direct',
        'coverage_class': 'direct-native',
        'system_compatibility': 'native-system',
        'canonical_harness_id': 'appliedscientist',
        'observation_ref': f'canonical_observations.json#{OBSERVATION_ID}',
        'primary_sources': [
            'https://arxiv.org/abs/2609.14738',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-scientist/.claude/CLAUDE.md',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-scientist/scripts/submit_for_review.sh',
            f'https://github.com/TheAppliedScientist/TheAppliedScientist/blob/{REVIEW_REF}/components/ai-reviewer/review_api.py',
        ],
        'finding': 'Canonical AppliedScientist establishes S3*=A through its separate fresh Reviewer service and Scientist correction/re-review loop. The first-party publication directly evaluates this organization over 30 scientific-revision trajectories and reports 128/150 execution-related weaknesses resolved (85.3%) while only 2/18 idea-related weaknesses are resolved (11.1%). This is admitted native direct S3* evidence; the result is first-party-reported rather than independently reproduced at the pinned Git revision and does not supply a matched cross-harness primary cell.',
        'admitted_to_canonical_registry': True,
    })
if 'appliedscientist' not in coverage['representative_canonical_s3star_systems_inspected']:
    coverage['representative_canonical_s3star_systems_inspected'].append('appliedscientist')
coverage['canonical_states_at_review']['appliedscientist'] = 'A'
write_json(cov_path, coverage)

# Primary baseline remains a gap; only reviewed evidence expands.
prim_path = ROOT / 'primary-baselines.json'
primary = json.loads(prim_path.read_text())
s3p = primary['functions']['S3*']
if s3p.get('status') != 'gap':
    raise SystemExit('S3* primary status unexpectedly not gap')
if not any(f.get('benchmark_id') == BENCHMARK_ID for f in s3p['reviewed_direct_families']):
    s3p['reviewed_direct_families'].append({
        'benchmark_id': BENCHMARK_ID,
        'benchmark_name': 'AppliedScientist iterative scientific review-revision',
        'primary_source': 'https://arxiv.org/abs/2609.14738',
    })
s3p['blocking_reason'] = 'Reviewed direct S3* families now include a canonical native within-system observation from AppliedScientist in addition to composed/benchmark-defined review-correction-reverification evidence, but public evidence still does not provide a matched comparison of native S3* implementations across multiple canonical harnesses under one common benchmark/model/configuration cell.'
write_json(prim_path, primary)

# Fail-closed validator.
val_path = S3 / 'validate.py'
text = val_path.read_text()
old = 'DIRECT_S3STAR = {"truecall-runtime-verification", "swe-review", "harness-bench-adversarial-review"}'
new = 'COMPOSED_DIRECT_S3STAR = {"truecall-runtime-verification", "swe-review", "harness-bench-adversarial-review"}\nDIRECT_S3STAR = COMPOSED_DIRECT_S3STAR | {"appliedscientist-iterative-review"}'
if old in text:
    text = text.replace(old, new, 1)
elif 'COMPOSED_DIRECT_S3STAR' not in text:
    raise SystemExit('direct-family validator anchor missing')

if 'CANONICAL_OBSERVATION_ID' not in text:
    anchor = 'COVERAGE_CLASSES = {\n'
    block = f'CANONICAL_OBSERVATION_ID = "{OBSERVATION_ID}"\nCANONICAL_DIRECT_HARNESS = "appliedscientist"\nCANONICAL_REVIEW_REF = "{REVIEW_REF}"\n\n'
    text = text.replace(anchor, block + anchor, 1)
if '    "direct-native",\n' not in text:
    text = text.replace('    "direct-composed",\n', '    "direct-composed",\n    "direct-native",\n', 1)
if f'    "{CASE_ID}",\n' not in text:
    text = text.replace('    "redteam-adversarial-review-native-no-direct-results",\n', f'    "redteam-adversarial-review-native-no-direct-results",\n    "{CASE_ID}",\n', 1)

helper = '''def validate_canonical_observation(observation: dict) -> None:
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

'''
if 'def validate_canonical_observation' not in text:
    text = text.replace('def main() -> None:\n', helper + 'def main() -> None:\n', 1)

old_empty = '    if canonical_observations:\n        fail("canonical direct S3* observation registry is expected to remain empty")\n'
new_obs = '    if len(canonical_observations) != 1:\n        fail("expected exactly one canonical direct S3* observation")\n    validate_canonical_observation(canonical_observations[0])\n'
if old_empty in text:
    text = text.replace(old_empty, new_obs, 1)
elif 'expected exactly one canonical direct S3* observation' not in text:
    raise SystemExit('canonical observation validator anchor missing')

old_families = '    if observed_families != DIRECT_S3STAR:\n        fail("composed S3* observations must cover every reviewed direct family")\n'
new_families = '    if observed_families != COMPOSED_DIRECT_S3STAR:\n        fail("composed S3* observations must cover exactly the reviewed composed direct families")\n'
if old_families in text:
    text = text.replace(old_families, new_families, 1)

old_admit = '        if case.get("admitted_to_canonical_registry") is not False:\n            fail(f"{case_id}: coverage case must remain non-admitted")\n'
new_admit = '        if coverage_class == "direct-native":\n            if case.get("admitted_to_canonical_registry") is not True:\n                fail(f"{case_id}: direct-native coverage must be admitted")\n        elif case.get("admitted_to_canonical_registry") is not False:\n            fail(f"{case_id}: non-direct-native coverage case must remain non-admitted")\n'
if old_admit in text:
    text = text.replace(old_admit, new_admit, 1)
elif 'direct-native coverage must be admitted' not in text:
    raise SystemExit('coverage admission validator anchor missing')

anchor = '    pawbench = by_id["pawbench-self-verification-label-not-s3star"]\n'
direct_check = '''    direct_native = by_id["appliedscientist-native-s3star-direct"]
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

'''
if 'AppliedScientist native S3* case must remain direct' not in text:
    text = text.replace(anchor, direct_check + anchor, 1)

val_path.write_text(text)
