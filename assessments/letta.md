---
harness_id: letta
project_name: Letta
repository: https://github.com/letta-ai/letta-code
review_ref: 5bc853fd6fd69f00c115e320316fa4c0654a3dfb
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Letta

## Review boundary
Letta at the pinned `letta-code` revision. The former `letta-ai/letta` repository now acts as a landing/source-redirect boundary and explicitly points current harness/runtime development to `letta-ai/letta-code`; the deep review therefore follows that first-party source relocation rather than assessing the landing repository as the runtime.

## Repository architecture
Letta Code runs persistent tool-using agents, supports child/subagent execution and includes a built-in background reflection subsystem. Reflection receives completed conversation material in a separate agent context and can update the primary agent's durable memory and reusable skills.

## Primary evidence
- `src/agent/subagents/manager.ts`: first-party subagent process manager supports child launch, parallel/background execution, lifecycle reporting and inherited permission boundaries; these are delegation/runtime mechanics rather than S2 by themselves.
- `src/agent/subagents/builtin/reflection.md`: a distinct background reflection agent explicitly reviews conversations that already happened, prioritizes mistakes/corrections, contradictions and durable learnings, and edits memory/skills for the primary agent.
- `src/cli/helpers/reflection-launcher.ts`: launches, serializes and retries reflection work, maintains a separate reflection worktree and integrates completed reflection changes into the parent memory state.
- `src/cli/helpers/memory-reminder.ts`: default reflection settings use `trigger: "compaction-event"` with `merge: "auto"`, making the reflection path a standard automatic behavior rather than only a user-composed optional reviewer.
- Reflection/subagent tests in the pinned tree exercise built-in reflection prompts, worktree completion/integration and memory-change handling.

## Operational model
The primary coding agent and delegated subagents perform S1 work. Child launch and parallel work are hierarchical delegation. Separately, the reflection agent receives a retrospective view of primary-agent behavior, evaluates it from another context and can commit corrective changes to the state that shapes future primary-agent behavior.

## S1 — Operations
`A`: the primary agent owns model/tool action decisions and can delegate bounded work to first-party subagents. Confidence: high.

## S2 — Coordination
`—`: subagent launch, parallel execution and lifecycle tracking do not establish an autonomous anti-oscillation/shared-resource coordination decision right among peer S1 units.

## S3 — Inside-and-now control
`—`: the subagent manager schedules/delegates tasks but does not own whole-system current priorities, resources and commitments as a superior regulator.

## S3* — Complementary audit
`A`: the default compaction-triggered reflection path launches a distinct autonomous background reviewer over already-completed primary-agent conversations. It searches for mistakes, contradictions and durable corrections and has an automatic integration path into parent memory/skills. This is a separate complementary audit/correction loop rather than ordinary self-reflection inside the S1 turn. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: reflection is retrospective internal learning from the agent's own conversations. It does not establish a distinct outside-and-then environmental intelligence function coupled to strategic adaptation.

## S5 — Policy and identity
`—`: reflection may maintain memory/persona/skills, but ultimate identity, policy and authority remain constrained by parent/runtime configuration; editable memory is not legitimate S5 closure.

## Recursion, variety, escalation
Subagents enlarge operational variety, while reflection supplies a metasystemic audit relation. Neither automatically makes each child a recursively viable system.