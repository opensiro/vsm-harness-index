---
harness_id: oh-my-agent
project_name: oh-my-agent
repository: https://github.com/first-fluke/oh-my-agent
review_ref: 428e80e93fa9e4e6e9776e755ee57af4ba5cd929
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# oh-my-agent

## Review boundary

- System in focus: the first-party oh-my-agent (OMA) multi-agent harness at pinned revision `428e80e93fa9e4e6e9776e755ee57af4ba5cd929`, including its plan/orchestrate/ultrawork/ralph workflows, OMA coordination skills, run/result contracts, independent review/judge paths, persistent event/task/run state, agent dispatch/runtime adapters, and opt-in project harness evolution loop.
- Purpose and identity: organize and verify multi-agent software-engineering work across supported coding-agent runtimes, keeping execution evidence, cross-agent coordination, current portfolio control, independent review, and optional evidence-driven harness adaptation inside one reusable harness boundary.
- Relevant environment: user-authorized software tasks, repositories/workspaces, API/data contracts, external coding-agent runtimes and model vendors, worker progress/results, tests/checks/diffs, failed or partial OMA runs, and later project tasks affected by learned skill overlays.
- Standard-distribution boundary: first-party OMA CLI/runtime, workflows, skills, persistent state/evidence machinery, native/cross-vendor dispatch adapters, reviewer/judge protocols, incident/feedback tooling and scheduled project harness evolution shipped in the pinned repository. Claude Code, Codex, Cursor, OpenCode, Gemini and other model/agent hosts remain external execution substrates; their undocumented behavior is not imported as OMA-owned organizational functionality.
- Credited operating / distribution surfaces: `/orchestrate`, `ultrawork`, `ralph`; `oma agent spawn`/native role dispatch; task boards and run/result contracts; `oma-coordination`; fresh-context QA/reviewer/judge dispatch; incident capture/promotion; `oma harness feedback`; and opt-in scheduled `oma harness evolution` in default apply mode.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/release processes and benchmark/scoring suites that evaluate OMA itself. They corroborate implementation but do not close product-harness functions unless wired into a credited runtime path.
- First-party operating / deployment modes considered: automated orchestrate; ultrawork's five-phase execution; persistent Ralph EXEC→JUDGE→REPLAN loop; manual coordination only as corroborating semantics where automated workflows actually consume the same coordination rules; and project harness evolution after an explicit one-time enable operation.
- Recursion level: one OMA-supervised multi-agent work organization. Specialist implementation/review agents are distinct S1 operational units at this level; their external vendor transports do not become separate OMA metasystems merely because they run in different CLIs.
- Reviewed revision: `428e80e93fa9e4e6e9776e755ee57af4ba5cd929`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

OMA is a cross-runtime agent harness rather than a new model provider. Its first-party workflows create plans and acceptance contracts, dispatch specialist coding agents through native host paths or `oma agent spawn`, assign separate workspaces, maintain durable task/run state, monitor current execution, and require structured result evidence. The coding agents make local implementation decisions, while OMA governs their organizational relationship.

The standard automated `orchestrate` path supplies distinct backend/frontend/mobile/QA/etc. work units. It reads the first-party coordination contract, groups work by dependency/priority tier, carries API/data contracts into worker prompts, monitors progress and process health, and can reclassify/re-dispatch work. The coordination rules name concrete cross-S1 disturbances: divergent API/data contracts and conflicting workspaces. They prescribe pausing dependent work until a contract is reconciled and splitting ownership boundaries when workspaces conflict. In the automated mode the root coordinating agent applies these rules, so S2 is not inferred from routing or shared state alone.

Current-control closure is separately visible in `orchestrate`: the coordinator keeps a whole-session task board, polls all active runs, distinguishes completion/failure/crash/no-artifact/stall, preserves partial work, and decides whether to resume or re-dispatch within retry and cost bounds. That is whole-system current commitment regulation rather than simple task decomposition.

