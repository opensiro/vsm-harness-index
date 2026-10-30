---
harness_id: anytool
project_name: AnyTool
repository: https://github.com/dyabel/AnyTool
review_ref: 6202212ce45329282cf812ae48427f8765cf164c
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AnyTool

## Review boundary

- System in focus: one AnyTool query execution, including hierarchical API discovery, a shared bounded API pool, API execution/answer generation and feedback-driven resumed search.
- Purpose and identity: solve natural-language requests using a large API database, choosing relevant APIs and executing a solution.
- Relevant environment: user requests, API descriptions, actual remote API responses/errors, model outputs and limited shared API/context capacity.
- Standard-distribution boundary: documented local Python runner `scripts/main.py`, repository-owned `anytool/` code and the vendored ToolBench solver adapters it actually instantiates.
- Credited operating / distribution surfaces: `scripts/main.py`, `anytool/api_database_function.py`, `anytool/dfs_gt.py`, `anytool/rapidapi.py`, `anytool/verifier.py`, `anytool/check_solved.py`, `anytool/prompt_template.py` and wired ToolBench inference code. Credit the concrete AnyTool composition, not arbitrary ToolBench capabilities.
- Adjacent first-party surfaces excluded from ownership: dataset generation, preprocessing, training/retrieval experiments, leaderboard/pass-rate summaries and paper metrics; GitHub maintenance and license authorship. External Azure/OpenAI, RapidAPI/ToolBench services and model internals remain dependencies.
- First-party operating / deployment modes considered: documented ToolBench/AnyToolBench runner; default threaded search and its explicit sequential branch; CLI-selected limits and stored-result continuation. No shipped interactive parent-governance mode was found.
- Recursion level: one query organization with category/tool retrieval work cells and a solver; spawning a hierarchy does not establish recursively viable systems.
- Reviewed revision: `dyabel/AnyTool@6202212ce45329282cf812ae48427f8765cf164c`, frozen #2406 / controller #2407 row 1.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [documented runner](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md) launches a main search agent, category agents and tool agents. Each model-driven cell queries descriptions, selects categories/tools/APIs and finishes or resumes from feedback. API selections enter a shared pool with a configurable maximum. A solvability model sees the aggregate detailed pool and can stop further search. The first-party DFS adapter instantiates the vendored tool-calling solver and returns its artifact. Solved checks and failure reasons can cause API pruning and renewed retrieval.

[Runner state and limits](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1-L103) include locks/semaphores, messages, finish/stop flags and token accounting. These mechanisms enforce or carry decisions; they are not automatically their owners. [The query loop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L890-L1138) persists artifacts and resumes failed search cells. The [CLI](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/arguments.py) supplies launch-time limits; it is not a live parent deliberation loop.

## Operational model

Category/tool cells deliver useful API candidates from distinct local portions of the API environment; the solver performs calls and produces the user answer. Agents own semantic relevance, API subset selection, action choice and completion judgments. Developers select initial budgets; deterministic locks and gates enforce them. The pooled solvability model owns an additional aggregate current-control judgment, distinct from initial task decomposition. Operators supply queries/credentials and launch configuration, without an evidenced runtime identity/adaptation mandate.

## S1 — Operations

