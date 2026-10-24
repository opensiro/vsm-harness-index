---
harness_id: pi-multi-agent
project_name: Pi-Multi-Agent
repository: https://github.com/jwangkun/Pi-Multi-Agent
review_ref: d2fef0f30a762ec04eff9d8dde6cd406648955bc
reviewed_at: 2026-10-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pi-Multi-Agent

## Review boundary

- System in focus: The first-party TypeScript agent-orchestration library and its documented installed Direct, Deep/AgentCluster, and Workflow operating modes, including exported `Agent`, `LLMAgentCollaboration`, `Orchestrator`, `DeepPlanner`, `AgentCluster`, and workflow runtime; not the organization that maintains this repository.
- Purpose and identity: Carry out user-defined research, synthesis, writing and other agent tasks through model-backed operational actors, optional teamwork, tools and controlled workflow execution.
- Relevant environment: Changing user goals and task outputs, model responses, tool results and failures, available model providers, token budgets and concurrent agents; organizational competition and future provider shifts are not automatically managed by the runtime.
- Standard-distribution boundary: Shipped `src/` public API and documented Direct/Deep/Workflow composition under a user-supplied model key and settings. Models perform inference externally but are deliberately wired to first-party agent calls. This is not a claim that the package supplies model weights or a fully assembled agent team without user configuration.
- Credited operating / distribution surfaces: [library exports](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/index.ts), [agent/tool/retry loop](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/core/agent.ts), [LLM collaboration methods](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/collaboration/llm-collaboration.ts), [deep planner](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/deep-planner.ts), [cluster execution/current-control feedback](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts), [workflow runtime](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/workflow/runtime.ts).
- Adjacent first-party surfaces excluded from ownership: Examples, test fixtures, README screenshot/demo/dashboard claims, contributor maintenance, CI, package release, and any user-written workflow script or externally hosted model/provider governance. Model decisions are credited only where the shipped library actually calls and returns them; a configurable graph/topology alone is not credited as an organization.
- First-party operating / deployment modes considered: `Agent` with injected `AgentExecutor` and tools; `LLMAgentCollaboration` sequential/parallel/debate/critic/hierarchical methods; `DeepPlanner` plus `AgentCluster` with external OpenAI-compatible inference and built-in tool/review/retry path; programmatic `runWorkflowScript` with user or generated workflow source, model provider, token/concurrency budgets and callbacks; ordinary self-hosted Node.js use. No actual provider request or live agent was run for this review.
- Recursion level: One execution of a goal by a composed group of first-party-wired agent work cells. Individual tool calls, model requests, task steps, and nested workflow scripts are not automatically recursively viable systems.
- Reviewed revision: `d2fef0f30a762ec04eff9d8dde6cd406648955bc`, frozen in [discovery #2024](https://github.com/opensiro/vsm-harness-index/issues/2024) and [serial assessment control #2025](https://github.com/opensiro/vsm-harness-index/issues/2025).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`src/core/agent.ts` executes a configured prompt through the injected `AgentExecutor`, can expose callable tools and task/handoff message handling, tracks states and retries, and returns result/event feedback. `src/orchestration/planner.ts` provides a mostly keyword-based task/dependency constructor, while `src/orchestration/deep-planner.ts` explicitly asks an external LLM to propose subtasks, priority, role and tools. `AgentCluster` invokes model-backed subtask actors with tool-call turns, dependent result context and shared memory, stores task progress, scores iterations, applies bounded retries, and synthesizes an output; final `DeepEvaluator` judges report quality. `LLMAgentCollaboration` supplies separate serial, parallel, debate, review and hierarchical operational modes. The workflow runner executes a caller-supplied script against `agent`, `parallel`, `pipeline`, phase/log and bounded model-call APIs; `TokenBudget` and concurrency settings constrain execution rather than make agent-level policy choices. [core agent](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/core/agent.ts), [orchestrator](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/orchestrator.ts), [cluster](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts), [shared memory](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/memory/enhanced-shared-memory.ts), [workflow](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/workflow/runtime.ts).

The package is a library with users choosing goals, API credentials, configured agents, provider and budgets. It offers no evidence of a single always-running organizational fleet. Developer tests and bundled sample workflows validate/illustrate APIs but are not independently credited S-functions. No live model inference, scripted end-to-end agent-quality experiment, or unpinned dependency execution was performed.

## Operational model

In a supported installed mode an operator supplies a goal and provider credentials; a first-party plan/execution path generates role-specific requests and gives outputs/tool results back to model-backed S1 work cells. Deep mode can allocate concurrent subtasks and later revise execution prompts/priorities when global output quality is weak. The separate collaboration API can make multiple configured LLM agents debate each other's arguments across several rounds. These are *different selectable first-party modes*: a positive path in one is not attributed to another without wiring. Higher-order authority remains bounded by the developer's selected library calls and constraints. The package's current task management and reports do not themselves demonstrate an independent organization-level identity authority.

## S1 — Operations

- State: A
- Function: Model-backed work cells turn user goals and subtasks into generated outputs or tool-mediated action within the supported installed library modes.
- Disturbance / variety regulated: Unpredictable task text, model output, tool responses and failed attempts; an actor must interpret each returned result and choose subsequent content or tool calls.
- Decisive decision or feedback right: A model-backed `AgentExecutor` chooses task response; in the cluster mode, the model selects offered function calls or a final answer, conditioned by prior tool output.
- Decision owner: The composed configured autonomous model-backed work-cell actor. First-party TypeScript executes transport/retry/tool effects; external model inference supplies bounded work discretion.
- Supporting / enforcement mechanisms: Prompt construction, context, tool definitions, message bus, state events, timeouts/retries, concurrency and token budgets, model router, result persistence.
- Closure path: Goal/subtask → first-party `Agent.execute` or `AgentCluster.executeLLMCall` → model response/tool-call choice → first-party tool execution and returned result → next model turn or task completion → output to user/plan.
- Boundary reachability: Both `Agent.execute()` and cluster `executeSubTaskWithTools()` are shipped and exported or invoked from public APIs, not in sample/test code only. The latter loops over real model-reported tool calls and feeds tool returns into the next model request.
- Why this is / is not agent-owned: Removing the model-backed actor leaves deterministic calls and retries, but not the flexible task-content/tool-choice decision. The package's own agent loop operationally wires those decisions rather than merely naming an external agent.
- Evidence: [agent model executor and result](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/core/agent.ts#L116-L233); [cluster model/tool loop](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L273-L357); [public exports](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/index.ts#L1-L110).
- Basis: Structural model-to-tool-to-model wiring; documented supported model-backed modes.
- Confidence: High for first-party implementation path; no empirical assertion of task effectiveness.
- Caveats: The generic `AgentExecutor` is injected by the embedding application; first-party `AgentCluster` supplies the concrete OpenAI-compatible tool-call loop. The external provider is not itself part of the package's codebase.

## S2 — Coordination

- State: C
- Function: In the exposed debate mode, mitigate incompatible contributions from two or more independently answering agent work cells by returning their earlier positions as a shared dispute context for later rounds.
- Disturbance / variety regulated: Contradictory claims or counterarguments across S1 work cells can make the group's combined response incoherent.
- Distinct S1 units: The separately configured `LLMAgent` actors passed into `executeDebate`, each with its own system prompt and model invocation.
- Inter-S1 disturbance: The built-in debate procedure intentionally elicits differing positions and **counterarguments**; unresolved cross-agent disagreement is the structurally represented interference, not mere concurrent invocation.
- Attenuating coordination relation: `debateHistory` accumulates each agent's previous position; subsequent `round > 0` prompts include those other arguments and request counterarguments/supporting evidence; an LLM moderator then summarizes a consensus candidate.
- Feedback into subsequent S1 behaviour: The history is included in each actor's next-round prompt, changing its available distinctions and potential reply; moderator synthesis provides a collective outcome to the caller.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This shipped method explicitly stages disagreement, re-presents opposing positions to the same actors and seeks a reconciled summary, unlike generic message-bus, dependency graph or speaker-selection APIs.
- Decisive decision or feedback right: Framing disagreement as counterargument on the next agent turn and proposing synthesis after the rounds; the first-party method supplies a particular reconciliation channel, but developer-supplied agents and prompts determine substantive convergence.
- Decision owner: First-party S2-specific **constructor** for the debate feedback relation; the configured model-backed debate participants and synthesized moderator judgment own content choices. No general cross-team autonomous conflict policy is established.
- Supporting / enforcement mechanisms: Debate transcript accumulation, fixed `maxRounds`, serial model requests and final moderator request.
- Closure path: Two or more agents provide positions → `debateHistory` collects responses → successive turns receive opposing positions → mediator model produces a consensus summary returned to the caller.
- Boundary reachability: `LLMAgentCollaboration.executeDebate` is exported in the first-party public library API and directly implements the feedback path; it requires the integrating developer to supply at least two agent configurations and invoke the mode.
- Why this is / is not agent-owned: Agent replies to conflict are model-authored, but the coordination mode and final synthesis are intentionally constructed by the framework and do not give an autonomous controller discretion to configure the whole debate/conflict policy. Hence `C`, not general S2 `A`.
- Evidence: [LLM debate implementation](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/collaboration/llm-collaboration.ts#L171-L242); [API export](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/index.ts#L22-L35); [contrast: shared memory](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/memory/enhanced-shared-memory.ts#L114-L185).
- Basis: Structural first-party debate-with-return path; inferred organizational disturbance as opposing work-cell claims.
- Confidence: Medium. Code proves the feedback construction, not that every model debate reduces actual conflict.
- Caveats: This state is **limited to the opt-in debate mode**, not generic inter-agent messaging. The separate `DebateAndConsensus` implementation in `patterns.ts` does not replay its accumulated history into future rounds, so it is **not** used as the S2 witness. No cross-run contention governance or demonstrated autonomous negotiation authority is claimed.

## S3 — Inside-and-now control

- State: C
- Function: Monitor the whole *current deep-mode goal execution* and regulate which weak work cells receive higher priority and revised instructions on the next iteration.
- Disturbance / variety regulated: Subtask output failures, underlength responses and insufficient quality across an active goal plan threaten the entire deliverable under bounded retries/iterations.
- Whole-system current view: `AgentCluster` maintains one `currentPlan`, results across subtasks, progress map, token usage and scoring over all plan subtasks, with access to `DeepPlanner`-supplied priorities.
- Current-control decision scope: `replanForIteration` checks results against weak-task criteria, raises weak task `priority` to `high` and modifies their prompts; the modified plan is used for the next execution iteration and per-task model selection.
- Decisive decision or feedback right: Select current weak tasks for increased priority and mandatory additional evidence/detail; presently implemented by a developer-coded threshold and template, not discretionary whole-system agent governance.
- Decision owner: First-party **deterministic constructor** implementing a narrow quality/current-allocation relation. Operator sets maximum iterations, initial goal and provider; the model does not own the hard-coded weak-task threshold.
- Supporting / enforcement mechanisms: Shared memory, progress/events, model router, tool records, fixed `maxIterations`, score threshold, queue and timeout/budget settings.
- Closure path: Complete an iteration → review all current subtask outputs/quality score → flag weak tasks and revise plan priorities/prompts → `executeIteration` / `resolveComplexityHint` consumes modified task attributes in the next run.
- Boundary reachability: `executePlan` invokes `evaluateIterationResults()` and `replanForIteration()` directly, replaces `currentPlan`, then runs the next iteration; model selection reads the same updated `SubTask.priority` in this shipped deep mode.
- Why this is / is not agent-owned: The current-control adjustment is observable in shipped code, but removing a putative manager LLM leaves the same hard-coded weak-task threshold/priority decisions. Thus this is narrow S3 construction `C`, **not** `A`; runtime enforcement and budget limits have no independent managerial ownership.
- Evidence: [whole plan/quality/replan loop](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L150-L218); [current result scoring and intervention](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L399-L435); [revised task model selection](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L253-L273).
- Basis: Structural, confined to the deep goal-team recursion.
- Confidence: Medium for function scope and constructor ownership; low for empirical quality effectiveness.
- Caveats: This is *one goal plan*, not a live organization-wide resource manager. No adaptive autonomous cross-goal budgeting, conflict intervention or parent S3 mode is established. `Orchestrator` worker assignment, token-budget enforcement and dashboard status alone are not additional S3 evidence.

## S3* — Complementary audit

- State: —
- Function: No first-party sufficiently independent complementary access to operational reality is established beyond ordinary production quality checks.
- Disturbance / variety regulated: Work cells might misstate facts or output correctness, but normal critic/quality scoring is embedded in the production loop.
- Decisive decision or feedback right: No separate audit judgment with independently sourced operational facts and returned corrective S3 decision is evidenced.
- Decision owner: Ordinary model critic/evaluator and deterministic quality heuristics support production QA, not an independent metasystem auditor.
- Supporting / enforcement mechanisms: `DeepEvaluator`, heuristic iteration score, `CriticReviewer`, reviewer round, log and progress snapshots.
- Closure path: Critic feedback can reach the creator in a routine production review; the final `DeepEvaluator` score affects the final success classification but does not initiate a complementary audit correction of a separate operational report.
- Why this is / is not agent-owned: A second model call or different prompt does not by itself establish independence of evidence, ownership or an alternative audit channel.
- Evidence: [DeepEvaluator input/output and fallbacks](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/deep-evaluator.ts#L65-L255); [producer-owned quality iteration](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L166-L218); [routine critic-reviewer](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/collaboration/llm-collaboration.ts#L304-L360).
- Basis: Bounded negative first-party source inspection.
- Confidence: Medium-high.
- Caveats: Embedding applications could separately implement external audits; their unshipped organization is outside the declared library boundary.

### Absence scope

- Surfaces inspected: Core agent reporting, deep-mode iteration and evaluator, collaboration reviewer, shared-memory snapshots, workflow events and provider routing.
- Plausible first-party paths checked: `DeepEvaluator` quality verdict, `CriticReviewer` feedback, debate moderator, operation log and snapshot, tool result traces.
- Why no material first-party path remains: They inspect or summarize the same production outputs as routine workflow quality gates, without a separate independent evidence-acquisition route or audit finding entering whole-current corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supported first-party loop models a future external environment, generates prospective capability options and returns an adaptation choice into present operations.
- Disturbance / variety regulated: Future model capability/provider changes, users and research-domain shifts could require adaptation, but present wiring only handles the current assigned goal.
- Decisive decision or feedback right: Not established for outside-and-then adaptation; task replanning improves current responses under existing capabilities.
- Decision owner: Human/developer chooses model/provider settings and upgrades; no evidenced agent S4 or function-specific parent adaptation mode.
- Supporting / enforcement mechanisms: Model registry, complexity estimator, tool search, current-goal `DeepPlanner`, memory and current-iteration replan.
- Closure path: The runtime reacts to current task and quality feedback; it does not propose an externally grounded future organizational adaptation and enact it through S3.
- Why this is / is not agent-owned: Model routing chooses configured endpoints for current subtasks, while the planner changes the current deliverable—not the organization's future capability/operating model.
- Evidence: [task-centric deep planning](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/deep-planner.ts#L92-L200); [short-loop replanning](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/orchestration/agent-cluster.ts#L399-L435); [model registry/routing](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/models/router.ts).
- Basis: Bounded negative at the shipped runtime modes.
- Confidence: Medium-high.
- Caveats: A user can ask the task agents to write a future-looking research report, which is an S1 task output, not automatically adaptation of this harness's operational capability.

### Absence scope

- Surfaces inspected: DeepPlanner prompts/replan, task result evaluator, model registry/router, workflow generator/runtime, memory and top-level modes.
- Plausible first-party paths checked: `createDeepPlan`, `DeepPlanner.replan`, `AgentCluster.replanForIteration`, tool-driven web search, selecting configured providers, workflow scripts and persistence.
- Why no material first-party path remains: Those paths elaborate or repair a current user task or apply preconfigured model choices. No first-party future-external sensing → adaptation-option judgment → S3/current-capability return is wired as a standing S4 function.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy deliberation and authoritative return path is supplied for this multi-agent organization.
- Disturbance / variety regulated: Role boundaries, sensitive tools, provider credentials and resource budgets create policy concerns, but shipped controls are static user/developer configuration and task execution gates.
- Decisive decision or feedback right: Not established at identity/ultimate-policy level. Runtime validates workflow metadata/schema and observes execution constraints; operator config sets goals and credentials.
- Decision owner: Human/developer provides overall purpose and limits externally; model-backed worker prompts do not receive ultimate identity authority. No packaged parent mode closes identity-level disputes and feeds binding governance back.
- Supporting / enforcement mechanisms: System prompts, `TokenBudget`, concurrency limit, tool list, prompt/schema validation, cancellation, config and runtime errors.
- Closure path: Configured constraints restrict a run, but no identity/policy issue is routed to legitimate authority and its resolution returned into ongoing organizational policy.
- Why this is / is not agent-owned: The ability to generate or execute a script and enforce an operator's token budget is not the right to revise ultimate policy.
- Evidence: [workflow runtime constraint path](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/workflow/runtime.ts#L1-L152); [fixed agent config and tool selection](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/src/core/agent.ts#L35-L90); [public modes](https://github.com/jwangkun/Pi-Multi-Agent/blob/d2fef0f30a762ec04eff9d8dde6cd406648955bc/README.md#L46-L126).
- Basis: Bounded negative source review.
- Confidence: Medium-high.
- Caveats: The maintainer's outside repository governance and a private downstream organization's human policy are not credited as this installed harness's S5(P).

### Absence scope

- Surfaces inspected: Public library API, agent config and system prompt, workflow budget/VM constraints, orchestration errors, reviewer prompt, README modes and local settings.
- Plausible first-party paths checked: Model prompts as identity, configurable role/policy, operator-supplied budgets, workflow-script validation, manual cancellation and external contributor governance.
- Why no material first-party path remains: Each governs task-level execution or static integration settings. None supplies an ultimate-policy question → legitimate decision owner → authoritative return → subsequent operation governed by a revised identity decision.

## Distributed OSS parent arrangement

Open-source contributors and independent embedding applications do not form one shared operational parent in this source. Source control, releases, submitted issues and maintainer approval govern development of the library, not S3/S4/S5 of a specific installed multi-agent run. No organization-level `(P)` is inferred from separate human users or contributor cells.

## Self-hosted and non-human modes

The Node library and model-provider configuration can be self-hosted or embedded. It can run multiple model-backed cells without an always-present human supervisor, and the caller can supply custom scripts/agents, but neither choice proves a parent-governed organizational control/adaptation/identity loop. A configured provider or scripted scheduler is not a non-human autonomous S3/S4/S5 owner just because it executes decisions.

## Recursion

Individual model-backed agents execute distinct tasks and can consume separate tool environments, but the repository does not demonstrate their own independent S2–S5 metasystems as recursively viable organizations. Nested subtask/depth metadata is technical decomposition only. The S2 and S3 ratings concern the **composed active goal team**, not the child agent or an entire network of deployments.

## Variety and escalation

Tasks, tool returns and model responses introduce operational variety. Context/tool results amplify a work cell's information, while scoring, bounded retries and fixed model selection attenuate available response variety. Debate feedback presents other work-cell claims to later rounds. Failed calls, task errors, timeout/budget exhaustions and workflow logs inform the caller but are not automatically exceptional algedonic channels or metasystem policy events. External provider or user action remains necessary when the existing task bound cannot be absorbed.

## Evidence gaps

- No live LLM calls or external provider endpoints were tested. The evidence is bounded to the pinned first-party source and public operating docs, not effectiveness in actual tasks.
- `S2=C` is limited to deliberate debate/counterargument coordination, not generic multi-agent messaging or global collision prevention; substantive consensus depends on supplied agent configurations and model outputs.
- `S3=C` is narrowly the current deep-mode plan-quality/resource-priority loop; it does not assert an independent, always-on organizational supervisor, human S3(P), or dynamic autonomous budget allocation.
- CI/tests/examples and adjacent dashboards may demonstrate code correctness but do not supply first-party independent S3* authority or organizational S4/S5 governance.
