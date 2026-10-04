---
harness_id: openseek
project_name: OpenSeek
repository: https://github.com/moonbitlang/openseek
review_ref: 3999e3c1a804651f7d59b2f69dad6c6dae48de71
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenSeek

## Review boundary

- System in focus: the first-party `moonbitlang/openseek` coding-agent engine at frozen revision `3999e3c1a804651f7d59b2f69dad6c6dae48de71`, including its model/tool turn loop, durable session/store, built-in coding/control tools, workspace skills, MCP bridge, run/serve execution surfaces, standing-goal machinery, and the shipped read-only `agent_review` / optional goal-met review-gate path where those mechanisms bear on organizational function.
- Purpose and identity: execute software-engineering work in a selected workspace through an iterative model/tool loop, preserve resumable execution state, and optionally subject a standing-goal completion claim to a separate read-only model-backed audit before subsequent main-agent action.
- Relevant environment: user objectives and steering, workspace/Git/filesystem state, command/compiler/test output, model-provider responses, configured MCP services, persistent session history and standing-goal state, and operator-selected approval/runtime options.
- Standard-distribution boundary: OpenSeek's root CLI engine, `agent`, `agent_runtime`, `agent_session` and store, built-in `agent_tool` registry, skills/MCP integration, `run` and `serve`, first-party `agent_review`, bundled review workflow, and opt-in `--review-gate` are inside. External model providers, external MCP servers, host OS/process facilities, target-project governance, and the separately maintained `moonbitlang/openseek_tui` repository are dependencies/environment rather than OpenSeek decision owners.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `agent/README.mbt.md`; `agent/turn_loop.mbt`; `agent/goal_gate_test.mbt`; `agent_review/README.mbt.md`; `agent_review/engine.mbt`; `agent_review/audit.mbt`; `internal/openseek/options/review.mbt`; `internal/openseek/execution/gate.mbt`; `internal/openseek/run/turn.mbt`; `cmd/openseek/README.md`; and the bundled review workflow where it is reachable from a durable standard run.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests/eval harnesses except where a runtime test directly corroborates the shipped review-gate closure; editor-development/browser fixtures; release/maintainer governance; standalone evaluation/reporting packages; and code in external `openseek_tui`. These may corroborate behavior but do not become runtime organizational owners by co-location.
- First-party operating / deployment modes considered: headless `run`; long-lived `serve`; durable/resumed sessions; configured MCP/skills; standing Goal use; optional `--review-gate`; model-initiated bundled read-only review in durable sessions; and the standalone `--kind review` engine as the first-party audit actor used by the gate.
- Recursion level: one OpenSeek coding session / standing-goal organization. The main model-backed agent is the operational S1. A review child is a complementary audit actor over that S1, not a production S1. Hosted scouts/subruns are bounded delegated support and are not promoted into a team recursion absent a concrete same-recursion coordination/control organization.
- Reviewed revision: `3999e3c1a804651f7d59b2f69dad6c6dae48de71`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OpenSeek separates provider data/transport, a first-party agent loop, durable session state, tool execution, CLI orchestration and review into explicit packages. The `agent` package owns orchestration policy: it projects the authoritative session into provider messages, calls the selected model, executes first-party tools, appends observations, absorbs mid-turn steering and repeats until finish, abort, cancellation, context yield or a configured bound. The root CLI wires this loop into one-shot `run` and long-lived `serve` modes.

The standard tool registry includes file mutation and reading, process execution through `mbtx`, background-job observation/control, planning, standing-goal status and finish. Durable sessions are append-only and resumable; compaction appends summaries rather than rewriting history. Skills and MCP tools can extend the evidence/action surface but do not own OpenSeek's organizational decisions.

OpenSeek also ships a distinct model-backed review engine. `agent_review` uses a read-only tool profile and a structured `submit_review` contract to inspect a change or audit a worktree against a goal. For the opt-in `--review-gate` path, the CLI supplies an `on_goal_met` callback that launches a managed `run --kind review` child against the live standing goal and its recorded baseline. The audit child receives its own bounded model run, worktree access and compiler/test evidence. Its validated report is reduced to a review digest and returned into the main turn as a durable runtime notice.

