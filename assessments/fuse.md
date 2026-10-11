---
harness_id: fuse
project_name: Fuse
repository: https://github.com/ethanhinson/fuse
review_ref: 5991a3366e44b0a4587cf1ab6ce00daf70b9742b
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Fuse

## Review boundary

- System in focus: the first-party Fuse Go terminal/headless coding agent and its locally spawned agent-tree runtime, with tool, approval, workflow, blackboard and session coordination surfaces.
- Purpose and identity: execute user-directed coding, research and tool-assisted tasks through model-selected steps with child-agent fan-out, bounded resource use and returned results.
- Relevant environment: workspace source and shell, configured LiteLLM/inference endpoint, user permissions, optional MCP/web providers, containers/Kubernetes sandbox substrate, and optional self-hosted loop service.
- Standard-distribution boundary: shipped `fuse <task>`, `fuse shell`, `loop-server` and `loop-serve-net` binaries and first-party agent/spawner/workflow paths at 5991a3366e44b0a4587cf1ab6ce00daf70b9742b. Third-party provider reasoning, external MCP server policy, operator CI workflows and example/eval agent organizations are not attributed to Fuse.
- Credited operating / distribution surfaces: [cmd/fuse/main.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/main.go); [cmd/fuse/shell.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/shell.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/agent/loop.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/loop.go); [internal/agent/spawn.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/spawn.go); [internal/agent/scheduler.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/scheduler.go); [internal/agent/blackboard.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/blackboard.go); [internal/pipeline/engine.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/engine.go); [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go).
- Adjacent first-party surfaces excluded from ownership: repository-maintainer CI/release workflows, development/evaluation outputs under evals and reports, test-only simulated policies, deployment observability stack and operational dashboards; external LiteLLM, provider models, third-party MCP servers, container engines and sandbox backends are dependencies rather than Fuse-owned organizational decision rights.
- First-party operating / deployment modes considered: one-shot task, interactive shell, child spawn and workflow/pipeline, local session events and server mode, user-mediated permission modes, optional research skill and permission classifier.
- Recursion level: one Fuse agent session with separately running local child S1 agents and nested workflow pools; not the parent software company, hosted provider or entire deployment fleet.
- Reviewed revision: 5991a3366e44b0a4587cf1ab6ce00daf70b9742b.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The bundled CLI instantiates a first-party `Agent.Run` loop for user requests; the loop calls inference, exposes coding/shell/search tools, executes model-selected tool calls and returns tool outcomes into subsequent model turns. Permission gates, fixed budgets, compaction and session event storage bound or record the loop rather than selecting the coding strategy. [cmd/fuse/main.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/main.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/agent/loop.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/loop.go); [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go).

The model-facing `spawn_agent` can create additional first-party local Agent instances with selected persona, child tools and budget. The scheduler enforces a global slot cap and per-workflow admission, dispatching queued children round-robin among pools and letting blocked parents yield/reacquire slots; child results flow back to their initiating agent. A shared per-session blackboard offers last-writer-wins keys and waits, while workflow/pipeline code can construct a DAG of spawned worker steps and conditionally route results. [internal/tools/spawn_agent.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/tools/spawn_agent.go); [internal/agent/spawn.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/spawn.go); [internal/agent/scheduler.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/scheduler.go); [internal/agent/blackboard.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/blackboard.go); [internal/pipeline/engine.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/engine.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go).

Optional research and pipeline synthesis delegate facet exploration or task planning to the same runtime; their task-focused research, static constraints, replay/event telemetry, approvals and checks are not assumed to establish a complementary auditor, strategic adaptation owner or ultimate-policy governor. [cmd/fuse/run.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/run.go); [internal/pipeline/synthesize.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/synthesize.go); [internal/agent/personas.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/personas.go); [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go).

## Operational model

An operating S1 is the root coding/task agent or an actually spawned independent child agent that chooses its tool work contingent on results. The user supplies the task and may approve or deny risky operations; the inference provider supplies tokens but not an external coding-agent harness. The agent chooses requested child tasks, whereas repository-defined scheduler rules determine contested slot grants and recovery from child waits. A root session remains the focal recursion. This assessment does not import control or audit ownership from the development organization.

## S1 — Operations

