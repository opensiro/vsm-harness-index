---
harness_id: suisuicode
project_name: SuisuiCode
repository: https://github.com/Yangtianspike/suisui-code
review_ref: c9017b0613b22151325a5904a521aefe4c62abbc
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SuisuiCode

## Review boundary

- System in focus: SuisuiCode's first-party Python terminal coding-agent runtime at frozen revision `c9017b0613b22151325a5904a521aefe4c62abbc`, including the primary model/tool loop, built-in coding tools, permissions, sessions/context, background/fork subagents, Team/Coordinator machinery, shared team task state, mailbox/message transport and per-teammate worktree lifecycle.
- Purpose and identity: perform software-engineering work in a project and, in supported Team/Coordinator modes, decompose current work across multiple first-party coding agents while keeping their mutable work isolated and their current commitments visible to a Lead actor.
- Relevant environment: user objectives, repository/worktree state, provider responses, filesystem/shell evidence, team task-board state, teammate lifecycle/status, team messages, project instructions, skills/hooks/MCP tools and operator permission decisions.
- Standard-distribution boundary: SuisuiCode's own Agent runtime, built-in tools, permission/session/context state, Team manager/backends/tools, Coordinator mode and worktree manager are inside. External model providers and MCP servers are dependencies. User-authored skills/hooks/instructions configure the runtime but do not donate unshipped organizational functions.
- Credited operating / distribution surfaces: `README.md`; `src/suisuicode/agent/agent.py`; `src/suisuicode/agent/agent_tool.py`; `src/suisuicode/agent/team_hook.py`; `src/suisuicode/team/spawn.py`; `src/suisuicode/team/manager.py`; `src/suisuicode/team/tasks/__init__.py`; team tools; `src/suisuicode/coordinator/__init__.py`; `src/suisuicode/permission/engine.py`; `src/suisuicode/cli.py`; worktree machinery.
- Adjacent first-party surfaces excluded from ownership: tests as authority by themselves, contributor/release activity, external provider/MCP behavior, user-supplied skills and application-authored hooks. Documentation or prompts are credited only where the frozen implementation exposes the corresponding runtime path.
- First-party operating / deployment modes considered: ordinary terminal coding sessions; foreground/background/fork Agent calls; Team teammates on supported backends; Coordinator mode; permission modes including default interactive approval and `BYPASS`/YOLO; worktree-isolated teammate execution.
- Recursion level: the assessed organization is one primary/Lead SuisuiCode session plus first-party teammate Agent runtimes that it can create and govern through Team state. Each teammate is a complete model/tool coding loop and therefore a distinct subordinate S1 at this recursion.
- Reviewed revision: `c9017b0613b22151325a5904a521aefe4c62abbc`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The primary `Agent` owns the repository-facing model/tool feedback loop. Model-selected tool calls run through SuisuiCode's first-party registry and permission engine; results return into the same conversation so subsequent model action can change from observed evidence. Sessions, context compaction/recovery, hooks, skills and MCP extend this operational loop without replacing its decision owner.

`AgentTool` can construct additional full `Agent` runtimes with narrowed tools and independent runtime/conversation state. Team spawning is stronger than ordinary awaited delegation: when `team_name` is supplied, the call enters `TeamHook`/Team manager machinery and launches a teammate that is persisted as a team member. The supported tmux backend starts a separate teammate process in an automatically created dedicated Git worktree. Thus multiple teammates can be simultaneously active while remaining separate S1 units.

The Team subsystem persists a shared task board with task status, assignee and dependency relationships under file locks. Model-facing Team tools let a Lead create/list/get/update those commitments and send directed or broadcast messages. Coordinator Mode is a shipped opt-in first-party mode, enabled by a feature flag plus environment switch, that narrows the Lead's tools and explicitly instructs it to research, synthesize a work allocation, create tasks, spawn teammates, wait for reports, verify results and merge teammate worktree branches.

Every Team teammate receives a dedicated worktree as part of the spawn path. This mechanically separates mutable repository state between concurrent S1s. The isolation decision itself is fixed first-party runtime policy rather than a task-specific model judgment, so the coordination function is classified `C`, not `A`.

