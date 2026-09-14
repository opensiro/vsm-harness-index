---
harness_id: opencode
project_name: OpenCode
repository: https://github.com/anomalyco/opencode
review_ref: 95daf90670b7c039c436c85537da5fbfe2205b41
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenCode

## Review boundary
OpenCode at the pinned revision as the coding-agent runtime with build/plan modes and the built-in `general` subagent.

## Repository architecture
OpenCode ships build and read-only plan agents that the user switches between, plus a general subagent for complex search and multistep tasks that can be invoked internally or explicitly.

## Primary evidence
- `README.md`: coding-agent product; build/plan agents; built-in general subagent and its complex-search/multistep role.

## Operational model
The active coding agent and delegated general subagent perform S1 work. User switching and parent→subagent invocation are specialization/delegation.

## S1 — Operations
`A`: standard agents autonomously perform bounded coding/search work. Confidence: high.

## S2 — Coordination
`—`: subagent invocation and user mode switching do not establish mutual adjustment among S1s.

## S3 — Inside-and-now control
`?`: parent agent does not evidence whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: plan/read-only role is not sufficiently independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: planning is not S4.

## S5 — Policy and identity
`?`: permissions/agent choice remain parent-owned.

## Recursion, variety, escalation
The general subagent extends operational variety; delegation is not recursion.