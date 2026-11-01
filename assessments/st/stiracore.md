---
harness_id: stiracore
project_name: StiraCore
repository: https://github.com/Resolver-TNG/StiraCore
review_ref: 2dee27f3c99c4f63b1ef2a7e377482d40c527996
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# StiraCore

## Review boundary

- System in focus: one self-hosted StiraCore installation, including chat and its explicitly supported optional stage-C goal-grant mode.
- Purpose and identity: perform model/tool work under identity-file protection, state-based guards and scoped operator-issued goal execution.
- Relevant environment: user tasks, local workspaces, model/tool providers, competing foreground/background work and operator constraints.
- Standard-distribution boundary: NXPAgent's concrete Strands composition, first-party tools/guards/context and dashboard server wiring; optional grants credited only with documented stage_c/stage_c_exec prerequisites.
- Credited operating / distribution surfaces: agent/nxp_agent, grant child/executor/service/routes, authority/TurnLock and host-confirmed grant controls in dashboard/stira_server.py.
- Adjacent first-party surfaces excluded from ownership: eval/audit CLI/scenarios, attack regression tests, documentation design proposals, contributor workflows and unpublished predecessor projects. Strands/provider internals are dependencies.
- First-party operating / deployment modes considered: supervised chat; optional manually stepped goal iteration; optional gated heartbeat starts; model-free heartbeat; opt-in delegation, procedural proposals and observe-only memory-autonomy phase 0.
- Recursion level: one installed service with chat work and a separate grant:<id> child work cell; no organization-level contributor-governance mapping.
- Reviewed revision: 2dee27f3c99c4f63b1ef2a7e377482d40c527996.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

NXPAgent wraps a freshly prepared Strands Agent each turn, carrying model/tools/messages, identity guards, checkpoint hooks and current context. Local tools, memory layers, model routing and optional delegates support the task actor. Breaker/state/taint/consent machinery constrains execution rather than owning its organizational choices. Dashboard wiring installs the optional GrantService and iteration executor behind separate configuration flags. A goal iteration uses a fresh grant-specific child engine/session, narrowed write roots and per-effect permits/budget reservations; only one live grant is supported. TurnLock signals foreground arrivals before lock acquisition so running goal work yields at effect boundaries. The human grant panel exposes current counters, remaining resources and intervention operations. Procedural proposals are staged for human approval; memory-autonomy phase 0 is explicitly observe-only. SOUL/IPD paths remain agent-read-only. Operational event/audit logs and the separate evaluation package do not supply an independent runtime auditor.

## Operational model

The ordinary model actor owns local task/tool decisions in chat or a permitted grant iteration. The optional whole-grant supervisor is the legitimate host operator: they commit the installation's bounded background work, select its resource/time/tool/workspace envelope and can revise current execution through pause/resume/revoke/verification. Deterministic permits enforce the returned human decision. Foreground/background interference has a first-party specific preemption path, while autonomous S2 policy and autonomous S3 discretion are not supplied.

## S1 — Operations

- State: A
- Function: perform user work through a concrete model/tool loop and produce workspace or conversational results.
- Disturbance / variety regulated: task inputs, tool observations/errors, local files, model response variation and bounded goal progress.
- Decisive decision or feedback right: choose task actions/tools, interpret feedback and report a result or blocker.
- Decision owner: the NXPAgent/Strands model actor, including the separate scoped grant child when enabled.
- Supporting / enforcement mechanisms: first-party tool/context composition, Strands loop, guards, checkpoints, provider adapters, permits and budgets.
- Closure path: tool results feed the configured Agent's later choices; grant work can report progress/blocker/claim while human verification remains separately owned.
- Why this is / is not agent-owned: without the model actor guards/storage/permits cannot choose the task transformation.
- Evidence: [src/stiracore/agent/nxp_agent.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/agent/nxp_agent.py); [src/stiracore/agent/grant_child.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/agent/grant_child.py); [src/stiracore/grants/executor.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/executor.py); [dashboard/stira_server.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/dashboard/stira_server.py)
- Basis: structural
- Confidence: high
- Caveats: Runtime availability, not verified task quality. Stage-C execution is alpha/off by default and requires its documented flags/provider/host constraints.
- Boundary reachability: NXPAgent.__call__ instantiates Agent with reachable tools/hooks and executes the task; create_grant_child supplies the supported isolated grant actor under the executor.

## S2 — Coordination

