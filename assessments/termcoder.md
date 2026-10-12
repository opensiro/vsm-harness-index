---
harness_id: termcoder
project_name: Termcoder
repository: https://github.com/nattergabriel/termcoder
review_ref: c642c36e8d65ca42a8ae05172c527f73cb2017d7
reviewed_at: 2026-10-12
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

# Termcoder

## Review boundary

- System in focus: first-party installed `termcoder` Python coding agent, comprising the per-conversation `Agent` loop, integrated coding tools and permissions, configuration, providers, project instructions/skills, and one active user-interface channel (terminal or optional Telegram).
- Purpose and identity: let a user ask for coding work on a local project and have a model iteratively inspect, search, edit, move/delete, or execute shell operations with concrete observed outputs and appropriate tool permission.
- Relevant environment: local working directory/filesystem, user terminal or authorized Telegram chat, externally provided model APIs/credentials, user/project TOML configuration and discovered Agent Skills.
- Standard-distribution boundary: packaged Python `termcoder` application instantiated by `termcoder.app.build`, its single active provider/tool/permission loop, terminal/Telegram channel, local skill discoverer and slash commands; not a fleet of separately launched sessions or unrelated downstream Telegram services.
- Credited operating / distribution surfaces: [README](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/README.md); [pyproject](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/pyproject.toml); [app composition](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py); [agent loop](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py); [message state](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/state.py); [prompt](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/prompt.py); [terminal channel](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/channels/terminal.py); [Telegram channel](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/channels/telegram.py); [permission policies](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/permissions.py); [configuration](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/config.py); [built-in tools](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/builtins.py); [Bash tool](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/bash.py); [edit tool](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/edit.py); [skills catalog](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/skills/catalog.py); [integration loop tests](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/tests/integration/test_full_loop.py).
- Adjacent first-party surfaces excluded from ownership: CI, developer tests/fake provider, root `AGENTS.md` maintainer notes and project governance as distinct actors; external model/provider APIs and Telegram Bot service; arbitrary user-authored skill content or manually composed multiple agent installations.
- First-party operating / deployment modes considered: default terminal interactive session, alternate Telegram channel using the same loop, `ask_each`, `allow_readonly`, `allow_all` permission modes, selected provider/model, configured instructions/skills, and per-turn cancellation/error rollback.
- Recursion level: one `Agent` instance/conversation serving one user channel. Multiple tool calls are serially dispatched within that one operative, and the alternate channel is a transport choice, not a distinct S1 business unit.
- Reviewed revision: `c642c36e8d65ca42a8ae05172c527f73cb2017d7`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[Agent.run_turn](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py) appends a user message to in-memory state, streams model text/tool-call requests from an injected provider, collects tool calls, records the model's result, then serially dispatches each tool after consulting a permission callback. It appends actual `ToolResult` messages before the next provider round, ending when the model emits no tool requests. A configurable iteration cap prevents unbounded rounds; exceptions roll back the partial turn state. [app.build](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py) instantiates one provider, built-in tool registry, discovered skills, `Agent`, permission policy and slash-command registry. [builtin_tools](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/builtins.py) supplies read/write/edit/bash/search/list/move/delete; bash runs child shell commands with timeout/output limits in [Bash.run](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/bash.py).

[permissions.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/permissions.py) distinguishes user approval for every non-whitelisted tool, read-only bypass, or `allow_all`, with actual interactive approval delegated to the channel. [configuration](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/config.py) loads user and project TOML layers and environment-provided secrets. [TerminalChannel](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/channels/terminal.py) and [TelegramChannel](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/channels/telegram.py) are user-facing alternatives around the **same agent loop**, not separately controlled task workers. The Telegram adapter queues incoming user messages and resolves per-command authorization by receiving replies in the active chat. The local [SkillCatalog](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/skills/catalog.py) deterministically discovers skill documents and optionally supplies their content to the operative model. These are execution aids or user-selected configuration, not new VSM managerial actors.

## Operational model

An agent-owned, present-task coding loop regulates uncertainty through model-selected tool action and observed results. The software's operational unit is one coding conversation. Tool dispatch is sequential; a Telegram chat is a communication endpoint for the same `Agent`, not a concurrently autonomous S1. The human supplies goals, permission decisions, model/channel choices and optional skill instructions; no independently closed multisystem coordination, whole-current managerial authority, complementary audit, future adaptation or identity governance is wired into the shipped application.

## S1 — Operations

