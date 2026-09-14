---
harness_id: aider
project_name: Aider
repository: https://github.com/Aider-AI/aider
review_ref: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Aider

## Review boundary
Aider at the pinned revision as a terminal coding-agent harness operating on one codebase/session.

## Repository architecture
Aider maps a codebase, edits files, integrates with Git, and can automatically lint/test changes and feed failures back into subsequent fixes. It is a single coding-agent operational loop rather than a multi-agent organization.

## Primary evidence
- `README.md`: codebase map, Git commits, IDE/terminal workflow, lint/test after changes and automatic fixing of detected problems.

## Operational model
The coding agent is S1; repo map, Git, linting and tests provide environment/feedback mechanisms inside that operation.

## S1 — Operations
`A`: the agent owns bounded edit/action decisions and iterates from repository/test feedback. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 coordination path is established at this boundary.

## S3 — Inside-and-now control
`?`: local loop controls do not establish whole-system regulatory authority.

## S3* — Complementary audit
`?`: lint/test feedback is routine operational QA and not sufficiently independent S3*.

## S4 — Outside-and-then intelligence
`?`: codebase/web context is environmental input but not a prospective adaptation function.

## S5 — Policy and identity
`?`: user instructions/configuration remain parent-owned.

## Recursion, variety, escalation
Repository/tool access amplifies one S1's variety; no recursive viable subsystem is established.