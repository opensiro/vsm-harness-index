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
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AnyTool

## Review boundary

- System in focus: one AnyTool task-processing run: hierarchical API-discovery agents and the subsequent API-using solver, with task-local retry and result checking.
- Purpose and identity: autonomously locate a usable subset of a large API catalog and execute a user's API-grounded query.
- Relevant environment: user queries, ToolBench API descriptions/data, unavailable or failing endpoints, API-list size and token limits, model responses, solver failures, and externally supplied API/model credentials.
- Standard-distribution boundary: first-party `scripts/main.py` with its category/tool-search agents, API pool and refind loop; first-party `anytool/dfs_gt.py` and ToolBench-derived solver adapter. OpenAI/Azure model inference, RapidAPI/ToolBench services and downloadable ToolBench data are external dependencies, not first-party decision owners.
- Credited operating / distribution surfaces: the published README invocation, `scripts/main.py` hierarchy and shared API pool, `anytool/api_database_function.py` catalog queries, `anytool/dfs_gt.py` solver invocation, and `anytool/rapidapi.py` request/observation adapter.
- Adjacent first-party surfaces excluded from ownership: `scripts/anytoolbench_generation.py`, `atb_data/`, standalone `anytool/check_solved.py`, upstream ToolBench benchmark and leaderboard/evaluation utilities, research metrics, maintainer development, and third-party remote providers. Only the verifier actually invoked by `scripts/main.py` is counted as an ordinary in-run check, not an independent audit.
- First-party operating / deployment modes considered: documented local Python command with model/ToolBench credentials, concurrent hierarchical discovery (default), configured non-threaded discovery (code path), initial solve and failure-driven refind, and direct ToolBench/DFS solver path. No separate first-party human supervisory or adaptation mode was found.
- Recursion level: the task-run organization, with distinct category/tool agents doing API discovery as its S1 work cells; the solver performs the subsequent API-execution work. Agent hierarchy alone does not establish recursive viability.
- Reviewed revision: `6202212ce45329282cf812ae48427f8765cf164c`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The documented [entry point](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md#L90-L103) starts `scripts/main.py`. `Main_Search_Agent` chooses API categories; `Category_Agent` partitions tools; `Tool_Agent` chooses individual APIs and adds them to a task-wide pool through function calls. Python threads run the cells subject to a semaphore and shared bookkeeping locks. A model-based sufficiency check stops further discovery when the aggregate APIs can answer the query. The main loop passes the selected pool to a DFS-based, model-directed API solver, tests the output, prunes failed APIs, and resumes unfinished discovery agents with failure feedback when needed. ToolBench interfaces, external model and live APIs supply the actual underlying execution substrate.

The task's state is mainly in process (`global_api_list`, `stop`, agent messages, tree and result lists) and serialized to result JSON. The source does not show an independently operating multi-task portfolio, long-horizon environment model, standing governance loop, or parent-return channel. The optional evaluation scripts and published benchmark pass rates are adjacent research surfaces rather than evidence of independent runtime audit. No live paid-provider E2E task was run in this source-only review.

Primary architecture evidence: [main hierarchy](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L73-L118), [tool-cell pool and sufficiency check](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L390-L553), [main task/refind loop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L898-L1082), [DFS solver](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/dfs_gt.py), [API execution adapter](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/rapidapi.py#L344-L489).

## Operational model

One input query creates category and tool discovery work cells. A model chooses categories/tools and API candidates through the first-party function-call interface. The shared pool creates both useful common task state and a real risk of concurrent duplicate additions, oversubscription, or conflicting search continuation. The Python harness coordinates the shared state, and a model sufficiency judgment can end collection. The whole-task controller tests the selected set with a real API-using solver; if unsuccessful, its feedback reopens unfinished agents. Successful work ends with an answer and task-level result log. These are bounded current-task decisions, not autonomous future strategy or identity policy.

## S1 — Operations

- State: A
- Function: autonomously discover APIs for a user request and carry out an API-grounded solving attempt.
- Disturbance / variety regulated: changing query requirements, catalog breadth, absent/invalid APIs, failed tool calls and solver observations.
- Decisive decision or feedback right: model-driven agents choose categories, tool groups and candidate APIs, while the solver chooses API calls and subsequent task actions from tool observations.
- Decision owner: first-party-dispatched LLM agents in the supported run; the external model endpoint executes inference but does not independently own the harness's task organization.
- Supporting / enforcement mechanisms: API metadata catalog, function-call dispatch, DFS runner, Python threads and task-result JSON.
- Closure path: input query -> model-selected categories/tools/APIs -> tool-environment execution -> returned observations/failure -> new model call or finished answer.
- Boundary reachability: `scripts/main.py` constructs `Main_Search_Agent`, spawns the child searches, and calls `solve_given_api_main` directly in the documented runnable path; the model-directed solver is wired rather than example-only.
- Why this is / is not agent-owned: without the model's task-conditional choices, the fixed API metadata and thread scheduling cannot select useful APIs or decide action sequences; source-defined guardrails do not replace this discretion.
- Evidence: [dispatch and hierarchy](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L680-L748), [tool agent choices](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L571-L660), [solver integration](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1006-L1027), [tool feedback](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/rapidapi.py#L344-L489).
- Basis: explicit and structural.
- Confidence: high for wiring, not measured task success.
- Caveats: requires separately provisioned model, API key, ToolBench data and live services; no provider-backed behavior reproduced here.

## S2 — Coordination

- State: C
- Function: attenuate interference among concurrent API-discovery cells sharing one candidate pool and global search state.
- Distinct S1 units: separate `Category_Agent` and `Tool_Agent` instances spawned by the same main search, potentially operating in concurrent threads.
- Inter-S1 disturbance: simultaneous additions to the bounded shared API pool can duplicate candidates or exhaust the task-wide API allowance; independently continuing searches can conflict with a sufficient-pool stop decision.
- Attenuating coordination relation: first-party duplicate guards, a mutex around tool-agent additions, shared `stop` feedback and a semaphore provide a concrete shared-pool coordination path.
- Feedback into subsequent S1 behaviour: a tool agent receives pool-limit or sufficiency feedback; `stop` causes peer cells to return rather than continue searching, and refind explicitly resumes unfinished cells only after the pool has been reconsidered.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: its shared-pool exclusion and stop feedback address concurrent interference in a bounded resource actually used by the distinct discovery cells, beyond simply allocating a category to a child.
- Disturbance / variety regulated: concurrent redundant additions and runaway overlapping search work around a shared API limit.
- Decisive decision or feedback right: regulate concurrent commits to the aggregate pool and communicate its sufficiency/limit condition to other discoverers.
- Decision owner: Python locking/limit mechanics enforce shared access; the model chooses candidate additions and a separate model-based sufficiency judgment selects whether collection should stop. There is no separately autonomous, fully evidenced S2 owner deciding an inter-cell conflict-resolution policy.
- Supporting / enforcement mechanisms: `counter_lock`, `Semaphore(16)`, duplicate checks, `max_api_number`, `stop`, status messages and child-agent life-cycle flags.
- Closure path: competing cells request pool additions -> synchronized insertion and duplicate/budget check -> pool sufficiency/limit signal -> child loops observe `stop` or add result and change subsequent search.
- Boundary reachability: `Tool_Agent.tool_search` directly wraps pool insertion under `counter_lock` in the default threaded runtime; the same runtime tests the shared stop condition before later calls.
- Why this is / is not agent-owned: the first-party S2-specific mechanism is present, but its contention-control policy is mostly fixed in Python; the agentic decisions serve API discovery and sufficiency rather than independently owning all inter-cell regulation. Thus this is a `C` constructor, not an `A` claim.
- Evidence: [thread/lock setup](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L17-L31), [pool bounds, dedupe and stop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L499-L553), [locked dispatch](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L631-L643), [child stop checks](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L555-L580).
- Basis: structural.
- Confidence: medium; concurrency safety is not formally verified.
- Caveats: the coordination is not transactional across every access to shared state, and the same Python guard may also be read as mechanical enforcement of whole-task S3 limits. `C` is restricted to the concrete inter-cell shared-pool path, not generic threading.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current whole-task API-resource commitment and decide when to move from discovery to solving, or back to discovery after failure.
- Disturbance / variety regulated: incomplete collective API coverage, accumulated API/tool cost, failed solver attempts and duplicate/unproductive search.
- Decisive decision or feedback right: decide whether the entire collected API portfolio suffices for the query; feed failure reasons into resumed search cells and stop or continue task-wide work under limits.
- Decision owner: the separately called model judge decides API sufficiency from the whole pool and question, while the main-loop Python controller determines the preprogrammed retry order and enforces token/API bounds; both are distinguished rather than attributing the hard limits to the model.
- Supporting / enforcement mechanisms: the global candidate pool, model-return parser, API limit, `stop`, result checker, DFS runner, selection/pruning and retry schedule.
- Closure path: all discovery cells contribute to a shared API portfolio -> model judges task-wide sufficiency -> shared stop changes their commitments -> DFS solver tests the portfolio -> failure reason prunes/resumes agents -> a new collective portfolio is tried.
- Boundary reachability: `Tool_Agent.add_apis_into_api_pool` invokes `check_task_solvable_by_function` on the aggregate pool, and the main `while` loop performs retry/refind and subsequent task execution within the documented command.
- Why this is / is not agent-owned: an agent chooses whether the current whole collection is adequate for the task; without that judgment, resource enforcement can halt at static ceilings but cannot make the same query-specific sufficiency decision. The scripted retry policy is not itself an agent-owned right.
- Whole-system current view: shared API list and descriptions, query, pool size/max, `stop`/status, per-agent unfinished status and last solver/checker outcome.
- Current-control decision scope: shared current API commitments and conditional redirection of discovery/solver work for one task, not future provider evolution or user-defined identity.
- Evidence: [whole-pool sufficiency call](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L82-L103), [tool-cell current decision](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L499-L553), [global retry/refind loop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L985-L1082), [model sufficiency prompt](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/prompt_template.py#L294-L302).
- Basis: structural.
- Confidence: medium; observed source path, not a provider-backed run.
- Caveats: this is narrow task-wide current control, not continuous management of a portfolio or a separate independent metasystem. The `Unsure` response also passes the source's non-`Unsolvable` stop check; this weakens reliability, not the existence of the mapped decision right.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit of operational claims is supplied inside the assessed task-run organization.
- Disturbance / variety regulated: unsupported success reports, API hallucinations and incorrect solver answers could escape routine task checks.
- Decisive decision or feedback right: the LLM-based `check_task_solved` and ToolBench pass-rate evaluation are ordinary acceptance checks of the same task-run output, not a separately governed sporadic audit judgment.
- Decision owner: no distinct complementary auditor evidenced; the default result checker feeds the ordinary same-task retry controller.
- Supporting / enforcement mechanisms: `anytool/verifier.py`, `anytool/check_solved.py`, benchmark evaluator data, saved trajectories and result JSON.
- Closure path: unsuccessful ordinary verification can trigger pruning and renewed search; a separate independent audit-to-current-control return is not supplied.
- Why this is / is not agent-owned: a separately invoked GPT checker and repeated evaluation calls do not establish claim-relative independence or a complementary nonroutine control channel; ToolBench scoring alone does not donate S3* ownership.
- Evidence: [ordinary checker and majority](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/verifier.py#L104-L178), [checker in retry loop](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L1013-L1041), [benchmark description](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md#L104-L128).
- Basis: structural bounded absence.
- Confidence: medium-high within the declared runtime.
- Caveats: a separately operated external benchmark audit could exist, but is not packaged as this task-run's complementary auditor.

### Absence scope

- Surfaces inspected: task runner and refind, `anytool/verifier.py`, `anytool/check_solved.py`, ToolBench evaluator files, result persistence, and README experiment route.
- Plausible first-party paths checked: second model check, multi-sample pass-rate majority, solver trajectory inspection, ToolBench leaderboard evaluator and main-loop result retry.
- Why no material first-party path remains: these paths form task acceptance or adjacent research evaluation; none establishes a separately controlled, claim-relative independent complementary inspection whose findings return through distinct S3* corrective control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective scan of the external environment that produces adaptation options for the harness's future capabilities and returns them to current control.
- Disturbance / variety regulated: API availability and model/tool ecosystem evolution might outdate search choices or capability, but the runtime responds to individual current queries only.
- Decisive decision or feedback right: model agents may refind APIs following current failure, yet no path decides strategic changes to AnyTool's future repertoire or operating policy.
- Decision owner: task agent owns current-query search; developers/operators own software/configuration changes outside the assessed run.
- Supporting / enforcement mechanisms: query-time catalog search, failure reflection prompts, mutable API pool, ToolBench data preprocessing and benchmark scripts.
- Closure path: failure feedback returns to the current task's discovery loop, not an outside/future adaptation option returned to S3 and persisted in future operating capability.
- Why this is / is not agent-owned: self-reflection here adjusts a single task attempt, not prospective environment intelligence for the harness's continued viability.
- Evidence: [refind prompt](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/prompt_template.py#L175-L190), [task retry](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L985-L1082), [data preparation](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md#L49-L66).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: user or maintainers may update dependencies and datasets, but that adjacent developer activity does not supply in-boundary S4 closure.

### Absence scope

- Surfaces inspected: README setup, API database and retrieval, prompt templates, task-level history/retry, local JSON state and evaluator/benchmark generation.
- Plausible first-party paths checked: failed-API reflection, discovery of fresh API catalog entries, result history, benchmark data generation, runtime configuration and provider changes.
- Why no material first-party path remains: inspected mechanisms either search for present tasks, persist current outputs, or require external developer reconfiguration; no shipped loop turns prospective external distinctions into future capability options and returns those options to current control.

## S5 — Policy and identity

- State: —
- Function: no legitimate identity/ultimate-policy decision and returned governing closure inside the assessed task-run boundary.
- Disturbance / variety regulated: user purpose, provider credentials, allowed API access and cost constraints can require policy decisions, but the included runtime handles them as configuration or ordinary task constraints.
- Decisive decision or feedback right: credentials and resource limits are preset by operator/developer; no first-party issue path escalates a purpose/policy dispute to a legitimate authority and returns a binding identity choice.
- Decision owner: outside operator/developer selects configuration; neither the running agents nor a declared parent S5 loop is shown owning ultimate policy.
- Supporting / enforcement mechanisms: configuration example, token/API caps, solver function permissions, ordinary input and result checking.
- Closure path: static configuration constrains execution; no identity-level dispute -> ultimate authority -> authoritative decision -> return-to-operation sequence is shipped.
- Why this is / is not agent-owned: obeying preset constraints or refusing an individual query is task execution, not authority to define or adjudicate the organization's enduring identity.
- Evidence: [configuration boundary](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/README.md#L17-L27), [resource limits](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/scripts/main.py#L17-L31), [policy-like solvability checks](https://github.com/dyabel/AnyTool/blob/6202212ce45329282cf812ae48427f8765cf164c/anytool/prompt_template.py#L294-L310).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: maintainers have normal development authority outside this bounded deployed harness; no distributed organizational parent mode is inferred from repository ownership.

### Absence scope

- Surfaces inspected: setup/configuration, all three agent levels, prompt templates, API and token gates, solver/checker, README governance and task result artifacts.
- Plausible first-party paths checked: human configuration of model/API credentials, hard usage ceilings, task refusal/solvability model, user query changes, and maintainer changes to shipped code.
- Why no material first-party path remains: none accepts an identity/ultimate-policy matter, routes it to legitimate authority, and enforces a returned decision in the continuing task-run organization; the paths are ordinary external configuration or local task control.

## Recursion

The root, category and tool agents form a hierarchy of decomposed retrieval tasks, not independently viable recursive systems. There is no evidence that each spawned cell has its own enduring identity and complete metasystem; the shared pool, task completion and retry decisions remain at one task-run recursion.

## Variety and escalation

The task's variety is attenuated by category/tool partitioning, duplicate API guards and a size cap; API observations and checker reasons amplify the information available to subsequent model calls. Unsolvable or failed attempts are handled by bounded refind and may end without an answer. The `stop` flag is a shared current-task signal, not by itself an algedonic channel. No identity-level escalation or enduring external adaptation channel is evidenced.

## Evidence gaps

- No paid-provider E2E run: the source demonstrates wiring and decision-right reachability, not runtime success, stability or the independence of any separately deployed auditor.
- The shared pool has mixed locked and unguarded accesses; the S2 constructor claim is confined to the explicitly locked insertion path, without asserting race-free coordination.
- No separate operator/supervisory mode for S3, S4 or S5 was documented. These negative states are relative to the inspected standard distribution, not claims about hypothetical extensions.
