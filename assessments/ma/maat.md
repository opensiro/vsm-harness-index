---
harness_id: maat
project_name: Maat
repository: https://github.com/mohannadrabie/maat
review_ref: bf57b4b5013960b2aa34eb8c707f77d587f5b93e
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

# Maat

## Review boundary

- System in focus: One installed Maat agentic software-delivery team operating through the Claude Code or GitHub Copilot plugin on a user-owned software project, with its generated project docs, agents, commands and scripts.
- Purpose and identity: Turn human-approved change requirements into reviewable, tested, policy-compliant changes without silently merging or waiving owner-reserved constraints.
- Relevant environment: User stories, mutable project source, tests and CI, ADR constraints, specialist review disagreements, security findings, risk/exposure, branch state and GitHub issues.
- Standard-distribution boundary: Shipped `/maat:ship`, `/maat:review`, `/maat:verify`, `/maat:audit` and `/maat:resolve` command/skill contracts, manager and specialist definitions, init-generated project documents, receipt-check/ADR-cache/run-log scripts. Underlying Claude/Copilot model execution, external GitHub permissions and user project implementations are external.
- Credited operating / distribution surfaces: Installed plugin commands and model-invoked agents, initialized state/reports/ADR cache and receipt validation, user plan/merge intervention, optional reviewer-team mode.
- Adjacent first-party surfaces excluded from ownership: Maat's own maintenance tests and CI, unrelated repo governance, opt-in generated example GitHub Actions not enabled by install, third-party model runtime internals, and any user-composed reviewers outside first-party commands.
- First-party operating / deployment modes considered: Normal initialized project in Claude Code/Copilot; standard parallel domain + cross-domain reviews, critical risk path, model manager deadlock resolution and design-council escalation; independent on-demand `/maat:audit`; no claim that every host natively runs agents with separate isolated contexts.
- Recursion level: A single software project delivery organization across distinct implementation/review operational units. Not every specialist is a separate complete VSM recursion.
- Reviewed revision: `bf57b4b5013960b2aa34eb8c707f77d587f5b93e`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Maat is principally an executable agent/skill specification delivered to a host coding agent, with auxiliary Node scripts rather than a standalone multi-agent daemon. The manager reads requirements, sends work to specialists, ratifies a risk tier, carries review findings to verification, audits provenance and hands off human-only merge. Domain reviewers and a standing cross-domain reviewer examine the same change in parallel. The Manager resolves conflicting decisions and, after bounded recurrent failure, calls a three-specialist design council. Reviews persist full reports, structured receipts, issue/log entries and ADR constraints. A native `receipt-check.mjs` detects contradictory report receipts, missing checks or evidence and stale HEAD. Its output is advisory and always exits zero; human/model decisions are needed to act on flagged discrepancies. User-approved project goals, ADR law and actual merge remain outside the agent's authority.

## Operational model

The host model and specialized subagents choose how to plan/implement/test a user story and inspect the candidate change. Risk-graded reviewers make distinct code-specific judgments, potentially conflicting. Manager receives returns, chooses whether to rework, reconcile, escalate or release a human-ready handoff within binding ADR and safety constraints. Optional `/maat:audit` examines past reviewers' record and credibility from report evidence and prior outcomes, distinct from per-story review. Runtime execution is dependent on the host's enabled plugin/agent capabilities and project setup; source-based reachability is shown, not an executed Claude/Copilot trace.

## S1 — Operations

