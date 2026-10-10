---
harness_id: nasiko
project_name: Nasiko
repository: https://github.com/Nasiko-Labs/nasiko
review_ref: 58cfe600559c67d58100ec2856d7b29838e2859f
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Nasiko

## Review boundary

- System in focus: one supported Nasiko server/control-plane deployment handling an agent fleet via authenticated A2A, its first-party model-backed ReAct orchestration path, and the shared flow-guard/ACL/proxy, with externally deployed A2A workers.
- Purpose and identity: admit, direct and govern multi-agent task requests securely, prevent runaway mutually delegated work, and produce orchestrated responses through first-party operating logic.
- Relevant environment: client requests, separately deployed user-provided A2A workers, external model inference APIs, MCP/tool providers, Postgres/Redis/S3-backed state, host Docker and network failures, model/agent capability shifts.
- Standard-distribution boundary: Nasiko Rust server, router/A2A dispatch, packaged `react-agent` model loop and tool adapter as actually wired by the production orchestrator route, `flow` guard, proxy/ACL/auth, agent registry and deployment; external agent container internals and their proprietary models/tool loops are not donated.
- Credited operating / distribution surfaces: `server/src/router/a2a_dispatch.rs` production branch, `react-agent/src/react_loop.rs` and A2A tool interface, `server/src/acl.rs`, `server/src/agent_proxy.rs`, `flow/src/guard.rs`; authenticated model-backed orchestrator mode and multi-agent server flow.
- Adjacent first-party surfaces excluded from ownership: examples, unit/e2e tests, CI/release/benchmark machinery, unrelated agents in the `agents/` directory not proven as part of this deployment; standalone library code not imported by the chosen mode; upstream third-party A2A worker cognition. Orchestrator `selector.rs` speaks to per-request routing, not a credited separate whole-current S3.
- First-party operating / deployment modes considered: self-hosted server with registered A2A agents and external model key, `agent_id=orchestrator` ReAct mode, multiple workers under same flow scope with Redis flow guard; direct A2A proxy-only mode without a Nasiko-owned discretionary agent loop.
- Recursion level: one deployed agent-fleet control plane and its model-driven orchestrator plus admitted S1 worker processes; independent user tenants/providers and the open-source maintainer organization are distinct.
- Reviewed revision: `58cfe600559c67d58100ec2856d7b29838e2859f`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Nasiko's Rust server implements an authenticated single ingress, identity and secret brokerage, A2A dispatch/reverse proxy, agent registry, optional three-stage routing (embedding shortlist, conversation-aware reranker and model-based final agent selection), OCI/deploy surface and Redis-backed per-flow guard. Production A2A dispatch explicitly constructs `nasiko_react_agent::Orchestrator`, supplies an active agent registry, model endpoint and ACL/flow guard, and streams a multi-turn ReAct process: model picks tool calls to individual registered A2A workers, executes them, injects their results/errors into a context window, and selects further calls or final response. This is a first-party built-in S1 decision path, not merely proxying external A2A agents.

For multi-worker calls sharing a flow identifier, `FlowGuard` tracks call chain/depth, fan-out, total tokens and timeout in Redis. The production A2A proxy runs guard `check` before reaching a target; the ReAct tool path runs `CpCallGuard` before invoking the named worker. Attempted calls back to a worker already active in the chain, or excess aggregate calls, are blocked. A blocked ReAct invocation becomes model-visible tool feedback; a direct proxy attempt returns `LOOP_DETECTED`. This attenuates specific A↔B looping and cascading disturbances rather than just classifying or routing one request.

Other first-party secrets, observability, LLM routing and ACL surfaces constrain/transport work but do not automatically establish S3, S3*, S4 or S5. Sources: [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md); [a2a_dispatch.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/router/a2a_dispatch.rs); [react_loop.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/react-agent/src/react_loop.rs); [guard.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/flow/src/guard.rs); [acl.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/acl.rs); [agent_proxy.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/agent_proxy.rs); [selector.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/selector.rs); [engine.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/engine.rs).

## Operational model

The credited first-party model-backed orchestrator is an S1 operating actor that produces responses through a discretionary ReAct loop. Separately deployed A2A agents perform real work as integrated operational units, but their internal loops/permissions are external. Within the same fleet, a deterministic guard coordinates the concrete disturbance of cyclic or exploding recursive cross-agent invocations. No global-current commitment authority or prospective adaptation loop is attributed to the routing engine merely because its final pick can invoke an LLM.

## S1 — Operations

