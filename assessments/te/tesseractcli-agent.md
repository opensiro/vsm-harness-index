---
harness_id: tesseractcli-agent
project_name: TesseractCLI-Agent
repository: https://github.com/tesseractai-lab/TesseractCLI-Agent
review_ref: 2ad0d2f5874034fa74797bb95737091748e01372
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TesseractCLI-Agent

## Review boundary

- System in focus: the repository-owned local TesseractCLI terminal coding agent in the supported Python 3.11 CLI/Textual mode, including its single ReAct loop, provider dispatcher, tool registry, approvals and workspace conversation persistence.
- Purpose and identity: help an operator perform repository/file development operations through a provider-independent model choosing bounded read/write/edit/shell/list tools, with explicit write approvals.
- Relevant environment: changing user instructions, workspace files, model-provider availability, command feedback, approval decisions and remembered session messages.
- Standard-distribution boundary: pinned `pyproject.toml` 1.0.0 Python package and launcher/UI, with five shipped core tools; provider SDKs are dependencies, and unused generic framework capabilities are excluded unless instantiated by TesseractCLI.
- Credited operating / distribution surfaces: `tesseractcli/__main__.py`, `ui/app.py`, `agent/loop.py`, `llm/dispatcher.py`, `llm/routing.py`, `tools/registry_builder.py`, `tools/registry.py`, `tools/approval.py`, shipped sandbox tools, `memory/store.py`, `prompts/system_prompt.py` and installed configuration.
- Adjacent first-party surfaces excluded from ownership: tests/mocks, manual demonstration scripts, example environment files, GitHub workflows, maintainer docs/roadmap and project-contributor decisions. Third-party LangChain abstractions, model APIs and external logging/tracing endpoints are not first-party organizational owners.
- First-party operating / deployment modes considered: local Textual chat session invoking `run_inner_loop`, pack/model selection and provider fallback, dynamic tool schema activation (dormant with the five current core tools), approval/denial loop, SQLite session history and per-workspace sandbox constraints.
- Recursion level: one locally operated TesseractCLI assistant and workspace, not a broader software-team or upstream development organization.
- Reviewed revision: `2ad0d2f5874034fa74797bb95737091748e01372` (batch #1011 frozen row 7).
- License screen: root `LICENSE` grants MIT.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Textual UI collects a workspace and model pack and calls `run_inner_loop` once per user turn. That loop builds a system message and tool schema, awaits a provider-backed model response, dispatches model-selected tool calls through a first-party registry and returns success/errors as `ToolMessage` inputs for the next model decision. Filesystem, edit, shell and read/list tools are bounded by a workspace sandbox and approval callback. The `LLMDispatcher` resolves a configured pack and handles provider or model fallback for inference resilience; fallback candidates are substitute providers for the same S1 decision loop, not distinct concurrently operating S1 cells. A SQLite `ConversationStore` records messages and metadata across turns.

The five shipped tools in `registry_builder.py` are write, read, edit, execute and list; none starts independently deciding subagents, offers a whole-current cohort roster, invokes a separate fresh auditor, or changes the harness's future capabilities. Lazy `search_tools` is first-party but all five tools are currently `core=True`, so the deferred-tool path is not active in this frozen distribution. Model pack selection and source-level configuration are task routing/owner setup, while memory replay serves ordinary conversational continuity. Upstream test mocks and contributor governance are outside the installed-runtime owner boundary.

Frozen primary evidence: [agent loop](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/agent/loop.py), [tool registry builder](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/registry_builder.py), [dispatcher](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/llm/dispatcher.py), [memory store](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/memory/store.py), [system prompt](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/prompts/system_prompt.py).

## Operational model

One provider-backed model per conversation turn chooses the next filesystem/tool action and reacts to dispatch and approval outcomes (`S1=A`). Configured provider fallback and replay normalization keep the same operational loop available rather than coordinating distinct S1 operations (`S2=—`). There is no first-party separately deciding whole-current supervisory actor (`S3=—`), material complementary independent audit (`S3*=—`), external/future-directed capability-adaptation decision circuit (`S4=—`) or governing identity/ultimate-policy body (`S5=—`). Those negatives are bounded to this pinned locally installed system, not impossibility claims for an operator-created extension.

## S1 — Operations

- State: A
- Function: implement file and code edits, inspect workspace information, execute bounded commands and revise actions based on returned outcomes.
- Disturbance / variety regulated: differing requests, changing code/files, tool validation errors, denied permissions, provider output and runtime command results.
- Decisive decision or feedback right: the configured model selects named tool calls, inputs, retries and final response after observing `ToolMessage` feedback.
- Decision owner: one model invoked through `LLMDispatcher` from `run_inner_loop` for the current session turn.
- Supporting / enforcement mechanisms: provider pack routing, `ToolRegistry` schemas/dispatch, terminal/UI approval callback, sandbox path/command policy, error formatting and SQLite history.
- Closure path: user/context → provider model decision → approved tool dispatch or denial → success/error `ToolMessage` → subsequent model/tool choice or final answer.
- Boundary reachability: `ui/app.py` and launcher invoke the first-party `run_inner_loop` with `build_registry` tools; its tool feedback is appended to the mutable session history and reused on later turns.
- Why this is / is not agent-owned: the model has the task-specific discretionary choice of edits and follow-up repair; the sandbox and approvals only enforce allowed effects.
- Evidence: [ReAct loop](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/agent/loop.py), [registry](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/registry.py), [tools](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/registry_builder.py).
- Basis: explicit supported loop/registry wiring and native script/mocked provider tests.
- Confidence: high for shipped S1 construction; no evidence of real-provider task quality is claimed.
- Caveats: all evaluations here use mock/offline tests; provider quality, model decision success and performance were not evaluated live.

## S2 — Coordination

- State: —
- Function: no coordination circuit between distinct independently deciding S1 cells is established at the local-agent recursion.
- Disturbance / variety regulated: multi-agent interference is not encountered as an evidenced internal design; a single model can issue multiple tools but they do not form separate operational agents.
- Decisive decision or feedback right: tool dispatch and provider fallback choose execution and alternate inference endpoints, not attenuation of an inter-S1 disturbance.
- Decision owner: current model for individual operations; fixed provider routing, approval and sequential tool loop for mechanics.
- Supporting / enforcement mechanisms: `LLMDispatcher`, `RoutingResolver`, registry dispatch, tool-call sequence and tool-result replay.
- Closure path: provider failure → same-turn alternate provider; tool result → same agent; no distinct-S1 interference → coordination decision → feedback loop.
- Why this is / is not agent-owned: alternate provider candidates answer for the same agent, and serial tool calls do not create a horizontal coordination mechanism for multiple operational cells.
- Evidence: [routing](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/llm/routing.py), [dispatcher](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/llm/dispatcher.py), [loop](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/agent/loop.py).
- Basis: inspected all shipped core tool registrations and provider selection path.
- Confidence: high within the pinned single-agent distribution.
- Caveats: external orchestrators could instantiate multiple independent installs; that unshipped assembly lies outside the declared boundary.

### Absence scope

- Surfaces inspected: agent loop, provider packs/fallback, tool registry and tool-call dispatch, UI/launcher and SQLite sessions.
- Plausible first-party paths checked: competing providers as independent S1, multiple tool calls as distributed work, workspace memory as shared task board and dormant lazy tooling as a prospective coordination constructor.
- Why no material first-party path remains: these operate one model decision chain with substitute inference providers and no first-party distinct-S1 conflict or interference regulator.

## S3 — Inside-and-now control

- State: —
- Function: no separately owned current whole-system prioritization, resource reallocation or selective intervention over multiple operational commitments is evidenced.
- Disturbance / variety regulated: iteration caps, command failures and approval decisions constrain individual tasks but do not regulate a running population of distinct S1 units.
- Decisive decision or feedback right: the operator picks workspace and model pack; fixed `max_iterations` limits one request, while the same model handles current step choices.
- Decision owner: primary model for task-local operation and human for tactical approvals, without a separate first-party current management function.
- Supporting / enforcement mechanisms: `AgentConfig.max_iterations`, model picker, approval view, saved sessions, dispatcher fallback and tool-result history.
- Closure path: user-selected settings and individual action approvals affect the next S1 step; no full-current operations view → supervisory prioritization/intervention → altered cohort exists.
- Why this is / is not agent-owned: a max-iteration guard, provider picker, conversation history or operator approval is not itself an S3 whole-system decision right.
- Evidence: [loop iteration bound](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/agent/loop.py), [UI](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/ui/app.py), [agent config](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/models/config_models/agent_models.py).
- Basis: current-operation and available mode inspection.
- Confidence: high for the local single-agent boundary.
- Caveats: operator session management may be useful but is not shown to own current cross-S1 decisions.

### Absence scope

- Surfaces inspected: REPL/Textual state flow, model selection/pack config, max iteration logic, workspace log/session controls and approval UI.
- Plausible first-party paths checked: human workspace/model selection as S3=P, iteration caps as resource control, persisted sessions as whole-system view and dispatcher fallback as supervisory allocation.
- Why no material first-party path remains: no cohort of separately operating S1 units with a current whole-system view and discretionary intervention/return is shipped; all cited controls are request-local or setup-time.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary auditor with independent access, judgment and feedback to the operational controller is present.
- Disturbance / variety regulated: latent correctness defects in generated edits can survive ordinary tool feedback, but no separately governed audit channel is supplied.
- Decisive decision or feedback right: tests and human approval may judge immediate effects, but there is no distinct audit owner or role that evaluates operational claims and returns actionable audit conclusions.
- Decision owner: the main model and attending user in the ordinary action/approval path.
- Supporting / enforcement mechanisms: Python test suite, tracing, tool results and human-visible approval previews.
- Closure path: error and approval outputs return to the same S1 conversation; no independent audit→finding→S3 response cycle is instantiated.
- Why this is / is not agent-owned: unit tests and observability are mechanics, and the approval user judges individual tool side effects rather than independent operational-system claims.
- Evidence: [registry builder](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/registry_builder.py), [tracing](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/observability/tracing.py), [approval](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/approval.py).
- Basis: audited available tools, review/diagnostic surfaces and runtime feedback path.
- Confidence: medium-high.
- Caveats: an external independent reviewer could be paired with this agent, but no such first-party constructor is included.

### Absence scope

- Surfaces inspected: runtime tool declarations, prompts, tracing, repository tests, approvals and user interface.
- Plausible first-party paths checked: `approve_fn` as independent auditor, source tests as complementary evidence, telemetry as monitoring and human source review as installed S3*.
- Why no material first-party path remains: none provides a distinct audit-specific owner and independent operational claim review with returned findings; each is ordinary task checking or outside-runtime development practice.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/future sensing and adopted capability adaptation loop is established in the supported installed system.
- Disturbance / variety regulated: shifting provider availability, future development practices and evolving tasks may matter, but current fallback and retained history do not choose changes to the harness's future repertoire.
- Decisive decision or feedback right: provider/pack fallback adapts current inference availability; user/admin must configure future model packs and source tools.
- Decision owner: configuration user for persistent pack changes and model dispatcher for fixed current-request fallback rules.
- Supporting / enforcement mechanisms: routing packs, configuration manager, optional deferred schema activation, persistent conversation history and source-level tool registrations.
- Closure path: current provider error → alternate model within the same request; messages → later conversation context. No external/prospective distinction → agent-generated new capability → adoption → later changed operation loop is shipped.
- Why this is / is not agent-owned: switching a provider for transient current work and persisting transcripts are not prospective capability choices; dormant lazy tool loading only reveals already installed tools.
- Evidence: [dispatcher](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/llm/dispatcher.py), [packs manager](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/config/global_config/packs_manager.py), [memory store](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/memory/store.py).
- Basis: current/future distinction inspected across routing, memory and tool registration.
- Confidence: medium-high.
- Caveats: a coding agent could be directly asked to edit its own source, but that remains user-directed S1 work rather than a shipped prospective S4 organization.

### Absence scope

- Surfaces inspected: persistent memory/session history, pack/provider routing, model picker and settings, lazy schema discovery and source/distribution tool registration.
- Plausible first-party paths checked: provider failover as future adaptation, SQLite as organizational learning, operator config as parent S4=P and `search_tools` as capability expansion.
- Why no material first-party path remains: no decision circuit transforms observed future/external distinctions into a model-chosen adopted capability; routing and schema activation change only the current inference/tool presentation, while lasting config is operator setup.

## S5 — Policy and identity

- State: —
- Function: no first-party governing identity/ultimate-policy authority and return circuit for a TesseractCLI operational organization is evidenced.
- Disturbance / variety regulated: competing final purposes and legitimate governance boundaries are not submitted to a distinct ultimate-policy institution.
- Decisive decision or feedback right: the operator can approve individual writes/commands and choose runtime settings; fixed prompt/sandbox defines static limits.
- Decision owner: user for tactical approvals and config; maintainers for external project direction, not an installed S5 body.
- Supporting / enforcement mechanisms: sandbox path guard, sensitive-file and command policy, prompt identity paragraph, tool approval callbacks and configuration file.
- Closure path: proposed write → human action approval/denial → S1 sees result; no identity-level problem → authoritative ultimate decision → returned constitution-like constraint exists.
- Why this is / is not agent-owned: restrictive execution policy and the assistant's self-description are not dynamic legitimate decisions about the organization's identity or purpose.
- Evidence: [approval](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/approval.py), [prompt](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/prompts/system_prompt.py), [path guard](https://github.com/tesseractai-lab/TesseractCLI-Agent/blob/2ad0d2f5874034fa74797bb95737091748e01372/tesseractcli/tools/sandbox/path_guard.py).
- Basis: inspected shipped identity, permission and policy paths.
- Confidence: medium-high.
- Caveats: user sovereignty over the workstation is real but lacks a first-party ultimate-policy loop at this recursion.

### Absence scope

- Surfaces inspected: system prompt identity/agency rules, safety/approval policy, model/settings screens, runtime config, maintainer documentation and test checks.
- Plausible first-party paths checked: human confirmations as parent S5, identity text as a constitution, filesystem/shell policy as a S5 authority and upstream maintainers as operational governors.
- Why no material first-party path remains: these implement static developer/operator constraints or development governance outside the assessed system; no legitimate identity-level decision and governed return is instantiated.

## Distributed OSS parent arrangement

Upstream developers and independent users can share code, but their source/CI processes are not operationally wired into a common S3–S5 authority governing locally installed TesseractCLI sessions. Local action approvals do not imply a shared organizational parent.

## Self-hosted and non-human modes

The local owner selects a provider pack and authorizes individual mutating tools, but the shipped terminal mode does not provide parent-governed current portfolio control, prospective capability adoption or ultimate policy through these UI controls. The autonomous primary model retains S1 discretion only.

## Recursion

There is one model-backed operational cell at this recursion. Tool calls are subordinate action effects, and provider pool candidates are substitutes for the same cell, not concurrent independently deciding organizational units.

## Variety and escalation

Task-local verification and approval failures enter the main loop as messages. Provider errors can invoke configured alternatives, but this protects S1 continuity without a cross-S1 coordination system. Session persistence and error reports do not independently establish a metasystem.

## Evidence gaps

- Exact frozen SHA `2ad0d2f5874034fa74797bb95737091748e01372`, native Python 3.11.17 `uv sync --frozen` from the committed `uv.lock`, `python -m compileall -q tesseractcli` PASS, and **164/164 pytest tests PASS** with a temporary local non-secret `.env` matching the documented required settings. That temporary config was removed after execution and the upstream checkout is clean.
- Initial unconfigured test collection yielded 20 `Settings` validation collection errors; injecting required keys via global process environment allowed 161 passes but interfered with three environment-specific tests. Providing the documented repo-local `.env` instead yielded the clean 164-pass suite; no failures were concealed or source tests patched.
- All tests used script/mock fixtures; no real LLM provider calls, real-agent tasks or external trace submissions were used. This establishes executable harness mechanics, not observed autonomous decision quality.
- The absence claims are bounded to the shipped five core tools and supported local runtime at this pinned revision. No inference is drawn from unimplemented README aspirations or independently composed agents outside the repository.
