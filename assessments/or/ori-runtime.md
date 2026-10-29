---
harness_id: ori-runtime
project_name: Ori Runtime
repository: https://github.com/ori-platform/ori-runtime
review_ref: 64d95bad6c5d173e249f31ed4b0d6c8e9df83c99
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ori Runtime

## Review boundary

- System in focus: installed Python Ori edge-device runtime and bundled sensor/skill work cells, Intelligence Elevator and governed Action Dispatcher at the frozen ref; not the separate Ori cloud company, firmware author or external operator's whole organization.
- Purpose and identity: observe device/site events, autonomously produce operator-facing diagnoses/advice, and execute configured informational or commissioned physical actions under a strict safety/approval envelope.
- Relevant environment: changing physical sensor conditions, local equipment, operator approvals/rejections, intermittent network, attached gateways, local model file and site commissioning state.
- Standard-distribution boundary: first-party `ori/runtime`, `ori/reasoning`, `ori/skills`, `ori/state`, `ori/actions`, safety and policy modules, including built-in skills. Model weights, devices and operator inputs are externally provided; first-party code wires inference and action loops.
- Credited operating / distribution surfaces: event bus → per-skill triggers and contextual model inference → operator informational action/records; independent triggered skill cells; event-wide dispatch planning and resource conflict gate.
- Adjacent first-party surfaces excluded from ownership: project CI/release/evidence lab, installer development, public demo, separate Ori cloud backend, source-only future safety design, hardware companion firmware and hypothetical downstream custom skills.
- Operating modes considered: rule-only/offline safety; local SLM available; optional MQTT gateway reasoning; first-party multiple concurrent sensor skills; Tier A informational, Tier B/C commissioned/approved and Tier D hardwired safety actions.
- Recursion level: one deployed Ori device's operational work cells; not a multi-site company or operator safety governance body.
- Reviewed revision: `64d95bad6c5d173e249f31ed4b0d6c8e9df83c99` on 2026-10-29. Generated and current Profile/Methodology: 0.2.4 / 0.3.7.

## Repository architecture and decisive boundary distinction

The runtime receives sensor events, identifies matching first-party skill triggers and runs `IntelligenceElevator.reason_and_dispatch`. With a configured local SLM or gateway, the model receives current event/history context and produces a free-form diagnostic/operator message; future events can include recent sensor history and a prior operator rejection. This constitutes a bounded agent-owned *informational/diagnostic* outcome. The model does **not** receive unrestricted physical actuation rights: `LocalLLM.reason` explicitly returns tier A and no proposed action, and the Elevator clamps a matched rule to its declared tier. `_actions_for_rule_result` chooses matched physical/default actions from skill declarations; `DispatchPlan`, resource admission and Tier C approval are host/constructor safety enforcement. The hard Tier D protective branch fires before LLM inference. Thus S1=A is narrow and must not be read as autonomous model authority to open relays or change commissioning policy.

Primary evidence, all pinned:

