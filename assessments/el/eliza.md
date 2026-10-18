---
harness_id: eliza
project_name: Eliza
repository: https://github.com/elizaOS/eliza
review_ref: 5b183d21ff25a8c3e43af9a284a38b5ff487ded9
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 4ec8130df99b89921ca39377f513ef8ef7c5fba7
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Eliza

## Review boundary
elizaOS/eliza at the pinned revision, including core `AgentRuntime` and the first-party agent-orchestrator plugin; bootable OS distributions are separate.

## Repository architecture
Core runtime agents are S1. The optional agent-orchestrator plugin adds durable coding tasks, parent-planner control of coding subagents, task/session lifecycle, task-scoped rooms, plan/diff/usage/recovery state and a validation gate before a subagent completion can become final.

## Primary evidence
- `plugins/plugin-agent-orchestrator/docs/SUBAGENT_FLOW_AND_PARITY.md`: planner creates tasks, spawns ACP coding subagents, receives events, can send follow-ups, and durable `task_complete` enters `validating` rather than `done`.
- The same document explicitly describes the topology as hub-and-spoke: subagents do not talk to each other and multiple subagents are unsynchronized.
- `plugins/plugin-agent-orchestrator/src/evaluators/sub-agent-completion.ts`: a response-handler evaluator accepts/rejects completion evidence, distinguishes provisional/unverified output, and can route control back toward planner follow-up rather than relaying an invalid completion.

## Operational model
Runtime agents are S1. The orchestrator plugin is opt-in and supplies team-level current regulation plus a distinct completion-verification path, therefore those functions are `C` rather than default `A`.

## S1 — Operations
`A`: standard runtime agents choose actions and use plugin capabilities toward outcomes. Confidence: high.

## S2 — Coordination
`—`: the reviewed orchestrator explicitly uses unsynchronized hub-and-spoke subagents with no direct peer mutual-adjustment channel.

## S3 — Inside-and-now control
`C`: the parent planner/orchestrator owns durable task/session state, spawning, mid-flight steering, lifecycle/recovery and completion-state transitions across coding workers. This is current team regulation, but only when the first-party orchestrator plugin is enabled.

R2 ownership-mode revalidation: the checked orchestrator now documents task-scoped rooms where live user messages can be forwarded to an active subagent, plus interaction/approval protocol surfaces. Those paths allow human intervention or additional input, but durable task creation, spawn/session control, recovery, follow-up routing and completion-state transitions remain on the planner/orchestrator path. The evidence does not establish a separate human/parent mode that closes the same whole-team S3 right, so S3 remains plain `C` rather than `C(P)`.

## S3* — Complementary audit
`C`: completion enters a separate `validating` state and a dedicated evaluator checks completion/failure evidence before relay or follow-up, giving a composable complementary verification path with corrective routing.

## S4 — Outside-and-then intelligence
`—`: schedules, connectors, memory and coding plans do not establish a distinct prospective environment-to-S3 intelligence loop.

## S5 — Policy and identity
`—`: character, plugin enablement, approval presets and task policy remain operator/developer supplied.

## Recursion, variety, escalation
The orchestrator adds durable hierarchy and verification, but subagent nesting is explicitly absent at the pinned ref and no recursive viable-system closure is established.
