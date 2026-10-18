---
harness_id: gastown
project_name: Gas Town
repository: https://github.com/gastownhall/gastown
review_ref: 649b832b7672bc7a2dbef26f5983aba6198b819b
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Gas Town

## Review boundary

- System in focus: one first-party Gas Town workspace at pinned revision `649b832b7672bc7a2dbef26f5983aba6198b819b`, including its Mayor, Polecat, Witness, Refinery and Deacon role contracts, rigs, hooks, Beads/convoy state, merge queue, patrol molecules, lifecycle/escalation paths and `gt` control/runtime surfaces.
- Purpose and identity: operate a persistent multi-agent software-engineering workspace that dispatches autonomous coding work across isolated workers, coordinates integration, regulates current town/rig execution, monitors failures and independently gates completed branches before they land.
- Relevant environment: user/Overseer requests, project repositories and target branches, issue/dependency state, git/test results, model-agent runtimes, external GitHub/PR state where configured, resource/concurrency limits and failures across multiple rigs and workers.
- Standard-distribution boundary: first-party `gastownhall/gastown` code, embedded/default role templates and formulas, shipped `gt` commands, worktree/rig/merge-queue machinery and persisted Beads/Dolt coordination state. Claude or other configured model-agent hosts, repositories being modified, GitHub itself and the human Overseer are external actors unless a Gas Town first-party protocol closes a claimed organizational function through them.
- Credited operating / distribution surfaces: Mayor and Polecat agent sessions launched by Gas Town; Witness/Refinery/Deacon patrol agents; `gt sling`, hooks, convoys and dependency state; per-rig isolated worktrees; the Refinery merge queue and verification gate; town/rig status and escalation/mail paths; scheduler/capacity support where it constrains the same running organization.
- Adjacent first-party surfaces excluded from ownership: contributor/CI/release machinery for developing Gas Town itself; research/survey documents and Gas City/HOP design material not required by the pinned standard operating path; optional community PR workflows where they do not establish a stronger function than the canonical Refinery path; static configuration, logs and dashboards when they only support rather than own a decision right.
- First-party operating / deployment modes considered: normal town operation with one or more undocked rigs; Mayor-dispatched Polecats; automatic Witness/Refinery/Deacon patrols; canonical non-fork Refinery merge-queue flow; configured scheduler capacity limits as supporting machinery; human/Overseer interaction only where it is explicitly returned through Gas Town runtime state.
- Recursion level: one Gas Town workspace. Rigs are project-level operational groupings with their own workers, Witness and Refinery, but this assessment does not assume each rig independently closes a full viable recursion.
- Reviewed revision: `649b832b7672bc7a2dbef26f5983aba6198b819b`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Gas Town is a multi-agent workspace manager built around persistent organizational roles and externalized work state. Polecats are autonomous coding workers in isolated worktrees. The Mayor is a model-driven global coordinator across rigs. Each active rig has a Witness that monitors worker lifecycle and a Refinery that independently processes completed branches. A town-level Deacon runs recurring infrastructure/lifecycle patrols. Hooks, Beads/Dolt state, convoys, mail/nudges and molecules carry durable assignments and feedback between those actors.

The canonical coding flow is intentionally separated: Mayor dispatches an issue to a Polecat; the worker executes and submits completion; Witness processes lifecycle state and emits `MERGE_READY`; Refinery independently rebases the branch against the moving target, runs configured quality/test checks, decides conflict/failure handling and either lands the branch or reopens the source issue and returns failure through Witness. This separates production from integration and verification while keeping subsequent worker behavior coupled to returned findings.

Primary evidence:

