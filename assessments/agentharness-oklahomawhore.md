---
harness_id: agentharness-oklahomawhore
project_name: AgentHarness
repository: https://github.com/Oklahomawhore/AgentHarness
review_ref: 6bedcf45fad75e21df5e5cac827a898ef5c7d228
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentHarness

## Review boundary

- System in focus: one first-party AgentHarness / DeepSeek Harness distribution at pinned revision `6bedcf45fad75e21df5e5cac827a898ef5c7d228`, including the shipped model/tool agent loop, base-bundle subagent providers and model-facing delegation/control tools, persistent Sessions, and the Web collaboration Task/Room runtime.
- Purpose and identity: execute engineering work through a persistent model/tool harness while supporting durable child-agent delegation and an optional Task-first multi-node collaboration surface for explicit shared context.
- Relevant environment: user objectives, local workspace and processes, configured model providers, tool/MCP resources, child-agent Sessions, other Task/Room participants and remote authenticated collaboration nodes.
- Standard-distribution boundary: shipped TUI/Web/headless/base-backed product compositions at the frozen ref. The repository is a fork lineage, but the assessed object is the implementation distributed by this repository at the pinned revision; external upstream development does not independently own functions inside the assessed deployment.
- Credited operating / distribution surfaces: core Agent turn/step runtime; base bundle; `dsh-subagent` plus bundled spawn/fork providers; model-facing `subagent`, `send_message`, `interrupt_agent` and `list_agents`; Session persistence; Web Task/Room collaboration packages; Task-context injection into native Agent requests.
- Adjacent first-party surfaces excluded from ownership: `agentharness/` evidence adapters; acceptance/snapshot harnesses; repository CI, tests and release scripts; `.agents` development notes except as corroboration of shipped source/configuration; experimental packages not mounted by the supported product composition; opt-in model-facing session-query tools that the shipped TUI/Web/headless compositions explicitly do not mount.
- First-party operating / deployment modes considered: ordinary single-agent model/tool operation; foreground one-shot subagents; bundled continuable background `spawn` children with follow-up control; fork children; shipped Web Task/Room collaboration and multi-node Task replication.
- Recursion level: one AgentHarness deployment/session organization. The root Agent and its separately persisted child-agent Sessions are distinct S1 units for S2/S3 analysis. Task/Room participants may span nodes, but Task lineage and membership alone are not promoted to higher-recursion viability.
- Reviewed revision: `6bedcf45fad75e21df5e5cac827a898ef5c7d228`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AgentHarness ships a persistent Agent turn/step loop. User/follow-up input is admitted into a Session, the runtime assembles instructions and request context, calls the selected LLM, records the assistant response, executes model-selected tools, appends ordered tool results and either advances to another step or closes the turn. The Session event log is the durable replay surface while `agent/*` carries live status, steering and lifecycle signals.

The shared base bundle also mounts the subagent service, in-process spawn and fork providers, a continuable `subagent` tool, and the global `send_message`, `interrupt_agent` and `list_agents` control tools. Continuable children are separate durable Sessions. The parent can launch children, enumerate the complete continuable descendant tree with `running` / `idle` / `ready` status, send follow-up input and interrupt a child's current turn without deleting its durable identity or descendants.

Parallel delegation is deliberate. The shipped continuable-tool guidance tells the model to start independent delegations together. The implementation permits sibling delegations to overlap against the shared workspace and explicitly records that sibling workspace effects can race; the product assigns that coordination judgment to the model rather than pretending the runtime can infer safe disjoint effects from free-text tasks. Results/settlement notices, the live child roster and follow-up/interrupt surfaces close feedback back into the parent model's later decisions.

The separate Web collaboration runtime organizes humans and Agents around an immutable Root/Fork/Merge Task DAG. Each Agent Session has an explicit Task binding; current Task context is injected at `agent/pre-step` as replayable user-role context. Hidden Rooms provide membership, while Task context remains the durable product object. This is useful shared organizational context but is not itself credited as S2/S3 without the stronger subagent control relations above.

Primary evidence:

