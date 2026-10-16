---
harness_id: superqode
project_name: SuperQode
repository: https://github.com/SuperagenticAI/superqode
review_ref: 5284b049e5e39e3159ca1a178ac4c655a3305a26
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# SuperQode

## Review boundary

- System in focus: the first-party installed SuperQode Python harness/tooling suite at frozen `5284b049e5e39e3159ca1a178ac4c655a3305a26`, including native agent coding execution, optional WorkOrder coding division and user-operated HarnessSpec improvement/promotion lifecycle. The recursion considered is one managed local coding-work system, not every registered third-party agent or SuperagenticAI's organization.
- Purpose and identity: execute repository work through model-selected tools, coordinate bounded work tasks, retain artifacts and allow an operator to inspect, govern, review and change the running harness configuration.
- Relevant environment: repositories, shell/tests, model endpoints, third-party ACP/A2A/SDK agents, harness specs, per-task worktrees and evaluation task sets.
- Standard-distribution boundary: installed `superqode` Python CLI and bundled first-party `agent`, `harness`, native RLM/PiPy backends, WorkOrders execution/CLI, evaluator and promotion subsystems. Optional native WorkOrders/reviewer and HarnessSpec promotion modes are explicitly declared; these are not asserted to run in every default chat.
- Credited operating / distribution surfaces: native `AgentLoop` plus first-party tools and model gateway; native RLM/PiPy backend adapters; `superqode work` commands, role-bound WorkOrder workers, isolated worktrees, integration conflict checks, independent reviewer task, status/cockpit and human operational control; `harness optimize-omni`, `harness promote` and code implementing held-out evidence-gated staging/canary/activation.
- Adjacent first-party surfaces excluded from ownership: docs/examples, benchmark suites as organizational actors, repository CI, release workflow, offline development and external hosted UHP registry. An eval set can supply evidence to the first-party **shipped promotion operation**, but its testing scripts alone are not a live S3* auditor. Third-party ACP coding CLI, vendor SDK, externally developed harness backend/weights or hosted agent cannot donate S1/S2/S3/S3*/S4 ownership.
- First-party operating / deployment modes considered: native locally model-driven interactive/headless coding session, opt-in native RLM/PiPy; first-party WorkOrder configured with native worker and reviewer roles in isolated worktrees; operator-controlled local WorkOrder cockpit/CLI; first-party candidate evaluation, staging, canary, activation and rollback. ACP, hosted vendors and third-party runtime routes considered solely as excluded alternatives. Neither WorkOrder configured reviewer nor model inference was exercised live during this source inspection.
- Recursion level: one SuperQode-managed coding work system (a native S1 session or a single WorkOrder containing distinct native task workers and a configured reviewer), with a parent operator controlling its current commitments and prospective HarnessSpec promotion. Function-specific positive states may rely on explicitly enabled WorkOrder/promotion modes and are not claimed in bare default chat.
- Reviewed revision: `5284b049e5e39e3159ca1a178ac4c655a3305a26`, frozen from Index intake #379.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

SuperQode is not exclusively an ACP shell. The native `AgentLoop` owns model-response parsing, tool execution and continuation ([src/superqode/agent/loop.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/agent/loop.py)); the first-party `HarnessSession.run` selects a backend, submits the request, records events and outcomes and applies approval/policy gates ([src/superqode/harness/kernel.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/kernel.py)). Built-in native RLM and PiPy backends are shipped independently of SDK/vendor routes ([src/superqode/harness/backends/rlm.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/backends/rlm.py), [src/superqode/harness/backends/pipy.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/backends/pipy.py)). A remote model provides inference, not an external coding-agent framework's decisions. Choosing an imported ACP/Codex/Claude/SDK route must not silently credit SuperQode with the imported agent's internal loops.

The optional first-party WorkOrder subsystem is a more demanding organizational boundary than bare agent chat. `work` CLI commands create, inspect, queue, resume, cancel, review, approve and merge orders ([src/superqode/commands/work.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/work.py)). `WorkOrderStore.claim_next_task` transactionally claims dependency-ready task units with resource/admission policy, while `run_until_idle` executes bounded native worker tasks; the WorkOrder integrates task-specific worktree patches with explicit changed-file collisions and returns a blocked task outcome on conflict ([src/superqode/workorders/store.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/store.py), [src/superqode/workorders/runner.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/runner.py), [src/superqode/workorders/integration.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/integration.py)). A distinct configured `REVIEWER` role reads integrated code and dependency evidence, must emit a typed verdict, and can veto integration; missing or nonapproved verdicts block the order.

