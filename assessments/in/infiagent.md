---
harness_id: infiagent
project_name: infiAgent
repository: https://github.com/polyuiislab/infiAgent
review_ref: cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: ?
autonomy_s5: —
---

# infiAgent

## Review boundary

- System in focus: One first-party installable infiAgent Python backend runtime and its configured task/agent hierarchy, operating across independently identified user tasks. Its operational unit is a model-driven agent with subordinate model-backed agent-tool calls, file/shell/browser/research skills, persisted task conversation and shared hierarchy state, resumable tool state, and optionally global experience reuse.
- Purpose and identity: Run potentially long-horizon user-directed tasks through configured tool-equipped LLM actors, recover from interrupted steps and pass context/results to delegated child agents and future task sessions.
- Relevant environment: User instructions, task workspaces, file/network/scientific tools, errors/results, external LLM deployments, installed skills/MCP servers, separate human tool confirmation and persisted prior experiences.
- Standard-distribution boundary: Shipped Python SDK `infiagent(...).run(...)` and CLI `start.py`; actual first-party `core.AgentExecutor`, `ToolExecutor`, `ContextBuilder`, `HierarchyManager`, `ThinkingAgent` and `utils` task/experience storage plus builtin tool server. LLM providers, optional MCP tools, external models and skills content authored elsewhere are execution dependencies. Local/direct-tools versus configured MCP service and thinking versus react/react-lite are supported operating modes.
- Credited operating / distribution surfaces: [RUNTIME.md](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/RUNTIME.md); [infiagent/sdk.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/infiagent/sdk.py); [start.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/start.py); [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py); [core/hierarchy_manager.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/hierarchy_manager.py); [core/context_builder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/context_builder.py); [services/thinking_agent.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/services/thinking_agent.py); [services/llm_client.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/services/llm_client.py); [tool_server_lite/tools/task_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/task_tools.py); [tool_server_lite/tools/experience_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/experience_tools.py); [utils/experience_store.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/experience_store.py); [utils/task_runtime.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/task_runtime.py); [utils/conversation_storage.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/conversation_storage.py); [config/builtin_level_0_tools.yaml](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/config/builtin_level_0_tools.yaml).
- Adjacent first-party surfaces excluded from ownership: Test harnesses/assertions, README research graphs/screenshots, release/package metadata, reference skills/templates under `skills/` unless actually installed and credited as tasks, project-maintainer workflow; external provider-side model routing and third-party MCP execution semantics are not native VSM owners.
- First-party operating / deployment modes considered: SDK synchronous run; CLI runtime with direct tool dispatch; configured MCP tools; `thinking` periodic-summary or `react`/`react_lite` model loops; nested synchronous configured `llm_call_agent` child roles; explicitly launched background tasks and cross-task messages; human-confirmed dangerous tool mode; restart/resume and task/global experiences.
- Recursion level: Single installed infiAgent task/harness organization. Nested agents act as S1 task-operation workers; inter-task communication and state stores are considered for wider closure but are not assumed to constitute a governed federation of organizations.
- Reviewed revision: `cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19`, immutably pinned by Index discovery #202, batch #1669 row 1; detached checked Git commit.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The supported SDK and CLI instantiate a configured `AgentExecutor` using a YAML-defined `llm_call_agent` identity. The real `AgentExecutor.run` loop loads/resumes an agent frame, optionally invokes a separate `ThinkingAgent` for **current-task progress summaries**, builds an evidence-rich prompt from `ContextBuilder`, sends it to configured `SimpleLLMClient`, dispatches model-selected `ToolExecutor` calls, appends actual tool results as agent action history and re-enters model decisions until `final_output`, error or a turn bound. It persists action and task metadata across interruption; no external hosted agent runtime supplies the loop logic. [infiagent/sdk.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/infiagent/sdk.py); [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [core/context_builder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/context_builder.py).

A configured tool with `type: llm_call_agent` is invoked through `ToolExecutor._execute_sub_agent` by constructing another **first-party** `AgentExecutor` and running it within the shared task hierarchy. `HierarchyManager.push_agent/pop_agent` stores parent/child and stack state; child results are returned to the invoking parent as tool observations. `tool_server_lite.tools.task_tools` also permits explicit background task launch and targeted message append with optional resume. These provide task decomposition and communication, not by themselves a demonstration of coordination under inter-S1 conflict or whole-current governance over tasks. [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py); [core/hierarchy_manager.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/hierarchy_manager.py); [tool_server_lite/tools/task_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/task_tools.py).

