---
harness_id: openrecoding
project_name: OpenRecoding
repository: https://github.com/jiaxz/open-recoding
review_ref: 4d726930706bd24ff1f99803cf8e1678cae8c61b
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenRecoding

## Review boundary

- System in focus: One OpenRecoding Session, its live Master and worker agents, first-party coordination system, execution pools and operator control surfaces.
- Purpose and identity: Carry out a coding or investigation project through a team of persistent model-tool actors with shared workspace and controlled compute.
- Relevant environment: A Linux host, configured model endpoint, one Session workspace and optional remote compute nodes. An operator supplies the objective, runtime settings and initial scope.
- Standard-distribution boundary: Web/CLI Session entrypoints instantiate the first-party Session, multi-agent System, Master and model-tool workers. Peer messages, lifecycle commands, workspace tools and execution ownership belong to this distribution. Inference, remote hosts and an external coding agent used for installation or maintenance are external.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/README.md), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md), [`core/session/session.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/session.py), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py), [`core/multiagent/worker.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/worker.py), [`core/multiagent/loop.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/loop.py), [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py), [`core/tools/workspace_files.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/tools/workspace_files.py), [`apps/web/recoding_web/server.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/apps/web/recoding_web/server.py)
- Adjacent first-party surfaces excluded from ownership: External maintenance coding agent, README self-modification scenario, browser tests, offline UI examples and the provider's inference service.
- First-party operating / deployment modes considered: Linux Web, CLI/TUI and embedded Session, with multiple persistent agent loops, host/sandbox and optional remote execution resources. Web operator can tune the live Session sub-agent cap.
- Recursion level: One Session is the team-level system. Persistent task agents with separate contexts are S1 units. Master may perform S1 work itself and holds team-level coordination and control rights.
- Reviewed revision: `4d726930706bd24ff1f99803cf8e1678cae8c61b`, [intake #3059](https://github.com/opensiro/vsm-harness-index/issues/3059) and [controller #3060](https://github.com/opensiro/vsm-harness-index/issues/3060).
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Session binds execution resources and constructs a System with a Master. Each worker runs a first-party continuous model-tool loop. The loop drains inbound mail before model calls, executes returned tools, and feeds results to the next request. A worker can sleep and wake on mail while preserving its independent context.
The coordinator records lifecycles and mail. Master can inspect the live roster, correspondence and process pool, direct work, and create, stop, resume or reassign workers. Workspace editing detects stale revisions and reports conflicts to the caller. Team instructions assign file ownership and call for conflict recovery and evidence-backed intervention.

## Operational model

Workers select and perform substantive coding, analysis and verification tasks and report results over mailbox tools. Peers and Master can resolve contention using task and file ownership messages. Master sees team-wide conditions and can change live commitments. A human can separately set a live session-wide concurrency constraint. Master can inspect actual worker artifacts and host failure information in response to doubts about ordinary reports.

## S1 — Operations

- State: A
- Function: Complete coding and investigation work with persistent model-tool actors.
- Disturbance / variety regulated: Ambiguous tasks, partial changes, tool errors, incoming peer reports and interruptions.
- Decisive decision or feedback right: Choose work methods and subsequent tool actions from workspace evidence and communications.
- Decision owner: Each bound model actor owns its task decisions. Master and peers may set work assignments and constraints.
- Supporting / enforcement mechanisms: Per-agent context and model binding, continuous loop, mailbox, workspace tools, execution pools and persisted state.
- Closure path: Task or peer message → worker model choice → tool observation → revised action and explicit result report or idle continuation.
- Boundary reachability: Session starts Master; Master can create an independently running child and deliver its task. The child has its own loop, context, model requests and workspace tools.
- Why this is / is not agent-owned: The workers choose and revise their own substantive operations. Runtime transports tools and messages.
- Evidence: [`core/session/session.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/session.py), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py), [`core/multiagent/worker.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/worker.py), [`core/multiagent/loop.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/loop.py#L154-L232), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

## S2 — Coordination

- State: A
- Function: Attenuate interfering work between independently active agents in a shared workspace and execution pool.
- Disturbance / variety regulated: Duplicate assignments, competing writes or a wait on another action queued behind the same persistent process.
- Decisive decision or feedback right: Choose file/work ownership, agree on boundaries or change execution routing after conflicts or peer feedback.
- Decision owner: Master allocates initial file/work scope and adjusts it. Peers can negotiate local changes directly in their model loops.
- Supporting / enforcement mechanisms: Role instructions, persistent sender/recipient mail, inbox wake and drain, shared work evidence and revision-aware edit receipts.
- Closure path: Shared-file conflict or anticipated overlap → affected worker observes the conflict and exchanges ownership or dependency information with peers/Master → revised assignments or files → later worker action reflects the decision.
- Boundary reachability: Default multi-agent role prompts explicitly direct coordination of competing writes and process bottlenecks. Tools route peer communications and reject stale file revisions before writes.
- Why this is / is not agent-owned: Removing the agents leaves conflict detection and message delivery, while the choice of which worker backs off, changes file scope or redirects work requires their discretion.
- Distinct S1 units: Persistent worker loops with separate model contexts, tool use and task ownership, operating concurrently in one Session.
- Inter-S1 disturbance: Workers can target the same file using stale revisions or queue incompatible work on one shared process.
- Attenuating coordination relation: Role-specific instructions direct ownership negotiation and duplicate-work avoidance. Conflict receipts and direct messages let peers and Master select a different work or file allocation.
- Feedback into subsequent S1 behaviour: Mail enters the affected model's next call. A revised file assignment, refreshed file revision or new process allocation changes its next tool action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped role instructions, conflict receipts and writable shared workspace bind mail to concrete shared-resource interference and subsequent worker behavior.
- Evidence: [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L268-L283), [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L319-L347), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L389-L433), [`core/tools/workspace_files.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/tools/workspace_files.py#L199-L213), [`core/session/session.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/session.py#L54-L70), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: The reviewed edit tool and coordination path support this response. Effectiveness and consistency across arbitrary raw tools were not measured.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the Session's current operating commitments and available agent capacity.
- Disturbance / variety regulated: Stalled and failed work, resource bottlenecks, duplicated work and changing capacity.
- Decisive decision or feedback right: Decide whether to stop, resume, reassign or transfer current work and process resources. Separately, set a live Session-wide agent capacity constraint.
- Decision owner: Master's model owns discretionary team and process intervention. The human operator owns the live cap decision in the parent path.
- Supporting / enforcement mechanisms: Global correspondence, roster, pool status, Master-only lifecycle rights, Web operator controls and persisted capacity policy.
- Closure path: Master samples current conditions, decides an intervention and invokes the owning tool or sends revised assignments. In the parent path the user updates the cap, the coordinator persists and enforces it, then notifies Master to revise its plan.
- Boundary reachability: First-party team prompt and System bind Master tools. Web Session control accepts operator cap changes during operation and calls System.set_limit.
- Why this is / is not agent-owned: Master does more than request a preset timeout. The operator owns cap changes separately, with Master operating inside that returned constraint.
- Whole-system current view: Master can access Session agent statuses and cap, correspondence and owners/executions across the shared process pool. The Web operator can inspect the Session-wide roster, occupancy, resource and activity displays.
- Current-control decision scope: Master may change assignments, stop/resume agents and preserve or reassign owned process resources. The parent can change the allowed count of concurrently active workers across the whole Session.
- Evidence: [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L285-L339), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L336-L356), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L389-L433), [`apps/web/recoding_web/host.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/apps/web/recoding_web/host.py#L162-L171), [`docs/guide.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/guide.md), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: The parent cap constrains new creation/resume and does not immediately stop an existing worker. Master selects interventions within the current settings.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Master model | Worker or process failure, bottleneck, useful resource at risk or redundant work | Inspect roster, pool and progress, then change commitments through stop/resume, reassignment or resource transfer and collect follow-up results. | [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L285-L339), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L389-L433) |
| Parent (`P`) | Human Session operator | Live Session capacity or resource pressure warrants changing the worker cap | Set the new whole-Session constraint in the Web interface. It is persisted, changes create/resume eligibility, and is delivered to Master with the occupancy and adjustment instruction. | [`apps/web/recoding_web/server.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/apps/web/recoding_web/server.py#L547-L553), [`apps/web/recoding_web/host.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/apps/web/recoding_web/host.py#L162-L171), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L336-L356) |

## S3* — Complementary audit

- State: A
- Function: Inspect worker output and actual failure evidence to challenge an uncertain operational report before choosing corrective action.
- Disturbance / variety regulated: Incomplete or unreliable worker reports, missing artifacts and failed work that left partial files.
- Decisive decision or feedback right: Choose whether and what to inspect independently of the worker's own message, and judge the actual state of its output.
- Decision owner: Master acts as the separate verifier of subordinate claims or partial outputs. Master also owns the subsequent control decision.
- Supporting / enforcement mechanisms: Dedicated Master role instructions to validate received and partial artifacts, workspace inspection, host failure and location records, distinct context and Master control tools.
- Closure path: Worker report or failure → Master inspects shared artifact and host evidence directly → Master judges completion or defect → resumes, reassigns or explicitly stops the worker and feeds back instructions.
- Boundary reachability: Session binds Master prompt and workspace inspection tools. The prompt instructs Master to verify artifacts and, on failure, read actual failure/location and validate partial artifacts.
- Why this is / is not agent-owned: Master can obtain artifact and host evidence without relying on a worker's self-report. It has an independent context for the audit judgment.
- Claim being audited: Whether a reported worker result is supported by the actual artifact or a failed worker left usable work.
- Ordinary reporting path: Workers explicitly send progress, result and blocker messages through the normal mailbox/reporting path.
- Complementary access path: Master directly reads the artifact or host failure/location and validates the partial work in the shared Session workspace.
- Independence boundary: Separate Master model invocation and context relative to the worker under review. Shared workspace and possibly provider; this does not establish independence for Master's own work.
- Who acts on findings: Master chooses whether to correct, resume, reassign or stop, then communicates and applies the choice through first-party controls.
- Evidence: [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L319-L339), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py#L389-L433), [`core/session/session.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/session.py#L54-L70), [`core/tools/workspace_files.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/tools/workspace_files.py), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for distinct access and returned control options; medium for audit selection and effectiveness in operation.
- Caveats: Optional model-directed inspection of subordinate work. No mandatory audit pass, independent review of Master itself, or run-level effectiveness is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then capability adaptation loop is established within the Session.
- Disturbance / variety regulated: Tool availability, runtime limits, package changes and immediate task research needs.
- Decisive decision or feedback right: Anticipate future external changes, select a capability adaptation and return it into present organization.
- Decision owner: Workers and Master decide current-task setup. External host operator or coding agent performs maintenance.
- Supporting / enforcement mechanisms: Session packages, context compaction, model configuration, tool inventory and host maintenance utilities.
- Closure path: Current-task needs can trigger installing tools or changing local context. An external maintenance action can modify a future deployment.
- Boundary reachability: Current work and package operations are supported. The documented host maintenance actor is outside the Session boundary.
- Why this is / is not agent-owned: Current task research, compaction and dependency setup serve production. The first-party Session does not bind a future-environment sensing and capability governance return.
- Evidence: [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py#L35-L73), [`core/session/compaction.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/compaction.py), [`core/session/package_inventory.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/package_inventory.py), [`docs/host-maintenance.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/host-maintenance.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Runtime research and package instructions, process/resource planning, compaction and host maintenance routes.
- Plausible first-party paths checked: Durable package setup, artifact reuse and external agent-assisted improvement.
- Why no material first-party path remains: The paths serve present tasks or require external host work. No first-party prospective decision owner and returned change to future Session capability is assembled.

## S5 — Policy and identity

- State: —
- Function: No identity or ultimate-policy arbitration is established for the assessed Session.
- Disturbance / variety regulated: Requests to change task scope, worker permissions, runtime resource constraints or external behavior.
- Decisive decision or feedback right: Decide a matter that changes the Session's ultimate mandate and return binding policy into operation.
- Decision owner: Human sets purpose and authority in the parent environment. Master manages work and resources inside that scope.
- Supporting / enforcement mechanisms: Master/sub capability separation, role prompt, task messages, settings and operator controls.
- Closure path: Authority limits and task instructions are enforced or interpreted by the current Session. This handles current operations and task direction.
- Boundary reachability: The user can message Master and control settings. Master can create, rename and stop workers within the Session.
- Why this is / is not agent-owned: Role identities and discretionary current-control rights do not themselves supply ultimate policy and identity closure.
- Evidence: [`core/multiagent/prompts.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/prompts.py), [`core/multiagent/tools.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/tools.py), [`core/multiagent/system.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/multiagent/system.py), [`core/session/settings.py`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/core/session/settings.py), [`docs/sub-agents.md`](https://github.com/jiaxz/open-recoding/blob/4d726930706bd24ff1f99803cf8e1678cae8c61b/docs/sub-agents.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Role prompts, actor permissions, user input, live settings and Session lifecycle controls.
- Plausible first-party paths checked: Human task and resource directions, Master arbitration between workers and named role configuration.
- Why no material first-party path remains: The supported routes govern task goals, current resource limits and execution. They do not bind a first-party identity-level policy issue, decision and policy return.

## Recursion

One Session is the team-level system. Persistent task agents with separate contexts are S1 units. Master may perform S1 work itself and holds team-level coordination and control rights.

## Variety and escalation

Agent inboxes and persistent context absorb asynchronous work, failure and restart. File revision checks and ownership discussion attenuate competing writes. The current cap, role authorization and process lifecycle constrain team operations.

## Evidence gaps

Pinned source only. No provider, host/sandbox, remote node or live multi-agent run was executed. Agent judgment quality and whether optional coordination/audit paths are selected in a particular run remain unmeasured.
