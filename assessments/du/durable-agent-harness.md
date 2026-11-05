---
harness_id: durable-agent-harness
project_name: Durable Agent Harness
repository: https://github.com/Eldergenix/Durable-agent-harness
review_ref: c4af97c1636127ae577491f8c2b6935207076062
reviewed_at: 2026-11-05
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

# Durable Agent Harness

## Review boundary

- System in focus: a single bounded multi-session knowledge-answering episode using the first-party Agent, MemoryManager, planner, provider, verifier, recovery and budget interfaces.
- Purpose and identity: produce answers to context-dependent questions across multiple synthetic sessions, studying memory persistence, budget use, verification and recovery under controlled disturbances.
- Relevant environment: session facts, distracting context, query semantics, limited token/tool/step budgets, injected ingestion failures and, in an optional mode, an external OpenAI-compatible language-model endpoint.
- Standard-distribution boundary: `src/dah/` library and public `Agent.run` path, with the default deterministic SimulatedProvider and optional separately installed OpenAI-compatible provider; no autonomous external coding environment or unspecified host application is credited.
- Credited operating / distribution surfaces: [agent loop](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py), [optional live provider](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/providers/openai_compat.py), [memory manager](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/memory/manager.py), [planner](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/planner.py), [verifier](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/verifier.py).
- Adjacent first-party surfaces excluded from ownership: pre-registered study hypotheses, research governance rules, quality-gate/test hooks, experiments, generated statistical plots, offline benchmark grading and development journal; these validate research, not live agent organizational decisions.
- First-party operating / deployment modes considered: default seeded simulated recall model and synthetic environment; optional live endpoint via `OpenAICompatProvider` and self-check; baseline versus verification/recovery/budget-enabled configured Agent.
- Recursion level: one sequential query-answering agent episode, not a team of independently operating agents or a research laboratory treated as a runtime VSM.
- Reviewed revision: `c4af97c1636127ae577491f8c2b6935207076062`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent.run` iterates sessions and information/query turns in a fixed episode definition. The memory manager persists optional compaction, episodic and semantic stores between session resets. At a query it asks a fixed or budget-aware planner for retrieval depth and retry allowance, assembles context, obtains `Provider.respond`, applies deterministic relevance-based verification, and may reformulate/retrieve/retry or abstain. Ingestion has an optional checkpoint/recovery path against seeded injected faults. The default `SimulatedProvider` probabilistically models context accessibility; its output is **not an AI actor**. The optional `OpenAICompatProvider` instead sends context/question to a real chat model and returns model-selected cited fact IDs, allowing the same answer-production path to be exercised with a bounded autonomous model decision. No general-purpose model-selected tools or self-authored plans are supplied. [Architecture and limits](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/README.md), [agent code](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py), [provider bridge](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/providers/openai_compat.py).

The research harness enforces integrity constraints with seeded simulations, answer-key separation, paired ablations and repository-only tests. Environment grading is deliberately external to the model and does not become an independent online audit of the operational agent. The live provider is explicitly a sanity-check adapter, not a validated production judge; its `USED:` parsing is a self-report. [Research design](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/docs/DESIGN.md), [rules](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/RULES.md), [live check](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/experiments/live_check.py).

## Operational model

In the optional live mode, the external model chooses an answer and claimed supporting context facts for each question, a bounded S1 decision responding to variable content. The first-party harness chooses **when** it may answer/retry, how much context it receives and whether an embedding threshold is met; those mechanical safeguards do not make the model owner of organizational S2–S5. In default experiments the provider is seeded simulation and no model agency should be inferred from its metrics. The environment's scoring oracle is strictly post hoc, with no independently governed in-operation audit feedback.

## S1 — Operations

- State: A
- Function: answer variable context-dependent user/task queries across sessions using the optional live model mode.
- Disturbance / variety regulated: differing questions, incomplete retrieved context, distractor facts, variable remembered evidence and semantic uncertainty.
- Decisive decision or feedback right: the configured language model selects its answer and which provided facts it reports using; the harness may reject and send a refined query to it.
- Decision owner: external OpenAI-compatible model reached through the first-party provider; **not** the deterministic SimulatedProvider used for published experiments.
- Supporting / enforcement mechanisms: `Agent._answer`, memory retrieval/context caps, `QueryPlan`, `ConsistencyVerifier`, token/step budget and forced abstention/retry.
- Closure path: session query → memory context → live `Provider.respond` → model-generated answer/citations → verifier decision/retry or environment result; subsequent turns proceed with retained memory.
- Boundary reachability: the released library exposes `OpenAICompatProvider` with optional dependency and compatible `Provider.respond`; README describes using the same `Agent` loop with a live endpoint, while `live_check` establishes only a manual single-question smoke path. No third-party host orchestration is imported.
- Why this is / is not agent-owned: the real model exercises bounded semantic answer discretion; retrieval policy, retry count, checkpoint and grading are deterministic first-party algorithms. The simulated default has no autonomous S1.
- Evidence: [Agent._answer](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py), [OpenAI-compatible response](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/providers/openai_compat.py), [README](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/README.md).
- Basis: structural, optional documented model-backed mode.
- Confidence: medium; supported interface is visible, live endpoint not executed and no free-form outcome judge is wired.
- Caveats: model emits a bounded answer, **not** self-directed tool calls or dynamically chosen execution objectives. Default published experiment runs are deterministic and should never be scored as autonomous behavior.

## S2 — Coordination

- State: —
- Function: no inter-agent coordination function is supplied at this recursion.
- Disturbance / variety regulated: source includes multiple sessions, stores and experimental arms, but no collision between two independent operational S1 units.
- Decisive decision or feedback right: absent; no inter-unit mediation or returned coordination decision.
- Decision owner: none within the shipped agent episode.
- Supporting / enforcement mechanisms: ordered session loop, shared memory stores and single-agent budget counters.
- Closure path: the sequential query loop contains no second concurrently acting S1 unit to negotiate or constrain.
- Why this is / is not agent-owned: alternate experiment runs are statistical replicates, not cooperating live operational agents.
- Evidence: [Agent.run](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py), [experiment runner](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/experiments/runner.py).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: an external application could arrange multiple such agents, but that is not supplied by this repository.

### Absence scope

- Surfaces inspected: agent loop, session environment, memory, experiment runner and provider interfaces.
- Plausible first-party paths checked: multiple sessions, parallel experimental arms, shared stores, fault injection and concurrent budgets.
- Why no material first-party path remains: no distinct interacting S1 operations or disturbance-to-coordination-feedback channel is implemented.

## S3 — Inside-and-now control

- State: —
- Function: no organizational whole-current decision maker over autonomous operational units.
- Disturbance / variety regulated: remaining budget and number of queries left, not an organizational portfolio of commitments or capacities.
- Decisive decision or feedback right: deterministic budget-aware allocation adjusts per-query context caps, retrieval and retries; it does not decide among independent S1 commitments.
- Decision owner: configured Python `BudgetAwarePlanner` rules and enclosing experiment/operator, not a model-backed regulator.
- Supporting / enforcement mechanisms: `Budget.remaining`, `pressure`, `queries_remaining`, hard charges and stop rules.
- Closure path: a budget measurement alters next query's retrieval depth and token allowance inside the same S1 episode; no distinct S3 current-control loop is closed.
- Why this is / is not agent-owned: a useful cross-query cost algorithm does not become resource/priority authority over an organization.
- Evidence: [planner](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/planner.py), [budget](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/budget.py), [agent loop](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: a parent can tune the budget and experiment conditions, but no parent-governed S3 organizational closure is shipped at this recursion.

### Absence scope

- Surfaces inspected: BudgetAwarePlanner, StaticPlanner, budget accounting, experiment configuration, Agent.run.
- Plausible first-party paths checked: budget pressure, allocation across remaining queries, stop-on-exhaustion, environmental scoring and parent-run configuration.
- Why no material first-party path remains: all paths are local deterministic execution economics and lack a whole-organization current commitment decision owner.

## S3* — Complementary audit

- State: —
- Function: no independent channel challenges the operational agent's claim against distinct online reality evidence.
- Disturbance / variety regulated: missing or irrelevant recalled facts and possible incorrect answers.
- Decisive decision or feedback right: `ConsistencyVerifier` compares the query vector with the model's **reported** recalled fact embeddings; thresholds accept/reject and request retries.
- Decision owner: deterministic same-answer-path verifier, not an independent auditor with complementary evidence.
- Supporting / enforcement mechanisms: relevance threshold, empty-recall check, retry/reformulation loop, offline `env.score_query` against ground truth, repository research gates.
- Closure path: verifier rejects and agent retries within ordinary operations; synthetic environment grades **after** the answer and stores research metrics, not audit findings returned to S3 authority.
- Why this is / is not agent-owned: same model-reported facts and ordinary QA are not a complementary independently accessed reality channel; the held-out answer-key oracle is explicitly absent from online decisions.
- Evidence: [verifier](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/verifier.py), [Agent._verify](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/agents.py), [design](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/docs/DESIGN.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: independent benchmark grading is valuable research assurance, but a different recursion and disconnected from runtime S3*.

### Absence scope

- Surfaces inspected: `ConsistencyVerifier`, live provider self-reported USED markers, environment grader, result CSVs, quality gate.
- Plausible first-party paths checked: oracle-free relevance checks, synthetic ground-truth scoring, research governance, corrective return to independent controller.
- Why no material first-party path remains: no operational complementary path independently inspects actual answer correctness and governs a corrected S1/S3 decision.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/environment exploration driving adaptation of operational capability.
- Disturbance / variety regulated: changing context length, noise, failure rates and benchmark parameters in preconfigured scientific sweeps.
- Decisive decision or feedback right: researcher/config writer selects preset sweeps; the runtime planner changes current query budgets, not future capability.
- Decision owner: research maintainer/operator, outside the assessed agent operation.
- Supporting / enforcement mechanisms: memory ablations, tau/noise/context sweeps and journalled hypotheses.
- Closure path: studies yield plots and conclusions; no deployed agent prospective-options loop returns a capability change to current runtime.
- Why this is / is not agent-owned: experimental sensitivity analysis is outside the agent's online future-facing decisions.
- Evidence: [experiment runner](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/src/dah/experiments/runner.py), [design](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/docs/DESIGN.md).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: a researcher can use findings to redesign a future release, but that is not a shipped autonomous or parent-governed S4 process.

### Absence scope

- Surfaces inspected: study runners, planner, memory parameter presets, GOAL/RULES design and live-provider extension.
- Plausible first-party paths checked: benchmark results as future intelligence, adaptive retrieval under current budget, operator tuning and automatic reconfiguration.
- Why no material first-party path remains: no external/prospective distinction → adaptation proposal → returned current capability decision loop is implemented.

## S5 — Policy and identity

- State: —
- Function: no runtime legitimate highest-level policy/identity arbitration for a persistent organization.
- Disturbance / variety regulated: research-rule compliance and query-level constraints rather than conflicts over an operational organization's identity or ultimate goals.
- Decisive decision or feedback right: GOAL/RULES are fixed maintainer documents and hooks; a user can change configs, not exercise a returned first-party S5 governance loop.
- Decision owner: repository maintainers for scientific ethics/protocol, outside the assessed runtime.
- Supporting / enforcement mechanisms: source lints, frozen hypothesis files, tests, local edit hooks and budget constraints.
- Closure path: quality gates reject noncompliant development artifacts; no operational S5 issue reaches legitimate authority and returns to govern future agent behavior.
- Why this is / is not agent-owned: code-repository research governance and runtime guardrails do not establish ultimate-policy closure within the agent harness installation.
- Evidence: [RULES.md](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/RULES.md), [GOAL.md](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/GOAL.md), [quality gate](https://github.com/Eldergenix/Durable-agent-harness/blob/c4af97c1636127ae577491f8c2b6935207076062/scripts/quality_gate.py).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: governance exists for the *study*; no conclusion is made about the human research group's wider organizational viability.

### Absence scope

- Surfaces inspected: GOAL/RULES, developer hooks, runtime configuration, safety/budget/abstain controls.
- Plausible first-party paths checked: approved amendments to frozen research rules, episode goals, model endpoint choice, escalation to human owner and returned identity-level policy.
- Why no material first-party path remains: the research repository has maintenance rules but no shipped loop adjudicating identity/ultimate-policy decisions for its running agent installation.

## Recursion

This is one active context-answering agent with persistent memory layers. Multi-session turns, memory stores, verification passes, research arms and model/provider choices are components or repeated experiments, not additional independently viable S1 organizations.

## Variety and escalation

Context assembly and retrieval absorb information variety; budget-aware caps attenuate scarce tokens; verification/retry/abstain responds to weak relevance; checkpoints and replay recover deterministic injected faults. Missing evidence or repeated failure terminates locally rather than escalating through an autonomous organizational policy hierarchy.

## Evidence gaps

- Frozen source inspected; no paid live model endpoint run, so the optional model-backed S1 is interface-supported rather than observed E2E. The default research corpus is explicitly deterministic simulation.
- Live provider reports used fact IDs, not free-text answer validity, and the maintainer expressly leaves a production judge as an extension point.
- This assessment does not count pre-registration, quality gates, experimental benchmark oracle or research ethics as operational S3*/S5.
