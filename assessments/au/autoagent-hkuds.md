---
harness_id: autoagent-hkuds
project_name: AutoAgent (HKUDS)
repository: https://github.com/HKUDS/AutoAgent
review_ref: 16c12b052ef2330a198063c62a07a7f9723031e3
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

# AutoAgent (HKUDS)

## Review boundary

- System in focus: the first-party AutoAgent harness at pinned revision `16c12b052ef2330a198063c62a07a7f9723031e3`, including the `MetaChain` execution loop, shipped system agents, ready-to-use multi-agent user mode, Agent Editor, Workflow Editor, plugin registry, and the first-party paths that create, test, register, and execute reusable tools, agents, and workflows.
- Purpose and identity: provide a zero-code agent harness that can solve user tasks through autonomous specialist agents and can extend its own reusable agent/tool/workflow capability from natural-language requirements.
- Relevant environment: user tasks; local files and code workspaces; web pages and downloadable artifacts; external APIs; current model/tool capabilities such as Hugging Face models; model-provider responses; and later tasks that can use newly created plugin artifacts.
- Standard-distribution boundary: the installable AutoAgent package and its documented `auto main`, `auto deep-research`, Agent Editor, and Workflow Editor modes at the pinned revision. Model providers, Docker itself, third-party APIs, Hugging Face services, and external websites are substrates/environment rather than AutoAgent-owned organizational actors.
- Credited operating / distribution surfaces: `autoagent/core.py`; `autoagent/agents/system_agent/*`; shipped meta-agents under `autoagent/agents/meta_agent/`; `autoagent/cli_utils/metachain_meta_agent.py`; plugin-editing tools under `autoagent/tools/meta/`; `autoagent/registry.py`; generated workflow execution through `autoagent/flow/` and `autoagent/workflows/`.
- Adjacent first-party surfaces excluded from ownership: repository benchmark/evaluation suites under `evaluation/`, examples/tests used only to evaluate or demonstrate AutoAgent, and repository-development/CI activity. They may corroborate implementation but do not close a product-harness function unless wired into the credited operating modes.
- First-party operating / deployment modes considered: ready-to-use multi-agent user mode; Agent Editor construction mode; Workflow Editor construction mode; generated plugin-agent/workflow execution through the same installed editable AutoAgent runtime.
- Recursion level: one AutoAgent installation as the system-in-focus. File Surfer, Web Surfer, Coding Agent, and generated task agents are operational actors inside that harness; third-party models/APIs do not become AutoAgent metasystem actors merely because agents call them.
- Reviewed revision: `16c12b052ef2330a198063c62a07a7f9723031e3`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

AutoAgent supplies a first-party `MetaChain` runtime that repeatedly asks the active agent for a model decision, exposes the agent's registered tools, executes selected calls, feeds tool results back into history/context, and can switch the active agent when a tool result returns another `Agent`. The standard system-triage setup wires File Surfer, Web Surfer, and Coding Agent into that loop with explicit transfer-to-specialist and transfer-back functions. The specialists own their local next-action/tool decisions while deterministic runtime code transports calls and state.

The same distribution also ships construction modes. Agent Former turns natural-language requirements into structured agent forms; Tool Editor can inspect existing tools plus external API/model information, create reusable plugin tools, and must execute/test them before reporting success; Agent Creator writes reusable plugin agents and, for multi-agent forms, generated orchestrators; Workflow Creator writes registered workflow code and executes it. The meta-agent CLI sequences those construction agents and retries failed creation/testing. Created tools, agents, and workflows live in first-party package directories and register into the runtime's global plugin/workflow registry.

AutoAgent also contains an asynchronous event engine used by generated workflows. It can execute multiple event tasks and gate downstream events on event groups, but generic workflow fan-out, joins, and sequencing are not treated as organizational coordination without an evidenced inter-S1 disturbance. Repository `evaluation/` suites are reviewed as adjacent benchmark infrastructure rather than an operational audit path of the supported product boundary.

## Operational model

In ordinary task operation, the System Triage Agent receives the task and autonomously chooses among specialist operational actors. File Surfer explores local documents, Web Surfer manipulates/browses web state, and Coding Agent writes/executes code in its scoped environment. Each specialist iterates through observations and tool results, then returns task status to triage. These are genuine environment-facing operations, but the transfer graph is principally task delegation and capability routing.

In editor operation, user requirements establish the desired capability. First-party meta-agents autonomously turn those requirements into reusable tool/agent/workflow artifacts, test them, and persist them into the installed editable AutoAgent package. The decisive adaptation details—what external capability to use, the reusable interface/code, repair attempts, and concrete generated organization—are selected by the meta-agents within user-supplied requirements and optional suggestions.

## S1 — Operations

