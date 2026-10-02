---
harness_id: ogcode
project_name: Ogcode
repository: https://github.com/prasenjeet-symon/ogcode
review_ref: b9077a0fcca60195da4426b3f733933b533be705
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Ogcode

## Review boundary

- System in focus: Ogcode's currently implemented first-party software-work runtime at frozen revision `b9077a0fcca60195da4426b3f733933b533be705`: interactive Build/Plan modes, model/tool loop, plan breakdown, task/worktree/branch/PR execution, task board, permissions, project instructions, sessions and persistent memory.
- Purpose and identity: turn a software-development goal into repository understanding, an approved plan, coordinated implementation tasks and reviewable code/PR outcomes while retaining operator oversight.
- Relevant environment: the target repository/workspace and git remote; developer/operator goals and policy; files, builds/tests and shell processes; external model providers; web/search sources; optional MCP/skills.
- Standard-distribution boundary: shipped Ogcode Go server/CLI, agent definitions, task/plan stores, plan breakdown and task execution paths, git/worktree integration, browser workbench, permissions, memory/search and project-instruction loading are inside. Model endpoints, git/GitHub services, external MCP servers, host OS and target-project code are dependencies/environment.
- Credited operating / distribution surfaces: `internal/agent/`; `internal/server/plan_routes.go`; `internal/server/task_routes.go`; `internal/task/`; `internal/plan/`; `internal/git/`; `internal/tool/`; `internal/session/`; `web/src/pages/plan-tasks.tsx`; `web/src/pages/task-execution.tsx`; `web/src/context/session.tsx`; README current-capability sections.
- Adjacent first-party surfaces excluded from ownership: Ogcode's own repository-development instructions/tests/CI and architecture audits; control-plane roadmap/development surfaces not required by the ordinary software-work runtime; future general computer-agent roadmap claims; external GitHub review/merge decisions.
- First-party operating / deployment modes considered: interactive Build Mode; read-only Plan Mode; locked-plan BreakdownAgent; headless TaskAgent execution in isolated git worktrees; browser task-board supervision; read-only delegated `task` investigations; persistent project/session memory; self-hosted local/server operation.
- Recursion level: one software-delivery plan/workspace organization. Interactive BuildAgent and independently executing TaskAgent worktrees are S1 units when producing software outcomes. BreakdownAgent can own S2 coordination over task workstreams. The operator is a parent recursion for whole-plan current supervision and project policy.
- Reviewed revision: `b9077a0fcca60195da4426b3f733933b533be705`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Ogcode ships several distinct model-backed agent profiles. BuildAgent performs interactive full-access coding. PlanAgent inspects the repository and develops a read-only implementation plan with the developer. Once the user locks that plan, a separate BreakdownAgent receives the final agreed plan and emits structured task definitions. TaskAgent then executes each implementation task in a dedicated git worktree with the same full coding toolset as BuildAgent and commits its result.

The breakdown path is explicitly coordination-aware rather than generic decomposition. BreakdownAgent is instructed that independent tasks must not edit the same files, that each file belongs to exactly one parallel workstream, and that any tasks which must touch the same file must be connected by a dependency so they execute sequentially. The resulting dependency/file-scope decisions are persisted as task records. Runtime machinery then creates isolated worktrees, starts dependency-ready tasks, integrates completed chain tasks before starting dependents, blocks failed chains and supports clean retry.

Ogcode also exposes a first-party plan task board. It shows the whole plan split into pending, in-progress, completed and failed work with aggregate progress and current running count. The operator can start eligible tasks, start all eligible work, open an in-progress agent session, mark current work complete/failed and retry failed work. A task session is a normal persisted session registered in the server's running-loop map; the standard session abort endpoint cancels that exact running loop and its in-flight tool work.

The model-facing `task` tool is a separate read-only investigation helper. It creates a clean-context child that can inspect code and web sources and returns a written result, but the frozen distribution does not define a reviewer/evaluator role or a standard audit decision/return loop around implementation claims. Coding/Task agents are instead instructed to verify their own work with syntax checks/build/tests.

