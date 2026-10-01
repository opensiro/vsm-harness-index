---
harness_id: cloud-coding-agent-node
project_name: Cloud Coding Agent Node
repository: https://github.com/fred1433/cloud-coding-agent-node
review_ref: a6758498055b54d765f6ca3423c58c67e0ead18e
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Cloud Coding Agent Node

## Review boundary

- System in focus: the first-party `fred1433/cloud-coding-agent-node` coding-node runtime at frozen revision `a6758498055b54d765f6ca3423c58c67e0ead18e`, including its controller-side model/tool loop, `NodeService` multi-run lifecycle surface, one hardened sandbox per run, tenant/run namespace isolation, reservation-based budget enforcement, event/result contract and the core post-run `acceptance` extension point.
- Purpose and identity: provide a workflow-engine coding step that autonomously writes and runs code in an isolated disposable environment, returns declared artifacts/diff/events/cost evidence, and exposes bounded coordination and complementary acceptance primitives for safe composition into larger workflows.
- Relevant environment: authenticated tenant/workflow caller, task and input files, Anthropic model inference, Docker/gVisor runtime, host filesystem and kernel, configured network/fetch destinations, downstream workflow nodes, and optional caller-supplied acceptance logic.
- Standard-distribution boundary: `codenode/node.py`, `codenode/service.py`, `codenode/sandbox.py`, `codenode/tools.py`, `codenode/webfetch.py`, configuration/schema/pricing/model helpers and shipped runtime behavior are inside. Anthropic/provider internals, Docker/gVisor internals, Kubernetes/host operations and the external workflow engine remain dependencies/parent environment rather than inherited organizational owners.
- Credited operating / distribution surfaces: `README.md`; `codenode/node.py`; `codenode/service.py`; `codenode/sandbox.py`; `codenode/tools.py`; `codenode/webfetch.py`; `codenode/config.py`; `tests/test_contract.py`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; `bench/` attack/benchmark outputs; `deploy/k8s/` validation manifests; recorded `runs/` as evidence rather than runtime owners; `examples/line3/` fixture-specific acceptance implementation except where it demonstrates the constructor path already exposed by core `run_node(..., acceptance=...)`.
- First-party operating / deployment modes considered: direct `run_node` coding execution; `NodeService` start/follow/cancel/wait service mode with concurrent tenant-scoped runs; default network-none sandbox and optional first-party egress/fetch profiles; optional caller-supplied post-run acceptance callable.
- Recursion level: one coding run is an S1 operational unit; a `NodeService` instance may host multiple such runs concurrently. Tenant/run namespace and sandbox isolation can regulate interference among those sibling run units, but the external workflow engine that chooses task topology, global priorities and downstream consequences is outside the assessed boundary.
- Reviewed revision: `a6758498055b54d765f6ca3423c58c67e0ead18e`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Cloud Coding Agent Node is a controller-side autonomous coding loop wrapped in a workflow-node contract. `run_node` validates tenant/server-side policy and node configuration, creates one isolated sandbox, places input files there, then repeatedly calls a model with a first-party coding-agent system prompt and tool schemas. The model selects tool calls; the controller executes them through the hardened sandbox or host-side fetch path, records results and returns those results into subsequent model turns until the model finishes or deterministic limits stop the run.

The runtime deliberately separates trusted controller state from untrusted sandbox output. It tracks ordered events, explicit terminal states, output manifests and a cost ledger. Budget, deadline, max-step, tenant-policy, network and runtime limits are deterministic constraints around the model-owned S1 loop. A failed command becomes tool feedback the model may recover from; trusted-helper failure, timeout or cancellation destroys the sandbox and fails closed.

`NodeService` can host multiple runs concurrently. Runs are keyed by `(tenant, run_id)`; a retry within one tenant returns the already-existing run, while the same public `run_id` in a different tenant creates a distinct run. Each run receives a unique sandbox identifier derived from tenant plus run ID. The shipped contract test exercises this exact interference surface: tenant B may already own `shared-id`, tenant A can still start its own `shared-id`, each gets a different underlying run identity and a third tenant cannot inspect either run. This is a first-party coordination primitive tied to concrete namespace/collision and cross-run interference, not merely generic shared state.

