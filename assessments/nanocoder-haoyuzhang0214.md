---
harness_id: nanocoder-haoyuzhang0214
project_name: NanoCoder (HaoyuZhang0214)
repository: https://github.com/HaoyuZhang0214/NanoCoder
review_ref: 1ac25d166295ae9339fa4f96586d01a94b4f559e
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# NanoCoder (HaoyuZhang0214)

## Review boundary

- System in focus: MIT-licensed first-party terminal coding agent packaged in `nanocoder/` at frozen `1ac25d166295ae9339fa4f96586d01a94b4f559e`; not any similarly named NanoCoder or unshipped upstream prototype.
- Purpose and identity: operator-requested repository investigation and editing via model-selected local tools, optional subordinate task agents, session save/resume, and optional LangGraph execution.
- Standard-distribution boundary: `nanocoder/cli.py` instantiates `Agent` with `ALL_TOOLS`, local consent/hooks and configured LLM; alternative `--use-langgraph` selects `LangGraphAgent`. Provider inference, arbitrary connected MCP servers, user-provided hooks, the shell operating system and maintainer CI are environment, not function owners.
- Environment: user task/plan approval, mutable source tree, model messages/tool responses, command permissions, bounded context/turns and optional external MCP tools.
- First-party modes considered: default `Agent.chat` interactive and one-shot sessions; bundled `AgentTool` creates child coding loops; optional LangGraph checkpoint/graph execution; read-only plan mode, human consent and the `--yes` choice treated as execution constraints, not parent organization.
- Recursion: parent S1 coding loop can synchronously call a subordinate independent S1 coding loop with distinct messages. This does not by itself instantiate a parent S2/S3 organization. Child tool list excludes `agent`.
- Profile 0.2.4 / Methodology 0.3.7.
- Credited operating / distribution surfaces: `nanocoder/agent.py`, `nanocoder/tools/`, `nanocoder/cli.py`, `nanocoder/permissions.py`, `nanocoder/langgraph_agent.py`, first-party session/context.
- Adjacent first-party surfaces excluded from ownership: external model and MCP servers, operator decisions, user-configured shell hooks and repo development tests.

## Repository architecture

The shipped `Agent.chat` is a bounded LLM → model tool-call → tool-result → next LLM feedback loop. A separate `AgentTool` can run a new `Agent` with its own history for an assigned task and report a capped text response. The child shares the parent's tool instances except `agent`, including a session-scoped todo checklist, and inherits human consent/hooks. Multiple model-requested tool calls can be executed concurrently by a thread pool. These are useful execution/composition mechanisms, but not evidence of task-conflict attenuation across multiple autonomous S1 units. LangGraph uses state graph/checkpointing for the same task tool cycle rather than a distinct coordination authority.

## Operational model

The operator supplies a coding objective and consent policy; the model selects file, search, shell, edit, checklist or subordinate agent tools and uses returned text to choose the next step. A child performs a bounded independent coding/research loop and returns its response to the parent; no persistent worker roster, worker-status inspection, independent task ownership arbitration, or team-wide corrective control path was found among the packaged tool definitions. The entire model-tool loop is first-party despite inference being provided by a configurable external model API.

## S1 — Operations

