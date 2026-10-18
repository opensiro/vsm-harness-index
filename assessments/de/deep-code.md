---
harness_id: deep-code
project_name: deep-code
repository: https://github.com/liwenka1/deep-code
review_ref: 94199de128d259ad513275db3e84433299a58a9a
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# deep-code

## Review boundary

- System in focus: the first-party Rust deep-code coding-agent runtime at frozen revision `94199de128d259ad513275db3e84433299a58a9a`, including the main model/tool turn loop, coding/search/shell/web/debug tooling, approval and execution policy, OS sandbox integration, persistent sessions/checkpoints, context compaction, model routing, and role-based sub-agent execution.
- Purpose and identity: execute software-engineering tasks against a local workspace through an autonomous coding loop, with bounded delegated investigation/implementation/review and persistent recovery surfaces.
- Relevant environment: user goal and steering, repository/workspace state, tool/shell/build/test results, model-provider responses, approval decisions, configured sandbox/network/write-root policy and persisted session/checkpoint state.
- Standard-distribution boundary: `crates/deep-code-agent`, the shipped TUI/headless/server entry surfaces and their first-party runtime composition are inside. External model endpoints, package/web services, OS sandbox primitives and Git hosting are dependencies. `crates/deep-code-eval` is an adjacent evaluation harness and does not donate ordinary-runtime VSM functions.
- Credited operating / distribution surfaces: interactive TUI, headless `-p`, HTTP/server execution, the first-party `agent` sub-agent tool, role-specific child contexts, permissions/sandboxing, sessions/resume/checkpoints/restore and model routing.
- Adjacent first-party surfaces excluded from ownership: SWE-bench/eval orchestration, repository-development CI/tests, release automation and maintainer governance.
- First-party operating / deployment modes considered: normal single-agent coding, delegated read-only reconnaissance/review/verification, explicit implementer children, parallel child calls inside one parent turn, interactive and unattended/headless execution.
- Recursion level: the parent coding run is the focal S1. A child agent can be a bounded subordinate S1 contribution when it has its own model/tool loop; child-role labels or parallelism do not by themselves establish S2/S3/S3*.
- Reviewed revision: `94199de128d259ad513275db3e84433299a58a9a`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

deep-code ships a first-party Rust agent runtime with a model-driven turn loop and tool registry over repository files, shell/jobs, search, web/debug/LSP and workspace operations. Runtime policy separates deterministic hard safety floors from configurable approval tiers and OS-level sandbox boundaries. Sessions persist and can be resumed; per-turn checkpoints support restore; long contexts are compacted and model routing can select between configured tiers.

The `agent` tool creates a fresh child runtime with a self-contained task and role-specific system prompt. Multiple agent tool calls in one parent turn may execute in parallel. Most child roles are read-only; only `implementer` can write. `review` is explicitly a read-only code-review role producing severity-scored findings, while `verifier` is explicitly a read-only verification role returning PASS/FAIL with command evidence. Each child returns a structured report as the parent tool result.

## Operational model

The parent model receives the coding objective and current context, chooses tool actions, receives concrete results and revises subsequent work. It may delegate a bounded task through the `agent` tool. Child agents start from fresh contexts, directly inspect the current workspace through their allowed tools and return their report to the parent. The parent can then change its own subsequent coding actions based on that result.

## S1 — Operations

