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
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Phoenix Agent Harness

## Review boundary

- System in focus: The **standard-distribution standalone file-first agent runtime**, operating over one installed harness directory, its model-backed goal/tool sessions, concurrent separately goal-directed child agent or workflow runs, shared durable files and opt-in learned-skill improvement. The credited S4 submode is **the executable skill-optimization/validated promotion loop**; this is not an assessment of the upstream developer's own company, independent provider organizations or benchmark success.
- Purpose and identity: Run a model-backed, tool-using agent configured in Markdown, persist sessions and shared state, optionally delegate to model-backed sub-agents, and improve later agent skill routing/capabilities through experiment-informed local changes.
- Relevant environment: User requests, real tool outcomes, uncertain task choices, simultaneous workflows/session writers, changing user and task patterns across conversations, skill trigger/quality test feedback, API/permission failures.
- Standard-distribution boundary: `harness init/run/chat`, TypeScript first-party runtime `createHarness`, supplied model API/local provider, first-party tool/delegation, persisted session/journal files, opt-in `skill optimize-description`, `skill optimize-quality --auto-approve` or `rules promote` eval-promoted adaptation. Node CLI is the only supported public entry; consumer API/model weights and environment are outside source.
- Credited operating / distribution surfaces: [runtime harness/model/tool loop](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L244), [model-backed conversation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L55-L239), [agent delegation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L265), [session and state concurrency](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/sessions.ts#L70-L112), [file-lock ownership and retry](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/file-lock.ts#L58-L200), [model instinct candidate synthesis](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L20-L105), [skill description optimization](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-description.ts#L35-L110), [skill content optimization](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-quality.ts#L36-L85), [rule promotion](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/promote-rule.ts#L25-L73), [rules loaded into later system prompt](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/context-loader.ts#L60-L110).
- Adjacent first-party surfaces excluded from ownership: README claims of continual measurable improvement; historical experiment reports or unavailable model-backed success figures; externally hosted Ollama/OpenRouter/other model capabilities; arbitrary downstream multi-agent organization governance; user-authored human constitutional policies; disabled/private optional integration and any evaluation not actually run in this review. The test suite is a structural evidence surface, not an agent-owned organizational function.
- First-party operating / deployment modes considered: Standalone CLI with real user-selected provider and model; tool-assisted agent conversations, concurrent durable workflows and model-delegated specialists, human approval mode for selected tools, scheduled auto-journal/auto-learn when explicitly enabled; opt-in promoted `rules` and skill optimizers including non-dry-run description optimization. CLI-only no-API-key failure is not an autonomous operational mode.
- Recursion level: One installed multi-operation agent work cell with separate sessions and model-backed delegated/task workers, shared durable state and a harness-optimization meta-loop. Do not turn model tool calls or all scheduled jobs into independent organizational S1 divisions by name alone.
- Reviewed revision: 0f67103affd30a3c778874b890dbd5801cdbd94f, frozen [batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700) row 5 and intake [#1699](https://github.com/opensiro/vsm-harness-index/issues/1699).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped `harness` CLI constructs a first-party model-backed session using provider configuration. `createHarness` loads identity and rules from the installed directory, attaches tools/MCP and optional approvals, calls `generateWithAgent` for model-directed tool use, saves session state and cost and exposes run/chat paths. The conversation mode streams responses with persisted context; `delegateTo` constructs a different configured agent identity and invokes a model with a bounded delegation/tool set. Scheduled/durable workflows track steps and can resume, but scheduling alone is not managerial autonomy. [harness boot and run](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L247), [conversation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L55-L349), [delegation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L278), [durable workflows](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/durable-engine.ts#L1-L160).

Shared session, semantic and state files have shipped lock acquisition/release code to prevent concurrent writers from overwriting the same durable content. The same installed harness may serve multiple separate goal sessions or delegated actors, so this is a narrow first-party constructor for mutual exclusion over a concrete destructive shared-file interference case. `state-merge` separately arbitrates conflicting **human-vs-agent** updates; that path is not mistakenly counted as inter-S1 S2 on its own. [file lock](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/file-lock.ts#L58-L203), [session write locking](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/sessions.ts#L70-L110), [conversation log locking](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L325-L360), [state-merge](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/state-merge.ts#L100-L175), [lock tests](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/tests/file-lock.test.ts#L1-L120).

The strongest future-facing mode is not a README marketing loop. Model-backed `proposeInstincts` constructs potential rules from real sessions or journal content and stores them as candidates. **Important discontinuity:** `learn --install` writes Markdown into `instincts/`, whereas current `buildSystemPrompt` loads `rules/` and skill catalogs, **not arbitrary instincts**. This means `learn --install` alone must **not** be credited as automatically changing the next model's instructions. A distinct supported path does close future capability: `rules promote <candidate-id>` checks trigger/quality evals and installs `rules/<id>.md` that a subsequent run loads; `skill optimize-description` goes further, having a model propose candidate skill descriptions against failing cases, measuring train/validation results, choosing the best held-out validation option and **writing it** unless in dry-run mode. These are source-real opt-in outside-and-then improvement modes, not a general default continual self-evolution guarantee. [instinct synthesis and install](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/instinct-learner.ts#L20-L185), [promotion eval and write](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/promote-rule.ts#L25-L73), [description optimize and apply](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-description.ts#L35-L112), [CLI promotion and optimizer](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/cli/index.ts#L3500-L3610), [prompt actually reads rules](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/context-loader.ts#L60-L111).

The frozen repo is MIT, source version 0.18.0, and supplies a Vitest suite plus an **opt-in** real-Ollama end-to-end learning test explicitly skipped without `INTEGRATION=1` and a local model. Source inspection/testing here is not a provider-backed performance benchmark. [package](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/package.json#L1-L86), [learning-loop test opt-in boundary](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/tests/integration/learning-loop.e2e.test.ts#L1-L85).

## Operational model

Operational S1 is genuine model-controlled tool and specialized delegation. Multiple concurrent goal/session workers could corrupt the same persistent session/state/memory file; specific source-installed locks reject/serialize destructive interference (S2=C), without agent negotiation or generic cross-team scheduling. Budget/rate guards, deterministic cron and per-workflow step state do not by themselves establish a whole-system discretionary S3 authority over current independent S1 commitments (S3=—). Verification gates and outcome tests are conventional task checks, not complementary independent auditor access with corrective management return (S3*=—). A separate opt-in model-guided skill-optimization pipeline *does* make externally prompted future usage distinctions, propose/test/select changed callable skill descriptions and install accepted changes for later runs (S4=A); installed instincts alone do not provide this closure. Identity text, approval settings and permission boundaries do not establish legitimate ultimate policy/identity decisions (S5=—).

## S1 — Operations

- State: A
- Function: Produce context-sensitive user-task results and tool-driven actions through a model-backed agent and its separately scoped delegated task actors.
- Disturbance / variety regulated: Unknown user tasks, external tool outcomes, code and file contexts, model choice and recovery from failed work.
- Decisive decision or feedback right: Choose substantive next model response, tool invocation/arguments, delegated specialist response and final task output based on actual observations.
- Decision owner: External supplied model executing the first-party `generateWithAgent` and `delegateTo` loops; CLI config and guards bound but do not preselect task solutions.
- Supporting / enforcement mechanisms: System prompt from identity/rules, tools and MCP adapter, guardrails, approvals, session persistence, continuation and skill activation.
- Closure path: Goal or ongoing chat → first-party runtime boots configured agent/tools → model issues tool calls → actual tool result is returned to ongoing model work → task answer/state stored and may inform later turns.
- Boundary reachability: Shipped `harness run/chat` calls `createHarness` and actual model provider; source includes model-backed `Conversation` and `delegateTo` for a separately configured agent. A provider must be configured but requires no speculative downstream product implementation.
- Why this is / is not agent-owned: The model chooses dynamic tool/reasoning actions; scheduler/guardrail only applies constraints. It is a genuine S1 model decision path, not README-only automation.
- Evidence: [first-party goal execution](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L27-L244), [provider invocation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/llm/provider.ts#L1-L165), [conversation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L180-L335), [delegation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/delegate.ts#L155-L278).
- Basis: Executable model/tool/observation loop and later goal-specific results.
- Confidence: High for structural function, not measured external provider quality.
- Caveats: No real provider-backed API calls were made for this isolated assessment; source/runtime tests have mocks.

## S2 — Coordination

- State: C
- Function: Protect shared persistent context of distinct concurrent operational session/delegated actors against destructive simultaneous updates.
- Disturbance / variety regulated: Overlapping writes to common memory/state/session log paths could lose event history, corrupt JSON/Markdown or conflate competing operational outcomes.
- Decisive decision or feedback right: Reserve shared file mutation for one actor at a time; reject/queue another contender until the lock is released or declared stale, returning failure instead of silently overwriting.
- Decision owner: Deterministic lock and file-write constructor. No model autonomously negotiates which competing S1 goal should get priority.
- Supporting / enforcement mechanisms: `tryLock/acquireLock/withFileLockSync`, token/state session writes, lock pid/timestamp/stale detection, guarded persistent writers.
- Closure path: Distinct live agent sessions/tasks approach a common durable context file → first-party locking admits one writer while the other waits or receives an explicit unavailable/timeout response → serialized writes preserve input for later agent context and downstream runs.
- Boundary reachability: The shipped conversation/session/state modules directly invoke `withFileLockSync` on writable source files, not merely declare concurrency support. Tests hold a lock and assert a second acquisition fails, confirming a real conflict mode.
- Why this is / is not agent-owned: Narrow S2-specific serialized shared-state coordination exists, but the choice is deterministic; no cross-agent negotiated compromise or autonomous portfolio-level arbitration is claimed.
- Distinct S1 units: Two separately goal-directed concurrent model-backed sessions/delegated workers attached to the same installed harness directory.
- Inter-S1 disturbance: Both write one shared context/session file, risking lost updates or corruption and incorrect later task context.
- Attenuating coordination relation: Per-file lock ownership, wait/stale policy and exclusive critical write section.
- Feedback into subsequent S1 behaviour: Contending writer cannot silently publish inconsistent state; successful serialized session record becomes the common context on later reads, or lock failure returns an exception/explicit block to the caller.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It is a direct structural treatment for overlapping writes among independent active workers, not simply a message bus or assigning tasks.
- Evidence: [lock acquisition/refusal](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/file-lock.ts#L58-L199), [session critical write](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/sessions.ts#L65-L110), [conversation critical write](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/conversation.ts#L325-L355), [executable double-acquisition regression](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/tests/file-lock.test.ts#L1-L115).
- Basis: Concrete shared-file collision + shipped mitigation + resulting serialized operational state.
- Confidence: Medium for multi-session/delegated inter-S1 context; the lock tests demonstrate the resource constraint but not full two-live-model priority fairness.
- Caveats: `state-merge` additionally arbitrates human/agent identity conflicts, which are not counted as separate S1s; this S2 classification does not claim full coordination of all parallel delegated tasks or dynamic negotiation.

## S3 — Inside-and-now control

- State: —
- Function: Whole-present system current-control authority over the commitments, resources and operating priorities of multiple S1 units.
- Disturbance / variety regulated: Competing current goal commitments, execution capacity, downstream errors and resource trade-offs needing ongoing whole-work-cell intervention.
- Decisive decision or feedback right: No first-party run-wide model-owned or human-parent-governed whole-system portfolio intervention right established beyond task/turn level.
- Decision owner: Not established; current user schedules, tool permissions, per-goal guardrail thresholds and preconfigured durable workflow graphs do not choose current cross-S1 commitments.
- Supporting / enforcement mechanisms: Scheduler, durable checkpoints/retries, health/cost monitors, configured rate limits and user approval before selected tools.
- Closure path: Runtime task failures and budget blocks affect a given operation, but no whole-system present status → discretionary current resource/commitment decision → independent S1 reallocation loop is supplied.
- Why this is / is not agent-owned: Per-run model planning and status/error handling are S1 autonomy; static scheduler/guardrails are support and not a current multiunit management owner.
- Evidence: [guardrails inside one run](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L129-L160), [scheduler](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/scheduler.ts#L92-L170), [durable workflow state](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/durable-engine.ts#L1-L166), [run state and health](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/health.ts#L1-L135).
- Basis: Bounded absence at actual distributed run and scheduler surfaces.
- Confidence: Medium-high for frozen shipped source.
- Caveats: A consumer may compose its own broader S3 across distinct agents, but this is outside the standard standalone boundary.

### Absence scope

- Surfaces inspected: Model run, separate delegation, durable workflow engine, scheduler, health/cost/guardrail enforcement, concurrent state/memory management and human-approval controls.
- Plausible first-party paths checked: Per-goal model plan, bounded retry, health thresholds, schedule assignment and workflow cancellation, parent user tool decisions.
- Why no material first-party path remains: All traced rights regulate tasks, predetermined schedules and local failure/enforcement; no actor with whole-S1 current overview chooses or revises cross-unit commitments/resources as an organizational decision.

## S3* — Complementary audit

- State: —
- Function: Independently access operational evidence to challenge routine S1–S3 performance claims and return corrective control beyond ordinary workflow validation.
- Disturbance / variety regulated: A task or internal status falsely reporting success or an agent's answer hiding actual source/tool failure.
- Decisive decision or feedback right: No specific independent operational auditor is shipped with a standing complementary access path and returned corrective management authority.
- Decision owner: Not established; verification gates evaluate supplied command outputs or manually checked criteria and skill eval graders assess improvement candidates, not separate organizational S3 truth.
- Supporting / enforcement mechanisms: VerificationGate command/manual criteria, run/session logs, health trackers, benchmark/eval grader, tool result and checkpoint checks.
- Closure path: No independently initiated raw operational inspection → corrective audit finding → S3 management decision loop in the shipped boundary.
- Why this is / is not agent-owned: Task gate pass/fail, routine tracing and evals performed inside S4's skill optimizer are ordinary validation/support, not an alternative sufficiently independent investigation of current organizational reporting.
- Evidence: [verification gate supplied-output check](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/verification-gate.ts#L254-L392), [session recording](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/harness.ts#L185-L241), [skill eval loop different recursion](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-description.ts#L35-L110).
- Basis: Bounded negative after primary verification/eval/trace surfaces inspected.
- Confidence: Medium-high within the declared run cell.
- Caveats: A user-authored auditor skill could be provided, but mere extensibility does not establish a first-party independent audit with returned authority.

### Absence scope

- Surfaces inspected: Verification gates and command outputs, eval graders, session recording, health/logs, approval, model delegation and workflow stages.
- Plausible first-party paths checked: Second evaluator model for a prospective skill candidate, manual gate confirmation and routine tool result checks.
- Why no material first-party path remains: None is an independent current S1/S3 fact-finding channel with an installed binding corrective return to whole-current management; skill evaluations instead belong to future capability modification.

## S4 — Outside-and-then intelligence

- State: A
- Function: Convert externally encountered use cases and failures into tested future changes in installed skill discovery or task capability, retained for later runs.
- Disturbance / variety regulated: Skill routing misses on real user/task queries, insufficient skill quality on held-out assertions and persistent learned user behavior needs requiring changed future agent capability rather than repair of one current task.
- Decisive decision or feedback right: Model-based proposer chooses revised skill descriptions/body or behavioral rule candidate; validation results select the best held-out performer, and source optimizer installs the selected revision that future model runs load.
- Decision owner: Model-based skill proposer with first-party evidence-driven automatic best-candidate selection in the supported **non-dry-run optimize-description** mode; user may initiate the improvement run but does not have to choose the winning description. `rules promote` is a separate operator-selected candidate admission path and is not credited as autonomous winner selection.
- Supporting / enforcement mechanisms: `proposeInstincts` LLM candidate generation, split train/validation trigger tests, runTriggerEval, writeDescription, `promoteRule` optional trigger/quality gates, rules/skills loader and persisted Markdown skill files.
- Closure path: Changing external task queries/observed use failures → optimizer collects failures and prompts model for prospective changed skill description → reruns train and held-out validation → chooses best measured candidate and overwrites live `SKILL.md` if not dry-run → subsequent runtime loads changed skill catalog/activation descriptions into a new execution.
- Boundary reachability: Source CLI directly invokes `buildLiveDescriptionProposer` and `optimizeDescription` without an external repair implementation; by default the command applies the selected best description, which is loaded by first-party `buildSystemPrompt` during later sessions. Optional auto-approved quality optimization likewise writes changed content.
- Why this is / is not agent-owned: The proposer is model-powered and the selection depends on actual tested query outcomes, with a future-capability artifact write; merely configuring a provider would not count. This is A at the **harness-improvement mode**, not automatic improvement of all production deployments or a guarantee of positive benchmark efficacy.
- External distinction: User/task trigger queries and observed failure cases represent variations in the environment that the skill description must recognize; separate validation examples approximate future unseen use.
- Future / prospective distinction: Changed skill discovery description or validated rule is intended for next sessions and not solely finishing the current request.
- Adaptation option generated: New model-proposed skill description, or a skill-content/rule candidate based on prior sessions; compared against baseline train/validation or quality gates.
- Path back into current capability / S3: Accepted update persists in the installed `SKILL.md` or `rules/<id>.md`; the next harness boot/context load activates its changed behavior (there is no independently assessed S3 manager, so this is direct return into the S1 capability and local current operation, not invented S3 ownership).
- Evidence: [LLM proposal and optimize wiring](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/cli/index.ts#L3490-L3570), [real description training/validation/selection/write](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/optimize-description.ts#L35-L113), [model proposer implementation](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/evals/agent-runner.ts#L118-L153), [runtime loads updated skill description](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/context-loader.ts#L100-L137), [rules promoter quality admission](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/promote-rule.ts#L25-L76), [rules subsequently loaded](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/context-loader.ts#L78-L94).
- Basis: Executable prospective model option generation, explicit held-out selection and source-file install.
- Confidence: Medium-high structural; no real LLM skill-optimization experiment independently run here.
- Caveats: **Do not equate `learn --install` with installed effective runtime rules:** this writes `instincts/` while `buildSystemPrompt` loads `rules/`. For learned rules to change next-run behavior, `rules promote` must write into `rules/`, or an optimizer must modify directly loaded skill files. `optimize-quality` requires `--auto-approve` to apply. No empirical quality gain or autonomous periodic promotion is claimed.

## S5 — Policy and identity

- State: —
- Function: Legitimate durable purpose, identity and ultimate policy deciding tensions between present goals and future adaptation.
- Disturbance / variety regulated: Conflicting identity/ethos claims, ultimate choice of what a durable agent may become beyond present task constraints.
- Decisive decision or feedback right: No source-connected legitimate ultimate policy adjudication/return path identified.
- Decision owner: Not established; IDENTITY.md supplies configured system behavior, approval policies limit tools and user can edit documents outside an internally governed constitutional decision loop.
- Supporting / enforcement mechanisms: IDENTITY.md/CORE.md loader, runtime rules, approval gates, guardrails, provider configuration and CLI file editing.
- Closure path: No detected identity-level dispute → legitimate ultimate authority → binding decision → returned new governance of future run cell. File contents and user preference are configuration, not constitutive S5 by themselves.
- Why this is / is not agent-owned: Model may obey an identity prompt but does not legitimately resolve changes to ultimate mission; user tool approval does not amount to whole-system constitutional policy.
- Evidence: [identity load](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/context-loader.ts#L20-L59), [tool approval](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/runtime/approval.ts#L1-L143), [config/constraints](https://github.com/Phoenixrr2113/agent-harness/blob/0f67103affd30a3c778874b890dbd5801cdbd94f/src/core/config.ts#L1-L150).
- Basis: Bounded negative after identity-like and permission surfaces.
- Confidence: Medium-high within standalone harness source.
- Caveats: A consumer might supply an external human/organizational ultimate authority, not included in this first-party operating boundary.

### Absence scope

- Surfaces inspected: IDENTITY.md load, rule/skill system prompt, approval config, CLI config, agent state, learning/autonomy, scheduler and verification/health controls.
- Plausible first-party paths checked: Agent proposes changing its own identity, human rule approvals, user changing provider/rules, dynamic learning of new behaviors.
- Why no material first-party path remains: These paths configure/learn task behavior but not a legitimate ultimate identity authority that receives and returns final constitutional decisions.

## Recursion

- Parent context: Human/adopter selects agent installation purpose, provider, permissions and installed goal work; it is external legitimate authority, not automatically credited as first-party S5.
- Operational S1s: Independently goal-directed agent sessions, durable workflow steps and model-backed delegateTo specializations when configured; tooling/skill activation are S1 support, not extra autonomous companies.
- Current regulation: Lock/owned-file constraints synchronize overlapping state writes; model run has S1 local decisions but no established current multiunit S3 governance.
- Future capability: Source-supported skill optimization creates/test/selects future skill descriptions and changes the next-use routing surface; no broader upstream corporation's strategy is borrowed.

## Variety and escalation

- Model/tool/local task variety flows from external user goal into first-party `generateWithAgent` and tool observations, returning session records/answers.
- S2 coordination locally prevents overwriting shared mutable state when multiple session/workflow actors operate on one harness.
- Guardrails, deterministic scheduler, verification gates and durable retries constrain run execution without granting S3/S3* autonomy.
- Later skill behavior can change through opt-in model-proposed held-out-evaluated revision and installed runtime update; `learn --install` instinct files alone are a known insufficient return path.
- Ultimate mission changes remain external decisions with no source-connected S5 legitimacy path.

## Evidence gaps

- Frozen source at `0f67103...` MIT, Node TypeScript 0.18.0, package lock/dependencies inspected. No real user LLM API or real Ollama end-to-end model run was executed.
- Full Vitest on isolated VM **1476 tests: 1466 PASS, 9 FAIL, 1 SKIP, 1 unhandled EPIPE** under highly concurrent default workers; all nine failures were 5-second per-test process/setup timeouts across six files, plus a separate trigger test EPIPE. Reran all affected files with `--maxWorkers=2 --testTimeout=30000`: **44/44 PASS**. This does not retroactively turn the first full run into a full all-green benchmark.
- Frozen upstream `npm run lint` (`tsc --noEmit`) PASS. The opt-in real Ollama learning-loop test is disabled unless `INTEGRATION=1`; its success and measurable quality delta are **not** claimed.
- Multi-agent inter-S1 lock witness is structural and narrow. Locking alone is not negotiated policy or whole-current management autonomy. An unconfigured single-agent installation cannot be treated as multiple S1 units.
- `learn --install` saves instincts outside the active rules prompt loader; S4 positive is specifically based on independently source-wired `optimize-description` and evaluated `rules promote` update paths that actually change live loaded capability, not the README's unconditional self-improvement assertion.
