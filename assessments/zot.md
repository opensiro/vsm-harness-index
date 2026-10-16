---
harness_id: zot
project_name: Zot
repository: https://github.com/patriceckhart/zot
review_ref: 2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zot

## Review boundary

- System in focus: Zot's first-party Go terminal coding-agent runtime at `2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3`, with optional locally launched `/swarm` child processes, not the OSS project governance or provider infrastructure.
- Purpose and identity: let a model-directed agent work with repository files/shell, optionally supervising model-directed subagents in the same workspace.
- Relevant environment: filesystem, shell, user task, external model APIs/local model endpoints, terminal UI, session state and optional child-process status.
- Standard-distribution boundary: first-party Go binary (`cmd/zot`, `packages/core`, `packages/agent`, `packages/agent/swarm`, `packages/agent/modes`, `packages/agent/tools`) in TUI, print, JSON and optional enabled swarm modes.
- Credited operating / distribution surfaces: model-directed `core.Agent.runLoop/oneTurn/executeTools`, local tools, primary session, first-party spawn/child subprocess loop, dashboard and operator current-control commands, opt-in auto-swarm task spawning and return.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI, release actions, vendor auth implementations, docs/demos, downloaded Zotfiles and optional user-installed extensions/skills. External model providers and third-party extensions do not donate organizational ownership.
- First-party operating / deployment modes considered: normal TUI/print/JSON local model-to-tool loop, optional `/swarm` manual child sessions, opt-in `auto-swarm` registered spawn tool, and operator swarm dashboard management. No provider-backed live task was executed for this source inspection.
- Recursion level: one owner-operated terminal coding workspace and, when enabled, its nested swarm of separate first-party Zot subprocess S1 actors sharing the workspace. S3 parent control is only supported in the declared operator-supervised swarm mode, not every single-agent turn.
- Reviewed revision: `2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3` from frozen intake #379.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The README explicitly advertises a Go model/tool coding-agent loop with first-party file tools, many external inference providers, three ordinary run modes and opt-in `/swarm`. Source establishes the S1 mechanism: `core.Agent.runLoop` requests the next response with `oneTurn`, invokes `executeTools`, appends tool result messages and iterates until stopped, while `packages/agent` wires CLI/interactive/runtime setup ([README.md](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/README.md), [packages/core/agent.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/core/agent.go), [packages/agent/cli.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/cli.go)). External inference services do not provide an imported agent workflow.

When `/swarm` is enabled, first-party `Swarm.SpawnReq` creates local Zot child processes with dedicated event logs, inbox sockets and persistent child session records ([packages/agent/swarm/swarm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/swarm.go), [packages/agent/swarm/runner.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/runner.go), [packages/agent/swarm_agent.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm_agent.go)). Children run their own local model loops and edit the **same working directory**, explicitly without per-agent worktrees. The dashboard shows each worker's state and permits parent-operator `new/send/resume/kill/remove` actions; these act on live subprocesses, not solely on transcript display ([packages/agent/modes/swarm_dialog.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/swarm_dialog.go), [packages/agent/swarm/swarm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/swarm.go)). With auto-swarm opted in, the main coding model can call `swarm_spawn` to launch parallel tasks and receives a terminal batch status + child text injected as an observation before a later model turn ([packages/agent/tools/swarm_spawn.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/tools/swarm_spawn.go), [packages/agent/modes/interactive.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/interactive.go)). This is delegation/return, not automatically S2 conflict attenuation or autonomous whole-current S3.

Session save/fork/import, compaction, standing instructions, user-installed skills and extension hooks preserve or customize a coding task; they do not by themselves demonstrate complementary audit or future/environmental organizational adaptation.

## Operational model

