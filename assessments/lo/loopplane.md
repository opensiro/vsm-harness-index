---
harness_id: loopplane
project_name: LoopPlane
repository: https://github.com/LJC-FVNR/LoopPlane
review_ref: 0798233a1d1e3d9058c491aaeffb32575966004d
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# LoopPlane

## Review boundary

- System in focus: one local LoopPlane durable project-workflow organization, including its shipped role contracts and supported configured CLI-agent composition.
- Purpose and identity: turn a user brief into reviewable, resumable project outcomes with evidence, validation and objective gates.
- Relevant environment: project files, local processes, operator requirements, installed/authenticated Codex or Claude Code and their model providers.
- Standard-distribution boundary: pinned Python runtime, CLI, portable skill and first-party prompt templates, instantiated in a target project. The native CLI's internal tool policy, inference implementation and own metasystem are dependencies.
- Credited operating / distribution surfaces: worker/recovery prompts and adapter execution; planning/change-request/control/read-model paths; optional long-running-background semantic inspector watchdog.
- Adjacent first-party surfaces excluded from ownership: release/package CI, showcase artifacts, fake CLI/noop/shell smoke fixtures, and repository-development governance. Machine-wide coordination between different project installations is outside this single-workflow recursion.
- First-party operating / deployment modes considered: installed skill with configured provider-backed runners; serial foreground/detached workflow; supervised dashboard/CLI change requests; optional background semantic-watchdog mode. Offline fixtures corroborate transport only.
- Recursion level: one project workflow with operational task/recovery cells, not an autonomous organization spanning all projects on the machine.
- Reviewed revision: `LJC-FVNR/LoopPlane@0798233a1d1e3d9058c491aaeffb32575966004d`; intake #2446 / controller #2447 row 1, original #201 row 1 unchanged.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/README.md); [SKILL.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/SKILL.md); [runtime/README.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/README.md) describe a stdlib Python control runtime plus an installable, first-party agent workflow. The worker is not merely a subprocess health check: [templates/worker_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/worker_prompt.template.md); [runtime/prompt_builder.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/prompt_builder.py); [runtime/adapters/codex_cli_adapter.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/adapters/codex_cli_adapter.py) bind a specific task, constraints and prior failures, authorize local repair, and require attributable deliverables/status. External CLI engines execute that owned role; their internal VSM functions are not imported.

[runtime/scheduler.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/scheduler.py); [runtime/detached.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/detached.py); [runtime/validation.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/validation.py); [runtime/reconciliation.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/reconciliation.py) implement task selection, leases, validation, authoritative plan reconciliation, background waits and recovery. [runtime/planning.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/planning.py); [runtime/change_requests.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/change_requests.py); [runtime/control.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/control.py) separate proposed intent from activated intent and operator-returned changes. JSON/JSONL state and derived dashboard views persist the workflow. [runtime/background_jobs.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/background_jobs.py); [runtime/inspector.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/inspector.py) launch a separate semantic inspection of raw job evidence and can stop a misleadingly healthy running process. Apache-2.0 applies at the pinned LICENSE. Shipped source, not a live credentialed inference run, is the evidence basis.

## Operational model

The supported installed mode supplies an agent-owned task transformation: task and previous evidence → role-bound agent selects edits/commands/repairs → durable evidence/status → validator/reconciler → later task or recovery. This first-party composition is stronger than an arbitrary command launcher but does not acquire the external engine's internal organization. The scheduler enforces task authority and completion rules. The human project owner retains whole-workflow commitment changes; independent inspector judgment can override process-health reporting in the optional watchdog mode.

## S1 — Operations

- State: A
- Function: Produce task deliverables and repair failures within the approved project work contract.
- Disturbance / variety regulated: Code/data/test failures, incomplete evidence and background execution.
- Decisive decision or feedback right: Choose task-local investigation, implementation and safe repair rather than mechanically execute a prechosen command.
- Decision owner: The worker/recovery agent instantiated by LoopPlane role contracts.
- Supporting / enforcement mechanisms: CLI adapters, generated context, status files, validator and reconciler.
- Closure path: Agent-produced artifacts/status enter authoritative validation and the next task/recovery prompt.
- Boundary reachability: The documented installed worker mode supplies the role prompt, adapter and result-to-recovery wiring after required CLI discovery/authentication.
- Why this is / is not agent-owned: The shipped task role explicitly grants local repair discretion. Removing the agent leaves scheduler/transport but no equivalent semantic implementation choice. Credit the role composition, not unexamined external CLI internals.
- Evidence: [templates/worker_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/worker_prompt.template.md); [templates/recovery_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/recovery_prompt.template.md); [runtime/prompt_builder.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/prompt_builder.py); [runtime/scheduler.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/scheduler.py); [runtime/adapters/codex_cli_adapter.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/adapters/codex_cli_adapter.py)
- Basis: structural
- Confidence: high
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.

