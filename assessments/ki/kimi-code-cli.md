---
harness_id: kimi-code-cli
project_name: Kimi Code CLI
repository: https://github.com/MoonshotAI/kimi-code
review_ref: 68a283894163204e93b072cef20db164015a5cad
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Kimi Code CLI

## Review boundary

- System in focus: one Kimi Code CLI coding workspace/session at the frozen revision, including the terminal model/tool loop, built-in subagents, and its explicitly supported opt-in experimental Tower collaboration mode with mission workers, independent reviewers and a target git branch.
- Purpose and identity: autonomously solve coding requests and, in Tower mode, coordinate parallel repository changes through assigned missions, scoped worktrees and review-gated integration.
- Relevant environment: human objective/steering, repository code and tests, git branches, model/provider/tool outcomes, tool permissions, worker availability, contested files, changing integration base and reviewer findings.
- Standard-distribution boundary: first-party TypeScript CLI and agent-core-v2 runtime, shipped agent profiles, bundled Tower feature/tools/protocol and user-facing activation path. Models are external inference providers but the shipped agents are first-party operational roles; the assessed outcome is the reachable packaged system, not the model vendor's organization.
- Credited operating / distribution surfaces: core model/tool step machine, default main coding agent and built-in coder/explore/plan; opt-in Tower coordinator/worker/reviewer roles, mission plan/status/spawn/inbox/send/review/merge/rebase tools, mission store and merge gate; user-facing TUI and documented `/tower` enablement.
- Adjacent first-party surfaces excluded from ownership: Kimi's own GitHub maintainer/release/CI workflows, marketing docs and external project organizations; user-authored plugin agent policies, external MCP orchestration, experimental modes that are merely discussed but not compiled. Goal/Plan/Swarm and generic tool permissions are considered for false-positive control, not assumed to operate concurrently with Tower.
- First-party operating / deployment modes considered: default single-agent coding session; supported background subagents and explicit `/swarm` (separate mode); Tower **opt-in** via `[experimental] tower=true` or `KIMI_CODE_EXPERIMENTAL_TOWER=1` and `/tower on`; Tower worker and independent reviewer on separate contexts/worktrees, mission merge/rebase, steering and stop; print/ACP where Tower is not active. The stronger S2/S3/S3* claims belong to Tower mode, **not** default print/ACP runs.
- Recursion level: one goal-bound software-development workspace with a Tower main-agent coordinator and a fleet of independently acting mission workers. Tower workers are operational units; the coordinator regulates that fleet. This does not equate every nested subagent with a recursively viable organization.
- Reviewed revision: `68a283894163204e93b072cef20db164015a5cad`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The ordinary Kimi agent iteratively chooses tools, observes tool feedback and continues coding. Built-in `coder`, `explore` and `plan` subagents isolate contexts, and `AgentSwarm` fans out item-shaped tasks only after a user enables swarm mode; these alone do not prove organizational metasystem functions. The first-party Tower feature is more specific: an explicit experimental flag assembles Tower tools, `/tower` activates an agent-owned coordinator, and a persisted mission protocol connects scoped worker worktrees to a common branch. The coordinator plans disjoint task scopes, dispatches separate model-backed workers, reads current fleet status and worker/reviewer reports, intervenes through messages or scope/dependency changes, and orders integration. A distinct reviewer is spawned for a completed branch, inspects it independently and submits a verdict; a git-commit-bound merge gate rejects unresolved findings, stale review, changed branch tip, scope leakage and unmet dependencies.

Pinned first-party entry points: [README](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/README.md), [agents guide](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/customization/agents.md), [Tower guide](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/guides/tower.md), [Tower activation](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/towerService.ts), [Tower agent instructions](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/injection/tower-mode-full-reminder.md), [mission gate](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/protocol/missionGate.ts).

## Operational model