- State: C
- Function: prevent overlapping foreground service turns and independent background grant work from interfering with shared installation state/work.
- Disturbance / variety regulated: chat/webhook/resume/new-session/procedure operations can arrive while a grant child is executing.
- Decisive decision or feedback right: prioritize an arriving foreground turn and make background work yield before further effects.
- Decision owner: the developer-composed TurnLock/PreemptSignal policy; no agent owns revision of that arbitration rule.
- Supporting / enforcement mechanisms: shared turn lock, arrival counter/pending mark, executor admission check and safe-boundary cancellation/yield.
- Closure path: TurnLock.acquire signals before locking; executor step refuses competing starts and _precheck ends a running iteration as yielded_user_turn before another effect.
- Why this is / is not agent-owned: the agent solves its work inside the granted turn; it does not select the fixed foreground/background priority policy. C credits the supplied interference-specific constructor path.
- Evidence: [src/stiracore/core/turn_lock.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/core/turn_lock.py); [src/stiracore/grants/executor.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/executor.py); [src/stiracore/agent/grant_child.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/agent/grant_child.py); [dashboard/stira_server.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/dashboard/stira_server.py); [docs/autonomy.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/autonomy.md)
- Basis: structural
- Confidence: high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.
- Distinct S1 units: foreground chat/integration work and independently session-bound grant child work with its own goal/outcome.
- Inter-S1 disturbance: a foreground turn can conflict with an in-flight background iteration over the same installation's mutable execution/workspace context.
- Attenuating coordination relation: foreground arrival preempts/refuses background execution at effect boundaries under one shared lock/signalling relation.
- Feedback into subsequent S1 behaviour: the iteration yields/stops; subsequent effects need fresh admission/permits and foreground work can proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock explicitly regulates the identified foreground-versus-grant overlap, with signal-before-lock and executor checks closing the race.
- Boundary reachability: dashboard installs TurnLock with grant_executor.preempt_signal when the supported executor is enabled; create_grant_child runs a separate grant session and the executor checks that same signal.

## S3 — Inside-and-now control

