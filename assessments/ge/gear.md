---
harness_id: gear
project_name: Gear
repository: https://github.com/rsi-gear/gear
review_ref: 74b8ff873a831930611dd0f0dfd680d91d5212a9
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gear

## Review boundary

- System in focus: the supported Gear Refine optimization organization: packaged Meta-agent instructions, lease/file/evidence gateway, refinement/search service and operator control over evolution/champion state.
- Purpose and identity: produce and retain evidence-backed changes to a supplied target harness using sealed seed/held-out evaluation policy.
- Relevant environment: user-authorized target source, benchmark results/trajectories, compatible Meta-agent host, external Hitch/target runtimes and finite generation/evaluation budgets.
- Standard-distribution boundary: published rsi-gear package, bundled Refine skill and its native DSH/CLI gateway plus concrete candidate/workspace/refinement/search machinery.
- Credited operating / distribution surfaces: skills/refine/SKILL.md and protocol; src/meta/skill.ts; src/skill/{gateway,files,control-plane}.ts; src/candidate/workspace.ts; src/refine/service.ts; src/search/ and promotion rules.
- Adjacent first-party surfaces excluded from ownership: marketing/benchmark claims, repository tests/dev workflows, example custom algorithms/parent policies, experimental model-training/joint-learning path. External Meta host reasoning engine and target agents/evaluators supply execution/evidence but do not donate their internal VSM functions.
- First-party operating / deployment modes considered: official installed Refine skill in a compatible host; DSH native refine_request or CLI/socket transport; staged search, candidate claims, finalization, operator status/rerun/publish/rollback. This assesses the supported composition, not a bare deterministic service without a Meta actor.
- Recursion level: one Gear-managed refinement installation with candidate-production work cells. Target-harness task execution is an evaluated adjacent system, not the Gear Meta organization's own business operations.
- Reviewed revision: `rsi-gear/gear@74b8ff873a831930611dd0f0dfd680d91d5212a9`, frozen intake #2412 / controller #2413.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [packaged skill](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/SKILL.md) instructs its Meta actor to claim work, diagnose observed seed failures, read/edit scoped candidates, justify a transferable intervention, check and finalize or decline. [src/meta/skill.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/meta/skill.ts) binds one client/runtime identity to a candidate lease and rejects stale or different clients. [src/skill/gateway.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/gateway.ts) routes authenticated capabilities; [src/skill/files.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/files.ts) restricts access to owned candidate paths. [src/refine/service.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/refine/service.ts) drives baseline/candidate evaluation, selection, held-out checks, immutable promotion and recovery. [src/search/promotion.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/search/promotion.ts) applies configured comparison/regression gates. Operators can inspect all evolutions/rounds and explicitly publish or roll back accepted champion state; these are actual returned changes, not merely dashboard labels.

## Operational model

Operational S1 is production of justified candidate harness changes by Meta agents under the bundled first-party Refine procedure. A supported host provides the underlying model/tool engine; Gear supplies the candidate/evidence organization and reachable owner instructions. No claim is made about internal functions of Codex/DSH/Claude or target workers. Candidate isolation and exclusive claim/commit machinery regulate interference; the installed operator owns whole-refinement current intervention. Target optimization is the primary transformation at this recursion, so it is not automatically Gear-level S4.

## S1 — Operations

