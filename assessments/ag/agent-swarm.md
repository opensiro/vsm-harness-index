---
harness_id: agent-swarm
project_name: Agent Swarm
repository: https://github.com/desplega-ai/agent-swarm
review_ref: 65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# Agent Swarm

## Review boundary

- System in focus: A self-hosted multi-agent work organization: one lead routes and controls persistent operational workers over the shared task service. Recursion is this deployed team, not one provider's internal tool loop or the upstream OSS institution.
- Credited operating / distribution surfaces: The official lead/coder/reviewer templates and docker-compose.example.yml, task API/runner/provider adapters, heartbeat, sibling awareness, review feedback, and explicitly optional first-party schedule templates. The GTM template is credited only as a function-specific construction path for a team's own GTM campaign after operator configuration.
- Adjacent first-party surfaces excluded from ownership: Repository contributor .claude/AGENTS/thoughts/CI workflows, evaluation applications, upstream maintainers' governance and private dogfood installations. External Claude Code/Codex/pi/OpenCode/Devin/ACP internals are not inherited. Generic extension hooks, editable persona and memory do not establish higher functions.
- Deployment qualifications: MIT source; operator supplies provider access, configured repos/integrations and permissions. The example instantiates an official lead and eleven official workers including coder, researcher, reviewer and tester. Referenced Docker latest images and external providers are not immutable runtime attestations.
- Reviewed revision: `65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Bun/SQLite task service persists agents, tasks, schedules, repository guidelines and progress. Each worker runs in an isolated environment using a selected external AI harness; the runner assembles first-party role, identity, repo and task context and calls the provider adapter. The official lead is a model-driven supervisor, not merely the deterministic scheduler. [docker-compose.example.yml](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docker-compose.example.yml); [src/commands/runner.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/commands/runner.ts); [docs-site/content/docs/(documentation)/architecture/overview.mdx](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docs-site/content/docs/(documentation)/architecture/overview.mdx).

## Operational model

A request becomes a task; lead chooses assignment and dependencies, worker chooses operational actions and reports progress. Same-context in-flight tasks are injected as explicit coordination context. Failed tasks and periodic current-state checks create lead decisions; code work can be assigned to a separate reviewer with direct checkout access. Repository merge permissions and human review remain explicit operational constraints. An optional weekly GTM template senses outside demand and proposes next options, but does not itself close adoption. [templates/official/lead/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/CLAUDE.md); [src/tasks/sibling-awareness.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tasks/sibling-awareness.ts); [src/heartbeat/heartbeat.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/heartbeat/heartbeat.ts); [templates/official/reviewer/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/reviewer/CLAUDE.md).

## S1 — Operations

- State: A
- Function: Operational delivery by distinct coding/research/review workers.
- Disturbance / variety regulated: Open-ended implementation/research requests, uncertain tool results and task failures.
- Decisive decision or feedback right: Choose task-local investigation, tool actions, implementation and completion/progress response.
- Decision owner: The model-driven operational worker in the configured provider session.
- Supporting / enforcement mechanisms: Runner prompt assembly, provider adapters, MCP tools, task persistence and runtime limits transport/enforce worker decisions.
- Closure path: Task → assembled context → worker tool/action choices → progress/result → task and lead follow-up.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: Removing the model worker leaves scheduling/storage, not the same discretionary investigation or implementation.
- Evidence: [docker-compose.example.yml](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docker-compose.example.yml); [src/commands/runner.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/commands/runner.ts) (adapter.createSession and task handling); [templates/official/coder/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/coder/CLAUDE.md); [src/prompts/base-prompt.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/prompts/base-prompt.ts).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: Provider access is required; the assessment does not import unexamined provider governance or claim successful business output.

## S2 — Coordination

- State: A
- Function: Attenuate interference among concurrent S1 workers.
- Disturbance / variety regulated: New requests arrive through different ingresses while related work remains in flight, risking duplicate or contradictory implementation/review.
- Decisive decision or feedback right: Interpret sibling intent, coordinate with named workers, avoid duplicate action, and choose compatible task work.
- Decision owner: Lead and operational model workers own the coordination judgment; the sibling detector does not decide task semantics.
- Supporting / enforcement mechanisms: contextKey lookup, in-flight task status, original-intent rendering, messaging/task tools, same-agent parent-session selection and lead no-duplicate rules.
- Closure path: Same-context sibling discovery → task prompt lists owners/status/original requests and instructs coordinate/do not duplicate → agent queries/messages/reuses ongoing work → subsequent assignment/action changes.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: Sibling context intentionally exposes this inter-worker disturbance; the agent decides what overlaps and what should change.
- Evidence: [src/tasks/sibling-awareness.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tasks/sibling-awareness.ts); [src/tasks/sibling-block.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tasks/sibling-block.ts); [templates/official/lead/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/CLAUDE.md) rules 2, 7, 8; [src/tools/send-task.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/send-task.ts).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: Structural disturbance witness, not a claim that every collision is prevented. Incorrect/missing context keys can miss related work.
- Distinct S1 units: Separately assigned coder, researcher and reviewer workers in the official multi-worker deployment.
- Inter-S1 disturbance: Concurrent same-context tasks from multiple ingresses can duplicate or conflict with each other's unfinished work; same-PR reviews can be double-assigned.
- Attenuating coordination relation: Named sibling tasks and status are supplied to the new worker; explicit coordinate/do-not-duplicate instructions plus task inspection/messaging let it adjust alongside lead deduplication.
- Feedback into subsequent S1 behaviour: Coordination changes which work a new task performs and whether lead creates/routes another task; same-agent continuation can resume existing context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party renderer explicitly detects concurrent related work, describes its original intent and instructs interference attenuation. Generic mailboxes or dependsOn alone are not the witness.

## S3 — Inside-and-now control

- State: A
- Function: Control the team's inside-and-now commitments and recovery.
- Disturbance / variety regulated: Stalled sessions, failed workers, unclaimed recovery pins, affinity-starved tasks and abandoned commitments across the team.
- Decisive decision or feedback right: Assess current state and choose reroute, retry, cancel, recreate or intervention rather than blindly continue.
- Decision owner: The official lead agent owns discretionary current-control decisions.
- Supporting / enforcement mechanisms: Heartbeat preflight and code triage detect/escalate; snapshots, task creation, steer/cancel/send tools enforce the selected decision.
- Closure path: Whole-team status and standing orders → lead heartbeat/reroute-decision task or worker-failure follow-up → lead investigates and chooses corrective task/resource action → task service changes subsequent worker operation.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: Automatic retry thresholds and transactions expose exceptional state; lead must choose the organizational response after those mechanisms cannot settle it.
- Evidence: [src/heartbeat/heartbeat.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/heartbeat/heartbeat.ts); [src/heartbeat/templates.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/heartbeat/templates.ts); [templates/official/lead/HEARTBEAT.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/HEARTBEAT.md); [src/tasks/worker-follow-up.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tasks/worker-follow-up.ts); [src/tools/templates.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/templates.ts) task.worker.failed; [src/tools/steer-task.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/steer-task.ts); [templates/official/lead/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/CLAUDE.md).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: A parent can administer deployment, but isolated configuration or approval is not counted as a distinct evidenced parent S3 mode.
- Whole-system current view: Gathered agents, active/pending/failed tasks and stalled sessions, combined with lead standing orders and full task-detail access.
- Current-control decision scope: Team commitments and recovery: cancel obsolete work, reassign eligible workers, steer current execution, recreate still-needed failed work and avoid retry storms.

## S3* — Complementary audit

- State: A
- Function: Complementary audit of an operational code-delivery claim.
- Disturbance / variety regulated: A coder can report completion while code contains security/race/state-machine faults or inadequate evidence/tests.
- Decisive decision or feedback right: Form an independent review judgment with blocking findings/request-changes and return corrective requirements.
- Decision owner: A distinct official reviewer model session owns audit judgment; coder/lead own correction and subsequent work routing.
- Supporting / enforcement mechanisms: Separate worker environment/task, direct git checkout, GitHub review/CI access, task completion/follow-up and parentTaskId continuity.
- Closure path: Lead routes a review to reviewer → reviewer independently clones/checks out actual PR code and examines tests/CI → blocking findings/request changes → coder resolves feedback with parentTaskId continuity; lead can route corrective work. Human approval remains a separate merge requirement.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: The reviewer directly inspects operational evidence in a separate role/session and decides substantive findings, beyond the implementer's summary or deterministic CI verdict.
- Evidence: [docker-compose.example.yml](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docker-compose.example.yml); [templates/official/reviewer/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/reviewer/CLAUDE.md); [templates/official/lead/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/CLAUDE.md) routing/review rules; [templates/official/coder/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/coder/CLAUDE.md) review-feedback rule; [src/tasks/worker-follow-up.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tasks/worker-follow-up.ts); [src/tools/templates.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/templates.ts).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: This is a supported role-based audit path when lead assigns review, not proof every task is audited. The ordinary 500-character completion follow-up alone is not complementary audit; shared credentials/model family are not institutional independence.
- Claim being audited: Coder's proposed change is ready/correct and tests cover changed paths.
- Ordinary reporting path: Coder progress/completion and a summary follow-up task to lead.
- Complementary access path: Reviewer must clone repository and check out the PR branch, inspect actual code, tests and CI; not only read the coder's summary/diff.
- Independence boundary: Separate reviewer worker/session and instructions, distinct from the producing coder; official deployment includes the reviewer.
- Who acts on findings: Reviewer requests changes with concrete blocking fixes; coder resolves review feedback in the originating task context, with lead routing and subsequent review as needed.

## S4 — Outside-and-then intelligence

- State: C
- Function: Outside-and-then intelligence for the deployed team's own GTM campaign.
- Disturbance / variety regulated: Changing discovery channels, search demand and content opportunities make the team's existing GTM plan less effective.
- Decisive decision or feedback right: Turn external trend distinctions into candidate future campaign/content adaptations; adopter must still compose selection and implementation closure.
- Decision owner: The configured lead produces options; deployment owner must supply campaign goal, integrations and the decisive adoption/return-to-S3 relation.
- Supporting / enforcement mechanisms: First-party parameterized weekly schedule prompt, GitHub/GSC integrations, configured GTM plan/state, admin report and saved research workspace.
- Closure path: Configured own-campaign metrics → week-over-week search/referrer/content analysis → what-to-try-next and gap/opportunity options → report. Turning that report into an adopted current-capability change is intentionally not supplied as an automatic closed mode.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: A function-specific first-party prospective adaptation constructor exists, but no closed agent-owned or parent-owned adoption loop is established by the template.
- Evidence: [templates/schedules/gtm-weekly-review/config.json](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/schedules/gtm-weekly-review/config.json); [templates/schedules/gtm-weekly-review/content.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/schedules/gtm-weekly-review/content.md); [templates/official/discoverability-optimizer/SOUL.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/discoverability-optimizer/SOUL.md).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: Optional template; requires own GTM goal, REPO_URL/GSC_PROPERTY and integrations. Ordinary customer research as a delivered task, generic memory, persona edits and arbitrary extensions are not S4 witnesses.
- External distinction: Repository traffic/referrers/popular paths and Search Console queries, impressions, CTR and rankings for the deployment's configured campaign.
- Future / prospective distinction: Week-over-week change, high-impression low-CTR/rank opportunities, content gaps and what to try next against the current GTM plan.
- Adaptation option generated: Candidate SEO/content/campaign experiments to improve the team's own future reach.
- Path back into current capability / S3: Report through configured admin/in-app channels and saved research workspace intentionally exposes options to the deployment; actor authority and adoption/execution closure must be composed, so C rather than A/P.

## S5 — Policy and identity

- State: —
- Function: Identity and ultimate-policy adjudication at deployed-team recursion.
- Disturbance / variety regulated: A prospective conflict about the team's constitutive purpose or ultimate policy would require authoritative settlement.
- Decisive decision or feedback right: No function-specific decisive identity/ultimate-policy arbitration and return loop is supplied in the inspected deployed surfaces.
- Decision owner: No in-boundary S5 owner established; operator configuration and lead profile editing are not sufficient evidence.
- Supporting / enforcement mechanisms: SOUL/IDENTITY/CLAUDE persistence, update-profile, repo guidelines, permission/budget and extension activation controls.
- Closure path: Observed paths persist persona, operational checks and permissions; they do not reconstruct a disputed identity/ultimate-policy matter being authoritatively settled and governing future operation.
- Boundary reachability: The supported self-hosted composition runs official lead and worker templates through provider adapters; the cited task/prompt paths are shipped deployment surfaces, not this repository's contributor agents.
- Why this is / is not agent-owned: Neither writable identity files nor final human say on individual merges establishes the S5 function.
- Evidence: [docs-site/content/docs/(documentation)/architecture/agents.mdx](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docs-site/content/docs/(documentation)/architecture/agents.mdx); [src/tools/update-profile.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/update-profile.ts); [src/tools/repos/update-repo.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/tools/repos/update-repo.ts); [templates/official/lead/CLAUDE.md](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/templates/official/lead/CLAUDE.md); [src/prompts/base-prompt.ts](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/src/prompts/base-prompt.ts); [docs-site/content/docs/(documentation)/guides/extensions.mdx](https://github.com/desplega-ai/agent-swarm/blob/65e0ab6bb1f50f796b9c226e2bb34b5041cbaa66/docs-site/content/docs/(documentation)/guides/extensions.mdx).
- Basis: Pinned first-party source, supported deployment example and operational instructions; no live execution claim.
- Confidence: High for the bounded source path; no measured reliability claim.
- Caveats: Bounded absence in this deployed distribution, not an impossibility claim for a separately composed organization's governance.

### Absence scope

- Surfaces inspected: Official lead and worker identity/instructions, update-profile persistence and authorization, assembled repository policy, update-repo, extension activation and operator controls.
- Plausible first-party paths checked: Lead asks user to set missing repo guidelines (prChecks/mergeChecks/allowMerge/review) and persists them; human approval before merging; SOUL/IDENTITY self-edit and lead coaching; operator-only extension activation option.
- Why no material first-party path remains: These paths settle operational checks, permissions or persona text. The reviewed source does not expose an identity-level dispute/proposal, legitimate ultimate adjudication and return-to-operation relation. Upstream OSS maintainers and generic future governance plugins lie outside the deployed-team boundary.

## Distributed OSS parent arrangement

Upstream contribution/PR governance is outside this deployed-team recursion. The operator legitimately supplies access and repository operating constraints; no function is credited simply from that authority.

## Synthesis

A / A / A / A / C / — for S1 / S2 / S3 / S3* / S4 / S5. S4 is only an optional, specifically exposed GTM intelligence construction path; the default team is not claimed to close prospective adaptation automatically. No maturity score or weights are implied.

## Evidence gaps

No live provider session, deployment trace or efficacy/performance test was run. Source supports ownership topology; provider-specific behavior, production audit coverage and any custom adoption/governance closure remain deployment-dependent.

## Assessment provenance

Source reviewed at the exact frozen ref above. Generated under Profile 0.2.4 / Methodology 0.3.7, Index's active contract, using the immutable v0.3.7 structural checker. Skills main 0.3.8 was observed but does not silently change this generation contract. Batch #2471 row 5, source intake #2470.

## Review / admission status

Proposed source assessment for ordinary PR integration. Canonical inclusion, catalog allocation and derived outputs require a distinct subsequent admission transaction. No independent reviewer or autonomy grade is claimed.
