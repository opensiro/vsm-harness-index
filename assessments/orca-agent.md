---
harness_id: orca-agent
project_name: Orca Agent
repository: https://github.com/echoVic/orca-agent
review_ref: 5838259b5f9622021db04d6fdda4d80963f17de3
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Orca Agent

## Review boundary

- System in focus: the first-party Orca coding organization around one user/session mission at frozen revision `5838259b5f9622021db04d6fdda4d80963f17de3`, including the main model/tool loop, built-in coding tools, model-visible subagent/task controls, optional worktree isolation, dynamic workflow runtime, persistent Goal mode, Goal terminal verifier, session/checkpoint machinery, permission/sandbox enforcement and supported TUI/headless/ACP/app-server surfaces where they affect organizational function.
- Purpose and identity: complete software-development tasks through an autonomous coding loop that can inspect and mutate a workspace, execute commands, verify outcomes, delegate bounded work, coordinate/steer running children, persist sessions and continue a long-lived goal until completion or a legitimate blocker.
- Relevant environment: user objectives and interventions, local project/worktree state, shell/process state, model/provider responses, tests and command evidence, MCP/external tools, project instructions/configuration, task-tree state, workflow state, durable sessions/checkpoints and sandbox/permission constraints.
- Standard-distribution boundary: Orca's shipped Rust runtime, agent loop, built-in tools, task registry, subagent/continuation machinery, worktree support, workflow runtime, Goal actor/verifier, first-party persistence and supported TUI/headless/ACP/app-server adapters are inside. DeepSeek service internals, external MCP servers, host OS policy beyond Orca's adapters, target-project governance and Pilion Browser internals are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `docs/subagents.md`; `docs/goal-mode.md`; `crates/orca-runtime/src/agent_common.rs`; `crates/orca-runtime/src/agent_loop.rs`; `crates/orca-runtime/src/subagent.rs`; `crates/orca-runtime/src/tasks.rs`; `crates/orca-runtime/src/worktree.rs`; `crates/orca-runtime/src/goal_verifier.rs`; `crates/orca-tools/src/registry.rs`; directly reached workflow/task/runtime surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows; tests and benchmarks as development evidence; `.boss`, `.trae`, `.superpowers` design/planning material when not part of shipped runtime behavior; contributor governance; website documentation rendering; Pilion Browser as a separate repository/product.
- First-party operating / deployment modes considered: interactive TUI; `orca exec` headless/JSONL; resumable/forked sessions; direct and async subagents; explicit worktree-isolated subagents; dynamic workflows; persistent Goal mode; ACP/app-server integrations; supported approval/sandbox modes.
- Recursion level: one Orca coding organization around one user/workspace mission. The main model-backed coding loop is an S1; independently executing delegated child agents are additional bounded S1 units when they perform environment-facing investigation/edit/command work. Goal verification is treated as a complementary metasystem path, not another S1.
- Reviewed revision: `5838259b5f9622021db04d6fdda4d80963f17de3`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Orca ships a first-party provider/tool feedback loop for coding. The main actor receives the current conversation and project context, chooses registered tools, receives tool results and continues until a terminal response, cancellation, approval boundary or explicit runtime stop. Built-in tools cover file reading/search, editing/writing, shell/process execution, git inspection, web access, task control, subagents, plans/goals, workflows and integrations. The same runtime backs TUI, headless/JSONL, ACP and app-server surfaces.

Delegation is not only a subprocess primitive. The main model sees a `subagent` tool with role, model, isolation, schema, continuation and deadline controls; it also sees `task_list`, `task_wait`, `task_stop`, `task_read_output`, `task_send_input` and `subagent_message`. First-party prompt guidance tells the main actor to split independent work, keep its own work non-overlapping, integrate returned evidence and avoid redundant duplicate branches. Child work can run in the current checkout or, when the model selects `isolation: "worktree"`, in a detached git worktree that is preserved when it contains changes.

