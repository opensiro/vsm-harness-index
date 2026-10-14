---
harness_id: zcode
project_name: ZCode
repository: https://github.com/zai-org/ZCode
review_ref: 872ad960de7ec172591f7e1952f7849229f94521
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# ZCode

## Review boundary
- System in focus: the shipped ZCode Agent CLI model/tool runtime plus its directly used child subagent runner and task control interfaces; Desktop and Web consume the same first-party runtime.
- Purpose and identity: execute user coding requests and optionally spawn independently executing child tasks under a model-led main session.
- Relevant environment: source workspace/files/shell, provider model endpoints, user tool permissions, session and task state, child outputs and user feedback.
- Standard-distribution boundary: included regular `apps/zcode-cli` source and shared package adapters, not just browser/TUI UI; third-party models/MCP servers and user-custom workflow definitions excluded ([README.en.md](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/README.en.md)).
- Credited operating / distribution surfaces: [apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts); [apps/zcode-cli/packages/core/src/subagent/runner.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runner.ts); [apps/zcode-cli/packages/core/src/subagent/message-steering.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/message-steering.ts); [apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts); [apps/zcode-cli/packages/core/src/agent/message-history.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/agent/message-history.ts).
- Adjacent first-party surfaces excluded from ownership: UI-only projections, testing harnesses, third-party model behavior, custom user-created plugins and separate provider orchestration.
- First-party operating / deployment modes considered: direct CLI agent tool loop; bundled Web/Desktop host; model-side child subagent launch/run/wait/stop/sendMessage; continuation and persisted session recovery.
- Recursion level: a primary ZCode coding session and its own active child tasks, not all tabs/users or the Z.ai company.
- Reviewed revision: `872ad960de7ec172591f7e1952f7849229f94521`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
ZCode's Agent CLI source is in-tree in `apps/zcode-cli`. The code routes a live model turn through first-party `turn-loop`, `turn-model-step`, tool scheduling/execution, permission handling and persistent message history rather than inheriting an outside coding agent's loop ([README.en.md](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/README.en.md); [apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts); [apps/zcode-cli/packages/core/src/agent/message-history.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/agent/message-history.ts)).
The `SubagentPort` is implemented in the included runner with `launch`, `run`, `start`, `getTask`, `backgroundTask`, `waitForTask`, `stopTask` and `sendMessage`. The host's subagent runtime methods construct separate child runtimes, inherit bounded permissions/tool policies and relay child activities to the parent; a live steer message can be queued into the child's turn ([apps/zcode-cli/packages/core/src/subagent/runner.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runner.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts); [apps/zcode-cli/packages/core/src/subagent/message-steering.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/message-steering.ts); [apps/zcode-cli/packages/core/src/subagent/tool-policy.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/tool-policy.ts)).
These task lifecycle and message delivery surfaces support control of current delegated operations, but they do not themselves demonstrate a conflict-specific S2 arbitration mechanism between separately operating children. Likewise, built-in completion verification and memory retention cannot be elevated automatically into independent audit or prospective intelligence.

## Operational model
The main model proposes tool actions, observes results, and may delegate bounded sub-tasks to child agent sessions. Child runs can proceed asynchronously with a registry that exposes status and control; the parent receives notifications and can steer or cancel. Permissions and time limits regulate actions but do not constitute a second agentic metasystem by themselves.

## S1 — Operations

- State: A
- Function: Direct first-party model-led coding and tool execution in the Agent CLI runtime.
- Disturbance / variety regulated: Dynamic coding objectives, file/workspace changes, model responses and tool errors.
- Decisive decision or feedback right: Choose tool calls and continue/repair from the returned tool observations.
- Decision owner: Configured model-driven ZCode primary Agent running under the shipped CLI service.
- Supporting / enforcement mechanisms: Turn-loop/model-step, executor, permission broker, persisted session history.
- Closure path: Task → model/tool-call turn → executable tool response → next model decision or completion.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Model-facing tool choices are operational rather than deterministic UI events.
- Evidence: [apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-model-step.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts); [README.en.md](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/README.en.md)
- Basis: structural
- Confidence: high
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## S2 — Coordination

