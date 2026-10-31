---
harness_id: agentworks
project_name: AgentWorks
repository: https://github.com/manishiitg/agentworks
review_ref: 5d53bfbb1541567fe3cb40b6a1a54197f2676fdc
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: C
autonomy_s4: A(P)
autonomy_s5: —
---

# AgentWorks

## Review boundary

- System in focus: the installed AgentWorks local/self-hosted workflow-agent organization, its runtime, workflow/crew execution, post-run Pulse lifecycle, durable evidence and operator-facing decision returns.
- Purpose and identity: execute user-defined goal-directed workflows and maintain their operational reliability, run evidence and improvement feedback over time.
- Relevant environment: user tasks and goals, tool/provider endpoints, repositories, workspace state, shared execution capacity, runtime failures, costs, changing requirements and operator oversight.
- Standard-distribution boundary: repository-owned Go server, workflow/crew scheduler and runtime, persisted workflow state, shipped Workshop agent guidance, Pulse module worklist/receipts, desktop/web operational UI and supported human decision tools.
- Credited operating / distribution surfaces: `agent_go/cmd/server/scheduler.go`, `crew_step_runner.go`, `pulse_worklist.go`, `pulse_review_tools.go`, `workflow_execution_tracker.go`, first-party workflow runners and shipped user-facing workflow/Pulse guidance.
- Adjacent first-party surfaces excluded from ownership: Go test/E2E fixtures, CI/release scripts, demo/example-only blueprints, roadmap proposals and this repository's contributor organization. External Claude Code/Codex/Pi model-and-tool loops, MCP servers, cloud models, external browser and channel services are not donated to AgentWorks.
- First-party operating / deployment modes considered: workflow-agent and crew execution, scheduled and manually triggered runs, full versus basic Pulse, optional specialist review and human approval/proposal flows, dashboard/notification operator mode; no actual paid provider run was executed.
- Recursion level: one operator-managed set of workflow/crew operating cells in an AgentWorks installation. A single worker's agent/tool loop is lower recursion; upstream project governance is adjacent.
- Reviewed revision: `manishiitg/agentworks@5d53bfbb1541567fe3cb40b6a1a54197f2676fdc`, identical GitHub repository ID 1075906855 to historical intake `manishiitg/coding-agent-loop` (#201 row 2), controller #2502.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/README.md) describes workflows with model/tool execution, crew steps, scheduling, durable runs, a Pulse post-run steward, goal-oriented improvement and human feedback. This is not a native model provider: it composes first-party execution and decision contracts with local or external inference/agent runtimes. [Workflow executor/crew runner](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/crew_step_runner.go) supplies stable per-step delivery identities, trigger dispatch and terminal-result polling. [Scheduler](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/scheduler.go) dispatches agent turns and a post-run Pulse lifecycle in the same retained session, validates due-worklist/receipt completion, and persists partial/recovery states rather than inferring success from prose. [Pulse design](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/pulse_consolidation.md) separates Gate evidence intake, perspective-specific review, bounded fixing, durable SQLite finding/verification state, finalization and operator decisions. [Reporting overview](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/self_improvement_and_reporting.md) links workflow health/goal outcomes with dashboard, notifications and proposal-only consequential changes. Source and design text were compared: the current scheduler uses successive selected review modules in one continuing session, not an automatically independent multi-agent audit organization.

## Operational model

Workflow agents and crew execution cells perform work; AgentWorks owns task/run handoff, receipt persistence, constraints, retry/idempotence and review/update prompts. Pulse's model-driven steward can choose due reviews and bounded repairs while Go enforces trusted execution/session and database integrity. Human approval is a separate decision owner for material strategy/goal changes; a dashboard or fixed enforcement mechanism is not credited with autonomous discretionary control. Multiple workers and operator-defined goals alone do not prove S2, S3 or S5. Both the native actor and first-party return path must be present for an ownership claim.

## S1 — Operations

- State: A
- Function: produce workflow/crew task outcomes and correct bounded operational failures through shipped model-driven action/tool turns.
- Disturbance / variety regulated: heterogeneous incoming tasks, tool execution results, provider changes, partial runs, errors and varying workflow context.
- Decisive decision or feedback right: the model-driven workflow/crew actor selects substantive task actions and, in Pulse's allowed repair scope, chooses corrective steps from run evidence.
- Decision owner: the first-party instantiated workflow/Pulse agent at the task-cell boundary; user specifies goals and external models/tools execute supplied requests.
- Supporting / enforcement mechanisms: schedule/trigger transport, workspace permissions, session/run identity, crew dispatch, tool APIs, durable SQLite, retry/timeout and receipt validators.
- Closure path: configured workflow input → runtime agent/tool turn or crew dispatch → artifacts and terminal run evidence → subsequent agent/Pulse decision or returned result to the requesting workflow.
- Boundary reachability: the supported scheduler invokes the agent session through `startSessionInternal` and the crew step runner dispatches first-party configured crew triggers with a polled terminal result; neither is only a development example.
- Why this is / is not agent-owned: the discretionary task content and repair selection are model-agent choices; removing that actor leaves transport/enforcement but no equivalent autonomous semantic task resolution.
- Evidence: [README](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/README.md); [scheduler.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/scheduler.go); [crew_step_runner.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/crew_step_runner.go); [workflow.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/workflow.go).
- Basis: structural
- Confidence: medium
- Caveats: shipped first-party composition, not an observed native model/provider E2E success. External coding CLIs retain their own internal agent loops and are not treated as AgentWorks-owned mechanisms.

## S2 — Coordination

- State: C
- Function: attenuate interference between separately dispatched crew cells/retries that otherwise reuse one workflow run's delivery/result boundary.
- Distinct S1 units: separately configured crew/worker cells and repeated attempted deliveries of a workflow step operating against the shared run/task state.
- Inter-S1 disturbance: duplicate dispatch of an already live/successful step, cross-group result adoption when a workflow folder is reused, and conflicting outcomes from replayed crew triggers.
- Attenuating coordination relation: the first-party runner uses immutable execution identity plus group/step/trigger/destination in a delivery key, adopts existing live/successful deliveries, explicitly retries only failed terminal outcomes, and keeps group delivery results isolated.
- Feedback into subsequent S1 behaviour: the crew step polls an existing/accepted terminal outcome and returns it to the invoking workflow step; the caller then advances or errors rather than launching a competing duplicate actor.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is an explicit collision/retry interference contract for parallel/repeated crew operations sharing one execution identity, not merely a mailbox or DAG.
- Disturbance / variety regulated: duplicated or misattributed crew work and inconsistent shared run completion.
- Decisive decision or feedback right: resolve which crew execution is authoritative for a specific task/group and feed that resolution back into subsequent step execution.
- Decision owner: a first-party deterministic workflow-specific coordination primitive; task/crew configuration and broader autonomous multi-unit regulation still require composition by the workflow developer/operator.
- Supporting / enforcement mechanisms: delivery keys, user-scoped trigger permissions, terminal polling and execution ID persistence.
- Closure path: attempted crew delivery → conflict/adoption check → existing or new run terminal status → result/error returned to the workflow step.
- Boundary reachability: `RunCrewStep` is a server-owned runner bound on ordinary UI, Builder, scheduled, webhook and workshop workflow paths; dedicated tests cover groups, duplicates, retries and run-folder reuse.
- Why this is / is not agent-owned: this narrowly evidenced S2-specific contract is not an autonomous coordination judgment over all conflicting S1 units; the deterministic key and composer-selected groups justify a constructor `C`, not `A`.
- Evidence: [crew_step_runner.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/crew_step_runner.go); [crew_step_runner_test.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/crew_step_runner_test.go); [sub-agent delegation guide](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/multiagent/sub_agent_delegation.md).
- Basis: structural
- Confidence: medium-low
- Caveats: scope is collision attenuation in crew-step operations, not proof that simple delegation, sequential steps or all concurrent workflow cells receive organization-wide S2 regulation.

## S3 — Inside-and-now control

- State: ?
- Function: proposed cross-workflow current-status, goal/cost and operational-exception supervision; the evidence does not establish a complete decisive whole-installation control/return owner.
- Disturbance / variety regulated: concurrent workflow health failures, cross-workflow cost/goal exceptions and resource/commitment conflicts.
- Decisive decision or feedback right: prioritize current installation-wide interventions or reallocate commitments using a whole-system view.
- Decision owner: operator and/or Chief-of-Staff proposal agent are described, but the exact shipped decision path versus dashboard/reporting support remains insufficiently verified.
- Supporting / enforcement mechanisms: run and cost ledgers, Org cards, Pulse verdicts, notification channels, configured budget/permission gates.
- Closure path: per-workflow evidence is surfaced through dashboard and proposals; an authoritative cross-workflow decision returned to reallocate live work is not unambiguously closed by the inspected first-party shipped path.
- Why this is / is not agent-owned: a health dashboard, scheduled reporting and bounded per-workflow fixers do not themselves own discretionary whole-system current control. The README/design describes an Org Pulse path, while source includes notices that an additional Chief-of-Staff product branch is unmerged.
- Evidence: [self-improvement and reporting](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/self_improvement_and_reporting.md); [scheduler.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/scheduler.go); [server.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/server.go).
- Basis: structural
- Confidence: low
- Caveats: a concrete supported parent-governed S3 current-control feedback loop remains the unresolved shipped path, not a hypothetical feature request. Do not infer S3 from a scheduler or cost enforcement alone.

## S3* — Complementary audit

- State: C
- Function: challenge workflow self-reports and remediation claims through an evidence-specific review-and-verification path before declaring an outcome fixed.
- Claim being audited: a workflow ran correctly, achieved its declared goal, and a proposed fix passed a real subsequent run/evaluation.
- Ordinary reporting path: the workflow writes run outcome, artifacts, summaries and status; the scheduler retains its run evidence.
- Complementary access path: Pulse's typed review finding, verification and worklist paths inspect run/eval/report/KB evidence and record failed, inconclusive or passed checks in SQLite rather than accepting final-answer prose.
- Independence boundary: perspective-specific reviewers and optional delegated specialists can inspect evidence separately, but current Pulse resumes the **same** workflow conversation and permits one owning agent to consolidate; mandatory materially independent challenge is not established for all normal runs.
- Who acts on findings: the Pulse Review+Fix actor may apply bounded repairs, pending user decisions handle material changes; scheduler validates terminal receipts and preserves missing-review recovery state.
- Disturbance / variety regulated: incorrect self-reported success, unverified repair claims, stale artifacts and missing evidence.
- Decisive decision or feedback right: issue an evidence-backed contrary review/verification result and require the workflow/fixer to follow it before closure.
- Decision owner: packaged review and verification agent/tool path; composing an independent specialist and accountable corrective return is supported, but not inherently closed for all default workflows.
- Supporting / enforcement mechanisms: trusted session registry, SQLite lifecycle tables, typed findings/verification tools, terminal receipt validator and scheduler turn ordering.
- Closure path: run evidence → due review/findings → bounded Fixer or pending approval → later producing run/evaluation verification → recorded closed/reopened/inconclusive finding and later workflow/Pulse behavior.
- Boundary reachability: `runPulseLifecycle`, typed worklist/result guards and module execution are shipped in the normal server; optional specialist compositions use product-supported delegation.
- Why this is / is not agent-owned: a distinct audit-specific evidence path exists; default same-session reviewer identity and deterministic receipt enforcement are insufficient for `A` independence, so the supported constructor is credited narrowly as `C`.
- Evidence: [pulse_consolidation.md](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/pulse_consolidation.md); [scheduler.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/scheduler.go); [pulse_worklist.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/pulse_worklist.go); [pulse_review_tools_test.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/pulse_review_tools_test.go).
- Basis: structural
- Confidence: medium-low
- Caveats: verification against a later producing run is stronger than parsing a textual QA verdict, but independent decision ownership remains conditional on actual specialist composition.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: reassess future workflow effectiveness against goals/changed evidence and adapt the operating strategy, while retaining a separate parent approval mode for consequential changes.
- External distinction: goal progress, evolving task evidence, model cost/tier trends, report/evaluation quality and updated external knowledge/requirements compared with earlier runs.
- Future / prospective distinction: a working implementation can still be off-goal; stale assumptions or an ineffective strategy will harm later workflow capability even when current runs complete.
- Adaptation option generated: `strategy_auditor`/`goal_advisor` recommend changed approach; technical/knowledge reviewers propose refreshed reports, learning and tools; bounded repairs can be selected and applied by the agent.
- Path back into current capability / S3: accepted safe fixes alter workflow artifacts/knowledge/steps and subsequent producing runs verify impact; material strategy/goal proposals enter an approve/reject/defer user decision and later approved workflow configuration.
- Disturbance / variety regulated: changing goals/evidence, strategy ineffectiveness, knowledge decay and mismatch between current workflow behavior and future desired outcome.
- Decisive decision or feedback right: select bounded safe prospective workflow improvements autonomously; separately approve or reject consequential strategy/goal changes under legitimate user authority.
- Decision owner: model-driven Pulse Review+Fix agent for bounded autonomous improvements; installation user/operator for material strategy or goal changes in the parent mode.
- Supporting / enforcement mechanisms: Gate due-worklist, typed pending decisions, impact ledger, freshness stamps, backup/publish and verified change receipts.
- Closure path: cross-run/external evidence → reviewer/Goal Advisor options → bounded agent fix or user approval → changed workflow/knowledge/plan → later run/eval/impact feedback.
- Boundary reachability: the normal post-run scheduler resumes the first-party workflow session for due reviewing/fixing, and shipped pending-decision tools/Workflow UI expose approval return for material changes.
- Why this is / is not agent-owned: in the base mode the model-driven actor chooses adaptive fixes, not the scheduler's fixed cadence. In the distinct parent mode, the user retains the consequential adaptation choice and its result is returned into workflow operation; these are alternative rights, not simultaneous owners.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Pulse agent within bounded safe-fix envelope | New run/goal evidence and due review | Selected fix/knowledge update → subsequent producing run/verification | `scheduler.go`, `pulse_consolidation.md` |
| Parent (`P`) | Local installation user/operator | Material strategy/goal proposal | Approve/reject/defer decision → approved workflow revision/next run | `pulse_consolidation.md`, `self_improvement_and_reporting.md` |

- Evidence: [pulse_consolidation.md](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/pulse_consolidation.md); [self_improvement_and_reporting.md](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/self_improvement_and_reporting.md); [scheduler.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/scheduler.go); [pulse_worklist.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/pulse_worklist.go).
- Basis: structural
- Confidence: medium
- Caveats: documented/implemented feedback paths are reviewed structurally, not tested with live model/provider; no causal empirical improvement claim is made. The parent mode is specific to material workflow adaptation, not general human approval.

## S5 — Policy and identity

- State: —
- Function: no first-party unresolved ultimate-identity or whole-organization policy adjudication/return loop established at this installation boundary.
- Disturbance / variety regulated: goal configuration, workspace permissions, provider constraints, run approvals and operational user preferences were checked as plausible but non-qualifying paths.
- Decisive decision or feedback right: no qualifying runtime identity/ultimate-policy right exposed beyond ordinary parent authoring or local policy enforcement.
- Decision owner: operators configure goals and permissions; Go enforces settings and agents perform tasks, but no organizational S5 decision process is evidenced.
- Supporting / enforcement mechanisms: fixed auth/workspace/folder policies, approval tools, goal scorecards and user config surfaces.
- Closure path: ordinary config/approval changes constrain later execution; this is not a reconstructable unresolved identity matter → legitimate ultimate authority → authoritative identity-policy decision → returned operation loop.
- Why this is / is not agent-owned: prompt identity, role/goal labels, safety policy and approval workflows are not evidence of decisive S5 ownership.
- Evidence: [README](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/README.md); [human feedback system](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/docs/workflow/human_feedback_system.md); [server.go](https://github.com/manishiitg/agentworks/blob/5d53bfbb1541567fe3cb40b6a1a54197f2676fdc/agent_go/cmd/server/server.go).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded standard-distribution absence, not a universal statement about operator institutions or future deployments.

### Absence scope

- Surfaces inspected: README, workflow/Pulse design, human-feedback workflow documentation, server/workspace permission paths, scheduler and relevant first-party implementation/tests at the pinned revision.
- Plausible first-party paths checked: org goal ownership, user approvals for consequential strategy changes, locked provider/permission settings, budget/schedule constraints, project contributor governance.
- Why no material first-party path remains: these paths either set operational objectives, approve an S4 proposal or enforce preselected constraints. None supplies a distinct in-boundary ultimate-identity or policy conflict adjudicator with authoritative return into subsequent system governance.

## Distributed OSS parent arrangement

The parent path credited for S4 is the local installation operator's approval of material strategy changes. It is not inferred from independent GitHub contributors, release maintainers, or the repository's own governance. No organization-level S3 or S5 ownership is borrowed from those adjacent arrangements.

## Self-hosted and non-human modes

The assessed modes are the shipped self-hosted/desktop runtime and its scheduled/manual workflow composition. External CLI agents, cloud LLMs and channel services remain outside; user approvals are credited only where a specific returned S4 decision is documented. No agent-owned ultimate policy is inferred.

## Recursion

Workflow/crew cells form lower operational units inside one installation. Delegation to a child actor is not itself a viable recursive subsystem; the narrow S2 witness is shared crew-delivery interference rather than hierarchy naming.

## Variety and escalation

Run identity, bounded retries, permit checks, timeout/cancellation, Pulse receipts and partial status handle ordinary disturbances. Pending strategy/goal decisions return to the operator; alerts and failed run status are not automatically algedonic signals or whole-system control.

## Evidence gaps

No paid-provider or live agent E2E execution was performed; the native Go toolchain was unavailable in this environment. Source and deterministic test definitions were inspected, not executed. The unverified current whole-installation S3 return path remains `?`; optional S3* specialist independence and S2 cross-crew scope are deliberately constructor-bounded. README and design documents sometimes describe richer organizational behavior than the exact shipped `scheduler.go`/`server.go` paths; source implementation takes precedence. Historical repository alias is preserved without changing the frozen GitHub ID/ref.
