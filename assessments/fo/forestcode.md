---
harness_id: forestcode
project_name: ForestCode
repository: https://github.com/hsghcop/ForestCode
review_ref: 406c792be7d365878113a70d2f1feff7aef94e1e
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ForestCode

## Review boundary

- System in focus: the first-party terminal coding harness and its one-level configured subagent runtime.
- Purpose and identity: repository coding and investigation through a model/tool loop with patch-first action approval and session continuity.
- Relevant environment: repository files, operator, DeepSeek/OpenAI-compatible model service, host commands and local runtime state.
- Standard-distribution boundary: installed forestcode CLI, terminal bridge, core loop, tools, runtime factory, memory/skills and configured subagents.
- Credited operating / distribution surfaces: src/forestcode core/runtime/terminal bridge and the shipped mutation gate and subagent model tools. User/project subagent definitions are a supported configuration surface.
- Adjacent first-party surfaces excluded from ownership: tests, build scripts and repository contributor activity; model providers and host shell are dependencies rather than imported organizational actors.
- First-party operating / deployment modes considered: ordinary CLI, optional commands, JSONL session/resume/compaction, selected skills, configured research/verify/edit/full children and manual child selection.
- Recursion level: one parent run with its current operational children.
- Reviewed revision: `406c792be7d365878113a70d2f1feff7aef94e1e`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/README_EN.md) describes the independently implemented model/tool loop, patch-first edits, sessions, memory and one-level children. The actual frozen implementation is broader than an exclusively read-only interpretation: [permission profiles](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/types.py#L252-L273) includes research, verify, edit and full, constrained by parent-visible tools and normal approvals.

[AgentLoop](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/core/agent_loop.py) builds context, requests a model turn, executes calls, returns tool results and records completion/failure. [Terminal bridge](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/terminal/bridge.py#L512-L615) wires a per-parent coordinator, child runner, confirmation bridge and common MutationGate. Each child gets an independent model/context/session/read state and patch service, with internal parent/sibling transcript paths hidden. A bounded FIFO pool tracks queued/running/waiting-approval/cancelling/terminal states. Parent model tools delegate, list, wait and cancel; the scheduler applies selected cancellation and preserves physical slot accounting until the worker exits. Memory/skills configure current context, not automatically future adaptation.

## Operational model

The parent and enabled editing/full children are coding S1 cells; research children supply investigations. Model actors choose operations. The shared mutation gate regulates a specific cross-cell file-write disturbance, but its serialization policy is preselected. The parent model's live child-task view and cancellation authority form a bounded current-control loop over this run's commitments. Operator action confirmations remain ordinary operational vetoes. No complete recursive child viability or higher identity-governance organization is assumed.

## S1 — Operations

- State: A
- Function: investigate and modify repository artifacts in response to user goals and tool observations.
- Disturbance / variety regulated: file contents, command results, rejected actions and coding errors.
- Decisive decision or feedback right: choose the next tool/arguments or final response.
- Decision owner: model-backed parent and configured operational child agents.
- Supporting / enforcement mechanisms: context builder, model router, tool executor, patch service, permission checks, session/memory store and stop policy.
- Closure path: model response becomes executed calls; results enter RunState and the next context/model request.
- Boundary reachability: the installed CLI reaches the terminal bridge's supplied AgentLoop/factory, including child model construction without an external agent runtime.
- Why this is / is not agent-owned: model removal retains enforcement/storage but removes the discretionary repository action strategy.
- Evidence: [Loop and returned tools](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/core/agent_loop.py#L145-L277), [Independent child construction](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/runtime/factory.py#L314-L370).
- Basis: structural.
- Confidence: high.
- Caveats: source availability, not provider performance; mutations remain approval-gated.

## S2 — Coordination

- State: C
- Function: prevent concurrent parent/child writers from computing and applying mutually stale file changes or overlapping mutation approvals.
- Disturbance / variety regulated: two coding cells propose edits against shared workspace state and a later writer silently clobbers an earlier result.
- Decisive decision or feedback right: define single-writer mutation ordering and reject a stale apply; broader discretionary collision-resolution policy remains a composition responsibility.
- Decision owner: developer-selected first-party coordination policy, enforced by a shared runtime gate; no autonomous coordination actor is established for this policy.
- Supporting / enforcement mechanisms: reentrant shared lock across propose → approval → apply/execute and PatchService content-hash stale-write checks.
- Closure path: later mutation sections wait before proposal; stale writes fail instead of overwriting and their tool result returns to the agent for subsequent action.
- Boundary reachability: terminal bridge creates one MutationGate for the run and passes it into parent runtime and child factory; ToolExecutor actually acquires it around the complete mutation section.
- Why this is / is not agent-owned: agents choose coding actions but the serialization response is selected in implementation; removing any putative coordinator model leaves the same gate policy.
- Distinct S1 units: parent coder and concurrent configured edit/full child coders.
- Inter-S1 disturbance: same-workspace competing mutation proposals and stale write application.
- Attenuating coordination relation: one shared mutation critical section plus content-hash rejection.
- Feedback into subsequent S1 behaviour: contenders wait for an up-to-date proposal/approval section or receive a failed stale apply, changing the subsequent edit path.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code explicitly identifies multi-writer clobbering and regulates the actual shared mutation, independently of FIFO task allocation.
- Evidence: [Collision-specific gate](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/tools/mutation_gate.py#L1-L36), [Shared parent/child wiring](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/terminal/bridge.py#L544-L590), [Child gate attachment](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/runtime/factory.py#L387-L395), [Mutation execution](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/core/tool_executor.py#L147-L195).
- Basis: structural.
- Confidence: high.
- Caveats: C is a supplied coordination construction path, not an agent-owned coordination policy or proof of semantic conflict resolution.

## S3 — Inside-and-now control

- State: A
- Function: regulate the parent run's active/queued child commitments through live status and selective intervention.
- Disturbance / variety regulated: work no longer required, failed/pending child commitments, blocked approvals and the bounded shared execution capacity.
- Decisive decision or feedback right: the parent model can inspect all current child snapshots/results, cancel a selected queued/running child and choose subsequent delegation/waiting.
- Decision owner: the parent model agent for discretionary intervention; fixed pool size and watchdog timeouts are developer/runtime enforcement.
- Supporting / enforcement mechanisms: coordinator task snapshots, list/wait/cancel tool wrappers, abort signal, per-child approval-ticket cancellation, FIFO queue and worker lifecycle.
- Closure path: selected queued work is removed immediately; a running/waiting child receives abort, late results are discarded, and cancellation/status returns through the model-visible tools. Actual worker exit governs slot release before new work proceeds.
- Boundary reachability: terminal bridge wires the coordinator and exposes its model tools in the same parent run; the ordinary model/tool loop receives their returned snapshots.
- Why this is / is not agent-owned: the runtime cannot choose which otherwise valid child commitment the whole run should abandon; the model chooses that intervention and the scheduler enforces it.
- Whole-system current view: all child tasks of this parent run, queue positions, status, results/errors and approval-wait/cancel state.
- Current-control decision scope: continue or curtail the run's current subordinate commitments; not just initial task decomposition, and not autonomous selection of max_workers or ultimate policy.
- Evidence: [Model-visible view and intervention](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/tools.py#L199-L240), [Actual cancellation effects](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/coordinator.py#L396-L457), [Tool wiring](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/terminal/bridge.py#L592-L610), [Completion/cancellation return](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/coordinator.py#L604-L654).
- Basis: structural.
- Confidence: medium.
- Caveats: narrow run-relative control, cooperative cancellation and bounded telemetry; not a claim of hard process kill, resource optimization or parent-human S3 governance.

## S3* — Complementary audit

- State: —
- Function: no material first-party path for this function at the declared run boundary.
- Disturbance / variety regulated: Separate child contexts hide parent/sibling transcripts and the verify profile can expose command execution, but no built-in auditor is assigned an independent claim-challenging relation with mandatory or optional audit return as such.
- Decisive decision or feedback right: none evidenced for the specific higher function.
- Decision owner: not established; operational model/developer/operator rights are kept separate.
- Supporting / enforcement mechanisms: generic tools, configuration, persistence and event transport do not inherit this function.
- Closure path: operational result feedback exists, without the distinct function-specific loop.
- Why this is / is not agent-owned: absence concerns the organizational relation before ownership grading.
- Evidence: [src/forestcode/subagents/types.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/types.py#L252-L273), [src/forestcode/runtime/factory.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/runtime/factory.py#L276-L288), [src/forestcode/subagents/tools.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/tools.py#L1-L17).
- Basis: structural.
- Confidence: medium.
- Caveats: bounded absence, not a claim that an external/custom organization could never add the function.

### Absence scope

- Surfaces inspected: child profiles, independent factory, delegate/wait tools, session/memory recording and tests.
- Plausible first-party paths checked: verify profile, research findings, direct file reads, logs and test/build pipeline.
- Why no material first-party path remains: Generic configurable child instructions could be composed into an auditor, but the inspected distribution supplies no material audit-specific owner/independence/claim-to-finding-control path. The verify permission label and ordinary coding tests do not establish S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path for this function at the declared run boundary.
- Disturbance / variety regulated: Long-term memory, session summarization, skills and provider overrides assemble/recover current context. They do not by themselves produce prospective adaptation options from external environmental distinctions.
- Decisive decision or feedback right: none evidenced for the specific higher function.
- Decision owner: not established; operational model/developer/operator rights are kept separate.
- Supporting / enforcement mechanisms: generic tools, configuration, persistence and event transport do not inherit this function.
- Closure path: operational result feedback exists, without the distinct function-specific loop.
- Why this is / is not agent-owned: absence concerns the organizational relation before ownership grading.
- Evidence: [README_EN.md](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/README_EN.md), [src/forestcode/core/agent_loop.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/memory/manager.py), [src/forestcode/runtime/factory.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/runtime/factory.py#L324-L370).
- Basis: structural.
- Confidence: medium.
- Caveats: bounded absence, not a claim that an external/custom organization could never add the function.

### Absence scope

- Surfaces inspected: memory manager/compaction architecture, child/model configuration, skills and README operating modes.
- Plausible first-party paths checked: learning from sessions, skill loading, model override, project rules and operator configuration.
- Why no material first-party path remains: No shipped external/future sensing plus adaptation judgment and return into current capability is established. Local memory writes and extension points do not supply autonomous, constructor or parent-governed S4 closure.

## S5 — Policy and identity

- State: —
- Function: no material first-party path for this function at the declared run boundary.
- Disturbance / variety regulated: Permissions, tool visibility and confirmation requests bound coding actions. Parent cancellation controls current work, while user approval authorizes an individual edit/command; neither is an identity/ultimate-policy issue.
- Decisive decision or feedback right: none evidenced for the specific higher function.
- Decision owner: not established; operational model/developer/operator rights are kept separate.
- Supporting / enforcement mechanisms: generic tools, configuration, persistence and event transport do not inherit this function.
- Closure path: operational result feedback exists, without the distinct function-specific loop.
- Why this is / is not agent-owned: absence concerns the organizational relation before ownership grading.
- Evidence: [README_EN.md](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/README_EN.md), [src/forestcode/subagents/types.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/subagents/types.py#L279-L301), [src/forestcode/runtime/factory.py](https://github.com/hsghcop/ForestCode/blob/406c792be7d365878113a70d2f1feff7aef94e1e/src/forestcode/runtime/factory.py#L373-L395).
- Basis: structural.
- Confidence: medium.
- Caveats: bounded absence, not a claim that an external/custom organization could never add the function.

### Absence scope

- Surfaces inspected: CLI/operator confirmations, parent and child tool composition, runtime factory, project/user settings and rules.
- Plausible first-party paths checked: patch approval, command enablement, configured child instructions/permissions and cancellation.
- Why no material first-party path remains: No identity/ultimate-policy matter is routed to a legitimate authority and returned as binding governance at the session recursion. Static rules and ordinary human action consent are not a first-party P mode.

## Distributed OSS parent arrangement

Users run local configured agents; repository maintainers develop the package. No wider OSS parent function is borrowed into those sessions. Concrete action approvals are evaluated at their operational level without automatic P notation.

## Self-hosted and non-human modes

Local CLI, optional commands and one-level configured child profiles are included. Configured edit/full profiles are recognized from code even though high-level material emphasizes independent/read-focused children. Generic human confirmation does not add S3/S4/S5 parent closure.

## Recursion

Independent child object graphs and sessions are real operational separation; one-level nesting does not establish full child viable-system recursion.

## Variety and escalation

Model/tool results, child snapshots and terminal events carry current variety. Timed waits do not cancel; explicit cancellation moves through cancelling until physical completion, and late results are discarded. Approval/abort/error mechanisms bound operational recovery without proving identity policy or an algedonic channel.

## Evidence gaps

Frozen source compileall and 18 native offline subagent permission/mutation/approval-cancellation tests passed. The host uses Python 3.12 although packaging declares >=3.13; a supported-version install/build and live provider or terminal tasks were not run. No source ref was changed. Causal performance/viability, complete semantic merge safety and guaranteed cooperative abort latency are not established. Parent current-control is limited to this run's commitments, not a whole organization.
