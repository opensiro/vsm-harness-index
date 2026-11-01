---
harness_id: moissanite-labs-exo
project_name: exo
repository: https://github.com/Moissanite-Labs/exo
review_ref: e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# exo

## Review boundary

- System in focus: Moissanite-Labs/exo's current standalone CoreEngine distribution, with installed memory/gate plugins and enabled principal-store learning.
- Purpose and identity: perform coding/assistant work across sessions while fitting one legitimate principal through durable memory and controlled adaptation.
- Relevant environment: principal tasks, corrections and evolving preferences; local repositories/tools; providers/peer inputs; approval and resource constraints.
- Standard-distribution boundary: current compose/CoreEngine/Loop, first-party delegate/task/trace tooling, deployed gate plugin and attached fast learner plus principal proposal-review CLI. No behavior is imported from the older Hermes architecture or personal dogfood stores.
- Credited operating / distribution surfaces: src/exo/compose.py, core engine/loop/delegate, installed exo-memory/exo-gate, learn runtime/review/promote and principal proposal acceptance.
- Adjacent first-party surfaces excluded from ownership: research and old Hermes migration architecture, author's private principal store, repository CI/evaluation artifacts, optional review-only Harness² fixtures/export and arbitrary adopter plugins. Held-out learning API is inspected but automatic nightly scheduling is not claimed.
- First-party operating / deployment modes considered: terminal/web self-hosted current core, optional peers/background/delegated work, principal-store fast learning and explicit proposal review, gate policy-change acceptance with authenticated principal transport. No store means learning is off.
- Recursion level: one deployed harness instance; child execution is not presumed recursively viable.
- Reviewed revision: `e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea`.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (Index active release; Skills main 0.3.8 inspected but not silently activated).

## Repository architecture

The current product factory composes CoreEngine, model router, tool registry, plugins, shared session/log context, delegation, jobs and optional scheduler, then attaches the learner. Loop owns bounded model→tool→result iterations with steering, crash repair and usage traces. Delegated children have typed briefs/receipts, narrower tools and tier/depth/token/time/concurrency ceilings. After-turn instrumentation detects trace anomalies and rechecks fixed findings. Fast learning reads principal-authored corrections/rulings, asks an aux reviewer for typed lessons with implications beyond one case, critiques them and applies constrained promotion; accepted nodes are recalled on later turns. Slow held-out climb is available as an API but has no automatic timer. Gate policy files are pinned; changes are surfaced/logged and can tighten behavior before explicit live-principal acceptance adopts the new policy.

## Operational model

The persistent main agent and optionally delegated work cells own model-driven tool decisions. A configured agent tier and runtime limits support operations; they do not prove S2/S3. External principal corrections are used to generate future behavioral options, with automatic unguarded promotion or explicit principal acceptance feeding the next turn. Policy authority is retained at the principal recursion through a specific policy-adoption path, not inferred from individual approvals. The name exo is also used by unrelated exoharness/exo already indexed at 181; this distinct stable repo ID 1414821298 uses harness_id moissanite-labs-exo.

## S1 — Operations

- State: A
- Function: persistent coding/assistant work with discretionary tool use and delegated subtasks.
- Disturbance / variety regulated: varying tasks, repository state, tool/provider errors and interrupted sessions.
- Decisive decision or feedback right: choose tools, edits, commands and follow-up steps from current observations.
- Decision owner: the main or configured delegated agent in the first-party Loop.
- Supporting / enforcement mechanisms: CoreEngine composition, router, tool runner, plugins/approval desk, context tree and typed result persistence.
- Closure path: tool results are appended to messages before the next model round; steering and errors update subsequent operation.
- Boundary reachability: compose.create builds the current core, registers the delegator, connects run_tool and starts Loop; no legacy Hermes host is required for this claim.
- Why this is / is not agent-owned: removing model discretion leaves tool/transport/persistence mechanisms without task-level transformation decisions.
- Evidence: [src/exo/compose.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/compose.py); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); [src/exo/core/loop.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/loop.py); [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py).
- Basis: structural.
- Confidence: high.
- Caveats: provider APIs/claude-cli can supply inference; their unrelated harness functions are not borrowed.

## S2 — Coordination