The task registry provides the parent with a current view of shell, workflow and subagent work, while stop and message controls can alter active child commitments. This makes the main actor capable of regulating an active multi-S1 task tree rather than merely receiving final delegation results.

Persistent Goal mode adds a separate completion-control path. The operational model may submit a `complete` or `blocked` intent with evidence, but that tool call is explicitly non-terminal. Runtime preflight checks state/evidence and a separate DeepSeek Goal verifier is invoked with no tools and a closed response schema. It may return `achieved`, `not_achieved`, `blocked` or `indeterminate`; the Goal state machine then completes, pauses/blocks, or continues work accordingly.

Primary evidence:

- [`README.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/README.md)
- [`docs/subagents.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/subagents.md)
- [`docs/goal-mode.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/goal-mode.md)
- [`crates/orca-runtime/src/agent_common.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/agent_common.rs)
- [`crates/orca-runtime/src/subagent.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/subagent.rs)
- [`crates/orca-runtime/src/tasks.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/tasks.rs)
- [`crates/orca-runtime/src/worktree.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/worktree.rs)
- [`crates/orca-runtime/src/goal_verifier.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/goal_verifier.rs)
- [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs)

## Operational model

For ordinary coding, the main model-backed actor decides what evidence to inspect and which coding action to take, while Orca executes or rejects tool calls and feeds results back into later turns. When parallelism is useful, the same actor can create child S1s and select their role and isolation. Children have their own model/tool loop and return reports or durable continuation identifiers.

The main actor can observe the active task set, wait for state changes, read task output, stop a running task and steer a running child before its next provider call. Therefore the parent can change current operational commitments after delegation. For work that risks shared-checkout interference, the model-visible `isolation: "worktree"` option moves a child to a detached git worktree, changing the operational environment of that child before it acts.

In Goal mode, an operational actor's terminal claim is deliberately separated from the authority to accept the claim. A tool-free verifier examines the objective, evidence, claimed state, viable fixable gaps and last model response; its returned judgment changes whether Orca completes, blocks or continues.

## S1 — Operations

