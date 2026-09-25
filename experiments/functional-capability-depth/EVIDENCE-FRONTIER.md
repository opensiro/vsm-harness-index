# Current Functional Capability Evidence Frontier

Generated current-state projection from `primary-baselines.json` and the function-level public-evidence closure records.

This file is **not** the historical experiment synthesis. `SYNTHESIS.md` and `experiment-state.json` preserve the closed research-cycle snapshot; this projection moves only when the current function-level source records move.

It is also not a second evidence database: every state, count, blocker and reopen rule below is read from an existing source-of-truth artifact.

## Current frontier

| Function | Primary state | Current evidence depth | Reviewed through | Source |
| --- | --- | --- | --- | --- |
| S1 | `selected` — PawBench v1.0 / `qwen3.6-35b-a3b` | `task_count`: `150` · `canonical_harnesses`: `3` | `2026-09-23` | [`primary-baselines.json`](primary-baselines.json) |
| S2 | `gap` | `direct_benchmark_families`: `7` · `direct_observations`: `3` · `canonical_direct_observations`: `0` · `native_proxy_projections`: `2` · `representative_canonical_s2_systems_inspected`: `16` | `2026-09-25` | [`s2-primary-search-closure.json`](s2-system-benchmarks/matched-cell/s2-primary-search-closure.json) |
| S3 | `gap` | `direct_benchmark_families`: `3` · `canonical_direct_observations`: `1` · `native_proxy_projections`: `1` · `representative_canonical_s3_systems_inspected`: `14` | `2026-09-25` | [`s3-primary-search-closure.json`](s3-system-benchmarks/matched-cell/s3-primary-search-closure.json) |
| S3* | `gap` | `direct_benchmark_families`: `5` · `composed_direct_observations`: `3` · `canonical_direct_observations`: `2` | `2026-09-24` | [`s3star-primary-search-closure.json`](s3star-system-benchmarks/matched-cell/s3star-primary-search-closure.json) |
| S4 | `gap` | `canonical_native_observations`: `2` · `reviewed_routes`: `6` | `2026-09-25` | [`s4-primary-search-closure.json`](s4-system-benchmarks/matched-cell/s4-primary-search-closure.json) |
| S5 | `gap` | `reviewed_cases`: `14` · `direct_benchmark_families`: `1` · `composed_direct_observations`: `1` · `canonical_direct_observations`: `1` · `representative_canonical_s5_systems`: `5` | `2026-09-25` | [`s5-primary-search-closure.json`](s5-system-benchmarks/matched-cell/s5-primary-search-closure.json) |

A `gap` is an empirical evidence state, not a zero capability score and not a statement about canonical VSM ownership.

## S1 — selected primary

- **Primary family:** PawBench v1.0 (`pawbench`).
- **Reference model:** `qwen3.6-35b-a3b`.
- **Comparison design:** `matched-model-cross-harness`.
- **Canonical harnesses in the first cell:** `qwenpaw`, `openclaw`, `hermes-agent`.
- **Primary source:** https://github.com/agentscope-ai/PawBench.
- **Provenance note:** Published PawBench rows predate the current September 2026 canonical review refs; later observations must preserve the published harness versions and historical-lineage relation explicitly.
- **Source:** [`primary-baselines.json`](primary-baselines.json).

## S2 — current `gap` frontier

- **Reviewed through:** `2026-09-25`.
- **Primary blocking reason:** Reviewed direct S2 evidence now includes seven disturbance/attenuation families. Nool and The Specification Gap provide two benchmark-scaffolded direct non-canonical observations, while CodeCRDT provides one descriptive direct observation at its own external native product boundary. Twining lacks recoverable exact treatment revision, and CooperBench lacks the pinned flash-run logs needed for observation admission. CodeCRDT has no matched uncoordinated-parallel control and is not a canonical Index harness. Public evidence still provides no canonical native direct S2 observation and no matched comparison of native S2 implementations across multiple canonical harnesses.
- **Closure claim:** Current public evidence contains seven direct S2 disturbance/attenuation families, three direct non-canonical observations, and two native quantitative S2 proxy projections. CodeCRDT expands direct evidence to an external first-party native product boundary, but the current reviewed canonical cohort, now including Lime, still contains no canonical native direct observation and no matched canonical-harness S2 primary cell.
- **Evidence depth:**
  - `direct_benchmark_families`: `7`
  - `direct_observations`: `3`
  - `canonical_direct_observations`: `0`
  - `native_proxy_projections`: `2`
  - `representative_canonical_s2_systems_inspected`: `16`
- **Reopen when:**
  1. a canonical S2 harness publishes an explicit native inter-S1 disturbance-to-attenuation result
  1. a materially matched benchmark evaluates two or more canonical systems exercising their own native or adapter-preserved S2 paths under one disturbance definition
  1. MAO-Bench or a comparable benchmark publishes recoverable multi-orchestrator results with immutable system/model/configuration provenance and direct S2 semantics