- [`README.md`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/README.md) — shipped multi-agent workspace boundary, role inventory, scheduler/capacity support and standard operating concepts.
- [`internal/templates/roles/polecat.md.tmpl`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/templates/roles/polecat.md.tmpl) — autonomous worker contract, isolated worktree, hooked assignment and completion/merge-queue return path.
- [`internal/templates/roles/mayor.md.tmpl`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/templates/roles/mayor.md.tmpl) — global coordination, dispatch, cross-rig regulation, escalation handling and current strategic/integration decisions.
- [`internal/cmd/mayor.go`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/cmd/mayor.go) — shipped Mayor session/control surface and its role as the global coordinator between the Overseer and automated agents.
- [`internal/templates/roles/witness.md.tmpl`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/templates/roles/witness.md.tmpl) — per-rig worker monitoring, lifecycle intervention, escalation and the protocol path into Refinery.
- [`internal/templates/roles/refinery.md.tmpl`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/templates/roles/refinery.md.tmpl) — separate merge processor, agent-owned ordering/conflict decisions, sequential-rebase coordination and mandatory verification/failure-return gate.
- [`internal/templates/roles/deacon.md.tmpl`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/internal/templates/roles/deacon.md.tmpl) — town patrol/lifecycle monitoring, operational-rig health checks and escalation boundaries.
- [`docs/design/mail-protocol.md`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/design/mail-protocol.md) — `MERGE_READY`, `MERGED`, `MERGE_FAILED` and role-to-role feedback protocol.
- [`docs/design/scheduler.md`](https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/design/scheduler.md) — capacity-aware dispatch support and wake-up of rig agents.

## Operational model

The principal S1 units are autonomous Polecats executing separate software-engineering issues in isolated worktrees. Mayor chooses and dispatches work across the town, while Witness and Deacon provide current operational observation/lifecycle feedback. Refinery is a distinct model-driven integration agent: its role explicitly states that merge order, conflict disposition and failure classification are agent decisions rather than decisions made by Go code.

The same Refinery actor supports two separate organizational functions with different decisive rights. For S2 it regulates interference among independently produced branches by serializing them against a moving target and choosing merge/conflict order. For S3* it challenges the producer completion claim through a separate verification gate, can block landing, reopen the source issue and return corrective feedback through Witness. These mappings do not rely on the role name `Refinery` or on ordinary CI alone.

## S1 — Operations

- State: A
- Function: autonomously implement bounded software-engineering issues in project repositories and return completed branch/work results.
- Disturbance / variety regulated: task ambiguity, repository state, implementation choices, tool/test observations, local blockers and discovered defects within an assigned issue.
- Decisive decision or feedback right: choose the substantive implementation/research/debugging actions required to satisfy the hooked issue and decide when the bounded work is ready to submit through the prescribed completion path.
- Decision owner: the model-driven Polecat worker agent.
- Supporting / enforcement mechanisms: isolated git worktrees, hooked Beads assignments, role/formula context, tool-capable model runtime, direct issue state updates and `gt done` completion plumbing.
- Closure path: Mayor/runtime hooks an issue to a Polecat → Polecat executes autonomously in its isolated worktree → commits/pushes and runs the completion protocol → branch/result enters the downstream Witness/Refinery or configured PR path.
- Boundary reachability: Polecat role templates, worktree provisioning, hook state and completion commands are shipped first-party Gas Town surfaces at the pinned revision; the external model host supplies inference but does not replace Gas Town's first-party worker contract.
- Why this is / is not agent-owned: the role and formula constrain execution, but the model-driven worker chooses substantive code/tool actions and how to solve the assigned issue.
- Evidence: `internal/templates/roles/polecat.md.tmpl`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: fork-backed rigs may use an external PR path instead of the canonical Refinery flow; S1 does not depend on the downstream merge mode.

## S2 — Coordination