Another supported but separate mode concerns **prospective harness capability change**. The CLI can run evidence-based candidate optimization and then `harness promote stage/canary/activate/rollback` against a user-selected HarnessSpec. The promotion logic enforces audit identity, held-out evidence, explicit actor and policy; `activate_harness_promotion` actually copies the approved candidate over the operational base spec, preserving rollback ([src/superqode/commands/harness/optimization.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/harness/optimization.py), [src/superqode/commands/harness/promotion.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/harness/promotion.py), [src/superqode/harness/promotion.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/promotion.py)). This parent-governed operating-mode closure is not equivalent to autonomous strategic intelligence by a single default coding session.

## Operational model

The default native coding session uses a model gateway to choose next actions; first-party tools are gated and their outcomes become the next model observation, eventually yielding a coding response. In an explicitly configured WorkOrder, the operator creates a goal, dependencies, budget, optional reviewer and acceptance constraints, then native task workers operate on isolated task worktrees. The first-party integration controller checks collisions against concurrent task changes, blocks the affected worker's state on conflict and returns that fact to the controller for parent remediation. A reviewer task is not the producer: its instruction asks it to inspect integrated repository state and dependency evidence, return `SUPERQODE_REVIEW` JSON and refrain from changes; a negative or missing verdict blocks progression. A parent has a current whole-order status, worker/budget/conflict/approval display and can choose to resume blocked work, cancel or approve an integration candidate.

Separately, operator-selected candidate HarnessSpecs can be evaluated against task/held-out evidence and are staged/canaried or activated under explicit operator and policy gates. Activation changes the base spec used for subsequent work, which is a first-party future-capability feedback path; the operator, not the model alone, owns the decisive promotion.

## S1 — Operations

- State: A
- Function: perform open-ended coding/inspection work with first-party model-steered code, file, tool and observation loops.
- Disturbance / variety regulated: unknown repo state, tool errors, changing files and nontrivial task progress.
- Decisive decision or feedback right: select task tools, arguments, follow-up steps and completion based on results.
- Decision owner: model-driven actor inside SuperQode's first-party `AgentLoop`; model service is an inference dependency.
- Supporting / enforcement mechanisms: gateway, tool registry/executor, policies, harness session, native RLM/PiPy modes, journal, checkpoint and WorkOrder native-worker configuration.
- Closure path: task → model output → tool calls / native executor → result observations → next model request or final task result. A WorkOrder task repeats this S1 pattern for each configured native worker.
- Boundary reachability: shipped native agent loop and native RLM/PiPy backend are reachable through installed CLI/harness runtime, without invoking a separate vendor coding agent. Credit is bounded to these first-party paths.
- Why this is / is not agent-owned: next engineering actions are chosen by a model within the native tool loop instead of a predetermined script; safety limits do not supply the model's decisions.
- Evidence: [src/superqode/agent/loop.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/agent/loop.py), [src/superqode/harness/kernel.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/kernel.py), [src/superqode/harness/backends/rlm.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/backends/rlm.py), [src/superqode/workorders/runner.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/runner.py).
- Basis: source-backed native loop and bundled runtime.
- Confidence: high for first-party structure, not a live model task benchmark.
- Caveats: external ACP/vendor routes are excluded from S1 attribution, and RLM/PiPy may require configured providers/dependencies.

## S2 — Coordination

