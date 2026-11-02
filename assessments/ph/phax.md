---
harness_id: phax
project_name: phax
repository: https://github.com/lbdremy/phax
review_ref: 3a9457a63ad8e2b6e6cd6ba63ce38366450c1499
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# phax

## Review boundary

- System in focus: phax's installed coding-work organization: phase prompts, agent provider orchestration, gates/fix sessions, plan overlap/readjustment and optional code-review sessions.
- Purpose and identity: Deliver a scoped, reviewable code change from an approved plan through gated worktree phases.
- Relevant environment: User repository, specifications/plans, files, git history, test commands and installed Claude Code/Codex/Mistral Vibe executors.
- Standard-distribution boundary: Public CLI and bundled phase/review/authoring doctrines at the pinned source, with supported installed external agent CLI as execution backend.
- Credited operating / distribution surfaces: `src/app/executePlan.ts`, `promptGeneration.ts`, `fixLoop.ts`, `reviewCode.ts`, plan overlap/readjustment, provider adapters and installed review doctrine.
- Adjacent first-party surfaces excluded from ownership: phax's own contributor agents, tests, CI/releases, project-local dogfood plans and development governance; external executors' internal metasystems.
- First-party operating / deployment modes considered: Headless phase execution, interactive stops/resume, secure/read-only review, optional automatic end-of-run review, human-driven plan adjustment.
- Recursion level: One phax-managed software-delivery project containing phase/run work cells.
- Reviewed revision: `3a9457a63ad8e2b6e6cd6ba63ce38366450c1499`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/README.md) describes approved spec→plan→phased run→review→publication. [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts) builds first-party worktree-scoped agent tasks, invokes a provider session, checks actual gate results, retries bounded fixes and persists commitments/artifacts. [src/app/promptGeneration.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/promptGeneration.ts) defines the phase actor's scope, local implementation discretion, handoff and acceptance responsibilities. [src/app/fixLoop.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/fixLoop.ts) returns real gate/protected-path failures to that actor. Providers execute the model/tool conversation; their internal capabilities are not imported as phax S2–S5.

Separate optional reviewers inspect current files/git history under a first-party review doctrine. Their sessions are read-only and worktree mutations invalidate the review. Findings and resumable reviewer sessions are persisted and surfaced to the operator. Cross-plan overlap and landed-change analysis feed a distinct interactive adjustment session; it requires developer decisions before edits. Locks, sequential phase branches, security constraints, costs and records are deterministic support.

## Operational model

Phase coding cells enact the approved task through model-selected edits/actions and gate feedback. phax supplies their task/role and corrective organization, rather than merely proxying arbitrary terminal input. External CLIs supply execution, not inferred additional VSM functions. Multiple runs may touch the same project; first-party impact analysis identifies concrete shared-file drift, but autonomous cross-run coordination requires composition. Code-review judgment is supplied as a separately instantiated first-party role; fixing findings remains an operator/current-control decision.

## S1 — Operations

- State: A
- Function: Produce scoped implementation changes and handoffs.
- Disturbance / variety regulated: Repository/task variety, gate failures, unexpected file changes and incomplete implementation.
- Decisive decision or feedback right: Choose implementation and corrective edits inside the current phase.
- Decision owner: phax's prompted phase agent, executed through its configured CLI backend.
- Supporting / enforcement mechanisms: Worktrees, provider adapters, gates, bounded fix attempts, protected paths, commits and state records.
- Closure path: Source changes produce actual gate feedback; fixLoop resumes the phase agent until success or bounded failure, then commit/handoff changes subsequent phases.
- Boundary reachability: executePlan builds the bundled phase prompt and invokes the supported provider; no developer has to invent the coding organization.
- Why this is / is not agent-owned: Removing the task agent leaves sequencing and gates but no equivalent discretionary implementation/fix choice. Executor internals are excluded.
- Evidence: [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts); [src/app/promptGeneration.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/promptGeneration.ts); [src/app/fixLoop.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/fixLoop.ts); [src/ports/backend.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/ports/backend.ts).
- Basis: structural
- Confidence: high for shipped source path.
- Caveats: Provider CLI must be installed; real model runs and outcome quality were not tested here.

