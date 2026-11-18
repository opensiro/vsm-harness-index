---
harness_id: tigrimosr
project_name: TigrimOSR
repository: https://github.com/Sompote/TigrimOSR
review_ref: e6056e803c81547f04a65178f0c0994fc36e016a
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# TigrimOSR

## Review boundary

- System in focus: The first-party TigrimOSR server-backed agent harness, at one configured workspace's operational team and skill library.
- Purpose and identity: Execute user tasks with model-directed tools and configurable swarms, verify delivered artifacts and maintain reusable operating procedures.
- Relevant environment: User requests and post-delivery feedback, workspace outputs, skill library, configured models and optional integrations.
- Standard-distribution boundary: Shipped server/runtime, desktop or web session wiring, agent/loop and graph profiles, toolbox and installed skill synthesis. External models, services and external agent internals are dependencies.
- Credited operating / distribution surfaces: [Cargo.toml](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/Cargo.toml), [README.md](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/README.md), [src/main.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/main.rs), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs), [src/server/services/protocols.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/protocols.rs), [src/server/services/graph.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/graph.rs), [src/server/services/skill_synthesizer.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/skill_synthesizer.rs)
- Adjacent first-party surfaces excluded from ownership: Development tests, package/release operations and external data sources or provider services. Desktop presentation does not independently own a function.
- First-party operating / deployment modes considered: Server-backed native execution, live sub-agent and router/swarm modes, optional tool-using judge panel and skill synthesis with configurable adoption. The lightweight CLI is an adjacent shipped entrypoint; team/audit/adaptation grades refer to server-backed modes.
- Recursion level: The operator's configured workspace with one primary orchestrator, its active workers and the first-party skill-revision loop that serves later jobs.
- Reviewed revision: `e6056e803c81547f04a65178f0c0994fc36e016a`
- Observation date: 2026-11-18
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The chat route assembles a request-specific operating mode, agent teams and optional evaluation configuration. The toolbox drives model and tool execution, manages child tasks/results and reports active team state. A graph profile can assign a separate judge call with bounded tool access and feed a rejected verdict into a worker revision. Persisted feedback can trigger a skill synthesizer separate from the immediate task loop.

## Operational model

The model chooses task actions and can assign work across a live team. Inter-agent dispatch, wait and result routing react to incomplete and conflicting work. A configured judge can inspect files directly and send findings back before delivery. The skill worker can propose revised procedures from later user feedback, either adopting eligible auto-skill revisions or handing them to the operator for decision.

## S1 — Operations

- State: A
- Function: Operational task execution
- Disturbance / variety regulated: New user objectives, tool observations and incomplete or failed task work
- Decisive decision or feedback right: Choose tool actions, worker requests and next steps from the returned evidence
- Decision owner: The first-party model-backed session agent and worker roles in operated modes
- Supporting / enforcement mechanisms: Tool executor, selected profiles, provider adapters and bounded loops
- Closure path: Results, errors and child outputs reenter model context before follow-up or delivery
- Boundary reachability: The chat route starts the model-backed agent run and attaches the first-party toolbox and team tools to the configured server mode.
- Why this is / is not agent-owned: The model chooses work and responses. The runtime transports observations and enforces limits.
- Evidence: [src/main.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/main.rs), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/services/agent_loop.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/agent_loop.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

## S2 — Coordination

