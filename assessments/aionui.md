---
harness_id: aionui
project_name: AionUi
repository: https://github.com/iOfficeAI/AionUi
review_ref: 6744099b279b991c17e31c243f0920477bd31cb6
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# AionUi

## Review boundary
Pinned built-in agent and Team Mode runtime, including persistent team task/mailbox/run/slot state and permission handling.

## Repository architecture
AionUi includes leader/teammate roles, Team MCP, task/mailbox state, queue/blocked/paused states, cancellation/interrupts and workspace modes. Human permission remains an outer authority path.

## Primary evidence
- Pinned review established Team MCP plus persistent task/mailbox/run/slot lifecycle and human permission handling at `review_ref`.
- Pinned PRD noted a remote-agent approval-propagation path may be a no-op; this limits stronger closure claims.

## Operational model
Built-in agents perform S1 work while Team Mode supplies constructor/runtime mechanisms for shared team state and control.

## S1 — Operations
`A`: built-in agents autonomously execute tool/model work. Confidence: high.

## S2 — Coordination
`C`: shared team task/mailbox/queue state provides composable coordination among teammates. Confidence: high.

## S3 — Inside-and-now control
`C`: persistent run/slot/task lifecycle and cancel/interrupt controls provide constructor-owned current regulation. Confidence: medium-high.

## S3* — Complementary audit
`—`: no independent complementary audit channel with corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective environment-facing adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: human permission and outer deployment policy retain ultimate authority. Confidence: high.

## Recursion, variety, escalation
Team state attenuates coordination uncertainty; cancellation/interrupt and human permission provide escalation boundaries.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. AionUi closes autonomous operations with composable team coordination/current control under parent authority.