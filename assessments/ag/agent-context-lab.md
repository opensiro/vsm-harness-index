---
harness_id: agent-context-lab
project_name: Agent Context Lab
repository: https://github.com/Qin-sor/agent-context-lab
review_ref: 372ecc514d48d8e1e5f92d672a9c2b16f4826b5d
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Context Lab

## Review boundary

- System in focus: Open-source minimal coding-task agent harness with a model/tool feedback loop, optional in-task history summarization/tool-result clearing and optional external-evidence default-FAIL completion gate; the published standalone experiment runners supply examples and first-party invocation of the harness.
- Purpose and identity: Research how one model-guided coding task retains hard constraints under context pressure and whether observable evidence can block false done claims. Its operational output is a coding-task artifact in a bounded workspace, plus optional offline experimental measurement.
- Relevant environment: Python 3 standard library, CLI matrix scripts and predefined coding task scenarios, optional OpenAI-compatible model API (DeepSeek or supplied model), host filesystem and subprocess runner, external API key and human experiment author. No cross-agent deployment, distributed scheduler or institutional executive assumed.
- Standard-distribution boundary: `harness.agent.run_task`, `harness.llm.OpenAICompatLLM`, `harness.tools.Workspace` and `execute`, `harness.context.ContextManager`, optional `harness.verifier.DefaultFailVerifier`, reachable via shipped `run_experiment.py` and `run_verifier_experiment.py`. Deterministic `MockLLM` is test-mode implementation, not an autonomous actor.
- Credited operating / distribution surfaces: [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/llm.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/llm.py); [`harness/tools.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/tools.py); [`harness/context.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/context.py); [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py). The supported source imports wire the optional verifier at done, and tool history to the next model call.
- Adjacent first-party surfaces excluded from ownership: [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py) predefined benchmark fixtures and independent task truth/evidence (may corroborate verifier); [`test_verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/test_verifier.py) upstream testing; `results/` stored past experiment data and claims; [`run_cache_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_cache_experiment.py) cache experiment and analysis; maintainer's GitHub/README research process; hidden task truth `_ground_truth_ok` used only for offline statistics; external provider reasoning internals, human operational supervision or imagined organization. No repo-level LICENSE metadata was published in preflight; source inspection is not a declaration of reuse rights.
- First-party operating / deployment modes considered: CLI with external OpenAI-compatible model and five local tools; full/compact/compact_clear context strategies; optional constraint-aware-summary configuration; optional default-FAIL verifier with max_rejects, false-done handling, mock test runs. No first-party continuously running deployed multi-agent control plane.
- Recursion level: One configured coding task with one model-controlled operator and deterministic environmental guards, followed by optional offline experiment analysis. Parallel experimental matrix runs are independent test cases, not live viable S1 departments.
- Reviewed revision: `Qin-sor/agent-context-lab@372ecc514d48d8e1e5f92d672a9c2b16f4826b5d`; GitHub immutable ID `1309065410`, Git tree `ade2c04a3b94c91cb179d201f9358e46144d474b`, public nonfork, nonarchived, GitHub API did not supply license metadata; frozen on 2026-10-20.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`harness.agent.run_task` prepares one coding task and its filesystem workspace, creates a conversation and iterates calling `llm.chat(history, tools=TOOL_SCHEMAS)`. Tool calls are dispatched through `harness.tools.execute`; this supports listing and reading files, editing files, and invoking Python on task work products. It appends structured results back to conversation history. A done call is deferred until other same-turn tools execute; repeated done calls return paired responses. A non-tool streak or configured step budget terminates a stuck run. The live `OpenAICompatLLM` makes an HTTP request to configured OpenAI-compatible endpoint with tool schema and returns model tool calls; the `MockLLM` simply replays a deterministic benchmark plan. [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/llm.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/llm.py); [`harness/tools.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/tools.py).

`ContextManager` optionally estimates token size and compresses earlier conversation text through a model summary, or clears older tool messages before summary. A fixed strategy is chosen per run by caller rather than updated based on later organizational intelligence. Constraint text survival probes are an experiment measurement surface, while task artifact/constraint checks at end provide task-specific behavior metrics. `run_experiment.py` compares strategies, saves run details and summaries; these are research outputs, not automatically imported into a running agent's governing future strategy. [`harness/context.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/context.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py); [`run_cache_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_cache_experiment.py).

The optional `DefaultFailVerifier` is notably more than model self-reporting: at the done boundary, independently specified evidence check callbacks read current workspace artifacts and tool logs, without access to task hidden truth. The report either permits one task's completion or returns a precise missing-evidence message as the done tool result so that the **same** model can attempt repair, limited by max_rejects. Evidence classes A/B/C/D label missing artifacts, incorrect content, missing procedure and unauthorized side effects. This is strong operational verification, yet there is no independent current-management S3 to receive, adjudicate and return an S3* systemic audit correction. The paper/README's numerical real DeepSeek performance claims were not reproduced. [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py); [`test_verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/test_verifier.py).

