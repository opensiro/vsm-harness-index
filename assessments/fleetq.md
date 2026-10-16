---
harness_id: fleetq
project_name: FleetQ
repository: https://github.com/escapeboy/agent-fleet-o
review_ref: d949ff4510548171b8a8648c794a7efd9d9d8c8c
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# FleetQ

## Review boundary

- System in focus: the shipped FleetQ Laravel PHP agent/crew platform at frozen `d949ff4510548171b8a8648c794a7efd9d9d8c8c`, **one configured crew** whose worker, coordinator and QA paths are first-party job/action logic, and available separate optional evaluation/evolution support on the *same managed agent/crew*.
- Purpose and identity: carry out model-backed multi-agent goal work, prevent duplicate concurrent task claims, manage current task delegation and bounded QA/capability changes, while keeping consequential policy, approval and ultimate human authority outside the autonomous crew agent.
- Relevant environment: configured team/tenant/crew agents, model gateway and provider responses, user goal, task/output ledger, team collaborators, curated eval cases, production run outcomes and human feedback, operator and quotas.
- Standard-distribution boundary: shipped `CrewOrchestrator`, `ExecuteCrewTaskJob`, `ExecuteAgentAction` and provider gateway; hierarchical `CoordinatorDecisionJob` mode, self-claim mode, QA model job and optional eval/config gate, post-execution feedback-driven evolution under an operator's approval. These are **mode-specific**; not all mechanisms execute in every crew.
- Credited operating / distribution surfaces: crew jobs/actions, work claim mutex, model-led coordinator, separate QA agent, opt-in eval dataset replay config gate, on-demand agent evolution and Livewire/MCP user approvals, persistent task and agent config state.
- Adjacent first-party surfaces excluded from ownership: FleetQ marketing claims and screenshots; `CLAUDE.md` contributor instructions and repository CI; future-only ideas; unrelated tenant/institutional governance, human project strategy outside app and independent inner organizational functions of Codex/Claude Code adapters and model providers.
- First-party operating / deployment modes considered: normal first-party model-backed crew workers; hierarchical coordinator-enabled crews; self-claim competition for pending tasks; separate crew QA and configured eval-gated candidate agent updates; user-authorized evolutionary modifications of stored agent prompt/personality. The preview/dogfood developer system is not credited.
- Recursion level: one FleetQ-managed crew with its first-party execution and capability-governance attachments. Agent calls are operational units, while current coordinator and complementary evaluation cover the crew; higher tenant-level policy/identity is not imported.
- Reviewed revision: `d949ff4510548171b8a8648c794a7efd9d9d8c8c`.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

FleetQ exposes first-party PHP execution paths rather than only a dashboard to third-party coding CLIs. `ExecuteCrewTaskJob` loads the assigned team agent, builds task/context and permitted tools, invokes first-party `ExecuteAgentAction`, and stores outputs/status and subsequent QA state. Provider inference is external, but the crew work/feedback loop and tool/credit control surfaces belong to FleetQ's configured platform ([app/Domain/Crew/Jobs/ExecuteCrewTaskJob.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Jobs/ExecuteCrewTaskJob.php), [app/Domain/Agent/Actions/ExecuteAgentAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/ExecuteAgentAction.php), [app/Domain/Crew/Services/CrewOrchestrator.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Services/CrewOrchestrator.php)).

**S2 is a narrow concurrency constructor.** In self-claim mode, `ClaimNextTaskAction` transactionally locks the next eligible pending task and atomically attributes it to exactly one agent, attenuating two distinct worker cells racing to execute the same task. This is a concrete inter-worker duplicate-claim disturbance and returned work-ownership effect, not merely having a queue. Separately, `ProjectScheduler` has skip/queue rules for overlapping scheduled *project runs*, but those belong to a wider project recursion and are not required here ([app/Domain/Crew/Actions/ClaimNextTaskAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Actions/ClaimNextTaskAction.php), [app/Domain/Project/Services/ProjectScheduler.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Project/Services/ProjectScheduler.php)).

**S3 is model-led in the optional hierarchical crew mode.** `CoordinatorDecisionJob` reads completed/failed/pending tasks, worker identities and current goal/iteration; it prompts the configured coordinator model to choose `delegate`, `complete` or, where available, `spawn_sub_experiment`, then first-party code applies that choice. This is whole-crew present-work judgment, not just a deterministic job scheduler. Bounded budget and kill-switch middleware enforce authorization but do not own the current resource judgment ([app/Domain/Crew/Jobs/CoordinatorDecisionJob.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Jobs/CoordinatorDecisionJob.php), [app/Domain/Crew/Services/CrewOrchestrator.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Services/CrewOrchestrator.php)).