- State: A
- Function: autonomously perform coding work through iterative model/tool decisions against the live workspace.
- Disturbance / variety regulated: unfamiliar codebase state, incomplete requirements, command/build/test failures, tool errors, model/provider failures, context growth and permission/sandbox constraints.
- Decisive decision or feedback right: choose the next repository/tool action, revise the approach after returned evidence, delegate bounded sub-tasks and decide when the requested coding work is complete.
- Decision owner: the active model-backed deep-code parent agent; bounded child agents own their delegated local decisions.
- Supporting / enforcement mechanisms: runtime turn loop, first-party tool registry, workspace/shell/web/debug/LSP tools, model routing/retry, approvals, sandbox policy, sessions/checkpoints, compaction and sub-agent execution.
- Closure path: task/context → model selects tool/coding action → runtime/tool returns concrete evidence → evidence re-enters the model context → later action changes until completion, cancellation or bounded failure.
- Boundary reachability: the standard TUI/headless/server product paths directly instantiate the same first-party runtime and tool loop.
- Why this is / is not agent-owned: removing the model actor leaves tools, policy, persistence and sandboxing but removes the open-ended decisions that transform evidence into coding actions.
- Evidence: README; `crates/deep-code-agent/src/runtime/turn_loop.rs`; `crates/deep-code-agent/src/tool/registry.rs`; `crates/deep-code-agent/src/runtime_launch.rs`; `crates/deep-code-agent/src/subagent/tools.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external inference remains a dependency; safety/approval machinery constrains but does not own the coding objective.

## S2 — Coordination

- State: —
- Function: no distinct first-party relation is established that attenuates a specific interference or oscillation among distinct operational S1 units.
- Disturbance / variety regulated: several child agents can run in parallel and implementer children may share the same parent workspace, but the frozen runtime does not expose a peer-collision detection/negotiation loop or shared-resource coordination authority among them.
- Decisive decision or feedback right: no S2-specific choice over inter-S1 conflict or mutual adjustment was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: blocking `agent` calls, child role/tool restrictions, approval gates, timeouts, manager records and parent-side task briefs.
- Closure path: children execute bounded delegated tasks and return reports; deterministic restrictions constrain each child but do not close a specific peer-interference attenuation loop.
- Why this is / is not agent-owned: delegation, parallel execution, permissions and shared workspace state are not S2 without an evidenced inter-S1 disturbance plus coordinating feedback.
- Evidence: README; `crates/deep-code-agent/src/subagent/tools.rs`; `subagent/manager.rs`; `subagent/runner.rs`; `subagent/roles.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: parallel implementers can create practical write interference, but the reviewed runtime does not demonstrate a first-party coordination function that detects and attenuates that disturbance.

### Absence scope

- Surfaces inspected: parent/child runtime, role/tool restrictions, parallel child dispatch, sub-agent manager state, approvals, workspace boundary and checkpoint behavior.
- Plausible first-party paths checked: child parallelism as S2; role separation as S2; manager bookkeeping as S2; approval/sandboxing as conflict coordination.
- Why no material first-party path remains: inspected mechanisms delegate or constrain individual child actions but do not regulate a concrete peer-S1 interference through a coordination decision and returned behavioral adjustment.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function over a standing portfolio of operations is established.
- Disturbance / variety regulated: the parent can choose child tasks and observe returned reports, while runtime limits track child status and timeout/cancellation.
- Decisive decision or feedback right: no separate authority has a whole-system current view plus substantive control over a persistent set of current S1 commitments/resources/priorities on behalf of the whole.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: parent `agent` tool calls, sub-agent manager records, child timeout/cancellation, session/status surfaces and model routing.
- Closure path: an `agent` tool call blocks until the child returns; the result becomes ordinary evidence in the parent S1 loop rather than a distinct persistent whole-current management cycle.
- Why this is / is not agent-owned: model-driven delegation is part of the parent operational strategy; bookkeeping and cancellation are runtime enforcement, not a metasystemic current-control owner.
- Evidence: `crates/deep-code-agent/src/subagent/tools.rs`; `subagent/manager.rs`; README; runtime state/session surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `/agents` and manager records provide observability, but observability plus bounded blocking delegation is insufficient for S3.

### Absence scope

