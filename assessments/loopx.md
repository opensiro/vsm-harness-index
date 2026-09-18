---
harness_id: loopx
project_name: LoopX
repository: https://github.com/huangruiteng/loopx
review_ref: ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.3
profile_version: 0.2.2
assessment_procedure_version: 0.3.3
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# LoopX

## Review boundary

- System in focus: one LoopX-governed long-horizon Goal, including its first-party Goal/Todo/quota/authority state, heartbeat/Turn contracts, peer/subagent orchestration, evidence settlement, review handoffs and parent authority paths at pinned revision `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`.
- Purpose and identity: keep autonomous coding/knowledge-work agents making bounded, evidence-backed progress across repeated turns while preserving durable authority, state, coordination, review and human ownership boundaries.
- Relevant environment: target repository/project, host agent runtimes such as Codex or Claude Code, tools/tests, remote services, user instructions, repository policy and protected production/publication boundaries.
- Standard-distribution boundary: LoopX control-plane code, generated skills/prompts, Goal/Todo/quota/lease/gate/evidence protocols and supported host integrations. Provider-native model runtimes are execution hosts, not inherited organizational functions unless LoopX's first-party contract establishes the relevant decision path.
- First-party modes considered: recurring autonomous heartbeat/Turn execution, registered peer and bounded child-worker orchestration, independent review handoff, operator/user gates and owner-level Goal authority.
- Recursion level: one governed Goal organization. Registered peers and bounded child workers are operational participants; technical nesting alone is not counted as recursion.
- Reviewed revision: `ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.3`.

## Repository architecture

LoopX is a provider-neutral long-horizon control plane layered over host agent runtimes. A Goal persists objective, gates, Todos, evidence, quota, execution profile, authority state and run history across otherwise replaceable agent turns. Heartbeats reconstruct current state before spending work, a governed Turn performs a bounded delivery slice, and accepted evidence is durably settled back into Goal/Todo state. Multi-agent execution keeps durable registered agents as peers while allowing a temporary task coordinator to choose bounded parallelism, activate eligible lanes, aggregate evidence and settle accepted task-bundle state. Human authority remains explicit for protected actions, owner decisions, scope/acceptance changes and final Goal ownership.

## Primary evidence

