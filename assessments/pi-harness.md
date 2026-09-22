---
harness_id: pi-harness
project_name: Pi-Harness
repository: https://github.com/wangmiaozero/pi-harness
review_ref: efed4bd8d01505ae5fc8a52de243af7a3827ec39
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: C(P)
autonomy_s5: —
---

# Pi-Harness

## Review boundary

- System in focus: one installed Pi-Harness desktop/control-plane instance at pinned revision `efed4bd8d01505ae5fc8a52de243af7a3827ec39`, including its Harness Console, orchestration service, task/dependency/team state, worktree isolation, handoffs, review gates, run/evidence/evaluation state, policy/budget/checkpoint/recovery controls, capability/package management, and operator-facing IPC/UI surfaces.
- Purpose and identity: provide a visual control plane around Pi Coding Agent that observes and regulates runs, coordinates multi-agent work, enforces policy/budgets, supports recovery/review, and manages the capabilities available to Pi without replacing Pi's agent runtime.
- Relevant environment: user/operator, project repository and Git state, Pi Coding Agent / Pi Agent Harness, model/provider services, npm package registry and package ecosystem, installed skills/extensions, filesystem/shell/network resources, and changing software-development tasks.
- Standard-distribution boundary: first-party Pi-Harness desktop/main-process/renderer code and bundled product-owned control-plane services. Pi Coding Agent and Pi Agent Harness remain the external operational agent runtime explicitly identified by the repository; model providers and third-party packages/skills remain environmental systems.
- Credited operating / distribution surfaces: `README.md`; Harness runtime/policy/run/checkpoint/evaluation services; `src/main/harness/orchestrator/*`; first-party orchestration IPC and renderer stores/panels; package/skill management and npm-registry services; workspace/Git controls used by the shipped desktop application.
- Adjacent first-party surfaces excluded from ownership: repository CI, tests, release/changelog maintenance, contributor workflows, and bundled third-party methodology/skill content when it is not wired into a first-party runtime closure path. These can corroborate implementation but do not donate metasystem ownership.
- First-party operating / deployment modes considered: normal single Pi session control; Harness Console run/policy/evaluation/recovery usage; multi-agent orchestration with manual/sequential/dependency scheduling, worktree isolation, handoffs and review gates; operator-controlled package/skill discovery, install and update.
- Recursion level: the installed Pi-Harness control plane is the system-in-focus. Individual Pi agent sessions assigned to bounded tasks are S1 operational units. Pi's internal agent-loop machinery is below/outside the credited Pi-Harness metasystem boundary unless reached through an explicit first-party control relation.
- Reviewed revision: `efed4bd8d01505ae5fc8a52de243af7a3827ec39`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Pi-Harness explicitly separates its desktop control plane from Pi Agent Harness: Pi runs the agent loop, tools, context, compaction and session execution, while Pi-Harness adds orchestration, observability, policy, evaluation, recovery and operator control. The first-party orchestrator creates tasks and agents, tracks dependencies, launches real Pi sessions, records run/artifact/evaluation state, creates per-agent worktrees, carries artifact handoffs, detects overlapping file modification and gates selected tasks through designated reviewer agents.

The Harness Console also owns current-control surfaces. It exposes orchestration status, task and agent state, budgets, run/evaluation results and recovery controls, while operator actions can pause/resume/abort an orchestration, retry/skip/reassign work, revise task/agent assignments and budgets, and change policy. Deterministic scheduling, dependency gates and budget enforcement implement decisions but are not treated as autonomous decision owners.

Capability management forms a separate adaptation surface. Pi-Harness queries the external npm registry for Pi packages, exposes package details and update checks, and can install/update/remove packages and skills that alter the capabilities available to subsequent Pi runs. The shipped path therefore reaches an external capability environment and returns selected changes into current operation, but the standard product leaves the decisive adoption choice with the operator and exposes programmatic first-party services for downstream specialization rather than packaging an autonomous adaptation owner.

## Operational model

