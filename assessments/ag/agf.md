---
harness_id: agf
project_name: AGF
repository: https://github.com/dcnl1980/agf
review_ref: 56088db39b66954e8d81e138c16d1e098d6470b6
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AGF

## Review boundary

- System in focus: first-party community AGF deterministic compliance kernel, policy/ruleset/approval control-plane API, catalog service and operator UI; not the external LangGraph/Temporal agent or business process receiving AGF decisions.
- Purpose and identity: return auditable, signed policy PASS/BLOCK (and mapped ALLOW/BLOCK/REQUIRE_APPROVAL) for externally supplied entity/tool data; let authorized policy authors publish rulesets and approvers resolve gates.
- Relevant environment: application/agent clients, finance/compliance data, tenant operators, pre-existing rule bundles, optional enterprise extension modules, kernel and control-plane deployments.
- Standard-distribution boundary: Rust `agf-sp1` ARSL compile/evaluate/sign/audit endpoints, Express `control-plane` authenticated APIs/SQLite state and HITL webhooks, catalog service, website UI, first-party thin LangGraph/Temporal pre-tool gate adapters. External agent model/tool loops and private enterprise modules are excluded.
- Credited operating / distribution surfaces: `README.md`, `docs/{KERNEL_EVALUATION_CONTRACT,API_CONTRACTS,DELIVERY_STATUS,INTEGRATION_QUICKSTART_LANGCHAIN_LANGGRAPH}.md`, `agf-sp1/server/src/{api,signing,audit}.rs`, `control-plane/src/{index,db,auth}.js`, `integrations/{langgraph,temporal}`, `catalog-api/server.mjs`.
- Adjacent first-party surfaces excluded from ownership: synthetic proof generation, benchmarks, conformance scripts, demo entities, CI/releases, investor/whitepaper claims, development UI, unimplemented hardware TEE and private enterprise extensions not in this tree.
- First-party operating / deployment modes considered: local community Docker stack; kernel `/evaluate` and `/evaluate-entity`; customer-scoped control-plane published bundles; registered agent metadata, approval queues/webhooks; LangGraph/Temporal gate adapters; optional external policy-author/approver UI; private enterprise extension points only as boundary notes.
- Recursion level: AGF evaluation/governance product at one customer scope, not the independent external agent/service or the customer's whole enterprise.
- Reviewed revision: `dcnl1980/agf@56088db39b66954e8d81e138c16d1e098d6470b6`; frozen intake #2473/controller #2474 row 5, original #188 row 10.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/README.md) describes AGF as a **deterministic governance and compliance stack for agentic systems**, composed of Rust evaluation kernel, control plane and operator website. The explicit [kernel contract](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/KERNEL_EVALUATION_CONTRACT.md) says “evaluation-only,” no workflow-queue orchestration, and no outbound calls during evaluation. [Rust handler](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/agf-sp1/server/src/api.rs) loads caller-chosen ARSL rules, compiles and evaluates them deterministically against supplied entity data, appends a chained audit record, stamps mock/attestation info and signs the PASS/BLOCK result. No model planning, tool selection or request-answer reasoning is present.

The [Express control plane](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1019-L1126) can **register** agent IDs/names, update statuses, list agents and enforce roles. [Evaluate API](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1520-L1626) checks customer/agent registration, finds the published policy bundle, posts an evaluation request to the Rust kernel, stores decision/evidence and optionally creates a human approval item and webhook. The registered “payments-orchestrator” seed in [DB](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/db.js) is **metadata**; this repo does not instantiate/run that autonomous agent. User-authored ruleset lifecycle, HITL and website actions belong to governance, not first-party semantic task ownership.

The [LangGraph adapter](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/integrations/langgraph/agf_langgraph_adapter.ts) is a **thin pre-tool gate**: it posts to AGF `/evaluate`, maps PASS/BLOCK, optionally returns `REQUIRE_APPROVAL` from a caller-provided predicate and returns signed evidence. The [integration quickstart](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/INTEGRATION_QUICKSTART_LANGCHAIN_LANGGRAPH.md) explicitly says to add this guard before the *external* graph tool node and continue the existing tool execution path only if allowed. Temporal is a similar external-host adapter. Nothing here composes an AGF-owned reasoning→tool→observation loop. [Delivery registry](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/DELIVERY_STATUS.md) reports local stack and API features; hardware TEE remains incomplete and is not credited as operational independent auditor capability.

