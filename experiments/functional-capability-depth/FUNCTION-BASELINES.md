# Function Capability Baselines

Generated experimental projection from `primary-baselines.json` and the function-specific S2–S5 coverage records.

This view reports baseline availability and evidence coverage only. It does not change canonical VSM ownership, create a capability score, or replace the function-specific evidence records.

## Current primary-baseline state

| Function | Status | Primary family | Reference model | Evidence state |
| --- | --- | --- | --- | --- |
| S1 | `selected` | PawBench v1.0 | `qwen3.6-35b-a3b` | [generated S1 baseline](S1-BASELINE.md) |
| S2 | `gap` | — | — | [`coverage.json`](s2-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 17 reviewed cases · direct families: `5` · direct observations: `2` · canonical direct observations: `0` |
| S3 | `gap` | — | — | [`coverage.json`](s3-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 11 reviewed cases · direct families: `3` · direct observations: `1` |
| S3* | `gap` | — | — | [`coverage.json`](s3star-system-benchmarks/coverage.json) · reviewed `2026-09-24` · 16 reviewed cases · direct families: `5` · canonical direct observations: `2` · composed direct observations: `3` |
| S4 | `gap` | — | — | [`coverage.json`](s4-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 15 reviewed cases · direct families: `4` · canonical direct observations: `2` · composed direct observations: `4` |
| S5 | `gap` | — | — | [`coverage.json`](s5-system-benchmarks/coverage.json) · reviewed `2026-09-25` · 14 reviewed cases · direct families: `1` · canonical direct observations: `1` · composed direct observations: `1` |

A `gap` means that no matched canonical-harness primary baseline has been selected for that function. It is not a zero capability score and it does not mean benchmark evidence is absent.

## Why the current gaps remain

### S2

Reviewed direct S2 evidence now includes five benchmark-defined disturbance/attenuation families. Nool and The Specification Gap supply two admitted immutable direct non-canonical observations; Twining conflict-resolution is direct at its benchmark boundary but lacks recoverable exact Twining treatment revision and canonical harness linkage. Public evidence still provides no canonical native direct S2 observation and no matched comparison of native S2 implementations across multiple canonical harnesses.

Evidence search: [`s2-system-benchmarks/coverage.json`](s2-system-benchmarks/coverage.json).

### S3

Reviewed direct S3 families now include a canonical native within-system current-control ablation, but public evidence still does not provide a matched comparison of native S3 implementations across multiple canonical harnesses under one common benchmark/model/configuration cell.

Evidence search: [`s3-system-benchmarks/coverage.json`](s3-system-benchmarks/coverage.json).

### S3*

Reviewed direct S3* evidence now includes two canonical native systems: AppliedScientist provides quantitative within-system weakness-closure measurements, while data-to-paper provides a first-party published descriptive reviewer→revision closure witness. These observations use different tasks, models, evaluators and result surfaces, so public evidence still does not provide a materially matched comparison of native S3* implementations across multiple canonical harnesses.

Evidence search: [`s3star-system-benchmarks/coverage.json`](s3star-system-benchmarks/coverage.json).

### S4

Direct S4 evidence now includes two canonical native systems: A-Evolve publishes harness-updating measurements across SWE-bench Verified, MCP-Atlas and SkillsBench, while KADATH publishes a ten-epoch locked-benchmark population-improvement run. Their tasks, benchmark definitions, models/configurations and result surfaces are not matched, so public evidence still does not provide a common cross-harness S4 comparison cell.

Evidence search: [`s4-system-benchmarks/coverage.json`](s4-system-benchmarks/coverage.json).

### S5

Reviewed direct S5 evidence now includes GovSim-SelfGovern's benchmark-scaffolded membership/identity authority path and one canonical native descriptive observation: Ouroboros PR #855 supplies a parent-governed constitutional/runtime policy-change witness with executable return and persistence into later canonical lineage. Public evidence still lacks a materially matched comparison of multiple canonical native or adapter-preserved S5 implementations under one comparable authority/change/subsequent-operation surface.

Evidence search: [`s5-system-benchmarks/coverage.json`](s5-system-benchmarks/coverage.json).

## Reading rule

```text
canonical VSM ownership
        ↓
one selected primary benchmark per function when evidence permits
        ↓
matched canonical-harness comparison
        ↓
secondary evidence and domain projections

separate evidence class:
adaptive / self-organizing S
```

Function-specific coverage schemas remain authoritative for their own evidence vocabulary. This projection intentionally consumes their common review metadata without forcing those schemas into one normalized replacement database.
