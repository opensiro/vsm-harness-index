---
harness_id: agenticx
project_name: AgenticX
repository: https://github.com/DemonDamon/AgenticX
review_ref: 582c9d00bfb23efe6f7e588c3a5edfce570729bf
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: —
---

# AgenticX

## Review boundary

- System in focus: the supported local AgenticX Python Agent/Studio runtime with its Meta-Agent-owned subagent team and optional session-learning capability; Near Desktop is one first-party route to the same local runtime.
- Purpose and identity: help an operator carry out open-ended tasks through model-selected tools and delegated agents, supervise a current session team and optionally turn environmental/tool experience into reusable future skills.
- Relevant environment: changing user work, external LLM/provider services, tools/MCP endpoints, CPU/memory pressure, provider failures, observed tool results, and operator approval.
- Standard-distribution boundary: installed Python package, local `agx serve`/Studio sessions, embedded ReAct and `AgentRuntime`, `AgentTeamManager`, registered session hooks, learning config and skill queue. Configured external provider cognition is integrated, not authored in the repo.
- Credited operating / distribution surfaces: `agenticx/runtime/agent_runtime.py`, `runtime/team_manager.py`, `runtime/meta_tools.py`, `studio/server.py`, `learning/session_review_hook.py`, `cli/agent_tools.py`, `skills/pending_queue.py`, Near local `agx serve` integration.
- Adjacent first-party surfaces excluded from ownership: Enterprise Go compliance/model-relay Gateway (not a Python runtime), Edge/Cluster planned modes, `plans/` design documents, benchmarks/tests, SDK-only collaboration templates without Studio wiring, maintainer/release governance and external skill marketplaces.
- First-party operating / deployment modes considered: Python SDK ReAct, Studio Meta-Agent with subagents, Near local desktop, group Team mode, user/operator tool-approval, local sessions, opt-in post-session model-backed skill review and approval-versus-direct-write learning modes. Enterprise current gateway is separately noted, not blended into the Studio hierarchy.
- Recursion level: one local Studio session team, with root Meta-Agent as current supervisor and spawned agents as S1; long-lived user configuration can influence future Studio sessions via the same local skills directory.
- Reviewed revision: `582c9d00bfb23efe6f7e588c3a5edfce570729bf`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgenticX is a Python framework and Studio runtime, with a Near Electron client that normally starts local `agx serve`. The installed ReAct/AgentRuntime path supplies an iterative model/tool loop through configured provider adapters; the Meta-Agent can use session-facing tools to spawn, query, message, retry and cancel subagents. `AgentTeamManager` maintains actual subagent status, bounded depth/concurrency, context and tool permissions; `ResourceMonitor` checks current machine pressure before admission. Group Team mode also composes a model-backed planner/coordinator and workers, with a project-scoped TaskLock event/action queue. An optional registered session-end learning hook observes real tool calls, invokes a background reviewer model on complex sessions and proposes or writes reusable skills. The normal config queues agent-authored writes for Desktop-user approval; a separate explicitly configured direct-write mode exists. Independent Enterprise Gateway controls auth/policy/quota/model relay, but it is not the Python agent execution path.

Primary sources: [runtime/team manager](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/team_manager.py), [Studio runtime integration](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/studio/server.py), [learning hook](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/learning/session_review_hook.py), [architecture and deployment distinctions](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/README.md).

## Operational model

The root and child LLM agents own substantive next-step and intervention decisions; Python code transports and constrains those decisions. Status/resource observation returns to a running root agent through explicit tools, so team-control ownership can be credited separately from its member operations. Normal group delegation, planning and TaskLock event queues do not by themselves prove regulation of a particular inter-S1 collision. Session-end learning changes the skill library available to later agent sessions, but its default proposal-approval mode and explicitly optional direct-write configuration are distinct. Enterprise permissions and audit traces are not imported across deployment boundaries.

## S1 — Operations