Counterfactual owner test: remove the LangGraph/Temporal application and any other agent using AGF while leaving kernel, policy catalog, ruleset versions, registered agent names, control-plane APIs, approvals, signing/audit and UI intact. AGF still evaluates provided policy inputs and governs hypothetical future actions, but it cannot autonomously choose substantive business actions, interpret their observations or decide next task steps. It is a governance **enforcement service**, not a first-party AI agent harness. The correct terminal Index outcome is **`excluded-no-agentic-vsm`**.

## Operational model

An operator creates/publishes rules, an external agent/service submits proposed action/entity data, AGF deterministically evaluates those inputs, signs/records its verdict, optionally queues human approval and returns the gate result. The external caller decides what substantive work to attempt and interprets result/feedback; the operator owns policy and high-risk approvals. No first-party model-driven operational execution or autonomous metasystem decision loop appears in the supported community stack. No live external agent, financial transaction or hardware attestation execution was performed.

## S1 — Operations

- State: —
- Function: autonomous operations would choose substantive financial/business tool acts from goals and observations.
- Disturbance / variety regulated: variable business tasks and external action outcomes; AGF regulates policy compliance of a supplied action/entity.
- Decisive decision or feedback right: interpret the objective, choose tool/action, observe execution and select next semantic operation.
- Decision owner: external LangGraph/Temporal/customer agent; AGF's kernel owns deterministic pass/block **enforcement** of another actor's proposed action.
- Supporting / enforcement mechanisms: ARSL compiler/evaluator, signed audit, control-plane bundle pin, approval queue, webhook, agent metadata registry and thin pre-tool adapters.
- Closure path: external agent proposes input → adapter/control-plane → kernel policy verdict → adapter returns allow/block/approval → external agent resumes or changes its operation. AGF does not choose the original or next substantive action.
- Why this is / is not agent-owned: no first-party model prompt/agent loop exists in the kernel, control-plane agent registry or adapters. “Agentic” in the product name refers to the **governed clients**.
- Evidence: [kernel contract](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/KERNEL_EVALUATION_CONTRACT.md); [Rust evaluation](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/agf-sp1/server/src/api.rs); [LangGraph guard](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/integrations/langgraph/agf_langgraph_adapter.ts).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: source may be integrated with real autonomous client systems, whose internal decision loop is separately owned.

### Absence scope

- Surfaces inspected: README, kernel contract/handlers, control-plane evaluate/agent CRUD, registered-agent database, LangGraph/Temporal adapter, UI, published rule workflow and catalog.
- Plausible first-party paths checked: “payments-orchestrator” registered agent metadata, control-plane evaluation endpoint, webhook approvals, adapter pre-tool guard and kernel rule compilation.
- Why no material first-party path remains: every supported path accepts externally chosen work/policy/data and returns a deterministic gate, rather than creating a model-owned operating task/tool loop.

## S2 — Coordination

- State: —
- Function: attenuate concrete interference/oscillation between distinct operational S1 units with feedback changing their subsequent behaviour.
- Disturbance / variety regulated: multiple registered agent identities and shared customer data could produce conflicts, but AGF's observed checks are customer isolation and per-input compliance.
- Decisive decision or feedback right: negotiate or regulate an actual cross-S1 operational conflict and inform both agents' later decisions.
- Decision owner: no AGF-owned independent S1 units or S2 conflict decider; callers and external orchestration framework govern peer interaction.
- Supporting / enforcement mechanisms: registered agent IDs/statuses, customer scoping, role-based access, policy bundles, audit links and optional integration middleware.
- Closure path: independent candidate action → per-customer policy decision → single caller response; no detected peer interference → coordination adjustment → feedback into multiple operating units.
- Why this is / is not agent-owned: registry cardinality and identical policy for multiple agents do not supply inter-agent S2 regulation.
- Evidence: [agent registry routes](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1019-L1126); [control-plane evaluate](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1520-L1626); [integration quickstart](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/INTEGRATION_QUICKSTART_LANGCHAIN_LANGGRAPH.md).
- Basis: structural negative.
- Confidence: high.
- Caveats: policy checks may constrain a *larger* multi-agent organization but do not own its coordination.

### Absence scope

- Surfaces inspected: agent CRUD/registration, evaluation requests, approvals, customer scoping, LangGraph and Temporal adapters.
- Plausible first-party paths checked: common policy across agents, status changes, approval webhooks and external graph guard.
- Why no material first-party path remains: no first-party operating peers, specific inter-S1 conflict detector/attenuator or returned coordination adjustment; the shipped interfaces remain per-request governance.

