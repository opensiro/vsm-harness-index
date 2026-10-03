---
harness_id: sandbox-agent
project_name: Sandbox Agent
repository: https://github.com/rivet-dev/sandbox-agent
review_ref: bbc195cc3fb5a1dd9cb05d8437442768c511e17e
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sandbox Agent

## Review boundary

- System in focus: the first-party `rivet-dev/sandbox-agent` server/SDK control plane at frozen revision `bbc195cc3fb5a1dd9cb05d8437442768c511e17e`, including agent-process lifecycle, ACP/HTTP translation, sessions, permission forwarding, universal event normalization, process/desktop control, restoration/persistence interfaces, Inspector, CLI and server surfaces.
- Purpose and identity: run and remotely control third-party coding-agent processes inside sandboxes through a stable HTTP/SDK interface while normalizing transport, sessions, events, permissions and process/desktop management.
- Relevant environment: client applications and operators, sandbox/container runtimes, target filesystems/processes/desktops, supported Claude Code/Codex/OpenCode/Cursor/Amp/Pi agent processes, credentials, prompts, agent-emitted tool/permission events, network/runtime failures and optional external persistence.
- Standard-distribution boundary: Sandbox Agent's Rust server, TypeScript SDK, ACP proxy/adapter, process/desktop runtime, session/event/permission transport, Inspector and CLI are inside. Claude Code, Codex, OpenCode, Cursor, Amp and Pi reasoning/tool loops are separate external agent organizations even when Sandbox Agent installs, launches or proxies their processes. The `foundry/` application is adjacent first-party software built on Sandbox Agent rather than part of the assessed server/SDK operating boundary.
- Credited operating / distribution surfaces: `README.md`; `server/packages/sandbox-agent/src/{router,acp_proxy_runtime,process_runtime,universal_events}.rs`; `server/packages/acp-http-adapter`; `server/packages/agent-management`; `docs/{agent-sessions,manage-sessions,session-restoration,session-persistence,processes,inspector}.mdx`.
- Adjacent first-party surfaces excluded from ownership: `foundry/` product/application organization; repository-development CI/tests/examples; Inspector/debug UI when used only to expose external-agent state; sandbox-provider examples; external agent-process packages and native coding-agent binaries; contributor/maintainer governance.
- First-party operating / deployment modes considered: embedded SDK; HTTP server; ACP proxy sessions; OpenCode compatibility; supported agent process install/launch; prompt/event streaming; permission requests and operator replies; session restoration/replay; generic process/PTY control; Inspector.
- Recursion level: one Sandbox Agent-managed coding-agent session/control plane is the focal organization. The launched Claude/Codex/OpenCode/etc. agent process is an external operational organization, not a first-party S1 merely because Sandbox Agent starts and transports it.
- Reviewed revision: `bbc195cc3fb5a1dd9cb05d8437442768c511e17e`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Sandbox Agent explicitly describes itself as a universal adapter/control server between a client application and multiple coding agents. The Rust `AcpProxyRuntime` resolves or installs the selected external agent process, starts that process through the ACP adapter, normalizes a small set of protocol differences, forwards JSON-RPC payloads, and streams the process's responses/events back to clients. The generic process runtime similarly owns spawn/list/stop/kill/log/input/PTY mechanics rather than semantic task interpretation.

Session APIs create/resume sessions and forward prompts into the external agent. Event schemas expose agent messages, thoughts, plans, tool calls and usage. Permission requests are surfaced to the client/operator, whose reply is `once`, `always` or `reject`; Sandbox Agent transports that decision. Session restoration recreates a fresh external-agent session and replays persisted recent events into the next prompt when configured persistence indicates the previous runtime session is stale.

Counterfactual owner test: remove the supported external coding-agent processes while retaining Sandbox Agent's HTTP server, ACP transport, session/event normalization, process/desktop runtime, Inspector, permission plumbing and restoration logic. The remaining system can create execution environments, move bytes/state, enforce lifecycle operations and replay context, but it cannot interpret an open-ended coding objective, choose semantic repository/tool actions from observations, or decide completion. The required autonomous operational decision loop is therefore not first-party.

Primary evidence:

