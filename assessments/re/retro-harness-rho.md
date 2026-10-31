---
harness_id: retro-harness-rho
project_name: retro-harness / RHO
repository: https://github.com/wbopan/retro-harness
review_ref: e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# retro-harness / RHO

## Review boundary

- System in focus: the MIT first-party retrospective harness evolution workflow (`rho evolve`, packaged Codex and Claude Code variants) at the pinned revision; external Codex/Claude model runtimes are worker dependencies, not inherited management.
- Purpose and identity: mine previous task trajectories, propose reusable harness changes, compare candidate-versus-incumbent work, and optionally install a preferred persistent harness for future agent tasks.
- Relevant environment: real past user tasks and session traces, failed solves, inconsistent task handling, variable task difficulty, external CLI/provider execution and quality feedback.
- Standard-distribution boundary: Python `src/rho/` evolution engine and packaged `codex/retrospection.py` / `.claude/workflows/retrospection.js` compositions; dataset graders, external agent internals, paper benchmarks and research results are outside first-party ownership.
- Credited operating / distribution surfaces: `rho evolve` round loop, model-backed proposal and pairwise self-preference evaluation, candidate harness store, winner gate; Codex/Claude project retrospection uses isolated probes and backed-up apply.
- Adjacent first-party surfaces excluded from ownership: held-out reporting, benchmark data adapters, figure-building scripts, WebUI and paper result tables; these do not establish independent management or audit autonomy.
- First-party operating / deployment modes considered: Python `rho evolve` driving configured external Codex as its decision-making actor; packaged Codex CLI project retrospection; packaged Claude Code dynamic workflow. The latter two are supported operator-triggered compositions rather than a continuously running autonomous daemon.
- Recursion level: one harness-evolution cell with multiple task probes; hosted coding agents and customer projects are separate systems-in-focus.
- Reviewed revision: `e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python evolution loop runs repeated task solves under a baseline harness, supplies trajectories to a model-backed proposal strategy, stages alternative harness versions, re-solves tasks under candidates, asks an agent to compare before/after trajectories, and accepts the candidate with highest positive mean preference. Persistent trajectory and content-addressed harness stores isolate successive versions. The Codex and Claude packaged project workflows mine existing sessions, diagnose failure patterns, stage candidate `AGENTS.md`/skills or `CLAUDE.md`/memory/scripts, run isolated project probes, and only apply an accepted winner with backups. A separate judging call is part of the same ordinary optimization selection path; it is not an independently mandated complementary audit of a whole-system executive.

Pinned primary evidence:

- [Runnable modes, first-party boundary and retrospective pipeline](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/README.md)
- [Round execution, candidate pool, preference gate and iteration](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/src/rho/loop.py)
- [Model-backed task-agnostic candidate proposals from task traces](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/src/rho/strategies/trajectory.py)
- [Pairwise trace comparator and score parsing](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/src/rho/orchestrators/evaluate.py)
- [Content-addressed versioned harness capture](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/src/rho/stores/harness.py)
- [Codex variant's stage, probe, winner and backed-up apply](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/codex/retrospection.py)
- [Claude Code dynamic workflow with future-task-oriented memory/skill changes](https://github.com/wbopan/retro-harness/blob/e5f2d1a8a06ab3523ab42e0042d2fa13d9acb701/.claude/workflows/retrospection.js)

## Operational model

An operator selects a dataset or an existing project/session history. A hosted model-backed agent performs task solves and edits proposed harness files under first-party prompts and staging boundaries. RHO compares the resulting trajectories; deterministic aggregation selects whether to retain the incumbent or adopt a candidate. A retained harness changes later task-agent behavior in the selected project. Parallel probes and isolated worktrees are evaluation work, not autonomous organizational departments whose ongoing interference is managed as S2.

## S1 — Operations

- State: A
- Function: model-mediated task execution and reusable harness change proposal in a retrospective optimization episode.
- Disturbance / variety regulated: unknown task failures, differing agent trajectories, weak project instructions and tool/skill mismatch.
- Decisive decision or feedback right: choose task-solving actions and author candidate persistent instructions/tools in response to trajectory diagnosis.
- Decision owner: externally executed model-backed Codex/Claude actors *composed by the first-party RHO workflow*; RHO itself owns the sequencing, artifacts and eligibility rules, not the models' general internals.
- Supporting / enforcement mechanisms: `rho` CLI, workspace staging, trajectory readers, optimize prompts, versioned harness store and rollout executor.
- Closure path: prior tasks/trajectory → model diagnosis/proposal → new staged harness → trial result → a next model proposal or accepted artifact.
- Boundary reachability: `rho evolve` invokes `run_evolution`/`run_round` and the shipped `TrajectoryStrategy.propose_candidates` calls the configured `Agent.run`; packaged Codex/Claude retrospection runs analogous external agent calls with first-party orchestration.
- Why this is / is not agent-owned: selected code/instruction improvements and task actions are not enumerated by deterministic rules; authored adapters stage and evaluate the model decisions.
- Evidence: pinned `loop.py`, trajectory strategy, Codex/Claude workflows above.
- Basis: explicit and structurally reachable in supported configured-agent mode.
- Confidence: high for decision ownership, not for quality.
- Caveats: no Codex/Claude agent, benchmark or live project was executed during this review.

## S2 — Coordination

- State: —
- Function: no materially independent relation regulating interference between several continuing organizational S1 business units is demonstrated.
- Disturbance / variety regulated: parallel task and candidate probes could collide in a workspace, but the reviewed system treats them as isolated experimental trials.
- Decisive decision or feedback right: first-party worktree/temporary workspace isolation and parallel call limits avoid file collisions as run machinery.
- Decision owner: constructor-written orchestration utilities; no S2-specific adaptive coordination right across viable peer operations is shown.
- Supporting / enforcement mechanisms: `solve_workspace`, parallel mapping, separate candidate directories and Git worktrees.
- Closure path: independent probes complete into the same round comparison; there is no inter-S1 conflict feedback that alters peer operating relations.
- Why this is / is not agent-owned: a model solves each task, but isolation of replicated benchmark runs is not evidence of a distinct S2 coordination institution.
- Evidence: pinned `loop.py`, Codex/Claude probe isolation code.
- Basis: scoped negative after checking possible parallel-worker paths.
- Confidence: medium-high.
- Caveats: deployments can embed RHO in a larger multi-agent organization, but that parent S2 is not inherited.

### Absence scope

- Surfaces inspected: core round parallelism, candidate trial workspaces, Codex/Claude project worktrees and score aggregation.
- Plausible first-party paths checked: test/task workers as separate S1 departments, worktree isolation as cross-S1 conflict arbitration, candidate fan-out as S2.
- Why no material first-party path remains: trials converge to one experiment/winner and are isolated for reproducibility, without a shipped peer-unit interference signal and corrective coordination return beyond deterministic evaluation scheduling.

## S3 — Inside-and-now control

- State: C
- Function: preserve current harness integrity and exercise present portfolio control over candidate adoption across the configured task set.
- Disturbance / variety regulated: candidate regressions, unusable comparison responses, contradictory per-task preference and risky writes to persistent project guidance.
- Decisive decision or feedback right: choose the accepted candidate by aggregated preference, reject nonpositive/invalid evidence, and retain or replace the active harness.
- Decision owner: constructor-defined `run_round` winner/threshold logic; Codex/Claude self-preference models supply evidence but do not have unconditional commit authority.
- Supporting / enforcement mechanisms: per-candidate scores, content-addressed harness store, task-level probe records, backups and optional `--no-apply` flag.
- Closure path: all candidate/task trial results → computed mean score and winning threshold → accepted harness becomes `current` for next round, or original persists; packaged project workflow applies with backup only on acceptance.
- Boundary reachability: `run_evolution` updates `current` only when `RoundResult.accepted`; `codex/retrospection.py` selects positive winners and invokes `apply_candidate` only in permitted mode.
- Why this is / is not agent-owned: the acceptance/rollback rule is explicit source-defined governance over the present set of alternatives, not agent improvisation or a free-form judge instruction.
- Whole-system current view: all candidate trajectories, per-task scores, mean scores and the current harness version within one retrospective evolution run.
- Current-control decision scope: active harness commitments for the current experiment/project, not user policy or external production release ownership.
- Evidence: pinned round loop, self-preference evaluator, harness store and project variant above.
- Basis: explicit constructor control over a closed cross-candidate result path.
- Confidence: medium.
- Caveats: this is a bounded evolution-project S3, not a company-level governance hierarchy.

## S3* — Complementary audit

- State: —
- Function: self-preference evaluation is an ordinary selection input, not a complementary audit of management's picture by a materially separate challenger.
- Disturbance / variety regulated: poor trajectory quality, model confidence and agent-generated candidate regression.
- Decisive decision or feedback right: independent audit would require separate evidence access and corrective findings distinct from ordinary candidate scoring; that path is not established.
- Decision owner: `evaluate()` invokes the same configurable `Agent` interface as task solving and proposal, and its score is directly consumed by normal selection.
- Supporting / enforcement mechanisms: before/after trajectory prompt, optional candidate order reversal, JSON score parsing and mean preference threshold.
- Closure path: score → ordinary winner selection; no separate complementary audit verdict addressed to an S3 manager or corrective reinspection loop.
- Why this is / is not agent-owned: the judging call is model-driven but not independent S3* ownership merely because it uses a role-specific prompt and rereads traces.
- Evidence: pinned `orchestrators/evaluate.py`, `loop.py` and packaged project workflows.
- Basis: independence and ordinary-gate distinction.
- Confidence: medium-high.
- Caveats: externally imposed auditing could challenge these evaluations but is outside the frozen distribution.

### Absence scope

- Surfaces inspected: pairwise score function, candidate selection, source/target harness reads, no-ground-truth retrospection and output reports.
- Plausible first-party paths checked: evaluator-as-independent-auditor, model self-consistency comparisons, isolated worktree trials as audit and held-out benchmark grading.
- Why no material first-party path remains: each is part of routine experiment selection or adjacent research grading, with no independently governed S3 claim challenge and returned corrective audit mechanism.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert accumulated externally encountered task/session failures into transferable, prospective harness capabilities for later tasks.
- Disturbance / variety regulated: shifting real project task types, recurrent error patterns and declining relevance of static instructions or skills.
- Decisive decision or feedback right: diagnose generalizable failures and choose future-task-oriented edits to persistent guidance, memory and tools.
- Decision owner: configured model-backed diagnosis and optimization calls in the supported first-party retrospective workflows; constructor gates decide activation.
- Supporting / enforcement mechanisms: session/trajectory mining, diverse coreset, task-agnostic optimization prompt, candidate staging, self-preference probe and backup/apply.
- Closure path: prior environmental task histories → model-derived transferable guidance/tool options → staged candidate evaluation → accepted persistent harness update → later real agent sessions consume changed capability.
- Boundary reachability: both `TrajectoryStrategy` and packaged Codex/Claude workflows explicitly ask for general improvements to the harness for *future tasks*, and `run_evolution`/`apply_candidate` adopt a winning version.
- Why this is / is not agent-owned: models generate the adaptive hypotheses and edit contents; a positive threshold and backups merely regulate which options may become active.
- External distinction: historical genuine task/session trajectories supply outside-workload evidence, not only the current response's scratchpad.
- Future / prospective distinction: proposed rules, skills and scripts are task-agnostic persistent capability changes for tasks not yet run, distinct from retrying the failed prior task alone.
- Adaptation option generated: candidate versions of `AGENTS.md`/skills or `CLAUDE.md`/memory/scripts, as well as general harness files in the Python engine.
- Path back into current capability / S3: the score-positive winner replaces the current harness and changes the context/tools available to subsequent operations; a rejected candidate cannot change the active version.
- Evidence: pinned trajectory prompt, run loop, Codex/Claude project workflows.
- Basis: explicit model-selected prospective capability construction and returned adoption.
- Confidence: medium-high for the supported retrospective evolution mode.
- Caveats: there is no claim that RHO monitors broad markets or autonomously sets a product strategy; the S4 horizon is future task execution in the target project.

## S5 — Policy and identity

- State: —
- Function: no final autonomous or parent-return constitutional policy authority is shipped within the declared harness optimization program.
- Disturbance / variety regulated: the project owner's objectives, permissions, task ethics, provider setup and desired update scope.
- Decisive decision or feedback right: owner decides whether/when to run retrospection, what project to target and whether automatic apply is allowed.
- Decision owner: external operator / project authority; first-party code only enforces these parameters.
- Supporting / enforcement mechanisms: explicit `apply`/`--no-apply`, CLI model selection, filesystem backups, project path boundaries.
- Closure path: operator provides allowed scope and flags → workflow stages/evaluates edits → optionally applies; no identity-level problem → legitimate higher authority → binding mission/policy decision → returned system-governing change is implemented as an organizational S5 loop.
- Why this is / is not agent-owned: updating task instructions or persistent skills for performance does not grant the optimizer the right to redefine the user's legitimate ultimate purpose.
- Evidence: pinned CLI and project workflow parameter/apply code.
- Basis: bounded negative authority test.
- Confidence: high.
- Caveats: project-level human S5 may exist outside this system-in-focus.

### Absence scope

- Surfaces inspected: `rho` CLI, Codex/Claude workflow arguments, harness apply/backup code, external agent provider interface and candidate-selection gates.
- Plausible first-party paths checked: automatic harness edit as identity change, model preference as final policy, user approval/apply as parent S5 mode.
- Why no material first-party path remains: these mechanisms optimize a task-oriented harness under an externally selected project/purpose, without an owned ultimate-policy adjudicator or an explicit parent identity-decision feedback loop.

## Recursion

RHO's evolving harness may later govern a separate coding agent, but the tested coding tasks are sampled probe operations rather than child viable systems whose S2/S3/S5 functions RHO inherits. The standing project owner is external to the RHO optimization cell.

## Variety and escalation

Historical trajectories amplify candidate failure modes; coreset selection, worktree isolation, before/after comparison and the positive-mean gate attenuate the search. Failed or nonpositive candidates leave the old harness untouched. No automatic independent auditor, constitutional policy channel or new authority is inferred.

## Evidence gaps

- Static code/prompt examination at pinned SHA; no hosted Codex/Claude run, API credential, live task execution or benchmark replication.
- Source shows distinct judging calls but not the independently governed complementary access and corrective mandate needed for S3*; evaluator quality claims are not borrowed from paper results.
- S4 is limited to task-agnostic future project capability changes based on real session histories; continual wider-environment sensing is not claimed.

## Assessment summary

Proposed `included`: model-authored task/harness operations (S1=A), constructor-defined present candidate adoption (S3=C) and agentic future-task harness adaptation (S4=A). Parallel probes do not establish S2, self-preference is not independent S3*, and ultimate policy remains outside. Vector **A · — · C · — · A · —**.
