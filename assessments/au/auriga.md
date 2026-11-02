---
harness_id: auriga
project_name: Auriga
repository: https://github.com/lose4578/Auriga
review_ref: 3e1be75e186e49f8c268fd5fc6c08427f99254ce
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Auriga

## Review boundary

- System in focus: the shipped Auriga model-led embodied manipulation runtime for an ARX X5 / RoboDojo episode, including its explicitly supported optional fresh-agent operation-verification mode.
- Purpose and identity: let an autonomous Codex-based actor inspect observed robot/camera state, plan and execute physical manipulations through a single action gateway, receive measured feedback and recover; optionally check action outcome claims with an independent visual evidence agent.
- Relevant environment: uncertain object positions, camera images, kinematics, contact/slip, collision risk, simulator step budget, native robot worker, model/provider delays and execution ambiguity.
- Standard-distribution boundary: Python `auriga` package, `auriga.apps.gateway` Workbench, Codex actor session, `runtime.Harness`/tools, RoboDojo-backed action worker and the optional `visual_review_model=gpt-6.1-sol` fresh official Codex helper. Native RoboDojo/Isaac/GPU/model weights must be installed separately; their benchmark evaluator truth is not exposed as actor evidence.
- Credited operating / distribution surfaces: `auriga/apps/gateway/{cli.py,workbench.py}`, `auriga/cortex/session/{codex.py,visual_review.py,codex_evidence_agent.py}`, `auriga/cortex/context/operation_verification.py`, `auriga/runtime/{harness.py,tools/handlers.py,tools/builtins.py,actions/unified_actions.py,programs/}`, `auriga/robot/backends/robodojo/` and runtime configuration.
- Adjacent first-party surfaces excluded from ownership: `auriga/apps/evaluation/` batch queue/benchmarks, test fixtures and CI, archive library/replay/HD rendering, contributor governance and third-party robot simulator/benchmark scoring. `program_run` primary-actor review is not mistaken for independent auditor; optional release/experiment notification is not a run-level governor.
- First-party operating / deployment modes considered: default single-episode model-directed actor with preview/execute/recovery and optional scripted programs; optional actor-requested fresh Sol visual operation verification; replay and benchmark queue considered only to set ownership exclusions. No live Isaac GPU/Codex/provider robot episode was run in this assessment.
- Recursion level: one embodied actor controlling one robot episode; dual arms are controllable actuators, not autonomous S1 organizations. Independent evidence Sol is a complementary auditor at the actor episode boundary, not another robot/action owner.
- Reviewed revision: `lose4578/Auriga@3e1be75e186e49f8c268fd5fc6c08427f99254ce` (GitHub repository ID 1440732401), frozen #2578 / controller #2579.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/README.md) and [Workbench](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/apps/gateway/workbench.py) wire a persistent Codex model session to a robot `Harness`, scene-limited observations, previewed stage batches and a single action gateway. [`Harness.execute`](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/harness.py) owns physical action admission, identity, current state, active-writer exclusivity, motion/stop receipts and measured outcomes, while the actor model chooses the next pose or action from feedback. Program jobs can issue action proposals but must receive [the primary model's review](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/unified-actions.md) before a frozen program execution is resumed, unless that job was explicitly granted direct actions.

The optional [Sol verification mode](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md) is off by default (`visual_review_model: null` in [config](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/configs/auriga.json)); `gpt-6.1-sol` enables the shipped `vision_review(evidence_mode='operation')` tool. [Handler](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/tools/handlers.py) dispatches the selected action/observation evidence to [`VisualReviewer.review_operation`](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/session/visual_review.py). [`CodexEvidenceAgent`](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/session/codex_evidence_agent.py) launches a fresh isolated app-server thread without actor history, memory, tools or workspace privileges. It checks the phase-specific claim against before/after RGB, measured robot state and immutable execution receipts; [operation verification](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/context/operation_verification.py) constrains unsupported `met` results and guides follow-up. The verdict returns to the primary actor, which decides new observation, correction or recovery. It does not autonomously execute motion or learn hidden task truth.

## Operational model

The model-driven actor is one operational S1 cell and controls robot task execution through a tightly bounded first-party action gateway. Disturbances like bad grasps and uncertain contact are handled by fresh measurements, trajectory previews, model adjustment and emergency native stop gates. The separate optional Sol evaluator is an independent, complementary check of selected action-outcome claims, not the main planner. Deterministic resource caps, plan locks and developer-run benchmarks are not credited as autonomous S3/S4/S5 owners.

