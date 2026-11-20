---
harness_id: keel
project_name: Keel
repository: https://github.com/agent-sh/keel
review_ref: a7981c9d6d022d3086e6ac09dc9358f0aba4727b
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Keel

## Review boundary

- System in focus: The Keel local daemon, built-in coding agents and their supported owner-operated workspaces.
- Purpose and identity: Execute and supervise software work through a local harness with optional linked fleet machines.
- Relevant environment: Operator, Git workspaces, configured model endpoints, optional external agent providers and remote placements.
- Standard-distribution boundary: Shipped Bun binary, web UI and built-in turn/session/fleet/automation modules. Third-party models and ACP programs are dependencies; their own controllers are outside scope.
- Credited operating / distribution surfaces: The CLI and web daemon, including built-in delegation, worktrees, goal verification and owner settings.
- Adjacent first-party surfaces excluded from ownership: Development test suites, installer scripts, maintainer infrastructure and external provider/plugin implementations.
- First-party operating / deployment modes considered: Local coding sessions with optional subagents, goal verifier, human-triggered review and optional linked machines.
- Recursion level: An owner-managed local installation, with an active team scoped to its parent coding session.
- Reviewed revision: a7981c9d6d022d3086e6ac09dc9358f0aba4727b
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The event-persisted engine builds prompts, conducts model turns, executes tools and adds their results to the session lineage. Server modules add worktrees, agents, verification, fleet routing and trust controls. Linked machines provide additional execution placements. [src/engine/turn.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/engine/turn.ts), [src/core/store.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/core/store.ts), [src/server/routes/index.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/server/routes/index.ts), [src/fleet/placement.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/fleet/placement.ts).

## Operational model

Top-level sessions carry software work. In the supported team mode, a parent session starts discrete read-only or worktree-isolated workers, regulates their current commitments and processes branch handbacks. Goal verification can independently inspect the operational work before an achievement is admitted.

## S1 — Operations

