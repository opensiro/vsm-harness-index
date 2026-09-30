---
harness_id: truecoder
project_name: TrueCoder
repository: https://github.com/Shivam583-hue/TrueCoder
review_ref: 0db47102068596eccaf26d16a6c4eb0f24936a8a
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TrueCoder

## Review boundary

- System in focus: the first-party `Shivam583-hue/TrueCoder` terminal coding-agent harness at frozen revision `0db47102068596eccaf26d16a6c4eb0f24936a8a`, including its model/tool agent loop, built-in coding tools, planning and memory stores, checkpoint and restore machinery, approval/mode enforcement, execution control plane, mutation audit, MCP/LSP integrations, and bounded delegation path where they bear on organizational function.
- Purpose and identity: execute coding tasks inside one project workspace by reading/searching code, planning work, editing files, running approved commands, consulting bounded external documentation, and optionally delegating a bounded side task to a fresh subagent.
- Relevant environment: the selected project workspace and git state, user task and approvals, project instructions, model/provider responses, shell/runtime capabilities and limits, MCP/LSP services, public web documentation reached by `web_fetch`, and persistent session/memory state.
- Standard-distribution boundary: the shipped `truecoder` CLI/TUI, `Agent`, built-in tools, execution/checkpoint/session/memory/planning/audit machinery, first-party subagent constructor, and shipped configuration loaders are inside. Model/provider inference, external MCP servers, language servers, Docker/host operating system, public websites, and the target repository's own policy are dependencies/environment rather than TrueCoder organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `docs/ARCHITECTURE.md`; `src/truecoder/agent/agent.py`; `src/truecoder/agent/mode.py`; `src/truecoder/tools/builtin/delegate.py`; `src/truecoder/tools/builtin/plan.py`; first-party execution, checkpoint, memory, mutation-audit, session, hook and tool surfaces reached by the normal CLI/TUI session.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests; offline `evaluation/` task scoring; release/install machinery; contributor governance; provider implementation internals; operator-authored `AGENTS.md`, hook configuration, MCP configuration and approval decisions except as evidence of an external control boundary.
- First-party operating / deployment modes considered: interactive and one-shot coding runs; Plan, Build and Full Access modes; normal approved mutation/shell execution; project-scoped sessions/memory/checkpoints; MCP/LSP augmentation; and the standard synchronous `delegate` path.
- Recursion level: one TrueCoder coding organization around one project/task. The main model-backed `Agent` is the primary operating S1. A delegated fresh agent can become a bounded subordinate S1 for a side task, but its existence alone does not establish S2 or S3.
- Reviewed revision: `0db47102068596eccaf26d16a6c4eb0f24936a8a`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

TrueCoder ships a standard model/tool coding loop. `Agent.run()` captures a checkpoint for change-capable modes, compacts context when necessary, opens a turn and enters `_agentic_loop()`. Each iteration builds context, calls the selected external model, executes returned tool calls, records results and feeds them into the next model request until the model returns a final answer or a deterministic limit/stall condition stops the turn. The standard `build_session()` wires file/search/edit/web/code-intelligence tools, planning, checkpoints, durable memory, mutation audit, execution policy, MCP and the `delegate` tool into that loop.

The harness also has a bounded delegation path. `DelegateTool` hands one self-contained task to a fresh `Agent` that shares the project workspace but not the parent's conversation. The child inherits the active mode and approval handler, receives only a restricted first-party file/search/edit tool registry, cannot delegate again, and returns only its final reply/tool-call count. This delegation is awaited synchronously by the parent tool invocation. The parent agent's own tool-call executor likewise iterates requested calls one by one, so the reviewed standard path does not create concurrently active TrueCoder S1 workers that need a coordination relation.

Planning, progress monitoring, checkpoints, mutation audit, approvals and execution policy are substantial safety/operability mechanisms but do not by themselves create additional VSM functions. `update_plan` replaces the current task's whole step list; repeated/no-progress calls trigger deterministic stall handling; checkpoints make workspace changes reviewable/restorable; modes and approval gates constrain tools according to operator-selected policy. None of those surfaces establishes a first-party whole-organization management actor, independent audit role, prospective strategy loop or identity-policy owner.

