# Functional capability depth beside VSM closure

Status: **non-normative research note**

This note records a hypothesis about what the VSM Harness Index does **not** measure.
It does not change the VSM Profile, assessment states, publication notation, ranking projection,
or any canonical assessment.

If this hypothesis later becomes an experimental classification or assessment procedure, that
protocol belongs upstream in `opensiro/vsm-harness-skills`; this Index repository should then hold
only the corresponding real-system evidence / fixtures / derived views.

## Observation

The current VSM vector answers a topological / ownership question:

> Which viable-system functions are present, and who owns the decisive closure for each function?

It deliberately does **not** answer:

> How capable, efficient, robust, mature, or high-quality is the implementation of that function?

Therefore two harnesses can both receive `S1=A` while exposing radically different operational
capacity.

`A` means autonomous closure was established. It is not a scalar performance score.

The same distinction applies to `S2`, `S3`, `S3*`, `S4`, and `S5`.

## Motivating comparison

### oh-my-pi

Canonical VSM vector at the reviewed revision:

```text
S1  S2  S3    S3*  S4  S5
A   A   A(P)  A    —   —
```

The vector correctly captures organizational closure, but the single `S1=A` cell compresses a
large amount of execution capability into one state. The first-party harness includes, among other
things, model-facing repository tools, LSP-backed editing, debugger integration, persistent code
execution, model-specific tool/prompt tuning, memory, isolated worktree subagents, structured
subagent returns, and dedicated review surfaces.

Reference:

- canonical assessment: [`assessments/oh-my-pi.md`](../../assessments/oh-my-pi.md)
- upstream: <https://github.com/can1357/oh-my-pi>

### Ouroboros

Current Full-A projection:

```text
S1  S2  S3  S3*  S4    S5
A   A   A   A    A(P)  A(P)
```

Ouroboros has broader organizational closure than oh-my-pi, including persistent adaptation and
identity / policy closure. It also has a substantial first-party operational loop, so this is not
merely an organizational overlay.

However, Full-A alone does not imply that Ouroboros must outperform oh-my-pi on a bounded coding
S1 task. Full-A is coverage of autonomous organizational functions, not an ordering of coding-tool
quality, edit fidelity, debugging capability, context efficiency, or task success.

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

Headcount is especially useful as a counterexample to interpreting VSM coverage as functional
performance. Its organization has broad S-function coverage, while much of the low-level execution
substrate is supplied by the external host that instantiates the skills / specialists.

Thus a system may have broader organizational closure while having less first-party depth in the
execution path between model decision and world / repository mutation.

Reference:

- canonical assessment: [`assessments/headcount.md`](../../assessments/headcount.md)
- upstream: <https://github.com/cbrock84/headcount>

## Hypothesis

VSM closure and functional capability are orthogonal enough that they should not be collapsed into
one ranking.

A useful representation may therefore contain two layers:

```text
Layer 1 — organizational closure / ownership

              S1   S2   S3   S3*  S4   S5
closure       A    A    A(P) A    —    —

Layer 2 — functional capability / depth

              S1   S2   S3   S3*  S4   S5
capability    q1   q2   q3   q3*  q4   q5
```

The second layer must not be inferred from the first.

In particular:

```text
S1=A
```

means that autonomous operational closure is present. It does **not** mean that two `S1=A`
systems have comparable task success, tool fidelity, execution breadth, recovery behavior, cost,
latency, or benchmark performance.

## Candidate capability dimensions

A first exploratory decomposition for agent harnesses could include:

```text
E  execution/task effectiveness
T  tool fidelity and environment reach
C  context and memory quality
D  delegation / multi-agent execution quality
V  verification and review quality
R  recovery / resilience
O  operational maturity
B  benchmark / experimental evidence strength
```

This is intentionally a candidate list, not a scoring specification.

A per-function formulation may ultimately be cleaner than a single global harness score. For
example, `S1 capability depth` could be evaluated separately from `S3 capability depth`, while the
canonical VSM vector continues to answer only closure / ownership.

## Important methodological constraint

Capability depth should not become a feature-count score.

A harness with twenty tools is not automatically stronger than one with five. Evidence should
prefer controlled or reproducible outcomes such as:

- fixed-model harness comparisons;
- task success / pass-rate changes attributable to the harness;
- recovery from injected failures;
- edit / tool-call correctness;
- context or token efficiency;
- latency / cost under a fixed task set;
- independent verification success;
- robustness across models or environments.

Host-inherited capability should also be separated from first-party harness capability where the
boundary can be established.

## Prior-art boundary

This note does **not** claim that separating structural viability from performance is new, nor that
harness benchmarking is new. Both ideas have prior art.

The candidate contribution to investigate is narrower:

> pair an evidence-backed VSM closure / ownership profile with a separate evidence-backed
> per-function capability profile for agent harnesses, without allowing either axis to stand in for
> the other.

## Research questions

1. Can `S1 capability depth` be defined in a way that is reproducible across very different harness
   architectures?
2. Should capability be measured per VSM function or through a harness-global vector?
3. How should first-party capability be separated from capability inherited from a host model,
   coding agent, runtime, or external tool provider?
4. Which measurements transfer across models, and which are model-specific?
5. Can fixed-model experiments expose harness effects large enough to make the closure / capability
   distinction empirically useful?
6. Does a richer organizational topology improve functional capability, or are the two largely
   independent until particular failure modes appear?
7. Can the Index identify cases where a narrower VSM profile has materially stronger S1 execution
   than a near-Full-A or Full-A system?

## Initial candidate cases

The first comparison set should include at least:

- `oh-my-pi` — deep coding S1 with strong S2/S3/S3* and no established S4/S5;
- `Ouroboros` — current Full-A case with first-party persistent operation and self-adaptation;
- `Headcount` — near-Full-A organizational layer with significant host-inherited execution;
- `thClaws` — broad first-party local runtime / multi-agent platform;
- one deliberately minimal `S1=A` harness as a low-depth control.

The useful result is not an overall winner. The experiment should show whether systems sharing the
same canonical autonomy state exhibit measurably different functional depth, and whether those
differences can be represented without corrupting the meaning of the VSM profile.