- State: C
- Function: first-party constructor for conflict-specific attenuation between distinct native WorkOrder coding-worker S1 units.
- Disturbance / variety regulated: two isolated WorkOrder workers producing overlapping/conflicting patches for shared integration state.
- Decisive decision or feedback right: detect changed-path/write integration collision, reject competing integration and change the affected task from running to blocked so it cannot silently progress.
- Decision owner: deterministic first-party WorkOrder integration/store controller owns the conflict gate; a parent may later choose remediation and restart. This is not autonomous model negotiation.
- Supporting / enforcement mechanisms: per-task worktrees and baselines, integration lock, concurrent changed-path comparison, blocked task and explicit parent `resume`.
- Closure path: independent native worker task result → `integrate_task_workspace` compares patch files against concurrent changes → conflict list → `store.block_task` and work-order BLOCKED gate → conflict exposed in `work status` / cockpit → parent may adjust/retry the affected worker task. No uncontrolled auto-merge on conflict.
- Boundary reachability: supported `superqode work run/worker` uses `execute_claimed_task` which calls integration logic for patch roles when WorkOrder has task-scoped worktree isolation; all code is first-party and in the installed WorkOrder mode.
- Why this is / is not agent-owned: the conflict-specific coordination relation is implemented, but decision/repair relies on deterministic conflict gating and parent operation rather than an independent autonomous S2 agent; thus **C**, not A.
- Evidence: [src/superqode/workorders/runner.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/runner.py), [src/superqode/workorders/integration.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/integration.py), [src/superqode/workorders/store.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/store.py), [src/superqode/workorders/cockpit.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/cockpit.py).
- Distinct S1 units: separate first-party WorkOrder native coding tasks with independent run/worker IDs and task-local worktrees.
- Inter-S1 disturbance: overlapping modifications to the same integration candidate/base tree.
- Attenuating coordination relation: serialized integration and baseline/path collision check with blocked admission for conflicting patches.
- Feedback into subsequent S1 behaviour: block persists as task state; the worker cannot continue as accepted; parent sees conflict and may repair and resume/requeue the blocked task for a later attempt.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: actual cross-task overlapping writes are checked against concurrent state and alter the admissibility of a worker's contribution, rather than merely limiting concurrency or exchanging results.
- Basis: explicit shipped first-party conflict-to-block path.
- Confidence: medium-high for optional isolated WorkOrder mode.
- Caveats: deterministic construction with parent resolution; non-isolated/single-worker chat or external-agent routes do not provide this S2 claim.

## S3 — Inside-and-now control

- State: P
- Function: parent-governed current control of an entire configured WorkOrder's operational commitments, constraints and blocked/accepted execution.
- Disturbance / variety regulated: worker stalls, resource/budget exhaustion, patch conflict, reviewer veto and uncertain readiness of an order-wide integration.
- Decisive decision or feedback right: after whole-order cockpit/status evidence, operator can set/revise work task commitments and constraints, resume specific blocked work, stop/cancel an order, or approve/reject a prepared candidate; controller enforces the return.
- Decision owner: legitimate parent operator controlling the WorkOrder via `superqode work` CLI; not the default model or mere code-tool approval.
- Supporting / enforcement mechanisms: `work status/tree/usage/watch`, ordered task states/dependencies/budget, `WorkOrderStore.resume/cancel/accept`, conflict/approval gates and journalled decisions.
- Closure path: order-wide current status (tasks/workers/conflicts/budget/reviews) → human operational decision via `work resume/cancel/add-task/queue/approve/reject` → WorkOrder store transition → worker scheduling and acceptance change on next operation.
- Boundary reachability: bundled `superqode work` commands operate on the first-party durable WorkOrder store; cockpit exposes whole-system state. Parent decisions are implemented in store actions and subsequent worker dispatch; no external organization control plane is imported.
- Why this is / is not agent-owned: this qualifies solely as parent mode `P`, not autonomous `A` or constructor `C`. A generic tool approval alone would not suffice; evidence is the order-wide current-state observation and distinct parent control actions that change ongoing task commitments.
- Evidence: [src/superqode/commands/work.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/work.py), [src/superqode/workorders/store.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/store.py), [src/superqode/workorders/cockpit.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/cockpit.py), [src/superqode/workorders/runner.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/runner.py).
- Whole-system current view: order status, individual worker leases and tasks, conflicts, remaining budget, policy and review/check gates and integration decision in cockpit.
- Current-control decision scope: assign additional tasks/constraints at the WorkOrder level; stop/restore blocked operational flow and accept/reject controlled integration under budget/risk.
- Basis: parent-governed current WorkOrder decision/return evidence.
- Confidence: moderate; mode-specific to WorkOrder parent CLI.
- Caveats: do not transfer this S3 parent authority to a native standalone coding turn, static workflow or external vendor harness.

## S3* — Complementary audit

