---
harness_id: forcecode
project_name: ForceCode
repository: https://github.com/samansarmasik-alt/forcecode
review_ref: 518672e170f570f59c2d2abdeb4b5cf148e1603b
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ForceCode

## Review boundary

- System in focus: shipped Python ForceCode terminal coding agent and first-party standard managed-team, persistent terminal-fleet, ForceFlow, Mission Control, and VibeCode execution modes, not the developer's GitHub project governance.
- Purpose and identity: autonomously inspect, edit, build and test local projects; optionally distribute bounded investigation across read-only specialist AIs, manage current worker assignments/integration, and verify acceptance through an independent final read-only review and repair.
- Relevant environment: local workspace and project test/build tools, model-provider APIs, user-selected trust/approval settings, atomic .forcecode task/mission/team state, optional sandbox, user commands and persisted sessions.
- Standard-distribution boundary: executable ForceCode CLI/REPL `forcecode.py` and first-party supporting queue/store/workspace/sandbox modules, including explicit `--team`, `/terminal`, `/mission`, `/vibe` modes; provider and plugins remain supporting inputs.
- Credited operating / distribution surfaces: [README and team/VibeCode usage](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md); [Agent / TeamBoard / TerminalFleet / VibeCode implementation](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [TaskQueueStore](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode_queues.py); [MissionView read-model](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/_forcecode_mission.py); [ForceFlow execution semantics](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/FORCEFLOW.md); [Mission Control scope](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/MISSION_CONTROL.md); [sandbox](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode_sandbox.py); [test surface](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/tests/test_forcecode.py).
- Adjacent first-party surfaces excluded from ownership: GitHub release workflows, development specs, changelogs, maintainer security policy, demos/benchmarks and external services. Provider switching, terminal skins, web browsing and model performance claims do not independently establish VSM managerial functions.
- First-party operating / deployment modes considered: normal coding-agent turn; bounded tool/ForceFlow sequence; managed team of manager plus up to three read-only specialists; persistent terminal fleet with model-action only on explicit user team authorization and direct /terminal operator controls; long-session /vibe with built-in independent final reviewer and repair.
- Recursion level: the live managed team (manager plus multiple separately executing model/tool S1 specialists) at the collaboration recursion, and the single coding session in solo mode. VibeCode is an alternative first-party mode with a separate complementary audit branch.
- Reviewed revision: `518672e170f570f59c2d2abdeb4b5cf148e1603b`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[ForceCode Agent](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py) provides a model-directed coding tool loop with real execution, verified artifact receipts and sandbox/permission boundaries. [TaskQueueStore](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode_queues.py) persists bounded ForceFlow tasks and verification state; [ForceFlow contract](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/FORCEFLOW.md) requires evidence before progressing to the next item and adds root-cause repair tasks when verification fails. [MissionView](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/_forcecode_mission.py) projects existing queue receipts, not a second autonomous planner or controller.

The first-party [TeamBoard](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py) creates a shared, file-locked team run, persists manager/worker assignments and worker reports, and exposes current phase/report context. `run_managed_team` invokes a model for specialist allocation, executes up to three separate read-only child AIs, publishes their reports to the board, waits for the synchronization barrier, then resumes a manager Agent with the complete current results and authority to inspect/edit/verify integration. The persistent [TerminalFleet](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py) separately exposes role/queue/active-task/report/status records for up to four terminals, uses a file lock for claims/updates and gives each worker a distinct queued assignment; `/terminal` exposes explicit operator allocation/retirement while model orchestration is gated by explicit user team intent.

[VibeCode](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py) executes a checkpointed long plan with deterministic local verification, followed by `run_vibecode_review`: it creates a **separate read-only Agent** with no saved conversation, instructs it to independently inspect actual project files against the objective, and parses its independent evidence-based judgment. A failing verdict with gaps appends repair tasks to the live work queue; another quality pass follows repair, and passing verification is required for final completion. This is complementary operational sampling and corrective feedback, not merely a status label.

## Operational model

The coding model autonomously selects task steps and tool actions. In managed-team mode, distinct read-only specialists inspect their assigned work independently while the manager owns current integrated assignment/resource choices and later incorporation of reports. Native queue claim/file-lock mechanics prevent concrete concurrent board or per-terminal task-claim clashes without asking a model to arbitrate: a narrow first-party S2 construction path rather than autonomous S2 discretion. The root manager's live multi-worker control can be model-owned or manually exercised by the human operator via the shipped terminal fleet interface. VibeCode adds independently sampled operational reality and a returned repair decision path. Provider/model selection, permissions and package/extension configuration remain separate from organizational policy or long-horizon strategy.

## S1 — Operations

- State: A
- Function: Perform uncertain coding tasks with model-selected repository inspection, editing, verification and repair actions.
- Disturbance / variety regulated: Changing code requirements, project-specific tools, failed commands, missing artifacts and model/provider interruptions.
- Decisive decision or feedback right: The active coding model or each independent read-only teammate chooses its next task-level tool action based on observed result.
- Decision owner: First-party Agent model loop and child models, with deterministic tool/sandbox enforcement.
- Supporting / enforcement mechanisms: WorkspaceTools, ForceSandbox, model/provider interface, project artifact receipts, retry policy, process/session controls and task queue.
- Closure path: Developer objective → AI tool/plan step → real file/shell/test result → observed evidence returned → next model decision or verified completion.
- Boundary reachability: The shipped `Force` and `forcecode.py` entrypoint invokes the normal Agent; `--team`/VibeCode instantiate the same first-party model/tool operating loop.
- Why this is / is not agent-owned: The model chooses situational coding operations; static test gates cannot decide which change to make.
- Evidence: [Agent and managed-team run](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [execution/kernel](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/FORCEFLOW.md); [supported CLI](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md).
- Basis: explicit and structural
- Confidence: high on reachable tool/result closure; live provider efficacy not reproduced
- Caveats: Permissions and sandbox may forbid tool actions; completed tasks require prescribed verification.

## S2 — Coordination

- State: C
- Function: Attenuate concrete concurrent-claim and shared-board state collisions between independently running worker terminals in the shipped terminal fleet.
- Disturbance / variety regulated: Two worker processes or actor threads could otherwise simultaneously read/update shared worker queues and reports, lose one another's updates or duplicate a claimed assignment.
- Decisive decision or feedback right: Native exclusive file lock and atomic queue pop allow only one claimant/board mutation at a time; a worker receives only its claimed task and other terminals see updated state.
- Decision owner: Deterministic first-party queue/board primitives, not an autonomous actor choosing adaptive cooperation policy. The broader coordination response requires a composed manager/operator: C, not A.
- Supporting / enforcement mechanisms: TerminalFleet._file_lock, active_task/queue status, TeamBoard._lock and publish, shared report context and manager barrier.
- Closure path: Concurrent attempts to mutate board or claim task → serialized lock/claim → one valid task assignment/update published → workers subsequently see distinct queued tasks/current reports rather than duplicate/lost state.
- Boundary reachability: Persistent terminal fleet is an explicit built-in `/terminal` and worker mode; manager and workers share these first-party records with real worker claim/publish calls.
- Why this is / is not agent-owned: File/queue locking and task claims apply fixed concurrency constraints; model discretion is for task assignment and report integration, not the lock arbitration.
- Distinct S1 units: Separate model-backed worker terminals, each with its own read-only operative loop and queued assignments in persistent fleet mode.
- Inter-S1 disturbance: Concurrent worker attempts to claim/edit shared queue/board state and overlapping assignment acquisition.
- Attenuating coordination relation: Exclusive file lock during queue pop/report publish with one active_task per worker, plus synchronized manager phase/report board.
- Feedback into subsequent S1 behaviour: Each terminal executes only its claimed task; next claim observes queue after prior mutation; manager sees updated reports for integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The mechanism actively prevents lost-update and duplicate-claim interference across concurrent first-party workers rather than merely transporting messages.
- Evidence: [TerminalFleet.claim/publish and TeamBoard locks](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [fleet mode documentation](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md).
- Basis: structural
- Confidence: medium-high for bounded shared-resource contention; no broader edit-conflict arbitration asserted
- Caveats: Read-only specialists also limit file-write interference; no native general semantic conflict/oscillation resolution is demonstrated.

## S3 — Inside-and-now control

- State: A(P)
- Function: Exercise whole-current managerial authority over live specialist workforce, assignment priorities, report integration and corrective action.
- Disturbance / variety regulated: Multiple worker roles/queued jobs/results need coherent present commitments; integrated changes must be prioritized, verified or redone, and worker lifecycle may need adjustment.
- Decisive decision or feedback right: In autonomous managed-team mode the model selects distinct specialist assignments from the objective, observes shared reports at the barrier, then decides concrete integration edits and verification. In parent mode the operator sees fleet status and uses /terminal add/task/configure/remove to change current live commitments.
- Decision owner: Root manager model for A mode; legitimate terminal operator for separate P mode. TeamBoard/TerminalFleet enforce state changes but do not make discretionary whole-team judgments.
- Supporting / enforcement mechanisms: TeamBoard phase/reports, run_delegations supervisor, manager-only integration pass, TerminalFleet running roles/queues/states, dedicated /terminal commands.
- Closure path: Manager views assignment plan and results → modifies worker commitments or integrates/fixes/validates current work → subsequent source state or worker tasks change; operator actions similarly mutate live fleet queues and active membership.
- Boundary reachability: Built-in `--team` and `/team` managed mode and `/terminal` persistent fleet; model fleet action is explicitly user-authorized, and same first-party registry implements human command mode.
- Why this is / is not agent-owned: Model chooses current workforce assignments and integrated corrective action in one legitimate mode; parent can independently exercise current whole-team control in a separate supported mode, so A(P), not automatic S3 in solo turns.
- Whole-system current view: Shared TeamBoard assignments/reports/phase plus TerminalFleet active_task, pending queues, current worker PID/status/report records.
- Current-control decision scope: Allocation of specialist responsibilities and current worker resources, termination/reassignment, multi-worker integration and verification of collective outcome.
- Evidence: [run_managed_team, TeamBoard, TerminalFleet](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [headless/interactive managed team modes](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md); [mission read-state boundary](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/MISSION_CONTROL.md).
- Basis: explicit and structural
- Confidence: medium-high for code-reachable mode; effective multi-agent performance not experimentally verified
- Caveats: Ordinary single-agent ForceFlow remains S1-level work. `MissionView` only projects work state; it is not independently credited as S3.

### S3 ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root manager model of multi-worker team | User-authorized managed-team request; specialist planning/report barrier or current fleet action | Model chooses allocation/worker action/integration after team-wide report context, applies edits and verification | [run_managed_team and TerminalFleet](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py) |
| Parent (`P`) | Human operator controlling live multi-terminal workforce | /terminal status, add, task, configure or remove | Human changes current workers, assignment queues and limits; workers observe changed tasks/state and report back | [TerminalFleet and /terminal command routing](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py), [operator commands](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md) |

These are separately supported ownership modes, not simultaneous dual authority. Model-controlled fleet action requires explicit user team authorization; this constraint does not eliminate autonomous team-level discretion within the admitted mode.

## S3* — Complementary audit

- State: A
- Function: Obtain independently sampled operational artifact evidence and a distinct reviewer judgment to challenge the completed VibeCode task outcome.
- Disturbance / variety regulated: The implementing agent may report success despite placeholder code, broken UX, missing tests, unsafe integration or package/build defects.
- Decisive decision or feedback right: A separate read-only model reviewer examines actual project files and selects acceptance/failure findings; parsing enforces output shape, while the executing VibeCode loop returns its gaps as repair work.
- Decision owner: Independent read-only reviewer Agent in first-party VibeCode completion mode; main coding agent acts on findings but does not author the audit verdict.
- Supporting / enforcement mechanisms: run_vibecode_review separate Agent with read_only=True/no history persistence, deterministic project-wide gate, typed pass/score/gaps format, parse_vibecode_review and ForceFlow repair queue.
- Closure path: Coding/verification receipts → separate reviewer instructed to inspect important files for missing implementation/integration/test evidence → independent structured gaps/pass → if failed append repair items and re-run implementation/quality loop; if accepted complete and persist report.
- Boundary reachability: Shipped `/vibe` and `/mission long` paths invoke built-in run_vibecode_review as final acceptance stage of the actual VibeCode loop.
- Why this is / is not agent-owned: The reviewer model generates source-informed judgment; deterministic JSON parsing and workqueue enforcement do not decide which defects exist.
- Claim being audited: Main agent's completion/acceptance claim for the objective and implementation status.
- Ordinary reporting path: Implementer tool/test receipts, task queue status, changed-file list and deterministic local gate.
- Complementary access path: Separate read-only Agent with its own context directly inspects project files against the objective and catches defects not established by normal receipts.
- Independence boundary: Reviewer is a new read_only=True Agent, record_history=False and no permission to edit; it receives objective/test/task evidence but must independently read actual project artifacts.
- Who acts on findings: VibeCode current-control execution consumes gaps into repair queue, then root model implements fixes and repeats final review.
- Evidence: [run_vibecode_review and VibeCode repair loop](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [VibeCode documented mode](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md); [receipt and repair gate](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/docs/FORCEFLOW.md).
- Basis: explicit and structural
- Confidence: high for first-party independent feedback loop; actual review quality not independently benchmarked
- Caveats: This is the opt-in long-session VibeCode mode, not a blanket assertion that every solo turn has S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party closed external-and-prospective organizational intelligence loop distinct from current coding/verification and manual provider setup is proven.
- Disturbance / variety regulated: New provider capabilities, different project needs and tool ecosystem changes may matter; configurable providers and model routing do not show independently selected future adaptation programs.
- Decisive decision or feedback right: Operator chooses provider/model and package configuration; active coding agent can research the present task, not demonstrably decide future organizational capability in an S4→S3 relationship.
- Decision owner: Human for config/product update, coder for current task; no distinct S4 authority.
- Supporting / enforcement mechanisms: Model selection, provider profiles, graph/repo intelligence, web lookup, skill loading, mission/vibe planning and snapshots.
- Closure path: Config or task feedback → current model/operations; no outside-horizon scan → adaptation option → authority decision → returned changed team capability.
- Why this is / is not agent-owned: Current task planning, self-repair and model selection do not count as future/environment S4 without the required prospective coupling.
- Evidence: [provider model and Agent loop](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [configuration](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode_config.py); [model and extension controls](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: External user-managed upgrades or research may do this, but are not the reviewed shipped organizational path.

### Absence scope

- Surfaces inspected: Provider/profile tooling, ForceGraph/repo search, task planning, VibeCode cycle and release/governance documents.
- Plausible first-party paths checked: External-future distinctions, capability options beyond current task, adoption judgment, returned organization-wide capability change.
- Why no material first-party path remains: Inspected features repair and improve the current job or expose operator-configurable resources; no attributable closed future-oriented loop.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate organizational purpose/constitutional policy adjudication loop with a returned whole-system mandate is demonstrated.
- Disturbance / variety regulated: Safety sandbox, model_lock, tool approval and read-only workers govern execution privilege, not the organization's ultimate identity.
- Decisive decision or feedback right: Operator approves potentially risky actions and chooses provider/model, while deterministic sandbox enforces bounds; no distinct S5 identity owner.
- Decision owner: Human for local trust and model choices, fixed runtime policy for enforcement.
- Supporting / enforcement mechanisms: ForceSandbox, Smart Autopilot, model_lock, worker role privilege, app config, redaction and workspace safety controls.
- Closure path: Selected permission/model policy → restricted/approved tool; missing ultimate-policy issue → legitimate S5 decision → binding returned organization identity mandate.
- Why this is / is not agent-owned: Enforcing a local safety rule or choosing a product role is not constitutive identity governance.
- Evidence: [sandbox](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode_sandbox.py); [agent/fleet permission constraints](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/forcecode.py); [project security policy](https://github.com/samansarmasik-alt/forcecode/blob/518672e170f570f59c2d2abdeb4b5cf148e1603b/SECURITY.md).
- Basis: structural
- Confidence: medium-high
- Caveats: Repository contributor policy and operator institutions are external to the running ForceCode team.

### Absence scope

- Surfaces inspected: Safety flags, sandbox, Smart Autopilot, tool approvals, model lock and contributor/security documents.
- Plausible first-party paths checked: Legitimate ultimate-policy disputes, identity arbitration and binding returned decision to subsequent operating team.
- Why no material first-party path remains: Available constraints control individual actions/worker privileges, not constitutional identity decision rights.
## Recursion

The managed team comprises a managerial root and independent read-only specialist S1s; terminal workers have distinct sessions and queued task identities. S2's claim/board contention control is lower-level enforcement between these real operatives, whereas S3 is the manager/parent current orchestration right. VibeCode's independent auditor samples code reality at a complementary path and returns repair proposals; it is not merely another normal implementation worker. Solo-mode coding and sequential ForceFlow task list remain S1.

## Variety and escalation

Failed verification blocks a subsequent ordered ForceFlow task and may trigger bounded root-cause repair; a status alone is not an algedonic function. Team-board queue contention is serialized to prevent duplicate claims/lost state. In VibeCode, reviewer-raised gaps turn into new current repair commitments before completion. Safety/auth limits remain ordinary bounded enforcement, not S5 authority.

## Evidence gaps

- This is source-first architecture/contract analysis at one immutable Git SHA; no separate paid-model live trace or production reliability experiment executed.
- S2=C applies narrowly to shared board/assignment write contention, not all possible concurrent edit conflicts. The team specialists are read-only, and their differing recommendations are integrated by S3 manager.
- S3=A(P) is only credited to explicit real multi-worker managed team/fleet mode, with model and human ownership documented separately.
- S3*=A is first-party VibeCode independent read-only review with potential remedial feedback; no claim of cryptographically sealed independent reviewer or automatic independent OpenSiro assessment reviewer is implied.
