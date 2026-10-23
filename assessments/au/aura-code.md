---
harness_id: aura-code
project_name: Aura Code
repository: https://github.com/DusanCar-sudo/aura-code
review_ref: 6fa7733b34ead5458fbf865efe7e2769c57377c3
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# Aura Code

## Review boundary

- System in focus: Aura Code's shipped TypeScript coding-agent CLI/REPL, its explicit multi-agent orchestration, tool-spawned subagents, optional verification and Archimedes modes, and the first-party protocol/board UI controlling task runs. This is an assessment of **an active user coding organization**, not the upstream Aura open-source developer community.
- Purpose and identity: execute natural-language tasks by exploring, editing, testing and reporting on a user's workspace; split work into specialist runs when supported; monitor current work, inspect selected claims and adapt some future model-capability routing from accumulated evidence.
- Relevant environment: changing repository files, provider/tool outputs, task scope and dependency, failed/blocked review findings, subordinate outcomes, current operator board state, external/local model availability and historical verified attempts.
- Standard-distribution boundary: CLI `src/cli/index.ts`, model runtime `src/agent/loop.ts`, `src/orchestration/` planner/executor/specialists, `src/verify/`, `src/archimedes/`, task tool and the shipped protocol/board runtime. External providers and operator-configured models, arbitrary MCP/plugins, customer project files, and test fixtures are dependencies, not first-party organizational decision owners.
- Credited operating / distribution surfaces: CLI default loop and model-triggered routing, explicit `--orchestrate`/`--build` specialist plan execution, `spawn_task` child loop, optional `--verify` deterministic completion checks, the orthogonal Archimedes alternation path enabled in config/REPL, and first-party board task/swarm start/stop/status paths.
- Adjacent first-party surfaces excluded from ownership: contributor `AGENTS.md`, project roadmap/screenshots, site, offline `tests/`, `scripts/` showcases, standalone development `--analyze`/`--propose-harness`/`--apply-harness` source-patching commands, and external publication/team governance. User-authored skills and future fine-tuning are not assumed to be implemented in the installed product.
- Modes inspected: solo model-driven coding loop; model-routed or explicitly requested specialist DAG with optional read-only reviewer; model-visible `spawn_task`; user-issued board/swarm tasks; opt-in `--verify` and opt-in learned Archimedes routing. These are **different modes**: CLI `--verify` is evaluated before Archimedes, so their functional evidence cannot be silently described as one simultaneous run.
- Recursion level: one user task with a lead agent/plan and independently executing specialist or child model loops. Board swarm executes independently selected agents sharing a workspace, but explicitly does **not** provide file-level collision locks inside a swarm. Deeper complete metasystem recursion is not established.
- Reviewed revision: `6fa7733b34ead5458fbf865efe7e2769c57377c3`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The standard TypeScript `runAgentLoop` owns model/tool turns and permission-mediated workspace actions. Its `spawn_task` tool registers a real child `runAgentLoop`, returning a result to the parent model. At the CLI entry point, a first-party routing model may decide to decompose a task; `--orchestrate` also enters this path explicitly. `createPlan` produces specialist task cards and a dependency DAG from a separate model invocation, and `executePlan` runs ready specialist agents, tracks their status, returns findings and persists outcomes. The plan's first-party read-only `runReviewer` is an independent model/tool loop with a review-specific brief; a blocking structured verdict can reopen a coder step, re-run review and ultimately block downstream tasks under a one-retry cap.

The user-facing board also runs real task sessions and can launch multiple model-backed swarm agents. Ordinary board writer tasks are serialized, but `swarm.ts` explicitly states that the single-writer queue does not cover simultaneous swarm edits. Thus S2 must be grounded in the *specialist dependency/review feedback* path rather than an imaginary universal shared-file mutex.

In a separate opt-in CLI `--verify` mode, the host checks filesystem/tool evidence and optional tests after a model turn, then supplies failure context for a bounded retry. Separately, the opt-in `ArchimedesAlternator` loads previously saved task episodes, estimates local-model competence on similar future tasks, selects a local read-only loop or a large-model path, tests local answers through a second verifier call, records the resulting outcome and occasionally probes low-competence patterns. This is a reproducible, deterministic policy update over observed future-task model capacity, not autonomous strategic self-redesign of the whole harness.