- State: —
- Function: no bounded first-party inter-S1 coordination function established.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Generic child concurrency and shared-log consistency do not establish a concrete inter-S1 interference/attenuation/feedback witness. The writer lock excludes competing cores of the same persistent agent, not mutually adjusted S1 work cells; peer messaging/delegation alone is insufficient.
- Evidence: [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/core/agentlog.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agentlog.py); [src/exo/peers.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/peers.py); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/core/agentlog.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agentlog.py); [src/exo/peers.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/peers.py); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); src/exo/compose.py, core engine/loop/delegate, installed exo-memory/exo-gate, learn runtime/review/promote and principal proposal acceptance..
- Plausible first-party paths checked: parallel delegated children, semaphore/depth/token limits, one-writer log lock, peer ingress and shared memory/receipts.
- Why no material first-party path remains: Generic child concurrency and shared-log consistency do not establish a concrete inter-S1 interference/attenuation/feedback witness. The writer lock excludes competing cores of the same persistent agent, not mutually adjusted S1 work cells; peer messaging/delegation alone is insufficient.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current organizational control decision loop established.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Task decomposition, narrow task intervention and constructor-selected limits do not independently establish whole-system resource/commitment regulation. The reviewed commands expose current state but no additional function-specific S3 decision/return path beyond ordinary operations was evidenced; no P inferred from a generic operator UI.
- Evidence: [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/subagents.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/subagents.py); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); [src/exo/model_spend/policy.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/model_spend/policy.py); [src/exo/scheduler.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/scheduler.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/subagents.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/subagents.py); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); [src/exo/model_spend/policy.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/model_spend/policy.py); [src/exo/scheduler.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/scheduler.py); src/exo/compose.py, core engine/loop/delegate, installed exo-memory/exo-gate, learn runtime/review/promote and principal proposal acceptance..
- Plausible first-party paths checked: cost-tier choices, child receipts/task listings, operator steer/stop, principal model/settings changes, spend ceilings and scheduler/jobs.
- Why no material first-party path remains: Task decomposition, narrow task intervention and constructor-selected limits do not independently establish whole-system resource/commitment regulation. The reviewed commands expose current state but no additional function-specific S3 decision/return path beyond ordinary operations was evidenced; no P inferred from a generic operator UI.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit loop established for current operational claims.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Trace and findings are first-party observability/self-report with deterministic rechecks; generic critic delegation lacks an audit-specific claim/access/corrective contract. Learning critique and held-out adaptation testing concern prospective proposals, not a separately closed operational audit. No S3* is inferred from audit/reviewer terminology.
- Evidence: [docs/TRACE.md](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/docs/TRACE.md); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); [src/exo/core/findings.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/findings.py); [src/exo/core/tools/builtin/harness.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/tools/builtin/harness.py); [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/learn/review.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/review.py); [src/exo/learn/climb.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/climb.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [docs/TRACE.md](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/docs/TRACE.md); [src/exo/core/engine.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/engine.py); [src/exo/core/findings.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/findings.py); [src/exo/core/tools/builtin/harness.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/tools/builtin/harness.py); [src/exo/core/agents/delegate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/core/agents/delegate.py); [src/exo/learn/review.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/review.py); [src/exo/learn/climb.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/climb.py); src/exo/compose.py, core engine/loop/delegate, installed exo-memory/exo-gate, learn runtime/review/promote and principal proposal acceptance..
- Plausible first-party paths checked: trace/anomaly findings, fixed-signature remeasurement, agent self-report, read-only critic delegation, proposal criticism and held-out candidate evaluation.
- Why no material first-party path remains: Trace and findings are first-party observability/self-report with deterministic rechecks; generic critic delegation lacks an audit-specific claim/access/corrective contract. Learning critique and held-out adaptation testing concern prospective proposals, not a separately closed operational audit. No S3* is inferred from audit/reviewer terminology.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: adapt future behavior to the external principal's recurring needs and corrected preferences through typed, evidence-linked options.
- Disturbance / variety regulated: current behavior no longer matches principal corrections/rulings or generalizable class-of-task expectations.
- Decisive decision or feedback right: derive a beyond-instance lesson and adopt an eligible future behavior rule; alternatively the principal explicitly accepts/rejects a proposed adaptation.
- Decision owner: base mode: aux reviewer/critic supplies adaptive judgment and bounded automatic promotion closes eligible ordinary lessons. Parent mode: legitimate store operator/principal decides the concrete proposal.
- Supporting / enforcement mechanisms: principal authorship filtering, evidence/session/weight constraints, guarded/conflict holds, proposal diffs, promotion ledger and refreshed memory nodes.
- Closure path: eligible autonomous promotions or explicit proposal_accept write accepted nodes/skills and ledger state; exo-memory reads nodes fresh for subsequent turns. Guarded/skill paths do not silently bypass their gates.
- Boundary reachability: compose attaches learn to the current engine; on_turn_end starts review for new principal signals; review calls constrained apply_policy. CLI exo proposals exposes show/accept/reject, and accepted nodes return through installed memory. Optional slow API/fixture export is not the basis of automatic A.
- Why this is / is not agent-owned: the model develops the prospective behavioral lesson from external principal feedback; deterministic policy constrains its acceptance. In the explicit review mode the principal owns adoption. Mere transcript retention, fact recall or a roadmap is not the credited S4 witness.
- Evidence: [src/exo/compose.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/compose.py); [src/exo/learn/learner.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/learner.py); [src/exo/learn/review.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/review.py); [src/exo/learn/promote.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/learn/promote.py); [src/exo/consolidate.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/consolidate.py); [docs/LEARNING.md](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/docs/LEARNING.md).
- Basis: structural.
- Confidence: medium.
- Caveats: base claim is limited to enabled store-backed, eligible generalizable behavior lessons; facts stored without a prospective behavior implication are not S4. Skill/held-out nightly automatic scheduling is not claimed; no empirical effectiveness or transfer result.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | aux reviewer/critic acting through bounded eligible promotion | new/repeated principal correction with beyond-instance behavioral implication | apply_policy accepts eligible unguarded lesson; next-turn memory reads accepted node | learn/learner.py, review.py, promote.py; docs/LEARNING.md |
| Parent (`P`) | legitimate principal/store operator | a proposed/held adaptation presented for explicit review | exo proposals show/accept or reject; proposal_accept updates node/skill and subsequent recall | consolidate.py cmd_proposals/proposal_accept; docs/LEARNING.md |
- External distinction: principal-authored corrections, rulings and repeated preferences filtered from agent/peer/tool text.
- Future / prospective distinction: typed proposals explicitly include an implication beyond this case, such as how future classes of task should be handled.
- Adaptation option generated: taste/behavior rule or task-class skill proposal with evidence, critique and guard/conflict status.
- Path back into current capability / S3: promotion/acceptance updates the deployed memory/skill source used on the next turn; no positive S3 is manufactured from that return path.

## S5 — Policy and identity

- State: P
- Function: retain ultimate authority over the harness's public/irreversible/financial risk-policy boundaries at the principal recursion.
- Disturbance / variety regulated: runtime gate policy changes could relax reserved authority or alter ultimate allowed exposure/risk.
- Decisive decision or feedback right: adopt or withhold a changed governing gate policy, rather than merely approve one action.
- Decision owner: the authenticated live principal; agent/peer input cannot supply that credential.
- Supporting / enforcement mechanisms: principal transport/authorship checks, pinned policy snapshot, changed-policy hashes, stricter interim enforcement and signed acceptance record.
- Closure path: gate status exposes changed policy; /gate accept requires principal authority, records policy_accept and replaces the pinned policy used to govern later calls.
- Boundary reachability: installed exo-gate command routes accept to accept_policies; the current composed core loads plugins and carries principal authority through the transport path.
- Why this is / is not agent-owned: ultimate policy adoption remains with the principal; deterministic classification, hashes and individual exact-text approval are supporting controls, not autonomous S5.
- Evidence: [plugins/exo-gate/exo_gate/hook.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/plugins/exo-gate/exo_gate/hook.py); [src/exo/principal.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/principal.py); [src/exo/compose.py](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/src/exo/compose.py); [docs/GATE.md](https://github.com/Moissanite-Labs/exo/blob/e9ad895d2c59e998f0358b982a9b8a4ac0ad2aea/docs/GATE.md).
- Basis: structural.
- Confidence: high.
- Caveats: bounded to the legitimate principal's ultimate risk/delegation policy; no claim that every approval, SOUL.md edit or maintainer action is S5. Required-executor behavior is mode-specific.
- Identity / ultimate-policy issue: who may authorize public/irreversible/financial acts and whether changed reserved-risk policy becomes governing.
- Ultimate authority in each claimed mode: principal transport authority checked by require_principal; no internal autonomous S5 mode established.
- Return-to-operation path: changed policy status/hash → live principal accept → logged policy_accept → new pinned policy → subsequent tool decisions.

## Distributed OSS parent arrangement

MIT licensing and contributor/maintainer activity establish distribution provenance, not project-level S3/S4/S5 parent closure. This assessment concerns the deployed product boundary; no organization-level parent mode is inferred from local maintainer decisions.

## Self-hosted and non-human modes

Principal-store learning and installed memory/gate plugins are required for the positive S4/S5 modes. Empty-store/disabled-learning installations retain operational S1 but do not instantiate those loops. Independent contributors' private stores and personal dogfood history do not establish organization-level parent governance.

## Recursion

Nested execution and delegated tasks do not establish recursive viable systems; no child full metasystem is claimed.

## Variety and escalation

Typed briefs/receipts and model tiers attenuate work/cost variety; traces retain routing/failure distinctions. Principal-authorship filtering separates external rulings from agent/peer data. Conflicts and guarded proposals remain visible for principal review. Exact-text action consent is separate from ultimate-policy adoption.

## Evidence gaps

Source-first only; no real provider/claude session, learning run, nightly experiment or external act executed. Native pytest suite not run because pytest is unavailable; optional real_claude tests were not executed. Older docs/ARCHITECTURE.md is stale for current standalone runtime and is excluded where code disagrees. Learning adaptation claims are bounded to explicit beyond-instance behavioral proposals and refreshed deployment state, not all memory or learning. No independent S3* attestation or empirical adaptation gain.
