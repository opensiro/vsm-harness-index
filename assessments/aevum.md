---
harness_id: aevum
project_name: Aevum
repository: https://github.com/aevum-labs/aevum
review_ref: 72a31ba909be20f41cf4ac9d587de30b5dda13f8
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Aevum

**Canonical disposition:** excluded-no-agentic-vsm. Frozen source-first review for Index batch #1537 row 3, originally intake #1281. The kernel owns real enforcement and evidence; it must not inherit the external agent's autonomous S1.

## Review boundary

- System in focus: public Aevum governed evidence kernel and supported SDK/A2A adapters pinned to 72a31ba909be20f41cf4ac9d587de30b5dda13f8.
- Purpose and identity: produce independently verifiable agent-action evidence and an optional consent/policy/barrier governed path.
- Relevant environment: third-party agent frameworks, application callers, optional graph/ledger backends, consent principals, human reviewers, external auditors and signing infrastructure.
- Standard-distribution boundary: published aevum-core, recorder adapters, aevum-agent A2A interceptor and documented server surfaces. External agent reasoning, third-party corrective audit judgment and unpublished maintainer dogfood do not donate ownership.
- Credited operating / distribution surfaces: README.md, packages/aevum-core/src/aevum/core/{engine,kernel,barriers,functions,complications,audit}, published agents/adapters, public verification workflow.
- Adjacent first-party surfaces excluded from ownership: packages/aevum-maintainer (explicitly unpublished ops-only), tests/conformance and release/CI machinery; externally run agents and independent investigators.
- First-party operating / deployment modes considered: recorder-only integrations; Engine.ingest/query/review/commit/replay; Kernel.local; A2A signing; optional governed operation with hard barriers and human checkpoint.
- Recursion level: one Aevum kernel deployment serving external agents, not a bundled autonomous task executor.
- Reviewed revision: 72a31ba909be20f41cf4ac9d587de30b5dda13f8.
- Observation date: 2026-10-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped Engine wires graph, consent ledger, configured policy, signed audit ledger, five unconditional barriers, complication registry and pending human review. Its five operations take caller-provided data, context and proposed actions, return envelopes, and persist cryptographic evidence. Kernel.local verifies signed principles/keys and runs startup canaries. A2A interceptor signs Task envelopes and Agent Cards but states it does not replace the underlying A2A transport. Recorder SDK adapters attach to external hosts. The separate verifier establishes chain integrity, while the project's capture-faithfulness documentation explicitly distinguishes that from faithful observation. The maintainer self-governance package is explicitly not published to end users.

Counterfactual owner test: remove the external coding/business/decision agent and the human reviewer but leave Aevum installed. Signing, barrier checks, ledger/replay and record verification still function when called. No component thereby selects an open-ended agent goal, meaningful next tool action, or context-sensitive corrective action. That operational decision right belongs outside this first-party standard-distribution boundary.

Primary source links: [README.md](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md); [packages/aevum-core/src/aevum/core/engine.py](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/engine.py); [packages/aevum-core/src/aevum/core/kernel.py](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/kernel.py); [packages/aevum-core/src/aevum/core/barriers.py](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/barriers.py); [packages/aevum-core/src/aevum/core/functions/review.py](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/functions/review.py); [packages/aevum-agent/src/aevum/agent/interceptor.py](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-agent/src/aevum/agent/interceptor.py); [packages/aevum-maintainer/README.md](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-maintainer/README.md); [docs/concepts/capture-faithfulness.md](https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/docs/concepts/capture-faithfulness.md).

## Operational model

External agent or application invokes a recorder hook or governed kernel operation. Kernel first checks unconditional barriers/consent and configured policy; approved operations update the graph and ledger, denied/review-pending operations return results to the caller. An independent verifier may validate the recorded chain afterward. These are substantive first-party safeguards, but they do not transform the kernel into an autonomously deciding task agent.

## S1 — Operations

