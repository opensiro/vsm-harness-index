# VSM Harness Index Metrics

Deterministic numerical snapshot generated from canonical Index artifacts. Do not edit the values by hand; run `python scripts/render_metrics.py` after corpus changes.

## Corpus

| Metric | Value | Definition |
| --- | ---: | --- |
| Included standalone assessments | 164 | Canonical assessments with `status: included`; this is the public corpus-size milestone counter. |
| Canonical assessment records | 167 | Included plus canonical `excluded-no-agentic-vsm` assessment records. |
| Canonical exclusions | 3 | Completed assessments with `status: excluded-no-agentic-vsm`. |
| Proposed intake assessments | 2 | Assessment files still in `status: proposed`; not counted in the canonical corpus. |
| Catalog entries | 167 | Rows in `data/catalog.psv`; this is discovery/order/provenance infrastructure, not a second assessment database. |
| Catalog entries without an included assessment | 3 | `catalog entries - included assessments`; this includes canonical exclusions and is not automatically equivalent to pending work. |
| Reassessment events | 80 | Recorded events in `data/reassessment-history.psv`. |
| Full-A assessments | 0 | Included assessments whose base state is autonomous across S1, S2, S3, S3*, S4 and S5. `A(P)` counts as autonomous coverage. |

## Active semantic contract

Profile **0.2.3** / Methodology **0.3.5**

## Public corpus milestones

Milestones count included completed standalone assessments only. They are corpus-size checkpoints, not coverage or quality scores.

| Target | Status | Progress |
| ---: | --- | ---: |
| 100 | Achieved | Achieved (current corpus: 164) |
| 250 | Next | 164/250 (65.6%) |
| 500 | Planned | 164/500 (32.8%) |
| 1000 | Planned | 164/1000 (16.4%) |

## Machine-readable view

The same snapshot is available in [`data/metrics.json`](data/metrics.json) for downstream synchronization such as `opensiro.com`.

Source-of-truth relationship:

```text
assessments/*.md + data/catalog.psv + data/reassessment-history.psv
                  + data/active-contract.psv
                         ↓
              scripts/render_metrics.py
                         ↓
             METRICS.md + data/metrics.json
```