In ordinary mode, a human asks a coding question; the main agent makes task-local model/tool choices and returns a result, optionally with bounded child-agent delegations. In Tower mode, after the human enables the feature and submits an objective, the main agent chooses missions, scopes, dependencies, workers and follow-up directions; workers execute coding tasks in isolated worktrees. Task completion triggers a separate reviewer and a review verdict. Failing reviews return feedback to the worker/coordinator and can reopen a mission. A clean exact-tip review plus resolved dependencies and checks permits TowerMerge to integrate the result. The recorded human objective bounds the system; human corrections do not by themselves constitute S5.

## S1 — Operations

- State: A
- Function: model-backed coding, codebase inspection, implementation, testing and committed mission work.
- Disturbance / variety regulated: uncertain implementation requirements, unfamiliar source, tool failures, repository/test feedback and local defects.
- Decisive decision or feedback right: decide next file/search/edit/shell action, inspect results, revise implementation and submit a bounded finished mission.
- Decision owner: Kimi main coding agent in default mode and independent Tower worker agents in Tower mode; each is a first-party model-driven agent role.
- Supporting / enforcement mechanisms: agent-core-v2 model/tool loop, provider adapters, tool permission gate, agent profiles, worker worktree, mission task list, session state and result handoff.
- Closure path: objective/mission reaches a model-driven coding role → agent chooses tools/edits/tests from actual feedback → tools affect the target workspace → agent continues or sends a completion report and committed changes → the higher-level Tower path receives the result.
- Boundary reachability: README/quick-start invoke the shipped coding agent; `TowerSpawn` constructs actual worker sessions on first-party mission worktrees when Tower mode is enabled.
- Why this is / is not agent-owned: tool execution and permissions enforce boundaries, but substantive implementation actions and task-specific responses to observed failures are selected by the model-backed coding workers.
- Evidence: [README](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/README.md), [tool contract](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/reference/tools.md), [agent profiles](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/customization/agents.md), [worker profile](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/workerProfile.ts), [worker spawn](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md).
- Basis: explicit + structural.
- Confidence: high for reachability/ownership.
- Caveats: external model quality is not independently measured; no live provider-backed task was executed for this assessment.

## S2 — Coordination

- State: A
- Function: active worker-workspace conflict attenuation and mission dependency/integration coordination in the opt-in Tower mode.
- Distinct S1 units: two or more simultaneously executing Tower coding workers with separate task objectives and git worktrees, later contributing to the same base branch.
- Inter-S1 disturbance: overlapping file scopes and branches can overwrite one another or incorporate unreviewed integration changes; a completed mission can become stale after another mission changes the base.
- Attenuating coordination relation: Tower model decomposes and selects mission scopes/dependencies, prefers disjoint scopes, routes conflict findings and may revise scope or dependencies; first-party protocol enforces overlapping-scope merge dependencies, independent worktrees, ordered merges, scope checks and rebase gates.
- Feedback into subsequent S1 behaviour: scope/dependency/merge refusal reaches the Tower agent; it can change the mission scope, rebase/redirect the affected worker or return conflicting code for correction before further worker progress and integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the specific regulated interaction is concurrent mutation/integration conflict among distinct coding workers. Private worktrees, overlapping-scope dependencies, stale-base checks and returned conflict repair are concrete disturbance attenuation rather than mere message passing.
- Disturbance / variety regulated: shared-file collisions, branching divergence, stale integration target, scope overlap and dependency-order interference among separate task executors.
- Decisive decision or feedback right: Tower's model chooses a conflict-attenuating decomposition/scope/dependency pattern and can adjust it after returned mission/review/merge feedback. Deterministic guards enforce its selected relationship.
- Decision owner: Tower coordinator agent for task-specific mission/scope/dependency adjustments (`A`); protocol/store for fixed isolation, auto-dependency and merge safety (`C` support, not a second independently published operating mode).
- Supporting / enforcement mechanisms: `TowerPlan`, `TowerMission`, per-worker git worktree, overlap auto-dependencies, `TowerRebase`, `TowerMerge`, and `evaluateMissionGate`.
- Closure path: multiple tasks target the same repository → Tower chooses scopes/deps and spawns workers in isolated worktrees → scope overlap/changed base/review conflicts are detected by store/merge gate → coordinator receives precise refusal/finding → coordinator revises scope, ordering or worker instructions → subsequent work/merges follow the revised separation.
- Boundary reachability: enabling the shipped Tower flag assembles and exposes planning, spawn, review, merge and rebase tools; documented workflow invokes them as runtime tools, and the repository includes Tower tool/protocol tests.
- Why this is / is not agent-owned: git worktree creation and dependency enforcement alone would only be `C`. The `A` witness is the Tower agent's discretionary choice and revision of mission partitioning/scope/response, guided by returned cross-worker interference and enforced through the protocol.
- Evidence: [Tower mode instruction](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/injection/tower-mode-full-reminder.md), [TowerPlan](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/plan/plan.md), [mission gate](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/protocol/missionGate.ts), [TowerMerge](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/merge/merge.md).
- Basis: explicit + structural.
- Confidence: medium-high; opt-in agent-owned role is explicitly prescribed but not empirically exercised here.
- Caveats: automatic scope/dependency checks are deterministic and do not guarantee semantic non-interference; parallel workers may still produce logically incompatible changes. Generic subagent invocation and AgentSwarm alone are not the S2 witness.

