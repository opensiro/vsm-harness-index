---
harness_id: pyflue
project_name: PyFlue
repository: https://github.com/SuperagenticAI/pyflue
review_ref: 657c2d1a1b024a0bc137ff3bb252339fa0d5f692
reviewed_at: 2026-10-19
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

# PyFlue

## Review boundary

- System in focus: The shipped first-party **Python model-backed operating agent harness** whose `PyFlueSession.prompt/task/skill` methods route model decisions to declared sandbox/custom/MCP tools and return typed results through an integrated pluggable backend. The assessed recursion is one persistent user/agent instance with its own sessions or one workflow-invoked agent; it is **not** the application organization that installs PyFlue, nor every hosted model/backend implementer.
- Purpose and identity: Allow an application to build and operate a bounded tool-using AI agent with persistent session context, configurable tools, skills, sandbox isolation, subtask delegation, events and optionally finite workflows.
- Relevant environment: User task/input, changing filesystem and tool responses, provider model output, sandbox permissions, session history, streaming clients, asynchronous incoming messages, child-task outcomes, service interruption and errors.
- Standard-distribution boundary: `pyflue/core.py`, `pyflue/agents.py`, `pyflue/harnesses/base.py`, shipped default `pyflue/harnesses/pydanticai.py`, optional `deepagents.py`, `pyflue/harnesses/registry.py`, `pyflue/sandbox.py`, `pyflue/sandboxes/`, `pyflue/session_history.py`, `pyflue/skills.py`, `pyflue/workflows.py`, `pyflue/dispatch.py`, CLI/server modules and published examples as *supported wiring evidence*, not as a separate developer's organizational governance.
- Credited operating / distribution surfaces: [README.md](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/README.md#L1), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L100), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L525), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L1479), [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L41), [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L124), [pyflue/agents.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/agents.py#L129), [pyflue/dispatch.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/dispatch.py#L66), [pyflue/workflows.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/workflows.py#L1).
- Adjacent first-party surfaces excluded from ownership: Maintainer/contributor development and CI, design/parity roadmap, examples' externally chosen business domains, their developer-supplied custom agents/workflows and policies, independent hosted Pydantic AI/DeepAgents reasoning implementation and provider weights, external sandbox platform operators, human organizational management and release governance. The published framework's explicit backend adapter is credited for model-to-tool wiring, but ownership of its provider API is **not** imported into a first-party higher recursion.
- First-party operating / deployment modes considered: `init(...)` with packaged Pydantic AI backend and optional installed DeepAgents backend, `create_agent/init_agent` persistent instances, `PyFlueSession.prompt` and `task`, declarative skills/roles, workflows invoked with `ctx.init`, REST/WebSocket service client and async `dispatch`; built-in virtual/local/remote sandboxes, configured provider/model and policy/approvals, history compaction and tracing. Server/client smoke is not equated to live provider model inference.
- Recursion level: One goal-facing model-backed agent operating cell; subordinate `task` invokes child sessions with inherited/scoped sandbox and separate history. Multiple independently maintained application agents would require a separately evidenced shared operational S2/S3 organization rather than automatic aggregation here.
- Reviewed revision: `657c2d1a1b024a0bc137ff3bb252339fa0d5f692`, official GitHub repo ID **1227772650**, exact fresh clone source tree `b86990ddcd42fc4935b169a7769b03321ad6b054`, frozen [batch #1735](https://github.com/opensiro/vsm-harness-index/issues/1735). Root `LICENSE` contains Apache 2.0 text; GitHub license API returned `NOASSERTION`.
- Observation date: 2026-10-19; Profile 0.2.4 / Skills Methodology 0.3.7 with immutable generation pair.

## Repository architecture

A `create_agent` definition records application-provided instructions, toolkit/model and related metadata, while `init` loads configuration and chooses the pluggable backend through the shipped registry. `PyFlueSession.prompt` constructs user/context/role input, merges the allowed tool set, invokes `_run_backend`, captures result/usage/events and persists conversation history; its typed output checker can give feedback for a model repair turn. The default backend `PydanticAIBackend.run` actually constructs a Pydantic AI `Agent(model, instructions, tools=_build_tools(...))`, invokes `agent.run(prompt)`, and returns its model/tool-run response to PyFlue's session. This is a first-party **source-connected model/tool act–observe loop**, using an explicitly external Python reasoning library; it is not merely an unimplemented `LLMProtocol` interface. [pyflue/agents.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/agents.py#L129); [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L100); [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L525); [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L1479); [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L41); [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L124).

The user/session chooses which tool behavior is allowed via `sandbox`, `allow_write`, `allow_shell`, `allowed_commands`, custom tools, optional MCP services and declared `skills`. Backend-adapted model tool calls run under those predeclared permissions and feed actual tool outcomes to its loop. `task` creates a subordinate session with isolated history but shared/scoped sandbox; recursion depth and role/model overrides are configured, not autonomously managed portfolio priorities. `dispatch` admits asynchronous input to the instance's background task queue, explicitly process-memory rather than restart-safe delivery. File-based workflows execute application-authored `run(ctx)` scripts with lifecycle records. None of these additional paths, by label alone, proves a separate agent-owned S2/S3/S3*/S4/S5. [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L737); [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L827); [pyflue/dispatch.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/dispatch.py#L1); [pyflue/workflows.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/workflows.py#L1); [pyflue/sandbox.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/sandbox.py#L1).

The optional DeepAgents backend and registry allow replacing the model-loop implementation. That variation is a deployment choice; the documented default is the Pydantic AI path, where the model's substantive choices are reached through first-party PyFlue wrappers. Even if a provider library implements much of the inner loop, the first-party model/tool owner is exercised through the shipped backend and provided operation boundary. Developer-defined workflows and business goals are excluded from claims about a supplied metasystem. [pyflue/harnesses/base.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/base.py#L1); [pyflue/harnesses/registry.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/registry.py#L1); [pyflue/harnesses/deepagents.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/deepagents.py#L1).

## Operational model

The relevant transformation is an application-authorized prompt and live contextual/tool variety becoming a sequence of provider model-selected actions, tool observations and a user-facing/typed result. Session persistence, tracking, file and command permissions, child dispatch, retry on invalid structured result, tracing and finite workflow orchestration are supporting mechanisms, not automatic distinct VSM executive or future adaptation functions.

## S1 — Operations

- State: A
- Function: Select and execute context-sensitive tools and typed/final responses for an application-assigned user task, with feedback from actual tool results.
- Disturbance / variety regulated: Unknown user tasks, changing repository/workspace state, available skill/tool choices, dynamic model replies, tool errors, incomplete result schemas and session history context.
- Decisive decision or feedback right: The model in the shipped default Pydantic AI operating mode, called from `PyFlueSession`, chooses declared tool calls and arguments or final output, receives actual tool results and can continue/revise the task response.
- Decision owner: Configured AI model acting through first-party `PydanticAIBackend.run` integration; application host predefines goals/permissions and the external Pydantic AI library transports/executes the inner model/tool protocol, but neither static config nor PyFlue session storage decides the next substantive tool for arbitrary observations.
- Supporting / enforcement mechanisms: Session/history store, provider registry, typed tool adapter, sandbox policy, effect permissions, optional MCP and skills, result parser/retry, event log, model usage accounting, workflow/HTTP wrappers.
- Closure path: Application goal → `session.prompt` context/history and declared tools → `_run_backend` → `Agent.run` model tool selection → authorized tool execution and model observation → PyFlue result/history/event or model repair turn → completed task.
- Boundary reachability: Supported `pyflue init`/API `create_agent`, `init(..., harness="pydanticai")` and `session.prompt` routes construct the shipped backend and pass concrete merged sandbox/custom tool adapters into the provider-backed agent loop. The official quick-start and code sample connect these paths without requiring separately authored orchestration core.
- Why this is / is not agent-owned: Remove the model and the first-party session wrapper, sandbox and registry can still store messages/enforce permitted tools but cannot pick task-specific tools or adapt to their results. The decisive S1 action remains model-owned in this supported composed mode.
- Evidence: [README.md](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/README.md#L59), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L525), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L554), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L1479), [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L41), [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L63), [pyflue/harnesses/pydanticai.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/pydanticai.py#L124).
- Basis: Explicit first-party registration, supported model tool invocation and return path, not a benchmarked success claim.
- Confidence: High for structural supported capability, medium for actual runtime availability in the local evidence environment.
- Caveats: `pydantic-ai` and configured model provider are external dependencies; isolated gateway lacked required `aiosqlite` when attempting its official model-free server/client smoke. No live inference, tool-effect success rate or server deployment was independently attested.

## S2 — Coordination

- State: —
- Function: No first-party distinct coordination owner was shown judging and attenuating specific mutual interference/oscillation between at least two independently viable S1 operating divisions with feedback to affected operations.
- Disturbance / variety regulated: Multiple sessions, child subtasks and concurrent dispatch inputs might compete for filesystem/tool/provider limits, but their shared resources and queue alone are not an evidenced inter-S1 conflict resolution relationship.
- Decisive decision or feedback right: The task-owner agent can delegate a child with a model/role override; the runtime limits recursion depth, isolates child history and processes async deliveries. No documented shipped first-party adaptive coordination decision responds to operational conflict between independently viable S1s.
- Decision owner: Calling S1 model or application for delegation/priority; deterministic task/queue and per-session enforcement for transport/admission.
- Supporting / enforcement mechanisms: `task`, child session IDs/parent link, max task depth, scoped sandbox, process-memory dispatch queue, finite `run(ctx)` workflows and event transport.
- Closure path: Parent task asks child → scoped child response → parent continues; separately async input enqueues and runs prompt. These paths do not establish sensed competing S1 interference → specialized S2 regulatory judgment → changed subsequent behavior of the two S1 units.
- Why this is / is not agent-owned: Child invocation is an S1 work operation and a queue is a mechanical scheduler; neither grants agent authority over conflict dampening.
- Evidence: [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L737), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L827), [pyflue/dispatch.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/dispatch.py#L20), [pyflue/dispatch.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/dispatch.py#L66), [pyflue/workflows.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/workflows.py#L1).
- Basis: Bounded negative after checking exposed nested task, workflow and delivery relationships.
- Confidence: Medium-high at the declared single-agent application boundary.
- Caveats: A separate application using several PyFlue agents could program an S2-specific regulator; a hypothetical host composition is not credited as shipped default.

### Absence scope

- Surfaces inspected: Child task/subagent session, dispatch queue, workflow dispatch, event/role services and sandbox sharing.
- Plausible first-party paths checked: Concurrent child tools, multiple persistent sessions and provider calls, possible shared workspace collisions and task dependency orchestration.
- Why no material first-party path remains: The shipped controls expose general delegation, routing and fixed safety limits but no source-backed concrete inter-S1 conflict detector/adjudicator with returned mutual operational adjustment within this assessed first-party mode.


## S3 — Inside-and-now control

- State: —
- Function: No independently owned whole-current management loop is evidenced that negotiates present resources, priorities and obligations across autonomous S1 departments and returns binding adjustments.
- Disturbance / variety regulated: Per-session token/context saturation, unauthorized writes/shell commands, malformed typed responses, queued input and subtask depth can affect execution reliability; they are local policy/enforcement and do not entail whole-organizational management.
- Decisive decision or feedback right: Application/developer selects model, sandbox, permission flags, allowed commands, role and max task depth; package enforces those bounds and tracks usage. No first-party agent manager decides cross-operation current commitments or resource reallocation.
- Decision owner: Host/application for authorization and operating constraints; task model for tool/action choices; deterministic engine for fixed bounds/usage.
- Supporting / enforcement mechanisms: SandboxPolicy, per-tool routing, child depth check, session storage, request events, compaction and output schema validation/retry.
- Closure path: Task's action/tool request → sandbox policy/admission/retry/error → same task continues or stops; no whole-current executive view → managerial choice → cross-S1 behavior change is shown.
- Why this is / is not agent-owned: Tool enforcement and workflow `run(ctx)` scheduling are useful infrastructure but the decisive organizational current-management right is not packaged with an autonomous owner in this boundary.
- Evidence: [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L100), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L153), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L737), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L827), [pyflue/sandbox.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/sandbox.py#L1), [pyflue/workflows.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/workflows.py#L1).
- Basis: Source-bounded negative after checking host config, sandbox/session/task/workflow control.
- Confidence: Medium-high.
- Caveats: Multi-agent application operators may exercise human S3 externally without a supported first-party returned parent-governed management mode.

### Absence scope

- Surfaces inspected: Main session/child-operation controls, config/model sandbox bounds, typed tool permissions, workflow run and storage lifecycle.
- Plausible first-party paths checked: Current priorities across sessions, host-configured shell/file rights, queue pressure, child model choice, execution error handling.
- Why no material first-party path remains: No first-party discretionary manager has a portfolio of S1 commitments and an operational S3 decision/return; fixed permissions and host-authored workflows are support, not demonstrated whole-current authority.


## S3* — Complementary audit

- State: —
- Function: No complementary independent audit channel of ordinary S1–S3 claims with a distinct audit judgment returned into current organizational regulation is evidenced.
- Disturbance / variety regulated: Untrusted tool responses, malformed structured output and failed operations can lead to wrong task answers; ordinary validation/error checks and observability catch local faults but do not independently verify executive reports against distinct operational reality.
- Decisive decision or feedback right: `_parse_with_retry` checks result schema and asks the same configured model to repair; event traces/OTel and session logs record ordinary run evidence without appointing an independent auditor with corrective governance authority.
- Decision owner: Same operating task model and deterministic parser/logger, not a separate complementary checker with independent mandate.
- Supporting / enforcement mechanisms: Pydantic typed result, retries, run events, OpenTelemetry adapter, history and test suite.
- Closure path: Parse failure → model-local retry, or tool/run event → log/client; no alternative evidence → independent corrective audit finding → changed S3 current decisions.
- Why this is / is not agent-owned: Parsing a schema and recording telemetry do not constitute a source-independent audit; ordinary tests of the framework are adjacent development QA rather than live run governance.
- Evidence: [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L1820), [pyflue/observability/otel.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/observability/otel.py#L1), [pyflue/runs.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/runs.py#L1), [pyflue/session_history.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/session_history.py#L1).
- Basis: Bounded negative from first-party typed validation/telemetry/repair mechanisms and runtime mode boundaries.
- Confidence: Medium-high.
- Caveats: Application-specific independent evaluators could be built using the emitted telemetry; no such first-party corrective S3* path was demonstrated.

### Absence scope

- Surfaces inspected: Typed-result validator/retry, logs/events/OTel, run/session records, tests and optional child-task calls.
- Plausible first-party paths checked: Structured-output repair, runtime status tracing, stored tools/history for offline validation, external model/tool checking.
- Why no material first-party path remains: These paths are local quality controls and transport for possible evidence, not complementary independent reality inspection of the organization's operation with audit authority and corrective feedback into S3.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future-oriented external environmental sensing → strategic option formulation → adopted changed organizational capability loop is established in the shipped agent harness.
- Disturbance / variety regulated: Changing input/context, tool availability and task instructions can require immediate adaptation, but prompt memory compaction, skills discovery and model/backend selection are task or developer configuration operations rather than prospective policy/capability change.
- Decisive decision or feedback right: Application/developer determines agent definitions, provider, tools, workflow file contents and persistent skills. The executing agent can adapt next S1 tool calls but does not have a shipped mandate to investigate future opportunities and authorize durable skill/model/strategy changes for subsequent independent runs.
- Decision owner: Operator/developer for long-term product and harness configuration; operating model for current prompt response.
- Supporting / enforcement mechanisms: Session history, role/skill loading, compaction, memory/session store, pluggable backends and workflow examples.
- Closure path: Old task context → compressed/reloaded context and unchanged configured toolkit → next current task; no external future distinction → model options → selection/adoption → modified future operating capability and return path is evidenced.
- Why this is / is not agent-owned: A model adapting its answer within a task is S1 discretion, not S4; static skill installation and dynamic model selection by developer do not themselves create future organizational intelligence ownership.
- Evidence: [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L525), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L1157), [pyflue/skills.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/skills.py#L1), [pyflue/config.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/config.py#L1), [pyflue/harnesses/registry.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/harnesses/registry.py#L1), [pyflue/workflows.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/workflows.py#L1).
- Basis: Source-bounded negative after considering current/future features and optional configuration.
- Confidence: Medium-high for the declared mode.
- Caveats: A developer can implement self-updating skills or a strategic research agent as a user application, but that is outside the evidenced default operating path.

### Absence scope

- Surfaces inspected: Skill/role loaders, persistent conversation/compaction, pluggable backend registry, agent/workflow definitions and event/dispatch APIs.
- Plausible first-party paths checked: Context recap and remembered history, new workflows, model selection, skills addition, future policy changes by applications.
- Why no material first-party path remains: No shipped first-party external-and-prospective distinction/option/adoption/return loop owns changes to future operational capabilities; these are developer-supplied composition inputs and local prompt support.


## S5 — Policy and identity

- State: —
- Function: No first-party legitimate decision path for ultimate-purpose and organizational identity questions, with a returned enduring policy governing later operations, was found.
- Disturbance / variety regulated: Permission decisions, provider configuration, shell commands and user task restrictions impose policy boundaries on current work; no organization-identity conflict is admitted and adjudicated at this recursion.
- Decisive decision or feedback right: The host/user chooses mission, sandbox and allowed operations; the runtime enforces those settings, while a model selects permissible current tools. The application organization remains external ultimate authority.
- Decision owner: External user/developer/organization for ultimate goals and acceptable risk; static first-party permission mechanism only enforces delegated bounds.
- Supporting / enforcement mechanisms: `SandboxPolicy`, `allow_write` / `allow_shell`, command filtering, configured provider/role/skill and runtime error reporting.
- Closure path: Operator constraints → tool allow/deny → operating task continues/halts; no ultimate-purpose issue → legitimate S5 authority judgment → changed binding identity-level policy is present.
- Why this is / is not agent-owned: A sandbox permission flag or `pyflue.toml` policy cannot decide an organization's ultimate identity. App-level owners may do that elsewhere, but there is no first-party parent-governed S5 intake/return loop in the reviewed runtime.
- Evidence: [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L100), [pyflue/core.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/core.py#L204), [pyflue/sandbox.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/sandbox.py#L1), [pyflue/config.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/config.py#L1), [pyflue/agents.py](https://github.com/SuperagenticAI/pyflue/blob/657c2d1a1b024a0bc137ff3bb252339fa0d5f692/pyflue/agents.py#L129).
- Basis: Bounded negative after reviewing operating config/policy and adjacent human input.
- Confidence: Medium-high.
- Caveats: This denies **shipped first-party S5 closure** at this recursion, not the existence or necessity of actual user/operator organizational governance.

### Absence scope

- Surfaces inspected: Sandbox policy, model/tool configuration, allowed commands, instructions/skills and user-developer agent declarations.
- Plausible first-party paths checked: Human authorization over file/shell mutations, static guardrails, provider role settings and stop/error paths.
- Why no material first-party path remains: No first-party intake of an identity/ultimate-policy question reaches legitimate authority and returns an enduring constitutional decision to govern subsequent work.


## Recursion

One PyFlue model-backed persistent user/agent instance with sessions or a workflow-invoked operating cell is the credited S1. Subtasks create child sessions, and the runtime can host other agent definitions, but a hypothetical application-defined multi-agent organization with independent executive/coordination/audit/identity rights cannot be silently imported from generic SDK interfaces.

## Variety and escalation

Tool results, errors and user responses feed current model decisions; session history, sandbox limits, task depth, structured-result retries and asynchronous dispatch constrain local variety. Process-local dispatch may lose accepted messages on restart, as the repository itself notes. Operational events are not by themselves an algedonic high-priority signal to a separate legitimate authority.

## Evidence gaps

- Root `LICENSE` is Apache License 2.0 text; GitHub SPDX autodetection reported `NOASSERTION`, so the root file rather than API license classification is cited.
- Attempted documented `examples/server_client/run_smoke.py` in an unmodified isolated Linux source checkout. It aborted before running with `ModuleNotFoundError: No module named 'aiosqlite'`; no live model inference, sandbox execution success, persisted server/session result or empirical agent task completion was tested.
- External Pydantic AI / DeepAgents backends and model provider APIs are runtime dependencies, not first-party PyFlue governance owners. The integrated default adapter code structurally connects model tool choices to PyFlue sessions.
- This file is `status: proposed` and does not change canonical catalog/signatures/rankings until a separately verified admission transaction.
