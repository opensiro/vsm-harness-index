---
harness_id: edgeplane
project_name: EdgePlane
repository: https://github.com/RyanMerlin/edgeplane
review_ref: 91f7f8902de61688fb7c7f3f31a11d4ce3706a4d
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# EdgePlane

## Review boundary

- System in focus: the first-party EdgePlane control plane at frozen revision `91f7f8902de61688fb7c7f3f31a11d4ce3706a4d`, including Domains/Missions/Tasks, task claim/lease state, membership authorization, MCP/HTTP surfaces, `edgeplaned` supervision, persistent-session/ACP adapters, AgentRun records, artifact publication/provenance and Git-backed record surfaces.
- Purpose and identity: coordinate humans and heterogeneous AI-agent runtimes by providing shared organizational state, durable ownership, supervision, authorization and artifact provenance.
- Relevant environment: operators, domains/missions/tasks, supervised agent profiles, external Claude/Codex/Gemini/OpenClaw/custom runtimes, Git/object-storage targets, chat/UI clients and task/artifact consumers.
- Standard-distribution boundary: EdgePlane API, CLI/MCP bridge, daemon, task scheduling/claim machinery, supervisors, runtime adapters and provenance/control state are inside. The model-backed semantic reasoning loop of Claude, Codex, Gemini, OpenClaw or another wrapped AgentRuntime is outside; adapter/supervisor code does not inherit that runtime's organizational decision ownership.
- Credited operating / distribution surfaces: `README.md`; `crates/edgeplane`; `crates/edgeplane-tower`; `crates/edgeplaned`; current migrations and persistent task/agent state; MCP and HTTP routes; AgentRuntime abstractions/adapters; artifact publication and session supervision.
- Adjacent first-party surfaces excluded from ownership: upstream agent CLI cognition; model providers; external Git/storage/chat systems; examples/demo workers; repository CI; roadmap-only overlap detection and governance/approval engine.
- First-party operating / deployment modes considered: MCP-native interaction; `edgeplane run` external-agent launch; persistent `edgeplaned` sessions; per-agent task claim→inject→progress loops; ephemeral subagent task worker; web/CLI/API task control; artifact publishing.
- Recursion level: the EdgePlane coordination/control layer governing a fleet of separately executing agent runtimes. Those runtimes can be S1 units in a broader deployed organization, but their semantic autonomy is not first-party EdgePlane ownership.
- Reviewed revision: `91f7f8902de61688fb7c7f3f31a11d4ce3706a4d`.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

EdgePlane explicitly describes itself as a coordination/control plane rather than a workflow runner or chatbot. The first-party server owns Domains, Missions, Tasks, durable claims, membership authorization and artifact provenance. The MCP stdio bridge proxies those control-plane tools into external agents.

The daemon adds substantial autonomous lifecycle behavior but preserves the same boundary. `AgentRuntime` is a pluggable interface whose implementors wrap specific CLI runtimes. The per-agent task loop polls/claims a ready task, injects it into that runtime, forwards progress and marks lifecycle state from the runtime's completion. The separate ephemeral task worker states its execution path directly: enroll/claim/create worktree/start AgentRun, then spawn `claude -p "<prompt>"` and close task/run state on subprocess exit. The Claude ACP implementation opens an external Claude agent session and forwards the generated prompt.

Counterfactual owner test: remove Claude/Codex/Gemini/OpenClaw/custom runtime executables and their model-backed semantic loops while retaining EdgePlane's API, MCP server, daemon, scheduler/claims, supervisors, authorization and artifact ledger. EdgePlane can still represent and coordinate work, enforce ownership, manage leases and publish records, but it cannot interpret and execute the open-ended task itself. The decisive operational semantic loop remains outside EdgePlane.

Primary evidence:

- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/README.md
- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/crates/edgeplane/src/agent_harness.rs
- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/crates/edgeplaned/crates/edgeplaned-core/src/agent_runtime.rs
- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/crates/edgeplaned/crates/edgeplaned-bin/src/task_loop.rs
- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/crates/edgeplaned/crates/edgeplaned-bin/src/task_worker.rs
- https://github.com/RyanMerlin/edgeplane/blob/91f7f8902de61688fb7c7f3f31a11d4ce3706a4d/crates/edgeplaned/crates/edgeplaned-runtimes/src/claude_agent_acp.rs

