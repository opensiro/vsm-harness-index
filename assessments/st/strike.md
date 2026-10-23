---
harness_id: strike
project_name: Strike
repository: https://github.com/jonathanung/strike
review_ref: 0191bb896b5a1969c5b7b784597ed891b814234a
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Strike

## Review boundary

- System in focus: Strike's shipped Go coding-agent engine and its standard CLI/TUI, headless, RPC/ACP, and optional live web-cockpit product surfaces at the frozen revision. The relevant organizational recursion is one lead coding session with its first-party subordinate task-agent sessions, not the company or open-source contributor community.
- Purpose and identity: produce, inspect, validate, and coordinate software-engineering changes in a user-provided workspace within first-party task, resource, permission, and session controls.
- Relevant environment: workspace source and edits, developer instructions, user objectives, tool/compile/test results, model outputs, external information tools, concurrent child edits and budgets, and optional operator direction.
- Standard-distribution boundary: Strike's headless engine, session team, task/delegation/board/ownership tools, verification gate mechanism and configured frontends. External LLM providers, project-defined commands, Git hosting, and human inputs are dependencies or outside authorities, not intrinsic autonomous actors.
- Credited operating / distribution surfaces: `cmd/strike/assemble_tools.go` and `session_lifecycle.go`; `harness/engine/engine.go`, `child.go`, `team.go`, `team_board.go`, `delegation.go`, `agent_roster.go`, `team_control.go`, `verify.go`; `harness/tool/task.go`, `team_task.go`, `agent_ownership.go`, `ownership.go`; `harness/verify/verify.go`; `internal/frontend/server/api.go`, embedded shipped web cockpit, and supported session interfaces.
- Adjacent first-party surfaces excluded from ownership: repository `.claude/` development helpers, `AGENTS.md` contributor directions, project release/CI jobs, `internal/eval/replay` benchmarking and simulated harness evaluation, SWE-bench runner, test fixtures, and the OSS maintainer decision process. They corroborate implementation but do not supply S3*/S4/S5 ownership to the user-facing product.
- First-party operating / deployment modes considered: solo coding turn; lead with autonomous model-backed child agents; team shared-board/path-ownership mode; optional configured completion gates; web-cockpit operator control over the same live root's team, including its read-only/attach-only limits; goal/loop/workflow and configurable model/tool/permission modes.
- Recursion level: one lead session/team overseeing independently acting task-specific child sessions. Children have distinct model/tool loops, local goals, and workspace interaction but no demonstrated complete metasystem of their own.
- Reviewed revision: `0191bb896b5a1969c5b7b784597ed891b814234a`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The `harness/engine` provider/tool loop emits events, accepts operations, and runs model-selected repository and process tools through the first-party permission, sandbox, and scheduling mechanisms. Session transcripts are durable JSONL event logs. The composition root registers task spawning/status/control, a shared team board, path ownership, peer communication, verification, plans, and ordinary coding tools. A spawned child has a separate session and its own model/tool loop; the parent can inspect its status and terminal evidence. A session-scoped `Team` retains roster, delegations, task claims, patch proposals, file ownership and contracts until root teardown.

The kernel also provides a process-local admission scheduler for model/bash resource pools, per-child budgets and a deterministic delegation-worthiness policy. These enforce constraints but do not themselves choose organizational priorities. Shared-board CAS ownership, conflict-aware path touches and exclusive/shared leases address concrete simultaneous-agent contention. In supported live web-cockpit operation the authenticated/authorized human root controller can separately spawn or interrupt children and change the team's board/delegation state through public protocol operations; those are not model decisions.

An optional, separately run completion-gate system executes parent/host-specified command, schema or path checks against claimed child work. It records discrepancies and can block the child's completed status despite the implementer's self-report. The goal-loop critic and repository evals are inspected as possible alternative channels but are not imported as independent whole-team adaptive strategy or governance without an actual return path.

Primary source entry points:

- [`README.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/README.md) and [`docs/ARCHITECTURE.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/ARCHITECTURE.md).
- [`cmd/strike/assemble_tools.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/cmd/strike/assemble_tools.go) and [`harness/engine/child.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/child.go).
- [`docs/agents-skills.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/agents-skills.md) and [`docs/human-orchestration-ops.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/human-orchestration-ops.md).

