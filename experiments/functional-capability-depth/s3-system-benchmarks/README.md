# Direct S3 system benchmark coverage

Status: experimental, non-normative.

Current public-evidence state:

```text
direct S3 benchmark families: 4
direct S3 observations: 3
canonical direct S3 observations: 2
native proxy projections: 1
S3 primary baseline: gap
```

The capability layer is **public-evidence only**. Opensiro does not run or reproduce benchmark experiments on assessed harnesses to fill this gap.

## Function boundary

S3 is **inside-and-now whole-system control**. A result is relevant only when the observed organization can inspect current operational state and exercise current-control authority over ongoing work, for example through live assignment/commitment regulation, lifecycle control, resource or privilege control, scheduling, or corrective intervention.

Names are not evidence:

```text
manager / supervisor / orchestrator / delegation
                    ≠
                    S3
```

Map the organizational function first, then classify the evidence boundary.

## Current direct families

### ClawArena-Team — direct, benchmark-scaffolded

ClawArena-Team gives a benchmark-defined main agent whole-team visibility and authority over worker creation, privileges, inspection, scheduling and dynamic workflow control. It directly exercises S3 at that benchmark boundary, but the organization is supplied by the benchmark. Model rows are therefore not native S3 observations for canonical harnesses.

### Loop-Back Authority — direct, benchmark-scaffolded

The paired experiment holds the five-agent team, roles, prompts, tools, model assignment and data fixed while varying one current-control right: the hierarchical Manager may reject completed worker output and loop work back with corrective instructions, while the flat Manager must route forward. This directly exercises a benchmark-defined S3 authority relation, not LangGraph's own S3.

### Multi-Agent Orchestration native supervisor ablation — direct, canonical-native

Canonical `multi-agent-orchestration` establishes S3 through its first-party live-state supervisor. Its committed deterministic benchmark compares the same engine with that supervisor disabled versus enabled while retry and parallelism remain disabled in the clean arms.

Published result:

```text
baseline:    11 / 54 passed; routing accuracy 56.7%
supervisor:  48 / 54 passed; routing accuracy 100%
```

This is an admitted first-party-reported canonical direct S3 observation. It is a within-system ablation, not a matched cross-harness primary cell.

### SupervisorAgent / SMAS — direct, composed non-canonical

Pinned source: `LINs-lab/SupervisorAgent@ab116b557b095ae8d45bdf2d61057ce19519d4ff`.

SupervisorAgent wraps a base MAS with a meta-level runtime control relation:

```text
live interaction / current risk
        ↓
risk filter + current context
        ↓
approve / guide / correct / verify
        ↓
intervention returns into ongoing operation
```

The published GAIA pass@1 Smolagent comparison with GPT-4.1 reports:

```text
Smolagent:        50.91% average accuracy; 527.76K average tokens
Smolagent + SMAS: 50.91% average accuracy; 371.12K average tokens
reported average token reduction: 29.68%
```

This is admitted as a **direct composed S3 observation at the supervised-MAS boundary**. It is not native S3 evidence for Smolagent, AWorld or OAgents. The complete SMAS action repertoire also contains verification-like interventions, so the aggregate base-versus-SMAS result is not treated as an isolated S3-only causal estimate.

Opensiro did not execute or reproduce this benchmark.

## Second canonical direct observation: Omnigent

Canonical `omnigent` establishes `S3=A`. Later first-party operational history at post-assessment descendant revision `d8d07168c05ce1385be19dbd6ea64f4574c8d144` adds a descriptive current-control witness after parent-runner loss: unfinished children are recovered under their original child/dispatch identities, completed work remains closed, and no replacement worker is created.

This is direct descriptive canonical S3 evidence, but it is materially heterogeneous with the Multi-Agent Orchestration supervisor ablation. It must not be relabeled as evidence at the earlier canonical assessment revision.

## Native proxy: AutoGen / Magentic-One

Canonical AutoGen AgentChat establishes S3 through Magentic-One's whole-team task/progress ledger, assignments, stall detection, reset/replan and direction. The Magentic-One orchestrator ablation changes end-task performance, but it simultaneously removes S2 and S3 mechanisms and uses general task benchmarks rather than an isolated S3 disturbance. It therefore remains a native quantitative proxy, not a direct S3 observation.

## Reviewed non-primary routes

- **Astra** — strongly matched framework campaign, but Agno and AutoGen are exercised through benchmark-selected organization modes rather than the canonical S3 paths used to establish their ownership states.
- **PrincipalBench** — benchmark-defined principal plus simulated workers; useful S3-adjacent recovery/decomposition evidence, not a canonical harness current-control path.
- **OrchestraBench** — direct orchestration-failure/recovery protocol, but the organization is benchmark-defined and public evidence does not bind results to canonical native S3 implementations.
- **C.A.D.I.S., Awaken, ARES** — canonical S3 mechanisms exist, but current public result surfaces do not isolate a current-control intervention and its subsequent organizational outcome.

## Why the primary remains `gap`

The two canonical direct observations are not materially matched:

```text
Multi-Agent Orchestration
  controlled supervisor ablation
  54 scripted scenarios
  deterministic MockProvider surface

Omnigent
  descriptive operational/recovery witness
  post-assessment descendant revision
  real Polly/Codex recovery history
```

SupervisorAgent / SMAS adds useful direct S3 evidence, but at a composed non-canonical boundary.

A primary can be selected only when public evidence supplies a materially matched comparison where two or more canonical systems exercise their own native or adapter-preserved S3 paths under a common benchmark/model/configuration/evaluator surface.

## Reopen rule

Reopen the primary search when public evidence provides one of:

1. a materially matched benchmark/model/configuration cell for two or more canonical native or adapter-preserved S3 implementations;
2. an existing matched framework campaign proving that canonical S3 paths are actually active for multiple systems;
3. a new direct orchestration benchmark with immutable comparable results linked to multiple canonical native S3 systems.

Do not reopen merely for another benchmark-authored manager topology, another unmatched descriptive row, another composed non-canonical supervisor result, or microperformance/mechanism tests without current-control outcome closure.

## Source of truth

- `observations.json` — direct S3 observations, including canonical and composed/non-canonical rows;
- `coverage.json` — reviewed direct/proxy/boundary/candidate cases;
- `matched-cell/s3-primary-search-closure.json` — current gap disposition and reopen conditions;
- `validate.py` — fail-closed evidence and boundary checks;
- `../vsm-benchmark-family-map/map.json` — reviewed benchmark-family semantics.

## Non-goals

This experiment does not:

- infer S3 from labels such as `manager`, `supervisor` or `orchestrator`;
- transfer a benchmark/composed supervisor's S3 ownership to a wrapped product;
- infer canonical autonomy from benchmark performance;
- normalize heterogeneous S3 observations into one scalar score;
- run harness experiments to manufacture missing capability evidence;
- change canonical assessments, TLDRs, rankings or Full-A state.
