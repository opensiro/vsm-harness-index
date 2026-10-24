---
harness_id: workbench
project_name: Workbench
repository: https://github.com/proactive-agent/workbench
review_ref: 4dbda41ac47809ce74ebc39408183c428ec55436
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Workbench

## Review boundary

- System in focus: the shipped Workbench desktop application, at immutable `4dbda41ac47809ce74ebc39408183c428ec55436`, operating a board of coding tasks and isolated Git worktrees through an installed Claude Code CLI.
- Purpose and identity: allow a human project owner to dispatch concurrent Claude Code development sessions and review changes before merging, with automated model/effort triage, plan/implementation/validation phases, accounting, resume, conflict resolution, and shared project memory.
- Relevant environment: local developer workstation, Electron app, user Git repositories, installed `claude` executable and provider account, task files/worktrees, optional integrations and MCP servers, reviewers and project owner.
- Standard-distribution boundary: first-party `src/main` Electron task/agent manager, worktree and merge infrastructure, first-party triage prompts and Claude Code subprocess wrappers, event/state records and optional memory relocation; the autonomous coding and tool-selection loop **inside Claude Code** is external, even when instructed by first-party phase prompts.
- Credited operating / distribution surfaces: `src/main/agent`, `src/main/claude-code`, `src/main/worktree`, `src/main/ai/merge`, `src/main/ai/runners`, `src/main/self-improve`, `src/main/live-agent`, app README and tests.
- Adjacent surfaces excluded from ownership: Claude Code's proprietary CLI, native tools, model context, tool loop, agent teams, self-review cognition and auto-memory generation; developer test mocks and human review/merge judgments also cannot be credited as Workbench-owned autonomous functions.
- First-party modes examined: project task triage; automatic/forced planning; implementation, validation and reviewer-revision task phases; isolated or direct checkout execution; multiple tasks in parallel; graph/memory prompting; pull request/merge conflict resolution; terminal/live-agent relay; manual review and merge.
- Recursion level: Workbench's own orchestration application, *not* the wider deployment in which externally installed Claude Code instances can be modeled as separate S1s.
- Reviewed revision: `4dbda41ac47809ce74ebc39408183c428ec55436`.
- Observation date: 2026-10-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

Workbench's README explicitly states that it *runs on Claude Code rather than competing with it*. `AgentManager` prepares worktrees and passes a task to `ClaudeTaskRun`. That runner selects a fixed or model-derived triage, optionally asks for a plan, calls an implementation phase, asks the same Claude session to verify/commit, and lets a human request revisions. The central adapter `startClaudeProcess` runs `claude -p`, streams JSON tool/result messages, and resumes the external session. Its first-party callbacks log, persist and display what Claude did; they do not choose the next substantive coding tool from an observation.

There are genuine first-party decisions around the outsourced session: `triageTask` prompts a *short separate Claude Code run* to select a model, effort, planning switch, scope and verification commands; `AgentManager` maintains run/profile state; Git worktree machinery isolates tasks; merge tooling performs deterministic conflict detection, attempts line-preserving merges and can launch a dedicated Claude Code merge agent. These controls are substantial, but agentic coding, arbitrarily iterative merge edits and open-ended validation remain inside spawned Claude Code processes. A model returning one bounded triage answer does not give the Workbench parent its own operational action/tool/feedback loop.

The optional **self-improve** feature relocates Claude Code's own auto-memory to shared project memory and injects a prompt asking Claude to save preferences learned from its sessions. The code documents this as Claude Code's auto-memory with a different shared location and nudge, not a Workbench-owned prospective strategy-generation/adoption actor. A transcript backfill is another bounded Claude Code call producing memory candidates. The README's value claim about compounding learning is acknowledged but not equated with S4.

Pinned primary evidence:

