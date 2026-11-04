---
harness_id: posse
project_name: posse
repository: https://github.com/ranger360ai/posse
review_ref: bdd3954bb86adc2d0fac14175abe9443ba439794
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: P
---

# posse

## Review boundary

- System in focus: One installed posse work-system instance: launcher/dispatcher/cockpit, explicitly staffed first-party reference persona modes and operator-governed constitution.
- Purpose and identity: Maintain a persistent task-working crew, bind intent and constraints to sessions, dispatch durable work and return settled results or explicit blockers.
- Relevant environment: Task queues, changing code/projects, concurrent workers, vendor/model capacity and cost, runtime failures, local operator decisions.
- Standard-distribution boundary: Public Go product and embedded seed, INSTALL-supported persona/queue configuration, first-party reference PIDs and promoted instance policy. External herdr, Beads and model CLIs are support/actors explicitly bound by posse, not sources of borrowed metasystem claims.
- Credited operating / distribution surfaces: Launch/dispatch work prompts, claim/settle/worktree flow; concrete concurrency guards; operator status/pause/budget; function-specific coordinator/audit construction paths; reference advisory role and constitution promotion.
- Adjacent first-party surfaces excluded from ownership: Private instance crew, memories, measured operations and private notes are not inspected or credited. Public product-development tests/ADRs corroborate implementation but are not the assessed deployed crew. Retired tmux branch is outside the pin.
- First-party operating / deployment modes considered: Bare CLI sessions; configured dispatch/watch and reference developer/QA/reviewer/business modes per INSTALL; operator supervision and promoted constitution; optional custom coordinator only as constructor evidence. Fresh init is inert with no staffed personas, no automatically granted controller or auditor.
- Recursion level: One configured operator instance; independent worker sessions are S1 cells, while tools/substrate services are support.
- Reviewed revision: bdd3954bb86adc2d0fac14175abe9443ba439794
- Observation date: 2026-11-04
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Go product embeds a neutral seed and binds operator-selected personas, runtime profiles, environment/cage rules and task queues. Init leaves active agents empty; INSTALL describes staffing from reference PIDs. Dispatch routes/claims tasks, launches model sessions, observes outcomes and settles committed work through isolated worktrees. Concrete launch/store locks and landing checks prevent named races. Status/cockpit and pulse expose shop facts, while operator controls set constraints/pause. Verify-after creates linked after-close challenge work but does not ship a staffed auditor. A separate operator-only promotion transaction ratifies the versioned instance constitution and validates it at later launches.

## Operational model

Worker sessions own S1 local work. Concrete concurrency paths are S2 constructors. S3 has a specific optional coordinator seam plus a closed operator mode, recorded C(P). After-close raw-artifact challenge is an audit constructor until independent staffing is bound. The optional reference advisory workflow retains external/future adaptation choice with the operator, while committed crew-policy ratification is a separate parent S5 path.

## S1 — Operations

- State: A
- Function: Execute durable project tasks through independently model-driven worker sessions and return completed/blocked outcomes.
- Disturbance / variety regulated: Unfamiliar code, failed commands/tests, task ambiguity and partial work.
- Decisive decision or feedback right: Worker chooses implementation/investigation actions and task-local repairs, then reports/commits the outcome or a precise blocker.
- Decision owner: Model-backed worker in the first-party task/PID execution mode.
- Supporting / enforcement mechanisms: Runtime CLI, herdr launch/prompt/wait, Beads claims/history, first-party work prompt, isolated worktree, cages and settle/landing checks.
- Closure path: Ready task → first-party route/claim/session launch and work prompt → model-directed task execution → commit/evidence and closed/blocked task → settle/landing or escalation.
- Boundary reachability: INSTALL wires a chosen PID/runtime and queue; dispatch launches those sessions and supplies their task/guardrail context. The shipped developer PID defines actual work/verification/closure rather than just naming a role. Bare init without staffing performs no work.
- Why this is / is not agent-owned: Worker action choice is model-owned; routing, claims, timeouts and commits transport/enforce it. External runtime internals do not donate unrelated S2–S5 decisions.
- Evidence: [INSTALL.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/INSTALL.md); [examples/agents/developer.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/developer.md); [internal/posse/dispatch.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/dispatch.go); [internal/posse/worktree.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/worktree.go); [NOTES.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/NOTES.md)
- Basis: explicit and structural supported configured mode
- Confidence: high
- Caveats: No private deployment or live external CLI session was inspected; this does not claim a fresh empty home already runs a crew.

## S2 — Coordination

