---
harness_id: suisuicode
project_name: SuisuiCode
repository: https://github.com/Yangtianspike/suisui-code
review_ref: c9017b0613b22151325a5904a521aefe4c62abbc
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-11
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# SuisuiCode

## Review boundary

- System in focus: the first-party SuisuiCode terminal coding-agent composition at frozen revision `c9017b0613b22151325a5904a521aefe4c62abbc`, including the main ReAct loop, coding tools, permission/session/context machinery, background SubAgent runtime, task-control tools, worktree isolation, memory updater, and the shipped Team/Coordinator surfaces insofar as their frozen implementation is operationally reachable.
- Purpose and identity: perform repository-facing coding work in a terminal, optionally delegate bounded work to autonomous subagents, regulate those active subordinate runs, preserve project/user guidance across later operation, and expose richer team/worktree collaboration machinery.
- Relevant environment: user coding objectives and approvals; repository/workspace state; model-provider responses; tool/process results; Git/worktree state; configured MCP servers; project/user instructions and memory; optional user/project subagent definitions.
- Standard-distribution boundary: shipped `src/suisuicode` runtime, built-in tools/subagent definitions, standard user/project subagent-definition loader, TaskManager, worktree manager, memory manager, permission/context/session/hook machinery, and model-facing Team/Coordinator primitives are inside. External model providers, MCP servers, tmux/iTerm applications, user-authored hooks/skills/subagent prompts, and Git itself are dependencies. Their internal organizational functions are not inherited.
- Credited operating / distribution surfaces: `README.md`; `src/suisuicode/cli.py`; `src/suisuicode/agent/agent.py`; `src/suisuicode/agent/run_to_completion.py`; `src/suisuicode/agent/agent_tool.py`; `src/suisuicode/agent/agent_worktree.py`; `src/suisuicode/task/manager.py`; `src/suisuicode/task/tools.py`; `src/suisuicode/subagent/definition.py`; `src/suisuicode/subagent/parser.py`; `src/suisuicode/memory/manager.py`; `src/suisuicode/memory/prompts.py`; and the inspected Team/Coordinator implementation.
- Adjacent first-party surfaces excluded from ownership: tests and chapter/spec commentary as authority by themselves; generic hooks and externally supplied MCP/skill logic; operator slash commands; development-only examples; and any advertised Team behavior that does not close through the frozen runtime implementation.
- First-party operating / deployment modes considered: ordinary terminal main-agent operation; built-in and forked foreground/background SubAgents; standard project/user subagent definitions including `isolation: worktree`; task-list/status/stop/re-task control; persistent memory update/load; and opt-in Coordinator/Team mode as an inspected but partially non-closing path.
- Recursion level: one SuisuiCode coding organization. Autonomous coding subagents are operational S1 cells when delegation is used; the main agent can act as the current-control lead over that population. In single-agent use the same model/tool loop directly supplies S1.
- Reviewed revision: `c9017b0613b22151325a5904a521aefe4c62abbc`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The ordinary path is a first-party ReAct coding loop. `cli.py` constructs the provider-backed main `Agent`, tool registry, permission engine, context/session state and optional extensions. `Agent.run` repeatedly presents the model with currently permitted tool definitions, executes selected tool calls, returns actual results into the conversation and lets the same model choose the next action until a final response or bounded stop condition.

SubAgent delegation is also operational in the frozen distribution independently of Team mode. The model-facing `Agent` tool resolves a built-in, user/project-defined or fork definition; constructs a child `Agent` with the parent provider, registry and permission engine; optionally switches model/tool scope; and executes it foreground or through `task.Manager`. `general-purpose` is a shipped full-tool operational role. Background tasks retain status, result, tool activity and usage. The main agent receives `TaskList`, `TaskGet`, `TaskStop` and `SendMessage`, giving the same autonomous lead a current view and intervention surface over its delegated S1 population.

Worktree isolation is a function-specific constructor on this subagent path. A standard subagent definition can request `isolation: worktree`; `AgentTool` then creates a dedicated Git worktree and `_execute_with_worktree` executes the child under `with_cwd(wt.path)`, explicitly telling it that it is isolated from the parent and must reread local files before edits. The isolation relation is selected by definition/configuration rather than by a shipped autonomous coordination policy, so it supports S2 at constructor level rather than S2=A.

