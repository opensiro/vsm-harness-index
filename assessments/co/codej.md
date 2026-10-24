---
harness_id: codej
project_name: CodeJ
repository: https://github.com/liumaishenjian/codej
review_ref: e51e6b5062fbab46881137342a2bff84bfc05645
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# CodeJ

## Review boundary

- System in focus: CodeJ's shipped Java coding-agent runtime, composed into its headless/print, CLI, and React/Ink TUI products at the frozen revision. Organizational recursion: one root coding Session supervising task-scoped child AgentRuntime sessions, with an optional approved-Plan mode. This is not an assessment of its open-source development team.
- Purpose and identity: act on a user's software-engineering objective by reading a workspace, editing code, running bounded tools, testing outcomes, and optionally delegating subtasks while the Java host enforces safety and lifecycle controls.
- Relevant environment: user instructions, repository state, tool and test results, model responses, child-session activity, contested task claims, permission decisions, workspace drift, and interrupted durable state.
- Standard-distribution boundary: the repository's core/domain/runtime, shipped local tools, CLI/headless composition, SDK/protocol, and TUI. External model providers, arbitrary MCP/plugin tools, operator inputs, and user-authored project instructions are dependencies, not first-party organizational decision owners.
- Credited operating / distribution surfaces: `cc-java-core` `AgentRuntime`, `subagent/AgentSupervisor` and `DelegateAgentTool`, `task/TaskListService` and Task tools, Plan final-response/evidence gates; `cc-java-cli` `HeadlessRuntimeSession`, `HeadlessChildRuntimeScopeFactory`, `StableProtocolHandler`, session stores; `cc-java-tools-local` workspace tools; and the shipped TUI.
- Adjacent first-party surfaces excluded from ownership: the repository `AGENTS.md`, G0–G6 stage gates and progress dashboard, its product/reference-roadmap research, release CI, offline agent-evaluation fixtures, and external authorization/source-study materials. These are development evidence or stated aspirations, not live S3*/S4/S5 controllers.
- Modes inspected: solo coding loop; root with bounded parallel/nested child agents and optional isolated Git worktrees; root/child shared task-board scopes; user-approved Plan with durable evidence and task-completion gates; permission modes including optional auto-approval classifier; session restore/checkpoint and TUI/SDK operator surfaces.
- Recursion level: a root Session and independently running, task-bounded child Sessions (default maximum depth two); no fully demonstrated child metasystem of its own.
- Reviewed revision: `e51e6b5062fbab46881137342a2bff84bfc05645`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The Java `AgentRuntime` handles model turns, tool proposals, tool-result feedback, limits, and final outcomes; the Spring AI module adapts providers rather than owning the loop. Headless composition registers coding tools and durable Task tools, then registers `delegate_agent` when an `AgentSupervisor` is available. Delegated child work runs a separate instance of the existing runtime with its own Session, permission context and bounded tools; the supervisor shares a per-root queue, ledger and terminal reporting channel. A top-level delegation can also explicitly share a narrowed subset of the root's Task Board. The host, rather than the LLM, gives each child its actor identity and hard task scope.

The root-owned Task Board stores dependencies, assignees, claims, revisions, current status and conflict diagnostics. Mutations use synchronized compare-and-swap, actor/capability checks, claim epochs and durable events. Model-visible `task_create`, `task_update`, `task_list`, and `task_get` permit the root or scoped children to use those facts to choose and adjust work. This is separate from the supervisor's deterministic admission limit, which by itself would be only a resource queue.

In an approved Plan, a first-party final-response controller independently rechecks the recorded workspace-file digest and/or successful tool-result evidence, and checks the current Plan Task cohort. A superficially successful model final response cannot satisfy an unmet requirement: bounded correction turns are requested, then the Run exits with `PLAN_VERIFICATION_REQUIRED` and the durable Plan remains `NEEDS_VERIFICATION`. This is a narrow, host-configured complementary check, not a general-purpose autonomous audit investigator.

Primary pinned source entry points:

- [`README.md`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/README.md) and [`docs/technical-design.md`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/docs/technical-design.md).
- [`AgentRuntime.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/AgentRuntime.java) and [`HeadlessRuntimeSession.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/runtime/HeadlessRuntimeSession.java).
- [`AgentSupervisor.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/subagent/AgentSupervisor.java), [`TaskListService.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/task/TaskListService.java), and [`HeadlessChildRuntimeScopeFactory.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/subagent/HeadlessChildRuntimeScopeFactory.java).

## Operational model

A root model iteratively observes tool and workspace results, chooses code actions, tracks a task graph and may delegate parts of the work to independent child model loops. A shared, owner-scoped board prevents simultaneous claims and conflicting transitions, returning diagnoses to the invoking agent. The root can inspect/reassign live board work and issue further delegations; the operator can alternatively approve, resume or cancel a Plan through the supported client surface. In approved-Plan mode, an additional host-side check of concrete execution evidence can reject a model's proposed successful final response. No first-party prospective organizational strategy or identity-setting policy-return system is demonstrated.

## S1 — Operations

- State: A
- Function: execute and adapt coding, investigation, workspace modification, command/test, and correction work against a user's task.
- Disturbance / variety regulated: codebase uncertainty, differing file content, failing tool results, command errors, and changing user goals within the allowed session.
- Decisive decision or feedback right: select a subsequent coding/tool action after model turns and observed workspace/tool responses.
- Decision owner: the root model-backed AgentRuntime, and the separate child model-backed AgentRuntime for delegated subtasks.
- Supporting / enforcement mechanisms: Tool Pipeline, permission/approval/sandbox, provider adapter, session journal, context handling, and command/file tools.
- Closure path: user/child objective → model next action → pipeline workspace/command tool → returned evidence → subsequent model decision or terminal outcome.
- Boundary reachability: standard headless composition registers the first-party tools and owns an ordinary AgentRuntime; the same runtime is instantiated for children.
- Why this is / is not agent-owned: deterministic host tools cannot decide which code investigation or correction best pursues a task without a model-backed operational choice.
- Evidence: [`AgentRuntime.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/AgentRuntime.java); [`HeadlessRuntimeSession.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/runtime/HeadlessRuntimeSession.java); [`DelegateAgentTool.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/subagent/DelegateAgentTool.java).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: assessed by frozen first-party source and script/fake tests; no live LLM was invoked. The model's choices remain within the permission and execution policy.

## S2 — Coordination

- State: A
- Function: attenuate competing work claims and inconsistent task/dependency transitions among separately executing S1 child/root actors.
- Disturbance / variety regulated: two child agents attempting the same Task; stale owner/claim epochs; contradictory dependency and progress mutations; resuming an interrupted actor's claim.
- Distinct S1 units: a root coding AgentRuntime and up to four concurrent supervised child AgentRuntime instances, each with independent Sessions, model turns and bounded tool scopes.
- Inter-S1 disturbance: top-level children can share a root-owned Task Board over host-approved task IDs; competing claims, writes to the same task state and stale revisions can collide even where their coding worktrees are separate.
- Attenuating coordination relation: the board serializes mutation, enforces CAS/claim epochs, actor capabilities, dependency DAG and blocked-by checks; a contested claim is rejected with explicit diagnostics rather than accepted as two independent owners.
- Feedback into subsequent S1 behaviour: `task_update` and `task_list/get` return the current authoritative claim/status and conflict to the model, which can choose another task, change dependencies or defer work; successful mutation changes later agents' view.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the exclusive claims and dependency/conflict results regulate demonstrable collision between concurrently acting S1s; supervisor queue limits and worktree creation alone would not establish S2.
- Decisive decision or feedback right: resolve which task to claim or reassign after live competition feedback, with atomic admissibility enforced by the host.
- Decision owner: root/child model actors select work and react to conflicts; the Java Task Board owns deterministic acceptance/denial of mutations.
- Supporting / enforcement mechanisms: `TaskListService`, `TaskUpdateTool`, `ChildTaskBoardAccess`, `TaskBoardCapabilityFactory`, `AgentSupervisor`, per-child actor identity and durable Task events.
- Closure path: multiple S1s request overlapping claims → synchronized claim/CAS check → one success or conflict return → agents observe revised task state and adjust subsequent work.
- Boundary reachability: `HeadlessRuntimeSession.initializeTaskBoard()` exposes model Task tools; `childTaskBoardAccess()` and `HeadlessChildRuntimeScopeFactory` bind a top-level child to the same parent board and narrow allowed task IDs.
- Why this is / is not agent-owned: host CAS itself cannot decide the next meaningful work; model actors retain task-selection and recovery decisions in response to the returned coordination signal.
- Evidence: [`TaskListService.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/task/TaskListService.java); [`TaskUpdateTool.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/task/TaskUpdateTool.java); [`HeadlessRuntimeSession.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/runtime/HeadlessRuntimeSession.java); [`HeadlessChildTaskBoardCompositionTest.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/test/java/io/github/liumaishenjian/ccjava/cli/subagent/HeadlessChildTaskBoardCompositionTest.java).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: shared task scope is opt-in in a top-level delegation, and the Task Board does not provide cross-worktree semantic merge or universal file locks. In unscoped child runs, this S2 path may not be active.

