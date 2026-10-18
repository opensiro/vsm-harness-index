---
harness_id: lean-coder
project_name: lean-coder
repository: https://github.com/codemonkeying/lean-coder
review_ref: f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# lean-coder

## Review boundary

- System in focus: installed stdlib-based lean-coder CLI coding agent, its first-party `lean_coder.py` model/tool loop, core file/shell tools and explicitly enabled optional worker-dispatch/task-board tools.
- Purpose and identity: perform user-requested repository inspection and modification under operator permission, and in optional driver mode organize autonomous child workers against a dependency-aware shared task board.
- Relevant environment: local working tree, model provider (Ollama or optional hosted), operating-system shell, sessions/config directory, optional MCP/SSH and board-sidecar state.
- Standard-distribution boundary: packaged core `lean_coder.py`, `lean-tools/builtins.py` and optional first-party `dispatch_worker`, `board` tools when enabled, not a generic arbitrary user-developed plugin.
- Credited operating / distribution surfaces: [README](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/README.md); [coding loop and claims](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [built-ins](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/builtins.py); [worker dispatch and path claims](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/dispatch_worker.py); [named DAG task board](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/board.py); [opt-in tool boundary](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/README.md); [mock tests](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/tests/_mocktest.py); [smoke tests](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/tests/_smoketest.py).
- Adjacent first-party surfaces excluded from ownership: repo CONTRIBUTING and hook/CI gates, roadmap, example provider/tool modules and third-party MCP servers. Opt-in tools must be explicitly activated, and user-created extension behavior is not automatically attributed to base CLI.
- First-party operating / deployment modes considered: solo coding agent with permissions; explicit `dispatch_worker` bounded subprocesses; optional driver `board` DAG and worker file claims; provider switching, remote SSH and session compaction as support.
- Recursion level: one root coding agent with optionally spawned model-backed child S1 workers, shared task-board view, atomic edit-path claims and worker completion return. Bare standalone solo model mode is operational S1 only.
- Reviewed revision: `f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[lean_coder.py](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py) implements the ordinary provider-backed coding agent, tool calling, compact context and local session state. Built-in [file/shell tools](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/builtins.py) execute model-directed local actions through the configured leash and approval modes. The optional [dispatch_worker](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/dispatch_worker.py) starts separate worker-agent processes with limited permissions, execution budget and explicit claim/release/list tools. The core's [_board_claim and _board_read_claims](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py) uses an append-only first-claim-wins record per path and TTL, returning REFUSED to a competing worker that attempts to claim a file another active worker holds; this is a concrete cross-worker edit-interference attenuation path, not merely communication.

The opt-in [board](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/board.py) routes model-selected driver-only create/add/assign/cancel actions to [_taskboard_mutate and task dependencies](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py), while workers may mark their own completed/failed task and the board returns ready dependents. A driver agent can see current assignees, ready/dead branches and statuses, alter assignments, ping live peers or resume dormant sessions, and reconcile completed results. The model chooses organization-wide present task allocation; the board's serialized mutation, status checks, assignee notifications and file-claim arbitration enforce or communicate those choices. Optional `/board` is read-only except deletion and is not automatically an equivalent human-owned strategic-manager mode.

## Operational model

The main coding loop governs its own immediate task. The optional workforce mode creates distinctly executing model S1 workers, a first-party path-specific S2 conflict arbiter and a driver model with current multi-worker task/assignee view and operative reassignment authority. Peer notifications return outcomes to the assigning driver, including completed/failed and blocked dependencies, so management can choose another task. Neither optional worker named review nor model self-testing automatically constitutes a separate complementary audit authority. Configuration, model switching and context compaction are not VSM future-strategy decisions.

## S1 — Operations

- State: A
- Function: Perform context-sensitive coding through model-selected file reading, editing, search and shell actions with actual execution feedback.
- Disturbance / variety regulated: Unknown source layout, failed edits/commands, dependency/test failures and context pressure.
- Decisive decision or feedback right: Active root/worker coding model picks next tool action from observed real output.
- Decision owner: Native lean-coder agent using provider inference in the integrated model/tool feedback loop.
- Supporting / enforcement mechanisms: Provider adapter, small tool registry, confirmation leash, session history/compaction and worker execution limits.
- Closure path: User goal → model-selected action → file/shell/tool result → model receives result → next action or reply.
- Boundary reachability: Supported `lean_coder` executable drives coding tools and optional model-backed dispatched workers.
- Why this is / is not agent-owned: Permissions and tool registry alone cannot select appropriate coding steps; context-dependent choices require the active model.
- Evidence: [main loop](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [tools](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/builtins.py); [standard modes](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/README.md).
- Basis: structural and explicit
- Confidence: high for source-level reachability; no provider-backed test executed here
- Caveats: User approval/sandbox, provider availability and optional tool activation constrain the reachable actions.

## S2 — Coordination

- State: C
- Function: Attenuate concurrent edit interference when two real S1 worker processes target the same repository file.
- Disturbance / variety regulated: Two workers selecting the same path for edits could overwrite each other's uncommitted work.
- Decisive decision or feedback right: First-claim-wins append-only path claim log deterministically identifies one live owner with TTL; second claimant receives an explicit REFUSED and instruction to choose other work or wait.
- Decision owner: Constructor-written file claim resolution; no agent chooses the arbitration policy dynamically, hence C rather than A.
- Supporting / enforcement mechanisms: Session-scoped claims.jsonl, atomic append-order reduction, TTL/release and `dispatch_worker` board_claim/board_release/board_list tools.
- Closure path: Two child S1s request same file → claim log resolves live winner → loser is REFUSED and instructed not to edit → next worker tool choice can avoid collision.
- Boundary reachability: Optional first-party `dispatch_worker` provides file claim tools to actually executing worker subprocesses and routes them to core claim reducers.
- Why this is / is not agent-owned: Constraint is deterministic and model obeys conflict signal; a model is not responsible for selecting the winner or negotiating an alternate policy.
- Distinct S1 units: Separate worker agents executing under shared driver run with their own provider turns and file tools.
- Inter-S1 disturbance: Concurrent edits to the same project file.
- Attenuating coordination relation: First-live-claim file reservation with conflict rejection and timeout/release.
- Feedback into subsequent S1 behaviour: Loser receives REFUSED with holder and must choose different file/work or wait, avoiding same-path edit attempt.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit claim tool detects a concrete contested path, refuses a conflicting operation and communicates a changed action constraint, rather than just queueing unrelated tasks.
- Evidence: [_board_claim and reducer](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [_worker_board tools](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/dispatch_worker.py).
- Basis: structural
- Confidence: high on concrete conflict-rejection path; no proof workers cannot bypass opt-in claims
- Caveats: Soft cooperative reservation: workers may ignore claim tools, and file edits are not universally kernel-locked.

## S3 — Inside-and-now control

- State: A
- Function: Manage active worker commitments and current organization-level assignment readiness across a bounded coding team.
- Disturbance / variety regulated: Multiple delegated workers and dependencies create unfinished, blocked, failed and ready work that requires reassignment/integration and active notifications.
- Decisive decision or feedback right: Root driver model chooses create/add/assign/cancel, reads board readiness/work results and responds to completion/dead-branch notifications, potentially dispatching/resuming a peer for changed current commitments.
- Decision owner: Model-driven driver acting over worker S1s; deterministic locks, notifications and DAG status enforcement are supporting control plane machinery.
- Supporting / enforcement mechanisms: Driver-only task board interface, atomic _taskboard_mutate, persisted task DAG/assignee/assigned_by, peer status and wake, result reconcile, worker dispatch.
- Closure path: Board current task/worker view → root agent chooses worker and ready work, pushes assignment → worker acts and marks outcome → assigner woken with results/dead dependents → root model updates later tasks/assignments.
- Boundary reachability: Opt-in first-party board and worker plugins are loaded by the supported CLI; the driver is the model owner of create/assign/cancel and can reach actual worker processes.
- Why this is / is not agent-owned: Root model exercises current multi-worker assignment and repair discretion; board rule enforcement alone would not pick work or priorities.
- Whole-system current view: Named board lists all task statuses/assignees, dependencies and peer liveness; /worker status and board result are available for the present run.
- Current-control decision scope: Create/update current commitments, assign to running/dormant worker, cancel, detect failing blocked branch and reconcile actual subtask outputs.
- Evidence: [board driver actions and return notifications](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/board.py); [_taskboard_mutate/ready](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [workers and resume](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/dispatch_worker.py).
- Basis: explicit and structural
- Confidence: medium-high for supported opt-in team mode; operational performance untested
- Caveats: No distinct parent-governed P mode credited: operator status/read commands and manual kill don't establish equivalent whole-team discretionary governance.

## S3* — Complementary audit

- State: —
- Function: No integrated complementary reality-sampling audit authority returning findings to whole-current management is demonstrated.
- Disturbance / variety regulated: Wrong code or incomplete worker reports can be checked by routine tests, code review user requests or a delegated reviewer, but none is first-party required independent operational audit wiring.
- Decisive decision or feedback right: Root model/worker can inspect source and request another agent; no separate sampled evidence and audit judgment closure is established by the default or enabled worker contracts.
- Decision owner: Ordinary coding S1/manager or user for ad-hoc review; no distinct S3* decision owner.
- Supporting / enforcement mechanisms: Worker transcript/result pages, named review role, git summary and diagnostics, demo audit.
- Closure path: Optional review tool result returns to requester like any ordinary delegated S1 result, without independent auditor requirement → S3 control return contract.
- Why this is / is not agent-owned: A label `review`, a separate model instance, or routine code/test tools are insufficient to infer a complementary independent audit.
- Evidence: [worker contract](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/dispatch_worker.py); [worker status/result](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/board.py); [coding demo](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/README.md).
- Basis: structural
- Confidence: medium-high for standard mode
- Caveats: A newly configured independent reviewer could be composed externally, but not inferred from generic worker semantics.

### Absence scope

- Surfaces inspected: Worker setup and role delegation, taskboard reports, optional tools and test/demo.
- Plausible first-party paths checked: Distinct sampled primary source access vs producer claims, independent audit verdict, returned current-management correction.
- Why no material first-party path remains: Standard worker dispatch doesn't enforce a separated independent inspection/audit-to-manager loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future/environment-facing intelligence and capability-adoption loop connected back to current-team control is demonstrated.
- Disturbance / variety regulated: Provider and tooling options, remote SSH and compaction can change, but these are operator-selected capabilities or current-task context.
- Decisive decision or feedback right: Operator installs/enables providers/tools; model acts on present coding requests rather than a prospective organizational adaptation remit.
- Decision owner: Human for capability configuration, ordinary coding agent for local task decisions.
- Supporting / enforcement mechanisms: Providers, optional update tool, web search, code/project context compaction.
- Closure path: Operator changes provider/tool → coding agent executes with newly configured resource. Missing future environment scan, option evaluation and adoption decision returning into S3.
- Why this is / is not agent-owned: Context summarization, present-task research and tool installation do not by themselves establish S4.
- Evidence: [provider/runtime](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [provider/update model](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/README.md); [update optional tool](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/update.py).
- Basis: structural
- Confidence: medium-high
- Caveats: External governance or custom research workflows are outside product standard boundary.

### Absence scope

- Surfaces inspected: Provider selection, update tool, web search, skills, session memory, optional plugins.
- Plausible first-party paths checked: Future-external sensing and prospective capability alternatives decided by an authority with return into current control.
- Why no material first-party path remains: No proven closed outside-and-then adaptation channel rather than configurable current execution.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate organizational identity/constitutional policy arbiter returns binding decisions into the whole continuing worker organization.
- Disturbance / variety regulated: Leash modes, approval settings and worker-depth constraints control tool safety and recursion, not ultimate collective purpose.
- Decisive decision or feedback right: Operator approves commands or edits and sets tool availability; deterministic software applies them.
- Decision owner: Human for permissions/tool configuration; runtime for enforcement, not S5 ultimate policy.
- Supporting / enforcement mechanisms: Leash levels chat/r/rw/rwe, ask/session/auto approvals, tool capability ceiling, security controls, driver-only board operations.
- Closure path: User configuration/permission → individual tool allowed/denied, not identity-level dispute → legitimate decision → organization policy return.
- Why this is / is not agent-owned: Tool access and prompt role labels do not confer ultimate constitutional authority.
- Evidence: [Safety section](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/README.md); [permissions](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean_coder.py); [driver-only role controls](https://github.com/codemonkeying/lean-coder/blob/f143f85344c0b0e5b3dcb68b5a1f884ac1c5ec63/lean-tools/board.py).
- Basis: structural
- Confidence: high on inspected modes
- Caveats: Maintainer OSS governance remains outside runtime.

### Absence scope

- Surfaces inspected: Approval/leash, board role restrictions, provider/tool selection, repo maintainer guidelines.
- Plausible first-party paths checked: Ultimate policy/identity conflict, legitimate deciding authority and binding whole-system return.
- Why no material first-party path remains: Available controls enforce operational tool privileges and role restrictions, not organizational identity decisions.
## Recursion

The standard opt-in driver + spawned worker configuration contains distinct task-level autonomous S1s. The path-claim S2 attenuates edit collisions between them; driver-only board controls and completed-worker return leg support current whole-team S3 ownership in the model, whereas base solo mode has only S1. This is not a claim of S3 or S2 for every default installation.

## Variety and escalation

A conflicting file claim is refused and a worker can change its next operation rather than corrupt concurrent edits. Failed board dependencies are surfaced back to the assigning agent with return notifications, including dormant-session wake. General user tool approval is unrelated to the S5 function. A failed task or alert alone is not an algedonic channel without separately established receiving authority.

## Evidence gaps

- Pinned static source-first review, not a fresh paid-provider end-to-end task trace.
- S2=C assumes cooperative use of exposed file-claim tools; no claim that every file-edit primitive has an unconditional lease enforcement gate.
- S3=A is claimed only for the opt-in first-party driver/board multi-worker topology, not solo coding or simple worker dispatch in isolation.
- No independent operational audit reviewer, prospective external-adaptation loop, or ultimate identity governance path was evidenced within the reviewed distribution.
