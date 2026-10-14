---
harness_id: ekuelkpodar-agent-control-plane
project_name: Agent Control Plane
repository: https://github.com/ekuelkpodar/agent-control-plane
review_ref: 895283b28a2a7a69d5c7078002e5613720e1c97f
reviewed_at: 2026-10-14
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

# Agent Control Plane

**Proposed canonical disposition:** `excluded-no-agentic-vsm`. Frozen source-first review for [batch #1537](https://github.com/opensiro/vsm-harness-index/issues/1537) row 2; canonical admission requires a separate PR and CI.

## Review boundary

- System in focus: executable modular-monolith `src/acp` control-plane API, planner, router, workflow, policy, audit, registry, tenant and approval mechanisms at exact source SHA 895283b28a2a7a69d5c7078002e5613720e1c97f.
- Purpose and identity: independently govern registrations, authorities, scheduling, routing, cost, tool calls and audit of heterogeneous agent runtimes without itself executing the autonomous agent cognitive task loop.
- Relevant environment: API caller, tenant policy authors, Postgres/Redis, optional OPA, registered external agent runtimes, mock tool functions/model, human approver and external AGRL goal ledger.
- Standard-distribution boundary: the shipped Python service and local demo with mock model/runtime, built-in deterministic planning/routing, authorized tools and governance. Real external model agents, hypothetical adapter implementations, planned LLM planner, future multi-agent runtime and AGRL are outside.
- Credited operating / distribution surfaces: README.md, ARCHITECTURE.md, pyproject.toml, src/acp/{api,orchestrator,planner,router,workflow,models,agents,governance,cost,learning,evaluation,core}, test/demo reference paths and local deployment.
- Adjacent first-party surfaces excluded from ownership: repository research/roadmap, example mock external tool demonstrations as proof of real semantic agent autonomy, contributor/CI tests and unrelated AGRL; code interfaces that deliberately raise NotImplementedError for future integrations.
- First-party operating / deployment modes considered: local API and container, deterministic planner and mock model provider, registered mock-tool workflows, tenant policy and approvals, agent lifecycle, evaluations/audit and proposed learning changes.
- Recursion level: one ACP tenant-scoped control-plane instance orchestrating external registered agent workloads; the semantically autonomous agent-runtime recursion is not shipped inside ACP itself.
- Reviewed revision: 895283b28a2a7a69d5c7078002e5613720e1c97f.
- Observation date: 2026-10-14.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The API exposes task creation and execution, approvals, agent/tool registration and audit. `orchestrator/service.py` implements a **real** governed execution pipeline, with state, risk, cost, approvals, delegation, per-tool authorization and workflow outcomes. `planner/__init__.py` turns goals into tool steps using deterministic regex/name matching; `LLMPlanner.plan` raises NotImplementedError. `models/__init__.py` defaults to `MockModelProvider.generate`, which returns deterministic hash-based text; OpenAI/Anthropic providers raise NotImplementedError. `workflow/__init__.py` sequentially runs fixed planned steps with idempotency/retry. `router/__init__.py` ranks registered agents by fixed weighted factors. The separate agent runtime is explicitly outside ACP in normative [architecture](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md). The `src/acp/learning` proposal service cannot autonomously apply capability changes, and audit verifies integrity rather than independently directing recovery.

The shipped mock tool case should not be mistaken for evidence of real model-operated, context-revising S1. The first-party system can execute tools under governance and preserve durable state; there is no supported runtime path for its own non-mock open-ended agent.

Primary sources: [README.md](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/README.md); [ARCHITECTURE.md](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md); [src/acp/orchestrator/service.py](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/orchestrator/service.py); [src/acp/planner/__init__.py](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/planner/__init__.py); [src/acp/models/__init__.py](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/models/__init__.py); [src/acp/workflow/__init__.py](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/workflow/__init__.py); [src/acp/core/config.py](https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/core/config.py).

## Operational model

External caller declares task goal, policy and tenant → deterministic planner chooses steps → router ranks registered agents → policy/risk may deny or request human approval → step runner invokes governed local tool functions or deterministic model mock → audit and state are updated. A real model-backed autonomous agent runtime is either an external actor or an unimplemented provider integration. Counterfactual owner test: remove real registered/external semantic agents but leave the service and mock provider. Most management, routing, approvals, workflow and demo operations still function deterministically, but no autonomous agent remains to interpret new observations and select/revise meaningful actions. No positive first-party autonomous S1 admission is evidenced.

## S1 — Operations

- State: —
- Function: No first-party non-mock autonomous semantic task operator is supplied by this ACP control plane.
- Disturbance / variety regulated: Open-ended task interpretation, action choice and adaptation to observations at agent-runtime level.
- Decisive decision or feedback right: Choose task-semantic model/tool actions from observations, reconsider tool results, and terminate on goal completion.
- Decision owner: Actual agent runtime/provider is an external service or adapter; the shipped ACP default is a deterministic `MockModelProvider`.
- Supporting / enforcement mechanisms: DeterministicPlanner/RuleBasedPlanner, registry, weighted router, PostgresDurableRunner, policy/risk/approval, local-function tool execution.
- Closure path: User creates task → static plan matches tool names or emits one mock `reason` step → router selects registry entry → fixed runner invokes tools or mock hash-based text → task status. No autonomous first-party model decision/observation/replan loop.
- Boundary reachability: Shipped Python `src/acp` API and CLI worker are reachable. The real model-backed agent-runner cited in architecture is deliberately outside, and OpenAI/Anthropic classes raise NotImplementedError.
- Why this is / is not agent-owned: An executable workflow is not automatically autonomous S1: its selectable actions are planned by deterministic string rules, and the sole executable model response is a stable mock hash.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/README.md; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/planner/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/models/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/orchestrator/service.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/workflow/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/core/config.py.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: API execute pipeline, planner, registered agents/tools, model provider implementations, mock demo, workflow and router, architecture boundary.
- Plausible first-party paths checked: LLMPlanner constructor, OpenAI/AnthropicProvider adapters, execution pipeline, reference local functions, model `reason` step and deployment defaults.
- Why no material first-party path remains: The only built-in provider implementing generate is deliberately mock, the LLM planner is NotImplemented, real model adapters are stubs, and the normative architecture explicitly separates agent execution from ACP decisions.

## S2 — Coordination

- State: —
- Function: No independent S2 regulation of concrete interference among distinct first-party autonomous S1 operational units is established.
- Disturbance / variety regulated: Scheduling contention, agent selection and tenant/workflow separation, but not witnessed rivalry between first-party autonomous S1 units.
- Decisive decision or feedback right: Detect inter-S1 collision/oscillation and return an attenuating coordination decision to change later S1 operation.
- Decision owner: No qualifying first-party autonomous S1 units are shipped; registered agents denote external runtimes or mock executions.
- Supporting / enforcement mechanisms: WeightedRouter, task state and step idempotency, leases, policy gates, tenant boundaries.
- Closure path: Task → single selected registered agent → sequential prepared steps. No S2 control loop responding to interference between distinct first-party operational agents.
- Boundary reachability: No first-party S2 reachability is claimed; generic routing and shared status are shipped but insufficient.
- Why this is / is not agent-owned: The router is a scoring selector based on capability/cost/risk, not evidence of actual inter-S1 conflict/attenuation/feedback.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/router/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/orchestrator/service.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/workflow/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/README.md; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: Router, workflow, task lifecycle, registry, coordination and future multi-agent roadmap.
- Plausible first-party paths checked: Multi-agent fleet inventory, scheduling/routing, retries, workflow step ordering, shared task state and conflict candidates.
- Why no material first-party path remains: Source shows ranked selection plus single-run step control; multi-agent S2 regulation belongs to future roadmap or external operational agents, not a shipped interference-specific relation.

## S3 — Inside-and-now control

- State: —
- Function: Strong current governance exists, but current-control discretion is explicitly external to a first-party autonomous VSM and no full parent S3 closure at that recursion is evidenced.
- Disturbance / variety regulated: Active budgets, task risk, tool permissions, approval states, cost and task status.
- Decisive decision or feedback right: Make discretionary whole-system present commitments and interventions across S1 operations based on a current view.
- Decision owner: Human API principals and tenant-policy authors own substantive task/constraints/approval; deterministic ACP enforcement honors configuration and records status.
- Supporting / enforcement mechanisms: Task API, policy engine, approval gate, risk score, budget hard deny, weighted scoring, dashboard and control APIs.
- Closure path: User supplies goal/policy → ACP evaluates fixed rules → routes/blocks/pauses; human approves exact plan if needed → executor resumes. There is no agent-owned whole-system decision over actual first-party S1 units.
- Boundary reachability: First-party check/approval return is reachable; autonomous S3 organizational discretion and comprehensive parent S3 at an actual autonomous first-party S1 recursion are not.
- Why this is / is not agent-owned: Risk/budget/approval gating executes existing policy; it does not itself supply a VSM S3 owner capable of choosing substantive current system-wide commitments from autonomous operating feedback.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/orchestrator/service.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/governance/policy.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/governance/approvals.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/core/config.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/api/routers/tasks.py.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: Task statuses, tenant policy, approvals, monitoring, lifecycle, current router, budget.
- Plausible first-party paths checked: Manager/dashboard current view, intervention APIs, human approval, risk/budget controls, delegated credentials and pause/resume.
- Why no material first-party path remains: All relevant in-boundary decisions reduce to fixed policy or per-task human commands; a complete discretionary whole-system S3 owner over first-party agentic S1 is not supplied.

## S3* — Complementary audit

- State: —
- Function: Signed audit trails and deterministic evaluation exist, but not an independent operational reality audit judgment with corrective managerial return.
- Disturbance / variety regulated: Potential incorrect task success, policy misapplication or model/tool self-report versus actual execution.
- Decisive decision or feedback right: Use a complementary independently owned access path, challenge a normal claim and return a corrective finding into current operation.
- Decision owner: AuditLedger signs/records events; metric calculators derive counts. No separately operating first-party auditor decides and returns corrective action.
- Supporting / enforcement mechanisms: Hash-chained Ed25519 entries, `verify_chain`, event records, evaluation metrics, API audit queries, human review.
- Closure path: Workflow writes event/audit rows → audit reader and metric function may inspect → operator decides whether to correct. Chain integrity alone cannot audit semantic task truth or independently steer system action.
- Boundary reachability: Audit ledger and evaluation are real shipped components, not an autonomous audit owner.
- Why this is / is not agent-owned: Cryptographic independence from agent writes is useful complementary evidence; it is not evidence of independent semantic judgment or management closure.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/governance/audit.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/evaluation/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/orchestrator/service.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: medium-high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: Audit writer/verify, evaluations, task events, approval and incident escalation, tests and docs.
- Plausible first-party paths checked: Signed chain verification, policy violation counters, task-success metrics, hidden model auditor, anomaly-to-intervention return.
- Why no material first-party path remains: Inspected implementations write/check event integrity and evaluate deterministic metrics; no independent audit actor makes a substantive judgment returned into autonomous system current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective external adaptation decision path altering current organizational capability is operationally closed.
- Disturbance / variety regulated: Future provider performance changes, risk factors, new tools/capabilities and agent versions.
- Decisive decision or feedback right: Sense external/future shifts, generate adaptation options, decide and return selected capability change.
- Decision owner: Humans submit agent/version/learning proposals; governance enforces human approval. Real model adaptive planning is future work.
- Supporting / enforcement mechanisms: Metric registry, LearningService propose-only, lifecycle versioning, policy and promotion gates, static router scores.
- Closure path: Human-proposed learning change → policy evaluation → inert record → explicit human approval to mark applied. No first-party generation of future strategy or application of a capability modification from observed external change.
- Boundary reachability: Records and approval hooks are shipped; no positive autonomous/parent S4 closure is evidenced.
- Why this is / is not agent-owned: `LearningService.apply_proposal` only changes proposal status to applied; it does not autonomously synthesize or deploy a capability change. Roadmap Phase 6 is prospective.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/learning/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/evaluation/__init__.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/agents/registry.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/README.md; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: Propose-only learning service, evaluation metrics, agent promotion/versioning and roadmap.
- Plausible first-party paths checked: Feedback from evaluations, model performance, policy updates, learning proposals, deploy/promote/rollback.
- Why no material first-party path remains: Future-facing options/decision and return into new effective capability depend on external humans or unimplemented systems; existing code records/evaluates but does not close that S4 function.

## S5 — Policy and identity

- State: —
- Function: No first-party autonomous ultimate-policy/organizational identity authority closes S5 at the autonomous agent boundary.
- Disturbance / variety regulated: Legitimate agent authority, tenants, credential delegation, risky tool access and organizational goals.
- Decisive decision or feedback right: Resolve the ultimate identity and controlling purpose of the operating organization and return authoritative policy into later action.
- Decision owner: External tenant/platform policy author, API caller and human approvers; ACP policy engine is a deterministic enforcer.
- Supporting / enforcement mechanisms: Tenant policy bundles, platform guardrails, delegation and identity records, approvals, signed audit and policy deny defaults.
- Closure path: Human/configured policy → engine evaluates context → denial/approval requirement → governed executor applies decision. ACP deliberately cannot mutate its own ultimate goal and guardrails.
- Boundary reachability: First-party policy enforcement is reachable but the legitimate parent S5 **decision** and higher-recursion return path are not independently evidenced for a first-party autonomous organization.
- Why this is / is not agent-owned: Policies, permissions and approvals do not automatically establish system-owned S5 or `P`; without qualifying first-party agentic S1 the classification is bounded absence.
- Evidence: https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/ARCHITECTURE.md; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/governance/policy.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/governance/approvals.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/core/config.py; https://github.com/ekuelkpodar/agent-control-plane/blob/895283b28a2a7a69d5c7078002e5613720e1c97f/src/acp/learning/__init__.py.
- Basis: direct frozen-source documentation and implementation; bounded negative adjudication.
- Confidence: high.
- Caveats: material governance and enforcement functionality is acknowledged; it does not automatically constitute first-party autonomous VSM-function ownership.

### Absence scope

- Surfaces inspected: Platform/tenant authority and guardrails, lifecycle/delegation and governance APIs, external AGRL goals.
- Plausible first-party paths checked: Identity issuer, platform veto, tenant bundles, delegated authority, human approval, protected goal layer.
- Why no material first-party path remains: Identity policy inputs remain supplied by outside principals; there is no autonomous identity-policy judgment and operational closure at a qualifying first-party agentic VSM recursion.

## Distributed OSS parent arrangement

Different tenants, local deployments and registered agent workers may carry their own external principal and review loops. These are not a first-party unified ACP-owned autonomous organization or parent-mode S3/S4/S5 closure at the declared recursion.

## Self-hosted and non-human modes

Self-hosted API/worker and mock provider are real, but the local model is deterministic and external provider adapters do not run. Combining a new real agent/provider would alter the inspected operating boundary and needs a separate exact-ref assessment.

## Recursion

The assessment focuses on one ACP control-plane installation. Agents in its registry are objects and possibly external runtimes; lifecycle states/tenants/workflow steps do not themselves establish an autonomous VSM recursion.

## Variety and escalation

Policy, risk, budget, credential and human approval paths constrain operational variety and can fail closed. Escalation to a human for tool permission or policy decisions is not automatically a separate S3*, S4 or S5 agent-owned loop.

## Evidence gaps

- Static frozen-source analysis; this execution did not run Postgres, Docker, integration tests or a real model.
- No executable non-mock semantic model provider or LLMPlanner exists in the reviewed distribution. Future pluggable adapters and roadmap work are excluded from credited ownership.
- Some reference tool functions are executable, but a fixed plan/runner acting on them does not prove autonomous semantic operation.
- Real agent deployments assembled by users may create a different system-in-focus; no S3/S3*/S4/S5 rights borrowed from them.

## Publication

`status: proposed` is not canonical. Review phase and canonical Index admission/exclusion must remain separate; no catalog, signature or rank may be changed by this proposal.
