---
harness_id: codeact
project_name: CodeAct
repository: https://github.com/xingyaoww/code-act
review_ref: d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CodeAct

## Review boundary

- System in focus: the source-distributed CodeActAgent interaction harness that turns user requests into model-proposed executable Python code, feeds back interpreter output, and produces a user-facing answer; includes the shipped per-conversation Jupyter execution service that supports multiple concurrent chat sessions.
- Purpose and identity: enable discretionary, iterative programmatic actions over a persistent session interpreter instead of rigid predefined JSON tools; success is task-specific user work or an explicit bounded failure.
- Relevant environment: user dialogue, available model service, code execution results and exceptions, interpreter state, per-chat session identity and runtime resource/timeout constraints.
- Standard-distribution boundary: documented `python scripts/chat/demo.py` and `scripts/chat/code_execution/start_jupyter_server.sh`/`api.py` with `jupyter.py`; first-party Docker and Kubernetes execution-service modes. The separately checked-out `chat-ui` submodule and hosted vLLM/llama.cpp model service are external dependencies, not assumed to donate first-party decision authority.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md) documented quickstart; [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (`Agent`, `Generator`, `ClientJupyterKernel`); [`scripts/chat/code_execution/api.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/api.py) (`ExecuteHandler`/cleanup); [`scripts/chat/code_execution/jupyter.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/jupyter.py) (container/pod gateway).
- Adjacent first-party surfaces excluded from ownership: `mint/` data-generation and benchmark harnesses, `scripts/eval/` experiment-specific agents/evaluators, `docs/MODEL_TRAINING.md`, model weights and paper benchmarks, separate `chat-ui`/Megatron-LLM/FastChat submodules and upstream deployment operator. Their functions do not become runtime organizational owners without a traced call path.
- First-party operating / deployment modes considered: command-line single-user chat with executable code; shared code-execution HTTP API serving multiple `convid` sessions with Docker default or Kubernetes flag; user-installed model endpoint and optional chat UI. No live provider call, container creation, generated Python execution, or benchmark run was performed during assessment.
- Recursion level: one bounded multi-session code-interaction service. Per-session model/code loops are operational cells, not separately proven viable enterprises.
- Reviewed revision: `d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8`; observation 2026-10-30; Profile 0.2.4 and Methodology 0.3.7 (generated/current).

## Repository architecture

`scripts/chat/demo.py` uses `Generator.generate` to call an OpenAI-compatible model. `Agent.handle_user_message` adds the user input, asks the model for content that may contain `<execute>...</execute>`, extracts the code and sends it through `ClientJupyterKernel.execute` to the execution endpoint. A `convid` identifies the session; result text is appended as a new conversational message, allowing the model to choose another code action or final answer. A fixed default of three executions limits one user-turn loop. The executable service's `ExecuteHandler.post` lazily constructs a session-specific `JupyterKernelWrapper` and kernel for each `convid`, sends execution to it and maintains last-access time. The Docker backend starts per-chat named containers with CPU/memory limits; Kubernetes creates a uniquely named pod and corresponding service. A timed cleanup removes stale sessions. The model service, external Python packages invoked by generated code and hosted web environment are dependencies, not first-party decision owners.

## Operational model

An operational cell receives a user's task and interpreter observations. The model decides whether and what code to execute, may revise its approach after results, or stops with an answer; Python transport and container gateway enforce parsing, session mapping and bounded execution. Across conversations the server isolates state so a variable or imported library in one session does not contaminate another. Model capability is pretrained/externally hosted; saving a transcript is not an autonomous strategy update or prospective environmental intelligence.

## S1 — Operations

- State: A
- Function: transform an open-ended user request into appropriate code-execution actions and a subsequent answer at the task boundary.
- Disturbance / variety regulated: variable natural-language questions, available Python state, software/tool/library outcomes, exceptions and intermediate computed observations.
- Decisive decision or feedback right: the model selects executable Python and the subsequent code/answer sequence in response to interpreter output, within a configured maximum of code executions.
- Decision owner: first-party model-backed `Agent` calling `Generator`; model service returns content but does not own the harness's code-execute-and-observe workflow.
- Supporting / enforcement mechanisms: `<execute>` parser, `ClientJupyterKernel`, Jupyter execution API, conversation message list, execution-count limit, Docker/Kubernetes gateway.
- Closure path: user task → generated code → first-party API execution → observed text/error → new model message → revised code or final response.
- Boundary reachability: `Agent.run` drives the documented Python CLI; `Agent.handle_user_message` calls `handle_execution`, which calls the session executor and appends its returned output for the next generation.
- Why this is / is not agent-owned: removing the model's discretionary code/action choice leaves a fixed execution transport; code selection and continuation are model driven, while safety/isolation primitives are deterministic.
- Evidence: [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (`Agent.handle_user_message`, `handle_execution`, `Generator.generate`); [`README.md`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md) CodeAct interaction description.
- Basis: structural.
- Confidence: high for source-wired feedback/continuation.
- Caveats: upstream model quality and safety of generated code are unverified; local code execution was deliberately not run.

## S2 — Coordination

- State: C
- Function: attenuate code-execution state interference between distinct simultaneously served chat-session operational cells.
- Disturbance / variety regulated: two independent conversations could otherwise overwrite variables, packages, execution state or temporary files when sharing one long-lived Python interpreter.
- Distinct S1 units: each separately identified conversation runs a user-facing code-action cell, potentially concurrently through the common Tornado execution API.
- Inter-S1 disturbance: one session's mutable interpreter global state or installed package changes could pollute another session's calculations/outputs if both shared a single kernel.
- Attenuating coordination relation: `ExecuteHandler` keys a per-session `conv_id_to_kernel` map on `convid`; an unknown conversation instantiates its own Docker container or Kubernetes pod/gateway plus kernel, while subsequent calls reuse only that session's kernel.
- Feedback into subsequent S1 behaviour: code execution returns results from the correct session-specific kernel, and later actions use that session's state without another conversation's changes; expired sessions are removed, requiring new isolated state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: separate stateful execution sandboxes address a specific destructive cross-cell state collision; merely forwarding a request or tagging a message would not insulate mutable interpreter state.
- Decisive decision or feedback right: determine session-to-kernel ownership and enforce separation; it is a deterministic per-conversation binding, not an autonomous negotiation between session agents.
- Decision owner: shipped `ExecuteHandler` plus `JupyterGatewayDocker` or `JupyterGatewayKubernetes` session allocation mechanism; no separate agent chooses/revises the isolation rule.
- Supporting / enforcement mechanisms: session map, per-conversation Docker container/pod creation, Jupyter kernel initialization, unique names, timeouts, CPU/memory quotas and gateway teardown.
- Closure path: `convid` on each request → select/create isolated environment → execute only in its kernel → return that result to the originating agent's dialogue.
- Boundary reachability: default Docker branch in `api.py` runs `JupyterGatewayDocker`; `USE_KUBERNETES=1` selects a shipped Kubernetes backend. The README documents per-chat container execution.
- Why this is / is not agent-owned: cell-specific model agents do task-level work but deterministic server code owns the collision-attenuating session binding; hence C rather than A.
- Evidence: [`scripts/chat/code_execution/api.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/api.py) (`ExecuteHandler.post`, `conv_id_to_kernel`, `cleanup_kernels`); [`scripts/chat/code_execution/jupyter.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/jupyter.py) (`JupyterGatewayDocker.__enter__`, `JupyterGatewayKubernetes.__enter__`).
- Basis: structural.
- Confidence: medium-high for intended isolation; actual isolation under running containers was not tested.
- Caveats: this is narrow per-session interpreter-state coordination, not arbitrary peer-agent workflow negotiation or multi-tenant security certification.

## S3 — Inside-and-now control

- State: —
- Function: no independently evidenced whole-service current resource/commitment regulation beyond fixed session lifecycle and quotas.
- Disturbance / variety regulated: runaway code executions or stale kernels may occupy CPU/memory, but the code applies static per-container limits and fixed idle cleanup rather than a whole-system discretionary resource decision.
- Decisive decision or feedback right: a fixed `n_max_executions` truncates one task turn, and 10-minute idle cleanup tears down old containers; no aggregate resource/commitment negotiation with a global view is shown.
- Decision owner: Python constants and startup operator, not a distinct operational S3 owner.
- Supporting / enforcement mechanisms: CPU/memory limits, `cleanup_kernels`, `PeriodicCallback`, execution counter and deployment configuration.
- Closure path: stale session cleanup or local execution limit ends that cell, without demonstrated whole-system resource bargaining/accountability across active sessions.
- Boundary reachability: session limits are shipped and callable, but this does not establish higher-order S3 regulation.
- Why this is / is not agent-owned: a fixed cleanup rule can enforce a bound without model-owned or substantive deterministic whole-current control decisions.
- Evidence: [`scripts/chat/code_execution/api.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/api.py) (`cleanup_kernels`, timer); [`scripts/chat/code_execution/jupyter.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/jupyter.py) (resource constraints); [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (turn limit).
- Basis: structural.
- Confidence: medium.
- Caveats: a separately operated Kubernetes cluster may have a scheduler/control plane, but external orchestration authority cannot be credited to CodeAct.

### Absence scope

- Surfaces inspected: CLI agent loop, execution API, per-conversation session map, Docker and Kubernetes gateway lifecycle, README-supported deployment modes, resource limits and cleanup.
- Plausible first-party paths checked: `n_max_executions`, per-container resource quotas, idle kernel cleanup, Kubernetes pod allocation and code-execution output feedback.
- Why no material first-party path remains: each is an execution-bound enforcement mechanism; no code-level whole-service view drives priority/resource/commitment trade-offs or accountable intervention across active sessions.

## S3* — Complementary audit

- State: —
- Function: no complementary inspection of operational assertions independent of the ordinary model-to-interpreter loop.
- Disturbance / variety regulated: code may compute a wrong answer or fail; raw interpreter output is visible, but visibility to the originating agent is part of its normal execution path.
- Decisive decision or feedback right: execution output is returned as a normal user-role observation to the same agent; no separately appointed checker can challenge its conclusions with additional reality access.
- Decision owner: ordinary session agent and deterministic Jupyter output transport.
- Supporting / enforcement mechanisms: Jupyter output, saved dialogue JSON, timeout/errors and optional benchmark evaluation outside the active service.
- Closure path: output directly informs next model action or final answer; no independent audit finding returns to an S3 owner.
- Why this is / is not agent-owned: model self-correction is operational feedback, and the existence of `scripts/eval/` tests does not itself wire an S3* channel into the documented live service.
- Evidence: [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (`handle_user_message`, `save`); [`scripts/chat/code_execution/api.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/api.py) (`ExecuteHandler`).
- Basis: structural.
- Confidence: medium.
- Caveats: externally configured evaluation could add an audit, but it is not part of this first-party runtime boundary.

### Absence scope

- Surfaces inspected: ordinary dialogue loop, execution output and error handling, transcript persistence, HTTP gateway, README and adjacent evaluation entry points.
- Plausible first-party paths checked: Jupyter outputs, replay of saved JSON conversation, isolated kernel results, and benchmark evaluator directories.
- Why no material first-party path remains: outputs are ordinary S1 observations and benchmark runners are separate research evaluation workflows; no independent sampled probe/reconciliation/audit-to-control path is wired into the active CodeAct chat service.

## S4 — Outside-and-then intelligence

- State: —
- Function: no sustained externally/prospectively oriented adaptation of the CodeAct operating capability at this recursion.
- Disturbance / variety regulated: an agent can investigate new information via generated code in response to one task, but this remains within-request operational variety.
- Decisive decision or feedback right: the agent chooses next code based on current interpreter output; it does not model anticipated environment changes, develop future options and return them through current-control assessment.
- Decision owner: operational model for task actions; future model/prompt releases are developer-controlled and outside the runtime.
- Supporting / enforcement mechanisms: conversation history, persisted JSON, model weights produced in separate training tracks and deployment choice.
- Closure path: current tool feedback influences current or later messages in the same session, not a prospective adaptation option closing into the service's installed capability.
- Why this is / is not agent-owned: model-led programming and observations are agentic, but generic planning, chat memory and iterative task correction alone do not meet S4's future/outside test.
- Evidence: [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (`Agent.messages`, execution loop, `save`); [`README.md`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md) (separate model training/deployment).
- Basis: structural.
- Confidence: medium-high for absence in shipped chat runtime.
- Caveats: the agent could be *asked* about the future by a user, but ordinary task response does not confer S4 organizational authority.

### Absence scope

- Surfaces inspected: main CodeAct CLI, executor HTTP service, container lifecycle, session JSON persistence, README research/training/deployment pathways.
- Plausible first-party paths checked: iterative code revision after tool results, conversation memory, new Python package installation, model training references and benchmark outputs.
- Why no material first-party path remains: no shipped controller senses future-relevant external trends, develops adaptation choices and installs/returns an evaluated capability change to the current service via a two-way S3 relation.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy deliberation or legitimate ratification path within the runtime CodeAct session organization.
- Disturbance / variety regulated: code permissions and model deployment involve risks, but runtime instructions and static container bounds alone are not identity-governing decisions.
- Decisive decision or feedback right: the user/operator picks model endpoint and runtime deployment, while the assistant chooses task-level code; no first-party mechanism elevates an ultimate-policy conflict to a legitimate parent and returns an authoritative ruling.
- Decision owner: external operator and repository maintainers, not a first-party ACE-like or CodeAct policy council.
- Supporting / enforcement mechanisms: static `SYSTEM_MESSAGE`, execution cap, container quotas, launch settings and infrastructure defaults.
- Closure path: fixed task limits and prompts shape code actions without any ratified change of identity/policy.
- Why this is / is not agent-owned: a model instruction, static policy text or Docker boundary is not proof of legitimate ultimate-policy ownership.
- Evidence: [`scripts/chat/demo.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/demo.py) (`SYSTEM_MESSAGE`, args); [`scripts/chat/code_execution/jupyter.py`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/scripts/chat/code_execution/jupyter.py) (static resource limits); [`README.md`](https://github.com/xingyaoww/code-act/blob/d607f56c9cfe9e8632ebaf65dcaf2b4b7fe1c6f8/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: upstream community governance is beyond this assessed runtime, not an inferred S5(P) feedback route.

### Absence scope

- Surfaces inspected: system prompt, CLI session/run boundaries, executor configuration, resource limits, optional Kubernetes mode, README and training documentation.
- Plausible first-party paths checked: user instructions, max-execution enforcement, code isolation, model endpoint selection and author-controlled prompt/deployment changes.
- Why no material first-party path remains: none routes system identity or ultimate policy questions to legitimate decision authority and feeds the resulting decision back into subsequent operating rules.

## Distributed OSS parent arrangement

Published researchers and submodule maintainers can update code/model releases, but the reviewed source has no wired communication/escalation channel by which CodeAct's session-level identity conflicts reach their authority and are ratified into live policy. External user administration does not automatically produce S5=P.

## Self-hosted and non-human modes

The user may self-host model and executor using Docker/Kubernetes or connect an OpenAI-compatible endpoint. The task loop can select and execute code without per-action approval in the standard script. Isolation is session-specific, not an assurance that generated code is safe; no generated code was run during this static assessment.

## Recursion

Per-conversation code-execution loops have local task outcome and discretionary model action; the shared endpoint attenuates session-state collisions. Neither individual session nor nested Python interpreter has an evidenced full distinct metasystem/identity policy set, so technical containment does not establish viable nested organizations.

## Variety and escalation

Executable Python expands local action variety; model feedback from interpreter output helps absorb environmental uncertainty. Session-specific kernels attenuate cross-conversation interference. A per-turn execution cap and 10-minute idle timeout bound resource consumption. Hitting these limits returns a task failure/teardown, not a verified algedonic path to whole-current or ultimate-policy authority.

## Evidence gaps

- No real model API, Docker/Kubernetes container, Jupyter service or provider-specific code execution was invoked in this assessment; S2 isolation is source-structural and not an operational security certification.
- The Git submodule `chat-ui` is external to the pinned first-party code review; its potential user administration and feature set are not credited to this assessment.
- The repository includes multiple experimental agent/evaluation tracks, but the selected publicly documented interactive runtime is the accountable system boundary for the assessment; papers and leaderboard scores cannot substitute for its decision ownership evidence.
