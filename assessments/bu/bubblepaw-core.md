---
harness_id: bubblepaw-core
project_name: BubblePaw Core
repository: https://github.com/BubbleBuffer/BubblePaw-Core
review_ref: 2f98827beda9f2c988368c99ee9fa69120899dff
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BubblePaw Core

## Review boundary

- System in focus: BubblePaw native core together with its first-party runner workspace/child-session composition, not the core-only crate or an imported agent product.
- Purpose and identity: Library-first durable model/tool work with workspace tools and controlled reusable children.
- Relevant environment: users, workspaces, model services, tools and the operational disturbances described below.
- Standard-distribution boundary: bubblepaw runner/host and embedded SDK using the native core, including registered child profiles and optional child worktrees.
- Credited operating / distribution surfaces: core Harness model/tool loop, runner provider/tool wiring, child-session status/control and model-facing isolated worktree path.
- Adjacent first-party surfaces excluded from ownership: Replay/chapter-bench probes, conformance/fixture tests and CI/release processes; external Codex/Claude internal agent control and optional third-party MCP server behavior.
- First-party operating / deployment modes considered: Native runner with API model adapter; registered read-only/workspace children, optional worktree isolation and self-hosted approval policies. Core-only embedding requires its own provider/tool wiring and is not assigned the assembled runner vector.
- Recursion level: one deployed harness/composition and its work sessions; repository maintainers and external hosts are outside this operational recursion.
- Reviewed revision: `2f98827beda9f2c988368c99ee9fa69120899dff`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (active Index pair; current Skills main calibration also consulted).

## Repository architecture

The Rust core owns durable sessions, the authoritative model/tool loop, effects, context preparation, approval gates and explicit interruption recovery. The runner supplies API/native provider adapters, workspace/CodeMode tools, MCP client and reusable child sessions; separate front ends share the host method table. Parent status/reminders and child send/cancel controls close current supervision, and optional git worktrees isolate child writes. SQLite/root/session ownership, inherited tool/deadline/profile constraints and preserved unknown external outcomes are enforcement machinery. Probes/replay and repository verification are adjacent evaluation surfaces.

## Operational model

Operational actors are the root and registered child Harness sessions. The assessment credits the first-party assembled runner, including the parent model discretion over child isolation and current child commitments, rather than assigning those functions to the core crate, locks or imported provider. There is no automatic credit for spawning recursion, quota meters, prose claims or benchmark checks.

## S1 — Operations

