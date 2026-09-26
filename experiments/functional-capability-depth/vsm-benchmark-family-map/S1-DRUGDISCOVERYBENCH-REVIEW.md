# DrugDiscoveryBench — S1 drug-discovery/life-sciences benchmark-family review

Status: experimental, non-normative.

Tracking issue: #721

Reviewed source:

```text
scaleapi/DrugDiscoveryBench@d58c703841abbad0ba1cc439488e15fbbeae3bd2
```

## Result

```text
function: S1
fit: direct
domain_scope: drug-discovery-life-sciences
system_linkage: observation-specific
evaluation_mode: execution-grounded
```

DrugDiscoveryBench directly evaluates an operational scientific-agent / harness loop inside a declared biomedical environment. The evaluated system must use repository/container state, biomedical data and tools to perform task-relevant research work and produce a final scientific output for grading.

This is direct S1 at the benchmark boundary. The classification is grounded in the operational transformation being performed, not in generic reasoning, tool-use, planning, research or science vocabulary.

## Reviewed task and runtime surface

The pinned repository publishes 82 Harbor-formatted drug-discovery and life-sciences tasks. Each task is a self-contained biomedical research problem executed inside a pre-built trial image with a full BiOMNI biomedical toolchain.

The public workflow fixes:

- Harbor `0.13.1` as the benchmark runner;
- trial image `ghcr.io/scaleapi/drugdiscoverybench:1.0.0-lightweight`;
- an on-container BiOMNI tool suite and biomedical data-lake surface;
- a shared `/workspace` where the agent writes its final answer;
- a separate rubric-based judge that grades the produced answer.

The reviewed example task requires the agent to compare a local patient cohort with historical colon-cancer treatment data, determine the relevant treatment proportions and return a constrained comparison result. Its instructions explicitly direct the agent to inspect the installed BiOMNI reference/tool surface and local data before or while performing the analysis.

The benchmark therefore evaluates more than static question answering. The S1 under test performs scientific operations over an environment: inspect, retrieve, query, compute, analyze and produce an operational research result.

## Execution boundary

The benchmark's `scripts/run_eval.sh` invokes the selected agent through Harbor over one or more task environments. Supported public first-party adapters include Claude Code, Codex and Gemini CLI. The benchmark image contains pinned CLI builds, and the wrapper reuses those preinstalled CLIs rather than treating the evaluated system as a bare model API.

Those implementation details improve later system-observation provenance, but they are not needed to establish family semantics. Benchmark-family admission asks what organizational function the benchmark directly exercises; individual scaffold/model rows remain a separate evidence transaction.

## Evaluation boundary

A separate LLM judge evaluates the final answer against expert-authored rubrics. That judge is part of the benchmark membrane, not evidence that the evaluated harness owns an S3* function.

The direct S1 classification therefore separates:

```text
agent/harness + biomedical operational environment
        -> scientific task operation / output

external benchmark judge
        -> evaluation of that S1 output
```

Judge quality, rubric design and benchmark scoring are relevant provenance fields for later observations, but do not donate organizational audit ownership to the measured system.

## Domain boundary

DrugDiscoveryBench adds a direct S1 surface outside the existing Coding/SWE cluster. Its domain scope is:

```text
drug-discovery-life-sciences
```

Raw scores must remain within this domain/benchmark family. They are not normalized against Coding/SWE, terminal or other S1 families into one universal capability score.

## System linkage

Benchmark-family fit and canonical-system attribution are separate.

A later observation transaction must independently recover, where public evidence permits:

- exact evaluated scaffold / agent CLI and version;
- exact model and materially relevant configuration;
- task set / trial count and concurrency policy;
- benchmark image/runtime version;
- judge model/configuration and rubric provenance;
- network/search/tool restrictions;
- result artifact provenance;
- whether the measured row preserves a canonical harness's own operational loop (`native-system`) or a defensible adapter-preserved historical boundary.

The pinned public image documents Claude Code `2.1.190`, Codex `0.122.0` and Gemini CLI `0.46.0`, making later provenance review promising. No row is admitted here merely because those versions are published.

## Primary-baseline boundary

Admitting DrugDiscoveryBench as direct S1 evidence does **not** replace PawBench v1.0 as the selected general S1 primary and does not replace Claw-SWE-Bench as the current Coding/SWE domain primary.

DrugDiscoveryBench is a new domain-scoped direct family. A later observation may support a domain-specific projection, but raw drug-discovery scores are not a PawBench challenger simply because they measure S1.

No system observation or leaderboard/result row is admitted in this transaction.

## Function-first non-claims

DrugDiscoveryBench does **not** establish:

- S2 from multi-step work, scientific workflow complexity, tool sequencing or parallel execution;
- S3 from planning, resource selection, retry, budget or control-flow behavior;
- S3* from the benchmark's external LLM judge, rubrics, verification or grading;
- S4 from literature/database lookup, exploration, hypothesis changes or within-task replanning;
- S5 from task instructions, safety rules, network restrictions, image policy or benchmark configuration;
- experimental self-organizing `S` from successful scientific task completion;
- any `A`, `C`, `P`, `—`, or `?` ownership state from benchmark performance.

## Admission consequence

DrugDiscoveryBench is admitted only to the experimental benchmark-family map as another direct S1 family with `drug-discovery-life-sciences` scope and observation-specific system linkage.

This issue does not run the benchmark, add raw system observations, copy result numbers into Index data, modify canonical assessments, or change any selected primary baseline. Public result artifacts, if sufficiently provenance-bound, belong in a later observation review.