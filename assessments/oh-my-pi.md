---
harness_id: oh-my-pi
project_name: oh-my-pi
repository: https://github.com/can1357/oh-my-pi
review_ref: acf943d3c8dc1ed135b42aa33fef4d9d2ff61c9a
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# oh-my-pi

## Review boundary
Pinned Pi-derived coding harness including task subagents/worktrees, Agent Hub, Advisor and review/permission paths.

## Repository architecture
The primary agent can delegate into task subagents/worktrees and use Agent Hub. A separate Advisor with its own context/model reviews each primary turn and can hard-block execution.

## Primary evidence
- Pinned deep review established task subagents/worktrees, Agent Hub and independent Advisor review/hard-block behavior at `review_ref`.

## Operational model
Primary coding agent performs S1 work; hub/worktree mechanisms structure concurrent work; Advisor supplies a distinct challenge channel; human authority remains outside.

## S1 — Operations
`A`: primary agent autonomously performs coding/tool work. Confidence: high.

## S2 — Coordination
`C`: Agent Hub/task-worktree mechanisms provide composable coordination across workers. Confidence: high.

## S3 — Inside-and-now control
`C`: hub/runtime controls provide constructor-owned current operational regulation. Confidence: medium-high.

## S3* — Complementary audit
`A`: Advisor is separately contextualized/modelled, reviews each primary turn and can hard-block, giving autonomous complementary audit closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: memory/review do not establish prospective organizational adaptation. Confidence: high.

## S5 — Policy and identity
`P`: ultimate task/policy/permission authority remains parent-owned. Confidence: high.

## Recursion, variety, escalation
Subagents amplify operational variety; Advisor attenuates unsafe/low-quality action and hard-blocks escalate beyond the primary worker.

## Deep-review conclusion
Signature at the pinned revision: `A C C A — P`. Its distinguishing metasystem feature is an autonomous, independent Advisor audit channel.