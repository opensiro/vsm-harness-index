---
harness_id: n8n
project_name: n8n
repository: https://github.com/n8n-io/n8n
review_ref: 4169b55bf3b3e6c255d7361642bc5243bd04345a
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: cf49003c27c19b2490cf004a8a07429a2035222a
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# n8n

## Review boundary
n8n at the pinned revision, including the first-party AI Agent / Agent Tool / Guardrails surfaces and the first-party Instance AI autonomous orchestrator, planned-task system, workflow verification loop and HITL/runtime controls. Generic deterministic workflow automation remains supporting infrastructure unless primary evidence establishes the relevant VSM function and an owner of its decisive organizational decision right.

## Repository architecture
The AI Agent node performs bounded plan-and-execute work with connected tools/model/memory/output-parser subnodes, and Agent Tool exposes another agent as a callable child. Instance AI adds a stronger repository-level autonomous surface: an orchestrator with explicit planning, direct workflow/data/tool actions, dependency-aware planned tasks, background follow-up runs, checkpoints, workflow verification and task-control paths. Plans are persisted for user approval before execution; build-workflow and checkpoint tasks run as orchestrator follow-ups. The runtime also supplies deterministic dependency scheduling, concurrency limits, cancellation/correction plumbing, verification state machines and HITL suspension/resume.

## Primary evidence
- `packages/@n8n/instance-ai/docs/architecture.md`: Instance AI is explicitly an autonomous orchestrator; planning creates dependency-aware task graphs, build/checkpoint tasks run as orchestrator follow-ups, and the user approves the plan before execution starts.
- `packages/@n8n/instance-ai/src/planned-tasks/planned-task-service.ts`: task graphs validate dependencies, begin in `awaiting_approval`, become active only after user approval, and deterministically cancel downstream dependents after task failure.
- `packages/@n8n/instance-ai/docs/tools.md`: `task-control` exposes checklist, cancellation and correction; `create-tasks` suspends for user plan approval; checkpoints are exceptional orchestrator-executed semantic/cross-workflow checks; workflow verification is a separate deterministic build→verify→debug obligation.
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/Agent.node.ts` and `AgentTool.node.ts`: ordinary AI Agent / child-agent plan-and-execute paths remain bounded operational delegation.
- `packages/@n8n/nodes-langchain/nodes/Guardrails/description.ts`: policy checks/sanitization remain builder-configured constraints on the normal execution path.

## Operational model
At the assessed repository boundary, the autonomous AI Agent / Instance AI loop is S1: it owns bounded planning, tool/action choice and workflow-building outcomes in its task environment. Instance AI can decompose larger work into planned follow-up runs and maintain current task state, but those follow-ups are task executors under one orchestrator plan rather than independently established viable S1 units. Dependency scheduling, concurrency limits, failure cascades, approvals and workflow-loop state machines regulate execution of that work without by themselves establishing metasystem ownership.

## S1 — Operations
`A`: first-party agent loops autonomously plan and execute bounded tool/workflow actions and incorporate returned results. Instance AI further performs autonomous workflow construction, research/tool use and execution-loop decisions. Confidence: high.

## S2 — Coordination
`—`: dependency-aware planned tasks, parallel execution and shared task state are stronger coordination machinery than ordinary workflow edges, but the Profile witness is not established. The inspected boundary does not show two distinct S1 operational units plus a specific inter-S1 oscillation/conflict and a coordination relation dedicated to attenuating it; planned follow-up runs are task decomposition under one orchestrator, and deterministic dependency constraints primarily order that decomposition. Confidence: high.

## S3 — Inside-and-now control
`—`: Instance AI has visibility into its current task graph and can participate in cancellation/correction flows, but the evidence still does not establish whole-system current control across autonomous S1 units with discretion over shared resources, commitments or priorities. Planning, delegation, dependency scheduling and result synthesis remain task execution structure; plan activation is parent-approved, and documented mid-flight correction/cancellation is user steering or deterministic enforcement rather than an autonomous S3 decision right on behalf of a multi-S1 whole. Confidence: high.

## S3* — Complementary audit
`—`: checkpoints and workflow verification provide useful checks, including semantic/cross-workflow validation and build→verify→debug closure, but they run through the same orchestrator/workflow-loop machinery and do not establish sufficiently independent complementary access to operational reality. Guardrails, execution records and ordinary tests remain production-path validation/diagnostics. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: Instance AI can research external information, plan and retain observational memory, but the inspected first-party paths use those capabilities to complete current user work. No separate external-and-prospective adaptation loop is established that develops future options and couples them into present whole-system S3 capability. Confidence: high.

## S5 — Policy and identity
`—`: user approval of a plan, tool/action approvals, permissions, system prompts, workflow topology and guardrail rules constrain current work. They do not form an identity- or ultimate-policy-level decision path at this recursion, so neither autonomous nor parent-governed S5 closure is established. Confidence: high.

## Recursion, variety, escalation
Agent Tool and planned orchestrator follow-ups increase compositional and execution variety but do not by themselves establish recursively viable child systems. Dependency graphs and workflow-loop gates attenuate execution variety; background-task correction, cancellation and HITL provide escalation/control channels. Because the decisive plan-activation and ordinary correction paths can remain with the user, these controls are recorded separately from autonomous metasystem ownership.