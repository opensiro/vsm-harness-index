# Public-evidence capability ingestion

Status: **experimental, non-normative**

Tracking issue: #452

This document defines the default operating model for `functional-capability-depth`.

The VSM Harness Index is an evidence index, not a required benchmark operator. Per-function capability evidence should therefore be built primarily from public benchmark, leaderboard, paper, repository, and result artifacts that can be provenance-bound and semantically mapped to a VSM function.

Opensiro-operated benchmark execution is optional validation or reproduction evidence. It is **not** a prerequisite for admitting a capability observation, selecting a primary benchmark family, or maintaining a function-level capability projection.

## Operating model

```text
public benchmark / paper / leaderboard / repository result
                    ↓
          provenance + normalization
                    ↓
       VSM-function attribution
                    ↓
         comparable evidence groups
                    ↓
        capability projections
```

The canonical VSM assessment remains separate:

```text
repository @ pinned revision
        ↓
canonical VSM function / ownership state

public capability evidence
        ↓
function-specific observations
```

Benchmark performance does not create or change `A`, `C`, `P`, `—`, `?`, `A(P)`, or `C(P)` states.

## Admission sequence

For a public result:

1. identify the public source and preserve an immutable source revision/artifact where available;
2. identify the benchmark family, version, task set/split, metric, model, and published harness configuration;
3. link the benchmarked harness identity to a canonical Index system without silently equating an ambiguous display label with a repository;
4. establish that the benchmark actually exercises the relevant first-party function boundary rather than supplying that function entirely from benchmark scaffolding;
5. classify system compatibility and comparison quality;
6. store the raw observation once;
7. project the observation into one or more VSM functions only after function-specific semantic review.

Do not infer VSM functions from benchmark slice names such as planning, verification, memory, coordination, governance, or learning.

## Evidence-source classes

These source classes describe **who produced the result**, not whether the result is semantically valid for a VSM function.

### `external-reproduced`

A public result produced by an evaluator, benchmark operator, leaderboard operator, research group, or other party that is independent of the harness/project being measured.

Examples include public third-party benchmark campaigns that run several harnesses under one evaluation surface.

This class is preferred for cross-harness comparison when the comparison cell is also materially matched.

### `first-party-reported`

A public result published by the harness/project owner or maintainer.

It may be admitted when provenance and configuration are recoverable, but it must remain visibly first-party-reported and must not be described as independently reproduced.

### `mechanism-only`

Primary executable or repository evidence establishes a relevant capability mechanism or VSM function path, but there is no admitted performance observation for that mechanism/system under a reviewed benchmark family.

`mechanism-only` is not a numeric result and must not be converted into one.

A later external or first-party result may add a performance observation without rewriting the earlier mechanism evidence.

## Orthogonal evidence dimensions

Evidence-source class is separate from existing compatibility and comparison classes.

System compatibility may remain, for example:

- `native-system`;
- `adapter-preserved`;
- `benchmark-scaffolded`;
- `unclear`.

Comparison quality may remain, for example:

- `matched-model`;
- `partially-matched`;
- `descriptive-only`.

A third-party result is not automatically comparable. A first-party result is not automatically unusable. Function validity, system identity, compatibility, and comparison matching are separate questions.

## Matched-comparison rule

A direct cross-harness capability comparison should use a public comparison cell that keeps constant, as far as the published evidence permits:

- benchmark family/version and task set or split;
- model and materially relevant model configuration;
- evaluator or grader;
- execution environment;
- budget, timeout, and repetition policy;
- adaptation/reset policy where persistent repertoire changes could contaminate later tasks.

The harness/system should be the intended varying factor.

If those conditions are not materially matched, preserve the observation as `partially-matched`, `descriptive-only`, proxy, or another explicit weaker class rather than manufacturing a direct comparison.

Raw metrics from different benchmark families must not be normalized into one universal function score.

## Required provenance

Preserve, where available:

- canonical harness ID and repository;
- benchmarked harness display label;
- benchmarked harness version, source revision, and configuration;
- relationship to the current canonical assessment revision;
- benchmark family, version, variant, and split;
- task count;
- exact model identifier and model configuration;
- metric and raw result;
- result date;
- publisher/source owner;
- primary source and immutable artifact source;
- evidence-source class;
- execution environment;
- evaluator/grader;
- budget, timeout, and repetition settings;
- system compatibility class;
- comparison group and comparison class;
- known discrepancies and confounders.

Unknown values remain unknown. Do not infer an exact historical harness revision, model configuration, or environment from a current repository state.

## Function attribution

A benchmark observation becomes S1/S2/S3/S3*/S4/S5 capability evidence only after the benchmark boundary is mapped to the corresponding organizational function.

Examples of invalid shortcuts:

```text
planning score       → S3
verification score   → S3*
coordination score   → S2
learning score       → S4
governance score     → S5
```

The benchmark scaffold may itself own the named behavior. A direct VSM benchmark can therefore still fail to provide a native canonical-harness comparison.

Map the organizational function first; only then use the benchmark result as capability evidence for that function.

## Capability ownership interpretation

Outcome provenance and causal ownership are distinct.

Where independently supported, a capability interpretation may use:

- `native` — material capability is owned inside the assessed first-party function boundary;
- `inherited` — capability is supplied primarily by an external model, host, runtime, tool service, or other substrate;
- `mixed` — material first-party control/transformation acts over inherited capability;
- `unclear` — evidence is insufficient for causal ownership attribution.

A benchmark score alone normally establishes behavior of the measured system plus its published substrate. It does not by itself prove that the observed difference was caused by the harness implementation.

## Historical observations

Public results are temporal evidence.

A result for `Harness X v1.2` remains valid historical evidence even if the canonical Index assessment later moves to a newer repository revision. Preserve the historical version/revision relationship rather than relabeling the result as current.

New upstream releases may justify new observations or a new comparison cell; they do not invalidate an older correctly identified observation.

## Primary baselines and gaps

The baseline view may select one primary benchmark family per VSM function when public evidence supplies a sufficiently matched canonical-harness comparison.

A function-level `gap` means:

> no selected matched canonical-harness primary baseline is currently supported by the reviewed public evidence.

It does **not** mean:

- the function has zero capability;
- no relevant benchmark family exists;
- Opensiro has failed to run its own benchmark.

S2-S5 gaps should therefore remain gaps until public evidence supports a valid primary, rather than being filled by an Opensiro-operated benchmark merely for completeness.

## Relationship to controlled reproduction

Controlled reproduction remains useful when it can answer a specific uncertainty, for example:

- verify a disputed public result;
- recover missing environment details;
- test adapter parity;
- run an ablation unavailable in published evidence;
- distinguish a harness effect from a model/environment effect.

Such reproduction is optional secondary evidence unless a separate experiment explicitly defines it as its own goal.

The frozen Batch 02 controlled-replication design and attempt records remain immutable historical experiment artifacts. They are not a prerequisite for the public-evidence capability layer.

## Relationship to self-organizing `S`

Public capability evidence and the self-organizing-autonomy experiment remain separate.

A high benchmark score does not establish experimental `S`. Persistent adaptation observed inside a benchmark must be identified explicitly rather than silently mixed with an ordinary frozen-repertoire comparison.

## Source-of-truth rule

Store raw published metrics once in the shared observation layer. Function-specific files and generated views should reference those observations rather than copying values into parallel manually maintained tables.

The current S1 observation layer already follows this direction through `s1-system-benchmarks/observations.jsonl` and generated projections.

## Non-goals

- no global harness winner;
- no scalar score across S1-S5;
- no replacement of canonical VSM assessment;
- no requirement that Opensiro execute every admitted benchmark;
- no inference of organizational function from benchmark vocabulary;
- no forced filling of S2-S5 gaps;
- no rewrite of frozen controlled-execution history.
