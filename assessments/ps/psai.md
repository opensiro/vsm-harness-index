---
harness_id: psai
project_name: PSAI
repository: https://github.com/dfinke/PSAI
review_ref: 018a3304dc7d09ac90e78525f5181bee17edb5a1
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

# PSAI

## Review boundary

- System in focus: the installed PSAI PowerShell module and its first-party New-Agent / Get-AgentResponse conversational tool loop.
- Purpose and identity: complete user requests through model-selected PowerShell tool actions and returned answers.
- Relevant environment: user requests, registered local commands, tool failures, OpenAI-compatible model responses and operator configuration.
- Standard-distribution boundary: PSAI.psd1/PSAI.psm1 exports, Public and Private functions and bundled tool modules at the pinned revision.
- Credited operating / distribution surfaces: Public/New-Agent.ps1, Public/Get-AgentResponse.ps1 and Public/Invoke-OAIFunctionCall.ps1, explicitly loaded by PSAI.psm1.
- Adjacent first-party surfaces excluded from ownership: examples, __tests__, repository CLAUDE.md, CI and publishing scripts; these corroborate usage, not a deployed metasystem.
- First-party operating / deployment modes considered: programmatic agent object, interactive CLI, caller-configured tools/model/instructions, and Assistants/thread/run API wrappers.
- Recursion level: one local installed agent harness; not the developer's organization or a whole enterprise automation deployment.
- Reviewed revision: `018a3304dc7d09ac90e78525f5181bee17edb5a1`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The module exports New-Agent, Get-AgentResponse, interactive CLI, command-to-tool registration and API wrappers. New-Agent installs a model/tool loop as a ScriptMethod. PrintResponse appends input, requests a model completion, records its message, executes requested tools, appends their results and repeats until finish_reason is stop. Invoke-OAIFunctionCall resolves registered command names, splats model arguments and turns failures into tool-result messages. Runtime invocation/serialization supports agent discretion.

Conversation messages are module-scoped (`$script:messages`), including reset on New-Agent; this is a state-isolation caveat, not evidence of coordination. The Assistants API functions expose provider threads, runs, polling, cancellation and metadata; they do not ship whole-system regulatory decisions. Human involvement selects requests/configuration and supplies CLI follow-ups or rewind. Repository examples and tests are adjacent. The file called 05-MultiAgent.ps1 actually constructs one New-Agent with two tools at this pin.

## Operational model

The operational unit is the configured agent handling a request. Its outcome is an answer/action grounded in successive tool results. The model chooses the next command/arguments or completion; PowerShell executes and feeds back the result. Developers select permitted commands/model/instructions; the user owns the requested task. No separate packaged organization-level regulator is imported from the surrounding developer workflow.

## S1 — Operations

- State: A
- Function: perform requested local work by selecting tool actions and interpreting their results.
- Disturbance / variety regulated: different user problems, available tools, command outputs and execution errors.
- Decisive decision or feedback right: choose next tool call/arguments and whether to continue or answer.
- Decision owner: the configured model-backed agent in PrintResponse.
- Supporting / enforcement mechanisms: chat API transport, PowerShell command invocation, message conversion and finish-reason loop.
- Closure path: model tool call → Invoke-OAIFunctionCall result/error → appended tool message → next model completion → terminal answer.
- Boundary reachability: PSAI.psm1 explicitly loads New-Agent and the tool dispatcher; Get-AgentResponse calls the exported agent object's PrintResponse method.
- Why this is / is not agent-owned: removing the model's choices leaves command plumbing but no discretionary task-solving sequence.
- Evidence: [module exports](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/PSAI.psm1), [agent loop](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/New-Agent.ps1), [response entry](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/Get-AgentResponse.ps1), [tool feedback](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/Invoke-OAIFunctionCall.ps1).
- Basis: structural.
- Confidence: high for source-defined closure.
- Caveats: no live provider run was executed; module-scoped messages can couple independently constructed agents.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation established for interference among distinct operational units.
- Disturbance / variety regulated: interference among distinct operational units; candidate paths evaluated below.
- Decisive decision or feedback right: no function-specific right with returned closure supplied.
- Decision owner: no qualifying owner at this boundary; agent task discretion and caller configuration remain separate.
- Supporting / enforcement mechanisms: The inspected standard loop is one agent with tools. Multiple object creation shares module-level messages, but no collision detection, negotiated correction or agent-owned isolation response is supplied. The multi-agent example is one agent with multiple tools.
- Closure path: no function-specific return established after checking positive, constructor and eligible parent alternatives.
- Why this is / is not agent-owned: absence concerns the organizational function, not merely deterministic implementation.
- Evidence: [pinned primary surface](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/New-Agent.ps1); inspected paths below.
- Basis: structural.
- Confidence: high within the declared installed-module boundary.
- Caveats: a custom application could add this function; generic extensibility is not supplied ownership.

