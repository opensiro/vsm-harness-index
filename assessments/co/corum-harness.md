---
harness_id: corum-harness
project_name: Corum Harness
repository: https://github.com/kukucaiCndy/Corum-Harness
review_ref: 1c40d29f933786660fd18b0bc0bf9b55f46ee6cf
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Corum Harness

## Review boundary

- System in focus: the released open-source Corum desktop Task Mode coding-agent installation, including its Conductor preset, worker/research subagent tools, orchestration, and task-level result acceptance.
- Purpose and identity: perform a user-authorized coding task and, in Conductor Mode, distribute the work to specialist children while the lead agent decides how to solve and accept it.
- Relevant environment: the user's current Git workspace, tool permissions, active task, code diffs, parallel worktrees, Git merge state, verification commands, available local/cloud models, and user intervention.
- Standard-distribution boundary: the first-party published Electron desktop, official `standard` and `conductor` presets, `corum-agent`, `corum-tool-subagent`, `corum-orchestration`, review shadow repository and bundled Task Mode configuration. The separately installed DeepSeek Harness runtime supplies the agent loop and fundamental tools; its unconfigured or unrelated modes are not borrowed as first-party Corum capabilities.
- Credited operating / distribution surfaces: [README](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/README.md), [Conductor persona](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts), [mode enforcement](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor-runtime.ts), [orchestrator](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-tool-subagent/src/index.ts), and [closer / worktree ledger](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts).
- Adjacent first-party surfaces excluded from ownership: the README's separately described *closed-source Project Mode* (not in this published repository), upstream DeepSeek Harness core decisions, development-time CI, internal development instruction files, local code-review UI regarded as an operator instrument, and repository maintainer governance.
- First-party operating / deployment modes considered: shipped ordinary coding-agent Task Mode and official Conductor Mode; research children read-only, working children in isolated Git worktrees by default, explicit main-worktree writing where supported; operator permission and plan modes. Packaged macOS Apple Silicon distribution is evidenced; Windows/Linux packaging is not claimed.
- Recursion level: one user task and its temporary lead/worker/closer cells, not the desktop vendor's entire development organization.
- Reviewed revision: `kukucaiCndy/Corum-Harness@1c40d29f933786660fd18b0bc0bf9b55f46ee6cf` (Apache-2.0).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Corum packages an existing agent-loop kernel as a desktop coding-agent product, with first-party session/preset/model/tool plugins. In its shipped Conductor preset the lead agent receives a technical-lead persona and a session-scoped, non-overridable guard against main-tree writes. It can inspect code and plan; it delegates writing and deep research to separate agent sessions. The Corum subagent tool can create isolated Git worktrees, track run/session identity, and settle branches. The `orchestrate` path runs children, then a separate AI closer aggregates their results and merges worktree branches with declared checks. The mechanism independently checks actual Git integration and verification rather than trusting the closer's report. The review shadow repository records per-turn changes for inspection; it is an observation service, not by itself an autonomous reviewer. [Conductor](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts), [worktree truth checks](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts), [review host](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/desktop/src/host/corum-review.ts).

## Operational model

The delivered operation is task-specific code investigation, edits, integration and acceptance. Agent workers choose how to execute a delegated brief. In Conductor Mode the lead is explicitly charged to form a technical solution, inspect actual diffs, reject incorrect child work and issue a corrective brief; the lead cannot silently edit files in place. The closer can perform a bounded merge-and-check step; deterministic checks establish whether changes reached the main tree. This review credits agent discretion where instructions grant it and treats Git isolation, sandbox policy, ledger reconciliation, tool dispatch and review presentation as mechanisms. User supervision remains an outer boundary, not automatic evidence of separate S4 or S5 loops.

## S1 — Operations

