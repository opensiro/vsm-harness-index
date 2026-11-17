---
harness_id: nano-workforce
project_name: Nano Workforce
repository: https://github.com/nanobpm/nano-workforce
review_ref: db6e2f220d8d2a8512897df9cb279e79d6d5cd16
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Nano Workforce

## Review boundary

- System in focus: One installed Nano Workforce Urban app orchestrating a configured local/remote fleet of coding-agent workers across issues, PRs, epics and delivery graphs, not the entire Nano engine or the upstream development organization.
- Purpose and identity: A durable agentic SDLC control/application layer that decomposes work, coordinates independent coding workers, resolves review loops and merge dependencies, and asks the operator to adjudicate bounded exceptions.
- Relevant environment: GitHub repositories/issues/PRs/branch protections, configured coding-agent CLI workers, human project operator and reviewers, connected Nano engine, external code/CI tools and target repositories.
- Standard-distribution boundary: First-party Nano Workforce source, manifests, BPMN process definitions, linked agent-task prompts, app operations, record workers, polling, user-task controls and cockpit views. The separately installed Nano engine, Studio shell and hired coding-agent implementation are external execution dependencies, not borrowed VSM ownership.
- Credited operating / distribution surfaces: Runnable [nano.app.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/nano.app.json), [plan-fanout.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/plan-fanout.bpmn), [convergence-loop.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/convergence-loop.bpmn), [retro.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/retro.bpmn), [service.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/service.ts), [completeUserTask.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/completeUserTask.ts) and their included first-party task prompts/record workers under supported Nano Studio or CLI installation modes.
- Adjacent first-party surfaces excluded from ownership: This repository's development CI/tests, docs-only claims, release installer/update governance and example/demo recipes; their code may substantiate reachability but does not itself act as an assessed fleet agent. GitHub Copilot/Claude/Codex model providers and Nano engine internals are excluded as independent owners.
- First-party operating / deployment modes considered: Installed Studio extension; supported CLI app against Nano engine; configured external worker fleet; model-backed plan-review and conformance tasks; operator-entered escalation decisions; optional auto-retro and opt-in escalation steward; agent-authored staged delivery graphs requiring operator dispatch.
- Recursion level: One operator-governed workforce managing distinct task-performing agent units and multiple concurrent work items; the human operator and target repository's maintainer organization are adjacent higher authority, not automatically agent-owned S5.
- Reviewed revision: db6e2f220d8d2a8512897df9cb279e79d6d5cd16, original public main at discovery (immutable for this assessment).
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The first-party Urban app deploys BPMN orchestration for plan-fanout, implementation, review-convergence, merge, human escalation and post-epic retrospective. It persists plan/PR/review/escalation records via app data tables, exposes human user tasks through its cockpit and operations, and reconciles status against the actual engine and GitHub state. Agent jobs are emitted as typed tasks (such as senior:plan, senior:plan-review, senior:feature, senior:pr-review, senior:adversarial-review, senior:conformance, senior:retro) for an *externally hired* fleet. Prompts and the first-party task graph determine which jobs execute and what decisions their model-backed worker agents must make, but the agent CLI implementation is not part of this codebase. The default application supports human-only decisions at particular gates and optional steward auto-answers only for allowlisted reversible situations. Sources: [README.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/README.md), [nano.app.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/nano.app.json), [service.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/service.ts), [escalationSteward.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/escalationSteward.ts), [plan-fanout.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/plan-fanout.bpmn), [retro.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/retro.bpmn).

## Operational model

Work starts from an issue/graph assigned by an operator or via an authenticated integration. A planning worker emits task decomposition and prerequisites; the separate plan-review worker tests whether agents will collide on source surfaces; the app levelizes dependencies and gates subsequent work on merged predecessors. Independent external coding workers implement tasks. Review-round and separate adversarial reviewers operate on the actual PR diff and current review feedback. The first-party engine-facing record handlers persist review/merge evidence, loop boundedly or park human user tasks for an operator decision. The after-epic conformance agent audits code against spec rather than trusting executor reports. The prospective retrospective agent proposes human-reviewed repository improvements, whose later adoption is not proven at this source boundary.