**S3* is a conditional first-party complementary evaluation construction, not automatic QA promotion.** An ordinary QA agent `ValidateTaskOutputAction` receives a worker's task/output summary and can request retries, but a second model scoring that same producer output does not alone have independent ground-truth access. The **opt-in** `EvaluateAgentConfigGateAction` instead separately replays curated external evaluation cases against a *candidate* agent model/prompt, uses judge/criteria/threshold results, and its installed `AgentUpdateTool` **withholds** an otherwise authorized update on a failed gate. Replay and dataset supply distinct evidence from current self-reports. This is a constructor C; fail-open infrastructure errors and configured-disabled paths materially bound the claim ([app/Domain/Agent/Actions/EvaluateAgentConfigGateAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/EvaluateAgentConfigGateAction.php), [app/Domain/Evaluation/Actions/ReplayEvaluationDatasetAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evaluation/Actions/ReplayEvaluationDatasetAction.php), [app/Mcp/Tools/Agent/AgentUpdateTool.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Mcp/Tools/Agent/AgentUpdateTool.php)).

**S4 has a parent-governed prospective capability path**, not automatic autonomous promotion. First-party `AnalyzeExecutionForEvolutionAction` calls a model over real recent execution outcomes/failures to propose future role/goal/backstory/personality improvements. `AnalyzeAgentFeedbackAction` can incorporate negative user feedback and corrections. These options are saved as pending `EvolutionProposal`; the Livewire panel supports an explicit operator `approve` and `apply`, and `ApplyEvolutionProposalAction` refuses a proposal that is not approved before changing the actual agent configuration for later runs. The model generates options but the human owns the effectful future-adaptation decision: **S4=P**, not autonomous S4=A or combined A(P) ([app/Domain/Evolution/Actions/AnalyzeExecutionForEvolutionAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evolution/Actions/AnalyzeExecutionForEvolutionAction.php), [app/Domain/Agent/Actions/AnalyzeAgentFeedbackAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/AnalyzeAgentFeedbackAction.php), [app/Livewire/Evolution/EvolutionProposalPanel.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Livewire/Evolution/EvolutionProposalPanel.php), [app/Domain/Evolution/Actions/ApplyEvolutionProposalAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evolution/Actions/ApplyEvolutionProposalAction.php)).

Tenant/agent role and policy versions, approval modes and crew mission description are active enforcement or user configuration, but a distinct ultimate identity/ethos/whole-crew policy decision-and-return is not established merely from those controls ([app/Domain/Approval/Services/AgentPolicyResolver.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Approval/Services/AgentPolicyResolver.php), [app/Domain/Agent/Models/AgentPolicyVersion.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Models/AgentPolicyVersion.php), [app/Domain/Crew/Models/Crew.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Models/Crew.php)).

## Operational model

In a configured crew, first-party jobs instantiate model-backed worker operations with specific task and scoped tool rights. In self-claim mode the service atomically reserves a pending task for one worker, preventing duplicate claims. In hierarchical mode a coordinator model observes crew state and chooses current work delegation; ordinary QA can return rejection/repair. Separately, optional replay against curated cases can hold a proposed agent configuration update before it lands, and the operator may analyze logged execution/user feedback and approve a changed agent goal/personality for subsequent work. No live provider-backed execution, production monitoring or actual team run was witnessed in this source-based review.

## S1 — Operations

- State: A
- Function: complete bounded assigned crew tasks via model-driven and tool-bearing operational work units.
- Disturbance / variety regulated: goal ambiguity, tool outputs, task-specific information/operation demands and errors.
- Decisive decision or feedback right: choose contextual model responses and tools/steps to satisfy assigned tasks within agent/crew constraints.
- Decision owner: model-backed agent instantiated through first-party FleetQ `ExecuteAgentAction` within a registered crew, not unbounded vendor-specific orchestration.
- Supporting / enforcement mechanisms: job queue, crew roster and tool allowances, provider gateway, result persistence, budget/middleware, retry.
- Closure path: worker task and approved tool context → model-led operation and environment replies → first-party result/outcome persistence → crew workflow.
- Boundary reachability: `ExecuteCrewTaskJob` concretely calls first-party `ExecuteAgentAction` as a shipped job; live provider credentials and queue workers required.
- Why this is / is not agent-owned: worker model actually selects work behavior, while task/queue/config merely structures it.
- Evidence: [app/Domain/Crew/Jobs/ExecuteCrewTaskJob.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Jobs/ExecuteCrewTaskJob.php); [app/Domain/Agent/Actions/ExecuteAgentAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/ExecuteAgentAction.php).
- Basis: installed source and configured model operations.
- Confidence: medium-high in implementation boundary, not provider task success.
- Caveats: no external model behavior is claimed as observed performance.

