---
harness_id: s1code
project_name: S1Code
repository: https://github.com/mertcicekci0/S1Code
review_ref: 3aeb8baa16f556e15bf550ba8debdcbfcfc366bd
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# S1Code

## Review boundary

- System in focus: the first-party native Rust S1Code coding-agent runtime at frozen revision `3aeb8baa16f556e15bf550ba8debdcbfcfc366bd`, including its native engine, generation/decision adapters, deterministic policy, repository tools, approval/revalidation path, verification requirement, durable session/evidence state and interactive/headless execution.
- Purpose and identity: perform bounded software-engineering work in one selected repository by observing workspace evidence, generating concrete candidate actions, filtering/revalidating them, selecting an admissible next action, executing it, persisting resulting evidence and requiring current verification evidence before completion.
- Relevant environment: the user task and follow-ups, selected repository/workspace and Git revision, source/test state, provider responses, optional Jev decision responses, configured execution consent, durable captured evidence, session state and supported local verification commands.
- Standard-distribution boundary: the native S1Code engine and directly owned OpenAI/Claude generation adapters, rules/Jev/constrained-generation decision modes, deterministic policy, native file/search/patch/check tools, approval flow, context eviction/rehydration and session/evidence persistence are inside. Provider inference services are dependencies. The official Codex bridge and official Claude Code terminal handoff explicitly delegate execution/context ownership to those upstream runtimes and therefore cannot donate their internal organizational functions to the native boundary.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `docs/BUILD_STATUS.md`; `docs/project-checks.md`; `SECURITY.md`; `docs/adr/008-bounded-followups-and-decisions.md`; native `src/engine.rs`, `src/decisions.rs`, `src/generation*`, `src/policy*`, `src/tools*`, `src/context.rs` and session/evidence surfaces reached by supported native interactive/headless runs.
- Adjacent first-party surfaces excluded from ownership: `s1code eval`, development fixtures and protected evaluator checks; repository tests/CI/release workflows; offline demos/probes; contributor governance; the Codex bridge, Claude Code terminal handoff and Claude MCP companion where they preserve upstream host ownership instead of extending the native runtime.
- First-party operating / deployment modes considered: native interactive sessions, native headless `run`/`resume`, rules/Jev/constrained-generative selection, manual or explicit session-wide approval, supported verification commands, durable resume/recovery and reversible context eviction/rehydration.
- Recursion level: one native S1Code coding session around one task/workspace is the assessed organization. Generation, Jev selection, deterministic policy, verification and evidence storage are components of that operational loop, not separately admitted S1 units. Separate S1Code processes are serialized as writers for one canonical workspace rather than composed into a multi-S1 organization.
- Reviewed revision: `3aeb8baa16f556e15bf550ba8debdcbfcfc366bd`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

S1Code documents a native control cycle of observation, candidate construction, deterministic policy filtering, selection, revalidation, approval, execution, evidence persistence and verification. Generative providers propose plans and complete candidate actions; forced transitions can run directly, while ambiguous candidate selection can use deterministic rules, Jev or constrained generation. The first-party runtime retains exact action arguments, hashes, workspace revision and policy state and rechecks those facts before execution.

The native runtime owns repository inspection, bounded reads/search, exact replacements and recoverable patches plus a limited set of project verification commands. Completion is not accepted from model prose alone: it requires a current successful verification for the observed workspace revision and a generated completion proposal. Changed workspace state invalidates stale verification and pending action assumptions.

Policy is deterministic allow/ask/deny. Repository instructions and model output cannot grant permissions, and neither scores nor approvals can override a deny. Manual approval or explicit session-wide consent authorizes only supported actions that already pass policy and stale-state checks. The runtime checkpoints action intent, records evidence/artifacts, serializes S1Code writers per canonical workspace and refuses to silently replay uncertain interrupted effects.

Context management keeps captured evidence durable while changing only the active working set. Eviction is budget-triggered and reversible; protected evidence and dependency groups remain pinned, and rehydration restores captured bytes without rerunning the originating command. Jev may answer focused relevance/retention questions, but this remains current-task context regulation rather than a separate organizational adaptation function.