## S3 — Inside-and-now control

- State: A
- Function: current regulation of the Tower development mission fleet as a whole, including commitment allocation, task progress and correction.
- Disturbance / variety regulated: dynamic task progress, worker failures, blocked missions, missed requirements, merge/review failures and changing shared priorities.
- Decisive decision or feedback right: split an objective into missions, choose worker assignments/scopes/dependencies, reprioritize, redirect workers, reassign stalled work and select compliant integration/recovery actions based on current roster and mission state.
- Decision owner: the active model-backed main agent in the explicitly entered Tower coordinator role; human controls bound/steer it but do not establish a distinct first-party closed parent S3 operating mode.
- Supporting / enforcement mechanisms: `TowerStatus` whole-fleet dashboard, `TowerInbox`, `TowerSend`, `TowerMission`, `TowerSpawn`, roster, persistent protocol and permission controls, merge/readiness reasons, task concurrency budget.
- Closure path: active workers report progress/completion/blockers → coordinator receives waking inbox messages and fleet/gate digest → model chooses reassignment, corrective prompt, review/rebase, revised dependencies or allowed merge → Tower tools update mission/worker state → further feedback becomes visible.
- Whole-system current view: first-party `TowerStatus` includes all current missions, statuses, owners, live roster, merge gates, dependencies, inbox and recent event history.
- Current-control decision scope: changing present work distribution, worker attention, mission scopes, blockers, dependencies, integration priority and escalation across the entire active fleet.
- Boundary reachability: one enabled Tower session's main agent receives the coordinator role and built-in tools; worker completion and review events wake the coordinator rather than relying on a third-party scheduler.
- Why this is / is not agent-owned: the model-driven coordinator selects substantive current fleet-control responses. Resource caps, state persistence, Git checks and message routing only support or enforce its choices; human steering is allowed but does not make it merely a manual dashboard.
- Evidence: [Tower mode instruction](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/injection/tower-mode-full-reminder.md), [Tower status](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/status/status.md), [Tower service](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/towerService.ts), [mission control](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/mission/mission.md).
- Basis: explicit + structural.
- Confidence: high for supported design path, medium for real-world task performance.
- Caveats: Tower is experimental, disabled by default and not active in print/ACP. Human can stop and steer any participant; those rights do not automatically constitute separate `A(P)`. Capacity limit and automatic wake alone would not prove S3.

## S3* — Complementary audit