### Absence scope

- Surfaces inspected: PSAI.psm1; Public/New-Agent.ps1; examples/agent-quickstarts/05-MultiAgent.ps1.
- Plausible first-party paths checked: multiple-object shared messages, tool dispatch and advertised multi-agent example.
- Why no material first-party path remains: Only generic invocation and shared state remain; no first-party S2-specific disturbance-response-return path exists.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party S3 relation established for whole-system current commitments/resources.
- Disturbance / variety regulated: whole-system current commitments/resources; candidate paths evaluated below.
- Decisive decision or feedback right: no function-specific right with returned closure supplied.
- Decision owner: no qualifying owner at this boundary; agent task discretion and caller configuration remain separate.
- Supporting / enforcement mechanisms: Run polling/cancellation, provider choice and instructions are caller/API controls, not a packaged whole-system view with current resource/commitment bargaining or an agent/parent decision-return loop.
- Closure path: no function-specific return established after checking positive, constructor and eligible parent alternatives.
- Why this is / is not agent-owned: absence concerns the organizational function, not merely deterministic implementation.
- Evidence: [pinned primary surface](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/Wait-OAIOnRun.ps1); inspected paths below.
- Basis: structural.
- Confidence: high within the declared installed-module boundary.
- Caveats: a custom application could add this function; generic extensibility is not supplied ownership.

### Absence scope

- Surfaces inspected: Public/New-Agent.ps1; Public/Wait-OAIOnRun.ps1; Public/Update-OAIRun.ps1; Public/Stop-OAIRun.ps1.
- Plausible first-party paths checked: CLI interventions, run lifecycle, metadata and provider/tool configuration.
- Why no material first-party path remains: These are local execution/API controls without the function-specific whole-system control relation; no autonomous constructor or qualifying parent loop is exposed.

## S3* — Complementary audit

- State: —
- Function: no material first-party S3* relation established for operational claims needing independent challenge.
- Disturbance / variety regulated: operational claims needing independent challenge; candidate paths evaluated below.
- Decisive decision or feedback right: no function-specific right with returned closure supplied.
- Decision owner: no qualifying owner at this boundary; agent task discretion and caller configuration remain separate.
- Supporting / enforcement mechanisms: Tool outputs are routine evidence for the producing agent. Parameter/CLI tests are repository development checks; no independently controlled complementary audit of operational claims is connected to corrective control.
- Closure path: no function-specific return established after checking positive, constructor and eligible parent alternatives.
- Why this is / is not agent-owned: absence concerns the organizational function, not merely deterministic implementation.
- Evidence: [pinned primary surface](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/__tests__/New-Agent.tests.ps1); inspected paths below.
- Basis: structural.
- Confidence: high within the declared installed-module boundary.
- Caveats: a custom application could add this function; generic extensibility is not supplied ownership.

### Absence scope

