---
harness_id: provable-harness
project_name: provable-harness
repository: https://github.com/0x471/provable-harness
review_ref: c9055e9e5c010997c5ae174ae165b1ec5de9320e
reviewed_at: 2026-11-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# provable-harness

## Review boundary

- System in focus: one provable agent session plus shipped witness, prover and separately invocable verification surface.
- Purpose and identity: execute bounded model-directed tasks and make operational claims independently checkable.
- Relevant environment: user task, committed workspace, network tools, model gateway/oracle or zkTLS notary and verifier expectations.
- Standard-distribution boundary: ph-core, host ph CLI, SP1 guest and first-party zkTLS adapters; external model, notary trust, SP1 implementation and external verifier organization not credited as internal agents.
- Credited operating / distribution surfaces: ph run, native and Rhai tool modes, signed gateway/oracle and zkTLS modes, ph prove and ph verify.
- Adjacent first-party surfaces excluded from ownership: eval suites/fixtures and graders as separate research mode, fuzzing, adversary examples and maintainer roadmap; may corroborate architecture.
- First-party operating / deployment modes considered: signed or notarized live session; native replay, optional proof and independent verifier with pinned anchors/challenge or unchallenged mode.
- Recursion level: a single local task-running harness with verifier interface, not a fleet or evaluation lab.
- Reviewed revision: c9055e9e5c010997c5ae174ae165b1ec5de9320e.
- Observation date: 2026-11-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The same sans-IO session core drives live calls and witness replay. The model selects scripts or native calls; tool policy validates actual arguments. The live host exports authenticated evidence and claims, then separate SP1 guest execution rebuilds context and checks witness integrity. The separate verifier checks proof and independently pinned scenario, keys, session and optional disclosures. Eval suites separately replay multiple fixture cases and grades; these are not additional cooperating operational agents. See [core/src/session.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/session.rs#L101-L310), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L321-L655), [docs/DESIGN.md](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/docs/DESIGN.md).

## Operational model

One model-backed operational agent owns local action selection. Tool/metering/attestation paths enforce constraints. The verifier can reject claims against its own expectations, but a model-driven audit and follow-up actor is not supplied. Static configuration is not parent-governed S3/S4/S5 closure.

## S1 — Operations

- State: A
- Function: Execute a task by selecting model-authored native tool calls or Rhai scripts against a committed workspace and permitted external APIs.
- Disturbance / variety regulated: Uncertain task environment, external results, denied calls and intermediate errors.
- Decisive decision or feedback right: Select subsequent calls and final answer from accumulated feedback.
- Decision owner: Model-backed operational agent.
- Supporting / enforcement mechanisms: Deterministic session loop, policy, script engine, native tools, authenticated backend.
- Closure path: Tool results enter later model context; model stops by returning no tool calls/script or runtime caps the run.
- Boundary reachability: Standard ph run constructs SessionInput and calls run_live, whose real gateway/zkTLS model backend drives run_session.
- Why this is / is not agent-owned: Without the model, policy and runtime cannot choose task actions.
- Evidence: [core/src/session.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/session.rs#L155-L263), [host/src/live.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/live.rs#L200-L260), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L321-L392)
- Basis: explicit
- Confidence: high
- Caveats: Configured budgets may terminate a session independently; no live execution performed.

## S2 — Coordination

- State: —
- Function: No material inter-S1 coordination at one-session recursion.
- Disturbance / variety regulated: Potential concurrent operational interference; no distinct cooperating live S1 cells established.
- Decisive decision or feedback right: No inter-unit coordination decision.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Serial model turns, call sequencing, witness slot numbering and independent eval runs.
- Closure path: No feedback that adjusts relations between separate operational units.
- Why this is / is not agent-owned: Tool calls are actions of one agent, not independent S1 units; notary slot constraints prevent evidence manipulation, not cross-S1 interference.
- Evidence: [core/src/session.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/session.rs#L169-L263), [core/src/eval.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/eval.rs#L668-L743), [docs/DESIGN.md](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/docs/DESIGN.md)
- Basis: structural
- Confidence: high
- Caveats: Multiple independently challenged evaluation sessions are not a coordinated operating organization.

### Absence scope

- Surfaces inspected: Session, live backend, eval batch and notary design.
- Plausible first-party paths checked: Native/script calls, repeat/case runs, sequential attestation slots.
- Why no material first-party path remains: One operational model per session; eval aggregates independent cases and no inter-S1 feedback path is supplied.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system discretionary current-control path beyond one bounded session.
- Disturbance / variety regulated: Potential resource or commitment variation.
- Decisive decision or feedback right: No substantive resource bargaining/reallocation right established.
- Decision owner: Scenario author selects fixed constraints; runtime enforces.
- Supporting / enforcement mechanisms: Policy limits, metering, taint, session step cap, proof acceptance.
- Closure path: Denial/error feedback changes local task action; no shared current commitments supervision.
- Why this is / is not agent-owned: The agent selects actions under limits; neither static budgets nor post-run verifier imply whole-system allocation. Parent scenario choice is configuration, not a returned current-control intervention.
- Evidence: [core/src/policy.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/policy.rs#L20-L157), [core/src/session.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/session.rs#L101-L169), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L321-L392)
- Basis: structural
- Confidence: high
- Caveats: No claim about an external fleet or operator organization.

### Absence scope

- Surfaces inspected: Policy, session, live host, CLI run/prove/verify and eval batch.
- Plausible first-party paths checked: Budget enforcement, operator scenario selection, proof rejection, evaluation counters.
- Why no material first-party path remains: Fixed per-session constraints and after-run evidence do not supply a current whole-system discretionary decision loop or its parent variant.

## S3* — Complementary audit

- State: C
- Function: Enable independently anchored reconstruction and rejection of operational claims rather than trusting the producing operator's report.
- Disturbance / variety regulated: Forged or selectively reported actions, policy, outcome and attested results.
- Decisive decision or feedback right: Determine whether to challenge a session and accept its evidence against independently chosen expectations; use findings for control.
- Decision owner: External verifier/operator or a composed autonomous reviewer; no shipped agent owns this decision.
- Supporting / enforcement mechanisms: Authenticated witness, guest replay, embedded verifying key, cryptographic checks, verifier-owned scenario/keys/challenge, optional disclosures.
- Closure path: Separate verifier accepts/rejects claim; nonzero verification failure can gate reliance on a run; an autonomous control actor consuming the verdict needs composition.
- Boundary reachability: ph prove and ph verify are first-party CLI paths, with separately supplied verifier expectations and optional session challenge.
- Why this is / is not agent-owned: The model that produced the run cannot choose the verifier's independently pinned expectations; deterministic proof verification implements the check, not autonomous audit judgment.
- Evidence: [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L395-L432), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L464-L575), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L614-L655), [core/src/witness.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/witness.rs#L331-L353), [program/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/program/src/main.rs#L16-L21), [host/src/prover.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/prover.rs#L100-L132)
- Basis: explicit/structural
- Confidence: medium
- Caveats: Constructor, not A: no first-party model reviewer that selects scrutiny and acts on findings. Non-collusion and independently sourced anchors required; does not prove model computation or outside-harness behavior. Eval-only grading not borrowed.

- Claim being audited: session ran specified task, policy, tool actions and claimed outcome under pinned authentication.
- Ordinary reporting path: live cmd_run exports claim, transcript, final workspace and action log.
- Complementary access path: separate guest replay rebuilds requests from authenticated responses; proof verification checks vk and verifier-owned expectations, optionally raw disclosure commitments.
- Independence boundary: verifier supplies own anchors and challenge, independently checks proof; same core is replayed but operator cannot rewrite authenticated evidence under the trust assumptions.
- Who acts on findings: verifier or caller rejects failed verification; autonomous follow-up/rework authority must be composed.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environmental adaptation loop.
- Disturbance / variety regulated: Future external threats or capability changes.
- Decisive decision or feedback right: No adaptation-option decision established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: HTTP tools, evaluation suites, proof reports and maintainer design notes.
- Closure path: Current task context and after-run report only; no return of future options into harness capability.
- Why this is / is not agent-owned: Evaluation can support a researcher but the product has no shipped adaptation actor or function-specific decision channel returning options to operation.
- Evidence: [core/src/session.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/session.rs#L169-L280), [core/src/eval.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/eval.rs#L668-L743), [docs/DESIGN.md](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/docs/DESIGN.md)
- Basis: structural
- Confidence: medium
- Caveats: Do not credit the prototype's development roadmap as operational intelligence.

### Absence scope

- Surfaces inspected: Live runtime, evaluation and verification paths, design roadmap.
- Plausible first-party paths checked: Web/tool sensing, attack evaluation, operator scenario edits and future design notes.
- Why no material first-party path remains: No first-party loop maps external future changes into adaptation options and returned capability decisions, even with parent involvement.

## S5 — Policy and identity

- State: —
- Function: No ultimate-policy or identity dispute-resolution loop.
- Disturbance / variety regulated: Potential conflict of trust, policy and purpose.
- Decisive decision or feedback right: No runtime ultimate-policy decision right established.
- Decision owner: Scenario/verifier configuration is externally supplied.
- Supporting / enforcement mechanisms: Policy hash, expected keys, tool rules and verifier identity checks.
- Closure path: Static input constrains execution and verification; no returned identity decision.
- Why this is / is not agent-owned: Cryptographic program identity is not organizational identity governance; static policy and verifier expectations are not a legitimate parent resolving a policy-level dispute.
- Evidence: [core/src/policy.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/core/src/policy.rs#L20-L105), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L350-L366), [host/src/main.rs](https://github.com/0x471/provable-harness/blob/c9055e9e5c010997c5ae174ae165b1ec5de9320e/host/src/main.rs#L480-L575)
- Basis: structural
- Confidence: high
- Caveats: No claim that outside institutions lack policy authority.

### Absence scope

- Surfaces inspected: Policy definition, scenario/live session, verification and design docs.
- Plausible first-party paths checked: User scenario/policy choices, trusted anchors, program vk, failed proof handling.
- Why no material first-party path remains: No first-party identity issue to ultimate authority and returned governing decision; inputs and proof acceptance remain fixed within one run.

## Recursion

No additional viable recursion inferred from script calls, proof replay or independent eval cases.

## Variety and escalation

Policy errors feed the model; fixed budgets bound steps and costs; evidence failures reject claims. No distinct algedonic channel established.

## Evidence gaps

Static source assessment only. No live provider, cryptographic benchmark or independent semantic audit executed. The independent verifier is a constructor for complementary audit, not proof of autonomous ownership; deployment trust assumptions are explicit.
