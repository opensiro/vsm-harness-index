---
harness_id: aero
project_name: Aero
repository: https://github.com/ronak-create/aero
review_ref: b66c50df07b1fbe5915e398fb5e7e9807b3d23a3
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Aero

## Review boundary

- System in focus: the first-party `ronak-create/aero` Python coding-agent distribution at frozen revision `b66c50df07b1fbe5915e398fb5e7e9807b3d23a3`, including its model/tool loop, built-in coding/web/planning tools, approval callbacks, plugin-tool loading, conversation/session handling and interactive/TUI/one-shot execution surfaces.
- Purpose and identity: perform software-engineering work in the user's current project directory by letting one model-backed coding actor inspect files and external information, select tools, modify/run the project subject to approval policy, observe results and iterate toward the requested outcome.
- Relevant environment: user task and follow-ups, current project filesystem, shell/process results, web resources fetched for the current task, provider/model responses, user approval decisions, process-local todo state, optional user-supplied plugins and saved conversation history.
- Standard-distribution boundary: `agent.py`, the shipped built-in tool registry/implementations, CLI/TUI callbacks and approval handling, configuration, plugin loading and supported save/load interaction are inside. Atria or another OpenAI-compatible inference endpoint, target-project code/governance, arbitrary user-authored plugins and the operating system are dependencies/environment rather than first-party organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `agent.py`; `cli.py`; `config.py`; `llm_client.py`; `tools/__init__.py`; `tools/fs_tools.py`; `tools/shell_tools.py`; `tools/web_tools.py`; `tools/todo_tools.py`; and the corresponding TUI path where it supplies the same first-party agent loop and approval callbacks.
- Adjacent first-party surfaces excluded from ownership: repository tests, development test runner, example plugin, UI rendering/theme helpers and contributor/repository maintenance surfaces. User-authored plugin code is not credited as a first-party organizational function merely because Aero can load it.
- First-party operating / deployment modes considered: line REPL, full-screen TUI, one-shot/headless-style CLI invocation, normal approval mode, explicit auto-approve (`--yolo` or `/yolo`), conversation save/load and built-in plus discovered plugin-tool exposure.
- Recursion level: one Aero conversation/agent loop acting on one project task is the assessed organization. Built-in tools, todo state and plugins are capabilities/actions of that S1 rather than separate S1 operational units. Separate Aero processes or saved sessions are not composed into a higher-level first-party organization by the pinned distribution.
- Reviewed revision: `b66c50df07b1fbe5915e398fb5e7e9807b3d23a3`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Aero is a compact first-party coding-agent runtime. Its documented and implemented loop is model request → optional tool calls → tool execution/result messages → another model request until the model returns no tool calls or the configured iteration bound is reached. The same `run_turn()` implementation backs line/TUI-style interaction; UI callbacks render streaming output, report tool state and decide whether dangerous tools receive human approval.

The model is explicitly instructed to plan nontrivial work, inspect before editing and verify changes after mutation. The built-in registry exposes read/write/edit, directory/glob/grep search, shell execution, URL fetching, image reading and a small todo scratchpad. File writes, edits and shell commands are classed as dangerous and pass through `on_approve` unless auto-approve is enabled. Returned tool results are appended as tool-role messages and therefore directly alter the same model actor's subsequent decisions.

Tool calls from one model response are executed by a single sequential loop over the returned calls. The callback contract can correlate separate calls by provider call id, but Aero does not create independent model-backed workers for them. The todo tool is explicitly an in-memory planning scratchpad whose state lasts only for the process. It is not a project-management/controller subsystem.

Plugins extend the model-facing tool registry by loading user-supplied Python schemas/callables at startup. This is a generic capability extension point: the pinned first-party distribution does not supply a function-specific multi-agent, audit, S3, S4 or S5 constructor through that mechanism, and arbitrary plugin behavior is outside the first-party evidence boundary.

Conversation persistence is simple. `/save` serializes the current model-message list to a project-local JSON file and `/load` restores it. This lets the same operational actor resume conversational context, but it does not introduce an independent memory-governance or adaptation actor.

Primary evidence:

- [`README.md`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/README.md)
- [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py)
- [`cli.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/cli.py)
- [`tools/__init__.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/__init__.py)
- [`tools/todo_tools.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/todo_tools.py)
- [`tools/web_tools.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/web_tools.py)

## Operational model

For each user turn, Aero supplies the current message history and tool schemas to the configured model. The model can answer directly or return one or more tool calls. Aero executes requested tools under its approval/error handling, appends each result to conversation state and asks the same model actor to continue. This closes an autonomous sensing/decision/action/feedback loop for software-engineering work when the selected actions are permitted.