- [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md)
- [`server/packages/sandbox-agent/src/acp_proxy_runtime.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/acp_proxy_runtime.rs)
- [`server/packages/sandbox-agent/src/router.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/router.rs)
- [`server/packages/sandbox-agent/src/process_runtime.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/process_runtime.rs)
- [`server/packages/agent-management/src/agents.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/agent-management/src/agents.rs)
- [`docs/agent-sessions.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/agent-sessions.mdx)
- [`docs/session-restoration.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/session-restoration.mdx)
- [`docs/inspector.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/inspector.mdx)

## Operational model

A client chooses a supported agent and creates or resumes a session. Sandbox Agent resolves/launches the external agent process, forwards prompts/configuration through ACP or a compatibility adapter, normalizes the resulting event stream and exposes lifecycle/permission/process controls over HTTP/SDK. When the external agent emits a permission request, a client/operator can respond and Sandbox Agent relays the response. When persistence is configured and a live agent session is lost, the SDK can recreate the session and replay recent stored events as context.

The semantic action-selection loop remains in the supported external coding-agent process. Sandbox Agent owns transport, execution substrate and control-plane mechanics around that loop.

## S1 — Operations

- State: —
- Function: no first-party autonomous open-ended coding operation is established at the Sandbox Agent server/SDK boundary.
- Disturbance / variety regulated: session/process lifecycle, agent selection/installation, protocol differences, streaming, permissions, runtime loss, filesystem/process/desktop access and transport failures are regulated; semantic coding-task variety is absorbed by the launched external coding agent.
- Decisive decision or feedback right: interpret the open-ended coding objective, choose semantic repository/tool actions after observations, evaluate those results and decide the next semantic action or completion.
- Decision owner: the external Claude Code/Codex/OpenCode/Cursor/Amp/Pi agent process.
- Supporting / enforcement mechanisms: ACP proxy/adapter; agent installation/launch; HTTP/SSE/WebSocket server; session/event normalization; process/desktop runtime; permission transport; restoration/replay; CLI/Inspector.
- Closure path: client prompt → Sandbox Agent session/ACP transport → external coding-agent reasoning/tool loop → tool/repository observations → external agent next semantic decision → normalized Sandbox Agent events/result.
- Why this is / is not agent-owned: Sandbox Agent controls where and how the external agent runs but does not supply the task-semantic decision loop. Removing the external agent leaves a capable remote-control/process substrate, not an autonomous coding operation.
- Evidence: [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md); [`server/packages/sandbox-agent/src/acp_proxy_runtime.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/acp_proxy_runtime.rs); [`server/packages/agent-management/src/agents.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/agent-management/src/agents.rs); [`docs/agent-sessions.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/agent-sessions.mdx).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: installation, launch and protocol normalization do not transfer the organizational decision ownership of the launched agent into Sandbox Agent.

### Absence scope

- Surfaces inspected: README architecture; ACP proxy and adapter; agent manager; session APIs; prompt/event transport; permission handling; process/desktop runtime; restoration/persistence; Inspector; CLI; OpenCode compatibility; adjacent Foundry integration.
- Plausible first-party paths checked: server-side agent wrapper; ACP payload normalization; session restoration/replay; permission automation; generic process execution; Inspector prompt testing; Foundry application code.
- Why no material first-party path remains: every standard-distribution open-ended coding path ultimately forwards the task to a separately implemented external coding-agent process for semantic action selection. First-party code supplies control/transport mechanics but not the autonomous objective→observation→semantic-action loop.

## S2 — Coordination

