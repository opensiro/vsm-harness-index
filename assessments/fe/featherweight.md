---
harness_id: featherweight
project_name: featherweight
repository: https://github.com/aadhithya/featherweight
review_ref: fc27810cc57580b9fa2fad41c311ca9abc22927c
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# featherweight

## Review boundary

- System in focus: The featherweight packaged Python runner and its first-party job execution facilities.
- Purpose and identity: Run typed model-driven work units and hand validated outputs or failures to a host application.
- Relevant environment: Embedding developer/application, configured model and tools, optional MCP endpoints, workers and persistence.
- Standard-distribution boundary: Published runner, model definitions, streaming, declared children, client/queue/worker modules and supplied persistence. Host workflow code and external tools do not supply credited actors.
- Credited operating / distribution surfaces: The agent library, standard worker/client APIs and supported SQLite or PostgreSQL persistence.
- Adjacent first-party surfaces excluded from ownership: Book examples and document-learning demo as assembled workloads, development tooling, tests, and the development-assistant plugin.
- First-party operating / deployment modes considered: Direct typed invocation, streamed chat and local or submitted jobs with eligible declared children.
- Recursion level: One host deployment of the reusable harness, examining its supplied in-process and worker execution modes.
- Reviewed revision: fc27810cc57580b9fa2fad41c311ca9abc22927c
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Agent classes declare prompt, tool access, models and children. The runner constructs the model/tool loop, validates typed results and handles failed attempts. Worker mode adds leasing, cancellation and background delivery without requiring the host and worker to share a process. [README.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/README.md), [src/featherweight/models.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/models.py), [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py), [src/featherweight/client.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/client.py), [src/featherweight/worker.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/worker.py).

## Operational model

A model-backed agent chooses actions using the configured tools and can launch eligible child agents. Each result returns to the parent, or via the host's next chat turn in streaming background mode. Workers lease and process submitted jobs as execution infrastructure.

## S1 — Operations

