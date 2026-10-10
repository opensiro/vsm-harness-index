---
harness_id: commonly
project_name: Commonly
repository: https://github.com/Team-Commonly/commonly
review_ref: 669889886a9436b8349e4e60e5197bab504909e8
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Commonly

## Review boundary

- System in focus: one self-hosted Commonly pod consisting of first-party pod/seat workspace services, shipped Tier-1 native model/tool runtime, shared attention claims, task-board controls, human pod writer/owner and optional first-party multi-seat modes.
- Purpose and identity: a workspace where human pod members and individually installed AI seats collaboratively process messages and tasks, with persistent pod context and per-seat memory.
- Relevant environment: humans/users and project task context, Mongo/PG databases, LiteLLM backend, external channels, optional BYO Claude/Codex/Cursor runtime, operator-controlled Docker/cloud deployment and connected services.
- Standard-distribution boundary: `backend/services/nativeRuntimeService.ts`, pod task/event/claim services, installed native first-party agent definitions and packaged web UI. Model providers supply cognition but Commonly implements and owns its native model/tool/result loop.
- Credited operating / distribution surfaces: native Tier-1 runAgent, first-party configured native apps, pod/seat registry, atomic message claims and claim-then-decline return, task status/assignment API and UI, event notification, grants/decision-request service.
- Adjacent first-party surfaces excluded from ownership: generic `@commonlyai/mcp` client/wrapper mode without native model-loop ownership; outside user-controlled agent CLI internals; docs/roadmap/test-only integrations, community marketplace examples not installed by default, and maintainer governance.
- First-party operating / deployment modes considered: self-hosted Compose/K8s UI with native installed Tier-1 agents (requires a configured LiteLLM provider), optional multiple pod seats, BYO CLI daemon/manual attach, human pod task-board parent controls, operator grants and scheduled native apps.
- Recursion level: **one pod**, with distinct installed model-backed seat instances as S1s. The multi-pod service itself, tenant administration and the Commonly OSS project are separate recursions.
- Reviewed revision: `669889886a9436b8349e4e60e5197bab504909e8`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The shipped `nativeRuntimeService.runAgent` makes bounded iterative LiteLLM `chat/completions` calls, dispatches explicitly allowlisted Commonly native tools (pod context, memory, messages, task creation, action proposal, agent status), returns tool outcomes and records run turns. Installed native app configs and `agentEventService` wire real pod triggers into this first-party loop. The separate CLI/BYO agents may use a Commonly MCP/REST plane while running their own proprietary or third-party model session; those external sessions are not donated to Commonly's internally owned loop.

At the pod boundary two or more installed seats may receive one human wake. `messageClaimService` performs a CAS lease so one seat responds while rivals stand down; explicit declines are recorded and `messageClaimHandoffService` re-offers the same message to the next permitted original target, supplying a concrete non-chat-only interference controller. Pod members with write permission see all pod tasks and can revise current assignments/statuses; task event/notification mechanisms return decisions to operational seats. Scheduler heartbeats, multiagent ensemble turn order, per-seat memory and grants are first-party support but cannot be promoted to S3*/S4/S5 merely by their labels.

Primary source routes at the frozen revision: [nativeRuntimeService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/nativeRuntimeService.ts); [agentEventService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentEventService.ts); [messageClaimService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/messageClaimService.ts); [messageClaimHandoffService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/messageClaimHandoffService.ts); [tasksApi.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/tasksApi.ts); [taskEventService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/taskEventService.ts); [agentEnsembleService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentEnsembleService.ts); [schedulerService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/schedulerService.ts); [grants.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/grants.ts).

## Operational model

S1 units are real installed native model sessions performing discretionary turns with first-party tools, not merely stored seat names. Message claims regulate a specific inter-S1 duplicate-response and abandoned-wake disturbance. The operator-authored pod with an authorized human writer is a distinct supported parent mode controlling the pod-wide **current task portfolio**; its task-board intervention loop is not proof of model-owned S3. Runtime quotas, subscriptions, turn order, event queues, hub ACLs and grants do not autonomously decide policy, priorities or future adaptation.

## S1 — Operations

