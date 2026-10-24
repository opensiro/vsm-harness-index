---
harness_id: grok-build
project_name: Grok Build
repository: https://github.com/xai-org/grok-build
review_ref: 4247f661689354b831191f11eeeac8424993fe3d
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

# Grok Build

## Review boundary

- System in focus: shipped first-party Grok Build Rust terminal coding agent plus its resident root/subagent task control at the reviewed frozen source revision.
- Purpose and identity: interpret coding requests using a model/tool loop, change and inspect a project workspace and delegate bounded coding tasks to independent child agent runs.
- Relevant environment: local repository, terminal commands, model responses, tool effects, child task failures, permission and VCS status, user approvals.
- Standard-distribution boundary: official `grok` CLI/TUI and agent runtime, headless/ACP modes, subagent Task tool and first-party workspace interface at the frozen checkout; separate upstream models, user-installed external MCP servers and UI/cloud service internals are excluded.
- Credited operating / distribution surfaces: [README.md](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/README.md); [crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs); [crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs); [crates/codegen/xai-grok-shell/src/extensions/task.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/task.rs).
- Adjacent first-party surfaces excluded from ownership: developer CI and test fixtures, UI-only review comments, unrelated bundled third-party ports, separate model/provider governance and cloud-storage backend internals.
- First-party operating / deployment modes considered: normal coding-agent tool loop; model-initiated subagent Task calls; resident parent with child status/query/message/cancel, optional child worktree isolation, supported TUI/headless/ACP host.
- Recursion level: one Grok Build root coding session supervising its children; not the vendor organization, every open terminal, or all remote agents.
- Reviewed revision: `4247f661689354b831191f11eeeac8424993fe3d`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The pinned Rust repo includes the directly runnable `grok` coding CLI and a first-party agent runtime, tools, workspace filesystem/VCS integrations, model/session interfaces and active subagent coordination. The `task` tool is model facing and launches a child with a task description, optionally with a worktree checkout. The parent shell coordinator drives the child runner and retains pending/active/completed state, list/query/waiters, cancellation and messaging. It also fences admissions during parent teardown and cancellation. [README.md](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/README.md); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs); [crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs).

A resident parent can query children and receive results, send active messages and terminate child attempts. The available `x.ai/review/comment` extension records inline review events to cloud storage; it does not by itself audit the agent's source artifacts. The coordinator concurrency admission limit is a technical workload gate, not a proven S2 conflict-specific arbitration function. [crates/codegen/xai-grok-shell/src/extensions/task.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/task.rs); [crates/codegen/xai-grok-shell/src/extensions/review.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/review.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/admission.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/admission.rs).

## Operational model

The root model owns action selection for a coding task. It may split work into model-directed child coding sessions through the shipped Task tool, then use first-party child lifecycle operations and results to decide further work. Technical scheduling and checkout isolation are separate from agent-owned inter-worker coordination or system-wide policy judgment. Evidence is restricted to this shipped first-party code, not inference quality or claimed product capability.


## S1 — Operations

- State: A
- Function: Model-guided terminal coding actions against a real file/shell/VCS workspace, with live tool-result feedback and continued model turns.
- Disturbance / variety regulated: User requirements, changing code/build/test state, tool errors and provider response variability.
- Decisive decision or feedback right: Choose and execute task-specific files, shell and code actions and adapt to tool results.
- Decision owner: Hosted Grok Build root coding agent with model-guided tool call decisions.
- Supporting / enforcement mechanisms: Rust xai-grok-shell agent runtime, model sampler, xai-grok-tools, VCS/workspace interfaces, permission and stop policies.
- Closure path: User coding goal → model selects tool/action → tool effect → new observations → model continuation/finish.
- Boundary reachability: Official terminal/headless/ACP `grok` modes activate the model/task/tool Rust agent from the packaged root shell and connect to first-party workspace tool operations.
- Why this is / is not agent-owned: The first-party root uses actual task-conditioned model/tool execution; deterministic policy and tool runner restrict, but do not replace, the choice of coding actions.
- Evidence: [crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs); [README.md](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/README.md)
- Basis: structural
- Confidence: high
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## S2 — Coordination

