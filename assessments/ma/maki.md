---
harness_id: maki
project_name: Maki
repository: https://github.com/tontinton/maki
review_ref: eb2274751272ffbc618a8d103041da3f4a96e8d0
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Maki

## Review boundary

- System in focus: the first-party Maki coding runtime at frozen revision eb2274751272ffbc618a8d103041da3f4a96e8d0, including the main model/tool coding loop, built-in and plugin tools, task-subagent sessions, shared file-access safety state, permission/session machinery, memory plugin, plan/headless/ACP execution and interactive task UI.
- Purpose and identity: perform software-engineering work through one top-level coding agent that can inspect/edit/execute, delegate focused research or implementation work to fresh subagents, and expose those live subagents to the operator.
- Relevant environment: user requests and approvals, repository files, tool/process results, provider/model responses, concurrent subagent file activity, persisted session/history state, long-term memory notes, MCP/skills and operator cancellation.
- Standard-distribution boundary: shipped Maki runtime and bundled first-party plugins. External model endpoints, MCP servers, skills/content packs, rtk, tree-sitter, Monty and host editor/ACP clients are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: maki-agent, maki-lua agent/task APIs, bundled task and memory plugins, maki-ui session/task surfaces, permissions, storage, headless/ACP/print paths and built-in coding tools.
- Adjacent first-party surfaces excluded from ownership: benchmark/report artifacts, telemetry, docs/tests/CI and package-management machinery unless they directly instantiate the running coding organization.
- First-party operating / deployment modes considered: interactive coding session; headless/print; ACP; Plan mode; research/general subagents spawned by the task tool; supported provider/model tiers and normal permission/trust modes.
- Recursion level: one Maki coding session. The top-level coding agent and any general/research task subagents that own focused operational outcomes are S1 units at this level. Deterministic shared file-access machinery coordinates their file mutation.
- Reviewed revision: eb2274751272ffbc618a8d103041da3f4a96e8d0.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Maki implements a first-party streaming Agent loop that repeatedly calls a selected model, dispatches requested tools and returns results into the same conversation. The bundled task plugin can launch autonomous fresh research or general-purpose subagent sessions, can run several through the batch/concurrency path, chooses a model tier bounded by the parent tier, and returns each subagent result to the parent.

Subagents deliberately share the parent's FileAccess state. The runtime records file mtimes, applies a per-file asynchronous write lock for mutable tools and rejects an edit after a stale read. The source explicitly explains that a fresh subagent-local lock would be ineffective once two agents edit one file. This is a concrete cross-S1 collision-control mechanism, but the decisive relation is deterministic rather than model-owned.

The interactive UI retains separate live subagent chats. The task picker reports the main chat plus working/done/error subagents and the user can focus a running subagent; double-Escape cancels that selected child without cancelling the main chat or unrelated children. This creates a supported human parent current-control path over active commitments. No equivalent model-owned live whole-system control loop was found: the main agent can choose delegation and receives task results, but task execution itself is a bounded tool call rather than a persistent model-owned supervision surface.

## Operational model

The main model-backed agent owns open-ended coding choices. Research/general subagents own the open-ended choices inside the task prompts given to them. Deterministic permission and file-access layers restrict execution; the operator can approve/deny tools and can cancel live subagents.

Long-term memory is a persisted note surface available to later operation. It provides useful continuity but the reviewed runtime does not establish a separate external-and-prospective adaptation owner that develops and returns future capability options. Plan mode and persistent sessions similarly change operating context rather than closing S4 or S5.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and test a software project through model-selected coding/tool actions, including focused subagent tasks when useful.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, tool/process failures, coding/test feedback, context pressure, permission denial and bounded delegated subtasks.
- Decisive decision or feedback right: choose substantive repository/tool actions, interpret their results, decide when to delegate work and decide when the coding objective is complete.
- Decision owner: the active model-backed main Maki Agent and, for delegated focused work, the model-backed subagent session.
- Supporting / enforcement mechanisms: tool registry/dispatch, provider adapters, permission manager, context compaction, sessions, file-access safety, MCP, skills and cancellation.
- Closure path: user request → model selects direct coding/tool action or task subagent → first-party runtime executes/returns evidence → model revises work → run finishes when the model completes or a hard boundary stops it.
- Boundary reachability: interactive, headless/print and ACP paths instantiate the same first-party Agent/tool machinery; the bundled task tool is exposed to the main/workflow audience.
- Why this is / is not agent-owned: deterministic runtime code transports and constrains the work, but the model decides the open-ended implementation/research actions and completion.
- Evidence: [README.md](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/README.md); [maki-agent/src/agent/run.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/agent/run.rs); [plugins/task/init.lua](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/plugins/task/init.lua).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: permissions may remain human-controlled for sensitive operations, but approval constrains an action rather than supplying the coding decision itself.