## S1 — Operations
- State: A
- Function: Model-backed coding agents execute planned tasks, invoke tools, inspect GitHub context, revise PR changes and return durable results through task jobs.
- Disturbance / variety regulated: Unpredictable issue requirements, source context, compiler/test feedback, reviewer findings and merge failures.
- Decisive decision or feedback right: The dispatched task agent chooses actual implementation and code/test/review responses, not a hard-coded host script.
- Decision owner: Configured agent workers executing first-party senior:feature, senior:pr-review, senior:fix-ci and related model-backed job specifications; external CLI tooling supplies execution but first-party orchestration defines their actionable role.
- Supporting / enforcement mechanisms: BPMN execution order, worker registration, agent job/result protocol, durable PR state and round timers.
- Closure path: Agent produces code changes or review responses and returns task outcome; host persists PR status, feeds next reviewer findings into subsequent worker turns, and advances or escalates the task.
- Boundary reachability: The standard plan-fanout and implement-cell BPMN actually emit these named agent jobs with linked first-party prompts; installed workforce workers subscribe to the exposed job types.
- Why this is / is not agent-owned: Code choices are made in the actual worker's model loop; the first-party BPMN engine only sequences and enforces them. Attribution is to the agent role in this supplied installed operating mode, not to Nano engine itself.
- Evidence: [README.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/README.md), [implement-cell.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/implement-cell.bpmn), [convergence-loop.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/convergence-loop.bpmn), [feature.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/feature.md), [review-round.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/review-round.md)
- Basis: explicit first-party orchestration and prompts, structural source reachability
- Confidence: high for shipped agent job path; no live external-model integration execution
- Caveats: Needs separately hired compatible workers and credentials; this source-only review does not demonstrate actual model output quality.


## S2 — Coordination
- State: A
- Function: Prevent distinct implementation agents from corrupting shared source or starting before incompatible prerequisites have landed.
- Disturbance / variety regulated: Parallel agents may edit the same file, choose wrong branch bases, miss dependency edges, create dependency cycles or run against unfinished upstream changes.
- Decisive decision or feedback right: Independent plan-review agent judges hidden dependencies and overlapping edit surfaces, may reject the entire plan with concrete remedies; planner revises it before deployment. Hard DAG and merge-wave rules enforce safe release of subsequent agent work.
- Decision owner: Model-backed senior:plan-review worker for conflict-specific discretionary judgment; deterministic wave levelizer and merge barrier enforce its approved dependency graph.
- Supporting / enforcement mechanisms: Plan review result recorder, typed approved/findings return, computeWaves cycle/dangling-edge rejection and waveMergeTargets merged-PR barrier.
- Closure path: Plan-review rejection routes critique to planner's subsequent attempt; accepted graph is wave-levelized, dependent workers wait for predecessor PRs to merge before starting.
- Boundary reachability: The plan-fanout BPMN calls senior:plan-review and pr.record-plan-review before selecting and dispatching implementation waves, with first-party prompt explicitly demanding conflict review.
- Why this is / is not agent-owned: The S2-specific *inter-agent collision judgment* is supplied by a model-backed reviewer. The deterministic DAG gate is neither the author of that judgment nor generic messaging.
- Evidence: [plan-review.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/plan-review.md), [plan.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/plan.md), [plan-fanout.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/plan-fanout.bpmn), [waves.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/waves.ts), [worker.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/workers/record-plan-review/worker.ts)
- Basis: explicit adversarial plan prompt + active task graph wiring
- Confidence: medium-high
- Caveats: The S2=A result is confined to enabled model-backed plan-review mode; the deterministic wave gate alone does not create A without this actor.
- Distinct S1 units: At least two independently executing coding worker tasks in the same plan, each preparing a separate PR.
- Inter-S1 disturbance: Two parallel tasks can modify one code surface or require each other's merged code, causing merge collision and semantically inconsistent combined tree.
- Attenuating coordination relation: Plan reviewer assesses shared-surface interference and demands coarsening or scaffolding; compiler verifies DAG and postpones dependent waves until requisite PRs have actually merged.
- Feedback into subsequent S1 behaviour: Rejected graph gets rewritten before any task dispatch; merged predecessor branches and release barriers alter which worker executes when and against what base.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The credited witness is explicit inter-agent write/merge interference identified and attenuated before execution; scheduling alone would not establish it.


