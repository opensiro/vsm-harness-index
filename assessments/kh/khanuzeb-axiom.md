---
harness_id: khanuzeb-axiom
project_name: AXIOM
repository: https://github.com/KhanUzeb/AXIOM
review_ref: ba3a9bddce05990593035eab635eee9f45c46ff5
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AXIOM

## Review boundary

- System in focus: the shipped AXIOM STEM-question-solving service in its configured LangGraph mode: a coordinator selects concurrent specialists, a separate critic challenges their work, and an aggregator emits an answer or bounded unresolved result.
- Purpose and identity: solve user math, physics, chemistry, research and document-grounded problems with agent-selected computation and explicit answer checks.
- Relevant environment: varying STEM queries and conflicting solver answers, code execution failures, document evidence, external constants, optional local stores, provider errors and user-specified contexts.
- Standard-distribution boundary: `app/api/main.py`, `app/graph/build_graph.py` and `state.py`, `app/agents/`, `app/tools/`, `app/memory/`, `app/rag/`, `app/config.py` and documented `run.py` entrypoint at frozen revision. LangGraph, Groq/OpenRouter/Gemini models, SymPy, Python subprocess, Tavily, Qdrant/FAISS and Redis are integrated dependencies, not first-party organizational owners.
- Credited operating / distribution surfaces: supported `/solve` and `/solve/stream` LangGraph paths, built-in model-facing coordinator and specialist nodes, reducer-backed shared state, mandatory in-graph critic and returned corrective route; supported deterministic school fast path and separate `/chat-doc` path are explicitly distinguished.
- Adjacent first-party surfaces excluded from ownership: `app/evals/eval_harness.py` concurrent benchmark cases and offline answer scoring; `tests/` unit/regression fixtures; repository maintenance, `CITATION.cff` and development UI/debug tooling. These may corroborate design but are not an in-run organizational auditor or policy decision owner.
- First-party operating / deployment modes considered: provider-configured full multi-agent graph (synchronous or SSE API), optional model/provider fallback, local API-key gate, Redis/in-process cache, Qdrant/FAISS memory, PDF RAG branch, standalone `/chat-doc`, and unaudited deterministic school-solver bypass. The positive S2 and S3* witnesses apply to the full graph, not to bypass/cache modes.
- Recursion level: one AXIOM graph-solving organization for a user question, with multiple specialized task work cells. Independently deployed API replicas or the repository's contributor organization are outside this runtime recursion.
- Reviewed revision: `ba3a9bddce05990593035eab635eee9f45c46ff5`; observation 2026-10-30; generated and current Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

`/solve` initializes a state and invokes a compiled LangGraph. An LLM-driven coordinator selects math/physics, reasoning, code, research, visualization, RAG or chemistry specialists; `Send` fans out to several in one superstep. Reducers combine per-branch keys and lists. After sufficient work (or the hop cap), a critic receives original query, raw specialist results and reasoning trace, independently re-derives certain equations and numerical/unit/chemistry claims, then requests a model audit. PASS leads to aggregation; REVISE/FAIL returns to the coordinator for bounded targeted work. The aggregator composes the final response and surfaces unresolved critic errors. A deterministic school solver, cached reply or direct document chat can bypass the graph and its critic, and explicitly does not acquire the graph-only audit claim.

The operator supplies credentials and provider/configuration choices. Optional persistent memory and RAG are retrieval facilities; Langfuse logs traces. `app/evals/eval_harness.py` is an optional separate benchmark caller rather than a controlling node in a served solve request.

## Operational model

The operational outcome is a STEM answer, computation, plot, sourced information or explicit unresolved result. Distinct specialist work cells use model/tool discretion to transform a query and intermediate state; code can execute bounded subprocess Python, and research can query Tavily. The coordinator/graph supplies shared-state coordination and the critic supplies a different checking path. Graph hop limits, API auth and provider fallback enforce constraints selected by developers/operators; they do not thereby own a separate S3 or S5 decision.

## S1 — Operations

