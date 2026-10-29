---
harness_id: openstinger
project_name: OpenStinger
repository: https://github.com/srikanthbellary/openstinger
review_ref: 73ea429d4eec4e900cb364e6ffc1982ef3f75b47
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenStinger

## Review boundary

- System in focus: first-party OpenStinger memory, vault, and response-alignment MCP services at the frozen commit; not a separately deployed OpenClaw, Qwen-Agent, Claude Code or other connected agent.
- Purpose and identity: retain and retrieve external-agent session memory, maintain derived notes, answer explicit memory requests and optionally evaluate/correct externally produced responses.
- Relevant environment: external model agents and their objectives, operators setting profiles/thresholds, session files, embedding/inference providers and persistence services.
- Standard-distribution boundary: Python `openstinger` package with Tier 1 MCP memory, Tier 2 StingerVault, Tier 3 Gradient, CLI, ingestion scheduler, FalkorDB and PostgreSQL integration.
- Credited operating / distribution surfaces: `mcp/server.py`, `mcp/tools/memory_tools.py`, `temporal/engine.py`, `ingestion/scheduler.py`, `scaffold/vault_engine.py`, `gradient/interceptor.py`, `gradient/correction_engine.py`, and Gradient MCP routing.
- Adjacent first-party surfaces excluded from ownership: integrations for other agent frameworks, template skill files, tests, benchmarks, deployment scripts and external agents instructed to call OpenStinger tools.
- First-party modes considered: standalone Tier 1 memory server, Tier 2 scheduled note classification/sync, Tier 3 observe-only or enabled alignment checks/correction, optional model-based memory reflection and external multi-namespace ingestion.
- Recursion level: one support substrate that several externally operated agents may consume; namespaces and source sessions are not first-party goal-executing organizations.
- Reviewed revision: `73ea429d4eec4e900cb364e6ffc1982ef3f75b47`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The package advertises a portable MCP agent memory server, not an agent runtime. MCP clients select a memory call; the server retrieves, records or classifies episodic records in its graph and audit stores. The per-namespace scheduler reads existing external session files and processes them with a fixed ingestion pipeline. LLM entity/fact extraction and StingerVault identity-note classification are bounded data transformations. The explicit `memory_reflect` path performs retrieval followed by one answer-generation call and optional abstention; the model does not choose the subsequent tool or decide a task-level intervention. Gradient evaluates a caller-produced answer, may make one LLM rewrite and re-evaluate it, while defaulting to observe-only. This is an externally invoked response filter, not a first-party autonomous task loop.

Pinned source evidence:

- [README: product boundary, tiers, external integrations and architecture](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/README.md)
- [Tier 1 MCP server: published tool schemas and dispatcher](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/mcp/server.py)
- [Memory tools: request-driven retrieval and `memory_reflect`](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/mcp/tools/memory_tools.py)
- [Temporal engine: model-backed structured extraction](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/temporal/engine.py)
- [Ingestion scheduler: per-namespace session batch processing](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/ingestion/scheduler.py)
- [StingerVault: scheduled note classification and evolution](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/scaffold/vault_engine.py)
- [Gradient: response evaluation, defaults and verdict routing](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/gradient/interceptor.py)
- [Correction engine: one rewrite and one re-evaluation](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/gradient/correction_engine.py)
- [Spawn contract: configuration validation only](https://github.com/srikanthbellary/openstinger/blob/73ea429d4eec4e900cb364e6ffc1982ef3f75b47/src/openstinger/agents/spawn.py)

## Operational model

An external runtime owns a user goal and invokes OpenStinger's MCP tools, or leaves its pre-existing session records available for background ingestion. OpenStinger transforms records and returns memory, scores, classifications, rewritten text, or alerts. It does not select the external runtime's next action. When Tier 3 is enabled, a response can be corrected or blocked, but the goal-directed task actor remains the connected agent and the policy originates in its administrator.

## S1 — Operations

- State: —
- Function: bounded memory storage, retrieval, note processing, and response rewriting do not form a first-party model-driven operational agent that closes a goal/action/observation loop.
- Disturbance / variety regulated: rapidly changing session records, memory retrieval ambiguity, conflicting facts and candidate responses submitted by external agents.
- Decisive decision or feedback right: decide what task action to take next from tool observations and whether a user's objective is satisfied.
- Decision owner: external MCP agent/user supplies the goal and selects next tools; OpenStinger's service chooses predesigned retrieval/extraction steps.
- Supporting / enforcement mechanisms: hybrid search, model extraction prompts, `memory_reflect`, per-namespace ingestion, StingerVault note revisions, Gradient correction.
- Closure path: external request or session event → service pipeline/LLM transform → return data/verdict to external agent; no first-party goal-revision and freely selected next-task-action loop.
- Why this is / is not agent-owned: model output may be a fact, summary, answer, classification, or corrected response but is not a self-selected intervention in an ongoing task.
- Evidence: MCP tools, memory reflection, temporal engine, vault engine, Gradient and README (pinned links above).
- Basis: source-first decision-right tracing and negative first-party runtime inspection.
- Confidence: high.
- Caveats: an OpenStinger-backed *external* agent may be fully autonomous; that actor must be assessed at its own boundary.

### Absence scope

- Surfaces inspected: published MCP tools, retrieval/ingestion/classification paths, model provider wrappers, Tier 3 evaluation and documented integrations.
- Plausible first-party paths checked: `memory_reflect` retrieval-augmented answer, LLM entity extraction, scheduled vault note evolution, correction engine's re-evaluation, `agents/spawn.py` and named agent namespaces.
- Why no material first-party path remains: these execute fixed service workflows, validate configuration or transform user-supplied content without autonomous goal-directed tool selection and subsequent task feedback.

## S2 — Coordination

- State: —
- Function: namespace separation and per-namespace ingest concurrency provide data isolation and worker scheduling, not corrective coordination between first-party S1 goal-executing units.
- Disturbance / variety regulated: concurrent batch ingestion, graph identity collisions, retrieval conflicts and cross-client data boundaries.
- Decisive decision or feedback right: detect conflict between operational S1 units and return coordination that changes their subsequent operations.
- Decision owner: server's configured scheduler/isolation code, not an S2 owner over OpenStinger-operated S1 units.
- Supporting / enforcement mechanisms: `IngestionSchedulerRegistry`, agent namespaces, graph deduplication, conflict resolution, bounded batch concurrency.
- Closure path: namespace input → isolated queued record processing → stored result; no first-party cross-S1 disturbance assessment and corrective return.
- Why this is / is not agent-owned: registered clients are external agents; technical isolation and concurrency alone do not evidence inter-S1 VSM coordination.
- Evidence: `ingestion/scheduler.py`, `temporal/engine.py`, `agents/spawn.py` and README.
- Basis: concrete scheduler and owner-boundary inspection.
- Confidence: high.
- Caveats: integration with multiple autonomous clients may support their external S2, but ownership is not transferred to this service.

### Absence scope

- Surfaces inspected: namespace registry, ingestion scheduler, graph conflict/deduplication, spawn validation and MCP dispatch.
- Plausible first-party paths checked: parallel ingest scheduling, agent namespace isolation and temporal conflict resolution.
- Why no material first-party path remains: no independently goal-directed first-party S1 units are coordinated through a returned inter-unit operational intervention.

## S3 — Inside-and-now control

- State: —
- Function: health/status, job logs and Gradient thresholds control service requests, not a whole-system portfolio of first-party S1 commitments.
- Disturbance / variety regulated: failed storage/ingestion jobs, dropped retrieval quality, invalid outputs and response-policy divergence.
- Decisive decision or feedback right: redirect or rebalance present goals/resources of operational units on a whole-system view and return the controlling action.
- Decision owner: external operator or agent runtime controls goals and thresholds; local service logic executes defined checks.
- Supporting / enforcement mechanisms: status MCP tools, operational logs, configured Grade thresholds, retry/circuit breakers, Gradient verdicts.
- Closure path: request/output → configured scoring/health decision → log/return/block; no whole-system S1 goal portfolio under OpenStinger control.
- Why this is / is not agent-owned: controlling an output channel is not equivalent to S3 governance over owned autonomous operations.
- Evidence: `gradient/interceptor.py`, `gradient/mcp/server.py`, `ingestion/scheduler.py`.
- Basis: whole-system owner and corrective-return discrimination.
- Confidence: high.
- Caveats: human or external-agent S3 can employ these tools as actuators in a larger system.

### Absence scope

- Surfaces inspected: Gradient mode/verdicts, health/audit MCP endpoints, job lifecycle and configured background workers.
- Plausible first-party paths checked: automatic response rewrite/block as current control, status monitoring and drift alerts.
- Why no material first-party path remains: they enforce predefined response/service policy without choosing changed commitments across first-party agent operations.

## S3* — Complementary audit

- State: —
- Function: Gradient checks, logs and drift notices provide optional response-evaluation support but no independently governed complementary audit path into an owned S3.
- Disturbance / variety regulated: candidate response inconsistency, safety/identity divergence and incomplete historical evidence.
- Decisive decision or feedback right: independently inspect actual operational truth, decide a complementary finding and compel corrective S3 follow-through.
- Decision owner: operator-provided profile/thresholds and externally integrated agent; Gradient evaluates supplied output with predefined tests.
- Supporting / enforcement mechanisms: value/identity/constraint/content scorers, correction engine, alignment history and audit store.
- Closure path: caller response → scores/verdict (observe-only by default; optional correction) → caller/record; no independent S3* actor with enforceable return to a first-party S3.
- Why this is / is not agent-owned: LLM-based scoring does not itself establish auditor independence, complementary operational evidence or a S3 corrective recipient.
- Evidence: `gradient/interceptor.py`, `gradient/correction_engine.py`, `gradient/mcp/server.py`.
- Basis: independence, decision-owner and feedback-return test.
- Confidence: high.
- Caveats: within a wider deployed organization, a separately staffed audit unit might use these results; that unit is outside this review.

### Absence scope

- Surfaces inspected: Tier 3 scoring/correction, drift status, operational logs and Gradient MCP tools.
- Plausible first-party paths checked: alignment evaluator and honeypot alerts as independent audit; corrective rewriting as audit closure.
- Why no material first-party path remains: no independent complementary auditor or owned S3 that must act on its findings is implemented in the package.

## S4 — Outside-and-then intelligence

- State: —
- Function: memory evolution and drift detection summarize past/ongoing content, not environmental futures and strategic capability adaptation.
- Disturbance / variety regulated: stale autobiographical notes, evolving facts, response-drift indicators and retention needs.
- Decisive decision or feedback right: sense prospective external threats/opportunities, compare alternatives and change future organizational capabilities.
- Decision owner: external agent/operator/developer defines integrations and decides deployments or strategy; vault note update is bounded classification.
- Supporting / enforcement mechanisms: StingerVault `Evolve`/`Decay`, temporal graph validity and Gradient drift checks.
- Closure path: new episodes → classify/update/expire notes → expose memory to caller; no prospective environment model → strategic selection → new operational capability.
- Why this is / is not agent-owned: a note named `identity` or `methodology` is mutable data, not organizational S4 governance.
- Evidence: `scaffold/vault_engine.py`, `temporal/engine.py`, `gradient/drift_detector.py`.
- Basis: prospective decision-right and implementation trace.
- Confidence: high.
- Caveats: future plans may add additional capabilities; this assessment does not project them into the pinned source.

### Absence scope

- Surfaces inspected: scheduled vault classification, temporal history, drift detector and README roadmap descriptions.
- Plausible first-party paths checked: note `Evolve` as strategic learning, drift alerts as environmental foresight and profile sync as capability change.
- Why no material first-party path remains: all update service memory/evaluation state; none chooses and implements a future-directed organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: profile/constraint evaluation and namespace admission apply inherited identity and guardrails, not legitimate ultimate organizational policy adjudication.
- Disturbance / variety regulated: mismatched outputs, absent API credentials, invalid namespace configuration and user-defined identity constraints.
- Decisive decision or feedback right: resolve contested purpose/identity at the organizational level and set the ultimate policy binding operating controls.
- Decision owner: external agent/operator authors profiles, constraints and configuration; software validates or evaluates them.
- Supporting / enforcement mechanisms: `SpawnContract`, vault identity notes, Gradient identity/constraint checks and configured observe-only enforcement.
- Closure path: externally authored policy/profile → deterministic validation or model score → pass/flag/correct/block; no self-owned constitutional policy judgment and mandate return.
- Why this is / is not agent-owned: treating an agent's stored identity as data or verifying a configured constraint does not confer authority to redefine that agent's mission.
- Evidence: `agents/spawn.py`, `scaffold/vault_engine.py`, `gradient/interceptor.py`, README.
- Basis: configuration authority versus implementation separation.
- Confidence: high.
- Caveats: genuine S5 could be human governance around an external system consuming OpenStinger.

### Absence scope

- Surfaces inspected: spawn contract, profile builder, vault notes, config gates and Gradient scoring/correction.
- Plausible first-party paths checked: `identity` vault category as policy owner, hard_block verdict as ultimate authority and namespace admission as constitutional boundary.
- Why no material first-party path remains: each accepts an inherited purpose/constraint and applies it; no legitimately authorized ultimate identity or policy redefinition belongs to the service.

## Recursion

Several namespaces can represent different external agents. OpenStinger stores and isolates their memory; it does not recursively own their objectives or coordinate their operational decision rights.

## Variety and escalation

The service attenuates high-volume session/response variety with fixed job batching, graph retrieval, model-backed extraction, classification, scoring and configured blocks. It can return alerts or enforcement results to an external actor. Neither operational task decisions nor overarching organizational judgments close inside the service.

## Evidence gaps

- Static reading of frozen source; no live provider, Docker, external autonomous-agent or security test was run.
- Model-based `memory_reflect`, structured extraction, vault classification and one-shot correction are acknowledged rather than ignored; their callable boundaries do not support a self-directed operational loop.
- No claim about answer quality, actual security effectiveness, or production behaviour of composed integrations.

## Assessment summary

**Proposed disposition: `excluded-no-agentic-vsm`.** OpenStinger is an MIT-licensed memory and alignment **service for external agents**. First-party model calls handle extraction, retrieval-grounded answering, classification and one rewrite/re-evaluation; none owns external goals, self-selected task actions and their feedback. Thus the supported boundary-relative vector is `— · — · — · — · — · —`.
