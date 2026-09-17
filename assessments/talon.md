---
harness_id: talon
project_name: Talon
repository: https://github.com/dylanneve1/talon
review_ref: afae82e60540e49970d04401a25725fd7635ec96
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 7aaddbd1f9bd76ec011c2378e31bf843eae1438e
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

# Talon

## Review boundary
Talon at the pinned revision as the multi-frontend harness/control runtime around pluggable agent backends, background heartbeats/dreams/triggers and persistent goals.

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