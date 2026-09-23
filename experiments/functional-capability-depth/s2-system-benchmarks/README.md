# Direct S2 system benchmark coverage

Status: experimental, non-normative.

Issue: #387

Latest primary-baseline search: #425

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do canonical Index systems that already establish **S2 — Coordination** have published benchmark observations that exercise their own S2 implementation under a benchmark already reviewed as `direct` for S2?

The answer is intentionally allowed to be **zero**.

A zero does not mean that the systems lack S2 capability. It means that the current public benchmark evidence does not simultaneously satisfy both gates:

```text
benchmark actually exercises S2
                +
benchmark actually uses the canonical system's own S2 path
```

For the primary baseline there is an additional comparison requirement:

```text
native canonical S2 path
        +
explicit S2 disturbance / attenuation relation
        +
matched model / task / environment across harnesses
```

## Current result

At this review point:

```text
direct S2 benchmark families reviewed: 1
native/adapter-preserved direct-S2 observations admitted: 0
primary S2 baseline: gap
```

The one committed direct family is `DPBench`.

DPBench supplies the Dining-Philosophers organization, simultaneous shared-resource contention, action protocol and communication structure itself. Its published model/provider runs therefore measure S2 capability **inside the benchmark-defined organization**. They are `benchmark-scaffolded` with respect to canonical OpenSiro harnesses and are not admitted as native system evidence.

The September 23 primary-baseline follow-up additionally reviewed controlled cross-framework/orchestration candidates. None currently closes all gates, so the gap remains deliberate rather than being filled with a weaker proxy.

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

`coverage.json` records five distinct evidence situations.

### `direct-scaffolded`

The benchmark directly exercises S2 semantics, but supplies the coordination organization itself.

Example: DPBench.

### `native-proxy`

A canonical S2 system is benchmarked through its own implementation, but the benchmark measures a broader/current task outcome rather than an explicit S2 disturbance.

Example: AutoGen/Magentic-One orchestrator ablations on GAIA/AssistantBench/WebArena. These are valuable mechanism/ablation evidence but not admitted direct S2 observations.

### `framework-scaffolded`

A benchmark uses a framework runtime to host a benchmark-authored coordination topology or workflow. This must not be confused with native S2 ownership by that framework.

Examples:

- MAFBench topology builds distributed coordination tasks through benchmark-authored LangGraph graphs while canonical LangGraph remains `S2=—`;
- Agent Framework Benchmark forces all compared frameworks into the same sequential Researcher → Analyst → Writer pipeline, so the application-level coordination structure is benchmark-authored rather than a native S2 disturbance comparison.

### `candidate-boundary-unresolved`

The benchmark or ablation is promising for coordination evidence, but the system-in-focus / canonical Index boundary or direct-S2 fit is not yet sufficient for a canonical system row.

Examples:

- Twining Benchmark;
- Squad / MARBLE controlled coordination ablation.

### `candidate-no-results`

The benchmark design is structurally promising for native orchestration comparison, but there is not yet a published matched result cell to evaluate or admit.

Example: MAO-Bench at `3343fe1cf5a24211023a69374d31df3d6711b613`.

This class is intentionally separate from a boundary problem: the evaluation design may be suitable in principle while evidence simply has not been produced yet.

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

## Controlled framework comparison that does not exercise S2

`LukaszGrochal/agent-framework-benchmark@2ce20686e939b9a065705877882bdfabdf857e27` is useful as a negative control for the primary-baseline search.

It does several things correctly for harness comparison:

- fixes the default model at Qwen3 14B;
- uses temperature 0;
- shares prompts and tools;
- compares five framework implementations;
- publishes quality, latency and token measurements.

But the workload is deliberately normalized to the same sequential three-stage pipeline:

```text
Researcher → Analyst → Writer
```

The AutoGen implementation uses `RoundRobinGroupChat` with `MaxMessageTermination(4)`, explicitly described as one round that matches the sequential pipeline.

