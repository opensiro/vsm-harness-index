# Direct S3 system benchmark coverage

Status: **experimental, non-normative**.

Initial coverage issue: #390  
Primary-baseline search follow-up: #427  
SupervisorAgent / SMAS composed-evidence review: #685

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

What public evidence directly exercises **S3 — Inside-and-now control**, and which observations can be linked to canonical Index systems without confusing benchmark-authored or externally composed management with native harness ownership?

Capability evidence and canonical ownership remain separate.

## Current result

```text
direct S3 benchmark families reviewed: 4
direct S3 observations admitted:       3
canonical direct S3 observations:      2
native quantitative proxies:           1
S3 primary baseline:                   gap
```

The direct families are:

1. `ClawArena-Team` — direct benchmark-scaffolded whole-team current control;
2. `Loop-Back Authority` — direct benchmark-scaffolded reject/revise authority experiment;
3. `Multi-Agent Orchestration native supervisor ablation` — direct canonical native S3;
4. `SupervisorAgent / SMAS runtime supervision` — direct composed non-canonical S3.

The admitted observations are:

- **Multi-Agent Orchestration** — canonical native controlled supervisor ablation;
- **Omnigent** — canonical native descriptive parent/child recovery witness at a post-assessment descendant revision;
- **SupervisorAgent / SMAS** — composed non-canonical runtime-supervision result.

The S3 primary remains `gap` because the two canonical observations are not materially matched to each other. Adding a non-canonical composed row does not close that comparison gap.

## Functional rule

A benchmark is direct S3 evidence only when it establishes a current-control relation such as:

```text
current whole-system state / disturbance
        ↓
whole-team control authority observes it
        ↓
assignment / intervention / correction / resource / lifecycle decision
        ↓
decision returns into current operation
        ↓
subsequent organizational behaviour changes
```

Names such as `manager`, `supervisor`, `coordinator`, `orchestrator`, or delegation by themselves do not establish S3.

## System-linkage rule

Direct function fit does not imply native canonical attribution.

```text
benchmark directly exercises S3
        ≠
underlying framework owns that S3 relation
```

For canonical capability evidence, the measured run must exercise the same native or adapter-preserved first-party current-control path that independently establishes S3 in the canonical assessment.

A benchmark-authored manager, an external supervisory layer, or a different framework mode remains evidence for that measured organization only.

## Canonical direct observations

### Multi-Agent Orchestration

Canonical `multi-agent-orchestration` establishes `S3=A` through its first-party live-state supervisor.

Its deterministic 54-scenario evaluation compares the supervisor against a HeuristicRouter-only baseline while retry and parallelism remain disabled in both clean comparison arms. The committed result reports:

```text
baseline:   11 / 54 scenarios passed; routing accuracy 56.7%
supervisor: 48 / 54 scenarios passed; routing accuracy 100%
```

This is a controlled within-system native S3 observation. The separately retry-enabled arm is not credited to the supervisor-only S3 effect.

The result remains first-party-reported: its embedded historical run SHA no longer resolves publicly, so it is not relabeled as an independent reproduction.

### Omnigent

Canonical `omnigent` establishes `S3=A` at review ref `4d963a36...`.

A later public descendant adds a first-party child-session recovery path. After a parent runner interruption it distinguishes completed/stopped/foreign/live-elsewhere work from unfinished child commitments, restores eligible interrupted children under their original child/dispatch identities, and resumes the unfinished work without creating replacement workers.

This is a direct descriptive operational S3 observation at a **post-assessment descendant revision**. It does not rewrite the earlier canonical review ref.

The Omnigent surface is materially different from the Multi-Agent Orchestration controlled benchmark, so the two canonical rows do not form a matched primary cell.

## Direct composed observation: SupervisorAgent / SMAS

Pinned public source: `LINs-lab/SupervisorAgent@ab116b557b095ae8d45bdf2d61057ce19519d4ff` and the ICLR 2026 paper.

SupervisorAgent adds an external meta-level runtime controller around a base multi-agent system:

```text
live MAS interaction / risk
        ↓
SupervisorAgent observes current state
        ↓
approve / guidance / correction / verification
        ↓
intervention returns into present operation
        ↓
subsequent task path / resource use / outcome changes
```

The published GPT-4.1 GAIA pass@1 comparison reports:

```text
Smolagent:        50.91% average accuracy; 527.76K average tokens
Smolagent + SMAS: 50.91% average accuracy; 371.12K average tokens
reported token reduction: 29.68%
```

This is admitted as **direct composed S3 evidence at the SMAS boundary**.

It is **not** native S3 evidence for Smolagent, AWorld, or OAgents. Their names identify the base systems used inside the composed treatment; the current-control relation is supplied by the external SupervisorAgent layer.

The aggregate SMAS treatment is also not a clean isolated S3-only causal estimate: its action repertoire includes `run_verification`, which introduces verification-like behaviour overlapping S3*. The result therefore expands direct S3 capability depth without creating a canonical matched row or a universal S3 score.

Opensiro did not execute or reproduce the benchmark.

## Other reviewed direct/proxy routes

### ClawArena-Team

ClawArena-Team directly exercises whole-team visibility and control over worker creation, privileges, workspace scopes, scheduling, inspection, and dynamic workflow management.

Its model leaderboard evaluates managers **inside the benchmark-defined organization**. The management system is benchmark-scaffolded, so the rows are not native canonical-harness S3 observations.

### Loop-Back Authority

The paired experiment keeps a five-agent organization, prompts, tools, model assignment, and data fixed while enabling or removing the Manager's right to reject completed worker output and require revision.

This directly measures a benchmark-defined S3 authority relation, but LangGraph is only the execution substrate. It is not native LangGraph S3 evidence.

### AutoGen / Magentic-One proxy

The native Magentic-One orchestrator ablation removes ledgers, progress tracking, planning/replanning, loop detection, and explicit direction and changes end-task performance.

This is strong native evidence, but the intervention jointly removes S2 and S3 mechanisms and the benchmarks are broad end-task surfaces rather than isolated S3 disturbances. It remains a proxy.

### Astra matched-framework campaign

Astra holds model, tools, workload, and much of the prompt surface fixed across frameworks, but the compared Agno and AutoGen modes are not the same native S3 paths that establish canonical S3 ownership. CrewAI and LangGraph are canonical S3-negative controls.

Matched framework execution therefore does not become matched native-S3 evidence automatically.

### OrchestraBench

OrchestraBench studies routing failures, cascades, and recovery under benchmark-defined orchestration. Its protocol is S3-relevant, but current public evidence does not bind results to multiple canonical native S3 implementations.

## Representative canonical cohort

The coverage layer tracks a mechanism-diverse canonical cohort including:

- `agno`;
- `autogen-agentchat`;
- `headcount`;
- `deepseek-harness`;
- `reigen`;
- `omnigent`;
- `loopx`;
- `thclaws`;
- `codex`;
- `pi-harness`;
- `multi-agent-orchestration`;
- `cadis`;
- `awaken`;
- `ares`.

This is a representative reviewed set, not a claim that no other canonical S3 system exists.

## What would close the primary gap

A usable S3 primary requires a materially matched public cell where:

1. at least two canonical systems independently establish S3;
2. each result exercises the exact native or adapter-preserved S3 path established by its assessment;
3. task/disturbance, model/configuration, environment, evaluator, budget, and comparison protocol are sufficiently matched;
4. the measured relation is whole-system current control rather than generic delegation, decomposition, or framework overhead;
5. evidence is already public upstream/third-party evidence — Opensiro does not create the missing row by running the harness itself.

Until then, `S3: gap` is an evidence-backed comparison state, not a zero capability score.

## Source of truth

- `observations.json` — admitted direct S3 observations, including canonical and composed/non-canonical rows;
- `coverage.json` — reviewed direct/proxy/boundary cases and the representative canonical cohort;
- `matched-cell/s3-primary-search-closure.json` — current primary-gap rationale and reopen conditions;
- `validate.py` — fail-closed function-evidence validation;
- `../vsm-benchmark-family-map/map.json` — benchmark-family semantic classification.

## Non-goals

This experiment does not:

- infer S3 from manager/supervisor vocabulary;
- attribute external supervision to an underlying framework;
- infer canonical autonomy from benchmark performance;
- normalize heterogeneous S3 observations into one universal score;
- run or reproduce harness benchmarks to fill evidence gaps;
- change canonical assessments, TLDR, rankings, or Full-A state.