## S2 — Coordination

- State: —
- Function: No additional inter-independent-S1 adjustment path established within one project workflow.
- Disturbance / variety regulated: Potential file, runner and background-job collisions were considered.
- Decisive decision or feedback right: No evidenced autonomous coordination decision at this recursion.
- Decision owner: Scheduler/developer rules; no separate agent coordination owner established.
- Supporting / enforcement mechanisms: Single active-work selection, leases, runner locks and background deduplication.
- Closure path: Sequential dependency enforcement and waiting preserve safe progress; they do not demonstrate a distinct inter-S1 adjustment loop within this workflow.
- Why this is / is not agent-owned: Parallel workers/multiple active-running workflows are explicitly deferred in the README. Machine-level runner locks regulate separate workflow installations, a different boundary.
- Evidence: [README.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/README.md); [runtime/scheduler.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/scheduler.py); [runtime/runner_locks.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/runner_locks.py); [runtime/background_jobs.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/background_jobs.py)
- Basis: structural
- Confidence: high
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.

### Absence scope

- Surfaces inspected: README supported/deferred scope, scheduler selection, runner locks and background state.
- Plausible first-party paths checked: Shared runner contention, duplicate background launches, dependency and scope control.
- Why no material first-party path remains: At this declared single-workflow recursion the shipped mechanisms serialize a task/recovery path; cross-project lock support is not borrowed as a fleet S2.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the current workflow commitments and intervene on behalf of the whole project.
- Disturbance / variety regulated: Changed priorities/scope, blocked work and unsafe or unwanted continued execution.
- Decisive decision or feedback right: Approve/reject whole-plan changes and issue current workflow control requests informed by authoritative state.
- Decision owner: The legitimate project operator in the supported supervised mode.
- Supporting / enforcement mechanisms: Read models/dashboard, planner-generated PLAN_PATCH, content-bound approval records and scheduler safe-point request application.
- Closure path: Operator sees whole plan/current task/job state → submits change → planner supplies patch → approval is bound to reviewed content → apply_approved_plan_patch changes active commitments; pause/resume/stop requests are recorded and applied before subsequent work.
- Boundary reachability: This is a supported project-runtime path, reached through the shipped CLI/dashboard or background-start options, not repository CI or a hypothetical plugin.
- Why this is / is not agent-owned: Parent owns the decisive commitment approval, while planner, scheduler, guards and snapshotting construct/execute it. Autonomous append-only objective-gap expansion does not establish autonomous whole-system resource bargaining.
- Evidence: [README.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/README.md); [runtime/change_requests.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/change_requests.py); [runtime/control.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/control.py); [runtime/scheduler.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/scheduler.py); [runtime/read_models.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/read_models.py)
- Basis: structural
- Confidence: high
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.
- Whole-system current view: active plan, task/evidence state, failures and background jobs in project dashboard/read models.
- Current-control decision scope: project commitments and authorized scope changes, with control returned to scheduling.

## S3* — Complementary audit