This return is operational rather than merely archival. The agent loop schedules the pending review at a batch-safe boundary before the following model request, appends the review notice durably, mirrors it into the in-flight model messages, and then continues. Frozen-revision tests explicitly assert that the request after the gate contains the audit digest and that a same-batch `goal(met)` plus `finish` is converted into a continuation through the review before the next final answer.

Primary evidence:

- [`docs/architecture.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/docs/architecture.md)
- [`agent/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/README.mbt.md)
- [`agent/turn_loop.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/turn_loop.mbt)
- [`agent/goal_gate_test.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/goal_gate_test.mbt)
- [`agent_review/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent_review/README.mbt.md)
- [`internal/openseek/execution/gate.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/execution/gate.mbt)
- [`internal/openseek/run/turn.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/run/turn.mbt)
- [`cmd/openseek/README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/cmd/openseek/README.md)

## Operational model

A normal OpenSeek run receives a user task and current durable session/workspace context. The main model-backed actor chooses from the exposed coding/control/MCP tools; OpenSeek executes the call, appends the result into the authoritative session and feeds the updated projection back to the same actor. Steering and background notices can alter the same active turn at safe boundaries.

When a standing goal is present, the main actor may report `goal(met)`. In the first-party `--review-gate` mode that claim schedules an independent goal audit. A separate review child receives the goal and baseline, inspects current worktree reality with a read-only model/tool profile, runs compiler/tests where relevant, and submits a validated structured report. OpenSeek then injects its digest as a durable model-visible notice before the main actor's next request. The main actor therefore receives evidence from a complementary path and can revise or reconfirm completion.

