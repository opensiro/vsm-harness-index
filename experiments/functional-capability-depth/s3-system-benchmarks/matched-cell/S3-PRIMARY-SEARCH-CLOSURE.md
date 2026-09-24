# S3 primary-search closure

Status: experimental, non-normative.  
Tracking issue: #567  
Scope: current public evidence reviewed through 2026-09-24.

## Result

```text
direct S3 benchmark families             3
canonical native direct observations     1
native quantitative proxy projections    1
matched canonical-native S3 primary      not available
S3 primary baseline                      gap
```

This closes the current public-evidence search transaction, not the possibility of future matched S3 evidence.

## Canonical native direct evidence

Canonical `multi-agent-orchestration` provides the first direct native S3 observation.

Its first-party benchmark isolates the native supervisor path against the same engine using `HeuristicRouter`, while retry and parallelism are disabled in both clean comparison arms:

| Arm | Passed | Routing accuracy |
| --- | ---: | ---: |
| Supervisor disabled | 11 / 54 | 56.7% |
| Native supervisor enabled | 48 / 54 | 100% |

This is strong within-system current-control evidence. It is still only one canonical system and therefore cannot form a matched cross-harness primary by itself.

## Direct benchmark-defined evidence

`ClawArena-Team` and the `Loop-Back Authority` experiment directly exercise S3-shaped authority:

- whole-team creation/assignment/inspection/scheduling/control;
- manager authority to reject worker output and route work back for correction.

Their S3 organization is created by the benchmark, so the results belong to the benchmark/composed boundary rather than to a canonical harness's native S3 implementation.

## Native proxy evidence

AutoGen/Magentic-One supplies quantitative native orchestrator ablations, but the removed mechanisms include progress tracking, planning/replanning, loop detection and explicit direction. The intervention spans both S2 and S3, so it remains a native proxy rather than an isolated direct S3 observation.

## Strongest matched framework negative control

Astra is a useful fixed-model framework comparison: Gemini 2.5 Flash, tools, workload and much of the prompting are held constant while the orchestration framework changes.

It nevertheless does not exercise the canonical S3 paths:

- Agno uses `TeamMode.coordinate`, not the `TeamMode.tasks` path underlying canonical S3 ownership;
- AutoGen uses `SelectorGroupChat`, not `MagenticOneOrchestrator`;
- CrewAI and LangGraph are current S3=`—` negative controls.

Therefore:

```text
matched framework execution
        !=
matched native S3 capability
```

unless the evaluated configuration actually activates the canonical current-control path.

## Other direct candidate

OrchestraBench directly studies routing, injected orchestration failures, cascade radius and recovery. Public evidence currently exposes a benchmark-defined orchestration organization rather than immutable result linkage to native canonical S3 implementations.

## Why the gap is evidence-backed

The reviewed evidence covers 11 representative canonical S3 systems and multiple current-control dimensions: lifecycle control, assignment/commitment regulation, resource allocation, privilege/workspace control, failure intervention and priority scheduling.

The missing piece is specific:

```text
second canonical native direct S3 observation
        +
materially matched task/model/configuration cell
```

It is no longer an unspecified search TODO.

## Reopen rule

Reopen when public primary evidence provides one of:

1. a second canonical native/adapter-preserved direct S3 result under a materially matched cell;
2. proof that an existing matched framework campaign actually activates canonical S3 paths for two or more systems;
3. a new direct orchestration benchmark whose immutable result rows bind to multiple canonical native S3 implementations.

Do not reopen merely for another manager-labelled benchmark, broad orchestration score or framework comparison using benchmark-authored current-control topology.

## Consequence

```text
S3 primary baseline = gap
```

This is an evidence state, not a zero S3 capability score and not a ranking derived from the single native observation.
