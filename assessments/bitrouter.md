---
harness_id: bitrouter
project_name: BitRouter
repository: https://github.com/bitrouter/bitrouter
review_ref: e2a8c644e8ece5a2f152d2516269497d23aeef5d
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# BitRouter

## Review boundary

- System in focus: one first-party BitRouter installation at pinned revision `e2a8c644e8ece5a2f152d2516269497d23aeef5d`, including the local routing daemon, `bro code` / `bro run` / ACP controller paths, daemon-owned supervised-run state, policy/eval/optimization machinery, worktree/directory claims, route controls, checkpoint/evidence surfaces and local/remote administration interfaces.
- Purpose and identity: provide a coding-agent execution and routing control plane that launches or proxies autonomous coding-agent sessions, supervises their current lifecycle, routes model traffic under signed policy and can evolve routing policy from admitted evaluation evidence.
- Relevant environment: human/operator; autonomous Claude/Codex/other ACP harnesses; upstream model providers; project repositories/worktrees; task-native tests and external evaluators; authenticated Eval writers; local/remote control clients; operating-system processes and SSH worker environments.
- Standard-distribution boundary: BitRouter-owned daemon/CLI/TUI/ACP supervisor, policy runtime, Eval Exchange and optimization/evolution paths. External ACP harnesses and model providers remain separate actors; their internal coordination, planning, verification, memory or governance functions are not inherited. SSH workers are execution environments rather than donated decision loops.
- Credited operating / distribution surfaces: `README.md`; `skills/bitrouter/SKILL.md`; `skills/bitrouter/references/sessions.md`; `skills/bitrouter/references/adaptive-routing.md`; `apps/bitrouter/src/supervisor.rs`; `apps/bitrouter/src/agent_sessions.rs`; `apps/bitrouter/src/acp_cli.rs`; `apps/bitrouter/src/optimization/controller.rs`; `apps/bitrouter/src/policy_compile.rs`; `docs/AGENTIC_OPTIMIZATION_SPEC.md`; `docs/ACP_EVOLUTION_SPEC.md`; `docs/BACKGROUND_AGENT_UX_SPEC.md`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; benchmark fixtures and experiment records except as corroboration; upstream ACP adapter internals; external evaluator semantics beyond the evidence they submit; remote worker operating systems and provider implementations.
- First-party operating / deployment modes considered: foreground ACP session; daemon-supervised background runs; `bro agents` / Code control deck; local ACP controller and route controls; explicit parent/operator controls; generic Eval submission; `optimize run`; low-level snapshot/compile/diff/publish/restore/evolve policy workflow; adaptive and frozen routing modes.
- Recursion level: one BitRouter-managed local coding organization is the system-in-focus. Autonomous ACP coding sessions are operational S1 units when launched through the first-party controller/supervisor relation. Harness-native internal child agents remain inside their external harness boundary unless a typed first-party relation exposes them; process trees/logs are explicitly not used to infer them.
- Reviewed revision: `e2a8c644e8ece5a2f152d2516269497d23aeef5d`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

BitRouter combines an LLM/model-routing daemon with an ACP execution/control plane. Foreground `bro run` and `bro code` launch supported coding harnesses through BitRouter's ACP controller; background runs move controller ownership into the resident daemon so they survive client exit. The supervisor records typed run state, pending permissions, activity, route/cost state, review state and lifecycle events, and exposes exact start/list/peek/attach/respond/stop/remove capabilities plus generation-fenced mutations. The autonomous coding harness/model remains the operational reasoner.

The supervisor is deliberately a control primitive rather than an autonomous manager. A `RunSnapshot`/`RunSummary` exposes current supervised runs and a `SessionAction` can prompt, cancel, answer a permission, select/configure a session, change/reset route or mark review state. The shipped `bro agents` / Code control deck gives a human parent an operational current-control mode. A downstream manager can also compose the same first-party protocol, but BitRouter does not package a separate autonomous agent that decides the whole-current control interventions by default.

BitRouter also implements a substantial adaptation pipeline. The daemon creates redacted Eval subjects from settled routed work; task-native tests, humans, BitRouter agents or private evaluators can submit immutable results. `optimize run` freezes admitted evidence and deterministically chooses an exploration, promotion, retreat, hold or convergence transition, then can atomically publish/reload the successor policy. Low-level `eval snapshot freeze`, `policy compile`, `policy diff`, `policy publish`, `policy evolve` and restore/withdraw surfaces expose the same function for separately managed workflows and direct operator governance.

