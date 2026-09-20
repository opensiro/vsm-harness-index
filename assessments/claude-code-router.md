---
harness_id: claude-code-router
project_name: Claude Code Router
repository: https://github.com/musistudio/claude-code-router
review_ref: a034b0c51cdd1b5628bbff545821f5540d30c6c5
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

# Claude Code Router

## Review boundary

- System in focus: the first-party Claude Code Router (CCR) local gateway/control plane at pinned revision `a034b0c51cdd1b5628bbff545821f5540d30c6c5`, including provider/model routing, retries/fallbacks, credential pools, transforms/plugins, logs/health/status, managed Agent Config integrations, multi-instance control-plane surfaces, ToolHub/MCP transport and AgentClaw relay machinery.
- Purpose and identity: give external coding agents and compatible API clients one stable local endpoint and a management surface for providers, models, accounts, routing rules, tools, observability and remote relay.
- Relevant environment: Claude Code, Codex, OpenCode, Kilo, Pi, ZCode, WorkBuddy and other external coding agents/clients; model providers; local/remote tools and MCP servers; IM platforms; operator configuration; provider health/rate limits; requests and responses.
- Standard-distribution boundary: CCR's own gateway, routing/provider/storage services, desktop/CLI management UI, per-agent configuration adapters, bot-gateway/AgentClaw companion relay, ToolHub/MCP and multi-instance machinery are first-party. The autonomous coding-agent loops belonging to Claude Code, Codex, OpenCode, ZCode, WorkBuddy and similar clients remain adjacent systems even when CCR launches/configures/manages an app entry or relays its sessions.
- Credited operating / distribution surfaces: `@claude-code-router/core`; router parser/selector and provider/fallback machinery; agent-specific environment/auth/config integrations; desktop and CLI gateway; logs/health/account status; AgentClaw companion relay; bot-gateway integration; ToolHub/MCP and plugins/transforms.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests/docs build; external coding-agent executables and their agent loops; model providers; `@the-next-ai/bot-gateway-sdk` and any external agent/relay SDK decision logic; third-party MCP/tool servers. These surfaces may be invoked or configured by CCR without transferring their autonomous organizational decisions into CCR.
- First-party operating / deployment modes considered: desktop gateway; npm CLI gateway/UI; custom routing and fallback; provider credential pools; multiple isolated CCR instances; Agent Config integrations; AgentClaw forwarding/handoff/reply relay.
- Recursion level: CCR control plane itself. Each connected coding agent may independently be an operational/viable system and requires its own repository-relative assessment; CCR does not inherit that S1 merely because it is the common gateway.
- Reviewed revision: `a034b0c51cdd1b5628bbff545821f5540d30c6c5`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

CCR describes itself as a **local model gateway and control plane for coding agents**. Its documented quick start is: start the local gateway, configure a provider/model, apply an Agent Config to Claude Code/Codex/OpenCode/etc., then start using that external agent while CCR records the resolved route, provider/model, tokens, latency and errors. The first-party core package describes itself as "gateway, routing, provider, and storage services" and depends on gateway/bot-relay infrastructure rather than shipping a model/tool reasoning loop of its own.

The `packages/core/src/agents` tree does not change that boundary. Its entries are integration surfaces for named external agents (`claude-code`, `codex`, `opencode`, `kilo`, `pi`, `claude-app`, local providers) plus bot-gateway support. For example, the Claude Code integration contains authentication/environment handling rather than a replacement Claude Code decision loop. Bot-gateway imports the external `@the-next-ai/bot-gateway-sdk` package.

AgentClaw is also explicitly a relay/access layer. Its documentation says it connects **an agent running locally under CCR** to IM apps while the agent continues to work with its own projects, tools and sessions. The "Local agent" concept is defined as Claude Code, Codex, OpenCode, ZCode or a similar agent opened through a CCR Agent Config. The companion worker handles IM messages, projects/sessions, queueing, attachments and diagnostics. Closing the managed Agent App stops the Bot connection; CLI-only agents can still use CCR model routing without entering AgentClaw. Thus AgentClaw can carry prompts, outputs, permission answers and session commands, but the substantive autonomous operational loop remains the connected agent's loop.

