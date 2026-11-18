---
harness_id: agystack
project_name: agystack
repository: https://github.com/jtaroreh/agystack
review_ref: 93f43a58ade41ca8271499d3497154b2c6c3619d
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# agystack

## Review boundary

- System in focus: One configured agystack engineering project/program running in Google Antigravity, optionally using its shipped agent swarm, arena, orchestrate and independent review skills, not the agystack repository's development organization.
- Purpose and identity: Produce and land small, verified software changes using model-directed engineering agents, bounded delegated scope, coordinated parallel workers, test feedback and owner-controlled project standards.
- Relevant environment: Software source and tests, GitHub PR/CI status, cloud worker resources and cost, research candidate outputs, reviewer findings, branch and worktree interference, changing task requirements and owner mandates.
- Standard-distribution boundary: First-party agystack plugin skills, playbooks, config rules, orchestration/verification protocols, Python cloud dispatch/harvest and host-native Antigravity subagent/task commands when available. Google Antigravity model inference, GitHub/Graphite, Cloud Run/GCS and third-party models remain external.
- Credited operating / distribution surfaces: `/poteto-mode` or `/agystack` routed engineering tasks; optional `/swarm`, `/arena`, `/interrogate`, `/loop`, project-scale Orchestrate and verified PR shipping; owner standing-orders and model-tier setup. First-party cloud dispatcher can execute/monitor jobs but a documented manifest alone is not evidence of a completed cloud fleet.
- Adjacent first-party surfaces excluded from ownership: External Antigravity platform guarantees, repo CI and this repository's unit tests, its author's own development/PR outcomes, optional off-repository project-specific checkers or user-composed procedures not included in the plugin.
- First-party operating / deployment modes considered: Installed Antigravity local model-assisted work, local branch-isolated parallel agents up to supported capacity, optional configured Cloud Run fleet, parallel adversarial model reviews with repro reruns, multi-PR project orchestrate and attended owner direction. No cloud execution was performed in this review.
- Recursion level: The operator's software project/program with its worker agents as operational S1 cells; named skill modes and reviewers do not automatically imply nested complete viable organizations.
- Reviewed revision: `93f43a58ade41ca8271499d3497154b2c6c3619d`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

agystack is a shipped Antigravity agent-skill/plugin harness rather than its own general LLM runtime. Its primary mode reads an operator task and routes to engineering playbooks, model-backed local subagents, optional Cloud Run jobs, source checks and user-visible artifacts. A project-level coordinator authorizes scoped worker briefs, exclusive write surfaces and separate verification. Swarm cloud workers produce patch diffs and test receipts, never push directly; the coordinator harvests and integrates verified candidates sequentially. Arena similarly uses isolated workspaces and cross-model judging before applying one base plus independently tested grafts. Orchestrate persists a project board, separate write owners, merge frontier, verified ledger, conflict/stacker ownership and human gates. Interrogate runs multi-model reviews against source diffs, reruns executable defect repros and returns a classified review verdict. The setup lets owners choose project-specific model policy and standing constraints. These are source-proven installed contracts and scripts, not an executed external autonomous engineering run.

## Operational model

The active task model chooses engineering work and uses Antigravity tools; large edits are assigned to scoped subagents who read source and return tested changes. For a multi-agent project, distinct workers hold private branches and report to a coordinating model. The coordinator chooses compatible outcomes, integrates only verified patches, reconciles PR status and handles cross-worker conflicts through exclusive ownership or serial patch adoption. For a persistent program it reads the project notes, ledger and current frontier to choose what should run next, reserving owner intervention for durable policy and actual permissions.

## S1 — Operations

