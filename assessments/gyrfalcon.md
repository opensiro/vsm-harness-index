---
harness_id: gyrfalcon
project_name: Gyrfalcon
repository: https://github.com/cargopete/gyrfalcon
review_ref: 090615a2f13a062fd91896950106aeb505376c55
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gyrfalcon

## Review boundary

- System in focus: the first-party Gyrfalcon terminal coding runtime at frozen revision `090615a2f13a062fd91896950106aeb505376c55`, including its single model session, act-observe loop, built-in workspace/process/Rust tools, approval policy, OS sandbox, append-only session log, resumable provider-native conversation state, deterministic context-budget handling and supported interactive/one-shot CLI surfaces.
- Purpose and identity: take a user's Rust software-engineering request, let one model-backed coding agent inspect and modify one workspace through a bounded first-party tool surface, return tool evidence into the same conversation, and report the resulting answer or changes under explicit approval/sandbox constraints.
- Relevant environment: user submissions, workspace files and Cargo state, compiler/test/process results, provider/model responses, provider context-window/token reports, approval decisions, OS sandbox behavior, persisted session state/logs and static user/project configuration.
- Standard-distribution boundary: shipped `gyr` runtime and installed crates that construct the agent, provider session, built-in tool set, approval/sandbox enforcement, session persistence, context-budget handling and interactive/one-shot operation. Hosted/self-hosted model endpoints, operating-system primitives, Cargo/compiler binaries and external repositories are dependencies and cannot donate VSM ownership.
- Credited operating / distribution surfaces: `README.md`; `crates/gyr-core/`; `crates/gyr-cli/`; `crates/gyr-model/`; `crates/gyr-tools/`; `crates/gyr-exec/`; `crates/gyr-rust/`; `crates/gyr-sandbox/`; built-in prompt/configuration and resume/session paths; the runtime tool construction exported from `crates/gyr-eval/src/runner.rs` because the executable intentionally shares that first-party tool-definition path.
- Adjacent first-party surfaces excluded from ownership: `evals/`, `crates/gyr-eval` case execution/metrics beyond the shared runtime tool constructor, repository unit/integration tests, CI workflows, RFC development experiments, and the withdrawn diagnostic-gate experiment. These may corroborate runtime behavior or explain design decisions but are not credited as live organizational owners merely because they are first-party.
- First-party operating / deployment modes considered: interactive `gyr`, one-shot `gyr run`, resumed sessions, read-only mode, interactive approvals, explicit allow-all mode, workspace sandbox and explicit unsandboxed mode, supported provider/model selections and static user/project configuration layers.
- Recursion level: one Gyrfalcon coding session over one workspace is the assessed viable-unit candidate. The reviewed standard runtime constructs one operational coding agent; provider adapters, tools, compiler/processes and the human approver are supporting actors/dependencies rather than peer operational S1 units.
- Reviewed revision: `090615a2f13a062fd91896950106aeb505376c55`.
- Observation date: 2026-10-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Gyrfalcon is a Rust-first terminal coding agent centered on one provider-owned model session and a normalized event stream. The core `Agent` repeatedly asks the selected model for the next turn, collects tool calls, classifies each call, applies an approval policy, executes allowed tools and returns each tool result under its original call ID. The model then chooses the next action until it ends the turn, refuses, is cancelled or reaches the configured model-turn limit.

The standard runtime exposes workspace read/search/list/apply-patch tools, process execution and a structured Cargo tool. The CLI deliberately obtains this tool set from the same first-party constructor used by the eval harness so the shipped executable and measured tool surface cannot drift. The diagnostic gate remains implemented and documented but is deliberately absent from that standard tool constructor after ablations found no runtime benefit.

Interactive operation adds a line-based shell, per-call approval, session status, cancellation and persisted provider-native conversation state. Read-only and allow-all approval modes change whether mutations/processes are permitted, but they do not add another autonomous organizational actor. Context pressure is handled deterministically: reported token use can trigger a warning and, for providers with local history support, elision of older tool-result contents. Model, sandbox, approval and related settings are selected from CLI/user/project configuration rather than being autonomously adapted by a metasystem actor.

