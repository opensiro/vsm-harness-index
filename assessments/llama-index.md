---
harness_id: llama-index
project_name: LlamaIndex
repository: https://github.com/run-llama/llama_index
review_ref: 7169bcd0dca2e16aecc8e0247f34e50079d9c0d5
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: fd4a517ad6490f0c8464a13fdf133760b696434a
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# LlamaIndex

## Review boundary
LlamaIndex OSS at the pinned revision. LlamaParse/LlamaCloud hosted behavior is not imported unless represented by first-party OSS code in this repository. The previous stored SHA was not resolvable upstream; this deep review explicitly repins the assessment to the current reproducible `main` HEAD shown above.

## Repository architecture
The repository ships `AgentWorkflow` plus general workflow/data/retrieval primitives. First-party multi-agent documentation presents three patterns: built-in handoffs, a top-level orchestrator calling sub-agents as tools, and a custom planner that emits a plan which application code executes.

## Primary evidence
- `docs/src/content/docs/framework/understanding/agent/multi_agent.md`: documents the three supported multi-agent patterns.
- `llama-index-core/llama_index/core/agent/workflow/multi_agent_workflow.py`: `AgentWorkflow` is explicitly a workflow for managing multiple agents with handoffs.
- The multi-agent guide states that `AgentWorkflow` gives control to one active agent, lets that agent hand off control, and repeats until final output.
- The same guide describes the orchestrator pattern as one `FunctionAgent` calling specialist agents as tools, with tools returning control to the orchestrator.

## Operational model
Individual specialist agents can be S1 units. The built-in relations between them are handoff/control transfer or parent-orchestrator delegation. Shared workflow state supports decomposition, but no first-party mutual-adjustment mechanism among peers is established by these patterns.

## S1 — Operations
`A`: first-party agents autonomously choose tools/actions and produce bounded outcomes. Confidence: high.

## S2 — Coordination
`—`: the documented standard multi-agent patterns are handoff routing, agents-as-tools delegation, or application-authored planning. None establishes a material first-party anti-oscillation/mutual-adjustment relation among autonomous S1s. Confidence: high.

## S3 — Inside-and-now control
`?`: an application can compose an orchestrator with shared state, but the generic `FunctionAgent`/tool pattern is not itself a function-specific whole-system regulatory primitive with demonstrated authority over shared resources/commitments.

## S3* — Complementary audit
`?`: examples can include reviewer agents, but a reviewer role inside task flow does not by itself establish sufficiently independent complementary audit plus corrective closure.

## S4 — Outside-and-then intelligence
`?`: retrieval/data access strongly expands informational variety, but the deep pass did not establish a distinct prospective external-intelligence role coupled to S3.

## S5 — Policy and identity
`?`: prompts, root-agent choice and workflow configuration are parent-authored; no runtime ultimate-policy closure was established.

## Recursion, variety, escalation
Workflow nesting, handoffs and agents-as-tools are not counted as VSM recursion without local metasystemic closure.

## Deep-review result
`S2` resolves from `?` to `—`. The remaining unknowns stay unresolved rather than being converted to negative claims without stronger repository-wide evidence.