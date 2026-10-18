---
harness_id: cadis
project_name: C.A.D.I.S.
repository: https://github.com/Growth-Circle/cadis
review_ref: 52c55854b1abbcda82839b7a934cbdb16a69b635
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# C.A.D.I.S.

## Review boundary

- System in focus: one first-party `cadisd` daemon/runtime organization at pinned revision `52c55854b1abbcda82839b7a934cbdb16a69b635`, including the main model-driven orchestrator, spawned/routed specialist agents and agent sessions, worker/worktree lifecycle, native tool loop, daemon-wide worker scheduler, policy/approval machinery, persistent runtime state and first-party CLI/HUD protocol control surfaces.
- Purpose and identity: operate a local-first multi-agent assistant that can execute user work through models and native tools, route or spawn specialist work, isolate parallel coding activity, regulate current agent/worker commitments and keep risky mutations behind daemon-owned policy and approval boundaries.
- Relevant environment: user/operator requests and interventions, project/workspace state, model-provider responses, tool/file/git/shell results, concurrent agent/worker activity, external provider availability and parent-authored configuration.
- Standard-distribution boundary: the reusable first-party Rust daemon/core runtime and shipped protocol clients at the pinned revision. External model endpoints, Codex/Ollama/OpenAI services, user repositories, external business services and third-party tools are dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: `Runtime` message/model/tool loop; daemon model streaming and repeated tool-observation generation; `Orchestrator` routing plus model-driven child-agent spawning; `orchestrator_awareness_context()`; agent/session/worker registries; worker worktree creation and concurrency queue; first-party policy/approval/store machinery; CLI/HUD `agent.list`, `agent.kill` and session-cancel control paths.
- Adjacent first-party surfaces excluded from ownership: repository CI/contributor workflows; project planning/roadmap material as design-only evidence where not backed by the pinned runtime; HUD presentation state that only renders daemon events; contributor `skills/`; documentation-only future integrations; generic logs/telemetry where they do not own an organizational decision.
- First-party operating / deployment modes considered: direct local daemon operation through CLI/HUD protocol clients; ordinary main-agent model/tool execution; routed/spawned specialist-agent operation; coding-worker operation with project worktrees; unattended autonomous model/tool steps within daemon limits; attended parent/operator control through shipped list/kill/cancel/approval surfaces.
- Recursion level: one running `cadisd` organization is the system-in-focus. Separately routed or spawned model-driven agents/agent sessions count as distinct S1 units when they pursue separate operational tasks inside the same daemon. Worker/process plurality alone is not treated as viability evidence.
- Reviewed revision: `52c55854b1abbcda82839b7a934cbdb16a69b635`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

C.A.D.I.S. ships a substantive daemon-owned agent runtime rather than a provider proxy. `message.send` enters `Runtime::begin_message_request`; the daemon invokes the selected provider, parses model-emitted tool directives, executes first-party tools under workspace/policy controls, builds a follow-up prompt containing tool results and invokes the model again. The loop continues until no further tool directive remains or bounded runtime/error conditions stop it. The model therefore owns substantive operational action selection while `cadisd` owns execution, feedback and limits.

The daemon is also genuinely multi-agent. The main agent receives a generated `Current CADIS runtime state` containing the agent roster, current statuses/tasks and recent agent sessions. Its first-party prompt tells it to use that state to route work and avoid duplicate work. More importantly, model output can contain first-party `[SPAWN role: task]` directives; the runtime converts these into child `AgentRecord`s and task-bearing agent sessions. That gives the main model a current whole-organization view plus a live decision right over additional operational commitments rather than merely a static manager label.

Cross-S1 coordination has a separate deterministic path. The project explicitly identifies parallel-agent file corruption and fan-out pressure as disturbances. Project coding workers receive daemon-owned worktree intent/metadata and the implementation creates Git worktrees under controlled project roots; worker validation runs with its current working directory inside the owned worktree. In parallel, the daemon counts all running workers, marks excess work `Queued` when `max_concurrent_workers` is reached and starts queued workers when slots become available. These mechanisms alter where and when separate S1 work can proceed, but the coordination regime itself is configured/mechanically enforced rather than chosen by an autonomous S2 actor, so S2 is `C`.

