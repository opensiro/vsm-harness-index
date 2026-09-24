#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('experiments/functional-capability-depth')
S3 = ROOT / 's3star-system-benchmarks'
REVIEW_REF = '81df14c4b9600466e645c3b2b336cc54daa3df3a'
BENCHMARK_ID = 'data-to-paper-review-revision'
OBSERVATION_ID = 'data-to-paper-review-revision-2024'
CASE_ID = 'data-to-paper-native-s3star-direct'
PUBLICATION = 'https://doi.org/10.1056/AIoa2400555'


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


# Keep the compact one-line benchmark map format and insert one family only.
map_path = ROOT / 'vsm-benchmark-family-map' / 'map.json'
map_text = map_path.read_text()
if BENCHMARK_ID not in map_text:
    anchor = '    {"function":"S4","benchmark_id":"a-evolve-harness-evolution"'
    if anchor not in map_text:
        raise SystemExit('S4 insertion anchor missing')
    entry = ('    {"function":"S3*","benchmark_id":"data-to-paper-review-revision",'
             '"benchmark_name":"data-to-paper native reviewer-revision case study",'
             '"fit":"direct","primary_source":"https://doi.org/10.1056/AIoa2400555",'
             '"evaluated_object":"canonical data-to-paper research-step organization in which a separate role-inverted reviewer conversation challenges a performer product, returns feedback to that performer, and the revised product must pass review before the step concludes",'
             '"evaluation_mode":"published-run-case-study","system_linkage":"native-canonical-observation",'
             '"non_claim":"This first-party publication supplies a direct descriptive native S3* closure witness, not an aggregate S3* score, independent reproduction, or a matched cross-harness primary baseline."},\n')
    map_text = map_text.replace(anchor, entry + anchor, 1)
    map_path.write_text(map_text)

# Add the second canonical native observation. Do not invent a score.
obs_path = S3 / 'canonical_observations.json'
observations = json.loads(obs_path.read_text())
if not any(o.get('observation_id') == OBSERVATION_ID for o in observations):
    observations.append({
        'observation_id': OBSERVATION_ID,
        'function': 'S3*',
        'benchmark_id': BENCHMARK_ID,
        'benchmark_fit': 'direct',
        'evidence_source_class': 'first-party-reported',
        'boundary_class': 'canonical-native-system',
        'canonical_harness_id': 'data-to-paper',
        'canonical_system_eligible': True,
        'system_compatibility': 'native-system',
        'canonical_review_revision': REVIEW_REF,
        'publication_id': 'DOI:10.1056/AIoa2400555',
        'publication_date': '2024-12-03',
        'comparison_class': 'descriptive-only',
        'published_example_count': 1,
        'published_example_reference': 'Figure 2B / Supplementary Run A5',
        'aggregate_s3star_metric_reported': False,
        'metric_note': 'The publication demonstrates native reviewer-feedback-to-revision closure but does not report an aggregate S3*-specific detection, correction, or re-verification score for this loop.',
        'audit_loop': [
            'the performer conversation creates a current research product',
            'a separate role-inverted Reviewer conversation receives the product and relevant prior research context',
            'Reviewer emits concrete feedback on the candidate product',
            'the feedback is transferred back into the performer conversation as corrective input',
            'the performer revises the product according to the reviewer findings',
            'the research step concludes only after the product passes rule-based and LLM review, so rejected products remain in the correction/review loop'
        ],
        'published_result_summary': 'The first-party paper Figure 2B, drawn from Supplementary Run A5, shows reviewer comments on a Discussion draft being returned to the performer and producing a corrected revised response. The Methods state that products must pass LLM review before the research step concludes.',
        'comparison_scope_note': 'This is a direct descriptive within-system closure witness. It is not a quantitative comparison with AppliedScientist or any other harness and must not be normalized into a common S3* score.',
        'provenance_limitation': f'The publication identifies the first-party data-to-paper project and codebase, and the canonical repository at review ref {REVIEW_REF} implements the same separate reviewer-to-performer correction loop. The publication does not bind Supplementary Run A5 to the exact canonical review revision. Preserve this as first-party-reported historical evidence; it is not independently reproduced at the pinned revision.',
        'vsm_interpretation': 'The canonical assessment independently establishes S3*=A for data-to-paper. The publication directly observes that native complementary-audit path in operation: a separate reviewer challenges a performer product, findings return to the producer, and the product is revised before review completion. This is direct native S3* capability evidence, but descriptive-only evidence under a different task/model/evaluator surface from AppliedScientist.',
        'primary_sources': [
            PUBLICATION,
            f'https://github.com/Technion-Kishony-lab/data-to-paper/blob/{REVIEW_REF}/src/data_to_paper/base_steps/dual_converser.py',
            f'https://github.com/Technion-Kishony-lab/data-to-paper/blob/{REVIEW_REF}/src/data_to_paper/base_steps/request_code.py',
            f'https://github.com/Technion-Kishony-lab/data-to-paper/blob/{REVIEW_REF}/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py'
        ]
    })
write_json(obs_path, observations)

