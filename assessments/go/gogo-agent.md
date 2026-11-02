---
harness_id: gogo-agent
project_name: gogo-agent
repository: https://github.com/DAgogo04/gogo-agent
review_ref: c6600ddcf824fda075b5f799a0a80976cbc5023e
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# gogo-agent

## Review boundary

- System in focus: the shipped local-first Gogo personal-assistant harness, its model/tool loop, memory and optional graph workflows in ordinary CLI/dashboard/gateway use.
- Purpose and identity: respond to personal-assistant requests with model-directed tools, persist relevant personal knowledge and expose trace/inspection surfaces under the operator's control.
- Relevant environment: user requests and preferences, files and calendar, provider/tool failures, network integrations, previously stored facts, changing research inputs and task budgets.
- Standard-distribution boundary: Python `gogo` package and its supported `Gogo.respond` runtime, `loop/`, `memory/`, `graph/`, `runtime/`, gateway integrations and optional local operations dashboard. External model providers and MCP services are dependencies, not credited first-party decision owners.
- Credited operating / distribution surfaces: `gogo/app.py`, `gogo/loop/agent.py`, `gogo/runtime/session.py`, `gogo/memory/{retrieval_gate.py,consolidation.py}`, `gogo/graph/{engine.py,workflows/triage.py,workflows/gather.py}`, registered tools and operational turn trace/evals readback where in-scope.
- Adjacent first-party surfaces excluded from ownership: `evals/` development/CI suites and `gogo/ops/release_gate.py` release qualification, experimental arena/model races, benchmark verdicts, contributor governance, roadmap/work-in-progress examples and documentation-only proposed workflows. On-demand operator dashboard button for judging a completed turn is treated as an observability feature unless it returns corrective authority into operation.
- First-party operating / deployment modes considered: local Python CLI/default agent, dashboard and additional gateway input paths, optional `GOGO_GRAPH_WORKFLOWS` triage, `gogo gather` graph command, SQLite memory plus configurable external memory mirror, model/provider/tool configuration and operator-controlled turn judging. No live provider key or hosted service E2E was used.
- Recursion level: one Gogo personal-assistant organization with one active main model/tool operational loop; graph steps can instantiate nested `agent_node` loops but mere graph nodes are not independent viable S1 organizations.
- Reviewed revision: `DAgogo04/gogo-agent@c6600ddcf824fda075b5f799a0a80976cbc5023e` (GitHub repository ID 1435500308), immutable intake #2578 / controller #2579.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/README.md) describes four shipped pillars: Harness, Loop, Memory and Eval. [`Gogo.respond`](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/app.py) composes provider, tool registry, memory, session and trace, then optionally tries graph triage before falling back to the ordinary agent loop. The [model/tool loop](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/loop/agent.py) repeatedly calls a model, executes selected tools, feeds observations back and stops naturally or at a hard iteration ceiling. [Session composition](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/runtime/session.py) adds editable SOUL instructions, time, history, retrieved memory and selected skills. [Consolidation](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/memory/consolidation.py) periodically distills facts/episodes to SQLite and optional external memory; retrieval and slot gates choose prompt context. The [graph engine](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/graph/engine.py) schedules deterministic dependency waves, rejects simultaneous writes to the same blackboard key, bounds loops and records errors. The supported [triage graph](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/graph/workflows/triage.py) classifies quick vs full turns and falls back to the regular loop; `gogo gather` uses parallel fixed information-gathering nodes. The [turn evals](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/ops/turn_evals.py) grade finished traces, while developer-facing [eval/release gates](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/docs/evals.md) check code/release quality outside the user's operational agent loop.

## Operational model

The assistant model owns ordinary tool selection and response synthesis; deterministic gates, graph routing and memory selection bound or organize it. A single Gogo turn, even with multiple parallel graph data collectors, is not evidence of several competing autonomous business units. An optional `agent_node` is a constructor for a nested loop, not a shipped conflict-resolution protocol. User changes to persona/skills, manual model selection and source maintenance remain distinguished from autonomous whole-system governance.

## S1 — Operations

