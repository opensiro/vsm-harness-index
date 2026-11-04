---
harness_id: mariomagdy-foreman
project_name: foreman
repository: https://github.com/MarioMagdy/foreman
review_ref: 219bf0961fa4c67caaa4e371fae63e497092d9b2
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# foreman

## Review boundary

- System in focus: One accepted Foreman-managed development run, using the installed `foreman` agent skill inside a supported model-bearing agent harness, including its delegated builder/reviewer sessions, milestone/track management, owner gates and first-party coordination artifacts. The assessed product is the **composed installed skill+supported host** mode, not an unattended Python daemon alone.
- Purpose and identity: Convert a user-approved engineering plan into usable milestone increments through separately executed agent stages, independent checks and explicit owner acceptance.
- Relevant environment: Repository Git state, multiple potentially interfering code-writing agents, reviewer findings, test output, branch conflicts, changing requirements, quota and worker failures, and the human project's acceptance decisions.
- Standard-distribution boundary: `install.py` ships `SKILL.md`, harness adapter, references and delegation utilities into Claude Code or generic Codex/opencode/Gemini skill directories. The host supplies model/tool execution and model instances; Foreman supplies task roles, coordination discipline, review loops, run state and explicit authority limits.
- Credited operating / distribution surfaces: [installer](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/install.py), [Foreman operating skill](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [generic harness adapter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/harness/generic.md), [Claude adapter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/harness/claude-code.md), [manager charter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md), [gates](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/references/gates.md), [delegation](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/references/delegation.md).
- Adjacent first-party surfaces excluded from ownership: HTML tracker and sample run as display/test fixtures; Windows-only pool launcher as deterministic job execution; test simulations and `evals/study.py` as development-time comparative evaluation; optional separately installed `council-judge`, `verified-pr` or `subagent-discipline` skills; maintainers' repository governance.
- First-party operating / deployment modes considered: Default single-session foreman plus delegated stage workers and reviewers; expressly supported long-run track-mode orchestration with agent managers and builders; Claude Code and generic CLI adapters; owner acceptance and no-owner-gate defaults only where consented in the run sheet.
- Recursion level: One approved development run as an agent-managed enterprise, with stage/track builder sessions as S1 units, foreman/orchestrator as current control and human as legitimate parent where specific modes actually return decisions.
- Reviewed revision: `219bf0961fa4c67caaa4e371fae63e497092d9b2`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The small, primarily Markdown/Python repository delivers a host-agnostic agent skill: a host LLM reads the binding Foreman instructions, creates a run sheet and plan, delegates implementation to separate model-bearing agent sessions, verifies Git/test evidence, runs non-builder review gates and prepares milestone packets. The default is one management session with workers; larger efforts add a manager per parallel track, a shared event/contract folder and a Windows-specific opencode launcher (or ordinary host agent commands elsewhere). Recorded events and a live dashboard expose claims, problems and human decisions. The human confirms the run arrangement and accepts milestone merges. The installed skill is normative orchestration logic interpreted by the host model; launchers, validators, tracker and file stores alone are not agent decision owners. [README](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/README.md), [SKILL](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [generic adapter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/harness/generic.md).

## Operational model

Once the user approves the plan/run sheet, the foreman or manager chooses ready stages and appropriate builder/reviewer models, starts them in separate worktrees, reads independent source and test evidence, rules on reported problems and can send corrective briefs. Workers make coding decisions inside their assigned branch; they may not merge milestones into the base branch. Cross-track handoffs travel via one-writer coordination files/events and can cause schedule/contract reassignment. The same owner-visible tracker or chat returns substantial human staffing, gate and acceptance rulings. Autonomous and parent modes are distinguished below; merely specifying model names in a run sheet does not itself grant independent S5 authority to a run.

## S1 — Operations

- State: A
- Function: Execute concrete plan stages through separate delegated coding agents; inspect files, edit code, run tests and return evidence.
- Disturbance / variety regulated: Unpredictable implementation and test outcomes, technical obstacles, task requirements and repository state.
- Decisive decision or feedback right: Choose and implement code changes and local fixes within each stage brief; interpret tool/test feedback.
- Decision owner: The delegated model-bearing builder session, constrained by Foreman's brief, approved plan, host tools and owner safety policy.
- Supporting / enforcement mechanisms: Git worktrees, stage branches, host CLI, brief/progress/mailbox/handoff files, deterministic runner and stage gate.
- Closure path: Approved stage brief → builder model inspects repository → code edits/tests → returns handback and changes → foreman independently checks and issues accept or fix feedback.
- Boundary reachability: Both installed host adapters explicitly launch agent CLI/subagent workers in prepared worktrees; this is a normal Foreman mode, not a README-only imaginary integration.
- Why this is / is not agent-owned: Workers choose substantive code and tool behavior. Neither the launcher nor the human-written stage brief predetermines implementation decisions.
- Evidence: [SKILL stage loop](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [generic host launch instructions](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/harness/generic.md), [delegation setup](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/delegation/prepare_worktree.py).
- Basis: explicit + structural.
- Confidence: high for the supported mode; no live provider-backed run was executed here.
- Caveats: A bare installation of files into an otherwise idle CLI does nothing autonomously; the host model and owner-approved run must be active.

## S2 — Coordination

- State: A
- Distinct S1 units: Parallel builder sessions in separate stage worktrees and, in track mode, separate manager-supervised build streams.
- Inter-S1 disturbance: Two tracks editing shared contracts or dependency interfaces; premature consumption of ungated upstream stage output; quota failure cascading across shared worker/reviewer accounts; conflicting worktree integration.
- Attenuating coordination relation: Foreman designs dependency/critical-path tracks and limits effective parallelism; track managers see per-stage gate states, coordinate cross-track facts via shared append-only files and explicitly wait/rebase when provisional dependencies change. Contract changes and loosening gates must escalate to the orchestrator/owner instead of silently racing.
- Feedback into subsequent S1 behaviour: The manager inspects cross-track shared notes, dependency and gate status, adjusts when an interface changes, sends a revised builder brief or rebase/test requirement, and can hold a stage pending the responsible decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The path addresses observed *inter-worker interference* over shared contracts, concurrent write ownership and ungated dependency consumption, and returns corrective replanning to affected workers; the event store itself is support only.
- Function: Attenuate collisions and timing conflicts among simultaneously acting stages and tracks.
- Disturbance / variety regulated: Incompatible contracts, premature downstream commitments, concurrent file ownership and shared-model quota contention.
- Decisive decision or feedback right: Tighten the stage dependency/contract handling, defer or provisionally start work, require rebase and re-verification, reroute workers after a shared-resource failure.
- Decision owner: Foreman/orchestrator model in the default mode and autonomous track-manager model under its approved charter in track mode.
- Supporting / enforcement mechanisms: One-writer track files, append-only shared notes, gate IDs, milestone branches, worktrees and launcher capacity limits.
- Closure path: Conflicting dependency/worker state → manager detects and records the shared issue → chooses reordering or corrective contract handling → affected worker brief/ready state changes → gate verifies the resolved output.
- Boundary reachability: Track mode is a supported built-in mode selected for sufficiently wide runs, and charter, event contracts and host adapters are shipped and installed. It requires an active host model, not an unshipped external coordinator.
- Why this is / is not agent-owned: The manager model chooses how to respond to cross-track disturbances; worktree isolation and deterministic launcher limits do not themselves make the corrective decision.
- Evidence: [architect pass/concurrent track rules](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [manager coordination/contract escalation](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md), [harness adapter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/harness/generic.md).
- Basis: explicit + structural.
- Confidence: medium; the prescribed return path is clear, but a live collision-recovery replay was not performed.
- Caveats: Single-stage runs need no inter-unit S2. Strict contract changes remain human/orchestrator-authorized, not discretionary manager edits.

## S3 — Inside-and-now control

- State: A(P)
- Whole-system current view: Foreman maintains the approved plan, all milestone/stage dependencies, worktree/branch state, per-gate evidence, worker handbacks, open questions and the tracker. The human can view the same run and answer its staffing and acceptance questions.
- Current-control decision scope: Select critical path and parallel tracks, assign workers and reviewers, schedule and retry stages, choose corrective briefs and alternate models; the parent separately approves resource/role arrangements and controls milestone integration.
- Function: Govern active stage and team commitments so independent outputs form a single usable milestone.
- Disturbance / variety regulated: Missing dependencies, failed tests, worker hang/quota, resource pressure, reviewer objections, owner priorities and integration seams.
- Decisive decision or feedback right: Autonomous mode allocates stage assignments and fix rounds under standing orders; parent mode accepts or changes the run sheet's model staffing, resource caps, branch authority and release of the current milestone.
- Decision owner: Foreman/orchestrator or track-manager model for authorized current work; human owner for the approved run's global staffing/constraints and milestone acceptance.
- Supporting / enforcement mechanisms: Run sheet, `plan.yaml`, briefs, `staffing.yaml`, gates, worktrees, tracker, events and launcher signals.
- Closure path: Current run/worker evidence → foreman selects commitments or fallback → worker/branch state changes and reports back; parent reviews proposed staffing/plan in run sheet or a milestone packet → approval/changes enter standing orders and govern subsequent workers/merges.
- Boundary reachability: Both Foreman's autonomous stage loop and owner-approved run-sheet/milestone gate are mandatory operating paths in the installed skill; the parent return path has explicit `decision`/`answer` events, not a mere UI button.
- Why this is / is not agent-owned: Model-controlled work allocation establishes the autonomous base; the human's explicit approval of staffing and ongoing milestone integration supplies a distinct legitimate parent control mode.
- Evidence: [architect pass/run sheet](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [manager current-control charter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md), [owner gate return](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/references/gates.md).
- Basis: explicit + structural.
- Confidence: medium-high, with no claim of measured staffing quality.
- Caveats: The parent mode is not inferred from a generic PR merge button; it includes pre-run resource allocation and explicit run-level choices consumed by the whole manager and workers.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Foreman/manager model | Active stage dependencies, gate feedback, failed worker | Reallocation/fix brief affects actual worker and branch commitments | [stage loop](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [charter](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md) |
| Parent (`P`) | Human run owner | Proposed run sheet/staffing/authority, milestone readiness | Owner answer is logged and governs current work and permitted merges | [setup and acceptance](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [human gate](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/references/gates.md) |

## S3* — Complementary audit

- State: A
- Claim being audited: Builder's assertion that a stage/milestone satisfies test criteria and that its PR is ready to merge.
- Ordinary reporting path: Builder writes a DONE/UNSURE/BLOCKED handback and commits source changes to its stage branch.
- Complementary access path: Non-builder Foreman/track manager inspects Git status/diff, runs actual tests and probes the app independently; a separate reviewer model reads the change and criteria at stage and milestone gates, recording findings before fixes.
- Independence boundary: The verifier/reviewer is explicitly forbidden to be the original builder for that stage; raw repository/test evidence is available rather than solely the worker's narrative. In track mode the manager never builds; reviewer routing is separated by role.
- Who acts on findings: Foreman/manager rules on each finding, writes a new fix brief, dispatches it to the implementation worker, and re-verifies the changed result; owner receives the integrated packet.
- Function: Challenge and correct produced work using complementary evidence under a non-builder decision right.
- Disturbance / variety regulated: False builder-success claims, hidden integration failures, unnoticed branch changes and ineffective fixes.
- Decisive decision or feedback right: Independent verifier/reviewer judges actual changes, issues an accept/fix verdict and sends corrective findings.
- Decision owner: Model-bearing Foreman or track manager and separately dispatched non-builder reviewer; deterministic tests provide data, not the autonomous finding decision.
- Supporting / enforcement mechanisms: Git diffs, stage tests, review gates, fixed test hashes, PR comments, independent verifier briefs and re-review.
- Closure path: Builder handback → independent raw-code/test inspection → reviewer findings and foreman rulings → new fix assignment → raw-diff re-check → gate passes or escalates.
- Boundary reachability: SKILL stage loop and first-party gate reference require the non-builder and actual source/test paths in the installed, user-approved Foreman operation; optional third-party reviewers are not needed.
- Why this is / is not agent-owned: An agent other than the producer interprets complementary evidence and chooses corrective findings; neither CI green nor self-reported builder status is substituted for that judgment.
- Evidence: [independent verification/gate loop](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [gate criteria/reviewer](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/references/gates.md), [manager not-builder rule](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md).
- Basis: explicit + structural.
- Confidence: high for prescribed independent evidence access and corrective return, without empirical reliability claims.
- Caveats: A separately installed `council-judge` skill is optional; this claim rests on core Foreman non-builder review, not on that optional dependency.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed prospective scanning/learning-and-adaptation function separate from executing and correcting this run is established.
- Disturbance / variety regulated: Changing future product/environment demands are discussed in planning, but not autonomously converted into durable future organization capability.
- Decisive decision or feedback right: Choosing future changes to operating repertoire after observing outside trends; no such first-party durable decision owner found.
- Decision owner: Foreman performs task-specific planning and post-gate fix loops; human can change local defaults or create a new run, which does not by itself establish S4 return.
- Supporting / enforcement mechanisms: Run sheets, `LOCAL.md`, optional explore spikes, study scripts, reports and retrospective observations.
- Closure path: Fix rounds adapt present work; new-run policy/workflow adoption from prospective intelligence is not an installed closed loop.
- Why this is / is not agent-owned: Model-mediated adaptation *inside* current stages is S3; comparison-eval reports and owner-made future ideas are adjacent development surfaces.
- Evidence: [explore and run lifecycle](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [study evaluator](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/evals/study.py), [local overlay example](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/LOCAL.md.example).
- Basis: structural + explicit.
- Confidence: medium-high for the declared installed-run boundary.
- Caveats: External owner may deliberately learn from final reports across runs, but no first-party binding feedback/update of future capability is established.

### Absence scope

- Surfaces inspected: Foreman plan and stage loop, explore milestones, fallback/criteria rules, local overlay, study evaluator, gate results and run-state persistence.
- Plausible first-party paths checked: Explore spikes as future research; `evals/study.py` as adaptive training; corrective fix briefs as learning; owner-editable `LOCAL.md` as recurrent policy update.
- Why no material first-party path remains: Explore work and fixes serve current approved deliverables; study evaluates the *skill in development*, not live-run outside/future intelligence; no runtime loop automatically or parent-governedly applies such findings to future organization capability.

## S5 — Policy and identity

- State: —
- Function: The installed run has task and authority rules, but no separate first-party ultimate identity/policy decision-and-return loop beyond its current plan/control is demonstrated.
- Disturbance / variety regulated: Changes in owner task/scope, permission, gate strictness and model staffing are handled in S3; no independent self-definition/governance cycle is established.
- Decisive decision or feedback right: Alter the enterprise's ultimate purpose, membership constitution or binding identity-policy rather than scheduling this project; no distinct runtime S5 owner/return found.
- Decision owner: The owner chooses the project and run settings; Foreman applies a fixed normative skill identity and approved standing orders without autonomous ultimate-policy revision.
- Supporting / enforcement mechanisms: Run sheet, `LOCAL.md` house rules, immutable role charters, owner question/decision events and deployment gates.
- Closure path: Task-specific authorization and policy enforcement enter S3 commitments; a separate identity/policy correction returned to changed future operation is not established at the stated run recursion.
- Why this is / is not agent-owned: Model-facing skill rules prohibit self-upgrading merge/prod powers, and humans changing ordinary project constraints are not automatically ownership of organization-level S5.
- Evidence: [fixed Foreman identity and standing rules](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/SKILL.md), [local overlay](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/LOCAL.md.example), [manager authority limits](https://github.com/MarioMagdy/foreman/blob/219bf0961fa4c67caaa4e371fae63e497092d9b2/track-mode/CHARTER.md).
- Basis: structural.
- Confidence: medium; bounded to the installed project-run organization.
- Caveats: S5 would require stronger source evidence of an authoritative identity/purpose decision, not merely a user-gated code merge or configurable agent role.

### Absence scope

- Surfaces inspected: Run sheet, standing orders, default settings, project owner gates, manager charters, local rules and terminal review packets.
- Plausible first-party paths checked: Owner-approved standing rules as a parent S5 mode; mutable role descriptions as identity authority; human milestone gate as ultimate policy; arbitrary skill changes by maintainers.
- Why no material first-party path remains: These change task-control boundaries, execution authority and current resource choices, or modify the skill's development source outside the installed run. No distinct ongoing policy/identity constitutional correction loop at the assessed recursion was found.

## Distributed OSS parent arrangement

Different OSS users install separate copies of Foreman; contributor collaboration and maintainers' release decisions do not form a shared runtime parent organization. The assessed parent mode concerns the owner of an individual approved run and its working team, not global governance of Foreman installations.

## Self-hosted and non-human modes

Supported generic CLI and Claude Code deployments leave execution to locally running host agents. The foreman operates autonomously *after* plan/run-sheet approval but cannot make the owner's milestone/base-branch acceptance decision. Human review changes S3 authority in the supported run; it is not a license to infer parent ownership in every other function.

## Recursion

Each builder session carries its own local tool loop and task scope; track managers control distinct groups. The overall run is one higher-level organization; stage workers and managers do not each demonstrate full independent S1–S5 capability.

## Variety and escalation

Worktree isolation, dependency gates and one-writer coordination streams reduce inter-agent interference. Reviewer findings return through rulings and fix briefs. Worker `BLOCKED`, repeated reviewer failure, contract weakening, exhausted quota and budget overruns escalate to the orchestrator or human owner; the existence of these hard stops is enforcement support, not a second S5 owner.

## Evidence gaps

- Reviewed pinned first-party docs, harness adapters, launcher/charter and local source, but did not execute an authenticated provider-backed, multi-agent, cross-track collision/recovery run at this ref.
- Conditional track-mode S2 witnesses are supported first-party installed paths, not a claim that every small Foreman run has multiple simultaneously active S1 workers.
- Reviewer independence is prescribed in source and materially supported by separate workers and raw evidence; no blinded observational success-rate claim is made.