Mutating Team/Agent actions pass through the ordinary permission engine. In `BYPASS`, the runtime automatically permits them, so the Coordinator model can autonomously create/update current commitments and spawn teammates. In default interactive modes the same mutating organization-level actions can require operator approval, yielding a parent-governed S3 path.

Teammate completion is persisted into Team communication state, but no standard Lead-side consumer of `Manager.poll_lead_mailboxes()` was found in the reviewed TUI integration. The S3 claim therefore does not rely on an automatic Lead wake-up. It relies on the explicit Team task-board view and model-facing current-control tools available during Lead turns.

Primary evidence:

- [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md)
- [`src/suisuicode/agent/agent.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py)
- [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py)
- [`src/suisuicode/agent/team_hook.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/team_hook.py)
- [`src/suisuicode/team/spawn.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/spawn.py)
- [`src/suisuicode/team/manager.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/manager.py)
- [`src/suisuicode/team/tasks/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/tasks/__init__.py)
- [`src/suisuicode/coordinator/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/coordinator/__init__.py)
- [`src/suisuicode/permission/engine.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/permission/engine.py)
- [`src/suisuicode/cli.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py)

## Operational model

An ordinary SuisuiCode actor can perform repository work itself or create subordinate Agents. In Team mode, the Lead creates a persistent team/task structure and can spawn multiple teammates. Every teammate obtains an isolated worktree and runs its own coding loop. The Lead can inspect the team's current task board, create new commitments, change assignments/status/dependencies, message teammates, and in Coordinator mode converge the work by inspecting and merging teammate branches.

This separates the relevant functions. S1 is each model/tool coding loop. S2 is the deterministic worktree-isolation policy that attenuates concurrent repository-mutation interference. S3 is the Lead's current organizational control over which tasks and teammate commitments exist now and how they are assigned/updated. Coordinator verification/merge is part of that production-control path rather than an independent S3* audit role.

## S1 — Operations

