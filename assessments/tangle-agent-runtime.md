---
harness_id: tangle-agent-runtime
project_name: Tangle Agent Runtime
repository: https://github.com/tangle-network/agent-runtime
review_ref: ed008c7623362720c47b1e628dbc19073e196b91
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# Tangle Agent Runtime

## Review boundary

- System in focus: the first-party `@tangle-network/agent-runtime` execution kernel at frozen revision `ed008c7623362720c47b1e628dbc19073e196b91`, especially `Scope`/Supervisor, `supervise`, coordination tools, conserved-budget execution, completion checks, trace-analysis seams, and the detached `improve`/proposal/activation path.
- Purpose and identity: an execution substrate for exact, measurable agent runs that can coordinate one or many agents under conserved budgets, retain execution records, supervise dynamic recursive trees, and keep optimization/search separate from live activation.
- Relevant environment: callers/applications, external model providers, worker backends and sandboxes, `agent-eval`, knowledge/evaluation packages, repositories/workspaces, and human/application reviewers.
- Standard-distribution boundary: shipped runtime kernel, recursive scope, supervisor, coordination tools, budget pool, journaling/recovery, checks, trace-analysis routing, improvement/proposal/activation contracts and public entry points are inside. External model cognition, caller-supplied domain objectives/check semantics, application-owned atomic writes, external benchmark campaigns, and adjacent package actors are not silently imported as first-party decision owners.
- Credited operating / deployment surfaces: `supervise(profile, task, opts)`, recursive `Scope`/Supervisor execution, the model-driven coordination verbs over a live scope, supported worker backends, completion-gated delivery, and first-party improvement/proposal/activation APIs where explicitly composed.
- Adjacent first-party surfaces excluded from ownership: tests/CI, repository governance, research plans, benchmark campaigns, external write-only final judges, and examples except as corroboration of shipped runtime reachability.
- Recursion level: child agents/workers are operational S1 units; a model-driven parent/supervisor can act over the active worker tree. Positive S2/S3/S3* claims are assessed at this multi-worker supervision recursion.
- Reviewed revision: `ed008c7623362720c47b1e628dbc19073e196b91`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The runtime defines one recursive agent atom: an `Agent` acts inside a `Scope`, may spawn children, observes their progress/results, and can steer or stop them. The public `supervise` front door supplies a model-driven manager with coordination verbs over that live scope. The runtime owns the live nursery, journaling/recovery, global nested-worker limits and a conserved budget pool; worker/provider cognition remains outside the repository boundary.

A parent can declare a deliverable check. A worker is delivered only when its real output passes that check; worker self-report does not establish completion. The coordination layer also exposes analyst/check seams over worker traces. However the repository explicitly separates the external final judge from the execution tree and forbids feeding that judge into steering/selection.

Across runs, `improve()` can materialize candidate profile/code surfaces, execute a complete optimization method, isolate the final-test partition, compare the selected candidate with baseline, and bind a measured candidate into proposal/review/activation records. The caller still supplies domain execution/objectives and the application owns the final atomic write into its live state.

Primary evidence:

- [`README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/README.md) — public runtime front doors, supervision, completion checks and detached improvement boundary.
- [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md) — recursive `Agent`/`Scope` model, spawn/observe/steer/stop, checks, analyst findings and judge firewall.
- [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md) — dynamic model-owned orchestration and public supervisor/check behavior.
- [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts) — authoritative live nursery, recursive child lifecycle, budget reservation/reconciliation and recovery.
- [`src/runtime/supervise/budget.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/budget.ts) — atomic conserved-resource reservation and fail-closed admission.
- [`src/runtime/supervise/types.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/types.ts) — agent/executor control surface including progress, steer and cancel.
- [`src/mcp/tools/coordination.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/mcp/tools/coordination.ts) — live-scope coordination and trace-analyst paths.
- [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md) — detached candidate generation/measurement, proposal review and activation boundary.
- [`docs/learning-flywheel.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/learning-flywheel.md) — explicit learning/adaptation composition boundaries and independent-assessment obligations.
- [`examples/supervise/README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/examples/supervise/README.md) — corroborates the shipped one-call model-driven supervisor and completion gate.

## Operational model