- State: A
- Function: carry out uncertain coding/developer tasks through chosen code-inspection, search, editing and shell operations informed by real tool feedback.
- Disturbance / variety regulated: unknown project structure, unavailable files, code defects, command failure, unexpected results and subsequent needed steps.
- Decisive decision or feedback right: model chooses a sequence of typed tools and the follow-up or terminal response based on previous tool outputs.
- Decision owner: model-driven first-party `Agent.run_turn` workflow. Provider supplies model inference but the installed app binds tools, executes actions and supplies feedback.
- Supporting / enforcement mechanisms: `Registry`, provider adapter, `State`, tool implementations, permission callbacks, channel UI, config/skills, iteration cap and rollback.
- Closure path: user task → model tool request → permission decision → real registered tool execution → `ToolResult` appended as model context → model chooses next action or completes turn.
- Boundary reachability: `app.build` supplies the native registry/provider/permission callback to `Agent`, and the supported terminal/Telegram modes run that same first-party loop.
- Why this is / is not agent-owned: removing model choice leaves a deterministic tool list and permission prompts but no context-sensitive coding plan, inspection or completion decision.
- Evidence: [agent loop](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py); [app composition](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py); [tools](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/builtins.py); [integration tests](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/tests/integration/test_full_loop.py).
- Basis: structural and explicit.
- Confidence: high for implementation-defined tool feedback; live provider-backed task not reproduced.
- Caveats: mutating calls remain subject to human permission, and external providers remain dependencies.

## S2 — Coordination

- State: —
- Function: no autonomous or constructor-owned first-party regulation of specific interference/oscillation between **distinct operating S1 units** is evidenced.
- Disturbance / variety regulated: multiple tool calls and incoming prompts are handled within one agent's own sequence, rather than competing independently goal-directed agent workers.
- Decisive decision or feedback right: serial `_dispatch_all` runs model-requested tools; UI input queue transports future user messages without conflict arbitration between autonomous S1s.
- Decision owner: model for its own operation, runtime for serial dispatch, channel for input handling; no separate S2 closure.
- Supporting / enforcement mechanisms: tool registry, sequential dispatch, Telegram input queue, slash-command/user channel routing.
- Closure path: result of each tool feeds the same model's next inference. No inter-S1 conflict signal → specific attenuation decision → changed subsequent worker obligations.
- Why this is / is not agent-owned: sequencing one operative's tools or swapping communications channels is not the S2 functional relation.
- Evidence: [loop.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py); [telegram.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/channels/telegram.py); [app.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py).
- Basis: structural.
- Confidence: high within shipped single-agent modes.
- Caveats: independent user-launched termcoder processes could interfere externally without creating native cross-process coordination.

### Absence scope

- Surfaces inspected: agent state/dispatch, tool registry, both channel adapters, permission and application composition.
- Plausible first-party paths checked: distinct concurrent S1 agents, shared resource arbitration, competing obligations, oscillation detection, correction returned to each affected S1.
- Why no material first-party path remains: the supported implementation creates one per-session Agent and serializes tools; no peer population or conflict-specific first-party coordination closure exists.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current management function over a population of operating S1 units with authority over shared resources/commitments is instantiated.
- Disturbance / variety regulated: current task and conversation progress are local to the only S1, not a managed organization's distinct current commitments.
- Decisive decision or feedback right: coding model decides its own tool sequence; channel/user can approve or refuse operations; no whole-system manager allocates resources, changes priority across workers or returns corrected commitments.
- Decision owner: the active coding model, human permissions/configuration and deterministic runtime; no separate S3 owner.
- Supporting / enforcement mechanisms: iteration limit, provider/model commands, task-local message state, approval gate.
- Closure path: task feedback and user guidance directly return to the operative model; no distinct whole-current view → corrective S3 decision → multiple S1 adjustment.
- Why this is / is not agent-owned: present coding-task management is S1 even when the model can change models or adjust its next action.
- Evidence: [app.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py); [loop.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py); [model command](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/commands/model.py); [config](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/config.py).
- Basis: structural.
- Confidence: high for standard application boundary.
- Caveats: external human operating several instances is not first-party returned S3 governance.

### Absence scope

- Surfaces inspected: app wiring, core agent loop, channel controls, state, slash commands and configuration.
- Plausible first-party paths checked: whole-system status/worker commitments, real S3 discretionary control, operator/parent S3 decision with consequential return, shared resource management.
- Why no material first-party path remains: no current-workforce coordinator or managerial return path is wired into the single-agent runtime.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent reality-sampling auditor emits a separate judgment and closes a feedback path into S3 management.
- Disturbance / variety regulated: tool/test failures can be seen by the active coding model and tests can be run as tools, but these are ordinary execution feedback rather than independent operational auditing.
- Decisive decision or feedback right: model may invoke tests/shell or view error messages; repo integration tests run by external developers/CI. None constitutes a first-party independent audit decision and management return.
- Decision owner: operative coding model for tool-followup, developer/CI for separate quality tests; no S3* audit owner in the deployed agent.
- Supporting / enforcement mechanisms: shell result, tool error marker, iterative model reasoning, developer tests.
- Closure path: failed tool or test output → same agent's subsequent action; no independent complementary auditor → managerial owner → binding corrective instruction.
- Why this is / is not agent-owned: routine self-verification and off-runtime test suites do not establish the S3* function.
- Evidence: [loop.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/loop.py); [Bash tool](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/tools/bash.py); [loop test](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/tests/integration/test_full_loop.py); [development CI](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/.github/workflows/ci.yml).
- Basis: structural.
- Confidence: medium-high.
- Caveats: human review or a downstream plugin could introduce an audit, but no such shipped ownership loop was found.