- State: A
- Function: specialist agents solve and revise the requested STEM or document-grounded task using calculations, code, research, retrieval and reasoning.
- Disturbance / variety regulated: heterogeneous user problems, unknown equations/constants, failed code, incomplete or inconsistent intermediate results and missing evidence.
- Decisive decision or feedback right: model-backed coordinator selects work cells; model-backed specialists choose derivations, executable code, research/retrieval and follow-up work from task and returned results.
- Decision owner: first-party wired model agents in the full graph; providers supply inference but do not choose the repository's organizational wiring, and deterministic tools execute selected acts.
- Supporting / enforcement mechanisms: LangGraph `Send` and reducer state, SymPy, code-exec timeout/static blocklist, Tavily, local RAG, provider fallback, memory and bounded hops.
- Closure path: original query and intermediate observations → coordinator/specialist choice → computation or retrieval → returned result/critic suggestions → further specialist choice or assembled answer.
- Boundary reachability: `app/api/main.py` constructs `graph=build_graph()` and invokes `graph.ainvoke`/`astream_events` for non-fast-path queries; `build_graph.py` wires the specialists and return edge.
- Why this is / is not agent-owned: first-party model calls choose actual solver/code/research work and adapt to tool results; deterministic school calculations are a separate bypass and are not credited as autonomous work.
- Evidence: [API graph invocation](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/api/main.py), [graph wiring](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/graph/build_graph.py), [coordinator](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/coordinator.py), [specialists](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/specialists.py).
- Basis: structural.
- Confidence: high for source-wired agent rights; task success was not measured.
- Caveats: provider and hosted tool dependencies were not invoked; the static code blocklist is explicitly not a hardened sandbox.

## S2 — Coordination

- State: C
- Function: attenuate actual shared-state write collisions and input-dependency conflicts among concurrently dispatched STEM specialist cells.
- Disturbance / variety regulated: multiple `Send` branches write the same LangGraph superstep (`InvalidUpdateError` without reducers), can overwrite state, and code dispatched beside math/chemistry cannot see those same-hop prerequisites.
- Decisive decision or feedback right: first-party `merge_dicts`, `keep_last_status` and narrow `_specialist_payload` prevent update collisions; `_staged_dependent_agents` schedules a bounded later code hop only after solver results become visible.
- Decision owner: developer-defined deterministic S2-specific reducers/staging rules; model coordinator chooses possible parallel workers but does not own the decisive shared-write arbitration, so autonomous S2 authority is not established for this collision.
- Supporting / enforcement mechanisms: LangGraph reducer annotations, unique specialist result keys, one-shot staged-code marker and `max_agent_hops` guard.
- Closure path: concurrent specialist writes → reducer-preserved merged results → next coordinator state → dependent code is rescheduled with actual upstream result or task can aggregate; rejected duplicate work does not repeatedly collide.
- Boundary reachability: the shipped graph uses `GraphState` and `_specialist_payload` for every concurrent `Send`; the code dependency guard runs inside the standard coordinator path.
- Why this is / is not agent-owned: this is more than generic routing because the source names concrete simultaneous-write failures and stale same-hop inputs, and implements attenuation with feedback; the decisive collision policy is first-party deterministic constructor machinery, not agent-selected negotiation.
- Distinct S1 units: parallel math/physics, chemistry, reasoning, code, research, RAG and visualization specialists in a requested fan-out.
- Inter-S1 disturbance: simultaneous writes to `status`/`intermediate_results` and dependent code lacking same-hop math/chemistry work product.
- Attenuating coordination relation: reducer-backed per-specialist state merger, restricted `Send` payload and one-shot staged code dispatch on prerequisite availability.
- Feedback into subsequent S1 behaviour: merged intermediate state determines the next coordinator route; the staged second-hop code agent consumes prior solver outputs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: reducers and staged dispatch specifically prevent demonstrated parallel-write collisions and stale-prerequisite calculations, rather than merely forwarding tasks.
- Evidence: [reducer witness](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/graph/state.py), [minimal Send and stage routing](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/graph/build_graph.py), [dependency-staging guard](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/coordinator.py).
- Basis: structural.
- Confidence: medium-high for collision/staging path; no measured multi-agent contention trace.
- Caveats: last-wins scalar merging does not solve arbitrary semantic disagreement or concurrent external tool conflicts; no autonomous shared-resource negotiation is demonstrated.

## S3 — Inside-and-now control

- State: —
- Function: no separately established whole-system current resource/commitment regulation at this one-query graph boundary.
- Disturbance / variety regulated: work cells may consume tokens, fail tools or repeatedly revise, but response is bounded by developer-set hops and fixed model/provider choices.
- Decisive decision or feedback right: coordinator picks task specialists and critic-driven retries, while fixed hop caps can terminate; neither supplies evidenced shared resource bargaining, whole-current commitment control or accountability interventions across independent operations.
- Decision owner: model for task decomposition and developer/operator for static limits; no distinct first-party whole-system S3 authority.
- Supporting / enforcement mechanisms: `MAX_AGENT_HOPS`, provider fallback, step flags, graph termination and API status/streaming.
- Closure path: current-task results and critic suggestions return to the same task loop, not to a whole-system resource-priority controller with return to multiple S1 commitments.
- Why this is / is not agent-owned: naming the entry node "coordinator" and providing hard limits is insufficient to establish S3; its view is of the one task, not a managed population of current commitments.
- Evidence: [coordinator routing](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/coordinator.py), [graph](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/graph/build_graph.py), [settings](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/config.py).
- Basis: structural.
- Confidence: medium-high for shipped request boundary.
- Caveats: external API deployment schedulers are not first-party S3 owners in this assessment.

