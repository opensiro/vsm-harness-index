---
harness_id: mindweave
project_name: Mindweave
repository: https://github.com/mindweave-cli/mindweave
review_ref: 7a108f043dbfca273dd420d193803f41040a64b7
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Mindweave

## Review boundary

- System in focus: the first-party Mindweave coding organization around one project/session mission at frozen revision `7a108f043dbfca273dd420d193803f41040a64b7`, including the main model/tool loop, subagents, deterministic engine gates, plan mode and persisted approved plans, adversarial verifier subagents, project/session memory, governor enforcement, MCP/tool integrations and supported terminal session controls.
- Purpose and identity: complete software-development tasks locally while keeping the model/tool surface compact, enforcing project/user constraints, preserving relevant context across sessions and allowing bounded delegation and verification.
- Relevant environment: user requests and approvals, repository/filesystem state, command/test/language-server results, provider/model responses, child-agent outputs, project notes and prior-session memory, MCP/external tools and per-project governance files.
- Standard-distribution boundary: shipped TypeScript engine, tools, memory/governor/plan machinery and terminal runtime are inside. Model-provider internals, external MCP servers, repository maintainer governance/CI and user project governance outside the runtime are environment/parent unless explicitly returned through a shipped Mindweave path.
- Credited operating / distribution surfaces: `README.md`; `src/dynamo/engine.ts`; `src/dynamo/verify.ts`; `src/dynamo/planArtifact.ts`; `src/tools/subagent.ts`; `src/tools/verifyReport.ts`; `src/tools/subagentReport.ts`; `src/tools/governorTools.ts`; `src/memory/autoMemory.ts`; `src/memory/projectNotes.ts`.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests as development evidence; project philosophy/architecture docs where they govern Mindweave development rather than a running user mission; website/release governance.
- First-party operating / deployment modes considered: ordinary terminal coding; read-only and mutating subagents; adversarial verifier subagent mode; plan/approval execution mode; resumable sessions and cross-session memory; per-project governor rules/forbidden surfaces; MCP-enabled sessions.
- Recursion level: one user/project mission. The main coding loop and bounded child coding loops are S1 units. A user approving/revising a whole mission plan is treated as a legitimate parent recursion only for the S3 parent mode.
- Reviewed revision: `7a108f043dbfca273dd420d193803f41040a64b7`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Mindweave's core engine runs a provider-neutral model/tool loop. The model receives the current session, project memory/governor state, available tools and current plan/todo context, chooses actions, gets first-party tool results and continues. The runtime adds deterministic safety/reliability gates for read-before-edit, forbidden paths/commands, verification nudges, repeated failures, scope re-entry and other mechanically observable failures.

`spawn_subagent` forks the same engine into a child session with independent transcript/read ledger/step budget. Read-only children can fan out concurrently; mutating children are forced through a serial lane so parallel edits cannot race. The parent receives a mechanically annotated report and can also request `verify:true`, which creates a separate adversarial read-only agent with a verifier-specific system prompt. The verifier must provide command/output evidence; a claimed pass with no evidence is deterministically downgraded.

Plan mode is a separate parent-governed path. While planning, mutating tools are unavailable. The model emits a complete plan for user approval. Once approved, Mindweave writes the exact plan to `.mindweave/plan.md`, injects it as standing knowledge during execution, and instructs the model not to improvise outside it. If a repeated-failure condition shows that an approved step is not working, the runtime stops execution and explicitly returns control for a replan decision rather than silently changing commitments.

The governor persists user-directed standing rules, forbidden paths/commands/MCP tools and skills, and mirrors them into the live session. These are strong policy-enforcement primitives, but the reviewed evidence does not by itself establish a distinct S5 identity/ultimate-policy issue-resolution function at the selected recursion.

## Operational model

The main model-backed actor owns open-ended coding choices. Child agents are separate S1s for bounded delegated work. Mindweave's scheduler distinguishes read-only children from editing children: read-only children may run concurrently, while a mutating child runs alone. This directly attenuates the concrete collision risk of concurrent edits but is a constructor/runtime policy rather than autonomous coordination discretion.

