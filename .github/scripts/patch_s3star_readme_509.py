#!/usr/bin/env python3
from pathlib import Path

path = Path('experiments/functional-capability-depth/s3star-system-benchmarks/README.md')
text = path.read_text()

text = text.replace(
    'First canonical native observation: #502\n',
    'First canonical native observation: #502  \nSecond canonical native observation: #509\n',
    1,
)
text = text.replace(
    'reviewed direct S3* benchmark families: 4\npublished direct observations at composed S3* boundaries: 3\ncanonical native direct-S3* observations: 1',
    'reviewed direct S3* benchmark families: 5\npublished direct observations at composed S3* boundaries: 3\ncanonical native direct-S3* observations: 2',
    1,
)
text = text.replace(
    'canonical linkage gap: partially closed\n  AppliedScientist provides the first reviewed native canonical observation',
    'canonical linkage gap: substantially narrowed\n  AppliedScientist and data-to-paper now provide two reviewed native canonical observations',
    1,
)

section = '''## Second canonical native observation — data-to-paper

Canonical anchor:

```text
harness_id: data-to-paper
review_ref: 81df14c4b9600466e645c3b2b336cc54daa3df3a
S3*=A
```

The standalone canonical assessment independently establishes the native S3* path: a separate reviewer conversation challenges the current performer product, reviewer concerns are returned to the original performer for revision, and review repeats until approval or the configured bound.

The first-party NEJM AI publication directly shows this organization in operation. Figure 2B, drawn from Supplementary Run A5, presents reviewer feedback on a Discussion draft being returned to the performer and producing a corrected revision. The Methods also state that a research step concludes only after its product passes rule-based and LLM review, so rejected products remain inside the corrective review loop.

This record is deliberately **descriptive-only**:

- it establishes a published native reviewer → revision closure witness;
- it does **not** report an aggregate S3*-specific detection, correction or re-verification score;
- the paper's broader paper-quality result must not be relabeled as an S3* metric;
- it is first-party-reported and not independently reproduced;
- the publication does not bind Supplementary Run A5 to the exact canonical repository revision.

Together with AppliedScientist this raises `canonical_direct_observation_count` to `2`, but the two observations use different scientific tasks, models, evaluators and result surfaces. They therefore do not form a matched cross-harness comparison.

'''
anchor = '## Native proxy — SWE-agent\n'
if '## Second canonical native observation — data-to-paper' not in text:
    if anchor not in text:
        raise SystemExit('native proxy section anchor missing')
    text = text.replace(anchor, section + anchor, 1)

text = text.replace(
    '- `appliedscientist` — `S3*=A`, first admitted canonical direct observation.\n',
    '- `appliedscientist` — `S3*=A`, first admitted canonical direct observation;\n- `data-to-paper` — `S3*=A`, second admitted canonical direct observation, descriptive-only.\n',
    1,
)
text = text.replace(
    '- `canonical_observations.json` — direct native/adapter-preserved canonical harness observations; currently one AppliedScientist record;',
    '- `canonical_observations.json` — direct native/adapter-preserved canonical harness observations; currently AppliedScientist (quantitative within-system closure) plus data-to-paper (descriptive published closure witness);',
    1,
)
text = text.replace(
    '- select a primary baseline from one native observation;\n',
    '- normalize AppliedScientist and data-to-paper into one score;\n- treat data-to-paper overall paper correctness as an S3* metric;\n- select a primary baseline from heterogeneous native observations;\n',
    1,
)

path.write_text(text)
