---
harness_id: open-agent-sdk-python
project_name: Open Agent SDK Python
repository: https://github.com/codeany-ai/open-agent-sdk-python
review_ref: ab068156bf7db79cd23a883e8264a12803e23966
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Open Agent SDK Python

## Review boundary

- System in focus: One first-party `open_agent_sdk.Agent` instance, its `QueryEngine` and installed tool/provider adapters, processing user prompts across retained conversation turns. The examined `agents` option, team/task tools and inter-agent mailboxes are assessed for actual runtime wiring, not accepted as separate S1 units because of their names.
- Purpose and identity: An embeddable Python model/tool execution SDK with multi-turn messages, filesystem/web/MCP actions, optional caller permissions, session persistence and budget/turn caps.
- Relevant environment: User prompts, model decisions, tool outputs/errors, provider failures, filesystem changes, MCP tools, context pressure and application-supplied policies.
- Standard-distribution boundary: Installed Python package invoked through public `query()` / `create_agent()` / `Agent.query()` with a configured provider and tool pool; standard code implements the agent loop in-process.
- Credited operating / distribution surfaces: [Agent API](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py), [QueryEngine](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [tool registry](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/__init__.py), [session storage](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/session.py), [provider interface](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/providers/factory.py).
- Adjacent first-party surfaces excluded from ownership: `examples/` and `examples/web/` sample applications, `tests/`, PyPI/release/CI, neighboring TypeScript/Go SDKs and upstream maintainer decisions. The sample `agents` declaration and available hook classes are not assumed to be wired into runtime merely because they appear in docs.
- First-party operating / deployment modes considered: A one-shot SDK query, reusable multi-turn `Agent`, optional persisted/forked session, allow-/deny-filtered tool pool, optional `can_use_tool` callback, optional MCP connections and model provider switching. The advertised subagent/team mode was traced through the actual dispatcher.
- Recursion level: The installed agent loop within one application process. Tool actions, task records, synthetic mailbox entries and independent application-created agents do not by themselves establish a viable multi-agent organization at this level.
- Reviewed revision: `codeany-ai/open-agent-sdk-python@ab068156bf7db79cd23a883e8264a12803e23966` (pinned source checkout).
- Observation date: 2026-11-10; pinned source/docs inspection, no paid-model execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

`Agent._initialize()` builds tools and optional MCP connections, may load a saved session, then `Agent.query()` creates a `QueryEngine` and passes it the prior conversation. `QueryEngine.submit_message()` constructs model requests, records response blocks, executes model-selected tools, feeds tool results back, compacts large histories, estimates cost and ends at a final answer or configured limit. Read-only/concurrency-safe tools run in bounded `asyncio.gather` batches; other tools run serially. [`agent.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py), [`engine.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py).

Several declared features have narrower first-party closure than their README labels: `AgentTool.call()` returns an error saying an engine subagent handler must execute it, but `_execute_single_tool()` only calls `tool.call()` and contains no subagent dispatch; `AgentOptions.agents` is not passed into `QueryEngineConfig`. The in-memory team/task/message tools store names, records and mailboxes without running separate agents. `Agent.set_permission_mode()` changes an option not consumed by engine permission checks; an explicitly configured `can_use_tool` callback and tool-list filtering **are** wired. `Agent.interrupt()` is a no-op. [`agent_tool.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/agent_tool.py), [`tools/__init__.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/__init__.py), [`agent.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py).

## Operational model

A model chooses the next local tool calls and answer from the returned observations. The Python SDK owns loop scheduling, context/usage bookkeeping and deterministic guardrails; the embedding application chooses tools, endpoint, budgets and any permission callback. It does not ship an operating supervisor that decides among multiple independently deployed task agents. Examples and upstream organization processes remain outside this operational ownership boundary.

## S1 — Operations

- State: A
- Function: Execute one task through iterated model-selected tools and observations until completion or bounded failure.
- Disturbance / variety regulated: New user tasks, provider replies, tool errors, changing files/web data and multi-turn feedback.
- Decisive decision or feedback right: Select a tool and its arguments, revise the approach after observations and choose final response content.
- Decision owner: Model-backed actor operating inside `QueryEngine`; developer-installed tool restrictions and deterministic execution remain surrounding constraints.
- Supporting / enforcement mechanisms: `submit_message`, `_call_api`, `_execute_tools`, tool result feedback, provider adapters, message normalization, retries, context compaction, turn and budget limits.
- Closure path: User prompt → model response → first-party permission-checked tool execution → returned result/error → next model turn or final answer.
- Boundary reachability: Public `Agent.query()` constructs the in-process engine with the installed tool pool and provider, and `submit_message()` actually calls `_execute_tools()` and appends resulting observations; no adjacent demo controller is needed.
- Why this is / is not agent-owned: The model selects the substantive operational next step; serial/concurrent dispatch and caps determine how selected actions are enforced, not which task action to choose.
- Evidence: [`agent.py` query path](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py), [`engine.py` model/tool loop](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [README quickstart](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/README.md).
- Basis: Structural implemented model/tool loop.
- Confidence: High in source-reachable ownership; not a live-provider reliability claim.
- Caveats: Needs a functioning external model/provider and relevant tools; budget/turn limits can halt work before task completion.

## S2 — Coordination

- State: —
- Function: Would attenuate conflicting demands or oscillation among distinct operational S1 agents and feed the decision back into their work.
- Disturbance / variety regulated: Potential shared-file collisions, inconsistent commitments or competition among agents, not parallel reads within one agent turn.
- Decisive decision or feedback right: No shipped, reachable inter-S1 conflict-specific decision owner or attenuation rule.
- Decision owner: One model owns its own loop; application authors would have to instantiate distinct agents and supply operational coordination.
- Supporting / enforcement mechanisms: Read-only tool batching, mutation serialization, task/team in-memory registries, `SendMessage` mailbox, advertised but unimplemented `AgentTool` subagent handler.
- Closure path: The scheduler prevents some within-turn tool collisions; mailbox writes have no connected distinct running-agent receiver/feedback cycle. `AgentTool` returns an error rather than executing a delegated S1.
- Why this is / is not agent-owned: Tool sequencing and generic message storage are not evidence of a specific S2 relation between autonomous operational units.
- Evidence: [`engine.py` dispatcher](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [`agent_tool.py` placeholder](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/agent_tool.py), [`send_message.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/send_message.py).
- Basis: Structural bounded absence at shipped runtime boundary.
- Confidence: High, including concrete stub/dispatch mismatch.
- Caveats: A separate application can compose multiple SDK agents and implement S2; such an application was not included.

### Absence scope

- Surfaces inspected: `QueryEngine`, `AgentOptions.agents`, `AgentTool`, task/team tools, mailbox API, tool scheduler and sample subagent usage.
- Plausible first-party paths checked: Real subagent execution, competing S1 identification, collision attenuation, inter-agent feedback and dynamically accepted joint commitments.
- Why no material first-party path remains: The built-in subagent entry is a stub not intercepted by engine, while remaining concurrency and messaging paths do not close a distinct inter-S1 conflict-resolution cycle.

## S3 — Inside-and-now control

- State: —
- Function: Would oversee actual commitments, priorities, capacity and intervention across a whole of operational units.
- Disturbance / variety regulated: Competing resource demands and cross-agent live-portfolio deviations rather than one-loop token/cost usage.
- Decisive decision or feedback right: No whole-system current-control actor with discretion to reallocate commitments or arbitrate operational units.
- Decision owner: Caller sets limits and tool access; runtime enforces them deterministically. The model directs its own S1 actions.
- Supporting / enforcement mechanisms: `max_turns`, `max_budget_usd`, token usage, tool allowlist/denylist, optional `can_use_tool` callback, sequential mutations and task metadata.
- Closure path: A budget violation ends the single run and an optional callback permits/denies one tool; neither decides current inter-unit commitments from a common whole-system view.
- Why this is / is not agent-owned: The budget and permission branches enforce configured constraints; no agent or legitimate parent is supplied a whole-organization current resource/commitment judgment loop.
- Evidence: [`engine.py` budget and permission branches](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [`agent.py` options wiring](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py).
- Basis: Structural bounded absence.
- Confidence: High for the standard one-agent distribution.
- Caveats: An embedding application may provide supervising humans or institutional capacity decisions; no first-party returned parent S3 mode was found.

### Absence scope

- Surfaces inspected: Query/budget lifecycle, tool permissions, task/team stores, `Agent` options, session persistence and exposed operator methods.
- Plausible first-party paths checked: Multi-S1 status aggregation, current whole-system choice among resource/priority commitments, parent intervention and returned altered operations.
- Why no material first-party path remains: Limits and callback checks act at an individual action/run boundary and task stores do not acquire whole-system current-control judgment or return authority.

## S3* — Complementary audit

- State: —
- Function: Would independently inspect primary operations against an alternate evidence path, challenge success claims and return actionable findings.
- Disturbance / variety regulated: Incorrect completion reports, missed tool failures and unobserved task deviations that routine self-report may conceal.
- Decisive decision or feedback right: No first-party independent outcome-evaluation or audit-verdict authority is supplied.
- Decision owner: Producing engine generates usage/results; external evaluator would have to be added by the host application.
- Supporting / enforcement mechanisms: Streaming tool/result events, persisted transcripts, usage/cost reports, hook registry definitions and tests.
- Closure path: A caller can observe or save the normal producer trace, but no independent evidence acquisition → challenge → returned corrective decision path is packaged.
- Why this is / is not agent-owned: Model/tool trace and telemetry are ordinary operational reporting; hooks are not wired as a standing independent audit actor in the query engine.
- Evidence: [`engine.py` result/event generation](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [`hooks.py` registry](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/hooks.py), [`session.py`](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/session.py).
- Basis: Structural bounded absence.
- Confidence: High at the installed package boundary.
- Caveats: Logged observations could be inputs to a separate audit, but are not themselves one.

### Absence scope

- Surfaces inspected: Events/results, transcripts, lifecycle hook registry and its runtime wiring, tests, task output tool and provider feedback.
- Plausible first-party paths checked: Independent replay, direct artifact inspection, audit-specific truth tests, separate verdict owner and returned operations correction.
- Why no material first-party path remains: The observed first-party output comes from the same execution path; no reachable independent audit judgment and control return was established.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would sense future/external changes, evaluate new capability options and return a selected adaptation into current operation.
- Disturbance / variety regulated: Evolving technologies, external demand, opportunities and threats beyond the present user's task.
- Decisive decision or feedback right: No shipped actor or constructor path decides enduring future-oriented capability changes from independent external sensing.
- Decision owner: Developers change models, instructions, tools and integration configuration; the running model chooses immediate actions within that setup.
- Supporting / enforcement mechanisms: Web search/fetch tools, provider switching, skill registry, auto-compaction, sessions and model-selected current research.
- Closure path: A model can read the web to answer a present task and a caller can later reconfigure an agent, but neither mechanism provides a standing outside/then → adaptation judgment → changed capability return.
- Why this is / is not agent-owned: Immediate research is S1 operation unless the installed system closes a distinct prospective organizational adaptation decision.
- Evidence: [`agent.py` provider/model and tools setup](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py), [`engine.py` task loop](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py), [skill tool](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/tools/skill_tool.py).
- Basis: Structural bounded absence.
- Confidence: Medium-high.
- Caveats: Caller-supplied custom tools may implement prospective adaptation but are not part of this standard distribution evidence.

### Absence scope

- Surfaces inspected: Core loop, web tools, skill registry, provider configuration, sessions, task planning and examples.
- Plausible first-party paths checked: Autonomous environment scanning, separate prospective interpretation, adaptation alternatives, decision authority, persistent capability update and return to current control.
- Why no material first-party path remains: Present-task tools and external developer configuration offer extension points without a first-party standing prospective decision and returned operational change.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate legitimate ultimate identity/policy questions and return authoritative rules to govern subsequent operation.
- Disturbance / variety regulated: Conflict about mission, ultimate constraints and legitimate authority, not per-tool allow/deny checks alone.
- Decisive decision or feedback right: No installed ultimate-policy adjudicator or parent-return cycle; embedding author supplies system prompt, tools and callback.
- Decision owner: External developer/operator chooses setup, not a first-party legitimate agent/parent S5 decision process at this boundary.
- Supporting / enforcement mechanisms: System prompts, tool filtering, optional `can_use_tool`, `permission_mode` option, session metadata and public API setters.
- Closure path: A caller can reconfigure tools or instructions, and the engine can refuse a callback-denied action; there is no identity/policy matter → legitimate authority resolution → authoritative returned rule process.
- Why this is / is not agent-owned: The model's task decisions occur within externally provided boundaries; `permission_mode` is not forwarded to the executing engine and is not evidence of constitutional policy ownership.
- Evidence: [`AgentOptions` configuration](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/types.py), [`agent.py` configuration wiring](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/agent.py), [`engine.py` permission callback](https://github.com/codeany-ai/open-agent-sdk-python/blob/ab068156bf7db79cd23a883e8264a12803e23966/src/open_agent_sdk/engine.py).
- Basis: Structural bounded absence.
- Confidence: High for the installed single-agent boundary.
- Caveats: A developer's external policy governance may be legitimate for its own organization; such governance is not included as first-party S5 parent mode here.

### Absence scope

- Surfaces inspected: System-prompt setup, tool filtering, `can_use_tool`, `permission_mode`, `set_permission_mode`, hooks, API options and runtime continuation.
- Plausible first-party paths checked: Identity dispute intake, legitimate ultimate-policy authority, adjudication, durable policy revision and returned effect on later execution.
- Why no material first-party path remains: Only external setup and per-tool constraint enforcement are wired; neither constitutes a first-party authoritative ultimate-policy closure.

## Distributed OSS parent arrangement

Repository maintainers govern SDK development/releases, not a deployed consumer's `Agent` session. Different applications install and run copies independently; no common project-level parent decisions return as first-party operation of all such agents. A developer owning one installation is not automatically a parent S3/S4/S5 function.

## Self-hosted and non-human modes

The library runs in-process and can use caller-selected local/remote providers. Its model/tool loop remains S1=A in the supported configuration; optional approvals, transcript persistence and provider changes do not add independently closed organizational metasystems. Advertised subagent execution is unimplemented in the inspected dispatcher, so no all-agent S2/S3 mode is credited.

## Recursion

Tools are operational actions of a single agent, not independent viable units. In-memory tasks/mailboxes do not instantiate operating S1s; an application author could construct a higher-recursion fleet, but the application would require its own review boundary and evidence.

## Variety and escalation

Model responses attenuate task variety via iterated observations; deterministic tool batching, mutation serialization, retry, context compaction, budget and turns delimit resource/error variety. Tool errors return to the same producing loop. External callback approvals can block calls, but no documented organization-wide escalation or ultimate-policy parent return is reachable in the SDK itself.

## Evidence gaps

- Static pinned-code review only; no live paid-provider execution, deployment reliability assessment or external consumer evaluation.
- The README lists subagents, permissions, hooks and interruption more broadly than reachable code demonstrates; conclusions use the actual `Agent` → `QueryEngine` → tool dispatcher, not feature names.
- Optional caller-created policies, external orchestrators or additional SDK languages may implement higher-recursion VSM functions but are not credited to this Python package.
