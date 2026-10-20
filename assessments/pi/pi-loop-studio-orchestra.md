---
harness_id: pi-loop-studio-orchestra
project_name: pi-loop-studio-orchestra
repository: https://github.com/LEO001020/pi-loop-studio-orchestra
review_ref: 0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pi-loop-studio-orchestra

## Review boundary

- System in focus: Shipped local Pi Loop Studio runtime's model-directed task work cell and its bounded XState worktree composition, review and gated publication process; a normal chat-only path is included as a separate supported mode.
- Purpose and identity: Turn a user-given software/research objective into evidence-backed, code-tested and independently reviewed changes in a user project workspace without publishing unverified proposals.
- Environment: User's task and workspace, Git/Node/Python and tools in an installed local environment, externally configured principal/executor/auxiliary model APIs and credentials, optional web/research sources, changes and faults from parallel workers, resource constraints and user approval of goals.
- Standard-distribution boundary: Supported `server/index.mjs` and `server/workflow.mjs` runtime invoking `server/pi.mjs` Pi SDK agent actors and model streams, server-side role/tool configuration, `server/workspace.mjs` worktree/result/publishing logic, `server/store.mjs` persistent run/job evidence, normal UI/API request modes. Provider inference, Git implementation, downloaded Python kernels and other external runtime internals support but are not credited as first-party organizational owners.
- Credited operating / distribution surfaces: [server/index.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/index.mjs); [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs); [server/tools.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/tools.mjs); [server/commands.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/commands.mjs); [server/settings.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/settings.mjs); [server/context.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/context.mjs); [server/python.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/python.mjs); [server/research.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/research.mjs).
- Adjacent first-party surfaces excluded from ownership: README / architecture prose and release-manifest aspirations; installed third-party SDK internals, `docs/verification` and acceptance screenshots, contributor/project maintenance, installer and release scripts, tests and fixtures, the end user's wider project team or organization. They can corroborate shipped paths, but are not themselves the credited operating system and do not supply function owners.
- First-party operating/deployment modes considered: Chat-only and model-routed task mode; task root `routing → preparing → scoping → reconnaissance → recon_audit → planning → executing → verifying → judging → publishing` with repair/blocked/pause; job `executing → auditing → integrating` with retries; user-stop/resume, checkpoint recovery, configured models and concurrency slots, single writer publishing. No task inference or workspace edits were executed during this assessment.
- Recursion level: One user-commissioned task operation with transient code/research worker jobs plus review; no demonstrated independently viable continuing business departments at a higher recursion.
- Reviewed revision: `LEO001020/pi-loop-studio-orchestra@0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7`, Git source tree `eec5d449ed36a87bb5bf373e23e5a0b660f185c3`; GitHub ID 1365788813, default main, created 2026-09-11T09:47:30Z, public nonfork/nonarchived MIT.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The local Express backend owns the work session and drives an XState `LoopController`. A model-configured principal probes/reads the workspace, creates scout assignments and a typed job DAG, with role-aware external-model Pi SDK `Agent` instances performing scout reading, task-specific implementation and independent review in isolated worktrees. The principal verifies scoped original acceptance criteria against actual validation commands, candidate manifest and audited integrated jobs. `Workspaces` implements captured Git candidates, disjoint paths, approved merge and a single-writer publish operation. `Store` persists check-pointed stages, job state and tool receipts, enabling resume; `PiRuntime` handles local/role concurrency and provider streams. A separate chat mode answers without pretending to modify files. [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs); [server/index.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/index.mjs).

A central evidence distinction is that real task-level independent reading/approval occurs, but its object is source changes and user task evidence, not a distinct S3 organization's management reports. Multiple role workers are temporary assignments in the same user work cell. Their owned-path conflict controls and dependency DAG are substantial local work coordination; they do not by themselves establish continuing viable operations with a VSM S2/S3 managerial relationship.

## Operational model

