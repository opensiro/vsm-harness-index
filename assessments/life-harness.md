---
harness_id: life-harness
project_name: Life-Harness
repository: https://github.com/Tianshi-Xu/Life-Harness
review_ref: 22c299b83d888405d34d2c7efc0fcf4d2ccfdcef
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# Life-Harness

## Review boundary

- System in focus: one first-party Life-Harness evaluation/evolution campaign at pinned revision `22c299b83d888405d34d2c7efc0fcf4d2ccfdcef`, including the shipped TauBench/AgentBench harness runtime surfaces, H2-H5 intervention hooks, benchmark adapters/evaluators, proposer wrapper, and the automated `life_loop.py` / `agentbench_loop.py` search-and-acceptance loops.
- Purpose and identity: improve a frozen LLM agent by adapting the persistent runtime interface around it from observed deterministic-environment failures, without retraining model weights or changing benchmark task semantics/reward criteria.
- Relevant environment: benchmark tasks/environments and their ground-truth/judge criteria, configured model/provider endpoints, the headless Qoder proposer CLI and proposer model, Docker/native execution substrates, operator-supplied run configuration and credentials.
- Standard-distribution boundary: the repository-shipped harness hooks, benchmark-running/evaluation code, evolution prompts, proposer wrapper and automated search loops are inside. External model/provider internals, the Qoder implementation itself, external services and host credentials are dependencies; their decisions count only where the pinned first-party distribution explicitly invokes them as the actor in a closed supported path.
- Credited operating / distribution surfaces: root `README.md`; `TauBench/scripts/eval_harness.py`; `TauBench/src/tau2/harness/{base.py,airline.py,retail.py,telecom.py,skills.py,h3_tools.py}`; `meta/{life_loop.py,agentbench_loop.py,benchmark.py,proposer.py}` and their normal run-state/plugin-chain/evaluation paths.
- Adjacent first-party surfaces excluded from ownership: paper/result tables as proof of VSM ownership, historical experiment artifacts as independent operating systems, repository CI/release/contributor governance, screenshots/assets, and benchmark code paths not reached by the declared current iteration modes.
- First-party operating / deployment modes considered: TauBench Airline/Retail/Telecom evaluation with H2-H5 enabled; automated Life-Harness iteration from released or zero content; AgentBench ALFWorld/DBBench bounded-evidence iteration; optional held-out finalization after search; native/Docker benchmark execution where supported.
- Recursion level: one Life-Harness campaign is the system-in-focus. A frozen model-driven benchmark episode is the operational S1 unit; the proposer plus benchmark feedback and persistent plugin-chain acceptance form the adaptive metasystem around repeated episodes.
- Reviewed revision: `22c299b83d888405d34d2c7efc0fcf4d2ccfdcef`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Life-Harness ships two benchmark families plus an automated meta-layer. At runtime, H2 pre-execution rules can reject invalid model-selected tool calls and return an explanatory error to the agent; H3 augments tool/environment contracts; H4 annotates successful tool results and detects repeated failure patterns; H5 injects procedural skills derived from prior recoveries. The model remains the substantive task actor and sees the harness-mediated observation on its next turn.

`meta/life_loop.py` implements a persistent adaptation loop over those H2-H5 surfaces. A headless Qoder session, restricted to read/edit tools and driven by an evolution prompt, inspects prior trajectories/search evidence and writes one candidate plugin plus a machine-readable hypothesis. The host validates the plugin, screens it on failing tasks plus regression sentries, and by default requires a complete frozen search-pool confirmation before acceptance. Accepted candidates are copied into an ordered persistent plugin chain and become active for later evaluations/proposals; regressions restore the last confirmed chain. `meta/agentbench_loop.py` implements the same principle for the current AgentBench path with frozen protocols, bounded public evidence, staged screening and strict full-pool improvement.

The score path is distinct from the operational actor's own report. `meta/benchmark.py` invokes the benchmark-native evaluator, reads `harness_summary.json`, and returns reward/per-task evidence to the outer loop. That evaluation can use task ground truth, deterministic assertions or a benchmark judge independently of the operational model's self-report. Life-Harness then uses the score to reject/accept a candidate and exposes prior trajectory/evaluation evidence to the next proposer turn. This establishes a complementary-evaluation constructor path, while the exact audit criterion/independence varies by benchmark configuration.