- State: —
- Function: no first-party same-recursion inter-S1 coordination function is established.
- Disturbance / variety regulated: multiple processes/sessions can coexist and the runtime has lifecycle/concurrency mechanics, but the assessed boundary does not establish multiple first-party autonomous S1 units whose interaction creates an evidenced conflict or oscillation.
- Decisive decision or feedback right: choose a coordination response to a concrete disturbance among distinct same-recursion S1 units and feed that response back into their subsequent behavior.
- Decision owner: not established as a first-party S2 owner.
- Supporting / enforcement mechanisms: session IDs; process registry; runtime limits; ACP instance registry/locks; independent event streams; external sandbox isolation.
- Closure path: deterministic registries/lifecycle rules separate or serialize transport/process activity; no first-party autonomous inter-S1 coordination judgment loop closes.
- Why this is / is not agent-owned: process/session plurality and locking are infrastructure coordination, while the operational agents themselves are external.
- Evidence: [`server/packages/sandbox-agent/src/acp_proxy_runtime.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/acp_proxy_runtime.rs); [`server/packages/sandbox-agent/src/process_runtime.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/process_runtime.rs); [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a host application can coordinate several external coding agents through Sandbox Agent, but that host organization is outside this boundary.

### Absence scope

- Surfaces inspected: session/process registries, ACP instance locking, process limits, examples with multiple sessions, Foundry integration and event routing.
- Plausible first-party paths checked: session plurality; process concurrency limits; ACP per-server locks; agent selection; Foundry queue/workflow use.
- Why no material first-party path remains: no standard Sandbox Agent runtime path establishes autonomous first-party S1 units plus an interference-specific decision/feedback relation. Adjacent Foundry coordination cannot be borrowed.

## S3 — Inside-and-now control

- State: —
- Function: substantial lifecycle and operator-control surfaces exist, but no first-party autonomous whole-system current-control judgment is established at the assessed recursion.
- Disturbance / variety regulated: agent/process availability, session status, permissions, runtime limits, desktop/process health and operator interventions.
- Decisive decision or feedback right: make discretionary whole-system current decisions over commitments/resources/priorities or interventions rather than merely execute client/operator commands and fixed lifecycle rules.
- Decision owner: client/operator or adjacent host system; Sandbox Agent transports/enforces requested actions and deterministic limits.
- Supporting / enforcement mechanisms: create/resume/destroy sessions; process create/stop/kill/delete; Inspector; runtime configuration; permission response forwarding; agent install/status; desktop start/stop; health/status endpoints.
- Closure path: current state is exposed → client/operator or host makes the decisive intervention → Sandbox Agent executes the requested lifecycle/configuration action → subsequent external-agent/process operation changes.
- Why this is / is not agent-owned: the server has hard enforcement power over processes, but the organizational choice of what current work should continue, stop, receive permission or be prioritized remains outside the autonomous first-party system.
- Evidence: [`server/packages/sandbox-agent/src/router.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/router.rs); [`docs/agent-sessions.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/agent-sessions.mdx); [`docs/processes.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/processes.mdx); [`docs/inspector.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/inspector.mdx).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deterministic process/runtime limits and operator commands are current-control mechanisms but do not establish autonomous S3 ownership under the Methodology.

### Absence scope

- Surfaces inspected: process/session/desktop lifecycle APIs; runtime limits; health/status; Inspector controls; permission request/reply; agent manager; restoration.
- Plausible first-party paths checked: process concurrency control; auto-restart; session restoration; permission handling; Inspector interventions; agent install/status management.
- Why no material first-party path remains: located first-party paths either execute predetermined lifecycle policy or carry a client/operator decision. No autonomous supervisory actor owns a whole-system current-control choice.

## S3* — Complementary audit

- State: —
- Function: Inspector, event history and replay provide observability/debugging but no independent first-party complementary audit judgment with corrective return.
- Disturbance / variety regulated: sessions/events/tool calls/process logs can be inspected and replayed for debugging or external audit.
- Decisive decision or feedback right: independently challenge an operational claim using materially different access and return findings that alter subsequent operation.
- Decision owner: human/client or external tooling; no first-party audit actor established.
- Supporting / enforcement mechanisms: normalized event schema; Inspector JSON/event views; process logs; persistence interfaces; replay/offsets.
- Closure path: evidence is exposed to clients/operators; any semantic audit judgment and corrective action are external to Sandbox Agent.
- Why this is / is not agent-owned: recording and rendering external-agent events is observability, not a distinct independent auditor.
- Evidence: [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md); [`docs/inspector.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/inspector.mdx); [`docs/session-persistence.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/session-persistence.mdx).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: clients may persist and audit the normalized event stream elsewhere; that external audit organization is not first-party S3* closure.

### Absence scope

- Surfaces inspected: Inspector; universal events; SSE/history; process logs; persistence and replay docs; tests/debug interfaces.
- Plausible first-party paths checked: Inspector audit/debug; event replay; permission history; process logs; restoration context replay.
- Why no material first-party path remains: the reviewed distribution provides evidence access but no independent semantic challenge owner plus findings→control feedback loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: supported agents/protocols, runtime connectivity and persisted session context can change, but adaptation choices are made by maintainers, operators, clients or external agents.
- Decisive decision or feedback right: interpret external/future change, generate adaptation options and select one that returns into present organizational capability.
- Decision owner: not established as a first-party S4 owner.
- Supporting / enforcement mechanisms: agent registry/installers; version detection; session persistence/restoration; configuration endpoints; compatibility adapters; roadmap/maintainer changes.
- Closure path: no autonomous environment-model → prospective option → selected adaptation → returned capability loop was found.
- Why this is / is not agent-owned: restoration and version/adapter management preserve continuity/compatibility; they do not autonomously reason over future external change.
- Evidence: [`server/packages/agent-management/src/agents.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/agent-management/src/agents.rs); [`docs/session-restoration.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/session-restoration.mdx); [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: replaying recent events into a new external-agent session affects future operation but is memory/continuity, not S4 by itself.

### Absence scope

- Surfaces inspected: agent installation/version management; compatibility adapters; restoration/persistence; configuration; roadmap; Foundry adjacent system.
- Plausible first-party paths checked: automatic agent install/update; session replay; compatibility normalization; runtime remediation; roadmap evolution.
- Why no material first-party path remains: found mechanisms maintain compatibility or continuity from current/configured state. They do not model external/future distinctions and autonomously develop/return organizational adaptation options.

## S5 — Policy and identity

- State: —
- Function: authentication, permissions and runtime configuration constrain operation without first-party identity/ultimate-policy closure.
- Disturbance / variety regulated: access tokens, permission requests, process/desktop controls, agent mode/config, credentials and runtime limits.
- Decisive decision or feedback right: resolve an identity- or ultimate-policy-level issue and return the authoritative decision to govern subsequent operation.
- Decision owner: client/operator/maintainer; external coding agents own their own internal policy/reasoning where applicable.
- Supporting / enforcement mechanisms: HTTP token auth; permission reply API; agent modes/config options; process/runtime config; credentials; sandbox isolation.
- Closure path: externally chosen policy/permission/configuration → Sandbox Agent transport/enforcement → external agent/process operation.
- Why this is / is not agent-owned: permission transport and fixed access controls enforce decisions selected elsewhere and do not create a first-party ultimate-policy authority.
- Evidence: [`server/packages/sandbox-agent/src/router.rs`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/server/packages/sandbox-agent/src/router.rs); [`docs/agent-sessions.mdx`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/docs/agent-sessions.mdx); [`README.md`](https://github.com/rivet-dev/sandbox-agent/blob/bbc195cc3fb5a1dd9cb05d8437442768c511e17e/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a client's `always` permission reply is durable operational permission, not an evidenced identity-level S5 decision at this recursion.

### Absence scope

- Surfaces inspected: authentication; permission handling; agent modes/configuration; credentials; process/runtime limits; sandbox boundary; repository governance.
- Plausible first-party paths checked: permission `once/always/reject`; token auth; mode/config settings; process policies; maintainer governance.
- Why no material first-party path remains: all located policy decisions are ordinary access/execution choices made externally or statically configured. No first-party identity/ultimate-policy dispute → authority → returned governance loop is shipped.

## Distributed OSS parent arrangement

Repository maintainers and downstream operators can govern deployments, and client applications may impose additional workflow policy. No organization-level parent S3/S4/S5 loop is credited because the assessed standard server/SDK exposes control primitives while the decisive organizational judgments remain outside the Sandbox Agent boundary.

## Self-hosted and non-human modes

Running the server locally or inside any supported sandbox changes execution location but not ownership. The external coding agent still owns semantic task decisions, while Sandbox Agent owns process/session/transport mechanics.

## Recursion

The focal recursion is the Sandbox Agent server/SDK control plane around one managed coding-agent session. The launched coding agent is an external organization. Generic processes, permission events and transport sessions are not promoted to first-party S1 units.

## Variety and escalation

Sandbox Agent attenuates infrastructure variety by normalizing agent protocols, event schemas, lifecycle APIs, permissions, process/desktop control and restoration. Semantic coding variety remains with external coding agents. Exceptional process/session conditions are surfaced through errors/status/logs to clients/operators rather than closed by an autonomous first-party metasystem.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The boundary decision is explicit in the product description and source: Sandbox Agent is a universal adapter/control server around separately implemented coding agents. The adjacent `foundry/` system may compose higher-level organizational behavior, but Methodology 0.3.6 boundary provenance forbids borrowing that actor into the server/SDK assessment.

## Assessment summary

At the frozen revision, Sandbox Agent is a substantial agent control/execution substrate, but the open-ended semantic action-selection loop remains in external coding-agent processes. Proposed terminal disposition: `excluded-no-agentic-vsm`.

**Vector:** — · — · — · — · — · —