- State: A
- Function: produce working code/task outputs through the shipped agent loop and work-performing subagents.
- Disturbance / variety regulated: varied user coding requests, actual source and tool feedback, implementation failures, and changed code found during execution.
- Decisive decision or feedback right: a configured model-led agent selects edits, tool calls and corrective execution steps within the current task; in Conductor Mode workers choose how to implement the lead's bounded brief.
- Decision owner: operational coding agents using the packaged `standard` / `conductor` tool presets; DeepSeek Harness supplies the underlying loop, but the Corum distribution makes the working agents directly usable.
- Supporting / enforcement mechanisms: desktop tool registration, worktree confinement, permissions, task model selection, session persistence and Git/validation checks.
- Closure path: user task and workspace evidence → agent analysis and action → file edits/commands and observed results → agent continuation or returned outcome.
- Boundary reachability: first-party desktop Task Mode registers executable editing and subagent tools, and the official Conductor preset explicitly retains full worker execution rights.
- Why this is / is not agent-owned: choosing task-specific edits and remediation is not determined by worktree/sandbox code or a fixed shell script; an executing model agent remains the operational decision owner.
- Evidence: [README shipped workflow](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/README.md), [Conductor's worker execution semantics](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts), [official executable preset](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/desktop/shipped-presets/official/conductor/agent.cordis.yml).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: actual task success depends on selected provider/model, permissions, dependencies and user environment; it is not independently benchmarked here.

## S2 — Coordination

- State: —
- Function: no separately established, agent-owned cross-S1 oscillation attenuation and returned coordination feedback at this task-cell boundary.
- Disturbance / variety regulated: concurrently writing children can collide in files, Git branches or main-tree state, but the established first-party response is primarily isolation, sequencing and integration.
- Decisive decision or feedback right: no demonstrated agent-owned S2-specific control that observes interference between still-operating distinct S1 units and feeds a corrective coordination decision back into their subsequent operations.
- Decision owner: predefined worktree/sandbox/ledger and closer workflow; the lead's final acceptance and task correction are counted under S3.
- Supporting / enforcement mechanisms: each writer's own branch, scoped write guard, `orchestrate` fan-out, closer's ordered merge, integration-truth checks and retained unmerged branches.
- Closure path: concurrent child results → merge/check or block-and-report to the lead; a merge may reconcile artifacts, but no established autonomous inter-worker feedback loop is visible.
- Why this is / is not agent-owned: a worktree barrier and automatic merge stage mitigate collisions, but isolation, final aggregation and post-task S3 acceptance alone are not S2-specific ongoing agent coordination.
- Evidence: [worktree/conflict mechanisms](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts), [closer persona](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts), [subagent tool](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-tool-subagent/src/index.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: a particular lead may choose corrective task delegation after a conflict; the review does not infer a distinct continuous S2 control loop from that possibility.

### Absence scope

- Surfaces inspected: official Conductor instructions, delegated-task implementation, worktree isolation/confinement, orchestration closer, integration truth checks and review records.
- Plausible first-party paths checked: multiple active children, file interference, merge conflict/verify failure, ledger notices and corrective re-delegation.
- Why no material first-party path remains: these paths establish separation, merge/check and eventual lead-level task acceptance, but not an independently specified S2-specific agent decision returned to re-regulate competing S1 units during subsequent operation.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current whole coding task, prioritize its sub-work, decide implementation strategy and accept or correct delegated results.
- Disturbance / variety regulated: incorrect delegated changes, failed branch integration or checks, incomplete research, scope mismatches and inconsistent child claims can jeopardize the whole task.
- Decisive decision or feedback right: the Conductor lead designs the implementation, selects delegation boundaries and acceptance bar, checks raw changed files/diffs itself, decides whether a child result meets the original objective, and orders a specific corrective round where needed.
- Decision owner: first-party Conductor-mode AI lead; user constraints and operator controls limit authority but do not predetermine its particular acceptance/correction decision.
- Supporting / enforcement mechanisms: enforced read-only lead scope, tool-mediated child dispatch, worktree ledger, closer integration report, Git integration truth/declared verification, read/diff tools.
- Closure path: lead's current task understanding → worker briefs and changes → settled child reports plus actual Git/source evidence → lead accepts, rejects, reroutes or requests corrective work → subsequent task operations reflect that decision.
- Boundary reachability: official `conductor` preset is shipped and the lead persona is installed by session-scoped `ConductorRuntime.apply`, not just described in development notes.
- Why this is / is not agent-owned: a deterministic gate verifies merge facts, but it does not make the technical strategy, issue prioritization, work-acceptance or corrective-brief judgment for the lead.
- Whole-system current view: current task goal, the main workspace, child outcomes, actual diffs and integrity/verification results aggregated through the lead/closer path.
- Current-control decision scope: subdivision and sequencing of task commitments, corrective assignment and acceptance of work for the active user task; not the vendor's future product strategy or external projects.
- Evidence: [lead's explicit decisions, raw-diff verification and correction loop](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts), [non-overridable mode guard](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor-runtime.ts), [closer / integration truth](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: the `standard` preset offers a flatter coding workflow; the positive whole-task lead claim is specific to the shipped Conductor mode, and says nothing about independent assurance of the lead.

## S3* — Complementary audit

- State: —
- Function: no separate agent-owned independent complementary audit route established for the Conductor's whole-task judgment.
- Disturbance / variety regulated: a child could overclaim success or a lead could accept a wrong modification, but not every check against this risk is an independent S3* process.
- Decisive decision or feedback right: the lead inspects workers' diffs and the closer runs declared checks; neither is demonstrated as a structurally independent auditor of the lead's current-control claims with complementary evidence rights.
- Decision owner: task-owning lead and task-finishing closer, with deterministic verification and optional human UI review.
- Supporting / enforcement mechanisms: shadow Git review snapshots, raw diff/round capture, integration truth and verification command, user-visible review cards.
- Closure path: raw changes → lead acceptance and optional human inspection; no distinct independent S3* verdict returned to regulate lead control is established.
- Why this is / is not agent-owned: machine truth checks and the same lead reviewing its subordinates do not create the complementary audit channel required for S3*.
- Evidence: [Conductor verification instructions](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts), [review capture host](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/desktop/src/host/corum-review.ts), [closer](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-orchestration/src/orchestration.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: independent user inspection can be valuable without proving first-party autonomous S3* ownership.

### Absence scope

- Surfaces inspected: lead verification, subagent reports, integration closer, review shadow repository and recovery, local review UI and mode presets.
- Plausible first-party paths checked: independent closer session, stored pre/post-image review, verification commands, manual inspect/revert, and read-only research children.
- Why no material first-party path remains: the closer is a task-finishing integration node and reports to the lead, review capture is observational, and research children answer delegated questions; none has a demonstrated mandate and complementary access to independently audit S3 decisions.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established future-environment sensing, candidate capability adaptation and adoption loop belonging to this task-cell recursion.
- Disturbance / variety regulated: longer-term shifts in external project needs, tools or operating strategy could require adaptation but are not a documented function-specific control path here.
- Decisive decision or feedback right: no separate prospective adaptation judgment with a returned capability change established beyond current-task planning and operator-managed settings/skills.
- Decision owner: human user or product maintainer for installed features/settings; task agents handle present coding objectives.
- Supporting / enforcement mechanisms: persistent memory, goals, configurable skills, model providers and plan mode can support longer use but do not themselves decide future adaptation.
- Closure path: no evidenced outside/then observation → proposed change → authorizing adoption → changed task-system capability loop.
- Why this is / is not agent-owned: a plan for solving the current task and stored facts are not proof of a strategic intelligence/adaptation function.
- Evidence: [README feature list](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/README.md), [official preset plan mode](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/desktop/shipped-presets/official/conductor/agent.cordis.yml), [task conductor](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: a user may ask the coding agent to improve its own tools as an ordinary task; that alone does not prove an ongoing S4 function at this assessed recursion.

### Absence scope

- Surfaces inspected: Task Mode, lead persona, memory/goals/skill integration and official plan preset.
- Plausible first-party paths checked: memory persistence, long-running goal tools, operator model/skill selection, current project research and developer CI/roadmap.
- Why no material first-party path remains: the shipped task cell has no evidenced autonomous prospective environment-scanning and adaptation-decision loop that changes the future capability under its own S4 mandate; adjacent maintainer planning is outside scope.

## S5 — Policy and identity

- State: —
- Function: no ultimate-identity or unresolved policy-tension adjudication at the assessed task-cell recursion.
- Disturbance / variety regulated: permission changes, safe worktree boundaries, user goals and model routes are operational constraints, not evidenced ultimate-identity disputes.
- Decisive decision or feedback right: no entity within the deployed Task Mode is shown deciding organizational purpose, ultimate policy or identity and returning a binding decision.
- Decision owner: legitimate user and vendor outside the assessed work-cell boundary; guard mechanisms enforce provided constraints.
- Supporting / enforcement mechanisms: permission presets and guard composition, immutable Conductor read-only scope, sandbox confinement, task plan approval controls and preset persona.
- Closure path: user setting or authorization → fixed runtime policy; no separate S5 issue → legitimate adjudication → governing decision → task return loop is established.
- Why this is / is not agent-owned: a persona, safety guard and permission decision do not make the task agent an ultimate-policy authority.
- Evidence: [mode permissions](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/permission-policy.ts), [conductor runtime guard](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/plugins/agent/corum-agent/src/conductor-runtime.ts), [official plan-mode rule](https://github.com/kukucaiCndy/Corum-Harness/blob/1c40d29f933786660fd18b0bc0bf9b55f46ee6cf/packages/desktop/shipped-presets/official/conductor/agent.cordis.yml).
- Basis: structural.
- Confidence: medium.
- Caveats: this does not evaluate the developer/maintainer's separate OSS governance.

### Absence scope

- Surfaces inspected: official operating modes, persona, user permissions, approval/plan controls, and tool guards.
- Plausible first-party paths checked: operator-selected autonomy, immutable restriction, research/worker policy, escalation and developer repository governance.
- Why no material first-party path remains: the inspected runtime enforces higher-level settings without a material policy-identity adjudication and returned task-governing S5 decision; upstream developer governance is excluded.

## Distributed OSS parent arrangement

Corum is distributed as an OSS agent application usable by independent desktop operators. The local user chooses a task, permissions, models and operating mode; the authors maintain source releases. The task cell does not inherit organization-level governance from the public GitHub repository. No `P` parent-mode autonomy state is asserted solely because the human can supervise or approve work.

## Self-hosted and non-human modes

Users can configure local model providers, but first-party Conductor/standard modes still run under user task and permission boundaries. No self-hosted operator variant establishes a separate S3/S4/S5 parent ownership mode with a function-specific feedback loop in this evidence. No autonomous organization outside the local task is credited.

## Recursion

Workers and research children perform bounded delegated tasks; the AI closer reports and integrates their results; the Conductor lead has whole-task acceptance rights. Separate subagents do not establish complete independent viable-system recursions. The closed-source Project Mode's larger management structure cannot be inferred from Task Mode source.

## Variety and escalation

Worktree and Git guards attenuate parallel write risk; the ledger distinguishes settled, unmerged and integrated branches using actual Git state. A failed verification is reported without a false success claim, and partial worktrees may be retained. The lead can return a precisely bounded corrective task to a worker. A plan-approval or sandbox permission card is an operator control, not automatically an S5 policy adjudication or independent S3* audit.

## Evidence gaps

- No independently executed desktop session or empirical success-rate result is claimed; conclusions refer to pinned first-party code, packaged instructions and unit-test surfaces.
- The separate closed-source Project Mode is excluded and may possess different cross-task control and adaptation rights that this assessment cannot infer.
- Worktree isolation and the closer's ordered merge regulate collisions, but no continuous S2-specific inter-S1 corrective decision/return loop was found in the inspected shipped paths; an observed one would warrant reconsideration.
