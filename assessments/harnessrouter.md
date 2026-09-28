---
harness_id: harnessrouter
project_name: HarnessRouter
repository: https://github.com/HarnessRouter/harnessrouter
review_ref: 9ae33e77a92f240853e6d67a374c545d736c0f2d
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HarnessRouter

## Review boundary

- System in focus: the first-party HarnessRouter Community Edition control/data plane at frozen revision `9ae33e77a92f240853e6d67a374c545d736c0f2d`, including Gateway, Runner, Console-facing lifecycle APIs, Unified Harness Protocol implementation, session/workspace isolation, provider/connection routing, built-in/custom harness configuration, MCP/skill/plugin materialization, tracing, cancellation and backend adapters/drivers.
- Purpose and identity: normalize heterogeneous existing agent harnesses behind one Responses-compatible/UHP lifecycle API so callers can start/continue/cancel tasks, switch harness backends, preserve sessions/files and configure reusable instructions/tools/skills without implementing each upstream harness integration separately.
- Relevant environment: callers selecting a harness/model; external agent harness runtimes and CLIs such as Codex, Claude Code, Hermes, Pi, DeepSeek Harness, OpenCode, Qwen, Gemini CLI, Cline, Oh My Pi, goose, Kimi, Aider and OpenHands; model providers; MCP servers; target workspaces/files; provider credentials; human Console users.
- Standard-distribution boundary: first-party Gateway/Runner/UI/protocol code, backend command builders/adapters, session/workspace/control-store machinery and bundled configuration at the frozen revision. The autonomous planning/tool loops implemented by the invoked upstream harnesses/agent servers remain adjacent runtimes. Model/provider inference likewise remains environment. A backend adapter does not inherit S1 ownership simply because HarnessRouter installs, configures, launches, polls or normalizes that external harness.
- Credited operating / distribution surfaces: `gateway/app.py`, backing/control/media planes, `runner/server.py`, first-party backend drivers/bridges including `openhands_driver.py` and Aider/MCP bridges, Docker/entrypoint installation, custom-harness configuration, UHP schemas/conformance, workspace/session/cancellation/checkpoint/tracing paths and connection policy/fallback machinery.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/conformance-development workflows, benchmark/report generation and docs-only examples. Upstream harness internals, their planners/reviewers/tool policies, provider-side model behavior and external MCP decisions are not credited as HarnessRouter-owned organizational functions.
- First-party operating / deployment modes considered: self-hosted Community Edition; built-in harness runs; custom harness pinned to a base harness with instructions/tools/skills/plugins; OpenAI Responses-compatible API and UHP session continuation; provider/model mapping and fallback chains; cancellation/recovery; supported OpenHands agent-server backend and CLI-based backends.
- Recursion level: one HarnessRouter service/control plane mediating one requested harness task/session. The selected upstream agent harness can itself be an autonomous system at a lower/adjacent recursion, but its task-level autonomy is not inherited by the router service.
- Reviewed revision: `9ae33e77a92f240853e6d67a374c545d736c0f2d`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HarnessRouter is a substantial first-party compatibility and lifecycle layer around existing agent harnesses. The Gateway receives a Responses/UHP request, reads the caller-selected `metadata.harness_id` (or the harness named by a route/header), resolves a custom harness's fixed base backend, model policy and provider connection, materializes instructions/MCP/skills/plugins, and sends a normalized `/turn` request to the Runner. The Runner then constructs backend-specific configuration/command lines or server requests and starts the selected external harness runtime.

The autonomy boundary is explicit in code. `runner/server.py` dispatches turns to Codex, Claude Code, Hermes, Pi, DeepSeek Harness, OpenCode, Qwen, Kimi, Aider, OpenHands, Gemini, Cline, goose and related runtimes. For ordinary CLI-backed modes, HarnessRouter builds the command and launches the upstream executable; for OpenHands it drives the maintained upstream agent-server/SDK interface. HarnessRouter parses/normalizes emitted events, tracks session IDs, retries/fallbacks connections, collects files and can cancel processes, but the external harness decides the substantive model/tool sequence inside the task.