First-party pinned source and offline-test entry points:

- [`src/cli/index.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/cli/index.ts), [`src/agent/loop.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/loop.ts), [`src/agent/spawner.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/spawner.ts).
- [`src/orchestration/router.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/router.ts), [`src/orchestration/orchestrator.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/orchestrator.ts), [`src/orchestration/executor.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/executor.ts), [`src/orchestration/specialists.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/specialists.ts).
- [`src/verify/index.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/verify/index.ts), [`src/verify/checks.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/verify/checks.ts); [`src/agent/swarm.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/swarm.ts) and [`src/protocol/handler.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/protocol/handler.ts).
- [`src/archimedes/alternator.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/archimedes/alternator.ts), [`src/archimedes/competence.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/archimedes/competence.ts), [`src/archimedes/episode-capture.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/archimedes/episode-capture.ts).

## Operational model

The model can solve a task directly or choose child/model-specialist delegation. A first-party planning model constructs the dependency/role map and separate specialists work on it, with a reviewer able to detect and block a claimed implementation and send it back for a bounded revision. A human board operator can assign, prioritize or stop active current work. When Archimedes is enabled, actual prior results also affect which inference capacity is trusted on later tasks. None of this supplies a runtime authority that can legitimately adjudicate the organization's ultimate mission or governing identity.

## S1 — Operations

- State: A
- Function: model-chosen observation, coding, command execution, verification actions and correction against a task.
- Disturbance / variety regulated: task uncertainty, changed code, tool failures, unsuccessful test runs, read-only boundaries, provider errors and user steering.
- Decisive decision or feedback right: select next tools or delegate a subproblem after observing returned workspace and tool evidence.
- Decision owner: lead `runAgentLoop` model and separately invoked specialist/child model loops for scoped work.
- Supporting / enforcement mechanisms: registered workspace/search/shell/test tools, permission system, history/context, provider adapter, task budget and user steering.
- Closure path: user task → model selects file/search/shell/child operation → tool performs or rejects the action → returned result drives the next model decision and final output.
- Boundary reachability: the CLI default path invokes `runAgentLoop`; `spawn_task` is wired from the run loop to `makeDefaultSpawner`, and specialist/Archimedes modes instantiate the same model-backed operation loop in shipped paths.
- Why this is / is not agent-owned: tooling and permissions are deterministic, but they do not independently decide task-specific actions and remedies without the model.
- Evidence: [`src/agent/loop.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/loop.ts); [`src/agent/spawner.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/spawner.ts); [`src/tools/index.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/tools/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: source and offline mock tests validate routing, not live task success; externally hosted models are inference dependencies, not independently assessed Aurora subsystems.

## S2 — Coordination

- State: A
- Function: attenuate cross-specialist dependency, handoff and rejection disturbances among distinct independently acting task workers.
- Disturbance / variety regulated: a reviewer acting before a coder's prerequisite, competing readiness and failure states, invalid downstream activation after a broken upstream step, and stale previous implementation context after a reviewer requires rework.
- Distinct S1 units: model-backed researcher/coder/reviewer/planner task runs with separate prompts, tool limits, result/state identities; parent and spawned subagent loops are also distinct, but their existence alone is not positive S2 evidence.
- Inter-S1 disturbance: a reviewer or dependent implementer must consume the right previous implementation status and current artifact; if an upstream coder fails or reviewer blocks its output, starting dependent workers would consume an invalid result.
- Attenuating coordination relation: the model-proposed `dependsOn` DAG guards specialist readiness; the executor propagates failed prerequisites, feeds verified review verdicts back to the coder, resets superseded coder context and re-arms the reviewer. A distinct board path serializes normal writer tasks, although swarm writers remain unguarded.
- Feedback into subsequent S1 behaviour: a blocking model reviewer verdict changes the coder's `status` back to `waiting`; the coder executes again, the reviewer re-runs against that attempt, and later dependent specialists are skipped if review remains blocking.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cross-S1 feedback **changes the admissible subsequent work and causes actual repeat model execution** after a conflicting acceptance claim; scheduling/role labeling alone would not do this.
- Decisive decision or feedback right: select meaningful specialist dependencies through `createPlan`, and generate rejection/issue content through a separate reviewer model that forces rework; the executor's graph rules enforce admissible status transitions.
- Decision owner: first-party planning/reviewer model decisions under deterministic DAG/retry limits; protocol board operator independently chooses task ordering in the parent-controlled surface.
- Supporting / enforcement mechanisms: `routeTask`, `createPlan`, specialist result records, dependency graph, `applyReviewFeedback`, `propagateSkips`, capped reviewer retry and user-board single-writer queue outside swarm.
- Closure path: model decides worker graph → workers produce status/artifact → dependency/reviewer findings constrain next work → coder repairs or failed dependencies are skipped → refreshed result returns to execution state.
- Boundary reachability: the ordinary CLI may model-route to `runOrchestratedTask`; `--orchestrate` forces it; the installed `executePlan` actually invokes `runSpecialist` and `applyReviewFeedback`. The workflow is not hypothetical.
- Why this is / is not agent-owned: the plan model and independent reviewer choose task-specific dependency/feedback content; deterministic adjacency and retry counters cannot invent what to review or which business task follows.
- Evidence: [`src/orchestration/orchestrator.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/orchestrator.ts); [`src/orchestration/executor.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/executor.ts); [`tests/orchestration/executor.test.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/tests/orchestration/executor.test.ts).
- Basis: explicit + structural.
- Confidence: medium-high, limited to the DAG/review mode.
- Caveats: no general cross-file locking was found for all `spawn_task`/swarm workers. `swarm.ts` explicitly permits concurrent writers to collide, so **S2=A must not be interpreted as globally conflict-free multi-agent editing**.

