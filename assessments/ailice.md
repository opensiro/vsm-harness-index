---
harness_id: ailice
project_name: AIlice
repository: https://github.com/myshell-ai/AIlice
review_ref: 63a22105cdf8c0d297af332010f46e4153bbc1ec
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 63a22105cdf8c0d297af332010f46e4153bbc1ec
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

# AIlice

## Review boundary
AIlice at the pinned revision as an autonomous general-purpose agent using the Interactive Agents Call Tree architecture.

## Repository architecture
AIlice recursively decomposes work into dynamically created processors/agents, invokes tools/environment modules and integrates child results back into the calling processor.

## Primary evidence
- `ailice/core/AProcessor.py`: each processor owns the ordinary model/tool loop; `EvalCall` creates or reuses a named subprocessor, forwards a task to it, waits for the result and transfers referenced variables/results between parent and child contexts.
- The pinned processor implementation therefore exposes hierarchical call-tree decomposition and result integration, not an independent organizational regulator or reviewer.

## Operational model
Root and child processors are operational S1 units. Parent-child calls delegate bounded work and aggregate results; nesting does not by itself create metasystemic functions.

## S1 — Operations
`A`: processors autonomously choose tools/subtasks and produce task outcomes inside their delegated scopes. Confidence: high.

## S2 — Coordination
`—`: IACT parent-child delegation and result integration do not establish peer anti-oscillation or shared-resource conflict regulation.

## S3 — Inside-and-now control
`—`: the root processor can decompose and call children, but no reviewed mechanism gives it whole-system resource, priority and accountability authority beyond ordinary task delegation.

## S3* — Complementary audit
`—`: fault handling and child result integration stay on the operational path; no distinct independent reviewer/auditor compares claims against evidence and returns corrective findings.

## S4 — Outside-and-then intelligence
`—`: web/tool use and self-expansion claims remain current-task capabilities at this revision; no separate prospective environmental intelligence loop shapes future organizational posture.

## S5 — Policy and identity
`—`: prompts, modules, permissions and ultimate goals remain parent/runtime supplied.

## Recursion, variety, escalation
Dynamically constructed child processors are nested workers. Recursive viability would require local metasystemic closure that the call tree does not itself provide.