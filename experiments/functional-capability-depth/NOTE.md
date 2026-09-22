# Per-function capability depth beside VSM closure

Status: **non-normative research note**

This note records a hypothesis about what the VSM Harness Index does **not** measure.
It does not change the VSM Profile, assessment states, publication notation, ranking projection,
or any canonical assessment.

If this hypothesis later becomes an experimental classification or assessment procedure, that
protocol belongs upstream in `opensiro/vsm-harness-skills`; this Index repository should then hold
only the corresponding real-system evidence / fixtures / derived views.

## Observation

The canonical VSM vector answers a topological / ownership question:

> Which viable-system functions are present, and who owns the decisive closure for each function?

It deliberately does **not** answer:

> Given the same VSM function in two systems, how capable is that function in one system relative to the other?

Therefore two harnesses can both receive `S1=A` while exposing materially different S1 capability.
The same distinction can apply to `S2`, `S3`, `S3*`, `S4`, and `S5` whenever the compared systems
actually instantiate the function under a comparable boundary.

`A`, `P`, `C`, `A(P)`, and the other publication states are closure / ownership states. They are not
scalar performance scores.

## Core comparison unit

The unit of capability analysis is **one VSM function across two or more systems**.

Correct comparison shape:

```text
oh-my-pi.S1   ↔ Ouroboros.S1
oh-my-pi.S3   ↔ thClaws.S3
Ouroboros.S4  ↔ another system's S4
```

Not:

```text
oh-my-pi      ↔ Ouroboros
```

as a single global harness-capability score.

The experimental question is therefore:

```text
capability(system A, Sx)  ↔  capability(system B, Sx)
```

The canonical state remains a separate input describing whether and how that function is closed.

## Two-layer representation

```text
Layer 1 — VSM closure / ownership

              S1   S2   S3   S3*  S4   S5
system A      A    A    A(P) A    —    —
system B      A    A    A    A    A(P) A(P)

Layer 2 — per-function capability comparisons

S1: system A ↔ system B
S2: system A ↔ system B
S3: system A ↔ system B
S3*: system A ↔ system B
S4: only among systems where an S4 comparison is meaningful
S5: only among systems where an S5 comparison is meaningful
```

There is no requirement to collapse Layer 2 into one harness-wide score.

## Function-specific capability criteria

Capability criteria should be defined **per VSM function**, because the thing being regulated is different in each case.

Candidate examples:

### S1 — operational capability

Possible comparison dimensions include:

- task effectiveness under matched conditions;
- tool / environment interaction fidelity;
- state and context handling during current work;
- failure recovery;
- result verification integrated into the operational loop;
- efficiency: tokens, retries, latency, cost;
- portability across models or environments.

### S2 — coordination capability

Possible comparison dimensions include:

- detection of concrete inter-S1 interference;
- conflict attenuation effectiveness;
- coordination latency;
- locality / minimality of intervention;
- scaling across concurrent S1 units;
- recovery from coordination failure.

### S3 — current-control capability

Possible comparison dimensions include:

- observability of current commitments and operational state;
- control / intervention reach;
- resource-allocation effectiveness;
- control latency;
- exception handling;
- capacity under concurrency.

### S3* — complementary-audit capability

Possible comparison dimensions include:

- independence from the ordinary current-control path;
- inspection coverage;
- defect / anomaly detection effectiveness;
- false-positive / false-negative behavior where measurable;
- ability to trigger or require corrective action;
- evidence binding / reproducibility of findings.

### S4 — prospective-adaptation capability

Possible comparison dimensions include:

- environment sensing breadth and fidelity;
- future / scenario modelling;
- novelty and threat/opportunity discovery;
- adaptation quality;
- learning rate;
- transfer of learning into changed future capability.

### S5 — identity / policy capability

Possible comparison dimensions include:

- policy coherence;
- identity preservation under change;
- constraint coverage;
- resolution of S3↔S4 tensions;
- stability of ultimate policy across perturbations;
- controlled policy revision when revision is legitimate.

These lists are hypotheses, not a scoring specification.

## Applied-domain projections

The function capability itself should be defined at a general, application-domain-agnostic level.
Applied domains are **projections / evidence contexts**, not separate capability systems.

```text
S1 capability comparison
        ↓
        ├── Coding / SWE evidence
        ├── Research / Science evidence
        ├── Government / Public Administration evidence
        ├── Cybersecurity / Incident Response evidence
        ├── Infrastructure / SRE evidence
        └── other applied-domain evidence
```

The same principle applies to S2–S5.

A specialized domain may provide:

- a domain-specific task distribution;
- domain-specific success criteria;
- required environment / tool reach;
- domain-specific failure modes;
- evidence relevant to the VSM function under test.

It must not redefine the VSM function or silently turn a specialized-domain result into universal
capability.

Example:

```text
"oh-my-pi shows stronger S1 tool fidelity on Coding/SWE tasks"
```

is a valid specialized-domain observation.

It is not automatically equivalent to:

```text
"oh-my-pi has universally stronger S1"
```

