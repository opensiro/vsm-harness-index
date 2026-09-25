# Direct S2 system benchmark coverage

Status: experimental, non-normative.

Initial issue: #387  
Primary-search closure: #564  
Current direct-evidence update: #586  
Canonical delta review: #592  
Benchmark-family review: #622

Parent semantic review: `../vsm-benchmark-family-map/`

## Question

Do public benchmark results directly exercise **S2 — Coordination** as defined by the current Profile, and can any such results be linked to canonical Index systems without confusing benchmark-authored or non-canonical coordination with native harness ownership?

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
direct S2 benchmark families reviewed:          5
direct S2 observations:                         1
canonical native direct-S2 observations:        0
native canonical proxy projections:             2
primary S2 baseline:                             gap
```

The direct families are:

- `DPBench`;
- `STALE semantic-coordination`;
- `Nool coding-agent fleet coordination`;
- `Twining Benchmark conflict-resolution`;
- `Grit parallel-agent merge-contention`.

The single admitted direct observation is the Nool Track D fleet-contention result at the benchmark-defined fleet boundary. It is **not** a canonical native observation.

Twining adds a direct family but not another admitted observation: its committed result does not recover the exact Twining MCP/plugin treatment revision, and `twining-mcp` is not an admitted canonical Index harness.

Grit adds a fifth direct family but not another admitted observation: its first-party benchmark scripts and immutable summary claims expose a direct contention/attenuation relation, while the run-level benchmark `results/` directories are intentionally gitignored and Grit is not an admitted canonical Index harness.

A `gap` therefore does not mean direct S2 families or observations are absent. It means no materially matched primary comparison of native canonical S2 implementations is available.

## Evidence separation

The experiment preserves three independent questions:

```text
canonical repository evidence
→ establishes whether a harness owns S2

benchmark/product-boundary direct evidence
→ can establish that a public family directly measures S2-shaped disturbance/attenuation

canonical native / adapter-preserved direct evidence
→ can support a canonical S2 capability row
```

A benchmark can be direct without making the runtime/model underneath it a canonical S2 owner. A non-canonical product can also publish a direct S2 family without becoming a canonical Index harness. Conversely, a canonical `S2=A` harness can have strong mechanism evidence without any public direct S2 capability result.

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

The primary N=10 comparison holds prompts, model (`claude-sonnet-5`), worker count and worktree isolation fixed. Raw provenance is committed under `results/trackc/fleet_runs.jsonl`, `results/replications/MANIFEST.md`, and `docs/findings/2026-08-21-findings.md`.

The public repository is the benchmark/evidence package. It does not establish the external Nool runtime as a canonical Index harness, so this observation is recorded as direct non-canonical S2 evidence.

## Direct benchmark: Twining conflict resolution

Pinned benchmark review:

```text
daveangulo/twining-benchmark@b6a4d5e5890c5617376ba5c8fb7a628014296663
```

The `conflict-resolution` scenario assigns two implementation agents incompatible notification architectures. A third resolver must detect the architectural conflict, choose one approach, unify the shared codebase, preserve tests and document the decision. The scorer separately measures conflict detection, resolution quality and decision documentation.

A committed completed run exists, but it is **not admitted as a direct observation**. Its metadata pins the benchmark harness commit while leaving `twiningMcpVersion` empty; the exact MCP/plugin treatment revision is therefore not recoverable from the saved run provenance. `twining-mcp` is also not an admitted canonical Index harness.

## Direct benchmark family: Grit merge contention

Pinned source:

```text
rtk-ai/grit@0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe
```

Grit exposes a first-party coordination relation for parallel coding workers:

```text
parallel workers on shared repository state
        ↓
overlapping symbol/file work + merge contention
        ↓
first-party symbol claims / queues
        ↓
isolated worktrees
        ↓
serialized integration
        ↓