- State: A
- Function: perform open-ended user tasks by choosing tools, using execution results, and modifying task artifacts through root/child provider-backed agent sessions.
- Disturbance / variety regulated: new task details, tool errors, repository content, provider responses and subtask outcomes.
- Decisive decision or feedback right: choose next model tool call, interpret feedback and continue/revise an execution plan.
- Decision owner: configured model-backed `AgentRuntime`/ReAct root and spawned agents; neither the SDK `Agent` data model nor the event queue owns model reasoning.
- Supporting / enforcement mechanisms: provider resolver, agent/tool loop, Studio session persistence, subagent context/tool permissions and callbacks.
- Closure path: model chooses a tool, runtime executes it, the result enters the same agent's context, and later decisions change task output.
- Boundary reachability: this path is shipped both through the `agx`/Studio local backend and embedded SDK; Near's default app starts this local runtime.
- Why this is / is not agent-owned: the agent model makes contextual tool/continuation decisions; host code supplies guardrails and transport.
- Evidence: [AgentRuntime](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/agent_runtime.py), [ReActAgent](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/agents/react_agent.py), [Studio server Meta-Agent setup](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/studio/server.py#L3980-L4070).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: successful live provider/model execution and claimed production quality were not measured.

## S2 — Coordination

- State: —
- Function: no evidence-backed distinct relation that autonomously attenuates an identified interference among simultaneously acting S1 units, beyond task partition and bounded queueing.
- Disturbance / variety regulated: potential overlap of parallel workers, resource contention and conflicting changes would require interference-specific handling.
- Decisive decision or feedback right: no first-party agent-owned cross-worker conflict detection, reconciliation or isolation decision shown as an operationally closed coordination loop for the declared Studio team.
- Decision owner: none established at S2; the model planner assigns tasks and host TaskLock transports actions.
- Supporting / enforcement mechanisms: Team task decomposition, worker assignments/dependencies, TaskLock action queue, group routing and shared context.
- Closure path: delegations can complete and summaries return, but that is ordinary task routing; no distinct detected inter-S1 collision and corrective relation is evidenced.
- Why this is / is not agent-owned: naming a CoordinatorAgent or serializing actions does not establish function-specific S2 conflict attenuation.
- Distinct S1 units: concurrent model-backed child agents.
- Inter-S1 disturbance: same-file edits or contested resources are plausible, but the inspected supported team path does not independently establish a response to an observed conflict.
- Attenuating coordination relation: no qualifying inter-S1 relation established; task lists and a queue prevent generic scheduling races, not semantically competing work ownership.
- Feedback into subsequent S1 behaviour: worker results and messages return to the manager/leader, but without a verified conflict-specific control decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: S2-specific ownership is not credited for generic dispatch or action queue operations.
- Evidence: [Team mode wiring and TaskLock](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/group_router.py#L3238-L3330), [TaskLock](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/collaboration/task_lock.py), [WorkforcePattern](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/collaboration/workforce/workforce_pattern.py).
- Basis: structural.
- Confidence: medium.
- Caveats: developers may compose custom S2 adapters with the SDK; that is not automatically the shipped Studio default.

### Absence scope

- Surfaces inspected: WorkforcePattern, group router, task lock, Meta-Agent tool table, team manager, execution contexts and workspace controls.
- Plausible first-party paths checked: role delegation, dependency scheduler, TaskLock action queue, shared chat history, team message and resource admission checks.
- Why no material first-party path remains: the cited operations route work and serialize lifecycle messages, but none owns and closes a demonstrated specific peer-agent interference mode; machine-pressure admission is S3 support, not S2.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current root-session team by observing children and deciding when to spawn, communicate, retry or cancel during live task delivery.
- Disturbance / variety regulated: active child runs may stall/fail, saturate concurrency or CPU/memory, need new work or require intervention to meet the immediate user task.
- Decisive decision or feedback right: select and invoke status query, spawn/cancel/retry/message subagent tools in light of reported current child state and goals.
- Decision owner: configured root model-backed Meta-Agent within the supported Studio session, not the `AgentTeamManager` or the deterministic `ResourceMonitor`.
- Supporting / enforcement mechanisms: `AgentTeamManager` actual live status registry, timeouts, caps and resource admission checks; root Meta-Agent tool dispatcher; Studio event stream.
- Closure path: root sees team status/tool results, chooses a current-team intervention, `AgentTeamManager` changes a child run/permission to launch, and updated state returns to the root's next model turn.
- Boundary reachability: Studio builds the root Meta-Agent with visible team-management tools, and the attached `AgentTeamManager` executes them on real session children in the shipped local backend.
- Why this is / is not agent-owned: current worker-team decisions are controlled by the root model, while deterministic caps merely reject inadmissible actions.
- Whole-system current view: `query_subagent_status` and team status provide running/completed/failed child state and resource-monitor context for the session team.
- Current-control decision scope: the current portfolio of active/retryable child agents in one root session, including admission and cessation; not Enterprise gateway quotas or an unrelated Studio user.
- Evidence: [team lifecycle/status/cancel](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/team_manager.py#L480-L700), [meta tool handler](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/meta_tools.py#L2780-L3138), [resource monitor](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/resource_monitor.py).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: the model might choose not to use these tools; the claim is an available integrated operational loop, not a guaranteed policy of continuous proactive optimization.

## S3* — Complementary audit

- State: —
- Function: no independently controlled complementary reality-audit path with corrective control established for the current Studio session team.
- Disturbance / variety regulated: an executor can mistakenly report complete work while the real environment differs.
- Decisive decision or feedback right: no independent auditor's direct-evidence veto/intervention against the team report established in the selected operating mode.
- Decision owner: none established; SDK evaluation/LLM judge and Enterprise audit logging are separate or routine surfaces.
- Supporting / enforcement mechanisms: traces, tool results, observability and optional evaluation framework.
- Closure path: tests/evaluations can be explicitly launched, but a first-party independently owned standing complementary team audit with returned corrective control is not demonstrated.
- Why this is / is not agent-owned: evaluation APIs, group worker results and log chains cannot substitute for a separate auditor owner.
- Evidence: [evaluation/observability overview](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/README.md), [team results](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/team_manager.py), [Enterprise gateway separation](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/README.md#L31-L42).
- Basis: structural.
- Confidence: medium.
- Caveats: externally composed independent reviewers are possible through the SDK, but their independence cannot be credited to the shipped session team.

### Absence scope

- Surfaces inspected: runtime status/agent tool feedback, framework judge/evaluation, SDK collaboration patterns, Enterprise audit description and Studio session transitions.
- Plausible first-party paths checked: model judge, logs/traces, child QA, Enterprise append-only audit and session review learning hook.
- Why no material first-party path remains: these either evaluate current tasks inside production, record reports, or change future skills; no distinct complementary operational-reality auditor returns a systemic corrective judgment to the declared team controller.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: convert observations of changing external tool/provider/task conditions and user corrections into future reusable skill capability for subsequent sessions.
- Disturbance / variety regulated: repeated external tool failures, newly learned environment conventions and multi-step strategies that existing installed skills do not yet encode.
- Decisive decision or feedback right: the background model-backed review agent decides whether and how to create/patch a reusable skill; under the normal supervised mode the Desktop operator separately decides whether to approve the proposed future capability.
- Decision owner: opt-in skill-review agent in the direct-authorized mode (`A`), and legitimate Desktop-user approver for a separately supported queued-proposal mode (`P`). These modes are not simultaneous autonomous governance.
- Supporting / enforcement mechanisms: registered `SessionReviewHook`, actual tool observation records, signal/complexity gate, configured review model, `skill_manage`, skill policy scan, pending proposals and desktop approval endpoint.
- Closure path: a completed tool-using session triggers a review of observed attempts/errors/user corrections; the model proposes a skill; in explicitly authorized direct mode it writes the skill for later sessions, while in default queue mode the Desktop user approves the same proposed document and installs it. Later model runs can discover/use the changed skill collection.
- External distinction: observations concern user corrections and tool/provider outcomes from the task environment, not just the host runtime's own counters; the model interprets their reusable implications.
- Future / prospective distinction: a post-session reviewer encodes a method for *later* task contexts rather than repairing only the completed current task, and the installed skill survives that session boundary.
- Adaptation option generated: choose a new action-oriented skill or a patch to an existing skill, including the specific steps and guardrails for future comparable disturbances.
- Path back into current capability / S3: after authorized direct installation or Desktop-user approval, the skill is added to the local installed registry so a later Meta-Agent/runtime session can discover and use the revised capability under its current task controls.
- Boundary reachability: `AgentRuntime` registers `SessionReviewHook`; `learning.review_enabled` is an active shipped configuration option, `agent_writes_require_approval` distinguishes queue versus direct install, and Studio/Near expose proposal inspection/approve/reject routes. Both paths require configured model/provider access; neither is default-on just because observation is enabled.
- Why this is / is not agent-owned: the reviewer model selects substantive future reusable methods, not just a deterministic score; the operator retains the separate approval right in the supervised mode.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | configured background review model | opt-in `review_enabled` and complex tool-using session; direct writes explicitly permitted | skill `create/patch` writes accepted reusable guidance to later sessions | `session_review_hook.py`, `config.py`, `cli/agent_tools.py` |
| Parent (`P`) | Desktop user approving a model-authored queued proposal | normal `agent_writes_require_approval: true` on opt-in reviewer | Studio `/api/skills/proposals/{pid}/approve` applies the reviewed skill | `skills/pending_queue.py`, `studio/server.py`, Desktop `PendingProposalsList.tsx` |

- Evidence: [review trigger, LLM review and `skill_manage`](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/learning/session_review_hook.py#L168-L420), [opt-in and approval config](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/learning/config.py#L29-L92), [queuing versus direct write](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/cli/agent_tools.py#L10871-L11065), [Desktop-user review endpoint](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/studio/server.py#L8165-L8192).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: this is opt-in retrospective environmental learning with prospective reusable capability, **not** evidence of strategic foresight, reliable self-improvement, future performance gains, or unattended default deployment. The separate optional GEPA branch writes candidate proposals only; it is not credited as direct adaptation.

## S5 — Policy and identity

- State: —
- Function: no closed ultimate-purpose or identity-policy governance path for the local Studio agent-team recursion.
- Disturbance / variety regulated: conflicts about the team's permanent charter, legitimacy or non-negotiable identity beyond ordinary tasks/permissions.
- Decisive decision or feedback right: no runtime identity-level final authority and returned policy choice established in the selected local session hierarchy.
- Decision owner: none established for this function; product maintainers, Enterprise administrators and local user are adjacent authorities for different matters.
- Supporting / enforcement mechanisms: operator permissions, skill-approval gate, safety policies, user prompts, Enterprise Gateway policies and contributor governance.
- Closure path: users permit/deny operations, administrators configure Gateway routing, and skill approvals modify future capabilities; these are operational/safety/adaptation choices rather than a reconstructed identity-level decision loop in local Studio.
- Why this is / is not agent-owned: a Meta-Agent CEO label does not create sovereign identity control, and separate enterprise governance does not transfer to deployed Studio S5.
- Evidence: [runtime/Enterprise boundaries](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/README.md#L27-L42), [Studio tool gates](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/studio/server.py), [Meta-Agent identity prompt](https://github.com/DemonDamon/AgenticX/blob/582c9d00bfb23efe6f7e588c3a5edfce570729bf/agenticx/runtime/prompts/meta_agent.py).
- Basis: structural.
- Confidence: medium.
- Caveats: no finding about how the open-source project or enterprise tenants should normatively govern themselves is made.

### Absence scope

- Surfaces inspected: Studio Meta-Agent authority, agent/tool approval, skill proposal governance, Enterprise boundary, local session configurations and contributor documentation.
- Plausible first-party paths checked: CEO/Meta-Agent naming, skill approval, user permissions, Enterprise policy enforcement and maintainer release processes.
- Why no material first-party path remains: inspected decisions concern task allocation, access and model routing or future methods, not a legitimate identity-charter dispute escalated and resolved at the declared local team boundary.

## Distributed OSS parent arrangement

Apache-licensed code is contributed and maintained by an upstream OSS project. Enterprise operational administrators can govern the independently deployed Gateway but are not automatically the owner of the local Studio team's S5; local human approval is separately identified for opt-in S4 skill changes.

## Self-hosted and non-human modes

The local Studio/Near path is self-hosted and uses user-configured models. Root and children can act without approval for every model turn within policy, while risky tool and skill modifications have gates. S4's direct-write mode must be intentionally enabled and does not describe default Near behavior.

## Recursion

Each spawned model agent is an operational S1 with its own context but does not automatically possess a full viable metasystem. The Meta-Agent supervises its own session team; separate Studio sessions or an Enterprise compliance Gateway are not silently rolled up into this assessed recursion.

## Variety and escalation

The runtime uses caps, per-agent status and resource monitoring to contain immediate task variety; root-model decisions can spawn, message, cancel or retry children. Learning records observed difficulties and can escalate a proposed future skill to human approval. Neither the message bus nor a team's final task report alone establishes independent S2 or S3* autonomy. Ordinary session shutdown is not an S5 policy referendum.

## Evidence gaps

- S4: agent-owned code path is opt-in and can be configured to direct-write, but actual improvement quality and reuse in a later session were not measured; default approval mode remains parent-controlled.
- S3: source establishes a root decision/feedback affordance, not that any given external model has an effective proactive scheduling policy.
- S2 and S3*: a third-party developer may create more sophisticated agents using the SDK; their function ownership is outside the shipped local Studio boundary.
- The repository has many independent product/development tracks; design plans and Enterprise gateway policy have not been credited to the local runtime.
- No external provider or end-to-end live agent test was run.