Persistence is substantive: the task hierarchy uses cross-process locks/atomic saves; `AgentExecutor` writes turn/tool history and recovers unfinished tool calls with idempotence safeguards, while `SimpleLLMClient` implements deployment retry/failover. Both are reliability/current task mechanisms, not organizational policy owners. Dangerous builtin tools may ask a human for confirmation, but this is local tool authorization, not mission governance. [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [core/hierarchy_manager.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/hierarchy_manager.py); [services/llm_client.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/services/llm_client.py); [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py).

A separate `write_experience` tool can append/replace/delete `task` or `global` experience markdown with concurrency-safe file revisions, while `ContextBuilder._build_experience_blocks` injects only `status=active` records into a future task prompt for the same agent/system. This is a **real installed optional write → persist → reread path**; there is no in-source proof of systematic environmental scanning, prospectively evaluated capability options or a distinct evaluation/admission controller choosing experience changes for future operational competence. Therefore retain an explicit *S4 unresolved* judgment, rather than counting every persisted note as S4 or denying that a potential in-boundary adaptive path exists. [config/builtin_level_0_tools.yaml](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/config/builtin_level_0_tools.yaml); [tool_server_lite/tools/experience_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/experience_tools.py); [utils/experience_store.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/experience_store.py); [core/context_builder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/context_builder.py).

## Operational model

Supported S1 outcomes are per-agent task responses, file/tool effects and `final_output` statuses. A subordinate configured LLM agent owns its own selected task tool calls inside a parent's delegation but shares one task stack and feedback; an explicitly background-launched task may have its own life cycle without a first-party global task-allocation regulator. Decisions on what to do next within a task are model-owned; context windows, retry, approvals and storage are deterministic enablers. Neither the `ThinkingAgent` name nor a message bus alone establishes a function-specific metasystem.

## S1 — Operations

- State: A
- Function: Perform user-requested long-horizon work through one or more model-directed operating agents that choose and execute real tools and change course from tool observations.
- Disturbance / variety regulated: Ambiguous and evolving user requests, varied files/data and tool interfaces, tool errors, missing context and subordinate-task outputs.
- Decisive decision or feedback right: A configured execution-model agent selects specific next tool, arguments and final answer conditional on current prompt and previously executed tool return. Optional model-directed subagent delegation supplies independent child model/tool steps.
- Decision owner: Configured model actor running inside first-party `AgentExecutor` and recursively inside a first-party child `AgentExecutor` when the tool's configured type is `llm_call_agent`; not the external LLM provider's service organization.
- Supporting / enforcement mechanisms: ToolExecutor direct/MCP dispatch, ContextBuilder task/skill/global context, child agent stack, turn/tool counters, prior results, human dangerous-tool approval, durable action storage.
- Closure path: Task prompt → model selects tool or configured child model agent → tool executed and result/error stored → next model turn receives observations and revises task work → `final_output` / persisted task result. Child return is an actual tool result fed into parent model.
- Boundary reachability: SDK `InfiAgent.run` and CLI `start.py` create `AgentExecutor.run`; its bounded model/tool loop calls `_execute_tool_call` → first-party `ToolExecutor.execute` → builtin or configured `llm_call_agent` nested executor, with feedback returned into current action context. These are installed operating paths, not test-only demos.
- Why this is / is not agent-owned: A model decides substantive task actions and evidence-dependent next steps; deterministic storage, failover and tool confirmation constrain but don't replace that decision.
- Evidence: [infiagent/sdk.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/infiagent/sdk.py); [start.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/start.py); [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py); [core/context_builder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/context_builder.py).
- Basis: Explicit first-party model/tool/action-feedback source.
- Confidence: High for reachable mode, not an actual executed remote-provider result.
- Caveats: Provider keys and selected tools/skills are required for live activity; no claim about empirical task success.


## S2 — Coordination

- State: —
- Function: No implemented function-specific feedback proven to attenuate **interference between distinct independently operating S1 work units**, rather than merely maintain shared task state or serialize writes.
- Disturbance / variety regulated: Sibling or background agents could contend for shared task context, tool capacity or storage; the reviewed controls address atomicity/idempotence and scheduling of nested calls, not observed operational conflict among independent units.
- Decisive decision or feedback right: Hierarchy stack and file locks serialize writes and track parent/child; a parent receives child output and continues its same task. No inter-S1 conflict-sensitive arbitration and returned mutual adjustment was demonstrated.
- Decision owner: Deterministic hierarchy/storage lock, caller-owned task delegation and task runtime state; none owns a separately demonstrated S2-specific variety-regulating judgment.
- Supporting / enforcement mechanisms: Cross-process read-modify-write locks for task and experience files, hierarchical parent/child IDs, nested-agent execution and background task messaging.
- Closure path: Same-task updates are serialized or nested children finish → one parent continues; the missing element is an identified clash between two S1 goals/actions → attenuation decision → changed subsequent distinct S1 behaviour.
- Why this is / is not agent-owned: Stack topology, task messages and generic file locks are not evidence of a Beer-style S2 function, autonomous or constructor.
- Evidence: [core/hierarchy_manager.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/hierarchy_manager.py); [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py); [utils/experience_store.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/experience_store.py); [tool_server_lite/tools/task_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/task_tools.py).
- Basis: Bounded negative inspection of strongest inter-agent candidates.
- Confidence: Medium-high, with substantive file correctness acknowledged.
- Caveats: A configured agent workflow or external deployment may implement specific S2 that is not part of the pinned first-party default distribution.

### Absence scope

- Surfaces inspected: Parent/child runtime frames, background task/message transport, concurrent task state and experience store locking, model/tool history and provider failover.
- Plausible first-party paths checked: Inter-agent stack push/pop, same-task state arbitration, background message and resume, cross-process file lock/optimistic conflict handling and multi-provider cooldown.
- Why no material first-party path remains: Every identified mechanism either executes a single task's delegation, preserves file consistency or handles one provider failure; none establishes conflict-specific inter-S1 attenuation with returned changed activity of distinct operating cells.


## S3 — Inside-and-now control

- State: —
- Function: No first-party separate inside-and-now control decision for the current resource and operational commitments of a multi-unit system at the declared recursion.
- Disturbance / variety regulated: Outstanding tool calls, interrupted runs, many agent steps, current task failures and context overload are real, but regulated locally as task execution/recovery.
- Decisive decision or feedback right: Top-level model decides its own current task action; `ThinkingAgent` plans next few actions of this same model and keeps context manageable. `HierarchyManager` records running actors but doesn't choose portfolio-level priorities/resource reassignment. Human config and tool approval don't close a live all-current decision.
- Decision owner: Per-task agent and deterministic state/step limits, not an identified separate S3 controller or legitimate parent resolving cross-task current commitments.
- Supporting / enforcement mechanisms: Agent task stack/status and shared context, periodic thinking, max_turns/action_window, runtime launch/resume, model-provider fallback and tool confirmation.
- Closure path: A task error/restart restores the same task or a model changes its current tool; no whole-installation view → decision on multiple S1 commitments/constraints → returned operative intervention is implemented.
- Why this is / is not agent-owned: Planning and controlling the task's own action window remains S1, while recovery and saved task state are enabling mechanisms and not S3 current management.
- Evidence: [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [services/thinking_agent.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/services/thinking_agent.py); [core/hierarchy_manager.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/hierarchy_manager.py); [utils/task_runtime.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/task_runtime.py); [infiagent/sdk.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/infiagent/sdk.py).
- Basis: Bounded negative of installed task-level and parent alternatives.
- Confidence: Medium.
- Caveats: SDK clients can externally orchestrate several tasks; no source-backed shipped S3-specific manager path was found for a positive constructor or supported parent modifier.

### Absence scope

- Surfaces inspected: Task CLI and SDK, multi-task launch/add_message/resume, hierarchy state, ThinkingAgent progress summary, real-time tool approval and model/provider recovery.
- Plausible first-party paths checked: Nested agent lifecycle, task lists, task event stream and state, planning to-do summaries, persistent past tasks, cross-task add_message and operator current controls.
- Why no material first-party path remains: The source-backed actor chooses work only within a task, and generic task listing/launching cannot establish whole-current multi-operation managerial rights or legitimate parent decision return at this recursion.


## S3* — Complementary audit

- State: —
- Function: No separate complementary evidence-access evaluator that independently challenges current agent outcome claims and returns findings into a corrective operating decision.
- Disturbance / variety regulated: An agent could report unsupported results or misread tool evidence, but only same-task reflection/recording and human tool approvals are installed in the reviewed core.
- Decisive decision or feedback right: The `ThinkingAgent` summarizes ongoing task progress/todo, context and next steps for the operating agent, not a fresh independent check of factual output using separate protected original evidence. It has no demonstrated reject-and-return authority over a reported claim.
- Decision owner: Same task agent and planning/context service; human confirmation controls dangerous tool execution, not an evidence-verification reviewer.
- Supporting / enforcement mechanisms: Event history, raw-trace recorder, task history, initial and periodic thinking, tool errors, command permission confirmations.
- Closure path: Thinking refresh → altered current context, or user confirmation → allow/deny tool; absent original claim → independent complementary evidence → findings/corrections → new output or withheld certification.
- Why this is / is not agent-owned: A second model for progress compression doesn't make an S3* critic. There is no independent source-evidence judge/right in that code path.
- Evidence: [services/thinking_agent.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/services/thinking_agent.py); [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py); [utils/raw_trace_recorder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/raw_trace_recorder.py); [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py).
- Basis: Bounded negative across task audit, thinking, tool approval and trace surfaces.
- Confidence: Medium-high.
- Caveats: An operator could manually review work or install external critic via MCP/skills, but those separate components are not first-party attached complementary closure here.

### Absence scope

- Surfaces inspected: ThinkingAgent instructions/runtime activation, CLI/display trace, tool/permission approval, context history, error/final_output, SDK result status.
- Plausible first-party paths checked: Reflection vs independent factual review, raw evidence comparisons, separate reviewer agent, tool-result validation, report gating and correction loops.
- Why no material first-party path remains: Only next-step reflection and execution checks appear as operating paths; no distinct audit owner's independently sourced claim challenge and corrective return is present in shipped runtime.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Investigate whether the installed task/global `write_experience` store constitutes actual future-oriented agent organizational capability adaptation, rather than replay of notes or same-task memory.
- Disturbance / variety regulated: New tool/task environment lessons may be useful in later different tasks; recorded active experience can change subsequent model inputs, but the improvement/selection relation is not established by this source trace.
- Decisive decision or feedback right: Agent or human can invoke `write_experience` to add/replace global notes, and next task ContextBuilder reads active notes, but a responsible prospective option-selection/admission right grounded in environmental feedback is not demonstrably distinct from arbitrary note entry.
- Decision owner: Agent writing model-selected tool arguments or human operating the tool, and deterministic revision-safe store/injector. Whether any of these owns a legitimate autonomous or constructor-owned S4 decision is unresolved.
- Supporting / enforcement mechanisms: WriteExperienceTool exposed in built-in tool catalog, task/global experience path selection, revision/active status and atomic multi-scope mutations, ContextBuilder active-note injection on later task runs.
- Closure path: Possible source task observation → model-initiated experience append/replace → persisted global active entry → next model's task prompt includes it. The observed return is concrete; missing is evidence that the decision is an externally and prospectively grounded *organizational capability option* deliberately selected instead of generic remembered content.
- External distinction: Task/tool outcomes originate from a mutable external work environment, but no implemented future-environment sensing/evaluation procedure is identified.
- Future / prospective distinction: Global per-agent experiences survive one task and are read on later tasks; persistence horizon alone doesn't show prospective capability-level choice.
- Adaptation option generated: Unstructured experience note that may influence later agent action/prompt. No in-source validated improvement proposal, impact metric, candidate comparison, capability revision or acceptance criterion.
- Path back into current capability / S3: First-party ContextBuilder injects status-active global experience into subsequent operating model context. This is a real S1-facing feedback path, but a corresponding S4 right/selection remains an unresolved function-specific evidence question.
- Why this is / is not agent-owned: A model may choose note content; model discretion is real, but assigning S4=A from model-authored memory would conflate routine context persistence with systematic future intelligence. Evidence is insufficient for positive S4, while the shipped cross-task path prevents a confident no-material-path negative.
- Evidence: [config/builtin_level_0_tools.yaml](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/config/builtin_level_0_tools.yaml); [tool_server_lite/tools/experience_tools.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/tool_server_lite/tools/experience_tools.py); [utils/experience_store.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/experience_store.py); [core/context_builder.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/context_builder.py); [core/agent_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/agent_executor.py).
- Basis: Structural, unresolved semantic ownership/closure test after inspecting positive and negative alternatives.
- Confidence: Medium for exact store→future prompt wiring; low for any wider S4 claim.
- Caveats: The `?` records a concrete plausible in-boundary future-capability path, not a claim of achieved adaptation or an obligation to introduce a runtime.


## S5 — Policy and identity

- State: —
- Function: No installed ultimate policy/identity owner is shown deciding the legitimate purpose and values of the deployment and returning changed institutional policy to operation.
- Disturbance / variety regulated: Unsafe tool actions, model credentials, task constraints, file access, and work approval are handled by configuration and permissions under operator-defined purpose.
- Decisive decision or feedback right: Human may approve a dangerous command and user supplies goals/configured agent identity; code routes, checks and persists constraints rather than adjudicating ultimate mission-value conflicts.
- Decision owner: External human deployer for task purpose/permissions and deterministic runtime for enforcing inherited local rules; no first-party legitimate S5 actor/authority loop.
- Supporting / enforcement mechanisms: Tool confirmation, sandbox policy, model permissions and keys, configured agent identity and state persistence.
- Closure path: Already chosen permission profile → tool approval/block; no independent ultimate policy/identity conflict → legitimate higher authority selection → binding revised policy returned into future control and action.
- Why this is / is not agent-owned: Agent name/role config and human tool approval are not first-party ethos/governance, and no independent organizational purpose decision right is exercised.
- Evidence: [core/tool_executor.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/core/tool_executor.py); [utils/sandbox_policy.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/sandbox_policy.py); [utils/config_loader.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/utils/config_loader.py); [infiagent/sdk.py](https://github.com/polyuiislab/infiAgent/blob/cf6e04e60a3ed3b3107aebe5f4ed0af52893ed19/infiagent/sdk.py).
- Basis: Bounded negative of available authority/permission and parent modes.
- Confidence: Medium-high.
- Caveats: Institutional governance of a deployment may exist outside first-party installation; don't inherit it.

### Absence scope

- Surfaces inspected: YAML agent definitions, permissions/sandbox, human dangerous-tool confirmation, task metadata, provider models, CLI operator config and release/developer ownership.
- Plausible first-party paths checked: Explicit task approval, changing authorization, model switching, agent identity policies, user goal and safety restrictions.
- Why no material first-party path remains: All traced mechanisms enforce previously chosen tool/task constraints rather than close a legitimate ultimate-policy conflict through an authoritative decision and return.


## Distributed OSS parent arrangement

The reviewed release is an installable Python agent runtime with separately operated local tasks. Open-source contributors and package maintainers don't automatically govern a deployed runtime as its legitimate S5 parent, and an operator's dangerous-tool confirmation is at the task-execution level. No first-party multi-tenant organizational parent mode at S3/S4/S5 is claimed. Separate external orchestration through client SDK calls or MCP servers cannot donate VSM owners to this installation.

## Self-hosted and non-human modes

The same Python backend may be invoked from an SDK, CLI and background task subprocess; configured LLM model deployments require outside API access, and MCP tools can supply external task abilities. Source inspection establishes the installed control loop and state operations but does not execute inference. Human-on-tool-confirm mode is not simultaneously assumed in unattended auto mode. Thinking/ReAct options change action summaries, not recursion.

## Recursion

For one installed infiAgent organization, model-driven task agents and recursively spawned child executors form the operational S1 cells. The shared stack, task messages and failure-safe storage organize task operations but cannot be promoted to S2 or S3 without their specific distinctive variety-control witnesses. ThinkingAgent refreshes working context for S1, not an independent S3*. Cross-task experience write→read is reachable, yet prospective S4 organizational option/decision ownership remains unresolved. Deployer task permissions and identity choices remain external to S5.

## Variety and escalation

The tool registry, child model/tool actors, MCP and background task spawning amplify S1 variety; authorization, file locks, context compaction, max turns, provider failover and manual consent attenuate immediate risk/errors. Failed actions can retry, restore from persisted state, ask humans for tool permission or return a bounded error. This is not proof of broader conflict regulation or independent corrective governance. No empirical reliability percentages or independent safety review asserted.

## Evidence gaps

- This is a pinned first-party source trace, not an executed model-provider benchmark or live test of human approvals, concurrent workers or long-horizon task outcomes.
- S2=— is relative to absent distinct S1 interference attenuation; atomic locks and child task tree are real, but not sufficient to establish S2.
- S3=— applies to absent first-party whole-current multi-operation decision; a configurable task executor or generic CLI isn't by itself a C constructor for S3.
- S3*=— is limited to the actual ThinkingAgent (same-task summary/planner) and trace/approval, not a proof that all possible external critic plugins are absent.
- S4=? is intentionally unresolved for the **installed** optional model-authored global experience write→next-task read path; an example demonstrating a prospective capability option, responsible acceptance/selection and measured future operating change could resolve it. Inversely, source proof that it only copies undifferentiated history would support a bounded negative. Neither is invented now.
- S5=— does not deny external maintainer/user governance; it lacks the first-party ultimate policy settlement/return loop.