Inside-and-now control is stronger. `orchestrator_awareness_context()` constructs an all-agent current view with status, specialist and latest task plus recent session state/step progress and injects it into the main agent on each relevant request. The main model can respond to that state by creating child agents with new current task commitments. Deterministic worker admission/queueing supplies additional current-resource enforcement. A separate legitimate parent mode is shipped: first-party protocol/CLI/HUD surfaces list the full agent roster and let the operator kill an agent or cancel a session, which also cancels associated non-terminal workers and changes subsequent live operation. The autonomous and parent closures support `S3=A(P)`.

No credited complementary audit organization is established. A `Reviewer` specialist is an optional role using the same general agent contract, and the docs/examples can route review work to it, but the standard runtime does not establish a distinct ordinary claim, materially complementary access path and required corrective return. Worker validation, patch-apply preflights, policy checks, test reports and approval gates are ordinary production/integrity controls rather than S3* merely because they inspect or block output.

Persistent memory is similarly bounded. `cadis-memory` stores typed facts, procedures, corrections and other records and exposes candidate/promote/reject plus confirmed-memory capsule injection. At the assessed runtime boundary, `cadis-core` consumes confirmed capsules but does not wire an operating actor that turns external/future evidence into a generated adaptation option, selects/promotes it and returns a changed capability or S3 regime into future operation. Retaining a correction or procedure is therefore memory/context, not sufficient S4 closure.

Finally, C.A.D.I.S. has a strong named persona, specialist-persona persistence and central safety policy, but no credited S5 path. The main identity text is a runtime prompt and `agent.specialist.set` changes a specialist persona; policy/approval configuration constrains actions. None of these surfaces establishes an identity/ultimate-policy issue reaching a legitimate ultimate authority that can adjudicate or amend the organization's governing identity and return that decision into operation. They are role/configuration/enforcement mechanisms at this boundary.

Primary evidence:

