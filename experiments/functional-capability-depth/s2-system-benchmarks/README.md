# Direct S2 system benchmark coverage

Status: experimental, non-normative.

Initial issue: #387  
Primary-search closure: #564  
Current direct-evidence update: #586

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do public benchmark results directly exercise **S2 — Coordination** as defined by the current Profile, and can any such results be linked to canonical Index systems without confusing benchmark-authored coordination with native harness ownership?

The functional gate is:

```text
distinct S1 units
        ↓
interaction-generated disturbance / interference
        ↓
coordination relation attenuates that disturbance
        ↓
feedback changes subsequent S1 behaviour
```

Generic communication, delegation, teamwork, topology, throughput or team success is insufficient by itself.

For a cross-harness primary baseline, the direct S2 path must additionally be native or adapter-preserved for multiple canonical systems under materially matched model/task/environment conditions.

## Current result

```text
direct S2 benchmark families reviewed:          3
direct S2 observations:                         1
canonical native direct-S2 observations:        0
native canonical proxy projections:             2
primary S2 baseline:                             gap
```

The direct families are:

- `DPBench`;
- `STALE semantic-coordination`;
- `Nool coding-agent fleet coordination`.

The single direct observation is the Nool Track D fleet-contention result at the benchmark-defined fleet boundary. It is **not** a canonical native observation.

A `gap` therefore no longer means direct S2 observations are absent. It means no materially matched primary comparison of native canonical S2 implementations is available.

## Evidence separation

The experiment preserves three independent questions:

```text
canonical repository evidence
→ establishes whether a harness owns S2

benchmark-defined direct evidence
→ can measure S2 capability at the benchmark's own organization boundary

canonical native / adapter-preserved direct evidence
→ can support a canonical S2 capability row
```

A benchmark can be direct without making the runtime/model underneath it a canonical S2 owner. Conversely, a canonical `S2=A` harness can have strong mechanism evidence without any public direct S2 capability result.

## Direct benchmark: DPBench

DPBench directly exercises simultaneous shared-resource contention. Multiple agents compete for shared resources and can deadlock; deadlock, throughput, fairness and consistency expose whether the benchmark-defined coordination organization attenuates the disturbance.

The benchmark itself supplies the philosophers, grouping, protocol and communication structure. Published model/provider rows are therefore `benchmark-scaffolded`, not native AutoGen/Headcount/DeepSeek Harness/etc. S2 observations.

## Direct benchmark: STALE semantic coordination

Pinned source:

```text
illinoisdata/STALE-bench@f7bc831e4eff08b9652acd893553824636ae3985
```

STALE creates a particularly clean semantic-interference witness: individual patches can be correct in isolation while their composition breaks tests. Controlled visibility/communication then changes whether the second worker can avoid the stale assumption.

The benchmark reports strong attenuation when a precise message exposes the finalized concurrent change, including roughly 98% reduction of synthetic interference and substantial recovery on real-derived Django tasks.

The coordination organization and information-sharing conditions are benchmark-defined. Underlying task-solving harnesses do not inherit native S2 ownership from these rows.

## Direct observation: Nool Track D fleet coordination

Pinned source:

```text
noolinc/nool_long_eval_bench@126d69b5921be71daffd38c70ec4aa77252b4f39
```

The benchmark studies many autonomous coding workers modifying one shared codebase. The Track D scale-up pre-registers three contention clusters inside a 20-ticket workload and compares uncoordinated parallel dispatch with pre-start coordination that delays footprint-overlapping tickets until the prior member integrates.

The S2 chain is explicit:

```text
parallel coding workers
        ↓
overlapping concurrent work
        ↓
merge conflicts / stale-base composition / silent poisoning
        ↓
pre-start footprint coordination
        ↓
overlapping work waits for prior integration
        ↓
later worker branches from updated shared state
        ↓
changed integration and acceptance outcomes
```

The primary N=10 comparison holds prompts, model (`claude-sonnet-5`), worker count and worktree isolation fixed:

| Arm | Run | Accepted | Clean merges | Final main |
| --- | --- | ---: | ---: | --- |
| uncoordinated git | `fleet_git_fleet_9a6eb70f` | 1/20 | 14/20 | broken |
| uncoordinated git | `fleet_git_fleet_803f2288` | 13/20 | 13/20 | green |
| coordinated | `fleet_nool_fleet_cb7ccf72` | 19/20 | 20/20 | green |
| coordinated | `fleet_nool_fleet_2a51582f` | 19/20 | 20/20 | green |

All conflicts in the two primary uncoordinated runs occur on second/third members of the designed contention clusters. The coordinated arm integrates all nine cluster tickets in both primary replicates.

The benchmark also preserves an excluded gate-hole run (`fleet_nool_fleet_16e2e1b0`) in the raw ledger and documents why it is not part of the primary comparison. A later control shows that a git-only scheduler using the same pre-start check-in relation can match the coordinated arm when declared footprints are accurate. That supports the narrow interpretation: the measured capability is the **coordination relation**, not product branding.

Raw provenance:

```text
results/trackc/fleet_runs.jsonl
results/replications/MANIFEST.md
docs/findings/2026-08-21-findings.md
```

The public repository is the benchmark/evidence package. It does not establish the external Nool runtime as a canonical Index harness, so this observation is recorded as `direct-scaffolded`, `canonical_harness_id: null`.

## Native proxy: AutoGen / Magentic-One

Canonical AutoGen AgentChat establishes S2 independently through first-party team selection plus explicit progress/loop/stall regulation.

