---
harness_id: codex
project_name: Codex
repository: https://github.com/openai/codex
review_ref: 36f0dbe796d9bb1a18a0fc0640ed08b3e1d54564
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Codex

## Review boundary
Deep review of the pinned multi-agent tool handlers and coding runtime. Child-agent spawning is evaluated as delegation unless a separate coordination or control function is implemented.

## Repository architecture
Codex is an autonomous coding harness with sandboxed tool execution and first-party multi-agent tools. The multi-agent handler can spawn child agents for bounded tasks and return child results to the calling context. That is real hierarchical decomposition, but the reviewed mechanism remains parent-to-child operational delegation.

## Primary evidence
- `codex-rs/core/src/tools/handlers/multi_agents.rs`: implements multi-agent tool calls including spawning and controlling child agent tasks and returning their results to the caller.
- The parent supplies the delegated task/context and consumes the child outcome; no separate peer interference-regulation loop is established.

## Operational model
A coding agent inspects repository state, chooses tools/commands and iterates. It can delegate scoped work to child agents and incorporate returned results into the parent task.

## S1 — Operations
`A`: the standard coding agent autonomously selects actions/tools and reacts to execution feedback. Confidence: high.

## S2 — Coordination
`—`: spawning, waiting for and receiving results from subagents is hierarchical task decomposition, not a dedicated mechanism for regulating interference, oscillation or shared constraints among autonomous S1 units. The shallow `S2=A` interpretation is removed.

## S3 — Inside-and-now control
`—`: parent ownership of child tasks does not establish whole-system authority over shared organizational resources/capacity/commitments.

## S3* — Complementary audit
`—`: no independent complementary audit path distinct from normal coding/subagent execution was established.

## S4 — Outside-and-then intelligence
`—`: planning and repository exploration serve the current coding objective; no separate prospective environmental intelligence function was found.

## S5 — Policy and identity
`—`: sandbox policy, instructions and agent topology remain externally configured rather than autonomously owned as ultimate policy/identity.

## Recursion, variety, escalation
Child agents add recursive operational capacity without closing S2–S5.