- State: C
- Function: Attenuate concrete collisions among independent sessions sharing tasks, launch state and work products.
- Disturbance / variety regulated: Two launch passes can both observe free seats and destroy/confuse session meta; concurrent task-store read-modify-write can lose updates; shared indexes/trees can mix worker changes.
- Decisive decision or feedback right: Serialize conflicting launch/store transitions, honor existing claims and isolate worker trees so subsequent operations see valid holders/results.
- Decision owner: First-party developer-defined runtime protocol; autonomous coordination discretion remains to be composed.
- Supporting / enforcement mechanisms: Launch flock, canonical per-store write locks, atomic claim handling, distinct session worktrees/indexes and guarded landing.
- Closure path: Contending launch/write checks run inside critical sections or lose a claim safely; later dispatch sees the committed holder/state; worker edits remain in separate trees until checked landing.
- Boundary reachability: Dispatcher/Beads wrapper/worktree launcher ship with the product and target named interference modes. These are concrete S2-specific paths, not generic graph or messaging expressiveness.
- Why this is / is not agent-owned: Locks and worktrees do not choose/revise an agentic coordination response; C records the functional construction path without claiming autonomous ownership.
- Distinct S1 units: Separately executing task workers and concurrent launch passes serving those workers.
- Inter-S1 disturbance: Duplicate seat/task acquisition, lost task-store updates and mixed edits/index operations.
- Attenuating coordination relation: Check-and-launch under one lock, serialize writes by canonical store identity, honor claims and isolate worktrees.
- Feedback into subsequent S1 behaviour: Losing/blocked launches do not fire; later sessions/dispatch read valid ownership and persistent updates, and isolated work is landed explicitly.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The code identifies actual TOCTOU/lost-update/cross-worktree failure classes and implements the corresponding mutual exclusion/isolation rather than merely storing tasks.
- Evidence: [internal/posse/launchlock.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/launchlock.go); [internal/posse/bdwritelock.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/bdwritelock.go); [internal/posse/dispatch.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/dispatch.go); [internal/posse/worktree.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/worktree.go); [NOTES.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/NOTES.md)
- Basis: explicit and structural constructor path
- Confidence: high
- Caveats: Store-lock coverage and OS enforcement are limited to the documented wrappers/launch surfaces, not every possible third-party writer.

## S3 — Inside-and-now control

- State: C(P)
- Function: Regulate current commitments, spend and exceptions across the instance fleet.
- Disturbance / variety regulated: Exhausted budgets/meters, blocked/stranded tasks, dead dispatch, unanswered decisions and continued spending while the operator intends a durable stop.
- Decisive decision or feedback right: Choose whole-instance pause/resume, resource limits and intervention on current work; optionally compose a coordinator receiving shop conditions and holding bounded pause authority.
- Decision owner: Parent mode: legitimate instance operator. Constructor mode: deployment author must bind/configure the coordinator actor and decision policy; no stock autonomous coordinator ships.
- Supporting / enforcement mechanisms: Live ShopCheck/status/cockpit, budget/plan meters, queue facts, pulse delivery, pause state and dispatch fire gates.
- Closure path: Parent sees fleet/queue/spend conditions → chooses constraints or pause/resume → persisted intent/config → subsequent dispatch changes admission while oversight continues. Optional pulse delivers conditions to a configured live coordinator; PauseActor permits that coordinator to return a pause choice, but staffing/policy are not supplied by an empty seed.
- Boundary reachability: Operator status and pause/budget paths are shipped supported commands. Optional coordinator/pulse configuration intentionally exposes a function-specific observation/authority/return seam; it does not instantiate a controller by itself.
- Why this is / is not agent-owned: Hard gates enforce owner-selected limits. The parent loop is operationally closed; an autonomous coordinator would require additional actor/policy composition, hence C(P), not A(P).
- Whole-system current view: ShopCheck over current queues/sessions, governance conditions, resource meters and dispatch health, rendered in status/cockpit and pulse.
- Current-control decision scope: Fleet dispatch pause/resume, resource/spend envelope and intervention on current blocked commitments; task decomposition alone is not the witness.
- Evidence: [internal/posse/govern.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/govern.go); [internal/posse/pulse.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/pulse.go); [internal/posse/pause.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/pause.go); [internal/posse/budget.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/budget.go); [internal/posse/dispatch.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/dispatch.go); [examples/config.yaml](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/config.yaml); [NOTES.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/NOTES.md)
- Basis: explicit and structural multi-mode evidence
- Confidence: medium-high
- Caveats: The public seed carries no coordinator name/actor; privately measured crew behavior is not used as evidence. The pulse itself delivers facts and grants no decision authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Deployer must compose coordinator model/policy and bind its live crew session | ShopCheck conditions delivered by configured pulse | Function-specific PauseActor authority can return coordinator intent into the dispatch gate; actor/policy remain uninstantiated in seed | `pulse.go`, `pause.go`, `examples/config.yaml` |
| Parent (`P`) | Legitimate instance operator | Fleet/queue/spend condition visible in status/cockpit | Operator pause/resume or resource choice is read by later dispatch, with oversight retained during pause | `govern.go`, `budget.go`, `pause.go`, `dispatch.go` |

