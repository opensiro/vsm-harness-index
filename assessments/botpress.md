---
harness_id: botpress
project_name: Botpress
repository: https://github.com/botpress/botpress
review_ref: 7bf2906580ab86fe647d4fb109b8c3bdcaef9c57
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Botpress

## Review boundary
The first-party LLMz runtime in the Botpress repository at the pinned revision, treated as one deployed production agent loop rather than arbitrary application code built around it.

## Repository architecture
LLMz is a code-first TypeScript agent framework. `execute()` loops until an exit, user wait, or iteration limit; the model generates TypeScript, invokes typed tools in an isolated VM, consumes results, retries errors and preserves variables across iterations. Snapshots, forced/voluntary thinking and lifecycle hooks support the loop.

## Primary evidence
- `packages/llmz/README.md`: LLMz production agent execution, autonomous worker mode, tools, iteration/snapshot/trace behavior.
- `packages/llmz/CLAUDE.md`: one `execute()` loop, code generation/execution pipeline, error recovery, state persistence, snapshots and hooks.
- `packages/llmz/CLAUDE.md`: `onTrace` monitoring, `onExit` validation/guardrails, `onBeforeExecution` security mutation, and `onIterationEnd` state augmentation are caller-supplied lifecycle hooks.

## Operational model
Generated code may orchestrate many tools in one turn, but those tools and subprograms are capabilities within one operational agent. Hook and sandbox infrastructure constrains that operation from outside the agent loop.

## S1 — Operations
`A`: the model-driven loop chooses/generated code and tool actions, incorporates returned values and iterates toward a typed exit. Confidence: high.

## S2 — Coordination
`—`: multi-tool orchestration inside generated code is intra-S1 composition. No first-party mutual-adjustment protocol among autonomous S1 units is supplied. Confidence: high.

## S3 — Inside-and-now control
`—`: iteration limits, sandboxing, error handling and lifecycle hooks constrain one execution loop; they do not constitute an autonomous whole-system regulator over multiple operational units. Confidence: high.

## S3* — Complementary audit
`—`: traces are monitoring and hooks/exit validators are application-provided checks on the normal path. No separate sufficiently independent runtime auditor with alternative reality access and corrective authority is supplied. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: reflection, retries and snapshot/resume adapt current execution but do not establish a distinct external/future-oriented intelligence loop coupled to S3. Confidence: high.

## S5 — Policy and identity
`—`: prompts, hooks, exits, limits and guardrails are parent-authored constraints. No agent-owned ultimate policy/identity closure is supplied. Confidence: high.

## Recursion, variety, escalation
Type schemas and sandbox boundaries attenuate tool/environment variety while generated code amplifies local action variety. Pausing, aborting and snapshots regulate S1 execution without demonstrating recursive viability.