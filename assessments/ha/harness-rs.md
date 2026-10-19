---
harness_id: harness-rs
project_name: Harness RS
repository: https://github.com/liliang-cn/harness-rs
review_ref: eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Harness RS

## Review boundary

- System in focus: The shipped first-party Rust `harness-rs` **model-backed agent operating cell**, with explicit optional packaged `experience::SkillDistiller::distill_and_write` post-run skill-learning mode. This is one task-facing `AgentLoop` and the separately opt-in procedural experience component, not a claim that every deployment runs self-learning by default, and not a multi-organization VSM recursion.
- Purpose and identity: Receive a task, use model-selected authorized tools and feedback to complete or bound its execution; optionally turn successful multi-tool episodes into reusable skill instructions for later task execution.
- Relevant environment: Variable human user goals, tool/shell/filesystem and web observations, differing provider output, errors/timeouts, budget and context length, sensor/acceptance failures, episodic outcomes, skill applicability, platform sandbox permissions and possible competing child tasks.
- First-party standard distribution: published Rust crates `harness-loop`, `harness-core`, `harness-context`, `harness-models`, `harness-tools`, optional `harness-serve`, and the public AgentLoop/Experience APIs. The model provider, user-written guides/hooks/goals/business logic, third-party orchestration or human approval process are not bundled first-party authorities.
- Credited operating / distribution surfaces: [README.md#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/README.md#L1), [crates/harness-loop/src/lib.rs#L647](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L647), [crates/harness-loop/src/lib.rs#L1008](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1008), [crates/harness-loop/src/lib.rs#L1446](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1446), [crates/harness-loop/src/lib.rs#L1561](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1561), [crates/harness-loop/src/lib.rs#L1744](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1744), [crates/harness-loop/src/experience/mod.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L1), [crates/harness-loop/src/experience/distill.rs#L259](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L259), [crates/harness-loop/src/experience/distill.rs#L416](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L416), [crates/harness-tools/src/skills.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-tools/src/skills.rs#L1).
- Adjacent first-party surfaces excluded from ownership: benchmark scripts, example vertical applications, repository test and CI systems, docs' future milestones, developer-assigned agent/organization roles, uninstalled host plugins and actual remote LLM provider internals. A generic Hook, configured Policy, AuditHook, scheduler or subagent API is credited as infrastructure only until function-specific ownership is demonstrated.
- Supported operating / deployment modes checked: `AgentLoop::new(model)` with registered typed tools and `run`, `run_with_max_iters`, `run_goal`, session turns, sensor/acceptance/hook feedback, CLI/service transport, optional explicit composition with `ExperienceRecorder`, `ExperienceGuide`, `SkillDistiller::distill` as **draft-only**, and opt-in `SkillDistiller::distill_and_write` writing into a first-party loadable skills directory. Default plain AgentLoop is not represented as autonomously scheduling post-run distillation.
- Recursion: The immediate S1 is a model/tool agent solving a user-assigned task, optionally a separately packaged model skill-improvement mode serving later instances of the same general operating capability. Subagents and finite orchestrator jobs are delegated operations; no separate independently viable S1 portfolio and manager is imported just because the SDK permits composition.
- Frozen identity: GitHub repo ID **1240445699**, public MIT licensed `liliang-cn/harness-rs`, default `main@eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329`, Git tree `3bf82f9d38ac133a7db5249450ef837373f66d1b`, [batch #1741](https://github.com/opensiro/vsm-harness-index/issues/1741). Reviewed 2026-10-19, Profile 0.2.4 and Methodology 0.3.7.

## Repository architecture

`AgentLoop` wraps the caller-supplied `Model`, a registry of first-party typed tools, hooks, guides, sensors, acceptance checks, sandbox and context. Public `AgentLoop::run` reaches the actual ReAct loop, which asks `self.model.complete` / `stream` for tool calls or user-facing response. Tool requests are checked through PreToolUse hooks, dispatched against declared tool handlers, and returned as observations; PostToolUse hooks, auto-correct sensors and acceptance-check failures can feed reasons back into later model iterations. This is a source-connected model↔tool operating path, not solely a Model trait. [crates/harness-loop/src/lib.rs#L647](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L647); [crates/harness-loop/src/lib.rs#L1008](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1008); [crates/harness-loop/src/lib.rs#L1561](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1561); [crates/harness-loop/src/lib.rs#L1744](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1744); [crates/harness-loop/src/lib.rs#L1793](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1793); [crates/harness-loop/src/lib.rs#L1894](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1894); [crates/harness-loop/src/lib.rs#L2215](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L2215).

An explicitly optional `ExperienceRecorder` captures tool traces and episode outcomes; `ExperienceGuide` can recall those experiences as a guide for a new task. More importantly, `SkillDistiller` checks success, number of tools and duplicate skills, asks a configured model to generalize one successful episode into a reusable SKILL.md draft, and in its public **opt-in** `distill_and_write` mode writes it directly under the configured skills root. The first-party `harness-context` scans the same documented root and `harness-tools` exposes skill management/loading to following agents. This source-backed option→persist→available-next-run path is credited as a bounded **S4=A operating mode**, not a claim that default AgentLoop auto-distills every conversation. The default, explicitly recommended multi-tenant mode returns `SkillDraft` for host/user approval, with no automatic adoption; it is not borrowed as an autonomous approval right. [crates/harness-loop/src/experience/mod.rs#L20](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L20); [crates/harness-loop/src/experience/mod.rs#L54](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L54); [crates/harness-loop/src/experience/distill.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L1); [crates/harness-loop/src/experience/distill.rs#L244](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L244); [crates/harness-loop/src/experience/distill.rs#L367](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L367); [crates/harness-loop/src/experience/distill.rs#L416](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L416); [crates/harness-tools/src/skills.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-tools/src/skills.rs#L1).

The package offers subagent/orchestrator/scheduler and serving components, sandbox and human gate capabilities. These show composability and bounded task control, but they do not by themselves prove distinct VSM coordination/executive/audit/identity ownership at a specified organization recursion. `AuditHook` records who/what/when but does not independently audit an S3-owned picture of reality. [crates/harness-loop/src/orchestrator/orchestrator.rs#L26](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/orchestrator/orchestrator.rs#L26); [crates/harness-loop/src/scheduler/scheduler.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/scheduler/scheduler.rs#L1); [crates/harness-loop/src/subagent.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/subagent.rs#L1); [crates/harness-loop/src/hooks/mod.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/hooks/mod.rs#L1).

## Operational model

A model uses a preconfigured model/tool operating loop to regulate task results; configured sensors and acceptance checks correct immediate execution. Optional successful-episode distillation makes future skill/procedural capabilities available after a new file is written. Host-selected model, hooks, guide/skill dirs, policy and any human approval remain externally chosen; not all are autonomous management functions.

## S1 — Operations

- State: A
- Function: Choose and execute context-dependent steps, tools and responses for task completion using observed action feedback.
- Disturbance / variety regulated: Heterogeneous user tasks, tool outcomes, changed workspace state, execution errors, failed acceptance and context-size pressure.
- Decisive decision or feedback right: The configured `Model` behind `AgentLoop` selects tool names/arguments or final output based on current context and returned tool/sensor/acceptance feedback; shell/file/web tool grants are caller-specified.
- Decision owner: Model-backed agent in first-party packaged `AgentLoop::run` and tool registry wiring; not a test MockModel, hook veto or external business operator.
- Supporting / enforcement mechanisms: Guides, typed Tool schemas, Model adapters, PreToolUse/PostToolUse hooks, sensors, Acceptance checks, Policy and budget guards, context compaction and response receipts.
- Closure path: User task → context + guides + tool schemas → model completion/stream → chosen authorized tool executes → tool result/sensor observation/acceptance result → next model decision or terminal outcome.
- Boundary reachability: `AgentLoop::new(model)` and public `run` call `run_built_context` → `run_in_span` with concrete model calls and typed tool dispatch, instrumented feedback after execution and return to the same loop; README demonstrates this actual supported Rust runtime rather than an adjacent benchmark runner.
- Why this is / is not agent-owned: Without the model, policy/hook infrastructure still checks and records work but cannot select a context-dependent tool/answer based on observed results. The model holds the material operational discretion.
- Evidence: [README.md#L35](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/README.md#L35), [crates/harness-loop/src/lib.rs#L647](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L647), [crates/harness-loop/src/lib.rs#L1008](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1008), [crates/harness-loop/src/lib.rs#L1561](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1561), [crates/harness-loop/src/lib.rs#L1793](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1793), [crates/harness-loop/src/lib.rs#L2215](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L2215).
- Basis: Explicit first-party model/tool composition and feedback, without live remote model benchmark evidence.
- Confidence: High for structural support.
- Caveats: Runtime execution and hosted model response were not verified in the available Linux environment.

## S2 — Coordination

- State: —
- Function: No separate first-party regulator of actual interference between independently viable S1 divisions, returning changed commitments/operations to the conflicting units, is proven at this assessed operating-cell boundary.
- Disturbance / variety regulated: Child task dependencies, concurrent tool calls, scheduling and potential workspace contention are plausible but generic task dispatch and orchestration do not establish a concrete inter-S1 conflict/oscillation relation.
- Decisive decision or feedback right: The user/developer configures DAG job dependencies, task routing or registered tools; runtime enforces a chosen execution plan. There is no evidenced agent-owned S2 interference adjudication across autonomous sibling S1 operational domains.
- Decision owner: Application constructor, current task model or deterministic orchestration scheduler, not a distinct S2 function.
- Supporting / enforcement mechanisms: Subagent API, `Orchestrator`, scheduler jobs, HookBus, tool concurrency and task result handling.
- Closure path: Parent/current task delegates → child executes → returned result or error → parent continues; there is no concrete S1 conflict sensed → S2 decides dampening → revised independent S1 behavior relationship.
- Why this is / is not agent-owned: A task dispatcher executes choices at the S1/task layer and can synchronize tools, but neither scheduling nor shared transport supplies an evidenced viable-operating-division coordination right.
- Evidence: [crates/harness-loop/src/subagent.rs#L92](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/subagent.rs#L92), [crates/harness-loop/src/orchestrator/orchestrator.rs#L101](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/orchestrator/orchestrator.rs#L101), [crates/harness-loop/src/scheduler/scheduler.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/scheduler/scheduler.rs#L1).
- Basis: Bounded negative for the shipped single-agent plus optional subagent operating modes.
- Confidence: Medium-high.
- Caveats: A downstream application could compose independent agents and provide S2, but its inter-S1 governance is outside the packaged boundary.

### Absence scope

- Surfaces inspected: Subagent invocation, Orchestrator run jobs, scheduler/channel and tool parallelism, HookBus.
- Plausible first-party paths checked: Multiple child operations, shared tools, job ordering and possible resource collision.
- Why no material first-party path remains: No concrete source-backed inter-S1 interference regulator at the reviewed operating recursion changes subsequent commitments of two separately viable S1 units; mechanisms are routing/locking/task completion, not distinct organizational S2.



## S3 — Inside-and-now control

- State: —
- Function: No discretionary first-party whole-current portfolio manager owns negotiated priority, resource or obligation adjustments across independently viable S1 divisions.
- Disturbance / variety regulated: Token budgets, stuck tool loops, commands, approval levels and resource exhaustion can threaten local execution, but they are run-level constraints and immediate controls.
- Decisive decision or feedback right: Developer/host chooses `Policy` (L1/L2/L3 operating constraints), Hooks, budgets and acceptance criteria; the AgentLoop applies deterministic bounds and model acts within them.
- Decision owner: User/application for resource/policy configuration; deterministic runtime enforces per-run limits; model acts in S1.
- Supporting / enforcement mechanisms: Runtime policy, bounds and loop engine, acceptance checks, human gate hooks, cancellation, stuck/monotony detectors, recorder/telemetry.
- Closure path: Tool call or budget event → configured guard denies/corrects/halts one task → same operating loop continues/stops. No portfolio managerial decision/return across autonomous S1 organizations.
- Why this is / is not agent-owned: Earned L1/L2/L3 approval is a harness security/autonomy deployment setting, **not** VSM S3 by numeric name or an evidence of autonomous enterprise-manager authority.
- Evidence: [README.md#L15](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/README.md#L15), [crates/harness-loop/src/lib.rs#L698](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L698), [crates/harness-loop/src/lib.rs#L1446](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1446), [crates/harness-loop/src/acceptance.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/acceptance.rs#L1), [crates/harness-loop/src/loop_engine/mod.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/loop_engine/mod.rs#L1).
- Basis: Bounded source-negative in packaged configuration and operational management paths.
- Confidence: Medium-high.
- Caveats: Human/application may provide actual S3 outside this assessed first-party recursion.

### Absence scope

- Surfaces inspected: Policy/autonomy level, budgets, resource/timeout guards, approval hooks, acceptance, scheduler and server session API.
- Plausible first-party paths checked: Allocation across agent sessions, L1–L3 promotion, runtime resource accounting, job priority and failure handling.
- Why no material first-party path remains: Every path shown is an application-configured execution rule or per-task/model control; no packaged discretionary current-organization manager with S1 portfolio obligation/priority feedback is identified.



## S3* — Complementary audit

- State: —
- Function: No operational independent complementary reality-inspection path with a mandate to correct a separate S3 managerial picture and cause subsequent present-regulation adjustments is shown.
- Disturbance / variety regulated: Incorrect outputs, failed tools and unaudited actions are observable; sensors, acceptance and AuditHook can test/log single-run events but do not establish independent audit correction of a first-party S3.
- Decisive decision or feedback right: Registered sensors/acceptance criteria and configured AuditHook record or locally veto actions; no audit officer/agent with independent organizational S3* corrective mandate.
- Decision owner: Task-time validators/host-defined hooks, not a separate complementary audit function.
- Supporting / enforcement mechanisms: `AuditHook`, tracing/telemetry, `Acceptance`, `Sensor`, run receipts and replay recorder.
- Closure path: Action → hook or local validation → same task accepts/retries/logs; no alternative independent operational inspection → S3 misinformation corrected → S3 changes current organizational management.
- Why this is / is not agent-owned: Telemetry and validators may provide evidence useful to an auditor, but are not themselves separate audit rights that can change present S3 decisions.
- Evidence: [README.md#L90](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/README.md#L90), [crates/harness-loop/src/lib.rs#L1634](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1634), [crates/harness-loop/src/lib.rs#L1894](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1894), [crates/harness-loop/src/hooks/mod.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/hooks/mod.rs#L1).
- Basis: Bounded negative after examining audit, sensors and external review.
- Confidence: Medium-high.
- Caveats: Independent human audit could be layered by a downstream host.

### Absence scope

- Surfaces inspected: AuditHook/HookBus, telemetry, acceptance/sensor feedback, goal receipts and server logs.
- Plausible first-party paths checked: Independent sampling of operational reality, challenge of model reports, findings returned to present S3 executive.
- Why no material first-party path remains: These mechanisms support current-task correctness and observability, but no first-party independent complementary audit with a correction/return path to an established S3 managerial owner is evidenced.



## S4 — Outside-and-then intelligence

- State: A
- Disturbance / variety regulated: Future task diversity, recurrence of complex procedures, changing tool affordances and the need to preserve a generalized successful multi-step approach for later agent tasks.
- Function: Form a generalized **future operating skill** from successful past complex tasks and make it persistently available for later task capabilities in an explicitly selected supported operating mode.
- External distinction: `ExperienceRecorder`/episode tool traces expose actual task context, tools used and outcome; `SkillDistiller::gate` checks success, diverse tools, situation length and duplicate-skill similarity against existing loaded skills.
- Future / prospective distinction: The model-backed distillation prompt directs the model to generalize the successful episode into an agentskills.io-compatible procedure for a future **class** of tasks, not to solve the same current task again.
- Adaptation option generated: A model produces a named reusable `SkillDraft` with instructions; the first-party validator checks schema/lint/duplicate safety.
- Path back into current capability / S3: In explicitly documented, first-party **opt-in** `distill_and_write(ep, skills_root)` mode, the accepted draft is written under `<skills_root>/<name>/SKILL.md` using the same first-party `harness-context` skills-root format. Subsequent operating sessions explicitly configured to scan/use that skills root can make the new procedure available to model task solving. Return is to future S1 capability, not a claimed separate S3 executive; no default automatic invocation.
- Decisive decision or feedback right: The model selects prospective generalized procedural content; the selected `DistillPolicy` is deterministic, and the host selects the invocation and whether to enable automatic writing versus requiring review. The source-backed autonomous portion is the **model's future procedural option**, integrated into a documented auto-write first-party mode.
- Decision owner: Configured model through shipped `SkillDistiller` after opt-in; application owner chooses when to call and provides skills directory. Draft-only default multi-tenant branch remains parent/host-reviewed and does **not** create autonomous admission.
- Supporting / enforcement mechanisms: Episode recorder/guide, policy gate, skill validation, duplicate scan, `SkillDraft::write_to`, `harness-context` skills-root scanner, optional `skill_manage` tool and skill loader.
- Closure path: Successful multi-step environmental episode → model generalizes prospective skill → safety and duplicate checks → opt-in write to canonical skill path → skills root available to configured later AgentLoop use → new goal encounters improved procedure.
- Boundary reachability: `SkillDistiller::new(model)`, public `distill_and_write` and first-party `SkillDraft::write_to` are exported, tested and documented for a host that opts out of approval; the docs explicitly distinguish review-only `distill()` and packaged automatic persistence. `harness-context::skills`/harness-tools implement scan/management of the persisted SKILL.md format. This is not an external user custom tool invented for the assessment.
- Why this is / is not agent-owned: Remove the model and the first-party policy/recorders retain successful episodes but cannot propose the generalized future procedure. Optional host invocation does not mean automatic background strategic intelligence is present.
- Evidence: [crates/harness-loop/src/experience/mod.rs#L20](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L20), [crates/harness-loop/src/experience/mod.rs#L54](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L54), [crates/harness-loop/src/experience/distill.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L1), [crates/harness-loop/src/experience/distill.rs#L259](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L259), [crates/harness-loop/src/experience/distill.rs#L367](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L367), [crates/harness-loop/src/experience/distill.rs#L416](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L416), [crates/harness-loop/src/experience/distill.rs#L873](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/distill.rs#L873), [crates/harness-tools/src/skills.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-tools/src/skills.rs#L1).
- Basis: Source-connected opt-in first-party autonomous future skill synthesis with persistent output, **not** claim of default auto-learning or measured improvement.
- Confidence: Medium for supported optional mode; no provider live task run was independently executed.
- Caveats: The host must initiate distillation and configure later skill loading; the commonly recommended multi-tenant mode holds the draft for parent/human review. No autonomous reconfiguration of Policy, S5 or all future services is claimed.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate-identity authority adjudicates conflicting organizational purposes with binding long-term returned policy for this single-agent organization.
- Disturbance / variety regulated: Risks from untrusted shell/tools, filesystem scope and skill modifications motivate guardrails and human approvals; no organizational identity conflict decision protocol is shipped.
- Decisive decision or feedback right: Application/user configures model policy, allowlists, sandbox and human approvals; runtime enforces selected bounds but does not decide ultimate organization mission.
- Decision owner: External user/application owner and deterministic policy guard; not a model-based constitutional authority.
- Supporting / enforcement mechanisms: Hooks, approval gates, sandbox, Policy levels, skill lint/validation, audit logs.
- Closure path: Configured action → allow/deny/approval enforcement → current task proceeds/halts; no ultimate-purpose issue reaches legitimate S5 and returns a durable constitutional decision.
- Why this is / is not agent-owned: Security and operator consent mechanisms are not organizational policy ownership simply because labelled `Policy`, `Audit` or L1–L3.
- Evidence: [README.md#L25](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/README.md#L25), [crates/harness-loop/src/lib.rs#L1793](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/lib.rs#L1793), [crates/harness-loop/src/experience/mod.rs#L54](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/experience/mod.rs#L54), [crates/harness-loop/src/loop_engine/mod.rs#L1](https://github.com/liliang-cn/harness-rs/blob/eb26e73fa4ca3e581e8e61be7a6c9bb91bd5f329/crates/harness-loop/src/loop_engine/mod.rs#L1).
- Basis: Bounded negative for standard distribution and opt-in skill-learning mode.
- Confidence: Medium-high.
- Caveats: Actual human governance and higher-recursion organization are external and should be assessed separately.

### Absence scope

- Surfaces inspected: Runtime permission hooks, human gates, policy/autonomy tiers, sandbox and skill review API.
- Plausible first-party paths checked: Potential task/policy conflicts, permanent skill governance, ultimate purpose changes and operator approvals.
- Why no material first-party path remains: No packaged authority decides an organizational identity question and returns binding ultimate-purpose policies to future operations; all surfaced rules are supplied by a downstream owner.



## Recursion

One model/tool operating cell supplies S1; in a separately configured post-run mode its model synthesizes a prospective reusable skill for future tasks, supplying bounded S4. Standalone task-subagents, a finite DAG orchestrator and multi-session service API do not automatically create viable sibling S1 departments with distinct VSM metasystem authority.

## Variety and escalation

Model choice/tool feedback and immediate accept/deny sensors handle task variety; a configured skill distiller can introduce longer-term reusable procedural learning. Runtime status, exceptions, approval prompts, logs and audit events are not automatically algedonic signals to a legitimate S3/S4/S5 owner.

## Evidence gaps

- The review is of the frozen Rust source; the supplied Linux VM did not expose a working `cargo` executable, so no Rust `cargo test` or live provider model run was independently completed here. Do not treat absent local Rust environment as proof of upstream defects.
- Skills-root scan/writing and model-based `SkillDistiller` are shipped and documented, but do **not** fire automatically from every `AgentLoop::run`. The credited S4=A is strictly the opt-in, packaged automatic persistence mode; multi-tenant draft review remains host/parent controlled.
- No cross-session organizational conflict regulator, whole-current managerial executive, independent S3* corrective audit or S5 legitimate constitutional return is established from generic APIs, labels, test code or docs alone.
- This is `proposed`; no catalog position, signature or cohort views are canonical until separate CI-backed admission.
