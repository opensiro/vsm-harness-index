---
harness_id: agent0
project_name: agent0
repository: https://github.com/xudafeng/agent0
review_ref: 3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65
reviewed_at: 2026-10-20
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

# agent0

## Review boundary

- System in focus: Shipped `xudafeng/agent0` desktop/CLI/headless local AI agent with real model-tool feedback, persistent profiles/session/computer backends, mission/goal task work, delegating isolated subtasks and recurring agent automations. This is **one agent workspace and its assigned tasks**, not a corporate multi-department organization.
- Purpose and identity: Help an operator complete interactive and scheduled tasks with tool calls, optional computer/Web/MCP connectors, persisted memory, mission progress and durable automation support.
- Relevant environment: Node.js/TypeScript/Electron runtime with configured provider credentials (OpenAI-compatible), desktop or headless profile folder, optional external MCP servers and browser/computer services, host filesystem policies, user-specified missions and schedules. Source `package.json` is private and GitHub repository has no declared license metadata at review: public visibility is not a grant of code reuse rights.
- Standard-distribution boundary: `src/runtime.ts` first-party model tool loop; `src/provider.ts` real LLM API wrapper; `src/agent-run.ts` headless mode/policies; `src/autonomy-tools.ts` and `src/autonomy.ts` mission actions; `src/subagent.ts`; memory and personal-state tools; optional configured `agent-worker.ts`, automation and background schedulers and Jev router. Do not import claimed intelligence from remote computer/MCP providers.
- Credited operating / distribution surfaces: [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`src/provider.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/provider.ts); [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts); [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts); [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/subagent.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/subagent.ts); [`src/agent-automation-runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-automation-runtime.ts); [`src/agent-worker.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-worker.ts); [`src/full-wake.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/full-wake.ts); [`src/memory.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/memory.ts); [`src/memory-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/memory-tools.ts); [`src/personal-state.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/personal-state.ts); [`src/scheduler.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/scheduler.ts); [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts); [`src/jev.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/jev.ts); [`README.md`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/README.md).
- Adjacent first-party surfaces excluded from ownership: Developer `AGENTS.md`, CI Electron packaging, screenshots and demo GIF, `src/eval.ts` manual arithmetic eval, code tests and mocks; any external TypeSafe Jev model or MCP server/remote computer's separate governance; human operator configuration and approval; future hypothetical enterprise deployment. These surfaces may corroborate contracts without becoming autonomous VSM owners.
- First-party operating / deployment modes considered: interactive Electron UI, CLI/headless `runHeadlessAgent` with read-only and trusted-workspace policies, model+tool registry, mission/subagent operation, memory/personal state, optional Jev route confidence fallback, scheduled background/headless automations, event/run history and computer backend connectors. A user-triggered automation remains a goal-scoped run, not a separate sustainable business.
- Recursion level: One supported agent instance and its operational tasks with delegated subprocesses; separate organization/department management requires evidence beyond installed tool names.
- Reviewed revision: `xudafeng/agent0@3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65`, immutable Git tree `bd374acff7a0ca9d6c187e09d92b98607a3a3edb`, stable GitHub repo ID 1376315936; created 2026-09-18T18:58:38Z, nonfork/nonarchived, main. GitHub license metadata absent at the pinned review; source accessible but no positive license reuse grant claimed.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The entry point `createAgentRuntime` assembles configurable first-party tool definitions, creates mission, memory, personal state, automation and run/event stores, and adds external MCP or computer tools only when configured. A configured provider produces text or structured tool calls; a bounded step loop checks execution policy, uses side-effect ledger semantics to prevent duplicate/uncertain replay, dispatches registered tools, records and reintroduces observations into the next provider call. That is a substantive autonomous S1 feedback loop, distinct from model-less tool routing. [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`src/provider.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/provider.ts); [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts); [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts).

