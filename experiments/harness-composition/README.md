# Harness composition experiment

Status: **experimental / non-normative**.

This directory studies whether separately assessed OSS harnesses and control substrates can be composed into a **new system-in-focus** whose VSM functions and decision ownership must then be evaluated at that new boundary.

It does **not** change canonical standalone assessments and it does not mechanically combine standalone vectors.

## Source-of-truth boundary

```text
vsm-harness-profile
    VSM semantics
        ↓
vsm-harness-skills
    canonical standalone assessment methodology
        ↓
vsm-harness-index/assessments
    accepted standalone repository-relative assessments
        ↓
experiments/harness-composition
    non-canonical composition hypotheses / prototypes / traces
```

Experimental findings here MUST NOT modify `assessments/`, `data/catalog.psv`, `data/signatures.psv`, `TLDR.md`, `RANKINGS.md`, metrics, or other released-state projections unless a separate methodology change explicitly admits composed systems.

## Provenance

This experiment was migrated from:

- `opensiro/opensiro-promotion/experiments/harness-composition/`;
- staging PR `opensiro/opensiro-promotion#51`;
- staging head `4a8fbb9af6bbf5f5b62877cdf3df1850d9fd2096`.

Promotion remains the presentation consumer for posters, video, renders and social copy. This directory owns the technical hypothesis while it remains small enough not to justify a separate repository.

## Core hypothesis

A component that is constructor-owned (`C`) in a standalone harness can potentially become agent-owned (`A`) at a newly declared composed boundary if another component owns the decisive decision right and the original constructor mechanism remains enforcement/support.

For every proposed composition verify the whole closure path:

```text
relevant disturbance / external distinction
        ↓
evidence reaches donor/component
        ↓
component owns decisive decision / feedback right
        ↓
decision crosses composition boundary
        ↓
base operation actually changes
        ↓
feedback closes into later operation
```

For a proposed `C -> A` ownership lift, use the counterfactual split:

```text
remove donor agent
    -> the same discretionary target-function decision disappears
       even if deterministic enforcement remains

remove deterministic enforcement
    -> donor decision may still exist,
       but safe/reliable execution weakens
```

If removing the donor leaves materially the same target decision, the donor was not the owner. If the donor only recommends while the base harness or operator makes the binding choice, do not infer `A`.

## Artifacts

- [`TODO.md`](TODO.md) — current experiment backlog and Raven-specific trials.
- [`candidates.psv`](candidates.psv) — component/donor registry and interface hypotheses.
- [`hypotheses.psv`](hypotheses.psv) — stack-level composition hypotheses.
- [`reference-architecture.md`](reference-architecture.md) — hypothetical composable organization architecture.

Future executable surfaces may be added under this directory, for example `adapters/`, `compositions/`, `runs/`, `traces/`, `evidence/` and experiment-local validation scripts.

## Working model

```text
operational S1 harness
    + coordination substrate
    + governance / audit / adaptation / policy component
        -> newly declared composed organization
```

A standalone component being strong for one function does **not** transfer that function automatically into the composition.

For an implemented composition ask again:

```text
who owns the decisive decision?
what concrete disturbance / variety is regulated?
what evidence crosses the component boundary?
does the result change later operation?
where does authority actually terminate?
```

## Raven as current composition base

Index PR [`#939`](https://github.com/opensiro/vsm-harness-index/pull/939) currently proposes Raven at the frozen experiment input as:

```text
S1=A / S2=C / S3=A(P) / S3*=C / S4=A / S5=P
```

The experiment treats that PR as a **provisional input**, not as permission to mutate canonical state from this directory.

The most direct composition questions are therefore:

| Target | Raven base | Donor candidate | Hypothesis |
| --- | --- | --- | --- |
| S2 | `C` stale-edit enforcement | Maestro `S2=A` | let an agentic moderator own coordination decisions while Raven's read-ledger remains enforcement |
| S2 | `C` stale-edit enforcement | Maestro + Grit | separate agentic S2 choice from stronger deterministic claim/worktree/merge enforcement |
| S3* | `C` machine-read Harness Manifest | redteam `S3*=A` | add an independent model reviewer whose verdict can block/redirect Raven after inspecting actual branch evidence |
| S3* | `C` machine-read Harness Manifest | HugAgentOS `S3*=A` | alternative read-only reviewer path that directly inspects artifacts and returns corrective verdicts |
| S5 | `P` operator-owned identity/policy | HugAgentOS `S5=A(P)` | low-confidence test of whether a model-owned project-policy mode can become legitimate ultimate authority over the composed Raven organization |
| S4 | `A` internal Analyst/Curator RSI | A-Evolve `S4=A` | not a lift: compare two autonomous adaptation loops and define arbitration if both can mutate the same harness |
| S4 | `A` internal Analyst/Curator RSI | Continual Harness `S4=A` | compare evaluator/Curator RSI with reset-free trajectory-driven refinement |
| S4 | `A` internal Analyst/Curator RSI | Utah `S4=A` | compare general harness curation with narrower durable skill/event-function capability extension |

### Current strongest hypotheses

1. `Raven + Maestro` — S2 `C -> A` ownership-lift candidate.
2. `Raven + redteam reviewer` — S3* `C -> A` ownership-lift candidate.
3. `Raven + Maestro + Grit` — explicit separation of S2 agentic choice from deterministic coordination enforcement.
4. `Raven + Maestro + redteam reviewer` — combined two-function lift after each single-function loop closes independently.
5. `Raven + HugAgentOS reviewer` — alternate S3* donor.
6. `Raven + HugAgentOS policy layer` — deliberately low-confidence S5 experiment.
7. `Raven + A-Evolve`, `Raven + Continual Harness`, `Raven + Utah` — duplicate-S4/arbitration comparisons, not S4-gap fills.

## Duplicate-function composition

When two components independently expose `A` for the same function, composition does not imply a stronger state. The composed system must define an arbitration relation or disjoint scopes.

For example, in `Raven + A-Evolve` both sides expose autonomous S4 paths. The experiment must determine whether one proposes and one selects, whether they own disjoint adaptation surfaces, or whether ownership becomes ambiguous.

## Useful component classes

- **Operational cores:** substantive S1 harnesses such as Codex or Raven.
- **Coordination substrates:** Grit-like interference attenuation below an agentic coordination owner.
- **Agentic S2 donors:** Maestro-like moderator/dispatch ownership.
- **Agentic S3* donors:** redteam or HugAgentOS reviewer paths with independent evidence and corrective return.
- **Runtime/policy substrates:** OpenShell, Agent Control Plane, Harmonist and similar mechanisms that may enforce decisions without necessarily owning them.
- **Composition glue:** HarnessRouter and LongHorizon-Harness style wrappers around external harnesses.
- **Adaptation references/donors:** Raven RSI, A-Evolve, Continual Harness and Utah.
- **Integrated references:** KADATH, Tandem, `gh-aw`, Chump and Conductor for comparison against externally assembled organizations.

The purpose of the experiment is to preserve the distinction between **mechanism, organizational function, and decisive ownership** while testing whether independently developed OSS components can close a coherent organization at a newly declared boundary.