## S2 — Coordination

- State: C
- Function: Attenuate cross-run shared-file overlap and stale commitments.
- Disturbance / variety regulated: One run lands changes that invalidate another plan's file assumptions or edit commitments.
- Decisive decision or feedback right: Revise affected plan commitments using concrete landed-change/overlap evidence.
- Decision owner: Developer in the shipped interactive adjustment mode; an autonomous coordination actor/right would need composition.
- Supporting / enforcement mechanisms: Deterministic overlap/impact analysis, persisted reconciliation and prompted adjustment session.
- Closure path: The adjustment procedure identifies drift, proposes a bounded plan diff, waits for approval, applies/commits it, and changes later execution's approved plan.
- Boundary reachability: Public plans-overlap/adjust-plan paths connect analysis to the bundled adjustment prompt; this is a specific coordination constructor rather than a generic mailbox.
- Why this is / is not agent-owned: Autonomous choice is not predelegated: the first-party prompt explicitly reserves every applied adjustment to the developer. C records the S2-specific constructor, not human P or automatic A.
- Distinct S1 units: Separately executed coding runs/phases represented by distinct plans at the same project recursion.
- Inter-S1 disturbance: Shared file creation/edit/deletion and stale references caused by one run's landed output relative to another run's commitments.
- Attenuating coordination relation: Concrete overlap/readjustment-impact comparison and constrained plan reconciliation.
- Feedback into subsequent S1 behaviour: Accepted edits are committed to the target plan read by later phase execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Analysis compares actual cross-run file effects with another unit's planned file commitments and exposes their corrective revision path.
- Evidence: [src/app/analyzePlanOverlap.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/analyzePlanOverlap.ts); [src/app/adjustPlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/adjustPlan.ts); [src/domain/planOverlap/adjustPrompt.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/domain/planOverlap/adjustPrompt.ts); [src/app/promptGeneration.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/promptGeneration.ts).
- Basis: structural
- Confidence: medium, constructor-level and project-relative.
- Caveats: Pure sequential phase progression and run locks are not the positive witness. Human adjustment is not published as S2=P; no autonomous cross-run coordinator is claimed.

## S3 — Inside-and-now control

- State: —
- Function: Inside-and-now control at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts); [src/app/dispatcher.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/dispatcher.ts); [src/app/decideArtifact.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/decideArtifact.ts); [src/ports/backend.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/ports/backend.ts)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts); [src/app/dispatcher.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/dispatcher.ts); [src/app/decideArtifact.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/decideArtifact.ts); [src/ports/backend.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/ports/backend.ts)
- Plausible first-party paths checked: Phase scheduling, model routing/security, cost records, per-run retries/stops, artifact decisions and operator approvals, including potential parent modes.
- Why no material first-party path remains: The inspected organization executes already-approved task commitments and bounds. No first-party whole-project current-view→resource/commitment regulation authority→returned control loop is supplied; local task/document decisions and deterministic enforcement are insufficient.


## S3* — Complementary audit

