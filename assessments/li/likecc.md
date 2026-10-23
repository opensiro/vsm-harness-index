---
harness_id: likecc
project_name: LikeCC
repository: https://github.com/KNIGHT15235/likecc
review_ref: 4a9b77d281646385bf48fd85b8a03c4d28bbee23
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# LikeCC

## Review boundary

- System in focus: shipped Python LikeCC local coding-agent runtime and its model-backed first-party child/team modes, frozen at `KNIGHT15235/likecc@4a9b77d281646385bf48fd85b8a03c4d28bbee23`.
- Purpose and identity: inspect, edit, test and coordinate software-engineering work in a user-selected repository, optionally distributing work to independent coding agents.
- Relevant environment: local Git worktree, source/tests and shell, configured LLM, model/tool return values, permission decisions, child-team message traffic, current task and worker state.
- Standard-distribution boundary: installed `likecc` Python CLI/TUI, model/tool loop, shipped subagent definitions, first-party Agent Team/worktree tools, optional coordinator and explicitly enabled Verification role.
- Credited operating / distribution surfaces: `likecc/agent.py`, `likecc/__main__.py`, `likecc/app.py`, `likecc/tools/agent_tool.py`, `likecc/tools/team_create.py`, `likecc/teams/`, `likecc/agents/`, `likecc/worktree/`, `likecc/prompts.py` and first-party bundled role definitions.
- Adjacent first-party surfaces excluded from ownership: repo maintainers' issue/release governance, benchmark reports, development tests, fake-model fixtures, documentation statements with no runtime wiring and externally installed MCP or custom agent definitions.
- First-party operating / deployment modes considered: ordinary interactive and headless model/tool execution; foreground/background subagents; in-process and terminal team workers in separate Git worktrees; two-flag coordinator mode; optional built-in `Verification` worker when separately enabled.
- Recursion level: one local coding session and its independently model-driven subagents or team workers, not an external OSS maintainers' organization.
- Reviewed revision: `4a9b77d281646385bf48fd85b8a03c4d28bbee23` (batch #996 frozen row 7).
- License screen: root `LICENSE` contains MIT; `pyproject.toml` declares MIT and frozen repository metadata reports `MIT`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The local agent delegates tool selection and subsequent remediation to a configured model, executes chosen file/shell tools under first-party permission checks, and returns their observations to the next model turn. `AgentTool` starts independent model-backed workers, while `TeamCreateTool` installs a named local team. Each teammate receives an actual Git worktree created by `WorktreeManager`, an independent conversation/tool registry, bounded permissions and persisted team membership. `SharedTaskStore` maintains assigned, blocked and completed tasks; teammates receive `TaskCreate`, `TaskList`, `TaskUpdate` and `SendMessage` tools; completion and mailbox observations reach the team lead. These mechanisms support coordination but cannot by themselves establish an interference-specific S2 correction cycle.

An explicitly optional coordinator mode requires **both** `enable_coordinator_mode: true` and `LIKECC_COORDINATOR_MODE=1`. Creating a team activates a dedicated first-party team-lead prompt and restricts the lead to coordinator tools. That prompt assigns the model whole-team planning, work assignment, worker reports, correction and mandatory independent Verification. However, the actual lead tool registration in `app.py` and `__main__.py` includes `Agent`, `TeamCreate` and `TeamDelete`, **not** `SendMessage` or `TaskStop`; `apply_coordinator_filter` cannot retain missing tools. The lead also lacks an actual `TaskList`/member-status tool. Hence its claimed continuing intervention into current team work is an incomplete function-specific constructor, not a closed S3=A path.

A distinct built-in `Verification` definition is shipped but excluded by default. When `enable_verification_agent: true` is set, the loader makes this role available to `AgentTool`, with separate fresh model context, narrowed read-only named tools, explicit artifact/build/test inspection and a `VERDICT` response. In supported opt-in coordinator operation, the lead is instructed to delegate implementation and then start a **fresh** verifier, consume the resulting notification and issue correction through a further agent assignment. This supports bounded independent artifact audit rather than equating worker self-report or ordinary tests with S3*. It is a model-directed path, **not** a runtime-mandated blocking merge gate; neither actual execution nor quality was measured with a live LLM.

Frozen primary sources: [`agent.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agent.py), [`agent_tool.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/agent_tool.py), [`team_create.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/team_create.py), [`team manager`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/manager.py), [`coordinator.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/coordinator.py), [`tool_filter.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agents/tool_filter.py), [`verification.md`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agents/builtins/verification.md), [`app.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/app.py), [`__main__.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/__main__.py).

## Operational model

One model-driven coding agent autonomously selects changes and responds to tool results (S1=A). Distinct teammates and per-worker worktrees exist, yet isolation, task metadata and mailbox messages do not establish the specific inter-worker conflict judgment and corrective feedback required for S2 (S2=—). Optional coordinator mode expresses a purpose-built whole-current control role, but main-lead follow-up and termination tools advertised in its prompt are not actually registered; its complete autonomous current-control cycle must still be composed/fixed (S3=C). Separately enabled first-party Verification supplies a fresh, role-restricted independent artifact-checking worker, whose verdict can redirect new implementation work (S3*=A within the supported dual-opt-in model-directed path). There is no evidenced future-environment-driven capability adaptation or ultimate policy-identity control (S4/S5=—).

## S1 — Operations

- State: A
- Function: autonomously implement and verify user-requested local coding tasks, including independently model-deciding child workers.
- Disturbance / variety regulated: changing code state, build/test failures, shell output, incomplete task requirements, permission denial and results of delegated coding.
- Decisive decision or feedback right: model chooses file/shell operations and child task instructions, then selects subsequent actions on observed results.
- Decision owner: LikeCC primary model and separately instantiated child/teammate model agents within their work scopes.
- Supporting / enforcement mechanisms: provider, conversation loop, tool registry, permission checker, `AgentTool`, `TaskManager`, team/worktree setup and notifications.
- Closure path: request → model tool/agent decision → checked native execution → result, error or child completion fed into a later model turn → revised action or final answer.
- Boundary reachability: interactive `app.py` and headless `__main__.py` both instantiate the runtime plus the first-party `AgentTool` and Team system; separately enabled workers run through real model loops.
- Why this is / is not agent-owned: deterministic code executes and restricts commands, but the substantive task choice and response to tool evidence are model decisions.
- Evidence: [`agent.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agent.py), [`agent_tool.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/agent_tool.py), [`__main__.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/__main__.py).
- Basis: pinned first-party source and native script/unit tests; no provider-connected runs.
- Confidence: high for installation and control wiring.
- Caveats: passing deterministic tests does not establish LLM coding efficacy or quality of model decisions.

## S2 — Coordination

- State: —
- Function: no complete first-party disturbance-specific inter-S1 coordination and correction circuit is established at the team recursion.
- Disturbance / variety regulated: distinct coding teammates may propose incompatible edits, overlap shared task dependencies or require conflict resolution at integration.
- Decisive decision or feedback right: no modeled, observable agent-owned assessment of an actual incompatible peer change followed by a conflict-resolving inter-S1 direction is established.
- Decision owner: each worker selects its own coding tasks; team worktree construction is automatic and current lead dispatch is task routing rather than proved interference-specific arbitration.
- Supporting / enforcement mechanisms: mandatory teammate-specific Git worktrees, shared task blocking fields, team mailbox and explicit coordinator prompt advice to serialize file-overlapping work.
- Closure path: isolated teammate work and returned status exist, but there is no evidenced peer conflict/incompatibility detection → model-selected attenuation or integration decision → changed S1 execution based on that assessment.
- Why this is / is not agent-owned: per-worker isolation and generic assignments prevent some direct overwrites; their creation is predetermined machinery rather than an agent deciding how to resolve detected inter-worker interference and closing that decision.
- Evidence: [`agent_tool.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/agent_tool.py), [`shared_task.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/shared_task.py), [`coordinator.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/coordinator.py).
- Basis: pinned source-level evaluation against five-witness S2 calibration.
- Confidence: medium-high; conservative classification.
- Caveats: a supported custom workflow could request a conflict review, but not enough is installed as S2-specific standard ownership here.

### Absence scope

- Surfaces inspected: per-teammate worktree constructor, worktree lifecycle, coordinator prompt, shared task dependencies, mailboxes, task status tools, integration and notification handling.
- Plausible first-party paths checked: separate Git worktrees as attenuation, file-set serial scheduling advice, `blocked_by` fields as conflict resolution, message traffic as negotiated assignment, task persistence as active coordination.
- Why no material first-party path remains: each is isolation, planned delegation or shared state without an evidenced concrete inter-S1 interference witness, agent-owned resolution and returned behavioral correction.

## S3 — Inside-and-now control

- State: C
- Function: a dedicated first-party coordinator-mode constructor targets present whole-team work and priorities, but the full autonomous intervention loop is not wired.
- Disturbance / variety regulated: simultaneously executing workers, changed readiness, task failures, unknown current worker progress and conflicting commitments within one local coding team.
- Decisive decision or feedback right: coordinator model can synthesize results, issue initial/nested `Agent` assignments and choose next work from returned task notifications; the advertised follow-up/stop and whole-task inspection tools are missing from its live registry.
- Decision owner: configured team-lead model selects initial and follow-on work, but the decisive whole-current feedback/reassignment right is only partially constructed.
- Supporting / enforcement mechanisms: two-flag coordinator opt-in, first-party role prompt, `TeamCreateTool`, `AgentTool`, filtered lead registry, persisted `TeamManager` and child completion notifications.
- Closure path: enabled lead → `TeamCreate` switches role → model delegates workers → runtime delivers completion or mailbox notifications → model may create new work; **missing** `SendMessage`/`TaskStop` registration and lead-side `TaskList` prevent the claimed direct current-worker correction/readback path.
- Boundary reachability: optional configuration and environment opt-in activate the installed role when a team is created in the interactive runtime; headless likewise constructs `TeamCreateTool`, while all missing-tool limitations persist.
- Why this is / is not agent-owned: coordinator-specific model discretion and role are purpose-built and first-party (hence `C` rather than generic delegation), but role text naming a tool cannot establish that tool's actual decision/feedback authority.
- Whole-system current view: model sees its delegated task history and returned notifications but no registered live team-wide `TaskList`/member-status query; this incompleteness limits whole-current control.
- Current-control decision scope: initial decomposition, dispatch and future new worker instructions are reachable; targeted follow-up, stop or reassignment of an active teammate is not fully available to the coordinator lead.
- Evidence: [`coordinator.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/coordinator.py), [`tool_filter.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agents/tool_filter.py), [`team_create.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/team_create.py), [`app.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/app.py), [`__main__.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/__main__.py).
- Basis: positive function-specific optional constructor, with missing registration verified through both entry points and default registry.
- Confidence: medium-high for constructor and negative actual-tool wiring conclusion.
- Caveats: `C` does not credit closed autonomous current control. A future code change registering functional lead-side status/message/stop tools would require new pinned evidence and reassessment.

## S3* — Complementary audit

- State: A
- Function: in explicitly configured first-party Verification mode, independently challenge another worker's implementation/verification claim by inspecting actual project artifacts and test commands.
- Disturbance / variety regulated: premature completion claims, self-serving implementation reports, missed regressions, unexecuted builds/tests and bugs hidden by producer assumptions.
- Decisive decision or feedback right: a fresh specialized Verification model independently selects evidence checks and issues `VERDICT: PASS / FAIL / PARTIAL`; configured lead may use failed evidence to assign a new correcting worker.
- Decision owner: different worker model with a new conversation and verification-specific instructions, not the implementation worker's own summary or test string.
- Supporting / enforcement mechanisms: bundled `verification.md`, opt-in `AgentLoader`, per-agent filtered tool registry denying named file-edit tools, `AgentTool` background completion, first-party coordinator's fresh-verifier and error-follow-up policy.
- Closure path: producing worker performs changes and claims completion → coordinator spawns separate freshly instructed `Verification` worker with access to actual project artifacts → verifier runs build/test/lint, independently challenges claim and returns explicit verdict via task notification → coordinator can assign correction or withhold verified completion.
- Boundary reachability: set `enable_verification_agent: true` so standard loader exposes the shipped named role; enable coordinator with config plus environment and create a team to install the mandate. For same-root ordinary subagents, the verifier can inspect the edited workspace; worktree-isolated teammates require explicit artifact/branch access or integration before the audit can see their edits.
- Why this is / is not agent-owned: the verifier, not a fixed CI assertion, makes a claim-relative judgment after independent artifact access; correction selection remains with the coordinating model. It is **not** an automatic runtime-enforced pass/fail gate.
- Claim being audited: the implementation worker's assertion that the requested code change is complete, builds correctly and introduces no unreported regression.
- Ordinary reporting path: implementer's own completion text, tool output and `task-notification` to the lead.
- Complementary access path: fresh verifier reads implementation/configuration from disk and runs independent build, tests, type/lint and regression checks using its own tool calls, then reports actual commands/output and verdict.
- Independence boundary: distinct fresh worker context and artifact access, restricted named edit tools; shared parent provider, potential shell side effects and absence of a runtime mandatory audit gate limit procedural independence.
- Who acts on findings: lead model may launch a correcting worker or report incomplete verification; no downstream merge veto is mechanically guaranteed.
- Evidence: [`verification.md`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agents/builtins/verification.md), [`loader.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agents/loader.py), [`agent_tool.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/tools/agent_tool.py), [`coordinator.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/teams/coordinator.py).
- Basis: first-party shipped opt-in operating path, built-in specialist definition, native role/configuration and coordinator tests; no live verifier was run.
- Confidence: medium; supported role/return path confirmed, actual quality and model compliance unknown.
- Caveats: default setup leaves Verification disabled, the model must obey its prompt, and the independent worker must reach the **actual modified artifact** rather than an untouched sibling worktree. This is supported option capability, not proof that every LikeCC task was independently audited.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed outside/future environmental sensing and selected, retained organizational capability change is established.
- Disturbance / variety regulated: changing requirements and historical context affect coding sessions, but no future-oriented capability mismatch/adaptation loop is installed.
- Decisive decision or feedback right: model can plan immediate tasks and user can configure roles/providers; no S4 owner decides durable capability redesign using an external future horizon.
- Decision owner: absent for S4; task execution and plugin configuration belong to other recursions/functions.
- Supporting / enforcement mechanisms: project instructions, memory/session compaction, configurable prompts, user-defined agents, model configuration and Git history.
- Closure path: retrieved context can alter current coding instructions, not a horizon scan → prospective option → adopted reusable capability → returned current-system support.
- Why this is / is not agent-owned: implementing software for a user's present task is not necessarily strategic adaptation of the harness's own capabilities.
- Evidence: [`prompts.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/prompts.py), [`config.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/config.py), [`agent.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/agent.py).
- Basis: local first-party source and runtime modes.
- Confidence: medium-high.
- Caveats: downstream agent-authored plugins could be developed, but generic ability to write code does not itself establish the organizational S4 circuit.

### Absence scope

- Surfaces inspected: core prompt/context, session persistence/compaction, agent definitions and loader, config, worktree and team lifecycle.
- Plausible first-party paths checked: persistent memory as future scanning, user-added specialists as adaptation, coordinator's planning as S4 and writing code that expands harness capacity.
- Why no material first-party path remains: inspected paths support present request handling or manually configured features; none owns a returned prospective system-capability decision.

## S5 — Policy and identity

- State: —
- Function: no identity-defining legitimate policy arbitrator mediating present vs future organizational choices is installed.
- Disturbance / variety regulated: dangerous tool effects and user permission boundaries are immediate operational constraints, not ultimate identity/purpose disputes.
- Decisive decision or feedback right: operator/config sets policy and runtime enforces per-tool constraints; no S5 organization-wide ultimate-policy decision actor is specified.
- Decision owner: no first-party S5 actor identified in the declared run-time recursion.
- Supporting / enforcement mechanisms: `PermissionChecker`, sandbox rules, bounded child permission inheritance, team role scope and configuration.
- Closure path: immediate permission allow/deny returns to tool execution; no identity-level dispute → legitimate authority choice → durable organization-wide governing return.
- Why this is / is not agent-owned: an operator's execution consent or static rule does not by itself constitute organizational purpose/identity governance.
- Evidence: [`permissions/checker.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/permissions/checker.py), [`__main__.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/__main__.py), [`config.py`](https://github.com/KNIGHT15235/likecc/blob/4a9b77d281646385bf48fd85b8a03c4d28bbee23/likecc/config.py).
- Basis: core permissions/configuration and local-vs-OSS boundary.
- Confidence: medium-high.
- Caveats: legitimate human ownership of a real OSS organization is outside the analyzed local harness runtime.

### Absence scope

- Surfaces inspected: shell/file permission checks, child permission inheritance, coordinator and Verification opt-ins, first-party startup/config and maintainer docs.
- Plausible first-party paths checked: local permission approval as parent S5, maintainer policies as harness S5 and coordinator's task priorities as identity governance.
- Why no material first-party path remains: all regulate per-request operations, local configuration or external OSS maintenance, not a returned identity-level decision of this agent organization.

## Distributed OSS parent arrangement

LikeCC is an MIT-licensed code repository whose contributors govern their OSS project. That maintenance group is not an agent-visible first-party S5 or S3 parent in the local deployed coding-agent/team operating boundary; maintainer CI and repository review are evidence sources, not credited S3* runtime auditors.

## Self-hosted and non-human modes

The application may use configured provider endpoints in TUI or headless mode; both install `AgentTool`, team manager and worktrees. Coordinator requires a configuration flag plus environment variable and a team creation transition. Verification independently requires its own opt-in flag. These first-party modes do not require a human to choose individual model tool calls, but tooling permissions remain operator-configured. Neither optional feature is presumed enabled by default.

## Recursion

At the declared recursion, separately executing team workers are the subordinate S1 units and the installed coordinator is an incomplete S3-specific higher-control constructor; the independent verifier examines actual artifacts on a distinct evidentiary path when configured and provided access to the changed work. Separate physical worktrees do not establish independent viable corporations, nor does a maintained GitHub repository become this runtime's policy-bearing S5.

## Variety and escalation

Tool results, task notifications, team mailbox messages and isolated branches propagate current operational information. The coordinator can choose later worker tasks based on reports; it cannot invoke the advertised direct message/stop controls because those tools are absent from its registry. Failed verification may motivate a new worker, but neither notifications nor a failed test automatically evidence algedonic escalation to higher policy/strategic intelligence.

## Evidence gaps

- Frozen deterministic verification: `uv run --locked python tests/verify_subagent.py` passed **90/90**; targeted `uv run --locked pytest -q tests/test_teams.py tests/test_subagent.py tests/test_permissions.py` passed **184/184**. Broader `pytest -q` started but was stopped after extended runtime without completion; do **not** report full-suite success. No real provider/LLM task execution was performed.
- Code-level gap: coordinator prompt refers to `SendMessage` and `TaskStop` and dynamic current-team tools; the main interactive/headless tool registration does not install `SendMessageTool` or a `TaskStopTool`, and coordinator filtering also excludes `TaskList`. `S3=C` reflects the function-specific, incomplete constructor, not successful direct follow-up.
- Independent Verification is role-restricted and can review actual files/tests when enabled, but an untouched new teammate worktree alone cannot reveal another isolated teammate's unmerged edits. S3* is bounded to a supported same-root or explicitly exposed changed-artifact path and is not a mandatory acceptance veto.
- The test assets use deterministic fake model behavior and source constructor assertions; there is no claim of empirical multi-agent effectiveness or reviewer accuracy.
