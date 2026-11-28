---
harness_id: alpacawork
project_name: AlpacaWork
repository: https://github.com/alpacakit/alpacawork
review_ref: 6bebae6f24cba458a27514a36d301a116486223f
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# AlpacaWork

## Review boundary

- System in focus: One installed AlpacaWork project as a task organization, including the coordinator, task owners, members and project operator.
- Purpose and identity: Turn user requests into verified task results across local coding-agent processes while retaining work and authority state.
- Relevant environment: A self-hosted PC with supported engines, their configured models, project repository/workspace and a legitimate project operator.
- Standard-distribution boundary: Source-distributed local backend and CLI, browser/phone user interface, engine adapters, task/run orchestration and supported managed skills.
- Credited operating / distribution surfaces: Native installation, coordinator/owner/member launch roles, versioned returns, project settings, standard independent review and the bundled opt-in model-choice trial workflow.
- Adjacent first-party surfaces excluded from ownership: External provider internals, upstream engine governance, AlpacaWork development tests and release telemetry. One-off delegates invoked by an external conversation are not required for the credited functions.
- First-party operating / deployment modes considered: Local or remote browser control of one local runtime, native agent launches and task-owned member review. Model optimization uses the opt-in bundled skill.
- Recursion level: Project task tree. A child with its own responsible agent is a nested operational unit.
- Reviewed revision: 6bebae6f24cba458a27514a36d301a116486223f
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The coordinator turns a request into tasks and selects the responsible agents. The backend launches configured runtimes with a role-specific task snapshot, retains the task outside the model session, and records reports, placement and decisions against current revisions. A return can cause an owner continuation. Managed skills supply organization-specific coordination and verification protocols and a supported opt-in trial of model/effort choices.

## Operational model

A task owner chooses its work and how to meet its done condition. Independent child owners carry distinct results. Members help the responsible agent under its coordination. The project operator retains acceptance of user-requested results and project policy rights. Agent engines and scheduling support the roles.

## S1 — Operations