- State: A
- Function: answer and act on personal-assistant goals using model-directed file/calendar/memory/research/tool calls.
- Disturbance / variety regulated: varying user requests, facts, tool observations, missing memory, provider results and newly learned conversation context.
- Decisive decision or feedback right: select and revise tool calls and final reply based on the current task and observed tool results.
- Decision owner: the running Gogo model/tool agent, using an external provider through the first-party client adapter.
- Supporting / enforcement mechanisms: registered tool schemas, `max_iterations`, quick/full triage option, working-memory assembly, SQLite, memory retrieval, traces and gateway UI.
- Closure path: gateway message → `Gogo.respond` → working-memory build → `run_loop` model/tool cycle (or small quick reply) → tool-result return → reply → persisted exchange/consolidation → later turn.
- Boundary reachability: the installed `gogo` CLI/dashboard routes through `Gogo.respond`; `run_loop` is the real runtime, not a fixture. The opt-in graph path preserves the full loop as an operational node.
- Why this is / is not agent-owned: remove model reasoning and only the deterministic tool dispatcher/memory store remains, not comparable autonomous goal pursuit.
- Evidence: [app wiring](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/app.py), [agent loop](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/loop/agent.py), [README](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/README.md).
- Basis: structural
- Confidence: high
- Caveats: no live model/provider E2E was performed; agentic action ownership is at turn/task recursion, not proven metasystem governance.

## S2 — Coordination

- State: —
- Function: no operating mode with feedback-closed regulation of demonstrated interference among distinct autonomous S1 units is established.
- Disturbance / variety regulated: possible competing writes or step ordering in graph branches, repeated tool calls and inconsistent results are candidate disturbances; the graph checks state collisions but does not negotiate substantive inter-S1 goals.
- Decisive decision or feedback right: settle inter-agent interference and modify subsequent S1 commitments; none is evidenced in supported workflows.
- Decision owner: graph developer predetermines edges and keys; the runtime follows dependencies and raises `GraphStateCollision`. An independent multi-agent coordination judgment owner is absent.
- Supporting / enforcement mechanisms: DAG wave scheduling, disjoint-key enforcement, route labels, visit/step bounds, per-turn tool-call guard and the optional `agent_node` factory.
- Closure path: graph nodes feed their data to later single-turn synthesis; a collision raises or records error, not a cross-agent conflict resolution returned to the competing agents' plans.
- Why this is / is not agent-owned: data fan-in, deterministic branch routing, a collision exception and node spawning are not a functional S2 feedback mechanism among distinct operational agents.
- Evidence: [graph engine](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/graph/engine.py), [node factories](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/graph/nodes.py), [loop-vs-graph documentation](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/docs/loop-vs-graph.md).
- Basis: structural
- Confidence: medium
- Caveats: generic `agent_node` could be configured by a user into a custom multi-agent protocol; the shipped supported modes do not demonstrate one.

### Absence scope

- Surfaces inspected: default loop, graph engine/nodes, actual triage and gather workflow, tool registry and optional graph wiring.
- Plausible first-party paths checked: parallel graph writes, wave barriers, route choices, nested agent nodes, tool reuse, shared blackboard and error-handling paths.
- Why no material first-party path remains: the shipped graph handles data-flow integrity and one assistant's task steps; no specific interfering S1 units and conflict attenuation with post-decision feedback are supported.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous or parent-returned discretionary whole-organization inside/current control distinct from individual assistant turn execution.
- Disturbance / variety regulated: turn token/spend ceiling, tool availability, memory/storage consistency, loop iterations, provider failures and queued gateway inputs.
- Decisive decision or feedback right: choose shared priority/resource commitments and intervene among several operational units for the present whole; no such owner/path is shipped.
- Decision owner: operator sets deployment and tools; deterministic runtime enforces iteration limits, budgets/availability indications and graph edges; the model picks work within one turn.
- Supporting / enforcement mechanisms: `max_iterations`, `GOGO_TURN_BUDGET_USD` post-hoc grade, tool availability prompt, graph visit caps, usage ledger and trace dashboard.
- Closure path: hard stops and ordinary errors feed a single turn's answer; traces/dashboard expose facts after operation without a whole-current resource-priority decision returned to other units.
- Why this is / is not agent-owned: the runtime cap or monitoring would still function without an S3 decision agent; no cross-unit current-control right is modeled.
- Evidence: [run loop](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/loop/agent.py), [app wiring](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/app.py), [turn checks](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/ops/turn_evals.py).
- Basis: structural
- Confidence: medium
- Caveats: a single agent can manage its own local task budget; that does not establish a distinct recursion-level metasystem or parent return.