`autonomy-tools.ts` supports creating a finite mission task graph, updating task progress, attaching artifacts, requesting a user handoff and evaluation. `subagent.ts` delegates a single focused prompt to an isolated model provider and returns a result, not an independently governed business unit. `agent-automation-runtime.ts` runs time-due configured headless prompts, with backoff and bounded policy; `agent-worker.ts` repeats wake cycles. Memory and personal-state store/user goal fields help context. None of these alone constitutes organization-wide resource control, independent management audit, long-horizon environmental intelligence or constitutional purpose setting. [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts); [`src/subagent.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/subagent.ts); [`src/agent-automation-runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-automation-runtime.ts); [`src/agent-worker.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-worker.ts); [`src/personal-state.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/personal-state.ts).

Jev is optional and routes a chosen tool based on confidence, with main-model fallback; the external Jev service is not credited as a separate VSM owner. The local tool ledger and headless denylist are safety/enforcement mechanisms, not organizational decision owners. [`src/jev.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/jev.ts); [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts); [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts).

## Operational model

Within a configured agent session, the LLM chooses task-contingent tool calls and follows their results to act/answer; run stores and schedules sustain the same operating surface. A user may set a mission, prompt, schedule, policy and workspace, and the assistant may fill steps. The decisive S1 right is model-controlled tool selection, while no separately viable continuing S1 departments, higher-level policy charter or strategic return path is supplied.

## S1 — Operations

- State: A
- Function: Perform model-directed user or scheduled tasks in a persistent desktop/CLI/headless assistant, choosing actual tools and subagent work and updating mission progress from returned observations.
- Disturbance / variety regulated: Unexpected user prompts, variable files/website data, tool errors/timeouts, missing resources, new task subgoals and ambiguous external returns.
- Decisive decision or feedback right: Configured real LLM provider produces function/toolCalls for the current context; createAgentRuntime loops over bounded steps and executes chosen registered tools (computer, web, MCP, skills, mission/memory, subagent), appending tool results to the model context. runHeadlessAgent can invoke the same runtime on a task prompt, including a scheduled trigger.
- Decision owner: Model agent controls which tool/arguments to invoke and how to respond/continue. The first-party runtime checks policy, stores events, bounds maxSteps and supplies tools; human sets credentials/profile and may authorize workspace modes.
- Supporting / enforcement mechanisms: OpenAI-backed Provider interface, createAgentRuntime, ToolRegistry, execution ledger idempotency, agent-run store, mission tools, memory, context assembly, optional TypeSafe Jev router with fallback, desktop/CLI/headless entry points.
- Closure path: Operator input, mission goal or scheduled prompt → model generates text/toolCalls → runtime chooses permitted tool handler, checks ledger/policy, executes and persists results → tool response fed into next model turn → answer, artifacts, mission changes or further tasks. Durable run checkpoint supports resumption.
- Why this is / is not agent-owned: Model's task-contingent action choice, not deterministic scheduler or prewritten pipeline, is the decisive operational step. Disabling the model leaves execution tools and stores without chosen actions.
- Evidence: [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`src/provider.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/provider.ts); [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts); [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/subagent.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/subagent.ts); [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts); [`README.md`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/README.md).
- Basis: Primary explicit model/function-call execution wiring in first-party app source; no paid provider execution claimed.
- Confidence: High for reachable configured S1, subject to external API credentials.
- Caveats: Headless read-only/trusted-workspace tool policies constrain tools and prohibit some automation administration; do not treat all available tools as accessible in every mode. No safety judgment about executing shell or external MCP code.
- Boundary reachability: Shipped createAgentRuntime calls a concrete configured Provider and first-party ToolRegistry; normal runtime and runHeadlessAgent use the same model step/tool observation loop and can invoke model-chosen mission, memory, computer, web, MCP or subagent actions within selected workspace policy.


## S2 — Coordination

