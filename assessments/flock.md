---
harness_id: flock
project_name: Flock
repository: https://github.com/Onelevenvy/flock
review_ref: 2eac827aa803ae2ee8578e401a864e116cd994d3
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Flock

## Review boundary

- System in focus: the first-party Flock harness at pinned revision `2eac827aa803ae2ee8578e401a864e116cd994d3`, including the `flock-agent` execution engine and graph, `flock-workflow` compiler/runtime, first-party tool/sandbox/approval machinery, `flock-skills` loading/discovery surfaces, scheduled/headless execution paths, and the shipped `skill-creator` adaptation workflow.
- Purpose and identity: provide a Rust AI-agent runtime in which autonomous agent loops execute tools against an environment, declarative workflows compose LLM/agent/code/human/plugin nodes, and reusable skills can be loaded or created/improved for later agent runs.
- Relevant environment: user requests; local files/projects/processes; sandbox/browser/computer surfaces; model-provider responses; MCP/tool services; existing project skills and documentation; external best practices or similar skills consulted during capability development; evaluation outputs and human feedback used while adapting a reusable skill.
- Standard-distribution boundary: the Flock application/runtime and bundled resources shipped from `flock-data/skills` at the pinned revision. External model providers, MCP servers, operating-system/container/browser substrates, third-party services, external LangGraph implementation internals, and users/humans are environment or Parent rather than Flock-owned autonomous actors.
- Credited operating / distribution surfaces: `crates/flock-agent/src/engine/run/run.rs`; `crates/flock-agent/src/graph/`; `crates/flock-workflow/src/`; `crates/flock-tools/`; `crates/flock-skills/`; `flock-data/skills/skill-creator/`; and application packaging/runtime paths that make bundled skills reachable in the installed product.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, contributor instructions, benchmark-only fixtures, UI observability by itself, and capabilities belonging only to external providers/substrates. The graph library is credited only for Flock-owned wiring and behavior visible through the shipped boundary; semantics not closed by Flock are not imported.
- First-party operating / deployment modes considered: ordinary interactive agent execution; declarative workflow execution with agent/LLM/code/human/plugin nodes; packaged desktop resources; scheduled/headless runs where they reuse the same first-party engine; and shipped skill creation/improvement when invoked through the runtime skill surface.
- Recursion level: one Flock installation as the system-in-focus. Individual agent/workflow agent nodes are operational actors inside it; graph edges, scheduler/checkpointer, approval manager, model providers and sandbox backends are supporting machinery unless they own a function-specific organizational decision.
- Reviewed revision: `2eac827aa803ae2ee8578e401a864e116cd994d3`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Flock's ordinary agent runtime builds a first-party cyclic graph around model-request and tool-call nodes. `AgentEngine::run` validates configuration, restores optional checkpoint state, prepares the tool/sandbox context, constructs the agent graph, invokes it with an iteration/timeout boundary, and returns final state. Inside that graph, the model-driven agent chooses tool calls, Flock executes them, and tool results return to the next model turn. The declarative workflow layer separately compiles ReactFlow-style JSON into a graph containing start/end, LLM, agent, classifier, conditional, answer, code, human, plugin, and parameter-extractor nodes. An agent workflow node itself has a bounded model/tool loop and can load configured skills.

Multiple agent nodes can therefore coexist in a workflow and graph edges can fan out or route conditionally. That is real multi-agent composition, but the reviewed first-party implementation primarily compiles user-authored topology and executes it. No shipped path was found that identifies a concrete inter-S1 collision/oscillation and autonomously chooses a coordination response, or that gives a supervisory agent a whole-system current view and broad discretionary authority over shared commitments/resources. Parallel nodes, routing and checkpointing are not promoted into S2/S3 by name.

Flock also ships a reusable skill subsystem. Runtime paths load workspace/user/project skills and dynamically discover nested `.flock/skills/` directories. The desktop bundle packages `flock-data/skills/` as application resources. Among those resources, `skill-creator` is a first-party reachable meta-capability for creating or improving reusable skills. It instructs the active agent to research relevant edge cases/docs/best practices when useful, draft a skill, create test prompts, run with-skill and baseline trials, inspect outputs/transcripts and quantitative feedback, revise the skill, rerun evaluation, and package/persist the resulting reusable capability. That adaptation loop is treated as S4 because external/future-relevant distinctions are turned into tested changes that become available to later Flock operation.

## Operational model

In a normal run, current messages and tool results form the operational state, a Flock agent chooses an action/tool call, first-party execution machinery performs it against the environment, and the resulting observation returns into the same bounded loop. Declarative workflows can instantiate several such agent loops and connect them through static/conditional graph structure. The workflow compiler and underlying scheduler enforce topology, retries, timeouts and checkpoints but do not by themselves own organizational coordination or current-control discretion.

