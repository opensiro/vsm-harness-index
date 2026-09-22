# Direct S3 system benchmark coverage

Status: experimental, non-normative.

Issue: #390

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do canonical Index systems that already establish **S3 — Inside-and-now control** have published benchmark observations that exercise their own whole-system current-control implementation under a benchmark already reviewed as `direct` for S3?

The first-pass answer may legitimately be zero.

## Current result

```text
direct S3 benchmark families reviewed: 1
native/adapter-preserved direct-S3 observations admitted: 0
```

The one committed direct family is `ClawArena-Team`.

ClawArena-Team directly exercises S3 at its own benchmark boundary: the main agent has whole-team visibility and authority over worker creation, tools, workspace scopes, foreground/background execution, inspection, scheduling and dynamic workflow composition.

Its published leaderboard nevertheless compares **models acting as managers inside the ClawArena-Team organization**. The worker pool, management tools and organizational boundary are supplied by the benchmark. Those runs are therefore `benchmark-scaffolded` with respect to canonical OpenSiro harnesses.

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

## Proxy: EnterpriseArena

EnterpriseArena stresses scarce-resource allocation over a long horizon and is useful for the resource-allocation dimension of S3. It remains a proxy because its CFO-style decision environment blends current regulation with prospective/environmental reasoning and is benchmark-defined rather than a native canonical harness control plane.

## Representative canonical S3 cohort inspected

The first pass checks mechanism-diverse canonical S3 systems, including:

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

## Source of truth

- `observations.json` — admitted native/adapter-preserved direct-S3 observations; currently `[]`.
- `coverage.json` — reviewed direct/proxy/boundary cases.
- `validate.py` — checks the empty observation contract, current direct-S3 map and representative canonical anchors.

## Non-goals

This experiment does not:

- treat delegation or a `manager` label as S3;
- attribute benchmark-owned team control to a product by model/provider name;
- infer S3 from benchmark performance;
- convert management metrics into a universal S3 score;
- change canonical assessments or benchmark-family semantics.
