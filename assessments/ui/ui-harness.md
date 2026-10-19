---
harness_id: ui-harness
project_name: UI Harness
repository: https://github.com/awizemann/harness
review_ref: 3f58c077ded131cca71d75efb05c5d325f0ed18f
reviewed_at: 2026-10-19
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

# UI Harness

## Review boundary

- System in focus: The distributed macOS 14+/Swift 6 native UI user-testing agent operating cell shipped by `awizemann/harness` (application and first-party CLI), with model decisions enacted through supported iOS Simulator, macOS-app and embedded web drivers. This is a single goal/session operating boundary, not a software engineering department or the external tested application.
- Purpose and identity: Pursue a user-defined app-testing goal with an agent persona, observe actual target UI, select interactive actions, record success/failure and identify user-experience friction.
- Relevant environment: Native macOS host, target iOS Simulator app/macOS app/web page, captured screenshots and marked interactive elements, network/model provider, operator permissions and app-under-test.
- Standard-distribution boundary: Shipped `Harness/Domain/AgentLoop.swift`, `Harness/Domain/RunCoordinator.swift`, `Harness/Tools/AgentTools.swift`, model `LLMClient` adapters, platform-specific `SimulatorDriving` implementations, and packaged `HarnessCLI/` entrypoints. The standalone `HarnessMCP/` can expose autonomous runs to an external agent, but an external MCP client is not counted as an internal VSM executive.
- Credited operating / distribution surfaces: [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L117), [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L171), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L108), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L574), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L621), [Harness/Tools/AgentTools.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Tools/AgentTools.swift#L1), [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L20), [HarnessMCP/RunBuilder.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessMCP/RunBuilder.swift#L1).
- Adjacent first-party surfaces excluded from ownership: Tested app's own internal agents and backend, upstream inference-provider servers/weights, developer/test fixtures, product's build/release/CI/docs organization, external MCP client, stored run reports as independent reviewers, and human product governance.
- First-party operating / deployment modes considered: Autonomous run until terminal tool/budget/stop, step-by-step approval mode, goal chains consisting of sequential legs, supported iOS/macOS/Web drivers, macOS packaged app, headless CLI and MCP-run adapter. External tool-only MCP UI sessions with no first-party model loop are not counted as S1 autonomy proof.
- Recursion level: One active UI-testing agent session/leg with model-backed action choice; a configured chain repeats sequential goals with fixed orchestrator mechanics rather than operating a portfolio of independently viable S1 departments.
- Reviewed revision: `3f58c077ded131cca71d75efb05c5d325f0ed18f` (public GitHub repository ID 1228325421), exact source tree `ed875a876ae67c06c781c5535d8ada5de4400ec0`, frozen in [batch #1724](https://github.com/opensiro/vsm-harness-index/issues/1724).
- Observation date: 2026-10-19; Profile 0.2.4 / Methodology 0.3.7, both the semantic and immutable generation-origin pair.

## Repository architecture

`HarnessRunner.run` constructs an actual inference `LLMClient` based on the selected provider and runtime dependencies, builds the per-platform execution adapter, and drives `RunCoordinator`. `RunCoordinator` captures a screenshot from the platform driver, prepares an `AgentLoopState`, calls `agent.step`, logs the proposed `ToolCall`, then sends the model's chosen action to `session.driver.execute`. It waits for UI settle, records success/error and physical UI details, and appends a `LLMTurn` that reaches the next loop iteration. The model receives updated screenshots and tool-result observations, so the S1 action-feedback loop is source-connected rather than marketing-only. [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L20); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L664); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L730); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L805); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L878).

The `AgentLoop` calls `llm.step` with goal, persona, history, screenshot and platform context, returning a model-chosen tool and inline friction notes. It compacts prior turns and retries malformed tool calls by returning the parse error to the model. Post-step screenshot hash and tool comparison detects repeated local screen cycles. `RunCoordinator` enforces configured step/token budgets, supports optional per-step operator approval, records friction/output logs, and handles a `mark_goal_done` terminal decision. Goal-chain legs can sequentially relaunch the tested app and rerun the same S1 loop; neither leg sequencing nor step gating by itself establishes metasystemic S2/S3 authority. [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L194); [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L250); [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L297); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L621); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L786); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L920).

The product includes a distinct `HarnessMCP` surface for driving or exposing sessions. Its tool-only step-level mode can act under a separately configured external agent; that outside actor is not silently credited as the model-backed product's own higher VSM organization. Default friction recording originates with the same operating model or coordinator safety logic and does not constitute independent complementary organizational audit. [HarnessMCP/RunBuilder.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessMCP/RunBuilder.swift#L1); [README.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/README.md#L1); [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L764).