In skill-development mode, the user's need identifies a capability gap or desired future behavior. The shipped `skill-creator` has the agent investigate requirements and relevant external information, draft or modify a reusable skill, test it against representative future tasks and baselines, interpret performance/feedback, revise it, and repeat. The user can provide requirements, feedback and an acceptance stopping condition, but the agent owns substantive option development and revision decisions within those constraints. The resulting skill is written into the same skill format/directories that Flock loads for future runs.

## S1 — Operations

- State: A
- Function: autonomously perform environment-facing task work through an iterative model/tool loop and return resulting observations into subsequent action selection.
- Disturbance / variety regulated: heterogeneous user requests, changing local/project state, model responses, tool outputs/errors, sandbox/browser/process state and other execution observations requiring context-sensitive next actions.
- Decisive decision or feedback right: select the next tool/action from current messages and tool results, then decide whether another operational action is needed or the task/run can terminate.
- Decision owner: the active first-party Flock agent loop, including agent nodes used inside declarative workflows.
- Supporting / enforcement mechanisms: `AgentEngine::run`, Flock's `model_request`/`call_tools` graph, tool registry/executor, sandbox creation, checkpoint state, retries/timeouts, iteration limits and workflow state transport.
- Closure path: task/messages/environment state → agent model selects a tool/action → first-party Flock tool/runtime executes it → tool result or changed environment returns into agent messages/state → agent chooses the next action or terminates.
- Boundary reachability: this is the core shipped `flock-agent` path used by ordinary runs; workflow `agent` nodes expose the same class of bounded autonomous tool loop in the supported declarative workflow surface.
- Why this is / is not agent-owned: deterministic graph/tool machinery transports and enforces execution, but it does not choose the context-sensitive next operational action; removing the model-driven agent leaves no owner of that S1 discretion.
- Evidence: [`crates/flock-agent/src/engine/run/run.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-agent/src/engine/run/run.rs), [`crates/flock-agent/src/graph/builder.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-agent/src/graph/builder.rs), [`crates/flock-workflow/src/nodes/agent.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/nodes/agent.rs).
- Basis: structural
- Confidence: high
- Caveats: external model inference and external tools remain substrate/environment; credit is for Flock's first-party autonomous action loop and environment/result closure, not provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination path is established at the reviewed recursion.
- Disturbance / variety regulated: not established; workflows can contain multiple operational agent nodes, but the reviewed shipped mechanisms do not identify a specific actual or structurally evidenced interference, conflict or oscillation among those S1 units that a coordination relation is designed to attenuate.
- Decisive decision or feedback right: no S2-specific actor is shown choosing or revising a coordination response to cross-S1 disturbance.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: graph edges, conditional routing, fan-out to multiple successors, shared workflow state, checkpointing, retries/timeouts and scheduler execution.
- Closure path: these mechanisms move and sequence state/work among nodes, but no interference → attenuation decision → changed subsequent S1 behavior closure is evidenced.
- Why this is / is not agent-owned: individual agent nodes own their local operational choices; graph topology and scheduler semantics are deterministic/user-authored. Neither fact establishes autonomous coordination of a concrete inter-S1 disturbance.
- Evidence: [`crates/flock-workflow/src/builder.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/builder.rs), [`crates/flock-workflow/src/nodes/agent.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/nodes/agent.rs), [`crates/flock-agent/src/graph/mod.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-agent/src/graph/mod.rs).
- Basis: structural
- Confidence: high
- Caveats: users can author workflows in which agents collaborate or exchange outputs, but generic composition/routing is below the Profile's S2 threshold without a first-party disturbance-and-attenuation witness.

### Absence scope