- State: A
- Function: perform environment-facing coding work by interpreting an objective, selecting permitted repository/tool actions, executing them and revising later actions from returned evidence.
- Disturbance / variety regulated: source/worktree state, implementation alternatives, provider uncertainty, file/shell results, tool failures, context pressure and changing task evidence.
- Decisive decision or feedback right: choose the next task-specific coding/tool action and revise it after observing the result.
- Decision owner: the model-backed SuisuiCode Agent in the primary session or each teammate/subagent runtime.
- Supporting / enforcement mechanisms: first-party tool registry; permission engine; provider adapters; sessions/context compaction; hooks; skills; MCP; runtime turn bounds and tool filtering.
- Closure path: task/current context → model decision → first-party tool execution → tool result appended to conversation → same model actor chooses another action or final response.
- Boundary reachability: the shipped CLI directly instantiates the primary Agent and Team/subagent paths instantiate the same first-party Agent class or supported teammate process.
- Why this is / is not agent-owned: removing the model actor leaves tools, permissions and state machinery but removes the open-ended task-specific choice of which repository action to take next.
- Evidence: [`src/suisuicode/agent/agent.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py); [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py); [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: mutating actions can be human-gated depending on permission mode; `BYPASS` is a first-party supported autonomous operating mode.

## S2 — Coordination

- State: C
- Function: attenuate a concrete interference class among concurrently active teammate S1s by separating their mutable repository state into dedicated Git worktrees and serializing shared Team metadata updates.
- Disturbance / variety regulated: simultaneous coding teammates could otherwise edit the same working tree, overwrite one another's changes or race on shared Team/task persistence.
- Distinct S1 units: Team spawn creates separately executing teammate Agents, including a supported tmux backend that launches a teammate process with its own Agent runtime and worktree.
- Inter-S1 disturbance: the teammates act on one project's source state and can make concurrent mutations whose effects would conflict if they shared a working tree; shared task/team metadata is also concurrently mutable.
- Attenuating coordination relation: Team spawn mechanically creates a distinct Git worktree for each teammate before launch; teammate execution is rooted there, while file locks protect shared Team/task persistence. Spawn fails if the required worktree cannot be established.
- Feedback into subsequent S1 behaviour: each teammate's filesystem actions occur against its isolated branch/worktree; the Lead later sees separate outputs/branches and merges them explicitly rather than allowing uncontrolled same-tree mutation. Team/task state updates are serialized before later actors read them.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism is not teammate plurality or messaging. It directly changes the mutable environment presented to simultaneous S1s in response to a specific cross-S1 conflict class: concurrent edits to shared project state.
- Decisive decision or feedback right: apply per-teammate workspace separation and serialize shared coordination-state mutation whenever a Team teammate is admitted.
- Decision owner: first-party deterministic runtime policy. The Lead chooses what work to delegate, but it does not choose whether the teammate receives the isolation response; the worktree is created as a mandatory spawn step.
- Supporting / enforcement mechanisms: Team spawn lifecycle; worktree manager/create/lifecycle code; Team file locks; task-store persistence; backend launch rooted in teammate worktree.
- Closure path: Team teammate admission → runtime creates isolated worktree / serializes Team state → child S1 executes against isolated mutable state → separate branch/result returns for later convergence; failed isolation blocks spawn rather than exposing shared mutable state.
- Boundary reachability: Team spawning, worktree creation and Team/task persistence are wired into the standard first-party CLI/Team runtime and require no application-authored coordinator.
- Why this is / is not agent-owned: the material attenuation decision is code-owned and deterministic. Removing the Lead model does not remove the rule that any admitted teammate is isolated; conversely the model cannot elect to bypass that coordination rule within this Team spawn path.
- Evidence: [`src/suisuicode/team/spawn.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/spawn.py); [`src/suisuicode/team/tasks/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/tasks/__init__.py); [`src/suisuicode/team/backend/tmux.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/backend/tmux.py); [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the positive S2 claim is bounded to workspace/persistence interference. It does not imply autonomous semantic negotiation among teammates. The in-process backend is not needed for the claim; the supported tmux path supplies concrete simultaneous teammate execution.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current Team's operational commitments by deciding what tasks should exist, how they are assigned/dependent, which teammates should be spawned, what instructions they receive and how current work is converged or removed.
- Disturbance / variety regulated: changing workload decomposition, multiple active teammate commitments, task dependencies/readiness, reassignment, blocked/incomplete work, teammate reports and the need to converge isolated branches into the current project.
- Whole-system current view: `TeamTaskList` exposes the Team's task population with status, assignee, dependency and readiness state; `TeamTaskGet` exposes selected commitment detail. Team/member persistence records the active organization. The S3 claim relies on these explicit queryable views, not on an unverified automatic Lead-mailbox wake-up.
- Current-control decision scope: the Lead can create tasks, update their status/assignee/dependencies, create/delete a Team, spawn Team teammates with `Agent(team_name=...)`, send directed/broadcast instructions, and in Coordinator mode inspect and merge teammate worktree branches. These actions change the current set, assignment and convergence of operational commitments.
- Decisive decision or feedback right: decide what current work should be delegated, which teammate/assignment structure should exist now, revise task state/dependencies after observed evidence, message teammates and decide how/when isolated results are merged.
- Decision owner: model-backed Lead in supported `BYPASS`/YOLO permission mode; interactive operator becomes decisive for mutating organization-tool authorization in parent-governed modes.
- Supporting / enforcement mechanisms: Coordinator tool whitelist/prompt; TeamCreate/TeamDelete; TaskCreate/TeamTaskGet/TeamTaskList/TaskUpdate; `Agent` Team spawn; TeamSendMessage; Team/task persistence; teammate worktrees; permission engine.
- Closure path: current Team task/member/worktree evidence → Lead model queries task state and selects create/update/spawn/message/merge action → permission path → Team/task/runtime state changes → later TeamTaskList/Get, repository state and teammate outputs provide changed evidence for subsequent Lead decisions.
- Boundary reachability: Coordinator mode and Team tools are registered/wired in the shipped CLI; the Team spawn path launches first-party SuisuiCode teammate runtimes. No application-authored orchestration is required.
- Why this is / is not agent-owned: in `BYPASS`, retaining Team stores and deterministic worktree machinery without the Lead model removes the task-specific judgment about decomposition, assignment, teammate creation and branch convergence. In parent-governed modes, the operator owns final authorization for the same mutating organization-level actions.
- Evidence: [`src/suisuicode/coordinator/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/coordinator/__init__.py); [`src/suisuicode/team/tools/task_list.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/tools/task_list.py); [`src/suisuicode/team/tools/task_update.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/tools/task_update.py); [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py); [`src/suisuicode/team/tools/send_message.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/team/tools/send_message.py); [`src/suisuicode/permission/engine.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/permission/engine.py); [`src/suisuicode/cli.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: Coordinator mode is opt-in behind a feature flag plus environment switch. Automatic Team Lead mailbox consumption was not found in the reviewed TUI integration, so the positive closure is episodic/query-driven through the task board and repository/worktree evidence rather than credited as push-driven wake-up.

### S3 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed Coordinator/Lead | Coordinator/Team mode is enabled and Lead selects mutating Team/Agent/task actions while permission mode is `BYPASS` | Runtime executes commitment/allocation changes directly; Team task/worktree state is queryable on later Lead turns | `coordinator/__init__.py`; Team tools; `agent_tool.py`; `permission/engine.py` |
| Parent (`P`) | Interactive operator | Lead proposes the same mutating organization action in a mode where the permission engine returns `ASK` | Operator approval permits the Team/task/spawn change and its result returns to the Lead loop; denial prevents it | `permission/engine.py`; `agent.py`; Team tools |

The parent leg is credited because approval controls organization-level commitments—creation/update of Team tasks or teammate execution—not merely an incidental file edit inside one S1.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit role with sufficiently independent evidence access, audit judgment and corrective return was established.
- Disturbance / variety regulated: Coordinator verification/merge and teammate reports regulate production convergence, but no separate audit-specific disturbance/claim channel was established.
- Decisive decision or feedback right: not established for a complementary auditor.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Coordinator verification/merge phase; ordinary tests/bash/git diff; teammate reporting; Explore/Plan/general-purpose subagents; hooks/skills.
- Closure path: absent at S3* level. Coordinator verification belongs to the same Lead production-control path, and generic subagent/skill primitives do not instantiate a default independent challenger whose audit verdict returns into corrective control.
- Why this is / is not agent-owned: multiplicity, plan roles, test execution and branch review by the governing Lead are not sufficient complementary independence. No first-party default reviewer/adversary with an independent claim-access path was found.
- Evidence: [`src/suisuicode/coordinator/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/coordinator/__init__.py); [`src/suisuicode/subagent/builtin/`](https://github.com/Yangtianspike/suisui-code/tree/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/subagent/builtin); [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user-authored skills or Team compositions could instantiate a reviewer, but uninstantiated composition is not credited as first-party closed S3*.

### Absence scope

- Surfaces inspected: Coordinator verification/merge; built-in subagent definitions; Team messaging/reporting; task board; hooks/skills; repository/test tooling; worktree convergence.
- Plausible first-party paths checked: default reviewer/adversary teammate, independent evidence channel, post-implementation audit worker, test/verifier role, branch-review gate and skill-based grading as possible S3*.
- Why no material first-party path remains: shipped verification is part of the governing Lead's production convergence, while generic role/skill primitives do not instantiate a materially independent complementary audit actor by default.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop over SuisuiCode's own organizational capability was established.
- Disturbance / variety regulated: memory, MCP, skills, remote skill installation, provider/model choice and context recovery can extend or reuse capabilities but do not close an outside-and-then strategy/adaptation function.
- Decisive decision or feedback right: not established for prospective organizational adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: memory manager/store; MCP; skill catalog/load/install; `InstallSkill`; hooks; provider configuration; compaction/recovery.
- Closure path: no closed environmental/future sensing → adaptation-option generation/evaluation → adopted change to present organizational capability/S3 loop was found. `InstallSkill` consumes a supplied GitHub URL and installs it under the normal permission path; it does not itself discover/evaluate external future-relevant capabilities.
- Why this is / is not agent-owned: current-task use or installation of a preselected extension is not evidence of a distinct future-facing intelligence function that develops and adopts strategy/capability change for the organization.
- Evidence: [`src/suisuicode/tool/install_skill.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/tool/install_skill.py); [`src/suisuicode/memory/`](https://github.com/Yangtianspike/suisui-code/tree/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory); [`src/suisuicode/skills/`](https://github.com/Yangtianspike/suisui-code/tree/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/skills); [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator or application can deliberately add new skills/MCP servers/providers, but external configuration is not imported as runtime S4 without a closed first-party prospective decision loop.

### Absence scope

- Surfaces inspected: memory; skills/catalog/install; MCP; hooks; provider configuration; Coordinator/Team modes; session/context recovery; remote skill installation.
- Plausible first-party paths checked: environment scanning, future-scenario modeling, autonomous skill/provider/tool scouting, evaluation of candidate capabilities, strategy generation and return of an adopted capability change into current control.
- Why no material first-party path remains: inspected mechanisms consume configured or directly supplied extensions for present work; no first-party actor closes a distinct future-facing adaptation cycle.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: permission modes/rules, Coordinator feature locks, system prompts, teammate tool filters, project instructions and configuration constrain operation but do not constitute legitimate ultimate-policy/identity authority.
- Decisive decision or feedback right: not established for identity or ultimate policy.
- Decision owner: developer/operator configuration remains the ultimate source of these constraints outside a qualifying runtime S5 loop.
- Supporting / enforcement mechanisms: permission engine and modes; feature flags/environment gates; Coordinator prompt/tool whitelist; teammate tool filtering; configuration/project instructions; hook/skill settings.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate runtime authority → authoritative policy decision → returned policy governing subsequent organization was found.
- Why this is / is not agent-owned: the Lead and teammates act within externally authored policy. They can make current operational commitments, but they do not possess the legitimate right to redefine SuisuiCode's identity or ultimate rules.
- Evidence: [`src/suisuicode/permission/engine.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/permission/engine.py); [`src/suisuicode/coordinator/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/coordinator/__init__.py); [`src/suisuicode/config/config.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/config/config.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator approval of a Team/task action is parent governance of S3, not evidence that the runtime has S5 identity authority.

### Absence scope

- Surfaces inspected: permission/configuration; Coordinator dual-lock and tool whitelist; teammate filters; system/project instructions; Team management; skills/hooks/MCP settings; repository-governance adjacency.
- Plausible first-party paths checked: runtime constitutional revision, autonomous ultimate-policy adjudication, identity-level escalation, authoritative persistent rule change returned into subsequent organization and repository governance as parent identity authority.
- Why no material first-party path remains: first-party mechanisms enforce externally authored constraints; no runtime actor owns legitimate ultimate-policy/identity closure.

## Recursion

Team teammates are complete first-party Agent runtimes with independent model/tool loops and isolated mutable worktrees. They therefore qualify as distinct S1 units for S2/S3 analysis. The review does not establish that each teammate recursively carries the same full Team metasystem, and the implementation deliberately constrains recursive teammate spawning.

## Variety and escalation

SuisuiCode attenuates operational variety through permission modes, tool filtering, task dependencies, file locks, dedicated teammate worktrees, non-recursive teammate controls, session/context recovery and explicit Team state. It amplifies capability through background/subagents, Team parallelism, skills/hooks/MCP and multiple providers.

Escalation from subordinate operation to current control is explicit but query-driven: the Lead can inspect the shared Team task board, change assignments/dependencies/status, spawn teammates, message them and converge separate branches. Teammate completion is persisted to Team communication state, but no standard Lead-side automatic mailbox poll/wake-up path was verified at this revision and is not required for the credited S3 closure.

## Evidence gaps

- No standard TUI caller of `Manager.poll_lead_mailboxes()` was found; automatic teammate-completion wake-up to the Lead is therefore not credited.
- The positive S2 claim is specifically deterministic workspace/persistence isolation, not evidence of autonomous semantic negotiation among teammates.
- The in-process Team backend showed a less complete construction surface than the tmux path; the positive multi-S1 claim relies on the supported concrete tmux teammate path and common Team/worktree machinery.
- No default complementary audit actor, outside-and-then adaptation loop or runtime ultimate-policy closure was found for S3*/S4/S5.