- State: A
- Function: model-driven local coding and task execution through real file, shell, search and delegated tool actions.
- Disturbance / variety regulated: user-directed changing workspace, tool errors, retrieved data, and task-completion uncertainty.
- Decisive decision or feedback right: select the next task action and tool invocation after inference observes prior tool results.
- Decision owner: first-party Fuse Agent operating with a configured model; the model's next action is integrated into Fuse's own loop rather than delegated to an external agent CLI.
- Supporting / enforcement mechanisms: file/shell/MCP tools, user approval gate, budget/context management, session events, sandbox and human prompts.
- Closure path: user request → model completion in Agent.Run → first-party tool execution → returned results → subsequent completion or final response.
- Boundary reachability: `fuse <task>`, the interactive shell and server bindings construct and run the same first-party Agent; source paths are executable entrypoints, not demo-only agents.
- Why this is / is not agent-owned: the model chooses contingent tool actions; fixed permission/throughput controls constrain the actions without taking operational discretion.
- Evidence: [cmd/fuse/main.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/main.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/agent/loop.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/loop.go); [cmd/fuse/run.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/run.go).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: requires an external inference service, credentials and configured tools; these dependencies do not transfer operational ownership.

## S2 — Coordination

- State: C
- Function: attenuate execution starvation and nested wait deadlock between distinct live child agent S1 units contending for a bounded pool of available execution slots.
- Disturbance / variety regulated: independent child S1 tasks can demand the same scarce concurrent-run slots; an already running child may wait for a descendant that cannot start unless its slot is released, and competing pools could otherwise starve each other.
- Decisive decision or feedback right: choose which waiting agent receives a freed concurrency slot and whether a blocked parent relinquishes/reacquires one, through the first-party fair dispatcher and priority reentry mechanism.
- Decision owner: deterministic scheduler rule authored/selected in the Fuse construction; an autonomous S2 dispute resolver or agent-owned revision of the coordination policy is not shown. The slot allocation path is S2-specific but constructor-owned.
- Supporting / enforcement mechanisms: global capacity cap, workflow pool queues, FIFO entries, round-robin cursor, slot acquisition/release, atomic queue bounds, cancellation backstops and wait channels.
- Closure path: independent child spawn demands saturate shared slot capacity → scheduler queues by pool → completed/yielded work releases a slot → dispatcher grants it to another waiting child or to a yielding parent on priority reacquisition → selected child/parent resumes independent task operation.
- Boundary reachability: `cmd/fuse/runtime_binding.go` wires `spawn_agent` with the AgentTree's Scheduler in the supported one-shot, research and shell bindings; `Spawner.Spawn` calls `enqueueSlot` before starting the child, while `dispatch` / `YieldSlot` / `UnyieldSlot` execute the inter-S1 capacity handoff.
- Why this is / is not agent-owned: fairness and deadlock avoidance would still run with identical decisions if a model were removed, given the same queued slot requests; the model selects work but not the coordination response. The S2 function is specifically evidenced by the contested-slot / child-wait disturbance, not credited merely because a scheduler or blackboard exists.
- Evidence: [internal/agent/scheduler.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/scheduler.go); [internal/agent/spawn.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/spawn.go); [internal/agent/tree.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/tree.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/agent/blackboard.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/blackboard.go); [internal/pipeline/engine.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/engine.go).
- Basis: structural + explicit.
- Confidence: medium; S2-specific constructor evidence is tied to source-observed contended slots and parent-wait deadlock, rather than a generic scheduler label.
- Caveats: the positive S2 witness is bounded to local child-agent contention. Shared blackboard, DAG dependencies and concurrent child count alone are not independent positive witnesses. No autonomous S2 arbitration is asserted.
- Distinct S1 units: independently running root-spawned and nested local child Agents, potentially grouped into separate workflow pools.
- Inter-S1 disturbance: finite global child execution slots are contended for by distinct active/queued child agents; descendant waits can deadlock a parent occupying its own needed slot, and one pool's queue can starve another.
- Attenuating coordination relation: per-pool FIFO with round-robin across pools, and explicit wait-yield plus priority slot reacquisition for dependent parents.
- Feedback into subsequent S1 behaviour: scheduler's slot grant wakes a particular waiter and allows that agent to execute its own model/tool loop; reacquired slot resumes the waiting parent's subsequent work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the recorded contention and nested-wait deadlock are interaction-induced disturbances; configured allocation and reentry rules directly alter which S1 operation can proceed, rather than merely passing messages or ordered tasks.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-session current-control decision over commitments, resource policy, priorities, or accountability beyond S1 task choice and deterministic slot enforcement is established.
- Disturbance / variety regulated: current workload, resource saturation, pending runs and user interventions are visible as runtime state but do not demonstrate a distinct discretionary whole-system supervisor.
- Decisive decision or feedback right: user/constructor fixes operating limits; model chooses its task and children; the runtime enforces caps and displays states, rather than making a new strategic current-control allocation decision.
- Decision owner: no separate evidenced S3 controller in the supported mode.
- Supporting / enforcement mechanisms: Scheduler, AgentTree snapshots, workflow quotas, session/loop services, auto permission gate, TUI panel and model/user messages.
- Closure path: capacity denials and status flow to agents/users; no distinct session-wide supervisory judgment returned as an ongoing management decision.
- Why this is / is not agent-owned: model discretion about its own task/delegation and deterministic fair slot allocation are not a demonstrated system-wide S3 decision owner.
- Evidence: [internal/agent/scheduler.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/scheduler.go); [internal/agent/tree.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/tree.go); [cmd/fuse/workflow.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/workflow.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: S2 fair coordination is assessed separately; no promotion of resource enforcement to S3 authority.

### Absence scope

- Surfaces inspected: current session/agent tree, scheduler admission and pool rules, workflow activation, CLI/shell/server bindings and permission-gate interventions.
- Plausible first-party paths checked: a whole-session current operation overview paired with a discretionary agent or legitimate parent controller selecting and returning common priorities/resources/commitments; no function-specific return beyond local S1 and fixed policy was established.
- Why no material first-party path remains: the supported components enforce configured caps, relay user approvals and expose telemetry, but do not close a distinct whole-current regulatory decision loop.

## S3* — Complementary audit

- State: —
- Function: no first-party independently grounded challenge of ordinary agent claims with a consequential corrective-audit feedback right is established at the standard operating boundary.
- Disturbance / variety regulated: unsafe tool use, malformed pipeline plans, task errors and unreliable answers can occur; documented mitigations are enforcement, validation or ordinary model/task feedback rather than an independent S3* audit.
- Decisive decision or feedback right: permission classifier and policy gate apply user/constructor rules to calls; pipeline checks structural validity; no auditor obtains complementary primary evidence of the agent's actual work and directs corrective return.
- Decision owner: no distinct first-party complementary audit judge with an evidenced S3* feedback closure.
- Supporting / enforcement mechanisms: permission decisions, optional model classifier, schema validator, pipeline retry on parse errors, research subagents, traces, tests/evals outside the shipped boundary.
- Closure path: denied calls or invalid plans can be retried/changed within normal S1 loop; no independently sourced audit verdict and follow-up regulation are evidenced.
- Why this is / is not agent-owned: generic review-capable spawned personas and an approval/permission classifier are not function-specific independent audits merely by their name or possible user prompt.
- Evidence: [internal/agent/personas.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/personas.go); [internal/pipeline/synthesize.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/synthesize.go); [internal/pipeline/engine.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/engine.go); [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go); [cmd/fuse/run.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/run.go); [internal/agent/loop.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/loop.go).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: a user could assemble a review workflow, but hypothetical developer composition is not credited as shipped S3* without an independent evidence path and corrective ownership.

### Absence scope

- Surfaces inspected: bundled agent personas, child spawning, pipeline synthesis/validation and retry, tool permission classifier, loop error/detector, session observability and adjacent repository eval/CI folders.
- Plausible first-party paths checked: an independently evidenced auditor with distinct access to actual actions/results, an autonomous or constructor audit judgment, and delivered correction that governs later S1 operation.
- Why no material first-party path remains: source demonstrates ordinary validation and safeguards but no shipped first-party independent complementary audit cycle distinct from those mechanisms.

## S4 — Outside-and-then intelligence

- State: —
- Function: no organizational future-oriented environmental appraisal, option selection and returned capability adaptation loop at the Fuse session recursion.
- Disturbance / variety regulated: outside information and new future conditions could call for a changed agent operating capability, but source research functions address user tasks.
- Decisive decision or feedback right: research facet exploration and pipeline synthesis support requested work, not a recognized future-system adaptation choice and rollout.
- Decision owner: no separately evidenced prospective S4 actor or legitimate parent-mode decision owner.
- Supporting / enforcement mechanisms: web research tools, research skill, context summaries, model selection, agent role prompts, release notes and configuration.
- Closure path: child research reports can inform the present user's task; no returned strategic decision changes the harness's subsequent operating architecture/capability.
- Why this is / is not agent-owned: collecting information or synthesizing a task DAG is not by itself outside-and-then governance or adaptive closure.
- Evidence: [cmd/fuse/run.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/run.go); [internal/skills/embedded/research.md](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/skills/embedded/research.md); [internal/pipeline/synthesize.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/pipeline/synthesize.go); [internal/agent/loop.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/loop.go); [cmd/fuse/workflow.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/workflow.go).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: operator reconfiguration and external ecosystem change do not establish a built-in S4 parent mode.

### Absence scope

- Surfaces inspected: bundled research, pipeline synthesis, skill embedding, session/context tools, workflow configuration, current CLI/server modes and adjacent release/eval artifacts.
- Plausible first-party paths checked: external trend recognition, autonomous/parent adaptive decision among alternatives and return of that choice into changed future-capable current operation.
- Why no material first-party path remains: observed research and plan synthesis serve current tasks; no shipped future-environment→capability-renewal feedback path is established.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational identity/purpose dispute resolution with authoritative return into operating policy at the declared agent-session recursion.
- Disturbance / variety regulated: permissions, user preferences and configured limits constrain tool actions, but are not identity-level ultimate-policy dilemmas.
- Decisive decision or feedback right: user chooses task and may approve tool usage; constructor configures safeguards; no source-shipped S5 identity or ultimate-purpose decision pathway.
- Decision owner: user/developer owns local configuration or approvals, not an evidenced integrated parent S5 mode.
- Supporting / enforcement mechanisms: permission modes, allow/deny lists, auth/tenant boundaries, model settings, role prompts, tool mediator and approval interface.
- Closure path: ordinary tool actions get permitted/blocked and the loop proceeds; no distinctive ultimate-policy matter is routed to legitimate authority and its authoritative resolution returned to govern future operation.
- Why this is / is not agent-owned: hard denial/approval enforcement does not confer constitutive policy judgment on the agent; a permission prompt is a local operations gate.
- Evidence: [internal/permissions/gate.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/permissions/gate.go); [cmd/fuse/main.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/main.go); [cmd/fuse/approval.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/approval.go); [cmd/fuse/runtime_binding.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/cmd/fuse/runtime_binding.go); [internal/agent/personas.go](https://github.com/ethanhinson/fuse/blob/5991a3366e44b0a4587cf1ab6ce00daf70b9742b/internal/agent/personas.go).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: no inference about maintainer governance or broader human organizations.

### Absence scope

- Surfaces inspected: user approval, permission policy, config/model selection, first-party shell/server controls, personas, contributor/deployment boundaries and adjacent release workflows.
- Plausible first-party paths checked: ultimate-policy issue, legitimate constitutive authority (including an actual parent mode), authoritative decision and governed return to subsequent operating behavior.
- Why no material first-party path remains: local tool permission and tenant policy execute already defined constraints or user approvals, without an identity-level governance decision process.

## Distributed OSS parent arrangement

The user-operated local session is not the maintainer organization. No evidence is credited that distributed Fuse contributors jointly operate a legitimate parent S3/S4/S5 decision-and-return process in the shipped local agent recursion. CI/release activity in this repository is adjacent evidence, not a parent mode by co-location.

## Self-hosted and non-human modes

Local shell and the optional networked loop server expose user/operator controls and configured sandbox/permission enforcement. None shows a separately completed parent-governed S3/S4/S5 function merely by supporting intervention or policy settings. The S2 constructor does not imply an agent-owned or parent-owned controller.

## Recursion

One Fuse session is the focal system; child Agents constitute interacting S1 units under its shared scheduler. An entire service deployment, external inference service, maintainer team and third-party CI are distinct higher/adjacent organizations not imported.

## Variety and escalation

Operational variety is absorbed through iterative tool/model selection; contested execution slots are regulated by a local deterministic coordination path. Quotas, permission denials and user escalation can stop or constrain the work. Those constraints do not automatically establish separate S3/S3*/S4/S5 rights.

## Evidence gaps

- **Bounded S2 attribution:** the accepted S2=C interpretation relies on source-observed scarce-slot interference and nested-wait deadlock between operating child agents, a function-specific fair scheduling/re-entry path, and deterministic (not agent-owned) coordination responses. A future separate audit may challenge this classification under Index correction rules.
- The inspected evidence is repository structure and first-party source at the immutable SHA, not a live execution trace. No claim is made of empirically observed S2 efficacy or production adoption.
- Any materially distinct supported parent-mode or audit wiring discovered later requires a source-pinned Index correction under its own authority; no Organization S3* audit result is asserted here.
