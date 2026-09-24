# Functional capability depth — public-evidence synthesis

Status: **experimental, non-normative**

Tracking issue: #571

This document closes the current `functional-capability-depth` research cycle. It is a historical synthesis of the reviewed public-evidence state, not a permanent freeze on later evidence ingestion.

The experiment keeps two questions separate:

```text
canonical VSM assessment
        -> which organizational function exists and who owns/closes it

public capability evidence
        -> how that function performs at a declared benchmark boundary
```

A capability result does not create or change canonical autonomy state. A canonical autonomy state does not imply a benchmark capability result.

## Final function state for this cycle

<!-- BEGIN FUNCTION STATE -->
| Function | Cycle result | Primary / evidence state |
| --- | --- | --- |
| S1 | `selected` | PawBench v1.0 / `qwen3.6-35b-a3b` |
| S2 | `evidence-backed-gap` | no matched canonical-harness primary |
| S3 | `evidence-backed-gap` | no matched canonical-harness primary |
| S3* | `evidence-backed-gap` | no matched canonical-harness primary |
| S4 | `evidence-backed-gap` | no matched canonical-harness primary |
| S5 | `evidence-backed-gap` | no matched canonical-harness primary |
<!-- END FUNCTION STATE -->

The machine-readable snapshot is [`experiment-state.json`](experiment-state.json). The public-evidence operating contract is [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md).

A `gap` is not a zero capability score. It means that the reviewed public evidence did not satisfy the complete matched-primary gate for that function.

## What this cycle demonstrates

### 1. Ownership and capability are separate variables

The canonical Index answers whether a first-party path performs an organizational function at the declared system boundary and how its decision rights are owned. This experiment answers a different question: what public evidence says about the performance of an already mapped function.

Neither direction is automatic. Benchmark performance cannot assign `A`, `C`, `P`, `—`, or `?`, and canonical ownership cannot manufacture a performance observation.

### 2. Capability evidence does not require Opensiro to operate the benchmark

The useful evidence path is:

```text
public benchmark / paper / leaderboard / repository result
        ↓
provenance + observation identity
        ↓
VSM-function attribution
        ↓
ownership / boundary classification
        ↓
matched comparison when justified
```

This cycle therefore treats controlled Opensiro-operated execution as optional reproduction or validation evidence rather than as a prerequisite for capability ingestion.

The frozen Batch 02 controlled-replication work remains historical evidence. Its infrastructure failures are not capability results and do not block the public-evidence capability layer.

### 3. Direct functional evidence is not automatically canonical-native evidence

A benchmark may directly instantiate the target organizational relation while supplying the relevant organization itself. Such evidence can be function-valid and useful without measuring a canonical harness's own native function path.

This distinction explains why direct benchmark-family depth can increase while a primary remains `gap`.

### 4. Canonical-native evidence is not automatically a matched primary

The primary-selection gate requires materially matched comparison across canonical systems. A single native ablation, heterogeneous case studies, or unmatched native results do not become a cross-harness primary merely because their function attribution is strong.

For this cycle:

- S3 has a canonical native direct supervisor-control observation, but not a second materially matched canonical S3 system;
- S3* has canonical native reviewer/revision evidence from multiple systems, but the task/model/evaluator/result surfaces are not matched;
- S4 has canonical native adaptation evidence from multiple systems, but no common benchmark/model/configuration cell satisfies the full primary gate.

### 5. A fail-closed gap is an empirical result

The experiment does not force one selected benchmark into every VSM function. When provenance, native-path activation, function attribution, or matching is insufficient, the correct baseline result is `gap`.

That result is stronger than filling a table with semantically adjacent benchmarks. It preserves the boundary between observed evidence and unsupported comparison.

### 6. Self-organizing `S` remains a separate evidence class

Ordinary function capability asks how the current functional repertoire performs. Persistent endogenous change to the tested function's own decision/feedback repertoire is a different question.

Adaptive or self-organizing `S` evidence therefore remains separate rather than being collapsed into ordinary S4 capability or an extra scalar added to S1–S5.

## Function-level closure records

The evidence-backed gaps are defined by their own fail-closed closure records and reopen rules:

- S2 — [`s2-primary-search-closure.json`](s2-system-benchmarks/matched-cell/s2-primary-search-closure.json)
- S3 — [`s3-primary-search-closure.json`](s3-system-benchmarks/matched-cell/s3-primary-search-closure.json)
- S3* — [`s3star-primary-search-closure.json`](s3star-system-benchmarks/matched-cell/s3star-primary-search-closure.json)
- S4 — [`s4-primary-search-closure.json`](s4-system-benchmarks/matched-cell/s4-primary-search-closure.json)
- S5 — [`s5-primary-search-closure.json`](s5-system-benchmarks/matched-cell/s5-primary-search-closure.json)

Those records are authoritative for function-specific reopen conditions. This synthesis does not duplicate their route inventories or replace their validators.

## Limits of the current evidence

Public benchmark evidence is temporal and heterogeneous. Historical harness versions must remain historical rather than being relabeled as current canonical revisions. First-party-reported and externally reproduced results remain distinct provenance classes. Unknown model, environment, adapter, budget, or repetition details remain unknown.

Raw metrics from different benchmark families are not normalized into a universal function score. Domain-specific projections remain domain-specific. A higher score on one evidence surface does not imply greater organizational maturity, stronger autonomy, or a global harness ranking.

## Reopen model

This closes the **current public-evidence research cycle**, not future evidence ingestion.

A function-level gap may be reopened when materially new public evidence satisfies that function's recorded `reopen_when` conditions. A later selected primary may replace a gap without invalidating this historical snapshot; the new cycle should record the new evidence state explicitly rather than rewriting what was known here.

Likewise, a stronger S1 primary may replace PawBench under the existing replacement rule without deleting the historical S1 observation layer.

## Conclusion

The baseline architecture is now evidence-complete for this research cycle without pretending that every VSM function has a comparable public benchmark. S1 has a selected matched primary. S2–S5 have explicit, reviewable evidence-backed gaps. The resulting structure preserves function semantics, provenance, system boundaries, matched-comparison requirements, and uncertainty instead of collapsing them into one score or ranking.
