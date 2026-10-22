---
harness_id: codeaf
project_name: CodeAF
repository: https://github.com/Agent-Field/CodeAF
review_ref: 9258f70523791330bf5128fd5aed6c70a70f138f
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: P
---

# CodeAF

## Review boundary

- System in focus: one installed CodeAF resident software-work factory, with conversational head, task-graph planner, executing leaves, ongoing resident/reconciler and local owner. The assessed recursion is the local multi-job installation, not Agent Field as a corporate or OSS organization.
- Purpose and identity: accept a person's work commitments, plan and execute separate bounded jobs, keep them coherent, return deliverables and learn reusable ways of working under standing user authority.
- Relevant environment: changing project files and requirements, independently running task leaves, incompatible input dependencies, model/tool failures, cost and time ceilings, delivered defects, accumulated task outcomes and user corrections.
- Standard-distribution boundary: supported `codeaf chat`, `codeaf do`/headless execution, task graph and resident scheduler, persistent stores, TUI/home, standing/wake lifecycle, model and tool adapters, craft repository and notebook.
- Credited operating / distribution surfaces: `cmd/codeaf/{chat,resident_build,wake}.go`, `internal/{head,resident,plan,exec,session,standing,store,craft,subharness}/`, task/head/worker lifecycle and `docs/AMBIENT.md` where verified against implementation.
- Adjacent first-party surfaces excluded from ownership: repository development, `bench/` experiments and scores, engineering tests and CI/release activities, unfinished design waves in `docs/`, author/maintainer organization and the external Agent Field SDK. They do not supply local organizational decisions.
- First-party operating / deployment modes considered: interactive resident chat/TUI with board and status, multi-node plan and model-led execution, headless one-shot work, ratified background standing watches, optionally budget-armed unattended Steward session, optional practice budget and persistent craft shelf. Do not read a roadmap example as a witnessed integration.
- Recursion level: resident installation with distinct planned worker leaves as S1 units; model head/current job portfolio at S3; local person is a legitimate parent for ratification and direct current control.
- Reviewed revision: [`Agent-Field/CodeAF@9258f70523791330bf5128fd5aed6c70a70f138f`](https://github.com/Agent-Field/CodeAF/tree/9258f70523791330bf5128fd5aed6c70a70f138f), frozen by [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-23; primary source/config/doc and deterministic test-code inspection only. No LLM agent, provider or benchmark was executed.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The model-backed `head` reads the resident's cross-job board, current conversation and durable store, selects belt tools (`recall`, `open`, `status`, `task`, `stop`, `ask`), and can commission or redirect work. A separately model-backed compiler interprets the person's request, and the planner constructs a dependency graph of bounded worker leaves. Binding and counter-audit passes reason about missing inter-leaf dependencies before those workers receive the inputs from predecessors. The `resident.Reconciler` turns durable commands into executable subtrees, advances work, handles overruns and cancellations, and reports outcomes. Work completion flows through acceptance/delivery gates. `docs/SUBHARNESS.md` describes opt-in typed graph workflows; subharness nesting is not automatically a new VSM recursion or a management owner.

The runtime stores settled outcomes, lessons and scoped notebook facts. Its model-backed distiller and cross-job reflector can produce memories, and a craft writer can produce validated, versioned reusable workflows; new worker leaves receive `NotebookDigest` as an input and subsequent tasks can select already forged craft. A separate self-practice path is budget-configurable and disabled in one-shot mode. The repository's own [`docs/LEARNING.md`](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/docs/LEARNING.md) candidly records several *incomplete* learning circuits (including planner anchor reuse, evidence preservation and some retrospective/router paths); they are not treated as closed evidence.

Persistent ambient actions require an explicit ratification card. Once ratified, the standing store and wake/tick process can perform bounded checks and run child tasks under already approved permissions; if an action exceeds standing consent, it stops for the person's decision. An attended operator can also inspect the current board and intervene. A budget-armed `Steward` offers an unattended principal for certain current acceptance/continuation paths, without thereby creating autonomous S5 authority.

Primary sources: [head turn loop](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/loop.go), [task commission](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/task.go), [planner dependency bind](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/bind.go), [resident lifecycle](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/resident.go), [runtime assembly](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/cmd/codeaf/resident_build.go).

## Operational model

The ordinary S1 unit is an independently runnable planned leaf with a scoped brief, tool feedback, output and acceptance/repair route. Multiple workers are not credited as an organization merely because they run concurrently; here additional model-led dependency binding, graph correction, job commissioning and resident re-intervention create distinct S2/S3 decision paths. The model's discretionary decisions are distinct from fixed DAG constraints, budgets, locks, refusal and schema validation. Durable user ratification is distinct from agent-generated recommendations; self-reported outcome success has not been independently benchmarked in this review.

## S1 — Operations

- State: A
- Function: perform and revise scoped user-requested repository/research/tool jobs with model-chosen actions and checked deliveries.
- Disturbance / variety regulated: ambiguous objectives, unexpected repository contents, tool failures, incomplete intermediate outputs and acceptance failures.
- Decisive decision or feedback right: executing leaf model chooses investigative/tool steps and revised output from its brief and live observations, rather than merely applying a predetermined script.
- Decision owner: model-backed worker executing an admitted task leaf, subject to consent, budget and contract gates.
- Supporting / enforcement mechanisms: `exec` runner, model/tool adapters, individual work contracts, isolated workspaces, retries and delivery checks.
- Closure path: admitted task brief → model action/tool observation → output and receipt → test/contract judgment → repair/replan or delivered result returned to dependent workers and the person.
- Boundary reachability: the standard `chat` graph-runner and `do` path wire planner output into ordinary executing task leaves; this is not a benchmark-only path.
- Why this is / is not agent-owned: task action/content is selected by the worker model; guards limit its reachable effects without replacing that choice.
- Evidence: [runtime chat execution](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/cmd/codeaf/chat.go), [plan builder](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/plan.go), [resident runner](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/runner.go).
- Basis: source-grounded standard runtime action-and-feedback loop.
- Confidence: high for shipped decision wiring, not for empirical agent success.
- Caveats: external model and tool availability was not exercised; `bench/` metrics are not production ownership evidence.

## S2 — Coordination

- State: A
- Function: dynamically attenuate incompatible or insufficient inputs between distinct S1 leaves of a shared deliverable, and return the repaired dependency relations to execution.
- Disturbance / variety regulated: one worker starting without decisions/results from another, duplicate leaves, overly serial dependencies and inconsistent plans under shared deliverable constraints.
- Decisive decision or feedback right: the model-led bind pass judges which upstream outputs each later-stage leaf must await and which duplicate leaf can be folded; a counter-audit can find material missing edges and add them.
- Decision owner: model-driven plan binding and counter-audit stages, with deterministic graph validation/enforcement.
- Supporting / enforcement mechanisms: `Graph.Needs`, staged fanout, topological stages, `Bind`, `auditWith`, `AddNeed`, `Retarget`, graph error checks.
- Closure path: complete proposed graph → bind model evaluates inter-worker requirements → dependencies materialize → audit model flags missing required inputs → graph adds permissible edges → later leaf sees required predecessor results before acting.
- Boundary reachability: both bind and audit are ordinary first-party `internal/plan` build components, rather than invented orchestration instructions; validated edges are consumed by the graph runner.
- Why this is / is not agent-owned: deciding that a *particular* other leaf's answer is required is a contextual model judgment; the DAG and lock code enforce rather than originate that decision.
- Distinct S1 units: separate work leaves in a planned multi-stage task graph, potentially executed in parallel within stages.
- Inter-S1 disturbance: a downstream implementer missing an earlier design/selection/result; redundant workers or unnecessary serial constraints reducing useful concurrency.
- Attenuating coordination relation: model-chosen predecessor edge and duplicate-node fold within one graph, strengthened by opposing finishability audit.
- Feedback into subsequent S1 behaviour: changed graph `Needs` determines which upstream outputs appear in an individual leaf's input and when it may start.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the model evaluates dependencies *between independently executable units* and alters their information/execution relation; static task fanout alone would not earn this state.
- Evidence: [binding passes](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/bind.go#L122-L225), [adversarial dependency audit](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/audit.go#L10-L149), [graph dependency execution](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/graph.go).
- Basis: agent-owned contextual inter-S1 dependency regulation with an enforced operational return.
- Confidence: moderate-high for the bounded graph coordination function.
- Caveats: not evidence of a general independent cross-project resource governor or empirical conflict-free execution; this is one shared deliverable's graph.

## S3 — Inside-and-now control

- State: A(P)
- Function: observe the local installation's live commitments, commission/cancel/adjust work and return current control decisions into its executing portfolio.
- Disturbance / variety regulated: competing requests, changed priorities or user corrections, stuck jobs, inadequate scope, interrupted attempts and unseen accumulated commitments.
- Decisive decision or feedback right: the agentic head judges when a user utterance requires a new task, a current-job intervention or just an answer, using portfolio-aware reads and actionable tools; in the separate operator mode the person can inspect the same work and direct changes.
- Decision owner: model-driven `head` in base mode (`A`); legitimate local human owner directs the portfolio in attended control mode (`P`).
- Supporting / enforcement mechanisms: board/lens/status and toolbelt, durable command journal, reconciler, cancel/replan, bounded tool calls and consent rules.
- Closure path: head/owner views live portfolio → selects commission, stop, revision or continuation → journaled command → resident materializes new graph/changes existing work → board and outcomes update for later control.
- Boundary reachability: `Head.runTurn`, `task`, `stop`, `status` and `Reconciler.Tick` form the standard resident chat path; the attended owner uses the same session/board commands, not an external maintainer issue queue.
- Why this is / is not agent-owned: tool selection and whether to initiate or redirect a work commitment are model decisions, not automatic queue ticks; user-directed parallel control remains a separate first-party human-owner mode.
- Whole-system current view: head's `status()` and rendered board unify active jobs, progress, approvals, standing work and outcomes for this installed resident; operator home/TUI exposes the portfolio.
- Current-control decision scope: issue a new commitment, withdraw/amend ongoing work or choose next intervention within delegated user instruction and budget. A fixed scheduler cap or time limit alone is not the S3 evidence.
- Evidence: [head tool-loop and board](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/loop.go), [commission](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/task.go), [portfolio lens](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/lens.go), [resident application](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/resident.go#L625-L754).
- Basis: model-chosen whole-resident current control and separate human-override path, both returning commands through the same execution journal.
- Confidence: moderate; scoped to this installation rather than company-wide portfolio strategy.
- Caveats: model cannot use automatic consent for non-delegated consequential actions; autonomy is bounded by current user authorization.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | model-backed conversational head | live board changes, new request, settled job or intervention cue | choose `task`/`stop`/follow-up and journal it; resident changes current work | `internal/head/{loop,task,lens}.go`; `internal/resident/resident.go` |
| Parent (`P`) | human installed-instance owner | attended TUI/board observation or correction | directly steer/withdraw/redefine a commitment; same store/worker graph changes | `cmd/codeaf/chat.go`; `internal/head/toolbelt.go`; `internal/resident/resident.go` |

## S3* — Complementary audit

- State: —
- Function: independently verify the S3 owner's current management decisions/claims and return management-level corrective findings through a separate access path.
- Disturbance / variety regulated: potentially incorrect board-level allocation, intervention and accountability claims; no distinct operational S3* owner found.
- Decisive decision or feedback right: none established for a separate S3-management auditor.
- Decision owner: the `plan/audit.go` model audits *inter-task finishability/dependency relations* during plan construction; delivery gates audit artifacts, not the head's portfolio-control judgment.
- Supporting / enforcement mechanisms: task gate, graph dependency counter-audit, status visibility and tests.
- Closure path: not applicable at the claimed management-audit level; S2 graph audit can correct `Needs` but does not independently audit S3 decisions.
- Why this is / is not agent-owned: an opposing model prompt is not sufficient if its claim, access and returned finding are about ordinary plan completeness rather than management control.
- Evidence: [dependency audit's stated scope](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/plan/audit.go), [head status path](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/head/lens.go), [resident reconciliation](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/resident.go).
- Basis: bounded negative at local-portfolio recursion after searching plausibly independent plan audit, artifact gate, status and model-head surfaces.
- Confidence: medium-high for this source-visible boundary.
- Caveats: a different recursion could separately analyze plan quality reviews; this cannot be silently promoted to a whole-organization S3*.

### Absence scope

- Surfaces inspected: `internal/head`, `internal/plan/audit.go`, `internal/resident`, task verification and session/status routes.
- Plausible first-party paths checked: opposing plan-dependency model, independent task acceptance checks, status/history readout, headless Steward's terminal audit and tests.
- Why no material first-party path remains: each checks leaf deliverability or graph correctness, or presents ordinary S3 data to its own decision maker; none has distinct S3-claim access and corrective management-decision return.

## S4 — Outside-and-then intelligence

- State: A
- Function: learn context-specific lessons and reusable work patterns from earlier environmental outcomes, then change how later task units act.
- Disturbance / variety regulated: recurring external tool/domain surprises, repeated failed approaches, changed recurring preferences and avoidable recreation of earlier work methods.
- Decisive decision or feedback right: model-driven distillation/reflection judges what a completed job or a series taught; it selects scoped facts/craft proposals for storage or refinement. Optional self-practice selects execution-verifiable gaps under budget/idle rails.
- Decision owner: the resident's configured distiller/reflector model for prospective content and choice, constrained by content validation and scope; deterministic guards admit/store but do not write the strategic lesson.
- Supporting / enforcement mechanisms: persisted scoped notebook and recall, `NotebookDigest`, craft candidate parse/repair/git versioning, retrospective cadence and optional practice metrics.
- Closure path: independent job outcomes/corrections → distillation/reflection judgments → recorded notebook fact or validated forged craft → later leaf retrieves scoped notebook input or craft-recognition path → subsequent execution receives changed instructions/workflow.
- Boundary reachability: `newResidentReconciler` wires model distiller/reflector in normal resident mode, and `chat.go` wires `leafNotebookInputs` into ordinary worker inputs; durable chat mode wires `CraftMind` and shelf. One-shot practice is deliberately disabled, so practice is not the decisive S4 evidence.
- Why this is / is not agent-owned: the model judges *which reusable adaptation* to preserve from external outcomes, distinct from a deterministic harvest threshold; the downstream worker consumes it on a later independently scoped task.
- External distinction: task results, faults, user corrections, verified failed approaches and changed project conditions supply feedback that earlier model prompts alone could not know.
- Future / prospective distinction: lessons and workflows are persisted for future tasks, not merely a repair instruction for the same failing leaf.
- Adaptation option generated: scoped operational lesson, reusable preference, replacement belief or executable craft/workflow candidate.
- Path back into current capability / S3: notebook retrieval becomes a future worker input; task/charter recognition may activate versioned craft on a subsequent work request.
- Evidence: [runtime model assembly](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/cmd/codeaf/resident_build.go#L69-L78), [resident learning tick](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/resident.go#L705-L749), [future leaf notebook injection](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/cmd/codeaf/chat.go#L2216-L2241), [model craft forge](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/craftforge.go), [craft reuse](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/craftmind.go), [retrospective](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/resident/retrospect.go).
- Basis: a bounded autonomous model-led prospective learning decision and future worker-input closure; not a claim that *all* designed learning loops work.
- Confidence: moderate; structural S4 exists, measured improvement and several secondary feedback paths remain unresolved.
- Caveats: [`docs/LEARNING.md`](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/docs/LEARNING.md#L16-L69) identifies incomplete recall/evidence/router/calibration circuits. No live agent trials were run, and adaptive improvement magnitude is not established.

## S5 — Policy and identity

- State: P
- Function: determine the standing scope and ultimate limits of what this local installed assistant may do, especially persistent unattended work and consequential tool permissions.
- Disturbance / variety regulated: changing user purpose, implicit versus explicit authorization, future requests to widen standing access and risk of unratified autonomous work.
- Decisive decision or feedback right: the legitimate person explicitly ratifies each standing item and retains power to withdraw, change or bound its budget/permissions; model suggestions are not authoritative creation of standing policy.
- Decision owner: local user as parent (`P`), not the CodeAF model or OSS maintainer organization.
- Supporting / enforcement mechanisms: standing proposal and approval card, persisted immutable-like rails, permission/consent desk, wake/timer checks, explicit `needs your look` refusal.
- Closure path: user judges proposed standing purpose/limits → ratifies bounded watch/rule → standing store persists authorized item → timer/runner evaluates and executes future firings under those rails → out-of-scope action returns to human instead of self-widening authorization.
- Boundary reachability: standard ambient mode uses `internal/session` ratification and `internal/standing` storage; `cmd/codeaf/wake.go` and interactive `chat` attach the same persistent resident. This is within the installed product, not documentation-only contributor governance.
- Why this is / is not agent-owned: the model can propose standing purposes, but the authority to install or expand enduring permissions is reserved to the human user.
- Evidence: [standing store contract](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/standing/standing.go#L25-L48), [ambient built-path documentation](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/docs/AMBIENT.md#L1-L20), [standing wake assembly](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/cmd/codeaf/wake.go), [user/session authority](https://github.com/Agent-Field/CodeAF/blob/9258f70523791330bf5128fd5aed6c70a70f138f/internal/session/).
- Identity / ultimate-policy issue: what enduring purposes, tool rights, spending rails and unattended authority the resident may have on the person's machine.
- Ultimate authority in each claimed mode: installed human owner (`P`); no competing first-party autonomous S5 constitution is established.
- Return-to-operation path: ratified standing policy in store is consulted by next wake/action; beyond-rail behavior is blocked/presented for a fresh person decision.
- Basis: supported positive local parent-authority loop with persistence and enforcement.
- Confidence: high for structural ratification/return, without asserting policy compliance under all tool inputs.
- Caveats: a user-owned charter is not the same as organization-wide governance of the CodeAF open-source project.

## Distributed OSS parent arrangement

Local installations have distinct parent users. OSS maintainers and external Agent Field contributors affect the released code, but no shared decision-and-feedback loop over all user installations was established. `P` belongs to the local installed-resident recursion, not the distributed upstream project's ultimate authority.

## Self-hosted and non-human modes

The supported unattended budget-armed Steward can make certain continuation/terminal-acceptance decisions after a user delegates bounded time/cost, and a standing item can fire after prior ratification. Neither silently transfers authority to create new standing policies. One-shot `codeaf do` turns self-practice off and may not expose the same learning/lens history as a durable resident.

## Recursion

Individual tool-using leaves provide S1 operations; a planned multi-leaf graph and its model-led dependency decisions provide bounded S2; the head/resident project-portfolio owner is S3; notebook/craft adaptation spans episodes in S4; the local person establishes final recurring authority in S5. No complementary independent auditor of S3 control was identified. These levels are not inferred from the number of provider calls, subharness graph nodes, or model names.

## Variety and escalation

Tool errors and acceptance failures return to leaf repair and sometimes replanning; failed graph or cost bounds stop or ask; owner corrections cause new commands/current-control changes. Retrospective and craft learning return observations from previous unrelated outcomes into later operations. Unratified standing changes and consequential external actions reach the human parent; fixed budget/refusal is a safety enforcer, not autonomous management judgment.

## Evidence gaps

- This is frozen-source classification only; no model run, external account, live agent, benchmark or actual performance claim was tested.
- The shipped model-dependency audit is distinct from an independent audit of S3 portfolio decision making; no S3* owner is established.
- Documented open learning circuits (particularly calibrated planning reuse and some retrospective/recall evidence links) limit S4 claims to closed notebook/craft paths; source evidence alone cannot quantify improvement.
- Model role independence between binding and its opposing audit is prompt/phase-based, not proven provider isolation or external assurance; S2 does not require a separate S3* organization at this boundary.
