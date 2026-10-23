---
harness_id: microcodex
project_name: MicroCodex
repository: https://github.com/paoloanzn/microcodex
review_ref: 8bd0f40d523f53b572a80c6540007b46a365f038
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

# MicroCodex

## Review boundary

- System in focus: the shipped single-process, C++23 MicroCodex coding agent, including interactive TUI, one-shot CLI, saved/resumed conversations, built-in tools, compaction and optional on-disk skill discovery.
- Purpose and identity: solve coding tasks in a local workspace through one configurable inference-backed tool loop, with the user as current task requester and optional cancellation/continuation operator.
- Relevant environment: source files and user goals, shell/compilation outcomes, API/tool errors, model context budgets, local saved transcripts, filesystem skills and user interruption.
- Standard-distribution boundary: the frozen standalone executable built from `main.cpp`, `api.cpp`, `agent.cpp`, tools, conversations, UI and local skill handling; a configured ChatGPT/Codex provider is inference infrastructure. Files, Git, shell, authentication and user-provided skills are external context/services rather than extra MicroCodex organizational decision owners.
- Credited operating / distribution surfaces: `main.cpp`, `agent.{h,cpp}`, `api.{h,cpp}`, `tool.cpp`, `bash.cpp`, `bash-safety.cpp`, `read.cpp`, `write.cpp`, `edit.cpp`, `glob.cpp`, `conversation.cpp`, `context-compaction.cpp`, `skills.cpp`, `ui.cpp`, `terminal.h`, `system-prompt.cpp` and the shipped CLI/TUI entrypoints.
- Adjacent first-party surfaces excluded from ownership: `tests/` Ruby loopback mock server/black-box CLI test fixtures, `.github` workflow/release metadata if present, `CONTRIBUTING.md`, installation/build scripts and issue/maintainer activity. They support product verification/distribution, not independently deciding functions during an end-user coding session.
- First-party operating / deployment modes considered: normal interactive terminal session, one-shot prompt, `resume` saved session, limited parallel tool-call batch within one model response, model-driven context compaction, optional skill catalog and operator interruption/continue.
- Recursion level: one local `CodexApi`/MicroCodex agent per coding conversation; parallel function calls are workers of the same S1 decision, not independently deciding daughter agents. Different CLI processes and repository contributors are outside this session's metasystem.
- Reviewed revision: `8bd0f40d523f53b572a80c6540007b46a365f038` (batch #1006 frozen row 4).
- License screen: root `LICENSE` provides Apache-2.0.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI initializes one `CodexApi` from the `makeCodingAgentConfig()` definition. That configuration supplies a coding system prompt, current local skill metadata and exactly five tools: `read`, `write`, `edit`, `glob` and `bash`. `sendUserMessage()` feeds the authenticated Responses API and loops over model-selected function calls; tool results and errors are appended to the same model conversation for continuation. A model response may carry multiple calls; `executeToolCalls()` dispatches them as C++ futures, then collects outputs in the original call order. These parallel tool executions have no separate prompts, goals, memories, deciding agents or coordinator.

Saved conversations append model/tool turns to local JSONL; optional checkpoints use model-generated summaries to keep the same ongoing task inside its context window. TUI/CLI controls can interrupt and later resume a single turn and change the requested work. The shell tool has a lexical denylist, but README explicitly cautions that it is not a sandbox. Local skill metadata is discovered from an operator-populated Codex skills directory and included in the current prompt; no first-party strategy agent monitors external futures or adopts new durable capabilities. Repository tests run the built executable against a fake loopback API, outside the installed organizational boundary.

Frozen primary sources: [README](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/README.md), [main](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/main.cpp), [coding tool configuration](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/agent.cpp), [model/tool loop](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/api.cpp), [skill discovery](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/skills.cpp), [tests boundary](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/tests/TESTS.md).

## Operational model

One model-backed coding cell decides tools and repairs based on response feedback (`S1=A`). Parallel C++ tool calls remain the implementation of that single agent decision and do not create distinct autonomous work cells (`S2=—`). Neither turn interruption, session history, context compaction, fixed skill catalog nor the shell safety denylist supplies current whole-system oversight, independent audit, future capability intelligence or ultimate identity governance (`S3/S3*/S4/S5=—`).

## S1 — Operations

- State: A
- Function: complete user coding requests by choosing file inspection/modification and shell operations and adapting to their outputs.
- Disturbance / variety regulated: differing repository state and tasks, model requests, errors from file/shell tools, unsuccessful commands, interrupted turns and changing user input.
- Decisive decision or feedback right: inference model selects registered `read/write/edit/glob/bash` calls, sees each result/error and can choose new actions or return a conclusion.
- Decision owner: configured model served by the external inference API, invoked through first-party `CodexApi`; fixed tool dispatcher is enforcement/support.
- Supporting / enforcement mechanisms: tool JSON schema, SSE Responses parser, output limits, tool-round and parallel-call limits, CLI/TUI events, local conversation checkpoints and optional compaction.
- Closure path: user request/context → model-chosen function calls → actual file/tool output or error → appended tool result → next model inference/tool choice or terminal reply.
- Boundary reachability: `main.cpp` builds `makeCodingAgentConfig()`, instantiates `CodexApi` and calls `sendUserMessage()` for one-shot or interactive operations. The shipped set of five real tools is registered through that path.
- Why this is / is not agent-owned: the model chooses task-specific operations and repairs from changing evidence; C++ dispatch and safety limits do not predetermine the coding solution.
- Evidence: [agent tools](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/agent.cpp), [tool execution loop](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/api.cpp), [CLI entry](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/main.cpp).
- Basis: frozen source plus native C++ build and read-only `--help` smoke; no model/provider test.
- Confidence: high for reachable autonomous S1 design.
- Caveats: a clean local build proves buildability, not task success or safe behavior under adversarial prompts; no real LLM was queried.

## S2 — Coordination

- State: —
- Function: no substantive first-party inter-S1 disturbance/attenuation loop exists within one installed MicroCodex conversation.
- Disturbance / variety regulated: multiple tool executions may touch overlapping files, but they are concurrently dispatched actions of the same model rather than conflicts between distinct deciding S1 units.
- Decisive decision or feedback right: one model chooses the batch; a fixed dispatcher enforces maximum call count and collects futures in order. No second work-cell decision owner or adaptive conflict mediator is established.
- Decision owner: one S1 model for the tool batch and deterministic runtime for futures; no independent S2 owner.
- Supporting / enforcement mechanisms: `std::async` function-call fan-out, bounded parallelism, response item accounting and error propagation.
- Closure path: tool call batch → fixed parallel execution → ordered returned outputs to the original model, which continues S1; no separate inter-autonomous-agent coordination adjustment.
- Why this is / is not agent-owned: the model may plan its own calls, but multiple tools or OS processes are not multiple independently deciding S1 systems.
- Evidence: [parallel tool dispatch](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/api.cpp), [tool registry](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/agent.cpp), [operating modes](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/README.md).
- Basis: exhaustive shipped tool registration and single-conversation control-path inspection.
- Confidence: high for scoped absence.
- Caveats: separate MicroCodex processes could be orchestrated externally, but are not joined by a first-party coordination organization here.

### Absence scope

- Surfaces inspected: first-party tool list, `CodexApi` loop and parallel futures, CLI/session lifecycle, conversation persistence, TUI and mock testing harness.
- Plausible first-party paths checked: asynchronous function calls as S2, saved conversations as independent workers, user-launched multiple processes, imported skills as an agent pool and cancellation as inter-agent arbitration.
- Why no material first-party path remains: no spawn/delegation registry or separate model-decision S1 units are created by installed runtime; fixed batch scheduling and one transcript are not an inter-S1 feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no separate agent/constructor/parent authority controls the whole of concurrently committed operational units inside a single coding session.
- Disturbance / variety regulated: a long-running tool or model call may need interruption and continuation, but there is one current task rather than a cohort of distinct S1 commitments requiring resource/prioritization control.
- Decisive decision or feedback right: a user can stop/resume the one turn, and runtime enforces tool/usage limits; neither has a current whole-system portfolio over which to exercise S3-specific allocation judgment.
- Decision owner: one S1 model and tactical human turn operator, not an independent S3 current-control owner.
- Supporting / enforcement mechanisms: `std::stop_token`, `stop_source`, tool maximums, task UI events and transcript resume.
- Closure path: cancellation or quota result changes/ends one running S1 turn; no current multi-unit resource or obligation decision is returned from a metasystem.
- Why this is / is not agent-owned: cancellation and retry are operational safeguards, not current-system governance over multiple action-owning units.
- Evidence: [turn lifecycle](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/api.cpp), [CLI commands](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/main.cpp), [terminal events](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/ui.cpp).
- Basis: first-party control surface and model topology review.
- Confidence: high for bounded negative.
- Caveats: operator authority over a task is real; it does not meet the Methodology's S3=P whole-current-function test at this recursion.

### Absence scope

- Surfaces inspected: `CodexApi` running-turn guards and cancellation, CLI one-shot/interactive/resume, TUI controls, maximum parallel tools, compaction and transcript state.
- Plausible first-party paths checked: user interrupt/continue as S3=P, concurrency cap as autonomous S3, tool-batch execution as a current portfolio and saved conversation browsing as whole-system visibility.
- Why no material first-party path remains: no concurrently deciding work-cell commitments are represented for discretionary whole-current coordination; controls affect an individual model turn or fixed execution limits.

## S3* — Complementary audit

- State: —
- Function: no first-party audit-specific independent claim review with alternative operational evidence and corrective return is packaged.
- Disturbance / variety regulated: mistaken coding changes and unsupported completion claims may occur, but the model's own test invocation and tool results are ordinary S1 evidence.
- Decisive decision or feedback right: no separate reviewer, independent sampling/inspection requirement, audit verdict or findings-to-correction owner is registered in the standard runtime.
- Decision owner: none established within the installed session; a user could independently commission review using another system.
- Supporting / enforcement mechanisms: shell test commands, saved transcript and error messages, test fixtures against the MicroCodex binary.
- Closure path: model requests/reads its own checks or user sees a transcript; no distinct complementary auditor selects operational evidence and returns a material verdict to corrective control.
- Why this is / is not agent-owned: the same model reading its own tool output or a maintainer running the package's tests is not an independent operating audit cell.
- Evidence: [registered tools](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/agent.cpp), [single-model agent loop](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/api.cpp), [black-box tests](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/tests/TESTS.md).
- Basis: installed agent/tool path and adjacent development-only validation scope.
- Confidence: high for bounded negative.
- Caveats: an external reviewer or user-supplied audit skill can be used outside this default system boundary.

### Absence scope

- Surfaces inspected: model/tool schemas, shell tool, saved conversations, UI, skills, black-box tests and developer feedback/release machinery.
- Plausible first-party paths checked: test execution as independent audit, self-review through the shell, user-resumed conversation as S3*, binary regression fixtures as live reviewer and imported review skills as a first-party audit constructor.
- Why no material first-party path remains: no distinct claim-relative operating auditor owns complementary inspection and returns findings into an operational control path. Development fixtures and user-authored skills cannot donate that owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established prospective external sensing, adaptation-option selection and future capability-change loop.
- Disturbance / variety regulated: future tasks might need different models/tools/skills, but inspected first-party mechanisms support only current model configuration and context management.
- Decisive decision or feedback right: the user selects model/effort and installs skills; task model reads relevant existing skills and asks for current coding actions. It does not govern acquisition/adoption of new reusable capabilities for anticipated environmental futures.
- Decision owner: operator for existing skill/model configuration; task model for current coding and compaction.
- Supporting / enforcement mechanisms: `skills.cpp` local metadata scan, `availableSkillsInstructions()`, lazy file reads, model context-limit discovery and model-generated compaction summary.
- Closure path: present session loads user-configured instructions or shrinks history for continuing the same task; no future-facing external alternatives are judged and durably adopted into operational capacity.
- Why this is / is not agent-owned: context compression is memory management and skill reading is configuration use, not future strategic adaptation.
- Evidence: [skills](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/skills.cpp), [compaction](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/context-compaction.cpp), [CLI model handling](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/main.cpp).
- Basis: first-party skills/model and context state analysis.
- Confidence: high for bounded negative.
- Caveats: user can extend capabilities outside the product's built-in strategic function.

### Absence scope

- Surfaces inspected: local skills search and prompt catalog, model selection, compaction, transcript persistence, API limits and README supported modes.
- Plausible first-party paths checked: Codex skill access as autonomous future acquisition, history summarization as long-term organizational learning, model switching as S4=P and external model catalog as environmental scouting.
- Why no material first-party path remains: all operate on immediate task context or user-provided choices, without prospective sensing/option judgment and return to changed future capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision cycle with governing authority and returned rule is established.
- Disturbance / variety regulated: unsafe shell commands and inappropriate modifications are possible; current lexical safety restrictions act only at execution time.
- Decisive decision or feedback right: developer-authored system prompt and bash denylist constrain ordinary tool use; user chooses goals/model and may interrupt. Neither processes an identity-level issue under a legitimate final-authority return channel.
- Decision owner: package developer and user for static preferences and tactical decisions, not a shipped S5 institution.
- Supporting / enforcement mechanisms: `codingAgentSystemPrompt()`, bash lexical denylist, credentials/endpoint configuration, process OS permissions, CLI operator and README safety disclaimer.
- Closure path: command candidate → fixed lexical check or current user control → execute/refuse, without policy dispute → ultimate decision owner → changed governing principle returned to subsequent operation.
- Why this is / is not agent-owned: current safety enforcement and an operator's single-task command do not decide the organization's ultimate mission or normative identity.
- Evidence: [prompt](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/system-prompt.cpp), [bash safety](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/bash-safety.cpp), [README scope](https://github.com/paoloanzn/microcodex/blob/8bd0f40d523f53b572a80c6540007b46a365f038/README.md).
- Basis: shipped instruction/enforcement boundaries and explicit safety disclaimer.
- Confidence: high for bounded negative.
- Caveats: human control over a terminal task is not, without an identity-level question and governing return, S5=P.

### Absence scope

- Surfaces inspected: system prompt, API configuration, safety gate, shell/user privileges, tool results, conversation commands, external provider login and contributor documentation.
- Plausible first-party paths checked: copied operating instructions as an internal constitution, bash policy as S5=A, user stop and model choice as S5=P, contributor/release controls as product-wide S5 of the installed coding session.
- Why no material first-party path remains: these constrain tool access or govern another recursion, but do not provide a session-level final identity authority deciding and feeding back ultimate-policy matters.

## Distributed OSS parent arrangement

MicroCodex's independent maintainers and users share public source but not a live project-level private agent organization. Repository governance, contributor conventions, tests and releases act on software development, not on the current terminal session's S3/S3*/S4/S5 decisions.

## Self-hosted and non-human modes

The local CLI and TUI let an attending user supply new work, interrupt execution and resume saved turns. Headless one-shot invocation runs the same model-owned S1 loop. Neither mode exposes first-party autonomous or parent-governed metasystem function over multiple current operational cells; an external automation wrapper is outside the reviewed standard distribution.

## Recursion

No first-party model-backed child-agent recursion is constructed. Parallel tool functions share the initiating model's conversation and return tool outputs to it; saved conversations are sequential time slices, not higher/lower organizational recursions.

## Variety and escalation

Tool and HTTP failures, context-limit retries, saved partial turns and user cancellation return to or interrupt the same S1 loop. No separate inter-S1 disturbance, current-portfolio supervision, complementary audit, prospective adaptation or identity-policy escalation is shown within the installed system.

## Evidence gaps

- Exact frozen revision `8bd0f40d523f53b572a80c6540007b46a365f038` and its pinned `vendor/md4c` and `vendor/termbox2` submodules were checked out. Local C++23 `make -j2` **PASS**, and compiled `./build/microcodex --help` **PASS** (offline, no provider).
- The bundled black-box script suite requires Ruby to serve deterministic loopback mock Responses. `make test` halted at the Ruby prerequisite (`Ruby is required`); Ruby was absent locally and on the accessible dev host. No suite-pass claim is made.
- No real LLM/provider session, tool execution through a model or interactive workflow was run. The grade describes first-party source ownership/closure, not coding success, operational safety or task quality.
