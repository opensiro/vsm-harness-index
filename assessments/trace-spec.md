---
harness_id: trace-spec
project_name: TRACE Specification
repository: https://github.com/agentrust-io/trace-spec
review_ref: 5222ed4e238627590fb21e801e0acdf7c9d78cbc
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TRACE Specification

## Review boundary

- System in focus: the first-party `agentrust-io/trace-spec` repository at pinned revision `5222ed4e238627590fb21e801e0acdf7c9d78cbc`, including the TRACE v0.2 specification/schema and the shipped `agentrust-trace` Python package for Trust Record models, adapters, validation, signing, verification, revocation/provenance, content marking and the optional intent bridge.
- Purpose and identity: define and implement a portable evidence format for recording what an AI agent ran, where, under which policy, touching which data and calling which tools, then allow that evidence to be signed and independently checked.
- Relevant environment: external agents and agent runtimes that produce execution/session evidence; policy and identity authorities; verifiers/auditors; trust roots and revocation sources; SCITT/transparency services; downstream tools consuming TRACE records.
- Standard-distribution boundary: the `trace-spec` repository's normative specification, schemas and `agentrust-trace` library are inside. Separate repositories named by the project itself — `trace-tests`, `trace-registry` and the cMCP reference implementation — are adjacent systems and are not imported as first-party runtime owners for this standalone assessment.
- Credited operating / distribution surfaces: `README.md`; `spec/trace-v0.2.md`; `schema/`; `src/agentrust_trace/models.py`; `src/agentrust_trace/sign.py`; `src/agentrust_trace/validate.py`; `src/agentrust_trace/revocation.py`; `src/agentrust_trace/provenance.py`; `src/agentrust_trace/content_marking.py`; `src/agentrust_trace/intent_bridge.py`; and `src/agentrust_trace/adapters/`.
- Adjacent first-party surfaces excluded from ownership: `trace-tests`, `trace-registry`, `agentrust-io/cmcp`, repository CI/fuzzing/release machinery, examples/tests, contributor/project governance and roadmap/RFC material that is not part of the shipped runtime-library boundary.
- First-party operating / deployment modes considered: direct library use to build/sign/verify TRACE records; AGT and sandbox adapters; optional revocation checking; provenance/content-marking/intent-bridge verification; use by an external agent runtime or verifier application.
- Recursion level: one installed TRACE evidence-format/library deployment. The external agent whose run is described by a Trust Record is environmental to this repository-relative system in focus.
- Reviewed revision: `5222ed4e238627590fb21e801e0acdf7c9d78cbc`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

TRACE explicitly identifies itself as an evidence specification rather than an agent execution harness. Its README describes an open specification for portable, signed runtime evidence about AI-agent runs and separately links `agentrust-io/cmcp` as the reference implementation. The standard distribution in this repository therefore defines the record/schema contract and ships a Python library for constructing, validating, signing and verifying those records.

The package export surface reinforces that boundary. `agentrust_trace.__init__` exports record models, schema validation, signing/verification, revocation checks and adapters. It does not export an agent loop, planner, tool executor or objective-processing runtime. `sign.py` owns cryptographic record operations and fail-closed revocation checks. The AGT adapter is explicit that it maps already-completed `govern()` session output to a TRACE Trust Record; it consumes an external agent identity, policy bundle, audit entries and chain tip rather than running the governed agent.

The optional intent bridge is also an evidence/authorization verifier. It signs and verifies a supplied authorization and checks that execution evidence matches that authorization. Its own comments distinguish evidence integrity from trust, freshness, independence and predicate sufficiency. This can constrain or verify an external execution, but it does not turn the TRACE library into the actor that receives an objective, selects substantive actions, observes operational results and decides what to do next.

The counterfactual owner test is decisive. Remove the external agent/runtime while retaining the specification, models, adapters, schemas, signing keys, verifiers, revocation sources and transparency integration. The remaining first-party system can represent, sign, validate and appraise evidence and authorization bindings, but it cannot pursue an operational objective through a model/tool decision/action/feedback loop. Repository-relative autonomous S1 does not close.

Under Methodology `0.3.6`, that first-party S1 admission failure yields a proposed terminal `excluded-no-agentic-vsm` result. Rich evidence, policy, provenance and verification machinery are not promoted into S2-S5 merely because they may serve those functions in a wider composed agent organization.

