---
harness_id: orch
project_name: orch
repository: https://github.com/fbrubacher/orch
review_ref: 16960b40ed6293e27e4536bbd99d62989264a87e
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# orch

## Review boundary

- System in focus: Shipped Python `orch` single-task autonomous coding workflow comprised of four model-backed roles and optional finalizer.
- Purpose and identity: Perform operator-specified repository changes, validation and review with a routing/planning/executor/reviewer model tool loop.
- Relevant environment: Python runtime, OpenRouter-compatible model endpoint/credentials, filesystem and git target repository, optional local `gh` for PR submission, external provider and operator.
- Standard-distribution boundary: `main.py`, `orchestrator/*`, `agents/*`, `models/openrouter.py`, `tools/*`, schemas, prompts and shipped skills. Includes optional `--resume` checkpoint mode and configured PR finalizer. The local target repo and hosted model are dependencies, not organizational function owners imported from upstream.
- Credited operating / distribution surfaces: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [agents/base.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/base.py); [models/openrouter.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/models/openrouter.py); [tools/registry.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/registry.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [tools/factory.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/factory.py); [tools/workspace.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/workspace.py); [tools/shell.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/shell.py); [tools/filesystem.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/filesystem.py); [tools/git.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/git.py); [orchestrator/state.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/state.py); [orchestrator/persistence.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/persistence.py); [orchestrator/config.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/config.py); [skills/README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/README.md); [skills/open-pr.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/open-pr.md).
- Adjacent first-party surfaces excluded from ownership: unit tests/mocks, README demonstration output, example invocation, upstream OSS maintainer/contributor governance, and the separate target repository's maintainer approval/CI/merge policy. No external model provider decisions beyond task inference are credited as first-party governance.
- First-party operating / deployment modes considered: library `Orchestrator.run`, CLI normal/forced workflow, `--no-router`, read-only planning/review plus write-capable executor, optional built-in skills and PR finalizer, `--state`/ `--resume`. No live configured hosted model used in this source assessment.
- Recursion level: One bounded repository coding-work request/agentic production cell, **not** an institution of multiple independently viable continuing departments.
- Reviewed revision: `fbrubacher/orch@16960b40ed6293e27e4536bbd99d62989264a87e`, Git tree `4f240e001469278514eb0745f7c6df4a7b06c79c`, default `main`, GitHub ID `1345077988`, created `2026-08-24T14:53:46Z`, public/nonfork/nonarchived.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The first-party `Agent.run` appends chat messages, supplies the allowed tool schema to the external model endpoint, dispatches returned function/tool calls through a local registry and appends tool observations to the next model turn. Router, Planner, Executor and Reviewer share this loop with task-specific prompts and tool grants; the tool registry gates mutating shell/file access to the Executor. `Orchestrator.run` sequences the roles, reads git diff and validation, obtains Reviewer PASS/FIX and on FIX returns issue feedback to the next Executor iteration. It persists phase state for opt-in resume and can optionally invoke a PR finalizer after PASS, without merging. This is executable first-party composition, not merely a collection of suggested prompts. [agents/base.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/base.py); [models/openrouter.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/models/openrouter.py); [tools/registry.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/registry.py); [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [tools/factory.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/factory.py); [tools/workspace.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/workspace.py); [tools/shell.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/shell.py); [tools/filesystem.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/filesystem.py); [tools/git.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/git.py); [orchestrator/state.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/state.py); [orchestrator/persistence.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/persistence.py).

## Operational model

The operational output is a bounded agentic coding change or error/status with review feedback and optionally an opened PR. The model owns task-specific decisions at each role, while the deterministic Orchestrator owns phase order, iteration limit, persistence and optional finalization gate. There is **one** task-owning S1 pipeline: agent roles are subfunctions, not independently viable continuing S1 organizations. S2–S5 hypotheses are tested below against possible model, runtime, human, and parent decision loops; operator credentials and external repo policy are not silently promoted to organizational owners.

## S1 — Operations

- State: A
- Function: Model-directed bounded coding work on a caller-selected repository: investigate, plan, modify code, validate, receive reviewer feedback and produce an answer/optional PR.
- Disturbance / variety regulated: Unknown bug/feature, variable repository structure, tool failures, failed validation, inconsistent plan and reviewer rejection.
- Decisive decision or feedback right: Router may classify task type; Planner chooses exploratory tool calls and proposes plan; Executor chooses first-party read/write/shell/git tools, then Reviewer examines reports/diff/test output and judges PASS/FIX. The Orchestrator decides phase transitions and iteration budget deterministically.
- Decision owner: Configured first-party model-backed Agent instances own case-specific task/tool selection and model-based reviewer judgment; the Python orchestrator owns deterministic workflow sequencing and retry count. Human selects task/repo/credentials and controls external merge.
- Supporting / enforcement mechanisms: Shared `Agent.run` model/tool loop and `_dispatch`, tool registry and writable/read-only tool splits, OpenRouter client, typed Router/Planner/Reviewer outputs, WorkflowState persistence, optional finalizer and git PR skills.
- Closure path: CLI/library request → Router model or default workflow → Planner model + read tools → Executor model + write/shell/git tools → validation/diff → Reviewer model PASS/FIX → on FIX next executor consumes reviewer feedback → final result/checkpoint; optional tool-using finalizer opens PR when local `gh` and configured target permit.
- Boundary reachability: Normal shipped `Orchestrator.run` instantiates and calls the role classes wired through `Agent.run`, which executes each selected tool and returns its observation to the subsequent model turn; `main.py` invokes this path, not only a demo/test placeholder.
- Why this is / is not agent-owned: Removing model inference leaves a deterministic phase shell without selecting task-specific investigation/edit/review judgments; using an external inference API doesn't transfer the first-party agent/workflow implementation to OpenRouter.
- Evidence: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [agents/base.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/base.py); [models/openrouter.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/models/openrouter.py); [tools/registry.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/registry.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [tools/factory.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/factory.py); [tools/workspace.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/workspace.py); [tools/shell.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/shell.py); [tools/filesystem.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/filesystem.py); [tools/git.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/git.py)
- Basis: structural (shipped first-party executable source, not live paid model performance)
- Confidence: High for reachable configured first-party S1; runtime quality untested.
- Caveats: Credentials/provider required for actual model run; source alone does not demonstrate successful external PR or useful coding outcome. The external target project remains outside the assessed local harness.

## S2 — Coordination

- State: —
- Function: No evidenced continuing inter-S1 mutual-regulation function at an organizational recursion above independently viable operational units.
- Disturbance / variety regulated: Plan/execution mismatch and reviewer disagreement within a single finite coding task, potential read/write overlap between role phases.
- Decisive decision or feedback right: `Orchestrator.run` serially calls distinct role instances and passes plans/review feedback; its fixed phase machine attenuates intra-task mismatch but does not negotiate disruptive commitments among independently viable continuing S1 businesses.
- Decision owner: Deterministic phase machine plus role-specific model decisions in one task, rather than an independently mandated inter-unit S2 regulator.
- Supporting / enforcement mechanisms: Router/Planner/Executor/Reviewer sequence, `state.history`, checkpoint data, event emissions and read-only vs writable tool access.
- Closure path: Task planning → execution → reviewer verdict → same task's corrective retry; no cross-business operational interference → independent S2 balancing decision → two viable S1s adapt their continuing behavior.
- Why this is / is not agent-owned: Multiple sequential agent roles are parts of a single job pipeline, not continuing independent viable S1 departments. A review feedback loop is not automatically an S2 relationship.
- Evidence: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [orchestrator/state.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/state.py); [orchestrator/persistence.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/persistence.py)
- Basis: bounded first-party absence
- Confidence: High at declared single coding-workflow recursion.
- Caveats: A higher-recursion organization could run many `orch` jobs, but that organization is not packaged in this standard distribution.

### Absence scope

- Surfaces inspected: Checked orchestration pipeline, each role adapter, workflow state/checkpoint, shared event stream, target workspace and tool registries.
- Plausible first-party paths checked: Tested whether Planner/Executor/Reviewer have independent enduring S1 purposes, whether their work creates actual inter-S1 disturbances and whether a distinct first-party S2 authority returns reciprocal operational constraints.
- Why no material first-party path remains: Shipped roles work on one caller-supplied task/repository, with internal PASS/FIX correction; no separate, independently viable S1 businesses nor cross-unit interference attenuation with independent feedback closure.

## S3 — Inside-and-now control

- State: —
- Function: No established accountable current whole-organization management of continuing viable operational units.
- Disturbance / variety regulated: Task delays, failing validation, wrong workflow, retries, incomplete edits and need for a protected merge decision.
- Decisive decision or feedback right: Configurable model routing, max iterations, deterministic workflow and `Reviewer.passed` determine local task sequencing; human may choose a repository/skill and later decide merge. No discretionary whole-system resource/commitment allocation across multiple viable S1 units is wired.
- Decision owner: Caller config and deterministic orchestrator for task execution, model reviewer for task correctness; no present S3 executive or reconstructable parent S3 mode.
- Supporting / enforcement mechanisms: OrchestratorConfig, workflow table, retry budget, state/persistence, validation steps, task status/output and optional PR finalizer.
- Closure path: One coding request → quality check → repeat/finalize task; no continuing operations portfolio reporting → current management allocation or intervention → binding updated organizational commitments.
- Why this is / is not agent-owned: Calling the top-level class `Orchestrator` does not make it a VSM S3 current manager. An operator choosing task or approving a PR is not a packaged parent-governed organizational S3 loop.
- Evidence: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [orchestrator/config.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/config.py); [skills/README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/README.md); [skills/open-pr.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/open-pr.md); [orchestrator/state.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/state.py); [orchestrator/persistence.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/persistence.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py)
- Basis: bounded first-party absence
- Confidence: High at declared single-task pipeline recursion.
- Caveats: Repo ownership and human downstream merge decisions are external to this harness.

### Absence scope

- Surfaces inspected: Examined orchestration phase loop, task/workflow config, reviewer quality gate, persistence, skill/finalizer and caller options.
- Plausible first-party paths checked: Checked whether an agent or operator has organizational whole-current view of ongoing independent business S1s, binding resource/priority control and a return path; also considered parent-governed S3 mode.
- Why no material first-party path remains: No durable collection of independently viable S1 units or whole-current management reports/manager authority is shipped; fixed phase iteration and coding PR permission are task-local.

## S3* — Complementary audit

- State: —
- Function: No independent field-reality audit challenging ordinary S3 management accounts and returning an S3 corrective decision.
- Disturbance / variety regulated: Executor may report incorrect success or validation; diff and tests may disagree with its narrative.
- Decisive decision or feedback right: Reviewer agent inspects executor summary, actual git diff and test/validation text and returns PASS/FIX; this is a substantive task-level quality check but not auditing managerial reality at an S3 recursion.
- Decision owner: Model-backed ReviewerAgent does the coding-work artifact check; no chartered complementary auditor of an existing current organizational manager.
- Supporting / enforcement mechanisms: `_git_diff`, `_run_validation`, read-only `ReviewerAgent`, PASS/FIX loop and events.
- Closure path: Executor output + diff/test observations → reviewer judgment → next coding attempt or result; no S3 normal management report → materially separate operations channel → management intervention.
- Why this is / is not agent-owned: Code reviewer is not automatically S3*; source shows different role and evidence but its object is the same bounded S1 product, not the veracity of S3 management statements about a multi-unit organization.
- Evidence: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [tools/factory.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/factory.py); [tools/workspace.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/workspace.py); [tools/shell.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/shell.py); [tools/filesystem.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/filesystem.py); [tools/git.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/git.py)
- Basis: bounded absence after inspecting strongest audit-like path
- Confidence: Medium-high: reviewer independence is real at code-artifact level; no S3 reporting/audit role established.
- Caveats: A different declared higher-level organization could make separate use of these checks; not evidenced here.

### Absence scope

- Surfaces inspected: Checked reviewer prompts, reviewer class, independently fetched diff and validation output, executor history and feedback state.
- Plausible first-party paths checked: Tested whether reviewer challenges an ordinary S3 management account through complementary direct access to ongoing S1 reality and whether correction returns to that S3 owner, rather than just rejecting a coding task.
- Why no material first-party path remains: Review feeds the executor within the same coding workflow; there is no evidenced legitimate organizational S3 reporting actor or separate S3* audit charter/manager correction loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No continuing future-environment intelligence selecting prospective organizational capability changes and returning accepted adaptations to present operations.
- Disturbance / variety regulated: New task categories, unfamiliar project architecture, evolving model choices, reusable skills and workflow variations.
- Decisive decision or feedback right: Router chooses a predefined workflow for the current task; `OrchestratorConfig` and skill files are maintainer/operator-set. The code does not autonomously investigate future organizational opportunities, select and accept new capability strategy.
- Decision owner: Human developer/config and task-specific router model; no organizational S4 adaptation decision right or parent-governed strategic return.
- Supporting / enforcement mechanisms: Router classifications, configurable model overrides, prompts, prewritten skills and workflow table.
- Closure path: Present task → task-class workflow selection → coding execution; no outside-environment search → strategic capability option → legitimate acceptance → revised organization-wide capability and current S3 operation.
- Why this is / is not agent-owned: Model selection for today's task and future extensibility described in README are not an implemented recurring S4 prospective intelligence function.
- Evidence: [main.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/main.py); [orchestrator/orchestrator.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/orchestrator.py); [orchestrator/config.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/config.py); [skills/README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/README.md); [skills/open-pr.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/open-pr.md); [agents/router.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/router.py); [agents/planner.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/planner.py); [agents/executor.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/executor.py); [agents/reviewer.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/agents/reviewer.py); [README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/README.md)
- Basis: bounded first-party absence
- Confidence: High.
- Caveats: Developer may extend prompts/workflows in later revisions, which is outside pinned source.

### Absence scope

- Surfaces inspected: Inspected router, predefined workflow config, optional strong model, skill loading, README extension instructions and task flow.
- Plausible first-party paths checked: Checked ongoing prospective external sensing, generation of strategic capability alternatives, autonomous or parent-authorized acceptance, durable integration and return to current control.
- Why no material first-party path remains: All observed adaptive choices are immediate task routing or manual configuration; no first-party continuous future-capability acceptance/return path is shipped.

## S5 — Policy and identity

- State: —
- Function: No ultimate purpose/identity and constitutional policy authority at the declared organizational recursion.
- Disturbance / variety regulated: Unsafe shell edits, scope violation, model choice, skill authority and external PR ownership.
- Decisive decision or feedback right: Target workspace paths are sandboxed, read/write tools are role-gated, configuration defines fixed budgets/default workflows, and a caller controls credentials/merge. This enforces limits but cannot decide and return a constitutional organization-identity issue.
- Decision owner: External user/developer controls boundaries; deterministic tool registry/workspace enforce them. No first-party policy/identity deliberator or packaged parent S5 return path.
- Supporting / enforcement mechanisms: Workspace and filesystem checks, read-only tooling for reviewers, configurable task skills, default prompt, no automatic PR merge.
- Closure path: Operator sets configuration/target and permissions → tool and workflow execution within limits; no organization-identity issue → legitimate S5 authority → binding constitutional decision returned into ongoing organizational operation.
- Why this is / is not agent-owned: Tool sandbox and human permission are necessary safety mechanisms but not S5. The human owns the project externally, with no first-party organization-level policy judgment protocol in `orch`.
- Evidence: [tools/factory.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/factory.py); [tools/workspace.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/workspace.py); [tools/shell.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/shell.py); [tools/filesystem.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/filesystem.py); [tools/git.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/tools/git.py); [orchestrator/config.py](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/orchestrator/config.py); [skills/README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/README.md); [skills/open-pr.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/skills/open-pr.md); [README.md](https://github.com/fbrubacher/orch/blob/16960b40ed6293e27e4536bbd99d62989264a87e/README.md)
- Basis: bounded first-party absence
- Confidence: High.
- Caveats: Upstream governance of the OSS source itself is adjacent to the published runtime and not assumed to operate a VSM S5 for the target user's job.

### Absence scope

- Surfaces inspected: Checked workspace protection, read/write role limits, config and skills, optional PR finalizer, CLI caller rights and README distribution modes.
- Plausible first-party paths checked: Checked whether first-party agents can address identity/ultimate purpose conflicts, whether legitimate operator parent S5 decisions are routed through an established policy cycle and whether authoritative decisions return to govern organizational operation.
- Why no material first-party path remains: Permission/configuration mechanisms govern a coding task and external host; there is no evidenced organizational identity issue adjudicator or constitutive parent return path in the shipped workflow.

## Distributed OSS parent arrangement

The upstream code is public OSS but this assessment covers one packaged coding workflow. The project's maintainers, contributors and a separate target repository's policies are not an automatically reachable institutional parent of the operator's task. No parent S3/S4/S5 first-party decision-and-return mode is evidenced here.

## Self-hosted and non-human modes

Local CLI/library execution and `--resume` preserve the same single-task recursion. OpenRouter or another compatible configured model serves as inference rather than an organizational parent. Self-hosted operation changes provider/deployment configuration, not the decisive S3/S4/S5 closure paths.

## Recursion

At the assessed level the model-backed coding workflow performs one S1 operational job. The router/planner/executor/reviewer labels describe sequential phases and model instances at that level. A hypothetical organization running many jobs has its own higher recursion, which is not shipped and is not imported into this finding.

## Variety and escalation

Novel file structure, failing commands, reviewer FIX and missing credentials are task variety. The first-party agent can replan/re-execute under bounded iterations; persistent failures or an external PR/merge decision go to the user/environment. Emitted status and errors are events, not an algedonic constitutional channel. Reviewer feedback returns to the same operational job, not organizational S3. No independently chartered higher-level escalation loop was observed.

## Evidence gaps

No live paid OpenRouter inference, target repository modification/PR submission, or real-world throughput is claimed. Evidence is the pinned shipped code and read-only repository architecture; the offline test suite may corroborate implementation when its declared dependencies are installed. No concrete unresolved in-boundary S2–S5 path remained after examining the model/role/runtime/configuration and optional finalizer boundaries. These bounded negatives do not exclude future extensions or externally composed organizational systems.
