---
harness_id: agentforeman
project_name: AgentForeman
repository: https://github.com/kumizeod/AgentForeman
review_ref: 634f9c0906f133fc577d6291c29b8f8cfd6af02a
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# AgentForeman

## Review boundary

- System in focus: a local AgentForeman task/experiment execution cell, with the shipped `briefing` → cooperative/adversarial task controllers, multi-member worker pool, independent checks and reporting; also inspect the shipped campaign and research-council modes for alternate function-specific closure.
- Purpose and identity: turn an operator-defined task or experiment into versioned, bounded work by locally registered model/CLI workers, with accountable evidence and restart-safe coordination.
- Relevant environment: an operator and confirmed task contract, registered Codex/Claude/Gemini/OpenCode/API connections, member-owned accounts/quota, local filesystem, frozen check scripts, supplied research evidence, and external project code/training/evaluation.
- Standard-distribution boundary: installable Python package and CLI/local web panel; first-party `Briefing`, `Cooperation`, `Debate`, `Council`, `Pool`, campaign and verifier controllers operating via registered external model/CLI providers. The providers choose their own outputs, but the first-party controller defines who may act and how results flow.
- Credited operating / distribution surfaces: [`briefing.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py), [`cooperate.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py), [`debate.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py), [`council.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py), [`pool.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/pool.py), [`council_experiment.py`](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council_experiment.py), CLI and bundled local panel.
- Adjacent first-party surfaces excluded from ownership: repository CI matrix, scripted model fixtures, browser regression tests, validation-evidence JSON and past-version validation claims; upstream providers' internal policy/training/approval, real human task acceptance and external project deployment; maintainer roadmap. These may corroborate topology but cannot supply an autonomous operational owner.
- First-party operating / deployment modes considered: explicit pre-execution human clarification/confirmation, cooperative and adversarial bounded tasks, multi-member research council and optional local experiment handoff, campaign/overnight coding experiments, and operator stop/monitor modes. Source inspection is at the pinned v0.13 revision, not an earlier README milestone.
- Recursion level: one locally supervised task/campaign as the operating organization; contributors are distinct task S1 units, not entire independently governed OSS organizations. Multiple remote members do not establish a project-wide parent governance body.
- Reviewed revision: `634f9c0906f133fc577d6291c29b8f8cfd6af02a`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The pre-execution chairman uses a model to elicit goals, deliverables, checks, exclusions, priorities, scope and autonomy boundaries. The controller persists a hash-bound contract and refuses stale confirmations; **the human**, not the chairman, confirms the reviewed charter before launch. Once confirmed, `Cooperation` first asks an integrator model to allocate disjoint assignments among member-owned workers; the contributors work independently, and the integrator receives their artifacts, reconciles inconsistencies and emits a combined candidate. The `Debate` base controller executes frozen checks, sends anchored artifacts/check receipts to distinct model critics, returns issues to the author/integrator for revision, and records `completed_scoped` only within configured verification scope. The chair summarizes rather than overrides check verdicts. This is a genuine first-party orchestration of provider actors, not proof of the models' correctness. [Briefing contract and launch](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L16-L24), [confirmation](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L159-L215), [cooperative control](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py#L66-L148), [critique and gate](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L111-L143).

Alternative shipped modes include a member council with anonymous non-self peer review, separate chair synthesis and a model audit, plus an optional bounded handoff into a local campaign, and overnight Codex experiments with detached supervision, independent checkpoint evaluation and replay archives. The council's supplied sources are not independently fetched, and its findings remain advisory. Local code/training runs inherit the user's permissions; the tool explicitly disclaims a hostile-code sandbox or autonomous deployment. [Council mode](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py#L142-L160), [experiment handoff](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council_experiment.py#L30-L103), [README trust boundary](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/README.md#L371-L380).

## Operational model

In cooperative mode, distinct S1 member workers create task artifacts against individualized assignments; the model integrator is itself an operational unit which reconciles competing contributions into a candidate. A first-party controller regulates ordering, immutable tasks, quotas, deadlines and statuses, but these mechanisms do not themselves own discretionary managerial priorities. Independent review and frozen checks can stop or return candidate work. A confirmed parent human owns the task's initial purpose and permissible-autonomy boundary and must be re-engaged when an executor declares a scope change. The council and campaign are alternate operational workflows at the same local project recursion; do not combine unrelated modes to fabricate an unshipped whole-system executive.

## S1 — Operations

- State: A
- Function: deliver bounded research, report, coding and experiment artifacts by choosing substantive content, implementation steps, tests and responses to criticism.
- Disturbance / variety regulated: open-ended tasks, project/code differences, source gaps, model disagreement, invalid artifacts, failed experimental outcomes and reviewer issues.
- Decisive decision or feedback right: contributor/proposer and integrator model outputs determine assigned artifacts, plans, edits and revisions; campaign manager/worker models choose proposed experiments or repair actions inside hard limits.
- Decision owner: externally provided model/CLI workers acting in first-party, role-assigned runtime paths. Provider infrastructure is external, but first-party Foreman dispatches the roles and consumes their choices.
- Supporting / enforcement mechanisms: member pool leases, frozen input/check hashes, bounded schemas, local supervisor, checkpoint verifier, immutable versions and archives.
- Closure path: accepted human task → integrator plan → member contributions → integrator synthesis → checked/reviewed candidate → revision or scoped result; coding campaign similarly returns independently verified metrics and archive.
- Boundary reachability: the installable CLI and local control panel launch actual `Cooperation`/`Debate`, worker registrations and campaign modes; these are not only examples or architectural plans.
- Why this is / is not agent-owned: content and repair decisions originate in provider-backed actor turns; deterministic validation and human contract approval bound but do not author those choices.
- Evidence: [role-specific jobs and integration](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py#L66-L94), [proposal/revision and review loops](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L111-L188), [campaign workflow described by maintainer](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/README.md#L194-L214).
- Basis: structural.
- Confidence: high for shipped actor and feedback topology; no live authenticated provider test performed.
- Caveats: simulated workers/fixtures test protocol, not model competence; standalone CLI tools and their internal decisions are not first-party Foreman implementations.

## S2 — Coordination

- State: A
- Function: attenuate the risk that simultaneous member work produces overlapping, incompatible or missing contributions before a combined task artifact is accepted.
- Disturbance / variety regulated: integration conflicts among independently produced contributor artifacts and assignment gaps when multiple workers work on one deliverable.
- Decisive decision or feedback right: an integrator model produces an explicit non-dependent assignment/integration contract, then observes all member results and chooses how to reconcile inconsistencies in the combined artifact; checks/critics feed residual defects back into the integrator's subsequent revision.
- Decision owner: the configured integrator model, not the deterministic pool queue; the controller requires one assignment per contributor and complete contribution receipts.
- Supporting / enforcement mechanisms: role-identity separation, one-to-one assignment validation, isolated contribution prompts, no partial integration, frozen checks and versioned review feedback.
- Closure path: integrator-generated separation contract → distinct S1 member work → all contributions returned → integrator resolves cross-member incompatibilities → independent checks/criticism → integrator revision or explicit stop.
- Boundary reachability: cooperative mode's first-party `Cooperation.enter` and `advance` dispatch this path from supported CLI/panel entry, with actual returned model proposals; it does not depend on hypothetical agent code.
- Why this is / is not agent-owned: choices about division and reconciliation of work are made by the model integrator; controller checks completeness but does not synthesize those adjustments.
- Distinct S1 units: named member-owned contributor worker tasks, assigned independently in `Cooperation`; the integrator is separately registered.
- Inter-S1 disturbance: inconsistent or overlapping parts of the intended combined artifact, plus missing contributor deliverables.
- Attenuating coordination relation: integrator's explicit partition/integration contract and later content-aware reconciliation of the returned contributions.
- Feedback into subsequent S1 behaviour: the integrator is instructed to resolve observed inconsistencies in its combined output; check failures and independent critique issues then return into its `revise` turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: unlike a bare fan-out, the model first constrains dependencies, then evaluates actual multiple contributor outputs for cross-unit inconsistency and revises a shared result under feedback. This credits the cooperative mode only, not every `Pool` dispatch or council stage.
- Evidence: [integrator plan and partition prompts](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py#L66-L94), [completeness gate and integration](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/cooperate.py#L109-L148), [reviewed revision return](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L198-L226), [cooperative operating guide](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/docs/COOPERATIVE.md#L8-L25).
- Basis: structural.
- Confidence: medium: explicit code path and authority, but not measured inter-agent conflict suppression.
- Caveats: contributor workers are not sent a second live coordination round; corrective feedback reaches the integrator/revised combined work, not a negotiated peer-to-peer protocol. This is a narrow project-cell S2, not organization-wide scheduling.

## S3 — Inside-and-now control

- State: —
- Function: no credited whole-cell discretionary current control over a live portfolio of resource and commitment tradeoffs.
- Disturbance / variety regulated: quota exhaustion, worker failure, stop requests, budgets, contribution absence and validation failures, handled through fixed runtime constraints or task-level S1/S2 corrections.
- Decisive decision or feedback right: hard limits, explicit operator choice of roles and run parameters, worker eligibility, cancellation and retry scheduling; no first-party executive agent with whole-task current view and arbitrable priority/resource commitments is established.
- Decision owner: developer-defined controller logic and pre-run operator settings; the advisory chair cannot reallocate resources or overrule check status.
- Supporting / enforcement mechanisms: `Pool` leases and quota waiting, stop/terminate, stage deadlines, reporting, dashboard and durable SQLite state.
- Closure path: deterministic enqueue/wait/fail/stop and human-visible receipts, not a discretionary whole-system management intervention returning to change a portfolio of current S1 operations.
- Why this is / is not agent-owned: naming a chairman, campaign manager or central controller does not transfer a current executive right; model choices are task-domain plans or synthesis, while workload/budget enforcement remains fixed.
- Evidence: [advisory chair and fixed controller gates](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L30-L36), [task/role budget validation](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L43-L62), [council staged transitions](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py#L211-L265).
- Basis: structural.
- Confidence: medium-high for currently reviewed task/campaign paths.
- Caveats: initial human selection of node counts/budgets is not itself a closed live S3 parent mode; separate member-owned workers do not supply a unified higher-level executive.

### Absence scope

- Surfaces inspected: briefing role selection, worker pool, cooperative/adversarial stages, council, campaign/overnight supervision, current status/panel and README scope.
- Plausible first-party paths checked: chairman role plan, operator dashboard and stop, integrator intervention, manager experiment decisions, quota-based failover and task-resource budgets.
- Why no material first-party path remains: role plan is pre-run and human-confirmed, integrator content decisions regulate S1/S2, and running quota/schedule/termination are fixed controllers; a live whole-system state plus discretionary current commitment/resource arbitration with returned intervention is not demonstrated.

## S3* — Complementary audit

- State: A
- Function: challenge a candidate's claimed adequacy through independently assigned critics, frozen external checks, and the council's separate post-synthesis audit.
- Disturbance / variety regulated: author self-assessment, invalid source support, untested claims, silent check failures and unresolved adversarial findings.
- Decisive decision or feedback right: distinct critic models write anchored issues and accept/revise/reject verdicts, while a separate council audit model can reject a chair's synthesis; the controller validates anchors and refuses unsupported scoped success.
- Decision owner: registered non-author reviewer model(s), with first-party controller enforcing receipt validity; fixed Python checks are complementary measured evidence, not autonomous verdict owners.
- Supporting / enforcement mechanisms: separate reviewer identity, non-self peer review, immutable evidence/check receipts, valid line anchors, issue IDs, recorded test results, versioned follow-up and independent checkpoint evaluator for coding campaigns.
- Closure path: author/integrator candidate → frozen checks and independently role-assigned critique → blocking issues/reject or acceptance → returned revision/retest or saved `needs_evidence`/rejection with outstanding issues.
- Boundary reachability: cooperative/adversarial task mode actively dispatches critics and processes their decisions; council's `audit` stage is another shipped path, not an unintegrated test fixture.
- Why this is / is not agent-owned: criticism and final audit judgments are model-authored under distinct role identities; controller refuses invalid structural claims but is not itself a deliberative auditor.
- Claim being audited: proposed task artifacts and council final answer meet the configured contract/checks and do not leave known major findings unresolved.
- Ordinary reporting path: proposer or integrator submits candidate artifacts, claims and eventual chairman summary.
- Complementary access path: critics receive full artifact texts, original supplied source strings and actual frozen-check receipts for anchored inspection; the council audit receives original independent answers, criticisms and sources, not merely the chair's self-summary.
- Independence boundary: different registered model/worker identities and role-specific prompts, with non-self review and separate local check executor; no guarantee of separate underlying foundation models, externally retrieved facts or measured true-world accuracy.
- Who acts on findings: `Debate.critique` returns issues into revision or rejects/stops; `Council.advance` prevents `completed_candidate` on unsupported/missing audit findings; results preserve unresolved questions for humans.
- Evidence: [critics see direct artifacts/check receipts](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L119-L129), [anchored issue and gate](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L198-L226), [non-self council review and audit inputs](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py#L147-L160), [audit status gate](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py#L245-L252).
- Basis: structural.
- Confidence: medium-high for topology and inspectable independent access, not audit quality.
- Caveats: external reality is not independently retrieved; input quote matches are not source authentication; scripted provider tests are not proof that independent models correctly catch factual errors.

## S4 — Outside-and-then intelligence

- State: —
- Function: no credited first-party future-environment intelligence feedback that durably adapts *AgentForeman's own* operating capability at the assessed local task recursion.
- Disturbance / variety regulated: open-ended future research questions, suggested tests and candidate experiment goals, but these remain user-seeded task outcomes or inputs to an isolated experimental project.
- Decisive decision or feedback right: council models propose future-oriented experiments and a selected proposal may trigger a bounded campaign, yet no agent/parent decides to change the harness's task-policy, membership/capabilities or ongoing strategic adaptation agenda.
- Decision owner: operator frames the research question and enables experiment handoff; models author candidate research text and campaign local edits, not the harness's prospective capability charter.
- Supporting / enforcement mechanisms: supplied source catalog, research council suggestions, audit status, optional campaign launch and independently verified local archives.
- Closure path: council candidate proposal → optional local experiment (with frozen project contract) → result metrics/archive; no inspected edge applies the learning as a durable change to the running Foreman organization or its future capability decisions.
- Why this is / is not agent-owned: a task about future experiments and even executable research tests is S1 at the assessed project task level unless the external/future intelligence actually returns into management of the harness's present capability.
- Evidence: [research context and no direction-changing rule](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council.py#L52-L59), [optional handoff restricted to one frozen experiment](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/council_experiment.py#L38-L100), [README current scope](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/README.md#L194-L214).
- Basis: structural.
- Confidence: medium: strongest candidate path is research council-to-experiment, but no self-adaptation closure at this recursion.
- Caveats: a separately framed viable *research organization* might classify the experiment handoff differently; that recursion is not silently substituted for the AgentForeman task/campaign boundary.

### Absence scope

- Surfaces inspected: council research, proposed experiments, optional execution handoff, campaign/manager, local project configuration and evidence archive return.
- Plausible first-party paths checked: prospective council experiments, measured training feedback, model manager's new experiment selection, operator-enabled handoff and maintainer roadmap.
- Why no material first-party path remains: future research artifacts improve an operator-specified experiment candidate, but no shipped control step treats external change intelligence as a mandate to adapt the continuing harness's own capabilities or returns that choice to its present organization.

## S5 — Policy and identity

- State: P
- Function: retain legitimate authority over the specific task-cell charter, permitted autonomous scope, goal and acceptance obligations before and during delegated execution.
- Disturbance / variety regulated: ambiguity about what work is authorized, attempted unilateral goal/constraint changes and conflict between worker-proposed new scope and the human-approved task identity.
- Decisive decision or feedback right: the operator accepts or edits the **version- and hash-bound** contract with explicit goals, exclusions, constraints, priorities and allowed decisions; a worker may flag need for scope change but cannot self-approve it.
- Decision owner: the local human operator as legitimate parent of this delegated task cell. The chairman writes suggestions but cannot confirm, revise an already launched charter or override the parent decision.
- Supporting / enforcement mechanisms: contract schema, immutable version/fingerprint, explicit confirmation, binding in child task record, fail-closed stale launches and pause-on-scope-change.
- Closure path: identity/authority question → chairman-human clarification → operator reviews and confirms exact charter → persisted binding governs worker prompts → scope conflict pauses ongoing execution → new human clarification/confirmation is required before a changed charter can govern new work.
- Boundary reachability: default shared task path is explicitly `Briefing` and `confirm` followed by `Debate`/`Cooperation`, with child-controller contract binding and scope-change pause enforcement. This is a supported parent-governed mode; unconfirmed standalone council commands are not credited as the same S5 loop.
- Why this is / is not agent-owned: the model can propose a role plan or articulate boundaries, but code requires a direct human confirmation fingerprint and rejects any material execution scope change without a new human decision. Only `P` is established, not autonomous S5.
- Identity / ultimate-policy issue: the particular delegated task's mission, exclusions and permitted decisions — who may redefine that mission when execution finds it insufficient.
- Ultimate authority in each claimed mode: the human who edits/confirms the binding contract is final parent authority; model chairman and executing members are subordinate.
- Return-to-operation path: exact reviewed contract flows into the child task prompt and checked binding; scope-change notice creates a recorded pause and forces a new confirmed charter for altered execution.
- Evidence: [contract includes goal, priorities, exclusions and autonomy](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L16-L24), [chair cannot self-confirm](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L99-L108), [human version-bound confirmation and launch](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/briefing.py#L159-L215), [binding and immutable task ID](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/task_contract.py#L6-L25), [executor scope-change pause](https://github.com/kumizeod/AgentForeman/blob/634f9c0906f133fc577d6291c29b8f8cfd6af02a/src/agentforeman/debate.py#L87-L95).
- Basis: structural.
- Confidence: medium-high for explicit parent contract and returned scope guard; semantic deviation detection is only agent self-report.
- Caveats: this `P` is **local task charter governance**, not a claim that the OS project or multiple contributors share an authoritative organizational parent; fixed test configuration and general UI stop by themselves would not justify S5.

## Distributed OSS parent arrangement

Workers can use independent accounts, and upstream OSS contributors can fork/run this package, but the evidenced parent authority is **one local operator per confirmed task cell**. Registration of member identities, shared quota leases, GitHub maintainers and CI do not constitute a shared governance layer over all independently operated Foreman instances. The `P` notation is not extended to the whole OSS project.

## Self-hosted and non-human modes

Local member-owned worker pool and web panel are self-hosted; operator confirmation materially changes S5 in the supported `briefing` path, but a panel stop button is not S3 parent governance. Council/adversarial commands can also run without briefing; those modes do not gain the task-charter `P` loop by implication, while the supported confirmed mode establishes the mode-specific S5 finding.

## Recursion

Members are independent contributors within a single current task; the integrator regulates shared deliverable compatibility. The local confirmed task is the focal viable organization. Project-wide maintainer governance, external model-provider accounts, and the external target ML experiment are different recursion boundaries and cannot supply missing current-control or strategic-adaptation decisions by aggregation.

## Variety and escalation

Model workers absorb task-context variety, the integrator absorbs conflicting contributions, independent critics and frozen check scripts expose acceptance failures, and the controller mediates retries/terminal evidence states. Quota waiting, role eligibility, time limits and cancellation are deterministic; unresolved critical issues and missing tests remain explicit. A material contract-scope change causes a pause for renewed human authorization; provider failures or a deadline stop with preserved state rather than silently synthesizing success.

## Evidence gaps

- No authenticated live Codex/Claude/Gemini/API task or overnight performance run was executed for this review. Claims about model quality, distributed execution reliability and empirical S2/S3* effectiveness remain unmeasured.
- The source and README provide scripted-fixture CI evidence, but historical matrix pass counts are not treated as independently observed current-head native execution results.
- A local `unittest` attempt with `PYTHONPATH=src` could not import `psutil`, a declared dependency, and therefore did not execute the Python tests. This is an environment dependency issue, not an observed upstream test failure.
- S2 is deliberately narrow to model integrator reconciliation of returned member contributions; no peer-to-peer contributor correction is demonstrated.
- The independently audited evidence corpus is operator-supplied and quote-matched, not independently retrieved or authenticated. Neither checker success nor model agreement proves broad factual correctness.
