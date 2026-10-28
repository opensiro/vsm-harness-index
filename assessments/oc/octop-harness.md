---
harness_id: octop-harness
project_name: Octop Harness
repository: https://github.com/TencentCloud/octop-harness
review_ref: 68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Octop Harness

## Review boundary

- System in focus: the distributed Python HarnessAgent and manager with supported optional peer teams and local operator-owned workspace.
- Purpose and identity: perform user-directed work through a persistent model/tool agent, optionally collaborating with other registered agents under owner-selected identity and behavioral rules.
- Relevant environment: user requests and workspace, provider models, local/remote tool backends, peer results, MCP tools and memory.
- Standard-distribution boundary: packaged HarnessAgent/Manager, CLI, agent graph composition, peer inbox, workspace bootstrap and memory/policy middleware.
- Credited operating / distribution surfaces: src/octop_harness/agent.py, manager.py, teams/*, middleware/*, memory/* and packaged builtin/md_files; DeepAgents is a declared runtime dependency instantiated by this product.
- Adjacent first-party surfaces excluded from ownership: tests and mocked model replies, examples, CI/release, maintainer development AGENTS.md; external Octop host/dashboard and octop-memory internals are not silently treated as in-repository owners.
- First-party operating / deployment modes considered: single agent CLI/library; manager-created peers in sync mode; optional async team mode with explicit TeamProcessor host binding; bootstrap enabled/disabled and memory manual_document_policy auto/user/agent.
- Recursion level: one persistent agent/team operating arrangement; registered peers are operational work cells, with no automatic claim of recursive VSM completeness.
- Reviewed revision: `68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

HarnessAgent resolves a model, backend, workspace, tools, middleware, subagents, skills, memory and checkpointer, then instantiates deepagents.create_deep_agent and exposes call/stream/events. Model decisions execute through the configured tool graph and return tool results. HarnessAgentManager registers agents and applies common security configuration. Peer tools synchronously call another registered agent or enqueue background work; the async inbox serializes calls per target and returned followups per source thread before resuming the source model. Workspace onboarding asks the human for agent identity and collaboration boundaries, persists a dossier and reloads the graph after completion. Manual owner documents enter subsequent session snapshots; structured memory adds recall/extraction using an external package. Filesystem guards, HITL, tool scanning, retry and observability enforce or report actions. These are materially different roles from autonomous management/audit/adaptation.

## Operational model

The S1 outcome is a completed user task and returned artifacts/answer. Provider-backed model actors choose tool use, peer requests and resulting content. The package deliberately composes their runtime, so using DeepAgents does not erase S1; equally, that dependency does not confer any unexamined DeepAgents governance. Optional peer reply locks regulate concrete shared runtime contention. User-owned identity rules govern later sessions at a local operator recursion; no organization-wide parent authority is inferred.

## S1 — Operations

- State: A
- Function: produce user task outcomes using a configured model/tool loop and returned environment feedback.
- Disturbance / variety regulated: variable requests, workspace/tool failures, unavailable providers and peer results.
- Decisive decision or feedback right: choose tool calls, edits, delegation and final answer.
- Decision owner: provider-backed graph agent assembled by first-party HarnessAgent.
- Supporting / enforcement mechanisms: DeepAgents/LangGraph execution, backend/tools, checkpointer, retries, model routing, skills and memory.
- Closure path: user message → model action/tool selection → actual backend/peer result → subsequent model reasoning/action → persisted answer/artifact.
- Why this is / is not agent-owned: the model supplies task-specific discretion; the imported graph executes it. This credits the shipped composition without attributing unrelated dependency behavior.
- Caveats: no live provider quality measurement; optional tools depend on configured services.
- Boundary reachability: public CLI/library builds and invokes the configured graph through HarnessAgent.call/stream, with registered tools/model and returned messages.
- Evidence: [src/octop_harness/agent.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/agent.py); [src/octop_harness/manager.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/manager.py); [src/octop_harness/teams/tools.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/tools.py); [pyproject.toml](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/pyproject.toml).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S2 — Coordination

- State: C
- Function: attenuate concurrent peer invocation and shared-source followup interference in optional async team operation.
- Disturbance / variety regulated: two independent peer jobs can concurrently invoke one target agent or return into the same source checkpoint/thread.
- Decisive decision or feedback right: target and source-thread admission/serialization plus ordered result return are exposed by the dedicated team inbox; autonomous negotiation/revision of that coordination policy is not supplied.
- Decision owner: developer/runtime selects fixed lock/semaphore policy; source/peer models own operational actions, not the coordination policy itself.
- Supporting / enforcement mechanisms: per-target locks and reference counts, per-source-thread locks, bounded global semaphore, cancel/status checks and TeamProcessor callback.
- Closure path: peer jobs wait for target access, then returned results wait for source-thread access → source model resumes against ordered followups → completion callback/status releases the job.
- Why this is / is not agent-owned: C credits a specific coordination feedback constructor, not autonomous discretion by an asyncio lock; an agent-owned coordination policy still needs composition.
- Caveats: async delivery requires a host TeamProcessor; synchronous generic ask_agent alone is not the S2 witness.
- Boundary reachability: HarnessAgentManager optional team_processor binding creates the inbox; packaged background ask_agent routes through it. The host must bind delivery, rather than this review borrowing a separate dashboard.
- Distinct S1 units: registered source task agent and distinct peer task agents executing delegated work with their own model/tool contexts.
- Inter-S1 disturbance: concurrent peer jobs contend for one target agent, and distinct returned work results race on the source conversation/checkpoint; native tests specifically exercise target serialization and per-thread followups.
- Attenuating coordination relation: _process serializes target invocation by target_agent_id and synthesis by source_thread_id/source_agent_id, with a concurrency envelope.
- Feedback into subsequent S1 behaviour: each completed peer result is synthesized by the source agent only after its source lock, so later source work receives the ordered feedback rather than overlapping updates.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence is the implementation/tested collision path and protected model resumption, not the existence of agent_list, messaging or delegation.
- Evidence: [src/octop_harness/teams/inbox.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/inbox.py); [src/octop_harness/teams/team_manager.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/team_manager.py); [src/octop_harness/teams/processor.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/processor.py); [tests/test_teams/test_inbox.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/tests/test_teams/test_inbox.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system discretionary current-control loop established in the reviewed distribution.
- Disturbance / variety regulated: per-turn tool/skill/member availability, provider retries, resource lifetime and concurrent jobs.
- Decisive decision or feedback right: decision middleware narrows tools/members for a request; manager creates/removes/rebuilds agents under externally supplied configuration.
- Decision owner: task model owns operational selection; developer/host supplies limits and configuration; runtime enforces them.
- Supporting / enforcement mechanisms: agent registry, shared factory, security application, cancellation, checkpointer and concurrency limits.
- Closure path: request-specific routing or configured rebuild changes execution, without a whole-system operational-resource bargain and accountable current-control return.
- Why this is / is not agent-owned: a manager API and ranking candidate tools do not supply whole-system discretion over commitments/resources.
- Caveats: a separate host may implement such control; its decision loop is not in this assessed package.
- Evidence: [src/octop_harness/manager.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/manager.py); [src/octop_harness/middleware/decision.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/middleware/decision.py); [src/octop_harness/teams/inbox.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/inbox.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Manager lifecycle/registry/security, decision middleware and team concurrency/cancellation.
- Plausible first-party paths checked: all-agent rebuild, per-turn member/tool selection, queue limits, host callback and user approval.
- Why no material first-party path remains: these are lifecycle/operation or externally configured enforcement paths; no shipped whole-system current view coupled to discretionary commitment/resource revision and returned control is established.

## S3* — Complementary audit

- State: —
- Function: no distinct complementary audit function over operational claims supplied.
- Disturbance / variety regulated: risky tools, secrets, context overflow, malformed results and model errors.
- Decisive decision or feedback right: guards scan/intercept tool actions; routine retries/observability report execution. No separate auditor owns a claim-challenging verdict and corrective return.
- Decision owner: developer-selected guard rules and ordinary acting model, not an independent audit actor.
- Supporting / enforcement mechanisms: tool guard, PII/filesystem controls, skill scanning, logging/tracing and generic peer tools.
- Closure path: guard blocks/warns/requests approval before action; ordinary result/error returns to acting model.
- Why this is / is not agent-owned: pre-execution safety checks and optional arbitrary peer prompts are not complementary access to operational reality beyond ordinary reporting.
- Caveats: a user can compose a reviewer with peers/tools, but no audit-specific mode/ownership/return is provided by generic extensibility.
- Evidence: [src/octop_harness/middleware/tool_guard.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/middleware/tool_guard.py); [src/octop_harness/security/models.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/security/models.py); [src/octop_harness/teams/tools.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/teams/tools.py); [src/octop_harness/observability/langfuse.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/observability/langfuse.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Tool guard/security/PII, retry, tracing, subagent loading, peer tools and memory feedback.
- Plausible first-party paths checked: tool-risk approval, skill scanning, generic review via ask_agent, logs and backend result inspection.
- Why no material first-party path remains: the supported paths enforce or report ordinary execution; no first-party audit-specific actor, complementary evidence access and corrective judgment loop remains.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop into current harness capability.
- Disturbance / variety regulated: new user facts/preferences, task failures, provider availability and context limits.
- Decisive decision or feedback right: memory captures/recalls conversation; routing chooses available model/tools/skills for the present request.
- Decision owner: task agents and configured memory service own local content; host/developer owns product configuration/evolution.
- Supporting / enforcement mechanisms: memory service/extraction, model routing, recall, compaction, skill/subagent/plugin loading and web tools.
- Closure path: past interaction enters future task context, but no outside/future model produces adaptation options and a capability-change decision returned to current regulation.
- Why this is / is not agent-owned: retention, extensibility and web research as S1 do not alone establish S4.
- Caveats: external octop-memory internals and prospective host development are outside the source boundary.
- Evidence: [src/octop_harness/memory/runtime.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/memory/runtime.py); [src/octop_harness/middleware/memory.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/middleware/memory.py); [src/octop_harness/middleware/model_router.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/middleware/model_router.py); [src/octop_harness/plugins/loader.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/plugins/loader.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Memory wiring/extraction/recall, model router, plugins/subagents, builtin skills and bootstrap.
- Plausible first-party paths checked: remembered preferences, new skills/plugins, model choice, proactive followups and web inquiry.
- Why no material first-party path remains: these change local task context or load developer/user-selected capability; none closes an external-and-prospective adaptation judgment into harness present capability.

## S5 — Policy and identity

- State: P
- Function: maintain the local agent identity and ultimate collaboration/behavioral mandate through an owner-selected durable dossier.
- Disturbance / variety regulated: a fresh workspace lacks an agreed agent form/name and hard behavioral boundaries; stored/recalled facts can conflict with owner instructions.
- Decisive decision or feedback right: local user decides what the agent is and the boundaries of its relationship; explicit owner changes to strong documents govern later sessions.
- Decision owner: legitimate local workspace operator/user; agent conducts onboarding and records the returned choice.
- Supporting / enforcement mechanisms: packaged BOOTSTRAP/USER templates, manual-document policy, bootstrap marker/reload, full owner-document session snapshot and precedence over recalled memory.
- Closure path: identity/behavior questions → user-selected name/form/hard lines → confirmed dossier/owner edits → bootstrap graph reload or next-session loading → later operations use the selected mandate.
- Why this is / is not agent-owned: P credits a specific owner-to-identity-to-subsequent-operation path; static security defaults and individual tool approvals are not its witness. No autonomous ultimate-policy actor is established.
- Caveats: scope is the personal agent/operator relationship. Editable-document mode (structured memory off or manual_document_policy=agent) permits the agent to record an explicit owner choice; locked-document modes require the owner to supply dossier edits. A final reply alone can set the bootstrap marker, so that marker is not evidence the dossier was saved. Broader institution authority and external dashboard editing UI are not credited; generic style changes alone are not a separate S5 witness.
- Boundary reachability: bootstrap middleware and packaged templates are supported workspace paths; completion triggers graph reload, while USER.md/MEMORY.md are explicitly included in graph memory paths and loaded for new sessions even with structured memory disabled.
- Identity / ultimate-policy issue: what form/purpose the local agent adopts and the hard privacy/outward-action/behavioral boundaries its operator chooses for collaboration.
- Ultimate authority in each claimed mode: the local user chooses and maintains the authoritative dossier; agent-editable document mode still requires an explicit user request for profile/strong-memory changes.
- Return-to-operation path: bootstrap completion calls reload; graph compilation includes strong documents, and memory policy makes user documents authoritative over conflicting recalled material. Session snapshots mean later edits apply to new sessions, not retroactively to the current one.
- Evidence: [src/octop_harness/builtin/md_files/en/BOOTSTRAP.md](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/builtin/md_files/en/BOOTSTRAP.md); [src/octop_harness/builtin/md_files/en/USER.md](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/builtin/md_files/en/USER.md); [src/octop_harness/middleware/bootstrap.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/middleware/bootstrap.py); [src/octop_harness/memory/policy.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/memory/policy.py); [src/octop_harness/agent.py](https://github.com/TencentCloud/octop-harness/blob/68b5423bb80ecef7fca57ba5a37d9a2bdcbf12d2/src/octop_harness/agent.py).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## Distributed OSS parent arrangement

Local dossier authority is not maintainer/project governance. Independent OSS contributors and external host operators do not establish one organization-wide parent. The P state is limited to the declared local user-agent identity loop.

## Self-hosted and non-human modes

Library/CLI and optional async team bindings are assessed. A host can supply delivery or stronger governance, but those extra actors must be composed and are not automatically credited. Memory auto/user/agent policies alter document write permissions without transferring ultimate mandate away from the local user.

## Recursion

Registered peers have task environments and model actions. Neither subagents nor the manager registry proves full recursive viability; this review makes no such claim.

## Variety and escalation

Backend/tool errors, provider retries, bounded context/recall, PII/file guards and ordered peer returns handle operational variety. HITL or ask_user routes ordinary decisions to the user without automatically becoming S3/S5. Pending bootstrap and new-session snapshots bound identity changes.

## Evidence gaps

Source inspection only; no live LLM/provider, Browser or host runtime run. Native pytest was unavailable in the interpreter and dependency-heavy DeepAgents/LangChain runtime tests were not executed; targeted inbox tests were read as corroboration, not reported PASS. The S2 C mode explicitly requires host delivery composition; S5 P is structural local identity closure, with model obedience/quality unmeasured. External octop-memory/DeepAgents implementations were not independently assessed.