S3* is unusually explicit. `ultrawork` requires fresh, context-isolated reviewer subagents for review passes. `ralph` requires a separately spawned JUDGE with fresh context that receives criteria/evidence but not implementer narration. Judge findings alter criterion state; failures and regressions return to REPLAN/implementation, while `orchestrate` sends QA findings back to the responsible implementation agent and repeats verification. Artifact gates additionally prevent the coordinator from declaring phases complete from narration alone.

S4 is established by the project harness evolution path, not by generic self-improvement wording. OMA records failed/blocked/partial run evidence, derives regression fixtures from pre-existing task contracts, attributes them to affected skills, optimizes future skill behavior under training/validation/final-test/isolation/negative-transfer gates, and in enabled `apply` mode installs a passing project skill overlay. The scheduler repeats this finite-budget loop and later sessions use the applied overlay. This is prospective adaptation from environment-relevant operational failures back into future capability.

No S5 closure is established. Execution policy, user authorization, constitutions, budgets, stop gates, approval prompts and workflow invariants constrain ordinary work, but no shipped path elevates an identity/ultimate-policy conflict to legitimate ultimate authority and returns a policy decision governing the OMA organization.

Primary evidence:

- [`/.agents/workflows/orchestrate.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/workflows/orchestrate.md) — automated plan/dispatch, task-board current view, monitoring, reclassification, re-dispatch and verification closure.
- [`/.agents/skills/oma-coordination/SKILL.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/skills/oma-coordination/SKILL.md) — concrete contract-divergence/workspace-conflict coordination rules and feedback into specialist behavior.
- [`/.agents/workflows/ultrawork.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/workflows/ultrawork.md) — multiple specialist S1s, current-control gates and mandatory fresh-context cross-reviewers.
- [`/.agents/workflows/ralph.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/workflows/ralph.md) — persistent EXEC/JUDGE/REPLAN loop, artifact anti-circumvention gate and corrective return.
- [`/.agents/workflows/ralph/resources/judge-protocol.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/workflows/ralph/resources/judge-protocol.md) — structurally independent verifier, evidence-only judgment, regression detection and explicit verdict/state transitions.
- [`/web/docs/guide/harness-incidents.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/web/docs/guide/harness-incidents.md) — failed-run capture, regression-fixture promotion, feedback loop and gated skill optimization.
- [`/web/docs/guide/harness-evolution.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/web/docs/guide/harness-evolution.md) — scheduled finite-budget evidence collection, optimization, default apply mode, project overlays and rollback.
- [`/.agents/skills/_shared/core/execution-policy.md`](https://github.com/first-fluke/oh-my-agent/blob/428e80e93fa9e4e6e9776e755ee57af4ba5cd929/.agents/skills/_shared/core/execution-policy.md) — ordinary authorization/clarification boundaries inspected and not promoted to S5.

## S1 — Operations

- State: A
- Function: perform specialist software-engineering transformations through autonomous implementation/review agent runs inside OMA-defined task, workspace and acceptance contracts.
- Disturbance / variety regulated: codebase-specific implementation choices, local failures, tool/runtime variation, specialist-domain uncertainty and task-specific repository state.
- Decisive decision or feedback right: each spawned implementation agent chooses its local sequence of coding/tool actions and produces a run-scoped result against its assigned acceptance contract.
- Decision owner: the executing specialist agent actor launched through an OMA native or cross-vendor dispatch path.
- Supporting / enforcement mechanisms: structured plan tasks, agent definitions, `oma agent spawn`, native dispatch adapters, isolated workspaces, result contract, progress/result artifacts and verification receipts.
- Closure path: authorized task → OMA creates/loads executable plan → specialist agent is dispatched with task/contracts/context → agent autonomously performs local implementation actions → changed files/result evidence return to OMA → result enters subsequent coordination/control/review.
- Boundary reachability: automated `orchestrate` and `ultrawork` directly spawn supported implementation agents; no downstream adopter must invent the operational work-unit relation.
- Why this is / is not agent-owned: OMA supplies organizational constraints and transport, while the specialist agent makes substantive local implementation decisions rather than replaying a fixed deterministic script.
- Evidence: `.agents/workflows/orchestrate.md`, `.agents/workflows/ultrawork.md`, shared result-contract/dispatch surfaces.
- Basis: explicit + structural
- Confidence: high
- Caveats: model/vendor internals remain external. Credit is limited to the standard OMA-created agent work unit and its first-party task/result boundary, not undocumented capabilities of Claude/Codex/etc.

## S2 — Coordination

- State: A
- Function: attenuate concrete interference among specialist S1s, especially API/data-contract divergence and workspace ownership conflict, while preserving parallel local work where safe.
- Disturbance / variety regulated: backend/frontend/mobile agents can diverge on shared API/data contracts or modify overlapping workspace areas; dependency timing can expose downstream agents to unstable upstream contracts.
- Decisive decision or feedback right: detect whether contracts/workspace ownership are conflicting, pause or defer affected downstream work, reconcile the shared contract, split ownership boundaries, then resume/re-dispatch affected S1s.
- Decision owner: the root coordinating agent executing the required OMA coordination/orchestrate workflow.
- Supporting / enforcement mechanisms: PM decomposition, priority tiers, shared API/data contracts, task board, separate workspaces/worktrees, progress/result state and coordination rules.
- Closure path: multiple specialist S1s operate against shared contract/workspace boundaries → coordinator reads progress and contract state → concrete divergence/conflict is detected → coordinator pauses/repartitions/reconciles → revised contract/ownership/instructions return to affected agents before subsequent work.
- Boundary reachability: automated `orchestrate` is required to read the first-party coordination skill before fan-out, carries contracts to each agent, and monitors alignment; the qualifying path is therefore reachable without the user manually coordinating every worker.
- Why this is / is not agent-owned: worktree isolation and tier scheduling are enforcement mechanisms, but the model coordinator owns the contextual judgment that a concrete contract/ownership disturbance exists and selects/revises the response.
- Evidence: `.agents/skills/oma-coordination/SKILL.md`, `.agents/workflows/orchestrate.md`, `.agents/workflows/ultrawork.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary parallel dispatch is not the witness; S2 rests on the explicit conflict modes plus corrective feedback to the affected S1s.

## S3 — Inside-and-now control

- State: A
- Function: maintain cohesion over the current multi-agent work portfolio by regulating active commitments, priority/dependency progression, failed/stalled work, retry/re-dispatch decisions and bounded recovery resources.
- Disturbance / variety regulated: agent failure, crash, silent no-artifact exit, stalled progress, incomplete acceptance evidence, changed specialist need, retry exhaustion and session cost pressure.
- Decisive decision or feedback right: decide whether current work counts as completed, must be preserved/retried, should be reclassified to another specialist, resumed, re-dispatched or stopped as partial/failed within current budget and authorization.
- Decision owner: the root OMA coordinating agent in automated orchestrate/ultrawork paths.
- Supporting / enforcement mechanisms: whole-session task board, plan priority/dependency state, process/run status, progress/result artifacts, result contract, retry/recovery budget, quota cap and phase gates.
- Closure path: active tasks/runs populate the task board → coordinator polls process health and result evidence across the session → distinguishes completion/failure/no-artifact/stall and current constraints → selects recovery/reclassification/re-dispatch/stop → OMA executes the changed commitment decision and updates shared state → later scheduling/reporting uses the new current portfolio.
- Boundary reachability: `/orchestrate` is explicitly an automated execution mode; first-party state and dispatch commands expose the whole-set view and intervention rights to its coordinator.
- Why this is / is not agent-owned: deterministic gates/caps constrain options, but the coordinating agent interprets heterogeneous current evidence and owns discretionary portfolio interventions such as reclassification and re-dispatch.
- Evidence: `.agents/workflows/orchestrate.md`, `.agents/workflows/ultrawork.md`, `.agents/skills/oma-coordination/SKILL.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: task decomposition alone is not credited; the positive mapping depends on the subsequent whole-session monitoring and intervention loop.
- Whole-system current view: task-board/session state plus run/progress/result evidence across all planned agents.
- Current-control decision scope: priority/dependency progression, acceptance of completed commitments, reclassification, retry/re-dispatch, preservation of partial work and bounded stop.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation/current-control claims using fresh-context reviewers and mechanically grounded artifact evidence, then return findings into corrective operation.
- Disturbance / variety regulated: implementer self-report, shared-context anchoring, rationalized shortcuts, stale PASS claims, regressions, missing execution phases and acceptance-criteria violations.
- Decisive decision or feedback right: independently classify evidence as PASS/FAIL/REGRESSED/BLOCKED or identify review findings that invalidate claimed completion.
- Decision owner: separately spawned fresh-context QA/reviewer/JUDGE agent(s), not the implementation agent or ordinary coordinator context.
- Supporting / enforcement mechanisms: CCR isolation contract, per-review fresh subagents, Ralph JUDGE protocol, evidence-only briefs, artifact paths/diffs/tests, anti-circumvention verifier, regression state transitions and run-scoped result artifacts.
- Closure path: S1/S3 produces implementation and ordinary completion claims → independent reviewer/judge receives complementary raw artifacts/evidence without implementer narration → reviewer returns verdict/findings → FAIL/REGRESSED changes criterion/task state and sends work to REPLAN or back to implementation → corrected work is re-verified before completion.
- Boundary reachability: fresh-context review is mandatory in `ultrawork`; Ralph's spawned judge is the default operating path, with inline judging explicitly recorded only as an independence downgrade fallback.
- Why this is / is not agent-owned: the audit judgment is produced by an independent reviewer agent. Deterministic state-transition/artifact machinery transports/enforces that judgment but does not substitute for the auditor.
- Evidence: `.agents/workflows/ultrawork.md`, `.agents/workflows/ralph.md`, `.agents/workflows/ralph/resources/judge-protocol.md`, `.agents/workflows/orchestrate.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: repository benchmark scorers are excluded; the positive witness is the deployed workflow's structurally independent reviewer/judge path and corrective return.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert evidence from failed/blocked/partial project runs into evaluated skill adaptations that change later OMA behavior on similar work.
- Disturbance / variety regulated: recurring mismatch between current skill guidance and project-environment acceptance contracts, observed failed outputs, negative transfer risk and changes in the managed skill base.
- Decisive decision or feedback right: derive/attribute a regression case from recorded operational evidence, generate candidate skill adaptations, evaluate alternatives, and install a passing project overlay in enabled apply mode.
- Decision owner: first-party optimization agent/path owns candidate adaptation generation; evaluation gates qualify the result and the enabled scheduled evolution controller applies the passing candidate automatically.
- Supporting / enforcement mechanisms: tracked run evidence, acceptance contracts, incident capture/promotion, judge rubrics, skill attribution/routing, optimizer, train/validation/final-test/isolation/negative-transfer checks, finite dispatch budget, persistent retry state, scheduler, overlay conflict checks and rollback history.
- Closure path: real project run fails/blocks/partially completes against a recorded acceptance contract → scheduled feedback captures and validates the failure as a regression fixture → affected skill is identified → optimizer generates an adaptation candidate → held-in/held-out/final-test and negative-transfer gates evaluate it → default enabled `apply` mode installs a project skill overlay → subsequent sessions resolve the effective skill body through the overlay and operate with changed capability.
- Boundary reachability: `oma harness evolution enable --max-dispatches ...` registers the built-in scheduler; the documented default schedule is daily and default mode is `apply`. After this explicit deployment choice, cycles close without per-change human approval.
- Why this is / is not agent-owned: the adaptation candidate is generated through the first-party optimization path from environment-relevant failure distinctions. Deterministic gates and scheduler constrain and operationalize the choice rather than inventing the semantic adaptation.
- Evidence: `web/docs/guide/harness-incidents.md`, `web/docs/guide/harness-evolution.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary memory, lessons and repository self-development are not the witness. S4 is credited only to the opt-in deployed project-evolution mode whose accepted changes feed future project operation.
- External distinction: actual project tasks, acceptance contracts, preserved outputs and failure evidence reveal where the current harness/skill fails to cope with its project environment.
- Future / prospective distinction: each validated incident becomes a regression case used to form and test a skill revision intended to prevent recurrence on later tasks.
- Adaptation option generated: candidate project skill overlay/diff with recorded parent/candidate hashes and evaluation evidence.
- Path back into current capability / S3: a passing overlay becomes the effective project skill body; later OMA sessions use it in operational/coordination/control workflows, while conflicts/rollback preserve control over present capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the reviewed OMA recursion.
- Disturbance / variety regulated: user authorization, scope limits, build permission, cost caps, constitutions, workflow invariants and approval/clarification paths constrain work but remain ordinary operational/governance boundaries rather than identity-level adjudication.
- Decisive decision or feedback right: none established for an identity/ultimate-policy issue at the OMA organization level.
- Decision owner: none established.
- Supporting / enforcement mechanisms: execution policy, user authorization, clarification protocol, phase gates, cost/retry caps, static constitutions/configuration and explicit approval requirements for out-of-scope/irreversible work.
- Closure path: not applicable; inspected human and policy paths approve or bound ordinary task execution but do not demonstrate an identity/purpose conflict reaching legitimate ultimate authority and returning as organization-level policy.
- Why this is / is not agent-owned: OMA's coordinator and workers operate under supplied purpose and authorization. They do not own ultimate identity authority, and ordinary human final say over task scope is explicitly insufficient for S5 under the Profile.
- Evidence: `.agents/skills/_shared/core/execution-policy.md`, `orchestrate`/`ultrawork`/`ralph` workflow gates, configuration/constitution surfaces.
- Basis: explicit + absence review
- Confidence: high
- Caveats: project owners can change configuration, skills and evolution mode, but editable policy/configuration is not itself a runtime S5 function.

### Absence scope

- Surfaces inspected: shared execution/authorization policy, clarification rules, workflow phase gates, user approval requirements, model/vendor configuration, cost/retry limits, constitutions, skill/evolution enablement and rollback controls.
- Plausible first-party paths checked: approval for new/out-of-scope actions, authorization persistence, explicit user approval before abridging required workflow structure, build permission, project evolution enable/disable/mode selection, and human rollback of overlays.
- Why no material first-party path remains: all inspected paths constrain ordinary execution or deployment configuration. None establishes an identity/ultimate-policy dispute, legitimate ultimate authority at the chosen recursion, and a returned policy decision that closes unresolved S3–S4 tension.

## Distributed OSS parent arrangement

Repository maintainers govern OMA development, but that OSS development organization is outside the deployed harness boundary. Project users remain legitimate authorities over task authorization and deployment configuration; those ordinary controls do not create a published `P` mode for S2/S3/S4/S5. In particular, enabling or disabling autonomous harness evolution is a deployment choice, while the credited S4 decision loop inside enabled apply mode closes without per-adaptation parent approval.

## Self-hosted and non-human modes

OMA is local/self-hostable and can orchestrate supported external coding-agent runtimes. Automated orchestrate, fresh-context reviewer paths and enabled scheduled harness evolution can close their credited functions without continuous human supervision. Human authorization still bounds scope and can disable/rollback automation, but those constraints do not transfer ownership of the credited organizational judgments.

## Recursion

Specialist implementation agents are S1 units at the OMA-supervised project recursion. A vendor runtime or spawned child may itself contain richer internal organization, but OMA does not inherit those internal VSM functions. The reviewed metasystem is the OMA coordination/control/audit/adaptation layer governing the work units it dispatches and observes.

## Variety and escalation

Parallel specialists amplify operational variety. Contract checkpoints, workspace separation and feedback damp cross-unit interference. Task-board/run evidence gives S3 enough current variety to intervene by exception. Fresh independent reviewers add a complementary channel that can override routine completion claims. Failed operational evidence can be escalated temporally into S4 as a regression fixture, where a gated adaptation may change future capability.

## Evidence gaps

No evidence gap large enough to require `?` remains for the six published states at the pinned revision. Future reassessment should distinguish any newly introduced identity-level governance from ordinary authorization and should re-check whether evolution promotion gains a separately parent-owned approval mode that would justify a composite S4 state.