- State: A
- Function: Attenuation of interference between distinct S1 units
- Disturbance / variety regulated: Two active workers can wait for each other's pending result; parallel browser workers can interfere in shared browser state
- Decisive decision or feedback right: Choose a safe way to complete or re-route a blocked task after a cycle-specific refusal, then return the available result
- Decision owner: The affected model-backed worker or its coordinating agent decides the next task action. The runtime detects the prohibited wait and isolates browser contexts
- Supporting / enforcement mechanisms: Per-agent work and result queues, waiting-on graph, cycle detection and per-agent browser context
- Closure path: The wait tool returns the cycle-specific corrective instruction and the waiting graph. A worker can finish with available evidence, deliver its result and release the blocked peer
- Boundary reachability: The active multi-agent tool path calls exec_wait_result_from with actual caller identity. The first-party prompt and tool output instruct operating agents how to recover from a blocked wait.
- Why this is / is not agent-owned: The runtime refuses a particular cyclic wait. A worker still decides what work outcome can be returned or what subsequent coordination action to take.
- Evidence: [README.md](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/README.md), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs), [src/server/services/protocols.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/protocols.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

- Distinct S1 units: Live model-backed workers with separate task queues and result identities within one session.
- Inter-S1 disturbance: A real circular wait occurs when one worker waits for another worker that is waiting on the first. Concurrent browser work has a separate structurally identified shared-state disturbance.
- Attenuating coordination relation: Caller-aware cycle detection rejects blocking waits and feeds a concrete return-result remedy. The browser adapter additionally separates concurrent workers' browser state.
- Feedback into subsequent S1 behaviour: The rejection becomes a tool result for the current agent, which can return a result for the blocked peer instead of repeatedly waiting or redispatching.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The detection uses the actual call relationship and targets the cyclic dependency between workers, with an explicit release path into later work.

## S3 — Inside-and-now control

- State: A
- Function: Whole-system current direction and resource or commitment intervention
- Disturbance / variety regulated: Current workload, incomplete results and differing worker/model capacity across an active job team
- Decisive decision or feedback right: Decide role/model allocation and current delegation, collect worker state and assign targeted remedial work
- Decision owner: The main or router orchestrator model in the configured live team
- Supporting / enforcement mechanisms: Agent status roster, architecture instantiation, task queues and result collection
- Closure path: The configured main agent sees active workers and results, then issues the scoped task allocation or targeted repair that updates subsequent work
- Boundary reachability: The chat route exposes create_architecture, send_task, wait_result and check_agents in applicable modes. The live team status and outer verifier feed the active agent loop.
- Why this is / is not agent-owned: The coordinating model can revise the team allocation and choose follow-up commitments. Provider fallback and hard caps enforce constraints.
- Evidence: [README.md](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/README.md), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: The witness is a session team's live control, not service-wide organization or generic operator stop.

- Whole-system current view: check_agents enumerates all active realtime session agents and their statuses. The orchestrator also collects work results and the job-level review findings.
- Current-control decision scope: Within this team, select roles/models for current work, assign duties and target additional work after an incomplete result.

## S3* — Complementary audit

- State: A
- Function: Complementary independent operational audit with corrective return
- Disturbance / variety regulated: A completed-job answer claims deliverables exist or satisfy a rubric despite incomplete files or inadequate work
- Decisive decision or feedback right: Independently judge the asserted outputs against a rubric and give findings that alter subsequent remediation
- Decision owner: A separately called tool-using judge or panel in the shipped opt-in evaluation mode
- Supporting / enforcement mechanisms: Judge-specific prompt, optional distinct provider/model, artifact access, aggregate verdict and bounded retry loop
- Closure path: An adverse finding becomes a structured gap in the worker/orchestrator conversation and triggers targeted revisions before the next decision
- Boundary reachability: The chat route resolves an active graph configuration and passes it into the first-party outer evaluation; the configured judge can independently read the workspace artifacts.
- Why this is / is not agent-owned: The separately invoked judge owns the claim judgment. Verdict aggregation and retry caps implement its feedback.
- Evidence: [README.md](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/README.md), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/services/graph.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/graph.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Graph evaluation is opt-in. A broken judge or exhausted review allowance can release an answer, so the loop is not an unconditional completion guarantee.

- Claim being audited: The worker's final result satisfies the objective and its claimed artifacts or checks exist.
- Ordinary reporting path: The worker's final answer and tool records.
- Complementary access path: The separately invoked judge uses bounded artifact access to open/list files independently of the worker's report.
- Independence boundary: The judge is invoked separately with its own rubric and can use a distinct configured model. The credited mode has tool-using direct evidence access.
- Who acts on findings: The main worker or orchestrator receives structured gaps and can issue targeted follow-up work.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: External, prospective intelligence and adopted capability adaptation
- Disturbance / variety regulated: External user corrections indicate a recurring future requirement or unsuitable procedure for similar jobs
- Decisive decision or feedback right: Use the feedback and workflow trace to choose a durable change to the procedure, then authorize that change for later tasks
- Decision owner: The skill synthesis agent in the auto-update mode for eligible auto skills. The operator owns the approval/rejection right in the separate review-required mode.
- Supporting / enforcement mechanisms: Persisted feedback, scheduled synthesis, validation, proposal store, enabled skill registry and subsequent skill discovery
- Closure path: An accepted procedure replaces or enables the live skill, whose contents become available to later agents carrying out relevant jobs.
- Boundary reachability: The server starts skill synthesis, stores message feedback and ships both auto adoption configuration and proposal approval. The toolbox advertises enabled skills to later agent sessions.
- Why this is / is not agent-owned: External user feedback identifies a mismatch in demand. The model changes a reusable operating procedure aimed at future similar tasks. Eligible updates can publish automatically or pass through a distinct operator-adoption mode.
- Evidence: [src/main.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/main.rs), [src/server/routes/chat.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/chat.rs), [src/server/routes/skills.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/skills.rs), [src/server/services/skill_synthesizer.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/skill_synthesizer.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: This is bounded adaptation of reusable skills. It is not a claim about tool-provider strategy, and custom skills require operator approval.

- External distinction: Post-delivery user comments and ratings are persisted separately from the agent's own claim and can identify changed or unmet requirements.
- Future / prospective distinction: The synthesis path targets an installed reusable skill and produces an amended procedure for subsequent comparable tasks, beyond repairing the already delivered answer.
- Adaptation option generated: A validated new or revised skill, in the feedback-driven case a procedure tailored to the failure and the previously loaded skill trace.
- Path back into current capability / S3: The skill file and enabled registry entry change on direct adoption or operator approval. The main/subagent tool context then advertises the enabled capability for new work.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Skill synthesizer model | Recorded qualifying user feedback relevant to an eligible auto-generated skill in the auto-adoption configuration | A validated revision overwrites and enables the auto skill for discovery in later runs. | [src/server/services/skill_synthesizer.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/skill_synthesizer.rs), [src/server/services/toolbox.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/toolbox.rs) |
| Parent (`P`) | Authorized workspace operator | Review-required proposal with a concrete skill revision | Approval promotes the staged procedure to the live file and enables it. Rejection preserves the live version. | [src/server/routes/skills.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/skills.rs), [src/server/services/skill_synthesizer.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/skill_synthesizer.rs) |

## S5 — Policy and identity

- State: —
- Function: Resolution and return of ultimate identity or policy decisions
- Disturbance / variety regulated: A conflict about the harness's enduring mission or ultimate operating rules
- Decisive decision or feedback right: No supplied authority resolves an ultimate purpose or constitutional policy question and returns it to operations
- Decision owner: The operator selects profiles, prompts, permissions and integration settings
- Supporting / enforcement mechanisms: Profile/graph stores, agent-role YAML, tool access policy and approval UI
- Closure path: Saved config selects mechanisms and constraints for later calls
- Why this is / is not agent-owned: Skill acceptance, graph rules and dynamic team design apply policy or adjust capabilities. The review found no separate decision loop for the system's ultimate identity.
- Evidence: [src/server/services/agent_loop.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/agent_loop.rs), [src/server/services/graph.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/graph.rs), [src/server/routes/settings.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/settings.rs), [src/server/routes/agent_loops.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/agent_loops.rs), [src/server/routes/skills.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/skills.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [src/server/services/agent_loop.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/agent_loop.rs), [src/server/services/graph.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/services/graph.rs), [src/server/routes/settings.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/settings.rs), [src/server/routes/agent_loops.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/agent_loops.rs), [src/server/routes/skills.rs](https://github.com/Sompote/TigrimOSR/blob/e6056e803c81547f04a65178f0c0994fc36e016a/src/server/routes/skills.rs)
- Plausible first-party paths checked: Check system-prompt replacement, graph aggregation policies, operator profile changes and approval of skill revisions.
- Why no material first-party path remains: These surfaces let an operator configure the runtime or approve a procedure within its mandate. The shipped workflow does not detect a constitutional conflict, route it to a legitimate policy authority and apply a returned decision.

## Recursion

Agent teams may contain separately operating workers and configured sub-agent depth. The mapped audit, coordination and capability adoption use the selected workspace/team boundary.

## Variety and escalation

Cycle-aware waits, separate contexts, task limits, operator gates and bounded artifact-grounded retries regulate specific operating variation.

## Evidence gaps

Source-only classification. No live model, browser, integration or skill-adoption experiment was run. State coverage depends on the documented modes and scoped first-party paths.
