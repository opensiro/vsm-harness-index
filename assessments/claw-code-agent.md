---
harness_id: claw-code-agent
project_name: claw-code-agent
repository: https://github.com/HarnessLab/claw-code-agent
review_ref: 167571da895b2a1a9e36ecfae2876984cef65e0d
reviewed_at: 2026-09-15
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
last_checked_ref: 167571da895b2a1a9e36ecfae2876984cef65e0d
last_checked_at: 2026-09-28
assessment_changed_at: 2026-09-28
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# claw-code-agent

## Review boundary

- System in focus: the first-party claw-code-agent runtime at `167571da895b2a1a9e36ecfae2876984cef65e0d`, including its coding-agent loop, child-agent delegation, Agent Manager lineage/groups, local task/plan runtimes, and local team/message runtime.
- Purpose and identity: autonomously perform coding/tool tasks with persistent local execution state, nested delegation, plans/tasks, and optional team/message composition.
- Relevant environment: user tasks, local repository/workspace state, model provider/runtime, shell/tools, parent configuration, and any externally supplied team/task definitions.
- Standard-distribution boundary: the repository-shipped Python runtime and documented CLI/slash/GUI surfaces at the pinned default-branch revision. Repository tests, development workflow, external model cognition and downstream application policy remain environment or adjacent evidence.
- Credited operating / distribution surfaces: `src/agent_runtime.py`, `src/agent_tools.py`, `src/plan_runtime.py`, `src/task_runtime.py`, `src/team_runtime.py`, Agent Manager/delegation paths, and documented runtime commands.
- Adjacent first-party surfaces excluded from ownership: `TESTING_GUIDE.md` examples and repository tests are corroboration only; `PARITY_CHECKLIST.md` describes implementation status but is not an operating actor; contributor/CI/release processes are excluded.
- First-party operating / deployment modes considered: ordinary coding-agent loop; nested child-agent delegation; dependency-aware task execution; persisted plan/task runtime; local team/message runtime.
- Recursion level: one claw-code-agent application organization. Child agents and groups are operational subdivisions unless their own complete metasystem is separately evidenced.
- Reviewed revision: `167571da895b2a1a9e36ecfae2876984cef65e0d`.
- Observation date: 2026-09-28 same-ref correction. Upstream default `main` still resolves exactly to the accepted review ref, so no new-ref reassessment is needed.
- Generated Profile version: not recorded in the legacy artifact.
- Generated Methodology version: not recorded in the legacy artifact.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The repository ships a model-driven coding loop with tools, persisted sessions and child-agent delegation. Agent Manager state records lineage/groups. Plans and tasks can persist owners, statuses and dependency relations; `PlanRuntime` translates `depends_on` into task `blocked_by` / `blocks` state and dependency-aware execution/topological batching. `TeamRuntime` persists team definitions and plain messages with sender, optional recipient, text and metadata.

Those mechanisms materially support decomposition and sequencing. Under the current Profile, however, dependency ordering and message transport do not become S2 unless they are tied to a concrete inter-S1 interference/conflict/oscillation plus an attenuation relation specifically responding to that disturbance. The repository's own parity checklist explicitly says broader task orchestration and team/collaboration flows remain incomplete beyond the local dependency-aware/message runtimes.

## Operational model

The model-driven coding/child agents are S1. They interpret tasks, use tools, modify or inspect the workspace, and return results. Parent/manager logic can spawn/delegate children and record execution relationships.

The previous `S2=C` promoted team messaging plus dependency-aware task state into constructor coordination. Re-review under Profile 0.2.4 finds only generic communication and predeclared sequencing: dependencies prevent a later task from running before prerequisites, but the repository does not establish an interaction-generated conflict/oscillation among distinct S1 units and a coordination result selected to attenuate it. S2 is therefore corrected from `C` to `—` at the same accepted revision.

## Primary evidence

