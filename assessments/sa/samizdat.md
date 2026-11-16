---
harness_id: samizdat
project_name: Samizdat
repository: https://github.com/samizdat-code/samizdat
review_ref: 6202b4fc4ce7b6d67025ef321b49d86d178f15a0
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: A
---

# Samizdat

## Review boundary

- System in focus: The shipped Samizdat server, agent workflow and built-in supervisor and workers at one project in a deployed live image.
- Purpose and identity: Implement and verify coding tasks while retaining locally governed changes to the harness itself.
- Relevant environment: A Clojure project, model providers and tools, plus a legitimate project operator at the local control surface.
- Standard-distribution boundary: Packaged server/TUI, durable project state, shipped role/loop configuration, and project-local userspace overrides.
- Credited operating / distribution surfaces: Live Jolt/EDN workflow, worker/task ledger, runtime critic, supervisor, human controls and versioned userspace.
- Adjacent first-party surfaces excluded from ownership: Repository release and contributor controls, optional separate GUI repository, development benches and offline experiments.
- First-party operating / deployment modes considered: Ordinary model-backed runs, supervised team runs, human control API and project-local policy/adaptation modes where configured.
- Recursion level: One project delivery organization with separate coding branches as S1 units and one live run at a time for claimed portfolio control.
- Reviewed revision: `6202b4fc4ce7b6d67025ef321b49d86d178f15a0`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A durable journal and store hold runs, task claims, events and outcomes. EDN workflows drive model turns and effects in isolated branch histories. The supervisor sees operating evidence, can submit typed intervention requests, and owns supported changes to project-local cells, prompts and policy. The critic reads Git evidence at completion. Project userspace versions accepted changes and permits rollback. [`README.md`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/README.md#L5-L54), [`src/samizdat/workflow.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/workflow.clj#L287-L385), [`resources/roles.edn`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/roles.edn#L45-L110), [`src/samizdat/store/interventions.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/store/interventions.clj#L17-L40), [`docs/RFCS/RFC-010-adaptation.md`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/docs/RFCS/RFC-010-adaptation.md).

## Operational model

Worker branches produce verified project changes. Claims make tasks exclusive, and supervisors or operators can revise live branch commitments. The packaged critic has a separate model call and can return a finding to the implementer. The operator owns overall deployment and credentials, whereas the supervisor can decide project-local userspace changes.

## S1 — Operations

- State: A
- Function: Produce a project change or answer from a coding task.
- Disturbance / variety regulated: Changing code state, task constraints, evidence and tool failures require discretionary action.
- Decisive decision or feedback right: Select edits and tools, use results to revise work and decide when to submit.
- Decision owner: The model-backed coding branch.
- Supporting / enforcement mechanisms: Compiled workflow, scoped tools, workspace, durable journal and ship gates.
- Closure path: Tool outcomes are returned to the worker and affect its subsequent actions; candidate completion enters the checking workflow.
- Why this is / is not agent-owned: Without the worker model, the state machine and tools cannot choose an implementation.
- Evidence: [`src/samizdat/workflow.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/workflow.clj#L287-L385), [`src/samizdat/agent/loop.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/loop.clj#L669-L725), [`src/samizdat/agent/loop.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/loop.clj#L1219-L1310), [`resources/roles.edn`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/roles.edn#L45-L77).
- Basis: structural
- Confidence: High
- Caveats: Production provider behavior was not exercised.
- Boundary reachability: The server launches the shipped workflow and model-backed project branch roles.

## S2 — Coordination

- State: C
- Function: Prevent two coding branches from making competing commitments to the same task.
- Disturbance / variety regulated: Two branches can observe one task as open before either commits to doing it.
- Decisive decision or feedback right: Admit or reject task claims against an atomic owner check, and inform the losing branch of the actual holder.
- Decision owner: The packaged task-claim policy determines the conflict outcome; the worker agents choose which eligible task to attempt next.
- Supporting / enforcement mechanisms: Task board state, guarded row transition, claim/release tools and the live task view.
- Closure path: The losing claimant receives a refusal and holder information; a successful claim becomes a pinned work statement and changes worker activity.
- Why this is / is not agent-owned: The first-writer rule assigns the winning owner independently of a model's judgment about the conflict.
- Evidence: [`src/samizdat/store/tasks.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/store/tasks.clj#L180-L215), [`src/samizdat/agent/tools/tasks.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/tasks.clj#L26-L42), [`src/samizdat/agent/tools/tasks.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/tasks.clj#L223-L266).
- Basis: structural
- Confidence: High
- Caveats: This claim covers duplicate task commitments, without asserting that all overlapping file edits are resolved.
- Boundary reachability: Agent roles expose the packaged task tool, which calls the guarded task store.
- Distinct S1 units: Separate coding branches with their own work commitments and model context.
- Inter-S1 disturbance: Concurrent claims over one task can duplicate implementation effort.
- Attenuating coordination relation: A persisted ownership rule admits one claimant and exposes the winner to others.
- Feedback into subsequent S1 behaviour: Task refusal directs the losing agent to another claim, while the winner receives its pinned task instructions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The conflict detection is keyed to an actual task reservation and governs subsequent behavior of competing actors.

## S3 — Inside-and-now control

- State: A(P)
- Function: Revise current commitments across branches of a live run.
- Disturbance / variety regulated: Work can stall, exceed a budget, need redirection or remain in the wrong branch.
- Decisive decision or feedback right: Choose which branch to redirect, cull or extend in response to current progress.
- Decision owner: The model-backed supervisor or, in the distinct direct-control path, the project operator.
- Supporting / enforcement mechanisms: Run views and session observations, typed interventions, queued disposition and branch/beam boundaries.
- Closure path: A supervisor or human directive reaches the branch/beam drain, affects work and records its outcome for later observation.
- Why this is / is not agent-owned: The common queue applies a decision from an identified actor; it does not choose a discretionary intervention.
- Evidence: [`resources/roles.edn`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/roles.edn#L82-L106), [`src/samizdat/agent/tools/intervene.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/intervene.clj#L93-L172), [`src/samizdat/api/control.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/api/control.clj#L456-L515), [`src/samizdat/store/interventions.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/store/interventions.clj#L17-L46), [`src/samizdat/agent/loop.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/loop.clj#L1443-L1532).
- Basis: structural
- Confidence: High
- Caveats: Current-control scope is the run, with changes applied between turns.
- Boundary reachability: The packaged supervisor has intervene, and the server exposes a human control API backed by the same queue.
- Whole-system current view: The supervisor and local operator can inspect branch and run progress and directive dispositions across the current run.
- Current-control decision scope: Direct which current branch work to continue, redirect or curtail within a configured run.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed supervisor | Observed lack of progress or changed work need | Submitted directive is applied at a branch or beam boundary and produces a recorded disposition | [`src/samizdat/agent/tools/intervene.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/intervene.clj#L93-L172) |
| Parent (`P`) | Operator responsible for the project deployment | Operator observes current progress and selects an intervention | Human-issued typed directive applies at the same runtime boundary and changes subsequent work | [`src/samizdat/api/control.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/api/control.clj#L456-L515) |

## S3* — Complementary audit

- State: A
- Function: Independently challenge a worker's claim that a change is complete.
- Disturbance / variety regulated: A final answer may assert completion despite deficiencies in the diff or evidence.
- Decisive decision or feedback right: Issue a complementary finding on the design intent, change and run evidence.
- Decision owner: A separate critic model call, with optional multiple samples under the shipped policy.
- Supporting / enforcement mechanisms: Git-derived review diff, journal, structured prompt, attempt count and revise transitions.
- Closure path: A blocking finding sends the branch back with corrective evidence, and a subsequent attempt is evaluated anew.
- Why this is / is not agent-owned: The critic independently decides substantive adequacy from primary evidence. The gate only enforces the result.
- Evidence: [`resources/cells/critic.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/cells/critic.clj#L69-L139), [`src/samizdat/agent/judge.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/judge.clj#L488-L520), [`src/samizdat/agent/judge.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/judge.clj#L547-L583).
- Basis: structural
- Confidence: High
- Caveats: Attempt caps and fallback behavior mean that the auditor's authority is bounded.
- Boundary reachability: The completion critic is a shipped workflow cell; its revise branch returns to the running worker.
- Claim being audited: The worker's proposed change satisfies the original task and is ready to ship.
- Ordinary reporting path: Worker completion message and recorded test/tool activity.
- Complementary access path: A separately composed critic call receives the actual Git diff and task requirements.
- Independence boundary: The critic evaluates separate input and call context from the worker. A configured provider may be shared.
- Who acts on findings: The workflow returns the blocking evidence to the worker for correction.

## S4 — Outside-and-then intelligence

- State: A
- Function: Adapt future project capability using observed provider and tool-environment outcomes.
- Disturbance / variety regulated: Provider reliability, tool usefulness and project demands vary across runs.
- Decisive decision or feedback right: Select an experiment in reusable project userspace, judge the outcomes and keep or revert the capability.
- Decision owner: The model-backed supervisor operating the adaptation tools.
- Supporting / enforcement mechanisms: Session telemetry, versioned userspace, bounded probes and retained experiments/knowledge.
- Closure path: Accepted capabilities affect later loop compilation or tool use, while durable outcome records inform later runs.
- Why this is / is not agent-owned: The model chooses the option and can act on observed results. Scoring, reload, acceptance checks and rollback constrain effects.
- Evidence: [`docs/RFCS/RFC-010-adaptation.md`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/docs/RFCS/RFC-010-adaptation.md), [`resources/roles.edn`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/roles.edn#L82-L109), [`src/samizdat/agent/tools/adopt.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/adopt.clj#L45-L102), [`src/samizdat/mutation.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/mutation.clj#L345-L430), [`src/samizdat/workflow.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/workflow.clj#L175-L215).
- Basis: structural
- Confidence: High
- Caveats: This claim is bounded to deployable project userspace and excludes upstream project release policy. Comparative live performance was not tested.
- Boundary reachability: The shipped supervisor sees cross-run signals and has experiment/adopt and edit surfaces for its project userspace.
- External distinction: Provider trouble, tool outcome and project-environment observations are available through the live feedback seams.
- Future / prospective distinction: The supervisor can choose a reusable capability or threshold to compare across subsequent runs and retain its outcome.
- Adaptation option generated: Versioned changes to a cell, manifest, prompt or threshold, including offered capabilities.
- Path back into current capability / S3: Kept and adopted userspace changes are reloaded by the workflow and can alter subsequent operational execution.

## S5 — Policy and identity

- State: A
- Function: Set standing project-local policy for what future workflow outcomes qualify and what the project agent roles may do.
- Disturbance / variety regulated: Changing project aims and failure modes can require new completion, review or role policy.
- Decisive decision or feedback right: Decide and commit a versioned policy-table change inside the project boundary.
- Decision owner: The explicitly empowered model-backed supervisor.
- Supporting / enforcement mechanisms: Named runtime policy tables, userspace versioning, reload/validation, journaled changes and rollback.
- Closure path: A saved valid table is reloaded and governs later gates or role behavior. A failed reload rolls it back.
- Why this is / is not agent-owned: The model chooses the durable policy content. Validators enforce immovable deployment and kernel constraints.
- Evidence: [`resources/roles.edn`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/resources/roles.edn#L82-L106), [`src/samizdat/agent/tools/policy.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/agent/tools/policy.clj#L268-L413), [`src/samizdat/userspace.clj`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/src/samizdat/userspace.clj#L1230-L1293), [`README.md`](https://github.com/samizdat-code/samizdat/blob/6202b4fc4ce7b6d67025ef321b49d86d178f15a0/README.md#L5-L24).
- Basis: structural
- Confidence: High
- Caveats: This does not credit authority over the immutable kernel or third-party deployment rules. A run-scoped human grant is narrower than the claimed durable policy scope.
- Boundary reachability: The supervisor's packaged policy tool writes the project-local versioned tables in its authorized deployment.
- Identity / ultimate-policy issue: Which project-specific conditions and actor authorities bind later operating runs.
- Ultimate authority in each claimed mode: The supervisor decides applicable project userspace policy within an immutable outer deployment envelope.
- Return-to-operation path: Checked, persisted tables reload and are read by later live gates and roles.

## Recursion

Individual workers own task execution. The project supervisor and deployment operator act across running branches. Project-local adaptive capabilities and standing policy belong to the project recursion.

## Variety and escalation

Tool feedback and run journaling let workers handle project variation. Exclusive claims, supervisory directives and the complementary critic regulate interference and quality. Project-local policy changes remain inside validation and outer constraints.

## Evidence gaps

Source and test code reviewed without running the Jolt service or live model roles. The held-out battery is conditional and its results are not used as observed evidence.
