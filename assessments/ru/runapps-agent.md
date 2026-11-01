---
harness_id: runapps-agent
project_name: RunApps Agent
repository: https://github.com/runapps/agent
review_ref: ccbe5ba7b7ea7d8f3957e4785b47341decbd1192
reviewed_at: 2026-11-01
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

# RunApps Agent

## Review boundary

- System in focus: `@runappsai/agent`, the first-party TypeScript agent/tool runtime and its standard Node/browser compositions, not a provider's hidden agent.
- Purpose and identity: a reusable model↔tool execution loop with workspace file operations, sandbox evaluation, skills, sessions and context management.
- Relevant environment: user instructions, model APIs, tools, browser/Node hosts and workspace files.
- Standard-distribution boundary: the exported `Agent` class, its supplied workspace/tools and shipped adapters; the caller instantiates an agent and provides a model endpoint.
- Credited operating / distribution surfaces: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L167-L243), [src/file-tools.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/file-tools.ts#L1-L75), [src/node.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/node.ts), [src/compaction.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/compaction.ts).
- Adjacent first-party surfaces excluded from ownership: example chat UIs, documentation/demo pages, package publish workflow, optional provider implementations and tests; model-provider decisions and user decisions remain external.
- First-party operating / deployment modes considered: SDK-instantiated browser or Node agent with local/custom workspace, interactive tool permission `ask`, and opt-in `auto` permission.
- Recursion level: one instantiated agent and its attached tools/workspace as the operational unit; multiple unrelated Agent instances do not by themselves form an upper-level viable organization.
- Reviewed revision: `ccbe5ba7b7ea7d8f3957e4785b47341decbd1192` (source checkout at exact commit).
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent` builds a tool set from caller-supplied tools plus shipped workspace file tools, `ask_user`, and JavaScript sandbox; attaches provider/UI/workspace, restores session history by ID and saves it after each committed turn ([src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L167-L270)). Its turn loop manages bounded context, issues model completions with tool schemas, accepts assistant tool calls, executes and records result messages, and feeds them to later turns ([src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L535-L685)). Tool execution validates arguments, applies caller hook and permission/confirmation policy, dispatches the selected tool, and records outcome ([src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L925-L1026)). The workspace APIs, read-before-write guard, compaction, history rewind, queue/steer/follow-up and stop/idle guard are operational support, not independent organizational actors. Provider inference, confirmation UI and user instructions remain external.

## Operational model

The S1 outcome is the agent's completion of user-directed tool-assisted work through its own model/tool cycle. Model-driven next action and tool argument choice belong to the agent; workspace guard, permission UI, execution executor, token limits and persistence enforce conditions. No first-party multi-unit operational organization with S2-specific disturbance handling or independent metasystem owner was established in this release. Do not infer higher VSM functions from the existence of a tool-loop budget, session summary, or a user approval.

## S1 — Operations

- State: A
- Function: execute user tasks by iterating model-selected tool calls and incorporating observed results into subsequent action.
- Disturbance / variety regulated: unpredictable user tasks and tool/workspace outputs.
- Decisive decision or feedback right: choose the next tool or answer in response to the latest conversation and tool observations.
- Decision owner: model-driven agent in the shipped `Agent.start` execution loop.
- Supporting / enforcement mechanisms: provider transport, permission hook/UI, file guard, workspace tools, max-turn guard and persistence.
- Closure path: tool outputs append to history and are included in the next completion; final reply or explicit termination ends the run.
- Boundary reachability: `Agent` is exported as the normal SDK runtime and invokes these tools in its actual turn loop, independent of demo-only code.
- Why this is / is not agent-owned: the agent chooses task actions; deterministic validators and human consent only condition their execution.
- Evidence: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L535-L685); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L925-L1026); [src/file-tools.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/file-tools.ts#L28-L75).
- Basis: explicit / structural.
- Confidence: high for the first-party source path; no live provider-backed E2E test claimed.
- Caveats: `permissions: ask` may halt external effects for consent; the permission decision is not the agent's discretion.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 stabilization loop established at this recursion.
- Disturbance / variety regulated: hypothetical conflicts among separate agents, not a witnessed operating condition here.
- Decisive decision or feedback right: none material for inter-S1 oscillation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-agent queues, steering and session/workspace APIs support a single agent's action sequence.
- Closure path: no first-party cross-agent coordination result returned to distinct S1 units.
- Why this is / is not agent-owned: a single loop's queue/serialization is not coordination among independently operating S1 units.
- Evidence: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L167-L243); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L400-L523); [src/types.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/types.ts).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: applications can compose multiple instances, but no S2-specific first-party contract is identified.
### Absence scope

- Surfaces inspected: `Agent` instance and queue logic, workspace/agent options, shipped SDK and Node/browser entry points.
- Plausible first-party paths checked: `followUp`/steer queue, provider dispatch, workspace session storage and tool batching.
- Why no material first-party path remains: these order one agent's work or provide generic APIs, without a concrete interference witness, attenuating relation or returned regulation among separate operational S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control decision owner established beyond the operational unit.
- Disturbance / variety regulated: local token/turn exhaustion and repetitive tools, handled as local execution limits rather than whole-system tradeoffs.
- Decisive decision or feedback right: no allocation of priorities, commitments or resources across an S1 collective.
- Decision owner: not established; caller fixes options and runtime enforces limits.
- Supporting / enforcement mechanisms: `maxTurns`, context budget, loop-progress guard, abort and permission hook.
- Closure path: local run stops/errors/compacts; no whole-system current-control decision returns to multiple units.
- Why this is / is not agent-owned: deterministic stop/compaction is enforcement of preset bounds, not S3 discretion.
- Evidence: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L535-L585); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L645-L685); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L1018-L1027).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: operators may impose budgets, but ordinary per-tool approval is not a proven parent S3 mode.
### Absence scope

- Surfaces inspected: turn loop, options/configuration, context policy, session/queue and tool approval.
- Plausible first-party paths checked: turn/usage guard, idle-loop detection, permission hooks and external caller controls.
- Why no material first-party path remains: each governs one agent run or carries external constraints, not a first-party current-control owner of the declared whole.

## S3* — Complementary audit

- State: —
- Function: no separate complementary direct-evidence challenge to ordinary S1 reporting established.
- Disturbance / variety regulated: potential false operational claims, without a shipped independent audit closure.
- Decisive decision or feedback right: none exposed for an independent audit judgment.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tool-result validation and file guards check ordinary execution integrity.
- Closure path: tool results are incorporated in the same agent loop, not independent challenge findings returned to control.
- Why this is / is not agent-owned: ordinary tool errors, validation and transcript visibility are in-band operational feedback.
- Evidence: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L925-L1026); [src/file-tools.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/file-tools.ts#L28-L75); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L610-L670).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a caller could provide an auditor, but generic tool extensibility does not ship audit ownership.
### Absence scope

- Surfaces inspected: model/tool execution, event hooks, file guard, tool outcome handling and standard SDK modules.
- Plausible first-party paths checked: tool schema validation, read-before-write guard, log/events, provider retry.
- Why no material first-party path remains: no separate auditor with complementary evidence access, independent judgment and corrective return is wired into the standard runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally/prospectively oriented adaptation decision and return into present capability established.
- Disturbance / variety regulated: context-window pressure is operational state, not future environmental change.
- Decisive decision or feedback right: none evidenced for prospective capability adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: context compaction summarises past dialogue and preserves recent turns.
- Closure path: summary re-enters the same session, without an adaptation option or S3 capability decision.
- Why this is / is not agent-owned: continuity of one conversation is not the outside-and-then S4 function.
- Evidence: [src/compaction.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/compaction.ts#L1-L120); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L770-L844).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: extensibility permits caller-authored adaptations, excluded absent a shipped function-specific loop.
### Absence scope

- Surfaces inspected: compaction, context, skills, session persistence and agent task loop.
- Plausible first-party paths checked: history summaries, skill discovery, model options and runtime reconfiguration.
- Why no material first-party path remains: these support task context/implementation options, not external future sensing → adaptation option → changed present capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy dispute and authoritative-return path at the agent-system recursion.
- Disturbance / variety regulated: tool safety and user preferences are local execution constraints.
- Decisive decision or feedback right: ultimate identity policy remains with the caller/operator; no S5-specific parent return path is shipped.
- Decision owner: not established at this boundary.
- Supporting / enforcement mechanisms: system prompt, tool confirmation UI, `onToolCall` hook and permissions setting.
- Closure path: permission allows/denies a tool operation, not a returned legitimate identity-level decision shaping future operation.
- Why this is / is not agent-owned: a caller-provided prompt/policy and operation consent are not S5 just by being authoritative for one call.
- Evidence: [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L203-L243); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L977-L1026); [src/agent.ts](https://github.com/runapps/agent/blob/ccbe5ba7b7ea7d8f3957e4785b47341decbd1192/src/agent.ts#L331-L347).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a host application may implement governance outside this distribution.
### Absence scope

- Surfaces inspected: system/permissions configuration, tool approvals, session life cycle, SDK surfaces and documentation.
- Plausible first-party paths checked: agent instruction construction, permission/approval callback, human `ask_user` and runtime settings.
- Why no material first-party path remains: no identity-policy issue is routed to a legitimate internal/parent ultimate authority and returned to govern the system's subsequent policy; these paths govern ordinary tasks/tool calls.

## Distributed OSS parent arrangement

No organization-level S3/S4/S5 parent ownership is inferred from public contributors or release processes. They are adjacent to a deployed SDK instance rather than its operating parent loop.

## Self-hosted and non-human modes

Node/browser SDK use supports caller-defined tools/permissions but does not by itself instantiate a parent S3/S4/S5 closure mode; no independent multi-agent non-human metasystem is shipped here.

## Recursion

A host could compose multiple `Agent` objects as lower-level S1 units; no such upper organization is graded without concrete first-party coordination/control wiring. This record grades one supported instantiated runtime.

## Variety and escalation

Agent-model output and tool observations provide local variety-handling. The runtime can ask the user, request tool consent, truncate/compact context, stop on time/turn limits and surface errors. Those are operational fallback paths, not a VSM algedonic signal or metasystem function by name.

## Evidence gaps

No live paid/model-provider E2E execution was performed. Source inspection supports the bounded absence conclusions at this published SDK boundary, not global claims about every application built with the library.
