---
harness_id: asktravel-agent-harness
project_name: AskTravel Agent Harness
repository: https://github.com/stoicdataguy/asktravel-agent-harness
review_ref: 9204095f29720ba70cdd90c9ccd6d214cda36c72
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# AskTravel Agent Harness

## Review boundary

- System in focus: the concrete travel-agent API and default background memory-maintenance mode.
- Purpose and identity: produce grounded travel advice/itineraries while maintaining a user's facts and trips.
- Relevant environment: user conversations, guidebooks, live travel search services, Postgres and model-provider failures.
- Standard-distribution boundary: installed travel-agent FastAPI service with its configured LangChain graph, tools, middleware and optional default-enabled memory consolidation.
- Credited operating / distribution surfaces: src/travel_agent/agent, tools, skills, consolidation.py and API lifespan wiring.
- Adjacent first-party surfaces excluded from ownership: evaluation scripts/notebooks, fake-model test fixtures, architecture diagrams and unimplemented feedback-audit roadmap; Open WebUI, LangChain internals, providers and search platforms are external.
- First-party operating / deployment modes considered: self-hosted chat service with consolidation enabled or disabled; neither custom SDK compositions nor future plans donate functions.
- Recursion level: travel-assistant service; chat work is S1, the separate memory integrity challenge is scoped to the same service's persisted user claims.
- Reviewed revision: 9204095f29720ba70cdd90c9ccd6d214cda36c72.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/travel_agent/agent/graph.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/graph.py) builds create_agent with guidebook/flight/hotel search, memory/trip tools, skill loading and structured itinerary presentation. Dynamic prompts reread per-user facts/trips on each model call; middleware compacts older tool results, retries provider errors and indexes chats. Postgres supplies checkpoint/store persistence. [src/travel_agent/api/app.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/app.py) wires the graph and, by default configuration, a separate idle-chat memory-review loop. [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py) gives a fresh structured model call saved facts plus raw user messages, then applies guarded corrections and logs changes. The actor is not the deterministic scheduler or quote matcher. Operators configure deployment and users direct travel work/data deletion. Tests/evals and planned thumbs-feedback tables do not own runtime decisions.

## Operational model

One model-backed travel actor chooses evidence gathering and itinerary content. Parallel tools are capabilities of that actor, not separately autonomous operational units. A background model reviewer can challenge persisted claims against user utterances after chats become idle. This limited audit does not attest itinerary quality, pricing correctness or all historical facts.

## S1 — Operations

