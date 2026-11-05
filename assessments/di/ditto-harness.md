---
harness_id: ditto-harness
project_name: Ditto Harness
repository: https://github.com/ditto-assistant/ditto-harness
review_ref: 8785d38b4aa64f7167860132204ec60c9cfece1b
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ditto Harness

## Review boundary

- System in focus: the installable Rust `ditto-harness` conversation/memory engine and its CLI/Node integration, not the external Ditto production backend or the DittoBench miner/validator network.
- Purpose and identity: answer a user's multi-turn request with model-selected tools while optionally retrieving and persisting personalized memories, subjects and retrieval metadata.
- Relevant environment: user questions, previous session artifacts, embedded SQLite/Turso memory, model and embedding providers, host-defined tools, repeated tool calls, memory noise and context limits.
- Standard-distribution boundary: first-party `crates/harness` chat façade, agent loop, memory tools/store, retrieval/dream modules and shipped CLI/Node wrappers; an importing application supplies the model and arbitrary external tools. Benchmark scoring, billing and closed-source Ditto features are explicitly absent.
- Credited operating / distribution surfaces: [README](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md), [agent loop](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [chat façade](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/chat.rs), [memory tools](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/memory/tools.rs), [dream pipeline](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/dream.rs).
- Adjacent first-party surfaces excluded from ownership: `dittobench-starter-kit` and remote validator, Ditto's private production backend, repo/build CI, docs test cases and mocks; consumption of this library does not transfer those systems' decisions to the assessed boundary.
- First-party operating / deployment modes considered: `chat::Harness::run` with optional memory and injected host tools; raw `agent::Loop::run_streaming`; Ollama or OpenAI-compatible provider; CLI chat; NAPI Node wrapper; optional composite retrieval/reranker and separately invoked dream maintenance.
- Recursion level: one user's memory-backed conversation task run with optional multiple tool calls, not a multi-agent company or the decentralized mining subnet.
- Reviewed revision: `8785d38b4aa64f7167860132204ec60c9cfece1b`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`chat::Harness::prepare` normalizes the conversation, derives a knowledge-graph/session ID, retrieves personal memories through the Store and appends memory-context messages. It exposes host-provided tools and five bundled memory tools. `agent::Loop::run_streaming` then repeatedly calls the configured `Model::next`, executes the model's tool requests (possibly multiple in one turn), records tool outputs in the conversation and lets the model continue or produce a final answer. Maximum turns, cost aggregation and repeat-tool-call detection bound execution. The default `NoopHandler` **does not veto** repeated calls; an embedding host can implement `decide_repeated_tool_call` to block a repeat when it knows side-effect semantics. Optional `save_memory` persists the final exchange. [Agent loop](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [chat façade](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/chat.rs), [loop detector](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/loopdetect.rs).

Memory storage uses an embedded vector-capable SQL backend, per-user/session context and optional composite retrieval with predicted signal-fusion weights and injected re-ranker. Composite retrieval is off by default. A separately triggered `dream` operation asks a model to extract and refine stable subject labels from past memory pairs, then deterministic merge/link logic updates the subject graph. This improves current and later recall but is not itself a forward-looking external adaptation function. Providers are chosen by a caller (Ollama, OpenAI-compatible) and model outputs are external dependencies. [README](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md), [dream](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/dream.rs), [models](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/models/mod.rs).

## Operational model

The operational actor is one task-scoped model deciding what tool to call next and when to stop, conditioned on returned tool results and retrieved memory. Tools, SQL and the dream pipeline are first-party constructor primitives, not distinct independent S1 units. The host supplies model identity, extensions and repetition-approval discretion. Loop event callbacks report progress but no first-party separate metasystem observes/controls a population of autonomous operations.

## S1 — Operations

- State: A
- Function: answer personalized requests through a multi-turn model/tool loop, including selected memory lookups and writes.
- Disturbance / variety regulated: changing natural-language queries, partial/noisy memory, unknown external tool results and repeated/failed calls.
- Decisive decision or feedback right: the configured model chooses which advertised tool and arguments to invoke or whether to deliver final text; subsequent choices incorporate returned tool outputs.
- Decision owner: model-backed `agent::Loop` cell running inside the first-party loop, with host-selected model and tool inventory.
- Supporting / enforcement mechanisms: `Tool` trait, memory search/fetch/save tools, loop limits, cost collection, `EventHandler`, optional persistence, repetition detector and provider adapters.
- Closure path: request and prepared memory context → `Model::next` → model-selected tool(s) → `handle_tool_call` execution/result → appended conversation → next model choice or final answer; optional memory save closes the turn.
- Boundary reachability: shipped `chat::Harness::run` constructs a real agent loop and passes memory plus injected tools, while the CLI exposes a standard chat mode and providers; not just a test fixture or proposed integration.
- Why this is / is not agent-owned: semantic tool choice and answer synthesis are delegated to the configured model; memory retrieval, persistence, concurrency and repetition counters are deterministic/runtime support.
- Evidence: [agent loop and calls](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [chat façade](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/chat.rs), [memory tools](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/memory/tools.rs).
- Basis: first-party frozen source, executable model/provider interfaces and shipped CLI mode.
- Confidence: high structural, no paid model E2E executed in this review.
- Caveats: host tools are arbitrary capabilities; neither their presence nor the provider selection establishes autonomous metasystem control.

## S2 — Coordination

- State: —
- Function: no inter-S1 collision/negotiation regulator established.
- Disturbance / variety regulated: multiple model tool calls and concurrent dream extractions could overlap in data, but no separate operational S1 actors with competing goals are coordinated.
- Decisive decision or feedback right: none over two independent operating cells.
- Decision owner: none at the declared recursion.
- Supporting / enforcement mechanisms: async tool dispatch, SQL upsert conflicts, duplicate subject merge, per-run sequential model turns.
- Closure path: tools return to one controlling model; no S1-to-S1 coordination contract changes two cells' future actions.
- Why this is / is not agent-owned: parallel tools, SQL idempotence and a multi-call model response are one S1's procedures, not a multi-S1 coordination function.
- Evidence: [agent tool dispatch](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [dream merge](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/dream.rs).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: an embedding application may run many loops and add coordination externally.

### Absence scope

- Surfaces inspected: `agent::Loop`, chat request preparation, memory tools/SQL, dream concurrency and CLI/Node adapters.
- Plausible first-party paths checked: simultaneous tool calls, background memory processing, user/session isolation, tool-repeat detector, host-shared storage and independent agents.
- Why no material first-party path remains: no two first-party agent work cells whose interference is sensed, adjudicated and returned as mutually adjusted operational decisions.

## S3 — Inside-and-now control

- State: —
- Function: no regulator decides current resources/commitments for a whole population of S1 operations.
- Disturbance / variety regulated: request-level turn budgets, cost, repeated calls and memory retrieval limits.
- Decisive decision or feedback right: host chooses model, tools, max turns and memory options; Rust loop enforces bounds without discretionary portfolio decisions.
- Decision owner: host configuration and deterministic loop rules; no first-party S3 owner.
- Supporting / enforcement mechanisms: max turns, cost collector, stop_reason metadata, event callbacks, per-request retrieval configuration.
- Closure path: requests terminate or emit progress; no whole-current task/agent commitment decision is fed into a distinct collection of S1 actors.
- Why this is / is not agent-owned: a per-run safety stop and billing data are not whole-system current regulation.
- Evidence: [RunRequest and Loop](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [chat request](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/chat.rs), [README boundary](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: the production Ditto backend and mining network can have other control systems, excluded from this repository boundary.

### Absence scope

- Surfaces inspected: agent loop, cost collector, chat API, Node/CLI and provider/router configuration.
- Plausible first-party paths checked: cost/time-limit governors, multiple sessions, operational portfolio dashboards, rescheduling/reassigning commitments, human supervisor return.
- Why no material first-party path remains: all shipped controls govern one conversation operation or caller parameters, not live cross-operation accountability or resource allocation.

## S3* — Complementary audit

- State: —
- Function: no independent reviewer inspects raw task reality and feeds a veto/correction into organizational control.
- Disturbance / variety regulated: repetitive tool effects, incorrect answers or bad retrieved memory.
- Decisive decision or feedback right: detector reports repeated identical calls, but default event handler explicitly **executes**; optional host-supplied handler may choose `Block`, without first-party evidence audit.
- Decision owner: host's injected handler for any repeat decision; no first-party complementary auditor.
- Supporting / enforcement mechanisms: repeat key/turn detection, tool progress/result events, optional future benchmark validator outside repo.
- Closure path: detection may be passed to host before a repeated call; the shipped default performs it, and no independent verification finding is returned to a controller.
- Why this is / is not agent-owned: matching successive tool call arguments is same-loop safety telemetry, not independently observing whether prior effects succeeded or whether claims match reality.
- Evidence: [EventHandler default](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [loop detector](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/loopdetect.rs), [README boundaries](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: a host may build external verification, but it must supply independent evidence and a corrective return before receiving S3* credit.

### Absence scope

- Surfaces inspected: repeat detection, event hooks, tool outputs, dream and retrieval stages, benchmark disclaimer.
- Plausible first-party paths checked: side-effect replay checks, agent-answer audit, LLM critic, separate factual oracle, external validator and host veto.
- Why no material first-party path remains: optional host intervention is a hook only; no first-party complementary evidence-acquisition and audit-to-control closure is implemented.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external/future-facing adaptation analysis closes a return into current operational capability.
- Disturbance / variety regulated: historical personal memories, changing recalled subjects and retrieval ranking quality.
- Decisive decision or feedback right: offline `Dreamer` uses an LLM to extract/condense *past* subject facts; caller controls when it runs and the retrieval mode.
- Decision owner: single-memory maintenance procedure and host, not a prospective environmental intelligence owner.
- Supporting / enforcement mechanisms: subject extraction, embedding dedup, MLP retrieval weights, optional reranker and vector database.
- Closure path: historic memories become subject graph entries and improve later retrieval; no future external scenario or adaptation option is generated for changing the agent's capability/policy.
- Why this is / is not agent-owned: memory consolidation and learned ranking are useful S1 information services, not S4 just because they persist over time.
- Evidence: [dream pipeline](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/dream.rs), [retrieval](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/retrieval/mod.rs), [README](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: downstream applications might add prospective strategy to this memory service, but none is first-party here.

### Absence scope

- Surfaces inspected: dream extraction/refine, retrieval MLP/reranker, CLI commands, README external backend boundary.
- Plausible first-party paths checked: future forecasting, external market/technology sensing, proposed capability changes, model/provider upgrades and automatic strategy revision.
- Why no material first-party path remains: offline past-memory consolidation has no future-external distinction or returned organizational adaptation judgment.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/policy decision loop for the harness installation.
- Disturbance / variety regulated: provider selection, tool availability, privacy scoping and storage of personal data rather than competing organizational ultimate purposes.
- Decisive decision or feedback right: application developer/operator chooses tools, model, user scope and runtime bounds before a run.
- Decision owner: external host; not first-party identity authority implemented in Ditto Harness.
- Supporting / enforcement mechanisms: user_id/kg_id/session_id isolation, `Options`, host-injected tool trait, optional memory persistence.
- Closure path: fixed host inputs constrain a run; no identity conflict rises to a legitimate authority that returns a policy decision into future agent operations.
- Why this is / is not agent-owned: normal configuration and data namespaces are not a standing policy-governance loop, and no closed-source product governance is borrowed.
- Evidence: [chat Options](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/chat.rs), [agent Options](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/crates/harness/src/agent/mod.rs), [README scope](https://github.com/ditto-assistant/ditto-harness/blob/8785d38b4aa64f7167860132204ec60c9cfece1b/README.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: host applications may supply user-authentication, billing or institutional governance outside the assessed library.

### Absence scope

- Surfaces inspected: public API configuration, storage scoping, supported interfaces and agent event hooks.
- Plausible first-party paths checked: model policy revision, parent authority approval, persistent normative decision, personal-data policy and returned identity governance.
- Why no material first-party path remains: no shipped pathway escalates an ultimate-policy question and enforces a legitimate returned choice beyond one host-configured task.

## Recursion

The conversation loop is one S1 operational unit. Memory stores, dream extraction, retrieval models, multiple tools, sequential model turns, host APIs and the mining starter kit cannot be silently promoted into separate autonomous recursive systems at this boundary.

## Variety and escalation

Prepared memory context attenuates missing information; model-selected tool calls respond to query uncertainty; optional re-ranker changes retrieved evidence; max turns and host-controlled repeated-call gates constrain local loops. Failure and exhaustion return to the caller, not to a first-party higher-recursion S3–S5.

## Evidence gaps

- Frozen Rust source and released CLI/library contracts inspected; no live Ollama/OpenRouter run or full Rust integration build performed here.
- Model choice and arbitrary tool behaviors are supplied by embedding hosts, as is any repeat-call blocking authority; the default `NoopHandler` does not veto repeats.
- The README expressly excludes the Ditto production backend, validator/scoring network, billing and proprietary features. Their organizational processes are not credited.