- State: A
- Function: produce evidence-backed editable candidate harness changes or justified no-change dispositions.
- Disturbance / variety regulated: heterogeneous failures/trajectories, incomplete diagnostics, unsafe/task-specific proposals and candidate validation feedback.
- Decisive decision or feedback right: diagnose a harness gap, select an intervention and rationale, edit/check, then finalize or decline.
- Decision owner: the Meta agent following Gear's packaged Refine skill in the supported installed-host mode.
- Supporting / enforcement mechanisms: host model/tool executor, scoped candidate APIs, lease broker, evidence receipts, compiler checks and evaluation/promotion service.
- Closure path: assignment seed evidence → Meta inspection/edits → candidate.check feedback → finalize/decline → service evaluates and retains or rejects result for subsequent rounds.
- Boundary reachability: README's normal quickstart installs the bundled skill; its protocol invokes the implemented gateway/lease/file/finalization methods. No developer-authored proposal controller is needed in that mode.
- Why this is / is not agent-owned: the service alone cannot invent a semantic intervention; removing the Meta actor leaves candidates unproduced. Host infrastructure supports this specific first-party procedure, without donating arbitrary host functions.
- Evidence: [skills/refine/SKILL.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/SKILL.md); [skills/refine/references/protocol.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/references/protocol.md); [src/skill/gateway.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/gateway.ts); [src/meta/skill.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/meta/skill.ts)
- Basis: structural
- Confidence: medium
- Caveats: A is conditional on the documented installed Refine-agent mode; the bare library/service is not itself an autonomous reasoning engine.

## S2 — Coordination

- State: C
- Function: prevent candidate/session cross-write and competing advancement of one shared refinement state.
- Distinct S1 units: separately assigned Meta candidate-production cells/clients, potentially acting on candidate workspaces and the same evolution/champion lineage.
- Inter-S1 disturbance: two clients could claim/edit the same assignment or stale work could commit over a newer candidate/champion state.
- Attenuating coordination relation: exclusive client/identity-bound candidate leases, candidate-scoped file access and round locks/compare-and-swap champion commits.
- Feedback into subsequent S1 behaviour: different/stale client is rejected; Refine instructions require dropping a stale lease and inspecting current status rather than continuing writes; accepted finalization ends that assignment.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is competing edits/advancement of the same candidate lineage, with enforced ownership/isolation and returned rejection; it is not a generic message bus.
- Disturbance / variety regulated: cross-cell state contamination and stale writer interference.
- Decisive decision or feedback right: assign/revoke scoped ownership and resolve which current candidate/round may mutate state.
- Decision owner: first-party lease/workspace/round control implements a developer-selected protocol; no autonomous coordination arbitration is established.
- Supporting / enforcement mechanisms: client/token binding, scoped workspaces, locks and CAS checks.
- Closure path: claim authorization/file mutation/commit checks reject competing or stale work; workers must refresh ownership before later actions.
- Boundary reachability: the standard gateway authorizes candidate methods through SkillMetaCoordinator and routes writes only into the active workspace; RefineService acquires locks for champion changes.
- Why this is / is not agent-owned: runtime enforcement preserves a specifically supplied coordination relation, but configured lease/lineage rules determine ownership; no A claim is made.
- Evidence: [src/meta/skill.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/meta/skill.ts); [src/skill/files.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/files.ts); [src/state/store.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/state/store.ts); [src/refine/service.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/refine/service.ts)
- Basis: structural
- Confidence: medium
- Caveats: C records function-specific first-party coordination support; not a claim of autonomous conflict negotiation or measured parallel scalability.

## S3 — Inside-and-now control

- State: P
- Function: whole-refinement current control over active commitments and the target champion in use.
- Whole-system current view: control.status/listEvolutions expose evolution/round status, candidate budgets, failures, seed results and repairable evaluations.
- Current-control decision scope: continue a selected evolution/round with focus/round commitments, repair eligible failed evaluations, publish an accepted champion as workspace default or roll back to a previously accepted version.
- Disturbance / variety regulated: failed evaluation commitments, unsuitable current champion and competing choices about continuing or deploying accepted refinement results.
- Decisive decision or feedback right: choose current continuation/intervention and which accepted champion governs subsequent use.
- Decision owner: the installation's user/operator; bundled skill reserves publish/rollback to explicit user requests.
- Supporting / enforcement mechanisms: control gateway, accepted-history verification, round lock, CAS champion/published pointer and sealed evaluation policy.
- Closure path: operator inspects current status → invokes continue/rerun/publish/rollback → service changes round commitments or stored champion/default pointer → later runs read that current accepted state.
- Boundary reachability: these are documented protocol operations implemented by gateway and RefineService, not example-only custom extensions.
- Why this is / is not agent-owned: operator selects the intervention; deterministic promotion gates do not acquire that discretionary right. No autonomous A or separate C base mode is established here.
- Evidence: [skills/refine/references/protocol.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/references/protocol.md); [src/skill/gateway.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/gateway.ts); [src/refine/service.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/refine/service.ts)
- Basis: structural
- Confidence: medium
- Caveats: parent is the local user/operator at installation recursion, not Gear's upstream maintainer. Routine candidate approval alone is not the witness; current cross-candidate/evolution status and returned champion/commitment control are.