- State: A
- Function: a configured native WorkOrder **reviewer** acts independently of its producer coding worker to test a code-change acceptance claim against actual integration state and dependency evidence.
- Disturbance / variety regulated: producer may claim a patch is correct while resulting code and checks reveal defects.
- Decisive decision or feedback right: model-driven reviewer child owns a distinct code-correctness verdict, which the WorkOrder controller requires before integration can progress.
- Decision owner: separate first-party `REVIEWER` task executing its own harness run, not the producing worker's in-band summary; first-party controller checks the verdict and blocks on nonapproval.
- Supporting / enforcement mechanisms: WorkTaskRole.REVIEWER prompt, separate task/workspace scope, evidence-only mutation check, `SUPERQODE_REVIEW` JSON parsing, stored review artifact and integration approval precondition.
- Closure path: earlier coding task/integrated source state and dependency evidence → configured separate reviewer native run → structured approved/changes_requested evidence → `_enforce_role_contract` returns BLOCK for failure or nonapproval → `prepare_integration` rejects missing/nonapproved reviewer verdict → parent observes remedy/block; successful review allows separate checks/parent merge decision.
- Boundary reachability: `superqode work add-task --role reviewer` / task creation and bundled `run_until_idle` execute configured reviewer tasks through first-party harness runner; `_task_prompt` requests examination of integrated state; enforcement exists in installed WorkOrder and integration code. No uninstalled development test or stand-alone CI is used.
- Why this is / is not agent-owned: reviewer model owns substantive code-quality adjudication within a distinct S1-independent role/task and returns findings through explicit controller gate; guard itself is deterministic but does not replace reviewer judgment.
- Evidence: [src/superqode/workorders/models.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/models.py), [src/superqode/workorders/runner.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/runner.py), [src/superqode/workorders/integration.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/workorders/integration.py), [src/superqode/commands/work.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/work.py).
- Claim being audited: correctness/acceptability of integrated code produced by coding worker(s), not the generic model's own `done` text.
- Ordinary reporting path: producer task run result and self-reported completion with artifacts and tool output.
- Complementary access path: reviewer role reads integrated repository state and predecessor evidence in a separate task, with evidence-only file guard.
- Independence boundary: distinct worker/role/task and workspace scope, separate native harness run, reviewer cannot become author by changing files without a violation. The same external inference provider may still be configured; this is operational independence of roles, not an independently attested external reviewer.
- Who acts on findings: WorkOrder controller blocks task/completion or refuses integration when verdict is negative/missing; parent can inspect outcomes and decide correction/resume.
- Basis: explicit first-party reviewer task + binding integration-gate path.
- Confidence: moderate for configured native WorkOrder reviewer; live reviewer decision results were not independently exercised.
- Caveats: positive `A` is **mode-specific and source-backed**, not proof default chat always audits, not an independent organizational assessment or paper-grade S3* audit. Merely configured vendor reviewer without a native first-party actor is excluded.

## S4 — Outside-and-then intelligence

- State: P
- Function: parent-governed prospective change of installed HarnessSpec capability based on external/held-out workload evidence.
- Disturbance / variety regulated: changing task distributions, regressions or inadequate model/harness capability relative to evaluation tasks outside a single production prompt.
- Decisive decision or feedback right: operator chooses candidate evaluation, staging/canary, activation or rollback based on independent held-out/test evidence and policy rather than the coding model autonomously rewriting its own spec.
- Decision owner: parent operator with required actor identity; evaluation and policy machinery constrain the choice, while no autonomous S4 owner is demonstrated.
- Supporting / enforcement mechanisms: `harness eval`, `optimize-omni`, candidate audit/held-out gates, staged snapshot, canary %, promotion policy, `activate_harness_promotion` and rollback.
- Closure path: external held-out tasks/eval results → candidate HarnessSpec with audit → parent command stage/canary/activate and policy approval → atomic candidate copy to base operational HarnessSpec → subsequent sessions use changed capability; rollback can restore original.
- Boundary reachability: installed `superqode harness optimize-omni` and `harness promote` CLI commands wire to first-party candidate audit and activation modules; actual base spec copy is a committed runtime configuration change rather than mere advice.
- Why this is / is not agent-owned: decisive future/capability adaptation is parent-controlled `P`. Built-in optimizer/eval/GEPA facilities supply candidate evidence; they do not establish that an autonomous S4 agent owns the promotion.
- Evidence: [src/superqode/commands/harness/optimization.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/harness/optimization.py), [src/superqode/commands/harness/promotion.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/harness/promotion.py), [src/superqode/harness/promotion.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/promotion.py), [src/superqode/harness/eval.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/eval.py).
- External distinction: held-out workload/evaluation evidence rather than the same current coding tool result.
- Future / prospective distinction: selecting whether a candidate HarnessSpec should replace the base for future tasks.
- Adaptation option generated: candidate spec from optimized/modified harness choices.
- Path back into current capability / S3: staged→canary→policy-gated activated spec copied to the base; parent decision changes the subsequently runnable harness.
- Basis: first-party promotion state machine and user-governed action path.
- Confidence: medium-high that optional parent mode exists, without claim it was exercised live during this assessment.
- Caveats: user invocation, evaluation input and operator authorization are required; optimization research artifacts alone are not S4.

