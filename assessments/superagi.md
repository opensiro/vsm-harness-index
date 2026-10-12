---
harness_id: superagi
project_name: SuperAGI
repository: https://github.com/TransformerOptimus/SuperAGI
review_ref: c3c1982e7bd6a11cfed53c5a193ea502f924b1b6
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: ?
---

# SuperAGI

## Review boundary
- System in focus: the shipped self-hosted SuperAGI agent-execution backend, model/tool step handlers, task queue, scheduled-execution runtime and first-party operator API.
- Purpose and identity: construct and run configurable autonomous task agents whose model responses select tools and iterative work, under human-chosen configurations and permissions.
- Relevant environment: user/project tasks, model providers, external APIs/tools, credentials, persistent executions, Redis/Celery, database, schedule and permission requests.
- Standard-distribution boundary: pinned 2025-01-22 first-party Python backend and compose/CLI operating mode ([README.MD](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/README.MD); [docker-compose.yaml](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/docker-compose.yaml)); cloud product claims, future features and third-party marketplace integrations not instantiated here are excluded.
- Credited operating / distribution surfaces: [main.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/main.py); [superagi/worker.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/worker.py); [superagi/jobs/agent_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/agent_executor.py); [superagi/agent/agent_iteration_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_iteration_step_handler.py); [superagi/agent/agent_tool_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_tool_step_handler.py); [superagi/controllers/agent_execution.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution.py); [superagi/controllers/agent_execution_permission.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution_permission.py).
- Adjacent first-party surfaces excluded from ownership: repo maintenance/CI, examples/tests, unrelated marketing and hosted SaaS, prompts not reached by executable handlers, third-party marketplace tools and external model internals.
- First-party operating / deployment modes considered: configured model/tool workflow step, iteration workflow, agent task queue mode, waiting-for-permission, scheduled run, web/API operator control. No unverified external multi-agent control-plane owner credited.
- Recursion level: one configured agent run as operating unit, with self-hosted deployment supervising multiple such runs; not the SuperAGI vendor's organization.
- Reviewed revision: `c3c1982e7bd6a11cfed53c5a193ea502f924b1b6`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The pinned Docker/worker service uses Celery tasks that call AgentExecutor. The executor loads a persisted AgentExecution and config, selects the corresponding agent tool/iteration/wait handler and schedules subsequent steps. Its stop/permission/iteration gates are host-coded. The iteration handler constructs a prompt from prior feeds, calls a configured LLM, parses a model response, routes it to the output handler, persists status and transitions the workflow. A separate tool handler runs configured tools, requests user permission when required, and follows authored next-step edges ([superagi/worker.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/worker.py#L49-L73); [superagi/jobs/agent_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/agent_executor.py#L39-L127); [superagi/agent/agent_iteration_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_iteration_step_handler.py#L46-L119); [superagi/agent/agent_tool_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_tool_step_handler.py#L39-L96)).
A TaskQueue is local to an agent-execution identifier, uses model-written task items, and feeds selected tasks back into that same run ([superagi/agent/queue_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/queue_step_handler.py#L35-L74); [superagi/agent/task_queue.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/task_queue.py)). A scheduled-execution service creates configured agent executions ([superagi/jobs/scheduling_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/scheduling_executor.py#L23-L84)); API exposes execution status and permission handling ([superagi/controllers/agent_execution.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution.py#L296-L407); [superagi/controllers/agent_execution_permission.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution_permission.py#L90-L155)).

## Operational model
An agent run's active task-directed choice is delegated to an LLM response inside an iteration/tool workflow. Host-coded step edges, queues, scheduled triggers, token budgets, and manual permission decisions enforce or constrain the run. Multiple runs exist, but this does not alone establish an inter-S1 regulating relationship or organization-level strategic decision owner.

## S1 — Operations
- State: A
- Function: Agentic tool/task execution driven by model responses, iterating on tool outcomes and runtime feedback.
- Disturbance / variety regulated: Task requirements, tool errors, external service responses, acquired files/knowledge, token and execution limits.
- Decisive decision or feedback right: Select task responses/tool calls and follow evidence-driven next actions in an active run.
- Decision owner: Configured LLM-driven agent in a first-party execution handler; configured workflow edges and permission guards limit reachable acts.
- Supporting / enforcement mechanisms: Celery worker, persisted AgentExecution, prompt/model adapters, ToolExecutor, agent feed and workflow steps, max-iteration checks.
- Closure path: Configured prompt and feed → model reply → parsed action/tool output → execution feed/status → model's next step or completion.
- Boundary reachability: first-party compose worker invokes the agent executor, which invokes the actual iteration or tool handler. [superagi/worker.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/worker.py#L66-L73); [superagi/jobs/agent_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/agent_executor.py#L83-L127).
- Why this is / is not agent-owned: The LLM determines context-dependent task and tool choices rather than only replaying static workflow nodes.
- Evidence: [superagi/agent/agent_iteration_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_iteration_step_handler.py#L46-L118); [superagi/agent/agent_tool_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_tool_step_handler.py#L39-L70); [superagi/agent/output_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/output_handler.py).
- Basis: structural
- Confidence: high
- Caveats: No live provider-backed task execution or benchmark performance verified; this is source-relative functional ownership, not capability quality.

## S2 — Coordination
- State: —
- Function: No first-party conflict-specific regulating/feedback path among distinct independently acting agent S1 units established in the reviewed standard distribution.
- Disturbance / variety regulated: Possible concurrent run contentions are an architectural risk, but task queue operations are intra-run sequencing, not demonstrated interference regulation.
- Decisive decision or feedback right: No inter-S1 interference-attenuation owner found in the examined orchestrated execution paths.
- Decision owner: Not established for positive S2; developer-authored workflow handlers and Celery scheduling select local execution transitions.
- Supporting / enforcement mechanisms: Per-agent TaskQueue, queue status, Celery job scheduling, running/permission status and tool transitions.
- Closure path: Per-run queue feeds an action back to its own execution, not a collision-specific adjustment of independently acting S1 units.
- Why this is / is not agent-owned: Creating parallel agents or selecting the next task does not satisfy the distinct S1, interference, attenuation and feedback conjunction.
- Evidence: [superagi/agent/task_queue.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/task_queue.py); [superagi/agent/queue_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/queue_step_handler.py#L35-L74); [superagi/jobs/agent_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/agent_executor.py#L39-L100); [superagi/jobs/scheduling_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/scheduling_executor.py#L23-L84).
- Basis: structural
- Confidence: medium
- Caveats: Scope is the 2025-01-22 self-hosted shipped backend; separate third-party extensions or the modern hosted product are not credited.
### Absence scope
- Surfaces inspected: entrypoint/compose, Celery worker and scheduling executor, per-run AgentExecutor, iteration/tool/queue handlers, persistent TaskQueue, API execution state and workflow transitions.
- Plausible first-party paths checked: parallel agent creation, per-agent scheduling, queue insertion/consumption, executor retry and next-step transitions, permission gating and run monitoring.
- Why no material first-party path remains: these observed paths govern one run or generic queue/permission state; none is a shipped distinct-S1 contention sensor plus specific attenuation action returning to subsequent S1 decisions in this assessed distribution.

## S3 — Inside-and-now control
- State: ?
- Function: Execution API provides cross-run observability and human controls, but whole-system current-control decision scope and returned authority path remain unresolved.
- Disturbance / variety regulated: Multiple run statuses, workflow priority, execution permission and resources.
- Decisive decision or feedback right: User/API can create/update agent executions and permission outcomes, yet a scoped whole-current commitment/resource choice has not been traced.
- Decision owner: Operator/API endpoints and possibly host runtime; exact discretionary S3 owner unresolved.
- Supporting / enforcement mechanisms: status queries, execution update API, token ceilings, max-iteration stop and schedule triggers.
- Closure path: Individual run control returns to executor; organization-wide feedback/commitment control not established.
- Why this is / is not agent-owned: Monitoring and stop status are not themselves current-control authority and do not establish a parent S3 mode.
- Evidence: [superagi/controllers/agent_execution.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution.py#L296-L407); [superagi/jobs/agent_executor.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/jobs/agent_executor.py#L39-L101); [superagi/controllers/budget.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/budget.py).
- Basis: unknown
- Confidence: low
- Caveats: Need determine whether dashboard/API has a first-party, supported whole-current resource/commitment decision and feedback loop at deployment recursion. No S3=P is inferred from generic operator controls.

## S3* — Complementary audit
- State: —
- Function: No separately independent first-party audit of operational claims feeding corrective organizational closure established.
- Disturbance / variety regulated: Incorrect tool results, bad code decisions or false task success could require auditing, but normal tool responses are primary operating feedback.
- Decisive decision or feedback right: No complementary auditor with distinct operational artifact access and corrective authority is wired as a supported runtime-wide path.
- Decision owner: Agent-run model and human/tool owner; the GithubReviewPullRequest class is an optional work tool, not a separate auditing authority over agent S1 results.
- Supporting / enforcement mechanisms: Tool outputs, feed status, optional GitHub PR review tool, user tool permission gate and logging.
- Closure path: Tool outputs re-enter the normal agent work loop; no separate audit findings → corrective overseer → returned task regulation channel is evidenced.
- Why this is / is not agent-owned: GitHub code-review tool invocation under the acting agent does not establish independent complementary sampling or second-party finding closure.
- Evidence: [superagi/tools/github/review_pull_request.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/tools/github/review_pull_request.py#L33-L108); [superagi/agent/agent_tool_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_tool_step_handler.py#L39-L96); [superagi/agent/agent_iteration_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/agent_iteration_step_handler.py#L93-L118).
- Basis: structural
- Confidence: medium
- Caveats: Not a general claim about any human organization's external code-review process.
### Absence scope
- Surfaces inspected: shipped agent iteration/tool/output/queue handlers, GitHub review tool, worker, execution feeds and the permission API.
- Plausible first-party paths checked: existing review-pull-request tool, model verification/action outcomes, user permission, calls/logs and callback/event surfaces.
- Why no material first-party path remains: all cited review/instrumentation mechanisms are task tools or host permissions; none shows structurally independent observation of the producing unit with a separate audit judgment returning through a corrective control relationship.

## S4 — Outside-and-then intelligence
- State: —
- Function: No first-party prospective external-intelligence adaptation loop shown to alter the deployed organization/capabilities.
- Disturbance / variety regulated: Future tasks, model/provider availability, tool capability and changed user requirements.
- Decisive decision or feedback right: Model can plan/create/prioritize immediate task items, but not documented to own future-oriented external capability adaptation.
- Decision owner: User/developer for configuration/marketplace updates; active agent for within-run task sequencing.
- Supporting / enforcement mechanisms: prompt templates, TaskQueue, knowledge handler, configurable toolkits and scheduled runs.
- Closure path: Queue/task planning feeds immediate operations, not an evaluated external future option selected and integrated into ongoing organizational capability.
- Why this is / is not agent-owned: Autonomous task decomposition and scheduled execution do not satisfy outside-and-then adaptation.
- Evidence: [superagi/agent/prompts/prioritize_tasks.txt](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/prompts/prioritize_tasks.txt); [superagi/agent/queue_step_handler.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/agent/queue_step_handler.py); [superagi/controllers/agent.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent.py#L167-L289); [superagi/models/agent.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/models/agent.py#L121-L252).
- Basis: structural
- Confidence: medium
- Caveats: Third-party installed marketplace capabilities and future hosted features are excluded.
### Absence scope
- Surfaces inspected: iteration and task queue planning, tool creation/configuration, scheduled run logic, model prompts, resource/knowledge and public API routes.
- Plausible first-party paths checked: task prioritization, scheduled automations, adapting prompt/tool configuration, marketplace templates and knowledge reuse.
- Why no material first-party path remains: supported positive paths address immediate tasks or human-authored configuration; the pinned first-party agent does not select a future external adaptation option and return it as an ongoing organizational capability change.

## S5 — Policy and identity
- State: ?
- Function: Organization accounts, security/configuration and permission decisions constrain runs, but ultimate identity/policy authority at the assessed recursion remains unresolved.
- Disturbance / variety regulated: Authorization, organizational model/key selection, budget and permission requests.
- Decisive decision or feedback right: Operator can configure organizations and answer run-scoped permission prompts; whether any first-party parent identity/policy loop closes across subsequent runs is unproven.
- Decision owner: Human operator and framework configuration rather than model, but S5-specific parent closure not reconstructed.
- Supporting / enforcement mechanisms: organization/account API, AuthJWT, budget CRUD and AgentExecutionPermission persisted status.
- Closure path: Run permission answer can resume/stop action; this is lower-level delegated authorization, not yet an ultimate-policy regulation loop.
- Why this is / is not agent-owned: Generic administrator UI and permission step do not give autonomous policy authority and do not alone warrant `P`.
- Evidence: [superagi/controllers/organisation.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/organisation.py#L48-L128); [superagi/controllers/agent_execution_permission.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/agent_execution_permission.py#L90-L157); [superagi/controllers/budget.py](https://github.com/TransformerOptimus/SuperAGI/blob/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6/superagi/controllers/budget.py#L30-L97).
- Basis: unknown
- Confidence: low
- Caveats: Determine whether a legitimate supported parent governance/identity decision can be shown returning to regulate the full deployment; cannot assume S5=P from AuthJWT or budget edits.

## Recursion
An agent execution is one model-directed S1 unit. The installed backend can run many such units; Celery/queues/framework startup do not by themselves establish S2/S3 organizational recursion. The user/deployer and provider are outside the autonomous run boundary.

## Variety and escalation
Per-task LLM/tool feedback absorbs immediate tool-site/task variety. Token ceilings, permission requests, retry scheduling and status logs constrain execution; neither an exception log nor a human permission request automatically supplies independent audit or an algedonic higher-system signal.

## Evidence gaps
Source-first frozen review of the shipped backend without live deployment/proprietary cloud. The whole-current operator/control path (S3) and organization-level ultimate identity/policy feedback loop (S5) require closer proof, so remain `?`. Negative S2/S3*/S4 judgments are explicitly bounded to reviewed distributed runtime surfaces and must be revisited if a specific shipped path contradicts them.
