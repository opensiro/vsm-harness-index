---
harness_id: cuijiejie-open-agent-harness
project_name: Open Agent Harness
repository: https://github.com/cuijiejie/open-agent-harness
review_ref: 9673ebb1ab77e89042a95e6c64cf19e2e2794943
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Open Agent Harness

## Review boundary

- System in focus: the first-party self-hosted, multi-user DeepAgents application with its chat API, per-user agent factory, sandbox, operational telemetry and administrator controls.
- Purpose and identity: deliver user-assigned tool-using conversations and file/knowledge tasks while administering the currently deployed users, permissions and tools.
- Relevant environment: user requests, model providers, MCP/tool outcomes, individual OpenShell sandboxes, persisted conversations, cross-user resource and permission constraints, and administrator intervention.
- Standard-distribution boundary: `src/agent/main_agent.py`, `src/chat/stream.py`, `src/web/routers`, `src/infra` and bundled web application. DeepAgents/LangGraph are imported execution dependencies rather than credited as separately operated first-party organizations.
- Credited operating modes: configured model-backed multi-turn chat; administrator-governed operational monitoring and role/tool intervention across users; first-party tool dispatch, trace and audit recording.
- Credited operating / distribution surfaces: shipped authenticated chat stream and agent graph, admin metrics/RBAC APIs, live per-user tool filtering and platform skill publication; external model and database services are deployment dependencies.
- Adjacent surfaces excluded: developer tests, examples, external maintainers, independently deployed model or MCP servers, and any imagined audit actor not implemented in the shipped app.
- Adjacent first-party surfaces excluded from ownership: repository developer CI and test suites, benchmark/demo paths, OSS maintainer processes and the installed third-party DeepAgents library's separate governance features.
- Recursion level: each user/session model agent is an operational S1; the shared deployed platform and administrator constitute the current parent control boundary. Disabled-by-default general-purpose subagents are not counted as established additional S1 organizations.
- Reviewed revision: `9673ebb1ab77e89042a95e6c64cf19e2e2794943` (source-static), 2026-11-11.
- Generated Profile version: 0.2.4; Methodology version: 0.3.8.
- Current Profile version: 0.2.4; Methodology version: 0.3.8.

## Repository architecture

The chat endpoints authenticate a user, restore a session and stream a compiled DeepAgents graph. `AgentManager.create_agent` builds the model-backed agent with the user's OpenShell backend, user/role-filtered tools, optional MCP and skill tools, middleware and PostgreSQL checkpointer. The shared service additionally records task traces, write/execute audit entries and aggregate per-turn metrics; administrator routes can inspect site-wide metrics and change users' role-to-tool permissions, evicting cached agent instances so new calls receive the updated tools. The administrator's intervention is a parent-owned current constraint decision, not autonomous S3 cognition. [Agent factory](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py), [chat stream](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/chat/stream.py), [RBAC API](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/rbac.py).

## Operational model

Individual model agents select tools and subsequent actions from user instructions and tool responses. Their execution resources and permissions are bounded by the app. In a separate supported parent mode the administrator observes multi-user current operational state and changes a shared permission allocation, which is enforced on later agent creation. The logs and admin dashboard alone are not credited as complementary independent audit; publishing platform skills changes available content but does not demonstrate prospective external adaptation.

## S1 — Operations

