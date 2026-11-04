---
harness_id: opal
project_name: OPAL
repository: https://github.com/xingjian-bai/opal
review_ref: e999c21ee1a05891ea09d7d29bf2cd6597ca686b
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# OPAL

## Review boundary

- System in focus: One OPAL reactive-optimizer organization: the running updater/analysis capability, model-backed decision worker and wrapper that adopts its changes during a wrapped training run.
- Purpose and identity: Improve the optimizer used by an ongoing training job while preserving the operator-fixed model, data, loss and evaluation boundary.
- Relevant environment: The wrapped training workload, gradients and loss/validation dynamics, parameter structure, update latency, remaining horizon, external coding-agent backend availability and operator goal.
- Standard-distribution boundary: The installable opal wrapper, executable updater/analysis programs, decision worker, supported persistent Claude/Codex/mailbox integration, version adoption/recovery and optional evaluation-integrity/report surface. The assessment is of this concrete composed reactive optimizer, not the general coding CLI or the broader research campaign.
- Credited operating / distribution surfaces: [README.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/README.md); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py).
- Adjacent first-party surfaces excluded from ownership: Benchmark/example scores, paper/blog claims, example training datasets and downloaded weights, CI/tests, author research organization and external Claude/Codex internals. Tests corroborate wiring but do not supply runtime owners. KeepBackend is a non-agent dry-run baseline rather than the basis of S1/S4 A.
- First-party operating / deployment modes considered: Live agent-backed wrap with a persistent decision session; blocking/nonblocking decisions; single-process and supported DDP program adoption; mailbox agent transport; keep/callable test modes; optional validation=N with default-on integrity check; reports and operator notes.
- Recursion level: One adaptive optimizer organization around one training run. DDP ranks and parameter groups enact one logical training operation rather than independently viable S1 organizations. The same model-backed worker can exercise operational and prospective adaptation rights; no recursive VSM hierarchy is inferred.
- Reviewed revision: `e999c21ee1a05891ea09d7d29bf2cd6597ca686b`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The wrapper starts from the user optimizer and writes updater.py/analysis.py. AgentWorker exports the running programs, observed losses/reports, prior adoption/reversion results and horizon into a decision workspace; a supported backend continues one coding-agent conversation. The worker checks completed edits and syntax. wrapper._apply merges only changes relative to the shown base, builds/installs a version at an update boundary, propagates it across ranks and retains fallback/recovery state. The active updater directly transforms gradients into parameter updates; analysis can generate observations and wake a new decision. The neutral prompt explicitly requests observed numbers, an edited-or-kept choice, a falsifiable prediction and later comparison with that prediction. Runtime cost/schedule/precision checks constrain decisions. Separately, integrity.py samples actual parameter trajectories independently of generated analysis and flags temporary evaluation-time swaps to the operator-facing events/report.

Primary implementation: [README.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/README.md); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py).

## Operational model

S1 is the ongoing agent-assisted optimizer work cell, whose actor chooses executable update behavior under a fixed training goal. At this declared optimizer boundary, prospective redesign of the running updater/analysis from training-environment evidence also supplies a distinct S4 role: the option is installed into the organization's present operating capability and later evidence returns to the same decision actor. This is a within-run capability loop, not a claim of general self-improvement or evidence imported from the coding CLI. The integrity sampler is an audit-specific construction surface; it does not ship an autonomous investigating/correcting audit actor.

## S1 — Operations

