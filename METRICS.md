# VSM Harness Index Metrics

Deterministic numerical snapshot generated from canonical Index artifacts. Do not edit the values by hand; run `python scripts/render_metrics.py` after corpus changes.

## Corpus

| Metric | Value | Definition |
| --- | ---: | --- |
| Included standalone assessments | 810 | Canonical assessments with `status: included`; this is the public corpus-size milestone counter. |
| Canonical assessment records | 877 | Included plus canonical `excluded-no-agentic-vsm` assessment records. |
| Canonical exclusions | 67 | Completed assessments with `status: excluded-no-agentic-vsm`. |
| Proposed intake assessments | 12 | Assessment files still in `status: proposed`; not counted in the canonical corpus. |
| Catalog entries | 877 | Rows in `data/catalog.psv`; this is discovery/order/provenance infrastructure, not a second assessment database. |
| Catalog entries without an included assessment | 67 | `catalog entries - included assessments`; this includes canonical exclusions and is not automatically equivalent to pending work. |
| Reassessment events | 88 | Recorded events in `data/reassessment-history.psv`. |
| Full-A assessments | 2 | Included assessments whose base state is autonomous across S1, S2, S3, S3*, S4 and S5. `A(P)` counts as autonomous coverage. |

## Active semantic contract

Profile **0.2.4** / Methodology **0.3.7**

## Public corpus milestones

Milestones count included completed standalone assessments only. They are corpus-size checkpoints, not coverage or quality scores.

| Target | Status | Progress |
| ---: | --- | ---: |
| 100 | Achieved | Achieved (current corpus: 810) |
| 250 | Achieved | Achieved (current corpus: 810) |
| 500 | Achieved | Achieved (current corpus: 810) |
| 1000 | Next | 810/1000 (81.0%) |

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
