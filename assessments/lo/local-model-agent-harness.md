---
harness_id: local-model-agent-harness
project_name: local-model-agent-harness
repository: https://github.com/eli-herman/local-model-agent-harness
review_ref: 9dd27c717695337faab70d13ad50f090b7c1d1d7
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# local-model-agent-harness

## Review boundary

- System in focus: The installable local-model-agent-harness CLI and concrete local/SSH ReAct composition.
- Purpose and identity: Answer user tasks using local Ollama inference, bounded command execution and optional persistent fact memory.
- Relevant environment: User questions, local or remote host command results, Ollama service, optional Mem0 service, command policy and connection errors.
- Standard-distribution boundary: The repository-owned build_agent composition, configured prompt, four tools and streaming CLI are the supported executable product. LangGraph and Ollama supply graph/inference mechanisms; no broader framework organization is imported.
- Credited operating / distribution surfaces: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Adjacent first-party surfaces excluded from ownership: LangGraph/Ollama/Mem0 internals and any SSH target organization. Package development and human repository maintenance are adjacent, not a runtime governing parent.
- First-party operating / deployment modes considered: Installed agent-harness one-shot or REPL, distinct thread IDs, local command backend, SSH backend, optional Mem0 enabled/disabled/failure paths.
- Recursion level: One task-executing harness; multiple calls, processes or sessions do not establish recursive viability.
- Reviewed revision: `9dd27c717695337faab70d13ad50f090b7c1d1d7`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

pyproject.toml exposes agent_harness.cli:main. graph.build_agent constructs ChatOllama and create_react_agent with four concrete tools and MemorySaver; invoke_agent and the CLI supply HumanMessage input with a thread_id. tools.run_command parses an argv, checks the command basename allowlist, optionally wraps it for SSH, executes with a timeout and returns output/errors. save_memory/recall_memory call an optional Mem0 service and return explicit soft-failure observations. config.py supplies deployment settings and an operational prompt; cli.py streams model decisions and tool messages to the user. There are no shipped roles/teams, planner-controller, auditor or adaptive strategy service.

Primary implementation: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).

## Operational model

A concrete configured model-and-tool composition executes S1. Although the ReAct graph mechanism is a dependency, the repository supplies a runnable product with selected model, prompt, operational tools, CLI and observation return. This is not a claim that the whole LangGraph framework or the external Mem0 system belongs to the first-party harness. The actor chooses which allowed information/action to request and when to answer; deterministic command gates do not choose the solution.

## S1 — Operations

