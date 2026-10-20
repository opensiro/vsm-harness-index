---
harness_id: forgedock
project_name: ForgeDock
repository: https://github.com/RapierCraftStudios/ForgeDock
review_ref: f5bfeeedf6baadd94aea1e6769f69abd45080016
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ForgeDock

## Review boundary

- System in focus: Public `RapierCraftStudios/ForgeDock` agent-directed software issue-to-PR pipeline, combining packaged agent command specs and an independently provided headless Anthropic tool-use runtime with durable GitHub state/protocol, phased work, parallel issue lanes and optional autonomous backlog scan.
- Purpose and identity: Execute a chosen GitHub issue, or a configured batch/milestone of issues, through task-reasoning, implementation, review, validation and merged/terminal receipt; preserve prior findings in issue and PR annotations for future tasks. This is an engineering-work pipeline, not a separately incorporated autonomous business.
- Relevant environment: GitHub issue/PR/commit/Actions evidence, repository file system, configured Claude Code/OpenCode or an explicitly opted-in Anthropic API and tool handlers, GitHub CLI credentials and branch protections, optional mounted sandbox/remote lane provider. Reviewer and coding model outputs are untrusted until recorded tool/CI evidence validates milestones.
- Standard-distribution boundary: `bin/runner.mjs` standalone model API/CLI loop, `bin/engine.mjs`, `bin/engine-cli.mjs` issue-stage execution, phase registry, GitHub reconciliation, runlog, sandbox lane and resource admission, shipped slash-command specs `commands/work-on.md`, `commands/orchestrate.md`, `commands/autopilot.md`, PR review phase and optional GitHub Actions autopilot template.
- Credited operating / distribution surfaces: [`bin/runner.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/runner.mjs); [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs); [`bin/engine-cli.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine-cli.mjs); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`bin/engine/state.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/state.mjs); [`bin/engine/runlog.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/runlog.mjs); [`bin/engine/reconcile.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/reconcile.mjs); [`bin/engine/admission.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/admission.mjs); [`bin/lean/execution.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/lean/execution.mjs); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`commands/orchestrate.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/orchestrate.md); [`commands/review-pr.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/review-pr.md); [`commands/autopilot.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/autopilot.md); [`templates/github-actions/forgedock-autopilot.yml`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/templates/github-actions/forgedock-autopilot.yml); [`bin/opencode-adapter.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/opencode-adapter.mjs); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).
- Adjacent first-party surfaces excluded from ownership: Public marketing claims about repository self-development throughput, user GitHub branch protection/maintainer organization and decision rights, Claude Code and external Anthropic SDK internals, third-party model intelligence, human-authored project roadmap/forge.yaml, README examples, test-only fixture behavior and optional remote sandbox/LLM providers.
- First-party operating / deployment modes considered: Native Claude Code slash-command route, optional OpenCode adapter, `forgedock run-issue` headless engine with CLI backend, explicitly owner-opted API-backed first-party `runCommand` model tool loop, parallel orchestrate lean lanes, GitHub persistent annotation/restart recovery, scheduled autopilot recon/fix, human needs-human gates and verified PR output. Optional sandbox execution does not grant organization-wide authority.
- Recursion level: The viable autonomous agent unit is **the model-led issue-to-PR engineering task loop**, not necessarily each issue lane as an independent continuing business or a whole software enterprise's viable operating department. Multiple issue instances share deterministic scheduling, git and PR evidence and finite task lifecycles.
- Reviewed revision: `RapierCraftStudios/ForgeDock@f5bfeeedf6baadd94aea1e6769f69abd45080016`, immutable upstream Git tree `c26134005bfb240b41146be22c8ac0b443400355`, stable GitHub repo ID `1259486715`, created `2026-06-04T14:57:20Z`, public AGPL-3.0 nonfork nonarchived, default main.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`commands/work-on.md` and its agent-executed phase specs define investigation, builder work, review, verified merge and issue closure, retaining structured FORGE annotations and recovery receipts on GitHub. The first-party `bin/runner.mjs` offers a standalone Anthropic model tool-use path: `runCommand` loads spec, picks an explicitly supported backend, repeatedly calls a concrete model, invokes the model-selected handlers on `tool_use`, appends their `tool_result` blocks as new messages, and stops at a model terminal or max-iteration boundary. The supported direct Claude Code/OpenCode mode uses external model-agent tool execution, but S1 positive ownership is not inferred from it alone. [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`bin/runner.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/runner.mjs); [`bin/opencode-adapter.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/opencode-adapter.mjs).

`bin/engine.mjs`, `bin/engine-cli.mjs` and `bin/engine/phases.mjs` implement a deterministic GitHub-backed stage/state/replay engine. Crucially the engine, **not** an LLM, chooses the next configured issue phase based on structured evidence. Local runlog, GitHub issue annotations and reconciliation allow crash recovery. The orchestrator admits parallel issue lanes through fixed dependency, file-overlap, admission and resource bounds. These are execution and integrity mechanisms, not independent institutional decision owners. [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs); [`bin/engine-cli.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine-cli.mjs); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`bin/engine/runlog.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/runlog.mjs); [`bin/engine/reconcile.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/reconcile.mjs); [`bin/engine/admission.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/admission.mjs); [`commands/orchestrate.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/orchestrate.md).

