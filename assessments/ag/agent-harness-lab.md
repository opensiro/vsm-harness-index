---
harness_id: agent-harness-lab
project_name: Agent Harness Lab
repository: https://github.com/mihazs/agent-harness-lab
review_ref: 1b165594818bab9f92605fb4bd5ec0c6f943c2fc
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness Lab

## Review boundary

- System in focus: an explicitly invoked project-scoped Agent Harness Lab `ahl improve` run with one selected Codex/Claude or controlled Responses runtime, project harness snapshots, proposer, independently contextualized evaluator author, frozen task bank, paired trials and terminal recommendation. The offline `ahl analyze` mode and installed `harness-self-improvement` skill are adjacent first-party entry surfaces.
- Purpose and identity: diagnose failures in coding-agent instructions/skills, create reversible candidate harness changes and compare their observable behavior against the baseline without treating synthetic improvement or a self-reported success as certification.
- Relevant environment: changing developer instructions and attached project skills, execution transcripts, repeated failures, injected source content, modified task banks, evaluation leakage, runtime resource limits, stale observation history and regressions.
- Standard-distribution boundary: first-party Python CLI, `workflow.py` controller, evidence collectors, proposer/evaluator role construction and bounded runner, task/grader custody, optional controlled Responses and Linux grader sandbox, monitoring/checkpoint logic and installed skills. Actual Codex/Claude provider and model inference are external dependencies.
- Credited operating / distribution surfaces: [README and explicit adoption limits](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/README.md), [workflow and role dispatch](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py), [agent-backed workflows](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md), [evaluation construction roles](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/evaluation/construction.py), [behavioral promotion policy](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/promotion/policy.py), [installed improvement skill](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/skills/harness-self-improvement/SKILL.md).
- Adjacent first-party surfaces excluded from ownership: scientific research roadmap, unpublished/invalid certification, autonomous behavioral promotion not yet integrated, future issue #77 adoption work, developer GitHub CI, examples and synthetic corpus outcomes as claims of general accuracy.
- Operating modes considered: `analyze` (deterministic evidence diagnosis), `improve` (agent-backed candidate and evaluator construction with baseline/candidate trials), `watch` (foreground repeated runs only on changed evidence), controlled Responses with explicit resource/custody prerequisites, `--repair-contracts` (narrow structural BOM repair), and installed skill invocation.
- Recursion level: one project harness improvement/evaluation run and its role-controlled subprocesses, not the external coding agent organization or the user's whole software governance.
- Reviewed revision: `1b165594818bab9f92605fb4bd5ec0c6f943c2fc`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`ahl analyze` gathers local evidence and runs deterministic process/duplicate-observation analysis; it does not call a model. `ahl improve` captures the original harness into a baseline snapshot, selects an authenticated runtime, asks a proposer agent to stage a candidate in a separate directory, freezes the patch, then starts a **fresh evaluator-author session** with baseline/source evidence but not the candidate. The author defines tasks and artifact graders; the controller validates grader broken/partial/complete controls, freezes task/grade inputs and runs paired baseline/candidate trials within a shared budget. Failed candidates may receive one bounded refinement with held-out separation; the final behavioral result is a recommendation, not a write to the active project's instruction files. Source files, private logs and original project state are checked for concurrent drift. The optional continuous watch mode re-runs only when source evidence changes, with locks/checkpoints and fail-closed repeat policy. [Workflow](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py); [user workflow](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md).

## Operational model

In model-backed mode distinct proposer and evaluator-author agents exercise discretion over proposed edits and test design within controller-defined views. First-party roles and runner arrange the real calls, artifacts, tests, deadlines and result conditions. Model identity, cooperative native session isolation and scientific certification are not universally verified. The CLI's default final boundary is **recommendation-only for behavioral changes**; a narrow explicit structural contract repair can be applied via a separate journaled path. The installed skill's assisted fallback describes a wider edit loop, but a skill document is not evidence that the guarded CLI has integrated general automatic behavioral adoption. [Promotion gate](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/promotion/policy.py); [one-call structural repair](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/one_call.py).