## S3 — Inside-and-now control
- State: P
- Function: Observe and intervene on the current portfolio of PR convergences, epics, feature runs, delivery graphs, incidents and human-gated decisions.
- Disturbance / variety regulated: Live fleet can stall, hit engine incidents, exhaust review rounds, need a merge decision or require reassignment/resumption after failure.
- Decisive decision or feedback right: The local operator decides how to respond to escalated plan/review/merge tasks and whether to retry or cancel current tracked work. No source-backed autonomous whole-portfolio discretionary S3 owner is established here.
- Decision owner: Legitimate operator of the installed workforce in its supported cockpit/Tasks mode, rather than the deterministic engine or individual developer/worker agent.
- Supporting / enforcement mechanisms: Overview lists across active epics/PRs/features/graphs, Tasks inbox, attributed completeUserTask, incident-retry and cancel operations, engine state reconciliation.
- Closure path: Operator submits typed decision to completeUserTask, or initiates retry/cancel on a tracked instance; engine resumes an affected run and status/read models update, modifying subsequent team execution.
- Boundary reachability: The standard app includes Overview and Tasks user interfaces and first-party API operation; plan, trial-merge, PR-escalation and conformance user-task elements are wired in live BPMN.
- Why this is / is not agent-owned: The S3 parent actor's intervention over current commitments is discretionary. Merge timers, status projections, budgets and process gates merely enforce or inform these current-control decisions.
- Evidence: [overview.page.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/pages/overview.page.json), [tasks.page.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/pages/tasks.page.json), [completeUserTask.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/completeUserTask.ts), [retryIncident.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/retryIncident.ts), [plan-fanout.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/plan-fanout.bpmn), [merge-loop.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/merge-loop.bpmn)
- Basis: structural runtime UI/action/BPMN closure
- Confidence: medium
- Caveats: Current evidence supports local operator current-control mode only; no distinct autonomous whole-workforce S3 mode is asserted. The UI's optional operator label is not authenticated individual identity and should not be represented as an independent audit.
- Whole-system current view: Overview lists active PR convergences, epics, features and delivery graphs of the installed workforce; cockpit shows live worker supply.
- Current-control decision scope: Operator intervention on stalled commitments, problematic reviews and merges, tracked incident retries and cancellations, returned to running or terminal process.


## S3* — Complementary audit
- State: A
- Function: Independently challenge the claims that an epic's delivered implementation satisfied the issue/spec, using direct inspection of landed code rather than worker self-report.
- Disturbance / variety regulated: Implementation and review status may signal apparent completion while actual code is missing, stubbed, untested or outside declared scope.
- Decisive decision or feedback right: Distinct senior:conformance agent compares spec/PRs/actual tree and assigns independent per-slice verdicts and identifies unreported scope changes.
- Decision owner: Model-backed conformance auditor (separate job and prompt from implementer and retro), not deterministic data projector.
- Supporting / enforcement mechanisms: Post-epic trigger, conformance digest, record worker, persisted plan_conformance evidence, human-only conformance-escalation user task.
- Closure path: Auditor files evidence report to epic issue and returns hasDeviations; conformance-record persists verdict, BPMN parks on human operator acknowledgment for detected deviations before continuing to the retrospective phase.
- Boundary reachability: The standard retro BPMN creates the senior:conformance job after epic completion, routes its result through pr.conformance-record and gw-deviations, and exposes a human-only escalated user task.
- Why this is / is not agent-owned: The auditor's substantive source-versus-spec judgment is model-backed; first-party record/gateway only transports it. It is not the ordinary implementation agent reporting itself.
- Evidence: [conformance.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/conformance.md), [retro.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/retro.bpmn), [conformance.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/conformance.ts), [worker.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/workers/conformance-record/worker.ts), [agentCompletion.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/agentCompletion.ts)
- Basis: first-party audit prompt, runtime BPMN and record/ack paths
- Confidence: medium
- Caveats: This review does not observe a real model audit episode, or verify that the operator remedies flagged defects; this is a complementary exception-detection and feedback channel, not proof of automatic remediation.
- Claim being audited: A completed epic delivered the scope, quality and wiring of its source issue/spec.
- Ordinary reporting path: Implementer task status, PR review thread updates, planner/worker completion and task transcripts.
- Complementary access path: Separate conformance agent reads original issue/spec plus actual landed PR diffs/code/tests, looking for unraised deviations and dead paths.
- Independence boundary: Separate named job after implementation, explicit first-party prompt forbidding reliance on worker claims, read-only inspection of implementation and independent evidence report.
- Who acts on findings: Operator receives report on issue and human-only conformance escalation, acknowledges and can pursue corrective follow-up; retro continues only after acknowledgment.


## S4 — Outside-and-then intelligence
- State: ?
- Function: Potential post-epic lesson-to-next-epic adaptation, but the full return path into future installed workforce capability remains unresolved.
- Disturbance / variety regulated: Repeated repository constraints, costly CI/test failures and recurring cross-epic mistakes that might invalidate future standard procedures.
- Decisive decision or feedback right: The senior:retro agent proposes durable changes to target repo instructions/scripts/CI; external human reviewers decide whether the PR actually becomes operational policy/capability.
- Decision owner: Agent proposes; target-repository parent/maintainer controls acceptance. A decisive accepted adaptation at the installed-workforce recursion was not confirmed.
- Supporting / enforcement mechanisms: Learning blackboard, gatherRetro, post-terminal trigger, linked senior:retro prompt, autoRetroEnabled opt-out.
- Closure path: The supplied path ends in a human-reviewed (never auto-merged) promotion PR to a target repo; evidence that merge was observed and the accepted revision changed later workforce agent operation was not found in this review.
- Why this is / is not agent-owned: Agent-authored retrospective and repository PR are meaningful prospective work, but their proposal does not itself demonstrate that current agent capabilities were adapted and reintegrated.
- Evidence: [retro.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/retro.ts), [retro.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/prompts/retro.md), [retro.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/retro.bpmn), [blackboard.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/blackboard.ts), [worker.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/workers/retro-record/worker.ts)
- Basis: explicit first-party source and prompt, incomplete closure witness
- Confidence: medium for proposed option, insufficient to publish A/C/P
- Caveats: Do not misread developer changelogs or routine postmortems as automatic S4. An accepted PR and a future run that operationally consumes its change would materially resolve the '?' question.


