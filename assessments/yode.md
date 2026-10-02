---
harness_id: yode
project_name: Yode
repository: https://github.com/anYuJia/yode
review_ref: 964d6230afb5e779e3157a452dac1c0ac0d24f16
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Yode

## Review boundary

- System in focus: the first-party Yode desktop coding organization at frozen revision `964d6230afb5e779e3157a452dac1c0ac0d24f16`, including the supported Tauri desktop runtime and the shipped `yode-core`, `yode-agent`, `yode-tools`, and `yode-runtime` composition used for coding turns, sub-agents, team/DAG orchestration, worktree isolation, verification/review, recovery, and persistent runtime state.
- Purpose and identity: perform long-running repository work through a model/tool coding loop that can plan, edit, run commands, delegate to independent sub-agents, coordinate concurrent workstreams, verify changes, recover from failures, and expose persistent run/team evidence to the desktop application.
- Relevant environment: selected repository/workspace; user goal and approval decisions; project/user/managed instruction and permission layers; model-provider responses; git/worktree state; shell/test/LSP/browser/MCP results; sub-agent task state; persisted `.yode/` artifacts.
- Standard-distribution boundary: the supported `apps/yode-desktop` product plus first-party Rust runtime/tool crates directly used by it are inside. External model providers, MCP servers, browser/network services, git itself, host OS, and target-project behavior remain dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `crates/yode-core/src/engine*`; `crates/yode-agent/src/{planning,orchestration,manager}.rs`; `crates/yode-tools/src/builtin/{agent,coordinator,team_runtime,verification_agent,review_pipeline,review_then_commit}/*`; `crates/yode-tools/src/worktree_coordinator.rs`; desktop Tauri runtime/permission composition.
- Adjacent first-party surfaces excluded from ownership: repository development/optimization reports and release CI, benchmark/evaluation artifacts not wired as runtime decision owners, future-looking plans, and documentation-only parity analysis.
- First-party operating / deployment modes considered: ordinary desktop coding turns; plan mode; foreground/background sub-agents; named teams; `coordinate_agents`; `team_run_ready`; worktree-isolated mutating agents; verification/review pipelines; persistent runtime tasks; user/managed permission modes.
- Recursion level: one Yode-managed repository work organization. The primary coding actor and delegated sub-agents are S1 units when they independently execute repository work. The main model-backed Yode agent can act as the current-control actor above those S1s; deterministic worktree/DAG machinery supplies constructor coordination around them.
- Reviewed revision: `964d6230afb5e779e3157a452dac1c0ac0d24f16`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Yode's supported surface is the desktop application rather than a root CLI. The Tauri runtime builds a first-party `AgentEngine` over model, tool, permission, session, cancellation, context, persistence and event services. The engine repeatedly exchanges model decisions and tool/environment results and persists the resulting turn state.

Sub-agents are not prompt-only placeholders. The shipped sub-agent runner creates separate `AgentEngine` instances with their own context/tool registry, optional background lifecycle, task state, team identity, and restricted allowed-tool surface. Team state records member status, task IDs, result previews, messages, plan progress and persistent monitor/bundle artifacts.

Yode ships two related coordination layers. `coordinate_agents` accepts model-authored workstreams/dependencies and executes dependency phases with bounded parallel batches while feeding prerequisite outputs to later workstreams. Separately, the team planner/runtime exposes ready/blocked/running/completed/failed state and can launch only dependency-ready members.

Yode contains worktree primitives and a `WorktreeCoordinator`, and its multi-repository executor uses that coordinator for mutating multi-repo steps. However, at the assessed desktop/team recursion the `coordinate_agents` and ordinary team/sub-agent paths do not wire `WorktreeCoordinator::should_auto_isolate`; `coordinate_agents` launches its workstreams with `isolation: None`. Explicit worktree isolation is therefore a capability a caller may request, not an established automatic inter-S1 coordination loop for the supported team path.

