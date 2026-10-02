---
harness_id: neo
project_name: Neo
repository: https://github.com/matrixheaven/neo
review_ref: 2828e253852a98cace95dc404caf3ac8a3e45bce
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: A(P)
---

# Neo

## Review boundary

- System in focus: one first-party Neo-managed coding project/session organization at frozen revision 2828e253852a98cace95dc404caf3ac8a3e45bce, including the main model/tool loop, model-created delegates and swarms, workflow-hosted child agents, workflow/task state, operator task-browser controls, project instruction authority, skills and supported interactive/headless execution.
- Purpose and identity: perform local software-engineering work on a project while allowing the main agent to delegate bounded specialist work, supervise current execution, invoke review workflows and preserve project-level operating instructions.
- Relevant environment: the user/operator, target repository/workspace and git state, files and shell processes, model/provider responses, optional MCP/tool integrations, project instruction files, tests/build commands and external package/runtime dependencies.
- Standard-distribution boundary: shipped Neo Rust crates, CLI/TUI/headless modes, neo-agent-core runtime, model-facing tools, multi-agent runtime, built-in workflows, project/user workflow registry, task/background runtime, project instruction engine and built-in skills are inside. External model providers, MCP servers, host OS/git, target-project code and third-party commands are dependencies/environment.
- Credited operating / distribution surfaces: README.md; crates/neo-agent-core/src/runtime/turn_loop.rs; crates/neo-agent-core/src/tools/delegate.rs; crates/neo-agent-core/src/tools/delegate_controls.rs; crates/neo-agent-core/src/multi_agent/; crates/neo-agent-core/src/workflow/; crates/neo-agent-core/src/worktree.rs; crates/neo-agent-core/src/tools/background_tasks.rs; crates/neo-agent-core/src/tools/workflow.rs; crates/neo-agent-core/src/instructions/; crates/neo-agent-core/src/skills/; crates/neo-agent/src/modes/interactive/; crates/neo-agent/src/modes/task_browser.rs.
- Adjacent first-party surfaces excluded from ownership: repository CI/release machinery, unit/integration tests as development validation, contributor-only engineering notes, source-code comments describing future work and benchmark/test fixtures that are not reached by the supported runtime mode being credited.
- First-party operating / deployment modes considered: interactive TUI; headless/local coding turns; foreground/background Delegate and DelegateSwarm; built-in and saved Workflow execution; built-in large-refactor and code-review workflows; /tasks operator control; /init project-guide authoring; project/user skills and project AGENTS.md instruction loading.
- Recursion level: one project/session organization. The main coding agent and separately instantiated mutation-capable child agents are operational S1 units when they act on repository work. The main agent may occupy an S3 role over current children; the operator is treated as a parent only where a first-party function-specific return path is separately evidenced.
- Reviewed revision: 2828e253852a98cace95dc404caf3ac8a3e45bce.
- Observation date: 2026-10-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Neo ships a model-backed coding runtime whose ordinary turn loop presents first-party repository, shell, workflow, delegate, skill and task tools, executes selected actions, appends tool results and instruction epochs, and continues model decisions until termination. Durable sessions, permissions, plan/goal state, context compaction and provider adapters support that loop without replacing the model's task-specific coding discretion.

The multi-agent runtime can instantiate independent child AgentRuntime executions with Coder, Explorer, Planner and Reviewer profiles. Delegate and DelegateSwarm support foreground/background execution, live status snapshots, result retrieval, live follow-up messages, interruption/cancellation and resume. Child roles have tool ceilings and separate state/history; workflow-hosted children can additionally request shared or isolated worktrees.

Neo also ships ordinary built-in workflows through the same registry/host API available to saved user/project workflows. The large-refactor workflow creates mutation-capable coding slices in isolated worktrees and keeps merge/retirement explicit. The code-review workflow dispatches separate read-only review domains and a challenge reviewer, producing structured findings. Workflow runs are durable background tasks and terminal transitions are queued as same-session notifications with TaskOutput as the canonical result path.