A user launches Zot and asks to inspect or modify a repository. The first-party agent calls an external model provider, receives tool selections, dispatches local tools and returns observations for the model's next choice. The main user can start independent background Zot children through `/swarm`, inspect and steer them; optionally, a model may spawn them autonomously when auto-swarm is enabled. All child edits share the same workspace by default, and the implementation does not establish a first-party collision-negotiation/attenuation owner across child writers. The parent's model auto-swarm update composes completed child summaries, but is prompted to summarize rather than change full current commitments. A human in the swarm dashboard can observe the whole worker population and explicitly spawn, message, stop or restart worker commitments, closing a narrower parent S3 path for that optional mode.

## S1 — Operations

- State: A
- Function: carry out open-ended coding and inspection by choosing local file/tool/shell actions with model-to-result feedback.
- Disturbance / variety regulated: unknown repository state, edit/test consequences, command failures, multiple file/tool observations.
- Decisive decision or feedback right: choose the next tool and coding action based on the current messages and results.
- Decision owner: first-party Zot `core.Agent` model-directed actor; external model endpoint supplies inference only.
- Supporting / enforcement mechanisms: per-agent model request, registered tools, native tool executor, first-party session state and credentials/provider adapters.
- Closure path: task→`oneTurn` model tool calls→`executeTools` results appended to transcript→next `runLoop` iteration or terminal answer.
- Boundary reachability: `core.Agent.runLoop` is the shipped binary's ordinary interaction loop, and optional swarm child processes invoke their own first-party Zot agent loop, not an imported coding-agent runtime.
- Why this is / is not agent-owned: meaningful next task actions are model-directed rather than a fixed scripted series; runtime and human constraints bound these choices.
- Evidence: [packages/core/agent.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/core/agent.go), [packages/agent/swarm_agent.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm_agent.go), [packages/agent/modes/print.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/print.go).
- Basis: explicit native source code.
- Confidence: high for first-party path and feedback; no live model execution performed.
- Caveats: performance and tool grants depend on model provider and operator configuration.

## S2 — Coordination

- State: —
- Function: no material first-party coordination relation that diagnoses and attenuates concrete interference among separate swarm S1 workers.
- Disturbance / variety regulated: swarm children share a writable workspace and may collide on edits; inter-worker write interference is a plausible disturbance.
- Decisive decision or feedback right: adjudicate competing writes/task claims, return a collision finding or negotiated rescope to affected workers. No such native relation is established.
- Decision owner: swarm management spawns independent child loops; parent can manually message children but no native inter-worker write-claim controller is evidenced.
- Supporting / enforcement mechanisms: child status/inbox and shared workspace; these are generic routing/status, not a conflict lock/arbiter.
- Closure path: child completion returns a summary to parent, not a conflict-specific arbitration-and-correction cycle among worker S1 units.
- Why this is / is not agent-owned: independent parallel work and communication do not establish S2 without a returned response to specific inter-S1 disturbance. README explicitly cautions that children edit the same files without isolation.
- Evidence: [README.md](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/README.md), [packages/agent/swarm/swarm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/swarm.go), [packages/agent/modes/interactive.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/interactive.go), [packages/agent/tools/swarm_spawn.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/tools/swarm_spawn.go).
- Basis: bounded negative source inspection.
- Confidence: medium-high, at default shared-workspace swarm boundary.
- Caveats: user-created external Git worktrees might attenuate conflicts but cannot be credited as shipped first-party automatic S2.

### Absence scope

- Surfaces inspected: core coding loop, child subprocess runner, swarm supervisor, inbox/status interfaces, auto-swarm completion watcher and documented shared workspace semantics.
- Plausible first-party paths checked: auto-swarm batch completion, child inbox, parent manual messages and shared-file work model.
- Why no material first-party path remains: these only route tasks/status/results and change subprocess lifetimes; no concrete native collision detection, negotiated competing worker correction or feedback preventing shared-write conflict.

## S3 — Inside-and-now control