- State: A
- Function: perform environment-facing software-development work by interpreting a task, inspecting repository/process evidence, choosing coding actions, mutating files, running commands/tests and reacting to returned results.
- Disturbance / variety regulated: heterogeneous source trees, build/test failures, command output, changing workspace state, external information, model/tool errors and implementation choices encountered while completing the requested software task.
- Decisive decision or feedback right: choose which available repository/tool action to invoke next, which evidence to inspect, what edit/command to perform, whether to delegate, and when the current operation has enough evidence to report or submit a terminal intent.
- Decision owner: the model-backed Orca main actor and, for bounded delegated work, each model-backed child agent.
- Supporting / enforcement mechanisms: agent loop; tool registry/router; shell and file tools; task registry; provider adapter; permissions/sandboxing; sessions/checkpoints; MCP; cancellation and budget enforcement.
- Closure path: user/goal and current workspace state → model request → agent selects action/tool → first-party runtime executes/rejects → result enters later model context → actor changes subsequent work or reports an outcome.
- Boundary reachability: the installed Orca TUI/headless runtime directly instantiates this loop and exposes the built-in coding tool surface; no application-side agent implementation is required.
- Why this is / is not agent-owned: removing the model-backed actor while retaining Orca's deterministic runtime leaves execution/storage/policy machinery but removes the open-ended judgment that selects and sequences coding work.
- Evidence: [`README.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/README.md); [`crates/orca-runtime/src/agent_loop.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/agent_loop.rs); [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is an external dependency; the credited S1 is Orca's first-party role/tool/feedback composition.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference between concurrently executing Orca S1 units by letting the parent agent assign non-overlapping work and, where shared-checkout file mutation would collide, place a child in a separate detached worktree.
- Disturbance / variety regulated: concurrent main/child or child/child coding work can inspect and mutate the same checkout, causing overlapping edits, stale assumptions or destructive interference when independently bounded branches touch the same files/state.
- Decisive decision or feedback right: decide whether a delegated branch should run against the shared checkout or an isolated worktree and shape delegated scopes so concurrently active work remains non-overlapping.
- Decision owner: the main model-backed Orca actor. The `subagent` schema exposes `isolation: none|worktree` directly to the model, while first-party delegation guidance requires the parent to choose independent branches and keep its own concurrent work non-overlapping.
- Supporting / enforcement mechanisms: detached git worktree creation/removal; frozen child launch configuration; task-tree capacity/queueing; child continuation identity; deterministic worktree preservation when a child leaves changes.
- Closure path: parent identifies parallel work with possible shared-state interference → parent selects bounded non-overlapping scope and, when needed, `isolation: "worktree"` → runtime creates an isolated checkout and child operates there → child's result/worktree outcome returns to the parent → parent integrates or continues from the separated state rather than allowing concurrent mutation in one checkout.
- Boundary reachability: `subagent` is a direct model-visible built-in tool in the standard runtime; worktree isolation is an explicit shipped call option and `WorktreeGuard` implements the detached checkout path.
- Why this is / is not agent-owned: Orca deterministically creates the worktree once requested, but the model-backed parent owns the situational choice to split work and select isolation. Without that actor, the runtime does not independently decide which semantic work branches require isolation.
- Evidence: [`docs/subagents.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/subagents.md); [`crates/orca-runtime/src/agent_common.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/agent_common.rs); [`crates/orca-runtime/src/subagent.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/subagent.rs); [`crates/orca-runtime/src/worktree.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/worktree.rs); [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: queue/fairness/capacity controls are not the S2 witness. The credited relation is specifically the parent actor's non-overlap/isolation decision for multiple environment-facing S1s.
- Distinct S1 units: the main Orca coding actor and independently executing child agents, or multiple child agents, each running its own model/tool loop against a project environment.
- Inter-S1 disturbance: concurrent coding units can otherwise work from and mutate the same checkout, creating overlapping edits or inconsistent shared-state assumptions.
- Attenuating coordination relation: the parent actor scopes branches as non-overlapping and can place a child in a detached worktree before execution.
- Feedback into subsequent S1 behaviour: the isolation decision changes the filesystem state visible to the child for all later tool calls; completion returns the child/worktree outcome to the parent, which then chooses integration or further work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mapping depends on a concrete concurrent shared-checkout mutation disturbance and a first-party isolation/non-overlap response, not on delegation or messaging by themselves.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current multi-task Orca organization by observing active work and intervening in running child commitments when current execution needs reprioritization, stopping or steering.
- Disturbance / variety regulated: children can be slow, wrong-direction, blocked, redundant, awaiting interaction, or no longer aligned with the parent actor's evolving current understanding; background shell/workflow/subagent commitments can remain active while the main operation changes.
- Decisive decision or feedback right: inspect the current task set, choose whether an active task should continue or stop, and send new guidance into a running child before its next model request.
- Decision owner: the main model-backed Orca actor through model-visible `task_list`, `task_wait`, `task_stop` and `subagent_message` controls.
- Supporting / enforcement mechanisms: task registry and task summaries; cancellation tokens; task-tree ownership; runtime message injection; execution leases/queues; lifecycle persistence. These enforce or transport the parent's decision but do not own it.
- Closure path: current task/subagent status and notifications become model-visible → main actor judges current whole-task needs → actor stops a task or sends revised guidance (and may later resume/redelegate) → runtime applies the intervention → subsequent child/current operation changes.
- Boundary reachability: these controls are direct built-in model-visible tools in the shipped Orca runtime and operate on the same session task registry that owns shell, workflow and subagent work.
- Why this is / is not agent-owned: removing the main model actor while leaving the registry/cancellation/message machinery preserves visibility and enforcement but removes the discretionary judgment about which active commitment should be changed and why.
- Evidence: [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs); [`crates/orca-runtime/src/tasks.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/tasks.rs); [`README.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: deterministic concurrency ceilings, budgets and workflow phase gates are supporting enforcement and are not themselves used to claim S3 ownership.
- Whole-system current view: `task_list` exposes background shell, workflow and subagent work for the current session; completion/status notifications and task waits expose changes in those commitments.
- Current-control decision scope: the main actor can stop an active task and inject guidance into a running child, changing current commitments rather than merely allocating the original subtask.

## S3* — Complementary audit

- State: A
- Function: independently challenge the operational actor's claim that a persistent Goal is complete or genuinely blocked before Orca accepts a terminal organizational state.
- Disturbance / variety regulated: an operational model can prematurely declare success, cite weak evidence, or classify a still-model-fixable gap as an external blocker.
- Decisive decision or feedback right: judge the submitted terminal intent and evidence as `achieved`, `not_achieved`, `blocked` or `indeterminate`.
- Decision owner: a separate DeepSeek Goal verifier model invocation with a verifier-specific system role and no tools; deterministic preflight constrains admissible evidence/state but does not make the semantic judgment.
- Supporting / enforcement mechanisms: deterministic terminal preflight; closed verifier JSON schema; bounded verifier input/output; verifier budget; Goal actor/state machine; continuation gate.
- Closure path: operational actor submits terminal intent/evidence → runtime closes the outer turn and preflights the claim → separate tool-free verifier makes an audit judgment → Goal actor accepts completion/blocking or records a non-achieved/indeterminate result → subsequent operation terminates, pauses or continues accordingly.
- Boundary reachability: persistent Goal mode is a supported first-party TUI/runtime mode, and `goal_verifier.rs` is wired directly into its terminal transition rather than living only in tests or CI.
- Why this is / is not agent-owned: the semantic terminal judgment comes from a separate model invocation. Removing that verifier while retaining deterministic preflight eliminates the independent learned judgment over whether evidence actually establishes the requested terminal state.
- Evidence: [`docs/goal-mode.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/goal-mode.md); [`crates/orca-runtime/src/goal_verifier.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-runtime/src/goal_verifier.rs); [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary command/test verification inside the S1 loop is not the witness; the mapping relies on Goal mode's separate verifier role and returned terminal-control effect.
- Claim being audited: the operational actor's claim that the persistent mission objective has been achieved or that further model work is legitimately blocked.
- Ordinary reporting path: the main actor calls `update_goal` with a requested terminal state, reason and concrete evidence gathered during ordinary operation.
- Complementary access path: the verifier receives the persistent objective, structured evidence, claimed state, viable model-fixable gaps and last model response after deterministic confirmation that the outer turn/tool state is terminal; it uses a separate tool-free provider call and closed verifier role.
- Independence boundary: verifier conversation/role and provider request are separate from the ordinary coding actor's conversation and tool authority; the operational actor cannot make its own `update_goal` call terminal by itself.
- Who acts on findings: Orca's Goal actor/runtime uses the verifier result to complete, block/pause or continue the persistent operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective organizational adaptation loop was established at the selected mission recursion.
- Disturbance / variety regulated: not established at S4 ownership level.
- Decisive decision or feedback right: not established. Orca can search the web, remember project facts, retain sessions, resume children and execute dynamic workflows, but those mechanisms support current/future task execution without a distinct prospective actor that develops adaptation options and changes persistent organizational capability or strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: web search; MCP; automatic/explicit memory; session history; continuation checkpoints; reusable skills/agents/workflows; model/config selection.
- Closure path: not applicable; no external/prospective distinction → adaptation option → current capability/S3 return loop was established.
- Why this is / is not agent-owned: the S1 actor can learn facts and use them later, but memory and research remain information available to operation rather than a separately evidenced intelligence/adaptation function.
- Evidence: [`README.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/README.md); [`docs/memory.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/memory.md); [`docs/subagents.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/subagents.md).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: this does not deny useful learning or reuse; it applies the Profile's stronger outside-and-then organizational adaptation threshold.

### Absence scope

- Surfaces inspected: web/MCP tools; automatic and explicit memory; persistent sessions and checkpoints; skills/custom agents; dynamic/reusable workflows; Goal mode; model/configuration surfaces.
- Plausible first-party paths checked: external research informing future work; durable learned project facts; workflow/agent reuse; model changes; persistent goals; automatic self-improvement or capability mutation.
- Why no material first-party path remains: the located mechanisms store/retrieve facts, resume execution or expose operator/project-defined reusable capabilities. No shipped path was found in which an S4 owner senses prospective environmental distinctions, develops adaptation options and returns a selected option as a persistent change to Orca's current organizational capability/strategy.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established at the selected Orca mission recursion.
- Disturbance / variety regulated: not established at S5 ownership level.
- Decisive decision or feedback right: not established. User goals, trust, approval modes, permission rules, project instructions and sandbox boundaries constrain or direct operation, but the reviewed runtime does not establish a separate identity/ultimate-policy issue-resolution loop whose authoritative decision is returned as organization-level policy.
- Decision owner: not established inside the assessed organization.
- Supporting / enforcement mechanisms: folder trust; plan/suggest/auto-edit/full-auto modes; permission profiles/rules; sandbox boundaries; project `AGENTS.md`/config; Goal objective; user approvals and steering.
- Closure path: not applicable; no qualifying identity/ultimate-policy issue → legitimate S5 authority → authoritative policy decision → returned governance of later operation path was established.
- Why this is / is not agent-owned: the main actor cannot edit an active Goal objective through `update_goal`, and deterministic policy enforcement does not own the underlying purpose/policy decision. Generic user approval or task steering remains operational rather than sufficient S5 evidence.
- Evidence: [`README.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/README.md); [`docs/goal-mode.md`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/docs/goal-mode.md); [`crates/orca-approval/src/policy.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-approval/src/policy.rs); [`crates/orca-tools/src/registry.rs`](https://github.com/echoVic/orca-agent/blob/5838259b5f9622021db04d6fdda4d80963f17de3/crates/orca-tools/src/registry.rs).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: a chosen recursion around a project institution could motivate a separate parent-governance analysis, but the standard mission runtime reviewed here does not by itself close that stronger S5 relation.

### Absence scope

- Surfaces inspected: Goal objective/create/update boundaries; user steering; trust and approval modes; permission rules/profiles; project instructions/configuration; sandbox enforcement; session/model settings; workflow/subagent inheritance.
- Plausible first-party paths checked: agent revision of mission purpose; parent revision of identity/ultimate policy with returned closure; safety-policy exception handling; persistent governance decisions; approval escalation; project instruction reload.
- Why no material first-party path remains: located controls either specify the task, enforce preselected execution policy or provide ordinary operational approval/steering. No dedicated identity/ultimate-policy resolution loop at the declared recursion was established.

## Recursion

The assessment uses one user/workspace mission as the system-in-focus. The main actor and independently executing children are operational units inside that recursion; workflows, task control and Goal verification are metasystem mechanisms for the same mission. Repository development/CI and external products are outside the ownership boundary.

## Variety and escalation

Orca absorbs coding variety through model/tool discretion, delegation and durable continuation. Parallel work can be separated into worktrees; active child commitments can be inspected, steered or stopped by the parent actor. Permission/sandbox interactions, user questions and typed blockers are escalation paths, but their existence does not automatically establish S5.

## Evidence gaps

The frozen revision provides strong direct evidence for S1, model-selected worktree coordination, model-visible task intervention and Goal verification. S2/S3 confidence is slightly lower than S1/S3* because these functions depend on use of optional multi-agent controls in a mission that actually runs multiple S1 units. No unresolved evidence gap is large enough to require `?` for S4/S5 after review of the documented runtime, goal, memory, permission, project-configuration and delegation surfaces.
