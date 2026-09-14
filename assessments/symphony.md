---
harness_id: symphony
project_name: Symphony
repository: https://github.com/openai/symphony
review_ref: e0ccc83720a42a600a53b61c5f8d3e518bebe1db
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Symphony

## Review boundary
Symphony at the pinned revision as the scheduler/runner around coding-agent sessions, with its draft v1 service specification as primary architecture evidence.

## Repository architecture
Symphony continuously reads an issue tracker, creates isolated per-issue workspaces, dispatches coding agents with bounded concurrency, retries/reconciles runs and exposes observability. Its spec explicitly states Symphony is a scheduler/runner; workflow policy lives in repo-owned `WORKFLOW.md`, while coding agents perform ticket writes and implementation work.

## Primary evidence
- `README.md`: autonomous isolated implementation runs and proof-of-work surface.
- `SPEC.md`: explicit scheduler/runner boundary; deterministic orchestrator state, dispatch/retry/reconciliation, workspace isolation, workflow-policy ownership.

## Operational model
Coding-agent runs are S1. Symphony’s coordination/orchestrator layers are deterministic service mechanisms, not AI agents absorbing organizational variety.

## S1 — Operations
`A`: spawned coding agents autonomously implement issue work in isolated workspaces. Confidence: high.

## S2 — Coordination
`—`: workspace isolation, concurrency limits and dispatch/reconciliation coordinate runs mechanically; no agent-owned S2 decision right is supplied.

## S3 — Inside-and-now control
`—`: the spec’s orchestrator owns scheduling/retry/state as deterministic code, not an autonomous S3 actor.

## S3* — Complementary audit
`?`: proof-of-work/CI/review evidence may support external checking, but the standard spec does not establish a sufficiently independent autonomous audit agent with corrective closure.

## S4 — Outside-and-then intelligence
`—`: tracker polling is current-work sensing, not strategic prospective adaptation.

## S5 — Policy and identity
`—`: `WORKFLOW.md` and operator trust/approval policy are repo/human-owned.

## Recursion, variety, escalation
Per-issue isolated agents are parallel S1s, not recursively viable systems.