The core runtime also exposes `acceptance` as an optional post-operation hook. After the operational sandbox is destroyed and exported outputs are materialized, `run_node` invokes the caller-provided acceptance callable, records `outputs_accepted` and the resulting checks, and documents that only accepted outputs should feed a consequential next node. The shipped line-3 example demonstrates a materially complementary implementation: hidden expected data unavailable to the agent, recomputation from source and re-execution of delivered code in a fresh sandbox. Because the decisive acceptance judgment/ground truth is supplied by the surrounding workflow rather than an autonomous auditor packaged by the node, this is credited as an S3* constructor path, not autonomous S3* ownership.

No first-party whole-service allocator or supervisor chooses priorities/resources among concurrent S1 runs. Per-run budgets and tenant ceilings are preselected policy and deterministic enforcement. Likewise, no prospective organizational adaptation or ultimate identity/policy loop is shipped.

Primary evidence:

- [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md)
- [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py)
- [`codenode/service.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/service.py)
- [`tests/test_contract.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/tests/test_contract.py)
- [`examples/line3/acceptance.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/examples/line3/acceptance.py)
- [`examples/line3/run_demo.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/examples/line3/run_demo.py)

## Operational model

For each run, the model actor receives the task and current message/tool context, chooses a coding tool action, observes the returned result and iterates. The controller owns sandbox/tool transport and hard constraints; the model owns the open-ended task-specific action choice. The resulting S1 can be hosted directly or as one of several concurrent `NodeService` runs.

At the service level, namespace and sandbox isolation attenuate a concrete cross-run disturbance: identical caller-visible run IDs or attempted cross-tenant access must not alias, block or expose another S1. The coordination outcome changes later run behavior because `start`, `events`, `cancel` and `wait` resolve against the tenant-scoped identity and each S1 continues in its distinct sandbox.

After operational execution, a workflow can supply a complementary acceptance function that examines exported artifacts outside the destroyed operational sandbox and returns a separate verdict before downstream use. Core code transports that verdict into `outputs_accepted`; a surrounding workflow must still supply the actual independent audit logic and enforce downstream consequence.

## S1 — Operations