- State: —
- Function: No first-party autonomous semantic task operation is established.
- Disturbance / variety regulated: Open-ended goal interpretation, tool action choice and feedback belong to third-party agents.
- Decisive decision or feedback right: Choose a semantic action and revise later actions from observed tool results.
- Decision owner: The external agent/application; Aevum owns deterministic evidence/consent/policy responses.
- Supporting / enforcement mechanisms: Engine five functions, five hard barriers, ledger/sigchain and A2A task interceptor.
- Closure path: Caller invokes governed kernel → Aevum checks/signs/records → caller/agent decides and acts; no Aevum-managed autonomous model/tool loop.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: Real kernel controls are first-party but do not own agent task judgments.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/engine.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/kernel.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-agent/src/aevum/agent/interceptor.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-maintainer/README.md.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: README, Engine, Kernel, A2A interceptor and unpublished maintainer package.
- Plausible first-party paths checked: Kernel operation calls, complication hooks, adapter callbacks and signed A2A tasks.
- Why no material first-party path remains: The supported published packages validate/record caller actions; the A2A interceptor wraps external transport rather than executing agent cognition.

## S2 — Coordination

- State: —
- Function: No demonstrated first-party regulation of interference among distinct autonomous S1 units.
- Disturbance / variety regulated: Potential contention among external agent tasks, plugins and concurrent graph writes.
- Decisive decision or feedback right: Resolve a specific inter-S1 conflict and return attenuation feedback.
- Decision owner: No first-party autonomous S1 units or an S2 coordination owner identified.
- Supporting / enforcement mechanisms: Complication conflict detector, state registry, signed ordering and common graph.
- Closure path: Extension conflicts may prevent plugin installation; no coordination feedback into later actions of distinct agent S1 units.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: Registry or shared ledger is not an interference-specific S2 witness.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/engine.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-agent/src/aevum/agent/interceptor.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/complications/registry.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: Complication registry, A2A interceptor, Engine and multi-adapter documentation.
- Plausible first-party paths checked: Manifest conflicts, task status chaining, extension lifecycle and shared state.
- Why no material first-party path remains: No first-party S1 team and no concrete inter-S1 disturbance–attenuation–return path ships.

## S3 — Inside-and-now control

- State: —
- Function: Strong current enforcement exists without autonomous whole-system management judgment.
- Disturbance / variety regulated: Consent, crisis flags, classification, provenance, irreversible actions and pending human approval.
- Decisive decision or feedback right: Select substantive present priorities, resources and interventions from an entire operating system view.
- Decision owner: Human/app policy owner; hardcoded barriers and policy engine only enforce a chosen standard.
- Supporting / enforcement mechanisms: Hard barriers, consent, policy bridge, human GOVERN approve/veto, operation envelopes.
- Closure path: Caller proposes operation → kernel checks constraints → allow/deny or human decision → result returns to external caller.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: A non-bypassable decision gate is powerful enforcement but does not itself own whole-system S3 discretion for an autonomous agent organization.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/engine.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/kernel.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/barriers.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/functions/review.py.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: Kernel API, Engine operations, review store and hardcoded barriers.
- Plausible first-party paths checked: Policy/consent denial, reviewer checkpoint, current status and possible corrective intervention.
- Why no material first-party path remains: Checks are deterministic or human-supplied and no current-view manager controls first-party autonomous S1 operations.

## S3* — Complementary audit

- State: —
- Function: Independent cryptographic verification is supplied, but no first-party independent semantic-audit judgment plus corrective return.
- Disturbance / variety regulated: Tampered records, incomplete capture, incorrect operational claims.
- Decisive decision or feedback right: Independently observe operational reality, judge a claim and return findings to corrective management.
- Decision owner: Standalone cryptographic verifier proves record integrity; external auditor or regulator judges operational truth.
- Supporting / enforcement mechanisms: Signed sigchain, capture-gap events, replay and independent aevum-verify package.
- Closure path: Recorded action → third party verifies signatures/chain → external actor interprets findings; no internal corrective autonomous management loop.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: Tamper evidence cannot guarantee all actions were captured or that records tell the full truth.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/engine.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/docs/concepts/capture-faithfulness.md; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/functions/replay.py.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: medium-high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: Verification/faithfulness documentation, ledger APIs, replay, external reviewer path.
- Plausible first-party paths checked: Independent sigchain verification, record replay, gap signals, semantic anomaly findings and corrective action.
- Why no material first-party path remains: The shipped system provides evidence and verification, not a separate first-party audit-judgment actor feeding corrections into an operating agent.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally informed prospective adaptation judgment and returned change of agent capability is established.
- Disturbance / variety regulated: Evolving risks, frameworks, policies, compliance demands and extensions.
- Decisive decision or feedback right: Identify future external changes, choose adaptation and return it into live capability.
- Decision owner: Human maintainer, operator or external agent decides; Aevum persists and enforces changed settings.
- Supporting / enforcement mechanisms: Replay history, signed principles, canaries and extension registry/lifecycle.
- Closure path: Operator installs/changes policy/extension → kernel checks and applies; no first-party autonomous prospective option-generation loop.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: Persistence, registry and maintenance dogfood do not constitute agent-owned future intelligence.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/kernel.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/complications/registry.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-maintainer/README.md.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: Kernel canaries, replay, registry, public docs and excluded maintainer package.
- Plausible first-party paths checked: Event history, plugin update, policy revisions, research and compatibility changes.
- Why no material first-party path remains: Shipped mechanisms consume external adaptation decisions and do not close external sensing–prospective choice–capability change.