The optimizer's publication authority is strong but does not make S4 `A`: Methodology 0.3.6 assigns `A` only when an autonomous agent owns the decisive organizational judgment. `optimization/controller.rs` makes the transition through deterministic controller logic and cohort gates. That machinery can enforce or transport a selected adaptation without itself becoming an autonomous-agent decision owner.

## S1 — Operations

- State: A
- Function: perform bounded coding/task work in a target workspace through autonomous ACP coding-agent sessions launched and routed by BitRouter.
- Disturbance / variety regulated: user task uncertainty, repository/worktree state, model/tool outcomes, permissions/questions, provider/model availability, route policy, session continuation and failure/timeout conditions.
- Decisive decision or feedback right: choose substantive task-local reasoning, model/tool actions and completion behavior inside the launched coding session.
- Decision owner: the autonomous external ACP coding-agent/model actor reached through BitRouter's first-party standard controller/launch path.
- Supporting / enforcement mechanisms: ACP controller; provider/model routing; daemon supervisor; worktree/directory claims; permission broker; timeout/cancel; route leases; model metering; attach/detach and native-session lifecycle.
- Closure path: user/manager starts or prompts a BitRouter-controlled coding session → BitRouter launches/initializes the configured ACP harness and routes its model traffic → autonomous worker chooses task actions → ACP/tool/model feedback returns to the worker → session continues or settles → BitRouter exposes resulting state to the metasystem.
- Boundary reachability: `skills/bitrouter/SKILL.md` documents `bro code`, `bro run` and background runs as normal product paths; `skills/bitrouter/references/sessions.md` and `apps/bitrouter/src/supervisor.rs` implement controller launch and daemon-owned sessions.
- Why this is / is not agent-owned: BitRouter deterministically routes, persists, meters and supervises execution but does not choose the code/task solution. Removing the external autonomous coding actor leaves a control/runtime plane without substantive operational reasoning.
- Evidence: [`skills/bitrouter/SKILL.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/SKILL.md); [`skills/bitrouter/references/sessions.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/sessions.md); [`apps/bitrouter/src/supervisor.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/supervisor.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: internal VSM functions of Claude, Codex or other harnesses are not inherited; the positive finding credits only their reachable task-local S1 role under the first-party launch/control relation.

## S2 — Coordination

- State: —
- Function: no complete installation-level S2 mutual-adjustment loop is established among sibling coding-agent S1 units.
- Disturbance / variety regulated: BitRouter prevents two potentially writable supervised runs from claiming the same canonical Git worktree/directory by default and supports independent worktrees, but this is pre-launch admission/isolation rather than an evidenced coordination decision fed back into subsequent behavior of already-established sibling S1 units.
- Decisive decision or feedback right: no S2-specific inter-S1 behavioral adjustment right is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: worktree/directory claims; `--allow-shared-directory` override; route/policy constraints; run ledger; parent-child run identity; session event streams and permission brokering reduce collision/lifecycle variety without independently satisfying S2.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S2 loop was found in the standard supervisor/controller modes.
- Why this is / is not agent-owned: there is no established S2 function to classify. Deterministic collision rejection is enforcement of an isolation rule, not autonomous or constructor coordination discretion by itself.
- Evidence: [`skills/bitrouter/references/sessions.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/sessions.md); [`docs/BACKGROUND_AGENT_UX_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/BACKGROUND_AGENT_UX_SPEC.md); [`apps/bitrouter/src/supervisor.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/supervisor.rs).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: the same-worktree collision is a real inter-run hazard, but Methodology 0.3.6 additionally requires feedback that alters subsequent S1 behavior. Here the second writer is rejected before launch and the correction belongs to the manager/operator; separate worktrees are preventive isolation rather than sufficient S2 evidence.

### Absence scope