## Operational model

A caller chooses benchmark task, backend/model and a preset context handling mode; the configured language model makes discretionary local coding tool choices within one bounded task. Workspace guard, context compression and optional external verifier are functional support; none automatically becomes an independent organizational management tier. The harness ends at reported task completion/rejection or exhaustion; the experiment runner separately checks task truth and aggregates evidence for later human analysis.

## S1 — Operations

- State: A
- Function: Model-guided execution of one coding task, selecting permitted filesystem/compute tools from feedback until a claimed completion or bounded failure.
- Disturbance / variety regulated: User-specified coding outputs, constraint-preservation difficulty, tool errors and result truncation, incomplete workspace information, context-size limits, generated-code execution errors, and premature done claims.
- Decisive decision or feedback right: The configured OpenAI-compatible language model picks the next tool and tool arguments in each loop iteration; the first-party harness dispatches list_dir/read_file/write_file/run_python, observes result, and repeats. It can decide to claim done; optional verifier gates acceptance based on independent checks.
- Decision owner: Externally supplied model supplies discretionary task action selection. Caller supplies the task, constraints, backend, strategy, and optional verifier; Python runner dispatches, truncates, tracks and stops according to deterministic conditions.
- Supporting / enforcement mechanisms: run_task task.prepare/history, llm.chat(...tools=TOOL_SCHEMAS), Workspace.execute and tool_log, ContextManager.prepare, bounded max_steps and stuck breaker, done acceptance/reject logic, OpenAICompatLLM.chat live-provider adapter.
- Closure path: Task prompt and constraint list → model-directed tool calls → first-party workspace execution → tool result in next model context → model next choice/done → optional verifier check and evidence gap returned on failure. On successful unblocked done, finished=True; if rejected, agent gets concrete gap feedback to change current operations.
- Boundary reachability: The shipped run_experiment.py and run_verifier_experiment.py instantiate real provider-capable OpenAICompatLLM and call harness.agent.run_task; five defined tools directly operate on workspace. MockLLM is an optional separate test mode and is not credited as model autonomy. The optional verifier is wired to the same running agent at the done boundary.
- Why this is / is not agent-owned: Without model-driven decisions, the deterministic scaffolding can replay a MockLLM plan but cannot determine new task-dependent tools/arguments from changing workspace observations. The integrated code supplies a live model feedback loop when configured.
- Evidence: [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/llm.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/llm.py); [`harness/tools.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/tools.py); [`harness/context.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/context.py); [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py).
- Basis: Explicit first-party code and supported CLI wiring, with upstream verifier tests; no independent empirical claims about model task success.
- Confidence: High for S1 model-discretion and tool/result feedback at this bounded runtime.
- Caveats: No live external provider/API run performed for this assessment; the repository's historical DeepSeek datasets/claims are not freshly reproduced. Tools allow running arbitrary Python inside a path-constrained subprocess that is not an actual security sandbox.

## S2 — Coordination

