---
harness_id: onion-harness
project_name: Onion Harness
repository: https://github.com/chenofchina/onion-harness
review_ref: dc2be116eddad9c45018d0d8590fa6cc96387bfe
reviewed_at: 2026-11-08
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Onion Harness

## Review boundary

- System in focus: the installable, locally operated Onion desktop/HTTP agent harness, including its ordinary tool-using agent mode and its separately selectable multi-seat Roundtable mode.
- Purpose and identity: local AI automation, executable tool work and bounded multi-model deliberation, with user-confirmed modifications to the harness's future capabilities and core operating prompt.
- Relevant environment: local user and filesystem, configured model providers, installed tool executors, optional web/MCP integrations, Windows desktop/HTTP clients and independent Roundtable model seats.
- Standard-distribution boundary: supported Python backend/API and optional desktop frontend at the pinned commit; a configured model API key is needed for normal live inference. A mocked model in tests is not evidence of actual provider-side reasoning quality.
- Credited operating / distribution surfaces: `onion_harness/harness/runtime.py`, `harness/roundtable.py`, `harness/meta.py`, `ledger/`, `core/roundtable.py`, `api/service.py`, the shipped UI communication path and configured first-party review/approval interfaces.
- Adjacent first-party surfaces excluded from ownership: tests, CI/release, frontend build tooling, documentation, example tool code, and the separate `loong_agent` package's internal implementation. That installed dependency can execute the selected agent loop but its undocumented internal organization is not imported as an independent Onion S-function.
- First-party operating / deployment modes considered: locally operated normal ReAct tool mode with Plan/Standard/Strict variants; optional safety-reviewer configuration; first-party Roundtable meeting with 2–6 model-backed seats, user intervention and hard breaker; agent-proposed, human-confirmed local meta changes.
- Recursion level: one self-hosted Onion application as a whole; ordinary task loops and Roundtable seats are operational cells inside this boundary. A spawned model call is not a separate viable recursion by itself.
- Reviewed revision: `chenofchina/onion-harness@dc2be116eddad9c45018d0d8590fa6cc96387bfe`.
- Observation date: 2026-11-08.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python API assembles a local `OnionRuntime`, executor registry, ledger, optional memory, review gate and a task/event store. `OnionRuntime.run_task` creates a session and executes an installed engine's `AgentLoop`, with locally assembled prompt, model/provider, tools, permission path and history/compression. The agent chooses tool calls; Onion adapts/enforces sandbox execution, conditional model safety review and human approval. These runtime restrictions do not own the agent's task-level decisions. The bridge explicitly imports `loong_agent` as an external dependency rather than implementing that engine's internal loop itself ([runtime task and loop](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/runtime.py#L450-L600), [dependency bridge](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/bridge.py#L17-L66)).

Roundtable is another shipped API path, not a test fixture. The user selects seats, host, provider/model, dissent rate and round limits; the application creates a distinct `RoundtableOrchestrator`. Each seat produces its own substantive position and potential rebuttal. The host model selects a first speaker based on unresolved disagreements; subsequent seats receive a transcript; a deterministic consensus test closes the meeting or the hard breaker returns divergences for human intervention. Mid-meeting human messages and extra seats are wired into subsequent rounds ([API constructor](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L822-L922), [orchestrator](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L253-L367)).

