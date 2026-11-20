---
harness_id: theseus
project_name: Theseus
repository: https://github.com/zeroaltitude/theseus
review_ref: 58196a8655dc3fedcbb771c5be51a5944c28d9bf
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Theseus

## Review boundary

- System in focus: One owner-operated Theseus Linux installation, with its daemon, configured model profiles, local state and first-party interfaces.
- Purpose and identity: A personal operator's agent for tool-backed work that can continue across conversations, restarts and scheduled wakes.
- Relevant environment: Owner and task requesters, model endpoints, Linux host and projects, supported message surfaces, and remote package registries when opted-in self-extension evaluates a dependency.
- Standard-distribution boundary: Daemon, turn runner, durable tasks, local command/interaction surfaces and first-party self-improvement components. External model, registry, source host and messaging-service internals are outside.
- Credited operating / distribution surfaces: [README](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/README.md), [daemon startup](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseusd/src/main.rs), [turn runtime](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/turn.rs), [durable tasks](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/docs/features/durable-tasks.md), [installed self-improvement](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/docs/features/self-improvement.md).
- Adjacent first-party surfaces excluded from ownership: Project contributor review, external development agents, release CI, benchmarks and tests. Tests corroborate code paths and supply no runtime decision owner.
- First-party operating / deployment modes considered: Private owner interaction, durable child and scheduled tasks, and opt-in self-improvement with an enabled source workspace and separately identifiable reviewer model.
- Recursion level: Installation, with current work and separately executing task sessions as operational subdivisions and the owner as legitimate parent authority.
- Reviewed revision: 58196a8655dc3fedcbb771c5be51a5944c28d9bf
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Linux service starts the storage, indexing and warm-up routines, accepts requests from its first-party clients, and assembles model turns with callable tools. Execution state and action receipts support task recovery. The parent can create child sessions with their own context and steer or pause ongoing work. Opt-in maintenance tenders connect backlog mining, bounded builds, branch review, installation and regression response. The contributor workflow and public release benchmarking are a separate project-development recursion. [Daemon](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseusd/src/main.rs) · [Turns](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/turn.rs) · [Task features](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/docs/features/durable-tasks.md) · [Self-improvement](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/docs/features/self-improvement.md)

## Operational model

A session model decides actions for a particular request or durable task. Independently executing child task sessions can do bounded work for the same root task, and the separate maintenance builder works on candidate changes. The daemon owns storage, scheduling, reservations and enforceable limits. The installation owner can see and steer current work, and retains final decisions on whether the installation may change its own governing constraints.

## S1 — Operations

- State: A
- Function: Deliver user-requested or scheduled operational work within a running session.
- Disturbance / variety regulated: Varying user inputs, partial execution and tool feedback.
- Decisive decision or feedback right: Select which action to take next and revise the task trajectory after its result.
- Decision owner: Task/session model actor.
- Supporting / enforcement mechanisms: Turn runner, registered tool gates, persistent execution state and wake scheduling.
- Closure path: Tool results return to the running turn and condition its next model call or resulting report.
- Boundary reachability: Built into the daemon's regular turn and durable-task modes.
- Why this is / is not agent-owned: Removing the session model leaves dispatch and replay machinery without discretionary selection of the next task action.
- Evidence: [Turn loop](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/turn.rs) · [Child fan-out](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/task_fan_out.rs).
- Basis: structural
- Confidence: high
- Caveats: The review establishes a supported operating path. No provider calls or task outcome measurement were performed.

## S2 — Coordination