## Operational model

The accountable primary transformation is an agent operating a GUI to test an operator-specified user journey and return observations/final verdict and friction. The first-party agent has genuine ongoing S1 discretion over which action to issue given screenshots; drivers and budgets are execution scaffolding. There is no separately evidenced organizational current-management, cross-S1 coordination, independent corrective audit or outside-and-then strategy-adoption machinery at the declared single-session recursion.


## S1 — Operations

- State: A
- Function: Choose and enact the next UI action while pursuing the active user-testing goal.
- Disturbance / variety regulated: Unfamiliar app screens, navigation outcomes, failed touches/typing, slow page loads, scroll exhaustion, visible UX friction, explicit terminal conditions and task uncertainty.
- Decisive decision or feedback right: `LLMClient.step` generates the next `ToolCall` based on current screenshot, persona/goal and prior tool history; the product executes the chosen action and returns actual driver success/error/screen state in the next model turn.
- Decision owner: The configured model-backed `AgentLoop` packaged in the first-party app/CLI operating path, subject to optional human step-by-step approval but not replaced by static replay.
- Supporting / enforcement mechanisms: Per-platform simulator/window/web drivers, `RunCoordinator` deterministic sequencing, screenshot serialization, model protocol adapters, tool schema, budgets, history compaction, action approval/skip/stop UI, logs and cycle detection.
- Closure path: User goal/persona → captured UI image + prior result → model tool decision → optional human approval → first-party driver action → settle/capture + tool-result history → next model decision or `mark_goal_done`.
- Boundary reachability: `HarnessCLI/HarnessRunner.swift` actually builds the model, run request, driver and coordinator; app/CLI implementation calls `RunCoordinator.run`, whose shipped `runLeg` invokes `AgentLoop.step` and `session.driver.execute` for the supported target. MCP autonomous run adapters are supplementary routes, not required for this first-party positive.
- Why this is / is not agent-owned: Without the model, the driver and coordinator can record/capture/enforce budgets but cannot select context-sensitive user actions for arbitrary screen states; the model is the decisive action selector.
- Evidence: [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L20), [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L194), [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L250), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L574), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L676), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L730), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L805), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L878).
- Basis: Explicit first-party model decision/action/observation closure and supported distribution route.
- Confidence: High for installed source-defined capability, not independently reproduced success or API quality.
- Caveats: Requires macOS host, functioning platform driver/device and model provider; neither live tested-app run nor provider quality is attested here.


## S2 — Coordination

- State: —
- Function: No first-party interference-sensitive coordination of distinct concurrently viable organizational S1 units is established at the single UI-testing-run recursion.
- Disturbance / variety regulated: Multiple target environments or goal-chain legs may require session sequencing, but they are mutually selected alternatives/sequential tasks rather than operating divisions with demonstrated reciprocal conflicts.
- Decisive decision or feedback right: `RunCoordinator` sequences one leg's model actions and a predetermined chain of user-specified legs; the same agent has task-level discretion, not a separate S2 function adjudicating interference between S1 units.
- Decision owner: Operator goal-chain configuration and deterministic coordinator, with the model owning local per-leg task choices.
- Supporting / enforcement mechanisms: Per-leg reset/relaunch, session state, platform driver selection, serial goal-chain ordering, one-at-a-time tool execution and step approval.
- Closure path: One leg concludes → configured next leg is launched or chain stops; this is fixed user-journey sequencing without inter-S1 disturbance judgment → coordination decision → changed later behavior of competing S1 units.
- Why this is / is not agent-owned: A tool execution controller and multiple platforms do not create distinct independent operating units; the model's choice among UI actions stays within S1.
- Evidence: [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L242), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L464), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L574), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L805), [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L74).
- Basis: Source-bounded negative across shipped operating/chain paths.
- Confidence: High for single-run boundary.
- Caveats: Externally organized multiple testing agents could supply their own coordination and need separate assessment.

### Absence scope

- Surfaces inspected: AgentLoop, RunCoordinator multi-leg chain and per-step agent/driver work, CLI driver routing, optional MCP modes.
- Plausible first-party paths checked: Multiple legs, parallel app targets, step approvals, source event streams and shared device/driver constraints.
- Why no material first-party path remains: The reviewed default product runs one current agent and fixed/sequential legs; it does not sense and attenuate a concrete interference cycle between two viable operating S1 units with returned coordination.


