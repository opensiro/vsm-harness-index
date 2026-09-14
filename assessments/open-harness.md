---
harness_id: open-harness
project_name: open-harness
repository: https://github.com/MaxGfeller/open-harness
review_ref: 026e8d9cb8f184cdeac2054b489ec20972ba8681
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# open-harness

## Review boundary
MaxGfeller/OpenHarness at the pinned revision as a general-purpose agent library built on Vercel AI SDK.

## Repository architecture
The core provides Agent, Session, Conversation, middleware and tools. Sessions add compaction/retry/persistence; built-in subagents support dynamic catalogs, resumable sessions and background runs.

## Primary evidence
- `README.md`: agent loop, sessions/middleware/tools and first-party subagents with nested delegation/background execution.

## Operational model
Parent and subagents perform S1 work. Standard subagents are delegated executors; session/middleware mechanics support the loop.

## S1 — Operations
`A`: agents autonomously select/use tools toward bounded outcomes. Confidence: high.

## S2 — Coordination
`—`: subagent delegation/background execution does not establish an anti-oscillation relation among autonomous operations.

## S3 — Inside-and-now control
`?`: session/middleware control is not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: no sufficiently independent audit role verified.

## S4 — Outside-and-then intelligence
`?`: no prospective adaptation function verified.

## S5 — Policy and identity
`?`: tool approval/configuration remains parent-owned.

## Recursion, variety, escalation
Resumable/nested subagents are compositional workers, not automatically recursively viable systems.