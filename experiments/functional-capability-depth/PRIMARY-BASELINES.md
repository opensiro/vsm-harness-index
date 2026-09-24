# Primary benchmark baseline selection

Status: **experimental, non-normative**

Tracking issue: #409

This file records the durable rationale and selection policy used by the `functional-capability-depth` experiment. It is **not** the current-state registry for benchmark-family coverage.

The current state has explicit sources of truth:

```text
vsm-benchmark-family-map/map.json
        -> reviewed function-valid benchmark families

primary-baselines.json
        -> selected / gap decision metadata

s2-system-benchmarks/coverage.json
s3-system-benchmarks/coverage.json
s3star-system-benchmarks/coverage.json
s4-system-benchmarks/coverage.json
s5-system-benchmarks/coverage.json
        -> function-specific evidence coverage

FUNCTION-BASELINES.md
        -> deterministic cross-function status projection

S1-BASELINE.md
        -> deterministic selected S1 projection
```

Do not maintain changing benchmark-family counts, gap inventories, or numeric benchmark values manually in this file.

## Baseline rule

The baseline view is intentionally simple:

```text
1 VSM function -> 1 primary benchmark
```

A primary is selected only when current public evidence can support a matched comparison of canonical harness systems. A benchmark being function-valid is not enough by itself if the benchmark scaffold supplies the target organizational function or if the published comparison varies models rather than harnesses.

A `gap` therefore means:

> no reviewed public evidence currently satisfies the complete primary-selection gate for that VSM function.

It does **not** mean the function has zero capability or no relevant benchmark evidence.

For the current selected/gap state and current direct-family depth, use [`FUNCTION-BASELINES.md`](FUNCTION-BASELINES.md).

## Selection gate

A primary family should be:

1. **function-valid** — it measures the target VSM function rather than a nearby feature label;
2. **matched-harness** — model/configuration, tasks, environment, evaluator and resource policy can be held fixed while the harness varies;
3. **canonical-linkable** — benchmarked systems can be linked to canonical Index harnesses without importing the target function from the benchmark scaffold;
4. **frozen-repertoire compatible** — ordinary baseline observations do not silently mix persistent self-improvement across benchmark tasks into the same score;
5. **public and reproducible** — protocol and provenance are sufficient to preserve observation identity;
6. **scope-honest** — narrow applied-domain results remain domain projections rather than universal capability claims.

The distinction is:

```text
function-valid benchmark
        !=
canonical-harness observation
        !=
matched canonical-harness primary
```

This is why benchmark-defined or composed direct evidence can increase evidence depth while the primary status remains `gap`.

## S1 — selected general-primary rationale

The current S1 primary is **PawBench v1.0**. The machine-readable selection and reference cell live in `primary-baselines.json`; benchmark values live only in the shared observation layer and are projected by `S1-BASELINE.md`.

Primary source: <https://github.com/agentscope-ai/PawBench>

PawBench is suitable as the general S1 primary because it is explicitly organized as a **Model × Harness** co-evaluation benchmark. Its v1.0 design supports holding a model fixed while comparing multiple harnesses over one task/evaluation surface.

The rationale for using it as the general S1 primary rather than a Coding/SWE-only benchmark is durable:

- it spans multiple task sources and capability slices rather than only repository issue resolution;
- it explicitly exposes harness choice as a comparison variable;
- additional harness adapters can extend the matrix without redefining S1;
- its isolated task execution is compatible with the frozen-repertoire baseline rule when exact run configuration and external persistent state are preserved in observation provenance.

### Historical-lineage limit

A primary-family selection is not a claim that every published row evaluates the latest canonical Index revision.

Raw observations must preserve:

- the benchmarked harness version/configuration;
- relationship to the current canonical lineage;
- fixed model/provider/configuration;
- benchmark version and task set;
- grading mode;
- known environment or persistence caveats.

Numeric results belong in the observation layer, never in this rationale file.

## Applied-domain projections

A VSM function can have domain-specific projections without replacing its general primary.

For S1, Coding/SWE evidence currently uses a dedicated domain primary plus additional technical evidence. The exact selected family, model cell, canonical harness rows and current observations are source-derived from `primary-baselines.json` and `s1-system-benchmarks/observations.jsonl` into `S1-BASELINE.md`.

The durable rule is:

```text
general S1 capability
        ↓
        ├── Coding / SWE projection
        ├── Research / Science projection
        ├── Government / Public Administration projection
        ├── Cybersecurity / Incident Response projection
        ├── Infrastructure / SRE projection
        └── other applied-domain projections
```

A domain result can support a comparison inside that domain. It must not be promoted automatically to universal S1 capability.

## Ownership and boundary rule

Capability observations do not determine canonical VSM ownership.

For every function:

```text
canonical assessment
        -> who owns/closes the organizational function

capability evidence
        -> how the observed function performs at the declared benchmark boundary
```

A benchmark-owned coordination, management, audit, adaptation, or governance layer must not be credited to a task-solving harness merely because that harness runs inside the benchmark.

This boundary is especially important for S2-S5, where many useful public benchmarks evaluate **benchmark-defined or composed organizations** rather than native canonical-harness implementations.

## Frozen-repertoire rule

The ordinary capability baseline asks how good the **current functional repertoire** is.

This does not forbid a function from performing its ordinary organizational job. For example, an existing S4 mechanism may sense the environment, generate adaptation options and change another part of the organization during an S4 evaluation.

What an ordinary baseline must not silently include is persistent endogenous improvement of the tested function's **own decision/feedback repertoire** across benchmark tasks.

```text
Sx uses its current repertoire to perform Sx
-> ordinary capability evidence

Sx persistently changes how Sx itself decides / senses / coordinates / audits
and carries the changed regulator forward
-> separate self-organizing-S evidence
```

The self-organizing `S` experiment remains a separate evidence class rather than an extra scalar capability dimension.

## Public-evidence-first rule

Opensiro does not need to operate every benchmark itself.

The default capability path is:

```text
public benchmark / paper / leaderboard result
        ↓
provenance + observation identity
        ↓
VSM-function attribution
        ↓
ownership/boundary classification
        ↓
matched comparison where justified
```

Opensiro-operated runs are optional reproduction or validation evidence, not a prerequisite for capability ingestion.

## Replacement and expansion rule

Primary selection is not permanent.

A new benchmark may replace a primary when it offers materially stronger:

- function validity;
- canonical harness coverage;
- matched-model comparability;
- reproducibility;
- frozen-repertoire control;
- domain breadth for a general baseline.

Replacing a primary changes the derived baseline view. It does not delete historical observations or secondary/domain evidence.

Adding a new direct benchmark family should update the benchmark-family map, the relevant function coverage, and `primary-baselines.json` as required. `render_function_baselines.py --check` mechanically rejects direct-family drift between the map and gap-selection metadata.

## Reading the current experiment

Use these artifacts instead of this file for changing state:

- [`FUNCTION-BASELINES.md`](FUNCTION-BASELINES.md) — current selected/gap projection and evidence-depth counts;
- [`primary-baselines.json`](primary-baselines.json) — machine-readable primary/gap decisions;
- [`S1-BASELINE.md`](S1-BASELINE.md) — current selected S1 observations;
- function-specific `coverage.json` files — reviewed evidence and boundary decisions;
- [`vsm-benchmark-family-map/map.json`](vsm-benchmark-family-map/map.json) — current function-valid direct/proxy/unsuitable benchmark-family mapping.

This separation keeps durable methodology/rationale stable while allowing public evidence to grow without creating another manually synchronized assessment database.
