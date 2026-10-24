---
harness_id: harness-cli
project_name: Harness² CLI
repository: https://github.com/3ae3ae/harness2-cli
review_ref: 0c811344a4edfe34960b2fc8f286369d7e81fb27
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: —
---

# Harness² CLI

## Review boundary

- System in focus: The separately packaged **Harness² CLI harness-improvement application**, not the target coding assistant, Google Research's experiment organization, or all developer work in this source repository. It reuses much of upstream `google-research/harness2`'s experimental core but ships materially different CLI, configuration, human selection, consolidation and deployment surfaces.
- Purpose and identity: Improve the *harness* of a configured coding agent against user-supplied tasks, compare executable candidate behavior, retain transferable domain lessons and prepare one consolidated future harness for optional application to the user's project.
- Relevant environment: User project tasks, actual coding-agent trajectories and deliverables, differences among candidate harnesses, project-specific components, newly encountered domain problems, future tasks and a supervising local operator.
- Standard-distribution boundary: Installable Python `harness2` CLI and `harness2/core`, `harness2/substrate`, `harness2/suite.py`, `harness2/settings.py`, `harness2/workspace.py` in the reviewed public revision. External Claude/Codex/OpenCode executors and model providers supply agent cognition but are not separately credited as first-party organizational owners.
- Credited operating / distribution surfaces: [CLI run](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L207), [recursive editor/probe](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/recursion.py#L135), [scheduler/adoption](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L495), [selection/reflection](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/selection.py#L268), [library](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/library.py#L58), [human selector](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/human.py#L29), [project apply](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/apply.py#L79).
- Adjacent first-party surfaces excluded from ownership: The inherited paper and Google Research benchmark experiments; `plugins/harness2-benchmarks`, tests and example fixtures when not configured as production runtime; project/maintainer governance and upstream research institution. Their grading or authority is not counted as a separate S3*, S5 or additional viable S1.
- First-party operating / deployment modes considered: Model-backed automatic proposer/selector/reflector with `run --mode parallel|sequential`, domain library and consolidation; supported `run --selector human` with interactive blind selection (`k > 1`); separate `diff`, `eval` and `apply` (`--yes`, confirm, per-file interactive review) commands. No paid/model-backed evaluation was executed for this source review.
- Recursion level: One harness-improvement work system; model-backed task improvement is its operational S1, and evidence-grounded across-task prospective adaptation is its S4. The configured coding agent is an *execution substrate*, not a separately established owned S1 division.
- Reviewed revision: `0c811344a4edfe34960b2fc8f286369d7e81fb27`, fixed intake [#2000](https://github.com/opensiro/vsm-harness-index/issues/2000), operational batch [#2001](https://github.com/opensiro/vsm-harness-index/issues/2001).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`harness2/cli/run.py` loads a named run, configures a benchmark/task adapter and proposer, selector and reflector channels, and invokes `schedule.run_sweep`. `schedule.run_task` gathers actual base-agent rollouts, calls `recursion.run_mode` to create/probe separate candidate harness trees, selects a final, then writes a selection and model-distilled experience into a mode/domain library. Later tasks read the library as part of their improver context. At `k > 1`, selection can be a configured model or a human choosing anonymously presented output evidence. The CLI also includes its own consolidator for a single future project harness, plus `diff`, `eval` and guarded `apply` commands. [Run](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L303), [sweep](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L584), [library return](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L702), [apply](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/apply.py#L79).

This is a **derivative**, not an unrelated invention: its recursive core and conceptual S1/S4 mechanism overlap with the already indexed [Harness²](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/ha/harness2.md). Separate provenance and a new supported interactive selection/final-project application boundary justify a distinct application assessment; shared core behavior must not be represented as an independent original research result or an extra observed performance gain.

## Operational model

The operational outcome is a validated candidate and final consolidated harness for the target user's coding-agent tasks. Configured model-backed improvers **choose and edit** harness components from task evidence; the deterministic scheduler/validator checks component scope, starts substrate rollouts, retries a rejected candidate once and persists artifacts. A configured selector or, in an explicit separate mode, the parent user chooses among final candidate outcomes. The reflector chooses future-relevant lessons; the library makes them available to later task improvers. The user may decide whether and which candidate files to apply to the actual project; this deployment gate is not an agent-owned ultimate-policy board. [Proposer](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/proposer.py#L126), [stage](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/recursion.py#L135), [selection](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/selection.py#L268).

## S1 — Operations

- State: A
- Function: Bounded model-backed improvement work per encountered task: examine operational evidence, edit a harness, probe the edited candidate and produce a selected task harness plus result.
- Disturbance / variety regulated: Different user problems and actual coding-agent failures demand different instruction, skill, script or hook changes; candidate edits can also violate a harness component contract.
- Decisive decision or feedback right: Configured improver chooses candidate file changes and explains them against evidence. The model selector (in automatic mode) chooses a final task result where multiple candidates exist.
- Decision owner: Model-backed proposer/editor and optional automatic selector, invoked through the first-party session interface. External executor cognition is a dependency, but the improvement goal and agent-edit control path are shipped by the reviewed CLI.
- Supporting / enforcement mechanisms: Workspace harvest, component allowlist, tree validation, per-stage retry/fallback, rollout adapter, result/trajectory records and candidate selection parser.
- Closure path: Current base-task rollout → independent agent-edited harness trees → validated candidate task probes → composed candidate and selector result → accepted task-harness and evidence for later reuse.
- Boundary reachability: `cli.run` constructs `Proposer` with the installed channel config and invokes `schedule.run_sweep`; `run_task` calls `recursion.run_mode`, whose `_run_stage` actually invokes `Proposer.call` with writable context/harness and captures its changed tree, then probes candidates. All are included in the shipped CLI mode.
- Why this is / is not agent-owned: The model makes contentful harness edits and, when configured, evidence-driven task-result choices; source-local Python merely bounds and enforces those decisions. Dry-run, static tests and deterministic fixtures by themselves do not prove model autonomy.
- Evidence: [run.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L307), [recursion.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/recursion.py#L135), [proposer.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/proposer.py#L126), [schedule.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L584).
- Basis: Supported live-model session path at the frozen commit, not asserted empirical success rate.
- Confidence: High for source-wired decision ownership; outcome quality untested.
- Caveats: The target coding assistant and provider are externally configured and not extra first-party viable S1 units.

## S2 — Coordination

- State: —
- Function: No evidenced S2-specific stabilization among two distinct, separately viable owned S1 units.
- Disturbance / variety regulated: Concurrent candidate and domain execution might consume resources, but distinct S1 divisions and an inter-unit oscillation/collision control relation are not established.
- Decisive decision or feedback right: Deterministic concurrency width, domain ordering, semaphore and run-label isolation coordinate experimental steps, not an agentic inter-S1 conflict response.
- Decision owner: Static Python scheduler and operator configuration.
- Supporting / enforcement mechanisms: `ThreadPoolExecutor`, proposer semaphore, namespace isolation, mode/domain libraries and run budget.
- Closure path: Scheduled experiments complete and aggregate; no S2-specific sensed interference and returned reciprocal adjustment across autonomous operating units.
- Why this is / is not agent-owned: Stage-level parallelism, composition and result pooling are parts of one bounded optimization process, not S2 because they run concurrently.
- Evidence: [schedule.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L702), [recursion.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/recursion.py#L400), [proposer.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/proposer.py#L36).
- Basis: Scoped source negative after examining task and domain concurrency.
- Confidence: High.
- Caveats: An external multi-agent product using this CLI might provide S2 independently.

### Absence scope

- Surfaces inspected: Task scheduler, parallel/sequential recursion, model-session concurrency, domain sequencing and candidate selection.
- Plausible first-party paths checked: Independent general/domain proposal editors, rollout resource collision, competing domains and shared reflection library.
- Why no material first-party path remains: These are separated experimental phases or per-domain histories, with no distinct S1 interference requiring damped mutual adjustment and no S2-specific closed path.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current control relationship over independently viable operational divisions at this recursion.
- Disturbance / variety regulated: Budget overruns, candidate failures, task completion, user approval and project file drift are local run/deployment constraints rather than multi-unit resource/commitment governance.
- Decisive decision or feedback right: The operator sets execution budget, task set and allowed surface; runtime enforces limits; selectors compare results. None revises current commitments across distinct S1 units with systemic authority.
- Decision owner: CLI user for configuration, deterministic scheduler for enforcement and model for candidate choice; no separately supported S3 owner.
- Supporting / enforcement mechanisms: Budget/call caps, run status, concurrency limit, retries, `apply` conflict checks and --force option.
- Closure path: Fixed run settings → bounded task experimentation → output; absent whole-current S3 view, discretionary priority/resource intervention and returned binding adjustment to multiple ongoing units.
- Why this is / is not agent-owned: Picking a better harness is an operational or prospective adaptation choice; enforcing an operator's preset budget is not agent-owned S3 and ordinary apply approval is not parent-governed whole-system control.
- Evidence: [run.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L207), [schedule.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L584), [apply.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/apply.py#L79).
- Basis: Bounded negative of whole-organization current-control closure.
- Confidence: Medium-high.
- Caveats: Operator may manage a larger organization, but its current control is not implemented by this application.

### Absence scope

- Surfaces inspected: CLI settings, task/domain scheduler, mode selection, call budget, stop/status and apply workflow.
- Plausible first-party paths checked: Budget controller, user-approved apply as S3 parent, domain coordinator as whole-current manager, candidate selector as resource allocator.
- Why no material first-party path remains: No surfaced path evaluates whole-current multi-unit commitments and returns binding current control; supplied limits and one project's adoption are below this organizational threshold.

## S3* — Complementary audit

- State: —
- Function: No independently complementary audit channel challenges routine S1–S3 reports and closes findings into corrective systemic control.
- Disturbance / variety regulated: Bad candidate harness files, inaccurate agent result claims and poor task answers are checked by local tree validation, rollout comparisons, benchmark judging or optional evaluation.
- Decisive decision or feedback right: Ordinary candidate validators, task selector and `eval` compare outputs; none has separately independent authority to audit a standing S3 report and route corrective findings to management.
- Decision owner: Deterministic validators/evaluation routines, configured model selector or human comparator within the same adaptation process.
- Supporting / enforcement mechanisms: Harness component checks, anonymous candidate selection, result reports and user-triggered `eval`.
- Closure path: Candidate/result evidence → within-loop selection and optional later quality measurement; no complementary audit → binding whole-current corrective return.
- Why this is / is not agent-owned: Independent improver proposals and blind selection reduce some bias, but are routine production/evaluation, not an independent S3* oversight path.
- Evidence: [selection.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/selection.py#L268), [eval.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/eval.py#L1), [judge.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/judge.py#L1).
- Basis: Scoped negative distinguishing quality checks from complementary audit independence.
- Confidence: Medium-high.
- Caveats: A separate external QA team could supply such audit for a deployed agent but is outside this reviewed system.

### Absence scope

- Surfaces inspected: Candidate validation and contrast, blind model/human selection, bench judging, standalone `eval` and reporting.
- Plausible first-party paths checked: Human selection as independent auditor, test-set re-evaluation as S3*, separate rubric and grader, invalid harness retry and leak checks.
- Why no material first-party path remains: These check/improve task results inside the same optimization activity and do not complement S3 current reporting with an independent corrective return path.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Model-backed across-task prospective harness adaptation with a second, explicitly supported **parent-controlled blind-selection mode** that changes which candidate and lesson enter the future task library.
- Disturbance / variety regulated: Unfamiliar project tasks, newly observed errors and weak transfer of task-specific improvements to later tasks; user may also disagree with automated candidate choice.
- Decisive decision or feedback right: Automatic selector chooses the adopted candidate and reflector extracts a transferable lesson; in `--selector human` mode the user personally selects among blinded final candidates while a model reflector can distill the adopted result. The choice feeds subsequent tasks through the library.
- Decision owner: `A`: model-backed selector and reflector/proposer in CLI sweep; `P`: operator at the shipped interactive selector, not the benchmark author or external research institute. Each mode has separately attributable adoption authority.
- Supporting / enforcement mechanisms: Per-domain sequential `Library`, `selection_pool`, anonymous candidate files, human TTY prompt/choice, adopted tree and experience persistence, `context.build` injection into later proposer contexts; final project deployment is optional with `apply`.
- Closure path: Encounters and candidate execution evidence → automatic/human chosen task harness → model-reflected generalizable lesson → `mode_lib.add` → next task's proposal context includes earlier domain library → potential changed subsequent harness. After a run, generated consolidated harness may also be explicitly applied to project files.
- Boundary reachability: Shipped `cli/run.py` chooses `HumanSelector` when `selector.channel.kind == human`; otherwise it instantiates model-backed `Proposer`. Both invoke `schedule.run_sweep` and `selection.run_selection`; `schedule._run_one_mode` calls `reflect_adoption` and conditionally `mode_lib.add`, while next task's `_run_stage` loads the library. `cli/apply.py` separately permits reviewed real project-file adoption.
- External distinction: Actual newly encountered user task domains and contrasted coding-agent trajectories expose operational shortcomings not specified in a fixed harness.
- Future / prospective distinction: Per-domain transferable lessons plus consolidated project harness target future tasks, rather than merely grading or repairing one immediate deliverable.
- Adaptation option generated: Model editor proposes changed skills/instructions/scripts/hooks; model/human selector adopts a tested candidate; reflector writes future-reuse cues; consolidation proposes project-wide next-task harness.
- Path back into current capability / S3: Selected experience is persisted in the per-domain library and read by subsequent model proposer sessions, changing the options considered for later edits. The optional `apply` command installs consolidated or one-task adopted components into the user's project; no independent S3 manager is asserted.
- Why this is / is not agent-owned: `A` has agent-owned candidate choice and lesson generation with model decisions returning through first-party memory to later operations. The distinct `P` mode assigns the same consequential selection right to the user through a real terminal interaction and returns it through the same library. This does **not** assign the separately guarded final installation to the model.
- Evidence: [run.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L307), [human.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/human.py#L29), [selection.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/selection.py#L268), [schedule.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L495), [library.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/library.py#L58), [apply.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/apply.py#L79).
- Basis: The two first-party shipped prospective adaptation loops share the persistent future-facing library, but have distinct actual adoption decision owners.
- Confidence: High for reachable branch/closure, medium for model generalization since no model runs were made.
- Caveats: `--selector human` requires a TTY and multiple finalists (`k > 1`); at `k=1` selection is trivial. A failed reflection yields no transferable lesson. Project `apply` defaults to human approval and is not evidence of autonomous project deployment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Configured model selector and reflector | `run` with model-backed selector; multiple candidate finals | Model chooses adopted tree, reflects lesson, library affects later proposer | [`cli/run.py`/`schedule.py`](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/core/schedule.py#L495) |
| Parent (`P`) | Terminal user choosing anonymous result | `run --selector human` (`k > 1`) | User's chosen tree and model-reflected lesson enter the same library for future task operations | [`cli/human.py`/`schedule.py`](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/human.py#L29) |

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate identity/mission-policy adjudication is shipped for the overall improvement organization.
- Disturbance / variety regulated: Operator task selection, allowed editable files, model/provider choice, benchmark scope and safety limits bound execution but do not create a separate ultimate policy decision loop.
- Decisive decision or feedback right: User chooses and configures the run and can approve/force project-file writes; no identity-level conflict is escalated to a legitimate authority and returned as governing policy.
- Decision owner: External developer/project owner for the overall purpose; shipped runtime for validation and configured model for bounded edits.
- Supporting / enforcement mechanisms: CLI config and setup, component tree validator, source boundaries, apply confirmation and git-dirty checks.
- Closure path: User-provided goal and constraints → local optimization and optional installation; absent system identity dispute → authority judgment → returned revised governing policy.
- Why this is / is not agent-owned: Supervised application is an operational/capability adoption gate, not by itself an identity- or ethos-level S5 decision. The parent-mode S4 classification does not automatically imply S5=P.
- Evidence: [settings.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/settings.py#L1), [run.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/run.py#L207), [apply.py](https://github.com/3ae3ae/harness2-cli/blob/0c811344a4edfe34960b2fc8f286369d7e81fb27/harness2/cli/apply.py#L79).
- Basis: Bounded negative for identity-level authority and operational return.
- Confidence: Medium-high.
- Caveats: The user's broader software organization may have S5; this repository does not establish its governance authority.

### Absence scope

- Surfaces inspected: Project init/config, run/proposer scope, selection, consolidation, apply and owner-supplied objectives.
- Plausible first-party paths checked: `--selector human` as ultimate authority, project `apply` as identity decision, component restrictions as policy, contributor/maintainer governance.
- Why no material first-party path remains: Shipped human and agent decisions change proposed capability within an externally supplied mission, but no first-party identity-level issue/decision/returned-policy channel exists.

## Distributed OSS parent arrangement

The repository is independently distributed from its Google Research ancestor; code inheritance is not evidence of common organizational governance. Local developer/operator, external model vendor, original upstream authors and source-repo maintainer are distinct. Parent `P` is credited **only** to the explicitly supported per-run human selection loop at local contribution-cell recursion, not a shared OSS institution. No organization-wide S3/S5 parent status is inferred.

## Self-hosted and non-human modes

The model-backed CLI supports self-configured model channels and target Claude/Codex/OpenCode/command substrates. The operator can run automatic blind selection, request a human selection instead, and later choose whether to `apply` (with confirmation, per-file review or `--yes`). The first-party CLI contracts and tests can be inspected deterministically; none of this report's labels represents a live provider execution or verified improvement on real external tasks.

## Recursion

The system under assessment is the *harness optimizer*. Proposed/probed task harnesses are S1 work products; the selection/reflection/library feedback generates future improvement options (S4). The downstream coding agent's own organization, the Google Research upstream lab and the user's governing project are distinct possible recursions requiring separate evidence. Human task-harness selection is a local S4 parent mode, not evidence of separate policy sovereignty.

## Variety and escalation

Model edits encounter both variable task outcomes and forbidden/malformed harness changes; fixed editable-surface checks, retry/fallback, per-run budgets and apply conflict handling constrain execution. Failed model calls or invalid candidate trees fall back or stop rather than proving S2/S3 governance. Human `--selector` intervention explicitly replaces automatic adoption of one candidate, then routes the chosen result to the common reflection and future library loop.

## Evidence gaps

- Source review only; no live LLM, paid provider, external coding agent or quality-efficacy benchmark run. Positives are source-wired autonomous and parent-controlled modes, not measured performance claims.
- Google Research `harness2` is already indexed; this CLI derives substantial core code and adds an installable, supervised operating surface. Its distinct assessment is boundary-specific and **must not** be read as independent research or a duplicate measurement of the same upstream evaluation.
- Default `k=1` bypasses contest-style selection, whereas supported `k > 1` gives the parent user a real adoption choice. S4 parent ownership is scoped to that supported mode, not every invocation.
- Per-domain library entries only materialize when both selection and usable model-produced experience are present; a failed reflection does not establish effective learning on that particular task.
