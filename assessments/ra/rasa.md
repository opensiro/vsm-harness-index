---
harness_id: rasa
project_name: Rasa
repository: https://github.com/RasaHQ/rasa
review_ref: 60a3cff9c08183760355b07bd60f5223d8916d6b
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 60a3cff9c08183760355b07bd60f5223d8916d6b
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rasa

## Review boundary
Classic Rasa Open Source as one deployed conversational assistant at the pinned revision. The system-in-focus is the runtime dialogue assistant, not Rasa's developer organization or an external contact-center operation.

## Repository architecture
`Agent`/`MessageProcessor` drive a dialogue loop over `DialogueStateTracker`; multiple trained policies produce next-action predictions and `DefaultPolicyPredictionEnsemble` deterministically chooses a final prediction. Ticket locks serialize concurrent processing for the same conversation. Fallbacks, two-stage clarification, rules and human handoff are configured exception paths.

## Primary evidence
- `rasa/core/agent.py` and `rasa/core/processor.py`: tracked dialogue state drives next-action prediction/execution.
- `rasa/core/policies/ensemble.py`: policy predictions are combined by fixed confidence/priority and rejection rules into one final prediction.
- `rasa/core/lock_store.py`: ticket locks deterministically serialize processing for a conversation id.
- `docs/docs/fallback-handoff.mdx`: low-confidence fallback, two-stage fallback and eventual human handoff are configured through classifiers, rules, thresholds and actions.

## Operational model
The dialogue assistant is one S1. Policy arbitration, locks and fallback mechanisms regulate execution inside that S1; they are not autonomous organizational actors above multiple S1 units.

## S1 — Operations
`A`: the runtime owns bounded next-action selection from current dialogue state and continues from action/user events. Confidence: high.

## S2 — Coordination
`—`: no multiple autonomous operational units requiring agent-owned mutual adjustment are supplied at this boundary. Ticket locks serialize technical access to one conversation and policy ensembles arbitrate internal action predictions; neither is cross-S1 coordination. Confidence: high.

## S3 — Inside-and-now control
`—`: the reviewed standard distribution supplies no autonomous whole-system regulator with a current view of multiple operations plus authority over their shared resources, commitments or priorities. Policy arbitration remains part of the S1 decision loop. Confidence: high.

## S3* — Complementary audit
`—`: tests, diagnostics and fallback checks do not supply a sufficiently independent runtime auditor with complementary access to operational reality and a corrective channel. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: training, NLU confidence, unexpected-message handling and fallback react to or learn from inputs but do not provide a distinct external-and-prospective intelligence function coupled back to S3. Confidence: high.

## S5 — Policy and identity
`—`: domains, rules, thresholds and fallback/handoff policies are authored/configured by developers. No agent-owned ultimate identity/policy authority or S3–S4 closure is supplied. Confidence: high.

## Recursion, variety, escalation
Dialogue state and policy ensembles attenuate conversational variety into one action. Fallback/handoff escalates exceptions to configured actions or humans, but escalation alone does not create S5 or recursive viability.