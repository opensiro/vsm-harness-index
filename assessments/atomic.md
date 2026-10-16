---
harness_id: atomic
project_name: Atomic
repository: https://github.com/bastani-inc/atomic
review_ref: d6bc44cf753bd2748ffac6dd994205a170216741
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
autonomy_s4: —
autonomy_s5: —
---

# Atomic

## Review boundary

- System in focus: installed Atomic TypeScript coding-agent CLI with its shipped workflow/subagent/intercom extensions and configurable durable multi-stage runs, at frozen `d6bc44cf753bd2748ffac6dd994205a170216741`. This is not bastani-inc's organization, externally managed model inference, or a hypothetical user-written workflow.
- Purpose and identity: execute engineering tasks through model-directed coding stages, optionally with first-party parallel child agents, durable workflow supervision and reviewer-evidence/repair closure.
- Relevant environment: a repository/worktree, model service, tools and filesystem, Git state, executor/container, user objectives, acceptance criteria, development/tests and verification evidence.
- Standard-distribution boundary: published `@bastani/atomic` coding-agent CLI and first-party bundled `@bastani/workflows`, `@bastani/subagents`, intercom, package-native file/shell/tools, `ralph` and `adversarial-verification` builtins. Standalone imported upstream Pi SDK core and third-party model endpoints are infrastructure dependencies; the whole packaged Atomic model-to-tool session and bundled extensions are the credited first-party harness, not upstream Pi as a separate assessed product.
- Credited operating / distribution surfaces: `AgentSession.prompt` and packaged tool execution; built-in parallel subagent executor and optional Git worktree setup; shipped `ralph` multi-stage workflow with dedicated fresh reviewer agents, finding gates and bounded corrective return; actual slash/tool workflow observation, pause/resume/abort/steering by an operator. The optional worktree and ralph workflow are explicitly mode-scoped.
- Adjacent first-party surfaces excluded from ownership: release CI, benchmark/case-study claims, repository development process, contributors, external hosted verification and default downloaded skills. No evidence that every default coding turn automatically follows the ralph review workflow.
- First-party operating / deployment modes considered: native CLI agent coding session (delegates generic agent loop to packaged pi-agent-core dependency); separately available bundled subagent parallel mode with `worktree` option; installed `ralph` workflow (reviewer A/B and repair); workflow dashboard/control actions through first-party command/tool surfaces. No live provider-backed coding run or independent outcome witness was performed.
- Recursion level: one Atomic-managed coding work system with separate model-driven operational coding and verifying workers inside a bounded optional workflow, under parent user control. Do not raise the system boundary to maintainers or reclassify scripted workflow stages as strategic organizational adaptation.
- Reviewed revision: `d6bc44cf753bd2748ffac6dd994205a170216741` (Index #379), immutable.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The repository documents Atomic as a packaged fork of the pi coding CLI with independently bundled workflow/subagent packages: `packages/coding-agent` ships the CLI and session and file/shell tool interface, while `packages/workflows` and `packages/subagents` ship as first-party extensions copied into the published package ([AGENTS.md](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/AGENTS.md), [packages/coding-agent/package.json](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/package.json)). `packages/coding-agent/src/core/agent-session-prompt.ts` dispatches model-directed prompt/continuation to the installed `pi-agent-core` engine; `AgentSession` owns the surrounding tools, input context, policy hooks and session state. Consequently Atomic has a reachable first-party supported coding-agent product with a model/tool feedback cycle, but generic Pi-core internals are not attributed to novel Atomic-specific algorithms.

The first-party subagent executor has supported parallel task execution with an explicit `worktree` option. The executor calls `createParallelWorktreeSetup` and `createWorktrees` to give sibling S1 coding tasks separate Git worktrees rather than the same mutable checkout. It also rejects duplicate configured publication output paths and incompatible child cwd, and returns independent task outcomes and patch artifacts ([packages/subagents/src/runs/foreground/subagent-executor-parallel.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/foreground/subagent-executor-parallel.ts), [packages/subagents/src/runs/foreground/subagent-executor-worktree.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/foreground/subagent-executor-worktree.ts), [packages/subagents/src/runs/shared/worktree.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/shared/worktree.ts)). This actually attenuates a concrete shared-checkout write interference when enabled; it is constructor-mediated isolation, not evidence that one model autonomously arbitrates colliding edits or repairs.

The bundled `ralph` workflow defines a task→research→orchestrator→two independent reviewer tasks→convergence gate→feedback/repair loop. It creates separate reviewer A/B task runs with comparison-base references and explicit evidence requirements, parses two results, requires both approval verdicts for `approved=true`, consolidates findings, runs bounded reverification of remaining findings and feeds the latest review report into the next orchestrator iteration. Invalid, failed, blocked or unparsed reviewer results are not silently counted as approval ([packages/workflows/builtin/ralph.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph.ts), [packages/workflows/builtin/ralph-runner.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph-runner.ts), [packages/workflows/builtin/ralph-review-gate.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph-review-gate.ts), [packages/workflows/builtin/review-convergence.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/review-convergence.ts)). The separate `adversarial-verification` builtin additionally supports criterion-scored verification and bounded repair, but the ralph native packaged path suffices as the primary audit evidence.

For whole-run current control, `packages/workflows` ships durable run status/stages/observation, workflow run-control command and control-tool actions (pause, resume, quit, inspect/attach), and human approval waiting stages, with resumed stage execution/state change rather than merely a display string ([packages/workflows/src/extension/workflow-run-control-command.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-run-control-command.ts), [packages/workflows/src/extension/workflow-tool-control.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-tool-control.ts), [packages/workflows/src/durable/resume-runtime.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/durable/resume-runtime.ts), [packages/workflows/src/extension/workflow-human-input.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-human-input.ts)).

## Operational model

A human asks Atomic to perform an engineering task. The packaged coding-agent session invokes the model-through-agent-core dependency to decide tool calls; the Atomic CLI runs its own supported file/shell tools and returns results to the model through session continuation. For a configured first-party parallel subagent task group, separate model-driven child agents can work in separate Git worktrees to avoid interfering changes to one checkout; their outputs remain separate for review/integration. When the operator chooses the bundled ralph workflow, the orchestrator writes a candidate result and evidence, two separately instructed reviewer tasks inspect its code/evidence and emit verdicts, and an explicit convergence gate requires both pass. Failure returns finding reports to the next bounded orchestrator iteration; exhausted reviews yield an unapproved handoff rather than fabricated success.

The operator can observe the entire current workflow, pause, steer/resume or abort active stage/run commitments, and supply human approval gates. That parent decision path is distinct from the model's ordinary choice of next file edit. No whole-system long-horizon outside/future intelligence based on the environment and returned durable capability redesign is established by the current-task research/reviewer/repair sequence.

## S1 — Operations

- State: A
- Function: adaptively execute coding tasks with tool use and observation-conditioned model choices.
- Disturbance / variety regulated: unknown repo state, test failures, tool errors, partial files, requirements ambiguity and changed task context.
- Decisive decision or feedback right: select coding action, inspect/change files, run commands and change the next task step after observing tool results.
- Decision owner: packaged Atomic model-directed coding actor; generic `pi-agent-core` provides an SDK loop as a dependency of the published package, while Atomic session and bundled tool/extension execution implement an agentic coding harness. No external vendor coding CLI is silently credited.
- Supporting / enforcement mechanisms: Atomic `AgentSession`, configured agent-core, first-party tools, session prompt/continue, persistence, provider adapters and optional subagents/workflows.
- Closure path: user task→`AgentSession.prompt`→model response through dependency→first-party tool results→agent continuation and revision/next action→completion.
- Boundary reachability: installed CLI exposes coding task paths in default modes, distinct from optional multi-stage workflow.
- Why this is / is not agent-owned: the model selects contextual next operations; guardrails, session state and extension hooks constrain rather than predetermine coding behavior.
- Evidence: [packages/coding-agent/src/core/agent-session-prompt.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/src/core/agent-session-prompt.ts), [packages/coding-agent/src/core/agent-session.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/src/core/agent-session.ts), [packages/coding-agent/src/core/tools/edit.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/src/core/tools/edit.ts), [packages/coding-agent/package.json](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/package.json).
- Basis: packaged first-party coding actor and dependency-labeled model/tool loop.
- Confidence: high that the shipped path exists; no live model performance claim.
- Caveats: the dependency supplies loop mechanics; no novel Atomic implementation of external SDK internals is claimed.

## S2 — Coordination

- State: C
- Function: prevent concrete cross-worker shared-checkout interference in a configured parallel coding-task group.
- Disturbance / variety regulated: two independent model-driven coding workers writing inconsistent changes to the same repo checkout or colliding when publishing a named output.
- Decisive decision or feedback right: choose isolated sibling Git worktrees with checked task CWDs; reject duplicate output paths and avoid concurrent write interference in the shared mutable checkout.
- Decision owner: first-party deterministic subagent orchestration constructor with optional `worktree` flag; not an autonomous coordinator model.
- Supporting / enforcement mechanisms: `createParallelWorktreeSetup`, Git worktree per task, independent child CWD, collision-safe output publication and explicit failure when worktree setup incompatible.
- Closure path: parallel work request with worktree option→first-party preparation isolates each coding S1's writable tree and validates CWD/output paths→child workers operate in separated worktrees→per-child results and patch artifacts return to parent without racing on the same working files.
- Boundary reachability: `packages/subagents` is bundled in shipped Atomic package; parallel executor actively calls setup in worktree-enabled supported mode.
- Why this is / is not agent-owned: concrete interference is attenuated by deterministic isolation, so constructor `C`, not A. Mere parallel spawn or messaging without isolation would not qualify.
- Evidence: [packages/subagents/src/runs/foreground/subagent-executor-parallel.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/foreground/subagent-executor-parallel.ts), [packages/subagents/src/runs/foreground/subagent-executor-worktree.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/foreground/subagent-executor-worktree.ts), [packages/subagents/src/runs/shared/worktree.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/runs/shared/worktree.ts), [packages/subagents/src/shared/exclusive-file-publication.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/subagents/src/shared/exclusive-file-publication.ts).
- Distinct S1 units: separate model-directed coding-agent children in a parallel execution group.
- Inter-S1 disturbance: overlapping writes to the shared Git working directory or duplicate output publication paths.
- Attenuating coordination relation: per-child Git worktree isolation, validated CWDs and duplicate output publication blocking.
- Feedback into subsequent S1 behaviour: accepted child execution paths move to isolated worktrees and conflicting publication is refused before the worker result can be treated as a valid shared artifact.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: construction specifically changes the shared mutable write domain, attenuating interference in the same resource two S1s would otherwise contend for.
- Basis: source-proven explicit mode-specific coordination construction.
- Confidence: high for static supported worktree path.
- Caveats: off by default when worktree false; isolation does not prove autonomous merge resolution or elimination of semantic conflicts between patches.

## S3 — Inside-and-now control

- State: P
- Function: parent-controlled current management of a whole durable coding workflow and its live stage commitments, failure/resumption and approvals.
- Disturbance / variety regulated: blocked/failed stages, developer interruptions, changing priorities and budget/time or review gate status within an ongoing multi-stage run.
- Decisive decision or feedback right: inspect an overall run/stage state then pause, resume/steer or quit a run, supply human gate decisions and return worker execution to an authorized state.
- Decision owner: human operator through first-party workflow command/TUI; model may orchestrate stage-level tasks but an autonomous distinct whole-current S3 decision owner was not demonstrated.
- Supporting / enforcement mechanisms: durable store, stage/run snapshots, workflow status and run-control commands, `pauseRun`, `resumeRun`, `quitRun`, human-input gate and stage admission/resume logic.
- Closure path: run-wide status/stages/blocker observations→operator command/approval choice→persisted control transition→stage work is paused, resumed or aborted with observable new state.
- Boundary reachability: bundled workflow extension registers shipped `/workflow` and tool controls and status inspections for user-run workflows.
- Why this is / is not agent-owned: parent `P` covers actual whole-run operational intervention rather than mere UI or local tool permission; no S3=A is claimed.
- Evidence: [packages/workflows/src/extension/workflow-run-control-command.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-run-control-command.ts), [packages/workflows/src/extension/workflow-tool-control.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-tool-control.ts), [packages/workflows/src/extension/workflow-human-input.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-human-input.ts), [packages/workflows/src/durable/resume-runtime.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/durable/resume-runtime.ts).
- Whole-system current view: run stage status, progress and resumable/paused state, including reviewer outcome when configured.
- Current-control decision scope: pause/resume/quit active workflow stages and human advancement through gated work.
- Basis: parent-governed current whole-workflow path.
- Confidence: medium; specifically workflow mode.
- Caveats: workflow stage sequencing or default single-agent approvals alone would not support a distinct whole-current S3.

## S3* — Complementary audit

- State: A
- Function: separately model-driven reviewer tasks verify a distinct producer/orchestrator's engineering claims using code/evidence and feed binding findings to the workflow's next action.
- Disturbance / variety regulated: candidate implementation looks complete but violates original objective, is incorrect, lacks validation or has regression/security flaws.
- Decisive decision or feedback right: reviewer A and B each issue independent judgment on code/evidence; both must give parsed acceptable verdicts for approval, otherwise continued correction or explicit unapproved handoff.
- Decision owner: separate first-party `ralph` reviewer model tasks (within packaged workflow), distinct from the producing orchestrator. The convergence arithmetic is a deterministic guardian of their agent judgments, not the author of correctness claims.
- Supporting / enforcement mechanisms: `ctx.parallel` reviewer calls with distinct role/model configs and evidence reads; parsed review decision contract, reject-invalid/convergence logic, consolidated findings, bounded independent reverification and next orchestrator iteration informed by reports.
- Closure path: implementation/research evidence from orchestrator→two independent reviewer task sessions inspect repo delta and evidence→structured findings + typed approve/incorrect verdict→`ralphReviewConvergence` checks→two-approval gate or consolidated findings/reverification→next model-directed implementation/repair, or explicit nonconverged outcome at bound.
- Boundary reachability: installed `ralph` builtin declared in workflow builtin manifest, wired by `runRalphWorkflow`; no external CI or human-authored review prompt is needed when this supported mode is invoked.
- Why this is / is not agent-owned: substantive pass/fail evidence and advice belong to separate reviewers, not the same producer and not a fixed program-only checker.
- Evidence: [packages/workflows/builtin/ralph.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph.ts), [packages/workflows/builtin/ralph-runner.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph-runner.ts), [packages/workflows/builtin/ralph-review-gate.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph-review-gate.ts), [packages/workflows/builtin/review-convergence.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/review-convergence.ts).
- Claim being audited: correctness, scope fidelity and sufficient proof of orchestrator-produced code changes.
- Ordinary reporting path: orchestrator task report and implementation notes.
- Complementary access path: new reviewer tasks read research, implementation notes and orchestrator report, and prompts require source-delta checking against base branch.
- Independence boundary: distinct reviewer task invocations with reviewer A/B model configurations, separate from producer; both must independently pass, though provider-level independence and real-world results are untested.
- Who acts on findings: workflow loop consolidates/reverifies and returns negative findings into bounded next orchestrator implementation; unapproved completion stays distinguishable from success.
- Basis: source-confirmed packaged, mode-specific auditor-decision-return closure.
- Confidence: medium-high for first-party wiring, no live witnessed audit.
- Caveats: does not imply default coding chat or every workflow automatically runs two reviewers. This is operational reviewer independence of sessions, not separately attested external review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separately owned external/future intelligence cycle that selects and returns a prospective change to Atomic's own sustained capabilities.
- Disturbance / variety regulated: iteration feedback, reviewer findings, memory pressure and task-specific research are about completing an ongoing coding objective, not reconfiguring future system capacity based on external futures.
- Decisive decision or feedback right: select a prospective capability/strategy change across future tasks in response to outside/environment intelligence; not identified.
- Decision owner: workflow orchestrator and reviewer model focus on present task, human may update configuration or packaged workflow outside run but no functional S4 actor.
- Supporting / enforcement mechanisms: research stage, resumable checkpoints, reviewer/repair iterations, skill and workflow authoring; none alone qualifies as an installed outside-and-then decision-owner.
- Closure path: reviewer feedback returns into present implementation attempt; no independent external change forecast→future-capability design→adoption into stable operational harness found.
- Why this is / is not agent-owned: the ralph research stage and retrospective repairs serve current work; mere extensibility and maintainer releases cannot donate organizational S4.
- Evidence: [packages/workflows/builtin/ralph-runner.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph-runner.ts), [packages/workflows/src/authoring.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/authoring.ts), [packages/coding-agent/src/core/agent-session-auto-compaction.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/src/core/agent-session-auto-compaction.ts).
- Basis: bounded negative source inspection.
- Confidence: medium.
- Caveats: external adopter could author a self-improvement process, which is not established by this frozen supported boundary.

### Absence scope

- Surfaces inspected: builtin ralph/goal/adversarial loops, workflow authoring/loader and durable state, agent-session context, subagent orchestration, user commands.
- Plausible first-party paths checked: workflow research, continuous implementation-review cycles, model routing, dynamic reloading of scripts, memory/skills.
- Why no material first-party path remains: all direct feedback is current coding/verification, and prospective harness capacity is not chosen and returned as an independently owned strategic/intelligence loop.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct ultimate organizational identity/policy adjudication owner at the installed coding-work recursion.
- Disturbance / variety regulated: unsafe tools, acceptance policy and authorization boundaries are operational enforcement, not demonstrated identity/purpose conflict.
- Decisive decision or feedback right: make rightful top-level purpose/identity interpretation and return binding policy authority to operational/current and future systems; no function owner evidenced.
- Decision owner: user can approve gates and configure workflow/agent resources, while code enforces fixed bounds; no installed S5 organ with legitimacy/purpose remit.
- Supporting / enforcement mechanisms: approval gates, role/tool constraints, task authorization, repository instructions and user settings.
- Closure path: configured command/human gate can permit or stop a workflow stage; this is S3 parent/current policy, not an ultimate-identity S5 decision loop.
- Why this is / is not agent-owned: having a human confirmation or immutable acceptance criteria does not automatically make the coding harness an organization with final identity/policy owner.
- Evidence: [packages/workflows/src/extension/workflow-human-input.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/src/extension/workflow-human-input.ts), [packages/coding-agent/src/core/agent-session.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/coding-agent/src/core/agent-session.ts), [packages/workflows/builtin/ralph.ts](https://github.com/bastani-inc/atomic/blob/d6bc44cf753bd2748ffac6dd994205a170216741/packages/workflows/builtin/ralph.ts).
- Basis: bounded negative.
- Confidence: medium.
- Caveats: adopting organization may be S5 parent but is outside the first-party installed harness boundary.

### Absence scope

- Surfaces inspected: command policy, workflow human gates, role restrictions, operator current controls, repository instructions.
- Plausible first-party paths checked: slash approvals, access credentials, human gates, workflow contracts, project maintainers.
- Why no material first-party path remains: none is a distinct accountable authority interpreting organization-wide ultimate identity and returning that ruling at a separate recursion level.

## Evidence gaps

- No provider-backed model inference, runtime adversarial conflict trial or genuinely independent reviewer execution was run; reported states concern shipped first-party paths in frozen source.
- Model loop mechanics are delegated in part to a packaged upstream-derived Pi agent core. S1 attribution is for the complete shipped Atomic coding-agent operating product and its first-party tool/continuation, not the invention of the dependency.
- S2 worktree option is explicit and opt-in; absent that setting parallel workers can still collide in a shared checkout, so state C must not be read as always-on isolation.
- S3 parent supervision and S3* two-reviewer agreement depend on installed workflow and specifically ralph verification mode, rather than an assumed default chat workflow. Actual reviewer success quality is not measured.

## Conclusion

Frozen Atomic ships autonomous coding sessions (S1=A), an optional first-party child-worktree collision attenuation constructor (S2=C), parent-owned durable whole-workflow current controls (S3=P), and model-owned separate dual-reviewer evidence/repair closure in a shipped ralph workflow (S3*=A). Current-task research/review does not establish future-capability S4 intelligence, and approvals do not establish S5 ultimate identity/policy. Source-first, mode-specific preliminary vector: **A / C / P / A / — / —**; proposed only until a separate Index canonical admission.
