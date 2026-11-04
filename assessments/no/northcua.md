---
harness_id: northcua
project_name: NorthCUA
repository: https://github.com/beipo-ai/NorthCUA
review_ref: fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# NorthCUA

## Review boundary

- System in focus: The released NorthCUA first-party computer-use harness: Desktop/Web actors, shared NexAU-backed model/tool round runtime, context and artifact services, independent round evaluator, controller/device bridge, and optional persistent batch orchestration.
- Purpose and identity: Turn user desktop/browser tasks into tool-mediated actions with retained context, assess their observable outcomes, and manage isolated attempts without conflating agent assertions with evaluation evidence.
- Relevant environment: GUI applications and websites, live browser/device state, user tasks and evaluation requirements, external model providers, remote workers/sandboxes, resource contention, tool errors and interrupted attempts.
- Standard-distribution boundary: Public Python packages and CLI entrypoints for local/remote Desktop/Web tasks, configured first-party evaluator and batch scheduler. Evaluate separately a single actor run and the supported multi-attempt operator-controlled batch mode; do not infer one mode's organizational functions for another without wiring.
- Credited operating / distribution surfaces: [architecture](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/architecture.md), [Web AgentKit runtime](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agents/web/agentkit.py), [Desktop step](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agents/desktop/runtime/step.py), [evaluator runner](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agentkit/evaluator/runtime/runner_loop.py), [batch scheduler](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/runner/scheduler.py), [batch operations](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md).
- Adjacent first-party surfaces excluded from ownership: Report benchmark and showcase metrics, training/experience-production pipelines explicitly outside release scope, research publication and repository CI/release governance. NexAU internals, external models, CUDA/vision checkpoints, arbitrary user workloads, cloud/sandbox providers and third-party device applications are dependencies, not extra first-party organizational owners.
- First-party operating / deployment modes considered: Local Desktop or Web model/tool session; remote controller/leased device; optionally enabled post-run evaluator with artifact-only or authorized live inspection; local-process and sandbox-backed batch with status, pause, drain, cancel, selected retry and resume controls.
- Recursion level: A single actor task/session for S1 and audit, and the task-attempt batch as the containing operational organization when S2 and parent S3 are considered. A tool call, browser tab or leased worker is not by itself another viable S1.
- Reviewed revision: `fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4` (stable GitHub repository ID 1443075589).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Desktop and Web agents specialize screenshots, accessibility/DOM observation and tool dispatch, while a shared AgentKit/NexAU adapter repeats model decisions, typed action calls, tool returns and persisted session/round/step history. Context projection keeps recent clean visual state and overlays, task-preserving summarization and agent-authored notes while storing full traces. The controller binds tasks to device sessions; a separate batch scheduler persists unique task/attempt claims, creates task-scoped leased environments, applies deterministic capacity/backpressure/retry rules and reconciles terminal state. A distinct evaluator agent can read actor artifacts and perform authorized direct live probes before the browser/device is released. It emits a structured verdict independent of the actor's terminal report, and batch status projection distinguishes evaluation success, failure and pending/error. A human operator can inspect whole-batch status and select current pause, drain, cancel, resume and failed-task retry actions. These are supported modes, not claims that a hosted provider or benchmark was run during this assessment. [System tour](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/system-tour.md), [evaluation lifecycle](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/evaluation.md), [batch lifecycle](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md).

## Operational model

The model-driven actor chooses which GUI/browser observation and action to use and reacts to tool results inside one task. In batch mode, independently running task attempts are operational units with isolated state; the deterministic scheduler reserves/leases attempts and regulates capacity and retry collision, while an operator retains discretionary whole-batch current-control rights. The separately instantiated model evaluator judges evidence, including probes not identical to the actor's success report, and its verdict changes the batch's accepted terminal status. Neither the batch scheduler nor the static safety/tool allowlists become agent-owned management merely because they enforce a decision. No first-party prospective outside-and-then or ultimate-policy appellate loop is established by the reviewed distribution.

## S1 — Operations