## S3 — Inside-and-now control

- State: —
- Function: No distinct first-party organizational whole-current executive with binding portfolio, cross-unit priorities and resource/commitment decision return was established.
- Disturbance / variety regulated: Step/token budgets, loop repetition, failed UI actions and goal-level state require task-local recovery/safety, not discretionary whole-system management.
- Decisive decision or feedback right: Operator defines run goal, persona, provider and limits; coordinator enforces budgets and stops or retries current action; there is no model/constructor charged with cross-goal whole-current priority adjudication.
- Decision owner: Operator for global current commitments; local agent for current UI action; deterministic runtime for enforcement.
- Supporting / enforcement mechanisms: Step/token caps, cycle detector, approval stream, cancellation handling, leg verdict and event logging.
- Closure path: Current UI error/budget/approval → task-local retry/block/stop or continuation; no whole-organizational view → S3 management decision → returned operating-unit adjustment.
- Why this is / is not agent-owned: RunCoordinator's centralized per-task lifecycle and budgets are real execution control, but do not decide whole-current competing work commitments with management discretion.
- Evidence: [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L194), [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L297), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L242), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L621), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L786).
- Basis: Explicit negative after checking plausible shipped management machinery.
- Confidence: High in declared recursion.
- Caveats: Product team/person deciding test portfolios is an adjacent human organization, not an in-boundary first-party parent S3 mode.

### Absence scope

- Surfaces inspected: RunCoordinator budgets and approval/step loops, goal chains, RunHistory and CLI/MCP entrypoints.
- Plausible first-party paths checked: Shared run budget, success/failure verdict, GUI progress, approval and per-leg restart.
- Why no material first-party path remains: No distinct whole-current cross-operational discretionary owner/return is wired; each inspected path enforces parameters or resolves one current testing session.


## S3* — Complementary audit

- State: —
- Function: No distinct source-independent complementary operational auditor that judges divergence between reported outcomes and actual operation and sends enforceable correction into governance.
- Disturbance / variety regulated: UX friction, agent stalls and unsuccessful UI actions are tracked during a run, but they are the same operator/agent's local observations rather than a separate audit channel.
- Decisive decision or feedback right: The operating model emits inline `note_friction` and `mark_goal_done`; runtime detector adds friction on cycle/budget; neither independently audits the truthfulness of current-control reports with correction authority.
- Decision owner: S1 model and deterministic coordinator for task reporting; human reviewer of outputs is external.
- Supporting / enforcement mechanisms: Screenshot history, friction event logs, driver error reporting, cycle detector, run replay/report artifacts and schema/parse retries.
- Closure path: S1 UI observation/tool/error → same S1 model and run log/friction → user-facing run report, not complementary inspection → independent findings → changed operation/S3 commitments.
- Why this is / is not agent-owned: A model reporting friction about its own action trace is not a separately appointed auditor; a replay record can aid humans but has no shipped autonomous corrective judgment and governance return.
- Evidence: [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L750), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L764), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L843), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L920), [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L250).
- Basis: Source-bounded negative after inspecting first-party friction/report and validation pathways.
- Confidence: High.
- Caveats: A human or separately wired external agent may independently review runs without that becoming this first-party S3*.

### Absence scope

- Surfaces inspected: Model inline-friction outputs, RunCoordinator runtime error/cycle friction, RunLogger/RunHistory, CLI and MCP result reporting.
- Plausible first-party paths checked: Self-reported UX friction, screenshot replay, cycle detection, parse retries, user approval review.
- Why no material first-party path remains: All examined correction paths either stay in the current S1 execution or surface a report externally; none is a distinct independent operational audit of current-control reality with accountable corrective return.


## S4 — Outside-and-then intelligence