- State: A
- Function: produce researched trip advice and structured itineraries.
- Disturbance / variety regulated: destinations, preferences, incomplete data, live tool observations and invalid itinerary arguments.
- Decisive decision or feedback right: choose searches/playbooks, interpret observations and select/revise the itinerary.
- Decision owner: the instantiated travel_agent model actor.
- Supporting / enforcement mechanisms: LangChain execution, first-party tool wrappers, Postgres, retry/compaction middleware and Pydantic validation.
- Closure path: tool and validation observations return to the model; present_itinerary persists and displays the chosen plan.
- Why this is / is not agent-owned: removing the model leaves storage/search wrappers without discretionary travel synthesis.
- Evidence: [src/travel_agent/agent/graph.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/graph.py); [src/travel_agent/api/app.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/app.py); [src/travel_agent/api/openai_compat.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/openai_compat.py); [src/travel_agent/tools/itinerary.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/tools/itinerary.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.
- Boundary reachability: API lifespan constructs build_agent; the public chat router invokes that graph with user context.

## S2 — Coordination

- State: —
- Function: No supplied regulation of a specific inter-S1 disturbance is established.
- Disturbance / variety regulated: parallel tools, independent chats and background upkeep must not be equated with coordinated autonomous work cells.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: thread/checkpoint branching, user namespaces, parallel tool execution and idle scheduling.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/travel_agent/api/thread_sync.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/thread_sync.py); [src/travel_agent/agent/graph.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/graph.py); [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py); [src/travel_agent/tools/memory.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/tools/memory.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: graph/tool bindings, thread_sync, per-user memory operations and background-loop scheduling.
- Plausible first-party paths checked: delegation or multiple S1 units, shared-memory collision regulation, chat branching and coordination feedback.
- Why no material first-party path remains: tools are one actor's capabilities; namespaces and transcript reconciliation preserve data paths, while idle scheduling supplies no distinct S2-specific discretionary coordination/return path.

## S3 — Inside-and-now control

- State: —
- Function: No whole-service current resource/commitment decision loop is supplied.
- Disturbance / variety regulated: provider rate limits and background workload are handled as configured runtime constraints.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: retry backoff, capped users per maintenance cycle, API state and database persistence.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/travel_agent/agent/retry.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/retry.py); [src/travel_agent/config.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/config.py); [src/travel_agent/api/app.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/app.py); [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: retry middleware, config, service lifespan, consolidation limits and operational API.
- Plausible first-party paths checked: whole-system allocation/intervention actor, feedback-based revision of commitments, legitimate parent current-control return.
- Why no material first-party path remains: fixed caps and retries enforce developer choices; user itinerary edits/data deletion are task-local and no shipped whole-system control loop closes.

## S3* — Complementary audit

- State: A
- Function: challenge the travel actor's persisted user-fact claims against raw user statements outside the ordinary chat-production path.
- Disturbance / variety regulated: misfiled interests/dislikes, contradicted or retracted saved facts and missing user-stated preferences.
- Decisive decision or feedback right: judge whether a saved user claim needs add/update/delete/noop and propose the smallest source-supported correction.
- Decision owner: the separately prompted structured memory-review model invoked by llm_proposer; not apply_plan's deterministic matcher.
- Supporting / enforcement mechanisms: idle-chat discovery, checkpoint access, guarded store writes, source-quote checks, sensitive-fact exclusion, MAX_OPS and memory_log.
- Closure path: the reviewer proposes corrections; accepted operations update the shared fact store, and graph.system_prompt reloads that store on subsequent model calls.
- Why this is / is not agent-owned: without the reviewer the scheduler and quote checker cannot decide semantic reclassification or contradiction; they only constrain/apply its proposed judgment.
- Evidence: [src/travel_agent/api/app.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/app.py); [src/travel_agent/config.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/config.py); [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py); [src/travel_agent/tools/memory.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/tools/memory.py); [src/travel_agent/agent/graph.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/graph.py); [tests/test_consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/tests/test_consolidation.py)
- Basis: structural
- Confidence: medium
- Caveats: A narrowly scoped source-supported memory-claim audit, not travel-answer verification. Same provider is permitted; trust is limited by selected recent messages, saved-fact evidence, model error, quote matching and excluded sensitive fields. No measured audit effectiveness.
- Claim being audited: persisted user facts written by ordinary save_memory calls faithfully represent user preferences/statements.
- Ordinary reporting path: the travel actor writes summarized facts through save_memory and later consumes their prompt projection.
- Complementary access path: consolidate_user reads HumanMessage content directly from checkpoints and compares it to the store in a fresh structured review context.
- Independence boundary: the producing chat actor neither selects the idle review invocation nor supplies its ordinary narrative as sole evidence; separate reviewer prompt and raw user messages can challenge that actor's stored claim. Shared provider/store do not establish global independence or coverage.
- Who acts on findings: guarded apply_plan updates memory and logs before/after; subsequent travel calls reread corrected facts.
- Boundary reachability: app.lifespan creates the nonstreaming proposer and run_consolidation_loop when default memory_consolidation is enabled; disabled mode intentionally has no audit run.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environment-to-capability adaptation loop is supplied.
- Disturbance / variety regulated: live travel availability and changed user preferences are current-task/domain data.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: search tools, skill playbooks, memory consolidation and dynamic prompt refresh.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/travel_agent/agent/prompts.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/prompts.py); [src/travel_agent/skills/__init__.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/skills/__init__.py); [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py); [docs/PLAN.md](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/docs/PLAN.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: skills loader/playbooks, travel searches, memory review, dynamic prompting and roadmap.
- Plausible first-party paths checked: external/future sensing, development of alternative future operating capabilities, autonomous or parent adoption feeding current capability.
- Why no material first-party path remains: current trip planning and evidence-grounded fact repair do not develop prospective harness-capability options; installed skills are authored playbooks and roadmap entries are adjacent plans.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate-policy or identity decision-and-return path is supplied.
- Disturbance / variety regulated: task preferences and data controls are not identity-level organizational disputes.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: system guidelines, sensitive-memory guard, settings and user export/delete endpoints.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/travel_agent/agent/prompts.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/agent/prompts.py); [src/travel_agent/config.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/config.py); [src/travel_agent/api/app.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/api/app.py); [src/travel_agent/consolidation.py](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/src/travel_agent/consolidation.py); [README.md](https://github.com/stoicdataguy/asktravel-agent-harness/blob/9204095f29720ba70cdd90c9ccd6d214cda36c72/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: prompt, service settings, data-control API, consolidation restrictions and README.
- Plausible first-party paths checked: agent identity amendment, legitimate parent ultimate-policy adjudication and authoritative returned governance.
- Why no material first-party path remains: developer rules and user data choices constrain ordinary operation; no first-party identity/ultimate-policy issue routing and returned authority loop is provided.

## Recursion

Chat threads, tool parallelism and the background reviewer do not establish recursively viable organizations.

## Variety and escalation

Middleware preserves task-specific tool feedback and exposes provider waits. Capped consolidation and quote checks attenuate memory-change risk. Errors return/log through ordinary channels, without an evidenced algedonic authority path.

## Evidence gaps

No live model/eval execution. S3*=A is limited to the raw-user-message memory challenge and return-to-prompt path; it does not claim exhaustive evidence, a different provider, or audit of final travel artifacts. Planned feedback-audit tables are not implementation evidence.