## S3* — Complementary audit

- State: —
- Function: No complementary audit loop established beyond normal evaluation/selection.
- Disturbance / variety regulated: LLM candidate assessment, hidden held-out evaluation, trajectory access, diagnosis receipts and evidence parity checks were tested as possible audit.
- Decisive decision or feedback right: no qualifying loop for this function at the declared Gear refinement boundary.
- Decision owner: Meta agents own candidate production; operators and sealed policy retain their explicit rights.
- Supporting / enforcement mechanisms: src/selection/llm-verifier.ts, src/search/promotion.ts, src/refine/service.ts
- Closure path: These form the ordinary candidate-production/acceptance pipeline. Seed/held-out separation protects validation independence, but a mandatory verifier or extra benchmark split alone does not supply a complementary audit organization with distinct access and returned current-control judgment.
- Why this is / is not agent-owned: agentic optimization does not automatically instantiate every metasystem function.
- Evidence: [src/selection/llm-verifier.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/selection/llm-verifier.ts); [src/search/promotion.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/search/promotion.ts); [src/refine/service.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/refine/service.ts)
- Basis: structural
- Confidence: medium
- Caveats: target harness internals, arbitrary downstream plugins and experimental training are not borrowed.

### Absence scope

- Surfaces inspected: src/selection/llm-verifier.ts, src/search/promotion.ts, src/refine/service.ts, README and supported Refine protocol.
- Plausible first-party paths checked: LLM candidate assessment, hidden held-out evaluation, trajectory access, diagnosis receipts and evidence parity checks were tested as possible audit.
- Why no material first-party path remains: These form the ordinary candidate-production/acceptance pipeline. Seed/held-out separation protects validation independence, but a mandatory verifier or extra benchmark split alone does not supply a complementary audit organization with distinct access and returned current-control judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: No Gear-level outside-and-then capability-adaptation loop established in this boundary.
- Disturbance / variety regulated: External benchmark failure sensing, prospective transferable target edits, historical experience, configurable search algorithms and experimental joint training were checked.
- Decisive decision or feedback right: no qualifying loop for this function at the declared Gear refinement boundary.
- Decision owner: Meta agents own candidate production; operators and sealed policy retain their explicit rights.
- Supporting / enforcement mechanisms: skills/refine/SKILL.md, src/experience/memory.ts, src/search/engine.ts, README.md
- Closure path: Target-harness refinement is Gear's S1 deliverable; resulting target changes are not by themselves changes to Gear's own current capability. History/search selection supports that operation. The documented unfinished training/automatic seed-generation roadmap and example algorithms do not close a shipped Gear-level S3–S4 adaptation conversation or parent-return mode.
- Why this is / is not agent-owned: agentic optimization does not automatically instantiate every metasystem function.
- Evidence: [skills/refine/SKILL.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/SKILL.md); [src/experience/memory.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/experience/memory.ts); [src/search/engine.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/search/engine.ts); [README.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/README.md)
- Basis: structural
- Confidence: medium
- Caveats: target harness internals, arbitrary downstream plugins and experimental training are not borrowed.