## S1 — Operations

- State: A
- Function: pursue robot-manipulation goals through visual observation, task planning, multi-stage preview/execution, measured action feedback and recovery.
- Disturbance / variety regulated: changing object/robot geometry, failed or partial grasps, occlusion, movement slips, constrained arm trajectories and uncertain action completion.
- Decisive decision or feedback right: choose the next physical task action, observation, program, trajectory revision or recovery in light of returned evidence.
- Decision owner: primary model-driven Codex actor (named Astra in optional verification documentation), with action authority mediated by the Harness.
- Supporting / enforcement mechanisms: action identity and current-observation checks, native motion planner, gripper guards, single action writer, program review broker, action ledger, wall/budget supervision and the physical simulator.
- Closure path: Codex task/plan → `robot_observe` and `robot_action` preview → model selects execute → `Harness.execute` native worker → measured receipt/images/stop reason → model adjusts or terminates episode.
- Boundary reachability: normal gateway creates the Codex session and Harness, registers `robot_action` and connects execution to native RoboDojo worker. The model/tool loop is shipped with documented flags, not merely a benchmark test.
- Why this is / is not agent-owned: static robot safety gates do not select a new manipulation strategy; the actor model makes the task-level decisions even when a hard guard prevents unsafe execution.
- Evidence: [README execution loop](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/README.md), [Harness](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/harness.py), [model-led operation](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md).
- Basis: structural
- Confidence: high
- Caveats: no GPU/Isaac/model E2E was reproduced; native benchmark task success is external and not inferred from completed command receipts.

## S2 — Coordination

- State: —
- Function: no distinct conflict-specific inter-S1 coordination and return is established in the supported robot actor organization.
- Disturbance / variety regulated: dual-arm trajectory interference and concurrent program/native action requests are real actuator/resource hazards but not conflicts among distinct autonomous S1 units.
- Decisive decision or feedback right: arbitrate independent agent commitments and return a coordination resolution; not evidenced.
- Decision owner: one actor plans both arms; deterministic Harness serializes physical actions and rejects stale plans, rather than an S2 coordination owner regulating competing agents.
- Supporting / enforcement mechanisms: stage-order dependencies, dual-arm path preview, active-writer exclusivity, plan revision, program broker approval and stop gates.
- Closure path: native constraints and the primary actor can alter a manipulation task, but no separate inter-S1 interference-resolution result is fed into distinct operational agents.
- Why this is / is not agent-owned: two robot arms are not independent goal-directed S1 cells; an optional evidence agent audits a claim but does not compete for physical task execution.
- Evidence: [unified actions](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/unified-actions.md), [Harness action writer](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/harness.py), [program review](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/programs/program_review.py).
- Basis: structural
- Confidence: medium
- Caveats: constraints against conflicting actuator commands have direct safety value but are not cross-agent oscillation governance at this recursion.

### Absence scope

- Surfaces inspected: dual-arm action schema, native execution writer, program broker, actor session, optional Sol and benchmark queue boundaries.
- Plausible first-party paths checked: simultaneous arm stages, program action review, action plan stale-state invalidation, single-writer lock and model tool/subagent invocation.
- Why no material first-party path remains: these coordinate one actor's actuators and auxiliary helpers without distinct competing operational S1 units or an S2 conflict decision-return loop.

## S3 — Inside-and-now control

- State: —
- Function: no independent whole-organization current-control authority over a population of operational S1 commitments is demonstrated.
- Disturbance / variety regulated: native action budget, simulator step accounting, active action conflicts, unknown stop confirmation, model transport failures and episode wall limits.
- Decisive decision or feedback right: select systemic allocation/priority/commitment intervention across distinct operations; absent beyond the single robot episode's work plan.
- Decision owner: primary actor owns task strategy; Harness enforces state/timeout/cost constraints; operator defines task/benchmark configuration.
- Supporting / enforcement mechanisms: `supervision.wait_turn`, action gate, per-action budget, program source grants, GPU resource checks and status/feedback records.
- Closure path: failures can stop one episode or prompt its actor to try another action, not a separate whole-current S3 decision that regulates multiple autonomous units.
- Why this is / is not agent-owned: counters, stop gates and request retry policy are enforcement; removing a hypothetical S3 model leaves them intact.
- Evidence: [runtime supervision](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/supervision.py), [Harness](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/harness.py), [model-led operation](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md).
- Basis: structural
- Confidence: medium
- Caveats: benchmark queue's GPU scheduling concerns the experimental portfolio, outside the declared live agent organization.

