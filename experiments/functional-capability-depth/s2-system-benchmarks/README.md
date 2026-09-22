# Direct S2 system benchmark coverage

Status: experimental, non-normative.

Issue: #387

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do canonical Index systems that already establish **S2 — Coordination** have published benchmark observations that exercise their own S2 implementation under a benchmark already reviewed as `direct` for S2?

The first-pass answer is intentionally allowed to be **zero**.

A zero does not mean that the systems lack S2 capability. It means that the current public benchmark evidence does not simultaneously satisfy both gates:

```text
benchmark actually exercises S2
                +
benchmark actually uses the canonical system's own S2 path
```

## Current result

At this review point:

```text
direct S2 benchmark families reviewed: 1
native/adapter-preserved direct-S2 observations admitted: 0
```

The one committed direct family is `DPBench`.

DPBench supplies the Dining-Philosophers organization, simultaneous shared-resource contention, action protocol and communication structure itself. Its published model/provider runs therefore measure S2 capability **inside the benchmark-defined organization**. They are `benchmark-scaffolded` with respect to canonical OpenSiro harnesses and are not admitted as native system evidence.

## Why this is not a failure

Repository-grounded S2 evidence and benchmark evidence answer different questions.

For example, current canonical systems already include concrete S2 mechanisms such as:

- write-surface and shared-file interference attenuation;
- worktree/isolation-based collision avoidance;
- durable shared commitments and controlled turn/task ownership;
- explicit loop/stall suppression;
- concurrency/admission queues for shared host resources.

Those mechanisms remain valid canonical evidence even when no public direct S2 benchmark has exercised them.

The experiment therefore preserves:

```text
canonical S2 ownership
        ↓
first-party mechanism evidence ────────┐
                                       ├── later S2 capability synthesis
native direct-S2 benchmark evidence ──┘
```

and does not replace the missing lower channel with a proxy score.

## Coverage classes

`coverage.json` records four distinct evidence situations.

### `direct-scaffolded`

The benchmark directly exercises S2 semantics, but supplies the coordination organization itself.

Example: DPBench.

### `native-proxy`

A canonical S2 system is benchmarked through its own implementation, but the benchmark measures a broader/current task outcome rather than an explicit S2 disturbance.

Example: AutoGen/Magentic-One orchestrator ablations on GAIA/AssistantBench/WebArena. These are valuable mechanism/ablation evidence but not admitted direct S2 observations.

### `framework-scaffolded`

A benchmark uses a framework runtime to host a benchmark-authored coordination topology. This must not be confused with native S2 ownership by that framework.

Example: MAFBench topology currently builds distributed coordination tasks through benchmark-authored LangGraph graphs while canonical LangGraph remains `S2=—`.

### `candidate-boundary-unresolved`

The benchmark itself appears to contain direct S2 disturbances and controlled coordination conditions, but the system-in-focus / canonical Index boundary is not yet established.

Example: Twining Benchmark.

## Representative canonical S2 cohort inspected

The first pass explicitly checked high-signal canonical S2 systems/mechanism classes, including:

- `autogen-agentchat` — autonomous team turn/loop/stall regulation;
- `headcount` — autonomous write-surface coordination;
- `deepseek-harness` — autonomous Agent Teams durable commitments/shared task coordination;
- `reigen` — autonomous parallel edit-scope collision prevention;
- `omnigent` — autonomous dependency-aware isolated-worker coordination;
- `loopx` — autonomous peer coordination;
- `thclaws` — autonomous Team-mode teammate interference regulation;
- `pi-harness` — constructor shared-file interference coordination;
- `reasonix` — constructor serialization of overlapping subagent write claims;
- `browser-harness` — constructor serialization/isolation of shared mutable browser state.

This is a mechanism-diverse inspection set, not a claim that no other canonical S2 system exists.

## Direct benchmark: DPBench

DPBench is retained as `direct` because its disturbance is explicit: multiple agents simultaneously contend for shared resources and can deadlock; deadlock, throughput, fairness and message/action consistency expose whether coordination attenuates the disturbance.

However, the benchmark API takes a model callback while DPBench defines the philosophers, grouping, protocol and coordination environment. Published model results are therefore not native AutoGen/Headcount/DeepSeek Harness/etc. S2 observations.

## Native proxy: AutoGen / Magentic-One

Canonical AutoGen AgentChat establishes `S2=A` independently through first-party team selection plus explicit progress/loop/stall regulation.

Magentic-One's published evaluations include a native orchestrator ablation: a simpler GroupChat-style selector removes progress tracking, loop detection and explicit direction and materially changes end-task performance on GAIA/AssistantBench/WebArena.

That is strong first-party **mechanism/ablation evidence**, but:

- the benchmark tasks are general task-success benchmarks rather than S2 disturbance benchmarks;
- the ablation changes mechanisms spanning both S2 and S3.

It is therefore not inserted into the direct S2 observation registry.

## Framework-scaffolded negative control: MAFBench / LangGraph

MAFBench's topology module contains S2-relevant distributed tasks: graph coloring with conflict avoidance, matching, vertex cover, leader election and Byzantine consensus.

The published implementation currently uses benchmark-authored graph builders and lists LangGraph as its completed framework integration. Canonical LangGraph itself remains `S2=—`: generic graph/routing expressivity does not establish first-party S2 ownership.

Therefore a successful MAFBench/LangGraph run can demonstrate coordination in the benchmark-authored application without becoming evidence for `LangGraph.S2`.

MAFBench still deserves a separate benchmark-family semantic review; it is not silently added to the committed map here.

## Direct-S2 candidate: Twining Benchmark

Twining Benchmark is a promising follow-up because it holds a common Claude-agent/codebase substrate while varying coordination conditions such as baseline/shared files/structured state/full Twining. Its scenario set includes concurrent agents and conflict resolution, which are much closer to explicit S2 disturbances than generic teamwork scores.

However, the current system boundary is unresolved:

- `twining-mcp` is primarily a coordination MCP/plugin surface providing shared blackboard, decisions, warnings and handoff state to external agents;
- the benchmarked organization is multiple Claude agents plus the selected coordination condition;
- `twining-mcp` is not currently a canonical Index system.

Therefore Twining is recorded only as a benchmark-family candidate pending separate semantic and system-boundary review.

## S2 mechanism classes exposed by the gap

The first pass suggests that one S2 benchmark family may not cover every S2 implementation form. Useful future benchmark families may need to target distinct disturbance classes while remaining inside the same VSM function:

```text
S2 — Coordination
├── shared-resource contention / deadlock
│   └── DPBench-like
├── parallel code/write collision
│   └── concurrent-agent / conflict-resolution coding benchmarks
├── team loop/stall/turn interference
│   └── direct team-progress disturbance benchmarks
└── host-resource saturation / admission contention
    └── concurrency/resource-allocation stress benchmarks
```

These are capability subdimensions, not new VSM systems and not a maturity scale.

## Source of truth

- `observations.json` — admitted native/adapter-preserved direct-S2 observations. It is currently an empty list.
- `coverage.json` — reviewed coverage/gap cases and their boundary classification.
- `validate.py` — checks the empty/non-empty observation contract, controlled vocabularies and canonical anchors used in coverage cases.

## Non-goals

This experiment does not:

- weaken S2 semantics to populate a dataset;
- turn generic communication/delegation into S2;
- infer S2 from benchmark performance;
- change canonical assessments;
- promote MAFBench or Twining into the benchmark-family map without separate semantic review;
- attribute benchmark-owned coordination to LangGraph, AutoGen or another framework by name association;
- create a scalar S2 score.
