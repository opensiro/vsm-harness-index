---
harness_id: alexi5000-clawkeeper
project_name: ClawKeeper
repository: https://github.com/Alexi5000/ClawKeeper
review_ref: 7b3ccd64550ac69a99a59603a11ffd6753bb81e0
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ClawKeeper

## Review boundary

- System in focus: the shipped Bun/Hono ClawKeeper finance-agent service, first-party model-backed CEO/orchestration paths, named domain leads and generic workers, plus its policy/approval boundary; not an external OpenClaw platform or real bank/accounting organization.
- Purpose and identity: interpret SMB finance commands, decompose/route bounded finance tasks and return results subject to tenant/capability/risk policy.
- Relevant environment: authenticated tenant/user instructions, financial inputs and uploaded invoices, configured DeepSeek-compatible model endpoint, optional data connectors, PostgreSQL, human approvers and API/dashboard clients.
- Standard-distribution boundary: `src/index.ts` initializes agents and API; `src/api/routes/agents.ts` exposes direct task and orchestrate/plan/execute/SSE routes; `src/core/llm-client.ts` supplies first-party model prompts and parsing; `src/agents/{clawkeeper,orchestration_service,base,worker_base,index}.ts` and domain leads form operational paths; `src/openclaw/{policy,runtime}.ts` gates them.
- Credited operating / distribution surfaces: live Hono orchestrate endpoints, model-backed `decompose_financial_task` and `complete` calls, `ClawKeeperAgent.execute`, `OrchestrationService.create_plan`/`execute_plan`, agent registry, accounts-payable/reporting/CFO leads, tenant/capability/approval policy.
- Adjacent first-party surfaces excluded from ownership: `agents/**/AGENT.md` role descriptions without executable model loop, synthetic proof/v2 artifacts and FDE benchmark, CI, test fixtures, developer scripts, website/marketing, dashboard presentations and independent external OpenClaw provider internals.
- First-party operating / deployment modes considered: server API explicit agent execution; model-backed plan creation followed by explicit execution; `/orchestrate` with optional `auto_execute`; streaming execution; CEO direct and complex requests; worker/lead delegation; dry-run policy; configured or absent model credentials.
- Recursion level: one tenant-scoped finance request and its internal model-proposed subtask execution, not 110 autonomous viable organizations merely because 110 profiles or descriptions exist.
- Reviewed revision: `Alexi5000/ClawKeeper@7b3ccd64550ac69a99a59603a11ffd6753bb81e0`; frozen intake #2473/controller #2474 row 3, historical #188 row 8.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/README.md) presents a 1+9+100 finance-agent hierarchy and deterministic money-movement gates. The **active source boundary is narrower than the roster**. [Entrypoint](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/index.ts) initializes the CEO and AP lead and serves Hono. The [agent API](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/api/routes/agents.ts) genuinely wires `/orchestrate/plan`, `/orchestrate/execute/:plan_id`, `/orchestrate` with optional `auto_execute`, and SSE to the [orchestration service](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestration_service.ts). That service calls first-party [LLM-client](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/core/llm-client.ts) `decompose_financial_task` with a concrete prompt, builds a dependency DAG, assigns capabilities, executes same-depth tasks in parallel through `agent_runtime.get_agent`, and streams status/results. It is not merely a framework API for future developers.

The [CEO agent](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/clawkeeper.ts) also uses model-backed decomposition for recognized complex phrases, but its local workflow implementation explicitly runs subtasks sequentially and does not materialize the declared DAG edges; simpler requests use deterministic capability routing, with an LLM-backed `execute_directly` fallback. Do **not** infer 110 independently model-reasoning workers: [registry](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/index.ts) lazily instantiates 10 agent classes and generic worker instances, while [WorkerAgent](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/worker_base.ts) largely emits a capability-labelled completion stub. Some leads implement real specialized logic. Prominent source labels and role files are not proof of separate independent operations.

