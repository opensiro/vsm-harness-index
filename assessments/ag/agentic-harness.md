---
harness_id: agentic-harness
project_name: Agentic Harness
repository: https://github.com/skrvidz/agentic-harness
review_ref: c67b6cec088d8f0054d9626adad6a22ea87fdbd6
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agentic Harness

## Review boundary

- System in focus: The local Python `rector_harness` executor/reviewer loop and optional planner-mode ticket organization acting on one target Git project.
- Purpose and identity: Deliver an engineer's requested project change via successive model-led edits, evidence-backed independent review, revision or human escalation; optional plan mode decomposes and evaluates the integrated goal.
- Relevant environment: A human objective/acceptance criteria, existing target project, its Git working tree, configured test command, installed Claude/Codex CLI agents, local SQLite/transcript state and human intervention.
- Standard-distribution boundary: Installed CLI/workspace TUI, `Harness` execution engine, `PlanHarness`, subprocess runner configurations, prompts, evidence collection, saved state and recovery. The external Claude/Codex client internals and upstream model abilities are not credited.
- Credited operating / distribution surfaces: [engineer-review control](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py), [review/planner prompts](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/prompts.py), [model runner policies](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/runner.py), [direct evidence](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/evidence.py), [DAG control](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py).
- Adjacent first-party surfaces excluded from ownership: Development tests, visual animation source, UI screenshot/diagrams, local dry-run scripted agents, GitHub read-only context panel, and external terminal-agent internal controls. Dry-run mocks support protocol testing, not live agent decisions.
- First-party operating / deployment modes considered: Single engineer/reviewer loop with revisions/decisions/resume; headless non-interactive pause; optional planner-generated ticket DAG with isolated parallel worktrees and final integrated evaluation; ad hoc read-only reviewer questions.
- Recursion level: One project goal as organization; engineer turns or ticket engineers are S1 operations, separate model review/planning provides metasystem feedback, but no second viable business recursion is credited.
- Reviewed revision: `skrvidz/agentic-harness@c67b6cec088d8f0054d9626adad6a22ea87fdbd6` (MIT).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Python harness launches selected external engineer and reviewer CLI processes as independent noninteractive subprocess turns; default fresh Codex reviewer sessions are `--sandbox read-only`, whereas engineer CLI receives editing permission. Each engineer turn persists its summary and sets `next_actor=reviewer`, even at a configured cycle boundary. `collect_evidence` independently reads target Git status/diff/untracked files and runs the selected project tests when present. The reviewer receives both the untrusted engineer summary and direct working-tree evidence, returns a schema-limited verdict and findings, and the harness converts `REVISE` into new engineer task feedback, `APPROVED` into its proposed next increment, `DONE` into completion, and `NEEDS_HUMAN` into a persisted human gate. SQLite/transcripts and explicit `next_actor` support restart.

