# Direct S3 system benchmark coverage

Status: experimental, non-normative.

Initial coverage issue: #390  
Primary-baseline search follow-up: #427

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do canonical Index systems that already establish **S3 — Inside-and-now control** have published benchmark observations that exercise their own whole-system current-control implementation under a benchmark already reviewed as `direct` for S3?

The answer may legitimately be zero.

## Current result

```text
direct S3 benchmark families reviewed: 1
native/adapter-preserved direct-S3 observations admitted: 0
S3 primary baseline: gap
```

The one committed direct family remains `ClawArena-Team`.

ClawArena-Team directly exercises S3 at its own benchmark boundary: the main agent has whole-team visibility and authority over worker creation, tools, workspace scopes, foreground/background execution, inspection, scheduling and dynamic workflow composition.

Its published leaderboard nevertheless compares **models acting as managers inside the ClawArena-Team organization**. The worker pool, management tools and organizational boundary are supplied by the benchmark. Those runs are therefore `benchmark-scaffolded` with respect to canonical OpenSiro harnesses.

## Rule — the native S3 path must actually run

A controlled benchmark does not become an S3 baseline merely because it:

- fixes one model across frameworks;
- uses a `manager`, `supervisor`, `coordinator` or `orchestrator`;
- delegates to several workers;
- measures decomposition, recovery or end-task quality.

For a canonical system-level S3 baseline, the benchmark must preserve the **same first-party current-control path that establishes S3 in the canonical assessment**.

```text
fixed model + same workload + different frameworks
                    ≠
matched native S3 implementations
```

If the benchmark substitutes a simpler framework mode, imposes its own manager organization, or bypasses the canonical S3 controller, it can still be useful framework/mechanism evidence but not a native S3 baseline row.

## Why model-manager results are not canonical harness S3 results

A row such as `gpt-*`, `claude-*`, `gemini-*` or `glm-*` in ClawArena-Team does not mean that Codex, AutoGen, DeepSeek Harness or another product's own S3 path was exercised.

The direct benchmark fit and system attribution remain separate:

```text
ClawArena-Team exercises S3 directly
             ≠
ClawArena-Team exercises Codex.S3 / AutoGen.S3 / Headcount.S3
```

## Native proxy: AutoGen / Magentic-One

Canonical AutoGen AgentChat independently establishes `S3=A` through the Magentic-One Orchestrator's whole-team task/progress ledger, agent assignments, stall detection, reset/replan and team direction.

The Magentic-One paper includes a native orchestrator ablation: replacing the full orchestrator with a simpler GroupChat-style selector removes ledgers, planning, progress tracking, loop detection and explicit direction and materially changes GAIA/AssistantBench/WebArena end-task performance.

This is strong native mechanism/ablation evidence, but it remains a proxy for direct S3 capability because:

- those benchmarks are general end-task benchmarks rather than S3 current-control disturbances;
- the ablation simultaneously removes S2 and S3 mechanisms.

It is not admitted into the direct S3 observation registry.

## Recent controlled-benchmark search

### Astra AGI five-framework benchmark — matched framework, wrong S3 paths

Pinned source: `HeeManSu/astra-agi@129b440e531af9d053645f7fab966c172bfb3b3b`.

This is a useful controlled comparison: `gemini-2.5-flash`, temperature, tools, workload and most prompts are held fixed while Astra, Agno, CrewAI, AutoGen and LangGraph vary. Trials run in fresh subprocesses and model calls are captured at the common Gemini boundary.

However, the benchmark does not exercise the canonical S3 modes:

- canonical Agno `S3=A` is established through `TeamMode.tasks`; the benchmark uses `TeamMode.coordinate`;
- canonical AutoGen AgentChat `S3=A` is established through `MagenticOneOrchestrator`; the benchmark uses `SelectorGroupChat`;
- CrewAI and LangGraph are current `S3=—` controls at their canonical boundaries.

Therefore this benchmark is retained as `framework-scaffolded` evidence, not a native S3 comparison.

### PrincipalBench — model orchestration proxy

Pinned source: `KalarisLabs/Principal-Bench@89923dd855664165813c776ca9e77ce308d969c0`.

PrincipalBench exposes useful S3-adjacent observables: decomposition quality, failure detection, adversarial recovery and context coherence over 500 multi-hop tasks and injected failures.

