---
harness_id: oh-my-pi
project_name: oh-my-pi
repository: https://github.com/can1357/oh-my-pi
review_ref: dbf3afad4894bde827d90f965e77b3fe1c5a95e5
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# oh-my-pi

## Review boundary
oh-my-pi at the pinned current `main` revision, including the primary coding agent, model-facing `task` and `hub` tools, subagent/worktree lifecycle, human Agent Hub, and the optional Advisor subsystem. Optional first-party modes are classified from actual decision ownership rather than treated as Constructor solely because they are configurable.

## Repository architecture
oh-my-pi supplies an autonomous coding agent that can fan work out to named subagents, keep them alive, message them through the process-global Hub/IRC surface, monitor background jobs and supervise long-running project processes. The `task` tool can expose an agent-selected `isolated` flag when task isolation is enabled; isolated worktrees separate sibling writes and are explicitly intended to prevent sibling merge conflicts.

The model-facing `hub` tool is an essential coordination/current-control surface over the agent's peers, owned background jobs and shared project processes. It can inspect peers/jobs/processes, cancel background jobs, send follow-up steering, and start/stop/restart supervised processes. Separately, the human-facing Agent Hub presents the whole current-session subagent roster with live activity/usage plus steer, revive and kill controls, establishing a distinct parent-governed current-control path.

The Advisor subsystem is a separate reviewer agent with its own model, context and `ToolSession`. By default it can independently inspect the workspace through `read`, `grep` and `glob`; it reviews primary transcript deltas and injects advice back into the primary loop. `concern` and `blocker` findings can interrupt/steer ongoing work, and blockers can force a follow-up turn after an otherwise terminal answer.

## Primary evidence
- [`docs/tools/task.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/docs/tools/task.md): model-facing multi-subagent fan-out; optional per-item isolated worktree execution; lifecycle/keep-alive and peer-roster wiring.
- [`README.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/README.md): first-party isolated-worktree mode is explicitly described as eliminating merge conflicts between sibling workers.
- [`docs/tools/hub.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/docs/tools/hub.md): always-registered agent-facing peer messaging, background-job control and shared long-running-process supervision, including job cancellation and process start/stop/restart.
- [`docs/agent-hub.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/docs/agent-hub.md): parent/operator live roster with transcript/usage inspection and steer/revive/kill authority over current-session subagents.
- [`docs/advisor-watchdog.md`](https://github.com/can1357/oh-my-pi/blob/dbf3afad4894bde827d90f965e77b3fe1c5a95e5/docs/advisor-watchdog.md): separate Advisor agents, isolated ToolSessions, default read/grep/glob workspace access, severity-aware findings and feedback/steering into the primary loop.

## Operational model
The primary agent performs coding work and can create multiple sibling S1 workers. It can choose interference-attenuating isolation for sibling work, regulate its current delegated jobs/processes through Hub, and receive independent challenge from Advisor. A parent user can separately supervise/kill/revive/steer the current subagent set through Agent Hub.

## S1 — Operations
`A`: the primary and delegated coding agents autonomously perform useful repository/tool work. Confidence: high.

## S2 — Coordination
`A`: the first-party task surface exposes a model-selected isolated-worktree mode specifically addressing sibling write/merge interference; the parent agent chooses which spawned work is isolated while the runtime enforces separation and merge/patch handling. Peer Hub messaging additionally returns coordination feedback between distinct S1s, but generic messaging alone is not the basis for the positive state. Confidence: high.

## S3 — Inside-and-now control
`A(P)`: the autonomous primary agent receives a current control surface through `hub`: it can observe its active peers/background commitments, cancel owned jobs, steer/revive peers through messaging, and start/stop/restart shared supervised processes. These interventions alter current capacity/commitments while deterministic registries/job managers/brokers enforce the decisions. Separately, the human Agent Hub exposes the current subagent roster and lets the parent steer, revive and kill members, establishing a distinct parent-governed S3 mode. Confidence: high.

## S3* — Complementary audit
`A`: Advisor is a distinct reviewer actor with its own model/context/ToolSession and default independent workspace-inspection tools. It can challenge the primary trajectory and return findings that change subsequent execution through steering/blocker feedback. This supplies materially complementary access rather than merely re-reading the primary's final report. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: Advisor review, memory, model fallback and lifecycle maintenance concern present operation/quality; no separate prospective environment-facing adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`: approval modes, user settings and human session control define operational permissions and configuration. No first-party identity/ultimate-policy matter with legitimate S5 closure was established, so generic user authority is not published as `S5=P`. Confidence: high.

## Recursion, variety, escalation
Subagents amplify operational variety. Agent-selected workspace isolation attenuates sibling write conflict; Hub provides current regulation; Advisor provides an independent challenge path. Human Agent Hub supervision is represented as parent S3 rather than being incorrectly lifted into S5.

## Admission conclusion
Canonical vector at the pinned revision: `A A A(P) A — —`. Relative to the proposal, S2 is upgraded from `C` to `A` because the autonomous parent selects the supplied conflict-attenuation mode, S3 is upgraded from `C` to `A(P)` because both autonomous and parent current-control closures are first-party, S3* remains autonomous with stronger complementary-access evidence, and generic user authority is removed from S5.