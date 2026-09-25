# Function Capability Baselines

Generated experimental projection from `primary-baselines.json` and the function-specific S2–S5 coverage records.

This view reports baseline availability and evidence coverage only. It does not change canonical VSM ownership, create a capability score, or replace the function-specific evidence records.

## Current primary-baseline state

| Function | Status | Primary family | Reference model | Evidence state |
| --- | --- | --- | --- | --- |
| S1 | `selected` | PawBench v1.0 | `qwen3.6-35b-a3b` | [generated S1 baseline](S1-BASELINE.md) |
| S2 | `gap` | — | — | [`coverage.json`](s2-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 20 reviewed cases · direct families: `7` · direct observations: `3` · canonical direct observations: `0` |
| S3 | `gap` | — | — | [`coverage.json`](s3-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 11 reviewed cases · direct families: `3` · direct observations: `1` |
| S3* | `gap` | — | — | [`coverage.json`](s3star-system-benchmarks/coverage.json) · reviewed `2026-09-24` · 16 reviewed cases · direct families: `5` · canonical direct observations: `2` · composed direct observations: `3` |
| S4 | `gap` | — | — | [`coverage.json`](s4-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 15 reviewed cases · direct families: `4` · canonical direct observations: `2` · composed direct observations: `4` |
| S5 | `gap` | — | — | [`coverage.json`](s5-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 14 reviewed cases · direct families: `1` · canonical direct observations: `1` · composed direct observations: `1` |

A `gap` means that no matched canonical-harness primary baseline has been selected for that function. It is not a zero capability score and it does not mean benchmark evidence is absent.

## Why the current gaps remain

### S2

Reviewed direct S2 evidence now includes seven disturbance/attenuation families. Nool and The Specification Gap provide two benchmark-scaffolded direct non-canonical observations, while CodeCRDT provides one descriptive direct observation at its own external native product boundary. Twining lacks recoverable exact treatment revision, and CooperBench lacks the pinned flash-run logs needed for observation admission. CodeCRDT has no matched uncoordinated-parallel control and is not a canonical Index harness. Public evidence still provides no canonical native direct S2 observation and no matched comparison of native S2 implementations across multiple canonical harnesses.

Evidence search: [`s2-system-benchmarks/coverage.json`](s2-system-benchmarks/coverage.json).

### S3

Reviewed direct S3 families now include a canonical native within-system current-control ablation, but public evidence still does not provide a matched comparison of native S3 implementations across multiple canonical harnesses under one common benchmark/model/configuration cell.

Evidence search: [`s3-system-benchmarks/coverage.json`](s3-system-benchmarks/coverage.json).

### S3*

Reviewed direct S3* evidence includes both benchmark-scaffolded and canonical-native/composed reviewer-revision surfaces, but the canonical rows are not yet materially matched across task/model/evaluator/configuration, so no primary cross-harness baseline is selected.

Evidence search: [`s3star-system-benchmarks/coverage.json`](s3star-system-benchmarks/coverage.json).

### S4

Reviewed direct S4 evidence includes public adaptation/evolution benchmark families and canonical-native/composed adaptation surfaces, but no common benchmark/model/configuration cell yet provides a materially matched comparison across canonical systems.

Evidence search: [`s4-system-benchmarks/coverage.json`](s4-system-benchmarks/coverage.json).

### S5

Reviewed direct S5 evidence includes one benchmark-defined governance society family plus one canonical descriptive parent-governed policy-change observation, but no materially matched second canonical system is available for primary selection.

Evidence search: [`s5-system-benchmarks/coverage.json`](s5-system-benchmarks/coverage.json).