- State: A
- Function: Challenge a running background job’s apparent health with separate semantic inspection.
- Disturbance / variety regulated: Alive/heartbeat-successful processes may stall or produce evidence requiring recovery.
- Decisive decision or feedback right: Judge healthy_progress/recommended_status from raw launch/log/task evidence and trigger recovery or termination.
- Decision owner: A separate inspector agent run, not the worker whose progress is assessed.
- Supporting / enforcement mechanisms: Throttled watchdog trigger, allowlisted raw paths, result parsing, supervisor termination and registry/scheduler feedback.
- Closure path: _run_watchdog_check calls answer_inspection in a new run; a successful negative judgment sets stop_job; supervisor terminates the process and persists needs_recovery/failure for subsequent regulation.
- Boundary reachability: This is a supported project-runtime path, reached through the shipped CLI/dashboard or background-start options, not repository CI or a hypothetical plugin.
- Why this is / is not agent-owned: The semantic verdict is agent-owned. Deterministic parsing/termination enforce it; cheap process probes alone do not receive this state.
- Evidence: [runtime/background_jobs.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/background_jobs.py); [runtime/inspector.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/inspector.py); [templates/inspector_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/inspector_prompt.template.md); [tests/test_background_jobs.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/tests/test_background_jobs.py)
- Basis: structural
- Confidence: medium
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.
- Claim being audited: a still-running delegated process remains healthy enough to continue.
- Ordinary reporting path: process liveness, heartbeat and worker-provided agent_status/job state.
- Complementary access path: bounded direct job launch/log files and task evidence, beyond liveness/summary.
- Independence boundary: separately launched inspector context/output, no authority to rewrite background registry; shared provider is not claimed to ensure model diversity.
- Who acts on findings: background supervisor and scheduler; negative findings change job and later recovery state.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped organizational outside-and-then adaptation loop established.
- Disturbance / variety regulated: Environmental/future change, distinct from current objective gaps.
- Decisive decision or feedback right: No prospective capability-selection right evidenced.
- Decision owner: Task planners/recovery agents solve the current brief; project capability strategy is not supplied.
- Supporting / enforcement mechanisms: Persistent context, objective reports, self-expansion proposals and runtime source snapshots.
- Closure path: Self-expansion adds work to satisfy current objectives; source hot-reload follows externally changed code, not an owned environmental-option decision.
- Why this is / is not agent-owned: Learning/research task content is an operational outcome unless a first-party adaptation return into this organization is shown.
- Evidence: [runtime/self_expansion.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/self_expansion.py); [templates/expansion_planner_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/expansion_planner_prompt.template.md); [runtime/detached.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/detached.py); [runtime/plan_objectives.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/plan_objectives.py)
- Basis: structural
- Confidence: high
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.

### Absence scope

- Surfaces inspected: Expansion implementation/prompt, objectives, detached source replacement and README modes.
- Plausible first-party paths checked: Research workflow templates, objective-driven task expansion and runtime self-update.
- Why no material first-party path remains: These supply current task repair/extension or deterministic code replacement, not environmental sensing plus prospective organizational options and capability adoption; no qualifying parent adaptation mode is supplied.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate-identity/policy adjudication loop established.
- Disturbance / variety regulated: Ultimate purpose/authority tensions, rather than ordinary task risk or scope.
- Decisive decision or feedback right: No first-party identity-level proposal→legitimate ultimate decision→operational return established.
- Decision owner: User sets brief and permissions; no S5-specific mode established.
- Supporting / enforcement mechanisms: Prompt authority hierarchy, security policy, approvals and protected paths.
- Closure path: Current scope changes and risky actions return through approvals, but these remain task/current-control choices.
- Why this is / is not agent-owned: Human final say and static purpose do not by themselves establish S5.
- Evidence: [references/SECURITY.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/references/SECURITY.md); [runtime/approval.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/approval.py); [runtime/change_requests.py](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/runtime/change_requests.py); [templates/worker_prompt.template.md](https://github.com/LJC-FVNR/LoopPlane/blob/0798233a1d1e3d9058c491aaeffb32575966004d/templates/worker_prompt.template.md)
- Basis: structural
- Confidence: high
- Caveats: boundary-relative source conclusion; configured external execution engines are required, and no live provider execution is claimed.

### Absence scope

- Surfaces inspected: Security reference, approval/change-request implementation and role contracts.
- Plausible first-party paths checked: User brief, protected PLAN authority, content-bound approvals and operator changes.
- Why no material first-party path remains: All evidenced returns concern operational scope/risk/commitments; none resolves ultimate identity/policy or S3–S4 tension at this boundary.

## Distributed OSS parent arrangement

The project operator is the evidenced S3 parent for one local workflow. Contributors, maintainers, releases and unrelated private agent sessions are not merged into a project-wide parent organization or S5 claim.

## Self-hosted and non-human modes

Provider-backed local installation and optional semantic-watchdog configuration are assessed. Noop/fake CLI fixtures are test modes, not autonomous owners. Supervised whole-plan changes support P only for S3; generic approvals do not spread parent notation to other functions.

## Recursion

Task/recovery cells retain local implementation discretion but nesting and project/workflow records do not establish recursively complete viable systems. Cross-project machine runner locks are explicitly outside this single-workflow assessment.

## Variety and escalation

Workers absorb implementation/test variety; validation separates claims from accepted evidence. Exhausted repair or scope gaps enter self-expansion/approval/attention paths. Background semantic inspection can challenge liveness and return a recovery state. Status/attention values alone are not algedonic-function evidence.

## Evidence gaps

No authenticated Codex/Claude model run, provider independence, deployment performance or empirical viability claim. Separate-context watchdog source wiring is established; live model reliability and operator governance in any actual installation remain unobserved. Native watchdog/inspector fixtures test protocol return, not independent model judgment.