- State: A
- Function: Deliver assigned task outcomes via native agent owners and member Runs.
- Disturbance / variety regulated: An instruction can require different workspace actions, supporting evidence and interpretation of changing task state.
- Decisive decision or feedback right: Select task actions, split or execute work within scope, and report the completed result or outstanding decision.
- Decision owner: The model in the first-party owner role, with separately commissioned models for delegated results.
- Supporting / enforcement mechanisms: CLI/API, agent adapters, launch context, requests, task/run persistence and report policy.
- Closure path: The selected engine works against the given workspace and task context. The owner writes a result that closes an agent-created child or enters normal acceptance of user-requested work.
- Boundary reachability: The standard installation supplies owner and coordinator skills, role-bearing launch context and the engine launch entry point. Selecting and authenticating an engine supplies infrastructure for the first-party operating protocol.
- Why this is / is not agent-owned: The model decides which actions constitute the job and how to produce it. The backend enforces states, launches processes and carries the action's result.
- Evidence: [README.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/README.md#L69-L96), [skills/alpacawork/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/SKILL.md#L22-L38), [skills/alpacawork/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/SKILL.md#L80-L85), [skills/alpacawork/references/owner.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/owner.md#L30-L44), [apps/backend/src/runs/launch-agent.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/runs/launch-agent.ts#L46-L75), [skills/alpacawork/references/lifecycle.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/lifecycle.md#L25-L31)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Final user acceptance remains explicit for user-requested top tasks. Qualification uses the supplied autonomous child and task-worker closure.

## S2 — Coordination

- State: A
- Function: Regulate interference between task owners whose work or decisions would overlap and whose parents/children compete for shared execution capacity.
- Disturbance / variety regulated: Overlapping requests can cause duplicate work and contradictory instructions. Waiting in a live parent run consumes a slot needed by a child.
- Decisive decision or feedback right: Decide which results can work independently, route overlapping instructions to the existing responsible actor, and revise the division on new dependencies.
- Decision owner: The directly responsible agent and the native coordinator, at the respective parent and project boundaries.
- Supporting / enforcement mechanisms: Task and placement identity, dependencies, versioned requests, one recipient for a member, slot limits, return router and lifecycle records.
- Closure path: New or conflicting input returns to the responsible worker with scope. An owner yields instead of occupying a slot while waiting, and the router wakes it with the child/member outcome to reconcile the next actions.
- Boundary reachability: The bundled coordinator and owner instructions specify overlap, coupled decisions and the yield/return procedure, and the native router can wake the appropriate owner.
- Why this is / is not agent-owned: The scheduler enforces state and resource limits. Agents determine which coupled results stay together and how conflicting changes are routed and reconciled.
- Distinct S1 units: Distinct task owners with independently scoped results and their own model Runs.
- Inter-S1 disturbance: Two tasks can duplicate or conflict on the same result. Worker slots can be held by parent Runs while child Runs need them.
- Attenuating coordination relation: Owner/coordinator inspects independence, reuses an existing responsible task for overlap, preserves one member instruction lane, and yields the live slot during a wait.
- Feedback into subsequent S1 behaviour: New dependency evidence or a child/member return re-enters the owner context for re-planning, rework or continuing independent work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The native role contract explicitly mitigates conflicting instructions, coupled work and contention, and the outcome informs the next action rather than merely being logged.
- Evidence: [skills/alpacawork/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/SKILL.md#L45-L52), [skills/alpacawork/references/coordinator.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/coordinator.md#L72-L77), [skills/alpacawork/references/request.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/request.md#L3-L11), [skills/alpacawork/references/owner.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/owner.md#L30-L38), [skills/alpacawork/references/owner.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/owner.md#L54-L68), [apps/backend/src/runs/scheduler.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/runs/scheduler.ts#L130-L166), [apps/backend/src/control/return-router.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/return-router.ts#L165-L187)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: This evidence concerns task and execution interference. It does not assert automatic Git write-set conflict detection.

## S3 — Inside-and-now control

- State: A(P)
- Function: Control currently active project commitments and resources via task supervision and returned state changes.
- Disturbance / variety regulated: A task can fail, split into coupled obligations, need a new owner or become lower priority than pending work.
- Decisive decision or feedback right: Select whether to retry or stop a currently blocked commitment, reassign its owner or hold/release work under current priorities.
- Decision owner: Native parent/coordinator model for ordinary reassignment, retry/stop and linked current commitments. The legitimate project operator owns explicit user-controlled current interventions.
- Supporting / enforcement mechanisms: Task-tree read model, task/placement revisions, role authorizer, stop and hold transitions, handover and resumed launches.
- Closure path: The chosen disposition changes placement or task state. A handover supplies current evidence to the replacement. A stop propagates to the relevant Runs and unfinished subtree.
- Boundary reachability: Supported launch roles have typed placement, task and run controls. The screen and coordinator proxy return explicit operator decisions through the same task lifecycle.
- Why this is / is not agent-owned: Runtime capacity limits are enforcement. The parent-agent or operator decides what commitment to carry, restore or stop from current evidence.
- Whole-system current view: Task list, current placements and Runs plus open work and changed-child context give the relevant current view of the project and task subtree.
- Current-control decision scope: Choose current obligation continuation, replacement or stop, and operator hold/release or rescope for the project.
- Evidence: [README.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/README.md#L110-L118), [skills/alpacawork/references/coordinator.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/coordinator.md#L62-L75), [skills/alpacawork/references/owner.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/owner.md#L54-L68), [skills/alpacawork/references/lifecycle.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/lifecycle.md#L36-L53), [apps/backend/src/control/placement-commands.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/placement-commands.ts#L63-L82), [apps/backend/src/control/task-transition.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/task-transition.ts#L264-L289)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The coordinator requires a user interaction to run. The native parent owner can receive automatic continuations. Estimation, slot gates and backoff do not constitute current decisions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Native parent-task owner or coordinator when handling present work | A child or top commitment needs intervention | Agent chooses retry, stop or replacement. Task/placement state and actual work change | [skills/alpacawork/references/coordinator.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/coordinator.md#L64-L75), [skills/alpacawork/references/owner.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/owner.md#L61-L68), [apps/backend/src/control/placement-commands.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/placement-commands.ts#L63-L82) |
| Parent (`P`) | Project operator | Current work appears in the user's turn, or priorities change | A direct or quoted decision holds, releases, redirects or stops a current obligation and changes subsequent Runs | [README.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/README.md#L114-L118), [skills/alpacawork/references/lifecycle.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/lifecycle.md#L36-L53), [apps/backend/src/control/task-transition.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/task-transition.ts#L264-L289) |

## S3* — Complementary audit

- State: A
- Function: Independently evaluate a candidate artifact against the user's actual request and return findings before the owner reports it ready.
- Disturbance / variety regulated: A producer may misinterpret the requirement or declare an artifact finished using inadequate evidence.
- Decisive decision or feedback right: Select direct checks and issue required findings, allowing the owner to accept, fix or rebuild on evidence.
- Decision owner: A fresh reviewer model under the standard quality protocol, with an owner model responsible for disposition of findings.
- Supporting / enforcement mechanisms: Managed quality skill, separate member Run, versioned artifact reference, request/return history and bounded rounds.
- Closure path: The reviewer inspects the actual artifact at the supplied version. The owner reads findings, fixes and submits again or reports unresolved requirements when the configured cap is reached.
- Boundary reachability: The bundled managed quality skill dispatches a separate reviewer role through native member placement and request. The member result returns to the owner without custom developer glue.
- Why this is / is not agent-owned: The reviewer's judgment comes from a separate invocation and direct evidence. The producer's self-check and the user's acceptance are distinct paths.
- Claim being audited: The actual versioned result meets the user's words and required checks.
- Ordinary reporting path: Builder report and the evidence the builder already verified.
- Complementary access path: Reviewer is commissioned to operate or inspect the actual artifact in its medium and may return unverified when that access fails.
- Independence boundary: Review uses a distinct conversation and role, with original user words and a pinned result independent of the builder's account.
- Who acts on findings: Owner judges the returned findings against the gate, records them and initiates fixes or re-review.
- Evidence: [packages/core/src/installed-skills.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/packages/core/src/installed-skills.ts#L12-L18), [skills/alpacawork/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/SKILL.md#L10-L20), [skills/alpacawork-betterquality/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-betterquality/SKILL.md#L46-L78), [skills/alpacawork-betterquality/references/alpacawork.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-betterquality/references/alpacawork.md#L1-L6), [skills/alpacawork-betterquality/references/reviewer.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-betterquality/references/reviewer.md#L3-L15), [skills/alpacawork-betterquality/references/rounds.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-betterquality/references/rounds.md#L19-L28)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The quality protocol permits self-check for light work and does not universally commission a reviewer.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt the project model/effort policy for future work categories using evidence from reviewed capability trials.
- Disturbance / variety regulated: The set and cost/capability of available engines and human quality demands can change, making near-term work cheaper or riskier under a previous rule.
- Decisive decision or feedback right: Judge whether a successful trial should change the standing selection rule for later task launches.
- Decision owner: Project operator owns adoption. The owner agent selects and evaluates the bounded trial, and the coordinator writes only after agreement.
- Supporting / enforcement mechanisms: Managed opt-in skill, available provider selections, separate review result, labelled trial outcomes, policy values, launch prompt injection and normal placement selection.
- Closure path: A passing trial yields a proposal for a reusable rule. The operator accepts or declines it, and an accepted rule is saved and read for comparable later tasks.
- Boundary reachability: Model optimization is a bundled supported opt-in. The skill specifies trial, review, recommendation and user-approved write, and the native launches consume project settings and policy.
- Why this is / is not agent-owned: Models experiment, interpret the verdict and propose an option. The decisive change to standing future policy belongs to the operator.
- External distinction: The currently offered models/efforts and relative cost or capability constraints, evaluated against real task quality.
- Future / prospective distinction: Trial results are classified by work type to select the option for subsequent requests, including whether changed available models justify trying again.
- Adaptation option generated: Use a reviewed lighter model or effort for this kind of work, or retain the baseline if significant findings persist.
- Path back into current capability / S3: User agreement returns through the coordinator's project-policy save. The standard role and launch consume the new rule on future matching work.
- Evidence: [packages/core/src/installed-skills.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/packages/core/src/installed-skills.ts#L12-L18), [skills/alpacawork-modelpickoptimization/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-modelpickoptimization/SKILL.md#L10-L30), [skills/alpacawork-modelpickoptimization/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork-modelpickoptimization/SKILL.md#L32-L37), [skills/alpacawork/references/coordinator.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/coordinator.md#L66-L70), [apps/backend/src/control/start-text.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/start-text.ts#L78-L94), [docs/projects.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/docs/projects.md#L35-L51)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The mode is opt-in, excludes unreviewable effects and does not require comparison with a full independent baseline run.

## S5 — Policy and identity

- State: P
- Function: Set the delegated authority, forbidden work and approval reservation that govern project agents.
- Disturbance / variety regulated: Project demands or candidate working practices can conflict with what the operator intends to allow or reserve.
- Decisive decision or feedback right: Decide a new project policy or change the set of decisions reserved to the operator.
- Decision owner: The legitimate project operator, with the coordinator acting as its attributable proxy.
- Supporting / enforcement mechanisms: Policy value, quoted direction, scoped project hierarchy, backend-authorized transaction and inherited launch context.
- Closure path: The authenticated operator edits the setting or requests the quoted change. Subsequent eligible agents receive the policy chain and apply it to action and approval choices.
- Boundary reachability: The installed project settings and task update route write the project policy. Native role instructions and launch context read the policy across the governing project chain.
- Why this is / is not agent-owned: The coordinator communicates, records and applies the governing rules. The instructions reserve rewriting project policy to a current project-operator request.
- Identity / ultimate-policy issue: Which work and effects the project authorizes, requires consultation for or forbids across its task organization.
- Ultimate authority in each claimed mode: The project operator holds the policy decision. The coordinator relays the current direction and is subordinate to that delegation.
- Return-to-operation path: Policy is saved in project values and occurs in launch context or a supplied read command for each scope.
- Evidence: [docs/projects.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/docs/projects.md#L21-L34), [skills/alpacawork/references/coordinator.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/references/coordinator.md#L64-L70), [apps/backend/src/control/task-commands.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/task-commands.ts#L215-L240), [apps/backend/src/control/project-settings.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/project-settings.ts#L150-L162), [apps/backend/src/control/start-text.ts](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/apps/backend/src/control/start-text.ts#L78-L94), [skills/alpacawork/SKILL.md](https://github.com/alpacakit/alpacawork/blob/6bebae6f24cba458a27514a36d301a116486223f/skills/alpacawork/SKILL.md#L132-L137)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Natural-language project policy is behavioral governance. It does not itself enforce an OS sandbox or guarantee provider adherence.

## Recursion

A responsible child with its own task and owner is a recursive operating cell. A member supplies separately invoked work or review within its owning task. The project operator is the legitimate parent for cross-task commitments and project-wide policy.

## Variety and escalation

Typed task states, permissions, admission, queue limits, review, question and return accounting bound ordinary operating variety. Exceptional stuck states are presented for the user's turn. A separate formal algedonic classification was not needed for the vector.

## Evidence gaps

Static review only. No live provider session, reviewed model trial, reviewer trace, concurrency collision or policy enforcement run was executed. Optional model optimization and independent review claims describe reachability in the supported managed-skill mode.