A caller supplies a task and supervisor profile. The supervisor model chooses at runtime which workers to spawn and how to react to their current state. Each child executes through a configured backend under a recursively shared scope; reservations are made before admission, measured spend is reconciled, and live descendants are journaled/recoverable. The manager can observe events/progress, issue steering, stop work, and continue until a parent deliverable check accepts an actual worker result or a hard resource/termination condition ends the run.

The vector therefore credits the model-driven supervised runtime where the repository supplies a complete current-control path. It gives constructor credit where the repository supplies a function-specific organizational mechanism but the decisive semantic actor or deployment closure must be supplied by composition.

## S1 — Operations

- State: A
- Function: perform delegated task work through agentic worker loops that act on task state and return operational results.
- Disturbance / variety regulated: changing task state, tool results, external workspace state, failures, incomplete information and provider/backend responses encountered by a worker.
- Decisive decision or feedback right: choose substantive next actions within the worker harness in response to task observations.
- Decision owner: the executing model-driven worker agent.
- Supporting / enforcement mechanisms: worker executors/backends, `Agent.act`, tool/harness integration, scope lifecycle, retries, accounting and result settlement.
- Closure path: assigned task → worker agent inference/action → environment/tool result → later worker decision → settled operational output.
- Boundary reachability: workers are the ordinary execution units used by the shipped `supervise`/Supervisor runtime; no development-only actor is required.
- Why this is / is not agent-owned: runtime code constrains and records execution, while the worker model owns the substantive task-action choices.
- Evidence: [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md); [`src/runtime/supervise/types.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/types.ts).
- Basis: explicit + structural.
- Confidence: high.

## S2 — Coordination

- State: C
- Function: attenuate resource-contention disturbance among concurrently active child S1 units sharing one finite execution budget.
- Disturbance / variety regulated: concurrent children can collectively request more tokens/USD/iterations/named resources or live-worker slots than the parent scope can safely commit.
- Distinct S1 units: concurrently executing child agents inside one recursive supervisor tree.
- Inter-S1 disturbance: simultaneous child reservations contend for the same finite parent-owned resource pool; uncoordinated admission could overcommit capacity and invalidate later operation.
- Attenuating coordination relation: the first-party conserved `BudgetPool` reserves all enforced channels atomically at spawn, rejects an admission when free capacity cannot cover it, reconciles measured spend at settlement, refunds known unused capacity and preserves reservations across recovery.
- Feedback into subsequent S1 behaviour: spawn refusal/shortfall and changed free capacity are returned into the manager's live coordination path, changing which workers can be admitted or what the manager does next.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited witness is a concrete cross-worker finite-resource interference and an atomic admission/reconciliation mechanism specifically preventing oversubscription, not delegation or a shared counter by itself.
- Decisive decision or feedback right: the runtime deterministically arbitrates whether a requested reservation fits; a composed manager can then choose the organizational response to refusal/remaining capacity.
- Decision owner: no autonomous S2 owner is established by the first-party reservation mechanism itself; the arbitration outcome for a given reservation request is deterministic.
- Supporting / enforcement mechanisms: `BudgetPool`, atomic reservation/reconciliation, root-wide `maxLiveWorkers`, fail-closed unknown measurements and typed spawn rejections/shortfalls.
- Closure path: multiple S1 commitments compete for finite shared capacity → first-party admission checks reserve or reject atomically → resulting capacity/refusal is exposed to the manager → later spawn/work choices operate under the reconciled pool.
- Boundary reachability: this machinery is in the shipped recursive `Scope`/`supervise` path and applies across nested children.
- Why this is / is not agent-owned: the coordination function is materially implemented first-party, but the decisive collision arbitration is enforced deterministically rather than selected by an autonomous coordination actor. A composed manager can own the response, hence constructor rather than autonomous credit.
- Evidence: [`src/runtime/supervise/budget.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/budget.ts); [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts); [`examples/supervise/README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/examples/supervise/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of the supervised worker tree and exercise present-tense authority over commitments, steering, cancellation and further allocation.
- Disturbance / variety regulated: active workers can stall, fail, exceed assumptions, need redirection, finish asynchronously or leave the parent objective incomplete while budget and live-worker capacity change.
- Whole-system current view: the parent/supervisor acts over one authoritative `Scope` containing the live child set, events, progress, settlements, spend/reservations and recursively nested execution state.
- Current-control decision scope: spawn new workers, await/observe current work, steer active workers, stop/cancel work, react to completion checks, and choose the next move under remaining budget/depth/concurrency limits.
- Decisive decision or feedback right: choose at runtime which worker commitments to create, continue, redirect or terminate and when the supervised objective is sufficiently complete to stop.
- Decision owner: the model-driven supervisor/driver agent supplied through the shipped `supervise`/coordination path.
- Supporting / enforcement mechanisms: `Scope`, Supervisor, coordination MCP tools, journals/recovery, progress/trace access, conserved budgets, nested-worker caps, cancellation and completion-gated finalization.
- Closure path: live worker/progress/settlement/resource state enters the parent coordination context → supervisor model chooses spawn/observe/steer/stop/next action → first-party runtime applies it to the live tree → changed worker/fleet state returns through the same scope.
- Boundary reachability: `supervise(profile, task, opts)` is a public first-party front door explicitly described as one manager agent driving workers under one budget; the example is corroboration, not the owner.
- Why this is / is not agent-owned: deterministic scope/budget machinery enforces constraints, but the runtime topology and intervention choices are explicitly delegated to the supervisor model rather than fixed in code.
- Evidence: [`README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/README.md); [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md); [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts); [`src/mcp/tools/coordination.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/mcp/tools/coordination.ts).
- Basis: explicit + structural.
- Confidence: high.

## S3* — Audit / monitoring

- State: C
- Function: independently check operational claims/results through evidence paths that do not rely on the producing worker's own success assertion, and return findings into control.
- Disturbance / variety regulated: a worker can claim completion despite a wrong artifact/result, or ordinary worker reporting can omit failures visible in direct output/trace evidence.
- Claim being audited: whether a worker result actually satisfies the parent deliverable and, for analyst routes, what operational failures/patterns are present in the worker's tool-trace evidence.
- Ordinary reporting path: worker settlement/final output and normal progress/results returned to the parent.
- Complementary access path: parent deliverable checks execute against the actual worker output; trace analysts can read structured worker trace evidence and publish findings separately from the worker's prose report.
- Independence boundary: the check/analyst executes outside the producing worker's self-report path. The architecture separately keeps the external final judge write-only and outside steering/selection, so that judge is not borrowed as an internal autonomous owner.
- Who acts on findings: the supervisor/driver can consume failed completion status or routed analyst findings and revise subsequent control decisions.
- Decisive decision or feedback right: first-party runtime supplies the independent-check and finding-return structure; caller/deployment configuration supplies the substantive deliverable predicate/analyst registry or profile in the general case.
- Decision owner: no single autonomous first-party auditor is guaranteed by the base runtime; a composed verifier/analyst can own the judgment.
- Supporting / enforcement mechanisms: deliverable completion gate, verifier/check APIs, trace evidence, analyst registry/routes, finding events and judge-to-steering firewall.
- Closure path: worker produces output/trace → independent first-party check/analyst path reads direct evidence → pass/fail/finding reaches supervisor → supervisor changes acceptance/continuation/steering.
- Boundary reachability: completion-gated delivery is part of the public supervisor API; analyst routes are shipped coordination mechanisms, but their substantive audit actor/policy is composition-dependent.
- Why this is / is not agent-owned: the repository closes a function-specific independent evidence path and feedback return but does not guarantee a standalone autonomous auditor with its own substantive judgment in every supported deployment.
- Evidence: [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md); [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md); [`src/mcp/tools/coordination.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/mcp/tools/coordination.ts).
- Basis: explicit + structural.
- Confidence: medium-high.

