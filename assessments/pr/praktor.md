---
harness_id: praktor
project_name: Praktor
repository: https://github.com/mtzanidakis/praktor
review_ref: 194025ff7f1451bb20d301bb8dc26818133eb450
reviewed_at: 2026-11-16
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

# Praktor

## Review boundary

- System in focus: The self-hosted Praktor gateway, its packaged agent runner, scheduled-task and swarm execution, and Mission Control.
- Purpose and identity: Operate named personal and specialist agents for interactive and scheduled tasks, and compose bounded multi-agent runs.
- Relevant environment: Telegram and web clients, optional email, self-hosted Docker and NATS, an operator, and separately installed Claude Code/provider services.
- Standard-distribution boundary: The repository's standard gateway, runner and UI wired by the documented Docker deployment. External model inference and tools are dependencies reached through this arrangement.
- Credited operating / distribution surfaces: Agent runner and session loop, gateway scheduling and container management, graph coordinator and Mission Control.
- Adjacent first-party surfaces excluded from ownership: Repository development, CI, external provider internals, custom extensions and independently deployed connected services.
- First-party operating / deployment modes considered: Named interactive agents, scheduled tasks, and fan-out, pipeline and collaborative graph runs. Operator controls over named agents are included.
- Recursion level: One self-hosted installation with separately named active agent cells and ephemeral swarm roles.
- Reviewed revision: `194025ff7f1451bb20d301bb8dc26818133eb450`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Praktor's Go gateway connects messages and events to agent containers over NATS. Its TypeScript runner starts or resumes Claude query sessions, streams effects, and returns task results. The swarm coordinator builds a tiered graph and runs isolated roles. Mission Control serves agent and task state and lifecycle operations. Workspace volumes hold local agent data and shared global instructions mount read-only. [`README.md`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/README.md), [`agent-runner/src/index.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/index.ts#L798-L883), [`internal/swarm/coordinator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/coordinator.go#L102-L215), [`internal/container/mounts.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/container/mounts.go#L12-L40), [`internal/web/api.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/web/api.go#L77-L121).

## Operational model

Named agents and graph roles perform tool-backed local work and return results. The model has task-local decision rights. The gateway routes work and runs graphs from the submitted topology. The deployment operator can select which named agents operate and manage recurring commitments.

## S1 — Operations