## S2 — Coordination

- State: C
- Function: attenuate double-claim competition for one pending crew task among independent self-claim workers.
- Disturbance / variety regulated: two concurrent agent cells might both claim/run the same pending task and duplicate or corrupt attribution and work effects.
- Decisive decision or feedback right: atomically reserve the task for one agent and expose its changed assigned state to subsequent work selection.
- Decision owner: first-party transactional claim constructor enforcing the self-claim mode's work custody rule; not a discretionary peer negotiator.
- Supporting / enforcement mechanisms: `DB::transaction`, `lockForUpdate`, status filter `Pending`, `Assigned` status update and attributed `agent_id`.
- Closure path: concurrent claimant workers → one database row lock / pending predicate → one assigned worker, other no longer finds pending row → later work/claims follow updated occupancy.
- Boundary reachability: first-party `ClaimNextTaskAction` in configured self-claim crew mode; ordinary serial/hierarchical modes need not execute it.
- Why this is / is not agent-owned: deterministic arbitration protects concurrent sibling operations against a specific duplicate-work disturbance; generic queueing alone would not.
- Distinct S1 units: independent members of the self-claim crew independently asking for pending work.
- Inter-S1 disturbance: both might execute the same task because of concurrent reads of unclaimed work.
- Attenuating coordination relation: pessimistic locked database transaction selecting and assigning one pending row.
- Feedback into subsequent S1 behaviour: losing claimant's later selection sees changed status and has to claim other work or idle.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: enforced exclusive work reservation protects competing S1 decisions, directly changing which worker may act.
- Evidence: [app/Domain/Crew/Actions/ClaimNextTaskAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Actions/ClaimNextTaskAction.php); [app/Domain/Crew/Services/CrewOrchestrator.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Services/CrewOrchestrator.php).
- Basis: source-visible atomic claim.
- Confidence: high for bounded structural prevention of double claims.
- Caveats: does not ensure agents never create conflicting artifacts across different tasks.

## S3 — Inside-and-now control

- State: A
- Function: select and regulate live crew-wide work commitments and task ownership.
- Disturbance / variety regulated: completed/failed/pending tasks, available specialists, bounded budget and need for replanning.
- Decisive decision or feedback right: model coordinator chooses `delegate/complete`, assigned worker, next bounded task and, for experiment-linked crews, spawning subordinate experiment capacity.
- Decision owner: configured model-backed coordinator agent, whose response is parsed and applied by first-party `CoordinatorDecisionJob`; middleware is enforcement, not owner.
- Supporting / enforcement mechanisms: stored `CrewExecution`, task status/outputs, `AiGatewayInterface`, `createAndDispatchTask`, first-party orchestrator and worker jobs.
- Closure path: current crew completion/pending task view → model chooses next portfolio action → job creates/dispatches task or closes goal → changed task state and future coordinator iterations use updated current frontier.
- Boundary reachability: hierarchical crew mode's `CrewOrchestrator` dispatches coordinator jobs; no claim that every crew process type uses the autonomous coordinator.
- Why this is / is not agent-owned: removing the model coordinator leaves only static process dispatch, not its context-dependent choice of whole-crew commitments.
- Whole-system current view: current crew goal, configured workers, pending and completed/QA-failed task inventory, associated outputs and iteration count.
- Current-control decision scope: selecting work assignments, new delegated task generation and closure at the crew recursion, not tenant-global authority.
- Evidence: [app/Domain/Crew/Jobs/CoordinatorDecisionJob.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Jobs/CoordinatorDecisionJob.php); [app/Domain/Crew/Services/CrewOrchestrator.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Services/CrewOrchestrator.php).
- Basis: executable model-backed whole-current selection.
- Confidence: medium-high within hierarchical mode.
- Caveats: no observed live coordinator decision or evidence of full company-level management autonomy.

## S3* — Complementary audit

