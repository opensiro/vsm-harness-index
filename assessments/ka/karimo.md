---
harness_id: karimo
project_name: KARIMO
repository: https://github.com/opensesh/KARIMO
review_ref: 305abbe8d7a86d01023913cd12072cd83e937f52
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# KARIMO

## Review boundary

- System in focus: A KARIMO Claude Code plugin installation conducting one bounded software feature/PRD from source research and planned agent work through implementation, task review and proposed integration. KARIMO's upstream maintainer organization and the user's entire software business are not the system in focus.
- Purpose and identity: Turn a user-approved product requirement into executable, wave-ordered agent briefs and reviewed software changes on the user's repository, subject to actual git, permission, review and human-merge conditions.
- Relevant environment: Changing project files, dependencies, test results, incompatible task briefs, simultaneous workers changing shared interfaces, GitHub PR/CI state, external review-provider findings, session interruption, approvals, tool/provider permissions and future optional user requests.
- Standard-distribution boundary: The published Claude Code marketplace plugin, its shipped slash commands and agent definitions, first-party PRD/status/worktree templates, manifest and supporting git/Bash scripts. Claude Code's native model/tool runtime, Task spawning and worktree facility are operational dependencies, not KARIMO-owned model internals.
- Credited operating / distribution surfaces: [marketplace and plugin manifest](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude-plugin/marketplace.json), [run command](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/run.md), [PM coordinator contract](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md), [implementer](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/implementer.md), [source-reading brief audit](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-reviewer.md), [corrector](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-corrector.md).
- Adjacent first-party surfaces excluded from ownership: Claude Code model/provider selection and its generic Task/worktree engines; external Greptile or Claude Code Review verdicts; GitHub Actions/CI decisions; non-default custom adapters, maintainer release tests and demo claims. The formerly conflict-resolving `review-architect` role explicitly says it is **deprecated for feature-branch mode**, so it is not credited as the default autonomous S2 owner.
- First-party operating/deployment modes: Installed `/karimo:research` and `/karimo:plan`; `/karimo:run --prd` with default brief review and model-backed PM/worker roles; configurable feature-branch/direct-to-main, integration cadence and optional review-provider/gate policies; final `/karimo:merge`; separate user-triggered `/karimo:feedback`. A supported `--skip-review` flag bypasses the brief-review stage.
- Recursion level: One PRD/feature organization with discrete planned worker tasks, coordinated by one current PM. Workers are operational units, not automatically nested independently viable organizations. The full customer product strategy, company, Claude Code vendor, and KARIMO source maintainers are distinct boundaries.
- Reviewed revision: `opensesh/KARIMO@305abbe8d7a86d01023913cd12072cd83e937f52` (`main`), marketplace/manifest version `9.10.1`.
- Observation date: 2026-10-26; pinned first-party source and native deterministic shell tests only.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

KARIMO supplies Markdown agent contracts and Claude Code slash commands, not a separate first-party LLM inference service. `/karimo:research` gathers project and optionally external technical evidence for a named feature; `/karimo:plan` generates a task PRD; `/karimo:run` creates briefs, routes them to a distinct brief-reviewer, allows human approval/correction, then starts the `karimo-pm` role. The PM reads `tasks.yaml`, a dependency/wave execution plan, `status.json`, config and findings; it runs work through distinct implementer/tester/documenter agents in isolated worktrees. It observes PR/CI/review results, controls wave admission, correction/model escalation and bounded gate/stop behavior, with a separate `pm-reviewer` for optional external review loops. `/karimo:merge` prepares the final feature PR subject to checks and user decisions. The distributed `.karimo/MANIFEST.json` enumerates the shipped 22 agent contracts and 11 command definitions; merely packaging agents does not prove successful runtime behavior.

## Operational model