Routing, retries, fallback, credential rotation, quotas, health, model selection and multi-instance isolation are meaningful control-plane machinery. They select or enforce how requests reach providers and recover from provider/API failures, but they do not create a first-party autonomous task-level decision/action loop. ToolHub/MCP and plugins add transport/transforms/capabilities to connected agents/models; they likewise do not turn CCR itself into the agent that interprets a task, chooses tools from observations and iterates to an outcome.

Primary evidence:

- [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md) — explicit local gateway/control-plane identity, external supported agents, provider/model routing, retry/fallback, ToolHub and observability surfaces.
- [`packages/core/package.json`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/packages/core/package.json) — core package identity as gateway/routing/provider/storage services and external bot-gateway SDK dependency.
- [`packages/core/src/agents/claude-code/`](https://github.com/musistudio/claude-code-router/tree/a034b0c51cdd1b5628bbff545821f5540d30c6c5/packages/core/src/agents/claude-code) — Claude Code-specific auth/environment integration rather than a first-party replacement agent loop.
- [`packages/core/src/agents/bot-gateway/sdk-import.ts`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/packages/core/src/agents/bot-gateway/sdk-import.ts) — bot relay resolves/imports `@the-next-ai/bot-gateway-sdk`.
- [`docs/src/content/docs/en/agentclaw.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/docs/src/content/docs/en/agentclaw.md) — AgentClaw as IM relay for a locally running external agent; local-agent/support matrix and companion-worker responsibilities.

## Operational model

An external coding agent or compatible client sends model requests through CCR. CCR parses the request and current configuration, chooses the configured/provider-compatible route, applies transforms/authentication, invokes the provider, performs retries/fallback/key rotation as authored policy permits, and returns the provider response to the client. The connected coding agent owns the task history, model/tool reasoning cycle, tool execution decisions and subsequent task actions.

AgentClaw extends the transport boundary rather than the agent boundary: a CCR-managed external Agent App stays local, and the companion worker mirrors/queues IM traffic and session/permission commands. Natural-language turns from IM are delivered to that local agent; the agent's output is relayed back. Removing the connected coding agent while leaving CCR's gateway, router, provider registry, logs, AgentClaw worker and UI intact leaves no first-party autonomous operational loop that can perform the coding/research task.

Methodology 0.3.5 states that if the standard distribution does not establish an autonomous operational decision/action loop, the Index should use its exclusion state rather than forcing an S1 classification. CCR therefore has a proposed canonical outcome of `excluded-no-agentic-vsm`, not `S1=C` merely because it manages agents and exposes rich control-plane primitives.

## S1 — Operations

- State: —
- Function: no first-party autonomous task-level operational decision/action loop is established in the CCR system boundary.
- Disturbance / variety regulated: CCR regulates provider/API heterogeneity, credentials, routing failures, request transport and remote access; task/environment variety is interpreted and acted on by the connected coding agent.
- Decisive decision or feedback right: choose the next substantive task/tool/action from task history and observations.
- Decision owner: the connected external coding agent (Claude Code, Codex, OpenCode, ZCode, WorkBuddy or similar), outside the assessed CCR boundary.
- Supporting / enforcement mechanisms: request router/parser/selector, provider adapters, retries/fallbacks, credential rotation, Agent Config environment/auth integration, ToolHub/MCP transport, plugins/transforms, logs and AgentClaw relay.
- Closure path: external agent task loop → model request through CCR → CCR route/provider invocation → response returned → external agent interprets result and chooses next tool/task action. The decisive operational feedback loop closes outside CCR.
- Why this is / is not agent-owned: CCR carries, transforms, routes, retries and observes requests for a separately operating coding agent. AgentClaw explicitly preserves that local agent as the executor and only relays its interactions.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md), [`docs/src/content/docs/en/agentclaw.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/docs/src/content/docs/en/agentclaw.md), [`packages/core/package.json`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/packages/core/package.json).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: connected clients may independently qualify as autonomous harnesses; this assessment does not downgrade or inherit their VSM functions.

### Absence scope

- Surfaces inspected: README/product boundary, core package identity/dependencies, `packages/core/src/agents` integrations, Claude Code integration, bot-gateway SDK import, AgentClaw docs, routing/retry/fallback/provider/ToolHub/multi-instance feature inventory.
- Plausible first-party paths checked: core gateway request processing; agent-specific integrations; AgentClaw managed apps/companion worker; ToolHub/MCP; routing plugins/transforms; provider fallback/recovery.
- Why no material first-party path remains: every task-level autonomous path still requires a separately operating coding agent; first-party CCR machinery remains gateway/configuration/transport/recovery/relay infrastructure when that agent is removed.

## S2 — Coordination

- State: —
- Function: no first-party S2 coordination function is established at the CCR recursion.
- Disturbance / variety regulated: no concrete interference/conflict/oscillation among distinct first-party S1 units is established because CCR does not establish first-party S1 units at this boundary.
- Decisive decision or feedback right: none established for an S2-specific attenuation relation.
- Decision owner: none established within CCR.
- Supporting / enforcement mechanisms: provider routing, account pools, isolated CCR instances, request queues, AgentClaw conversation serialization and multi-client management.
- Closure path: no qualifying first-party inter-S1 disturbance → attenuation decision → changed subsequent S1 behaviour loop is established.
- Why this is / is not agent-owned: routing among models/providers or serializing IM turns manages infrastructure contention/transport, not an evidenced organizational disturbance among first-party operational S1 units.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md), [`docs/src/content/docs/en/agentclaw.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/docs/src/content/docs/en/agentclaw.md).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: multiple external agents may share CCR, but their cross-agent organization is not defined merely by sharing a gateway.

### Absence scope

- Surfaces inspected: multi-agent/client support, routing and provider pools, multi-instance operation, AgentClaw queue/serialization and Agent Config integrations.
- Plausible first-party paths checked: common endpoint routing, provider/key failover, request serialization, instance isolation and shared management UI.
- Why no material first-party path remains: these paths regulate transport/provider availability rather than a concrete interference relation among first-party operational units with feedback that changes their later organizational behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-organization current-control function over CCR-owned S1 operations is established.
- Disturbance / variety regulated: CCR monitors and regulates current provider/request health, route availability, credentials, sessions and instances, but the underlying organizational operations belong to external agents.
- Decisive decision or feedback right: routing and fallback choices are determined by operator-authored configuration and deterministic router/retry machinery; operator UI actions administer infrastructure rather than an internally owned S1 organization.
- Decision owner: no autonomous first-party S3 owner established.
- Supporting / enforcement mechanisms: route selector, fallback chain, credential pool/key rotation, health/status/logging, quotas/rate-limit handling, multi-instance management and session commands.
- Closure path: no qualifying whole-system S1 view → discretionary organizational current-control decision → changed CCR-owned S1 commitments loop is established.
- Why this is / is not agent-owned: deterministic routing/recovery can strongly control request execution but does not own an organizational current-control decision; the substantive agents remain external.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md), [`packages/core/package.json`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/packages/core/package.json).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: provider failover is operationally important but Methodology explicitly separates deterministic enforcement from S3 ownership.

### Absence scope

- Surfaces inspected: route/provider/model selection, retries/fallback, credential pools, quotas/rate limits, logs/health/status, multi-instance management and AgentClaw session controls.
- Plausible first-party paths checked: dynamic routing, provider recovery, account rotation, session cancellation/model changes and operator current-state dashboards.
- Why no material first-party path remains: these mechanisms execute authored infrastructure policy or human commands and do not close autonomous whole-system regulation of first-party operational commitments.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit loop of operational reality with corrective return is established within CCR.
- Disturbance / variety regulated: observability can reveal route/provider/request failures, but no independent organizational audit claim/path is established.
- Decisive decision or feedback right: none established for an independent audit judgment that changes subsequent organizational operation.
- Decision owner: none established within CCR.
- Supporting / enforcement mechanisms: request logs, resolved-route records, latency/tokens/costs, provider/account status, diagnostics and AgentClaw delivery/error diagnostics.
- Closure path: no separate evidence path → independent audit verdict → corrective return into operation loop is established.
- Why this is / is not agent-owned: telemetry and health data are ordinary reporting/diagnostic surfaces; retries/fallback consume provider errors directly rather than an independently positioned auditor's complementary evidence.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md), [`docs/src/content/docs/en/agentclaw.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/docs/src/content/docs/en/agentclaw.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: external coding agents may run reviewers/verifiers of their own; CCR does not inherit those audit loops.

### Absence scope

- Surfaces inspected: request logs, route traces, provider/account health, usage/cost reporting, AgentClaw diagnostics/deliveries and retry/fallback behavior.
- Plausible first-party paths checked: health checks, traces/logs, provider error detection, bot diagnostics and automatic fallback.
- Why no material first-party path remains: all inspected evidence is ordinary runtime reporting or direct error handling; no sufficiently independent complementary observer/judge returns findings into subsequent organizational operation.

## S4 — Intelligence/adaptation

- State: —
- Function: no prospective external/environment-facing adaptation loop is established that develops options and changes CCR's future organizational capability autonomously.
- Disturbance / variety regulated: changing providers/models/API health is handled by configured routing/fallback, not by prospective organizational adaptation.
- Decisive decision or feedback right: provider/model/account/routing/plugin changes remain operator/developer configuration; no autonomous adaptation judgment is established.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: provider presets/probing, custom routers, plugins/transforms, ToolHub/MCP, logs/usage data and fallback rules.
- Closure path: no qualifying external/prospective distinction → generated adaptation options → selected option → changed present capability/S3 loop is established.
- Why this is / is not agent-owned: dynamic provider selection reacts within current authored policy; extensibility lets developers add capability but does not constitute an autonomous prospective adaptation loop.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: provider ecosystems and plugins can evolve, but maintainer/operator development is outside the assessed runtime adaptation function.

### Absence scope

- Surfaces inspected: provider discovery/presets, routing/fallback, plugins/transforms, ToolHub/MCP, observability, multi-instance and AgentClaw integrations.
- Plausible first-party paths checked: auto-probing providers, fallback from failures, custom router logic, plugin extension and usage-driven configuration changes.
- Why no material first-party path remains: these surfaces either react under predefined rules or require human/developer composition; none closes prospective intelligence into autonomous future capability change.

## S5 — Policy/identity

- State: —
- Function: no runtime identity/ultimate-policy authority loop is established for CCR as an organization.
- Disturbance / variety regulated: operator configuration constrains providers, models, credentials, tools and agent permissions, but no identity-level dispute/closure is evidenced.
- Decisive decision or feedback right: ultimate provider/routing/tool/permission policy is authored by the operator/developer through configuration and Agent Config; no first-party S5 authority loop is established.
- Decision owner: none established for S5 publication.
- Supporting / enforcement mechanisms: configuration files/UI, routing rules, provider/model selection, auth/credential policy, ToolHub/MCP config, AgentClaw permission-answer relay and session settings.
- Closure path: no qualifying identity/ultimate-policy matter → legitimate ultimate authority decision → returned governance of subsequent operation loop is established.
- Why this is / is not agent-owned: strong configuration and permission control governs ordinary operation; generic operator policy or permission answers are not S5 under the Methodology.
- Evidence: [`README.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/README.md), [`docs/src/content/docs/en/agentclaw.md`](https://github.com/musistudio/claude-code-router/blob/a034b0c51cdd1b5628bbff545821f5540d30c6c5/docs/src/content/docs/en/agentclaw.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: humans can approve/deny agent permission requests through AgentClaw, but that is local operational approval rather than identity/ultimate-policy governance.

### Absence scope

- Surfaces inspected: provider/model/account configuration, routing rules, Agent Config, ToolHub/MCP/plugins, permission relay and session configuration.
- Plausible first-party paths checked: master/operator configuration, permission requests, model/mode changes, custom routing policy and remote session administration.
- Why no material first-party path remains: inspected paths express operating constraints or local action decisions; none establishes an identity/ultimate-policy matter and operationally closed S5 authority/return loop at the CCR recursion.

## Recursion, variety, escalation and evidence gaps

- Recursion: CCR can manage/route many external agent instances and AgentClaw can bind a local agent to IM conversations, but those agents remain separate systems rather than nested first-party CCR S1 units for this assessment.
- Variety: CCR absorbs provider/API/model/credential/protocol/channel variety through routing, transforms, retries/fallback, account pools, ToolHub/MCP and relay machinery. That is substantial infrastructure variety management without creating first-party autonomous S1 ownership.
- Escalation: provider failures can trigger retry/fallback and agent permission/input requests can be relayed to humans through AgentClaw. These are operational mechanisms, not evidence of S5 or parent-governed metasystem ownership.
- Evidence gaps: no material gap blocks the proposed exclusion. The principal boundary question—whether AgentClaw or the `agents` tree contains a first-party agent loop—was directly checked; primary documentation defines AgentClaw as a relay to external local agents, while agent-specific core directories provide integration/configuration surfaces.

## Standalone vector

`— — — — — —`
