---
harness_id: agentdock
project_name: AgentDock
repository: https://github.com/uvwt/agentdock
review_ref: 43b80c72fbd6b3952e7b46b311aa4eeaededdbde
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentDock

**Proposed disposition:** `excluded-no-agentic-vsm` at the first-party AgentDock Core/MCP/ACP gateway boundary. This is an architectural admission decision, not a claim that AgentDock deployments cannot perform autonomous agent work: a separately selected ChatGPT/Claude/Codex or ACP adapter can perform that work through AgentDock tools.

## Review boundary

- System in focus: the shipped open-source Go AgentDock server, MCP tool exposure, local/remote device access, optional ACP client/adapter manager, persistent task and workflow-template tools, Nexus bridge, recovery and access controls.
- Purpose and identity: provide secure, persistent, multi-device resources, tools, task state and sessions to external AI assistant clients and separately installed coding agents.
- Relevant environment: external ChatGPT/Claude/Codex model-backed callers, ACP adapter executables, configured local/remote machines, user permissions, Git workspaces, external Nexus service and its template store.
- Standard-distribution boundary: AgentDock receives tool requests, invokes deterministic Go handlers or separately started ACP processes, returns results and records state. It does not implement an internally owned general-purpose model→tool→observation→next-action reasoning loop for user tasks.
- Credited surfaces: [README](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/README.md), [server boot](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/cmd/agentdock/server.go), [MCP/ACP wiring](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/specs_acp.go), [ACP manager](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/manager.go), [ACP process boundary](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/process.go), [task tool bindings](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/specs_task.go).
- Adjacent surfaces not silently credited: ChatGPT/Claude/Codex hosted inference, adapter-implemented native coding-agent loops, assistant-side interpretation of `agentdock_context` rules, external Nexus orchestration, manually authored skills, README diagrams, automated tests and third-party MCP plugin reasoning.
- Considered modes: direct local MCP, remote Nexus-connected bridge, multi-host tool routing, optional ACP, direct task persistence and workflow-template lookup, default instructions and workspace context.
- Recursion: one AgentDock server controlling access to tools/sessions, potentially across many hosts; those external assistant sessions are not first-party S1 production cells simply by being multiplexed.
- Reviewed revision: `43b80c72fbd6b3952e7b46b311aa4eeaededdbde` (immutable intake #3047 / controller #3048).
- Observation date: 2026-11-10; Profile 0.2.4; released Methodology 0.3.8. Source-static review only; no remote device, provider model or Nexus runtime exercised.

## Repository architecture

The [README](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/README.md) explicitly depicts `ChatGPT / Claude / Codex` **above** separate AgentDock instances, connecting over MCP to machine resources. The [server](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/cmd/agentdock/server.go) starts the Go runtime, MCP endpoint and optional Nexus bridge. The [ACP adapter process](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/process.go) executes a configured external `AgentSpec.Command`, initializes the external ACP process over JSON-RPC and relays events, rather than supplying its own autonomous task policy. [ACP manager](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/manager.go) implements session records, concurrency slots, lifecycle and interruption. [ACP prompt handling](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/prompts.go) forwards the request to that adapter and tracks its events.

The [agentdock_context](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/agentdock_context.go) contains detailed instructions for a *client model* (check state, use skills, create tasks, validate). Instructions are context supplied to an external model; they are not proof the host implements the model's reasoning loop. [Workflow-template management](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/tool/task/workflow_actions.go) fetches templates via Nexus APIs and explicitly asks **the model** to compose, prune, deduplicate and order returned templates before creating a task. [Task transition store](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/taskstate/store_transition.go) enforces fixed legal transitions and validates checkpoints; the agent or user chooses the semantic steps and statuses.

Counterfactual ownership test: remove the connected assistant client and separately installed ACP coding-agent executable while retaining AgentDock's Go service, tools, skill indexes, workflow templates, remote device tunnels, task store and policies. The service can still enumerate resources, validate input and process explicit commands, but it has no endogenous model-owned mechanism to select goals, act on novel observations, and revise semantic next steps. The missing S1 decision belongs to the removed external agent.

## Operational model

- Delivered outcome: authenticated tool execution against devices, reusable contexts and skills, persistent task/session telemetry and resumable adapter operations.
- Actual action owners: human or external model selects a tool or prompt; Go handlers apply configured routing, security and transition rules; external ACP adapter (when selected) chooses internal coding actions and observes results.
- Feedback: file/command/desktop output returns via MCP to external model; ACP session events return to a client and into adapter history. AgentDock regulates transport/operation, not the substantive task's autonomous next decision.

## S1 — Operations

- State: —
- Function: no first-party-owned autonomously deciding task production cell at this server boundary.
- Disturbance / variety regulated: local machine state, process errors, disconnected hosts and task/checkpoint state are handled through configured tool handlers; semantic coding/research disturbances are addressed by external assistant/ACP agents.
- Decisive decision or feedback right: select the next file edit, command, browser interaction or deployment intervention based on the result of a previous tool; held by the MCP client model or external ACP adapter.
- Decision owner: third-party agent executable or external ChatGPT/Claude/Codex; AgentDock Go process routes, validates, records, bounds and returns.
- Supporting / enforcement mechanisms: MCP server, ACP manager, tool schemas, context/instruction indexes, local/remote transport, task store.
- Closure path: external model selects tool → AgentDock validates/executes → tool observation returned → **external model** chooses its next step; or external model requests ACP prompt → AgentDock starts/relays adapter → **adapter** runs its loop.
- Reachability: these transport paths are first-party and supported; the owner of adaptive semantic execution is explicitly outside the first-party boundary.
- Why not S1: providing an execution substrate and capability instructions does not itself implement autonomous task decision ownership. An external agent using it remains an autonomous S1 *in its own assessment*.
- Evidence: [MCP-facing description](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/README.md), [ACP adapter startup](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/process.go), [ACP prompt surface](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/specs_acp.go), [agent tool context](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/agentdock_context.go).
- Basis: source-static architectural ownership; confidence: high for shipped Go Core and ACP client, not a runtime proof of all ecosystem plugins.

### Absence scope

- Inspected: source README, server, MCP tool registration, ACP adapter spawn/manager/prompts, context instructions, workflow-template implementation and persistent task transitions.
- Plausible first-party paths: built-in ACP mode, Nexus-backed workflows, skill bootstrap, multi-device tool use and model-facing procedural guidance.
- Why no material path remains: all identified paths delegate semantic next-action choice to the external agent or caller and implement bounded service operations. Future user-authored workflows or plugin models would be a different boundary.

## S2 — Coordination

- State: —
- Function: no first-party discretionary coordination loop mediating conflicting autonomous S1 cells at this recursion.
- Disturbance / variety regulated: concurrency limits and simultaneous host sessions are regulated as resource/transport contention; not evidence of inter-agent work-cell oscillation control.
- Decisive right and owner: session slots, per-session busy behavior and remote transport are deterministic, configuration-bound server rules; conflict resolution across independent task goals remains with the external assistant/operator.
- Closure: [ACP manager](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/manager.go) admits bounded adapter runs; [prompt handling](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/acp/prompts.go) routes busy/steering events, but no first-party adaptive inter-S1 conflict policy is shown.
- Basis: structural; confidence: medium-high at this boundary.

### Absence scope

- Checked multi-device README claims, ACP concurrency and steering, task checkpoint validation and workflow template matching. None gives a resident first-party coordination actor the right to reconcile conflicting goal commitments among autonomous S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current resource/priority intervention owner.
- Disturbance / variety regulated: server health, process interruption, auth and task-state validity are handled by fixed rules rather than system-wide goal-sensitive supervision.
- Decisive right and owner: current multi-device priorities and releases are selected by the external client/operator; the store checks requested transitions.
- Closure: task creation/checkpoint/final review from client → [task handlers](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/tool/task/task_actions.go) and [store](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/taskstate/store_transition.go) validate/persist → client chooses changes; no first-party current-system discretionary return.
- Why not S3=P: providing a task dashboard and operator-controlled checkpoints is not a documented whole-current decision-return mechanism with first-party analysis and intervention proposal.
- Basis: source-static; confidence: medium-high.

### Absence scope

- Checked persistent tasks, checkpoints, final review, session recovery, multi-device manager and agentdock_context. They enforce or expose current state, but do not aggregate a supervisory model for discretionary corrective S3 choice.

## S3* — Complementary audit

- State: —
- Function: no independent first-party checker with authority to challenge and correct S1 actions.
- Disturbance / variety regulated: bad tool arguments and unsafe operations face validation/security checks; no separate audit entity performs independent task-outcome diagnosis.
- Decisive owner: static input/auth policies, external assistant or ACP adapter; none is a separate first-party auditing decision loop with corrective return.
- Closure: request policy check/permission and error reports → allow or reject; [ACP interaction](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/app/specs_acp.go) forwards permissions offered by external adapters. No complementary audit on semantic S1 results shown.
- Basis: structural; confidence: medium-high.

### Absence scope

- Checked ACP permissions, tool validation, task final review and runtime status/recovery; static safety gates and caller-declared final review are not independent verification/correction ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party ongoing external-environment sensing → future strategic adaptation → implemented operational feedback.
- Disturbance / variety regulated: changing host availability, workflows and skills are surfaced as capabilities or externally matched templates, not autonomously forecast and translated into first-party policy change.
- Decisive owner: external agent/user composes templates, refreshes skills and selects future action; [workflow-template API](https://github.com/uvwt/agentdock/blob/43b80c72fbd6b3952e7b46b311aa4eeaededdbde/internal/tool/task/workflow_actions.go) retrieves/matches persisted artifacts.
- Closure: query remote templates/context → external assistant chooses goal/steps → task state enforces; no first-party prospective adaptation act shown.
- Basis: source-static; confidence: medium-high.

### Absence scope

- Checked Nexus template match/get/get_many, skill and dynamic MCP indexes, context refresh and self-update service boot. These change tooling and metadata, but leave semantic future adaptation decisions external.

## S5 — Policy and identity

- State: —
- Function: no first-party identity-level policy reconciliation over conflicting operating/future commitments of a viable autonomous organization.
- Disturbance / variety regulated: device access, permission and credential limits are authentic security boundary controls; they are not strategic organizational-identity decisions.
- Decisive right and owner: administrator configuration, security rules, external assistant/operator; runtime enforces these settings and adapter-offered permission choices.
- Closure: auth/access policy → validate/reject a request; no first-party model-backed reconciliation of S3/S4 demands into organizational identity and mandate.
- Basis: structural; confidence: medium-high.

### Absence scope

- Checked ACP interaction policy, server configuration/auth, context rules and task-state contracts. Neither stable instructions nor static permissions establish whole-organization S5 autonomy.

## Recursion

At the considered server recursion, AgentDock is a durable multi-device capability and ACP session platform for autonomous clients. Individual installed clients may themselves form viable agent harnesses; this assessment neither denies their functions nor attributes them to the Go server. Nexus cloud services are adjacent and not audited as an inseparable first-party distributed VSM.

## Variety and escalation

AgentDock is strong at transport, isolation, device/tool variety and crash recovery. Its source-visible fail-closed state transitions and adapter separation may reduce operational hazards, but they do not substitute for a first-party semantic S1 owner. Escalation for planning, ambiguous tool results and cross-task conflicts returns to the connected assistant or user.

## Evidence gaps

- No live MCP/ACP/model/device execution was performed; operation and test success are not inferred from source.
- Separate Nexus backend and external adapter internals were not assessed as first-party functions.
- No assertion that zero future plugin, external skill or custom mode could supply a semantic model loop; such a changed product boundary merits a new assessment.
- Re-review if the first-party distribution ships its own runnable decision-owning general agent loop or endogenous metasystem, not merely additional tool and session management.