- State: ?
- Function: Candidate inter-worker coordination; no source-grounded, interference-specific arbitration loop established.
- Distinct S1 units: Main and separately running model/tool child agent sessions can operate concurrently.
- Inter-S1 disturbance: Potential changes to overlapping files, conflicting work results and child request contention.
- Attenuating coordination relation: No proven policy that detects a concrete inter-child conflict and alters their operational scope or placement.
- Feedback into subsequent S1 behaviour: Task status/notifications feed the parent, but conflict-specific corrective worker action remains unproven.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: S2 remains unknown, without treating ordinary task messages or technical scheduling as substantive S2.
- Disturbance / variety regulated: Potential workspace resource contention between concurrently spawned agents.
- Decisive decision or feedback right: Unresolved beyond configured tool availability, task registry and permissions.
- Decision owner: Unresolved: service and parent may impose task control, not proven inter-S1 conflict arbitration.
- Supporting / enforcement mechanisms: Subagent child isolation configuration, task registry, parent messages and permission checks.
- Closure path: Separate child results and message handling exist without verified conflict → attenuation → repair for competing workers.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Session/task registration, generic delegation and permission checking do not establish S2.
- Evidence: [apps/zcode-cli/packages/core/src/subagent/runner.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runner.ts); [apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts); [apps/zcode-cli/packages/core/src/subagent/tool-policy.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/tool-policy.ts)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## S3 — Inside-and-now control

- State: A
- Function: Model-led parent regulates ongoing independently running child agent tasks at the current team recursion.
- Whole-system current view: Root has task IDs, child status/results and notifications for the children it launched.
- Current-control decision scope: Child task allocation, interruption, follow-up and result integration within the bounded parent-child task set.
- Disturbance / variety regulated: Unfinished subordinate coding tasks, timeouts, interrupted child runs and new results.
- Decisive decision or feedback right: Launch subordinate tasks, steer running child requests, wait/stop, integrate reports and select new work.
- Decision owner: Primary ZCode model-guided coordinator session through shipped SubagentPort.
- Supporting / enforcement mechanisms: Child runner, SubagentPort, task snapshots, coordinator response and steering interface.
- Closure path: Child status/result → parent model sees tool response or asynchronous notification → follow-up/steering or next child task.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Decisive model task allocation and follow-up can alter active worker runs; task registry merely implements control.
- Evidence: [apps/zcode-cli/packages/core/src/subagent/runner.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runner.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts); [apps/zcode-cli/packages/core/src/subagent/message-steering.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/message-steering.ts); [apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runtime-task-registry.ts)
- Basis: structural
- Confidence: medium
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## S3* — Complementary audit

