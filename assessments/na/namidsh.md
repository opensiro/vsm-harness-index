---
harness_id: namidsh
project_name: NamiDSH
repository: https://github.com/aa1143/NamiDSH
review_ref: 629e9efcb121b2805a2f3c48565144b732c0ff7f
reviewed_at: 2026-11-05
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

# NamiDSH

## Review boundary

- System in focus: One locally self-hosted NamiDSH web agent and its shipped first-party mini-Cordis plugin tree, from HTTP chat request through configured model, native tools and session-local feedback. The larger DeepSeek Harness project whose design is illustrated is **not** included.
- Purpose and identity: Small educational but runnable agent harness demonstrating first-party plugin-composed model/tool interaction, session state and dynamic dependency lifecycle.
- Relevant environment: Operator's local workspace and browser, configured model API endpoint/credentials or offline mock, plugin availability, local file/time tools and input/tool-result disturbances.
- Standard-distribution boundary: `apps/web/src/main.ts`, `packages/{agent-spine,agent-loop,llm,llm-deepseek,llm-mock,tools,tool-fs,tool-time,session,system-prompt,cordis,webserver}/src`, web static UI and supported Node 22+ workspace package installation.
- Credited operating / distribution surfaces: [assembled entry](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/apps/web/src/main.ts), [agent loop](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-loop/src/index.ts), [spine](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-spine/src/index.ts), [model adapter](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/llm-deepseek/src/index.ts), [tools](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts), [webserver](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/webserver/src/index.ts), [sessions](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/session/src/index.ts).
- Adjacent first-party surfaces excluded from ownership: Educational tutorial series and architecture diagrams, standalone compatibility/agent tests, npm/release tooling, author's external NamiAgent/NamiGPT repos and upstream DeepSeek Harness/Cordis implementation. Tests may corroborate a path but do not install governance or independent audit into the web agent.
- First-party operating / deployment modes considered: Standard local web entry with API_KEY/DEEPSEEK_API_KEY and streamed DeepSeek tool calls; offline deterministic `llm-mock` demonstration without API key; operator-composed plugin replacement, optional `tools/pre-execute` guard shown in tests; session-local request cancellation and maxSteps stop.
- Recursion level: One web-agent session using one model-owned S1 task loop, not a viable organization of independently operating plugin services or all client sessions.
- Reviewed revision: `aa1143/NamiDSH@629e9efcb121b2805a2f3c48565144b732c0ff7f` (first-party MIT source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The web entry creates a `Context`, installs a spine of model/session/tool/prompt/agent-loop services, selects the DeepSeek adapter when credentials are present or deterministic mock otherwise, then exposes an HTTP/SSE chat endpoint. `AgentLoop.run` appends the user turn, builds the prompt and session-derived messages, streams the model, collects discretionary tool calls, invokes `ctx.tools.execute`, stores tool results and repeats up to a fixed maxStep bound. Session events are in an in-memory map and re-derived as model messages; the webserver forwards only matching session events, cancels on connection close, and cleans up listeners. Tool registration is dynamic and the execution pipeline offers pre/execute/post waterfalls. Cordis registry/fiber machinery starts or disposes dependent services when providers appear/disappear; its lifecycle is not a second autonomous executive. [README](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/README.md), [entry](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/apps/web/src/main.ts), [loop](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-loop/src/index.ts), [tests](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/tests/agent.ts).

## Operational model

An individual configured model is the agent actor selecting whether to answer or use an available first-party tool in response to a task and observed tool effects. The TypeScript loop transports its choices and feeds observations back; a separate mock mode produces rule-scripted tool calls and is **not** proof of agentic discretion. Plugin lifecycle, operator credential/config choice, approval hooks and HTTP request control are deterministic/human constraints. No second S1 manager, independent auditor, future strategy maker or identity-policy decisional body is packaged at this session boundary.

## S1 — Operations

- State: A
- Function: A self-hosted model-driven session performs user-requested observation/tool actions and produces a revised answer to task/environment feedback.
- Disturbance / variety regulated: User tasks, changing available tools, local time/filesystem observations, returned tool values/errors and model-selected next steps.
- Decisive decision or feedback right: In DeepSeek mode, the model determines assistant text or tool name/arguments from its session history and current advertised tool schemas; after receipts it can choose the next action or end.
- Decision owner: Configured agent model through the shipped first-party `agentLoop`/DeepSeek adapter path; tool executor and host transport enforce choices without choosing the task strategy.
- Supporting / enforcement mechanisms: `maxSteps=8` default bound, tool registration/list, JSON parsing and errors, pre-execute waterfall, event stream, abort signal, in-memory session log and restricted filesystem tool.
- Closure path: User input → first-party webserver/session/loop → configured model tool decision → first-party ToolRuntime/local tool → logged result → next model turn/answer → web SSE response.
- Boundary reachability: `apps/web/src/main.ts` **actually installs** spine, model adapter and webserver; the `AgentLoop.run` reached by HTTP executes the model/tool feedback loop with the shipped read-only FS/time tools. This is a supported opt-in real provider mode, not merely an external model callback skeleton.
- Why this is / is not agent-owned: The agent chooses tool actions and final responses in configured DeepSeek mode. Deterministic mock fallback, model provider infrastructure and safety hooks do not themselves own that discretion.
- Evidence: [entry wiring](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/apps/web/src/main.ts), [agent loop](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-loop/src/index.ts), [DeepSeek SSE tool-call adapter](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/llm-deepseek/src/index.ts), [tools](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts), [session](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/session/src/index.ts).
- Basis: Explicit installed real-provider mode and first-party closed tool-result feedback; offline tests corroborate routing only.
- Confidence: High for source reachability; no live paid DeepSeek E2E attempted.
- Caveats: Mock mode is deterministic and all first-party file tools are read-only; neither implies broader system authority or external-provider correctness.

## S2 — Coordination

- State: —
- Function: No coordination of multiple independently autonomous S1 work units with a specific attenuated interaction conflict is established.
- Disturbance / variety regulated: Plugin service name conflicts and simultaneous web sessions can occur, but these are registry/transport concerns rather than demonstrated inter-S1 organizational interference.
- Decisive decision or feedback right: Cordis resolves service registration and dependency readiness; sessions remain independent records with no reciprocal task coordination decisions.
- Decision owner: Deterministic registry/fiber scheduler and the operator who composes plugins.
- Supporting / enforcement mechanisms: Service uniqueness checks, plugin hot-unplug lifecycle, event channels and per-session SSE filters.
- Closure path: Service availability changes reload dependent plugin implementations, not a feedback relation between two task-operating S1 cells.
- Why this is / is not agent-owned: A model sees its own session and tools, not conflicts between separate autonomous operational units.
- Evidence: [spine](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-spine/src/index.ts), [tool registry](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts), [webserver](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/webserver/src/index.ts), [agent tests](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/tests/agent.ts).
- Basis: Bounded negative against shipped multi-session and plugin-interference candidates.
- Confidence: High.
- Caveats: Future compositions could introduce many autonomous agents, but such a mode is not shipped.

### Absence scope

- Surfaces inspected: Agent loop, session and webserver transport, service registry, tool lifecycle, plugin composition examples and agent tests.
- Plausible first-party paths checked: Multiple HTTP sessions, Cordis service conflict handling, plugin hot-reload, tool registry uniqueness, events as an inter-S1 channel.
- Why no material first-party path remains: None supplies distinct S1 work cells, task-level conflict, coordination decision and returned adjustment to multiple agents at the same recursion; registry contention is technical service lifecycle.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current controller regulates a portfolio of autonomous S1 work, priorities and resource commitments.
- Disturbance / variety regulated: Individual session turn limits, client disconnects, tool errors and plugin availability.
- Decisive decision or feedback right: The model performs local S1 continuation; the host enforces fixed maxSteps and client cancellation. No second actor holds cross-session budget/resource/commitment discretion.
- Decision owner: Local agent for its task choices; deterministic runtime and human operator for installed configuration.
- Supporting / enforcement mechanisms: maxSteps counter, AbortController, dependency readiness, session event log and tool pre-execute hooks.
- Closure path: Limit/abort terminates or prevents one run; no whole-portfolio observation → S3 priority/resource decision → changed subsequent multi-unit operation.
- Why this is / is not agent-owned: Stop enforcement and tool transport do not own whole-system current management merely because they can block an action.
- Evidence: [loop](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-loop/src/index.ts), [webserver](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/webserver/src/index.ts), [tools](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts).
- Basis: Bounded negative.
- Confidence: High.
- Caveats: A host could add an operator management plugin; generic plugin hooks do not constitute an installed S3.

### Absence scope

- Surfaces inspected: Local run loop, service lifecycle, web session handling, tool guard hooks, test/example plugin replacements.
- Plausible first-party paths checked: MaxStep stop as current S3, pre-execute approval as S3/P, dependency lifecycle as current manager, session store as portfolio view.
- Why no material first-party path remains: These implement per-session execution policy or technical dependency state, without whole-S1-portfolio resource/commitment decision owner and corrective feedback.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit pathway checks the actual agent's claims through alternate reality evidence and returns findings into control.
- Disturbance / variety regulated: Tool action mistakes and stale results can be tested or blocked, but product does not install a separate independent truth-checking auditor.
- Decisive decision or feedback right: Optional pre-execute hooks can block action and unit tests verify mock behavior, neither produces an independent audit judgment from distinct operational evidence.
- Decision owner: Operator-authored guard/test runner outside the packaged runtime; no S3* reviewer in standard deployed mode.
- Supporting / enforcement mechanisms: Tool-result events, session logs, mocked agent tests and mock/real Cordis compatibility comparison.
- Closure path: Direct tool result → same agent context; separate test/guard → local failure/block. No independent audit finding → accountable S3 corrective change.
- Why this is / is not agent-owned: Technical testing and configurable permission hooks are not independent S3* just because a different function handles them.
- Evidence: [tool hooks](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts), [agent test guard](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/tests/agent.ts), [compatibility test](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/tests/compat.ts).
- Basis: Bounded negative.
- Confidence: High.
- Caveats: Operator may externally audit runs; not a first-party packaged complementary audit channel.

### Absence scope

- Surfaces inspected: Tool waterfall, session event logger, mock/compat tests, plugin architecture and standard web entry.
- Plausible first-party paths checked: Pre-execute guard as auditor, tool-post-execute hook as raw-reality check, compatibility tests as independent reviewer, session traces as S3*.
- Why no material first-party path remains: None establishes independent complementary reality access, a distinct audit judgment owner and a returned correction to a controlling S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective strategy/adaptation feedback loop is installed in the session's first-party distribution.
- Disturbance / variety regulated: New tasks, plugin/provider availability, workspace changes and future model upgrades.
- Decisive decision or feedback right: Operator may replace plugins/provider or edit persona; the agent plans only the present chat turn and follows current tool results.
- Decision owner: Operator/developer for longer-term model/tool changes; no strategically deciding agent in the standard distribution.
- Supporting / enforcement mechanisms: Dynamic plugin dependency restart, configurable provider/model, ephemeral session log and prompt service.
- Closure path: Current task → local reply, or manual plugin/config update → next run; no external forecast/adaptation option → S3 conversation → future capability change loop.
- Why this is / is not agent-owned: A hot-swappable model service is an adaptation *mechanism*, not evidence that the agent models changing external capability and selects revisions.
- Evidence: [entry](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/apps/web/src/main.ts), [spine](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-spine/src/index.ts), [agent loop](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/agent-loop/src/index.ts), [plugin tests](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/tests/agent.ts).
- Basis: Bounded negative.
- Confidence: High.
- Caveats: Educational articles explain extensibility, not installed strategic decision ownership.

### Absence scope

- Surfaces inspected: Web entry, context lifecycle, model and tool adapters, in-memory session store, prompt and agent loop, educational plugin examples.
- Plausible first-party paths checked: Runtime model switching, plugin hot-swap, task planning in the model, memory of recent tool feedback.
- Why no material first-party path remains: All serve the present session or externally authored configuration. No shipped future-environment model, adaptation option chooser and returned operational adoption are wired.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy deliberation and returned mandate operates at the local harness recursion.
- Disturbance / variety regulated: Access to local file tools, persona changes, model credentials and user preferences.
- Decisive decision or feedback right: Operator preselects workspace, model and persona and may compose a permission guard; the shipped web agent lacks a channel for identity-level matters to a legitimate parent authority with returned policy.
- Decision owner: Human developer/operator outside the agent session; static code and optional plugin veto enforce limits.
- Supporting / enforcement mechanisms: Static system prompt, root-scoped tools, runtime configuration, dependency hooks and tool waterfall.
- Closure path: Ordinary guard veto or user input influences one run; no identity/policy issue → ultimate authority → authoritative decision → subsequent harness governance feedback.
- Why this is / is not agent-owned: Persona text, workspace permissions and generic approval-like hooks do not transfer the S5 decision right to the agent or establish a parent-governed closed mode.
- Evidence: [system prompt](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/system-prompt/src/index.ts), [entry](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/apps/web/src/main.ts), [tools](https://github.com/aa1143/NamiDSH/blob/629e9efcb121b2805a2f3c48565144b732c0ff7f/packages/tools/src/index.ts).
- Basis: Bounded negative.
- Confidence: High.
- Caveats: Maintainer governance of the public project is a separate organization, not the installed local session.

### Absence scope

- Surfaces inspected: Prompt service, workspace configuration, tool guard extensibility, web entry, session model and contributor/docs boundary.
- Plausible first-party paths checked: System prompt identity, manual model selection, tool approval, plugin hot-reload, project maintainer policy.
- Why no material first-party path remains: No runtime identity-level issue is routed to a legitimate parent decision owner and returned as policy governing subsequent operation; all reviewed controls are static or ordinary S1 constraints.

## Recursion

The single model-driven session is the assessed S1. Cordis plugins are technical dependencies; neither their nested scopes nor the existence of many web sessions proves viable recursive organizational units. No separate parent metasystem is installed in this compact demonstration.

## Variety and escalation

Available tool schemas and the local session history amplify the agent's task response variety; maxSteps, optional tool veto and workspace root attenuate/limit unsafe actions. Missing providers stop/restart dependent plugins and disconnects abort current responses. Those are ordinary lifecycle/failure controls, not evidence of a separately authorized algedonic S3/S4/S5 path. Policy/identity questions remain with the operator outside this assessed session.

## Evidence gaps

- Node 24 is available, but a fully offline `npm install --offline` failed because a package tarball was absent from the local npm cache; no provider-backed E2E was performed. Source/test paths provide the positive first-party model-to-tool closure witness, not a claimed live deployment receipt.
- The no-key mock is deterministic, not evidence of AI autonomy; the keyed first-party DeepSeek adapter is an expressly supported mode, but actual hosted availability and performance were not tested.
