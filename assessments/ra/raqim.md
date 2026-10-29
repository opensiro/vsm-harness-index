---
harness_id: raqim
project_name: Raqim
repository: https://github.com/raqim-ai/raqim
review_ref: b795d9630d298408868429ae4bd2dd6c8ec1f541
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Raqim

## Review boundary

- System in focus: Raqim's first-party Rust ledger/policy daemon, Python instrumentation SDK, MCP gateway and management CLI at the pinned public source revision, not arbitrary external agent runtimes using them.
- Purpose and identity: receive and authenticate externally produced agent execution records, enforce configured namespace/rate policies on supported paths, record effects, provide replay/memory/audit data and route explicitly requested agent-to-agent messages.
- Relevant environment: external LLM agents, their tools and side effects, operators setting policies, network clients and storage/replay consumers.
- Standard-distribution boundary: `raqim-core` binary and libraries, `raqim-py/raqim/client.py`, `raqim-mcp`, `raqim-cli` and optional console; Python showcases are integration examples, not a default autonomous actor.
- Credited operating / distribution surfaces: daemon ingress and `PolicyEngine`, WAL/Merkle/effect storage, SDK `trace`/replay/requests, MCP tool dispatch, CLI/admin APIs and console.
- Adjacent first-party surfaces excluded from operational ownership: scripted quickstart/AML examples, load/siege tools, build scripts, tests and release workflow. These illustrate use but do not supply a general autonomous agent runtime.
- First-party modes considered: core daemon service, instrumented record/replay mode, A2A capability call, MCP bridge, console, demonstrations with either heuristic or optional Gemini inference.
- Recursion level: one support/control substrate beneath independently operated agents. Multiple registered agent identities or namespaces are not evidence that Raqim itself owns their task decisions.
- Reviewed revision: `b795d9630d298408868429ae4bd2dd6c8ec1f541`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The core starts an event bus, identity keys, `PolicyEngine`, WAL/Merkle/effect stores, registry, transports and admin APIs. Its decisions are deterministic authentication, configured namespace/rate enforcement and record handling. The Python SDK decorates *caller-supplied* functions, records their outputs, replays cached effects and exposes explicitly invoked capabilities. Its `boot` registers client identity; it does not accept a user goal and plan or choose the next model/tool action. The MCP bridge offers memory, record and request tools to **external** LLM assistants. The included demos sequence an AML screening function, a single LLM/heuristic verdict, record/replay and denial checks by script; a model response does not decide the next tool or loop termination.

The project's own scoped threat-model document describes the current product as a single-node execution-integrity daemon and distinguishes implemented limitations from roadmap ambitions. Its security caveats matter for accurate technical scope, but this VSM determination does not constitute a security audit or assert end-to-end enforcement of all external tool side effects.

Primary source at exact review ref:

- [README: identity, architecture, record/replay and external-agent integration](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/README.md)
- [Daemon startup and service wiring](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-core/src/main.rs)
- [PolicyEngine: namespace, rate and quarantine decisions](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-core/src/policy.rs)
- [Execution cascade and event schema](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-core/src/lib.rs)
- [Agent registry](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-core/src/registry.rs)
- [Python client: trace, replay, capability and control hooks](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-py/raqim/client.py)
- [MCP handler and request dispatch](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-mcp/src/main.rs)
- [Scripted quickstart: optional Gemini call](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/examples/01_quickstart.py)
- [Scripted agent-master showcase](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/raqim-py/agent_master_showcase.py)
- [Source-bounded threat model and non-goals](https://github.com/raqim-ai/raqim/blob/b795d9630d298408868429ae4bd2dd6c8ec1f541/docs/THREAT_MODEL.md)

## Operational model

An external agent or client chooses an action and invokes the SDK/MCP/ingress route with a signed identity and namespace. Raqim authorizes or denies the supported request under operator-provisioned rules, stores the accepted record/effect and returns status, proof, history or cached output. An external agent or developer determines what the result means for its objective and whether to change its next action. An SDK callback can receive an eviction directive, but the consuming agent must implement its own response. Replaying a recorded LLM result without inference is not a replacement for first-party autonomous goal selection.

## S1 — Operations

- State: —
- Function: no first-party goal-directed agent S1 owns task decomposition, model-selected interventions and learning from resulting tool observations.
- Disturbance / variety regulated: signed ingress requests, record/effect availability, cached replay, namespace checks and external-client communications; the open-ended task disturbance belongs to the caller.
- Decisive decision or feedback right: choose an action relevant to a user's objective, interpret its outcome and decide a subsequent action or stopping point.
- Decision owner: external agent or explicitly scripted demonstration author; Raqim's daemon handles that actor's requests.
- Supporting / enforcement mechanisms: `RaqimClient.trace`, signed TCP envelopes, policy checks, effect cache, WAL/Merkle pipeline and MCP tools.
- Closure path: external agent chooses request → Raqim validates/records or replays it → result returns to external agent; no first-party agent goal → judgment → next-tool loop closes inside Raqim.
- Why this is / is not agent-owned: `RaqimClient` is an identity-bearing instrumentation client, not an agent controller; the examples include a model call but script their next steps explicitly.
- Evidence: daemon entry, SDK `trace` and `ask_swarm`, MCP handler, `examples/01_quickstart.py` and `agent_master_showcase.py` (links above).
- Basis: repository architecture, concrete call/return code and negative loop inspection.
- Confidence: high.
- Caveats: a composed external autonomous agent *using* Raqim could satisfy S1=A at a separately declared broader boundary; that agency is not owned by this first-party runtime.

### Absence scope

- Surfaces inspected: daemon bootstrap, core ingress/cascade, policy, SDK run modes, MCP tools, documented architecture and scripted Gemini/heuristic demonstrations.
- Plausible first-party paths checked: `agent_master_showcase` model verdict, `RaqimClient` record/replay/fork, MCP `ask_swarm`, registry heartbeat and scripted A2A examples.
- Why no material first-party path remains: no shipped component turns a general goal and changing observations into self-chosen tool steps; provider calls and capability choices are explicitly invoked by external code.

## S2 — Coordination

- State: —
- Function: cryptographic identity, namespace isolation, A2A routing and replay convergence support other agents but do not evidence Raqim-owned S2 feedback between autonomous first-party S1 units.
- Disturbance / variety regulated: signed message routing, namespace conflicts, shared-state consistency, token-rate bursts and overlapping external clients.
- Decisive decision or feedback right: detect actual interference between autonomous operational units, decide corrective coordination and return adjustments to those units.
- Decision owner: supplied group configuration, transport/capability callers and external agent controllers; no separate first-party inter-S1 coordinator is shown.
- Supporting / enforcement mechanisms: `SwarmRegistry`, A2A capability dispatch, `PolicyEngine`, CRDT/registry and rate quotas.
- Closure path: registered external client/request → deterministic enforcement or message transport → client-side result; no cross-S1 conflict evaluation and returned coordinated work revision.
- Why this is / is not agent-owned: a policy firewall can attenuate unwanted calls without constituting an organization of first-party task-performing S1 agents.
- Evidence: `registry.rs`, `policy.rs`, `client.py`, `raqim-mcp/src/main.rs`.
- Basis: source-first boundary and closure inspection.
- Confidence: high.
- Caveats: policies can be imposed on many *external* agents; function ownership at that larger deployment is not inferred here.

### Absence scope

- Surfaces inspected: registry, policy enforcement, SDK A2A handling, MCP capability dispatch and core event bus.
- Plausible first-party paths checked: conflict-free state merges, multi-agent traffic limiting, quarantine and signed A2A calls as S2 coordination.
- Why no material first-party path remains: these regulate transport/permissions or preserve data, but do not own a decision over conflicting first-party autonomous operations with corrective return.

## S3 — Inside-and-now control

- State: —
- Function: the daemon can enforce preconfigured controls, report process statuses and quarantine requests, but does not govern and adapt whole-system current commitments of its own autonomous operational units.
- Disturbance / variety regulated: runtime ingestion rate, invalid identities, failed policies, WAL load, process registration and operator-directed restore.
- Decisive decision or feedback right: reallocate attention/resources or change active operational goals in light of a whole-system view and return the intervention to S1 execution.
- Decision owner: operator/configuration supplies admission and policy boundaries; deterministic `PolicyEngine` implements them; external agent owner decides task commitments.
- Supporting / enforcement mechanisms: token buckets, quarantine blocklist, checkpointing, admin lift, console telemetry and registry.
- Closure path: configured threshold/request → allow/deny/quarantine and notification → external operator/agent; no demonstrated system-wide S3 judgment over internally owned S1 commitments.
- Why this is / is not agent-owned: kill switches and health dashboards are useful control mechanisms, not sufficient evidence of discretionary whole-system S3 ownership.
- Evidence: `policy.rs`, `main.rs`, `registry.rs`, `client.py` control callback.
- Basis: code-grounded separation of enforcement from governance.
- Confidence: high.
- Caveats: a human/parent organization could use Raqim's control APIs as its S3 actuator outside the declared boundary.

### Absence scope

- Surfaces inspected: rate/quarantine state machine, daemon event bus, registry, admin lift and SDK eviction hook.
- Plausible first-party paths checked: automatic quarantine, dashboard swarm topology, resumption and context eviction as control authority.
- Why no material first-party path remains: each is a rule-bound or operator-triggered technical action, without a first-party S1 portfolio and returned S3 task-level control decision.

## S3* — Complementary audit

- State: —
- Function: cryptographic evidence, replay and Merkle proof tools support independent auditors but do not themselves provide a first-party complementary audit judgment with corrective return to S3.
- Disturbance / variety regulated: record tampering, replay divergence, historical observability and disputed execution traces.
- Decisive decision or feedback right: independently examine an operational claim against a complementary evidence path, determine a finding and change whole-system control.
- Decision owner: external auditor, operator or LLM assistant interpreting logs/proofs; Raqim supplies requested evidence and verification primitives.
- Supporting / enforcement mechanisms: WAL, effect history, Merkle leaves/proofs, MCP `query_memory`, admin replay views and threat model.
- Closure path: external query → record/proof/replay data → external interpretation; no independently owned S3* verdict and mandatory return to a governing S3.
- Why this is / is not agent-owned: immutable/auditable records are *audit inputs*, not an independent judgment unit. Source-authored threat model also identifies current limits of some claimed proof/security invariants.
- Evidence: `lib.rs`, MCP gateway, README and `docs/THREAT_MODEL.md`.
- Basis: evidence-vs-actor discrimination.
- Confidence: high.
- Caveats: no claim that every cryptographic/security feature is correct; this assessment is an autonomy function analysis, not a penetration test.

### Absence scope

- Surfaces inspected: WAL/Merkle pipeline, proof APIs, replay tools, MCP query/commit, console replay and threat model.
- Plausible first-party paths checked: Merkle validation as independent audit, anomaly dashboards, reconstructed history and local tamper evidence.
- Why no material first-party path remains: they return raw or mechanically checked evidence to an external evaluator, without autonomous audit interpretation and corrective escalation.

## S4 — Outside-and-then intelligence

- State: —
- Function: hypothetical replay forks and historical search do not constitute external prospective analysis of future capability or an adaptation decision.
- Disturbance / variety regulated: changed function inputs, divergent recorded effects, model prompts and software deployment versions.
- Decisive decision or feedback right: detect prospective environmental threats/opportunities, assess options and commit future organizational adaptation into current operating capability.
- Decision owner: developer/external agent selecting prompts, code changes and deployment strategy; SDK chooses deterministic cache miss/fork mechanics only.
- Supporting / enforcement mechanisms: `on_divergence`, replay cache, versioned execution history and demonstration scripts.
- Closure path: caller changes input/prompt → SDK fork/re-executes supplied function → result goes to caller; no prospective strategy selection or capability change owned by Raqim.
- Why this is / is not agent-owned: alternative replay branch is a technical test facility, not strategic intelligence.
- Evidence: `client.py`, `examples/01_quickstart.py`, README.
- Basis: decision owner and feedback return path inspection.
- Confidence: high.
- Caveats: external researchers can use counterfactual history for S4, but that is their organizational function.

### Absence scope

- Surfaces inspected: replay/fork behavior, memory search, demo prompt mutation, README claims and core configuration.
- Plausible first-party paths checked: prompt divergence as experimentation, historical trend analysis and code release roadmap.
- Why no material first-party path remains: no first-party future/environment sensing, option evaluation and authorized change into a governed S1/S3 capability is implemented.

## S5 — Policy and identity

- State: —
- Function: security-group manifests and cryptographic CA identity are configuration/enforcement, not a first-party authority resolving ultimate organizational identity and policy conflicts.
- Disturbance / variety regulated: unauthorized paths, capability lineage, credential expiry, namespace limits and operator-defined safe operating rules.
- Decisive decision or feedback right: legitimately decide a contested ultimate purpose/identity matter, set overarching policy and return its adjudication to operating control.
- Decision owner: operator/admin configuring group rules and minting credentials; daemon applies programmed checks, including default deny and quarantine.
- Supporting / enforcement mechanisms: `aegis.toml`, `PolicyConfigFile`, signing keys and certificates, hot reload, admin endpoints.
- Closure path: externally authored rule/credential → daemon policy enforcement → allow/deny and logging; no Raqim-owned constitutional identity adjudication or identity-level policy revision loop.
- Why this is / is not agent-owned: a CA root key is an authentication root, not an organizational S5 decision authority by itself.
- Evidence: `policy.rs`, `main.rs`, `aegis.toml`, `docs/THREAT_MODEL.md`.
- Basis: concrete separation of access enforcement from identity-policy decision ownership.
- Confidence: high.
- Caveats: security policy enforcement may be an actuator for an S5 in a larger organization; no such first-party owner is evidenced.

### Absence scope

- Surfaces inspected: security-group manifest, CA minting, policy hot reload, quarantine/lift, daemon boot and documented trust model.
- Plausible first-party paths checked: Swarm Master CA as sovereign identity, auto-quarantine as policy adjudication and user-supplied group changes as parent-returned authority.
- Why no material first-party path remains: there is no organizational identity conflict judgment, legitimate governing choice and returned whole-system constitutional update within the Raqim runtime.

## Recursion

Named external agents, groups and namespaces are tracked workloads or trust principals, not separately evidenced *Raqim-owned* viable S1 organizations. The embedded SDK and MCP gateway have no goal-directed autonomy of their own.

## Variety and escalation

Raqim attenuates network and record variety through signed requests, namespace/rate rules, cached effects and evidence serialization. It can enforce predetermined thresholds and emit escalation/eviction data; task meaning, revised plans, policy authorship and audit judgments remain with external agents/operators. This division matters even when an external AI agent consumes a tool result and subsequently adapts.

## Evidence gaps

- Static source-first analysis at the exact pinned commit. No agent/provider E2E execution, network exposure testing, security penetration test, or empirical proof of all advertised enforcement/replay guarantees.
- The optional Gemini demos make model calls, but each surrounding step is explicitly scripted and does not evidence a goal-directed first-party agent loop. The resulting boundary-relative exclusion does not deny Raqim's value as a supporting control-plane component.
- Raqim's own `docs/THREAT_MODEL.md` labels important current enforcement/proof limitations; those are not independently re-audited here and are not needed to prove or disprove organizational function ownership.

## Assessment summary

**Proposed disposition: `excluded-no-agentic-vsm`.** Raqim is an Apache-2.0 agent-execution ledger, instrumentation/replay SDK and policy service whose first-party code receives, constrains and records **external** agent behavior. A scripted demonstration with a model verdict does not transfer the external agent's objective, next-action choice or control loop to the substrate. The supported six-function vector is bounded negative (`— · — · — · — · — · —`).
