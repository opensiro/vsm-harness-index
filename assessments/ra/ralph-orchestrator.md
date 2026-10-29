---
harness_id: ralph-orchestrator
project_name: Ralph Orchestrator
repository: https://github.com/mikeyobrien/ralph-orchestrator
review_ref: b5789dfbb25bd4aa65ce565c756d95acc8c42f76
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Ralph Orchestrator

## Review boundary

- System in focus: one deployed Ralph orchestration run and its optional first-party parallel worktree loops, from a supported CLI/preset to actual model-backed backend invocations, durable event/task/memory files, review and optional merge-loop feedback. The external coding-agent CLI/model supplies the per-iteration intelligence; Ralph supplies the first-party organizational loop and assigned roles.
- Purpose and identity: drive an open-ended development/research/review task to evidenced completion through model-directed iterations, persistent state, role-specific event handoffs and bounded termination.
- Relevant environment: operator goals, changing repository/worktree contents, CLI/model backends, failed tools and verification, running sibling worktrees, conflicts, cost/runtime constraints and optional Telegram operator guidance.
- Standard-distribution boundary: shipped Rust `ralph-cli`, `ralph-core` and backend adapters, bundled `code-assist`/`review`/`merge-loop` presets, supported optional worktree/auto-merge and RObot modes. A project configuration and installed external agent backend are normal prerequisites, not assumed Ralph-owned model software.
- Credited operating / distribution surfaces: `ralph run` event loop, durable task/event/memory handling, bundled model-backed hats, `code-assist` Critic rejection/repair feedback, and the supported *selected* `features.parallel: true` plus `features.auto_merge: true` merge-loop mode. The positive S2 and S3* claims are mode-specific, not properties of every solo run.
- Adjacent first-party surfaces excluded from ownership: internal E2E fixtures, CI, package/release automation, web UI/dashboard visualization, benchmark scripts, documentation examples and the repository-maintainer organization. The external Claude/Codex/Kiro/OpenCode/Pi CLI and provider policy/agent engine are separate; their unwrapped capabilities are not automatically credited.
- First-party operating / deployment modes considered: default solo `ralph run`; configured hat-based `code-assist` with independent Critic and Finalizer; review-only preset; parallel worktree mode with auto-merge explicitly opted in; optional RObot human steering. No claim that all roles and auto-merge run simultaneously by default.
- Recursion level: a task/loop is one operational cell; under parallel mode distinct worktree loops are operational S1 cells within a repository-level orchestration/merge boundary. Merely spawning an iteration or hat is not a new viable-system recursion.
- Reviewed revision: `mikeyobrien/ralph-orchestrator@b5789dfbb25bd4aa65ce565c756d95acc8c42f76` (shallow first-party checkout, exact Git HEAD; MIT license).
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust CLI repeatedly calls a selected backend agent, injects task/event context and active hat instructions, processes model-published events and routes them to the next hat. The `EventLoop` registers named hats plus a universal Ralph fallback, persists loop state and retains task/memory/scratchpad continuity. The model chooses work actions and event payloads; routing, state serialization and limit enforcement are first-party deterministic supports. The built-in `code-assist` prescription connects model Planner → Builder → fresh-eyes Critic → Finalizer and returns `review.rejected` to Builder or `queue.advance` to Planner. [Core event loop](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs), [CLI execution](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/src/loop_runner.rs), [supported code-assist preset](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/code-assist.yml).

Parallel CLI runs may occupy distinct Git worktrees. With `auto_merge` specifically enabled, completed loops are queued and a separate first-party `merge-loop` agent receives each branch, reads conflicting code, resolves merge conflicts semantically, runs verification and returns a merge or actionable failure state. The durable queue and file locking do not themselves choose how to reconcile incompatible changes. Importantly, `auto_merge` defaults to **false**: the coordination claim applies to its available opt-in mode. [Feature defaults](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/config.rs), [completion-to-queue path](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/loop_completion.rs), [merge-loop spawn](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/src/loop_runner.rs), [merge-loop roles](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/presets/merge-loop.yml).