- State: A
- Function: Perform delegated interactive, scheduled or graph-role tasks.
- Disturbance / variety regulated: Changing messages, external tool outcomes, and persistent session context.
- Decisive decision or feedback right: Choose operational tool actions and responses within the assigned task and allowed tool boundary.
- Decision owner: The model-backed Claude agent working through the shipped runner.
- Supporting / enforcement mechanisms: Gateway and router, Docker lifecycle, NATS, session bridge, prompt construction and allowed-tools configuration.
- Closure path: Runner sends or resumes a turn, carries tool/session results through the stream, then publishes response or completion for the gateway and caller.
- Why this is / is not agent-owned: Without the model-backed actor the gateway can transport or route a task but cannot choose and execute its responsive actions.
- Evidence: [`Dockerfile.agent`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/Dockerfile.agent), [`agent-runner/src/index.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/index.ts#L800-L883), [`agent-runner/src/session-run.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/session-run.ts), [`internal/swarm/coordinator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/coordinator.go#L270-L397)
- Basis: structural
- Confidence: High
- Caveats: Inclusion covers the first-party runner plus its documented external runtime dependency. Provider internals and arbitrary custom tools remain outside scope.
- Boundary reachability: The documented agent image installs the runtime and packages this runner. The gateway starts named containers and sends requests over the wired bus.

## S2 — Coordination

- State: —
- Function: Attenuate destructive interaction between distinct live operational agents.
- Disturbance / variety regulated: Peers can share work context or be given the same writable workspace, and differently tasked roles can compete over work.
- Decisive decision or feedback right: No evidenced first-party mechanism allocates conflicting peer commitments or resolves contested workspace edits.
- Decision owner: Run submitter sets topology and workspace. Agents choose collaboration messages or local actions.
- Supporting / enforcement mechanisms: Separate workspaces when configured distinctly, tier ordering, and group chat scoped to a graph run.
- Closure path: Output travels into dependent prompts and chat history into later collaborations. Shared-workspace collisions have no dedicated arbitration return path.
- Why this is / is not agent-owned: Fixed topology enforces user-described execution. Shipped chat transports role messages, while local same-session guards serialize work within one role.
- Evidence: [`internal/swarm/graph.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/graph.go#L19-L162), [`internal/swarm/coordinator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/coordinator.go#L121-L264), [`agent-runner/src/mcp-swarm.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/mcp-swarm.ts), [`internal/container/mounts.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/container/mounts.go#L12-L31), [`ui/src/pages/Swarms.tsx`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/ui/src/pages/Swarms.tsx#L65-L89)
- Basis: structural
- Confidence: Medium
- Caveats: The caller can define separate volumes or explicit team conventions. That application-level organization is outside the reviewed runtime.

### Absence scope

- Surfaces inspected: Swarm topology and tests, runtime invitations and channel, named message queues, workspace mounts, and workspace mapping in swarm creation.
- Plausible first-party paths checked: Concurrent edits under the same workspace name, directed prerequisite waiting, bidirectional chat, and same-session turn serialization.
- Why no material first-party path remains: Workspace volumes are keyed by supplied workspace and may be shared; the runtime provides no shared-writer claims or collision response. Graph barriers implement submitted task dependencies, and the collaboration channel supplies no decision or feedback path specific to interference.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the live portfolio of named agents under the installation operator.
- Disturbance / variety regulated: An agent may keep doing work or retain queued messages when its current commitment should be withdrawn.
- Decisive decision or feedback right: From the installation view, select a managed named agent to start or stop and withdraw its live or buffered work.
- Decision owner: The authorized deployment operator using Mission Control.
- Supporting / enforcement mechanisms: Agent definitions and running registry, returned state, deployment UI, queue cleanup, container lifecycle and stop event.
- Closure path: The operator's stop is delivered to the gateway, removes session and pending work and requests container stop/removal. Mission Control refetches the registry. Later agent starts and task delivery use the updated running state.
- Why this is / is not agent-owned: The graph coordinator runs a configured topology and the container manager implements an operator decision. No shipped model has the same system-level operating right.
- Evidence: [`internal/web/api.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/web/api.go#L77-L121), [`internal/web/api.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/web/api.go#L199-L242), [`internal/agent/orchestrator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/agent/orchestrator.go#L1026-L1035), [`internal/container/manager.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/container/manager.go#L344-L379), [`ui/src/pages/Agents.tsx`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/ui/src/pages/Agents.tsx#L125-L154)
- Basis: structural
- Confidence: High
- Caveats: This credited mode concerns the named-agent portfolio. It does not imply live graph rewiring or guaranteed stop success under a Docker failure.
- Boundary reachability: The standard self-hosted gateway serves the named agent roster and Start/Stop actions used by the installed UI.
- Whole-system current view: The definitions endpoint joins the installation's named agents with actual running containers. The UI distinguishes running and stopped agents.
- Current-control decision scope: Start or stop chosen named units and remove the selected unit's active and pending work from the gateway.

## S3* — Complementary audit

- State: —
- Function: Challenge agent outcome reports through distinct evidence access and corrective feedback.
- Disturbance / variety regulated: An output summary or normal tool result can miss effects in an agent workspace.
- Decisive decision or feedback right: No shipped independent outcome audit with a corrective return.
- Decision owner: Graph roles produce results. The coordinating runtime records them, and an operator or role may inspect ordinary reports.
- Supporting / enforcement mechanisms: Events, logs, stored messages, SQLite, UI and final lead-agent synthesis.
- Closure path: The lead may consume returned summaries for synthesis. Runtime logs feed visibility.
- Why this is / is not agent-owned: Lead synthesis and monitoring are routine paths. A caller-authored reviewer needs an independent evidence and feedback relationship supplied by that caller.
- Evidence: [`internal/swarm/coordinator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/coordinator.go#L142-L214), [`internal/swarm/coordinator.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/coordinator.go#L230-L264), [`internal/web/api.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/web/api.go#L136-L160), [`internal/swarm/graph_test.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/swarm/graph_test.go)
- Basis: structural
- Confidence: High
- Caveats: Repository tests and CI assess implementation behavior in the development boundary.

### Absence scope

- Surfaces inspected: Swarm graph and result plumbing, lead synthesis prompt, web message retrieval, stored output and core tests.
- Plausible first-party paths checked: Whether the lead reads original operational artifacts, Mission Control verifies claims against separate evidence, or a distinct review verdict drives corrective work.
- Why no material first-party path remains: The built-in lead receives predecessor/result text and emits synthesis. Live status/logs expose normal work reports. No shipped audit actor has distinct access and returned corrective scope.

## S4 — Outside-and-then intelligence

- State: —
- Function: Construct and return external-and-prospective options for future installation capability.
- Disturbance / variety regulated: Tool ecosystems, capability demands, and integration environments can change.
- Decisive decision or feedback right: No shipped decision loop selecting a forward capability option from prospective external evidence.
- Decision owner: Agents choose packages required for assigned work. An operator owns deployment changes and extension choices.
- Supporting / enforcement mechanisms: Optional Nix search/install, scheduler, memory, web access and hot config.
- Closure path: Installed packages can become usable by later commands, and changed config feeds the runtime.
- Why this is / is not agent-owned: The first-party instruction ties package selection to a tool missing for the current task. Optional persistence and scheduling provide continuity. The installation lacks a shipped prospective evaluation and adoption loop.
- Evidence: [`agent-runner/src/index.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/index.ts#L293-L309), [`agent-runner/src/mcp-nix.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/mcp-nix.ts#L81-L166), [`agent-runner/src/mcp-tasks.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/mcp-tasks.ts), [`README.md`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/README.md)
- Basis: structural
- Confidence: Medium
- Caveats: The runtime supplies real task-local tool acquisition. Deployment operators can compose periodic research or external capability evaluation.

### Absence scope

- Surfaces inspected: Prompt instructions, Nix package API, task scheduling, memory, extension management and hot configuration.
- Plausible first-party paths checked: Package search/install and persistent volume, recurring external research, skill/extension management and config reload.
- Why no material first-party path remains: The wired package loop fills an immediate task dependency. Scheduling and extension surfaces lack a first-party responsibility for comparing future capability options and returning an adaptation decision into installation-level operations.

## S5 — Policy and identity

- State: —
- Function: Maintain the identity and ultimate policy of the self-hosted organization at installation recursion.
- Disturbance / variety regulated: A named agent may need a role/persona adjustment, and the installation can receive work across different agents and access scopes.
- Decisive decision or feedback right: No supplied decision path for selecting and returning an ultimate installation mandate.
- Decision owner: Named agents and the operator can edit local role instructions. Global instructions and allowable tool scope stay deployment-authored.
- Supporting / enforcement mechanisms: Local AGENT.md, globally mounted instructions and config binding, user profile MCP, web editing.
- Closure path: Future prompts load local identity and global guidance. This returns a local persona edit and applies existing deployment policy.
- Why this is / is not agent-owned: The agent can revise its own name, style or expertise. Evidence for that locally scoped choice does not establish authority over installation-wide purpose or governing policy.
- Evidence: [`agent-runner/src/index.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/index.ts#L259-L289), [`agent-runner/src/mcp-profile.ts`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/agent-runner/src/mcp-profile.ts), [`internal/container/mounts.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/container/mounts.go#L12-L27), [`internal/web/api.go`](https://github.com/mtzanidakis/praktor/blob/194025ff7f1451bb20d301bb8dc26818133eb450/internal/web/api.go#L535-L610)
- Basis: structural
- Confidence: High
- Caveats: At a separate single-agent recursion, mutable identity warrants its own study.

### Absence scope

- Surfaces inspected: Runner prompt assembly, per-agent workspace and read-only global mount, user profile MCP, Mission Control profile editing and registry config.
- Plausible first-party paths checked: Whether an agent can change its own durable persona, whether that choice applies to peer roles, and whether installation-level mandate disputes reach an owner and come back as binding changes.
- Why no material first-party path remains: AGENT.md edits are local to the configured workspace. The global instructions and lifecycle policy are applied from deployment configuration. The runtime exposes no function-specific installation mandate decision and return process.

## Recursion

Named containers and swarm roles can be S1 operating units inside the installation. Temporary graph roles are not established as self-regulating nested viable organizations.

## Variety and escalation

Model-backed roles absorb task variation while routing, workspace partitioning, tier limits and operator intervention constrain operations. Telegram responses, event updates and Mission Control expose operational changes. The inspected source supplies no separate organizational algedonic signal path.

## Evidence gaps

This assessment used pinned source and repository tests as evidence. It did not launch a live container or provider session. The scope concerns the installation, so the narrower per-agent identity path and any caller-composed audit or adaptation stay outside these ownership states.