- State: A
- Function: discover relevant APIs and execute a query solution.
- Disturbance / variety regulated: unfamiliar API descriptions, changing tool outputs, missing APIs and failed candidate solutions.
- Decisive decision or feedback right: choose categories, tool/API subsets, subsequent solver actions and whether to finish or retry.
- Decision owner: model-driven search and solver agents in the shipped runner.
- Supporting / enforcement mechanisms: API lookup functions, threads, message histories, DFS tool adapter, remote calls and result files.
- Closure path: tool/error output returns to agent messages; failed solution reasons resume retrieval and a new selected API set reaches the solver.
- Boundary reachability: README invokes `scripts/main.py`, which constructs these cells and directly calls `solve_given_api_main`; no custom actor composition is required.
- Why this is / is not agent-owned: removing model decisions leaves dispatch/storage but no semantic API or action choices.
- Evidence: [search cells and tool feedback](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L390-L678), [solver instantiation](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/dfs_gt.py#L87-L136), [solve/retrieve return](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1004-L1090).
- Basis: structural.
- Confidence: high.
- Caveats: source-established ownership, not a claim that remote APIs currently work or paper performance reproduces.

## S2 — Coordination

- State: A
- Function: mutual adjustment of API contributions competing for one bounded solver pool.
- Distinct S1 units: independently running tool-search agents with different assigned tool subsets.
- Inter-S1 disturbance: one cell's additions consume shared pool capacity, so a later cell's selected batch may exceed remaining slots; duplicate selections also compete for the same pool representation.
- Attenuating coordination relation: serialized pool admission rejects over-capacity contributions with current count and an instruction to reduce the candidate batch; duplicate APIs are suppressed.
- Feedback into subsequent S1 behaviour: the rejection is appended as a tool response to the submitting agent, whose next model turn can select a smaller set or finish; admitted contributions change available capacity for subsequent agents.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is concrete cross-cell contention over finite shared API capacity plus returned adjustment feedback, not the mere hierarchical delegation.
- Disturbance / variety regulated: conflicting demands for shared API slots.
- Decisive decision or feedback right: choose the revised relevant subset after another cell has consumed capacity.
- Decision owner: the receiving tool-search agent; developer chooses the maximum and runtime enforces admission.
- Supporting / enforcement mechanisms: `counter_lock`, duplicate checks, maximum count and tool-message transport.
- Closure path: rejected contribution → model receives remaining-capacity feedback → revised API selection → pool admission or termination.
- Boundary reachability: every `add_apis_into_api_pool` call in the default tool loop runs under the shared lock and returns its result into that same cell's model history.
- Why this is / is not agent-owned: a lock alone cannot select which APIs to drop; that semantic adjustment remains with the model.
- Evidence: [shared capacity and duplicate gate](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L499-L553), [execution and returned tool response](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L571-L666), [distinct worker construction](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L352-L388).
- Basis: structural.
- Confidence: medium.
- Caveats: a structurally reachable regulation path, not measured contention-free performance; no autonomous right to increase the configured maximum is claimed.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current search organization's aggregate commitment to further API discovery versus solving with its existing capability.
- Whole-system current view: the query and `global_api_list_detailed` collected across retrieval cells, together with shared sufficiency/stop status.
- Current-control decision scope: determine whether the aggregate available tools can solve the query and stop further search work; failed solving returns reasons for renewed search.
- Disturbance / variety regulated: wasteful continued retrieval after sufficient capability, or insufficient pooled tools for the current commitment.
- Decisive decision or feedback right: semantic solvability judgment over the whole current API pool.
- Decision owner: the model invoked by `check_task_solvable_by_function`; deterministic code applies its judgment.
- Supporting / enforcement mechanisms: global stop/status, per-cell stop checks, pool cap, semaphore and fixed token ceiling.
- Closure path: model verdict changes stop/status → search cells stop or continue → selected pool reaches solving; failure reasons return to search.
- Boundary reachability: `add_apis_into_api_pool` and `check_if_request_solvable` directly invoke this judgment in the normal runner, and active cell loops inspect its stop flag.
- Why this is / is not agent-owned: the aggregate sufficiency choice disappears without the judging model; fixed token/API limits remain separate developer choices.
- Evidence: [whole-pool judgment and stop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L82-L103), [judgment owner](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/verifier.py#L62-L102), [judgment returned into workers](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L526-L578).
- Basis: structural.
- Confidence: medium.
- Caveats: query-level current control only. The main search agent's category assignment alone is not the S3 witness. No qualifying separate parent mode is established.

## S3* — Complementary audit

- State: —
- Function: no complementary audit channel established beyond routine solver verification.
- Disturbance / variety regulated: possible false solved claims were checked as a candidate.
- Decisive decision or feedback right: no separately organized complementary audit right found.
- Decision owner: routine evaluator models judge the normal answer path; no additional audit owner credited.
- Supporting / enforcement mechanisms: repeated pass-rate checks, saved trajectories and failure-reason parsing.
- Closure path: routine failures prune APIs and resume search, but that is the normal production feedback path.
- Why this is / is not agent-owned: a separate model invocation does not itself establish complementary independent access.
- Evidence: [mandatory solved checker](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/verifier.py#L144-L179), [same-artifact evaluation](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/check_solved.py#L36-L98), [routine correction](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1016-L1068).
- Basis: structural.
- Confidence: medium.
- Caveats: the verifier can challenge an answer, but its repeated reading of the production artifact supplies no materially different operational access.

### Absence scope

- Surfaces inspected: runner, verifier/check_solved, DFS/rapidapi composition, README, result/recheck options and vendored ToolBench evaluation wiring.
- Plausible first-party paths checked: independent evaluator call, majority voting, saved-trajectory recheck and result-to-search correction.
- Why no material first-party path remains: these are normal solution acceptance checks using the same recorded answer/available-tool material; benchmark evaluation and leaderboards are adjacent. No complementary probe/reconciliation/audit authority is wired into the assessed mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability adaptation loop established.
- Disturbance / variety regulated: current query failure and changing API responses are handled as operational variety.
- Decisive decision or feedback right: no prospective adaptation choice returning into future capability found.
- Decision owner: search/solver agents own current-query retries only.
- Supporting / enforcement mechanisms: API database, failure reasons, result histories and preprocessing.
- Closure path: reflection returns to the same query, not a prospective S3–S4 capability conversation.
- Why this is / is not agent-owned: autonomous reflection is present but does not by itself establish S4.
- Evidence: [query-local reflection and re-search](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L987-L1090), [resume prompt path](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L555-L569), [documented run/preparation scope](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: broader research/training possibilities are outside this supported runner.

### Absence scope

- Surfaces inspected: retrieval/solver/resume paths, prompt templates, preprocessing scripts, CLI, saved results and README operating modes.
- Plausible first-party paths checked: failure-based API reselection, API database preparation, stored-query continuation and benchmark/training material.
- Why no material first-party path remains: runtime changes the current tool set to solve the existing task; no environmental/future model generates and installs capability-development options or closed parent adaptation decisions.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate-policy/identity closure established.
- Disturbance / variety regulated: ordinary query/budget/configuration constraints only.
- Decisive decision or feedback right: no identity-level issue-to-authority-to-return path found.
- Decision owner: users/developers choose queries, prompts and launch configuration outside runtime deliberation.
- Supporting / enforcement mechanisms: fixed prompt purpose, API/token ceilings and finish/stop conditions.
- Closure path: no identity-level returned decision governs subsequent operation.
- Why this is / is not agent-owned: selecting APIs or stopping retrieval does not confer ultimate authority.
- Evidence: [launch parameters](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/arguments.py), [role prompts](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/prompt_template.py#L7-L86), [runtime boundaries](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1-L103).
- Basis: structural.
- Confidence: high.
- Caveats: OSS maintainer rights are real but not a wired parent-governed mode at this query recursion.

### Absence scope

- Surfaces inspected: README, CLI/configuration example, role templates, runner stop/finish/retry and result continuation.
- Plausible first-party paths checked: user-defined query/limits, role instructions, solvability/final-answer decisions and maintainer changes.
- Why no material first-party path remains: none carries an identity/ultimate-policy matter to legitimate authority and returns its decision into operation; launch configuration and repository maintenance are not such a loop.

## Distributed OSS parent arrangement

No organization-level parent mode is credited. Local operators supply credentials/data and launch the runner; independent contributors and repository maintainers are outside this query organization's function ownership.

## Self-hosted and non-human modes

The local runner may execute without interactive human intervention after setup. Its sequential/threaded branches retain the same semantic owners. No separate first-party operator S3/S4/S5 loop is evidenced.

## Recursion

The main/category/tool tree is technical decomposition. Distinct retrieval cells have local API-search variety, but no claim of complete recursive viability follows.

## Variety and escalation

The API database and hierarchy attenuate discovery variety; model choices amplify relevant retrieval. Shared capacity feedback attenuates cross-cell contention. Failure reasons return to unsatisfied search cells; token caps, API caps and connection errors bound or stop execution. These are ordinary task recovery channels, not an evidenced algedonic channel.

## Evidence gaps

Static exact-ref source review and Python compilation only; no paid model, remote API, dataset download or live task was executed. API service availability, stochastic judgment reliability and bug-free concurrency are unverified. S2 and S3 claims are bounded structural ownership findings, not causal/performance results. No concrete additional shipped governance/adaptation/audit path remains unresolved in the declared runner.