## S2 — Coordination

- State: C
- Function: prevent concurrent operational agents from corrupting one another's file work by serializing mutations and feeding stale-read conflicts back into later action.
- Disturbance / variety regulated: two parent/subagent or subagent/subagent operations reading and mutating the same file concurrently, including stale read-modify-write races.
- Decisive decision or feedback right: the first-party runtime decides whether a mutable operation must wait on the canonical per-file lock and whether an attempted edit must fail because the file changed after the recorded read.
- Decision owner: deterministic FileAccess / tool-dispatch code.
- Supporting / enforcement mechanisms: canonical FileKey identity, shared FileAccess across parent/subagents, per-file asynchronous mutex, mtime read tracking and stale-read rejection.
- Closure path: operational unit reads/targets a file → another unit may mutate it → shared lock serializes simultaneous mutation and recorded mtime detects stale evidence → waiting/failure result changes the affected unit's subsequent tool behavior.
- Boundary reachability: the subagent session constructor explicitly shares the parent's FileAccess state and all mutable-path tools receive the dispatcher lock.
- Why this is / is not agent-owned: the model may choose parallel delegated work, but it does not decide lock ownership or stale-read arbitration; those coordination decisions are encoded in deterministic runtime logic.
- Distinct S1 units: the main coding agent plus concurrently launched autonomous research/general task sessions when they own focused operational work.
- Inter-S1 disturbance: simultaneous mutation of one file can interleave/corrupt work and a subagent with a stale read can overwrite newer content.
- Attenuating coordination relation: canonical per-file write locks serialize mutable operations and shared read-version state rejects stale edits.
- Feedback into subsequent S1 behaviour: a waiter cannot proceed until the lock releases; a stale-edit rejection tells the agent to re-read before attempting another edit.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism exists to attenuate a concrete peer operational interference mode and returns the collision state to the affected operation.
- Evidence: [maki-agent/src/tools/file_access.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/tools/file_access.rs); [maki-lua/src/api/agent.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-lua/src/api/agent.rs); [plugins/task/init.lua](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/plugins/task/init.lua).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the task plugin's process-wide concurrency cap is supporting enforcement; the C classification rests on deterministic collision attenuation, not on agent plurality alone.

## S3 — Inside-and-now control