## S3* — Complementary audit

- State: C
- Function: Expose complementary challenge to a worker closed-task claim using the closing commits and acceptance evidence.
- Disturbance / variety regulated: A task marked closed can fail its stated acceptance despite a successful worker report.
- Decisive decision or feedback right: Judge the actual product/diff against the closed-task claim and create evidence-backed corrective findings.
- Decision owner: The public product supplies an audit-specific constructor: verify-after plus QA/reviewer reference protocols. Actual independent actor staffing/assignment must be selected for the instance.
- Supporting / enforcement mechanisms: After-close verify work, commit/closer linkage, separate PID restrictions, task-store corrective findings and routing.
- Closure path: Closed code/devops task → verify-after files linked QA work naming claim/commits/acceptance → independently staffed verifier tests/falsifies raw artifacts → findings become corrective work or operator escalation → future workers address them. The first-party default does not staff that actor.
- Boundary reachability: verifyafter.go is real dispatch behavior; shipped reference PIDs specify raw-evidence judgments and corrective return. INSTALL explains copying/staffing personas and verify_assignee configuration. Without those bindings a ready verify task can remain unassigned.
- Why this is / is not agent-owned: Filing an audit task is not audit judgment. C preserves the function-specific access and return contract without inventing an automatically active, sufficiently independent evaluator in a fresh home.
- Claim being audited: A closed code/devops task satisfies its own stated acceptance criteria.
- Ordinary reporting path: Worker close reason/comment, task status and session/settle records.
- Complementary access path: QA directly executes the product/hostile-edge cases; reviewer inspects actual closing commits/diffs, not just the close text.
- Independence boundary: Separate staffed verifier role and restrictions separate judgment from implementation; assignment/runtime must be configured, and tests/developer dogfood do not substitute for that binding.
- Who acts on findings: Code/devops/architecture lanes receive defect work; operator alone may reopen a closed task under the documented protocol.
- Evidence: [internal/posse/verifyafter.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/verifyafter.go); [examples/agents/qa.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/qa.md); [examples/agents/reviewer.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/reviewer.md); [examples/agents/developer.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/developer.md); [examples/config.yaml](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/config.yaml); [INSTALL.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/INSTALL.md)
- Basis: explicit and structural constructor path
- Confidence: medium-high
- Caveats: This is an after-close challenge seam, not a blanket claim that every routine QA/reviewer title is S3*. No private completed audit execution is inferred.

## S4 — Outside-and-then intelligence

- State: P
- Function: Develop outside-and-future capability options for the instance crew, with operator-owned adoption.
- Disturbance / variety regulated: Changing vendor/tool prices, licensing obligations, lock-in and future exit/renewal costs can invalidate current operating choices.
- Decisive decision or feedback right: Choose whether to adopt a vendor/tooling/resource adaptation after source-backed option comparison.
- Decision owner: Legitimate operator in the supported advisory business-manager/reference-crew mode. The analyst recommends and explicitly commits to nothing.
- Supporting / enforcement mechanisms: First-party advisory PID, task/question/dependency protocol, durable option rationale and technical follow-up routing into code/devops.
- Closure path: Operator/product raises an external vendor/cost/license question → reference business role gathers current evidence and compares future cost/lock-in/exit options → decision goes to operator as question → operator choice returns via question/technical follow-up → task-ready dispatch implements the chosen current capability change.
- Boundary reachability: The business-manager PID is included in the embedded reference set and can be staffed through INSTALL. Its handoffs explicitly place every choice with the operator and route the technical implication back to operational lanes; this is a supported optional mode, not an assumed active default crew.
- Why this is / is not agent-owned: The model can analyze/choose a recommendation, but the adoption verdict remains human-owned. Current queue grooming, local memories and ordinary architecture planning alone are not the S4 witness.
- External distinction: Actual vendor prices/usage, license terms and dependency/tooling alternatives.
- Future / prospective distinction: Total cost over time, renewal obligations, lock-in and exit paths rather than only the current task implementation.
- Adaptation option generated: Source-backed vendor/tooling/license recommendation with trade-offs and what changes under alternative choices.
- Path back into current capability / S3: Owner answers the decision question and the resulting code/devops follow-up becomes current executable task work under dispatch.
- Evidence: [examples/agents/business-manager.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/business-manager.md); [examples/agents/product.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/product.md); [docs/adr/0005-work-prompt-blueprints.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/docs/adr/0005-work-prompt-blueprints.md); [internal/posse/dispatch.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/dispatch.go); [INSTALL.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/INSTALL.md)
- Basis: explicit and structural parent-governed reference mode
- Confidence: medium
- Caveats: Requires actually staffing the documented reference mode; no private market analysis, accepted vendor decision or beneficial result was inspected. Generic future research remains outside this bounded witness.

