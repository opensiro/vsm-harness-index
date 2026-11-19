---
harness_id: forceharness
project_name: ForceHarness
repository: https://github.com/showlab/ForceHarness
review_ref: 733407c1ea90d8b474dff7809d9349d0f5f0b1d5
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ForceHarness

## Review boundary

- System in focus: first-party model-to-primitive harness and supported simulation/real-robot operating deployment, including live monitor runner management.
- Purpose and identity: complete manipulation tasks using frozen model decisions, bounded force tools and physical feedback.
- Relevant environment: contact/object mechanics, robot/simulator, cameras, inference/relay, human operator and one shared real arm/scene.
- Standard-distribution boundary: Episode/LLMAgent, primitive/translation/backends, real runner/relay/validation and monitor launch/live/stop paths.
- Credited operating / distribution surfaces: model/tool/receipt loop; monitor-managed live hardware admission and operator current commitment intervention.
- Adjacent first-party surfaces excluded from ownership: benchmark scoring/research matrices, held-out comparisons, offline policy baselines, fake scripted demos, CI/tests and repository governance. Monitor historical score/labels/comparison are evaluation, distinct from its live operating controls.
- First-party operating / deployment modes considered: API-model simulator episodes; real runner with API/CLI bridge; optional fresh grasp/release confirmation; monitor single-live-robot admission and operator intervention. Manual/mock/scripted routes do not establish A.
- Recursion level: supplied manipulation deployment with episode cells and local monitor-operator parent; not the research lab or all robot clients.
- Reviewed revision: `733407c1ea90d8b474dff7809d9349d0f5f0b1d5`.
- Observation date: 2026-11-19.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A frozen model selects tools between observations. Primitive controllers close fast physical loops, terminate on contact/completion/limits and return reports. Fixed estimators translate force traces into quantities and uncertainties, without learning or deciding task success. Episode supplies prompts/tools, dispatches calls, appends results and repeats; model done and terminal evaluation truth are distinct.

Backends cover MuJoCo, ForceBench, real Franka and offline fake. The real runner validates one relay call per turn, invokes guarded primitives and sends receipts/scene observations. A first-party monitor API/CLI bridge or a manual source answers the relay; confirmation can constrain grasp/release. The monitor launches runners, observes live current state and exposes finish/interrupt/kill with guarded sequencing, refuses overlapping monitor-managed real episodes and requires human scene reset. Historical evaluation charts, training and labels do not supply runtime owners.

Primary sources: [Episode/LLMAgent](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/loop.py), [tool schemas](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/tools.py), [primitives](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/primitives/library.py), [fixed estimators](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/translation/estimators.py), [real runner](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/runner.py), [model/operator relay](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/relay.py), [monitor SessionManager](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/sessions.py), [monitor control routes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/server.py), [live state/force view](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/live.py), [monitor modes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/monitor.md), [architecture](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/architecture.md), [robot guard](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/robot_side/franka_polymetis/guard.py).

## Operational model

Model-led episode cells are operational units. Primitive controllers, translation, transport and guards support their discretion. The optional monitor deployment adds shared-robot admission and operator current-control relations; those are established independently from low-level force regulation or benchmark scores.

## S1 — Operations

- State: A
- Function: complete a physical manipulation/investigation task through model-selected tools.
- Disturbance / variety regulated: unknown object/contact properties, failed actions and changing physical outcomes.
- Decisive decision or feedback right: choose the next primitive/arguments or done after physical observations.
- Decision owner: API model in LLMAgent or monitor model bridge; manual/scripted sources do not establish A.
- Supporting / enforcement mechanisms: primitive controllers, validation, estimators, images, relay, history and guards.
- Closure path: Episode appends ContactReports as tool results; real runner validates a relay call, executes and returns receipts/scene into the next model turn.
- Boundary reachability: native episode/real runner and monitor bridge wire model selection to supplied tools without custom autonomous policy code.
- Why this is / is not agent-owned: the model selects task-dependent actions; motor control and formula-based estimators enforce/describe them.
- Evidence: [Episode/LLMAgent](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/loop.py), [tool schemas](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/tools.py), [real runner](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/runner.py), [model/operator relay](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/relay.py), [primitives](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/primitives/library.py)
- Basis: structural.
- Confidence: medium-high.
- Caveats: human grasp/release permission can constrain actions without choosing the complete solution. No model/simulator/robot was run.