- [`README.md`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/README.md) — product identity, external Claude Code dependence, human review, triage and project learning.
- [`src/main/claude-code/process.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/process.ts) — spawning `claude -p` and handling streamed external events.
- [`src/main/claude-code/task-runner.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/task-runner.ts) — phase orchestration, external session resume and instruction prompts.
- [`src/main/claude-code/triage.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/triage.ts) and [`run-text.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/run-text.ts) — bounded first-party prompt composition; Claude Code subprocess is the evaluator.
- [`src/main/agent/agent-manager.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/agent/agent-manager.ts) — per-project task lifecycle and event forwarding.
- [`src/main/ai/merge/orchestrator.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/ai/merge/orchestrator.ts) and [`src/main/ai/runners/merge-agent.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/ai/runners/merge-agent.ts) — deterministic merge strategy and externally executed Claude agent for hard conflicts.
- [`src/main/self-improve/index.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/self-improve/index.ts), [`memory-writer.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/self-improve/memory-writer.ts) — Claude memory relocation and file persistence.

## Operational model

Human creates task → Workbench assigns an isolated worktree and triages it using a constrained `claude -p` call → Workbench launches and resumes the external Claude Code planning, implementation and validation tool loops → stream events, commits and cost are stored for the task board → human reviews and approves changes; optional conflict management invokes another Claude run. First-party controls supply lifecycle and shared state, not an independent alternative agent capable of selecting coding actions after tools return.

## S1 — Operations

- State: —
- Function: first-party autonomous open-ended coding work is absent at the declared Workbench boundary.
- Disturbance / variety regulated: arbitrary coding ambiguities, failed checks, tool feedback and repository changes are handled by the installed Claude Code agent; Workbench handles process status, settings, worktree isolation and phase transitions.
- Decisive decision or feedback right: interpret actual tool outputs and select or revise the next substantive code edit/test action.
- Decision owner: external `claude -p` session, explicitly named by first-party runner; triage decisions are bounded setup choices, not the task execution loop.
- Supporting / enforcement mechanisms: `ClaudeTaskRun`, prompts, JSON schemas, process streaming, event state, worktree manager and resume/revision controls.
- Closure path: Workbench launches a configured phase → Claude Code privately performs model/tool/observation recurrence → Workbench records and forwards the result, optionally initiating the next configured phase.
- Why this is / is not agent-owned: first-party code delegates model-driven tool choice to an installed executable and never implements a substitutable observation-to-next-action coding loop.
- Evidence: [`task-runner.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/task-runner.ts); [`process.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/process.ts); [`triage.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/triage.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a real deployed Workbench + Claude installation is an agentic application; its autonomy belongs to a composed boundary, not the repository-local first-party boundary selected for Index admission.

### Absence scope

- Surfaces inspected: CLI subprocess adapter, task/triage/plan/implement/validate lifecycle, model/effort routing, merge agent and task manager.
- Plausible first-party paths checked: multi-phase task runner as S1, triage's read-only model decision as an operating loop, external process streaming as adaptive next-action selection, merge agent as owned coding actor.
- Why no material first-party path remains: each open-ended model/tool recurrence is performed inside `claude -p`; first-party Workbench owns wrappers, restricted decisions and data/control plumbing.

## S2 — Coordination

- State: —
- Function: substantial conflict/worktree coordination exists, but multiple first-party autonomous Workbench S1 units are not established at this recursion.
- Disturbance / variety regulated: concurrent tasks may alter overlapping files or collide at merge time.
- Decisive decision or feedback right: regulate conflicts between owned operational agents based on live joint work state.
- Decision owner: first-party deterministic worktree/conflict logic and external Claude merge subprocess; human decides when and whether to merge.
- Supporting / enforcement mechanisms: isolated branches, touched-file changelog in task prompts, file-evolution tracker, conflict detector, auto-merger and merge-agent fallback.
- Closure path: concurrent external Claude tasks → Workbench tracks branch/file overlap and merges or requests another external Claude conflict resolution → human reviews outcome.
- Why this is / is not agent-owned: coordination serves Claude Code actors whose operational loops are not Workbench-owned S1; file isolation and merge helpers cannot establish that missing local plurality.
- Evidence: [`agent-manager.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/agent/agent-manager.ts); [`orchestrator.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/ai/merge/orchestrator.ts); [`merge-agent.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/ai/runners/merge-agent.ts).
- Basis: structural absence at declared recursion.
- Confidence: high.
- Caveats: composed-system assessment could credit these mechanisms as S2 support over externally provided Claude S1s, given a separately declared boundary.

### Absence scope

- Surfaces inspected: worktree isolation, task parallelism, changed-file notifications, merge orchestration, conflict resolution and human review.
- Plausible first-party paths checked: branch isolation as S2, task collision warnings as coordination policy, AI merge conflict resolution as adaptive inter-S1 management.
- Why no material first-party path remains: no pair of Workbench-owned open-ended S1 units exists; independent action decisions are delegated to Claude Code.

## S3 — Inside-and-now control

- State: —
- Function: no closed Workbench-owned whole-current portfolio control over its own S1 units is established.
- Disturbance / variety regulated: per-task model cost, rate limits, task states and project concurrency are measured or rule-managed.
- Decisive decision or feedback right: revise whole-current allocation, ordering or composition of operational units from observed portfolio feedback.
- Decision owner: human project owner chooses work and priorities; Workbench triage selects an individual task's model/effort, not a revising project portfolio.
- Supporting / enforcement mechanisms: task board and run ledger, Claude account rotation on rate limits, fixed retry bounds, per-task budget, triage prompts and status events.
- Closure path: human selects task → one bounded model/effort choice → Claude Code executes; feedback populates task status rather than a first-party adaptive whole-current resource decision.
- Why this is / is not agent-owned: a board, bounded per-task routing and automatic profile swaps are not themselves discretionary portfolio management closure.
- Evidence: [`agent-manager.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/agent/agent-manager.ts); [`triage.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/triage.ts).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: humans do act as managers in the deployed product; the frozen first-party automatic workflow does not demonstrate a separate S3=P closing over first-party S1s.

### Absence scope

- Surfaces inspected: board, event state and budget summaries, dynamic profile swap, task triage and settings.
- Plausible first-party paths checked: per-task triage as S3, rate-limit continuation as S3, human board as S3=P, parallel task state as portfolio management.
- Why no material first-party path remains: these are configured per-task lifecycle mechanisms; no whole-current first-party S1 portfolio is autonomously reorganized in response to feedback.

## S3* — Complementary audit

- State: —
- Function: validation phase and PR/merge checks do not demonstrate a complementary independent audit actor over Workbench-owned production S1.
- Disturbance / variety regulated: failing tests, wrong diffs, merge losses, misreported task success.
- Decisive decision or feedback right: inspect an operating unit's substantive output independently and feed corrective challenge into its production loop.
- Decision owner: the *same* Claude Code session resumes to validate its own changes; separate merge/run utility also invokes installed Claude Code, while human is final reviewer.
- Supporting / enforcement mechanisms: `VALIDATION_SCHEMA`, built-in `/code-review` or Claude subagent instructions, project test commands, PR merge verification and human review gate.
- Closure path: same external Claude session implements then validates → Workbench records report and awaits human review; reviewer feedback invokes another Claude phase, not a first-party independent evidence judge.
- Why this is / is not agent-owned: phase label `validate` and a prompted subagent do not establish Workbench-controlled independent audit ownership or evidentiary separation.
- Evidence: [`task-runner.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/task-runner.ts); [`merge-agent.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/ai/runners/merge-agent.ts).
- Basis: structural absence.
- Confidence: high.
- Caveats: ordinary project tests and human review may be strong controls; they are not counted as a separate autonomous S3* here.

### Absence scope

- Surfaces inspected: task validation schema, shared Claude session, reviewer revision, project test records and merge verification.
- Plausible first-party paths checked: Claude self-review as independent S3*, auto-merge tests as audit, human reviewer as runtime S3*=P and isolated merge-agent prompt as independent auditor.
- Why no material first-party path remains: validation remains inside external Claude cognition or deterministic test/gate machinery; no first-party independent audit/return owner was found.

## S4 — Outside-and-then intelligence

- State: —
- Function: first-party prospective environmental sensing, alternative capability generation and adopted future strategy loop not established.
- Disturbance / variety regulated: developer preferences, recurring mistakes, tooling lessons and model/skill availability can change over time.
- Decisive decision or feedback right: evaluate longer-horizon opportunities and adopt a changed future tool/capability repertoire for the organization.
- Decision owner: external Claude Code's own auto-memory, prompted by Workbench, decides what to learn; user enables/disables sharing and chooses capabilities.
- Supporting / enforcement mechanisms: `SELF_IMPROVE_NUDGE`, shared `.workbench` memory paths, Claude-format `MEMORY.md` and topic files, transcript backfill and persistent settings.
- Closure path: Claude session may save preferences → Workbench stores/relocates memory file → later Claude sessions may read it; no Workbench-owned prospective strategy evaluation and adoption decision is shown.
- Why this is / is not agent-owned: useful persistent task memory is not equivalent to S4, particularly when recognition and writing of the lessons is delegated to Claude Code's own memory actor.
- Evidence: [`index.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/self-improve/index.ts); [`memory-writer.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/self-improve/memory-writer.ts); [`backfill.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/self-improve/backfill.ts).
- Basis: explicit + structural absence.
- Confidence: high for attribution; medium for downstream learning effectiveness (not tested).
- Caveats: the memory feature may materially improve user productivity, which this assessment does not measure.

### Absence scope

- Surfaces inspected: self-improve settings, project memory relocation, memory format/writes, transcript backfill and task prompts.
- Plausible first-party paths checked: persistent preferences as S4, backfill as first-party learning, prompt-based Claude memory as independent external intelligence and task triage as strategy adoption.
- Why no material first-party path remains: no separately owned future-oriented alternative generation, adoption authority and changed organizational capability loop exists in first-party code.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy adjudication loop over an autonomous Workbench organization established.
- Disturbance / variety regulated: task scope, isolation, shell permissions, publishing restrictions, human review authority and provider account selection.
- Decisive decision or feedback right: decide ultimate project identity or resolve conflicting legitimate highest-level policies and return an authoritative ongoing ruling.
- Decision owner: human developer/user sets tasks and approves merges; fixed Workbench prompts and execution settings enforce chosen constraints; external Claude still owns its native tool permissions.
- Supporting / enforcement mechanisms: worktree permission mode, instructions prohibiting push/deploy, human merge gate, per-task caps and provider profile settings.
- Closure path: human sets work policy → Workbench passes prompts and settings → external Claude executes within (or subject to) them → final acceptance returns to human; no first-party identity policy deliberation/adoption actor.
- Why this is / is not agent-owned: hardcoded safety instructions or user approval gates do not instantiate an autonomous ultimate-purpose governor.
- Evidence: [`task-runner.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/claude-code/task-runner.ts); [`agent-manager.ts`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/src/main/agent/agent-manager.ts); [`README.md`](https://github.com/proactive-agent/workbench/blob/4dbda41ac47809ce74ebc39408183c428ec55436/README.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: the practical human governance of the deployed product is not being denied; repository-local first-party ownership is the assessment criterion.

### Absence scope

- Surfaces inspected: task permission modes, user review/merge controls, budgets, project settings, phase system prompts and provider profiles.
- Plausible first-party paths checked: owner as S5=P, prompt prohibitions as S5 policy, Claude permissions as Workbench authority, project identity in settings as ultimate policy.
- Why no material first-party path remains: these controls constrain external execution, without implementing a first-party top-level policy conflict judgment and authoritative policy feedback loop.

## Recursion

Workbench is a useful human-supervised orchestration layer above external Claude Code workers. If a *composed* deployment includes multiple separately modeled Claude Code agents, Workbench's worktrees, triage, retries and merge controls may be analyzed as coordination structures at the next recursion. The Index row assesses this application's own shipped agentic function ownership, so autonomy of a separately installed Claude Code agent cannot be reassigned by integration alone.

## Variety and escalation

Workbench attenuates task/process variety through model/effort triage, phase schemas, spend limits, concurrent worktree isolation, task-aware changelog, status recovery and merge gates; it amplifies usable parallel development capacity by staging several external Claude sessions. Human review is the final merge escalation. These substantive features are documented even though they do not close the first-party agentic VSM loops.

## Evidence gaps

- Repository frozen by commit and assessed source-first; no Claude Code/model/LLM session was launched, no user-facing task outcome quality was benchmarked.
- Workbench's own README explicitly places autonomous coding in installed Claude Code; source independently confirms spawn/stream/resume rather than a replacement agent loop.
- Self-improve was checked separately: it reuses Claude Code auto-memory and bounded Claude backfill; effectiveness and future revisions are outside this frozen assessment.
- Proposed canonical disposition after review: `excluded-no-agentic-vsm`, vector `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.

## Assessment summary

At the frozen repository-local boundary Workbench does not own the autonomous coding action/tool/feedback loop or a corresponding higher-level first-party agent organization. It is nevertheless a substantial desktop orchestration and persistence product around Claude Code, with bounded AI triage, parallel worktrees and optional shared external auto-memory. The suggested `excluded-no-agentic-vsm` status is about first-party Index admission, not an assertion that Workbench cannot run autonomous agents as a composed deployment.
