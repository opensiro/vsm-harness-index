# Function Capability Baselines

Generated experimental projection from `primary-baselines.json` and the function-specific S2–S5 coverage records.

This view reports baseline availability and evidence coverage only. It does not change canonical VSM ownership, create a capability score, or replace the function-specific evidence records.

## Current primary-baseline state

| Function | Status | Primary family | Reference model | Evidence state |
| --- | --- | --- | --- | --- |
| S1 | `selected` | PawBench v1.0 | `qwen3.6-35b-a3b` | [generated S1 baseline](S1-BASELINE.md) |
| S2 | `gap` | — | — | [`coverage.json`](s2-system-benchmarks/coverage.json) · reviewed `2026-09-23` · 8 reviewed cases · direct observations: `0` |
| S3 | `gap` | — | — | [`coverage.json`](s3-system-benchmarks/coverage.json) · reviewed `2026-09-23` · 7 reviewed cases · direct observations: `0` |
| S3* | `gap` | — | — | [`coverage.json`](s3star-system-benchmarks/coverage.json) · reviewed `2026-09-23` · 9 reviewed cases · direct families: `1` · canonical direct observations: `0` · composed direct observations: `1` |
| S4 | `gap` | — | — | [`coverage.json`](s4-system-benchmarks/coverage.json) · reviewed `2026-09-23` · 13 reviewed cases · direct families: `3` · canonical direct observations: `0` · composed direct observations: `3` |
| S5 | `gap` | — | — | [`coverage.json`](s5-system-benchmarks/coverage.json) · reviewed `2026-09-23` · 11 reviewed cases · direct families: `0` · canonical direct observations: `0` |

A `gap` means that no matched canonical-harness primary baseline has been selected for that function. It is not a zero capability score and it does not mean benchmark evidence is absent.

## Why the current gaps remain

### S2

The coordination organization and protocol are benchmark-scaffolded; published comparisons do not yet isolate native S2 implementations across canonical harnesses under a matched model.

Evidence search: [`s2-system-benchmarks/coverage.json`](s2-system-benchmarks/coverage.json).

### S3

The benchmark supplies the management tool surface, worker pool and team organization; published comparison varies the main-agent model rather than native S3 implementations of canonical harnesses.

Evidence search: [`s3-system-benchmarks/coverage.json`](s3-system-benchmarks/coverage.json).

### S3*

The complementary audit function is supplied by the external TrueCall layer, so wrapped harness results cannot be attributed as native S3* capability of the canonical harness.

Evidence search: [`s3star-system-benchmarks/coverage.json`](s3star-system-benchmarks/coverage.json).

### S4

Current direct families evaluate benchmark-defined or composed adaptation loops rather than matched native S4 implementations across canonical harnesses.

Evidence search: [`s4-system-benchmarks/coverage.json`](s4-system-benchmarks/coverage.json).

### S5

No reviewed benchmark family currently provides direct legitimate ultimate-policy/identity authority, actual adjudication or revision, and return of the newly decided policy into subsequent operation.

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
