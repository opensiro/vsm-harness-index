---
harness_id: react-agent-harness
project_name: react-agent-harness
repository: https://github.com/ramannanda9/agent-harness
review_ref: 6b399e57daeef6475f2dc37c11a1e8fc097ca7e4
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# react-agent-harness

## Review boundary

- System in focus: The distributed, self-hosted BYO-LLM Python agent harness as one bounded goal-solving operational cell, with its registered ReAct specialists, optional subagent delegation, orchestrator, shared memory and runtime safety controls. The relevant recursion is one multi-agent execution/run and its retained memory context, not the upstream GitHub maintainer organization, an external provider or the user's entire enterprise.
- Purpose and identity: Carry out developer-configured tool-assisted goals, optionally decompose complex work among registered specialist agent runs, respond to failure and return a synthesized result.
- Relevant environment: Incoming goals, changing tool observations, failed/low-confidence subtasks, concurrent workers contending for agent instance state, supplied external LLM services and user approvals.
- Standard-distribution boundary: Library-native AgentRuntime with explicit agent/tool registries, a supplied model and MemoryManager, streaming or blocking dispatch, orchestration and optional PersistentAgent/subagent mode. Standard Python package and opt-in extras; a live model credential or its implementation is supplied by the adopter.
- Credited operating / distribution surfaces: [AgentRuntime dispatcher](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L373-L454), [classification and run wiring](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L707-L851), [ReAct worker](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L186-L291), [Orchestrator plans and executes](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L176-L317), [replanning and state updates](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L321-L514), [per-task worker copies](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L706-L784), [MemoryManager reconciliation](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/memory/manager.py#L267-L317), [run-end merge](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/memory/manager.py#L476-L544) and the supported optional [persistent plan gate](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/persistent.py#L798-L863).
- Adjacent first-party surfaces excluded from ownership: Library author's GitHub Actions/build and release jobs; examples and test-only mocks as production guarantees; unconfigured external LLM/model providers, Docker or MCP infrastructure; arbitrary customer-created institutional policy, external organization hierarchy, regulatory/audit service, and separately installed future strategic analysis tools. Tests can establish a structural failure and intended remedy but do not themselves operate a deployed organization.
- First-party operating / deployment modes considered: Standard streamed AgentRuntime classification into single-agent routed and multiagent orchestrated execution, parallel task runs including reused agent IDs, model-selected replan, per-goal guard budgets; optional SubAgentTool, durable checkpoint and session memory, human tool approval, and opt-in PersistentAgent plan-mode approval.
- Recursion level: One goal-executing multiagent work cell; distinct ReAct task actors with bounded technical outcomes and a run-level planner/replanner. Persisted memory can feed later tasks/runs but is not by itself an independent corporate organization.
- Reviewed revision: 6b399e57daeef6475f2dc37c11a1e8fc097ca7e4, immutable frozen [batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700) row 3 and intake #1699.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The caller registers AgentConfig and tools, creates a MemoryManager and supplies an LLM implementing completion; no model is shipped as an autonomous process. AgentRuntime dispatch_stream first classifies task complexity via an LLM: simple goals use model-selected routing to one BaseAgent ReAct loop; complex goals construct an Orchestrator using a planner LLM, registered agents, common budget and memory. Agents choose actions, call allowed tools, observe results and finish; parallel tasks are explicitly driven by fresh clones to avoid one agent template's per-run working memory being overwritten. [Runtime registration and setup](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L329-L451), [dispatch_stream](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L765-L851), [task cloning and isolation](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L257-L289), [parallel batch and result context](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L706-L797).

The orchestrator uses a validated DAG, dependency readiness, checkpoint and fan-in event transport; failed/low-confidence results trigger specified retry/skip/abort decisions or a new model-generated remaining-task DAG, subject to max replans and budget. The synthesizer LLM merges agent results, surfaces conflicting conclusions, and writes a run-end summary through the shared memory component. On default reconcile_on_write the MemoryReconciler LLM proposes semantic ADD/UPDATE/MERGE/DELETE/NOOP operations for persistent memory; delete is restricted by default, and per-agent working facts are namespaced. This contextual memory is later read by future runs. [Plan and replan prompts](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L84-L175), [DAG execution and control](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L321-L514), [LLM replan](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L632-L704), [reconciler](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/memory/manager.py#L160-L217), [run-end dispatch](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/memory/manager.py#L476-L544).

Additional first-party capabilities include optional persistent SQLite sessions, background tasks, checkpoints, tool/plan HITL, model switching, MCP tools, controlled subprocess/Docker bridge, and subagent tools. These are support surfaces, not automatic VSM higher functions. The frozen source was checked out clean (MIT; Git tree 67c0845c8477528bab9027778714d8671d429d1d). The shipped deterministic MockLLM quickstart completed successfully under PYTHONPATH=. No credential-backed real LLM run, Docker container execution or full upstream pytest suite is claimed. [Quickstart](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/examples/quickstart.py#L1-L180), [PersistentAgent](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/persistent.py#L621-L711), [plan approval](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/plan_mode.py#L88-L166), [executor bridge](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/executor_bridge.py#L1-L120).

## Operational model

Separate registered specialist agent runs produce task-specific outcomes through their own ReAct choices, bounded by tool permission and actual tool observations. Two independently ready tasks may use the same agent ID, which is a concrete source-documented race over task instruction and working-memory state. First-party cloning and run-scoped tool cloning prevent that interference; a run-end LLM memory reconciler additionally consolidates potentially conflicting semantic claims for later context, but is not evidence of a distinct, continuously empowered inter-worker arbitrator. A planner LLM can choose/revise run-wide commitments after new outcomes, while the deterministic DAG scheduler/budget guard enforce its plan. No independent complementary evidence-auditor, externally prospective strategic adaptation, or ultimate constitutional policy path is supplied by the frozen standard distribution.

## S1 — Operations

- State: A
- Function: Produce task-specific technical, research or tool-using outcomes through distinct model-backed ReAct specialists.
- Disturbance / variety regulated: Variable task intent, uncertain tool outputs, investigation and local implementation decisions under dynamically observed results.
- Decisive decision or feedback right: Select next thought, tool invocation, arguments and final answer in each agent's permitted domain.
- Decision owner: A supplied LLM acting through first-party BaseAgent and registered AgentConfig. Tool registry and human allow gates bound the choices but do not select the answer.
- Supporting / enforcement mechanisms: AgentConfig, allowlisted ToolRegistry, ReAct loop, working memory, streaming bus, per-run budget and error/resume state.
- Closure path: User goal → router or orchestrator chooses task → BaseAgent interprets observation and chooses action/tool → actual tool result returns to its reasoning loop → agent returns concrete task output for the parent run.
- Boundary reachability: The shipped AgentRuntime instantiates BaseAgent for registered configurations in both direct and orchestrated entry points; examples exercise a deterministic provider stub without adding outside orchestration code.
- Why this is / is not agent-owned: A model chooses substantive next actions conditional on tool output; the framework configures boundaries but does not deterministically decide task substance.
- Evidence: [Agent configuration](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L93-L155), [Agent ReAct phases](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L609-L754), [tool execution](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L846-L950), [runtime run paths](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L790-L979).
- Basis: Source-explicit model-driven ReAct, structurally reachable through public runtime.
- Confidence: High structurally; no production-model observations at this frozen ref.
- Caveats: The example MockLLM only validates wiring and should not be mistaken for model quality or externally authorized tool execution.

## S2 — Coordination

- State: C
- Function: Attenuate concrete interference when multiple S1 task runs use one shared registered agent template and would overwrite each other's local task and working-memory state.
- Disturbance / variety regulated: Two concurrent task drivers receiving identical/incorrect answers after the second overwrites the first task's mutable BaseAgent instance; nested stateful delegation can reproduce that corruption.
- Decisive decision or feedback right: Allocate an independent mutable runtime state to each ready task, including per-run steering, working memory, checkpoint scope and stateful nested subagent tool, while preserving a shared run-wide budget.
- Decision owner: Deterministic first-party Orchestrator and BaseAgent clone_for_run machinery; no autonomous agent negotiates the two task runs' shared-resource conflict.
- Supporting / enforcement mechanisms: Clone-per-task, separate stateful child tools, task-scoped checkpoints, isolated steering queues, common budget and fan-in result collection.
- Closure path: DAG produces simultaneous ready tasks referring to the same registered agent → executor clones per task before launch → independent instruction/memory/action execution → distinct valid outputs returned for the corresponding tasks; later planner branches on each separate result instead of overwritten shared state.
- Boundary reachability: Orchestrator._run_batch invokes clone_for_run for each Task in the normal shipped parallel code path. A first-party explicit regression test exercises genuine asyncio interleaving and asserts distinct returned answers and original registry preservation.
- Why this is / is not agent-owned: Specific inter-S1 destructive interference is remedied by a shipped deterministic constructor/enforcement path. A planner's LLM makes assignments, but does not make the isolation decision or handle competing resource claims. The optional LLM memory reconciler concerns later semantic persistence and must not be borrowed as agent-owned live coordination between these task actors.
- Distinct S1 units: Concurrent tA and tB operational task runs (even if they share one agent template ID); each has a distinct task, working state and outcome.
- Inter-S1 disturbance: Actual structurally demonstrated shared-instance overwrite causing both task actors to report the second task's answer while falsely succeeding.
- Attenuating coordination relation: Require a unique clone of BaseAgent and stateful tools for each task within the fan-in batch, isolate checkpoint and steering scopes.
- Feedback into subsequent S1 behaviour: Each task retains and executes its own instruction, returns a separate output, and downstream dependent tasks/planner use the correct per-task result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This directly prevents a demonstrated cross-worker mutable-state collision at the shared instance boundary, not merely ordering a DAG or carrying messages.
- Evidence: [Concurrent collision regression](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/tests/test_concurrent_same_agent.py#L1-L154), [nested tool and budget controls](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/tests/test_concurrent_same_agent.py#L160-L238), [clone_for_run](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L257-L289), [Orchestrator._run_batch](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L706-L796).
- Basis: Explicit concrete failure class plus first-party executable mitigation, with structural test coverage.
- Confidence: High for the narrow interference class; no evidence of general inter-worker negotiation/portfolio resource fairness.
- Caveats: C is not independent autonomous S2 decision rights; other cross-agent conflicts (external tools, shared database, contradictory facts) are not universally resolved by per-agent copies.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current whole-run multiagent commitments by choosing and revising which specialist tasks are to proceed, retry, skip or be replaced when observed results fail.
- Disturbance / variety regulated: Failed/low-confidence S1 results, current goal incompleteness, a DAG no longer suitable for the remaining workload and finite run budget.
- Decisive decision or feedback right: Choose new task assignments, instructions and dependency/remaining-work configuration in a fresh DAG following failures or low-confidence results.
- Decision owner: Model-backed run-level planner/replanner LLM in the shipped Orchestrator; fixed on_failure, max-replan count, validator and BudgetGuard only enforce constraints and trigger thresholds.
- Supporting / enforcement mechanisms: TaskResult/evaluation, validated DAG, shared budget, run-state/checkpoints, task statuses, streaming feedback and run-level model prompt.
- Closure path: Whole-run task/result overview → low-confidence/error and remaining DAG → model chooses revised tasks/agents → validated new DAG replaces current pending commitments and checkpoints → changed S1 agents/tasks actually execute next → synthesized whole-goal answer.
- Boundary reachability: AgentRuntime._build_orchestrator directly wires planner_llm and actual registered agents. _execute_plan_stream calls _replan on in-boundary task failures and replaces pending tasks with the returned validated plan.
- Why this is / is not agent-owned: Removing the planner LLM removes the discretionary reassignment/revision of remaining run-wide commitments; remaining deterministic scheduler and budget checks can enforce and retry/abort but cannot choose the new goal-specific DAG.
- Whole-system current view: Run goal, full selected specialist registry, existing completed and failed task results, and remaining unfinished tasks carried in the replan prompt.
- Current-control decision scope: Task commitment/agent assignment and revision of remaining present work, not merely initial decomposition; no evidence of organization-wide staffing/portfolio/budget policy beyond this one-run recursion.
- Evidence: [Runtime orchestrator wiring](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L707-L763), [Run-plan ownership](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L84-L112), [Failure/replan control and pending replacement](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L377-L505), [LLM plan and replan](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L632-L704).
- Basis: Explicit live feedback/reallocation path with autonomous model judgment.
- Confidence: Medium-high structural, restricted to current goal execution.
- Caveats: Only low-confidence/failure triggers drive replanning; decision is bounded by max-replan and registered agents, and real external-provider efficiency/correctness is unmeasured. Opt-in PersistentAgent plan-mode lets a human approve/revise an ordinary step plan, but primarily returns prompt priors, not a separate authoritative whole-system parent current-control loop at this assessed recursion; no S3 (P) modifier is claimed. [Plan-mode prior injection](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/persistent.py#L820-L857).

## S3* — Complementary audit

- State: —
- Function: Independent complementary access to operational truth beyond agents' normal self-reported outcomes, with audit findings returned to present control.
- Disturbance / variety regulated: Potential fabricated tool outcomes or an overconfident producer report that ordinary run traces/quality signals would fail to challenge.
- Decisive decision or feedback right: No distinct first-party independently empowered raw-evidence auditor established in this boundary.
- Decision owner: Not established; production specialists and orchestrator are ordinary operational actors, while an optional human plan approver reviews future plan proposal rather than actual independent evidence.
- Supporting / enforcement mechanisms: Trace/event capture, model response confidence, task validation, HITL tool approval and plan-mode prompts; these are not independent complementary audit owners.
- Closure path: No first-party independent evidence acquisition → autonomous auditor verdict → corrective S3 intervention loop shown.
- Why this is / is not agent-owned: The synthesized answer and conflict list are derived from producer TaskResult rather than independently inspecting task-primary artifacts; no separate read-only reviewer/remediation control is mandated.
- Evidence: [Synthesis prompt](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L114-L150), [synthesis after ordinary task results](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L494-L540), [approval gate](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/hitl.py#L214-L280), [trace and run events](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/runtime.py#L71-L145).
- Basis: Bounded absence after inspecting shipped orchestration, synthesis, audit-like tracing and HITL.
- Confidence: Medium-high for the first-party standard paths.
- Caveats: Developers can register a separate auditor as an ordinary specialist, but no shipped independent review contract plus corrective return exists automatically.

### Absence scope

- Surfaces inspected: AgentRuntime, Orchestrator synthesis/evaluation, traces, tool and plan HITL, SubAgentTool and examples, tests for approval/plan mode.
- Plausible first-party paths checked: Separate model synthesizer, low-confidence evaluation, user approval prompts and trace viewer; none provides separate raw-artifact access and independent corrective audit authority.
- Why no material first-party path remains: Every inspected claimed verifier is ordinary production-plan/answer processing or human permission gating; the first-party supported distribution lacks a specific auditable independent actor and returned findings/remediation contract.

## S4 — Outside-and-then intelligence

- State: —
- Function: Externally oriented prospective assessment and option generation to change future system capability, returned to current S3.
- Disturbance / variety regulated: Changes in future user demands, models, tools or environment that would require a prospective capability/organization redesign.
- Decisive decision or feedback right: No first-party prospective option right and adoption loop established. Model selection, memory consolidation and replanning change current task execution, not future operational capability.
- Decision owner: Not established in the shipped reviewed modes.
- Supporting / enforcement mechanisms: RoutingLLM and ModelSwitcher for configured choices, run-end memory reconciliation, failure replanning, session persistence, background task tools and extensibility hooks.
- Closure path: No shipped external/future model → capability-change option → commitment/adoption into present runtime or S3.
- Why this is / is not agent-owned: Config-driven model changes and retrospective context writing are not agent-judged external strategic adaptation with installed capability consequences.
- Evidence: [Routing](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/llm/routing.py#L1-L112), [manual model switching](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/model_switching.py#L24-L123), [Replan prompt only current work](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/orchestrator/planner.py#L113-L174), [reconciliation for future memory](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/memory/manager.py#L160-L217).
- Basis: Bounded negative from complete reviewed prospective-looking surfaces.
- Confidence: Medium-high within the shipped execution cell.
- Caveats: The adopter can write custom forecasting/adaptation agents, but the repository does not ship their specific function/authority loop.

### Absence scope

- Surfaces inspected: Planner/replanner, shared/persistent memory and reconciliation, dynamic LLM selection, agent/tool configuration, opt-in subagents, persistent session and examples.
- Plausible first-party paths checked: Future-facing memory consolidation, reassignment on failed current goals, model switching and user-supplied skill evolution.
- Why no material first-party path remains: The supplied operations only retain knowledge, select already configured resources or repair present work; no externally prospective options are formed and applied to first-party future capability.

## S5 — Policy and identity

- State: —
- Function: Legitimate purpose/identity and ultimate organizational-policy choice balancing current execution and prospective adaptation.
- Disturbance / variety regulated: Ultimate conflict over the goal cell's persistent mission, acceptable mission changes or constitutional boundary at the organizational recursion.
- Decisive decision or feedback right: No source-owned identity-level ultimate-policy decision owner or escalation/return mechanism.
- Decision owner: Not established. AgentConfig prompts and allowed tools are adopter inputs; HITL and approval gates cover task/plan/action permission, not authoritative identity revision.
- Supporting / enforcement mechanisms: Static role/system prompts, tool policy allow lists, explicit human tool/plan approvals, guardrail values, persistent session configuration.
- Closure path: No first-party path from identity-level question to legitimate ultimate authority and returned binding new mission policy.
- Why this is / is not agent-owned: A system prompt or safety constraint bounds tasks without constituting a live identity government. Ordinary operator approval is not an identity-level arbitration loop.
- Evidence: [AgentConfig](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/agents/base.py#L93-L185), [tool policy](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/tool_policy.py#L1-L115), [HITL](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/hitl.py#L126-L214), [plan-mode approval](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/harness/plan_mode.py#L88-L194).
- Basis: Bounded negative after examining all shipped policy-like/approval surfaces.
- Confidence: High for the declared execution-cell boundary.
- Caveats: An adopter may establish institutional parent S5 outside this library; absent a first-party identity/ultimate-policy return path it cannot be borrowed here.

### Absence scope

- Surfaces inspected: AgentConfig prompts and role instructions, ToolRegistry, policy/guard configuration, HITL and plan-mode, persistence/session config, upstream README and examples.
- Plausible first-party paths checked: User task veto, prompt updates, parent coordinator identity instructions and dynamic tool policy.
- Why no material first-party path remains: All supported levers decide individual run/action permissions or externally configure roles, not a continuous legitimate identity/ultimate-policy dispute/return procedure at this recursion.

## Recursion

- Parent boundary: User/adopter constructs and authorizes a goal-execution cell by selecting provider, agents, tools, budget, human approval and allowed interfaces. The external adopter organization and provider are not credited as internal VSM higher functions.
- Internal S1 recursion: Specialist ReAct agent can itself delegate to SubAgentTool; nested task runs may exhibit local ReAct/streaming/working-memory regulation but do not automatically establish an independent complete S1–S5 organization at every depth. [SubAgentTool](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/tools/builtin/subagent.py#L40-L99), [nested delegation stream](https://github.com/ramannanda9/agent-harness/blob/6b399e57daeef6475f2dc37c11a1e8fc097ca7e4/tools/builtin/subagent.py#L143-L244).
- Horizontal units: Model-backed specialist tasks/agent runs. Planner controls remaining run commitments; clone-per-task attenuates concrete shared instance conflicts.

## Variety and escalation

- Task-specific variety: Agent selects tools and responds to observations (S1); hard allowed-tool gates/budgets constrain excess variety.
- Inter-task instability: Per-task clones prevent concurrent reuse of mutable instance state, including nested stateful tools (S2=C).
- Current operational exceptions: Failure or low confidence invokes retry/skip/abort or model-selected new remaining-work DAG (S3=A); deterministic thresholds are triggers/enforcement rather than choice owner.
- Human route: Optional plan/tool approval blocks or advises a particular turn; no separate independent S3* auditor or parent S5 is inferred.
- Escalation beyond boundary: Adopter/provider must supply credentials, external policy, actual real-world authority and any future adaptation/audit organization.

## Evidence gaps

- Frozen checkout and MIT permission inspected; no independent live provider-backed multiagent execution was attempted. Deterministic MockLLM quickstart successfully exercised the first-party standard wiring, not a quality benchmark.
- Source regression tests document and exercise clone-per-task concurrency isolation, but a full pytest run was not available in the initial isolated checkout without installing test dependencies. Do not assert all upstream tests passed merely because source contains them.
- Reconcile-on-write is default and calls an LLM on combined agent results, but no concrete independently proven real multi-agent semantic contradiction/adjudication trace was run here; do not promote this to S2=A solely because a model summarizes memory.
- Optional PersistentAgent human plan approval is real, but its injected approved prior is guidance to one coordinator, not shown as an enforceable whole-of-organization parent control loop; no A(P), C(P) or S5 parent claim.
- No external-model task success or actual authorization/policy outcome is inferred from static code/tests.