- State: A
- Function: attenuate integration interference among independently produced Polecat branches so concurrent work does not collide on a stale common baseline or land in an incompatible order.
- Disturbance / variety regulated: multiple autonomous workers can finish branches from earlier target states; parallel/direct merging can create conflicts, invalid dependency order or inconsistent integration as the target branch moves after each accepted change.
- Decisive decision or feedback right: choose the next branch/merge order using priority, dependencies and timing; rebase it against the current target; resolve or reject conflicts; and require each subsequent branch to rebase against the newly advanced target.
- Decision owner: the model-driven Refinery agent.
- Supporting / enforcement mechanisms: per-rig merge queue, `MERGE_READY` protocol, isolated worker branches, sequential-rebase rule, target-resolution rules and merge-request state.
- Closure path: multiple Polecat outputs enter the queue → Refinery selects one and rebases it on the current target → accepted merge advances the target → the next queued branch is rebased against that new baseline; unresolvable conflicts reopen the source issue and return through Witness for new work.
- Boundary reachability: the canonical Refinery role and merge queue are shipped first-party operating surfaces for non-fork rigs; the role contract explicitly assigns merge/conflict/order judgment to the running agent.
- Why this is / is not agent-owned: deterministic queue/state machinery exposes and enforces the integration surface, but the first-party Refinery contract gives the model agent discretion over ordering and conflict/failure disposition; this is not merely authored static sequencing.
- Evidence: `internal/templates/roles/refinery.md.tmpl`, `docs/design/mail-protocol.md`, `internal/refinery/batch.go`.
- Basis: explicit + structural
- Confidence: high
- Caveats: isolated worktrees by themselves would only be supporting interference attenuation; the `A` classification rests on the agent-owned sequential integration feedback loop.
- Distinct S1 units: two or more autonomous Polecats completing separate issues/branches in the same rig or integration target.
- Inter-S1 disturbance: their branches can be based on the same earlier target and therefore conflict, invalidate each other's assumptions or require dependency-sensitive ordering when integrated.
- Attenuating coordination relation: Refinery serially selects, rebases and integrates branches against the current moving target instead of allowing parallel direct merges.
- Feedback into subsequent S1 behaviour: failed/conflicting work reopens its source issue and returns through Witness for re-sling/rework; successful integration changes the baseline against which later queued work is evaluated.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited relation addresses a concrete interference mode among outputs of independent S1 workers — incompatible concurrent branch integration — and feeds conflict/failure results back into later operational work.

## S3 — Inside-and-now control

