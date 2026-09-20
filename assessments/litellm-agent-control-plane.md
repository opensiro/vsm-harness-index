---
harness_id: litellm-agent-control-plane
project_name: LiteLLM Agent Control Plane
repository: https://github.com/LiteLLM-Labs/litellm-agent-control-plane
review_ref: 53bfd20e2fec51fc8f665fb614512c6b138367da
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LiteLLM Agent Control Plane

## Review boundary

- System in focus: the first-party LiteLLM Agent Control Plane / Agent Platform (`lite` service plus its Postgres-backed state, normalized runtime SDK/adapters, agent/session APIs, scheduler, memory/access/channel surfaces and dashboard/API) at pinned revision `53bfd20e2fec51fc8f665fb614512c6b138367da`.
- Purpose and identity: provide one control-plane/UI/API layer for creating, addressing, scheduling, persisting and observing agents that execute on separately registered agent runtimes.
- Relevant environment: users/developers, registered Claude/Cursor/Gemini/OpenCode/OpenClaw/Deep Agents/Hermes and other agent runtimes, model providers, MCP servers, communication channels and application requests.
- Standard-distribution boundary: the `lite` service, database schema/state, runtime registry/adapters, normalized managed-agent API, session/routine/memory/access/channel machinery and dashboard are first-party. Registered agent runtimes and their autonomous decision/action loops remain separate upstream services. Bundled `templates/*` are inspected as adjacent wrapper/demo/runtime-integration surfaces and are not used to transfer ownership of the wrapped runtime's agent loop into the control-plane boundary.
- Credited operating / distribution surfaces: root Docker image and `lite` service; REST/UI/gateway/MCP/channel endpoints; Postgres-backed agent/session/runtime/schedule/memory/settings state; normalized `RuntimeAdapter` SDK; first-party deterministic routine scheduler; runtime registration and event streaming.
- Adjacent first-party surfaces excluded from ownership: `templates/opencode`, `templates/deepagents`, `templates/hermes`, `templates/openclaw` and similar wrapper/template services where the repository explicitly says they wrap a separate AI agent runtime; optional Compose runtime profiles used for local development/demos; repository CI/tests/contributor tooling. Their integration evidence informs the boundary but does not make OpenCode, Deep Agents, Hermes or OpenClaw organizational decisions first-party LiteLLM ACP decisions.
- First-party operating / deployment modes considered: base `lite + Postgres` deployment; dashboard/API/Slack/channel access; hosted runtime registration; optional local template runtime profiles; scheduled routines and persistent sessions/memory.
- Recursion level: the LiteLLM Agent Control Plane itself as the system in focus. A separately registered runtime may host one or more viable agent systems, but those systems are downstream/external systems and require their own repository-relative assessments.
- Reviewed revision: `53bfd20e2fec51fc8f665fb614512c6b138367da`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

LiteLLM Agent Control Plane is explicitly a control plane layered above agent runtimes. Its README and introduction say it "sits on top of any runtime" and manages a unified API, access, persistent sessions, CRON schedules and memory. The architecture document narrows the deployed core further: one `lite` process plus Postgres, while everything requiring a model, MCP server or agent runtime is an upstream call. Postgres persists agents, sessions, runtime harnesses, schedules, memory and settings; the `lite` process exposes the UI/API/gateway/channel surfaces and streams runtime events back to callers.

The normalized managed-agent SDK preserves that separation. `RuntimeAdapter` implementations map `agents.create`, `sessions.create`, `send_events` and `stream_events` to provider/runtime-specific APIs. The caller selects `lap_agent_runtime`; first-party code translates requests and responses while the selected runtime performs the actual agent execution. The SDK contract documents concrete mappings to Anthropic Managed Agents, Cursor and Gemini Antigravity rather than implementing a model/tool decision loop in the control plane.

The repository also ships optional runtime templates. Those do not close the boundary gap. `templates/README.md` describes each template as a self-contained server that **wraps an AI agent runtime** behind the Anthropic Managed Agents API. The OpenCode template makes the relation explicit: `LAP -> opencode-agent-server -> opencode serve`. Likewise Compose starts optional OpenCode, Deep Agents, Hermes and OpenClaw services and then registers their API bases with LAP. The architecture document describes these template runtimes as optional local services for development/demos. They therefore demonstrate runtime interoperability, not a first-party autonomous operational owner in the control-plane system itself.