- Surfaces inspected: core agent graph; declarative workflow builder; agent workflow nodes; conditional/classifier/human nodes; checkpoint/retry/timeout behavior; scheduled execution and shared workflow state.
- Plausible first-party paths checked: parallel/fan-out agent nodes, conditional routing, shared node outputs, retries, workflow checkpointing and multi-agent examples/claims.
- Why no material first-party path remains: every reviewed candidate primarily routes, sequences, persists or retries work. None ties a concrete cross-S1 collision/oscillation to a coordination relation whose result changes later S1 behavior.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function is established in the reviewed standard distribution.
- Disturbance / variety regulated: workflow progress, node failures, retries, timeouts and branch routing are regulated mechanically, but no first-party actor is shown regulating current shared resources, commitments, priorities or constraints on behalf of the whole Flock organization.
- Decisive decision or feedback right: no shipped actor has both a whole-system current view and discretionary authority to revise relevant organization-wide commitments/resources/priorities/interventions.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: workflow scheduler/compiled graph, checkpoints, retries/timeouts, cancellation state, workflow event sink, cron/headless execution controls and per-session approval state.
- Closure path: these mechanisms close execution and error-handling transitions according to configured topology/policy, not a discretionary whole-system S3 control conversation.
- Why this is / is not agent-owned: agent nodes select local task actions, while the workflow compiler/scheduler enforces configured structure. Neither worker selection nor deterministic current-state execution supplies the broader S3 decision right.
- Evidence: [`crates/flock-workflow/src/builder.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/builder.rs), [`crates/flock-workflow/src/nodes/common.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/nodes/common.rs), [`crates/flock-agent/src/engine/run/run.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-agent/src/engine/run/run.rs).
- Basis: structural
- Confidence: high
- Caveats: a user-authored graph could encode a manager/supervisor pattern, but framework expressiveness and static workflow control are not credited as shipped S3.

### Absence scope

- Surfaces inspected: workflow graph/state/compiler, agent node execution, scheduler/checkpointer, retries/timeouts, cancellation/error state, cron/headless surfaces, approval manager and multi-agent workflow composition.
- Plausible first-party paths checked: graph scheduler as controller, workflow status/event reporting, conditional/classifier routing, retries/timeouts as intervention, cron scheduling and agent-node composition.
- Why no material first-party path remains: none combines whole-system current visibility with an actor that autonomously chooses or revises shared organization-wide resources, commitments, priorities or constraints. The strongest paths are configured workflow execution and local S1 autonomy.

## S3* — Complementary audit

- State: —
- Function: no material complementary operational-audit path is established for the current S1/S3 control boundary.
- Disturbance / variety regulated: Flock exposes tool results, workflow events, retries and evaluation utilities, but no reviewed supported path independently challenges an operational unit's ordinary current-control claim and returns that finding into S3.
- Decisive decision or feedback right: none established for S3* at the current-control layer.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: workflow/tool event emission, retries, error state, checkpoints, logs, and grader/comparator/analyzer machinery bundled specifically inside the skill-development evaluation workflow.
- Closure path: routine tool/workflow results feed the same operational path; skill-development graders/comparators feed S4 capability adaptation. Neither supplies a complementary current-operations audit channel returning findings to an S3 owner.
- Why this is / is not agent-owned: independent graders can judge skill-development trials, but the audited claim there is prospective adaptation quality rather than current S1 operational accountability; moving that mechanism across functions would be a category error.
- Evidence: [`crates/flock-workflow/src/nodes/agent.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/nodes/agent.rs), [`flock-data/skills/skill-creator/SKILL.md`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/flock-data/skills/skill-creator/SKILL.md).
- Basis: structural
- Confidence: high
- Caveats: evaluation independence inside S4 is useful evidence for adaptation quality; the negative classification concerns S3*'s complementary access to current operational reality and return into current control.

### Absence scope

- Surfaces inspected: workflow/tool event reporting, checkpoints, retries/error paths, workflow debug/observability surfaces, skill-creator graders/comparators/analyzers, and human-review/evaluation paths.
- Plausible first-party paths checked: logs/traces as audit, retry/error handling as verification, skill eval graders as independent evaluator, and human review as complementary inspection.
- Why no material first-party path remains: routine reporting is not independent, while the materially separate graders/comparators belong to the future-capability S4 adaptation loop rather than an S3 operational-control conversation. No first-party complementary current-operations audit closure is established.

## S4 — Outside-and-then intelligence