- State: A
- Function: Carry out the training-optimizer task through model-chosen executable updater/analysis behavior.
- Disturbance / variety regulated: Loss/gradient dynamics, parameter roles, code failures and the operator's fixed training goal.
- Decisive decision or feedback right: Keep or edit updater/analysis programs and choose the corresponding next optimization behavior.
- Decision owner: The model-backed AgentWorker decision actor in supported live backends.
- Supporting / enforcement mechanisms: Persistent backend session, decision workspace, syntax/closure checks, program loader, update-boundary installation, DDP transport, trial snapshots and rollback.
- Closure path: Agent edits are collected from the workspace, checked, installed as active programs and executed on subsequent updates; actual outcomes/errors and adoption status are exported into later decisions.
- Boundary reachability: wrap instantiates the first-party worker/backend and supplies its prompt/workspace; _apply and _install make completed choices active. The repository owns the observation-to-decision-to-training organization even though a coding CLI supplies the actor runtime.
- Why this is / is not agent-owned: Removing the model leaves the unchanged starting optimizer or keep backend and deterministic safeguards; the discretionary program choices do not occur.
- Evidence: [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

## S2 — Coordination

- State: —
- Function: No separate S2 inter-operational-unit stabilization organization.
- Disturbance / variety regulated: Potential rank disagreement and stale asynchronous program answers.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: DDP synchronization, _agree/_check_ranks, one worker in flight and file-level base merge.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Ranks/parameter groups are replicas or parts of one logical training operation. Version agreement and stale-answer merge preserve one optimizer's consistency; they do not establish a regulator of interference among distinct autonomous S1 units.
- Evidence: [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/misc/ddp.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/ddp.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/README.md); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py).
- Plausible first-party paths checked: DDP agreement/broadcast, rank checks, one decision worker, file-level base merge, and parameter-group validation.
- Why no material first-party path remains: Ranks/parameter groups are replicas or parts of one logical training operation. Version agreement and stale-answer merge preserve one optimizer's consistency; they do not establish a regulator of interference among distinct autonomous S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No separately established whole-system current-control function at this recursion.
- Disturbance / variety regulated: Decision spending, waiting time, current training constraints and task failures.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: The operator selects fixed constraints; the agent owns bounded optimizer decisions.
- Supporting / enforcement mechanisms: _budget_left/_cost_reached, schedule/waiting policy, watchdog, program adoption and recovery.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: The model chooses local optimizer behavior; the wrapper enforces host-selected budget, horizon and safety rules. No whole-system organizational resource/commitment bargaining or intervention mandate is supplied. Parameter-wise learning rates remain task algorithm choices, not S3 merely because they allocate step sizes.
- Evidence: [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/schedule.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/schedule.py); [opal/misc/waiting.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/waiting.py); [opal/backends/base.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/base.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/README.md); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py).
- Plausible first-party paths checked: Cost/decision caps, blocking/nonblocking schedule, nonfinite-loss pause, trial recovery, operator notes and fixed workload boundaries.
- Why no material first-party path remains: The model chooses local optimizer behavior; the wrapper enforces host-selected budget, horizon and safety rules. No whole-system organizational resource/commitment bargaining or intervention mandate is supplied. Parameter-wise learning rates remain task algorithm choices, not S3 merely because they allocate step sizes.

## S3* — Complementary audit

- State: C
- Function: Provide complementary evidence challenging whether evaluation measurements reflect lasting training progress rather than temporary parameter substitution.
- Disturbance / variety regulated: An updater can move weights for a validation measurement and restore them afterward, misleading ordinary reported performance.
- Decisive decision or feedback right: Detect/report suspicious parameter round trips and enable an independently mandated reviewer/controller to judge their significance and corrective action.
- Decision owner: The shipped Integrity sampler/analyzer deterministically owns diagnostic flags; an autonomous investigating audit actor and corrective mandate still require composition.
- Supporting / enforcement mechanisms: Seeded tensor samples/ring buffers, validation-opened windows, versioned eval_integrity events, stderr warnings and HTML report banner.
- Closure path: Flags reach operator-facing events/report and direct the operator to inspect programs before trusting metrics. Automatic intervention and an autonomous review-to-control return are not shipped; this is the remaining constructor obligation.
- Boundary reachability: With validation=N, eval_integrity defaults on in the real wrapper. report_validation opens a window and per-update recording resolves it; report.integrity_flag consumes the resulting events. This is runtime code rather than only a test fixture.
- Why this is / is not agent-owned: The source supplies an audit-specific independent reality-access and diagnostic/report path, rather than a generic log hook. It does not supply agent-owned audit judgment or correction, so C rather than A is credited.
- Evidence: [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py); [tests/test_eval_integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/tests/test_eval_integrity.py).
- Basis: structural.
- Confidence: medium-high for the bounded constructor claim.
- Caveats: The agent is not told of the check, but generated Python is not proven unable to evade it. Flags do not stop/revert training; warnings alone are not completed autonomous audit closure.
- Claim being audited: That the observed validation performance describes the durably trained model produced by the active updater.
- Ordinary reporting path: Generated analysis reports and scalar validation measurements delivered to the optimization worker.
- Complementary access path: Wrapper-owned sampling of actual parameter entries before/after externally reported validation, independent of agent-written analysis.py.
- Independence boundary: The sampler and flag/report code are outside the generated programs and hidden from the agent prompt; test_the_agent_is_not_told corroborates the documented separation. This is bounded access separation, not a security proof.
- Who acts on findings: The operator is prompted to inspect saved programs. An application must compose an independent audit actor/authority and returned corrective control to close autonomous enactment.

## S4 — Outside-and-then intelligence