- [`README.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/README.md) — daemon-owned runtime boundary, multi-agent operation, native tools, policy/approvals and isolated coding workers.
- [`crates/cadis-daemon/src/main.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-daemon/src/main.rs) — daemon request dispatch, provider generation, model-output tool parsing, execution and repeated tool-result follow-up generation.
- [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs) — core Runtime ownership; agent/session/worker state; tool directives; whole-agent awareness context; model-driven child-agent spawning; worker queue/worktree/apply/cancel paths; specialist persona injection.
- [`crates/cadis-core/src/orchestrator.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/orchestrator.rs) — first-party routing/delegation grammar and bounded model-driven spawn directive parsing.
- [`docs/10_RISK_REGISTER.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/10_RISK_REGISTER.md) — explicit fan-out resource and parallel-edit conflict disturbances plus their depth/budget/worktree mitigations.
- [`docs/29_PROTOCOL_FREEZE.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/29_PROTOCOL_FREEZE.md) — stable agent list/kill/model/specialist/spawn and worker/apply protocol control surfaces.
- [`docs/standards/10_AGENT_STANDARD.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/standards/10_AGENT_STANDARD.md) — main-agent requirement and optional coding/reviewer/tester roles under the common runtime contract.
- [`crates/cadis-memory/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-memory/src/lib.rs) — typed persistent memory, explicit candidate/promote/reject states and confirmed-memory capsule construction; considered and rejected as S4 by itself.

## S1 — Operations

- State: A
- Function: execute user objectives through a model-driven tool/action loop that receives environment/tool observations and chooses subsequent operational action until completion.
- Disturbance / variety regulated: request ambiguity, workspace/file/git/shell state, tool results, provider responses, failed actions and intermediate evidence that changes the next useful operational step.
- Decisive decision or feedback right: choose which available tool/action to invoke, its arguments, whether further action is needed and the final operational response within configured safety/step bounds.
- Decision owner: the model-driven CADIS agent running through the daemon's first-party generation/tool loop.
- Supporting / enforcement mechanisms: provider adapters, `parse_tool_call_directives`, native tool registry, workspace grants, policy engine, approvals, session/step limits, persistence and daemon event streaming.
- Closure path: request enters `cadisd` → routed agent/model generates a tool directive or response → daemon executes the selected tool under policy/workspace controls → tool results are placed into a follow-up prompt → model chooses the next action or completes → result returns to the caller/environment.
- Boundary reachability: ordinary `message.send` through the shipped daemon executes this first-party loop; no downstream organizational actor must be supplied to obtain model/action/feedback closure.
- Why this is / is not agent-owned: policy, grants and bounds can reject or constrain choices, but they do not predetermine the substantive tool/action sequence. Removing the model actor removes the ordinary operational decision path.
- Evidence: [`crates/cadis-daemon/src/main.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-daemon/src/main.rs); [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs); [`README.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: direct client commands and deterministic policy/approval branches also exist. `A` is based on the standard model-owned tool/action path, not on every request transition being autonomous.

## S2 — Coordination

- State: C
- Function: attenuate interference among distinct concurrently active CADIS operational agents/workers by isolating project mutations and bounding shared worker concurrency.
- Disturbance / variety regulated: parallel coding units can corrupt or overwrite the same working tree, while unbounded fan-out can consume shared daemon capacity and delay peer work.
- Decisive decision or feedback right: choose/revise the cross-S1 isolation and shared-concurrency regime that determines where a coding worker may mutate files and whether another worker may begin now or must wait.
- Decision owner: no autonomous first-party S2 actor owns that regime. The standard daemon supplies the function-specific worktree/queue relation and deterministically enforces parent/configured limits, leaving revision of the regime outside autonomous S2 ownership.
- Supporting / enforcement mechanisms: per-worker worktree intent and metadata, Git worktree creation, workspace/grant checks, worktree-local worker command cwd, `max_concurrent_workers`, global running-worker count, queued worker state and slot-release/start logic.
- Closure path: multiple S1 tasks enter parallel worker execution → daemon allocates project work into separate owned worktrees and counts current running workers → excess workers remain `Queued` and isolated workers operate on separate branches/paths → freed slots start waiting workers and their subsequent execution proceeds under the isolated context.
- Boundary reachability: worktree-backed worker operation and global worker admission are shipped daemon/core paths at the pinned revision; callers do not need to implement their own isolation or worker queue.
- Why this is / is not agent-owned: the disturbance and attenuation relation are first-party and specific to cross-unit interference, but isolation/admission outcomes are mechanically derived from configured policy rather than selected by an autonomous coordinating model. This supports `C`, not `A`.
- Evidence: [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs); [`docs/10_RISK_REGISTER.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/10_RISK_REGISTER.md); [`README.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic `@agent` routing and child-agent spawning are not credited as S2 by themselves. Positive credit rests on the documented parallel-edit/resource disturbances and the first-party isolation/backpressure relation.
- Distinct S1 units: two or more separately routed/spawned model-driven agents/agent sessions executing operational tasks inside the same `cadisd`, including coding tasks represented by daemon-managed worker records.
- Inter-S1 disturbance: simultaneous project mutations can conflict on the same repository state, and concurrent worker fan-out can exceed shared worker execution capacity even when each task is locally valid.
- Attenuating coordination relation: CADIS assigns project workers separate Git worktrees and applies a daemon-wide maximum number of running workers, holding excess work in `Queued` state.
- Feedback into subsequent S1 behaviour: the owned worktree becomes the worker's execution context/cwd for validation and artifacts, while queued workers do not begin until a shared slot is released; both relations change where or when each S1's next operation occurs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanisms are explicitly aimed at cross-agent file-conflict and aggregate fan-out disturbances, not merely at transporting messages, naming specialists or ordering a task graph.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain a current organization-wide view of agent commitments and use it to allocate/change present operational work, with an additional legitimate parent/operator intervention mode.
- Disturbance / variety regulated: duplicated or poorly allocated agent work, changing agent/session status, current task commitments, runaway/unwanted current activity and aggregate worker pressure can make the daemon's present operation incoherent or exceed current capacity.
- Decisive decision or feedback right: autonomous mode — decide from current all-agent state whether to create a new child agent and assign it a task; parent mode — inspect the current roster and terminate an agent or cancel a session, removing associated current commitments/workers from later operation.
- Decision owner: autonomous mode — the main CADIS model actor receiving first-party current runtime state; parent mode — the legitimate self-hosting operator using shipped CLI/HUD/protocol controls.
- Supporting / enforcement mechanisms: `orchestrator_awareness_context()`, agent/session registries and sorted snapshots, recent-session task/step summaries, bounded model-driven `[SPAWN]` parsing, spawn limits, global worker scheduler, `agent.list`, `agent.kill`, `session.cancel`, persistence and cancellation propagation.
- Closure path: current agent roster/session state is assembled → injected into the main agent's prompt → main model selects a new child role/task when current organization needs it → runtime creates the child and task-bearing session → subsequent organization state includes the changed commitment. In parent mode, roster inspection → kill/cancel request → agent/session and non-terminal associated worker cancellation → subsequent live operation reflects the intervention.
- Boundary reachability: whole-agent awareness and model-driven child spawning are standard first-party runtime paths; parent list/kill/cancel operations are stable shipped protocol/CLI/HUD surfaces.
- Why this is / is not agent-owned: the main actor receives whole-organization current state rather than only one delegated task and autonomously changes current commitments. Deterministic spawn/worker limits constrain that authority but do not choose the child task. The parent path is separately owned by the operator, producing the `(P)` modifier.
- Evidence: [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs); [`docs/29_PROTOCOL_FREEZE.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/29_PROTOCOL_FREEZE.md); [`crates/cadis-cli/src/main.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-cli/src/main.rs).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: ordinary delegation is not credited as S3 by itself. The positive autonomous mapping depends specifically on the main agent's injected whole-roster/recent-session state plus its live model-owned commitment-creation path. Worker concurrency limits are supporting current-control enforcement, not the reason for `A`.
- Whole-system current view: `orchestrator_awareness_context()` enumerates the current agent roster with status, specialist and latest task and also includes recent agent sessions with state and step/budget progress; this generated state is injected into the main orchestrator prompt.
- Current-control decision scope: autonomous creation/allocation of new child-agent commitments in response to current organization state, plus parent termination/cancellation of existing live commitments; daemon worker admission additionally constrains concurrent execution.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main CADIS model actor | Current all-agent roster/recent-session state indicates another specialist/task commitment is useful | current runtime state → main model `[SPAWN role: task]` decision → first-party child agent/session creation → changed subsequent current organization | `crates/cadis-core/src/lib.rs`, `crates/cadis-core/src/orchestrator.rs` |
| Parent (`P`) | Self-hosting CADIS operator | Operator sees current agent state and decides a live agent/session should stop | `agent.list`/current HUD state → `agent.kill` or `session.cancel` → cancellation of agent session and associated workers → later runtime state excludes/terminates that commitment | `docs/29_PROTOCOL_FREEZE.md`, `crates/cadis-core/src/lib.rs`, `crates/cadis-cli/src/main.rs` |

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path is established for the declared CADIS operating boundary at the pinned revision.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: optional reviewer/tester specialist roles, worker validation commands/test-report artifacts, patch-apply preflight, policy checks, approvals, logs and lifecycle events.
- Closure path: not established as S3*. These paths validate ordinary outputs or expose ordinary evidence but do not establish a materially independent complementary challenge of an S1/S3 operational claim with a required corrective return.
- Why this is / is not agent-owned: a role named `Reviewer` can be spawned/routed, but it uses the common agent contract and is not packaged as a mandatory complementary audit owner with distinct evidence access/authority. Deterministic validation/preflight is routine production QA/integrity control.
- Evidence: [`docs/standards/10_AGENT_STANDARD.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/standards/10_AGENT_STANDARD.md); [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs); [`docs/29_PROTOCOL_FREEZE.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/29_PROTOCOL_FREEZE.md).
- Basis: explicit + structural absence
- Confidence: medium-high
- Caveats: a downstream organization can deliberately instantiate a reviewer with different workspace/test access. That would be a separate system-in-focus and does not upgrade the standard CADIS distribution here.

### Absence scope

- Surfaces inspected: main/specialist agent contract, worker result/artifact/validation/apply paths, reviewer/tester role documentation, policy/approval machinery, logs/events and protocol control surfaces.
- Plausible first-party paths checked: optional `Reviewer` agent, worker test report/summary, `worker.apply` preflight and clean-tree checks, approval gates, audit/event logs and generic agent tail/state views.
- Why no material first-party path remains: each inspected path is either optional same-contract review, ordinary production validation/integrity enforcement or observability. None packages complementary access plus independent audit judgment plus findings returned into ordinary S1/S3 corrective operation.

## S4 — Outside-and-then adaptation

- State: —
- Function: no material first-party outside-and-then adaptation loop is established for the declared CADIS operating boundary at the pinned revision.
- Disturbance / variety regulated: not established as prospective adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent memory records/capsules, workspace/project facts, correction/procedure memory kinds, provider/model selection, specialist personas, configuration reload and project/workspace state.
- Closure path: no first-party operating path was found that distinguishes an external/future capability issue, generates an adaptation option, selects it and returns a changed capability or S3 regime into subsequent operation.
- Why this is / is not agent-owned: `cadis-memory` can store candidate records, explicitly promote/reject them and inject already-confirmed capsules, but `cadis-core` only consumes confirmed memory. The standard runtime does not wire autonomous evidence-to-adaptation proposal/selection/promotion closure.
- Evidence: [`crates/cadis-memory/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-memory/src/lib.rs); [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: retaining a user correction or project procedure can change future model context after external promotion, but memory persistence/context reuse alone does not establish S4's prospective adaptation decision function.

### Absence scope

- Surfaces inspected: `cadis-memory`, confirmed-memory prompt injection, specialist/persona state, provider/model controls, workspace state and configuration surfaces.
- Plausible first-party paths checked: correction/procedure memory kinds, candidate/promote/reject lifecycle, memory capsule injection, model switching, specialist persona changes, workspace/project updates and configuration reload.
- Why no material first-party path remains: the inspected mechanisms retain/reconfigure existing operating context or require an external actor to decide what becomes confirmed. They do not generate and select prospective organizational adaptation options and close them back into capability/current control.

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy authority loop is established for the declared CADIS operating boundary at the pinned revision.
- Disturbance / variety regulated: not established at identity/ultimate-policy level.
- Decisive decision or feedback right: no legitimate first-party ultimate authority is wired to adjudicate or amend the organization's governing identity/policy when such an issue arises.
- Decision owner: none established.
- Supporting / enforcement mechanisms: hardcoded/default CADIS identity prompt, specialist persona fields and `agent.specialist.set`, central policy engine, workspace grants, risk classes, approval state and ordinary model/provider configuration.
- Closure path: no identity/ultimate-policy issue → legitimate authority → adjudication/amendment → subsequent-operation-under-new-policy chain is established.
- Why this is / is not agent-owned: the named CADIS persona and parent-editable specialist persona configure operating roles; policy/approval components enforce already-selected constraints. Neither surface establishes ultimate-policy ownership merely because it changes prompts or blocks risky actions.
- Evidence: [`crates/cadis-core/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-core/src/lib.rs); [`docs/29_PROTOCOL_FREEZE.md`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/docs/29_PROTOCOL_FREEZE.md); [`crates/cadis-policy/src/lib.rs`](https://github.com/Growth-Circle/cadis/blob/52c55854b1abbcda82839b7a934cbdb16a69b635/crates/cadis-policy/src/lib.rs).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: `agent.specialist.set` and parent configuration can materially change behavior, but task/role/persona configuration is not automatically the organization's identity/ultimate-policy function.

### Absence scope

- Surfaces inspected: main identity/system prompt, specialist/persona persistence and setter, agent role/model controls, policy engine, risk/approval state, workspace grants, profile/agent-home material and configuration surfaces.
- Plausible first-party paths checked: main persona text, `agent.specialist.set`, parent model/persona changes, approval decisions, central policy configuration and agent-home identity/instruction persistence.
- Why no material first-party path remains: these surfaces configure roles or enforce existing rules. The reviewed distribution does not identify an ultimate-policy class of issue, a legitimate final authority for it and a return path by which an authoritative identity/policy decision governs later operation.