## S3 — Inside-and-now control

- State: A(P)
- Function: choose and regulate the current set of task workers, dependencies and execution commitments in one active coding organization.
- Disturbance / variety regulated: task complexity needing division, specialist failure, blocked review, unready dependencies, selected agent capacity and current user need to redirect or terminate board runs.
- Whole-system current view: the modeled `ExecutionPlan` retains all specialist steps, dependency/status/result/retry metadata and a synthesis of the active cohort; the board UI/protocol projects actual task/swarm roster and status rather than unrelated GitHub activity.
- Current-control decision scope: routing/planning model chooses whether to decompose and which specialists/ordering to deploy; an ordinary lead `runAgentLoop` can sequentially choose further `spawn_task` delegations after returned child summaries. Authorized board operator selects present tasks/agents, manages order and stops active swarm tiles.
- Decisive decision or feedback right: allocate present tasks among workers and, after returned child/reviewer outcomes, continue, retry or terminate work; human parent can explicitly revise current board selection/stop conditions.
- Decision owner: model-backed lead/router/planner for active-task division and model-visible follow-up (`A`); human managing the current board session via protocol (`P`). Static executor/cap rules constrain but do not own high-level task meaning.
- Supporting / enforcement mechanisms: model `routeTask` and `createPlan`, `executePlan` and step report state, `spawn_task`, board-agent presets, protocol board start/stop/move and swarm per-agent status.
- Closure path: current user task/perception → planning model selects a worker graph and executes it → reported specialist outcome or reviewer block updates current team state and lead synthesis/follow-on model choice; in parent mode, live board state → human task/roster choice or stop → protocol changes current runs and broadcasts updated status.
- Boundary reachability: the standard CLI uses model routing before the solo path and supports explicit orchestration, while the shipped server protocol runs task/swarm agents and responds to task transitions. Current board run uses actual `runAgentLoop` rather than dummy labels.
- Why this is / is not agent-owned: the model selects task-specific division of labour; the operator makes discretionary choices for the active board rather than merely setting fixed startup flags. The host alone would only enforce queues and render status.
- Evidence: [`src/cli/index.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/cli/index.ts); [`src/orchestration/router.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/router.ts); [`src/orchestration/executor.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/executor.ts); [`src/protocol/handler.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/protocol/handler.ts).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: the model creates the specialist DAG up front; within its run, many transitions are deterministic and the plan is not continuously reauthored by a persistent executive model. Board human control is for the present task/roster; it does not authorize cross-workspace global governance.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead/router/planning model-backed actor | New complex task and returned subagent/reviewer evidence | Chooses model-worker decomposition and later follow-on child/tool decisions; `executePlan` records present statuses | `cli/index.ts`, `orchestration/router.ts`, `orchestrator.ts`, `agent/spawner.ts` |
| Parent (`P`) | Human board operator | Live task/swarm needs allocation, priority, stop or retry | First-party board/protocol changes active task and swarm state, aborts on tile leaving execution and broadcasts results | `protocol/handler.ts`, `agent/swarm.ts`, `board/store.ts` |