The first-party ledger distinguishes model- or user-originated **proposals** from human-authorized **application**. Proposed tools, executors, provider presets, skills and prompt changes do not activate until the local user explicitly applies them; versions and snapshots persist in SQLite. Subsequent task construction reads the changed state, and MCP tools are hot-loaded after approved changes ([meta tools](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/meta.py#L193-L307), [ledger application](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/ledger/ledger.py#L146-L210), [return to runtime](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L1585-L1658)).

## Operational model

The normal S1 cell is a model-backed agent session that interprets a user goal, decides on tool calls and returns an outcome. In Roundtable, model-backed seats are distinct S1 cells contributing independent arguments to a shared meeting outcome. The host's targeted next-speaker choice is an agent decision, whereas seat ceilings, tokens, consensus arithmetic and timeout/breaker are deterministic enforcement. The human local operator retains whole-meeting interventions, authority to accept capability and identity changes, and final policy decisions. Repository maintainers/CI belong to a separate development recursion, not Onion runtime management.

## S1 — Operations

- State: A
- Function: first-party hosted model agents interpret user tasks and perform tool or deliberative work in local environments.
- Disturbance / variety regulated: changing user goals, tool results, file/task conditions and differing model-seat arguments.
- Decisive decision or feedback right: model-backed agent chooses next task-level action/tool call or substantive seat reply/rebuttal from prompt and feedback.
- Decision owner: model-backed agent actor in normal mode; individual seat agents in Roundtable. The deterministic Onion application and external engine transport the choice.
- Supporting / enforcement mechanisms: `EngineLoop`, provider adapters, executor registry, sandbox, Plan/Standard/Strict mode, approvals, memory, task events and configured ceilings.
- Closure path: agent-selected call reaches an Onion executor, tool result returns to engine context for further agent choice; Roundtable seat replies enter the shared transcript and later rounds/final consensus.
- Boundary reachability: `OnionRuntime.run_task` wires live tools/options into `EngineLoop.run`; the API constructs and starts Roundtable in a supported application path, rather than only in tests.
- Why this is / is not agent-owned: model-dependent action and substantive reasoning disappear with the agent actor, while retaining Onion's deterministic mechanics; the latter do not independently choose the goal's actions.
- Evidence: [runtime loop](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/runtime.py#L450-L600), [tool creation and feedback](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/runtime.py#L617-L655), [Roundtable turn/feedback](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L282-L334).
- Basis: structural.
- Confidence: high for shipped model-backed action/seat loops; no claim of successful paid-provider E2E execution in this review.
- Caveats: the internal `loong_agent` dependency is not separately assessed; local app uses its installed engine and a configured model rather than a first-party foundation model.

## S2 — Coordination

- State: A
- Function: Roundtable reduces blocking disagreements among independent model-seat contributions to produce a coherent joint deliberative outcome or a bounded explicit divergence.
- Disturbance / variety regulated: incompatible seat stances and directed rebuttals can prevent the meeting from converging.
- Decisive decision or feedback right: the model-backed host chooses the first seat per round after reading the evolving transcript and outstanding disagreement; each seat can revise/rebut from shared feedback.
- Decision owner: host model agent for the discretionary next-speaker selection; other seat agents own their subsequent replies. Deterministic consensus/budget computation does not inherit that discretion.
- Supporting / enforcement mechanisms: shared transcript, validated seat IDs, fixed tail speaking order, agreement/rejection parsing, round/call/token ceilings and human breaker.
- Closure path: conflict appears as rejected stances/rebuttals; the host reads the transcript and selects the next first speaker, seats read preceding positions on later turns; consensus or the recorded divergences determines whether to stop, continue or involve the human.
- Boundary reachability: the user-facing Roundtable API creates an actual `RoundtableOrchestrator`, while `_speaking_order` makes a live host model call on its first-party normal execution path.
- Why this is / is not agent-owned: removal of host deliberation leaves only deterministic rotation, not the dispute-aware speaker choice; mechanical ordering and consensus calculation remain supporting machinery. The host's returned `focus` field is **not** presently forwarded as a direct seat instruction, so the positive witness is bounded to first-speaker selection plus visible transcript/replies, not a stronger agenda-control claim.
- Distinct S1 units: 2–6 model-backed seats with separate replies and optional rebuttal targets.
- Inter-S1 disturbance: concrete disagreeing stances/rebuttals about the shared topic, which block consensus.
- Attenuating coordination relation: host selection uses the transcript and prompts priority to whoever can address the open disagreement; subsequent seats see the accumulated positions.
- Feedback into subsequent S1 behaviour: next round's host prompt and seat prompts include preceding contributions, and the consensus result stops/continues the meeting.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a real conflict representation (rejections/targeted rebuttals) is tied to disagreement-aware host choice and a next-round response path; generic message passing alone is not the credited function.
- Evidence: [host and seat prompts](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L44-L79), [host choice](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L438-L470), [rebuttal and consensus path](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L282-L339), [verdict implementation](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L662-L706), [rebuttal/breaker tests](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/tests/test_roundtable.py#L193-L255).
- Basis: structural.
- Confidence: medium; source proves a dispute-specific feedback design, not observed convergence improvement under live provider conditions.
- Caveats: this is S2 in supported Roundtable mode, not in an ordinary single-agent session. The host model's optional `close` and `focus` JSON fields are not the decisive mechanical closure of a round.

## S3 — Inside-and-now control

- State: P
- Function: parent/operator supervision of the current Roundtable's resource composition and commitments across its model-seat cells.
- Disturbance / variety regulated: debate stalls, insufficient specialist coverage, divergent statements or unsatisfactory current answer distribution across seats.
- Decisive decision or feedback right: the human operator chooses the meeting roster/model constraints at creation and can add a new seat, address one or all seats, and return a new directive while the meeting is underway or after the breaker.
- Decision owner: the local human/operator at the application/meeting parent boundary; model host selection alone does not establish agent-owned whole-system S3.
- Supporting / enforcement mechanisms: meeting status/roster/minutes, API mediation, capped seat count, inbox, event persistence, model-cost and breaker display.
- Closure path: a user-added seat joins the next meeting round; a targeted message enters that seat's inbox and is delivered at its next speaking turn; post-meeting human input reopens a bounded follow-up without silently clearing prior consensus.
- Boundary reachability: the shipped Roundtable UI/API connects operator messages and seat addition to the same live orchestrator and its subsequent rounds.
- Why this is / is not agent-owned: the model host cannot decide to create extra provider seats or authoritatively change the operator's live constraints; these are returned human current-control decisions. Generic cancel and destructive-command approval are not separately counted as whole-system S3.
- Whole-system current view: Roundtable's member roster, statements, per-seat usage, divergences and minutes are available to the user across its current operational seats.
- Current-control decision scope: parent choices over team composition, targeted priorities and intervention within the bounded meeting; not an inferred global allocator across independent Onion tasks.
- Evidence: [Roundtable UI contract](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/README.md#L620-L675), [human messages/follow-up](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L940-L997), [live seat addition](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L999-L1047), [inbox return](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/roundtable.py#L620-L658).
- Basis: structural.
- Confidence: medium; the positive parent claim is bounded to the current Roundtable, not whole installation-wide budgeting.
- Caveats: the operator can be human and does not need to be modeled as an AI agent; no autonomous S3 resource/commitment discretion is established merely from timeouts/host ordering.

## S3* — Complementary audit

- State: —
- Function: a separate audit would have to compare ordinary operational success/claims against independent underlying reality and return findings to current control.
- Disturbance / variety regulated: false reported completion, unsound execution, unobserved side effects or unverifiable model claims.
- Decisive decision or feedback right: not established as a distinct first-party complementary operational audit right in the reviewed modes.
- Decision owner: none evidenced for such a distinct audit; the optional safety-review model judges proposed **code before execution**, and the user can approve a flagged request, but neither audits a claimed completed operational outcome through another access path.
- Supporting / enforcement mechanisms: code-only safety filter, Plan mode refusal, user confirmation, diff view, tests and logs.
- Closure path: no first-party complementary direct-reality audit finding is wired to corrective control as a separate function. Safety-review verdicts affect the ordinary executor's pre-execution gate only.
- Why this is / is not agent-owned: an isolated reviewer model is not an S3* owner without a complementary audit of operating reality; authors explicitly call it a filter, not final authority.
- Evidence: [review-gate invocation](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/runtime.py#L839-L960), [code-only review](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/review.py#L230-L301), [README warning](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/README.md#L433-L462).
- Basis: structural.
- Confidence: medium-high within the shipped runtime/reviewer/GUI paths inspected.
- Caveats: no universal claim about unexamined third-party plugins or a user's own independent verification procedure.

### Absence scope

- Surfaces inspected: normal runtime loop, optional review gate, approval return, API task events and diff controls, Roundtable consensus/breaker, README, tests and first-party ledger.
- Plausible first-party paths checked: destructive-command `ReviewGate`, approval side channel, per-tool result display, Roundtable consensus, local diff/version view and repository CI/tests.
- Why no material first-party path remains: those shipped paths are routine pre-execution filtering, debate convergence, monitoring or development validation. They do not independently sample/inspect operational reality and return a separately owned audit judgment after a production claim.

## S4 — Outside-and-then intelligence

- State: P
- Function: parent-governed prospective adaptation of the agent's future available model/tool/skill capabilities in response to demands from the external user/work environment.
- Disturbance / variety regulated: new tool/provider/skill needs beyond the currently enabled local repertoire.
- Decisive decision or feedback right: the working agent can formulate a reasoned future-capability change proposal, but only the legitimate local human/operator decides whether it changes the installed repertoire.
- Decision owner: human parent for adoption of the future capability; no automatic agent-owned S4 closure is claimed.
- Supporting / enforcement mechanisms: `MetaTools` proposal API, dry-run ledger diff, capability validation and versioning, MCP tool materialization and hot reload.
- Closure path: user-supplied/newly encountered capability need reaches the agent prompt; agent may propose a new executor/provider/skill/MCP tool; parent applies the proposal; the next runtime constructs its tools/prompt from the revised state or hot-loaded MCP registry.
- Boundary reachability: meta tools are added to the normal agent's live tool registry and `_after_ledger_change` updates the shipped runtime, including persisted tool availability; this is not merely a developer roadmap or test fixture.
- Why this is / is not agent-owned: only the parent approval changes capability. Counterfactually removing the parent leaves proposals un-applied and does not close adaptation; this is not S4=A.
- External distinction: changing user tasks and available model/tool services create a capability gap that can be expressed through the tool's mandatory `reason` and proposal content; no autonomous external scanning is claimed.
- Future / prospective distinction: requested changes alter tools/providers/skills for subsequent actions or sessions, not merely the immediate task answer.
- Adaptation option generated: agent-proposed registration of an MCP tool, model-provider preset, executor or skill.
- Path back into current capability / S3: approved ledger state is re-read by `OnionRuntime` / refreshed MCP tools and becomes an available action for subsequent S1 execution.
- Evidence: [default operating prompt](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/ledger/state.py#L29-L64), [meta tool proposals](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/meta.py#L193-L307), [human apply/reload](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L1585-L1658).
- Basis: structural for shipped proposal/return; inferred for the external-demand-to-adaptation interpretation.
- Confidence: medium-low. This is a supported parent-closed *capability adaptation mode*, not evidence of autonomous environmental forecasting or systematic S4 strategy.
- Caveats: a generic user-chosen plugin is not S4 by itself; this positive claim is limited to the model-originated, reasoned future capability proposal and actual parent return path. No source trace establishes recurring environmental surveillance or measured adaptation effectiveness.

## S5 — Policy and identity

- State: P
- Function: parent-governed ultimate change to the agent's core identity and operating rules, rather than an ordinary task/tool approval.
- Disturbance / variety regulated: tension between the current core behavior/policy and a desired enduring operating identity for future sessions.
- Decisive decision or feedback right: human operator authoritatively accepts/rejects a model- or user-originated update to the persistent core system-prompt segment.
- Decision owner: legitimate local human operator of the self-hosted agent, not the proposing agent or deterministic ledger.
- Supporting / enforcement mechanisms: `onion_update_system_prompt`, `ChangeLedger` validation/diff/version history, API confirmation and ordered system-channel prompt assembly.
- Closure path: core operating-rule proposal reaches confirmation UI; operator calls apply/reject; accepted segment is persisted; `compose_system_prompt` and `OnionRuntime._compose_system_prompt` inject it into future model calls.
- Boundary reachability: normal agent tool registry contains the prompt-update meta tool, and user-facing API applies proposals to live state read on every later task. No adjacent maintainer CI or unshipped governance actor is needed.
- Why this is / is not agent-owned: model can suggest but cannot activate its own enduring identity/policy change. No separate autonomous S5 ultimate-authority mode is established.
- Identity / ultimate-policy issue: the core segment begins with `You are Onion` and durable operating rules; changing that segment changes the identity-level instructions inherited by future tasks, distinguishable from approval of a particular shell command.
- Ultimate authority in each claimed mode: only human parent mode positively established; autonomous policy proposal is not decisive authority.
- Return-to-operation path: ledger `apply` persists the approved segment; the runtime composes the system channel from that state on the next run.
- Evidence: [core identity and policy](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/ledger/state.py#L29-L64), [prompt-change proposal](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/meta.py#L217-L229), [parent application](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/api/service.py#L1585-L1596), [runtime system-channel return](https://github.com/chenofchina/onion-harness/blob/dc2be116eddad9c45018d0d8590fa6cc96387bfe/onion_harness/harness/runtime.py#L1083-L1153).
- Basis: structural.
- Confidence: medium-high for the shipped parent closure; the grade does not imply the default agent authors its own constitutional rules.
- Caveats: a generic per-tool confirmation is not counted as S5. This applies only when the human-authorized change affects the durable identity/core policy segment.

## Recursion

Roundtable seats have distinct model-backed operational outputs, but no evidenced independent S3/S4/S5 metasystem per seat; technical multi-agent nesting is not credited as additional viable recursion. The local human/application parent can govern the Roundtable as an operational unit within Onion; this does not establish a public distributed OSS organizational parent merely because the repository has contributors.

## Variety and escalation

Local task variety is amplified by executors, memory, MCP/web tools and model reasoning while Plan mode, sandbox and user review attenuate destructive tool risk. Roundtable amplifies viewpoints by choosing multiple seats and attenuates persistent disagreement through host speaker selection, shared transcript, consensus test and hard stop. Round/budget exhaustion produces a specific human-required return rather than silently declaring success. Inability to call an external model, safety reviewer unavailability and permission rejection are ordinary execution/approval boundaries, not an extra VSM function or proof of autonomous S3.

## Evidence gaps

- No credentialed end-to-end provider run or empirical convergence-performance claim was attempted; cited tests use stubs for substantial model behavior.
- The external installed `loong_agent` implementation is not reviewed as a separate organization; only Onion's first-party orchestration and integration at the declared boundary are credited.
- S2's agent-specific conflict attenuation is based on a dispute-aware host *first-speaker* choice and shared next-round transcript. The host-returned `focus` text is not applied as a direct per-seat directive; a narrower S2 adjudication could reasonably weigh this limitation.
- S3's parent claim is deliberately limited to the Roundtable's live roster/directive decisions, not broad scheduling across unrelated normal tasks.
- S4's positive parent adaptation interpretation depends on the agent using its shipped meta tools to address an outside/future capability gap; source establishes the available path, not an observed self-directed environmental study or successful adaptation case. If an actual operational witness is required to distinguish this from generic extensibility, S4 merits focused re-review before canonical admission.