Primary evidence:

- [`README.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/README.md)
- [`docs/ARCHITECTURE.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/docs/ARCHITECTURE.md)
- [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py)
- [`src/truecoder/agent/mode.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/mode.py)
- [`src/truecoder/tools/builtin/delegate.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/delegate.py)
- [`src/truecoder/tools/builtin/plan.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/plan.py)

## Operational model

A normal TrueCoder session receives an operator task, combines it with workspace/project context and available tool definitions, and lets the model-backed agent choose the next coding action. Tool calls are prepared against the first-party registry, checked against the active mode, approval-gated where necessary, executed through bounded first-party machinery and returned to the same agent loop. The agent can revise its task plan, persist workspace notes, inspect diagnostics or public documentation, mutate files, run allowed shell commands and inspect the resulting feedback before choosing another action.

A delegation call is a nested operational path rather than a persistent multi-agent organization. The parent selects a bounded subtask and iteration budget, then waits while a fresh child agent executes against the same workspace under inherited mode/approval constraints. Only the child's final reply crosses back. The reviewed distribution does not expose a standard parallel team scheduler, shared-work arbitration loop or ongoing multi-S1 controller around those agents.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected project by interpreting the user task, inspecting code/environment evidence, choosing and executing coding tools, observing results and iterating toward a final answer/change.
- Disturbance / variety regulated: heterogeneous repository structure and code, incomplete task information, compiler/LSP diagnostics, command results, provider responses, tool failures, changing workspace state and implementation choices encountered while completing the requested coding task.
- Decisive decision or feedback right: choose which available tool/action to invoke next, what code/files/evidence to inspect or modify, how to revise the current task plan, and when sufficient evidence/work exists to return a final answer within the externally supplied mode/policy boundary.
- Decision owner: the model-backed first-party `Agent` role instantiated by TrueCoder's standard session and driven through its shipped prompt/context/tool loop.
- Supporting / enforcement mechanisms: context builder; project instructions; planning and memory stores; file/search/edit/web/LSP tools; execution service; checkpoints; progress monitor; mode/approval checks; mutation audit; session state and context compaction.
- Closure path: user task and workspace state enter the standard session → TrueCoder builds model context/tool surface → the agent chooses an action → first-party policy/approval machinery executes or rejects it → result/workspace feedback is recorded into the turn → the same agent receives that feedback and chooses the next action or terminates with a final response.
- Boundary reachability: `truecoder`/`python -m truecoder` reaches `build_session()` and the shipped `Agent`/tool loop directly; an application author does not need to construct a separate orchestration layer to obtain the coding S1.
- Why this is / is not agent-owned: removing the model-backed `Agent` decision loop leaves useful deterministic safety, persistence and tool primitives but removes the open-ended coding judgment that selects and sequences environment-facing work.
- Evidence: [`README.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/README.md); [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py); [`src/truecoder/tools/builtin/plan.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/plan.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference remains an external dependency; the assessment credits TrueCoder for the standard first-party role/context/tool/runtime path that operationally closes the loop, not for provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party coordination loop was established that attenuates concrete interference or oscillation among simultaneously active TrueCoder S1 units.
- Disturbance / variety regulated: not established at S2 level.
- Decisive decision or feedback right: not established. The standard delegate path creates a bounded subordinate agent but awaits it synchronously; main-agent tool calls are executed sequentially. No first-party actor or S2-specific deterministic relation was found arbitrating contested work among concurrent TrueCoder S1s.
- Decision owner: not established.
- Supporting / enforcement mechanisms: delegation depth/iteration bounds, inherited mode/approval handling, mutation audit, atomic/concurrent-change-safe file tooling and sequential tool execution are safety/execution mechanisms rather than a demonstrated inter-S1 coordination loop.
- Closure path: not applicable; the reviewed standard path does not expose the required inter-S1 disturbance-and-attenuation cycle.
- Why this is / is not agent-owned: a fresh delegated agent is a real subordinate S1, but multiplicity/delegation alone is insufficient. The parent waits for the child and consumes its report; there is no established cross-worker interference relation whose feedback changes ongoing S1 behavior.
- Evidence: [`src/truecoder/tools/builtin/delegate.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/delegate.py); [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py); [`docs/ARCHITECTURE.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/docs/ARCHITECTURE.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: file tools defend against unsafe/stale mutation, but coordination with external processes/users is not an inter-S1 VSM witness.

### Absence scope

- Surfaces inspected: main agent loop and tool-call executor; `delegate` tool and subagent constructor; mutation-audit/file-mutation path; progress monitoring; execution/mode/approval surfaces; architecture documentation and standard session wiring.
- Plausible first-party paths checked: parent/child delegation; multiple model tool calls in one turn; shared-workspace mutation handling; execution cancellation and audit state; persistent session/memory state; MCP/LSP augmentation.
- Why no material first-party path remains: delegated work is synchronously awaited and one level deep, ordinary tool calls are executed sequentially, and the located shared-state safeguards do not implement a feedback relation among simultaneously active first-party S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-regulation function was established beyond the operating agent's own task execution and deterministic enforcement of externally selected limits/modes.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. The parent agent can create a bounded side task and revise its own current plan, but no distinct whole-system actor has a current organization-wide view plus substantive authority to revise shared resources, commitments, priorities or constraints across S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: current-task plan store, max-iteration bounds, stall detection, checkpoints, cancellation, execution limits, approval policy and mode restrictions.
- Closure path: not applicable; observed paths either belong to S1 task execution or enforce operator/configuration policy mechanically.
- Why this is / is not agent-owned: delegation/task planning is operational orchestration, not sufficient evidence of S3. The model-backed parent does not receive or exercise a separate organization-wide regulatory mandate over a persistent multi-S1 system.
- Evidence: [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py); [`src/truecoder/tools/builtin/plan.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/plan.py); [`src/truecoder/tools/builtin/delegate.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/delegate.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the main agent is operationally capable and can sequence work; this absence concerns the stronger S3 organizational-control threshold, not generic orchestration.

### Absence scope

- Surfaces inspected: task planning; delegation; progress/stall handling; iteration limits; checkpoint/change handling; execution policy and cancellation; approval/mode logic; session state and architecture documentation.
- Plausible first-party paths checked: parent-agent task allocation; whole-list plan replacement; subagent iteration budgeting; current progress feedback; resource/shell ceilings; operator mode changes; resume/restore state.
- Why no material first-party path remains: located control decisions either govern the agent's own S1 task, are fixed/operator-supplied constraints, or are deterministic runtime enforcement. No separate whole-current organizational controller with substantive reallocation/commitment authority was found.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit function with sufficiently independent access and a corrective return into later organizational control was established in the standard runtime.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Checkpoints, mutation audit, execution evidence, LSP diagnostics, hooks and offline evaluation record or inspect behavior but do not constitute an independent runtime challenger authorized to judge ordinary S1 conclusions and return that judgment into control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: immutable mutation/execution records, checkpoints/diffs, diagnostics, hooks and offline evaluation tasks.
- Closure path: not applicable; no standard independent challenge → verdict → corrective-control return loop was found.
- Why this is / is not agent-owned: a delegated agent can perform a user/model-selected side investigation, but TrueCoder does not ship that path as a distinct complementary audit role with independence and mandatory/standard corrective return. Audit logs preserve evidence rather than own judgment.
- Evidence: [`README.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/README.md); [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py); [`docs/ARCHITECTURE.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/docs/ARCHITECTURE.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strong observability/auditability is not itself the S3* organizational function.

### Absence scope

- Surfaces inspected: mutation audit; execution evidence; checkpoints and restore; diagnostics/LSP; hooks; delegate path; offline evaluation; architecture/runtime documentation.
- Plausible first-party paths checked: post-change review evidence; hook outcomes; diagnostics; child-agent reports; checkpoint comparison; evaluation scoring; durable audit records.
- Why no material first-party path remains: the located mechanisms record, enforce or assist ordinary S1 work, but no sufficiently independent first-party reviewer is assigned a complementary challenge mandate whose verdict feeds a later current-control decision.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party prospective environment-intelligence and organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. The operating agent can inspect public documentation via `web_fetch`, query code intelligence, revise the current task plan and remember workspace notes, but those are information/action capabilities inside the present coding task rather than authority to model future environmental change and alter organizational capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `web_fetch`, code intelligence, memory, context compaction, project instructions and current-task `update_plan`.
- Closure path: not applicable; no prospective scan → option formation → capability/strategy change → return-to-present organization path was found.
- Why this is / is not agent-owned: the S1 can adapt its immediate coding behavior to newly observed information. Methodology 0.3.6 requires the stronger organizational S4 function; current-task replanning and durable memory do not satisfy it alone.
- Evidence: [`README.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/README.md); [`src/truecoder/tools/builtin/plan.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/tools/builtin/plan.py); [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external web access establishes an information channel, not by itself a prospective organizational-intelligence function.

### Absence scope

- Surfaces inspected: web/document retrieval; LSP/code intelligence; plan revision; durable memory; context compaction; provider/model selection; MCP extension; project instructions; architecture and feature documentation.
- Plausible first-party paths checked: external documentation lookup; current-task replanning; learning/persistence across turns; changing model/provider; adding MCP tools; project-local remembered notes.
- Why no material first-party path remains: all located adaptation is current-task/operator-configured capability use. No shipped actor continuously or episodically models future environment, forms strategic alternatives and feeds an organizational capability/strategy change back into the running organization.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party ultimate identity/policy closure was established.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Agent modes, hard execution policy, project instructions, credentials, hooks, approvals and resource ceilings constrain behavior, but their authoritative values are selected by the user/configuration/runtime rather than autonomously owned as the organization's identity or ultimate policy.
- Decision owner: not established inside the assessed organization; ultimate constraints remain operator/configuration owned.
- Supporting / enforcement mechanisms: Plan/Build/Full Access modes, approval service, execution-policy configuration, workspace containment, project instructions, hook/MCP configuration and hard resource/isolation boundaries.
- Closure path: not applicable; TrueCoder enforces selected policy but does not itself close the decision over what the organization's ultimate purpose/identity/policy should be.
- Why this is / is not agent-owned: the model-backed S1 operates under the selected mode and policy. Even Full Access explicitly remains subject to hard execution-policy denials, isolation/resource limits and project boundaries; enforcement does not transfer policy ownership to the agent.
- Evidence: [`src/truecoder/agent/mode.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/mode.py); [`src/truecoder/agent/agent.py`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/src/truecoder/agent/agent.py); [`README.md`](https://github.com/Shivam583-hue/TrueCoder/blob/0db47102068596eccaf26d16a6c4eb0f24936a8a/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this assessment distinguishes strong policy enforcement from ownership of the ultimate policy decision.

### Absence scope

- Surfaces inspected: agent modes; approval service; execution-policy/bootstrap configuration; project/workspace boundary; AGENTS/project instructions; hooks/MCP configuration; model/provider selection; runtime hard limits.
- Plausible first-party paths checked: mode switching; automatic approval in Full Access; system prompt guidance; hard execution denials; project instruction loading; provider/model selection; remembered configuration.
- Why no material first-party path remains: the reviewed distribution supplies mechanisms for selecting and enforcing policy, but the authoritative policy/identity choices originate from operator/configuration boundaries and are not delegated to a first-party autonomous S5 actor.

## Assessment summary

TrueCoder closes a strong first-party coding S1: the standard product directly instantiates a model-backed agent that chooses and executes software-engineering actions and incorporates tool/environment feedback. Its additional machinery materially improves safety, persistence and usability, but under Profile 0.2.4 / Methodology 0.3.6 it does not establish further VSM functions. Delegation is bounded and synchronous rather than an S2 coordination loop; planning/delegation do not create S3; audit/checkpoint/evaluation surfaces do not create an independent S3* challenge path; web/memory/replanning do not create prospective S4; and operator-selected modes/policies do not transfer S5 ownership.

Proposed vector: **`A · — · — · — · — · —`**.
