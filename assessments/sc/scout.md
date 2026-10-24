---
harness_id: scout
project_name: Scout
repository: https://github.com/dairycow/scout
review_ref: 1c7b51f4b03f719bedaf6a81dcdf896f6f39f806
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

# Scout

## Review boundary

- System in focus: the shipped first-party Python terminal coding-agent kernel and bundled plugins in `dairycow/scout` at frozen commit `1c7b51f4b03f719bedaf6a81dcdf896f6f39f806`.
- Purpose and identity: one model-controlled local coding/inspection session that can call tools, inspect feedback and revise further steps from a CLI or REPL.
- Relevant environment: current project, files and shell outputs, user prompt, installed project/user skills/plugins, model provider responses and local session history.
- Standard-distribution boundary: `scout` CLI, `host.boot`, synchronous bus, `Agent` model/tool loop, tool registry, shipped built-in tools/providers/config/session/skills/display/commands, and supported project/user plugin loading. Model endpoints, installed third-party/user plugins, target-project organization and user decisions remain outside Scout's ownership.
- Credited operating / distribution surfaces: `scout/{cli,host,agent,tools,bus,http}.py`, first-party `scout/builtin/` manifest and implementations, registered shell/read/write/edit/search/skill tools, configuration and SQLite session projection; project-local `.agents/plugins/topo.py` where explicitly loaded from the repository checkout.
- Adjacent first-party surfaces excluded from ownership: offline test suite and fake provider clients, `examples/` user-plugin and skill samples, development/build/release metadata, `docs/plans/` authoring materials and contributor governance. The repository-local Topo plugin is *not* packaged in the `scout-harness` installed Python module by `pyproject.toml`; it is reachable when operating with this checkout as the project directory, and is inspected separately rather than silently counted as an installed default.
- First-party operating / deployment modes considered: `scout` interactive REPL, `scout -p` headless one-shot, `scout -c` resume, `/clear` and `/fork`, built-in Anthropic/OpenAI-compatible providers, parallel and serial same-turn tool execution, layered configuration, project/user plugin/skill loading and repo-local Topo review mode.
- Recursion level: one running Scout agent session. Concurrent thread-pool tool invocations are action executions of the same model S1, and `/fork` constructs a new *history view*, not a simultaneously operating child agent.
- Reviewed revision: `1c7b51f4b03f719bedaf6a81dcdf896f6f39f806`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`cli.py` maps interactive, prompt and resume modes into one `host.boot` runtime. The host registers built-in plugins using the same `PluginApi` supplied to project/user Python plugins, resolves layered configuration, opens a session and constructs one `Agent`. The agent sends the session's message projection and registered tool schemas to its model client, receives model-selected tool calls, dispatches them, emits results on the event bus and repeats. A thread pool can execute multiple calls in one turn concurrently, but it reorders their results into the issuing model's call order; it does not create agents with their own prompts or decisions. Built-in tools cover shell, filesystem read/write/edit/search and loading skill bodies. A configured provider supplies inference, not an independently owned runtime organization.

`builtin/session.py` persists append-only event rows and rebuildable message projections in local SQLite; `/fork` copies a prefix into a different conversation ID, while `/clear` creates another empty conversation. Neither operation starts a new decision loop. Plugins can add commands, prompt text, tools, event listeners, providers and defaults; the distributor does not prescribe that external plugins own VSM functions. The source checkout includes `.agents/plugins/topo.py`, which opens an HTML plan in a browser and receives a human's annotations for the same coding agent to consider. It is real project-scoped feedback when running the checkout, but the audited object is a single plan artifact, not independent audit or governance of Scout's operational metasystem.

Pinned primary source:

- [`scout/agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/agent.py)
- [`scout/host.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/host.py)
- [`scout/tools.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/tools.py)
- [`scout/builtin/session.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/session.py)
- [`scout/builtin/tools/__init__.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/tools/__init__.py)
- [`.agents/plugins/topo.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/.agents/plugins/topo.py)
- [`tests/test_agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/tests/test_agent.py)

## Operational model

The provider-guided Scout session is one adaptive S1: the model decides the next code/files/shell action, receives its success or error and decides the next turn or final response. The host deterministically executes selected tools, orders result messages, stores session history and enforces a turn cap. Human user prompts, user-defined plugins and project-specific instruction files are inputs or delegated configurations, not independent first-party S2–S5 owners. No packaged native subagent or worker-team controller was found; temporary concurrency of tools, forked saved histories and the project checkout's human Topo comments were individually examined to avoid inflating higher-function claims.

## S1 — Operations

- State: A
- Function: achieve local coding/inspection goals by choosing tool actions and revising them after execution feedback.
- Disturbance / variety regulated: novel user requests, unknown source structure, shell/file errors, available skill context and changed tool results.
- Decisive decision or feedback right: model chooses registered tool names and arguments on successive calls, revising actions or terminating after observed outcomes.
- Decision owner: the live provider-backed `Agent` model/tool conversation; the external user sets the task and plugin/provider context.
- Supporting / enforcement mechanisms: registered tools and provider adapters, event bus, SQLite message projection, optional concurrent tool dispatch, config/skills prompting, tool-error return and turn bound.
- Closure path: user prompt and session messages → model selects tool calls → registry executes first-party handlers → result/error events project into conversation → model observes changes and chooses another action or answer.
- Boundary reachability: both interactive and `-p` paths construct the same `Agent` in `host.boot`; default built-in providers and native tools are registered by its shipped plugin manifest. The offline fake-client test directly exercises the tool-result feedback loop and error retries.
- Why this is / is not agent-owned: model choice is not predetermined by the CLI or registry; execution feedback changes subsequent model-selected actions, satisfying local adaptive operations. Executor concurrency does not create additional owners.
- Evidence: [`scout/cli.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/cli.py); [`scout/agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/agent.py); [`scout/host.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/host.py); [`tests/test_agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/tests/test_agent.py).
- Basis: explicit + structural + deterministic fake-client script tests.
- Confidence: high for shipped decision/feedback architecture.
- Caveats: no real LLM-agent run or measured repair effectiveness; after allowing localhost sockets for HTTP unit tests, 127 first-party tests passed.

## S2 — Coordination

- State: —
- Function: no distinct agent-owned or constructed interference-damping function between independent Scout S1 units is shipped.
- Disturbance / variety regulated: simultaneous tool execution can affect files/processes, but all calls originate from one model turn and are not independently deciding S1 units.
- Decisive decision or feedback right: the single model chooses the multi-tool call set; executor threads only run and reassemble the calls.
- Decision owner: same `Agent` model loop and deterministic thread-pool/registry dispatch.
- Supporting / enforcement mechanisms: `parallel_tools`, `ThreadPoolExecutor`, ordered result IDs, synchronous bus event delivery, `/fork` session view copying.
- Closure path: tool results return to the same S1; no independent-S1 conflict signal → dedicated coordination action → distinct S1 behavior change is wired.
- Why this is / is not agent-owned: concurrent *tools* and forked *conversation storage* are not concurrently operating independent agents; result ordering is implementation consistency rather than S2 interference control.
- Evidence: [`scout/agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/agent.py); [`scout/builtin/session.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/session.py); [`tests/test_agent.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/tests/test_agent.py).
- Basis: explicit plus full small-source negative review.
- Confidence: high.
- Caveats: users could add independently operated agents with custom plugins; their unseen behavior is outside this first-party boundary.

### Absence scope

- Surfaces inspected: CLI, host plugins, model loop, tools, thread pool, event bus, session fork, bundled providers and repo-local Topo.
- Plausible first-party paths checked: agent delegation, multi-session parallelism, thread-pool cross-agent arbitration, fork as child dispatch and external tool/plugin coordination.
- Why no material first-party path remains: one `Agent` is constructed, parallel dispatch lacks separate decision loops, and `/fork` only changes the saved message projection; no first-party inter-S1 coordinator is shipped.

## S3 — Inside-and-now control

