---
harness_id: a-evolve
project_name: A-Evolve
repository: https://github.com/A-EVO-Lab/a-evolve
review_ref: 18ba996dac9843f2759b2cdf8a94022f58fbfeb9
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# A-Evolve

## Review boundary

- System in focus: one first-party A-Evolve `Evolver` organization at pinned revision `18ba996dac9843f2759b2cdf8a94022f58fbfeb9`, including the selected first-party/bound `BaseAgent`, its copied mutable workspace, benchmark adapter, observation/history/versioning machinery, the configured evolution engine, and the repeated solve → observe/evaluate → evolve → reload cycle.
- Purpose and identity: run an operational agent against an environment/task distribution and autonomously adapt the agent's persistent harness/workspace so later operation can better absorb observed task/environment variety.
- Relevant environment: benchmark/task distributions; repositories, containers, APIs or other task environments reached by the selected agent; model-provider endpoints used by solver/evolver actors; benchmark ground truth/judges; operator-supplied configuration and optional custom agent/benchmark/evolution implementations.
- Standard-distribution boundary: the shipped `agent_evolve` package, top-level `Evolver`, bundled `BaseAgent` protocol and reference agents/seed workspaces, benchmark-adapter contract and built-in adapters, default `AEvolveEngine`, `EvolutionLoop`, Observer/History/VersionControl, and documented built-in evolution path. External model providers, benchmark datasets/services, task repositories/containers/APIs, and adopter-supplied custom agents/engines/benchmarks remain dependencies or alternative constructor inputs.
- Credited operating / distribution surfaces: `README.md`; `QUICKSTART.md`; `DESIGN.md`; `agent_evolve/api.py`; `agent_evolve/config.py`; `agent_evolve/protocol/base_agent.py`; `agent_evolve/engine/loop.py`; `agent_evolve/engine/observer.py`; `agent_evolve/engine/history.py`; `agent_evolve/benchmarks/base.py`; `agent_evolve/algorithms/skillforge/engine.py`; bundled seed manifests and reference agent implementations such as `seed_workspaces/swe/manifest.yaml` and `agent_evolve/agents/swe/agent.py`.
- Adjacent first-party surfaces excluded from ownership: published benchmark scores and paper result tables; `artifacts/` and result summaries; repository-development CI/release/contributor governance; tests and one-off examples except where they corroborate reachability of shipped APIs; research branches/releases not present at the pinned revision; organizational functions internal to external model providers, task benchmarks, containers or adopter-supplied agents.
- First-party operating / deployment modes considered: documented top-level `ae.Evolver(...)` with built-in seed workspaces and built-in benchmark adapters; default `AEvolveEngine`; documented benchmark-specific evolution scripts; supported bring-your-own `BaseAgent`, benchmark adapter and evolution-engine modes only where they clarify constructor boundaries. Published benchmark gains are excluded from ownership classification.
- Recursion level: one evolving-agent run is the system-in-focus. The bound operational agent is S1; benchmark/environment evidence and the evolver participate in the metasystem for that run. Separate tasks in one batch are repeated/local operational episodes, not automatically sibling S1 units. A-Evolve's ability to accept arbitrary downstream agents does not transfer those agents' internal VSM functions into this assessment.
- Reviewed revision: `18ba996dac9843f2759b2cdf8a94022f58fbfeb9`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

A-Evolve packages a common filesystem contract around three pluggable components: an operational Agent, a Benchmark that supplies tasks/evaluation, and an Evolution Algorithm. The top-level `Evolver` resolves those components, creates or copies a mutable agent workspace, and wires them into `EvolutionLoop`. Bundled seed workspaces include a manifest naming the concrete agent entrypoint and the layers that may evolve; for the SWE seed these are prompts, skills and memory with hot reload.

`EvolutionLoop` owns the repeated lifecycle. In ordinary engine-managed evaluation mode it obtains training tasks from the benchmark, invokes `agent.solve(task)`, evaluates each returned trajectory through the benchmark adapter, persists observations, snapshots workspace state, calls the evolution engine, snapshots the result, records cycle history and reloads the operational agent from the mutated filesystem. A later cycle therefore executes the same operational organization with changed persistent capability rather than merely carrying a transient prompt from one task attempt.

