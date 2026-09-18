---
harness_id: chief
project_name: Chief
repository: https://github.com/SmileLikeYe/agent-chief
review_ref: d46072a804ff16aa7ce87751b82178f13fb973be
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Chief

## Review boundary

- System in focus: one Chief resident attention-routing process plus its first-party ingest, decision, dispatch, verification, feedback-learning, memory and delivery surfaces at the pinned revision.
- Purpose and identity: turn incoming events from agents, feeds and integrations into bounded decisions to drop, digest, interrupt, dispatch or curate while preserving inspectability and conservative fallback.
- Relevant environment: external feeds/connectors, user context and reactions, configured LLM judge, delegated executors, delivery channels and local policy/configuration.
- Standard-distribution boundary: repository code and packaged skills/configuration; external judge/executor models are execution hosts credited only where Chief supplies the first-party organizational contract.
- First-party operating / deployment modes considered: resident daemon, dispatch with acceptance command, optional LLM verifier hook, feedback learning, shadow mode and local operator configuration.
- Recursion level: one Chief attention-management organization. External dispatched coding/OpenClaw agents are not silently promoted to internal S1 units.
- Reviewed revision: `d46072a804ff16aa7ce87751b82178f13fb973be`.
- Observation date: 2026-09-18.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.4`.

## Repository architecture

Chief is a local-first resident loop: ingest normalizes events, the Brain triages/associates them, hard rules and similarity filters reduce cheap cases, an LLM judge handles remaining relevance/actionability choices, and the selected route drives interrupt/digest/dispatch behavior. Dispatch results can be checked by an acceptance command or an optional LLM second opinion and can retry before human escalation. User reactions feed a bounded learner that updates topic weights, similarity sets, pins and thresholds; nightly jobs distill learned preferences into local policy.

## Operational model

The primary operation is deciding and acting on attention-bearing events. The LLM judge is the autonomous operational decision owner when Stage 3 is reached, while deterministic rules, thresholds, shadow mode and delivery limits constrain execution. Dispatch verification is a separate completion-challenge path, but ordinary resident wiring does not supply the autonomous verifier callback, so that path is classified as constructor rather than autonomous audit.

## Primary evidence

- [`docs/architecture.md`](https://github.com/SmileLikeYe/agent-chief/blob/d46072a804ff16aa7ce87751b82178f13fb973be/docs/architecture.md) — end-to-end event path, dispatch verification, learning and accountability.
- [`core/brain.py`](https://github.com/SmileLikeYe/agent-chief/blob/d46072a804ff16aa7ce87751b82178f13fb973be/core/brain.py) — staged decision loop and dispatch preparation.
- [`dispatch/acceptance.py`](https://github.com/SmileLikeYe/agent-chief/blob/d46072a804ff16aa7ce87751b82178f13fb973be/dispatch/acceptance.py) — acceptance command / optional LLM second-opinion verification, retry and escalation.
- [`cli/runtime.py`](https://github.com/SmileLikeYe/agent-chief/blob/d46072a804ff16aa7ce87751b82178f13fb973be/cli/runtime.py) — standard resident wiring; `prepare_delivery` is called without an autonomous verifier callback.
- [`core/learner.py`](https://github.com/SmileLikeYe/agent-chief/blob/d46072a804ff16aa7ce87751b82178f13fb973be/core/learner.py) — bounded user-feedback learning and threshold adaptation.

## S1 — Operations

- State: A
- Function: autonomously classify attention-bearing events and execute the selected handling path.
- Disturbance / variety regulated: heterogeneous event content, urgency/relevance uncertainty, user context, dispatchability and changing local preference history.
- Decisive decision or feedback right: for events reaching the model stage, choose the scored route and whether work should be dispatched or attention requested.
- Decision owner: the configured model-driven Chief judge operating through the first-party Brain contract.
- Supporting / enforcement mechanisms: hard-rule filters, similarity classifier, scene thresholds, shadow mode, state store, executor and delivery adapters.
- Closure path: the judge decision becomes a persisted route; Chief delivers, dispatches or defers accordingly; resulting feedback/state is available to later events.
- Why this is / is not agent-owned: deterministic filters can settle simple cases, but the standard distribution includes a model-owned judgment path for unresolved operational events and directly executes its selected action.
- Evidence: `docs/architecture.md`, `core/brain.py` and `cli/runtime.py`.
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference is a host capability; the credited organizational right is the decision exercised through Chief's first-party Brain contract.

## S2 — Coordination

- State: —
- Function: no separate inter-S1 coordination function is established at the selected Chief boundary.
- Disturbance / variety regulated: potential contention among external executors was inspected, but no internal multi-S1 coordination relation is established.
- Decisive decision or feedback right: no material first-party right was found that regulates interference among multiple distinct Chief S1 units.
- Decision owner: none established for qualifying S2.
- Supporting / enforcement mechanisms: source deduplication, dispatch timeout and delivery sequencing regulate the event pipeline, not interactions among distinct S1 work units.
- Closure path: no qualifying inter-S1 attenuation-and-feedback loop is established.
- Why this is / is not agent-owned: the missing element is the S2 function itself, not merely autonomous ownership.
- Evidence: `docs/architecture.md`, `core/brain.py`, `cli/runtime.py`.
- Basis: structural
- Confidence: high
- Caveats: external dispatch targets may have their own coordination systems, but those are outside Chief's declared standard-distribution boundary.

### Absence scope

- Surfaces inspected: architecture, Brain decision path, resident runtime, dispatch/executor flow, ingest/delivery and local state/learning.
- Plausible first-party paths checked: deduplication, queueing, dispatch sequencing, timeout/retry and multiple external integration sources.
- Why no material first-party path remains: these paths regulate event processing or one delegated task; they do not establish multiple distinct Chief S1 units plus a specific inter-unit disturbance and returned coordination decision.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established above Chief's primary attention-routing operation.
- Disturbance / variety regulated: runtime failures, cost/context state and routing exceptions were inspected but remain part of the operational pipeline.
- Decisive decision or feedback right: no separate organizational owner was found with whole-system discretion over current S1 resources, commitments or priorities.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: scene caps, timeouts, thresholds, status/trace data and configuration constrain current operation without forming a separate S3 owner.
- Closure path: no qualifying whole-system current-control decision loop separate from S1 is established.
- Why this is / is not agent-owned: naming the product “Chief” or having control logic does not establish the VSM S3 function; the evidenced decisions are the primary service itself.
- Evidence: `docs/architecture.md`, `core/brain.py`, `cli/runtime.py`.
- Basis: structural
- Confidence: high
- Caveats: operator configuration may influence current behavior, but generic configuration is not enough to establish parent-governed S3.

### Absence scope

- Surfaces inspected: Brain stages, resident assembly, context/scene engine, dispatch, delivery, trace/report and configuration surfaces.
- Plausible first-party paths checked: scene policy, thresholds, dispatch timeout, graceful degradation, trace/cost reports and operator overrides.
- Why no material first-party path remains: no separate whole-system current-control role with discretionary resource/commitment authority and a returned regulation loop was found.

## S3* — Complementary audit

- State: C
- Function: challenge a delegated task's completion claim with a separate acceptance path and feed rejection back into correction/escalation.
- Disturbance / variety regulated: false-positive completion, executor self-report error and outputs that do not satisfy explicit acceptance criteria.
- Decisive decision or feedback right: judge whether a dispatch result satisfies the acceptance claim and, on failure, require retry or escalate.
- Decision owner: constructor path; Chief supplies the verifier interface and closed retry/escalation protocol, but the ordinary resident mode does not wire an autonomous `AskFn` verifier as the decisive owner.
- Supporting / enforcement mechanisms: `acceptance_cmd`, optional `ask` callback, verification prompt, one-retry limit and human escalation.
- Closure path: failed verification rejects the first result, triggers one retry, and on repeated failure returns an escalation instead of accepting the claim.
- Why this is / is not agent-owned: the audit function is first-party and specific, but autonomous audit ownership still requires composition of the verifier callback; deterministic acceptance commands alone do not make the decision agent-owned.
- Evidence: `dispatch/acceptance.py`, `core/brain.py`, `cli/runtime.py`.
- Basis: explicit + structural
- Confidence: high
- Caveats: deployments that supply an autonomous verifier can close the agentic reviewer role, but canonical classification records the standard distribution rather than a possible custom composition.
- Claim being audited: that a dispatched executor completed the requested goal and acceptance criterion.
- Ordinary reporting path: the executor returns its result to Chief's dispatch preparation path.
- Complementary access path: Chief runs an acceptance command or sends the acceptance criterion plus result to a separate optional verifier callback instead of trusting the executor claim.
- Independence boundary: the verifier path is distinct from the executor result path, but first-party standard wiring leaves autonomous verifier identity/authority to composition.
- Who acts on findings: Chief's dispatch preparation loop retries once and then escalates the rejected result to the human path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external/prospective adaptation function is established at the selected boundary.
- Disturbance / variety regulated: user preference drift and historical response quality are adapted, but not as an outside-and-then organizational intelligence loop.
- Decisive decision or feedback right: no material first-party right was found that converts external/future distinctions into adaptation options returned to present capability/S3.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: feedback signals, EMA weights, learned pins, threshold tuning, classifier reseeding and nightly policy distillation.
- Closure path: feedback changes future routing preferences directly inside S1; no distinct external/prospective option-development conversation is established.
- Why this is / is not agent-owned: learning and personalization alone do not establish S4 under the Profile.
- Evidence: `core/learner.py`, `docs/architecture.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: future product research or maintainer development is outside this runtime assessment.

