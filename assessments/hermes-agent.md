---
harness_id: hermes-agent
project_name: Hermes Agent
repository: https://github.com/NousResearch/hermes-agent
review_ref: db66b21ae4ed7c06fdf37c0199c588b5f5b22387
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hermes Agent

## Review boundary
Deep review of the pinned persistent-agent runtime, including subagents, scheduled work and the closed memory/skill learning loop. Self-improvement is not mapped to S4 unless it performs the prospective environment-intelligence function defined by the profile.

## Repository architecture
Hermes is a persistent personal agent with tools, messaging gateways, cron scheduling, isolated subagents, durable memory and agent-managed skills. After foreground turns it can spawn a separate background review fork that replays the conversation and decides whether memory or skills should be saved or updated. This changes later operational behavior, but the loop learns from the agent's own completed trajectory rather than operating as a distinct outside-and-then environmental intelligence function.

## Primary evidence
- `README.md`: describes autonomous skill creation, skill self-improvement, persistent memory, scheduled automation and isolated subagents.
- `agent/background_review.py`: after a turn, a forked agent reviews the conversation and may write memory/skill updates directly to durable stores.
- The background reviewer is explicitly subordinate to live foreground work and exists to capture reusable experience; it is not a regulator/auditor of multiple S1 units.

## Operational model
The persistent agent chooses tools/actions for current work, can delegate bounded work to isolated subagents, and periodically distills completed experience into memory/skills for reuse.

## S1 — Operations
`A`: Hermes autonomously uses tools, executes scheduled or conversational work and maintains persistent operational state. Confidence: high.

## S2 — Coordination
`—`: subagent spawning is parent-to-child delegation; no peer interference-regulation mechanism among autonomous S1 units was established.

## S3 — Inside-and-now control
`—`: foreground/subagent lifecycle and scheduling do not create a whole-system current-control function over multiple S1 resources and commitments.

## S3* — Complementary audit
`—`: the background review fork is separately executed, but its responsibility is memory/skill capture and self-improvement rather than independent assurance of operational compliance/performance with corrective escalation.

## S4 — Outside-and-then intelligence
`—`: the closed learning loop adapts from completed internal task experience, but no distinct function was found that scans the external future environment and converts that intelligence into strategic/capability adaptation. The shallow `S4=A` interpretation is removed.

## S5 — Policy and identity
`—`: personality, policies, tools, approvals and user model remain configured around the agent rather than autonomously owned as ultimate system identity/values.

## Recursion, variety, escalation
Hermes has unusually strong persistent learning and recursion, but under the strict functional boundary those remain S1 self-adaptation rather than S4 metasystem closure.