- Surfaces inspected: Public/Invoke-OAIFunctionCall.ps1; __tests__/New-Agent.tests.ps1; __tests__/Get-AgentResponse.tests.ps1; .github/workflows.
- Plausible first-party paths checked: tool error reporting, tests and examples including event-log analysis.
- Why no material first-party path remains: Ordinary task observations and developer tests do not create a separate complementary audit judgment or corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party S4 relation established for future external change affecting present capability.
- Disturbance / variety regulated: future external change affecting present capability; candidate paths evaluated below.
- Decisive decision or feedback right: no function-specific right with returned closure supplied.
- Decision owner: no qualifying owner at this boundary; agent task discretion and caller configuration remain separate.
- Supporting / enforcement mechanisms: Web/stock tools and prompt/context updates serve current tasks. No shipped prospective option-generation and capability-adoption loop couples those observations to present harness control.
- Closure path: no function-specific return established after checking positive, constructor and eligible parent alternatives.
- Why this is / is not agent-owned: absence concerns the organizational function, not merely deterministic implementation.
- Evidence: [pinned primary surface](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/README.md); inspected paths below.
- Basis: structural.
- Confidence: high within the declared installed-module boundary.
- Caveats: a custom application could add this function; generic extensibility is not supplied ownership.

### Absence scope

- Surfaces inspected: Public/New-Agent.ps1; Public/Tools; README.md; examples; changelog.md.
- Plausible first-party paths checked: search tools, provider/model choice, thread updates and development changes.
- Why no material first-party path remains: Task information gathering and caller reconfiguration supply no first-party outside-and-then adaptation decision-return path, including no qualifying parent mode.

## S5 — Policy and identity

- State: —
- Function: no material first-party S5 relation established for identity or ultimate-policy disputes.
- Disturbance / variety regulated: identity or ultimate-policy disputes; candidate paths evaluated below.
- Decisive decision or feedback right: no function-specific right with returned closure supplied.
- Decision owner: no qualifying owner at this boundary; agent task discretion and caller configuration remain separate.
- Supporting / enforcement mechanisms: New-Agent accepts fixed instructions/name/description; CLI asks ordinary task questions. No identity-level matter is routed to legitimate ultimate authority with an authoritative returned decision governing subsequent operation.
- Closure path: no function-specific return established after checking positive, constructor and eligible parent alternatives.
- Why this is / is not agent-owned: absence concerns the organizational function, not merely deterministic implementation.
- Evidence: [pinned primary surface](https://github.com/dfinke/PSAI/blob/018a3304dc7d09ac90e78525f5181bee17edb5a1/Public/Invoke-InteractiveCLI.ps1); inspected paths below.
- Basis: structural.
- Confidence: high within the declared installed-module boundary.
- Caveats: a custom application could add this function; generic extensibility is not supplied ownership.

### Absence scope

- Surfaces inspected: Public/New-Agent.ps1; Public/Invoke-InteractiveCLI.ps1; README.md; CLAUDE.md; Support.md.
- Plausible first-party paths checked: system messages, caller authority, instruction changes, repository contributor instructions.
- Why no material first-party path remains: Static identity/configuration and developer governance are not a runtime identity-policy closure at the assessed recursion.

## Distributed OSS parent arrangement

Repository maintainers and independent module users are not shown operating one common agent organization. No project-level parent mode is inferred from contributors or release changes.

## Self-hosted and non-human modes

The local installed module is self-hosted with external inference. Interactive input, rewind and provider/API controls do not establish function-specific S3/S4/S5 parent modes. No separate non-human organization mode is supplied.

## Recursion

Creating agent objects or calling tools is not recursive viability. No nested unit with its own evidenced metasystem is established.

## Variety and escalation

Tool execution failures return to the agent as messages; unsupported CLI commands return to the user. There is no distinct exceptional algedonic path or declared whole-system escalation regulator. Shared module messages limit isolation.

## Evidence gaps

Source-defined reachability was reviewed without paid/live model execution. Provider reliability and hidden remote Assistants internals are outside scope. The five negative findings are bounded distribution conclusions, not claims that custom PowerShell programs cannot implement those functions.