- State: C
- Function: Attenuate conflicting work claims among separately executing managed task sessions.
- Disturbance / variety regulated: Multiple task actors can attempt to reserve the same scoped task record.
- Decisive decision or feedback right: Resolve competing work choices after a claim is refused or stale.
- Decision owner: The lease engine arbitrates deterministically. Task actors consume the refusal and can choose another item or surface the conflict. An autonomous policy for negotiated work allocation across contenders requires composition.
- Supporting / enforcement mechanisms: Versioned lease records, a holder and expiry, exposed blocking receipt and renewal.
- Closure path: Claim or refusal returns to the acting model; projected task state returns holder and expiry to later turns.
- Boundary reachability: The daemon ships the task graph tool and scoped task projection used by task sessions.
- Why this is / is not agent-owned: The same holder wins the mechanical contention regardless of which model reasons about the returned claim. The first-party path provides concrete conflict feedback on which a composed coordinating actor could act.
- Distinct S1 units: Separate managed executing task sessions that share a task graph projection within their common work scope.
- Inter-S1 disturbance: Two sessions try to take ownership of the same scoped item, risking competing edits and duplicate work.
- Attenuating coordination relation: Exclusive renewable claim on the record; a competing session receives holder and expiration rather than a second claim.
- Feedback into subsequent S1 behaviour: The refusal directs that session to choose other work or report the blockage, and the holder's changes renew or close the claim.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A competing execution is explicitly refused on the same item and receives actionable ownership feedback.
- Evidence: [Task claims](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/task_graph/lease.rs) · [Scoped graph](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/task_graph/view.rs) · [Claim tests](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/tests_task_claims.rs).
- Basis: structural
- Confidence: medium
- Caveats: The lease protects work using the task-claim path. Its existence does not establish coordination of arbitrary shell or filesystem effects.

## S3 — Inside-and-now control

- State: P
- Function: Review installation-wide open work and intervene in current task commitments.
- Disturbance / variety regulated: Active commitments and waits accumulate across contexts, with priorities or owner availability changing while tasks are running.
- Decisive decision or feedback right: Identify which active operation to steer, suspend or resume after seeing the shared work portfolio.
- Decision owner: Installation owner, acting from the private operator context.
- Supporting / enforcement mechanisms: Work projection, owner access check, persistent hold bit, task wake path and separate hard resource limits.
- Closure path: The owner intervenes on the selected task; the loop parks at its next boundary or is woken to execute again.
- Boundary reachability: Owner work view uses daemon-wide projections; stops/resumes are first-party task operations on the daemon that runs the task.
- Whole-system current view: Daemon scope across conversations, tasks, pending owner decisions, routines and projects, with documented per-list truncation.
- Current-control decision scope: Which current commitments to hold, steer or resume. This goes beyond merely selecting a tool for one task.
- Why this is / is not agent-owned: The private view can inform a model turn, while the traced cross-task intervention path acts under the owner's authority. Task-local delegators and deterministic ceilings do not establish an independent whole-installation supervisor.
- Evidence: [Global work view](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/look/work.rs) · [Owner task hold](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rpc/task_pause.rs) · [Return at turn boundary](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/turn/join_step.rs).
- Basis: structural
- Confidence: medium
- Caveats: This is current-work intervention, not ownership of the installation's hard policy.

## S3* — Complementary audit

- State: A
- Function: Independently challenge a maintenance builder's candidate change before it becomes live.
- Disturbance / variety regulated: A candidate that appears ready through ordinary builder and gate reporting can still contain a semantically unsuitable change.
- Decisive decision or feedback right: A separately executed model evaluates a prepared candidate and rejects or accepts it, with model identity verified after routing.
- Decision owner: The reviewer actor owns its verdict. Join machinery enforces the predicate and records the result.
- Supporting / enforcement mechanisms: Separate reviewer target, live identity recheck, raw branch material, planted control and persistent verdict.
- Closure path: Rejection reopens the backlog item with reasons; the valid positive decision permits further join gates. Verification and installation are separate steps.
- Boundary reachability: Startup invokes first-party self-improvement tenders when that mode is enabled. The join implementation invokes the reviewing stage inside this installation.
- Claim being audited: A self-built branch is suitable for integration after ordinary build/gate completion.
- Ordinary reporting path: Builder session, backlog state and build/gate results.
- Complementary access path: Independent review stage examines candidate branch changes and supporting gate evidence; a planted negative control probes review behavior.
- Independence boundary: Different model from the builder is required before and after the review call, with unknown or same-model outcomes refused.
- Who acts on findings: Join runtime returns rejected work to the backlog and gates further integration.
- Why this is / is not agent-owned: The different model supplies the discretionary verdict. Test and identity checks enforce conditions rather than make that decision.
- Evidence: [Join route](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join.rs) · [Review inputs](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join/review.rs) · [Review independence and rework](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join/reviewing.rs).
- Basis: structural
- Confidence: high
- Caveats: Limited to self-made changes on this supported optional path. No independent semantic audit of every ordinary task output is claimed.