Autopilot can periodically rediscover issues or signal CI/review problems, and automatic review agents can create issue findings, but their decision envelope is to improve code or recover stalled issue work under user-configured project constraints, not future company strategy. GitHub PR/CI/code review supports task artifact correctness without a direct-management field audit relationship. [`commands/autopilot.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/autopilot.md); [`templates/github-actions/forgedock-autopilot.yml`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/templates/github-actions/forgedock-autopilot.yml); [`commands/review-pr.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/review-pr.md); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).

## Operational model

The model selects meaningful tool and implementation choices for each accepted issue while GitHub-backed state and configured deterministic checks control phase admission and completion. Subtasks and parallel issue lanes remain bounded work units. No corporate metasystem functions are inferred from routine issue coordination, CLI secrets, CI, human PR merge approvals or repeated automation.

## S1 — Operations

- State: A
- Function: Autonomous model-guided GitHub issue software-engineering operations from investigate through implement, test and review to a bounded PR/closure receipt.
- Disturbance / variety regulated: Variable codebase/issue text, unexpected tool errors, merge conflicts, failed CI, incomplete requirements, unexpected changes by other contributors and stopped/restarted agent execution.
- Decisive decision or feedback right: A configured Claude Code/OpenCode agent or the shipped first-party headless Anthropic tool-use runner chooses code investigation, execution, file edits and review findings. `runCommand` calls a live model with tool schemas and acts on model-selected `tool_use` blocks, returns concrete tool results to the next model step, and limits iterations. `runIssue`/phase protocol advances based on GitHub/commit outcomes not arbitrary model success prose.
- Decision owner: Model-driven execution agent chooses current investigation/build/review actions within first-party ForgeDock spec and tool handlers. Deterministic engine/projector and GitHub CI/merge evidence constrain acceptance and recovery; human can invoke or withhold credentials but is not each tool action's author.
- Supporting / enforcement mechanisms: Packaged `commands/work-on.md` and phase specs, `bin/runner.mjs` API/CLI backend selection, first-party tool handlers and output feedback, `bin/engine.mjs` phases/runlog/projector, GitHub FORGE markers, staged PR/CI evidence and lease recovery.
- Closure path: GitHub issue and configured code workspace → model reads phase spec, inspects files and proposes/executes tools → tool outputs returned in iterative messages → model edits/tests/reviews → first-party engine observes git/CI/GitHub status and records durable FORGE annotations → next phase or needs-human/engine-error/merged terminal result. Reconciliation resumes after crashes.
- Why this is / is not agent-owned: The distribution includes `forgedock run-issue`, CLI native Claude/OpenCode integration and a standalone model API `runCommand` with real tool_use/tool_result loop. A concrete configured provider and GitHub CLI/auth is needed but does not require downstream authors to implement a new agent actor.
- Evidence: Without the configured model the engine can only route named phases and check evidence; it cannot select code changes, investigations or fix strategies. The meaningful task decision is agent-owned, rather than static shell-only orchestration.
- Basis: [`bin/runner.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/runner.mjs); [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs); [`bin/engine-cli.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine-cli.mjs); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).
- Confidence: Primary runnable first-party source, model/tool handoff and shipped command specifications; no private upstream PR results credited as measurements.
- Caveats: High for S1 agent action ownership with supported configured model.
- undefined: Executing repo shell, branch or merge actions on a real target requires operator permission and can have significant side effects. This Index review ran no live model or target GitHub issue; README's claimed self-production metrics not independently reproduced.
- Boundary reachability: [`bin/runner.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/runner.mjs); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs): normal configured headless CLI/API route and packaged issue phases jointly provide a concrete agent actor, available tools, true task-variation feedback, on-disk/git observations and bounded terminal execution. The first-party runner does not require external agent authoring.


## S2 — Coordination

- State: —
- Function: No separate autonomously owned regulator of interference between multiple independently viable *continuing* S1 business units.
- Disturbance / variety regulated: Parallel issue lanes can touch the same files, exhaust worker capacity, collide on branch names or depend on each other's PRs; new findings can amplify work.
- Decisive decision or feedback right: ForgeDock resolves issue dependencies and same-path/overlap conflicts, sets concurrency and issue admission/defer rules, and can resume/stop lanes. Those are finite issue pipeline scheduling/resource constraints; no separate viable S1 enterprise units receive dynamically negotiated reciprocal operating commitments from an independent S2 owner.
- Decision owner: Fixed implementation of scheduler/admission, configured `forge.yaml` bounds and operator's selected issue set; model lanes each own their current issue, not S2 balancing a set of organizational S1 units.
- Supporting / enforcement mechanisms: Orchestrate DAG, lane sandbox/leases, phase completion predicates, cascade admission policy, conflict-aware overlap rules, issue labels and GitHub source of truth.
- Closure path: Competing issue paths or worker exhaustion → static queue/defer/lease decisions → the affected *individual issues* launch serially or defer. No continuing interdepartmental disturbance feedback / negotiated commitments / return to viable units.
- Why this is / is not agent-owned: Concurrent coding issue pipelines are transient task instances, not necessarily viable operational departments. Merge-conflict avoidance does not automatically satisfy Beer S2 even if it dampens task collisions.
- Evidence: [`commands/orchestrate.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/orchestrate.md); [`bin/engine/admission.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/admission.mjs); [`bin/lean/execution.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/lean/execution.mjs); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`forge.yaml.example`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/forge.yaml.example).
- Basis: Bounded negative after inspecting standalone/parallel and optional execution modes.
- Confidence: Medium-high.
- Caveats: If installed in a real multi-team company, it might help a human S2 coordinator, but team organization/authority would be external to shipped runtime.

