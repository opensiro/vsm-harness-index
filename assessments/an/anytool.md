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
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# AnyTool

## Review boundary

- System in focus: one invocation of the published AnyTool research-time API-selection and task-solving harness against a ToolBench-style query, including its first-party meta/category/tool search agents, shared API pool, downstream API solver, and in-loop solution checking.
- Purpose and identity: choose relevant APIs from a large indexed tool universe and execute a bounded tool-use solution to the submitted query, revising the search when evidence says the current selection is inadequate.
- Relevant environment: incoming query and API taxonomy, tool descriptions, model responses, external RapidAPI/ToolBench service outcomes, available tokens/API count, and errors during execution.
- Standard-distribution boundary: the repository's documented `python scripts/main.py` execution using `arguments.py`, `anytool/`, and the bundled `toolbench/` inference/evaluation code actually called by that entry point. This is an executable research harness, not a deployed autonomous business process.
- Credited operating / distribution surfaces: [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py), [`anytool/api_database_function.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/api_database_function.py), [`anytool/dfs_gt.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/dfs_gt.py), [`anytool/verifier.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/verifier.py), the invoked ToolBench solver/evaluator packages, and documented configuration.
- Adjacent first-party surfaces excluded from ownership: ToolBench training and leaderboards, the standalone evaluation CLI, data-generation/preprocessing scripts, sample datasets, author/repository governance and CI. Hosted OpenAI/Azure inference, RapidAPI, ToolBench keys and the remote APIs themselves are outside the first-party decision boundary; the harness's own model-call orchestration is included.
- First-party operating / deployment modes considered: default threaded multi-level search with top-level/category/tool agents; shared API sufficiency and bounded DFS solution/retry; synchronous fallback when `multi_thread` is false. No provider-backed run, third-party API call or benchmark execution was performed for this review.
- Recursion level: one research query-solving organization; category/tool agents are subordinate operational search cells, not automatically separate viable recursive organizations.
- Reviewed revision: `6202212ce45329282cf812ae48427f8765cf164c`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[`README.md`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md) documents the research implementation, its API/tool database, model and ToolBench prerequisites, and local runner. In `scripts/main.py`, `Main_Search_Agent` uses model function calls to choose API categories; `Category_Agent` divides tools; `Tool_Agent` chooses concrete APIs and contributes them to a global candidate pool. Child searches may run in threads behind a 16-slot semaphore and selected shared-state locks. The runner then calls `solve_given_api_main` over selected tools, checks the result, prunes unsuitable APIs and resumes unfinished search agents with failure feedback. `anytool/rapidapi.py` and ToolBench solver code execute external function calls; the model provider and APIs remain external. Configuration and dataset queries are supplied at launch. JSON messages, search trees, token counts and check results are saved under the configured output directory. There is no shipped long-lived service, organizational policy authority, scheduled evolution loop or formal multi-user governance.

The in-run evaluator deserves separate treatment. `anytool/verifier.py::check_solved_toolbench` calls the bundled ToolBench pass-rate evaluator on saved solution data and sends its majority result/reason into another search iteration. This is more than an ordinary completion flag, but its real independence from production reporting and API reality is bounded and requires the S3* question below. No benchmark score is used as a VSM state.

## Operational model

The outcome is a solved API-use query or explicit unsuccessful/timeout result. The top-level search agent, category search agents and tool search agents enact differentiated operational API discovery, while the downstream solution generator executes the selected tools. Model decisions choose categories, tool groups, APIs and next actions; Python enforces thread budget, shared-store updates, fixed token/API limits, and execution mechanics. External API services and the evaluator's model endpoint do not become first-party policy owners. An answer check can trigger a new in-query search but is not evidence that the harness changes its future installed capability.

## S1 — Operations

- State: A
- Function: perform the query-specific transformation from user goal and observed API/tool environment into selected tool calls and a task result.
- Disturbance / variety regulated: heterogeneous natural-language requests, an extensive API taxonomy, changing tool results, malformed calls and unsuccessful answers.
- Decisive decision or feedback right: model-selected categories, tools and APIs, followed by a model/tool action sequence that may be revised from tool/error observations.
- Decision owner: the first-party wired model-backed `Main_Search_Agent`, `Category_Agent`, `Tool_Agent` and downstream solver; external inference provider serves decisions but does not itself own the harness workflow.
- Supporting / enforcement mechanisms: API database functions, Python threads/semaphore, argument limits, schema/function dispatch, RapidAPI wrapper, JSON state and fixed iteration caps.
- Closure path: chosen APIs enter the shared pool, the solver attempts the query, execution/solution feedback is returned to search-agent messages, and a new selection or answer follows.
- Boundary reachability: `scripts/main.py` instantiates and runs these actors and solver as its ordinary documented entry point; no separate dogfood actor is necessary.
- Why this is / is not agent-owned: removing the model-backed decision makers leaves only a fixed taxonomy/database and execution shell, not the discretionary API selection and iterative solution.
- Evidence: [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py) (`Main_Search_Agent.assign_main`, `Tool_Agent.tool_search`, main `__main__` solve/refind loop); [`anytool/dfs_gt.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/dfs_gt.py); [`README.md`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md).
- Basis: structural.
- Confidence: high for a source-wired research-time agent loop.
- Caveats: no external model/tool invocation was run; real-world success/reliability is not established.

