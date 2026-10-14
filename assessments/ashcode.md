---
harness_id: ashcode
project_name: AshCode
repository: https://github.com/AuthRan/AshCode
review_ref: 74f30ddac455175d4a18cb105a00ae1bde42cd69
reviewed_at: 2026-10-11
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

# AshCode

## Review boundary

- System in focus: the shipped AshCode Python terminal coding agent, including its first-party asynchronous Agent/Session, model/tool loop, typed-event CLI consumer, tool registry, bounded subagent execution, configured approval and hooks, context management and persistence.
- Purpose and identity: perform user-directed coding and codebase investigation by iteratively selecting first-party source/shell/search tools and applying resulting observations to later turns.
- Relevant environment: user-specified working directory, local shell and file system, user/operator, OpenAI-compatible inference provider, optional user-defined MCP tools and configured hooks.
- Standard-distribution boundary: installed `ashcode` CLI and source `main.py` with interactive/single-prompt modes; root `Agent.run`, bundled tools and default registered read-only investigator/reviewer subagents at the frozen SHA. Optional shipped hook and MCP integration is considered as integration/support, without borrowing decisions from external user scripts or servers.
- Credited operating / distribution surfaces: [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L22-L121), [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L12-L176), [agent/session.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/session.py#L18-L86), [tools/registry.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/registry.py#L14-L138), [tools/subagents.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/subagents.py#L9-L156), [safety/approval.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/safety/approval.py#L92-L162), [context/manager.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/context/manager.py#L43-L216), [hooks/hook_system.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/hooks/hook_system.py#L12-L144), [config/config.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/config/config.py#L54-L105).
- Adjacent first-party surfaces excluded from ownership: [tests/test_approval.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tests/test_approval.py), [tests/test_streaming_tool_calls.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tests/test_streaming_tool_calls.py), [.github/workflows/ci.yml](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/.github/workflows/ci.yml), packaging and developer examples in [pypi/pyproject.toml](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/pypi/pyproject.toml) and [scripts/test_tool.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/scripts/test_tool.py); these corroborate behavior but do not add runtime S3* audit or governance rights.
- First-party operating / deployment modes considered: non-interactive `ashcode <prompt>`; interactive TUI with optional user confirmations and `/approval` / `/model`; configured custom tools, MCP and lifecycle hooks; nested investigator and reviewer subagent tool calls. These are modes of the same terminal agent, not additional autonomous organizations by default.
- Recursion level: one locally operated AshCode coding session with short-lived task-scoped subagents as candidate lower-level S1 units, not an assumed viable cross-session organization or developer team.
- Reviewed revision: `74f30ddac455175d4a18cb105a00ae1bde42cd69`.
- Observation date: 2026-10-11 (repository source, not a production trace).
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI consumes typed events from `Agent.run`. The `Agent._agentic_loop` calls the configured model with a current tool schema, collects model-selected tool calls, invokes each via `ToolRegistry.invoke` and appends concrete tool results to the next model message. A `Session` constructs tools, MCP manager, user-memory read, chat compactor, loop detector, approval manager and hooks. Filesystem/shell/network tools operate in the selected working directory; model reasoning comes from the external provider, but AshCode owns the iteration, dispatch and tool feedback. Context compaction, pruning, persistence and saved CLI checkpoints protect continuity. [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L22-L166); [agent/session.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/session.py#L18-L86); [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L125-L166); [README.md](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/README.md#L72-L147).

Built-in subagent tools are registered in the same registry. A tool invocation creates a new `Agent` with an allowlist/turn budget, consumes events under `asyncio.wait_for` and returns text/error to its parent as a tool result. `codebase_investigator` and `code_reviewer` use scoped read-only tool sets. The parent loop awaits each tool invocation in an ordinary `for tool_call in tool_calls` loop, so the shipped orchestration does not by itself establish simultaneous inter-unit resource conflict or a supervisory policy owner. [tools/registry.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/registry.py#L90-L143); [tools/subagents.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/subagents.py#L25-L156); [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L113-L151).

Approval rules are configurable by an operator. `ToolRegistry.invoke` collects tool confirmation and consults `ApprovalManager`; user confirmation may allow or reject a dangerous or non-whitelisted request. Configured before/after hooks execute user-supplied commands; errors in a hook are printed, and hooks are disabled by default. They do not amount to a shipped independent auditor's judgment. [safety/approval.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/safety/approval.py#L92-L162); [hooks/hook_system.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/hooks/hook_system.py#L12-L143); [config/config.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/config/config.py#L86-L106).

## Operational model

The root coding agent has an S1 operating loop: select an action against code/user request, invoke a tool, observe result and decide next action. If invoked, child `Agent` instances do bounded investigation or code review with their own local model/tool choices, but their results enter the parent's next task-oriented tool observation. The operator sets task, inference endpoint, tool access and approval policy. Deterministic runtime machinery enforces turn limits, allowlists, confirmations, timeouts and context limits. Removing the root model's discretionary tool choice leaves a registry and gates without the coding task decisions; removing an imagined autonomous S2/S3/S3*/S4/S5 manager leaves essentially the same shipped coordination and policy behaviors.

## S1 — Operations

- State: A
- Function: autonomously carry out coding/repository investigation through iterative tool choice and environment changes/observations.
- Disturbance / variety regulated: changing user requests, source contents, errors in tool output, shell outcomes, model output and context-window pressure.
- Decisive decision or feedback right: the model-driven root `Agent` chooses tool names/arguments and next turns conditional on tool results; spawned subagents may independently choose local read-only tools toward a delegated task.
- Decision owner: the executing model-guided agent actor within AshCode's owned loop; external inference supplies tokens, not a separate coding-agent runner.
- Supporting / enforcement mechanisms: `ToolRegistry`, approval confirmations, tool schemas, client stream parser, context compactor, max-turn and loop detector.
- Closure path: tool result → `ContextManager.add_tool_result` → next `chat_completion` → agent's next tool/response.
- Boundary reachability: `main.py` instantiates the first-party `Agent`; `Session.initialize` installs tools; `Agent.run` invokes `_agentic_loop` in both shipped interactive and single-shot modes.
- Why this is / is not agent-owned: model selects task-level actions and responds to environment feedback, while runtime dispatch/gates enforce those selections. Agent discretion is material under the counterfactual owner test.
- Evidence: [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L22-L121); [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L22-L166); [tools/registry.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/registry.py#L52-L113); [tools/builtin/shell.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/builtin/shell.py); [tools/builtin/edit_file.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/builtin/edit_file.py).
- Basis: structural.
- Confidence: high for owned iterative loop; no end-to-end benchmark claim.
- Caveats: ability to execute a requested operation depends on provider tool-calling support, environment and safety rules.

## S2 — Coordination

- State: —
- Function: no first-party evidenced inter-S1 oscillation/conflict-attenuation feedback cycle beyond task sequencing and child invocation.
- Disturbance / variety regulated: a parent may issue multiple tool calls and nested investigation tasks; structurally evidenced competing S1 use of shared resources or conflicting commitments is not regulated by a purpose-built S2 response.
- Decisive decision or feedback right: parent delegates one goal as a tool call; child returns a result. No cross-S1 arbitration, reservation or reciprocal stabilization right is established.
- Decision owner: parent task agent for delegation; deterministic `for` loop and `wait_for` enforce invocation order and deadline.
- Supporting / enforcement mechanisms: tool registry, read-only child allowlists, timeouts, ordinary sequential tool dispatch.
- Closure path: child text enters parent next S1 step, not a demonstrated corrective feedback path regulating interference between independently operating S1 units.
- Why this is / is not agent-owned: delegating or serially invoking children is not S2; the record contains no concrete disturbance-plus-attenuation witness as required by Profile 0.2.4.
- Evidence: [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L112-L151); [tools/subagents.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/subagents.py#L25-L156); [tools/registry.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/registry.py#L93-L141).
- Basis: structural.
- Confidence: medium-high for bounded absence at checked execution graph.
- Caveats: external custom plugins or independently run AshCode CLI processes might create resource competition, but their coordination is not shipped as a first-party S2 organization.

### Absence scope

- Surfaces inspected: parent tool-call loop, bundled subagent definitions/implementation, `ToolRegistry`, context/session state, tool allowlists, config and README-supported operating modes.
- Plausible first-party paths checked: nested agents, parent-child results, multi-tool response batch, parallelism wording in prompts, tool safety and shared CWD.
- Why no material first-party path remains: each nested child is synchronously awaited and feeds a task result to its parent; no shipped coordination relation is evidenced as resolving a specific interaction-induced oscillation/conflict among distinct S1 units and returning the resolution to alter those units' later work.

## S3 — Inside-and-now control

- State: —
- Function: no owned whole-system current-control supervisory loop with discretionary resource/commitment intervention at the assessed session recursion.
- Disturbance / variety regulated: token/context pressure, unsafe edits and shell commands, hanging subagent work, repetitive actions.
- Decisive decision or feedback right: operator selects approval policy and turn/model config; runtime gates execute those limits, and agents select local next task steps. No distinct supervisor with an authoritative whole-system current operating view and returned shared-commitment decisions.
- Decision owner: human/user for per-tool approvals and policy config, deterministic constructors for hard limits; neither is evidenced as a first-party higher-recursion S3 current-control feedback owner.
- Supporting / enforcement mechanisms: `ApprovalManager`, `ContextManager`, loop detector, per-subagent timeout, CLI `/stats`.
- Closure path: ordinary approval or context management modifies a specific operation/turn; no function-specific whole-current supervisory response loop established.
- Why this is / is not agent-owned: resources and limits are enforced, but no autonomous or supported parent S3 whole-system discretionary resource decision returns through a first-party protocol.
- Evidence: [safety/approval.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/safety/approval.py#L92-L162); [agent/agent.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/agent/agent.py#L38-L165); [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L166-L279); [context/manager.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/context/manager.py#L119-L216).
- Basis: structural.
- Confidence: medium-high.
- Caveats: user may manually manage multiple terminals, outside the bounded session organization.

### Absence scope

- Surfaces inspected: session bookkeeping, CLI commands, agent loop, approval config and checks, tool invocation, context/loop detector, subagent budgets and timeout.
- Plausible first-party paths checked: `/stats` and `/approval`, budget controls, hook errors, timeout intervention, self-management through model tools.
- Why no material first-party path remains: these paths constrain/observe operations but no shipped whole-system S3 owner uses a current shared view to revise inter-unit commitments/resources and close subsequent control, including a legitimate operator-governed S3 mode.

## S3* — Complementary audit

- State: —
- Function: no independently grounded source-of-truth audit of routine operational claims with a consequential findings-return path is established by the standard runtime.
- Disturbance / variety regulated: potentially incorrect code and tool results, tests or unsafe edits; ordinary coding verification or a reviewer persona could challenge an individual task artifact but no complementary audit mandate/closure is wired.
- Decisive decision or feedback right: bundled `code_reviewer` is a general read-only child that the parent agent may invoke as a normal tool; hook commands are user-configured and default disabled. No independent auditor controls a complementary source path and adjudicates actual production claims.
- Decision owner: parent coding agent selects child reviewer task; custom hooks belong to external user-defined scripts; neither establishes separate first-party audit judgment ownership.
- Supporting / enforcement mechanisms: read-only reviewer tools, generic logs/tool events, optional callbacks, tests and CI (adjacent development).
- Closure path: generic child text → parent task context, without required independent audit evidence, report, correction authority or closed audit finding path.
- Why this is / is not agent-owned: `code_reviewer` name and prompt do not establish independence from the audited agent or a distinct complementary S3* operating channel.
- Evidence: [tools/subagents.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/subagents.py#L134-L156); [tools/registry.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/registry.py#L119-L145); [hooks/hook_system.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/hooks/hook_system.py#L12-L143); [.github/workflows/ci.yml](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/.github/workflows/ci.yml).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an operator could configure an external audit workflow around the agent, but that is not shipped first-party independent S3* closure.

### Absence scope

- Surfaces inspected: default code reviewer/investigator, bundled tool registry, user-configured hooks, agent events, CI/test files, approval policies.
- Plausible first-party paths checked: child reviewer reading code, after-tool hook receiving result, tests/CI, user approval of changes.
- Why no material first-party path remains: reviewer is an ordinary caller-chosen S1 tool, hooks carry external scripts and do not own judgment, CI belongs to contributor development; none ships an independently sourced audit owner with authoritative corrective return into the assessed operating organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective model of external change that generates and implements future capability adaptations.
- Disturbance / variety regulated: changing working files, tasks, model context and provider settings; these are absorbed as current task inputs and operator configuration.
- Decisive decision or feedback right: agents may search the web and plan current requested work; user changes provider/model; compaction updates conversation summary. No distinct future-oriented adaptation choice enters a current-capability feedback loop.
- Decision owner: user for model/config changes, task agent for current research and edits, deterministic compaction/retention routines for context management.
- Supporting / enforcement mechanisms: web/search tools, `memory`, context compression, project instructions, optional hooks.
- Closure path: normal tool context feeds current task; no source-evidenced environmental scanning → future option → adopted capability change.
- Why this is / is not agent-owned: task planning, memory and context compression do not by themselves constitute external-prospective S4 intelligence.
- Evidence: [tools/builtin/web_search.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/builtin/web_search.py); [tools/builtin/memory.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/builtin/memory.py); [context/compaction.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/context/compaction.py); [context/manager.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/context/manager.py#L119-L181); [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L185-L215).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the agent may be asked to propose improvements; a task response does not create a shipped S4 organization.

### Absence scope

- Surfaces inspected: model configuration and CLI switching, context/compaction/memory, web tools, subagents and hooks, task planning.
- Plausible first-party paths checked: web investigation as environmental sensing, saved memory as durable change, adapting provider/model during a run, code-reviewer recommendations and test feedback.
- Why no material first-party path remains: no evidenced first-party prospective capability option evaluation and authoritative return into future operating capability; changes remain current-task decisions or external operator configuration.

## S5 — Policy and identity

- State: —
- Function: no explicit identity/ultimate-policy issue → legitimate deciding authority → returned operation-changing decision cycle at the scoped harness recursion.
- Disturbance / variety regulated: risky tool operations, mutable developer instructions, model choice, cwd and user trust boundaries.
- Decisive decision or feedback right: operator selects tool approval policy and may accept/reject individual operations; supplied prompts/config bound execution. These are ordinary security and task controls, not an identity-level deliberative decision.
- Decision owner: external user and static configuration for access settings, plus runtime for deterministic enforcement; no shipped S5 identity/ultimate-policy closure.
- Supporting / enforcement mechanisms: approval policy Enum, system prompt assembly, `AGENT.MD`, hook/tool allowlists.
- Closure path: task/permission choices affect a call or session configuration; an identity/policy issue is not routed to legitimate authority with a specific returned ultimate policy decision.
- Why this is / is not agent-owned: the model cannot authoritatively redefine its own organizational identity, and configurable safety policy does not itself supply an S5 decision protocol.
- Evidence: [config/config.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/config/config.py#L54-L106); [safety/approval.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/safety/approval.py#L92-L162); [main.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/main.py#L166-L220); [prompts/system.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/prompts/system.py); [config/loader.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/config/loader.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: OSS maintainer policy governs the project as a distinct higher recursion but is not this single operating CLI session's included first-party return path.

### Absence scope

- Surfaces inspected: user/project configuration, model/system prompt, approval policy and CLI updates, hook configuration, custom tools, project instruction loading and contributor development boundary.
- Plausible first-party paths checked: per-task confirmation, interactive policy switch, user instruction hierarchy, developer config override, external hook, contributor project governance.
- Why no material first-party path remains: only ordinary static/runtime bounds and per-operation authorization are supported; no first-party ultimate-policy issue adjudication and binding return cycle for the assessed session is established.

## Recursion

A child `Agent` is independently model-guided for its bounded investigation/review task, but it is owned/invoked via parent tool dispatch, shares configured workspace and returns one summarized result. That evidences nested operational capacity, not independent viability of a full child metasystem or an autonomous cross-agent organization. [tools/subagents.py](https://github.com/AuthRan/AshCode/blob/74f30ddac455175d4a18cb105a00ae1bde42cd69/tools/subagents.py#L25-L118).

## Variety and escalation

The tool response/error carries local environmental variety back to the decision-making S1. Safety decisions constrain risky actions, subagent deadline protects from hanging awaits, and compaction attenuates large context. The CLI user can change model/approval policies and reject a step, but those actions do not by themselves establish S3 or S5 ownership. Exceptional error callbacks/logging do not establish a new VSM function or audited algedonic channel.

## Evidence gaps

- Static-source assessment at one exact frozen commit; no production trace or benchmark performance claims. External model quality, arbitrary configured MCP/hook semantics and third-party extension behavior are not imported.
- A generic child code-review capability is operationally reachable, but its invocation/independent evidence/closed corrective mandate is not S3* specific in the shipped path. A separate source-first audit could challenge this bounded absence, without being assumed to have occurred.
- No material unresolved *shipped* S2/S3/S4/S5 path was identified after reviewing the frozen executable mode, nested-agent registration, configuration and developer-only testing boundary. An imagined future extension alone does not force `?`.
