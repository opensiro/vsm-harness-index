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
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: C
autonomy_s5: —
---

# Tangle Agent Runtime

## Review boundary

- System in focus: first-party `@tangle-network/agent-runtime` at frozen revision `ed008c7623362720c47b1e628dbc19073e196b91`, especially `Scope`/Supervisor, `supervise`, coordination tools, conserved budgets, completion checks, trace-analysis seams, and the detached improvement/proposal/activation path.
- Purpose and identity: execution substrate for measurable agent runs that can coordinate recursive agent trees under bounded resources while separating search/measurement from live activation.
- Relevant environment: callers/applications, model providers, worker backends/sandboxes, adjacent eval/knowledge packages, repositories/workspaces, and human/application reviewers.
- Standard-distribution boundary: shipped runtime kernel, scope/supervisor, coordination tools, journaling/recovery, budget pool, completion/analysis mechanisms, and improvement/proposal/activation contracts are inside. External model cognition, caller-supplied domain objectives/check semantics, application-owned atomic writes, external benchmark campaigns, and adjacent-package actors are not imported as first-party owners.
- Credited operating / distribution surfaces: `supervise(profile, task, opts)`, recursive `Scope`/Supervisor execution, model-driven live coordination verbs, supported worker backends, completion-gated delivery, and first-party improvement/proposal/activation APIs.
- Adjacent first-party surfaces excluded from ownership: tests/CI, repository governance, research plans, benchmark campaigns, external write-only final judges, and examples except as corroboration of shipped reachability.
- Recursion level: child agents/workers are S1 units; a model-driven parent/supervisor acts over the active worker tree.
- Reviewed revision: `ed008c7623362720c47b1e628dbc19073e196b91`.
- Observation date: 2026-09-29.

## Repository architecture

The runtime defines a recursive agent atom: an `Agent` acts in a `Scope`, can spawn children, observe them, steer them, and stop them. The public `supervise` entry point places a model-driven manager over that live scope. The runtime owns live child state, durable journals/recovery, global nested-worker limits, resource accounting, and a conserved budget pool. A parent deliverable check can reject a worker result independently of the worker's own completion claim. Trace analysts/check seams can consume direct execution evidence. The external final judge is explicitly outside the execution tree and excluded from steering/selection.

Across runs, `improve()` can materialize candidate profile/code surfaces, execute optimization methods, isolate final-test evaluation, compare a selected candidate against baseline, and bind the result into proposal/review/activation records. Domain objectives/execution and the application's final atomic write remain explicit composition boundaries.

Primary evidence:

- [`README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/README.md)
- [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md)
- [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md)
- [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts)
- [`src/runtime/supervise/budget.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/budget.ts)
- [`src/runtime/supervise/types.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/types.ts)
- [`src/mcp/tools/coordination.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/mcp/tools/coordination.ts)
- [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md)
- [`docs/learning-flywheel.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/learning-flywheel.md)

## Operational model

A caller supplies a task and supervisor profile. The supervisor model decides at runtime what workers to spawn and how to react to live state. Children execute through configured backends under one recursive scope; budget is reserved before admission and reconciled after measured spend. The manager can observe progress/events, steer/cancel work, and continue until a parent completion check accepts a real result or a hard termination/resource condition ends the run.

## S1 — Operations

- State: A
- Function: perform delegated task work through agentic worker loops.
- Disturbance / variety regulated: changing task state, tool/environment results, failures, missing information, and backend/provider responses.
- Decisive decision or feedback right: choose substantive next actions from current task observations.
- Decision owner: executing model-driven worker agent.
- Supporting / enforcement mechanisms: worker executors/backends, `Agent.act`, tool/harness integration, scope lifecycle, retries, accounting, and settlement.
- Closure path: assigned task → worker inference/action → environment/tool result → later worker decision → operational output.
- Boundary reachability: workers are the normal execution units of shipped `supervise`/Supervisor paths.
- Why this is / is not agent-owned: host code constrains and executes actions, while model cognition owns substantive next-action choice.
- Evidence: [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md); [`src/runtime/supervise/types.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/types.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-side cognition remains external; credit is for the first-party execution loop around it.

## S2 — Coordination

- State: C
- Function: attenuate resource contention among concurrently active child S1 units sharing finite execution capacity.
- Disturbance / variety regulated: concurrent children can jointly request more tokens, USD, iterations, named resources, or live-worker slots than the parent can commit safely.
- Distinct S1 units: concurrently executing child agents in one recursive supervisor tree.
- Inter-S1 disturbance: simultaneous child reservations contend for one finite parent-owned resource pool; uncontrolled admission could overcommit capacity.
- Attenuating coordination relation: first-party `BudgetPool` reserves enforced channels atomically, rejects insufficient admission, reconciles actual spend, refunds known unused capacity, and restores reservations conservatively after recovery.
- Feedback into subsequent S1 behaviour: typed spawn rejection/shortfall and changed free capacity return into the live manager path and affect later spawn/work choices.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is a concrete cross-worker finite-resource interference plus an atomic attenuation mechanism, not messaging or delegation alone.
- Decisive decision or feedback right: runtime deterministically decides whether a requested reservation fits; a composed manager chooses what to do after refusal or changed capacity.
- Decision owner: no autonomous S2 owner is established by the deterministic reservation mechanism itself.
- Supporting / enforcement mechanisms: conserved budget pool, atomic reservation/reconciliation, root-wide worker cap, fail-closed unknown measurements, typed spawn rejections/shortfalls.
- Closure path: competing child commitments → reserve/reject atomically → capacity/refusal visible to manager → subsequent work choices operate under reconciled capacity.
- Boundary reachability: budget admission is part of shipped recursive `Scope`/`supervise` execution across nested children.
- Why this is / is not agent-owned: the S2-specific mechanism is first-party, but its collision arbitration is deterministic rather than autonomous, so constructor credit is used.
- Evidence: [`src/runtime/supervise/budget.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/budget.ts); [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic shared budgets are not credited by themselves; credit rests on finite cross-child contention and fail-closed admission/reconciliation.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of the supervised tree and exercise present-tense authority over commitments, steering, cancellation, and further allocation.
- Disturbance / variety regulated: active workers can stall, fail, drift, need redirection, finish asynchronously, or leave the parent objective incomplete while capacity changes.
- Whole-system current view: one authoritative `Scope` exposes the live child set, progress/events, settlements, spend/reservations, and recursively nested execution state to the manager path.
- Current-control decision scope: spawn, await/observe, steer, stop/cancel, react to completion checks, and choose the next move under current resource/depth/concurrency limits.
- Decisive decision or feedback right: decide which worker commitments to create, continue, redirect, or terminate and when the objective is complete enough to stop.
- Decision owner: model-driven supervisor/driver agent in the shipped `supervise`/coordination path.
- Supporting / enforcement mechanisms: `Scope`, Supervisor, coordination tools, journals/recovery, progress/trace access, budgets, worker caps, cancellation, and completion gating.
- Closure path: live worker/resource state → supervisor model decision → runtime applies spawn/steer/stop/etc. → changed tree state returns through the same scope.
- Boundary reachability: public `supervise(profile, task, opts)` is explicitly a manager agent driving workers under one budget.
- Why this is / is not agent-owned: deterministic machinery enforces constraints, while the supervisor model chooses dynamic topology/intervention at runtime.
- Evidence: [`README.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/README.md); [`docs/canonical-api.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/canonical-api.md); [`src/runtime/supervise/scope.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/runtime/supervise/scope.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this positive state is specific to the supported model-driven supervisor mode, not every fixed topology/combinator.

## S3* — Audit / monitoring

- State: C
- Function: check operational claims/results through evidence paths that do not rely on the producing worker's own success assertion and return findings into control.
- Disturbance / variety regulated: a worker can claim completion despite a wrong result, or ordinary worker reporting can omit failures visible in direct output/trace evidence.
- Claim being audited: whether worker output satisfies the parent deliverable and, for analyst routes, what failures/patterns appear in worker tool-trace evidence.
- Ordinary reporting path: worker settlement/final output and normal progress/results returned to the parent.
- Complementary access path: parent completion checks execute against actual worker output; trace analysts can read structured worker trace evidence and publish findings separately from worker prose.
- Independence boundary: check/analyst execution is outside the producing worker self-report path; the external final judge stays write-only/outside steering and is not borrowed as an internal owner.
- Who acts on findings: supervisor/driver consumes failed completion or routed analyst findings and can revise acceptance/continuation/steering.
- Decisive decision or feedback right: runtime supplies independent evidence/check/finding-return structure; deployment supplies substantive check/analyst semantics in the general case.
- Decision owner: no guaranteed autonomous first-party auditor exists in every base deployment; a composed verifier/analyst can own the judgment.
- Supporting / enforcement mechanisms: completion gate, verifier/check APIs, trace evidence, analyst routes, finding events, and judge-to-steering firewall.
- Closure path: worker output/trace → independent check/analyst path → pass/fail/finding → supervisor changes acceptance/continuation/control.
- Boundary reachability: completion-gated delivery and analyst coordination mechanisms are shipped runtime surfaces, while substantive audit configuration remains composition-dependent.
- Why this is / is not agent-owned: the first-party constructor closes evidence and feedback paths but not a mandatory autonomous auditor, so constructor credit is used.
- Evidence: [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md); [`src/mcp/tools/coordination.ts`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/src/mcp/tools/coordination.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the external benchmark judge is intentionally excluded from the execution-control tree and is not used to inflate this state.

## S4 — Intelligence / adaptation

- State: C
- Function: construct and independently measure candidate changes to agent/profile/code surfaces for later operation while separating search from final assessment and activation.
- Disturbance / variety regulated: current configuration may underperform on fresh/future work; search may overfit or mutate live state before independent validation.
- External distinction: improvement consumes caller-supplied scenarios/objectives and can use production/search findings about environment/domain performance outside the current execution tree.
- Future / prospective distinction: train/selection/final-test separation asks whether a changed surface should improve subsequent runs rather than merely finish the current action.
- Adaptation option generated: optimization methods/candidate generators produce changed profile/code/tool/MCP/memory surfaces with exact candidate identity/diffs.
- Path back into current capability / S3: selected candidates are independently final-tested, bound into review/activation records, and can become later runtime state after an authorized application-owned atomic write.
- Decisive decision or feedback right: runtime owns candidate identity, measurement binding, final-test isolation, review/activation records, and result validation; caller/application owns domain objective/execution and final adoption write.
- Decision owner: no autonomous first-party S4 actor closes the complete domain sensing→adaptation→adoption loop alone.
- Supporting / enforcement mechanisms: `improve`, optimization-method integration, partition separation, candidate diffs/population, proposal review, activation identity/expiry/retry validation, application transaction port.
- Closure path: external/fresh evidence → candidate generation/search → independent final-test comparison → review/activation → application write → later runtime uses changed capability.
- Boundary reachability: these are public runtime APIs, but documentation explicitly preserves caller/application composition boundaries.
- Why this is / is not agent-owned: the adaptation constructor is first-party and function-specific, while decisive domain adaptation/adoption remains composition-dependent.
- Evidence: [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md); [`docs/learning-flywheel.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/learning-flywheel.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: learning documentation explicitly says the complete process is not itself a demonstrated standalone learner; constructor credit does not assume that closure.

## S5 — Identity / ultimate policy

- State: —
- Function: no qualifying first-party identity / ultimate-policy function established within the assessed runtime boundary.
- Disturbance / variety regulated: identity-level or constitutional-policy disturbance is not established.
- Decisive decision or feedback right: no qualifying ultimate-policy decision right is established.
- Decision owner: none identified for an S5 function inside the assessed operating boundary.
- Supporting / enforcement mechanisms: profiles, permissions, resource constraints, human review, and activation authorization exist but are execution/adaptation controls rather than an identity organ.
- Closure path: no path was found from an identity/ultimate-policy issue through legitimate ultimate authority and back into subsequent runtime operation.
- Why this is / is not agent-owned: because no qualifying S5 function is established, autonomy is not graded.
- Evidence: [`docs/improve.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/improve.md); [`docs/architecture.md`](https://github.com/tangle-network/agent-runtime/blob/ed008c7623362720c47b1e628dbc19073e196b91/docs/architecture.md).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: ordinary human approvals, profile configuration, and repository governance are not treated as S5 by substitution.

### Absence scope

- Surfaces inspected: root/API/architecture docs; recursive supervision/runtime types; live scope; budget machinery; coordination/analyst tools; completion checks; improvement/proposal/review/activation surfaces.
- Plausible first-party paths checked: supervisor standing instructions/profile authority; permissions/resource constraints; proposal approval; candidate activation; external final judging; repository governance and profile identity metadata.
- Why no material first-party path remains: these surfaces govern task execution, verification, adaptation approval, or application mutation; none establishes an identity/constitutional issue, legitimate ultimate authority deciding it, and a closed return path governing later operation.

## Recursion

Nested managers use the same Agent/Scope building block as workers, so the organization can recur without a distinct organizational type. This does not promote constructor states to autonomous states.

## Variety and escalation

Finite budgets, depth/global-worker caps, exact execution identities, recovery, cancellation, completion checks, and explicit question/escalation channels bound operational variety. They support credited functions but do not create additional organs without function-specific ownership and closure.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=C / S3=A / S3*=C / S4=C / S5=—`.

S3 has the strongest direct autonomy evidence through model-driven supervision over a live recursive worker tree. S2 remains constructor credit because finite-resource contention is first-party attenuated but concrete reservation arbitration is deterministic. S3* remains constructor credit because evidence/check return is first-party while substantive verifier/analyst semantics are generally composed. S4 remains constructor credit because candidate measurement/proposal/activation is first-party while domain objective/execution and final application adoption are explicit external closures. No qualifying S5 loop was found.
