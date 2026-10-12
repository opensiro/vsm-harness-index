---
harness_id: agentscope-2-0
project_name: AgentScope 2.0
repository: https://github.com/agentscope-ai/agentscope
review_ref: 5ff52f877de12d66a30d55af279dd4f42b1590f3
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# AgentScope 2.0

## Review boundary
- System in focus: installed first-party AgentScope 2.0 Python ReAct Agent SDK plus the shipped optional Agent Service's team leader/worker model, toolkit, message bus, session storage and goals pipeline.
- Purpose and identity: build and run model-driven tool agents, optionally configured as a team where a leader delegates to and receives feedback from independently executing workers.
- Relevant environment: user requests, external model APIs, workspace/tool effects, persistent sessions, permission/HITL, other team agents and external channels.
- Standard-distribution boundary: `agentscope` Python package `src/agentscope/` plus shipped Agent Service and `examples/agent_service/` host entrypoint; no authority borrowed from external MCP servers, model providers, user-defined custom graphs or unrelated apps ([README.md](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/README.md#L122-L235); [src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py)).
- Credited operating / distribution surfaces: [src/agentscope/agent/_agent.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/agent/_agent.py); [src/agentscope/app/_tool/_team_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_create.py); [src/agentscope/app/_tool/_agent_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_agent_create.py); [src/agentscope/app/_tool/_team_say.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_say.py); [src/agentscope/app/_service/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_toolkit.py); [src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py); [src/agentscope/app/middleware/_team_member_middleware.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/middleware/_team_member_middleware.py); [src/agentscope/pipeline/_goal_pipeline.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/pipeline/_goal_pipeline.py).
- Adjacent first-party surfaces excluded from ownership: provider-internal LLM behavior and external tool servers, demo-only customized agent scripts, CI/tests, unconfigured optional plugins or non-installed user SOPs.
- First-party operating / deployment modes considered: simple ReAct agent; packaged multi-session Agent Service with team leader/worker tools; goal executor/verifier pipeline; optional user permissions, scheduled tasks, middleware and memory.
- Recursion level: model-driven leader and the worker agents of a single AgentScope service team. Not every tenant/organization sharing the Agent Service or the AgentScope maintainers.
- Reviewed revision: `5ff52f877de12d66a30d55af279dd4f42b1590f3`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The first-party `Agent` implements an asynchronous ReAct model/tool loop with policy middleware and stateful sessions. Packaged Agent Service assembles the toolkit dynamically, exposing model-driven `TeamCreate`, `AgentCreate`, `AgentInvite`, `TeamSay` and related actions. A leader can create a team, spawn a worker with a model-configured profile/initial task, receive results through team messages and send follow-up tasks. Team-member middleware requires worker completion to end with a successful report to the actual leader, retries nudges, and terminates after a bounded retry budget instead of silently treating an unreported result as success. [src/agentscope/agent/_agent.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/agent/_agent.py#L117-L198); [src/agentscope/app/_tool/_team_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_create.py#L30-L146); [src/agentscope/app/_tool/_agent_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_agent_create.py#L145-L174); [src/agentscope/app/_tool/_team_say.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_say.py#L35-L140); [src/agentscope/app/middleware/_team_member_middleware.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/middleware/_team_member_middleware.py#L113-L175).
A separate `GoalPipeline` takes an executor's goal/report and invokes a verifier agent, returning pass/fail feedback to the executor. That source does not prove independent material inspection beyond the supplied result, so its mere two-model topology is not credited as S3*. [src/agentscope/pipeline/_goal_pipeline.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/pipeline/_goal_pipeline.py#L91-L285). The service message bus serializes individual session runs, but this is not by itself attenuation of interference among distinct operating units ([src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py#L130-L145)).

## Operational model
At a single-agent boundary, model proposals choose tools with observed feedback. In Agent Service team mode, the model leader owns which workers and tasks to instantiate and when to send clarifications or follow-ups, while the first-party service ensures messages reach the correct session and completion reports come back. The hosting/storage implementation is a delivery mechanism, not automatically a separate S2 or S3 decision owner. The evaluator/verifier and long-term memory are tested for function-specific closure independently.

## S1 — Operations
- State: A
- Function: Configurable first-party model-directed reasoning/acting tool loop performs user/worker tasks and returns tool/environment feedback.
- Disturbance / variety regulated: Unknown task conditions, tool execution responses/errors, context limits and external model results.
- Decisive decision or feedback right: Choose goal-specific tool calls, perform actions, interpret outcomes and continue or finish.
- Decision owner: AgentScope-configured agent model in the SDK/Service's direct agent execution mode.
- Supporting / enforcement mechanisms: Model adapters, Toolkit, middleware hooks, workspace/sandbox, permission gates, message/session store.
- Closure path: User or leader prompt → agent reasoning → selected tool action → tool/environment result → model continuation and final worker report.
- Boundary reachability: The published SDK and example Agent Service initialize real AgentScope Agent instances with toolkit/model and feed messages into `reply_stream` ([README.md](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/README.md#L122-L174); [src/agentscope/agent/_agent.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/agent/_agent.py#L288-L380); [src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py)).
- Why this is / is not agent-owned: The model selects substantive task acts; host/session middleware only applies technical limits and transport policy.
- Evidence: [src/agentscope/agent/_agent.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/agent/_agent.py); [src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py); [src/agentscope/tool/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/tool/_toolkit.py).
- Basis: structural
- Confidence: high
- Caveats: Static first-party source, no online model/benchmark execution.

## S2 — Coordination
- State: ?
- Function: Candidate team message routing and session locking, but no proven function-specific first-party inter-S1 interference attenuation with returned feedback.
- Distinct S1 units: Separately instantiated model-driven members of a first-party TeamRecord, each with its own session/task and message bus.
- Inter-S1 disturbance: Potential conflicting simultaneous operations against shared task resources or overlapping workspace targets; the service's mere presence of separate sessions does not establish the specific disturbance regulation.
- Attenuating coordination relation: The observed session lock serializes calls *within one session*; TeamSay routes messages and avoids misdelivery, but a function-specific inter-member contention/coordination policy has not been demonstrated.
- Feedback into subsequent S1 behaviour: Team messages and leader reassignments exist; their connection to mitigation of a particular verified inter-worker conflict remains unproven.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: No positive S2 attribution is made from generic team topology, messaging, per-session locks or leader assignment alone.
- Disturbance / variety regulated: Candidate inter-member resource contention, not established as an implemented control target.
- Decisive decision or feedback right: Unresolved for interference-specific arbitration among independent worker sessions.
- Decision owner: Potential leader or host service, not yet reconstructable for a material S2 relation.
- Supporting / enforcement mechanisms: MessageBus, TeamSay, session_run lock, team membership constraints, toolkit role filtering.
- Why this is / is not agent-owned: No positive S2 owner is credited; the leader sends messages and the service serializes individual session turns, but neither path is proven to own inter-worker interference-specific decisions.
- Closure path: Inter-agent messages are delivered; no defensible concrete collision → arbitration → modified workers path established.
- Evidence: [src/agentscope/app/_tool/_team_say.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_say.py); [src/agentscope/app/_service/_chat.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_chat.py#L130-L145); [src/agentscope/app/_tool/_team_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_create.py); [src/agentscope/app/_service/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_toolkit.py).
- Basis: unknown
- Confidence: low
- Caveats: Inspect first-party SOP/workspace shared-resource coordination and actual collision tests before resolving `?` to a positive state or bounded `—`.

## S3 — Inside-and-now control
- State: A
- Function: Model-led team leader makes current team staffing, delegation, repair and follow-up decisions based on worker reports.
- Disturbance / variety regulated: Pending delegated tasks, changed worker outcomes, failures, information gaps and incomplete task progress.
- Decisive decision or feedback right: Create a team, select role/worker, assign task, request clarifications and continue work after returned findings.
- Decision owner: First-party hosted model leader using TeamCreate/AgentCreate/TeamSay, not a deterministic background task dispatcher.
- Supporting / enforcement mechanisms: TeamRecord, role-separated team tools, agent/worker session allocation, message bus, report-enforcing middleware.
- Whole-system current view: Leader receives team roster and completion/failure reports of the team it created; no claim of full multi-tenant service-wide control.
- Current-control decision scope: Assign current work, change team tasks, re-instruct workers and integrate returned work in the bounded team recursion.
- Closure path: Worker performs task and sends mandatory TeamSay report → leader model receives result → chooses follow-up or new task → worker session/action changes.
- Boundary reachability: The Agent Service toolkit grants leader-specific team tools in configured leader mode; worker reports are actively enforced by middleware and persisted/routed back to the leader ([src/agentscope/app/_service/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_toolkit.py#L55-L100); [src/agentscope/app/_tool/_agent_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_agent_create.py#L145-L174); [src/agentscope/app/middleware/_team_member_middleware.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/middleware/_team_member_middleware.py#L113-L175)).
- Why this is / is not agent-owned: The actual choices of child role, scope and continuation are model-generated via shipped team tools; technical message delivery and individual session run locks are merely enforcement.
- Evidence: [src/agentscope/app/_tool/_team_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_create.py#L30-L146); [src/agentscope/app/_tool/_agent_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_agent_create.py); [src/agentscope/app/_tool/_team_say.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_team_say.py); [src/agentscope/app/middleware/_team_member_middleware.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/middleware/_team_member_middleware.py).
- Basis: structural
- Confidence: medium
- Caveats: Limited to configured Agent Service leader/team mode; neither a whole-deployment portfolio S3 nor distinct human parent S3 is implied.

## S3* — Complementary audit
- State: ?
- Function: GoalPipeline provides separate executor/verifier agents and revision feedback, but complete independent operational-artifact challenge path is not established.
- Disturbance / variety regulated: False executor goal-completion statements, missing required deliverables.
- Decisive decision or feedback right: Verifier returns pass/fail about executor goal and an explanation, which may prompt another executor iteration.
- Decision owner: Separately configured verifier Agent, subject to its actual tools/evidence access.
- Supporting / enforcement mechanisms: GoalPipeline executor/verifier alternation, structured execution report, structured verification result.
- Claim being audited: Executor's report that it fulfilled the original goal.
- Ordinary reporting path: Executor returns a structured report under _ExecutionReport.
- Complementary access path: The verifier receives original goal plus executor's text report; supported independently sampled source/tool artifact inspection is not guaranteed by this pipeline contract.
- Independence boundary: Distinct Agent object is possible, but materially independent observation from primary operational artifacts is unresolved.
- Who acts on findings: Pipeline sends failure feedback back to executor, conditional on the verifier's structured judgment.
- Closure path: Report → verifier model check → pass/fail → continue or return; missing independent observational basis prevents positive state.
- Why this is / is not agent-owned: An independent model call is necessary but not sufficient when its only guaranteed input is the producer's own claim.
- Evidence: [src/agentscope/pipeline/_goal_pipeline.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/pipeline/_goal_pipeline.py#L91-L286); [src/agentscope/app/middleware/_team_member_middleware.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/middleware/_team_member_middleware.py).
- Basis: unknown
- Confidence: low
- Caveats: Inspect verifier tool configuration and direct code/environment access of packaged modes before S3* credit or bounded absence.

## S4 — Outside-and-then intelligence
- State: ?
- Function: Persistent memory, scheduling and middleware extension may support reuse across future tasks but do not yet establish an outside-and-then capability adaptation decision.
- Disturbance / variety regulated: New task conditions, changing knowledge and external user contexts.
- Decisive decision or feedback right: No confirmed owner/loop deciding a prospective adaptation option to future team capability.
- Decision owner: Unresolved between user, configured agent, memory backend and developer.
- Supporting / enforcement mechanisms: Long-term memory middleware, scheduler manager and goal/planning toolkit.
- External distinction: External observations may be retained in memory, but this alone is not systemic intelligence.
- Future / prospective distinction: Reuse is future-facing in time but not necessarily prospective organizational adaptation.
- Adaptation option generated: Not established from the read-only source evidence.
- Path back into current capability / S3: Memory/context or schedule modifications can affect future runs; full future intelligence → change is unproven.
- Closure path: Captured memory → later prompt is technically supported, but no established S4 choice/feedback.
- Why this is / is not agent-owned: Memory retention and schedules are mechanisms, not proof of autonomous or parent S4.
- Evidence: [src/agentscope/middleware/_longterm_memory](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/middleware/_longterm_memory/__init__.py); [src/agentscope/app/_manager/_scheduler/_scheduler_manager.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_manager/_scheduler/_scheduler_manager.py); [src/agentscope/tool/_task/_update_task.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/tool/_task/_update_task.py).
- Basis: unknown
- Confidence: low
- Caveats: Full packaged learning/longterm-memory and capability-changing paths need separate scrutiny; retain `?`.

## S5 — Policy and identity
- State: ?
- Function: Team identities, access/permission rules and human confirmations exist without established ultimate-policy identity decision/return loop at the bounded team recursion.
- Disturbance / variety regulated: Permissions over tools, resource access, multi-tenant rights and delegation.
- Decisive decision or feedback right: The human/application owner sets permission rules and may approve actions, but ultimate organizational identity/policy closure is unresolved.
- Decision owner: User/app role policies; not automatically a first-party agent policy controller or a qualified parent S5.
- Supporting / enforcement mechanisms: PermissionEngine, TeamRecord roles, workspace permissions and HITL middleware.
- Identity / ultimate-policy issue: Allowed identity, roles and acceptable operating permissions of configured team members.
- Ultimate authority in each claimed mode: No S5-specific autonomous/parent owner established; execution-level rules are narrower than ultimate policy.
- Return-to-operation path: Permission decisions guard specific tool calls and inheritance to child agents, not a proven changing-policy feedback loop.
- Closure path: Permission request/policy → allow/deny action, lacking ultimate identity-level decision.
- Why this is / is not agent-owned: A policy engine enforces rules but does not decide the system's ultimate purpose or identity.
- Evidence: [src/agentscope/permission/_engine.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/permission/_engine.py); [src/agentscope/app/_tool/_agent_create.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_tool/_agent_create.py#L60-L113); [src/agentscope/app/_service/_toolkit.py](https://github.com/agentscope-ai/agentscope/blob/5ff52f877de12d66a30d55af279dd4f42b1590f3/src/agentscope/app/_service/_toolkit.py).
- Basis: unknown
- Confidence: low
- Caveats: Check the actual authority of organization/group policies and complete return path before changing `?`.

## Recursion
A normal AgentScope SDK agent is an S1 operating unit. The installed Agent Service can assemble multiple separately executing workers and a model-directed leader; S3 is attributed only to that task team. No inter-S1 S2 or independent-audit S3* is inferred from module plurality, and platform-wide application owners remain a separate higher recursion.

## Variety and escalation
Agent ReAct tool feedback regulates dynamic operational tasks. TeamSay reports and leader follow-ups regulate present team commitments; backend lock and middleware protect individual run/message integrity. Verifier retry, memory reuse, approval and administrative roles are not automatically S3*, S4 or S5.

## Evidence gaps
Static frozen-source assessment, no live model evaluation. Positive claims limited to shipped SDK and Agent Service model/team modes; provider-native internals and custom user solutions excluded. Shared-resource S2 interference mitigation, verifier independent operational evidence (S3*), external-prospective S4 adaptation and ultimate-policy S5 remain unresolved with specific plausible first-party paths to inspect. No universal negative function claim is made.
