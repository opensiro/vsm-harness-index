---
harness_id: sagamind
project_name: SagaMind
repository: https://github.com/BlurredBox/SagaMind
review_ref: 647fdcfd6b2c8def3775a3a2068aa27223bc1066
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SagaMind

## Review boundary

- System in focus: the first-party SagaMind core runtime at frozen revision `647fdcfd6b2c8def3775a3a2068aa27223bc1066`, including the REST/gRPC gateways, `SagaTransactionCoordinator`, Z3 verification gate, sandbox/tool registry, transaction state store, speculative draft executor, tiered memory retrieval/consolidation and first-party HTTP/MCP client surfaces.
- Purpose and identity: provide a transaction-safe execution and memory co-processor for externally driven agents, with verification, rollback/compensation, durable saga state, memory consolidation and speculative action validation around caller-supplied actions.
- Relevant environment: external agents or applications that choose goals/actions/drafts/invariants, human approvers, model providers or LLM clients supplied by integrators, Z3, TimescaleDB/PostgreSQL, Neo4j, Wasmtime, Redis and filesystem/database targets.
- Standard-distribution boundary: code and configuration actually present in the frozen repository distribution. External MCP clients such as Claude Code, downstream agents/applications, externally supplied LLM clients and backend services do not donate autonomous VSM ownership.
- Credited operating / distribution surfaces: `src/main.py`; `src/grpc_server.py`; `src/orchestrator/coordinator.py`; `src/orchestrator/sandbox.py`; `src/orchestrator/state_store.py`; `src/verifier/z3_prover.py`; `src/speculative/orchestrator.py`; `src/memory/**`; `sdk/client.py`; `sdk/mcp_server.py`.
- Adjacent first-party surfaces excluded from ownership: tests, demos, research/architecture documents, CI/contributor workflows and documentation-only claims. Optional downstream LLM summarization is considered only where the frozen runtime actually invokes it; an external model endpoint or MCP client remains environment.
- First-party operating / deployment modes considered: direct REST saga submission; direct gRPC saga submission; SagaMind MCP tools driven by an external MCP client; human approval/rejection of pending steps; scheduled/manual memory consolidation; speculative validation/commit of caller-supplied drafts; startup crash recovery/compensation.
- Recursion level: one SagaMind runtime/service. External agents that decide what actions to submit are separate systems-in-focus.
- Reviewed revision: `647fdcfd6b2c8def3775a3a2068aa27223bc1066`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

SagaMind ships substantial first-party runtime infrastructure, but the frozen standard distribution does not package an autonomous operational agent loop. The REST `StepProposal` schema requires the caller to supply `tool_name`, action `arguments`, compensation, invariants and approval mode. `/saga/step` validates that caller-owned proposal, constructs one `SagaStep` and passes it to `SagaTransactionCoordinator`. The gRPC surface mirrors the same ownership boundary: callers submit complete steps and the coordinator verifies/executes them.

`SagaTransactionCoordinator` is a real transaction controller. It verifies each supplied action, executes it through the sandbox, records completion, performs LIFO compensations after failure, pauses for human approval when requested, and restores incomplete sagas on startup. Those are meaningful safety/current-state mechanisms, but the coordinator does not decide what operational action should be attempted next from observations of the environment. The substantive step decision remains upstream with the external agent/application.

The MCP server makes that boundary explicit: it exposes SagaMind as tools so Claude Code or another MCP client can start a saga, submit steps, approve/reject, query status and retrieve memory. The external MCP client is therefore the decision-making system; SagaMind is the governed execution substrate it calls.

Speculative execution also does not close S1. `SpeculativeOrchestrator` accepts already formed draft commands from the caller, validates them in parallel and commits the first passing draft in input/result order. It does not generate alternative actions, compare goal-level consequences or feed execution observations back into a first-party model/agent decision loop.

Memory consolidation is similarly a support capability rather than S4 closure at this boundary. The scheduled/manual sleep cycle clusters stored episodes and writes semantic graph relationships. An optional caller-supplied LLM may label a cluster, but the resulting concept graph is not connected to a first-party autonomous operating loop that forms prospective adaptation options and changes current capability. Without an autonomous S1 boundary, the higher VSM functions cannot be credited as organizational ownership even where useful control mechanisms are present.