## S2 — Coordination

- State: C
- Function: attenuate simultaneous tool-search cells' interference over one finite shared pool of selected APIs.
- Disturbance / variety regulated: separately executing `Tool_Agent` cells can select the same API or contend for the common max-API resource, producing duplicate selection, pool overflow or premature sufficiency decisions.
- Distinct S1 units: concurrently launched tool-search cells below one or more category agents; each searches a different assigned subset of the API taxonomy.
- Inter-S1 disturbance: duplicate selected APIs and competing additions against `global_api_list`/`max_api_number`, with a shared `stop` criterion.
- Attenuating coordination relation: `add_apis_into_api_pool` checks pool capacity, deduplicates APIs, serializes the tool-call insertion through `counter_lock`, and rechecks whether the common pool can solve the query.
- Feedback into subsequent S1 behaviour: an insertion result reports API count/sufficiency/error to the originating Tool Agent; shared `stop` and refind feedback constrain further tool-agent selection.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited code directly guards a concrete duplicate/over-capacity collision among concurrent API producers. Merely spawning category agents or listing a tree would not suffice.
- Decisive decision or feedback right: whether to accept each candidate API into the common bounded pool and return a capacity/sufficiency signal to the search cells.
- Decision owner: the shipped deterministic shared-pool coordination code; no agent-owned discretion over cross-cell conflict resolution is evidenced. Autonomous agents choose APIs but do not revise the S2 deduplication/locking rule.
- Supporting / enforcement mechanisms: Python `Lock`, semaphore, pool and count variables, model-based sufficiency check and per-agent messages.
- Closure path: accepted/denied/duplicate selection changes shared capacity and reported feedback; search cells subsequently select more APIs or stop.
- Boundary reachability: the coordination function is invoked by `Tool_Agent.tool_search` in the default threaded runner; it is not an unused generic extension point.
- Why this is / is not agent-owned: the cross-cell collision rule remains the same if the model selector changes; the first-party S2-specific constructor/runtime primitive exists, but no autonomous coordinator owns its policy or correction discretion.
- Evidence: [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py) (`Tool_Agent.add_apis_into_api_pool`, `tool_search`, `counter_lock`, `sem`, `stop`).
- Basis: structural.
- Confidence: medium; scope is API-pool interference, not arbitrary inter-agent negotiation.
- Caveats: the documented locking protects the addition path; it is not a proof of race-free behavior for every global read, and this narrow coordination is not generalized across separate user-query runs.

## S3 — Inside-and-now control

