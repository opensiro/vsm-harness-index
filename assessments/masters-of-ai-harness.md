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
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: C(P)
---

# Masters of AI Harness

## Review boundary

- System in focus: one Masters of AI Harness installation at pinned revision `3f5c4846a2f7ecdf48198d6d1116204132e967a5`, including its TUI/headless/serve runtime, configured agent roster, system-prompt assembly, first-party MCP tools, built-in sub-agent registry, session/memory/workspace state, serve-mode worker processes, operator/admin control surfaces, introspection proposals, configuration/frontmatter and hot-reload paths.
- Purpose and identity: turn human-authored `IDENTITY.md` files into persistent autonomous Claude Agent SDK-backed agents whose tools, memory, sessions, users and deployment controls remain inspectable and operator-configurable.
- Relevant environment: installation owner/operator, local and remote users, workspaces and files, the Claude Agent SDK/model service, web sources, remote A2A agents, external MCP services, access/budget constraints, session/process failures and the application environments in which configured agents act.
- Standard-distribution boundary: first-party runtime, TUI/headless/serve interfaces, agent/context loader, prompt assembly, MCP tool servers, sub-agent registry, sessions/memory, worker/session isolation, access/rate/cost controls, introspection tools, configuration/frontmatter and hot-reload behavior. Claude Agent SDK/model internals, remote A2A agents and external MCP implementations remain separate actors/dependencies and do not donate their internal organizational functions.
- Credited operating / distribution surfaces: `README.md`; `DESIGN.md`; `docs/architecture.md`; `docs/agents.md`; `docs/configuration.md`; `docs/tools.md`; `docs/design-decisions.md`; `src/agent.ts`; `src/agent-context.ts`; `src/tools/index.ts`; `src/tools/introspection.ts`; `src/tools/model-query.ts`; `src/serve.ts`; `src/watcher.ts`; default agent definitions such as `defaults/agents/cofounder/IDENTITY.md`.
- Adjacent first-party surfaces excluded from ownership: GitHub Actions/CodeQL, contributor/development governance, changelog validation work, repository security-hardening plans and tests, and source-maintainer implementation work required to add new core tool code. These may corroborate design intent but do not close runtime VSM functions for an installed harness.
- First-party operating / deployment modes considered: local TUI/headless agent runs, multi-user `--serve` deployment, built-in sub-agent delegation, configured remote A2A/MCP access, operator/admin serve mode, default cofounder self-improvement/introspection path and supported hot reload of agents/config/access state.
- Recursion level: the installed harness deployment is the system-in-focus. Primary configured agent sessions are top-level S1 work cells. Researcher/deep-thinker/writer sub-agents are treated as lower-recursion operational decomposition inside one primary-agent work cell unless a top-level relation explicitly regulates them as peer S1 units.
- Reviewed revision: `3f5c4846a2f7ecdf48198d6d1116204132e967a5`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Masters of AI Harness is a first-party control/runtime layer over the Claude Agent SDK. An agent definition is a directory whose `IDENTITY.md` body becomes the core system prompt; the harness appends transparent runtime context such as persistent memory, date/time, workspace state, enabled tools, verification guidance and continuity hints. `buildOptions()` then creates first-party MCP servers, sub-agent definitions, hooks and the `canUseTool` control path before the request enters the SDK `query()` loop.

The distribution supports a local TUI, headless runs and a multi-user Fastify/WebSocket serve mode. Serve mode isolates workspace, memory, sessions and logs per user, runs conversations in child workers, tracks usage/cost, exposes current sessions/usage, and lets administrators intervene in budgets, access and configuration. `access.yaml` and `config.yaml` are hot-reloaded; token revocation, budget changes and rate-limit changes return directly into subsequent runtime behavior.

Sub-agents are separate SDK contexts with bounded turns and tool restrictions. Researcher, deep-thinker and writer can exchange intermediate artifacts through a confined `.scratch/` directory. This is a real delegation/coordination mechanism, but the reviewed top-level evidence does not identify a concrete inter-S1 conflict or oscillation that the scratchpad attenuates, so it is not promoted to S2.

The default tool set includes web/A2A access plus an explicit introspection server. `prompt_read` and `prompt_propose` let an agent inspect its identity and record identity/system-prompt changes for review. `tools_read` and `tools_propose` similarly expose capability/tool-change proposals. The bundled cofounder explicitly describes this as self-improvement and states that proposals are reviewed before taking effect. The agent cannot directly apply those proposals through the introspection tools; this separation is material to S4/S5 ownership.