## S5 — Identity and ultimate policy

- State: —
- Function: no supported distinct first-party rightful ultimate organizational identity/policy judgment loop above WorkOrder/current controls.
- Disturbance / variety regulated: unsafe tools, budget, promotion risk and authorizations can be constrained by policies but are not identity-purpose conflicts resolved by S5.
- Decisive decision or feedback right: adjudicate who the overall organizational system is, what ultimate purposes/policies prevail and return authoritative identity/policy decisions to S3/S4; not demonstrated.
- Decision owner: project/operator supplies configuration and governance rules, first-party engine enforces them; WorkOrder operator actions provide S3 and HarnessSpec promotion S4, not identity-level policy.
- Supporting / enforcement mechanisms: `superqode.governance`, user approvals, policy engine, budget/cap and promotion authorization.
- Closure path: existing configured rules can block unsafe requests/promotion; no higher first-party S5 identity decision and return loop established.
- Why this is / is not agent-owned: centralized allow/deny configuration and a human merge/promotion decision do not automatically constitute a legitimate ultimate organizational-purpose adjudicator.
- Evidence: [src/superqode/governance.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/governance.py), [src/superqode/harness/kernel.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/kernel.py), [src/superqode/harness/promotion.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/harness/promotion.py), [src/superqode/commands/work.py](https://github.com/SuperagenticAI/superqode/blob/5284b049e5e39e3159ca1a178ac4c655a3305a26/src/superqode/commands/work.py).
- Basis: bounded negative after checking plausible parent and first-party paths.
- Confidence: moderate.
- Caveats: external adopter/maintainer organization may own S5, but it is outside this installed system assessment.

### Absence scope

- Surfaces inspected: CLI commands for operator tasks, global governance/policy decisions, WorkOrder and harness promotion gates and host project/release policy.
- Plausible first-party paths checked: policy engine allowed/denied actions, operator work decisions, promotion activation policy and meta-level project maintainers.
- Why no material first-party path remains: none resolves legitimate identity and ultimate purpose/policy at a distinct S5 recursion with a returned authoritative decision; parent action here is specific current WorkOrder (S3) or prospective capability (S4) control.

## Evidence gaps

- No live external-model run, production WorkOrder reviewer execution or held-out promotion experiment was run. Positive states derive from pinned shipped first-party wiring and explicit supported modes; operational reliability/performance/independence beyond those modes remains unmeasured.
- For S2, task conflict-gate construction has concrete inter-worker interference evidence; no autonomous coordination actor is claimed.
- For S3*, reviewer is positive only for **explicitly configured native WorkOrder**; one cannot transfer its role-specific result to generic chat, prompt-only reviewers or external ACP-agent internals. True independence from the provider and the creator cannot be asserted.
- S4 is explicitly parent-owned and opt-in; external optimization algorithms/GEPA backends are not credited with owning first-party strategy decisions. The actual parent selected spec/policy gate is the decisive boundary.

## Conclusion

At the declared multi-mode installed SuperQode boundary, native model-directed coding operations qualify as S1=A; first-party WorkOrder patch-conflict attenuation is a constructor S2=C; the real WorkOrder parent has order-wide current control S3=P; a separately configured native WorkOrder reviewer task provides auditable, binding model-owned S3*=A return; and an optional parent-approved held-out HarnessSpec promotion path establishes S4=P. S5 identity/ultimate-policy judgment is not established. This mode-specific vector **A / C / P / A / P / —** must not be read as automatically active in every default TUI/ACP or vendor-only route. The standalone proposal is source-first, revision-bound, and not canonical until Index admission.
