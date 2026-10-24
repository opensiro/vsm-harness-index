# VSM Harness Index Metrics

Deterministic numerical snapshot generated from canonical Index artifacts. Do not edit the values by hand; run `python scripts/render_metrics.py` after corpus changes.

## Corpus

| Metric | Value | Definition |
| --- | ---: | --- |
| Included standalone assessments | 696 | Canonical assessments with `status: included`; this is the public corpus-size milestone counter. |
| Canonical assessment records | 750 | Included plus canonical `excluded-no-agentic-vsm` assessment records. |
| Canonical exclusions | 54 | Completed assessments with `status: excluded-no-agentic-vsm`. |
| Proposed intake assessments | 11 | Assessment files still in `status: proposed`; not counted in the canonical corpus. |
| Catalog entries | 750 | Rows in `data/catalog.psv`; this is discovery/order/provenance infrastructure, not a second assessment database. |
| Catalog entries without an included assessment | 54 | `catalog entries - included assessments`; this includes canonical exclusions and is not automatically equivalent to pending work. |
| Reassessment events | 88 | Recorded events in `data/reassessment-history.psv`. |
| Full-A assessments | 2 | Included assessments whose base state is autonomous across S1, S2, S3, S3*, S4 and S5. `A(P)` counts as autonomous coverage. |

## Active semantic contract

Profile **0.2.4** / Methodology **0.3.7**

## Public corpus milestones

Milestones count included completed standalone assessments only. They are corpus-size checkpoints, not coverage or quality scores.

| Target | Status | Progress |
| ---: | --- | ---: |
| 100 | Achieved | Achieved (current corpus: 696) |
| 250 | Achieved | Achieved (current corpus: 696) |
| 500 | Achieved | Achieved (current corpus: 696) |
| 1000 | Next | 696/1000 (69.6%) |

## Machine-readable view

The same snapshot is available in [`data/metrics.json`](data/metrics.json) for downstream synchronization such as `opensiro.com`.

Source-of-truth relationship:

```text
assessments/**/*.md + data/catalog.psv + data/reassessment-history.psv
                  + data/active-contract.psv
                         ↓
              scripts/render_metrics.py
                         ↓
             METRICS.md + data/metrics.json
```