Human approval in normal mode is an operational gate on selected side effects rather than the owner of the coding decisions themselves. Explicit auto-approve removes those prompts while keeping the same model/tool loop. Read/search/web/todo operations execute without approval; write/edit/shell operations require approval unless auto-approved.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected project by interpreting the user task, inspecting local/external evidence, selecting coding/tool actions, applying or running permitted actions, observing results and iterating toward an answer or completed change.
- Disturbance / variety regulated: heterogeneous source trees, incomplete task information, file contents, search and shell output, external documentation needed for the current task, failed actions, implementation alternatives and changed evidence encountered while coding.
- Decisive decision or feedback right: choose what evidence to inspect, which exposed tool/action to invoke next, what content/change/command to attempt and when to stop tool use and return a final response within externally configured execution limits.
- Decision owner: the model-backed Aero coding actor instantiated by `run_turn()`.
- Supporting / enforcement mechanisms: built-in tool registry; provider adapter; tool-result message plumbing; dangerous-tool classification and approval callback; iteration limit; interrupt handling; conversation state; optional todo scratchpad; plugin-tool discovery; CLI/TUI transports.
- Closure path: user task/current context → model request → model-selected tool call(s) → Aero approval/execution/error path → tool/environment result appended to messages → same model actor receives the result on the next iteration → next action or final response.
- Boundary reachability: standard REPL, TUI and one-shot CLI modes directly invoke the repository-owned loop and tools; no application-authored orchestration layer is required.
- Why this is / is not agent-owned: removing the model-backed actor while retaining Aero's tools, approval callbacks and state removes the open-ended task-specific judgment that chooses and sequences coding actions. Human approval can veto a dangerous side effect but does not select the coding plan/action sequence on the actor's behalf.
- Evidence: [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py); [`README.md`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/README.md); [`tools/__init__.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/__init__.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: inference is supplied by an external provider, and dangerous operations may require human approval in the default mode. The autonomy claim is for the shipped model/tool decision-and-feedback role, not unrestricted side-effect authority.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established at S2 level because one Aero conversation exposes one primary model-backed S1 rather than multiple distinct S1 operational units with a concrete mutual interference, conflict or oscillation relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: multiple tool calls can occur in one model response, but `run_turn()` executes them sequentially as actions of the same S1; plugin tools are generic callables; saved sessions and todos are state mechanisms rather than inter-S1 coordination.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation → changed subsequent S1 behavior loop exists in the reviewed standard distribution.
- Why this is / is not agent-owned: provider tool-call plurality is not operational-unit plurality. No subagent/team/delegation lifecycle or first-party constructor specifically aimed at regulating interference among independent S1 units was found.
- Evidence: [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py); [`tools/__init__.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/__init__.py); [`README.md`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user could author a plugin that talks to another agent or run several Aero processes externally, but generic extensibility/external composition does not establish first-party S2 at this boundary.

### Absence scope

- Surfaces inspected: core agent loop; tool-call execution order; built-in tool registry; plugin loader; CLI/TUI/session surfaces; todo state; repository tree/tests for runtime topology.
- Plausible first-party paths checked: subagent/delegation/team APIs; concurrent model-backed workers; multiple tool calls; plugins as possible worker constructors; multiple saved conversations/processes; shared todo/session state.
- Why no material first-party path remains: the standard runtime exposes one coding actor and sequentially executes its actions. Generic plugin/session facilities do not supply an S2-specific coordination relation or a concrete inter-S1 disturbance/feedback witness.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-current organizational control function distinct from the coding S1 and deterministic/operator execution limits was established.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. Todo planning, iteration caps, interrupts, approval gates and current conversation state regulate one task loop rather than organization-wide priorities, commitments, resources or accountability across S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: process-local todo list; `max_iterations`; user interrupt; approval/auto-approve mode; tool errors returned to the model; request timeout/configuration.
- Closure path: not applicable; no whole-system view of multiple relevant current operations plus substantive management decision and return-to-operation path was found.
- Why this is / is not agent-owned: the model can update its own todo list and react to failures, but this is self-management of the S1 task. Runtime limits and approvals are fixed/operator controls, not a separate manager owning organizational current-control discretion.
- Evidence: [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py); [`tools/todo_tools.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/todo_tools.py); [`cli.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/cli.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: task planning and operational guardrails are useful current-control mechanisms at the action level without satisfying the stronger organization-level S3 threshold.

### Absence scope

- Surfaces inspected: todo planning implementation; agent iteration lifecycle; tool approval callbacks; configuration/timeout/interrupt paths; conversation/session handling; CLI/TUI controls.
- Plausible first-party paths checked: planner as manager; todo board as whole-current state; approval owner; iteration/budget controller; plugin supervisor; session manager; error/retry control.
- Why no material first-party path remains: every located mechanism governs one operational conversation/task or enforces operator-selected limits. No separate actor/path receives a whole-organization current view and owns substantive cross-operation resource/priority/commitment intervention.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit role with sufficiently independent access, audit judgment and corrective return into supported runtime operation was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. The system prompt tells the same coding actor to verify its work by re-reading/running tests/executing code, but no separate runtime reviewer/judge challenges the actor's conclusions.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ordinary read/shell tools, model self-verification guidance, approval/diff presentation and repository development tests.
- Closure path: not applicable; no independent challenge → audit judgment → corrective-control return loop was found.
- Why this is / is not agent-owned: verification is performed or interpreted within the same S1 coding loop. Human approval reviews a selected side effect rather than independently auditing operational truth and returning a corrective verdict through a dedicated first-party audit role.
- Evidence: [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py); [`README.md`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: testing, diff review and user approval can improve correctness without establishing S3* independence.

### Absence scope

- Surfaces inspected: system verification instructions; core loop; dangerous-tool approval/diff path; repository tests/test runner; plugin mechanism; session history and result callbacks.
- Plausible first-party paths checked: independent reviewer/judge agent; second-pass verifier; test evaluator role; human approval as audit; plugin-provided audit; post-run quality controller.
- Why no material first-party path remains: all standard verification evidence is consumed by the same operational actor or by the user as an execution gate. No first-party independent audit judgment is wired back into subsequent current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective outside-and-then intelligence loop that changes Aero organizational strategy/capability was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. `fetch_url` lets the coding actor retrieve external information for the present task, while saved history/todos/plugins provide current capabilities/state; none supplies a future/environment sensing and organizational adaptation decision loop.
- Decision owner: not established.
- Supporting / enforcement mechanisms: URL fetch tool; provider/model configuration; plugin discovery; saved conversation context; todo planning.
- Closure path: not applicable; no external/future distinction → adaptation option → strategic capability/current-control change → subsequent-operation return loop was found.
- Why this is / is not agent-owned: the same S1 may read web documentation and then change code for the user task. That is environment sensing inside operations, not a distinct function that changes Aero's own strategy or capabilities in response to future-relevant conditions.
- Evidence: [`tools/web_tools.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/web_tools.py); [`tools/__init__.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/__init__.py); [`cli.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/cli.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: web access can materially broaden present-task evidence; S4 requires the additional prospective organizational adaptation closure that is absent here.

### Absence scope

- Surfaces inspected: web-fetch implementation; model/tool loop; plugin loading; provider/model configuration; save/load sessions; todos; repository runtime tree.
- Plausible first-party paths checked: autonomous external monitoring; future-state planning; self-improvement; plugin acquisition/generation; automatic provider/model switching; durable strategic memory; web-triggered capability change.
- Why no material first-party path remains: external information is fetched only on demand as another current-task tool result, and plugins/configuration are supplied by the operator. No standard runtime actor autonomously changes Aero's organizational capability/strategy from future/environment intelligence.

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy decision function was established at the selected recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. The user/configuration decides model endpoint, iteration/timeout parameters and whether dangerous tools require approval; `/yolo`/`--yolo` changes execution consent, not organizational identity or ultimate policy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: dangerous-tool set; callback approval; auto-approve toggle; CLI/config provider/model settings; system prompt; plugin directory selection.
- Closure path: not applicable; no identity/ultimate-policy matter reaches a legitimate autonomous or parent S5 authority whose returned decision governs subsequent organization operation.
- Why this is / is not agent-owned: the model operates inside authored tool/system constraints and cannot itself redefine the dangerous-tool set, approval ownership or system identity through a first-party governance loop. Human permission for individual/all supported side effects is operational authority rather than demonstrated S5 identity governance.
- Evidence: [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py); [`cli.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/cli.py); [`tools/__init__.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/tools/__init__.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator configuration and approval are meaningful governance/safety surfaces; they do not meet the Profile's identity/ultimate-policy closure threshold merely because the operator has final execution authority.

### Absence scope

- Surfaces inspected: system prompt; dangerous-tool policy; callback approval semantics; auto-approve toggle; config/model/provider controls; plugin loading; slash commands and conversation state.
- Plausible first-party paths checked: autonomous policy revision; parent-governed identity decision; purpose/constitutional update; approval escalation; plugin/config governance; model/provider choice as strategic identity.
- Why no material first-party path remains: the standard distribution exposes externally authored configuration and operational consent but no identity/ultimate-policy decision-and-return loop at the assessed recursion.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one Aero model/tool conversation acting on one project task. Tools/plugins/todo state are subordinate capabilities of that S1, while externally run Aero instances are separate organizations unless another system composes them.
- Variety: source/project state, tool results, web evidence, task ambiguity, execution failures and implementation alternatives are handled mainly by the S1 actor plus approval and iteration safeguards.
- Escalation: dangerous tool calls may be escalated to the user for approval; denial is returned as a tool result and can change the same actor's next action. This operational escalation does not establish S3/S5 because the disputed matter is the concrete side effect rather than whole-current management or ultimate policy.
- Unresolved evidence: no material evidence gap remained that required `?` at the frozen revision. Generic user-authored plugin possibilities were not used to infer unshipped organizational functions.

## Assessment vector

**`A · — · — · — · — · —`**