- State: A
- Function: Execute software tasks through file, model and tool feedback.
- Disturbance / variety regulated: Uncertain workspace state, task breakdown and effects of tool calls.
- Decisive decision or feedback right: Select the next tool action and decide how to revise the work.
- Decision owner: The model-backed session including enabled worker agents in their task scope.
- Supporting / enforcement mechanisms: The engine constructs model requests, dispatches tools and stores ordered events.
- Closure path: Tool results enter the session history and determine the next model step or final output.
- Boundary reachability: The shipped daemon installs the built-in engine and workspace tools. Both the web UI and CLI reach it.
- Why this is / is not agent-owned: The session model decides what action to take after seeing tool returns.
- Evidence: [src/engine/turn.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/engine/turn.ts#L739-L931), [src/automation/agents.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/agents.ts), [src/core/store.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/core/store.ts).
- Basis: Explicit
- Confidence: High
- Caveats: ACP and provider-specific external runtime internals are outside the credited loop.

## S2 — Coordination

- State: A
- Function: Attenuate conflicts among concurrently editing agents.
- Disturbance / variety regulated: Two child agents assigned software work could write to the same checkout or produce overlapping changes.
- Decisive decision or feedback right: Distribute editing scopes and decide which returned branch changes to integrate.
- Decision owner: The parent coding agent, with first-party worktree isolation as enforcement.
- Supporting / enforcement mechanisms: Writable children in a Git workspace default to separate worktrees. Child instructions specify the branch, commitment and handback.
- Closure path: Workers report branch and work disposition to the parent. The parent can instruct a worker, consume its isolated branch or leave it out.
- Boundary reachability: The tool starts native workers and defaults to worktree isolation for writable Git workers. The branch convention and parent report are built into their instructions and return path.
- Why this is / is not agent-owned: The resolver/merge choice is a discretionary parent model decision. Deterministic isolation limits interference but does not resolve returned changes.
- Evidence: [src/automation/agents.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/agents.ts#L409-L490), [src/automation/agents.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/agents.ts#L622-L648), [src/automation/tools.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/tools.ts#L66-L112), [src/worktree/manager.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/worktree/manager.ts).
- Basis: Structural
- Confidence: High
- Caveats: The documented shared-checkout override removes this isolation. No claim that a merge is always attempted or conflict-free.
- Distinct S1 units: Separate model-backed child sessions assigned simultaneous operative tasks.
- Inter-S1 disturbance: Concurrent mutable changes against one software project can interfere before or during integration.
- Attenuating coordination relation: Scope is chosen at spawn, writeable work is isolated per worktree, and the parent controls integration from the returned branches.
- Feedback into subsequent S1 behaviour: Reports wake the parent with the returned branch and disposition. Parent sends revised work or incorporates a branch into subsequent software work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The native branch isolation and parent handback specifically bound mutable interference among distinct workers.

## S3 — Inside-and-now control

- State: A
- Function: Regulate currently running work for the active parent coding team.
- Disturbance / variety regulated: Worker stalls, changed priorities, open task dependencies and conflicting timing.
- Decisive decision or feedback right: Choose which child commitments to continue, revise, interrupt, or close.
- Decision owner: The model-backed coding session that owns the active team.
- Supporting / enforcement mechanisms: Tool-accessible child status and reports, task-scoped lists and guarded parent intervention.
- Closure path: Interventions change the worker commitment or terminate it. Continued results and stopped dispositions report back to the parent.
- Boundary reachability: The agent control and status tools are installed by the daemon and exposed to supported parent sessions in its normal toolkit.
- Why this is / is not agent-owned: The parent chooses the commitment change. Runtime caps, state and allowed targets enforce the choice.
- Evidence: [src/automation/tools.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/tools.ts#L163-L216), [src/automation/tools.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/tools.ts#L237-L252), [src/automation/tools.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/tools.ts#L380-L393), [src/automation/agents.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/agents.ts#L622-L648).
- Basis: Structural
- Confidence: High
- Caveats: Team scope is one active parent session. Fleet rule matching and helper-wide visibility do not establish a separate installation-wide autonomous control grade.
- Whole-system current view: Parent-owned child roster, active waits and schedules, live child states and the ongoing report stream at the active team recursion.
- Current-control decision scope: Start, update or interrupt a child, change its current job, and close outstanding work based on team status and reports.

## S3* — Complementary audit

- State: A
- Function: Independently verify goal-completion claims and return findings into correction.
- Disturbance / variety regulated: The ordinary producing session and transcript-based judge can accept incomplete or misleading results.
- Decisive decision or feedback right: Decide whether the evidence in the work products supports goal completion.
- Decision owner: Separate verifier model in a fresh read-only child session.
- Supporting / enforcement mechanisms: Goal judge triggers verification, creates a restricted child with primary-workspace access, validates its verdict and applies the result.
- Closure path: Only a met verifier verdict admits verified achievement. A not-met verdict and evidence return to the producing agent to continue. Separately the GUI can route review findings for fix.
- Boundary reachability: The daemon's automation installs the goal verifier and calls it after a positive ordinary judge. The built-in review route separately exposes a fresh-context diff check.
- Why this is / is not agent-owned: The verifier makes an independent judgment about observed artifacts. The scheduler and verdict handler enforce the recorded consequence.
- Evidence: [src/automation/verify.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/verify.ts), [src/automation/goals.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/goals.ts#L197-L249), [src/server/routes/reviews.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/server/routes/reviews.ts#L96-L204).
- Basis: Explicit
- Confidence: High
- Caveats: This is an audit of goal closure in the enabled goal session. Read-only execution limits which checks can be run.
- Claim being audited: The producer's claim that its configured software goal has been met.
- Ordinary reporting path: Producing model's transcript and goal judge reading the work session.
- Complementary access path: Verifier opens the same workspace in a fresh session and reads actual files and Git state or runs allowed checks. It receives the objective and ordinary claim as inputs to test.
- Independence boundary: The verifier starts with a separate transcript and restricted read-only operational authority.
- Who acts on findings: Goal controller refuses unverified completion and passes actionable evidence to the working session for correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: Choose a prospective capability adaptation from external intelligence.
- Disturbance / variety regulated: Changes in model providers, fleets or future mission conditions can change the needed operating capability.
- Decisive decision or feedback right: No specific first-party loop was established for selecting such adaptation and returning it to current capability.
- Decision owner: None established.
- Supporting / enforcement mechanisms: The platform lists models and fleet resources, reacts to wait signals, schedules follow-up, and supports task-local advisor/model switching.
- Closure path: Configured triggers resume work. Fleet selection and model switching change current placement or inference when commanded.
- Why this is / is not agent-owned: The inspected first-party paths monitor or affect current and scheduled tasks. They do not close prospective adaptation of the installation's operating capabilities.
- Evidence: [src/automation/consult.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/consult.ts), [src/automation/loops.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/loops.ts), [src/automation/waits.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/automation/waits.ts), [src/fleet/placement.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/fleet/placement.ts), [src/helper/helper.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/helper/helper.ts), [src/server/routes/switch.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/server/routes/switch.ts).
- Basis: Structural
- Confidence: Medium
- Caveats: An operator could apply external judgment through the exposed settings outside a shipped intelligence loop.

### Absence scope

- Surfaces inspected: Advisor, helper, waits, scheduled loops, provider selection and fleet placement.
- Plausible first-party paths checked: External event recognition, self-paced responses, owner-enabled helper, provider and fleet capabilities, and possible policy return.
- Why no material first-party path remains: Signals wake or redirect the existing work. Advisor sees its current transcript and fleet placement matches configured rules, with no first-party prospective capability judgment and return identified.

## S5 — Policy and identity

- State: P
- Function: Set owner-authorized standing instructions and decide whose workspace instructions govern the agent.
- Disturbance / variety regulated: Stale or changed workspace instructions can alter the agent's standing policy.
- Decisive decision or feedback right: Determine the standing owner instruction and authorize workspace instruction versions.
- Decision owner: The local installation owner.
- Supporting / enforcement mechanisms: Owner instruction editing, trust review and pinned project versions feed the frozen system prompt.
- Closure path: On operative prompt construction or refresh, owner-authorized standing instructions enter model messages and govern subsequent turns.
- Boundary reachability: The shipped owner settings and Trust routes are installed in the daemon and the engine checks their results when building system prompts.
- Why this is / is not agent-owned: The owner fixes standing instructions and approves or rejects project versions. The model follows the instructions supplied at that boundary.
- Evidence: [src/engine/turn.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/engine/turn.ts#L148-L218), [src/engine/prompt-store.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/engine/prompt-store.ts), [src/safety/trust.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/safety/trust.ts), [src/server/routes/trust.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/server/routes/trust.ts), [src/server/routes/surfaces.ts](https://github.com/agent-sh/keel/blob/a7981c9d6d022d3086e6ac09dc9358f0aba4727b/src/server/routes/surfaces.ts).
- Basis: Structural
- Confidence: High
- Caveats: Policy is the standing instruction authority. Individual tool permission approval is narrower and does not supply the S5 claim.
- Identity / ultimate-policy issue: Which owner and project instructions define the persistent working mandate and whether a changed project source is accepted.
- Ultimate authority in each claimed mode: The local owner sets their global instructions and controls which project instruction revisions can apply.
- Return-to-operation path: Authorized instructions become part of the agent's system prompt. Unapproved project changes do not take over the trusted instruction version.

## Distributed OSS parent arrangement

The local installation owner is the credited parent. Repository governance and external providers do not hold that right.

## Self-hosted and non-human modes

The shipped local daemon can extend execution to linked machines while keeping the parent session, worker records and owner trust boundary. No additional non-human ultimate-policy mode was identified.

## Recursion

The team is evaluated as one virtual organization for S2 and S3, under its parent coding session. Fleet placement and helper visibility have broader reach but are separate evidence paths.

## Variety and escalation

Separate child checkouts absorb write interference. Goal verification returns discrepancies. Owner trust governs persistent instruction sources.

## Evidence gaps

Static review at the pinned commit. No live model calls, linked machines, externally hosted ACP sessions, or workspaces were exercised.