- State: P
- Function: give the legitimate operator a current view of the active session organization and the right to stop a selected live subagent commitment.
- Disturbance / variety regulated: a running delegated task that is no longer wanted, is wedged, or should be terminated while the rest of the session continues.
- Decisive decision or feedback right: select the live child task and cancel it while preserving the parent session and unrelated children.
- Decision owner: the human operator in the interactive Maki UI.
- Supporting / enforcement mechanisms: task status model, /tasks picker, task focus routing, per-subagent cancel tokens and double-Escape UI action.
- Closure path: operator observes the main chat plus live child task statuses → focuses a chosen running subagent → issues cancel → first-party cancel token terminates that child and marks it finished → remaining session/subagents continue.
- Boundary reachability: the task picker is bundled with the task plugin; tests and UI code show multiple simultaneous subagents and cancellation of one without cancelling the main or other children.
- Why this is / is not agent-owned: the main model can create delegated work, but no model-owned live whole-system supervision decision path was established; the concrete current-control right is exercised by the operator.
- Whole-system current view: the picker rebuilds from the main chat and all task sessions, reporting working/done/error state and current focus.
- Current-control decision scope: selective cancellation of an active delegated S1 commitment while leaving the rest of the current coding organization running.
- Evidence: [plugins/task/picker.lua](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/plugins/task/picker.lua); [maki-ui/src/app/tasks.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-ui/src/app/tasks.rs); [maki-ui/src/app/tests.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-ui/src/app/tests.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: tool approval and ordinary session cancellation are not used to manufacture this claim; it rests on the task-level whole-session view and selective subagent commitment control.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no separate first-party auditor independently challenges the coding agent's completion/result and returns findings into corrective operation.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: plan prompts, ordinary tests/tool evidence, task subagents, hooks and telemetry can support operation but do not by themselves provide an independent complementary audit owner.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: research/general task subagents are generic delegated S1 workers; the reviewed distribution does not wire a distinct reviewer/auditor with an independent claim/evidence path and corrective return.
- Evidence: [plugins/task/init.lua](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/plugins/task/init.lua); [maki-agent/src/prompts/plan.md](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/prompts/plan.md); [maki-agent/src/agent/run.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/agent/run.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: an operator can ask a task subagent to review something, but generic user/model-created delegation is not a standard independent S3* constructor.

### Absence scope

- Surfaces inspected: main and subagent prompts, task plugin, plan mode, hooks, tool results, UI task lifecycle and benchmark/telemetry-adjacent surfaces.
- Plausible first-party paths checked: dedicated reviewer/verifier role, authorship-independent second pass, test gate, plan approval, hook verdict and benchmark feedback.
- Why no material first-party path remains: no shipped path assigns a separate audit actor both independent evidence access and a review judgment that is automatically returned into corrective S1 operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no qualifying outside/future disturbance is placed under an actor that develops adaptation options and returns them into present capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: long-term memory notes, provider/model selection, skills/MCP, context compaction and project instructions provide persistence/capability inputs but are not sufficient S4 closure.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the memory tool can retain facts for later sessions, but persistence/reuse alone does not establish an external-and-prospective option-development loop.
- Evidence: [README.md](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/README.md); [plugins/memory/init.lua](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/plugins/memory/init.lua); [maki-agent/src/agent/compaction.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/agent/compaction.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: later work can benefit from saved notes and changed providers/skills, but those changes are not shown to be chosen by an S4 adaptation owner from outside/future evidence.

### Absence scope

- Surfaces inspected: memory plugin, provider/model switching, skills/MCP, instructions, compaction, session persistence and task delegation.
- Plausible first-party paths checked: autonomous skill/model change, learned policy update, future-facing environment scan and durable behavioral adaptation.
- Why no material first-party path remains: inspected paths are memory/configuration/current-task mechanisms rather than a closed prospective adaptation conversation with current control.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy issue is routed to an authoritative S5 owner.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: project trust, permission rules, plan-mode write restriction, prompts and plugin/provider configuration constrain operation but do not create identity-policy authority.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent follows developer/user-authored permissions and configuration and cannot authoritatively redefine Maki's identity or ultimate operating policy.
- Evidence: [maki-agent/src/permissions.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/permissions.rs); [src/project_trust.rs](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/src/project_trust.rs); [maki-agent/src/prompts/system.md](https://github.com/tontinton/maki/blob/eb2274751272ffbc618a8d103041da3f4a96e8d0/maki-agent/src/prompts/system.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: operator permissions are legitimate constraints but no identity/ultimate-policy issue/decision/return loop is established.

### Absence scope

- Surfaces inspected: permissions, trust, prompts, Lua/plugin configuration, provider/model settings, task controls and ACP/headless modes.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity policy, agent-authored permission policy and project governance.
- Why no material first-party path remains: all observed policy surfaces are static/configured operating constraints or local permissions, not a closed identity-governance function.

## Distributed OSS parent arrangement

The assessed organization is the running Maki coding session, not the GitHub maintainer project. Repository maintainers/contributors are not imported as parent S3/S4/S5 owners. The positive parent claim is limited to the live operator's current task-control surface.

## Self-hosted and non-human modes

Maki supports local and hosted providers plus headless/ACP modes. S1 and S2 do not depend on a specific provider. The S3 parent path is interactive-mode specific; absence of that UI in headless operation does not convert it into autonomous S3.

## Recursion

One coding session is the viable-unit candidate. Main and task subagents are operational S1 units when instantiated. Shared FileAccess is S2 coordination code. The human task-view/cancel surface supplies parent S3. No separate higher-function organization is inferred from plugins, providers or protocol clients.

## Variety and escalation

S1 absorbs ordinary coding/tool variety. Shared per-file locking and stale-read feedback attenuate cross-agent write interference under S2. A human may stop one live delegated commitment under S3=P. Permissions, retries, compaction and cancellation enforce limits without establishing S3*, S4 or S5.

## Evidence gaps

No ? state is required. The frozen implementation directly exposes the model/tool loop, subagent construction, shared file coordination and interactive task-control paths; the inspected review/memory/policy surfaces are sufficient for documented no-material-path conclusions on S3*, S4 and S5.
