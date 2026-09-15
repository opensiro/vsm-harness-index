---
harness_id: cline
project_name: Cline
repository: https://github.com/cline/cline
review_ref: cfe9cadab99617d5013bf89f07b079d105057791
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Cline

## Review boundary
Cline at the pinned revision across the shared agent engine and the first-party SDK/CLI team runtime. Human approval remains parent authority unless configured otherwise.

## Repository architecture
Cline provides autonomous coding agents plus an opt-in persistent team mode. A lead/coordinator can spawn teammates around a shared task board; teammates exchange mailbox messages, tasks carry dependencies/status, runs expose progress/heartbeats, and the team maintains a mission log. The same runtime has outcome fragments with explicit review state and prevents finalization until every required section has a reviewed fragment.

## Primary evidence
- `docs/cli/agent-teams.mdx`: team mode uses a coordinator agent, persistent shared task board, inter-agent mailbox and mission log; team work can be resumed across sessions.
- `sdk/packages/core/src/extensions/tools/team/multi-agent.ts`: team members exchange direct mailbox messages/broadcasts; tasks and async runs track dependencies/status/progress; mission logging records activity.
- `sdk/packages/core/src/extensions/tools/team/multi-agent.ts`: outcome fragments transition through draft/reviewed/rejected and `finalizeOutcome()` rejects outcomes lacking reviewed required sections.
- `sdk/packages/core/src/extensions/tools/team/runtime.ts` exports the first-party team runtime and `createWorkerReviewerTeam` helper; team tools expose review operations.

## Operational model
Coding agents are S1 units. Team mode is not the ordinary single-agent path, so organizational functions exposed by this subsystem are classified composable (`C`) rather than default autonomous ownership (`A`).

## S1 — Operations
`A`: coding agents autonomously edit, run commands, browse/use tools and react to execution feedback. Confidence: high.

## S2 — Coordination
`C`: persistent team mailboxes, broadcast, shared dependency-aware tasks and steer messages let autonomous teammates mutually adjust ongoing work beyond simple parent-child result return. Closure requires entering/configuring team mode.

## S3 — Inside-and-now control
`C`: the coordinator/team runtime maintains current task ownership/dependencies, run status/progress, mission state and teammate lifecycle, enabling current commitment regulation at team scope; this is an optional team subsystem rather than the default single-agent path.

## S3* — Complementary audit
`C`: first-party reviewer composition plus explicit reviewed/rejected outcome fragments create a separate review path; finalization is gated on reviewed required sections. The audit role is composable rather than universally closed/default.

## S4 — Outside-and-then intelligence
`—`: planning, schedules and execution feedback remain task/team-current behavior; no distinct prospective environment intelligence function is established.

## S5 — Policy and identity
`—`: rules, approvals, permissions, team definitions and reviewer policy remain parent/developer configured.

## Recursion, variety, escalation
Persistent teams add meaningful organizational variety and review gates, but nested team composition alone is not evidence of recursively closed viability.