- State: A
- Function: develop and test reusable future Flock capability in response to capability needs and externally/future-relevant information, then return the resulting adaptation into the skill surface used by later operation.
- Disturbance / variety regulated: a user's desired capability may not exist or an existing skill may perform poorly; relevant documentation, similar skills, best practices, edge cases, model/tool behavior, evaluation failures and changing triggering behavior create future-facing distinctions that should change the reusable capability.
- Decisive decision or feedback right: choose the concrete skill design and revisions—workflow/instructions/resources, evaluation cases/assertions, changes suggested by trial transcripts/benchmarks, reusable helper scripts and triggering-description changes—then decide whether further adaptation iterations are warranted within the user's stated objective/feedback.
- Decision owner: the active first-party Flock agent following the shipped `skill-creator` adaptation procedure. The user/Parent supplies the capability goal, may confirm intent/evals and can stop or accept the loop, but the agent develops, tests and revises the adaptation options rather than merely persisting a user-authored artifact.
- Supporting / enforcement mechanisms: packaged `skill-creator` instructions/resources; research through available tools/MCP where useful; with-skill versus baseline trial runs; graders/comparators/analyzer; benchmark aggregation; human feedback; description-optimization loop; filesystem skill format; skill loader/discovery and packaged application skill resources.
- Closure path: capability need + relevant external/future distinctions → agent researches/designs a reusable skill option → with-skill/baseline trials and feedback expose performance distinctions → agent revises the skill/description/resources → resulting skill is written/packaged in a Flock-readable skill location → later agent runs load/use the changed capability.
- Boundary reachability: `skill-creator` is under `flock-data/skills`, those resources are included in the Tauri application bundle, and `flock-skills` resolves the installed `skills` resource directory plus user/project skill directories. This is a shipped product capability, not repository-only CI/dogfood.
- Why this is / is not agent-owned: user intent and acceptance constrain the adaptation, but the substantive future-capability option generation, diagnosis of trial failures, revision choices and reusable artifact construction are delegated to the agent. Deterministic loaders/eval scripts support and measure the loop rather than owning those adaptation decisions.
- Evidence: [`flock-data/skills/skill-creator/SKILL.md`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/flock-data/skills/skill-creator/SKILL.md), [`crates/flock-skills/src/paths.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-skills/src/paths.rs), [`crates/flock-skills/src/discovery.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-skills/src/discovery.rs), [`flock-ui/src-tauri/tauri.conf.json`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/flock-ui/src-tauri/tauri.conf.json).
- Basis: structural
- Confidence: medium-high
- Caveats: generic loading/discovery of already-authored skills alone would not establish S4. Credit depends on the separately shipped adaptation procedure that actively researches/develops/tests/revises a capability and closes it back into the runtime-readable skill surface. Some evaluation branches depend on optional subagent/CLI facilities; the core draft → test/review → revise → persist loop remains explicitly adapted for environments without those facilities.

## S5 — Identity and ultimate policy

- State: —
- Function: no identity- or ultimate-policy-level closure is established at the reviewed Flock recursion.
- Disturbance / variety regulated: ordinary tool risk and human intervention are regulated, but no evidenced organizational identity/policy issue is routed to a legitimate ultimate authority whose decision returns as non-routine global policy for subsequent operation.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: `ToolApprovalManager`, per-session `Default`/`AutoEdit`/`Yolo` modes, per-category “always” approval, sensitive-tool approval, human nodes/ask-human/request-human-assistance, sandbox permissions and workflow configuration.
- Closure path: human/tool approvals can approve or deny an ordinary pending action and session modes can change which tool categories auto-approve, but that is task/session authorization rather than identity/ultimate-policy closure balancing current operations and future adaptation.
- Why this is / is not agent-owned: approval machinery enforces user/session choices; neither it nor an agent is shown owning legitimate ultimate organizational identity/policy authority. Ordinary human final say over a tool call does not meet S5 by itself.
- Evidence: [`crates/flock-core/src/ipc_interface/approval.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-core/src/ipc_interface/approval.rs), [`crates/flock-workflow/src/nodes/agent.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-workflow/src/nodes/agent.rs), [`crates/flock-tools/src/tools/builtin/ask_human.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-tools/src/tools/builtin/ask_human.rs), [`crates/flock-tools/src/tools/sandbox/request_human_assistance.rs`](https://github.com/Onelevenvy/flock/blob/2eac827aa803ae2ee8578e401a864e116cd994d3/crates/flock-tools/src/tools/sandbox/request_human_assistance.rs).
- Basis: structural
- Confidence: high
- Caveats: user-controlled approval and sandbox policy are meaningful safety mechanisms; the negative classification is specifically about the Profile's identity/ultimate-policy function, not about the absence of human control or constraints.

### Absence scope

- Surfaces inspected: approval manager and session modes, sensitive-tool execution, ask-human/request-human-assistance paths, human workflow node, sandbox/skill permissions, workflow configuration and shipped skill-development boundary.
- Plausible first-party paths checked: human approval as Parent authority, session mode as global policy, sensitive-tool allow/deny controls, sandbox permissions and skill-level allowed tools.
- Why no material first-party path remains: all reviewed mechanisms regulate ordinary task/session/tool execution or static capability constraints. None establishes a legitimate identity/ultimate-policy issue path with a decision that returns to govern the organization at the S5 level.

## Summary

At the pinned revision Flock is classified as **`A — — — A —`**. Its core agent/tool graph provides autonomous S1 operations. Declarative multi-agent/workflow topology does not by itself establish S2 coordination or S3 current control, and observability/evaluation mechanisms do not establish S3*. The shipped, packaged `skill-creator` does establish S4 by turning externally/future-relevant capability distinctions into evaluated reusable skill adaptations that later Flock runs can load. Human/tool approval remains ordinary operational authorization rather than S5 identity or ultimate policy.