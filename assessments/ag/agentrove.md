---
harness_id: agentrove
project_name: Agentrove
repository: https://github.com/Mng-dev-ai/agentrove
review_ref: a1cfe4999f50646b00dcab696483d1526071291b
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agentrove

## Review boundary

- System in focus: One Agentrove workgroup in a configured coding workspace, with either a lead chat and its attached workers or a supervised group channel.
- Purpose and identity: Carry out software changes and investigation with installed coding agents, preserving workspace and turn continuity.
- Relevant environment: User goals, an operator-provisioned code workspace, supported ACP agents and model credentials.
- Standard-distribution boundary: Backend, frontend, sandbox and bundled Agentrove MCP service in the self-hosted distribution. Attached agents supply operational discretion in the supported modes.
- Credited operating / distribution surfaces: Self-hosted backend and workspace, bundled MCP tools, ACP adapters, delegated subthreads, and channel activity and intervention routes.
- Adjacent first-party surfaces excluded from ownership: Release and contributor CI, desktop/mobile packaging and the repository's own test harness. GitHub review decisions and ACP provider internals remain outside the system in focus.
- First-party operating / deployment modes considered: Individual workspace chat, MCP lead and workers, multi-agent channel, and scheduled chat or channel dispatch.
- Recursion level: One workgroup applied to a workspace assignment. Individual agent turns and workers are operational units. The deployment and operator sit above this workgroup.
- Reviewed revision: a1cfe4999f50646b00dcab696483d1526071291b
- Observation date: 2026-11-15
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The [distribution](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/docker-compose.yml) runs the web and backend services with the first-party MCP service. The backend binds supported ACP sessions to workspace directories, model configuration and tools. The [agent service](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/agent.py#L498-L654) constructs the MCP configuration and the session; the stream runtime records outcomes and forwards a delegated child's completion or request to its lead. Channels maintain a separate message and activity stream with per-member delivery and retry. The user configures workspace access, credentials and agent selection before operation.

## Operational model

A workgroup produces repository changes, investigations or a consolidated response. A worker chat or channel member uses its configured coding agent to choose actions and return results. The lead can choose which worker runs, how its work is isolated and how to respond if it stalls. In channels the operator can see group-wide activity and adjust the current commitments of the group.

## S1 — Operations

- State: A
- Function: Execute an assigned coding or investigation task in a workspace.
- Disturbance / variety regulated: Uneven codebase conditions, tool outcomes and the changing information needed to complete the assignment.
- Decisive decision or feedback right: Choose successive edits, tool actions and a task result in the configured execution mode.
- Decision owner: The ACP coding agent operating as a workspace chat or worker.
- Supporting / enforcement mechanisms: Workspace binding, ACP session and tool feedback, stream lifecycle and result persistence.
- Closure path: The agent receives a prompt, acts in its bound workspace, receives tool feedback and returns a persisted completion or interruption to the user or lead.
- Boundary reachability: The Docker distribution and first-party ACP launcher connect the agent to the workspace and its available tools after ordinary provisioning.
- Why this is / is not agent-owned: The running agent chooses task actions and when to return a result.
- Evidence: [ACP prompt and update loop](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/agent.py#L147-L232), [MCP runtime binding](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/agent.py#L498-L654), [worker launch contract](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/mcp-server/server.py#L462-L573).
- Basis: Source reconstruction.
- Confidence: High.
- Caveats: Models, credentials and supported tool permissions remain deployment prerequisites.

## S2 — Coordination

- State: A
- Function: Attenuate collisions between agent units sharing a working directory.
- Disturbance / variety regulated: Two members can attempt overlapping file changes or redundant responses to the same developing discussion.
- Decisive decision or feedback right: Choose and announce an intended edit, yield when another member is working on it, or suppress a redundant response.
- Decision owner: The participating agents in the channel.
- Supporting / enforcement mechanisms: The injected introduction gives a file-level avoidance rule; the channel incorporates agent replies into subsequent member prompts.
- Closure path: An agent announces its edit scope. Subsequent deliveries expose that intent to other members, whose next work selection can exclude that scope.
- Boundary reachability: First-party group channels install the prompt and delivery behavior on configured member sessions.
- Distinct S1 units: Separate channel member agents with their own execution sessions.
- Inter-S1 disturbance: Overlapping edits in the shared directory and repetitive turn responses.
- Attenuating coordination relation: Before-edit announcement, peer avoidance and a reply-or-pass protocol.
- Feedback into subsequent S1 behaviour: Later prompts include the peer response and its stated work scope so a member can yield or choose another edit.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped instructions explicitly connect each unit's intended edit to the other units' next permissible work choices.
- Why this is / is not agent-owned: Members decide whether their proposed work overlaps an announced action and which action they take next.
- Evidence: [File-avoidance protocol](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/channel.py#L84-L105), [protocol injection and member execution](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/channel.py#L1235-L1305), [reply redistribution](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/channel.py#L1547-L1614).
- Basis: Source reconstruction.
- Confidence: Medium.
- Caveats: The coordination protocol depends on agents following the prompt. Simultaneous edits can still race before the announcements propagate.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate active worker commitments and interruptions across one live workspace assignment.
- Disturbance / variety regulated: Stalled workers, conflicting or unfinished assignments, and the need to stop or redirect the group.
- Decisive decision or feedback right: Decide whether a worker continues, gets redirected or stops in the lead mode. Decide how the channel's active commitments and membership change in the operator mode.
- Decision owner: Lead agent in an MCP-delegated workgroup. The owning operator in a supervised group channel.
- Supporting / enforcement mechanisms: Lead-accessible chat roster, outcomes, pending requests, follow-up and cancellation. Channel activity and pending permissions, member controls, group stop and subsequent message dispatch.
- Closure path: A finished or blocked turn wakes the lead. It can answer a pending request, stop a worker or revise its assignment. In the channel mode, operator intervention cancels active turns or changes membership, and the next committed prompt fans out over the resulting group.
- Boundary reachability: Both the lead session's bundled MCP service and the channel owner's backend API and UI are ordinary supported features.
- Whole-system current view: Lead sees the workgroup through its child roster, completion and interruption summaries, with drill-down into each worker. Channel owner sees participant activity and pending inputs in a shared view.
- Current-control decision scope: Restart, stop or reassign an active commitment, including a group interruption and resumed work with changed membership or priorities.
- Why this is / is not agent-owned: The lead chooses the intervention in its delegated workgroup. The operator exercises the corresponding workgroup-level discretion in a supervised channel.
- Evidence: [MCP worker roster and controls](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/mcp-server/server.py#L326-L358), [stop and pending-request controls](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/mcp-server/server.py#L597-L682), [lead wake and feedback](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/subthread_wake.py#L371-L407), [owner-bound channel operations](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/api/endpoints/channels.py#L205-L284), [group stop and delivery handling](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/channel.py#L1616-L1642).
- Basis: Source reconstruction and [first-party wake test cases](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/tests/test_subthread_wake.py#L57-L174).
- Confidence: Medium.
- Caveats: Evidence covers one workgroup and the source-defined lead and operator modes. Matters requiring the user's judgement may still be escalated.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead chat's agent | One or more workers finish, stall or need a decision | Lead receives workgroup reports and changes active assignments or unblocks a worker through MCP | [Lead wake instructions](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/subthread_wake.py#L371-L407) |
| Parent (`P`) | Channel-owning operator | Workgroup activity indicates blocked or misdirected effort | Operator inspects group activity, interrupts or changes membership, and issues the revised assignment through the channel | [Channel endpoints](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/api/endpoints/channels.py#L205-L284), [channel UI activity](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/frontend/src/components/channels/ChannelView.tsx#L389-L429) |

## S3* — Complementary audit

- State: —
- Function: Independent inspection of ongoing operational claims and return to control.
- Disturbance / variety regulated: Reported progress or completion can diverge from the actual worktree or execution evidence.
- Decisive decision or feedback right: Select a claim, inspect independent evidence and return an actionable judgment to workgroup control.
- Decision owner: No audit-specific owner established in the shipped workgroup.
- Supporting / enforcement mechanisms: Chat history, worktrees and the external GitHub review interface expose potential evidence.
- Closure path: No dedicated verdict and return path is installed for an audit role.
- Why this is / is not agent-owned: An agent reviewer requires a separately assigned mandate and evidence target.
- Evidence: [Documented reviewer-persona recipe](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/README.md#L25-L38), [event logging](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/streaming/runtime.py#L475-L517), [GitHub reviewer routing](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/github.py#L187-L212).
- Basis: Bounded source inspection.
- Confidence: Medium.
- Caveats: A user or lead can compose an audit by creating a reviewer persona and assigning an independent inspection.

### Absence scope

- Surfaces inspected: Bundled worker and persona tools, documented reviewer recipe, GitHub review integration, event logging, channel and lead feedback.
- Plausible first-party paths checked: Reviewer worker with diff access, stream audit records and GitHub reviewer requests.
- Why no material first-party path remains: The documented recipe supplies ordinary worker launch and return tools. It leaves the audit mandate, independent sampling target and use of findings to the user's or lead's ad hoc composition. The event archive preserves the producing stream. GitHub reviewer routing leaves the judgment and feedback with the external review process.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense relevant environmental change, choose prospective adaptations and install them into subsequent capability.
- Disturbance / variety regulated: Future work can face changed tools, systems and requirements.
- Decisive decision or feedback right: Select a future-relevant change and alter reusable workgroup capability in response.
- Decision owner: No adaptation owner established in the shipped workgroup.
- Supporting / enforcement mechanisms: Scheduled dispatch, persistent memories and persona editing supply general tools.
- Closure path: No shipped trigger-to-adaptation path connects environmental change to a governed capability update.
- Why this is / is not agent-owned: A scheduled task author can compose the judgment and capability update.
- Evidence: [MCP memory and persona tools](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/mcp-server/server.py#L254-L459), [memory prompt composition](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/memory.py#L77-L101), [scheduled dispatch](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/automation.py#L337-L440).
- Basis: Bounded source inspection.
- Confidence: Medium.
- Caveats: A configured scheduled prompt can instruct an agent to carry out an adaptation workflow.

### Absence scope

- Surfaces inspected: Automation definitions and dispatch, memory storage and prompt loading, persona tools, installed models and adapters.
- Plausible first-party paths checked: Scheduled external sensing, reusable persona changes and memory-based feedback to future turns.
- Why no material first-party path remains: Scheduler dispatch executes user- or agent-supplied tasks. Memory and personas persist selected context. The shipped operating modes leave the environmental distinction, prospective options and adaptation judgment to an externally specified workflow.

## S5 — Policy and identity

- State: —
- Function: Resolve workgroup identity or ultimate-policy decisions and return them to ongoing operation.
- Disturbance / variety regulated: Potential conflict over the workgroup mission or the enduring boundary of its mandate.
- Decisive decision or feedback right: Settle the workgroup identity or ultimate policy and bind future operation to it.
- Decision owner: No identity or ultimate-policy owner established in the assessed workgroup modes.
- Supporting / enforcement mechanisms: Workspace provisioning, agent permissions, channel membership and ordinary query escalation.
- Closure path: No workgroup identity decision and durable governance return were established.
- Why this is / is not agent-owned: The lead agent may refer individual issues to the operator. The observed intervention path covers ordinary work.
- Evidence: [Channel permission and member controls](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/api/endpoints/channels.py#L227-L284), [member configuration updates](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/channel.py#L837-L889), [lead escalation prompt](https://github.com/Mng-dev-ai/agentrove/blob/a1cfe4999f50646b00dcab696483d1526071291b/backend/app/services/subthread_wake.py#L389-L407).
- Basis: Bounded source inspection.
- Confidence: Medium.
- Caveats: Operators retain workspace and model provisioning authority.

### Absence scope

- Surfaces inspected: Operator configuration and channel controls, chat modes, role and persona specifications, escalation from worker to lead and user.
- Plausible first-party paths checked: User permission decisions, member configuration, persistent persona changes and escalated worker questions.
- Why no material first-party path remains: Those paths govern execution permissions, role configuration or individual workgroup decisions. The inspected workgroup modes supply no route that identifies and resolves an identity or ultimate-policy issue and feeds it back as governing policy.

## Recursion

A workspace workgroup contains participating turns and workers as S1 units. Agentrove's flat sub-thread model implements the lead-to-worker return at a single level. Additional independent workspaces and the operator's deployment choices sit above the assessed unit.

## Variety and escalation

MCP tools expose distinct ways to continue, redirect, answer or cancel a blocked worker. The lead's wake prompt directs questions requiring user judgement back to the user. Group channels offer aggregate activity and operator intervention for current work.

## Evidence gaps

This assessment uses pinned source and test definitions. Provider-backed runs, compliance with the channel prompt under simultaneous edits and backing-service restart behavior of pending lead wakes were not exercised.