- State: A
- Function: Produce an answer or system-inspection result through a model/tool feedback loop.
- Disturbance / variety regulated: User tasks, host command observations, memory availability and rejected/failed actions.
- Decisive decision or feedback right: Choose among current_utc_time, run_command, save_memory, recall_memory or a final answer after feedback.
- Decision owner: The model-backed ReAct actor instantiated by build_agent.
- Supporting / enforcement mechanisms: LangGraph graph execution and MemorySaver, ChatOllama inference adapter, first-party allowlisted tools and CLI thread/stream handling.
- Closure path: The concrete tools return observations to the configured ReAct graph; the next model turn acts on those observations and the CLI displays the final response.
- Boundary reachability: The installed console script invokes this first-party composition in both one-shot and REPL modes without requiring a user to write a graph or tool bridge.
- Why this is / is not agent-owned: Removing the model leaves a command/memory API and static prompt, but no task-dependent next-action or completion discretion.
- Evidence: [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

## S2 — Coordination

- State: —
- Function: No separate S2 function established.
- Disturbance / variety regulated: Potential interaction among threads or shared memory users.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Thread checkpointer, Mem0 user partition and single configured executor.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Thread isolation and a shared memory API are generic state mechanisms. The package instantiates no distinct cooperating S1 units with specific interference, attenuating coordination and returned mutual adjustment.
- Evidence: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Plausible first-party paths checked: Thread IDs/MemorySaver, Mem0 user_id partition, single-agent graph construction and local/SSH switching.
- Why no material first-party path remains: Thread isolation and a shared memory API are generic state mechanisms. The package instantiates no distinct cooperating S1 units with specific interference, attenuating coordination and returned mutual adjustment.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control loop.
- Disturbance / variety regulated: Task execution bounds and current host/resource observations.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: Operator selects deployment constraints; task actor owns local operational choices.
- Supporting / enforcement mechanisms: Config allowlist, timeout, output truncation and CLI error handling.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: The runtime enforces fixed operator settings and the actor solves one task. No whole-current organization view plus resource/commitment intervention and autonomous or parent-return closure is supplied.
- Evidence: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Plausible first-party paths checked: Allowlist/config ownership, command timeout, system prompt, REPL/one-shot paths and memory failures.
- Why no material first-party path remains: The runtime enforces fixed operator settings and the actor solves one task. No whole-current organization view plus resource/commitment intervention and autonomous or parent-return closure is supplied.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit path.
- Disturbance / variety regulated: Potential erroneous answers or misleading host observations.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Tool stdout/stderr, exit codes, streaming observations and error messages.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Command outputs are ordinary S1 observations and the same task actor chooses any recheck. There is no separate auditor, alternative access mandate or corrective audit judgment returned to control.
- Evidence: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Plausible first-party paths checked: Tool exit/output return, CLI trace display, memory return/error handling and README operational guidance.
- Why no material first-party path remains: Command outputs are ordinary S1 observations and the same task actor chooses any recheck. There is no separate auditor, alternative access mandate or corrective audit judgment returned to control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability adaptation loop.
- Disturbance / variety regulated: New user facts, changing host environment and future task needs.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: No first-party function-specific decisive owner established.
- Supporting / enforcement mechanisms: Optional Mem0 HTTP calls, thread memory and environment settings.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Fact storage and retrieval affect context but do not develop prospective adaptation options and return an adopted capability change to present operations. Neither optional memory nor operator configuration closes an S4-specific base or parent mode.
- Evidence: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Plausible first-party paths checked: Mem0 save/recall, prompt instructions, thread persistence and model/backend configuration.
- Why no material first-party path remains: Fact storage and retrieval affect context but do not develop prospective adaptation options and return an adopted capability change to present operations. Neither optional memory nor operator configuration closes an S4-specific base or parent mode.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy decision-return process.
- Disturbance / variety regulated: Changes to purpose, command permissions and user instructions.
- Decisive decision or feedback right: No function-specific decisive right and closed feedback path established.
- Decision owner: Operator/developer configure the task boundary; no runtime S5 organization is supplied.
- Supporting / enforcement mechanisms: Static prompt, command gate and deployment environment variables.
- Closure path: The inspected paths do not return a decision closing this metasystem function.
- Why this is / is not agent-owned: Initial operator settings and ordinary action refusals do not route an identity or ultimate-policy issue to legitimate parent authority and return a binding governance decision.
- Evidence: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/README.md); [pyproject.toml](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/pyproject.toml); [src/agent_harness/graph.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/graph.py); [src/agent_harness/tools.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/tools.py); [src/agent_harness/config.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/config.py); [src/agent_harness/cli.py](https://github.com/eli-herman/local-model-agent-harness/blob/9dd27c717695337faab70d13ad50f090b7c1d1d7/src/agent_harness/cli.py).
- Plausible first-party paths checked: SYSTEM_PROMPT, ALLOWED_COMMANDS, local/SSH endpoint selection and REPL interaction.
- Why no material first-party path remains: Initial operator settings and ordinary action refusals do not route an identity or ultimate-policy issue to legitimate parent authority and return a binding governance decision.

## Distributed OSS parent arrangement

The upstream maintainer and contributors govern repository development. That adjacent organization is not a runtime parent mode of the assessed task harness. No function-specific returned organization-level S3/S4/S5 decision is credited merely from contributor activity.

## Self-hosted and non-human modes

The operator selects model, allowlist, timeout, thread and local/SSH endpoint. Such configuration and ordinary REPL messages constrain a single task. No function-specific supervisory S3, adaptive S4 or identity-level S5 referral/return is wired in either backend.

## Recursion

No complete recursive viable unit is established. Local tool execution, process spawning and durable session state alone do not demonstrate a child identity, environment and metasystem.

## Variety and escalation

Refused commands, missing programs, timeouts, SSH errors and disabled/unavailable memory return informative text or CLI errors. The model can revise its next action; the shipped system does not route these exceptions to a metasystem authority.

## Evidence gaps

This is pinned-source analysis. No real model, paid provider, external worker or production workload was executed. Operational success, reliability and downstream effectiveness are unmeasured. The bounded negative judgments concern the declared distribution, not hypothetical future extensions.