# Coverage: second native direct system, composed evidence unchanged.
cov_path = S3 / 'coverage.json'
coverage = json.loads(cov_path.read_text())
if coverage.get('direct_benchmark_family_count') not in (4, 5):
    raise SystemExit('unexpected direct S3* family count')
if coverage.get('composed_direct_observation_count') != 3:
    raise SystemExit('unexpected composed S3* observation count')
if coverage.get('canonical_direct_observation_count') not in (1, 2):
    raise SystemExit('unexpected canonical S3* observation count')
coverage['direct_benchmark_family_count'] = 5
coverage['canonical_direct_observation_count'] = 2
if not any(c.get('case_id') == CASE_ID for c in coverage['cases']):
    coverage['cases'].append({
        'case_id': CASE_ID,
        'benchmark': 'data-to-paper native reviewer-revision case study',
        'benchmark_fit': 'direct',
        'coverage_class': 'direct-native',
        'system_compatibility': 'native-system',
        'canonical_harness_id': 'data-to-paper',
        'observation_ref': f'canonical_observations.json#{OBSERVATION_ID}',
        'primary_sources': [
            PUBLICATION,
            f'https://github.com/Technion-Kishony-lab/data-to-paper/blob/{REVIEW_REF}/src/data_to_paper/base_steps/dual_converser.py',
            f'https://github.com/Technion-Kishony-lab/data-to-paper/blob/{REVIEW_REF}/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py'
        ],
        'finding': 'Canonical data-to-paper establishes S3*=A through a separate reviewer conversation whose findings return to the performer for revision. The first-party publication Figure 2B / Supplementary Run A5 directly shows that reviewer-to-revision closure. The evidence is descriptive-only and reports no aggregate S3*-specific score, so it is admitted as a native direct observation without creating a matched primary cell.',
        'admitted_to_canonical_registry': True
    })
if 'data-to-paper' not in coverage['representative_canonical_s3star_systems_inspected']:
    coverage['representative_canonical_s3star_systems_inspected'].append('data-to-paper')
coverage['canonical_states_at_review']['data-to-paper'] = 'A'
write_json(cov_path, coverage)

# Primary-family inventory: evidence grows; primary remains gap.
prim_path = ROOT / 'primary-baselines.json'
primary = json.loads(prim_path.read_text())
s3p = primary['functions']['S3*']
if s3p.get('status') != 'gap':
    raise SystemExit('S3* primary unexpectedly selected')
if not any(f.get('benchmark_id') == BENCHMARK_ID for f in s3p['reviewed_direct_families']):
    s3p['reviewed_direct_families'].append({
        'benchmark_id': BENCHMARK_ID,
        'benchmark_name': 'data-to-paper native reviewer-revision case study',
        'primary_source': PUBLICATION
    })
s3p['blocking_reason'] = 'Reviewed direct S3* evidence now includes two canonical native systems: AppliedScientist provides quantitative within-system weakness-closure measurements, while data-to-paper provides a first-party published descriptive reviewer→revision closure witness. These observations use different tasks, models, evaluators and result surfaces, so public evidence still does not provide a materially matched comparison of native S3* implementations across multiple canonical harnesses.'
write_json(prim_path, primary)

# Validator: preserve the quantitative AppliedScientist contract and add a separate descriptive data-to-paper contract.
val_path = S3 / 'validate.py'
text = val_path.read_text()
old_direct = 'DIRECT_S3STAR = COMPOSED_DIRECT_S3STAR | {"appliedscientist-iterative-review"}'
new_direct = 'DIRECT_S3STAR = COMPOSED_DIRECT_S3STAR | {"appliedscientist-iterative-review", "data-to-paper-review-revision"}'
if old_direct in text:
    text = text.replace(old_direct, new_direct, 1)
elif new_direct not in text:
    raise SystemExit('direct S3* constant anchor missing')

const_anchor = 'CANONICAL_REVIEW_REF = "762824fd41598370e75588861b48991b0a9fd784"\n'
extra_consts = ('DATA_TO_PAPER_OBSERVATION_ID = "data-to-paper-review-revision-2024"\n'
                'DATA_TO_PAPER_HARNESS = "data-to-paper"\n'
                f'DATA_TO_PAPER_REVIEW_REF = "{REVIEW_REF}"\n')
if 'DATA_TO_PAPER_OBSERVATION_ID' not in text:
    if const_anchor not in text:
        raise SystemExit('canonical constant anchor missing')
    text = text.replace(const_anchor, const_anchor + extra_consts, 1)

case_anchor = '    "appliedscientist-native-s3star-direct",\n'
if '    "data-to-paper-native-s3star-direct",\n' not in text:
    if case_anchor not in text:
        raise SystemExit('required-case anchor missing')
    text = text.replace(case_anchor, case_anchor + '    "data-to-paper-native-s3star-direct",\n', 1)