The first-party routine scheduler is deterministic. It parses CRON expressions, polls active routines, determines due timestamps and invokes the routine trigger. Persistent memory likewise preserves agent context across sessions. These mechanisms are meaningful execution/control infrastructure, but neither creates the missing autonomous S1 decision/action loop.

Primary evidence:

- [`readme.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/readme.md) — explicit product boundary above external runtimes and managed surfaces.
- [`docs/introduction.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/introduction.mdx) — "sits on top of any runtime" and supported control-plane features/channels.
- [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx) — `lite + Postgres` core, upstream runtime calls and optional template-runtime boundary.
- [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx) — normalized runtime adapter contract and provider-specific execution mappings.
- [`compose.yaml`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/compose.yaml) — optional runtime services registered into LAP through their API bases.
- [`templates/README.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/templates/README.md) — templates explicitly wrap separate AI agent runtimes.
- [`templates/opencode/README.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/templates/opencode/README.md) — wrapper topology `LAP -> opencode-agent-server -> opencode serve`.
- [`src/http/managed_agents/routines/scheduler.rs`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/src/http/managed_agents/routines/scheduler.rs) — deterministic CRON scheduling/trigger machinery.

## Operational model

A user creates/configures an agent and selects or registers a runtime. LiteLLM ACP persists the agent/session configuration, translates normalized API operations into the runtime's native protocol, sends prompts/events to that runtime and streams normalized results back. Scheduled routines can initiate the same path deterministically at configured times, and memory/state can persist between calls.

The substantive autonomous operational decision/action loop—interpreting the task, selecting model/tool actions, observing tool results and deciding subsequent actions—runs in the selected upstream agent runtime. Removing OpenCode/Deep Agents/Hermes/Claude/Cursor/Gemini or an equivalent registered runtime while leaving `lite`, Postgres, adapters, scheduler and memory intact leaves a control plane that can store and route agent definitions but does not itself perform autonomous agent work. This counterfactual is decisive for S1 ownership.

