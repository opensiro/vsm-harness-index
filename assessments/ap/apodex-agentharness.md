---
harness_id: apodex-agentharness
project_name: Apodex AgentHarness
repository: https://github.com/ApodexAI/AgentHarness
review_ref: 7cc9e3bfca12ec44930073f20ee3f0732a7950da
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Apodex AgentHarness

## Review boundary

- System in focus: the shipped single-question `react_base` research-solving runtime, not the Apodex model-development organization.
- Purpose and identity: search, fetch and calculate evidence to produce an answer to an assigned research question.
- Relevant environment: question text, web/search results, sandbox outputs and an OpenAI-compatible model endpoint.
- Standard-distribution boundary: public Python package and concrete react_base composition at the pinned commit; default and keep5 YAML profiles and the BenchmarkSession/Harbor entry adapters.
- Credited operating / distribution surfaces: `workflows/react_base`, first-party `agent_harness` loop, tools, role-resource wiring and task execution; benchmark adapters only insofar as they launch this concrete solver.
- Adjacent first-party surfaces excluded from ownership: benchmark datasets, score/judge/rejudge machinery, performance tables, CI and model training/publication. These do not donate metasystem ownership to the solver.
- First-party operating / deployment modes considered: configured research question through BenchmarkSession or Harbor, default and named profiles; no unseen commercial service or unpublished workflow.
- Recursion level: one solver/task cell. Multiple benchmark trials are independent runs, not automatically a coordinated organization.
- Reviewed revision: `7cc9e3bfca12ec44930073f20ee3f0732a7950da`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped [pipeline specification](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/spec.py#L18-L50) has one main_agent node and then END. Its [node composition](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/nodes/main_agent.py#L424-L579) resolves the model, tools, profile, deterministic observers and question, runs the first-party loop and returns final_answer. The [loop](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/core/runtime/loop/agent_loop.py#L191-L360) calls the model, parses chosen tools, executes them and appends observations for later model decisions. Compaction, rollback for empty/duplicate searches and refusals, limits and final-answer extraction bound execution.

Role permissions and model routing are provided by ResourceManager. ProcessManager maintains per-session task status in memory and emits events; scheduler checks stale execution tokens, status and configured wall time. Event/trajectory storage preserves traces, not independent governance. External search/fetch/sandbox/model services supply observations or inference; no external coding-agent loop is borrowed. Human setup selects a question, endpoint, credentials and fixed limits. Contributor/CI and benchmark scoring are separate from the running solver.

## Operational model

One agentic research solver is the S1 unit: it decides what evidence to request next and when to answer. The model-backed actor owns those local operational choices; Python dispatch, timeouts, tool schemas and limits enforce the preconfigured envelope. Removing the model actor leaves transport and rules but no substantive research strategy. This is sufficient for agentic S1 inclusion even though the primary entry surface is an evaluation harness. No benchmark performance or verification-centric model description is used as higher-function evidence.

## S1 — Operations

- State: A
- Function: transform a research question into an evidence-informed answer through selected web and calculation actions.
- Disturbance / variety regulated: incomplete results, changing query evidence, failed or empty tool observations and question-specific reasoning.
- Decisive decision or feedback right: select the next search/fetch/code call and arguments or emit the final answer.
- Decision owner: the model-backed react_solver agent.
- Supporting / enforcement mechanisms: provider client, tool execution, role permissions, bounded iteration/retries, compaction and observer interventions.
- Closure path: tool result enters message history; subsequent model turn changes evidence acquisition or returns a final answer, copied to terminal output.
- Boundary reachability: the shipped react_base node directly calls run_agent_loop with registered tools and returns its output; no developer must invent an additional agent workflow.
- Why this is / is not agent-owned: substantive research choices disappear if the agent is removed while dispatcher and limits remain; the runtime does not prescribe the sequence of evidence requests.
- Evidence: [loop response and tools](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/core/runtime/loop/agent_loop.py#L214-L360); [reachable composition](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/nodes/main_agent.py#L443-L579).
- Basis: structural.
- Confidence: high.
- Caveats: source-supported ownership, not an observed live quality or reliability measurement; bounded retries/forced summarization can terminate or constrain the actor.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function established at the single-solver boundary.
- Disturbance / variety regulated: duplicate/empty queries within one solver are local S1 disturbances, not interference between distinct S1 units.
- Decisive decision or feedback right: no S2-specific coordination choice identified.
- Decision owner: not established.
- Supporting / enforcement mechanisms: single-node DAG, task IDs, stale-run checks and observer rollback.
- Closure path: local result/rollback returns to the same solver; not inter-unit mutual adjustment.
- Why this is / is not agent-owned: tool plurality and concurrent benchmark trials do not supply a coordination actor.
- Evidence: [one-node graph](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/spec.py#L18-L50); [scheduler](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/scheduling/scheduler.py).
- Basis: structural.
- Confidence: high.
- Caveats: extensible graph types do not establish an additional shipped coordinated organization.

### Absence scope

- Surfaces inspected: react_base specification/node/observers, scheduler, ProcessManager, graph and role registration, benchmark task entry.
- Plausible first-party paths checked: query deduplication, graph sequencing, task/execution-token state and parallel evaluation orchestration.
- Why no material first-party path remains: these regulate one solver or isolate trials; no distinct interacting S1 units with specific conflict attenuation and returned coordination are shipped in the assessed composition.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-cell current-control function separate from S1 execution and preselected limits.
- Disturbance / variety regulated: token/context/time exhaustion and task interruption are enforced mechanically.
- Decisive decision or feedback right: budgets and role resources are selected in profiles/configuration; no in-boundary discretionary whole-system regulation established.
- Decision owner: configuration author/operator for setup; no evidenced S3 owner.
- Supporting / enforcement mechanisms: BudgetObserver, ResourceManager, scheduler wall-time checks, pause hook and status transitions.
- Closure path: configured thresholds stop/warn the loop; no qualifying autonomous or parent current-control decision-return loop.
- Why this is / is not agent-owned: an agent can choose ordinary task actions within limits but does not own allocation of a whole organization's current resources.
- Evidence: [budget enforcement](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/components/observers/budget_observer.py#L17-L67); [role resources](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/core/runtime/resources/manager.py); [pause bridge](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/core/runtime/pause_check.py).
- Basis: structural.
- Confidence: high.
- Caveats: APIs that could support future supervision do not establish function-specific constructor or P closure.

### Absence scope

- Surfaces inspected: profiles, resource/permission manager, budget/context observers, scheduler, ProcessManager, pause hooks and benchmark entry configuration.
- Plausible first-party paths checked: operator abort/pause, token warnings, provider routing, configurable resource envelopes and graph status.
- Why no material first-party path remains: these supply fixed setup or per-task lifecycle enforcement, without a whole-current organizational view, decisive bargaining/intervention owner and returned supervisory decision in the shipped mode.

## S3* — Complementary audit

- State: —
- Function: no complementary corrective audit of the operational cell established.
- Disturbance / variety regulated: trajectory visibility, malformed calls and benchmark answer scoring.
- Decisive decision or feedback right: observers apply routine production rules; benchmark judges compute evaluation results outside solver control.
- Decision owner: no in-boundary independent audit actor with corrective return.
- Supporting / enforcement mechanisms: trajectory/SSE observers, normalizers, rollback, answer extraction and separate benchmark judges.
- Closure path: production observers alter the same loop; evaluation/rejudge produces scores rather than an in-boundary corrective-control return.
- Why this is / is not agent-owned: independent model-based scoring alone cannot donate S3* to the running solver.
- Evidence: [observer assembly](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/nodes/main_agent.py#L166-L214); [benchmark runner](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/benchmarks/runner/run_one_task.py); [judges](https://github.com/ApodexAI/AgentHarness/tree/7cc9e3bfca12ec44930073f20ee3f0732a7950da/benchmarks/judges).
- Basis: structural.
- Confidence: high.
- Caveats: this does not deny the usefulness of external evaluation; it limits ownership to the declared runtime.

### Absence scope

- Surfaces inspected: first-party loop, observer assembly/implementations, trajectory storage, benchmark runner, answer extraction and judge/rejudge code.
- Plausible first-party paths checked: rollback checks, logged evidence inspection and post-run model judges.
- Why no material first-party path remains: checks in production are routine self-path feedback; complementary evaluation is adjacent and has no wired return changing this solver's organizational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective adaptation of the solver's present capability established.
- Disturbance / variety regulated: external web information relevant to the assigned question.
- Decisive decision or feedback right: research actions answer the current task; no evidenced adaptation-option decision returned to present capability.
- Decision owner: S1 agent for current research; no S4 owner.
- Supporting / enforcement mechanisms: web tools, context compaction, profiles and traces.
- Closure path: evidence changes the answer, not the organization's future capability.
- Why this is / is not agent-owned: external research is the primary transformation here, not automatically metasystem intelligence.
- Evidence: [research node](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/nodes/main_agent.py#L424-L579); [profile loader](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/profile.py); [workflow compaction](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/compactors.py).
- Basis: structural.
- Confidence: high.
- Caveats: the model's training or future operator use of benchmark results is outside the assessed solver.

### Absence scope

- Surfaces inspected: search/fetch/code tools, react_base prompts/profile/compactor, node and loop, benchmark result/rejudge entry points.
- Plausible first-party paths checked: web sensing, model/profile selection, context/history reuse and evaluation feedback.
- Why no material first-party path remains: no shipped external-and-prospective adaptation-options loop returns a selected capability change into the solver; ordinary research and setup do not satisfy S4.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure established.
- Disturbance / variety regulated: task scope and tool/model constraints fixed by setup.
- Decisive decision or feedback right: no first-party identity-level matter→legitimate authority→returned governing decision path found.
- Decision owner: developer/operator sets static purpose and configuration; no evidenced S5 closure.
- Supporting / enforcement mechanisms: system prompt, role permissions, profiles, limits, project license.
- Closure path: static constraints govern actions, without a function-specific runtime policy dispute and authoritative return.
- Why this is / is not agent-owned: model task answers and configuration enforcement are not ultimate-policy decisions.
- Evidence: [prompts](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/workflows/react_base/prompts.py); [permissions](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/agent_harness/core/runtime/resources/permissions.py); [README](https://github.com/ApodexAI/AgentHarness/blob/7cc9e3bfca12ec44930073f20ee3f0732a7950da/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: legitimate maintainers exist; their repository development does not itself close runtime S5 at this boundary.

### Absence scope

- Surfaces inspected: prompts, profiles, permission/resource registry, task lifecycle and operator setup documentation.
- Plausible first-party paths checked: model/tool configuration, pause/abort, fixed research identity and contributor authority.
- Why no material first-party path remains: no shipped identity-level escalation and authoritative governing return beyond static setup; future custom governance remains hypothetical.

## Distributed OSS parent arrangement

Public contributions and configuration authorship are not evidence of organization-level P at the single-solver boundary. No distributed parent S3/S4/S5 return was established.

## Self-hosted and non-human modes

Self-hosting the endpoint changes infrastructure and model choice, not the ownership topology supported here. No separate function-specific parent mode is established by credentials or stop APIs.

## Recursion

Task IDs, graph nodes, tools and benchmark trials are not recursively viable units. Only the single operational solver is credited.

## Variety and escalation

Search/code observations amplify operational distinctions; compaction and guardrails attenuate them. Empty-search/refusal/duplicate rollback and retry policies are local mechanisms. Errors, stop reasons and traces make failures visible but do not themselves establish an algedonic channel or higher-function owner.

## Evidence gaps

No live model/provider execution, benchmark reproduction or performance judgment was performed. Source shows the operational decision/return path; it does not prove answer quality, effective reliability or viability. No material unresolved shipped higher-function path remains within the stated react_base boundary. Other future/commercial workflows are outside scope.