### Absence scope

- Surfaces inspected: Concurrent issue orchestration, dependency DAG, same-file collision prevention, lane lease/admission, worker budgets and cascade review-finding cap.
- Plausible first-party paths checked: Checked whether scheduling handles real conflict between *continuing independently viable S1 organizations*, autonomously negotiates their relative obligations and returns changes to both.
- Why no material first-party path remains: All first-party lanes are finite issue/PR tasks under one pipeline. Scheduling and deduplication are deterministic tool/workflow constraints without a function-specific autonomously owned relation among separate viable business units.


## S3 — Inside-and-now control

- State: —
- Function: No separately authorized discretionary organizational S3 overseeing ongoing viable S1 unit objectives, allocations, commitments and management accountability.
- Disturbance / variety regulated: Pipeline failures, stale sessions, pending PR reviews, test budget overruns, high-severity findings and resource contention.
- Decisive decision or feedback right: The deterministic phase engine/reconciler chooses next phase from observed markers and evidence; admission and max-concurrent rules are static, and human can configure concurrency, reject/merge PR or handle needs-human. These do not close a first-party parent-managed S3 *over continuing independently viable S1 units*.
- Decision owner: Per-issue model agent and deterministic engine; human maintainer decisions on PR and project configuration, but not a published S3 parent decision/return over a viable departmental system.
- Supporting / enforcement mechanisms: Lease, crash recovery, phase verification, issue/PR status, `work-on` safety, resource caps, manual handoff and static config.
- Closure path: Task result → status/phase updates → next issue action, or needs-human escalation → maintainer resolves *one issue*. No cross-unit whole-current authoritative manager report → dynamic resource/commitment choice for viable operating units → changed continuing S1 business performance.
- Why this is / is not agent-owned: Multi-issue queue supervision and human PR approvals are work control, not organizational S3. In particular the engine explicitly says it, not an LLM, picks phases deterministically.
- Evidence: [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`bin/engine/reconcile.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/reconcile.mjs); [`bin/engine-cli.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine-cli.mjs); [`commands/orchestrate.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/orchestrate.md); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md).
- Basis: Source-bounded negative after checking autonomous and potential parent-governed pathways.
- Confidence: High.
- Caveats: Specific owner approval steps might satisfy another organizational boundary if its viability and parent contract were separately supplied.

### Absence scope

- Surfaces inspected: Pipeline state machine, deterministic phase selection, queue/parallel issue admission, operator config/PR approval, stalled-run recovery and manual handoff.
- Plausible first-party paths checked: Checked whole batch orchestration as current organizational executive, headless auto-merge as accountable S3, human maintainer as parent S3(P), and static budget/rate setting as current-resource control.
- Why no material first-party path remains: Current decisions manage issue/task phases and capacity, not a standing viable-unit organization. No separate whole-organization discretionary current control owner or returned viable department commitments; human PR approval is not itself operationally closed S3 parent mode.


## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of S3 current-management claims from field reality and return of binding correction to S3.
- Disturbance / variety regulated: Model-generated code may be wrong, review may miss vulnerabilities, merged PR may regress CI, command output may exaggerate success.
- Decisive decision or feedback right: Domain-specialist reviewers can generate PR-specific findings, GitHub CI and engine detect merge/verification outcomes independently of model prose; these inspect software artifacts and run correctness, not an organizational S3 management statement about continuing viable units.
- Decision owner: Agent review role and CI evidence guards; not independently chartered management-reality auditor with a separate operating-information mandate.
- Supporting / enforcement mechanisms: Structured PR review comments, first-party review phase, issue/PR merge markers, GitHub evidence projector and status parity checks.
- Closure path: Build PR → independent agents review code/test/CI → findings return to the issue and builder for remediation; no S3's whole-current state report → independent organizational field audit → S3 correction.
- Why this is / is not agent-owned: Good code QA is not the complementary organizational S3* audit relationship. The decision subject and return recipient are one coding deliverable and task worker.
- Evidence: [`commands/review-pr.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/review-pr.md); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`bin/engine/phases.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/phases.mjs); [`bin/engine/runlog.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine/runlog.mjs); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).
- Basis: Bounded negative despite substantive independent work-product review.
- Confidence: High.
- Caveats: GitHub reviewers may be humans; no independently authorized viable-unit organizational audit structure is assumed.

