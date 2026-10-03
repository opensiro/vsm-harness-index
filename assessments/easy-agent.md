---
harness_id: easy-agent
project_name: Easy Agent
repository: https://github.com/vietor/easy-agent
review_ref: f13207671ad142fb89d1c36d413f7e42d60b18a6
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Easy Agent

## Review boundary

- System in focus: the shipped Easy Agent terminal coding organization at frozen revision `f13207671ad142fb89d1c36d413f7e42d60b18a6`, including `@vietor/agent-core` agent/session runtime, built-in coding tools, nested SubAgent execution, todo/context/session machinery and the CLI that wires those surfaces.
- Purpose and identity: autonomously complete coding tasks in a local project while allowing the main agent to delegate independent exploration/planning/implementation chunks to bounded child agents.
- Relevant environment: user requests, repository/filesystem state, shell/web/tool results, model-provider responses, child-agent reports, todos, skills and persistent session state.
- Standard-distribution boundary: core runtime, bundled tools/subagent machinery and CLI session wiring are inside. LLM-provider internals, external MCP servers, target-project governance and repository development/CI are outside.
- Credited operating / distribution surfaces: `README.md`; `packages/core/src/runtime/agent.ts`; `packages/core/src/runtime/sub-agent-runner.ts`; `packages/core/src/tools/sub-agent.ts`; `packages/core/src/tools/registry.ts`; session persistence and CLI session-resolution surfaces where they affect the same runtime.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI and publishing workflow; CLI presentation logic; examples and development assertions that are not wired into runtime.
- First-party operating / deployment modes considered: ordinary writable coding session; read-only sessions; Explore/Plan/General subagents; nested subagents within configured depth; parallel tool/subagent batching; persisted/resumed CLI sessions.
- Recursion level: one user/project mission. The main model/tool loop is an S1; independently running child agents are additional bounded S1 units when they perform delegated exploration, planning or implementation work.
- Reviewed revision: `f13207671ad142fb89d1c36d413f7e42d60b18a6`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`Agent` owns the main model/tool feedback loop, context compaction, todo reminders, tool batching, stall handling and execution limits. It groups only tools marked concurrency-safe into parallel batches and otherwise serializes calls. `SubAgent` is itself marked concurrency-safe, so one model turn may fan out multiple children. Each child receives a new `SessionMessages`, filtered tool set, its own agent loop/turn budget and optional nested SubAgent tool until the configured depth ceiling.

The subagent contract is role-specific. Explore and Plan are read-only. General may edit and run shell commands. The main-agent guidance explicitly requires parallel General children to receive disjoint file/module areas and forbids overlapping edits; the General child prompt reciprocally tells each child that sibling agents may be running and not to touch files in sibling-assigned areas. Returned child reports are tool results for the parent, and file-changing delegated work must be independently rechecked by the parent before it is reported complete.

That last recheck requirement is useful reliability guidance but is not an independent S3* auditor: the same main actor that delegated and integrates the work is the one instructed to re-read/run tests. No separate verifier role or complementary access owner was found.

## Operational model

The main agent chooses tools and delegation based on current task variety. Parallel subagents are semantically scoped by the parent: the model chooses independent/disjoint chunks, includes those boundaries in each child task, and later consolidates the returned reports. The runtime supplies concurrency, depth/budget/tool ceilings and child isolation at the conversation level, but it does not itself infer semantic file conflicts.

## S1 — Operations

