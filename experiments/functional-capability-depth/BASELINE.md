# Per-function capability baseline rules

Status: **experimental, non-normative**

Tracking issues: #406, #452

Public-evidence operating contract: [`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md).

This document defines a simple baseline for comparing harness capability beside canonical VSM closure and ownership.

It does not change the VSM Profile, released assessment states, canonical assessments, rankings, or the separate self-organizing-autonomy experiment.

Current primary-family selections and explicit gaps are recorded in [`PRIMARY-BASELINES.md`](PRIMARY-BASELINES.md), with a machine-readable projection in [`primary-baselines.json`](primary-baselines.json).

## Operating mode — public evidence first

The default capability source is public benchmark evidence, not Opensiro-operated execution.

```text
public result
    ↓
provenance + normalization
    ↓
function attribution
    ↓
matched comparison where supported
    ↓
capability projection
```

A published observation may come from an independent benchmark operator or from the harness project itself. Preserve the evidence-source class and provenance explicitly.

Opensiro-operated runs are optional validation/reproduction evidence. They are useful when a specific uncertainty requires reproduction or ablation, but they are not required to admit a capability observation or select a primary benchmark family.

The frozen Batch 02 controlled-replication artifacts remain historical experiment evidence and are not a prerequisite for this baseline.

## Baseline shape

For the baseline view:

```text
1 VSM function -> 1 primary benchmark
```

This is a rule for keeping the comparison view simple. It is **not** a rule that a function may only have one benchmark.

The underlying evidence model remains one-to-many:

```text
Sx
  primary benchmark      <- baseline view
  secondary benchmarks   <- additional evidence
  domain projections     <- applied-domain evidence
```

Do not automatically average several benchmark families into one composite score.

## Rule 1 — compare one VSM function at a time

The capability comparison unit is:

```text
capability(system A, Sx) <-> capability(system B, Sx)
```

Do not turn S1-S5 into one universal harness score.

Canonical states such as `A`, `C`, `P`, `A(P)`, `C(P)`, `—`, and `?` remain a separate layer describing closure and ownership.

A function with canonical state `—` does not receive a low capability score. It is outside that function's capability cohort.

## Rule 2 — keep the comparison cell matched

A baseline comparison should use evidence that keeps constant, as far as the published record allows:

- model and model configuration;
- benchmark version and task set;
- execution environment;
- evaluator or grader;
- budget, timeout, and repetition policy.

The harness/system is the intended varying factor.

If these conditions are not matched or cannot be reconstructed, keep the result as observational, descriptive, partially matched, or proxy evidence with explicit confounders rather than treating it as a baseline-comparable harness result.

The Index does not need to rerun a public benchmark merely because some metadata are unavailable; unavailable fields remain explicit evidence limits.

## Rule 3 — one primary benchmark does not exclude more benchmarks

Each VSM function may have several reviewed benchmark families.

The baseline view chooses one `primary` benchmark family for simplicity. Other accepted families can remain available as:

- secondary evidence;
- robustness checks;
- mechanism-specific evidence;
- alternative environments;
- future replacement candidates for the primary baseline.

Changing the primary benchmark must not delete or rewrite historical observations.

## Rule 4 — applied domains are projections

Domain-specific evaluation is a projection over the same VSM function, not a new VSM function.

Example:

```text
S1
  general baseline
  coding / SWE
  research / science
  cybersecurity
  infrastructure / SRE
```

A domain benchmark must not redefine S1-S5.

A domain result can support a statement such as:

> system A shows stronger S1 capability on Coding/SWE tasks under benchmark B

It does not automatically support:

> system A has universally stronger S1 capability

Domain-specific indexes or views may therefore be generated independently from the same canonical function and raw observation layers.

## Rule 5 — ordinary baseline observations use a frozen functional repertoire

This rule matters when a harness may support the experimental self-organizing `S` distinction.

An ordinary capability baseline measures the quality of the harness's **current functional repertoire**. It should not also measure the harness's ability to improve that repertoire across benchmark tasks.

For an admitted public result, inspect the published benchmark protocol and preserve whether task isolation/reset prevents persistent cross-task adaptation. For an optional Opensiro-operated reproduction, enforce the same rule directly.

For baseline-comparable observations:

- ordinary within-task reasoning and tool use are allowed;
- retry and recovery inside the task are allowed;
- transient context and state inside the episode are allowed;
- persistent endogenous changes to the tested function's repertoire must not carry into later benchmark tasks.

Examples of persistent changes that should be disabled, reset, isolated, or explicitly marked as adaptive include:

- learned or newly generated skills;
- persistent prompt or policy rewrites;
- new orchestration or control rules;
- persistent toolset changes;
- self-generated code or configuration changes that alter later functional behavior;
- persistent learned memory used as a new regulator for later tasks.

If the public evidence does not establish repertoire isolation, record the limitation rather than assuming a frozen baseline.

If adaptation is intentionally part of the benchmark, record the observation as adaptive and non-baseline-comparable instead of silently mixing it into the ordinary baseline.

## Rule 6 — adaptive and self-organizing evaluation stays separate

The ordinary capability baseline and the self-organizing experiment answer different questions:

```text
ordinary capability baseline:
How good is the current Sx repertoire?

self-organizing experiment:
Can Sx endogenously improve its own repertoire and later close relevant variety through the changed repertoire?
```

Adaptive evaluation may later measure:

- capability before and after adaptation;
- adaptation cost;
- tasks or experience required before improvement;
- retention;
- transfer to related disturbances;
- regressions elsewhere;
- escalation-boundary shifts.

Those observations belong to a separate evidence class.

Do not infer experimental `S` from a high ordinary benchmark score.

Do not directly compare an adaptive run with a frozen baseline run.

Ordinary retry or recovery within one task is not, by itself, experimental `S` and should not be disabled merely to satisfy the frozen-repertoire rule.

## Rule 7 — raw benchmark observations stay shared

One published benchmark result may be relevant to more than one VSM function.

Store the numeric result once in the shared raw observation layer. Function-specific layers should reference the same observation ID and interpret it separately.

Example:

```text
published system observation
        ↓
shared raw record
        ├── S2 projection
        └── S3 projection
```

Do not create separate manually maintained copies of the same metric for each function.

## Rule 8 — preserve version and provenance identity

A capability observation should identify, where available:

- canonical harness ID;
- benchmarked harness version, revision, and configuration;
- relationship to the current canonical assessment revision;
- model and model configuration;
- benchmark version and split;
- execution environment;
- budget, timeout, and repetition settings;
- metric and result;
- publisher and evidence-source class (`external-reproduced`, `first-party-reported`, or non-numeric `mechanism-only` where appropriate);
- primary/immutable artifact source;
- system compatibility class such as `native-system` or `adapter-preserved`;
- comparison class and known confounders.

Unknown provenance remains unknown; do not infer it from current repository state.

A historical benchmark result remains historical evidence. It must not be represented as if it evaluated the current canonical review revision.

## Relationship to experimental self-organizing `S`

The self-organizing-autonomy experiment remains independent from this baseline.

Experimental `S` is not another capability dimension beside S1-S5 and is not equivalent to S4.

The current experimental `S` procedure first requires the ordinary VSM function and its released ownership state to be established, then asks whether that function can endogenously improve its own decision/feedback repertoire and later close relevant variety through the changed repertoire.

Therefore the capability baseline remains usable whether a system:

- has a released state such as `A`;
- later supports an experimental `S` hypothesis for that function;
- does not support the `S` hypothesis at all.

A system may have strong S4 capability without supporting experimental `S`. A function may also support experimental `S` with internal help from S4 without that automatically establishing `S4=S`.

## Scalable representation

A future derived view can remain simple:

```text
Harness X

S1
  state: A
  baseline:
    primary_benchmark: Benchmark A
    fixed_model: Model M
    result: ...
    evidence_source: external-reproduced

  secondary:
    Benchmark B: ...
    Benchmark C: ...

  domains:
    coding: ...
    research: ...

  self_organizing:
    separate experimental evidence
```

The important separation is:

```text
canonical VSM state
        ↓
public function capability evidence
        ↓
primary / secondary / domain projections

optional:
controlled reproduction / validation

separate track:
self-organizing adaptation evidence
```

## Gap semantics

A primary `gap` means that reviewed public evidence does not currently support a selected matched canonical-harness primary for that function.

It does not mean that the function has zero capability, that no benchmark evidence exists, or that Opensiro has failed to operate its own benchmark.

Do not create an Opensiro-run benchmark merely to fill a gap.

## Promotion boundary

This file is an Index research contract, not released assessment methodology.

If these baseline rules become a formal evaluation procedure, that procedure belongs upstream in `opensiro/vsm-harness-skills`. The Index should continue to hold public real-system evidence, benchmark observations, provenance, optional reproduction evidence, and derived experimental views.
