---
harness_id: nvidia-nemo-guardrails
project_name: NVIDIA NeMo Guardrails
repository: https://github.com/NVIDIA-NeMo/Guardrails
review_ref: 0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1
reviewed_at: 2026-10-15
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

# NVIDIA NeMo Guardrails

## Review boundary

- System in focus: the published first-party `nemoguardrails` programmable conversation/agent guardrail runtime: its **Colang/LLMRails operating mode**, its supported alternative `Guardrails`/IORails mode, and shipped Python/server action and policy enforcement entry points. The package governs an LLM-powered conversational process; it does not own arbitrary applications that embed it.
- Purpose and identity: enable a developer/operator to construct and execute policy-constrained conversational flows, tool/action gates and conditional responses around configured LLMs.
- Relevant environment: user messages, LLM completions, registered local action functions, optional external tool/LLM engines, attached knowledge/retrieval, and host applications. External inference endpoints are dependencies and their internal organization is not credited.
- Standard-distribution boundary: Apache-2.0 `nemoguardrails` Python distribution at its frozen **develop** commit, which declares `0.25.0.dev0`; this is a development revision, *not* an asserted released version. `Guardrails` can choose IORails or fall back to `LLMRails` depending on config, while `LLMRails` remains a supported direct API.
- Credited operating / distribution surfaces: `LLMRails.generate_async/process_events_async` with Colang 1.0 / 2.x runtime and first-party LLM-generation/action dispatcher; configured `Guardrails`/IORails with input/output/tool rail guards and model call; supported Python API/server invocation, where packaged.
- Adjacent first-party surfaces excluded from ownership: docs, notebooks, standalone example bots/flows, evaluation and jailbreak benchmarks, model-training artifacts, repository test fixtures, CI, release/maintainer operations, and third-party host apps/agents integrating the library. External connected models/tools do not donate their independent organization.
- First-party operating / deployment modes considered: direct `LLMRails` Colang dialog generation and local actions; `Guardrails(config, use_iorails=False)` explicit fallback mode; default `Guardrails(config)` IORails mode for supported configs (including per-tool rails), and API/server use of the engines. These modes are not assumed behaviorally identical.
- Recursion level: one packaged guardrail-controlled conversational operation/runtime; concurrent user conversations, Colang subflows and multiple configured validators are *not* presumed organizational S1 subunits.
- Reviewed revision: `0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1` (live default `develop` pinned on 2026-10-15).
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The root [pyproject.toml](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/pyproject.toml) packages an executable Python framework. [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md) documents the `LLMRails(RailsConfig.from_path(...)).generate(...)` call, five rail types (input, dialog, retrieval, execution and output), registered Python actions, and Colang 1.x/2.x conversation programming. The actual [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py) initializes `RuntimeV1_0` or `RuntimeV2_x` from config, converts messages into events, runs the Colang interpreter, dispatches registered actions and converts resultant events into responses/tool calls. The v2 runtime [nemoguardrails/colang/v2_x/runtime/runtime.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/colang/v2_x/runtime/runtime.py) maintains active flow state, processes incoming events via `run_to_completion`, starts local actions, awaits action completion and feeds resulting events back into the same state machine. Agent-facing intent and next-step generation are implemented by [nemoguardrails/actions/llm/generation.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/actions/llm/generation.py) and [nemoguardrails/actions/v2_x/generation.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/actions/v2_x/generation.py): a configured LLM can supply substantive next conversational/action choices within the Colang-bounded flow.

An alternative newer wrapper [nemoguardrails/guardrails/guardrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/guardrails.py) selects `IORails` for eligible config or `LLMRails` when it cannot use IORails; per-tool IORails-only configurations deliberately fail rather than silently downgrade. [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py) runs configured input, output and tool-call/tool-result validators, including early block, rewrite and per-tool conditions. [nemoguardrails/guardrails/model_engine.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/model_engine.py) sends model requests to configured *external* inference engines. The supported direct `LLMRails` mode matters because the default IORails pathway alone could be only guardrail-wrapped completion, not the Colang autonomous operational loop.

Runtime/event state exists within conversations. Configured policy and flows originate with the developer/operator; the library interprets and enforces them. Model decisions are bounded by those rules. Multiple flows or checks can run without constituting multiple autonomous S1s. Tracing, evaluations, tests, server endpoints and historical logs are support/observation, not automatically separate supervisory functions.

## Operational model

