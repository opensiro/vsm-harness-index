---
harness_id: agnes-harness
project_name: Agnes Harness
repository: https://github.com/AgnesAI-Labs/agnes-harness
review_ref: 98bc11572ba162bcdf6ce2b29612a44508faf951
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agnes Harness

## Review boundary

- System in focus: the source-built AGH task/session harness, with Host-wired Base/Code extensions and supported subagent/batch modes.
- Purpose and identity: deliver tool-using tasks and reusable business integrations through shared CLI/Web/SDK sessions.
- Relevant environment: workspace files, model providers, tools/MCP, plugins, optional devices and supervising users.
- Standard-distribution boundary: daemon/worker → Host → Core with bundled presets, tools, subagent isolation, budget and resource controls.
- Credited operating / distribution surfaces: packages/core, host, daemon, base/extensions and code/presets; their wired public source-build composition.
- Adjacent first-party surfaces excluded from ownership: repository CI/guards, tests, benchmark claims, contributor governance, sample business/device plugins; planned Jev integration is not a shipped owner.
- First-party operating / deployment modes considered: standard CLI/Web/SDK, source-built supervised sessions, worktree/shared child tasks, daemon batches, resource/approval management; optional MHS is a tool boundary.
- Recursion level: one session's operational task tree/batch; not the Agnes company or contributor organization.
- Reviewed revision: `98bc11572ba162bcdf6ce2b29612a44508faf951`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Clients share daemon-backed sessions; workers host assembled Host/Core instances. Core advances inference/tool steps with durable event facts, approvals, cancellation and recovery. Base extensions expose standard tools, child spawn/collect/cancel, Git worktree isolation, budgets, loop hygiene and batch start/status/cancel. Host resolves actual policy and child factories; the subagent extension's inert default export is not mistaken for the Host-wired ecosystem factory. Standard presets allow model tool choice within configured bounds. Batch workers process files in isolated read-only sessions and report aggregate counts/spend. Skill/package/MCP governance updates mounted capabilities through reviewed resource snapshots. The default verifier is pure Tier-0 schema/repetition/progress checking with a repair ladder, not an independent auditor. Jev is documented as planned; the current Core loop supplies execution.

## Operational model

Model-directed task sessions and delegated child/file sessions are operational units. Runtime persistence, authorization, credit reservations and OS confinement execute or constrain choices. Worktree separation is a concrete inter-unit conflict-attenuation constructor. Child/batch credit and intervention surfaces expose current-control decisions, but a coherent supervising policy must still be composed; a generic task-spawning model is not automatically credited with every metasystem decision. Human approval and resource trust remain specific authorization rights, not automatically S5.

## S1 — Operations

- State: A
- Function: execute requested tool-using work
- Disturbance / variety regulated: unknown files/business state, tool failures and task revisions
- Decisive decision or feedback right: select model-proposed actions, revise work from tool results and produce a result
- Decision owner: model actor in the shipped Core/Host task loop
- Supporting / enforcement mechanisms: inference adapters, ledger, tool dispatcher, authorization and sandbox
- Closure path: model call → authorized tool execution → result/event state → next model decision
- Why this is / is not agent-owned: without the model the state machine cannot choose substantive task actions
- Boundary reachability: source-build standard preset and Host assembly wire provider, tools and Core inference directly; custom organizational glue is unnecessary
- Evidence: [packages/core/src/step/inference.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/core/src/step/inference.ts), [packages/core/src/step/session.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/core/src/step/session.ts), [packages/host/src/assemble.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/host/src/assemble.ts), [packages/code/presets/standard.yaml](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/code/presets/standard.yaml).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S2 — Coordination

