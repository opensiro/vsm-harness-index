---
harness_id: mola-harness
project_name: mola-harness
repository: https://github.com/Mola-maker/mola-harness
review_ref: 3329d2fb4e878e5058263d345c7f7aa4880a73e0
reviewed_at: 2026-10-31
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

# mola-harness

## Review boundary

- System in focus: The shipped v0.1 TypeScript CLI and model/tool loop for one local developer task.
- Purpose and identity: Answer developer requests using local read and allowlisted command observations.
- Relevant environment: A user workspace, OS subprocesses, environment-provided configuration and optional OpenAI-compatible model endpoint.
- Standard-distribution boundary: The CLI, configuration, provider implementations, two registered tools and per-run session log at the exact pin; DeepSeek/custom real-provider mode is assessed separately from deterministic mock.
- Credited operating / distribution surfaces: src/cli.ts, src/config.ts, src/providers.ts, src/loop.ts and src/tools.ts as actually wired by package.json.
- Adjacent first-party surfaces excluded from ownership: tests/smoke.mjs, design survey/roadmap and repository development/licensing describe or test the product but do not act as runtime regulators.
- First-party operating / deployment modes considered: Real DeepSeek/custom execution, network-free mock and dry-run; no shipped subagent, MCP, skill, resume, compaction, permission-ask or sandbox mode in v0.1.
- Recursion level: One local product/run boundary; one operational assistant, not a recursive multi-agent organization.
- Reviewed revision: `3329d2fb4e878e5058263d345c7f7aa4880a73e0`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI resolves environment/flag settings, constructs either a scripted MockProvider or OpenAICompatibleProvider, then calls runLoop. The loop gives a model tool schemas, executes selected read/bash calls sequentially, appends observations to the conversation and stops on a text answer or maxSteps. The read tool uses resolved-path prefix checks and a file size bound; bash uses execFile without a shell, an allowlist, timeout and output cap. Each run logs task, assistant, tool and final events to JSONL. Those checks are implementation controls, not a proof of confinement. There is no persistent cross-run agent memory or delegation. Skills, MCP, resume/fork, subagents and real isolation are roadmap entries. [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json).

## Operational model

A real model-backed assistant owns local action selection and observation interpretation. The provider is an inference dependency, while the first-party CLI/loop/tool composition is the assessed harness. Scripted mock behavior demonstrates wiring only. Developer-authored safety rules and user-authored tasks remain separate from agent ownership.

## S1 — Operations

- State: A
- Function: The real-provider conversation loop performs local workspace investigation and command-assisted answers.
- Disturbance / variety regulated: Different user questions, selected files, command outputs and tool failures.
- Decisive decision or feedback right: Choose the next read/bash call, interpret returned observations and decide when to answer.
- Decision owner: The model-backed assistant in DeepSeek/custom mode; the first-party loop invokes that decision maker.
- Supporting / enforcement mechanisms: Provider transport, registry, step bound, output/timeout caps and JSONL persistence enforce/record operation.
- Closure path: Model tool call → runTool → tool result appended to messages → next provider completion or final answer.
- Boundary reachability: The shipped CLI constructs OpenAICompatibleProvider for deepseek/custom and passes it into runLoop; this requires configured credentials but no custom agent-loop implementation.
- Why this is / is not agent-owned: Removing the model-backed assistant leaves only transport and gates, not discretionary selection or interpretation. The mock mode is explicitly scripted and supplies no autonomy evidence.
- Evidence: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source establishes the configured real-provider operating path; no live provider/model-quality experiment was run.


## S2 — Coordination

- State: —
- Function: No inter-S1 anti-interference coordination function is supplied.
- Disturbance / variety regulated: Potential conflicts among independent operational cells would require more than this single sequential conversation.
- Decisive decision or feedback right: No multi-unit conflict-response right is exposed.
- Decision owner: No first-party S2 owner established.
- Supporting / enforcement mechanisms: Sequential tool execution and message order support one S1.
- Closure path: Tool feedback returns to the same conversation, not to distinct units under a coordination relation.
- Why this is / is not agent-owned: The agent's selection of tools is operational discretion; tools and provider calls are not distinct S1 units.
- Evidence: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: high.
- Caveats: A future subagent extension is outside the pinned v0.1 distribution.

### Absence scope

- Surfaces inspected: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json)
- Plausible first-party paths checked: Checked the loop's tool-call iteration, registry and CLI for worker scheduling, reservations, conflict detection or peer feedback; checked the explicit v0.2 subagent roadmap.
- Why no material first-party path remains: Only one run-local agent loop is implemented. No shipped distinct-S1 interference-to-attenuation-to-feedback relation remains.


## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control function beyond local loop execution is supplied.
- Disturbance / variety regulated: Step exhaustion and tool errors are local run conditions.
- Decisive decision or feedback right: No first-party regulator selects/revises whole-system commitments or resources from a current operational view.
- Decision owner: User selects maxSteps/workspace/provider before a run; deterministic code enforces these values.
- Supporting / enforcement mechanisms: Loop cap, command timeout, allowlist and logging.
- Closure path: A cap returns a stop answer; failed tools return to S1. Neither feeds a separate current-control judgment.
- Why this is / is not agent-owned: Choosing a cap before running one task and deterministic termination do not establish S3. No S3-specific constructor or parent decision-return loop is exposed.
- Evidence: [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts).
- Basis: structural.
- Confidence: high.
- Caveats: The claim is bounded to v0.1, including configured real providers.