- State: A
- Function: run real model/tool/feedback sessions for installed native agents serving pod requests and updating pod messages/tasks/memory.
- Disturbance / variety regulated: pod user requests, changing discussion context, returned tool outcomes, memory and local service errors.
- Decisive decision or feedback right: which reply and allowed tool call to make in each native model turn, and whether to continue with additional tools.
- Decision owner: the installed native agent's model-backed turn; Commonly supplies the actual bounded model-call/tool-result loop.
- Supporting / enforcement mechanisms: `runAgent`, LiteLLM `/chat/completions`, allowlisted `commonly_*` tool dispatcher, `AgentRun` traces, message/claim constraints and caps.
- Closure path: an addressed/scheduled native installation receives trigger → model chooses tool call → first-party dispatcher executes permitted tool → result enters message history → next model turn chooses subsequent action/response.
- Boundary reachability: shipped native `runtimeType:'native'` installations are dispatched through first-party agentEventService to nativeRuntimeService when LiteLLM is configured; optional BYO seats are not needed to demonstrate the native loop.
- Why this is / is not agent-owned: removing model calls leaves relay/DB handlers and deterministic tools but no discretionary content/operation decisions.
- Evidence: [nativeRuntimeService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/nativeRuntimeService.ts); [agentEventService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentEventService.ts); [task-clerk.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/config/native-agents/task-clerk.ts); [index.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/packages/commonly-apps/src/task-clerk/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Native LiteLLM must be configured; BYO seats alone are not a first-party native model loop.

## S2 — Coordination

- State: C
- Function: attenuate duplicate or abandoned work by two distinct active seat agents receiving the same human pod message through first-party exclusive attention claims and bounded handoff.
- Disturbance / variety regulated: multiple seat S1s may answer the same broad human message, produce duplicate/conflicting replies, or a dead/declining seat may leave it unattended.
- Decisive decision or feedback right: determine which seat may own a message claim, make other seats stand down and select the next eligible wake target after an explicit decline.
- Decision owner: first-party deterministic CAS lease/attention kernel plus preconfigured original wake-target set, not a packaged autonomous coordinator that adaptively decides agent selection.
- Supporting / enforcement mechanisms: message_claims transaction/lease with a single valid holder, decline history, handoff service and per-seat runtime claim/release paths.
- Closure path: broadcast message produces potential seat wakeups → claim transaction grants one seat/denies other → loser stands down → winner processes, or explicitly declines → release/handoff enqueues next eligible original seat → next S1 acts while rejected seats do not.
- Boundary reachability: native runtime attempts claims before model work and releases them at terminal; shipped local/CLI adapters also use the shared kernel, though their own external cognition is not credited to the kernel.
- Why this is / is not agent-owned: the disturbance-specific first-party gate and returned handoff are real, but their selection policy is enforced by lease/CAS and configured targets, not autonomously chosen by a first-party S2 model actor; this is C, not A.
- Evidence: [messageClaimService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/messageClaimService.ts); [messageClaimHandoffService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/messageClaimHandoffService.ts); [nativeRuntimeService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/nativeRuntimeService.ts); [agentMentionService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentMentionService.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: A deterministic exclusive claim is a real S2-specific construction path, not agent-owned planning; seat-agent cognition and policy choice are not credited to the kernel.

- Distinct S1 units: two separately installed model-backed seats in the same pod, independently addressed by the original human message.
- Inter-S1 disturbance: simultaneous seats replying to one human message create duplicated/conflicting operational responses, while one abandoned/declined claim may suppress necessary downstream service.
- Attenuating coordination relation: CAS `message_claims` gives exactly one lease, rejects rival claims and preserves explicit decline state for limited one-seat handoff.
- Feedback into subsequent S1 behaviour: losing seat stands down before its model loop; a declined seat's handoff event wakes the next original unserved seat, changing which S1 works next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: duplicate-answer suppression and return on decline specifically regulate inter-seat contention for the same operational request, not merely generic chat distribution.

## S3 — Inside-and-now control

- State: P
- Function: a legitimate human pod-member/operator sees the pod task portfolio and installed agents and can revise current assignments, statuses and commitments, returning those revisions to active work.
- Disturbance / variety regulated: misallocated, stale or blocked pod tasks and changes to commitments/work priorities across seats.
- Decisive decision or feedback right: human pod member with write authority can assign/reassign, change task status, dependency and scope, and push the new current commitments into agent notifications.
- Decision owner: authorized human pod operator/member in the supported parent-governed task-board mode; not the native model or automated lease/scheduler.
- Supporting / enforcement mechanisms: pod-scoped GET of full task set with lease states, PATCH task fields, membership write check, per-task update history, task event notifications, UI board.
- Closure path: operator observes complete pod task board plus seat status → makes current-work allocation/status decision → authorized task PATCH commits changed assignment/status → `notifyPodAgents` and board events deliver feedback to operational seat agents.
- Boundary reachability: the self-hosted web UI and backend task APIs ship as the supported human-in-the-loop pod control mode; all task changes are scoped to a pod and gated to writers.
- Why this is / is not agent-owned: the model/tool loops and message claims do not autonomously aggregate and control the pod's full current commitments; in this supported mode the parent writer owns current task portfolio interventions.
- Evidence: [tasksApi.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/tasksApi.ts); [V2PodBoard.tsx](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/frontend/src/v2/components/V2PodBoard.tsx); [taskEventService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/taskEventService.ts); [agentStateService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentStateService.ts).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: P refers only to the pod-scoped human task-board current-control loop; it does not infer organization-level governance for all pods or the maintainer community.

- Whole-system current view: a pod-authorized human can request the unfiltered pod task list with claim/lease state and view the installed agent roster, rather than only one personal task.
- Current-control decision scope: pod-wide task assignment/reassignment, status change, blocking, dependency metadata and current work commitments; not just approval of a single tool call.
- Parent-mode whole-current view and return: the same human writer who inspects all pod tasks is authorized to patch current portfolio state, and task events/agent notifications return those decisions to live seats.
- Legitimate parent authority: human pod member granted write access by pod membership enforcement; this is a local parent arrangement for one pod, not a shared organizational parent for the OSS community.

## S3* — Complementary audit

- State: ?
- Function: a complementary audit of reported agent task completion by an independent access route; not established from reviewed surfaces.
- Disturbance / variety regulated: incorrect completion reports, ungrounded answers or unverified PR/task artefacts.
- Decisive decision or feedback right: not established: the inspected audit logs/task updates provide evidence and visibility but no separate challenge owner and independently returned correction path was reconstructed.
- Decision owner: unresolved; human users can view records, but that alone is not a credited complementary audit system.
- Supporting / enforcement mechanisms: task change history, `AuditLog`, and agent ensemble observers are available instrumentation/roles without a proven independent direct-source audit procedure.
- Closure path: no concrete independent audit finding → controller correction → changed S1 path verified.
- Boundary reachability: the reviewed runtime, task board, audit logging and ensemble turn scheduler do not suffice for positive credit; additional first-party modules might alter this.
- Why this is / is not agent-owned: storage/observability and routine multi-agent conversation alone cannot substitute for a contrasting evidence-access/independent reviewer.
- Evidence: [agentEnsembleService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentEnsembleService.ts); [tasksApi.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/tasksApi.ts); [AuditLog.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/models/AuditLog.ts).
- Basis: explicit + structural + unknown.
- Confidence: medium (in unresolved closure).
- Caveats: Inspected support mechanisms do not justify a confident positive state; uncertainty is not a universal absence claim.

- Claim being audited: an agent's statement that a pod task or produced artefact is correct.
- Ordinary reporting path: agent message, task completion/status and task change history.
- Complementary access path: not independently established; audit-log existence is not proof a challenger reads source/artefacts apart from the claimed narrative.
- Independence boundary: not established for a mandatory or optional first-party evidence-challenger role.
- Who acts on findings: a human could intervene, but no complete first-party independent-audit → returned intervention path was demonstrated.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospective external-environment sensing and adaptation of the pod's future operating capability remains unresolved.
- Disturbance / variety regulated: new external requirements, provider/capability shifts and future team needs.
- Decisive decision or feedback right: unproven; scheduled summaries, memories, marketplace/installables and heartbeats do not by themselves settle adaptation choices or close them back into present capability.
- Decision owner: unknown. Users can install/configure seats and models can remember information, but the S4 decision loop is not evidenced.
- Supporting / enforcement mechanisms: pod-summarizer, long-term memory, scheduler, installable app registry, config APIs.
- Closure path: no witnessed external distinction → prospective option → legitimate decision → changed pod operational capability loop.
- Boundary reachability: shipped native summaries and memory exist but have not been connected into a decisive prospective adaptation loop.
- Why this is / is not agent-owned: a retrospective digest and static memory are not sufficient for agent-owned or parent-owned S4.
- Evidence: [schedulerService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/schedulerService.ts); [agentMemoryService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/agentMemoryService.ts); [index.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/packages/commonly-apps/src/pod-summarizer/index.ts).
- Basis: explicit + structural + unknown.
- Confidence: medium (in unresolved closure).
- Caveats: Inspected support mechanisms do not justify a confident positive state; uncertainty is not a universal absence claim.

- External distinction: not reconstructed beyond ordinary chat/provider inputs and generic knowledge sources.
- Future / prospective distinction: scheduled digests and persistent memory do not establish a future-specific adaptation question.
- Adaptation option generated: not evidenced as a first-party system capability decision.
- Path back into current capability / S3: absent from the inspected evidence; further source review required before changing `?`.

## S5 — Policy and identity

- State: ?
- Function: whole-pod identity/ultimate-policy resolution, beyond permissions and individual operational approvals, remains unverified.
- Disturbance / variety regulated: conflicts about ultimate pod purpose, legitimate authority and constitution of the shared organization.
- Decisive decision or feedback right: operator owns pod configuration, membership and grants; operational action approvals exist, but no identity-level issue → authoritative decision → returned governing operation chain was reconstructed.
- Decision owner: the human pod creator/operator owns configuration and grants; ownership of a function-specific S5 loop has not been established.
- Supporting / enforcement mechanisms: membership roles, pod configuration, tool grants, approval/decision requests and their enforcement.
- Closure path: tool-level and connector-grant approvals can change allowed actions, but they do not necessarily settle the ultimate identity/policy question of the pod.
- Boundary reachability: supported self-hosted UI, pod and service-grant routes were inspected; no identity-level S5 mode is asserted.
- Why this is / is not agent-owned: human-administered permissions are not automatically S5=P; no model-owned ultimate-identity authority demonstrated.
- Evidence: [grants.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/grants.ts); [decisionRequestService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/decisionRequestService.ts); [pods.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/routes/pods.ts); [roomGrantService.ts](https://github.com/Team-Commonly/commonly/blob/669889886a9436b8349e4e60e5197bab504909e8/backend/services/roomGrantService.ts).
- Basis: explicit + structural + unknown.
- Confidence: medium (in unresolved closure).
- Caveats: Inspected support mechanisms do not justify a confident positive state; uncertainty is not a universal absence claim.

- Identity / ultimate-policy issue: no evidence-backed dispute or revision of the pod's ultimate purpose or constitutional authority was reconstructed.
- Ultimate authority in each claimed mode: operator controls membership/grants/creation, but no positive S5 mode is claimed.
- Return-to-operation path: operational action approvals and grants return into tool access, but no demonstrated ultimate-policy decision/feedback loop.

## Distributed OSS parent arrangement

The contributors of the Commonly public repository do not form an operating metasystem for every self-hosted pod. A pod's writer/owner is a local human parent for S3 current task intervention, not automatically a legitimate S4/S5 authority for the OSS organization.

## Self-hosted and non-human modes

A self-hosted operator may use the native model loop with no continuously participating human and still run first-party S1 plus deterministic contention control. Human pod task-board writers supply the evidenced S3 parent mode. BYO model agents may use MCP/REST but their internal planning or safety checks are outside the credited first-party Native Tier-1 loop. A pod with one installed seat lacks the distinct-units S2 witness.

## Recursion

The focal pod is a workspace containing separate seat operational units; multiple pods, tenants, external channels and ecosystem/marketplace operator are distinct levels, not automatically subunits of this pod.

## Variety and escalation

First-party native tool guards restrict agent actions, message claims suppress duplicates and transfer a declined wake, task leases preserve accountable ownership, and human task-board writers revise current pod work. Human decision requests and grant policies provide operational escalation, not by themselves ultimate-policy closure.

## Evidence gaps

- S2=C depends on at least two first-party/compatible live seats and claim-enabled human wake; verify multi-seat CAS/handoff traces separately from example fixtures.
- S3=P is bounded to a human pod writer's visible task portfolio and operational write/notification return, not generic service admin capability; test an actual operator-driven reassignment return.
- Inspect any first-party audit/challenger deployment and prospective capability-change workflow before promoting S3*/S4.
- Distinguish ultimate pod policy/identity decisions from grants, seat authorizations and individual tool approvals before claiming S5.
- No full end-to-end provider-backed run was executed for this repository review. Unresolved `?` states are intentionally not `—`.