- State: C
- Function: attenuate mutable-workspace interference among concurrent child tasks
- Disturbance / variety regulated: parallel child writes colliding in one Git checkout and unsafe cleanup of unfinished work
- Decisive decision or feedback right: select isolated/shared child workspace and reconcile retained child work
- Decision owner: first-party worktree constructor; autonomous conflict/reconciliation owner still requires composition
- Supporting / enforcement mechanisms: unique branches/worktrees, durable child workspace binding, dirty/unmerged retention and child lifecycle
- Closure path: spawn chooses isolation → worktree bound before child resume → child works separately → retained/cleanup state informs collection and later integration
- Why this is / is not agent-owned: deterministic isolation is concrete S2 support, not evidence that the runtime owns discretionary cross-unit reconciliation
- Boundary reachability: Host ecosystem supplies createSubagentExtension with resolved preset limits and gitWorktrees; standard preset requests worktree isolation
- Distinct S1 units: concurrent independent child task sessions acting on project files
- Inter-S1 disturbance: shared-checkout write collision and cleanup that could lose another child’s work
- Attenuating coordination relation: per-child Git worktrees plus binding and conservative dirty/unmerged/in-use retention
- Feedback into subsequent S1 behaviour: child cwd is rebound before execution; later work/integration sees retained paths rather than overwritten shared files
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: workspace isolation and retention directly attenuate an identified mutable-state conflict; spawn/collect alone would not qualify
- Evidence: [packages/base/extensions/subagent/src/tools.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/subagent/src/tools.ts), [packages/base/extensions/subagent/src/worktree.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/subagent/src/worktree.ts), [packages/base/src/ecosystem.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/src/ecosystem.ts), [packages/code/presets/standard.yaml](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/code/presets/standard.yaml).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S3 — Inside-and-now control