Primary evidence:

- [`src/main.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/main.py) — REST request schemas and caller-driven saga/speculative endpoints.
- [`src/grpc_server.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/grpc_server.py) — gRPC surface mirrors caller-supplied `SagaStep` execution rather than an autonomous agent loop.
- [`src/orchestrator/coordinator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/coordinator.py) — verification, execution, approval pause, compensation, recovery and saga status lifecycle.
- [`src/orchestrator/sandbox.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/sandbox.py) — governed tool execution/compensation registry for supplied actions.
- [`src/verifier/z3_prover.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/verifier/z3_prover.py) — deterministic caller-invariant safety gate.
- [`src/speculative/orchestrator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/speculative/orchestrator.py) — parallel validation of supplied drafts and first-valid commit.
- [`src/memory/consolidation.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/memory/consolidation.py) — deterministic episodic clustering/graph projection plus optional externally supplied LLM labelling.
- [`sdk/client.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/sdk/client.py) — thin API client requiring the integrator to submit complete actions/invariants.
- [`sdk/mcp_server.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/sdk/mcp_server.py) — exposes SagaMind as tools to an external Claude Code/other MCP client.
- [`README.md`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/README.md) — product scope as transaction-safe multi-agent runtime/memory co-processor and documented control mechanisms.

## S1 — Operations

- State: —
- Function: no autonomous operational unit is closed by the frozen standard distribution.
- Disturbance / variety regulated: SagaMind can safely execute action variety supplied by external agents/applications, but it does not itself absorb task/environment variety through a repeated autonomous decision/action/feedback loop.
- Decisive decision or feedback right: not established inside SagaMind; the caller chooses the goal, tool, arguments, compensation, invariants and speculative drafts.
- Decision owner: external agent/application/MCP client.
- Supporting / enforcement mechanisms: saga state machine, verifier, sandbox/tool registry, compensation, persistence, approval pause, speculative validation and memory retrieval.
- Closure path: no first-party goal/observation → autonomous action choice → environment effect → observation → subsequent autonomous action choice loop is reachable in the standard distribution.
- Why this is / is not agent-owned: REST/gRPC/MCP surfaces accept complete proposed actions from outside the boundary; the coordinator and verifier decide admissibility/execution safety, not what operational action advances the goal. The optional memory LLM only labels memory clusters and is not wired as an operating actor.
- Evidence: [`src/main.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/main.py); [`src/grpc_server.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/grpc_server.py); [`sdk/mcp_server.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/sdk/mcp_server.py); [`src/orchestrator/coordinator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/coordinator.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: downstream autonomous agents can use SagaMind as their transaction/memory substrate. Such a composed system is a separate system-in-focus and must be assessed on its own evidence.

### Absence scope

- Surfaces inspected: REST API, gRPC gateway, coordinator, sandbox/tool registry, state lifecycle, speculative orchestrator, memory consolidation, SDK client and MCP server.
- Plausible first-party paths checked: saga goal lifecycle, step execution, speculative drafts, optional LLM memory labelling, MCP integration and startup recovery.
- Why no material first-party path remains: every action-bearing path either receives the substantive decision from an external caller, deterministically validates/executes it, or performs support processing without a returned autonomous operating decision loop.

## S2 — Coordination

- State: —
- Function: no S2 function is established because the reviewed boundary does not establish multiple autonomous S1 operational units whose concrete interference is regulated.
- Disturbance / variety regulated: no qualifying inter-S1 disturbance at the declared recursion.
- Decisive decision or feedback right: not established.
- Decision owner: none established inside the reviewed boundary.
- Supporting / enforcement mechanisms: sequential saga commits, compensations, sandbox/path isolation, tenant scoping and parallel speculative validation.
- Closure path: no distinct autonomous S1 units → concrete inter-S1 disturbance → attenuation decision → changed subsequent S1 behavior loop is established.
- Why this is / is not agent-owned: transaction ordering and rollback regulate consistency of externally submitted actions, while speculative drafts are alternative candidate actions rather than autonomous S1 units. Multi-agent product positioning does not supply missing operational ownership.
- Evidence: [`src/orchestrator/coordinator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/coordinator.py); [`src/speculative/orchestrator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/speculative/orchestrator.py); [`src/orchestrator/sandbox.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/sandbox.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: multiple external agents could share SagaMind and experience transaction/resource interference, but that composed deployment is not packaged here as first-party autonomous S1 plurality with a function-specific coordination owner.

### Absence scope

- Surfaces inspected: saga sequencing, compensation, tenant scoping, speculative parallel validation and sandbox isolation.
- Plausible first-party paths checked: transaction ordering, multiple saga steps, speculative parallel drafts and multi-agent claims.
- Why no material first-party path remains: no first-party autonomous S1 units are present, and the inspected mechanisms regulate submitted actions/candidates rather than interaction-generated disturbance among autonomous operating units.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established over autonomous S1 operations.
- Disturbance / variety regulated: transaction failure, approval pauses, recovery and compensation are regulated, but not as whole-system current management of autonomous operational commitments/resources/priorities.
- Decisive decision or feedback right: SagaMind deterministically accepts/rejects supplied steps and rolls back failed transactions; human callers may approve/reject flagged steps. No first-party actor owns whole-system current prioritization of autonomous operations.
- Decision owner: external caller for substantive commitments and human approval; deterministic runtime for transaction enforcement.
- Supporting / enforcement mechanisms: `active_sagas`, status snapshots, approval pause/resume, compensation, dead-letter escalation, crash recovery and bounded retention.
- Closure path: no whole-system autonomous-S1 view → current commitment/resource/priority decision → changed autonomous S1 behavior loop is established.
- Why this is / is not agent-owned: the coordinator is a strong transaction state machine, but it enforces the caller-supplied sequence rather than deciding what the organization should do now. Human approval is a local step gate, not evidence of an established S3 function without autonomous S1 operations.
- Evidence: [`src/orchestrator/coordinator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/coordinator.py); [`src/main.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/main.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: these mechanisms can become S3 support inside a larger agent organization, but generic transaction enforcement does not itself close organizational current control at this boundary.

### Absence scope

- Surfaces inspected: saga status, active-saga registry, approval/reject paths, rollback, dead-letter handling, startup recovery and retention controls.
- Plausible first-party paths checked: coordinator naming, whole-saga status view, human approval, rollback/recovery and dead-letter escalation.
- Why no material first-party path remains: the runtime has current transaction state but no first-party decision owner choosing or revising current organizational commitments/resources/priorities for autonomous S1 units.

## S3* — Complementary audit

- State: —
- Function: no materially independent organizational audit path is established for claims made through an autonomous S1 reporting path.
- Disturbance / variety regulated: the Z3 verifier detects violations of caller-supplied invariants before action execution, but there is no qualifying S1 claim/audit relationship at this boundary.
- Decisive decision or feedback right: deterministic satisfiability/refutation of supplied invariants; no independent audit actor owns challenge criteria or investigative judgment.
- Decision owner: caller supplies the invariant; SagaMind/Z3 deterministically enforces it.
- Supporting / enforcement mechanisms: Z3 verifier, semantic fallback, path containment, tool schema validation, transaction failure/rollback and logs/history.
- Closure path: no ordinary autonomous S1 reporting path → complementary evidence acquisition → independent audit judgment → corrective return into S3/S1 loop is established.
- Why this is / is not agent-owned: verification is real and direct, but its claim boundary is an invariant supplied with the proposed action and its judgment is deterministic. It is a safety gate on external decisions, not a sufficiently independent organizational audit path over autonomous operations.
- Evidence: [`src/verifier/z3_prover.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/verifier/z3_prover.py); [`src/orchestrator/coordinator.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/coordinator.py); [`src/orchestrator/sandbox.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/sandbox.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: a composed harness could use SagaMind's verifier as an S3* evidence mechanism if it separately establishes the required ordinary reporting path, independence boundary, audit judgment and corrective return.

### Absence scope

- Surfaces inspected: Z3 verification, semantic fallback, sandbox/path enforcement, transaction history/logging, rollback and speculative validation.
- Plausible first-party paths checked: formal verification, rollback after failed verification, transaction history and speculative draft validation.
- Why no material first-party path remains: the verifier checks caller-authored constraints deterministically and no autonomous S1/S3 reporting-and-correction loop exists for it to audit independently.

## S4 — Intelligence / adaptation

- State: —
- Function: no environment-facing prospective adaptation function returns a generated adaptation option into current organizational capability.
- Disturbance / variety regulated: memory volume/relevance and semantic clustering are managed, but not as future-environment variety translated into an organizational adaptation decision.
- Decisive decision or feedback right: no first-party actor selects a prospective adaptation to operating capability.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Ebbinghaus decay/retrieval, scheduled/manual consolidation, clustering, semantic graph projection, optional cluster labelling and memory query retrieval.
- Closure path: no external/future distinction → generated adaptation option → decision → changed current capability/S3 operation loop is established.
- Why this is / is not agent-owned: the sleep cycle summarizes past episodic memories; even optional LLM cluster labels are written as semantic memory relationships. The frozen runtime does not use those labels to autonomously redesign tools, policies, strategies or operating structure.
- Evidence: [`src/memory/consolidation.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/memory/consolidation.py); [`src/main.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/main.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: memory support can inform an external agent's adaptation, but external use of retrieved/consolidated memory does not donate S4 ownership to SagaMind.

### Absence scope

- Surfaces inspected: memory decay, active retrieval, scheduled/manual consolidation, semantic graph projection and optional LLM cluster labelling.
- Plausible first-party paths checked: "sleep cycle" consolidation, semantic concept discovery, memory retrieval and LLM-backed cluster summarization.
- Why no material first-party path remains: these paths transform/store past experience but do not model future external conditions, generate organizational adaptation options and return a selected change into first-party operating capability.

## S5 — Policy / identity

- State: —
- Function: no system-identity or ultimate-policy decision function is established.
- Disturbance / variety regulated: API authentication, tenant boundaries, tool allow-lists, invariants and sandbox restrictions constrain execution but do not resolve identity/ultimate-policy questions for an autonomous organization.
- Decisive decision or feedback right: policy/configuration is supplied by operators/integrators; no first-party ultimate-policy actor is present.
- Decision owner: external operator/deployer.
- Supporting / enforcement mechanisms: API keys, tenant binding, tool registry, schema validation, Z3 invariants, path jail, environment configuration and approval flags.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority decision → return into operation loop is established.
- Why this is / is not agent-owned: SagaMind enforces configured safety boundaries but does not decide its organizational identity, purpose or governing policy. Generic configuration and approval are enforcement/support mechanisms, not S5 closure.
- Evidence: [`src/main.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/main.py); [`src/orchestrator/sandbox.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/orchestrator/sandbox.py); [`src/verifier/z3_prover.py`](https://github.com/BlurredBox/SagaMind/blob/647fdcfd6b2c8def3775a3a2068aa27223bc1066/src/verifier/z3_prover.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: parent organizations may impose meaningful S5 policy through SagaMind's controls, but that authority belongs to the parent system unless a first-party SagaMind identity/policy loop is established.

### Absence scope

- Surfaces inspected: API auth/tenant controls, tool registry, verifier/invariants, sandbox restrictions, approval flags, configuration and documented product identity.
- Plausible first-party paths checked: human approval, safety invariants, tool policy, API authorization and product-level mission statements.
- Why no material first-party path remains: the inspected paths enforce externally configured constraints and do not provide a legitimate first-party ultimate authority whose identity/policy decisions return into autonomous operation.

## Assessment summary

SagaMind is a substantial transaction-safety, verification, rollback and memory substrate for agentic systems, but the frozen standard distribution does not package the autonomous operational decision/action/feedback loop required to establish S1 at the declared boundary. Its REST, gRPC and MCP surfaces receive substantive action decisions from external agents/applications; first-party components then validate, execute, compensate, persist, retrieve or consolidate them. Under Profile 0.2.4 / Methodology 0.3.6, those support/control mechanisms cannot be promoted into S2-S5 organizational ownership without a qualifying S1 organization and function-specific closure.

Proposed canonical outcome: `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