Project AGENTS.md files are first-party instruction authority. The resolver re-discovers applicable AGENTS.md files without caching a previous absence across calls, emits instruction epochs and re-pins authority after compaction. The shipped /init path asks the main model to create or update the root AGENTS.md with project identity, architecture, durable principles, practices and documentation guidance, then validates/repairs its structure.

## Operational model

A user starts a local coding turn. The main model receives the current project/session authority and available first-party tools, chooses repository-facing actions and may delegate specialist work or launch a workflow. Tool/delegate/workflow results return through the session/task surfaces. Background child state can be inspected and changed while work is active. Project instructions are versioned by content and re-enter later model requests as instruction authority.

The assessed multi-agent functions are credited only where a concrete organizational disturbance and closure are present. Generic queues, mailboxes, workflow edges, task lists and permissions are treated as mechanisms unless a function-specific decision/feedback loop is reconstructed below.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected project through open-ended model/tool action, including repository inspection, coding, shell/tool execution and task-specific response to returned evidence.
- Disturbance / variety regulated: heterogeneous source trees, incomplete requirements, implementation alternatives, changing workspace state, tool/build/test failures, provider responses, permissions, project instructions and local execution results encountered while completing coding outcomes.
- Decisive decision or feedback right: choose what project evidence to inspect, which offered coding/tool action to invoke, what implementation change or command to attempt, how to react to tool/environment results and when the assigned coding outcome is ready.
- Decision owner: the model-backed Neo main agent for ordinary work and each separately instantiated model-backed coding child for its delegated operational outcome.
- Supporting / enforcement mechanisms: tool registry, permission layer, project instruction engine, provider adapters, session/context state, process supervision, worktree binding, role tool ceilings, context compaction, cancellation and task/workflow persistence.
- Closure path: task plus project/session state enters a model-backed agent → the agent chooses a repository/tool action → Neo executes or rejects it → environment/tool result returns into that agent context → the agent revises the next action until a terminal outcome.
- Boundary reachability: interactive and headless Neo execution directly instantiate the first-party model/tool runtime; Delegate, DelegateSwarm and workflow child execution instantiate the same first-party child runtime without adopter-authored agent loops.
- Why this is / is not agent-owned: removing the model-backed actor while retaining tools, permissions, journals and schedulers removes the open-ended task-specific coding judgment that chooses and revises operations.
- Evidence: [README.md](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/README.md); [turn_loop.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/runtime/turn_loop.rs); [delegate.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/delegate.rs); [runtime.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/multi_agent/runtime.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model inference remains external; the assessment credits Neo's first-party role/tool/feedback composition and not provider internals.

## S2 — Coordination

- State: C
- Function: attenuate destructive workspace interference among distinct mutation-capable child S1 cells by assigning independent Git worktree execution roots before those cells act.
- Disturbance / variety regulated: two independently executing coding children working from the same checkout can overwrite or observe one another's in-progress changes, couple through stale workspace assumptions and lose clean ownership of separate change slices.
- Distinct S1 units: workflow-hosted coder children are separately instantiated model-backed AgentRuntime units with their own lifecycle, task/context and tool execution.
- Inter-S1 disturbance: mutation-capable slices of one refactor can otherwise interfere through a shared checkout even when each slice is locally reasonable.
- Attenuating coordination relation: workflow child plans expose ChildWorktreePolicy::Isolated; resolve_child_worktree creates a dedicated detached Git worktree before child start; the shipped large-refactor workflow explicitly requests isolated worktrees for its mutation slices and never auto-merges or deletes them.
- Feedback into subsequent S1 behaviour: the resolved isolation changes the actual workspace root supplied to each child before execution, so later reads/writes occur in distinct checkouts; merge/retirement remains an explicit later decision instead of allowing concurrent slices to destructively share one mutable root.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to a concrete shared-workspace mutation conflict and the first-party worktree separation specifically intended to attenuate that conflict. Delegate mailboxes, queues and lifecycle state are not independently used as S2 evidence.
- Decisive decision or feedback right: bind a mutation-capable operational child to an isolated worktree rather than the shared parent workspace when constructing the multi-child workflow.
- Decision owner: constructor-level workflow definition/authoring selects the isolation policy; the runtime deterministically resolves and enforces it. No shipped autonomous coordinator is evidenced as semantically deciding, from observed collision risk, which concrete child pair must be isolated.
- Supporting / enforcement mechanisms: ChildPlan and ChildWorktreePolicy; workflow child isolation resolver; WorktreeManager; typed child workspace binding; worktree provenance; explicit cleanup semantics and no-auto-merge rule.
- Closure path: a first-party workflow child definition selects isolated worktree policy → Neo resolves and creates the dedicated worktree before child start → the child model/tool loop runs against that isolated workspace root → subsequent child file actions remain separated from other mutation cells → later merge/retirement decisions operate on preserved isolated results.
- Boundary reachability: worktree is an explicit first-party neo.delegate/workflow child policy, and large-refactor is a shipped built-in ordinary workflow registry definition reachable through the standard Workflow tool. User/project workflows can use the same host API without inventing a separate isolation mechanism.
- Why this is / is not agent-owned: removing the model's task discretion leaves the same definition-selected isolation relation available and enforced. The positive path is therefore constructor-owned C rather than autonomous A.
- Evidence: [lineage.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/lineage.rs); [worktree.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/worktree.rs); [large-refactor.lua](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/large-refactor.lua); [large-refactor.workflow.toml](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/large-refactor.workflow.toml).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary DelegateSwarm children default to a shared workspace, so the positive state is intentionally limited to the first-party workflow constructor path that explicitly selects isolated worktrees.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain a current whole-fleet view of active delegated/workflow operations and regulate present commitments through live guidance, resume/reallocation, pause/resume and interruption/cancellation.
- Disturbance / variety regulated: several delegate agents, swarms and workflows can be queued, running, completed, failed, cancelled or timed out; current progress can make a commitment stale, blocked, misdirected or no longer worth consuming capacity.
- Whole-system current view: the model-facing ListDelegates path exposes point-in-time agent/swarm state and aggregate queued/running/completed/failed/cancelled/timed-out counts; TaskList/TaskOutput expose workflow/background state. The operator /tasks browser projects the same current task/workflow population with current phase/children/progress.
- Current-control decision scope: create/resume delegated capacity, inspect active workers, send live corrective messages, interrupt an agent or whole swarm, and in the parent mode pause/resume/stop workflows or answer a workflow's pending current-control question from the task browser.
- Decisive decision or feedback right: decide, from the current fleet state, which active commitments should continue unchanged, receive new guidance, resume, pause or terminate.
- Decision owner: Base A mode — the main model-backed Neo agent through ListDelegates, MessageDelegate, InterruptDelegate, Delegate resume and task/result surfaces. Parent P mode — the human operator through the first-party /tasks task browser for workflow pause/resume/stop and pending workflow answers.
- Supporting / enforcement mechanisms: MultiAgentRuntime lifecycle registry, swarm aggregates, background-task manager, cancellation tokens, TaskList/TaskOutput, workflow operator projections, task-browser rendering/refresh and actor-tagged pause/resume/stop methods.
- Closure path: current agent/swarm/workflow state is projected to the current-control owner → owner chooses guidance/resume/pause/stop/cancel action → Neo runtime applies the intervention to active commitments → subsequent child/workflow operation proceeds under the changed state and is visible in later snapshots.
- Boundary reachability: all base control tools are shipped in the ordinary model-facing runtime. /tasks is a shipped interactive surface that calls BackgroundTaskManager pause_workflow, resume_workflow and stop_with_actor with WorkflowActor::Human; no adopter-written supervisor is required.
- Why this is / is not agent-owned: lifecycle registries and cancellation tokens only expose/enforce decisions. In the autonomous mode, removing the main model removes the semantic choice of which current worker to redirect, resume or interrupt. In the parent mode, the operator explicitly owns the same class of current-control intervention through the task browser.
- Evidence: [delegate_controls.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/delegate_controls.rs); [delegate.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/delegate.rs); [background_tasks.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/background_tasks.rs); [interactive/input.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent/src/modes/interactive/input.rs); [task_browser.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent/src/modes/task_browser.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: hard concurrency/resource ceilings and scheduler state are treated as enforcement, not autonomous ownership. The parent-mode claim relies on the whole-task/workflow task browser plus actor-tagged control path, not on a generic emergency kill switch in isolation.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (A) | main model-backed Neo agent | current delegate/swarm/task state reveals need for redirection, continuation or cancellation | inspect fleet → choose message/resume/interrupt/current-task action → runtime applies it → later child/workflow state reflects the intervention | delegate_controls.rs, delegate.rs, background_tasks.rs |
| Parent (P) | human operator | operator opens /tasks and decides a current workflow commitment should pause, resume, stop or answer pending input | task browser projects current workflow/children → operator chooses control → BackgroundTaskManager records WorkflowActor::Human and changes run state → subsequent operation follows returned state | interactive/input.rs, task_browser.rs, background_tasks.rs |

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation claims through separate read-only review agents that inspect repository reality across multiple review domains and return structured findings into later current control.
- Disturbance / variety regulated: an implementing coding agent can report completion while code contains correctness, security, maintainability or test-coverage defects that its own operational path missed.
- Claim being audited: the reviewed code/scope is correct and sufficiently safe/maintainable/tested, rather than merely that the implementing S1 reported success.
- Ordinary reporting path: implementation results and any tests/checks selected by the implementing main/coder agent return through its normal model/tool or delegate result path.
- Complementary access path: the shipped code-review workflow dispatches separate security, correctness and maintainability/test-gap agents with read-only tool ceilings, then dispatches a further reviewer to challenge weak findings; those agents inspect repository files through their own child contexts and return structured findings.
- Independence boundary: review children are separately instantiated model-backed agents with dedicated Reviewer/Explorer profiles and no Write/Edit/Bash/Terminal mutation tools in the credited workflow. Their evidence path is distinct from the implementation agent's own transcript and self-verification, while still using the same project workspace.
- Who acts on findings: the main model-backed agent that launched/owns the workflow receives the terminal workflow notification in the same durable session, can retrieve the canonical result with TaskOutput, and can then modify code, redirect/resume delegates or launch corrective work.
- Decisive decision or feedback right: make the semantic audit judgment about security/correctness/maintainability/test gaps from complementary read-only repository evidence.
- Decision owner: the model-backed review/challenge child agents; deterministic workflow code aggregates and deduplicates their structured output without owning the semantic review judgment.
- Supporting / enforcement mechanisms: built-in code-review workflow and manifest; Reviewer/Explorer role profiles; read-only tool ceilings; workflow child schemas; durable workflow journal/result projection; notification queue and TaskOutput.
- Closure path: main agent invokes shipped code-review → independent read-only reviewer agents inspect the target scope and produce findings → workflow aggregates a terminal structured result → same-session terminal notification directs the main agent to TaskOutput → findings re-enter current control and can cause corrective coding/delegation before later acceptance.
- Boundary reachability: code-review is a shipped built-in ordinary workflow registry definition reachable through the standard model-facing Workflow run_saved path. It uses the same public Lua host API as other supported workflows and requires no adopter-authored reviewer implementation.
- Why this is / is not agent-owned: removing the reviewer models leaves workflow schemas and deterministic aggregation but removes the semantic judgment about whether arbitrary code contains the cited defects. The positive state relies on separate reviewer contexts/read-only access and returned findings, not the name code-review by itself.
- Evidence: [code-review.lua](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/code-review.lua); [code-review.workflow.toml](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/code-review.workflow.toml); [builtins/mod.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/mod.rs); [workflow.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/workflow.rs); [queue.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/runtime/queue.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: review is an optional agent/workflow-chosen path rather than a mandatory acceptance gate for every code change. Workflow completion notification does not embed the findings themselves; it durably returns the result handle and canonical TaskOutput path for the next model turn.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then loop was established that senses external/future-relevant change, develops adaptation options and returns a selected option into Neo's present organizational capability.
- Disturbance / variety regulated: Neo exposes research, saved workflows, skills, history/session state, goals/plans, provider/tool integrations and a self-evo skill, but those mechanisms either support the current task, preserve history or require an explicit user-selected evidence scope rather than autonomously model a changing future environment.
- Decisive decision or feedback right: none established for a qualifying prospective organizational adaptation function.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: built-in deep-research workflow; self-evo skill; CreateSkill and skill-store reload; Workflow save/run surfaces; goal/plan state; MCP/provider configuration; durable sessions and context compaction.
- Closure path: not applicable; no external/future distinction → adaptation option → persistent capability change → return into present S3/capability loop was found in the supported standard distribution.
- Why this is / is not agent-owned: self-evo explicitly distills an operator-selected history scope into reusable skills, while deep-research answers a current question using bounded local read-only children. Saved workflows/skills can persist capability, but the inspected runtime does not supply the prospective environmental sensing and adaptation decision loop that would make those writes S4.
- Evidence: [self-evo.md](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/skills/builtin/self-evo.md); [deep-research.lua](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/workflow/builtins/deep-research.lua); [skills_manager.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/skills_manager.rs); [workflow.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/tools/workflow.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user can intentionally use Neo's composable workflows/skills to build an adaptation process, but generic composability or current-task research does not donate S4 to the frozen standard distribution.

### Absence scope

- Surfaces inspected: built-in self-evo skill; built-in deep-research workflow; skill creation/reload; saved/user/project workflows; goal/plan state; durable sessions/history/context compaction; provider/MCP configuration; multi-agent/workflow runtime.
- Plausible first-party paths checked: self-evo as organizational learning; deep-research as environmental intelligence; model-authored saved workflows as adaptation; provider/tool changes as capability evolution; goals/plans as future strategy; session history as learning.
- Why no material first-party path remains: the located persistence surfaces can store skills/workflows/instructions, but no shipped loop ties external/prospective distinctions to an adaptation choice and then returns that choice into current capability/S3. The explicit self-evo path is history-scoped and user-triggered rather than outside-and-then.

## S5 — Policy and identity

- State: A(P)
- Function: establish and preserve the durable project-level identity, principles and standing operating instructions that govern later Neo coding agents in the workspace.
- Disturbance / variety regulated: missing, stale or inconsistent project identity and durable working principles can cause later agents to make incompatible assumptions about architecture, documentation, boundaries, conventions and what project rules should remain stable.
- Identity / ultimate-policy issue: what project identity, durable principles, architecture assumptions, working practices and standing boundaries should govern later AI collaborators at the selected project recursion.
- Ultimate authority in each claimed mode: Base A — the model-backed main agent executing the shipped /init workflow synthesizes and writes the authoritative project AGENTS.md from repository evidence and user-supplied context. Parent P — the legitimate project owner can directly author/edit the same AGENTS.md authority, and /init guidance explicitly treats durable project principles as requiring explicit user approval to change.
- Return-to-operation path: AGENTS.md persists in the project; the instruction resolver discovers applicable root/nested scopes without caching prior absence, produces instruction epochs, and the runtime injects/re-pins the resulting authority into subsequent model requests, including after compaction.
- Decisive decision or feedback right: decide the semantic content of the durable project AGENTS.md layer that later Neo model turns receive as standing project authority.
- Decision owner: Base A mode — the main model-backed agent during shipped /init authoring/repair. Parent P mode — the legitimate project owner/editor when directly deciding or changing the same project-level instruction layer.
- Supporting / enforcement mechanisms: /init system-reminder workflow; AGENTS.md structure validation/repair; instruction resolver and scope discovery; content-addressed instruction bundles; instruction epochs; preflight/reconciliation after tool execution; rehydration after compaction.
- Closure path: project identity/policy gap or change → model-driven /init synthesis or legitimate owner edit → root AGENTS.md persists → instruction resolver observes the authoritative revision → instruction epoch enters the session/model context → later coding work is governed by the returned standing layer.
- Boundary reachability: /init is a shipped interactive Neo surface that starts a normal model turn and repairs the resulting root AGENTS.md when needed. The ordinary instruction registry/resolver consumes AGENTS.md on supported project turns, and newly created instruction files are discovered before later tool/model batches.
- Why this is / is not agent-owned: triggering /init does not predetermine the file's project-specific semantic content; the main model researches the workspace and chooses the synthesized identity/principles within higher-level user/Neo constraints. In the parent mode, the project owner directly owns the authoritative edit. Deterministic validation and instruction injection only enforce/transport the selected policy.
- Evidence: [init_command.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent/src/modes/interactive/init_command.rs); [interactive/mod.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent/src/modes/interactive/mod.rs); [resolver.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/instructions/resolver.rs); [instruction_context.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/runtime/instruction_context.rs); [turn_loop.rs](https://github.com/matrixheaven/neo/blob/2828e253852a98cace95dc404caf3ac8a3e45bce/crates/neo-agent-core/src/runtime/turn_loop.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is project-recursion S5. It does not claim the model can rewrite Neo's higher-level application safety model, permission semantics or operator authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (A) | model-backed main Neo agent | user invokes shipped /init for a project instruction gap/update | inspect repository/user context → synthesize and write root AGENTS.md → resolver admits its revision → later model requests receive the durable project authority | init_command.rs, interactive/mod.rs, resolver.rs, instruction_context.rs |
| Parent (P) | legitimate project owner/editor | owner directly creates/edits project AGENTS.md or supplies an explicit authoritative project-policy change | owner changes durable project authority → resolver detects the revision → instruction epoch is injected/re-pinned → subsequent coding behavior follows returned policy | resolver.rs, instruction_context.rs, turn_loop.rs |

## Distributed OSS parent arrangement

Neo's GitHub maintainers govern the Neo software project, but that repository-development governance is outside one local project/session organization assessed here. Parent-mode credit is limited to first-party runtime paths through which the local project operator/owner regulates the current session organization or its durable project instruction authority.

## Self-hosted and non-human modes

The autonomous S1, S3, S3* and project-level S5 base modes do not require continuous human decision-making after their initiating task/trigger and configured authority. S2 remains constructor-owned because isolation policy is definition-selected. The operator has separately credited parent modes only for S3 current-control and S5 project-policy closure; ordinary permission prompts are not promoted to S3/S5 by themselves.

## Recursion

At the chosen project/session recursion, model-backed coding children are S1 cells when they directly produce repository outcomes. Isolated worktree binding supplies an S2 constructor path between mutation cells. The main model can occupy S3 over current delegates/workflows, while review children provide complementary S3* access. The project AGENTS.md authority supplies S5 at the same project recursion. Lower-level tool/process activity and higher-level Neo OSS governance are not promoted into this vector.

## Variety and escalation

Operational coding variety is absorbed locally by S1 agents. Isolated worktrees attenuate mutation interference where selected. Current agent/swarm/workflow state can escalate to the main model for live redirection/interruption or to the operator through /tasks. Complementary review findings return via durable workflow results. Project-level standing-rule changes return through instruction epochs. No external-and-prospective S4 adaptation channel is established.

## Evidence gaps

No reviewed evidence gap requires ?. The positive claims are tied to shipped runtime surfaces and explicit closure paths; the S4 negative conclusion is supported by review of the plausible learning/research/persistence surfaces rather than by absence of a component name.

## Assessment summary

Neo closes autonomous coding S1; exposes constructor S2 through definition-selected isolated worktrees that attenuate concrete cross-child mutation interference; closes autonomous-plus-parent S3 through model-facing live fleet control and the operator /tasks control plane; closes autonomous complementary S3* through the shipped multi-domain read-only code-review workflow; does not establish outside-and-then S4; and closes autonomous-plus-parent project-recursion S5 through model-authored or owner-edited durable AGENTS.md authority that is injected into later model requests.

Proposed vector: **A · C · A(P) · A · — · A(P)**.
