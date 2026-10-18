---
harness_id: agent-zero
project_name: Agent Zero
repository: https://github.com/agent0ai/agent-zero
review_ref: b1cbd1f960a1a5c4482b324dcff4742aa67b7a51
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: b1cbd1f960a1a5c4482b324dcff4742aa67b7a51
last_checked_at: 2026-09-17
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

# Agent Zero

## Review boundary
Agent Zero at the pinned revision as an open agent framework with computer/browser/document tools, persistent contexts and focused subordinate delegation.

## Repository architecture
Agent Zero gives agents a Linux desktop, browser, files/projects/memory, skills/plugins and host bridge. A parent can create or continue named subordinate contexts, run subordinates in parallel, await/cancel them and integrate their returned results.

## Primary evidence
- `tools/call_subordinate.py`: creates parent-linked subordinate contexts, assigns one task, runs the child's monologue and returns the result to the parent; continuing/resetting children remains parent-controlled delegation.
- `helpers/parallel_tools.py` and `tools/parallel.py`: parallel jobs can include subordinate calls and support await/collect/cancel lifecycle control.
- `prompts/agent.system.tool.call_sub.md`: subordinates are recommended for specialized tasks and independent perspectives, but this remains generic task delegation rather than a dedicated metasystem role.

## Operational model
The principal and subordinate agents are S1 work units. Parent→child task assignment, persistence and parallel job lifecycle expand operational capacity without establishing a separate team-wide regulator or peer coordination function.

## S1 — Operations
`A`: agents autonomously operate tools/computer resources toward outcomes. Confidence: high.

## S2 — Coordination
`—`: children are delegated work by a superior and return results; no distinct mutual-adjustment/collision-regulation relation among S1 units is established.

## S3 — Inside-and-now control
`—`: subordinate creation, continuation, await/cancel and project context are delegation/runtime controls, not autonomous whole-system regulation of commitments/resources.

## S3* — Complementary audit
`—`: a subordinate can be prompted for review or an independent perspective, but the generic delegation tool does not supply a distinct first-party audit function with its own corrective authority.

## S4 — Outside-and-then intelligence
`—`: memory, web access, scheduling and plugins do not establish a distinct prospective intelligence loop coupled back to S3.

## S5 — Policy and identity
`—`: profiles, prompts, projects, tools and settings remain user/developer controlled.

## Recursion, variety, escalation
Subordinates can nest operational work, but hierarchy and nested contexts alone are not recursive viable-system closure.