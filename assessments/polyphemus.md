---
harness_id: polyphemus
project_name: Polyphemus
repository: https://github.com/polyphemus-ai/release-rehearsal
review_ref: 02020f3bc2829c350fd726273a7721254068925f
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Polyphemus

## Review boundary

- System in focus: one supported local-first Polyphemus deployment/project at pinned revision `02020f3bc2829c350fd726273a7721254068925f`, including the first-party daemon/CLI/app, model/provider adapters, session and project runtime, tools and approvals, isolation, multi-agent thread execution, durable workflow/run engine, shipped agent templates, project memory/rules and first-party service integrations.
- Purpose and identity: run one or more model-driven agents as a durable local team that performs project work through tools and external services, preserves project context, coordinates concurrent agents, executes evidence-backed workflows, independently reviews changes, and remains governed by operator-approved project rules.
- Relevant environment: project files and repositories, configured model providers/vendor CLIs, external services reachable through granted connections, GitHub repositories/issues/PRs, local container/host resources, paired operator devices, project users, provider capacity/quota and changing task state.
- Standard-distribution boundary: the shipped `polyphemus` CLI, `@polyphemus/core`, daemon/app runtime, built-in workflow engine and `ship-issue` workflow, bundled agent templates, project/session/memory/rules machinery, isolation/tooling and supported self-hosted operator surfaces. Provider/model internals, GitHub itself, external MCP/services and unrelated contributor/development organization remain environment/dependencies and do not donate VSM functions.
- Credited operating / distribution surfaces: ordinary interactive sessions using the first-party agent loop; project-scoped sessions and memory/rules; concurrent multi-agent thread operation; the shipped workflow/run engine; built-in `ship-issue`; bundled Reviewer; first-party operator review of proposed project rules.
- Adjacent first-party surfaces excluded from ownership: repository contributor governance; CI/release workflows; private post-mortems referenced by design docs; tests/examples except as corroboration of shipped behavior; future roadmap items not implemented at the pinned revision; the repository's own development organization.
- First-party operating / deployment modes considered: ordinary local session; project-bound session; concurrent addressed agents in one thread; built-in durable workflow execution; `ship-issue`; isolated and host execution modes; operator-approved project-rule review.
- Recursion level: one Polyphemus project/deployment is the system-in-focus. Model-driven sessions/agent workflow nodes that own substantive project outcomes are S1 operations. Workflow review and project-rule governance are mapped separately only where their function and closure are distinct from ordinary task execution.
- Reviewed revision: `02020f3bc2829c350fd726273a7721254068925f`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Polyphemus is a local-first agent harness with a first-party model/tool loop, persistent session/project state, model/provider routing, guarded tool execution, container/host isolation, skills, agent personas, memory, scheduled routines, connections and a daemon-backed phone/web control surface. `runTurn` repeatedly calls the selected model, executes requested tools, returns tool results, and continues until the model stops or a bounded step limit is reached. The decisive task-specific action selection is model-driven; approval, redaction, isolation, provider routing and tool execution constrain or support that operational loop.

A project supplies durable identity/context around those operations. `AGENTS.md` records what the project is, how work is done and its ground rules; private memory carries handoff and reviewed notes. Every project session receives the project rules/context. Agents may draft new rules and notes into an inbox, but the standard project flow requires the operator to keep or discard them before they become authoritative.

Polyphemus also supports more than one agent working in the same thread. Distinct addressed agents receive independent runtimes while sharing the thread. Their messages can interleave in a way that would break model tool-call/result adjacency. The shipped runtime therefore re-reads shared thread state and deterministically `stitchHistory` so each tool call is paired with its result while preserving the rest of the conversation. This is a concrete inter-S1 anti-interference path rather than generic messaging alone.

The durable workflow subsystem is explicitly code-orchestrated: "orchestration is code, intelligence is in the nodes." It stores run/node state, attempts, artifacts, checks and budgets; creates fresh model sessions for agent nodes; validates submitted artifacts; executes checks/actions/gates; and resumes from persisted state. This is strong execution control, but at the assessed project/deployment recursion the reviewed standard distribution does not expose a separate autonomous or parent whole-system current regulator over the portfolio of active S1 commitments. Per-run budgets, fixed graph progression, fallback routing, stop controls and ordinary human gates remain support/enforcement or lower-scope execution mechanisms rather than a positive S3 mapping.