### Absence scope

- Surfaces inspected: learner, memory, nightly distillation, eval/drift tooling, architecture and runtime scheduling.
- Plausible first-party paths checked: preference learning, drift/calibration evaluation, policy distillation and memory association.
- Why no material first-party path remains: the shipped loops learn from current/past user feedback to tune the operating service; they do not sense an external/future environment, generate adaptation options and return a selected option into current capability/S3.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy governance loop is established at the selected runtime boundary.
- Disturbance / variety regulated: user routing preferences and operational policy constraints are represented, but no ultimate organizational identity dispute is evidenced.
- Decisive decision or feedback right: no material first-party identity/ultimate-policy decision right with a complete authority-and-return loop was found.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: `POLICY.md`, user profile/configuration, hard rules and learned preference distillation.
- Closure path: operational preferences affect routing directly; they do not establish an S5 identity/ultimate-policy closure.
- Why this is / is not agent-owned: a policy file or human-editable rule is not S5 merely because it constrains operation.
- Evidence: `docs/architecture.md`, `core/policy.py`, `core/learner.py`.
- Basis: structural
- Confidence: high
- Caveats: a larger organization embedding Chief could supply S5 outside this boundary.

### Absence scope

- Surfaces inspected: policy templates/loader, user profile, config, learner distillation, Brain hard rules and operator surfaces.
- Plausible first-party paths checked: user rules, learned policy lines, mute/promote signals and configuration changes.
- Why no material first-party path remains: these are operational preference/control inputs; no identity-level issue is routed to a legitimate ultimate authority and returned as an authoritative organizational identity decision.

## Recursion

Chief can connect to external agents and tools, but the pinned evidence does not establish recursively nested viable Chief organizations. External executors are treated as environment/hosts unless independently assessed.

## Variety and escalation

Chief attenuates event variety through cheap deterministic filters before model judgment, then through scene-sensitive delivery levels and bounded dispatch verification. Repeated dispatch-verification failure escalates to a human instead of silently accepting the claim.

## Evidence gaps

No qualifying S2, S3, S4 or S5 path was found after inspecting the standard runtime and its principal control/learning surfaces. S3* is constructor because the autonomous verifier role is explicitly supported but not wired as a standard resident owner.
