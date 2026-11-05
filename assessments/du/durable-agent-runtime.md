---
harness_id: durable-agent-runtime-faleovad
project_name: Durable Agent Runtime
repository: https://github.com/Faleovad/durable-agent-runtime
review_ref: fd75463b6c33f9b32aa1de4c3d8d0b75297bf589
reviewed_at: 2026-11-05
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

# Durable Agent Runtime

## Review boundary

- System in focus: public Apache-2.0 experimental PostgreSQL-backed task/effect runtime at `Faleovad/durable-agent-runtime@fd75463b6c33f9b32aa1de4c3d8d0b75297bf589`, not a hypothetical service supplied with an external reasoning model.
- Purpose and identity: durable task submission, bounded execution, persisted external-effect intent, independent effect observation and safe UNKNOWN reconciliation after lost acknowledgments.
- Relevant environment: authenticated tenant/API requests, a disposable PostgreSQL control database, a separate synthetic provider database, worker crashes, lost acknowledgments, expiry, retries, tool responses and operator-driven incident response.
- Standard-distribution boundary: shipped `dar` CLI, execution and recovery workers, typed public adapter protocols, first-party deterministic model, API, persistence, policy, provider and read-only reconciliation. No external model/provider implementation is bundled as the default operational owner; a separately written `ModelAdapter` and live network providers are extensions, not demonstrated agent loops in the supplied distribution.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md), [`docs/public-api.md`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/public-api.md), [`src/durable_agent_runtime/cli.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/cli.py), [`src/durable_agent_runtime/_internal/runtime.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_internal/runtime.py), [`src/durable_agent_runtime/_core/executor.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/executor.py), [`src/durable_agent_runtime/_core/models.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/models.py), [`src/durable_agent_runtime/_core/recovery_worker.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/recovery_worker.py) and public [`contracts.py`](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/contracts.py).
- Adjacent first-party surfaces excluded from ownership: synthetic provider and fault injection, browser/chaos/verification test suites, artificial team responsibility matrix in `docs/OWNERSHIP.md`, future production/provider integrations, audit/release evidence generated outside ordinary task execution and historical project release decisions. They corroborate implemented safeguards but do not donate a live autonomous agent, independent audit reviewer or staffed parent authority.
- First-party operating / deployment modes considered: native `dar serve/worker/recovery/submit/status`, Compose execution plus separate recovery reader, default deterministic model and synthetic provider, injectable custom model/effect adapter through public Python contracts, manual incident/reconciliation procedures and test-only forced faults.
- Recursion level: one repository-relative, self-hosted runtime and its synthetic task/work units, not a future company/team, externally integrated language-model agent or separately developed product using this library.
- Reviewed revision: `fd75463b6c33f9b32aa1de4c3d8d0b75297bf589`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The runtime persists tenant tasks, claims, model calls, tool intents, effect identities and recovery receipts in PostgreSQL. Execution workers admit only configured tasks, reserve budgets, retrieve bounded context, validate the model-shaped JSON response, persist effect intent/SENT before writing, then await ACK and independently observed completion. Ambiguous effects become UNKNOWN; a separate recovery process holds reader-only provider capability and must corroborate the full persisted identity before recording reconciliation. The implementation deliberately forbids using an expired lease or missing ACK as permission for blind replay. These are substantive transaction-safety and runtime-control mechanisms, not just documentation. [Runtime overview](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md); [executor](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/executor.py); [recovery worker](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/recovery_worker.py).

At the decisive agentic boundary, `Runtime.__init__` uses `model_adapter or DeterministicModel()`. The only shipped default model constructs an evidence-summary string and predetermined `continue` response from retrieved excerpts, or synthetic `review` under a test fault flag; it makes no model/network invocation and does not plan tools. A submitted task already specifies the requested tool. The executor explicitly rejects model responses changing the persisted tool plan (`output.tool_requests != planned`). The public `ModelAdapter` is an intentionally injectable protocol; the HTTP example implements a **provider effect adapter**, not a reasoning/model provider. The repository's explicit release boundary does not claim certified real-provider operation. [Runtime selection](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_internal/runtime.py); [default deterministic model](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/models.py); [fixed tool-plan validation](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/executor.py); [public model adapter contract](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/public-api.md).

## Operational model

An authenticated user submits an objective plus a validated tool plan and data. The service deterministically admits and executes the request; a hard-coded model-shaped responder returns an excerpt-based summary; policy/quotas/gates validate its output. The executor may issue only the already-authorized effect; independent observation resolves uncertainty. Tenant/operator actions can cancel, inspect or invoke bounded reconcile, but no shipped agent interprets feedback and autonomously chooses a new substantive objective, tool or course of action. An independently implemented injected `ModelAdapter` could supply a model-produced answer or `continue/review` choice, but that actor and its actual behavioral closure are not demonstrated by the bundled standard operation. The first-party executor also blocks autonomous redesign of the tool plan.

Counterfactual: remove all externally supplied custom model adapters and actual network providers while retaining the shipping CLI, database, worker, source defaults and synthetic provider. Durable work, deterministic summaries, constraints, receipts and reconciliation remain; a substantive model-owned decision/action/feedback loop does not. The declared standard-distribution boundary therefore fails the autonomous S1 eligibility condition. Terminal classification, once accepted, is `excluded-no-agentic-vsm`; the six negative states describe this bounded recursion and do **not** deny this project's transactional safety engineering.

## S1 — Operations

- State: —
- Function: no established first-party autonomous operational agent loop; task execution is a deterministic orchestration of an operator-provided objective and preselected effect.
- Disturbance / variety regulated: failures, uncertain effect outcomes, bounded text retrieval and synthetic provider conditions are handled by state machine and policy; the open-ended task-level choice of what to attempt is not delegated to a shipped autonomous actor.
- Decisive decision or feedback right: the user/tenant submits the objective and tool/payload; the default `DeterministicModel` emits canned continuation or synthetic fault-forced review, and executor forbids an unplanned tool request.
- Decision owner: submitted contract and deterministic first-party policies for available actions; an external implementer would own any genuinely model-driven choice if a custom `ModelAdapter` were plugged in.
- Supporting / enforcement mechanisms: model-output schema and citation validation, retrieval isolation, budgets, SENT fences, provider effects and independent observation.
- Closure path: user submit → deterministic worker and canned model response → validated preselected effect → persistence/observation or manual review → user/operator feedback; no agent-authored next-operation decision closes inside the shipped model.
- Boundary reachability: no positive autonomous S1 mode demonstrated; the public model protocol accepts future integration but does not itself instantiate an autonomous actor.
- Why this is / is not agent-owned: default model is handwritten transformation of retrieved text, and executor's fixed tool-plan enforcement prevents a purported model output from selecting a new tool.
- Evidence: [CLI and user-provided task](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/cli.py); [runtime default](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_internal/runtime.py); [deterministic model](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/models.py); [tool-plan constraint](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/executor.py).
- Basis: explicit runtime source + structural counterfactual.
- Confidence: high for the shipped default; this finding does not cover unspecified external adapters.
- Caveats: an independently supplied LLM adapter with a bounded `continue/review` choice would require a separately declared assembled boundary; it must not be silently included at this frozen ref.

### Absence scope

- Surfaces inspected: CLI/public client, `ModelAdapter` contract, runtime default, model/output schema, executor, tool plan, retrieval, provider, tests and integration example.
- Plausible first-party paths checked: default model call, custom-adapter injection, task continuation after effects, fault-simulation review and user/provider feedback.
- Why no material first-party path remains: the shipped model is deterministic and no implemented model-driven next-action owner is established; the model slot depends on external code, while effects remain user-planned.

## S2 — Coordination

- State: —
- Function: no qualifying coordination function over multiple autonomous first-party S1 agents is established at this recursion.
- Disturbance / variety regulated: concurrent worker leases, duplicate task keys, provider effect races and shared database capacity are bounded by deterministic locks/queues; these are real infrastructure conflicts, not competing first-party S1 agent decisions.
- Decisive decision or feedback right: database leases, capacity gates, idempotency keys and effect-fence rules allow or deny preconfigured work deterministically.
- Decision owner: runtime scheduler and database-enforced protocol, not an autonomous coordination actor mediating independently deciding agents.
- Supporting / enforcement mechanisms: global leases, bounded worker concurrency, tenant quota/admission, persisted effect identity and per-intent no-replay fence.
- Closure path: duplicate/concurrent request → DB/state admission or exclusion → stable task or UNKNOWN reconciliation; no adjustment of autonomous first-party S1 units' subsequent independent behavior is evidenced.
- Boundary reachability: not applicable to a positive S2 state.
- Why this is / is not agent-owned: structural protection against two worker processes touching the same intent is not a coordination relation between separate autonomous operating agents under the declared boundary.
- Evidence: [runtime worker lease](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_internal/runtime.py); [executor](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/executor.py); [known concurrency limits](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md).
- Basis: bounded structural negative.
- Confidence: high at first-party S1 boundary.
- Caveats: at a wider multi-agent deployment these primitives may become a useful S2 enforcement substrate, requiring a different reviewed system.

### Absence scope

- Surfaces inspected: worker scheduling, global lease protocol, task/admission constraints, provider-effect intent and reconciliation.
- Plausible first-party paths checked: competing execution workers, per-tenant concurrency, multiple tools, duplicate submissions and observer/writer separation.
- Why no material first-party path remains: no distinct agent-owned S1 units and no returned inter-agent behavioral coordination loop exist in the supplied standard operating mode.

## S3 — Inside-and-now control

- State: —
- Function: the code provides current-process controls but no autonomous whole-agent-organization S3 decision loop under the declared recursion.
- Disturbance / variety regulated: tenant quotas, task deadlines, queue saturation, worker availability, cost estimates, incident thresholds and unresolved provider effects.
- Decisive decision or feedback right: configured admissions, hard budget exhaustion, worker lease and manual operator overrides; no first-party discretionary organizational resource/commitment decision over a functioning autonomous S1 population.
- Decision owner: prior operator-supplied limits plus deterministic admission/incident routines; manually invoked incident mitigation belongs to a real operator, not an internally instantiated parent-governance actor.
- Supporting / enforcement mechanisms: policy reservations, budget counters, metrics, SLO alerts, worker capacity and incident records.
- Closure path: configured limit or threshold → task refusal/suspension/manual-review event → operator may inspect and change configuration; no evidenced autonomous whole-system current prioritization/reallocation with return into agent operations.
- Boundary reachability: not applicable to a positive S3 state.
- Why this is / is not agent-owned: quota enforcement can be operationally effective, but it applies preselected constraints and does not choose between organizational commitments; the repository explicitly calls incident ownership roles synthetic.
- Evidence: [budget policy](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/policy.py); [runtime metering](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_internal/runtime.py); [synthetic organization](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/OWNERSHIP.md).
- Basis: structural + explicit synthetic-governance scope.
- Confidence: medium-high.
- Caveats: strong implementable current resource controls are acknowledged; the ownership-negative claim is limited to an autonomous agent organization, not an ordinary service.

### Absence scope

- Surfaces inspected: queue/worker capacity, tenant/step/task budget code, metrics/incident/runbook docs, current API, manual review and synthetic responsibility mapping.
- Plausible first-party paths checked: SLO-driven current control, quota reprioritization, admission override, operator dashboard, parent human decision and incident closure.
- Why no material first-party path remains: these are deterministic service-level enforcement or hypothetical owner instructions, without a live agent S1 organization, S3 discretionary owner and closed organizational current-control return.

## S3* — Complementary audit

- State: —
- Function: independent **effect-outcome observation** exists, but no complementary organizational audit of agent/manager assertions followed by an independent judgment and corrective-return path is established.
- Disturbance / variety regulated: an uncertain external effect's ACK/commit status and possible duplicate execution; not whether an agent's substantive reported work meets a task or organizational claim.
- Decisive decision or feedback right: fenced recovery observer decides from matching persisted effect identity and read-only provider state whether a specific external mutation occurred, according to fixed predicates.
- Decision owner: separate read-only recovery process for effect verification; no auditor judging an S1 operational work claim or reporting substantive deviations into S3 control.
- Supporting / enforcement mechanisms: distinct recovery credentials/image, immutable intent fingerprint, full identity comparison, read-only observation, UNKNOWN and CONFIRMED receipts.
- Closure path: ambiguous provider dispatch → recovery-only observation → matching effect receipt or manual-review fence; this closes transaction uncertainty, not complementary S3* governance of autonomous operations.
- Boundary reachability: not applicable to a positive S3* state.
- Why this is / is not agent-owned: the read path is genuinely separated from the writer and should not be erased; nevertheless it audits effect identity, not the correctness of a distinct agent's organizational decisions; no autonomous S1/S3 claims are available for an organizational audit path.
- Evidence: [reconciliation design](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md); [recovery worker](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/src/durable_agent_runtime/_core/recovery_worker.py); [public observer contract](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/public-api.md); [synthetic personnel caveat](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/OWNERSHIP.md).
- Basis: explicit complementary *transaction* verification, bounded organizational absence.
- Confidence: medium-high; an independent factual observer alone is not sufficient to infer VSM S3*.
- Caveats: read-only non-writer recovery is significant for safety/assurance and could be a component of a stronger assembled S3* process.

### Absence scope

- Surfaces inspected: observer/recovery worker, provider reader/writer separation, incident/audit documents, fault fixtures, manual review API and test evidence.
- Plausible first-party paths checked: separate recovery role, incident audit, provider state lookups, verification manifest, model-output citation checks and synthetic security ownership.
- Why no material first-party path remains: each shipped supplementary check targets protocol integrity or effect finality, while no independently authorized reviewer adjudicates S1/manager operational assertions and routes substantive findings into subsequent organization behavior.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped environmental/future adaptation judgment and feedback loop into the runtime's agent capability is established.
- Disturbance / variety regulated: workload saturation and future failure risks are documented; queue-tail objectives and limitations describe engineering issues rather than an agent-owned outward-looking strategy function.
- Decisive decision or feedback right: future design/release changes are developer decisions outside the runtime; the worker does not propose, choose and apply system-level adaptation in response to sensed external change.
- Decision owner: maintainers or future operators outside the declared runtime boundary.
- Supporting / enforcement mechanisms: metrics, SLO windows, roadmap/known limitations, verification reports and manually configured operational limits.
- Closure path: measurements/reports can inform maintainers, who may revise code or deployments later; no first-party S4 option selection and returned adaptation is shipped.
- Boundary reachability: not applicable to a positive S4 state.
- Why this is / is not agent-owned: telemetry and an engineering roadmap supply information, not a closed environment→future-option→strategy→S3 loop.
- Evidence: [limitations and roadmap](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md); [synthetic escalation roles](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/OWNERSHIP.md).
- Basis: bounded structural negative.
- Confidence: high for shipped runtime.
- Caveats: longitudinal project evolution and benchmarks are not credited as a live runtime's S4 merely for sharing a Git repository.

### Absence scope

- Surfaces inspected: metrics/SLO/incidents, roadmap, release/verification reports, worker/runtime configuration and operator ownership design.
- Plausible first-party paths checked: threshold-triggered adaptation, capacity planning, model/provider re-routing, roadmap implementation and parent-governed change decisions.
- Why no material first-party path remains: observed telemetry and maintainer plans do not implement autonomous or operationally closed parent-owned future-environment adaptation with return into the agent organization.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational purpose/identity issue adjudication and authoritative return loop operates within the shipped agent runtime.
- Disturbance / variety regulated: tool budgets, privileges, idempotency/finality and security constraints are important safety boundaries, but not conflicts about organizational identity or ultimate purpose.
- Decisive decision or feedback right: hard-coded validation and trusted administrator configuration define permission edges; an independent final-purpose policy decision is not made by a staffed human hierarchy or first-party agent.
- Decision owner: developer/administrator outside the runtime for foundational constraints; deterministic authorization code enforces them.
- Supporting / enforcement mechanisms: role-specific credentials, tenant tokens, no-replay fences, bounded model-output schemas and release-policy evidence.
- Closure path: operator config/release defines rules → API/worker rejects unsupported actions → incident/manual review; no extraordinary identity issue reaches legitimate ultimate authority and returns as a new binding collective policy decision.
- Boundary reachability: not applicable to a positive S5 state.
- Why this is / is not agent-owned: safe default authority and a fictional future organization chart are not a living identity-level governance process; even legitimate human administration of a database is not automatically S5.
- Evidence: [public contract](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/public-api.md); [synthetic role disclaimer](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/docs/OWNERSHIP.md); [runtime permission boundary](https://github.com/Faleovad/durable-agent-runtime/blob/fd75463b6c33f9b32aa1de4c3d8d0b75297bf589/README.md).
- Basis: explicit authority/protocol scope + bounded organizational negative.
- Confidence: medium-high.
- Caveats: real independent operators of a future deployed service may own ultimate policy at a different recursion; this is not proven for the pinned synthetic lab.

### Absence scope

- Surfaces inspected: public contracts, credentials/configuration, security/provisioning, immutable effect policy, release governance and synthetic ownership/incident runbooks.
- Plausible first-party paths checked: trusted admin decisions, security owner escalation, manual-review override, release-disposition audit and parent-controlled identity/purpose change.
- Why no material first-party path remains: every shipped policy mechanism constrains preselected tasks or lab release practice; no in-boundary ultimate-purpose issue, legitimate decision owner and returned governance closure can be reconstructed.

## Recursion

This review is of the runnable first-party synthetic execution service. Multiple worker processes and read-only recovery roles belong to the same transactional runtime; they are not independently deliberating VSM S1 agents. A production system composing an external model-backed planner, multiple autonomous agents, real provider and accountable human governance would be a distinct system-in-focus requiring new evidence and possibly a different vector. The similarly named but distinct `murilo-bassan/durable-agent-runtime` repository is not this assessment's source identity.

## Variety and escalation

The system reduces failure variety by admitting only schema-valid requests, reserving scarce capacity before model calls and effects, fencing ambiguity, physically separating recovery read rights from execution writes, and refusing replay without identity-matched observation. Budget exhaustion and manual review are honest terminal or operator-dependent states. These safeguards may be directly relevant to AI assurance even though the core agentic S1 threshold is not met at this immutable source revision.

## Evidence gaps

- Source and documentation were inspected at pinned Git revision. `python -m compileall -q src/durable_agent_runtime` passed locally. Full upstream `pytest` was not run: `python -m pytest -q` failed immediately because `pytest` is not installed, and PostgreSQL provisioning/real-provider E2E was not configured. No test-suite or production readiness claim is made.
- The public injection protocol could accept a third-party model-written adapter; its actual deployed reasoning/feedback behavior and independent authority are not supplied at the reviewed standard boundary. A different assembled deployment may warrant reassessment with its own frozen evidence.
- The repository's synthetic ownership map disclaims actual staff and independent operation. Release verification and independent transaction outcome checking are not credited as an organizational S3* or S5 owner.
- `excluded-no-agentic-vsm` is a corpus/boundary classification, not a claim that durability, at-most-once controls, provenance, recovery design or tests are unimportant.
