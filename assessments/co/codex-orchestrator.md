---
harness_id: codex-orchestrator
project_name: Codex Orchestrator
repository: https://github.com/kingbootoshi/codex-orchestrator
review_ref: 035d5813a1d93c4d8385ee4d5ff09a9416f6a749
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Codex Orchestrator

## Review boundary

- System in focus: One local coding-project campaign using the Codex Orchestrator plugin or CLI, with Codex workers and a directing Claude session or operator.
- Purpose and identity: Delegate, observe and steer coding work and synthesize results for a user-defined project.
- Environment: Shared project checkout, agent outputs, live job states and user direction.
- Standard-distribution boundary: Shipped Claude Code skill and Codex worker CLI, tmux and job persistence. Native model/tool internals and optional external plugin capabilities stay dependencies.
- Credited operating / distribution surfaces: Skill-authored job lifecycle and claim discipline, job/status CLI, tmux worker start, capture, turn and steering mechanisms.
- Adjacent first-party surfaces excluded from ownership: Repository release, CI and implementation tests, target project PR governance and optional external codebase-map generator.
- First-party operating / deployment modes considered: One active Claude-led worker portfolio, collaborating Claude project cells in the same checkout, and direct CLI operation.
- Recursion level: One local coding project. Individual worker sessions or Claude-led cells are subordinate operations. The portfolio claims apply only where the directing actor has the relevant local view.
- Reviewed revision: `035d5813a1d93c4d8385ee4d5ff09a9416f6a749`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The CLI persists a job record, runs a native interactive Codex session under tmux and observes turn signals, process state and output. The optional skill supplies the supervising Claude role, project workflow and multi-cell scope discipline. [Native Codex launch](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/tmux.ts#L114-L142) · [Current job portfolio](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L630-L675) · [Plugin install mode](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/README.md#L227-L239)

## Operational model

Codex workers own local execution. The acting director uses whole-portfolio feedback to adjust current work. Project claims prevent two participating directing cells from picking the same work. [Worker turn and return loop](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L261-L287) · [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78) · [Multi-session claims](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L597-L618)

## S1 — Operations

- State: A
- Function: Perform project research, changes and test work.
- Disturbance / variety regulated: Varying task goals, source state, tool results and failed attempts.
- Decisive decision or feedback right: Worker chooses permissible code, investigation and tool actions.
- Decision owner: Model-backed Codex worker in its interactive job.
- Supporting / enforcement mechanisms: Launcher, runtime environment, provided scope and turn signal.
- Closure path: The worker reports a result or blocker. Its session stays available for corrections and another turn.
- Why this is / is not agent-owned: The plugin and CLI launch executable native workers rather than simulating task selection.
- Evidence: [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78) · [Worker turn and return loop](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L261-L287) · [Native Codex launch](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/tmux.ts#L114-L142)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: The native reasoning and tool runtime belong to Codex.
- Boundary reachability: CLI start and skill delegation reach a live Codex process in a job-specific tmux session.

## S2 — Coordination

- State: A
- Function: Avoid duplicate modules and overlapping project stages between active cells.
- Disturbance / variety regulated: Several Claude/Codex cells simultaneously target the same codebase.
- Decisive decision or feedback right: Claim a distinct stage or module and use peers' logged claims to adjust what to delegate.
- Decision owner: Each involved Claude agent in the multi-session plugin mode.
- Supporting / enforcement mechanisms: Shared agents.log, job identifiers and a provided claim protocol.
- Closure path: An existing stage or module claim is visible in the shared log. Peers partition their subsequent delegation accordingly.
- Why this is / is not agent-owned: The installed skill names the interference, tells agents to communicate a scope claim and leaves scope choice to them.
- Evidence: [Multi-session claims](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L597-L618) · [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78)
- Basis: Explicit procedural and structural.
- Confidence: Medium-high.
- Caveats: Advisory file convention. The CLI does not enforce exclusion or resolve simultaneous writes.
- Boundary reachability: The project-wide claim convention and log format are shipped with the installed directing skill.
- Distinct S1 units: Separately directed Claude/Codex cells with their own workers and project assignments.
- Inter-S1 disturbance: Duplicate work or conflicting edits when two cells pick the same stage or module.
- Attenuating coordination relation: Each directing agent claims a stage or module in the shared agents.log and reads other cells' commitments.
- Feedback into subsequent S1 behaviour: The peer adjusts the next work allocation away from already claimed project scope.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The protocol ties advertised scope to duplicate-work and collision avoidance in a shared checkout.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate outstanding work across a worker portfolio and intervene in current commitments.
- Disturbance / variety regulated: Stalled workers, contradictory findings, failing implementations and work split affecting the same project.
- Decisive decision or feedback right: Use full portfolio state to choose which work starts, is redirected, split, continued or terminated.
- Decision owner: Shipped Claude directing role in plugin mode, or the human CLI operator in a distinct direct mode.
- Supporting / enforcement mechanisms: Jobs/status/capture, per-turn completion signals and start/send/stop commands.
- Closure path: A director reads the job set and output, changes the affected worker commitments and reads later status or output from the resulting work.
- Why this is / is not agent-owned: The CLI supplies evidence and actuators. The plugin directs the Claude agent to exercise the portfolio decisions itself, while direct CLI mode leaves them with the user.
- Evidence: [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78) · [Plugin install mode](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/README.md#L227-L239) · [Current job portfolio](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L630-L675) · [Job changes and follow-up](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L725-L805) · [Project intervention instructions](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L713-L737) · [Direct CLI controls](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/README.md#L104-L137)
- Basis: Explicit and structural.
- Confidence: High.
- Caveats: Local worker portfolio only. Multiple Claude groups need additional partitioning to assure a single whole-project view.
- Boundary reachability: Installer exposes the skill that gives Claude the live portfolio and command loop. The same CLI is directly installable and usable by an operator without that skill.
- Whole-system current view: Job states, scope/cwd, turns, blockers, last output and usage across the managed portfolio, with capture for individual jobs.
- Current-control decision scope: Assign current work, change job guidance, split failed work and release or terminate a worker commitment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Claude with the installed directing skill | Worker status or results show a blocker, divergence or finished work | Chooses a portfolio intervention and receives the subsequent job state | [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78) · [Worker turn and return loop](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L261-L287) · [Current job portfolio](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L630-L675) · [Project intervention instructions](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L713-L737) |
| Parent (`P`) | Direct CLI project operator | Operator inspects the current job roster and finds an intervention necessary | Starts, redirects or stops the chosen session and rechecks the roster or output | [Direct CLI controls](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/README.md#L104-L137) · [Current job portfolio](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L630-L675) · [Job changes and follow-up](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L725-L805) |

## S3* — Complementary audit

- State: —
- Function: Provide complementary independent audit of live operational claims.
- Disturbance / variety regulated: Worker summaries can overlook problems or misstate quality.
- Decisive decision or feedback right: No separate source-witnessed operational audit mandate and corrective return path was established.
- Decision owner: Read-only review workers and the directing agent own ordinary implementation review tasks.
- Supporting / enforcement mechanisms: Review phase, worker logs, capture and status signals.
- Closure path: Regular findings enter the pre-commit fix and testing process. Diagnostic capture feeds work steering.
- Why this is / is not agent-owned: Distinct review sessions are real, but their routine artifact checkpoint is part of the documented production pipeline.
- Evidence: [Production review stage](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L548-L584) · [Pipeline completion criteria](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L704-L711) · [Project intervention instructions](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L713-L737) · [Current job portfolio](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/src/jobs.ts#L630-L675)
- Basis: Bounded structural absence.
- Confidence: Medium.
- Caveats: A future or custom campaign can define sporadic organization-level sampling.

### Absence scope

- Surfaces inspected: Review worker roles, evidence sources, task pipeline, status and error recovery.
- Plausible first-party paths checked: Complementary sampling of current job claims, directly independent evidence access and return of exceptional findings to a portfolio regulator.
- Why no material first-party path remains: The standard review checks produced code at the normal delivery gate. Capture exposes the same worker's operational stream for ordinary supervision.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospectively model the external environment and update the campaign's own operating capability.
- Disturbance / variety regulated: Changes in tools, dependencies or the project context could require future adaptation.
- Decisive decision or feedback right: No shipped prospective capability decision and return workflow was established.
- Decision owner: Claude directs current project ideation and research. The user decides ordinary project scope.
- Supporting / enforcement mechanisms: Source mapping, project research, PRD and decision feedback from workers.
- Closure path: Research and planning become implementation work for the current user request.
- Why this is / is not agent-owned: The reviewed shipped path improves task planning. Its research results do not enter a prospective reconfiguration loop for the host organization.
- Evidence: [Task discovery and planning](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L460-L536) · [Plugin install mode](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/README.md#L227-L239) · [Project intervention instructions](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L713-L737)
- Basis: Bounded structural absence.
- Confidence: Medium-high.
- Caveats: Users can formulate prospective projects, which are separate task instantiations.

### Absence scope

- Surfaces inspected: Ideation, research and synthesis stages, project-map input, recovery and operator options.
- Plausible first-party paths checked: Future environment analysis, experiments followed by an operational capability adoption decision, and maintained tool or role adaptation.
- Why no material first-party path remains: The documented stages derive a project plan from present code and needs. Runtime launch settings can be changed separately but there is no supplied loop from a prospective finding to new operating capability.

## S5 — Policy and identity

- State: —
- Function: Adjudicate changes to ultimate policy or campaign identity.
- Disturbance / variety regulated: User planning approval and project scope could conflict with working conventions.
- Decisive decision or feedback right: No reachable identity-policy dispute, ultimate decision and binding return path was established.
- Decision owner: User sets the work and approves important plans. Skill defines the recurring operating rules.
- Supporting / enforcement mechanisms: User discussion, PRD review, worker launch and session controls.
- Closure path: Approval authorizes the implementation plan. The same strategic and worker authority pattern governs work afterward.
- Why this is / is not agent-owned: The task sponsor's approval updates the project plan. The supplied workflow lacks an adjudication path for the identity or ultimate rules of the directing organization.
- Evidence: [Shipped Claude role](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L38-L78) · [Task discovery and planning](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L460-L536) · [Pipeline completion criteria](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L704-L711)
- Basis: Bounded structural absence.
- Confidence: Medium.
- Caveats: The user's project authority is explicit, with no automatic credit for policy-level closure at the assessment recursion.

### Absence scope

- Surfaces inspected: User and Claude authority guidance, PRD approval, job steering and execution constraints.
- Plausible first-party paths checked: Escalation of ultimate role or purpose disputes, returned rule decisions and application to later operation.
- Why no material first-party path remains: The shipped feedback concerns current project commitments and plans. An identity or ultimate-policy decision path is not supplied.

## Distributed OSS parent arrangement

The local project user owns direct operation and task approval. Upstream maintainers govern a different recursion.

## Self-hosted and non-human modes

The plugin mode supplies an autonomous directing actor under user goals. Direct CLI controls support an operator-owned mode.

## Recursion

The worker cell is nested in the local project portfolio. Multi-Claude project work preserves a separate portfolio under each Claude with shared scope claims.

## Variety and escalation

Turn signals, capture and status expose blockers. A director can redirect or stop a stalled worker. [Project intervention instructions](https://github.com/kingbootoshi/codex-orchestrator/blob/035d5813a1d93c4d8385ee4d5ff09a9416f6a749/plugins/codex-orchestrator/skills/codex-orchestrator/SKILL.md#L713-L737)

## Evidence gaps

The frozen source and documentation were reviewed. Multi-session behavior and provider execution were not run. Scope claims rely on participating agents following the shipped protocol.