- [`README.md`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md) — full coding runtime, nested delegation, local team/messages, task/plan runtime and dependency-aware execution.
- [`src/agent_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py) — autonomous coding loop and dependency-aware child/delegated task execution.
- [`src/plan_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/plan_runtime.py) — `depends_on` plan state synchronized into task `blocked_by`/`blocks` relationships.
- [`src/team_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/team_runtime.py) — persisted team definitions and generic sender/recipient message history.
- [`TESTING_GUIDE.md`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/TESTING_GUIDE.md) — executable examples for team messages and dependency-aware task execution.
- [`PARITY_CHECKLIST.md`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/PARITY_CHECKLIST.md) — broader orchestration/collaboration remains beyond the implemented local runtimes.
- [Upstream default branch](https://github.com/HarnessLab/claw-code-agent/commit/167571da895b2a1a9e36ecfae2876984cef65e0d) — still exactly the canonical review ref at re-review time.

## S1 — Operations

- State: A
- Function: autonomously perform coding and tool-mediated implementation/analysis tasks, including delegated child-agent subtasks.
- Disturbance / variety regulated: heterogeneous coding requests, workspace/repository state, tool outputs/failures, context/session state and delegated subtask uncertainty.
- Decisive decision or feedback right: select the next model-driven coding/tool action and produce the operational result for the assigned task.
- Decision owner: the model-driven main or child coding agent at its operating boundary.
- Supporting / enforcement mechanisms: tool runtime, sessions, Agent Manager lineage, child delegation, plans/tasks, dependency checks, file history and runtime state.
- Closure path: task → model decision → tool/workspace action → observed result → subsequent model decision → returned outcome.
- Boundary reachability: the autonomous agent loop and child delegation are standard first-party runtime paths, not repository-development-only actors.
- Why this is / is not agent-owned: deterministic task/session machinery persists and sequences work, while the agent owns substantive coding/tool decisions.
- Evidence: `src/agent_runtime.py`; `README.md`; agent/tool runtime surfaces.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: parent prompts/configuration and the model provider constrain the operating space, but the shipped loop still exposes autonomous S1 discretion.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes disturbance-specific attenuation of interference/conflict/oscillation among distinct S1 units at the declared recursion.
- Disturbance / variety regulated: no qualifying interaction-generated inter-S1 disturbance is established. A dependency relation describes required order; a team message records/forwards information.
- Decisive decision or feedback right: no S2-specific coordination decision/feedback right is established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: dependency-aware task blocking/topological batching, plan/task ownership/status, persisted teams, sender/recipient messages, child-agent groups and delegation.
- Closure path: dependencies can delay a task until prerequisites complete and messages can influence later work, but neither is evidenced as a response to a concrete inter-S1 disturbance with a coordination result fed back into later S1 behaviour.
- Why this is / is not agent-owned: ownership classification does not begin because the functional S2 witness is absent; the observed mechanisms are sequencing, state and communication.
- Evidence: `src/plan_runtime.py`; `src/task_runtime.py`; `src/team_runtime.py`; `src/agent_runtime.py`; `PARITY_CHECKLIST.md`.
- Basis: current-contract same-ref correction.
- Confidence: high.
- Caveats: a downstream system could use these primitives to build genuine coordination, but general composability is not `C` under Methodology 0.3.6.
- Distinct S1 units: main/child agents and multiple delegated workers can constitute distinct operational units.
- Inter-S1 disturbance: not established as actual or structurally evidenced interference/conflict/oscillation arising from their interaction.
- Attenuating coordination relation: dependency ordering prevents invalid prerequisite order but is deterministic task sequencing, not a response relation to an evidenced inter-S1 disturbance; team messages are generic transport.
- Feedback into subsequent S1 behaviour: task completion and messages can affect later work, but not as feedback from an S2-specific disturbance-attenuation decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the evidence is precisely generic messaging, dependency sequencing and delegation.

### Absence scope

- Surfaces inspected: local team/message runtime, plan/task dependency runtime, child-agent delegation, Agent Manager lineage/groups, testing examples and parity status.
- Plausible first-party paths checked: dependency-aware batching as collision avoidance; team messages as mutual adjustment; task ownership/blocking as conflict control; Agent Manager groups as coordination; parent-child handoff as S2.
- Why no material first-party path remains: none ties a concrete inter-S1 disturbance to a first-party attenuation relation and returned behavioural adjustment; the repository explicitly leaves broader orchestration/collaboration beyond these local primitives incomplete.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established over the organization-wide portfolio of S1 resources, commitments, priorities or constraints.
- Disturbance / variety regulated: not established as S3 at this recursion.
- Decisive decision or feedback right: not established for whole-system current regulation.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: parent-task delegation, Agent Manager lineage/groups, task statuses/owners/dependencies, plan summaries and runtime/tool limits.
- Closure path: not applicable as S3.
- Why this is / is not agent-owned: these surfaces decompose and sequence work but do not establish a whole-current-system view plus discretionary authority over shared resources/commitments/priorities on behalf of the whole.
- Evidence: `src/agent_runtime.py`; `src/plan_runtime.py`; task/Agent Manager surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: manager/owner/status labels are not S3 shortcuts.

### Absence scope

- Surfaces inspected: Agent Manager, nested delegation, plan/task state, owner/dependency fields, execution summaries and runtime constraints.
- Plausible first-party paths checked: Agent Manager as S3; task owner/status ledger as whole-system current view; dependency scheduling as S3 allocation; parent agent as current regulator.
- Why no material first-party path remains: the evidence remains task orchestration/decomposition rather than whole-system current regulation with organizational intervention authority.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is supplied that challenges ordinary operational claims with different access and returns findings into corrective control.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: not established for an independent audit judgment.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: transcript/file history, tests, diagnostics and runtime event records expose evidence but are not an independent operating auditor.
- Closure path: not applicable as S3*.
- Why this is / is not agent-owned: no first-party standard role/path separates an auditor from the producing operation and returns its findings into correction/re-verification.
- Evidence: runtime history/diagnostic surfaces and repository tests considered as adjacent evidence only.
- Basis: structural absence review.
- Confidence: high.
- Caveats: a downstream child agent can be prompted as a reviewer, but generic delegation does not establish first-party complementary-audit ownership.

### Absence scope

- Surfaces inspected: child agents, diagnostics, transcripts/file history, tests and task result flows.
- Plausible first-party paths checked: child reviewer as S3*; repository tests as audit; transcript/history inspection as complementary access.
- Why no material first-party path remains: no standard operating path establishes sufficiently independent audit judgment plus findings returned into corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective intelligence loop develops adaptation options for the claw-code-agent organization and returns them into present capability.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: not established for organizational adaptation.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: search, planning, context compaction, remote triggers and runtime adaptation support current task execution.
- Closure path: not applicable as S4.
- Why this is / is not agent-owned: current-task planning/search does not establish environment/future modelling → adaptation option → present-capability change.
- Evidence: search/planning/runtime surfaces at the pinned revision.
- Basis: structural absence review.
- Confidence: high.
- Caveats: downstream agents may perform research, but their task output is not inherited as organizational S4.

### Absence scope

- Surfaces inspected: search runtime, plans/tasks, remote triggers, context/session mechanisms, plugins/hooks and child delegation.
- Plausible first-party paths checked: web search as S4 sensing; planning as adaptation; compaction/session memory as learning; remote triggers as environmental response.
- Why no material first-party path remains: these support current operations rather than a first-party outside-and-then adaptation loop changing organizational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at this recursion.
- Disturbance / variety regulated: not established as an identity/ultimate-policy matter.
- Decisive decision or feedback right: prompts, policies, permissions, budgets and runtime configuration remain parent/application authored.
- Decision owner: developer/operator outside the autonomous assessed runtime for those choices.
- Supporting / enforcement mechanisms: prompt/configuration, permission/policy hooks, budgets and tool restrictions.
- Closure path: static/parent configuration constrains later operation, but no identity-level issue reaches legitimate S5 authority and returns as an authoritative policy decision through a first-party loop.
- Why this is / is not agent-owned: agents operate under configured policy rather than owning ultimate organizational identity/policy.
- Evidence: runtime configuration/policy surfaces at the pinned revision.
- Basis: structural absence review.
- Confidence: high.
- Caveats: operator configuration power alone does not establish published `P`.

### Absence scope

- Surfaces inspected: prompts, policy/hooks, permissions, budgets, plugin/runtime configuration and operator-facing controls.
- Plausible first-party paths checked: parent prompt as S5; policy/tool restrictions as S5; operator approval/config edits as parent S5.
- Why no material first-party path remains: no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned subsequent-operation path is established.

## Distributed OSS parent arrangement

Repository contributor/maintainer governance is outside the shipped runtime boundary and is not credited as a distributed parent metasystem.

## Self-hosted and non-human modes

Local/self-hosted operation exposes parent configuration and control, but no separate first-party parent S3/S4/S5 closure is established merely from operator access.

## Recursion

Agent Manager lineage, groups and nested child agents prove decomposition and local operational autonomy, not that each child carries its own complete S2-S5 metasystem. No recursive viable-system credit is inferred from nesting alone.

## Variety and escalation

Nested delegation and tools amplify operational response variety; plans/dependencies attenuate execution-order variety; messages transmit team information. Permission/policy/tool failures can reach the parent/user, but ordinary operational escalation does not itself establish S3/S4/S5.

## Evidence gaps

- No accepted-revision trace or structural relation was found where interaction among distinct S1 agents creates a concrete interference/conflict/oscillation and the runtime selects a coordination response specifically to attenuate it.
- The local dependency-aware runtime enforces prerequisite ordering, but Profile 0.2.4 explicitly distinguishes generic sequencing from S2.
- The local team runtime persists generic messages; broader collaboration/orchestration is explicitly incomplete in `PARITY_CHECKLIST.md`.
- Upstream default `main` remains exactly the accepted review ref, so this is a semantic/current-contract same-ref correction rather than new evidence repinning.
