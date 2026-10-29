---
harness_id: carry
project_name: Carry
repository: https://github.com/wiggzz/carry
review_ref: fd293547416818edd90a9667c31bd05498889569
reviewed_at: 2026-10-29
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

# Carry

## Review boundary

- System in focus: the first-party native Carry coding agent, with CLI/interactive/web modes; standalone context proxy considered as a separate supported service mode without borrowing its external client agent.
- Purpose and identity: perform repository tasks with model-directed shell actions and inspectable context retention.
- Relevant environment: user repository/shell, model API or subscription endpoint, external MCP tools, prompt-cache behavior and local session storage.
- Standard-distribution boundary: src/main.rs, run.rs, context/core/protocol and supporting native UI/session/MCP code; proxy advice/history paths reviewed for boundary contrast.
- Credited operating / distribution surfaces: native run_loop, first-party coding prompt, parsed shell/finish actions and result-to-history feedback.
- Adjacent first-party surfaces excluded from ownership: SWE-bench/FrontierHarness runners, evaluator containers, benchmark claims and infrastructure, repository AGENTS/CI/release and tests. Their independent graders do not become a native runtime S3* actor.
- First-party operating / deployment modes considered: native one-shot, terminal interactive, browser steering/resume; local context/economic retention policies; separately operated OpenAI Responses context proxy.
- Recursion level: one native coding session and its local tool/context regulation.
- Reviewed revision: fd293547416818edd90a9667c31bd05498889569
- Observation date: 2026-10-29
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Rust CLI assembles a model backend and native RunConfig. run_loop sends the current context, parses a shell or finish action, executes the shell under timeout/process-group handling, stores observations and model retention signals, and loops. Session checkpoints, traces and final patches support inspection/resume. The actor can protect/release context and preserve concise memories; deterministic economics choose admissible rewrites. Interactive/web input is queued into subsequent turns. A separate proxy consumes external client histories and fresh reviewer advice, validates retention authorization and selects disposable request projections. The proxy's external primary agent is not a first-party operational actor of that service. Benchmark/evaluator orchestration is an adjacent research surface.

## Operational model

Native model calls own task-specific shell choices, completion and context annotations. Runtime economics, guards, storage and timeout enforce fixed developer/operator constraints. Context reviewer advice decides relevance/retention within that mechanism rather than auditing the truth of a completed coding claim. Standard native S1 is established without treating a proxy client, benchmark grader or optional external MCP agent as internal ownership.

## S1 — Operations