The default `AEvolveEngine` is an autonomous LLM-driven workspace mutation actor. It reads recent observation/history material, constructs an evolution prompt, and receives bash access scoped to the workspace. Its configured mutation repertoire includes prompts, skills and memory by default; tools may be enabled separately. The evolver chooses what to add/change, while filesystem helpers and Git versioning apply and record the selected mutation. `BaseAgent.reload_from_fs()` then reloads prompt/skill/memory/harness state before subsequent operation.

Benchmark evaluation is intentionally separate from the operational Agent. `BenchmarkAdapter.evaluate(task, trajectory)` is specified to judge a trajectory against benchmark ground truth and return rich `Feedback` for failure diagnosis. Concrete benchmark/evaluator semantics vary by selected adapter and may themselves be deterministic, model-based or externally hosted. This supplies a first-party complementary-evidence construction path, but the general A-Evolve distribution does not package one autonomous audit actor that owns the audit judgment across supported benchmarks.

## Operational model

A documented autonomous evolution run starts from a bundled or adopter-supplied agent workspace. The operational agent acts in its task environment and produces trajectories/results. A benchmark adapter supplies an independent evaluation surface. The resulting behavior/evidence is persisted and made available to the evolver. The evolution-engine agent interprets recent operational evidence and autonomously chooses persistent changes to the workspace. A-Evolve commits the mutation, reloads the operational agent and subjects the changed capability to later tasks/cycles.

The principal function split is therefore not “agent versus benchmark names” but operation versus adaptation: the bound `BaseAgent` owns task-local action decisions (S1), while the default evolver owns the prospective adaptation judgment over persistent capability (S4). Benchmark evaluation can provide complementary evidence about operational claims, but its decisive judgment is supplied by the selected benchmark/adapter rather than a standard autonomous audit actor, so the shipped cross-benchmark path is classified as an S3* constructor.

## S1 — Operations