## S1 — Operations

- State: A
- Function: investigate bounded harness defects and generate an executable candidate instruction/skill change against project evidence.
- Disturbance / variety regulated: unknown agent failure mechanisms, contradictory observations, ineffective instructions, regressions and source-context gaps.
- Decisive decision or feedback right: the proposer model chooses which supported mechanism to address and what candidate file edits to stage; baseline/candidate model task executors choose actions under identical frozen tasks and runtime settings.
- Decision owner: selected Codex/Claude/Responses model-backed proposer and task roles in explicitly invoked `improve` mode; first-party controller scopes and executes them.
- Supporting / enforcement mechanisms: project-local snapshots and path allowlists, model role prompts, source/analysis receipts, artifact hashes, shared trial/time ceiling, frozen candidate, paired executors and evaluation feedback.
- Closure path: collect bounded evidence → proposer model selects candidate → change is frozen → baseline and candidate agent trials execute → observed failures/regressions feed the bounded refinement or final no-change/recommendation.
- Boundary reachability: `workflow.py` invokes native/Responses role runner in preparation and task phases; `ahl improve` is the documented CLI entry, provided runtime availability and permissions.
- Why this is / is not agent-owned: proposer decides semantic repair hypotheses and actual candidate contents, not just a deterministic suggested text; `analyze`, static classifiers and test bookkeeping alone would be constructors, not S1 A.
- Evidence: [proposer dispatch and trial flow](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py), [controlled role preparation](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/evaluation/construction.py), [documented modes](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md).
- Basis: pinned first-party execution code and runtime contract; not a live paid Codex/Claude experiment here.
- Confidence: high that model-backed roles are shipped, medium for real-world repair quality.
- Caveats: no model calls in `analyze` or offline diagnostics; no general automatic promotion implied by successful paired tasks.

## S2 — Coordination

- State: —
- Function: no separately established inter-S1 reciprocal conflict-attenuation loop beyond task role isolation and experiment scheduling at the defined single-run boundary.
- Disturbance / variety regulated: a proposer could contaminate evaluator inputs or a concurrent improvement run could alter the same project, but AHL prevents those situations by frozen views/locks rather than demonstrated feedback among independently operating S1 units.
- Decisive decision or feedback right: controller grants separate role paths, budgets, frozen snapshots and project locks; a stale or leaked input blocks the whole evaluation.
- Decision owner: deterministic custody/permission controller, without cross-worker conflict-specific negotiation or corrective return to both S1 cells.
- Supporting / enforcement mechanisms: role-scoped views, frozen task banks and hashes, project lock, candidate/baseline isolation, source-drift checks, sequential trial orchestration.
- Closure path: potential cross-role contamination is prevented or detected; invalid runs stop or require intervention. This is evaluation integrity, not evidenced coordination of independent operational commitments.
- Boundary reachability: role views, frozen candidate and validation are shipped; a separate correction negotiation between proposer and evaluator is not.
- Why this is / is not agent-owned: distinct fresh roles, sequential stages and file isolation are important safeguards, but not enough to infer VSM S2 without a concrete disturbance-feedback relation returning to affected S1 units.
- Evidence: [role construction and separation](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py), [controlled execution boundaries](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/runtime-boundary.md), [preflight/custody policy](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/one_call.py).
- Basis: bounded negative review of multi-role experiment/custody paths.
- Confidence: medium-high for this recursion.
- Caveats: a future multi-project adaptation fleet could implement true S2; that is outside this single-project run.

### Absence scope