## Operational model

A task exists inside a Domain/Mission with claim policy, capability requirements and durable state. EdgePlane or `edgeplaned` selects an eligible supervised profile, claims the task and establishes a lease. It then injects task context into a wrapped external runtime or spawns an external agent process. That runtime performs the semantic work and streams progress/results back. EdgePlane records progress, heartbeats/fences ownership, completes/fails the task, preserves AgentRun/provenance state and can publish artifacts.

## S1 — Operations

- State: —
- Function: no first-party EdgePlane autonomous semantic operational unit is established for the task work being coordinated.
- Disturbance / variety regulated: EdgePlane absorbs task availability, ownership, capability matching, leases, session lifecycle and artifact-state variety; open-ended problem interpretation and semantic action variety are absorbed by wrapped agent runtimes.
- Decisive decision or feedback right: interpret task meaning and observations, choose semantic actions/tools/content, revise from results and decide substantive completion.
- Decision owner: the external Claude/Codex/Gemini/OpenClaw/custom AgentRuntime implementation and its model-backed process.
- Supporting / enforcement mechanisms: task scan/claim, capability matching, leases/fencing, `edgeplaned`, AgentRuntime adapter, ACP/PTY process supervision, AgentRun records and progress forwarding.
- Closure path: EdgePlane identifies/claims work → task is injected into or used to launch the selected external runtime → runtime performs semantic task loop → EdgePlane records progress/result and advances durable state.
- Boundary reachability: no positive first-party S1 path claimed; the semantic actor is reached through an adapter or child process whose cognition remains external.
- Why this is / is not agent-owned: the repository explicitly wraps pluggable external runtimes. Autonomous polling and lifecycle management decide which work to dispatch, not how to solve the open-ended task.
- Evidence: `README.md`; `agent_runtime.rs`; `task_loop.rs`; `task_worker.rs`; `claude_agent_acp.rs`.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: EdgePlane's daemon is highly autonomous as infrastructure. Methodology 0.3.6 does not treat deterministic scheduling/supervision of external semantic workers as ownership of their S1 task loop.

### Absence scope

- Surfaces inspected: README architecture/current status; launcher/AgentDriver code; AgentRuntime trait; persistent task loop; ephemeral task worker; Claude ACP runtime; MCP server; task/agent HTTP routes.
- Plausible first-party paths checked: task claim loop; capability matching; AgentRun lifecycle; ACP session supervision; peer-message relay; local worktree creation; artifact publication; MCP control tools.
- Why no material first-party path remains: every inspected execution path that performs open-ended task semantics delegates to a wrapped/spawned external runtime, while first-party code owns deterministic coordination, lifecycle and state.

## S2 — Coordination

