---
harness_id: phi-agent
project_name: phi-agent
repository: https://github.com/hibuka-labs/phi-agent
review_ref: 7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# phi-agent

## Review boundary

- System in focus: The published phi-agent Rust library and shipped `phi` executable as a configured LLM-backed agent/session runtime. An arbitrary host application built with this library is outside the reviewed first-party operating boundary.
- Purpose and identity: Construct tool-using LLM agents with model provider configuration, event streaming, persistent conversation sessions, a CLI, and optional tool/MCP/skill integrations.
- Relevant environment: User prompts, configured LLM API, tool invocations and returned results, session files, CLI operator approvals and optionally composed multi-agent tools.
- Standard-distribution boundary: First-party `src/` and bundled Cargo features as installed. The published `agent-base`, `agent-works`, `phi-kernel-tools` and external providers are dependencies; their internal discretionary multi-agent or governance features do not automatically become first-party phi-agent organizational ownership.
- Credited operating / distribution surfaces: [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs), [src/event_log.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/event_log.rs) and default-supported CLI/agent library configuration.
- Adjacent first-party surfaces excluded from ownership: `examples/`, `benches/`, fuzz targets, project CI, documentation-generation and release management. Their examples corroborate possible composition but do not act as runtime owners in a default installed run.
- First-party operating / deployment modes considered: Default-feature library + interactive CLI session, one-shot invocation, operator tool approval handler; opt-in multi-agent feature and compositional tools considered explicitly, not credited without a proven S2 closure. Automatic approval and custom embedding modes are also available, but generic tool authorization is not constitutive governance.
- Recursion level: One agent with model-mediated tools/sessions, optionally configured with children through an external composition engine; no first-party organization of independent S1 operational units proven at this boundary.
- Reviewed revision: `7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a` at original public `main`; no repinning.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The project exports `PhiAgent` over an `agent_base::AgentRuntime` produced by the `agent_works::AgentBuilder`; tool-agnostic `PhiAgentConfig` supplies model, safety and turn limits. `PhiAgent::run_turn` uses the constructed runtime; a CLI supports one-shot and REPL execution with Ctrl-C cancellation, session/log persistence, tool permission approval and output rendering. Default features include file, MCP, logging, telemetry, compression and focus; `multi-agent` is a separately opted-in feature backed by external `agent-works` and `phi-kernel-tools` crates, and examples show optional composition. Persistent local session history and event logs describe individual run continuity rather than independent organizational audit. Sources: [README.md](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/README.md), [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs).

## Operational model

A developer configures provider, system prompt, tools and execution options. A model-backed runtime chooses answers and calls selected tools, incorporates their results and can continue the session; the CLI logs events and may interrupt runs. The first-party wrappers own the build and CLI invocation but do not own external crate internals. Distinct agent teams, independent reviewers, portfolio supervision, organization identity and future-directed control loops require additional hosting/application composition; they are not assumed from optional feature names or standalone examples.


## S1 — Operations
- State: A
- Function: Run LLM-conditioned interactive or one-shot tool-using agent work.
- Disturbance / variety regulated: User requests and dynamically observed results of calls to configured tools.
- Decisive decision or feedback right: Select response, tool-call intent and subsequent turn from contextual model output through the installed runtime.
- Decision owner: Configured PhiAgent model-backed operational agent (through the published runtime wrapper), not the user-input event renderer or CLI log writer.
- Supporting / enforcement mechanisms: AgentBuilder configuration, tool registry, turn count/safety limits, cancellation, session log and stream renderer.
- Closure path: `run_turn` routes model output and tool results through underlying runtime; tool outcomes and user feedback feed later turns; CLI records the outcome and preserves sessions.
- Boundary reachability: `PhiAgent::build` consumes the builder to produce an operative `AgentRuntime`, and the shipped CLI calls `PhiAgent::run_turn` in one-shot or REPL modes.
- Why this is / is not agent-owned: Model-conditioned operational action is real; the Rust wrapper and external provider are supporting machinery and not independent organizational owners.
- Evidence: [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/bin/phi/main.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/main.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs)
- Basis: explicit first-party source; structural runtime entrypoint
- Confidence: high for code path, no live provider execution in this review
- Caveats: Runs require a configured model provider; supporting dependency behavior is not independently assessed.


