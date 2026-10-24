---
harness_id: connectonion
project_name: ConnectOnion
repository: https://github.com/openonion/connectonion
review_ref: 7011faa911e2563e485f865db5be60f6e595f1bd
reviewed_at: 2026-10-18
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

# ConnectOnion

## Review boundary

- System in focus: One installable ConnectOnion Python agent harness and its normal `Agent.input` execution loop, including a configured `co ai` instance and the shipped selected tool/event/skill/subagent/host mechanisms. The recursion is the deployed agent application; remote models, organizations of contributors and independently installed users' agents are not assumed inside the boundary.
- Purpose and identity: Respond to operator/user requests and execute bounded file, shell, browser, external-tool and specialist agent actions while preserving conversation, observations and permitted task state; ship a reusable agent runtime with CLI/self-hosted paths.
- Relevant environment: Incoming user and inbox messages; model inference and remote provider/tool responses; filesystem/terminal/browser outcomes; operator-approved exceptions and trust identities; runtime timeouts, context limits and recurrent hosted sessions.
- Standard-distribution boundary: Shipped `connectonion.core.Agent`, tool executor and configured built-in `co ai` factory, first-party bundled optional plugins and host scheduling/trust surfaces. `co ai` is the packaged concrete default and may use an external LLM or external Codex/Claude Code worker. Test/eval/dogfood and outside provider internals are not borrowed as first-party organizational decision rights.
- Credited operating / distribution surfaces: [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L343); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L654); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L820); [tool_executor.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/tool_executor.py#L183); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L108); [subagents.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/subagents.py#L143); [approval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/tool_approval/approval.py#L409); [skills.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/skills.py#L670); [schedule.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/host/schedule.py#L1); [trust_agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/trust/trust_agent.py#L200). A bundled optional evaluation path is inspected but credited only to the extent its function is closed: [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L165).
- Adjacent first-party surfaces excluded from ownership: Repository tests, CI, maintainer contributor reviews, published developer-use skills/examples (unless loaded in the specific runtime), third-party code-writing agent executors and their internal decisions, remote inbox participants' organizations, external model host, and standalone diagnostics. A skill's authoring guidance is an operating option, not proof that future system adaptation is automatically executed.
- First-party operating / deployment modes considered: Direct `Agent.input` with selected tools/plugins; packaged `co ai` with file/bash/planning/subagent and approval tool surfaces; installed/loaded optional Skill; standalone hosted turns and scheduler/inbox entry; optional independent test `eval` plugin, trust and user approval controls.
- Recursion level: One ConnectOnion agent application; delegated subagents are individually executable S1 participants, but plurality and scheduler coexistence alone do not imply a nested viable organization or independent S2/S3 owner.
- Reviewed revision: `7011faa911e2563e485f865db5be60f6e595f1bd` (frozen in candidate #202 / serial batch #1669; not silently advanced to current upstream main).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party `Agent.input` restores or creates a session, records the task and invokes `_run_iteration_loop`. The loop asks the configured LLM adapter for the next decision with registered tool schemas, executes selected tool calls through `execute_and_record_tools`, appends structured results/errors, dispatches event handlers, and re-enters the model until a final answer, bounded stop or interrupt. `_get_llm_decision` and the tool executor preserve durable trace and conversation observations. [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L343), [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L654), [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L820), [tool_executor.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/tool_executor.py#L183).

The default `co ai` factory assembles this real runtime with built-in file, shell, TodoList, user-interaction, skill and subagent tools plus host permission hooks and context compaction; `subagents.task` instantiates a separate `Agent` with a selected prompt/tool set and returns the result to the caller. External Codex/Claude Code plugin executions are *tools* at this boundary: no vendor worker organization is credited as first-party S2–S5. [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L108), [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L165), [subagents.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/subagents.py#L143).

An optional user-configured `eval` plugin makes an additional model call to compare a completed turn's requested intent with trace/answer and emits its verdict to UI and trace after task completion. Hosted scheduler dispatches configured recurring prompts/commands with durable schedule receipts; TrustAgent fast-rules/optionally model-based stranger admission, and explicit tool approval, gate access to operating tools/entry. These separate control surfaces are assessed function-first rather than inferred from the terms `eval`, `trust`, `scheduler` or `agent`. [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L165), [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L255), [schedule.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/host/schedule.py#L1), [trust_agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/trust/trust_agent.py#L200), [approval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/tool_approval/approval.py#L409).

## Operational model

The primary operating unit is the model-backed task agent; delegated specialized subagents run separately but their caller owns per-request integration and tool/result handling. First-party deterministic hooks, pause/approval and limits constrain individual task execution. Some `co ai` modes permit interactive self-authored skill files and continued tool use; no automatic app-wide future-governance, S3 resource allocation or independently corrective S3* is assumed merely because these capabilities share a package.

## S1 — Operations

- State: A
- Function: Perform user-specified work by model-directed choice of first-party registered tools/subagents and respond using returned execution observations.
- Disturbance / variety regulated: Changing freeform user requests, tool failures/outputs, subagent responses, environment state, interruptions and context changes during the turn.
- Decisive decision or feedback right: Agent model chooses next tool call or final response given accumulated messages/tool observations; a delegated subagent makes local model decisions within its allowed tools.
- Decision owner: Configured model-backed `Agent`/concrete `co ai` first-party execution loop; provider infrastructure is a dependency, not an imported organizational actor.
- Supporting / enforcement mechanisms: LLM adapters, ToolRegistry and tool executor, conversation/trace, explicit operator approvals, TodoList, optional subagent and skill registration, iteration bounds and stop gates.
- Closure path: User/input or hosted inbound prompt → `Agent.input` → `_run_iteration_loop` → `_get_llm_decision` → first-party tool executor or delegated `task` → captured tool_result/error in messages/trace → next model decision/answer or bounded stop.
- Boundary reachability: The exported `Agent.input` directly calls the real run loop; default `create_agent` registers first-party plugins and tools on that concrete `Agent`, not only a sample. Subagent tool explicitly instantiates and executes a real local `Agent`.
- Why this is / is not agent-owned: Model-selected tool/response decisions condition on live observations; executor, provider transport, static permissions and scheduled entry do not substitute for the agent's choices.
- Evidence: [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L343); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L654); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L820); [tool_executor.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/tool_executor.py#L183); [subagents.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/subagents.py#L143); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L165).
- Basis: Explicit first-party runtime source and actual tool/result return.
- Confidence: High for shipped code structure/reachability; no live provider workload benchmark in this review.
- Caveats: Requires configured provider, runnable tools and permissions; subagents/remote coding CLIs are not evidence of autonomous other VSM functions.

## S2 — Coordination

- State: —
- Function: No proven first-party S2-specific attenuation of concrete clashes among distinct viable S1 operational participants at assessed recursion.
- Disturbance / variety regulated: Potential conflicting tool writes, duplicate requests and simultaneous subordinate work; the reviewed mechanisms bound a tool session and admission rather than negotiate interference among independent cells.
- Decisive decision or feedback right: Parent model chooses when to invoke `task` or other tools; deterministic host approval/permission rules enforce per-request safety.
- Decision owner: Task-local caller/model and mechanical permission/host mechanisms, with no evidenced distinct inter-unit adjustment owner.
- Supporting / enforcement mechanisms: Per-call sequential tool execution, subagent task API, session serialization/host state, tool approval and provider workroom state.
- Closure path: Delegated subagent sends result back to caller; no demonstrated disturbance between two independent S1 units → conflict-sensitive coordination choice → returned stabilizing changes to their later operations.
- Why this is / is not agent-owned: Subagent dispatch and same-turn tool ordering are composition/scheduling, not a distinct operational S2 conflict attenuation loop.
- Evidence: [subagents.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/subagents.py#L143); [tool_executor.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/tool_executor.py#L183); [provider_workroom.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/host/provider_workroom.py#L27); [approval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/tool_approval/approval.py#L409).
- Basis: Reviewed installed delegation and execution coordination surfaces; bounded negative.
- Confidence: Medium-high at defined distributed app boundary.
- Caveats: Custom adopters can build their own cross-agent coordinator; that is not shown as an included native S2 operating mode.

### Absence scope

- Surfaces inspected: Core executor and Agent loop, packaged co ai subagents and plugin assembly, hosted provider workroom, approval/permissions and scheduler.
- Plausible first-party paths checked: Multiple tools and delegated Agents, same-turn ordering, session/host serialization, workroom claim/admission and recurring tasks.
- Why no material first-party path remains: There is no evidenced first-party identification of a specific inter-S1 contention/oscillation, discretionary mutual adjustment and closed feedback between distinct S1 cells; ordering and safety locks do not meet this function.

## S3 — Inside-and-now control

- State: —
- Function: No established whole-current aggregate control loop across independently executing Agent operations.
- Disturbance / variety regulated: Task backlogs, concurrent hosted sessions, scheduled work, tool costs and competing commitments that could require system-level current prioritization.
- Decisive decision or feedback right: Individual task model sets steps/tools; host scheduler executes author-specified entries; approval hook enforces permissions. No app-scoped present-wide resource/commitment decision-right shown.
- Decision owner: Per-agent model, deterministic hosted scheduler and external operator setting static job rules; no demonstrated S3 owner or parent S3 adjudication/return cycle.
- Supporting / enforcement mechanisms: TodoList, per-agent max iterations, stop handling, workroom run/trace, schedule-state and status views, host deployment.
- Closure path: Per-task execution and scheduling have operational completion receipts, but no whole-current work-state integration → binding cross-S1 prioritization/commitment negotiation → changed subsequent agent operations.
- Why this is / is not agent-owned: An autonomous per-task plan is not S3 at this recursion, nor does a cron dispatcher become an organizational current-control decision-maker.
- Evidence: [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L654); [schedule.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/host/schedule.py#L1); [todo_list.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_tools/todo_list.py#L51); [provider_workroom.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/host/provider_workroom.py#L27); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L108).
- Basis: Source-inspected runtime, scheduling and host responsibilities; bounded negative.
- Confidence: Medium-high for default/packaged modes.
- Caveats: External owner may use manual controls for their larger organization; not credited as a ConnectOnion-shipped parent return path.

### Absence scope

- Surfaces inspected: Agent control loop, TodoList, host scheduler, provider workroom, network inbox and approval/trust host.
- Plausible first-party paths checked: Scheduled work/state, per-turn plan and progress, multi-session host status, delegated subtasks and run cancellation/approval.
- Why no material first-party path remains: The inspected mechanisms schedule or constrain one work item/session and report status; they do not hold a cross-unit current-view right to arbitrate shared capacity/commitments and return binding operational decisions.

## S3* — Complementary audit

- State: —
- Function: Complementary independent challenge of ordinary operating reality returning into current control was not established.
- Disturbance / variety regulated: Agent's potentially misleading self-report of completed work and inaccurate tool outcomes; optional eval can score such reports but is not wired into current control.
- Decisive decision or feedback right: Optional `eval` computes post-turn expected vs observed summary and LLM pass/fail; writes an evaluation UI/trace event, with no evidenced independent authority to challenge an S3 claim and force current operational correction.
- Decision owner: Extra optional scorer model plus caller choosing plugin, separated from required first-party operating control; it is not demonstrated an S3* operating auditor.
- Supporting / enforcement mechanisms: Turn trace, summarization, `on_complete` handler, expected-outcome prompt, UI eval event; debug/auto-debug instrumentation.
- Closure path: Agent turn completes → optional post-turn judge reads requested intent/actions/response → records and displays evaluation. Missing return: independent finding → accountable whole-current S3 reconsideration/withholding/corrective decision → changed S1 operation.
- Why this is / is not agent-owned: A model grading completed task quality is genuine evaluation but its stored output is not a complementary governance audit with closed corrective challenge of current-control reporting.
- Evidence: [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L109); [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L165); [eval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/eval.py#L255); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L547); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L165).
- Basis: Explicit optional eval handler, separate post-task output and default factory plugin list inspection.
- Confidence: Medium-high in evaluated native paths.
- Caveats: Adopters can read UI evaluation and choose manual corrective interventions externally; this is not an evidenced built-in S3* return path.

### Absence scope

- Surfaces inspected: `eval` module's pre/post-turn hooks, normal Agent on_complete handling, trace/event emission, default co ai plugin set and debug tools.
- Plausible first-party paths checked: Standalone model evaluator, expected-output comparison, trace inspection, stop/error hooks, operator approval and debug prompts.
- Why no material first-party path remains: The grade is optional, emitted after completion and persisted as UI/trace. No native S3 current-control review/adjudication and corrective return consumer was shown; tests/debug and user-initiated retries are not themselves S3*.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Plausible first-party prospective capability creation via model-selected skill authoring, but an accountable future-adaptation decision plus return into subsequently installed operation is not established.
- Disturbance / variety regulated: New automation sites, changed external interfaces, recurring tool workflows and a need for durable reusable future capabilities beyond the current task.
- Decisive decision or feedback right: The shipped model-backed co ai can write files and invoke skills; packaged browser-workflow-skill-builder instructs a user/agent to create a new SKILL.md under project skills and test helper scripts. Who accepts/promotes a candidate as a system future strategy/capability and when it becomes active is not fully established.
- Decision owner: Model-assisted skill authoring under user tool permissions; first-party skills loader discovers/loads available skills. The prospective parent/operator selection and systematic future-control authority remain unresolved.
- Supporting / enforcement mechanisms: File tools, developer-selected skills, `skill` invocation, project skill discovery, runtime prompt instructions and tool approval.
- Closure path: Novel task/site issue → optionally invoke supplied skill-builder recipe → model/file tools create or edit a project skill → loader may discover and invoke this artifact on a later task. Missing: evidenced S4-specific option comparison/selection by legitimate future intelligence owner and a returned institutional decision admitting a new capability to future operation.
- Why this is / is not agent-owned: Writing durable skill code under a prompted task may be ordinary S1 programming work; a usable skills loader alone is not proof that the agent exercises a distinct S4 future/environment adaptation right. Material shipped candidate precludes an unqualified absence conclusion.
- Evidence: [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L108); [skills.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/skills.py#L312); [skills.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/skills.py#L670); [skills.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/skills.py#L801); [SKILL.md](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_skills/browser-workflow-skill-builder/SKILL.md#L14); [SKILL.md](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_skills/browser-workflow-skill-builder/SKILL.md#L54); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/core/agent.py#L654).
- Basis: Specific shipped skills authoring, file I/O and future load path, but missing conclusive S4 decision/return reconstruction.
- Confidence: High for authoring/availability mechanics; low for whole S4 ownership state.
- Caveats: Need a source-verified or controlled reproduction tying the model's prospective selection, durable skill admission and later changed operating options to one first-party S4 function, separated from ordinary user-requested coding.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate-purpose/organizational-identity decision and returned policy closure established, despite trust and tool authorization.
- Disturbance / variety regulated: Untrusted remote clients, tool risk, provider delegation and access-right changes; these are operational admission/safety disturbances, not by themselves ultimate identity disputes.
- Decisive decision or feedback right: TrustAgent applies configured allow/deny rules and optionally a model 'ask' for unknown remote clients; owner/operator approves tool execution. Nothing in these paths defines and adjudicates the installed agent's ultimate purpose or ethos on behalf of its governed organization.
- Decision owner: Operator-configured trust/permission policies, per-request user, deterministic gate and bounded trust model decision for admission; not an established S5 organizational parent.
- Supporting / enforcement mechanisms: Signed client identity/trust levels, trusted-client onboarding, tool approval modes, permission scopes and audit/trace.
- Closure path: Client request → trust allow/deny, or tool action → permission/approval → execution/blocked outcome; no distinct ultimate identity/purpose dispute → legitimate parent decision → accepted revised governing policy affecting later operations was established.
- Why this is / is not agent-owned: An autonomous classifier of access to an endpoint is not the final legitimate guardian of an organization's identity; self-hosted owner may provide that authority externally.
- Evidence: [trust_agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/trust/trust_agent.py#L200); [trust_agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/network/trust/trust_agent.py#L253); [approval.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/tool_approval/approval.py#L409); [skills.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/useful_plugins/skills.py#L583); [agent.py](https://github.com/openonion/connectonion/blob/7011faa911e2563e485f865db5be60f6e595f1bd/connectonion/cli/co_ai/agent.py#L165).
- Basis: Explicit first-party trust and permissions control plus boundary-relative negative adjudication.
- Confidence: Medium-high for selected packaged modes.
- Caveats: Self-hosted operators retain ultimate external governance of what this agent is for; no first-party parent-mode closure is claimed.

### Absence scope

- Surfaces inspected: Host TrustAgent and client identity, tool approvals and mode permissions, co ai wiring, dynamic skill permission scope, self-hosted application configuration.
- Plausible first-party paths checked: Trust model-based stranger admission, whitelist/blocklist mutation, 'full access' grant and human tool approval.
- Why no material first-party path remains: These decide *who may enter or do a specific act* under already installed policy, not settle an ultimate purpose/identity conflict or return binding S5 legitimate-policy resolution to the application.

## Distributed OSS parent arrangement

An application user's consent to one tool and a trust decision about a remote client are real but restricted permissions, not a proven first-party S3/S4/S5 parent governance mode. The organization maintaining the OSS repository, model provider and any user's operator organization are different systems. S4 remains unresolved due to an actual shipped skill authoring/activation candidate, not a generic assertion that all human configuration counts as parent ownership.

## Self-hosted and non-human modes

The same first-party task loop operates in direct Agent instances and packaged co ai with chosen tools. First-party host scheduling repeatedly initiates independently bounded turns. Optional `eval` adds model judging after the task (not default mandatory operational acceptance). External hosted model choice or remote coding-agent work is not counted as internal S2–S5. This is pinned-source assessment; no credentials, live external model or remote browser/social account behavior were exercised.

## Recursion

Multiple task agent instances and specialized subagents can be deployed with returned results to a caller, but the source reviewed does not establish a second complete viable recursive organization with independent metasystem closures. Recursion is fixed at one ConnectOnion application.

## Variety and escalation

Iteration bounds, stop signals, no-progress guard, tool approval, trust admission, context compaction and host scheduler reduce operating variety and define intervention gates. They are not automatically credited as systemic coordination, current management, independent audit, prospective intelligence or ultimate-policy authority. Exceptions can be returned to the requesting model/user without evidence of a separate S3/S4/S5 organ.

## Evidence gaps

- **S4=?** The packaged model-driven coding runtime can generate durable reusable project skills, and the first-party skills loader discovers those. Trace whether a subsequent run actually loads/adopts a self-authored, externally relevant capability under a deliberate prospective option-selection/approval right rather than executing a one-off coding request.
- Optional evaluation has a real output path but no evidenced operating S3 corrective consumer; therefore S3* is a bounded `—`, not a promise of independent operational audit.
- No live hosted agent/provider/credentialed inbox execution, remote worker internal governance, cloud deployment or integration tests were attempted. External customization could change the mapping and requires new evidence.
