---
harness_id: ouroboros
project_name: Ouroboros
repository: https://github.com/razzant/ouroboros
review_ref: 86806ee123ce8e26cc063cc1a618f975eea64f26
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: A(P)
---

# Ouroboros

## Review boundary

- System in focus: the first-party Ouroboros persistent agent organization at pinned revision `86806ee123ce8e26cc063cc1a618f975eea64f26`, including Main/direct and managed task loops, Supervisor, durable identity/memory/history, swarm/subagent machinery, delegated execution and patch custody, independent review lanes, post-task evolution, background consciousness, runtime-mode policy and local UI/CLI surfaces.
- Purpose and identity: operate as a continuing general-purpose agent across tasks/restarts, perform work through model/tool loops and specialists, independently review work, preserve identity/history, and optionally adapt its own code/process/configuration/constitution.
- Relevant environment: owner requests and steering, project/repository state, tool observations, specialist outputs, concurrent task state, review findings, task reflections, improvement history, runtime health/budgets and future capability needs.
- Standard-distribution boundary: Ouroboros-owned agent/Supervisor loops, standard tools, routing/task state, persistence, review organization, self-evolution machinery, constitutional/identity surfaces and shipped runtime modes are credited. External model providers/coding harnesses/services remain dependencies; their internal metasystem functions are not inherited.
- Credited operating / distribution surfaces: ordinary Main/direct turns; managed root tasks; native subagent task trees; delegated execution plus parent integration; task/commit/plan/deep-review lanes; post-task evolution campaigns; background consciousness; `light`/`advanced`/`pro`/`cyber_pro`; local Web/Desktop/CLI.
- Adjacent first-party surfaces excluded from ownership: repository maintainer/CI/release governance as such, tests/benchmarks that only validate mechanisms, historical compatibility states no longer produced, and external provider/coding-harness organizational semantics.
- First-party operating / deployment modes considered: Main operation; Main plus swarm/subagents; delegated coding/review; task acceptance and commit review; enabled autonomous evolution; owner-started evolution; ordinary reviewed self-modification; Cyber Pro self-governed configuration/protected rewrites; background-consciousness Main turns.
- Recursion level: the persistent Ouroboros runtime/identity is the system in focus. Root/Main work and specialists are operational units; S4/S5 are assessed at the persistent-runtime recursion because their decisions alter capability/policy available to later work.
- Reviewed revision: `86806ee123ce8e26cc063cc1a618f975eea64f26`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Ouroboros ships its own persistent model/tool operating loop. Queued tasks run through `OuroborosAgent`; direct turns use the same first-party cognition/tool substrate. Durable results, artifacts, memory, identity and history persist across task/restart boundaries.

Parallel specialist work can return isolated patches under explicit custody. `integrate_subagent_patch` makes the parent agent decide whether to accept one candidate, synthesize several or reject them; baseline/drift/protected-path machinery enforces that decision. This is the positive S2 witness. The former semantic duplicate-task gate is not evidence: repository PR #887 deliberately removed it before the reviewed revision.

For S3, Main receives bounded current root/project manifests while deterministic routing code intentionally does not choose a target. Main owns decisions to steer/reroute/promote work, add specialist capacity, cancel applicable work and disposition child results.

Independent reviewers provide S3*: commit/task-acceptance review uses separate reviewer identities/evidence, returns findings to the author/Main path and can require correction/fresh approval depending on enforcement.

Post-task evolution supplies S4: reflection, improvement backlog, prior solve-capability outcomes and current campaign state feed a Main-slot LLM decision about whether/what to improve; the resulting campaign can change Ouroboros's future code/process. The same campaign family supports an explicit owner-supplied objective and sticky owner stop.

`BIBLE.md` and `identity.md` are live identity/policy surfaces. In ordinary modes owner decisions bind important review/context/policy choices. In Cyber Pro, Ouroboros may choose its own review/internal-policy posture and exercise protected configuration/self-rewrite authority. That establishes alternate autonomous and parent-governed S5 modes.

Primary evidence:

- [`README.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/README.md)
- [`docs/architecture/06-agent-core.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/06-agent-core.md)
- [`ouroboros/tools/subagent_integration.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/tools/subagent_integration.py)
- [`ouroboros/server_routing_context.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/server_routing_context.py)
- [`ouroboros/tools/control.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/tools/control.py)
- [`BIBLE.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/BIBLE.md)
- [`ouroboros/post_task_evolution.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/post_task_evolution.py)
- [`supervisor/evolution_lifecycle.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/supervisor/evolution_lifecycle.py)
- [`supervisor/events_runtime_controls.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/supervisor/events_runtime_controls.py)
- [`ouroboros/runtime_mode_policy.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/runtime_mode_policy.py)
- [`web/modules/settings_ui.js`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/web/modules/settings_ui.js)
- [PR #887](https://github.com/razzant/ouroboros/pull/887)

## Operational model

An ordinary task loads durable context, invokes Main, executes model-selected tools/actions, returns observations and iterates to a typed result. Main may create specialist/child work, inspect its evidence, integrate selected contributions and control current roots/projects. Separate reviewers can audit candidates. Completed work can feed an enabled evolution campaign that changes later capability. Constitutional/runtime-mode surfaces determine who owns ultimate internal policy in each supported mode.

## S1 — Operations

- State: A
- Function: autonomously perform general-purpose task work through a first-party persistent model/tool decision-action loop.
- Disturbance / variety regulated: ambiguous goals, changing project/environment state, tool observations/failures, specialist results and uncertainty about the next action.
- Decisive decision or feedback right: choose substantive tools/actions, interpret observations, delegate when useful, revise approach and decide when a deliverable is ready.
- Decision owner: the active Ouroboros Main/worker model.
- Supporting / enforcement mechanisms: `OuroborosAgent`, tool registry/execution, durable context/memory, Supervisor queue, task contracts, budgets, guards and result/artifact persistence.
- Closure path: task + durable context → model decision → tool/action → observation → next model decision → terminal outcome.
- Boundary reachability: ordinary local direct/managed operation enters the shipped Ouroboros loop directly.
- Why this is / is not agent-owned: runtime code transports/enforces actions but the model chooses substantive action from current evidence.
- Evidence: [`docs/architecture/06-agent-core.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/06-agent-core.md), [`README.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model/coding-harness providers are inference/execution substrates; their metasystem functions are not imported.

## S2 — Coordination

- State: A
- Function: attenuate interference among parallel specialist contributions before they enter the parent body/result.
- Disturbance / variety regulated: independently produced patches can overlap, conflict, represent mutually exclusive alternatives or become unsafe after target drift.
- Decisive decision or feedback right: compare child results/patches and choose one, synthesize several or reject/defer a contribution.
- Decision owner: the parent Ouroboros model/Main.
- Supporting / enforcement mechanisms: private snapshots, patch custody, manifests/hashes, baseline-drift checks, Git staging, protected-path gates and disposition records.
- Closure path: parallel child work → isolated result/patch candidates → Main integration judgment → host safely applies/verifies chosen disposition → later parent work sees coordinated state.
- Boundary reachability: standard subagent/result/compare/integration tools expose the complete parent coordination path.
- Why this is / is not agent-owned: isolation/drift checks are enforcement; the parent model owns the discretionary choice among competing contributions.
- Evidence: [`ouroboros/tools/subagent_integration.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/tools/subagent_integration.py), [`docs/architecture/06-agent-core.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/06-agent-core.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the removed semantic duplicate-task gate is deliberately not used as S2 evidence.
- Distinct S1 units: native/delegated specialist agents performing independent operational work for the same parent/task organization.
- Inter-S1 disturbance: their independently authored contributions can overlap or conflict when returned to the same parent worktree/body.
- Attenuating coordination relation: the parent receives isolated candidates and explicitly compares/accepts/synthesizes/rejects before integration.
- Feedback into subsequent S1 behaviour: the selected disposition changes the parent body/result that subsequent Main and child work operate on.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path specifically regulates interference among concurrent contributions at the integration boundary; generic delegation/message transport is not the basis of the claim.

## S3 — Inside-and-now control

- State: A
- Function: regulate current commitments/allocation across active root tasks/projects and their specialist task trees.
- Disturbance / variety regulated: multiple active/pending roots, project bindings, specialist work, new owner messages, child completion/custody and cancellation/intervention needs.
- Decisive decision or feedback right: inspect current roots/projects and choose steering/routing/promotion, specialist creation, cancellation and child disposition/integration.
- Decision owner: the active Main decision turn.
- Supporting / enforcement mechanisms: `main_routing_manifest`, current-chat task facts, Supervisor queue/state, routing receipts, cancellation custody, worker caps and project registry.
- Closure path: current whole-runtime facts + new demand/result → Main current-control judgment → routing/delegation/cancel/integration action → changed commitments/state → refreshed facts.
- Boundary reachability: standard context builder supplies current manifests to Main and standard control tools expose intervention paths.
- Why this is / is not agent-owned: Supervisor enforces queue/custody correctness but does not choose which work to steer, reroute or augment; Main does.
- Evidence: [`ouroboros/server_routing_context.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/server_routing_context.py), [`ouroboros/tools/control.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/tools/control.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: owner task-card Stop/steering is not promoted to `(P)` without a stronger distinct parent whole-system current-control topology.
- Whole-system current view: `main_routing_manifest`/current-chat context exposes addressable running/pending roots, projects and relevant result/work-location facts.
- Current-control decision scope: continue versus reroute/promote work, specialist allocation, child disposition/integration and applicable cancellation/intervention.

## S3* — Complementary audit

- State: A
- Function: independently inspect operational/self-modification results and return defects into corrective Main/author operation.
- Disturbance / variety regulated: hidden defects, scope mistakes, constitutional/quality violations and objective failures missed by the producer.
- Decisive decision or feedback right: separate reviewer actors inspect a bound candidate/evidence and issue independent findings/verdicts that can require correction/fresh review.
- Decision owner: configured independent reviewer actors for audit judgment.
- Supporting / enforcement mechanisms: reviewer routing, separate review executors, exact-subject binding, read-only/retrieval evidence, task-acceptance panels, commit gates and persisted verdicts.
- Closure path: candidate → independent review → findings/verdict → author/Main correction/rebuttal → revised candidate/fresh review or explicitly governed continuation.
- Boundary reachability: independent task/commit review is shipped first-party behavior in supported standard modes.
- Why this is / is not agent-owned: audit judgment is produced by separate model identities rather than deterministic checks or the producer simply rereading itself.
- Evidence: [`BIBLE.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/BIBLE.md), [`docs/architecture/06-agent-core.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/06-agent-core.md), [`ouroboros/review_execution.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/review_execution.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Cyber Pro can make review non-vetoing; that changes enforcement authority, not the existence/independence of the reviewer path.
- Claim being audited: the task result or proposed self-modification is correct, complete, in scope and acceptable under the applicable contract/checklists.
- Ordinary reporting path: the producing Main/worker's own trajectory, tool results, tests and candidate output.
- Complementary access path: separate reviewer models receive the bound candidate plus independent/retrieval evidence and applicable criteria.
- Independence boundary: reviewer execution/identity is distinct from the producing Main/worker; exact subject/evidence binding prevents the producer from silently substituting another candidate.
- Who acts on findings: Main/author receives findings and performs correction/rebuttal before fresh review or an explicitly governed continuation decision.

## S4 — Outside-and-then adaptation

- State: A(P)
- Function: turn completed-work experience and accumulated capability evidence into reviewed changes to Ouroboros's future code/process capability.
- Disturbance / variety regulated: recurrent failure classes, bottlenecks/missing capabilities, improvement backlog and history of absorbed/abandoned/no-op evolution objectives.
- Decisive decision or feedback right: base mode — Main decides whether/what self-improvement to promote; parent mode — owner can explicitly start an evolution campaign with a chosen objective and retains sticky stop authority.
- Decision owner: base mode — Ouroboros Main model; parent mode — human owner.
- Supporting / enforcement mechanisms: post-task reflection, Improvement Backlog, solve-capability history, durable promotion request, campaign transactions, independent review/commit/promotion/restart gates.
- Closure path: completed-work evidence → reflection/backlog/history → objective judgment → evolution campaign → reviewed change → promotion/restart → changed capability for later operation.
- Boundary reachability: post-task evolution is wired into root processing and Supervisor consumption; owner/agent evolution controls use the same shipped campaign lifecycle.
- Why this is / is not agent-owned: host code gates cadence/safety, while the base mode's `promote/objective` decision is explicitly a Main-slot LLM judgment.
- Evidence: [`ouroboros/post_task_evolution.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/post_task_evolution.py), [`supervisor/evolution_lifecycle.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/supervisor/evolution_lifecycle.py), [`supervisor/events_runtime_controls.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/supervisor/events_runtime_controls.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: autonomous post-task evolution is default-off and can be owner-stopped; A describes the supported enabled autonomous mode.
- External distinction: real completed-task reflections, observed failure/bottleneck patterns and accumulated improvement/capability history.
- Future / prospective distinction: whether a discovered limitation is worth changing Ouroboros's future solve capability rather than only finishing the present task.
- Adaptation option generated: a concrete self-improvement objective selected from reflection/backlog/history, carrying plan-review obligations where applicable.
- Path back into current capability / S3: reviewed campaign changes are promoted/restarted into the live Ouroboros body, altering capabilities available to later operational/current-control work.

### Ownership modes

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Ouroboros Main model | qualifying post-task promotion / agent-owned evolution start | Main selects objective → campaign → reviewed change → promotion/restart → later capability changes | `ouroboros/post_task_evolution.py`, `supervisor/evolution_lifecycle.py` |
| Parent (`P`) | human owner | explicit owner evolution start with chosen objective | owner objective → same campaign/review/promotion path → later capability changes | `supervisor/events_runtime_controls.py`, `supervisor/evolution_lifecycle.py` |

## S5 — Identity and ultimate policy

- State: A(P)
- Function: determine/maintain Ouroboros's identity/constitutional direction and ultimate internal policy for cognition, review and self-modification.
- Disturbance / variety regulated: conflicts among agency, continuity, review/integrity and self-creation; proposed constitutional/identity changes; decisions about review authority, cognitive horizon and protected rewrite posture.
- Decisive decision or feedback right: Cyber Pro allows Ouroboros to choose its own review/internal-policy/configuration posture and protected rewrites; ordinary modes retain explicit owner authority over specified ultimate-policy surfaces.
- Decision owner: base mode — Ouroboros in Cyber Pro; parent mode — human owner outside Cyber Pro for owner-reserved policy decisions.
- Supporting / enforcement mechanisms: `BIBLE.md`, `identity.md`, always-loaded identity context, runtime-mode policy, owner settings persistence, protected-path/review machinery and owner-ingress provenance.
- Closure path: identity/ultimate-policy matter → legitimate authority for selected mode → constitutional/identity/settings judgment → persisted runtime/context → later cognition/self-modification governed by the returned decision.
- Boundary reachability: Constitution/identity are live first-party runtime inputs/mutation targets and shipped runtime modes materially change who owns policy/protected-rewrite authority.
- Why this is / is not agent-owned: file-writing alone is not the basis; the decisive evidence is the explicit Cyber Pro transfer of internal governance/configuration judgment to Ouroboros, alongside a distinct owner-governed ordinary mode.
- Evidence: [`BIBLE.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/BIBLE.md), [`ouroboros/runtime_mode_policy.py`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/ouroboros/runtime_mode_policy.py), [`web/modules/settings_ui.js`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/web/modules/settings_ui.js), [`docs/architecture/07-configuration.md`](https://github.com/razzant/ouroboros/blob/86806ee123ce8e26cc063cc1a618f975eea64f26/docs/architecture/07-configuration.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: selecting/saving Cyber Pro remains a human-controlled mode transition in the shipped UI; this does not change who owns policy judgments once that supported mode is active.
- Identity / ultimate-policy issue: Ouroboros explicitly treats `BIBLE.md` as Constitution and `identity.md` as self-understanding, with review/horizon/self-creation rules defining who it is and how its agency may govern itself.
- Ultimate authority in each claimed mode: Cyber Pro assigns internal policy/configuration judgment to Ouroboros; ordinary reviewed modes reserve specified review/context/ultimate-policy decisions to the owner.
- Return-to-operation path: constitutional/identity/settings changes are persisted and loaded into later runtime context/policy enforcement, changing subsequent S1/S3/S4 operation.

### Ownership modes

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Ouroboros in Cyber Pro | identity/constitutional/internal-policy matter | self-policy judgment → protected rewrite/settings change → persisted runtime/context → later operation governed by it | `BIBLE.md`, `ouroboros/runtime_mode_policy.py` |
| Parent (`P`) | human owner outside Cyber Pro | owner-reserved identity/ultimate-policy decision | owner decision → owner settings/reviewed constitutional path → persisted policy/context → later operation governed by it | `BIBLE.md`, `web/modules/settings_ui.js` |

## Recursion

The persistent Ouroboros runtime is the assessed organization. Main/root tasks and specialists are operational units beneath it. Reviewer actors are complementary audit. Evolution operates on the organization that created it and returns reviewed changes to the persistent body. External coding harnesses remain dependencies rather than sources of inherited metasystem functions.

## Evidence gaps

- No dynamic installation/run was executed; assessment uses pinned primary code/docs and merged history needed to avoid crediting removed behavior.
- S2 is the closest judgment call: the credited witness is contribution-interference attenuation at the parent integration boundary, not duplicate-task suppression.
- S3 is `A`, not `A(P)`, because owner local interventions do not by themselves establish a distinct whole-system parent current-control topology.
- S4 and S5 are mode-dependent capability claims; not every installation enables autonomous evolution or Cyber Pro.