### Absence scope

- Surfaces inspected: API requests and streaming, graph and coordinator, specialist statuses/flags, settings, model fallback and optional memory/cache.
- Plausible first-party paths checked: global `graph` object, task fan-out, hop cap, critic rerun, API key, Langfuse traces, concurrent eval cases and provider retries.
- Why no material first-party path remains: only per-request work routing and enforcement are wired; the optional eval harness is adjacent and no controller with a whole-service current view and discretionary resource/commitment intervention returns to service work.

## S3* — Complementary audit

- State: A
- Function: independently challenge a bounded class of specialist solution claims through a separate checking path before answer publication.
- Disturbance / variety regulated: incorrect algebra roots, unit/dimension mismatch, numeric/symbolic disagreement, chemistry mass imbalance and conflicting model-specialist accounts.
- Decisive decision or feedback right: a separate critic model evaluates original query, intermediate results, raw reasoning trace and programmatic rechecks, issues PASS/REVISE/FAIL and suggestions; failed independent programmatic checks override any critic PASS.
- Decision owner: first-party wired critic agent for semantic audit judgment, with deterministic independent re-derivation and hard failure override; the solver specialists do not choose the critic's verdict.
- Supporting / enforcement mechanisms: SymPy re-solving of original recorded equation, numeric cross-check, Pint dimensions, chemistry mass-balance routines, budgeted critic payload, verdict parser and graph gate.
- Closure path: specialist claims/raw trace → independent re-derivation and critic judgment → `critic_report` → `route_from_critic` reopens specific specialist work (unless capped), or PASS allows aggregation; unresolved findings are surfaced in final answer.
- Boundary reachability: `build_graph.py` mandates `critic_node` before aggregation in the full graph; `critic_agent.py` is a shipped node, not the optional offline `eval_harness`. Fast school and `/chat-doc` bypasses are excluded from this positive mode.
- Why this is / is not agent-owned: a distinct model call judges cross-agent consistency and mistakes instead of merely accepting their output; separate deterministic algorithms rederive selected claims from lower-level evidence. Static override enforces the check but does not choose the critic's full audit findings.
- Claim being audited: math/physics/chemistry correctness and consistency of specialist-generated answer components (not general correctness of arbitrary website facts or external provider output).
- Ordinary reporting path: specialists write `intermediate_results` and summarized reasoning/answer paths for the aggregator.
- Complementary access path: critic receives original query, raw per-specialist trace/tool inputs and a separately recalculated SymPy/numeric/unit/chemistry check, rather than only the aggregator's success assertion.
- Independence boundary: distinct critic node/model invocation plus programmatic re-derivation independent of solver-produced numeric answers; both remain within one local graph/provider environment and trace inputs can still share upstream modeling errors.
- Who acts on findings: the graph routes REVISE/FAIL into the coordinator's bounded rerun, and the aggregator reports unresolved faults at the hop limit.
- Evidence: [critic audit and verdict override](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/critic_agent.py), [fresh algebra recheck and unit checks](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/evals/guardrails.py), [returned critic control edge](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/graph/build_graph.py), [unresolved handling](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/aggregator.py).
- Basis: structural.
- Confidence: medium, restricted to corroborated classes of mathematical/structural claims; not observed audit effectiveness.
- Caveats: a routine critic name alone would not qualify; the positive mapping depends on complementary raw-trace access and independent recomputation. The fallback may PASS when checks are unavailable, no independent external web-ground-truth audit exists, and no provider-backed run was executed.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported prospective environmental-model and capability-adaptation loop beyond present query solving.
- Disturbance / variety regulated: research results, changing APIs and remembered user context can alter a current answer, but are not developed into future operating strategies.
- Decisive decision or feedback right: research Tavily, PDF RAG and FAISS/Qdrant memory supply current-task evidence; developer/operator configures providers, model lists and future code.
- Decision owner: task agents choose retrieval for the present problem, while maintainers/operators own durable capability changes outside the assessed graph.
- Supporting / enforcement mechanisms: Tavily, RAG retrieval, saved turns, provider fallback, offline eval cases, static model/configuration.
- Closure path: new facts or recalled turns feed the next answer, with no distinct prospective option selection returning to changed harness capability or S3.
- Why this is / is not agent-owned: web search and persistence alone are S1 information gathering, not outside-and-then organizational adaptation.
- Evidence: [research node](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/agents/specialists.py), [memory façade](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/memory/store.py), [RAG](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/rag/retriever.py).
- Basis: structural.
- Confidence: medium-high at shipped service boundary.
- Caveats: model providers can evolve externally, but that evolution is not a first-party AXIOM S4 decision owner.