### Absence scope

- Surfaces inspected: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json)
- Plausible first-party paths checked: Inspected max-step configuration, termination, JSONL state and dry-run for a current view plus intervention authority; considered user-controlled modes.
- Why no material first-party path remains: The distribution exposes static per-run controls and local action feedback, with no whole-system regulatory decision surface or qualifying parent-control loop.


## S3* — Complementary audit

- State: —
- Function: No complementary independent challenge of operational claims is supplied.
- Disturbance / variety regulated: Incorrect claims about file contents or task completion.
- Decisive decision or feedback right: No separately controlled audit judgment with corrective return exists.
- Decision owner: The producing assistant also generates the final answer; tests belong to repository development.
- Supporting / enforcement mechanisms: JSONL logs preserve ordinary tool results; system prompt asks the assistant to avoid unsupported claims.
- Closure path: The same assistant consumes its own ordinary tool observations; there is no independent audit feedback path.
- Why this is / is not agent-owned: Logs, ordinary input facts and mock smoke assertions do not create complementary audit ownership.
- Evidence: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs).
- Basis: structural.
- Confidence: high.
- Caveats: Users can manually inspect logs, but no audit actor or function-specific constructor is shipped.

### Absence scope

- Surfaces inspected: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json)
- Plausible first-party paths checked: Checked final-answer return, system instructions, log events, tool-error handling and smoke test for independent evidence access and a corrective control hook.
- Why no material first-party path remains: All operational evidence follows the producing loop; the smoke script validates development mechanics and is not wired into an independent runtime audit.


## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation function is supplied.
- Disturbance / variety regulated: Future provider capability or environment changes are not modeled by a shipped adaptation loop.
- Decisive decision or feedback right: No adaptation-option selection/return right is implemented.
- Decision owner: Maintainers author future releases; users choose static provider settings.
- Supporting / enforcement mechanisms: Provider interface and environment configuration support interoperability.
- Closure path: Responses affect the current task; there is no prospective option-to-current-capability return path.
- Why this is / is not agent-owned: General provider replaceability and a roadmap do not implement S4 or a parent-governed S4 mode.
- Evidence: [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: The roadmap's proposed benchmark and extensibility work were not credited.

### Absence scope

- Surfaces inspected: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json)
- Plausible first-party paths checked: Checked provider selection, design survey, benchmark roadmap, session logging and extension seam for environmental sensing, future distinctions and capability modification.
- Why no material first-party path remains: Those surfaces provide present execution/configuration or future plans; none ships an external/prospective adaptation closure.


## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy adjudication path is supplied.
- Disturbance / variety regulated: Permission refusals and task instructions are lower-level constraints.
- Decisive decision or feedback right: No identity-level issue is routed to legitimate ultimate authority and returned as a governing decision.
- Decision owner: Developers set the fixed system prompt and tool allowlist; users submit tasks/configuration.
- Supporting / enforcement mechanisms: Allowlist, path checks, no-shell execution and step limits.
- Closure path: Allowed/refused actions become ordinary tool results, not identity-policy decisions.
- Why this is / is not agent-owned: Static restrictions and human-selected settings constrain S1 but do not establish runtime S5 or parent governance.
- Evidence: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: high.
- Caveats: Safety enforcement is not a security certification; the source itself says process hardening is not a sandbox.

### Absence scope

- Surfaces inspected: [src/loop.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/loop.ts), [src/providers.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/providers.ts), [src/cli.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/cli.ts), [src/config.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/config.ts), [src/tools.ts](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/src/tools.ts), [README.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/README.md), [docs/ARCHITECTURE.md](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/docs/ARCHITECTURE.md), [tests/smoke.mjs](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/tests/smoke.mjs) and [package.json](https://github.com/Mola-maker/mola-harness/blob/3329d2fb4e878e5058263d345c7f7aa4880a73e0/package.json)
- Plausible first-party paths checked: Inspected system prompt, command/path gate, CLI/environment settings, project license and architecture for a policy issue, legitimate parent decision and authoritative return.
- Why no material first-party path remains: No supported runtime identity/ultimate-policy conversation or S3–S4 tension-resolution path remains at this product boundary.


## Distributed OSS parent arrangement

The Apache-2.0 repository has maintainer-controlled code/configuration. No organization-level or contribution-cell parent S3/S4/S5 loop is instantiated by this CLI; public OSS status alone does not supply one.

## Self-hosted and non-human modes

The product runs locally with user-supplied provider credentials; mock and dry-run do not establish model autonomy. Operator settings and the ability to terminate a process do not add function-specific parent modes.

## Recursion

A provider call, tool invocation and command subprocess are parts/dependencies of one operational loop. No sub-unit with an evidenced local metasystem is shipped.

## Variety and escalation

Tool schemas and allowlists attenuate action variety; tool errors and real observations feed S1. Step and timeout bounds cap resource use. Provider errors fail the CLI; no separate exceptional response authority or algedonic channel is established.

## Evidence gaps

Static pinned-source assessment; no live model/provider E2E run, reliability benchmark or security evaluation. No unresolved shipped higher-function path was found within the deliberately small v0.1 distribution. Future roadmap capabilities require a new-ref review.