### Absence scope

- Surfaces inspected: actor/planning context, Harness current state and model budgets, program broker, optional Sol return and evaluation queue documentation.
- Plausible first-party paths checked: per-episode action-resource admission, model turn limit, GPU and inactivity supervision, task_plan/phase sequencing, experiment GPU scheduler and operator stop.
- Why no material first-party path remains: these enforce a single operational episode or manage development evaluation; no separate current/whole intervention loop at the selected recursion is shipped.

## S3* — Complementary audit

- State: A
- Function: provide an independent, evidence-limited second opinion on a manipulation operation's claimed visible outcome and send discrepancies or uncertainty back to the acting agent.
- Disturbance / variety regulated: optimistic success interpretations of completed motion receipts, wrong target identity, occlusion, unsupported grasp/placement/release claims and partial execution.
- Decisive decision or feedback right: judge `met`, `not_met` or `uncertain` for a claimed phase by comparing independent before/after RGB, execution receipts and measured robot state, and specify evidence gaps/recovery feedback.
- Decision owner: separate fresh `gpt-6.1-sol` evidence agent; primary Astra remains owner of the subsequent physical action and the operator decides whether to enable this configuration.
- Supporting / enforcement mechanisms: deterministic provenance and schema checks, isolated fresh home/thread, suppressed tools/memory, payload source hashes, shared model budget, exact model assertion and unsupported-positive veto in `constrain_answer`.
- Closure path: actor selects meaningful checkpoint and invokes `vision_review(evidence_mode='operation')` → fresh Sol independently examines linked images/receipts and issues bounded verdict and follow-up → tool response returns to the primary actor's Codex turn → actor instructed to resolve uncertainty or choose a changed recovery before later motions. The auditor never executes robot actions.
- Boundary reachability: `features.visual_review_model='gpt-6.1-sol'` is a documented supported config; the actual Workbench instantiates `VisualReviewer(CodexEvidenceAgent(session))`, the runtime tool handler dispatches it and returns the structured assessment to the ordinary actor context. Default `null` mode has no S3* helper; positive vector reflects the first-party enabled operating mode, not default execution.
- Why this is / is not agent-owned: the fresh model provides the discretionary visual evidence judgment; deterministic validation limits unsupported assertions but cannot itself interpret ambiguous target retention/phase outcome. Actor authority to choose recovery is distinct from auditor judgment ownership.
- Evidence: [mode and return contract](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md), [Workbench construction](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/apps/gateway/workbench.py), [fresh agent isolation](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/session/codex_evidence_agent.py), [review judgment](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/session/visual_review.py), [actor recovery instructions](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/cortex/context/operation_verification.py), [tool handler](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/tools/handlers.py).
- Basis: structural
- Confidence: medium
- Caveats: actor chooses evidence/request and need not obey a fixed compulsory verification phase sequence; this is a first-party supported optional independent second-opinion loop, not privileged simulator-ground-truth audit or guaranteed physical correction. No real provider/robot verification was executed here.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate externally prospective adaptation process with authorized whole-runtime capability-choice and return is demonstrated.
- Disturbance / variety regulated: novel object geometries, repeated failed grasps, changing camera viewpoints, different robot scenes and future task transfer.
- Decisive decision or feedback right: change organizational operating capability based on prospective environmental alternatives; not evidenced at the assessed one-episode recursion.
- Decision owner: primary model adapts task actions in the current scene; developers/operators configure perception services, model and robot plugins.
- Supporting / enforcement mechanisms: `adaptive_action_checkpoint` failure reminders, observation memory, trajectory cost previews, program synthesis and optional external perception.
- Closure path: measured failures can prompt an immediate alternate grasp, viewpoint or trajectory within one task; no distinct environment/future analysis → approved organization-wide capability adaptation → feedback loop is implemented.
- Why this is / is not agent-owned: adaptive recovery within one operating episode is S1 learning/action selection, not automatically S4 strategic adaptation.
- Evidence: [checkpoint helper](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/actions/strategy_checkpoint.py), [model-led recovery](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md), [unified actions/memory](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/unified-actions.md).
- Basis: structural
- Confidence: medium
- Caveats: task memory across episodes informs later S1 work but lacks a separately evidenced S4 decision right.