Held-out `--test` finalization is intentionally isolated from search and freezes the run; it is therefore not itself used to inflate S4 or S3*. The positive S4 path already closes on the search split through autonomous proposal, independent outcome measurement, persistent accepted plugin content and reuse in later operation.

## Operational model

A benchmark episode supplies a task/environment to a frozen model-driven agent. Life-Harness augments the interface before/during/after tool execution through H2-H5, returns resulting errors/annotations/skills to the model, and records the episode outcome. The benchmark evaluator separately scores the completed run. Across episodes, the first-party evolution loop presents bounded trajectory/outcome evidence to a configured model-backed proposer, receives a concrete H2-H5 plugin mutation, validates and evaluates it, and automatically persists it only when configured acceptance criteria are met. Later operational episodes execute with the accepted chain, producing new evidence for another adaptation iteration.

## S1 — Operations

- State: A
- Function: execute an open-ended model-driven benchmark task through repeated model action, tool/environment response and harness-mediated corrective feedback until completion or bounded termination.
- Disturbance / variety regulated: task instructions, environment/database state, invalid or incomplete tool actions, tool results/errors, recurring loops, procedural mistakes, prompt/tool-contract ambiguity and runtime step limits.
- Decisive decision or feedback right: choose the substantive next task action/tool call or response after observing the current conversation and the harness-mediated environment result.
- Decision owner: the configured autonomous agent LLM invoked by the shipped benchmark runner.
- Supporting / enforcement mechanisms: TauBench task runner, H2 `HarnessRule` validation, H3 tool-description contracts, H4 post-execution annotations/stuck-loop guidance, H5 skill injection, environment/tool execution and episode/result capture.
- Closure path: task + current context → model chooses a substantive action/tool call → H2 may validate/reject and the environment executes permitted action → H4/environment returns error/result/annotation and H5/H3 context remains available → the next model turn observes that evidence and revises/continues → completed episode/result is recorded.
- Boundary reachability: `TauBench/scripts/eval_harness.py` is the documented standard evaluation path and directly invokes the bundled runner with the configured agent model and H2-H5 switches; the first-party harness mixins return their interventions into the agent-visible tool-result path. No downstream orchestration package is needed beyond a configured provider endpoint.
- Why this is / is not agent-owned: deterministic harness rules can constrain or enrich actions but do not choose the task solution. Removing the model actor while keeping H2-H5 leaves validation/annotation machinery but removes the same substantive next-action right.
- Evidence: [`README.md`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/README.md); [`TauBench/scripts/eval_harness.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/TauBench/scripts/eval_harness.py); [`TauBench/src/tau2/harness/base.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/TauBench/src/tau2/harness/base.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference may be served externally; credit rests on the first-party operational organization that concretely closes model decision → tool/environment result → agent-visible feedback.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 disturbance-attenuation function is established at the campaign recursion.
- Disturbance / variety regulated: not established as a concrete interaction-generated conflict or oscillation between distinct sibling operational S1 units.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: evaluation concurrency, task batching, isolated worktrees/run directories, candidate screening and plugin-chain ordering coordinate execution mechanics but are not an S2 relation among mutually interacting S1 units.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: parallel benchmark episodes do not communicate or interfere in a way that the system detects and attenuates through an S2-specific feedback loop; they are independent measurements whose aggregate evidence feeds S4.
- Evidence: [`meta/life_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/life_loop.py); [`meta/agentbench_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/agentbench_loop.py); [`README.md`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: concurrency and multiple tasks are not counted as multiple coordinated S1 units without a concrete interaction disturbance and attenuation path.

### Absence scope

- Surfaces inspected: TauBench/AgentBench episode execution, task concurrency, worktrees/run isolation, plugin chain, proposer/evaluation loops, screen/full-confirmation logic and held-out finalization.
- Plausible first-party paths checked: concurrent tasks as sibling S1s, shared accepted plugin state, screen-sentry selection, batch rollback, candidate competition and benchmark-wide aggregation.
- Why no material first-party path remains: these paths isolate, aggregate or sequentially adapt episodes. No standard path identifies interaction-generated S1↔S1 conflict/oscillation and feeds an S2-specific attenuation decision back into those sibling operations.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system inside-and-now control function is established above operational episodes and the prospective adaptation loop.
- Disturbance / variety regulated: run state, candidate lifecycle, evaluation failures, concurrency, task pools, search budgets and acceptance thresholds are controlled, but those controls are deterministic lifecycle/enforcement or belong to S4 adaptation selection.
- Decisive decision or feedback right: no separate substantive authority is established over multiple current operational commitments/resources/priorities at the campaign recursion.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: run configuration fingerprints, protocol freezing, task-pool selection, concurrency bounds, screen/full gates, rollback, resume state and finalization freeze.
- Closure path: not applicable for the negative finding.
- Boundary reachability: all listed controls are first-party and reachable, but they do not constitute a distinct S3 organizational function.
- Whole-system current view: run/state files expose accepted chain, scores, task cache/history and iteration state, but that view is primarily used to choose/verify future harness changes rather than regulate a set of simultaneous current organizational commitments.
- Current-control decision scope: deterministic campaign lifecycle and candidate acceptance/rollback under configured rules; no separate present-tense resource/commitment/priority judgment owner is established.
- Why this is / is not agent-owned: the model-backed proposer owns future capability proposals mapped to S4. Reclassifying candidate acceptance/search control as S3 would double-count the adaptation mechanism rather than establish a distinct current-control loop.
- Evidence: [`meta/life_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/life_loop.py); [`meta/agentbench_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/agentbench_loop.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: H4 stuck-loop guidance is local S1 regulation; full-pool confirmation/rollback governs candidate adaptation, not an independent S3 metasystem.

### Absence scope

- Surfaces inspected: run/state manifests, protocol/config freezing, task scheduling/concurrency, candidate validation, screen/full confirmation, batch rollback, proposer lifecycle, finalization and runtime H2-H5 controls.
- Plausible first-party paths checked: evolution outer loop as manager, state.json as whole-system view, regression rollback as intervention, benchmark score as current performance regulator, H4 loop detection as supervisory control and held-out freeze as parent control.
- Why no material first-party path remains: the reviewed controls either bound one operational episode or implement prospective harness search/selection. No separately owned whole-current resource/commitment/priority decision-and-return loop is established.

## S3* — Complementary audit

- State: C
- Function: independently evaluate an operational episode/candidate against benchmark-native outcome evidence and return discrepancy/performance feedback into later candidate regulation and adaptation.
- Disturbance / variety regulated: the model-driven S1 can produce a plausible-looking trajectory/tool history that nevertheless violates benchmark ground truth, deterministic assertions, task success conditions or an independent judge criterion; a candidate harness can also regress previously passing tasks.
- Decisive decision or feedback right: determine benchmark reward/per-task success for completed operational episodes and expose that outcome to the outer selection/adaptation loop.
- Decision owner: constructor-dependent. Life-Harness wires a distinct benchmark/evaluator path and consumes its result, but the actual criterion may be deterministic ground truth, environment assertions or a configured benchmark judge rather than one packaged autonomous auditor common to every supported environment.
- Supporting / enforcement mechanisms: `meta/benchmark.py`, benchmark-native `eval_harness.py`/AgentBench evaluators, `harness_summary.json`, per-task reward maps, full-pool confirmation, regression sentries, infrastructure-error rejection and frozen split/task contracts.
- Closure path: operational model/harness produces a trajectory/result → separate benchmark-native evaluator checks it against task/environment criteria and emits reward/per-task evidence → Life-Harness outer loop uses the evidence to reject/accept/rollback a candidate and records the resulting trajectory/evaluation state → later proposer iterations consume that evidence and later S1 runs use the resulting accepted chain.
- Boundary reachability: every normal `life_loop` candidate evaluation invokes `meta/benchmark.py`, which in turn calls the shipped benchmark evaluator and extracts its summary; AgentBench's current loop similarly calls a separate evaluation phase. The path is part of the standard iteration workflow, not repository CI or a paper-only analysis.
- Claim being audited: that the operational episode/candidate actually satisfies the benchmark task/environment criterion and that a proposed harness change does not merely look plausible while reducing measured task success.
- Ordinary reporting path: the frozen model-driven agent emits actions/messages/tool interactions and an episode result/trajectory.
- Complementary access path: benchmark-native reward/assertion/judge logic and per-task outcome state not defined by the operational actor's own self-report.
- Independence boundary: evaluation is executed as a separate host/benchmark path from the operational model actor; exact judge/model independence varies by domain/configuration, so the generic distribution is constructor-owned rather than `A`.
- Who acts on findings: deterministic selection logic rejects/accepts/rolls back candidates from evaluator scores, and the model-backed proposer receives prior trajectory/outcome evidence when generating later adaptation options.
- Why this is / is not agent-owned: the first-party repository provides the S3*-specific separation and return path, but the decisive audit criterion is benchmark/configuration dependent rather than owned by one autonomous first-party auditor across the distribution. This supports `C`.
- Evidence: [`meta/benchmark.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/benchmark.py); [`meta/life_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/life_loop.py); [`meta/agentbench_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/agentbench_loop.py); [`TauBench/scripts/eval_harness.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/TauBench/scripts/eval_harness.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: screen sentries or held-out testing alone are not credited as S3*. Credit rests on the normal separate benchmark-evaluation path plus its return into candidate regulation/adaptation; exact independence remains benchmark-specific.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert recurring external task/environment outcome evidence into persistent H2-H5 runtime adaptations that change how the frozen operational model behaves on later episodes.
- Disturbance / variety regulated: repeated action-format failures, wrong tool conventions, missing fields, loops/no-ops, premature submissions, procedural mistakes, benchmark performance gaps and regressions observed across earlier episodes.
- Decisive decision or feedback right: choose the concrete next persistent harness intervention — its target layer, mechanism and code — from prior trajectory/evaluation evidence.
- Decision owner: the configured model-backed proposer agent invoked through the first-party `meta/proposer.py` wrapper and constrained by the Life-Harness evolution prompt/evidence contract.
- Supporting / enforcement mechanisms: evolution prompt, bounded trajectory/evidence exposure, Qoder proposer wrapper, candidate plugin contract, H2-H5 registries/hooks, candidate validation, screen/full evaluation, strict acceptance/rollback, persistent chain manifest/loader and resumable state/history.
- Closure path: S1 episodes encounter external benchmark/environment distinctions → trajectories plus independent benchmark outcomes are persisted → the model-backed proposer inspects bounded prior evidence and autonomously writes one targeted H2-H5 candidate plugin → first-party host validates and evaluates it → accepted plugin is copied into the persistent chain/confirmed state → later operational episodes load that changed harness behavior → their outcomes seed the next adaptation cycle.
- Boundary reachability: `README.md` documents `meta/life_loop.py` and `meta/agentbench_loop.py` as the current iteration commands; those loops directly call `proposer.run`, automatically evaluate generated candidate files and persist accepted content. Qoder/provider implementation is an external dependency, but the first-party standard path concretely installs it as the decisive adaptation actor rather than leaving evolution to an unspecified downstream integration.
- Why this is / is not agent-owned: deterministic host logic chooses when/how to validate and whether measured improvement crosses the configured gate, but it does not decide what failure mechanism to target or what code change to make. Removing the model-backed proposer while preserving screening, evaluation and state machinery removes the same substantive adaptation-option judgment.
- External distinction: benchmark task trajectories, environment/tool outcomes, per-task rewards, failure groups and regression evidence describe where the present harness succeeds/fails in the external task distribution.
- Future / prospective distinction: each accepted plugin is retained specifically to alter behavior on later episodes; the proposer is instructed to diagnose recurring patterns and implement reusable interventions rather than retry the current episode.
- Adaptation option generated: a concrete self-contained plugin that modifies one or more H2 action-realization, H3 environment-contract, H4 trajectory-regulation or H5 procedural-skill surfaces.
- Path back into current capability / S3: after full confirmation, the candidate is copied into the ordered accepted chain (or into the frozen AgentBench incumbent), the loader/state is updated, and subsequent evaluation/operational episodes execute with that persistent changed interface.
- Evidence: [`README.md`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/README.md); [`meta/life_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/life_loop.py); [`meta/agentbench_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/agentbench_loop.py); [`meta/proposer.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/proposer.py); [`TauBench/src/tau2/harness/base.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/TauBench/src/tau2/harness/base.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: published performance gains are not used to infer ownership. The operator selects model/task/configuration and launches the campaign; that does not establish a distinct parent S4 mode because ordinary launch/configuration is not a returned adaptation judgment.

## S5 — Policy and identity

- State: —
- Function: no closed first-party runtime path is established for deciding or reaffirming the campaign's ultimate identity, purpose or foundational policy.
- Disturbance / variety regulated: operator-selected benchmark/domain, task pool, models, proposer budget, H2-H5 mutation contract, forbidden references, allowed tools, acceptance thresholds and held-out rules strongly constrain evolution but are externally authored mandate/enforcement.
- Decisive decision or feedback right: no first-party actor is shown receiving an identity/ultimate-policy issue, deciding the foundational mandate and returning that authoritative decision into operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: CLI/run configuration, frozen protocol/config fingerprints, proposer tool allowlists, read-only/forbidden-reference guards, H2-H5 search-space constraints, acceptance rules and finalization freeze.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → authoritative decision → returned governance path is established.
- Why this is / is not agent-owned: the proposer may autonomously change permitted operational interface content, but its prompt explicitly forbids changing model weights, benchmark tasks, environment/evaluation criteria and hidden policy boundaries. Capability self-improvement inside that mandate is S4, not authority to redefine the mandate itself.
- Evidence: [`meta/life_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/life_loop.py); [`meta/agentbench_loop.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/agentbench_loop.py); [`meta/proposer.py`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/meta/proposer.py); [`README.md`](https://github.com/Tianshi-Xu/Life-Harness/blob/22c299b83d888405d34d2c7efc0fcf4d2ccfdcef/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: strong anti-cheat/security/search-space rules are enforcement, not S5 ownership. Human ability to alter source/configuration outside the run is not a complete parent S5 loop at this recursion.

### Absence scope

- Surfaces inspected: current iteration prompts/configuration, H2-H5 plugin contract, proposer permissions/forbidden references, protocol/run fingerprints, benchmark/model/task selection, acceptance/rollback/finalization policy, repository governance and runtime harness code.
- Plausible first-party paths checked: proposer editing its own mandate, H2 policy rules as S5, frozen protocol as identity authority, acceptance criteria as ultimate policy, held-out freeze as governance and maintainer/operator configuration as parent S5.
- Why no material first-party path remains: all reviewed mandate-defining choices are prior configuration/code constraints. The model-backed proposer is deliberately prevented from changing them and no supported runtime mechanism escalates a foundational identity/policy question to a legitimate authority and returns a new authoritative mandate into operation.

## Distributed OSS parent arrangement

Repository maintainers govern development/releases, while a campaign operator selects task pools, models and run configuration. Neither relationship is imported as organization-level parent S3/S4/S5 ownership without a function-specific runtime return loop. No parent modifier is claimed.

## Self-hosted and non-human modes

The current loops are designed to run unattended once the required local/native/Docker services, Qoder CLI, models and run configuration are available. Human launch/configuration does not remove autonomous S1/S4 ownership, and optional held-out finalization is a frozen evaluation phase rather than a parent adaptation decision.

## Recursion

At the assessed recursion, a Life-Harness campaign contains repeated operational benchmark episodes plus an adaptive outer loop. The model-driven episode is S1. Separate benchmark evaluation exposes complementary outcome evidence as S3*=C. The model-backed proposer converts accumulated external evidence into persistent interface changes as S4=A. Parallel episodes, screening and rollback do not create separate S2/S3 functions.

## Variety and escalation

Life-Harness attenuates task-local variety through action validation, explicit environment contracts, state-aware trajectory annotations and procedural skills. Across episodes it amplifies adaptation variety through model-generated targeted plugins, then attenuates unsafe/non-generalizable changes with code guards, regression sentries and full-pool confirmation. Evaluation failures and regressions reject or roll back candidates; accepted changes become later capability rather than escalating into a distinct S3 or S5 authority.

## Evidence gaps

- S1 credit is bounded to the supported benchmark-runner/harness path; external provider internals do not donate higher functions.
- S2 is not inferred from parallel task evaluation, candidate competition or shared accepted-chain state.
- S3 is not inferred from iteration orchestration, score gates, rollback or H4 stuck-loop detection; these belong to deterministic lifecycle, S1 or S4.
- S3* is constructor-owned because Life-Harness wires a separate benchmark-evaluation return path, but the exact ground-truth/judge independence is benchmark/configuration dependent.
- S4 is autonomous because a model-backed proposer chooses substantive persistent harness mutations from prior external outcome evidence and the standard loop returns accepted mutations into later operational capability.
- S5 is not inferred from strong frozen protocols, H2 policy constraints, proposer permissions or operator-authored run configuration.