Concrete protected operation: user message → configured rail/Colang event → model reasoning about intent or next step where configured → first-party conversation/action runtime dispatch → execution/result event → renewed state-machine transition → guarded response. This is a bounded model-driven operational closure when the supported Colang `LLMRails` mode is selected. In the alternative IORails-only mode, the ordinary operation may just be model invocation with guards and model tool-call *validation*; the external host may still own tool execution. The first-party S1 claim is **mode-specific**, not universal across every configuration.

A registered `actions.py` function can be user-authored; its internal cognitive or organizational choices are not credited as Guardrails S2–S5. A tool action returned to the external host is a request, not proof that Guardrails controls external execution. The user/developer is the source of configured normative constraints; that does not establish an S5 dispute-resolution/return mode.

## S1 — Operations

- State: A
- Function: a guarded LLM agent/conversational operation performs intent interpretation, conditional next-action selection, local action execution (when registered), continuation and response generation.
- Disturbance / variety regulated: changes in user utterances, dialogue context, permitted tool/action opportunities and tool/action results within a configured protected conversation.
- Decisive decision or feedback right: select the next conversational/action step from the model-supported flow and process the result into subsequent next-step/response events.
- Decision owner: the LLM agent actor operating inside the **first-party `LLMRails` Colang flow runtime**; external inference services calculate tokens, but first-party flow dispatch/continuation closes the bounded process. The runtime/developer constrain its choices.
- Supporting / enforcement mechanisms: Colang interpreter, active `State` and event queue, action dispatcher, hard rail checks, configured model adapters, async action completion, event/response serialization.
- Closure path: new user/event → model-backed intent/next step through generation actions → runtime `Start...Action` dispatch → `...ActionFinished`/updated context → `run_to_completion` → subsequent response/action.
- Boundary reachability: the public supported `LLMRails` Python API directly initializes its own Colang runtime and actions; `Guardrails(config,use_iorails=False)` also explicitly exposes it. This does not depend on evaluation fixtures, an adjacent agent harness or borrowed host action planner.
- Why this is / is not agent-owned: the configured model makes nontrivial discretionary conversational/next-step choices; the first-party runtime sequences and returns action results. Static Colang policy and rails are constraints, not themselves the agent actor. **IORails-only passthrough does not independently justify this claim**.
- Evidence: [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md); [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py); [nemoguardrails/colang/v2_x/runtime/runtime.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/colang/v2_x/runtime/runtime.py); [nemoguardrails/actions/llm/generation.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/actions/llm/generation.py); [nemoguardrails/guardrails/guardrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/guardrails.py).
- Basis: explicit source and supported API.
- Confidence: high for the direct Colang mode; no claim of S1 ownership by pure IORails middleware alone.
- Caveats: neither the external LLM provider nor developer-written tools donate their internal governance. Constrained scripted conversations without discretionary model action should not be read as agent-owned S1.

## S2 — Coordination

