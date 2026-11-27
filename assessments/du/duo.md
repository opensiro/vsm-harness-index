---
harness_id: duo
project_name: Duo
repository: https://github.com/kkkarthik6/duo-agents-harness
review_ref: ab366d9ed0dfd327b9ed536e234ff2ce219351a4
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Duo

## Review boundary

- System in focus: A configured Duo installation, assessing one full project run for internal control and the local installation for cross-run coordination and updates.
- Purpose and identity: Deliver project work through provider CLI roles and evidence-based review.
- Relevant environment: A local project, installed and signed-in coding CLI, local engine and operator UI.
- Standard-distribution boundary: Duo engine, role profiles, prompt and worker launch, local workspace/review state, run controls and optional local feature/core update workflow.
- Credited operating / distribution surfaces: Quick and full role workflows, isolated review, current-run steering, overlapping workspace admission and supported self-improvement.
- Adjacent first-party surfaces excluded from ownership: Native CLI internals, upstream provider governance, contributor repository CI and unrelated application release decisions.
- First-party operating / deployment modes considered: Quick build, full staged builds, goal-loop review, supervised operation and owner-approved local core changes.
- Recursion level: Project runs are operational units in a local installation. Within a full run, assess the lead, build and review roles and the commitments they regulate.
- Reviewed revision: ab366d9ed0dfd327b9ed536e234ff2ce219351a4
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Duo assigns provider CLI sessions to roles, issues work with persisted turn briefs, and can maintain multiple local project runs. The local engine tracks active workspaces, package readiness, review artifacts and goals. It constructs code review artifacts from changes against a stored baseline and imports reviewer output from a separate workspace. Local improvement proposals use an isolated checkout and an explicit apply step.

## Operational model

The builder decides how to implement the project task and produces files and evidence. The engine makes role routing and routine workflow transitions from state. Goal and review actors own judgments from their own contexts. The operator can add run constraints or change the live budget when the engine returns a decision to them.

## S1 — Operations

- State: A
- Function: Deliver requested project changes and check evidence.
- Disturbance / variety regulated: Changing codebase, evidence and execution results.
- Decisive decision or feedback right: Select workspace actions and decide the resulting work artifact or report.
- Decision owner: The configured builder CLI agent running Duo-issued tasks.
- Supporting / enforcement mechanisms: Role assignment, workspace, handoff storage, tasks and receipt checks.
- Closure path: The builder acts on the workspace, reports outputs and checks, and receives review findings for subsequent revision.
- Boundary reachability: The installed full and quick workflow ships the builder role, prompt, launch and returned artifact path. The external CLI supplies the configured executor.
- Why this is / is not agent-owned: Without the builder the pipeline still routes requests but cannot choose or perform project changes.
- Evidence: [README.md](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/README.md#L35-L71), [engine/handoff.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/handoff.py#L108-L129), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L1635-L1659)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The native CLIs and credentials are dependencies, and their internal autonomy is not independently rated here.

## S2 — Coordination

- State: C
- Function: Attenuate independent project agents' contention over overlapping working trees.
- Disturbance / variety regulated: Two active runs or a remaining background job can work over the same tree.
- Decisive decision or feedback right: Choose response to a competing workspace commitment.
- Decision owner: The local run pool implements an overlap-specific admission relation. An autonomous coordination owner must be composed.
- Supporting / enforcement mechanisms: Saved-run and live-actor registry, overlap checks and active-run constraints.
- Closure path: A conflicting start is refused until the conflicting work is stopped or complete, or until a disjoint workspace is used.
- Boundary reachability: The shipped engine applies the workspace check to ordinary local project run operations.
- Why this is / is not agent-owned: The project agents may act independently on their tasks. The admission disposition comes from fixed policy and caller construction of the schedule.
- Distinct S1 units: Separately launched Duo project runs with autonomous builders.
- Inter-S1 disturbance: Concurrent runs or leftover background jobs may write an overlapping workspace.
- Attenuating coordination relation: The supplied admission check finds path overlap against live and saved background work before allowing a start.
- Feedback into subsequent S1 behaviour: An attempt is held out of the overlapping workspace until the conflicting commitment ends or a disjoint workspace is selected.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Admission uses actual path overlap and reservations to prevent cross-run write interference.
- Evidence: [README.md](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/README.md#L73-L90), [engine/run_pool.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/run_pool.py#L85-L117), [engine/server.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/server.py#L744-L752)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The serialized response applies to a local Duo process and its observed jobs.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate whole-run commitments when goal evidence is inadequate or the run reaches a decision point.
- Disturbance / variety regulated: Reported completion can leave outstanding obligations or time constraints.
- Decisive decision or feedback right: Decide whether remaining whole-run work should be reassessed, resumed, revised or stopped.
- Decision owner: Goal critic in the automated goal-loop mode. The local operator owns the distinct supervised plan and budget decision.
- Supporting / enforcement mechanisms: Goal-report parser, run state, pause function, updated round limits and dispatch.
- Closure path: Goal judgment triggers reassessment, a revise turn, a blocker decision or closure. In supervised mode the run pauses for the owner and returns to execution under the changed plan constraints or budget.
- Boundary reachability: The local engine supplies both goal-loop evaluation and owner-facing decisions in the same shipped run controls.
- Why this is / is not agent-owned: The model critic decides whether the overall goal is met. In the distinct supervised path the engine acts on the operator's returned current decision.
- Whole-system current view: Run state contains the overall goal, active phase, documented results, saved checks, worker roles and round budget.
- Current-control decision scope: Whether current commitments remain open and how to restart, constrain or fund the active workflow.
- Evidence: [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L1717-L1727), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2090-L2128), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2415-L2426), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2449-L2475), [engine/server.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/server.py#L568-L576)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Deterministic work-package eligibility or stalled-loop detection alone provides no autonomous ownership.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Goal critic | Current-run goal check after role work | Structured goal judgment triggers reassessment, revision or closure. | [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2090-L2128) |
| Parent (`P`) | Run owner | Supervised plan decision or exhausted goal-work budget | Owner adjusts constraints or budget and resumes the current commitment. | [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L1717-L1727), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2113-L2125), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2415-L2426) |