- State: A
- Function: carry out user coding objectives through iterative repository actions.
- Disturbance / variety regulated: unknown repository state, test failures, shell errors and changing user requests.
- Decisive decision or feedback right: choose commands, interpret their results and finish or continue the task.
- Decision owner: model-backed native Carry actor.
- Supporting / enforcement mechanisms: OpenAI-compatible backend, typed shell/finish protocol, process-group timeout, context/checkpoint/log and user-input channels.
- Closure path: Shell result becomes function_call_output and context_state.add_tool; later backend.step consumes that history. Finish returns an answer; new interactive input can start another turn.
- Boundary reachability: native main/run_interactive/run_with_shutdown directly use run_loop with the supplied coding prompt and action schema; no external agent loop needs to be composed.
- Why this is / is not agent-owned: removing model inference leaves execution/storage/economic machinery but no task-specific command/repair decisions.
- Evidence: [src/run.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/run.rs); [src/main.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/main.rs); [src/protocol.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/protocol.rs); [docs/context-policy.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/context-policy.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

## S2 — Coordination

- State: —
- Function: No supplied inter-S1 coordination path at the declared operating boundary.
- Disturbance / variety regulated: conflicting independent operational units.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: none established; model/local-runtime/operator roles remain as described.
- Supporting / enforcement mechanisms: native action loop, web/interactive queues, proxy branch/history matching and in-flight owner pins.
- Closure path: No qualifying higher-function closure; inspected serial shell actions, queued user input and one in-flight review per paid owner remain local operational/support paths.
- Why this is / is not agent-owned: Function-first positive and parent options were examined; deterministic enforcement or generic user control cannot create the missing function.
- Evidence: [src/run.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/run.rs); [docs/proxy-fork-continuity.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/proxy-fork-continuity.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: native action loop, web/interactive queues, proxy branch/history matching and in-flight owner pins.
- Plausible first-party paths checked: serial shell actions, queued user input and one in-flight review per paid owner.
- Why no material first-party path remains: These preserve one actor's transcript and request settlement. No first-party relation regulates concrete interference among separate autonomous S1 cells; proxy client agents are external, and branch identity is data ancestry rather than operational coordination.

## S3 — Inside-and-now control

- State: —
- Function: No supplied whole-system inside-and-now control path at the declared operating boundary.
- Disturbance / variety regulated: binding cross-operation resources/commitments.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: none established; model/local-runtime/operator roles remain as described.
- Supporting / enforcement mechanisms: native usage/context metrics, economic compaction planner, limits/shutdown, proxy capacity/admission and operator options.
- Closure path: No qualifying higher-function closure; inspected context protection/removal, prompt-cache pricing, hard-cap refusal and session stop/steer remain local operational/support paths.
- Why this is / is not agent-owned: Function-first positive and parent options were examined; deterministic enforcement or generic user control cannot create the missing function.
- Evidence: [docs/context-policy.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/context-policy.md); [src/core.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/core.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: native usage/context metrics, economic compaction planner, limits/shutdown, proxy capacity/admission and operator options.
- Plausible first-party paths checked: context protection/removal, prompt-cache pricing, hard-cap refusal and session stop/steer.
- Why no material first-party path remains: These govern local task context and service capacity by preselected policies, not an evidenced whole-operational portfolio decision actor. Cost projection and admission enforce choices; neither the native model nor the human UI supplies a separate whole-system resource-accountability loop.

## S3* — Complementary audit

- State: —
- Function: No supplied complementary independent operational audit path at the declared operating boundary.
- Disturbance / variety regulated: unreliable coding-completion or management claims.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: none established; model/local-runtime/operator roles remain as described.
- Supporting / enforcement mechanisms: native traces/retention_audit, original-history proxy advice, reviewer freshness and adjacent evaluator architecture.
- Closure path: No qualifying higher-function closure; inspected fresh-context retention review, shell/test evidence, logged rewrite reasons and benchmark grading remain local operational/support paths.
- Why this is / is not agent-owned: Function-first positive and parent options were examined; deterministic enforcement or generic user control cannot create the missing function.
- Evidence: [docs/proxy-fork-continuity.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/proxy-fork-continuity.md); [src/proxy_advice.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/proxy_advice.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: native traces/retention_audit, original-history proxy advice, reviewer freshness and adjacent evaluator architecture.
- Plausible first-party paths checked: fresh-context retention review, shell/test evidence, logged rewrite reasons and benchmark grading.
- Why no material first-party path remains: The supplied reviewer judges what history may be omitted, not independent operational truth or a current-control report. Traces are observation; native verification remains S1. External research graders are outside the runtime boundary. No complementary operational audit and corrective-control ownership path is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied outside-and-then capability adaptation path at the declared operating boundary.
- Disturbance / variety regulated: future external distinctions requiring changed capability.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: none established; model/local-runtime/operator roles remain as described.
- Supporting / enforcement mechanisms: context economic horizon/rollouts, saved memories, model catalog/discovery and benchmark/maintainer surfaces.
- Closure path: No qualifying higher-function closure; inspected future request cost estimates, model retention advice, subscription catalog and manual model/config changes remain local operational/support paths.
- Why this is / is not agent-owned: Function-first positive and parent options were examined; deterministic enforcement or generic user control cannot create the missing function.
- Evidence: [docs/context-policy.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/context-policy.md); [src/models.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/models.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: context economic horizon/rollouts, saved memories, model catalog/discovery and benchmark/maintainer surfaces.
- Plausible first-party paths checked: future request cost estimates, model retention advice, subscription catalog and manual model/config changes.
- Why no material first-party path remains: Economic prospective horizons model internal context costs, not external adaptation options in a dialogue with current capability. Discovery exposes available model metadata without an agent/parent selection-adoption loop; memory and adjacent benchmark development do not supply that loop.

## S5 — Policy and identity

- State: —
- Function: No supplied runtime identity/ultimate-policy closure path at the declared operating boundary.
- Disturbance / variety regulated: ultimate-purpose or policy tensions.
- Decisive decision or feedback right: No qualifying function-specific decisive right established.
- Decision owner: none established; model/local-runtime/operator roles remain as described.
- Supporting / enforcement mechanisms: coding/system prompt, CLI/auth/limits, protected human history, proxy authorization and contributor instructions.
- Closure path: No qualifying higher-function closure; inspected user steering, hard retention protections, authentication, config and system directions remain local operational/support paths.
- Why this is / is not agent-owned: Function-first positive and parent options were examined; deterministic enforcement or generic user control cannot create the missing function.
- Evidence: [src/run.rs](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/src/run.rs); [docs/proxy-fork-continuity.md](https://github.com/wiggzz/carry/blob/fd293547416818edd90a9667c31bd05498889569/docs/proxy-fork-continuity.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: coding/system prompt, CLI/auth/limits, protected human history, proxy authorization and contributor instructions.
- Plausible first-party paths checked: user steering, hard retention protections, authentication, config and system directions.
- Why no material first-party path remains: These are static authorization/retention constraints or ordinary task instructions. No identity-policy issue is routed to legitimate ultimate authority with a returned governing settlement in native or proxy modes; contributor governance remains adjacent.

## Distributed OSS parent arrangement

User task input, steering, auth and policy flags are first-party operator surfaces, but no function-specific parent S3/S4/S5 decision-and-return mode is established by them. OSS maintainer decisions stay outside native session ownership.

## Self-hosted and non-human modes

The local native CLI/web UI and separate localhost proxy are supported. Native agent provides S1; proxy-only deployment does not inherit the external client's coding loop. No live account/provider, proxy load or benchmark run was performed.

## Recursion

History forks, request branches and context reviewers are technical execution/data arrangements; no recursively viable child organization is established.

## Variety and escalation

Model retention choices preserve task evidence while economics manage cache/size tradeoffs. Shell timeout/errors and user steering return to the actor. Proxy pinning/advice validation prevents unauthorized history omission and stale advice; these guards do not select organizational strategy or ultimate identity.

## Evidence gaps

Source-only assessment makes no benchmark, cost-saving or task-success claim. External clients, private sessions and model-provider implementation are excluded. Fresh context reviewers and retention_audit traces concern history selection, not independent operational audit. The inspected native/proxy entry paths expose no specific unresolved higher-function path at this boundary.
