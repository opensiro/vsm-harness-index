---
harness_id: bread-companion
project_name: Bread Companion
repository: https://github.com/ZJUZhiyuCai/bread-companion
review_ref: 058ad153e27bd6470a7e5ef4cab778a93d659a6d
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Bread Companion

## Review boundary

- System in focus: the shipped Bread Companion bounded conversational/evidence-task harness, including real provider validation/repair and contested-output review.
- Purpose and identity: support voluntary conversation, grounded notes/review and one-question interview practice while preserving user correction and saving authority.
- Relevant environment: user utterances/materials and corrections, provider failures, voice/text latency, stale asynchronous results and optional local archives.
- Standard-distribution boundary: the deployed browser application plus first-party server real-agent provider in text/call and listen/organize/review/practice modes. Model and speech services are external dependencies, not organizational owners borrowed into the product.
- Credited operating / distribution surfaces: RealAgentProvider, prompts, evidence/context builder, reducer, BreadController/RunController and optional rejection-review request/fallback.
- Adjacent first-party surfaces excluded from ownership: synthetic evaluations, benchmark/model-comparison scripts, formative research plans, repository CI/contributor governance and visual assets do not donate organizational functions.
- First-party operating / deployment modes considered: text and voice conversation, explicitly chosen evidence/practice work, user correction/rejection and confirmed local save/export. Mock provider is test support, not positive agent evidence.
- Recursion level: one deployed harness instance; child execution is not presumed recursively viable.
- Reviewed revision: `058ad153e27bd6470a7e5ef4cab778a93d659a6d`.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (Index active release; Skills main 0.3.8 inspected but not silently activated).

## Repository architecture

The client owns mode, source/card revisions, request epochs, cancellation and user-confirmed saving. RealAgentProvider sends bounded mode-specific source/context to a model, parses structured candidates and validates schema, verbatim evidence, style and mode constraints. A two-attempt loop feeds specific validation failures back to the generator. In contested non-listen analysis, a separate fresh semantic review call compares the actual candidate with the user's rejection record; an inconsistent result forces regeneration and ultimately a literal-quote/unknown fallback. Reducer epochs reject stale results; source correction invalidates dependent findings/cards; rejection records suppress old assistant analysis in later context. Speech services handle transcription/synthesis; the model cannot save, browse or execute arbitrary external tools.

## Operational model

The model owns discretionary interpretation, grounded draft findings, note composition and practice-question selection within user-selected tasks. Output is the operational artifact, not a permission to save or contact others. The first-party candidate→validation→repair loop establishes a bounded operational decision/feedback path despite absence of arbitrary tools. Deterministic lifecycle/storage decisions remain with the controller/user. The contested-output reviewer is credited only for the narrow challenge to respect for prior user rejection.

## S1 — Operations

