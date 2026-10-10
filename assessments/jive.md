---
harness_id: jive
project_name: Jive
repository: https://github.com/merijjeyn/jive
review_ref: 7b12a061ac77aca94851a0c2f53e6140fae95e74
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Jive

## Review boundary

- System in focus: packaged Jive Bun/TypeScript CLI coding agent, its GraphAgentController primary model planner, first-party DAG executor, bash/Jev decision nodes, plugin evaluation and saved-graph repair/edit loop.
- Purpose and identity: accelerate coding and bulk analysis by having a primary model choose executable graphs instead of a long sequence of high-cost model tool-call decisions.
- Relevant environment: current repository and tool/shell state, task goals, provider/model inference results, graph execution reports, plugin outputs and user configuration.
- Standard-distribution boundary: first-party planner/executor/session CLI. Jev model service and any external provider are inference dependencies; demo benchmarks, taskground and third-party skills are excluded from native organizational ownership.
- Credited operating / distribution surfaces: src/planner/agent.ts, src/core/executor.ts, src/core/schema.ts, src/core/graph-edits.ts, src/core/process.ts, src/jev/client.ts and src/cli.tsx.
- Adjacent first-party surfaces excluded from ownership: harbor/taskground evaluation harness, demo/video benchmarks, docs' aspirational claims, GitHub CI/maintainers and unrelated user-authored external multi-agent extensions.
- First-party operating / deployment modes considered: default CLI coding GraphAgentController; graph program execution with bash/Jev nodes; conditional, repeat and foreach groups; saved graph editing and reruns; project skills and runtime instructions.
- Recursion level: one Jive planner operating on a coding task and driving mechanical/semantic child graph steps. Bash and Jev evaluation nodes are task suboperations, not by default separate autonomous S1 organizations.
- Reviewed revision: 7b12a061ac77aca94851a0c2f53e6140fae95e74.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The GraphAgentController provides one primary model-based planner with execute_graph and execute_graph_mod as its intrinsic actions. Rather than a usual alternating tool-call loop, it generates executable graph programs containing deterministic bash actions and Jev fast semantic judgments. First-party executeGraph validates the graph and runs DAG-dependency/condition gates with a bounded concurrency semaphore. It creates per-node outcomes and append-only event artifacts, honors loops/foreach, executes actual tools, and returns an aggregate report so the same planner can decide what to do next, modify its program or answer.

Despite independent concurrent graph nodes, the basic node types are bash and Jev evaluation, not separately tasked autonomous coding-agent loops. The source explicitly proposes replacing multi-agent stacks with a model planning higher-level execution graphs. A graph's edges reflect mechanical data flow, and the Jev node chooses scoped answers/acceptance conditions, but no demonstrated first-party inter-S1 conflict attenuation loop exists. The GraphAgentController can reinterpret failed results and rerun a graph, a plausible control candidate without a separable whole-current S3 decision owner at the selected recursion.

A Jev node can reject unacceptable output and return a yielded result; however evidence supplied to Jev is selected by the graph planner, and there is no default independent source-inspection audit channel or automatic corrective audit governance. S3* remains uncertain rather than credited from a separate model name. Long-term skills/session context and user-run schema limits are not prospective organizational adaptation or ultimate policy by themselves.

Primary pinned code: [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts); [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/core/schema.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/schema.ts); [src/core/graph-edits.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/graph-edits.ts); [src/jev/client.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/jev/client.ts).

## Operational model

Primary model drives project work by deciding graph code and interpreting graph outcomes. The runtime performs deterministic shell work, fast semantic Jev calls and strict graph contract enforcement, collecting tool evidence and failures. Error reports may cause planner reruns, but multiple autonomous coding units, independent audits and prospective strategic renewal are not established merely from DAG labels.

## S1 — Operations

- State: A
- Function: Model-directed planning and execution of project coding work through a first-party graph of shell commands and scoped fast judgments.
- Disturbance / variety regulated: Unknown repository requirements, execution errors, CLI/test output and requested task changes.
- Decisive decision or feedback right: Design graph instructions, accept or modify graph based on observed results and choose subsequent executable steps.
- Decision owner: Primary LLM GraphAgentController plus first-party executeGraph task executor, with Jev serving lower-scope bounded evaluation choices.
- Supporting / enforcement mechanisms: Native Bun/TypeScript provider integration, bash/Jev nodes, execution artifacts, session persistence, graph JSON schema and error surfaces.
- Closure path: Coding request → planner designs execute_graph → first-party executor runs bash/Jev task steps → records output, execution state and errors → model receives graph report and chooses next graph/edit or final answer.
- Boundary reachability: CLI creates native GraphAgentController wired to source executor and first-party native tool/graph functions; not a wrapper around an external coding-agent binary.
- Why this is / is not agent-owned: Main model owns operational graph choices, with observed effects returned through graph report. Deterministic executor enforces and records.
- Evidence: [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts); [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/core/process.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/process.ts); [src/cli.tsx](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/cli.tsx); [docs/GRAPH_CONTRACT.md](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/docs/GRAPH_CONTRACT.md).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Jev is a decision support dependency; evaluation outputs do not by themselves establish an independent organization or benchmark quality..