- [`README.md`](https://github.com/huangruiteng/loopx/blob/ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f/README.md) — provider-neutral long-horizon control-plane boundary, durable Goal state, bounded autonomous execution, human judgment and final-ownership boundary.
- [`docs/integration.md`](https://github.com/huangruiteng/loopx/blob/ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f/docs/integration.md) — heartbeat execution obligation, autonomous validated public delivery, Goal authority sources, peer claims/leases/worktrees and independent review handoff.
- [`docs/integrations/codex-subagent-orchestration.md`](https://github.com/huangruiteng/loopx/blob/ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f/docs/integrations/codex-subagent-orchestration.md) — temporary task-coordinator authority, adaptive parallel admission, blocked/runnable peer lanes, independent review/adversarial validation and evidence settlement.
- [`docs/reference/canonical-lease-renew.md`](https://github.com/huangruiteng/loopx/blob/ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f/docs/reference/canonical-lease-renew.md) — canonical lease ownership, CAS/version fences and contention enforcement.
- [`docs/reference/protocols/lark-manager-context-authority-v0.md`](https://github.com/huangruiteng/loopx/blob/ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f/docs/reference/protocols/lark-manager-context-authority-v0.md) — typed authority records and separation of context visibility from authorized Manager turns.

## S1 — Operations

- State: A
- Function: execute bounded outcome-bearing work for a Goal through model-driven host agents while preserving evidence-backed completion and durable continuation.
- Disturbance / variety regulated: repository/task uncertainty, tool observations, implementation choices, test results, bounded failures and changing local work state inside the current authority snapshot.
- Decisive decision or feedback right: choose the next local action/effect sequence needed to advance the selected Todo and decide whether evidence supports completion, continuation, replan or blocker reporting.
- Decision owner: the active autonomous model-driven Goal worker in LoopX's supported host mode.
- Supporting / enforcement mechanisms: heartbeat preflight, Turn envelope, execution profile, Goal/Todo state, quota, capability checks, tool/runtime host and durable settlement.
- Closure path: the agent executes a bounded slice, validates an artifact/outcome, writes evidence and state back through LoopX, and the next heartbeat/Turn reconstructs that settled state before acting again.
- Why this is / is not agent-owned: LoopX's standard recurring contract requires the worker agent to inspect current state and make the local work decision; deterministic quota/gates constrain or reject actions but do not choose the operational solution for the agent.
- Evidence: `README.md` describes bounded autonomous Goal progress; `docs/integration.md` states that an eligible heartbeat with `must_attempt_work=true` should attempt one bounded segment and that routine validated public commit/push/PR delivery may proceed autonomously.
- Basis: explicit + structural
- Confidence: high
- Caveats: the underlying model/tool runtime is external; the mapping credits the organizational worker decision exercised through LoopX's first-party supported host contract, not provider features outside that contract.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference and dependency conflict among multiple Goal workers while preserving peer autonomy.
- Disturbance / variety regulated: overlapping write scopes, concurrent claims on the same Todo, dependency-constrained work, duplicated execution and unsafe parallelism across registered peers or bounded child workers.
- Decisive decision or feedback right: decide whether useful work should run in parallel or serially, which eligible lanes to delegate/activate, and how to resolve work-bundle boundaries before execution proceeds.
- Decision owner: the temporary model-driven task coordinator selected for the bounded work bundle.
- Supporting / enforcement mechanisms: disjoint write-scope admission, independent worktrees, canonical claims/leases, CAS/version fences, capability/readiness checks, capacity deferral and typed continuation.
- Closure path: the coordinator's choice determines admitted lanes and briefs; rejected/blocked lanes do not run, admitted workers execute within separated scopes, and accepted evidence is reconciled into the shared Goal before subsequent work is scheduled.
- Why this is / is not agent-owned: deterministic leases and scope checks enforce the coordination boundary, but `codex-subagent-orchestration.md` explicitly leaves the parallelize/keep-serial, lane-selection and context choices to the temporary coordinator agent.
- Evidence: `docs/integrations/codex-subagent-orchestration.md` documents adaptive orchestration and coordinator decisions; `docs/integration.md` states that overlapping write scopes require task-coordinator arbitration; `docs/reference/canonical-lease-renew.md` supplies the concrete contention fence.
- Basis: explicit + structural
- Confidence: high
- Caveats: durable peers are deliberately not ranked and no permanent S2 controller is inferred; the positive mapping is the bounded coordination relation around concrete interference.
- Distinct S1 units: two or more registered peer agents or admitted bounded child workers operating on distinct Goal Todos/work scopes.
- Inter-S1 disturbance: concurrent workers can claim the same work or write overlapping repository surfaces, producing duplicate execution, stale authority, merge/write races or dependency violations.
- Attenuating coordination relation: the task coordinator chooses the work split while LoopX admits only capability-ready, dependency-ready and non-overlapping scopes and uses leases/worktrees to preserve the chosen separation.
- Feedback into subsequent S1 behaviour: blocked/deferred lanes remain non-runnable; admitted lane briefs and lease/scope state constrain what each worker subsequently does; returned evidence changes the shared bundle/Goal state used by later workers.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited path exists specifically to prevent overlapping writes, duplicate ownership and dependency-invalid parallel execution, rather than merely to pass messages or assign tasks.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current whole-Goal commitments, admissible work, evidence settlement, exception handling and protected intervention across active lanes.
- Disturbance / variety regulated: competing runnable work, blocked peer lanes, quota/capability limits, failed or incomplete evidence, current user gates, stale authority and exceptions that exceed an ordinary worker's bounded lane.
- Decisive decision or feedback right: in the autonomous mode, choose the currently admissible work bundle, accept/reject returned evidence for settlement and determine continuation/replan/blocker disposition; in the parent mode, decide current protected-operation/user-gate exceptions and steering that the agent is not authorized to settle itself.
- Decision owner: autonomous mode — model-driven task coordinator / accountable Goal worker within its current authority; parent mode — legitimate human Goal owner/operator.
- Supporting / enforcement mechanisms: quota projections, runnable/blocked lane state, Goal/Todo/gate projections, settlement receipts, scheduler stop/re-arm rules, user gates and host capability observations.
- Closure path: autonomous control changes lane activation, accepted settlement and next actionable Todo state; parent decisions clear/retain gates or change current scope/permission/steering, after which the returned authority state is read by subsequent Goal workers.
- Why this is / is not agent-owned: the autonomous mode includes real agent discretion over work admission and current task-bundle settlement, while user-gate/protected-operation decisions remain explicitly parent-owned rather than being inferred from deterministic enforcement.
- Evidence: `docs/integrations/codex-subagent-orchestration.md` gives the coordinator current runnable/blocked peer state and authority to activate lanes, accept evidence and settle a bundle; `README.md` and `docs/integration.md` preserve human gates and protected-operation authority that return into Goal execution.
- Basis: explicit + structural
- Confidence: high
- Caveats: the task coordinator does not acquire durable Goal identity authority; that boundary is intentionally separated from current-control discretion and is reflected under S5.
- Whole-system current view: the coordinator/Goal worker receives current Goal state, actionable and blocked lanes, quota/gate snapshots, capability readiness, accepted/rejected evidence and current continuation state for the governed Goal.
- Current-control decision scope: current lane admission/activation, task-bundle settlement, continuation versus wait/replan, exception escalation and protected current-operation decisions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-driven task coordinator / accountable Goal worker | Runnable multi-lane or bounded Goal work under a valid authority snapshot | Coordinator admits/activates lanes, reconciles evidence and writes accepted bundle/Goal state used by the next Turn | `docs/integrations/codex-subagent-orchestration.md`, `docs/integration.md` |
| Parent (`P`) | Human Goal owner/operator | User gate, protected action, current scope/permission exception or steering beyond agent authority | Human decision clears/retains the gate or changes current authority; the result is persisted/projected and constrains subsequent execution | `README.md`, `docs/integration.md`, `docs/reference/protocols/lark-manager-context-authority-v0.md` |

## S3* — Complementary audit

- State: A
- Function: obtain an independent challenge to an operational delivery claim using evidence access separate from the producing worker's own success report.
- Disturbance / variety regulated: false-positive completion, biased self-review, invalid implementation evidence and risky changes whose ordinary producer report is insufficient.
- Decisive decision or feedback right: independently judge whether the submitted claim/artifact passes the review or adversarial validation brief and return evidence for acceptance/correction.
- Decision owner: a separate autonomous reviewer/adversarial-validation worker.
- Supporting / enforcement mechanisms: fresh reviewer context, explicit `action_kind=review`, `independent_handoff`, optional author exclusion, read-only/evidence boundaries and parent/coordinator acceptance of returned evidence.
- Closure path: independent findings become eligible review evidence; the accountable coordinator/Goal path accepts or rejects the delivery and routes correction/continuation accordingly before settlement or publication.
- Why this is / is not agent-owned: the audit judgment is produced by a distinct model-driven reviewer, while author-exclusion and handoff machinery enforce independence without owning the judgment.
- Evidence: `docs/integrations/codex-subagent-orchestration.md` explicitly recommends a fresh worker for independent review/adversarial validation and supports excluding the author; `docs/integration.md` routes higher-risk work through `independent_handoff` with review semantics.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: not every LoopX delivery invokes the independent path; S3* is credited as a first-party supported complementary audit mode, not as generic validation/logging.
- Claim being audited: that a completed Goal/Todo delivery is valid, evidence-backed and safe to accept/merge/publish under the relevant review policy.
- Ordinary reporting path: producing worker returns its changed files/artifact, validation and completion evidence into the normal Goal/Todo settlement path.
- Complementary access path: a fresh independent reviewer receives the claim, exact evidence/authority source and validation command and can inspect/run checks without relying on the producer's reasoning trace or self-judgment.
- Independence boundary: `independent_handoff` may exclude the author; the reviewer is a separate worker and does not inherit the producer's execution ownership.
- Who acts on findings: the accountable task coordinator / Goal settlement path accepts the review evidence and changes subsequent settlement, correction or escalation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate externally and prospectively oriented adaptation function is established at the reviewed one-Goal boundary.
- Disturbance / variety regulated: potential future changes in model capability, project environment or control-plane operating conditions were inspected, but no first-party S4 closure is established.
- Decisive decision or feedback right: no material first-party decision right was found that converts external/future distinctions into adaptation options and closes them back into present Goal capability as S4.
- Decision owner: none established for a qualifying S4 function.
- Supporting / enforcement mechanisms: self-repair, heartbeat recovery, run history, gray-rollout/canary practices, adapters and memory can support maintenance/learning but do not establish the required outside-and-then conversation by themselves.
- Closure path: no qualifying external/future model → adaptation option → present capability/S3 return loop is established at the declared boundary.
- Why this is / is not agent-owned: the missing element is the organizational S4 function itself, not merely autonomous ownership; ordinary recovery and retrospective state do not become S4 because agents use them.
- Evidence: `README.md`, `docs/integration.md`, and the reviewed orchestration/authority protocols were inspected for environment-facing adaptation paths; the evidenced loops are current execution/control/recovery or maintainer development practices.
- Basis: structural
- Confidence: high
- Caveats: LoopX research RFCs discuss future adaptive control, but draft/research proposals are not credited as standard-distribution S4 implementation.

### Absence scope

- Surfaces inspected: pinned README, integration/heartbeat behavior, Goal/Turn authority protocols, peer/subagent orchestration, review/lease paths, self-repair/gray-rollout descriptions and standard runtime state surfaces.
- Plausible first-party paths checked: self-repair, canary promotion, adapter/project-signal handling, run-history learning, model/runtime qualification and long-horizon research/adaptation references.
- Why no material first-party path remains: shipped evidence closes these paths as current recovery, maintenance, developer release practice or proposals; it does not supply a standard autonomous/constructor/parent S4 loop that senses external/future change, develops adaptation options and returns them into current Goal capability.

## S5 — Policy and identity

- State: P
- Function: maintain the Goal's purpose/identity and ultimate authority boundary over what the organization is trying to achieve and which protected changes are legitimate.
- Disturbance / variety regulated: proposed changes to Goal objective/acceptance, execution authority, protected publication/production actions and cases where autonomous work would otherwise drift beyond the owner's intended identity or risk boundary.
- Decisive decision or feedback right: establish or change the Goal objective/acceptance/ultimate authority boundary and settle owner-reserved decisions that agents must not make for themselves.
- Decision owner: legitimate human Goal owner/operator.
- Supporting / enforcement mechanisms: Goal/registry authority sources, active-state projection, user/owner gates, typed authority records, execution profiles and protected-operation fences.
- Closure path: the owner supplies/changes the authoritative Goal or owner decision; LoopX records/projects that authority into canonical Goal/Todo/gate state; subsequent heartbeats and workers reread it before acting, so future operation is governed by the returned decision.
- Why this is / is not agent-owned: LoopX deliberately keeps final ownership and protected authority human; agents may propose, route and execute within the boundary but do not acquire legitimate ultimate Goal authority.
- Evidence: `README.md` states that judgment/final ownership and dangerous permissions stay human; `docs/integration.md` records Goal documents as primary authority sources and requires workers to reread registry/Goal state; typed user/owner gates stop unauthorized progression until a legitimate decision returns.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary task approvals are not counted as S5; the positive mapping is limited to Goal identity/acceptance and ultimate protected authority at the chosen Goal recursion.
- Identity / ultimate-policy issue: what the Goal is for, its acceptance boundary, and whether protected changes to scope/permission/direction are legitimate.
- Ultimate authority in each claimed mode: human Goal owner/operator only; no autonomous S5 mode is claimed.
- Return-to-operation path: owner authority is written/projected into Goal/registry/gate state and becomes mandatory input to later heartbeat/Turn decisions.

## Recursion

Registered peers and host child workers can contain their own local loops, but LoopX deliberately treats durable peers as equal participants under one Goal and bounded children as task-scoped workers. No nested unit is credited as a complete viable recursion merely because it has its own host session, worktree or transcript.

## Variety and escalation

LoopX amplifies operational capacity through multiple replaceable workers but attenuates coordination/current-control variety with explicit claims, leases, disjoint scopes, quota, gates, evidence settlement and bounded task coordinators. Exceptions move outward when a worker lacks capability/authority, when evidence fails, when a peer lane is blocked, or when owner/protected authority is required.

## Evidence gaps

No shipped S4 closure is established. S3* confidence is lower than S1/S2/S3/S5 because the independent-review path is optional and evidence eligibility still returns through the accountable Goal path, but its fresh context and author-exclusion path are materially complementary to producer self-report.

## Admission conclusion

Canonical vector: `A A A(P) A — P`.