- State: A
- Function: autonomous operational units directly transform task/environment state by browsing files/web resources or writing/executing code and return task outcomes into the AutoAgent run.
- Disturbance / variety regulated: heterogeneous user tasks, changing page/file state, code/runtime errors, tool results, and local environment observations that require different next actions.
- Decisive decision or feedback right: choose the next environment-facing tool/action from current history/observations and decide when the assigned subtask is complete enough to return.
- Decision owner: the active first-party AutoAgent specialist agent (File Surfer, Web Surfer, Coding Agent, or a generated plugin agent) through its model-driven decision loop.
- Supporting / enforcement mechanisms: `MetaChain` history/context propagation, tool dispatch, environment wrappers, registered tool sets, scoped workspaces, and deterministic transfer plumbing.
- Closure path: observation/history → agent selects tool/action → first-party runtime executes it → result/changed environment returns into agent history → agent selects the next action or returns completed status to triage.
- Boundary reachability: the specialist agents and `MetaChain` loop are shipped runtime components used by documented ready-to-use/user-mode execution; the positive path does not depend on repository-development or benchmark actors.
- Why this is / is not agent-owned: removing the specialist agent while retaining deterministic dispatch leaves no actor that chooses context-sensitive file/web/code actions; the runtime only executes the selected tool calls.
- Evidence: [`autoagent/core.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/core.py), [`system_triage_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/system_triage_agent.py), [`filesurfer_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/filesurfer_agent.py), [`websurfer_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/websurfer_agent.py), [`programming_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/programming_agent.py).
- Basis: structural
- Confidence: high
- Caveats: model inference is external compute, but the reviewed first-party harness defines the operational actor, action space, environment coupling, tool/result loop, and handoff closure; undocumented provider behavior is not imported.

## S2 — Coordination

- State: —
- Function: no material first-party S2 path is established at the reviewed recursion.
- Disturbance / variety regulated: not established; the reviewed multi-agent mechanisms do not identify a concrete interference, conflict, or oscillation among distinct S1 units that they specifically attenuate.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: triage-to-specialist transfers, generated orchestrator handoffs, shared conversation/context propagation, asynchronous event groups, and workflow sequencing/joins.
- Closure path: the mechanisms close delegation/workflow transitions, but no S2-specific disturbance → attenuation → changed-S1-behaviour loop is evidenced.
- Why this is / is not agent-owned: agents choose transfers and workflow actions, but autonomy over routing/delegation does not convert those mechanisms into S2 without the Profile's interference witness.
- Evidence: [`system_triage_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/system_triage_agent.py), [`edit_agents.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_agents.py), [`flow/core.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/flow/core.py), [`edit_workflow.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_workflow.py).
- Basis: structural
- Confidence: high
- Caveats: a user could author a generated workflow that implements S2, but generic framework expressiveness is outside the `C` threshold unless a first-party S2-specific path is already supplied.

### Absence scope

- Surfaces inspected: the core agent loop; shipped system-triage/specialist agents; generated orchestrator construction; workflow/event engine; workflow generator; meta-agent CLI and editor paths.
- Plausible first-party paths checked: specialist transfer/back-transfer, orchestrator delegation, event fan-out/join semantics, shared context, workflow ordering and parallel execution.
- Why no material first-party path remains: every reviewed path moves, assigns, sequences, or joins work, but none ties that machinery to a specific actual or structurally evidenced inter-S1 collision/oscillation together with an attenuation response and feedback into later S1 behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function is established in the reviewed standard distribution.
- Disturbance / variety regulated: task decomposition, specialist choice, construction errors, and workflow transitions are handled, but no evidenced current whole-system resource/commitment variety is regulated on behalf of the complete AutoAgent organization.
- Decisive decision or feedback right: no first-party actor is shown holding a whole-system current view plus discretionary authority over shared resources, commitments, priorities, constraints, accountability, synergy, or intervention.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: System Triage selects a specialist; generated orchestrators delegate subtasks and receive outputs; editor code retries failed parse/build/test attempts; the event engine schedules executable workflow events.
- Closure path: those paths close task routing, construction, or workflow execution, not an S3 current-control conversation for the whole system.
- Why this is / is not agent-owned: model-driven triage/orchestration is agent-owned delegation, but the Profile explicitly requires more than worker selection/decomposition; no broader current-control decision right is evidenced.
- Evidence: [`system_triage_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/system_triage_agent.py), [`agent_creator.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/agent_creator.py), [`edit_agents.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_agents.py), [`metachain_meta_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/cli_utils/metachain_meta_agent.py), [`flow/core.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/flow/core.py).
- Basis: structural
- Confidence: high
- Caveats: generated downstream agents/workflows can be authored with richer management semantics; that does not establish shipped AutoAgent S3 at this boundary.

### Absence scope