helper = '''\n\ndef validate_data_to_paper_observation(observation: dict) -> None:\n    if observation.get("observation_id") != DATA_TO_PAPER_OBSERVATION_ID:\n        fail("unexpected data-to-paper canonical observation_id")\n    if observation.get("function") != "S3*" or observation.get("benchmark_fit") != "direct":\n        fail("data-to-paper canonical observation must remain direct S3*")\n    if observation.get("benchmark_id") != "data-to-paper-review-revision":\n        fail("data-to-paper benchmark linkage drift")\n    if observation.get("evidence_source_class") != "first-party-reported":\n        fail("data-to-paper result must remain first-party-reported")\n    if observation.get("boundary_class") != "canonical-native-system":\n        fail("data-to-paper observation must retain canonical-native-system boundary")\n    if observation.get("canonical_harness_id") != DATA_TO_PAPER_HARNESS:\n        fail("data-to-paper canonical_harness_id drift")\n    if observation.get("canonical_system_eligible") is not True:\n        fail("data-to-paper observation must remain canonical-system eligible")\n    if observation.get("system_compatibility") != "native-system":\n        fail("data-to-paper observation must remain native-system")\n    if observation.get("canonical_review_revision") != DATA_TO_PAPER_REVIEW_REF:\n        fail("data-to-paper canonical review ref drift")\n    if observation.get("comparison_class") != "descriptive-only":\n        fail("data-to-paper observation must remain descriptive-only")\n    if observation.get("published_example_count") != 1:\n        fail("data-to-paper published example count drift")\n    if observation.get("published_example_reference") != "Figure 2B / Supplementary Run A5":\n        fail("data-to-paper published example reference drift")\n    if observation.get("aggregate_s3star_metric_reported") is not False:\n        fail("data-to-paper must not acquire an invented aggregate S3* metric")\n\n    fields = assessment_fields(DATA_TO_PAPER_HARNESS)\n    if fields.get("status") != "included":\n        fail("data-to-paper canonical assessment must remain included")\n    if fields.get("autonomy_s3_star") != "A":\n        fail("data-to-paper no longer establishes canonical S3*=A")\n    if fields.get("review_ref") != DATA_TO_PAPER_REVIEW_REF:\n        fail("data-to-paper assessment review_ref drift")\n\n    audit_loop = observation.get("audit_loop")\n    if not isinstance(audit_loop, list) or len(audit_loop) < 6:\n        fail("data-to-paper observation must preserve full reviewer-correct-review closure")\n    loop_text = " ".join(audit_loop)\n    for phrase in ("separate role-inverted Reviewer", "transferred back into the performer", "concludes only after the product passes"):\n        if phrase not in loop_text:\n            fail(f"data-to-paper audit-loop closure drift: {phrase}")\n\n    limitation = observation.get("provenance_limitation")\n    if not isinstance(limitation, str) or DATA_TO_PAPER_REVIEW_REF not in limitation:\n        fail("data-to-paper provenance limitation must retain pinned review ref")\n    if "not independently reproduced" not in limitation:\n        fail("data-to-paper provenance limitation must preserve non-reproduction boundary")\n    if "does not bind Supplementary Run A5 to the exact canonical review revision" not in limitation:\n        fail("data-to-paper historical run/revision caveat must remain explicit")\n\n    sources = observation.get("primary_sources")\n    if not isinstance(sources, list) or len(sources) < 4 or any(not valid_https(s) for s in sources):\n        fail("data-to-paper observation requires publication plus pinned first-party code sources")\n    if "https://doi.org/10.1056/AIoa2400555" not in sources:\n        fail("data-to-paper observation must retain the publication source")\n    if not any(DATA_TO_PAPER_REVIEW_REF in source for source in sources if "github.com" in source):\n        fail("data-to-paper observation must retain pinned repository evidence")\n    metric_note = observation.get("metric_note")\n    if not isinstance(metric_note, str) or "does not report an aggregate S3*-specific" not in metric_note:\n        fail("data-to-paper no-score boundary must remain explicit")\n'''
if 'def validate_data_to_paper_observation' not in text:
    marker = '\ndef main() -> None:\n'
    if marker not in text:
        raise SystemExit('validator main anchor missing')
    text = text.replace(marker, helper + marker, 1)

old_block = '''    if len(canonical_observations) != 1:\n        fail("expected exactly one canonical direct S3* observation")\n    validate_canonical_observation(canonical_observations[0])\n'''
new_block = '''    if len(canonical_observations) != 2:\n        fail("expected exactly two canonical direct S3* observations")\n    canonical_by_id = {obs.get("observation_id"): obs for obs in canonical_observations}\n    expected_canonical_ids = {CANONICAL_OBSERVATION_ID, DATA_TO_PAPER_OBSERVATION_ID}\n    if set(canonical_by_id) != expected_canonical_ids:\n        fail(f"unexpected canonical S3* observation set: {sorted(canonical_by_id)}")\n    validate_canonical_observation(canonical_by_id[CANONICAL_OBSERVATION_ID])\n    validate_data_to_paper_observation(canonical_by_id[DATA_TO_PAPER_OBSERVATION_ID])\n'''
if old_block in text:
    text = text.replace(old_block, new_block, 1)
elif 'expected exactly two canonical direct S3* observations' not in text:
    raise SystemExit('canonical observation cardinality anchor missing')
val_path.write_text(text)