Before any agent-specific `execute`, [BaseAgent](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/base.ts#L142-L229) calls first-party [deterministic OpenClaw policy](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/policy.ts): tenant match, granted capability, user role, prompt-pattern/PII checks, risk amount and explicit approval ID. Missing approval returns `requires_approval`, and disallowed tasks fail before execution; redacted audit and traces follow. The [OpenClaw runtime adapter](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/runtime.ts) adds another policy gate but simply delegates to the passed local runnable agent. These controls are **constructor-owned enforcement**, not an autonomous metasystem deciding ultimate policy or independently reviewing operations.

The source offers a real but **bounded** model-generated operational plan: model decomposition happens once at plan creation; `execute_plan` follows static dependency order, checks failed prerequisites and stores outcomes, but no feedback-driven model replanning or cross-agent conflict mediation was found. Proof bundles are synthetic/offline; no live payment, banking integration or provider-backed E2E execution was conducted here.

## Operational model

An authenticated tenant sends a finance command. The first-party LLM prompt turns it into action-capability tasks. ClawKeeper assigns its own lead agents, and its runtime executes permissible portions behind deterministic policy and user approval. Successful and failed subtasks return results to the API/stream; planning and execution can be separate client calls or combined by `auto_execute`. The model has discretion over task decomposition and direct finance responses, but not authority to bypass a missing payment approval or rewrite governance. The multi-agent hierarchy supplies work decomposition; remaining metasystem functions require independent function/owner/closure evidence.

## S1 — Operations

- State: A
- Function: locally select and perform bounded finance-request operations through first-party model-generated task decomposition, finance-domain capabilities, and returned results.
- Disturbance / variety regulated: natural-language finance requirements, changing task/capability mix, invoice and reporting inputs, model outputs, provider failures and subtask success/failure.
- Decisive decision or feedback right: interpret the tenant's command into substantive tasks/capabilities/dependencies and produce direct finance guidance or executed domain outputs.
- Decision owner: model-backed ClawKeeper `decompose_financial_task` and `ClawKeeperAgent.execute_directly`, with first-party prompts, parser, mapped tool/lead dispatch and results; the model provider supplies inference but does not choose ClawKeeper's operating contract.
- Supporting / enforcement mechanisms: API/tenant authorization, `BaseAgent` policy checks, deterministic capability-matching, worker registry, DAG ordering, retry/backoff and Opik/audit records.
- Closure path: authenticated command → `create_plan`/CEO → model-generated task decomposition → capability assignment → `execute_plan`/local leads or direct LLM reply → outcomes/error/result back to API caller. Follow-on requests can incorporate returned information; no continuous autonomous replanning is claimed.
- Boundary reachability: `/api/agents/orchestrate` and `/orchestrate/plan`/`execute` routes import and invoke the first-party orchestration service in the shipped server; `src/index.ts` starts the agent runtime; no external agent binary is required for the decision loop.
- Why this is / is not agent-owned: the deployed first-party semantic decomposition/response is model-owned, while task timing, DAG control, policy and payments are deterministic or human-owned. `A` does not imply unrestricted money movement or a self-governing 110-agent organization.
- Evidence: [API routes](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/api/routes/agents.ts#L242-L436); [orchestration service](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestration_service.ts#L73-L284); [LLM prompt](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/core/llm-client.ts#L263-L340); [CEO](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/clawkeeper.ts#L40-L97).
- Basis: structural (direct reachable call graph) + explicit.
- Confidence: high for model-backed S1; medium for completeness of specialized finance outputs.
- Caveats: many advertised workers are generic stubs; model planning is one-shot and real external financial writes are human/tenant-gated.

## S2 — Coordination

- State: —
- Function: attenuate concrete interference or oscillation among distinct operational S1 units, with feedback changing their subsequent behaviour.
- Disturbance / variety regulated: task dependency failure and parallel task scheduling; these are not themselves evidenced as conflict between independently autonomous S1s.
- Decisive decision or feedback right: settle competing agent actions on shared finance data or conflicting objectives and return a coordinated revision to each affected S1.
- Decision owner: none evidenced for a first-party S2 relation. The service computes a topological ordering and skips failed-dependency tasks; policy gates independently evaluate each task.
- Supporting / enforcement mechanisms: capability routing, dependency edges, parallel same-depth execution, agent registry, retry and tenant isolation.
- Closure path: model plan → static dependency graph → ready tasks parallelized → result/failure events; no first-party observed interference → peer-coordination decision → revised peer behaviour loop.
- Why this is / is not agent-owned: multiple agent labels, role files, a DAG and parallel execution prove workflow structure, not conflict attenuation between viable operational peers.
- Evidence: [orchestration graph and executor](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestration_service.ts#L83-L285); [CEO sequential execution](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/clawkeeper.ts#L73-L110); [worker stub](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/worker_base.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: conflicts could arise in real multi-user finance deployment, but shipped S2-specific regulation is not demonstrated by the reviewed paths.

### Absence scope

- Surfaces inspected: task DAG planning/execution, topological sort/parallel dispatch, `ClawKeeperAgent`, agent registry, base policy, worker and lead implementation, OpenClaw runtime adapter.
- Plausible first-party paths checked: dependency ordering, failed-prerequisite skipping, tenant/capability policy, repeated CEO delegation and retries.
- Why no material first-party path remains: these regulate dependencies and individual action eligibility, not a specific cross-S1 interference with adaptive feedback to multiple operating units.

## S3 — Inside-and-now control

- State: —
- Function: whole-tenant/current-system oversight of shared agent operations, commitments and resources with authority for revised interventions.
- Disturbance / variety regulated: concurrent finance subtasks, task failures, high-risk actions, model cost and tenant boundaries.
- Decisive decision or feedback right: weigh current portfolio/whole-system results against common priorities and autonomously change allocations, constraints or commitments.
- Decision owner: tenant/operator supplies authorizations and policies; deterministic orchestration and policy decide permitted state transitions under preselected rules; no model-owned whole-system S3 discretion.
- Supporting / enforcement mechanisms: API status/counts, plan statuses, per-task audit, policy risk tiers, amount approval IDs, role and tenant checks.
- Closure path: policy/plan → individual task execution status → result stream/dashboard; operator may respond with new work or approval but no whole-system current S3 decision-return mode is evidenced.
- Why this is / is not agent-owned: the CEO title and plan aggregation do not make the model a whole-system manager; one-shot decomposition and static executor do not autonomously intervene over shared commitments on feedback.
- Evidence: [agent dashboard/status routes](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/api/routes/agents.ts#L18-L48); [execution result updates](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestration_service.ts#L150-L305); [policy engine](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/policy.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: high-risk human approval is important governance, but it is a single-action gate, not automatically S3 parent governance.

### Absence scope

- Surfaces inspected: CEO, orchestrate plan/execute APIs, plan aggregation, status dashboard and policy/approval runtime.
- Plausible first-party paths checked: CEO plan selection, stream statuses, dependency failure handling, risk/amount approvals and task reruns.
- Why no material first-party path remains: no dynamic whole-system current-control decision owner/return loop; operator provides scoped permission and the code enforces static plan choices.

## S3* — Complementary audit

- State: —
- Function: obtain sufficiently independent complementary access to operating reality, audit ordinary reports and return corrective findings to current control.
- Disturbance / variety regulated: fabricated finance outputs, invalid model tasks, policy bypass attempts and hidden execution failures.
- Decisive decision or feedback right: separately judge original transaction/artifact reality against the operational agent's account and demand correction.
- Decision owner: routine policy/validation checks and external human approval; no independent audit agent or separate audit judgment with returned S3 authority is wired.
- Supporting / enforcement mechanisms: BaseAgent audit rows, redaction, Opik traces, finance policy scanner, FDE synthetic proof, approval metadata and test suite.
- Closure path: action input → pre-execution deterministic checks → allow/deny/approval; after task, status/audit rows log the same operational path. Benchmark proof is out-of-band test infrastructure, not a deployed independent audit loop.
- Why this is / is not agent-owned: policy validation and append-only logs are evidence integrity and routine enforcement, not automatically complementary independent inspection of actual financial reality.
- Evidence: [BaseAgent audit and policy](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/base.ts#L142-L229); [policy rules](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/policy.ts); [offline proof boundary](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/docs/proof/v2.0/README.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: an external auditor may consume immutable logs, but independent authority and correction are not shipped as this agent's S3*.

### Absence scope

- Surfaces inspected: first-party policy engine, task audit/Opik hooks, OpenClaw adapter, compliance lead, synthetic proof/tests and reporting routes.
- Plausible first-party paths checked: compliance checks, policy violations, independent stored audit events, proof bundles and approval escalation.
- Why no material first-party path remains: available checks are routine/preconfigured, telemetry is produced by the operational path, and proof/test artifacts are adjacent; no distinct independent audit judgment and returned corrective authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: sense future-relevant external environment, develop capability/strategy alternatives and return adaptive decisions to present operation.
- Disturbance / variety regulated: evolving market/financial trends, integration changes, unfamiliar finance workflows and changing model capabilities.
- Decisive decision or feedback right: adjust the agent organization's future capability or strategy from prospective external distinctions.
- Decision owner: API user/operator and static project implementation. The model can analyze requested financial forecasts, but those are tenant task outputs, not an adaptation loop governing the harness.
- Supporting / enforcement mechanisms: CFO lead financial analysis, model `deepseek-reasoner` report-analysis prompt, generic memory files, static domain roles, integrations and manual deployment/configuration.
- Closure path: user asks for forecast → domain lead/model returns analysis as S1 result; no source-grounded external foresight → selected capability redesign → subsequent agent runtime changed.
- Why this is / is not agent-owned: forecasting the customer's finance data and composing a plan for the current request is not S4 organizational adaptation of ClawKeeper itself.
- Evidence: [LLM report analysis](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/core/llm-client.ts#L235-L261); [CFO lead](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestrators/cfo.ts); [agent task service](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/agents/orchestration_service.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: external developments may matter to finance clients, but no active CK-level strategic learning/change owner was found.

### Absence scope

- Surfaces inspected: CFO/reporting leads, LLM prompts, runtime plan creation/execution, memory files, model/provider configuration, integration and deployment docs.
- Plausible first-party paths checked: financial forecasting, model task decomposition, static worker catalog and config evolution.
- Why no material first-party path remains: no prospective external-to-capability adaptation feedback; those paths serve current task answers or operator changes.

## S5 — Policy and identity

- State: —
- Function: legitimate settlement of identity/ultimate-policy differences, including S3–S4 tension, with binding return into the agent organization.
- Disturbance / variety regulated: tenant isolation, authorization, payment risk, approval semantics and potentially conflicting finance strategies.
- Decisive decision or feedback right: choose ultimate acceptable identity/mission policy and bind the result to future operation.
- Decision owner: project developers define policy constants and tenant/role capability tables; user/human approver supplies action-level approval metadata. The model is not empowered to rewrite it.
- Supporting / enforcement mechanisms: `get_capability_policy`, `evaluate_agent_policy`, tenant role checks, `requires_approval`, audit trails and API authentication.
- Closure path: configured capability/amount policy → deterministic allow/deny/approval response → per-task execution gate. No identity-level dispute and legitimate independent decision/return system is shown.
- Why this is / is not agent-owned: strict, useful financial control is enforcement of previously set policy; an approval ID for a payment does not establish autonomous or parent S5.
- Evidence: [policy implementation](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/policy.ts); [manifest capability rules](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/manifest.ts); [OpenClaw adapter](https://github.com/Alexi5000/ClawKeeper/blob/7b3ccd64550ac69a99a59603a11ffd6753bb81e0/src/openclaw/runtime.ts).
- Basis: explicit + structural negative.
- Confidence: high for absence of model authority; medium-high for boundary-complete absence.
- Caveats: a tenant institution could have real identity governance *outside* the shipped agent service, not credited here.

### Absence scope

- Surfaces inspected: manifest, deterministic policy, base agent enforcement, tenant/user auth, approval routes, CEO/lead capabilities, project steering docs.
- Plausible first-party paths checked: policy role/amount configuration → execution; action approval metadata → resumed task; CEO decision overriding risk.
- Why no material first-party path remains: the shipped system has no first-party identity/ultimate-policy deliberation and return loop; the model cannot override preconfigured constraints and action approval is lower-level.

## Distributed OSS parent arrangement

The repository's maintainers can alter manifest/policy code and provider configuration and tenant users can approve scoped actions. Neither contributor updates nor ordinary financial approvals are evidence of a first-party multi-mode parent S3/S4/S5 organization at this run recursion. No `(P)` state is credited from repository co-location.

## Recursion

One CEO plus nine named leads and 100 described workers form a deployment/role hierarchy, not evidence of recursively viable S1s. Most generic worker executions are fixed capability completion messages and many orchestrators are deterministic. The substantive model-owned S1 is the current finance request and model-generated task plan, not a self-governing fleet at every role.

## Variety and escalation

ClawKeeper attenuates semantic task variety by prompted decomposition and capability routing; deterministic policy attenuates dangerous actions, tenant crossovers, prompt-pattern risks and high-value payments. Failed dependencies are skipped; errors are streamed/logged; risky actions require external approval metadata. These are useful exception channels, but without a whole-system authority/return witness they are not automatically independent algedonic regulation or S2/S3/S5.

## Evidence gaps

Provider-backed model inference, real financial integrations, DB-backed audit integrity and E2E payment/approval behaviour were not run here; the source code and supported entry points were reviewed at the frozen SHA. Model-generated DAG shape can be imperfect and execution is primarily deterministic after planning. No claim is made that 110 individually autonomous agents exist or that financial safety is guaranteed. Future genuine inter-agent coordination or learning would require its own new source-first review.