## S3* — Complementary audit

- State: A
- Function: Audit a builder's completion and quality claims against the underlying changes.
- Disturbance / variety regulated: A build reply and its reported checks can omit defects or unfinished work.
- Decisive decision or feedback right: Render an independent code verdict and specify the required repairs.
- Decision owner: The fresh critic agent in the full/selected quick-review path.
- Supporting / enforcement mechanisms: Baseline snapshot, generated diff, separate review workspace, alternate provider preference and verdict parser.
- Closure path: The critic reads a patch and workspace evidence, returns approval or required corrections, and a revision cycle consumes the findings.
- Boundary reachability: Duo's full role workflow installs the review route and collects the isolated review outputs. The reviewed source provides this mode with one or multiple vendor CLIs.
- Why this is / is not agent-owned: The critic selects defects and disposition. The engine copies evidence and enforces transitions.
- Claim being audited: Builder reports that the implementation and its checks satisfy the task.
- Ordinary reporting path: Build replies, receipts and generated handoff briefs.
- Complementary access path: Workspace evidence and a diff against the runtime's recorded baseline.
- Independence boundary: A fresh review session and scoped review copy reduce dependence on builder's preceding context. A distinct provider is preferred where available.
- Who acts on findings: The runtime uses the verdict and defects to schedule subsequent builder revision or proceed.
- Evidence: [README.md](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/README.md#L53-L76), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L1198-L1225), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L1729-L1739), [engine/phases.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/phases.py#L107-L184), [engine/roleflow.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/roleflow.py#L57-L100)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Independence is relative to the builder's output and session. Different vendors are optional.

## S4 — Outside-and-then intelligence

- State: P
- Function: Use evidence of operator needs to change the local harness's future capabilities.
- Disturbance / variety regulated: User requests or gaps in previous behavior motivate a method or product change.
- Decisive decision or feedback right: Select whether a tested local capability proposal becomes the active core.
- Decision owner: Local installation owner for reviewed core proposals.
- Supporting / enforcement mechanisms: Queued proposal worktree, agent implementation, test and review checks, and apply/tag mechanics.
- Closure path: A proposal launches an isolated improvement run. On approval the tested change is integrated locally and loaded on the next launch.
- Boundary reachability: The optional proposal route and self-improvement worker are present in the engine and UI server.
- Why this is / is not agent-owned: Agents implement and evaluate proposed changes. The core-approval action supplies the decisive return into future operation.
- External distinction: The operator brings demand from using Duo on projects.
- Future / prospective distinction: The improvement changes behavior of subsequent work rather than repairing the present project artifact.
- Adaptation option generated: A concrete tested code proposal in a separate worktree.
- Path back into current capability / S3: Owner approval cherry-picks the proposal and tags the change, loaded on next launch.
- Evidence: [engine/server.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/server.py#L578-L597), [engine/selfdev.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/selfdev.py#L107-L123), [engine/selfdev.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/selfdev.py#L172-L194)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The assessed parent path is the core proposal workflow. Ordinary model discovery and a feature feedback report alone do not establish adaptation.

## S5 — Policy and identity

- State: —
- Function: Ultimate identity governance was sought for a local installation.
- Disturbance / variety regulated: Potential conflicts over purpose or ultimate policy.
- Decisive decision or feedback right: No identity-level issue-return path established.
- Decision owner: The owner sets practical local rules and accepts code changes.
- Supporting / enforcement mechanisms: Settings, per-run constraints, versioned core and local proposal approval.
- Closure path: Configuration changes apply to project work or later launches.
- Why this is / is not agent-owned: The supplied decisions regulate project constraints and reviewed updates. No first-party identity dispute reaches a standing ultimate authority and returns as an authoritative policy decision.
- Evidence: [README.md](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/README.md#L103-L129), [engine/session.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/session.py#L2415-L2426), [engine/server.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/server.py#L578-L597), [engine/selfdev.py](https://github.com/kkkarthik6/duo-agents-harness/blob/ab366d9ed0dfd327b9ed536e234ff2ce219351a4/engine/selfdev.py#L107-L123)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: A code proposal could change a policy mechanically.

### Absence scope

- Surfaces inspected: Settings, role mapping, operator approvals, local core proposals and update controls.
- Plausible first-party paths checked: A routed dispute about purpose or identity, authorized resolution and a binding return to later operations.
- Why no material first-party path remains: Task steering and local code updates close operating and adaptation decisions. The supplied workflow offers no distinct ultimate-policy adjudication.

## Recursion

Duo's installation hosts several project runs. The audit and goal dispositions apply within a full run. The adaptation path applies to the local installation, and corporate provider policies remain outside this boundary.

## Variety and escalation

Role selection, package readiness and review returns regulate process variation. Agent availability, budget stops and blockers are translated into run transitions or questions for the owner.

## Evidence gaps

Static source analysis. No provider sessions or local modification were executed. Conditional branch reachability was traced in the distribution. Relative audit independence depends on the actual scope of a review context.
