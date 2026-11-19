---
harness_id: mybot
project_name: MyBot
repository: https://github.com/yexi-by/MyBot
review_ref: 9449bed56bb9ae34ec0646111046a2d69001f6ab
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MyBot

## Review boundary

- System in focus: The deployed QQ Agent Harness service shipped in MyBot, including its operator WebUI and supported optional background subagents.
- Purpose and identity: Handle authorized QQ conversations and delegated workspace/media/research tasks through a tool-using model runtime.
- Relevant environment: QQ groups/private chats through NapCat, model providers, shared workspace, MCP services, operator configuration and live workload.
- Standard-distribution boundary: First-party service/runtime/WebUI, scoped conversation policies, tool registry, subagent manager and workspace service. External QQ/NapCat, model APIs, MCP servers and user-authored skills are dependencies.
- Credited operating / distribution surfaces: Application lifecycle wires AgentRuntime, workspace service, TimerManager and SubagentManager; model session/tool loop, global runtime snapshots, operator steering/cancellation and resource settings.
- Adjacent first-party surfaces excluded from ownership: Tests, verification notes, WebUI development/build tooling and repository maintenance. Those demonstrate interfaces without supplying operational agent ownership.
- First-party operating / deployment modes considered: Local/container service with WebUI; group/private sessions, optional workspace/skills/MCP/timers and scoped background subagents. Operator console is included in the deployed boundary.
- Recursion level: One deployed harness instance; nested execution is not presumed recursively viable.
- Reviewed revision: 9449bed56bb9ae34ec0646111046a2d69001f6ab
- Observation date: 2026-11-19
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

A configured NapCat connection feeds scoped messages to workers. Each conversation retains a provider-neutral ModelSession; the model selects authorized tools, results return to context, and explicit QQ send tools perform outward communication. Optional subagents run separate contexts with restricted tools, progress notices and return/wakeup into the parent. Context and subagent retention are memory-bounded. The operator console exposes all current sessions/turns, capacity, workspace activity and subagents; it can steer/cancel work and change effective configuration. Some concurrency/topology settings explicitly require restart; dynamic retention/policy settings are consulted during later execution.

## Operational model

Conversation agents and optional background task agents produce real chat/workspace/media outcomes. At the whole-service recursion, individual model actors have scoped views; the operator console provides whole-current visibility and intervention. Generic queues, resource semaphores, role restrictions and parent-child messages are not credited as inter-S1 conflict coordination without a specific witness.

## S1 — Operations

