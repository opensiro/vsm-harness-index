---
harness_id: runvil-harness
project_name: runvil-harness
repository: https://github.com/cppalliance/runvil-harness
review_ref: ee199e3ae04366e02c61488c096f2981c057ff0b
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Runvil Engine and Harness

## Review boundary

- System in focus: the first-party Rust Runvil prompt engine, Harness library, shipped model/tool loop and gateway/Pack adapters.
- Purpose and identity: run Markdown/Lua prompts, execute model-selected tools and return recorded task results to a Host.
- Relevant environment: Host application, selected inference broker/gateway, file system, remote MCP/web services and authored prompt input.
- Standard-distribution boundary: public runvil/runvil-engine APIs, private engine/runner crates, first-party gateway client, web/MCP plugins and shipped executable prompt compositions.
- Credited operating / distribution surfaces: Harness::run, models.loop, effect dispatch/answer return and research_person prompt; the latter demonstrates the supplied operational mode, rather than donating an external actor.
- Adjacent first-party surfaces excluded from ownership: offline greeting example, fake-broker integration tests, structural xtask/CI checks, repository development tooling and external Runvil Host/Gateway product organizations.
- First-party operating / deployment modes considered: library embedded in a documented Host with broker/timer/Packs, ordinary model/tool prompt, nested prompt chains, optional user inbox/control and VFS policy.
- Recursion level: one prompt execution organization; chains are subordinate execution contexts, not assumed viable systems.
- Reviewed revision: `ee199e3ae04366e02c61488c096f2981c057ff0b`.
- Observation date: 2026-11-19.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Runvil separates a deterministic Engine from a per-run Harness that performs requested effects. A Host binds Packs, prompt finding and a timer, then creates RunSetup with recorder, broker, filesystem, model selection and limits. Harness::run prepares the prompt and drives step→record→perform→answer→resume. Model/tool/timer futures run inside that future; file requests execute synchronously and are recorded. RunControl can send input, stop a round or cancel. Records preserve correlated events, effects, answers and final results.

Prompts combine prose, Lua and model-role declarations. models.loop is implemented by a first-party Rust state machine behind a Lua trampoline, so a Host does not have to invent iterative tool handling. The supplied research_person composition offers web search/fetch, adds the user's task and enters that loop. The provided run-prompt Rust example instead uses an offline greeting and is explicitly not autonomous evidence. Web/MCP Packs extend tools; the gateway client binds inference/search. Stores are run/execution-local; remote provider internals, CI and development governance remain outside the assessed ownership boundary.

Primary surfaces: [public Harness/Host API](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil/src/lib.rs), [RunSetup](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/setup.rs), [models.loop state machine](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/lua/src/models_loop/machine.rs), [models.loop adapter](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/lua/src/models_loop.rs), [effect loop](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/effect_loop.rs), [Harness and RunControl](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/harness.rs), [gateway broker](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-gateway-client/README.md), [shipped research prompt](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/prompts/research-person.md), [runtime boundary](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/runtime/README.md), [VFS Policy](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/vfs/src/traits/policy.rs), [recorder interface](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/recorder.rs).

## Operational model

A model-led prompt/chain is S1 when it chooses meaningful task actions from offered tools and sees their outcomes. Lua execution, broker transport, cap enforcement, VFS policy and recording support that discretion. A library Host is a required deployment binding, not automatically a parent regulatory actor. Generic chains, control flags and role selection do not import another product's metasystem into this repository.

## S1 — Operations

- State: A
- Function: execute an authored operational prompt using model-selected tool actions and returned observations.
- Disturbance / variety regulated: unknown external information and tool outcomes in a prompt's bounded task.
- Decisive decision or feedback right: choose offered tools/arguments and whether to continue or return an answer.
- Decision owner: the model bound to the active prompt role.
- Supporting / enforcement mechanisms: Engine/Lua state machine, effect driver, inference broker, Pack registry, tool limits and recorder.
- Closure path: models.loop returns model tool requests to the first-party executor and appends observations for later rounds; final content becomes the run result.
- Boundary reachability: the library exposes Harness::run and models.loop; the supplied research_person prompt wires web tools and iterative model work. A Host supplies documented broker/timer/configuration bindings, rather than implementing the agent loop.
- Why this is / is not agent-owned: the engine's deterministic stepping is support: replacing the model with no decision-maker would not select the research actions. The offline greeting example alone is not the positive witness.
- Evidence: [shipped research prompt](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/prompts/research-person.md), [models.loop adapter](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/lua/src/models_loop.rs), [models.loop state machine](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/lua/src/models_loop/machine.rs), [effect loop](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/effect_loop.rs), [gateway broker](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-gateway-client/README.md)
- Basis: structural.
- Confidence: high.
- Caveats: library deployment requires a Host, inference service and installed Packs. Source inspection does not assert a separately shipped end-user UI or a live provider test.