- State: —
- Function: EdgePlane implements extensive coordination mechanisms, but a qualifying first-party autonomous S2 owner is not established at this standalone boundary.
- Disturbance / variety regulated: parallel workers can race for tasks, duplicate work, collide on ownership and depend on predecessor outputs; EdgePlane regulates these disturbances through claims, leases, dependencies, capability gates and durable state.
- Decisive decision or feedback right: detect a concrete interference between distinct same-recursion S1 units, choose an attenuation response and feed it back to alter those S1 units.
- Decision owner: deterministic claim/dependency/fencing machinery over externally owned agent runtimes; no separate first-party autonomous S2 actor with first-party S1 plurality is established.
- Supporting / enforcement mechanisms: `try_claim_one`, claim leases, task transition fences, dependency/readiness state, semaphore concurrency cap, Mission/Domain scoping and ownership.
- Closure path: task/control state exposes eligibility/contention → deterministic rules accept one claim, defer others or hold dependent work → external runtimes receive or do not receive work.
- Boundary reachability: no positive first-party S2 path claimed because the relevant operational S1 units are external runtimes and cannot be borrowed into EdgePlane ownership.
- Why this is / is not agent-owned: EdgePlane is designed to coordinate agents, but Methodology 0.3.6 requires organizational ownership to be evaluated at the fixed first-party boundary. Claims and fencing are mechanisms; the semantic S1 units they coordinate are external.
- Evidence: `README.md`; `edgeplaned-work/src/claim.rs`; `task_transitions.rs`; `task_loop.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: in a broader deployed system containing the external agent runtimes, EdgePlane may instantiate a real S2 function. That parent arrangement is different from the standalone first-party Index boundary.

### Absence scope

- Surfaces inspected: claims/leases/fencing, capability gates, dependency handling, multi-agent daemon task dispatch, Domain/Mission organization, message relay and concurrency limiting.
- Plausible first-party paths checked: race resolution, cross-agent messages, task dependencies, capacity limiting, claim ownership and publish coordination.
- Why no material first-party path remains: the mechanisms coordinate externally owned agent runtimes; no distinct first-party autonomous S1 plurality and separately owned S2 decision loop is established.

## S3 — Inside-and-now control

- State: —
- Function: EdgePlane supplies current organizational state and hard lifecycle controls, but no first-party autonomous whole-system current-control decision owner is established.
- Disturbance / variety regulated: current task status, agent presence/status, stale leases, process/session failures, domain membership, retry/failure and concurrency availability.
- Decisive decision or feedback right: choose discretionary whole-system current commitments/priorities/resources or exceptional interventions for the organization.
- Decision owner: operators/configuration and deterministic task/daemon rules; external agents decide their task semantics.
- Supporting / enforcement mechanisms: Domain/Mission/Task API state, daemon supervision, leases, watchdog modes, restart/context-clear/message routes, status/heartbeat, claim policies and current fleet UI.
- Closure path: configured/current state triggers deterministic claim/supervision behavior or an operator issues a control action → EdgePlane enforces it → external runtime/task state changes.
- Boundary reachability: no positive autonomous S3 path claimed.
- Why this is / is not agent-owned: strong current visibility and enforcement exist, but substantive organizational discretion is not owned by a first-party autonomous supervisory actor.
- Evidence: `README.md`; `task_loop.rs`; `routes/agents.rs`; current task-transition code.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: autonomous watchdog/claim responses are bounded lifecycle policy rather than a general whole-system current-control decision owner.

### Absence scope

- Surfaces inspected: fleet/agent status, task transitions, watchdog offline modes, daemon supervision, restart/clear-context/message control, claims and current UI/API state.
- Plausible first-party paths checked: automatic failure handling, lease expiry, current capacity allocation, process restart, task retry and operator intervention.
- Why no material first-party path remains: current responses are configured/deterministic lifecycle mechanisms; no first-party autonomous actor closes discretionary whole-system control.

## S3* — Complementary audit

- State: —
- Function: EdgePlane preserves provenance, AgentRun records, Git publication history, event replay and fenced transition evidence, but no independent autonomous audit judgment loop is established.
- Disturbance / variety regulated: attribution, task ownership history, artifact provenance, process/session events and rejected transition evidence can be reconstructed.
- Decisive decision or feedback right: independently challenge operational claims through a complementary access path and return findings that alter current operation.
- Decision owner: deterministic provenance/logging/replay machinery or an external human/consumer.
- Supporting / enforcement mechanisms: AgentRun records, Git artifact ledger, publication metadata, event replay, tracing and durable task attribution/fencing.
- Closure path: evidence is recorded/exposed → operator/consumer may inspect it → any corrective action is external or separately requested.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: provenance and replay provide strong evidence but do not themselves form an independent semantic audit judgment returned into control.
- Evidence: `README.md`; task/AgentRun lifecycle; artifact publication model; ACP replay surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent auditing system could use EdgePlane's evidence to instantiate S3*, but that external judgment is not credited here.

### Absence scope

- Surfaces inspected: Git ledger/provenance, AgentRun records, progress events, session replay, task transition tracing and publication metadata.
- Plausible first-party paths checked: replay→correction, provenance→automatic intervention, audit finding→task cancellation/reassignment and independent verification of agent claims.
- Why no material first-party path remains: inspected paths persist or expose evidence; they do not autonomously make independent audit judgments and return them to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous prospective/external adaptation loop is established.
- Disturbance / variety regulated: new runtime types, changing tasks, persistent organizational knowledge and historical artifacts can be represented, but future adaptation selection remains human/developer-owned.
- Decisive decision or feedback right: sense relevant external/future change, generate options, choose an adaptation and return it into current capability.
- Decision owner: operator/developer/maintainer through configuration, runtime adapters, missions/tasks and software changes.
- Supporting / enforcement mechanisms: persistent task/artifact state, Git record, profiles/capabilities, pluggable runtime adapters and configuration.
- Closure path: humans or external agents interpret history/environment → adjust tasks/configuration/code/runtime selection → EdgePlane stores/enforces the new state.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: persistence and replay are memory mechanisms; pluggability is capability. Neither establishes an autonomous outside-and-then option-generation/selection loop.
- Evidence: `README.md`; AgentRuntime abstraction; persistent session/task/artifact surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: roadmap overlap detection is not credited; even if implemented as similarity analysis, detection alone would not establish S4 adaptation ownership.

### Absence scope

- Surfaces inspected: Git/provenance memory, session replay, task history, profiles/capabilities, runtime adapters, current roadmap and configuration paths.
- Plausible first-party paths checked: history-driven replanning, autonomous runtime/profile selection, external trend sensing, self-generated mission changes and learned organizational adaptation.
- Why no material first-party path remains: future-facing choices remain externally authored; current repository mechanisms store, route or supervise them.

## S5 — Policy and identity

- State: —
- Function: EdgePlane implements identity/membership and default-deny authorization, but no first-party autonomous ultimate-policy/identity governance loop is established.
- Disturbance / variety regulated: domain membership, owner/contributor permissions, admin access, task ownership and agent/service identities.
- Decisive decision or feedback right: authoritatively decide organizational identity or ultimate policy and return that decision to govern subsequent operation.
- Decision owner: human/operator/admin configuration and membership state.
- Supporting / enforcement mechanisms: domain owners/contributors, admin allowlists, session/service-account authentication, authorization checks and claim ownership.
- Closure path: operator/configuration sets membership/policy → EdgePlane enforces it on MCP/HTTP/task transitions → subsequent operations are constrained.
- Boundary reachability: no positive autonomous S5 path claimed.
- Why this is / is not agent-owned: default-deny enforcement is substantive, but the repository explicitly says a separate versioned governance/approvals engine is planned rather than current. Ultimate policy remains externally authored.
- Evidence: `README.md`; current authorization/task-transition routes and status/roadmap statement.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: permissions and organizational naming do not establish autonomous S5 ownership without an identity/ultimate-policy decision loop.

### Absence scope

- Surfaces inspected: membership authorization, admin allowlists, task ownership/leases, agent identities, MCP/HTTP enforcement, current roadmap.
- Plausible first-party paths checked: autonomous membership changes, constitution/policy revision, identity governance, policy conflict resolution and governance approval engine.
- Why no material first-party path remains: policy is configured by humans/admins; the richer governance/approval engine is explicitly not implemented at the frozen revision.

## Distributed OSS parent arrangement

The assessed organization is the runtime EdgePlane control plane, not its GitHub maintainer project. Contributor/release governance is not imported as runtime S3/S4/S5.

## Self-hosted and non-human modes

EdgePlane is self-hostable and can autonomously supervise/dispatch external agent processes. Those runtime agents can themselves satisfy S1 at their own boundaries. This review does not inherit Claude/Codex/Gemini/OpenClaw cognition into EdgePlane merely because first-party code launches, injects, monitors and records them.

## Recursion

At a larger deployment recursion EdgePlane can supply coordination/control mechanisms across many autonomous agents. For this repository-relative standalone assessment, those agents are separate systems and EdgePlane's own first-party machinery does not establish an autonomous semantic S1.

## Variety and escalation

EdgePlane absorbs contention, ownership, authorization, process-lifecycle, task-state and provenance variety with claims, leases, fencing, supervision and durable records. Failures are retried, fenced or surfaced to operators. This is strong orchestration infrastructure but does not change the ownership finding.

## Evidence gaps

No `?` state is required. The frozen code directly identifies the pluggable external runtime boundary and shows how task work is injected/spawned into it, while the first-party control plane owns coordination/lifecycle/state. Proposed terminal disposition: `excluded-no-agentic-vsm`.