- State: ?
- Function: Candidate coordination of concurrently operating subagent S1 units; no proven specific cross-child disturbance arbitration beyond quotas/queue and opt-in checkout separation.
- Distinct S1 units: Independent child coding-agent tasks with separate subagent identifiers and optional worktrees.
- Inter-S1 disturbance: Possible shared-workspace concurrent edits/collisions; source offers isolation but not a proven content-specific arbitration trigger.
- Attenuating coordination relation: Bounded coordinator admission and optional worktree isolation are available, but not demonstrated as detecting a particular inter-S1 disturbance and returning corrective coordination.
- Feedback into subsequent S1 behaviour: Child completion/query and queue release inform the parent; a specific cross-child interference remedy is unproven.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: S2 not credited; the observed controls could be generic concurrency limits, session lifecycle and optional separation.
- Disturbance / variety regulated: Possible overlapping child changes to a shared workspace, exhaustion of concurrency slots, stale child messages.
- Decisive decision or feedback right: Subagent spawn admission is bounded, and optional `isolation=worktree` alters child workspace; no definite interference-dependent S2 owner/feedback path located.
- Decision owner: Coordinator actor and parent/root choice; function-specific S2 ownership unresolved.
- Supporting / enforcement mechanisms: Single-writer coordinator, `Admission` concurrency ceiling, pending/active queues, worktree option and separate child lifecycle.
- Closure path: Child events pass through queued/active lifecycle, but no demonstrated inter-child content-conflict sensor and returned remedial assignment has been established.
- Why this is / is not agent-owned: Concurrency caps, independent child actors and worktree isolation alone are not evidence of a cross-S1, conflict-specific regulation loop.
- Evidence: [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/admission.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/admission.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/mod.rs)
- Basis: unknown
- Confidence: low
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## S3 — Inside-and-now control

- State: A
- Function: Root coding agent controls current child task commitments, interrupts and collects returned subordinate results in its own team recursion.
- Whole-system current view: Parent/root has child task list, pending/active/completed state and returned outputs in its own session's bounded team.
- Current-control decision scope: Child task commitments, start/stop, future instructions and result integration within one coding-team run.
- Disturbance / variety regulated: Running, queued or stalled subagent tasks, completion/failure and changes to parent coding goal.
- Decisive decision or feedback right: Model-root may invoke task spawn, inspect running children, await child outputs, send child messages and cancel/redirect child tasks.
- Decision owner: Model-driven Grok Build parent/root agent using packaged task and subagent lifecycle tools; coordinator implements these decisions.
- Supporting / enforcement mechanisms: Task tool, coordinator registry, list/query/kill controls, active message delivery, root/child ownership enforcement.
- Closure path: Child progress and completion → coordinator result/query to parent → root model selects further task/message/cancel or integrates child output → changed child activity.
- Boundary reachability: First-party Task/subagent query/cancel/message interfaces are wired to the parent agent and coordinator and admit actual independent worker attempts rather than merely showing a static status dashboard.
- Why this is / is not agent-owned: The model root chooses consequential team task commitments based on child outcomes, not merely reading one worker's progress bar.
- Evidence: [crates/codegen/xai-grok-shell/src/extensions/task.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/task.rs); [crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/subagent/spawn.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator/query.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator/query.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs)
- Basis: structural
- Confidence: medium
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## S3* — Complementary audit