But `harness/pipeline.py` constructs the organization itself: `WorkerSimulator` supplies worker outputs and failures, then one model receives those outputs through a benchmark-defined principal prompt. The evaluated object does not operate a canonical harness's native worker lifecycle, assignments, current resource/priority authority, retry/replan loop or completion control.

It remains `proxy-scaffolded` evidence.

### Multi-Agent Orchestration Engine — strong native candidate, not canonical yet

Pinned source: `Vinay-veeragani/Multi-Agent-Orchestration@e6c34462af045d7e53d383103346362351c96353`.

This repository is structurally much closer to the desired S3 object. Its first-party supervisor acts against live execution state and can choose delegation, fan-out, retry, replan, approval and finalization while deterministic runtime machinery enforces budgets, permissions, concurrency, persistence and recovery boundaries.

The repository also commits a deterministic 54-scenario benchmark with baseline, supervisor, supervisor+retry and supervisor+parallel arms covering routing, fan-out, retry recovery, permission denial, human approval and budget exhaustion.

This is a strong `candidate-direct` / `native-system` S3 case **at its own boundary**. It is not currently a canonical Index system, so it cannot populate the canonical S3 observation registry or primary baseline until independent assessment/admission establishes the relevant S3 function and boundary.

### OrchestraBench — controlled failure/recovery protocol, scaffolded organization

`arXiv:2608.05263` studies orchestration failure injection, routing, cascade radius and recovery over controlled dependency chains. Its observables are strongly S3-relevant.

The reviewed public evidence still evaluates a benchmark-defined orchestration organization, and no authoritative code repository was recovered that links the reported runs to native canonical harness S3 implementations. It therefore remains a candidate protocol, not a canonical baseline row.

## Proxy: EnterpriseArena

EnterpriseArena stresses scarce-resource allocation over a long horizon and is useful for the resource-allocation dimension of S3. It remains a proxy because its CFO-style decision environment blends current regulation with prospective/environmental reasoning and is benchmark-defined rather than a native canonical harness control plane.

## Representative canonical S3 cohort inspected

The coverage layer checks mechanism-diverse canonical S3 systems, including:

- `agno` — autonomous task-board/current-control path;
- `autogen-agentchat` — autonomous whole-team progress/current control;
- `headcount` — autonomous executive/current control;
- `deepseek-harness` — parent-governed autonomous current-control path;
- `reigen` — parent-governed current-control path;
- `omnigent` — autonomous team/current control;
- `loopx` — parent-governed current control;
- `thclaws` — autonomous Team-mode current control;
- `codex` — constructor MultiAgent V2 whole-tree control;
- `pi-harness` — constructor/parent-governed current-control path.

This is a representative mechanism-diverse set, not a claim that no other canonical S3 system exists.

## S3 capability dimensions exposed by the gap

A useful future benchmark program may need several disturbance/control dimensions inside S3:

```text
S3 — Inside-and-now control
├── worker/team lifecycle control
├── live assignment and commitment regulation
├── resource/budget allocation
├── privilege/tool/workspace control
├── progress/stall/failure intervention
└── priority/scheduling control
```

These are S3 capability dimensions, not additional VSM systems and not an ordinal maturity ladder.

## What would close the primary gap

A usable S3 primary should provide at least one matched cell where:

1. two or more canonical systems independently establish S3;
2. each run exercises the exact native/adapter-preserved S3 path established by its assessment;
3. model/configuration, disturbance/task set, environment, evaluator and budget are matched strongly enough for comparison;
4. the benchmark stresses whole-system current control rather than only decomposition or delegation;
5. persistent self-improvement is excluded/reset under the ordinary frozen-repertoire rule.

Until then, `S3: gap` is the evidence-backed baseline state, not a zero capability score.

## Source of truth

- `observations.json` — admitted native/adapter-preserved direct-S3 observations; currently `[]`.
- `coverage.json` — reviewed direct/proxy/boundary/candidate cases.
- `validate.py` — checks the empty direct-observation contract, current direct-S3 map, reviewed search cases and canonical anchors.

## Non-goals

This experiment does not:

- treat delegation or a `manager` label as S3;
- attribute benchmark-owned team control to a product by model/provider name;
- infer S3 from benchmark performance;
- turn a matched framework experiment into S3 evidence when the canonical S3 mode is not exercised;
- convert management metrics into a universal S3 score;
- change canonical assessments or benchmark-family semantics.
