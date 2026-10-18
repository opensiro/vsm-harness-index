---
harness_id: phoenix-agent-harness
project_name: Phoenix Agent Harness
repository: https://github.com/Phoenixrr2113/agent-harness
review_ref: 0f67103affd30a3c778874b890dbd5801cdbd94f
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Phoenix Agent Harness

## Review boundary

- System in focus: One persistent, local **file-first agent cell** created by the first-party `harness` CLI with its own model, identity, skills/rules, tool registry, sessions, scheduled tasks and stored state. The boundary includes its ordinary run/chat modes, optional configured scheduler, delegate-to-agent tool, post-session journal/learning tools and budget/approval guards. The system is not the upstream maintainer organization, a network of separately administered agents or an autonomous company.
- Purpose and identity: Perform user-defined knowledge/technical work with tools and long-lived local context; remember observations and optionally update future run behaviour through learned Markdown instructions.
- Relevant environment: Current user requests, tool observations and tool failures, recurring user patterns, model API and host process availability, scheduled workload and spending limits.
- Standard-distribution boundary: First-party TypeScript/Node CLI and runtime with user-configured LLM provider, installed model-backed `createHarness`/Conversation paths, memory and session files, optional MCP tools, delegated stateless subagents, scheduler, skill evaluations, rule learning, rate-budget gating, and configuration. Provider/model inference requires real external credentials or a local configured provider; third-party hosted services are not first-party organizational owners.
- Credited operating / distribution surfaces: [createHarness and LLM work](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L226), [Conversation run/stream](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L55-L345), [subagent delegation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L297), [global daily/monthly guardrails](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/guardrails.ts#L20-L114), [scheduler workflow and learning](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L275-L336), [auto-journal and auto-learn](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L450-L486), [journal's LLM synthesis](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/journal.ts#L24-L150), [learned instinct flow](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L20-L205), [skill quality baseline eval](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/quality.ts#L71-L165) and [promote runtime adapter](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/agent-runner.ts#L183-L223).
- Adjacent first-party surfaces excluded from ownership: Upstream repo author GitHub CI/releases, README self-improvement performance rhetoric, Terminal-Bench and learning-delta benchmark experiments, customer-specific extensions, independent agent organizations not instantiated by the shipped runtime, the external LLM provider as a separate policy institution, and historical design notes without callable runtime closure.
- First-party operating/deployment modes considered: Standard `harness run/chat` with tool choice and saved sessions; CLI `journal` and `learn --install`; configured scheduler `auto_learn`, durable workflows and stateless `delegate_to` agents; opt-in skill evaluation/optimization; rate and spending limits, approval and file-lock utilities. S2 and S3* cannot be borrowed from optional tests or sibling scripts without an actual operational closure.
- Recursion level: One local agent cell across repeated interactions and configured scheduled workflows. A stateless delegated subagent can be another S1 work unit when actually assigned a task; this does not automatically make the whole cell a network of independently viable organizations.
- Reviewed revision: `0f67103affd30a3c778874b890dbd5801cdbd94f`, immutable frozen [intake #1699](https://github.com/opensiro/vsm-harness-index/issues/1699), current [batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700) row 5.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The self-contained runtime loads IDENTITY.md, rules, skills and persistent local state to assemble the system prompt and allowed tools, obtains the configured model, then iterates model-generated tool decisions and observations through the model client. Work can be one-shot or interactive; tool-enabled runs can invoke stateless child agents. Each run writes a session record, updates health/cost/state and optionally invokes lifecycle/trigger hooks. The CLI is a real model-backed operation, not a prompt generator alone. [construct model and tools](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L119), [run/model/tools and session feedback](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L120-L271), [delegate-to-agent model call](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L293).

The local scheduler launches configured periodic workflows, considers quiet hours and cooldowns, and can synthesize saved sessions into an LLM-generated journal. When `auto_learn` is configured, journal/interaction-derived instinct candidates can be installed as Markdown instructions for later sessions. The separate `rules promote` CLI exposes an apparent eval gate, but its actual first-party `buildLiveRulePromoter` passes optimistic fixed results for trigger and quality checks. Therefore that gate **does not constitute observed rule-quality verification** at this pinned revision. A different `skill eval-quality` path does execute with-skill/without-skill samples and grades resulting output artifacts; `optimize-quality` can propose future skill text, but its application is opt-in, not a standing independent auditor of work outcomes. [scheduler/current cooldown](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L275-L321), [automatic journal and learning](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L450-L486), [journal model synthesis](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/journal.ts#L54-L143), [candidate/install path](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L152-L196), [promoter's fixed pass-through](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/agent-runner.ts#L183-L222), [real optional skill test runs](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/quality.ts#L71-L164), [opt-in future skill rewrite](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-quality.ts#L31-L76).

The runtime also ships deterministic rate/spend guards with persisted usage and time-window status, durable checkpoint and resume, developer/model authorization requests before selected tools, file-lock helpers and diagnostics. These mechanisms are important operational infrastructure, but locks are fail-open under contention and no source-evidenced inter-S1 conflict/feedback transaction was found at the assessed parent recursion. The mandatory same-time whole-cell budget/limit guard does provide a narrow first-party current-control constructor, not a separate autonomous executive model. [budget/rate guard](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/guardrails.ts#L20-L113), [model-call gate](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L122-L156), [durable engine](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/durable-engine.ts#L48-L161), [file-lock fail-open](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/file-lock.ts#L141-L196).

## Operational model

At S1 a model chooses requested task steps/tool calls and reacts to observations. The local cell can run distinct scheduled and delegated operations, but the inspected source does not show an independent S2 response that detects and resolves a concrete conflict among distinct S1 operations. It imposes one configured whole-cell resource envelope across repeated primary runs, with measured cost and rejection on exceeded quotas (S3=C; limited coverage of nested delegate calls). Trace capture, doctor/lints, opt-in with/without-skill evaluation and optimistic `rules promote` signals do not establish an independent complementary audit with correction returned to S3 (S3*=—). The journal/learning path produces durable retrospective changes to future prompts; without future-external modelling and a two-way strategic option path it cannot be counted as S4. Identity is user-authored and constrained by rule/approval files, not decided through ultimate authority (S5=—).

## S1 — Operations

- State: A
- Function: Produce goal-specific model-generated answers and real tool-mediated work, including model-initiated subagent tasks and scheduled workflows.
- Disturbance / variety regulated: Unpredictable user goals and tool outputs, multi-turn reasoning, resource and API failures, tool arguments and dynamic skill selection.
- Decisive decision or feedback right: Choose context-dependent actions, tool arguments, next steps and final task output within configured tool/provider/guardrail limits.
- Decision owner: The configured primary LLM through first-party `createHarness`/Conversation; delegated child model owns its own bounded task output, but the parent chooses whether to invoke it.
- Supporting / enforcement mechanisms: System context loader, primary model API, model-driven tools and MCP, permission wrapper, session store and optional scheduler.
- Closure path: Request or scheduled prompt → model interprets loaded identity/rules and selects an action → allowed tool executes and returns evidence → model updates its response → final result/session saved for subsequent work.
- Boundary reachability: Shipped CLI supports `harness run/chat` and the first-party `createHarness` path wires actual provider inference to tools, sessions and state. Provider credentials/availability remain external requirements.
- Why this is / is not agent-owned: The model chooses substantive local responses and tool actions; deterministic infrastructure only bounds, logs and executes the selected operations.
- Evidence: [model setup/boot](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L119), [model run with tools](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L120-L207), [saved outputs and feedback](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L209-L269), [child-agent model invocation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L284), [Conversation flow](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L180-L330).
- Basis: Source-explicit model-backed agent/tool loop reachable from shipped CLI.
- Confidence: High structural, not externally benchmarked at this review ref.
- Caveats: No credential-backed provider/tool success was executed as part of the assessment; unit/integration test successes are not inference-quality evidence.

## S2 — Coordination

- State: —
- Function: Regulate interference and oscillation **between distinct S1 operating units** without simply centralizing every decision.
- Disturbance / variety regulated: Potential overlapping file/working-state effects when separately invoked scheduled work, parent and delegated agent tasks share the local harness directory.
- Decisive decision or feedback right: No identifiable shipped decisive inter-worker collision-resolution or mutually negotiated scope/budget adjustment with documented changed downstream S1 behavior.
- Decision owner: Not established for this function at the declared recursion; a parent model's tool selection and static scheduler control are not independent S2 coordination decisions.
- Supporting / enforcement mechanisms: Generic `delegateTo` task calls, scheduler cooldown and no-recursion child tool configuration, per-file lock helpers, local session state.
- Closure path: Message/task routing and file serialization helpers are present, but no demonstrated inter-S1 disturbance → coordination decision → affected S1 rescheduling/repartition outcome transaction closes.
- Why this is / is not agent-owned: The primary agent can delegate one task; that alone is decomposition, not S2. The file-lock primitive's `withFileLock` proceeds even when lock acquisition fails, so it is not source evidence of fail-closed coordination among independent S1s; no first-party consumer transaction using that helper was found.
- Evidence: [stateless child invocation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L237-L294), [parent agent tools](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/agent-tools.ts#L20-L77), [scheduler cooldown](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L492-L537), [lock helpers' fail-open behavior](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/file-lock.ts#L141-L194).
- Basis: Bounded negative; declared S1 plurality alone is insufficient.
- Confidence: Medium-high for reviewed standard runtime; no blanket claim against adopter-written plugins.
- Caveats: Separate user-configured scripts could implement specific inter-worker conflict attenuation beyond the reviewed default.

### Absence scope

- Surfaces inspected: Built-in agent-as-tool delegation, scheduler/proactive controls, budget limits, file-lock helper, durable-engine checkpoint and stored session state.
- Plausible first-party paths checked: Shared persistent files under two agent invocations, cooldown of one proactive workflow, lock-based write access, child-agent no-recursion tool selection.
- Why no material first-party path remains: No concrete distinct-S1 conflict with a designated coordination choice and a returned changed inter-worker operating arrangement appears in those shipped normal paths; generic routing, cooldown and fail-open lock utilities do not close the required four-part S2 witness.

## S3 — Inside-and-now control

- State: C
- Function: Maintain the whole resident agent cell's current viable operation within configured spending and request limits across repeated runs.
- Disturbance / variety regulated: Aggregated spending and request-rate growth across sessions and scheduled/current prompts that would exceed user-authorized resource ceilings.
- Decisive decision or feedback right: Enforce a configured stop/allow decision at the cell's primary model-run entry point using live usage records and daily/monthly cap policy.
- Decision owner: Current operating envelopes are chosen by the user/configuration; first-party deterministic `checkGuardrails` implements that narrowly scoped management constructor. There is no resident model selecting or renegotiating the budgets.
- Supporting / enforcement mechanisms: Persisted cost records, rate limiter, daily/monthly spending aggregation, current health state and primary run/stream preflight.
- Closure path: Current primary-run request → shared cost/rate records are assessed → configured limit leads to block or permit → next model work is prevented or allowed and usage is recorded for future decisions.
- Boundary reachability: `createHarness.run` and its streaming counterpart call the guardrail directly before model generation in shipped primary runtime. A configured spending cap denies execution on exceeded usage, rather than merely rendering a dashboard.
- Why this is / is not agent-owned: C is the delivered **deterministic** current resource-control constructor; no discretionary S3=A is asserted. This does not prove complete whole-of-project coordination/priority optimization.
- Whole-system current view: Daily/monthly totals and time-window request counts across this configured resident agent's recorded primary sessions; includes multiple user and scheduled invocations, not company-wide organizational resources.
- Current-control decision scope: Whether new primary model work proceeds within quota, with static owner-configured limits; subordinate delegate paths may bypass this particular check and are not claimed fully covered.
- Evidence: [shared budget and rate guard logic](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/guardrails.ts#L20-L112), [entry blocking and exception path](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L122-L160), [health success/failure tracking](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/health.ts#L65-L127), [scheduler running workflows](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L275-L337).
- Basis: Specific instantiated current-resource controller with feedback and execution effect.
- Confidence: Medium: narrow constructor demonstrated, management autonomy not.
- Caveats: This is not a portfolio manager; nested agent calls can use direct `generate` rather than all going through the same top-level gate. A static limit would not justify S3=A, and additional source-owned budget negotiation is not shown.

## S3* — Complementary audit

- State: —
- Function: Independently examine raw operational truth beyond ordinary S1 reports and return findings capable of correcting S3/worker decisions.
- Disturbance / variety regulated: Model task failure, falsely claimed successful outputs or misleading quality/improvement claims needing independent correction.
- Decisive decision or feedback right: No default first-party independent raw-evidence operational auditor with binding corrective findings returned to current control is established.
- Decision owner: None in the normal run/learn/approval loop; user may run optional skill evaluations but these do not install independent review of normal agent claims.
- Supporting / enforcement mechanisms: Session logs, health diagnostics, doctor rules, tool approvals, verification criteria, optional skill eval-quality/trigger tests and `rules promote`.
- Closure path: Operational outputs are logged, and separate optional skill benchmarks can run, but no independently empowered auditor is automatically fed task-primary evidence and returns a mandatory corrective finding into the current work controller.
- Why this is / is not agent-owned: A real opt-in with/without-skill benchmark is useful evaluation, yet is not a second operational inspection channel with corrective S3 authority over the live goal. The nominal `rules promote` gate's installed adapter **returns fixed optimistic pass signals** rather than observed pass/fail samples; it cannot be credited as independent quality audit.
- Evidence: [quality eval actually compares outputs](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/quality.ts#L71-L165), [optional optimize quality approval](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-quality.ts#L31-L76), [rule promotion gating API](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/promote-rule.ts#L40-L73), [actual promoter fixed success signals](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/agent-runner.ts#L183-L223), [verification gate checks](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/verification-gate.ts#L254-L391), [approval asks user, not independent evidence](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/approval.ts#L36-L155).
- Basis: Bounded negative for operational S3* in the shipped resident-agent standard mode.
- Confidence: Medium-high; no claim that all independent plugins are impossible.
- Caveats: Isolated skill benchmark assertions or third-party independent reviewer plugins may augment the system, but cannot be imported as demonstrated default audit ownership.

### Absence scope

- Surfaces inspected: Rule promotion source and live eval adapter, real skills eval-quality/optimize, doctor and verification-gate modules, conversation result/session log, approval and hooks.
- Plausible first-party paths checked: Independent quality assessment of skill revisions, verification of routine tool results, learned-rule approval, correction of work after false-positive reports.
- Why no material first-party path remains: The real benchmark is a separately invoked skill optimization workflow, not complementary work audit; the learning promotion gate has placeholder positive scores, and ordinary traces/approvals do not independently inspect source-primary production outcomes and feed corrective findings into S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: Model prospective external changes/opportunities, propose viable future capability adjustments and return those options for present adoption.
- Disturbance / variety regulated: Changes in user requirements, outside tooling/competitors, model capabilities or future environmental conditions requiring new skills or organizational capacity.
- Decisive decision or feedback right: Not established: the journal model extracts **retrospective** repeated behaviours from completed sessions, and optional quality optimizer suggests changes against existing skill-eval cases, not possible future outside environments.
- Decision owner: No source-owned externally prospective options manager or returned S3 adoption choice. The user chooses new skills/provider and installed rules are based on past local interaction evidence.
- Supporting / enforcement mechanisms: Session capture, model-generated journal, instinct proposals, scheduled auto-learn/auto-install, optional skill optimize and future prompt/rule reload.
- Closure path: A real past-interaction → future prompt-modification mechanism exists, but there is no sensed external future alternatives → option model → current S3 capability decision and feedback path. `rules promote` cannot supply missing strategic selection via its stubbed evaluations.
- Why this is / is not agent-owned: Model judgment over recurrent session text changes later behaviour, but generic self-learning/prompt tuning is not S4 unless externally and prospectively oriented.
- Evidence: [journal text comes from past sessions](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/journal.ts#L24-L143), [LLM derives instincts from past events](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L20-L101), [optional learned rule installation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L152-L196), [scheduled auto learning](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L450-L485), [rule use on subsequent boots](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L47-L93), [quality optimization inputs](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-quality.ts#L31-L76).
- Basis: Bounded negative despite actual agent-derived persistent learning.
- Confidence: Medium-high for this reviewed revision and stated resident-agent boundary.
- Caveats: Real cross-session prompt evolution is acknowledged as operational adaptation; user-defined prospective skills can be authored but are not shipped as a default closed organizational S4 mechanism.

### Absence scope

- Surfaces inspected: Journal, instinct learner, rule promoter, scheduled auto-learn, skill optimization, graph/dead primitive intelligence, external source connectors and tool selection.
- Plausible first-party paths checked: Automatic post-session rule changes, measured skill improvements, proactive scheduled workflows and user-configured model/tool switching.
- Why no material first-party path remains: Reviewed options are retrospective behaviour extraction, present workload execution or user-directed configuration; no outside-and-then alternative comparison and return to present system capability control is implemented.

## S5 — Policy and identity

- State: —
- Function: Legitimate ultimate purpose and identity governance, including resolution when current operations and future adaptation pull in opposite directions.
- Disturbance / variety regulated: Conflicting long-lived agent purpose, changes in acceptable work domain, ultimate owner authorization and identity-level tradeoffs.
- Decisive decision or feedback right: No first-party live route to an ultimate identity arbiter and binding return path is established.
- Decision owner: End user/operator authors `IDENTITY.md`, limits, approval choices and configuration from outside the agent cell; model/system prompt restrictions do not grant a legitimate autonomous S5 right.
- Supporting / enforcement mechanisms: `IDENTITY.md`, rule files, config, approval on selected tools, content filters and static safety/permission guards.
- Closure path: Local prompts/approvals govern particular tool/run choices; no constitutional-level identity conflict → legitimate ultimate authority deliberation → durable binding mission revision path is source-evidenced.
- Why this is / is not agent-owned: The agent reading an identity file does not make it the legitimate governor of that identity, and ordinary `[y/n]` tool approval is not a parent-governed S5 return loop.
- Evidence: [identity/rules loaded into system](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L93), [human tool approval path](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/approval.ts#L28-L110), [guardrail config](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/guardrails.ts#L20-L112), [content filter execution](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L163-L188).
- Basis: Bounded negative at first-party user-installed agent recursion.
- Confidence: High for standard modes.
- Caveats: A human/adopter organization can supply separate governing S5, but none is wired as a credible first-party identity-level return path in this revision.

### Absence scope

- Surfaces inspected: Config, identity documents, rule learner/installer, model/tool approvals, content filters, proactive scheduler and core lifecycle.
- Plausible first-party paths checked: Self-edited identity files, model overrides and user permissions, learned rules, higher-policy enforcement and ownership of future mission changes.
- Why no material first-party path remains: Existing paths configure or carry task rules; they do not detect identity-governance conflicts and route authoritative new policy through an ultimate decision maker back into long-term runtime constraints.

## Recursion

- Parent: User/adopter defines this agent's goals, identity, provider, limits and acceptance; upstream developer and platform provider are separate organizations.
- Operational child units: Optional delegated stateless agents can perform scoped model work. They have their own prompts/outputs but do not automatically create viable nested S1–S5 recursive organizations.
- Parent-child return: Delegated answers feed the main model and session context, not a distinct parent S3* audit or negotiated horizontal S2 settlement.

## Variety and escalation

- S1 absorbs diverse user/tool outcome variety via model choices.
- S2: No positive inter-S1 conflict-and-return relation observed within the credited modes; task routing and no-recursion helpers are insufficient.
- S3 attenuates resource/throughput variety through shared configured usage budgets and rejection of new primary runs on exceeded caps (C; no model-owned control discretion).
- S3*: The nominal learned-rule eval gate currently returns fixed optimistic results, limiting quality claims; optional actual skill benchmark is not mandatory complementary independent audit.
- S4: Learned behavioural instructions persist from prior sessions, changing later run context, but without externally prospective option/adoption dialogue.
- S5: Human-controlled identity and approval remain outside first-party legitimate policy government.

## Evidence gaps

- Reviewed clean immutable frozen Git ref `0f67103affd30a3c778874b890dbd5801cdbd94f`, tree `b0c4cb5f7f863e8f09f5817732908a1e33353a45`, MIT. Model/provider credentials and real external tool success not supplied in this source-first run.
- After `npm ci --ignore-scripts`, TypeScript `tsc --noEmit` passed. Upstream Vitest standard parallel run had **1467 passed / 8 timed-out / 1 skipped** tests; the five affected integration files independently reran at two workers and a 30-second timeout: **14/14 passed**. Never represent the original complete run as all-green at default settings.
- `rules promote` uses optimistic stubbed trigger and quality evaluation scores in the default adapter even though separate real opt-in skill eval functionality exists. Do not claim quantitatively demonstrated self-improvement or independent audit from that gate.
- The S3=C attribution is narrow: primary model-run guardrail shared spending limits, not all nested delegates and not an autonomous cross-agent planner.
- Runtime and user-defined skill customization could introduce future S2/S3*/S4/S5 systems, but those are outside the pinned first-party implementation being assessed.