## S2 — Coordination

- State: —
- Function: no supplied function-specific regulation of interference between distinct operational cells.
- Disturbance / variety regulated: parallel chains, effects and shared VFS operations could contend, but the supplied mechanisms regulate execution mechanics.
- Decisive decision or feedback right: no installed inter-S1 disturbance-response decision/feedback path established.
- Decision owner: developer-authored scheduling and host policy; no established S2 actor.
- Supporting / enforcement mechanisms: oldest-first tool-call cap, synchronous VFS operations, per-execution stores and generic chains.
- Closure path: effects resume the requesting chain; this is ordinary execution correlation, not a supplied inter-unit conflict-settlement loop.
- Why this is / is not agent-owned: multiple futures/chains and ordered file operations alone do not establish S2 or justify C.
- Evidence: [effect loop](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/effect_loop.rs), [runtime boundary](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/runtime/README.md), [RunSetup](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/setup.rs), [shipped research prompt](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/prompts/research-person.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: Bounded source-based absence; custom Host/prompt organizations and external Runvil products are not credited.

### Absence scope

- Surfaces inspected: runner effect scheduling, Engine chains/stores, host setup, shipped prompts and VFS APIs.
- Plausible first-party paths checked: tool-call queue fairness, VFS serialization, nested execute and isolated stores as possible anti-interference paths.
- Why no material first-party path remains: no shipped relation identifies distinct operational S1 units and a concrete inter-unit conflict with a corresponding feedback policy; generic sequencing/isolation cannot donate the missing function.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system resource/commitment regulation path supplied.
- Disturbance / variety regulated: per-run limits and external interruption, rather than current whole-system bargaining or intervention.
- Decisive decision or feedback right: no first-party current-control actor selects portfolio priorities or resource reallocations from a whole-system view.
- Decision owner: Host author/operator sets limits and sends messages; that extensibility alone is not a closed parent S3 mode.
- Supporting / enforcement mechanisms: RunLimits, max_tool_calls_in_flight, RunControl send/stop/cancel and recorded events.
- Closure path: a stop/cancel is enforced in one run; no packaged observer→current-control judgment→returned whole-system intervention is supplied.
- Why this is / is not agent-owned: a kill/steer API and performance records are support, not proof of S3 ownership.
- Evidence: [RunSetup](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/setup.rs), [Harness and RunControl](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/harness.rs), [effect loop](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/effect_loop.rs), [recorder interface](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/recorder.rs)
- Basis: structural.
- Confidence: medium-high.
- Caveats: Bounded source-based absence; custom Host/prompt organizations and external Runvil products are not credited.

### Absence scope

- Surfaces inspected: RunSetup, RunControl, effect loop, reporting/recorder, Host API and sample launches.
- Plausible first-party paths checked: run steering, caps, per-run reports, model-role binding and host user-inbox mode.
- Why no material first-party path remains: no function-specific supervisor with a whole-system operational view and discretionary resource/commitment control is wired in; a custom external Host might add one, but generic controls do not establish C/P.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit path of the runtime's operational claims supplied.
- Disturbance / variety regulated: run fidelity is observable through records and deterministic tests, without a packaged independent claim challenge.
- Decisive decision or feedback right: no audit-specific evidence judgment and corrective return.
- Decision owner: not established.
- Supporting / enforcement mechanisms: event/effect/answer recording, typed receipts, deterministic replayability and tests.
- Closure path: records report the same production execution; no distinct auditor feeds findings into subsequent control.
- Why this is / is not agent-owned: recording every effect and testing the engine do not create complementary S3* judgment.
- Evidence: [recorder interface](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/recorder.rs), [effect loop](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/effect_loop.rs), [runtime boundary](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/runtime/README.md)
- Basis: structural.
- Confidence: medium-high.
- Caveats: Bounded source-based absence; custom Host/prompt organizations and external Runvil products are not credited.

### Absence scope

- Surfaces inspected: recorder interface, driver, report/result types, public API, tests and shipped prompts.
- Plausible first-party paths checked: event provenance/replay, refusal reporting and model/tool records as possible alternative evidence surfaces.
- Why no material first-party path remains: no function-specific audit actor/constructor selects complementary raw evidence and routes a claim-relative judgment to an operational control owner; another tool prompt could be authored but is not supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied external/prospective adaptation loop for the harness's current capability.
- Disturbance / variety regulated: research_person senses the external web to answer its task; this is the product's S1 outcome.
- Decisive decision or feedback right: no prospective harness-adaptation option judgment with return into present capability.
- Decision owner: prompt/Host author selects models and Packs; model chooses operational search, not an established S4 decision.
- Supporting / enforcement mechanisms: web tools, model-role requirements, models.use, plugin loading and context compaction.
- Closure path: research facts return as a summary; static model bindings and compaction do not feed prospective capability options into current control.
- Why this is / is not agent-owned: external sensing alone, or changing the model by authored Lua, does not establish S4.
- Evidence: [shipped research prompt](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/prompts/research-person.md), [role selection example](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/prompts/analyst-example.md), [RunSetup](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/setup.rs), [models.loop adapter](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/lua/src/models_loop.rs)
- Basis: structural.
- Confidence: medium-high.
- Caveats: Bounded source-based absence; custom Host/prompt organizations and external Runvil products are not credited.

### Absence scope

- Surfaces inspected: shipped prompts, model binding/resolution, loop/compaction interfaces, Host/plugin setup and gateway boundary.
- Plausible first-party paths checked: web research, stronger-model role selection, compactor callbacks and external plugin replacement.
- Why no material first-party path remains: the source supplies information-task execution and generic configuration, without an external/future distinction→adaptation options→current-capability decision loop; no qualifying parent adaptation return is wired.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure path supplied.
- Disturbance / variety regulated: tool/file permissions and scope constraints regulate ordinary execution.
- Decisive decision or feedback right: no identity/policy escalation to legitimate ultimate authority with a returned governing resolution.
- Decision owner: Host/developer configuration supplies static scope and VFS policies; no established S5 owner.
- Supporting / enforcement mechanisms: frozen tool offers, Policy trait, workspace access, has_user inbox and cancellation.
- Closure path: allow/deny, user messages and run stops affect task execution; no identity/ultimate-policy transaction closes.
- Why this is / is not agent-owned: a policy interface and user input are not themselves S5.
- Evidence: [VFS Policy](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil-internal/vfs/src/traits/policy.rs), [public Harness/Host API](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/runvil/src/lib.rs), [RunSetup](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/setup.rs), [Harness and RunControl](https://github.com/cppalliance/runvil-harness/blob/ee199e3ae04366e02c61488c096f2981c057ff0b/crates/harness-internal/runner/src/harness.rs)
- Basis: structural.
- Confidence: medium-high.
- Caveats: Bounded source-based absence; custom Host/prompt organizations and external Runvil products are not credited.

### Absence scope

- Surfaces inspected: VFS policy/access, frozen tool scopes, prompt/model requirements, Host user mode, control API and contribution/CI boundary.
- Plausible first-party paths checked: runtime file verdicts, user inbox, host instructions and cancellation as possible parent-policy returns.
- Why no material first-party path remains: none identifies an ultimate-policy issue, legitimate decision-holder and authoritative returned policy within the distributed library runtime; maintainers governing the source repository are outside this boundary.

## Distributed OSS parent arrangement

Maintainers govern the repository and Hosts may have their own governance. No source-visible project-recursion parent S3/S4/S5 loop is part of the assessed embedded runtime.

## Self-hosted and non-human modes

A Host may be automated or operator-driven and may enable a user inbox. Those bindings are supported; function-specific parent control, adaptation and identity loops must still be supplied separately.

## Recursion

Nested execute creates chains and local stores, not evidence of recursively viable units.

## Variety and escalation

Model/tool decisions absorb task-specific variety; frozen offers, limits and VFS checks attenuate actions. Failures/refusals become recorded results; recorder refusal is distinct from a normal completed run. Cancellation and errors do not themselves establish algedonic authority or a VSM function.

## Evidence gaps

Complete pinned tree inventoried and implementation/README/prompt/API/test paths inspected. No Rust build, live gateway, model or tool-service execution was used; no performance or independent-secondary-review claim is made.
