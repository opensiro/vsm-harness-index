---
harness_id: water
project_name: Water
repository: https://github.com/manthanguptaa/water
review_ref: 454a86b79980877ed77d38ad1a150246a9bf1cf2
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Water

## Review boundary

- System in focus: the first-party `water-ai` Python package at pinned revision `454a86b79980877ed77d38ad1a150246a9bf1cf2`, including its ReAct task loop, tool/subagent support, multi-agent team orchestrator, dynamic planner, shared context, approvals, guardrails, memory, resilience and execution/deployment surfaces.
- Purpose and identity: provide an agent harness framework around model-backed tasks and flows, with a first-party autonomous ReAct operating path plus composable orchestration, resilience, safety and deployment machinery.
- Relevant environment: user goals, model responses/tool calls, tool outputs, flow/task state, subordinate agent results, shared team state/messages/history, guardrail findings, persistent memories, external services and human approval responses.
- Standard-distribution boundary: shipped `water` package runtime and documented/cookbook-supported operating modes. External model providers, remote A2A/MCP agents, LangChain/CrewAI/Agno and other third-party agent frameworks remain outside ownership. User application code that supplies tasks, policies, callbacks or custom evaluators is external composition unless the package itself closes the relevant function.
- Credited operating / distribution surfaces: `water.agents.react.create_agentic_task`; first-party Tool/Toolkit and subagent wrappers; `AgentOrchestrator`/`SharedContext`; `PlannerAgent`; guardrails/retry; memory; approvals; core Flow/Task execution; shipped tests and cookbook examples that demonstrate supported usage.
- Adjacent first-party surfaces excluded from ownership: repository CI; benchmark/eval runs when used only as offline quality measurement; cookbook application-specific decision logic; maintainer/version-release governance; downstream integrations whose autonomous decisions are made by external agent frameworks or services.
- First-party operating / deployment modes considered: single ReAct agentic task; parent ReAct agent with isolated subagent tools; multi-agent sequential/round-robin/dynamic team modes; planner-generated current task plan; approval-gated flow; guardrail retry; memory-enabled runs; ordinary server/trigger/deployment modes.
- Recursion level: one Water harnessed task/team organization. A model-controlled ReAct task is an operational S1 unit. In team mode, `AgentRole` tasks can be distinct S1 units at the team recursion. An isolated subagent invoked as a Tool is subordinate operation; spawning alone is not credited as VSM recursion.
- Reviewed revision: `454a86b79980877ed77d38ad1a150246a9bf1cf2`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Water is a Python harness framework containing both deterministic flow infrastructure and a first-party autonomous agent loop. Its core `create_agentic_task` implementation runs a Think-Act-Observe-Repeat loop: the model receives current messages and available tool schemas, chooses tool calls, Water executes them, observations are fed back, and the model decides subsequent actions or stops. Optional callbacks can reject/modify tool calls or stop the loop, but they do not replace the model-owned ordinary operating discretion. `create_sub_agent_tool` constructs a fresh isolated Water ReAct loop for a child and exposes it as a parent tool.

The multi-agent layer is a separate constructor surface. `AgentOrchestrator` maintains `SharedContext` containing team state, messages and execution history and injects that whole-team snapshot into each role's task input. Its `dynamic` strategy accepts `_next_agent` from the current role, validates that target against the team and `can_delegate_to`, and changes which S1 unit receives the next commitment. This is a function-specific current-control path rather than a generic message bus alone. However the repository's own cookbook and tests wire the dynamic decision to ordinary Python task functions (`router_execute`, `make_fn`) rather than to an autonomous model-owned controller. A downstream user can compose a model-driven task that consumes `_shared_context` and emits `_next_agent`, but the standard first-party evidence does not already close that autonomous owner. The mapping is therefore S3 constructor (`C`), not S3 autonomous (`A`).

