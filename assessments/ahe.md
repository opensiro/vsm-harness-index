---
harness_id: ahe
project_name: Agentic Harness Engineering
repository: https://github.com/china-qijizhifeng/agentic-harness-engineering
review_ref: 8b2a55d97590363fe50c3cc6b5e833b020a4bb4c
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Agentic Harness Engineering

## Review boundary

- System in focus: the first-party `china-qijizhifeng/agentic-harness-engineering` automated evolution system at frozen revision `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`, including the shipped coding agent, `evolve.py` orchestration loop, Evolve Agent, bundled Agent Debugger integration, Explore Agent, workspace/change-attribution machinery, and supported Best-of-N mode where they bear on organizational ownership.
- Purpose and identity: improve a coding-agent harness around a fixed base model by repeatedly evaluating real task performance, analyzing traces and verifier evidence, researching relevant external techniques, and applying evidence-backed changes to prompts, tools, middleware, skills, sub-agents and memory.
- Relevant environment: benchmark software tasks and repositories; E2B/Harbor execution outcomes; external verifier tests and rewards; coding-agent trajectories; source repositories and web documentation/research; evolving workspace state; historical iteration scores and regressions.
- Standard-distribution boundary: installable repository code, shipped agent/config/prompt assets, bundled Agent Debugger source/integration, Explore Agent, and first-party orchestration are inside. Harbor/E2B, model-provider inference, benchmark task definitions/verifiers, remote source repositories and web pages are external environment/dependencies; they can supply evidence to first-party decision paths but are not silently credited as AHE decision owners.
- Credited operating / distribution surfaces: `evolve.py`; `agents/code_agent_simple`; `agents/evolve_agent`; bundled `agent-debugger-cli` source and the `adb ask` integration; `agents/explore_agent`; default `configs/base.yaml`; workspace snapshots/change manifests/change evaluation; supported Best-of-N variant generation/evaluation/selection.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/development files; documentation-only reference examples; notification plumbing; post-evolve validation when disabled; generic tracing, thread locks and progress bookkeeping where they do not own an organizational decision.
- First-party operating / deployment modes considered: default iterative evaluate → analyze → evolve mode with Explore Agent and Agent Debugger enabled; ordinary single-evolution-agent mode; supported optional Best-of-N parallel variant mode; resume/recovery behavior; post-evolve validation as an optional adjacent mode.
- Recursion level: one AHE harness-evolution organization. Coding-agent task executions are operational S1 activity; the Debugger is a complementary audit path over those operations; the Evolve/Explore path adapts the coding harness used by subsequent operations. Alternative Best-of-N worktrees are candidate adaptations at this recursion, not silently treated as cooperating operational S1 units.
- Reviewed revision: `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AHE ships a complete iterative harness-development loop rather than only a benchmark wrapper. Its coding agent uses a configured LLM plus shell access to inspect repositories, edit files and run builds/tests. `evolve.py` evaluates that harness with Harbor, computes pass/fail statistics and cross-iteration flips, invokes Agent Debugger over trajectories and external verifier output, and gives the resulting evidence to a separate Evolve Agent that can edit the harness workspace. The next iteration runs the changed harness again, making prior adaptation outcomes observable and attributable.

The default distribution also enables an Explore Agent. At experiment start, source and web sub-agents inspect the pinned NexAU implementation plus external coding-agent architecture sources, write distilled skill files, and register those skills into the Evolve Agent. The web path explicitly searches for current state-of-the-art architectures, benchmarks, tools and ablations. This gives the adaptation loop a prospective external-sensing path beyond retrospective benchmark failures.

Agent Debugger is organizationally distinct from routine evaluation. AHE collects the coding agent's raw traces, external verifier reward and verifier test output, then runs `adb ask` with its own QA-agent configuration. The code explicitly describes verifier output as evidence from an external evaluator that the coding agent never sees. Debugger output is written as analysis, injected into the Evolve Agent's query, and can therefore alter the harness used by subsequent operational trials. The Debugger does not itself edit the coding workspace in this path.

Best-of-N is a supported optional evolution mode: multiple Evolve Agents work in isolated git worktrees, each variant is benchmarked, and deterministic selection adopts the variant with the best measured pass rate (with exception-count tie breaking). This is evidence-backed adaptation selection. It is not credited as S2 because the candidate variants are isolated alternatives rather than mutually interfering operational units, and it is not credited as S3 because the selection changes the future harness configuration rather than regulating live current task commitments.

Primary evidence:

- [`README.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/README.md)
- [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml)
- [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py)
- [`agents/code_agent_simple/code_agent.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/code_agent_simple/code_agent.yaml)
- [`agents/code_agent_simple/systemprompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/code_agent_simple/systemprompt.md)
- [`agents/evolve_agent/evolve_prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/evolve_prompt.md)
- [`agents/explore_agent/run.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/explore_agent/run.py)
- [`agents/explore_agent/source_agent/prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/explore_agent/source_agent/prompt.md)
- [`agents/explore_agent/web_agent/prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/explore_agent/web_agent/prompt.md)
- [`agents/evolve_agent/skills/agent-debugger-cli/_source/`](https://github.com/china-qijizhifeng/agentic-harness-engineering/tree/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/skills/agent-debugger-cli/_source)

## Operational model

The operational coding harness receives a software task, lets its LLM inspect/edit/test the target repository through `run_shell_command`, and returns the resulting task state to the benchmark environment. AHE records the trajectory and verifier result for each rollout.

After evaluation, AHE computes task-level outcomes, regressions and change attribution. The enabled Agent Debugger separately reconciles raw trajectories with verifier evidence and produces root-cause analysis. The Evolve Agent receives evaluation statistics, historical trends, attribution and debugger findings, then autonomously chooses targeted edits inside the workspace. The next iteration evaluates the modified harness. In parallel with the first evaluation, the enabled Explore Agent researches framework internals and current external coding-agent techniques and registers its distilled skills into the Evolve Agent.

This produces two different higher-order loops: complementary audit (`S3*`) over operational evidence and prospective harness adaptation (`S4`). The assessment does not collapse them into S3 merely because the outer loop is called an orchestrator or because it tracks scores.

## S1 — Operations

- State: A
- Function: solve environment-facing software tasks by inspecting a target repository, choosing shell-based edits/tests/actions, and iterating from tool results until the task is completed.
- Disturbance / variety regulated: heterogeneous software tasks, repository state, compiler/test failures, command output, file contents, runtime errors and task-specific implementation constraints.
- Decisive decision or feedback right: choose the substantive next repository inspection, edit, build or test action from the live task/tool context.
- Decision owner: the configured coding-agent LLM in `agents/code_agent_simple`, invoked through the shipped NexAU agent loop.
- Supporting / enforcement mechanisms: `run_shell_command`; NexAU execution loop; E2B/Harbor task environment; in-memory tracing; model/provider configuration; iteration limits.
- Closure path: benchmark task/repository state enters coding agent → model selects shell action → command changes or inspects the task environment → output/test result returns to the model → subsequent action adapts until completion/termination → external verifier evaluates the resulting task state.
- Boundary reachability: this coding-agent loop is the default operational harness evaluated and evolved by AHE, not a repository-development-only helper.
- Why this is / is not agent-owned: removing the model actor leaves shell and benchmark machinery but removes the open-ended selection of implementation/debugging actions.
- Evidence: [`code_agent.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/code_agent_simple/code_agent.yaml); [`systemprompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/code_agent_simple/systemprompt.md); [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Harbor/E2B and model inference are external dependencies; AHE deliberately wires the model actor into the first-party coding harness and closes tool results back into that actor.

## S2 — Coordination

- State: —
- Function: no material first-party S2 loop was established that attenuates a concrete interference/conflict/oscillation between distinct operational S1 units at the selected recursion.
- Disturbance / variety regulated: AHE can run many benchmark rollouts and optional evolution variants concurrently, but the reviewed distribution does not establish a shared operational disturbance among them that is sensed and attenuated as S2.
- Decisive decision or feedback right: not established for S2 at this recursion.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: Harbor concurrency; thread pools; progress/tracer locks; git worktrees for Best-of-N variants; deterministic winner selection; task/variant result aggregation.
- Closure path: no S2-specific closure established. Parallel benchmark trials are independent evaluations, while Best-of-N worktrees deliberately isolate candidate adaptations and later select one; neither path demonstrates coordination feedback that changes distinct S1 units to attenuate an inter-S1 disturbance.
- Why this is / is not agent-owned: concurrency and isolation are runtime/experiment support; no autonomous or constructor-owned S2 decision is needed because the required S2 disturbance/coordination relation is not established.
- Evidence: [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py); [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: generated/evolved harnesses may themselves contain multi-agent coordination; those later candidate designs are not automatically part of AHE's own frozen organizational closure.

### Absence scope

- Surfaces inspected: main evolution loop; Harbor concurrency; Best-of-N worktree creation/evaluation/selection; thread/progress/tracer locking; coding-agent and Evolve-Agent configurations; Explore-Agent parallelism; bundled skills/middleware searches for shared-resource conflict and coordination.
- Plausible first-party paths checked: concurrent coding-agent rollouts as S1 peers; parallel Explore sub-agents; Best-of-N evolution variants; git-worktree isolation; locks around tracer/progress state; variant winner selection.
- Why no material first-party path remains: reviewed parallel actors either work on isolated alternatives, independent benchmark trials or separate research outputs. Locks protect implementation bookkeeping, and winner selection is adaptation choice after evaluation. No path documents or structurally establishes an inter-S1 interference plus attenuation plus feedback into the affected S1 operations.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control loop was established that observes live operational commitments/resources/priorities and makes bounded present-time interventions across the selected organization.
- Disturbance / variety regulated: the orchestrator observes evaluation status, scores, timeouts and historical regressions, but its consequential changes are primarily future harness adaptations rather than regulation of live coding-task commitments.
- Decisive decision or feedback right: not established for S3. Target pass rate, maximum iterations, concurrency and timeouts are configured thresholds/enforcement rather than a discretionary whole-current decision right.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: iteration loop; current pass-rate/statistics; task stability; experiment/job timeouts; configured concurrency; best-ever bookkeeping; notifications; Best-of-N result selection.
- Closure path: no S3-specific closure established. Evaluation evidence flows into Debugger/Evolve analysis and then into changes to the next harness capability; that path is credited under S3*/S4. Timeout/termination and target-threshold checks enforce predefined rules rather than making an open current-control allocation/commitment judgment.
- Why this is / is not agent-owned: the Evolve Agent owns adaptation choices, not a distinct current-control function over live operational commitments. Deterministic orchestration supplies execution support but does not close S3 under the Profile's whole-current test.
- Evidence: [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py); [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml); [`evolve_prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/evolve_prompt.md).
- Basis: explicit + structural negative finding.
- Confidence: medium-high.
- Caveats: if a future AHE mode gives an agent authority to reallocate or preempt live task resources/commitments from a whole-system current view, that would warrant reassessment; no such frozen first-party closure was found here.

### Absence scope

- Surfaces inspected: `run_single_experiment`; evaluation/statistics/timeout handling; task stability and diff logic; best-ever tracking; Best-of-N selection/merge; resume rollback; notifications; Evolve-Agent prompt and available tools/middleware.
- Plausible first-party paths checked: orchestrator as manager; target pass-rate gate; experiment/job timeout enforcement; Best-of-N winner selection; best-ever/rollback machinery; Evolve Agent reacting to regressions; configured Harbor concurrency.
- Why no material first-party path remains: the open-ended agent decision path changes the harness for subsequent operations and therefore closes adaptation, not present-time operational regulation. Remaining present-time controls are fixed thresholds, lifecycle/recovery or experiment bookkeeping without a separate whole-current discretionary owner.

## S3* — Complementary audit

- State: A
- Function: independently reconcile coding-agent operational trajectories with external verifier evidence, diagnose root cause beyond ordinary pass/fail reporting, and return those findings into the evolution decision path.
- Disturbance / variety regulated: superficial task outcomes or the coding agent's own trajectory may not reveal why a task failed, timed out or regressed; an independent evidence path is needed to distinguish agent behavior from verifier-grounded failure reality.
- Decisive decision or feedback right: judge the likely root cause and salient failure mechanism from raw traces plus verifier evidence, producing an audit finding used by the subsequent harness-change decision.
- Decision owner: the Agent Debugger QA LLM invoked through bundled `adb ask`; it is a separate analysis actor from the audited coding-agent LLM path.
- Supporting / enforcement mechanisms: bundled Agent Debugger source; per-task trace collection; external verifier reward/test-output collection; separate debugger LLM configuration; analysis overview/detail artifacts; query injection into Evolve Agent.
- Closure path: coding agent executes task → Harbor/verifier produces reward/test output and trace is persisted → Agent Debugger independently reads raw trace plus verifier evidence → debugger produces root-cause analysis → `adb_overview` is injected into the Evolve Agent query → Evolve Agent uses the finding to choose workspace changes → subsequent coding-agent operations run the changed harness.
- Boundary reachability: `agent_debugger.enabled: true` in the shipped base configuration, bundled source can be installed automatically when `adb` is absent, and `run_single_experiment` directly invokes the analysis before evolution.
- Claim being audited: the operational account implicit in the coding-agent trajectory and ordinary benchmark outcome — whether/why the performed behavior actually satisfies the task, times out, or causes a verifier-grounded failure/regression.
- Ordinary reporting path: Harbor statistics expose pass/fail/exception/reward and AHE records the coding-agent trace; these results alone feed iteration statistics and history.
- Complementary access path: Agent Debugger receives the raw/cleaned coding-agent trace together with `verifier/test-stdout.txt` and reward evidence; AHE explicitly notes that this external verifier output is produced after the agent finishes and is never seen by the coding agent.
- Independence boundary: the Debugger runs as a separate QA-agent process/configuration over persisted evidence and writes analysis artifacts, not the audited coding workspace. Its evidence access includes external verifier output unavailable to the S1 actor; the Evolve Agent remains the separate actor that can modify the harness after receiving the finding.
- Who acts on findings: the Evolve Agent; AHE inserts Debugger analysis into section 4 of the evolution query, after which the Evolve Agent selects and applies evidence-backed harness edits used by later trials.
- Why this is / is not agent-owned: removing the Debugger LLM leaves raw traces and verifier outputs but removes the open-ended root-cause judgment. The deterministic code only assembles evidence and routes the finding; the audit judgment is model-owned.
- Evidence: [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py); [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml); [`agent-debugger-cli/_source`](https://github.com/china-qijizhifeng/agentic-harness-engineering/tree/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/skills/agent-debugger-cli/_source).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external verifier logic itself is not credited as AHE S3* ownership; the credited audit is AHE's distinct Debugger judgment over trace plus verifier-ground-truth evidence and its wired return to the Evolve Agent.

## S4 — Intelligence / adaptation

- State: A
- Function: sense external performance and current/future-relevant harness techniques, generate adaptation options, and autonomously install persistent harness changes that alter capability in later coding operations.
- Disturbance / variety regulated: benchmark failures/regressions, unstable task behavior, ineffective prior changes, evolving framework internals, and newly observed coding-agent architectures/tools/ablations can make the current harness inadequate for future tasks.
- Decisive decision or feedback right: choose which prompt/tool/middleware/skill/sub-agent/memory changes to make, retain, revise or roll back based on evaluation, debugger, historical and research evidence.
- Decision owner: the Evolve Agent LLM for substantive adaptation choices; Explore-Agent LLMs autonomously produce external/source knowledge used as adaptation evidence. Optional Best-of-N selection deterministically chooses among already agent-generated variants by measured performance.
- Supporting / enforcement mechanisms: evaluation statistics and task flips; `change_evaluation.json`; best-ever/history data; Agent Debugger findings; Explore Agent web/source research; registered research skills; writable evolution workspace; git commits/tags/worktrees; subsequent Harbor evaluation.
- Closure path: current harness runs external benchmark tasks → AHE records performance/traces and Debugger findings while Explore Agent gathers source/web evidence → Evolve Agent synthesizes this evidence into concrete harness edits → first-party tools write those edits into the persistent workspace → next iteration executes the changed coding harness → new outcomes validate, revise or trigger rollback/pivot decisions.
- Boundary reachability: Explore Agent and Agent Debugger are enabled in the default base configuration; the Evolve Agent and persistent workspace mutation are the core documented `evaluate → analyze → improve` loop.
- External distinction: external benchmark/verifier outcomes expose task failures and regressions, while the enabled Explore Agent reads remote framework source plus current external coding-agent architecture/benchmark/web sources.
- Future / prospective distinction: Explore Agent is instructed to search recent state-of-the-art designs and ablations for implementable techniques; cross-iteration change evaluation, stability and regression evidence also distinguish which adaptations are likely to improve rather than damage later task capability.
- Adaptation option generated: the Evolve Agent may create or modify system prompts, tool descriptions/implementations, middleware, skills, sub-agents and long-term memory, and may choose rollback/pivot when prior changes are harmful or ineffective.
- Path back into current capability / S3: chosen edits are written into AHE's persistent `workspace`, committed/tagged, and that workspace becomes the coding-agent harness evaluated on the next iteration. Thus the prospective decision changes the capability currently available to later S1 operations even though no separate S3 loop is credited.
- Why this is / is not agent-owned: the orchestrator supplies evidence and writable boundaries, but the Evolve Agent makes the open-ended semantic choice of what capability change to implement. Removing that model actor leaves metrics and files but not materially the same adaptation decision.
- Evidence: [`README.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/README.md); [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py); [`evolve_prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/evolve_prompt.md); [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml); [`explore_agent/run.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/explore_agent/run.py); [`web_agent/prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/explore_agent/web_agent/prompt.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external benchmark, web and source systems provide evidence rather than owning AHE's adaptation decision. Best-of-N is optional and not required for the S4 result; the ordinary default evolution loop already closes adaptation.

## S5 — Identity / ultimate policy

- State: —
- Function: no runtime identity/ultimate-policy decision loop with legitimate ultimate authority and return-to-operation closure was established at the assessed recursion.
- Disturbance / variety regulated: AHE has an explicit pass@1 optimization objective, protected prompt rules, workspace write boundaries and model/config restrictions, but these are authored constraints on evolution rather than a runtime identity-policy adjudication loop.
- Decisive decision or feedback right: no S5-specific right was found to resolve an identity/ultimate-policy issue or to change the organization's ultimate purpose/constitution at runtime.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: configured `target_pass_rate`; Evolve-Agent prompt constraints; write-only-within-workspace rule; prohibition on changing LLM config; protected original system-prompt rules; static strategy constraints; experiment configuration.
- Closure path: no S5-specific escalation-and-return path established. The Evolve Agent optimizes within the existing pass@1 objective and authored boundaries; it does not escalate an unresolved identity/ultimate-policy question to a legitimate ultimate authority whose ruling returns into later operation.
- Why this is / is not agent-owned: autonomous optimization inside a fixed objective is S4-capability adaptation, not ownership of ultimate policy. Static operator-authored constraints remain configuration even when strongly enforced.
- Evidence: [`evolve_prompt.md`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/agents/evolve_agent/evolve_prompt.md); [`configs/base.yaml`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/configs/base.yaml); [`evolve.py`](https://github.com/china-qijizhifeng/agentic-harness-engineering/blob/8b2a55d97590363fe50c3cc6b5e833b020a4bb4c/evolve.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: a human running AHE can edit configuration or source out of band, but generic maintainer authority is not a first-party operational S5 closure path.

### Absence scope

- Surfaces inspected: base configuration; Evolve-Agent system prompt and strategy constraints; workspace/write restrictions; coding-agent prompt; evolution target/stop rules; Best-of-N; notifications; Explore/Debugger paths; repository-wide searches for policy, governance, identity, approval, escalation and authority mechanisms.
- Plausible first-party paths checked: pass@1 target as mission; protected original prompt rules as identity; operator configuration as parent governance; strategy constraints; model/config immutability; change manifest author metadata; notification/human interaction.
- Why no material first-party path remains: all reviewed paths define or enforce the existing evolution objective and operating boundaries. None establishes a runtime identity/ultimate-policy issue → legitimate ultimate authority → ruling → returned operational change loop.

## Recursion, variety, escalation

At the selected recursion AHE is an evolution organization around a coding-agent S1, not every process/thread as a separate VSM unit. Parallel benchmark rollouts and Best-of-N candidate worktrees therefore do not create S2 by concurrency alone. Likewise, benchmark scores and deterministic stopping rules are not promoted to S3. The two material higher-order closures are narrower: Agent Debugger supplies complementary audit over operational evidence (`S3*`), while Explore/Evolve converts external and prospective evidence into persistent future capability (`S4`).

## Admission conclusion

Proposed vector at the pinned revision: `A — — A A —`. AHE closes autonomous S1 through its model-driven coding agent, autonomous complementary audit through a separate Debugger path that reconciles raw trajectories with external verifier evidence and returns findings to evolution, and autonomous S4 through external research/evaluation-informed harness mutation reused by later operations. No concrete inter-S1 coordination disturbance, distinct whole-current S3 control loop, or identity/ultimate-policy S5 closure is established at the frozen standard-distribution boundary.