A user selects a project/session and asks Pi to perform work. Pi-Harness starts or resumes the Pi-compatible session, selects model/tool/configuration state and exposes streaming runtime state. In orchestration mode, the operator creates a team/task graph and the orchestrator dispatches bounded tasks to Pi-backed agent sessions. Dependencies, worktrees, artifacts and handoffs structure interaction between those sessions. Finished work can be routed to a separate reviewer agent before a task is accepted; rejection is persisted and injected into the next executor attempt.

At the installation recursion, Pi-Harness supplies rich whole-orchestration state and first-party current-control actions but no packaged autonomous installation manager that decides when to pause, reassign, retry, skip or change budgets. This is therefore an S3 constructor mode with a directly usable operator/parent mode. For S2, the product exposes a specific multi-agent interference witness and attenuation machinery, but the reviewed distribution does not close that coordination decision right autonomously or establish a sufficiently explicit parent conflict-resolution loop from detected conflict to chosen coordination relation; the shipped surface is therefore constructor-only.

## S1 — Operations

- State: A
- Function: execute bounded software-engineering work through real Pi Coding Agent sessions, including reasoning, tool use and artifact production for user or orchestration-assigned tasks.
- Disturbance / variety regulated: heterogeneous coding objectives, repository/workspace state, tool results, model uncertainty, test/build feedback and task-specific environmental changes.
- Decisive decision or feedback right: choose the substantive reasoning path, tool calls and task actions needed to pursue the admitted objective within the configured Pi session.
- Decision owner: the autonomous Pi Coding Agent/model actor reached through the first-party Pi-Harness session/orchestration path.
- Supporting / enforcement mechanisms: session start/resume/fork controls, model/tool selection, Harness policy, run recording, worktree binding, task context, checkpoints, evaluation and orchestration dispatch.
- Closure path: objective/task is admitted → Pi-Harness starts or resumes a Pi-backed session with task context → the model actor chooses reasoning/tools/actions → tool/environment feedback returns through Pi → produced artifacts/run state return to Pi-Harness and the user/orchestrator.
- Boundary reachability: the README states that every orchestrated agent executes through a real Pi session and that Pi remains the sole agent runtime; Pi-Harness directly reaches that autonomous actor through its shipped session/orchestration host rather than through repository-development machinery.
- Why this is / is not agent-owned: Pi-Harness supplies control and constraints, but the task-local substantive choices are made by the Pi/model actor. Deterministic policy or scheduling does not replace that S1 discretion.
- Evidence: [`README.md`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/README.md); [`src/main/agent/agent-runtime-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/agent/agent-runtime-service.ts); [`src/main/harness/orchestrator/orchestrator-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/orchestrator-service.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `A` credits the external Pi/model actor reached by the standard Pi-Harness operating mode; it does not attribute Pi Agent Harness internals to this repository.

## S2 — Coordination

- State: C
- Function: attenuate interaction-generated interference between sibling task agents that can modify overlapping repository state while participating in one orchestration.
- Disturbance / variety regulated: parallel agents can touch the same file or depend on one another's changing repository state, creating clobbering, incompatible edits or invalid downstream assumptions.
- Decisive decision or feedback right: choose the coordination relation that should resolve or avoid a detected inter-agent interference — for example dependency ordering, task reassignment/retry or another relation exposed by the orchestration control plane.
- Decision owner: no autonomous S2 owner is packaged at the reviewed boundary; the first-party conflict/dependency/worktree/task-control surfaces expose the function for a downstream coordinator.
- Supporting / enforcement mechanisms: per-agent worktree isolation, explicit task dependencies, artifact handoffs, `ConflictService`, task scheduler, orchestration state and retry/reassign controls.
- Closure path: sibling Pi-backed task agents operate on bounded work → worktree/artifact records expose their touched paths → `ConflictService` groups file artifacts by path and reports files touched by more than one agent → the first-party orchestration surface exposes the affected agents/tasks and coordination controls → a composed coordinator can change the relation governing subsequent task execution.
- Boundary reachability: conflict detection, worktree creation, task dependency state and retry/reassign/update controls are first-party runtime services reached in normal multi-agent orchestration; no CI or maintainer-only path is required.
- Why this is / is not agent-owned: deterministic isolation/detection attenuates and surfaces interference but does not choose how to resolve the reported multi-agent conflict. The repository exposes the S2-specific path without supplying an autonomous decision owner, so the state is constructor rather than autonomous.
- Evidence: [`README.md`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/README.md); [`src/main/harness/orchestrator/conflict-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/conflict-service.ts); [`src/main/harness/orchestrator/orchestrator-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/orchestrator-service.ts); [`src/main/harness/orchestrator/task-scheduler.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/task-scheduler.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: dependency graphs and worktrees are not credited merely because they exist. The positive mapping relies on the repository's explicit overlapping-file conflict witness across distinct agents. No stronger `P` claim is made because the reviewed evidence does not establish one explicit shipped operator loop that detects a particular conflict, selects the S2 relation, and returns that relation into execution as a named conflict-resolution path.
- Distinct S1 units: separate Pi-backed orchestration agents/tasks, such as the documented Frontend and Backend agents running concurrently.
- Inter-S1 disturbance: two sibling agents can modify the same repository path; the README gives `Frontend and Backend both modified src/api.ts` as a concrete conflict example and `ConflictService` detects paths touched by multiple agents.
- Attenuating coordination relation: per-agent worktree isolation prevents direct workspace clobbering while dependencies/handoffs and task-control surfaces provide a first-party place to impose ordering/reassignment before subsequent work.
- Feedback into subsequent S1 behaviour: changed dependencies/assignment/retry state alters which agent is dispatched next and what task context/workspace relation it receives.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is not merely a DAG or message path; it is a concrete interaction-generated disturbance between sibling S1 units over shared file state, with first-party isolation, detection and relation-changing controls aimed at that interference.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current orchestration as a whole by deciding whether and how active work should proceed under present task, agent, dependency, budget, run and failure conditions.
- Disturbance / variety regulated: current orchestration state can include running/blocked/failed tasks, exhausted agent or orchestration budgets, stuck work, dependency readiness, failed evaluations and changing assignment/load conditions.
- Decisive decision or feedback right: pause/resume/abort the orchestration; retry, skip or reassign tasks; revise task/agent assignment and budgets; and otherwise alter current execution commitments using the exposed orchestration control plane.
- Decision owner: base constructor mode — no autonomous whole-orchestration manager is packaged, so a downstream controller must consume the first-party snapshot/control interfaces. Parent mode — the human operator using the shipped Harness Console/IPC controls.
- Supporting / enforcement mechanisms: orchestration store/snapshot, scheduler, dependency resolver, budget checks, stuck detection, run/evaluation records, renderer orchestration store/panels and IPC handlers.
- Closure path: current whole-orchestration state is observed → controller/operator chooses a current intervention → first-party orchestration control mutates status/task/agent/budget state → scheduler/runtime reconciles the new state → subsequent current dispatch/admission changes accordingly.
- Boundary reachability: the orchestrator, IPC and renderer expose these state/control surfaces in the normal desktop runtime; the operator can close them directly and a downstream autonomous controller can be composed over the same first-party functions.
- Why this is / is not agent-owned: task scheduling and policy enforcement are deterministic mechanisms, not S3 decision owners. The repository exposes S3-specific whole-system current state and intervention rights but packages only the operator as the decisive owner.
- Evidence: [`README.md`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/README.md); [`src/main/harness/orchestrator/orchestrator-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/orchestrator-service.ts); [`src/main/ipc/register-harness.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/ipc/register-harness.ts); [`src/renderer/src/stores/orchestration.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/renderer/src/stores/orchestration.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: automatic dependency scheduling, budget stops and stuck detection are supporting mechanisms only; they do not by themselves establish autonomous S3 ownership.
- Whole-system current view: the orchestration snapshot covers the team/task graph, agent state, task status/dependencies, current runs, budgets/cost/tokens and orchestration status, while Harness Console surfaces current run/evaluation/recovery state.
- Current-control decision scope: change whether the orchestration continues now and which agent/task commitment proceeds next through pause/resume/abort, retry/skip/reassign and current budget/assignment edits.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous orchestration controller must be composed | current task/agent/run/dependency/budget state requires an intervention | controller consumes the first-party snapshot and invokes the existing control functions; scheduler/runtime reconciles the changed current state | `src/main/harness/orchestrator/orchestrator-service.ts`; `src/main/ipc/register-harness.ts` |
| Parent (`P`) | Pi-Harness operator | current failure, budget, dependency, stuck or assignment condition | operator uses shipped pause/resume/abort/retry/skip/reassign or edit controls; changed state is persisted and affects subsequent dispatch | `README.md`; `src/renderer/src/stores/orchestration.ts`; orchestration panels |

## S3* — Complementary audit

- State: A
- Function: independently challenge a producer agent's claim that a review-gated task is acceptable before allowing task completion, and return adverse findings into corrective re-execution.
- Disturbance / variety regulated: an executor can produce incomplete, incorrect or otherwise unacceptable artifacts despite ordinary run/evaluation reporting.
- Decisive decision or feedback right: a distinct reviewer agent returns an approval/rejection verdict and summary over the producer's task outcome; rejection prevents accepted completion and becomes corrective input to the next executor attempt.
- Decision owner: the autonomous Pi/model actor instantiated as a designated reviewer agent (`isReviewer`) rather than the producer agent.
- Supporting / enforcement mechanisms: `reviewRequired`, `reviewAgentId`, reviewer dispatch phase, reviewer task-context construction, artifact/run summaries, parsed review verdict, persisted `reviewVerdict`/`reviewSummary`, retry state and task-context feedback.
- Closure path: executor produces task artifacts/run evidence → review-required task is dispatched to a distinct reviewer agent → reviewer inspects the task/output evidence and returns verdict/summary → approval permits completion; rejection records the finding and fails/returns the task → retry preserves the rejected-review summary → the next executor prompt explicitly instructs the producer to address that reviewer feedback.
- Boundary reachability: reviewer templates/agents, review-required task state and review dispatch are all first-party orchestration runtime paths reachable in the shipped multi-agent mode.
- Why this is / is not agent-owned: the decisive challenge is generated by a separate autonomous reviewer actor, not by deterministic evaluation alone or by the original producer's self-check. The orchestrator only routes evidence and enforces the returned verdict.
- Evidence: [`src/main/harness/orchestrator/team-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/team-service.ts); [`src/main/harness/orchestrator/orchestrator-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/orchestrator-service.ts); [`src/main/harness/orchestrator/task-context-builder.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/orchestrator/task-context-builder.ts); [`src/shared/types/harness.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/shared/types/harness.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic Run Evaluation is not counted as S3* ownership. The positive finding relies on the distinct reviewer-agent path and corrective return loop.
- Claim being audited: the executor agent's implicit claim that the bounded task output/artifacts satisfy the task and are ready to pass the review gate.
- Ordinary reporting path: executor run state, task status, produced artifacts, run/evaluation summaries and normal completion reporting recorded by the orchestration/run services.
- Complementary access path: the reviewer receives a separately constructed review context with the task and produced evidence/artifacts rather than merely accepting the producer's completion status.
- Independence boundary: `isReviewer` is a distinct orchestration-agent role/session from the executor; the reviewer makes its own model judgment while deterministic orchestration code transports evidence and enforces the verdict.
- Who acts on findings: the orchestrator prevents accepted completion on rejection and preserves the review summary so a retried executor receives the finding as explicit corrective context.

## S4 — Outside-and-then adaptation

- State: C(P)
- Function: sense changes/options in the external Pi capability ecosystem and adapt the installed capability set for future Pi work.
- Disturbance / variety regulated: the external package/skill ecosystem changes over time as packages, versions and capability options appear or update, while the installed capability set can become insufficient or outdated.
- Decisive decision or feedback right: choose whether a discovered external package/capability or available update should be installed/updated/removed so future agent sessions operate with a changed capability repertoire.
- Decision owner: base constructor mode — first-party registry/search/update/install services expose the complete adaptation path but no autonomous adoption controller is packaged. Parent mode — the human operator selects capabilities/updates through the shipped Capabilities/package-management UI.
- Supporting / enforcement mechanisms: `PiPackageRegistry`, package detail/search and update checks, curated capability collections, `SkillsService` install/update/remove methods, IPC exposure and capability-management renderer state.
- Closure path: Pi-Harness queries external npm registry/package metadata and installed-version state → surfaces capability/update options → controller/operator selects an adaptation → first-party package/skill manager installs or updates it → subsequent Pi sessions discover/use the changed installed capability set.
- Boundary reachability: external registry search, package detail/update checks and install/update operations are first-party runtime services exposed through normal IPC/UI; no repository-development workflow is needed.
- Why this is / is not agent-owned: the system can sense the external capability environment and execute adoption, but the standard distribution does not supply an autonomous actor that decides which capability change to accept. It therefore exposes a constructor mode and a closed parent-governed mode rather than `A`.
- Evidence: [`README.md`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/README.md); [`src/main/packages/pi-package-registry.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/packages/pi-package-registry.ts); [`src/main/services/skills-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/services/skills-service.ts); [`src/preload/index.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/preload/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary run replay, checkpoints and baseline regression analysis are current/past operational feedback, not sufficient S4 by themselves. The positive S4 mapping relies on the explicit external package-registry/update path and return into future capability.
- External distinction: `PiPackageRegistry` calls the external npm registry/search/download services rather than merely reading internal run history.
- Future / prospective distinction: registry search and installed-package update checks identify capability/version options that can change what later Pi sessions can do, rather than only explaining a current run.
- Adaptation option generated: search/detail/update-check results identify installable packages or concrete newer versions, while curated capability collections expose supported capability choices.
- Path back into current capability / S3: selected packages/skills are installed or updated through first-party management services; the installed capability set is then available to subsequent Pi operation and remains operator-manageable through the control plane.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous capability/adaptation controller must be composed | external registry search/update information indicates a relevant new or changed capability | controller uses the first-party package search/detail/update/install interfaces; installed capability state changes and later Pi sessions can use it | `src/main/packages/pi-package-registry.ts`; `src/main/services/skills-service.ts`; `src/preload/index.ts` |
| Parent (`P`) | Pi-Harness operator | operator sees a capability option or available update and decides it should change the installation | operator installs/updates/removes via the shipped capability-management path; package/skill state changes for subsequent operation | `README.md`; `src/main/services/skills-service.ts`; renderer capability store/UI |

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party installation-level identity/ultimate-policy closure path is established at the reviewed boundary.
- Disturbance / variety regulated: Pi-Harness has tool/file/git/network policies, model/provider configuration, orchestration templates and user confirmations, but these govern operational permissions/capabilities rather than resolving a question of what the system ultimately is, whom it serves or which identity-defining policy takes precedence.
- Decisive decision or feedback right: not established for an S5 identity/ultimate-policy issue.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `PolicyEngine`, interactive `ask` confirmations, provider/model preferences, team/template configuration, package/capability management and ordinary application settings are inspected but not promoted to S5.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: there is no established S5 function to assign. Human configuration authority alone does not become `P` unless a material identity/ultimate-policy issue is surfaced, decided and returned to operation.
- Evidence: [`src/main/harness/policy/policy-engine.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/harness/policy/policy-engine.ts); [`README.md`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/README.md); [`src/main/services/skills-service.ts`](https://github.com/wangmiaozero/pi-harness/blob/efed4bd8d01505ae5fc8a52de243af7a3827ec39/src/main/services/skills-service.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: policy controls are materially important but remain inside-and-now operational constraints; capability adoption is mapped to S4. Neither becomes S5 merely because an operator can configure it.

### Absence scope

- Surfaces inspected: Harness policy engine and policy UI; provider/model configuration; tool/file/git/network/budget controls; team/agent templates; orchestration control; package/skill capability management; application settings and user confirmation paths described by the shipped desktop runtime.
- Plausible first-party paths checked: policy allow/ask/deny configuration, dangerous-command confirmation, provider/model choice, orchestration/team identity labels, package/skill adoption/removal, application update/configuration and reviewer gates.
- Why no material first-party path remains: these paths regulate operational permissions, current control, quality challenge or future capability, but the reviewed distribution does not surface an identity/ultimate-policy conflict together with an ultimate authority and return-to-operation closure.
