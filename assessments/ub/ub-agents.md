---
harness_id: ub-agents
project_name: ub-agents
repository: https://github.com/uberblick-ai/ub-agents
review_ref: 883bc1e4a241a573facaeb025489be59e7cb3428
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# ub-agents

## Review boundary
- System in focus: One project deployment of the ub-agents launchers and starter issue-to-PR workflow using GitHub as operating state.
- Purpose and identity: Turn maintained GitHub issue commitments into independently reviewed pull requests under project-owned checks and approval policy.
- Relevant environment: Issues, PR heads, feedback, checks, merge conditions, provider CLIs and launcher coordination records on GitHub.
- Standard-distribution boundary: Packaged launcher, CLI, generated init starter roles and policy, worktrees, coordinator, operator monitoring, approved upgrade and restart paths.
- Credited operating / distribution surfaces: Model-facing starter roles, exact-head review, GitHub claim and outcome handling, operator interventions, shared-policy tailoring and controlled config reload.
- Adjacent first-party surfaces excluded from ownership: Upstream project dogfood, development/CI/release machinery, optional Uberblick service and external Claude Code/Codex internals.
- First-party operating / deployment modes considered: Local or server launchers, configured GitHub project, model CLI choices, optional cross-provider review, maintainer intervention, and supported release-aware continuation.
- Recursion level: One repository workflow across its configured launcher fleet. The repository maintainer is the legitimate external parent of that installation.
- Reviewed revision: `883bc1e4a241a573facaeb025489be59e7cb3428`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The launcher plans eligible GitHub items, elects a single renewable claimant, creates an isolated checkout and invokes the configured agent with shared instructions, role context and a report interface. Typed outcomes apply explicit label transitions and return accepted feedback to subsequent runs. The starter includes issue preparation, implementation, review and integration roles. Operators observe the queue and active lease state through status and monitor surfaces.

## Operational model

Independent issue and PR assignments form work units that produce checked issue scopes, code changes and integrated PRs. Roles possess constrained task discretion; a launcher arbitrates claims and enforces outcomes, while maintainers control admission, current exceptional decisions and the continuing workflow mandate.

## S1 — Operations