- State: A
- Function: independently challenge a coding worker's claim that a completed branch meets its mission and is safe to integrate.
- Disturbance / variety regulated: unverified implementation, missing task requirements, test regressions, branch divergence, out-of-scope modifications and misleading worker self-reports.
- Decisive decision or feedback right: a separately spawned reviewer examines the branch against mission text and actual diff/tests, judges `clean` versus findings, records explicit `merge`/`fix-then-merge`/`hold`, and thereby permits or blocks merge of that commit.
- Decision owner: distinct model-backed Tower reviewer agent for the independent audit judgment; deterministic review store/merge gate binds the verdict to branch tip and enforces it. Tower itself retains current integration/dispatch S3 decisions.
- Supporting / enforcement mechanisms: `TowerSpawn(review_target)`, independent reviewer work context, read-only reviewer role instructions, `TowerReview`, stored verdict/finding protocol, `evaluateMissionGate`, precise tip/scope/dep enforcement and returned non-clean notifications.
- Closure path: worker completes mission → coordinator spawns new independent reviewer with mission intent and author report → reviewer checks actual branch and reports findings/verdict → non-clean result returns to worker/coordinator for repair and re-review; clean approved exact-tip result opens the enforced merge gate → coordinator can integrate.
- Claim being audited: the worker's completed branch is consistent with the declared mission scope/task requirements and sufficiently verified to merge.
- Ordinary reporting path: worker `TowerComplete(report)` reconciles its own task checklist and source changes.
- Complementary access path: separate reviewer is assigned `review_target`, reads original mission requirements and the actual branch/diff/relevant checks rather than merely accepting the worker's report.
- Independence boundary: reviewer is a distinct spawned agent/role with separate context from the worker, reviewer-target ownership validated by protocol and a read-only audit mandate; providers/models may still be shared, so this is role/context independence rather than proven statistical independence.
- Who acts on findings: reviewer owns `clean`/finding judgment; protocol rejects a bad/stale/hold verdict; coordinator and worker receive corrective notifications, the worker can fix/recommit, and another review is required before merge.
- Boundary reachability: Tower guide explicitly documents automatic reviewer assignment; shipped `TowerSpawn` reviewer profile and `TowerReview`/missionGate implementation are reachable under the enabled Tower session.
- Why this is / is not agent-owned: the review model, not mere CI or the deterministic merge parser, chooses substantive claim-verification findings and acceptance. The gate prevents operator shortcuts in normal flow; exceptional `reviewer=tower` break-glass is explicitly documented and is **not** the basis of this independent-audit claim.
- Evidence: [Tower guide](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/guides/tower.md), [review submission protocol](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/review/review.md), [review tool](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/tools/review/reviewTool.ts), [review assignment and submission](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/protocol/store.ts), [merge gate](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/protocol/missionGate.ts).
- Basis: explicit + structural.
- Confidence: medium-high; supported architectural independence and corrective return, no live defect-detection quality measured.
- Caveats: Tower coordinator can exceptionally submit a break-glass review, reducing independence in that exceptional path. This assessment claims the normal separately assigned-reviewer operating mode only; it does not promise perfect review or unconditional independent quality.

## S4 — Outside-and-then intelligence

- State: —
- Function: no materially separate first-party external/prospective adaptation loop with capability return was established.
- Disturbance / variety regulated: future coding ecosystem, provider capability shifts and changes in organizational strategy could require adaptation, but ordinary current task management is not this function.
- Decisive decision or feedback right: none established for an agent/constructor/closed parent to assess the external future, develop a new operating capability and return it into the present Tower fleet.
- Decision owner: none established for qualified S4 in the pinned standard distribution.
- Supporting / enforcement mechanisms: future-oriented planning subagent, Tower mission decomposition/replans, Goal mode auto-continuation, web search/fetch, model configuration and user-installed skills/plugins.
- Closure path: tasks and present worker failures can trigger current replanning; no separate environment-prospecting → capability-selection → enacted adaptive change loop with a distinct S4 mandate was identified.
- Why this is / is not agent-owned: a `plan` agent or adaptive coding conversation can propose implementation steps, and Goal mode continues the same objective; neither is automatically a future-facing environmental-intelligence organ with returned organizational adaptation.
- Evidence: [interaction and Goal](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/guides/interaction.md), [custom agents](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/customization/agents.md), [Tower mode instruction](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/injection/tower-mode-full-reminder.md), [configuration](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/configuration/config-files.md).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a user could assign a strategic-research mission via Tower or configure external plugins; that user-defined application objective is not evidence of a shipped first-party S4 role.

### Absence scope

