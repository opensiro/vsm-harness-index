---
harness_id: smolagents
project_name: smolagents
repository: https://github.com/huggingface/smolagents
review_ref: 30bb1161095dbae2271e6bc3cc4c219cc3897a57
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# smolagents

## Review boundary
Deep review of the pinned core agent implementation, including managed-agent delegation. Manager/worker terminology is not treated as VSM S3 without whole-system current-control evidence.

## Repository architecture
smolagents implements autonomous tool/code agents and supports managed agents that can be exposed to a manager agent as delegated capabilities. This enables hierarchical task decomposition, but the manager remains an operational agent deciding which subordinate capability to call rather than a distinct metasystem regulator.

## Primary evidence
- `src/smolagents/agents.py`: implements the autonomous agent loop, tool/action execution and managed-agent composition/delegation.
- Managed agents are invoked as subordinate capabilities with task descriptions/results returned into the manager's operational context.

## Operational model
An agent reasons over a task and invokes tools/code; a manager-style agent can delegate scoped work to managed agents and use their returned results in its own loop.

## S1 — Operations
`A`: tool/code agents autonomously choose and execute task actions within configured bounds. Confidence: high.

## S2 — Coordination
`—`: managed-agent delegation does not itself regulate interference among peer autonomous S1 units. No separate anti-conflict/anti-oscillation or shared-constraint coordination function was established; the earlier `S2=C` interpretation is therefore removed.

## S3 — Inside-and-now control
`—`: a manager agent assigning work is still task execution. The reviewed runtime does not provide whole-system authority for current resource, capacity or commitment regulation across S1 units.

## S3* — Complementary audit
`—`: no independent/complementary audit channel separate from routine agent execution was established.

## S4 — Outside-and-then intelligence
`—`: agent planning and delegation operate on the current objective; no distinct prospective environmental intelligence function was found.

## S5 — Policy and identity
`—`: prompts, tools, managed-agent topology and permissions are parent/developer configured rather than determined by an autonomous policy/identity authority.

## Recursion, variety, escalation
Managed agents provide recursive specialization and useful hierarchy, but hierarchy alone does not close S2–S5.