- State: A
- Function: perform environment-facing coding work by interpreting the user task, reading/searching project state, editing files, executing shell/web tools and reacting to returned results.
- Disturbance / variety regulated: heterogeneous codebases, command/test failures, incomplete information, model/tool errors, implementation choices and changing project state.
- Decisive decision or feedback right: choose the next substantive tool/action, interpret observations, revise the approach and decide when to delegate or report.
- Decision owner: the model-backed Easy Agent actor; bounded child agents own the corresponding local decision right within delegated scope.
- Supporting / enforcement mechanisms: `Agent` loop; ToolRegistry; run limits; context compaction; session messages/persistence; built-in file/shell/web tools; stall detection.
- Closure path: user/project state → model call → chosen tool/subagent → runtime executes or rejects → result is appended → later model call changes subsequent operation.
- Boundary reachability: the published CLI wires the core `Agent` and bundled tools directly; SubAgent forks the same first-party loop.
- Why this is / is not agent-owned: removing the model actor leaves execution/storage machinery but removes open-ended judgment over coding actions and evidence.
- Evidence: [`packages/core/src/runtime/agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/agent.ts); [`packages/core/src/runtime/sub-agent-runner.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/sub-agent-runner.ts); [`README.md`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: runtime budgets/concurrency ceilings constrain autonomy but do not own the operational decision.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among simultaneously delegated coding S1s by assigning non-overlapping file/module scopes before concurrent execution.
- Disturbance / variety regulated: parallel writable General subagents sharing one working tree can edit the same files/areas and overwrite or invalidate one another's work.
- Decisive decision or feedback right: decide which branches of work are sufficiently independent to run concurrently and assign each writable child a disjoint file/module scope.
- Decision owner: the main model-backed Easy Agent actor.
- Supporting / enforcement mechanisms: model-visible SubAgent tool; concurrent-safe SubAgent batching; per-child independent conversation/tool loop; configured parallelism/depth budgets; role prompts that carry the assigned scope into each child.
- Closure path: main actor identifies independent branches → emits multiple SubAgent calls with disjoint scopes → each child's prompt binds it to its assigned area and warns against sibling areas → children perform later actions within those scopes → reports return to the parent for consolidation.
- Boundary reachability: SubAgent is a bundled model-visible tool and multiple SubAgent calls in one turn are explicitly executed concurrently by the shipped `Agent.runToolCalls` path.
- Why this is / is not agent-owned: the runtime can run calls concurrently but does not know which semantic file areas conflict. Removing the parent model removes the discretionary non-overlap assignment that attenuates the identified edit disturbance.
- Evidence: [`packages/core/src/tools/sub-agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/tools/sub-agent.ts); [`packages/core/src/runtime/agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/agent.ts); [`packages/core/src/runtime/sub-agent-runner.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/sub-agent-runner.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: no filesystem worktree/lock enforces semantic disjointness; this state credits the parent agent's explicit scope-assignment decision and returned child contract, not the generic concurrency primitive.
- Distinct S1 units: multiple General child agents, or the main coding actor plus a General child, each running an independent model/tool loop and capable of modifying the shared project.
- Inter-S1 disturbance: overlapping concurrent edits in sibling-assigned areas can race or invalidate shared working-tree state.
- Attenuating coordination relation: parent assigns disjoint file/module scopes; General child instructions require staying out of sibling-assigned areas.
- Feedback into subsequent S1 behaviour: assigned scope is included in each child's standalone task/system contract and therefore constrains its subsequent file/tool actions; results return to the parent for integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation explicitly addresses parallel write interference and prescribes non-overlapping operational territories, rather than counting delegation/fan-out alone.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established at the declared recursion.
- Disturbance / variety regulated: not established at S3 level.
- Decisive decision or feedback right: no actor was found with a persistent whole-system view of running S1 commitments plus authority to reprioritize, stop or steer those commitments after delegation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: todo reminders; run/turn limits; subagent concurrency budget; stall detection; nested-depth ceiling; parallel tool batching.
- Closure path: not applicable; these fixed bounds and local reminders do not close whole-system current-control decisions over active S1s.
- Why this is / is not agent-owned: the main agent chooses initial delegation and later integrates final reports, but launch/decomposition/merge alone are not S3.
- Evidence: [`packages/core/src/runtime/agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/agent.ts); [`packages/core/src/runtime/sub-agent-runner.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/sub-agent-runner.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: synchronous completion of parallel SubAgent calls gives the parent returned results but no live intervention path over the running child set.

### Absence scope

- Surfaces inspected: Agent loop, todo/stall logic, SubAgent runner/budget/depth, concurrent tool batching, session state and CLI session persistence.
- Plausible first-party paths checked: active task registry, whole-system current status, resource/priority negotiation, live stop/steer/retry of children and exception-based intervention over current commitments.
- Why no material first-party path remains: no shipped runtime surface was found that exposes running child commitments to an S3 owner for discretionary intervention after launch.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent first-party complementary audit loop was established.
- Disturbance / variety regulated: not established through an independent audit owner/path.
- Decisive decision or feedback right: not established outside the ordinary main-agent path.
- Decision owner: not established.
- Supporting / enforcement mechanisms: child self-verification guidance; parent instruction to re-read diffs/run tests after file-changing delegation; tool results and saved child reports.
- Closure path: not applicable as S3*; ordinary parent verification remains inside the same decision path that delegated and integrates the work.
- Why this is / is not agent-owned: a model may verify its own/child work, but no separate verifier identity, independent access path or constructor-owned complementary verdict was found.
- Evidence: [`packages/core/src/tools/sub-agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/tools/sub-agent.ts); [`packages/core/src/runtime/sub-agent-runner.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/sub-agent-runner.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: “verify important results yourself” is reliability guidance, not sufficient S3* independence.

### Absence scope

- Surfaces inspected: Explore/Plan/General role definitions, child-report handling, parent verification guidance, todos/stall logic and core tests.
- Plausible first-party paths checked: dedicated reviewer/verifier child, independent test/audit executor whose verdict controls continuation, second-channel workspace inspection and independent audit-to-correction closure.
- Why no material first-party path remains: the shipped roles do not include a verifier/auditor, and the required recheck is performed by the same parent path that owns ordinary integration.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop was established at the selected mission recursion.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Web fetch, skills, context compaction, session persistence and past-session resume support future work but do not form an external/prospective adaptation function.
- Decision owner: not established.
- Supporting / enforcement mechanisms: WebFetch; skills; persisted session JSONL; notes/report files; compaction.
- Closure path: not applicable; no external/future distinction → adaptation option → persistent capability/S3 change loop was established.
- Why this is / is not agent-owned: retaining information or resuming a session is not by itself S4.
- Evidence: [`README.md`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/README.md); [`packages/core/src/runtime/agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/agent.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: application developers can compose additional intelligence around the SDK; that is outside the standard-distribution closure.

### Absence scope

- Surfaces inspected: session persistence/resume, skills, WebFetch, compact/notes behavior, subagents and tool registry.
- Plausible first-party paths checked: environmental forecasting, durable self-improvement, future strategy revision, automatic capability/model/tool changes and return of selected adaptation into current organization.
- Why no material first-party path remains: located mechanisms preserve context or expose reusable procedures but do not select and apply prospective organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established at the mission recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. System prompts, tool levels, project instructions and CLI configuration constrain execution without a runtime identity/ultimate-policy resolution loop.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: agent-level tool filtering; read-only session restrictions; system/subagent prompts; skills and project instruction loading; CLI configuration.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → returned governance decision loop was established.
- Why this is / is not agent-owned: static instructions and capability ceilings are enforcement/configuration rather than S5 ownership.
- Evidence: [`packages/core/src/tools/sub-agent.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/tools/sub-agent.ts); [`packages/core/src/runtime/sub-agent-runner.ts`](https://github.com/vietor/easy-agent/blob/f13207671ad142fb89d1c36d413f7e42d60b18a6/packages/core/src/runtime/sub-agent-runner.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: external/project governance may configure the harness, but generic configuration is not a positive S5 parent mode.

### Absence scope

- Surfaces inspected: core/system/subagent prompts, agent-level capabilities, read-only/full modes, skills/project instructions, CLI/session configuration.
- Plausible first-party paths checked: runtime identity revision, ultimate-policy proposals/escalation, parent policy resolution and returned persistent governance.
- Why no material first-party path remains: found mechanisms define/enforce capabilities but do not close identity/ultimate-policy decisions at the selected recursion.

## Recursion

The selected recursion is one Easy Agent project mission. Main and writable child agents are operational units. Nested child loops are bounded recursion of delegation, not automatically separate viable-system recursions.

## Variety and escalation

The main actor absorbs coding variety with tools, skills and delegated searches/implementation. Stall/max-turn/depth/concurrency limits fail or bound execution. User interaction remains at the main session; children cannot ask the user and must report a decision point upward.

## Evidence gaps

The positive S2 claim is narrower than “multi-agent exists”: it depends on the explicit parallel-writable-child collision warning and the parent-owned disjoint-scope decision. No live task-control or dedicated verifier path was found, supporting `—` for S3/S3* rather than `?`.