## S5 — Policy and identity
- State: —
- Function: No in-boundary first-party decisive identity/ultimate-policy closure identified; task permission, dispatch and merge approvals regulate specific present actions rather than defining organizational identity.
- Disturbance / variety regulated: Choice of ultimate mission, persistent governing authority and change to organization-level policy identity; these are not shown as first-party agent/human policy loops.
- Decisive decision or feedback right: Not evidenced at the assessed workforce recursion, beyond operator-approved individual workflow changes and hard-coded permissible actions.
- Decision owner: No qualifying S5 agent, constructor or parent owner found within declared operating boundary.
- Supporting / enforcement mechanisms: Delivery graph operator-only dispatch, human merge approvals, per-job/retry limits, restricted escalation steward and static completion-policy flags.
- Closure path: No verified identity/ultimate-policy decision -> legitimate authority -> authoritative policy change -> revised future runtime path; ordinary gated actions still resume current workflows.
- Why this is / is not agent-owned: The bundled nodePolicy vocabulary and approval-only PR gates are per-workflow constraints and not a source of organizational identity/ultimate-policy authority.
- Evidence: [nodePolicy.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/nodePolicy.ts), [deliveryGraphProposals.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/deliveryGraphProposals.ts), [dispatchDeliveryGraph.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/dispatchDeliveryGraph.ts), [escalationSteward.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/escalationSteward.ts), [convergence-loop.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/convergence-loop.bpmn), [nano.app.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/nano.app.json)
- Basis: bounded inspected first-party supported paths
- Confidence: medium (scoped negative)
- Caveats: This is a bounded no-material-shipped-path conclusion for this installed application, not a claim that a human or external organization lacks an S5 function.

### Absence scope

- Surfaces inspected: [nano.app.json](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/nano.app.json), [nodePolicy.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/nodePolicy.ts), [escalationSteward.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/escalationSteward.ts), [deliveryGraphProposals.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/app/deliveryGraphProposals.ts), [dispatchDeliveryGraph.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/dispatchDeliveryGraph.ts), [completeUserTask.ts](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/operations/completeUserTask.ts), [convergence-loop.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/convergence-loop.bpmn), [retro.bpmn](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/resources/processes/retro.bpmn), plus standard installation/operation in [README.md](https://github.com/nanobpm/nano-workforce/blob/db6e2f220d8d2a8512897df9cb279e79d6d5cd16/README.md).
- Plausible first-party paths checked: hard-coded node completion policies, operator graph staging/dispatch, human merge and plan decisions, escalation steward permissions, setup configuration and after-epic promotion proposals.
- Why no material first-party path remains: these mechanisms govern concrete tasks/current execution or propose human-reviewed repo changes, without a shipped organization-identity/ultimate-policy decision and returned revision of operating constitutional authority at the declared recursion.


## Recursion

One deployed workforce spans many S1 worker tasks. Separate target repositories and their governance, Nano engine implementation, hosted Studio, and the external hired CLI agent runtimes are not collapsed into the fleet's internal recursion. S3 local operator ownership is described only at this local workforce scope.

## Variety and escalation

Source-backed disturbances include hidden inter-agent edits, failed merges, missing preflight capacity, stale reviewer comments and SLA/incident failures. A separate plan reviewer, deterministic dependency-wave barrier and model-backed PR review constrain these; exceptional work parks on typed human user tasks. A conformance finding parks on a human-only audit acknowledgment. The escalation steward can auto-complete only explicitly eligible reversible tasks; it cannot bypass human-only merge, credential, readiness or conformance gates.

## Evidence gaps

- Source-only assessment: no Nano engine deployment, GitHub-hosted real epic run, external coding-model calls, acceptance-stage review or independent secondary S3* semantic audit executed.
- S4: verify a merged retrospective improvement is ingested by future work and whether this forms a first-party closed prospective loop at the claimed recursion; until then '?'.
- S3*: verify an independent live conformance job actually accesses code/spec and that findings reach a responsible corrective owner, beyond a documented user-task acknowledgment.
- S3: the local operator's whole-current view and task-return routes are evident; distinct automatic whole-workforce S3 ownership and stronger actor authentication are not established.
- S5: the inspected supported app surfaces show operational approvals, but no ultimate-identity policy loop. This negative is scoped to the frozen source and declared shipped mode, not to possible extension or outside enterprise governance.
