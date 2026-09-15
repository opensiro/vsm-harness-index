---
harness_id: kilo-code
project_name: Kilo Code
repository: https://github.com/Kilo-Org/kilocode
review_ref: c36e22634860e06e0aa63234fae37bbd83d3b182
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kilo Code

## Review boundary
Deep review of the pinned Kilo Code core, including the agent registry/subagent mode and the repository's explicitly named `control-plane` package. Labels are mapped to functions only when the implementation satisfies the VSM criterion.

## Repository architecture
Kilo Code provides configurable coding agents and subagents. The core agent service stores/selects agent definitions and excludes `subagent` modes from ordinary top-level selection. The `control-plane` directory reviewed at this revision contains session/workspace transport logic: `move-session.ts` moves a session and optionally its Git changes between directories within the same project. It is infrastructure control, not VSM S3.

## Primary evidence
- `packages/core/src/agent.ts`: maintains the agent registry/default selection and explicitly distinguishes `subagent` mode from selectable top-level agents.
- `packages/core/src/control-plane/move-session.ts`: validates the destination project, captures/applies Git changes, moves the session location and emits a move event.
- `packages/core/src/control-plane/`: at the pinned revision contains session/workspace control-plane utilities, not a metasystem managing autonomous S1 commitments.

## Operational model
A selected coding agent performs operational work under configured capabilities; subagent modes support specialization. Session-control infrastructure can relocate execution state/worktree changes.

## S1 — Operations
`A`: coding agents are autonomous operational units within configured tools/modes. Confidence: high.

## S2 — Coordination
`—`: subagent specialization and session movement do not provide interference regulation among multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: despite the directory name `control-plane`, the reviewed implementation manages session placement/state transfer rather than whole-system resource, capacity and commitment authority across S1 units.

## S3* — Complementary audit
`—`: no independent complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: no distinct prospective environmental intelligence/adaptation function was found in the reviewed boundary.

## S5 — Policy and identity
`—`: agent definitions, modes and policy remain externally configured rather than owned by an autonomous ultimate identity function.

## Recursion, variety, escalation
Subagent modes add hierarchical variety; session movement adds runtime mobility. Neither closes the missing S2–S5 functions.