Optional `PlanHarness` obtains a model-authored, validated dependency DAG, schedules ready tickets with bounded parallelism and clean worktree isolation, runs an engineer-review loop per ticket, integrates completed branches and invokes the distinct read-only planner again to evaluate the full integrated objective; a failed merge/blocked dependency pauses instead of silently moving work. These first-party modes are reachable from the documented CLI/TUI, not merely library extension hooks. See [engine](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py#L44-L175) and [planner](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py#L230-L435).

## Operational model

The engineer chooses edits/actions for the current goal; a separately launched reviewer reads project reality and makes verdict/next-work decisions. The engine changes future engineer instructions based on those verdicts. Plan mode adds model-generated task decomposition, per-ticket isolation and final whole-goal review, but its static DAG concurrency/dependency gates are not themselves evidence of S2 peer oscillation control. Human decisions and terminal-client sandbox rules constrain these model rights.

## S1 — Operations

- State: A
- Function: Model-led project implementation via Claude or Codex engineer turns, including tool/repository feedback and task revision.
- Disturbance / variety regulated: Changing local source and tests, uncertain implementation requirements, reviewer defects, failed commands and subsequent model observations.
- Decisive decision or feedback right: Choose code edits, test/inspection commands, interpretation of feedback and implementation strategy inside the supplied objective/current task.
- Decision owner: Spawned engineer model CLI as explicit task-operating actor, bounded by `Harness` and its model/tool permissions.
- Supporting / enforcement mechanisms: `ClaudeRunner`/`CodexEngineerRunner`, persistent state, per-run worktrees, test evidence, max-cycles and reviewer feedback file.
- Closure path: Human objective → engineer model turn and code edits → terminal/tool feedback → engine captures outcome → separate review → revised task fed into next engineer turn or final result.
- Boundary reachability: `agent-harness run` and workspace Run create a real engineer subprocess, while `--dry-run` is explicitly separate and not credited for autonomous operation.
- Why this is / is not agent-owned: Engineer model chooses substantive implementation; removing it leaves only runner/orchestration and scripted test fixtures.
- Evidence: [CLI invocation](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/README.md), [subprocess runners](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/runner.py#L31-L113), [engineer turn](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py#L66-L96).
- Basis: structural first-party executable path.
- Confidence: High for decision-loop wiring, medium for actual provider behavior without an authenticated run.
- Caveats: The harness does not implement provider transport; installed authenticated CLI models are required outside dry-run.

## S2 — Coordination

- State: —
- Function: No qualifying S2 loop that detects operational-unit interaction-induced disturbance and returns attenuation into independent peer behavior.
- Disturbance / variety regulated: Parallel plan tickets may conflict during Git integration, or dependencies may block scheduling; these are prevented/flagged by fixed isolation/dependency checks.
- Decisive decision or feedback right: Static scheduler selects ready DAG nodes; merge conflicts fail/pause rather than a distinct S2 coordinator negotiating or adapting peer commitments.
- Decision owner: Model planner authored the initial task graph; deterministic `PlanHarness` enforces it with fixed width, worktrees and merge checks.
- Supporting / enforcement mechanisms: Validated `depends_on`, `ready[:width]`, bounded `asyncio.gather`, isolated `TicketWorkspace` and fail-on-conflict integration.
- Closure path: Plan → independent ticket loops → deterministic merge or pause; no observed conflict signal → inter-S1 attenuation decision → peer behavior correction path.
- Why this is / is not agent-owned: A dependency graph and isolation are generic task sequencing. Model planning is not proven to monitor competing peers and damp induced interference during current execution.
- Evidence: [DAG scheduler](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py#L230-L265), [worktrees/merge](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py#L147-L197).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: Model could have chosen safer dependencies ex ante, but a hypothetical conflict-attenuation behavior is not an evidenced first-party closed S2 loop.

### Absence scope

- Surfaces inspected: Model-created DAG, readiness scheduler, worktree isolation, merge conflict return and per-ticket reviewer feedback.
- Plausible first-party paths checked: Parallel task dependency control as S2, independent worktree conflict avoidance, integration merge error as peer-disturbance signal, reviewer revisions as coordination.
- Why no material first-party path remains: The only cross-ticket checks are static readiness/isolation and error/stop on merge conflict; reviewer corrections address per-ticket quality, not peer interference attenuation.

## S3 — Inside-and-now control

- State: A
- Function: Current-goal control of implementation commitments and task direction based on whole-run state and independent evidence.
- Disturbance / variety regulated: Code that does not satisfy goal/acceptance tests, unresolved scope decisions, an incomplete increment, and uncertainty whether a wider ticket plan achieved the objective.
- Decisive decision or feedback right: Reviewer decides `APPROVED` with a next task, `REVISE` with required changes, `DONE` or `NEEDS_HUMAN`; the plan-level evaluator judges the integrated project against the whole original objective and may pause delivery.
- Decision owner: Dedicated reviewer model for the single-run organization; in plan mode, dedicated planner/final-evaluator model for whole-ticket commitment judgment. Harness applies decisions to future task/current status.
- Supporting / enforcement mechanisms: Typed review schema, recorded run state/criteria, feedback file, `next_actor` transition, bounded cycle budget, SQLite event artifacts and final-plan evaluation.
- Closure path: Current project evidence + engineer work → reviewer compares objective/criteria → chooses revision/next increment/completion/human gate → engine adjusts the next S1 task or stops. In DAG mode, integrated ticket results and source evidence → planner's final verdict → whole-goal completion or pause.
- Whole-system current view: `reviewer_prompt` receives the complete current objective/criteria and source-backed diff/status/test evidence; `planner_final_prompt` additionally receives every ticket outcome, full plan and integrated-repo evidence.
- Current-control decision scope: Approve a sound increment and redirect the next task, require corrective rework, declare current run complete or require human decision; final plan acceptance can be withheld. This is discretionary present-task commitment control, not a deterministic max-cycle or width guard.
- Boundary reachability: Every default engineer turn is followed by reviewer control in `Harness.run_async`; plan mode invokes final model evaluation after all ticket integrations.
- Why this is / is not agent-owned: The model selects the quality/commitment verdict and next operational instruction from evidence; the Python engine merely branches on the verdict to update S1 commitments. Parent human involvement is a pause/answer gate, not claimed as a separate S3(P) mode.
- Evidence: [review verdict and actions](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py#L97-L177), [current-state prompts](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/prompts.py), [final planner control](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py#L397-L434).
- Basis: explicit + structural first-party model choice and return path.
- Confidence: Medium-high; model verdict rights are explicit though semantic quality is unobserved in live providers.
- Caveats: No independent fleet budget arbitration claimed; scoped to goal commitment/current work in one configured harness.

## S3* — Complementary audit

- State: A
- Function: Separate evidence-facing review of operational completion claims and test outcomes before continued implementation or acceptance.
- Disturbance / variety regulated: Engineer can confidently report a completed change that fails acceptance criteria, hides untracked files or contains regressions not captured in its summary.
- Decisive decision or feedback right: Read-only reviewer supplies structured findings and `REVISE`/`DONE`/`APPROVED` verdict from direct repository/test evidence; engine records it and routes corrections.
- Decision owner: Distinct Codex reviewer CLI session (fresh read-only sandbox), separate from edit-capable engineer; the independent final planner evaluates integrated evidence in DAG mode.
- Supporting / enforcement mechanisms: `collect_evidence` runs real Git diff/status/untracked listing and optional project test command; review prompt calls engineer text untrusted; Codex `--sandbox read-only` and JSON schema; persisted audit raw artifacts.
- Closure path: Engineer's report → independent evidence capture plus reviewer primary-source inspection → verdict and cited findings → `reviewer_feedback.md`/`current_task` → next engineer turn, or blocked human decision/completion.
- Claim being audited: Work delivered in the active turn meets the stated objective and acceptance criteria and can be accepted as done or as a sound increment.
- Ordinary reporting path: The engineer summary and external CLI stream, persisted as `pending_engineer_summary` and transcript artifacts.
- Complementary access path: Git diff/stat/status and untracked file listing from the actual working tree, configured test-command output and reviewer direct read-only access to the code, plus independent integrated working-tree evidence for final plan review.
- Independence boundary: Separate subprocess agent and session; fresh Codex reviewers start under read-only sandbox, cannot directly modify engineer's work. Captured evidence is provided by harness code, not inferred from engineer text; resumed sessions retain prior policy.
- Who acts on findings: `Harness._apply_review` converts `REVISE` into the next engineer assignment; `NEEDS_HUMAN` forces a human question; `DONE` gates completion. Planner can withhold whole-plan completion.
- Boundary reachability: Review is mandatory after each successful engineer turn in default `Harness`, with `next_actor=reviewer` durable even when the cycle limit is exhausted.
- Why this is / is not agent-owned: Independent evidence-backed reviewer judgments are not the same as generic logs or unit tests; they determine whether the operation is revised, continued or completed.
- Evidence: [evidence collection](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/evidence.py), [read-only reviewer runner](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/runner.py#L57-L86), [review feedback return](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py#L97-L235).
- Basis: explicit + structural independent reviewer path.
- Confidence: High for separation, evidence path and corrective wiring; no provider-backed audit of actual generated changes performed here.
- Caveats: Missing configured test command is marked `unverified`; evidence bounded/truncated to 40k chars, and a read-only CLI sandbox still relies on vendor client enforcement outside the first-party product.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective organizational adaptation that changes future harness capabilities in response to an external environment.
- Disturbance / variety regulated: Future implementation milestones are decomposed from the present task; no separate environmental foresight is continuously collected to change agent organization.
- Decisive decision or feedback right: Model planner defines the current goal's ticket list, but cannot alter the harness's future capability, governance or strategy; user changes model/settings manually.
- Decision owner: Planner for near-term task plan and human for future system configuration; no S4 actor established.
- Supporting / enforcement mechanisms: DAG plan/review, stored transcripts and model selection configuration.
- Closure path: Goal → model-authored near-term tickets → implementation; no future environment scan → adaptation option → selection → return to future operating capability.
- Why this is / is not agent-owned: Time-ordered ticket planning is present operational decomposition, not strategic outside-and-then environmental intelligence.
- Evidence: [planner prompt](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/prompts.py#L37-L112), [DAG execution](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/planner.py#L230-L314).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: An outside organization could adopt findings to redesign its tooling, but that return is not wired in the assessed package.

### Absence scope

- Surfaces inspected: Planner/engineer/reviewer prompts, persisted state, DAG planning, provider/model selection and README.
- Plausible first-party paths checked: Task DAG as future planning, final evaluator as product roadmap, persisted transcript as learning, user-adjusted run configuration as strategic adaptation.
- Why no material first-party path remains: Choices regulate one present goal and its increments; no first-party pathway performs environmental future distinction and consequential organization-level capability adaptation.

## S5 — Policy and identity

- State: —
- Function: No recurring ultimate organizational identity and policy arbitration loop within the product.
- Disturbance / variety regulated: Unsafe edits, unsupported decisions and risky plan changes are bounded by configured CLI sandbox/limits and human pause.
- Decisive decision or feedback right: Human sets objective and decides blocked product/scope questions; no first-party actor adjudicates enduring identity or constitutional policy.
- Decision owner: Human user for objective and particular decision; editor/CLI sandbox for fixed access bounds.
- Supporting / enforcement mechanisms: Human decision callback/CLI, max cycles, explicit noninteractive pause, read-only reviewer setting and worktree constraints.
- Closure path: Risk/product question → human decision → next engineer task, or configured hard limit → pause; neither constitutes policy identity dispute → ultimate arbitration → binding organizational-policy change.
- Why this is / is not agent-owned: Operational question/approval and fixed sandbox policy are not S5 policy-authority decision rights.
- Evidence: [human decision handling](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/rector_harness/engine.py#L137-L175), [README safety boundary](https://github.com/skrvidz/agentic-harness/blob/c67b6cec088d8f0054d9626adad6a22ea87fdbd6/README.md).
- Basis: bounded structural absence.
- Confidence: High.
- Caveats: User's employer or external host may retain ultimate policy authority outside this local harness.

### Absence scope

- Surfaces inspected: Objective/config editor, model prompts, review/human states, CLI runner permissions and planner.
- Plausible first-party paths checked: Human goal as mission policy, `NEEDS_HUMAN` as S5 escalation, read-only sandbox as binding constitution, goal completion as identity decision.
- Why no material first-party path remains: These are task scope, implementation risk and permissions decisions; none is an identity/ultimate-policy dispute with enduring constitution-level feedback.

## Recursion

The optional DAG creates independent operational ticket loops and integrates their output into one project goal. The overall planner/reviewer layer has a visible cross-ticket perspective, but tickets are not proven fully viable independent organizations with their own S2–S5 loops. Hence do not infer another recursion level from ticket multiplicity alone.

## Variety and escalation

Engineer model selection and multiple tickets amplify implementation variety. Read-only reviewer and structured verdicts attenuate unjustified completion claims. The engine routes corrections as new S1 work, while the planner decomposes and checks the integrated task. Human questions, cycle limits and merge failures pause rather than invent automatic authorization. No algedonic organizational channel beyond these bounded task escalations is claimed.

## Evidence gaps

- Assessed pinned first-party implementation and shipped CLI/TUI modes; did not execute a real authenticated Claude or Codex engineer/reviewer on an external target repository. Unit tests/dry runs cannot certify live agent quality.
- New reviewer sessions are explicitly read-only; restored sessions inherit the original CLI policy and rely on vendor semantics, not a first-party kernel sandbox.
- `collect_evidence` truncates outputs and optional test commands may be absent; a reviewer must treat incomplete test evidence as unverified.
- Bounded negative results apply to installed local harness, not external teams operating it.
