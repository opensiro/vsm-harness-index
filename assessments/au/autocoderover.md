---
harness_id: autocoderover
project_name: AutoCodeRover
repository: https://github.com/AutoCodeRoverSG/auto-code-rover
review_ref: 585d3e639aeda58ef0b6a151dd1cc2721a94d267
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AutoCodeRover

## Review boundary

- System in focus: the first-party, local Python AutoCodeRover issue-to-patch runtime at the frozen revision, not the research consortium, SWE-bench as an external evaluator, or a hosted foundation model.
- Purpose and identity: navigate a Python project's code, locate suspected faults, synthesize applicable patches, and optionally construct/review executable issue reproducers.
- Relevant environment: an issue description; checked-out target source and its tests; search API responses, Python execution and regression-test results; configured external model provider.
- Standard-distribution boundary: `app/main.py`, `app/inference.py`, `app/search/`, `app/agents/`, `app/api/`, `app/task.py`, and first-party CLI modes.
- Credited operating / distribution surfaces: default model-guided iterative search/patch; the opt-in SWE-bench `--reproduce-and-review` generator that compares distinct test and patch proposals and separately feeds back to their generators.
- Adjacent first-party surfaces excluded from ownership: research paper, published pass-rate claims, SWE-bench leaderboard, output samples, development tests, Docker/CI infrastructure, external model internals and the human developer organization.
- First-party operating / deployment modes considered: `github-issue`, `local-issue`, `swe-bench`; optional SBFL, validation and experimental SWE-bench reproduce/review; single or grouped multiprocessing execution.
- Recursion level: a single issue-to-patch AutoCodeRover execution, including its specialized test/patch production cells in the opt-in review mode; not the external project being repaired.
- Reviewed revision: [`AutoCodeRoverSG/auto-code-rover@585d3e639aeda58ef0b6a151dd1cc2721a94d267`](https://github.com/AutoCodeRoverSG/auto-code-rover/tree/585d3e639aeda58ef0b6a151dd1cc2721a94d267), frozen by [intake #237](https://github.com/opensiro/vsm-harness-index/issues/237) and [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-22; source-first review, no LLM/provider-backed execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The CLI creates a task from a GitHub issue, local issue or SWE-bench input and checks out/prepares its target source. `run_one_task` cycles configured models over bounded retries. Each attempt can write and execute a reproduction test, derive optional fault-localization data, conduct iterative model-selected AST-aware code searches through `SearchManager`, and ask `PatchAgent` to generate an applicable diff. Validation, retry and final candidate selection are available; validation is **off by default**, so producing/choosing a patch does not prove correctness. Grouped subprocesses run task batches, not cooperating agents managing a shared organization.

In the experimental `swe-bench --reproduce-and-review` route, `TestAgent` and `PatchAgent` generate separate candidate artifacts with their own prompts and feedback histories. `ReviewManager` executes the test against original and patched code. A distinct model call considers whether **the test** or **the patch** is wrong, returns two independent yes/no decisions and advice, and sends corrective feedback back to the appropriate generator. This relation is narrower than a general multi-agent control plane, applies only if a reproducible test was found, and is not enabled for ordinary GitHub/local modes.

Evidence: [CLI and review mode](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L38-L119), [mode flag](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L155-L185), [issue pipeline](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/inference.py#L98-L326), [review feedback router](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/api/review_manage.py#L78-L171).

## Operational model

AutoCodeRover's main operational unit is an issue-resolution coding agent whose model selects source-search actions, observes tool results and proposes patch text. The optional reproducer and patch generators are distinct narrowly tasked S1 cells, each with its own generation history and revision after feedback. An opt-in model reviewer assigns fault between these cells and returns separately addressed corrective information. The runtime/orchestrator owns deterministic limits, process grouping and final acceptance conditions; the human operator controls the starting issue, model, flags and permissions. Nothing makes this local patch repair workflow the current-resource governor, outside-future strategist or supreme authority of the project's organization.

## S1 — Operations

- State: A
- Function: investigate a supplied code issue and produce an applicable candidate patch through autonomous search and code-edit choices.
- Disturbance / variety regulated: uncertainty about code locations, incompatible search requests, non-applicable diffs, failed reproduction and regression outcomes.
- Decisive decision or feedback right: select iterative search APIs and suspected bug locations, generate patch content, and revise attempts after code/tool feedback.
- Decision owner: first-party search/patch model interactions; operator selects provider and issue, while deterministic backends execute code searches and validation.
- Supporting / enforcement mechanisms: `SearchBackend` AST-aware calls, API-call proxy, diff extraction/applicability, optional SBFL and test execution, bounded retries and candidate selection.
- Closure path: issue + repository → model-selected code search → returned source context → model-generated patch → applicability/test/reviewer feedback → next patch or output selection.
- Boundary reachability: the main source-search/patch path is the default `github-issue`, `local-issue` and SWE-bench work mode and does not require the experimental reviewer.
- Why this is / is not agent-owned: model-generated search instructions and patch content vary with observed task data; configured round ceilings, tool execution and user-provided issue are supporting restrictions, not owners of those decisions.
- Evidence: [search selects APIs and consumes outcomes](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/search/search_manage.py#L29-L196), [model-generated applicable patch and feedback](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/agents/agent_write_patch.py#L97-L210), [pipeline](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/inference.py#L263-L326).
- Basis: structural.
- Confidence: high for the shipped model/tool/patch control loop; no claim about the patch's external task success.
- Caveats: live model-backed operation was not tested; ordinary validation is opt-in and some tasks fall back to patch-only generation.

## S2 — Coordination

- State: A
- Function: in the experimental reproducer/reviewer mode, dampen conflict between independently proposed issue reproducer and corrective patch by adjudicating which of the two must be revised.
- Disturbance / variety regulated: a patch can make a faulty test pass, or a valid patch can seem wrong because the test incorrectly represents the issue; indiscriminate iteration on only one cell would perpetuate mismatch.
- Distinct S1 units: `TestAgent` autonomously proposes executable reproducing tests; `PatchAgent` autonomously proposes code changes, each with a dedicated model prompt, artifacts and feedback/revision history.
- Inter-S1 disturbance: their *joint* candidate outcome disagrees with the observed buggy/patched reproducer results and issue semantics, with the conflict potentially attributable to either test construction or patch construction.
- Attenuating coordination relation: an independent reviewer model is given the issue, both artifacts and original/patched execution evidence and returns separate `patch-correct` / `test-correct` judgments and targeted advice.
- Feedback into subsequent S1 behaviour: `ReviewManager._generator` routes `patch_decision == NO` to `PatchAgent.add_feedback` and `write_applicable_patch_with_feedback`, while `test_decision == NO` updates `TestAgent.add_feedback` and `write_reproducing_test_with_feedback`; the resulting artifacts are re-executed on the following round.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the reviewer is explicitly asked to settle **which of two distinct operational outputs is defective**, and that decision changes which S1 producer receives a corrective instruction. Merely executing tests or selecting the last patch is not the credited S2 relation.
- Decisive decision or feedback right: dynamically judge whether to correct the test, patch or both from cross-cell evidence; the Python manager routes the judgment.
- Decision owner: first-party model reviewer in the opt-in mode, not the fixed CLI scheduler or a user-assembled external supervisor.
- Supporting / enforcement mechanisms: original/patched repro execution, two-sided review JSON, separate feedback histories, bounded review rounds and validation.
- Closure path: test + patch candidates → execute both interpretations → reviewer locates mismatch → affected producer receives focused feedback → regenerated test/patch enters next comparison.
- Boundary reachability: the first-party SWE-bench `--reproduce-and-review` switch installs this loop when a valid reproducer exists; it is experimental, **off by default**, and not exposed for general local/GitHub issue commands.
- Why this is / is not agent-owned: the correctness allocation and advice are discretionary reviewer-model output; the manager's branches only implement the model's two judgments. This does not imply shared-system scheduling, generic writer-conflict mediation or whole-current governance.
- Evidence: [flag and scope](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L155-L185), [mode gate](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/inference.py#L288-L324), [two-sided reviewer prompt](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/agents/agent_reviewer.py#L111-L186), [feedback dispatched to each agent](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/api/review_manage.py#L111-L171), [reproducer feedback memory](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/agents/agent_reproducer.py#L46-L121).
- Basis: structural.
- Confidence: medium; the narrowly defined test/patch coordination closure is explicit, but no model-run has established effectiveness or a broader autonomous S2.
- Caveats: opt-in experimental SWE-bench only; no reproducer means fallback to patch-only generation. The review loop is quality-focused, does not coordinate parallel workers or resource contention, and its S2 interpretation depends on treating the test and patch generators as distinct operational units rather than one monolithic coding S1.

## S3 — Inside-and-now control

- State: —
- Function: direct present resource, commitment, priority and accountability trade-offs of multiple operating units for the whole assessed harness.
- Disturbance / variety regulated: model/task retries, concurrent batch workloads, failing patch attempts and tool execution time.
- Decisive decision or feedback right: none established at an S3-specific organizational level; task grouping, fixed retry limits and patch selection are preset process management.
- Decision owner: human CLI/config author and deterministic orchestration, with model decisions local to repair tasks.
- Supporting / enforcement mechanisms: `ProcessPoolExecutor`, group sequencing, overall retry limit, model cycling, validation and generated patch selection.
- Closure path: user-supplied task groups → parallel/serial processing → per-issue output; no separate current-wide negotiation/reprioritization and corrective allocation among an accountable whole.
- Why this is / is not agent-owned: process limits and ranking candidate patches do not own whole-organization resource/commitment decisions.
- Evidence: [task group scheduling](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L373-L493), [bounded attempts and selection](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/inference.py#L98-L240).
- Basis: structural.
- Confidence: high for the bounded first-party negative.
- Caveats: a separate operator organization can add current management, but is outside this assessed runtime.

### Absence scope

- Surfaces inspected: CLI and multiprocessing orchestration, task/retry path, candidate selection, review manager and config switches.
- Plausible first-party paths checked: shared budget allocation, cross-issue priority revision, delegation commitment negotiation and runtime whole-current operational interventions.
- Why no material first-party path remains: observed actions choose/execute local issue attempts or fixed batch jobs, without a separate whole-current discretionary management relation.

## S3* — Complementary audit

- State: —
- Function: independently challenge an S3 current-management claim using a complementary route to operational reality, then return findings for corrective control.
- Disturbance / variety regulated: potentially false patch-correctness claims and misleading local tests.
- Decisive decision or feedback right: no such S3 audit right; the experimental `agent_reviewer` decides whether local code/test artifacts are correct as ordinary repair-loop QA.
- Decision owner: model reviewer and deterministic validator under S1/S2 repair production, not a distinct management auditor.
- Supporting / enforcement mechanisms: test execution against original/patched code, reviewer feedback JSON, optional regression validation and logs.
- Closure path: code/test pair → reviewer/validator → revise task artifacts, not S3 claims → independent operational audit → S3 corrective management return.
- Why this is / is not agent-owned: the reviewer is model-owned but its object is the code patch and reproducer, not complementary verification of whole-current S3 management.
- Evidence: [reviewer's actual task](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/agents/agent_reviewer.py#L14-L35), [manager feedback scope](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/api/review_manage.py#L111-L171), [local patch validation](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/api/validation.py#L191-L263).
- Basis: structural.
- Confidence: high for task-level QA versus S3* boundary.
- Caveats: the term "reviewer" alone does not establish audit ownership at organizational recursion.

### Absence scope

- Surfaces inspected: reviewer input/output, original-versus-patched execution, validation controls, logs and result selection.
- Plausible first-party paths checked: independently collected S3 management evidence, audit appointment/independence and authority to return audit findings to present whole-system control.
- Why no material first-party path remains: there is no assessed S3 current-management assertion or complementary S3 audit/recovery path.

## S4 — Outside-and-then intelligence

- State: —
- Function: monitor wider future environment, propose adaptive changes and return selected options to current harness capability.
- Disturbance / variety regulated: unfamiliar future issue classes, external library changes, provider variation and changing codebases.
- Decisive decision or feedback right: no evidenced prospective organizational capability decision; model selection, fault localization and retrieval are for the present issue.
- Decision owner: user/developers choose providers, install new methods and maintain the project; the repair model chooses present-task actions.
- Supporting / enforcement mechanisms: model alternatives, AST search, issue context, regression feedback, retries and an external paper/benchmark.
- Closure path: issue/code evidence → patch for the same issue, or configured provider fallback; not future trend sensing → strategic adaptation → returned capability change.
- Why this is / is not agent-owned: solving a previously unseen issue is S1 operational adaptation, not an installed outside-and-then intelligence function.
- Evidence: [pipeline and model retry](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/inference.py#L98-L142), [public research and scope statement](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/README.md#L16-L91).
- Basis: structural.
- Confidence: medium-high for reviewed runtime.
- Caveats: external researchers can measure and change future versions, but their decisions are outside the one-run harness boundary.

### Absence scope

- Surfaces inspected: README operating claims, CLI modes, model/retry config, source search, patch selection and experiment-facing entrypoints.
- Plausible first-party paths checked: ongoing external trend sensing, option comparison for future organizational capability, and feedback to current S3 adopting a change.
- Why no material first-party path remains: the observed inputs and revisions are local issue/patch decisions or human-maintained research releases, not first-party prospective management.

## S5 — Policy and identity

- State: —
- Function: settle ultimate purpose and binding identity/policy conflicts for the running organization.
- Disturbance / variety regulated: requested edits outside intended scope, provider-policy rejection, task-local constraints and permissible execution.
- Decisive decision or feedback right: no first-party ultimate policy/identity decision path; user provides issues/models/options and model produces candidate patches subject to configured guards.
- Decision owner: human operator/developer for values and configuration, with external provider policy enforced by provider.
- Supporting / enforcement mechanisms: CLI tasks, prompt instructions, errors/exception fallback and test validation.
- Closure path: user-supplied goal/config → issue repair attempt; no identity-level disagreement → legitimate ultimate authority → binding policy decision returned to the operating system.
- Why this is / is not agent-owned: prompt-level do/don't rules and fallback on an external content-policy exception do not transfer supreme policy authority to the coding agent.
- Evidence: [CLI goal and model selection](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L38-L150), [provider-policy exception fallback](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/main.py#L597-L625), [patch prompt scope](https://github.com/AutoCodeRoverSG/auto-code-rover/blob/585d3e639aeda58ef0b6a151dd1cc2721a94d267/app/agents/agent_write_patch.py#L22-L77).
- Basis: structural.
- Confidence: high for bounded negative at the local runtime.
- Caveats: broader project governance and legal restrictions are external arrangements.

### Absence scope

- Surfaces inspected: CLI entrypoints, configured models, patch/reviewer prompts, permissions implicit in source execution and provider fallback.
- Plausible first-party paths checked: mission/identity change requests, contested supreme values, legitimate parent adjudication and binding post-decision policy application.
- Why no material first-party path remains: no explicit identity-policy arbitration or returned supreme directive exists in the inspected first-party runtime.

## Distributed OSS parent arrangement

The AutoCodeRover researchers and outside contributors maintain the repository, and users may run independent local issue repairs. Those release and publication decisions are not a shared S3/S4/S5 authority executing inside each AutoCodeRover task. No `P` or parent-mode modifier is credited from the public organization's existence.

## Self-hosted and non-human modes

Self-hosted Docker/local operation lets the operator choose models and target repositories; models can be local or external. Experimental review is a source-supported optional flag under SWE-bench, not a distinct human-governed S3/S4/S5 operating mode. Without a reproducer or under general local/GitHub issue commands, the reviewed special S2 loop does not run. The positive S1 loop is model-directed rather than human-stepped, but no live model task was executed in this assessment.

## Recursion

The TestAgent/PatchAgent pair produces separate working artifacts, and a reviewer controls their compatibility in an opt-in task. They do not themselves contain distinct S3/S4/S5 functions. Concurrent SWE-bench task subprocesses are batch execution cells, not automatically another viable organization or mutual-current governance layer.

## Variety and escalation

Source search feeds concrete repository context to patch synthesis. Applicable-diff extraction, reproducibility checks and optional regression tests reject local failures. The narrow experimental two-sided review relation routes the *reason for mismatch* to the test or patch cell; generic retry counters and error logs do not acquire S3 or S3* authority. No separate algedonic escalation into identity/current-governance control is supported by this boundary.

## Evidence gaps

- Source-only review; no provider-backed LLM-agent run or real SWE-bench repair experiment. Script tests and static analysis cannot establish measured coordination success.
- The reviewer pathway is explicitly experimental, off by default and available only for SWE-bench issues with an executable reproducer. S2 is strictly limited to this two-producer mismatch relation; a reviewer may reasonably dispute whether these task-local producers constitute independent S1 cells for S2 rather than internal S1 verification.
- Default patch validation is disabled. Neither a returned `True` from `run_one_task` nor a published benchmark percentage demonstrates task correctness at the inspected revision.