### Absence scope

- Surfaces inspected: loop limit, graph scheduling, Gogo app assembly, budget/trace evaluation, gateway and operator configuration.
- Plausible first-party paths checked: budget status, model choice, error recovery, graph execution order, memory management, dashboard intervention and human config controls.
- Why no material first-party path remains: these are single-turn constraints, user-selected tasks or after-the-fact telemetry; no whole-current decision right/feedback closure over operational commitments is shipped.

## S3* — Complementary audit

- State: —
- Function: no independent operational audit with authority to correct an agent's produced answer before or after acceptance is closed.
- Disturbance / variety regulated: fabricated numeric claims, ungrounded replies, failed-tool concealment, overspend, duplicate reports and weak judged answers.
- Decisive decision or feedback right: an independent auditor could challenge these claims and force revised operation; shipped turn checks and on-demand judge do not exercise that right.
- Decision owner: deterministic check code reads the completed trace; optional operator-triggered provider judge scores one stored response, but the observed answer has already been delivered and no corrective action follows by design.
- Supporting / enforcement mechanisms: trace capture, five 0/1/n-a turn checks, optional `Judge this turn` model call and separate offline developer/release gates.
- Closure path: score/grade appears on Evals/Observability after a finished turn; `turn_evals.py` explicitly says checks never stop, rewrite or delay a reply. No audit judgment → mandatory correction → subsequent operational change is wired.
- Why this is / is not agent-owned: even where a different model supplies a judgment, a score-only observation lacks complementary S3* corrective closure; CI/release qualification concerns source development.
- Evidence: [turn evals](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/ops/turn_evals.py), [eval docs](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/docs/evals.md), [release gate](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/ops/release_gate.py).
- Basis: explicit
- Confidence: high
- Caveats: the on-demand scorer is independent in some possible provider configurations but not a corrective audit authority; no status upgrade from evaluator existence alone.

### Absence scope

- Surfaces inspected: operational turn-eval code/docs, trace readback, on-demand judge, developer eval suites, release gate and `Gogo.respond` result persistence.
- Plausible first-party paths checked: numeric grounding checks, budget grading, independent LLM judgment, deterministic test regression gate and graph `on_error` branches.
- Why no material first-party path remains: source explicitly confines operational grades to completed turns without stopping/rewriting/delaying replies; development release tests are outside runtime ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: no whole-assistant external/prospective adaptation option selection with returned capability-change governance is evidenced.
- Disturbance / variety regulated: changing research information, user preferences, model providers, new tools, durable facts and future tasks.
- Decisive decision or feedback right: weigh outside/future alternatives and choose systemic capability adaptation rather than merely perform a user's task or retain its context; no such distinct mechanism is established.
- Decision owner: the model and memory summarizer choose task facts/actions; users/maintainers install tools, approve persona/skill changes and select providers.
- Supporting / enforcement mechanisms: retrieval gate, consolidation and slot scoring, procedural skills, editable `SOUL.md`, graph triage, external MCP memory and research report memory.
- Closure path: retained facts/persona/tools influence later task prompts, but no prospective environment-sensing → strategic adaptation choice → authorized change of whole operating capability is presented as a first-party closed loop.
- Why this is / is not agent-owned: persistent memory and task learning are substantive S1 support, not automatically S4; authoring a skill on a user's instruction is a task/configuration change.
- Evidence: [memory consolidation](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/memory/consolidation.py), [session/persona](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/runtime/session.py), [app](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/app.py), [roadmap](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/docs/roadmap.md).
- Basis: structural
- Confidence: medium
- Caveats: memory can alter responses and user-taught skills can change procedures; neither proves whole-system future-adaptation governance at this recursion.