## S3* — Complementary audit

- State: A
- Function: independently challenge a coder model's implementation claim with read-only reviewer/model inspection and require bounded correction if the verdict blocks; optional host-side verification supplements this.
- Disturbance / variety regulated: implementer declares success despite missed requirements, incorrect code, under-tested changes or conflicting evidence; self-report alone is not sufficient in the orchestrated reviewer branch.
- Claim being audited: a completed coder specialist step and its artifact/result, distinct from the evaluator's later read-only review; the optional `--verify` wrapper separately tests ordinary loop claims against changed files/tests.
- Ordinary reporting path: coder `runAgentLoop` terminal summary, tool history, stored step `result` and `done` status.
- Complementary access path: reviewer is dispatched as its **own `runAgentLoop`** with `REVIEWER_SYSTEM_PROMPT`, a fresh task brief with dependency memory and enforced read-only permissions; it can inspect repository facts. The independent model's structured issues/`blocking` verdict, rather than coder prose, enters `parseReviewVerdict`. The `--verify` wrapper separately re-reads filesystem state and optionally re-runs configured tests.
- Independence boundary: separate run, reviewer role, read-only capability and independent verdict decision, but the configured provider can be the same vendor/model and the reviewer depends partly on coder-provided summaries. The host review parser treats unparseable output as nonblocking; a caller must include a reviewer step for this active path. These limits bound, but do not erase, model ownership of the **configured first-party review mode**.
- Who acts on findings: `executePlan.applyReviewFeedback` reopens dependent coder step and resets superseded memory, then executes a fresh review. Persistent blocking at the one-retry limit marks review failed and skips dependents.
- Decisive decision or feedback right: choose specific acceptance/rejection judgment from fresh read-only inspection after the implementer's claim, with authority to block or reopen the worker's current task through the reviewed plan.
- Decision owner: independently invoked model-backed reviewer specialist, with engine-owned parsing, dependency and retry guard; deterministic `--verify` is only supplemental constructor evidence, not the basis for agent-owned review judgment.
- Supporting / enforcement mechanisms: `runReviewer`, specialized prompt, read-only tool permissions, structured findings, `parseReviewVerdict`, capped `applyReviewFeedback`, `runWithVerification` file/test checks.
- Closure path: coder claims completion → separate reviewer examines task/code and emits structured verdict → blocking issue resets coder and reviewer → coder revises, reviewer checks again or failure prevents downstream promotion.
- Boundary reachability: `--orchestrate` invokes `executePlan`; `createPlan` supports a reviewer `PlanStep` with dependency edges and the executor dispatches `runReviewer` through a shipped first-party path. Offline tests cover one-retry, blocking and skip behavior. A normal solo/Archimedes task need not enter this optional reviewer path.
- Why this is / is not agent-owned: acceptance issues and blocking are substantively selected by a distinct reviewing model, whereas the host would otherwise only have fixed file/test checks; removing reviewer model choice leaves no equivalent semantic review verdict.
- Evidence: [`src/orchestration/specialists.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/specialists.ts); [`src/orchestration/executor.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/executor.ts); [`src/orchestration/specialist-prompts.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/orchestration/specialist-prompts.ts); [`tests/orchestration/executor.test.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/tests/orchestration/executor.test.ts).
- Basis: explicit + structural.
- Confidence: medium-high for wired optional audit, not for real-world detection effectiveness.
- Caveats: `parseReviewVerdict` intentionally treats unparsable results as nonblocking and explicit `blocking:false` as authoritative even if severity is critical; review cannot be claimed as fail-closed in all cases. User-selected reviewers/plan quality and same-model-provider self-critique can reduce substantive independence; no live LLM results measured.