## S3 — Inside-and-now control

- State: —
- Function: make discretionary whole-system current decisions over shared resources/commitments, priorities and operational intervention.
- Disturbance / variety regulated: financial/compliance risk, active vs inactive agent registration, approval backlog and policy violations.
- Decisive decision or feedback right: inspect whole operating portfolio and revise current priorities/resources/interventions for the agent organization.
- Decision owner: human customer administrators/policy authors and approvers define constraints; deterministic kernel evaluates each request; no AGF agent makes whole-system allocation decisions.
- Supporting / enforcement mechanisms: dashboard/summary, agent status registry, role guards, bundle versions, approval queue and signed per-action verdicts.
- Closure path: human publishes rules → kernel enforces against external action → approval/decision appears to operator/external caller. No AGF-owned whole-system current S3 decisor with binding feedback to subsequent autonomous operation.
- Why this is / is not agent-owned: policy rule enforcement, dashboard counts and an inactive-agent flag do not by themselves decide operational resource/commitment tradeoffs; HITL concerns individual high-risk inputs.
- Evidence: [control-plane evaluate and approval](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1520-L1641); [agent list/status](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1019-L1126); [kernel contract separation](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/KERNEL_EVALUATION_CONTRACT.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: customers may use the control plane as support for human current control at a larger recursion; that is not a complete eligible AGF-owned parent S3 closure here.

### Absence scope

- Surfaces inspected: control-plane agent CRUD/evaluation/approvals, dashboard, kernel contract and execution, operator role APIs.
- Plausible first-party paths checked: inactive-agent gate, rule bundle version change, approval resolution, metrics and dashboard overview.
- Why no material first-party path remains: each path enforces operator-selected rights or reports current state; none closes discretionary whole-system management at assessed AGF-agent recursion.

## S3* — Complementary audit

- State: —
- Function: independently inspect operational reality beyond normal reports and return corrective findings to current control.
- Disturbance / variety regulated: tampered evidence, false compliance claims, unverifiable policy results and missing transaction provenance.
- Decisive decision or feedback right: an independent auditor judges external operating evidence and returns a corrective intervention, separate from routine evaluation.
- Decision owner: Rust kernel evaluates its own input and signs the result; offline signature verifier and human auditor can check that same evidence. No separate autonomous/constructor independent corrective audit owner is shipped.
- Supporting / enforcement mechanisms: Ed25519 signatures, BLAKE3 proof/chain hashes, audit log, public key endpoint, `agf_verify` CLI and optional TEE attestation stub.
- Closure path: same request's kernel verdict → audit/signature → verifier or external auditor integrity check. This authenticates the *ordinary* decision trail; it does not provide independent access to the actual business process and feedback that changes AGF whole-system control.
- Why this is / is not agent-owned: provenance and cryptographic verification can be excellent but cannot alone judge whether an external agent achieved the intended real-world operation; the TEE path is explicitly mock/unfinished.
- Evidence: [Rust evaluator sign/audit](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/agf-sp1/server/src/api.rs); [kernel contract](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/KERNEL_EVALUATION_CONTRACT.md); [delivery gaps](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/DELIVERY_STATUS.md).
- Basis: structural negative.
- Confidence: high.
- Caveats: signed evidence may be consumed by an external independent auditor; it is not itself AGF-owned S3* judgment.

### Absence scope

- Surfaces inspected: audit/signing code, verifier, kernel handler, attestation stub, control-plane evidence and proof documentation.
- Plausible first-party paths checked: proof signature verification, chain integrity, audit log, non-mock TEE, external verifier.
- Why no material first-party path remains: these validate the kernel's own outputs or are incomplete hardware proof; no independently governed complementary reality test and corrective return to S3 exists.

## S4 — Outside-and-then intelligence

- State: —
- Function: sense future-relevant environmental changes, develop alternatives and adapt current agent capabilities or system strategy.
- Disturbance / variety regulated: changing rules/regulations, business ecosystems, marketplace offers, future compliance risk.
- Decisive decision or feedback right: select prospective strategy/ruleset/capability changes from external future evidence and feed the choice into present agent operation.
- Decision owner: human policy authors/marketplace operators publish bundle versions; deterministic kernel consumes the current package. AGF does not autonomously choose regulatory options or alter the agent's objectives.
- Supporting / enforcement mechanisms: community ruleset marketplace/catalog, lifecycle draft/validate/publish APIs, operator UI, version pins and digest check, documentation/whitepaper.
- Closure path: human-authored rule update → published bundle → later deterministic evaluation; no first-party environmental foresight → alternatives → agent-owned adaptive change loop.
- Why this is / is not agent-owned: maintaining a policy catalog and publishing new versions is governance infrastructure, not outside-and-then autonomous strategic intelligence.
- Evidence: [ruleset lifecycle specification](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/RULESET_LIFECYCLE_SPEC.md); [control-plane API](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js#L1297-L1520); [marketplace catalog](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/catalog/README.md).
- Basis: structural negative.
- Confidence: high.
- Caveats: legitimate regulators and enterprise policy teams operate outside the assessed product boundary and can adapt business rules there.

### Absence scope

- Surfaces inspected: ruleset lifecycle, marketplace, versioning, control-plane publication, evidence schema, operator UI and kernel contract.
- Plausible first-party paths checked: catalog updates, published policy bundles, future regulatory pages and ruleset changes.
- Why no material first-party path remains: changes are authored/approved externally and no prospective environment model or decision owner adapts AGF/agent capability automatically or through an eligible parent loop.

## S5 — Policy and identity

- State: —
- Function: legitimate ultimate-policy/identity adjudication for an autonomous AGF-owned agent organization.
- Disturbance / variety regulated: authorized rule ownership, policy disputes, role boundaries and conflicting high-risk decisions.
- Decisive decision or feedback right: settle ultimate identity or policy tension and return that judgment into subsequent viable agent operation.
- Decision owner: human customer admin/policy_author/approver and external institutions; AGF enforces published rules and routes action approvals, rather than deciding what ultimate principles should govern the organization.
- Supporting / enforcement mechanisms: RBAC, published bundle digest/signatures, approval IDs/webhooks, policy author and approver UI, kernel PASS/BLOCK decision mapping.
- Closure path: external author policy/version → AGF publish → evaluation and human case-by-case approval → external client acts or stops. No first-party identity-level arbitration is evidenced; action approval does not automatically become S5.
- Why this is / is not agent-owned: the product is built to **enforce** governance chosen by people, not autonomously determine ultimate organizational identity. The agent registry is not a self-governing organization.
- Evidence: [control-plane lifecycle and RBAC](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/control-plane/src/index.js); [kernel contract responsibilities](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/docs/KERNEL_EVALUATION_CONTRACT.md); [README scope](https://github.com/dcnl1980/agf/blob/56088db39b66954e8d81e138c16d1e098d6470b6/README.md).
- Basis: explicit + structural negative.
- Confidence: high.
- Caveats: a customer may have authentic parent S5 policy governance beyond the AGF integration, but this assessment does not borrow its identity decisions.

### Absence scope

- Surfaces inspected: auth roles, rule-version publication, evaluate/approve endpoints, extension hooks, kernel and product-governance docs.
- Plausible first-party paths checked: admin policy authoring, rule audit, approval result webhook, agent activation/deactivation.
- Why no material first-party path remains: these enforce externally chosen rules/permissions or record operator state; no independent first-party identity/ultimate-policy settlement and closed feedback is shipped.

## Distributed OSS parent arrangement

The community/enterprise split, contributors, operator admins and private extension points are not an operationally closed first-party parent VSM for the evaluated community product. Human-authored rules and payment approvals remain real authority, but they cannot supply absent AGF agent autonomy through source co-location.

## Recursion

The kernel serves a customer-scoped evaluation endpoint; the control plane can register many external agents and many ruleset versions. Neither a registered agent row nor nested rule evaluation establishes internally viable S1 units or metasystem recursion. A larger customer agent organization could use AGF as infrastructure, outside this record's first-party recursion.

## Variety and escalation

AGF reduces compliance variety to deterministic results, cryptographically identifies the evaluation trail and escalates selected high-risk actions to a human approval queue/webhook. These gates are operationally valuable, but their PASS/BLOCK/status signals do not prove autonomous governance, whole-system S3/S4/S5 decision rights or an independent algedonic channel with returned regulatory closure.

## Evidence gaps

No live enterprise plugin, actual LangGraph agent run, external financial action or hardware TEE was inspected/executed. The documented hardware attestation remains a stub in the community kernel. The negative states are bounded to the pinned public standard-distribution control plane/kernel and do not assess autonomy of customers' connected agents or the unavailable private enterprise implementation.
