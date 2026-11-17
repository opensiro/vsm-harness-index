---
harness_id: agensh
project_name: Agensh
repository: https://github.com/microsoft/Agensh
review_ref: 2dae4e14a653da48549fd9aa093f834841475d6c
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agensh

## Review boundary

- System in focus: One Agensh multi-worker software-project campaign, from goal intake and worker startup through shared work coordination, integration and delivery.
- Purpose and identity: Coordinate a team of coding agents to develop a project against one goal and acceptance contract, then deliver the integrated branch.
- Environment: A supplied goal, target code and upstream branch, concurrent worker changes, acceptance results, tool outputs, provider budgets and optional owner input.
- Standard-distribution boundary: The shipped software-project pack, team driver, collaboration and lifecycle prompts, worker adapters, shared board and event router. Native agent engines, language models, Git hosting and chat services provide execution or transport.
- Credited operating / distribution surfaces: Rendered worker guidance and work cycle, Compose team and ACP bridge, expiring board claims and direct messages, backlog synchronization, integration gates, owner digest and campaign finalization.
- Adjacent first-party surfaces excluded from ownership: Benchmark packs and standalone baseline, post-run scoring and export consumption, repository development CI, research replay and upstream maintainer governance. The final evaluator is a delivery measurement, after the workers stop.
- First-party operating / deployment modes considered: Decentralized software-project team, optional named product owner, fixed-length campaign and pause/resume. A single-worker launch is supported but has no intra-team S2 witness.
- Recursion level: One project team. Workers own distinct deliverables within it. Multiple campaigns, upstream maintainers and host providers are outside this team's boundary.
- Reviewed revision: `2dae4e14a653da48549fd9aa093f834841475d6c` (frozen original default branch).
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The software-project pack supplies prepare, sync, export and final acceptance hooks. The driver imports a seed, applies integration controls, opens a root goal issue and wakes parallel workers. The worker entrypoint renders the Agensh collaboration protocol into the selected native agent's working context and runs it over ACP. Gitea records issues and changes. Mattermost and the board carry peer decisions, commitment claims and observations. The driver aggregates campaign health without assigning every work item. [Software-project pack](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/pack.toml#L29-L48) · [Team startup](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L428-L464) · [Worker entrypoint](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agent/entrypoint.sh#L64-L107) · [Mid-turn delivery](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/board-service/main.py#L341-L400)

## Operational model