- State: A
- Function: Prepare work, implement changes and resolve bounded coding and integration decisions within the configured role.
- Disturbance / variety regulated: Varying issue scope, repository contents, exact PR heads, check outcomes and reviewer findings.
- Decisive decision or feedback right: Select implementation actions, tests, and a task outcome to report.
- Decision owner: First-party instructed model-backed role agent running via a configured CLI.
- Supporting / enforcement mechanisms: Assignment context, worktrees, run lease, tool permissions and typed outcome transitions.
- Closure path: Changed artifacts and outcome summaries persist to GitHub, and accepted observations enter later role runs.
- Why this is / is not agent-owned: The launcher dispatches and enforces policy. The assigned model selects substantive work and outcome.
- Boundary reachability: Init generates the role set and the normal launcher invokes one configured runtime under the matching trigger.
- Evidence: [starter dispatch and handoffs](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/how-the-loop-works.md#L9-L34), [assignment and feedback](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L138-L155), [execution contract](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L668-L706).
- Basis: structural
- Confidence: medium
- Caveats: A configured supported model CLI and GitHub access are prerequisites.

## S2 — Coordination

- State: —
- Function: Deterministic claim arbitration regulates real competition between work units. A publishable agentic S2 mode was not established.
- Disturbance / variety regulated: Two launchers can attempt the same item or an issue and its linked PR branch simultaneously.
- Decisive decision or feedback right: The earliest live claim wins and the losing launcher selects another eligible item by the shipped ordering rule.
- Decision owner: Run coordination implements fixed claim arbitration. Project admin supplies ordering and timing configuration.
- Supporting / enforcement mechanisms: Renewable claims, related work exclusion, GitHub rereads and operation-specific feedback.
- Closure path: Losing contenders withdraw and replan. Related branch work waits until the conflicting live claim or cleanup clears.
- Why this is / is not agent-owned: The collision winner is fixed by GitHub comment order before a model starts. A model does not choose how to settle the conflict.
- Evidence: [same-item and linked-branch exclusion](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L8-L21), [priority and losing-claim feedback](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L84-L136), [election and withdrawal](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L242-L259).
- Basis: structural
- Confidence: medium
- Caveats: A bounded absence of an A/C ownership arrangement. The shipped deterministic interference control is effective within its cooperative launcher contract.

### Absence scope

- Surfaces inspected: Claims and associated work, ordering/dependency gates, launcher-scoped selection and typed report feedback.
- Plausible first-party paths checked: Duplicate live assignments and issue/PR interference, priority and dependency adjustment, and candidate-review handoffs.
- Why no material first-party path remains: Timing and eligibility controls configure a fixed-arbitration protocol. No first-party decision slot delegates the choice of interference resolution to a composed autonomous coordination actor.

## S3 — Inside-and-now control

- State: P
- Function: Regulate current work commitments across the project queue when live work must stop, change priority or resume after an exception.
- Disturbance / variety regulated: Blocked items, overlapping deadlines, active leases and assignments that need owner input.
- Decisive decision or feedback right: Approve continued work, hold or stop a chosen current commitment, or restore the selected role to eligibility.
- Decision owner: Repository maintainer/operator with authority over project workflow labels and retry.
- Supporting / enforcement mechanisms: Project-wide status and monitor, GitHub stop/trigger labels, lease renewal check and retry command.
- Closure path: A stop label cancels the affected live run during renewal. A returned answer and retry or restored trigger determine subsequent execution under the same queue.
- Why this is / is not agent-owned: Model roles can report an exception while trusted GitHub state records the operator's current-control disposition.
- Boundary reachability: Standard monitor/status views, eligible GitHub operator actions and the retry CLI are shipped.
- Whole-system current view: Status exposes running, eligible, parked and blocked assignments with reason, priority, head, lease and responsible agent.
- Current-control decision scope: The parent can interrupt or unblock a chosen commitment while keeping the rest of the project queue active.
- Evidence: [whole queue state](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/commands/06-status.md#L3-L20), [live stop semantics](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L261-L273), [operator response and retry](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/configuration/09-stop-labels.md#L44-L71).
- Basis: structural
- Confidence: medium
- Caveats: The scope is the current repository workflow. Per-item task choices and fixed queue order do not establish autonomous whole-queue discretion.

## S3* — Complementary audit

- State: A
- Function: Independently challenge a candidate's claim to satisfy issue acceptance and supply the feedback that regulates revision or integration.
- Disturbance / variety regulated: Implementation claims and summaries can miss a criterion, conceal a regression or refer to an old PR head.
- Decisive decision or feedback right: Choose which checks and artifacts are sufficient, then render findings and a changes-requested or approved outcome.
- Decision owner: Bundled reviewer role in the independently configured runtime mode.
- Supporting / enforcement mechanisms: Head provenance, separate role/worktree, runtime eligibility, review records and outcome transitions.
- Closure path: Findings send the candidate back to the implementer or release the verified head for integration. Renewed heads are rechecked.
- Why this is / is not agent-owned: The reviewer performs discretionary judgment from the exact code, diff and candidate test evidence.
- Boundary reachability: Init provides a supported separate reviewer runtime configuration backed by candidate/head provenance.
- Claim being audited: The proposed head meets the issue criteria and has adequate check evidence.
- Ordinary reporting path: Implementer handoff, PR summary and automated check status.
- Complementary access path: Reviewer opens source and exact candidate diff, consults candidate-specific check evidence and may run reachable check steps.
- Independence boundary: A separate non-writing reviewer can require a CLI and model different from the known candidate producer.
- Who acts on findings: A later implementer repairs the current candidate, or the integrator handles a head released by review.
- Evidence: [shipped reviewer checks and report](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/templates/reviewer.md#L1-L44), [origin-runtime and head binding](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L621-L657), [findings enter later runs](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/docs/coordination.md#L138-L155), [feedback and correction](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/how-the-loop-works.md#L40-L50).
- Basis: structural
- Confidence: medium
- Caveats: Require the first-party supported independent reviewer mode for the stronger witness. The source records configured runtime identity, which is distinct from model weight independence.

## S4 — Outside-and-then intelligence

- State: P
- Function: Plan a controlled change of the launcher fleet when an external release would alter compatibility and coordination.
- Disturbance / variety regulated: Upcoming launcher builds can change coordination record formats or introduce configuration older launchers reject.
- Decisive decision or feedback right: Decide to defer or execute a coordinated rollout, and choose which current commitments to park before restarting the upgraded fleet.
- Decision owner: Project launcher operator responsible for all deployed launchers.
- Supporting / enforcement mechanisms: Release-range checks, terminal upgrade/skip banner, drain and graceful stop, known install procedure and restart.
- Closure path: The operator's rollout decision is applied to the fleet version and restart plan, changing later queue and lease behavior. The automatic route refuses an unsafe independent replacement.
- Why this is / is not agent-owned: Metadata and version predicates control the automatic path. Timing, coordinated adoption and treatment of affected commitments belong to the operator.
- Boundary reachability: Continuous launcher checks and reports incompatible release ranges, and the shipped operator workflow defines coordinated stop, upgrade and restart.
- External distinction: Published distribution and release markers distinguish independent upgrades from coordination-format or configuration-breaking releases.
- Future / prospective distinction: Current fleet runs an older format. A mixed-version fleet could lose shared live claim and retry semantics.
- Adaptation option generated: Offer independent rollout where the release range allows it, or require coordinated drain/restart, leaving the current fleet running if the parent defers.
- Path back into current capability / S3: The parent sequences the rollout and parks affected work, then the new launcher version resumes queue/lease control for future assignments.
- Evidence: [release alternatives and fleet return](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/upgrading.md#L1-L37), [supported v4 transition](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/site/content/upgrading.md#L39-L56), [bound release scan and automatic skip](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/updates/self_updates.py#L147-L182), [release compatibility before upgrade](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/updates/self_updates.py#L206-L244).
- Basis: structural
- Confidence: medium
- Caveats: This positive parent path is specifically for launcher fleet compatibility. A periodic upgrade of an already-approved compatible component does not establish autonomous S4.

## S5 — Policy and identity

- State: P
- Function: Set which classes of changes the entire project's agent workflow may integrate and which authorities retain ultimate disposition.
- Disturbance / variety regulated: The starter policy may conflict with a repository's reserved change classes, release rules or designated legitimate maintainers.
- Decisive decision or feedback right: Approve or decline the proposed durable workflow-policy revision and set the resulting division of responsibility.
- Decision owner: Project maintainers who approve the shared workflow policy into their default branch.
- Supporting / enforcement mechanisms: Init's policy tailoring issue, generated shared policy, maintainer-only merge rule and runtime reload.
- Closure path: The proposed policy is routed to maintainers. Merged policy is refreshed and read before later assignment runs, affecting which changes agents may integrate and which must return to parent.
- Why this is / is not agent-owned: Agent authors can propose a repository-specific boundary. The maintainer decides policy, and each subsequent role is bound to the accepted version.
- Boundary reachability: The installer offers the first policy-tailoring issue and the launcher refreshes the selected shared policy at runtime.
- Identity / ultimate-policy issue: Choose which categories of change this installed workflow can integrate autonomously under the project mandate and which require legitimate parent authority.
- Ultimate authority in each claimed mode: The maintainers decide which continuing policy to merge or retain.
- Return-to-operation path: The next role startup reloads merged instructions and uses the policy to merge only authorized change classes or send them to the named maintainer.
- Evidence: [shipped policy-tailoring intake](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/init/tailoring.py#L1-L11), [tailoring and reserved policy merge](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/templates/tailor-policy.md#L1-L25), [continuing merge and human decision policy](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/templates/ub_agents.md#L10-L39), [reload returned policy](https://github.com/uberblick-ai/ub-agents/blob/883bc1e4a241a573facaeb025489be59e7cb3428/src/ub_agents/loop.py#L745-L778).
- Basis: structural
- Confidence: medium
- Caveats: The witness is approval and runtime return of a policy revision affecting all future role runs. Routine approval of a particular PR is a lower-level decision.

## Distributed OSS parent arrangement

The maintainers of a deployed project are the parent for its own workflow. This assessment does not use company operations or the ub-agents publisher as evidence for the deployment's decision rights.

## Self-hosted and non-human modes

Self-hosted single- and multi-launcher installations share GitHub claim state. Operators retain current-control, coordinated upgrade and durable mandate decisions in the supported paths.

## Recursion

An issue assignment and its handoff PR can carry durable state through a sequence of roles. No separate viable metasystem is inferred from each child issue or launcher process.

## Variety and escalation

Trusted input, leases, limits and exact-head checks attenuate operating variety. Review corrections and action-needed notices return relevant evidence to subsequent roles or repository maintainers.

## Evidence gaps

Assessment is based on pinned primary source, including shipped roles and documented code wiring. No provider, coordinated upgrade or live GitHub workflow was run as part of the assessment.