- **Do not reopen for:**
  - another benchmark-scaffolded direct S2 observation without canonical native or adapter-preserved linkage
  - another broad collaboration or task-success score without an explicit S2 disturbance
  - another topology or framework benchmark whose coordination organization is benchmark-authored
  - another communication or token-efficiency metric without disturbance-to-attenuation closure
- **Non-claim:** This closure is not a zero S2 capability score and does not downgrade canonical S2 ownership. Nool and The Specification Gap provide direct evidence only for their benchmark-defined organizations. CodeCRDT provides direct descriptive evidence for its own external native product boundary, but it has no canonical Index identity and its sequential-versus-parallel study does not estimate a causal coordination uplift versus an uncoordinated-parallel control. Twining and CooperBench contribute direct-family coverage without admitted observations for their recorded provenance reasons. Lime contributes a canonical constructor S2 mechanism without a direct capability observation. The S2 primary remains frozen until materially new canonical native or matched evidence appears.
- **Source:** [`s2-primary-search-closure.json`](s2-system-benchmarks/matched-cell/s2-primary-search-closure.json).

## S3 — current `gap` frontier

- **Reviewed through:** `2026-09-25`.
- **Primary blocking reason:** Reviewed direct S3 families now include a canonical native within-system current-control ablation, but public evidence still does not provide a matched comparison of native S3 implementations across multiple canonical harnesses under one common benchmark/model/configuration cell.
- **Closure claim:** Current public evidence contains direct S3 benchmarks and one canonical native direct S3 observation. Post-closure review of C.A.D.I.S., Awaken and ARES adds native mechanism coverage but no new direct capability observation, so no materially matched comparison of multiple canonical native or adapter-preserved S3 implementations exists.
- **Evidence depth:**
  - `direct_benchmark_families`: `3`
  - `canonical_direct_observations`: `1`
  - `native_proxy_projections`: `1`
  - `representative_canonical_s3_systems_inspected`: `14`
- **Reopen when:**
  1. a second canonical native or adapter-preserved direct S3 observation appears under a materially matched benchmark/model/configuration cell
  1. an existing matched framework campaign proves that canonical S3 paths are actually active for two or more systems
  1. a new direct orchestration benchmark binds immutable results to multiple canonical native S3 implementations
- **Do not reopen for:**
  - another benchmark-authored manager topology
  - another whole-task orchestration score without isolated current-control attribution
  - another framework comparison that does not activate canonical S3 paths
  - microperformance or mechanism tests that do not measure a current-control intervention and subsequent organizational outcome
- **Non-claim:** This closure is not a zero S3 capability score and does not generalize the single Multi-Agent Orchestration result into a cross-harness ranking. It freezes the reviewed current canonical/public-evidence state until materially new matched-native evidence appears.
- **Source:** [`s3-primary-search-closure.json`](s3-system-benchmarks/matched-cell/s3-primary-search-closure.json).

## S3* — current `gap` frontier

- **Reviewed through:** `2026-09-24`.
- **Primary blocking reason:** Reviewed direct S3* evidence now includes two canonical native systems: AppliedScientist provides quantitative within-system weakness-closure measurements, while data-to-paper provides a first-party published descriptive reviewer→revision closure witness. These observations use different tasks, models, evaluators and result surfaces, so public evidence still does not provide a materially matched comparison of native S3* implementations across multiple canonical harnesses.
- **Closure claim:** Current public evidence contains direct canonical native S3* observations and matched whole-system comparisons, but no materially matched comparison in which multiple canonical native or adapter-preserved complementary-audit paths are actually active and measured.
- **Evidence depth:**
  - `direct_benchmark_families`: `5`
  - `composed_direct_observations`: `3`
  - `canonical_direct_observations`: `2`
- **Reopen when:**
  1. a public study evaluates two or more independently canonical-linkable systems with their native or adapter-preserved S3* paths active under one matched task/model/evaluator cell
  1. an existing matched study publishes configuration or trajectory evidence proving native S3* activation for multiple canonical systems
  1. an immutable result directly compares discrepancy detection, corrective return and re-verification across multiple canonical systems
- **Do not reopen for:**
  - another benchmark-supplied external reviewer loop
  - another whole-system paper-quality leaderboard without native S3* path activation
  - another heterogeneous single-system reviewer-revision result
- **Non-claim:** This closure is not a zero S3* capability score, not a claim that matched evidence can never appear, and not a ranking. It freezes the reviewed public-evidence state until materially new primary evidence changes the matched-native condition.
- **Source:** [`s3star-primary-search-closure.json`](s3star-system-benchmarks/matched-cell/s3star-primary-search-closure.json).

## S4 — current `gap` frontier

