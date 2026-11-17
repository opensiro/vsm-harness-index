---
harness_id: hive-workflow-engine
project_name: Hive (workflow engine)
repository: https://github.com/ivankuznetsov/hive
review_ref: 9229e25af42398979a8b11ff923e98471f55f543
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Hive (workflow engine)

## Review boundary

- System in focus: Native local Hive Ruby CLI and daemon managing one project, supported coding and review workflows and optional post-merge Patrol.
- Purpose and identity: Run durable agent stages from human idea to PR, review and handoff without losing evidence, and enable controlled future workflow adaptation.
- Relevant environment: Git worktree and Hive state branch, installed external agent CLIs, GitHub PR service and legitimate local project owner.
- Standard-distribution boundary: Shipped coding/content workflows, stage markers, model-backed CLI stage runners, dependency admission, review/fix, status and opt-in Patrol.
- Credited operating / distribution surfaces: Native CLI/daemon, task/artifact state, coding and reviewer agents, operator status/approval and opt-in post-merge source review.
- Adjacent first-party surfaces excluded from ownership: Developer CI/dogfood, unrelated hosted cloud product, test-only fixtures, unpublished import features, upstream GitHub maintainer authority.
- First-party operating / deployment modes considered: Native coding-stage daemon, project-level operator-supervised control, separate reviewer processes and enabled optional architecture Patrol.
- Recursion level: One local project task organization whose model-backed stage agents form S1 units; project owner is the legitimate parent.
- Reviewed revision: 9229e25af42398979a8b11ff923e98471f55f543.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Hive is a Ruby workflow engine with task folders on a separate state branch, worktree-based code changes and stage-specific model-backed CLI subprocesses. It runs from idea through brainstorm, plan, execute, PR creation, distinct review, artifact collection and finalize. Source-level reviewer passes inspect exact changes and can return fixes to execution/review loops. The operator receives current queue and recovery decisions. Optional Patrol and Architecture Patrol discover post-merge maintenance issues and route them to a distinct Patrol Fix workflow, whose proposed PRs still depend on maintainer acceptance. [README.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/README.md); [docs/concepts.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/concepts.md); [docs/architecture.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/architecture.md); [wiki/stages/review.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/stages/review.md).

## Operational model

A model-backed agent owns task-specific artifact and code decisions, while stage/branch admission is a deterministic guard. Interdependent project branches are regulated through explicit dependency policy. Model reviewer processes use independent source/CI evidence and can trigger repair. Parent owner approves current exceptional recovery and durable workflow policy. Post-merge architecture intelligence provides optional future-capability choices with owner-governed PR acceptance; source changes are not assumed merely because a PR was opened.

## S1 — Operations

- State: A
- Function: Execute an authored task via model-backed stage agents and durable artifacts
- Disturbance / variety regulated: Uncertain requirements, implementation choices and tool results
- Decisive decision or feedback right: Choose research, planning, code edits and task-specific responses within an admitted stage
- Decision owner: External model-backed agent CLI spawned by Hive as a supported workflow stage
- Supporting / enforcement mechanisms: Ruby stage runner, CLI profiles, tracked stage markers, state and code worktrees
- Closure path: Stage agent writes artifact/commit; daemon checks marker and advances or returns for correction
- Boundary reachability: Installed coding/content workflows invoke actual configured Claude/Codex/Pi/Grok/other supported CLI processes
- Why this is / is not agent-owned: The agent decides task content; Hive's deterministic machinery transports and validates results, rather than originating a code plan
- Evidence: [docs/concepts.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/concepts.md); [docs/architecture.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/architecture.md); [README.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/README.md)
- Basis: structural
- Confidence: high
- Caveats: Installed and authenticated model CLI is required; no live model run was performed

## S2 — Coordination