- Surfaces inspected: supervisor run claims; parent-run identities; ACP events; multi-agent control deck; background-run lifecycle; route/session controls; worktree collision handling; external/native child-agent visibility.
- Plausible first-party paths checked: same-worktree write collision; multiple supervised runs; harness-native child agents; shared routing/model constraints; parent/child run relations; permission contention.
- Why no material first-party path remains: BitRouter can isolate or reject potentially conflicting runs and show them together, but no reviewed standard path reconstructs an interaction-generated sibling disturbance, an S2-specific coordination judgment and a returned adjustment into subsequent behavior of the sibling S1s.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain a whole-current view of supervised coding runs and expose present-control interventions over their lifecycle, permissions, routes, prompts/configuration, review state and termination.
- Disturbance / variety regulated: running/idle/failed/interrupted agents, unresolved permissions/questions, incorrect route/configuration, concurrent workspace claims, review-ready turns, attachment/control ownership and runs that need cancellation or intervention.
- Decisive decision or feedback right: choose whether/how to start, prompt, configure, route, answer, cancel, mark reviewed, stop, attach or remove supervised runs based on current organization state.
- Decision owner: constructor mode — not supplied; BitRouter exposes a function-specific control protocol for a downstream autonomous manager. Parent mode — the human/operator through the shipped `bro agents` / Code control-deck surfaces owns the current intervention decision.
- Supporting / enforcement mechanisms: `RunSummary`/`RunSnapshot`; typed lifecycle/event journal; exact command scopes; generation-fenced control leases; session mutations; worktree claims; attention/review state; daemon process ownership.
- Closure path: supervisor exposes current run inventory and detailed snapshots → manager/operator identifies a present-control issue → a first-party session command/mutation is issued → daemon applies it to the live controller/run → updated typed state/events return to the control surface and subsequent operation changes.
- Boundary reachability: background sessions, `bro agents`, attach/stop/remove and the daemon owner-scoped local session-control protocol are shipped standard product paths.
- Why this is / is not agent-owned: the function is materially implemented, but the repository does not package an autonomous agent that owns the current-control judgment over the run set. Deterministic daemon state transitions enforce a caller's selected intervention. The human parent mode is closed and explicit.
- Evidence: [`skills/bitrouter/references/sessions.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/sessions.md); [`docs/BACKGROUND_AGENT_UX_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/BACKGROUND_AGENT_UX_SPEC.md); [`apps/bitrouter/src/supervisor.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/supervisor.rs); [`apps/bitrouter/src/agent_sessions.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/agent_sessions.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `Ready for review`, queue/lifecycle state, timeout and deterministic route enforcement are evidence/support mechanisms, not autonomous S3 ownership by themselves.
- Whole-system current view: the supervisor's list/snapshot projections expose run identity, agent/session identity, directory claim, process/turn/attention/attachment/review states, activity, route, attributed cost, pending permissions, failure, lease and timestamps across daemon-owned runs.
- Current-control decision scope: start; prompt/respond; cancel; permission choice; select native session; set mode/config; route set/clear; mark reviewed; attach/takeover; stop; remove.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous manager must be composed | typed whole-run state indicates a current-control intervention | manager reads first-party list/snapshot/event state and issues the function-specific `SessionCommand`/`SessionAction`; supervisor applies it and returns updated state | `apps/bitrouter/src/supervisor.rs`; `skills/bitrouter/references/sessions.md` |
| Parent (`P`) | human/operator | Code/`bro agents` shows Needs input, Ready for review, error, active run or requested lifecycle action | operator uses shipped control deck/attach/stop/respond/route/review controls; daemon mutates live run state and later state reflects the decision | `docs/BACKGROUND_AGENT_UX_SPEC.md`; `apps/bitrouter/src/agent_sessions.rs`; `skills/bitrouter/references/sessions.md` |

## S3* — Complementary audit

- State: —
- Function: no current-operation complementary audit loop with materially independent challenge and corrective return to the operational S1 is established in the reviewed standard distribution.
- Disturbance / variety regulated: BitRouter records ACP sessions, freezes checkpoints, accepts human/agentic quality assessments, can invoke configured judges and exposes `Ready for review`; however these surfaces primarily support evidence, evaluation and future policy adaptation rather than an independent current-task audit that returns findings to repair the same operational work.
- Decisive decision or feedback right: no qualifying S3* audit judgment with corrective rework authority is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ACP recording; immutable checkpoints; assessment revision history; rubric/judge jobs; policy evidence verification; review-state markers and result schemas expose evidence but do not by themselves close S3*.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no standard first-party path was found that independently audits a worker completion claim and feeds a finding into a bounded worker repair/retry before acceptance.
- Why this is / is not agent-owned: an evaluator/judge can independently score historical checkpoint evidence, but its output is consumed by the learning/policy path or operator review. It is not sufficient to infer a current complementary-audit organization.
- Evidence: [`docs/ACP_EVOLUTION_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/ACP_EVOLUTION_SPEC.md); [`skills/bitrouter/references/sessions.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/sessions.md); [`docs/BACKGROUND_AGENT_UX_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/BACKGROUND_AGENT_UX_SPEC.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: the evaluation system is substantial and independent enough to support S4 evidence quality, but function mapping precedes ownership: evaluation of past coding outcomes is not automatically S3*.

### Absence scope

- Surfaces inspected: supervisor review state; ACP recordings/checkpoints; rubric prepare/submit; configured judge jobs; assessment revision/history; result schemas; Eval Exchange; policy evidence verification and optimizer cohort gates.
- Plausible first-party paths checked: Ready-for-review state; judge assessment; checkpoint quality scoring; `policy verify --evidence`; result-schema failures; manual review markers.
- Why no material first-party path remains: these paths record, score, validate or route evidence, but no standard loop independently challenges a worker's current completion claim and routes the audit finding back into a bounded repair action by that worker before the current result is accepted.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: learn from externally supplied/future-relevant quality and cost evidence, develop alternative routing policies for future tasks and return an adaptation into the active signed routing capability.
- Disturbance / variety regulated: current champion routes may be unnecessarily expensive, lower-cost challengers may preserve or degrade task quality, evaluator evidence may be insufficient/conflicting, and adopted routes can later show quality regressions.
- Decisive decision or feedback right: choose whether to explore a challenger, promote it, retreat/withdraw, hold, or converge; in low-level workflows choose whether a compiled candidate should replace the active policy.
- Decision owner: constructor mode — BitRouter supplies function-specific Eval, optimizer/controller, compiler, evidence/diff/publication and rollback/restore paths but no first-party autonomous agent owns the adaptation judgment. Parent mode — an operator can inspect/freeze evidence, compile/diff and explicitly publish/restore policy, closing a human-governed adaptation path.
- Supporting / enforcement mechanisms: immutable Eval Exchange; evidence roots; task/episode cohort gates; cost/quality/hard-violation checks; deterministic opportunity selection; signed experiments/rejection ledger; compare-and-swap policy parent digest; atomic policy-history publication; daemon reload/recovery; monitoring and withdrawal fences.
- Closure path: normal routed work produces redacted subjects → task-native tests/humans/agents/private evaluators submit admitted external quality/cost results → evidence is frozen/assessed → adaptation candidate or controller transition is developed → publication replaces the active signed policy and reloads the daemon → subsequent sessions route under the changed capability; later evidence can cause retreat/withdrawal.
- Boundary reachability: `skills/bitrouter/references/adaptive-routing.md` documents the normal history-driven lifecycle and low-level operator workflow; `optimization/controller.rs` implements exploration/promotion/retreat/hold/convergence over admitted evidence; the policy publication path updates live routing.
- Why this is / is not agent-owned: the adaptation function is strong, but `ControllerAction` is selected by deterministic code and cohort thresholds. Methodology 0.3.6 explicitly separates deterministic enforcement/selection machinery from autonomous-agent ownership. The repository also intentionally exposes the same function-specific primitives to a separately managed workflow, satisfying `C`, and a closed human operator path, satisfying `(P)`.
- Evidence: [`skills/bitrouter/references/adaptive-routing.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/adaptive-routing.md); [`docs/AGENTIC_OPTIMIZATION_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/AGENTIC_OPTIMIZATION_SPEC.md); [`docs/ACP_EVOLUTION_SPEC.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/docs/ACP_EVOLUTION_SPEC.md); [`apps/bitrouter/src/optimization/controller.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/optimization/controller.rs); [`apps/bitrouter/src/policy_compile.rs`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/apps/bitrouter/src/policy_compile.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: BitRouter documentation uses the phrase "autonomous controller step" for `optimize run`; that is product/runtime autonomy, not Methodology `A` unless an autonomous agent owns the decisive organizational judgment.
- External distinction: admitted quality/cost/latency/violation evidence comes from normal task outcomes and external evaluator authorities such as task-native tests, humans, agentic evaluators or private evaluators; it is immutable and authority-scoped rather than inferred from the live request alone.
- Future / prospective distinction: the system asks whether a different routing treatment should be explored or become the route for future task/episode cohorts, including post-adoption monitoring/withdrawal.
- Adaptation option generated: the controller/compiler creates signed exploration or successor policy states and can select candidate route treatments, promotion, retreat/withdrawal, hold or convergence.
- Path back into current capability / S3: atomic publication replaces the active policy lock, activates adaptive mode where required and reloads a reachable daemon; later routed sessions use that changed policy.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous adaptation actor must be composed around first-party function-specific surfaces | admitted Eval evidence and/or a separately managed optimization workflow indicates a candidate adaptation | actor can use Eval snapshot, compile/evolve/diff/publish/restore interfaces; signed publication changes active routing and subsequent operation | `skills/bitrouter/references/adaptive-routing.md`; `docs/AGENTIC_OPTIMIZATION_SPEC.md`; `apps/bitrouter/src/policy_compile.rs` |
| Parent (`P`) | human/operator | operator decides evidence justifies exploration/policy replacement or rollback | operator freezes/inspects evidence, compiles/diffs and explicitly publishes or restores a policy; publication/reload returns decision into live routing | `skills/bitrouter/references/adaptive-routing.md`; `docs/CLI.md`; `docs/ACP_EVOLUTION_SPEC.md` |

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established at the assessed recursion.
- Disturbance / variety regulated: signed routing policy, access policy, adaptive/frozen mode, provider configuration, evaluator authority and operator credentials strongly constrain operation, but they are operational/adaptation governance rather than adjudication of BitRouter's organizational identity or ultimate policy.
- Decisive decision or feedback right: no identity/ultimate-policy issue and authoritative return loop is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: policy locks; runtime mode; virtual-key/control authorization; evaluator authorities; config validation; operator restore and route controls constrain lower-level functions without constituting S5.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S5 path was found in standard runtime modes.
- Why this is / is not agent-owned: autonomous workers follow active policy and humans can change operational policy, but neither path establishes a decision over system identity/ultimate policy as defined by the Profile.
- Evidence: [`skills/bitrouter/references/adaptive-routing.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/adaptive-routing.md); [`skills/bitrouter/references/sessions.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/skills/bitrouter/references/sessions.md); [`README.md`](https://github.com/bitrouter/bitrouter/blob/e2a8c644e8ece5a2f152d2516269497d23aeef5d/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: `policy` in BitRouter's product vocabulary primarily means routing/access/experiment policy; vocabulary similarity is not S5 evidence.

### Absence scope

- Surfaces inspected: signed route policy and runtime mode; optimizer/evolution; access/control credentials; evaluator authority; supervisor permissions; provider/model configuration; remote administration; policy history/restore.
- Plausible first-party paths checked: adaptive/frozen policy mode; operator publication authority; access policy; control grants; route ownership; experiment governance and rollback.
- Why no material first-party path remains: these mechanisms decide how current/future routing and access operate but do not surface a genuine organizational identity/ultimate-policy matter, legitimate ultimate authority over that matter and a returned identity-level governing decision.

## Recursion

BitRouter materially exposes multiple operational coding sessions under one supervisor and can record parent-run identity, but it does not inherit the internal VSM structure of an ACP harness. Harness-native child agents are explicitly not inferred from process trees, ANSI output or logs. At the assessed parent boundary, supervised external coding sessions can act as S1 units for S3 current-control analysis; no stronger nested viable-system claim is required for the reported vector.

## Variety and escalation

BitRouter attenuates substantial operational variety: provider/model availability, route selection, permission requests, session lifecycle, background detach/attach, same-worktree writer hazards, cost attribution, stale-control generations and policy publication races. Exact scopes and generation fences reduce unsafe current-control variety; worktree claims prevent an accidental second writer; compare-and-swap policy digests prevent stale publishers from replacing a newer route policy.

Escalation remains function-specific. Unmatched background permissions can become Needs input for a manager/operator; current run state can be stopped or reconfigured through S3 control; evaluation uncertainty can hold S4 adaptation; hard violations or exhausted evidence budgets can trigger retreat/withdrawal. None of these lower-level escalations is promoted to S5 without identity-level evidence.

## Evidence gaps

- BitRouter is broad and rapidly evolving; this assessment is pinned to the exact frozen revision and does not infer later repository behavior.
- The ACP evolution docs contain extensive controlled/fixture experiment evidence but explicitly disclaim measured live routing benefit in some studies. Functional ownership is assessed from the implemented control/adaptation paths, not from a claim of proven product performance.
- A downstream autonomous manager can compose the S3 constructor surface, and a downstream autonomous adaptation actor can compose the S4 constructor surface. Each concrete composition is a separate system-in-focus and may classify differently.
- A future first-party independent reviewer that returns audit findings into bounded worker rework could change S3*; the inspected frozen distribution does not establish that closure.