- [`docs/agent-lifecycle.md`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/docs/agent-lifecycle.md) — shipped model/tool turn and feedback lifecycle.
- [`packages/bundle/base/cordis.patch.yml`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/packages/bundle/base/cordis.patch.yml) — standard base composition, including subagent providers and model-facing child-control tools.
- [`packages/subagent/tool-subagent/README.md`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/packages/subagent/tool-subagent/README.md) — delegation lifecycle, continuable background mode and model-visible independent-delegation guidance.
- [`packages/subagent/tool-subagent-control/README.md`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/packages/subagent/tool-subagent-control/README.md) — model-facing child listing, steering and interruption semantics.
- [parallel-subagent implementation decision](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/.agents/notes/archived/feature/2026-08-09-parallel-subagent-delegations.md) — implemented shared-workspace sibling-race boundary and model-owned coordination responsibility, corroborated by shipped tool/bundle behavior.
- [`docs/subsystems/development-room.md`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/docs/subsystems/development-room.md) — Task-first collaboration boundary and hidden Room membership runtime.
- [`packages/collaboration/development-task/src/index.ts`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/packages/collaboration/development-task/src/index.ts) — immutable Task lineage, explicit publications, Agent-session assignment and Room reconciliation.
- [`packages/collaboration/development-task-context/src/index.ts`](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/packages/collaboration/development-task-context/src/index.ts) — current Task snapshot injection into native Agent model context and revision acknowledgement.
- [session-query default decision](https://github.com/Oklahomawhore/AgentHarness/blob/6bedcf45fad75e21df5e5cac827a898ef5c7d228/.agents/notes/archived/feature/2026-08-02-session-search-not-shipped-default.md) — confirms the complementary model-facing session-query consumer is opt-in and absent from shipped TUI/Web/headless compositions.

## Operational model

The active model is the S1 owner. It chooses substantive tools, arguments and continuation from user/session/tool evidence. In the shipped continuable multi-agent mode, the same parent model also decides decomposition and which tasks are sufficiently independent to overlap, then receives child lifecycle/result feedback and can steer or interrupt current children. Runtime scheduling, persistence, depth limits and authorization enforce those decisions without becoming their organizational owner.

The Task/Room layer supplies explicit shared context and durable cross-node lineage. It does not claim task completion, approval or audit authority, and the documentation explicitly describes Task as a context atom without lifecycle, evidence, approval, completion or audit controls.

## S1 — Operations

- State: A
- Function: perform user-directed engineering work through repeated model-selected tool actions and feedback.
- Disturbance / variety regulated: changing user objectives, workspace/process state, tool outcomes and failures, model context pressure, follow-up input, child outcomes and external tool/provider responses.
- Decisive decision or feedback right: choose the next substantive tool/action and revise the next step from returned evidence, or conclude the turn.
- Decision owner: the active Agent model in the root Session; child models own the same local operational discretion within delegated child Sessions.
- Supporting / enforcement mechanisms: Agent driver, Session event log, tool registry/execution scheduler, sandbox and approval services, LLM adapters, compaction/retry hooks and persistence.
- Closure path: admitted user/session context → model request → assistant tool call/action → runtime execution → ordered `tool/result` / durable event → next model step observes the result and chooses a revised action or final response.
- Boundary reachability: the Agent loop and core tools are mounted by the standard base-backed TUI/Web/headless product compositions.
- Why this is / is not agent-owned: removing the model removes the task-specific choice of tool, arguments, sequencing and stopping point; deterministic runtime machinery validates, schedules and executes those choices but does not make materially equivalent operational judgments.
- Evidence: `docs/agent-lifecycle.md`; `packages/bundle/base/cordis.patch.yml`.
- Basis: explicit + structural
- Confidence: high
- Caveats: sandbox, approvals, retry and compaction are supporting regulation, not S1 ownership.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrently operating child Agents sharing the same workspace by deciding which delegated work is sufficiently independent to overlap and by revising/steering work when current child state requires coordination.
- Disturbance / variety regulated: sibling child Sessions can run concurrently against one shared workspace or external resources and can race or invalidate one another when their effects overlap.
- Decisive decision or feedback right: choose task decomposition and whether multiple child commitments are independent enough to launch together; subsequently message or interrupt continuable children as coordination needs change.
- Decision owner: the parent Agent model.
- Supporting / enforcement mechanisms: parallel-safe delegation execution, separate child Sessions/identities, ordered parent result commit, durable continuable child identities, `send_message`, `interrupt_agent`, settlement notices and `maxParallelToolCalls` enforcement.
- Closure path: parent model identifies independent work → emits multiple `subagent` delegations together (or keeps dependent work sequential) → children operate concurrently in separate Sessions against the shared environment → settlement/status/message evidence returns to parent context → parent may steer/interrupt/redelegate or change its own subsequent work.
- Boundary reachability: the base bundle mounts the continuable `subagent` tool and its fixed model-visible guidance to "Start independent delegations together", along with the follow-up control surface; the shared-workspace race is an implemented/shipped behavior rather than test-only topology.
- Why this is / is not agent-owned: the scheduler treats delegation as concurrency-safe and cannot infer whether free-text child tasks have disjoint workspace effects; the project explicitly leaves sibling workspace coordination to the model. Removing that model judgment leaves only unconditional overlap/caps, not materially equivalent task-specific coordination.
- Evidence: `packages/subagent/tool-subagent/README.md`; `packages/subagent/tool-subagent-control/README.md`; `packages/bundle/base/cordis.patch.yml`; `.agents/notes/archived/feature/2026-08-09-parallel-subagent-delegations.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the runtime does not provide a write-lease conflict solver; S2 credit is for the model-owned independence/timing/steering relation, not for the generic mailbox or parallel scheduler.
- Distinct S1 units: root Agent plus two or more separately persisted child-agent Sessions, each with its own model/tool operation and durable identity.
- Inter-S1 disturbance: concurrent sibling children can race on shared workspace files or external resources and thereby invalidate or interfere with peer work.
- Attenuating coordination relation: parent-model decomposition/independence judgment determines what is co-scheduled; continuable children can then receive model-selected follow-up steering or interruption.
- Feedback into subsequent S1 behaviour: child settlement notices, `list_agents` status and accepted messages/interrupts feed current child outcomes into later parent decisions; follow-up input changes child execution at a later step boundary.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation is tied to the repository's explicit shared-workspace sibling-race disturbance and changes which child commitments overlap or are subsequently steered; Task/Room messaging alone is not credited.

## S3 — Inside-and-now control

- State: A
- Function: maintain current control over the root Agent's active continuable child organization: create commitments, observe the current descendant portfolio and intervene in live child work.
- Disturbance / variety regulated: changing child lifecycle state, completed/failed/idle/running commitments, new information requiring follow-up, runaway or no-longer-useful child work, and current need to change delegated effort.
- Decisive decision or feedback right: create children with task/persona/tool/model/depth commitments, inspect the continuable descendant tree, send task-changing follow-up input and interrupt a child's current turn.
- Decision owner: the parent Agent model for its current child organization.
- Supporting / enforcement mechanisms: durable child catalog and Session identities, continuation manager, live Agent registry, authorization/lineage checks, `list_agents`, `send_message`, `interrupt_agent`, settlement notices and depth/capacity enforcement.
- Closure path: parent creates current child commitments → `list_agents`/settlement notices expose current descendant status → parent chooses follow-up, interruption, additional delegation or its own integration action → runtime delivers/enforces the choice → subsequent child/root operation changes.
- Boundary reachability: the shipped base bundle mounts continuable spawn children and all three model-facing control tools; no custom downstream controller is required for this mode.
- Why this is / is not agent-owned: lifecycle and authorization services enforce identity and interruption, but they do not decide which child should be started, redirected or stopped for the current objective. Those task-specific current-control decisions belong to the parent model.
- Evidence: `packages/bundle/base/cordis.patch.yml`; `packages/subagent/tool-subagent/README.md`; `packages/subagent/tool-subagent-control/README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: `list_agents` intentionally excludes one-shot children. S3 is established by the supported continuable-child mode, where the root can enumerate the complete continuable descendant tree; this does not claim equivalent supervision over every optional child mode.
- Whole-system current view: for the continuable-child mode, `list_agents(scope=descendants)` walks the root's complete continuable child tree and reports durable identity, direct parent/depth and current `running`, `idle` or `ready` status; settlement notices add outcome/final-message feedback.
- Current-control decision scope: create/withhold child commitments; select task, route/persona/tool/depth settings where supported; send new work/steering to direct continuable children; interrupt current child turns; launch further work or integrate returned outcomes.

## S3* — Complementary audit

- State: —
- Function: no material shipped complementary-audit function was established that independently challenges operational reporting or completion through a distinct access path.
- Disturbance / variety regulated: potential inaccurate child claims or hidden operational failure were considered, but the standard distribution does not close an independent audit loop for them.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: none established at the assessed boundary.
- Supporting / enforcement mechanisms: Session/event durability, task status, approval logs, ordinary child transcripts/status and optional development evidence infrastructure provide observability or validation but do not form an independent complementary audit function.
- Closure path: no qualifying independent audit finding → organizational response closure was found in the shipped mode.
- Why this is / is not agent-owned: ordinary parent result/status observation is the in-band S3 path; no separate autonomous auditor or shipped audit judgment path owns a complementary verdict.
- Evidence: `packages/subagent/tool-subagent-control/README.md`; `docs/subsystems/development-room.md`; `.agents/notes/archived/feature/2026-08-02-session-search-not-shipped-default.md`.
- Basis: explicit + structural absence
- Confidence: high
- Caveats: custom compositions can opt into model-facing session-query tooling, but that consumer is explicitly absent from shipped TUI/Web/headless surfaces and generic transcript access would still require an audit judgment/closure to qualify.

### Absence scope

- Surfaces inspected: standard base bundle, Agent lifecycle, subagent/delegation/control packages, Task/Room collaboration runtime, Session-query default decision, approval/telemetry/evidence references and repository search for reviewer/audit paths.
- Plausible first-party paths checked: child result/status verification, Task/Room evidence fields, model-facing session queries, approvals, development-evidence adapters and repository test/acceptance surfaces.
- Why no material first-party path remains: the shipped multi-agent path exposes ordinary current-control reporting but no separately mounted reviewer/verifier/auditor with sufficiently independent operational access and a finding-to-control closure; model-facing session queries are explicitly opt-in rather than a shipped product capability.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop was established.
- Disturbance / variety regulated: future environmental/capability change can be researched through ordinary tools and shared Task context, but no shipped mechanism converts such intelligence into a governed change of the harness's present capability/organization.
- Decisive decision or feedback right: not established for S4.
- Decision owner: none established at the assessed boundary.
- Supporting / enforcement mechanisms: MCP/tool discovery, development-evidence providers, skills, settings, Task publications, model-route selection and compaction alter current task information/configuration but do not close a prospective adaptation function.
- Closure path: no qualifying external/prospective option → capability-change → subsequent-operation loop was found.
- Why this is / is not agent-owned: current-task research and configuration choices remain S1/support behavior; they do not grant an actor organizational adaptation authority.
- Evidence: `packages/bundle/base/cordis.patch.yml`; `docs/subsystems/development-room.md`; repository collaboration/evidence package surfaces.
- Basis: structural absence
- Confidence: medium-high
- Caveats: repository development agents and maintainer workflows can evolve AgentHarness, but those adjacent development systems are outside the standard-distribution ownership boundary.

### Absence scope

- Surfaces inspected: core/base bundle, skills/settings/model routing, MCP and development-evidence surfaces, Task/Room context flow, `.agents` development notes as adjacent evidence and product documentation.
- Plausible first-party paths checked: self-improvement/skill mutation, learned policy updates, external trend/research loop, automatic capability reconfiguration and parent-governed adaptation returning into the running harness.
- Why no material first-party path remains: the reviewed product can retrieve external information and consume configured capabilities but does not operationally close a future-oriented adaptation decision into changed current organizational capability; repository R&D workflows are adjacent to the deployed harness.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity / ultimate-policy closure is established inside the assessed harness organization.
- Disturbance / variety regulated: sandbox, approvals, system instructions, model/tool settings and profile composition constrain operation but do not constitute an S5 identity/policy issue handled by ultimate organizational authority and returned into operation.
- Decisive decision or feedback right: not established for S5.
- Decision owner: none established for S5 at this recursion.
- Supporting / enforcement mechanisms: system prompt assembly, sandbox policy, user approval, model/provider settings, profile/bundle configuration and Task context authority boundaries.
- Closure path: no qualifying identity/ultimate-policy issue → legitimate authority → authoritative policy decision → returned operational change loop was found.
- Why this is / is not agent-owned: the main model acts under configured identity and permission constraints but does not own the ultimate right to redefine the organization's identity or governing policy.
- Evidence: `packages/bundle/base/cordis.patch.yml`; `docs/agent-lifecycle.md`; approval and collaboration boundaries described in repository documentation.
- Basis: explicit + structural absence
- Confidence: high
- Caveats: ordinary user approvals and configuration edits constrain actions but Methodology 0.3.6 does not promote generic approval/configuration to S5 or parent-governed S5.

### Absence scope

- Surfaces inspected: prompt/instruction assembly, sandbox/approval configuration, bundle/profile settings, collaboration authority boundaries, Task/Room ownership, model-selection configuration and product lifecycle documentation.
- Plausible first-party paths checked: autonomous identity revision, ultimate-policy adjudication, parent-governed identity/policy escalation and a returned authoritative decision governing later operation.
- Why no material first-party path remains: policy/configuration is preconfigured or operator-supplied enforcement, while no shipped function closes an identity/ultimate-policy decision at the declared recursion.

## Recursion

AgentHarness supports nested child-agent Sessions and a bounded delegation depth, but spawning/nesting is not itself VSM recursion. At the assessed deployment recursion, the root plus children form one temporary operating organization. Task/Room participants may span nodes and Tasks may fork/merge context lineage, but each fork is a context object rather than evidence that a complete viable-system recursion has been instantiated.

## Variety and escalation

Operational variety is absorbed through model/tool choice, persistent Sessions, parallel child delegation, follow-up steering, interrupt, sandbox/approval boundaries and explicit Task context. Continuable child settlement and status are current-control feedback. Host approval is action-scoped escalation for permissions, not S5. Task/Room remote ownership routes mutations to authoritative nodes but is data/coordination authority rather than evidence of a higher-recursion S5 parent.

## Evidence gaps

The frozen repository is large and highly compositional. This review centered on the shipped base-backed compositions and explicitly excluded custom overlays and experimental packages from positive ownership. A downstream composition could mount additional session-query/audit/adaptation services, but such possibilities do not change this standalone repository-relative classification. No unresolved gap was large enough to require `?` for the six published states.