The supportable first-party mode uses the Pi SDK agent abstraction with **configured external model endpoints**, a task-contingent principal and scout/worker/auditor models, and deterministic orchestration/side-effect enforcement. Independent audits read frozen candidates and may reject them, the host prevents an unaudited change from becoming a dependency, and the principal cannot publish a candidate without pass records from the job audits, concrete verification commands, success criteria and host gates. Model decisions are not conflated with deterministic concurrency, XState, storage or Git enforcement.

## S1 — Operations

- State: A
- Function: An autonomous, environment-facing software/task work cell: model-directed reconnaissance, evidence reading, typed task planning, tool-using implementation in isolated worktrees and verified integration/publishing, or a separate conversational response in chat mode.
- Disturbance / variety regulated: Uncertain user intent, unfamiliar code and files, conflicting implementation changes, partial reconnaissance, task failures, rejected evidence, provider/time-budget failures and tests that fail after a proposed change.
- Decisive decision or feedback right: The configured model principal chooses task decomposition and success-criteria plan; models running executor roles investigate and implement tasks within owned paths, while read-only investigator/auditor models independently sample evidence and pass/fail candidate changes. Model-run tool access and final typed results return to XState; accepted changes are integrated and potentially published by deterministic host gates.
- Decision owner: First-party PiRuntime creates Pi agent actors and connects configured models for principal, executor and auxiliary roles, which own substantive local coding/evidence/planning discretion. External model services supply inference; the deterministic server/XState/Git host owns mechanical safety and execution, and human supplies objective/configuration.
- Supporting / enforcement mechanisms: The shipped backend wiring uses Pi SDK Agent, per-role model routing and streaming, tool bundles, role concurrency slots, XState root/job lifecycle, checkpointed SQLite, workspace branch and accepted-facts ledger, shell command/test execution, manifest comparison and a single-writer publish gate.
- Closure path: HTTP task request → role-model scoping / scout evidence → independently audited findings → principal plan/task DAG → executor worktree modifications → distinct auditor checks → gated integration → real verification commands + final principal acceptance → host single-writer publication or a repair/blocked path; future decisions in same run inspect earlier results.
- Boundary reachability: The server constructs LoopHost and its LoopController; the run transitions invoke PiRuntime structured and run on configured model credentials, worker/auditor subgraphs and accepted-worktree host operations. Both main and per-job paths are called by supported normal task mode rather than tutorial-only samples.
- Why this is / is not agent-owned: Without the task-specific model actors, the host cannot produce observations, select substantive code changes or judge acceptance. Without the deterministic host the distributed model decisions would lack checkpoint/worktree isolation, tool and publish enforcement. Agent ownership is task discretion, not the host's hardwired state transitions.
- Evidence: [server/index.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/index.mjs); [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/tools.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/tools.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs); [server/commands.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/commands.mjs)
- Basis: structural and explicit first-party code, source-wired task mode
- Confidence: High for model-owned work cells and feedback path; no live model performance checked.
- Caveats: Uses externally configured model endpoints and model authentication; code presence is not proof of successful deployment or AI output quality. Separate chat path is a single S1 user conversation, not a new viable organizational recursion.

## S2 — Coordination