- **Reviewed through:** `2026-09-25`.
- **Primary blocking reason:** Direct S4 evidence now includes two canonical native systems: A-Evolve publishes harness-updating measurements across SWE-bench Verified, MCP-Atlas and SkillsBench, while KADATH publishes a ten-epoch locked-benchmark population-improvement run. Their tasks, benchmark definitions, models/configurations and result surfaces are not matched, so public evidence still does not provide a common cross-harness S4 comparison cell.
- **Closure claim:** The current public evidence contains canonical native S4 observations and materially matched paper-level comparisons, but no route satisfies the full matched canonical-harness primary gate. Post-closure ARES review adds a canonical S4=C(P) mechanism with no admitted capability result; its GA/runtime reports measure computational cost rather than future capability improvement after adaptation.
- **Evidence depth:**
  - `canonical_native_observations`: `a-evolve`, `kadath`
  - `reviewed_routes`: `6`
- **Reopen when:**
  1. a blocked provenance or common-membrane gate is resolved by new public primary evidence
  1. a new public study exposes two or more independently canonical-linkable S4 systems under one benchmark/model/configuration cell
  1. an adapter-preserved common execution membrane becomes publicly established for existing canonical systems
- **Do not reopen for:**
  - another heterogeneous single-system S4 result
  - another benchmark-defined evolver without canonical-native linkage
  - method-name similarity without immutable implementation provenance
  - GA or runtime microperformance measurements without future capability improvement after adaptation
- **Non-claim:** This closure is not a claim that a matched S4 primary can never exist, not a zero capability result, and not a ranking. It freezes the reviewed current canonical/public-evidence state until materially new primary evidence changes a blocked gate.
- **Source:** [`s4-primary-search-closure.json`](s4-system-benchmarks/matched-cell/s4-primary-search-closure.json).

## S5 — current `gap` frontier

- **Reviewed through:** `2026-09-25`.
- **Primary blocking reason:** Reviewed direct S5 evidence now includes GovSim-SelfGovern's benchmark-scaffolded membership/identity authority path and one canonical native descriptive observation: Ouroboros PR #855 supplies a parent-governed constitutional/runtime policy-change witness with executable return and persistence into later canonical lineage. Public evidence still lacks a materially matched comparison of multiple canonical native or adapter-preserved S5 implementations under one comparable authority/change/subsequent-operation surface.
- **Closure claim:** Current public evidence contains one direct composed S5 benchmark family/observation and one canonical native direct descriptive observation. GovSim-SelfGovern exercises benchmark-scaffolded membership/identity authority, while canonical Ouroboros supplies a parent-governed constitutional/runtime policy-change witness with executable return and persistence into later canonical lineage. The S5 primary remains a gap because public evidence still lacks a materially matched comparison of multiple canonical native or adapter-preserved S5 implementations under one comparable authority/change/subsequent-operation surface.
- **Evidence depth:**
  - `reviewed_cases`: `14`
  - `direct_benchmark_families`: `1`
  - `composed_direct_observations`: `1`
  - `canonical_direct_observations`: `1`
  - `representative_canonical_s5_systems`: `5`
- **Reopen when:**
  1. a second canonical native or adapter-preserved direct S5 observation appears under a materially comparable authority/change/subsequent-operation surface
  1. a materially matched benchmark compares two or more canonical-linkable S5 systems under the same authority/change/subsequent-operation protocol
  1. GovSim-SelfGovern or another direct family publishes adapter-preserved canonical harness rows with recoverable model/configuration provenance suitable for a matched primary cell
- **Do not reopen for:**
  - another benchmark-scaffolded direct S5 family without canonical native or adapter-preserved linkage
  - another heterogeneous single-system descriptive policy-change witness that cannot be materially compared with an existing canonical observation
  - fixed-policy adherence, filtering or enforcement benchmarks
  - external public-policy analysis, value-expression tasks, governance mechanism unit tests or protocols without direct organizational authority/change closure
- **Non-claim:** This closure is not a zero S5 capability score, does not attribute GovSim-SelfGovern's benchmark-scaffolded S5 organization to an underlying model, and does not treat Ouroboros PR #855 as evidence that autonomous Cyber Pro independently chose the policy change. It preserves the primary gap until materially matched multi-canonical evidence appears.
- **Source:** [`s5-primary-search-closure.json`](s5-system-benchmarks/matched-cell/s5-primary-search-closure.json).

## Reading rule

```text
historical SYNTHESIS.md / experiment-state.json
        = immutable closed-cycle snapshot

current primary-baselines.json
        +
current S2–S5 function closure records
        ↓
this generated evidence-frontier projection
```

Function-specific closure schemas remain authoritative. This projection deliberately does not normalize `A`, `C`, `P`, benchmark counts, observation counts, route counts or provenance gates into a scalar maturity/capability score.