The executing agents are model-backed first-party role configurations whose tool decisions are enacted by the external Claude Code host. The first-party PM is assigned the current PRD and delegates bounded work to separate operational roles. On the default pre-execution path, the brief-reviewer inspects proposed worker contracts against actual code and cross-task dependencies; findings return through an explicit human choice and, when selected, a first-party brief-corrector rewrites affected briefs/tasks before workers receive them. This is a narrowly completed **constructor**, not an always-on self-reconciling operational S2. The reviewer independently audits preparation claims, but optional external PR review cannot be credited to KARIMO. Human acceptance of plans/gates/merges is not by itself S5.

## S1 — Operations

- State: A
- Function: Research codebase/external technical context, prepare task briefs and implement/test/document concrete feature changes in an actual project.
- Disturbance / variety regulated: Source/API uncertainty, contradictory requirements, failing tests, changing files, dependencies and task-specific errors.
- Decisive decision or feedback right: Installed model-backed researcher, interviewer, implementer, tester and documenter roles choose project inspections, edits, tests and corrections within assigned briefs; outputs return as research artifacts, commits, test evidence and PR results.
- Decision owner: Selected first-party KARIMO agent role operating on the Claude Code Task/tool host, not Bash alone or the generic Claude runtime acting without the role configuration.
- Supporting / enforcement mechanisms: Agent frontmatter and tools, file-boundary rules, worker worktrees, task brief, `gh`, git, tests, status and CI.
- Closure path: User feature request → research/PRD/brief → PM's task assignment → model worker reads actual code and chooses write/check actions → source/test/commit/PR result → PM and ultimately user.
- Boundary reachability: The marketplace declares the plugin and `/karimo:run` explicitly spawns PM and worker types. Implementer has Read/Write/Edit/Bash tools, source-inspection instructions, validation and commit/PR handoff. External generic Claude Code cognition is not claimed as an independent KARIMO operation.
- Why this is / is not agent-owned: Removing model-backed workers leaves install/manifest/branch scripts and static instructions but no task-specific product research, code design, chosen edits or semantic repair.
- Evidence: [manifest and plugin declaration](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude-plugin/marketplace.json); [run's installed spawn path](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/run.md#L650-L707); [worker task/tool/validation contract](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/implementer.md#L1-L39); [worker implementation and test return](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/implementer.md#L96-L177); [research role and technical source access](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/researcher.md#L1-L73).
- Basis: First-party installed model/tool agent configurations linked through the normal task workflow.
- Confidence: High for specified operational ownership path; no generated-code-quality measurement.
- Caveats: Model, host and GitHub permissions must exist, and prompt-obedience is not verified by native shell tests. A feature may be run with fewer roles.

## S2 — Coordination

- State: C
- Function: Pre-empt a concrete conflict between **distinct planned workers** whose briefs encode incompatible wave dependencies, overlapping files or mutually inconsistent acceptance criteria, so their subsequent execution instructions no longer collide.
- Disturbance / variety regulated: Two tasks placed in a parallel wave both modifying dependent/shared files, one worker expecting a file a later-wave worker must first create, or conflicting per-wave success criteria.
- Decisive decision or feedback right: First-party `brief-reviewer` inspects the cross-task briefs against actual source/dependency state and proposes correction; `brief-corrector` can modify task dependencies, briefs and wave preconditions. In the default run command the **human must select** the apply-fixes path before those corrections take effect, so autonomous end-to-end S2 attenuation is not established.
- Decision owner: A composed brief-reviewer → user-choice → brief-corrector construction; there is no claimed autonomous live inter-worker conflict arbitrator.
- Supporting / enforcement mechanisms: Dependency DAG, generated execution plan, file scopes, source/PRD read access, review findings, brief-corrector, model-backed worker prompts, serial wave gates, native worktree separation.
- Closure path: Proposed parallel worker briefs and current code → reviewer spots a specific cross-task collision and produces actionable finding → user selects apply fixes → corrector alters `tasks.yaml` dependencies or briefs → PM dispatches changed instructions in subsequent execution waves.
- Boundary reachability: The standard `/karimo:run` brief-review phase challenges task order, dependencies and file-boundary collisions, then exposes an explicit correction option wired to a shipped corrector. The positive claim is limited to this selected preparatory mode; `--skip-review` bypasses it.
- Why this is / is not agent-owned: The first-party source-aware conflict detector and editing agent can settle a specified cross-S1 task interference, but the essential default user choice means a fully autonomous S2 function is not shown. Generic wave ordering, isolated git worktrees, branch guards and PM scheduling alone would not satisfy S2.
- Distinct S1 units: Two or more different planned implementer/tester/documenter workers whose briefs share or conflict over concrete source files and prerequisite outputs.
- Inter-S1 disturbance: Same-wave edits or inconsistent order/acceptance contracts causing incompatible worker outputs, not generic task uncertainty or review quality.
- Attenuating coordination relation: Source-aware cross-brief mismatch finding and explicit rewrite of dependency order / work brief before the named workers are dispatched.
- Feedback into subsequent S1 behaviour: Changed `tasks.yaml` dependency order and corrected briefs are loaded by PM, then affect worker wave placement and source modifications.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The witness is **conflict detection against two named task contracts followed by a concrete correction of their interference**, not the existence of a DAG, queue or mailbox.
- Evidence: [brief-review collision and original-code probes](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-reviewer.md#L30-L85); [shared-file sequencing checks](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-reviewer.md#L114-L128); [run's review and correction selection](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/run.md#L86-L178); [corrector modifies dependencies and task briefs](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-corrector.md#L48-L125); [deprecation of separate legacy conflict resolver](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/review-architect.md#L1-L35).
- Basis: Narrow source-constructed S2-specific pre-dispatch correction, with a necessary user choice; not measured runtime inter-worker reconciliation.
- Confidence: Medium-low; preparatory planned-unit conflict correction is a narrower witness than live operational oscillation attenuation.
- Caveats: No (P) state is used for S2. A user bypassing review or declining the correction lacks this path. A runtime git merge conflict is not itself credited as resolved by KARIMO; the deprecated `review-architect` is outside the default feature-mode claim.

## S3 — Inside-and-now control

- State: A
- Function: Maintain the current PRD's full task/wave commitments, assign specialized workers, redirect failing tasks and decide current repair/gate/stop actions.
- Disturbance / variety regulated: Dependency stalls, worker failure and incomplete PRs, unexpected code/test/review results, shifting per-task complexity, worktree crashes and exhausted revision budget.
- Decisive decision or feedback right: The model-backed PM examines current PRD/task status and GitHub/git reality, chooses current worker allocation, wave progress, model escalation, corrective delegation and whether to pause/replan. It spawns `pm-reviewer` and `pm-finalizer` for specialized current subflows. Configured deterministic guards can prevent unsafe branch/wave transitions without themselves owning the decisions.
- Decision owner: KARIMO `karimo-pm` role for the one running PRD; user retains product/merge authorization, and native Claude Code/CI only supply execution/check facilities.
- Supporting / enforcement mechanisms: `tasks.yaml`, `execution_plan.yaml`, `status.json`, `findings.md`, worktree/branch guards, provider result adapters, wave merge verification, human gate model and git-state crash reconstruction.
- Closure path: PRD scope and task graph plus current worker/PR/test/review feedback → PM selects remaining worker/wave/rework/escalation commitment → task/tool dispatch or pause → changed PRD work and task/PR state return for subsequent decisions.
- Boundary reachability: `/karimo:run` invokes this model-backed role in the shipped feature workflow. PM receives a whole-PRD status view and explicit authority over its task delegation, waves, review/repair and current stop/resume choices.
- Why this is / is not agent-owned: Branch assertions, automatic test gates and concurrency caps are fixed mechanisms; removing the PM model actor removes task-specific current prioritization, rerouting and correction decisions.
- Whole-system current view: Current PRD/task graph, briefs, execution plan, model assignment, `status.json`, GitHub PR merge/review states, findings and open gates across the PRD's workers.
- Current-control decision scope: Which task to execute/retry and with which worker/model, how to respond to review and stalls, what wave/gate can proceed, and whether this single PRD is ready or blocked; not global multi-project enterprise policy.
- Evidence: [PM owner and current scope](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1-L83); [PRD-wide inputs and overlap check](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L228-L246); [current plan/collision probes](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1055-L1104); [wave and worker delegation loop](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1198-L1245); [PR/review return](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1444-L1535); [terminal wave gate](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1678-L1759).
- Basis: First-party configured model coordinator with current multi-worker commitment and feedback paths.
- Confidence: Medium; source-wiring evidence, not observed live model control effectiveness.
- Caveats: Initial user confirmation and optional human wave gates constrain execution. The role's embedded Bash snippets are instructions, not a verified standalone PM scheduler runtime. `auto_merge_on_green` claims are deployment-dependent and do not establish an independent ultimate authority.

## S3* — Complementary audit

- State: A
- Function: Challenge the preceding research/planning/brief agents' readiness claims against the **actual codebase and task requirements** before executable commitments are handed to workers.
- Disturbance / variety regulated: A brief writer's incorrect file assumptions, infeasible success criteria, missing prerequisite, contradictory tasks and project configuration mismatch not visible in a summary-only status signal.
- Decisive decision or feedback right: Separately configured `brief-reviewer` uses Read/Grep/Glob/Bash to directly inspect first-party project files and distinguishes critical blockers from warnings, returning `HOLD`/clearance findings. The run command makes those findings part of the human-gated correction path and can dispatch a different `brief-corrector` before current work begins.
- Decision owner: The model-backed KARIMO `brief-reviewer` for substantive pre-execution audit; it does not itself implement changes. The user/runner determines whether fixes are applied.
- Supporting / enforcement mechanisms: Separate named agent and review step, direct repository artifact access, original PRD/brief inputs, structured findings, correction instructions and optional model-backed corrector.
- Closure path: Brief writer's planned-task claims → independently invoked reviewer checks originals against codebase and cross-task ground truth → documented critical findings and execution clearance → run controller/user routes correction → amended briefs/PRD and ensuing PM task dispatch.
- Boundary reachability: The normal `/karimo:run` flow explicitly spawns a distinct source-reading review role, saves recommendations and exposes corrections before the PM's execution stage. This is first-party audit of **planned work**, not first-party independent code audit of every produced PR.
- Why this is / is not agent-owned: A model reviewer selects discrepancies and operational clearance from source evidence independently of brief author reports. A deterministic YAML validator or GitHub PR approval alone would not. Role/context separation is structural, not a proof of separate vendor, host isolation or actual quality.
- Claim being audited: Research/brief-generation claim that task contracts reflect current files, dependencies and viable acceptance criteria.
- Ordinary reporting path: Researcher and brief writer submit consolidated findings, proposed task briefs and dependencies to `/karimo:run`/PM.
- Complementary access path: Reviewer directly reads source code, config files and actual task briefs through its own Read/Grep/Glob/Bash tools, with explicit no-edit/no-commit rule.
- Independence boundary: Different model-backed reviewer role/context with read-only instructions and its own clearance verdict; both use Claude Code host and may use same model family.
- Who acts on findings: Run controller presents recommendations; user may select first-party corrector to alter tasks before PM delegates them.
- Evidence: [reviewer task/source-access rights](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-reviewer.md#L1-L91); [findings and clearance contract](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-reviewer.md#L140-L193); [run's separate audit and correction-return path](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/run.md#L85-L180); [corrector's no-independent-investigation rule](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/brief-corrector.md#L13-L67).
- Basis: Default-connected, independent source-reading audit path for pre-execution planning claims, not optional external PR review.
- Confidence: Medium, limited to the preparatory planning phase.
- Caveats: The `--skip-review` option bypasses this audit; no guaranteed independent model/provider or sandbox separation is evidenced. External Greptile/Claude Code Review results routed by `pm-reviewer` are not credited as KARIMO's own independent source-review decision.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would monitor external/future conditions, select changes to the feature organization's enduring capability and return those adaptations into subsequent current operations.
- Disturbance / variety regulated: Future shifts in product needs, platform options or project environment, beyond technical evidence needed for today's PRD.
- Decisive decision or feedback right: No supported S4-specific future capability decision owner at this one-PRD recursion. Research examines external libraries **for a named current feature**; feedback investigates **past/internal** KARIMO failures after user prompting and applies user-approved learnings to future tasks.
- Decision owner: No source-established autonomous future-policy owner for this PRD organization; human product architect chooses future features and rules.
- Supporting / enforcement mechanisms: `researcher` WebSearch/WebFetch, `/karimo:research` external technical references, investigator drift checks, `/karimo:feedback` interviews, feedback auditor, persistent `.karimo/learnings` and per-PRD config.
- Closure path: Feature research returns into present planning, and retrospective feedback may change future rules after user approval; neither is a differentiated external-prospective intelligence → autonomous organizational capability change → operational return at the declared recursion.
- Boundary reachability: These are shipped options but their first-party contracts distinguish feature-focused knowledge gathering and after-the-fact human-triggered improvement, not a standing outside-and-then regulator.
- Why this is / is not agent-owned: Web search or retention of a learned rule does not by itself establish anticipatory environment modelling or authority to change the organization's future capability.
- Evidence: [feature-scoped research requirement](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/research.md#L1-L120); [external best-practice evidence used in PRDs](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/researcher.md#L1-L72); [feedback is user-triggered and approval-gated](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/feedback.md#L1-L58); [retrospective auditor and approval return](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/feedback.md#L215-L338).
- Basis: Negative at the declared one-PRD recursion; nontrivial adjacent retrospective learning acknowledged.
- Confidence: Medium.
- Caveats: At a differently scoped long-lived parent organization, the feedback/learned-rule path could warrant dedicated S4 reassessment. No upgrade of the present PRD's research activity is inferred.

### Absence scope

- Surfaces inspected: Researcher general and PRD modes, research command, feature planning and investigator drift, PM and per-PRD adaptation, feedback interview/auditor, persistent learnings and project config.
- Plausible first-party paths checked: External trend scans, capability/agent policy changes, reusable learning from PRD failures, provider choice changes and future scope/technology decisions.
- Why no material first-party path remains: External research is scoped to immediate requested features; the rule update mechanism is initiated and approved by the operator based on past failures. The shipped current-PRD mode has no prospective external-variation sensing and first-party future-capability decision/return loop.

## S5 — Policy and identity

- State: —
- Function: Would adjudicate an identity/ultimate-purpose conflict and return a binding policy decision for the continuing organization.
- Disturbance / variety regulated: Conflicts over the fundamental product purpose, standing authority, legitimacy or ultimate trade-offs beyond today's requested PRD.
- Decisive decision or feedback right: KARIMO exposes requirement interviews, optional human approval gates, PR merge restrictions, branch/file safety rules and configuration choices, but no first-party identity-policy decision path.
- Decision owner: Human project owner outside the assessed one-PRD operating organization retains these strategic/authorization rights; PM owns current task allocation, not enduring purpose.
- Supporting / enforcement mechanisms: CLAUDE/KARIMO rules, PRD approval, gated execution, `never_touch`/review boundaries, GitHub merge approval and review-provider configuration.
- Closure path: User may authorize, pause, edit or merge the current feature; no evidence of an ultimate identity conflict deliberated and returned as organizational policy to subsequent PRDs.
- Boundary reachability: Existing commands implement task acceptance and human limits, not identity-level governance.
- Why this is / is not agent-owned: Prompt rules, GitHub branch protection and ordinary operator assent are constraints, not a policy-setting agent or fully specified parent-governed S5 mechanism.
- Evidence: [run human approval and options](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/run.md#L112-L187); [PM current scope](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/agents/pm.md#L1-L69); [manual/auto merge command permissions](https://github.com/opensesh/KARIMO/blob/305abbe8d7a86d01023913cd12072cd83e937f52/.claude/plugins/karimo/commands/merge.md#L1-L62).
- Basis: Bounded source-negative.
- Confidence: Medium-high.
- Caveats: A parent institution may exercise S5 for the project/company, but that would be another system in focus. No standalone `P` inferred from ordinary PR approvals.

### Absence scope

- Surfaces inspected: Marketplace, KARIMO rules, interview and requirement approval, PM role and delegation, branch/file permissions, user gates, final merge and project feedback rules.
- Plausible first-party paths checked: Conflict over product mission, lawful ultimate governance, authority hierarchy, external institutional policy escalation and binding future identity decisions.
- Why no material first-party path remains: The documented choices all govern project-task scope, implementation permissions, quality or integration. No separate ultimate identity-policy regulation and return process is established.

## Distributed OSS parent arrangement

KARIMO's maintainers, Claude Code runtime provider, optional external code reviewers and the current project's human owner are separate authorities. Their combined actions do not create a single evidenced parent S3/S4/S5 mode for this installed PRD. In particular, optional human review and GitHub merge permission are not automatically `(P)` functions.

## Self-hosted and non-human modes

The plugin is installed locally into a user's project, but operating worker/PM decision rights depend on configured Claude Code models and credentials. Feature mode may have parallel workers, one PRD-wide PM and user/CI gates. The pre-execution review/corrector path is supported in the standard `/run` command and may be opted out of; optional external provider review and legacy direct-to-main mode are alternative operating surfaces and are not merged into an invented always-on autonomous workflow.

## Recursion

The one-feature/PRD scope is essential. Individual worktree workers implement subtasks; PM owns current cross-worker mission control; pre-execution reviewer challenges the planning contract. KARIMO's source-maintenance team and a customer's portfolio of multiple features belong to different recursions. Human final-merge authority is explicitly outside these agent-owned current function claims.

## Variety and escalation

Uncertain requirements and project code variety first enter researcher/brief generation and independent brief audit. On chosen correction, cross-task collisions are repaired before worker deployment. Workers handle local code/test variation; PM reacts to PR, finding and gate status. Human intervention occurs for required plan/gate/merge approvals, unrecoverable conflicts and exhausted attempts. Deterministic worktree and wave safeguards support but do not independently choose VSM policy.

## Evidence gaps

- No live Claude Code, provider-backed agent-quality, Browser, review-effectiveness, generated-code-security or prompt-compliance test was performed. Agent rights are pinned first-party source wiring, conditional on correct installation and available external runtime.
- Eight shipped deterministic test scripts (unit, integration and verification) were executed **individually** and returned PASS. They use temporary git fixtures and primarily check packaging, syntax, commit/report mechanics and template safety, not the autonomous organizational judgments in this assessment.
- S2=C is deliberately narrow: brief collision correction requires a user choosing the run command's apply-fixes branch. No autonomous runtime conflict-resolution outcome is claimed; the deprecated legacy `review-architect` is excluded from the feature-branch default.
- S3*=A is specifically the source-reading **pre-execution** brief/PRD audit, not a first-party code-diff reviewer of every resulting PR. Optional Greptile/Claude Code Review may improve quality but their external cognition is not attributed to KARIMO.
- Documentation contains versioned and legacy alternatives, e.g. hook descriptions versus an empty shipped `.claude/settings.json`. Only connected shipped source paths are credited, not every architectural feature table or illustrative pseudocode as tested enforcement.