The repository also ships an eval corpus and records experimental design findings. That surface is development/evaluation infrastructure: it can compare models or tool surfaces across runs, but the shipped coding session does not consume those corpus findings as an autonomous decision loop that changes its future organizational capability.

## Operational model

The operational outcome is one answered or modified Rust workspace request. The sole material S1 unit in the standard runtime is the active model-backed coding agent: it chooses which files to inspect, which tool calls to make, what edits to propose, which compiler/process evidence to request and when to stop. First-party runtime code constrains the available actions, approval boundary, workspace fence, sandbox and turn budget, but those mechanisms do not choose the substantive implementation.

The human operator may approve or deny individual mutating/process calls, cancel a turn, select a model and configure static runtime settings. Those are important safety and operating controls, but no separate whole-system metasystem decision loop over multiple S1 units, independent complementary auditor, prospective adaptation owner or identity-policy authority is established inside the assessed runtime.

## S1 — Operations

- State: A
- Function: autonomously perform a Rust coding task by interpreting the user's request, gathering workspace/compiler evidence, choosing edits/tool actions and iterating on returned results until the agent ends the turn.
- Disturbance / variety regulated: unfamiliar repository structure, incomplete task information, type/compiler errors, failing commands, stale file state, refused tools, provider responses and local implementation choices.
- Decisive decision or feedback right: choose the next repository/tool action, interpret its returned evidence, decide what code/content change to make and decide when the operational response is complete.
- Decision owner: the active model-backed Gyrfalcon agent in the provider session.
- Supporting / enforcement mechanisms: `ToolSet`, exact/fingerprinted patching, approval policies, workspace fencing, OS sandboxing, bounded model turns, provider adapters, Cargo/process tools, session logging, resumable state and deterministic context elision.
- Closure path: user request → model selects workspace/tool action → first-party runtime classifies/permits/executes it → result returns to the same provider session → model revises the plan or implementation → further actions/results continue until the model ends the turn.
- Boundary reachability: both the standard interactive `gyr` path and `gyr run` call the same `prepare` path that constructs `Agent` with the standard tool set, provider session, approval policy and session sink, then invokes the agent loop directly.
- Why this is / is not agent-owned: runtime policy and sandbox code constrain what can happen, but removing the model removes the open-ended coding judgments; the deterministic layers do not independently select implementation edits or interpret task evidence.
- Evidence: [README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/README.md); [crates/gyr-core/src/lib.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-core/src/lib.rs); [crates/gyr-cli/src/main.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/main.rs); [crates/gyr-eval/src/runner.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-eval/src/runner.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: mutating/process actions may require human approval in the default interactive mode, but the approval decision constrains execution rather than supplying the substantive coding decision; read-only and allow-all are alternate supported policy modes over the same agent loop.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the reviewed session boundary.
- Disturbance / variety regulated: not applicable; the standard runtime does not construct multiple operational S1 units whose interactions require attenuation.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sequential model turns, tool-call settlement, workspace fencing, approval and sandbox logic coordinate components of one S1 loop but do not coordinate distinct operational S1 units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the architecture explicitly lists multi-agent orchestration as a non-goal, and the standard runtime constructs one `Agent` over one model session rather than peer operational agents.
- Evidence: [docs/rfcs/RFC-0001-architecture.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/docs/rfcs/RFC-0001-architecture.md); [crates/gyr-core/src/lib.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-core/src/lib.rs); [crates/gyr-cli/src/main.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/main.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: provider/tool/runtime components cooperate inside one coding loop; component sequencing is not promoted to S2 without distinct S1 units and a concrete inter-S1 disturbance.

### Absence scope

- Surfaces inspected: architecture RFC, core agent loop, CLI session/runtime construction, standard tool constructor, workspace/process/Rust tools, approvals, sandbox, persistence/resume, configuration and eval/runtime wiring.
- Plausible first-party paths checked: tool-call batching, provider adapters, multiple tool runtimes, eval runner, resumed sessions and any documented delegation/orchestration path.
- Why no material first-party path remains: all inspected runtime paths converge on one model-backed coding agent per session; multi-agent orchestration is explicitly outside the MVP and no first-party peer-S1 topology or interference-feedback loop is shipped.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function is established at the declared recursion.
- Disturbance / variety regulated: no distinct whole-session resource/commitment/prioritization disturbance is placed under a metasystem decision right; current execution is bounded by static/deterministic limits and local operator controls.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: model-turn limit, approval policy, sandbox, Ctrl-C cancellation, `/status`, per-session model selection and deterministic context-budget thresholds constrain or expose the single S1 but do not constitute a separate inside-and-now control owner.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the core agent itself consumes tool evidence for its operational task, while deterministic limits and human stop/approval actions regulate local execution. No separate actor receives a whole-system current view and makes resource/commitment/prioritization decisions over the assessed organization.
- Evidence: [README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/README.md); [crates/gyr-cli/src/session.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/session.rs); [crates/gyr-core/src/lib.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-core/src/lib.rs); [docs/rfcs/RFC-0013-context-budget.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/docs/rfcs/RFC-0013-context-budget.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: operator approval/cancellation and deterministic context elision are real control mechanisms, but Methodology 0.3.6 requires a whole-system current decision loop rather than generic operator UI, fixed budgets or termination enforcement.

### Absence scope

- Surfaces inspected: interactive session commands/status, cancellation, approval modes, model-turn limits, context-budget handling, provider usage reporting, session persistence and one-shot execution.
- Plausible first-party paths checked: `/status`, Ctrl-C, per-call approval, `max_turns`, token-window warning/elision, model choice and sandbox/configuration.
- Why no material first-party path remains: none of these surfaces creates a distinct current-control actor with a whole-organization view and a returned resource/commitment/prioritization decision; they are local intervention or deterministic enforcement around one S1.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is supplied in the standard runtime.
- Disturbance / variety regulated: no separate first-party channel independently challenges the coding agent's ordinary claims/results and returns findings into corrective operation.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the same agent can call Cargo/process tools and inspect compiler/test evidence; the withdrawn diagnostic gate can compute deterministic progress verdicts but is deliberately absent from the standard tool set; the eval corpus judges development/evaluation runs outside the assessed live session.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: compiler/tool feedback is available through the ordinary S1 observation path, not through an independent complementary auditor. The eval harness and repository CI are adjacent validation systems rather than standard-distribution runtime owners.
- Evidence: [README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/README.md); [crates/gyr-eval/src/runner.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-eval/src/runner.rs); [docs/rfcs/RFC-0011-diagnostic-gate.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/docs/rfcs/RFC-0011-diagnostic-gate.md); [evals/README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/evals/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: successful Cargo/tests can verify aspects of an implementation, but verification evidence used by the same ordinary agent does not by itself establish S3* independence.

### Absence scope

- Surfaces inspected: standard tool constructor, Cargo/process tool paths, diagnostic-gate code/RFC, eval harness, session log/replay and CI/test-adjacent documentation.
- Plausible first-party paths checked: separate reviewer/verifier agent, authorship-independent audit session, diagnostic gate, eval assertions/metrics, replay and repository CI.
- Why no material first-party path remains: no separate reviewer/auditor is constructed by the shipped coding session; the gate is explicitly not offered, and eval/CI/replay surfaces are adjacent development/inspection mechanisms rather than an independent runtime audit loop returning findings to S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop is established in the shipped runtime.
- Disturbance / variety regulated: external model/tool-performance changes and future capability choices are studied in repository eval/RFC work, but no live runtime actor owns their prospective interpretation and adaptation.
- Decisive decision or feedback right: none established inside the assessed runtime.
- Decision owner: none established.
- Supporting / enforcement mechanisms: static model catalogue, user/project configuration, provider profiles, context-window metadata and the development eval corpus can inform a human or maintainer but do not autonomously close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the coding agent operates against the model/tool/configuration already selected for the current session. Measured model/tool comparisons remain in adjacent eval/RFC artifacts and are not consumed by a first-party runtime adaptation actor that changes future capability.
- Evidence: [README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/README.md); [crates/gyr-cli/src/main.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/main.rs); [crates/gyr-cli/src/config.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/config.rs); [docs/rfcs/RFC-0012-eval-harness.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/docs/rfcs/RFC-0012-eval-harness.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainers can use eval findings to evolve the project and users can choose another model/configuration, but those external human development/configuration decisions are not a closed first-party S4 mode at the assessed session boundary.

### Absence scope

- Surfaces inspected: model catalogue/selection, user and project configuration, provider profiles, eval harness/corpus, RFC measurement record, context-budget adaptation and resumed-session state.
- Plausible first-party paths checked: autonomous model switching, capability tuning, tool-surface adaptation, learned future policy/configuration, parent S4 configuration loop and runtime ingestion of eval outcomes.
- Why no material first-party path remains: future-facing measurements are retained for maintainers/users, while shipped sessions consume static selections and deterministic thresholds; no first-party actor turns external/future evidence into an adaptation decision that is returned into subsequent runtime capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established at the reviewed session boundary.
- Disturbance / variety regulated: no runtime identity or ultimate-policy issue is placed under an authoritative S5 decision loop.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: developer-authored system prompt, approval policy, sandbox rules, project/user configuration restrictions and tool schemas define operating constraints but do not provide a runtime owner that can legitimately establish or revise Gyrfalcon's identity/ultimate policy.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent follows the shipped prompt and runtime policy; it does not own authority to redefine those governing principles. Human per-call approval and static configuration likewise do not form an identity/policy decision-return loop.
- Evidence: [crates/gyr-core/src/prompt.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-core/src/prompt.rs); [README.md](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/README.md); [crates/gyr-core/src/approval.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-core/src/approval.rs); [crates/gyr-cli/src/config.rs](https://github.com/cargopete/gyrfalcon/blob/090615a2f13a062fd91896950106aeb505376c55/crates/gyr-cli/src/config.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: repository maintainers own project development policy outside the runtime boundary, and the operator owns local permission choices; neither is promoted to S5 without a first-party identity/ultimate-policy issue, authoritative decision and return-to-operation loop at the declared recursion.

### Absence scope

- Surfaces inspected: system prompt, approval policies, sandbox/configuration restrictions, CLI settings, project config, session commands, RFC architecture and repository governance-adjacent documentation.
- Plausible first-party paths checked: autonomous prompt/policy revision, constitution/governance artifact, parent-governed identity changes, project-config authority and operator approval modes.
- Why no material first-party path remains: the governing prompt/policies are static developer-authored inputs to operation and cannot be authoritatively revised by the assessed runtime; project config and approvals alter local execution settings rather than closing an identity/ultimate-policy feedback loop.

## Distributed OSS parent arrangement

Gyrfalcon is open source, but the assessed organization is one local coding session rather than the maintainer/contributor project organization. Repository maintainers and independent contributors are therefore not inferred as an organization-level parent mode for S3, S4 or S5. The reviewed runtime exposes local operator choices, but none establishes the function-specific parent closure required for a positive parent state.

## Self-hosted and non-human modes

Gyrfalcon supports self-hosted Qwen-compatible endpoints as well as hosted providers and exposes supervised operator modes through approvals, read-only operation, cancellation and static configuration. These materially constrain the operational S1 but do not establish complete parent S3/S4/S5 loops under Methodology 0.3.6.

## Recursion

One interactive or one-shot coding session is the viable-unit candidate. The model-backed agent is the sole material operational S1. Provider transport, tool runtimes, Cargo/processes, sandbox and approval machinery are lower-level/supporting components. The human operator is an environmental/parent actor for permission and configuration choices, but no positive parent-mode metasystem closure is established at this recursion.

## Variety and escalation

Operational variety is handled inside S1 through workspace inspection, compiler/process feedback, exact patching, provider turns and ordinary tool-result iteration. A refused action returns to the same model as tool evidence so it can choose another operational path. Hard boundaries include model-turn limits, sandboxing, approval and deterministic context elision. Ctrl-C and failures can terminate a turn. These mechanisms bound or redirect S1 variety; they do not create distinct S2/S3/S3*/S4/S5 owners.

## Evidence gaps

No `?` state is required. The frozen source is explicit about the single-agent product boundary, standard tool construction, operator/session controls, withdrawn gate and eval-development separation. That boundary is broad enough to establish S1 positively and to support documented no-material-path conclusions for S2, S3, S3*, S4 and S5 without relying on adjacent CI/eval/maintainer systems.