## S3 — Inside-and-now control

- State: A(P)
- Function: observe and regulate the current root Session's task allocation, active progress, dependencies, child delegation and immediate execution exceptions.
- Disturbance / variety regulated: unbalanced/blocked task progress, unfinished Plan steps, stale ownership, failed children and changed execution outcomes requiring present-time reallocation.
- Whole-system current view: root-scoped `task_list/get` sees the root's canonical task graph and statuses; `AgentSupervisor` reports child terminal status, failures and summaries to its parent, while the TUI projects the same board state. This is the bounded current organization, not all unrelated CodeJ processes.
- Current-control decision scope: the root model creates tasks and dependencies, chooses delegates and task scopes, revises assignments/status, and can issue later corrective actions; approved-Plan execution couples those transitions to actual terminal control. The host applies capability/approval gates.
- Decisive decision or feedback right: select the current work split and revise current task execution in view of reported progress, blocked dependencies and failures.
- Decision owner: primary root model-backed actor in normal operation (`A`); in the alternate user-controlled Plan path the human owns Plan approval/re-approval and may prevent or authorize present execution (`P`).
- Supporting / enforcement mechanisms: `TaskListTool`, `TaskCreateTool`, `TaskUpdateTool`, `DelegateAgentTool`, `AgentSupervisor`, Plan coordinator, session store and TUI progress/approval panels.
- Closure path: current task graph and child reports → root model's revised task/delegation decision → host-checked mutation or child dispatch → updated board/child evidence → next present-time control decision. In Plan-parent mode, user approval/re-approval gates the corresponding execution Run.
- Boundary reachability: root Task tools and delegation are registered in shipped Headless composition; child status/journal return, Plan approval/resume and TUI Board are ordinary product paths rather than separate maintainer scripts.
- Why this is / is not agent-owned: the default root model chooses priority, task breakdown and active correction; deterministic queues/revisions only implement bounds. Human Plan approval is recorded as a different owner, not silently attributed to the model.
- Evidence: [`HeadlessRuntimeSession.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/runtime/HeadlessRuntimeSession.java); [`AgentSupervisor.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/subagent/AgentSupervisor.java); [`TaskListService.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/task/TaskListService.java); [`TaskToolProductionCompositionTest.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/test/java/io/github/liumaishenjian/ccjava/cli/runtime/TaskToolProductionCompositionTest.java).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: root task board does not prove general multi-team enterprise control; child process cancellation is exposed separately through host/TUI APIs rather than established as a root model Tool. Parent approval is a bounded operating mode, not an organizational S5.

### S3 owner-mode split

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root model-backed actor | Current board/child completion and blocked work | Model-facing task mutations, task/delegation decisions and updated durable board | `task/TaskListService`, `HeadlessRuntimeSession`, `AgentSupervisor` |
| Parent (`P`) | Authorized human user | Plan proposal, approval and `NEEDS_VERIFICATION` resumption | Approve/deny/reapprove to launch or withhold the present execution Run | `PlanModeCoordinator`, `HeadlessRuntimeSession`, TUI Plan review picker |

## S3* — Complementary audit