- State: A
- Function: Resolve conversation/task requests with discretionary model-selected actions.
- Disturbance / variety regulated: Changing chat context, tool errors, media and workspace tasks.
- Decisive decision or feedback right: Select tool calls, revise action choices from results and decide explicit message delivery/completion.
- Decision owner: Configured conversation or background-subagent model actor.
- Supporting / enforcement mechanisms: ModelSession, authorization registry, NapCat/MCP/workspace transports, context retention and cancellation.
- Closure path: AgentRuntime._turn calls session.step, executes authorized calls, appends results and repeats; subagent results can wake the parent.
- Why this is / is not agent-owned: The model selects meaningful task actions; transports/permission checks do not generate solutions without it.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/providers.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/providers.py); [qq_agent_harness/registry.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/registry.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Boundary reachability: web application lifecycle creates and wires the runtime/subagent managers; received authorized messages and enabled subagent tools enter their packaged loops.

## S2 — Coordination

- State: —
- Function: No established inter-S1 disturbance-specific coordination loop.
- Disturbance / variety regulated: Potential incompatible actions by concurrent conversations/children.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Scoped sessions, subagent send restrictions, parent mailboxes and global/conversation/workspace semaphores.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Delegation, fixed role restrictions and capacity queues do not themselves show mutual adjustment over a concrete inter-unit conflict. The documented workspace remains shared rather than file-isolated.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py); [qq_agent_harness/workspace/executor.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/workspace/executor.py); [docs/workspace.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/docs/workspace.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py); [qq_agent_harness/workspace/executor.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/workspace/executor.py); [docs/workspace.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/docs/workspace.md); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Conversation serialization, subagent tool restrictions/steering and workspace bounded queues/cleanup guards.
- Why no material first-party path remains: Inspected mechanisms provide generic scope/capacity/lifecycle control; no shipped function-specific coordination decision/feedback relation over conflicting S1 commitments or artifacts is established.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the whole service current workload, active commitments and shared operating capacity through the operator.
- Disturbance / variety regulated: Simultaneous sessions/subagents, retained-context pressure, blocked workspace capacity and ongoing work needing intervention.
- Decisive decision or feedback right: Inspect the current fleet and capacity; choose which work to stop/redirect and adjust shared retention/resource constraints.
- Decision owner: The deployed service human operator through the first-party console/API; individual conversation agents do not own a whole-service view.
- Supporting / enforcement mechanisms: runtime.snapshot, combined /api/runtime with subagents/timers, workspace status, configuration store/reload, cancel/send routes and retention enforcement.
- Closure path: Operator cancellation/steering reaches active task/subagent state; later model requests consume changed steering/policy, and runtime retention enforces updated max sessions/bytes. Startup-only concurrency/root changes are reported as requiring restart rather than credited as immediate effects.
- Why this is / is not agent-owned: The operator makes the discretionary whole-current intervention; snapshots, cancellation events and limits enforce/transport the decision. Removing the operator leaves preset bounds, not the selected fleet intervention.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/configuration.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/configuration.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py); [qq_agent_harness/workspace/executor.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/workspace/executor.py); [docs/workspace.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/docs/workspace.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Whole-system current view: Combined runtime status lists all retained sessions/current turns, capacity and rejected-message counts, timers/subagents, plus workspace active/queued operations and disk budget.
- Current-control decision scope: Whole-service workload intervention and shared memory/workspace operating constraints; no autonomous policy bargaining is credited.
- Boundary reachability: The shipped WebUI calls live status, config, subagent send/cancel and runtime cancel endpoints wired to the same running managers; this is part of the deployed service.

## S3* — Complementary audit

- State: —
- Function: No supplied complementary audit owner/return loop.
- Disturbance / variety regulated: An operational report may not match raw work reality.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Session projection, events, operator inspection and general-purpose exploratory subagents.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: The console exposes ordinary retained records; a generic child can inspect source but no audit-specific independent evidence/judgment/corrective-control arrangement is shipped.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/session_view.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/session_view.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py); [docs/verification.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/docs/verification.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/session_view.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/session_view.py); [qq_agent_harness/subagent.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/subagent.py); [docs/verification.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/docs/verification.md); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: session_view projection, subagent prompt/tools/return and console inspect endpoints.
- Why no material first-party path remains: Observability and general delegation require user-composed audit semantics; repository tests/verification reports are outside the runtime ownership boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation loop.
- Disturbance / variety regulated: Future external needs or provider/tool capability change.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: On-demand skill loading, provider/model changes, knowledge files, timers and context compaction.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: These are task context/configuration or scheduled operations; no environmental foresight develops and returns a reusable capability option.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/skills.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/skills.py); [qq_agent_harness/providers.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/providers.py); [qq_agent_harness/timers.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/timers.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/skills.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/skills.py); [qq_agent_harness/providers.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/providers.py); [qq_agent_harness/timers.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/timers.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Skill scanning/loading, provider switching, timer wakes and idle/turn compaction.
- Why no material first-party path remains: The supported modes do not connect external future distinctions to a harness adaptation decision and return; user-authored new skills cannot donate a built-in S4 actor.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy escalation and returned decision loop.
- Disturbance / variety regulated: Identity or ultimate-policy disputes.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Persona text, conversation permissions, operator configuration and authorization checks.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Operator control over settings constrains behavior but does not itself supply an identity-level issue/decision/return protocol.
- Evidence: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/prompts.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/prompts.py); [qq_agent_harness/settings.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/settings.py); [qq_agent_harness/registry.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/registry.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/README.md); [qq_agent_harness/web.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/web.py); [qq_agent_harness/runtime.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/runtime.py); [qq_agent_harness/prompts.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/prompts.py); [qq_agent_harness/settings.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/settings.py); [qq_agent_harness/registry.py](https://github.com/yexi-by/MyBot/blob/9449bed56bb9ae34ec0646111046a2d69001f6ab/qq_agent_harness/registry.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Persona composition, policy configuration/live revocation and operator save workflow.
- Why no material first-party path remains: The runtime rechecks permissions and prompts; it exposes no established identity-policy matter routed to legitimate ultimate authority and returned as a policy decision.

## Distributed OSS parent arrangement

Repository maintenance and contributor approvals are outside the deployed product recursion. Multiple contributors do not establish organization-level parent governance in the assessed harness.

## Self-hosted and non-human modes

The local service operator is the legitimate parent for current whole-service workload/capacity regulation, supporting S3=P. Operator authentication is configurable; the assessment establishes decision topology, not deployment access-security quality. Static persona/provider/permission edits do not establish S4 or S5.

## Recursion

No claim of recursively complete VSM units is made. Execution phases, provider instances and nested calls do not establish recursive viability.

## Variety and escalation

Tool failures, unknown send outcomes, queue pressure, stalled children and context limits remain visible to local agents/operators. Unknown sends are not automatically replayed. Subagent notices reach the parent conversation; global workload signals reach the operator console. No algedonic or ultimate-policy loop is inferred from status fields.

## Evidence gaps

Source analysis only; no live QQ/NapCat, model, workspace process or browser integration was run. S3 parent evidence is limited to the documented live operator surface and returned steering/capacity/intervention, not autonomous fleet control. Concurrent workspace use is explicitly shared, not isolated.