attenuated overlap and merge interference
```

The repository commits synthetic, throughput, sweep and real-agent benchmark scripts. Immutable commit `a2c48735e0a16c49ca1541c4865fce438c479405` also records first-party benchmark summary claims. This is enough to classify the family as direct S2 at the Grit product-defined boundary.

It is **not enough to admit a direct observation**. `scripts/README.md` says benchmark runs produce timestamped result directories containing logs and CSV summaries, while `scripts/.gitignore` explicitly excludes `*/results/`. The run-level ledgers required by the current observation-provenance gate are therefore not public at the pinned revision.

Grit is also not an admitted canonical Index harness. The review creates no `observation_ref`, canonical linkage, or primary selection.

## Native proxy: AutoGen / Magentic-One

Canonical AutoGen AgentChat establishes S2 independently through first-party team selection plus explicit progress/loop/stall regulation.

Magentic-One's published native orchestrator ablation changes end-task performance on GAIA/AssistantBench/WebArena. This is useful quantitative evidence, but the ablation spans S2 and S3 mechanisms and the tasks do not instantiate an explicit S2 disturbance. It remains a `native-proxy` projection rather than a direct S2 observation.

## Native proxy: Squad / MARBLE

Canonical Squad establishes `S2=A`. The public MARBLE campaign exercises Squad's first-party coordination path under controlled same-model/same-task factorial conditions. It remains a proxy because MARBLE reports broad collaborative completion/milestone/quality outcomes rather than a measured inter-S1 interference variable and its attenuation.

## Framework-scaffolded negative controls

MAFBench contains S2-relevant distributed tasks but its coordination application is benchmark-authored and hosted through LangGraph; canonical LangGraph itself remains `S2=—`.

Agent Framework Benchmark deliberately normalizes compared frameworks to a sequential Researcher → Analyst → Writer pipeline, removing recurring inter-S1 interference rather than measuring it.

Astra provides useful matched framework/runtime measurements, but its compared organization is benchmark-authored and does not expose an explicit S2 disturbance/attenuation variable.

## Native mechanism without direct result

Canonical DeepSeek Harness establishes `S2=A` through Agent Teams shared tasks/commitments and coordination machinery, but its public benchmark entry point still does not exercise that path directly.

C.A.D.I.S. and ARES also establish canonical S2 mechanisms, but reviewed public result surfaces remain performance/latency/microbenchmark oriented rather than direct disturbance-to-attenuation observations.

## Candidate: MAO-Bench

Pinned source:

```text
rachitpareek/multi-agent-orchestration-evals@3343fe1cf5a24211023a69374d31df3d6711b613
```

MAO-Bench is structurally close to a future canonical S2 comparison: parallel/sequential tiers, adversarial failure/conflict tasks, topology and parallelism metrics, hermetic execution and a multi-orchestrator adapter interface.

Its public seeded leaderboard still contains no multi-orchestrator result rows. The design is promising; the result cell does not yet exist.

## Representative canonical S2 cohort inspected

The current coverage record checks 13 mechanism-diverse canonical systems including `autogen-agentchat`, `squad`, `headcount`, `deepseek-harness`, `reigen`, `omnigent`, `loopx`, `thclaws`, `pi-harness`, `reasonix`, `browser-harness`, `cadis`, and `ares`.

The cohort is an inspection set, not a claim of exhaustiveness.

## Why the primary gap remains

```text
direct S2 benchmark family exists
        !=
admitted direct S2 observation exists
        !=
canonical native direct S2 observation exists
        !=
matched canonical S2 primary exists
```

Nool supplies the one admitted direct non-canonical observation. Twining and Grit increase reviewed direct-family coverage but fail distinct observation/canonical gates. None closes the canonical layer.

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
- run or reproduce assessed harness benchmarks to create capability-depth evidence;
- turn generic communication/delegation into S2;
- infer canonical S2 ownership from benchmark performance;
- attribute benchmark-owned or non-canonical coordination to an underlying model/framework by name association;
- promote Grit summary claims into `observations.json` without public run-level provenance;
- promote native proxy evidence into direct S2 after seeing favorable scores;
- select a primary without matched canonical native evidence;
- create a scalar S2 score or overall harness score;
- modify Profile, Skills, canonical assessments, catalog, TLDR, rankings or Full-A artifacts.