- State: A
- Function: execute incoming requests through a Nasiko-owned model-driven ReAct orchestration agent which can choose and call external A2A worker tools, and synthesize final responses.
- Disturbance / variety regulated: changing requests, heterogeneous fleet capabilities, remote worker outputs and tool failures across successive model turns.
- Decisive decision or feedback right: a configured model makes discretionary tool-call, worker-selection and continuation/final-answer choices across the first-party ReAct loop.
- Decision owner: the hosted completion model as the decisive agent actor inside the first-party `nasiko-react-agent::Orchestrator`; model inference provider is an external dependency, not a source of imported hidden worker governance.
- Supporting / enforcement mechanisms: production A2A `agent_id=orchestrator` dispatch, agent registry, dynamically constructed A2A tools, model completion, local context window, tool-result feedback, turn limit, call guards.
- Closure path: authenticated A2A request selects `orchestrator` → first-party orchestrator chooses from running A2A agent tools → first-party loop invokes chosen tool and records result/error → result is added to model context → following model turn chooses further calls or final response → streamed event returns to caller.
- Boundary reachability: `server/src/router/a2a_dispatch.rs` instantiates `nasiko_react_agent::Orchestrator`, injects actual agent registry, A2A client, live ACL/flow guard and invokes `run_stream` in a shipped server route. This is not an unused example or only a dependency test.
- Why this is / is not agent-owned: without the completion model the harness would retain routers and HTTP plumbing but lack discretionary multi-turn response/tool selection; the specifically packaged first-party ReAct loop supplies the operational structure.
- Evidence: [a2a_dispatch.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/router/a2a_dispatch.rs); [react_loop.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/react-agent/src/react_loop.rs); [tool.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/react-agent/src/tool.rs); [context.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/react-agent/src/context.rs); [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md)
- Basis: structural + explicit.
- Confidence: high for configured provider-backed ReAct mode.
- Caveats: external A2A workers can perform their own operational transformations, but their private decision loops are not credited to Nasiko. A generic direct A2A proxy-only installation without `orchestrator` does not by itself prove Nasiko-owned model S1.

## S2 — Coordination

- State: C
- Function: prevent inter-agent invocation cycles and explosive fan-out in shared multi-agent work flows so distinct worker S1 units do not consume each other's operating capacity through endless delegated calls.
- Disturbance / variety regulated: agent A invokes B, B sends work back to A or to too many other agents; a recursive/cascading call chain can destabilize the shared worker fleet and exhaust common budget.
- Decisive decision or feedback right: reject a next agent invocation when target is already on the recorded call chain, or invocation/depth/token limits are exceeded; otherwise admit it and record the call under shared flow state.
- Decision owner: first-party deterministic `FlowGuard`/ACL constructor; administrators set thresholds and agents choose work, but no agent autonomously revises the guard's decision policy.
- Supporting / enforcement mechanisms: Redis scoped flow context, call chain/depth/invocation counters, `check`, `record_invocation`, `record_return`, bounded fail-closed GuardUnavailable, server A2A proxy and ReAct tool boundary.
- Closure path: worker agent A calls B with propagated flow identity → guard checks and updates shared chain → if B calls an earlier S1 such as A, `CycleDetected` refuses it (or `MaxFanOutExceeded` refuses surplus calls) → HTTP proxy returns `LOOP_DETECTED` or ReAct tool error is inserted into next model context → no prohibited inter-S1 call reaches target, so the caller must modify or stop the attempted delegation.
- Boundary reachability: production `server/src/agent_proxy.rs` calls flow `check` and `record_invocation` on A2A proxy requests, and `server/src/acl.rs` implements `CallGuard` injected into actual ReAct dispatch. This is a standard server path, not an invented coordination layer.
- Why this is / is not agent-owned: the constructor chooses the outcome from configured counters, not model discretion; models can react to blocked feedback but do not own the first-party interference gate.
- Distinct S1 units: at least two independently operating registered user-provided A2A workers in one `FlowContext`, with Nasiko ReAct orchestrator invoking those workers where enabled.
- Inter-S1 disturbance: recursive agent A↔B calls or repeated cross-worker delegation amplifies demand and can prevent either worker from making progress, exhausting a common flow's invocation/token budget.
- Attenuating coordination relation: the shared Redis `call_chain` detects the target already active and shared `total_invocations` bounds fleet-wide delegation before admitting next S1 call.
- Feedback into subsequent S1 behaviour: a `LOOP_DETECTED` response or tool `Blocked` observation prevents the receiver being invoked; source model can choose an alternative worker or terminate while stable flow state prevents additional damaging calls.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it targets a documented and structurally evidenced *mutual cross-S1 disturbance* (reentrant cycles/cascade growth) rather than merely forwarding messages, preserving call order or applying a per-agent ACL.
- Evidence: [guard.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/flow/src/guard.rs); [context.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/flow/src/context.rs); [acl.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/acl.rs); [agent_proxy.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/agent_proxy.rs); [a2a_dispatch.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/router/a2a_dispatch.rs); [react_loop.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/react-agent/src/react_loop.rs); [state.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/state.rs)
- Basis: explicit + structural.
- Confidence: medium-high for connected multi-agent flow-guard mode.
- Caveats: flow depth/fan-out are configured static bounds, not proof of autonomous conflict negotiation, global fair scheduling or file-merge mediation. Redis availability is a prerequisite and distinct context IDs limit which invocations share a guard scope.