## S2 — Coordination
- State: —
- Function: No supported first-party closure for concrete cross-agent interference among independent operational units is established.
- Disturbance / variety regulated: Competing subordinate agent commitments, resource conflicts or oscillating concurrent operations would require a distinct S2 function.
- Decisive decision or feedback right: No first-party function-specific inter-S1 conflict arbitration/feedback decision identified.
- Decision owner: None established in the published default or opt-in phi-agent wrapper; optional `MultiAgentRuntime` is constructed by external `agent-works` and returned for composition.
- Supporting / enforcement mechanisms: Optional multi-agent tool factory, session contexts, event transport and generic plans.
- Closure path: No shipped first-party path observed that identifies actual agent-agent interference, chooses an attenuating remedy and feeds that remedy into later distinct S1 behavior.
- Why this is / is not agent-owned: Spawning/delegating to a child or exposing a multi-agent runtime is not evidence of actual S2; the agent-works internals are outside this repository's first-party decisional evidence.
- Evidence: [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [examples/multi-agent/multi_agent.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/examples/multi-agent/multi_agent.rs)
- Basis: bounded source inspection of default and opt-in wiring
- Confidence: medium (scoped negative; dependent crate not evaluated)
- Caveats: A host application may compose cross-agent coordination separately; that outside code is not credited.

### Absence scope

- Surfaces inspected: [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml), [src/session/mod.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/mod.rs)
- Plausible first-party paths checked: Optional multi-agent feature and tool factory; default single-agent builder, session event/message transport, examples and CLI execution.
- Why no material first-party path remains: Only tool/child construction and external library runtime exposure are evidenced in the shipped first-party wrapper; no first-party interference-specific decision with subsequent S1 closure remains.


## S3 — Inside-and-now control
- State: —
- Function: No first-party whole-team current-management loop governing the shared operational commitments of multiple S1 agents is established.
- Disturbance / variety regulated: Portfolio priority, capacity, shared-resource allocation, blocked-team commitments and active performance interventions.
- Decisive decision or feedback right: No supervisor in this published wrapper receives a global operational view and decides cross-agent resource/commitment changes.
- Decision owner: Not established; host developer, CLI user and external multi-agent runtime can configure/interrupt individual runs, but do not constitute an evidenced S3 authority here.
- Supporting / enforcement mechanisms: Turn limits, safety config, individual cancellation, telemetry and tool-approval callbacks.
- Closure path: No first-party whole-system view → discretionary current-control decision → changed S1 commitment loop demonstrated.
- Why this is / is not agent-owned: A hard limit, cancel button or tool-approval prompt is enforcement of a local operation rather than whole-system current-control ownership.
- Evidence: [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs), [src/bin/phi/serve.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/serve.rs)
- Basis: bounded shipped source
- Confidence: medium-high for described boundary
- Caveats: Operator-owned supervision may be constructed in a different host; not evidenced as first-party runtime.

### Absence scope

- Surfaces inspected: [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs), [src/bridge/server.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bridge/server.rs)
- Plausible first-party paths checked: Multi-agent optional runtime, per-agent safety/telemetry, CLI prompt approvals, bridge server and cancellation.
- Why no material first-party path remains: Those paths regulate or observe one agent/tool/run and do not close whole-team shared commitments; no first-party S3-specific supervisor or legitimate parent return mode is packaged.


## S3* — Complementary audit
- State: —
- Function: No sufficiently independent source-of-reality audit with its own corrective feedback path is shipped.
- Disturbance / variety regulated: Misleading agent self-reports, incomplete or false task completion, undiscovered operational deviation.
- Decisive decision or feedback right: No separate auditor with complementary access and independent judgment over first-party operational reality shown.
- Decision owner: None established; event logs, CLI output, telemetry and sample observability are ordinary reports/recording.
- Supporting / enforcement mechanisms: Session event logs, telemetry, rendering adapters, optional test and logging infrastructure.
- Closure path: No first-party independent evidence inspection triggering a corrective decision returned into an ongoing agent process.
- Why this is / is not agent-owned: Persistent logs do not become audit merely by being durable or reviewable.
- Evidence: [src/event_log.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/event_log.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/render/mod.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/render/mod.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs)
- Basis: bounded inspection
- Confidence: medium-high
- Caveats: An external audit tool or application could be composed, but no shipped independently judging auditor is credited.

### Absence scope

- Surfaces inspected: [src/event_log.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/event_log.rs), [src/render/mod.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/render/mod.rs), [src/bin/phi/run.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/run.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs), [tests/common/mod.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/tests/common/mod.rs)
- Plausible first-party paths checked: Telemetry, event capture, session persistence, renderers, standard tests and example-specific observability.
- Why no material first-party path remains: All checked paths report/retain the same runtime outputs or are development tests, not an independent complementary access-and-corrective-judgment channel.


## S4 — Outside-and-then intelligence
- State: —
- Function: No first-party environment-facing prospective adaptation loop that modifies later organizational capability is established.
- Disturbance / variety regulated: Future model/provider/tool/environment changes requiring revised agent abilities or deployment strategy.
- Decisive decision or feedback right: User/developer configures model, feature flags and tool registry; no shipped agent/adaptation actor decides new future capability and returns an adopted change.
- Decision owner: No qualifying first-party S4 owner; dynamic prompt/context compression and memory are within-run support, not future strategic adaptation.
- Supporting / enforcement mechanisms: Model configuration, compression middleware, optional MCP management, examples and session context.
- Closure path: No external foresight → adaptation alternative → changed supported future capability → subsequent operational adoption loop shown.
- Why this is / is not agent-owned: Context management and provider selection by a constructor do not demonstrate external/prospective option selection and closure.
- Evidence: [src/config/llm.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/config/llm.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs), [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml)
- Basis: bounded source and feature declarations
- Confidence: medium
- Caveats: Tool providers may change independently, but their adaptation loops cannot be donated to phi-agent.

### Absence scope

- Surfaces inspected: [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/config/llm.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/config/llm.rs), [src/session/context.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/session/context.rs), [Cargo.toml](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/Cargo.toml)
- Plausible first-party paths checked: Model/provider switching, compression/memory, optional plugins, MCP connections and runtime option configuration.
- Why no material first-party path remains: These are in-session context/tools and static developer-configured extensions without a material first-party outside-and-then decision returned to future capability.


## S5 — Policy and identity
- State: —
- Function: No first-party identity/ultimate-policy authority closing the purpose and constitutional rules of a multi-agent organization is established.
- Disturbance / variety regulated: Changes to collective purpose, identity, ultimate non-negotiable organizational policy and its legitimate owner.
- Decisive decision or feedback right: No ultimate organization-level policy revision decision/return discovered; tool approvals authorize a current action.
- Decision owner: No qualifying S5 agent, constructor or parent owner in the declared package boundary.
- Supporting / enforcement mechanisms: SafetyConfig, interactive approval mode, tool allow/deny decision, system prompt and opt-in feature flags.
- Closure path: Approvals affect current tool execution only; no identity policy decision reaches a legitimate high-level owner and returns to govern a subsequent organizational constitution.
- Why this is / is not agent-owned: Static safety settings and a CLI yes/no confirmation are not identity/ultimate-policy adjudication.
- Evidence: [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/approval.rs)
- Basis: bounded first-party runtime/configuration inspection
- Confidence: medium-high
- Caveats: Not claiming hosted organizations around the library lack an S5 system.

### Absence scope

- Surfaces inspected: [src/cli/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/cli/approval.rs), [src/agent/factory.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/factory.rs), [src/agent/builder.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/agent/builder.rs), [src/bin/phi/approval.rs](https://github.com/hibuka-labs/phi-agent/blob/7c9b17c40d0ecdc04f3e51ca3c5fe7be77b1421a/src/bin/phi/approval.rs)
- Plausible first-party paths checked: Risk approval handlers, developer supplied prompts, session cancellation and optional multi-agent wrappers.
- Why no material first-party path remains: They perform individual tool authorization or configuration, not a first-party identity/policy decision-and-return at organizational recursion.

## Recursion

The default system is one model-backed agent/session with developer-supplied tools. An optional `multi-agent` feature can wire external `agent_works::multi_agent` and a tool factory, but this source-only review cannot infer an independently governed nested viable organization from that construction. Separate hosts using the library are not automatically grouped into one first-party recursion.

## Variety and escalation

Relevant variability includes prompt requests, tool errors and permission decisions. The first-party wrapper supports per-turn safety caps and cancellation; interactive CLI approvals can refuse a tool call. These are support constraints on the S1 loop; they do not prove S2 conflict attenuation or S3/S5 organizational governance.

## Evidence gaps

- No live provider call, runtime source inspection of `agent-works` / `phi-kernel-tools` crates, or independent second VSM reviewer was performed. Their internal behaviors must not be claimed as local first-party organizational decision rights.
- A specifically installed multi-agent host that demonstrates conflicting S1 commitments and a first-party attenuating/feedback loop could justify a new scoped assessment, but is not part of this standard first-party source review.
- No integrated second audit agent, prospective capability adaptation feedback or organization-wide identity authority is established at this pinned boundary. These negatives are bounded to the actual first-party package surfaces and do not rule out future downstream composition.