RObot supports model-origin human questions, inbound mid-loop guidance and per-loop routing. Human answers influence ordinary task direction; status, budget, reset and completion guards enforce configured policies. The reviewed code does not turn these surfaces into a general autonomous whole-system controller, an external/future adaptation authority or identity-level policy tribunal. [RObot user flow](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/README.md), [termination handling](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs).

## Operational model

In a normal solo task, the backend model decides what to inspect/edit/test next within the user's prompt and the selected hat. Ralph controls when to invoke that model and how events, checkpoints and termination are carried. In `code-assist`, Planner and Builder are task roles of successive model invocations, while Critic inspects the resulting *actual source and tests* and independently chooses rejection or pass; this is a supported separate corrective access mode, not just logging. In selected parallel auto-merge operation, independent worktree loops produce candidate changes and the merge-loop model resolves interference at the common repository boundary; deterministic queue/locks transport the conflict and resulting state. No inference is made from the provider's own external organization, CI or repository maintainer governance.

## S1 — Operations

- State: A
- Function: produce working code, review or researched task artifacts through model-directed tool-use iterations against a real project environment.
- Disturbance / variety regulated: changing source/tool outputs, failing tests, partial code, unavailable backend responses and unresolved task requirements.
- Decisive decision or feedback right: the active backend agent selects investigation, edits, tests and event/continuation response, within the supplied role and user task.
- Decision owner: model-backed agent session invoked in the supported Ralph loop, not the deterministic `EventLoop` dispatcher.
- Supporting / enforcement mechanisms: backend adapters, prompt/hats, event bus, tasks/memory/scratchpad, persisted iteration state and cost/runtime/failure guardrails.
- Closure path: user objective → Ralph invokes model backend with current context → model executes tools and emits state/event → Ralph stores outcome and selects subsequent iteration/hat → subsequent model action or evidence-backed completion.
- Boundary reachability: `ralph run` with a configured supported backend is the public CLI path, not a development-only demo; `code-assist` is a bundled preset.
- Why this is / is not agent-owned: removing model decision-making leaves an event dispatcher and durable state, not the task-specific source-changing choices.
- Evidence: [backend execution/iteration](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/src/loop_runner.rs), [event/hat dispatch](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs), [Builder's actual TDD/tool duty](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/code-assist.yml).
- Basis: structural shipped execution path plus explicit role prescriptions and unit/E2E fixture coverage.
- Confidence: high for available autonomous S1 path, without claiming a paid live model run in this review.
- Caveats: Ralph depends on externally installed agent backends; hard runtime limits and fixed role prompts constrain but do not themselves own task action selection.

## S2 — Coordination

- State: A
- Function: reconcile conflicting outputs of distinct concurrently operating worktree-loop S1 cells before they can become one coherent repository state in the **selected auto-merge mode**.
- Disturbance / variety regulated: independently completed branches can modify overlapping files or introduce mutually incompatible behavior; unsynchronized merges can break the shared working tree.
- Distinct S1 units: separately executing model-backed Ralph loops in distinct Git worktrees, each contributing a task branch rather than only successive hats of a single loop.
- Inter-S1 disturbance: two independent loop branches may edit the same file or cause a test failure when combined, so blindly admitting both would corrupt or destabilize the shared project.
- Attenuating coordination relation: completed worktree loops submit to the durable merge queue; selected merge-loop mode uses a model-driven Branch Merger/Conflict Resolver and verification stages against the shared target branch.
- Feedback into subsequent S1 behaviour: merge success makes the reconciled output available on main for later work; conflict/failing-test outputs lead the model to repair or leave an explicit needs-review state for the next operational decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path explicitly detects and resolves **incompatible outputs of distinct operating loops** at their common repository boundary, not merely delivering the next task event.
- Decisive decision or feedback right: on a substantive conflict, the merge-loop model chooses how to preserve both branch intents and repair failing merged behavior; queue locks only transport and gate this discretion.
- Decision owner: dedicated merge-loop model agent in the first-party preset; Git/file-lock state and test runner are supporting deterministic mechanisms.
- Supporting / enforcement mechanisms: worktree isolation, `MergeQueue` durable states, CLI subprocess spawning, Git merge/test invocations, conflict events and failure/needs-review escalation.
- Closure path: independent loop outputs → queued branch → merge-loop conflict evidence/diff → model selects reconciliation/repair → changed main branch and verified outcome (or explicit unresolved state) → subsequent loops use new codebase.
- Boundary reachability: parallel worktrees are supported; enabling shipped `features.auto_merge` actually enqueues and starts the bundled merge-loop preset after completion. The default manual-merge mode is **not** claimed to have autonomous S2.
- Why this is / is not agent-owned: the queue serializes transport but cannot semantically reconcile a C++/Rust/source conflict or choose correct combined behavior; a configured model agent does that in the positive mode.
- Evidence: [worktree completion queue](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/loop_completion.rs), [merge queue states and locks](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/merge_queue.rs), [merge-loop spawn](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/src/loop_runner.rs), [resolver/merger/tester roles](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-cli/presets/merge-loop.yml), [parallel and auto-merge defaults](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/config.rs).
- Basis: explicit configuration, positive source-level feedback path, and merge-queue/loop tests; no live merge conflict generated in this assessment.
- Confidence: medium-high for selected supported coordination path; real conflict-resolution quality remains unmeasured.
- Caveats: `auto_merge` is disabled by default and conflict resolution depends on the external model backend. In a solo or manual-merge-only deployment there is no positive S2 at the declared multi-loop relation.

## S3 — Inside-and-now control

- State: —
- Function: no first-party model/parent controller with a whole-system current operating view and discretionary authority over all live loop commitments/resources was established for the assessed task/parallel-loop boundary.
- Disturbance / variety regulated: cost exhaustion, runtime failure, stale iterations, merge backlog and human-requested correction, mostly handled as local stop/retry/queue mechanics.
- Decisive decision or feedback right: configured budgets, maximum iterations, scheduler/role selection and operator interventions; these are preset/deployment policy or task-local operational choices, not an evidenced whole-system S3 judgment.
- Decision owner: developer/operator for limits and selected task mode; backend agents for their own task work. No qualifying first-party S3 owner demonstrated.
- Supporting / enforcement mechanisms: `LoopState`, `TerminationReason`, per-loop RObot status, merge queue, TUI/web status and runtime config.
- Closure path: local failure/cost signals stop or retry a loop; there is no established decision from a total current operational view into revised cross-loop commitments or priorities.
- Why this is / is not agent-owned: stopping at a configured limit or displaying multiple loops does not transfer current-system resource discretion to an autonomous agent; merge reconciliation is S2, not whole-system S3.
- Evidence: [termination and state](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs), [configuration of limits and parallel mode](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/config.rs), [operator interface](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/README.md).
- Basis: bounded structural negative after active role, loop, merge and operator path review.
- Confidence: medium; whole-system control was not inferred from the product's “orchestrator” label.
- Caveats: an external human project manager may provide S3 at a higher recursion, but their wider organization is not packaged as Ralph's first-party S3.

### Absence scope

- Surfaces inspected: main `ralph run` event loop/termination, preset Planner/Finalizer and other hats, merge queue/auto-merge, parallel worktrees, RObot status/guidance and config limits.
- Plausible first-party paths checked: single-run Finalizer, multi-loop merge queue, cost/runtime guard, Telegram operator control, dashboard/status and optional wave aggregation.
- Why no material first-party path remains: these paths finish a task, resolve inter-loop merge interference, enforce preselected limits or relay per-loop human guidance. None supplies a shipped model/parent whole-system current view **and** returned, discretionary resource/commitment intervention for the group.

## S3* — Complementary audit

- State: A
- Function: challenge an implementer's reported success with a fresh model-backed inspection of actual changed code, tests and failure paths, returning an independent correct/reject judgment to the implementation loop.
- Disturbance / variety regulated: false-positive builder completion, hidden regression, failed requirement/edge case and claims based only on self-reported test success.
- Claim being audited: Builder's `review.ready` assertion that its task-specific code increment and verification satisfy acceptance criteria.
- Ordinary reporting path: Builder emits `review.ready` after code/test work with task identity and claimed result.
- Complementary access path: bundled `code-assist` **Critic** is a different hat/backend invocation, told to inspect *actual changed source*, rerun verification and an adversarial failure scenario instead of trusting Builder. The separate review-only preset provides an additional independently selectable direct-code inspection mode.
- Independence boundary: role-separated Critic has independent review instructions, fresh turn context and an explicit pass/reject decision; no claim of external organizational independence or a separately audited provider model.
- Who acts on findings: `review.rejected` activates Builder for repair; `review.passed` permits Finalizer to assess whole-task completion; subsequent task state reflects rejection/repair rather than accepting Builder's assertion automatically.
- Decisive decision or feedback right: Critic model decides whether code evidence supports pass or requires rejection/correction.
- Decision owner: Critic's separate model-backed role, not deterministic event routing or the Builder that authored the increment.
- Supporting / enforcement mechanisms: `review.ready` event, hat subscriptions/publications, task IDs, required review event, backend execution and task/verification persistence.
- Closure path: Builder source changes and `review.ready` → Critic independently inspects code/tests → `review.rejected` or `review.passed` → Builder repairs or Finalizer reviews completion → subsequent work acts on auditor judgment.
- Boundary reachability: first-party published `code-assist` preset directly wires Builder/Critic/Finalizer and passes these events through `ralph run`, with no custom external audit plugin required.
- Why this is / is not agent-owned: Critic's adverse code/test diagnosis is model discretion; the event bus only delivers its choice. Ordinary self-tests alone would not meet the complementary independence test.
- Evidence: [Critic, role separation, actual runtime/failure-path check and rejection](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/code-assist.yml), [hat event routing](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs), [separate adversarial review preset](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/review.yml).
- Basis: explicitly shipped separate-agent review instructions and structurally closed pass/reject feedback.
- Confidence: medium-high for selected mode; actual auditor independence/accuracy was not measured with live backend invocations.
- Caveats: separate role invocation is narrower than external auditor independence; solo/preset-without-Critic runs do not acquire S3* from ordinary tests. This verdict is restricted to supported code-assist Critic mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped loop was established that senses externally/future-relevant changes, evaluates prospective options for **Ralph's own operating capability** and closes a strategic adjustment into current whole-system control.
- Disturbance / variety regulated: changing coding-task details, research questions, locally measured improvement experiments and memory of task errors, rather than a sustained whole-system environmental-future strategy.
- Decisive decision or feedback right: agent/Strategist may plan a project experiment or choose an implementation adjustment; operator chooses new goals/backends/presets.
- Decision owner: task agent for bounded research/optimization operations; user/developer for Ralph's model/capability policy. No separate first-party S4 right established at this boundary.
- Supporting / enforcement mechanisms: `research` and `autoresearch` task presets, memories, experiment logs, benchmark/rubric loops, configurable backend/hats.
- Closure path: experimentation can improve the **user's target artifact** inside the active S1 task, but no evidenced future-environment model returns a capability/governance decision to a Ralph-level S3 loop.
- Why this is / is not agent-owned: agent-driven experiment planning is not automatically S4; its object is usually an operational deliverable, with no separate S3–S4 long-horizon conversation.
- Evidence: [autoresearch experiment preset](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/autoresearch.yml), [research-only preset](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/presets/research.yml), [core configuration](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/config.rs).
- Basis: structural negative with explicit consideration of shipped positive experiment modes.
- Confidence: medium.
- Caveats: a human can employ Ralph to study future technologies, but such use does not by itself install an S4 for the harness at this recursion.

### Absence scope

- Surfaces inspected: `research`/`autoresearch` experiment roles and logs, task memory, normal code-assist planning, backend selection, runtime limits and merge-loop.
- Plausible first-party paths checked: Strategist/Measure/Judge optimization, dynamic research findings, persistent learnings and ability to change source/backends.
- Why no material first-party path remains: these are model-directed *task operations* or operator-selected configurations, without a supported external-and-prospective whole-system intelligence loop returning options into current Ralph system capability/S3 regulation.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy decision channel with legitimate governing authority and return to the running harness was established.
- Disturbance / variety regulated: operator prompt changes, content/approval bounds, safe defaults, per-task human help, backend configuration and resource ceilings.
- Decisive decision or feedback right: user/developer selects the task, configuration and permissions; the model can ask for task clarification but no identity-level matter is routed to a governing parent S5 by first-party protocol.
- Decision owner: external user/deployment policy, not an autonomous Ralph S5 or evidenced operationally closed parent S5.
- Supporting / enforcement mechanisms: guards, configurations, RObot `human.interact`, Telegram commands, stop/restart, role prompts, Git safety/merge defaults.
- Closure path: human guidance changes a task iteration or deployment config, but no identity/ultimate-policy proposal → legitimate parent ruling → returned durable policy decision is defined for this system-in-focus.
- Why this is / is not agent-owned: approvals and human messages regulate immediate tasks; static instructions are not themselves identity policy deliberation or S5 closure.
- Evidence: [human interaction/Telegram scope](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/README.md), [loop event/termination policy](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/event_loop/mod.rs), [configurable support modes](https://github.com/mikeyobrien/ralph-orchestrator/blob/b5789dfbb25bd4aa65ce565c756d95acc8c42f76/crates/ralph-core/src/config.rs).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: the maintainers' development governance or a deployment owner's wider organization may supply higher-recursion S5, but that is not the selected packaged task/loop boundary.

### Absence scope

- Surfaces inspected: task/persona config, backend/CLI setup, guardrails, human interaction/RObot, completion and merge safety, published presets and operator docs.
- Plausible first-party paths checked: Telegram request/response, `human.interact` escalation, human merge steering, preset policy edits and hard safety limits.
- Why no material first-party path remains: every observed human/model path concerns local execution, merge/review or preconfigured limits; none carries a genuine identity-level matter to legitimate ultimate authority and returns a governing policy ruling into subsequent harness operation.

## Distributed OSS parent arrangement

Public contributors and maintainers develop the project, but the reviewed deployed CLI does not include a shared maintainer-organization parent decision loop. Local operator instructions and task guidance are not evidence that a distributed project S3/S4/S5 parent is wired into the assessed runtime.

## Self-hosted and non-human modes

Self-hosting permits model/agent backend selection, local configuration, manual merge and Telegram steering. These modes constrain task autonomy but do not independently establish a second parent S3/S4/S5 mode. The optional model-led merge and critic modes are separate supported functional circuits; no `(P)` is inferred.

## Recursion

One loop has a local operational task identity, but its hats are successive dispositions of one operation, not individually proven viable systems. In parallel mode multiple worktree loops are distinct operating cells whose merged output must coexist; the merge-loop is their cross-cell S2 support. The external backend agents may contain their own recursions not assessed here.

## Variety and escalation

Task variety enters through code/test/tools and model interpretations; event/task stores compress and preserve continuity. Runtime/stale/cost limits and failed merge states attenuate uncontrolled repetition. Critic rejection returns counter-evidence into an implementer turn; RObot relays exceptional task uncertainty to a human. None of these signals alone establishes S3/S4/S5 ownership. Unresolvable merges and task human questions stay visible rather than being silently reclassified as governance.

## Evidence gaps

- No paid/live external-model run was executed in this assessment; role/loop closures are supported by pinned first-party code, shipped presets and deterministic tests, not measured model correctness.
- The selected auto-merge S2 mode is opt-in and may have operational safety limits under truly concurrent large merges; no universal guarantee of serial conflict-free integration is asserted.
- Critic independence is relative to a distinct model role/invocation, not a security-grade independent organization. Positive S3* is limited to the explicit Critic feedback mode.
- The bounded S3/S4/S5 negatives do not exclude richer parent governance composed by a deployment owner or future plugin.