- State: —
- Function: No separate S2 interference damping between independently viable continuing S1 organizations; delegated subagents and mission task graphs are pieces of one assigned task.
- Disturbance / variety regulated: Several subtask calls, dependent mission tasks, parallel tool calls, API quota or stale side-effect execution may interact.
- Decisive decision or feedback right: Agent-selected delegate_task runs isolated one-turn provider subtask; task dependency and tool concurrency/ledger gate prevent invalid task transitions. No distinct first-party coordinating owner measures interdepartmental conflict and feeds negotiated adjustments back to multiple viable S1 operations.
- Decision owner: Primary model and deterministic per-call runtime, scheduler/tool execution ledger; not an independent S2 unit managing distinct operational departments.
- Supporting / enforcement mechanisms: SubagentRuntime, MissionStore task dependencies, sequential tool execution labels and ledger, separate session/automation queues.
- Closure path: Current parent task → delegated provider response/mission task update → current parent model consumes result. This resolves one work item, not reciprocal interference across independently viable ongoing operations.
- Why this is / is not agent-owned: Subagents lack separate persistent viability and autonomous business obligation; routine message passing/dependency management cannot establish S2.
- Evidence: [`src/subagent.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/subagent.ts); [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts); [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts).
- Basis: Source-bounded absence at shipped single-agent/session/task mission recursion.
- Confidence: High.
- Caveats: Other applications could deploy multiple ongoing independently viable agent enterprises and add S2 externally, but not demonstrated here.

### Absence scope

- Surfaces inspected: Delegated one-shot model subagents, MissionStore dependency handling, concurrent/sequential tool result execution, persistent session and scheduled workflows.
- Plausible first-party paths checked: Checked whether delegated roles have viable independent obligations and whether coordination detects/attenuates mutual operational interference and returns changes to their behavior.
- Why no material first-party path remains: Shipped subagents are single prompted subtask calls within one agent/mission. DAG and tool sequencing control dependency and execution integrity; no independent viable S1 units and inter-unit conflict feedback or balancing S2 owner are present.


## S3 — Inside-and-now control

- State: —
- Function: No standing inside-and-now organizational manager of multiple viable S1 business operations and their shared resources/commitments.
- Disturbance / variety regulated: Active concurrent jobs, headless errors, failed mission subtasks, interrupted sessions and retry/backoff limits.
- Decisive decision or feedback right: File MissionStore handles one named user goal and task status, model can evaluate mission within that bounded goal. AgentAutomationWake executes user/model-configured scheduled prompts by fixed time, backoff and maxRunMs. Human/host can manage policies. These do not constitute discretionary current authority over a stable portfolio of independently viable S1 departments.
- Decision owner: Model directing a single mission, deterministic wake scheduler, external human setting profile/tool policies; none is a distinct ongoing whole-current S3 owner.
- Supporting / enforcement mechanisms: Mission evaluator/handoff fields, agent-run stores, wake cycles, retry windows, per-tool execution policies, session/run checkpoints.
- Closure path: One task/mission result → current session task progress or evaluator feedback; scheduled job outcome → next configured run/backoff. No whole-organization state → autonomous or parent-governed cross-S1 resource allocation decision → returned accountable operating commitments.
- Why this is / is not agent-owned: The application supervises *task runs* and local budgets, not separate independently viable departments; an escalation/handoff to a human on one mission task is not a standing S3(P) decision contract.
- Evidence: [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts); [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/agent-automation-runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-automation-runtime.ts); [`src/background-runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/background-runtime.ts); [`src/agent-worker.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-worker.ts); [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts).
- Basis: Strong possible parent modes investigated but not established in first-party supported boundary.
- Confidence: Medium-high.
- Caveats: An external owner can use agent0 as a dashboard/executor for S3, but external institution's actual decision and feedback are not evidenced here.

### Absence scope

- Surfaces inspected: Whole mission task status/evaluation/handoff, agent run store, headless automation wake/scheduler, session UI and host-selected policy controls.
- Plausible first-party paths checked: Checked model-managed mission as a potential discretionary S3 current controller, user approval as possible S3(P), and recurring automations as portfolio management.
- Why no material first-party path remains: Each candidate governs a single goal/session or scheduled prompt. Neither a separately viable S1 portfolio nor a standing accountable whole-current decision authority allocating obligations and returning resource/priority decisions is shipped.


## S3* — Complementary audit

- State: —
- Function: No complementary independently authorized audit of an S3 manager's operational truth with correction returned to S3.
- Disturbance / variety regulated: LLM may hallucinate result, tools may complete uncertain external side effects, stored checkpoints may diverge, mission claim may overstate completeness.
- Decisive decision or feedback right: ExecutionLedger prevents duplicate/uncertain tool replay and records tool outcomes; mission evaluation can score the same current mission's output and emit an answer. Those are product/task verification, not independent reality-inspection challenging an S3's reported state of separately viable S1 units.
- Decision owner: Deterministic tool receipt/ledger gate and provider-assisted mission evaluator under same user-directed workflow; no separate first-party S3* auditor.
- Supporting / enforcement mechanisms: ToolExecutionUncertainError and durable run store, mission evaluate tool, task status, console/activity trace, agent run event log.
- Closure path: Tool call → ledger success/uncertain status → next model turn or block; mission work → evaluation text/score → user-agent context. No management report → distinct independent field-access audit judgment → returned S3 corrective resource decision.
- Why this is / is not agent-owned: Per-tool certainty and optional task evaluator aren't complementary governance audit; no separate accountable S3 management reporting channel exists.
- Evidence: [`src/execution-ledger.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/execution-ledger.ts); [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`src/autonomy-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy-tools.ts); [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts); [`src/eval.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/eval.ts).
- Basis: Bounded negative after checking evaluator, execution ledger, tool-side effects, traces and human review paths.
- Confidence: High.
- Caveats: Independent code reviews of agent0 are outside assessed distribution and do not create S3* for this agent.