## S2 — Coordination

- State: C
- Function: prevent distinct episode work cells from overlapping control of one real arm/scene.
- Disturbance / variety regulated: a new live-episode request can compete with an already running cell for the same robot and unreinitialized scene.
- Decisive decision or feedback right: admit/defer a requested episode until shared hardware and scene handover are ready.
- Decision owner: operator/developer composition; no installed autonomous episode coordinator.
- Supporting / enforcement mechanisms: SessionManager active-live registry, guarded launch planning and terminal states.
- Closure path: conflicting live launch is refused as already running; after terminal state and operator scene reset/checklist, a new checked launch can proceed.
- Boundary reachability: the shipped monitor checks existing live sessions before launching the native runner; the real-mode handover path is hardware-specific.
- Why this is / is not agent-owned: fixed exclusion is S2 support, not an autonomous owner. A developer would still compose an actor around the supplied admission/feedback path.
- Evidence: [monitor SessionManager](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/sessions.py), [monitor control routes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/server.py), [monitor modes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/monitor.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: only monitor-managed live launches share this check. Independent monitors/robot clients are not shown to share a global lock; manual scene reset is required.

- Distinct S1 units: separately identified model-led episode cells, each with task, runner/relay state and outcomes.
- Inter-S1 disturbance: requested live cells would compete for the same arm/scene; the source refuses a second active real-robot episode and requires manual reset between trials.
- Attenuating coordination relation: exclusive monitor-managed live episode admission and handover.
- Feedback into subsequent S1 behaviour: busy launch starts no second runner; terminal state plus checked relaunch governs when the deferred work can act.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this gate addresses overlapping physical robot/scene control, not merely a task sequence or comparative demo order.

## S3 — Inside-and-now control

- State: P
- Function: operator control over monitor-managed current episode commitments and shared robot use.
- Disturbance / variety regulated: active/queued work may need ending, interruption or recovery after inspection of progress and current physical/model state.
- Decisive decision or feedback right: choose Finish next turn, Interrupt or controlled Force quit for selected current work, cancelling queued continuation.
- Decision owner: authorized local monitor operator; no autonomous current-portfolio controller.
- Supporting / enforcement mechanisms: session registry, live force/action/scene view, bridge state, process handles and authenticated stop route.
- Closure path: stop cancels a queued successor, requests relay finish or interrupts the active runner; native cleanup stops control and persists/returns updated session status.
- Boundary reachability: monitor is a shipped live operating console with current state and targeted intervention, beyond historical experiment charts.
- Why this is / is not agent-owned: the human selects current intervention. Signals, budget caps and motor guards enforce it; per-grasp approval is not the S3 witness.
- Evidence: [monitor SessionManager](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/sessions.py), [monitor control routes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/server.py), [live state/force view](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/live.py), [monitor modes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/monitor.md), [real runner](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/runner.py)
- Basis: structural.
- Confidence: medium-high.
- Caveats: P is the monitor-operated deployment, not bare Episode or the whole research organization. Soft Interrupt is not an emergency-stop certification.

- Whole-system current view: monitor session public state plus task, runner/bridge status, turns, force traces and scene for active work.
- Current-control decision scope: current episode commitment, shared real hardware use and queued continuation; targeted finish/interrupt changes what remains running.

## S3* — Complementary audit

- State: —
- Function: no supplied complementary audit with a corrective operational return.
- Disturbance / variety regulated: claimed success may differ from simulator truth or operator visual judgment.
- Decisive decision or feedback right: no packaged independent audit judgment entering subsequent control.
- Decision owner: benchmark scorer/operator labels are evaluation; no runtime S3* owner established.
- Supporting / enforcement mechanisms: ground truth, contact QA, transcripts, reports, videos and monitor labels/comparison.
- Closure path: true/claimed success is saved after the task; monitor labels do not modify original episode records or route corrective agent control.
- Why this is / is not agent-owned: alternative ground truth exists, but terminal scores/charts/labels alone do not close runtime S3*.
- Evidence: [Episode/LLMAgent](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/loop.py), [live state/force view](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/live.py), [monitor modes](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/monitor.md), [labels](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/monitor/fhmon/labels.py)
- Basis: structural.
- Confidence: medium-high.
- Caveats: external researchers can audit these records, but their actor and closure are not supplied by the assessed runtime.

### Absence scope

- Surfaces inspected: terminal scoring/contact QA, transcripts/reports, raw force/video, monitor labels/comparison, real operator scoring and tests.
- Plausible first-party paths checked: true-vs-claimed success, periodic contact questions and operator visual/raw-data review.
- Why no material first-party path remains: measurement/evaluation and routine action safety have no supplied audit-specific agent/constructor and governed finding return into later operational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied prospective external adaptation of future harness capability.
- Disturbance / variety regulated: current force/contact differences are handled within the manipulation task.
- Decisive decision or feedback right: no future-capability option selection and adaptation return.
- Decision owner: model chooses current actions; developers/operators choose calibration and offline research variants.
- Supporting / enforcement mechanisms: tare/settle, fixed estimators, context, task prompts, static playbooks and offline learned baselines.
- Closure path: measurements change the next primitive choice; no prospective capability-library/option/admission loop.
- Why this is / is not agent-owned: external force response and bias calibration are current operations, not automatically S4.
- Evidence: [architecture](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/architecture.md), [fixed estimators](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/translation/estimators.py), [primitives](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/primitives/library.py), [Episode/LLMAgent](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/agent/loop.py), [offline baselines](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/docs/baselines.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: frozen model weights alone do not justify absence; the missing relation is prospective organizational adaptation.

### Absence scope

- Surfaces inspected: translation/calibration, action loop/prompts, real setup, playbooks/configuration and separate offline training/evaluation.
- Plausible first-party paths checked: force adaptation, calibration updates, task-text edits and offline training.
- Why no material first-party path remains: the operational paths lack external/future distinction→capability options→present-capability adaptation closure; research training/manual configuration do not donate it.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy issue-resolution loop.
- Disturbance / variety regulated: physical risk, force/speed/workspace limits and consent bound episodes.
- Decisive decision or feedback right: no identity/policy escalation and authoritative returned governing resolution.
- Decision owner: operator approves actions and developer fixes guards, without an established S5 function.
- Supporting / enforcement mechanisms: system/task prompts, validation, guard, startup checklist and fresh grasp/release confirmation.
- Closure path: consent/refusal becomes tool feedback or execution constraint; no identity/ultimate-policy adjudication governs later operation.
- Why this is / is not agent-owned: human go-ahead, safety veto and static guard are not themselves S5.
- Evidence: [model/operator relay](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/relay.py), [robot guard](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/robot_side/franka_polymetis/guard.py), [real runner](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/runner.py), [validation](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/forceharness/real/validation.py), [repository boundary](https://github.com/showlab/ForceHarness/blob/733407c1ea90d8b474dff7809d9349d0f5f0b1d5/AGENTS.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: lab/institution governance cannot be inferred from ordinary local operating permission.

### Absence scope

- Surfaces inspected: prompts, startup/checklists, confirmations, guards/validation, monitor permissions/settings and repository instructions.
- Plausible first-party paths checked: operator consent/stop, hard refusals and task instruction changes as possible parent-policy channels.
- Why no material first-party path remains: these close operational authorization or enforce static bounds; no identity/ultimate-policy matter is routed to legitimate authority and returned as a governing policy resolution.

## Distributed OSS parent arrangement

Only the local deployment operator parent is evidenced. Source maintainers or robot-lab institutions do not automatically close deployed functions.

## Self-hosted and non-human modes

Bare simulated/external-relay episodes need not include monitor oversight. P is specifically monitor operation; a manual model replacement is not autonomous S1. No autonomous current-portfolio controller is claimed.

## Recursion

Control rates/layers and episode nesting do not prove recursively viable agents.

## Variety and escalation

Fast physical disturbance is handled by primitives; slower task choices reach the model. Invalid/declined actions return feedback. Severe faults terminate/hold through native guards. A stop/fault status does not itself establish algedonic authority or S5.

## Evidence gaps

Complete pinned tree (323 blobs, untruncated) and relevant source/docs/monitor/evaluation boundary inspected. No simulator, model, robot, motor/gripper movement or deployment test was executed. Hardware safety, distributed exclusion, performance and independent secondary semantic agreement are not certified.