- State: A
- Function: Perform model-driven software design, implementation, review, tests and debugging in the approved project.
- Disturbance / variety regulated: Unstructured requirements, unpredictable code/test results, reviewer findings and task-specific design constraints.
- Decisive decision or feedback right: Specialist model selects plan details, code changes, tests or findings using project context.
- Decision owner: Deployed model-driven specialist/implementer under its assigned scope; Manager owns dispatch but does not replace the worker's substantive work.
- Supporting / enforcement mechanisms: Plugin command and agent definitions, project docs and check/report persistence.
- Closure path: A specialist produces a plan/change/review with evidence and returns it to the Manager for acceptance or another concrete operation.
- Boundary reachability: Shipped `/maat:ship`, `story-implementer`, `test-writer`, `/maat:review` invoke first-party role definitions in supported host plugins.
- Why this is / is not agent-owned: Model chooses work and reviewer judgments; static stage scripts and external model host only route/execute the decision.
- Evidence: [ship stages](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/ship.md#L6-L34), [manager ownership](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L8-L26), [installed commands](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/README.md#L42-L88).
- Basis: structural
- Confidence: high
- Caveats: The model host must support these roles and tools; neither a host session nor full delivery run was executed in this review.

## S2 — Coordination

- State: A
- Function: Resolve conflicts between distinct specialist review decisions and prevent cross-domain gaps from producing incompatible change acceptance.
- Disturbance / variety regulated: Domain reviewers can disagree on scope, risk tier, severity or ADR applicability; changes across application and infrastructure seams may fall between reviewers.
- Decisive decision or feedback right: Select which specialist finding is supported, determine the real disputed interaction, route ADR ambiguity, choose further work or request an owner ruling when reserved law is involved.
- Decision owner: Model-driven Manager after reading the conflicting evidence; human remains final authority where policy forbids a ruling.
- Supporting / enforcement mechanisms: Two or more independently tasked reviewer reports, standing cross-domain reviewer over whole ADR catalog, explicit deadlock-resolution matrix and design council conditions.
- Closure path: Manager reads conflicting persisted reports, rules on factual disagreement or escalates the ADR, and sends a revised action to the implementation/review loop instead of allowing simultaneous incompatible approvals.
- Boundary reachability: Standard `/maat:review` runs domain+cross-domain reviewers in parallel and invokes Manager on disagreement; `/maat:resolve` is first-party command.
- Why this is / is not agent-owned: Manager must interpret real conflicting claims and choose a correction, not just sequence tasks or copy reviewer messages; the static reopen checker alone is not S2.
- Distinct S1 units: Domain and cross-domain reviewers are separate model-backed task roles with independently persisted conclusions over the same change.
- Inter-S1 disturbance: Contradictory acceptance/risk findings and uncovered cross-domain constraints lead to incompatible downstream approval.
- Attenuating coordination relation: Whole-catalog cross-domain pass plus Manager evidence-based deadlock resolution and bounded council escalation.
- Feedback into subsequent S1 behaviour: Manager's ruling, named blocker/unlock and revised review/implementation stage change the work or direct a fresh targeted review; unresolved human-only dispute blocks handoff.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The explicit source procedure recognizes real conflicting reviewer verdicts, opens full evidence and rules on the contested obligation, rather than merely passing specialist outputs.
- Evidence: [parallel reviewer disagreement](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/review.md#L11-L36), [manager conflict resolution](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L133-L169), [cross-lane checks](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/cross-domain-reviewer.md#L11-L38), [council stop/return](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L79-L97).
- Basis: structural
- Confidence: medium
- Caveats: The evidence concerns incompatible review findings, not generalized scheduling/resource conflict between independent build workers; absent actual reports in a specific run, this is structural first-party decision reachability, not observed conflict resolution.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the current delivery team's workload, risk-level review intensity and whether a change is eligible to advance to merge handoff.
- Disturbance / variety regulated: Too many review loops, incomplete evidence, conflicting reviewers, wrong review ceremony for change risk and unexamined blockers.
- Decisive decision or feedback right: Ratify change risk tier, select specialist lanes and remediation priority, triage exposure, enforce bounded repeated-review decisions, and stop when a project-wide blocker is unresolved.
- Decision owner: Model Manager for ordinary tier/triage/dispatch; human owner for plan approval, exceptional governance and final merge.
- Supporting / enforcement mechanisms: Project state/risk tier, persisted reports, exposure triage, review-round counters, ADR-cache, CI state, blocker and council gates.
- Closure path: Decided tier controls the next reviewer set; reviewed evidence changes current work selection or stops/redirects it; human ratification re-enters the implementation loop.
- Boundary reachability: Normal `/maat:ship` manager and `/maat:review` paths, with the installed project's current state and optional team mode.
- Why this is / is not agent-owned: Model makes bounded current-control decisions using reports and active project work; deterministic counters/checks enforce stop conditions, while owner retains separately reserved gates.
- Whole-system current view: State file tracks project stage and tier; reviewer results and reports, run-log and required checks span implementation, review, verification and the handoff.
- Current-control decision scope: Current risk/coverage and reviewer assignment, whether another review round is justified, which remediation takes precedence; parent can halt or withhold approval.
- Evidence: [risk tier and stages](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/ship.md#L14-L40), [reviewer selection](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/review.md#L9-L33), [triage and stop](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L99-L115), [bounded council path](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L79-L96).
- Basis: structural
- Confidence: medium
- Caveats: Manager cannot merge, waive an accepted ADR or decide owner-only spending/risk approvals. No autonomous cross-project S3 of all Maat installations is implied.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Manager model | Current reviewer findings, risk tier and repeated failure | Selects lanes/triage/redirects within binding rules | [manager/ship](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/ship.md#L25-L40) |
| Parent (`P`) | Project owner | Plan requires ratification; final merge or hard ADR exception | Approves change of mandate or refuses handoff, governing later run | [hard gates](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L38-L43), [merge reserved](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/ship.md#L55-L64) |

## S3* — Complementary audit

- State: C
- Function: Construct a distinct review-of-review evidence channel that checks whether specialist receipts and the Manager's claimed checks actually match persisted reports and observed repository state.
- Disturbance / variety regulated: An agent may overstate tests, silently omit a finding, misreport severity or conceal a stale review.
- Decisive decision or feedback right: An on-demand audit actor samples accumulated review artifacts and judges evidence credibility; report-check script identifies concrete suspected mismatches requiring independent full read.
- Decision owner: User-invoked audit model (periodic /maat:audit), separate from the authoring reviewer role; the operator may decide remediation. Mechanical script is not an autonomous auditor.
- Supporting / enforcement mechanisms: Persisted complete reviewer reports and raw check outputs, Git HEAD and bug issue state, report-vs-receipt reconciliation, per-reviewer audit scorecard and run-log.
- Closure path: Script flags `REOPEN`/`UNREAD`, a separately invoked audit actor reads original reports and observed check/issue evidence, issues a credibility finding, and Manager adjusts trust/review routing or owner requests correction.
- Boundary reachability: First-party `/maat:audit` and `receipt-check.mjs` are installed commands, with existing persistent report/state surfaces; additional human/sample invocation makes the audit constructible, not an always-on autonomous check.
- Why this is / is not agent-owned: The supplementary audit is distinct from ordinary reviewer work; the script comparing self-authored receipts alone cannot prove independently that tests actually ran, and the full-read/audit step must consult evidence beyond the producer's summary.
- Claim being audited: Reviewer/Manager statements about findings, checks, ADR compliance and acceptable handoff.
- Ordinary reporting path: Specialist's `RECEIPT:` block and Manager summary passed forward.
- Complementary access path: Separate periodic audit reads report body, raw command output, actual Git HEAD/issue traces, past findings and manager decisions, not only current reviewer summary.
- Independence boundary: Separate audit invocation and actor are constructible from first-party commands; the host does not enforce distinct model identity, blind context, or isolation from the producer.
- Who acts on findings: Manager and/or project owner revise review depth, task status, auditor assignment or stop decisions.
- Evidence: [audit actor sampling](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/audit.md#L1-L39), [mechanical contradiction checks](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/scripts/receipt-check.mjs#L235-L314), [full-body cross-check](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/verify.md#L14-L36), [manager audit limits](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L21-L32).
- Basis: structural
- Confidence: medium
- Caveats: C is restricted to user-composable supplementary audit with an actual separate evidence read; it is not a first-party independent S3* institution automatically running in every project. The script always exits zero, and plugin command prose does not demonstrate a runtime execution trace or guarantee independence. If no separate audit actor is available at deployment, this path is not active.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party installed prospective external sensing → capability adaptation loop demonstrated for the project organization itself.
- Disturbance / variety regulated: Future architectural/market changes, new constraints, upcoming platform or dependency shifts might motivate strategic adaptations.
- Decisive decision or feedback right: Impact analysis and future cost comparisons are available within requested project tasks, but standard manager decisions concern current change shipping and reviewer conflicts.
- Decision owner: The human project owner may request future planning or ADR amendments; the installed Manager is scoped to bounded present delivery decisions.
- Supporting / enforcement mechanisms: Impact-analyst, architecture-reviewer, design council, ADR amend command, source-based CI/quality checks.
- Closure path: Design council may choose an option for resolving present blocked work, not an autonomous future-environment diagnosis that reconfigures the organization's capabilities.
- Why this is / is not agent-owned: Long-horizon-looking architecture advice and a plan to fix today's blocked change are not by themselves an outside-and-then intelligence loop.
- Evidence: [council stop conditions](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L79-L97), [conformance remediation](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L193-L200), [change-stage purpose](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/ship.md#L21-L39).
- Basis: structural
- Confidence: medium
- Caveats: A user can compose prospective architecture research from these agents. That uninstalled specific construction is not credited as a positive S4 closure.

### Absence scope

- Surfaces inspected: Manager roles, `ship`, `challenge`, `council`, `review`, `audit`, `adr-amend`, impact/architecture reviewer and local state/CI scripts.
- Plausible first-party paths checked: Design council as strategic intelligence, impact analyst as external-environment sensing, reviewer trend/auditor dashboard as anticipatory warning and ADR amendment as adaptation.
- Why no material first-party path remains: The shipped decisions fix or route the current user's software delivery and adjust local review process after internal evidence; none establishes a prospective environmental distinction, distinct candidate options and lawful return to changed future project capability.

## S5 — Policy and identity

- State: P
- Function: Legitimate owner chooses project mission and binding ADR/approval rules for its software-delivery organization.
- Disturbance / variety regulated: Model-chosen shortcuts or convenience pressure could override project law, safety/critical change criteria, owner approval or final merge decision.
- Decisive decision or feedback right: Adopt/modify accepted ADRs and project charter, approve plan/design boundaries and reserve final merge/apply; disallow model waivers of binding rules.
- Decision owner: Project owner/authorized human, not agent Manager or source maintainers.
- Supporting / enforcement mechanisms: Project `CLAUDE.md`, `PRINCIPLES.md`, accepted ADRs and `maat.json`, owner approval stages and persistent plan/risk record.
- Closure path: Human adopts a rule/goal/approved plan → project policy/ADR/state files persist it → manager and reviewers read it for subsequent tasks and risk selection → violative change is blocked or owner legitimately changes the policy.
- Boundary reachability: `/maat:init` creates owner-editable charter/ADR inputs; `/maat:ship` and `/maat:verify` consult those rules in ordinary workflow.
- Why this is / is not agent-owned: Ultimate standards and the release mandate stay human-owned; agent ratification of a risk tier is delegated S3 current control under S5, not autonomous ultimate policy.
- Identity / ultimate-policy issue: Which architectural and safety commitments count as the project's enduring law across stories, beyond one tool approval.
- Ultimate authority in each claimed mode: The legitimate project owner. ADR changes require approved amendment process; no unconditional model authority or nonhuman S5 mode established.
- Return-to-operation path: Owner charter/ADR rule → cached/persisted project policy → future plan risk tier and full-catalog checks → block/accept following implementation/review decisions.
- Evidence: [owner-only policy limits](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/agents/manager.md#L38-L43), [accepted ADR priority](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/README.md#L82-L106), [project init charter/ADR setup](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/README.md#L250-L295), [verify gates](https://github.com/mohannadrabie/maat/blob/bf57b4b5013960b2aa34eb8c707f77d587f5b93e/commands/verify.md#L6-L22).
- Basis: structural
- Confidence: medium
- Caveats: Human review of individual PR alone would not qualify; claimed P rests on persistent binding organization-wide ADR and project law changing subsequent agent choices.

## Distributed OSS parent arrangement

Maat maintainers publish its plugin templates, but the project owner's installed `CLAUDE.md`, ADR constraints and merge rights are the legitimate parent at this recursion. A GitHub maintainer's upstream rules are not imported as an S5 decision of an arbitrary customer project unless adopted by the owner.

## Self-hosted and non-human modes

The normal plugin may be installed in more than one host; feature reachability is conditional on host plugin commands and subagent support. Concurrent reviewer assignments do not automatically guarantee separate inference identities or memory isolation. Only an explicitly invoked and evidence-separated audit actor supports the bounded S3* constructor grade.

## Recursion

The delivery project is the organization whose current outputs and reviews are governed; its implementation and reviewer agents are operational cells. A named agent, role or subagent is not automatically a viable autonomous S1+metasystem recursion. There is no installed whole-company strategic function inferred from the plugin's mythology.

## Variety and escalation

Risk tiers allocate scarce review attention; cross-domain pass and manager conflict resolution attenuate disagreement; independent report/receipt audit can call for reopens; hard owner-only gates prevent unauthorized change approval. Every claim is bounded to configured first-party plugin paths and source inspection.

## Evidence gaps

Read-only pinned-source review; no live Claude Code/Copilot installation, model execution, independent human audit or customer project change was run. The auxiliary validator exits zero and its output is advisory; it is not security enforcement. S2 and S3 positive closures are structural model-in-the-loop instructions, not empirical successful runtime decisions. S3* C is only a constructible independent audit path, not proof of neutral auditor isolation or check correctness.
