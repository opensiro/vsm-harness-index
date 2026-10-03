---
harness_id: tyrion
project_name: Tyrion
repository: https://github.com/Xtejasveer/tyrion
review_ref: 35806697ba873e069b6ec6346216baea8b94a72f
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Tyrion

## Review boundary

- System in focus: the first-party `Xtejasveer/tyrion` terminal coding-agent distribution at frozen revision `35806697ba873e069b6ec6346216baea8b94a72f`, including the pure model/tool loop, stateful `AgentHarness`, `CodingSession`, shipped coding tools, session persistence/tree restoration, context compaction, CLI/TUI surfaces and the provider abstraction where they bear on organizational function.
- Purpose and identity: execute software-engineering tasks against one local workspace by letting a model inspect files, edit code, run shell commands, observe results and iterate until it can finish the requested task.
- Relevant environment: the selected project workspace and repository files, user task, shell/process environment, project instructions such as `AGENTS.md`, provider/model responses, model context limits and persisted conversation/session state.
- Standard-distribution boundary: the shipped `tyrion` CLI/TUI, `run_agent_loop`, `AgentHarness`, `CodingSession`, first-party read/write/edit/bash tools, prompt/context/session machinery and provider adapter are inside. OpenAI-compatible model providers, Ollama/vLLM servers, the host OS/shell, target project policy and external project code are dependencies/environment rather than Tyrion organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `src/tyrion_agent/loop.py`; `src/tyrion_agent/harness.py`; `src/tyrion_coding/session.py`; `src/tyrion_coding/session_coding.py`; directly reached first-party coding tools/system-prompt/session surfaces.
- Adjacent first-party surfaces excluded from ownership: `evals/` benchmark fixtures, metrics and optional DeepEval/OpenRouter judge; repository CI/release/development tooling; tests; contributor/development governance. These surfaces may corroborate behavior but are not wired into the supported coding runtime as organizational decision owners.
- First-party operating / deployment modes considered: interactive TUI sessions, one-shot CLI prompts, session resume/continue, automatic/manual context compaction and normal model/tool coding runs through the standard `CodingSession`/`AgentHarness` path.
- Recursion level: one Tyrion coding organization around one user task/workspace. The model-backed loop is the single primary operating S1 at this recursion. The stateful harness supervises execution of that same S1 and does not instantiate a separate operational unit merely because it is named a harness/supervisor.
- Reviewed revision: `35806697ba873e069b6ec6346216baea8b94a72f`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Tyrion separates a stateless model/tool loop from stateful runtime/session concerns. `run_agent_loop()` repeatedly asks the configured model for a response, executes any returned tool calls, appends tool results to the transcript and feeds those results into the next model turn until the model stops calling tools or an external cancellation/max-turn condition ends the run. Tool calls inside a turn are executed sequentially.

`AgentHarness` wraps that loop with transcript ownership, cancellation, listener/event dispatch, overlap prevention and repair of interrupted tool-call history. It explicitly rejects overlapping runs of the same harness instance. `CodingSession` then adds the coding-specific tool set, system prompt, append-only session persistence, restoration and context compaction. Compaction is a present-session continuity mechanism: when context pressure crosses a threshold, the same configured provider summarizes older conversation history and the runtime resumes from the compacted session state.

The repository also contains an `evals/` development/evaluation harness. Its deterministic metrics and optional LLM judge can score isolated coding tasks, and the judge is recommended to use a different model family than the generator. That surface is development-time/offline evaluation rather than part of the supported `tyrion` runtime path: normal installs do not require the evaluation dependencies, and runtime coding operations do not consume evaluator verdicts to regulate subsequent work.

Primary evidence:

- [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md)
- [`src/tyrion_agent/loop.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/loop.py)
- [`src/tyrion_agent/harness.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/harness.py)
- [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py)
- [`evals/judge.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/evals/judge.py)

## Operational model

A supported run starts with a user task and a project-scoped coding session. Tyrion constructs the system/tool context and the model chooses either a final response or one or more tool calls. The first-party loop executes each requested tool call, records the result and returns that evidence to the same model-backed actor on the next turn. File contents, edit results, shell output and failures therefore become closed-loop feedback for later coding choices.

The surrounding runtime preserves and repairs transcript state, allows an operator to cancel work, limits turns when configured and can compact old context. Those mechanisms support the coding S1 but do not establish additional VSM functions by themselves.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected workspace by interpreting a task, inspecting project evidence, choosing coding actions, applying edits/commands and reacting to the resulting feedback.
- Disturbance / variety regulated: heterogeneous repository structure and code, incomplete task information, file contents, command/test outcomes, tool failures, model/provider feedback and changing workspace state encountered while solving the coding task.
- Decisive decision or feedback right: choose which available coding tool/action to invoke next, which project evidence to inspect or modify, and when the task has enough evidence/work to terminate with a final response.
- Decision owner: the model-backed actor driven through Tyrion's first-party `run_agent_loop` in the standard `CodingSession`/`AgentHarness` path.
- Supporting / enforcement mechanisms: `AgentHarness`; coding tool registry; system/project prompt construction; transcript/session persistence; cancellation; max-turn enforcement; context compaction; provider/model adapter; CLI/TUI event rendering.
- Closure path: user task/workspace context → model response and selected tool call → first-party tool execution against the workspace → tool result appended to transcript → same model-backed actor receives the result on the next turn → revised action or final response.
- Boundary reachability: `tyrion` interactive and one-shot entry points instantiate the shipped coding session/harness and tool loop directly; an application author does not have to compose a separate agent runtime to obtain this operating loop.
- Why this is / is not agent-owned: removing the model-backed decision actor while leaving the tool/session/harness machinery intact removes the open-ended coding judgment that selects and sequences repository-facing operations.
- Evidence: [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md); [`src/tyrion_agent/loop.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/loop.py); [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference itself is supplied by an external compatible provider; Tyrion is credited for the first-party role/tool/feedback composition that operationally closes the coding loop, not provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the reviewed recursion.
- Disturbance / variety regulated: not established at S2 level because the supported organization exposes one primary coding S1 rather than simultaneously active first-party S1 units with a concrete mutual interference/oscillation relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential tool-call execution, `AgentHarness._ensure_not_running()` overlap prevention, append-only session state and ordinary transcript repair are execution-integrity mechanisms, not an inter-S1 attenuation loop.
- Closure path: not applicable; the required distinct-S1 disturbance → attenuation → changed later S1 behavior relation was not found.
- Why this is / is not agent-owned: the repository does not ship a standard multi-agent/team/delegation topology at the frozen ref. Preventing two prompts from overlapping on one `AgentHarness` instance protects one S1 runtime rather than coordinating distinct operational units.
- Evidence: [`src/tyrion_agent/loop.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/loop.py); [`src/tyrion_agent/harness.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/harness.py); [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: event listeners and shared transcript/session mechanisms provide communication/observation but are not evidence of S2 without distinct operating units and an interference-specific feedback loop.

### Absence scope

- Surfaces inspected: pure loop; harness overlap/cancellation/event machinery; coding session and persistence; standard CLI/TUI architecture; coding tool execution; repository architecture documentation.
- Plausible first-party paths checked: concurrent tool calls; overlapping harness prompts; event subscribers; session branches/resume; provider/runtime parallelism; any first-party multi-agent/delegation/team surface in the pinned source tree.
- Why no material first-party path remains: ordinary tool calls are executed sequentially, one harness instance explicitly forbids overlapping runs, and no shipped distinct S1 workers plus concrete cross-worker interference-and-attenuation relation were found.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the single coding S1 and deterministic runtime safeguards was established.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. Cancellation, max-turn limits, transcript repair and context thresholds enforce externally supplied/runtime rules, while the model-backed actor's task sequencing remains its own S1 operation rather than management of multiple current operational units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `AgentHarness` running-state guard; cancellation token; max-turn condition; listener/event dispatch; session restoration; context-limit checks and compaction trigger.
- Closure path: not applicable; no actor receives a whole-organization current view and uses substantive authority over shared resources, priorities, commitments or constraints across S1 units.
- Why this is / is not agent-owned: the class name `AgentHarness` and its supervisor wording describe software lifecycle supervision of one loop, not evidence of the stronger organizational S3 function.
- Evidence: [`src/tyrion_agent/harness.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/harness.py); [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py); [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator cancellation is a useful intervention channel but generic stop/control capability does not establish a first-party S3 parent mode or autonomous S3 loop.

### Absence scope

- Surfaces inspected: `AgentHarness` state/cancellation/listeners; model/tool loop; session state; context-limit/compaction logic; CLI/TUI operation and architecture description.
- Plausible first-party paths checked: run supervision; progress/current-state observation; cancellation; iteration caps; session recovery; context-pressure handling; operator command surface.
- Why no material first-party path remains: all located mechanisms either support one S1's execution or enforce preset/operator decisions; there is no distinct whole-current regulator with organization-wide allocation/commitment authority.

## S3* — Complementary audit

- State: —
- Function: no material complementary independent runtime audit function with a corrective return into ordinary Tyrion operation was established.
- Disturbance / variety regulated: not established at S3* level inside the supported distribution.
- Decisive decision or feedback right: not established in runtime. The adjacent `evals/` package can score isolated benchmark runs and optionally invoke a separate LLM judge, but its verdicts are not consumed by normal `tyrion` sessions as corrective control over the audited S1.
- Decision owner: not established within the assessed standard distribution.
- Supporting / enforcement mechanisms: development-time deterministic eval metrics, isolated fixtures and optional DeepEval/OpenRouter judge are adjacent evaluation infrastructure rather than a runtime audit owner.
- Closure path: not applicable; no supported ordinary-run path was found from independent challenge → audit verdict → returned correction/control affecting subsequent production coding behavior.
- Why this is / is not agent-owned: the judge can be independently model-backed, but Methodology 0.3.6 requires boundary reachability and corrective return. The repository explicitly keeps evaluation dependencies separate from normal runtime installation, and the standard coding loop does not consume judge decisions.
- Evidence: [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md); [`evals/judge.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/evals/judge.py); [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this does not deny that maintainers can use evaluation results during development; the assessed boundary is the supported Tyrion coding organization, not its project-development process.

### Absence scope

- Surfaces inspected: `evals/` judge/evaluation description; standard loop/harness/session path; runtime dependency boundary documented in README; session persistence and event/listener paths.
- Plausible first-party paths checked: independent judge verdicts; deterministic test/eval scores; runtime listener feedback; post-tool verification; development regression evaluation.
- Why no material first-party path remains: evaluation is adjacent/offline and no verdict-return wiring into normal runtime control was found; ordinary coding self-checks remain part of S1 rather than an independently accessed complementary audit role.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party prospective environment-intelligence and organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Tyrion can inspect current project evidence, resume historical sessions and summarize old context, but it does not ship an actor that scans an external/prospective environment, forms strategic alternatives and changes persistent organizational capability/strategy for later operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: project instructions; session history; context token estimation; model-written compaction summaries; provider/model switching by the operator.
- Closure path: not applicable; no prospective scan → option formation → persistent capability/strategy change → later operational return path was found.
- Why this is / is not agent-owned: context compaction changes representation of the present conversation so the same coding S1 can continue; it does not change the organization's capabilities or strategy in response to future-facing environmental intelligence.
- Evidence: [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py); [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: runtime learning/replanning inside a current task and long-lived conversational memory are not sufficient S4 evidence under the Profile.

### Absence scope

- Surfaces inspected: context-window/compaction path; persisted sessions/tree restore; project instructions; provider/model selection; eval infrastructure; architecture documentation.
- Plausible first-party paths checked: memory/history reuse; automatic context adaptation; model switching; project instruction refresh; benchmark-driven improvement; any self-update/evolution capability in the pinned source tree.
- Why no material first-party path remains: located mechanisms preserve current-task continuity or expose operator configuration; no supported autonomous/constructor/parent prospective organizational adaptation loop was found.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity or ultimate-policy closure was established.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. The user chooses the coding task, provider/model and operating environment; system/project instructions and tool boundaries are authored configuration. Tyrion does not autonomously decide or escalate and close its own ultimate purpose/identity/policy.
- Decision owner: not established inside the assessed organization; ultimate policy remains external/operator/developer owned.
- Supporting / enforcement mechanisms: system prompt, project instructions, provider configuration, tool definitions, max-turn/cancellation controls and host-user privileges.
- Closure path: not applicable; no first-party runtime identity-policy decision reaches a qualifying S5 owner and returns to alter operation.
- Why this is / is not agent-owned: the model-backed S1 operates under externally supplied task/prompt/tool/provider boundaries. The README additionally notes that mutating tools act without confirmation, which removes rather than establishes a governance/identity closure layer.
- Evidence: [`README.md`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/README.md); [`src/tyrion_agent/harness.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_agent/harness.py); [`src/tyrion_coding/session.py`](https://github.com/Xtejasveer/tyrion/blob/35806697ba873e069b6ec6346216baea8b94a72f/src/tyrion_coding/session.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: static prompt/tool constraints and user ownership of the machine are operating conditions, not first-party S5 closure.

### Absence scope

- Surfaces inspected: system/project prompt construction; tool/runtime boundary; provider/model configuration; cancellation/max-turn control; CLI/TUI command surface; session/persistence architecture; README safety boundary.
- Plausible first-party paths checked: agent-authored policy changes; runtime approval/governance; policy escalation; purpose/identity revision; operator configuration returned as a first-party parent-governed S5 loop.
- Why no material first-party path remains: authoritative purpose/policy choices remain external inputs/configuration, and the reviewed distribution contains no runtime identity/ultimate-policy closure path.

## Assessment summary

Tyrion closes a clear autonomous coding S1 through its shipped model/tool feedback loop. Its harness, session tree, compaction, cancellation and persistence machinery are substantial execution-support features, but they remain support for the same operating unit at the reviewed recursion. No distinct inter-S1 coordination relation, whole-current regulator, reachable complementary audit return loop, prospective organizational adaptation function or identity/ultimate-policy closure is established in the standard distribution. The repository's optional evaluation judge is specifically treated as adjacent development/evaluation infrastructure rather than imported into runtime S3* ownership.

Proposed vector: **`A · — · — · — · — · —`**.