- State: A
- Function: interpret variable user work, choose appropriate tools/actions, incorporate feedback and return a task result.
- Disturbance / variety regulated: natural-language tasks, discovered file/tool state, tool errors, model uncertainty and interrupted sessions.
- Decisive decision or feedback right: the configured model chooses a next tool invocation or response within a DeepAgents turn based on returned messages and state.
- Decision owner: model executing through the installed DeepAgents graph; first-party platform chooses configured tools and constraints but does not decide ordinary semantic task steps.
- Supporting / enforcement mechanisms: user-scoped OpenShell backend, MCP/skill tool registry, role filtering, middleware, checkpointer, SSE transport and cache.
- Closure path: authenticated chat request → `create_agent` → model/tool cycle → streamed tool observations and updated checkpoint → subsequent model action/final user response.
- Boundary reachability: `src/chat/stream.py` calls the first-party `create_agent`; its `AgentManager` constructs `create_deep_agent` with the configured model and tool suite, serving live sessions.
- Why this is / is not agent-owned: discretionary tool selection is model-owned; password, cache, sandbox and RBAC mechanics are deterministic support.
- Evidence: [agent construction](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py#L183-L353), [streaming execution](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/chat/stream.py).
- Basis: structural; confidence: high for packaged configured-model mode.
- Confidence: high.
- Caveats: source-static review; no live model/provider benchmark or performance inference.

## S2 — Coordination

- State: —
- Function: no evidenced inter-S1 collision attenuation with a dedicated coordination relation and returned behavior for distinct operational agents.
- Disturbance / variety regulated: users can use parallel sessions and isolated sandboxes, but interaction-specific oscillation or conflict among autonomous work units is not demonstrated.
- Decisive decision or feedback right: user permissions and request rate-limits bound individual requests; no negotiation or interference-specific response is supplied to two agents.
- Decision owner: deterministic user/session isolation and rate limits, not an inter-agent coordination decision actor.
- Supporting / enforcement mechanisms: per-user OpenShell backend, user-specific compiled graph/cache and session persistence.
- Closure path: ordinary tasks remain isolated or rejected by policy; no cross-S1 interference signal is resolved and fed back to participating work units as coordination.
- Why this is / is not agent-owned: multiple running model agents and isolation alone do not prove S2; optional DeepAgents subagents are default-disabled.
- Evidence: [per-user agent scope and subagent mode](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py#L183-L353), [chat entrypoints](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/chat/stream.py).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: a separately configured external organization could coordinate agents; it is outside this deployed app boundary.

### Absence scope

- Surfaces inspected: session/chat paths, OpenShell backend attachment, model graph construction, tool registry, rate-limiting and subagent toggle.
- Plausible first-party paths checked: concurrent user conversations, sandbox isolation, shared Redis cache and optional DeepAgents subagents.
- Why no material first-party path remains: none establishes a concrete disturbance between two autonomous operating units and a conflict-specific coordinating decision with feedback to both.

## S3 — Inside-and-now control

- State: P
- Function: current whole-platform supervision of user/session operations and shared action/tool entitlements, with administrator intervention.
- Disturbance / variety regulated: aggregate activity, failure/error conditions, excessive or disallowed actions, competing user access to privileged tool capabilities.
- Decisive decision or feedback right: a legitimate administrator sees all-site recent per-turn metrics and cross-user activity and may disable a user, revise assigned roles or revise role-to-tool allocation for affected users.
- Whole-system current view: administrator-only aggregated turn outcomes for all served users and accessible cross-user audit/users/traces, rather than just one model's chat narration.
- Current-control decision scope: platform-wide role-to-tool entitlement revision and user-level disable/role adjustment, affecting future independently running agents rather than only a single current tool call.
- Decision owner: authenticated human administrator (`is_admin`), not the ordinary agent, metrics service or RBAC cache.
- Supporting / enforcement mechanisms: `/api/metrics/summary` global aggregates, cross-user user management, RBAC database, role-to-tool APIs, cache invalidation and `AgentManager.create_agent` tool filtering.
- Closure path: active multi-user tasks emit metric/audit status → admin reviews site-wide operating constraints → admin changes user or role tool entitlements → `evict_all_agents` or per-user eviction and RBAC refresh → subsequent user agent instances receive revised accessible tools.
- Boundary reachability: all referenced APIs, current aggregates, authority checks and cache invalidation are wired into the shipped web application; this is an installed parent-operated mode, not a third-party dashboard or hypothetical policy hook.
- Why this is / is not agent-owned: discretionary whole-current intervention belongs to the parent administrator; compiled agents merely obey changed operational permissions. This is not `A` or `C` for autonomous S3.
- Evidence: [site-wide summary](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/chat.py#L421-L437), [admin role tool intervention and invalidation](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/rbac.py#L249-L280), [user role intervention](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/rbac.py#L299-L335), [tool filtering on new agent](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py#L270-L326).
- Basis: structural first-party parent mode; confidence: medium.
- Confidence: medium.
- Caveats: a human must actually interpret telemetry and choose constraints; aggregate metrics do not automatically allocate resources. This is primarily tool/permission control, not demonstrated dynamic budget or task-priority bargaining.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary verification and audit-judgment-to-control loop is shown beyond ordinary operational instrumentation.
- Disturbance / variety regulated: false-success assertions, unreported side effects and denied tool calls are risks; normal trace/audit tables collect execution events.
- Decisive decision or feedback right: `AuditService.record` records write/exec or denied calls, and admin can query; no separately controlled raw-artifact, sampled replay or ground-truth audit verdict is demonstrated.
- Decision owner: the same live runtime produces the events and records; human admin could use the logs but a supplied independent audit process is not established.
- Supporting / enforcement mechanisms: `pa_audit_log`, `pa_trace_log`, redacted event records and admin-only `/api/audit` endpoint.
- Closure path: records can be inspected outside a conversation; none independently challenges production claims and returns a distinct audit finding to current control as shipped.
- Why this is / is not agent-owned: dedicated table/endpoint names and detailed traces do not alone establish complementary audit independence.
- Evidence: [audit recording, query and filtering](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/infra/AuditService.py), [trace collection](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/infra/TraceService.py), [admin audit route](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/audit.py).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: operational audit records can be valuable input to an externally operated auditor; they are not credited as an implemented independent judgment here.

### Absence scope

- Surfaces inspected: chat tool event handling, `AuditService`, `TraceService`, audit/trace API and admin telemetry.
- Plausible first-party paths checked: step-by-step traces, long-lived write/exec audit records, risk labels and administrator inspection.
- Why no material first-party path remains: observation derives from the same instrumented execution path and no separate ground-truth access or audit-specific decision/return loop is provided.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated prospective external environmental inquiry, alternative adaptation selection and current-capability return loop.
- Disturbance / variety regulated: new skills, changing user tasks and MCP/tool inventory may cause configuration changes, but the shipped app treats them as immediate user/admin actions.
- Decisive decision or feedback right: user can publish a skill and others can install it; administrator can upload skills. No shipped actor forecasts external changes and evaluates prospective options with S3.
- Decision owner: external user/admin publishing, not an identifiable S4 adaptation decision actor.
- Supporting / enforcement mechanisms: `platform_skill` publish/add/upload routes, user skill packages and dynamic agent cache evictions.
- Closure path: manual publishing can change subsequent tools, but not through an evidenced external-and-future options → S3 dialogue → selected capability adaptation loop.
- Why this is / is not agent-owned: capability distribution and contextual memory do not by themselves establish prospective intelligence.
- Evidence: [platform skill publication and installation](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/platform_skill.py), [agent skill wiring](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: a deployed organization might run an external skill roadmap, but this review cannot attribute it to the app.

### Absence scope

- Surfaces inspected: platform skill lifecycle, model context/memory, MCP tool registry, app management routes and configuration.
- Plausible first-party paths checked: publishing a new skill, reading agent memory, reconfiguring models and administrator-provided tools.
- Why no material first-party path remains: durable tool changes lack a first-party prospective environmental model, evaluated future options and an evidenced S3–S4 return conversation.

## S5 — Policy and identity

- State: —
- Function: no demonstrated identity-level/ultimate-purpose conflict escalation and legitimate policy decision return into the deployed system.
- Disturbance / variety regulated: role violations, skill content restrictions, model prompt and tool-use security; these are operational restrictions rather than mission/identity tension.
- Decisive decision or feedback right: admin owns local access changes; no first-party process receives ultimate policy disputes from S3/S4 and resolves them with governing authority.
- Decision owner: operator/developer sets product mission outside this operational decision route.
- Supporting / enforcement mechanisms: RBAC administration, fixed agent prompt, skill content checks and configuration.
- Closure path: access and skill decisions change immediate permitted actions, but no identity/ultimate-policy matter returns as a changed governing mission or charter.
- Why this is / is not agent-owned: operational parent S3 administration cannot be promoted to S5 merely because the same human is senior.
- Evidence: [RBAC administration](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/rbac.py), [skill content checks](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/web/routers/platform_skill.py), [model configuration](https://github.com/cuijiejie/open-agent-harness/blob/9673ebb1ab77e89042a95e6c64cf19e2e2794943/src/agent/main_agent.py).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: external organizational governance cannot be inferred from admin menus and configuration.

### Absence scope

- Surfaces inspected: RBAC rights, model prompt/middleware, skill management routes, admin and chat APIs.
- Plausible first-party paths checked: privileged admin decisions, tool policy refusal, risk logs and operator ability to edit configuration.
- Why no material first-party path remains: all observed closures concern access to task/tool execution, not ultimate identity/policy decisions with return from legitimate authority.

## Distributed OSS parent arrangement

The repository's open-source governance and external maintainers are not counted as a deployed runtime parent S4/S5; the app's administrator is credited only for evidenced current S3 tool and user constraint intervention.

## Self-hosted and non-human modes

The model owns S1 task discretion when configured and reachable. An operator-hosted administrator can choose platform-wide current access changes (S3=P); an unattended deployment does not thereby acquire autonomous S3. Optional subagents disabled by default are not counted as an independent metasystem.

## Recursion

Each model-backed session is an S1 unit within a shared multi-user platform; administrator telemetry and tool constraints operate at the parent platform recursion. The vendor DeepAgents subagent option alone is not a verified viable suborganization.

## Variety and escalation

User-specific tool RBAC, sandbox isolation and cached-agent eviction attenuate potentially unsafe multi-user action variety. Tool denials are visible through operational traces; parent-admin revision can alter subsequent S1 tool repertoires. Nothing demonstrates prospective S4 or identity S5 escalation.

## Evidence gaps

- No live model call, production database, multi-user load or administrator intervention was executed; structural reachability is established from shipped paths.
- Whole-platform S3 parent claim is limited to current observed site-wide metrics and tool/user constraints; no automatic budgeting, prioritization or economic tradeoff optimization is claimed.
- Audit logs are not treated as independent S3* verdicts, and third-party DeepAgents implementation is not credited as first-party governance.