- State: —
- Function: No separately operating prospective intelligence/adaptation process changes the agent harness's future capabilities through an adopted strategic option based on external change.
- Disturbance / variety regulated: New apps, personas and models may require new settings; shipped user-selected provider/platform and in-run adaptive actions do not amount to an organizational long-horizon strategy loop.
- Decisive decision or feedback right: Operator selects provider, target, goal, persona, model and chain. Model adapts momentary UI choices, while no first-party S4 actor evaluates future alternatives and promotes a changed stable future harness strategy.
- Decision owner: External human user/developers for future settings/features; task model for present UI navigation only.
- Supporting / enforcement mechanisms: Model/provider factory, persona/goal request, historical run artifacts and user journey reporting.
- Closure path: Existing model/profile + user-defined session → goal-local run and report; no outside-and-then scan → strategy option → governance/adoption → subsequent changed autonomous operation.
- Why this is / is not agent-owned: Dynamic screen choice and history compaction are S1 adaptation within a run; capturing friction data does not create an independent future-capability selection or deployment loop.
- Evidence: [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L194), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L242), [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L20), [README.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/README.md#L1).
- Basis: Bounded negative after inspecting available launch/feedback and reporting paths.
- Confidence: Medium-high for frozen first-party distribution.
- Caveats: User may later change tests or developers may improve product using reports, but their independent research/design work is not a packaged S4 mode here.

### Absence scope

- Surfaces inspected: UI agent history/retry, RunCoordinator verdict/friction, model/provider and CLI configuration, test reports and supported chain paths.
- Plausible first-party paths checked: Cross-run reports and UX observations, model selection, persona/goal changes, potential future product iteration.
- Why no material first-party path remains: No first-party future environmental option maker, adopted organizational strategy and subsequent operational return path is present in these shipped modes.


## S5 — Policy and identity

- State: —
- Function: No first-party legitimate ultimate-purpose/organizational identity policy decision and return loop at this UI user-testing agent recursion.
- Disturbance / variety regulated: App safety boundaries and user approvals constrain individual screen actions, but do not settle competing organizational identities or enduring mission/policy.
- Decisive decision or feedback right: User specifies test purpose/target/persona and may approve/skip/stop individual actions; app enforces them as task policies. No legitimate S5 actor resolves an ultimate identity/purpose matter within the shipped agent harness.
- Decision owner: Operator for product-testing mission and human safety approvals; S1 agent only for task actions.
- Supporting / enforcement mechanisms: Prompt/goal injection, step-by-step approvals, permission/platform restrictions, default budget, tool schema.
- Closure path: Operator-configured goal and constraints → task-local agent action authorization; no first-party identity/purpose dispute → legitimate policy arbitration → returned enduring organizational rule.
- Why this is / is not agent-owned: The model's UX judgments are bounded by an external human goal, not a grant to redefine organizational identity and ultimate policy.
- Evidence: [Harness/Domain/AgentLoop.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/AgentLoop.swift#L194), [Harness/Domain/RunCoordinator.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/Harness/Domain/RunCoordinator.swift#L786), [HarnessCLI/HarnessRunner.swift](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/HarnessCLI/HarnessRunner.swift#L20), [README.md](https://github.com/awizemann/harness/blob/3f58c077ded131cca71d75efb05c5d325f0ed18f/README.md#L1).
- Basis: Boundary-relative negative for first-party S5 under the reviewed product.
- Confidence: Medium-high.
- Caveats: Actual human governance of the user/organization conducting tests remains external, not a positive first-party `P` mode without an explicit returned identity-policy channel.

### Absence scope

- Surfaces inspected: CLI goal/persona/provider selection, AgentLoop prompt, step-mode approval gates, platform/driver permissions and terminal verdict/report flow.
- Plausible first-party paths checked: Human stop/skip/reject, app sandbox/security approvals, static tool restrictions, user mission-setting.
- Why no material first-party path remains: No packaged first-party identity-level matter intake, authoritative constitutional choice and future-operations policy return exists beyond task configuration.


## Recursion

One autonomous GUI testing session/leg is the credited agentic operating cell. Additional goals in a chain sequentially rerun the same task loop rather than constituting independently viable business divisions. The tested app and external MCP agent can have their own organizations but neither is included in this first-party assessment boundary.

## Variety and escalation

The model absorbs UI uncertainty through screenshots and tool results. Parse retries, limit exhaustion, cycle blockage, request cancellation and explicit user approval manage local execution variety and safety. These events do not establish an algedonic signal or autonomous S3/S4/S5 by their mere presence.

## Evidence gaps

- No Mac/Xcode/Simulator runtime is available in this Linux source-review environment; Swift 6/macOS tests, platform-driver UI sessions, model-provider inference and goal success rates were **not** executed or measured. The positive S1 claim is source-wired first-party supported mode evidence, not verified empirical effectiveness.
- A future independently deployed multi-agent testing fleet with shared contested resources may require fresh S2/S3 examination; this frozen first-party single-run distribution does not entail such a fleet.
- MCP's external client may use a separate autonomous agent; this review does not import that actor's management, future adaptation, auditing or policy rights into the first-party product.
- This is a noncanonical `status: proposed` assessment until a separate exact-head PR/CI and later canonical admission/exclusion transaction.