The repository also ships an evaluator. Its protected checks live outside the native tool root and are run independently after task execution, but `s1code eval` is an evaluation/development mode rather than an audit actor wired into ordinary native sessions. The evaluator documentation explicitly distinguishes fixture validation from `agent_success`, and evaluation results do not form a standard runtime corrective-return loop.

Primary evidence:

- [`README.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/README.md)
- [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md)
- [`docs/BUILD_STATUS.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/BUILD_STATUS.md)
- [`docs/project-checks.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/project-checks.md)
- [`docs/evaluation.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/evaluation.md)
- [`SECURITY.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/SECURITY.md)
- [`docs/adr/008-bounded-followups-and-decisions.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/adr/008-bounded-followups-and-decisions.md)
- [`docs/adr/010-managed-host-and-evidence-companion.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/adr/010-managed-host-and-evidence-companion.md)

## Operational model

A native task begins from user intent plus a workspace snapshot and active evidence. The generative model can plan and propose fully specified actions. The runtime constructs/validates candidates, applies deterministic policy, selects an admissible candidate through the configured first-party decision mode when selection is needed, revalidates the candidate and approval against current state, executes it, captures the result, and returns new evidence into the next model/decision step. The loop continues until current verification plus a completion proposal supports termination or a configured/runtime bound stops progress.

Rules/Jev/generative decision modes vary how an admissible candidate is selected, but they do not create separate operational units at this recursion. Durable sessions, context eviction, evidence rehydration, no-progress bounds, recovery, approval and stale-state checks support the same S1 closure.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected repository by planning from task/evidence, choosing concrete admissible repository actions, executing them, observing results and iterating until verified completion or a bounded stop.
- Disturbance / variety regulated: heterogeneous source/test state, ambiguous implementation choices, repository search/read evidence, failing checks, stale workspace revisions, patch conflicts, incomplete context and execution outcomes encountered during coding work.
- Decisive decision or feedback right: generate and, in supported autonomous decision modes, select what concrete repository-facing action to attempt next and whether the accumulated evidence supports a completion proposal, subject to first-party policy/approval constraints.
- Decision owner: the model-backed native coding actor; optional Jev or constrained generation can autonomously close ambiguous candidate selection while the generative provider owns open-ended planning/proposal generation.
- Supporting / enforcement mechanisms: deterministic allow/ask/deny policy; candidate schema; workspace hashes/revisions; approval binding; native repository/check tools; writer lock; durable journals/checkpoints/artifacts; context working-set management; cancellation and request/step bounds.
- Closure path: task/current evidence → generative proposal/candidate construction → policy filtering and first-party selection → revalidation/approval → execution → captured tool/verification evidence → evidence returns into subsequent generation/decision → next action or completion.
- Boundary reachability: ordinary native interactive and headless modes directly instantiate this engine; no application-authored orchestration or external coding runtime is required.
- Why this is / is not agent-owned: removing the model-backed planning/selection actor while leaving policy, tools and persistence intact leaves enforcement and predefined transitions but removes the open-ended coding judgment that constructs and sequences task-specific repository actions.
- Evidence: [`README.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/README.md); [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md); [`docs/BUILD_STATUS.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/BUILD_STATUS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic rules can select some candidate transitions, and human consent can gate side effects, but those mechanisms constrain or support the autonomous task actor rather than replace its open-ended planning/proposal loop. Delegated Codex/Claude modes are excluded from this S1 claim.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established at S2 level because a native task exposes one coding S1 rather than multiple distinct operational units with a concrete interference/oscillation relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: workspace writer serialization, stale-file/revision checks, candidate invalidation, provider/decision components and bounded verification are safeguards/components around one S1 rather than coordination among several S1s.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation → changed subsequent S1 behavior loop was found in the reviewed native mode.
- Why this is / is not agent-owned: generation and Jev selection participate in one action-selection pipeline and do not operate as independent environment-facing S1 units. The build-status boundary also explicitly does not claim swarms.
- Evidence: [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md); [`docs/BUILD_STATUS.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/BUILD_STATUS.md); [`SECURITY.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/SECURITY.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: separate processes or external delegated runtimes can exist, but the pinned native distribution does not compose them into one multi-S1 S1Code organization.

### Absence scope

- Surfaces inspected: native engine architecture; decision/generation roles; workspace writer lock and concurrent-edit protections; native tools/checks; session/resume/recovery; build-status limitations; Codex/Claude delegation boundaries.
- Plausible first-party paths checked: subagent/team/swarm execution; independent concurrent native coding workers; shared-workspace writer coordination; provider-plus-Jev role separation; bridge-hosted upstream agents.
- Why no material first-party path remains: no first-party native mode creates multiple distinct S1 operational actors whose interaction produces a specific disturbance regulated by an S2-specific feedback path. Serialization and stale-state checks protect one workspace but do not establish such a relation.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current organizational control function distinct from the native coding S1 and deterministic runtime safeguards was established.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. Policy, request/step budgets, no-progress checks, approvals, cancellation, writer locking and stale-state revalidation limit one task loop; they do not manage organization-wide priorities, commitments or resource allocation across operational units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic policy; candidate filtering; no-progress detection; request limits; manual/session-wide consent; persistence/recovery; current verification invalidation after workspace change.
- Closure path: not applicable; no separate whole-system current view → substantive management decision → changed organization-wide current operation loop was found.
- Why this is / is not agent-owned: when deterministic safeguards intervene, they enforce preselected runtime policy around the same S1. Jev/generative selection chooses the next task action rather than acting as a manager over a population of operational units.
- Evidence: [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md); [`SECURITY.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/SECURITY.md); [`docs/adr/008-bounded-followups-and-decisions.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/adr/008-bounded-followups-and-decisions.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the native engine is deliberately control-heavy, but strong execution control does not itself establish the Profile's organization-level S3 function.

### Absence scope

- Surfaces inspected: engine control cycle; policy/approval/revalidation; provider and decision request budgets; no-progress/retry bounds; recovery and writer locking; session continuation; verification invalidation.
- Plausible first-party paths checked: runtime supervisor; policy engine; Jev decision role; whole-task progress management; approval owner; current resource/budget controller.
- Why no material first-party path remains: located controls either enforce fixed/operator policy or select/continue one S1's task actions. No separate first-party owner receives a whole-organization current view and makes substantive organization-wide management decisions with a return path.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit role with sufficiently independent access, judgment and corrective return into ordinary native operation was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Native completion verification executes bounded project checks and the coding actor must justify completion from that evidence, but those checks are part of the same S1 feedback loop. The separate evaluator can run protected checks, yet it is not wired as an ordinary runtime auditor that sends a verdict back into current control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: supported verification commands, completion gate, evaluator protected checks, offline fixtures, CI/tests and persisted evidence.
- Closure path: not applicable; no supported independent challenge → audit judgment → corrective-control return path exists in the ordinary native coding distribution.
- Why this is / is not agent-owned: test/check output is environment evidence consumed by the same coding actor, not an independent audit judgment. `s1code eval` is a separate assessment/development surface and explicitly distinguishes evaluator/fixture validation from agent success.
- Evidence: [`docs/project-checks.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/project-checks.md); [`docs/evaluation.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/evaluation.md); [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: protected external-to-tool-root checks provide meaningful evaluation separation, but boundary reachability and runtime corrective closure are still absent for S3* classification.

### Absence scope

- Surfaces inspected: native verification/completion gate; supported project checks; evaluator and protected fixture checks; persisted evidence; CI/offline validation; decision modes and recovery paths.
- Plausible first-party paths checked: separate reviewer/judge agent; independent protected evaluator during normal runs; second-pass verification actor; evaluator verdict re-entering engine control; ordinary test/check self-review.
- Why no material first-party path remains: verification is operational evidence inside the S1 loop, while the independent evaluator is adjacent and does not feed an audit verdict into subsequent ordinary task control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective outside-and-then intelligence loop that changes S1Code organizational strategy/capability was established in the supported native runtime.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Generation can investigate the current repository/task, and context eviction/Jev retention can adapt the active working set, but those mechanisms optimize present task execution rather than sense external/future distinctions and alter organizational capability or strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: context evidence ranking/eviction, durable history, follow-ups, model/provider choice, evaluation tooling and captured metrics.
- Closure path: not applicable; no external/future sensing → adaptation option → strategic capability/current-control return loop was found.
- Why this is / is not agent-owned: Jev retention and rehydration decide what current-task evidence stays active; they do not own a future-facing adaptation program. Evaluation outputs remain development evidence rather than an autonomous runtime capability-change loop.
- Evidence: [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md); [`docs/adr/008-bounded-followups-and-decisions.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/adr/008-bounded-followups-and-decisions.md); [`docs/evaluation.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/evaluation.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: current-task planning and evidence management can be sophisticated without satisfying S4's prospective organizational adaptation threshold.

### Absence scope

- Surfaces inspected: generation/planning; context working-set control; Jev relevance/retention decisions; follow-up handling; provider/model configuration; evaluation/metrics; delegated-host companion design.
- Plausible first-party paths checked: web/external sensing, future-state planning, self-improvement, learned policy update, evaluator-driven capability change, automatic model/provider adaptation, persistent strategic memory.
- Why no material first-party path remains: all located adaptation is scoped to the present task/session or developer evaluation. No first-party runtime path autonomously converts external/future distinctions into changed organizational strategy/capability and returns that change to current operation.

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy decision function was established at the selected native-session recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Deterministic policy defines allowed/ask/deny execution boundaries, while the user may grant exact or session-wide consent for already-supported actions; neither path is an identity/ultimate-policy deliberation owned by an autonomous actor.
- Decision owner: not established.
- Supporting / enforcement mechanisms: compiled/runtime policy; workspace/path protections; approval prompts; `--auto-approve`/full-access consent; provider/model configuration; repository instructions that are explicitly unable to confer permission.
- Closure path: not applicable; no identity/ultimate-policy matter reaches a legitimate autonomous or parent S5 authority whose decision returns to govern subsequent organizational operation.
- Why this is / is not agent-owned: models cannot change the deterministic policy, approvals cannot override denies, and repository instructions cannot grant authority. The human/operator chooses operational permissions/configuration, but the reviewed evidence does not establish a higher-order identity/purpose governance loop rather than ordinary execution authorization.
- Evidence: [`SECURITY.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/SECURITY.md); [`docs/architecture.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/docs/architecture.md); [`README.md`](https://github.com/mertcicekci0/S1Code/blob/3aeb8baa16f556e15bf550ba8debdcbfcfc366bd/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strong hard policy and human approval are substantive governance/safety mechanisms but do not automatically become S5 under the Profile.

### Absence scope

- Surfaces inspected: deterministic policy semantics; approval/full-access modes; repository-instruction authority; provider/model/decision configuration; native/delegated boundary; security and recovery constraints.
- Plausible first-party paths checked: autonomous policy revision; parent-governed identity decision; purpose/constitutional update; approval escalation; repository instructions as authority; provider/model choice as strategic identity.
- Why no material first-party path remains: the standard native system enforces externally authored constraints and supports operational consent, but no identity/ultimate-policy decision-and-return loop is supplied at this recursion.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one task/session/workspace native S1Code runtime. Upstream Codex/Claude hosts are delegated external organizations when selected, not subordinate functions imported into this assessment.
- Variety: source/test state, task ambiguity, candidate actions, provider proposals, stale revisions, verification results, context pressure, approvals and execution failures are handled primarily by S1 plus deterministic supporting machinery.
- Escalation: policy may require user approval for a supported action, and impossible/denied/stale states can stop or return planning feedback. These operational escalations do not by themselves establish S3, S4 or S5.
- Unresolved evidence: no material evidence gap remained that required `?` at the frozen revision. Positive claims are limited to boundary-reachable native behavior; adjacent evaluator and delegated-host surfaces were not used to upgrade the vector.

## Assessment vector

**`A · — · — · — · — · —`**