Individual worker agents take responsibility for slices of the goal. They choose work, use tools, make and test changes, handle integration feedback and record the result. The same peers adjust their commitments when they interfere. At the team recursion an ordinary autonomous run lets the workers decide when the whole campaign is ready to deliver. A supported owner mode transfers the acceptance decision to the named person while workers retain their local coding choices. [Worker work cycle](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/templates/work_cycle.txt#L1-L15) · [Peer case handling](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/prompts/agents.txt#L48-L71) · [Campaign decision path](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L992-L1047)

## S1 — Operations

- State: A
- Function: Deliver tested changes to the integrated project branch from a goal and backlog.
- Disturbance / variety regulated: Ambiguous work items, tool responses, failed checks, changing branch state and integration conflicts.
- Decisive decision or feedback right: Choose the next local change, implementation, tool calls and revisions following acceptance or merge feedback.
- Decision owner: Each configured model-backed worker agent for its assigned or claimed deliverable.
- Supporting / enforcement mechanisms: Agensh prompts, provider adapters, Gitea branch and PR machinery, model/tool feedback and branch gates.
- Closure path: The worker runs checks, repairs failed changes or merges the updated main branch into its work, integrates accepted work into the team's main branch and publishes its result before taking another issue.
- Boundary reachability: The standard software-project pack generates the work-cycle prompt and the entrypoint applies it to the actual native worker session. Agensh starts workers with the goal through the team driver.
- Why this is / is not agent-owned: The configured agent exercises implementation and recovery discretion. Provider and CI services supply execution and constraints.
- Evidence: [Work-cycle steps](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/templates/work_cycle.txt#L1-L15) · [Prompt construction](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/hooks/prepare.py#L140-L181) · [Provider setup and dispatch](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agent/entrypoint.sh#L64-L107)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Model behavior and provider availability were not tested in a live deployment.

## S2 — Coordination

- State: A
- Function: Attenuate duplicate work and overlapping edits among concurrently operating workers.
- Disturbance / variety regulated: Two agents claiming the same deliverable or discovering that their intended edits overlap while both have active workspaces.
- Decisive decision or feedback right: Choose a different active issue or negotiate which peer continues and which work is redirected when claims or edits collide.
- Decision owner: The affected peer agents.
- Supporting / enforcement mechanisms: Typed expiring claims, Gitea assignee synchronization, mid-turn peer notices and direct messages.
- Closure path: Workers read claims before picking work, see another peer's live claim mid-turn, resolve the collision by direct message and then continue with adjusted task choices.
- Boundary reachability: Worker prompts already name the collision cases and prescribe the coordination relation. The team board and notice path are part of the supported launch.
- Why this is / is not agent-owned: The driver can mirror multiple simultaneous claims into the assignee list. The workers supply the discretionary conflict resolution.
- Distinct S1 units: Two or more separately executing worker agents with independent issues, branches and deliverables.
- Inter-S1 disturbance: Both peers may spend work on the same issue or edit the same area against the same integration branch.
- Attenuating coordination relation: Publish an expiring issue-specific claim before coding and negotiate via a direct message on observing an overlap.
- Feedback into subsequent S1 behaviour: A peer picks another unclaimed item or changes its current edit after the live notice and negotiation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The shipped work cycle and live prompt explicitly attach behavioral adjustments to concrete competing work and conflicting edits.
- Evidence: [Specific coordination use cases](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/prompts/agents.txt#L7-L42) · [Mid-turn collision instructions](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/prompts/agents.txt#L48-L71) · [Assignee and expiry rules](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/backlog.py#L1-L47) · [Notice delivery](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/board-service/main.py#L341-L400) · [Claim-before-coding protocol](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/templates/work_cycle.txt#L1-L15)
- Basis: explicit and structural.
- Confidence: high.
- Caveats: Claims are advisory and can coexist. A team of one does not exercise this witness.

## S3 — Inside-and-now control

- State: A(P)
- Function: Decide whether the whole team should keep spending its current commitment or finalize integrated delivery, with a supervised alternative.
- Disturbance / variety regulated: Team-wide tradeoff among ready deliverables, outstanding work, branch health and remaining run resources.
- Decisive decision or feedback right: Decide whether to continue the campaign or terminate the team work window and deliver the integrated result. The named owner additionally decides whether protected changes are permitted under the owner mode.
- Decision owner: Distributed worker team with an authorized worker close in the autonomous non-fixed-length mode. Named product owner for goal acceptance in the separately selected owner mode.
- Supporting / enforcement mechanisms: Root goal issue, board and branch evidence, product-owner digest, guarded root-issue closure and finalization driver. Timers, token limits and main-health status apply preset constraints.
- Closure path: A qualifying root-issue close is consumed by the driver. It ends team activity, initiates wrap-up, synchronizes and exports main, and stops the campaign. In owner mode worker closes are reopened and the authorized owner's close is required for this decision path.
- Boundary reachability: The standard project pack enables `issue_closed`. With no named owner and fixed-length disabled the driver's close path is reachable from the workers. Selecting the shipped named-owner mode supplies the digest, injected communications and owner-only acceptance.
- Why this is / is not agent-owned: The autonomous mode delegates the go/continue judgment to the team. The driver only validates mode-specific authority and implements the consequence. The supervised mode reserves the same approval for the owner.
- Whole-system current view: Workers can inspect the root issue, open work, shared board and integrated branch. The owner receives a campaign digest with merges, outstanding issues and PRs, full-suite status, board activity and token use.
- Current-control decision scope: Release or retain active campaign commitments across all workers and the shared work window. The observation supports this bounded control right, without establishing dynamic autonomous reallocations across campaigns.
- Evidence: [Supported team and owner closure modes](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/README.md#L82-L140) · [Worker view of issues, board and main](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/prompts/idle.txt#L1) · [Owner progress digest](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L493-L539) · [Identity check and stop decision](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L992-L1047) · [Delivery and stop](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L1049-L1104) · [Owner and fixed-length rejection smoke-test source](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tests/smoke/run_smoke.sh#L515-L534)
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: Workers have access to the whole campaign state. The runtime does not require a consensus vote, a coverage attestation or a specific readiness rubric before it accepts a worker close. Fixed-length mode disables this discretionary stop path.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Worker team through the closing worker | Team judges the root goal complete before the time limit in an autonomous non-fixed-length run | Root issue closes, driver stops active commitments, finishes integration and exports the result | [Mode description](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/README.md#L82-L140) · [Root-issue watcher](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L992-L1047) · [Finalization](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L1049-L1104) |
| Parent (`P`) | Configured product owner | Owner reviews the goal and current delivery state via team reports and board/branch access | Only that owner's root-issue close is accepted for discretionary finalization of the team's work | [Owner mode](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/README.md#L206-L218) · [Current view](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L493-L539) · [Owner guard](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L992-L1047) |

## S3* — Complementary audit

- State: —
- Function: Independent alternative access to team operational reality and corrective findings returned to current control.
- Disturbance / variety regulated: A worker report, patch summary or ordinary acceptance signal could misrepresent actual work.
- Decisive decision or feedback right: No separately constituted auditor judgment and return path established in the assessed mode.
- Decision owner: None evidenced for complementary audit. Peer reviewers and named owners participate in the regular integration route.
- Supporting / enforcement mechanisms: Board verifier, selected-path peer review, protected-path owner approval, main suite and final acceptance.
- Closure path: Integration results affect normal merge status. Final acceptance measures delivered main after the team stops.
- Why this is / is not agent-owned: Board admission checks the format and placeholder text. It does not obtain independent underlying evidence. Review distinctness supports routine gating without creating a complementary operational audit role.
- Evidence: [Board verifier implementation](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/board-service/verifier.py#L1-L56) · [Mandatory path review and health gate](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/quality.py#L115-L183) · [Normal review instructions](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/hooks/prepare.py#L140-L181) · [Final evaluation order](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/team_run.py#L1049-L1104)
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: A reviewer can choose to inspect an artifact closely. The distribution does not wire a separate sampling or escalation route on that basis.

### Absence scope

- Surfaces inspected: Board gists and verifier, peer and owner PR procedures, health feedback and final evaluation lifecycle.
- Plausible first-party paths checked: Independent re-execution of reported checks, exceptional artifact sampling by a separate reviewer and acceptance failures routed back to a live S3 actor.
- Why no material first-party path remains: Board validation is textual, CI and approval are standard integration steps, and final acceptance is performed after the workers stop.

## S4 — Outside-and-then intelligence

- State: —
- Function: Model prospective external change and feed a tested adaptation option into current team capability or governance.
- Disturbance / variety regulated: Target upstream can change and lessons can invalidate current assumptions.
- Decisive decision or feedback right: No reachable judgment path established for prospective external scenarios and a returned adaptation decision.
- Decision owner: No S4 actor evidenced. Workers own task choices and current compatibility fixes. An operator can configure a later run.
- Supporting / enforcement mechanisms: Upstream sync, conflict issues, durable shared lessons, planning prompt and pause/resume.
- Closure path: Sync imports an observed upstream head or assigns a reactive merge conflict. Shared notes and planning change current implementation choices under the supplied goal.
- Why this is / is not agent-owned: The team adapts its immediate work to new evidence. The reviewed paths yield neither prospective alternatives for its operating capability nor an authority loop that adopts one.
- Evidence: [Observed upstream sync](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/hooks/sync.py#L41-L88) · [Shared lessons](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/prompts/agents.txt#L7-L42) · [Goal decomposition](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/prompts/planning.txt#L1-L3) · [Run continuation](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/README.md#L93-L108)
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: A user could supply a dedicated foresight project or custom pack. This review covers the supplied project-team modes.

### Absence scope

- Surfaces inspected: Sync hook and timing, board reuse, optional planning, task brief construction and resumed project operation.
- Plausible first-party paths checked: External upstream intelligence, prospective use of recorded lessons, scouting for future model or tool shifts followed by a team capability commitment.
- Why no material first-party path remains: Sync and planning are bounded to current project delivery, and retained notes go back to the same goal. A changed operator profile has no supplied prospective choice-and-feedback loop.

## S5 — Policy and identity

- State: —
- Function: Close an identity or ultimate-policy matter at the team recursion and return the authoritative ruling into subsequent operation.
- Disturbance / variety regulated: Ambiguous requirements, changes to protected files and possible conflicts between the supplied goal and operational constraints.
- Decisive decision or feedback right: Runtime owner may clarify the goal, approve a protected PR or decide delivery. No supplied path turns a campaign identity or ultimate-policy question into active policy replacement with a returned decision.
- Decision owner: The operator supplies starting purpose and constraints. The product owner owns the evidenced project supervision and goal-acceptance choices.
- Supporting / enforcement mechanisms: Profile and policy configuration, rendered prompts, Gitea restrictions, urgent owner communications and branch approvals.
- Closure path: Clarifications return to workers and normal owner decisions change what may merge or when the run ends. The active campaign loads its governing inputs from the project configuration and prepared run prompts.
- Why this is / is not agent-owned: Neither deploying a new profile nor accepting ordinary delivery is an evidenced ultimate-policy deliberation inside this system.
- Evidence: [Goal and approval wiring](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/hooks/prepare.py#L140-L181) · [Owner flow](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/README.md#L206-L218) · [Shipped run and protection policy](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/tasks/software-project/pack.toml#L29-L48) · [Operator lifecycle commands](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/project.py#L427-L470)
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: A protected PR can touch project configuration, and later operators can use revised inputs. The shipped runtime does not wire acceptance of such a PR to an ultimate-policy decision returned to the active team.

### Absence scope

- Surfaces inspected: Project configuration and prompts, protected-file route, product-owner communications and driver lifecycle.
- Plausible first-party paths checked: Owner response to an ambiguous goal, changing the governing project file through the owner, and worker or owner choice to terminate.
- Why no material first-party path remains: These routes close requirements, integration exceptions or current resource commitments. No distinct identity-level escalation, adjudication and reapplication path is provided at the assessed recursion.

## Distributed OSS parent arrangement

The source repository's maintainers govern Agensh development outside the team. The optional named product owner has a distinct current-control role for a specific managed project deployment. An upstream delivery PR review belongs to the target project and does not transfer control of the assessed team to its maintainers.

## Self-hosted and non-human modes

The project pack supports teams with no in-run product owner plus the selectable named-owner mode. Native-model providers remain execution dependencies in both configurations. Pause and resume expose operator control over a campaign segment independently of inside-team issue acceptance.

## Recursion

Worker cells have local goals and separate execution context. The assessed team integrates their contributions against one root goal. Hosting multiple campaigns or contributing to Agensh itself is outside the stated recursion.

## Variety and escalation

Peers use short claims and direct messages to damp work collisions. A failing integration branch first alerts the responsible worker, escalates to the team and blocks ordinary merges for a bounded interval. Time and token pressure trigger wrap-up or pause. The named owner receives requirements questions and protected integration decisions in the supervised mode. [Health escalation](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/quality.py#L115-L183) · [Lifecycle and owner modes](https://github.com/microsoft/Agensh/blob/2dae4e14a653da48549fd9aa093f834841475d6c/agensh/README.md#L82-L140)

## Evidence gaps

- Source-first assessment only. No live worker session, provider use, benchmark replay or deployment was performed.
- Directly observed agent judgments on a real whole-goal close would strengthen the S3 base evidence. The shipped authority and state-transition code support the conditional operation described above.
- Bounds are specific to the supplied software-project pack. Custom task packs and alternate operating boundaries require their own evidence.
