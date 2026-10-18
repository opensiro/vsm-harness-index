---
harness_id: masters-of-ai-harness
project_name: Masters of AI Harness
repository: https://github.com/mastersof-ai/harness
review_ref: 3f5c4846a2f7ecdf48198d6d1116204132e967a5
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: C(P)
---

# Masters of AI Harness

## Review boundary

- System in focus: one installed Masters of AI Harness runtime at pinned revision `3f5c4846a2f7ecdf48198d6d1116204132e967a5`, including the shared TUI/serve runtime, installed agent definitions, Claude Agent SDK bridge, first-party MCP tools, bundled sub-agents, sessions/memory, serve-mode worker/session control, access/budget control, introspection proposal channel and supported configuration/hot-reload paths.
- Purpose and identity: provide a transparent agent runtime in which the installation owner controls agent identity/system prompt and tool environment while autonomous model actors execute work through a common local or multi-user runtime.
- Relevant environment: installation owner/operator, local and remote users, workspaces and task environments, Anthropic/Claude Agent SDK and model service, web/market/competitor information, external MCP and A2A agents, filesystem/shell/network resources, and changing operational demand across users and sessions.
- Standard-distribution boundary: first-party package/runtime code and the `~/.mastersof-ai/` agent/config/access/state layout shipped and documented by the repository. Claude Agent SDK/model reasoning is a separate external agent actor reached by the supported runtime and does not donate unrelated framework internals. External MCP/A2A systems remain environmental systems rather than first-party metasystem owners.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/agents.md`; `docs/configuration.md`; `docs/tools.md`; `docs/memory.md`; bundled default agents; `src/agent.ts`; `src/session-worker.ts`; `src/serve.ts`; access/cost/usage/health/watcher modules; first-party introspection, A2A and sub-agent tooling.
- Adjacent first-party surfaces excluded from ownership: repository-development specs and security-wave planning/review documents; CI and CodeQL workflows; tests and test fixtures; changelog/release work; contributor/maintainer governance. These may corroborate implementation intent but do not close runtime VSM functions for the installed harness.
- First-party operating / deployment modes considered: local TUI/headless agent execution, multi-user `--serve`, bundled default-agent execution, built-in sub-agent delegation, optional sandboxed remote execution, A2A/MCP integrations, operator-edited `IDENTITY.md`/`config.yaml`/`access.yaml`, and serve-mode hot reload.
- Recursion level: the installed harness is the system-in-focus. Primary agent sessions are installation-level operational units. Built-in researcher/deep-thinker/writer sub-agents are lower-recursion work units inside a primary agent's operational loop unless a top-level installation relation explicitly reaches them.
- Reviewed revision: `3f5c4846a2f7ecdf48198d6d1116204132e967a5`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Masters of AI Harness wraps Claude Agent SDK `query()` with an explicit first-party runtime. `IDENTITY.md` supplies the behavioral identity, `buildSystemPrompt()` adds transparent environment/memory/continuity context, `buildOptions()` creates filtered in-process MCP servers and SDK sub-agent definitions, and `sendMessage()` calls the external SDK query loop. The standard tool plane includes memory, workspace, web, shell, tasks, introspection, model-query, scratchpad and A2A capabilities. The primary model actor chooses reasoning, tool use and delegation; deterministic callbacks enforce configured permissions, approvals, verification reminders and sandbox/access constraints.

The runtime exposes two principal operating modes. TUI/headless execution is local and single-user. Serve mode adds Fastify/WebSocket transport, per-user workspace/memory/session isolation, process-isolated session workers, authentication, per-user access/tool restrictions, token budgets, usage accounting, worker-pool limits, health state and operator hot reload. The admin usage response includes all observed session usage records, while deep health exposes active sessions/connections, error rate and worker-pool utilization. `access.yaml` carries per-user agent access, budgets and denied tools; changes are hot-reloaded, budgets are resynchronized, and revoked tokens are disconnected.

The standard distribution also exposes deliberate meta-change surfaces. Introspection tools let an agent read its own `IDENTITY.md` and tool source, then write structured prompt/tool proposals explicitly "for review". The bundled cofounder identity instructs the agent to use these surfaces when its behavior, framing, context or capabilities should change and explicitly states that proposals are reviewed before taking effect. Separately, the built-in researcher is designed to inspect web information, competitors and market data before decisions, and the A2A client can discover external Agent Cards and capabilities. These provide concrete sensing and proposal paths, but the default agent is not granted authority to apply its own identity or global capability changes.

## Operational model

A user selects an installed agent and submits an objective. The harness assembles that agent's identity, persistent context, workspace/environment state and available tools, then invokes the Claude Agent SDK. The model actor autonomously selects reasoning, tools, sub-agents and task actions within first-party restrictions. Outputs and state are persisted for continuation; remote mode runs each conversation in an isolated worker process and routes approvals/results through the parent server.

At installation recursion, current whole-system control is intentionally operator-oriented rather than autonomously supervised. First-party admin/health/usage/access surfaces expose current load, usage, access and budget state plus concrete intervention mechanisms, but no packaged autonomous installation supervisor chooses those interventions. That creates an S3 constructor mode alongside a closed operator/parent mode.

For adaptation and identity, the autonomous agent can generate structured options through `tools_propose` and `prompt_propose`, but those tools deliberately stop at a reviewable proposal. The installation owner can accept an adaptation by editing supported config/agent-definition surfaces; config/access watchers and subsequent worker/session construction return those decisions into runtime capability. Identity-body edits are re-read by `buildSystemPrompt()` on subsequent turns. The same first-party proposal channels therefore expose constructor modes while the default closed authority remains the parent operator.

## S1 — Operations

- State: A
- Function: perform user-directed research, coding, analysis, writing and other tool-mediated work in a persistent agent workspace/session.
- Disturbance / variety regulated: heterogeneous user goals, workspace state, web/external information, tool results, model uncertainty, remote service responses and iterative task feedback.
- Decisive decision or feedback right: choose the substantive reasoning path, tool calls, delegated sub-agent work and task-specific actions required to pursue the admitted objective.
- Decision owner: the autonomous Claude model/agent actor invoked through the harness runtime.
- Supporting / enforcement mechanisms: `IDENTITY.md`/system-prompt assembly, MCP server creation, tool filters, `canUseTool`, approvals, sandbox/egress policy, session persistence, process isolation, verification/loop-detection hooks and UI/transport layers.
- Closure path: user objective → first-party context/tool construction → SDK query loop → model chooses actions/tools/sub-agents → tool/environment results return into the model loop → result/artifacts return to the user and persisted workspace/session.
- Boundary reachability: TUI, headless and serve modes all directly reach the agent actor through the repository's `sendMessage() → query()` path with first-party system-prompt and tool construction. The model service is external, but the autonomous S1 actor is part of the supported assembled operating mode rather than borrowed from repository-development machinery.
- Why this is / is not agent-owned: the runtime constrains and transports actions, but the substantive operational choices are made by the model actor. Static tool filters, budgets and approvals do not replace that local task discretion.
- Evidence: [`README.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/README.md); [`docs/architecture.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/architecture.md); [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts); [`src/session-worker.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/session-worker.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `A` credits the externally supplied model actor reached through the standard first-party harness mode; it does not attribute Claude Agent SDK internals to Masters of AI Harness.

## S2 — Coordination

- State: —
- Function: no installation-level S2 coordination function is established from the reviewed standard distribution.
- Disturbance / variety regulated: the harness can run multiple agents, users, workers and sub-agents, but the top-level evidence does not identify a specific interference/conflict/oscillation among distinct installation-level S1 units together with a first-party mutual-adjustment relation that attenuates it.
- Decisive decision or feedback right: not established at the installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-user isolation, worker-pool caps, query mutexes, access restrictions, scratchpad files and sub-agent task routing can prevent generic races or carry work, but they do not by themselves establish the required inter-S1 disturbance/coordination witness at installation recursion.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: there is no established installation-level S2 function whose decisive coordination discretion could be assigned to an owner.
- Evidence: [`docs/architecture.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/architecture.md); [`docs/agents.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/agents.md); [`src/serve.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/serve.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the bundled sub-agent scratchpad pattern coordinates lower-recursion delegated work, but shared scratch state and delegation are not promoted to installation-level S2 without a concrete sibling-S1 disturbance witness.

### Absence scope

- Surfaces inspected: primary/sub-agent architecture, scratchpad relation, serve-mode worker/session lifecycle, query mutex, worker-pool limits, per-user workspaces/memory, access/budget controls, tool routing and session persistence.
- Plausible first-party paths checked: researcher/deep-thinker/writer scratchpad flow; concurrent user/session workers; query serialization; worker caps; access isolation; task/delegation and A2A paths.
- Why no material first-party path remains: the reviewed mechanisms isolate, serialize, limit, delegate or transport work, but no top-level path is tied to regulation of a specific interaction-generated disturbance among distinct installation-level S1 units. Lower-recursion sub-agent sequencing is not sufficient to manufacture top-level S2.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current installation-wide access and resource commitments across users/sessions using current usage, health and worker-pool state.
- Disturbance / variety regulated: concurrent sessions and users vary in token consumption, active worker demand, error/load state, agent access and tool permissions; these can exceed current budgets/capacity or require immediate access/resource intervention.
- Decisive decision or feedback right: choose or revise a user's current agent/tool access and token-resource allowance, revoke access, or reset exhausted budget state in response to current installation conditions.
- Decision owner: base constructor mode — no autonomous installation supervisor is supplied; a downstream autonomous controller must be composed over the first-party health/usage/admin/access surfaces. Parent mode — the installation owner/operator with admin access and control of `access.yaml`/runtime administration.
- Supporting / enforcement mechanisms: `UsageTracker`, `CostTracker`, budget checks, worker-pool limits, authentication, `toolsDeny`, access filtering, file watchers, WebSocket disconnect on token revocation and admin budget-reset endpoint.
- Closure path: current installation usage/health/session state is observed → controller/operator decides a resource/access intervention → admin API or supported access/config state is changed → budget/access state is reloaded/enforced → subsequent requests/sessions are admitted, blocked, constrained or disconnected accordingly.
- Boundary reachability: serve mode directly exposes admin `/api/usage`, `/health/deep`, budget reset and hot-reloaded access/config state; no CI, maintainer or development-only actor is needed. The constructor path is reachable through those first-party runtime surfaces, while the standard parent mode is reachable to the self-hosting installation operator.
- Why this is / is not agent-owned: deterministic budget checks and token revocation enforce decisions but do not choose allocation policy. The standard distribution exposes the S3-specific current-control path without packaging an autonomous owner, while the operator can close it directly.
- Evidence: [`src/serve.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/serve.ts); [`src/usage.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/usage.ts); [`src/cost.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/cost.ts); [`src/access.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/access.ts); [`src/health.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/health.ts); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary per-tool user approvals and static rate limits are not themselves credited as S3 ownership; the positive mapping relies on installation-wide current state plus resource/access intervention.
- Whole-system current view: admin `/api/usage` adds summaries and `allSessions()` records across observed users/sessions, including `agentId`, `userName`, token use, turns and `lastUsedAt`; `/health/deep` adds active sessions/connections, error rate and worker-pool utilization.
- Current-control decision scope: revise per-user budgets/agent/tool access, revoke tokens with immediate disconnect, or reset current budget counters so subsequent current operation changes.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous installation controller must be composed | current health/usage/session/access state exposed by first-party runtime | controller can use the specific admin/access/config paths to change current resource/access constraints; enforcement then alters subsequent requests | `src/serve.ts`; `src/usage.ts`; `src/access.ts`; `src/cost.ts` |
| Parent (`P`) | self-hosting installation owner/operator | current usage, worker/load, budget or access condition requires intervention | operator resets budget or edits supported `access.yaml`/config state; watcher/runtime updates enforcement and subsequent requests are admitted/blocked/disconnected under the returned decision | `docs/configuration.md`; `src/serve.ts`; `src/watcher.ts`; `src/access.ts` |

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is established for installation-level operational claims.
- Disturbance / variety regulated: ordinary agent outputs may be wrong and runtime state may fail, but the shipped checks do not create a sufficiently independent audit organization that challenges S1/S3 claims and returns findings into current control.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `verifyBeforeComplete` write/read tracking, loop detection, tool logs, health checks, `model_query`, researcher delegation, CI/tests and CodeQL.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: verification reminders are part of the producer's ordinary loop; health checks are routine runtime observability; generic model/sub-agent calls are not wired as an independent audit claim/challenge/return loop; CI/CodeQL belongs to the adjacent repository-development system.
- Evidence: [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts); [`docs/configuration.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/configuration.md); [`src/health.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/health.ts); [`src/tools/model-query.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/model-query.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user can ask a sub-agent/model to review work, but generic optional review composition is not a first-party S3* function under the Methodology.

### Absence scope

- Surfaces inspected: verification/loop-detection hooks, model-query tool, sub-agent definitions, health/logging, tool approvals, test/CI/security-review surfaces and serve-mode error/worker handling.
- Plausible first-party paths checked: post-write verification, independent model query, researcher/deep-thinker delegation, health/deep checks, logs, security validation and CI/CodeQL.
- Why no material first-party path remains: none of the credited runtime paths establishes a distinct claim under audit, materially complementary access to operational reality, sufficient independence and a corrective return into installation control. Repository CI/reviews are outside the operating boundary.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: sense changing external capabilities/information, form prospective capability-adaptation options, and return selected options into the installed agent's future tool/integration capability.
- Disturbance / variety regulated: external competitors/markets, web information, remote-agent capabilities and available integration options can change, creating new opportunities or capability gaps relative to the installed agent's current toolset.
- Decisive decision or feedback right: decide which sensed external capability/gap should become a future runtime capability, for example by registering a useful remote A2A agent or changing enabled/attached tools.
- Decision owner: base constructor mode — the standard distribution supplies external sensing plus a dedicated tool-change proposal path, but no autonomous authority that applies global capability changes; a downstream autonomous adopter must be composed. Parent mode — the installation owner/operator reviews the proposal and decides whether to change supported config/agent capability surfaces.
- Supporting / enforcement mechanisms: researcher web/competitor/market sensing, `a2a_discover` Agent Card inspection, `tools_read`, `tools_propose`, `config.yaml`, per-agent tool/MCP frontmatter, config watcher and new worker/session construction.
- Closure path: agent/researcher observes an external capability or environment distinction → agent identifies a capability gap/opportunity and records a tool proposal → autonomous downstream adopter or parent operator selects an option → supported config/agent capability state is changed → watcher/new session construction exposes the selected capability to subsequent operation.
- Boundary reachability: researcher, A2A discovery and introspection are all enabled/reachable first-party runtime surfaces in the standard package; `config.yaml` and agent frontmatter are documented operator surfaces. The positive claim does not borrow repository roadmap/maintainer research as S4.
- Why this is / is not agent-owned: the agent can autonomously sense and generate adaptation proposals, but `tools_propose` deliberately records them for review rather than applying them. Therefore no `A` closure is claimed; the shipped proposal/config interfaces support a constructor path and a separately closed operator mode.
- Evidence: [`src/agents/researcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agents/researcher.ts); [`src/tools/a2a.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/a2a.ts); [`src/tools/introspection.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/introspection.ts); [`docs/configuration.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/configuration.md); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: persistent memory and generic learning are not used as the S4 witness. The positive mapping depends on the concrete external-sensing → capability proposal → supported adoption path; source-code development/release activity is excluded.
- External distinction: the built-in researcher is explicitly intended for web searches, competitor scans and market data before decisions; `a2a_discover` fetches a remote Agent Card's advertised skills/capabilities.
- Future / prospective distinction: `tools_propose` is explicitly for a missing capability, tool improvement or new tool that would make the agent more effective in future operation.
- Adaptation option generated: a structured tool/capability proposal containing the target tool, reason/gap and proposed change; one concrete supported option is adding/registering a discovered A2A capability or changing the configured tool/MCP set.
- Path back into current capability / S3: accepted operator/config changes are loaded through documented config/frontmatter paths; config hot reload changes server configuration and subsequent session/worker construction receives the updated capability set.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adaptation authority must be composed | first-party researcher/A2A sensing exposes an external change/capability and `tools_propose` records an adaptation option | downstream actor can be composed to accept a proposal and write the documented config/agent capability surface, which later runtime construction consumes | `src/agents/researcher.ts`; `src/tools/a2a.ts`; `src/tools/introspection.ts`; `docs/configuration.md` |
| Parent (`P`) | installation owner/operator | reviewed proposal identifies a useful external capability or tool gap | owner accepts/rejects the option and edits documented config/frontmatter; hot reload/new worker/session returns the selected capability into operation | `src/tools/introspection.ts`; `docs/configuration.md`; `src/watcher.ts`; `src/tools/index.ts` |

## S5 — Policy and identity

- State: C(P)
- Function: surface and close changes to the agent's durable identity/system-prompt policy when experience indicates that its behavior, framing or governing instructions should change.
- Disturbance / variety regulated: accumulated operation can reveal that the current identity produces undesirable behavior, lacks important context or embodies a framing/instruction set that should change while preserving a legitimate ultimate authority over what the agent is.
- Decisive decision or feedback right: authorize a change to the durable `IDENTITY.md` body that defines the agent's system-prompt identity and therefore governs subsequent operation.
- Decision owner: base constructor mode — the first-party agent can inspect and propose identity changes but has no shipped authority to apply them; a downstream autonomous ultimate-policy authority would have to be composed. Parent mode — the installation owner/operator who reviews proposals and controls the agent's `IDENTITY.md`.
- Supporting / enforcement mechanisms: `prompt_read`, `prompt_propose`, per-agent proposal directory, documented human-readable `IDENTITY.md` source of truth, `buildSystemPrompt()` reload and serve-mode agent-file watcher.
- Closure path: agent detects an identity/behavior issue → reads current identity and writes a structured identity/system-prompt proposal → downstream authority or parent operator makes the ultimate identity decision → accepted text is written to `IDENTITY.md` → `buildSystemPrompt()` reloads the identity for subsequent turns → later operation is governed by the returned decision.
- Boundary reachability: introspection is enabled by default, the bundled cofounder explicitly instructs self-reflection/proposal use, `IDENTITY.md` is the documented operator-controlled source of agent identity, and system-prompt construction is part of every supported execution mode. No project-maintainer governance is required for the parent loop.
- Why this is / is not agent-owned: the agent owns proposal generation but the shipped tool intentionally stops at “recorded for review.” Because it cannot authorize its own durable identity change, no `A` closure is claimed. The dedicated proposal path supports `C`, while the local operator provides the closed parent mode.
- Evidence: [`src/tools/introspection.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/introspection.ts); [`defaults/agents/cofounder/IDENTITY.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/defaults/agents/cofounder/IDENTITY.md); [`docs/agents.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/agents.md); [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts); [`src/session-worker.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/session-worker.ts); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: static presence of `IDENTITY.md` is not the positive witness. The positive mapping depends on the runtime identity-issue/proposal/review/application/return loop. Ordinary tool approvals, access rules and model selection are not treated as S5.
- Identity / ultimate-policy issue: the first-party introspection surface explicitly covers changes to “your own identity or system prompt” when behavior, framing or missing context should change.
- Ultimate authority in each claimed mode: base `C` leaves autonomous ultimate authority uncomposed; parent `P` places authority with the installation owner/operator who controls and reviews `IDENTITY.md` changes.
- Return-to-operation path: accepted identity text is written to `IDENTITY.md`; `buildSystemPrompt()` loads the current manifest/body when constructing subsequent prompts, including on subsequent messages in the serve worker, so later model operation is governed by the accepted identity.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous identity/policy authority must be composed | agent detects a behavior/framing/identity issue and records it through `prompt_propose` | first-party proposal + identity-source path is exposed, but an autonomous approver/editor must be added before the system can close the identity decision without a parent | `src/tools/introspection.ts`; `docs/agents.md`; `src/agent.ts` |
| Parent (`P`) | installation owner/operator | agent proposal or operator judgment identifies an identity/system-prompt change | owner reviews and edits `IDENTITY.md`; subsequent `buildSystemPrompt()` use returns the authoritative identity to operation | `defaults/agents/cofounder/IDENTITY.md`; `docs/agents.md`; `src/agent.ts`; `src/session-worker.ts` |

## Distributed OSS parent arrangement

The positive parent modes in this assessment are local to one self-hosted installation. They do not rely on or imply organization-level governance by the public repository's maintainers or contributors. Repository PR/release/security-review machinery is outside the credited runtime ownership boundary.

## Self-hosted and non-human modes

The self-hosted operator has explicit current-control, adaptation and identity authority in supported files/admin surfaces, producing the recorded `(P)` modes. The package also exposes function-specific constructor surfaces from which downstream autonomous S3/S4/S5 authorities can be composed, but this review does not upgrade them to `A` because the standard distribution does not supply those decisive autonomous closure owners.

## Recursion

Primary agent sessions enact the installation's operational purpose and may internally delegate to researcher, deep-thinker and writer contexts. Those sub-agents have bounded roles, tool restrictions and scratchpad exchange, but spawning/delegation alone does not establish them as fully viable recursive organizations. Their relations are therefore treated as lower-recursion implementation of one primary S1 rather than as automatic evidence for installation-level S2/S3/S3*.

## Variety and escalation

The harness attenuates operational variety through per-agent tool filters, remote sandbox policy, per-user tool denial, rate limits, process isolation, query serialization and token budgets. It amplifies response variety through web/shell/workspace tools, model queries, built-in sub-agents, external MCP and A2A calls. User questions and serve-mode tool approvals can escalate local uncertainty to a human, but generic approval is not promoted to S5. Budget/access changes and identity/capability proposals are classified according to the specific S3/S4/S5 functions they close.

## Evidence gaps

- No first-party autonomous installation supervisor was found that owns the S3 current-control decisions exposed by admin/health/access surfaces.
- No installation-level inter-S1 disturbance/coordination witness was found for S2; lower-recursion scratchpad/delegation is intentionally not promoted.
- No materially independent runtime audit organization with corrective return was found for S3*.
- S4 parent closure is strongest for capability changes expressible through documented runtime configuration/frontmatter (for example A2A/tool/MCP configuration); proposals requiring package source development/release remain outside the credited operating boundary.
- S5 autonomous closure is intentionally absent from the default introspection design: identity changes are proposals for review, not self-applied policy changes.