- Surfaces inspected: sub-agent registry/manager, `agent` tool lifecycle, parallel calls, runtime/session state, routing, approvals, checkpoints and unattended/server modes.
- Plausible first-party paths checked: parent as supervisor S3; `/agents` as whole-system current view; child cancellation/timeouts as intervention; model routing as resource control.
- Why no material first-party path remains: child work is scoped to blocking delegated calls and lacks a distinct persistent portfolio-control loop with whole-system current authority.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation/correctness claims by direct read-only inspection or verification and return findings to the producing parent agent.
- Disturbance / variety regulated: implementation defects, incorrect assumptions and unverified completion claims that may survive the producer's own reasoning.
- Decisive decision or feedback right: the reviewer/verifier child model decides which observed evidence constitutes a material review finding or PASS/FAIL conclusion and reports that judgment to the parent.
- Decision owner: the separate model-backed `review` or `verifier` child agent.
- Supporting / enforcement mechanisms: fresh child context, explicit read-only role policy, role-specific review/verifier prompts, direct repository/search/read/shell access, dedicated fast-tier model selection and structured child report return.
- Closure path: parent/implementer produces or proposes work → parent dispatches read-only review/verifier child → child directly inspects workspace and/or runs verification gates → structured findings/PASS-FAIL return as the `agent` tool result → parent changes subsequent coding/repair action based on the audit result.
- Boundary reachability: `review` and `verifier` are shipped first-party role aliases accepted by the standard `agent` tool; no external reviewer product is required.
- Why this is / is not agent-owned: removing the reviewer/verifier model leaves role restrictions and tool plumbing but removes the independent semantic judgment over inspected evidence.
- Evidence: README; `crates/deep-code-agent/src/subagent/roles.rs`; `subagent/tools.rs`; `subagent/runner.rs`; `subagent/registry.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dispatch is chosen by the parent and is not mandatory for every coding task; the positive state concerns the supported first-party complementary-audit mode.

- Claim being audited: that the implementation/workspace state is correct enough, free of material review defects, or passes the requested verification gates.
- Ordinary reporting path: the producing parent or implementer child reports its own completion/result through the normal model/tool/sub-agent return path.
- Complementary access path: a fresh read-only review/verifier child directly reads/searches the current workspace and can run allowed verification commands rather than relying on producer self-report.
- Independence boundary: reviewer/verifier has a separate model context and role prompt, cannot write files, and therefore cannot silently repair the object it is auditing.
- Who acts on findings: the parent coding agent receives the child report as a tool result and can revise code, dispatch an implementer or run further verification.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: model routing, persistent sessions, compaction, skills/configuration and web access can change how current or later tasks are executed.
- Decisive decision or feedback right: no first-party actor was found that senses external/future change, generates organizational adaptation options and installs a selected adaptation into later capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: model router, skills loading, sessions/checkpoints, web tools, compaction and configuration.
- Closure path: these mechanisms support current task execution, recovery or operator-selected capability, not a separate outside-and-then adaptation conversation.
- Why this is / is not agent-owned: persistence, external lookup and model selection are not sufficient for S4 without prospective environmental distinction and adaptation-option closure.
- Evidence: README; model-routing, skills, session and compaction modules under `crates/deep-code-agent/src`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: no reviewed first-party self-evolution/update path changes reusable capability from cross-task environmental evidence.

### Absence scope

- Surfaces inspected: model routing/fallback, skills, sessions/checkpoints, context compaction, web/debug/LSP tools, sub-agent roles and update/install documentation.
- Plausible first-party paths checked: skills as S4; web access as external sensing; model auto-routing as adaptation; persisted sessions/checkpoints as learning.
- Why no material first-party path remains: all inspected paths serve current execution or static/operator-selected configuration and do not close prospective adaptation into future capability.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: permission modes, approval memory, hard deny floors, sandbox/write-root/network policy and role restrictions constrain ordinary execution.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to legitimate ultimate authority and returned as a durable governing system decision.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: permission tiers, approval classifier/human approval, execution-policy engine, sandbox policy, write-root grant boundary, child role restrictions and configuration.
- Closure path: these mechanisms approve/refuse specific operational actions or configure execution posture; they do not settle identity-level policy questions for subsequent system operation.
- Why this is / is not agent-owned: safety policies and human approval gates are operational constraints, not S5 by themselves.
- Evidence: README; `approval_classifier.rs`; `runtime/approval_flow.rs`; `execution_policy/engine.rs`; `sandbox/policy.rs`; `subagent/roles.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the operator has meaningful authority over permissions and write/network grants, but ordinary action approval does not create an identity-level S5 return loop.

### Absence scope

- Surfaces inspected: all permission tiers, hard deny floor, auto-classifier, write-root approvals, network policy, sandbox configuration, child role permissions and repository governance.
- Plausible first-party paths checked: permission modes as S5; human approval as ultimate authority; hard safety floor as constitution; role restrictions as identity policy.
- Why no material first-party path remains: inspected controls govern concrete action authorization and safety, while development governance is adjacent; no identity-policy issue → legitimate authority → authoritative decision → returned durable operation path is established.

## Recursion

Child agents have fresh model contexts and bounded tool environments, so they may own local S1 contributions. The assessment does not infer a complete recursive viable system from nesting: child roles are intentionally subordinate to the parent task and lack independent higher-system closure.

## Variety and escalation

The main coding loop absorbs operational variety through iterative tool use, model routing, approvals, sandbox enforcement, context compaction and persistent recovery. Bounded child agents let the parent offload investigation, implementation and complementary review/verification. Findings and failures return to the parent for subsequent action; hard policy denials or unavailable approvals constrain or stop execution.

## Evidence gaps

No `?` state is required. The frozen source exposes the agent loop, child-role semantics, tool restrictions, report return path, permissions and persistence directly enough to support S1/S3* and the documented negative conclusions for S2/S3/S4/S5.

## Assessment summary

deep-code closes autonomous S1 through its first-party model/tool coding loop and closes autonomous S3* through separate read-only reviewer/verifier child contexts whose findings return to the parent. Parallel sub-agent delegation does not establish S2, blocking child management does not establish whole-current S3, persistence/routing/skills do not close S4, and execution policy/approvals do not establish S5.

**Vector:** A · — · — · A · — · —