Verification is a separate first-party agent path. The `verification_agent` launches a dedicated verification sub-agent with a restricted inspection/test-oriented tool set. `review_pipeline` combines review plus verification results and, by default, returns a recoverable validation error and skips commit when either path reports findings. `review_then_commit` likewise aborts commit on review findings unless explicitly overridden.

Yode also stores postmortems and derived lessons. At the frozen revision, however, the retrieval method for relevant lessons is not wired back into the operational agent path; the learning store is retrospective persistence rather than a closed outside-and-future adaptation loop.

## Operational model

A user starts a desktop coding turn. The model-backed Yode agent receives current instructions/context and selects first-party tools. It may work directly or construct sub-agent/team work, inspect live team state, message members, run ready work, invoke verification/review, and react to returned evidence. Sub-agents execute in separate model/tool loops and return results through tool/task/team state.

Team/DAG state and monitor artifacts give the main agent a current view of active, completed, failed and blocked work. The main agent can then change current execution through further delegation, messages, ready-step dispatch and other tool decisions. Although Yode exposes worktree isolation primitives, the reviewed standard team/coordinator path does not automatically connect them to concurrent mutating team members, so that mechanism is not credited as S2 closure here.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering work by inspecting code/state, choosing tools, editing files, running commands/tests, and revising actions from returned evidence.
- Disturbance / variety regulated: heterogeneous repository structure, incomplete task requirements, command/test failures, code and git state, provider responses, permissions, context pressure, and changing workspace evidence.
- Decisive decision or feedback right: choose the next substantive coding action, tool use, direct edit/command, delegation step, and completion response within the configured authority boundary.
- Decision owner: the model-backed Yode `AgentEngine` actor; delegated sub-agents instantiate the same class of autonomous operational actor at lower recursion.
- Supporting / enforcement mechanisms: tool registry; context/session persistence; permissions; cancellation; retry/recovery hints; LSP/search/git/browser/MCP tools; sub-agent runner; desktop event/runtime state.
- Closure path: user goal + workspace/context → model decision → first-party tool/sub-agent action → environment result/event → result returns into the model context → next coding decision or completion.
- Boundary reachability: the supported desktop runtime directly instantiates this loop; downstream application code is not required to supply the core coding actor.
- Why this is / is not agent-owned: removing the model-backed engine leaves execution, persistence and safety machinery but removes the open-ended task-specific coding choices.
- Evidence: [`README.md`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/README.md); [`crates/yode-core/src/engine.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/engine.rs); [`crates/yode-core/src/engine/subagent_runner.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/engine/subagent_runner.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is external; the assessment credits Yode's first-party role/tool/feedback composition rather than provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party S2 loop was established at the selected desktop/team recursion.
- Disturbance / variety regulated: concurrent model-backed team members can in principle contend over shared repository state, but the reviewed standard team/coordinator path does not itself connect that disturbance to an operational attenuation loop.
- Decisive decision or feedback right: none established for S2. The main agent may choose dependencies, `max_parallel`, or explicit worktree isolation, but those are delegation/scheduling/capability choices without a demonstrated shipped relation that detects or structurally maps an actual inter-S1 interference and feeds attenuation back into the affected S1 units.
- Decision owner: none established.
- Supporting / enforcement mechanisms: dependency DAGs, bounded parallel batches, team messaging/state, optional explicit sub-agent `isolation: "worktree"`, standalone worktree tools, and a `WorktreeCoordinator` used by the separate multi-repository executor.
- Closure path: not applicable at this recursion; no standard desktop/team path was found that takes a concrete inter-S1 conflict/oscillation, applies a coordination relation to it, and returns the result into subsequent behavior of the affected team S1s.
- Why this is / is not agent-owned: the model can decide how to delegate and can explicitly request isolation, but generic sequencing, concurrency limits, messaging and optional isolation capability do not by themselves establish the S2 function.
- Evidence: [`crates/yode-agent/src/planning.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-agent/src/planning.rs); [`crates/yode-tools/src/builtin/coordinator/mod.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/coordinator/mod.rs); [`crates/yode-core/src/engine/subagent_runner.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/engine/subagent_runner.rs); [`crates/yode-tools/src/worktree_coordinator.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/worktree_coordinator.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `yode-runtime::multirepo` does use `WorktreeCoordinator` for mutating multi-repository steps, but PRODUCT.md places Multi-repo Agent in P2 and the reviewed supported desktop/team organization does not establish that as its normal inter-S1 coordination path.

### Absence scope

- Surfaces inspected: team planner and ready-batch scheduler; `coordinate_agents`; ordinary and background sub-agent runner; team messages/monitoring; explicit sub-agent isolation; standalone worktree tools; `WorktreeCoordinator`; multi-repository runtime; product/runtime boundary documentation.
- Plausible first-party paths checked: dependency ordering as conflict attenuation; `max_parallel` as S2; team mailboxes/shared state as S2; automatic worktree isolation for mutating team members; explicit `isolation: "worktree"`; multi-repo worktree merge serialization.
- Why no material first-party path remains: dependency/sequencing and messaging are generic mechanisms, `coordinate_agents` passes `isolation: None`, code search finds `should_auto_isolate` only at its definition, explicit isolation is not tied to a demonstrated conflict/feedback relation, and the multi-repo executor is not established as the supported desktop/team recursion being assessed.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of the multi-agent coding organization and make task/worker execution decisions over active, ready, blocked, completed and failed work.
- Disturbance / variety regulated: changing worker/task status, dependency readiness, background execution, failures, pending messages, returned workstream results and current orchestration progress.
- Decisive decision or feedback right: the main model-backed agent can choose team/workstream decomposition, dependencies and concurrency, inspect current team state, send new guidance/handoffs, invoke ready-step execution, request/inspect background task output, and choose subsequent current-work interventions.
- Decision owner: the main model-backed Yode agent using first-party team/coordinator/task tools.
- Whole-system current view: `team_monitor` and persisted `AgentTeamState` expose the current team goal/plan plus member counts and member-level planned/running/completed/failed status, ready/blocked/running/completed/failed plan progress, runtime task IDs, result previews and pending team messages.
- Current-control decision scope: the main agent can choose/decompose workstreams, dependencies and concurrency, launch or continue current team work through `team_run_ready` / sub-agent tools, send mid-course guidance through `send_message`, inspect current/background results, and create follow-up work in response to failures or completion evidence.
- Supporting / enforcement mechanisms: `AgentTeamManager`; persisted team state/monitor/bundle artifacts; `team_monitor`; `team_run_ready`; `send_message`; runtime task store; dependency planner; deterministic status reconciliation.
- Closure path: current team/task state is exposed to the main agent → the agent interprets current progress/failure/blocked state → selects a current-control action such as dispatching ready work, changing decomposition/concurrency, sending guidance or launching follow-up work → first-party runtime updates worker/team state → the resulting state/output returns for subsequent decisions.
- Boundary reachability: team/coordinator tools are part of the shipped desktop agent tool surface and sub-agent runtime; they are not merely an external SDK substrate.
- Why this is / is not agent-owned: deterministic managers expose/enforce state, but removing the main model-backed agent removes the discretionary current-work decisions over what to delegate, how to sequence/parallelize, and how to respond to live results.
- Evidence: [`README.md`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/README.md); [`crates/yode-tools/src/builtin/coordinator/mod.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/coordinator/mod.rs); [`crates/yode-tools/src/builtin/team_runtime/mod.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/team_runtime/mod.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the deterministic DAG executor alone is not credited as S3 ownership. The positive classification depends on the main model actor's access to current team state plus its first-party intervention tools.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation claims and return findings into a path that can block delivery/commit or trigger corrective work.
- Disturbance / variety regulated: false completion, regressions, missing test coverage, risky assumptions, build/test failures and implementation errors not caught by the implementing S1.
- Decisive decision or feedback right: a separate model-backed review/verification agent inspects current workspace evidence and produces findings/judgment; that judgment determines whether the review pipeline may proceed to commit absent explicit override.
- Decision owner: the dedicated model-backed verification/review sub-agent.
- Claim being audited: that the implementation/current workspace changes are correct and safe enough to proceed toward delivery or commit.
- Ordinary reporting path: the implementing main/worker S1 returns its own completion text, tool results and team/task result state through the normal coding loop.
- Complementary access path: `verification_agent`, `review_changes`, `review_pipeline`, and `review_then_commit` launch a separate sub-agent that directly inspects git/workspace state and may run targeted tests/commands with a review-specific tool allowlist.
- Independence boundary: the audit actor is a fresh model-backed `AgentEngine`/sub-agent with a distinct review or verification prompt, conversation context and restricted evidence-gathering tool surface; it is not the implementing S1 merely rereading its own conclusion.
- Who acts on findings: the first-party review pipeline deterministically returns a recoverable validation failure and skips commit by default; the parent/main agent receives the findings/error and can correct the implementation and rerun the audit.
- Boundary reachability: the dedicated verification/review tools and sub-agent runner are shipped in the first-party `yode-tools` / `yode-core` runtime used by the supported desktop composition; no downstream application-authored auditor is required.
- Supporting / enforcement mechanisms: isolated sub-agent runner; restricted inspection/test tool set; persisted review artifacts; findings parsing/counting; deterministic review-pipeline gate; `review_then_commit` commit suppression.
- Closure path: implementation exists → fresh verification/review sub-agent inspects repository/git/test evidence → findings are returned to the parent/tool pipeline → findings cause a recoverable validation failure and commit is skipped by default → subsequent agent work can address findings before retrying verification/commit.
- Why this is / is not agent-owned: the runtime gate is deterministic support, but the complementary audit judgment is produced by a separate model-backed actor with direct workspace/test access rather than by the implementing S1.
- Evidence: [`crates/yode-tools/src/builtin/verification_agent/mod.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/verification_agent/mod.rs); [`crates/yode-tools/src/builtin/review_pipeline/execution.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/review_pipeline/execution.rs); [`crates/yode-tools/src/builtin/review_then_commit/execution.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/review_then_commit/execution.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: confirmation requirements constrain execution authority but do not move the audit judgment away from the independent verification/review actor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop was established.
- Disturbance / variety regulated: Yode records postmortems, failures, verification evidence and lessons, performs current-run recovery hints, supports repository/web intelligence and can persist memory; these mechanisms do not close a future-oriented adaptation loop that changes organizational capability/strategy.
- Decisive decision or feedback right: none established for prospective capability adaptation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `LearningStore`; postmortem/lesson persistence; current-run failure/retry hints; repository intelligence/indexes; memory/instruction loading; evaluation artifacts.
- Closure path: no standard path was found from external/future distinctions through adaptation-option selection into a persistent change of Yode's current organizational capability. At the frozen ref, `relevant_lessons()` is defined in the learning store but is not consumed by the operational agent runtime.
- Why this is / is not agent-owned: retrospective lesson derivation and present-run recovery can improve continuity/behavior without constituting the required outside-and-future intelligence function.
- Evidence: [`crates/yode-core/src/learning.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/learning.rs); [`crates/yode-core/src/engine/intelligence_runtime.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/engine/intelligence_runtime.rs); [`crates/yode-core/src/instructions.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/instructions.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: README language such as “Evaluate / Postmortem / Learn” is not promoted to S4 without operational prospective-adaptation closure.

### Absence scope

- Surfaces inspected: learning/postmortem store; runtime failure-intelligence/recovery hints; instruction/memory loading; repository intelligence; evaluation artifacts; workflow/sub-agent/team layers.
- Plausible first-party paths checked: lessons automatically injected into later runs; postmortem-driven strategy/capability mutation; autonomous skill/policy adaptation; external trend/future monitoring; evaluation-to-runtime capability update.
- Why no material first-party path remains: the learning store records and can query retrospective lessons, but no operational consumer closes them back into later capability; other inspected paths support current execution, operator-supplied instructions or offline evaluation rather than prospective organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity or ultimate-policy decision loop was established.
- Disturbance / variety regulated: user, managed, project and local instruction/permission layers constrain tool authority; plan-mode approval and per-tool confirmations constrain execution.
- Decisive decision or feedback right: none established for an identity/ultimate-policy issue. Managed/user configuration can set stronger operating constraints, but no runtime S5 actor receives an identity-level issue, decides the organization's governing purpose/policy, and returns that decision into later operation.
- Decision owner: none established inside the assessed Yode organization.
- Supporting / enforcement mechanisms: managed/user/project/local permission layers; project instructions; plan-mode approval; tool confirmation requirements; workspace trust and deny rules.
- Closure path: no identity/ultimate-policy issue → legitimate S5 authority → authoritative policy decision → returned governance path was found.
- Why this is / is not agent-owned: static or externally edited configuration and permission enforcement define the operating envelope but do not themselves constitute runtime S5 ownership.
- Evidence: [`apps/yode-desktop/src-tauri/src/runtime/turn_permissions.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/apps/yode-desktop/src-tauri/src/runtime/turn_permissions.rs); [`crates/yode-core/src/instructions.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-core/src/instructions.rs); [`crates/yode-tools/src/builtin/plan_mode/mod.rs`](https://github.com/anYuJia/yode/blob/964d6230afb5e779e3157a452dac1c0ac0d24f16/crates/yode-tools/src/builtin/plan_mode/mod.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: generic approvals and managed policy are important governance/safety mechanisms, but Methodology 0.3.6 does not promote them to S5 without function-specific identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: instruction hierarchy; desktop permission layering; managed policy; plan mode and approval; workspace trust; tool confirmation behavior; session/runtime configuration.
- Plausible first-party paths checked: model-authored durable identity rules; autonomous policy revision; admin/user policy as parent S5; plan approval as ultimate governance; project instruction mutation as identity closure.
- Why no material first-party path remains: authoritative values are externally supplied and enforced. No first-party identity-level decision process and return loop was established, and generic human approval/configuration is insufficient.

## Distributed OSS parent arrangement

Open-source maintainers and local operators can alter Yode code/configuration, but repository governance is outside the running Yode work organization assessed here. Managed configuration supplies operating constraints rather than a demonstrated S5 parent loop.

## Self-hosted and non-human modes

Yode can run model-backed S1/S3/S3* decisions after task/configuration input, subject to confirmation and permission constraints. Those approvals are execution controls rather than separate parent-mode ownership of S3/S4/S5, so no `(P)` mode is published.

## Recursion

At the selected recursion, direct coding and delegated sub-agents are operational S1 units. Worktree/DAG machinery coordinates their interference, while the main model-backed Yode agent can regulate current team execution above them. Verification/review sub-agents are complementary auditors rather than ordinary implementation S1s when invoked through the dedicated review paths.

## Variety and escalation

Task/repository variety is absorbed by model-backed coding actors. Constructor coordination isolates concurrent mutations and returns merge conflict/dirty-parent outcomes. Current team state and failures can be surfaced to the main agent for intervention. Verification findings return as recoverable validation failures that can prevent commit. Repeated tool failures also produce deterministic strategy-change hints, but those hints remain S1/recovery support rather than a separate S4 function.

## Evidence gaps

The main residual uncertainty is S3 breadth across every desktop workflow: the repository clearly exposes live team monitoring/intervention and model-selected coordination tools, but some simple single-agent runs never instantiate the multi-agent recursion. The classification therefore applies to the first-party supported team/coordinator mode at the declared organization boundary. No evidence gap was found that requires `?` for the published vector.

## Assessment summary

Yode closes autonomous coding S1, autonomous S3 through the main agent's live team orchestration, and autonomous S3* through separate verification/review agents whose findings can block commit. The reviewed standard team path does not establish S2 beyond generic scheduling/messaging/optional isolation capability, while retrospective learning/current-run recovery and external policy layers do not establish S4 or S5.

Proposed vector: **`A · — · A · A · — · —`**.