- State: —
- Function: no metasystem-level live resource/commitment/prioritization control over a portfolio of S1 units is established.
- Disturbance / variety regulated: turn limits, provider retries and plugin failures are one-session technical constraints rather than organizational current-management conflicts.
- Decisive decision or feedback right: user starts/resumes sessions and selects provider/tool settings; no whole-current management decision actor.
- Decision owner: one operating agent and operator CLI, without separate S3 responsibility.
- Supporting / enforcement mechanisms: max turns, config layering, REPL session commands, statusline, token usage and event log.
- Closure path: session/tool feedback drives the same S1; no all-units current view → management priority/resource intervention → returned operation change circuit.
- Why this is / is not agent-owned: model changing tasks and operator configuration are local operations, not substantive S3 current-control ownership, even under a parent-mode test.
- Evidence: [`scout/host.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/host.py); [`scout/cli.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/cli.py); [`scout/builtin/statusline.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/statusline.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: repo-local Topo human approval of a *plan artifact* is not an operator's whole-current portfolio management.

### Absence scope

- Surfaces inspected: `Runtime`, CLI/REPL controls, session/store, config, usage/statusline, project Topo and fake-agent tests.
- Plausible first-party paths checked: all-agent dashboards, budget allocation, multi-agent commitment revision, parent approval of whole-system actions and operational loop caps as controls.
- Why no material first-party path remains: source has a single session's task loop; no S3-specific whole-current decision scope or correction returned to a population exists.

## S3* — Complementary audit

- State: —
- Function: no independent checking of management or operational claims through complementary reality access and authorized corrective return is packaged.
- Disturbance / variety regulated: test/tool errors, event history and human artifact comments can challenge local outputs but do not constitute independent organizational audit.
- Decisive decision or feedback right: no separate auditor with mandate and corrective management return.
- Decision owner: same operational model consumes tool errors; in checkout mode, a human can comment on an HTML plan using Topo.
- Supporting / enforcement mechanisms: event bus, persistent history, developer offline tests and Topo `topo_write`/`topo_open`/`topo_feedback` review channel.
- Closure path: tool results or human Topo notes reenter the existing task conversation; no independent claim-vs-reality audit → responsible S3 decision owner → oversight correction path.
- Why this is / is not agent-owned: first-party Topo human feedback is genuinely separate from model output, but reviews a plan artifact, not independently assesses management claims against operational reality; development tests and logs are ordinary evidence.
- Evidence: [`.agents/plugins/topo.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/.agents/plugins/topo.py); [`scout/bus.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/bus.py); [`scout/builtin/session.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/session.py).
- Basis: explicit + structural absence review, including project-local review mode.
- Confidence: medium-high.
- Caveats: an externally designed independent auditor using plugin hooks could differ; none is shipped as Scout's own S3* circuit.

### Absence scope