- Surfaces inspected: runtime loop, triage, generated orchestrator path, workflow engine/generator, editor retry/test paths, registry and supported user/editor modes.
- Plausible first-party paths checked: triage as manager, generated orchestrator as manager, async workflow scheduling, construction monitoring/retries, and registry-level management.
- Why no material first-party path remains: none of the inspected actors combines a current whole-system view with discretionary regulation of shared resources/commitments/priorities/constraints. The strongest candidates are delegation and deterministic execution support, which are explicitly below the S3 threshold.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary access-to-reality audit path is established inside the supported operating boundary.
- Disturbance / variety regulated: ordinary construction errors and benchmark correctness are observable, but no operational claim is challenged through a materially independent audit channel that returns findings into current control.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: Tool Editor runs newly created tools before success; Agent Creator runs created agents; workflow creation syntax-checks generated files; `evaluation/` contains benchmark suites.
- Closure path: editor tests can cause same-path retry/rework, but they are ordinary validation performed by the construction path itself; the repository evaluation suites are not wired into the declared standard-distribution runtime as a complementary audit/control loop.
- Why this is / is not agent-owned: the same editor/creator agent that creates an artifact also interprets its routine run/test outcome, so the evidence does not supply the complementary independence required for S3*.
- Evidence: [`tool_editor.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/tool_editor.py), [`metachain_meta_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/cli_utils/metachain_meta_agent.py), [`edit_workflow.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_workflow.py), [`evaluation/`](https://github.com/HKUDS/AutoAgent/tree/16c12b052ef2330a198063c62a07a7f9723031e3/evaluation).
- Basis: structural
- Confidence: high
- Caveats: successful compile/run tests are useful quality controls; the negative classification is specifically about the Profile's complementary-audit function, not the absence of validation.

### Absence scope

- Surfaces inspected: tool/agent/workflow creation and test loops, core runtime reporting, registry metadata, workflow execution, and first-party evaluation directories.
- Plausible first-party paths checked: compile/run validation of generated artifacts, repeated editor retries after failures, benchmark/evaluation infrastructure, and normal runtime logs/results.
- Why no material first-party path remains: the credited runtime exposes routine same-path tests and reporting, while repository evaluation is adjacent; no first-party supported mode supplies a complementary, sufficiently independent operational-reality channel whose findings feed back into control.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt AutoAgent's reusable future capability from externally relevant task needs and available external tool/model capabilities, then return the selected adaptation into the installed runtime for later use.
- Disturbance / variety regulated: user capability requirements that current tools/agents do not satisfy, changing third-party API opportunities/documentation, and changing available model capabilities relevant to future tasks.
- Decisive decision or feedback right: choose the concrete reusable adaptation—external capability/source, tool interface/implementation, required dependencies, agent composition, or workflow structure—and decide how to repair it until it passes execution/testing.
- Decision owner: first-party meta-agents, especially Tool Editor and Agent Creator/Workflow Creator, operating autonomously inside the shipped editor modes. The user supplies the high-level requirement and may add suggestions, but the meta-agent selects and implements the concrete adaptation within that envelope.
- Supporting / enforcement mechanisms: external API/model discovery tools; file creation; plugin decorators/registry; editable-package lookup; `run_tool`, `run_agent`, and `run_workflow`; deterministic parser/compile checks; bounded retry loops in the CLI.
- Closure path: capability requirement → meta-agent inspects existing capability and, when relevant, external API/current model information → agent develops reusable tool/agent/workflow option → artifact is written into first-party plugin/workflow directories and registered → artifact is executed/tested → success leaves the capability available to subsequent agents/workflows/tasks in that installation.
- Boundary reachability: Agent Editor and Workflow Editor are documented/shipped first-party operating modes reached through AutoAgent's CLI; the creation/test/registration loop runs against the installed editable AutoAgent package rather than a repository-development-only tool.
- Why this is / is not agent-owned: removing the Tool Editor/Creator agents while retaining file/registry/test utilities removes the actor that chooses which external capability to adopt and how to turn it into a reusable adaptation. Deterministic utilities write/test the selected option but do not make the adaptation judgment.
- External distinction: the editor can query third-party API documentation and authentication details and search current trending Hugging Face models/capabilities when the requested tool requires them; user requirements also expose unmet environment-facing capability needs.
- Future / prospective distinction: created tools are required to be abstract/modular/reusable rather than one-off task scripts; created agents/workflows are persisted as registered package artifacts intended for later execution beyond the current construction turn.
- Adaptation option generated: reusable registered plugin tool, plugin agent/multi-agent orchestrator, or registered workflow plus any required dependencies.
- Path back into current capability / S3: `create_tool`/`create_agent`/`create_workflow` write into AutoAgent's installed package; registration decorators expose the artifact through the global registry; `run_tool`/`run_agent`/`run_workflow` test and exercise it, after which later runtime calls can discover/use the new artifact.
- Evidence: [`tool_editor.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/tool_editor.py), [`edit_tools.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_tools.py), [`agent_former.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/agent_former.py), [`agent_creator.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/agent_creator.py), [`workflow_creator.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/workflow_creator.py), [`edit_workflow.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_workflow.py), [`registry.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/registry.py), [`metachain_meta_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/cli_utils/metachain_meta_agent.py).
- Basis: structural
- Confidence: high
- Caveats: S4 credit is for the shipped editor/self-development mode, not ordinary user-mode task planning. A user can guide construction with requirements/suggestions, but the reviewed evidence does not establish a distinct parent-owned adaptation mode, so no `(P)` modifier is published.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established for the AutoAgent installation at the reviewed recursion.
- Disturbance / variety regulated: user requests, construction requirements, prompts, tool restrictions, and optional suggestions constrain operation, but no evidenced identity-level or ultimate-policy dispute is escalated to a legitimate authority and returned as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: system instructions, tool availability, protected built-in tools, user requirements/suggestions, environment scopes, and static framework constraints.
- Closure path: ordinary instructions and constraints affect task/construction behavior directly; no separate identity/policy issue → ultimate authority → authoritative decision → returned operation path is supplied.
- Why this is / is not agent-owned: neither the agents nor a first-party parent mode are shown exercising ultimate identity/policy authority at this recursion.
- Evidence: [`tool_editor.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/meta_agent/tool_editor.py), [`edit_tools.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/tools/meta/edit_tools.py), [`metachain_meta_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/cli_utils/metachain_meta_agent.py), [`system_triage_agent.py`](https://github.com/HKUDS/AutoAgent/blob/16c12b052ef2330a198063c62a07a7f9723031e3/autoagent/agents/system_agent/system_triage_agent.py).
- Basis: structural
- Confidence: high
- Caveats: the user remains an important source of requirements and suggestions; generic human influence over tasks or construction is below the Methodology's S5 parent-governance threshold.

### Absence scope

- Surfaces inspected: ready-to-use runtime instructions, system triage, meta-agent CLI, tool/agent/workflow editors, plugin protection rules, registry, environment constraints, and supported user/editor interaction paths.
- Plausible first-party paths checked: user requirements and suggestions, protected tools, system prompts/instructions, editor failure handling, and ordinary operator control over construction.
- Why no material first-party path remains: none of the inspected paths identifies an identity/ultimate-policy matter, a legitimate ultimate authority for that matter, and a returned authoritative decision governing subsequent operation. They are task requirements, construction guidance, or static constraints.

## Distributed OSS parent arrangement

The public repository has maintainers/contributors, but repository-development governance is outside the assessed installed-harness recursion. No organization-level parent S3/S4/S5 mode is inferred from ordinary OSS maintenance. In the shipped editor mode the local user can supply requirements and suggestions, but the concrete S4 adaptation judgment remains agent-owned; the inspected interaction does not establish a separate legitimate parent-owned adaptation closure.

## Self-hosted and non-human modes

AutoAgent is locally deployable and exposes interactive user/editor control, but no distinct first-party operator mode closes S3, S4, or S5 with parent-owned organizational decision rights. Human input is therefore recorded as environment/constraint/trigger rather than `(P)` publication evidence.

## Recursion

The assessment treats one AutoAgent installation as the viable system under review. Shipped specialists and generated plugin agents may contain their own local loops, but spawning/creating them does not by itself prove a fully viable recursive subsystem. Third-party model providers/APIs remain environmental substrates. Generated downstream organizations can realize additional VSM functions, but those functions are not imported into the base AutoAgent classification unless the standard distribution itself supplies the required path.

## Variety and escalation

Operational variety is attenuated by the System Triage Agent selecting a specialist with the appropriate action repertoire and by each specialist's scoped tool set. Tool/action results amplify the agent's information for the next decision. Construction mode handles capability gaps at a longer horizon: unmet requirements and external capability information can trigger creation of reusable new tools/agents/workflows, which returns additional regulatory variety to later operation.

Failures during editor creation/testing are fed back to the same constructor agent for bounded retries. That is construction error recovery, not a separate S3* audit. No distinct whole-system current-control escalation or identity-policy escalation path was found at this recursion.

## Evidence gaps

- The pinned repository documents and implements external API/model discovery in editor mode, but the assessment does not claim that every generated adaptation uses fresh external search; S4 is established by the shipped path that can distinguish external/current capabilities and close reusable adaptation when relevant.
- Generated downstream multi-agent systems are intentionally open-ended. They may implement S2/S3/S3*/S5 patterns beyond this assessment, but their user-authored semantics are not treated as out-of-box AutoAgent functions.
- No runtime trace was executed during this review; classification is based on pinned first-party source and documented standard modes.