---
harness_id: limen
project_name: Limen
repository: https://github.com/overment/limen
review_ref: f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: P
---

# Limen

## Review boundary

- System in focus: One installed Limen project with a hosted Pi or OMP coordinator and Limen-managed worker and review jobs.
- Purpose and identity: Turn accepted product work into checked, reviewable repository changes while preserving project intent and decision authority.
- Relevant environment: Product owner and users, the target Git project, model providers, a shared workstation, and external sources named in research jobs.
- Standard-distribution boundary: Package CLI, installed project templates and extensions, native job lifecycle and Git worktree integration in the documented first-party setup.
- Credited operating / distribution surfaces: `limen init`, coordinator role instructions, detached worker and reviewer jobs, project board, recovery/wake hooks, owner-supplied vision and project choices.
- Adjacent first-party surfaces excluded from ownership: The Limen project's own feature histories and dogfood evidence, GitHub actions, external product articles, and undocumented remote agent behavior.
- First-party operating / deployment modes considered: Local hosted coordinator with detached Pi/OMP workers, agent-directed review and repair, owner-held project decisions, and opt-in research roles.
- Recursion level: One managed product project with several operational jobs; the shared seat's aggregate process limits are infrastructure.
- Reviewed revision: `f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Limen initializes a project-controlled specification and board and equips a hosted agent to start bound Pi or OMP jobs. Each job keeps its prompt, worktree and branch, engine settings, state, session and logs. Hooks deliver completion back to the subscribed coordinator. The coordinator uses project policy, proof, job evidence and active tickets to steer, continue, request review or land. The shared launch queue checks process resources and the applicable priority rules before spawning. Project policy lives in the owner's vision and recorded board choices. External providers supply model inference while Limen supplies the installed operating context, tools and roles.

## Operational model

Separate worker jobs take real product scopes and produce branch changes plus checks. The coordinator may do small work itself and regulates the set of jobs at the project boundary. A review job has a different operating mandate and inspects a pinned candidate. The owner retains product scope and standing-policy changes plus specific interventions; the CLI enforces recorded state, worktree separation and applicable checks.

## S1 — Operations

- State: A
- Function: Implement and check an accepted product change at a specified repository base.
- Disturbance / variety regulated: Different tickets, code states, tool outputs and failed checks require different edits and follow-up actions.
- Decisive decision or feedback right: Choose worktree edits, tools and checks inside the ticket scope and report the evidence.
- Decision owner: The model-backed worker.
- Supporting / enforcement mechanisms: Job preamble, durable task, independent Git worktree, engine binding, status files and terminal handoff.
- Closure path: The executed edits and checks yield a candidate branch and result that the coordinator receives and can land or repair.
- Boundary reachability: The shipped CLI creates and starts the native job using the configured Pi or OMP engine with the standard worker preamble.
- Why this is / is not agent-owned: The wrapper launches the job, while only the worker chooses what code and proof satisfy the task.
- Evidence: [worker setup](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/src/commands/spawn.ts), [worker contract](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/worker.md).
- Basis: structural
- Confidence: High
- Caveats: Source review of a configured engine path. No worker session was executed.

## S2 — Coordination

- State: A
- Function: Set and adjust simultaneous project-work scopes to attenuate interference at shared code and sequencing boundaries.
- Disturbance / variety regulated: Multiple active job candidates may touch the same files or subsystems or consume a dependency before its predecessor lands.
- Decisive decision or feedback right: Use the whole active-ticket set and actual seams to decide parallel versus sequenced work, and steer or hold affected workers on observed overlap.
- Decision owner: The hosted project coordinator agent.
- Supporting / enforcement mechanisms: Project board, tickets and seam identifiers, worktree isolation, scoped job steering and terminal wakes.
- Closure path: The chosen disjoint jobs are started while dependent work waits. A live correction reaches the addressed running job through steering and changes its next work.
- Boundary reachability: The installed coordinator prompt specifies disjoint-seam versus Sequenced work and provides the first-party spawn, status and steer tools.
- Why this is / is not agent-owned: A worktree reduces direct write contention. The coordinator supplies the discretionary cross-job seam and sequencing choices.
- Evidence: [default coordinator loop and recovery](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L146-L161), [steer](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/src/commands/steer.ts), [steering hook](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/hook/steering.ts).
- Basis: structural
- Confidence: Medium
- Caveats: Agent judgment governs the seam test; no generic automatic file-ownership arbiter is assumed.
- Distinct S1 units: Concurrent product implementation jobs in their own worktrees.
- Inter-S1 disturbance: Overlapping change seams and dependency order across jobs aimed at the same product branch.
- Attenuating coordination relation: Coordinator chooses disjoint parallel seams and sequences shared or dependent seams, then directs corrections to the affected jobs.
- Feedback into subsequent S1 behaviour: Deferred launches and scoped steers change which work can proceed and how already-running work continues.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The operating protocol identifies actual shared seams and dependency clashes, using the returned job view to decide when parallelism would create conflicting work.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate live project commitments and quality or resource tradeoffs across all jobs on the board.
- Disturbance / variety regulated: Work stalls, checks reject candidates, spend limits change and several accepted tickets compete for attention.
- Decisive decision or feedback right: Allocate or stop jobs, choose correction versus landing, or apply a legitimate owner decision on a project-level tradeoff affecting priorities, scope or proof.
- Decision owner: Hosted coordinator for ordinary current control; legitimate project owner for the separate reserved control mode.
- Supporting / enforcement mechanisms: Board/job state, subscribed wakes, spawn/steer/stop/continue, recorded authority precedence and land checks.
- Closure path: The coordinator starts, holds, steers, resumes or lands work. Recorded owner choices supersede package defaults and change subsequent launch or acceptance behavior.
- Boundary reachability: The installed coordinator has the board and job commands. The same hosted session takes explicit owner intervention and records durable current-control decisions.
- Why this is / is not agent-owned: Routine work disposition is the coordinator's decision. In the parent mode the owner decides the escalated current project tradeoff and the coordinator carries it out.
- Evidence: [policy precedence and default loop](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L61-L75), [coordinator discretion](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L189-L195), [landing](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/src/commands/land.ts).
- Basis: structural
- Confidence: Medium
- Caveats: The project-wide mode is bounded to the local product project. The seat-wide process gate enforces resource constraints.
- Whole-system current view: Active and queued feature tickets, current and completed jobs, review evidence and constraints are assembled for the same project by the board, jobs and coordinator session.
- Current-control decision scope: Allocate jobs, stop or correct current work and set authoritative current scope, priorities and review or quota choices for ongoing project commitments.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Hosted coordinator model | Rejected candidate or stalled accepted work | Decides and issues scoped repair, continuation, stop or land | [coordinator discretion](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L187-L195) |
| Parent (`P`) | Project owner | Escalated project priority, scope or resource decision | Decision supersedes current choices on the board and later jobs operate within it | [policy precedence](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L61-L75) |

## S3* — Complementary audit

- State: A
- Function: Directly challenge a candidate's claimed correctness in a separate review job and return the finding to current control.
- Disturbance / variety regulated: Green worker logs or a clean exit can hide a contract break in the resulting diff.
- Decisive decision or feedback right: Establish proven, plausible or unverified findings by independently examining the pinned artifact, callers and discriminating tests.
- Decision owner: Fresh model reviewer distinct from the worker and the coordinator.
- Supporting / enforcement mechanisms: Dedicated review preamble, candidate ref and Git worktree, terminal receipt and coordinator wake.
- Closure path: The reviewer delivers a commit-bound verdict. The coordinator files it and chooses repair or landing under project policy.
- Boundary reachability: The first-party CLI recognizes the review role, checks its candidate and prepares the review job from the standard preamble.
- Why this is / is not agent-owned: The review model reads the candidate and chooses the proof and verdict. The coordinator separately owns the response to that verdict.
- Evidence: [reviewer contract](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/reviewer.md), [review plumbing](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/src/commands/spawn.ts), [review and return](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/docs/jobs.md#L39-L56).
- Basis: structural
- Confidence: High
- Caveats: Independent review is opt-in under project policy and need not use a different model vendor.
- Claim being audited: The worker candidate satisfies the acceptance and repository contracts at the specified commit.
- Ordinary reporting path: Worker's result, checks and done state reach its owning coordinator.
- Complementary access path: The reviewer opens the candidate diff and source in a separate git context and runs independent checks.
- Independence boundary: Fresh reviewer role/session with artifact access and no mandate to implement the candidate.
- Who acts on findings: Project coordinator, subject to owner policy.

## S4 — Outside-and-then intelligence

- State: C
- Function: Research external alternatives and put the judged evidence into a future project choice.
- Disturbance / variety regulated: Outside repositories or documented approaches can change which prospective product or implementation direction is viable.
- Decisive decision or feedback right: Select scoped external questions and turn independently gathered evidence plus a judge result into a future project decision or specification.
- Decision owner: A project-configured coordinator under the owner's research authority composes the inquiry and selects the receiving spec or decision.
- Supporting / enforcement mechanisms: Dedicated researcher and judge roles, external source references, committed reports and documented judgment-to-spec handoff.
- Closure path: The coordinator consumes the judgment in a ticket, decision or vision proposal that may be carried into subsequent project work.
- Boundary reachability: The standard installed coordinator research recipe starts dedicated roles with specified external sources and stores a judgment where the coordinator owns planning.
- Why this is / is not agent-owned: Research tooling and judge reports are available, while the receiving future policy choice and practical adoption depend on the project's composed operator/coordinator arrangement.
- Evidence: [research recipe](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L199-L214), [researcher](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/researcher.md), [judge](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/judge.md).
- Basis: structural
- Confidence: Medium
- Caveats: An ordinary worker's current coding research, external task inbox or speculative feature in the development tree does not supply this witness.
- External distinction: Independent research can compare named upstream revisions and external documentation.
- Future / prospective distinction: An inquiry on an unresolved choice informs later scope, design direction or a future capability to build.
- Adaptation option generated: Judged alternatives that can enter a new ticket, a decision or a proposal for future vision.
- Path back into current capability / S3: The coordinator records the selected outcome in project planning and controls subsequent jobs against accepted work.

## S5 — Policy and identity

- State: P
- Function: Set and amend durable project purpose and ultimate constraints when a proposed change affects product identity or authority.
- Disturbance / variety regulated: A prospective change can conflict with established product principles, owner authority or a standing operative constraint.
- Decisive decision or feedback right: Approve or reject a proposed change to the human-owned project vision or settle incompatible governing choices.
- Decision owner: Legitimate product/project owner, who remains authoritative across coordinator replacement.
- Supporting / enforcement mechanisms: Human-owned vision file, hosted coordinator context, worker requirements and explicit owner precedence. A vision-defined test cap can mechanically bind landing.
- Closure path: Approved durable intent enters the vision and subsequent coordinator and worker context. A changed cap takes effect in later landed changes.
- Boundary reachability: The documented initialized workflow routes durable product decisions to the owner, then writes the decision into the same package-supported project files later consumed in operation.
- Why this is / is not agent-owned: The coordinator may develop and request a change, while the owner has authority to amend project identity and ultimate constraints.
- Evidence: [durable intent and precedence](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/templates/agents.md#L43-L74), [project onboarding](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/README.md#L43-L61), [binding test limit](https://github.com/overment/limen/blob/f1e3a54a6cd9c2baa4cf3d2acd2d1e640b1d5a75/src/commands/land.ts#L165-L205).
- Basis: structural
- Confidence: High
- Caveats: Ordinary feature approval and maintainer governance of Limen itself are outside this witness.
- Identity / ultimate-policy issue: Durable project purpose, boundaries and standing constraints that govern the model and workers beyond a single ticket.
- Ultimate authority in each claimed mode: Human project owner can authorize a different project vision; coordinator executes within it.
- Return-to-operation path: Coordinator context and worker instruction point to the amended vision and applicable machine-enforced constraints take effect at land.

## Recursion

The assessment concerns one product project. Worker jobs have scoped operational autonomy. The seat's external capacity and the Limen project maintainers' own development system are adjacent organizational boundaries.

## Variety and escalation

Project-wide visibility comes from the accepted-work board, job evidence and Git context. Ordinary job failures return to coordinator correction. Identity and meaningful priority conflicts can reach the owner via the hosted coordinator. A separate auditor reads the artifact and gives a verdict for corrective closure.

## Evidence gaps

Source-only assessment. Supported tool wiring and role instructions establish the claimed paths at the frozen revision. No live provider, hosted session, deployment behavior or independent Index audit was tested.