- State: A
- Function: autonomous bounded conversation and evidence-task transformation.
- Disturbance / variety regulated: different user material, missing/conflicting evidence, rejected interpretations and malformed or inappropriate generated candidates.
- Decisive decision or feedback right: choose supported findings, wording, draft structure or a practice question; revise after concrete rejection/validation feedback.
- Decision owner: the configured real-agent model within the first-party generation/repair loop.
- Supporting / enforcement mechanisms: mode prompts, selected source segments, schema/evidence/style validators, two-attempt repair, run IDs and client lifecycle checks.
- Closure path: validation errors re-enter a new generator attempt; accepted content becomes current findings/card/practice state, influencing later turns.
- Boundary reachability: real-agent.generate implements the provider interface used by the deployed server; BreadController submits a current turn and reducer applies only matching epoch/context results.
- Why this is / is not agent-owned: the model determines substantive task content and correction, while the controller enforces validity and human save authority. Fixed UI transitions alone could not produce the same discretionary outcomes.
- Evidence: [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [prompts/agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/prompts/agent.ts); [domain/evidence.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/evidence.ts); [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts).
- Basis: structural.
- Confidence: high.
- Caveats: no general tool-executing autonomy; drafts require user confirmation for persistence. This is not a therapy efficacy or clinical safety claim.

## S2 — Coordination

- State: —
- Function: no distinct operational-unit coordination path.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These are one conversational work cell's pipeline/transport stages and revision-consistency controls. No distinct purposeful operational S1 cells with an inter-S1 disturbance/attenuation relation were found.
- Evidence: [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [services/run-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/run-controller.ts); [services/call-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/call-controller.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [services/run-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/run-controller.ts); [services/call-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/call-controller.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); RealAgentProvider, prompts, evidence/context builder, reducer, BreadController/RunController and optional rejection-review request/fallback..
- Plausible first-party paths checked: generator/reviewer roles, voice capture/playback, cancelling overlapping requests and epoch-based stale-result rejection.
- Why no material first-party path remains: These are one conversational work cell's pipeline/transport stages and revision-consistency controls. No distinct purposeful operational S1 cells with an inter-S1 disturbance/attenuation relation were found.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current organizational control function established.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These regulate individual requests, versions, service capacity and task consent. A session view or stop button is not by itself whole-system resource/commitment regulation with a function-specific parent decision loop.
- Evidence: [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [services/run-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/run-controller.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); [server/limits.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/limits.ts); [server/admission.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/admission.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [services/run-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/run-controller.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); [server/limits.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/limits.ts); [server/admission.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/admission.ts); RealAgentProvider, prompts, evidence/context builder, reducer, BreadController/RunController and optional rejection-review request/fallback..
- Plausible first-party paths checked: mode selection, stop/end/cancel, service admission/rate limits, correction invalidation and user save confirmation; parent supervisory mode considered.
- Why no material first-party path remains: These regulate individual requests, versions, service capacity and task consent. A session view or stop button is not by itself whole-system resource/commitment regulation with a function-specific parent decision loop.

## S3* — Complementary audit

- State: A
- Function: narrow complementary semantic audit of whether contested analysis reintroduces the user's denied interpretation.
- Disturbance / variety regulated: a candidate can pass schema/verbatim/lexical checks yet paraphrase or recommend the rejected interpretation again.
- Decisive decision or feedback right: independently compare actual candidate with user rejection record and judge semantic consistency.
- Decision owner: the model in the fresh rejection-review invocation; runtime parses/enforces its verdict.
- Supporting / enforcement mechanisms: separate review prompt/request, only candidate/rejection/current user data, bounded audit input, conservative verdict parsing and forced retry/fallback.
- Closure path: inconsistent/invalid audit adds REJECTED_INTERPRETATION_REPEATED; generator receives explicit corrective feedback; after a second repeated rejection the product returns quote/unknown fallback rather than display the contested interpretation.
- Boundary reachability: RealAgentProvider invokes the separate reviewer only for non-listen analysis with rejectedFindings after normal validation; reducer REJECT and context-builder persist/send that rejection record.
- Why this is / is not agent-owned: the independent review call supplies semantic judgment beyond the generator's candidate and deterministic lexical check; parsing is enforcement, not the owner. No independent provider identity is claimed.
- Evidence: [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [server/providers/rejection-review.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/rejection-review.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); [domain/context-builder.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/context-builder.ts); [domain/evidence.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/evidence.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: same configured model/provider may serve both roles; independence is fresh context and task separation for this narrow consistency claim, not empirical independence from shared model biases. Ordinary chat is unaudited.
- Claim being audited: the candidate respects the user's previously rejected interpretation and its paraphrases.
- Ordinary reporting path: generator candidate passes schema/evidence/style and exact-normalized rejection checks.
- Complementary access path: fresh semantic comparison of the actual full candidate against persisted user rejection records.
- Independence boundary: separate stateless request with dedicated review instructions and no generator hidden reasoning/history; source of correction is user record, not a generator self-report.
- Who acts on findings: the provider's repair loop withholds the candidate, requests revision and eventually substitutes a traceable non-interpretive fallback.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective capability-adaptation loop.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These adjust current task content, context and service availability. They do not develop future environment/capability options and return an adaptation decision that changes the harness's present repertoire. Research/benchmark plans are adjacent.
- Evidence: [domain/context-builder.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/context-builder.ts); [domain/preferences.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/preferences.ts); [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [docs/product-harness.md](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/docs/product-harness.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [domain/context-builder.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/context-builder.ts); [domain/preferences.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/preferences.ts); [server/providers/real-agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/server/providers/real-agent.ts); [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [docs/product-harness.md](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/docs/product-harness.md); RealAgentProvider, prompts, evidence/context builder, reducer, BreadController/RunController and optional rejection-review request/fallback..
- Plausible first-party paths checked: conversation preference extraction, source revisions, rejected-findings memory, selected practice criteria, service-readiness refresh and real/mock/provider settings.
- Why no material first-party path remains: These adjust current task content, context and service availability. They do not develop future environment/capability options and return an adaptation decision that changes the harness's present repertoire. Research/benchmark plans are adjacent.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy decision/return path.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Static identity/permissions and user authority over task/content/save do not supply ultimate-policy arbitration. No identity-level issue is routed to a legitimate ultimate decision owner and returned as a new governing policy.
- Evidence: [prompts/agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/prompts/agent.ts); [domain/policy.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/policy.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [docs/product-harness.md](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/docs/product-harness.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [prompts/agent.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/prompts/agent.ts); [domain/policy.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/policy.ts); [domain/reducer.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/domain/reducer.ts); [services/bread-controller.ts](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/services/bread-controller.ts); [docs/product-harness.md](https://github.com/ZJUZhiyuCai/bread-companion/blob/058ad153e27bd6470a7e5ef4cab778a93d659a6d/docs/product-harness.md); RealAgentProvider, prompts, evidence/context builder, reducer, BreadController/RunController and optional rejection-review request/fallback..
- Plausible first-party paths checked: AI identity/safety prompt, explicit user modes/preferences, support routing, saving consent, stop/end and operator provider configuration; human parent alternative tested.
- Why no material first-party path remains: Static identity/permissions and user authority over task/content/save do not supply ultimate-policy arbitration. No identity-level issue is routed to a legitimate ultimate decision owner and returned as a new governing policy.

## Distributed OSS parent arrangement

MIT licensing and contributor/maintainer activity establish distribution provenance, not project-level S3/S4/S5 parent closure. This assessment concerns the deployed product boundary; no organization-level parent mode is inferred from local maintainer decisions.

## Self-hosted and non-human modes

Self-hosting selects providers and service limits. The user controls task mode, corrections, stop and saving; these are bounded task/consent rights and do not automatically become S3/S4/S5 parent governance.

## Recursion

Nested execution and delegated tasks do not establish recursive viable systems; no child full metasystem is claimed.

## Variety and escalation

Bounded source selection and schemas attenuate context/payload variety; quotes/version IDs preserve evidence distinctions. Rejection records and fresh semantic review amplify correction visibility. Cancellation/epochs exclude stale returns. Support messages are a product route, not a claimed algedonic governance channel.

## Evidence gaps

Source-first only. No live model, voice, deployment, participant study or clinical evaluation performed. Node/Vitest unavailable in the workspace, so no native test pass is claimed; product state/provider/evidence paths and package scripts were inspected. The S3* positive is limited to the documented fresh-context rejection-consistency audit, with shared-model bias explicitly unresolved.