Primary evidence:

- [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md) — project identity as an evidence specification/library and explicit separation of test-suite, registry and cMCP reference implementation.
- [`src/agentrust_trace/__init__.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/__init__.py) — shipped package API: models, adapters, validation, signing, verification, revocation and provenance rather than an autonomous agent loop.
- [`src/agentrust_trace/sign.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/sign.py) — record signing/verification and caller-supplied revocation-status enforcement.
- [`src/agentrust_trace/adapters/agt.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/adapters/agt.py) — maps external AGT session output into a TRACE Trust Record and explicitly delegates higher-level hardware-rooted runtime operation to cMCP.
- [`src/agentrust_trace/intent_bridge.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/intent_bridge.py) — verifies signed authorization/evidence bindings; integrity is explicitly separated from wider trust/independence questions.

## Operational model

The first-party executable unit is an evidence library, not an autonomous operational agent. Callers supply execution/session facts or authorization artifacts; TRACE canonicalizes, validates, signs, verifies or transforms them. Substantive task selection and tool/action decisions are produced by an external agent/runtime. Verifiers or policy authorities likewise supply trust keys, revocation sources, appraisal inputs and authorization decisions that the library checks or preserves.

This means TRACE may be an important evidence/control substrate inside a viable agent organization without itself being the repository-relative S1 organization assessed by the Index. A wider composed assessment that includes cMCP or another autonomous agent runtime would be a separate system in focus.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action/feedback loop is established inside `trace-spec`.
- Disturbance / variety regulated: the library handles variation in record structure, signatures, provenance, revocation state, authorization bindings and evidence inputs; the task/environmental variety of the governed agent is handled outside the boundary.
- Decisive decision or feedback right: interpret an operational objective, choose the next substantive action/tool call, interpret returned environmental results and choose what follows.
- Decision owner: the external agent/runtime whose execution TRACE records or verifies.
- Supporting / enforcement mechanisms: JSON/schema models, canonicalization, signatures, key/revocation checks, record validation, adapters, provenance/content-marking checks and intent-bridge verification.
- Closure path: external agent/runtime acts → execution/session evidence is supplied to TRACE → first-party code structures/signs/verifies that evidence → result is returned to the caller/verifier; subsequent operational action remains a decision of the external runtime or its parent system.
- Why this is / is not agent-owned: the first-party package processes evidence about an agent run but does not itself receive the task objective and close a model/tool operational loop.
- Evidence: [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md); [`src/agentrust_trace/__init__.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/__init__.py); [`src/agentrust_trace/adapters/agt.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/adapters/agt.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: TRACE can be composed with an autonomous runtime and can preserve evidence from that runtime; composition does not transfer first-party S1 ownership into `trace-spec`.

### Absence scope

- Surfaces inspected: README/spec boundary, package exports, record models/validation, signing/verification, adapters, provenance/revocation/content-marking and intent-bridge surfaces.
- Plausible first-party paths checked: adapters as an agent loop; verifier/appraisal as an agent actor; intent bridge as goal-directed execution; record signing as action ownership; separate cMCP reference implementation as an in-repository runtime.
- Why no material first-party path remains: each shipped path consumes, represents, constrains or verifies externally supplied execution/authorization evidence; the reference execution runtime is explicitly separate from this repository.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 coordination function is established at the declared boundary.
- Disturbance / variety regulated: TRACE records can describe delegation/tool transcripts and multiple external actors may exchange records, but the library itself does not operate a population of distinct first-party S1 units with an interaction disturbance.
- Decisive decision or feedback right: no S2-specific coordination judgment over first-party S1 units is established.
- Decision owner: none established at this boundary.
- Supporting / enforcement mechanisms: record fields for delegation/origin/transcripts, schema constraints, canonicalization and validation.
- Closure path: evidence can be represented or verified, but no internal inter-S1 disturbance → coordination decision → changed later S1 behaviour loop closes in the standard distribution.
- Why this is / is not agent-owned: representing relationships among external agents is not the same organizational function as coordinating first-party S1 units.
- Evidence: [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md); [`src/agentrust_trace/__init__.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/__init__.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a multi-agent system may use TRACE records as coordination evidence, but that composed organization is outside this standalone repository boundary.

### Absence scope

- Surfaces inspected: record models, delegation/origin/transcript fields, adapters, intent bridge, verification and README integration topology.
- Plausible first-party paths checked: delegation metadata; shared evidence records; authorization bridge; registry/test-suite links; multiple adapter inputs.
- Why no material first-party path remains: no distinct first-party autonomous S1 population or S2-specific anti-interference feedback path is supplied by the repository.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous whole-system current-control function over internal S1 operations is established.
- Disturbance / variety regulated: malformed/stale/unauthorized evidence, invalid signatures, revoked keys and authorization mismatches can be rejected, but these are verification/enforcement concerns over externally generated operations.
- Decisive decision or feedback right: no actor inside `trace-spec` chooses current resources, commitments, priorities, constraints or interventions for a first-party operational whole.
- Decision owner: external policy authorities/verifiers supply the policy, keys, revocation sources or authorization whose conditions the deterministic library enforces.
- Supporting / enforcement mechanisms: `verify_record`, schema validation, fail-closed revocation checks, authorization verification and deterministic refusal paths.
- Closure path: supplied record/authorization → deterministic validation or verification verdict → caller accepts/rejects/handles the result; the current operational organization remains external.
- Why this is / is not agent-owned: hard verification and rejection are enforcement capabilities, not evidence of an autonomous manager owning current-control decisions over internal S1 units.
- Evidence: [`src/agentrust_trace/sign.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/sign.py); [`src/agentrust_trace/intent_bridge.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/intent_bridge.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: applications embedding TRACE can use verification verdicts as current-control inputs; downstream ownership is not borrowed into this assessment.

### Absence scope

- Surfaces inspected: signing/verification, revocation, schema validation, intent bridge, adapters, provenance/content marking and public integration docs.
- Plausible first-party paths checked: verifier as S3 manager; revocation fail-closed path as intervention owner; intent authorization as policy/current-control owner; appraisal fields as management view.
- Why no material first-party path remains: these paths apply externally supplied trust/policy conditions to evidence and do not establish a whole-system current view plus discretionary authority over first-party S1 operations.

## S3* — Complementary audit

- State: —
- Function: TRACE provides strong audit-evidence and independent-verification primitives, but no qualifying complementary audit loop over a first-party S1 operational reality closes inside this repository boundary.
- Disturbance / variety regulated: tampered records, invalid signatures, stale records, revoked keys, provenance inconsistencies and authorization/evidence mismatches.
- Decisive decision or feedback right: deterministic verification can reject evidence and external verifiers can appraise it, but no first-party independent auditor investigates internal S1 reality and returns corrective findings into internal operation.
- Decision owner: deterministic verification code plus the external verifier/trust authority supplying trusted material and deciding how a finding is acted on.
- Supporting / enforcement mechanisms: signatures, schema/profile checks, revocation, provenance verification, transparency references, appraisal fields and the optional intent bridge.
- Closure path: external operation produces evidence → TRACE structures/signs/checks evidence → a verifier obtains a verdict; corrective operational action, if any, belongs to the external governed organization.
- Why this is / is not agent-owned: cryptographic independence and verifiability are valuable audit properties, but Methodology S3* requires an organizational complementary-audit function with a corrective feedback path, not merely an evidence format/verifier.
- Evidence: [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md); [`src/agentrust_trace/sign.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/sign.py); [`src/agentrust_trace/intent_bridge.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/intent_bridge.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: in a wider system, an independent verifier consuming TRACE can participate in S3*. That wider auditor-and-operation closure is not packaged by `trace-spec` itself.

### Absence scope

- Surfaces inspected: record signing/verification, appraisal, revocation, provenance, content marking, intent bridge, transparency references and external test/registry/reference-runtime boundaries named by the README.
- Plausible first-party paths checked: verifier as complementary auditor; appraisal as audit judgment; transparency anchoring as independent access; trace-tests as auditor; intent-bridge successor observation as audit channel.
- Why no material first-party path remains: the repository supplies evidence and deterministic checks, while independent audit judgment/authority and return into operational behaviour remain external; the separate conformance suite is also outside the assessed distribution boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop that changes current operational capability is established.
- Disturbance / variety regulated: changing trust roots, revoked keys, schema/profile versions and external evidence conditions can change verification outcomes, but the library does not autonomously sense an environment, generate adaptation options and adopt one into an operational agent capability.
- Decisive decision or feedback right: no first-party actor owns prospective capability adaptation for an internal S1 system.
- Decision owner: maintainers/spec authorities and downstream operators decide upgrades, accepted profiles, trust material and integration changes outside a runtime S4 loop.
- Supporting / enforcement mechanisms: configurable trusted inputs, revocation sources, profile/schema versions, adapters and verification functions.
- Closure path: configuration/spec/library changes can alter later verification behaviour after human/downstream adoption; there is no autonomous environment → prospective analysis → adaptation decision → changed internal capability closure.
- Why this is / is not agent-owned: handling changing evidence or configuration is not itself prospective organizational adaptation.
- Evidence: [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md); [`src/agentrust_trace/sign.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/sign.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: specification evolution and Linux Foundation/project governance are real development/governance processes, but Methodology 0.3.6 excludes adjacent contributor/governance surfaces from runtime ownership.

### Absence scope

- Surfaces inspected: adapters, profile/schema handling, revocation, provenance, intent bridge, project README and adjacent governance/RFC boundaries.
- Plausible first-party paths checked: revocation refresh as adaptation; profile selection as adaptation; adapters as learning; intent bridge as prospective reasoning; specification evolution as runtime S4.
- Why no material first-party path remains: runtime-library paths validate supplied inputs; longer-term change is decided through external maintainer/spec/operator processes and is not an autonomous capability-adaptation loop of the assessed system.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy authority for an autonomous operational organization is established.
- Disturbance / variety regulated: TRACE can bind records to subjects, policies, confirmation keys, profiles and signed authorization artifacts, but those values/authorities are supplied by issuers, policy owners, verifiers or operators.
- Decisive decision or feedback right: define the identity and ultimate policy/purpose governing a first-party operational agent organization.
- Decision owner: external policy/identity authorities and project maintainers for their respective domains; the library validates or records their declarations rather than authoring runtime ultimate policy.
- Supporting / enforcement mechanisms: `subject`, policy metadata, confirmation keys, signatures, profile identifiers, authorization bridge and schema validation.
- Closure path: external authority supplies identity/policy/authorization → TRACE binds/verifies it → downstream runtime or verifier may enforce/act on the result; no first-party operational S5 authority returns policy into an internal S1 organization.
- Why this is / is not agent-owned: carrying signed identity/policy evidence does not make the evidence format the ultimate authority that chose those commitments.
- Evidence: [`README.md`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/README.md); [`src/agentrust_trace/adapters/agt.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/adapters/agt.py); [`src/agentrust_trace/intent_bridge.py`](https://github.com/agentrust-io/trace-spec/blob/5222ed4e238627590fb21e801e0acdf7c9d78cbc/src/agentrust_trace/intent_bridge.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the TRACE project has specification/governance authority over the standard itself, but project governance is an adjacent organizational recursion and is not the runtime S5 of an autonomous agent harness.

### Absence scope

- Surfaces inspected: record subject/policy/key/profile surfaces, signing/verification, intent bridge, adapters, specification identity and project governance boundary.
- Plausible first-party paths checked: policy claim as S5; signing key as identity authority; profile URI as identity; intent authorization as ultimate policy; LF/project governance as runtime S5.
- Why no material first-party path remains: all runtime identity/policy commitments are encoded, signed or verified from externally supplied authority; project/spec governance governs the standard, not a first-party autonomous operational organization inside `trace-spec`.

## Recursion

The repository exposes evidence artifacts that can cross organizational recursions, but the reviewed library itself does not instantiate a nested viable agent organization. The external agent/runtime, verifier and specification project are distinct neighboring or higher-level systems and are not collapsed into one assessed recursion.

## Variety and escalation

TRACE attenuates evidence variety through a common schema, canonicalization, signatures and verification rules. Invalid or untrusted evidence is rejected or surfaced to the caller. That is useful trust/evidence infrastructure, but escalation and subsequent operational response are owned by the embedding application, verifier, operator or parent organization.

## Evidence gaps

No material evidence gap changes the terminal boundary result. The review inspected the shipped package API, core verification/signing paths, external-runtime adapters and authorization bridge. Separate `trace-tests`, `trace-registry` and `cmcp` repositories may implement additional organizational roles, but importing them would define a different system in focus and requires separate assessment.