- State: ?
- Function: No established independently sourced complementary audit of the producing coding agents or team current-operation claims.
- Claim being audited: That the child or root-produced code actually fulfills its requested task.
- Ordinary reporting path: A completed child returns a result into the parent Task/output and coordinator message path.
- Complementary access path: Unresolved; neither cloud inline review comment records nor an optional reviewer persona prove separately observed source/evidence.
- Independence boundary: A separately executing auditor with direct artifact sampling and corrective feedback is not established at the declared mode.
- Who acts on findings: Parent may act on child output/messages, but no guaranteed complementary audit finding route was identified.
- Disturbance / variety regulated: Erroneous developer work, unverified result claims and hidden defects.
- Decisive decision or feedback right: A separate reviewer persona/agent can be requested as a child, but guaranteed independent direct-source observational audit and corrective return are not established as a shipped built-in closure.
- Decision owner: Unresolved; review-comment extension stores UI events and is not an independent auditing agent.
- Supporting / enforcement mechanisms: Subagent task/persona facilities; ACP review extension; standard tool feedback.
- Closure path: Review comments/child messages may be consumed by root, but source-to-independent-reviewer audit → corrective control path is unproven.
- Why this is / is not agent-owned: A review UI event or model-provided reviewer persona is insufficient without materially independent observation and change in current work.
- Evidence: [crates/codegen/xai-grok-shell/src/extensions/review.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/review.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/coordinator.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/backend_tests.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/backend_tests.rs)
- Basis: unknown
- Confidence: low
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Memory, task planning and persistent/long-running sessions are present, but no complete outside-and-then foresight and adaptation closure is established.
- External distinction: Workspace and model inputs may refer to external trends or code, without an identified sensing-and-foresight role.
- Future / prospective distinction: Persisted memory and long-running tasks affect later operations, but future time alone is not a prospective decision.
- Adaptation option generated: Not established as a future organizational capability redesign choice.
- Path back into current capability / S3: Memory/session resume can influence subsequent coding decisions; strategic capability-change closure remains unresolved.
- Disturbance / variety regulated: Changed future user coding needs, project architecture and external developments.
- Decisive decision or feedback right: Model can adapt a present coding plan and maintain memory, but capacity-changing future-oriented decision ownership is unresolved.
- Decision owner: Unresolved between user/configuration and model decisions on immediate tasks.
- Supporting / enforcement mechanisms: xai-grok-memory, session resume, task tools and configuration.
- Closure path: Saved context returns to future model tasks, without an established external prospective option/apply loop.
- Why this is / is not agent-owned: Persistent memory or near-term task planning is not automatically VSM S4.
- Evidence: [crates/codegen/xai-grok-memory/src/lib.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-memory/src/lib.rs); [crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs); [crates/codegen/xai-grok-shell/src/extensions/task.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/extensions/task.rs)
- Basis: unknown
- Confidence: low
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## S5 — Policy and identity

- State: ?
- Function: Product identity, permissions and policy constrain operations but do not yet establish a function-specific ultimate-policy closure.
- Identity / ultimate-policy issue: What Grok Build root/team is ultimately allowed to do and for whom.
- Ultimate authority in each claimed mode: No confirmed ultimate-policy actor at this recursion; session credentials and user permission gates exist but do not qualify by themselves.
- Return-to-operation path: Sandbox and permission decisions filter tool actions, without a demonstrated complete governing policy feedback path.
- Disturbance / variety regulated: User trust, sandbox boundaries, resource access and model policy.
- Decisive decision or feedback right: Runtime and human user authorize particular actions; no definitive highest-policy actor and feedback reorganization demonstrated.
- Decision owner: Unresolved at project coding-team recursion; user permission enforcement is not enough to credit S5=P.
- Supporting / enforcement mechanisms: Sandbox restrictions, workspace permissions, client authentication and configuration.
- Closure path: Allowed/denied actions change execution, but an ultimate identity/policy choice returned across organizational operation is not established.
- Why this is / is not agent-owned: Enforcing sandbox or workspace permissions is narrower than ultimate organizational policy authority.
- Evidence: [crates/codegen/xai-grok-sandbox/src/lib.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-sandbox/src/lib.rs); [crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-shell/src/agent/mvp_agent/mod.rs); [crates/codegen/xai-grok-tools/src/implementations/grok_build/task/root_control.rs](https://github.com/xai-org/grok-build/blob/4247f661689354b831191f11eeeac8424993fe3d/crates/codegen/xai-grok-tools/src/implementations/grok_build/task/root_control.rs)
- Basis: unknown
- Confidence: low
- Caveats: The review is at one frozen source SHA without a model-backed runtime benchmark; absent proof is not treated as universal impossibility.


## Recursion

The root's immediate task-level code execution and delegated child coding agents are S1 units. Root-owned model decisions over outstanding children may instantiate S3 at that parent/team recursion, without crediting external providers or platform-wide governance. The single-writer coordinator and worker quota are technical concurrency mechanisms; they are not by themselves S2.

## Variety and escalation

Model/tool feedback and task continuation absorb coding-environment variety. Subagent status/output and active messages return disturbances to the parent; cancellation and worktree safety are bounded controls. Inline review events, approval dialogs, memory retention and persistence alone do not qualify S3*, S5 or S4.

## Evidence gaps

Static source-first assessment at exact pinned SHA. Verify a concrete inter-child write-conflict sensor/attenuation feedback before S2 credit, first-party independent operational-artifact sampling before S3* credit, external-future adaptation/return before S4, and legitimate ultimate-policy owner/return before S5. Unknown states deliberately preserve those plausible paths instead of making unsupported negative assertions.