The review gate is advisory and fails open if the auditor is unavailable. That limits enforcement strength but does not erase the established audit feedback loop when the supported mode is active: the decisive audit judgment is model-owned by the separate reviewer, its access is complementary to the producer's completion claim, and the result is returned into subsequent S1 cognition/action.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by interpreting a task, selecting coding/tool actions, executing them through the first-party runtime, observing their results and iterating until completion or another terminal condition.
- Disturbance / variety regulated: heterogeneous repositories and objectives, changing file/Git/process state, compiler/test output, tool failures, model observations, user steering, background-job completion and task-specific implementation choices.
- Decisive decision or feedback right: decide what evidence to inspect, which coding/control/MCP action to take next, how to revise work from returned observations, and when to finish, continue or report standing-goal status within externally selected runtime constraints.
- Decision owner: the main model-backed OpenSeek agent instantiated by the first-party turn loop.
- Supporting / enforcement mechanisms: agent loop; typed tool registry; `mbtx`; file/edit/write/remove tools; plan/goal/finish; durable session/store; steering queue; context compaction; skills/MCP; approval/sandbox policy; run/serve transports.
- Closure path: user task + workspace/session state → main model selects tool/action → OpenSeek executes or gates it → tool/environment result is appended to the authoritative session → the updated session projection returns to the main model → next action or terminal decision.
- Boundary reachability: standard `openseek run` and `openseek serve` directly instantiate the first-party model/tool loop and built-in tools; no downstream application-authored orchestration layer is required.
- Why this is / is not agent-owned: deterministic runtime code transports, persists and enforces selected actions, but removing the main model-backed actor removes the open-ended software-engineering judgment that chooses and sequences those actions.
- Evidence: [`agent/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/README.mbt.md); [`docs/architecture.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/docs/architecture.md); [`cmd/openseek/README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/cmd/openseek/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is an external provider dependency; OpenSeek is credited for its shipped actor/tool/feedback organization rather than provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party same-recursion inter-S1 coordination function was established.
- Disturbance / variety regulated: not established at S2 level. OpenSeek can launch bounded hosted child agents/scouts/reviewers, but the frozen standard distribution does not establish a concrete mutual interference, conflict or oscillation among distinct production S1 units that a first-party coordination relation specifically attenuates.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: hosted child/subrun transport; child-session identity; workflow delegation; task-group/runtime queues; review/scout results; session locks and sequential turn processing.
- Closure path: not applicable; no distinct-production-S1 interference → attenuation decision → changed subsequent S1 behaviour loop was reconstructed.
- Why this is / is not agent-owned: delegation and concurrent bounded investigation move work/results between actors but are not S2 without a specific interference witness and attenuation relation.
- Evidence: [`cmd/openseek/README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/cmd/openseek/README.md); [`agent/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/README.mbt.md); [`agent_review/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent_review/README.mbt.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a larger application can compose several OpenSeek workers into an organization with S2; that organization is outside this standalone engine/session boundary.

### Absence scope

- Surfaces inspected: main agent loop; task groups/runtime queues; durable sessions; hosted subruns/scouts; review children; MCP tools; run/serve command sequencing; session-store locking.
- Plausible first-party paths checked: multiple child agents; concurrent scouts; reviewer/main coexistence; parallel background jobs; shared session state; workflow child IDs; serve command sequencing.
- Why no material first-party path remains: the located plurality is bounded delegation, audit or execution support. No frozen-revision evidence establishes a specific interference among distinct production S1 units plus an S2-specific autonomous attenuation and feedback path.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the main coding S1 and deterministic run/session controls was established.
- Disturbance / variety regulated: active goal state, current plan, tool/background-job progress, context/step ceilings, approvals, cancellation and session sequencing are regulated operationally, but not as a whole-system portfolio of multiple operational commitments/resources.
- Decisive decision or feedback right: not established at S3 level. Main-agent plan/goal choices remain part of executing the current task, while runtime scheduling, bounds and approval machinery enforce configured/operator policy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: plan/goal tools; standing-goal reminders; task groups; step/context ceilings; serve queue; cancellation/steering; approval desk; background-job controls; session persistence.
- Closure path: not applicable; no whole-system current view plus substantive current-control decision over multiple relevant S1 resources, commitments, priorities or accountability was found.
- Why this is / is not agent-owned: the main model owns coding-task decisions, not a distinct metasystem current-control role over an organization of S1s. Deterministic runtime controls continue to enforce their configured bounds without an autonomous managerial owner.
- Evidence: [`agent/turn_loop.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/turn_loop.mbt); [`docs/architecture.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/docs/architecture.md); [`cmd/openseek/README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/cmd/openseek/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this does not deny substantial current-task supervision and lifecycle control; the negative conclusion is specific to the Profile's stronger whole-system S3 function at this recursion.

### Absence scope

- Surfaces inspected: plan/goal lifecycle; serve scheduler/queue; active task group; step/context budgets; approvals; cancellation/steering; child sessions; background jobs; current session state.
- Plausible first-party paths checked: main agent as supervisor; standing Goal as whole-system control; review gate as management intervention; workflow child allocation; serve process as current-control center; operator approval.
- Why no material first-party path remains: these mechanisms govern one coding organization/turn or provide complementary audit. They do not expose a distinct whole-system view with substantive organization-wide commitment/resource authority and returned current-control decisions.

## S3* — Complementary audit

- State: A
- Function: independently challenge a main-agent standing-goal completion claim using complementary read-only worktree/compiler evidence and return the audit finding into the same coding organization before subsequent main-agent action.
- Disturbance / variety regulated: a producing coding agent may report a goal as met while the actual worktree, diff, compiler/test state or goal criteria reveal incomplete, incorrect or superficially satisfying work.
- Decisive decision or feedback right: decide, from an independently modelled read-only audit of the worktree against the goal/baseline, what findings exist and submit the structured `ReviewReport` that becomes the audit verdict returned to the main run.
- Decision owner: the separate model-backed `agent_review` child in the supported review-gate mode.
- Supporting / enforcement mechanisms: `run --kind review`; read-only `mbtx` profile; compiler/test execution; structured `submit_review`; report validation at child and parent trust boundaries; captured goal baseline; child step/deadline bounds; durable review runtime notice; main-loop pending-review scheduler.
- Closure path: main S1 records `goal(met)` → OpenSeek schedules a separate review child → reviewer independently inspects the live worktree against the goal/baseline and submits a validated report → gate converts it to a review digest → digest is durably appended and mirrored into the main agent's messages → next main-agent request sees the audit and can revise/reconfirm work.
- Boundary reachability: `--review-gate` is a first-party option shared by supported `run` and `serve` modes; it wires the shipped `agent_review` child directly into the main turn. No external reviewer service or downstream orchestration code is required.
- Why this is / is not agent-owned: deterministic code launches and validates the audit, but the substantive review judgment and findings are generated by a distinct model-backed reviewer. Removing that reviewer leaves only transport/validation and no semantic audit verdict.
- Evidence: [`agent_review/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent_review/README.mbt.md); [`internal/openseek/options/review.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/options/review.mbt); [`internal/openseek/execution/gate.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/execution/gate.mbt); [`internal/openseek/run/turn.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/run/turn.mbt); [`agent/goal_gate_test.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/goal_gate_test.mbt); [`agent/turn_loop.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/turn_loop.mbt).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the gate is opt-in and advisory/fail-open; `A` therefore describes the supported first-party audit ownership mode, not a claim that every OpenSeek run is audit-gated or that reviewer availability is guaranteed.
- Claim being audited: the producing main agent's claim that the current standing goal is met.
- Ordinary reporting path: the main agent's own `goal(met)` / finish path in the active coding session.
- Complementary access path: the separate `agent_review` child reads the current worktree against the captured goal/baseline through a read-only tool profile and grounds findings in compiler/test evidence rather than relying on the producing agent's report.
- Independence boundary: the audit is a distinct child model run with its own bounded session/allowance and a no-edit review toolset; the gate reads the live standing goal/baseline from authoritative session state, so the audited S1 does not restate the criteria to the reviewer.
- Who acts on findings: the main coding agent. The review digest is appended as a durable runtime notice and injected into the next model request; frozen-revision tests verify that same-batch completion continues through the gate and the post-gate model request sees the audit.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-future intelligence loop that generates and adopts an organizational adaptation was established.
- Disturbance / variety regulated: not established at S4 level. Durable history, compaction, skills, MCP, web/search-like tools, review findings and resumable goals improve present/future task context but do not by themselves model environmental change and alter OpenSeek's persistent organizational capability/strategy.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: append-only session memory; compaction summaries; skills; MCP; review reports; durable goals; provider/model/runtime configuration.
- Closure path: not applicable; no first-party external/future distinction → adaptation-option generation → autonomous selection → persistent capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: retained information and audit feedback can change the current task, while installed skills/configuration can change capability under operator/developer control. Neither establishes an autonomous prospective adaptation owner.
- Evidence: [`docs/architecture.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/docs/architecture.md); [`README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/README.md); [`agent/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/README.mbt.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: users can author workflows that research and change a project or agent setup; generic composability is not a first-party S4 closure.

### Absence scope

- Surfaces inspected: session persistence/compaction; skills; MCP; standing goals; review/audit; background-job notices; provider/runtime options; bundled workflows and evaluation surfaces.
- Plausible first-party paths checked: memory-driven learning; review-driven persistent improvement; autonomous skill installation; future/environment scans; provider/model adaptation; session summaries as organizational learning.
- Why no material first-party path remains: the reviewed mechanisms preserve or expose information and support present task correction, but no shipped autonomous process owns prospective adaptation selection and writes the chosen change back into persistent organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: prompts, approval policy, workspace/tool restrictions, model/provider selection, MCP configuration and runtime bounds constrain behavior, but they are operating configuration/enforcement rather than a reconstructed identity-level governance function.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: user/operator/developer configuration for the relevant constraints; deterministic OpenSeek machinery enforces those selections and the agent acts inside them.
- Supporting / enforcement mechanisms: system prompt selection; approval policy/channel; workspace/tool boundaries; model/provider/API settings; MCP configuration; goal/review options; cancellation.
- Closure path: not applicable at S5 level; configuration can govern later behavior, but no standard identity/policy conflict → legitimate ultimate authority → authoritative decision → returned operation loop was established.
- Why this is / is not agent-owned: the main or review model does not own OpenSeek's ultimate identity/policy boundary, and hard enforcement of externally selected constraints is not itself S5 ownership.
- Evidence: [`cmd/openseek/README.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/cmd/openseek/README.md); [`agent/README.mbt.md`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/agent/README.mbt.md); [`internal/openseek/run/turn.mbt`](https://github.com/moonbitlang/openseek/blob/3999e3c1a804651f7d59b2f69dad6c6dae48de71/internal/openseek/run/turn.mbt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a deployment can place OpenSeek under an external parent organization's policy; that parent is not imported into this standalone first-party assessment without a function-specific closed mode.

### Absence scope

- Surfaces inspected: prompt ownership; approval policy; tool/workspace restrictions; model/provider configuration; MCP setup; run/serve options; standing-goal/review controls; repository governance boundary.
- Plausible first-party paths checked: user approval as parent policy; system prompt as identity; model choice; sandbox/tool restrictions; Goal as mission identity; review gate as policy authority.
- Why no material first-party path remains: these surfaces define or enforce task/runtime constraints. No frozen-revision evidence shows a genuine identity/ultimate-policy issue adjudicated by a legitimate first-party ultimate authority and returned as the governing policy of subsequent operation.

## Distributed OSS parent arrangement

OpenSeek's public maintainer/contributor process is adjacent to deployed agent sessions and is not inferred to be an organization-level runtime parent. A local operator can set prompts, approval policy and model/provider configuration, but those ordinary controls do not establish parent-mode S3/S4/S5 without the corresponding function-specific closure.

## Self-hosted and non-human modes

OpenSeek is self-hosted and supports interactive/controller-assisted approval as well as unattended headless execution. The main coding S1 remains autonomous within the selected boundary. The optional audit mode adds a separate autonomous S3* reviewer; it does not imply autonomous or parent-owned S3/S4/S5.

## Recursion

The focal recursion is one OpenSeek coding session with its standing goal. The main model-backed actor is the production S1. The review child is organizationally complementary: it inspects the producing S1's claim via a separate evidence and model path, then returns findings to that S1. Hosted scouts or other workflow children remain bounded delegation/support unless a separately assessed organization establishes persistent production-unit plurality and metasystem relations.

## Variety and escalation

OpenSeek attenuates operational variety through typed tools, durable sessions, context checkpoints, steering, process/job controls, standing-goal reminders, approvals, cancellation, retries and read-only review. The review-gate path is a particularly strong escalation: a goal-met claim can leave the ordinary S1 path, be challenged by a separate reviewer, and return as model-visible evidence before continuation. This supports S3* but does not turn the audit mechanism into S3 or S5.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. Primary exact-ref documentation, implementation and executable tests are sufficient to establish the S1 and S3* closures and to bound the stronger S2/S3/S4/S5 claims. The review specifically inspected the most plausible positive paths—hosted child agents, standing goals/current-control machinery, durable state/skills, and approval/prompt configuration—rather than inferring functions from component names.

## Assessment summary

OpenSeek is a substantive first-party coding-agent engine. It closes autonomous S1 through its model/tool/session loop and, in a supported opt-in mode, closes autonomous S3* through a separate read-only model reviewer whose validated standing-goal audit is returned into the main agent before subsequent action. The frozen standard distribution does not establish the stronger S2, S3, S4 or S5 closures.

**Vector:** A · — · — · A · — · —