This prevents the benchmark from becoming direct S2 evidence. It measures framework execution of a benchmark-authored workflow, not attenuation of a recurring inter-S1 interference/conflict/oscillation.

## Squad / MARBLE controlled coordination ablation

Pinned sources:

```text
tamirdresher/squad-marble-benchmark@f539d22557827292a664572536ca909ccbb4f8dc
bradygaster/squad@a1a8e1f4ec10b2dc08411009f29acf725d9ab515
```

This is one of the strongest public coordination-layer ablations found in the follow-up search:

- same Claude Opus 4.6 model in the MARBLE ablation;
- aligned tasks;
- Full Squad / Coord-only / Memory-only / No Squad conditions;
- task decomposition/routing and parallel specialists in the coordination layer;
- public raw artifacts and an aligned correctness re-run.

It is still not the S2 primary baseline.

First, MARBLE measures broad collaborative task outcomes rather than directly exposing a specific S2 disturbance and its attenuation. The result is therefore best treated as **coordination mechanism/proxy evidence**, not automatically direct S2.

Second, `bradygaster/squad` is not currently a canonical Index system. Exact repository-identity search found no current canonical entry or intake issue. The benchmark cannot be linked to a canonical S2 state until Squad is separately assessed as its own system-in-focus.

A future Squad assessment must still map its organizational functions from primary repository evidence; the benchmark result cannot establish S2 by itself.

## MAO-Bench — structurally promising, no published baseline cell yet

Pinned source:

```text
rachitpareek/multi-agent-orchestration-evals@3343fe1cf5a24211023a69374d31df3d6711b613
```

MAO-Bench is architecturally close to what an OpenSiro S2 cross-harness baseline would want:

- parallel and sequential multi-agent task tiers;
- adversarial failures, conflicts and ambiguity;
- topology and parallelism-efficiency measurements;
- persistence and recovery metrics;
- hermetic Docker environments;
- automated oracles;
- an adapter interface intended for multiple orchestrators.

Its README names Gas Town, CrewAI, AutoGen and LangGraph as seeded baseline targets. However, at the reviewed revision those leaderboard cells are unpopulated; the initial implementation provides the benchmark framework/tasks and a Claude Code baseline adapter rather than completed matched multi-orchestrator results.

So MAO-Bench is retained as a **future primary candidate**, not evidence that can populate `observations.json` today.

Promotion would require at least:

1. published result rows for multiple actual orchestrators;
2. recoverable model/configuration identity;
3. task/environment/evaluator matching across those orchestrators;
4. confirmation that the compared coordination path belongs to each system rather than the benchmark scaffold;
5. canonical Index linkage for the systems used in the baseline cell;
6. a direct S2 semantic review of the relevant task/metric subset rather than importing MAO's composite score wholesale.

## S2 mechanism classes exposed by the gap

The review suggests that one S2 benchmark family may not cover every S2 implementation form. Useful future benchmark families may need to target distinct disturbance classes while remaining inside the same VSM function:

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

## Current primary-baseline conclusion

After the controlled-orchestration follow-up:

```text
S2 primary: gap
```

The reason is now more specific than “no coordination benchmarks exist.” Public benchmarks cover several useful pieces, but none currently combines all of:

```text
explicit S2 disturbance
+ native coordination path
+ matched cross-harness comparison
+ canonical system linkage
+ published reproducible results
```

The gap should be revisited when:

- MAO-Bench or a similar adapter benchmark publishes real matched orchestrator cells;
- Squad is independently assessed and a direct-S2 benchmark surface can be isolated;
- Twining's system boundary is resolved;
- or a canonical S2 harness publishes a native matched coordination benchmark.

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
- promote MAFBench, Twining, Squad/MARBLE, Agent Framework Benchmark or MAO-Bench into the committed benchmark-family map without separate semantic review;
- attribute benchmark-owned coordination to LangGraph, AutoGen or another framework by name association;
- treat MAO-Bench's future composite score as a VSM S2 score;
- create a scalar S2 score.