- State: P
- Function: parent-operator whole-swarm current supervision of worker commitments and allocation while a coding workspace is active.
- Disturbance / variety regulated: stale/failed/background child activity, task assignment and progress across multiple running Zot child agents.
- Decisive decision or feedback right: view the swarm worker population and make actual current commitments by spawning another worker, redirecting work with a message, canceling/terminating work, or resuming a stopped worker.
- Decision owner: human terminal operator through `/swarm` dashboard; the coding model's optional spawn tool is ordinary task delegation and does not prove a distinct autonomous S3 supervisor.
- Supporting / enforcement mechanisms: swarm SnapshotAll/current status, per-agent subprocess and inbox, session-scoped dashboard, `SpawnReq`, `Stop`, `SendInput`, `Resume` and child persistent state.
- Closure path: whole-swarm dashboard status/activity view → operator's current worker assignment/intervention → first-party process spawn/send/stop/resume → live child run/inbox changes → updated statuses and outputs.
- Boundary reachability: installed `/swarm` UI is a shipped optional interactive feature controlling first-party child Zot processes, rather than an external management application or developer-only test.
- Why this is / is not agent-owned: decisive group-level current control belongs to the parent operator, hence `P`; auto-swarm alone is insufficient for autonomous S3.
- Evidence: [README.md](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/README.md), [packages/agent/swarm/swarm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/swarm.go), [packages/agent/modes/swarm_dialog.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/swarm_dialog.go), [packages/agent/modes/interactive.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/interactive.go).
- Whole-system current view: session-scoped swarm dashboard shows each child state, recent activity, error, task and lifecycle.
- Current-control decision scope: operator changes which subordinate agents are running/paused, their task messages and active commitments from that group view.
- Basis: first-party parent current supervision path.
- Confidence: moderate for explicitly enabled operator swarm mode.
- Caveats: S3 is **not** credited merely to auto-swarm summary or one ordinary coding session; no S3=A/C independent actor mode is established.

## S3* — Complementary audit

- State: —
- Function: no independently owned complementary audit/verification function with a separate findings return and corrective disposition is shipped at this session/swarm boundary.
- Disturbance / variety regulated: erroneous outputs, incomplete work or unverified code changes may occur, but review ability through ordinary model tools or optional user-installed skills is not S3*.
- Decisive decision or feedback right: independently inspect S1 claims/evidence and return findings into accountable current control; such a first-party distinct review path was not found.
- Decision owner: one main coding model or manually spawned subagents under operator direction; no designated native auditor role/verdict authority mandatory for a specified supported mode.
- Supporting / enforcement mechanisms: generic tool results, session logs, statuses and auto-swarm summary, without binding independent claim audit.
- Closure path: generic child task report→parent summary only. No first-party independent audit claim→source access→finding→correction/stop gate beyond ordinary work completion.
- Why this is / is not agent-owned: built-in children and a user-created reviewer prompt are generic S1/parent delegation, and optional extensions are not first-party audit owners.
- Evidence: [packages/core/agent.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/core/agent.go), [packages/agent/swarm/swarm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/swarm/swarm.go), [packages/agent/modes/interactive.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/modes/interactive.go), [packages/agent/tools/swarm_spawn.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/tools/swarm_spawn.go).
- Basis: bounded negative.
- Confidence: moderate, at inspected first-party standard distribution.
- Caveats: user may spawn reviewer-like child tasks, but this is an external constructed audit; optional third-party extensions not credited.

### Absence scope

