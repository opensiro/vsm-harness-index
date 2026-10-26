---
harness_id: deepresearch-agent-harness
project_name: DeepResearch Agent Harness
repository: https://github.com/SichengLong26/deepresearch_agent_harness
review_ref: 4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# DeepResearch Agent Harness

## Review boundary

- System in focus: The runnable first-party Python/FastAPI DeepResearch research service and its installed research-workflow and optional Skill Learning capabilities, not the external LLM provider or graph/search infrastructure.
- Purpose and identity: Produce source-backed research reports by running user-selected single-research or multi-agent workflows, preserving evidence and resumable execution, and optionally generating reusable candidate skills for later research.
- Relevant environment: User research requests, remote web/private GraphRAG sources, model responses, source gaps, changing task requirements, parallel-worker dependencies, ambiguous/redundant evidence, provider/tool errors, user permission and cost constraints.
- Standard-distribution boundary: FastAPI `RunService` wiring to `HarnessRuntime` with a supported `DeepResearchDriver` or `PlanExecuteReportDriver`, model-backed first-party planner/research tools, `WorkerCoordinator`, persistent SQLite and evidence ledger, completion contract, and optional configured in-process `SkillLearningService`/promotion APIs/loader. A separate local `run_persistent_query` entry point wires the same runtime families.
- Credited operating / distribution surfaces: [application RunService wiring](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [persistent harness loop](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/runtime.py), [default multi-agent bundle](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/integration/multi_agent_factory.py), [worker coordinator](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/executor/worker_coordinator.py), [learning and promotion routes](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/api/v1/learning.py).
- Adjacent first-party surfaces excluded from ownership: `tests/`, `evals/`, evaluation-case execution, gold labels, browser acceptance scripts, development CI, author-maintainer governance, simulation/model stubs and UI presentation. Evaluator success claims are not imported as observed operating capability or S3* audit.
- First-party operating / deployment modes considered: API-launched persisted `deep_research`; `plan_execute_report` with sequential/parallel worker configuration; pause/resume/replan/repair; optional provisioned (non-test) background Skill Learning with explicit human promotion and staged rollout. Without model credentials or enabled learning review, the latter mode is inactive; its structural availability is not a claim that it ran here.
- Recursion level: One deployed research-service organization and its local workflow cells, not the broader OSS contributor organization or external infrastructure providers.
- Reviewed revision: `SichengLong26/deepresearch_agent_harness@4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0`.
- Observation date: 2026-10-26; pinned static source inspection, no live model/provider/browser execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

FastAPI's `RunService` owns the application entry and schedules persisted runs; its factory selects either `DeepResearchAgent` (model-backed retrieval/reasoning) or the first-party `MultiAgentFactory` that binds `BasePlanner`, `WorkerCoordinator` and `BaseReporter`. The local bootstrap independently wires the same two workflow categories. Those are **shipped** entry points, rather than disconnected sample classes. [RunService](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [bootstrap](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/bootstrap.py), [factory](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/integration/multi_agent_factory.py).

In multi-agent mode, model-backed `BasePlanner` clarifies the question, decomposes work and reviews a task graph before issuing an execution signal. A coordinator launches first-party worker executors and collects their evidence; a reporter synthesizes and checks a report. In parallel mode, worker state is deep-copied and reconciled in planned order, and task-dependency failures prevent unsupported downstream work. The persistent harness then compares the report to evidence- and policy-based completion checks, triggers repair or replan on bounded failure, or marks verified completion. [planner](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/planner/base_planner.py), [orchestrator](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/orchestrator.py), [coordinator](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/executor/worker_coordinator.py), [harness](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/runtime.py).

The conditional learning path is separate from executing a user's current report. With `LEARNING_REVIEW_ENABLED` and model credentials, completed sufficiently rich traces are queued for first-party Proposer and read-only Critic models, validated into candidates, evaluated and withheld until a human-approved promotion/deployment sequence. Accepted active skills are available to later `ContextBuilder`/`SkillLoader` selections. This is a supported optional future-capability path, not automatic model self-modification and not an autonomous S5. [production learning configuration and enqueue](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [review service](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/review_service.py), [promotion policy](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/promotion.py), [skill loader](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/loader.py).

## Operational model

The primary transformation is user research question → model-directed retrieval/analysis and evidence capture → verified research report. Model-backed first-party planning and research workers make bounded information/tool choices; deterministic runtime, source policy, leases, budgets, checkpointing, contract checks and the scheduler constrain rather than own that discretion. The operator initiates/cancels/pauses runs and explicitly approves an optional learned-skill release. Parallel worker isolation is a specific first-party mechanism for inter-worker shared-state interference but is not evidence of a model-owned conflict arbitrator. The model Proposer/critic can prepare and criticize future-skill options, while the promotion right belongs to the operator in the supported supervised mode. No actual quality/latency measurements are claimed by this static assessment.

## S1 — Operations

- State: A
- Function: Produce researched, source-grounded answers through agent-mediated inquiry, tool calls, interpretation, revision and report generation.
- Disturbance / variety regulated: Novel user questions, uncertain retrieval results, ambiguous task decomposition, conflicting/insufficient evidence and tool failures.
- Decisive decision or feedback right: Shipped model-backed planner chooses task breakdown/criteria, research agent selects inquiry paths and tools, and report generation/repair uses feedback from source evidence and checks.
- Decision owner: First-party instantiated planner/DeepResearch actor or composed research workers using configured external model inference; the provider supplies inference, but first-party orchestration determines the agent's operational role and feeds tool results back into its subsequent decisions.
- Supporting / enforcement mechanisms: `HarnessRuntime` state machine, run leases, budgets, tool adapter, structured plan models, event bus, persisted evidence and verifier.
- Closure path: User run → planner/agent model choice → tool execution and results → subsequent model planning/reporting/repair → verified report or bounded honest failure.
- Boundary reachability: `RunService._execute` actually constructs `DeepResearchAgent` or `MultiAgentFactory` as the selected deployed workflow and executes it via `HarnessRuntime`; this is not only an offline test/example.
- Why this is / is not agent-owned: Removing the model planner/researcher while leaving the scheduler/verifier would remove the substantive choice of how to investigate or synthesize the request; deterministic checks cannot produce equivalent research outcomes.
- Evidence: [runtime production factory](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [model planner](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/planner/base_planner.py), [research agent](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/deep_research_agent.py), [run/replan/verify](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/runtime.py).
- Basis: Structural, backed by explicit shipped wiring.
- Confidence: High for reachable architecture; no live effectiveness measure.
- Caveats: Requires a configured external inference provider and source service; no unsupported offline autonomous execution implied.

## S2 — Coordination

- State: C
- Function: Attenuate state interference and dependency oscillation among distinct concurrently executing research-work units that must contribute to one result.
- Disturbance / variety regulated: Parallel workers copying/updating plan state, evidence registries, intermediate results and completion markers; dependent tasks observing an incomplete or failed predecessor.
- Distinct S1 units: Separate planned research/retrieval/reflection work cells run as independent `WorkerCoordinator` task executors in the supported parallel plan mode, each with a task goal, source interaction and local execution state; these are bounded sub-run operational units, not independent viable organizations.
- Inter-S1 disturbance: Concurrent writes to one shared `PlanExecuteState` can collide or introduce nondeterministic result order; a dependent work cell may run before its source-producing predecessor completes or fail correctly.
- Attenuating coordination relation: `WorkerCoordinator._execute_isolated_task` deep-copies shared state; `_merge_isolated_state` reconciles deltas and deduplicates records on the coordinator thread in plan order; dependency checks delay/mark tasks according to predecessor status.
- Feedback into subsequent S1 behaviour: Reconciled `execution_context` and task statuses feed the next scheduling loop's dependency checks and next workers' input/evidence; failed dependencies produce explicit failure records instead of unsafe follow-on execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The isolation plus conflict-avoiding merge specifically regulates parallel state interference and exposes dependency-sensitive response, beyond merely transporting data or starting tasks.
- Decisive decision or feedback right: The first-party deterministic coordinator decides isolation/merge/dependency enforcement under an operator/developer-configured parallel policy; it exposes a function-specific coordination path, but no autonomous agent selects conflict resolution strategies after observing competing worker choices.
- Decision owner: Configured runtime/developer for the existing mechanism; an autonomous S2 response owner would need further composition.
- Supporting / enforcement mechanisms: Task graph, deep snapshot, `ThreadPoolExecutor`, ordered merge, explicit task/error records.
- Closure path: Parallel task launch → isolated local decisions/results → deterministic conflict-safe merge/dependency status → next worker scheduling and shared evidence.
- Boundary reachability: `RunService` constructs `WorkerCoordinator` and the shipped multi-agent factory wires it to the deployed plan-execute-report workflow; “parallel” is an accepted first-party execution mode, not test-only.
- Why this is / is not agent-owned: The S2 function-specific primitive is shipped, but the decisive strategy is a developer-defined algorithm, not an autonomously revised coordination decision. Hence constructor `C`, not `A`.
- Evidence: [parallel isolation/merge/dependency code](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/agents/multi_agent/executor/worker_coordinator.py), [production coordinator wiring](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [parallel isolation deterministic test](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/tests/smoke/test_worker_parallel_isolation.py).
- Basis: Structural.
- Confidence: Moderate; coordination is specific, but autonomous ownership intentionally unclaimed.
- Caveats: Coordinator's deterministic merge may not resolve substantive semantic disagreement between research results; model-authored plan dependencies alone do not earn S2=A.

## S3 — Inside-and-now control

- State: —
- Function: Would regulate shared current priorities, resources, commitments and interventions for the whole operating research organization.
- Disturbance / variety regulated: Token/time/concurrency budgets, recovery, failed tasks, cancellation and paused research.
- Decisive decision or feedback right: Budget policy is preconfigured; runtime enforces caps and recovery classifications; parent operator can pause/cancel a requested run. No actor is shown exercising whole-current discretionary priority/resource bargaining across S1 work cells.
- Decision owner: Developer/configuration and user for limits/supervision; deterministic runtime for state transitions only.
- Supporting / enforcement mechanisms: `BudgetManager`, `StateMachine`, checkpoints, lease owner and `RunService.schedule`.
- Closure path: Configured cap or operator control → runtime enforces pause/retry/fail; no whole-current discretionary S3 decision owner returns changed commitments across the research enterprise.
- Boundary reachability: Not applicable for positive S3.
- Why this is / is not agent-owned: The planner's task graph and the scheduler's budget checks are local workflow decisions/enforcement, not a whole-system current-control view with agent-owned tradeoffs. Generic user pause is not automatically S3=P.
- Evidence: [budget and transitions](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/runtime.py), [run scheduler and control](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py).
- Basis: Structural negative.
- Confidence: Moderate-high.
- Caveats: A wider human research organization could supply parent S3 outside this shipped run boundary.

### Absence scope

- Surfaces inspected: Persistent runtime, budget manager, orchestration, worker coordinator, run scheduler, pause/resume/cancel API path and deployment configuration.
- Plausible first-party paths checked: Whole-current view across research cells/runs, agent-selected resource reallocation, inter-team commitment/prioritization, legitimate parent S3 control decision and returned intervention.
- Why no material first-party path remains: Code exposes per-run fixed policies, task decomposition and operator lifecycle controls, but not a discretionary whole-current metasystem decision/return path.

## S3* — Complementary audit

- State: —
- Function: Would independently sample or challenge operational research claims beyond routine S1–S3 reporting.
- Disturbance / variety regulated: Unsupported citations, inconsistent reports, missing evidence, stale/inaccurate worker assertions and false completion claims.
- Decisive decision or feedback right: The in-line deterministic `ContractEvaluator` checks required sections, citations and ledger coverage; the same ordinary completion path classifies repair/replan/failure. External semantic judges belong to evaluation machinery, not credited production audit.
- Decision owner: Developer-written verification algorithm; no independently deciding complementary auditor shown closing an audit claim into control.
- Supporting / enforcement mechanisms: EvidenceLedger, deterministic verification checks, `ContractVerdict`, checkpoint and failure classifier.
- Closure path: Report → mandatory in-line checks → ordinary run repair/replan/fail; not a separate independent audit channel that can challenge normal operational reporting.
- Boundary reachability: Not applicable for positive S3*.
- Why this is / is not agent-owned: Reading original ledger IDs makes deterministic claim hygiene stronger but does not by itself establish a sufficiently independent discretionary auditor; Proposer/Critic later review a *candidate skill*, not an independently sampled live research output.
- Evidence: [contract evaluator](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/contracts.py), [in-line verification](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/runtime.py), [Skill critic scope](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/review_agents.py).
- Basis: Structural negative.
- Confidence: Moderate-high.
- Caveats: The eval suite may add independent quality evidence when separately executed, but that does not become a shipped operating S3* claim.

### Absence scope

- Surfaces inspected: Evidence/contract pipeline, runtime verify/repair branch, review agent/learning path, test/eval separation and API wiring.
- Plausible first-party paths checked: Separate raw-ground-truth sampling, replay auditor, independently controlled model/evaluator and findings returned into whole-current control.
- Why no material first-party path remains: Operational checks are routine on-path verifiers; model critic audits skill candidates in a different adaptive workflow, while research evaluation scripts do not close a production complementary-audit function.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: Convert experience of the changing user-task/source environment into prospective procedural-skill options and selectively return approved capability changes into later runs.
- Disturbance / variety regulated: Recurring complex research workflows, new retrieval demands, costly/failing approaches and tradeoffs between generalized procedure reuse and permission/source constraints.
- External distinction: Completed user-facing research and its tool traces encode encountered task/source patterns; `ReviewPack` aggregates these environment-facing episodes while active skill catalog and source modes constrain generalization.
- Future / prospective distinction: The Proposer generates an option to create/patch/ignore a **reusable skill for future runs**; the Critic/validation/evaluation sequence checks whether an option should become future available capability rather than only repairing the current report.
- Adaptation option generated: Trace-backed procedure candidate with triggers, limited tools, source modes, machine policy and evaluation cases; a distinct review critic can reject/revise options.
- Path back into current capability / S3: Human confirmation → passed offline evaluation and shadow/canary/active promotion → active skill registry → `SkillLoader.resolve` in context builder for subsequent research runs. Canary outcome can suspend; activation is not automatic.
- Decisive decision or feedback right: In the candidate construction mode, model Proposer/Critic forms an option but has no autonomous authority to alter deployed capability. In a separately supported parent mode, the operator expressly confirms promotion and stage advancement, which controls capability adoption.
- Decision owner: First-party model-supported candidate constructor (`C`) and legitimate operator parent (`P`) for deployment/adaptation right, in distinct supported modes.
- Supporting / enforcement mechanisms: `SkillLearningService` queue/review, candidate registry, validators, offline evaluator and `PromotionPolicy` staged controls.
- Closure path: Environment-facing finished runs → model-reviewed candidate → evaluated option → parent explicit PROMOTE/ADVANCE → active skill selection in future runs; without credentials/enabled mode or parent confirmation no change is claimed.
- Boundary reachability: Production `RunService` constructs enabled learning models conditionally and enqueues terminal runs, exposes `skill_promotion`; FastAPI promotion routes require exact user confirmation, and `ContextBuilder` uses an active `SkillLoader`. This is shipped but optional, not test-only.
- Why this is / is not agent-owned: Model agents generate and critique prospective options, but human approval is the decisive capability-change right. Therefore a first-party constructor plus distinct operationally closed parent mode, not autonomous S4=A.
- Evidence: [production learning wiring](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/services/run_service.py), [review/Proposer path](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/review_service.py), [model Proposer and Critic](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/review_agents.py), [parent promotion contract](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/promotion.py), [API confirmation and stage transition](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/api/v1/learning.py), [loader](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/loader.py).
- Basis: Structural; inference limited to why reusable future skills constitute prospective adaptation rather than episodic task repair.
- Confidence: Moderate; activation sequence wired but no live promotion observed in this review.
- Caveats: This S4 concerns reuse of environment-facing **task capabilities**, not broad market forecasting. Skills learned from only one run can overfit; real efficacy/transfer not measured. With learning disabled, the current deployment has no such S4 path.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Model Proposer/Critic prepares an option; no autonomous deployment owner | Configured post-run learning review with traceable terminal Run | Candidate enters registry for possible evaluation, but further composition/authority is required for capability activation | [review service](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/review_service.py) |
| Parent (`P`) | Explicit human/operator promotion and stage advancement | Evaluated, non-regressing candidate and exact confirmation | Promote to shadow → parent-approved canary/active → subsequent runs load selected active skill | [promotion policy](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/promotion.py), [API](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/api/v1/learning.py) |

## S5 — Policy and identity

- State: —
- Function: Would adjudicate ultimate research-harness identity/policy disputes and bind subsequent operation at the same recursion.
- Disturbance / variety regulated: Source-mode leakage, tool permissions, safety rules, promotion scope and choice of research purpose.
- Decisive decision or feedback right: User chooses run goal/source; configuration, validators and operator promotion govern ordinary capability/risk boundaries, not a live identity/ultimate-policy dispute.
- Decision owner: External user/maintainer for static identity and policy, not a first-party S5 loop.
- Supporting / enforcement mechanisms: Fixed `SourceMode`, machine-policy validation, exact PROMOTE/ADVANCE confirmations and authorization checks.
- Closure path: Per-run source restrictions and Skill promotion approvals enforce known operating boundaries; no identity/policy-level question is escalated to legitimate authority and returned as a new ultimate mandate.
- Boundary reachability: Not applicable for positive S5.
- Why this is / is not agent-owned: An operator approving a learned procedural skill is S4 adaptation in this boundary, not S5 identity closure. Static source constraints are enforcement, not constitutional governance.
- Evidence: [source/run contracts](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/harness/contracts.py), [Skill validators](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/src/deepresearch_agent/evolution/validators.py), [operator promotion](https://github.com/SichengLong26/deepresearch_agent_harness/blob/4c98d6e144fde5bc28c821e6ee2c3b980eecc9a0/backend/app/api/v1/learning.py).
- Basis: Structural negative.
- Confidence: Moderate-high.
- Caveats: Governance of the human research organization or open-source project may have its own S5 outside this product runtime.

### Absence scope

- Surfaces inspected: Source/workflow contracts, permission validators, API controls, learning promotion, configuration and repository project identity.
- Plausible first-party paths checked: Identity-level option/dispute, legitimate governing authority, explicit final policy ruling, return into subsequent entire-organization operation.
- Why no material first-party path remains: All operational paths inspected are task-source configuration, bounded risk enforcement or future-skill activation, not a shipped identity-policy deliberation/return loop.

## Recursion

Model-backed planners and research workers are distinct local operational work cells, but the repository does not show that each contains a separately viable full metasystem or durable environmental identity. Threaded parallelism and a task DAG do not establish another VSM recursion. The whole deployed research service is the chosen level.

## Variety and escalation

Source mode and model/tool budget attenuate risk and cost variety; Planner and research tools amplify inquiry options. The immutable evidence ledger, contract checks and versioned checkpoints preserve provenance and return ordinary failure evidence for model report repair or replan. Pause/cancel and `NEEDS_USER_INPUT` return unresolved task variety to the user; they are not automatically algedonic or S5. Reusable skill adaptation, when configured, is explicitly bounded by evaluation and parent approval. The mechanism's presence does not demonstrate measured reliability or autonomy performance.

## Evidence gaps

No live API/model/provider experiment, replay-quality judge, independent audit, or deployed human promotion trace was performed. The configured optional S4 path is structurally connected through application code and tests but actual transfer quality remains unmeasured. Native pytest suite was not executed because `pytest` was not installed in the assessment environment; the repository's pinned source and its deterministic test contracts were inspected. This limitation affects empirical confidence, not the exact source identity or presence of the shipped model-backed workflow.