- State: C
- Function: construct a separate, dataset-grounded replay/score challenge to candidate agent capability/configuration claims and return that evidence as a gate on subsequent changes.
- Disturbance / variety regulated: model/prompt regression that would be missed by current worker self-reports or success-status summaries.
- Decisive decision or feedback right: compare candidate agent responses against distinct eval cases and configured criteria, calculate threshold score and hold the candidate config update when below threshold.
- Decision owner: first-party evaluation replay and configured deterministic gate (C), with a separate LLM judge supplying scored evaluation in the constructed path; no independent evidence of company-wide auditor S3*=A.
- Supporting / enforcement mechanisms: `ReplayEvaluationDatasetAction`, `LlmJudge`, separate cases/expected outputs, `EvaluateAgentConfigGateAction`, MCP agent update refusal.
- Closure path: proposed agent config → replay curated dataset separately against candidate → independent evaluator and threshold → nonpassing verdict → `AgentUpdateTool` returns held and *does not apply candidate*, altering future agent operations.
- Boundary reachability: opt-in `agent.eval_gate.enabled` + configured dataset ID, wired into shipped MCP `agent_update` path. It is not an unconditional gate on every role/config API.
- Why this is / is not agent-owned: constructor captures independently curated examples and enforces them beyond routine task output QA; structured LLM judge output is a component, not proof of independently managed first-party auditor ownership.
- Claim being audited: candidate prompt/model/agent configuration is safe enough to replace current operational capability.
- Ordinary reporting path: worker task status/output, QA self-report feedback and aggregate crew summary.
- Complementary access path: separately curated expected eval cases, re-execution against proposed config and independent scoring.
- Independence boundary: dataset cases are not the producer's own completion message, and are rerun on the candidate, though judge/model independence and dataset coverage are not guaranteed.
- Who acts on findings: candidate update MCP tool holds a below-threshold configuration change before it mutates persisted agent settings; operator can investigate/modify.
- Evidence: [app/Domain/Evaluation/Actions/ReplayEvaluationDatasetAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evaluation/Actions/ReplayEvaluationDatasetAction.php); [app/Domain/Agent/Actions/EvaluateAgentConfigGateAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/EvaluateAgentConfigGateAction.php); [app/Mcp/Tools/Agent/AgentUpdateTool.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Mcp/Tools/Agent/AgentUpdateTool.php); [app/Domain/Evaluation/Services/LlmJudge.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evaluation/Services/LlmJudge.php); [app/Domain/Crew/Actions/ValidateTaskOutputAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Actions/ValidateTaskOutputAction.php).
- Basis: configured executed first-party comparator/return constructor.
- Confidence: medium-high only in enabled gate with available dataset.
- Caveats: infra failure is **fail-open**, and current ordinary QA consumes producer-provided output; neither implies universal successful independent verification of tasks.

## S4 — Outside-and-then intelligence