- State: A
- Function: Perform a coding task by selecting tools, inspecting results and adapting subsequent steps within bounded model/tool rounds.
- Disturbance / variety regulated: Changing user requirements, repository state, tool errors, permission refusals, and context limits.
- Decisive decision or feedback right: Model-driven Agent.chat chooses the next local action from feedback; no mandatory human action selection for each permitted tool call.
- Decision owner: The shipped Agent/model-tool loop; a configured provider supplies inference, not agent ownership.
- Supporting / enforcement mechanisms: First-party tool registry, command/file adapters, context compression, local session/history, permission checks and iteration bound.
- Closure path: cli.main → Agent.chat → model tool calls → _permit/_exec_tool or concurrent dispatch → tool reply appended to messages → new model step / final response.
- Why this is / is not agent-owned: This is an operational feedback closure under packaged agent control, rather than a static prompt or an external provider being counted as the harness.
- Boundary reachability: CLI creates Agent and supplies ALL_TOOLS, with optional LangGraph graph preserving iterative tool feedback.
- Evidence: [nanocoder/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/agent.py); [nanocoder/cli.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/cli.py); [nanocoder/tools/__init__.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/__init__.py); [nanocoder/llm.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/llm.py); [nanocoder/langgraph_agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/langgraph_agent.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: high.
- Caveats: This assessment does not grade execution performance or external dependencies.

## S2 — Coordination

- State: —
- Function: Regulate interfering actions of distinct S1 operations so their mutual disturbances are attenuated.
- Disturbance / variety regulated: Two independently delegated subagents or parallel tool calls can affect a common worktree/checklist and conflict over the same task or files.
- Decisive decision or feedback right: No shipped independent claim/lock/task-owner regulation with distinct inter-S1 disturbances and corrective feedback was found.
- Decision owner: Operator or parent model sequences/delegates; shared checklist mutation is not a separately established coordinating owner.
- Supporting / enforcement mechanisms: AgentTool delegated calls, shared TodoWriteTool and ThreadPoolExecutor; permission gates apply locally and uniformly.
- Closure path: Parent may invoke child and read its final text, and the common todo may be overwritten; no first-party policy resolves competing child task claims or routes inter-worker conflicts to both affected S1 units.
- Why this is / is not agent-owned: Delegation, batch execution, shared state and returning a child report are not in themselves S2-specific interference attenuation.
- Boundary reachability: AgentTool is in the default tool list; no task lock or queue/worker ownership transaction is provided by these registered tools.
- Evidence: [nanocoder/tools/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/agent.py); [nanocoder/tools/todo.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/todo.py); [nanocoder/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/agent.py); [nanocoder/tools/__init__.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/__init__.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: medium-high.
- Caveats: This assessment does not grade execution performance or external dependencies.

### Absence scope

- Surfaces inspected: Parent/child tool loop, simultaneous tool-call executor, shared checklist, child task execution, bundled tool registry.
- Plausible first-party paths checked: Distinct model-driven child S1, mutual task/file interference, todo checklist as shared task owner, batch results as inter-worker feedback, human tool approvals.
- Why no material first-party path remains: A child or parallel tool call can update shared state but no first-party competing-task ownership decision, conflict attenuation, or repair-feedback channel between distinct S1 agents appears in the shipped mechanisms.

## S3 — Inside-and-now control

- State: —
- Function: Maintain a current whole-system picture and intervene in operational capacity and priorities across distinct S1 units.
- Disturbance / variety regulated: Multiple delegated activities may be competing for current resources, priority or work ownership.
- Decisive decision or feedback right: No shipped team-wide current state/roster and associated model-selected reallocating, stopping, reprioritizing or reassigning of live independent workers was found.
- Decision owner: Main Agent chooses its own next tool call and child request; no separate live team-controller role is established.
- Supporting / enforcement mechanisms: todo_write current checklist and subagent creation with bounded synchronous result; optional LangGraph state is a single agent's workflow.
- Closure path: Parent assigns a subtask and receives a final report; it does not observe the whole current population of active worker S1 units or use dedicated intervention tools to revise their assignments while running.
- Why this is / is not agent-owned: The parent model's local planning/delegation is ordinary S1 self-regulation and not a proven whole-current S3 management loop.
- Boundary reachability: Default CLI reaches AgentTool but has no model-callable team roster or worker intervention tool; LangGraph is an optional execution backend.
- Evidence: [nanocoder/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/agent.py); [nanocoder/tools/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/agent.py); [nanocoder/tools/todo.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/todo.py); [nanocoder/langgraph_agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/langgraph_agent.py); [nanocoder/cli.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/cli.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: medium-high.
- Caveats: This assessment does not grade execution performance or external dependencies.

### Absence scope

- Surfaces inspected: AgentTool parent/child flow, checklist reinjection, CLI modes, LangGraph checkpoints.
- Plausible first-party paths checked: Delegation as parent control, model-managed checklist as current whole-system view, graph orchestration as S3, approval as current-control authority.
- Why no material first-party path remains: No persistent global child roster, current whole-of-work operational view, or model-reachable live intervention into independently operating workers is evidenced; parent task execution remains local S1.

## S3* — Complementary audit

- State: —
- Function: Provide a complementary inspection of actual operational reality distinct from S3's reports, with corrective return to S3.
- Disturbance / variety regulated: Subagent work reports might be incomplete, wrong or inconsistent with actual files and task progress.
- Decisive decision or feedback right: No independently owned S3* reality inspection or binding corrective return to a whole-current S3 controller is shown.
- Decision owner: Parent can see child text and tool outputs; external operator/test/CI may assess results but are outside this boundary.
- Supporting / enforcement mechanisms: Tool results, session logs/checkpoints, pre/post hooks and normal LLM self-checking.
- Closure path: The child reports truncated text to parent; no separate audit owner inspects operational ground truth and returns corrective findings to an S3 control function.
- Why this is / is not agent-owned: Observation and checkpoint records do not constitute an independent audit path; no S3 audit closure exists to be corrected.
- Boundary reachability: First-party hooks are user-authored commands, not a packaged independent auditor.
- Evidence: [nanocoder/tools/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/tools/agent.py); [nanocoder/hooks.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/hooks.py); [nanocoder/session.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/session.py); [nanocoder/langgraph_agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/langgraph_agent.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: medium-high.
- Caveats: This assessment does not grade execution performance or external dependencies.

### Absence scope

- Surfaces inspected: AgentTool final report, hooks, context/session persistence, checkpoint machinery.
- Plausible first-party paths checked: Child summary checking, error catching, pre/post hook inspection, persistent trace as audit, operator/CI review.
- Why no material first-party path remains: These paths do not provide a distinct first-party ground-truth audit with corrective return to an established S3 controller.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense future/external changes and transform prospective strategic adaptation into current organizational capability.
- Disturbance / variety regulated: Changes in environment, coding technology, tools and future organizational requirements.
- Decisive decision or feedback right: No bundled future-focused intelligence/adaptation owner or choice→implementation return path is demonstrated.
- Decision owner: Developer/user selects providers, MCP servers, hooks, configuration and task strategy outside a first-party prospective organization.
- Supporting / enforcement mechanisms: Dynamic model reasoning, contexts, optional externally added MCP tools, saved session, graph checkpoint and prompts.
- Closure path: Model actions solve current coding tasks; user-installed MCP services or future maintainer changes do not create a prospective external sensing/adaptation loop inside the assessed harness.
- Why this is / is not agent-owned: Iteration and restoring checkpoints are retrospective/operational; no S4 owner, strategy review, or prospective policy of adaptation is instantiated.
- Boundary reachability: CLI permits external extension but does not establish a first-party future-governing loop.
- Evidence: [nanocoder/cli.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/cli.py); [nanocoder/mcp.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/mcp.py); [nanocoder/context.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/context.py); [nanocoder/langgraph_agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/langgraph_agent.py); [nanocoder/config.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/config.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: medium-high.
- Caveats: This assessment does not grade execution performance or external dependencies.

### Absence scope

- Surfaces inspected: Agent prompt/context, model/tool loop, plugin/MCP configuration, session and graph checkpoint persistence.
- Plausible first-party paths checked: Model research and tool discovery as prospective sensing, externally configured MCP change as adaptation, checkpoint resume as future planning.
- Why no material first-party path remains: No shipped owner for scanning external future, deciding system adaptation and feeding changes into the operating organization; current-task reasoning and externally configured extensibility do not close that path.

## S5 — Policy and identity

- State: —
- Function: Resolve organizational purpose, ultimate identity and legitimacy conflicts and return binding policy decisions.
- Disturbance / variety regulated: Conflicting user goals, permissions, credentials and external operating restrictions.
- Decisive decision or feedback right: No shipped organizational mission/identity authority or binding escalation/return path is established.
- Decision owner: Operator sets task and approvals; code enforces local consent/plan mode under externally chosen scope.
- Supporting / enforcement mechanisms: Permission per tool, persisted allow-list, noninteractive refusal, plan mode, user-provided config and hooks.
- Closure path: Human grants/denials become local tool results; no distinct organization-level S5 decision about mission, identity, or policy legitimacy is formed and implemented.
- Why this is / is not agent-owned: Permissions and read-only mode regulate execution but are not automatically the function that owns ultimate policy and identity.
- Boundary reachability: Default CLI configures permissions; `--yes` and user approvals are not autonomous S5.
- Evidence: [nanocoder/permissions.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/permissions.py); [nanocoder/agent.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/agent.py); [nanocoder/cli.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/cli.py); [nanocoder/hooks.py](https://github.com/HaoyuZhang0214/NanoCoder/blob/1ac25d166295ae9339fa4f96586d01a94b4f559e/nanocoder/hooks.py).
- Basis: static shipped-source reconstruction at fixed SHA; no live model evaluation.
- Confidence: high.
- Caveats: This assessment does not grade execution performance or external dependencies.

### Absence scope

- Surfaces inspected: Consent, plan mode, CLI configuration, user hooks and task input.
- Plausible first-party paths checked: Tool approvals as S5, user-provided rules as constructed governance, prompt constraints, parent operator policy.
- Why no material first-party path remains: All reachable first-party decisions concern tool authorization under operator-supplied purpose, without an ultimate organization identity/legitimacy decision and policy return.

## Distributed OSS parent arrangement

The upstream MIT project has maintainers and users but these external roles do not constitute an evidenced live parent VSM organization governing a running NanoCoder instance. An operator's permission response controls a local tool, not a proven S3/S4/S5 parent mode.

## Self-hosted and non-human modes

Configured self-hosted or external model inference still leaves the first-party `Agent.chat` in control of tool choice and returned evidence. No A(P), C(P), or separate parent-closed function is inferred from operator-set permissions, hooks or external MCP processes.

## Recursion

A child `Agent` has independent message history and bounded model-tool work, but its tool registry deliberately omits `agent` to prevent further recursion. The parent receives a capped completion text, with no independently established S2/S3 regulation of multiple children.

## Variety and escalation

Permission refusal, tool failure, model errors and bounded stop messages flow into the executing S1 loop. Operator approval and plan exit are explicit external choices; none makes the harness S5 by label.

## Evidence gaps

Static code review only; no provider credentials or benchmark runs used. Parallel model tool calls and shareable mutable todo/checklist raise potential cross-operation contention; absence conclusions are scoped to first-party implemented function ownership at the frozen revision. Optional user-configured MCP processes and hooks can add behaviour but are not assessed as native ownership.

## Assessment summary

**Proposed included**, source-first vector `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`. This is distinct from CodeAgent's verified team-wide control/conditional-task ownership at its separate pinned revision. Proposal status is not canonical admission; Skills validation, Index checks, CI, and separate canonical admission remain required.