The product's “router” naming does not imply an autonomous task-aware router. With a harness configured, the backend is pinned to that harness's base. The public API guide says `metadata.harness_id` selects which harness runs a task. When no harness is supplied, `_route_backend` uses deterministic model-name/backend hints. Provider connection chains are likewise ordered compatibility/failure fallback rather than a model actor comparing task semantics or organizational consequences. Benchmark cost/latency material is descriptive; no first-party task-aware harness-selection loop was found in the frozen runtime.

Counterfactually, remove Codex/Claude/Hermes/OpenHands/etc. while keeping Gateway, Runner, UHP, sessions, workspaces, provider routing and custom-harness configuration: HarnessRouter can still validate requests, select/configure an adapter, persist/route state and enforce lifecycle controls, but no autonomous task actor remains to interpret an open-ended request, choose tools/actions from observations and continue until completion. The task-level decision loop therefore closes in the adjacent upstream harness.

Primary evidence:

- [`README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/README.md) — explicit positioning as a unified interface that turns existing harnesses into pluggable agent backends; caller-selected harness/model API and Community Edition architecture.
- [`docs/self-hosting-guide.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/docs/self-hosting-guide.md) — installed upstream harnesses and `metadata.harness_id` as the mechanism selecting the harness that executes a task.
- [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py) — request/session lifecycle, harness/base-backend resolution, model/provider policy and fallback, plugin/skill/MCP materialization, normalized turn dispatch/polling/cancellation.
- [`runner/server.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/server.py) — backend-specific command construction, external process/server launch, event normalization, resume/workspace handling and turn lifecycle.
- [`runner/openhands_driver.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/openhands_driver.py) — adapter/driver around the maintained OpenHands agent-server rather than an independent HarnessRouter planner/tool loop.
- [`protocol/README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/protocol/README.md) — UHP lifecycle/API contract for interchangeable harness implementations.

## Operational model

A caller chooses a built-in/custom harness and model, or supplies a direct backend hint in an ad-hoc case. Gateway resolves the harness's fixed base backend, provider/model eligibility, connection chain, persistent instructions, tools, skills and plugins. It creates/continues a durable session, enforces single-live-turn/idempotency/cancellation rules and asks Runner to start a turn.

Runner prepares the session workspace and backend-specific configuration, then launches the upstream agent runtime. The upstream harness performs its own model/tool/observation loop. Runner streams/normalizes upstream text/tool/result/session events; Gateway persists traces and usage, exposes them through Responses/UHP, collects produced files, handles retries across provider connections where allowed and can stop the running process. These are strong execution-governance mechanisms, but the substantive autonomous decision loop remains inside the selected harness.

## S1 — Operations

- State: —
- Function: no first-party HarnessRouter operational unit owns the open-ended task-level model/tool/action/feedback loop.
- Disturbance / variety regulated: user task ambiguity, repository/workspace state, tool results, coding/research choices and iterative task failures are substantively handled by the selected upstream harness runtime.
- Decisive decision or feedback right: interpret task observations, choose the next substantive tool/action or plan, evaluate returned evidence and continue/revise toward task completion.
- Decision owner: selected external harness/agent runtime such as Codex, Claude Code, Hermes, Pi, OpenHands or another supported backend.
- Supporting / enforcement mechanisms: Responses/UHP request normalization, session/workspace provisioning, backend command/config construction, provider credential brokering, MCP/skill/plugin materialization, timeout/max-step controls, trace/event normalization, cancellation and produced-file collection.
- Closure path: caller selects harness/task → Gateway resolves config/backend → Runner launches selected upstream harness → upstream harness interprets task and performs model/tool turns → Runner/Gateway normalize/persist events/results → continuation request is handed back to the same/upstream harness. The autonomous operational loop closes in that adjacent harness.
- Why this is / is not agent-owned: first-party code implements transport, lifecycle and adapter behavior but not a generic autonomous planner/tool loop of its own. Even the OpenHands mode explicitly drives the vendor-maintained agent-server; CLI modes invoke separately implemented harness executables.
- Evidence: [`README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/README.md); [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py); [`runner/server.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/server.py); [`runner/openhands_driver.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/openhands_driver.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: a deployed HarnessRouter task absolutely contains autonomous agent behavior because it deliberately runs an upstream harness. This finding is about repository-relative ownership of that behavior, not whether the composed deployment is agentic.

### Absence scope

- Surfaces inspected: Responses/UHP entry point, harness/base-backend resolution, Runner turn dispatch, all backend builders/drivers, custom-harness configuration, provider/model routing, session continuation and cancellation.
- Plausible first-party paths checked: Gateway as S1; Runner turn loop as S1; OpenHands driver as first-party S1; custom harness instructions/tools as S1; model-family `_route_backend` as S1.
- Why no material first-party path remains: every substantive task execution path delegates the autonomous actor loop to an upstream harness/agent server; first-party code selects/configures/observes/enforces the dependency but does not replace its task-level decision function.

## S2 — Coordination

- State: —
- Function: no qualifying first-party coordination function among multiple first-party autonomous S1 units is established at the declared recursion.
- Disturbance / variety regulated: session concurrency, duplicate requests, backend/provider conflicts and workspace isolation are regulated, but these are request/runtime consistency problems rather than interaction-generated disturbance among first-party autonomous operational units.
- Decisive decision or feedback right: deterministic admission/idempotency/lease/connection rules decide whether a turn may run and which compatible provider connection is tried; the caller/harness determines substantive task organization.
- Decision owner: deterministic Gateway/Runner control code.
- Supporting / enforcement mechanisms: single-live-turn session lease, idempotency keys, session-user/workspace isolation, provider connection fallback, backend compatibility tables and cancellation fencing.
- Closure path: requests/turns are admitted or refused and external harness processes are isolated; no distinct first-party S1 units → concrete inter-S1 operational disturbance → coordination decision → changed first-party S1 behavior loop is established.
- Why this is / is not agent-owned: concurrency gating and provider fallback are real controls but do not constitute VSM S2 at this recursion without first-party autonomous S1 plurality and a concrete interaction disturbance between those units.
- Evidence: [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py); [`runner/server.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/server.py).
- Basis: structural absence at declared ownership boundary
- Confidence: high
- Caveats: HarnessRouter can mediate many independent upstream agent sessions; at a broader product-level organization those agents may become S1 units, but the frozen router itself does not define or own that higher organizational composition.

### Absence scope

- Surfaces inspected: concurrency limits, session leases, idempotency, per-session OS users/workspaces, provider chains, backend compatibility and cancellation/recovery.
- Plausible first-party paths checked: per-tenant concurrency as S2; workspace isolation; provider fallback chain; multiple simultaneous harness tasks; UHP session ordering.
- Why no material first-party path remains: the inspected controls regulate infrastructure/request consistency around adjacent harnesses rather than a function-specific coordination relation among first-party autonomous S1 operational units.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous whole-system current-control actor decides organizational commitments, priorities or interventions over first-party operations.
- Disturbance / variety regulated: live turn status, leases, retries, provider refusal, timeout, cancellation, hydration/checkpoint failure and current usage are monitored/enforced.
- Decisive decision or feedback right: fixed runtime policies can fail/refuse/cancel/retry a turn or try the next configured provider connection; harness/task priority and substantive intervention remain with caller/upstream agent/product logic.
- Decision owner: deterministic Gateway/Runner lifecycle code and external caller/operator.
- Supporting / enforcement mechanisms: trace/session state, heartbeat/lease renewal, connection chain, timeout/max-step policy, cancellation, checkpoint hydration and durable control store.
- Closure path: runtime event/failure → deterministic lifecycle rule changes request/process state or tries compatible connection → upstream harness continues or caller receives terminal status. No first-party organizational manager interprets a whole-current operational view and chooses a substantive current-control correction.
- Why this is / is not agent-owned: the service is a capable control plane, but its choices are lifecycle/fallback policy around adjacent agents. “Router” and “Gateway” naming do not create autonomous S3 ownership.
- Evidence: [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py); [`runner/server.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/runner/server.py).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: provider fallback and cancellation are important present-time regulation. They remain deterministic execution controls rather than a qualifying organizational S3 actor/function at this repository-relative boundary.

### Absence scope

- Surfaces inspected: turn/session state machine, connection fallback, hydration/recovery, timeouts/max steps, cancellation, traces/usage and concurrency controls.
- Plausible first-party paths checked: Gateway as manager; fallback chain as current-control decision; cancellation/timeout as S3; trace observability; custom-harness runtime policy.
- Why no material first-party path remains: first-party code has current execution state but no autonomous organizational decision owner revising substantive commitments/resources/priorities for first-party S1 operations.

## S3* — Complementary audit

- State: —
- Function: no materially independent first-party organizational audit path evaluates a substantive completion claim from a first-party S1 unit and returns a corrective judgment.
- Disturbance / variety regulated: protocol/conformance tests, harness verification, event normalization and structured failure handling can detect integration defects, but they do not form a runtime audit of an autonomous first-party worker claim.
- Decisive decision or feedback right: production runtime accepts/normalizes the upstream harness's emitted tool/result state subject to deterministic protocol checks; substantive correctness review belongs to the upstream harness/custom tools/caller.
- Decision owner: none established as an independent first-party audit actor.
- Supporting / enforcement mechanisms: UHP conformance suite, backend verification/support matrices, traces, structured errors, disabled-tool policy and protocol validation.
- Closure path: no ordinary first-party S1 reporting path → complementary independent evidence acquisition → audit judgment → corrective return loop is established in production runtime.
- Why this is / is not agent-owned: conformance/verification infrastructure primarily validates adapter/protocol behavior and repository integrations. It does not independently inspect whether an autonomous task result actually satisfies the user's operational goal and then alter first-party S1 behavior.
- Evidence: [`protocol/conformance/README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/protocol/conformance/README.md); [`docs/harness-verification.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/docs/harness-verification.md); [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py).
- Basis: structural absence
- Confidence: high
- Caveats: an upstream harness or custom harness may itself implement reviewer/audit agents. That audit belongs to that composed/upstream system unless HarnessRouter supplies and owns the independent judgment path.

### Absence scope

- Surfaces inspected: conformance suite, harness verification docs/matrices, runtime traces, error normalization, disabled-tool enforcement and backend tests/drivers.
- Plausible first-party paths checked: UHP conformance as S3*; harness verification as audit; trace normalization; backend support matrix; custom-harness reviewer tooling.
- Why no material first-party path remains: these surfaces verify protocol/integration behavior or expose evidence, not an independent runtime judgment over substantive first-party operational claims with corrective closure.

## S4 — Intelligence / adaptation

- State: —
- Function: no first-party prospective environment-facing intelligence loop autonomously chooses how the organization should adapt its harness/backend capability.
- Disturbance / variety regulated: provider/model compatibility, benchmark cost/latency differences, media capability availability and backend support drift are represented in catalog/policy/configuration.
- Decisive decision or feedback right: callers/operators choose harnesses, model mappings, connection order and media policy; deterministic code applies those choices or compatibility rules.
- Decision owner: external user/operator/product configuration; no first-party autonomous S4 actor.
- Supporting / enforcement mechanisms: support matrix/benchmarks, model/provider catalogs, connection policy/fallback, media capability catalog/policy, harness CRUD/configuration and release/upgrade machinery.
- Closure path: no first-party external/future sensing → autonomous adaptation-option generation → selection → returned change into current harness capability is established. Benchmark/support information can inform humans/products, but runtime does not task-semantically choose a different harness based on those observations.
- Why this is / is not agent-owned: “Optimize cost and latency” in product positioning describes the choice enabled by a unified interface; the public API still has the caller select `metadata.harness_id`. Provider/media fallback is configured/deterministic service routing rather than organizational prospective intelligence.
- Evidence: [`README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/README.md); [`docs/self-hosting-guide.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/docs/self-hosting-guide.md); [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: an external product could build a learned/task-aware harness selector atop UHP and HarnessRouter benchmarks. That would be a separate S4-bearing composed system.

### Absence scope

- Surfaces inspected: benchmark/support data, provider/model mappings, `_route_backend`, harness/base resolution, connection chains, media policies, custom-harness settings and upgrade/release mechanisms.
- Plausible first-party paths checked: cost/latency benchmark as S4; automatic harness selection; provider fallback; model-family routing; media-model policy; compatibility-driven migration.
- Why no material first-party path remains: harness choice is caller/configuration owned and remaining runtime routing is deterministic compatibility/failure handling; no autonomous prospective adaptation decision returns into organizational capability.

## S5 — Policy / identity

- State: —
- Function: no first-party ultimate-policy/identity decision authority for an autonomous organization is established.
- Disturbance / variety regulated: harness instructions, disabled tools, skills/plugins, model permissions, provider policy, API authorization and lifecycle limits constrain how an upstream harness may run.
- Decisive decision or feedback right: humans/product callers/configuration owners define custom harness instructions/base/model/tools and service policy; HarnessRouter enforces the stored/configured result.
- Decision owner: external owner/operator/product caller, not a first-party organizational S5 actor.
- Supporting / enforcement mechanisms: custom harness configuration, `agent_doc`, disabled-tool policy, model permission/fallback, auth/tenant boundaries, UHP governance for the interoperability standard and service configuration.
- Closure path: external owner chooses harness identity/configuration/policy → first-party storage/materialization/enforcement passes it into the selected upstream harness → upstream agent operates under those constraints. No first-party ultimate-policy decision loop resolves organizational identity/purpose and returns its own decision into autonomous first-party operation.
- Why this is / is not agent-owned: protocol governance concerns the public UHP standard/repository process, not runtime S5 for a task organization. Custom-harness identity is user-defined configuration around an external base harness.
- Evidence: [`README.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/README.md); [`gateway/app.py`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/gateway/app.py); [`protocol/GOVERNANCE.md`](https://github.com/HarnessRouter/harnessrouter/blob/9ae33e77a92f240853e6d67a374c545d736c0f2d/protocol/GOVERNANCE.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a parent product can encode genuine S5 policy in a custom harness's instructions/tool/model restrictions. That authority belongs to the parent product unless a separate first-party HarnessRouter ultimate-policy loop is established.

### Absence scope

- Surfaces inspected: custom harness CRUD/configuration, agent instructions, tool/skill/plugin policy, model permission, auth/tenant/service configuration and UHP repository governance.
- Plausible first-party paths checked: custom harness identity as S5; disabled tools/model permissions; UHP governance; admin/operator controls; base-harness immutability.
- Why no material first-party path remains: first-party code stores/enforces policy selected outside the task organization and protocol governance governs the interoperability specification, not an autonomous first-party organizational identity/ultimate-policy decision loop.

## Assessment summary

HarnessRouter is a sophisticated execution/lifecycle interoperability layer, but at the frozen repository-relative boundary it deliberately turns separately implemented agent harnesses into pluggable backends rather than implementing its own task-level autonomous agent loop. Gateway and Runner own request normalization, durable sessions/workspaces, provider compatibility/fallback, instructions/tools/skills materialization, tracing and cancellation; Codex/Claude/Hermes/OpenHands/etc. own the substantive model/tool reasoning. Caller-selected harness identity and deterministic routing likewise do not establish an autonomous meta-router. Under Profile 0.2.4 / Methodology 0.3.6, the first-party boundary therefore does not establish S1 and the surrounding control mechanisms are not promoted into S2-S5 organizational ownership.

Proposed canonical outcome: `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
