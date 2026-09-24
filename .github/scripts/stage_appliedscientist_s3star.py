#!/usr/bin/env python3
from pathlib import Path

path = Path('experiments/functional-capability-depth/vsm-benchmark-family-map/map.json')
text = path.read_text()
benchmark_id = 'appliedscientist-iterative-review'
if benchmark_id not in text:
    anchor = '    {"function":"S4","benchmark_id":"a-evolve-harness-evolution"'
    if anchor not in text:
        raise SystemExit('S4 insertion anchor missing')
    entry = '    {"function":"S3*","benchmark_id":"appliedscientist-iterative-review","benchmark_name":"AppliedScientist iterative scientific review-revision","fit":"direct","primary_source":"https://arxiv.org/abs/2609.14738","evaluated_object":"canonical AppliedScientist scientific-revision system in which a separate fresh reviewer independently audits each manuscript, returns feedback into Scientist code/experiment/manuscript revision, and reviews the subsequent revision again","evaluation_mode":"execution-grounded-research","system_linkage":"native-canonical-observation","non_claim":"This is a first-party-reported within-system canonical S3* observation; it is not an independently reproduced run at the pinned Git revision and does not create a matched cross-harness S3* primary baseline."},\n'
    text = text.replace(anchor, entry + anchor, 1)
    path.write_text(text)