- Surfaces inspected: native/Responses role startup, proposer/evaluator view split, project lock, frozen evaluation bank, task trial scheduling and contamination checks.
- Plausible first-party paths checked: parallel task evaluations, multiple candidate variants, proposer/evaluator cross-talk, concurrent project runs and contradictory failures.
- Why no material first-party path remains: discovered mechanisms isolate roles or stop invalid attempts; no concrete independent S1 collision-resolution conversation with feedback into both operational units is shipped at this level.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the active run's preparation/evaluation roles, resource budget, candidate eligibility, current evidence and terminal disposition, with user-owned runtime/scope initiation.
- Disturbance / variety regulated: budget exhaustion, changed source files, invalid evaluator controls, failing task bank, unavailable authentication, partial runs and repeated monitoring without new evidence.
- Decisive decision or feedback right: controller freezes/validates candidate and grader inputs, schedules tests/refinement, rejects a candidate or emits recommendations; human owner authorizes project, chosen runtime, scope and any later behavioral adoption.
- Decision owner: deterministic `workflow.py` and promotion prerequisites (`C`), with human operator (`P`) initiating and deciding outside-CLI adoption. Controller does not quietly grant itself publication rights.
- Supporting / enforcement mechanisms: project locks, shared 45-minute/24-role defaults, checksums, state receipts, role budgets, graded trial coverage, early fail-closed exits, optional monitor checkpoints.
- Closure path: current evidence and role result → controller authorizes next preparation/test/stop or reports unsupported → stored checkpoint/receipt constrains the next agent dispatch.
- Boundary reachability: `ahl improve` and `ahl watch` use these live controller functions; `watch` is foreground and must be explicitly started.
- Why this is / is not agent-owned: current-run scheduling/disposition is rule-based despite model roles doing task work; real human controls authenticated invocation and reviewed candidate adoption.
- Whole-system current view: baseline/candidate hashes, source identity, proposer/evaluator states, task bank coverage, model calls, time/trial remaining, results and previous monitor checkpoints.
- Current-control decision scope: allow/deny a role run, protect frozen inputs, retry once, stop on invalid evidence, write final review/recommendation and watch restart suppression.
- Evidence: [controller loop](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py), [invocation preflight](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/one_call.py), [monitoring mode](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md).
- Basis: first-party deterministic role/state controller.
- Confidence: high in structural control rights; actual credentialed runs not repeated here.
- Caveats: human adoption beyond CLI and real trusted production integration are not claimed as observed automatic completion.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Improvement controller | Evidence hash, trial or grader outcome, remaining budget | validate and freeze → dispatch/refine/reject or stop → result/checkpoint controls next role | [workflow](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py) |
| Parent (`P`) | Project owner/operator | Explicit request, runtime permission or final candidate review | choose project/agent and boundaries; decide whether to manually incorporate an eligible recommendation → later project files/workflow may change outside current CLI run | [README](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/README.md) |

## S3* — Complementary audit

