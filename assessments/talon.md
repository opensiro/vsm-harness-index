---
harness_id: talon
project_name: Talon
repository: https://github.com/dylanneve1/talon
review_ref: 1a4b8b60e142a6de3e0cdae9c7fa4a34c88b571e
reviewed_at: 2026-09-18
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
last_checked_ref: 1a4b8b60e142a6de3e0cdae9c7fa4a34c88b571e
last_checked_at: 2026-09-18
assessment_changed_at: 2026-09-15
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Talon

## Review boundary
Talon at the pinned revision as the multi-frontend harness/control runtime around pluggable agent backends, background heartbeats/dreams/triggers and persistent goals.

Candidate-batch #37 new-ref reassessment on 2026-09-18 accepted `7aaddbd1f9bd76ec011c2378e31bf843eae1438e` → `1a4b8b60e142a6de3e0cdae9c7fa4a34c88b571e` (v4.0.1 → v4.2.0). The delta adds cross-frontend media delivery, agent-accessible WhatsApp account operations and companion self-update. These extend operational/tooling surfaces but do not add a distinct inter-S1 coordination loop, whole-system current regulator, independent audit channel, prospective environment-intelligence loop or ultimate-policy closure. The canonical vector therefore remains unchanged.

## Repository architecture
Talon routes chats to agent backends, offers MCP tools/skills/plugins, runs heartbeat/dream/cron/trigger tasks, stores persistent goals and task state, and uses a typed event bus/task table. Self-authored watcher scripts can wake the agent when conditions become true.

## Primary evidence
- `README.md`: frontend/backend architecture; heartbeat/dream agents, persistent goals, self-authored triggers, task table/event bus and per-chat serial dispatcher.

## Operational model
Backend-powered agent sessions/background agents perform S1 work. Serial dispatch/event routing are deterministic support. Heartbeats/triggers react to conditions and advance current goals; dreams consolidate memory.

## S1 — Operations
`A`: standard agent sessions/background runs autonomously use tools toward persistent goals. Confidence: high.

## S2 — Coordination
`—`: per-chat serialization/event bus mechanically prevent execution collisions but do not constitute agent-owned S2 enactment.

## S3 — Inside-and-now control
`—`: task tables, lifecycle state, dispatcher and background scheduling expose current execution state but remain runtime infrastructure; no autonomous whole-system regulator with resource/commitment authority is supplied.

## S3* — Complementary audit
`—`: dreams, logs, task/event views and watcher state do not provide a sufficiently independent complementary audit path that challenges ordinary operational claims.

## S4 — Outside-and-then intelligence
`—`: self-authored triggers and heartbeats react to external events/conditions, but event reaction alone does not model future environmental change or generate adaptation options coupled to S3. External trigger ≠ S4.

## S5 — Policy and identity
`—`: persistent goals, soul/personality and configuration can shape behavior, but they are user/configuration authored and do not establish legitimate agent-owned ultimate-policy closure.

## Recursion, variety, escalation
Concurrent chats/background tasks are runtime work units, not recursively viable systems.