### Absence scope

- Surfaces inspected: ExecutionLedger durability/uncertain marker, model task evaluation, mission result fields and run/activity traces.
- Plausible first-party paths checked: Checked independent work-product evaluation, underlying tool outcome receipts, external computer observations and durable trace as possible complementary management audit.
- Why no material first-party path remains: These enforce task/side-effect integrity or assess one current mission's output. No distinct S3 manager ordinary report, independently authorized reality-inspection path or binding corrective return to S3 exists.


## S4 — Outside-and-then intelligence

- State: —
- Function: No independent outside-and-then future strategic-intelligence owner selecting accepted changes to a continuing organizational capability portfolio.
- Disturbance / variety regulated: Stored past memory, changing user goals, future scheduled prompts and provider performance might motivate future adaptations.
- Decisive decision or feedback right: Memory tools store/search experiences and personal goals, mission task planning and agent automation can schedule recurring *specified* prompts. Jev selects tools with confidence fallback. No shipped loop autonomously monitors prospective external environment, compares long-term adaptation alternatives and adopts strategic organizational changes as future operating obligations.
- Decision owner: Operator/user defines personal objectives and scheduled prompts; model chooses current-task actions; deterministic wake mechanism executes schedule. No standing strategic S4 decision owner.
- Supporting / enforcement mechanisms: PersonalState goals/tasks, episodic memory, MissionStore, ScheduleAgentRun tool, AgentAutomationWake, Jev route/fallback, recurring cron.
- Closure path: Configured automation time → new bounded prompt task, memory item → reused in current context. No independent outside/then intelligence → new future strategic option → legitimate acceptance and change into multi-operation current capability.
- Why this is / is not agent-owned: Persistence and temporal execution do not by themselves constitute prospective strategic function. A single model could complete research about future if prompted, but no first-party continuous S4 research/adaptation feedback is established.
- Evidence: [`src/personal-state.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/personal-state.ts); [`src/memory-tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/memory-tools.ts); [`src/agent-automation-runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-automation-runtime.ts); [`src/agent-worker.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-worker.ts); [`src/jev.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/jev.ts); [`src/autonomy.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/autonomy.ts).
- Basis: Bounded negative after checking headless recurring autonomy modes and long-horizon goal storage.
- Confidence: Medium-high.
- Caveats: Users can configure automations that perform periodic research; that is a task capability without owned independent strategic-adoption mandate.

### Absence scope