## Operational model

A user selects or exposes a configured agent and supplies a message. The first-party runtime resolves that agent, constructs the prompt and available tools, creates the SDK options and sends the task into Claude Agent SDK `query()`. The model actor chooses the substantive reasoning/tool sequence while the harness constrains tools, workspaces, budgets, approvals and process/session lifecycle.

In serve mode, current-control ownership is intentionally split. The runtime exposes whole-deployment usage/session summaries, health and explicit admin intervention such as budget reset; config/access hot reload can change current resource constraints. Those are S3-specific construction surfaces but no packaged autonomous deployment-level supervisor decides when to use them. A legitimate operator/admin can close the same loop manually, so S3 is `C(P)`.

For adaptation, the standard runtime can sense external distinctions through web/A2A tools and exposes a first-party capability-proposal path through `tools_read`/`tools_propose`. Supported capability changes such as MCP/A2A attachments and enabled-tool configuration can be returned into subsequent runs through `IDENTITY.md` frontmatter/config and hot reload. The autonomous actor is not allowed to apply its own proposal, so the base mode is constructor-owned; an operator can review and apply supported adaptations, producing a distinct parent mode. S4 is therefore `C(P)` rather than `A`.

Identity follows the same deliberate split. `prompt_propose` is specifically an identity/system-prompt proposal primitive, while `IDENTITY.md` remains the operator-authored source of truth and subsequent prompt assembly reloads it. The default cofounder states that self-improvement proposals are reviewed before taking effect. The distribution therefore exposes both an S5 constructor path and a parent-governed closure mode, but not autonomous ultimate identity authority: S5 is `C(P)`.

## S1 — Operations

