---
harness_id: agentsystems-control-plane
project_name: AgentSystems Agent Control Plane
repository: https://github.com/agentsystems/agent-control-plane
review_ref: f09a940d4185a44dfab7df77796641268c592e18
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentSystems Agent Control Plane

## Review boundary

- System in focus: the first-party `agentsystems/agent-control-plane` gateway/control-services repository at pinned revision `f09a940d4185a44dfab7df77796641268c592e18`, including FastAPI request routing, Docker agent discovery/start-stop lifecycle, invocation tracking, artifact staging, egress controls/proxying and audit persistence.
- Purpose and identity: front an AgentSystems deployment with a gateway that discovers separately deployed agent containers, starts/stops them, forwards invocation payloads, tracks asynchronous jobs, manages artifacts/egress and records audit evidence.
- Relevant environment: independently packaged agent containers and their model/tool reasoning loops, clients/users, Docker runtime, PostgreSQL, configured egress destinations, external services and the wider multi-repository AgentSystems platform.
- Standard-distribution boundary: code in this repository's `cmd/gateway` runtime and shipped gateway configuration is inside. The autonomous agent implementations discovered through Docker labels and reached through each container's `/invoke` endpoint are outside this repository-relative boundary.
- Credited operating / distribution surfaces: `README.md`; `cmd/gateway/main.py`; `cmd/gateway/docker_discovery.py`; `cmd/gateway/lifecycle.py`; `cmd/gateway/egress.py`; `cmd/gateway/proxy.py`; `cmd/gateway/database.py`.
- Adjacent first-party surfaces excluded from ownership: other AgentSystems repositories, agent container images/SDK implementations not present in this repository, tests/CI and future platform components. A wider multi-repository deployment would be a different system-in-focus.
- First-party operating / deployment modes considered: synchronous and asynchronous `/invoke/{agent}` gateway paths, Docker label discovery, lazy container start, manual start/stop, idle reaping, per-agent egress restrictions, artifact staging and audit/job-state persistence.
- Recursion level: this repository's gateway/control-services layer itself, as pinned in organizational/control batch #407. Discovered agent containers may supply autonomous operational units in a wider AgentSystems deployment, but their reasoning/action loops are not inherited into this repository assessment.
- Reviewed revision: `f09a940d4185a44dfab7df77796641268c592e18`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The README calls this repository the "gateway and orchestration layer" and then makes the execution boundary concrete: a client talks to the Gateway, which discovers separately running agent containers and forwards requests to them. The listed first-party modules are HTTP routing, Docker discovery, database/job management, egress allowlisting/proxying and lifecycle management.

The invocation implementation preserves that separation. `/invoke/{agent}` refreshes the external-container registry, lazily starts a matching container if needed, stages request/artifact data, records invocation state and then performs an HTTP POST to `docker_discovery.AGENTS[agent]`. The target mapping itself resolves to an agent container's `/invoke` endpoint. The gateway accepts and returns that container's result; it does not run the agent's model, choose the agent's next tool, or feed tool observations through an internal reasoning loop.

Lifecycle automation also regulates containers rather than operational objectives. The idle reaper periodically compares last-invocation timestamps with configured timeout values and stops containers that exceed the threshold. Manual start/stop endpoints, egress allowlists, job-state persistence and hash-chained audit records similarly control deployment/runtime mechanics around external actors.

A repository-wide negative search at the pinned revision did not establish a first-party LLM/model-agent loop in this control-plane repository. No standard-distribution path remains that can take an objective and autonomously decide and execute substantive model/tool actions once the discovered agent containers are removed.

Counterfactual owner test: remove the external agent containers while leaving the gateway, discovery registry, lifecycle controller, egress proxy, database and audit paths intact. The remaining first-party system can list/start/stop hypothetical agents, accept requests, enforce transport constraints and record lifecycle/audit state, but there is no actor capable of pursuing the requested objective. Operational S1 therefore closes outside the assessed repository boundary.

Under Methodology `0.3.6`, control-plane richness around external agents cannot substitute for first-party S1. The proposed terminal result is therefore `excluded-no-agentic-vsm`; S2-S5 primitives are not separately published once the qualifying operational organization is outside the boundary.

Primary evidence:

- [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md) — gateway role, platform diagram, Docker-discovered agents, forwarding, audit and module responsibilities.
- [`cmd/gateway/main.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/main.py) — invocation endpoint, lazy start, artifact/job handling and direct HTTP forwarding into the selected agent container.
- [`cmd/gateway/docker_discovery.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/docker_discovery.py) — agent-container discovery and `/invoke` endpoint mapping.
- [`cmd/gateway/lifecycle.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/lifecycle.py) — threshold-based idle container stopping and activity bookkeeping.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop is established inside this repository boundary.
- Disturbance / variety regulated: the gateway regulates request transport, container availability, artifact movement, outbound connectivity and invocation lifecycle; substantive task uncertainty is handled by the selected external agent container.
- Decisive decision or feedback right: interpret the invocation objective, choose substantive model/tool actions, observe their results and decide what operational action follows.
- Decision owner: the external discovered agent container/runtime, not the AgentSystems control-plane repository.
- Supporting / enforcement mechanisms: request routing, Docker discovery/lazy start, job records, artifact directories, egress allowlists/proxy, audit log and lifecycle tracking.
- Closure path: client request → first-party gateway prepares/tracks invocation → gateway POSTs payload to external agent `/invoke` → external agent performs the goal-directed work → gateway stores/returns its response. No internal model/tool feedback loop intervenes between these steps.
- Boundary reachability: the README deployment diagram and `docker_discovery.AGENTS` mapping both make the agent container a separate network target; the gateway remains deployable infrastructure rather than the agent implementation.
- Why this is / is not agent-owned: the repository can decide whether/how an external actor is reachable, but it does not own the autonomous task-level decision loop that produces the actor's work.
- Evidence: [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md); [`cmd/gateway/main.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/main.py); [`cmd/gateway/docker_discovery.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/docker_discovery.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a complete AgentSystems deployment containing this gateway plus one or more agent repositories may establish S1 and higher functions; that composed multi-repository system is not the declared repository-relative boundary.

### Absence scope

- Surfaces inspected: README architecture, gateway request paths, Docker discovery, lifecycle management, egress proxy/allowlist, database/audit/job tracking and repository-wide model/runtime dependency search.
- Plausible first-party paths checked: gateway as agent runtime; background worker as autonomous agent; lifecycle reaper as operational loop; Docker orchestrator as S1; audit/job worker as agent.
- Why no material first-party path remains: all inspected first-party loops manage infrastructure or forward work to an external `/invoke` actor; none performs goal-directed model/tool reasoning itself.

## S2 — Coordination

- State: —
- Function: no first-party S2 coordination function is established at the declared boundary because the autonomous S1 units being discovered/routed are external to this repository.
- Disturbance / variety regulated: registry refresh and lifecycle controls can prevent stale/unavailable endpoints; transport routing can select a named agent, but no specific interference between internal first-party S1 units is identified and attenuated.
- Decisive decision or feedback right: no internal S2 coordination decision over competing first-party operational units is established.
- Decision owner: none established inside this repository.
- Supporting / enforcement mechanisms: Docker discovery registry, agent name routing, start/stop state and invocation records.
- Closure path: client names an external agent → gateway resolves/starts/routes to it. This is service discovery/routing, not an evidenced S2 anti-interference relation among internal S1 units.
- Why this is / is not agent-owned: multiple agent endpoints and routing do not establish S2 by themselves, especially when the operational units lie beyond the assessed boundary.
- Evidence: [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md); [`cmd/gateway/main.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/main.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a wider platform deployment may implement inter-agent coordination elsewhere; no such function is inherited into this repository.

### Absence scope

- Surfaces inspected: registry/discovery, invocation routing, lifecycle, async worker/job state and gateway configuration.
- Plausible first-party paths checked: discovery as S2; named routing as S2; async invocation tracking as S2; container lifecycle as coordination.
- Why no material first-party path remains: these paths manage endpoints and request mechanics without a function-specific relation that attenuates disturbance between internal autonomous S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous first-party whole-system current-control owner is established for an internal operational organization.
- Disturbance / variety regulated: container idleness, stopped/running state, egress destinations, request/job lifecycle and gateway availability.
- Decisive decision or feedback right: no evidence establishes a first-party manager deciding operational priorities, commitments, shared resources or interventions across internal S1 units.
- Decision owner: operators/configuration and deterministic gateway/lifecycle rules.
- Supporting / enforcement mechanisms: manual start/stop, lazy start, idle timeout, egress allowlist, job-state transitions and audit persistence.
- Closure path: configured threshold/operator request/current request state → deterministic infrastructure action → external agent container availability changes. This is deployment control, not autonomous organizational current-control over first-party S1 work.
- Why this is / is not agent-owned: lifecycle authority over containers is materially real but remains deterministic infrastructure management around external operational actors, not the whole-current S3 function at this recursion.
- Evidence: [`cmd/gateway/lifecycle.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/lifecycle.py); [`cmd/gateway/main.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/main.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: the wider AgentSystems platform may use this gateway as an S3 enforcement surface, but a function-specific owner/closure over a qualifying operational whole is not present in this repository alone.

### Absence scope

- Surfaces inspected: lifecycle controller, discovery registry, job state, egress controls, start/stop endpoints and audit data.
- Plausible first-party paths checked: idle reaper as manager; lazy start as resource allocation; egress policy as control; job database as whole-system view.
- Why no material first-party path remains: actions are threshold/request/config driven and govern external containers; no internal autonomous current-control judgment is evidenced.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit of operational reality is established at this repository boundary.
- Disturbance / variety regulated: request/response and lifecycle facts are recorded for audit, but recording is not a separate actor independently challenging operational claims.
- Decisive decision or feedback right: no independent reviewer/verifier decides that first-party S1 reality contradicts reported state and returns corrective action into S3/S1.
- Decision owner: not established.
- Supporting / enforcement mechanisms: append-only/hash-chained audit rows, invocation/job records and tests.
- Closure path: gateway records request/result/status facts; no independent runtime audit path with corrective return is evidenced.
- Why this is / is not agent-owned: an audit log is evidence infrastructure, not S3* solely by being called audit or being tamper-evident.
- Evidence: [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md); [`cmd/gateway/database.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/database.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: external auditors can consume the persisted evidence, but their organizational role is outside this repository.

### Absence scope

- Surfaces inspected: audit persistence, invocation result/error recording, health/metadata endpoints, tests and lifecycle state.
- Plausible first-party paths checked: hash chain as S3*; job status as operational audit; health endpoints as audit.
- Why no material first-party path remains: these surfaces preserve or expose same-path state without an independent corrective audit actor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective sensing and persistent adaptation loop is established.
- Disturbance / variety regulated: configuration can change available agents, egress rules and lifecycle limits, but those changes are authored by maintainers/operators.
- Decisive decision or feedback right: choose future capabilities or redesign based on an external/future model.
- Decision owner: external developers/operators.
- Supporting / enforcement mechanisms: configuration loading, discovery refresh and deployment updates.
- Closure path: operator/developer changes configuration or deployed containers → gateway subsequently discovers/enforces the new state. The adaptation judgment itself is outside the first-party runtime.
- Why this is / is not agent-owned: dynamic discovery is sensing of current deployment state, not future-oriented organizational intelligence or option development.
- Evidence: [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md); [`cmd/gateway/docker_discovery.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/docker_discovery.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: ordinary software evolution in other repositories is not credited as runtime S4.

### Absence scope

- Surfaces inspected: configuration, discovery/watch paths, lifecycle state, egress configuration and repository docs.
- Plausible first-party paths checked: Docker watch as environmental sensing; registry refresh as learning; dynamic configuration as adaptation.
- Why no material first-party path remains: these mechanisms track/apply externally authored current deployment state and do not develop prospective adaptation options.

## S5 — Policy / identity

- State: —
- Function: no first-party identity/ultimate-policy deliberation and closure path is established.
- Disturbance / variety regulated: bearer-token placeholder, egress allowlists, agent labels/configuration and lifecycle settings constrain gateway operation.
- Decisive decision or feedback right: decide the organization's durable mission, identity and ultimate governing policy.
- Decision owner: external platform operators/configuration authors.
- Supporting / enforcement mechanisms: configuration files, egress allowlist, auth placeholder, agent labels and manual lifecycle endpoints.
- Closure path: external authority supplies policy/configuration → gateway enforces it. No first-party S5 actor deliberates identity-level matters and returns authoritative decisions into operation.
- Why this is / is not agent-owned: configured policy enforcement and administrative control do not establish S5 merely because the repository is called a control plane.
- Evidence: [`README.md`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/README.md); [`cmd/gateway/main.py`](https://github.com/agentsystems/agent-control-plane/blob/f09a940d4185a44dfab7df77796641268c592e18/cmd/gateway/main.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a parent organization may legitimately supply S5 for a wider AgentSystems deployment; generic operator ownership is not enough to publish `P` for this repository without a function-specific authority/return loop.

### Absence scope

- Surfaces inspected: gateway configuration, auth, egress controls, container labels, lifecycle endpoints and platform-boundary documentation.
- Plausible first-party paths checked: gateway configuration as policy; bearer auth as identity; egress allowlist as S5; operator start/stop as ultimate authority.
- Why no material first-party path remains: these are externally authored operational/security constraints without an internal identity-level decision loop.

## Terminal outcome

`excluded-no-agentic-vsm`.

AgentSystems Agent Control Plane is substantive infrastructure for deploying and governing separately packaged agents, but its first-party repository boundary terminates at discovery/lifecycle/forwarding/audit services. The autonomous goal-directed agent loop lives in external containers, so the repository does not establish first-party S1 required for Index inclusion.

## Evidence boundaries / caveats

- The word `orchestration` in product positioning is not used as a VSM classification shortcut.
- Container start/stop, idle reaping and egress enforcement are treated as infrastructure/lifecycle control unless a function-specific organizational owner/closure is evidenced.
- Hash-chained audit storage is not treated as S3* without independent challenge and corrective feedback.
- Other AgentSystems repositories are not silently imported into this repository-relative assessment.
