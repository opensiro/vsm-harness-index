---
harness_id: qwen-code
project_name: Qwen Code
repository: https://github.com/QwenLM/qwen-code
review_ref: e4755ef6abb53a83316076f0e9e53f5f08c1f844
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Qwen Code

## Review boundary
Pinned first-party coding agent including ordinary subagents and TeamManager runtime.

## Repository architecture
TeamManager owns teammate lifecycle, priority message queues, shared tasks/automatic claiming, idle detection, backpressure, shutdown and an approval bridge.

## Primary evidence
- Pinned deep review established TeamManager lifecycle, priority queues, shared-task claiming, idle/backpressure/shutdown and approval bridge at `review_ref`.

## Operational model
Coding agents are S1 units. TeamManager's runtime mutual-adjustment and backpressure coordinate multiple workers; configuration/approval boundaries remain constructor/parent-owned.

## S1 — Operations
`A`: first-party coding agents autonomously perform work. Confidence: high.

## S2 — Coordination
`A`: shared claiming, priority queues, idle detection and backpressure close runtime mutual adjustment beyond delegation. Confidence: high.

## S3 — Inside-and-now control
`C`: lifecycle/shutdown/control surfaces regulate current team execution but concrete authority is constructor-defined. Confidence: high.

## S3* — Complementary audit
`—`: no distinct independent complementary audit channel was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: approval bridge and outer task/policy preserve parent authority. Confidence: high.

## Recursion, variety, escalation
Automatic claiming/backpressure attenuate contention; shutdown and approval bridge provide escalation boundaries.

## Deep-review conclusion
Signature at the pinned revision: `A A C — — P`. Qwen Code's TeamManager supplies unusually strong autonomous S2 closure.