### Absence scope

- Surfaces inspected: Domain-specialist PR reviews, CI/action evidence, GitHub PR annotations, phase verification, runlog/projector and replay status checks.
- Plausible first-party paths checked: Checked review agent independence, report vs code/test evidence, whether audit examines an S3 manager's normal whole-current report and returns independently sourced correction.
- Why no material first-party path remains: Reviewers independently inspect particular PR work and return implementation findings; no separately chartered audit of a distinct S3 operating manager's account of continuing viable units is supplied.


## S4 — Outside-and-then intelligence

- State: —
- Function: No separately evidenced prospective outside-and-then agent ownership of long-term organizational adaptation and accepted changes to future capability.
- Disturbance / variety regulated: New security findings, codebase architecture drift, rising issue backlog, new upstream dependencies and CI failure signals can require new work.
- Decisive decision or feedback right: Autopilot periodically scans/reconstructs work and optionally raises fixes; review can file issues and dependency/health checks suggest improvements. The first-party mechanism does not provide a standing agent with a future-oriented environmental strategy mandate that selects and legitimizes new organizational capabilities and returns that acceptance to continuing S3/S1 operating structure.
- Decision owner: Configured coding agent chooses remediation within current issue; human owner sets `forge.yaml` feature and project roadmap. Deterministic autopilot scheduling/admission does not own institutional prospective strategic choices.
- Supporting / enforcement mechanisms: Autopilot scan/fix command, GitHub Actions cron, issue-derived review findings, staged issue backlog, phase pipeline health/quality gates and memory annotations.
- Closure path: Observed regression/CI/stale issue → new issue/remediation PR → merge when evidence gates pass. This updates particular software artifacts but does not by itself establish an institutional future-adaptation portfolio decision and formal return into ongoing organizational authority.
- Why this is / is not agent-owned: Creating issues or modifying software code is not sufficient to prove autonomous S4: the future strategic choice and owning organizational authority are not a distinct first-party closed function. A coding agent may answer strategic queries when prompted, but that is a bounded S1 task.
- Evidence: [`commands/autopilot.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/autopilot.md); [`templates/github-actions/forgedock-autopilot.yml`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/templates/github-actions/forgedock-autopilot.yml); [`commands/orchestrate.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/orchestrate.md); [`forge.yaml.example`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/forge.yaml.example); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).
- Basis: Bounded negative after checking self-produced findings and regular unattended scanning, not just simple cron.
- Confidence: Medium-high.
- Caveats: Long-running autonomous bug discovery may improve product resilience, but no general organizational adaptation-success claim follows.