### Absence scope

- Surfaces inspected: memory selection/consolidation, session `SOUL.md`, procedural skills, providers, graph routing, ops evals and roadmap.
- Plausible first-party paths checked: learned facts influencing future prompts, user-approved skill creation, model selection, research update checks and CI/release tuning.
- Why no material first-party path remains: these are memory/context management, explicit operator configuration or out-of-boundary development; no distinct prospective adaptation decision feeds back into an authorized system-capability mode.

## S5 — Policy and identity

- State: —
- Function: no deliberate ultimate-policy/identity arbitration by a legitimate first-party governance authority with operational return is shown.
- Disturbance / variety regulated: assistant persona/rules, provider choice, access keys, user permissions, calendar/outbox boundaries and tool restrictions.
- Decisive decision or feedback right: decide unresolved ultimate identity or policy commitments and bind all subsequent organizational action; neither model nor runtime is assigned this right.
- Decision owner: user edits `SOUL.md` and confirms skill additions, developer defines static defaults, tool code enforces configured boundaries; these do not document an S5 adjudication loop.
- Supporting / enforcement mechanisms: default SOUL rules, tool schemas, approval/config values, unavailable-tool list, prompt requirements, fixed iteration limits and local storage.
- Closure path: preselected instructions constrain model turns; no identity-level conflict is escalated through legitimate policy authority and returned as a binding revised operating principle.
- Why this is / is not agent-owned: having an editable persona and a model capable of writing preferences is not proof of an autonomous identity-policy governor.
- Evidence: [session/default SOUL](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/runtime/session.py), [config](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/config.py), [app](https://github.com/DAgogo04/gogo-agent/blob/c6600ddcf824fda075b5f799a0a80976cbc5023e/gogo/app.py).
- Basis: structural
- Confidence: medium
- Caveats: human authority to edit rules is external baseline control; no separately proven S5 parent return should be inferred from that fact.

### Absence scope

- Surfaces inspected: session/persona initialization, user-specified skills, config and provider choice, tool constraints, memory and normal response loop.
- Plausible first-party paths checked: update-SOUL tool, skill creation consent, source-defined rules, prompts that govern tool use, local dashboard settings and maintainer/release decisions.
- Why no material first-party path remains: shipped features implement user-configured behavior and per-task decision-making, not the identity/ultimate-policy adjudication and closure of a viable metasystem.

## Distributed OSS parent arrangement

Gogo is a personal, locally controlled assistant; users with separate home databases and public repo maintainers are not shown as a common recursive parent organization. An operator may edit model, memory or SOUL, but no parent S3/S4/S5 decision-return topology is supported at this reviewed runtime recursion.

## Self-hosted and non-human modes

Local CLI/dashboard/gateway use, opt-in graph triage and optional MCP memory all retain the model-directed S1 loop. `GOGO_GRAPH_WORKFLOWS` changes task routing, not an inter-agent governing system. A fully automated memory consolidator is an internal persistence/selection service; the human can configure it, but it is not a separate non-human S4 or S5 organization.

## Recursion

The graph can instantiate agent loops as nodes, yet the shipped triage has one full-agent path and gather uses fixed data collectors. Nested agent loops and multiple gateways do not establish independently viable subordinate systems or a whole-system inter-S1 controller.

## Variety and escalation

Memory retrieval gates, periodic consolidation, tool result observation, graph order/collision checks, iteration caps and error surfacing bound operational variety. Traces and five post-hoc turn grades provide diagnostic signals, but their display is not itself evidence of an algedonic path into an S3/S4/S5 owner.

## Evidence gaps

The assessment is source-first at the exact frozen commit; it did not use external model APIs or reproduce a live dashboard session. The code contains multiple operator-facing and development-only evaluation systems; no operational corrective audit loop is inferred from those. Generic graph factories could be extended by a user, but only the documented shipped triage/gather modes are credited.