- State: A
- Function: regulate the town's current work commitments, dispatch, cross-rig allocation, escalations and active execution on behalf of the whole Gas Town workspace.
- Disturbance / variety regulated: unassigned ready work, stalled or failed workers, competing/cross-rig work, blocked dependencies, changed priorities, integration/escalation problems and idle or misallocated execution capacity.
- Decisive decision or feedback right: choose what work to dispatch and to which rig/worker, coordinate batch/cross-rig work, resolve escalations that Witnesses cannot handle, redirect priorities/integration decisions and intervene when current agents or rigs are stuck.
- Decision owner: the model-driven Mayor agent in the standard autonomous mode.
- Supporting / enforcement mechanisms: town/rig status, convoys, Beads dependencies, mail/escalation state, Polecat lists, hooks, `gt sling`, scheduler capacity support and Witness/Deacon feedback.
- Closure path: current town/rig/convoy/escalation state becomes visible to Mayor → Mayor makes dispatch/coordination/intervention decisions → Gas Town creates/hooks workers or routes instructions/escalations → Polecat/Witness/Refinery/Deacon behavior proceeds under the changed current state and reports back.
- Boundary reachability: Gas Town ships a dedicated Mayor session, first-party Mayor role template and control commands; Mayor is launched as an agent and connected to the same persisted work/communication surfaces used by the operational organization.
- Why this is / is not agent-owned: scheduler and hook mechanisms constrain execution, but the global dispatch, cross-rig judgment and escalation-resolution rights are assigned to the model-driven Mayor rather than being fully predetermined by runtime code.
- Evidence: `internal/templates/roles/mayor.md.tmpl`, `internal/cmd/mayor.go`, `README.md`, `docs/design/escalation.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the human Overseer can interact with or administratively operate Gas Town, but the reviewed evidence does not establish a sufficiently explicit distinct parent S3 operating mode comparable to a first-party approval/override lifecycle; ordinary human tasking and process controls are therefore not encoded as `A(P)`.
- Whole-system current view: Mayor has first-party commands and persisted state for overall town status, rigs, Polecats, active convoys, issue/dependency readiness, mail and escalations across the workspace.
- Current-control decision scope: current work dispatch, worker/rig routing, batch/cross-rig coordination, escalation resolution, priority/integration judgments and intervention on stuck execution.

## S3* — Complementary audit

- State: A
- Function: independently challenge a Polecat's completion claim before its branch is allowed to land and return corrective action when the integrated result is not acceptable.
- Disturbance / variety regulated: producer self-verification can miss failures that appear only after rebasing onto the current target, integration conflicts, branch-caused test failures or untracked pre-existing failures that would otherwise be merged without an independent gate.
- Decisive decision or feedback right: run the configured verification suite after rebase, decide whether failure is branch-caused or pre-existing, block/reject a failing branch, reopen its source issue and require returned rework, or allow a verified branch to merge.
- Decision owner: the separate model-driven Refinery agent.
- Supporting / enforcement mechanisms: `MERGE_READY` handoff from Witness, separate Refinery session/role, queue state, rebase onto current target, configured setup/typecheck/lint/build/test commands, mandatory `handle-failures` gate and `MERGE_FAILED`/`MERGED` return protocol.
- Closure path: Polecat completion passes through Witness → Refinery obtains the branch independently and rebases/tests it → pass permits merge; branch-caused failure reopens source issue, closes the merge request and notifies Witness → Witness/current-control machinery can re-sling corrected operational work.
- Boundary reachability: the verification gate is embedded in the shipped canonical Refinery patrol contract and directly controls whether standard non-fork work reaches the target branch.
- Why this is / is not agent-owned: tests provide evidence but do not decide the organizational response; Refinery independently interprets conflict/failure provenance and owns the block/reopen/merge judgment under a role explicitly separated from application development.
- Evidence: `internal/templates/roles/refinery.md.tmpl`, `docs/design/mail-protocol.md`, `internal/templates/roles/witness.md.tmpl`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the same Refinery actor also owns S2 integration ordering, but the S3* claim uses a distinct decision right: independent acceptance/challenge of a producer completion claim and corrective return, not merge sequencing itself.
- Claim being audited: that a Polecat's submitted branch is integration-safe and satisfies the configured quality/test checks sufficiently to land on the target branch.
- Ordinary reporting path: Polecat performs its own completion/self-verification and signals done; Witness processes completion/lifecycle state and sends `MERGE_READY`.
- Complementary access path: Refinery independently checks the queued branch after rebasing onto the current target and runs the configured verification commands in its own merge-processing session.
- Independence boundary: Refinery is a separate agent role and is explicitly forbidden from acting as the application developer; it does not simply accept the producer's self-report and can block landing/reopen work.
- Who acts on findings: Refinery directly blocks or merges; on failure it reopens the source issue and notifies Witness, which can return the work to a new/current operational worker.

## S4 — Outside-and-then intelligence

- State: —
- Function: no materially separate first-party external/prospective adaptation function is established at the reviewed town boundary.
- Disturbance / variety regulated: external ecosystem change, future project/runtime conditions, model/provider evolution and strategic capability adaptation were inspected, but no qualifying shipped S4 owner and closed return loop was found.
- Decisive decision or feedback right: none established that continuously or episodically distinguishes outside/future conditions, develops adaptation options and returns a selected organizational adaptation into present Gas Town capability/S3.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: Mayor strategic/integration judgments, shared memories, project/research documents, HOP/Gas City material, scheduler state and historical capability/ledger data can inform work but do not by themselves close S4.
- Closure path: no qualifying outside/future sensing → adaptation option → present capability/current-control return path is established in the credited standard operating surfaces.
- Why this is / is not agent-owned: the Mayor's use of the word `strategic` concerns current architecture, priority and integration decisions in the reviewed role contract; without a distinct external/prospective sensing-and-adaptation loop it is not promoted to S4.
- Evidence: `internal/templates/roles/mayor.md.tmpl`, `internal/cmd/mayor.go`, `README.md`, reviewed design/research surfaces.
- Basis: explicit + absence review
- Confidence: high
- Caveats: future or optional Gas City/HOP organizational-evolution designs may justify new-ref reassessment if they become part of the standard running boundary.

### Absence scope

- Surfaces inspected: Mayor/Polecat/Witness/Refinery/Deacon role contracts, scheduler, convoys, escalation/mail protocols, memories/ledger references, HOP context and Gas City/research/design documentation.
- Plausible first-party paths checked: Mayor `strategic decisions`, capability ledger/history, shared memory, scheduler capacity behavior, HOP/Wasteland context, Gas City specialization/reorganization concepts and research surveys.
- Why no material first-party path remains: shipped credited paths regulate current execution and integration; the inspected external/future material does not establish a standard first-party agent that senses prospective environmental distinctions and closes a returned adaptation into present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no materially separate first-party organizational identity/ultimate-policy closure is established at the declared Gas Town workspace boundary.
- Disturbance / variety regulated: user intent, architecture/priorities, role templates, directives/configuration and Overseer interaction were inspected, but no qualifying town-level identity dispute/policy authority with a closed S5 return path was established.
- Decisive decision or feedback right: none established for choosing or ratifying the ultimate purpose/identity/constitutional policy of the Gas Town organization as distinct from assigning work, configuring roles or exercising current operational control.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: the human Overseer, Mayor interface, role/formula templates, project configuration, directives/overlays, rig lifecycle controls and user instructions shape the system but are not sufficient S5 ownership by themselves.
- Closure path: no first-party identity/ultimate-policy decision lifecycle comparable to goal/constitution/strategy ratification and return into autonomous operation was found at the pin.
- Why this is / is not agent-owned: naming the human as `Overseer`, routing strategic questions to Mayor, or allowing an operator to configure/stop/dock agents does not by itself establish S5; those paths are tasking, configuration or current control unless the ultimate organizational identity decision is explicit.
- Evidence: `internal/cmd/mayor.go`, `internal/templates/roles/mayor.md.tmpl`, `internal/templates/roles/deacon.md.tmpl`, reviewed configuration/directive surfaces.
- Basis: explicit + absence review
- Confidence: high
- Caveats: if a future standard mode introduces durable town mission/constitutional policy with explicit human or agent ultimate authority and operational return, it should be reassessed rather than inferred from today's Overseer terminology.

### Absence scope

- Surfaces inspected: Mayor/Overseer interface, role templates, rig lifecycle controls, formulas, directives/overlays/configuration, town/rig Beads identity state, escalation paths and Gas City/HOP design material.
- Plausible first-party paths checked: human user instructions, Mayor architecture/priority decisions, `rig dock/undock`, agent-role configuration, strategic issue routing, town-level identity beads and future organizational-specialization material.
- Why no material first-party path remains: these surfaces alter tasks, current capacity, implementation policy or agent configuration, but the pinned standard distribution does not expose a separate decisive lifecycle for the Gas Town organization's ultimate purpose/identity with authoritative return into operation.

## Recursion

Gas Town is explicitly nested into town and rig structures, but the assessment declares the town as system-in-focus. A rig has operational workers plus Witness/Refinery support, yet no claim is made that every rig independently closes S4/S5 or otherwise constitutes a full recursively viable organization.

## Variety and escalation

Variety is attenuated through isolated worktrees, dependency-aware Beads state, convoys, scheduler capacity limits, sequential integration and role-separated patrols. Local worker/lifecycle problems escalate Polecat → Witness → Mayor, while town infrastructure patrols can escalate Deacon → Mayor → human when unresolved. Escalation is supporting evidence for current-control closure, not a shortcut to S5.

## Evidence gaps

No material evidence gap remains for the positive S1-S3* findings at the pinned standard boundary. The main conservative edge is parent control: the repository clearly models a human Overseer and exposes administrative/current-control surfaces, but this assessment does not encode `A(P)` or `P` without a more explicit function-specific parent lifecycle. S4 and S5 are therefore left absent rather than inferred from strategic language, memory, configuration or human presence.