Methodology 0.3.5 states that included autonomous harnesses should normally establish `S1=A`, and when the standard distribution does not establish an autonomous operational decision/action loop the Index exclusion state should be used rather than forcing an S1 classification. The repository's own architecture makes that condition explicit here. The proposed outcome is therefore canonical exclusion as `excluded-no-agentic-vsm`, not an included assessment with `S1=C`.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop is established in the declared LiteLLM ACP control-plane boundary.
- Disturbance / variety regulated: the control plane regulates runtime/API heterogeneity, persistence, access, scheduling and transport, but substantive task/environment variety is regulated by the selected upstream agent runtime.
- Decisive decision or feedback right: the task-level choice of next model/tool/action belongs to the registered runtime's agent loop, not to `lite`, its adapters, scheduler or database.
- Decision owner: no first-party LiteLLM ACP autonomous S1 owner established; the relevant owner is external to the assessed boundary.
- Supporting / enforcement mechanisms: agent/session CRUD, normalized runtime adapters, runtime registry, Postgres persistence, scheduling, memory, MCP/gateway/channel transport and event streaming.
- Closure path: LiteLLM ACP request/configuration → selected external runtime → external runtime's autonomous loop → normalized events/results back through ACP. The decisive operational loop closes outside the system in focus.
- Why this is / is not agent-owned: first-party code transports/configures/invokes a separately registered autonomous runtime but does not own the runtime's model/tool decision cycle. Bundled templates explicitly wrap those runtimes rather than replacing them.
- Evidence: [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx), [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx), [`templates/README.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/templates/README.md), [`templates/opencode/README.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/templates/opencode/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: individual supported runtimes may independently qualify as autonomous harnesses and require separate assessment. This finding is about LiteLLM ACP at the declared standard-distribution boundary, not those projects.

### Absence scope

- Surfaces inspected: product README/introduction, architecture docs, normalized runtime SDK contract, Compose deployment, runtime template boundary, OpenCode wrapper topology, scheduler, session/runtime/memory surfaces.
- Plausible first-party paths checked: core `lite` process; SDK/runtime adapters; managed-agent/session APIs; scheduled routines; persistent memory; bundled runtime templates/profiles.
- Why no material first-party path remains: every operational execution path ultimately calls a separately registered/wrapped agent runtime; first-party ACP machinery remains control/transport/persistence/scheduling infrastructure when that external autonomous runtime is removed.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 coordination function is established at the declared ACP recursion because the boundary does not establish distinct first-party S1 operational units in the first place.
- Disturbance / variety regulated: no concrete first-party inter-S1 conflict/oscillation witness established.
- Decisive decision or feedback right: none established for an S2-specific attenuation relation.
- Decision owner: none established within the ACP boundary.
- Supporting / enforcement mechanisms: runtime registry, unified APIs, sessions, schedules, channels and shared database can route/manage multiple external agents but generic routing/shared state is not S2 by itself.
- Closure path: no qualifying first-party inter-S1 disturbance → attenuation → changed subsequent S1 behaviour loop established.
- Why this is / is not agent-owned: ACP can address multiple externally executed agents, but no first-party autonomous coordinator is shown owning an S2-specific decision over first-party S1 units.
- Evidence: [`readme.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/readme.md), [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx), [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: an external multi-agent runtime may implement S2 behind ACP; its coordination is not inherited by this repository assessment.

### Absence scope

- Surfaces inspected: agent/runtime/session CRUD and registry, schedules, persistent state, channel/API surfaces and runtime adapter contract.
- Plausible first-party paths checked: multi-runtime routing, shared session state, scheduled execution and management of multiple agent definitions.
- Why no material first-party path remains: these are generic control-plane/routing/persistence primitives and no evidence ties them to attenuation of a concrete conflict among distinct first-party operational S1 units with returned behavioural feedback.

## S3 — Inside-and-now control

- State: —
- Function: no VSM S3 function is credited at the declared ACP recursion because the control plane does not contain the first-party operational S1 population whose current commitments would be regulated.
- Disturbance / variety regulated: ACP manages current sessions/runtimes/schedules/access, but these lifecycle/configuration concerns do not establish whole-system operational current control over first-party S1 units.
- Decisive decision or feedback right: runtime selection, schedule definitions and operator CRUD are user/configuration choices; the scheduler deterministically enforces authored CRON policy.
- Decision owner: no autonomous first-party S3 owner established.
- Supporting / enforcement mechanisms: dashboard/API, runtime registry, session status/events, Postgres state, routine scheduler and access controls.
- Closure path: no qualifying whole-system current operational view → discretionary S3 decision → changed first-party S1 commitments loop established.
- Why this is / is not agent-owned: ACP exposes a control plane to humans/applications and deterministic services, but there is no first-party model-driven current-control actor over an internally owned operational organization.
- Evidence: [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx), [`src/http/managed_agents/routines/scheduler.rs`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/src/http/managed_agents/routines/scheduler.rs), [`readme.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/readme.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a human can administer current external agents through ACP, but generic operator control does not create an included autonomous-harness S3 when the underlying S1 is outside the system boundary.

### Absence scope

- Surfaces inspected: dashboard/API architecture, runtime/session state, CRON routine scheduler, memory/settings and access/channel surfaces.
- Plausible first-party paths checked: scheduler-triggered runs, operator agent/session management, runtime choice and current session event streaming.
- Why no material first-party path remains: scheduler/runtime lifecycle are deterministic or user-authored control-plane actions and no autonomous actor closes whole-system current regulation over first-party S1 operations.

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary audit of operational S1 reality with corrective return is established.
- Disturbance / variety regulated: no qualifying audit disturbance/path established.
- Decisive decision or feedback right: none established.
- Decision owner: none established within ACP.
- Supporting / enforcement mechanisms: logs/events, runtime status, API validation, access/security and persisted state provide observability/enforcement but not independent audit judgment.
- Closure path: no separate evidence path → independent audit verdict → corrective return into operation loop established.
- Why this is / is not agent-owned: normalized runtime events report what the external runtime emits; they do not constitute an independent challenger with complementary access.
- Evidence: [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx), [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: external runtimes may expose their own reviewers/evaluators; those are separate organizational evidence.

### Absence scope

- Surfaces inspected: event streaming/normalization, session state, API validation, access/security, runtime registry and persistence.
- Plausible first-party paths checked: runtime event observation, logs/telemetry, API validation, memory/history and operator inspection.
- Why no material first-party path remains: no distinct first-party auditor uses a materially complementary evidence path to judge an operational claim and return findings into corrective operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental intelligence loop that selects and returns reusable capability adaptations is established.
- Disturbance / variety regulated: no qualifying future/environment adaptation disturbance established.
- Decisive decision or feedback right: none established.
- Decision owner: none established within ACP.
- Supporting / enforcement mechanisms: persistent memory, runtime catalog/registration, MCP integrations and model/runtime configurability preserve or expose context/capability options but do not choose future organizational adaptation.
- Closure path: no external/future distinction → adaptation option → selected capability change → subsequent operation path established.
- Why this is / is not agent-owned: memory is persistence and adding/selecting a runtime is operator/developer configuration; neither is an autonomous S4 adaptation loop.
- Evidence: [`readme.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/readme.md), [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx), [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: an upstream agent may learn/research/adapt; that does not establish ACP-owned S4.

### Absence scope

- Surfaces inspected: memory, runtime catalog/registry, model/runtime selection, MCP integration, scheduler and session persistence.
- Plausible first-party paths checked: cross-session memory, runtime extensibility, adding new adapters/templates and scheduled agent activity.
- Why no material first-party path remains: persistence and extensibility are configuration/construction mechanisms; no autonomous prospective sensing and adaptation-selection loop returns a new reusable ACP capability into current operation.

## S5 — Policy and identity

- State: —
- Function: no first-party identity or ultimate-policy decision loop is established for an autonomous viable organization at this boundary.
- Disturbance / variety regulated: access, credentials, runtime/model choice and settings constrain use but do not constitute an identity/ultimate-policy issue and closure.
- Decisive decision or feedback right: relevant settings are supplied by users/operators/developers; no first-party autonomous or qualifying parent S5 loop is established.
- Decision owner: none established for a VSM S5 closure within the assessed autonomous-harness target.
- Supporting / enforcement mechanisms: master/API keys, access controls, runtime credentials, agent system prompts, settings and runtime/model selection.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority → authoritative returned decision → governed autonomous organization loop established.
- Why this is / is not agent-owned: ACP stores and enforces configured policy/access choices but does not autonomously decide organizational identity; operator configuration alone is not S5.
- Evidence: [`readme.md`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/readme.md), [`docs/learn/architecture.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/learn/architecture.mdx), [`docs/engineering/sdk-api-contract.mdx`](https://github.com/LiteLLM-Labs/litellm-agent-control-plane/blob/53bfd20e2fec51fc8f665fb614512c6b138367da/docs/engineering/sdk-api-contract.mdx).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: this does not deny that an operator organization has policies; the Methodology requires a reconstructed runtime identity/ultimate-policy closure at the declared assessed boundary.

### Absence scope

- Surfaces inspected: access/credentials/settings, runtime/agent configuration, system prompts, model/runtime selection, scheduling and channel surfaces.
- Plausible first-party paths checked: master-key/operator authority, agent configuration, runtime permissions and persisted settings.
- Why no material first-party path remains: these paths configure/enforce how the control plane invokes external agent systems; none establishes the requisite identity/ultimate-policy closure for an autonomous organization owned by ACP.

## Distributed OSS parent arrangement

The upstream LiteLLM-Labs repository governance is outside the runtime system in focus and is not used to rescue the missing autonomous S1. Likewise, a self-hosting operator's administration of ACP is ordinary control-plane ownership unless a function-specific VSM parent loop is established over a qualifying autonomous organization. Because the inclusion boundary fails at S1, no parent-mode notation is published for this proposed exclusion.

## Self-hosted and non-human modes

Self-hosting `lite + Postgres` does not alter the ownership result: autonomous task execution still requires a registered external runtime. Optional local Compose profiles colocate those runtimes operationally but the repository architecture and template documentation preserve them as separate runtime services/wrappers. Co-deployment therefore does not transfer their agent-owned decisions into LiteLLM ACP itself.

## Recursion

LiteLLM ACP is a control-plane layer above separately viable agent runtimes. Each registered runtime or agent system can be assessed as its own system-in-focus at its own pinned repository revision. Collapsing ACP and all possible registered runtimes into one assessment would make the result runtime-dependent and violate the repository-relative evidence boundary.

## Variety and escalation

ACP usefully absorbs integration variety: runtime protocols are normalized, sessions and memory are persisted, scheduled calls are triggered, credentials/access are centralized and events are surfaced consistently. Those capabilities explain why the product is a control plane, but they do not themselves supply autonomous operational variety absorption. Operational judgment remains in the selected runtime; operator/developer decisions remain outside or above the control-plane mechanics.

## Evidence gaps

No evidence gap blocks the exclusion conclusion at the pinned revision. The product boundary, architecture, SDK adapter contract, Compose topology and template documentation consistently separate LAP from the autonomous runtime. A later revision that embeds a first-party autonomous decision/action loop directly into the standard control-plane distribution would require a new-ref reassessment; merely adding another runtime adapter or wrapper would not.
