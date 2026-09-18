---
harness_id: parlant
project_name: Parlant
repository: https://github.com/emcie-co/parlant
review_ref: ea737442b8ae65854a842542e544fbe7e6144bad
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
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Parlant

## Review boundary

- System in focus: the Parlant conversational-agent runtime and its first-party context matching, guidelines, journeys, tool calling, composition and observability at the pinned revision.
- Purpose and identity: control customer-facing AI interactions so only contextually relevant instructions, knowledge, tools and workflow state shape each response.
- Relevant environment: end-user conversation, developer-authored behavioral rules/SOPs, external tools/APIs/retrievers and configured model providers.
- Standard-distribution boundary: Parlant engine/runtime and SDK abstractions; developer-authored application policy and external models/services are environment/inputs unless Parlant itself closes an organizational function.
- First-party operating / deployment modes considered: guideline matching, observations, exclusions/dependencies, journeys, tools, fluid/canned response composition and tracing.
- Recursion level: one Parlant conversational agent/runtime. Guideline elements are not treated as independent S1 units.
- Reviewed revision: `ea737442b8ae65854a842542e544fbe7e6144bad`.
- Observation date: 2026-09-18.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.4`.

## Repository architecture

Parlant is an interaction-control harness. Developers declare observations, guidelines, relationships, journeys, knowledge and tools. At each turn the engine matches relevant context, resolves journey state, invokes contextually associated tools/workflows and composes either model-generated or canned output. Explainability/tracing records guideline matches and decisions.

## Operational model

The primary operation is the customer-facing agent turn: interpret conversational state under first-party contextual-control rules, use tools as needed and produce the response/action. Guideline relationships and journey transitions regulate that same operation. They do not create multiple independent S1 units, and tracing is evidence/observability rather than an independent auditor.

## Primary evidence

- [`README.md`](https://github.com/emcie-co/parlant/blob/ea737442b8ae65854a842542e544fbe7e6144bad/README.md) — interaction-control boundary, context matching, guidelines, relationships, journeys, tools and explainability.
- First-party source under [`src/parlant`](https://github.com/emcie-co/parlant/tree/ea737442b8ae65854a842542e544fbe7e6144bad/src/parlant) — runtime implementation corresponding to the documented engine.
- First-party docs at [`docs`](https://github.com/emcie-co/parlant/tree/ea737442b8ae65854a842542e544fbe7e6144bad/docs) — customization and runtime concepts.

## S1 — Operations

- State: A
- Function: autonomously conduct a controlled customer-facing interaction turn, including context-sensitive reasoning/tool use and response selection.
- Disturbance / variety regulated: non-linear user language, changing conversational context, competing relevant rules, workflow state, external tool results and response uncertainty.
- Decisive decision or feedback right: choose the concrete response/tool action within the context and constraints assembled by the Parlant engine.
- Decision owner: the configured model-driven Parlant agent for fluid operation; strict canned mode constrains the available output without removing the standard autonomous mode.
- Supporting / enforcement mechanisms: contextual matching engine, observations, guidelines, relationships, journeys, tools/retrievers, glossary/variables and composition modes.
- Closure path: user input is matched to relevant state/rules/tools, the agent/tool path executes, and the resulting response/event updates the conversation for the next turn.
- Why this is / is not agent-owned: the model-driven agent owns the substantive interaction choice in the standard fluid path; deterministic context engineering constrains rather than replaces that operational decision.
- Evidence: README engine diagrams and examples; first-party runtime/docs.
- Basis: explicit + structural
- Confidence: high
- Caveats: individual deployments can intentionally use strict/canned paths for some turns, but the standard distribution establishes an autonomous operational path.

## S2 — Coordination

- State: —
- Function: no inter-S1 coordination function is established at the declared single-agent runtime boundary.
- Disturbance / variety regulated: conflicting guidelines and journey branches are regulated inside one operational agent, not between distinct S1 units.
- Decisive decision or feedback right: no material first-party right was found that attenuates interaction among multiple distinct Parlant S1 work units.
- Decision owner: none established for qualifying S2.
- Supporting / enforcement mechanisms: guideline exclusions/dependencies, contextual matching and journey transitions.
- Closure path: those mechanisms alter one agent's context/response path; no inter-unit coordination loop is established.
- Why this is / is not agent-owned: the missing requirement is multiple distinct S1 units and their interference, not model autonomy.
- Evidence: README relationships/journeys/context-engineering documentation and runtime structure.
- Basis: structural
- Confidence: high
- Caveats: applications may compose several Parlant agents externally; that separate application boundary is not established by this repository's standard single-agent engine.

### Absence scope

- Surfaces inspected: engine diagram, observations, guidelines/relationships, journeys, tools/retrievers, composition and SDK/runtime structure.
- Plausible first-party paths checked: exclusion/dependency resolution, workflow branching, tool orchestration and multi-turn journeys.
- Why no material first-party path remains: all inspected paths coordinate context/instructions within one conversational operation; no distinct S1 units plus inter-unit disturbance and returned coordination relation are established.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established above the conversational S1 operation.
- Disturbance / variety regulated: current rule relevance, journey state and tool availability are regulated, but as part of producing the current interaction.
- Decisive decision or feedback right: no separate owner was found with whole-system authority over resources, commitments, priorities or current organizational constraints.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: contextual matching, guideline relations, journeys, canned-response constraints and tool gating.
- Closure path: no distinct S3 control loop separate from S1 was found.
- Why this is / is not agent-owned: “conversational governance” and behavioral control are product semantics; they do not by themselves establish VSM S3 at this boundary.
- Evidence: README design goals, diagrams and runtime concepts.
- Basis: structural
- Confidence: high
- Caveats: application operators author rules, but rule authorship/enforcement is not automatically S3 ownership.

### Absence scope

- Surfaces inspected: matching engine, guideline/journey state, tools, response composition, server/runtime and configuration surfaces.
- Plausible first-party paths checked: behavioral-control rules, strict output mode, journey state resolution, tool gating and developer configuration.
- Why no material first-party path remains: no separate whole-system current view and discretionary current-control authority distinct from the primary conversational operation is established.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established.
- Disturbance / variety regulated: response explainability and unwanted-behavior prevention were inspected, but these do not create an independent audit judgment loop.
- Decisive decision or feedback right: no separate reviewer/auditor decision right with corrective feedback into control was found.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: OpenTelemetry tracing, guideline match logs, constraints and pre-approved/canned responses.
- Closure path: observability records ordinary runtime decisions; no independent audit finding is returned to force correction.
- Why this is / is not agent-owned: logging/explainability and deterministic guardrails are evidence/enforcement, not a complementary independent auditor.
- Evidence: README explainability and design-goal sections.
- Basis: explicit + structural
- Confidence: high
- Caveats: developers can inspect traces externally, but that human development workflow is outside the standard autonomous runtime boundary.

### Absence scope

- Surfaces inspected: explainability/tracing, constraints, canned responses, guideline matching and runtime generation path.
- Plausible first-party paths checked: trace review, unwanted-behavior prevention, strict composition and tool/guideline validation.
- Why no material first-party path remains: none supplies a distinct sufficiently independent evidence path plus audit judgment and returned corrective action into current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external/future intelligence and adaptation loop is established in the standard runtime.
- Disturbance / variety regulated: product/user feedback may motivate developer changes, but that workflow is outside the assessed runtime.
- Decisive decision or feedback right: no material first-party owner was found that senses external/future distinctions, generates adaptation options and returns a chosen change into present capability/S3.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: external retrievers/tools can fetch current information for S1 tasks; developers can revise guidelines from feedback.
- Closure path: no first-party outside-and-then adaptation closure is established.
- Why this is / is not agent-owned: external information use during a customer task and developer maintenance are not S4 by themselves.
- Evidence: README tools/retrievers and design goal describing product-feedback-to-implementation workflow.
- Basis: explicit + structural
- Confidence: high
- Caveats: a larger application could build an S4 loop around Parlant.

### Absence scope

- Surfaces inspected: retrievers/tools, customization APIs, feedback-oriented design goals, docs and runtime architecture.
- Plausible first-party paths checked: external retrieval, product feedback, guideline updates and journey maintenance.
- Why no material first-party path remains: these paths either serve the current conversation or depend on external developer action; no runtime external/future distinction → option generation → capability return loop is closed.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy governance loop is established at the Parlant runtime boundary.
- Disturbance / variety regulated: developer-authored brand/policy rules constrain behavior but do not constitute an S5 authority process.
- Decisive decision or feedback right: no material first-party identity/ultimate-policy dispute resolution right with authoritative return was found.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: guidelines, agent description, journeys, canned responses and developer configuration.
- Closure path: authored constraints feed directly into operational context; no identity-level authority loop is established.
- Why this is / is not agent-owned: policy-like content or “on-brand” behavior is not VSM S5 merely because it shapes outputs.
- Evidence: README design goals and customization examples.
- Basis: structural
- Confidence: high
- Caveats: a parent organization can own brand/ultimate policy outside the harness; generic developer authorship is insufficient for canonical `P`.

### Absence scope

- Surfaces inspected: agent creation/configuration, guidelines, journeys, canned responses, brand/compliance framing and server runtime.
- Plausible first-party paths checked: developer-authored policies, strict output templates, guideline relationships and agent descriptions.
- Why no material first-party path remains: no identity-level matter is routed to a legitimate ultimate authority with an authoritative decision returned into subsequent operation as an S5 closure.

## Recursion

Parlant can be embedded in larger systems, but the reviewed repository evidence is mapped at one conversational-agent runtime. Its rules, observations and journey states are internal control elements, not recursive viable organizations.

## Variety and escalation

Parlant attenuates conversational variety by selecting only contextually relevant guidelines/tools/knowledge and by enforcing relationships and strict output options where configured. Escalation patterns are application-specific and do not establish higher VSM functions at this boundary.

## Evidence gaps

No material first-party S2-S5 path remained after inspection of the documented runtime/control surfaces. The strongest rejected shortcut is guideline conflict resolution: it is intra-S1 contextual control, not inter-S1 S2.