## S2 — Coordination

- State: —
- Function: No demonstrable function-specific inter-S1 coordination among independently deciding coding operating cells.
- Disturbance / variety regulated: Simultaneous bash/Jev graph nodes share a project environment, but they are low-level task operations/evaluators, not evidenced independently governed S1 units whose oscillatory interference is autonomously attenuated.
- Decisive decision or feedback right: No S2 coordinating right established; graph dependency scheduling enforces data dependencies of a single planner-authored program.
- Decision owner: No independent S2 decision owner.
- Supporting / enforcement mechanisms: DAG dependency tokens, semaphore concurrency, groups, graph limits, automatic output refs.
- Closure path: Completing graph node releases a dependent node via the same program's deterministic scheduler; a tool-level dependency is not organizational cross-agent feedback.
- Why this is / is not agent-owned: The graph intentionally replaces multi-agent workflows with a single planner, mechanical bash work and small bounded Jev decisions. Generic DAG scheduling is not proof of S2 recursion.
- Evidence: [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/core/schema.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/schema.ts); [src/core/types.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/types.ts); [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts); [README.md](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/README.md).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: No claim that future custom graph/plugin integrations could not create multiple S1 operating cells..

### Absence scope

- Surfaces inspected: Native GraphAgentController and graph execution engine, node schemas and grouping, Jev adapter, plugin execution and scheduler.
- Plausible first-party paths checked: DAG needs, foreach/repeat groups, bounded concurrent bash commands, Jev decision node, planner graph reuse and corrections.
- Why no material first-party path remains: The validated shipped graph nodes are shell operations or Jev decisions inside a single executing planner's program, with no separate autonomous S1 operating organization receiving inter-unit conflict dampening and corrective decision ownership.


## S3 — Inside-and-now control

- State: ?
- Function: A planner can reinterpret graph progress and reissue modified programs, but whether it owns a distinct whole-current regulation function is unresolved.
- Disturbance / variety regulated: Graph effects can partially fail, exceed budgets or produce unexpected outputs and need reprioritization of work.
- Decisive decision or feedback right: The main model reviews report-level status and can call execute_graph_mod to adjust graph and rerun; this may remain normal S1 planning rather than S3 multi-unit current resource governance.
- Decision owner: Potential primary planner, not a demonstrably separate metasystem above autonomous coding cells.
- Supporting / enforcement mechanisms: Graph reports, event streams, allowFailedDependencies, stop on error, context compaction and saved graph edits.
- Closure path: Execution result with error/status → model chooses next graph/modification; not established that this regulates several autonomous S1 commitments at the whole-current level.
- Why this is / is not agent-owned: A single planner’s control over its program is not automatically a separate whole-system regulator; evidence supports a possible but not decisive S3 interpretation.
- Evidence: [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts); [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/core/graph-edits.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/graph-edits.ts).
- Basis: structural + explicit.
- Confidence: medium for controls, indeterminate for S3.
- Caveats: Do not count graph-level status and reruns as S3 merely from their labels..


## S3* — Complementary audit