- State: A
- Function: perform the task/environment work whose outcomes the evolving organization is intended to improve.
- Disturbance / variety regulated: task-specific repository/environment state, tool/API/container feedback, implementation or reasoning uncertainty, execution errors, and other local distinctions presented by the selected task distribution.
- Decisive decision or feedback right: choose the substantive task actions, tool calls, code/environment changes and stopping/submission behavior needed to solve the current task within the bound operational agent.
- Decision owner: the autonomous model-driven actor instantiated by the selected first-party `BaseAgent` implementation; the bundled SWE reference path constructs a real `strands.Agent` with the current workspace prompt/tools/skills and invokes it on the task.
- Supporting / enforcement mechanisms: `BaseAgent` workspace loading/export/reload, manifest/entrypoint resolution, tool registry/loading, benchmark task loading, container/environment wrappers, model-provider bindings, trajectory capture, optional deterministic step limits and submission tooling.
- Closure path: benchmark/environment supplies a task → A-Evolve invokes `BaseAgent.solve()` → autonomous agent chooses task actions and receives local tool/environment feedback → a `Trajectory`/operational result is returned → the result enters evaluation/observation and later organizational adaptation.
- Boundary reachability: the documented `ae.Evolver(agent="swe-verified", benchmark="swe-verified")`/built-in seed path resolves a shipped first-party workspace manifest to `SweAgent`; `Evolver.run()` directly invokes the same `BaseAgent` through `EvolutionLoop`. The autonomous S1 actor is therefore reachable in the standard distribution without borrowing an adjacent repository-development agent.
- Why this is / is not agent-owned: deterministic workspace/container/tool machinery constrains execution, but it does not choose the substantive task actions. Under the counterfactual owner test, retaining those mechanisms without the model-driven `BaseAgent` actor removes the operational decision right.
- Evidence: [`agent_evolve/api.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/api.py); [`agent_evolve/protocol/base_agent.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/protocol/base_agent.py); [`seed_workspaces/swe/manifest.yaml`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/seed_workspaces/swe/manifest.yaml); [`agent_evolve/agents/swe/agent.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/agents/swe/agent.py); [`agent_evolve/engine/loop.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/engine/loop.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: arbitrary adopter-supplied `BaseAgent` internals are not inherited into A-Evolve. The positive state is grounded in the first-party protocol plus bundled reference-agent operating mode directly reached by the standard `Evolver` API.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the reviewed evolving-agent recursion.
- Disturbance / variety regulated: not established as an inter-S1 disturbance. The standard `EvolutionLoop` binds one operational `BaseAgent`; multiple benchmark tasks or parallel task processes are repeated/isolated episodes of that operation rather than evidenced sibling S1 units whose interaction generates a conflict or oscillation requiring mutual coordination.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: batch sizing, optional solve parallelism, process/container isolation, task sequencing, workspace copying, benchmark splitting and evolution-cycle ordering.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: scheduling and isolation may prevent implementation interference, but the reviewed standard distribution does not establish two distinct S1 units plus a specific interaction-generated disturbance and a coordination response that changes their subsequent peer behavior.
- Evidence: [`DESIGN.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/DESIGN.md); [`agent_evolve/engine/loop.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/engine/loop.py); [`agent_evolve/config.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/config.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: A-Evolve can evolve multi-agent implementations and contains specialized research/example machinery, but agent plurality in an input agent or experiment is not transferred into the standard generic A-Evolve boundary.

### Absence scope

- Surfaces inspected: top-level API/config, `EvolutionLoop`, architecture design, bundled reference-agent path, benchmark interface, batch/parallel execution descriptions and evolution algorithms.
- Plausible first-party paths checked: batch parallelism, multi-agent seed/example references, process isolation, benchmark task scheduling, navigation/branching algorithms and shared workspace/versioning state.
- Why no material first-party path remains: none of the standard generic relations establishes distinct sibling S1 units at this recursion together with a concrete interaction-generated interference/oscillation and a first-party relation specifically regulating it. The reviewed mechanisms schedule or isolate work rather than implement S2 at the declared boundary.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system inside-and-now current-control function is established at the reviewed evolving-agent boundary.
- Disturbance / variety regulated: A-Evolve tracks task/cycle status, scores, workspace history and convergence, but those surfaces either execute the operational task lifecycle or support prospective adaptation; no separate actor is shown regulating current shared resources, commitments, priorities or constraints on behalf of multiple current operations.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic cycle sequencing, batch/task selection, score calculation, Git snapshots, convergence checks, configured limits, trial execution and optional navigation/promotion thresholds.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the evolution-engine agent owns adaptation choices mapped to S4, while the operational agent owns task-local S1 choices. Deterministic loop/gating/versioning machinery applies configured lifecycle rules but does not evidence discretionary whole-system current-control authority.
- Evidence: [`agent_evolve/engine/loop.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/engine/loop.py); [`agent_evolve/config.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/config.py); [`DESIGN.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/DESIGN.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an evolution engine can decide what future capability should change, but prospective adaptation is not reclassified as S3 merely because it changes the currently persisted workspace.

### Absence scope

- Surfaces inspected: `Evolver`, `EvolutionLoop`, config/gating/convergence, Observer/History/VersionControl, default evolution engine, benchmark adapters, reference S1 and architecture docs.
- Plausible first-party paths checked: cycle scheduler as controller, convergence/score thresholds as performance regulation, Git rollback/promotion as intervention, evolver as manager and benchmark evaluation as current-control input.
- Why no material first-party path remains: reviewed controls are deterministic lifecycle/enforcement or belong to S1/S4. No autonomous actor is given a whole-system view of multiple current operations plus authority over their shared present commitments/resources/priorities at the declared recursion.

## S3* — Complementary audit

- State: C
- Function: provide a complementary evidence path that can challenge the operational agent's trajectory/result against benchmark-specific ground truth or an independent evaluator and feed the resulting discrepancy information into later regulation/adaptation.
- Disturbance / variety regulated: S1 may return an apparently plausible result or trajectory that fails task/environment ground truth, tests, judge criteria or other benchmark-specific outcome checks not available from the operational actor's own report alone.
- Decisive decision or feedback right: determine whether/how the completed operational trajectory satisfies the independent benchmark criterion and return structured `Feedback` describing the result sufficiently for later diagnosis.
- Decision owner: constructor-dependent. A-Evolve specifies and wires the S3*-specific `BenchmarkAdapter.evaluate(task, trajectory) -> Feedback` path and ships concrete adapters, but the decisive audit criterion/judge is supplied by the selected benchmark/evaluator configuration rather than one packaged autonomous audit actor common to the standard distribution.
- Supporting / enforcement mechanisms: `BenchmarkAdapter` contract, built-in adapters, task/environment ground truth, Docker/API/judge integrations, `Observation` persistence, Observer/History and deterministic transport of feedback into the evolution loop.
- Closure path: operational `BaseAgent` returns a trajectory/result → separate benchmark adapter evaluates it against its own evidence/ground truth → structured feedback is attached to the observation/history → the evolution engine can use the discrepancy evidence when choosing later workspace/capability changes → the changed operational agent executes later cycles. The constructor supplies this complete function-specific path, while the audit owner/criterion depends on the configured adapter.
- Boundary reachability: every ordinary non-self-evaluating `EvolutionLoop` cycle calls the bound benchmark adapter's `evaluate()` after `agent.solve()`, and the documented `Evolver` API requires/resolves a benchmark. The first-party complementary-evidence path is therefore a normal supported construction surface, not an adjacent CI/test-only mechanism.
- Why this is / is not agent-owned: `BenchmarkAdapter` explicitly separates operational production from the independent judgment path, but A-Evolve does not package a single autonomous audit actor owning that judgment across benchmarks. A deterministic/test-based or externally supplied judge may close a concrete instantiated audit path; the generic first-party distribution therefore exposes a real S3*-specific constructor rather than autonomous `A` ownership.
- Claim being audited: that the operational agent's returned trajectory/result correctly satisfies the current benchmark task/environment criterion.
- Ordinary reporting path: `BaseAgent.solve(task)` returns the agent-generated `Trajectory`, output/patch and tool/action trace from ordinary S1 execution.
- Complementary access path: benchmark-specific `evaluate()` can use ground truth, tests, containers, API results or separate judge logic outside the S1 actor's ordinary self-report.
- Independence boundary: the benchmark adapter is a separate component from `BaseAgent`; its dataset/evaluation logic is selected independently of the operational agent and is not defined by the S1 trajectory itself. The exact independence strength remains adapter-specific, which is one reason the generic state is constructor-owned.
- Who acts on findings: the configured evolution-engine agent consumes persisted observations/history and can convert the feedback into future workspace adaptations; deterministic loop/versioning machinery then closes those adaptations into subsequent S1 operation.
- Evidence: [`agent_evolve/benchmarks/base.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/benchmarks/base.py); [`agent_evolve/engine/loop.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/engine/loop.py); [`agent_evolve/api.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/api.py); [`QUICKSTART.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/QUICKSTART.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary S1 self-verification, solver skill proposals and generic logs are not credited as S3*. The positive constructor is specifically the separate benchmark/evaluation path. A concrete downstream instantiation may have stronger deterministic or autonomous audit ownership, but that does not upgrade the generic A-Evolve distribution to `S3*=A`.

## S4 — Outside-and-then intelligence

- State: A
- Function: interpret task/environment evidence across operational episodes into persistent adaptation options and autonomously change present capability so later operation can respond differently.
- Disturbance / variety regulated: recurring task failures, trajectory/tool-use patterns, benchmark/environment feedback, newly encountered task distinctions and other evidence that the current prompt/skill/memory/tool repertoire is insufficient for future tasks in the relevant distribution.
- Decisive decision or feedback right: choose which persistent workspace adaptations to make from accumulated evidence — including prompt, skill and memory changes by default — and thereby alter the operational repertoire exposed to subsequent S1 runs.
- Decision owner: the autonomous LLM actor inside the default first-party `AEvolveEngine`; it receives the evolution prompt/history context and workspace-scoped bash tools and decides what to inspect and mutate.
- Supporting / enforcement mechanisms: Observer/history collection, trajectory files/indexing, benchmark feedback where exposed by the configured mode, `EvolveConfig` mutation permissions, workspace filesystem contract, Git pre/post snapshots, optional trials/gates/rollback machinery, deterministic cycle sequencing and `BaseAgent.reload_from_fs()`.
- Closure path: S1 executes tasks in an external/task environment → trajectories and available feedback are recorded → the autonomous evolution-engine actor interprets recent evidence and chooses persistent workspace changes → A-Evolve writes/commits the changed prompt/skills/memory/tool state → `BaseAgent.reload_from_fs()` reloads the changed capability → later tasks/cycles are solved using the evolved repertoire, producing new evidence for another adaptation cycle.
- Boundary reachability: `Evolver` defaults to `AEvolveEngine` when the caller does not supply another engine; default `EvolveConfig` enables prompt, skill and memory evolution; bundled seed workspaces expose evolvable layers and hot reload; the documented Quick Start's ordinary evolution tutorial executes the solve → observe → evolve → reload loop. The autonomous S4 path is therefore a first-party standard mode rather than a research-only adjacent actor.
- Why this is / is not agent-owned: deterministic code controls when a cycle starts, what layers are writable and how mutations are versioned/reloaded, but it does not choose the substantive adaptation. Removing the evolver LLM while leaving Observer, Git, config and reload machinery preserves evidence/enforcement but removes the discretionary choice of what future capability should change.
- External distinction: task/environment trajectories and, depending on benchmark/configuration, independent evaluation/feedback expose distinctions about where the current operational repertoire succeeds, fails or behaves poorly in the relevant external task distribution.
- Future / prospective distinction: the evidence is analyzed after/between operational episodes specifically to improve performance on later tasks/cycles; it is not merely current-episode retry or context continuation.
- Adaptation option generated: the evolver may add/replace/refine persistent prompts, skills and memory by default, with tools/infra available under configuration; default `AEvolveEngine` autonomously selects concrete workspace mutations using recent observation history.
- Path back into current capability / S3: selected adaptations are written into the bound AgentWorkspace, committed/versioned, and then reloaded by `BaseAgent.reload_from_fs()` before later S1 operation. No separate positive S3 mapping is required for this implementation topology; the S4 return path reaches operational capability directly through the shared workspace contract.
- Evidence: [`README.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/README.md); [`QUICKSTART.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/QUICKSTART.md); [`DESIGN.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/DESIGN.md); [`agent_evolve/api.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/api.py); [`agent_evolve/config.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/config.py); [`agent_evolve/engine/loop.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/engine/loop.py); [`agent_evolve/algorithms/skillforge/engine.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/algorithms/skillforge/engine.py); [`seed_workspaces/swe/manifest.yaml`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/seed_workspaces/swe/manifest.yaml); [`agent_evolve/protocol/base_agent.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/protocol/base_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: published benchmark gains and research-paper scores are capability evidence and are not used to establish S4 ownership. Bring-your-own agents/engines remain separate constructor configurations; the `A` claim rests on the shipped default autonomous evolution engine plus bundled first-party operational workspaces and documented integrated loop. Human selection of initial config or manual workspace edits does not establish a distinct operationally closed S4 parent mode.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established at the reviewed evolving-agent boundary.
- Disturbance / variety regulated: manifests, evolution configuration, allowed writable layers, model choices and benchmark selection constrain the run, but the reviewed standard distribution does not surface an identity/ultimate-policy conflict to a legitimate authority that decides it and returns a governing decision into subsequent operation.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `manifest.yaml`, `EvolveConfig`, writable-layer flags, system prompts, benchmark choice, model/provider configuration, workspace contract and operator launch arguments.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the evolver has broad discretion to adapt permitted operational capability, but it acts inside developer/operator-selected identity and mutation boundaries. Capability self-improvement is S4 here; it does not establish authority to redefine the organization's ultimate purpose or policy.
- Evidence: [`agent_evolve/config.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/config.py); [`seed_workspaces/swe/manifest.yaml`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/seed_workspaces/swe/manifest.yaml); [`agent_evolve/api.py`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/agent_evolve/api.py); [`DESIGN.md`](https://github.com/A-EVO-Lab/a-evolve/blob/18ba996dac9843f2759b2cdf8a94022f58fbfeb9/DESIGN.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: maintainers/operators can configure or modify the software, but generic configuration/development authority is not runtime S5 at this recursion.

### Absence scope

- Surfaces inspected: manifests/workspace contract, top-level API and run config, evolution-engine permissions/prompts, benchmark selection, Git/versioning/rollback, operator-facing Quick Start and architecture docs.
- Plausible first-party paths checked: evolver rewriting system prompt as identity change, mutation-layer permissions as policy, benchmark/model selection as ultimate authority, Git rollback/promotion as policy closure and maintainer/operator configuration as parent governance.
- Why no material first-party path remains: these surfaces bound or adapt operational capability but do not expose a runtime identity/ultimate-policy issue to a legitimate S5 authority and return an authoritative decision to govern later operation. The evolver's writable repertoire is constrained by prior configuration and is mapped to S4 rather than S5.

## Distributed OSS parent arrangement

The public repository has normal maintainer/contributor governance, but the assessed system is one local evolving-agent run. No first-party evidence reviewed here turns project maintainership into an operational parent S3/S4/S5 loop for that run. An operator chooses the initial agent/benchmark/configuration and can alter files/configuration between runs, but generic launch-time configuration or manual edits do not establish a distinct parent-governed function under Methodology `0.3.6`.

## Self-hosted and non-human modes

A-Evolve is self-hosted and intentionally pluggable. The standard default mode closes S1 and S4 autonomously through model actors while deterministic local runtime machinery transports/enforces decisions. Supported BYO Agent/Benchmark/Engine interfaces create additional downstream organizations with their own ownership boundaries; those must be assessed separately rather than inheriting this vector. No distinct qualifying parent-governed S3/S4/S5 mode is established merely from operator configurability.

## Recursion

A-Evolve can wrap operational agents whose internal organizations may themselves be viable systems, including multi-agent or domain-specific implementations. This assessment does not automatically credit those nested internals. At the declared recursion the bound operational agent contributes S1 while the benchmark/evolver/workspace loop supplies metasystemic evidence/adaptation. A downstream custom agent or specialized fork is a separate system-in-focus and requires its own evidence.

## Variety and escalation

Operational variety enters through benchmark/task environments and local execution feedback. The benchmark/evaluator can amplify distinctions that the operational agent's ordinary report would miss. Observer/history/filesystem contracts attenuate accumulated trajectories into a persistent evidence surface. The evolution-engine actor amplifies regulatory variety by creating new prompts, skills, memory and optionally tools/infra; versioning/reload returns those changes into future S1 capability. Configured bounds on writable layers, cycles, tokens and convergence constrain the adaptation repertoire.

Failures in task execution are normally represented as trajectories/feedback and become adaptation evidence rather than a separate whole-system escalation hierarchy. No independent S5 escalation closure is established. Benchmark/evaluator discrepancy evidence can enter the S4 loop through the S3* constructor path, but audit ownership remains configuration-dependent.

## Evidence gaps

- Concrete benchmark adapters differ materially in how independently and autonomously they judge trajectories. The generic distribution supports `S3*=C`; a downstream instantiated organization may justify a different audit ownership state only after adapter-specific review.
- Some specialized evolution algorithms, navigation branches and benchmark-specific scripts may add organizational relations not needed for the standard default mapping. They are not generalized into S2/S3/S3*/S5 without function-specific evidence.
- Published A-Evolve benchmark gains, papers and leaderboard claims were intentionally excluded from this standalone ownership assessment. They may be reviewed separately as non-normative capability evidence after canonical admission.
