---
harness_id: codex
project_name: Codex
repository: https://github.com/openai/codex
review_ref: 36f0dbe796d9bb1a18a0fc0640ed08b3e1d54564
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Codex

## Review boundary
OpenAI Codex CLI at the pinned revision, including its first-party multi-agent spawn/delegation tools. Codex Web and the vendor organization are separate systems.

## Repository architecture
Codex is a local coding agent. Its pinned source includes `spawn_agent` multi-agent tooling with child-depth limits, delegated task messages, parallel workers and returned child work.

## Primary evidence
- `README.md`: local coding-agent product boundary.
- `codex-rs/core/src/tools/handlers/multi_agents/spawn.rs`: first-party subagent spawning/delegation and depth handling at the pinned ref.

## Operational model
Root and child coding agents perform S1 work. Spawn/delegate/parallel-worker mechanics decompose operational work and return results to the parent.

## S1 — Operations
`A`: Codex agents autonomously inspect/edit/run tools toward coding outcomes. Confidence: high.

## S2 — Coordination
`—`: first-party multi-agent mechanics are delegation/task decomposition; no separate mutual-adjustment or conflict-regulation function among S1 units is established.

## S3 — Inside-and-now control
`?`: parent-agent integration does not prove whole-system resource/accountability regulation.

## S3* — Complementary audit
`?`: review/testing paths are not shown as sufficiently independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: planning/context work remains current-task behavior.

## S5 — Policy and identity
`?`: permissions/instructions remain parent/user controlled.

## Recursion, variety, escalation
Child depth and nested delegation do not establish recursive viable systems.