- Surfaces inspected: main agent, native swarm manager, spawn/result transport, UI status/auto-swarm watcher, documented installed modes and extensions.
- Plausible first-party paths checked: model checking its own work, automatic child summaries, independent child process with optional reviewer prompt and user-installed code-review skills.
- Why no material first-party path remains: none establishes first-party specific complementary audit access, independent verdict authority and closed binding findings return rather than generic task completion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/environment monitoring and owned prospective capability change loop at installed session boundary.
- Disturbance / variety regulated: context pressure and recurring user tasks are handled by compaction/persistent instructions; not a distinct adaptive external-intelligence remit.
- Decisive decision or feedback right: select a future-facing change to the system's capability from environmental evidence and return it to present operation; absent.
- Decision owner: operator can modify settings/skills, and main model can re-plan current tasks; neither qualifies without outside-and-then strategy closure.
- Supporting / enforcement mechanisms: session compaction, per-project AGENTS.md, skills, extension loader, model selection, persistence.
- Closure path: ongoing task context restored or compacted; no evidence-first adaptation option→binding prospective system change.
- Why this is / is not agent-owned: memory, model switching and user skill installation are configuration/continuity mechanisms rather than S4 intelligence adaptation.
- Evidence: [packages/core/compact.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/core/compact.go), [packages/agent/skill_pins.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/skill_pins.go), [packages/agent/extcmd.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/extcmd.go), [packages/agent/settings_store.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/settings_store.go).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: external operator workflows can evolve installed Zot, outside credited first-party S4.

### Absence scope

- Surfaces inspected: state recovery and compaction, instruction files, built-in skills and optional extensions, provider routing and swarm modes.
- Plausible first-party paths checked: automatic context compression, user-saved skills, extension updates, repetitive task observations and agent switching.
- Why no material first-party path remains: inspected paths support present coding or static installation; no source-identified outside/future information→adaptive choice→changed capability return exists.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct legitimate organizational identity/ultimate-policy decision loop at this local coding/swam boundary.
- Disturbance / variety regulated: tool approvals and provider credentials protect local execution, without adjudicating ultimate organizational purpose or policy.
- Decisive decision or feedback right: issue a binding ultimate identity/policy interpretation and return it to current/swarm operations; not evidenced.
- Decision owner: human configures permissions, credentials and agent identity; runtime applies configured access bounds.
- Supporting / enforcement mechanisms: agent options, user tool confirmation, jail settings and extension policies.
- Closure path: permission allows/denies a tool and config changes future tool availability, but neither establishes first-party rightful S5 identity authority.
- Why this is / is not agent-owned: parent S3 operational control over child sessions does not automatically amount to ultimate organizational policy and purpose adjudication.
- Evidence: [packages/agent/config.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/config.go), [packages/core/confirm.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/core/confirm.go), [packages/agent/cli.go](https://github.com/patriceckhart/zot/blob/2a19df15ba8278dd6a92240ab6c2ae267c3cf6c3/packages/agent/cli.go).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: external user or organization may provide a parent S5, not credited at this installed binary recursion.

### Absence scope

- Surfaces inspected: agent config, CLI modes, tool confirmation and jail controls, persistent standing instructions, swarm authorization and repository governance.
- Plausible first-party paths checked: tool approval, default jail, spawned child credentials and operator parent control.
- Why no material first-party path remains: no distinct policy-purpose/identity governance function with legitimate rights and authoritative return beyond local task permissions and S3 operator worker control.

## Evidence gaps

- No live model execution, producer audit or independent multi-agent collision test. Paths and documented installed modes are source-confirmed, not a guarantee of performance or actual human use.
- Swarm child sessions share files without first-party collision arbitration: external worktrees are not credited, and multi-agent capacity is not equivalent to S2.
- Parent S3 applies to configured `/swarm` dashboard, not bare coding chat. The model's auto-swarm spawn and aggregate summary do not establish a distinct autonomous current-regulation function.
- No optional third-party skill/extension was assumed installed or authorized to donate metasystem control.

## Conclusion

At the pinned installed Go Zot boundary, one or many first-party model-directed coding loops supply S1=A. The shipped shared-workspace swarm has no distinct evidenced conflict regulation S2, while its **operator-driven whole-swarm dashboard** gives a bounded parent S3=P mode. Generic child outputs are not separate S3* audit, local memory/skills are not S4 intelligence and tool permission is not S5 identity governance. Final proposed vector: **A / — / P / — / — / —**, strictly conditional on the operator-managed swarm for S3.
