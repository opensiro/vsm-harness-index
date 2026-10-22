---
harness_id: vtcode
project_name: VTCode
repository: https://github.com/vinhnx/VTCode
review_ref: dc32271158bec3c37b81ad7bf57157a801307517
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# VTCode

## Review boundary

- System in focus: first-party VTCode Rust coding-agent distribution, including the installed interactive TUI, headless `vtcode exec` and ACP-backed agent runtime, bundled subagent delegation, opt-in worktree/loop-engine and opt-in plan/build/evaluate orchestration.
- Purpose and identity: take a user's development request, inspect a repository, choose coding/terminal actions, verify changes, optionally divide bounded subtasks among model-driven agents, and report/continue work.
- Relevant environment: project repository/worktrees, terminal and tool observations, developer/user instructions, model provider, permissions and approvals, git state, dynamic task tracker, session archives, background subagents and externally installed MCP/skills.
- Standard-distribution boundary: shipped `src` CLI routes and first-party `crates/codegen/vtcode-core`, `vtcode-config`, `vtcode-safety` and tool packages at the frozen commit; opt-in first-party built-in features credited only to the extent their active wiring and closure are evidenced.
- Credited operating / distribution surfaces: model-guided `AgentRunner`, tool registry and sandbox policy, native primary `build/auto/plan` roles, built-in `default/explorer/worker` subagents, controller lifecycle, optional child worktrees, heuristic reconciliation, task-local evaluator/replanner and durable session state.
- Adjacent first-party surfaces excluded from ownership: code-host CI, repository maintainers, benchmarks/test fixtures, future features described in roadmap, downstream connected tools/models, user's custom agent definitions or worktree configuration beyond the shipped defaults, and external schedulers as a separate organization.
- Operating modes considered: interactive TUI, headless task/full-auto, ACP interface, read-only plan/approved build handoff, foreground/background and nested subagent tasks, optional `isolation=worktree`, and `plan_build_evaluate` harness setting.
- Recursion level: one VTCode session/task operating organization that can delegate bounded independent child work; not the VTCode development company or a hypothetical enterprise portfolio.
- Reviewed revision: [`dc32271158bec3c37b81ad7bf57157a801307517`](https://github.com/vinhnx/VTCode/tree/dc32271158bec3c37b81ad7bf57157a801307517) from immutable intake #200.
- Observation date: 2026-10-22, first-party pinned-source inspection; no provider-backed task execution or parallel-worktree runtime reproduction.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The terminal, headless and ACP interfaces share the model-driven Rust agent runtime: a provider response proposes tool calls, VTCode routes them through a typed tool registry, execution policy and sandbox, returns observations, and continues or stops based on task and verification state. Built-in `build`, `auto`, and `plan` modes vary tool permissions and whether planning must await a user-approved handoff. Session archives, compacted state, trackers and human policy sustain operation but do not themselves constitute a higher VSM layer.

The first-party `SubagentController` can spawn read-only explorer and write-capable worker model-driven children with their own message context, runtime configuration, tools, status and lifecycle. It can run several active children, wait/cancel/close them, and return task results to the parent. Both built-in `explorer` and `worker` specs have `isolation: None` by default. A separately configured worktree-isolated child can use a generated git branch under `.vtcode/worktrees/`, and a completion hook tries `diff → heuristic verification → git merge`. Critically the worktree is created as `<spec-name>-<timestamp>` while the completion hook passes only the **spec name** as the worktree name into the reconciler; moreover reconciliation follows the child's terminal status notification and exposes outcomes only in traces. Thus the available source cannot establish successful conflict-aware coordination and returned inter-S1 adjustment in this route. The separate model-backed `verify_proposed_change()` is a callable code QA path, while worktree reconciliation itself uses `HeuristicDiffVerifier`, not that reviewer.

For opt-in `plan_build_evaluate`, a model planner writes task-local spec/contract/tracker, the main generator implements the same user's task, and a skeptical evaluator may request bounded revisions/replanning. This is a substantial local quality-control loop, but the architecture expressly calls it single-threaded and does not show independent whole-current resource authority. Generalization notes are explicitly task scoped, not published as global future-environment policy.

Primary anchors: [architecture and agent-scope declaration](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/ARCHITECTURE.md), [core model run](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/execute.rs#L507-L550), [subagent startup and isolation](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_spawn_run.rs#L926-L1059), [child worktree completion](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_child_loop.rs#L40-L85), [reconciliation implementation](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_verify.rs#L156-L216).

## Operational model

VTCode's operative discretion is model-based coding action selection. Child agents own bounded delegated task execution and may work independently; the parent can spawn, wait and use their task reports. Runtime caps, approval rules, planning gates, fixed worktree separation and verifier checks are important supporting mechanisms. To credit S2/S3/S3*/S4/S5, however, a separate qualifying disturbance, decisive decision and return path is required rather than a role name, task decomposition, source roadmap or policy setting.

## S1

- State: A
- Function: Carry out user-scoped coding tasks through model-selected terminal/file/patch/search tools and iterative observation; optionally carry out bounded delegated subtasks.
- Disturbance / variety regulated: Varying user requirements and source structures, build/test failures, provider responses, filesystem and terminal output, and findings during code changes.
- Decisive decision or feedback right: The active model chooses task-specific tools/actions and subsequent continuation from returned tool outputs. First-party child agents have their own model-guided runner and tools within configured permissions.
- Decision owner: VTCode `AgentRunner` model response and active child model sessions; typed tool registry executes selected actions under platform/user restrictions.
- Supporting / enforcement mechanisms: Model/provider adapter, tool dispatcher, sandbox and command policy, task tracker, session memory, auto-compaction, verification/continuation controls, child lifecycle statuses and bounded budgets.
- Closure path: User task or delegated prompt → provider tool decision → executable tool action → result in session context → next model choice or completion/verification; child findings may return to parent.
- Why this is / is not agent-owned: Reasoning over current source/output and choosing concrete actions is task-owned autonomy, even though permission policy, operator plan approval and provider contracts remain external constraints.
- Boundary reachability: `vtcode` interactive and `vtcode exec` load this agent/tool runtime, and the registered subagent facade can construct first-party child `AgentRunner` sessions with effective workspace and permissions.
- Evidence: [CLI/agent flow](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/README.md#L125-L170), [main task model/tool feedback loop](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/execute.rs#L780-L1060), [batched tool dispatch](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/execute.rs#L1300-L1365), [child model-runner configuration](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_child_loop.rs#L205-L275).
- Basis: structural.
- Confidence: high for first-party operational wiring; no empirical model-backed successful coding task is claimed.
- Caveats: Child capabilities vary by spec, model and tool policies; the default explorer is intentionally read-only.

## S2

- State: —
- Function: Detect and attenuate real interference between independent S1 coding cells, then return a compensating coordination decision into ongoing units.
- Disturbance / variety regulated: Potential concurrent child edits to the same project files, competing branch changes, conflicting integration results and resource collisions.
- Decisive decision or feedback right: The controller spawns/waits and may create optional isolated worktrees. The completion hook's heuristic diff/merge is not a demonstrated returned inter-S1 adjustment: built-in child specs default to no worktree, the branch/worktree name handed to reconciliation differs from creation, and outcomes are logged rather than propagated as child/parent coordination decisions.
- Decision owner: Fixed `SubagentController` lifecycle/worktree utilities and parent task delegator; no source-backed separate owner closing actual cross-S1 conflict detection/attenuation/return.
- Supporting / enforcement mechanisms: Child concurrency/depth caps, optional `WorktreeManager`, git worktree locks, read-only explorer permission, status/wait/close, heuristic unsafe-added-line check and git merge failure handling.
- Closure path: Parent delegate → children perform bounded tasks → statuses/results returned; optional child worktree → completion reconciliation attempt. A conflict-aware correction received by independently operating affected children is not evidenced.
- Why this is / is not agent-owned: Parallel worktrees can prevent direct write collisions and git may reject merges, but source does not show a working regulated inter-unit feedback relationship rather than isolation, delegation and a post-hoc integration attempt.
- Evidence: [built-in worker/explorer isolation none](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-config/src/subagents.rs#L539-L600), [generated worktree name on spawn](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_spawn_run.rs#L945-L972), [after-child reconciliation with spec.name](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_child_loop.rs#L56-L79), [reconciler hard-codes main branch and logs result](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_verify.rs#L156-L215), [git verify and merge](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/git/reconciler.rs#L201-L278).
- Basis: structural.
- Confidence: medium; concurrency/worktree mechanisms are real but integration effectiveness is untested and a naming mismatch is visible in source.
- Caveats: A repaired or externally coordinated worktree installation could produce new evidence for S2. This is not an assertion of any reproduced runtime merge failure.

### Absence scope

- Surfaces inspected: `SubagentController` spawn/status/wait, built-in child specs and tools, git worktree creation/lock, heuristic verifier, reconciliation call/merge errors and parent result flow.
- Plausible first-party paths checked: read/write child agents, foreground/background concurrency, optional worktree branches, direct peer conflict avoidance, child/parent return, worktree merge/reject and review-model approval.
- Why no material first-party path remains: Default concurrent workers can share state without first-party conflict attenuation, while opt-in isolation/reconciliation lacks a demonstrated correct identifier and coordination result return into affected S1s; neither path evidences the required S2 loop.

## S3

- State: —
- Function: Make binding current whole-system resource, priority and commitment decisions over distinct viable S1 units.
- Disturbance / variety regulated: Multiple subagent requests, shared task progress, accumulated spend/time, incomplete subtasks and accepted/rejected local work.
- Decisive decision or feedback right: The parent can delegate, wait, cancel and integrate findings, while plan/build/evaluate controls one current task. No distinct whole-current portfolio tradeoff owner reassigns resources/commitments across operating cells on their shared current state.
- Decision owner: Parent task agent for delegation and fixed controller for caps; no additional evidenced S3-specific manager.
- Supporting / enforcement mechanisms: Subagent status/notifications, max depth and concurrency, task tracker, runtime budget, session handoff and single-threaded spec/contract/evaluator revisions.
- Closure path: Subtask prompt → child status/report → parent coding turn; plan spec → generator → task evaluator → possible retry. This is work delivery/QA inside S1, not governance of all current interdependent operations.
- Why this is / is not agent-owned: Parent retains local task control, but performing decomposition does not prove whole-current current-control authority with accountable cross-unit commitments.
- Evidence: [subagent queue and concurrency](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_spawn_run.rs#L974-L1058), [wait/result flow](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_spawn_run.rs#L360-L433), [single-threaded PBE boundary](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/ARCHITECTURE.md), [task-local planner](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/orchestration.rs#L45-L132).
- Basis: structural.
- Confidence: medium-high for bounded assessment.
- Caveats: Enterprise scheduling external to one session is a different recursion, not silently included here.

### Absence scope

- Surfaces inspected: parent and child lifecycles, progress/loop ledgers, task tracker, budgets, plan mode, evaluator and workspace/tool policies.
- Plausible first-party paths checked: child task assignment and cancellation, current statuses, concurrency quotas, plan/build/evaluate phases, background task scheduling and tool budget/cost signals.
- Why no material first-party path remains: The packaged controls select individual work or bound resource consumption, without a separate whole-current intervention into shared S1 commitments and subsequent accountable return.

## S3*

- State: —
- Function: Complement current management claims with sufficiently independent operational evidence and return actionable correction to S3.
- Disturbance / variety regulated: Incorrect patches, false task completion, missed acceptance criteria, unsafe diffs and overconfident agent output.
- Decisive decision or feedback right: `verify_proposed_change` can spawn a read-only verifier, and opt-in PBE uses a skeptical evaluator or a multi-model skeptic panel; they judge the local change/spec/verification, not the whole-current S3 operational account. Worktree reconciliation instead calls a deterministic line heuristic.
- Decision owner: Task-level reviewer model/evaluator and heuristic diff gate; no S3* management-audit owner.
- Supporting / enforcement mechanisms: Read-only explorer/verifier, explicit PASS/REJECT parsing, evaluator scorecard and high-severity findings, task tracker contracts, model skeptic panel, git changed-file summaries.
- Closure path: Code changes and task spec → reviewer/evaluator findings → local S1 revision or user report. This is artifact/task QA; an S3 state or claim is not independently observed and corrected.
- Why this is / is not agent-owned: Separate models may challenge local work genuinely, but independence of a task reviewer is not the independence/authority of a complementary managerial audit channel.
- Evidence: [verifier agent and fail-closed verdict](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_verify.rs#L40-L153), [worktree heuristic instead of model reviewer](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/subagents/controller_verify.rs#L156-L175), [evaluator and skeptic option](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/orchestration.rs#L140-L215), [PBE single-threaded architecture](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A QA tool can materially improve reliability without crossing the VSM S3* boundary.

### Absence scope

- Surfaces inspected: reviewer/explorer subagents, separate verification call, multi-model skeptic/evaluator, PBE feedback, diff heuristic, runtime traces and task tracker.
- Plausible first-party paths checked: independent read-only code verifier, conflicting reviewer models, external current-state evidence, different model routes and rejection-revision loops.
- Why no material first-party path remains: These paths validate tasks or changed files and cannot challenge a distinct whole-current S3's accounting and feed a corrective managerial decision.

## S4

- State: —
- Function: Model external future changes/opportunities and choose organizational capability adaptations with return to current management.
- Disturbance / variety regulated: Changing developer needs, model/tool ecosystem, future projects and software/repository practices.
- Decisive decision or feedback right: Plan/build/evaluate can ask a model to replan the **current** rejected implementation and record bounded, task-scoped generalization notes. Skills, context and scheduling may alter tasks, but no installed separate prospective environmental intelligence and S3-mediated capability choice is evidenced.
- Decision owner: Local task planner/replanner or human config/skill author; no demonstrated S4 strategist.
- Supporting / enforcement mechanisms: Task spec/contract, acceptance criteria, scorecard, task generalization notes with falsifiers, local session memory, external MCP/skills and opt-in durable `vtcode schedule` invocations.
- Closure path: Current implementation → skeptical evaluation → revised task plan → continued main execution; no future external environment → alternative capability strategy → S3 handoff and adoption closure.
- Why this is / is not agent-owned: Genuine model re-planning is confined to present-task correctness; available external tools and task-triggered schedules do not prove autonomous anticipation or organizational adaptation.
- Evidence: [task-local reevaluation and replan](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/orchestration.rs#L140-L295), [evidence-bounded generalization and evaluator prompt](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/crates/codegen/vtcode-core/src/core/agent/runner/orchestration.rs#L18-L42), [runtime architecture and scheduling](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/ARCHITECTURE.md), [loop engineering workflow scope](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/loop-engineering.md).
- Basis: structural.
- Confidence: medium-high within shipping first-party paths.
- Caveats: Users may explicitly ask VTCode to research or implement future tooling; the general S1 capability to accept such prompts is not an autonomous first-party S4 mechanism.

### Absence scope

- Surfaces inspected: task replanner/evaluator, generalization-note scope, continuation/failure handling, session memory and skills, durable local schedule and optional external provider/tool access.
- Plausible first-party paths checked: model-driven revising of failed plans, scoring options, recurrent automation, longer-run loop memory, external information tool use and self-modifying coding ability.
- Why no material first-party path remains: Inputs and decisions optimize current/local task execution; no evidence of prospective external distinctions, organizational option selection, and return through current-control decision authority.

## S5

- State: —
- Function: Legitimately settle ultimate organizational purpose, identity and governing values, including tensions between current operation and proposed future strategy.
- Disturbance / variety regulated: Untrusted workspace instructions, malicious commands, protected files, conflicting tool privileges and unsafe/unapproved implementation.
- Decisive decision or feedback right: Operator/user decides task and approves plans/workspaces; fixed tool policy and sandbox control allowable actions. The runtime has no legitimate ultimate identity/policy decision right beyond applying these choices.
- Decision owner: User and application-defined command/workspace safety gates; not a first-party autonomous S5 holder.
- Supporting / enforcement mechanisms: Planning review gate, workspace trust, ToolPolicyGateway, command policy, sandbox, `AGENTS.md` context, permission profiles, tool denial paths and human consent.
- Closure path: User task/policy → tool catalog and dispatch approval → accepted/denied S1 action; plan finalization explicitly awaits user approval before build. No new binding agent-level ultimate policy is decided and returned to an S3/S4 balance.
- Why this is / is not agent-owned: Enforcing preconfigured policy and producing a proposed plan is operational accountability, not legitimate authority to define VTCode's ultimate purpose or override the user.
- Evidence: [planning human handoff and read-only enforcement](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/guides/planning-workflow.md), [security/model and command policy](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/README.md#L90-L110), [configurable approval/sandbox components](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/development/CGP_ARCHITECTURE.md#L150-L195), [project instructions as non-security context](https://github.com/vinhnx/VTCode/blob/dc32271158bec3c37b81ad7bf57157a801307517/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: high on human and fixed-rule gate boundary; medium-high on absent S5.
- Caveats: Code safety, review and honest handoffs are useful but not proof of S5 self-governance.

### Absence scope

- Surfaces inspected: planning flow, project/user instructions, runtime guidance, workspace trust, command safety, tool approval, subagent permissions and model override handling.
- Plausible first-party paths checked: plan approval, tool risk review, automated full-auto execution, user trust grants, delegate policy constraints and task-level replanning.
- Why no material first-party path remains: The user/provider/developer defines constraints and authority. The installed model/runtime has no legitimate final-policy adjudication or binding S3–S4 governance return.

## Distributed OSS parent arrangement

The repository's developers maintain Rust crates, release channels, tests and documentation. These are external to one VTCode operating session. Connected provider APIs, MCP servers or custom agent manifests are environmental services/extensions and are not assigned independent governance rights just for being in the repository.

## Self-hosted and non-human modes

Headless `vtcode exec`, ACP support, background child tasks and opt-in full-auto loops can run with fewer manual prompts under chosen policy, while plan handoff and workspace/tool permissions remain conditional. Worktree isolation and reconciliation are opt-in feature surfaces, not proven production conflict resolution without a live run and correct identity/return chain.

## Recursion

The main task model and eligible delegated child agents are bounded S1 work cells. Task-local planning/evaluation, subagent result accumulation, status and budgets support those cells without demonstrating independent S2–S5 closures. Evaluating a fleet of VTCode sessions under an external organization would require a different system-in-focus.

## Variety and escalation

Tool errors, blocked calls, task failures and verification findings are fed into the main model or resumable checkpoint. Subagent statuses, timeouts and results can return through `wait`; worktree merge/reject attempts log their outcomes. Worktree namespace isolation and fixed concurrency caps reduce some varieties without a source-proven returned inter-S1 conflict adjustment. An external human approval remains decisive for restricted actions.

## Evidence gaps

- Source inspection only; no provider credentials or end-to-end VTCode run used, and no multi-child write/merge conflict reproduction claimed.
- Specific worktree-completion code appears to pass `record.spec.name` instead of generated `<spec>-<timestamp>` name; this is a source-level wiring discrepancy requiring runtime confirmation, not independently proven exploit or failure.
- Worktree reconciliation uses `HeuristicDiffVerifier` (added-line dangerous-command detection), not the separately available LLM verifier. Its completion event and log results do not prove successful mutual-adjustment feedback.
- Runtime completion accuracy, evaluator reliability and future capability improvements were not experimentally measured.