- State: A
- Function: perform a supplied coding task by autonomously inspecting inputs, writing/running code and reacting to tool/runtime feedback inside a bounded disposable environment.
- Disturbance / variety regulated: heterogeneous task/input state, uncertain code changes, shell/tool outcomes, model uncertainty, execution failures, missing/incorrect outputs and current-run environmental constraints.
- Decisive decision or feedback right: choose the substantive next model/tool action in response to the task and accumulated tool evidence, including when to stop calling tools and produce a completion response.
- Decision owner: the model-backed coding-agent actor driven by the shipped first-party controller loop.
- Supporting / enforcement mechanisms: first-party tool schemas/runner; sandbox; controller event recorder; policy validation; reservation budget; deadline/max-step limits; retries; output export/manifest; network/fetch controls.
- Closure path: task/files → controller model request → autonomous model chooses tool/action → first-party tool/sandbox executes → result returns into message history → model chooses subsequent action → repeated feedback loop reaches completion or a deterministic terminal limit.
- Boundary reachability: `run_node` is the repository's normal node execution API and directly instantiates the model/tool loop; `NodeService.start` invokes the same path without requiring an application-authored agent loop.
- Why this is / is not agent-owned: removing the model actor leaves policy, sandbox, tools and limits but no open-ended task-specific selection of reads, code changes, commands or completion strategy.
- Evidence: [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md); [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py); [`codenode/tools.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/tools.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is an external dependency; deterministic controller enforcement does not become the owner of the model's coding decisions.

## S2 — Coordination

- State: C
- Function: attenuate namespace/state interference among concurrently hosted coding-run S1 units so retries and equal caller-visible run IDs do not collide across tenants and one tenant cannot observe/control another tenant's run.
- Disturbance / variety regulated: concurrent S1 runs can present the same `run_id`, retry an already-running identity, or attempt cross-tenant access; without isolation those interactions could alias operational state, duplicate work, squat an identity or expose/cancel another S1.
- Distinct S1 units: each independently executing `run_node` instance started through `NodeService`, with its own model loop, task, recorder, cancel signal, terminal result and sandbox.
- Inter-S1 disturbance: collision/aliasing and unauthorized cross-access when concurrent runs reuse a caller-visible `run_id` or different tenants query the same identifier.
- Attenuating coordination relation: `NodeService` keys runs by `(tenant, run_id)`, performs idempotent same-tenant start, hashes tenant plus run ID into a unique sandbox identity and resolves events/cancel/wait through the same tenant-scoped key.
- Feedback into subsequent S1 behaviour: the namespace decision determines whether `start` returns the existing same-tenant S1 or creates a new distinct S1, and routes all later lifecycle operations to the correct run/sandbox; the contract test demonstrates two tenants using `shared-id` continue independently while a third tenant sees no run.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation regulates a concrete interference among distinct concurrent operational runs—identity collision, duplicate execution and cross-tenant control/visibility—not merely message transport. The namespace decision changes which S1 exists or receives later lifecycle actions, and the isolated sandbox/run identity keeps the sibling S1s from destructively aliasing each other.
- Decisive decision or feedback right: select/maintain the first-party tenant-scoped identity relation that decides whether an incoming lifecycle action belongs to an existing S1 or a distinct sibling S1 and which run state receives it.
- Decision owner: constructor/runtime path. The first-party service deterministically supplies the S2-specific relation, but no autonomous coordinating agent chooses/revises the policy or resolves coordination discretion.
- Supporting / enforcement mechanisms: service lock, `runs` map, tenant context, hashed sandbox IDs, per-run recorder/cancel/result state and isolated sandbox provisioning.
- Closure path: concurrent lifecycle request → tenant/run identity lookup → collision is attenuated by same-tenant idempotence or distinct-tenant namespace/sandbox creation → later events/cancel/wait are routed to the selected S1 → each coding S1 continues against its own state.
- Boundary reachability: `NodeService` is a shipped first-party service API, and `tests/test_contract.py::test_run_ids_are_per_tenant` executes the exact simultaneous-identity case against standard run execution.
- Why this is / is not agent-owned: the S2 function is structurally closed by a first-party deterministic constructor relation, but removing any autonomous actor leaves materially the same namespace/isolation decision; therefore `A` is not justified.
- Evidence: [`codenode/service.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/service.py); [`tests/test_contract.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/tests/test_contract.py); [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this credits only the specific namespace/isolation disturbance actually wired by `NodeService`; it does not infer richer coordination such as shared planning, negotiation, scheduling or global resource arbitration.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-service current-control function is established above the concurrent coding-run S1 population.
- Disturbance / variety regulated: not established at S3 level. Per-run limits, tenant ceilings and cancellation constrain individual runs but do not constitute a whole-system managerial choice over current shared priorities, commitments or resources.
- Decisive decision or feedback right: not established. The service tracks run entries and routes lifecycle operations, but it does not form a whole-system current view and choose reallocations/interventions on behalf of the run population.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-run budget reservation, max steps, deadline watchdog, policy ceilings, lifecycle status/events, cancellation, sandbox limits and service run registry.
- Closure path: not applicable for the negative finding; observed feedback either regulates one S1 or routes to an already-selected S1 identity rather than closing whole-system current management.
- Why this is / is not agent-owned: hard budget/timeout/policy enforcement continues unchanged without an autonomous manager, while no first-party actor is shown choosing organization-wide tradeoffs among active runs.
- Evidence: [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py); [`codenode/service.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/service.py); [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the surrounding workflow engine may own S3 at a higher recursion, but it is outside this repository boundary and is not inherited.

### Absence scope

- Surfaces inspected: `NodeService` run registry/lifecycle; tenant policy; per-run budget/deadline/max-step enforcement; controller events/status; cancellation; sandbox resource limits; README node contract.
- Plausible first-party paths checked: global run scheduler, shared budget allocator, priority arbitration, admission controller across tenants/runs, whole-service utilization view, exception supervisor and cross-run commitment management.
- Why no material first-party path remains: all located controls are per-run constraints or identity routing. The repository explicitly leaves larger workflow orchestration to a caller and supplies no whole-population decision right over current S1 resources/commitments.

## S3* — Complementary audit

- State: C
- Function: expose a post-operation complementary challenge path that can inspect exported operational artifacts separately from the ordinary agent completion path and produce a verdict before those outputs are used downstream.
- Disturbance / variety regulated: an operational coding S1 may report successful execution while exported artifacts are semantically wrong, non-reproducible, self-tested against weak checks or inconsistent with external/hidden ground truth.
- Decisive decision or feedback right: core `run_node(..., acceptance=...)` invokes a supplied acceptance callable only after execution/export, records the returned checks and sets `outputs_accepted`; the decisive audit judgment itself is intentionally supplied by the surrounding workflow/constructor.
- Decision owner: constructor path. The first-party node owns the audit hook, timing, evidence handoff and verdict field, but a developer/workflow must compose the independent acceptance logic/ground truth and downstream consequence.
- Supporting / enforcement mechanisms: exported output snapshot; ordinary `status`; separate `outputs_accepted`; acceptance result event; example hidden `expected.json`; source recomputation; fresh-sandbox re-execution.
- Closure path: coding S1 finishes and sandbox is destroyed → exported artifacts are handed to the acceptance callable → complementary checks produce pass/fail findings → node records `outputs_accepted`/checks → a composed workflow can permit or withhold consequential downstream use according to that verdict.
- Boundary reachability: `acceptance` is a parameter of the shipped core `run_node` API and is evaluated in the normal result path. The line-3 example is excluded as an owner but demonstrates the intended constructor with hidden evidence and fresh-sandbox replay.
- Why this is / is not agent-owned: removing the operational model does not eliminate the acceptance mechanism; removing the caller-supplied acceptance composition eliminates the substantive audit judgment. The node therefore supplies a real S3*-specific constructor primitive but not an autonomous independent auditor.
- Evidence: [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py); [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md); [`examples/line3/acceptance.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/examples/line3/acceptance.py); [`examples/line3/run_demo.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/examples/line3/run_demo.py); [`tests/test_contract.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/tests/test_contract.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `C` does not credit fixture-specific example logic as part of every deployment. The positive state is the core function-specific acceptance constructor; independent judgment and consequential gating still require composition.
- Claim being audited: that a successfully completed coding run has produced outputs fit for consequential downstream consumption.
- Ordinary reporting path: model completion response plus `status == succeeded`, exported output manifest/diff and ordinary tool/event history.
- Complementary access path: post-sandbox acceptance receives exported artifacts and original inputs independently of the model's completion text; the shipped example additionally uses hidden expected facts, source recomputation and re-execution in a fresh sandbox.
- Independence boundary: core runtime separates the audit phase from the operational sandbox/model loop, but the actual acceptance authority/evidence is caller supplied; therefore independence is available as a constructor and not autonomously closed by the node.
- Who acts on findings: core code records the verdict; the surrounding workflow must use `outputs_accepted` to decide whether outputs feed a consequential next node.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material outside-and-then organizational sensing/adaptation loop is implemented.
- Disturbance / variety regulated: not established at S4 level. Fetch/network tools can bring task-relevant external content into a current run, but that is immediate S1 task evidence rather than prospective organizational intelligence.
- Decisive decision or feedback right: not established. The node does not survey future/external change, develop adaptation options for its own capabilities and return such options into present system configuration.
- Decision owner: not established.
- Supporting / enforcement mechanisms: optional `fetch_url`; egress allowlists; current-run message history; task/tool evidence; static runtime/model/tool configuration.
- Closure path: not applicable; no external/future distinction → adaptation option → present-capability change path is shipped.
- Why this is / is not agent-owned: model reasoning can adapt the current coding task after fresh evidence, but that remains S1 regulation. No durable self-improvement, capability promotion or strategic environmental model is present.
- Evidence: [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md); [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py); [`codenode/webfetch.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/webfetch.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external web access is an operational information source; it is not S4 merely because information comes from outside.

### Absence scope

- Surfaces inspected: model/tool loop; fetch/egress path; configuration/schema; recorded state/event model; service lifecycle; sandbox lifecycle; README limitations and deployment surfaces.
- Plausible first-party paths checked: persistent cross-run learning, environment/trend monitor, model/tool capability evaluation, prospective option generation, self-reconfiguration, durable memory/strategy state and adaptation promotion.
- Why no material first-party path remains: all first-party state is execution/service state for current runs or static configuration; no persistent prospective intelligence loop or return-to-current-capability mechanism is supplied.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established.
- Disturbance / variety regulated: not established at S5 level. Tenant policies, network modes, resource ceilings and provenance permissions bound operation but are supplied constraints rather than runtime identity/policy deliberation.
- Decisive decision or feedback right: not established. The node validates a `TenantContext` that the workflow engine built from its own records and enforces configured ceilings; it does not decide or revise the legitimate ultimate policy behind those constraints.
- Decision owner: ultimate policy remains with the external tenant/workflow/developer authority; no first-party parent-return path for identity-level decisions is packaged.
- Supporting / enforcement mechanisms: `TenantContext`; `DEFAULT_POLICY`; config schema; network/fetch allowlists; runtime allowlist; budget/resource ceilings; provenance permission checks.
- Closure path: not applicable; supplied policy is checked before/during operation, but no identity/ultimate-policy issue is raised to a legitimate authority, decided there and returned as a new governing decision.
- Why this is / is not agent-owned: removing the model actor leaves materially identical policy enforcement, showing the S1 actor does not own ultimate policy. Conversely, the external authority that supplies tenant policy is outside the first-party boundary and no operational S5 parent loop is exposed.
- Evidence: [`README.md`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/README.md); [`codenode/node.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/node.py); [`codenode/config.py`](https://github.com/fred1433/cloud-coding-agent-node/blob/a6758498055b54d765f6ca3423c58c67e0ead18e/codenode/config.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent workflow platform could compose tenant governance around this node; that would be a wider system-in-focus and is not inherited here.

### Absence scope

- Surfaces inspected: tenant context/policy validation; default policy and ceilings; config schema; system prompt; network/fetch permissions; runtime selection; service lifecycle; README contract.
- Plausible first-party paths checked: autonomous policy revision; parent-governed identity escalation/return; dynamic purpose/ethos negotiation; model-owned constraint changes; persistent constitutional state; policy conflict resolution.
- Why no material first-party path remains: all authoritative limits are preselected by code/configuration or supplied by an external authenticated workflow engine, and no first-party identity/ultimate-policy closure path is shipped.

## Assessment summary

Cloud Coding Agent Node closes an autonomous coding S1 through its controller-side model/tool loop. Its `NodeService` also exposes an S2-specific constructor relation: concurrent coding runs are tenant/run namespaced and sandbox-isolated so concrete same-ID and cross-tenant interference is attenuated and later lifecycle actions feed back to the correct S1. The runtime exposes a second constructor path for S3*: post-sandbox acceptance can challenge ordinary completion against complementary evidence before downstream use, with the shipped example demonstrating hidden-ground-truth recomputation and fresh-sandbox replay. Neither function is autonomously owned by a coordinating/auditing agent, so both publish as `C`. Per-run limits do not establish whole-system S3, current-run external fetch is not prospective S4, and supplied tenant policy does not establish S5.

Proposed vector: **`A · C · — · C · — · —`**.
