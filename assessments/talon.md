---
harness_id: talon
project_name: Talon
repository: https://github.com/dylanneve1/talon
review_ref: afae82e60540e49970d04401a25725fd7635ec96
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# Talon

## Review boundary
Talon at the pinned revision as the multi-frontend harness/control runtime around pluggable agent backends, background heartbeats/dreams/triggers and persistent goals.

## Repository architecture
Talon routes chats to agent backends, offers MCP tools/skills/plugins, runs heartbeat/dream/cron/trigger tasks, stores persistent goals and task state, and uses a typed event bus/task table. Self-authored watcher scripts can wake the agent when conditions become true.

## Primary evidence
- `README.md`: frontend/backend architecture; heartbeat/dream agents, persistent goals, self-authored triggers, task table/event bus and per-chat serial dispatcher.

## Operational model
Backend-powered agent sessions/background agents perform S1 work. Serial dispatch/event routing are deterministic support. Heartbeats/triggers react to conditions and advance current goals.

## S1 — Operations
`A`: standard agent sessions/background runs autonomously use tools toward persistent goals. Confidence: high.

## S2 — Coordination
`—`: per-chat serialization/event bus mechanically prevent execution collisions but do not constitute agent-owned S2 enactment.

## S3 — Inside-and-now control
`?`: task table/lifecycle controller are runtime infrastructure, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: dream/log/task views are not sufficiently independent audit.

## S4 — Outside-and-then intelligence
`—`: self-authored triggers and heartbeats react to external events/conditions, but event reaction alone does not model future environmental change or generate adaptation options coupled to S3. External trigger ≠ S4.

## S5 — Policy and identity
`?`: goals/soul/personality/configuration do not establish legitimate ultimate-policy closure.

## Recursion, variety, escalation
Concurrent chats/background tasks are runtime work units, not recursively viable systems.