## S4 — Intelligence / adaptation

- State: C
- Function: construct and independently measure candidate changes to the agent/profile/code surface for later operation while keeping search separate from final assessment and activation.
- Disturbance / variety regulated: current agent configuration can underperform on future/fresh work, and search can overfit or accidentally mutate the live system before independent validation.
- External distinction: the improvement path consumes caller-supplied scenarios/objectives and can use production/search findings about performance against an environment/domain outside the current execution tree.
- Future / prospective distinction: train/selection/test partitions and detached candidate materialization explicitly ask whether a changed profile/code surface should be used in subsequent runs rather than merely completing the present worker action.
- Adaptation option generated: optimization methods/candidate generators produce changed complete profile/code/tool/MCP/memory surfaces with exact candidate identity and diffs.
- Path back into current capability / S3: selected candidates are independently re-measured on a held-out final-test partition, then can be bound into review/activation records; after authorized application-owned atomic write, later runtime execution uses the adopted surface.
- Decisive decision or feedback right: first-party runtime owns candidate identity, measurement binding, final-test isolation, review/activation records and result validation; the caller supplies the domain objective/execution and the application owns the final atomic write/adoption transaction.
- Decision owner: no autonomous first-party S4 actor closes the complete domain sensing→adaptation→adoption loop by itself; autonomous optimizers can be composed into the provided constructor.
- Supporting / enforcement mechanisms: `improve`, complete optimization-method integration, train/selection/test separation, candidate population/diffs, proposal review, activation identity/expiry/retry validation and application transaction port.
- Closure path: external/fresh performance evidence and scenarios → candidate generation/search → independent selected-candidate final-test comparison → review/activation object → application-owned authorized write → later runtime executes the changed capability.
- Boundary reachability: these are public runtime APIs, not merely research prose, but the repository explicitly documents the domain execution/objective and final storage/adoption composition boundaries.
- Why this is / is not agent-owned: the adaptation constructor is strong and first-party, while decisive domain adaptation/adoption remains composition-dependent; therefore constructor credit is appropriate rather than autonomous or parent-autonomous credit.
- Evidence: [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md); [`docs/learning-flywheel.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/learning-flywheel.md); [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md).
- Basis: explicit + structural.
- Confidence: medium-high.

## S5 — Identity / ultimate policy

- State: —
- Function: no qualifying first-party identity / ultimate-policy closure established within the assessed runtime boundary.
- Disturbance / variety regulated: not credited.
- Decisive decision or feedback right: not established for constitutional identity or ultimate policy.
- Decision owner: none identified in the assessed operating boundary.
- Supporting / enforcement mechanisms: profiles, permissions, budget/policy constraints, human review and activation authorization exist, but these are execution/adaptation controls rather than evidence of an identity-level policy organ.
- Closure path: no first-party path was found from an identity/ultimate-policy issue through legitimate ultimate authority and back into governing subsequent runtime operation.
- Boundary reachability: repository governance, caller/application policy and ordinary approval surfaces are outside or below the S5 threshold.
- Why this is / is not agent-owned: no qualifying S5 function is established, so autonomy is not graded.
- Evidence: [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md); [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md).
- Basis: explicit absence after boundary review.
- Confidence: high.

### Absence scope

- Surfaces inspected: root README and architecture/API docs; recursive supervision/runtime types; live `Scope`; conserved budget machinery; coordination/analyst tools; completion-gate descriptions; improvement, proposal, review and activation documentation.
- Plausible first-party paths checked: supervisor standing instructions/profile authority; static permissions and resource constraints; human/application proposal approval; candidate activation; external final judging; repository governance and identity-like profile metadata.
- Why no material first-party path remains: these surfaces govern task execution, verification, adaptation approval or application mutation. None establishes a runtime identity/constitutional issue, a legitimate ultimate-policy authority deciding it, and a closed return path by which that decision governs subsequent operation as S5.

## Recursion

The strongest supported recursive form is a manager agent operating over child agents that are themselves the same `Agent`/`Scope` building block. Nested managers can therefore recur without introducing a separate organizational type. The assessment credits only functions whose ownership remains visible at the chosen parent-over-workers recursion; the existence of recursion itself does not promote constructor states to autonomous states.

## Variety and escalation

The runtime constrains execution variety through finite budgets, depth/global-worker caps, materialization and recovery identities, cancellation, completion checks and explicit escalation/question channels. Those mechanisms support the credited functions but are not independently treated as VSM organs unless the required function-specific disturbance and feedback closure are present.

## Evidence gaps / terminal outcome

- Proposed vector: `S1=A / S2=C / S3=A / S3*=C / S4=C / S5=—`.
- Strongest direct autonomy evidence is the model-driven `supervise` current-control loop over a live recursive worker tree.
- S2 remains constructor credit because finite-resource contention is materially attenuated, but the reservation/admission decision for a concrete request is deterministic enforcement rather than autonomous coordination judgment.
- S3* remains constructor credit because the runtime supplies independent completion/trace evidence paths and return into control, while the substantive verifier/analyst is generally supplied by configuration/composition; the external final judge is explicitly not imported into steering.
- S4 remains constructor credit because candidate generation/measurement/proposal/activation structure is first-party, while domain objective/execution and final application adoption are explicitly outside the runtime's standalone ownership.
- No qualifying S5 identity / ultimate-policy loop was found.