- State: A
- Function: Execute an application-defined task as a model-directed turn or tool loop.
- Disturbance / variety regulated: Uncertain task input and intermediate outcomes from tools and nested work.
- Decisive decision or feedback right: Decide the next allowed action and produce or revise the output.
- Decision owner: The model-backed agent instantiated from the host declaration.
- Supporting / enforcement mechanisms: Framework-bound tools, schema validation, context, retry and result handling.
- Closure path: Agent messages and tool results feed subsequent choices. Host sees valid output or a terminal failure.
- Boundary reachability: AgentRunner implements the normal packaged entry point and creates the loop with the host-supplied model and the framework's declared tool constraints.
- Why this is / is not agent-owned: The agent chooses how to act within the typed interface. The framework builds and guards the loop.
- Evidence: [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py#L1443-L1488), [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py#L1198-L1241), [src/featherweight/models.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/models.py).
- Basis: Explicit
- Confidence: High
- Caveats: Agent task purpose and concrete tools come from the embedding deployment.

## S2 — Coordination

- State: —
- Function: Regulate interactions between distinct operative agent units.
- Disturbance / variety regulated: Parallel agent work can interfere through shared resources or duplicated work.
- Decisive decision or feedback right: No supplied agent-level interference arbitration decision path was established.
- Decision owner: None established at the organizational assessment boundary.
- Supporting / enforcement mechanisms: Launch limits, semaphore handback, background completion delivery, and worker leases regulate execution mechanics.
- Closure path: A waiting parent returns its execution slot and reacquires it after children finish. A worker whose lease is lost stops execution.
- Why this is / is not agent-owned: The platform prevents runtime pool deadlock and duplicate execution claims. Host policy still supplies any discretionary coordination of scope, competing outputs, or substantive shared resources.
- Evidence: [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py#L159-L188), [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py#L1198-L1241), [src/featherweight/background.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/background.py), [src/featherweight/worker.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/worker.py#L277-L313).
- Basis: Structural
- Confidence: Medium
- Caveats: The deterministic parent/child slot handback is an explicit resource safeguard. The assessment treats it at runtime execution recursion.

### Absence scope

- Surfaces inspected: Parent/child launch and results, background callbacks, shared runner slots, queue leases and worker recovery.
- Plausible first-party paths checked: Deadlock between a parent attempt and child slot, duplicate claims across workers, and combining overlapping child jobs.
- Why no material first-party path remains: The first two paths stabilize mechanical execution. Generic child launch and results supply no organization-level scope arbitration or interference feedback beyond application-defined choices.

## S3 — Inside-and-now control

- State: —
- Function: Control current commitments across the deployed agents or workers.
- Disturbance / variety regulated: Job failures, cancellations, and demand exceeding worker capacity.
- Decisive decision or feedback right: No whole-deployment current operating view connected to substantive discretionary intervention was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: The host can read job-specific status and cancel it. Worker queue leases and counters drive bounded enforcement.
- Closure path: Cancellation, replay and lease loss produce job state changes. A host can compose decisions from this information.
- Why this is / is not agent-owned: Worker limits and failover enact predetermined rules. Job status and cancellation alone do not establish a whole-system current-control owner and scope.
- Evidence: [src/featherweight/client.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/client.py#L112-L168), [src/featherweight/worker.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/worker.py#L123-L171), [src/featherweight/worker.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/worker.py#L236-L325), [docs/submitted-jobs.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/docs/submitted-jobs.md).
- Basis: Structural
- Confidence: Medium
- Caveats: A host application could implement a separate workload control plane.

### Absence scope

- Surfaces inspected: Runner and worker controls, client status and cancellation, job events, background result handling.
- Plausible first-party paths checked: Current operator oversight over all commitments, agent intervention over other jobs, worker takeover, and host-applied resource changes.
- Why no material first-party path remains: No shipped coupling of an organizational current view with discretionary resource or commitment allocation. Client operations address individual known jobs, and restart/takeover are deterministic.

## S3* — Complementary audit

- State: —
- Function: Independently audit actual work and feed findings into correction.
- Disturbance / variety regulated: A schema-valid report can misrepresent what was done.
- Decisive decision or feedback right: No packaged independent evidence judgment path with direct primary operational access was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Typed output checks, developer callbacks, attempt traces, and retry are built in.
- Closure path: A check_output failure reaches a new retry attempt, with the decision originating in the host-supplied validator.
- Why this is / is not agent-owned: The supplied API evaluates the submitted input and output through the agent instance. Traces carry ordinary execution reporting. An independent evidence source and audit role would come from new host code.
- Evidence: [src/featherweight/models.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/models.py#L202-L208), [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py#L1482-L1488), [src/featherweight/otel.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/otel.py), [docs/observability.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/docs/observability.md).
- Basis: Structural
- Confidence: High
- Caveats: A check_output implementation programmed by a host can query independent evidence, but the shipped signature and default do not install that path.

### Absence scope

- Surfaces inspected: Typed output checking, structured retries, trace/observer API, doclearn sample pipeline and declared children.
- Plausible first-party paths checked: Direct audit through a validation callback, complementary traces, and a separate verifier composed using an example agent.
- Why no material first-party path remains: The callback receives normal input and output and is a no-op by default. Examples and observability do not supply a standard primary-evidence audit and corrective owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense future-relevant external changes and decide a capability adaptation.
- Disturbance / variety regulated: Changing provider and environment conditions can render a deployment's setup unsuitable.
- Decisive decision or feedback right: No supplied prospective intelligence-to-capability return path was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Provider settings, skill and MCP discovery, result reuse and caller-defined pipelines.
- Closure path: Configured tools are found on demand and cached results may resume work. No installed adaptation policy follows from these returns.
- Why this is / is not agent-owned: Tool search and model settings help execute the current task. The document-learning example transforms sample inputs within its application purpose.
- Evidence: [src/featherweight/model_settings.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/model_settings.py), [src/featherweight/registry.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/registry.py), [src/featherweight/skills.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/skills.py), [examples/doclearn/README.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/examples/doclearn/README.md), [docs/example-pipeline.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/docs/example-pipeline.md).
- Basis: Structural
- Confidence: Medium
- Caveats: A host can program a future-facing process using the same runtime.

### Absence scope

- Surfaces inspected: Model providers, skills and discovery, resume, and first-party documentary learning example.
- Plausible first-party paths checked: External signal recognition, prospective host capability decisions, and durable adaptation through model or skills changes.
- Why no material first-party path remains: The library loads configuration and surfaces tools. The sample derives document templates as an operational workload rather than governing the reusable deployment's future capability.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate identity or standing policy questions for the assessed harness deployment.
- Disturbance / variety regulated: Competing purposes and authorities could change the deployment's governing mandate.
- Decisive decision or feedback right: No supplied route for a runtime-originating policy or identity issue to reach an ultimate owner and return as a governed resolution was established.
- Decision owner: None established at the credited deployment boundary.
- Supporting / enforcement mechanisms: Agent classes declare prompt, version, tools and eligible subagents, and the framework assembles the resulting system prompt.
- Closure path: Developer definitions govern their instantiated agents. The library has no first-party decision return loop for settling mandate conflicts.
- Why this is / is not agent-owned: The developer's deployment definition constructs its actors. Permission by declared class and static injected prompt parts are enforcement of design choices.
- Evidence: [src/featherweight/models.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/models.py#L101-L140), [src/featherweight/models.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/models.py#L253-L285), [src/featherweight/runner.py](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/src/featherweight/runner.py), [docs/agents.md](https://github.com/aadhithya/featherweight/blob/fc27810cc57580b9fa2fad41c311ca9abc22927c/docs/agents.md).
- Basis: Structural
- Confidence: Medium
- Caveats: The embedding organization may separately supply an S5 authority with its own policy path.

### Absence scope

- Surfaces inspected: Agent definitions and prompt construction, declared tools/children, worker job binding and developer docs.
- Plausible first-party paths checked: Host as policy parent during operation, policy escalation through run output, and first-party return into future operating authority.
- Why no material first-party path remains: The class API constructs an agent at deployment and app code interprets any output. No explicit in-boundary ultimate decision and return relationship was identified.

## Distributed OSS parent arrangement

Featherweight repository maintainers govern library releases. That governance is adjacent to an installed host application and does not supply its assessment owner.

## Self-hosted and non-human modes

The local and worker modes run application-defined models and policies. Neither exposes a separate installed organizational authority at the assessed boundary.

## Recursion

The assessment covers framework execution under a host. Host-authored operational workflows may exhibit additional functions at a separately declared application recursion.

## Variety and escalation

Validation retries narrow malformed output. Lease recovery and cancellation protect worker execution. Domain conflicts and higher-order decisions return to the embedding application only by its own composition.

## Evidence gaps

Static source at the pinned commit. No provider, application implementation, background queue deployment or external MCP server was executed.