## Operational model

The primary coding actor receives the task and workspace evidence, chooses model/tool actions, and can produce code changes or responses. It can create multiple bounded child actors, each independently choosing actions for its subtask. Team-coordination data and child reports are exposed through model-facing tools and engine events. The primary actor can use this information to allocate or revise live work; a separate supported human web-control mode exposes an alternative parent-owned intervention path on the same operating team. A child claiming completion is not necessarily verified: configured gates perform independent checks and can block the report. None of these current-task mechanisms alone gives the system a self-governing constitutional identity or external/future-focused capacity adaptation loop.

## S1 — Operations

- State: A
- Function: autonomously perform coding, repository inspection, editing, shell/build/test work and local task-specific recovery against a changing workspace.
- Disturbance / variety regulated: ambiguous requirements, differing code paths, changing file state, failed tool/command results, and model/tool uncertainties while pursuing assigned outcomes.
- Decisive decision or feedback right: choose task-specific next model/tool action and revise the sequence after returned tool, workspace or child evidence.
- Decision owner: lead model-backed session, or each child model-backed session for its own bounded operational objective.
- Supporting / enforcement mechanisms: Go engine loop, tool registry, permissions, file-state guards, session JSONL, budgets, scheduler, optional sandbox and provider adapters.
- Closure path: user/subtask objective → model request/decision → first-party tool action → returned result and updated session state → later model decision or completion.
- Boundary reachability: standard CLI/headless/engine composition builds and invokes this loop; child creation uses the same operational engine. No evaluation-only or contributor-only actor is needed.
- Why this is / is not agent-owned: removing the model leaves a deterministic tool runner and control plumbing but no context-dependent choice among code edits, investigations and validations.
- Evidence: [`harness/engine/engine.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/engine.go); [`cmd/strike/assemble_tools.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/cmd/strike/assemble_tools.go); [`harness/engine/child.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/child.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no live model was invoked during this source-pinned assessment; tool permissions may block a chosen operation.

## S2 — Coordination

- State: A
- Function: attenuate conflicting work claims and path modifications among separately acting child/lead S1 sessions in one shared workspace.
- Disturbance / variety regulated: two live agents can claim the same work item, overwrite an actively held file/prefix, or submit mutually incompatible patches.
- Distinct S1 units: lead and spawned child sessions with separate engine/model/tool action loops, and multiple concurrent children on the same implicit team.
- Inter-S1 disturbance: live team members share a workspace and team task/patch state; duplicate task claims and conflicting file leases/touches are explicitly represented and rejected or warned by first-party code.
- Attenuating coordination relation: model-facing `team_task` uses owner-exclusive claim and CAS; `agent_ownership` supplies inspectable exclusive/shared leases; write touches and `patch_collab` expose overlaps, with `session.overlapPolicy=block` able to reject conflicting mutation.
- Feedback into subsequent S1 behaviour: conflict/claim results return to the invoking model, live path overlaps reach the team event stream, and ownership claims alter what other member sessions may subsequently claim/write under the configured policy.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: claim exclusivity and conflict-aware path leases target demonstrable shared-workspace collision modes of independent S1s rather than merely transferring or listing their tasks.
- Decisive decision or feedback right: choose and revise task claims, leases and coordinated file scopes in light of contested ownership and overlap feedback.
- Decision owner: model-backed team actors choose claims/scopes and adjust behavior; deterministic shared board, path tracker, CAS and policy enforce or report conflicts.
- Supporting / enforcement mechanisms: `Team` shared state, team board, `PathOwnership`, `agent_ownership`, policy setting, file mutation hooks, patch conflict detection and event delivery.
- Closure path: autonomous S1 requests claim/lease → conflict-aware team registry decides admissibility → return result/warning/block → same or competing S1 chooses a different task/path or waits; subsequent changes obey the updated claim.
- Boundary reachability: `cmd/strike/assemble_tools.go` registers `team_task`, `agent_ownership` and `patch_collab` in the shipped registry, while the standard child engine shares the team's state and file ownership tracker.
- Why this is / is not agent-owned: code can reject a preset conflict, but without an autonomous actor it cannot decide which meaningful task/file scope should be taken next following a denial.
- Evidence: [`harness/engine/team_board.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/team_board.go); [`harness/tool/ownership.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/tool/ownership.go); [`harness/tool/agent_ownership.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/tool/agent_ownership.go); [`harness/engine/team_control_test.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/team_control_test.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the default overlap policy warns rather than blocks file writes; stronger protection is a supported configuration. The claim board itself nevertheless enforces exclusive ownership.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current subordinate commitments, resources, priorities and interventions on behalf of a live multi-child session team.
- Disturbance / variety regulated: independently evolving child work becomes blocked, stalled, over-budget, conflicting or obsolete relative to the lead's overall objective and remaining resources.
- Whole-system current view: the model-facing `agent_roster` exposes the complete session team with current status, objectives, last actions, blocks, touched files and budget/usage/stall fields; the progressive `task` list/status API tracks a shared delegation population, not just a single awaited handoff.
- Current-control decision scope: lead can choose child assignments/personas/budgets and dependencies, subscribe to block/completion feedback, interrupt/cancel/reopen work and transition owned delegations; supported root human controls can separately spawn, interrupt and change delegation/board commitments.
- Decisive decision or feedback right: revise live-team resource and commitment choices using current population observations, including exceptions and blocked/dependency state.
- Decision owner: autonomous lead model in the base mode; human operator controlling the live root team via the shipped web-cockpit protocol in the distinct parent mode. Neither the scheduler nor the dashboard owns these choices.
- Supporting / enforcement mechanisms: roster and `task` tools; child state/budget record; delegation lifecycle with CAS and dependency guards; shared scheduler; human `team.*` Op permission/identity/root checks and browser UI.
- Closure path: live team roster/delegation exception → lead model observes status and issues bounded `task` create/cancel/transition or allocation update → engine changes child commitments and reports state → continued child/lead action. In parent mode, live team observation → human operation through `team.spawn`, `team.child_interrupt`, `team.task_transition`, or board Ops → engine applies/rejects and publishes updated team state.
- Boundary reachability: the CLI registry exposes roster and progressive task controls to the lead; the first-party live web cockpit implements separate root-authorized human team-control Ops through the same engine, not an imagined plugin.
- Why this is / is not agent-owned: removing the lead model from the autonomous mode leaves a status dashboard and rule enforcement but no task-specific cross-child intervention judgment. Parent mode makes that judgment explicitly human, with the same first-party return path.
- Evidence: [`harness/engine/agent_roster.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/agent_roster.go); [`harness/tool/task.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/tool/task.go); [`harness/engine/delegation.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/delegation.go); [`harness/engine/team_control.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/team_control.go); [`internal/frontend/server/api.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/internal/frontend/server/api.go).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: claims concern one active session team; global scheduler limit config is enforcement, not agent-owned budget governance. The human path requires an active, mutation-authorized live root; historical/attach-only and read-only modes do not close it.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead model-backed actor | Shared live roster/budget/block/delegation state exposes current-team exception or need to reallocate | Model uses `task` controls to revise live child assignments, dependencies, cancellations or budgets; returned status informs later decisions | `harness/engine/agent_roster.go`, `harness/tool/task.go`, `harness/engine/delegation.go` |
| Parent (`P`) | Authorized human live-root operator | Live cockpit team status or need to intervene in present work | Human `team.*` Op reaches engine under root/permission/idempotency checks; changed child/board state is returned to the live session | `harness/engine/team_control.go`, `internal/frontend/server/api.go`, shipped cockpit team controls |