- State: —
- Function: No separately substantiated regulation of real recurrent oscillation between *independently viable continuing* S1 departments at a wider organizational recursion.
- Disturbance / variety regulated: Parallel job branches can attempt overlapping paths, require dependencies or compete for capacity; their attempted changes can conflict during host integration.
- Decisive decision or feedback right: The principal generates DAG/ownedPaths, validator rejects overlapping independent tasks, per-role slot pools limit concurrency and Git integration resolves a particular worktree path. Although these are real **task-workflow coordination** functions, the source does not establish multiple continuing viable operational S1 businesses with reciprocal demands or a returned inter-S1 balancing decision after ongoing mutual disturbance.
- Decision owner: Configured model principal chooses temporary assignments and the deterministic host enforces their boundaries. No dedicated continuing S2 owner independent of the individual task's plan emerges.
- Supporting / enforcement mechanisms: validatePlan, ownedPaths, task dependencies, role capacity Slots, candidate conflict detection, sequential application of audited Git proposals, restart/replan if a job fails.
- Closure path: One task goal → temporary work DAG/path partition and per-job capacity → completion/failure → plan repair or blocked. There is no cross-business interference signal → S2 negotiated binding coordination → operational policies returned to separately viable business units.
- Why this is / is not agent-owned: The strongest S2 candidate was explicitly considered: ownedPath conflict avoidance and dependency/capacity scheduling. Those manage collaboration among temporary agents within one coding operation; reviewer and executor are not independently enduring environmental/business units. Task-level shared-repository serialization is not by itself VSM S2.
- Evidence: [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs)
- Basis: bounded negative with explicit positive hypothesis evaluated
- Confidence: Medium-high at the declared single-operation recursion.
- Caveats: A different system-in-focus consisting of several enduring organizational services using this harness could show S2; such a mode/return path is not shipped here.

### Absence scope

- Surfaces inspected: Root/job graph and dependency orchestration, ownedPaths contract and validator, per-role slot pools, workspace branch/integration, job failure/repair and their store events.
- Plausible first-party paths checked: Checked independent status of executor roles and continuing units; task assignment and mutual path-conflict management; returned feedback and same-run replanning; normal supported user task and chat modes.
- Why no material first-party path remains: All competing workers are bounded pieces of one temporary user-defined coding operation. Their path disjointness and DAG rules do not close reciprocal disturbances among independently viable enduring S1 operations, so no material first-party S2 organizational return remains at this declared recursion.

## S3 — Inside-and-now management

- State: —
- Function: No sustained whole-organization present-control actor managing resources, current accountability and binding interventions across multiple continuing S1 operations.
- Disturbance / variety regulated: Different jobs need staffing and dependencies; audit failures, token budgets and integration conflicts require corrective intervention.
- Decisive decision or feedback right: Principal models do allocate job roles, dependencies and acceptance items across one user objective; host governs fixed role concurrency, budgets, verified aggregation and repair. But none is a continuing accountable management authority regulating independent operational businesses with ongoing resource policy and returned commitments.
- Decision owner: The model principal owns current **task** decomposition and final work-product arbitration. Operators own settings; the host owns enforcement. No function-specific continuing S3 management owner is wired.
- Supporting / enforcement mechanisms: Role configuration, active pools, root XState, persisted jobs and budgets, accepted-task set, final checks, user pause/resume and worktree single-writer gate.
- Closure path: Per-user objective → task graph and current round → workers' status / audited artifacts → principal replan and next task round or final output; not continuing S3 managerial portfolio/units → resource/intervention commitments → re-regulated autonomous businesses.
- Why this is / is not agent-owned: The source has unusually strong central planning, performance verification and adaptive reassignment. The decisive object nonetheless is satisfying a single commissioned software task, not managing organizational operations over time. A component called 主席位 (chair/principal) is not sufficient.
- Evidence: [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/settings.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/settings.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs)
- Basis: bounded negative after strongest manager-like path inspection
- Confidence: Medium-high, boundary-dependent.
- Caveats: Changing the recursion to a full agency with operating work cells could change classification; this code does not demonstrate that first-party organizational mode.

### Absence scope

- Surfaces inspected: Principal scoping/planning/repair/judging steps, root graph, role/capacity settings, job-status store, validation and publish gate.
- Plausible first-party paths checked: Tested S3 hypothesis that principal resource delegation + acceptance/repair is whole-current management, as well as operator parent intervention via pause/settings and host deterministic control.
- Why no material first-party path remains: These decisions are internal to a finite client task and are not tied to continuing independent S1 business units or a managerial accountability/resource-control and return path. Operator settings constrain the task but do not close a parent S3 organizational mode.

## S3* — Complementary audit

