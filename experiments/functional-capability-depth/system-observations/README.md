# Shared benchmark ↔ system observations

Status: experimental, non-normative.

Issue introducing this layer: #403  
Current neutral-registry boundary: #782  
Machine-readable registry: #786  
Registry contract: [`../BENCHMARK-SYSTEM-REGISTRY.md`](../BENCHMARK-SYSTEM-REGISTRY.md)

## Purpose

This directory is the neutral raw evidence layer for public benchmark results that can be linked to concrete harness/system identities.

The raw layer records:

```text
public benchmark/result
        ↓
benchmark identity
        ↓
concrete harness/system identity
        ↓
raw result + provenance
```

It does **not** require OpenSiro to decide what VSM function the benchmark measures before the observation can be stored.

Community/research interpretations may reference the same raw observation later:

```text
published system observation
        ↓
shared raw record
        ├── possible VSM-function interpretation
        ├── domain interpretation
        └── comparison/capability view
```

Different interpretations may disagree without changing the underlying raw result.

## The raw layer answers

```text
what benchmark/version was used?
what concrete system/configuration was run?
can that system be linked to a canonical Index harness?
what model/configuration was used?
what metric/result was published?
who published it?
where is the public source/artifact?
how does the historical run relate to the current canonical revision?
was the native system path preserved or benchmark-scaffolded?
what comparison metadata/confounders are known?
```

## The raw layer does not answer

```text
which VSM function does the benchmark measure?
is the result direct/proxy evidence for S1/S2/S3/S3*/S4/S5?
is that interpretation persuasive enough to use in a capability argument?
```

Those are separate interpretation questions.

Canonical assessment independently answers which VSM functions exist and who owns their closure. Benchmark results do not change canonical autonomy states.

## Boundary requirements

Each raw record should preserve where possible:

- benchmark family/version/variant/split;
- published system name and benchmark display label;
- canonical harness ID/repository when the public provenance supports the linkage;
- benchmarked harness version/revision/configuration;
- relationship to the current canonical Index revision;
- exact model/configuration;
- metric and raw result;
- task/replicate/confidence information where published;
- publisher/source relation;
- `external-reproduced`, `first-party-reported`, or `mechanism-only` source class where applicable;
- `native-system`, `adapter-preserved`, `benchmark-scaffolded`, or `unclear` compatibility where supportable;
- comparison group/quality and known confounders;
- adaptation/reset state where the public protocol establishes it;
- primary-source and immutable-artifact provenance;
- explicit non-claims preventing causal or historical over-interpretation.

Unknown values remain unknown. Do not infer historical run metadata from current repository state.

A benchmark display label alone is not enough to establish canonical system identity. A link should be backed by recoverable public evidence such as an adapter, submission metadata, exact version/revision, or first-party artifact.

## Machine-readable registry

The raw JSON files are the source of truth. Two generated projections make the linkage easy to consume:

- [`registry.psv`](registry.psv) — compact machine-readable manifest, one row per `observation_id`;
- [`REGISTRY.md`](REGISTRY.md) — human-readable table over the same rows.

Generate them with:

```bash
python experiments/functional-capability-depth/system-observations/render_registry.py
```

Validate the raw registry with:

```bash
python experiments/functional-capability-depth/system-observations/validate.py
python experiments/functional-capability-depth/system-observations/render_registry.py --check
```

The generated manifest deliberately contains identity/provenance metadata only. Heterogeneous numeric benchmark payloads remain in their raw JSON record and are not copied into a second manually maintained result database.

The neutral validator checks global `observation_id` uniqueness, public HTTPS provenance, canonical linkage shape when present, supported source/compatibility classes, and recoverable benchmark identity. It does **not** require a `function`, `benchmark_fit`, canonical S-state, or VSM interpretation.

## Source-of-truth rule

A numeric result belongs in one raw observation record.

Function-specific, domain-specific, or comparison views should reference `observation_id` / `ablation_id` instead of copying the benchmark metric.

Existing records may contain historical interpretation notes introduced before #782. Those notes are not part of raw observation identity and must not be treated as canonical benchmark semantics. New raw admissions should keep VSM-function relevance in separate derived/community interpretation artifacts.

## Relationship to existing function-specific experiment artifacts

The existing S1–S5 benchmark maps, projections, coverage records, and primary-gap closures remain useful historical/derived research outputs from `functional-capability-depth`.

They are **not** admission prerequisites for this raw registry.

The direction after #782 is:

```text
raw benchmark ↔ system evidence first
        ↓
optional/revisable interpretation later
```

This layer is experimental evidence infrastructure, not a leaderboard, not a second canonical assessment database, and not a canonical taxonomy of benchmark meaning.