- State: C
- Function: independently test specified evidence supporting an approved Plan's claimed completion, and refuse to promote an unsupported final answer.
- Disturbance / variety regulated: an implementer model can write convincing completion prose even if a required workspace file is missing/changed, a verification Tool failed/never ran, or a Plan Task remains incomplete.
- Claim being audited: final `AssistantMessage` proposing completion of an already approved Plan execution, distinct from the human's initial decision to approve the Plan.
- Ordinary reporting path: model final answer, self-updated task statuses, and declared results in the implementing loop.
- Complementary access path: a host-owned `PlanExecutionCorrectionController` reads the durable Plan Task cohort and verifies actual workspace files by guarded re-read/SHA-256 plus recorded successful tool-result events directly from the Session. It does not rely on model prose that a check passed.
- Independence boundary: an enforced final-handler gate runs on the host side, checks underlying workspace/journal facts against existing requirements, and can withhold a model-proposed final answer. It is bounded to approved-Plan evidence types and shares the product host; no separate autonomous investigator, independent audit policy or general audit sampling was found.
- Who acts on findings: host requests up to two correction turns; recurring or unrepaired failures stop the Run with `PLAN_VERIFICATION_REQUIRED`, preserving durable `NEEDS_VERIFICATION`. A human can later explicitly reapprove verification resumption.
- Decisive decision or feedback right: accept or reject declared completion based on direct evidence rather than implementer self-report, within an externally supplied Plan brief.
- Decision owner: host-side validator judges specified facts and enforces an override; the human supplies approval/review authority; the model does not own independent audit strategy. This supports only a bounded constructor (`C`).
- Supporting / enforcement mechanisms: `validatePlanEvidence`, `PlanExecutionCorrectionController`, durable PlanArtifact/Ledger, guarded filesystem, tool-result journal, Plan Task snapshots, and `FinalAssistantDecision`.
- Closure path: model final claim → separate direct-evidence recheck → failed witness rejects final and provides correction details → resumed agent work or durable blocked terminal state.
- Boundary reachability: Plan execution wires the final-handler into the ordinary headless/TUI Run path; offline first-party tests demonstrate bounded rejection and durable state.
- Why this is / is not agent-owned: deterministic evidence validation has material separation from model claims, but cannot invent and execute independent audit scope on its own; the host and user retain the decisive gate.
- Evidence: [`HeadlessRuntimeSession.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/runtime/HeadlessRuntimeSession.java); [`DurablePlanExecutionHandoffTest.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/test/java/io/github/liumaishenjian/ccjava/cli/runtime/DurablePlanExecutionHandoffTest.java); [`PlanEvidenceLedger.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-domain/src/main/java/io/github/liumaishenjian/ccjava/domain/PlanEvidenceLedger.java).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: `AutoReviewCoordinator` reviews permission ASK before operations, **not** completed work, so it is not additional S3* evidence. The validator only checks a prescribed file or successful tool event, not semantic correctness of code or correctness of an arbitrary LLM conclusion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/external-facing organizational adaptation decision with a return to CodeJ's current whole-runtime control was established.
- Disturbance / variety regulated: web search, model routing, skills/plugins, context memory, long-running task planning, provider retries and benchmark outputs can inform a user task, but do not constitute a distinct prospective self-adaptation system.
- Decisive decision or feedback right: not established for prospective capability or environmental repositioning of the operating CodeJ organization.
- Decision owner: none established; the user chooses configured providers/plugins, the model chooses task-level approaches, and maintainers evolve CodeJ through external development.
- Supporting / enforcement mechanisms: web tools, context projection/compaction, file memory, provider router, staged roadmap, project feature matrix and G0–G6 regression/evaluation harness.
- Closure path: no autonomous outside/future diagnosis → strategic alternative → authorized present-system adaptation return loop found.
- Why this is / is not agent-owned: operational research/planning and retrospective benchmark reports do not by themselves create a long-term agent-owned adaptive organization.
- Evidence: [`README.md`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/README.md); [`docs/reference-architecture.md`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/docs/reference-architecture.md); [`ContextPreparationService.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/ContextPreparationService.java); [`ProviderRouter.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/model/ProviderRouter.java).
- Basis: explicit + bounded structural absence review.
- Confidence: medium-high.
- Caveats: the project itself has an extensive future roadmap, but it is not runtime S4 of the assessed user-facing agent system.

### Absence scope

- Surfaces inspected: shipped runtime/model router, web/context/memory/tool/plugin extension paths, approved Plan and session lifecycle, README and architecture/roadmap, and the repository's offline evaluation/progress machinery.
- Plausible first-party paths checked: web search as external-sensing function; Plan as future organizational strategy; self-compaction/file memory as cross-task learning; provider failover as prospective capability adaptation; feature parity/evals as an S4 regulator; marketplace plugins/skills as an evolving capacity allocator.
- Why no material first-party path remains: these paths execute or support current user-defined coding work, local efficiency, or the outside maintainer development process. No product-owned future scenario/strategic-choice decision feeds a deliberate adaptation back into the current S3 organization.

## S5 — Policy and identity

- State: —
- Function: no distinct operating-level identity, ultimate-purpose or policy-adjudication process returning binding decisions to the same runtime organization was established.
- Disturbance / variety regulated: permissions, approvals, hard denials, session retention, governance configuration, sandbox requirements, and root-owner Plan approvals are concrete operational constraints, not evidence of ultimate constitutional policy judgment.
- Decisive decision or feedback right: no first-party right to reconsider CodeJ's identity or arbitrate S3/S4 purpose tension is implemented.
- Decision owner: users/hosts set tool permissions and approved plans; developers configure managed feature policies; none is a shown identity-level systemic S5 feedback owner within the product.
- Supporting / enforcement mechanisms: `PermissionPolicy`, `DefaultHardDenialPolicy`, `AutoReviewCoordinator`, Plan approval, `ManagedGovernance`, and SDK `AgentControlApi.governance()` read-only projection.
- Closure path: no identity/purpose dilemma → legitimate final authority → binding identity-policy return path into the evaluated root Session.
- Why this is / is not agent-owned: a permission classifier approves particular tool requests, while the SDK's governance endpoint describes enabled feature gates; neither sets organizational self-identity or adjudicates its purposes.
- Evidence: [`AutoReviewCoordinator.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-core/src/main/java/io/github/liumaishenjian/ccjava/core/AutoReviewCoordinator.java); [`AgentControlApi.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-sdk/src/main/java/io/github/liumaishenjian/ccjava/sdk/AgentControlApi.java); [`ManagedGovernance.java`](https://github.com/liumaishenjian/codej/blob/e51e6b5062fbab46881137342a2bff84bfc05645/cc-java-cli/src/main/java/io/github/liumaishenjian/ccjava/cli/governance/ManagedGovernance.java).
- Basis: explicit + bounded structural absence review.
- Confidence: medium-high.
- Caveats: the repository's term `governance` names managed configuration/provenance; terminology cannot substitute for an operational S5 function.

### Absence scope

- Surfaces inspected: first-party permission modes, approval/AutoReview, Plan authority and verification-resume, managed governance, SDK/stable protocol, sandbox and session retention, and external contributor/development contracts.
- Plausible first-party paths checked: user Plan approval as a constitutional decision; `governance.get` as an S5 owner; managed policies and hard denial as organizational identity; permission model reviewer as independent ultimate authority; project product requirements as an in-product S5 conversation.
- Why no material first-party path remains: the paths control authorized operational effects or display already configured rules. No implemented first-party identity-level final-choice and feedback path at root/child organization recursion was demonstrated.

## Recursion

- Root Session is the focal viable organization; each supervised child has a separate AgentRuntime, Session, permission context and task goal, but its visible parent Task Board rights are constrained to assigned IDs.
- Default supervisor limits of four active, 32 queued and depth two constrain resource use; they do not mean that every nested child operates a full S1–S5 metasystem.
- Worktree isolation provides optional workspace separation rather than a substitute for S2. The root-owned Task Board is a genuine shared coordination mechanism only in the composed, scope-sharing mode.

## Variety and escalation

- Operational variety: model-selected file and command tools with returned evidence; explicit tool denial, timeout, cancellation and context recovery.
- Coordination variety: actor-bound Task claims, Board/Task revision checks, DAG blockers, recovery-required claims and conflict diagnostics; parent-model task allocation on top of host enforcement.
- Current control: parent board overview, task/delegation changes and child reports; a different human Plan authorization path.
- Complementary discrepancy: bounded independent file/tool-event evidence checks can defeat unsupported Plan completion prose; failures return correction projections or preserve an explicit unresolved state.
- Escalation: deterministic permissions, Plan approval, host-owned Task constraints and durable recovery can require a human decision; none thereby creates S4 or S5.

## Evidence gaps

- Frozen first-party code and its checked-in fake/provider-mock tests were inspected. No live model-agent runs were executed (out of assessment test scope).
- The local available JDK is 17, below CodeJ's declared Java 21 build requirement; native Maven test execution is therefore not claimed. Source tests are cited as corroboration, not as locally executed proof.
- The scoped-board path is opt-in and permits cross-task claim coordination, not comprehensive cross-file semantic conflict analysis or an across-all-CodeJ organizational control plane.
- The complementary Plan checker verifies concrete predeclared evidence and completion records, not arbitrary mathematical/software correctness; no separate autonomous auditor is present in the first-party shipping boundary.
- No first-party S4/S5 closure was found in the named runtime and adjacent candidate paths. The absence states do not assert impossibility in third-party compositions.
