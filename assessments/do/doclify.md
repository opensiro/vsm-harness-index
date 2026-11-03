---
harness_id: doclify
project_name: Doclify
repository: https://github.com/shreyas-dhakal/doclify-harness
review_ref: 67714ce9c24adf726f3d30ea35ce7afe9c249b4f
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Doclify

**Canonical disposition:** `excluded-no-agentic-vsm` after first-party operating-boundary inspection. This is not a claim that its session capture, evidence extraction, review-gated documentation or future-agent context do not work. Its delivered outcome is a supervised documentation memory overlay for *externally run* coding agents, with no own autonomous operational agent S1.

## Review boundary

- System in focus: Doclify's installed Rust CLI/hooks, capture queue, constrained documentation-model inference, human review and accepted-record context handoff.
- Purpose and identity: Extract proposed documentation from real Codex/Claude session evidence and return *human-reviewed* requirements/decisions to later sessions.
- Relevant environment: Source repository and worktree, installed coding-agent transcripts, hook/trust configuration, provider output, local accepted/proposed records and subsequent external agent sessions.
- Standard-distribution boundary: `doclify init` registers hooks inside separately installed Codex/Claude; `sync` captures sessions and runs one constrained model extraction per event; an operator accepts/rejects proposals; `SessionStart` exposes accepted records as context. Doclify does not itself instantiate a code-writing agent loop.
- Credited operating / distribution surfaces: [README.md](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/README.md), [capture hooks](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-capture/src/hook.rs), [hook installer](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-capture/src/install.rs), [pipeline](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [structured extraction](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/model-bridge/src/providers.rs), [context builder](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-context/src/lib.rs).
- Adjacent first-party surfaces excluded from ownership: Independently installed Codex/Claude model/tool cognition; docs/live-verification's host-controlled coding-agent tasks, test fixtures, UI viewer, deployment/CI and human Git workflows.
- First-party operating / deployment modes considered: Claude constrained extraction with existing CLI login, configured OpenAI-compatible API extraction, Codex transcript capture (its documentation-model bridge disabled), hook-based accepted context on future Claude/Codex sessions, interactive `review`/`handoff`/`docs`.
- Recursion level: One local repository-level documentation evidence/approval overlay. Attached external agent sessions are not first-party Doclify operational units.
- Reviewed revision: `67714ce9c24adf726f3d30ea35ce7afe9c249b4f`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Hooks observe separate coding-agent sessions and enqueue transcript-derived events. A pipeline processes pending work serially, invoking constrained Claude CLI or a configured API for structured proposal JSON. Source citation and schema validation reject unsupported or stale claims; the model may only return `review: proposed`. The human explicitly accepts a selected version before the local records become settled requirements or decisions. Later `SessionStart` hooks assemble a bounded context from reviewed records; the builder itself performs no model call. Doclify never launches/owns the external Codex or Claude engineering work loop. [README.md](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/README.md), [pipeline](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [context builder](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-context/src/lib.rs), [live verification](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md).

Counterfactual owner test: remove externally installed Codex/Claude *coding agent* loops while retaining Doclify's capture/records/viewer, JSON model provider and hook code. The remaining system can classify previously captured text into doc proposals, validate evidence and serve approved context, but cannot observe a source repository, choose its next engineering tool action, execute/repair code and close a substantive coding task. The LLM documentation response is a bounded structured inference, not an autonomous multi-step operational worker. Removing the human reviewer leaves *unapproved* proposals, not an autonomous implementation mode. This source-first distinction supports exclusion, not dismissal of useful governance infrastructure.

## Operational model

External agent session → Doclify hook event/transcript queue → one bounded documentation inference → validator and record proposal → human review/acceptance → future hook context sent to another externally run agent. All material operational code-writing decisions still belong to the external coding agent and its human user; extraction/capture and approval logic do not become a first-party agent organization. [live verification](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md), [providers.rs](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/model-bridge/src/providers.rs).

## S1 — Operations

- State: —
- Function: Autonomous adaptive software/documentation execution would select and revise meaningful task actions from tool/environment feedback.
- Disturbance / variety regulated: Captured transcript facts, partially observed requirements and repeated documentation claims are handled by extraction/validation and human review.
- Decisive decision or feedback right: Choose further task/tool actions after observing actual results and close the operational objective; no first-party Doclify owner.
- Decision owner: Separate Codex/Claude coding agents select engineering tool actions; Doclify's structured extraction model proposes records only and cannot accept them or drive the original work.
- Supporting / enforcement mechanisms: Hooks, durable queue, constrained provider request, proposal schema/citation checks, human review and context injection.
- Closure path: A captured event gets one JSON proposal pass and deterministic validation, then waits for human acceptance; any later coding action occurs in a different external agent session.
- Why this is / is not agent-owned: The model classifies/generates proposed documentation but does not iteratively select tools or adjust a task on execution feedback. Its outcome cannot itself become accepted without a human.
- Evidence: [pipeline](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [structured instruction](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/model-bridge/src/documentation.rs), [providers.rs](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/model-bridge/src/providers.rs), [live verification](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md).
- Basis: explicit + structural negative.
- Confidence: high at the pinned standard distribution.
- Caveats: Verified external Codex/Claude sessions and real model extraction do occur, but neither gives Doclify independent semantic operational S1 ownership.

### Absence scope

- Surfaces inspected: Installed capture hooks, pipeline extractor, model bridge, review store, handoff context, CLI commands and live guest-checkout evidence.
- Plausible first-party paths checked: Claude constrained model extraction, OpenAI-compatible extraction, Codex capture, future session context, user review and recovery worker.
- Why no material first-party path remains: No supported path creates and controls a model-bearing operational task agent that can observe tool results and revise own next action; bounded doc inference and external agent attachment are distinct.

## S2 — Coordination

- State: —
- Function: No first-party attenuation of interference between distinct autonomous S1 units is established.
- Disturbance / variety regulated: Multiple captured sessions and near-duplicate proposals are data-quality/queue issues, not conflicting live agent commitments.
- Decisive decision or feedback right: Interpret an inter-S1 collision and return changed mutual commitments; absent.
- Decision owner: Queue is a deterministic single-writer processor; human adjudicates proposed documents, and external agent hosts own their runs.
- Supporting / enforcement mechanisms: Hook ownership, queue locking, duplicate-target guards, per-record revision and source evidence validation.
- Closure path: Duplicate or stale proposal is rejected/retained for review; no model-based inter-agent coordination returns into both workers' behaviour.
- Why this is / is not agent-owned: Shared documentation and serial extraction are not peer S1 collision attenuation or adaptive coordination.
- Evidence: [pipeline](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [capture queue](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-capture/src/queue.rs), [live verification limitations](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md).
- Basis: structural.
- Confidence: high.
- Caveats: Two independent external agent users may read the same reviewed context, but Doclify does not regulate their simultaneous task collisions.

### Absence scope

- Surfaces inspected: Capture queue, pipeline serial processing, multi-session hooks, cross-worktree context merge and review versions.
- Plausible first-party paths checked: Shared requirements, independent agent sessions, duplicate proposals, record conflicts and recovery.
- Why no material first-party path remains: These are evidence/record consistency concerns without distinct first-party S1 workers or an inter-worker response-and-return relation.

## S3 — Inside-and-now control

- State: —
- Function: No current whole-agent-organization resource/commitment control loop is evidenced.
- Disturbance / variety regulated: Queue health, stale sessions and review status are local documentation workloads, not S1 organizational commitments.
- Decisive decision or feedback right: Allocate or reassign current work/resources among autonomous S1 workers; absent.
- Decision owner: Human determines which documentation proposals become accepted; external Codex/Claude/human determine coding task priorities, while Doclify processes its queue mechanically.
- Supporting / enforcement mechanisms: `sync`, queue ack/pending states, `status`, review prompts, document records and handoff selection.
- Closure path: Captures are processed into proposals and displayed for acceptance; no whole-system current-control decision changes a portfolio of model-owned S1 work.
- Why this is / is not agent-owned: Human approval of individual document records does not imply parent S3 over an autonomous Doclify operation.
- Evidence: [README.md](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/README.md), [pipeline](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [domain](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-domain/src/lib.rs).
- Basis: structural.
- Confidence: high.
- Caveats: External user/team coordination can use accepted docs but is not Doclify-owned S3.

### Absence scope

- Surfaces inspected: CLI review/status commands, record authorization, queue scheduling, session hooks and handoff context.
- Plausible first-party paths checked: Human reviewed decisions, repository/project scope, model-generated tasks and background recovery.
- Why no material first-party path remains: No current whole-system S1 resource controller or function-specific parent supervisory return exists in the delivered product.

## S3* — Complementary audit

- State: —
- Function: No independent agentic audit of ordinary S1 outcome claims returning corrective orders to a current-control owner is evidenced.
- Disturbance / variety regulated: False or stale documentation assertions are checked against citation versions and excerpt source by deterministic validation.
- Decisive decision or feedback right: Independently assess true operational results and require task correction; absent.
- Decision owner: Structured validator and human document reviewer check evidence; neither is an autonomous complementary auditor of an owned S1 organization.
- Supporting / enforcement mechanisms: Evidence IDs, bounded verbatim excerpts, proposal schema, document history, actual session records and rejection.
- Closure path: Invalid proposals fail intake or wait for human review; no independent S1 execution audit finding returns into a Doclify-managed operational task.
- Why this is / is not agent-owned: Source validation and human document approval preserve epistemic quality but do not supply an independent S3* model-audit loop over original agent work.
- Evidence: [pipeline validation](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-pipeline/src/lib.rs), [providers.rs](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/model-bridge/src/providers.rs), [live verification](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Session evidence may be valuable input to an external auditor, not an independently owned corrective Doclify auditor.

### Absence scope

- Surfaces inspected: Extraction validation, record acceptance, transcript evidence, proposal rationale and version constraints.
- Plausible first-party paths checked: Citation audit, source excerpt checks, human acceptance, separate Claude extraction and session replay.
- Why no material first-party path remains: None owns an independent operational S1 success-claim challenge and feedback-to-task-correction path.

## S4 — Outside-and-then intelligence

- State: —
- Function: Human-approved memory transfer across sessions is established, but no distinct prospective external scanning/organizational capability adaptation function is established at a first-party agentic S1 boundary.
- Disturbance / variety regulated: Loss of accepted requirements between current and next agent sessions, not a forecasted future environmental change.
- Decisive decision or feedback right: Authorize changes to future organizational capabilities in response to prospective alternatives; not demonstrated.
- Decision owner: Human reviewer approves local requirements/decisions from retrospective sessions; externally launched agents decide later task actions.
- Supporting / enforcement mechanisms: Accepted/proposed record versions, scoped handoff, `SessionStart` context injection and model documentation extraction.
- Closure path: Past session → extracted doc suggestion → human acceptance → future external session context; this is a real transfer of settled constraints, but not a Doclify-owned prospective adaptation/strategic option loop.
- Why this is / is not agent-owned: Durable human-approved documentation is organizational memory support, yet the assessed project lacks its own autonomous operating S1 and prospective capability decision mode.
- Evidence: [context builder](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-context/src/lib.rs), [hook.rs](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-capture/src/hook.rs), [live verification](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/docs/live-verification.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: A host organization may use Doclify for future capability decisions; that legitimate external use is not classified as first-party Doclify S4.

### Absence scope

- Surfaces inspected: Cross-session handoff, accepted requirement/decision selection, proposal inference and review authority.
- Plausible first-party paths checked: Retrospective documentation learning, model suggestions, human version approval and next-session returned context.
- Why no material first-party path remains: These transmit reviewed present/past facts rather than evaluate prospective environmental alternatives into an authorized durable capability adaptation at the defined agentic harness boundary.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy adjudication and binding return to owned agent operations is evidenced.
- Disturbance / variety regulated: Conflicting document proposals, permissions, project trust and accepted decisions, not the autonomous organization’s binding purpose.
- Decisive decision or feedback right: Resolve an identity/ultimate-policy question with legitimate authority and govern subsequent autonomous operation; absent.
- Decision owner: Local user owns requirement/decision acceptance and host-agent trust; Doclify cannot alter the coding agent's ultimate purpose.
- Supporting / enforcement mechanisms: Exact-version record review, project hook trust, accepted-constraint injection and source identifiers.
- Closure path: Human accepts a repository requirement, and later external agents see it as context; no Doclify-first-party constitutional dispute adjudicator owns a binding purpose return to its own S1.
- Why this is / is not agent-owned: Human review of per-project documentation facts cannot be equated with S5 legitimate ultimate policy over an autonomous Doclify organizational unit.
- Evidence: [README.md](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/README.md), [context builder](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-context/src/lib.rs), [hook installer](https://github.com/shreyas-dhakal/doclify-harness/blob/67714ce9c24adf726f3d30ea35ce7afe9c249b4f/crates/doclify-capture/src/install.rs).
- Basis: structural.
- Confidence: high at the source-pinned boundary.
- Caveats: Human projects may govern agents with approved documents, but that governance belongs to their own external organizational recursion.

### Absence scope

- Surfaces inspected: Human review/record status, hook trust, local repository policy records, extraction constraints and later context injection.
- Plausible first-party paths checked: Accepted requirements as binding downstream context, rejected decisions, plan documentation and restricted provider mode.
- Why no material first-party path remains: These do not create an accountable policy/identity authority for a first-party autonomous Doclify operation and a returned constitutional decision.

## Distributed OSS parent arrangement

Separate Doclify installations feed independently controlled coding agents in local repositories. The human's acceptance of local records does not establish an organization-wide parent mandate or parent-mode S3/S4/S5 for a first-party Doclify agent organization.

## Self-hosted and non-human modes

Capture, records, viewer and pipeline run locally. Structured documentation extraction uses constrained installed Claude or configured API models; Codex's documentation bridge is disabled while its session capture remains available. No supported non-human mode bypasses review to accept project requirements.

## Recursion

The installed project overlay does not own the externally controlled coding agent S1. Multiple sessions and worktrees are evidence sources/consumers, not internally viable Doclify S1 units.

## Variety and escalation

Provenance checks reject unsupported suggestions; queue failures preserve evidence for retry; humans choose accepted changes, and future sessions receive bounded reviewed context. That closes a useful information/authorization pipeline but not a standalone autonomous VSM harness.

## Evidence gaps

- The reviewed upstream live verification reports a successful multi-agent hook/handoff run, but this assessment did not run Codex/Claude or verify its reported timing; `cargo` is unavailable.
- Doclify's final approved documents may influence a downstream external coding agent, yet the autonomy of that agent is not inherited by Doclify.
- No observation of a Doclify-owned autonomous tool/action loop, independent S3* auditor, or higher-recursion identity authority in inspected shipped modes.