### Absence scope

- Surfaces inspected: skills/refine/SKILL.md, src/experience/memory.ts, src/search/engine.ts, README.md, README and supported Refine protocol.
- Plausible first-party paths checked: External benchmark failure sensing, prospective transferable target edits, historical experience, configurable search algorithms and experimental joint training were checked.
- Why no material first-party path remains: Target-harness refinement is Gear's S1 deliverable; resulting target changes are not by themselves changes to Gear's own current capability. History/search selection supports that operation. The documented unfinished training/automatic seed-generation roadmap and example algorithms do not close a shipped Gear-level S3–S4 adaptation conversation or parent-return mode.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate-policy/identity closure established.
- Disturbance / variety regulated: Sealed runtime/skill identity, authorized editable scope, promotion thresholds, explicit user publication/rollback and configuration mismatch handling were checked.
- Decisive decision or feedback right: no qualifying loop for this function at the declared Gear refinement boundary.
- Decision owner: Meta agents own candidate production; operators and sealed policy retain their explicit rights.
- Supporting / enforcement mechanisms: src/meta/identity.ts, src/skill/gateway.ts, src/refine/service.ts, skills/refine/SKILL.md
- Closure path: Runtime identity checks enforce the immutable evolution specification. Publication/rollback choose accepted operational artifacts, not identity/ultimate-policy adjudication. Changing the experiment's contract requires operator configuration/new admission; no identity-level escalation-to-legitimate-authority-and-return loop is supplied.
- Why this is / is not agent-owned: agentic optimization does not automatically instantiate every metasystem function.
- Evidence: [src/meta/identity.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/meta/identity.ts); [src/skill/gateway.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/skill/gateway.ts); [src/refine/service.ts](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/src/refine/service.ts); [skills/refine/SKILL.md](https://github.com/rsi-gear/gear/blob/74b8ff873a831930611dd0f0dfd680d91d5212a9/skills/refine/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: target harness internals, arbitrary downstream plugins and experimental training are not borrowed.

### Absence scope

- Surfaces inspected: src/meta/identity.ts, src/skill/gateway.ts, src/refine/service.ts, skills/refine/SKILL.md, README and supported Refine protocol.
- Plausible first-party paths checked: Sealed runtime/skill identity, authorized editable scope, promotion thresholds, explicit user publication/rollback and configuration mismatch handling were checked.
- Why no material first-party path remains: Runtime identity checks enforce the immutable evolution specification. Publication/rollback choose accepted operational artifacts, not identity/ultimate-policy adjudication. Changing the experiment's contract requires operator configuration/new admission; no identity-level escalation-to-legitimate-authority-and-return loop is supplied.

## Distributed OSS parent arrangement

Positive P is local installation-operator current control only. OSS contributor/maintainer rights and supplied examples/parent-policy concern other responsibilities and are not credited as project-level VSM governance.

## Self-hosted and non-human modes

Supported hosted-skill and native DSH transports reach the same owned candidate/evidence methods. Headless deterministic service use lacks a candidate-producing actor unless that supported Meta composition is supplied. No uninspected custom host or algorithm receives an automatic grade.

## Recursion

Meta candidate work and external target task execution are distinct boundaries. Neither nested searches nor an optimization loop prove recursively viable organizations.

## Variety and escalation

Seed diagnoses attenuate trajectory volume; scoped capabilities and held-out withholding constrain proposal variety. Stale leases, finalization readiness and recoverable failures return explicit repair/status feedback. operatorAction messages expose limitations but do not alone establish S5 or an algedonic channel.

## Evidence gaps

Pinned source, shipped skill/protocol and configuration surfaces reviewed; no native Node/npm runtime on host, so TypeScript tests not run. Bundled Python syntax compilation only; no Hitch, target agent, live model, training or benchmark execution. Claims describe supported-mode structure/ownership, not benchmark gains, causal improvement or bug-free deployment.