`PlannerAgent` is model-driven but performs goal decomposition before executing a fixed ordered plan; it does not continuously regulate the current whole-team organization from execution feedback. The guardrail retry layer can feed validation failures into another attempt, but the judgment is supplied by a configured `check_fn`/guardrail rather than an independently positioned audit actor. Water's `LLMJudge` is an offline EvalSuite evaluator: it scores completed `flow.run` output against expected results and returns an `EvalScore`; no first-party path returns that score into the live production run. Layered memory—including `AUTO_LEARNED` entries writable by agent tools—persists information and can influence later prompts, but the package does not turn prospective external distinctions into adaptation options that change the harness's future capability. Approval gates, risk policies and ORG-priority memory are operating constraints/data, not identity or ultimate-policy closure.

Primary evidence:

- [`README.md`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/README.md) — framework boundary and documented ReAct, team, planner, approval, memory, guardrail/eval/resilience modes.
- [`water/agents/react.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/react.py) — first-party model-controlled Think-Act-Observe-Repeat loop and feedback closure.
- [`water/agents/subagent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/subagent.py) — isolated subordinate Water ReAct loops exposed as parent tools.
- [`water/agents/multi.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/multi.py) — whole-team shared state/history and dynamic `_next_agent` current-control constructor path.
- [`tests/test_multi_agent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/tests/test_multi_agent.py) and [`cookbook/agents/multi_agent_flow.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/cookbook/agents/multi_agent_flow.py) — supported dynamic team path is exercised with developer-authored Python decision functions.
- [`water/agents/planner.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/planner.py) — model-generated current-goal execution plans, distinct from ongoing whole-system control or prospective adaptation.
- [`water/guardrails/retry.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/guardrails/retry.py) — configured guardrail findings can be returned as retry feedback.
- [`water/eval/evaluators.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/eval/evaluators.py) and [`water/eval/suite.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/eval/suite.py) — LLMJudge scores completed outputs and records reports without live corrective closure.
- [`water/agents/memory.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/memory.py) — layered persistent memory and agent-writable `AUTO_LEARNED` entries.
- [`water/agents/approval.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/approval.py) — configured auto/human approval gate and timeout behavior.

## Operational model

In Water's first-party ReAct mode, the developer supplies a model provider, tools and optional operating constraints. Water owns the loop structure and action/observation return path, while the running model decides which available tools to call and whether to continue. Tool results are appended to message history and become evidence for the next model decision. Isolated subagents use the same Water loop and return a bounded summary to the parent.

In multi-agent team mode, Water owns the team registry, shared current state/messages/history and transition machinery. Sequential and round-robin modes are deterministic. Dynamic mode exposes a special `_next_agent` return field through which the current role may change which team member runs next, subject to `can_delegate_to`. That is sufficient to expose a current-control construction path but not to establish autonomous ownership in the shipped standard mode: tests and cookbook examples make the next-agent decision in application Python. Generic team messaging and sequencing do not establish S2 because no concrete cross-S1 interference/oscillation and distinct attenuation loop is evidenced.

The remaining subsystems are mechanisms rather than additional autonomous organizational owners. PlannerAgent creates a current task plan; approvals enforce configured risk policy or a human decision; guardrails validate outputs and may retry with feedback; offline evals measure finished runs; memory persists notes; resilience/checkpoint/trigger machinery executes authored policies. None of those inspected standard paths closes independent S3* audit, prospective S4 capability adaptation or S5 identity/ultimate-policy authority.

## S1 — Operations

- State: A
- Function: autonomously execute an assigned task through a model-controlled Think-Act-Observe-Repeat loop using first-party Water tools and returned observations.
- Disturbance / variety regulated: task ambiguity, changing tool/environment state, tool failures/results, intermediate evidence and uncertainty about which action should be taken next.
- Decisive decision or feedback right: select substantive tool calls/actions from current evidence and decide whether to continue or conclude the task.
- Decision owner: the running model inside Water's first-party `create_agentic_task` loop.
- Supporting / enforcement mechanisms: provider adapter, Toolkit/Tool execution, message/tool-call normalization, max-iteration limit, optional `__done__` tool, callbacks, stop condition, sandbox/context/memory/resilience capabilities.
- Closure path: user/task input → model response/tool choice → Water executes selected tool → observation appended as tool message → next model decision → repeated action or terminal response.
- Boundary reachability: `create_agentic_task` is exported from the installed `water.agents` package and documented in the top-level README as the first-party Agentic Loop; subordinate agent tools instantiate the same loop directly.
- Why this is / is not agent-owned: Water's deterministic runtime transports and bounds actions, while the model chooses the operational action from current observations in the ordinary path. Optional callbacks may override individual calls but do not remove the available autonomous mode.
- Evidence: [`water/agents/react.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/react.py), [`README.md`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/README.md), [`water/agents/subagent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/subagent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model providers supply inference but do not own Water's first-party loop mechanics. Generic `create_agent_task` one-shot LLM tasks are not the S1 basis; the explicit ReAct implementation is.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced S2-specific attenuation of concrete interference/conflict/oscillation among distinct Water S1 units is established in the reviewed standard distribution.
- Disturbance / variety regulated: no specific inter-S1 disturbance satisfying the Profile witness is established.
- Decisive decision or feedback right: none established for an S2-specific attenuation relation.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: SharedContext state/message bus, deterministic sequential/round-robin execution, dynamic handoff, subagent isolation, DAG/parallel flow primitives and delegation permissions.
- Closure path: no qualifying inter-S1 disturbance → attenuation decision/relation → returned change in subsequent S1 behaviour loop is established.
- Why this is / is not agent-owned: Water supplies substantial communication, isolation, sequencing and routing machinery, but the Methodology does not treat those generic primitives as S2 without evidence of an actual/structurally evidenced interference and a relation specifically attenuating it.
- Evidence: [`water/agents/multi.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/multi.py), [`tests/test_multi_agent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/tests/test_multi_agent.py), [`water/agents/subagent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/subagent.py).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: a downstream Water application could define a real S2 disturbance and use these mechanisms to regulate it; that would be a separate system-in-focus and does not upgrade the repository-level assessment.