- State: A
- Function: Carry out one user computer-use task through observed Desktop/Web state and model-chosen actions.
- Disturbance / variety regulated: Unknown application screens, changed DOM/state, unexpected tool responses, context growth, unsatisfied task conditions and execution interruptions.
- Decisive decision or feedback right: Choose next computer-use/tool action or finish based on observed state and returned tool results.
- Decision owner: Configured agent model operating in the first-party Desktop/Web round executor; external inference service supplies model computation but does not implement the NorthCUA task loop.
- Supporting / enforcement mechanisms: NexAU-compatible model adapter, typed tool contracts, context/image window, working notes, action backend, controller/device bridge, step budgets and persisted history.
- Closure path: User request → contextual observation → model step/action choice → constrained tool execution → new screenshot/DOM/tool result and notes → subsequent model step or terminal result.
- Boundary reachability: The documented local Web/Desktop CLI and remote task modes instantiate this actor loop using bundled AgentKit specs and first-party tool dispatch; no test-only harness or adjacent research agent is needed.
- Why this is / is not agent-owned: The model selects substantive environment actions after seeing observations. Tool schemas, transport, budget and safety gates constrain or carry this discretion rather than select it.
- Evidence: [Web agent specification](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agents/web/agentkit.py), [Desktop step executor](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agents/desktop/runtime/step.py), [runtime architecture](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high for the first-party model/tool loop; no live hosted-provider success claim.
- Caveats: S1 depends on configured model/device/backend availability, and the assessment does not measure task efficacy.

## S2 — Coordination

- State: C
- Function: Attenuate interference between distinct simultaneously admitted batch task attempts, especially duplicate execution, resource oversubscription and accidental state reuse.
- Disturbance / variety regulated: Concurrent attempts may claim the same task, worker/device capacity or prepared environment after restarts, timeouts and parallel preparation.
- Decisive decision or feedback right: Select or revise which attempt can claim a lease and when backpressured capacity may admit subsequent tasks; a higher-level autonomous coordination policy would have to be composed to own the discretion.
- Decision owner: First-party deterministic scheduler, leases and persisted rules select immediate admission based on human/developer-provided limits; there is no demonstrated autonomous agent choosing inter-task coordination policy.
- Supporting / enforcement mechanisms: SQLite task claim/heartbeat, attempt identity, task-scoped sandbox/device lease, backpressure samples, single-use prepared reservation and reconciliation.
- Closure path: Contending batch attempts → exclusive task/lease claim and controller-pressure check → one attempt proceeds, conflicting contenders wait or reconcile → subsequent tasks claim only released/eligible capacity.
- Boundary reachability: Batch mode ships these scheduler/lease components and documented resume semantics; unlike a hypothetical generic queue, the code specifically handles simultaneous task claims and attempt reuse.
- Why this is / is not agent-owned: Concrete inter-S1 conflict attenuation exists, but its decisive runtime rule is deterministic; a first-party S2-specific constructor path is exposed without a shipped model-owned policy adjustment loop.
- Distinct S1 units: Independently running Desktop/Web task attempts with their own task goals, environments and actor loops under a single batch.
- Inter-S1 disturbance: Duplicate task submissions or competing sandbox/device admissions and reused application state when attempts overlap or a runner resumes.
- Attenuating coordination relation: Unique task/attempt claims and task-scoped leases, bounded concurrency, backpressure gating and selected retry/reconcile rules.
- Feedback into subsequent S1 behaviour: Denied/late claims do not start duplicate actor operations; capacity availability and persisted task status determine later submission and resume.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The coordination enforces a named cross-attempt collision and resource contention invariant and feeds a concrete admission/withholding result into subsequent distinct task attempts.
- Evidence: [batch scheduler](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/runner/scheduler.py), [lease coordinator](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/runner/leases.py), [backpressure gate](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/backpressure.py), [batch recovery documentation](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md).
- Basis: structural.
- Confidence: medium-high for an actual inter-attempt coordination path, medium for constructor classification.
- Caveats: The batch is optional; an individual local run has no distinct S2 peer set. Deterministic conflict avoidance cannot be upgraded to S2=A without autonomous coordination discretion.

## S3 — Inside-and-now control

- State: P
- Function: Whole-batch current commitments and running capacity can be supervised by a legitimate operator who controls admission, pause, cancellation, drain and selected retries.
- Disturbance / variety regulated: Failed or uncertain attempts, exhausted retry budgets, workload pressure, controller interruptions and cleanup problems across a batch.
- Decisive decision or feedback right: View current aggregate task statuses and choose to stop new admissions, cancel current work, drain running tasks, resume or authorize specific failed-task retries.
- Decision owner: The first-party mode's human batch operator. The scheduler and SQLite state apply that returned decision; no independent AI whole-batch manager is shipped.
- Supporting / enforcement mechanisms: Status/report CLI, persisted control flags and task states, pause/drain/cancel handlers, selected-retry plan validation and scheduler poller.
- Closure path: Operator reviews whole-batch status/report → invokes pause/drain/cancel or bounded selected retry/resume → persistent flags/attempt ceilings are read by the live scheduler → current/new task admissions and execution change.
- Boundary reachability: The documented `northcua batch status|report|pause|drain|cancel|resume` commands and scheduler's control-flag poller form a usable first-party operator mode over the same persisted batch.
- Why this is / is not agent-owned: This is an operationally returned parent mode (`P`), not automatic agent S3; deterministic capacity thresholds and external operator actions do not supply autonomous S3=A or C by themselves.
- Whole-system current view: Persisted all-task states and report/failure breakdown across one identified batch, including attempts and evaluation statuses.
- Current-control decision scope: Stop or resume new admissions, cancel active work, drain committed tasks and select permitted retries for failed tasks, affecting whole-batch present commitments.
- Evidence: [batch operator commands](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md), [CLI branch handling](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/cli/batch_commands.py), [control-flag scheduler](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/runner/scheduler.py), [selected retry plan](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/selected_retry.py).
- Basis: explicit + structural.
- Confidence: medium; owner/control return is directly coded, but no actual operator run was reproduced in this assessment.
- Caveats: Parent governance is only at a single batch's current-operations recursion, not at the OSS project's policy/identity recursion. This finding does not classify arbitrary status dashboards as S3.

## S3* — Complementary audit

- State: A
- Function: A separate evaluator agent challenges actor completion against independently gathered artifact and optionally live application reality.
- Disturbance / variety regulated: Agent self-report may disagree with task requirements, unsaved application state, missing artifacts or unseen outcome failures.
- Decisive decision or feedback right: Select relevant raw/recorded evidence and optional live probes, judge requirements and submit a structured success/failure report distinct from actor termination.
- Decision owner: The separately instantiated first-party model-driven evaluator, through its own tool-selection and final-report loop; not the actor, trace writer or deterministic batch status projector.
- Supporting / enforcement mechanisms: Evidence manifest, read-only artifact and live probe tools, bounded evaluator step execution, report schema, fail-open/fail-closed configuration and batch result projection.
- Closure path: Actor completion → independent artifact/live evidence collection → evaluator model verdict in `final_report` → recorded outcome distinct from actor claim → batch task becomes success/failure/pending and controls downstream retry/reporting decisions.
- Boundary reachability: Shipped local/remote Web/Desktop evaluator modes can be enabled in app configuration or CLI, and the Web evaluator runs before releasing the actor's original browser session. A direct live probe is conditional on explicit permission; the artifact-evidence route remains independently wired.
- Why this is / is not agent-owned: The evaluator chooses direct evidence inspection and a task-grounded judgment in its own model/tool loop; its report changes terminal status. Deterministic tooling does not make that independent audit judgment.
- Claim being audited: Whether the actor actually satisfied the user's task despite its own reported completion.
- Ordinary reporting path: Actor terminal result, its model/tool traces, screenshots and action outputs.
- Complementary access path: Separate evaluator's evidence selection and tool access to saved artifacts plus, when enabled, fresh DOM/screenshot or allowed device read-only probes against the original live session.
- Independence boundary: The evaluator executes in a separate model-round/runtime and has evidence/probe tools unavailable to ordinary self-report; it is still a first-party evaluation path, not an externally independent scientific audit or proof of blind reviewer independence.
- Who acts on findings: Batch status projection treats a present negative verdict as failure, while operator/retry flow may admit a subsequent attempt; no claim that the same actor is automatically corrected before finalization.
- Evidence: [evaluator loop](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agentkit/evaluator/runtime/runner_loop.py), [Web evaluator service](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agents/web/evaluation/service/round_evaluator.py), [read-only probe contracts](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/agentkit/evaluator/tools/client_probe.py), [terminal projection](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/northcua/batch/runner/attempt_reconcile.py), [evaluation modes](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/evaluation.md).
- Basis: explicit + structural.
- Confidence: medium-high for independently wired model audit and returned verdict, not for real-world judge accuracy.
- Caveats: Evaluation may be disabled or fail open; live probes require permission and original session availability; a status verdict affects subsequent batch handling rather than guaranteeing a corrective rerun. No actual hosted model, external evaluator or empirical accuracy study was executed for this assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped S4-specific prospective external-environment model and adaptation-option decision returning to present organizational capability.
- Disturbance / variety regulated: Changes in apps/sites, task complexity and model quality are seen by current actor/evaluator, but not separately explored as future environment adaptation at the batch/harness recursion.
- Decisive decision or feedback right: Generate future-facing capability/policy adaptation options from external distinctions and negotiate them with current operational control.
- Decision owner: Project developers/operators may separately plan upgrades; actor plans current tasks, evaluator judges completed work.
- Supporting / enforcement mechanisms: Working notes, image/context compaction, feedback artifacts, model/provider configuration, benchmark and research documentation.
- Closure path: Task observations and evaluator reports feed current run/batch status, not a first-party outside-and-then option/implementation return loop.
- Why this is / is not agent-owned: Task planning, context memory, runtime retries and post-run quality reporting are not themselves prospective adaptation judgments.
- Evidence: [system tour](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/system-tour.md), [context mechanisms](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/context.md), [batch lifecycle](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md).
- Basis: structural.
- Confidence: medium-high within the reviewed distribution.
- Caveats: Research and model upgrades can support future work outside this runtime boundary.

### Absence scope

- Surfaces inspected: Desktop/Web actor loops, working-memory/summary services, evaluator, batch failure/retry control, report/research and release/benchmark material.
- Plausible first-party paths checked: Agent task plans, model memory and compaction, evaluator verdict reuse, batch selected retry, research experience/training pipeline.
- Why no material first-party path remains: These paths regulate current tasks or preserve post-run evidence; none is wired as a prospective environment model proposing capability changes with a returned S3/current-operation adaptation decision in the shipped harness.

## S5 — Policy and identity

- State: —
- Function: No system-level identity or ultimate-policy resolution channel with a legitimate deciding owner and returned binding decision is shipped for the assessed task/batch organization.
- Disturbance / variety regulated: Risky computer actions, provider/device access, evaluation-probe mutability and cost/time limits are bounded by operator-set configuration and tool controls.
- Decisive decision or feedback right: Adjudicate contested identity/purpose/ultimate-policy matters and return binding changed policy to the running organization.
- Decision owner: Users/developers choose static configuration and external provider access; no first-party S5 decision actor or parent appeal path is established for such matters.
- Supporting / enforcement mechanisms: Read-only evaluator probes by default, explicit mutating-tool opt-in, sandbox capabilities, model/task budgets, run authorization and cancellation.
- Closure path: Current operator configuration → enforcement of permitted tools/budgets, with no identity-level proposal → parent authority → decision → changed operation loop.
- Why this is / is not agent-owned: Ordinary permission and task cancellation choices are not ultimate-policy decisions, and no shipped independent policy/identity deliberation return is identified.
- Evidence: [evaluation configuration](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/evaluation.md), [batch configuration](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/batch.md), [architecture](https://github.com/beipo-ai/NorthCUA/blob/fb5f9e2725c7cfe268fa0c2dc40f44cc132c12f4/docs/architecture.md).
- Basis: structural.
- Confidence: medium-high at assessed operation/batch boundary.
- Caveats: Project maintainers naturally retain licensing/release governance, but that adjacent project-level authority cannot be silently credited as runtime S5.

### Absence scope

- Surfaces inspected: CLI/operator controls, tool-policy configuration, agent/evaluator runtime, batch scheduler and parent-facing documentation.
- Plausible first-party paths checked: Tool approval, evaluator live probe permissions, batch pause/cancel, user model choice, research/maintainer governance.
- Why no material first-party path remains: No evidence of an identity/ultimate-policy issue being raised to legitimate authority and returned as an operational mandate; the inspected controls execute preselected constraints or current task decisions.

## Distributed OSS parent arrangement

Public maintainers, paper authors and local operators are not assumed to form one shared parent recursion. S3=P is limited to a supported local batch where the legitimate operator sees and alters current commitments. It does not import the developers' release process or an external model provider as an organization-wide S5 mode.

## Self-hosted and non-human modes

Local-process execution and optionally connected remote workers preserve the task actor's loop. A human batch operator retains S3 current intervention, while the evaluator is a distinct model-owned audit when enabled. Deterministic scheduler/lease machinery is not an autonomous manager. No agent-owned S5 or prospectively adaptive S4 mode was found.

## Recursion

One model-driven Desktop/Web task is the operational S1. A batch contains multiple such isolated attempts, each with its own environment and purpose; the batch scheduler coordinates claims and an operator controls current aggregate commitments. The workers, tools and provider calls do not each become separate viable recursive organizations merely because they are nested.

## Variety and escalation

Typed actions, live observations and direct evaluator probes amplify task-relevant distinctions. Context compaction and bounded image windows attenuate prompt volume, while leases, backpressure and retry ceilings attenuate cross-task interference and unsafe operational variety. Model/tool/evaluator failures return as task records and optional retries; operator pause/drain/cancel applies current control. No exceptional cross-recursion identity-policy escalation is shown.

## Evidence gaps

This is a source-pinned review, not a live paid-model, CUDA/GPU, hosted sandbox or real-world benchmark run. Automated fixture tests described by the project establish integration paths but not model effectiveness, independent reviewer identity or guaranteed evaluator accuracy. The S2 constructor classification and parent-mode S3 reachability are bounded to the documented multi-attempt batch mode; S3* uses the separately instantiated first-party evaluator and may be disabled by config.

## Verdict

**Propose inclusion.** NorthCUA ships an operational model/tool computer-use S1, a concrete deterministic inter-attempt coordination constructor, an operator-closed batch current-control mode and a separately wired model-driven complementary evaluator whose verdict affects accepted task status. Static safeguards, memory, research and benchmark surfaces do not establish S4/S5 runtime ownership.