unless the transfer to general S1 capability is independently supported.

This matches the intended Awesome split: generic organizational/capability views first, specialized
applied-domain views as projections over them.

## Capability ownership boundary

Every positive capability claim should distinguish where the capability comes from:

- `native` — implemented and owned inside the assessed first-party boundary;
- `inherited` — supplied primarily by an external host, model, runtime, tool service, IDE, or other substrate;
- `mixed` — the system adds a material first-party control/transformation over inherited capability;
- `unclear` — evidence is insufficient to assign the boundary confidently.

This matters because two systems may produce similar user-visible outcomes while owning very
different portions of the causal path.

For example, Headcount or Henterprise may have broad organizational closure while much of S1's
low-level execution capability is inherited from the host. That does not reduce their canonical S1
state; it changes what can be credited in a capability comparison.

## Evidence hierarchy

Capability depth should not become feature counting.

Prefer, in descending order:

1. reproducible fixed-model or matched-model comparisons;
2. public traces / artifacts sufficient to inspect the claimed function effect;
3. controlled ablations or before/after results attributable to a mechanism;
4. executable tests or code paths that demonstrate the mechanism;
5. primary technical documentation tied to concrete implementation;
6. maintainer claims without reproducible evidence.

Self-reported benchmark results may be recorded, but should remain labeled `self-reported` unless
independently reproduced or externally verified.

## Motivating S1 comparison

### oh-my-pi

Canonical vector at the reviewed revision:

```text
S1  S2  S3    S3*  S4  S5
A   A   A(P)  A    —   —
```

Its `S1=A` compresses a substantial first-party operational surface: repository tools, LSP-backed
editing, debugger integration, persistent code execution, model-specific tool/prompt tuning,
memory, isolated worktree subagents, structured subagent returns, and related mechanisms.

Reference:

- canonical assessment: [`assessments/oh-my-pi.md`](../../assessments/oh-my-pi.md)
- upstream: <https://github.com/can1357/oh-my-pi>

### Ouroboros

Current Full-A projection:

```text
S1  S2  S3  S3*  S4    S5
A   A   A   A    A(P)  A(P)
```

Ouroboros has broader organizational closure and a substantial first-party operational loop.
However, Full-A does not establish that `Ouroboros.S1` is more capable than `oh-my-pi.S1` on any
specific S1 criterion. That must be measured independently.

References:

- canonical assessment: [`assessments/ouroboros.md`](../../assessments/ouroboros.md)
- Full-A projection: [`FULL_A.md`](../../FULL_A.md)
- upstream: <https://github.com/razzant/ouroboros>

### Headcount

Canonical vector:

```text
S1  S2  S3  S3*  S4  S5
A   A   A   C    A   A
```

Headcount is useful because broad organizational closure does not imply deep first-party S1
execution capability. Much of the execution substrate is supplied by the host that instantiates the
skills / specialists.

Reference:

- canonical assessment: [`assessments/headcount.md`](../../assessments/headcount.md)
- upstream: <https://github.com/cbrock84/headcount>

## Comparison eligibility

Capability should only be compared where the function comparison is meaningful.

For the first experiments, prefer same-function / same-state cohorts such as:

```text
S1=A vs S1=A
```

This minimizes ambiguity about whether an apparent capability difference is actually a difference
in ownership / closure mode.

Later work may compare different publication states, but must keep the state difference explicit
and must not interpret capability as replacing the canonical classification.

A system with `S4=—` does not receive a low S4 capability score; it is simply not in an S4 capability
comparison cohort.

## Prior-art boundary

This note does **not** claim that separating structural viability from performance is new, nor that
harness benchmarking is new.

The candidate contribution to investigate is narrower:

> for each VSM function, pair an evidence-backed closure / ownership state with a separate,
> evidence-backed cross-system capability comparison for that same function, while keeping applied
> domains as projections rather than redefining the function.

## Research questions

1. Can S1 capability be compared reproducibly across systems that all have `S1=A`?
2. Which comparison dimensions are specific to S1, S2, S3, S3*, S4, and S5 respectively?
3. How should native, inherited, and mixed capability be handled in same-function comparisons?
4. Which measurements transfer across models and applied domains, and which remain domain-specific?
5. Can fixed-model experiments expose function-level harness effects large enough to be useful?
6. Does broader VSM coverage correlate with stronger capability in any particular function, or are
   closure breadth and function strength mostly independent?
7. Can specialized Awesome/domain views be generated from the same function-level evidence without
   creating incompatible taxonomies?

## Initial experiment

Batch 01 tests **S1 only** across systems whose canonical state is `S1=A`:

- `oh-my-pi`;
- `Ouroboros`;
- `thClaws`;
- `Headcount`;
- `Henterprise`;
- `Pi`.

The experiment should not produce an overall harness winner. Its purpose is to determine whether
`S1=A` systems exhibit reproducible, evidence-backed differences in **S1 capability**, and whether
those differences can be represented without corrupting the meaning of the canonical VSM state.