Project instructions and memory are distinct. Ogcode discovers `AGENTS.md` and `AGENT.md` from filesystem root to project leaf, preserving closer instructions as later/higher-precedence prompt material; these owner-authored rules enter the model system context. `MEMORY.md`, session memory and project-memory recall preserve prior operational facts/decisions, but do not by themselves select future organizational adaptations.

## Operational model

In ordinary Build Mode, a model-backed coding agent reads project evidence, invokes tools, receives results and iterates until the requested software outcome is complete.

For larger work, PlanAgent develops a plan with the user. Locking is a deliberate operator transition: Ogcode captures the base branch and generates the final canonical plan. BreakdownAgent then independently translates that locked plan into implementation-ready tasks with dependencies and file ownership. The server materializes those decisions into isolated task worktrees. Dependency-free work can run concurrently; dependency chains run in order and share their chain branch so later workers see predecessor output. Successful work is committed and can be pushed into standalone or chain pull requests.

The task board supplies the operator with a current whole-plan view and intervention surfaces, while task sessions expose the underlying live model/tool transcript and ordinary session abort. This parent current-control path is separate from BreakdownAgent's autonomous S2 decision.

## S1 — Operations

- State: A
- Function: produce repository-facing software outcomes through open-ended model/tool coding action.
- Disturbance / variety regulated: heterogeneous code structure, incomplete implementation details, syntax/build/test failures, repository state, tool output, external documentation, context limits and changing user requirements encountered during implementation.
- Decisive decision or feedback right: decide what project evidence to inspect, which coding/tool action to take, how to respond to returned failures/evidence, what implementation satisfies the assigned outcome and when local work is complete.
- Decision owner: model-backed BuildAgent in interactive work and model-backed TaskAgent in each plan worktree.
- Supporting / enforcement mechanisms: tool registry; repository maps/search/read/edit/write/bash; syntax checks; provider adapters; permissions; sessions; compaction/memory; worktrees and git; cancellation/timeouts.
- Closure path: software goal/task description plus project context → agent selects action/tool → tool/environment result returns into the same agent loop → agent revises implementation or verifies/finishes → repository-facing result is produced.
- Boundary reachability: BuildAgent is the normal interactive mode; TaskAgent is constructed by the standard plan/task execution path and runs the shipped coding loop in its worktree without adopter-authored orchestration.
- Why this is / is not agent-owned: removing the model-backed Build/Task actor while retaining tools, worktrees, stores and permission machinery removes the task-specific software-engineering judgment.
- Evidence: [`internal/agent/agent.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/agent.go); [`internal/agent/loop.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/loop.go); [`internal/server/task_routes.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/server/task_routes.go); [`README.md`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference and GitHub remote service behavior are dependencies; the credited loop/control composition is first-party Ogcode.

## S2 — Coordination

- State: A
- Function: prevent destructive interference and merge conflict among parallel implementation S1 workstreams by deciding file ownership/dependency relations before execution and feeding those relations into task scope/order.
- Disturbance / variety regulated: independently executing TaskAgents can otherwise modify overlapping files from parallel branches, creating incompatible patches/merge conflicts; dependent implementation can also run before prerequisite changes are present.
- Distinct S1 units: separate TaskAgent sessions executing different implementation tasks in distinct git worktrees/branches.
- Inter-S1 disturbance: overlapping parallel file mutation can produce competing patches at integration time; premature dependent execution can act on a repository state missing predecessor work.
- Attenuating coordination relation: BreakdownAgent must assign each file to exactly one parallel workstream and add a dependency whenever two tasks need the same file. It also defines linear dependencies reflecting implementation prerequisites. The runtime then isolates tasks in worktrees and executes dependencies only after predecessor integration.
- Feedback into subsequent S1 behaviour: BreakdownAgent's task descriptions/dependencies become the authoritative TaskAgent prompts and task records; the chosen graph determines whether a task starts concurrently or waits, which branch/worktree it sees, and which files it is instructed to modify.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party breakdown prompt explicitly names the concrete shared-file merge-conflict disturbance and requires file ownership/dependency decisions to attenuate it. Worktrees and dependency scheduling enforce that selected coordination relation rather than merely moving work between agents.
- Decisive decision or feedback right: choose the task-specific partition of files/workstreams and the dependency relation needed to avoid cross-worker conflict while preserving safe parallelism.
- Decision owner: model-backed BreakdownAgent.
- Supporting / enforcement mechanisms: structured `submit_task_breakdown`; task dependency records; per-task worktrees/branches; chain branches; dependency readiness checks; atomic task claims; serialized git metadata mutation; automatic dependent startup after predecessor integration.
- Closure path: locked plan/repository evidence → BreakdownAgent identifies scopes/dependencies under explicit anti-conflict rules → structured task graph is stored → server creates isolated worktrees and schedules according to that graph → TaskAgents receive scoped descriptions and predecessor state → later S1 operation follows the selected coordination.
- Boundary reachability: BreakdownAgent, breakdown tool and plan/task materialization are invoked automatically by the standard locked-plan mode; no consumer-authored coordinator is needed.
- Why this is / is not agent-owned: removing BreakdownAgent leaves deterministic mechanisms capable of enforcing a supplied graph, but removes the discretionary, task-specific choice of which files/workstreams should be parallel versus ordered.
- Evidence: [`internal/agent/breakdown.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/breakdown.go); [`internal/agent/agent.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/agent.go); [`internal/tool/breakdown.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/tool/breakdown.go); [`internal/server/task_routes.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/server/task_routes.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: worktree/dependency enforcement itself is deterministic; autonomy is assigned to the BreakdownAgent's organizational partition decision, not to git or the scheduler.

## S3 — Inside-and-now control

- State: P
- Function: give the legitimate operator a whole-plan current view and authority to intervene in active implementation commitments on behalf of the current software-delivery whole.
- Disturbance / variety regulated: a plan may contain pending, blocked, running, failed and completed tasks; a current TaskAgent can stall, take a wrong path, fail, need retry or need operator-directed interruption while other plan commitments continue.
- Whole-system current view: the first-party task board groups every task in the active plan by current status, shows total/done/running/failed/pending counts, dependency eligibility and per-task branch/session/PR state.
- Current-control decision scope: start one eligible task or all eligible tasks; inspect a running task's live agent session; abort that running session; mark current work complete/failed where appropriate; retry failed work from a clean task state.
- Decisive decision or feedback right: choose which currently eligible commitments are started and when a current task session should be interrupted/retried/failed as part of supervising the active plan.
- Decision owner: human/operator at the parent recursion.
- Supporting / enforcement mechanisms: plan/task stores; task-board projections; task/session routes; server running-loop registry; context cancellation; dependency scheduler; worktree cleanup/retry; SSE/bus status updates.
- Closure path: task board/current session exposes whole-plan current state → operator selects start/intervention/retry or abort → first-party API mutates task state or cancels the registered task session loop → task/plan events and dependency eligibility update → subsequent current execution changes.
- Boundary reachability: the browser plan/task board and task-execution session are standard product surfaces; TaskAgent loops are registered in the same server `running` map consumed by the generic first-party session-abort endpoint.
- Why this is / is not agent-owned: BreakdownAgent selects the initial coordination graph but does not receive a live whole-plan control loop. Runtime auto-start is deterministic enforcement of the frozen dependency graph. The discretionary current-control mode established in the frozen product belongs to the operator.
- Evidence: [`web/src/pages/plan-tasks.tsx`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/web/src/pages/plan-tasks.tsx); [`web/src/pages/task-execution.tsx`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/web/src/pages/task-execution.tsx); [`internal/server/task_routes.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/server/task_routes.go); [`internal/server/session_routes.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/server/session_routes.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a parent/operator supervisory mode, not autonomous S3. The deterministic dependency scheduler and automatic completion transitions do not themselves own discretionary whole-system current-control judgment.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit loop was established that independently challenges implementation claims and returns a distinct audit judgment into current control.
- Disturbance / variety regulated: implementation agents can be wrong about the correctness/completeness of their own changes, but the frozen standard distribution does not package a separate reviewer/evaluator role or audit gate with complementary evidence access.
- Claim being audited: no standard first-party independent-audit claim/route was established.
- Ordinary reporting path: BuildAgent/TaskAgent implement changes and are themselves instructed to run syntax/build/test/lint verification before declaring completion.
- Complementary access path: none established as an audit function. The generic `task` tool can spawn a clean-context read-only investigator over code/web evidence, but its shipped contract is broad investigation/context offload rather than independent review of producer claims, and no standard reviewer role/accept-correct loop is wired around task completion.
- Independence boundary: no material audit boundary is established beyond optional generic investigation.
- Who acts on findings: no standard independent-audit finding/closure path established.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: self-verification in coding prompts; read-only TaskTool investigation; syntax checker; builds/tests; git/PR artifacts.
- Closure path: not applicable; no standard complementary auditor judgment is returned as a distinct control input.
- Boundary reachability: not applicable for a positive path.
- Why this is / is not agent-owned: ordinary tests and the implementer's own verification are the production path, while generic clean-context investigation is not packaged as an audit function in the frozen distribution.
- Evidence: [`internal/agent/agent.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/agent.go); [`internal/tool/task.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/tool/task.go); [`internal/server/task_routes.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/server/task_routes.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator or BuildAgent could formulate a review-like prompt for the generic read-only child, but generic subagent expressiveness is not treated as a standard-distribution S3* audit loop.

### Absence scope

- Surfaces inspected: all shipped agent definitions; coding/task verification instructions; read-only delegated TaskTool; plan/breakdown/task execution; task board/session supervision; syntax/build/test paths; git worktree/PR completion; frozen tree paths matching review/audit/verify/subagent.
- Plausible first-party paths checked: dedicated reviewer/evaluator agent; independent post-task review gate; generic read-only child as reviewer; Plan/Breakdown agent as post-hoc auditor; PR creation as audit; tests/syntax checking as complementary evidence.
- Why no material first-party path remains: no dedicated or standard audit role/gate was found at the frozen ref; Plan/Breakdown act before implementation, PR creation transports completed work, and tests are selected/interpreted by the implementation path itself. The generic child is an investigation primitive without a packaged audit claim/closure relation.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then loop was established that senses external/future change, develops organizational adaptation options and returns a selected adaptation into present capability.
- Disturbance / variety regulated: external documentation/search, prior project decisions, model/tool availability and persistent memory can influence current software work, but none forms a first-party prospective adaptation cycle at the selected organization boundary.
- Decisive decision or feedback right: none established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `deep_search` and page fetching; PlanAgent; NoteAgent; session/project memory recall; MEMORY.md; skills/MCP/model configuration; compaction; persistent sessions and archived plans.
- Closure path: not applicable; no external/future distinction → adaptation-option development → selected persistent capability/strategy change → return to current S3/capability loop was found.
- Why this is / is not agent-owned: PlanAgent plans current requested software, recall restores past operational context, and search answers present questions. These paths do not establish prospective organizational adaptation merely because they contain research, learning or persistence.
- Evidence: [`README.md`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/README.md); [`internal/agent/agent.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/agent.go); [`internal/tool/memory_recall.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/tool/memory_recall.go); [`internal/tool/project_memory_recall.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/tool/project_memory_recall.go); [`internal/agent/memorymd.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/memorymd.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the README contains a broader future computer-agent vision; intake explicitly excludes those roadmap claims from current-state evidence.

### Absence scope

- Surfaces inspected: Plan/Breakdown/Note agents; web/deep search; skills/MCP/model configuration; session/project memory and MEMORY.md; archives; task retry; provider/tool hot configuration; current software-delivery workflow.
- Plausible first-party paths checked: web research as future intelligence; PlanAgent as strategic planning; NoteAgent as environmental sensing; memory consolidation/recall as organizational learning; skill/MCP/model changes as adaptation; retry/failure recovery as adaptation.
- Why no material first-party path remains: all located paths serve a current user goal, retain/retrieve operational history, or expose operator-selected configuration. The frozen product does not autonomously convert external/prospective distinctions into adaptation alternatives and persist one back into the organization's later capabilities/current-control loop.

## S5 — Identity / ultimate policy

- State: P
- Function: carry legitimate project-owner standing instructions/rules into every relevant Ogcode agent context so later software work remains governed by project-level policy.
- Disturbance / variety regulated: coding/planning/task agents can otherwise diverge from repository architecture, conventions, risk boundaries or durable owner instructions across sessions/worktrees.
- Identity / ultimate-policy issue: which durable project rules, priorities and behavioral constraints legitimately govern Ogcode's work in the selected repository.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/editor owns project `AGENTS.md` / `AGENT.md` instruction content. No autonomous agent-owned identity/ultimate-policy mode is established.
- Return-to-operation path: Ogcode discovers owner-authored instruction files from root to current project directory, preserves root-to-leaf precedence, loads their text into the agent system-prompt construction and thereby governs later Build/Plan/Task execution in that project.
- Decisive decision or feedback right: decide the durable project-level instructions and precedence that should constrain future agent operation.
- Decision owner: human/project owner at the parent recursion.
- Supporting / enforcement mechanisms: instruction-file discovery/loading; root-to-leaf ordering; prompt block rendering/escaping; system prompt builder; ordinary file/version-control persistence.
- Closure path: project-level policy issue → legitimate owner changes AGENTS.md/AGENT.md → Ogcode reloads project instructions for agent execution → instructions enter system context → subsequent software operation is governed by the returned policy.
- Boundary reachability: AGENTS.md/AGENT.md loading is first-party runtime code invoked by the standard agent prompt construction; it is not a contributor-only plugin or external wrapper.
- Why this is / is not agent-owned: model agents consume the standing instructions but do not receive a first-party mechanism making their self-authored policy legitimate ultimate authority; ownership remains with the project authority that supplies the files.
- Evidence: [`internal/agent/agentmd.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/agentmd.go); [`internal/agent/loop.go`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/internal/agent/loop.go); [`README.md`](https://github.com/prasenjeet-symon/ogcode/blob/b9077a0fcca60195da4426b3f733933b533be705/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: permission prompts and ordinary task/plan approval are operational controls and are not used as S5 evidence; S5 is limited to durable project-recursion policy returned through the project instruction surface.

## Distributed OSS parent arrangement

Public maintainers govern the Ogcode software project itself, but that repository-development organization is outside the target software-delivery plan/workspace assessed here. The credited parent rights are local: the operator supervises current plan execution for S3, and the legitimate target-project owner supplies project policy for S5.

## Self-hosted and non-human modes

Build/Task S1 and BreakdownAgent S2 can operate autonomously once goals/plan authority are supplied. Plan task execution is then largely deterministic between agent decisions. The frozen distribution retains operator current-control over active plan commitments and project-owner ultimate policy; no autonomous S3/S5 mode is credited. No autonomous S4 or S3* path is established.

## Recursion

At the chosen plan/workspace recursion, individual Build/Task coding sessions are S1 cells. BreakdownAgent regulates interference among task workstreams as S2. The operator sits at a parent recursion for whole-plan S3 control; the project owner supplies S5 policy. Read-only TaskTool children, NoteAgent and memory-recall agents are mechanisms/specialists but do not become additional VSM functions by name.

## Variety and escalation

Local implementation variety stays with each S1. Cross-workstream file/dependency variety is attenuated by BreakdownAgent's graph/file-ownership decision and enforced by worktrees/chains. Current task failures/stalls surface to the plan board and can be interrupted/retried by the operator. Project-level standing-policy changes return through AGENTS.md/AGENT.md. No independent audit escalation or outside-and-then adaptation path is established.

## Evidence gaps

No reviewed evidence gap requires `?`. S3* and S4 negatives are backed by explicit absence scopes; S3 is restricted to the parent current-control mode rather than inferred from deterministic scheduling; S5 is restricted to durable project policy rather than ordinary approval.

## Assessment summary

Ogcode closes autonomous coding S1 and autonomous S2: its dedicated BreakdownAgent makes task-specific file-ownership/dependency decisions explicitly intended to prevent merge conflicts, and runtime worktrees/chains enforce those decisions. The frozen distribution does not expose an autonomous whole-plan S3 manager; instead the first-party task board/session controls close S3 at the operator parent. Coding agents self-verify and can spawn generic clean-context investigations, but no standard complementary audit loop is packaged, so S3* is absent. Research/memory/planning remain current-work mechanisms rather than S4. Project-recursion S5 remains parent-owned through AGENTS.md/AGENT.md instructions returned into agent system prompts.

Proposed vector: **`A · A · P · — · — · P`**.