The supported plan mode creates a parent-governed current-control topology. The user sees and approves the whole plan before execution; that approved commitment persists and is re-injected on later execution. When the plan's current step repeatedly fails, Mindweave refuses sideways improvisation and returns the unresolved current-control choice to the user.

Verification can be delegated to an independent adversarial child whose edit/write tools are removed and whose report contract is evidence-gated before the parent sees its verdict.

## S1 — Operations

- State: A
- Function: perform environment-facing software work by inspecting repository state, choosing tools, editing code, executing commands/tests and reacting to returned evidence.
- Disturbance / variety regulated: arbitrary codebase structure, failing checks, diagnostics, command output, provider variation, tool errors, user feedback and implementation alternatives.
- Decisive decision or feedback right: choose the next substantive coding/search/command action, interpret returned results, revise the approach, delegate bounded work and decide when to report.
- Decision owner: the active model-backed Mindweave actor and, within assigned scope, each child model-backed subagent.
- Supporting / enforcement mechanisms: provider-neutral engine; tool registry; deterministic guards; project memory/governor injection; file/shell/MCP tools; session persistence; language-server diagnostics; budgets and cancellation.
- Closure path: user/project state → model request → selected tool/action → runtime executes/refuses → result returns into the transcript → later model turn changes subsequent work.
- Boundary reachability: this is the installed terminal agent's normal runtime; `spawn_subagent` reuses the same first-party engine for bounded children.
- Why this is / is not agent-owned: removing the model actor leaves deterministic tools and guards but removes the open-ended judgment that chooses and interprets coding actions.
- Evidence: [`README.md`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/README.md); [`src/dynamo/engine.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/dynamo/engine.ts); [`src/tools/subagent.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/tools/subagent.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider inference is a dependency; the credited role/tool/feedback loop is first-party.

## S2 — Coordination

- State: C
- Function: prevent destructive interference between concurrently delegated S1 units by allowing parallel read-only work while serializing mutating child agents.
- Disturbance / variety regulated: two child coding agents editing the same project concurrently can race, overwrite changes or reason from incompatible intermediate filesystem states.
- Decisive decision or feedback right: classify a delegated worker as read-only versus mutating and apply the corresponding parallel-versus-serial execution lane.
- Decision owner: constructor/runtime path. The parent model supplies `read_only`, but Mindweave's first-party scheduler owns the hard rule that only read-only workers are concurrency-safe and mutating workers run alone.
- Supporting / enforcement mechanisms: process-wide semaphore; per-tool `isConcurrencySafe`; child-session forking; one-level recursion cap; step budgets.
- Closure path: multiple delegated children are requested → runtime inspects the child mode → read-only workers may execute concurrently while a mutating worker is serialized → subsequent child filesystem actions cannot race with another editing child → results return to the parent.
- Boundary reachability: this policy is implemented directly in shipped `spawn_subagent` and used by the standard engine's concurrent tool execution.
- Why this is / is not agent-owned: the collision attenuation is guaranteed by constructor/runtime scheduling rather than an autonomous actor negotiating between workers; the first-party S2-specific path is nevertheless complete enough to meet the constructor threshold.
- Evidence: [`src/tools/subagent.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/tools/subagent.ts); [`src/dynamo/engine.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/dynamo/engine.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic delegation and the semaphore capacity ceiling are not the witness; the positive mapping is the explicit edit-race prevention rule.
- Distinct S1 units: multiple forked Mindweave child agents, each running the same model/tool engine on a bounded project task.
- Inter-S1 disturbance: concurrent mutating children can race on shared project files and invalidate each other's working state.
- Attenuating coordination relation: runtime admits parallelism only for read-only children and routes mutating children through a serial execution lane.
- Feedback into subsequent S1 behaviour: the scheduling classification determines whether a child may begin concurrently and therefore what filesystem state its later tool calls can observe/mutate.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation explicitly names concurrent edit races as the disturbance and changes execution concurrency specifically to eliminate that interference.

## S3 — Inside-and-now control

- State: P
- Function: regulate the mission's current commitments through a user-approved whole plan that binds subsequent execution and returns failed-plan decisions to the user rather than allowing silent replanning.
- Disturbance / variety regulated: an autonomous coding actor can drift from an agreed implementation plan, expand scope, or improvise around a failing current step in ways that change the user's active commitments without authority.
- Decisive decision or feedback right: approve the full plan that governs the work and, when execution evidence shows the approved path is no longer viable, decide whether/how to replan.
- Decision owner: the user/operator as legitimate parent authority in the supported plan mode.
- Supporting / enforcement mechanisms: read-only plan mode; `exit_plan`; persisted `.mindweave/plan.md`; standing-knowledge injection; repeat-failure/divergence detector; automatic clearing/completion of the plan artifact after the governed work turn.
- Closure path: model researches and proposes a full plan → user approves → runtime persists exact approved plan and injects it into execution → model must follow the approved commitments → repeated plan-step failure triggers a hard stop with instruction not to improvise → user receives the unresolved current-control choice and can authorize a new plan.
- Boundary reachability: plan mode and plan approval are standard interactive Mindweave features; the approved artifact is read by the same runtime that executes the work, including across sessions.
- Why this is / is not agent-owned: the model proposes and executes, but the authority to establish or replace the whole approved commitment set belongs to the user in this mode.
- Evidence: [`src/dynamo/engine.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/dynamo/engine.ts); [`src/dynamo/planArtifact.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/dynamo/planArtifact.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary user prompts/approvals are not credited. The witness is the distinct plan mode with whole-plan authority, persisted returned commitment and fail-closed replan path.
- Whole-system current view: the complete approved implementation plan is the mission-level set of current commitments presented to the parent before execution; the runtime retains that exact plan as standing knowledge while work proceeds.
- Current-control decision scope: establish/replace the mission's current implementation commitments and decide what to do when the active approved plan cannot be followed.
- Parent mode: user approval creates the active plan; repeated execution failure returns the decision to that same parent authority; the returned plan governs later operation.
- No autonomous/constructor base mode is claimed: todo/re-scope/verification guards support current execution, but this review does not treat those fixed backstops or model-authored task lists as an independently established S3 ownership mode.

## S3* — Complementary audit

- State: A
- Function: independently challenge completed code/work through a separate adversarial verifier agent before its verdict is relied on.
- Disturbance / variety regulated: a worker/main coding actor can produce plausible but incorrect changes, skip meaningful checks or self-report success without evidence.
- Decisive decision or feedback right: judge the already-produced work as `pass`, `fail` or `partial` after independently executing checks and attempting to break it.
- Decision owner: a separate model-backed verifier child created with `verify:true` and verifier-specific instructions.
- Supporting / enforcement mechanisms: read-only child tool restriction; separate child session/context; verifier system prompt; required command/output report shape; deterministic evidence counter that downgrades an unevidenced pass.
- Closure path: parent identifies work to audit → launches adversarial verifier with original request/change scope → verifier independently reads/runs checks without edit authority → verifier returns evidence-backed verdict → parser may downgrade unsupported pass → parent receives verdict/concerns and can fix, continue or accept.
- Boundary reachability: verifier mode is a documented option of the shipped `spawn_subagent` tool, not a test-only evaluator.
- Why this is / is not agent-owned: the substantive adversarial test selection and pass/fail judgment are made by a separate model actor; deterministic parsing only enforces evidence hygiene.
- Evidence: [`src/tools/subagent.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/tools/subagent.ts); [`src/tools/verifyReport.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/tools/verifyReport.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the ordinary deterministic `VERIFY_NUDGE` is not the S3* witness; it only detects “edited but no check”. The positive mapping relies on the separate adversarial child.
- Claim being audited: that already-performed code changes satisfy the original request and survive meaningful execution/boundary checks.
- Ordinary reporting path: main/worker coding actor edits and reports its result.
- Complementary access path: verifier child is forked in a separate session with a dedicated adversarial prompt and read-only tool set, then runs its own checks against project reality.
- Independence boundary: the verifier cannot edit the project, does not share the parent's conversational reasoning and must produce command/output evidence; an unevidenced pass is mechanically rejected as partial.
- Who acts on findings: the parent Mindweave actor receives the verdict and concerns and can take corrective operational action.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop was established at the selected mission recursion.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Cross-session memory, project notes, web/MCP access and session summaries preserve useful information, but no shipped S4 actor was found that develops adaptation options from future/external distinctions and changes persistent organizational capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `save_memory`; automatic memory index; MINDWEAVE.md; project/directory notes; web/MCP tools; session memory/compaction; provider/model switching.
- Closure path: not applicable; no distinct external-and-prospective intelligence → adaptation option → current capability/S3 return loop was established.
- Why this is / is not agent-owned: the operational actor can remember facts and use them later, but durable context is not by itself prospective organizational adaptation.
- Evidence: [`src/memory/autoMemory.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/memory/autoMemory.ts); [`src/memory/projectNotes.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/memory/projectNotes.ts); [`README.md`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/README.md).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: learning/persistence may improve later S1 decisions; that effect does not satisfy the stronger S4 functional/closure threshold.

### Absence scope

- Surfaces inspected: auto/cross-session memory, project notes, session summaries/compaction, web/MCP access, model/provider switching, skills/governor and update command.
- Plausible first-party paths checked: autonomous self-improvement, future-environment research, strategy/capability revision, learned policy changes and adaptation of tool/model capabilities.
- Why no material first-party path remains: located mechanisms store/retrieve context or let the user change configuration; no separate prospective intelligence loop selects an adaptation and returns it as a persistent capability/strategy change.

## S5 — Policy and identity

- State: —
- Function: no distinct first-party identity/ultimate-policy issue-resolution loop was established at the selected mission recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established as an S5 right. The user can state durable governor rules/forbidden paths/commands and the runtime enforces them, but these are general standing constraints rather than evidence of a distinct identity/ultimate-policy issue reaching a legitimate S5 authority.
- Decision owner: not established for an S5 function.
- Supporting / enforcement mechanisms: governor rule files; forbid/unforbid tools; live governance reload; mechanical path/command/MCP enforcement; project notes and skills.
- Closure path: no qualifying identity/ultimate-policy issue → authoritative decision → returned governance loop was established. User rule requests do return into operation, but the reviewed examples/path are ordinary project execution constraints.
- Why this is / is not agent-owned: governor comments explicitly say the user decides what to make a rule/forbid and tools only record/enforce it; enforcement authority does not itself establish S5.
- Evidence: [`src/tools/governorTools.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/tools/governorTools.ts); [`src/dynamo/engine.ts`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/src/dynamo/engine.ts); [`README.md`](https://github.com/mindweave-cli/mindweave/blob/7a108f043dbfca273dd420d193803f41040a64b7/README.md).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: a deployment that uses the governor for genuine mission identity/ultimate-policy decisions could motivate a different recursion-specific analysis; generic standing rules are not enough here.

### Absence scope

- Surfaces inspected: governor rules/forbidden controls, project notes, system prompt/governance injection, plan approval, tool approvals, MCP trust and session/model configuration.
- Plausible first-party paths checked: runtime identity revision, ultimate-policy proposals/escalations, parent policy dispute resolution, persistent policy exceptions and return to operation.
- Why no material first-party path remains: located governance mechanisms persist and enforce operator-chosen constraints but do not distinguish/close an identity or ultimate-policy issue at the assessed mission recursion.

## Recursion

The selected recursion is one user/project mission. Main and child coding actors are operational units. The user is treated as parent only for the explicit whole-plan S3 mode; ordinary approvals/configuration do not automatically become parent S3/S5.

## Variety and escalation

Mindweave absorbs coding variety through model/tool discretion, deterministic guardrails, context/memory, delegation and independent verification. Editing children are serialized to remove write races. Plan-mode divergence and permission/governor constraints can return control to the user, but only the plan path is credited as a function-specific parent S3 closure.

## Evidence gaps

Primary evidence is strong for S1, S2 constructor coordination, S3 parent plan control and S3* verifier independence. The repository contains rich memory/governor facilities, but the reviewed standard distribution does not establish the stronger S4 or S5 organizational functions at this recursion.