- State: A
- Function: Develop and adopt prospective optimizer/observation capability changes from the training environment.
- Disturbance / variety regulated: Changing loss/gradient behavior, validation-versus-training divergence, performance cost and the remaining future update horizon.
- Decisive decision or feedback right: Interpret the observed trajectory, form a predicted adaptation option, keep or rewrite the active optimizer/analysis, and revise that option after its consequences.
- Decision owner: The persistent model-backed decision worker owns the bounded adaptation choice; the operator fixes the larger training identity and constraints.
- Supporting / enforcement mechanisms: Training observations/inbox, versioned programs, syntax/build checks, _apply/_install, trial/fallback machinery and prior-outcome messages.
- Closure path: The prompt requires predicted effect and falsification timing; AgentWorker passes current evidence and prior outcomes to the model. Completed option files become the active updater/analysis at a boundary. Their subsequent training effects/reversions return in the next request and prediction comparison.
- Boundary reachability: This loop is wired by wrap/AgentWorker in the standard live backend mode; _submit exports losses/reports/horizon, _apply/_install execute adopted files, and format_message/previous_answer report consequences. No user-written adaptation controller or adjacent research agent is borrowed.
- Why this is / is not agent-owned: The runtime can enforce a cap or reject code, but cannot select the prospective algorithmic response without the model. The same actor may perform S1 work and S4 adaptation; implementation co-location does not erase the distinct environment-to-capability role.
- Evidence: [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py).
- Basis: structural.
- Confidence: medium-high at the declared optimizer-run boundary.
- Caveats: This is within-run adaptation of deployed optimizer capability. Merely writing code or updating memory would not suffice; the credited evidence includes explicit future prediction, executable adoption and subsequent environmental feedback. No empirical improvement or cross-task transfer is established.
- External distinction: Actual training-workload loss/gradient/validation and latency distinctions arrive from outside the optimizer decision cell; the operator-fixed model/data/loss are its environment.
- Future / prospective distinction: total_updates and remaining decisions constrain the horizon; the prompt requires a predicted effect, by when, and what would falsify it, then comparison with observed outcomes.
- Adaptation option generated: A kept or revised updater.py/analysis.py (and helper modules), changing the live update rule and/or the observation capability.
- Path back into current capability / S3: wrapper._apply checks/merges the option and _install replaces the active runtime objects; later updates use them and _submit returns their consequences. This is a capability-return path, without claiming a separately agent-owned S3.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy adjudication path established.
- Disturbance / variety regulated: Proposals to change training purpose, data/model/loss or permitted optimizer scope.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: Operator/developer own the initial training purpose and constraints; no first-party runtime S5 organization is supplied.
- Supporting / enforcement mechanisms: Static prompt/spec, backend workspace policy, code diagnostics and precision contracts.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: The operator defines the goal and immutable training boundaries in advance. Ordinary notes, cost approval and code boundary rules do not provide an identity-level issue referral, legitimate authoritative resolution and returned governance loop.
- Evidence: [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/boundary.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/boundary.py); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/README.md); [opal/wrapper.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/wrapper.py); [opal/agent.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/agent.py); [opal/programs.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/programs.py); [opal/prompts/neutral.md](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/prompts/neutral.md); [opal/backends/__init__.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/__init__.py); [opal/backends/claude.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/backends/claude.py); [opal/misc/integrity.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/misc/integrity.py); [opal/report.py](https://github.com/xingjian-bai/opal/blob/e999c21ee1a05891ea09d7d29bf2cd6597ca686b/opal/report.py).
- Plausible first-party paths checked: Fixed goal/spec, neutral prompt boundaries, protected workspace/control folders, operator notes and source-edit/precision restrictions.
- Why no material first-party path remains: The operator defines the goal and immutable training boundaries in advance. Ordinary notes, cost approval and code boundary rules do not provide an identity-level issue referral, legitimate authoritative resolution and returned governance loop.

## Distributed OSS parent arrangement

The upstream maintainer and contributors govern repository development. That adjacent organization is not a runtime parent mode of the assessed task harness. No function-specific returned organization-level S3/S4/S5 decision is credited merely from contributor activity.

## Self-hosted and non-human modes

The operator owns the goal, training script, model/data/loss, invocation permissions and cost/time limits. Notes can influence decisions but no function-specific parent-governance protocol is established. The agent-backed mode installs its own bounded updater options; the keep baseline makes no autonomous choices. Integrity reports ask the operator to inspect programs before trusting results; no automatic remediation or parent-mode symbol is inferred.

## Recursion

No recursive viable-system claim. Distributed tensor ranks, parameter groups and one persistent external coding session are implementation topology. The assessment does not treat a trained model, a dataset or the external CLI as a child viable organization.

## Variety and escalation

Load/syntax/precision/runtime failures can reject or revert a program and feed errors to the next decision; non-finite loss may pause for a decision. Budget/schedule and backend-unavailable policies stop further calls or wait. Integrity flags are persistent warnings, not an automatic training stop. Source explicitly documents incomplete rollback after later failing updates and the detector's bounded sampling window.

## Evidence gaps

No live Claude/Codex/mailbox call, training run or benchmark replication was executed. torch and pytest are absent, so the upstream CPU suite was not run; source and tests were inspected and Python files were parsed. S4 A is limited to the supported within-run optimizer capability adaptation, not cross-run knowledge transfer, empirical uplift or general agent evolution. S3* C does not assert an autonomous auditor, binding corrective action or tamper-proof isolation; operator/agent composition remains necessary. Integrity false positives/negatives and unsafe generated-program boundary crossings remain explicitly bounded by upstream source.
