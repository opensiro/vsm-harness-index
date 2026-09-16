---
harness_id: superagentx
project_name: SuperAgentX
repository: https://github.com/superagentxai/superagentx
review_ref: 28f2759f20d2dba9fa184ca4fe6b50943388cfbc
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 28f2759f20d2dba9fa184ca4fe6b50943388cfbc
last_checked_at: 2026-09-16
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

# SuperAgentX

## Review boundary
Deep review of the pinned first-party workflow runtime, with sequential/parallel execution, routing and approval language tested against the VSM function definitions rather than accepted by label.

## Repository architecture
SuperAgentX composes autonomous agents into workflows. `AgentXPipe` can execute agents sequentially or in parallel, select agents through a router, pass results forward and persist workflow state. These are useful orchestration primitives, but the reviewed implementation does not establish a separate mechanism for regulating interference among autonomous S1 units or a whole-system S3 authority.

## Primary evidence
- `superagentx/agentxpipe.py`: constructs sequential/parallel agent workflows, optionally routes to a subset of agents, propagates prior results and persists workflow execution state.
- `README.md`: documents workflow composition and human-approval/governance patterns; these remain configured application behavior rather than autonomous S5 authority.

## Operational model
Configured agents perform task work and can be composed into a pipeline. Parallel execution uses concurrent fan-out and aggregation; sequential execution passes context/results along the configured chain.

## S1 — Operations
`A`: individual configured agents autonomously execute model/tool work within the workflow. Confidence: high.

## S2 — Coordination
`—`: sequencing, routing, parallel fan-out and result aggregation define workflow topology, but no dedicated mechanism was found that detects and regulates interference or instability among multiple autonomous S1 units. Therefore the earlier workflow-derived `C` interpretation is rejected.

## S3 — Inside-and-now control
`—`: workflow state and routing do not amount to a whole-system current-control function with authority over shared resources, priorities and commitments across the viable system.

## S3* — Complementary audit
`—`: persistence, logging and ordinary review/approval stages remain part of the configured operational workflow; no independent complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: routing and workflow planning concern present task execution, not a distinct prospective environment-scanning/adaptation function.

## S5 — Policy and identity
`—`: human approval and governance configuration are parent authority. The harness does not autonomously own ultimate identity, values or policy.

## Recursion, variety, escalation
Workflow composition adds operational variety, but topology is not metasystem closure. Escalation to human approval remains external/parent-governed.