- State: A
- Function: perform the configured agent's user-facing work through an autonomous model/tool loop and produce task outcomes in the agent workspace and external environment.
- Disturbance / variety regulated: heterogeneous user objectives, workspace state, web/A2A/MCP information, tool results, persistent context, failures and domain-specific task uncertainty.
- Decisive decision or feedback right: choose the substantive reasoning, tool calls, delegation, file/workspace actions and response sequence required to satisfy an admitted task.
- Decision owner: the Claude model/agent actor reached through the Claude Agent SDK `query()` loop.
- Supporting / enforcement mechanisms: `IDENTITY.md` prompt assembly, first-party MCP servers, tool filtering, `canUseTool`, sandbox/access policy, session persistence, worker isolation, budgets, memory and sub-agent registry.
- Closure path: user/remote caller submits objective → harness resolves agent and builds prompt/options → model actor selects and executes work through allowed tools/sub-agents → runtime streams/persists results → user or subsequent work consumes the outcome.
- Boundary reachability: TUI, headless and serve modes all enter the same first-party `buildSystemPrompt()` / `buildOptions()` / SDK query path; the external model actor is therefore reached by the supported distribution rather than borrowed from repository-development tooling.
- Why this is / is not agent-owned: first-party code selects constraints and transports events, but the task-specific operational discretion is exercised by the model actor. `sendMessage() → query()` is the documented execution path.
- Evidence: [`README.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/README.md); [`docs/architecture.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/architecture.md); [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `A` credits the autonomous operational actor made reachable by the first-party harness; it does not reclassify Claude Agent SDK/model internals as first-party Masters of AI code.

## S2 — Coordination

- State: —
- Function: no top-level S2 function is established from the reviewed standard distribution.
- Disturbance / variety regulated: multiple users, primary agents and nested sub-agents can coexist, but no specific top-level interaction-generated interference/conflict/oscillation plus attenuating coordination relation was established.
- Decisive decision or feedback right: not established at the installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-user isolation, query mutexes, rate limits, sub-agent tool restrictions, delegation and `.scratch/` shared state prevent or organize some technical interactions but are not credited as S2 without the required concrete inter-S1 disturbance witness.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: delegation and scratchpad exchange move work/information, but the evidence does not tie them to regulation of a specific conflict or oscillation among top-level S1 units.
- Evidence: [`docs/architecture.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/architecture.md); [`docs/agents.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/agents.md); [`src/serve.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/serve.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the researcher/deep-thinker/writer scratchpad flow may be useful coordination inside a lower-recursion primary-agent work cell, but nesting/delegation alone is not promoted into installation-level S2.

### Absence scope

- Surfaces inspected: architecture and agent docs; sub-agent registry/roles; scratchpad coordination; serve-mode mutex/isolation; rate/concurrency controls; session/worker lifecycle; A2A/MCP delegation surfaces.
- Plausible first-party paths checked: `.scratch/` exchange, sub-agent sequencing, per-user query mutexes, rate limits, worker/process isolation and remote-agent calls.
- Why no material first-party path remains: reviewed mechanisms delegate, isolate, serialize or transport work, but none is tied to a concrete top-level inter-S1 disturbance with an S2-specific attenuation decision and feedback path.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current deployment-wide resource/access constraints and intervene in ongoing user/agent operation using whole-deployment usage/session state.
- Disturbance / variety regulated: concurrent sessions/users can consume different amounts of model capacity, exceed budgets, require access revocation, hit rate/concurrency limits or need current constraint changes while the deployment remains live.
- Decisive decision or feedback right: choose current budget/access/resource interventions for users/agents and return those choices into active/subsequent operation.
- Decision owner: constructor mode — not supplied; a downstream autonomous supervisor must be composed over the first-party current-state/admin/config surfaces. Parent mode — an authenticated installation operator/admin.
- Supporting / enforcement mechanisms: `UsageTracker`, `CostTracker`, rate limiter, worker limits, `/api/usage`, `/health/deep`, admin budget reset, `access.yaml`/`config.yaml` reload, token revocation and deterministic budget/rate enforcement.
- Closure path: current usage/session/deployment state is exposed → controller/operator selects a resource/access intervention → admin API or supported config/access change applies it → cost/rate/access machinery updates → later requests/sessions are admitted, blocked or constrained under the returned decision.
- Boundary reachability: the constructor primitives and parent/admin paths are all shipped serve-mode surfaces; no development-only bot, CI workflow or maintainer process is needed.
- Why this is / is not agent-owned: deterministic meters and limits enforce already-selected budgets/rules. No standard-distribution autonomous metasystem decides when a user should receive a reset, new allocation or access change; the API/config surfaces expose that decision path for composition, while the parent operator can close it directly.
- Evidence: [`docs/architecture.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/architecture.md); [`docs/configuration.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/configuration.md); [`src/serve.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/serve.ts); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the ordinary task-level tool approval callback is not used as S3 evidence; the credited parent loop is deployment-level current resource/access regulation.
- Whole-system current view: authenticated operators receive `/api/usage` with full `summary` and `sessions`; deep health exposes deployment state; serve mode tracks active sessions/connections and worker-pool state.
- Current-control decision scope: reset user/session/daily/monthly budget counters, revise budget/access entries, revoke users/tokens, and alter live rate/resource constraints through hot-reloaded configuration.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous supervisor must be composed | whole-deployment usage/session/health state or budget/access exception | supervisor can use first-party admin/config paths to change current budget/access/resource state; harness enforcement applies the returned choice | `docs/architecture.md`; `docs/configuration.md`; `src/serve.ts` |
| Parent (`P`) | installation operator/admin | current usage/session state or an operational budget/access/resource exception | operator resets/revises budget/access/config; watcher/admin path reloads it and subsequent requests run under the changed constraints | `docs/configuration.md`; `src/serve.ts`; `src/watcher.ts` |

## S3* — Complementary audit

- State: —
- Function: no materially independent top-level complementary audit loop is established from the reviewed runtime.
- Disturbance / variety regulated: ordinary agents may make incorrect completion or artifact claims, but the shipped verification/model-query/logging surfaces do not themselves establish an independent audit relation with corrective return into installation-level control.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: verify-before-complete reminders, read-after-write tracking, loop detection, structured logs, model-query comparisons, health checks and repository CI/security checks.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the verification hook is inside the producer's ordinary execution path; `model_query` is a generic one-shot comparison tool with no first-party audited claim, independence contract or mandatory corrective-return loop; CI/CodeQL are adjacent repository-development systems.
- Evidence: [`docs/configuration.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/configuration.md); [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts); [`src/tools/model-query.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/model-query.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user-created agent could employ `model_query` as part of a critic/reviewer design, but generic framework expressiveness is not a first-party S3* function.

### Absence scope

- Surfaces inspected: verification hooks and prompt; `canUseTool` read-after-write tracking; model-query tool; sub-agent definitions; logs/health; serve worker isolation; repository CI/CodeQL/security-validation surfaces.
- Plausible first-party paths checked: independent sub-agent reviewer, cross-model critic, raw-artifact checker, sampled replay/reconciliation and development security checks.
- Why no material first-party path remains: no runtime path specifies the claim being audited, ordinary reporting path, materially independent complementary evidence path and corrective return into current control. The strongest checks are producer-side/routine or development-adjacent.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: expose an adaptation path in which an agent can sense external/future-relevant capability needs, formulate a tool/capability change and return an accepted change into subsequent runtime capability.
- Disturbance / variety regulated: changing external information sources, available remote agents/services, missing tool capability, tool limitations and future task requirements can make the current configured capability set inadequate.
- Decisive decision or feedback right: decide which capability/tool adaptation should become part of the installation's future operating repertoire.
- Decision owner: constructor mode — the standard runtime supplies external sensing plus `tools_read`/`tools_propose`, but an autonomous authority/apply loop must be composed. Parent mode — installation owner/operator reviewing a proposal and applying a supported configuration/frontmatter capability change.
- Supporting / enforcement mechanisms: default-enabled web and A2A tools, external MCP attachment in agent frontmatter, A2A registry/config, introspection proposal files, config/agent hot reload and MCP/tool creation in `buildOptions()`.
- Closure path: external/future-relevant capability gap is observed → agent can formulate a concrete tools proposal → controller/operator selects an adaptation → supported MCP/A2A/tool configuration or agent frontmatter is changed → watcher/runtime reloads configuration/agent definition → subsequent sessions are created with the adapted capability set.
- Boundary reachability: web/A2A/introspection tools and MCP/frontmatter/configuration are standard-distribution runtime features; the credited parent closure is limited to adaptations expressible through supported configuration/frontmatter. Core source-code development required for a novel built-in tool is excluded from the parent-mode proof.
- Why this is / is not agent-owned: the default cofounder is instructed to notice tool gaps and propose improvements, but `tools_propose` only records a proposal for review. No shipped path lets the proposing agent authoritatively apply the capability change itself.
- Evidence: [`README.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/README.md); [`defaults/agents/cofounder/IDENTITY.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/defaults/agents/cofounder/IDENTITY.md); [`src/tools/introspection.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/introspection.ts); [`src/tools/index.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/index.ts); [`docs/agents.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/agents.md); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic memory, web research and ordinary task planning are not credited as S4. The constructor claim rests specifically on the self-improvement proposal primitive plus supported capability configuration/attachment paths.
- External distinction: default-enabled web/A2A and configurable external MCP surfaces expose changing external sources, remote agents and services to the operational agent.
- Future / prospective distinction: `tools_propose` is explicitly for a missing capability, tool improvement or new tool that would make the agent more effective; the default cofounder is instructed to use it for tool gaps/improvements that expand future capability.
- Adaptation option generated: `tools_propose` records the proposed tool/capability change and reason for review.
- Path back into current capability / S3: accepted supported changes can be expressed through agent frontmatter/config (tool filtering, external MCP, A2A registry) and hot-reloaded; subsequent `buildOptions()` constructs the changed tool set.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adaptation authority/apply loop must be composed | agent detects an external/future capability gap and records a tools proposal | first-party proposal + configuration/MCP/A2A primitives expose the path, but autonomous adoption authority is intentionally absent | `src/tools/introspection.ts`; `src/tools/index.ts`; `docs/agents.md` |
| Parent (`P`) | installation owner/operator | reviewed tools proposal or observed external capability gap | operator changes supported agent/config/MCP/A2A capability; hot reload / next option build returns it into subsequent operation | `docs/agents.md`; `docs/configuration.md`; `src/watcher.ts` |

## S5 — Policy and identity

- State: C(P)
- Function: surface identity/system-prompt issues for authoritative review and return an accepted identity decision into subsequent agent behavior.
- Disturbance / variety regulated: the current agent identity/instructions can become behaviorally inadequate, omit needed framing/context or require a deliberate identity-level change while preserving a legitimate ultimate authority.
- Decisive decision or feedback right: determine which proposed change becomes the authoritative `IDENTITY.md` / system prompt governing future operation.
- Decision owner: constructor mode — no autonomous ultimate authority is supplied; `prompt_read`/`prompt_propose` expose an identity-specific proposal path for downstream composition. Parent mode — the installation owner/agent author who controls the `IDENTITY.md` source of truth.
- Supporting / enforcement mechanisms: `prompt_read`, `prompt_propose`, proposal storage under agent state, human-readable `IDENTITY.md`, manifest loading, prompt assembly, agent-directory watcher and roster/config reload behavior.
- Closure path: agent detects an identity/behavior issue → `prompt_propose` records an identity/system-prompt proposal for review → parent authority accepts/rejects and edits the authoritative `IDENTITY.md` when accepting → subsequent prompt assembly loads that identity → later agent operation is governed by the returned decision.
- Boundary reachability: introspection is enabled in the default runtime configuration, the bundled cofounder explicitly uses it for self-improvement, and `IDENTITY.md` editing is the documented first-party agent-authoring mechanism. No repository maintainer or CI actor is required for the credited parent mode.
- Why this is / is not agent-owned: the proposing agent may formulate an identity change but cannot apply it through the introspection tool. `prompt_propose` explicitly records the proposal "for review", and the bundled cofounder states proposals are reviewed before taking effect; ultimate identity authority therefore remains outside the agent in the standard mode.
- Evidence: [`README.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/README.md); [`docs/agents.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/docs/agents.md); [`defaults/agents/cofounder/IDENTITY.md`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/defaults/agents/cofounder/IDENTITY.md); [`src/tools/introspection.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/tools/introspection.ts); [`src/agent.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/agent.ts); [`src/watcher.ts`](https://github.com/mastersof-ai/harness/blob/3f5c4846a2f7ecdf48198d6d1116204132e967a5/src/watcher.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: static identity text by itself would not be S5. The positive mapping depends on the explicit runtime identity-proposal path plus a documented parent-owned identity source of truth and return into later prompt assembly.
- Identity / ultimate-policy issue: `prompt_propose` is specifically for changes to the agent's own identity or system prompt when behavior, framing or context should change.
- Ultimate authority in each claimed mode: base constructor mode leaves authority uncomposed; parent mode vests authority in the installation owner/agent author who edits the authoritative `IDENTITY.md`.
- Return-to-operation: accepted identity edits are loaded by `loadAgentManifest()` / `buildSystemPrompt()` for subsequent agent execution; serve mode watches agent definitions and broadcasts roster updates when `IDENTITY.md` changes.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous identity authority/apply loop must be composed | agent identifies an identity/behavior deficiency and records a proposal | first-party `prompt_read`/`prompt_propose` expose the identity feedback path, but applying/authorizing it is deliberately absent | `src/tools/introspection.ts`; `defaults/agents/cofounder/IDENTITY.md` |
| Parent (`P`) | installation owner / agent author | reviewed identity/system-prompt proposal | owner edits authoritative `IDENTITY.md`; subsequent prompt assembly loads the decision and future operation follows it | `README.md`; `docs/agents.md`; `src/agent.ts`; `src/watcher.ts` |

## Recursion

- Top-level S1 units are configured primary-agent sessions producing user outcomes. In serve mode several users/agents can operate concurrently under shared deployment controls.
- Built-in researcher/deep-thinker/writer contexts are nested work decomposition under a primary agent. They have bounded roles and tool restrictions, but this review does not treat spawning/delegation alone as proof that each is a viable recursive system.
- Remote A2A agents are external systems contacted through a first-party tool, not first-party S1 units unless a separate deployment explicitly moves that boundary.

## Variety, escalation, and homeostasis

- Variety attenuation: per-user workspaces/memory, tool allow/deny filters, sandbox/egress/credential restrictions, rate limits, cost caps, worker limits and compact-success hooks reduce operational variety presented to agents/operators.
- Variety amplification: web, A2A, external MCP servers, model-query and built-in sub-agents extend the response repertoire available to S1.
- Current-control escalation: tool approval prompts, budget warnings/exceeded states, access/admin paths and health/usage summaries can bring current exceptions to an operator; these channels do not change the S-function classification by themselves.
- S3↔S4 relation: present resource/access state is visible through serve-mode usage/admin surfaces, while future capability proposals can return through supported tool/MCP/A2A configuration. No autonomous top-level agent is packaged to arbitrate that present/future balance.
- S5 closure: identity adaptation is intentionally separated from autonomous application; the agent may propose, while authoritative identity change remains parent-governed unless a downstream constructor closes a different mode.

## Evidence gaps and caveats

- No first-party autonomous deployment-level supervisor was found for S3; constructor notation does not imply one ships.
- No qualifying S3* loop was found despite verification, model-query and CI/security surfaces.
- S4 parent closure is limited to adaptations expressible through supported runtime configuration/frontmatter. A proposal requiring new first-party source code moves into the adjacent development organization and is not credited as runtime closure.
- S5 parent closure is reconstructed from the explicit proposal-for-review contract plus operator-authored `IDENTITY.md` as the system-prompt source of truth; there is no dedicated approve/apply command.
- Claude Agent SDK/model behavior, remote A2A agents and external MCP services remain outside first-party ownership even when they are reachable through the standard runtime.