## S5 — Policy and identity

- State: —
- Function: No first-party autonomous organization-wide identity/ultimate-policy decision loop is closed.
- Disturbance / variety regulated: Who may access data, declare purposes, consent, govern actions and set immutable principles.
- Decisive decision or feedback right: Legitimately select ultimate system identity/purpose/policy and return that decision into operation.
- Decision owner: Human consent principal, deployer or organization; Aevum validates signed principles and policy.
- Supporting / enforcement mechanisms: Signed principles verifier, unconditional barriers, Cedar/OPA policy and GOVERN review.
- Closure path: External principal sets consent/policy → kernel validates, allows/denies or requests human decision → returned constraint applied to external agent actions.
- Boundary reachability: No positive first-party autonomous functional owner/constructor path is claimed at the assessed distribution boundary.
- Why this is / is not agent-owned: Static principles and human approval are enforceable constraints, not first-party S5 autonomous ownership or a qualifying parent mode for an autonomous first-party organization.
- Evidence: https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/README.md; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/kernel.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/barriers.py; https://github.com/aevum-labs/aevum/blob/72a31ba909be20f41cf4ac9d587de30b5dda13f8/packages/aevum-core/src/aevum/core/functions/review.py.
- Basis: explicit and pinned implementation, bounded negative review.
- Confidence: high.
- Caveats: Real governance, verification and signed evidence capabilities are recognized; no external system's cognition or corrective audit right is borrowed.

### Absence scope

- Surfaces inspected: Signed kernel principles, barrier module, human review, consent and public governance documentation.
- Plausible first-party paths checked: Operator goal selection, policy governance, human review, consent identity and approval.
- Why no material first-party path remains: The legitimate ultimate policy right remains external; no internally owned identity-policy decision and subsequent operating-system feedback loop.

## Distributed OSS parent arrangement

Independent downstream users and unpublished maintainer agents do not establish a shared published Aevum autonomous organization or its parent governance closure.

## Self-hosted and non-human modes

Both locally deployed and optional server paths implement deterministic governance/recording; separately integrated model agents retain their own task decisions. No parent-mode S3/S4/S5 is claimed without an actual first-party autonomous organization and function-specific parent decision/return loop.

## Recursion

Evidence episodes, subprocesses, signed task envelopes and extension registrations are not evidence of autonomous VSM recursion.

## Variety and escalation

Hard barriers, consent, fail-closed human GOVERN checkpoints, capture-gap records and signed receipts constrain risk and preserve provenance. Their existence alone cannot establish organizational S3/S3*/S4/S5 rights.

## Evidence gaps

- Frozen first-party source analysis only; no actual external model task run, end-to-end integration experiment or conformance execution was performed.
- Independent signature verification is material evidence access, but not a substitute for a complementary independent *judgment* about operational reality with a return path.
- If a user composes Aevum with a capable external agent and independent auditor, assess that explicit expanded system separately rather than reassign their functions to Aevum.

## Publication

This assessment became canonical following merged review PR #1542 and a separate admission PR. It is excluded, with catalog and deterministic projections updated and without any included-corpus signature or rank.

