---
harness_id: doompi
project_name: DoomPi
repository: https://github.com/AgiFlow/doompi
review_ref: c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DoomPi

## Review boundary

- System in focus: Installed DoomPi composable Pi-based coding-agent distribution and the shipped, selectable first-party Team/Task/Plan/runtime packages.
- Purpose and identity: Run a model-driven coding agent with explicitly chosen capabilities, optional bounded multi-agent delegation and persistent task/workflow execution.
- Relevant environment: User workspace, selected agent/model provider, task and tool results, repo-scoped configuration, optional user-created extension packages, TUI/web/desktop clients and headless server.
- Standard-distribution boundary: The published `@agimon-ai/doompi` host with native headless direct-harness execution, pinned Pi interactive integration, default/foundation packages, and selectable first-party mode/layer packages that the host can synchronize and activate.
- Credited operating / distribution surfaces: Interactive Pi agent runtime under DoomPi configuration; native headless DirectHarnessRuntime; optional shipped Team/Task child controls and current fleet views; Plan mode workflow; configured tool, permission and compositional lifecycle.
- Adjacent first-party surfaces excluded from ownership: Unselected custom plugins, maintainer scripts, architecture design proposals, standalone user-authored workflows and arbitrary third-party MCP servers; upstream Pi considered only as the packaged interactive execution dependency, not a separate DoomPi-authored S3/S4/S5 function.
- First-party operating / deployment modes considered: Interactive `doompi`/`dpi` with selected modes, headless direct-host sessions, optional Team and Task layer composition, local and client-neutral server interaction.
- Recursion level: One owning agent session and its currently registered, session-scoped subagent/team-run and task portfolio.
- Reviewed revision: `c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

DoomPi compiles repository/home YAML selection into a pinned package composition and immutable generation. The interactive path loads Pi extension factories and executes Pi's coding agent; the native headless path uses its own `DirectHarnessRuntime` with model requests, tool registration/execution and durable session state. First-party selectable Team packages launch subagents, expose model-visible status/steer/stop/restore controls and track current runs. Task maintains a durable dependency graph; optional workflows run explicitly ordered sessions. An interactive fleet overlay and web run panel expose the same live child portfolio to the operator with explicit stop and steering routes. The runtime and modes supply real operating paths beyond mere configuration, but mode selection, task ordering, intercom transport, static isolation, plan review and composition fingerprints must not be inflated into positive VSM functions without a decisive decision/feedback right. [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L1-L58), [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L103-L175), [`packages/core/doompi-core/src/server/directHarnessRuntime.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/packages/core/doompi-core/src/server/directHarnessRuntime.ts#L153-L320), [`docs/features.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/features.md#L78-L107), [`docs/automation.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/automation.md#L1-L51).

## Operational model

The coding model completes user work through available tools. In a shipped Team-enabled mode, the owning model may view and change current child-run commitments. In a separate parent-governed interactive mode, the human sees the fleet and can stop or steer specific current runs; both paths act through concrete Team management services. A task graph enforces authored dependency ordering, and optional planner children generate candidate plans for root synthesis. These mechanisms do not by themselves establish cross-child conflict-specific attenuation, independently audited completed work, future capability selection from the outside environment or constitutive governance.

## S1 — Operations

