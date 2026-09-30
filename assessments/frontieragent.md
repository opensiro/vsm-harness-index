---
harness_id: frontieragent
project_name: FrontierAgent
repository: https://github.com/ApodexAI/FrontierAgent
review_ref: 9e533db6f6c34d16037ee5ec964c479d0eb51cde
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# FrontierAgent

## Review boundary

- System in focus: the shipped FrontierAgent `Agent Team` multi-agent runtime at frozen revision `9e533db6f6c34d16037ee5ec964c479d0eb51cde`, including its model-backed coordinator, persistent model-backed sub-agent sessions, task board, AgentBus/SpawnGuard runtime, assignment/report/stop tools, publication-ownership controls, local conflict verifiers and final verifier when reached through the first-party Agent Team profiles.
- Purpose and identity: execute long-horizon research and file-producing tasks by decomposing work, dispatching bounded independent sub-agents, regulating their current commitments, resolving conflicts, verifying the integrated result and returning a synthesized answer or deliverable.
- Relevant environment: user requests; configured model providers; web and file/tool observations; shared or private sandbox state; sub-agent reports and disagreements; agent liveness/job state; task-board commitments; runtime budgets/deadlines; output manifests; operator steering and approval events.
- Standard-distribution boundary: first-party `frontier_agent/`, `workflows/agent_team/`, `plugins/tools/`, and the shipped `apodex` CLI/TUI execution surfaces are inside. External model-provider internals, web services, MCP-server internals and benchmark evaluators are dependencies and are not credited with FrontierAgent organizational functions.
- Credited operating / distribution surfaces: `README.md`; `workflows/agent_team/README.md`; `workflows/agent_team/prompts.py`; `workflows/agent_team/nodes/main_agent.py`; `workflows/agent_team/subagent_runtime.py`; shipped Agent Team profiles under `workflows/agent_team/profiles/`; `plugins/tools/create_subagent.py`; `plugins/tools/assign_task.py`; `plugins/tools/collect_reports.py`; `plugins/tools/stop_subagent.py`; `plugins/tools/task_board.py`; `plugins/tools/finalize_answer.py`; first-party AgentBus/SpawnGuard and sandbox publication controls reached from that runtime.
- Adjacent first-party surfaces excluded from ownership: benchmark scoring/evaluator logic; repository-development CI/governance; the external model provider's internal reasoning; third-party MCP/tool services; operator approval itself; and the single-agent ReAct workflow where it does not participate in the Agent Team organizational closure assessed here.
- First-party operating / deployment modes considered: shipped Agent Team `simple`, `tui` and `benchmark` profiles; interactive TUI/CLI runs; benchmark Agent Team runs; optional reporter mode; optional planning mode as a supported first-party configuration. The positive S2/S3/S3* findings do not require a user-authored orchestration layer.
- Recursion level: one Agent Team run is the system in focus. Model-backed sub-agent sessions are the primary S1 operating units; the model-backed coordinator is assessed as the current metasystem regulator; `local_verifier` and `final_verifier` sessions are specialized complementary agents. A sub-agent is not treated as recursively viable merely because its session can be reused.
- Reviewed revision: `9e533db6f6c34d16037ee5ec964c479d0eb51cde`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

FrontierAgent ships both a single-agent ReAct workflow and a native Agent Team workflow. Agent Team is not only a fan-out helper: a model-backed coordinator maintains a task board, creates named persistent sub-agent sessions, assigns bounded tasks, receives structured reports, can issue follow-up work to retained sessions, and synthesizes the whole run. Sub-agents run the first-party agent loop with their own session identity, specialist system prompt, allowed tools, private worktree and terminal `submit_report` path.

The Agent Team runtime also closes concrete coordination problems. Research agents may produce conflicting claims; the coordinator's shipped `team_effort: max` contract directs it to attach both reports to a separately prompted `local_verifier`, which re-derives or source-checks the disputed point and reports the arbitration. File-producing runs have a second concrete interference surface: `output_paths` is a structured publication grant, verifiers cannot receive it, non-publishers are forced workspace-only, and `assign_task` serializes publication ownership so two agents cannot concurrently own the same final manifest.

