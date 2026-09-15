---
harness_id: open-interpreter
project_name: Open Interpreter
repository: https://github.com/openinterpreter/openinterpreter
review_ref: f110a7a85f43efc343f936f5bc504e01eb262550
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Open Interpreter

## Review boundary
Open Interpreter at the pinned revision, focusing on its Codex-derived coding-agent runtime plus first-party multi-agent and Guardian review capabilities. External MCP services/provider organizations are outside the boundary. Optional first-party capabilities are `C` when the function exists but requires enabling/configuration rather than being owned in the standard path.

## Repository architecture
The main coding agent executes tools in a sandboxed workspace. The pinned source also contains stable but default-disabled `MultiAgentV2` with spawning, ongoing messages, follow-up tasks, waiting/interruption and agent-state listing. Separately, the stable Guardian approval path can launch a dedicated review session that evaluates a planned privileged action and returns allow/deny; repeated denials can interrupt the operating turn.

## Primary evidence
- `codex-rs/core/src/tools/handlers/multi_agents_v2.rs` and `multi_agents_v2/spawn.rs`: first-party collaboration tools create named child agents, deliver task communications and preserve agent paths rather than only a one-shot tool return.
- `codex-rs/core/src/tools/handlers/multi_agents_v2/list_agents.rs`: agents can inspect current team/agent states through shared agent-control.
- `codex-rs/core/src/session/multi_agents.rs`: root and child agents receive `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `interrupt_agent` and `list_agents`; children can spawn children and agents share the workspace.
- `codex-rs/features/src/lib.rs`: `MultiAgentV2` is `Stage::Stable` but `default_enabled: false`; the richer team path is therefore a first-party composable capability rather than unconditional OOB behavior.
- `codex-rs/core/src/guardian/mod.rs`: a dedicated Guardian review session assesses the exact planned approval action, uses structured allow/deny output and fails closed; a rejection circuit breaker can interrupt a turn after repeated denials.
- `codex-rs/core/src/guardian/review.rs`: Guardian routes as a distinct reviewer for approval decisions and can return denial/abort outcomes that constrain subsequent operation.
- `codex-rs/features/src/lib.rs`: `GuardianApproval` is stable/default-enabled, while Guardian V2 is under development/default-disabled; reviewer/approval configuration still determines when the complementary path is exercised.
- `codex-rs/core/src/config/mod.rs` and `codex-rs/core/src/session/handlers.rs`: permissions, approval decisions and policy amendments are runtime/user-managed constraints around agent execution.

## Operational model
Coding agents are S1. Optional MultiAgentV2 adds persistent inter-agent communication/state access that can be composed into S2 coordination, but does not supply a complete anti-oscillation policy. Guardian is a separate review path with distinct context and corrective authority over privileged actions, yielding composable S3*. Sandbox/permission machinery remains runtime control rather than agent-owned S3/S5.

## S1 — Operations
`A`: the coding agent autonomously inspects/edits the workspace, executes tools and reacts to results. Confidence: high.

## S2 — Coordination
`C`: stable first-party MultiAgentV2 exposes ongoing messaging, follow-up work, waits/interrupts and team-state listing over a shared workspace, enough to compose mutual-adjustment/collision-regulation. Because the richer path is default-disabled and coordination policy is not closed by the runtime, it is not `A`. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: agent-control and permission services can list, spawn, interrupt and constrain work, but the harness does not give an autonomous agent a whole-system current view plus authority over shared budgets/priorities/commitments as an S3 function. Confidence: medium-high.

## S3* — Complementary audit
`C`: Guardian supplies a distinct reviewer session that examines a proposed privileged action against contextual evidence and can deny it or trigger interruption, materially differing from the operating agent's normal production path. Reviewer/approval configuration determines when it is active, so it is composable rather than unconditional agent-owned audit. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: web/tools, memory and goals do not establish a distinct external-and-prospective adaptation function in two-way conversation with S3. Confidence: medium-high.

## S5 — Policy and identity
`—`: AGENTS.md, permission profiles, approval policy, hooks and harness configuration are user/runtime/managed constraints; no agent-owned ultimate identity/policy closure is established. Confidence: high.

## Recursion, variety, escalation
Nested agents support task decomposition, not recursive viability. MultiAgentV2 amplifies coordination capacity; Guardian adds an exceptional corrective channel, while permissions attenuate action variety.

## Deep-review result
`S2` changes from `—` to `C`; `S3` resolves from `?` to `—`; `S3*` resolves from `?` to `C`; `S4` and `S5` resolve from `?` to `—`; `S1 A` is confirmed. The new positives come from pinned implementation beyond README, not component labels.