### Absence scope

- Surfaces inspected: Autopilot CI/recon, backlog and review-derived finding generation, GitHub milestones, dependency scan, run memory and project README goals.
- Plausible first-party paths checked: Checked recurring environment scanning, automatically created issue findings and self-improving code loop as a candidate prospective future-option/acceptance route into a continuing company operational capability.
- Why no material first-party path remains: These mechanisms choose or recommend bounded bug and implementation work in current engineering operations. No separate prospective organizational-environment intelligence with accepted capability/strategy-level return and decision owner is demonstrated.


## S5 — Policy and identity

- State: —
- Function: No constitutional/ultimate identity or purpose authority, autonomous or operationally closed parent mode, for a viable organization.
- Disturbance / variety regulated: Actions may violate target project's permission boundaries, GitHub auth may be revoked, secrets or unsafe tool capabilities can be misused, owner may change repository priorities.
- Decisive decision or feedback right: Static `forge.yaml` safety bounds, command specifications and project maintainer decisions control coding scope/merge. They do not form an identity-level institutional legitimate authority deciding the organization's ultimate purpose and returning a binding charter change to S3/S4/S1.
- Decision owner: External repository owner and operator define purpose and rights; ForgeDock engine enforces local config and GitHub permissions. No first-party agent owns an ultimate organizational charter decision.
- Supporting / enforcement mechanisms: Local config permissions, host/provider credential authorization, GitHub branch protection, issue/PR review safety, human handoff.
- Closure path: User config or GitHub protection → task allowed/blocked/needs-human; no purpose/identity conflict → constitutional decision by legitimate S5 → persistent institution-wide mandate returned to operation.
- Why this is / is not agent-owned: Permission enforcement, PR merge rights and static project objectives are supporting constraints, not a self-governing organization policy loop.
- Evidence: [`forge.yaml.example`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/forge.yaml.example); [`commands/work-on.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/commands/work-on.md); [`bin/engine.mjs`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/bin/engine.mjs); [`README.md`](https://github.com/RapierCraftStudios/ForgeDock/blob/f5bfeeedf6baadd94aea1e6769f69abd45080016/README.md).
- Basis: Bounded negative after inspecting native/human approval and auto-merge modes.
- Confidence: High.
- Caveats: A deployed company may embed ForgeDock under its human S5, but that external governance is not a shipped ForgeDock decision-and-return mode.

### Absence scope

- Surfaces inspected: forge.yaml config, GitHub credential/branch-policy rules, needs-human gates, autonomous merge and CI policies, repo maintainer review modes.
- Plausible first-party paths checked: Checked autonomous update of overarching company mission, legitimate owner parent policy-authority with returned constitutional decision, and developer config as possible S5.
- Why no material first-party path remains: Rules constrain what this issue pipeline may do; no first-party purpose/identity constitution judgment or closed legitimate parent decision that changes institution-wide identity/policy is present.



## Recursion

ForgeDock orchestrates multiple issue/task loops and review phases but those are finite software-engineering workflows; there is no source demonstration that each is an independently viable organizational S1 with separate enduring customers, mandate and independently evolving resource decisions. The model-runner is an actual operational agent S1. Dependency and PR collision controls are execution-level mechanisms; reviewer/CI correction is work-product quality, not S3*. Human users may place ForgeDock under an external corporation's S3/S5, but that does not change the published first-party ownership state.

## Variety and escalation

Task-code ambiguity, tool errors, failed checks, missing reviewer confirmation and current run state generate variety. Model observations enable a new code/analysis decision while a deterministic engine insists on GitHub evidence, bounded retries and needs-human exit rather than inventing success. Issue annotations preserve learning, and scheduling prevents task collisions. Escalating one issue to its human maintainer is not a complete organizational S3/S5 channel without the required owning institution and return rights.

## Evidence gaps

- Review pinned to immutable AGPL source and concrete first-party model tool-use execution, specs and GitHub-backed engine. Shipped CLI and API-backed routes require configured external model and permissions, but no live external model calls or actual upstream PR modifications were performed.
- No claim that README's claimed many autopilot-produced PRs and throughput are independently replicated. Node syntax/focused test evidence, if recorded, is separate from any live coding task success benchmark.
- Future deployments may integrate ForgeDock into business team management or independent audit functions not present as first-party packaged mode. Negative results are bounded no-material-path statements, not universal impossibility.