- Surfaces inspected: Topo plugin server/browser feedback, SQLite events and rebuilding, tool-error return, built-in tools, repository tests and user/plugin API.
- Plausible first-party paths checked: browser human review as audit, separate test-based verifier, event-driven auditing plugin, history integrity checking and independent management escalation.
- Why no material first-party path remains: available checks and comments concern a single task/output; no distinct auditor mandate, independent live operational evidence route, and returned S3 correction path coexist.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future-environment sensing and selected adaptation of the agent's enduring capabilities is closed.
- Disturbance / variety regulated: new files, provider choices and project skills are present-context inputs; long-term external changes are not modeled and acted upon through a prospective capability loop.
- Decisive decision or feedback right: operator installs/edits skills/plugins or changes config; one agent chooses present tool calls.
- Decision owner: external author/installer for durable capabilities and the current S1 for task actions.
- Supporting / enforcement mechanisms: `.agents/` skill discovery, plugin loading, config layering, persisted history, `/fork`, Topo plan artifacts.
- Closure path: external instructions/plugins load at boot and may influence the present model; no observed future distinction → candidate capability changes → selected implementation → validated later return is shipped.
- Why this is / is not agent-owned: memory, provider switching and user-authored modules expand action possibilities without a first-party prospective adaptation decision owner.
- Evidence: [`scout/builtin/skills.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/skills.py); [`scout/host.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/host.py); [`scout/builtin/session.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/session.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a model could be asked to write a plugin as a coding task, but task output alone does not make a standing S4 adaptation cycle.

### Absence scope

- Surfaces inspected: skills/prompt loading, plugin registrations, session history/fork, provider settings, repo-local Topo, built-in command/help and tests.
- Plausible first-party paths checked: autonomous skill self-improvement, retained lessons as future capability changes, external trend sensing and strategy selection, installed plugin mutation and user-led parent S4 governance.
- Why no material first-party path remains: load/selection uses pre-existing artifacts/config; the kernel has no prospective planning, trial, authorization and persistent capability-update return loop.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate purpose/identity-policy governance circuit is implemented in first-party Scout.
- Disturbance / variety regulated: operator-provided project instructions and tool/provider configuration shape allowed tasks but not ultimate organizational dilemmas.
- Decisive decision or feedback right: user starts and directs coding work; no issue-to-policy authority-and-return channel.
- Decision owner: external user/maintainer for repository purpose, plugin installation and optional model credentials.
- Supporting / enforcement mechanisms: `AGENTS.md` prompt injection, model/provider configuration, user-installed plugins, REPL commands and runtime error handling.
- Closure path: settings and prompts affect S1 actions; no legitimate identity-policy question → authority deliberation → binding governance decision → operational return.
- Why this is / is not agent-owned: system prompt and installed plugin commands are externally chosen task constraints, not S5 policy adjudication; the absence of permission prompts does not establish a policy owner either.
- Evidence: [`scout/builtin/prompt.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/builtin/prompt.py); [`scout/host.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/host.py); [`scout/cli.py`](https://github.com/dairycow/scout/blob/1c7b51f4b03f719bedaf6a81dcdf896f6f39f806/scout/cli.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: real maintainer/user governance exists outside the declared agent runtime.

### Absence scope

- Surfaces inspected: CLI/host settings and startup, AGENTS prompt handling, built-in command/help, provider/credential selection, external plugin interface and first-party project Topo review.
- Plausible first-party paths checked: standing purpose amendments, legitimate parent S5 mandate, role/authority changes, plugin permission rules as policy and human plan review as governance.
- Why no material first-party path remains: no shipped authority path owns ultimate organizational disputes or returns binding identity-policy decisions; task choices remain local and owner-external.

## Recursion

One model/tool S1 is closed. Same-turn tool threads are actions of that S1, not separate agents. `/fork` copies a conversation prefix but does not launch another live autonomous decision unit. A user can run multiple independent Scout processes outside the first-party installed runtime's internal management, but no Scout-owned coordination hierarchy is supplied for them.

## Variety and escalation

The model/tool loop and project-defined plugins can amplify operational variety; `max_turns`, output clipping, provider timeouts/retries and deterministic tool dispatch bound resources and failure propagation. Errors return to the same model. REPL commands and Topo browser comments can introduce operator feedback for the task; neither establishes an elevated S2–S5 escalation owner.

## Evidence gaps

- Entire frozen first-party test suite passed **127/127** with a local loopback exception for Topo HTTP tests. The restricted sandbox initially blocked five socket-binding checks (`PermissionError`) despite 122 other passes; re-running the same suite with permitted 127.0.0.1 loopback yielded 127 passes. All provider responses in tests are fakes; no LLM-agent call was performed.
- The shipped Python package excludes `.agents/plugins/topo.py`; it is first-party project-local and automatically loaded only in a checkout used as the working project (or if independently installed). Its HTML plan review feedback was inspected and not promoted to an organizational audit/S3 claim.
- The negative states concern standard first-party distribution and declared project-local mode, not externally authored plugins or custom higher-level organizations users might assemble from PluginApi.

## Assessment summary

Scout operates one first-party model-guided terminal coding session that chooses tool actions and revises them after returned results (`S1=A`). Parallel tool execution, persisted/forked conversation histories, plugin extensibility and optional checkout-local Topo human review do not by themselves provide distinct-S1 coordination, whole-current management, complementary organizational audit, prospective capability adaptation or legitimate identity-policy governance.

Proposed vector: **`A · — · — · — · — · —`**