- State: —
- Function: No distinct continuing S1 departments and feedback relationship attenuating inter-S1 disruption at the one-task harness/experiment boundary.
- Disturbance / variety regulated: Individual tools may be invoked in a batch, constraint checks may reject done, and alternative strategies can run comparable tasks independently.
- Decisive decision or feedback right: The loop serially dispatches model-produced calls and defers done to after normal tool calls; experiment runner iterates across independent task/strategy matrices. No inter-unit conflict-coordination judgment exists.
- Decision owner: Single task's model and deterministic control-flow; no second coordinating decision owner over viable operational S1 units.
- Supporting / enforcement mechanisms: Sequential tool execution, done-last handling, explicit call/result matching, task matrix scheduling and multiple independent experimental runs.
- Closure path: Each tool result returns to its own task model; experimental results are aggregated offline for comparison. Neither causes interdepartmental commitment adjustment/feedback.
- Why this is / is not agent-owned: Independent experiment cases are not distinct operational departments that compete or oscillate under shared resource commitments; a one-loop tool batch does not confer S2.
- Evidence: [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/tools.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/tools.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py).
- Basis: Bounded negative from shipped supported main runner and experiment orchestration.
- Confidence: High.
- Caveats: An external service orchestrating multiple deployed copies could instantiate genuine multi-S1 coordination outside this repository's shipped boundary.

### Absence scope

- Surfaces inspected: Model/tool loops, task/strategy CLI matrix, done-last call handling and tool history tracking.
- Plausible first-party paths checked: Simultaneous tool calls, independently scored experiment cases and shared context/constraints as possible inter-S1 conflict resolution.
- Why no material first-party path remains: Only one viable task-operating agent exists at the supported boundary; tools and repeated experiment cases are task-local mechanisms, not distinct self-maintaining business units with evidenced mutual interference and corrective inter-unit feedback.

## S3 — Inside-and-now control

