---
harness_id: hermes-agent
project_name: Hermes Agent
repository: https://github.com/NousResearch/hermes-agent
review_ref: db66b21ae4ed7c06fdf37c0199c588b5f5b22387
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# Hermes Agent

## Review boundary
Hermes Agent at the pinned revision as the persistent self-improving agent harness, including its skill/memory/cron/subagent features.

## Repository architecture
Hermes runs one persistent agent across CLI/messaging, with a closed learning loop that creates/improves skills and curates memory. It schedules unattended work and spawns isolated subagents for parallel workstreams.

## Primary evidence
- `README.md`: autonomous skill creation/improvement, agent-curated memory, cron scheduling, parallel subagents and tool/sandbox backends.

## Operational model
The principal/subagents perform S1 work. Subagent fan-out is task decomposition. Learning changes the principal's future operational repertoire but does not itself establish outside-and-then intelligence in the VSM sense.

## S1 — Operations
`A`: Hermes autonomously uses tools/skills/memory and scheduled execution toward outcomes. Confidence: high.

## S2 — Coordination
`—`: isolated subagent parallelization is delegation, with no separate anti-oscillation relation established.

## S3 — Inside-and-now control
`?`: gateway/scheduler/root control does not establish whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: scheduled audits and trajectory tooling do not by themselves create sufficiently independent complementary audit.

## S4 — Outside-and-then intelligence
`—`: the closed learning/skill-improvement loop is internal experience learning; no distinct external-prospective option-generation function coupled to S3 is supplied. Learning ≠ S4.

## S5 — Policy and identity
`?`: personality/context/configuration do not establish legitimate runtime ultimate-policy closure.

## Recursion, variety, escalation
Skills/memory amplify temporal S1 variety; spawned subagents are delegated workers, not recursive viable systems.