- State: ?
- Function: Fast Jev node acceptances and separate evaluations can test generated outputs, but no mandatory independent audit with complementary access and correction closure has been established.
- Disturbance / variety regulated: The primary model or code program can overclaim a completed task or generate incorrect output.
- Decisive decision or feedback right: Jev model can answer scoped questions and accept/evaluate criteria, but graph author chooses state and tests; independent operational reality acquisition and audit role are not required.
- Decision owner: Candidate fast Jev evaluator, but its independence and definitive audit feedback path to operative coder remain ambiguous.
- Supporting / enforcement mechanisms: jev.evaluate, validateAnswer, accept expressions, tool trace and graph status yielded/blocked.
- Closure path: Planner defines question/state → Jev returns answer → graph may yield on acceptance failure → the planner sees report and may change program. This is feedback, but not a proven sufficiently independent source-inspecting audit channel.
- Why this is / is not agent-owned: A model call different from the planner and typed acceptance does not alone establish complementarity when its evidence is planner-authored state.
- Evidence: [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/jev/client.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/jev/client.ts); [src/core/schema.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/schema.ts); [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: No exclusion of user-authored graphs that explicitly build and validate independent evidence; claim is native generic contract only..


## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped prospective environment-facing organizational adaptation decision loop.
- Disturbance / variety regulated: Changes in future user environment/project capability demands are not autonomously scanned and converted into organization-level renewal.
- Decisive decision or feedback right: No prospective adaptation judgment owner; provider selection, project instructions and saved graph edits are operational context.
- Decision owner: No S4 authority evidenced.
- Supporting / enforcement mechanisms: Skills/instructions snapshots, session history/compaction, provider models and plugin catalog.
- Closure path: Context and skills alter later prompts or graph drafting, but no outside-future intelligence loop decides new capability renewal and closes it to current operations.
- Why this is / is not agent-owned: Future improvement is an aspiration in README; using different model tiers and persisted sessions is not S4.
- Evidence: [src/core/project-skills.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/project-skills.ts); [src/planner/agent.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/planner/agent.ts); [src/session/context.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/session/context.ts); [README.md](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/README.md).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: External developer updating Jive versions is outside first-party runtime organizational authority..

### Absence scope

- Surfaces inspected: Project instructions and skills snapshots, planner context, graph versioning, session store and model registry.
- Plausible first-party paths checked: Skill selection, provider changes, cache compaction, saved graph modification, user reassignment of tasks.
- Why no material first-party path remains: No first-party model-owned external/prospective sensing process with adaptive-option decision and capability-changing return path into present coding organization was found.


## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy-governance function above coding-graph operation.
- Disturbance / variety regulated: Resource/time limits, user instructions and data trust are not foundational system-identity policy conflicts.
- Decisive decision or feedback right: No S5 ultimate-policy decision right; code executes user-specified local graph/program limits.
- Decision owner: User/model chooses task scope, while deterministic validation enforces fixed boundaries.
- Supporting / enforcement mechanisms: Graph schema validator, limits and CLI configuration, permission and immutable stream header.
- Closure path: Invalid programs/over-budget calls fail or request correction; no ultimate-identity issue is resolved and returned as organization-wide binding policy.
- Why this is / is not agent-owned: Schema gates, immutable graph rules, and user model settings are support/authorization, not S5.
- Evidence: [src/core/schema.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/schema.ts); [src/core/executor.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/executor.ts); [src/core/runtime-contract.ts](https://github.com/merijjeyn/jive/blob/7b12a061ac77aca94851a0c2f53e6140fae95e74/src/core/runtime-contract.ts).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: No assertion about governance in the project’s public maintainer organization..

### Absence scope

- Surfaces inspected: Graph schema, execution budget, CLI model configuration and session permissions, program validation.
- Plausible first-party paths checked: Fixed tool ceilings, schema restrictions, graph immutability, user-issued instructions and model switching.
- Why no material first-party path remains: No identity/ultimate-policy organizational authority and deliberation → binding decision → governing return path exists in the shipped coding harness at this recursion.


## Distributed OSS parent arrangement

The public Jive project's maintainers, taskground benchmark developers and ecosystem providers are not first-party owners of organizational decisions inside an installed CLI coding task. The source's marketing comparison against other systems is not imported into function ownership or measured operational quality.

## Self-hosted and non-human modes

LLM and Jev calls can route to separately chosen inference providers, with owned source code preserving the graph execution contract. Tool outputs, provider selection and session artifact effects stay within one coding-graph harness. No parent-governed higher function is inferred merely because a user approves graph execution.

## Recursion

A graph's command and Jev nodes are computational suboperations; their concurrency is neither independent S1-agent recursion nor an S2 coordinating organization absent function-specific cross-cell interference/feedback. The principal task-operating autonomy belongs to the planner/executor combination.

## Variety and escalation

The executor records graph node failures, emitted events, blocking dependencies, exhausted budgets and yielded Jev acceptance as structured observations. The primary planner can revise or rerun a saved graph with the resulting feedback, or stop. This is source-native task adaptation, but it does not alone settle S3/S3* organizational ownership.

## Evidence gaps

- S2 is negative at the chosen first-party coding recursion: tool-node concurrency does not establish coordination among multiple autonomous operating cells.
- S3 remains unresolved, because the whole-graph planner could be interpreted as a manager but direct higher-recursion current resource/commitment regulation is not demonstrated.
- S3* remains unresolved; Jev evaluation and acceptance may serve an audit inside carefully authored graphs, but first-party evidence independence and systematic corrective return are not proven for the standard native mode.
- No empirically benchmarked success or token-efficiency claim is made from the demo comparison table.