## S3* — Complementary audit

- State: C
- Function: offer a parent/host-controlled, implementer-independent completion challenge on a subordinate actor's claimed result.
- Disturbance / variety regulated: an implementer can wrongly claim to have completed required work or tests; routine model handoff text may assert success without supporting reality.
- Claim being audited: a child session's `completed`/self-reported verification and, optionally, a solo root's claimed final turn.
- Ordinary reporting path: model-produced terminal handoff (`summary`, `verification`, files changed and findings) or ordinary tool results in the implementer's execution stream.
- Complementary access path: a separately executing engine `verify.Runner` inspects actual filesystem path existence, independent shell-command outcomes and/or structured handoff schema, ignoring the model's self-certification string; a failed check changes a claimed-completed child to `blocked` and injects failures into handoff blockers/lead notification.
- Independence boundary: the checks run after the child has claimed success under the parent engine, not as the child's own `verification` prose. However the shipped general component is a configured deterministic gate runner; its independent audit strategy, sampling, or model-based auditor is not a fully autonomous, separately assigned first-party role.
- Who acts on findings: the parent engine blocks promotion of a failed child and feeds gate failures to the lead; the lead or operator can correct/re-delegate. Autonomous complementary audit judgment beyond the specified gates must be composed.
- Decisive decision or feedback right: decide which independent checks to require and interpret their direct-evidence failure, versus accepting the implementer claim.
- Decision owner: the parent/host configuring `verify` gates owns the audit brief; the independent deterministic runner owns factual pass/fail evaluation and blocking, not autonomous audit policy or judgment in the general case.
- Supporting / enforcement mechanisms: `harness/verify/verify.go`, `harness/engine/verify.go`, `child.go` gate-to-blocked transition, verification events and handoff error propagation.
- Closure path: implementer completion claim → independent parent-side gate execution → direct-evidence verdict → failed claim demoted to blocked and exposed to lead → bounded corrective response/redelegation. Constructor state reflects missing autonomous auditor/selection ownership rather than absence of this first-party function-specific path.
- Boundary reachability: the shipping `task` API accepts `verify` gates, `child.go` invokes the independent runner, and the ordinary parent receives blocked/status evidence; this is not imported from the separate benchmark evaluator.
- Why this is / is not agent-owned: no model can override a failed gate by claiming it passed; the shipped checking judgment is deterministic and task-configured. The runtime offers the independent complementary witness, but does not itself provide an autonomous audit investigator beyond it.
- Evidence: [`harness/verify/verify.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/verify/verify.go); [`harness/engine/verify.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/verify.go); [`harness/engine/child.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/child.go); [`harness/engine/verify_gates_test.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/verify_gates_test.go).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: opt-in gates cover defined outcomes and can resemble ordinary QA; `C` is credited only to the bounded first-party complementary check of implementer claims, not to evaluation/CI in the adjacent development organization or a claim of broad independent review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct externally and prospectively oriented adaptation system that changes Strike's own present organizational capability was established at the assessed team recursion.
- Disturbance / variety regulated: external web/documentation tools, code intelligence, agent/persona selection, repository memory, plan/workflow/goal loops and model routing can influence current work, but the reviewed paths do not form a prospective capability-adaptation conversation with S3.
- Decisive decision or feedback right: not established for future environmental adaptation of the operating organization.
- Decision owner: not established; agents can plan user tasks and operators can change static config, not thereby own S4.
- Supporting / enforcement mechanisms: web/browser tools, goal-loop planner/critic, scheduled loops, workflow phases, skill/persona discovery, model routing and local memory/ledger.
- Closure path: no first-party external/future distinction → developed adaptation option → capability intervention returning into team-wide current S3 control was found.
- Why this is / is not agent-owned: current task research, local replanning, recurring prompts and failure memory remain current operations without first-party prospective strategic choice/return.
- Evidence: [`docs/goal.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/goal.md); [`docs/loop.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/loop.md); [`docs/agents-skills.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/agents-skills.md).
- Basis: explicit + bounded structural absence review.
- Confidence: medium-high.
- Caveats: users can script ongoing market or technology research with tools, but that is not a first-party always-linked adaptation decision in the assessed organization.

### Absence scope

- Surfaces inspected: shipped goal/loop/workflow description and goal code, agent/skill/model routing, repository tools, product config, team/delegation current-control surface, and adjacent eval/replay separation.
- Plausible first-party paths checked: provider/tool catalog as environmental intelligence; scheduled or goal-based project self-improvement; agent memory and decision ledger as a prospective option channel; workflow phase changes as return to present capability; offline evaluations as prospective regulator.
- Why no material first-party path remains: the supported paths apply user-defined tasks/constraints, current coding observations or local evaluation; no evidenced first-party agent-owned strategic adaptation loop both models an outside-and-then future and effects corresponding revisions to the team's organizational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision and returned governance loop exists at the assessed runtime team recursion.
- Disturbance / variety regulated: permission, sandbox, provider selection, workflow gates and human approval constrain tools and phases, but do not themselves adjudicate organizational identity or an S3–S4 policy tension.
- Decisive decision or feedback right: no such ultimate-policy issue/decision right established at the team boundary.
- Decision owner: developers/operators select settings and grant ordinary access; they do not constitute a documented first-party runtime S5 closure merely by doing so.
- Supporting / enforcement mechanisms: managed permission denies, tool authorization, sandbox, config, `team.*` human control, audit log, workflow `/autonomy` gate.
- Closure path: no identity-level issue → legitimate ultimate authority → binding policy return into the same operating team established. Human `team.*` acts on live work and is counted only as S3 parent control.
- Why this is / is not agent-owned: neither model nor operator is given a first-party process for resolving ultimate identity/policy questions; existing policies merely bound choices already assigned elsewhere.
- Evidence: [`harness/engine/team_control.go`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/harness/engine/team_control.go); [`docs/human-orchestration-ops.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/human-orchestration-ops.md); [`docs/usage.md`](https://github.com/jonathanung/strike/blob/0191bb896b5a1969c5b7b784597ed891b814234a/docs/usage.md).
- Basis: explicit + bounded structural absence review.
- Confidence: high.
- Caveats: higher-level real human or OSS governance may exist outside this operational recursion, but co-location is not a first-party S5 product path.

### Absence scope

- Surfaces inspected: engine/user/team Op model, human-control authorization, permission and sandbox modes, workflow exit approval, user/project instructions, durable ledger, and adjacent contributor/release governance.
- Plausible first-party paths checked: human approval as parent ultimate-policy arbitration, managed policy changes as durable identity reform, agent policy/role editing as internal S5, higher-recursion project governance as product control.
- Why no material first-party path remains: shown decisions approve tools, choose workflow transitions, constrain actions or alter current team work; none sends an identity/policy issue to a legitimate ultimate authority and returns a governing constitutional decision to the assessed session organization.

## Recursion

Each active child is a meaningful subtask-level S1 with its own working environment, actions and bounded discretion. Team nesting is real, but the reviewed child instances are not demonstrated to contain a viable S1–S5 metasystem recursively. The primary mapping covers one session team; simultaneous unrelated roots are separate teams and process-local scheduling across them is not credited as a larger S3/S5 parent.

## Variety and escalation

Strike amplifies operational variety through tools, provider/model choice, project context, child specialization and parallel independent tasks. It attenuates destructive variety with task-claim CAS, path leases/overlap warnings or blocking, bounded budgets, permission/sandbox rules, and verified-completion gates. Child errors, stall/budget statuses and independent gate failures can reach the lead through live task status, completion events and messages. The lead can revise current commitments; in live parent-control mode the human root operator has an alternative intervention path. These are current-control signals, not automatically algedonic identity or future-adaptation governance.

## Evidence gaps

- Go 1.26+ was not available in the local container or connected dev VM, so no native Go build/test run was executed in this assessment. Static first-party code, documented supported paths and committed mock/scripted-provider tests were inspected; no live LLM or external tool activity was performed.
- The `S3=A(P)` claim is bounded to a live multi-child team and separately reconstructable model-owned and human-owned modes; it is not a claim that every solo task runs a full metasystem.
- The `S3*=C` finding credits the concrete configured post-claim direct-evidence gate as a complementary challenge of child self-report. It does not credit ordinary tool `verify`, development CI, or offline benchmark grading as independent runtime S3*. Its restricted audit brief and deterministic judgement make a broader autonomous audit classification unproven.
- No upstream source ref was changed: every positive and absence conclusion is tied to the frozen commit, not current upstream HEAD.
