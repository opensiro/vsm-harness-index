---
harness_id: proliferate
project_name: Proliferate
repository: https://github.com/proliferate-ai/proliferate
review_ref: 74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f
reviewed_at: 2026-09-16
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-16
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Proliferate

## Review boundary
Proliferate at pinned revision `74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f`, assessed as the shipped AI IDE/control plane plus its first-party subagent and review runtimes. The review distinguishes task isolation/delegation from VSM coordination and distinguishes product-triggered review initiation from the autonomous audit work performed after a review run starts.

## Repository architecture
A workspace hosts native coding-agent sessions in isolated task branches/worktrees. Parent agents can create bounded child sessions, configure them, send work, and receive a durable exactly-once completion result. Separately, Proliferate has a dedicated plan/code review runtime: review-only agents inspect a trusted target, return a structured pass/critique result, and are explicitly forbidden from editing the target or launching children. Review feedback is delivered into the parent session; with `auto_iterate` enabled, revision and a new review round repeat until pass or the configured round bound.

## Primary evidence
- `README.md`: parallel native harnesses, per-task worktree isolation, scoped subagent delegation, workflows.
- `specs/systems/subagents/README.md`: product-owned parent/child delegation, bounded child roster, durable child sessions, exactly-once result wakeup.
- `specs/systems/subagents/workspace-mcp.md`: workspace MCP create/configure/message lifecycle; delegated sessions cannot recursively delegate.
- `specs/systems/subagents/reviews.md`: separate review-role contract, review-only permissions, structured `submit_review_result`, review rounds, parent feedback/revision states and bounded iteration.
- `anyharness/crates/anyharness-lib/src/domains/reviews/runtime/feedback.rs`: critique persistence, parent-session feedback delivery, `auto_iterate` revision/re-review closure and retry-safe delivery state.
- `anyharness/crates/anyharness-lib/src/api/http/reviews.rs`: first-party plan/code review run creation and dispatch through the product review runtime.
- `anyharness/crates/anyharness-lib/migrations/0034_review_agent_loops.sql`: review-loop `auto_iterate` defaults enabled.

## Operational model
Coding agents and delegated child sessions are S1 work units. Worktree isolation and one-level delegation reduce collisions and context load but do not regulate mutual interference among operational units. Audit is a separate runtime path: a constrained reviewer observes the target independently, cannot repair it itself, and feeds findings back to the parent execution session for correction and possible re-review.

## S1 — Operations
`A`: standard product sessions run native coding-agent harnesses that autonomously inspect, edit and execute work inside bounded task workspaces; child sessions can independently complete delegated scoped work and return results. Confidence: high.

## S2 — Coordination
`—`: first-party isolation, parent→child messaging and exact completion wakeups are conflict avoidance/delegation mechanisms. The pinned implementation does not provide an agent-owned mutual-adjustment loop that observes and dampens interference or oscillation among peer S1 units. Confidence: high.

## S3 — Inside-and-now control
`—`: the product control plane provisions workspaces, sessions and workflows, while a parent may supervise its own delegated children, but no distinct autonomous actor is given current-whole authority to regulate shared resources, commitments or priorities across the operational system. Scheduling/provisioning alone is not Beer S3. Confidence: medium-high.

## S3* — Complementary audit
`A`: the first-party review runtime establishes an independent audit path. Review-only agents inspect trusted plan/code targets, are prohibited from modifying them, submit structured pass/critique results, and return findings to the parent session. The runtime can automatically iterate parent revision → trusted recapture → fresh review round until pass or a configured round limit. This is a ready, agent-enacted complementary audit/feedback loop rather than a developer-supplied verifier primitive. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: recurring/event-driven workflows react to configured events and can run tasks such as triage or dependency updates, but the pinned distribution does not establish a persistent agent-owned external/prospective intelligence function that models environmental change and feeds adaptation into present control. Confidence: medium-high.

## S5 — Policy and identity
`—`: harness choice, workflow definitions, reviewer configuration, permissions and review policy remain product/operator configuration. No first-party agent holds final authority over organizational identity, purpose or constitutional policy. Confidence: high.

## Recursion, variety, escalation
Child sessions add operational variety but are deliberately one-level and parent-owned, so they are not recursive viable systems by default. Review agents form a separate audit channel rather than a nested operational unit. Escalation is concrete in the review loop: critique is delivered to the parent execution session, which revises the target before another audit round.

## Deep-review conclusion
Signature at the pinned revision: `A — — A — —`. The important correction from the shallow assessment is S3*: Proliferate has substantially more than per-task “review state”; it ships a constrained, independent, feedback-closing review-agent runtime. Conversely, parallel worktrees and delegation do not justify S2 or S3.