## S3 — Inside-and-now control

- State: ?
- Function: regulate aggregate current agent-fleet commitments, resource allocation and priority conflicts in a coherent whole-workspace current-control feedback loop.
- Disturbance / variety regulated: unhealthy/running workers, overburdened agents, competing current projects, uneven worker utilization and failures.
- Decisive decision or feedback right: the route selector chooses a target for one request and operators can deploy/stop/view agents, but a system-wide live commitment adjudication over the fleet was not established.
- Decision owner: LLM selector owns per-request assignment; runtime operators own individual deployment/configuration. Whole-current S3 authority not evidenced.
- Supporting / enforcement mechanisms: fleet agent list, dashboard, agent registry, three-stage intent/context route selection, traces, rate/flow guard, deploy controls, health monitors.
- Closure path: the request-local selector forwards one request to a chosen agent and returns its outcome; no demonstrated first-party aggregate portfolio of current commitments → decision reprioritizing competing work → return to multiple S1s.
- Boundary reachability: routing, fleet registry and UI are shipped but they do not by themselves close S3.
- Why this is / is not agent-owned: even a model choosing an agent by skill/intent is speaker/work selection, not authority over shared current resource/priority policy.
- Whole-system current view: active fleet descriptors are available; whole-current work and priorities across all running flows are not convincingly represented in the decision loop.
- Current-control decision scope: per-call routing and deterministic flow admission established; systemic current reallocation remains unresolved.
- Evidence: [engine.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/engine.rs); [selector.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/selector.rs); [agent_registry.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/agent_registry.rs); [a2a_dispatch.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/router/a2a_dispatch.rs); [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md); [state.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/state.rs)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: do not promote routing/monitoring/quotas to S3 merely because there is a fleet dashboard.

## S3* — Complementary audit

- State: ?
- Function: independently challenge worker performance claims using material operational evidence and return corrective decisions.
- Disturbance / variety regulated: misreported task completion, missing artifact or false remote outcomes.
- Decisive decision or feedback right: observability spans and API request/response traces preserve information but no independent audit judge with returned correction is established.
- Decision owner: unresolved for first-party complementary auditor.
- Supporting / enforcement mechanisms: OTel traces, per-hop logs, token/cost usage, flow events and dashboard diagnostics.
- Closure path: traces follow agent calls, yet a separate direct-evidence audit verdict feeding changes to worker tasks/admission is not evidenced.
- Boundary reachability: telemetry and trace UI ship, but independent challenge does not follow automatically.
- Why this is / is not agent-owned: a model or user viewing traces is not an enacted S3* audit function without independently sourced challenge and action.
- Claim being audited: a worker reported a correct response/artifact or completion.
- Ordinary reporting path: A2A task event and response.
- Complementary access path: OTel trace and server metrics, which document calls rather than validating answer correctness.
- Independence boundary: no separately bound first-party independent reviewer/verifier proved.
- Who acts on findings: human can investigate but no automatically returned audit-correction function identified.
- Evidence: [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md); [a2a_dispatch.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/router/a2a_dispatch.rs); [agent_proxy.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/agent_proxy.rs)
- Basis: explicit + unresolved.
- Confidence: medium in insufficiency.
- Caveats: telemetry ≠ audited correctness; hold uncertain instead of claiming absence.

## S4 — Outside-and-then intelligence