- State: ?
- Function: Separate operational audit path not established even though completion verification helpers and review surfaces exist.
- Claim being audited: Child or root agent delivered the requested code/tasks correctly.
- Ordinary reporting path: Child completion and model/tool outputs return to root via task runner and notifications.
- Complementary access path: Unproven source/artifact sampling by a separate reviewer; completion helper can inspect claims without a second operating audit path.
- Independence boundary: No guaranteed materially independent reviewer decision owner established.
- Who acts on findings: Root continuation may use checks, but returned independent audit findings and corrective closure remain unproven.
- Disturbance / variety regulated: Incorrect code/task completion claims or missing verification evidence.
- Decisive decision or feedback right: Possible target-completion checking, but independent source sampling and corrective return are not established.
- Decision owner: Unresolved separate reviewer authority; no independent audit actor guaranteed by core runtime.
- Supporting / enforcement mechanisms: Target completion verification helper and standard tool feedback.
- Closure path: Model output/checks may feed same agent, but a materially independent challenger with primary artifact access is not proven.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Single-agent tests and helper names alone are insufficient for S3* semantics.
- Evidence: [apps/zcode-cli/packages/core/src/runtime/methods/target-completion-verification.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/target-completion-verification.ts); [apps/zcode-cli/packages/core/src/subagent/runner.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/runner.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-loop.ts)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Retained project or subagent memories and dynamic workflows may influence later tasks without a proved outside-and-then capability evolution loop.
- External distinction: Provider/context and project changes can enter through tools or memory, not a demonstrated strategic environmental-scan unit.
- Future / prospective distinction: Later recall and project memory are temporally future-facing but not sufficient organizational anticipation.
- Adaptation option generated: No definite capability-changing option/owner documented in the reviewed running mode.
- Path back into current capability / S3: Prompt/session reuse may affect later actions, without proving S4-to-S3 redesign closure.
- Disturbance / variety regulated: Changing environments, new project requirements and capability gaps.
- Decisive decision or feedback right: Not established which model-led agent chooses future capability adaptation based on external horizon scanning.
- Decision owner: Unresolved among task agent, configured workflows, app owner and memory subsystem.
- Supporting / enforcement mechanisms: Persistent subagent memory, project-context and workflow facilities.
- Closure path: Stored experience → later prompt/context, but no traced external prospective option → adoption into current operational capability.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Persistent memory or model summaries do not automatically establish S4.
- Evidence: [apps/zcode-cli/packages/core/src/subagent/persistent-memory.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/persistent-memory.ts); [apps/zcode-cli/packages/core/src/agent/message-history.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/agent/message-history.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## S5 — Policy and identity

- State: ?
- Function: First-party permission and configuration governance exists but not a complete ultimate identity/policy loop.
- Identity / ultimate-policy issue: Which coding-agent purpose, permissible authority and final governance applies at root/team level.
- Ultimate authority in each claimed mode: Human/user settings and deterministic policies govern tools; no qualifying complete model/parent S5 closure proven.
- Return-to-operation path: Permissions change individual tool admit/deny, not proven ultimate organizational policy adaptation.
- Disturbance / variety regulated: Trust/permission boundaries, operator confirmations and tool access to host environment.
- Decisive decision or feedback right: User/developer permissions and policies may constrain actions; ultimate-policy decision and organization-level return unproven.
- Decision owner: Human and deterministic permission engine; a qualifying agent/parent S5 is not established.
- Supporting / enforcement mechanisms: Permission broker, subagent tool allowlist, session capabilities and workspace restrictions.
- Closure path: Permission allow/deny → local tool execution; no proved ultimate organizational identity/policy rewrite and feedback.
- Boundary reachability: The cited code is reached from the bundled first-party `apps/zcode-cli` runtime, whose CLI also supplies Desktop/Web hosting.
- Why this is / is not agent-owned: Safety gates or provider permission modes do not establish S5.
- Evidence: [apps/zcode-cli/packages/core/src/subagent/tool-policy.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/subagent/tool-policy.ts); [apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/subagent.ts); [apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts](https://github.com/zai-org/ZCode/blob/872ad960de7ec172591f7e1952f7849229f94521/apps/zcode-cli/packages/core/src/runtime/methods/turn-tools.ts)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party-source review at the pinned commit; not a provider-backed trajectory, and no other user's custom plugin/workflow is counted.

## Recursion

Primary coding execution and child delegated model/tool tasks are S1 at their operating level. The model-led parent may own current child task commitments (S3=A) in this restricted recursion. Additional app panels, provider internals and future other users' organizational workflows are not silently included.

## Variety and escalation

Tool observations and permission feedback regulate unpredictable coding actions. Child results and steering provide root current-control feedback. No inter-child conflict attenuation, independent audit, prospective strategic intelligence or ultimate policy mode was attributed from naming or generic primitives alone.

## Evidence gaps

Review of the frozen in-tree runtime and concrete SubagentPort implementation, not a live model trajectory. S2 needs specific independent-worker interference → attenuation evidence; S3* needs separate primary-artifact challenge with corrective return; S4 needs external prospective adaptation plus a returned capability-change loop; S5 needs identity/ultimate-policy owner and governing closure. The `?` states intentionally remain open.