- State: C
- Function: construct resource/commitment supervision for a task tree or batch
- Disturbance / variety regulated: aggregate credit exhaustion, excess child work and continued spending on undesired file processing
- Decisive decision or feedback right: set child/batch budgets and concurrency, inspect current status/spend, cancel child subtrees or a batch
- Decision owner: a supervising agent/policy must compose these first-party controls into a whole-task regulation loop; operator may issue direct commands
- Supporting / enforcement mechanisms: credit reservations, fan-out/depth enforcement, durable batch status and cancellation
- Closure path: status/credits → supervisor resource judgment → spawn budget or cancel → changed running/pending work; concrete primitives exist without a shipped dedicated regulator
- Why this is / is not agent-owned: fixed credit gates do not own budget choices; tool availability alone does not establish autonomous whole-system judgment
- Boundary reachability: bundled child/batch tools and Host/daemon ports expose the controls in supported sessions; no adjacent CI actor is borrowed
- Whole-system current view: batch status reports total/running/pending/done/failed files and spent/budget credits; child collection returns status and credits
- Current-control decision scope: task-tree/batch resource commitments and subtree/batch intervention, within preset limits
- Evidence: [packages/base/extensions/subagent/src/tools.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/subagent/src/tools.ts), [packages/base/extensions/batch/src/tools.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/batch/src/tools.ts), [packages/core/src/child/runtime-budget.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/core/src/child/runtime-budget.ts), [docs/guide/batch.md](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/docs/guide/batch.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit established
- Disturbance / variety regulated: schema, repeated-write and no-progress errors in ordinary production
- Decisive decision or feedback right: Tier-0 verification and repair/park/escalate transitions
- Decision owner: pure verifier/repair policy, not a separate independent audit judgment owner
- Supporting / enforcement mechanisms: verifier seam, event ledger, repair ladder and approval continuation
- Closure path: routine check → repair or park → model continuation/operator decision
- Why this is / is not agent-owned: mandatory deterministic loop hygiene is not complementary audit
- Evidence: [packages/base/extensions/loop-hygiene/src/verifier.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/loop-hygiene/src/verifier.ts), [packages/base/extensions/loop-hygiene/src/repair.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/base/extensions/loop-hygiene/src/repair.ts), [packages/core/src/step/verifier-continuation.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/core/src/step/verifier-continuation.ts).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: default verifier/repair, verification seam, continuation, logs and supported extension assembly
- Plausible first-party paths checked: verifier model-route label, replaceable seam, raw ledger and operator continuation
- Why no material first-party path remains: default verification uses production shape/history checks; a generic replacement seam requires custom independent auditing logic and is not itself an S3*-specific complementary access/ownership path

## S4 — Outside-and-then intelligence

- State: —
- Function: no external prospective capability-adaptation loop established
- Disturbance / variety regulated: task context, reusable methods and plugin/version changes
- Decisive decision or feedback right: review/enable resource revisions or revise task instructions
- Decision owner: users/plugin authors; no shipped future-environment adaptation decision owner
- Supporting / enforcement mechanisms: Skill Helper confirmation, resource snapshots, MCP/package mounting and context compaction
- Closure path: accepted resource state changes current tools; no evidenced external prospective option-generation/return cycle
- Why this is / is not agent-owned: retained methods and hot updates are capability mechanisms, not automatically S4
- Evidence: [docs/guide/skills.md](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/docs/guide/skills.md), [docs/develop/architecture.md](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/docs/develop/architecture.md), [packages/host/src/resources/skill-preload.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/host/src/resources/skill-preload.ts).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: skills/resource governance, package/MCP mounting, batch and model configuration, supported operator modes
- Plausible first-party paths checked: Skill Helper install request, resource revision approval, incremental refresh, model/provider configuration
- Why no material first-party path remains: these close installation/context management without a first-party externally and prospectively oriented adaptation loop; future custom plugins are not credited

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure established
- Disturbance / variety regulated: tool permissions, package trust and session execution constraints
- Decisive decision or feedback right: approve a tool/resource or select session permission mode
- Decision owner: user/configured authorization policy, not an evidenced identity-level decision-return arrangement
- Supporting / enforcement mechanisms: approval/grant persistence, security denials, resource trust and policy matching
- Closure path: tool/resource authorization changes allowed operation, without a specific identity-level referral/return
- Why this is / is not agent-owned: ordinary permission authority does not establish S5
- Evidence: [docs/guide/security.md](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/docs/guide/security.md), [packages/code/presets/standard.yaml](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/code/presets/standard.yaml), [packages/core/src/step/approval-grants.ts](https://github.com/AgnesAI-Labs/agnes-harness/blob/98bc11572ba162bcdf6ce2b29612a44508faf951/packages/core/src/step/approval-grants.ts).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: presets/persona, authorization, resource trust, session mode changes and contributor boundary
- Plausible first-party paths checked: manual/smart/off approvals, Full permissions, installation confirmation and protected profile state
- Why no material first-party path remains: no supported identity/ultimate-policy issue → legitimate ultimate authority → authoritative return loop is supplied; configuration and operational approvals remain constraints

## Distributed OSS parent arrangement

Source maintainers and business-plugin developers remain outside each task tree. Multiple contributors do not establish organization-level parent governance.

## Self-hosted and non-human modes

Source-built CLI/Web/SDK sessions support supervised approvals, cancellation and resource management. These direct controls do not alone establish a parent S3/S4/S5 mode. Batch supervision remains an exposed composition surface.

## Recursion

Child sessions and batch file workers are operational decomposition; no complete viable metasystem per child is inferred.

## Variety and escalation

Model/tool results and durable facts carry task variety. Worktrees attenuate file interference; depth, credit, approval and sandbox gates constrain action. Park/repair/approval returns are task-local; no algedonic status is inferred from a failure code.

## Evidence gaps

No provider-backed, device or full application execution was performed. The dependency-heavy TypeScript suite was not run. The native public-doc verifier passed after hydrating omitted sparse-checkout assets: 79 Markdown files, 1329 local links, 35 source checks, zero errors. This checks documentation/source consistency, not the VSM interpretation. Generic custom verifier/adaptation plugins are not credited as shipped functions.