### Absence scope

- Surfaces inspected: operation memory, failed-mechanism reminders, actor recovery guidance, optional perception, model configuration and development architecture.
- Plausible first-party paths checked: cross-task memories, new robot tooling, model-selected views, strategy checkpoints, external perception upgrades and benchmark-derived tuning.
- Why no material first-party path remains: these are task recovery, user/developer configuration or external research/evaluation; no distinct future-oriented organizational adaptation owner and returned capability closure exists.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational policy/identity arbitration with legitimate authoritative return is implemented inside the robot episode.
- Disturbance / variety regulated: robot safety boundaries, model permissions, execution modes, privileged task truth, tool grants and physical stop decisions.
- Decisive decision or feedback right: adjudicate identity-level commitments and revise binding policy for the whole; not shown beyond fixed configuration and task controls.
- Decision owner: developer/operator specifies guardrails and modes; deterministic Harness enforces validation; primary actor decides ordinary manipulation steps within those bounds.
- Supporting / enforcement mechanisms: actor observation redaction, action schema and state locks, program grants, model call budget and sandbox controls.
- Closure path: individual actions are admitted/rejected against predefined rules, but no policy-level dispute → qualified authority → ultimate decision → new identity-governing operating rule is shipped.
- Why this is / is not agent-owned: the model may choose a risky trajectory and receive advisory data, but it does not own the system's ultimate identity or change invariant control policy.
- Evidence: [action gate](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/auriga/runtime/harness.py), [actor information boundary](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/actor-information-boundary.md), [model-led operation](https://github.com/lose4578/Auriga/blob/3e1be75e186e49f8c268fd5fc6c08427f99254ce/docs/development/model-led-operation.md).
- Basis: structural
- Confidence: medium
- Caveats: hard physical safety enforcement is not S5 ownership; hosted model provider and robot/simulator platform policies are outside the first-party actor boundary.

### Absence scope

- Surfaces inspected: actor rules/information boundary, Harness validation and safety, program action permissions, optional review and config/replay modes.
- Plausible first-party paths checked: task-plan mandate, execution approval, sandbox flag, user stop, privileged evaluator truth redaction and helper no-tools policy.
- Why no material first-party path remains: these prescribe or enforce existing operating constraints without an evidenced deliberative ultimate-policy authority and corrective policy return.

## Distributed OSS parent arrangement

Open-source contributors, simulator maintainers, robot operators and independent benchmark evaluators are separate actors; repository co-location or an evaluation queue does not make them the live robot episode's S3/S4/S5 parent. The operator may enable optional Sol audit, but remains outside audit judgment ownership once invoked. No separate legitimate parent policy loop is reconstructed.

## Self-hosted and non-human modes

Default locally hosted RoboDojo episode has one model-owned robot S1 and no separate S3* helper. The documented enabled Sol mode adds an independent model-owned S3* second opinion, with instruction-level corrective return; the model remains responsible for subsequent action. Direct program action authorization and optional robot policy step do not promote external policies or child process gates into metasystem owners.

## Recursion

The robot episode comprises model-led operation, native robot actuators, optional read-only evidence helper and deterministic safety control. Multiple arms, programs, tool calls and fresh helper threads are functional components, not separately evidenced viable organizational recursions.

## Variety and escalation

Geometry previews, stage guards, native stopping, measured receipts, recovery guidance and optional independent Sol operation review reduce uncertainty at action boundaries. Hard stop/unknown gates are immediate execution regulation; only the optional Sol path carries a complementary independent finding back to the main actor. Neither establishes a separately modeled S3/S4/S5 policy/governance escalation channel.

## Evidence gaps

No GPU simulator, Codex/provider credentials or physical robot session were run, and the actual benchmark task-success evaluator was not inspected as an operational decision owner. The released optional reviewer path is structurally explicit, with selected-evidence independence and actor-facing feedback; its practical use and whether a particular actor heeds a verdict remain unobserved. Two targeted source tests were attempted but could not start in this environment because the project-specific test import path and OpenCV runtime dependencies were unavailable; no E2E success is claimed.
