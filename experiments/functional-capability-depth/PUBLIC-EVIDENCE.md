# Public-evidence capability ingestion

Status: **experimental, non-normative**

Tracking issue: #452  
Operating-model clarification: #617  
Neutral benchmark-system registry boundary: #782

Current registry contract: [`BENCHMARK-SYSTEM-REGISTRY.md`](BENCHMARK-SYSTEM-REGISTRY.md).

This document defines the active public-evidence operating model for `functional-capability-depth`.

The VSM Harness Index is an evidence index, not a benchmark operator. OpenSiro does not need to operate a harness benchmark, nor canonically decide what VSM function a benchmark measures, in order to preserve an otherwise valid public benchmark ↔ system observation.

**Opensiro does not run or reproduce benchmark experiments on assessed harnesses to create capability evidence for this experiment.** A public-evidence gap remains a gap until suitable upstream or third-party evidence exists.

Historical controlled-execution designs, preregistrations, fixtures, fake artifacts, and execution harnesses may remain under `experiments/` as research history. They are not an active admission path and must not be treated as capability observations.

## Active operating model

```text
public upstream / third-party benchmark, paper, leaderboard, repository result
                    ↓
              benchmark identity
                    ↓
          concrete system identity
                    ↓
       raw system-linked observation
                    ↓
          provenance + normalization
                    ↓
      optional derived interpretations
        ├── VSM-function relevance
        ├── domain relevance
        └── capability/comparison views
```

The canonical VSM assessment remains separate:

```text
repository @ pinned revision
        ↓
canonical VSM function / ownership state
```

Benchmark performance does not create or change `A`, `C`, `P`, `—`, `?`, `A(P)`, or `C(P)` states.

The following is explicitly **not** part of the active workflow:

```text
capability gap
        ↓
OpenSiro operates the harness / benchmark
        ↓
newly generated result
        ↓
Index evidence
```

Nor is this required for raw observation admission:

```text
public benchmark result
        ↓
OpenSiro must first decide one canonical VSM-function meaning
        ↓
only then preserve the result
```

VSM relevance is a separate research/community interpretation layer.

## Admission sequence for a raw public result

1. identify the public source and preserve an immutable source revision/artifact where available;
2. identify the benchmark family, version, task set/split, metric, model, and published system configuration;
3. link the benchmarked system identity to a canonical Index harness only when the public provenance supports that link;
4. classify whether the benchmark exercised a native system path, preserved it through an adapter, supplied a benchmark-scaffolded organization, or remains unclear;
5. preserve the raw metric/result and historical execution identity;
6. record comparison metadata and known confounders without manufacturing comparability;
7. store the raw observation once.

A later VSM-function, domain, or capability interpretation references the raw observation ID and may be revised independently.

Do not infer system identity from a benchmark display label alone. Do not infer historical versions or run configuration from current repository state.

## Evidence-source classes

These source classes describe **who produced the public result**, not what the benchmark means semantically.

### `external-reproduced`

A public result produced by an evaluator, benchmark operator, leaderboard operator, research group, or other party independent of the harness/project being measured.

This class is preferred for cross-system comparison when the comparison cell is also materially matched.

### `first-party-reported`

A public result published by the harness/project owner or maintainer.

It may be admitted when provenance and configuration are recoverable, but it must remain visibly first-party-reported and must not be described as independently reproduced.

### `mechanism-only`

Primary executable or repository evidence establishes a relevant mechanism/system path, but there is no admitted public performance observation.

`mechanism-only` is not a numeric result and must not be converted into one.

## Orthogonal evidence dimensions

Evidence-source class, system compatibility, comparison quality, canonical VSM state, and later function interpretation are separate questions.

System compatibility may include:

- `native-system`;
- `adapter-preserved`;
- `benchmark-scaffolded`;
- `unclear`.

Comparison quality may include:

- `matched-model`;
- `partially-matched`;
- `descriptive-only`.

A third-party result is not automatically comparable. A first-party result is not automatically unusable. A result linked to a canonical harness is not automatically evidence for any particular VSM function.

## Matched-comparison rule

A direct cross-harness comparison should use a public comparison cell that keeps constant, as far as the published evidence permits:

- benchmark family/version and task set or split;
- model and materially relevant model configuration;
- evaluator or grader;
- execution environment;
- budget, timeout, and repetition policy;
- adaptation/reset policy where persistent repertoire changes could contaminate later tasks.

The harness/system should be the intended varying factor.

If those conditions are not materially matched, preserve the observation as `partially-matched`, `descriptive-only`, or another explicit weaker class rather than manufacturing a direct comparison.

Raw metrics from different benchmark families must not be normalized into one universal score.