- State: —
- Function: No separate audit of an S3 managerial picture against unit field reality with findings returned for S3 corrective governance.
- Disturbance / variety regulated: Scouts or workers may hallucinate evidence, misstate tests or change code during reviewer inspection; errors could be hidden by a synthetic summary.
- Decisive decision or feedback right: The first-party auxiliary agents read independent files/evidence, evaluate frozen changes in separate worktrees and emit audit pass/fail; this is strong evidence-backed **task output verification**. The checked claims are scout findings and worker changes, not S3 management's accounting of whole operations.
- Decision owner: Auxiliary model auditors judge task evidence; principal and XState consume their verdict to allow/correct task output, not manage an organization through independent audit of management reporting.
- Supporting / enforcement mechanisms: Scout audit with independent evidence tools, job audit in separate worktree, mutation detection, typed schema, actual check commands, final host verification.
- Closure path: Scout/worker report and frozen candidate → independent audit pass/fail → exclude report, repair or integrate work → final acceptance; no ordinary S3 managerial report → complementary independent S3* evidence sampling → corrected managerial control of continuing S1 units.
- Why this is / is not agent-owned: Reviewer independence is genuine but audits operational task artifacts rather than a separate current S3 managerial account. Independence alone does not transform code QA into S3*.
- Evidence: [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs); [tests/workflow.test.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/tests/workflow.test.mjs)
- Basis: bounded negative with positive independent audit path assessed
- Confidence: High for audit scope in first-party source.
- Caveats: Tool may be useful for external organizational audits, but no first-party S3 target/report/closure is presented.

### Absence scope

- Surfaces inspected: Scout and job audit code, independent worktree and read-only review tools, typed reports, final principal judging, workspace mutation checks.
- Plausible first-party paths checked: Checked whether auditors bypass managerial self-report to sample direct operational evidence; identified actual report target and recipient and looked for S3 correction rights.
- Why no material first-party path remains: They independently inspect work-cell evidence and deliver verdicts for the same user software task; no ongoing managerial S3 report exists to be challenged and returned for organization-level correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: No adopted strategic response to a changing outside environment governing future viability of the deployed harness organization.
- Disturbance / variety regulated: Unknown packages, external research results, new workspace requirements or model/provider changes may affect the user's future code project.
- Decisive decision or feedback right: Scouts can fetch external URLs, run searches and summarize constraints; principal can form and revise technical plans. But these are scoped to an incoming user objective, with no standing S4 environmental agenda, long-range options and acceptance into the harness's continuing capability plan.
- Decision owner: Case-specified scouts/principal and user-selected model configuration; no separate strategic intelligence or legitimate parent adoption owner is shipped.
- Supporting / enforcement mechanisms: Research and web tools, typed evidence reporting, repair planning, project workspace exploration and model settings.
- Closure path: User objective → evidence for that task → present execution/replan/publish. No continual external intelligence → organizational future-capability options → decisive adoption → modified sustained host capability or management.
- Why this is / is not agent-owned: A feature with named reconnaissance or research only proves task investigation, not S4 outside-and-then function at this viable system boundary.
- Evidence: [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/research.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/research.mjs); [server/pi.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/pi.mjs); [server/settings.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/settings.mjs); [server/tools.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/tools.mjs)
- Basis: bounded negative
- Confidence: High.
- Caveats: An operator may learn and manually alter the repo later; no first-party strategy-adoption loop demonstrated.

### Absence scope

- Surfaces inspected: Reconnaissance/independent audit, research tools, role configuration, plan repair and final decision stages.
- Plausible first-party paths checked: Checked whether research targets the system's ongoing environment (rather than the input coding problem), and whether a model or legitimate parent accepts persistent future organizational strategy.
- Why no material first-party path remains: All exploration feeds the same commissioned task. No first-party standing outside/then management or accepted capability adaptation return exists.

## S5 — Policy and identity

