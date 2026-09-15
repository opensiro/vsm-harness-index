---
harness_id: dify
project_name: Dify
repository: https://github.com/langgenius/dify
review_ref: 43ac0fce5c87815a2a6c71e109ca12aa2d467710
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Dify

## Review boundary
Dify Community Edition at the pinned revision, focusing on first-party workflow/agent runtime. Human operators and external observability systems are outside the autonomous system-in-focus.

## Repository architecture
Dify embeds agent nodes inside an authored workflow graph. Agent v2 resolves an agent binding and snapshot, runs the agent backend, adapts outputs, type-checks declared outputs, handles failures, and can pause/resume for human input. These mechanisms regulate execution of a workflow node but do not establish a Beer-style metasystem across autonomous operational units.

## Primary evidence
- `api/core/workflow/nodes/agent_v2/agent_node.py`: `DifyAgentNode` resolves a configured agent binding/snapshot and executes it through the agent backend; the node also handles output type checks, failure orchestration and human-input pauses/resumption.
- `api/core/workflow/nodes/agent_v2/ask_human_hitl.py` and `ask_human_resume.py`: HITL is an explicit parent-human pause/resume boundary rather than agent-owned policy authority.
- `api/core/workflow/nodes/agent_v2/output_failure_orchestrator.py` and `output_type_checker.py`: failure/type handling is part of the same node execution path, not complementary independent audit.
- `api/core/workflow/nodes/`: the pinned first-party node set includes agent, agent_v2, human_input, trigger and data/workflow nodes; authored workflow composition supplies sequencing and branching.

## Operational model
The executing Dify agent is S1. Workflow graph structure, bindings, output adaptation, failure handling and HITL support that S1 or sequence multiple operations, but no inspected path regulates interference among multiple autonomous S1 units as S2.

## S1 — Operations
`A`: the first-party agent runtime autonomously chooses and executes bounded model/tool actions and returns workflow outcomes. Confidence: high.

## S2 — Coordination
`—`: workflow edges, node scheduling, bindings and HITL route/sequence work. No inspected first-party mechanism provides mutual adjustment or anti-oscillation among multiple S1 units. Confidence: high.

## S3 — Inside-and-now control
`—`: failure orchestration and output constraints regulate one node/run, while the workflow engine enforces authored structure. The reviewed boundary has no whole-system agent with authority over shared resources, commitments or priorities across S1s. Confidence: high.

## S3* — Complementary audit
`—`: output validation, type checks, logs and failure handling are routine production checks in the same execution path. They do not provide sufficiently independent alternative access to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: retrieval, tools, triggers and runtime context can sense current external information, but no first-party external-and-prospective adaptation loop develops options and couples them into present S3 control. Confidence: high.

## S5 — Policy and identity
`—`: prompts, snapshots, workflow configuration and human approval boundaries are parent-authored constraints rather than legitimate runtime ultimate-policy closure. Confidence: high.

## Recursion, variety, escalation
Workflow nesting, agent bindings and pause/resume increase compositional variety. They do not establish recursively viable child systems; HITL explicitly escalates authority outward to the human/operator boundary.