- State: A
- Function: a separately prompted evaluator-author agent constructs tests/graders from baseline/source evidence while deliberately blind to the candidate, and the controller executes those frozen evaluators to challenge the proposer's claimed improvement.
- Disturbance / variety regulated: proposer self-praise, overfit instruction rewrites, candidate-specific tests, evaluator leakage and differences that disappear on held-out/regression cases.
- Decisive decision or feedback right: evaluator-author model independently chooses test cases and grader construction within the baseline evidence and broken/partial/complete control contract; frozen graders then measure actual paired task outputs and can cause rejection or bounded refinement.
- Decision owner: separate fresh model-backed evaluator-author role owns substantive test design; deterministic comparison controller enforces controls and verdict/disposition.
- Supporting / enforcement mechanisms: separate role workspace/views, baseline-only source context, withheld candidate and held-out inputs, grader self-tests, manifest freezing, task result artifacts, same-runtime paired trials and custody checks.
- Closure path: proposer freezes candidate/claim → independently scoped author designs tests without seeing patch → controls/graders are frozen → baseline/candidate execute → actual result comparison rejects/permits refinement or emits review recommendation.
- Boundary reachability: `workflow.py` constructs a separate evaluator session in native mode or `construction.author`/controlled role access, and validates a manifest before paired trials. No optional uninstalled reviewer service is required beyond the chosen agent runtime.
- Why this is / is not agent-owned: deciding *what independent probes should measure* involves a different model context, not simply running a copy of the proposer's test; the final grader/veto itself is deterministic, so this is not automatically a certified independent human scientific audit.
- Claim being audited: a proposed harness instruction/skill edit improves required task outcomes without regression under comparable inputs.
- Ordinary reporting path: proposer mechanisms, candidate diff, self-declared `proposal.json` and any development trial feedback.
- Complementary access path: evaluator author receives baseline/source/analysis **without** candidate patch, builds unrelated executable tasks and graders, and the controller examines fresh baseline/candidate task artifacts.
- Independence boundary: roles are separately scoped and patch-blind by construction, but cooperative Codex/Claude runtime/hook behavior and model provider isolation are not proven adversarial security; some source metadata is shared.
- Who acts on findings: controller rejects/refines/recommends; human decides any behavioral adoption. No claim of certified unconditional promotion.
- Evidence: [independent evaluation-construction prompt and calls](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/workflow.py), [role-specific controlled author](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/evaluation/construction.py), [frozen task method](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md).
- Basis: explicit shipped two-role model construction plus executable artifact feedback, not observed scientific effect size.
- Confidence: medium-high for independent **input view** and actual verdict path, medium for model quality and native role isolation.
- Caveats: “fresh session” alone is not a proof of full root independence or test correctness; graders need explicit self-tests and absence of leakage.

## S4 — Outside-and-then intelligence

- State: —
- Function: no **completed behavioral adoption return** turning evaluated future-harness candidates into active project operating capability under the shipped CLI's general workflow.
- Disturbance / variety regulated: evolving task types and systematic future agent behavior might warrant new harness instructions and skills.
- Decisive decision or feedback right: proposer can forecast candidate effects and evaluation compares development/regression/held-out tasks, but `improve` deliberately returns a review recommendation instead of applying behavioral changes; the human may later edit active files separately.
- Decision owner: user/project outside the CLI owns actual behavioral promotion; no first-party general S4 decision-to-adoption loop has authority.
- Supporting / enforcement mechanisms: retrospective analysis, selected candidate proposals, prospective task banks, held-out controls, promotion prerequisites and fail-closed recommendation status.
- Closure path: candidate → prospective paired task evidence → review recommendation; missing final behavioral activation in the same supported controller means the full outside-and-then capability return is unclosed.
- Why this is / is not agent-owned: creating and evaluating future options is substantial S4-adjacent intelligence but cannot be scored as completed S4 when the proposed capability is explicitly not adopted. Narrow structural BOM repair is not general behavioral S4.
- Evidence: [README no auto-adoption](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/README.md), [promotion policy recommendation-only](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/promotion/policy.py), [one-call narrow repair](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/one_call.py).
- Basis: explicit runtime/README negative authority and supported-mode examination.
- Confidence: high for CLI's deliberate blocked behavioral return; a manual fallback may differ under explicit user authority.
- Caveats: installed `harness-self-improvement` skill describes assisted evaluation/editing; without a validated matching runtime/receipt this is not imported as general autonomous promotion into the guarded `ahl improve` path.

### Absence scope

- Surfaces inspected: CLI improvement/watch, proposer and evaluator trials, promotion policy/adoption flag, `--repair-contracts`, skill invocation/fallback and documented #77 future integration.
- Plausible first-party paths checked: recommendation-only behavioral changes, CLI automatic application, repeated optimization, certified future transfer, journaled structural correction and skill-assisted edits.
- Why no material first-party path remains: automatic behavioral promotion and verified installed activation are explicitly unavailable in the supported controller; the only enacted edit is a narrow non-behavioral contract repair or separate human-assisted skill operation without matching controller certification.

## S5 — Policy and identity

