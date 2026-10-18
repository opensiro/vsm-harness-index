---
harness_id: open-harness
project_name: open-harness
repository: https://github.com/MaxGfeller/open-harness
review_ref: 026e8d9cb8f184cdeac2054b489ec20972ba8681
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 026e8d9cb8f184cdeac2054b489ec20972ba8681
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# open-harness

## Review boundary
MaxGfeller/OpenHarness at the pinned revision as a general-purpose agent library built on Vercel AI SDK.

## Repository architecture
The core provides Agent, Session, Conversation, middleware and tools. Sessions add compaction/retry/persistence; built-in subagents support dynamic catalogs, resumable sessions and background runs.

## Primary evidence
- `README.md`: agent loop, sessions/middleware/tools and first-party subagents with nested delegation/background execution.

## Operational model
Parent and subagents perform S1 work. Standard subagents are delegated executors; session/middleware mechanics support each loop but do not close organizational metasystem functions across independent operations.

## S1 — Operations
`A`: agents autonomously select/use tools toward bounded outcomes. Confidence: high.

## S2 — Coordination
`—`: subagent delegation/background execution does not establish an anti-oscillation relation among autonomous operations.

## S3 — Inside-and-now control
`—`: sessions, middleware, retries, approvals and subagent lifecycle support individual runs; no standard autonomous actor has a whole-system current view plus authority over shared resources/commitments.

## S3* — Complementary audit
`—`: middleware/events/tool approval expose checks and hooks, but no distinct sufficiently independent autonomous audit path is supplied.

## S4 — Outside-and-then intelligence
`—`: compaction, retry, resumable sessions and background execution manage current execution/context rather than external-and-prospective adaptation.

## S5 — Policy and identity
`—`: tools, approvals, prompts and model/configuration choices are application/parent supplied; no agent holds ultimate policy or identity authority.

## Recursion, variety, escalation
Resumable/nested subagents are compositional workers, not automatically recursively viable systems.