- State: A
- Function: Perform workspace tasks through durable model/tool sessions and reusable child work actors.
- Disturbance / variety regulated: Uncertain task progress, tool errors, context limits, interrupted external effects and child questions.
- Decisive decision or feedback right: Choose next action, tool, child task or final answer from the current observations.
- Decision owner: The model actor driven by the native Harness model/tool loop.
- Supporting / enforcement mechanisms: SQLite history/effects, ToolDispatcher, CodeMode/workspace tools, provider adapters, approvals, queued steering and explicit resume.
- Closure path: Prepared model request → model-selected tools → durable tool results → subsequent model request; child completion can wake the parent.
- Why this is / is not agent-owned: Own runtime.rs executes the authoritative tool loop. The API provider witnesses inference-only transport; external Codex/Claude adapters do not donate their inner control functions.
- Evidence: [crates/bubblepaw-core/src/runtime.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/runtime.rs); [crates/bubblepaw-core/src/dispatch.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/dispatch.rs); [crates/bubblepaw-runner/src/agents.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/agents.rs); [docs/providers.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/providers.md); [docs/child-sessions.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-sessions.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.
- Boundary reachability: The normal bubblepaw runner wires Harness, tools and model providers; API provider mode and registered child profiles reach the same first-party loop.

## S2 — Coordination

- State: A
- Function: Attenuate shared-workspace write interference between autonomous workspace child sessions.
- Disturbance / variety regulated: Two workspace-profile children otherwise inherit the same filesystem and can overwrite one another; descendants may accidentally use the wrong root workspace.
- Decisive decision or feedback right: Choose isolated child workspaces for concurrent writers and use returned branch/workspace state when continuing them.
- Decision owner: The parent model actor selects worktree:true through the shipped tools.agent interface; git and workspace resolvers enforce that choice.
- Supporting / enforcement mechanisms: Per-child git worktree/branch, nearest-isolated-ancestor workspace resolution, scope-bound file/exec tools, status receipts and safe retention/cleanup.
- Closure path: Parent selects isolation → child runs against its effective checkout → spawn/status returns workspace/branch/worktree facts → parent continues/steers the corresponding session without sharing its write surface.
- Why this is / is not agent-owned: The credited decision is the agent-selectable conflict-attenuation mode, not deterministic git or session plurality. It is available to the running parent without custom host coordination code.
- Evidence: [docs/child-worktrees.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-worktrees.md); [docs/child-sessions.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-sessions.md); [crates/bubblepaw-runner/src/agents.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/agents.rs); [crates/bubblepaw-runner/src/worktrees.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/worktrees.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: Optional mode; default workspaces are shared, and isolation does not automatically merge conflicting results or prove semantic conflict resolution..
- Boundary reachability: Registered model-facing workspace profiles expose the worktree field; agents.rs creates the binding at admission and subsequent child tools resolve that same workspace.

- Distinct S1 units: two or more workspace-profile child Harness sessions, each with its own task, model/tool loop and outcome.
- Inter-S1 disturbance: concurrent children sharing the parent checkout can modify the same files or act in an incorrect ancestor workspace.
- Attenuating coordination relation: model-selected per-child worktree separation, explicit parent/root binding and branch-aware status feedback.
- Feedback into subsequent S1 behaviour: every child read/edit/write/exec and descendant workspace resolution uses the accepted binding; parent status retains the binding for later sends/continuations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the option changes the shared mutation topology to prevent a concrete cross-worker write collision; creating a session or sending a message alone is not credited.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current commitments and compute across a parent task and its descendant work tree.
- Disturbance / variety regulated: Stale/running/failed/waiting children, finite shared tool allowance/deadline and unfinished commitments competing for that allowance.
- Decisive decision or feedback right: Inspect descendant status, cancel or steer child commitments, and assign fresh per-child tool/deadline bounds for the next turn.
- Decision owner: The parent model actor owns these current choices within host-imposed maximums.
- Supporting / enforcement mechanisms: Descendant-tree status with unread/results, stale-child reminders, child completion wake, inherited budget/deadline clamping and subtree cancellation cleanup.
- Closure path: State/reminder → parent observes current descendant tree/result → parent cancels, redirects or issues a bounded next turn → child runtime applies the changed commitment/allowance and returns status/results.
- Why this is / is not agent-owned: Credit is bounded to the parent task organization: the actor sees and can change ongoing child work on behalf of that whole. Host quota waiting and concurrency limits merely enforce ceilings; they do not own the parent decision.
- Evidence: [docs/child-sessions.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-sessions.md); [crates/bubblepaw-runner/src/agents.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/agents.rs); [crates/bubblepaw-runner/src/agent_handles.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/agent_handles.rs); [crates/bubblepaw-core/src/runtime.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/runtime.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: Spawn/decomposition alone is not the witness. Controls cannot enlarge an active turn by steering; fresh limits apply on later child turns and remain clamped by originating bounds. No separate parent-human mode is inferred from approval UI..
- Boundary reachability: The ordinary runner model tool set includes agent_status, agent_send and cancel with the originating parent ownership checks; no custom supervisor is needed for these decisions.

- Whole-system current view: the parent-visible descendant tree lists state, parent/session identity and unread work; direct reads expose result/usage/error, and stale reminders flag neglected commitments.
- Current-control decision scope: retained child commitments, cancellation/intervention and fresh tool/deadline allocation across descendants within the root task; account quota and operator-wide project prioritization are excluded.

## S3* — Complementary audit

- State: —
- Function: No complementary independent operational-audit loop is supplied in the normal workspace runner.
- Disturbance / variety regulated: The possible organizational disturbance associated with the inspected mechanisms.
- Decisive decision or feedback right: No function-specific decisive organizational right established in this supported mode.
- Decision owner: No qualifying owner established; developer/operator constraints remain external decisions.
- Supporting / enforcement mechanisms: Context-recall probes/judges, replay/chapter-bench commands, direct child transcript access, logs, structured-output validation and ordinary tool checks.
- Closure path: No corresponding organizational return loop established.
- Why this is / is not agent-owned: Probe scoring belongs to explicit replay/evaluation rather than a normal-session corrective controller. Generic research/child tools can be composed into review, but no specifically wired independent audit judgment plus corrective return is shipped for normal workspace operations. Source-level verification is adjacent.
- Evidence: [crates/bubblepaw-runner/src/probes.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/probes.rs); [crates/bubblepaw-runner/src/main.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/main.rs); [crates/bubblepaw-core/src/observation.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/observation.rs); [docs/verification.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/verification.md); [docs/child-sessions.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-sessions.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: crates/bubblepaw-runner/src/probes.rs, crates/bubblepaw-runner/src/main.rs, crates/bubblepaw-core/src/observation.rs, docs/verification.md, docs/child-sessions.md and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Context-recall probes/judges, replay/chapter-bench commands, direct child transcript access, logs, structured-output validation and ordinary tool checks.
- Why no material first-party path remains: Probe scoring belongs to explicit replay/evaluation rather than a normal-session corrective controller. Generic research/child tools can be composed into review, but no specifically wired independent audit judgment plus corrective return is shipped for normal workspace operations. Source-level verification is adjacent.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then organizational adaptation loop is supplied.
- Disturbance / variety regulated: The possible organizational disturbance associated with the inspected mechanisms.
- Decisive decision or feedback right: No function-specific decisive organizational right established in this supported mode.
- Decision owner: No qualifying owner established; developer/operator constraints remain external decisions.
- Supporting / enforcement mechanisms: Summary/chapter decision models, compaction/recall, selectable model roles, live provider configuration and research children.
- Closure path: No corresponding organizational return loop established.
- Why this is / is not agent-owned: Context organization and provider reconfiguration preserve current operation. Research and recall mechanisms do not by themselves investigate prospective environmental change and return selected capability adaptations. Replay model comparisons are evaluation, not a deployed adaptation authority.
- Evidence: [docs/decision-providers.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/decision-providers.md); [docs/live-config.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/live-config.md); [docs/context-compaction.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/context-compaction.md); [crates/bubblepaw-runner/src/agents.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/agents.rs); [crates/bubblepaw-runner/src/probes.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-runner/src/probes.rs).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: docs/decision-providers.md, docs/live-config.md, docs/context-compaction.md, crates/bubblepaw-runner/src/agents.rs, crates/bubblepaw-runner/src/probes.rs and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Summary/chapter decision models, compaction/recall, selectable model roles, live provider configuration and research children.
- Why no material first-party path remains: Context organization and provider reconfiguration preserve current operation. Research and recall mechanisms do not by themselves investigate prospective environmental change and return selected capability adaptations. Replay model comparisons are evaluation, not a deployed adaptation authority.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy arbitration loop is supplied.
- Disturbance / variety regulated: The possible organizational disturbance associated with the inspected mechanisms.
- Decisive decision or feedback right: No function-specific decisive organizational right established in this supported mode.
- Decision owner: No qualifying owner established; developer/operator constraints remain external decisions.
- Supporting / enforcement mechanisms: Ask/Allow/Deny/Auto approvals, model-based bounded auto checks, profile narrowing, live config updates and inherited child authority.
- Closure path: No corresponding organizational return loop established.
- Why this is / is not agent-owned: The returned decisions concern ordinary tool permissions and execution constraints, not an identity/ultimate-policy matter at this recursion. No first-party escalation and authoritative arbitration/return path for that function is packaged.
- Evidence: [docs/approvals.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/approvals.md); [docs/live-config.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/live-config.md); [crates/bubblepaw-core/src/approvals/mod.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/approvals/mod.rs); [crates/bubblepaw-core/src/approvals/modes.rs](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/crates/bubblepaw-core/src/approvals/modes.rs); [docs/child-sessions.md](https://github.com/BubbleBuffer/BubblePaw-Core/blob/2f98827beda9f2c988368c99ee9fa69120899dff/docs/child-sessions.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level assessment; no live model/provider execution is claimed.

### Absence scope

- Surfaces inspected: docs/approvals.md, docs/live-config.md, crates/bubblepaw-core/src/approvals/mod.rs, crates/bubblepaw-core/src/approvals/modes.rs, docs/child-sessions.md and the declared runtime/distribution wiring.
- Plausible first-party paths checked: Ask/Allow/Deny/Auto approvals, model-based bounded auto checks, profile narrowing, live config updates and inherited child authority.
- Why no material first-party path remains: The returned decisions concern ordinary tool permissions and execution constraints, not an identity/ultimate-policy matter at this recursion. No first-party escalation and authoritative arbitration/return path for that function is packaged.

## Distributed OSS parent arrangement

Public maintainers own development and release governance. Their repository process is adjacent to the installed harness; contributor plurality does not establish operational parent S3/S4/S5 at this recursion. No additional closed parent-governed function is established by ordinary configuration or approvals.

## Self-hosted and non-human modes

Native runner with API model adapter; registered read-only/workspace children, optional worktree isolation and self-hosted approval policies. Core-only embedding requires its own provider/tool wiring and is not assigned the assembled runner vector. Model choice, permission settings and deployment administration alone do not establish ultimate-policy governance. Unimplemented extensions do not receive constructor credit.

## Recursion

Subagents are task decomposition; no recursively viable suborganization is established.

## Variety and escalation

Tool/model failures, permission limits and context exhaustion return as observations, refusals, pauses or terminal results. These channels support local recovery; they are not additional VSM functions or automatic algedonic evidence.

## Evidence gaps

No live provider or product E2E run was performed. Conclusions concern reachable source-level ownership at the exact frozen revision, not performance, deployment reliability or benchmark quality. Bounded absence claims cover the stated supported distribution, not arbitrary future extensions.
