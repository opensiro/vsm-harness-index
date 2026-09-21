---
harness_id: cuga
project_name: CUGA
repository: https://github.com/cuga-project/cuga-agent
review_ref: b3bdcaee74aaf7a53d3fb621b781d305fb714f5d
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CUGA

## Review boundary

- System in focus: the shipped CUGA agent harness at one installed/deployed product boundary, including the first-party `CugaAgent` / CugaLite model-tool runtime, `CugaSupervisor` multi-agent mode, policy/HITL machinery, skills loader, agent/server management surfaces and the first-party event service that invokes CUGA workers.
- Purpose and identity: execute complex enterprise tasks across web/API/tool environments and, in supervisor mode, compose several specialized agents into one adaptive task-execution organization.
- Relevant environment: users and host applications, model providers, browsers/APIs/MCP tools, external A2A agents, external event transports/services, optional Evolve service/package, external Activepieces service and operator/administrator input.
- Standard-distribution boundary: repository-shipped Python SDK, graph/runtime code, server/CLI/UI/event-service surfaces and built-in policy/skill integrations at the frozen revision. Model providers, external A2A agents, Evolve's adaptation logic, Activepieces execution and third-party MCP/application behavior remain outside ownership even when CUGA ships a client/integration path.
- Credited operating / distribution surfaces: `CugaAgent`, CugaLite graph, `CugaSupervisor`, supervisor delegation tools/state, first-party code/tool executor, policy/HITL enforcement, skills discovery/loading, `/run` worker path and first-party event-service entry points.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests/development instructions, benchmark/evaluation work (the README points evaluation to the separate `cuga-evaluation` repository), demos used only as corroborating evidence, and repository-maintainer governance.
- First-party operating / deployment modes considered: SDK single-agent execution, SDK supervisor/multi-agent execution, CLI/Web/server execution, event-service-triggered worker invocation and configured policy/HITL modes.
- Recursion level: one CUGA harness installation. A running `CugaAgent` / CugaLite loop is an operational S1 unit. In `CugaSupervisor` mode, separately instantiated internal `CugaAgent` loops are candidate subordinate S1 units; external A2A agents remain environmental/adjacent actors and are not needed for the positive mappings below.
- Reviewed revision: `b3bdcaee74aaf7a53d3fb621b781d305fb714f5d`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

CUGA ships a first-party model-driven execution loop rather than only an integration shell. The shared graph builder wires `START -> prepare -> call_model <-> execute -> END`; the model response is parsed for executable code, the first-party executor runs that code against the current tool/variable context, and observations return to the next model step. `CugaAgent` exposes this runtime through the SDK and the server/CLI surfaces use the same product graph.

`CugaSupervisor` is a supported second operating mode. It owns a separate supervisor conversation, an available-agent registry, selected-agent history, per-agent results/chat histories/variables and aggregated supervisor variables. The supervisor model receives a complete catalog of the configured agents and first-party `delegate_to_*` tools. After each delegated `CugaAgent` run, CUGA records its result and variables; the next supervisor model step sees those accumulated outcomes and can choose a different next delegation, transform intermediate data, retry via another agent or finish. The supervisor prompt explicitly describes this as dynamic multi-agent coordination where later agent tasks can depend on earlier agent results.

CUGA also ships substantial governance and observability machinery. Policies can block intents, inject playbook/tool guidance and require human approval for generated actions; pre-execute VERIFY can reject a proposed write block and feed a revision request into the same production loop; post-execution reflection summarizes the just-produced output back into that loop. Skills are discovered from installed `SKILL.md` files and exposed through a read-only `load_skill` tool. An optional Evolve integration sends trajectories/facts to an external Evolve MCP service and later retrieves its generated guidelines/preferences for prompt injection. These mechanisms are classified below by organizational function rather than by their names.

## Operational model

For ordinary CugaLite operation, a user task enters the first-party graph. The model decides whether to emit executable code or a final answer. When it emits code, the runtime executes that code against available tools and variables, records the resulting observations, and loops them back into the model. This is the primary operational S1 closure.

In supervisor mode, each internal delegated `CugaAgent` has its own first-party operational loop. The parent supervisor model sees the whole configured team catalog and the accumulated current results/variables from subordinate work. It owns the discretionary choice of which subordinate to call next and how the next commitment should depend on current returned evidence. That establishes a current whole-team S3 path. It does not establish S2: the supported supervisor path deliberately serializes delegation calls into separate execution cycles and the reviewed code does not identify a concrete cross-S1 collision/oscillation plus a distinct attenuation mechanism.