## S5 — Policy and identity

- State: P
- Function: Ratify the instance crew identity, role authority and durable operating/risk policy before it governs launches.
- Disturbance / variety regulated: Draft or agent-edited role/guardrail changes must not silently become authoritative instance policy.
- Decisive decision or feedback right: Accept a committed constitution diff and put that identity/policy version into force, or reject it.
- Decision owner: Legitimate instance operator; persona sessions are explicitly denied promotion.
- Supporting / enforcement mechanisms: Versioned agents/config/recipes/runtimes/skills, operator-only promote, source commit and per-file hash manifest, launch verification and persona/config write fences.
- Closure path: Proposed committed role/guardrail/instance-policy diff → operator reviews displayed diff and ratifies with promote → copy/manifest records the accepted version → subsequent launch validates/loads it and rejects unratified drift in dispatched mode.
- Boundary reachability: INSTALL documents the separate constitution source and promote workflow; the same first-party launcher verifies the installed promoted set. It is an actual returned governing-policy path rather than a configuration file merely called constitution.
- Why this is / is not agent-owned: The operator owns ratification; hashes and launch refusal enforce that decision. Agent prose edits or recommendations do not authorize promotion, and individual tool permissions are not used as the S5 witness.
- Identity / ultimate-policy issue: Crew roles/intents and risk/authority boundaries in the instance constitution, including who can spend, publish, alter live systems or widen visibility.
- Ultimate authority in each claimed mode: Instance operator in the promoted-constitution mode; no autonomous ultimate-authority mode is established.
- Return-to-operation path: Accepted committed policy is copied to the live home, hash-recorded and consumed/checked by following launches.
- Evidence: [internal/posse/promote.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/promote.go); [internal/posse/init.go](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/internal/posse/init.go); [INSTALL.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/INSTALL.md); [README.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/README.md); [examples/agents/developer.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/examples/agents/developer.md); [NOTES.md](https://github.com/ranger360ai/posse/blob/bdd3954bb86adc2d0fac14175abe9443ba439794/NOTES.md)
- Basis: explicit and structural parent-governed policy ratification
- Confidence: high
- Caveats: Not every promote invocation is a policy-level issue; the credit is for the documented crew-identity/guardrail ratification path. Ordinary binary promotion and source maintenance are separate.

## Distributed OSS parent arrangement

The parent is the operator of one configured instance. Public product maintainers and private author-instance crew are outside that deployed recursion. Private notes/memory/metrics were neither fetched nor used.

## Self-hosted and non-human modes

The operator chooses runtimes/substrates and staffs documented modes. A fresh init deliberately contains no active crew/controller/verifier. External Beads/herdr/model CLIs transport state and execute workers, but do not donate their own governance or audit functions. Optional coordinator autonomy remains a constructor, while parent pause and policy ratification are concrete supported paths.

## Recursion

Worker sessions are local task cells with meaningful action discretion. This alone does not establish full viable metasystems inside each worker; technical runtime/cage/substrate nesting is not recursive viability.

## Variety and escalation

Claims, isolated worktrees, locks and bounded guards address concrete concurrency/resource disturbances. ASK creates an operator question and dependency so guessing cannot silently resume work; answering releases dependent work. REFUSE names the hard line. Pause stops new dispatch spend while oversight/settlement continues. These are function-specific paths, not an automatic algedonic label for every blocked status.

## Evidence gaps

No instance was installed, no private instance source consulted and no live herdr/Beads/model flow was executed. Actor staffing is material: constructor states do not claim an already running controller/auditor. The reference advisory S4 mode is structural and narrower than claims about a real accepted future capability change. Product fixture tests and historic measured comments do not prove current deployed operation.