- [README and deployed tiers](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/README.md).
- [LLM informational output authority](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/local_llm.py).
- [Event→reasoning→action and safe clamping](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/elevator.py).
- [Multi-skill event planning and Tier D ordering](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/dispatch_coordinator.py).
- [Resource identity/opposing outcomes](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/dispatch_plan.py).
- [Site-global conflict gate](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/resource_gate.py).
- [Tier A/B/C/D dispatcher](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/reasoning/action_dispatcher.py).
- [Remote verified policy application](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/runtime/_device_policy.py) and [DevicePolicy privileges](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/ori/policy/device_policy.py).
- [Capability matrix / shipped-vs-planned boundary](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/docs/CAPABILITY_MATRIX.md); [physical trust principles](https://github.com/ori-platform/ori-runtime/blob/64d95bad6c5d173e249f31ed4b0d6c8e9df83c99/PRINCIPLES.md).

## S1 — Operations

- State: A
- Function: autonomously interpret environmental sensor evidence into diagnostic/operator guidance, within declared skill outcomes, and use later sensor/operator history for the next informational response.
- Disturbance / variety regulated: unusual readings, changing measured conditions, incomplete history, operator-provided rejection reasons and model-dependent natural-language diagnosis.
- Decisive decision or feedback right: generate situation-specific explanation/advice for operator-facing Tier A information rather than replaying a fixed notification string.
- Decision owner: local SLM or configured gateway model, invoked by the first-party Elevator inside an installed skill/event loop; deterministic rules own physical action selection.
- Supporting / enforcement mechanisms: sensor event bus, rule engine, contextual prompt builder, causal-memory and history store, action-tier clamps, configured alert/log executors.
- Closure path: sensor event and remembered evidence → model-generated diagnosis → informational message delivered/logged → later sensor event/rejection history enters the next model prompt; physical actions follow separately declared rule/policy rights.
- Why this is / is not agent-owned: the diagnosis content is model-selected under input variety, while trigger matching and relay commands remain deterministic. Only the former supports S1=A.
- Evidence: `ori/reasoning/local_llm.py`, `elevator.py`, `dispatch_coordinator.py`, `state/_reasoning.py` and README (links above).
- Basis: source-first narrow affirmative boundary.
- Confidence: medium-high.
- Caveats: no bundled model weights; rule-only mode has no autonomous model diagnosis and cannot support the same agent ownership claim alone.
- Boundary reachability: installed local-SLM path is first-party wired in `reason_and_dispatch`; `LocalLLM.reason` runs the model and returned text reaches `event.context['operator_message']` and bundled informational executors.

## S2 — Coordination

- State: C
- Function: attenuate concrete contradictory and duplicate physical acts from independently event-triggered operational skill cells targeting the same commissioned resource.
- Disturbance / variety regulated: one skill's protective open command versus another skill's close/reconnect proposal, or two triggers redundantly commanding the same act on one physical zone.
- Decisive decision or feedback right: coalesce equivalent outcomes and refuse/preempt incompatible outcomes according to commissioned resource identity, authority tier and in-flight state.
- Decision owner: first-party constructor-authored `DispatchPlan`/`ResourceGate` policy; operating models do not negotiate collision priority or grant actuation rights.
- Supporting / enforcement mechanisms: event-wide discovery, `ResourceIdentity(resource_key, desired_outcome)`, context-scoped holder record, Tier D preemption, refusal outcomes and cooldown accounting.
- Closure path: two active skill plans claim an actuator → resource gate recognizes same-resource opposite/equal outcome → duplicate joins or lower-priority conflict is refused/preempted → the caller records refusal/attempt status, suppresses duplicate execution and corrects later cooldown/retry behavior.
- Why this is / is not agent-owned: this is substantive inter-operational interference regulation, but its decisive tie-breaking and refusal logic are fixed in the packaged constructor, so **C**, not model-owned A.
- Evidence: `dispatch_plan.py`, `resource_gate.py`, `dispatch_coordinator.py` (pinned links above).
- Basis: structural implementation witness, not live physical field test.
- Confidence: medium-high.
- Caveats: the S1 cells are independently event-triggered skill operations sharing an inference substrate, not separate permanently running LLM processes; S2 credit is bounded to their actuator conflict, not arbitrary inter-agent messaging.
- Distinct S1 units: separate bundled sensor/skill trigger work cells can act independently on environmental events and generate advice/actions for their local condition; the coordinator schedules each separately.
- Inter-S1 disturbance: opposite actions `open_protected_circuit` and `close_protected_circuit` share a resource key, while equal desired outcomes could execute twice.
- Attenuating coordination relation: `ResourceGate` arbitrates holders by resource identity, outcome, scope and current state; `DispatchCoordinator` attempts Tier D before other work.
- Feedback into subsequent S1 behaviour: refusal and coalesced/attempted outcomes enter `DispatchOutcome`/cooldown handling and prevent a denied action from consuming a turn; only successfully attempted/proposed work changes cooldown.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: implemented physical opposite-outcome contention and duplicate-act suppression are specific cross-cell interference, not just an event bus or task sequence.
- Boundary reachability: shipped dispatcher/coordinator/gate operate on first-party skill plans whenever multiple matching triggers target a commissioned resource.

## S3 — Inside-and-now control

- State: —
- Function: no separate discretionary whole-device current management of autonomous agent commitments/resources has been demonstrated beyond safety arbitration and configured permissions.
- Disturbance / variety regulated: local sensor/actuator contention, Tier D urgency and action approval are real operational disturbances but are resolved by fixed per-event rules.
- Decisive decision or feedback right: reprioritize whole-device goals and current agent commitments or make an exception-based intervention on behalf of all S1 units.
- Decision owner: none supplied for that broader right; installer/operator/skill author supplies targets and limits, while the dispatcher enforces them.
- Supporting / enforcement mechanisms: resource gate, event-wide Tier D ordering, action tiers, DevicePolicy, approval state and runtime health.
- Closure path: per-event rule/dispatched action → record/refusal; no model/supervisor uses a whole-agent operational view to revise current priorities across missions.
- Why this is / is not agent-owned: high-consequence deterministic protection and scope-specific S2 collision handling cannot be promoted into S3 current discretionary management without a distinct whole-system intervention decision.
- Evidence: `dispatch_coordinator.py`, `resource_gate.py`, `action_dispatcher.py`, `policy/device_policy.py`.
- Basis: bounded negative review.
- Confidence: medium-high.
- Caveats: a wider physical plant operator organization may supply S3 outside this runtime.

### Absence scope

- Surfaces inspected: event-wide discovery, resource gate, runtime health, policy refresh, approvals, Tier D preemption and skill scheduler.
- Plausible first-party paths checked: dispatcher as whole-system manager, Tier D preemption as S3 and remote DevicePolicy as supervisory current resource allocation.
- Why no material first-party path remains: each executes preselected resource/authority semantics without a discretionary cross-mission view and corrective current-control judgment.

## S3* — Complementary audit

- State: —
- Function: no independent audit judgment using an alternate operational truth channel returns findings to whole-system control.
- Disturbance / variety regulated: chain-signed action receipts, remote telemetry, safety evidence and tests can document physical claims.
- Decisive decision or feedback right: challenge S1/controller claims with complementary independent observations, judge them and return corrective findings.
- Decision owner: an independent auditor is not packaged in the assessed standard runtime; operators/developers may inspect exported evidence.
- Supporting / enforcement mechanisms: evidence ledger/signing, action logs, health telemetry, hardware validation docs and tests.
- Closure path: the runtime emits records and signed evidence → external analysis is possible; no first-party auditor's finding autonomously changes current control.
- Why this is / is not agent-owned: cryptographically durable records are evidence quality/transport, not an independent operational reality judgment loop.
- Evidence: `docs/CAPABILITY_MATRIX.md`, `ori/reasoning/action_dispatcher.py`, `ori/runtime/_device_policy.py`.
- Basis: bounded negative review.
- Confidence: medium-high.
- Caveats: field measurements and third-party auditors may enable a separate S3* composition.

### Absence scope

- Surfaces inspected: Tier C/D evidence chain, signed telemetry, health socket, reasoning/action logs, hardware test evidence and approval history.
- Plausible first-party paths checked: signed ledger as audit; routine action verification as independent challenge; lab evidence as deployed S3*.
- Why no material first-party path remains: sources record/check the producing path or are development fixtures, with no autonomous or independent audit claimant and corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established external-and-prospective capability adaptation loop returns future options to present device control.
- Disturbance / variety regulated: causal memory and operator rejection can change future explanations, but remain feedback about recurring present events.
- Decisive decision or feedback right: assess future external developments, select an adaptation option and install a changed operational capability.
- Decision owner: downstream operator/developer/cloud policy issuer; not first-party prospective intelligence.
- Supporting / enforcement mechanisms: contextual memory, dynamic skill loading, Model/Gateway tier, config/policy refresh, capability matrix and release engineering.
- Closure path: earlier sensor/response data enters later prompts; no future-oriented alternative is tested/selected and returned into the device's capability portfolio.
- Why this is / is not agent-owned: learning-like cached explanations and event adaptation are not S4 without future/external modeling and a capability-change return.
- Evidence: `elevator.py`, `state/_reasoning.py`, `runtime/_device_policy.py`, `docs/CAPABILITY_MATRIX.md`.
- Basis: bounded negative review.
- Confidence: high.
- Caveats: platform roadmap and future installer changes are developer work outside the standard deployed operational loop.

### Absence scope

- Surfaces inspected: causal memory, operator rejection notes, model/gateway tier selection, policy refresh, runtime skill config and capability roadmap.
- Plausible first-party paths checked: feedback as learning, remote policy updates as adaptation, new skills as prospective strategy.
- Why no material first-party path remains: updates are external commands/config/retrospective feedback, not a first-party future-option selector returning into S3.

## S5 — Policy and identity

- State: —
- Function: signed DevicePolicy/commissioning authorization enforces permitted actuation, but no evidenced identity-level issue → legitimate ultimate authority decision → returned governance closure is packaged.
- Disturbance / variety regulated: dangerous actuation, unauthorized equipment access, cloud privilege leases, operator approval and skill signing.
- Decisive decision or feedback right: decide Ori's ultimate organizational identity/ethos and resolve genuine policy-level tensions between present safety and future adaptation.
- Decision owner: deployment operator/issuer/maintainer outside the assessed runtime; it chooses policy, equipment commissioning and authority tiers.
- Supporting / enforcement mechanisms: runtime-fixed Tier D safety, Tier C human transaction, `DevicePolicy` signature verification, remote refresh, local approver registry and resource binding.
- Closure path: external policy bundle → signature validation → installed enforcement → actions permitted/refused; this is a returned **configuration**, but not evidence of an explicit identity-level issue adjudicated by ultimate authority.
- Why this is / is not agent-owned: even a strong safety constitution, signed grants and ordinary YES/NO approvals are constraints/enforcement rather than a legitimate ongoing S5 decision loop at this recursion.
- Evidence: `PRINCIPLES.md`, `policy/device_policy.py`, `runtime/_device_policy.py`, `action_dispatcher.py`.
- Basis: bounded negative review.
- Confidence: medium-high.
- Caveats: the site owner may be S5 at a larger human-plant organizational boundary; it does not become product runtime-owned by remote policy transport alone.

### Absence scope

- Surfaces inspected: site commissioning, signed DevicePolicy acceptance, remote issuer refresh, Tier C approvers, Tier D invariant, principles and runtime enforcement.
- Plausible first-party paths checked: Physical Actuation Trust constitution, remote policy issuer as S5 parent, operator approval as policy return, immutable Tier D as identity choice.
- Why no material first-party path remains: no identity-level proposal/conflict is delivered to legitimate ultimate authority and resolved back in a traced governing decision; the verified bundle is external configuration and ordinary action permission.

## Recursion, variety and escalation

Sensor/skill cells are distributed operating contributions but not separately proven viable six-function subsystems. Sensors → triggers → operator diagnosis carry environmental variety; model explanations can be revised by history while a hard safety envelope attenuates physical risk. Resource contention is returned as refusal/coalescing and Tier C demands explicit approval. Alerts and failure statuses do not alone prove an algedonic metasystem.

## Evidence gaps

- Static pinned-source review; no real circuit, gateway, cloud, model-weight or paid-provider E2E run. Published hardware test documents are background validation, not observations reproduced here.
- S1=A is constrained to semantically discretionary *informational diagnosis*. Never interpret it as LLM-selected Tier B/C/D actuation, because source explicitly denies those privileges.
- Causal memory and signed policies are strong mechanisms but cannot substantiate S4/S5 by names alone. The independent S3* audit claim is not made.

## Assessment summary

**Proposed disposition: `included`**, bounded vector **A · C · — · — · — · —**. Ori's built-in agentic reasoning produces context-sensitive operator advice under event feedback (S1=A); the constructor-specified resource gate resolves actual conflicting physical actions among independent skill cells (S2=C). The model does not own relay decisions; deterministic safety, record signing, policy refresh and approvals do not by themselves close S3, S3*, S4 or S5.