### Absence scope

- Surfaces inspected: active model/tool loop, registry, error paths, channel feedback and test/CI surfaces.
- Plausible first-party paths checked: separately commissioned auditor, independent direct observation, corrective audit judgment, return to current-control authority.
- Why no material first-party path remains: the default application contains one coding agent and ordinary developer testing, without an independent S3* controller connected to operational management.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party closed future/environment-sensing adaptation function is shipped to alter sustained organizational capability.
- Disturbance / variety regulated: changing provider/models and source content may influence today's coding task; there is no prospective adaptation program.
- Decisive decision or feedback right: user selects/configures provider, model and skills; a model may adapt local tactics after tool feedback, not authorize a future-oriented change in organizational capability.
- Decision owner: user/developer for configuration and skill provision, current task model for immediate work.
- Supporting / enforcement mechanisms: provider registry, slash commands, global/project config, discovered Agent Skills and project instructions.
- Closure path: user changes settings → next local session/tool choices; no distinct outside/future observation → capability proposal → S4 decision → returned organizational adaptation.
- Why this is / is not agent-owned: task-local reasoning, model switching and skill activation are not substantive external-and-prospective S4 by themselves.
- Evidence: [config.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/config.py); [app.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py); [SkillCatalog](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/skills/catalog.py); [provider command](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/commands/provider.py).
- Basis: structural.
- Confidence: high on bounded standard modes.
- Caveats: custom extensions might implement a separate adaptation function, not attributed to standard distribution.

### Absence scope

- Surfaces inspected: configuration, provider commands, skills/instructions, application initialization and agent model loop.
- Plausible first-party paths checked: external monitoring of changing options, prospective selection of a new capability, authorized returned implementation into subsequent operation.
- Why no material first-party path remains: the identified path is manually configured tool/provider selection plus current-task operation, not an autonomous or parent-governed S4 adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party legitimate ultimate-policy or continuing-identity arbitration loop at the agent-organization boundary.
- Disturbance / variety regulated: permission postures, project instructions and credentials govern local tool execution, not organization identity.
- Decisive decision or feedback right: human approval and static policy choose whether particular tool calls are allowed. No S5 identity decision is made and returned as binding whole-system governance.
- Decision owner: user/configuration for permissions, deterministic runtime for enforcement; no S5 decisive owner.
- Supporting / enforcement mechanisms: `ask_each`, `allow_readonly`, `allow_all`, project/user config and tool metadata.
- Closure path: user/local config → permission callback → tool allowed/denied. No legitimate ultimate authority receives an S5 issue and returns an organizational identity-level decision.
- Why this is / is not agent-owned: a permission gate or a system prompt cannot be credited as ultimate policy/identity decision ownership without the function-specific closure.
- Evidence: [permissions.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/permissions.py); [config.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/config.py); [app.py](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/app.py); [prompt](https://github.com/nattergabriel/termcoder/blob/c642c36e8d65ca42a8ae05172c527f73cb2017d7/src/termcoder/agent/prompt.py).
- Basis: structural.
- Confidence: high within shipped modes.
- Caveats: project maintainer governance occurs outside the packaged agent's operational recursion.

### Absence scope

- Surfaces inspected: permissions, tool registry, prompt and config, user/channels, project README and developer/test/governance contexts.
- Plausible first-party paths checked: ultimate identity/policy disputes, agent-owned S5 right, eligible parent-owned S5 authority and return into operation.
- Why no material first-party path remains: available controls regulate individual tools and user-selected settings without organization-level identity-policy adjudication or returned closure.

## Recursion

The system implements one S1 coding session. Switching its front-end from terminal to Telegram does not create an additional independent operational S1. Tool calls, chat channels and locally discovered skill instructions do not supply nested viable-system recursion.

## Variety and escalation

The model absorbs present-task variability by acting on tool feedback and either continuing or finishing. Unknown tool calls and denied permissions produce in-band error results; a max-iteration exhaustion raises a bounded error and failed turns roll back. Human approval can authorize/reject individual actions. No distinct exceptional algedonic signal path to an autonomous organizational manager is evidenced.

## Evidence gaps

- Static source and integration-test review at the fixed Git SHA; no provider-backed coding run executed by this reviewer.
- The local state is an in-memory message log; do not credit absent long-lived organization knowledge or runtime management just because project-level configuration or skills persist as files.
- Negatives are confined to the shipped first-party `termcoder` application and its documented modes; independent external orchestrators or users operating fleets are outside the boundary.