- State: —
- Function: No constitutional purpose/identity-policy authority at the assessed coding-workflow recursion.
- Disturbance / variety regulated: Budget limits, security and file ownership, model access, stop requests, tool side-effect uncertainty and acceptance conflicts.
- Decisive decision or feedback right: Human operator chooses goals/credentials/budgets and can pause/stop; model principal sets a task plan and judges task criteria; deterministic host enforces safety/verification/no-unaudited-publication gates. No actor determines and returns decisions on ultimate mission identity or conflicts between organizational S3 and S4 mandates.
- Decision owner: External operator for configuration and task definition; first-party runtime enforces controls; no first-party S5 or demonstrated parent constitutional authority.
- Supporting / enforcement mechanisms: Configurable roles/model endpoints/slots, budget caps and effect ledger, path restrictions, publication locks, fail closed verification and deterministic mode switches.
- Closure path: Task instruction and hardcoded safety settings → model work + host checks → terminal status; no ultimate policy issue → legitimate identity owner decision → binding changed rule on future organizational operation.
- Why this is / is not agent-owned: A strict publish safety policy and user intervention protect outputs but are not the decisive organizational identity/purpose governance function.
- Evidence: [server/index.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/index.mjs); [server/workflow.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workflow.mjs); [server/settings.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/settings.mjs); [server/workspace.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/workspace.mjs); [server/tools.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/tools.mjs); [server/store.mjs](https://github.com/LEO001020/pi-loop-studio-orchestra/blob/0a6b65c63a0eb11f2e928e773de1774b2c7d5bd7/server/store.mjs)
- Basis: bounded negative after parent-mode analysis
- Confidence: High.
- Caveats: The owner's eventual change to project goals can occur through development outside this runtime; this is not an observed in-boundary parent-mode S5 cycle.

### Absence scope

- Surfaces inspected: Settings, server operator endpoints, workflow stop/resume, per-role permissions, tool/effect gate, original acceptance retention and single-writer publish.
- Plausible first-party paths checked: Checked prospective identity decisions in principal arbitration and human operator control, including whether policy deliberation reaches a legitimate parent and the returned decision changes governance of continuing operations.
- Why no material first-party path remains: All decisions bind a user job, its token/resource limits and publication safety; no first-party enduring organizational identity-policy decision and return channel exists.

## Distributed OSS parent arrangement

Public repository authors and users are external to the shipped local runtime's bounded operating system. A human setting roles, approving a goal or upgrading installed source code does not itself establish a first-party legitimate parent-manager or ultimate-policy adoption feedback loop. Parent-mode S3/S4/S5 hypotheses were checked against settings, stop/resume, principal orchestration and publish paths and did not close their distinct functions.

## Self-hosted and non-human modes

Local self-hosting and configurable principal/executor/auxiliary model endpoints are part of the supported distribution. A missing endpoint fails preflight rather than proving a model can operate without credentials. The host owns process control, persisted state and final file publishing while configured model agents own bounded case-dependent decisions. Role concurrency and tool enforcement do not automatically inherit model autonomy.

## Recursion

A single client's software task is the operative system-in-focus. Jobs are temporary role-specific work and inspections with bounded owned paths, dependencies and a shared ultimate acceptance standard, not several self-maintaining external businesses. The host may run multiple concurrent jobs but only commits an integrated verified outcome for that task. The larger user team could form a different viability boundary, but is not embedded as an operating mode.

## Variety and escalation

Partial scout failures, rejected audits, mutation during audit, ownership conflict, budget pauses and command failures change the persisted run state and may produce repair, a retry or an operator-visible blocked terminal state. The single-writer gate contains unsafe publication; effects whose outcomes are unknown halt tool progression. These operational evidence/failure paths should not be renamed S3*, S4, S5 or an algedonic governance signal without a distinct higher-recursion decision and returned correction.

## Evidence gaps

Code inspection is pinned to first-party commit and source tree and not conflated with the checked-in screenshots/verification dossiers. No configured live model endpoints were called, no user project was modified, and model cost/output quality was not evaluated. Node 24 and third-party runtime dependencies may be necessary for a live execution; local Index tests are evidence of assessment artifact consistency only. The bounded negative conclusions do not claim impossibility for hypothetical wider deployments.