Complementary audit is stronger in the shipped `ship-issue` workflow. After a builder's candidate has passed objective checks and been pushed at an exact head commit, a read-only reviewer agent is launched with `independentOf` the producing work node. The engine preferentially selects a model from another vendor, the reviewer inspects the actual diff/files and runs relevant checks, and its structured `approve` / `request_changes` verdict controls whether the loop repairs the candidate. A posted approval is bound to the reviewed head, and merge verifies that the approved commit is still the one being merged.

No material S4 loop is established at this boundary. Provider-capacity forecasting predicts whether current quota will last until reset; routing can change providers; project memory and orientation preserve facts/rules; scheduled routines react to configured triggers. These are useful current-operation mechanisms, but they do not form the Profile's external-and-prospective environmental model → adaptation options → return into present capability loop.

## Operational model

The ordinary S1 is a model-driven Polyphemus agent session or workflow agent node performing a substantive project outcome. The first-party runtime supplies the system prompt/context, model route, tools, isolation and approvals; the model actor decides task-specific reasoning/tool actions and updates its behavior from returned tool/environment observations.

At the same project recursion, multiple distinct agent runtimes can work concurrently in one shared thread. Polyphemus attenuates a concrete coordination disturbance introduced by that concurrency: one agent's interleaved messages can separate another agent's tool calls from their results and leave a stale private copy of shared conversation state. The runtime repairs model-visible history and refreshes shared context before later turns. The anti-interference function is first-party and closed, but the decisive policy is deterministic constructor/runtime logic rather than an autonomous agent choice, so S2 is `C` rather than `A`.

The built-in shipping workflow separates ordinary production from complementary audit. Builder/planner nodes create the candidate; objective checks establish ordinary evidence; an independently instantiated reviewer receives the exact candidate through direct repository access, judges it, and returns findings into the next repair round. This supplies autonomous S3* ownership even though deterministic workflow code enforces exact-head and merge constraints.

Ultimate project rules remain parent-governed. Agents can propose durable rule changes, but the operator decides whether a proposed `AGENTS.md` is kept. Once kept, the authoritative file is loaded into future project sessions, giving a project identity/policy issue → legitimate parent decision → authoritative rule change → subsequent-operation closure path.

## S1 — Operations

