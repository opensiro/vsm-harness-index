---
harness_id: polter
project_name: Polter
repository: https://github.com/Lugia123/polter
review_ref: c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Polter

## Review boundary

- System in focus: a single self-hosted Polter terminal-group organization, including the first-party Ghostty-derived terminal host, authenticated per-terminal MCP control plane, configured autonomous CLI agent sessions, designated supervisor agent with the shipped supervising Skill, durable group/task state and screen-quiescence feedback.
- Purpose and identity: sustain and coordinate concurrent independently operating coding-agent terminals by designating one active supervisor to observe status, assign/revise ongoing tasks, steer stalled workers and report progress without operator micromanagement.
- Relevant environment: user-supplied work goals, terminal/shell/file state, installed Claude Code or other compatible agent CLIs, user keyboard, local project files and agent-derived outcomes; developer/host OS/terminal dependencies.
- Standard-distribution boundary: Polter's shipped terminal host, `src/poltergeist/` server/bus/task/group/sampler code and its first-party editable `supervising` Skill, plus included CLI provisioning plugin that registers Polter MCP tools with the chosen external CLI. A supported live assembled mode requires at least one independently running external agent CLI. External Claude/Codex model reasoning, hidden tools, memory, safety policies and internal planner/verifier are not borrowed for organizational credit.
- Credited operating / distribution surfaces: supported user-started CLI in Polter terminal, supervisor designation, registered MCP tools (`me`, group, task, terminal and notice), terminal content monitoring and text steering, group/task persistent records, user-held protected terminal controls.
- Adjacent first-party surfaces excluded from ownership: upstream Ghostty renderer/PTY features absent their Polter organizational wiring; product/development tests, repository CI, unshipped future designs, private CLI internals, independent OSS maintainer organization.
- First-party operating / deployment modes considered: one/multiple independent CLI-backed coding agent terminals, designated Claude Code supervisor under shipped Skill, registered MCP tool server, terminal monitoring enabled as needed, persistent group/task, human operator holds and shields, optional CLI provisioning.
- Recursion level: one Polter-managed local terminal group with a designated supervisor and distinct autonomous worker terminals as S1 operational units; the developer's entire desktop, other users' Polter installations, and repository maintainers are different recursions.
- Reviewed revision: `c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Polter packages terminal sessions and the MCP tool gateway around host-run CLI coding agents. The README explicitly requires an installed agent CLI, launches it inside a terminal and marks one running session as supervisor. `agent_cli.zig` discovers/provisions available CLIs and launch configurations; `Server.zig` authenticates a caller's terminal identity using issued/revocable tokens rather than an agent's claimed name. `rpc.zig` mediates `terminal_read`, `terminal_send`, task/group, supervisory and notice operations; it checks marks and target reachability. A screen sampler measures quiescence without decoding hidden CLI reasoning. Transcripts/group messages and the task panel are persisted, and user-held locks/shields forbid certain agent actions.

The shipped supervisor Skill explicitly directs the designated agent to reconstruct current state from `me`, `group_list/read`, `task_list`, `terminal_list`, and `notices`; to reconcile stale/blocked work; to create/assign tasks and type actionable instructions into target terminals; and to inspect screens rather than rely on the supervisor's own prior memory. The first-party runtime *wires* those tools to actual persistent group and terminal state. The supervisor's model makes situational choices through the shipped Skill/tool pathway; the model engine itself remains an external dependency.

- Assembled operations: [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md); [agent_cli.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/agent_cli.zig); [Server.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Server.zig); [adapter.py](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/plugins/claude-code/adapter.py).
- First-party group/task/controller: [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig); [Tasks.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Tasks.zig); [TaskLog.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/TaskLog.zig); [Bus.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Bus.zig); [Chat.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Chat.zig); [supervising.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/supervising.md).
- Sensor/enforcement: [Sampler.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Sampler.zig); [actions.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/actions.zig); [operating-a-terminal.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/operating-a-terminal.md); [Transcript.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Transcript.zig).

## Operational model

S1 work cells are separately running CLI agent processes in Polter-hosted terminals, performing real coding/research work using their own model/tool loops and host workspace. Polter does not implement Claude's internal reasoning loop but includes the supported autonomous processes as operational actors in its *assembled standard operating boundary*; removing those actors leaves a terminal/sensor/controller with no agentic task work. A designated **supervisor is itself an autonomous agent actor** supplied by the hosted CLI, but its S3-specific organizational inputs and return actions are explicitly surfaced/wired by Polter's own shipping supervisor Skill/MCP gateway. Attribution is to this first-party assembled control configuration, not any undocumented external CLI private manager.

The group task panel holds a single terminal owner for each open item and rejects other workers' progress mutation; that constructor-level conflict rule contributes to S2 without establishing an autonomous task-collision arbiter. The supervisor reads aggregate group/task/terminal state, decides to intervene, reassign or continue monitoring, and returns directives to workers via `terminal_send`/task commands. User locks/shields constrain operations but do not establish S5 ultimate-policy closure.

## S1 — Operations

- State: A
- Function: execute user-assigned coding and other task transformations through independently running terminal-based autonomous agent actors.
- Disturbance / variety regulated: evolving task instructions, filesystem/shell/tool output, compilation/test failures and other local environmental information encountered during worker task execution.
- Decisive decision or feedback right: choose task-specific coding/shell actions and subsequent steps from local tool feedback.
- Decision owner: the hosted Claude Code/Codex-style autonomous worker agent in each Polter-managed terminal; internal provider decision procedure is *not* owned by Polter.
- Supporting / enforcement mechanisms: Ghostty-derived PTY, per-terminal token, provisioned MCP tools, CLI inventory/launch, captured screen output and transcripts, outbound text input.
- Closure path: operator or supervisor sends work to a Polter terminal → supported CLI agent autonomously works using its own model/tool loop → file/terminal results return to that terminal → agent adjusts its next local operation and reports outcomes into terminal/group/task channels.
- Boundary reachability: the README's Quick Start operates exactly through active Polter terminals and a live Claude Code CLI; first-party provisioning/launch and server token/tool wiring permit this normal assembled mode.
- Why this is / is not agent-owned: removing the autonomous CLI agent leaves only terminal control and observation; the latter cannot independently decide coding changes, while the external agent's *private* higher-level VSM systems remain outside the credited evidence.
- Evidence: [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md); [agent_cli.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/agent_cli.zig); [Server.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Server.zig); [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig).
- Basis: explicit + structural.
- Confidence: high for supported assembled CLI mode.
- Caveats: Polter has no independent model key/inference loop; the supported hosted model/tool worker is an essential third-party operational actor. This is not a claim of first-party implementation of Claude/Codex cognition.

## S2 — Coordination

- State: C
- Function: prevent competing worker terminals from overwriting the ownership and progress of a shared group task, stabilizing inter-S1 commitments.
- Disturbance / variety regulated: two distinct workers reporting/changing one task as their own, or a worker continuing to update a reassigned, closed or cancelled task.
- Decisive decision or feedback right: admit or refuse a task progress mutation based on actual assigned worker and task open state; supervisor/operator can assign or release an owner.
- Decision owner: first-party deterministic task ownership/enforcement checks, with owner selection supplied externally by supervisor/human rather than first-party autonomous interference-specific negotiation.
- Supporting / enforcement mechanisms: `Tasks.Task.owner`, `Tasks.assign`, `Tasks.setProgress` with `NotYours`/`NotOpen`, MCP `task_assign`/`task_progress`, persistent task/group records, result/error responses.
- Closure path: group task assigned to a named terminal → only that S1's progress call is accepted → a different S1 gets an explicit refusal → that worker's subsequent recorded progress cannot silently overwrite the owner's; on reassignment or cancellation, former owner's update is also refused.
- Boundary reachability: task tools are part of the standard Polter MCP surface; the shipped supervisor Skill uses them to manage tasks for live terminal IDs, not hypothetical example workers.
- Why this is / is not agent-owned: runtime checks know the owner but cannot independently judge how to resolve an inter-worker dispute; an external supervisor can choose an assignee, so the **first-party conflict-control seam** is constructor-class rather than an internally autonomous S2 actor.
- Distinct S1 units: at least two independently executing Claude/Codex agent CLI terminals in one group, each with its own agent task/environment and terminal identity.
- Inter-S1 disturbance: one worker might overwrite another worker's progress state or continue reporting on an item no longer assigned to it; the code explicitly rejects not-owned updates.
- Attenuating coordination relation: single-owner task state and `setProgress(by)` check against `task.owner`, with closed/cancelled-task rejection.
- Feedback into subsequent S1 behaviour: a denied progress action returns the distinct failure to the calling agent's MCP/tool response; task panel no longer reflects invalid cross-worker updates, permitting correct reassignment by supervisor.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: refusal is keyed to **cross-worker ownership contention** of one shared operating commitment, rather than mere group chat or task list existence.
- Evidence: [Tasks.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Tasks.zig); [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig); [supervising.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/supervising.md); [TaskLog.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/TaskLog.zig).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: this is a narrow shared-task integrity witness, not proof that concurrent file edits are sandboxed, Git conflicts automatically resolved, or worker priorities autonomously negotiated. Task assignee can be changed by a privileged actor; user locks impose separate hard constraints.

## S3 — Inside-and-now control

- State: A
- Function: regulate current shared group commitments, worker responsiveness and corrective intervention through a designated autonomous supervisor agent.
- Disturbance / variety regulated: stalled or quiescent workers, obsolete assignments after worker exit, blocked tasks, duplicated overnight work, false assumptions from supervisor's compacted context.
- Decisive decision or feedback right: choose whether a worker requires a nudge, should be reassigned, continue waiting, or have a newly allocated task, based on group-wide current evidence.
- Decision owner: **designated supervisor CLI agent** operating through first-party Polter Skill and MCP control surface, not the deterministic screen sampler; its model inference remains external.
- Supporting / enforcement mechanisms: whole-group `group_list/read`, task panel `task_list`, terminal inventory, `notices`, screen `terminal_read`, quiescence stamps, `task_assign/close`, `terminal_send`, `set_watch`, user-held/shielded constraints.
- Closure path: supervisor obtains full group/task/terminal current picture → assesses reports, blocked work and live screens → selects new assignment or intervention → first-party task/terminal tools persist/send it → target S1 changes current work or reports back for further supervisor decisions.
- Boundary reachability: README Quick Start marks an actual running CLI as supervisor, auto-prompts it to read the packaged supervising Skill, and the MCP server provides the specified tools with per-terminal authentication and role checks.
- Why this is / is not agent-owned: a sampler measuring unchanged text is an alarm source, not the decision owner. The live supervisor model must interpret the multi-terminal evidence and select intervention; removing it leaves sensors, task records and locks but no corresponding current-control judgment.
- Whole-system current view: shipped Skill requires reconstructing `group_list`/all `group_read`, each group's full `task_list`, `terminal_list`, and notices before work decisions; task and terminal membership is reconciled after restarts.
- Current-control decision scope: agent-selected worker/task assignments and reassignments, progress check and closure, intervention via target-terminal instructions, escalation to the user if evidence conflicts.
- Evidence: [supervising.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/supervising.md); [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig); [Tasks.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Tasks.zig); [Sampler.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Sampler.zig); [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md).
- Basis: explicit + structural.
- Confidence: medium-high for the supervised multi-worker mode.
- Caveats: the user's held/shielded terminal controls are hard operator constraints, not S3 decision ownership. This claim rests solely on supervisor decisions made *through Polter's first-party specific Skill/tool composition*, never on Claude's private built-in team/management abilities. A configuration without a live designated supervisor lacks this S3 witness.

## S3* — Complementary audit

- State: ?
- Function: independently challenge ordinary S1 reports with direct operational evidence and return corrective findings.
- Disturbance / variety regulated: false 'done' or 'blocked' status, misleading self-reporting and divergent real progress.
- Decisive decision or feedback right: a supervisor can read raw terminal text and task status, but separate independent *audit judgment* beyond ordinary supervision has not been established with enough specificity.
- Decision owner: unresolved; the supervisor has current-control authority and observational tools, but no distinct first-party independent reviewer or audit protocol was reconstructed.
- Supporting / enforcement mechanisms: `terminal_read`, transcripts, group status/progress messages and quiescence sampler.
- Closure path: raw terminal screen is an alternative access channel, but the inspected path does not independently prove a sporadic challenge to an operating claim followed by a distinct audit verdict and returned correction.
- Boundary reachability: screen access and group channels are shipped; positive audit semantics cannot be inferred from access alone.
- Why this is / is not agent-owned: reading another terminal is not necessarily a complementary independent audit; no hidden Claude self-review is credited.
- Claim being audited: reported worker progress/finished task faithfully reflects actual work.
- Ordinary reporting path: group messages, `task_progress` and worker final statements.
- Complementary access path: raw terminal screen and transcript, distinct from the group's report channel.
- Independence boundary: no clearly independent audit owner/methodology from the coordinating supervisor's ongoing observations.
- Who acts on findings: supervisor can intervene, but a separately identifiable audit decision/feedback loop is not established.
- Evidence: [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig); [supervising.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/supervising.md); [Transcript.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Transcript.zig); [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md).
- Basis: structural + unknown.
- Confidence: medium in the unresolved mapping.
- Caveats: not an absence claim; further targeted scrutiny of a shipped full audit loop could resolve this question.

## S4 — Outside-and-then intelligence

- State: ?
- Function: anticipate changes external to the current group and adapt future operating capability.
- Disturbance / variety regulated: future goals, shifting environment and deployment needs not yet reflected in current tasks.
- Decisive decision or feedback right: no evidenced prospective environmental option-selection/feedback right owned by Polter or designated supervisor.
- Decision owner: unresolved.
- Supporting / enforcement mechanisms: persistent transcripts, group log, Skill/prompt editing, screens/notices and restart reconciliation.
- Closure path: recovered state can inform subsequent task control, but history is not proof of external/prospective adaptation and capability-change return.
- Boundary reachability: persistent state and prompts ship; positive S4 actor is unverified.
- Why this is / is not agent-owned: current-progress recovery and future work scheduling are not S4 without external prospecting.
- External distinction: not established beyond ordinary task input.
- Future / prospective distinction: not established beyond overdue/blocked tasks.
- Adaptation option generated: not evidenced as first-party organizational choice.
- Path back into current capability / S3: no decisive capability-change return identified.
- Evidence: [supervising.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/skills/supervising.md); [GroupLog.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/GroupLog.zig); [Transcript.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Transcript.zig); [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md).
- Basis: structural + unknown.
- Confidence: medium in the insufficient finding.
- Caveats: `?` rather than `—` preserves uncertainty about qualified prospective configurations.

## S5 — Policy and identity

- State: ?
- Function: settle an ultimate-policy/identity issue for the whole terminal group at the declared recursion.
- Disturbance / variety regulated: changes to group's legitimate purpose and constitutive supervisory authority.
- Decisive decision or feedback right: user designates supervisor and establishes held/shielded constraints, but a first-party identity-level issue–authoritative decision–returned operation loop was not reconstructed.
- Decision owner: user has explicit local override/permission authority; no proven S5 function-specific owner.
- Supporting / enforcement mechanisms: terminal marks, MCP authorization, user-only held/shielded controls, supervisor designation, editable Skill, provisioning settings.
- Closure path: operator lock/shield decisions are enforced, yet ordinary safety and access control are not proof of ultimate-policy closure.
- Boundary reachability: supported user settings and tool authorization are shipped; policy identity closure remains unverified.
- Why this is / is not agent-owned: a supervisor subject to operator locks does not have ultimate group identity authority merely by holding tools.
- Identity / ultimate-policy issue: no independently evidenced change-of-purpose or legitimate-governance adjudication.
- Ultimate authority in each claimed mode: none claimed.
- Return-to-operation path: user restrictions return into tool permissions, not a proven identity-level decision loop.
- Evidence: [Bus.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/Bus.zig); [rpc.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/rpc.zig); [actions.zig](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/src/poltergeist/actions.zig); [README.md](https://github.com/Lugia123/polter/blob/c2fe7ed9233ce5e36cb8fd86f4d2d2530c57b771/README.md).
- Basis: structural + unknown.
- Confidence: medium in the unresolved mapping.
- Caveats: held/shielded are ordinary operational protective constraints; do not upgrade to `P` simply because the user may operate them.

## Distributed OSS parent arrangement

One local supervised group is not the Polter OSS contributor community. Multiple external agent CLI instances working for one user do not confer the governance of this open-source project on the assessed organization; no multi-contributor parent arrangement is credited.

## Self-hosted and non-human modes

Polter is offline/local-first and inherits host CLI subscriptions. A supervisor-mediated multi-worker configuration supplies an agent S3 mode through first-party tool/Skill wiring, but standalone user sessions without a designated supervisor have only their local operational model and deterministic support. Explicit user-held/shielded/permission controls constrain autonomous decisions, with no demonstrated separate first-party parent S3 mode.

## Recursion

The terminal group and its supervisor are the declared whole. Independently running worker CLIs are its local S1 cells; a terminal/PTY/process alone is not a viable nested system. Supervisor's coordination role is established by functional tool wiring, not by a literal `supervisor` label.

## Variety and escalation

Model-backed workers absorb local coding variety; first-party group/task state limits contradictory progress writes; the agent supervisor regulates current work via group and terminal observations plus assignments and nudges. Quiescence notices detect unchanged screens but make no semantic judgment. Protected terminal marks preserve user authority, and conflicting/incomplete evidence may escalate to the operator.

## Evidence gaps

- S2=C is based specifically on cross-worker shared task progress integrity; verify multi-agent tool refusal and returned behavior with a live target group, not generic group chat.
- S3=A rests on packaged supervisor Skill and genuine MCP actions, not unspecified Claude planning; end-to-end repeatability with actual supervisor and multiple workers remains unmeasured.
- Independent audit, prospective adaptation, and legitimate identity/ultimate-policy closure require further targeted review before changing S3*/S4/S5 `?`.
- No live multi-agent provider-backed execution was run as part of this repository/source assessment; code, packaged operating surfaces and explicit documented behavior are primary evidence.