- State: C
- Function: Attenuate interference between dependent task worktrees and their shared project branch
- Disturbance / variety regulated: Concurrent task branches may rely on unfinished prerequisites or incompatible Git bases
- Decisive decision or feedback right: Apply dependency gate, reject cycles, select stacked or unstacked branch base, and withhold an ineligible task
- Decision owner: First-party deterministic task dependency admission with operator-authored dependency declarations
- Supporting / enforcement mechanisms: Stage-gated depends_on edges, cycle detection, worktree pointers, stable task metadata
- Closure path: Unmet dependency blocks admission until prerequisite stage and branch evidence change; later work inherits the valid base
- Boundary reachability: Packaged workflows and CLI/daemon resolve the dependency graph for real project tasks
- Why this is / is not agent-owned: This S2-specific coordination path exists but has no agent-owned discretionary resolution; autonomous choice requires composition
- Distinct S1 units: Separate coding-agent tasks with isolated feature worktrees within a shared repository
- Inter-S1 disturbance: Dependent work may use a stale or incompatible base before a prerequisite completes
- Attenuating coordination relation: Dependency edge and branch stacking/fan-in policy validated at scheduling and execution
- Feedback into subsequent S1 behaviour: Stage transition releases dependency gate and selects correct future task base
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The protocol checks real inter-task branch dependencies and cycle/integration hazards, beyond simply passing messages or order
- Evidence: [wiki/decisions.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/decisions.md) (ADR-056); [docs/concepts.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/concepts.md); [docs/architecture.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: No general autonomous cross-task conflict negotiation claimed

## S3 — Inside-and-now control

- State: P
- Function: Current portfolio control of project tasks, blockers, retries and recoverable workflow commitments
- Disturbance / variety regulated: Provider limits, errors, waiting questions and stale CI can block multiple ongoing tasks
- Decisive decision or feedback right: Choose what to retry, answer, hold, approve or grant using a fresh operational-action observation
- Decision owner: Legitimate local project operator using TUI, native web, bot or CLI
- Supporting / enforcement mechanisms: Durable operational status/action descriptors, journal, leases, daemon recovery and error markers
- Closure path: Operator command changes task state/permission so the daemon can dispatch or recover subsequent work
- Boundary reachability: Shipped hive status --operational, hive act, review-grant and TUI all expose this live path
- Why this is / is not agent-owned: The daemon computes readiness but does not own the substantive owner-granted decision to escalate or resume blocked work
- Whole-system current view: Registered project task queue, running stages, blockers, scheduler freshness and action descriptors
- Current-control decision scope: Live task dispatch, recovery authorization, review grants and human escalation at one project recursion
- Evidence: [lib/hive/operational_status.rb](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/lib/hive/operational_status.rb); [wiki/stages/review.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/stages/review.md); [README.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/README.md)
- Basis: structural
- Confidence: high
- Caveats: A machine-readable status API alone would not confer autonomous S3

## S3* — Complementary audit

- State: A
- Function: Independently assess implementation changes from direct code/CI evidence and return corrective findings
- Disturbance / variety regulated: Implementation agent can produce flawed or unverified patch despite reporting success
- Decisive decision or feedback right: Review actual patch and tests, issue findings and approve/reject before finalization
- Decision owner: Independent review-stage model agent process, distinct from execute agent; separate triage routes findings
- Supporting / enforcement mechanisms: Per-reviewer separate process, role-specific prompt, immutable review files, exact-head CI gates, bounded fix-pass ledger
- Closure path: Reviewer findings return to triage/fix and trigger new verification on updated exact PR head before completion
- Boundary reachability: The default coding workflow includes a shipped 6-review stage with configured independent agent reviewer adapters
- Why this is / is not agent-owned: Model-backed independent reviewers decide the substantive findings; Ruby rules enforce pass/merge conditions only
- Claim being audited: Implementer says its branch satisfies requirements and is ready for PR finalization
- Ordinary reporting path: Implementation stage marker, code commit and worktree output
- Complementary access path: Independent subprocess directly inspects diff, task details, CI and project tests
- Independence boundary: Fresh isolated model session and review prompt, distinct from implementing agent; models can still share provider
- Who acts on findings: Triage/fix agent and final stage gate; operator decides unresolved escalations
- Evidence: [wiki/stages/review.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/stages/review.md); [lib/hive/reviewers.rb](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/lib/hive/reviewers.rb); [docs/concepts.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/concepts.md)
- Basis: structural
- Confidence: high
- Caveats: Supported shipped reviewer configuration only; not a witnessed independent OpenSiro S3* audit

## S4 — Outside-and-then intelligence

- State: P
- Function: Post-merge architecture observation and prospective project improvement via Patrol and Patrol Fix
- Disturbance / variety regulated: Source architecture may drift, duplicate components or weaken boundaries after new features
- Decisive decision or feedback right: Generate and route source-backed refactoring theses; accept or decline proposed future source changes
- Decision owner: Patrol agent produces candidate options; legitimate project maintainer decides acceptance/merge in the parent-governed mode
- Supporting / enforcement mechanisms: Merged-PR manifests, read-only architecture reviewer, evidence-checked snippets, immutable findings, separate Patrol Fix workflow
- Closure path: Post-merge change drives future refactoring proposal; an accepted maintainer merge applies a new source baseline used by later project tasks
- Boundary reachability: Packaged opt-in Architecture Patrol/Patrol Fix and native daemon operate on registered source repos, not test fixtures
- Why this is / is not agent-owned: An agent can propose improvements but may not unilaterally claim that its PR has been adopted; parent owns final integration
- External distinction: Changed default-branch source and architecture coupling revealed after completed features
- Future / prospective distinction: Refactoring thesis addresses later maintainability and capability, not just active task validation
- Adaptation option generated: Evidence-cited architecture thesis routed to fix/discuss/dismiss and Patrol Fix intake
- Path back into current capability / S3: Maintainer acceptance and merge changes tracked default branch; subsequent task worktrees use that updated capability
- Evidence: [docs/architecture.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/architecture.md); [wiki/modules/patrol.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/modules/patrol.md); [wiki/commands/refactor-patrol.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/wiki/commands/refactor-patrol.md)
- Basis: structural
- Confidence: medium
- Caveats: No live accepted external PR measured; post-merge workflow is an optional first-party mode and publication alone is not positive adopted-outcome evidence

## S5 — Policy and identity

- State: P
- Function: Constitute a local project's enduring workflow, role, stage approval and deployment/acceptance policy
- Disturbance / variety regulated: Agent autonomy and quality or publication behavior must remain within project owner's continuing purpose
- Decisive decision or feedback right: Select workflow descriptor, stage permissions, gate/approval policy and persistent settings
- Decision owner: Legitimate local project owner, with upstream maintainer retaining external PR acceptance authority
- Supporting / enforcement mechanisms: State-branch workflow YAML, validated stage permissions, protected policy snapshots, human decision markers
- Closure path: Owner-authored workflow is validated/persisted; later tasks and stage agents follow that accepted policy and refuse disallowed actions
- Boundary reachability: Native hive workflow commands, state branch, init and daemon load the owner-selected descriptor
- Why this is / is not agent-owned: Stage agents work inside the adopted policy but cannot unilaterally replace the ultimate project purpose or publisher rights
- Identity / ultimate-policy issue: What product/task pipeline Hive operates, what acceptable completion means and what decisions remain with its legitimate owner
- Ultimate authority in each claimed mode: Local project owner for workflow identity and external maintainers for upstream source acceptance
- Return-to-operation path: Persisted policy and stage bindings → next task admission → runtime permission and approval enforcement
- Evidence: [docs/workflows.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/workflows.md); [docs/permissions.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/permissions.md); [docs/architecture.md](https://github.com/ivankuznetsov/hive/blob/9229e25af42398979a8b11ff923e98471f55f543/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: Ordinary task approval alone does not establish S5; it is the project-wide durable policy that matters

## Distributed OSS parent arrangement

The local operator owns one installed Hive project's standing policy. External GitHub maintainers retain authority for acceptance of upstream PRs; an independent installation cannot infer organization-level authority from the existence of many contributors.

## Self-hosted and non-human modes

Native Hive can run admitted agent stages while no human is present, but exceptional approval and later PR merge decisions may still belong to a human. Its optional Patrol mode needs enablement, provider availability and source access. Externally operated models are tool/decision providers, not Hive-owned model weights.

## Recursion

One project's stage agents perform distinct operational units. Deterministic task dependency relations limit interference. A legitimate owner regulates the current queue and standing purpose. Separate model reviewers audit code/CI evidence. Opt-in Patrol creates future architectural adaptation proposals for parent acceptance.

## Variety and escalation

Unmet task dependencies, lost worker leases, stale PR heads, review exhaustion and provider limits retain explicit blocked states rather than false success. Accepted findings route to bounded fix/review passes. Future architecture proposals need legitimate integration before their outcome changes the project source.

## Evidence gaps

This is source-first review of the immutable original revision, without live multi-agent execution or direct witness of an accepted external Patrol fix. Review-agent independence is a shipped subprocess/ownership construct, not a separate OpenSiro S3* audit result. Post-merge S4 is source-constructible and parent-governed; proposal publication does not prove actual acceptance. The Index's existing hive entry refers to a separate repository (aden-hive/hive), so this source uses the distinct hive-workflow-engine identifier.