- Surfaces inspected: coding agent and subagent profiles, Goal/Plan/Swarm/Tower mode documentation, Tower coordinator/mission plan/status/review/merge code, model/provider/skills/plugin configuration and public runtime guide.
- Plausible first-party paths checked: `plan` subagent, Tower task replanning, ongoing Goal progression, web-search tooling, model switching, agent/plugin installation and experimental capabilities.
- Why no material first-party path remains: these modes continue or reorganize the current user-defined coding objective or load chosen configuration; none supplies distinct authorized environmental foresight and an adaptive organizational-capability decision fed back into current control.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational identity/policy closure at the Tower-workspace recursion was established.
- Disturbance / variety regulated: disagreements over final purpose, authority and identity could arise, but the shipped controls govern permissible tools, tasking and current integration rather than determine the ultimate organizational constitution.
- Decisive decision or feedback right: none evidenced for ratifying/changing the workspace's fundamental mission or policy through a distinct closed organizational S5 process.
- Decision owner: the user supplies objectives and can change tools, permissions and agent configuration; this does not by itself establish a first-party S5 `P` lifecycle.
- Supporting / enforcement mechanisms: main agent prompts, AGENTS.md, permission modes, Tower activation/teardown, user steering, mission goals and review/merge guardrails.
- Closure path: the user may replace the current task or turn Tower on/off, but no identity-level adjudication/ratification path into the runtime distinct from task/current-control commands is shown.
- Why this is / is not agent-owned: the word `tower`, a global mission list, main-agent instruction priority or a person retaining all permissions is not evidence that the coding harness has a separate ultimate-policy function with a returned authority lifecycle.
- Evidence: [Tower guide](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/guides/tower.md), [permission tools](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/reference/tools.md), [Tower instructions](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/packages/agent-core-v2/src/features/tower/injection/tower-mode-full-reminder.md), [interaction modes](https://github.com/MoonshotAI/kimi-code/blob/68a283894163204e93b072cef20db164015a5cad/docs/en/guides/interaction.md).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a human-led development organization using Kimi Code may possess S5 at a different recursion; its real governance was not assessed here.

### Absence scope

- Surfaces inspected: first-party mission/agent role contracts, user command and approval modes, Tower enablement, session identity and policy/configuration surfaces, S3 control and S3* review-gate roles.
- Plausible first-party paths checked: human objective replacement, explicit `/tower` control, permission rules, review approval, agent prompts, project instruction files and runtime role selection.
- Why no material first-party path remains: observed authority sets current tasks, can veto actions or changes operational configuration. No first-party constitutional identity negotiation, ratification or separate ultimate-policy decision with an enacted return path is evidenced.

## Recursion

The Tower coordinator is assessed at the software-development-workspace level, not as each isolated worker's full organization. Worker agents and reviewer agents use first-party roles but the reviewer is not reclassified as a separate S1 simply because it is a model call. Tower may be disabled or not initialized in normal Kimi print/ACP use; ownership states for the whole artifact represent the opt-in mode's reachable capabilities.

## Variety and escalation

Subagent context isolation reduces local context pressure. Tower adds conflict-specific scopes, git worktrees and ordered integration; whole-fleet status and inbox wakeups route current exceptions to the coordinator; independent reviewers examine concrete work, return findings and can block commits before merge. The user can steer or stop the fleet, while an automatic failure/merge refusal follows a documented correction path. None of those current-control or audit return paths proves forward-looking S4 or ultimate-policy S5.

## Evidence gaps

The assessment is structural and source-pinned; no real provider-backed agent mission, independent semantic adjudication or benchmark of reviewer correctness was run. Tower is experimental and opt-in but has concrete feature flags, compiled role/tool implementations, protocol stores and deterministic tests. Its normal independent-review path qualifies S3* only when a separately assigned reviewer is actually used; exceptional coordinator-submitted break-glass is not credited. S2 `A` depends on model-driven allocation/adjustment in Tower rather than worktree provision alone, and logical multi-branch conflicts can still escape simple scope isolation. The negative S4/S5 states are bounded to inspected first-party runtime surfaces.