The advertised Agent Team/Coordinator path is not used to establish the positive findings below because the frozen implementation contains a material closure gap. The tmux backend starts `python -m suisuicode --team-member ...`, but `cli.py` calls `run_team_member` without a constructed `sub_agent`/provider/registry/engine; `run_team_member` only executes mailbox tasks when `agent is not None`. The in-process Team builder likewise creates a child `Agent` with `provider=None`, `registry=None` and `engine=None`. Team task/mailbox/worktree structures are therefore evidence of intended organization and useful primitives, but this assessment does not silently promote the advertised Team topology into autonomous S2/S3 closure.

SuisuiCode ships a memory-update **constructor**, but the frozen standard CLI does not close its autonomous model-to-memory loop. After a main turn, `Agent.run` schedules `memory.Manager.update_async`; however `cli.py` builds `Manager(provider=None, model="")`, and `tui/app.py` attaches the selected provider only to the main `Agent`, not to this Manager. `update_async` returns immediately when its own provider is `None`. The first-party `Manager.set_provider` method can compose a provider-dependent memory updater, but the frozen tracked `src/suisuicode` tree has no call to that setter or direct replacement of the Manager provider. Existing/manually maintained memory still loads into later session prompts. This supports a proposed *constructor-level* S4 rather than the original claim that automatic model-authored S4 adaptation is operational in the ordinary CLI.

## Operational model

A user gives the main model a coding objective. The model chooses coding/tool actions from the live registry and revises later choices from returned file/process/tool evidence. It can also delegate operational work to child model loops. For background children, first-party task state provides a whole subordinate-population view and model-facing controls to inspect, cancel or re-task work. Separately, isolated-subagent definitions can attenuate concurrent workspace interference, while a memory-updater constructor could convert completed-turn distinctions into future guidance **if a developer binds its provider**; the pinned ordinary CLI does not bind it.

## S1 — Operations