### Absence scope

- Surfaces inspected: multi-agent SharedContext/orchestrator, dynamic delegation and permissions, subagent isolation, README flow patterns, team cookbook/tests, parallel/DAG/round-robin modes.
- Plausible first-party paths checked: message bus, shared state, handoffs, parallel agents, deterministic round-robin, delegated isolated ReAct children and dependency sequencing.
- Why no material first-party path remains: inspected paths move information, isolate contexts or select execution order, but none identifies a concrete inter-S1 collision/oscillation and a distinct Water-owned attenuation relation with feedback into later S1 behaviour.

## S3 — Inside-and-now control

- State: C
- Function: expose a whole-team current-control path that can choose which operational role receives the next commitment from current team state/history.
- Disturbance / variety regulated: changing team state, accumulated role outputs/messages/history and the need to choose or stop the next active role within current work.
- Decisive decision or feedback right: emit `_next_agent` from the currently executing team role, thereby selecting the next S1 commitment or ending the dynamic chain; Water validates the requested target and delegation authority.
- Decision owner: constructor path. Water exposes the S3-specific whole-team state/transition interface, but application/developer-composed task logic owns the decisive choice in the shipped examples/tests; an autonomous controller must still be composed to receive `A`.
- Supporting / enforcement mechanisms: `SharedContext` state/messages/history, injection of `_shared_context` and `_agent_messages`, team registry, `can_delegate_to`, max-round limit and deterministic transition validation.
- Closure path: whole-team SharedContext snapshot → current role/task decision emits `_next_agent` → Water validates role and delegation permission → selected role runs next with updated current state/history → later team operation changes.
- Boundary reachability: `AgentOrchestrator(strategy='dynamic')`, SharedContext injection and `_next_agent` handling are shipped package APIs with direct tests and cookbook usage; no custom Water runtime implementation is needed, only composition of the decisive autonomous actor/logic.
- Why this is / is not agent-owned: the first-party primitive is function-specific, but Water's own supported examples/tests use ordinary Python functions to choose `_next_agent`. Therefore the current-control function is exposed but autonomous ownership is not closed by the repository standard distribution.
- Evidence: [`water/agents/multi.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/multi.py), [`tests/test_multi_agent.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/tests/test_multi_agent.py), [`cookbook/agents/multi_agent_flow.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/cookbook/agents/multi_agent_flow.py).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: `_next_agent` alone would be ordinary routing; the S3 constructor claim additionally relies on Water injecting the whole team's state/messages/history into the role and using the returned decision to alter current team commitments. There is no shipped autonomous controller tied to this interface, so `A` is not claimed. Approval gates, rate limits and schedulers are enforcement mechanisms and are not counted as S3 ownership.
- Whole-system current view: every role task receives a serialized `SharedContext` containing current shared state, all messages and execution history, plus messages addressed to that role.
- Current-control decision scope: choose the next team member to operate (within delegation constraints) or terminate the dynamic handoff chain, changing the team's current allocation of work.

## S3* — Complementary audit

- State: —
- Function: no live, sufficiently independent complementary audit path is established that returns an audit judgment into subsequent Water operation.
- Disturbance / variety regulated: potential hidden divergence between ordinary production reports/outputs and operational reality is not covered by a qualifying first-party audit loop.
- Decisive decision or feedback right: none established for independent audit judgment with production feedback closure.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: deterministic/LLM evaluators, guardrails, RetryWithFeedback, observability/traces and ordinary reviewer tasks can inspect outputs, but their roles/closure do not establish S3* at the reviewed boundary.
- Closure path: no qualifying complementary evidence → independent audit verdict → corrective return into live/subsequent operation loop is established.
- Why this is / is not agent-owned: `LLMJudge` is an agentic evaluator, but it runs after a completed `flow.run` against expected output and writes `EvalScore`/report state rather than steering the production run. RetryWithFeedback closes configured guardrail failures into retries, but the judgment comes from application-supplied `check_fn`/guardrail rules rather than a separately evidenced independent audit actor.
- Evidence: [`water/eval/evaluators.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/eval/evaluators.py), [`water/eval/suite.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/eval/suite.py), [`water/guardrails/retry.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/guardrails/retry.py).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: applications may wire evaluation/reviewer outputs back into a later flow, but that closure is not supplied as a standard first-party audit mode here.