- Surfaces inspected: MemoryStore recall, PersonalState future goals/tasks, scheduled AgentAutomationWake and headless agent-worker, mission creation and Jev routing.
- Plausible first-party paths checked: Checked recurrence as autonomous strategic research, persistent goals as prospective authority, memories and adaptive tool routing as organizational capability adaptation.
- Why no material first-party path remains: No first-party supported standing environmental intelligence and option-selection/acceptance loop returning new organizational capability. Recurrence executes specified prompts and stored goals rather than creating/authorizing future organizational adaptation.


## S5 — Policy and identity

- State: —
- Function: No first-party legitimate constitutional/identity authority for a continuing organization, autonomous or recognized parent-governed.
- Disturbance / variety regulated: Untrusted MCP/computer tool access, write permissions, user profiles and arbitrary scheduled actions.
- Decisive decision or feedback right: Read-only and trusted-workspace policies restrict tool calls, and headlessAlwaysDenied prevents altering automation tools in some modes. User controls profile credentials and mission goal; no authorized first-party autonomous body deliberates/revises identity or purpose and returns binding constitutional decisions.
- Decision owner: Human/profile chooses security policies, deterministic tool access filter and agent runtime enforces. There is no separate parent-governed S5 decision-return path.
- Supporting / enforcement mechanisms: ToolExecutionPolicy, denylist, per-workspace agent run, memory/mission stores, desktop preferences.
- Closure path: Policy configuration → tool allowed/blocked or run fails. This is a safety/local capability enforcement path rather than constitutional decision → organizational charter → returned changed operations.
- Why this is / is not agent-owned: Tool permission rules do not define a viable enterprise's identity. User being able to change settings or give an instruction does not meet standalone S5=P requirements.
- Evidence: [`src/agent-run.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/agent-run.ts); [`src/tools.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/tools.ts); [`src/runtime.ts`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/src/runtime.ts); [`README.md`](https://github.com/xudafeng/agent0/blob/3eb4d8b31fa1c0b3ba785c0c773e33bc13f30f65/README.md).
- Basis: Bounded negative across headless and interactive policy modes.
- Confidence: High.
- Caveats: External users or deployers may have legitimate organizational identity governance; not implemented as a first-party closed loop here.

### Absence scope

- Surfaces inspected: Headless policy denied tool sets, workspace permissions, user profile data and model-run tool configuration.
- Plausible first-party paths checked: Checked per-workspace write trust, user/agent scheduling power, user-authorized handoff and stored personal goal setting for legitimate constitutional authority.
- Why no material first-party path remains: First-party checks enforce predefined user/developer tool limits; no organizational self-identity charter decision or recognized parent decision/return is established.



## Recursion

An agent run can plan and execute one mission through various model tools, but its subagents are one-shot task executors and scheduled invocations are repeated goal-scoped operations. Nothing converts multiple tools, sessions or external MCP services into an autonomous VSM organizational metasystem by default. First-party S1 exists without supporting a positive S2/S3/S3*/S4/S5 finding at a continuing separately viable department recursion.

## Variety and escalation

Novel model/tool data and provider errors generate operating variety. The agent can adapt tool choices from returned observations, retry or refuse uncertain side effects, and request task-level human handoffs. A blocked mission/task or failed scheduled run is a normal status transition, not independently an algedonic S3/S5 escalatory channel. Periodic wake and memory keep jobs/cases available, not a strategically intelligent organization by themselves.

## Evidence gaps

- Immutable first-party source reviewed; positive S1 depends on a configured model provider in a shipped supported operating mode, not a separately reproduced paid deployment.
- No actual provider call or GUI interaction was executed in assessment; source wiring and tests are distinct from empirical model quality. External MCP/computer service internals and TypeSafe Jev provider are outside credited ownership.
- Repo GitHub license metadata is absent and `package.json` uses `private: true`. This statement concerns source reuse rights, not Index assessment eligibility.
- If external integrations are deployed as continuing independently viable businesses, their management/strategy/policy relations require a different evidence-bound review. This negative result is bounded to shipped first-party app modes.
