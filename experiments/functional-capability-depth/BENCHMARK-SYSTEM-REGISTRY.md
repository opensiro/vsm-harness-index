# Benchmark ↔ system evidence registry

Status: **experimental, non-normative**

Tracking issue: #782

This document defines the active neutral evidence boundary for the `functional-capability-depth` experiment.

The registry does **not** decide what a benchmark means in VSM terms. Its job is narrower:

1. identify which concrete harness/system a public benchmark result actually exercised;
2. preserve the published result and enough provenance to reconstruct its identity;
3. expose those system-linked observations for later community/research interpretation.

## Core flow

```text
public benchmark / paper / leaderboard / repository result
                    ↓
          benchmark identity
                    ↓
       concrete harness/system identity
                    ↓
      raw system-linked observation
                    ↓
          provenance + metadata
                    ↓
      optional derived interpretations
        ├── VSM-function relevance
        ├── domain relevance
        └── capability/comparison views
```

The first four steps are the registry. The final interpretation layer is not a prerequisite for admitting a raw system-linked observation.

## What OpenSiro establishes

For every admitted observation, establish as far as the public record allows:

- **evidence-surface identity** — benchmark family/version/task split when benchmarked, or an explicit paper/repository/operational surface when not benchmark-based;
- **system identity** — canonical harness ID when linkable, repository, benchmark display label, historical harness version/revision/configuration;
- **execution identity** — model/configuration, evaluator, environment, budget, timeout, repetition policy where published;
- **result identity** — raw metric/result, result date, task/replicate counts where published;
- **provenance** — publisher, primary source, immutable artifact/source revision where available;
- **system compatibility** — for example `native-system`, `adapter-preserved`, `benchmark-scaffolded`, `unclear`;
- **comparison metadata** — comparison group, `matched-model` / `partially-matched` / `descriptive-only` where supportable, plus known confounders;
- **historical relation** — whether the benchmarked system revision matches, predates, or cannot be tied exactly to the current canonical assessment revision;
- **adaptation state** — frozen/reset where established, adaptive where persistent repertoire change is intentionally part of the public run, otherwise unknown.

Unknown values remain unknown. Current repository state must not be used to invent historical run metadata.

## What OpenSiro does not need to decide at registry admission

The raw registry does not require a canonical answer to:

```text
Which VSM function does this benchmark measure?
Is this metric direct or proxy evidence for S2/S3/etc.?
Is the benchmark relevant enough to use in a function-level capability argument?
```

Those are interpretation questions. They may be discussed and encoded in separate derived views, issues, papers, or community annotations that reference the raw observation ID.

The same raw result may legitimately receive:

- several competing function interpretations;
- more than one function interpretation;
- no function interpretation yet;
- a later revised interpretation without rewriting the raw result.

## Linkage rule

A benchmark display label is not sufficient by itself to establish a canonical harness linkage.

A system link should be backed by public evidence such as:

- an adapter that installs/invokes a first-party harness;
- an exact repository/revision/version in submission metadata;
- first-party benchmark artifacts identifying the implementation;
- another recoverable public provenance chain.

If the benchmark supplies the organization itself and no canonical harness identity is supportable, keep the observation benchmark-scaffolded/non-canonical rather than inventing a harness mapping.

## Non-benchmark evidence surfaces

The neutral layer also accepts public system evidence that is not a benchmark result, such as immutable repository history, public operational incident/case-study evidence, or another explicitly named evidence surface.

Such an observation MUST use `evidence_surface` or `evidence_surfaces` rather than inventing a benchmark label. Function-specific interpretation remains downstream exactly as it does for benchmark observations.

## Result provenance classes

Preserve at least these source classes where applicable:

- `external-reproduced` — result published by an evaluator/benchmark operator independent of the harness project;
- `first-party-reported` — result published by the harness/project owner;
- `mechanism-only` — public implementation/mechanism evidence exists but there is no admitted numeric performance observation.

Source class is independent of system compatibility and comparison quality.

## System compatibility

Compatibility describes what implementation the benchmark actually exercised, not what VSM function it may later be interpreted as testing.

Typical values:

- `native-system` — benchmark runs the first-party system boundary directly;
- `adapter-preserved` — an adapter is present but preserves the material first-party system path;
- `benchmark-scaffolded` — benchmark authors supply the material organization/mechanism under test;
- `unclear` — public evidence is insufficient to decide.

## Comparison quality

Raw observations may be grouped for comparison only where public evidence supports the grouping.

Record, where available:

- benchmark/version/task set;
- model/configuration;
- evaluator/grader;
- execution environment;
- budget/timeout/repetition policy;
- reset/adaptation policy.

Use explicit weaker classes when these are not materially matched. Do not normalize unrelated benchmark families into one universal score.

## Capability ownership annotation

Where public evidence independently supports it, a derived interpretation may additionally describe causal capability ownership as:

- `native`;
- `inherited`;
- `mixed`;
- `unclear`.

This is separate from both canonical VSM autonomy state and result provenance. A score alone does not prove which component caused the outcome.

## Shared raw record

A numeric result is stored once.

```text
raw observation: benchmark B × harness H × configuration C
        ↓
        ├── community interpretation: relevant to S1
        ├── community interpretation: relevant to S2
        ├── domain view: Coding/SWE
        └── comparison view: matched cell M
```

Derived views reference the raw observation ID instead of copying the metric into independent manually maintained databases.

The existing `system-observations/` directory is the neutral experimental seed for this model. Existing function-specific S1–S5 artifacts remain valid historical/derived research products, but they are not prerequisites for admitting a new raw benchmark ↔ system observation.

## Community/research interpretation boundary

VSM relevance is deliberately reviewable rather than baked into raw evidence identity.

A community/research annotation can reference an observation and argue, for example:

```text
observation X → S2-relevant
observation X → not direct S2
observation X → S2 + S3 proxy
observation X → no useful VSM attribution
```

OpenSiro may maintain derived experimental views from such interpretations, but the underlying benchmark-system-result record remains unchanged.

This prevents disagreement about benchmark semantics from blocking collection of objective public evidence.

## Relationship to canonical assessments

Canonical VSM assessment remains upstream and independent:

```text
repository @ pinned revision
        ↓
VSM function / ownership state
```

The registry is empirical evidence infrastructure:

```text
public benchmark result
        ↓
benchmark ↔ system linkage
        ↓
result + provenance
```

Neither changes the other automatically.

Benchmark performance cannot assign `A`, `C`, `P`, `—`, `?`, `A(P)`, or `C(P)`. A canonical autonomy state does not imply any benchmark result.

## Adaptive / self-organizing evidence

Persistent self-modification remains a separate evidence class. The registry records whether a public run appears frozen/reset, adaptive, or unknown where the protocol establishes it.

Experimental self-organizing `S` remains a separate research track and must not be inferred from a high ordinary benchmark score.

## Non-goals

- no canonical `benchmark → VSM function` taxonomy required for raw admission;
- no global harness winner;
- no scalar score across S1–S5;
- no maturity ladder;
- no forced normalization across unrelated benchmark families;
- no OpenSiro-operated benchmark runs to manufacture evidence;
- no benchmark-driven mutation of canonical VSM assessments.

## Promotion rule

If the neutral registry becomes durable infrastructure, its data/provenance schema can remain in the Index because it describes public real-system evidence.

Any normative procedure for deciding VSM-function relevance belongs in the Profile/Skills architecture rather than being silently encoded as a property of raw benchmark records.