## S4 — Outside-and-then intelligence

- State: P
- Function: Decide whether to incorporate an external software capability into a future running build.
- Disturbance / variety regulated: A maintenance candidate can use an external package or version outside the installed dependency set.
- Decisive decision or feedback right: Accept or decline the candidate's change to the installation's external dependency supply.
- Decision owner: Installation owner for the resulting dependency change.
- Supporting / enforcement mechanisms: Registry allowlist, isolated package trial, lockfile comparison, version/source card, gate and install.
- Closure path: An owner-held head can proceed only through the cleared hold and join gates. Integration and a verified installation return the dependency choice to the next running build.
- Boundary reachability: The enabled daemon's maintenance pipeline reaches the dependency resolver and join hold when the candidate changes package identities.
- External distinction: A concretely fetched registry package and candidate version/source are distinct from the installation's current package inputs.
- Future / prospective distinction: The candidate is tried against a proposed next build while the installed runtime continues serving.
- Adaptation option generated: A self-build can propose a different dependency to support a new or revised installed capability.
- Path back into current capability / S3: Owner disposition changes which candidate may proceed through the join, installation and verification path.
- Why this is / is not agent-owned: The builder can devise and trial an option, while the dependency-change decision reaches the owner. Internal ledger mining by itself substantiates internal improvement, with no general autonomous external-sensing closure established here.
- Evidence: [Dependency trial and fetch](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/deps.rs) · [Owner card](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join/dependencies.rs) · [Hold and return](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join.rs) · [Installed build verification](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/join/verify.rs).
- Basis: structural
- Confidence: medium
- Caveats: Narrow dependency adoption path. No broad external trend detection or efficacy inferred.

## S5 — Policy and identity

- State: P
- Function: Decide whether the installation may self-modify and under whose rules that capability operates.
- Disturbance / variety regulated: Changes to the operating mandate or safeguards of the installation's self-improvement.
- Decisive decision or feedback right: Authorize enabling or resuming self-improvement and any applicable relaxation of protected constraints.
- Decision owner: The installation owner. The runtime and workers have delegated operating rights.
- Supporting / enforcement mechanisms: Persistent switch, authenticated owner route, protected-change hold and signed gate.
- Closure path: Owner-authorized resume writes the switch record and the daemon checks it before self work. A never-resumed installation holds. Protected changes are surfaced to the owner instead of being decided by builder or reviewer.
- Boundary reachability: The daemon starts the maintenance tenders and consults the persistent self-improvement gate in the supported mode.
- Identity / ultimate-policy issue: Whether the installation may alter its own capabilities, and which classes of relaxation remain reserved.
- Ultimate authority in each claimed mode: The legitimate installation owner decides whether a held installation resumes. Ability to stop work does not confer authority to resume it.
- Return-to-operation path: The stored switch gates subsequent maintenance activity; protected changes take the owner's hold path.
- Why this is / is not agent-owned: A candidate builder cannot grant itself the owner's authorization, even if an independent model accepted the change.
- Evidence: [Gate and default hold](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/mod.rs) · [Owner-only resume](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/crates/theseus-core/src/rsi/switch.rs) · [Keel mechanism](https://github.com/zeroaltitude/theseus/blob/58196a8655dc3fedcbb771c5be51a5944c28d9bf/docs/features/self-improvement.md).
- Basis: structural
- Confidence: high
- Caveats: Claim concerns this installation's ultimate mandate for self-change, with no project-maintainer authority inferred.

## Recursion

The installation contains conversation turns, task sessions, and a self-maintenance workstream. Coordination and audit claims refer to specific relations at those boundaries. Separate project maintainers and provider internals are outside.

## Variety and escalation

Tool or operator input reaches the active task through the turn loop. Contested work claims feed back to task sessions. The owner receives held requests across surfaces and can change task execution or decide protected operating-policy matters.

## Evidence gaps

Reviewed frozen source and first-party documentation only. Runtime recovery, different-model behavior and owner decisions were not exercised. A separate installation-wide autonomous current-work supervisor or general external strategy loop would require additional reachability evidence.