- State: —
- Function: no legitimate whole-project identity/ultimate-purpose adjudication loop evidenced in one harness optimization run.
- Disturbance / variety regulated: privacy of traces, scope of external models, credentialed cost, whether an evaluator can be trusted and changes to global instructions are real governance concerns.
- Decisive decision or feedback right: invocation permissions and configured scope restrict project files and runtime capabilities, while the user decides model/provider, accepts adoption and can stop the command; none is charter-level identity resolution returned as binding system purpose.
- Decision owner: outside user/project authority; controller enforces safety/eligibility preconditions rather than deliberating ultimate purpose.
- Supporting / enforcement mechanisms: project path allowlists, no global skills by default, no publication rights, credential-bound external calls, privacy-safe artifacts and explicit fail-closed prerequisites.
- Closure path: invalid permission/role scope blocks the run or preserves unmodified files; no first-party identity dispute reaches a higher legitimate policy owner and returns as an ultimate revised charter.
- Why this is / is not agent-owned: safety and provenance constraints limit experiments but are not themselves S5 governance.
- Evidence: [scope and limits](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/docs/workflows.md), [preflight boundaries](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/one_call.py), [promotion authority](https://github.com/mihazs/agent-harness-lab/blob/1b165594818bab9f92605fb4bd5ec0c6f943c2fc/agent_harness_lab/promotion/policy.py).
- Basis: bounded negative review.
- Confidence: medium-high.
- Caveats: the human project owner has external policy rights; those are not automatically first-party runtime S5(P).

### Absence scope

- Surfaces inspected: invocation authorization, scoped paths, model credentials, role budgets, private artifacts, code publication ban, adoption policy and skill invocation boundary.
- Plausible first-party paths checked: global skill request, user-directed correction, denied permissions, personal data handling, certification authority and automatic promotion.
- Why no material first-party path remains: each path regulates experiment authority or current file scope; no general identity/purpose issue-to-legitimate-policy-to-operational-return cycle is implemented.

## Distributed OSS parent arrangement

The maintainer of the open-source utility and the assessed user's coding project are separate legitimate authorities. An AHL trial does not acquire their identity policy by running against their files; the product explicitly confines itself to project-owned harness material and local recommendations.

## Self-hosted and non-human modes

The offline diagnosis can run without model credentials. Model-backed improvement requires authenticated Codex/Claude or an explicitly configured controlled Responses endpoint. The program does not auto-launch on installation, and foreground `watch` requires user invocation. Behavioral edits are not silently activated; the controlled workflow is an evidence-producing evaluation service, not a self-certifying deployment authority.

## Recursion

The proposer, evaluator author and paired task executors have differentiated roles and model contexts, but the role-separated trial is an experimental unit governed by one deterministic controller. It is not a newly independent viable contributor organization or a multi-project regulatory hierarchy.

## Variety and escalation

History/context mining, model-proposed candidate edits and independent grader construction amplify possible fixes. Frozen baseline/candidate views, patched-blind evaluator input, controlled grader self-tests, shared budgets, regression/held-out comparisons and non-adoption policy attenuate overfitting and unauthorized changes. Invalid evidence, exhausted budgets and unavailable authentication fail closed with distinct reported dispositions.

## Evidence gaps

- Exact pinned source and execution paths were inspected; no authenticated Codex/Claude/Responses E2E evaluation was run, and comparative benchmark quality is not inferred from synthetic test fixtures.
- Fresh evaluator-author sessions are structurally separate from candidate generation, but provider/hook, scientific root and grader independence are not universally qualified; S3* A is bounded to substantive independent test design and its frozen feedback path.
- Model-owned S1 is mode-specific. `analyze` and the structural BOM fix do not establish autonomous agent decisions.
- Automatic behavioral adoption/verified activation is explicitly unavailable in CLI; S4 remains absent even though future-facing candidate evaluation exists.
- No inter-S1 S2 collision-feedback path is inferred from role isolation; no ultimate S5 is inferred from privacy and permission gates.