- State: P
- Function: supervise the installation's current goal-work commitment and resource/constraint envelope in the optional stage-C mode.
- Disturbance / variety regulated: finite tokens/time, stalled work, completion claims, current execution state and the need to stop/resume a bounded commitment.
- Decisive decision or feedback right: issue a scoped goal grant, select total/per-iteration budget and tool/workspace/time envelope, pause/resume/revoke it and accept/reject its completion claim.
- Decision owner: the legitimate installation operator through host-confirmed control operations; no autonomous base S3 owner is established.
- Supporting / enforcement mechanisms: GrantService state/store, current grant APIs/panel, operation confirmation, AuthorityService epochs/permits and executor reservations/checks.
- Closure path: the operator reads current grant state/counters, returns an authenticated control operation, service state/epoch changes, and subsequent executor effects are admitted/refused or bounded by that returned decision; rejection of a completion claim returns the goal to active work.
- Why this is / is not agent-owned: the model can report progress or claim completion but cannot issue/loosen its own grant or mark itself verified. Removing the operator leaves fixed enforcement without the discretionary current commitment decision.
- Evidence: [docs/grants.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/grants.md); [docs/autonomy.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/autonomy.md); [src/stiracore/grants/service.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/service.py); [src/stiracore/grants/routes.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/routes.py); [src/stiracore/grants/executor.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/executor.py); [src/stiracore/authority/service.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/authority/service.py); [dashboard/stira_server.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/dashboard/stira_server.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Parent current-control over the bounded single-live-grant regime, not autonomous S3, multiple-goal portfolio optimization or S5. Generic tool approval alone is not the witness.
- Whole-system current view: the goal-grant panel/APIs expose the installation's live grant/goal state, remaining TTL/budget, iteration/stop/progress and claim-evidence counters; v1 allows at most one live grant.
- Current-control decision scope: commitment admission plus its resources/constraints and subsequent pause/resume/revoke/verification intervention on behalf of the installed service.
- Boundary reachability: dashboard server creates and routes GrantService only with stage_c; stage_c_exec adds the supported executor. Host-confirmation channel and configured prerequisite checks are part of this mode, not assumed universal defaults.

## S3* — Complementary audit

- State: —
- Function: No independent complementary runtime audit actor/feedback loop is supplied.
- Disturbance / variety regulated: unsafe actions, completion claims and untrustworthy operational reports.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: breaker heuristics, identity checks, prefix sycophancy monitoring, logs/hash chains, measured claim counters and human completion verification.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/stiracore/middleware/sycophancy_monitor.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/middleware/sycophancy_monitor.py); [src/stiracore/middleware/identity_guard.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/middleware/identity_guard.py); [src/stiracore/grants/executor.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/grants/executor.py); [docs/grants.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/grants.md); [src/stiracore/observability/audit_chain.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/observability/audit_chain.py); [docs/tool-audit.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/tool-audit.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: runtime guard/monitor paths, artifact/check counters, event/audit logging, human grant verification and adjacent eval/audit package.
- Plausible first-party paths checked: independently controlled raw-artifact challenge with a supplied audit judgment and returned corrective authority, distinct from ordinary production checks.
- Why no material first-party path remains: heuristic guards and records are enforcement/observability; grant verification is the ordinary parent supervisory acceptance path rather than a supplied independent audit organization. The evaluation/audit CLI and historical tool inventory are adjacent systems, not wired runtime owners.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied external-and-prospective adaptation-options loop is established.
- Disturbance / variety regulated: task experience, memory growth, reusable procedural notes and changing execution state.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: procedural proposal/staging/review, context rule injection, distillation/harvest and phase-0 memory ratings/jobs.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [src/stiracore/tools/procedure_tool.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/tools/procedure_tool.py); [src/stiracore/control/procedural_review.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/control/procedural_review.py); [src/stiracore/agent/context_assembler.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/agent/context_assembler.py); [docs/memory-autonomy.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/memory-autonomy.md); [docs/memory-maintenance.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/memory-maintenance.md); [docs/autonomy.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/autonomy.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Does not equate absent S4 with absent memory learning. A generic reusable-rule approval is not automatically prospective adaptation or parent S4.

### Absence scope

- Surfaces inspected: server-bound reusable-procedure proposal/review/return, context assembly, Harvest, memory-autonomy phase-0 and autonomous-scheduling roadmap.
- Plausible first-party paths checked: external/future sensing that generates alternative future capabilities and a function-specific adaptation judgment returning into present capability.
- Why no material first-party path remains: procedure approval can change later instructions but supplies generic experience/learning rather than an evidenced outside-and-then option-development relation; phase 0 deliberately changes no recall/retention and future self-scheduling/self-maintenance stages are not implemented.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy decision-and-return loop is supplied.
- Disturbance / variety regulated: identity file mutation, ordinary tool authority and bounded goal permission.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: No owner established for this function at the declared boundary.
- Supporting / enforcement mechanisms: SOUL/IPD read-only paths, IdentityGuard, breaker floors, host rules/confirmations and permit epochs.
- Closure path: No qualifying organizational return path; ordinary task feedback is separate.
- Why this is / is not agent-owned: The examined paths do not supply the agent-owned or eligible parent-governed function.
- Evidence: [docs/soul-read-only.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/soul-read-only.md); [src/stiracore/middleware/identity_guard.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/middleware/identity_guard.py); [src/stiracore/tools/identity_tools.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/tools/identity_tools.py); [src/stiracore/control/procedural_review.py](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/src/stiracore/control/procedural_review.py); [docs/authority-service.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/authority-service.md); [docs/grants.md](https://github.com/Resolver-TNG/StiraCore/blob/2dee27f3c99c4f63b1ef2a7e377482d40c527996/docs/grants.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded source assessment of the supported distribution; no live model or performance claim.

### Absence scope

- Surfaces inspected: protected identity paths, layer/guard enforcement, parent tool/grant confirmation, procedure approval and authority service.
- Plausible first-party paths checked: a genuine identity/ultimate-policy issue reaching legitimate ultimate authority and returning binding identity governance.
- Why no material first-party path remains: identity text is protected static configuration and changes require external host editing/restart; procedural/task approvals and grant authority govern subordinate work, not a supplied identity-level adjudication transaction.

## Recursion

Chat, delegated agents and the grant child are isolated work contexts. No recursively viable contributor or organization-level system is inferred from them.

## Variety and escalation

Progress/blocker codes, approval cards, resource counters and stop reasons retain operational distinctions. Authority epochs and per-effect permits make returned narrowing effective. These enforcement/exception channels are not automatically agent-owned control or algedonic policy authority.

## Evidence gaps

No live Bedrock/provider, grant, scheduler or LLM-agent E2E run. Optional flags, host confirmation and platform limits remain explicit. S3=P is scoped to the complete shipped current-grant supervision loop; S2=C is the concrete preemption relation. Model-free guards, static identity and generic memory proposals are not promoted by their names. Future/unpublished implementations and adjacent eval actors remain outside this assessment.