- State: ?
- Function: sense prospective environmental change and choose adaptations to the whole system's future operating capabilities.
- Disturbance / variety regulated: new external model/agent opportunities, future customer needs and changing provider reliability.
- Decisive decision or feedback right: operator can register or deploy new agents, but no first-party prospective scanning/evaluation/choice loop was demonstrated.
- Decision owner: unknown.
- Supporting / enforcement mechanisms: agent discovery, skill embedding shortlist, LLM response selection, registry, usage history and optional deployment.
- Closure path: route selection responds to current query against current registry; not a future capability planning decision returned into fleet resources.
- Boundary reachability: registry and routing are in standard server, but that is insufficient prospective option-generation.
- Why this is / is not agent-owned: reactive reranking against currently available skills is not forward-looking intelligence simply because an LLM is involved.
- External distinction: no specialized external horizon-sensing channel for fleet evolution shown.
- Future / prospective distinction: no decision affecting future system composition, only current invocation.
- Adaptation option generated: unverified.
- Path back into current capability / S3: no function-specific return established.
- Evidence: [engine.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/engine.rs); [selector.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/selector.rs); [agent_registry.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/orchestrator/src/agent_registry.rs); [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: this does not rule out S4 in downstream enterprises deploying Nasiko.

## S5 — Policy and identity

- State: ?
- Function: decide and return legitimate ultimate organization-wide purpose/policy of the agent fleet, rather than enforce static permissions.
- Disturbance / variety regulated: competing purposes, invalid authority changes and ultimate policy/identity disputes.
- Decisive decision or feedback right: JWT, secrets, ownership grants, per-agent ACL and model routing policies are real, but a distinct identity-level authority judgment is not established.
- Decision owner: operator/admin defines credential/access configuration; ultimate organization policy-deciding role unresolved.
- Supporting / enforcement mechanisms: ownership/auth claims, short-lived tokens, central secrets, Docker deployment controls and ACL guard.
- Closure path: claims influence access to specific agent calls; no observed constitutive purpose dispute → legitimate authority decision → returned organizational identity/policy closure.
- Boundary reachability: security administration is shipped but lacks function-specific ultimate-policy evidence.
- Why this is / is not agent-owned: static access gate and secret broker enforce existing policy, not own agent organization identity.
- Identity / ultimate-policy issue: not evidenced at this recursion.
- Ultimate authority in each claimed mode: no positive S5 mode established.
- Return-to-operation path: allow/deny security result impacts tool call but not ultimate purpose decision.
- Evidence: [README.md](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/README.md); [acl.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/acl.rs); [lib.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/auth/src/lib.rs); [state.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/state.rs); [agent_proxy.rs](https://github.com/Nasiko-Labs/nasiko/blob/58cfe600559c67d58100ec2856d7b29838e2859f/server/src/agent_proxy.rs)
- Basis: structural + unresolved.
- Confidence: medium in insufficiency.
- Caveats: identity tokens and ownership grants are not synonymous with VSM S5.

## Distributed OSS parent arrangement

Nasiko's GitHub maintainers are outside the deployed customer fleet; external A2A agent maintainers are not automatic policy controllers of this local installation. A fleet operator configures admission/permissions, but this doesn't prove the installation has S5 ultimate-policy decision closure.

## Self-hosted and non-human modes

A self-hosted Nasiko server may run autonomously with a configured completion model and active A2A agents through its packaged ReAct route. Model-inference API and Redis/Postgres/docker services are required for their respective pathways. In proxy-only mode local session routing and flow guard continue, but the dedicated Nasiko ReAct S1 model-loop witness is not active. Human dashboard deployment and policy settings constrain access without establishing whole-system human S3.

## Recursion

The control-plane deployment plus registered workers and its ReAct orchestrator form the focal whole. Each third-party A2A agent is one lower-level operational unit; a requester, model API provider, enterprise tenant and OSS project organization are outside the same recursion. The inter-worker guard is credited only for calls under a properly propagated common `FlowContext`.

## Variety and escalation

Model-driven orchestrator absorbs task and worker-result variety; flow guard stops mutual work amplification via cycle/fan-out/depth and per-worker ACL, returning explicit tool/HTTP refusals; observability makes incidents visible to operator. Rejection or health alerts are not independently an S3 or S3* owner. No future adaptation or identity dispute closure proved.

## Evidence gaps

- Reproduce a provider-backed ReAct request through `agent_id=orchestrator` and separately verify model-driven tool routing and follow-up against live worker outputs; source evidence shows actual server wiring but no running provider account used in this review.
- Reproduce an A→B→A attempted cycle and excess fan-out with shared trace/flow context against Redis; verify the returned error reaches an operating worker. Guarded noncycles are not proof of broad workload fairness.
- Check if any distinct whole-current fleet resource management, independent direct-evidence auditing, prospective adaptation or ultimate identity governance is actually wired before upgrading S3/S3*/S4/S5.
- Do not inherit generic external A2A workers' hidden planning/review/governance into Nasiko S1/S3/S3*/S4/S5.