- State: A
- Function: Perform coding and workspace work using model-selected actions.
- Disturbance / variety regulated: Different repository tasks, observed code/tool outcomes and selected operating capabilities.
- Decisive decision or feedback right: Choose tools or delegated task actions and continue work from resulting feedback until completion.
- Decision owner: Configured coding model in an interactive Pi session or native headless agent session.
- Supporting / enforcement mechanisms: Packaged Pi runtime with DoomPi extension composition, native `DirectHarnessRuntime`, session state, provider and tool interfaces.
- Closure path: The session model requests tools, receives their results and selects subsequent actions, producing an answer or changed repository artifacts.
- Why this is / is not agent-owned: Model choice drives operations; composition code and tool dispatch enforce selected facilities but do not themselves make discretionary task decisions.
- Evidence: [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L1-L28), [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L159-L175), [`packages/core/doompi-core/src/server/directHarnessRuntime.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/packages/core/doompi-core/src/server/directHarnessRuntime.ts#L153-L320), [`README.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/README.md#L90-L157).
- Basis: structural
- Confidence: High
- Caveats: Interactive Pi is a pinned runtime dependency; assessment credits the shipped deployment and first-party extensions rather than claiming DoomPi independently authors every upstream Pi tool.
- Boundary reachability: The installed CLI launches the pinned interactive runtime, while the supported server constructs a direct headless session; neither path depends on a custom user-created agent.

## S2 — Coordination

- State: —
- Function: Resolve interference among distinct operational child agents in their shared task environment.
- Disturbance / variety regulated: Child agents may modify overlapping files, depend on another task's output or send competing requests.
- Decisive decision or feedback right: No shipped inter-S1 interference-specific attenuating choice and closed corrective return was established.
- Decision owner: Root/model or workflow author selects job/dependency relations; Team intercom transports messages; Task graph and file locks enforce deterministic consistency.
- Supporting / enforcement mechanisms: Team intercom, model-visible subagent controls, durable Task graph, task-store advisory lock, explicit workflow `needs` and optional workspaces.
- Closure path: Submitted messages and authored dependencies route or defer work; mutex/provenance mechanisms protect shared task state. A first-party conflict detection → coordination decision → changed peer behavior loop was not found.
- Why this is / is not agent-owned: Generic communication, authored sequencing and file-store locking alone do not establish disturbance-specific S2 coordination, even when several agents are active.
- Evidence: [`docs/features.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/features.md#L87-L107), [`docs/automation.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/automation.md#L1-L52), [`layers/task/doompi-task/src/services/taskStore/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/task/doompi-task/src/services/taskStore/index.ts#L62-L90), [`layers/task/doompi-task/src/services/taskStore/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/task/doompi-task/src/services/taskStore/index.ts#L190-L229), [`layers/team/doompi-team/src/services/teamCollaboration/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/teamCollaboration/index.ts#L52-L82).
- Basis: structural
- Confidence: Medium
- Caveats: A bespoke workflow/agent-team prompt can detect a collision and coordinate a specific response; not credited as bundled first-party S2 closure.

### Absence scope

- Surfaces inspected: Team intercom, native run coordinator, collaboration services, Task dependency graph/store and reconciliation, workflow `needs`, mode isolation and shared-state locks.
- Plausible first-party paths checked: Child direct messages, shared task ordering, task-store critical sections, dependency-aware launch, run cancellation and optional independent worktrees.
- Why no material first-party path remains: The examined paths are generic transport, authored dependencies or persistence safety. They do not themselves select an S2-specific response after observing interference between distinct live S1 units and verify its corrective effect on both units.

## S3 — Inside-and-now control

- State: A(P)
- Function: Maintain and modify the active subagent-run/commitment portfolio in a Team-enabled session.
- Disturbance / variety regulated: A child run stalls, requires redirection, consumes resources after becoming obsolete or can no longer execute the requested work.
- Decisive decision or feedback right: Inspect the session's current run roster, select a specific run, steer supported Pi children, request stop/interrupt, or restore supported suspended work; a human can inspect and intervene through shipped fleet controls.
- Decision owner: Base autonomous mode: root model invoking `subagent` management actions. Parent mode: authenticated local operator using the TUI fleet overlay or web session controls.
- Supporting / enforcement mechanisms: `SubagentToolService` status/steer/stop actions, `ManagementActions`, `AsyncJobTracker`, fleet projections, interactive stop/steer commands and web subagent run actions.
- Closure path: A model- or operator-selected control calls the session-scoped Team management layer, issues a run-specific interruption or steer and returns request status; the child runtime handles the requested subsequent change.
- Why this is / is not agent-owned: Model decides which current child commitment to redirect or stop after consulting the live roster. The separately credited parent operator can make an equivalent session-scoped decision; neither is inferred from deterministic capacity limits alone.
- Evidence: [`layers/team/doompi-team/src/services/subagentTool/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/subagentTool/index.ts#L327-L420), [`layers/team/doompi-team/src/services/managementActions/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/managementActions/index.ts#L20-L115), [`layers/team/doompi-team/src/services/statusViews/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/statusViews/index.ts#L1-L100), [`layers/team/doompi-team/src/extensions/workspaces/sessions/(backend)/command/_lib/subagents-fleet.cli.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/extensions/workspaces/sessions/(backend)/command/_lib/subagents-fleet.cli.ts#L50-L95), [`layers/team/doompi-team/src/extensions/workspaces/sessions/(frontend)/_lib/subagentsStore.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/extensions/workspaces/sessions/(frontend)/_lib/subagentsStore.ts#L45-L77), [`docs/features.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/features.md#L86-L102).
- Basis: structural
- Confidence: High
- Caveats: This is the root session's Team-enabled fleet, not cross-repository governance. Steering explicitly rejects unsupported child backends; a stop *request* is not misrepresented as immediate confirmed termination.
- Boundary reachability: Team is a shipped selectable first-party layer, and its model-facing `subagent` management tool plus operator fleet commands are mounted into supported session modes.
- Whole-system current view: The root receives the current tracked-run fleet, activity, statuses and optional bounded transcripts. The operator's fleet overlays show the same session scope and can open individual runs.
- Current-control decision scope: Select which presently active child run to stop, interrupt or steer; a restored/continued run is contingent on its supported runtime and recorded state.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root model | Child status or result requires current change | `subagent` status → selected `steer` / `stop` → run management request and returned state | [`layers/team/doompi-team/src/services/subagentTool/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/subagentTool/index.ts#L327-L420) |
| Parent (`P`) | Operator within the owning session | Fleet overlay shows stalled or obsolete run | UI/command selection → authenticated run-specific stop/steer call | [`layers/team/doompi-team/src/extensions/workspaces/sessions/(backend)/command/_lib/subagents-fleet.cli.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/extensions/workspaces/sessions/(backend)/command/_lib/subagents-fleet.cli.ts#L50-L95), [`layers/team/doompi-team/src/extensions/workspaces/sessions/(frontend)/_lib/subagentsStore.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/extensions/workspaces/sessions/(frontend)/_lib/subagentsStore.ts#L45-L77) |

## S3* — Complementary audit

- State: —
- Function: Independently challenge operational output with direct complementary evidence and return a corrective verdict to current S3.
- Disturbance / variety regulated: A child may produce an incorrect implementation or an implausible plan.
- Decisive decision or feedback right: No bundled separate audit owner is shown selecting evidence and returning a corrective verdict about a completed S1 operational result into current portfolio control.
- Decision owner: The root model can compare optional planning drafts or ask other agents for reports; the user approves implementation plans.
- Supporting / enforcement mechanisms: Plan prompt with multiple delegated drafts and root comparison, subagent transcripts, plan approval and ordinary tool/unit test execution.
- Closure path: A plan can be revised before approval, but the supplied mechanism does not independently adjudicate an operational outcome with corrective return to an S3 controller.
- Why this is / is not agent-owned: Multiple drafts and root synthesis are planning/delegation. Human plan acceptance is task authorization, not a separate first-party S3* audit protocol with complementary direct evidence.
- Evidence: [`packages/minor/doompi-plan/src/services/prompts/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/packages/minor/doompi-plan/src/services/prompts/index.ts#L70-L100), [`packages/minor/doompi-plan/src/prompts/doompi-use-plan/SKILL.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/packages/minor/doompi-plan/src/prompts/doompi-use-plan/SKILL.md#L13-L34), [`layers/team/doompi-team/src/services/statusViews/index.ts`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/layers/team/doompi-team/src/services/statusViews/index.ts#L75-L110).
- Basis: structural
- Confidence: Medium
- Caveats: Users may select an auditor agent or write a verification workflow, but those compositions require their own separate evidence.

### Absence scope

- Surfaces inspected: Team task execution and transcript views, Plan mode's delegated draft comparisons, task graph, shared tool results, optional test hooks and user review.
- Plausible first-party paths checked: Multiple planner agents, root cross-checking their plans, human acceptance/revision, generic reviewer role and workflow-gated tests.
- Why no material first-party path remains: None established a first-party independent audit verdict on an S1 completed artifact grounded in direct complementary evidence and formally returned to select rework or acceptance through S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: Detect outside change and select a future operating-capability alternative with operational return.
- Disturbance / variety regulated: Different task domains and evolving external provider/tool capabilities could alter what should run in later sessions.
- Decisive decision or feedback right: No evidence-based future capability strategy is autonomously or parent-governedly chosen from external-environment intelligence by the shipped runtime.
- Decision owner: Operator chooses YAML major modes, package layers and profiles; the selected composition and immutable fingerprint enforce that choice.
- Supporting / enforcement mechanisms: Configuration resolver, immutable sync generation, dynamic selected package activation, skills, optional reminders/workflows.
- Closure path: Explicit configuration selections change available later capabilities. The first-party path does not use its own outside assessment to select such a change and close a prospective feedback loop.
- Why this is / is not agent-owned: Configuration composition and tactical tool discovery are not outside-and-then intelligence merely because they permit later changes.
- Evidence: [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L1-L58), [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L60-L132), [`docs/features.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/features.md#L10-L35), [`docs/automation.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/automation.md#L1-L35).
- Basis: structural
- Confidence: Medium
- Caveats: A user-authored external monitoring workflow or strategic extension can create a separate prospective loop.

### Absence scope

- Surfaces inspected: Home/repo mode selection, profile/layer composition, registry fingerprints, synchronization, versioned artifact admission, headless sessions and optional workflows.
- Plausible first-party paths checked: Manual mode swaps, dynamic feature installation, dependency graph, recurrent task scheduling, capability config and server session reinstatement.
- Why no material first-party path remains: All credible bundled paths implement preselected composition or current tasks, not a first-party decision coupling prospective external observation to a choice changing future system capability.

## S5 — Policy and identity

- State: —
- Function: Resolve standing identity or ultimate governing policy and return a binding authority decision.
- Disturbance / variety regulated: Package selections, tool permissions, session scopes and plan approvals can differ by workspace and operator.
- Decisive decision or feedback right: No shipped higher-level identity/policy issue is escalated, adjudicated and returned as constitutive governance for future operations.
- Decision owner: Operator edits configuration and approves plans; runtime validates and enforces modes, provenance, authenticating session rights and sandbox restrictions.
- Supporting / enforcement mechanisms: Plan approval, selection policy and trusted generation, scoped APIs, sandbox, fail-closed versioned artifact checks.
- Closure path: Policy gates stop unauthorized actions and permit selected configurations; a parent can approve a concrete plan but this does not settle a standing constitutive policy dispute.
- Why this is / is not agent-owned: Security boundaries and task-specific approval are application policy, not evidence of an independent identity-governance loop.
- Evidence: [`docs/architecture.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/architecture.md#L115-L175), [`packages/minor/doompi-plan/src/prompts/doompi-use-plan/SKILL.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/packages/minor/doompi-plan/src/prompts/doompi-use-plan/SKILL.md#L23-L35), [`docs/features.md`](https://github.com/AgiFlow/doompi/blob/c3f057ab58a94667fb6f5c1e94c5a31e43bf84cf/docs/features.md#L16-L35).
- Basis: structural
- Confidence: Medium-high
- Caveats: Repository maintainer governance and user-authored policies lie outside this assessed agent runtime recursion.

### Absence scope

- Surfaces inspected: Selection and artifact admission, operator config, plan approval, sandbox and authenticated session controls, Team capability policy.
- Plausible first-party paths checked: Changing a major mode, approving a proposed implementation plan, controlling a delegated child and enforcing constraints on a tool.
- Why no material first-party path remains: All returned decisions are current task permissions or operator-selected configuration, without a standing S5 issue → legitimate policy decider → identity-level determination → subsequent organization feedback path.

## Recursion

The interactive and headless host maintains independent root sessions. A Team-enabled root can launch and observe child sessions and control their current commitments, but the per-session team fleet is the explicitly credited S3 boundary; the mere presence of nested contexts is not itself a further complete recursive viable organization.

## Variety and escalation

Model and first-party tools absorb code task variability. Explicit mode/layer selection reduces presented capabilities; task dependencies and child runtime tracking constrain parallel work. Root-model and parent-operator fleet actions change current obligations. Plan approvals and runtime security boundaries do not imply additional S5 authority.

## Evidence gaps

Frozen source review only, no live API-provider run, custom extension execution or independent semantic evaluator. The interactive Pi model loop is a pinned shipped dependency; native headless execution is first-party. S3 positive claims the shipped optional Team mode and concrete model-/operator-facing fleet controls. S2, S3*, S4 and S5 negatives are bounded to source-supported first-party paths, not a denial that users could construct them.