Current control is explicit rather than inferred from mere delegation. The coordinator sees task resolutions/owners plus live agent/job state, can add/cancel/reopen tasks, replace owners, issue another evidence wave, stop an off-track or budget-burning agent, reuse a specialist, assign a fresh agent when a session is exhausted, and select or transfer the final publisher under runtime guards. Final verification is organizationally separated again: a `final_verifier` receives the original question and complete draft, is routed to a dedicated verifier system prompt, is barred from publishing, independently re-checks the answer and returns findings to the coordinator for repair and re-verification.

Primary evidence:

- [`README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/README.md)
- [`workflows/agent_team/README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/README.md)
- [`workflows/agent_team/prompts.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/prompts.py)
- [`workflows/agent_team/nodes/main_agent.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/nodes/main_agent.py)
- [`workflows/agent_team/subagent_runtime.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/subagent_runtime.py)
- [`plugins/tools/assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py)
- [`plugins/tools/task_board.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/task_board.py)
- [`plugins/tools/stop_subagent.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/stop_subagent.py)
- [`plugins/tools/finalize_answer.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/finalize_answer.py)

## Operational model

An Agent Team run begins with the coordinator receiving the user objective and building a task board. It creates persistent sub-agent sessions with role-specific prompts and dispatches bounded assignments through AgentBus. Each sub-agent independently iterates over its permitted tools and observations, then returns a structured report. The coordinator consumes reports, updates task commitments, decides where evidence is weak or conflicting, and can dispatch additional waves or stop/reassign work before producing the integrated answer.

For file-producing tasks, publication is a first-party coordination resource rather than an unconstrained shared write surface. An assignment with no `output_paths` is workspace-only; one selected publisher receives the exact `/outputs` manifest. The runtime serializes the publication claim, refuses a second active publisher, blocks verifiers from publishing and delays/controls publisher transfer while an incumbent publish job is active. Thus the coordinator's assignment decision is closed into distinct later capabilities of the affected S1 units.

## S1 — Operations

- State: A
- Function: independently perform bounded open-ended research, analysis, coding/file and evidence-gathering assignments using model reasoning and tool feedback.
- Disturbance / variety regulated: changing task instructions, web/file/tool observations, failures, intermediate evidence, sandbox state, assigned output constraints and follow-up questions from the coordinator.
- Decisive decision or feedback right: choose the next task-specific search, tool, file, computation or report action and revise later actions from returned observations within the delegated assignment.
- Decision owner: each model-backed Agent Team sub-agent session.
- Supporting / enforcement mechanisms: `SwarmSubagentRuntime`; first-party agent loop; per-session specialist prompts; allowed-tool sets; private worktrees; task/session budgets; `submit_report`; context compaction/recovery; AgentBus dispatch.
- Closure path: coordinator assignment + original question → sub-agent model chooses task-specific actions → first-party tool/runtime executes them → observations return to that sub-agent session → the model revises its approach until it submits a report or reaches a runtime stop condition.
- Boundary reachability: Agent Team is a documented native workflow in `README.md` and ships ready profiles whose coordinator can create/assign sub-agents with first-party research/file tools; no user-authored orchestration code is required.
- Why this is / is not agent-owned: removing the sub-agent model while retaining AgentBus, sandboxing, queues and tool executors removes the open-ended choice of what evidence/action to pursue next. Deterministic runtime components constrain the work but do not own its task-specific decisions.
- Evidence: [`README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/README.md); [`subagent_runtime.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/subagent_runtime.py); [`assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic recovery/finalization fallbacks can terminate a failed sub-agent, but ordinary task ownership remains model-backed and feedback-driven.

## S2 — Coordination

- State: A
- Function: regulate concrete interference among distinct S1 work units, including contradictory evidence and competing authority to publish the same final deliverable.
- Distinct S1 units: independently running model-backed Agent Team sub-agent sessions assigned separate research/file tasks, including parallel investigators, a selected publisher, and specialized verifier sessions.
- Inter-S1 disturbance: distinct sub-agents can return contradictory claims/derivations, and independently active workers could otherwise contend for the same final `/outputs` deliverable or retain stale publication authority after reassignment.
- Attenuating coordination relation: the coordinator routes disagreements to a dedicated `local_verifier` with both reports attached and assigns follow-up work from that arbitration; for output contention it grants exactly one structured `output_paths` manifest while runtime publication state/locking excludes competing publishers and forces all others workspace-only.
- Feedback into subsequent S1 behaviour: verifier findings change which claim the coordinator accepts and what follow-up assignments it dispatches; publication arbitration changes which sub-agent can write `/outputs`, which agents remain workspace-only, and whether publisher work is reused, delayed, or transferred.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited paths regulate identified interference among otherwise autonomous S1 outcomes/commitments and close the resolution back into those units' later work or write authority; mere fan-out, messaging and the task board are not used by themselves as S2 evidence.
- Disturbance / variety regulated: incompatible sub-agent reports/derivations; overlapping or contradictory evidence; concurrent attempts to own/write the run's final output manifest; stale publisher ownership during reassignment.
- Decisive decision or feedback right: the coordinator decides when a disagreement requires separate arbitration and which S1 receives follow-up work/publication authority; a dedicated `local_verifier` independently resolves the contested claim, while runtime publication guards enforce the coordinator's single-publisher allocation.
- Decision owner: the model-backed Agent Team coordinator for coordination strategy and assignment; the separately model-backed `local_verifier` for the disputed-evidence arbitration it is assigned.
- Supporting / enforcement mechanisms: `team_effort: max` conflict policy; `<attach agent="..."/>` report transfer; `LOCAL_VERIFIER` specialist prompt; task-board owner changes; structured `output_paths` grant; publication lock/state; one-publisher guard; workspace-only routing for non-publishers; verifier publish prohibition.
- Closure path: distinct S1 reports conflict → coordinator detects the disagreement and spawns/assigns `local_verifier` with both reports → verifier re-derives/source-checks and returns an arbitration report → coordinator updates the task/evidence plan and later assignments from that result. For file contention, coordinator grants one exact output manifest → runtime blocks overlapping publisher ownership → affected agents execute either publisher or workspace-only roles accordingly.
- Boundary reachability: all three shipped Agent Team profiles set `team_effort: max`, which injects the conflict-verifier strategy into the coordinator contract; `assign_task` and its publication guards are first-party tools in those shipped profiles.
- Why this is / is not agent-owned: deterministic locks alone would only serialize access, but here the model-backed coordinator decides which evidence conflict to arbitrate, whether to dispatch more work and which agent owns the publisher commitment. Removing that agent-owned decision while retaining the lock/task board removes the adaptive coordination policy.
- Evidence: [`prompts.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/prompts.py); [`assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py); [`task_board.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/task_board.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every parallel assignment is S2. The positive finding is limited to the concrete conflict/arbitration and publication-interference loops above.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current whole-run view of work and regulate present commitments, staffing and priorities across the Agent Team.
- Whole-system current view: the coordinator receives the run-wide task board with open/in-progress/resolved/cancelled commitments and owners, live AgentBus session/job status, collected/failed/running reports, publication ownership, and remaining runtime/budget signals across the Agent Team.
- Current-control decision scope: the coordinator can add/cancel/reopen tasks, replace owners, create/reuse/stop sub-agents, dispatch another evidence wave, wait or proceed, and select/transfer the final publisher, thereby changing current resource allocation and operational commitments across the run.
- Disturbance / variety regulated: unfinished or newly emergent tasks, weak evidence, stalled/off-track agents, exhausted sessions, failed assignments, conflicting reports, publication responsibility and shrinking runtime/time budgets.
- Decisive decision or feedback right: decide which work remains open/resolved/cancelled, add new work, choose/replace owners, dispatch or reuse agents, stop an active agent, launch another evidence wave, wait for reports, and select/transfer the final publisher subject to first-party safety guards.
- Decision owner: the model-backed Agent Team coordinator.
- Supporting / enforcement mechanisms: live task board with resolutions/owners and agent/job status; `create_subagent`; `assign_task`; `collect_reports`; `stop_subagent`; `add_task`/`update_task`; AgentBus; SpawnGuard; session/task caps; wall/budget observers; publication-state guard.
- Closure path: task board + live agent/job/report state → coordinator compares current coverage/commitments with the user objective → coordinator changes owners/status, dispatches follow-up/new agents, stops/reuses/reassigns work or changes publisher → AgentBus/task-board/publication state applies those choices → subsequent S1 work proceeds under the revised commitments and returns new reports/state.
- Boundary reachability: the documented native Agent Team workflow exposes these tools to the coordinator in shipped `simple`, `tui` and `benchmark` profiles; the task board is always on even though shipped profiles disable the optional two-phase planning mode.
- Why this is / is not agent-owned: AgentBus, task limits and the board mechanically represent/enforce state, but the coordinator chooses which current disturbance matters and how to reallocate commitments. Removing the coordinator model leaves resource caps and queues but removes adaptive whole-run prioritization/reassignment.
- Evidence: [`README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/README.md); [`workflows/agent_team/README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/README.md); [`task_board.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/task_board.py); [`stop_subagent.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/stop_subagent.py); [`assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the S3 finding is not based on delegation or result aggregation alone; it is based on the coordinator's current whole-run state plus actual commitment/reassignment/stop/publication rights.

## S3* — Complementary audit

- State: A
- Function: independently challenge the integrated answer/evidence before completion and return corrective findings to current control.
- Claim being audited: the coordinator's integrated draft and its load-bearing factual, computational and sourced claims before the Agent Team presents the final answer/deliverable.
- Ordinary reporting path: research/worker sub-agents return assignment reports to the coordinator, which synthesizes those reports into the current draft and manages the ordinary task board/commitment loop.
- Complementary access path: a separately instantiated `final_verifier` receives the original question plus the complete draft, then uses its own verifier prompt and independent/different queries, source checks or re-derivations rather than merely accepting the workers' reports.
- Independence boundary: verifier role names are routed to a dedicated first-party verifier system prompt, verifiers are prohibited from publishing the deliverable, and the audit runs in a separate model-backed session from the coordinator and ordinary workers; the optional planning gate can additionally require verifier participation.
- Who acts on findings: the model-backed coordinator consumes verifier findings, repairs the synthesis or dispatches new S1 research on failed points, updates present commitments, and can send the corrected result through another verification pass.
- Disturbance / variety regulated: unsupported or incorrect final claims, arithmetic/factual errors, weak sourcing, contradictions surviving synthesis and other defects in the coordinator's draft.
- Decisive decision or feedback right: the separately instantiated `final_verifier` decides whether claims survive independent re-derivation/source checking and reports concrete failures; the coordinator must then repair/research the failed part and can re-verify before finalizing.
- Decision owner: the model-backed `final_verifier` sub-agent for audit findings; the coordinator owns the corrective response to those findings.
- Supporting / enforcement mechanisms: reserved verifier role names; automatic specialist prompt routing; `FINAL_VERIFIER` role contract; independent/different-query verification guidance; verifier publication prohibition; report handoff; coordinator repair/re-verification loop; optional planning-mode `finalize_gate` that additionally hard-blocks completion without verifier participation.
- Closure path: coordinator forms a complete draft → creates/assigns `final_verifier` with the original question and draft → verifier independently checks load-bearing claims from sources/re-derivation and returns a report → coordinator repairs substantive gaps by revising synthesis or dispatching another S1 wave → corrected answer can be re-verified before completion.
- Boundary reachability: all shipped Agent Team profiles set `team_effort: max`, whose standard coordinator contract explicitly calls for a final verifier and repair/re-verification. Optional planning mode strengthens this with a deterministic finalize gate, but that non-default gate is supporting evidence rather than the sole basis of the positive state.
- Why this is / is not agent-owned: the verifier is a separate model-backed session with a dedicated verifier prompt and no publication authority; it does not merely echo the coordinator's normal synthesis path. Removing the verifier model leaves logging/guards but removes the independent challenge and finding generation.
- Evidence: [`prompts.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/prompts.py); [`create_subagent.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/create_subagent.py); [`assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py); [`finalize_answer.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/finalize_answer.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: shipped profiles keep `planning_mode: false`, so the verifier requirement is model-contract enforced there rather than deterministically blocked by `finalize_gate`. The verifier itself is nevertheless a first-party, separately prompted, boundary-reachable audit actor with corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop established at the declared Agent Team recursion.
- Disturbance / variety regulated: candidate adaptation signals include changing external information, repeated task outcomes, benchmark results, runtime failures, reusable session history, skills and operator steering.
- Decisive decision or feedback right: no first-party actor was found that owns external/future modelling and converts it into a persistent change to FrontierAgent's operational strategy, tool/skill repertoire or organizational configuration, then returns that adaptation through S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: web research; reusable sub-agent sessions; context/history/checkpoints; skills loading; benchmark/evaluation surfaces; user steering; profile configuration.
- Closure path: not established. Agents can research external facts for the current task and retain/reuse current-run context, while skills/profiles are loaded from configured artifacts; no standard first-party loop was found that autonomously generates/selects and persists a future-oriented organizational adaptation for later operations.
- Why this is / is not agent-owned: current-task research and evidence-driven follow-up are S1/S3 activity, not S4 by themselves. Memory/checkpoints and operator-supplied skills preserve or configure capability but do not create an agent-owned outside-and-then adaptation conversation.
- Evidence: [`README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/README.md); [`workflows/agent_team/README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/README.md); [`frontier_agent/components/skills/`](https://github.com/ApodexAI/FrontierAgent/tree/9e533db6f6c34d16037ee5ec964c479d0eb51cde/frontier_agent/components/skills); [`subagent_runtime.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/subagent_runtime.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the runtime has useful ingredients for future adaptive machinery, but ingredients and generic external access are not credited as S4 without the complete prospective adaptation closure.

### Absence scope

- Surfaces inspected: Agent Team coordinator/sub-agent prompts and runtime; shipped profiles; reusable sessions; checkpoint/history/compaction; skills loader/configuration; benchmark/evaluation surfaces; web/tool access; operator steering and reporting.
- Plausible first-party paths checked: current external research; retained specialist context; session/checkpoint recovery; configured skill loading/toggling; benchmark feedback; profile changes; verifier-driven follow-up.
- Why no material first-party path remains: inspected mechanisms either improve the current run, retain context, evaluate externally or load operator-authored capability. None shows a runtime agent forming future/environment distinctions, selecting a durable organizational adaptation and closing that changed capability back through present control into later runs.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure established for one Agent Team run.
- Disturbance / variety regulated: candidate policy matters include tool permissions, approval requirements, execution/sandbox policy, role naming, model/profile configuration and publication authority.
- Decisive decision or feedback right: no first-party agent or parent path was found with authority to resolve identity/purpose/ultimate-policy questions for the runtime and return the result as authoritative policy governing subsequent operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: operator-authored profiles; execution/tool permissions; approval gates; sandbox constraints; role/session identities; publication manifests; runtime limits.
- Closure path: operational policy/configuration constrains tools and writes, but it is supplied/enforced as configuration. No identity-level issue is escalated to legitimate ultimate authority and returned as a policy decision by the assessed runtime.
- Why this is / is not agent-owned: technical agent/session identity, system prompts, permissions and approval enforcement are operational boundaries. They do not by themselves constitute S5 identity and ultimate-policy ownership.
- Evidence: [`README.md`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/README.md); [`workflows/agent_team/profiles/`](https://github.com/ApodexAI/FrontierAgent/tree/9e533db6f6c34d16037ee5ec964c479d0eb51cde/workflows/agent_team/profiles); [`assign_task.py`](https://github.com/ApodexAI/FrontierAgent/blob/9e533db6f6c34d16037ee5ec964c479d0eb51cde/plugins/tools/assign_task.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: this is a runtime-recursion finding; it does not claim the OSS project or its maintainers lack human governance.

### Absence scope

- Surfaces inspected: Agent Team role/session identity, shipped profiles/system prompts, tool/execution permissions, approval and sandbox enforcement, publication authority, operator steering and repository governance as an adjacent development system.
- Plausible first-party paths checked: runtime role identity; approval escalation; execution-policy decisions; publication authority; profile/system-prompt configuration; human project governance.
- Why no material first-party path remains: these paths govern operational actions or project development, but no credited Agent Team path closes an identity/ultimate-policy question through an S5 authority and back into runtime policy.

## Distributed OSS parent arrangement

FrontierAgent is an OSS project, but repository maintainers and project governance are not automatically part of one deployed Agent Team run. Operator approvals and steering can constrain a run, yet no function-specific parent mode is inferred from generic human intervention. The S2/S3/S3* findings are first-party runtime-autonomous rather than parent-attributed; S4/S5 remain absent rather than being promoted from project governance.

## Self-hosted and non-human modes

The documented runtime can execute Agent Team with configured model providers and first-party tools in TUI/CLI/benchmark contexts. Human approval can gate mutating operations, and interactive steering can redirect current work, but neither is required for the positive S1–S3* closure described above. Conversely, no non-human S4/S5 closure was found in the inspected standard modes.

## Recursion

Persistent sub-agent sessions can accept multiple bounded assignments and retain task context, but they do not acquire their own complete metasystem. The assessed recursion therefore remains the whole Agent Team run: sub-agents are S1 operations; coordinator/local-verifier/final-verifier roles form the metasystem functions credited above. Reuse of one sub-agent session is continuity of an operating unit, not evidence of recursive viability.

## Variety and escalation

FrontierAgent attenuates variety through bounded parallelism, task/session caps, tool allowlists, sandbox isolation, exact publication manifests, one-publisher serialization, wall/token budgets and explicit stop/finalization reserves. It amplifies response variety through parallel independent sub-agents, role specialization, follow-up waves, retained session context, web/file/tool access and conflict/final verifier roles. Disagreements escalate to local verification; weak or incomplete evidence can trigger new S1 work; off-track agents can be stopped or replaced; final-audit defects return to the coordinator for repair. Those are material S2/S3/S3* closure paths, while no comparable prospective-adaptation or identity-policy escalation loop was found for S4/S5.

## Evidence gaps

- Standard shipped profiles set `planning_mode: false`; therefore the deterministic finalize gate's verifier requirement is not the default enforcement path. The positive S3* result instead relies on the shipped `team_effort: max` coordinator contract plus the separately instantiated/verifier-specialized runtime path. A future review should re-check if profile defaults change.
- Reporter mode is optional and can fail open, so it is not used as the basis for S3*. The credited audit actor is the Agent Team `final_verifier` sub-agent.
- No self-improvement/adaptation owner was found behind skills, checkpoints, benchmark results or retained sessions. If FrontierAgent later ships a loop that changes and persists its own operational organization from external/future evidence, S4 should be revisited.
- Technical role/session identities and approval policies were deliberately not promoted to S5 without identity/ultimate-policy closure.