## S4 — Outside-and-then intelligence

- State: C
- Function: adapt future inference-capacity selection to measured competence of the local model on similar past tasks and periodically retest its capability.
- Disturbance / variety regulated: local model capability differs by task pattern, untested or degraded model performance threatens correctness and spend, and fixed routing rules can keep competence estimates stale as local models evolve.
- External distinction: recorded attempts reflect actual user tasks, downstream independent-verifier judgments and availability of a separate local inference endpoint. These outcomes are environmental performance evidence beyond the internal current-token prediction.
- Future / prospective distinction: saved episodes are reloaded on subsequent tasks; their task-similarity success rates change whether **future tasks** attempt the local model or go straight to the large model. Epsilon probes revisit previously gated patterns to detect competence changes.
- Adaptation option generated: `assessCompetence` produces a future-task `useArchimedes` policy decision from similarity/threshold/minimum evidence, with a low-rate probe alternative; `resolveArchimedesConfig` also selects a currently available local backend/model.
- Path back into current capability / S3: the chosen branch of `ArchimedesAlternator.run` actually instantiates a local read-only agent or a large-model agent, independently verifies the local answer, escalates if invalid, records a durable Episode, and the next invocation reads those episodes to revise the policy.
- Decisive decision or feedback right: decide which model-capacity tier is trusted for a similar upcoming task and when to re-probe, then feed the observed success outcome back into future routing.
- Decision owner: first-party **deterministic** competence matcher/threshold/epsilon controller and explicit operator configuration; no autonomous model owns broader future organizational strategy or open-ended capability redesign. Thus a substantive adaptive constructor (`C`) rather than `A`.
- Supporting / enforcement mechanisms: episode store, task similarity and competence assessor, local endpoint probe, read-only local task loop, second verifier call, escalation to large model, cost log and epsilon re-probe.
- Closure path: real task → local attempt and separate verification → persisted success/failure episode → subsequent similar-task competence estimate → alternative model-tier decision and occasional probe → updated operating capacity/cost and new evidence.
- Boundary reachability: CLI and REPL explicitly compose `ArchimedesAlternator` when enabled and local model available; its actual `run` body loads and saves Episodes and applies routing decisions. It is an optional mode and is skipped in the `--verify` branch of the same CLI dispatch.
- Why this is / is not agent-owned: model outputs are used as solver/verifier signals, but the prospective **routing strategy** is a fixed code-defined threshold/epsilon decision, not an autonomous S4 agent inventing and promoting strategic alternatives.
- Evidence: [`src/cli/index.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/cli/index.ts); [`src/archimedes/alternator.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/archimedes/alternator.ts); [`src/archimedes/competence.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/archimedes/competence.ts); [`tests/archimedes/competence.test.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/tests/archimedes/competence.test.ts).
- Basis: explicit + structural.
- Confidence: medium-high for conditional wiring, lower for operational generalization beyond similar task strings.
- Caveats: this is **bounded future capacity routing**, not autonomously improved model weights, online fine-tuning, organizational scenario forecasting, or self-modifying production code. `--propose-harness` uses a hardcoded patch registry and the default apply path targets the Aura source checkout rather than an arbitrary installed user runtime; it is not evidence of a broader autonomous S4.

## S5 — Policy and identity