- State: A
- Function: Independently challenge the delivered code/change beyond producer handoff and routine gates.
- Disturbance / variety regulated: Passing tests or plausible phase reports while code/acceptance behavior still contains defects.
- Decisive decision or feedback right: Form evidence-backed code-review findings from current files and git history.
- Decision owner: Separately instantiated phax code-review agent.
- Supporting / enforcement mechanisms: Read-only provider session, allowed git commands, worktree before/after snapshot guard, typed finding schema, durable review/session records and operator fix hints.
- Closure path: Review findings are persisted and surfaced to current delivery control with a concrete resumable review/fix session. The native interactive review requires developer-confirmed fixes; the reviewer owns audit judgment, not the operator's acceptance/merge decision.
- Boundary reachability: reviewCodeHeadless/reviewCodeAndRecord are public CLI/runtime paths, optionally called by executePlan at run completion using the bundled review doctrine.
- Why this is / is not agent-owned: Deterministic parsing and snapshot protection do not choose defect findings. Removing the distinct reviewer preserves gates/records but removes complementary audit judgment.
- Claim being audited: That the produced code/change satisfies the intended behavior and has no material escaped defects.
- Ordinary reporting path: Phase handoffs, final report and configured gate results.
- Complementary access path: A separate session reads current code, spec/acceptance surfaces and raw git change/history with an outside-in review doctrine.
- Independence boundary: Fresh reviewer role, read-only tools and refusal/restoration on unexpected worktree mutation separate audit from the producing phase. Headless review cannot execute the product and states that limitation.
- Who acts on findings: Developer/current delivery control through surfaced findings and supported reviewer-session resumption; audit is advisory and not an automatic publication gate.
- Evidence: [src/app/reviewCode.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/reviewCode.ts); [src/domain/review/codeReviewPrompt.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/domain/review/codeReviewPrompt.ts); [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts).
- Basis: structural
- Confidence: medium-high for the supported optional code-review mode.
- Caveats: Same model family may be used; no external benchmark, live reviewer performance or forced corrective action is claimed. Routine fix-loop gate tests are not the audit witness.

## S4 — Outside-and-then intelligence

- State: —
- Function: Outside-and-then intelligence at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [README.md](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/README.md); [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts); [src/app/adjustPlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/adjustPlan.ts); [src/app/decideArtifact.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/decideArtifact.ts)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/README.md); [src/app/executePlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/executePlan.ts); [src/app/adjustPlan.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/adjustPlan.ts); [src/app/decideArtifact.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/decideArtifact.ts)
- Plausible first-party paths checked: Specs/plans, brief/context providers, code review, landed-change adjustment, model selection and skill-edit permissions; autonomous and parent adaptation alternatives.
- Why no material first-party path remains: Task authoring and code-drift correction address current delivery, not an external/future model generating organizational adaptation options that return into phax capability. Operator-selected providers or skill edits alone do not supply that closed function.


## S5 — Policy and identity

- State: —
- Function: Policy and identity at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/app/promptGeneration.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/promptGeneration.ts); [src/domain/planOverlap/adjustPrompt.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/domain/planOverlap/adjustPrompt.ts); [src/ports/backend.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/ports/backend.ts); [README.md](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/README.md)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/app/promptGeneration.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/app/promptGeneration.ts); [src/domain/planOverlap/adjustPrompt.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/domain/planOverlap/adjustPrompt.ts); [src/ports/backend.ts](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/src/ports/backend.ts); [README.md](https://github.com/lbdremy/phax/blob/3a9457a63ad8e2b6e6cd6ba63ce38366450c1499/README.md)
- Plausible first-party paths checked: Spec/plan approvals, doctrine, protected files, secure/unsafe modes, action restrictions and publication authority; possible parent identity-return path.
- Why no material first-party path remains: These define task constraints and protect operator-owned files, but no identity/ultimate-policy issue→legitimate authority decision→returned governing policy is supplied in the assessed runtime. Maintainer governance remains adjacent.


## Recursion

Phase/run nesting and provider sessions do not establish independently viable recursive organizations. The assessment credits only the declared project-level production, coordination constructor and optional audit path.

## Variety and escalation

Gate errors and actual file reconciliation retain task-local evidence; bounded retries and interactive stops preserve unresolved work for the operator. Cross-plan drift is explicitly surfaced rather than erased. Rate limits, approvals, stop states and telemetry are not themselves algedonic or higher-function evidence.

## Evidence gaps

Static pinned-source review only: no external CLI/model, cloud credentials or paid end-to-end run was invoked. Audit accuracy and provider-level read-only guarantees were not independently tested. S2=C preserves the uncomposed autonomous coordination right; developer-driven task decisions are not generalized parent S3/S4/S5 governance.
