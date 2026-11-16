---
harness_id: poco
project_name: Poco
repository: https://github.com/poco-ai/poco-claw
review_ref: f4055e64f66e547a687206bac6e1891a97409448
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: ?
autonomy_s5: P
---

# Poco

## Review boundary

- System in focus: Poco's packaged self-hosted shared-server/channel AI-agent organization, with independent persistent server agents and a human operator at the channel/server recursion.
- Purpose and identity: Carry out user and channel tasks through model-directed tool use, retained sessions and shared channel operations.
- Relevant environment: Human channel and server members, requested tasks and artifacts, local/sandbox workspaces, model service and optional MCP/skill integrations.
- Standard-distribution boundary: First-party backend, executor, executor-manager and shipped supported configuration for server/channel agent tasks, plus its exposed server-admin and task-management operating mode.
- Credited operating / distribution surfaces: Backend server-agent identity/channel task management and run state; executor's SDK-backed agent and first-party channel task/memory tools; manager's executable queue/dispatch and skill staging.
- Adjacent first-party surfaces excluded from ownership: Developer/contributor and CI/release workflows; standalone test fixtures; web client display without decisive runtime feedback; unrelated workspace issue system when reasoning about channel-level S2; and the separate upstream Claude Agent SDK/provider's internal architecture.
- First-party operating / deployment modes considered: Model-backed persistent server/channel agent runtime; server and channel operator management; scheduler/queue lifecycle; optional enabled memory and creation/confirmation of reusable skills.
- Recursion level: One supported server/channel task organization; autonomous agent sessions are distinct S1 operating units. This is not a classification of the external model provider or independent host SDK.
- Reviewed revision: `f4055e64f66e547a687206bac6e1891a97409448`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Poco separates persistent backend state and channel-task APIs, an executor manager that claims runs and prepares sandboxes, and an executor that constructs `ClaudeAgentOptions` and consumes an external `ClaudeSDKClient` response stream. The shipped executor adds its own workspace, tool permissions, agent configuration, channel task MCP, memory MCP and run snapshots. Server-channel agents may respond to addressed messages via runtime-specific session creation and queue dispatch. Task assignment, status, priority and server membership persist in the first-party database; human operators act through supported management APIs. External Claude Agent SDK/model calls make agent/tool choices but their unimplemented internal algorithms are not credited as Poco-owned metasystem logic. [`executor/app/core/engine.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/engine.py#L234-L426), [`executor_manager/app/services/run_pull_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor_manager/app/services/run_pull_service.py#L141-L213), [`backend/app/services/server_agent_trigger_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_agent_trigger_service.py#L274-L356), [`backend/app/services/agent_identity_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/agent_identity_service.py#L165-L242).

## Operational model

Each enabled server agent receives channel messages or structured tasks, uses model-directed tools to produce a response/artifact, and returns events/status to the backend. Concurrent S1 units exist across persistent agent identities; within a run the scheduler and SDK-client leases serialize resources. The human operator can revise a channel-wide task/agent configuration; a model agent can read and update structured tasks via first-party channel MCP. An operator's current-control rights and identity authority must not be assigned to the agent merely because first-party tooling enforces them.

## S1 — Operations

- State: A
- Function: Handle a user/channel task with model-directed tool selection, sandbox/workspace actions and returned results.
- Disturbance / variety regulated: Unpredictable user requests, workspace contents, tool failures and cross-run context require discretionary next actions.
- Decisive decision or feedback right: Select the next model/tool action and revise the run using tool observations while satisfying task requirements.
- Decision owner: The executing model-backed agent, through the supported first-party SDK-backed executor mode; external SDK/provider supply execution dependency, not Poco-owned metasystem decisions.
- Supporting / enforcement mechanisms: Run/worker leases, workspace preparation, SDK options, permission callbacks, sandbox and tool interfaces.
- Closure path: Executor submits prompt to the SDK client, streams tool/model responses through first-party hooks, and reports terminal execution through the run lifecycle.
- Boundary reachability: Server message trigger creates a persistent agent task and the manager dispatches it to the packaged executor, which invokes the model SDK with first-party tool options.
- Why this is / is not agent-owned: Removing the model-backed agent leaves a deterministic queue and permission shell, not an implementation decision-maker.
- Evidence: [`executor/app/core/engine.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/engine.py#L234-L426); [`executor_manager/app/services/run_pull_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor_manager/app/services/run_pull_service.py#L325-L369); [`executor_manager/app/services/run_pull_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor_manager/app/services/run_pull_service.py#L574-L619); [`executor/app/core/client_pool.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/client_pool.py#L42-L64).
- Basis: structural
- Confidence: High for the first-party reachable model-backed operating path; not an execution benchmark.
- Caveats: Actual provider behavior was not live-tested; SDK-internal functions were not borrowed for S2–S5.

## S2 — Coordination

- State: —
- Function: No independently established inter-S1 conflict-attenuation function within the inspected channel agent mode.
- Disturbance / variety regulated: Possible concurrent work by separate channel agents on overlapping tasks; such conflict is a plausible disturbance but not yet shown to be attenuated by an S2-specific first-party mechanism.
- Decisive decision or feedback right: A decisive rule capable of detecting and resolving incompatible inter-agent work commitments was not established.
- Decision owner: No qualifying owner is established for inter-S1 coordination; agents can request collaboration and assign tasks, but this is not sufficient by itself.
- Supporting / enforcement mechanisms: Task status/assignee record, collaboration request, per-session queue and per-worker claim safeguards.
- Closure path: Channel task claim rewrites assignee and posts an event; it does not check prior assignee to reject a competing claim. Session serialization closes per-session execution, not competing S1 task commitments.
- Why this is / is not agent-owned: The agent may choose a collaboration recipient or task, but no function-specific inter-S1 disturbance regulation with returned conflict resolution is verified.
- Evidence: [`backend/app/services/server_channel_task_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_service.py#L865-L927); [`executor/app/core/channel_runtime.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/channel_runtime.py#L579-L649); [`backend/app/services/session_queue_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/session_queue_service.py#L276-L293); [`backend/app/services/run_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/run_service.py#L160-L205).
- Basis: structural
- Confidence: Moderate, bounded to the reviewed shipped channel task and run paths.
- Caveats: Other optional custom integrations are not credited; this is bounded absence rather than universal impossibility.

### Absence scope

- Surfaces inspected: Server channel task CRUD and claim, agent-facing channel MCP and collaboration requests, backend run claiming, same-session queue serialization, persistent agent trigger/dispatch.
- Plausible first-party paths checked: `claim_task` assignment semantics, request/handoff between distinct channel agents, in-channel task state feedback, per-session queue and worker claim gates.
- Why no material first-party path remains: The shipped paths move/overwrite tasks or serialize an individual run, but the reviewed code establishes no condition that detects and attenuates a conflict between distinct S1 task commitments and feeds its result into their subsequent work. Mere conversation/handoff and storing an assignee cannot substitute for an inter-S1 disturbance witness.

## S3 — Inside-and-now control

- State: P
- Function: Channel-level human-led revision of live task priorities, assignees and current commitments across a server/channel's agent team.
- Disturbance / variety regulated: Multiple active or pending tasks and agents can require current operational reprioritization or reassignment.
- Decisive decision or feedback right: Read the channel-wide task board and revise the selected task's priority, due date or assignee to redirect the team's live commitments.
- Decision owner: A legitimate channel/server operator in the supported human management mode, not an autonomous agent supervisor established over the whole team.
- Supporting / enforcement mechanisms: Persisted channel task board, assignee/status events, agent-readable channel task API, dispatch and runtime status services.
- Closure path: The persisted operator decision is returned through the same channel task repository exposed to agent `list_channel_tasks` and `read_channel_task`; agents can subsequently claim or act on the updated task assignment.
- Boundary reachability: First-party channel management endpoints persist human-selected changes, and packaged channel-runtime tools expose the resulting task state to subsequent model runs.
- Why this is / is not agent-owned: Model agents can update their own tasks but the source does not establish that they own team-wide current prioritization; the operator owns the evidenced broader decision.
- Evidence: [`backend/app/services/server_channel_task_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_service.py#L674-L683); [`backend/app/services/server_channel_task_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_service.py#L729-L812); [`executor/app/core/channel_runtime.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/channel_runtime.py#L651-L768); [`backend/app/services/server_channel_task_agent_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_agent_service.py#L185-L231).
- Basis: structural
- Confidence: Moderate: verified supported owner/board/return path, not automatic autonomous S3.
- Caveats: No claim that every operator edit results in an immediate agent run; the feedback is available on the next relevant task read.

- Whole-system current view: `list_tasks` enumerates tasks in the selected channel/team, including status and assignees; the scope is that channel rather than all independent Poco deployments.
- Current-control decision scope: Task priority, due-date, assignee and position/status adjustments across channel tasks, with persisted changes and agent-accessible reads.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit function was established in the scoped standard-distribution server/channel operation.
- Disturbance / variety regulated: Operational reporting and changes can be inaccurate; an audit would need materially different access and independent judgment.
- Decisive decision or feedback right: No first-party complementary audit decision or corrective independent feedback path was established.
- Decision owner: None established. A human could inspect work, but generic access to a UI or task state is not a separately evidenced audit organization.
- Supporting / enforcement mechanisms: Workspace diffs, Git run snapshots, execution/error callbacks and `in_review` task status.
- Closure path: These artifacts retain ordinary execution evidence; the inspected runtime does not autonomously or in an evidenced first-party audit mode compare independent observations and return an independent corrective finding to subsequent control.
- Why this is / is not agent-owned: Snapshots and task status are evidence suppliers, not an independent auditor or audit decision owner.
- Evidence: [`executor/app/hooks/workspace.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/hooks/workspace.py#L22-L56); [`executor/app/hooks/run_snapshot.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/hooks/run_snapshot.py#L38-L192); [`backend/app/services/server_channel_task_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_service.py#L814-L863).
- Basis: structural
- Confidence: Moderate, bounded to the inspected shipped standard execution, task and run evidence surfaces.
- Caveats: An external independent reviewer may use exported artifacts; external services and future user composition are excluded.

### Absence scope

- Surfaces inspected: Executor workspace and run-snapshot hooks, channel task state transitions, run lifecycle/callback and human task-management surfaces.
- Plausible first-party paths checked: Git snapshot evidence at run completion, file-diff observation and structured task `in_review` status.
- Why no material first-party path remains: The inspected shipped code records ordinary process evidence and can mark work for review, but provides neither an independent audit judgment nor an independently controlled alternate evidence access path whose finding changes subsequent current control.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Potential future-capability adaptation via discovery, human confirmation and installation of workspace-derived reusable skills remains unresolved as a full S4 loop.
- Disturbance / variety regulated: Changing task demands may expose capability gaps and useful reusable tools.
- Decisive decision or feedback right: Select a prospective reusable skill in response to a future/environment distinction, approve and feed it into later runtime capability.
- Decision owner: Unresolved: a human owns final skill confirmation; it has not been established that a supported organization-level outside-and-then intelligence path owns the prospective recommendation rather than merely packaging a generated workspace file.
- Supporting / enforcement mechanisms: Pending-skill discovery after successful skill tool uses, workspace-export metadata, confirmation endpoint, user skill registry and skill stager.
- Closure path: Confirmed workspace skill files are copied to the registry and enabled, with enabled skills staged into later execution. A full environment-sensing/prospective-feedback function and its decisive judgment ownership were not proven.
- Why this is / is not agent-owned: Neither a successful `Skill` tool use nor a UI confirmation automatically makes the agent the owner of prospective organizational adaptation.
- Evidence: [`backend/app/services/pending_skill_creation_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/pending_skill_creation_service.py#L37-L105); [`backend/app/services/pending_skill_creation_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/pending_skill_creation_service.py#L182-L236); [`backend/app/services/skill_workspace_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/skill_workspace_service.py#L75-L173); [`executor_manager/app/services/skill_stager.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor_manager/app/services/skill_stager.py#L55-L98).
- Basis: structural; unresolved functional ownership
- Confidence: Low for full S4; high for concrete skill artifact/confirmation/staging mechanisms.
- Caveats: The shipped path could support operator-assisted adaptation but the external distinction, prospective decision and closed S4 return into S3 are not sufficiently established for P or C(P).

- External distinction: Task-derived workspace outputs and human skill suggestions may carry information from the task environment; the code does not identify a dedicated external trend/forecast sensing path.
- Future / prospective distinction: An approved skill can be retained across subsequent sessions; evidence of a prospective capability decision rather than retrospective file import remains unresolved.
- Adaptation option generated: Candidate `SKILL.md` exported from an agent workspace, awaiting user confirmation.
- Path back into current capability / S3: Confirmed skills are enabled in the user registry and included in subsequent executor staging, without proof of explicit S3 intake of an external/future adaptation decision.

## S5 — Policy and identity

- State: P
- Function: Legitimate operator governance of server agent identity and ultimate membership authority for the operational team.
- Disturbance / variety regulated: New, withdrawn or transferred agent identities and channel membership change which agents are authorized to operate.
- Decisive decision or feedback right: Create/remove agent identities and determine team/channel membership, plus transfer server ownership to a legitimate member.
- Decision owner: Server/channel owner or authorized server administrator in the first-party management mode; model agents do not grant their own ultimate server identity.
- Supporting / enforcement mechanisms: Server ownership/membership checks, persistent agent state, membership repository, runtime stop and queued-work cancellation.
- Closure path: Authorized human identity decisions persist to the agent and server registry and reach subsequent operation: new identities get runtime state, removed identities are inactivated, their queues canceled, and their membership marked removed.
- Boundary reachability: Server admin/owner endpoints are first-party deployed operations, and the persisted identity and membership state governs which agent runtimes can accept channel tasks.
- Why this is / is not agent-owned: An agent can accept tasks but cannot exercise the evidenced ultimate identity creation/removal/ownership-transfer right independently.
- Evidence: [`backend/app/services/agent_identity_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/agent_identity_service.py#L165-L242); [`backend/app/services/agent_identity_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/agent_identity_service.py#L300-L335); [`backend/app/services/agent_identity_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/agent_identity_service.py#L395-L475); [`backend/app/services/server_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_service.py#L179-L221).
- Basis: explicit code authority and operational closure
- Confidence: High for the bounded server-level identity governance mode.
- Caveats: Ordinary per-tool permission approvals are excluded; the identity claim concerns agent existence and legitimate server membership, not all organization policy.

- Identity / ultimate-policy issue: Which persistent agents constitute the server organization and are permitted to act as channel members, and who legitimately owns the server.
- Ultimate authority in each claimed mode: Human server owner/admin; no autonomous model-owned identity-governance mode established.
- Return-to-operation path: Identity creation initializes persistent runtime and membership; removal deactivates runtime, cancels work and removes memberships; ownership transfer changes the authorized server decision holder.

## Distributed OSS parent arrangement

This assessment is about a **deployed self-hosted server/channel team**, not contributors to Poco's GitHub development organization. No maintainer PR or release practice is borrowed as an organization-level `(P)` claim. Positive S3 and S5 parent rights are bounded to supported operator APIs at the deployed team recursion.

## Self-hosted and non-human modes

The packaged self-hosted server exposes operator task and identity controls, while model-backed workers decide ordinary S1 actions. No independent first-party autonomous S3 or S5 closure was established, so S3/S5 are reported as `P`, not `A(P)`. Human approval for a tool in plan mode is an operational permission step, not itself evidence of S5.

## Recursion

A Poco deployment contains a server, channels and persistent agent identities. The credited recursion is one channel task organization under a server's legitimate ownership. Distinct active agents are the S1 units. A model-internal subagent spawned through `SdkAgentDefinition` remains a lower-level execution dependency; it does not automatically create a higher-recursion viable system.

## Variety and escalation

Channel messages and changing task assignments introduce task variety; autonomous agent decisions absorb ordinary work variety. The backend persists run/task state and delegates control to a human operator for team-level reprioritization, agent membership and identity. Plan-mode `ExitPlanMode` can request human approval; an exceptional interruption is not a separate VSM function, and this does not itself close S5. [`executor/app/core/engine.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/executor/app/core/engine.py#L117-L232), [`backend/app/services/server_channel_task_service.py`](https://github.com/poco-ai/poco-claw/blob/f4055e64f66e547a687206bac6e1891a97409448/backend/app/services/server_channel_task_service.py#L729-L863).

## Evidence gaps

- No live model/provider/sandbox execution trace was collected. Claims follow code-reachable first-party paths at the frozen revision.
- For S4, the skill proposal→confirmation→staging pipeline is present, but its **outside-and-then** sensing/decision/return role at this recursion has not been validated; resolve through an exact-source traced supported case before assigning positive S4.
- For S2, reassess if a separate first-party shipped collision-attenuation path among distinct channel agents is produced; the inspected task-claim implementation permits reassignment without conflict adjudication.
- For S3*, independent audit judgment and independent alternate access have not been shown; `in_review`, Git snapshots and telemetry alone are not positive proof.
- Third-party Claude SDK internals, optional external MCP servers, private deployed activity and repo development/dogfood actions are outside this assessment's owner claims.