- State: —
- Function: no shipped first-party inter-S1 attenuation/feedback loop established at the declared protected-conversation recursion.
- Disturbance / variety regulated: potential overlap among Colang flows, concurrent rail validators and concurrent requests; these are workflow/validation concurrency, not evidenced conflict among distinct first-party operating S1 units.
- Decisive decision or feedback right: choose a resolution to concrete inter-S1 interference and return that choice to each S1's subsequent operations.
- Decision owner: no S2-specific owner established. The state machine and configured rail manager deterministically coordinate local stages/checks.
- Supporting / enforcement mechanisms: flow-state scheduling, event ordering, rail sequencing, parallel rail execution/cancellation and semaphores.
- Closure path: ordered/parallel checks constrain one local operation; no independently evidenced cross-S1 conflict attenuation/return is supplied at this boundary.
- Why this is / is not agent-owned: multiple rails, event heads, validators, local actions or sessions do not by themselves create autonomous operational units and their interference-control organization.
- Evidence: [nemoguardrails/colang/v2_x/runtime/runtime.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/colang/v2_x/runtime/runtime.py); [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py); [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a larger host system coordinating multiple guarded agents could show S2, but must be separately bounded and evidenced.

### Absence scope

- Surfaces inspected: Colang flow start/event scheduling, `LLMRails` event handling, per-request rail manager including parallel checks, supported packaging/API and registered actions.
- Plausible first-party paths checked: simultaneous active flows and local async actions; request-level parallel input/output/tool checks; externally hosted multiple guarded conversations.
- Why no material first-party path remains: the inspected facilities schedule/validate a protected conversation or unrelated requests, without a distinct first-party S1-unit population plus evidenced inter-S1 disturbance/attenuation/feedback at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: no shipped whole-system current-operational resource/commitment controller distinct from local safety enforcement is established.
- Disturbance / variety regulated: local request guard violation, model tool-call risk, action execution and per-flow state; not a whole current enterprise/agent organization with commitments and portfolio-level control.
- Decisive decision or feedback right: independently judge current priorities/resources/constraints across operating S1 units and return intervention.
- Decision owner: configured policy is developer/operator-authored; deterministic runtime evaluates and enforces per-request constraints, not an S3 owner at declared recursion.
- Supporting / enforcement mechanisms: `RailsManager` block/rewrite; tool guards; flow event caps; optional tracing and server routes.
- Closure path: a violation can block or rewrite *the same* request/tool call. There is no demonstrated shared whole-current system view → current organizational control decision → returned S1 regulation.
- Why this is / is not agent-owned: enforcing a previously authored rail or managing a dialog head is not substantive global current-control discretion.
- Evidence: [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py); [nemoguardrails/guardrails/guardrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/guardrails.py); [nemoguardrails/colang/v2_x/runtime/runtime.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/colang/v2_x/runtime/runtime.py); [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a separate parent application can aggregate guardrail incidents and act as S3, but that is not this package's owned operating loop.

### Absence scope

- Surfaces inspected: public `LLMRails`/IORails APIs, flow state/history, `RailsManager`, model/tool gate actions, server-facing execution and tracing.
- Plausible first-party paths checked: policy-level global governance through configured rails, per-tool risk gate aggregation, cross-dialog active state, runtime termination limits and operator review/reconfiguration.
- Why no material first-party path remains: the material shipped decisions are local allow/block/rewrite/execute/return, not a whole-current S1 operation/commitment visibility and first-party authoritative current-control feedback loop.

## S3* — Complementary audit

- State: —
- Function: no independent, complementary organizational corrective audit loop over the protected operation is established apart from normal in-band rail checks.
- Disturbance / variety regulated: unsafe model outputs, malicious inputs, undesired tools and protocol violations.
- Decisive decision or feedback right: independently inspect ordinary operations from a complementary evidence path, adjudicate a material finding and return correction to ongoing governance.
- Decision owner: configured rail/check implementations judge individual inline data; tests and evaluations are developer/CI surfaces, not an operating independent audit authority.
- Supporting / enforcement mechanisms: input/output/tool rails, optional LLM classifiers, logs, tracing, evaluation scripts and violation reports.
- Closure path: in-line rail decision blocks/modifies a request; test/trace evidence may reach an external operator. No first-party *complementary* independent audit judgment and returned organizational correction to its own S1/S3 is shown.
- Why this is / is not agent-owned: an additional safety model or checker can validate data while remaining part of normal execution; its mere separation from the main model is not complementary S3* independence/feedback.
- Evidence: [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py); [nemoguardrails/guardrails/iorails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/iorails.py); [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py); [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: a configured external monitoring/audit operator can use Guardrails results; no such separate first-party corrective owner is assumed.

### Absence scope

- Surfaces inspected: input/output/tool checks, telemetry/tracing and check/explain surfaces, repo `tests/`/benchmark/evaluation facilities, CLI/server invocation.
- Plausible first-party paths checked: independently evaluated rail blocks, model-based safety judges, asynchronous parallel rails, operational logs, independent post-hoc evaluation.
- Why no material first-party path remains: all checked safety decisions are part of the ordinary request path or exported telemetry/tests; no complementary independent audit owner with operational corrective-return loop is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped external-future environmental sensing and capability adaptation closed back into present Guardrails runtime.
- Disturbance / variety regulated: changes in attacks, provider behavior, threat patterns and future desired guardrails.
- Decisive decision or feedback right: originate future adaptation options from external intelligence and commit selected changes to live rules/capability.
- Decision owner: developers/operators author and update Colang/config/actions; no first-party prospective adaptation actor/controller established.
- Supporting / enforcement mechanisms: configurable rail flows, model/provider selection, custom action/filter registration, runtime `update_llm`, roadmap and examples.
- Closure path: a human may edit and reload config; none of the inspected standard modes continuously senses external threats, deliberates prospective choices and returns the decision to current runtime capability.
- Why this is / is not agent-owned: rule extensibility and external-model use are not adaptive S4; a threat-intelligence agent could be composed externally, not credited here.
- Evidence: [nemoguardrails/guardrails/guardrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/guardrails.py); [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py); [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md); [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: future model-based rail authoring or separate red-team pipeline would be a different supported integration/boundary if demonstrated.

### Absence scope

- Surfaces inspected: runtime/config loaders, rail registry and custom action API, model update hooks, development docs/examples, tests and CI threat-evaluation facilities.
- Plausible first-party paths checked: dynamic runtime config, guardrail feedback/logging, automatic rule evolution, model choice switching, threat scanning and developer release flow.
- Why no material first-party path remains: changes are fixed configured/reloaded policy or maintainer work; no executable first-party external sensing → prospective adaptation decision → return-to-current-capability owner/closure established.

## S5 — Policy and identity

- State: —
- Function: runtime enforces externally supplied behavioral rules but does not itself close ultimate organizational identity/policy disputes.
- Disturbance / variety regulated: unwanted topics, unsafe requests, tool permissions and prompt/output constraints.
- Decisive decision or feedback right: determine legitimate ultimate values/identity for the protected organization when conflict or escalation arises and return authoritative policy decision.
- Decision owner: host developer/operator supplies `RailsConfig` and business-specific rules. Local model judges may choose allow/block within these bounds but do not authoritatively adjudicate *ultimate policy*.
- Supporting / enforcement mechanisms: Colang config, system flows, guardrail policy evaluation, tool CEL/regex checks, allow/block/rewrite, server configuration.
- Closure path: loaded settings → request-time enforcement. No demonstrated identity-level matter → legitimate policy authority → new authoritative decision → returned updated operation path in supported first-party mode.
- Why this is / is not agent-owned: a safety constraint is not an ultimate-policy decision; human authoring and operator ability to change config are not sufficient for `P`.
- Evidence: [README.md](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/README.md); [nemoguardrails/guardrails/guardrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/guardrails.py); [nemoguardrails/guardrails/rails_manager.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/guardrails/rails_manager.py); [nemoguardrails/rails/llm/llmrails.py](https://github.com/NVIDIA-NeMo/Guardrails/blob/0e2efcb55a61ef3f7c875f55d54dc1bbc9ccc4a1/nemoguardrails/rails/llm/llmrails.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: specific host apps may build human escalation/policy governance on this enforcement substrate. Such ownership must be evaluated at their system boundary, not borrowed.

### Absence scope

- Surfaces inspected: configuration and Colang policy definitions, model and rail decisions, tool permissions, server/operator entry points, maintainer governance and tests.
- Plausible first-party paths checked: policy prompts, config reload, human-authored blocking rules, runtime-generated risk assessments, local tool-approval and response censorship.
- Why no material first-party path remains: these enforce preselected constraints or local action choices; no shipped first-party ultimate identity-authority dispute/return loop is identified.

## Distributed OSS parent arrangement

NeMo Guardrails' public maintainers own upstream source and releases, while downstream operators own configurations/LLM contracts for their deployed cells. Public contribution/release governance and ordinary runtime operator updates are not treated as one evidenced organization-wide S3/S4/S5 parent authority with shared control. No `(P)` modifier is claimed.

## Self-hosted and non-human modes

Running an embedded Python runtime or optional server does not itself change decisive governance ownership. The supported Colang agent mode is model-guided under developer-authored constraints; a separately deployed operator can reconfigure the package, but no specific complete current-control, future-adaptation or ultimate-policy parent loop has been demonstrated in this distribution. Neither the absence of a P mode nor the existence of external human users is treated as a maturity ranking.

## Recursion

One guardrail-mediated conversational execution boundary is the assessed recursion. Distinct model calls, Colang subflows, concurrent rail checks and local Python actions are subsystems, not automatically viable daughter organizations. A host product deploying many guardrailed agents may define a wider recursion, requiring a separate assessment.

## Variety and escalation

The first-party Colang agent handles conversational intent/action variety under constraining input/dialog/retrieval/tool/output policies. A blocked rail locally returns a rejection or transformed content; some branches can surface events, errors or logs to the host/operator. These are local enforcement/reporting paths, not by themselves special algedonic organizational loops or proven S3–S5 escalation. Configuration and model dependencies bound the work the package can do.

## Evidence gaps

- This is a **source-first, pinned-revision** review, not a deployment attestation, third-party safety efficacy benchmark, or test of a live adversarial model. No runtime/model provider secrets were used.
- Some Colang configs are entirely deterministic or pure in/out guards. The positive S1 is **not** attributed to those modes: it is established by the *supported, shipped* model-guided `LLMRails`/Colang action/event mode with a first-party operational closure path.
- Potential specialized customer/host systems performing whole-operation current control, independent safety audits, external threat adaptation or ultimate-policy governance cannot be credited without their own concrete deployed evidence.
- The negative symbols document a bounded standard-distribution conclusion at this exact frozen revision, not impossibility for a future composition.

## Assessment summary

**Proposed canonical disposition: `included`**, for its supported first-party model-guided Colang conversational/action agent mode. **Proposed vector:** `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`. This is an ownership/function classification, not a safety score or a claim about the correctness or efficacy of NVIDIA's guardrails.