Magentic-One's published native orchestrator ablation changes end-task performance on GAIA/AssistantBench/WebArena. This is useful quantitative evidence, but the ablation spans S2 and S3 mechanisms and the tasks do not instantiate an explicit S2 disturbance. It remains a `native-proxy` projection rather than a direct S2 observation.

## Native proxy: Squad / MARBLE

Canonical Squad now establishes `S2=A`. The public MARBLE campaign exercises Squad's first-party coordination path under controlled same-model/same-task factorial conditions, including coordination-only versus no-Squad and full-Squad versus memory-only contrasts.

That is native historical-lineage capability evidence. It remains a proxy because MARBLE reports broad collaborative completion/milestone/quality outcomes rather than a measured inter-S1 interference variable and its attenuation.

The repository also ships orchestration-log templates, but no committed real `.squad/orchestration-log/` run corpus was recovered at the reviewed revision, so templates are not promoted into a descriptive direct observation.

## Framework-scaffolded negative controls

### MAFBench / LangGraph

MAFBench contains S2-relevant distributed tasks such as conflict avoidance, matching, leader election and Byzantine consensus, but the published topology is benchmark-authored and currently hosted through LangGraph. Canonical LangGraph itself remains `S2=—`; framework expressivity does not create native S2 ownership.

### Agent Framework Benchmark

`LukaszGrochal/agent-framework-benchmark@2ce20686e939b9a065705877882bdfabdf857e27` fixes model/prompts/tools across several frameworks, but deliberately normalizes them to a sequential:

```text
Researcher → Analyst → Writer
```

pipeline. Recurring inter-S1 interference is removed rather than measured, so quality/latency/token differences are not direct S2 evidence.

### Astra cross-framework investment team

Astra provides useful matched framework/runtime measurements, including Agno and AutoGen rows, but the compared organization is benchmark-authored and the workload does not expose an explicit S2 disturbance/attenuation variable. These rows remain framework-execution evidence.

## Candidate: Twining Benchmark

Twining varies coordination conditions over multiple coding agents and includes concurrent-agent/conflict-resolution scenarios. It remains a strong candidate, but the system-in-focus is multiple external agents plus the selected coordination condition; `twining-mcp` is not currently a canonical Index system. The boundary remains unresolved for canonical capability use.

## Native mechanism without direct result: DeepSeek Agent Teams

Canonical DeepSeek Harness establishes `S2=A` through Agent Teams shared tasks/commitments and coordination machinery. Current public Agent Team code/tests demonstrate the mechanism, including overlap-related primitives, but no published capability run/result was recovered that closes an explicit inter-S1 disturbance → attenuation → changed-operation chain.

Tests and mechanism existence are not converted into a capability observation.

## Candidate: MAO-Bench

Pinned source:

```text
rachitpareek/multi-agent-orchestration-evals@3343fe1cf5a24211023a69374d31df3d6711b613
```

MAO-Bench is structurally close to a future canonical S2 comparison: parallel/sequential tiers, adversarial failure/conflict tasks, topology and parallelism metrics, hermetic execution and a multi-orchestrator adapter interface.

Its public seeded leaderboard still contains no multi-orchestrator result rows. The design is promising; the result cell does not yet exist.

## Representative canonical S2 cohort inspected

The current coverage record checks a mechanism-diverse set including:

- `autogen-agentchat`;
- `squad`;
- `headcount`;
- `deepseek-harness`;
- `reigen`;
- `omnigent`;
- `loopx`;
- `thclaws`;
- `pi-harness`;
- `reasonix`;
- `browser-harness`.

These systems span autonomous and constructor coordination paths, write-surface collision prevention, isolated-worker coordination, durable team commitments, turn/stall regulation and shared mutable-resource admission. The cohort is an inspection set, not a claim of exhaustiveness.

## Why the primary gap remains

The current state is:

```text
direct S2 benchmark-defined observation exists
        !=
canonical native direct S2 observation exists
        !=
matched canonical S2 primary exists
```

Nool closes the first observation-layer hole but not the canonical one.

A future primary still requires materially matched evidence for two or more canonical systems exercising their own native or adapter-preserved S2 paths under a common disturbance definition, with recoverable model/configuration provenance.

## Source of truth

- `observations.json` — admitted direct S2 observations; currently one non-canonical Nool Track D observation;
- `coverage.json` — reviewed direct/proxy/candidate cases and canonical linkage;
- `proxy_links.json` — native canonical proxy projections;
- `validate.py` — fail-closed separation of direct, canonical and proxy evidence;
- `matched-cell/s2-primary-search-closure.json` — current primary-gap disposition;
- `matched-cell/S2-PRIMARY-SEARCH-CLOSURE.md` — human-readable closure and reopen rule;
- `../vsm-benchmark-family-map/map.json` — benchmark-family semantic classification.

## Non-goals

This experiment does not:

- weaken S2 semantics to populate a dataset;
- turn generic communication/delegation into S2;
- infer canonical S2 ownership from benchmark performance;
- attribute benchmark-owned coordination to an underlying model/framework/product by name association;
- treat Nool's external product runtime as a canonical OpenSiro harness without a separate repository-grounded assessment;
- promote native proxy evidence into direct S2 after seeing favorable scores;
- select a primary without matched canonical native evidence;
- create a scalar S2 score or overall harness score;
- modify Profile, Skills, canonical assessments, catalog, TLDR, rankings or Full-A artifacts.