- State: A
- Function: Execute model-directed investigation, design, implementation, test and code repair for a project task.
- Disturbance / variety regulated: Unanticipated code states, bugs, user requirements, test failures, program outputs and new artifacts.
- Decisive decision or feedback right: Choose a hypothesis, modification, verification step or tool call and revise it after test feedback.
- Decision owner: Installed Antigravity model-backed task or individual agent, subject to owner constraints and tools; model provider is external.
- Supporting / enforcement mechanisms: Shipped mode/playbooks, subagent dispatch, source editing tools, test commands and durable decision artifacts.
- Closure path: Model changes source/workspace, runs a check, observes output and chooses the next action or returns the tested change for owner review.
- Boundary reachability: `/poteto-mode` is the shipped top-level mode with explicit host-native tools and code-agent routing; `/loop` implements a bounded edit/verify/revert control for a model in a connected Antigravity session.
- Why this is / is not agent-owned: Model chooses substantive edits and task decisions; the deterministic verify command only supplies feedback.
- Evidence: [top-level routing and native tools](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/SKILL.md#L12-L40), [code-work delegation](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/SKILL.md#L97-L106), [edit and verify loop](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/loop/SKILL.md#L7-L53).
- Basis: structural
- Confidence: high
- Caveats: The host must supply Antigravity subagent/model and tool capabilities; this assessment did not execute a hosted model or external task.

## S2 — Coordination

- State: A
- Function: Attenuate inter-worker write/merge conflicts and competing patch integrations while multiple agent workers contribute to one shared software objective.
- Disturbance / variety regulated: Concurrent workers editing overlapping source and branches, PRs whose stacked dependencies conflict, speculative candidate patches that cannot be applied together without invalidating tests.
- Decisive decision or feedback right: Project coordinator chooses exclusive write scope and conflict owner, selects a verified candidate patch and serializes later grafts/merges after actual validation; stacker decides whether an integration is lawful at the active frontier.
- Decision owner: Model coordinator/stacker in the configured program/arena/swarm mode; deterministic tools provide git and test feedback, owner retains release policy.
- Supporting / enforcement mechanisms: One-writer per worktree, immutable scoped briefs, isolated cloud/local candidates, GCS patch delivery without remote pushes, PR stacker ownership and verified merge frontier.
- Closure path: Conflicting candidates remain isolated; coordinator uses source/test outcomes to choose a base, applies one candidate, rechecks, and only then integrates the next compatible one. Stacked conflict goes to owning stacker for resolution instead of independent workers rebasing blindly.
- Boundary reachability: First-party `/swarm` and `/arena` explicitly offer parallel branches and candidate integration; Orchestrate is a bundled model-directed multi-PR mode.
- Why this is / is not agent-owned: Choosing candidate compatibility and how to integrate depends on concrete worker outputs and current source conflicts, not merely a queue scheduler or arbitrary model chat.
- Distinct S1 units: Separate subagents/cloud workers produce independent code patches or experimental changes for the same project.
- Inter-S1 disturbance: Competing writes or PR stack conflicts can overwrite a peer's change or invalidate shared correctness and green merge frontier.
- Attenuating coordination relation: Exclusive brief worktree ownership, zero-push candidate patches, one owner for stack surgery and verified sequential merge.
- Feedback into subsequent S1 behaviour: Coordinator inspects conflict/test evidence, sends a revised brief/fix to the responsible agent or rejects a candidate, and rebaselines subsequent patches against the accepted source.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Source explicitly names collisions, exact write ownership, and sequential verification of contested patch adoption, not only dispatch or results exchange.
- Evidence: [exclusive worktree/stacker protocol](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L17-L21), [stack safety](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L78-L90), [patch integration and verification](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/swarm/SKILL.md#L142-L161), [competing worktree graft](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/arena/SKILL.md#L21-L59).
- Basis: structural
- Confidence: medium
- Caveats: Opt-in concurrent modes required. The cloud dispatcher cannot establish semantic compatibility by itself; model coordinator and actual project verifier must return feedback before integration.

## S3 — Inside-and-now control

- State: A(P)
- Function: Govern a multi-worker project/program's current task queue, work allocation, verification frontier, execution budgets and stalled operations.
- Disturbance / variety regulated: Too many overlapping workers, blocked stages, stale checks, late/zombie worker outputs, budget-exhausted jobs and unverified merges.
- Decisive decision or feedback right: Model coordinator chooses ready units, their scopes and model tiers, whether to refill/stop a worker wave, which verified work to land and which broken unit to replan; owner sets the mandate, risk budget and reserved gates.
- Decision owner: Coordinator model for the active program mode; human operator for standing orders, authorized compute and policy exceptions.
- Supporting / enforcement mechanisms: Durable `notes.md`, `ledger.md`, `frontier.md`, `gates.md`, status projection, cloud dispatch preflight and liveness, separate verifier role and run receipts.
- Closure path: Child status/check returns update the project-wide ledger/frontier; coordinator rescopes work or integrates a verified unit and recalculates next ready assignments, while human approvals remain parked in `gates.md`.
- Boundary reachability: Shipped Orchestrate playbook defines one coordinator, sub-coordinators only when needed, rolling worker windows and explicit loop/drain protocol; `/swarm` supports local/cloud status aggregation.
- Why this is / is not agent-owned: The model makes current project prioritization and allocation decisions; the mutable tables and CLI monitors are evidence, not themselves autonomous managers.
- Whole-system current view: Project-wide notes and verification ledger list active units/PRs, owners, head hashes, conflicts and statuses rather than only one worker's local task history.
- Current-control decision scope: Release a ready worker slot, prevent overlap, react to a failed verification, keep/stop a provider job, and choose a verified merge frontier.
- Evidence: [coordinator/worker levels](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L15-L21), [durable current board](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L25-L34), [queue drain and conflict handling](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L69-L99), [cloud liveness/harvest](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/swarm/SKILL.md#L99-L162).
- Basis: structural
- Confidence: medium
- Caveats: Plain single-chat coding does not show multi-worker S3. The model holds current-control choices only in the selected project orchestration mode, not in an autonomous external organization.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Coordinator model | Rolling worker completions, conflicting branches, failed verification and current budget | Reassign/replan, advance verified frontier and update task board | [queue/drain](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L69-L99) |
| Parent (`P`) | Project owner | Scope/budget/standing-order or reserved human gate | Project preferences/gates constrain next worker brief and authorization | [standing orders](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L25-L55) |

## S3* — Complementary audit

- State: C
- Function: Construct a separate evidence-seeking reviewer/verifier track that probes claims made by ordinary coding workers rather than trusting their own success message.
- Disturbance / variety regulated: A worker or review model can claim a defect is fixed, a merge-ready head is green or an alternative patch is superior without objective reproducible evidence.
- Decisive decision or feedback right: Separately tasked reviewers investigate actual code/diffs, provide executable repros and an independent checker/lead reruns them to decide whether a finding or candidate survives.
- Decision owner: Configured independent review-model subagent(s) and coordinator for verification/acceptance; project owner for final release mandate.
- Supporting / enforcement mechanisms: Shipped `/interrogate` multi-model review panel with parallel subagent launches and mandatory empirical repro; `/arena` external cross-judge; Orchestrate's differently tiered verifier worker and ledger.
- Closure path: Reviewer independently reads code, issues a reproducible claim, coordinator reruns it against current source, rejects non-reproducing findings and directs repair/handoff; a separate PR verifier can block a not-green source head.
- Boundary reachability: Installed `/interrogate` defines three model tiers and actual `invoke_subagent` roles plus rerun command, while `/show-me-your-work` offers cross-model trail audit; these paths require deliberate invocation/configured host roles.
- Why this is / is not agent-owned: Ordinary model-worker output does not substitute for separately opened code and rerun defect evidence; a role labeled reviewer without actual separate source access and reruns would not qualify.
- Claim being audited: Candidate worker's code-correctness, defect resolution and shippability assertions.
- Ordinary reporting path: Worker emits patch and task completion / PR status to project coordinator.
- Complementary access path: Independent reviewer subagent receives source diff and surrounding files, examines failure pathways, produces a runnable repro; lead/verifier reruns on actual source.
- Independence boundary: Reviewer roles are separate first-party dispatch with different model tiers and source views; no guarantee of distinct providers or blind contexts on `inherit` mode, so grade is bounded to constructible configured independent channel.
- Who acts on findings: Coordinator rejects a failing candidate or sends a repair unit, and project owner decides release through applicable gates.
- Evidence: [separately tasked reviewers and reproducibility](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/interrogate/SKILL.md#L11-L85), [verification ownership separate from worker](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L17-L21), [independent verdict before shipping](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/shipping.md#L1-L26), [cross-judge source review](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/arena/SKILL.md#L43-L59).
- Basis: structural
- Confidence: medium
- Caveats: C is a first-party constructor for separately invoked evidence-based audit, not a live audit demonstrated in this review or an independent always-on S3* institution. Reviewers in `Workspace: inherit` share project context and may not be blind. The model's claimed independent verification is not proof absent actual repro/execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped outside-environment prospective sensing-to-project-capability adaptation loop was established beyond current engineering plans.
- Disturbance / variety regulated: Future changes in project APIs, tool capability, cloud pricing, external deployment conditions and organizational skill repertoire.
- Decisive decision or feedback right: `/why` can search external evidence and architects can propose future improvements on demand, but project coordinator primarily chooses how to ship the current stated work.
- Decision owner: Human requests new project strategy or installs different skills; task model operates within present owner-selected mandate.
- Supporting / enforcement mechanisms: `why`, `architect`, technical investigation playbooks, cloud capability selection and `/reflect`.
- Closure path: A finished current task can propose a rule/skill revision, but no source-backed first-party actor continuously identifies external future threats/opportunities and returns an autonomous capability change into current project control.
- Why this is / is not agent-owned: Replanning after failed tests and choosing a better method for the present assignment is ordinary operational/current coordination, not itself the required outside-and-then intelligence function.
- Evidence: [routed present-task playbooks](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/SKILL.md#L16-L43), [Orchestrate project-scale scope](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L3-L12), [empirical current task tests](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/loop/SKILL.md#L19-L55).
- Basis: structural
- Confidence: medium
- Caveats: Operators may compose anticipatory market/technology monitoring workflows using the plugin, but such a first-party installed positive S4 actor with a future-capability return loop was not shown.

### Absence scope

- Surfaces inspected: Primary mode routing, research/why/architect/reflect, autonomous program and current checkpoint loop, swarm and arena, model configuration and external provider setup.
- Plausible first-party paths checked: Cloud pricing/auth preflight as environment intelligence, exploratory prototypes as future options, `/reflect` as learning, and long-term program coordinator as organization strategy.
- Why no material first-party path remains: These surfaces solve a current scope, detect execution affordances, or summarize learned task patterns; none owns a distinct prospective external distinction with candidate adaptation decision and an applied changed future operational capability.

## S5 — Policy and identity

- State: P
- Function: Legitimate operator defines the ongoing project mandate and binding governance for worker scope, verification threshold and reserved approvals.
- Disturbance / variety regulated: New agents or late resumed work could lose owner constraints, widen prohibited paths, overspend or misclassify unverified release as accepted.
- Decisive decision or feedback right: Decide standing model policy, forbidden paths, human gates, release authorization and level of evidence required across program work.
- Decision owner: Operator as installed project parent, not the auto-selected coordinator model.
- Supporting / enforcement mechanisms: User-supplied `preferences.md` standing-orders register, per-agent brief constraints, `gates.md`, setup-selected model tiers/rules, mandatory verification and project decision trail.
- Closure path: Owner states project policy → coordinator persists it in standing-orders and gates → each subsequent worker spawn/resume receives the binding restrictions → project work and final acceptance remain within the mandate.
- Boundary reachability: Orchestrate playbook directly requires `preferences.md` be created before dispatch and pasted into every spawned brief; setup skill selects model tiers and plugin rules used by later tasks.
- Why this is / is not agent-owned: Owner's durable organization-wide purpose and authority envelope governs future workers; the model cannot convert a passing test into permission to violate owner-reserved gates.
- Identity / ultimate-policy issue: What kind of work and degree of autonomous permission the project organization may undertake, as an enduring standing order rather than an individual tool request.
- Ultimate authority in each claimed mode: Human project owner for the mandate, releases and material policy changes; no general nonhuman S5 actor or unconditional model self-policy.
- Return-to-operation path: Persisted owner preferences/mandate → new and resumed worker instructions and gates → enforced owner-described scope decisions in subsequent model actions and verified PR landing.
- Evidence: [standing orders and human gates](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/orchestrate.md#L25-L55), [operator-configurable models](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/SKILL.md#L97-L106), [verified stop/landing ceiling](https://github.com/jtaroreh/agystack/blob/93f43a58ade41ca8271499d3497154b2c6c3619d/skills/poteto-mode/playbooks/shipping.md#L1-L27).
- Basis: structural
- Confidence: medium
- Caveats: These are textual human-parent contracts interpreted by models, not first-party hard security isolation; the host may enforce additional independent permissions. A project-local operator's policy is not the OSS maintainer's policy.

## Distributed OSS parent arrangement

agystack upstream maintainers author generic skill specifications. They are not the S3/S5 parent of each deployed project. The installed project's human owner controls the standing mandate, model availability and reserved approval rules, and host Antigravity manages technical tool permissions.

## Self-hosted and non-human modes

Local branch agents and cloud fleet workers have differing execution and data boundaries. Cloud work requires configured paid credentials, project IAM and matching runtime; no provider-specific success was claimed. A single Antigravity task without configured parallel agents cannot borrow S2/S3 multi-worker positives from an unused cloud manifest. Independent review is constructible via separate model roles plus source repros but not automatic or context-isolated in all modes.

## Recursion

The complete project/program is the assessed recursion. Workers perform distinct software tasks but do not acquire separate independent S3–S5 authority just because the host spawns a subagent. Track coordinators are conditional scoped control, not demonstrated autonomous viable subsidiaries.

## Variety and escalation

Exclusive writer scope, patch-only cloud returns and verified sequential grafts reduce competing edit variety. Project status, ledger and merge frontier support current control; empirical independent review supplies constructible complementary audit; owner standing orders govern final policy and escalation.

## Evidence gaps

Source-only frozen-commit assessment. No local Antigravity subagents, Cloud Run jobs, GitHub PR shipping operation, independent reviewers or model inference were actually run here. Skills are actionable first-party instructions plus dispatch scripts, not provider-executed evidence. Especially, separate-model and empirical verification claims are structural design requirements until tested in the host; no independent S3* audit result or S4 future strategy was manufactured.