- State: —
- Function: no distinct installed ultimate-purpose/identity-policy decision loop returning a binding constitutional ruling to the same coding organization was established.
- Disturbance / variety regulated: conflicting tool permissions, provider trust, read-only reviewer limits, operator instruction and persistent persona preferences are operating constraints or context, not organizational existential policy questions.
- Decisive decision or feedback right: absent at the assessed recursion; users choose task, capability settings and desired board work, while developers supply fixed prompts/permission policy.
- Decision owner: no first-party S5 adjudicator; ordinary user/developer configurations or saved identity text are external inputs.
- Supporting / enforcement mechanisms: permission roles, `AGENT_PRESETS`, safety confirmations, managed access to board, project memory and persona/identity context.
- Closure path: requested action → configured permission/role check → operation admitted or blocked; no identity/purpose tension → legitimate final authority → returned governing-policy change is evidenced.
- Why this is / is not agent-owned: current-operation safety, model-rank trust, long-term memory and human ability to terminate a task do not by themselves instantiate an ultimate organizational policy function.
- Evidence: [`src/safety/permissions.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/safety/permissions.ts); [`src/board/agents.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/board/agents.ts); [`src/agent/unified-memory.ts`](https://github.com/DusanCar-sudo/aura-code/blob/6fa7733b34ead5458fbf865efe7e2769c57377c3/src/agent/unified-memory.ts).
- Basis: bounded structural absence review.
- Confidence: medium-high.
- Caveats: user's global moral/legal authority over their own computer is not a separately wired in-product identity-policy return process at the coding-session recursion.

### Absence scope

- Surfaces inspected: system prompt/role settings, tool permissions, project/user memory and identity blocks, CLI/provider choice, board management, model-verification and harness self-patch commands.
- Plausible first-party paths checked: human permission approval as constitutional authority, persistent identity note as S5 owner, model fallback as ultimate policy, source-code self-patching as deployed constitutional governance, and repository `AGENTS.md` as operating identity law.
- Why no material first-party path remains: these are task/infrastructure controls, source-development artifacts or descriptive memory. There is no closed separate purpose-dispute adjudication authority that changes the live organization's governing identity.

## Recursion

The active lead task is the focal system. Specialist model calls each execute their own `runAgentLoop` with their own task/result record and tool permissions, but their statuses and dependencies belong to one parent `ExecutionPlan`. `spawn_task` also starts a fresh child loop and returns the result to the caller. Board swarms instantiate distinct model loops, but do not gain a second complete S1–S5 metasystem or file-write exclusivity merely from parallel operation. Archimedes is a **separate configured routing mode** controlling inference capacity over repeated user tasks, not a new organization owned by local model alone.

## Variety and escalation

- Operations: model reacts to code/test/tools and can delegate or choose follow-on actions.
- Coordination: planned specialist dependency and reviewer-revision edges attenuate premature handoff and acceptance conflicts; independently launched swarm writers can still collide.
- Current control: model-mediated role/task DAG and later subagent delegation, plus separate human board control over present run/roster.
- Complement: the independent read-only model reviewer can cause a coder re-run or terminal blocked plan; deterministic opt-in `--verify` checks local effects independently but has limited coverage.
- Prospective adaptation: Archimedes episode success/failure changes model-capacity routing on future similar tasks; this is constructor ownership, not open-ended strategic AI autonomy.
- Escalation: permissions and user model configuration bound action; no in-runtime ultimate identity/policy escalation is demonstrated.

## Evidence gaps

- Source inspected at exact frozen SHA. Installed `npm ci --ignore-scripts --no-audit --no-fund` produced local dependencies. **278/278 targeted Vitest offline/mock tests PASS** (orchestration, reviewers, Archimedes, verification, board permission and swarm); `tsc --noEmit -p tsconfig.json` PASS. No live model or agent task was run.
- Initial offline Vitest invocation inside restricted sandbox failed 8 of 278 verification fixtures with `spawnSync /bin/sh EPERM`. The same 278 tests **all passed** on an appropriately permitted host retry; do not count the sandbox error as a source-code regression or pretend it never occurred.
- No claim of improved correctness from actual LLM reviewers or improved model cost is made. Tests establish executable wiring with mocked models, not output quality under real APIs.
- The default solo coding mode does not require a reviewer; `--verify` and Archimedes are separate opt-in CLI branches. The credit for S2/S3*/S4 is scoped to these reachable modes, not asserted to be active on every user request.
- In the first-party reviewer, malformed/non-JSON output is nonblocking, and self-reported `blocking:false` can override severity. A configured reviewer can still miss defects; the review loop is materially distinct but not uniformly fail-closed.
- Board swarm intentionally bypasses ordinary board single-writer serialization. Worktree file safety and universal subagent conflict coordination are not evidenced. `--analyze`/`--apply-harness` source-patch facilities require an Aura source checkout and do not establish installed-package self-evolution.
