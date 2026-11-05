---
harness_id: tram
project_name: Tram
repository: https://github.com/taewooyo/tram
review_ref: cf676742728b4d85020b210c8f0e6aa922f51fd0
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Tram

## Review boundary

- System in focus: the installed Tram development plugin for one host coding-agent session, its per-project task/approval state, orchestrating main agent, possible separate implementer agents, mandatory independent full reviewers and the Python transition/verification runtime.
- Purpose and identity: convert a user's bounded coding intent into an approved, implemented and independently verified change, preserving provenance and resumability rather than quietly expanding scope.
- Relevant environment: changing code/project docs, human requirements, conflicts in worker write-sets and resources, test failures, ambiguous policy, host tool availability and new/modified Git HEADs.
- Standard-distribution boundary: Tram's packaged `init`, `start`, `prd`, `plan`, `impl`, `verify`, `status` and related first-party skills, role/context cards, Codex/Claude host adapters, Python local runtime, generated plugin installation layout and user/worker interaction. Underlying Codex/Claude inference and tool infrastructures are dependencies, not Tram-owned standalone enterprises.
- Credited operating / distribution surfaces: [README usage](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/README.md), [single orchestration contract](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [implementation dispatcher](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/impl/SKILL.md), [independent full verification](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/verify/SKILL.md), [runtime state implementation](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/runtime/tram.py), [host validation limitations](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/docs/support.md).
- Adjacent first-party surfaces excluded from ownership: maintainer's own development tasks and release CI, static documentation previews, package-build tests, sample target applications, provider-native agent policies that Tram does not override and user organizations not encoded in the per-project task loop.
- First-party operating / deployment modes considered: single main agent doing small safe tasks; separate implementer agents for larger work; strict serial/shared-resource versus parallel/independent worker dispatch; full fresh reviewer and light tests; explicit PRD/Plan approvals; resumable project/task state; read-only status and optional push/PR finish routes.
- Recursion level: one user-authorized software development task with a main coordinator and zero or more separate operational workers in a project; not a durable cross-project company.
- Reviewed revision: `cf676742728b4d85020b210c8f0e6aa922f51fd0`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Tram ships host-specific packages with a shared skill tree and Python control runtime. The main agent inspects current project/doc/code state, asks for human PRD and Plan approvals when required, and determines whether to work directly or dispatch a fresh isolated implementer. The controller validates permitted task transitions, recorded approval digests, execution ownership, independent test references and verification rounds. A full review must use a new agent role that inspects actual source/tests against the pinned approved criteria; main verifies the review result and either completes, fixes cited defects in another round or escalates a design change. The user's own coding host supplies models and tool execution. [Orchestration](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md); [runtime](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/runtime/tram.py); [flow](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/flow-rules.md).

## Operational model

The provider-backed main and implementer roles perform source investigation, choose code changes and run actual tools; independent full reviewers judge current code and tests instead of accepting an implementer's claim. The main model chooses worker dispatch/parallelism and the next stage within a bounded state machine, while the user retains explicit requirements/design approval, wider policy decisions and optional Git publication. A documented 0.0.1 alpha candidate exists with locally tested host package installation and a 242-test suite; a complete authenticated fresh-install→approval→implementation→review→resume lifecycle is **not** reported as passed at this pin. This supports a shipped source-level construction, not an invented live end-to-end agent result. [Supported/missing host coverage](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/docs/support.md); [release validation](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/docs/release-validation.md).

## S1 — Operations

- State: A
- Function: main or separately dispatched coding agents investigate a specific project, change implementation code/tests and return concrete source-level results; reviewer roles additionally perform verification work.
- Disturbance / variety regulated: unknown code and dependency behavior, changing requirements within approved scope, tool/test failures and reviewer-discovered defects.
- Decisive decision or feedback right: choose source modifications, affected tests, debugging actions and fixes using actual project context while the user-approved PRD/Plan bounds the task.
- Decision owner: model using the Tram role contract on an installed Codex/Claude host; the Python runtime validates allowed phase transitions but does not author code.
- Supporting / enforcement mechanisms: first-party role instructions, project context cards, scoped worker dispatch, bounded implement/review transition, task evidence records and `verify-run` assertions.
- Closure path: user-approved task and plan → model investigates files and implements/tests → independent verification returns cited defects → implementing model revises work → passing head-specific evidence permits completion.
- Boundary reachability: package exposes the documented `/tram:start` and implementation roles; its skill contracts explicitly dispatch tool-using workers through host-native adapters and connect their results to installed runtime transitions.
- Why this is / is not agent-owned: source-change choice and correction require meaningful task-specific model discretion. The host and model supply inference, but Tram's first-party skill construction makes the role operationally reachable; Python gates remain constructor enforcement.
- Evidence: [main dispatcher and per-round work](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/impl/SKILL.md), [start continuation](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [release verification limits](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/docs/release-validation.md).
- Basis: documented packaged skill/host role wiring plus shipped transition implementation, without provider-backed full workflow acceptance.
- Confidence: medium-high for supported construction, medium for untested integrated host lifecycle.
- Caveats: no independently observed authenticated full run was performed; installed host/provider tools are required and a mere package-install success does not prove agent edits work end to end.

## S2 — Coordination

- State: A
- Function: main model decides which concurrently eligible operational sub-tasks are genuinely independent and serializes those competing for files, ports, databases or outputs.
- Disturbance / variety regulated: separate implementer agents overwriting a shared file, racing on a DB/port/output directory or acting on an unfinished prerequisite.
- Decisive decision or feedback right: identify each task's owned files/resources/dependencies, select parallel dispatch only for disjoint units, and order shared-write or dependent work sequentially; inspect active/aborted worker state before reassignment.
- Decision owner: the model-based main orchestration role applying a mandatory first-party coordination contract; worker agents cannot re-delegate or rewrite the common Task/approval state.
- Supporting / enforcement mechanisms: Task entries with owners/paths/dependencies, adapter-provided independent agent invocation, one main Task writer, active-worker liveness check and shared-resource serial-first policy.
- Closure path: proposed worker assignments → main compares file/port/DB/output ownership and prior completion → independent tasks may run concurrently, but shared resources wait → main reads workers' actual edits/results → updates Task and only then authorizes dependent work.
- Boundary reachability: the single-orchestration contract expressly governs *all* skill paths, including `impl`, `quick`, `coverage` and `perf`; implementation dispatcher links native agent delegation back to main Task reconciliation.
- Why this is / is not agent-owned: the coordination rule sets constraints, but the model must classify live task/resource overlap and exercise discretion over serial versus parallel work; these are cross-agent interference decisions, not a generic speaker selector or mere worker naming.
- Distinct S1 units: multiple separately spawned implementer agents with independently owned sub-tasks in one approved project plan.
- Inter-S1 disturbance: conflicting writes to a shared file or mutable runtime resource can invalidate another worker's results.
- Attenuating coordination relation: main-assigned ownership and dependency records; only independent resource sets are dispatched concurrently, while shared operations are serialized.
- Feedback into subsequent S1 behaviour: a dependent/shared-path worker is withheld until prerequisite work has returned and current state is reread, then receives revised files/instructions rather than writing concurrently.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the decisive discriminator is the *specific material collision of two operational workers*, and the chosen serial/parallel pattern directly prevents that collision.
- Evidence: [resource-conflict dispatch](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [implementation dispatch choices](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/impl/SKILL.md), [ownership and progress state](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/runtime/tram.py).
- Basis: explicit model-directed first-party contract and persistent task ownership, not observed measured parallel conflict traces.
- Confidence: medium; the prevention is prompt/protocol-directed rather than an atomic cross-process file reservation.
- Caveats: a worker can violate its assigned ownership and no universal OS-level lock is claimed across all worker-edited files; runtime write lock protects metadata, not all project source.

## S3 — Inside-and-now control

- State: A(P)
- Function: model-based main maintains a whole-task view across worker assignments, completion evidence, verification rounds, resource/budget/approval limits and active blockers while a human controls the current task envelope.
- Disturbance / variety regulated: mismatched PRD and implementation scope, missing worker results, stale check evidence, repeated failed reviews, excessive rounds and unreliable execution state.
- Decisive decision or feedback right: main assigns/changes worker tasks, chooses direct versus delegated execution, selects review strength, integrates outcomes and branches to fix, complete or design escalation; human separately ratifies PRD/Plan and may halt/change permitted work.
- Decision owner: operating main model for current work allocation and stage strategy (`A`), constrained by the user as parent authority for approvals/current commitments (`P`). Python refuses invalid transitions and unverifiable references.
- Supporting / enforcement mechanisms: project Task board, status/next-action state, scoped worker references, digest-bound approvals, round budget, 90-point full-review min-gate and `transition` authority.
- Closure path: current tasks and worker results → main chooses new assignment/verification route or escalates → runtime validates evidence and updates state → next worker/reviewer receives changed instructions or waits for human approval.
- Boundary reachability: `start` routes to `impl`/`verify` and main owns `transition`, `approve` and `review` in the documented packaged host workflow; tests implement the refusal boundaries.
- Why this is / is not agent-owned: model has real discretion in prioritizing and integrating this task's workers, although it cannot change approved scope or bypass explicit owner gates.
- Whole-system current view: main reads complete per-task stage, Task worker owners/dependencies, verification status and blockers, rather than only one code-edit output.
- Current-control decision scope: division and ordering of sub-tasks, live delegated work, verification effort, retry/stop/escalation and current human authorization envelope.
- Evidence: [main/worker authority split](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [implement/review branching](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/impl/SKILL.md), [state/approval implementation](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/runtime/tram.py).
- Basis: first-party main-role/worker stage contract plus built runtime validation.
- Confidence: medium-high for control boundaries, with integrated host execution unverified.
- Caveats: the recursion is a bounded development task, not evidence of a standing multi-project autonomous executive or direct PR merge authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main model | Task/worker/verification state calls for next work choice | Main chooses assignments, review strength, fix or escalation; recorded transition changes subsequent agent work | [orchestration contract](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md) |
| Parent (`P`) | Human user | PRD/Plan requires approval or current scope/policy has materially changed | User approves, revises or stops the task; digest-bound runtime gate enforces change before work resumes | [flow rules](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/flow-rules.md) |

## S3* — Complementary audit

- State: A
- Function: a new isolated reviewer agent independently checks the current implementation's real tests/code and user-approved acceptance criteria against the implementer's report.
- Disturbance / variety regulated: untested or mis-scoped changes, stale evidence after HEAD edits, fabricated test success, missing project policy and review contamination from earlier rounds.
- Decisive decision or feedback right: fresh reviewer performs its own `verify-run`, checks diff and tests against PRD/Plan, assigns five-axis substantiated verdict and either passes or cites blocking defects; main must validate recorded independent execution and reject contradictory results.
- Decision owner: an independently spawned model reviewer with a separate run/reference and strict no-implementation role; main registers but does not replace its independent inspection.
- Supporting / enforcement mechanisms: `verify` full mandatory fresh reviewer, 5-axis rubric, `verify-run` command receipts, start snapshot/round check, review registration and refusal of missing/invalid evidence.
- Closure path: implementation change → new reviewer independently reads current code/tests and runs checks → evidence/score/verdict returned → main validates & stores reviewed round → failed defects go to implementer fix; passed verified round allows completion.
- Boundary reachability: `start`/`impl` require full review for new/high-risk work, and `verify` explicitly routes to the host's native isolated agent creation and runtime `review` registration; if independent review is unavailable the project must withhold completion.
- Why this is / is not agent-owned: an independent role makes qualitative adversarial judgment about the observed diff and actual tests; mandatory runtime scoring checks only enforce evidence validity.
- Claim being audited: implementation meets the approved PRD/Plan and passes required tests at the current state.
- Ordinary reporting path: implementer explanation, local test claims, Task progress and completion summary.
- Complementary access path: fresh separate reviewer's own tools reading the source diff/test outputs plus original user-intent provenance and approved criteria, independent of implementer's prior conversation.
- Independence boundary: new run, separate reviewer role/context and no implementation edits; shares the configured provider/model infrastructure and is not an external institution.
- Who acts on findings: main controller rejects completion and routes concrete cited defects to another implementation round; changed code requires a new reviewer.
- Evidence: [full independent verifier](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/verify/SKILL.md), [rubric and evidence](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/review-rubric.md), [main round branch](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/skills/impl/SKILL.md).
- Basis: mandatory packaged role workflow and hard evidence checks, not a claimed completed public host review run.
- Confidence: medium-high for separation contract, medium for unobserved fidelity in a full authenticated session.
- Caveats: the release notes do not establish a full real Codex/Claude review cycle on the candidate package, and the same model provider may supply implementer and reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate operational loop that models changing external/future project conditions, develops adaptation options and returns a selected enduring capability to the current task organization was established.
- Disturbance / variety regulated: evolving third-party requirements, dependencies, model/tool capabilities and future market needs could motivate a different project strategy.
- Decisive decision or feedback right: project research/`domain` skills can gather context; the human approves policy and scope, but no prospective outside-environment option-and-return authority was observed within the installed organization.
- Decision owner: not established at S4. Main researches the *current* approved task; user/maintainers may later choose new project scope outside that loop.
- Supporting / enforcement mechanisms: code research, project knowledge, existing-doc evidence, domain interviews, retrospectives, and performance experiments.
- Closure path: observed project facts influence current PRD/Plan and code work; no separate future-external scenario selection is shown governing an enduring adapted operational capability.
- Why this is / is not agent-owned: planning present implementation, repeating tests or gathering knowledge is not by itself the outside-and-then S4 relation.
- Evidence: [project knowledge bounds](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/project-experience.md), [start/approved work scope](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [workflow limits](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/flow-rules.md).
- Basis: bounded negative examination of shipped task, knowledge and improvement workflows.
- Confidence: medium-high at the per-project task recursion.
- Caveats: a user's own future product planning might provide S4 in a larger organization, but is outside this installed task-level scope.

### Absence scope

- Surfaces inspected: `start`, `domain`, project-experience guidance, PRD/Plan research, `perf-loop`, `retro`, runtime Task/approval transitions and host support notes.
- Plausible first-party paths checked: domain exploration, external reference discovery, knowledge writeback, performance experiments and scope-change escalation to the user.
- Why no material first-party path remains: none establishes a durable distinct outside-and-future selection channel that changes ongoing organizational capability, beyond today’s human-scoped project request or local optimization.

## S5 — Policy and identity

- State: —
- Function: no installed organizational identity-level agenda, legitimate decision on ultimate policy and binding charter-return loop was established within this bounded task workflow.
- Disturbance / variety regulated: a fundamental change to the project's purpose, ethics or ultimate product authority could exceed a scoped coding assignment.
- Decisive decision or feedback right: human must approve PRD/Plan and policy/requirements changes, but the shipped approvals are for a task's scope/design, not shown as a continuing VSM S5 identity function.
- Decision owner: human project owner retains ultimate responsibility outside Tram's implemented local task orchestration.
- Supporting / enforcement mechanisms: explicit requirement/design approvals, immutable snapshots, `scope` conflict escalation, project config and user-controlled publication.
- Closure path: new requirements or product/security policy choices are escalated to human PRD/Plan review and return to *this task*; no evidence such a decision returns as binding revised organization identity across recurring tasks.
- Boundary reachability: documented owner approvals and repeated validity checks are real; an identity/policy-level recursion beyond them is not.
- Why this is / is not agent-owned: important parent approval does not alone establish S5(P) where the closed issue is task scope, not ultimate mission/ethos or constitutional authority.
- Evidence: [approval/change handling](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/start-experience.md), [human decision boundaries](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/project-experience.md), [workflow gate rules](https://github.com/taewooyo/tram/blob/cf676742728b4d85020b210c8f0e6aa922f51fd0/src/context/flow-rules.md).
- Basis: first-party installed flow source review, distinguishing task approvals from ultimate organizational policy.
- Confidence: medium-high within this scope.
- Caveats: an enclosing human-owned company/project may have an external S5; no positive credit is borrowed from it without a first-party return path.

### Absence scope

- Surfaces inspected: PRD/Plan human gates, conflict-to-PRD escalation, project config, ownership/host security rules, end-of-task commit/push/PR choices and main agent authority contract.
- Plausible first-party paths checked: explicit product behavior/security policy changes, human approval snapshots, user request provenance and recurrent project knowledge updates.
- Why no material first-party path remains: the decisions govern an individual task or local project settings; no demonstrated identity-level disagreement is adjudicated through a standing legitimate charter-setting process that binds subsequent independent work.

## Distributed OSS parent arrangement

Tram's GitHub maintainers, package release and development/testing workflow are separate from an installed user-run task organization. The user is a first-party current-control participant through task approval and scope steering, but that alone does not close S5. Model providers and native host APIs remain external components.

## Self-hosted and non-human modes

Tram can be installed into Codex/Claude, with the Python runtime and project documents local; available host tools decide whether independent worker/reviewer spawning is possible. Human approval is mandatory before large/high-risk implementation and cannot be bypassed by automatic resumption. The direct model-led small task still has S1, while multi-worker S2/S3 and fresh S3* are supported role modes, not guaranteed in every installation.

## Recursion

The main model with delegated implementers constitutes a coordination/metasystem relative to these bounded S1 work cells. A reviewer is separate from implementing workers and has a narrow audit mandate. No complete autonomous S3–S5 inside every worker or higher standing company-level metasystem is inferred.

## Variety and escalation

Scoped role prompts and tool-using models amplify source-repair variety. Separate file ownership, serial collision handling, approval digests, independent review, test references and a maximum five-round verification budget attenuate quality and resource risk. Repeated defects or unresolved changed requirements stop the cycle and return a concrete decision request to the human, instead of silently widening the mandate.

## Evidence gaps

- The candidate is alpha, with package installation and local suite results but not an accepted full authenticated Codex/Claude task lifecycle across approval, implementation, independent review and resumed session.
- Agent-side S2 conflict judgment and S3 dispatch are first-party prompt contracts with runtime state support; there is no measured live worker-overlap prevention or atomic lock on *every* source file.
- Mandatory S3* independent full review has a real separation and evidence-rejection contract but no independently reproduced paid-provider full run for this exact version in this review.
- No current installed S4 or identity-level S5 closure was found; project policy and PRD/Plan changes remain human decisions on the task boundary.