- State: P
- Function: parent-governed future improvement of an agent's working role/personality based on execution history and optional actual user feedback.
- Disturbance / variety regulated: recurring task failures, feedback and future behavior/capability mismatch after environmental use.
- Decisive decision or feedback right: human operator authorizes/refuses a proposed change to future agent config; model analyzes external performance evidence and proposes options, but cannot cause the effectful promotion without approval.
- Decision owner: human maintainer/operator using the shipped EvolutionProposal approval/apply UI or equivalent MCP/API process.
- Supporting / enforcement mechanisms: model-proposed `EvolutionProposal`, recent execution logs/negative feedback, Livewire panel `approve/apply`, `ApplyEvolutionProposalAction` approved-status gate.
- Closure path: past runs/negative user feedback → model suggests changed goals/backstory/personality intended to improve later capability → legitimate user approves and applies → persisted managed agent context changes for subsequent executions.
- Boundary reachability: `EvolutionProposalPanel.analyze/approve/apply` and `ApplyEvolutionProposalAction` are shipped; this is an explicit user-driven optional mode, not automatic evolution.
- Why this is / is not agent-owned: the agent proposes, but model suggestions are insufficient to enact future organizational adaptation. Human selection is the decisive authority, hence P, not A or A(P).
- External distinction: failures and feedback from actual crew executions, including user correction/negative ratings, are not merely self-authored future tasks.
- Future / prospective distinction: proposes modifications to reusable agent goal/backstory/personality for later runs, not merely completing the current prompt.
- Adaptation option generated: model-generated structured proposed_changes saved with rationale and confidence for an agent.
- Path back into current capability / S3: explicit human approved/applied update persists new agent configuration subsequently used by the crew.
- Evidence: [app/Domain/Agent/Actions/AnalyzeAgentFeedbackAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Actions/AnalyzeAgentFeedbackAction.php); [app/Domain/Evolution/Actions/AnalyzeExecutionForEvolutionAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evolution/Actions/AnalyzeExecutionForEvolutionAction.php); [app/Livewire/Evolution/EvolutionProposalPanel.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Livewire/Evolution/EvolutionProposalPanel.php); [app/Domain/Evolution/Actions/ApplyEvolutionProposalAction.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Evolution/Actions/ApplyEvolutionProposalAction.php).
- Basis: shipped model-assisted, parent-owned option selection and persisted effect.
- Confidence: medium in parent-mode closure, not improvement efficacy.
- Caveats: the negative-feedback analyzer may require at least three qualifying ratings, and new proposals require deliberate parent authorization.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct legitimate identity/ethos/ultimate-policy decision path with subsequent whole-crew normative closure is established by the inspected first-party controls.
- Disturbance / variety regulated: fundamental team identity/mandate, ethical principles and unresolved tensions between present crew delivery and prospective adaptation.
- Decisive decision or feedback right: an ultimate-policy/identity question brought to legitimate authority and returned as an organization-level governing decision — absent as a distinct function-specific path in reviewed modes.
- Decision owner: humans configure the team, agent/tool policies and permission approvals, but the evidence does not show this as an actual recurring ultimate-policy settlement.
- Supporting / enforcement mechanisms: per-agent policies, tool-risk approval, tenancy and role access, constraints, kill switch and versioned execution policy.
- Closure path: existing policy is executed on actions and can be edited by users, yet no policy-identity issue → ultimate authority choice → governing return channel is identified beyond operational safety controls.
- Boundary reachability: shipped agent/approval policy and crew identity configuration inspected; this is not a claim that a deploying organization lacks S5 outside FleetQ.
- Why this is / is not agent-owned: names, permissions, tenant roles and risk approvals do not autonomously regulate ultimate identity. P is not warranted by ordinary approval alone.
- Evidence: [app/Domain/Approval/Services/AgentPolicyResolver.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Approval/Services/AgentPolicyResolver.php); [app/Domain/Approval/Services/PolicyEvaluator.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Approval/Services/PolicyEvaluator.php); [app/Domain/Agent/Models/AgentPolicyVersion.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Agent/Models/AgentPolicyVersion.php); [app/Domain/Crew/Models/Crew.php](https://github.com/escapeboy/agent-fleet-o/blob/d949ff4510548171b8a8648c794a7efd9d9d8c8c/app/Domain/Crew/Models/Crew.php).
- Basis: bounded negative after checking plausible shipped policy/identity surfaces.
- Confidence: medium-high for reviewed recursion and modes.
- Caveats: wider tenant/company policy authority is outside the declared crew.

### Absence scope

- Surfaces inspected: team/crew mission and agent role fields, risk/approval actions and policy versions, user edits, workflow authorization, capability evolution.
- Plausible first-party paths checked: binding agent policy, team mission configuration, high-risk approval, organizational adaptation tension and parent-authorized model/prompt changes.
- Why no material first-party path remains: controls set constraints for agent execution and approvals of operations/config; they do not expose a distinct ultimate identity/ethos policy issue and subsequent whole-crew governing settlement at the assessed level.

## Evidence gaps

- All positive mappings are **code-path/source-first** at frozen SHA, not observed external model runs, user decision traces or production efficacy.
- The configured modes are not simultaneous defaults: hierarchical model S3, self-claim S2, dataset-gated S3* and parent evolution S4 require their own setup; aggregate vector is a supported-mode composite, not one witnessed deployment.
- Independent replay S3* does not guarantee a trusted oracle on all tasks; optional config gate is fail-open on infrastructure errors. Ordinary crew QA sees mainly producer task/output, not raw independent code evidence.
- S4 results are parent-approved proposal *capabilities*, not autonomous skill evolution evidence or measured gains.
- Repository CI, development contributions and model-provider internals were not counted as first-party VSM proof.

## Conclusion

**Proposed general assessment, not canonical.** In supported separately configured FleetQ modes: `S1=A / S2=C / S3=A / S3*=C / S4=P / S5=—`. First-party model-backed worker operations close S1; exclusive self-claim prevents conflicting sibling task assignments (S2=C); the hierarchical model coordinator allocates whole-crew current work (S3=A); a separate optional dataset replay gate can hold risky candidate agent config changes using independent evidence (S3*=C); a human decides effectful future agent capability adaptation based on performance feedback (S4=P). Risk/approval and policy infrastructure do not alone establish ultimate identity S5. This mapping does not imply all modes active simultaneously or verified real-world outcomes.