- State: —
- Function: No independent S3 portfolio owner regulating current total operation of several viable S1 units through collective resource/commitment decisions.
- Disturbance / variety regulated: One coding task can exceed max_steps, emit no tool calls, call done prematurely, or violate file constraints; test suites may reveal incomplete result.
- Decisive decision or feedback right: Runner enforces fixed max_steps, no-tool break, and max_rejects; optional verifier directly vetoes one task's completion and returns required fixes to same S1 actor. No management actor owns current strategy for a portfolio of separately viable operational units.
- Decision owner: Deterministic Python harness and evidence-check callbacks supplied by task authors; the experiment developer sets resources, strategy, budgets and success tests externally.
- Supporting / enforcement mechanisms: task.prepare; verifier.verify(ws); fixed execution budget, call logging, constraint evaluations, context compaction, run/condition selection CLI.
- Closure path: Current task attempt → model actions → rule-based evidence pass/fail → current task continuation or stop; no overall-management view → discretionary binding decision → differentiated operating units and returned accountability.
- Why this is / is not agent-owned: The verifier's acceptance gate is a task-specific guard and is not an independent inside-and-now manager; the runner aggregates benchmark results for offline research, but it does not operate a managed portfolio of viable S1 departments.
- Evidence: [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py); [`harness/context.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/context.py).
- Basis: Bounded negative after testing current-run supervision, budget and distinct parent modes.
- Confidence: High.
- Caveats: External task designer or supervising operator could make S3-like decisions at a larger system boundary; no first-party closed managerial parent path in this published code.

### Absence scope

- Surfaces inspected: Verifier's done gate, model loop budgets, experiment runner condition assignment, per-task hard constraints and policy-like workspace restrictions.
- Plausible first-party paths checked: Task-level controller or an external human experimenter's strategy choice as current management; potential parent decision to reject an agent's done.
- Why no material first-party path remains: There is no aggregate current view or autonomous/parent-governed discretionary allocation across multiple viable S1 units; fixed model iteration and local completion admission cannot close S3 at this recursion.

## S3* — Complementary audit

- State: —
- Function: Task-completion verification against independently observable local artifacts exists, but no complementary audit of S3's ordinary operating reporting with independent corrective return to S3.
- Disturbance / variety regulated: A model can falsely declare done, omit artifacts, compute an incorrect value, skip required testing or produce forbidden workspace side effects.
- Decisive decision or feedback right: DefaultFailVerifier checks a task's evidence checklist against current workspace and tool_log, independently of the model's done assertion or hidden experiment ground truth; its pass/fail can reject completion and return a missing-evidence explanation. That is per-S1 work-product acceptance, not a separately evidenced S3* audit of an operational system's management reports.
- Decision owner: Task author/configuration supplies Evidence checks, deterministic verifier executes them; no independently commissioned audit owner with access to live work beyond task-specific workspace; no separate S3 authority receiving and adjudicating systemic findings.
- Supporting / enforcement mechanisms: Evidence(eid,gap_class,check), verifier.verify(ws) default FAIL, reject_message(), agent.run_task's done handler, separately measured _ground_truth_ok in experiment (not visible to verifier).
- Closure path: One agent's done claim → workspace/evidence test → reject result directly returned to the same agent as one tool message → agent retries or stops. No audit of distinct management's current-state account → independent report → S3 binding corrective decision → changed multiple S1 current conduct.
- Why this is / is not agent-owned: The checker is independent **of a worker's claim** and uses direct evidence, an important factual distinction from mere self-verification; however it lacks the organizational independence/management challenge and S3 decision-return required for VSM S3*. Its tests and negative/positive labels should not be mistaken for a managerial audit office.
- Evidence: [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py); [`run_verifier_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_verifier_experiment.py); [`test_verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/test_verifier.py).
- Basis: Explicit direct-evidence verification wiring; bounded negative specifically for the missing organizational S3* relation, not for the useful task-level verifier.
- Confidence: Medium-high.
- Caveats: At a different deployed multi-S1 system boundary, a first-party supervisor could use this verifier as one evidence component, but that larger arrangement and returned managerial corrective path are not shipped here.

### Absence scope

- Surfaces inspected: DefaultFailVerifier and observable evidence callbacks; tool log, independent workspace recalculation/test rerun; run_task done rejection; hidden truth metric separation.
- Plausible first-party paths checked: Real independently checked workspace evidence, false-done interception and bounded worker retry are the strongest first-party S3* candidates. Tested whether an independent S3 management report, complementary operational reality path and managerial corrective owner are present.
- Why no material first-party path remains: The verifier audits task delivery and returns tool feedback directly to the same S1 model, not independent management S3. No management-state claim is challenged by a separately authorized S3* with returned organization-level S3 decision or accountable downstream collective correction. This negative is function-specific, not a denial of task-verification independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: No agent-owned prospective external intelligence and accepted adaptation of subsequent organization's long-term capability; context compaction is within-run history management.
- Disturbance / variety regulated: Long input/output histories create token pressure, loss of original constraints and possible false completion; provider token cache and experimental context strategies affect local run cost.
- Decisive decision or feedback right: ContextManager switches among host-selected full/compact/compact_clear strategy, may ask LLM to summarize old conversation, and clears old tool results. Experiment scripts compare static chosen settings and write reports; they do not autonomously accept research results as a new governing policy for future agent capability.
- Decision owner: Configuration/experiment author externally chooses strategy, budget, keep_recent and constraint_aware_summary; runtime deterministic thresholds trigger current context transform; the model that summarizes text does not decide future strategic adoption.
- Supporting / enforcement mechanisms: ContextManager.prepare/summary prompt; before/after survival probes; CLI experiment matrix and offline results/markdown; separate cache experiment.
- Closure path: Within one task, prompt history → estimated-budget threshold → current messages shortened → same model task loop continues; across experimental runs, statistics are saved for human study, with no shipped result-driven policy-update feedback.
- Why this is / is not agent-owned: LLM-based summary generation is not itself an adaptive organizational strategy owner. Even the optional constraint-aware prompt is an upstream authored alternative evaluated by an experiment, not a function that deploys future methods to subsequent runs based on external intelligence.
- Evidence: [`harness/context.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/context.py); [`harness/llm.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/llm.py); [`run_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_experiment.py); [`run_cache_experiment.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/run_cache_experiment.py); [`README.md`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/README.md); [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py).
- Basis: Bounded negative after checking both in-task compression and optional experiment/result feedback into subsequent deployment.
- Confidence: High.
- Caveats: A researcher reading reported findings may later modify this project, but that human R&D process is not a shipped first-party S4 parent-governed mode.

### Absence scope

- Surfaces inspected: Context compaction/clearing, LLM summary instructions, constraint-aware prompt toggle, experiment strategy matrix and saved comparison reports.
- Plausible first-party paths checked: LLM summary and observed constraint-loss measurements as learning/adaptation candidates; cache experiments as prospect of future capability tuning.
- Why no material first-party path remains: Supported loops affect the *ongoing request* using externally selected static strategies. Offline experiment summaries do not enter a first-party autonomous future-option evaluation/acceptance and feedback that changes subsequent operational capabilities.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/purpose policy-making authority with a returned constitutional decision governing multiple operating units.
- Disturbance / variety regulated: Tasks include prohibitions on file modification and mandatory audit/test actions; coding side effects and improper done claims threaten task-level acceptability.
- Decisive decision or feedback right: Task templates contain fixed hard constraints; workspace path and subprocess environment restrictions and verifier check lists apply predefined local permissions. User/experiment author fixes identity, task and criteria outside the agent.
- Decision owner: External experimenter/maintainer writes benchmark tasks, evidence and system prompt, not a VSM S5 actor inside the one-task runtime.
- Supporting / enforcement mechanisms: SYSTEM_PROMPT, task.constraint/evidence() lists, Workspace.resolve path confinement, run_python trimmed environment, verifier default-fail gate and CLI settings.
- Closure path: Static task/policy configuration → tool calls admitted/rejected according to task rules; no question of organizational ultimate purpose → independent legitimate owner decision → binding system identity/charter change returned to S1–S4.
- Why this is / is not agent-owned: User-provided local constraints are not an internally owned identity-level function; default-fail does not change authority hierarchy and a developer's patch to a summary prompt is not an S5 policy decision.
- Evidence: [`harness/agent.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/agent.py); [`harness/tools.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/tools.py); [`harness/verifier.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/harness/verifier.py); [`tasks.py`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/tasks.py); [`README.md`](https://github.com/Qin-sor/agent-context-lab/blob/372ecc514d48d8e1e5f92d672a9c2b16f4826b5d/README.md).
- Basis: Bounded absence of S5 at released harness/task deployment boundary.
- Confidence: High.
- Caveats: Repository maintainer governance and downstream business/operator oversight are deliberately excluded; an optional human parent cannot be assumed to have an implemented policy-return mandate.

### Absence scope

- Surfaces inspected: System prompt and hard constraint list, task evidence definitions, path-enforcement and capped runtime, experiment configuration and project maintainer source.
- Plausible first-party paths checked: Local user/developer-defined policies, automatic veto of false done claims and task instructions as alleged high-level constitutional mandates.
- Why no material first-party path remains: No first-party ultimate organizational purpose/identity decision owner or returned binding system policy exists; local work rules and externally edited task definitions do not implement S5=P or S5=A.


## Recursion

One S1 coding agent under a predefined task and supplied model. The verifier is a functionally independent evidence admission helper **within that S1 work loop**, and test-case replication is experimental methodology rather than a live second organizational recursion. The externally chosen context strategy and benchmarks cannot be silently promoted into S4 strategic adaptation. Claims about higher human governance or workgroup communication require another deployed boundary.

## Variety and escalation

Unexpected workspace content, tool errors, context budget exhaustion, missing required artifacts or test omission disturb coding. The model can change local tool plans in response. The context manager may discard or summarize historical messages; the task verifier can flag evidence gaps, which the model receives as actionable same-task feedback. Consecutive non-tool turns, attempt limits or check failure end a run. These signals operate inside the task, not as demonstrated organizational algedonic feedback to S3/S5.

## Evidence gaps

- Repository source and tests were read at a pinned public commit; this review did not rerun the historical DeepSeek paid-API experiments or infer their performance from README tables.
- Upstream `test_verifier.py` (non-provider, deterministic) ran locally: **11 checks passed, zero failed**; Python compileall on harness/scripts passed. They support current verifier code behavior, not VSM S3* status or broad coding reliability.
- `run_python` workspace path restrictions and trimmed process environment are not resource/network isolation; this is not an endorsement of production sandbox safety.
- No separate viable S1 departments or standing parent mandate were found in shipped code. A user may build a managed multi-agent application using these components, but its organizational functions are outside this source-bound artifact.