The VERIFY/reflection machinery remains ordinary production checking. VERIFY receives the same task/history/variables/proposed code used by the live execution path and acts as a mandatory pre-write gate; reflection uses the active production model and the just-produced execution history/output. Neither supplies materially independent complementary access to operational reality. The optional Evolve path can change later prompts, but the adaptation judgment and generated guidelines reside in an external Evolve service/package, so CUGA's first-party client transport is not credited as repository-local S4 ownership.

## S1 — Operations

- State: A
- Function: perform substantive enterprise/web/API/tool work through an iterative model-selected action and observation loop.
- Disturbance / variety regulated: ambiguous user goals, changing browser/API/tool state, retrieved data, tool errors, generated-code outcomes, conversation context and intermediate task results.
- Decisive decision or feedback right: choose the next substantive code/tool/action step from current task context and observations, and decide whether to continue acting or return a final answer.
- Decision owner: the running CUGA model agent.
- Supporting / enforcement mechanisms: `CugaAgent`, CugaLite/shared agent graph, code extraction, `CodeExecutor`, variables/state storage, tool registry/MCP adapters, budgets, policy gates, context management and checkpointer-backed thread state.
- Closure path: user/host task → model call → model-selected executable action/tool use → first-party execution → returned output/variables → next model call → revised action or final answer.
- Boundary reachability: CUGA ships the SDK/CLI/server runtime and the shared graph used by supported `CugaAgent` execution; `build_agent_graph` explicitly closes the `call_model <-> execute` loop, so no downstream harness implementation is required to obtain the operational feedback path.
- Why this is / is not agent-owned: deterministic runtime code parses, constrains and executes model output, but removing the model actor removes the discretionary choice of substantive next action from current observations.
- Evidence: [`README.md`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/README.md), [`src/cuga/sdk.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/sdk.py), [`src/cuga/backend/cuga_graph/nodes/cuga_agent_core/graph/shared_graph.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_agent_core/graph/shared_graph.py), [`src/cuga/backend/cuga_graph/nodes/cuga_agent_core/graph/shared_nodes.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_agent_core/graph/shared_nodes.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider inference is execution substrate and is not imported as a separate organizational owner.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes a specific inter-S1 interference/oscillation plus a distinct attenuation relation that changes later S1 behaviour.
- Disturbance / variety regulated: no qualifying cross-S1 disturbance is established at the reviewed recursion.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: supervisor delegation tools, sequential delegation isolation, shared/supervisor variables, result transport, task todos, budgets and external-agent routing.
- Closure path: not applicable.
- Why this is / is not agent-owned: the supervisor model chooses and sequences subordinate work, but delegation, routing, shared variables and sequencing are not S2 without evidence that they attenuate a concrete disturbance among distinct operational S1 units.
- Evidence: [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/prompts/supervisor_lite_prompt.jinja2`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/prompts/supervisor_lite_prompt.jinja2), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/delegation.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/delegation.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: a downstream deployment could add a real collision/resource-contention relation, but generic supervisor choreography does not establish that relation for the repository-level assessment.

### Absence scope

- Surfaces inspected: supervisor agent registry/state, delegation functions, delegation execution loop, task todos, variable bridging, tool-call budgets, event-service agent runtime and multi-agent examples/documentation.
- Plausible first-party paths checked: sequential sub-agent delegation as coordination; shared variables/results as coordination; task ordering/todos; event routing; budget enforcement; external A2A routing.
- Why no material first-party path remains: every inspected path moves, orders, bounds or records work, but none supplies the Profile-required concrete inter-S1 conflict/oscillation witness plus an S2-specific attenuation relation and returned behavioural change distinct from generic task orchestration.

## S3 — Inside-and-now control

