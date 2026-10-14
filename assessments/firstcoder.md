---
harness_id: firstcoder
project_name: FirstCoder
repository: https://github.com/KomorGiaoGiao/FirstCoder
review_ref: 3856a10203bc21b8f78a7060be3a99bc44f2e0ac
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# FirstCoder

## Review boundary

- System in focus: the first-party installable Python FirstCoder coding-agent CLI/TUI at pinned source `3856a10203bc21b8f78a7060be3a99bc44f2e0ac`, including model/tool operation, first-party role subagents, background jobs, task plan, worktree isolation, prewrite review, verification feedback and local policy/session machinery.
- Purpose and identity: complete operator-requested software tasks through model-directed tool use, optionally delegate independent research/review/test/coding outcomes, and coordinate current background work without quietly modifying the user's main working tree.
- Relevant environment: mutable source repository, git worktrees and competing changes, tool output, compilation/test errors, child review findings, provider output, asynchronous tasks, pending human authorization and configurable capabilities.
- Standard-distribution boundary: shipping `firstcoder` Python package and its assembled session/agent/tool/permission/background/subagent modes. External model APIs, task repository, benchmark/Harbor studies, upstream maintainer CI, hand-authored extensions, and external autonomous agents are dependencies rather than credited organizational function owners.
- Credited operating / distribution surfaces: `firstcoder/agent/loop.py`, `firstcoder/agent/subagent.py`, `firstcoder/agent/background.py`, `firstcoder/agent/tool_execution.py`, `firstcoder/agent/worktree.py`, `firstcoder/agent/session.py`, `firstcoder/tools/delegate.py`, `firstcoder/tools/background.py`, first-party task plan, session/context, permission and review paths.
- Adjacent first-party surfaces excluded from ownership: `benchmark/` task runners and observations, archived async-subagent DAG design, development plans/tests/CI and docs illustrative examples, any third-party skill/MCP runtime not composed into the shipped first-party distribution.
- First-party operating / deployment modes considered: synchronous local model/tool coding loop; fresh reader/reviewer/tester/coder child agent via `delegate`; asynchronous read-only/investigation workers and mutation-capable background coder *required* to use an isolated worktree; background status/cancel and revisioned task plan; interactive approval/prewrite diff; resumed session and one-shot/headless CLI.
- Recursion level: one coding project/session with a main first-party model-run S1 and optional child model-run S1s whose current operation is supervised by the main agent. A fresh child AgentLoop is not by itself a whole nested viable system.
- Reviewed revision: `3856a10203bc21b8f78a7060be3a99bc44f2e0ac` (frozen #898 intake; no upstream repin).
- Observation date: 2026-10-15.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The released CLI/TUI uses a common `SessionBootstrap`/app factory path to construct `AgentSession`, a provider and an `AgentLoop` with tool schemas, permission enforcement, tool-result feedback and durable JSONL facts. The main model chooses tool invocations through the actual provider completion/stream loop; `ToolExecutor` dispatches to first-party tools after authorization and returns the results as model-visible observations.

The `AgentLoop._ensure_delegate_tool` method installs the real first-party `delegate` tool. `SubagentRunner` creates a separate `AgentLoop` in a fresh child session with a role profile and specific tools. `researcher` reads sources, `reviewer` is read-only and instructed to examine diffs/call-sites/risks, `tester` can investigate verification, and `coder` can edit. Role-specific budgets apply; recursion is disabled in child runners. The first-party reviewer's response is returned as a normal parent-visible `delegate` tool result that can influence subsequent model code changes. This is separate from the deterministic `prewrite_review` human confirmation, which inspects the proposed diff before one tool writes.

The shipped `run_in_background` control schedules approved long-running `delegate` or tool operations under a `BackgroundManager` and immediately returns a placeholder result; completed jobs later deliver a `task_notification` to the model. The main loop exposes `background_status` and `background_cancel`; background tasks can be associated with revisioned task-plan IDs and update completion after the work finishes. A background mutation-capable `coder` is required to use `WorktreeManager` to create a separate git checkout and worktree-rooted permissions. The child does not mutate the parent's working tree; on completion a branch/path/diff report is returned for parent review, explicitly without automatic merge. Therefore safe separation of concurrent writers is real, but whether this bundle supplies a *closed* specific inter-S1 S2 coordination relation at the target project boundary remains unresolved, not credited from isolation alone.

The task plan/goal, session snapshots, token/context compaction, skill/MCP loading, scope permissions and provider retries are real supporting mechanisms. The historical `docs/ASYNC_SUBAGENTS_DAG_DESIGN.md` explicitly labels itself archived; this assessment credits only the current unified TaskPlan and executable sources, not historical design intentions.

Evidence: [`README.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/README.md); [`docs/ARCHITECTURE.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/ARCHITECTURE.md); [`docs/ASYNC_SUBAGENTS_DAG_DESIGN.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/ASYNC_SUBAGENTS_DAG_DESIGN.md); [`firstcoder/agent/loop.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/loop.py); [`firstcoder/agent/subagent.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/subagent.py); [`firstcoder/agent/background.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/background.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/agent/worktree.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/worktree.py); [`firstcoder/tools/delegate.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/delegate.py); [`firstcoder/agent/execution_evidence.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/execution_evidence.py).

## Operational model

The main model and its separately instantiated role workers own bounded S1 action discretion; first-party tool and permission paths constrain it. The main model sees whole-current plan and active background work and owns discretionary coordination of current commitments. A dedicated fresh reviewer S1 can independently inspect code and report findings to its parent in an in-boundary review mode. Worktree isolation and deferred parent merge prevent unapproved crossover but do not, absent further evidence, prove a completed S2 regulation/return over conflicts between already operating writers. None of these local operating permissions or task plans is automatically future-oriented S4 or ultimate-policy S5.

## S1 — Operations

- State: A
- Function: carry out open-ended software engineering and verification tasks by model-directed workspace exploration, edits, commands and tool-observation feedback.
- Disturbance / variety regulated: unknown code, broken builds, test regressions, varying tool/provider output and incomplete implementation requirements.
- Decisive decision or feedback right: choose/revise model tool actions and optional child work after interpreting actual results.
- Decision owner: first-party main FirstCoder `AgentLoop` model actor and bounded separately model-running child coding/research sessions, not the deterministic executor.
- Supporting / enforcement mechanisms: provider adapter, `ToolExecutor`, tool registry, permissions, context compaction, JSONL session, tool limits and cancellation.
- Closure path: operator task → model-selected tool/child request → first-party permission/execution → captured tool result or child report → next model action or response.
- Boundary reachability: standard package assembly constructs its own `AgentLoop` with registered local tools; `delegate` builds child FirstCoder `AgentLoop` rather than spawning a foreign coding CLI.
- Why this is / is not agent-owned: with the model's tool decisions removed, permission/registry/session machinery cannot independently select context-specific software changes.
- Evidence: [`firstcoder/agent/loop.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/loop.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/agent/subagent.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/subagent.py); [`firstcoder/tools/delegate.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/delegate.py); [`docs/ARCHITECTURE.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/ARCHITECTURE.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: this maps organizational ownership, not empirical correctness, benchmark success or safety certification.

## S2 — Coordination

- State: ?
- Function: possible attenuation of interference between parallel first-party coding S1s through separate mutable workspaces and parent-held integration, but a complete inter-S1 corrective feedback path remains unresolved.
- Disturbance / variety regulated: background workers could modify the same code paths while a parent/other worker is coding, potentially generating incompatible changes or accidental overwrite.
- Decisive decision or feedback right: first-party worktree constructor forbids direct writes to parent checkout and retains isolated child changes for later parent review. The separately required merge/conflict reconciliation decision is not shown as a first-party active S2-specific outcome loop.
- Decision owner: deterministic `WorktreeManager` for per-writer isolation and parent model/human for possible future integration; final S2-specific owner cannot be assigned on this evidence.
- Supporting / enforcement mechanisms: per-child git worktree/branch, worktree-rooted sandbox, permission manager, diff summary, asynchronous task notifications and parent review.
- Closure path: child is isolated before mutation → child produces changed-files/diff and a separate branch → parent sees report; missing witness is concrete opposing S1 change/conflict → function-specific arbitration/repair → revised interacting S1 operation. No automatic merge is shipped.
- Why this is / is not agent-owned: isolation is a real preventive mechanism; generic per-worker sandboxing and task result handoff are insufficient to assert S2=A or C without the function-specific inter-worker corrective closure.
- Evidence: [`firstcoder/agent/worktree.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/worktree.py); [`firstcoder/agent/subagent.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/subagent.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/agent/background.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/background.py); [`docs/ARCHITECTURE.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/ARCHITECTURE.md).
- Basis: structural + unresolved
- Confidence: medium
- Caveats: a standard parent may explicitly inspect/merge child's worktree via git, but the review did not establish a shipped conflict-sensitive first-party return relation; neither a positive state nor a bounded no-path `—` is defensible while this concrete integration boundary remains unexamined.

## S3 — Inside-and-now control

- State: A
- Function: direct current tasks, dependencies, backgrounds and specialized worker assignments for the active coding project, rather than only executing a single tool.
- Disturbance / variety regulated: several concurrent independent work commitments, delayed background jobs, unfinished plan tasks, verification blockers and child roles with different capacity/tool boundaries.
- Decisive decision or feedback right: model-led parent creates/delegates current research/review/test/coding tasks, chooses synchronous or background execution, inspects status, cancels unneeded work, decides subsequent project actions and reconciles task completion against task plan.
- Decision owner: first-party model-backed main FirstCoder agent for discretionary whole-current task and worker decisions. `BackgroundManager`, task-plan IDs and permission gates implement/status-limit those decisions.
- Supporting / enforcement mechanisms: `delegate` tool and role profiles, background status/cancel/notification, revisioned TaskPlan with completion checks, per-session project status, model-visible outcomes and hard limits.
- Closure path: current task plan + child/background state → main model decides a role/priority/assignment/cancellation → first-party task/job dispatcher changes current work → asynchronous notification or delegated result returns into next main model turn and plan reconciliation.
- Boundary reachability: `AgentLoop` installs `delegate` and background status/cancel tools, `ToolExecutor` invokes first-party job scheduler and first-party child loops, and notifications reenter the live provider context; shipped supported modes expose the whole session's current work surface.
- Why this is / is not agent-owned: hard task-plan consistency, child caps and notifications do not select current task priorities or remediation; these are chosen by the main model from the wider task/worker view.
- Whole-system current view: the session's task plan, queued/running/completed background jobs, delegated role outcomes and present coding/verification commitments.
- Current-control decision scope: select worker roles and tool budgets, assign task/plan IDs, suspend/wait or cancel current work, rework dependent tasks and decide what to integrate into the main workspace.
- Evidence: [`firstcoder/agent/loop.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/loop.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/agent/background.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/background.py); [`firstcoder/tools/background.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/background.py); [`firstcoder/tools/delegate.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/delegate.py); [`firstcoder/agent/task_plan_policy.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/task_plan_policy.py).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: S3 claim is bound to enabled first-party multi-work/background mode and parent model discretion, not to a full organization, external CI, or automatic global resource optimisation; no `(P)` inferred.

## S3* — Complementary audit

- State: A
- Function: challenge produced coding changes using a distinct role-bound source-reading model actor and return actionable critique to current coding control.
- Disturbance / variety regulated: code regressions, defective diffs, missed call sites and risks that the authoring actor's summary/tests may omit.
- Claim being audited: correctness/quality of implementation and changed-code risks in the main/child coding task.
- Ordinary reporting path: coding model and tool results returned through `AgentLoop`, including the worker's own declared completion.
- Complementary access path: separately created `reviewer` role child `AgentLoop` with read-only `REVIEWER_TOOL_NAMES`, fresh session/context and instructions to inspect diffs, call sites and risks.
- Independence boundary: `reviewer` has separate role-scoped model run and direct source inspection, not merely a replay of the original coder's prose. This is a supported optional model-invoked review mode; no claim that every task is automatically audited.
- Who acts on findings: the main parent model receives `delegate(role=reviewer)`'s text and evidence as an ordinary first-party tool result and may revise code or seek further tests. Human prewrite-diff approval is not itself the independent actor credited here.
- Decisive decision or feedback right: reviewer model selects critique and source-backed defects; parent model has subsequent corrective task discretion when the result enters its next turn.
- Decision owner: first-party separate reviewer model for complementary evidence judgment; parent for corrective operation, with read-only enforcement separate.
- Supporting / enforcement mechanisms: `SUBAGENT_PROFILES['reviewer']`, child context, restricted tools, `SubagentRunner.run`, return `make_text_result('delegate',...)`, parent tool observation loop.
- Closure path: coding artifact/diff → independent reviewer read-only file/diff investigation → reviewer findings in returned delegate result → main model chooses corrective action, revision, or further verification using normal coding tools.
- Boundary reachability: `AgentLoop._ensure_delegate_tool` installs `delegate`, role `reviewer` is enumerated in the shipped tool schema, and `SubagentRunner._run_inline` actually builds a child AgentLoop in a new session and passes its result back to the parent.
- Why this is / is not agent-owned: the reviewer exercises model judgment based on its own read-only source observations; removing this actor leaves only the authoring model/self-checks and human prewrite gates, not equivalent complementary assessment.
- Evidence: [`firstcoder/agent/subagent.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/subagent.py); [`firstcoder/tools/delegate.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/delegate.py); [`firstcoder/agent/loop.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/loop.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/tools/review.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/review.py).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: optional review is not independently accredited, mandatory before publish, or empirically verified here. Parent may disregard findings; positive state rests on a real in-boundary independent review-result/next-action channel, not a guaranteed repair.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party organizational future intelligence/adaptation decision tied back into revised ongoing capabilities.
- Disturbance / variety regulated: evolving external tools, provider interfaces and future project needs are potential concerns, but the inspected product tracks the current coding task.
- Decisive decision or feedback right: main model can research current implementation; user configures skills/models; automatic compaction and provider retries maintain task continuity, not prospective system-level adoption.
- Decision owner: task-level model/current operator and deterministic context/adapter recovery; no distinct future-option owner established.
- Supporting / enforcement mechanisms: context compaction L1-L4, skills discovery and on-demand loading, task-boundary classification, provider retry, sessions, and external benchmark/roadmap material outside the runtime boundary.
- Closure path: task observations/memory alter current prompt/tools; no future environmental distinction → alternative capability design → adoption into the first-party working organization returns.
- Why this is / is not agent-owned: model investigations and skill loading inside a present task are part of S1, not a future-oriented capability management loop.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/ARCHITECTURE.md); [`firstcoder/agent/loop.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/loop.py); [`firstcoder/agent/task_boundary_classifier.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/task_boundary_classifier.py); [`firstcoder/agent/provider_retry.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/provider_retry.py); [`firstcoder/agent/session.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/session.py); [`README.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: user extension of the Python repo itself is adjacent development and does not donate current S4 autonomy.

### Absence scope

- Surfaces inspected: model/tool loop, task classifier and plan, context compaction, skills, provider retry, subagent investigations, session continuity and benchmarks/roadmap boundaries.
- Plausible first-party paths checked: continuous external sensing beyond a present goal, autonomous future option-development, selection among prospective capabilities, durable organizational update subsequently returned into S3/current operations.
- Why no material first-party path remains: the supported mechanisms work on current tasks, current context or user-invoked config; no in-boundary prospective capability adaptation circuit is wired.

## S5 — Policy and identity

- State: —
- Function: no first-party legitimate ultimate mission/identity-policy decision with returned governance path is established.
- Disturbance / variety regulated: risky commands, sensitive file edits, user approval and security/resource constraints are important but local action policy concerns.
- Decisive decision or feedback right: operator chooses permissions/project requirements, runtime enforces prewrite approvals and isolated worker boundaries; no model or legitimate institutional parent settles an identity-level constitutional question.
- Decision owner: user/permission configuration for tool rights; deterministic guard for enforcement. No first-party S5 ultimate-policy owner.
- Supporting / enforcement mechanisms: permission manager and grants, prewrite diff review, tool confirmation, child worktree sandbox, AGENTS.md project instructions.
- Closure path: allow/deny confirmation changes one tool's execution. No identity dispute reaches a legitimate governing parent and returns a durable ultimate-policy decision governing later organizational behavior.
- Why this is / is not agent-owned: even agent-authored plans and permission-approved writes do not create legitimate authority to redefine the coding organization's ultimate purpose.
- Evidence: [`firstcoder/agent/session.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/session.py); [`firstcoder/agent/tool_execution.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/tool_execution.py); [`firstcoder/agent/worktree.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/agent/worktree.py); [`firstcoder/tools/review.py`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/firstcoder/tools/review.py); [`docs/PERMISSIONS_DESIGN.md`](https://github.com/KomorGiaoGiao/FirstCoder/blob/3856a10203bc21b8f78a7060be3a99bc44f2e0ac/docs/PERMISSIONS_DESIGN.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: human consent is real and respected, but ordinary tool-level review should not be encoded as `S5=P`.

### Absence scope

- Surfaces inspected: per-tool approval, user prewrite review, project permissions/grants and child sandbox, session and local AGENTS.md context.
- Plausible first-party paths checked: authoritative purpose/identity dispute adjudication, institutional parent returning revised ultimate-policy rules, S3–S4 constitutional settlement.
- Why no material first-party path remains: these mechanisms enforce or expose local code/action permissions and task instructions only, not a closed identity-level issue→legitimate authority→returned policy cycle.

## Distributed OSS parent arrangement

The FirstCoder upstream project and its maintainers/release CI are outside the installed local coding-agent operating boundary. They cannot be imported as a first-party current-governance or S5 authority for arbitrary user instances.

## Self-hosted and non-human modes

Local CLI and TUI can use configured providers and noninteractive messages. Background jobs and isolated coder worktrees make unattended S1 operations possible, with explicit permission and parent review constraints. These do not assert parent-controlled S3/S4/S5 `(P)` ownership or guaranteed child review enforcement.

## Recursion

The primary model can instantiate a secondary FirstCoder AgentLoop with its own tools/context/role. This is a real nested operational cell, not a separately established fully viable S1–S5 recursive unit: child delegation is disabled and there is no evidenced child metasystem for whole nested organization.

## Variety and escalation

Model-led tools and role specialization absorb coding variety; task plans, permission gates, background limits and isolated worktrees attenuate resource/write uncertainty. A separate reviewer can return source-based challenges; human prewrite consent is a tool authorization check rather than an algedonic function or ultimate policy.

## Evidence gaps

- S2: resolve whether a supported first-party parent worktree-admission/reconciliation mode actually detects and regulates conflicting outputs from two independent S1s and returns corrective feedback. Isolation plus unmerged diff reporting alone is not promoted to a positive S2; bounded absence is also premature while that in-boundary integration possibility remains.
- S3*: model-backed read-only review mode is wired, but no task benchmark or compulsory automatic review gate was executed; separate decision-role and parent return are evidence of organizational structure, not a guarantee the reviewer is right.
- Source-first static review of frozen code only; no live agent/provider execution or full regression suite was run.