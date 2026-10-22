---
harness_id: devon
project_name: Devon
repository: https://github.com/entropy-research/Devon
review_ref: 8f68f1d7467161562d64138aefee7d26c7e68130
reviewed_at: 2026-10-22
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

# Devon

## Review boundary

- System in focus: a locally operated Devon coding-assistant session running the published `devon_agent` backend with its supported desktop or terminal client, rather than the entropy-research developer community or its SWE-bench experiment.
- Purpose and identity: accept a user's development task, inspect and modify a local project through shell/editor/search tools, and ask for user guidance or another task as needed.
- Relevant environment: the user's project tree and git branch, shell/tool responses, provider-generated model output, user corrections, and session state exposed over the local server.
- Standard-distribution boundary: `pipx install devon_agent` plus `npx devon-ui` or `devon-tui`, as instructed by the pinned README; backend `devon_agent/server.py` creates one `Session` and one `ConversationalAgent` per request, with local shell and user environments. Optional session git-versioning and persistence modes are included when configured.
- Credited operating / distribution surfaces: `devon_agent/session.py`, `agents/conversational_agent.py`, `server.py`, `config.py`, `environments/{shell,user}_environment.py`, registered tools, versioning support, and first-party terminal/desktop UI control calls.
- Adjacent first-party surfaces excluded from ownership: `devon_swe_bench_experimental/` alternative benchmark pipeline, `evals/`, unit tests and test fixtures, developer roadmap/contributor process, and provider-side language models. The unused `TaskAgent` class is not instantiated by the normal `Session` path.
- First-party operating / deployment modes considered: normal interactive backend with TUI/desktop UI; pause/resume/revert/interrupt; optional git-branch/checkpoint/merge flow; persisted/restored session; optional local model endpoint. The benchmark experiment is an adjacent evaluation mode, not silently borrowed into the standard interactive session.
- Recursion level: one Devon-assisted coding session, with one conversational agent and its tool/user/environment loop. Other sessions in the server are peers, not established autonomous operational suborganizations.
- Reviewed revision: [`entropy-research/Devon@8f68f1d7467161562d64138aefee7d26c7e68130`](https://github.com/entropy-research/Devon/tree/8f68f1d7467161562d64138aefee7d26c7e68130), frozen in [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-22; frozen source and documentation inspection, with no model-provider or LLM-agent execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The README installs a Python agent backend and a separately launched web/terminal UI. The FastAPI backend creates a `Session` from a project path, a model selection, a local shell environment and a user-response environment; the session constructor instantiates exactly one `ConversationalAgent` for the supported `agent_type="conversational"`. Tools registered for that agent include file creation/open/edit/delete, file and code search, navigation, directory/tree display, shell fallback and `ask_user`. The UI submits user messages and can request lifecycle actions through the server API.

The event loop consumes `Task`, `ModelRequest`, `ModelResponse`, `ToolRequest` and `ToolResponse` records. An agent prediction reads its chat history and current file observations, generates one command, and passes it back to the session; the session runs a registered tool or a shell command and feeds the response into the next model request. This is an actual source-level discretionary operational loop; no quality or benchmark result is needed to establish its ownership topology.

Optional git mode isolates work on `devon_agent`, makes checkpoints and exposes user-mediated branch/merge/error handling. The server's `sessions` mapping and persistence database retain sessions but do not assign management decision rights to a strategic or audit unit. TUI/desktop status, interrupts, pause, revert, merge and user questions are session controls, not by themselves distinct S1 managers. A separate `devon_swe_bench_experimental/` contains benchmark infrastructure; the pinned README advertises the interactive `devon_agent` installation, so the experiment's model/role claims are not imported into this recursion.

Primary evidence: [README](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md), [server session creation](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L239-L301), [session constructor and tools](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L106-L158), [event dispatch](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L788-L1110).

## Operational model

The user supplies or revises a coding goal. One conversational agent chooses the next tool command using the current observation and project context; deterministic session machinery parses, dispatches and returns observations. The agent's action choice, including continuing to inspect or edit files after tool feedback, is the relevant autonomous S1 right. The human may interrupt, answer `ask_user`, pause, revert or merge; these are first-party operator controls but do not demonstrate a second operational cell, whole-system management, complementary management audit, future adaptation, or ultimate-policy adjudication at the assessed session boundary.

## S1 — Operations

- State: A
- Function: perform the current software-development task through discretionary codebase inspection, tool commands, edits and follow-up actions.
- Disturbance / variety regulated: incomplete task description, unknown source layout, tool errors, partial code changes, test/command observations and changing user instructions.
- Decisive decision or feedback right: the `ConversationalAgent` generates the next `<command>` from the current observation, conversation and visible editor state; subsequent responses feed another `ModelRequest`.
- Decision owner: the model-driven `ConversationalAgent` in the standard supported session; the runtime, local tools and provider interface supply execution and feedback rather than choose the task-local next action.
- Supporting / enforcement mechanisms: generated command documentation, registered editor/search/shell tools, prompt/response parser, event log, session persistence, git checkpoints and user-response tool.
- Closure path: user task → `ModelRequest` → agent command → `ModelResponse` → parsed `ToolRequest` → tool or shell result → `ToolResponse` → next `ModelRequest` and revised action.
- Boundary reachability: `server.create_session` explicitly selects `agent_type="conversational"`; `Session.__init__` instantiates that agent and `run_event_loop` dispatches its output through the installed first-party toolchain. This is the regular backend path used by both advertised UI clients.
- Why this is / is not agent-owned: the model response chooses among operations and constructs tool arguments. The event router executes those choices but does not substitute a predetermined action list for the agent's judgment.
- Evidence: [agent prediction and response parsing](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/agents/conversational_agent.py#L172-L281), [session event cycle](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L845-L1107), [tool registration](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L121-L150).
- Basis: explicit source structure and reachable runtime control flow.
- Confidence: high for S1 ownership; no claim about model competence or successful completion of particular programming tasks.
- Caveats: the model provider is external, and no live model, user session, benchmark or LLM-agent quality run was executed for this assessment.

## S2 — Coordination

- State: —
- Function: attenuate an evidenced interference or oscillation between distinct operational S1 units and return the correction into their subsequent activity.
- Disturbance / variety regulated: hypothetical incompatible edits or competing delegated workers; no such distinct operational cells are shipped in the supported session.
- Decisive decision or feedback right: none for a conflict-specific inter-S1 relation. Tool dispatch and session/event sequencing do not adjudicate incompatible commitments between independent operational cells.
- Decision owner: no qualifying S2 owner in the reviewed standard mode.
- Supporting / enforcement mechanisms: single-agent event queue, multiple tool implementations, session map and UI communication; these route or execute one agent's work.
- Closure path: tool response → same agent's next step is an S1 feedback loop, not inter-S1 interference sensing → attenuation → changed behavior in multiple S1 cells.
- Why this is / is not agent-owned: there is one instantiated conversational agent per session; naming multiple tools, saved sessions or an unused task-agent class does not create interacting S1 units and a conflict-damping loop.
- Evidence: [single-agent session construction](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L106-L150), [server session topology](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L51-L58), [tool routing](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L902-L1030).
- Basis: inspected complete standard session wiring; bounded negative.
- Confidence: high for the reviewed interactive distribution.
- Caveats: a third party could build multi-agent coordination around Devon, but that hypothetical composition is not shipped or credited here.

### Absence scope

- Surfaces inspected: normal agent constructor, session event router, registered tools, server session table, optional git flow, README client instructions and TUI event input.
- Plausible first-party paths checked: second agent role activation, sibling-agent conflict reports, session-level inter-worker arbitration and test/reviewer tool effects.
- Why no material first-party path remains: the reachable mode creates one conversational agent with tools; separate sessions have no cross-session conflict-regulating owner, and neither sequencing nor branch isolation constitutes S2-specific feedback.

## S3 — Inside-and-now control

- State: —
- Function: govern present-wide operating priorities, resources, commitments and accountability at the session's recursion.
- Disturbance / variety regulated: task interruptions, working-tree divergence, pauses, checkpoints and provider errors; these are handled by session lifecycle and local recovery mechanisms without a distinct whole-current governance loop.
- Decisive decision or feedback right: the user can pause/revert/merge and choose git-resolution actions, while the backend deterministically changes a session's state; no present-wide management decision with a comprehensive view and discretionary trade-off across S1 commitments is established.
- Decision owner: session operator for local controls and deterministic backend for their enforcement, neither evidenced as a qualifying closed S3 governance arrangement.
- Supporting / enforcement mechanisms: `status`, `checkpoints`, `git_setup`, `revert`, `merge`, API endpoints for pause/start/revert and persistent event history.
- Closure path: operator lifecycle action → session state/branch transition → resumed or stopped single-agent operation; missing the whole-current managerial sensing, resource/commitment judgment and corrective control required for S3.
- Why this is / is not agent-owned: the conversational agent chooses code operations, not organization-wide prioritization or resource commitments. A git safeguard, timeout, checkpoint or lifecycle endpoint executes a preconfigured local action; it does not own S3.
- Evidence: [session status/checkpoints](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L218-L265), [git setup and user decisions](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L267-L433), [server lifecycle endpoints](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L332-L472).
- Basis: bounded first-party runtime negative after checking plausible supervisory parent mode.
- Confidence: medium-high; the supported UI can steer task-local state but does not demonstrate whole-current S3.
- Caveats: users may externally manage multiple Devon sessions or a development team; that independent human organization is outside the assessed session boundary.

### Absence scope

- Surfaces inspected: server session registry and lifecycle APIs, `Session` state/control/git/recovery flows, `Config`, user-response environment and advertised UI.
- Plausible first-party paths checked: server-wide scheduling and resource assignment, agent manager rights, git/checkpoint decision ownership, operator pause/merge/revert as candidate `P` S3 mode.
- Why no material first-party path remains: no shipped component builds a whole-current management view and decides competing resources/commitments or returns a management correction; controls affect an individual task/session and git safety only.

## S3* — Complementary audit

- State: —
- Function: independently inspect operating and management claims through a complementary reality-access route and return an audit judgment for current-management correction.
- Disturbance / variety regulated: possibly mistaken agent completion or inaccurate self-report; local tool/test observations are made available to the same agent or user rather than a separate complementary manager-auditor.
- Decisive decision or feedback right: no S3 management-claim audit owner, independently sourced verdict, or return-to-S3 correction path in the shipped session.
- Decision owner: none evidenced at the assessed recursion.
- Supporting / enforcement mechanisms: tool output, logs, test commands the agent may choose, and UI status/checkpoint views; these are ordinary S1 feedback/observability facilities.
- Closure path: shell/test output → same conversational agent's next operation; no complementary inspection → audit judgment about S3 → management correction.
- Why this is / is not agent-owned: an operational test or a user-visible event stream is not an independent S3* audit. The optional git revert is not an independent reality-assessment function.
- Evidence: [single agent and tool model](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L106-L150), [ToolResponse feedback](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L1049-L1097), [event stream](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L519-L549).
- Basis: bounded standard-runtime negative.
- Confidence: high for absence of an independent complementary audit path in the assessed session.
- Caveats: a human could manually review Devon's output; this is not a packaged complementary management-audit loop.

### Absence scope

- Surfaces inspected: agent/runtime wiring, local tools and results, server events and user interaction, git checkpoints and unit/evaluation adjacent files.
- Plausible first-party paths checked: verifier/reviewer-agent invocation, independent instrumentation or system-inspection path, audit verdict routing into whole-current S3.
- Why no material first-party path remains: only the same agent consumes tool feedback; no independent audit judgment or management-return owner is shipped, and no positive S3 function was established to audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: sense external and future environmental shifts, create strategic capability options and feed an adopted option back into current operations.
- Disturbance / variety regulated: future technology, evolving code patterns and changing provider capabilities; current source/code retrieval serves the present task instead of a standing forward-looking adaptation loop.
- Decisive decision or feedback right: no first-party prospective option evaluation and adoption right is connected to the running session.
- Decision owner: public roadmap/model-support choices belong to maintainers outside the assessed runtime; the conversational agent owns present-task searches only.
- Supporting / enforcement mechanisms: code search/index tools, configurable model name and endpoint, maintenance roadmap and benchmark files.
- Closure path: external project text → present code task is S1 context gathering; no future-sensing → option selection → persistent capability change → return-to-operation S4 loop.
- Why this is / is not agent-owned: model configuration by an operator and one-off code search do not close an outside-and-then strategic adaptation function.
- Evidence: [supported model selection in server](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L239-L310), [code-search tool registration](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/session.py#L121-L150), [README roadmap](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md).
- Basis: bounded negative with separate developer governance.
- Confidence: high for the reviewed standard deployment.
- Caveats: a maintainer may develop Devon over time; repository evolution is not evidence of a shipped autonomous or parent-closed S4 function.

### Absence scope

- Surfaces inspected: agent prompt/prediction, session loop, model selection, server settings, code index/retrieval, published README and benchmark/development-adjacent surfaces.
- Plausible first-party paths checked: persistent learning or model policy adaptation, future-environment sensing, benchmark-to-runtime improvement decision, operator strategic-option approval.
- Why no material first-party path remains: search and configuration support the active coding task; no supported prospective option-and-adoption return loop exists inside the assessed session.

## S5 — Policy and identity

- State: —
- Function: legitimately resolve disputes over ultimate system purpose and governing identity/policy, with binding return into operation.
- Disturbance / variety regulated: conflicting human instructions and proposed code actions; the installed prompts and user task constrain a session but do not form an ultimate-policy adjudication mechanism.
- Decisive decision or feedback right: user supplies tasks and answers questions; `ask_user`, update-config and interrupt can adjust immediate goals, not demonstrate an explicit identity-level policy arbitration and returned binding rule.
- Decision owner: human/operator for ordinary instructions, developer for static prompt and application policy; no qualifying closed S5 right is established in the supported runtime mode.
- Supporting / enforcement mechanisms: model system prompts, parsed `ask_user` tool, user environment, interrupt/API message routes and session lifecycle.
- Closure path: user instruction → agent action is ordinary task direction; there is no shipped policy dispute escalation → legitimate ultimate-policy verdict → changed governing constraints and return-to-operation path.
- Why this is / is not agent-owned: the model's command selection is S1 discretion, not authorship or adjudication of the system's identity; generic human prompting does not by itself establish `S5=P`.
- Evidence: [user tool](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/tools/usertools.py#L70-L108), [user response environment](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/environments/user_environment.py#L23-L43), [server interrupt/event input](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/server.py#L497-L517), [agent prediction](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/devon_agent/agents/conversational_agent.py#L172-L255).
- Basis: bounded negative after checking the plausible parent-controlled instruction and configuration modes.
- Confidence: medium-high; static prompts and task/user corrections are visible, identity-policy ratification is not.
- Caveats: organizational policies governing the real user or contributor community are outside the one-session boundary.

### Absence scope

- Surfaces inspected: agent/user prompts, `ask_user` and interrupt flow, session/task/state mutation APIs, operator settings and developer governance references.
- Plausible first-party paths checked: autonomous ultimate-policy amendment, explicit parent policy-decision return through UI, configured governing identity/policy changes and policy escalation from tool execution.
- Why no material first-party path remains: first-party interaction updates immediate task and configuration, but does not establish an identity-level dispute, legitimate final policy decision or durable binding governance return loop.

## Distributed OSS parent arrangement

Devon's contributors publish code, releases and a roadmap, but the first-party interactive agent distribution does not wire those maintainers as a runtime management/strategic/policy parent. Their outside development and governance cannot be borrowed to assert `S3=P`, `S4=P` or `S5=P` for a particular Devon session.

## Self-hosted and non-human modes

Local server and terminal/desktop clients support user-steered operation with several model providers and an experimental local model option. A human can pause, interrupt, revert and merge; these are operational controls and do not automatically upgrade S3/S4/S5 parent modes. The model still owns next code/tool-action selection for S1. No supported standalone non-human multisession S2–S5 organization is established at this revision.

## Recursion

One session contains an agent and instrumental tools, not recursively viable independent S1 suborganizations. The server can host multiple sessions but provides no first-party higher-recursion feedback governance tying them into one viable multi-session operating system.

## Variety and escalation

Devon absorbs changing code-task variety through conversational model instructions, repository actions and returned local observations. `ask_user`, interrupts and git conflict/error prompts expose human assistance and session recovery. There is no specific inter-S1 damping loop, whole-current control function, complementary managerial inspection, outside-future adaptation or ultimate-policy escalation with a demonstrable return path.

## Evidence gaps

- S1 is structurally reachable from packaged runtime code; no model or SWE-bench quality result is claimed and no LLM-agent/model-provider test was executed.
- The complete published normal backend path is adequate for **bounded** negative S2–S5 judgments. Those negatives are not universal claims about future Devon versions, private enterprise wrappers or third-party multi-agent integrations.
- `TaskAgent` and `devon_swe_bench_experimental/` are adjacent/unwired in the documented normal `Session` path; their existence does not override the standard-distribution boundary.
- A user's manual code review, strategic product decisions and policy governance could exist externally; no first-party closure into an eligible S3/S3*/S4/S5 ownership mode is shown here.