- State: A
- Function: in supported `CugaSupervisor` mode, regulate the current whole-team portfolio by selecting subordinate agents and changing later commitments from accumulated current results and shared variables.
- Disturbance / variety regulated: changing intermediate results, missing data, subordinate outputs that alter what work remains, and the need to choose which specialist should take the next current commitment.
- Decisive decision or feedback right: choose which configured subordinate agent to invoke next, what task/context to give it and whether current evidence warrants another delegation or completion.
- Decision owner: the model-driven `CugaSupervisor` actor.
- Supporting / enforcement mechanisms: complete configured agent catalog, `available_agents`, `selected_agents`, `agent_results`, per-agent histories/variables, supervisor variables, generated delegation code, variable bridge, code executor, budgets and optional plan-approval gate.
- Closure path: current task + whole configured team catalog + accumulated subordinate outcomes → supervisor model chooses next delegation/task → first-party delegated `CugaAgent` runs → result/variables are recorded in supervisor state → next supervisor model step revises the current team commitment or finishes.
- Boundary reachability: `CugaSupervisor` is exported by the first-party SDK and the repository ships its graph, prompt, state and delegation machinery; internal subordinates are ordinary first-party `CugaAgent` instances, so the current-control path is available without a downstream scheduler or supervisor implementation.
- Why this is / is not agent-owned: the runtime exposes the agent tools and deterministically executes generated delegation code, but the supervisor model owns the discretionary current-team choice of which specialist receives the next commitment and how returned team evidence changes subsequent work.
- Evidence: [`src/cuga/sdk.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/sdk.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/cuga_supervisor_graph.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/cuga_supervisor_graph.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/cuga_supervisor_state.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/cuga_supervisor_state.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/prepare_agents_and_prompt.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/prepare_agents_and_prompt.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the positive claim is not based on the word `Supervisor`. It rests on the shipped whole-team catalog plus accumulated subordinate outcomes feeding a model-owned decision over subsequent team commitments. Static budgets/approval are supporting constraints, not S3 ownership.
- Whole-system current view: the supervisor receives the configured team catalog and persists the set of selected agents together with current per-agent results, histories and variables plus aggregated supervisor variables across the active task.
- Current-control decision scope: assign the next current subtask to any configured subordinate, condition that assignment on prior team results/variables, retry or redirect work through another specialist, and terminate the team task when the current portfolio is sufficient.

## S3* — Complementary audit

- State: —
- Function: no material first-party path establishes sufficiently independent complementary access to operational reality beyond CUGA's ordinary production/reporting path.
- Disturbance / variety regulated: not established as S3* at the reviewed boundary.
- Decisive decision or feedback right: not established for a sufficiently independent audit function.
- Decision owner: not established.
- Supporting / enforcement mechanisms: pre-execute VERIFY, post-execution reflection, policy/tool guards, activity tracking, telemetry and run histories.
- Closure path: VERIFY can return a revision instruction into the ordinary agent loop and reflection can append a summary of execution output, but those are routine production-checking closures rather than independent complementary audit.
- Why this is / is not agent-owned: VERIFY/reflection can be model-driven, yet agent autonomy does not make a routine verifier S3*. The inspected checks use the production task/history/variables/proposed code or just-produced execution output and run inside the same operational graph rather than obtaining materially different access to operational reality.
- Evidence: [`src/cuga/backend/cuga_graph/nodes/cuga_lite/reflection/pre_execute.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_lite/reflection/pre_execute.py), [`src/cuga/backend/cuga_graph/nodes/cuga_lite/adapter/sandbox_node.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_lite/adapter/sandbox_node.py), [`src/cuga/backend/cuga_graph/nodes/cuga_lite/reflection/reflection.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_lite/reflection/reflection.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a deployment can attach an independent evaluator through external tooling; that adjacent evaluator is not imported into the standalone repository mapping.

### Absence scope

- Surfaces inspected: pre-execute VERIFY, post-execution reflection, tool/policy guards, activity tracker, telemetry/observability and run-history/event records.
- Plausible first-party paths checked: VERIFY as independent audit; reflection as complementary review; policy guards as audit; telemetry/traces/logs as independent reality access; event run history as audit evidence.
- Why no material first-party path remains: VERIFY and reflection are routine stages inside the production graph and consume the same production evidence; logs/history are observation records; policy guards are enforcement. None establishes a materially independent audit actor/access path that challenges ordinary operational claims and returns that distinct judgment into control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path establishes an external-and-prospective adaptation loop whose adaptation judgment is owned inside the assessed CUGA boundary.
- Disturbance / variety regulated: not established as repository-local S4.
- Decisive decision or feedback right: not established inside CUGA for creating future-oriented adaptation options from environmental change.
- Decision owner: not established inside the assessed boundary.
- Supporting / enforcement mechanisms: optional Evolve client integration, durable/user memory, installed skills, standing event flows, knowledge/RAG, reflection and configuration/publish surfaces.
- Closure path: the Evolve integration can send trajectories/facts to an external Evolve service and later inject returned guidelines/preferences into future prompts, but the adaptation judgment and guideline generation occur in that external service. Other inspected first-party mechanisms persist or trigger information without developing a repository-local prospective adaptation option.
- Why this is / is not agent-owned: CUGA transports trajectories to Evolve and consumes Evolve output, but removing the external Evolve decision service removes the adaptation judgment while the first-party client machinery remains. Installed skills are read-only at runtime (`load_skill`), and standing flows execute future events rather than adapt CUGA capability in response to a modeled future.
- Evidence: [`src/cuga/backend/evolve/integration.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/evolve/integration.py), [`src/cuga/backend/evolve/memory.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/evolve/memory.py), [`src/cuga/backend/skills/tools.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/skills/tools.py), [`src/cuga/backend/events/runtime.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/events/runtime.py).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: Evolve may itself implement a qualifying adaptation function at a wider assembled-system boundary; that would be a different system-in-focus and requires its own evidence rather than importing external behavior into CUGA.

### Absence scope

- Surfaces inspected: Evolve integration/memory feedback path, skills discovery/loading, knowledge/memory, reflection, event-driven standing flows, agent manager/publish/configuration surfaces and README feature claims.
- Plausible first-party paths checked: saved trajectories and later Evolve guidelines; user-fact memory; reusable skills; reflection/self-improvement language; event/cron/poll/push flows; mutable/published agent configuration.
- Why no material first-party path remains: first-party CUGA either stores/loads current information, executes preconfigured future triggers, or transports evidence to/from an external adaptation service. No inspected repository-local actor turns external/future distinctions into an adaptation option and closes that option back into changed present capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party path establishes identity/ethos/ultimate-policy adjudication for the CUGA organization at the declared recursion.
- Disturbance / variety regulated: no identity-level or S3-S4 policy tension is shown reaching a legitimate ultimate authority and returning as governing identity/policy.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: administrator-authored policy objects, Intent Guards, Playbooks, Tool Guides/Tool Guards, Tool Approval/HITL, plan approval, prompts/instructions, permissions and configuration management.
- Closure path: policy matching can block, guide, require approval or modify tool behavior for current work, but no identity/ultimate-policy issue → legitimate authority decision → returned governing-policy closure is established.
- Why this is / is not agent-owned: models may apply or respond to configured policies and humans may approve ordinary delegations/actions, but those are operational constraints/approvals. The code explicitly describes policy code as administrator-authored; it does not supply an agent-owned or parent-governed identity adjudication process merely because policy is mutable.
- Evidence: [`src/cuga/backend/cuga_graph/policy/models.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/policy/models.py), [`src/cuga/sdk.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/sdk.py), [`src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py`](https://github.com/cuga-project/cuga-agent/blob/b3bdcaee74aaf7a53d3fb621b781d305fb714f5d/src/cuga/backend/cuga_graph/nodes/cuga_supervisor/nodes/execute_agent_tool.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an organization deploying CUGA may supply its own legitimate governance authority and encode resulting policies through these surfaces; that parent organization is outside the standalone repository boundary.

### Absence scope

- Surfaces inspected: policy models/storage/SDK mutation surfaces, intent blocking, playbooks/tool guides/tool guards, tool/plan approval, HITL resumption, prompt/instruction configuration, manage/publish surfaces and permissions.
- Plausible first-party paths checked: policy files as S5; admin policy CRUD as S5; human tool/plan approval as parent S5; supervisor instructions/prompts as identity; publish/version controls as ultimate-policy governance.
- Why no material first-party path remains: all inspected mechanisms configure or enforce operational behavior, permissions and current-task approvals. None establishes the required identity/ultimate-policy issue, legitimate adjudication authority and returned closure governing the organization at this recursion.

## Decision-right inventory

| Function | State | Decisive organizational right | Owner |
| --- | --- | --- | --- |
| S1 | A | Choose substantive next tool/code/action from current task evidence | Running CUGA model agent |
| S2 | — | No qualifying inter-S1 attenuation right established | — |
| S3 | A | Choose and revise current subordinate commitments from whole-team catalog and accumulated results | `CugaSupervisor` model actor |
| S3* | — | No sufficiently independent complementary audit judgment established | — |
| S4 | — | No repository-local prospective adaptation-option judgment established | — |
| S5 | — | No identity/ultimate-policy adjudication right established | — |

## Assessment summary

CUGA closes a strong autonomous operational loop and, in its supported multi-agent supervisor mode, a separate autonomous current-control loop: the supervisor model sees the configured team plus accumulated subordinate results and owns subsequent team commitments. That is S3, not S2; the reviewed implementation does not tie its routing/sequencing to a concrete inter-S1 disturbance/attenuation relation.

Its verifier/reflection machinery is substantial but remains routine production checking rather than independent complementary audit. Its optional Evolve integration can feed externally generated guidance back into later CUGA prompts, but the prospective adaptation judgment resides outside the first-party repository boundary. Policy/HITL features likewise constrain and approve current operation without establishing identity-level S5 closure.

**Proposed autonomy vector:** `A — A — — —`.
