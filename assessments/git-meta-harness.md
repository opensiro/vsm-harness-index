---
harness_id: git-meta-harness
project_name: git-meta-harness
repository: https://github.com/brenonaraujo/git-meta-harness
review_ref: 167b13c66993fa0a5216e4be2fc9bf911cd02cf8
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# git-meta-harness

## Review boundary

- System in focus: The **first-party materialized git-meta-harness delivery organization** installed from this frozen repository into an adopter project: its generated personas, GitHub issue/PR and branch contracts, Hermes cron-backed team-manager, separately invoked builders and QA, conflict sensors and optional future-persona proposal tooling. Recursion is the live *adopter project delivery cell* with multiple ongoing independently acting coding personas, not the source author's own company/repo governance, and not the Hermes runtime internals.
- Purpose and identity: Transform a user's product specification or GitHub issue backlog into completed software changes using model-backed specialist agents, a live team manager, evidence/test gates, human validation before final release and recorded issue/PR state.
- Relevant environment: New functional specs, PRs, failures of model-backed implementation, shared branch/file conflicts among builders, CI checks, user acceptance and evolving persona/skill suitability inferred from actual issue comments.
- Standard-distribution boundary: Go `gmh seed`/install and `gmh loop install` materialization, copied `harness/personas`, `harness/scripts/loop`, `harness/workflow`, `harness/sensors` and optional `gmh evolve` inside an adopter repository. Hermes profiles/cron and `gh` execute the materialized contract as externally provided tool/process services; they do not supply unrelated organizational rights to this harness.
- Credited operating / distribution surfaces: [seed.go L1-145](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/seed/seed.go#L1-L145), [loop.go L1-164](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/loop/loop.go#L1-L164), [loop.go L14-91](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/cmd/loop.go#L14-L91), [spawn-tm.sh L1-32](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/spawn-tm.sh#L1-L32), [team-manager-tick.md L1-45](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L1-L45), [team-manager.md L1-91](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/team-manager.md#L1-L91), [check-parallel-builders.sh L1-93](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/check-parallel-builders.sh#L1-L93), [10-decomposition-safety.md L1-117](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/sensors/10-decomposition-safety.md#L1-L117), [quality-assurance.md L1-86](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/quality-assurance.md#L1-L86), [evolve.go L1-141](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/evolve/evolve.go#L1-L141), [evolve.go L1-91](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/cmd/evolve.go#L1-L91), [08-persona-evolve.md L1-112](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/08-persona-evolve.md#L1-L112).
- Adjacent first-party surfaces excluded from ownership: The framework repository maintainer's live source CI/releases; the external Hermes model/runtime/shell/gateway as an independent organization; speculative architecture diagrams and proposed future features; real customer's GitHub branch protection not necessarily configured; human organizational mission-setting; reported third-party case-study quality/performance.
- First-party operating / deployment modes considered: Successful `gmh seed` installs runnable team-manager and specialist personas/cron; `gmh loop install` for existing projects; no-agent cron launcher that starts a `hermes` model-backed manager; dynamic GitHub label/PR reading and specialist spawning; optional path overlap sensor and QA review; separately invoked `gmh evolve --apply` deterministic proposal/trace writer (not an autonomous mutation).
- Recursion level: One project delivery organization with separately executing specialist coding agents as operations and shared delivery management, interference control, quality audit and potential future role improvements.
- Reviewed revision: `167b13c66993fa0a5216e4be2fc9bf911cd02cf8`, frozen intake [#1699](https://github.com/opensiro/vsm-harness-index/issues/1699), serial [batch #1700](https://github.com/opensiro/vsm-harness-index/issues/1700).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `gmh` CLI is primarily a **materializer**, not a separately resident autonomous agent runtime: `seed.Plan` constructs domain-specialized personas, Issue 0 and two cron job definitions; `seed.Apply` copies the first-party harness, emits spec and loop scripts. `gmh loop install` calls the externally installed Hermes cron with declared schedules, while `spawn-tm.sh` starts one bounded `hermes -p team-manager chat --oneshot` process. The installed `team-manager-tick.md` is executed by that actor and explicitly requires reading GitHub Issues/PRs, deciding label/state changes, spawning separate personas and returning on a later tick. This makes a source-wired operating mode rather than attributing an entire runtime to a prose README. [seed.go L20-145](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/seed/seed.go#L20-L145), [loop.go L94-164](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/loop/loop.go#L94-L164), [loop.go L16-100](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/cmd/loop.go#L16-L100), [spawn-tm.sh L1-32](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/spawn-tm.sh#L1-L32), [team-manager-tick.md L1-45](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L1-L45), [07-hermes-loop.md L1-95](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/07-hermes-loop.md#L1-L95).

The manager sees the project-level backlog and current open pull requests, classifies `type/*` work, chooses persona ownership, creates implementation branches, enforces a maximum three-worker budget, watches blocked and QA-rejected tasks and loops back to builders. The distinct builder personas operate on actual repository changes; the manager does not author their feature code. Cross-worker interference is addressed by shipped Sensor 10: before releasing ready builders, parse their `path-scope:`/dependency labels; a missing scope or uncovered overlapping scope blocks parallel dispatch. Detection is a deterministic helper and policy from the materialized harness; false negatives from synthetic glob matching are possible, so do not infer self-governing S2 autonomy. [team-manager.md L14-155](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/team-manager.md#L14-L155), [team-manager-tick.md L12-44](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L12-L44), [check-parallel-builders.sh L1-205](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/check-parallel-builders.sh#L1-L205), [10-decomposition-safety.md L1-110](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/sensors/10-decomposition-safety.md#L1-L110).

The separately spawned QA persona reads DoD, PR, actual build/test/security/contract outcomes and creates a report with approve/reject. Rejection uses `in-review` rather than `qa`; the next manager tick detects that state, re-dispatches a builder and withholds final closure. These return conditions form independent complementary operating inspection beyond an implementing builder's claim of completion. Some reported sensor integrations refer to adoption-project toolchains that are not bundled or executed in the source checkout; do not count listed example commands as successful test runs. [quality-assurance.md L1-123](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/quality-assurance.md#L1-L123), [team-manager-tick.md L20-42](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L20-L42), [02-pull-request.md L42-122](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/02-pull-request.md#L42-L122).

`gmh evolve` **does not evolve live personas**. The Go implementation scans already supplied issue/comment JSON for deterministic keywords such as AC/DoD/persona gaps, formats future-oriented candidate persona/skill patch suggestions, and `--apply` writes only `comments.json`, `proposal.md` and `PROMPT.md` under a dated trace. The delivered `PROMPT.md` is explicitly a handoff to the external Hermes manager, and project docs mandate human `validado` before someone edits a persona file. Thus an externally informed prospective **constructor/proposal** path exists but no first-party autonomous candidate judgment and installed future capability is source-closed solely by `gmh evolve`. [evolve.go L1-183](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/evolve/evolve.go#L1-L183), [evolve.go L1-83](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/cmd/evolve.go#L1-L83), [08-persona-evolve.md L45-110](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/08-persona-evolve.md#L45-L110).

Frozen source checkout at `167b13c66993fa0a5216e4be2fc9bf911cd02cf8` with MIT license passed `bash -n` across **13 first-party shell scripts** plus `python -m compileall` of bundled Python visual helpers, with clean worktree. Go toolchain was unavailable in isolated assessment VM, so no `go test ./...` or external Hermes/GitHub production run was executed and no README case-study success is independently claimed.

## Operational model

The materialized delivery cell runs independent model-backed coding specialists as its S1 work. Its installed manager observes the shared issue/PR board and exercises model-based current commitment decisions over who works next and what blocks/repairs (S3), while a narrower source-backed conflict sensor can be composed into true inter-S1 damping (S2=C). A separate QA persona accesses branch/DoD/test evidence and sends findings into rework/merge control (S3*=A). `gmh evolve` produces future-change options and an explicit manual/Hermes completion recipe but does not itself close automatic adaptation (S4=C). The parent user's normal product acceptance is not ultimate constitutional policy authority (S5=—).

## S1 — Operations

- State: A
- Function: Independently implement or inspect product changes through distinct model-backed builder, architect and specialist personas, in contact with real issue requirements and repository work.
- Disturbance / variety regulated: Unfamiliar user requirements, changing source code, failing tool/build responses and task-specific choices about edits or investigations.
- Decisive decision or feedback right: Installed persona model acting via Hermes selects the content of source edits/technical output and returns a comment, PR, revised specification or real artifact to the project.
- Decision owner: Project-specific model-backed worker personas materialized by `gmh seed` and launched through supported Hermes profile/runtime; external runtime supplies terminal/LLM execution but role-specific mission/contract is first-party.
- Supporting / enforcement mechanisms: Persona Markdown, Hermes cron, `spawn-persona.sh`, issue/PR state, executable specialist commands, branch rules, local Git repository, deterministic CI/sensor gates.
- Closure path: Project requirement → manager-dispatched persona issue/brief → worker chooses and executes terminal/source operations → comments/branch/PR/test outputs → returned GitHub state for subsequent work/next manager tick.
- Boundary reachability: Source-owned `seed.Apply` writes persona and spawn contracts, loop installer schedules recurring manager launches, `team-manager-tick.md` calls `spawn-persona.sh` with a real named profile; this is an executable first-party installed operating path, not just a sample infographic.
- Why this is / is not agent-owned: The installed personas are explicit external-model-powered actors, and the content of implementation/technical judgments is not determined by a static issue-label script. Hermes owns tools, not the whole delivery governance.
- Evidence: [seed.go L1-145](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/seed/seed.go#L1-L145), [spawn-tm.sh L1-32](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/spawn-tm.sh#L1-L32), [spawn-persona.sh L1-36](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/spawn-persona.sh#L1-L36), [team-manager.md L15-88](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/team-manager.md#L15-L88), [team-manager-tick.md L10-43](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L10-L43).
- Basis: Model-backed first-party materialized actor plus usable task/feedback path.
- Confidence: Medium-high source-structural; live external-model session not run here.
- Caveats: Merely executing `gmh seed` without Hermes gateway/provider/GitHub authorization does not produce completed S1 tasks.

## S2 — Coordination

- State: C
- Function: Prevent destructive interference among independently running builder S1s that would otherwise edit overlapping source paths on parallel sub-issues.
- Disturbance / variety regulated: Simultaneous frontend/backend and same-layer builders can overwrite or break shared files/types and lose incompatible in-flight work.
- Decisive decision or feedback right: The materialized safety check compares actual path-scope/dependency metadata across candidate tasks, blocks uncontrolled overlaps and requires an explicit dependency/serialization or scope adjustment before dispatch.
- Decision owner: The project actor/team manager and author of path-scope/dependency labels choose how to refactor/serialize; first-party sensor computes and enforces the specific interference check. No independent fully autonomous S2 agent decides compromise.
- Supporting / enforcement mechanisms: `path-scope:` and `depends-on:` issue labels, `check-parallel-builders.sh` Python glob overlap analyzer, Sensor 10 and manager predispatch policy.
- Closure path: Multiple ready/in-progress S1 builders → conflict in intended changed file scopes detected → fail/blocked state on missing/disputed scope → manager revises mutual scope/dependency or serializes → safe future builder launches.
- Boundary reachability: Sensor 10's executable shell script calls GitHub to inspect actual issue labels and exits with blocking status for an uncovered overlap, while the installed manager's persona contract requires this check before issuing parallel work. Still requires the installed operator/manager to invoke and heed the gate.
- Why this is / is not agent-owned: Detection is deterministic; the decisive policy/negotiation over which parallel work to delay is supplied by the project manager/label owners. Source provides a specific S2 constructor/enforcement path, not autonomous ownership.
- Distinct S1 units: Independently spawned backend/frontend or multiple builder personas on separate live sub-issues/branches.
- Inter-S1 disturbance: Concrete concurrent edit overlap in paths/definitions (reported as root cause in the first-party Sensor 10 design note; not independently re-enacted).
- Attenuating coordination relation: Block on non-empty `path-scope` intersection without declared `depends-on`, and force disjoint file scopes or explicit serial dependency before the manager starts workers.
- Feedback into subsequent S1 behaviour: Failed executable check prevents uncontrolled concurrent `in-progress` launches; manager must change dependency/path assignments before resuming builder operations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It detects a particular inter-builder source-file interference condition and specifically changes mutual scheduling; not simply following an issue DAG.
- Evidence: [check-parallel-builders.sh L1-210](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/check-parallel-builders.sh#L1-L210), [10-decomposition-safety.md L1-128](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/sensors/10-decomposition-safety.md#L1-L128), [team-manager-tick.md L16-43](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L16-L43).
- Basis: Shipped context-dependent inter-S1 conflict detector and constructor routing; incomplete autonomous compromise ownership.
- Confidence: Medium source-structural; glob overlap is heuristic and actual live `gh` queries were not reproduced.
- Caveats: Missing `gh` or `jq` fails the check; manager must actually invoke the sensor in its installed mode. A comment-only division without enforceable predispatch use would not by itself establish S2.

## S3 — Inside-and-now control

- State: A
- Function: Govern the current delivery project across ongoing independent specialist work cells by tracking the whole issue/PR state and making present assignments, commitment/intervention and closure decisions.
- Disturbance / variety regulated: Conflicting current priorities, stalled domain refinement, dead builders, unreviewed PRs, rejected QA, dependencies blocking delivery, excessive parallel workers and missing human validation.
- Decisive decision or feedback right: Configured model-backed `team-manager` reads open GitHub Issues/PRs at every cron tick, selects issue type/persona/branch, moves labels, limits worker concurrency, prompts failed/rejected work, defers blockers and determines when the project task is eligible for final delivery/human validation.
- Decision owner: First-party materialized Hermes `team-manager` model-backed actor, separate from coding-worker personas and provided explicit team-wide current-delivery governance mandate.
- Supporting / enforcement mechanisms: `gmh seed` persona contracts, Hermes cron schedule, GitHub issue state, labels, branches, `gh` CLI, `spawn-tm.sh`, `spawn-persona.sh`, max-three-workers guard, QA and scope sensors.
- Closure path: Whole current issue/PR/blocked/dependency/QA board → model manager chooses updated assignment/constraint/repair → changes GitHub label/branch or spawns named persona → subsequent specialist starts/stops/repairs work → manager sees next returned state and may adjust further.
- Boundary reachability: `loop.CronCommands` creates recurring no-agent launcher of live model-manager plus orchestrator supervisor; installed scripts and materialized role source require actual GitHub state reads and actions, not merely a hand-designed static workflow graph.
- Why this is / is not agent-owned: A bare scheduler periodically launches the manager; the manager, not cron, exercises discretionary current staffing/recovery choices and holds the whole-board view. Removing that actor leaves no contextual policy owner for resolving delivery commitments.
- Whole-system current view: `gh issue list --state open`, `gh pr list --state open`, issue labels/dependencies, QC/CI, waiting/failed workers and progress across the installed project's specialist cells.
- Current-control decision scope: Decide if/which persona works next, maintain max three simultaneous workers, create shared branch, move commitments through states, block or repair stalled work, send QA rejection back to builders and gate closure.
- Evidence: [loop.go L103-164](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/loop/loop.go#L103-L164), [spawn-tm.sh L1-32](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/spawn-tm.sh#L1-L32), [team-manager-tick.md L1-45](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L1-L45), [team-manager.md L1-160](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/team-manager.md#L1-L160), [07-hermes-loop.md L1-92](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/07-hermes-loop.md#L1-L92).
- Basis: Model-backed current whole-project regulator with evidence-returning resource and commitment effects.
- Confidence: Medium-high source-structural, not a claim of user project's real deployment metrics.
- Caveats: The authored role mandate alone is not sufficient; the shipped cron/launcher and tools close its reachability. Source does not prove the manager always obeys the prompt or that a real external Hermes gateway was run in this review.

## S3* — Complementary audit

- State: A
- Function: Independently challenge builders'/manager's ordinary claims of completed work with raw source/CI/tests/acceptance evidence and route failures to current managerial correction.
- Disturbance / variety regulated: Builders may say `pronto` despite failing checks, security holes, missing contracts, visual regressions or incomplete DoD.
- Decisive decision or feedback right: Distinct configured model-backed `quality-assurance` persona reviews the actual PR/DoD, tests/sensors and optional live snapshot, reports `APROVADO` versus `REPROVADO` and places the issue in `qa` or back in `in-review`.
- Decision owner: QA model persona separate from implementing builder and issue-wide team-manager; GitHub CI/sensors provide independent observable facts, not autonomous audit judgment on their own.
- Supporting / enforcement mechanisms: QA persona, source PR diff, DoD issued by architect, static/security/contract/smoke/snapshot sensors, GitHub comments/labels, next manager cron tick.
- Closure path: Builder PR/current completion claim → QA independently loads DoD and actual source/tests/CI → failed finding plus report/label `in-review` → model manager notices returned state and spawns builder for repair → new PR status/review. Pass returns `qa`, leading to human acceptance/merge control.
- Boundary reachability: `team-manager-tick.md` explicitly spawns QA when PR+CI is ready and explicitly spawns a builder on rejected QA; `quality-assurance.md` defines executable commands, code/DoD inspection and label-producing return actions. Applies in the materialized first-party project flow.
- Why this is / is not agent-owned: A separately prompted QA specialist reads evidence rather than trusting the builder summary, forms an accept/reject judgment, and triggers corrective action through a distinct manager. Sensor exit codes are supporting evidence only.
- Claim being audited: A coding persona's claimed implementation/PR readiness and fit to architecture-defined DoD.
- Ordinary reporting path: Builder's branch/PR, completion comment, issue label `in-progress`/in-review and claimed tests.
- Complementary access path: QA accesses raw branch/diff, code tests/security/contract/smoke checks and possible actual running snapshot independent of the implementer report.
- Independence boundary: Distinct persona and process dispatched after builder, separate QA report; may share Hermes model vendor/infrastructure, so not vendor-independent.
- Who acts on findings: Team-manager reassigns the builder on a rejected QA result, withholds merge pending green checks and/or human acceptance.
- Evidence: [quality-assurance.md L1-160](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/quality-assurance.md#L1-L160), [team-manager-tick.md L17-40](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/scripts/loop/team-manager-tick.md#L17-L40), [02-pull-request.md L41-133](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/02-pull-request.md#L41-L133).
- Basis: Independent source/acceptance observation with active corrective return to current management.
- Confidence: Medium-high conditional on configured Hermes and project test tools.
- Caveats: Source does not demonstrate that listed external snapshot/Gatling/tool commands are installed in every adopter; source-specific QA decision and repair return, not every illustrative test, support the function.

## S4 — Outside-and-then intelligence

- State: C
- Function: Form future-oriented persona/skill improvement options from previously observed external project issue/comment evidence, with a first-party prescribed *handoff* but no self-contained completed autonomous application.
- Disturbance / variety regulated: Repeated missing acceptance criteria, weak DoD, domain persona gaps, missing skills and changing project delivery needs.
- Decisive decision or feedback right: Deterministic `evolve.Propose` selects issue-comment snippets by keyword and drafts suggested persona/skill patch prompts; a separate model-backed Hermes manager could choose actual changes and a human must explicitly validate before modifications. No in-product autonomous change/commit decision is made by this CLI.
- Decision owner: CLI's keyword extraction and prospective proposal scaffold is first-party; decisive editing/adoption remains with external composed Hermes actor plus human approval. Hence `C` and not `A`, `A(P)` or `P`.
- Supporting / enforcement mechanisms: Issue/comment JSON fixtures, `harness/memory/traces/<utc>`, deterministic `proposal.md`, `PROMPT.md`, (--apply) only persistent trace write and explicit human validation instructions.
- Closure path: Historical issue/PR comments → deterministic keyword/signal extraction → written prospective persona/skill adjustment `proposal.md` → human/Hermes handoff in `PROMPT.md` → *possible* approved persona/skill update → next project's persona execution. **Return is documented as a required external composition, not executed within `gmh evolve`.**
- Boundary reachability: Shipped `gmh evolve --from-dir ... --apply` creates concrete trace and change prompt artifacts and existing `harness/workflow/08-persona-evolve.md` specifies who may act on them; however this command intentionally does not rewrite persona files and the model runtime/approval handoff is not natively executed, so no autonomous S4 closure is claimed.
- Why this is / is not agent-owned: Keyword matching and prompt text generation are deterministic, not an agent choosing/accepting new future capability. The installed manager could respond to prompt only as separately composed external agent/user behaviour.
- External distinction: GitHub issue/comment records reflect actual project/domain gaps and user acceptance problems from previous delivery, not an internal same-action memory reset.
- Future / prospective distinction: Proposed edits target the persona/skill library for **later issues**, rather than simply retrying the current PR.
- Adaptation option generated: Suggested changes to skill/persona instructions derived from historical AC/DoD/persona gap references, recorded for later human/editor decisions.
- Path back into current capability / S3: `PROMPT.md` → external Hermes manager → required human `validado` → changes in `harness/personas/` or `harness/skills/` → future manager/builder ticks. This path is **specified but not source-executed**, a concrete constructor gap preventing A.
- Evidence: [evolve.go L1-187](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/evolve/evolve.go#L1-L187), [evolve.go L1-92](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/cmd/evolve.go#L1-L92), [08-persona-evolve.md L45-112](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/08-persona-evolve.md#L45-L112), [EVOLVE docs](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/docs/EVOLVE.md).
- Basis: First-party future-capability proposal and explicit constructible parent/agent-return path, not closed autonomous adoption.
- Confidence: High on deterministic source limits, medium on hypothesized later handoff.
- Caveats: `--apply` only writes traces and prompts. A README claim of evolving personas is not evidence they were changed; the human approval contract should not be counted as executed action.

## S5 — Policy and identity

- State: —
- Function: No established legitimate ultimate organizational purpose/identity decision over the delivery organization is made and returned through this first-party harness.
- Disturbance / variety regulated: User requirements, project-specific persona names, GitHub merge protections and ordinary human acceptance can limit delivery but do not necessarily present a contested constitutional purpose/identity decision.
- Decisive decision or feedback right: Human specifies project requirements and may validate release/persona edits, while software enforces workflow stages; no first-party S5 actor legitimately resolves whole-system purpose conflicts and returns a revised ultimate policy.
- Decision owner: The product adopter's true organizational leadership is outside the scoped generated delivery system, while team-manager's authority is **current delivery S3** rather than supreme mission-setting S5.
- Supporting / enforcement mechanisms: `docs/SPEC.md`, `PROJECT.md`, `harness/AGENTS.md`, GitHub PR protection, `validado` instruction and CLI persona domain policies.
- Closure path: User spec / final acceptance → current delivery limits; missing legitimate identity/purpose conflict → terminal rightful decision → revised system-wide organizational identity applied to future operations.
- Why this is / is not agent-owned: Team manager routes development work; human PR approval and static constraints do not adjudicate legitimacy or constitutional identity simply because they can veto a merge.
- Evidence: [seed.go L1-145](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/cli/internal/seed/seed.go#L1-L145), [team-manager.md L1-85](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/personas/team-manager.md#L1-L85), [08-persona-evolve.md L68-112](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/08-persona-evolve.md#L68-L112), [02-pull-request.md L85-120](https://github.com/brenonaraujo/git-meta-harness/blob/167b13c66993fa0a5216e4be2fc9bf911cd02cf8/harness/workflow/02-pull-request.md#L85-L120).
- Basis: Source-first bounded absence.
- Confidence: Medium-high.
- Caveats: A customer organization may exercise real S5 elsewhere. Its existence does not flow into this product merely because someone provided a product spec.

### Absence scope

- Surfaces inspected: Seed/new/adopt entrypoints, manager and specialist personas, user validation guidance, GitHub merge/approval policy and evolve workflow.
- Plausible first-party paths checked: Current manager making project-political decisions, human persona change approval as parent ultimate policy, changed product spec applied through team-manager.
- Why no material first-party path remains: Reviewed decisions concern workload routing, code/feature correctness, standard release acceptance or future persona proposals. No actual purpose/identity-level conflict with a distinct legitimate S5 decision and returned whole-organization guidance is supplied.

## Recursion

The installed project team, not the top-level Go CLI, is the declared organization. Each coding persona's model/tool loop is operational S1; sensor-managed overlapping files are inter-S1 conflict control; team-manager's whole GitHub board is S3; QA owns independently corrective evidence; `gmh evolve` prepares future team capability proposals but returns authority outside its own code. External Hermes provider and source authors' company are not extra inferred S1/S5 cells.

## Variety and escalation

Specialist actors absorb local task variance; dynamic issue/PR state lets team-manager absorb current workload variety. Sensor 10 blocks conflicting simultaneous builders; QA reporting can force rework despite implementer assurances. `gmh evolve` gathers future-facing user/project evidence but does not install the new persona automatically. Ordinary `blocked` labels and release approvals are not assumed to be algedonic or ultimate-policy mechanisms.

## Evidence gaps

- Exact Git source ref `167b13c66993fa0a5216e4be2fc9bf911cd02cf8`, MIT, clean checkout. **13 shell files passed `bash -n` and bundled Python visual helpers passed compileall**. Isolated VM has **no Go toolchain**, so no `go test ./...` was performed. No Hermes gateway, coding-model completion or real GitHub project run claimed.
- Positive S3 and S3* are source-wired **model-backed installed profile operating modes**; they require real external runtime authorization and provider setup. They are not merely brand marketing, but their empirical delivery quality is not attested.
- S2 is graded `C`: sensor is a concrete first-party inter-builder path-overlap regulator yet requires manager dispatch and human/project scope metadata; overlap matcher uses heuristic generated file candidates and can miss collisions.
- S4 is only `C`: `gmh evolve --apply` writes trace/prompt artifacts, not persona modifications, and the future acceptance/return is manually composed. Default install is not an autonomous self-improving system.