## Required provenance

Preserve, where available:

- canonical harness ID and repository when linkable;
- benchmarked harness/system display label;
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
- reset/adaptation state where public evidence establishes it;
- known discrepancies and confounders.

Unknown values remain unknown.

## System linkage

The registry's first semantic responsibility is **identity**, not benchmark meaning.

A canonical harness linkage should be supported by public evidence such as:

- an adapter that installs or invokes the first-party harness;
- benchmark/submission metadata with a recoverable version or repository identity;
- first-party benchmark artifacts identifying the implementation;
- another reconstructable provenance chain.

If the benchmark authors supply the evaluated organization and no canonical harness identity is supportable, preserve that boundary as benchmark-scaffolded/non-canonical instead of inventing a harness mapping.

## VSM-function relevance is a derived interpretation

A raw observation may later be interpreted as relevant to one or more VSM functions, or to none.

Examples of invalid automatic shortcuts remain:

```text
planning score       → S3
verification score   → S3*
coordination score   → S2
learning score       → S4
governance score     → S5
```

But rejecting those shortcuts does **not** mean raw evidence must wait for OpenSiro to produce an authoritative replacement classification.

Community/research views may instead reference the raw observation and argue:

```text
observation X → S2-relevant
observation X → S2 + S3 proxy
observation X → not direct S2
observation X → no useful VSM attribution
```

Such interpretation may change without rewriting the benchmark/system/result identity.

Existing function-specific maps, projections, and closure artifacts remain historical/derived outputs from this experiment. They are not prerequisites for admitting new raw public observations.

## Capability ownership interpretation

Outcome provenance and causal ownership are distinct.

Where independently supported, a derived capability interpretation may use:

- `native` — material capability is owned inside the assessed first-party boundary;
- `inherited` — capability is supplied primarily by an external model, host, runtime, tool service, or other substrate;
- `mixed` — material first-party control/transformation acts over inherited capability;
- `unclear` — evidence is insufficient for causal ownership attribution.

A benchmark score alone normally establishes behavior of the measured system plus its published substrate. It does not by itself prove what caused the observed difference.

## Historical observations

Public results are temporal evidence.

A result for `Harness X v1.2` remains valid historical evidence even if the canonical Index assessment later moves to a newer repository revision. Preserve the historical version/revision relationship rather than relabeling the result as current.

New upstream releases may justify new observations or a new comparison cell; they do not invalidate an older correctly identified observation.

## Shared raw source of truth

Store a published numeric result once in the neutral observation layer.

```text
raw observation
        ↓
        ├── VSM interpretation view
        ├── domain view
        ├── comparison view
        └── other community/research view
```

Derived views reference observation IDs rather than copying the metric into parallel manually maintained tables.

The current neutral seed is [`system-observations/`](system-observations/).

## Function-level primary baselines and gaps

Historical/current per-function primary-baseline work may continue as a **derived research view** when someone chooses a VSM interpretation and enough matched evidence exists.

A function-level `gap` means only that the reviewed derived view does not currently support a selected matched canonical-harness primary for that function.

S2-S5 gaps therefore remain gaps until public upstream or third-party evidence supports a valid derived primary; the neutral raw registry does not need to wait for that interpretation before preserving a system-linked result.

It does **not** mean:

- the function has zero capability;
- no relevant benchmark family exists;
- the raw registry lacks system-linked evidence;
- OpenSiro should run its own benchmark to fill the gap.

## Controlled-execution history

Controlled-execution work already present under this experiment is historical research material only.

This includes frozen Batch 02 controlled-replication design/attempt records and LoopX S2 preregistration/execution-harness artifacts produced before #617.

These artifacts may document methodology questions such as identifiability, adapter preservation, or why a proposed comparison would be invalid. They must not be scheduled for live harness execution as part of this evidence registry, and fake/stub results must never be promoted into capability observations.

If a future OpenSiro research track intentionally studies controlled reproduction, it must be scoped separately from this registry.

## Relationship to self-organizing `S`

Raw public benchmark evidence and the self-organizing-autonomy experiment remain separate.

Persistent adaptation observed inside a public benchmark should be recorded explicitly where the protocol establishes it rather than silently mixed with an ordinary frozen/reset comparison.

A high benchmark score does not establish experimental `S`.

## Non-goals

- no canonical benchmark-to-VSM-function taxonomy required for raw admission;
- no global harness winner;
- no scalar score across S1-S5;
- no replacement of canonical VSM assessment;
- no OpenSiro-operated harness benchmark runs to create evidence;
- no inference of organizational function from benchmark vocabulary;
- no forced filling of S2-S5 gaps;
- no rewrite of frozen controlled-execution history.