### Absence scope

- Surfaces inspected: coordinator prompts, research/RAG, conversational memory, provider fallback, offline eval harness, README and configuration.
- Plausible first-party paths checked: external-constant search, document retrieval, memory recall, cached answers, fallback-model selection and benchmark cases.
- Why no material first-party path remains: all are current-query adaptation or adjacent testing; none creates prospective options and returns accepted change into the standard distribution's future solver capability.

## S5 — Policy and identity

- State: —
- Function: no legitimate first-party ultimate identity/policy decision-and-return path in the shipped service.
- Disturbance / variety regulated: credentials, code safety, allowed execution and API access are governed by operator/developer settings, not a runtime policy authority balancing identity decisions.
- Decisive decision or feedback right: operator sets `AXIOM_API_KEY`, provider keys, hop/code limits; static blocklist/middleware enforces these inputs and agents solve within them.
- Decision owner: external API deployer/developer for security and task constraints, not a first-party S5 autonomous or closed parent mode.
- Supporting / enforcement mechanisms: API key middleware, `MAX_AGENT_HOPS`, static code blocklist, subprocess timeout, config/default prompts.
- Closure path: startup rules gate requests/tools, without identity-level proposal → legitimate policy authority → authoritative decision → return governing subsequent operation.
- Why this is / is not agent-owned: technical authorization and per-task acceptance/retry do not confer ultimate-policy authority.
- Evidence: [settings](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/config.py), [API middleware](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/api/main.py), [guardrails](https://github.com/KhanUzeb/AXIOM/blob/ba3a9bddce05990593035eab635eee9f45c46ff5/app/evals/guardrails.py).
- Basis: structural.
- Confidence: medium-high for the shipped first-party service.
- Caveats: public repository contribution decisions and operator-local admin choices are adjacent human governance, not in-run S5 closure.

### Absence scope

- Surfaces inspected: user API and auth, graph entry/critique, agent prompts, config, code-exec guardrails, memory/cache and README deployment instructions.
- Plausible first-party paths checked: API-key verification, prohibited code patterns, model/provider fallback, task critic verdict, UI controls and maintainer changes.
- Why no material first-party path remains: these enforce preset operational rules or external developer choices; no first-party path escalates identity-level disputes to authoritative judgment and feeds settled policy back into later graph operation.

## Distributed OSS parent arrangement

Repository authors and operators can alter source, launch options and credentials, but the standard-distribution request graph does not route whole-system S3/S4/S5 matters into a documented distributed project authority and back into its running service. Local user intervention and GitHub contribution are not assumed to be parent VSM closure.

## Self-hosted and non-human modes

The service can be run locally with optional external LLM, vector store and cache backends, and an optional API key. The graph has bounded autonomous specialist decisions; manual configuration does not establish an additional S3/S4/S5 parent mode. Full-graph S3* does not extend to unaudited deterministic school fast-path, cached replies or direct document chat.

## Recursion

Specialists are separate S1 work cells within one STEM solve, but no child is evidenced with its own independent S2–S5 metasystem or durable identity. LangGraph nesting and concurrent evaluation cases do not establish a recursively viable suborganization.

## Variety and escalation

Parallel model/tool specialties amplify problem-response variety; reducer state and staged code hops attenuate collision/dependency variety. The critic's distinct recomputation and revision signal re-enter the same bounded graph. Provider errors trigger a fallback model; fixed hop and code-exec bounds are enforcement, not independently owned S3 or identity-policy escalation. No separate algedonic organizational channel is established.

## Evidence gaps

- No live LLM provider, Tavily search, untrusted Python execution, Qdrant service, external website or end-to-end evaluation was run; code-only evidence supports wiring, not effectiveness or safety.
- The audit witness is specifically independent algebra/unit/numeric and cross-specialist checking. It cannot verify external web claims, and trace-fed evidence may share upstream solver errors; confidence in broad independent operational reality is bounded.
- `merge_dicts` and last-status reducers address documented concurrent-write collisions but do not prove semantic convergence when specialists disagree. S2 agent-owned negotiation is not inferred.
- Adjacent `app/evals/eval_harness.py` concurrently scores known answers but is not wired as a runtime S3* feedback controller.