- State: A
- Function: transform a coding objective into repository/process actions and a task result through iterative model-selected tool use with environment feedback.
- Disturbance / variety regulated: repository state, implementation alternatives, tool/process outcomes, context pressure, provider responses, permission outcomes and user corrections.
- Decisive decision or feedback right: choose the next substantive coding/delegation/tool action and revise subsequent action from returned evidence.
- Decision owner: the configured model actor in the first-party main `Agent` loop; spawned child `Agent` instances own the same task-local operational discretion for delegated S1 work.
- Supporting / enforcement mechanisms: tool registry/executor, permission engine, context manager and compaction, session persistence, iteration bounds, hooks, MCP adapters, TaskManager and worktree machinery.
- Closure path: user objective/current context → model chooses a tool/action → SuisuiCode executes it → actual tool/environment result is appended to the conversation → the same model receives that result and chooses another action or a final answer.
- Boundary reachability: `suisuicode` constructs this shipped provider-backed `Agent` directly; built-in coding tools and standard subagent runtime are wired by `cli.py` without requiring an external orchestration framework.
- Why this is / is not agent-owned: if the model actor is removed while deterministic permissions, tool execution, context management and persistence remain, those mechanisms can enforce constraints but cannot choose open-ended coding actions. The substantive operational discretion is therefore agent-owned.
- Evidence: [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md); [`src/suisuicode/cli.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py); [`src/suisuicode/agent/agent.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py); [`src/suisuicode/agent/run_to_completion.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/run_to_completion.py); [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is supplied by an external provider. The finding credits SuisuiCode's first-party loop that places the model in the operational decision role, not provider-side internals.

## S2 — Coordination

- State: C
- Function: attenuate workspace interference among distinct delegated coding S1 cells by assigning an isolated Git worktree execution root to subagents whose standard definition requests worktree isolation.
- Disturbance / variety regulated: concurrent coding agents operating against one checkout can overwrite or observe one another's in-progress file changes and lose clear ownership of a change set.
- Distinct S1 units: the main Agent tool can instantiate multiple independent child `Agent` loops, including the shipped full-tool `general-purpose` role and fork/user/project roles, with separate conversations/runtime state and foreground/background lifecycles.
- Inter-S1 disturbance: mutating child agents can otherwise act against the same repository workspace, coupling independent work through shared files and stale observations.
- Attenuating coordination relation: `Definition.isolation` exposes the explicit `worktree` mode; `AgentTool` routes such a child through `_execute_with_worktree`, which creates a dedicated worktree and runs the child's full model/tool loop under that worktree cwd.
- Feedback into subsequent S1 behaviour: the isolation result changes the actual filesystem root seen by that child; the injected worktree notice also requires local rereads before editing, so subsequent S1 file decisions/actions occur against the isolated checkout rather than the parent's live workspace.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is specifically an interference-attenuation mechanism for concurrent mutating S1s. Generic background delegation, TaskManager state and mailbox surfaces are not by themselves used as S2 evidence.
- Decisive decision or feedback right: bind an operational child to a dedicated worktree so its mutable workspace is separated from other S1 work.
- Decision owner: no shipped autonomous coordination actor owns that isolation choice as an organizational policy. The developer/operator selects it in the subagent definition; first-party runtime then deterministically enforces the relation.
- Supporting / enforcement mechanisms: subagent-definition parser; worktree manager; unique worktree creation; `with_cwd`; worktree context notice; auto-cleanup/preservation reporting.
- Closure path: a standard subagent definition specifies `isolation: worktree` → the model delegates work to that role → SuisuiCode creates a dedicated worktree → the child Agent executes with that worktree as cwd → its later reads/writes remain separated from the parent's checkout → cleanup preserves or removes the isolated branch/worktree according to result state.
- Boundary reachability: `isolation: worktree` is an explicit first-party definition field accepted from the standard user/project subagent-definition surfaces and executed by the ordinary model-facing `Agent` tool. The user supplies the role/configuration but does not have to invent the isolation path.
- Why this is / is not agent-owned: removing the main model's discretion leaves the same definition-selected worktree relation available to any invocation; the decisive coordination policy is not autonomously selected by a shipped coordinator. The S2-specific constructor is therefore `C`, not `A`.
- Evidence: [`src/suisuicode/subagent/definition.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/subagent/definition.py); [`src/suisuicode/subagent/parser.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/subagent/parser.py); [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py); [`src/suisuicode/agent/agent_worktree.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_worktree.py); [`src/suisuicode/subagent/builtin/general-purpose.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/subagent/builtin/general-purpose.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: none of the inspected built-in role files makes worktree isolation the autonomous default; the positive finding is intentionally constructor-level. The frozen Team mode is not used to strengthen this state because its teammate execution path does not close reliably.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current population of delegated operational subagents by deciding which work to spawn, observing all background-run status/activity, cancelling work and re-tasking retained agents.
- Disturbance / variety regulated: changing workload decomposition, long-running or failed delegated work, redundant/obsolete current tasks, child-agent completion and the need to redirect follow-up work while the main objective is still active.
- Decisive decision or feedback right: decide whether/what to delegate, which child role/model/task to instantiate, whether a running task should be cancelled, and what follow-up task should be sent to a completed named agent.
- Decision owner: the autonomous main model actor, because `Agent`, `TaskList`, `TaskGet`, `TaskStop` and `SendMessage` are registered as model-facing tools in the ordinary first-party composition.
- Supporting / enforcement mechanisms: TaskManager's task registry/status/result/activity accounting; background asyncio lifecycle; name registry; completion queue; tool schemas; deterministic cancel/restart execution.
- Closure path: main model delegates via `Agent` → child Agent runs as an independent S1 under TaskManager → TaskManager records current status/activity/result → model can inspect the population through `TaskList`/`TaskGet` → model decides to wait, stop or issue follow-up work → `TaskStop` cancels or `SendMessage` restarts the retained child conversation, changing subsequent current operation.
- Whole-system current view: `TaskList` returns all tracked background tasks, with id, name, status, tool count and last activity; `TaskGet` adds result/error, timing and usage. At the declared delegated-subagent recursion this is a current view of the operational child population managed by the main agent.
- Current-control decision scope: the main model can create operational commitments through `Agent`, terminate an active commitment through `TaskStop`, inspect completion/failure, and assign follow-up work through `SendMessage`; these decisions alter which S1 work remains active and what retained agents do next.
- Boundary reachability: `cli.py` registers the `Agent`, `TaskList`, `TaskGet`, `TaskStop` and `SendMessage` tools in the ordinary shipped main-agent registry, and `AgentTool`/TaskManager instantiate and track the same first-party child Agent loops; no Team-mode path or application-authored supervisor is required.
- Why this is / is not agent-owned: TaskManager itself only records/enforces lifecycle transitions. Without the main model actor, the registry can list or cancel only preselected ids but does not decide which current work should exist, be stopped or be re-tasked. The substantive supervisory discretion belongs to the model.
- Evidence: [`src/suisuicode/cli.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py); [`src/suisuicode/agent/agent_tool.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent_tool.py); [`src/suisuicode/task/manager.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/task/manager.py); [`src/suisuicode/task/tools.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/task/tools.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this S3 finding is the ordinary functional SubAgent/TaskManager composition, not the richer advertised Coordinator/Team composition. `SendMessage` resumes completed named agents rather than modifying an already-running child's prompt; a currently wrong run is instead stopped and replaced/redelegated.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary operational-audit loop with sufficiently independent access, audit judgment and corrective return is established at the assessed recursion.
- Disturbance / variety regulated: permission checks, hooks, tests, worktree isolation and lead-side result inspection provide safety/visibility, but none closes a materially independent audit channel over current operational S1 claims.
- Decisive decision or feedback right: no distinct first-party auditor is shown owning an independent approve/reject/escalate judgment over the operating subagent population.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: permission engine; lifecycle hooks; task result/status inspection; worktree cleanup; ordinary user review; repository tests.
- Closure path: not applicable for the negative finding.
- Claim being audited: no distinct operational claim is assigned to an independent first-party auditor in the standard runtime.
- Ordinary reporting path: child results/status/tool activity return through TaskManager and ordinary model/tool results to the same main supervisory agent.
- Complementary access path: not established. Hooks are configurable extension points supplied by operator/project configuration, while worktree and permission checks are inline execution/support mechanisms rather than a separate route to operational reality.
- Independence boundary: no qualifying shipped autonomous auditor with materially different access from the ordinary lead/task path was found. Development tests and user review remain outside runtime S3* ownership.
- Who acts on findings: the main model or human can react to normal task/tool results; there is no distinct S3* finding-and-return closure.
- Why this is / is not agent-owned: autonomous main/subagents can inspect work, but the same operating/supervisory actors do not become a complementary audit function merely by reviewing their own outputs.
- Evidence: [`src/suisuicode/task/tools.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/task/tools.py); [`src/suisuicode/agent/agent.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py); [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream project can configure hooks or specialist agents to perform review, but generic extensibility does not establish first-party S3*.

### Absence scope

- Surfaces inspected: main/subagent event loops; TaskManager and result tools; Team/Coordinator task/mailbox surfaces; permission engine role; hook lifecycle; worktree execution/cleanup; built-in subagent definitions; tests/development surfaces.
- Plausible first-party paths checked: main lead verification as audit; TaskGet/result inspection; worktree isolation as independent observation; hooks as reviewer; Plan mode; permission approval; project tests.
- Why no material first-party path remains: the inspected checks either belong to ordinary production/supervision, are deterministic enforcement, are generic user-configurable extensions, or are development evidence. None supplies a distinct complementary access route plus independent audit judgment and corrective return.

## S4 — Outside-and-then adaptation

- State: C
- Function: first-party provider-injectable memory updater can select and persist future-oriented notes from completed work; the original standard CLI leaves its provider unbound.
- Disturbance / variety regulated: recurring user corrections, conventions and project decisions whose future reuse can avoid rediscovery or repeated mistakes.
- Decisive decision or feedback right: **when externally composed**, a model may decide which past observations merit future retention and select structured note create/update/delete actions.
- Decision owner: the injected model could own the memory-update judgment, but there is **no configured memory-update model** in the frozen standard CLI. Its built-in storage and event scheduling do not decide what to adapt.
- Supporting / enforcement mechanisms: `Agent.run` per-turn trigger; `Manager.update_async`; explicit `Manager.set_provider`; provider guard; JSON action parsing; two note stores; `MEMORY.md`; `load_index` at next startup.
- Closure path: conditional first-party constructor: external developer calls `Manager.set_provider` → later completed Agent turn triggers `update_async` → supplied model may select note actions → Store writes them → later startup reloads notes into Agent context. **Ordinary CLI instead:** `Manager(provider=None)` → selected provider goes into the main Agent only → scheduled memory update returns at its `None` guard → no model-written update occurs from this path.
- Boundary reachability: `cli.py#L139-L151` instantiates unbound Manager and `cli.py#L307-L325` passes it to `new_app`. `tui/app.py#L702-L788` configures a main provider and passes the unchanged manager to Agent. Frozen tracked-source search finds the sole `set_provider` *definition* in `memory/manager.py#L117` and no call site. The purpose-specific setter and update/store/load machinery remain available to a developer-composed caller, not a default autonomous mode.
- External distinction: completed user/project discussions can supply feedback and project conventions if a model is attached.
- Future / prospective distinction: the memory updater's prompt explicitly requests lessons worth retaining for future sessions, not only storing raw transcript text.
- Adaptation option generated: with an attached provider, the model can select structured create/update/delete actions; without the binding, no such model-generated output is produced by the CLI route.
- Path back into current capability / S3: previously stored notes are loaded into future session prompts, but **new model-selected memory** is not created through the original unbound provider path.
- Why this is / is not agent-owned: `A` cannot be credited where the decisive actor is never wired in the claimed first-party standard mode. `C` is proposed because `Manager.set_provider` and its integrated turn-trigger/store/load machinery deliberately expose a function-specific, developer-composable adaptation loop. Whether this constitutes S4 rather than task-local preference persistence still requires independent semantic review under the original Methodology.
- Evidence: [`cli.py#L139-L151`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py#L139-L151); [`cli.py#L307-L325`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py#L307-L325); [`tui/app.py#L702-L788`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/tui/app.py#L702-L788); [`agent.py#L545-L569`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py#L545-L569); [`manager.py#L117-L164`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/manager.py#L117-L164); [`memory/prompts.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/prompts.py).
- Basis: exact original frozen-tree call-path audit and existing in-process conditional memory-manager reproduction; no full CLI end-to-end success is claimed.
- Confidence: high for missing provider in standard CLI; medium for proposed S4 constructor `C` until independent Index review.
- Caveats: a blank `MEMORY.md`, user-managed notes, or the mere existence of an LLM prompt is not autonomous adaptation. No unseen external integration may be silently credited to the standard distribution.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy tension-and-resolution loop is established at the chosen recursion.
- Disturbance / variety regulated: permissions, modes, system prompts, subagent definitions, coordinator instructions and memory constrain or inform operation, but none is shown resolving a dispute about the organization's identity or ultimate policy.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: permission modes/rules; user approvals; configuration; system/subagent prompts; Coordinator feature flag; memory/instructions; hook policies.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: models make task and supervisory decisions, and a memory model could decide note adaptations **if externally bound**, but no first-party actor is given ultimate authority to resolve identity/policy tensions and return such a resolution into subsequent organization-wide operation.
- Evidence: [`README.md`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/README.md); [`src/suisuicode/cli.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py); [`src/suisuicode/coordinator/__init__.py`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/coordinator/__init__.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: human control over permissions or feature/configuration choices is ordinary parent/operator control over implementation and task execution; it is not promoted to S5 without an identity/ultimate-policy function.

### Absence scope

- Surfaces inspected: system prompt and Coordinator prompt; permission modes/rules/approvals; user/project subagent definitions; Team creation/deletion; hooks; project/user memory; CLI/configuration surfaces.
- Plausible first-party paths checked: permission approval as ultimate authority; Coordinator role as identity owner; Team lifecycle as policy; memory/user preferences as identity adaptation; system prompts and feature flags as S5 policy.
- Why no material first-party path remains: these surfaces configure, constrain or adapt coding operation but do not present an identity/ultimate-policy issue to a legitimate ultimate authority and close the resulting resolution back into organization-wide operation.

## Team-mode closure caveat

The frozen repository advertises Agent Team and Coordinator Mode and ships substantial Team persistence, mailbox, dependency and worktree machinery. Those surfaces are not ignored; they were inspected as plausible S2/S3 evidence. However the frozen executable path does not close teammate cognition in the standard Team backends: tmux/iTerm subprocesses enter `run_team_member` without a constructed agent/provider/registry/engine, while the in-process builder creates an `Agent` with those core dependencies unset. The positive S2/S3 findings above therefore rely only on the independently operational ordinary SubAgent/TaskManager/worktree composition. This prevents architecture intent from being credited as runtime autonomy.

## Assessment summary

SuisuiCode closes autonomous S1 operations and S3 delegated-task current control; S2 worktree isolation is constructor-level. Its memory updater exposes an S4-specific provider-binding interface and store/load path, but the standard CLI never binds the memory provider, so the originally claimed autonomous S4 loop is not evidenced at the pinned revision. The proposed `S4=C` constructor interpretation is subject to independent Index semantic review. No S3* corrective-audit or S5 ultimate-policy loop is established.

**Author-proposed corrected vector (review required):** `A · C · A · — · C · —`