- State: A
- Function: perform substantive project work through model-driven reasoning, tool use and iterative response to environment/tool feedback.
- Disturbance / variety regulated: ambiguous task requests, changing project/repository state, tool results and failures, external service responses, model uncertainty, provider/tool differences and local implementation/research variety.
- Decisive decision or feedback right: choose the next task-specific reasoning/tool action and revise later actions from returned observations in order to complete the assigned outcome.
- Decision owner: the model-driven agent actor executed through the first-party Polyphemus session/workflow runtime.
- Supporting / enforcement mechanisms: `runTurn`, provider adapters, model routing/fallback, tool registry, approvals, redaction, isolation workers, session persistence, skills/persona/project context and connection grants.
- Closure path: user/workflow outcome + project/agent context → model actor selects an action/tool call → Polyphemus executes it within the allowed boundary → tool/environment result returns to the model → subsequent model action changes until the outcome/turn closes.
- Boundary reachability: ordinary `polyphemus` sessions and workflow agent nodes directly invoke the shipped first-party loop and tools; no adjacent dogfood or contributor actor is required.
- Why this is / is not agent-owned: removing the model-driven actor while keeping routing, tools, isolation and persistence leaves execution machinery but removes the task-specific discretionary action choice.
- Evidence: [`README.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/README.md); [`packages/core/src/loop.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/loop.ts); [`packages/core/src/projects.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/projects.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model/provider internals and vendor CLI internals remain external dependencies. `A` credits the model actor reached through the first-party supported runtime, not organizational functions internal to those providers.

## S2 — Coordination

- State: C
- Function: attenuate a concrete interference mode created when distinct S1 agent runtimes work concurrently in one shared thread while preserving each runtime's coherent model-visible history.
- Disturbance / variety regulated: concurrently working agents interleave messages in the shared thread; another agent's messages can appear between a tool call and its tool result, and a runtime can otherwise continue from a private history that omits intervening peer contributions.
- Decisive decision or feedback right: determine the safe model-visible ordering/synchronization of shared-thread messages so each runtime sees its tool call/result pairs coherently while still incorporating peer contributions.
- Decision owner: first-party deterministic Polyphemus runtime policy (`stitchHistory` plus shared-thread resynchronization); no autonomous agent owns the coordination semantics.
- Supporting / enforcement mechanisms: per-agent aside runtimes, addressed-agent dispatch, shared thread store, per-agent stop state, held-message queue, sequence tracking and runtime/session persistence.
- Closure path: concurrent S1 runtimes append interleaved shared-thread events → Polyphemus reconstructs model-valid history and refreshes the shared thread before subsequent turns → each affected agent receives the repaired/current conversation → later S1 behavior proceeds from coordinated state rather than the destructive interleaving/stale copy.
- Boundary reachability: concurrent addressed agents and history stitching are shipped daemon/core behavior documented and implemented at the pinned revision; adopters do not have to invent a separate coordination protocol.
- Why this is / is not agent-owned: removing either model actor does not remove the deterministic coordination policy; the same first-party runtime rule decides how interleaved shared history is repaired. The S2-specific path is therefore constructor/runtime-owned `C`, not agent-owned `A`.
- Distinct S1 units: two or more independently addressed model-driven agent runtimes working concurrently in the same Polyphemus thread.
- Inter-S1 disturbance: peer output interleaves with another agent's tool call/result sequence and can leave a model-facing history invalid or stale with respect to the shared conversation.
- Attenuating coordination relation: `stitchHistory` moves tool results next to their calls, synthesizes a stopped-turn result where needed and preserves intervening peer material after the repaired pair; the multi-agent runtime also re-synchronizes each agent with shared thread state before later work.
- Feedback into subsequent S1 behaviour: the repaired/current history is what the next model invocation receives, so subsequent reasoning/actions are conditioned on coordinated peer state rather than corrupted or permanently skipped context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on an explicitly documented concurrency-induced model-history corruption/staleness mode and a shipped attenuation transform that changes later sibling-agent input. Addressing, queueing and shared storage alone are not used as the S2 witness.
- Evidence: [`docs/design/parallel-agents.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/docs/design/parallel-agents.md); [`packages/core/src/history.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/history.ts); [`packages/daemon/src/server.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/daemon/src/server.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the held-message queue and agent addressing are generic routing/sequencing mechanisms by themselves. The positive S2 finding is narrower: concurrent shared-thread history interference plus the specific repair/resynchronization path.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party S3 function is established at the assessed project/deployment recursion.
- Disturbance / variety regulated: per-run failures, step state, budgets, provider exhaustion, approvals and concurrent job status are regulated locally, but the reviewed boundary does not establish a separate whole-project current regulator with authority over the portfolio of S1 resources/commitments/priorities.
- Decisive decision or feedback right: no qualifying whole-system current-control decision right is established.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: durable run store, node state machine, retries, hard attempt/loop/budget limits, one-at-a-time workflow keys, provider fallback/capacity readings, session stop controls, scheduler and human gates.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: model nodes make local operational decisions, while the workflow engine deterministically advances fixed graphs and enforces preselected limits. Ordinary operator gates approve specific actions. Neither path demonstrates a separate agent-owned or constructor-specific whole-system current regulator at the selected recursion.
- Evidence: [`docs/design/workflows.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/docs/design/workflows.md); [`packages/core/src/workflows/define.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/workflows/define.ts); [`packages/daemon/src/runs.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/daemon/src/runs.ts); [`packages/core/src/routing.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/routing.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: at a narrower workflow-run recursion the deterministic engine strongly regulates execution, and a future portfolio-level scheduler/manager could change this assessment. The current conclusion is specific to the declared project/deployment recursion and Profile threshold.

### Absence scope

- Surfaces inspected: workflow design and implementation; run state/executor; workflow node/gate/action/check semantics; per-run budgets and retries; provider routing/capacity; routine scheduler; daemon live-session controls; project/session status and operator controls.
- Plausible first-party paths checked: workflow engine as current controller; planning agent as supervisor; provider-capacity routing; one-at-a-time run admission; human action/merge gates; session stop/guard mechanisms; daemon-wide live-session observation.
- Why no material first-party path remains: the inspected mechanisms sequence or enforce bounded execution, regulate a single run/provider/action, or expose operator intervention. The pinned standard distribution does not establish the required whole-system current view plus a function-specific decision over the project's active operational resources, commitments, priorities or synergy on behalf of the whole.

## S3* — Complementary audit

- State: A
- Function: independently challenge a produced software change using access and judgment distinct from the builder's ordinary production path, then return findings into correction before merge.
- Disturbance / variety regulated: implementation defects, missing requirements, risky changes or false confidence that can survive the producing agent's own reasoning and objective checks.
- Decisive decision or feedback right: inspect the exact candidate and decide whether to approve it or request changes based on direct repository/diff/test evidence.
- Decision owner: the read-only model-driven Reviewer agent instantiated by the first-party `ship-issue` workflow; the workflow preferentially selects a different model vendor from the producing agent.
- Supporting / enforcement mechanisms: fresh node session; `independentOf` provider selection; read-only mode; exact-head push/check linkage; typed review artifact; deterministic verdict parsing; GitHub Reviewer identity; exact-head posted review; merge guard.
- Closure path: builder candidate + objective checks at exact head → separate reviewer agent directly inspects diff/files and runs relevant checks → reviewer returns `approve` or `request_changes` with concerns → deterministic workflow either passes the approval check or loops findings back to the work node → repaired candidate is rechecked/re-reviewed before merge.
- Boundary reachability: `ship-issue` is a built-in shipped workflow; its review node is explicitly `readOnly` and `independentOf` the producing node, and the run engine implements other-vendor reviewer selection in ordinary workflow execution.
- Why this is / is not agent-owned: the audit judgment about defects/adequacy comes from the separate reviewer model actor. Exact-head validation, read-only restrictions and merge gating enforce that judgment but do not decide the review verdict.
- Claim being audited: that the candidate change at the exact pushed head satisfies the requested issue/plan and is safe/complete enough to merge.
- Ordinary reporting path: the builder's submitted change report plus objective build/typecheck/lint/test/preview checks and workflow artifacts.
- Complementary access path: a separate read-only reviewer session reads the actual diff/files and runs its own relevant checks against the candidate; it is not limited to the builder's self-report.
- Independence boundary: the review node is declared `independentOf` the producing work node; the run engine attempts to choose a ready model from another vendor, and the bundled Reviewer is instructed not to edit/merge the candidate it audits.
- Who acts on findings: the workflow's approval check and repair loop return `request_changes` concerns to the producing work node; subsequent push/check/review repeats on the corrected head. Merge additionally verifies an approval by an identity other than author/merger at the exact head.
- Evidence: [`docs/design/workflows.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/docs/design/workflows.md); [`packages/core/src/workflows/ship.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/workflows/ship.ts); [`packages/core/src/workflows/define.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/workflows/define.ts); [`packages/daemon/src/runs.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/daemon/src/runs.ts); [`packages/core/templates/agents/reviewer/instructions.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/templates/agents/reviewer/instructions.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: when no ready model from another vendor exists, the run engine can fall back to the same vendor and records that loss of vendor diversity. The positive state relies on the standard supported mode in which independent reviewer selection is available and on role/session/read-only separation plus direct artifact access, not on vendor diversity alone.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the assessed project/deployment recursion.
- Disturbance / variety regulated: provider capacity, project history, current external events and scheduled triggers are observed, but the standard distribution does not convert a model of changing external/future conditions into adaptation options that return through S3 to change present organizational capability.
- Decisive decision or feedback right: no qualifying prospective adaptation judgment/feedback right is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: provider usage forecasting, fallback routing, project memory/notes/handoff, orientation, routines/triggers, web/external connections and editable project/agent configuration.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: agents can research, react to external events and propose memory/rules, and runtime code can forecast quota exhaustion, but these paths remain current task execution, memory/governance or resource routing rather than a distinct outside-and-then adaptation function.
- Evidence: [`packages/core/src/forecast.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/forecast.ts); [`packages/core/src/routing.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/routing.ts); [`packages/core/src/projects.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/projects.ts); [`README.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: general-purpose agents can of course be tasked with future research, and custom workflows could be authored. Generic expressiveness does not establish a first-party S4 path under the Methodology.

### Absence scope

- Surfaces inspected: provider capacity forecasting/routing; project memory and orientation; routines/triggers; web/external service connections; workflow planning; shipped agent templates; project configuration/rules; roadmap/design surfaces for future capability.
- Plausible first-party paths checked: quota forecasting as prospective intelligence; project-memory consolidation; agent orientation/rule proposals; scheduled environmental reactions; custom/built-in workflows; research/reviewer templates; provider/model switching.
- Why no material first-party path remains: these mechanisms either predict a current resource window, preserve/review project context, react to configured events, or provide generic agent capability. None supplies the required external/future environmental distinction → adaptation option → returned change to current organizational capability loop in a shipped first-party mode.

## S5 — Policy and identity

- State: P
- Function: maintain durable project identity and ultimate project ground rules through an authoritative parent-owned rule surface that governs later agent operation.
- Disturbance / variety regulated: proposed changes to what the project is, how its work should be done and which durable rules/conventions future agents must follow.
- Decisive decision or feedback right: accept or reject a proposed authoritative project-rule change (`AGENTS.md`) before it becomes the rule set future project sessions receive.
- Decision owner: the legitimate self-hosted project operator/user in the first-party review flow.
- Supporting / enforcement mechanisms: project scaffold; orientation agent; inbox; `poly projects review` / app Review UI; `resolveInboxItem`; project briefing/session context injection; agent/vendor support for `AGENTS.md`.
- Closure path: current project/context or orientation agent surfaces a proposed rule/identity update into the project inbox → operator keeps or discards it → a kept `AGENTS.md` replaces the authoritative project rule file → later project sessions load/follow the changed rules.
- Boundary reachability: project creation/orientation/review and per-session project briefing are shipped first-party product paths at the pinned revision; no contributor-governance or development-only actor is needed.
- Why this is / is not agent-owned: agents can draft/propose durable rules but are explicitly prevented from making them authoritative directly. The parent operator owns the ultimate keep/discard decision; therefore the established mode is `P`, not `A`.
- Identity / ultimate-policy issue: the durable declaration of what the project is, how work is done and the ground rules all project agents must follow, rather than an approval of one ordinary tool call or merge.
- Ultimate authority in each claimed mode: parent mode only — the legitimate local project operator/user accepting or rejecting the proposed authoritative `AGENTS.md` change.
- Return-to-operation path: accepted rule file becomes the project's authoritative `AGENTS.md`; subsequent Polyphemus sessions in that project receive/read those rules and conduct later work under them.
- Evidence: [`docs/design/projects.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/docs/design/projects.md); [`packages/core/src/projects.ts`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/packages/core/src/projects.ts); [`README.md`](https://github.com/polyphemus-ai/release-rehearsal/blob/02020f3bc2829c350fd726273a7721254068925f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary tool approvals, merge gates and model-fallback questions are not used as S5 evidence. The positive mapping is limited to durable project identity/ground-rule governance and its returned effect on future sessions.

## Distributed OSS parent arrangement

The positive S5 parent mode is local to the self-hosted project/deployment being assessed. It does not infer organization-level governance for the public `polyphemus-ai/release-rehearsal` repository from the existence of multiple contributors. Repository maintainer/release governance is outside the ownership boundary.

## Self-hosted and non-human modes

The reviewed standard distribution is explicitly self-hosted. Operator participation can alter individual approvals, project rules and runtime settings. Only the function-specific S5 project-rule loop is credited as parent governance. Generic operator stop/approve/configuration actions do not create S3/S4/S5 states by themselves.

## Recursion

A Polyphemus project can contain many agent sessions, concurrent thread participants and workflow-run node sessions. They are not automatically recursive viable systems merely because they are nested/spawned. This assessment uses the project/deployment as the recursion of interest and treats individual model-driven work cells as S1 operations unless a separate metasystem function is evidenced over them.

## Variety and escalation

Polyphemus attenuates operational variety with project-scoped context, isolation, scoped connections, read-only/mutating tool distinctions, bounded workflow attempts, typed artifacts and provider routing. It amplifies response capacity through multiple models/providers, reusable skills, concurrent agents and external tools. The shared-thread stitching path preserves distinctions that concurrent interleaving would otherwise corrupt.

Escalation is explicit at several operational boundaries: mutating tools can ask the operator; fallback can ask before changing provider; workflow gates stop for a person; run limits/failures stop rather than loop forever; and agent-to-agent exchange guards can return control to a person. These are useful escalation channels but are classified by the function they actually serve; they are not separate VSM functions.

## Evidence gaps

- The S2 classification is intentionally narrow. It credits shared-thread concurrent-history interference/repair, not every queue, handoff or routing feature.
- No positive S3 is assigned from the powerful workflow state machine because the reviewed project/deployment boundary lacks a distinct whole-system current-control decision path over the active operational portfolio.
- S3* vendor diversity is best-effort: when another vendor is unavailable the engine can use the same vendor. The separate read-only reviewer session, direct artifact access and corrective return remain explicit, but deployment configuration can weaken one independence dimension.
- No S4 is inferred from future-facing wording, provider forecasts, memory, routines or general research ability.
- S5 is parent-governed only. The standard flow deliberately requires operator acceptance before agent-proposed project rules become authoritative.