### Absence scope

- Surfaces inspected: EvalSuite, LLMJudge and deterministic evaluators; guardrail base/retry surfaces; observability/trace inventory; team reviewer cookbook pattern; ReAct callbacks.
- Plausible first-party paths checked: LLM-as-judge, post-run eval, guardrail retry feedback, trace/telemetry and reviewer role naming.
- Why no material first-party path remains: eval judgments terminate in reports/scores, while guardrail retries use configured validation rather than an independently positioned complementary audit actor. No inspected standard path satisfies both independence/complementary access and corrective return into production operation.

## S4 — Intelligence/adaptation

- State: —
- Function: no prospective environment-facing adaptation loop is established that develops options and changes Water's future operating capability.
- Disturbance / variety regulated: no first-party path is established for future-relevant environmental change requiring adaptation of the harness's capabilities/organization.
- Decisive decision or feedback right: none established for choosing and incorporating a future capability adaptation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: PlannerAgent, persistent layered memory including `AUTO_LEARNED`, eval reports, plugin/configuration surfaces, versioning and ordinary user/developer composition can alter what later runs know or execute.
- Closure path: no qualifying external/prospective distinction → adaptation options → selected option → change to present capability/S3 loop is established.
- Why this is / is not agent-owned: model planning decomposes the current goal; memory tools store/retrieve notes; evals measure outputs. None of these inspected paths autonomously translates future/environmental intelligence into a changed Water capability or organizational design.
- Evidence: [`water/agents/planner.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/planner.py), [`water/agents/memory.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/memory.py), [`water/eval/suite.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/eval/suite.py).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: `AUTO_LEARNED` is a storage layer name, not evidence of a prospective adaptation function; downstream code can use memories/evals to redesign a harness, but that is external composition.

### Absence scope

- Surfaces inspected: dynamic PlannerAgent; layered memory/AUTO_LEARNED tools and prompt injection; eval suite/reports; plugin/versioning inventory; ReAct/subagent/team runtime.
- Plausible first-party paths checked: learning from stored memories, current-goal replanning, eval-driven improvement, plugin loading and persistent checkpoint/recovery.
- Why no material first-party path remains: inspected mechanisms preserve information, execute current plans or expose developer extension, but do not produce an operationally closed prospective outside→options→future-capability adaptation loop.

## S5 — Policy/identity

- State: —
- Function: no runtime identity or ultimate-policy authority loop is established at the reviewed Water harness/team boundary.
- Disturbance / variety regulated: no identity/ultimate-policy dispute requiring authoritative organizational closure is evidenced.
- Decisive decision or feedback right: none established for S5-level identity or ultimate policy.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: developer system prompts, guardrails, risk/approval policies, ORG-priority memory, tool permissions, delegation constraints, rate/budget limits and human approve/deny actions constrain ordinary operation.
- Closure path: no qualifying identity/ultimate-policy matter → authoritative S5 decision → returned governance of subsequent operation loop is established.
- Why this is / is not agent-owned: Water's policy-like mechanisms enforce authored operating constraints or local action approvals. Neither a prompt nor a human approval of a risky task becomes S5 without evidence that it closes identity/ultimate-policy authority at this recursion.
- Evidence: [`water/agents/approval.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/approval.py), [`water/agents/memory.py`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/water/agents/memory.py), [`README.md`](https://github.com/manthanguptaa/water/blob/454a86b79980877ed77d38ad1a150246a9bf1cf2/README.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: operators can impose strong policy and humans can have final say over individual actions, but generic configuration/approval is not the Methodology's S5 parent-governance case.

### Absence scope

- Surfaces inspected: approval/risk policy and timeout behavior; system prompts; memory layer precedence; guardrails; delegation/tool restrictions; runtime/configuration/deployment inventory.
- Plausible first-party paths checked: human approval, auto-approval thresholds, ORG memory precedence, static prompts/guardrails and administrator/developer configuration.
- Why no material first-party path remains: all inspected paths govern ordinary task execution or stored context. No first-party standard path elevates identity/ultimate-policy matters to a legitimate ultimate authority and returns that decision to govern the organization.

## Recursion, variety, escalation and evidence gaps

- Recursion: Water supports nesting through subagent tools and team-as-Task composition, but nesting alone is not credited as VSM recursion. The assessed team recursion is explicit only where multiple `AgentRole` operational tasks are treated as one Water team with shared current state/history.
- Variety: agentic action variety is provided by model-selected tools; team variety by multiple roles/subagents; runtime variety is bounded by iteration/round limits, schemas, delegation permissions, guardrails, approvals, sandboxing, retries/rate limits and flow structures.
- Escalation: approval gates can wait for human approve/deny or mark timeout escalation, and ReAct/task callbacks can reject actions. These are operational escalation/control mechanisms; they do not by themselves establish S5 or a parent-governed S3 mode.
- Evidence gaps: no material gap blocks the published vector. The principal judgment call is S3=C: the first-party dynamic-team primitive is specifically whole-team/current-state aware, but the repository does not ship a model-owned controller already wired to that decisive path. A future revision that packages such a controller could justify reassessment.

## Standalone vector

`A — C — — —`