- State: —
- Function: no established whole-system current-control function above the task's routing and global resource enforcement.
- Disturbance / variety regulated: the task can run out of tokens/APIs or need replanning, but fixed bounds and resuming a search cell do not establish whole-current S3 regulation.
- Decisive decision or feedback right: no first-party whole-system discretionary allocation/commitment decision beyond per-query category/tool search and hard threshold enforcement was located.
- Decision owner: initial model category selection and fixed Python orchestrator logic; developer sets limits; no qualifying S3 owner established.
- Supporting / enforcement mechanisms: `max_api_number`, `total_tokens`, `stop`, thread/semaphore orchestration and solver/refind controls.
- Closure path: these mechanisms constrain a query's search or retry; they do not close separate current enterprise/whole-system accountability, resource bargaining or intervention.
- Why this is / is not agent-owned: the main agent chooses search branches for the query, but it is not shown to own a distinct whole-system resource/commitment decision informed by an aggregate current operational view.
- Evidence: [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py) (`Main_Search_Agent`, pool checks and main loop); [`arguments.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/arguments.py).
- Basis: structural.
- Confidence: medium.
- Caveats: this is the single-query standard-distribution boundary, not a claim about all possible deployments.

### Absence scope

- Surfaces inspected: root README, `arguments.py`, hierarchical search classes, shared-pool/stop controls, downstream solve/refind loop, API wrapper and evaluator entry points.
- Plausible first-party paths checked: main meta-agent category assignment, global selected-API view, token/API limits, thread semaphore, failure-based tool pruning and resume scheduling.
- Why no material first-party path remains: these paths route or constrain one query's discovery/solution process; no separately evidenced whole-system current view plus substantive resource/commitment decision authority and returned control of the whole is wired in the supported mode.

## S3* — Complementary audit

- State: ?
- Function: plausible in-run challenge of solution claims, with unresolved independence and complementary-access strength.
- Disturbance / variety regulated: a solver may report a plausible final answer despite incomplete or invalid API execution.
- Decisive decision or feedback right: `check_solved_toolbench` obtains several ToolBench evaluator verdicts and returns a majority pass/fail plus reason that can trigger a fresh API search; the code establishes a challenge path but does not establish that the evaluator independently accesses ground truth rather than the solver's own report.
- Decision owner: model-backed ToolBench evaluator makes the judgment; Python aggregates outcomes and resumes search. Whether this is sufficiently independent audit ownership at the declared recursion remains unresolved.
- Supporting / enforcement mechanisms: stored solution transcript, ToolBench conversion, `compute_pass_rate` and evaluator prompts, a three-call pool, majority vote and reason forwarding.
- Closure path: an unsuccessful external evaluation sends `failed_reason` into `resume_search`, may prune prior APIs and leads to a subsequent solver attempt. This corrective return is source-wired, conditional on the evaluator verdict.
- Why this is / is not agent-owned: a model evaluator judges the candidate answer, but the independence from the ordinary operational answer claim and materially different access to reality cannot be firmly established from its inputs/prompted status check alone.
- Evidence: [`anytool/verifier.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/verifier.py) (`check_solved_toolbench`); [`anytool/check_solved.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/check_solved.py) (`compute_pass_rate`, answer/available-tools inputs); [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py) (check result/refind path).
- Basis: structural for the evaluator/return, unknown for independent complementary access.
- Confidence: medium for existence of a separate challenge, low for positive S3* ownership.
- Caveats: benchmark-oriented correctness evaluation may be an adjacent research measurement; the reviewed source does wire it into the default task loop, so a blanket no-path claim would also be premature.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental adaptation function established for continuing harness capability.
- Disturbance / variety regulated: tool failures and unsolved current queries drive within-query refind, not a future-oriented capability change across runs.
- Decisive decision or feedback right: no actor is wired to decide future tool inventory, strategy or platform adaptation from external trend evidence.
- Decision owner: model agents revise the current API selection; developer and static configuration determine later deployments.
- Supporting / enforcement mechanisms: saved run outputs, API database retrieval, refind prompts, and benchmark score files.
- Closure path: within-query retry changes the current solution path but no returned externally/prospectively grounded adaptation into later installed capability is evidenced.
- Why this is / is not agent-owned: solving the current query again is operational correction, not outside-and-then intelligence.
- Evidence: [`scripts/main.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py) (refind loop and output persistence); [`README.md`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: nothing here rules out an externally built S4 around the tool.

### Absence scope

- Surfaces inspected: published runner, API taxonomy, feedback prompts, DFS solver, run output persistence, README and adjacent evaluation/training surfaces.
- Plausible first-party paths checked: failure-aware `resume_search`, selected-API pruning, cached JSON messages and automated ToolBench pass-rate evaluation.
- Why no material first-party path remains: these paths improve or score the *current* task attempt and do not carry external/future distinctions through adaptation options into a lasting current capability update of the assessed runtime.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision and authoritative return path established at the task-solving organization.
- Disturbance / variety regulated: permitted API count, provider keys and task completion criteria are startup constraints, not unresolved organizational identity/policy matters.
- Decisive decision or feedback right: configuration and prompts are supplied by developers/operator; no first-party policy-level deliberation/ratification path is wired.
- Decision owner: external developer/operator for constants and credentials; no qualifying first-party or parent-governed S5 closure established.
- Supporting / enforcement mechanisms: `arguments.py`, `config_example.py`, static agent prompts, API whitelist, `stop` and timeout limits.
- Closure path: static configuration conditions operation, but no identity-level issue reaches legitimate ultimate authority and returns as a decision to govern subsequent execution.
- Why this is / is not agent-owned: changing a command-line limit or selecting an API is routine operations/configuration, not ultimate-policy choice.
- Evidence: [`arguments.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/arguments.py); [`config_example.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/config_example.py); [`anytool/prompt_template.py`](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/prompt_template.py).
- Basis: structural.
- Confidence: medium.
- Caveats: OSS maintainers have project-level decisions, but repository maintenance is outside the runtime recursion and cannot donate S5.

### Absence scope

- Surfaces inspected: CLI configuration, main runtime/agent prompts, API database/whitelist, evaluation/refind and repository README.
- Plausible first-party paths checked: main agent strategy decisions, static tool access limits, user query input, evaluator failure response and developer-owned keys/settings.
- Why no material first-party path remains: none carries an identity/ultimate-policy matter to a legitimate policy authority and returns an authoritative policy decision into future task execution at the assessed recursion.

## Distributed OSS parent arrangement

The public repository documents research code and prerequisites, not a first-party organizational governance loop for independent users. The source does not expose an Index-eligible parent-owned S3/S4/S5 path inside one query-solving runtime; independent contributor/release decisions remain outside this system boundary.

## Self-hosted and non-human modes

The local scripted mode is operator-configured but model-driven for API discovery/solving. Switching to a local model or serial thread path does not establish a separate parent S3/S4/S5 decision loop. Its model-powered search cells are subordinate to a fixed research workflow, not independently established viable recursive organizations.

## Recursion

Category and tool agents have local search assignments, but no separately evidenced full metasystem/identity and closure that would establish them as recursive viable systems. The catalog's API hierarchy is not a VSM recursion tree.

## Variety and escalation

The API database attenuates a large action space into categories, tools and selected APIs; model-guided search amplifies local response variety. A shared pool/threshold reduces cross-cell collisions and total tool context. Errors and answer failures re-enter search-agent prompts. The external human/API credential/provider and fixed token/API budgets bound the loop; exhausting them produces failure/timeout, not an autonomously ratified identity change. No genuine algedonic channel is established by `stop`, error logs or benchmark status alone.

## Evidence gaps

- S3*: the in-run ToolBench evaluator consumes solver outputs and available-tool metadata; the source does not establish materially independent raw service/world access or independent judgment sufficient to distinguish a complementary audit from a routine benchmark correctness judge. This specific shipped path warrants `?` rather than unproven `A` or unsupported `—`.
- No first-party tool/model/API execution was performed in this source-only review; actual model reliability, parallel race behavior and external API reachability remain untested, without changing the static source-backed S1/S2 findings.
