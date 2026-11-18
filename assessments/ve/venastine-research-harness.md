---
harness_id: venastine-research-harness
project_name: Venastine Research Harness
repository: https://github.com/YahyaHammad/Venastine-Research-Harness
review_ref: bcf78619b56ec8bffead629673f074b9a0a34a8c
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Venastine Research Harness

## Review boundary
- System in focus: One running installation of the Venastine chat and deep-research harness with an operator, a configured model provider and first-party tools.
- Purpose and identity: Produce tool-assisted answers and evidence-graded research reports within operator-defined limits.
- Relevant environment: Operator queries, model-provider responses, retrieved publications and web sources, project files, local subprocesses and optional MCP tool services.
- Standard-distribution boundary: Pinned Python chat, research, CLI and TUI runtime with bundled agent roles and research passes. Provider inference and remote tool services are external dependencies.
- Credited operating / distribution surfaces: Model-tool conversation loop, multi-pass research runner, optional bundled pipeline reviewer, attended finding disposition and local TUI process-wide session control.
- Adjacent first-party surfaces excluded from ownership: Hosting-provider governance, release/maintainer workflows, contributor tooling and tests; tests corroborate wiring without supplying operating actors.
- First-party operating / deployment modes considered: Local CLI chat and research, local attended TUI, headless research and opt-in post-run review with tools where authorized.
- Recursion level: One running Venastine process with its active conversations, research runs and child sessions.
- Reviewed revision: `bcf78619b56ec8bffead629673f074b9a0a34a8c`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The chat entry point invokes a model-tool feedback loop, stores conversation context and can spawn constrained child agents. The research runner selects from prescribed passes for claims, grounding, critique, revision and synthesis, and persists the run for inspection or resumption. Its optional post-synthesis reviewer starts a separate agent thread and sends structured findings to the operator. The TUI exposes live subprocess rows and an operator intervention path across child threads.

## Operational model

The conversational agent and research execution are operational units when active. Their outputs are a responded conversation, executed tool work or a persisted report. Individual research passes and temporary subordinate tool calls contribute to an operational unit. The parent operator retains whole-process intervention authority in the TUI and approves specific research corrections when attended.

## S1 — Operations

- State: A
- Function: Carry out conversational and research work under model-selected tool actions and source judgments.
- Disturbance / variety regulated: Changing user questions, evidence quality, tool returns and provider failures.
- Decisive decision or feedback right: Select tool calls and parameters, synthesize results and choose the next action or final response.
- Decision owner: Active chat model or model-driven research pass within the shipped loop.
- Supporting / enforcement mechanisms: Tool authorization, bounded dispatch, conversation storage, pass validation and report persistence.
- Closure path: Tool results re-enter the model context and can change subsequent calls or final output.
- Why this is / is not agent-owned: The dispatcher executes selected calls and returns observations. Removing the model removes substantive discretionary selection.
- Boundary reachability: Normal CLI/TUI chat uses the bundled conversation loop, and research mode dispatches model-driven passes through the same harness core.
- Evidence: [chat entry](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/main.py#L924-L966), [model-tool loop](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/loop.py#L2192-L2285), [research pipeline](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/reasoning/orchestrator.py#L1704-L1744).
- Basis: structural
- Confidence: medium
- Caveats: Source paths establish standard-distribution reachability. Provider execution was unobserved.

## S2 — Coordination

- State: —
- Function: No material agentic inter-unit interference regulator was established.
- Disturbance / variety regulated: Child or concurrent tool work can interact through local resources and may block a parent awaiting completion.
- Decisive decision or feedback right: A separate decision right governing mutual adjustment between operational units was not established.
- Decision owner: Session supervisor, dispatch grouping and parent-to-child delegation control their individual paths.
- Supporting / enforcement mechanisms: Thread ownership, tool grants, bounded scheduling and wake event delivery.
- Closure path: A child result or subprocess event returns to its caller or owner thread. The examined paths do not feed a negotiated interference response back to multiple units.
- Why this is / is not agent-owned: The model chooses delegated tasks while grant boundaries and ordering are enforced by the runtime.
- Evidence: [parallel grouping](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/loop.py#L997-L1024), [child execution](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/agents/subagent_tool.py#L263-L388), [child wake](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/agents/subagent_tool.py#L430-L471).
- Basis: structural
- Confidence: medium
- Caveats: Bounded finding for shipped modes. A deployment could design additional coordination.

### Absence scope

- Surfaces inspected: Tool parallelism, child task/spawn controls and shell-session wake delivery.
- Plausible first-party paths checked: Access collision, serialized side effects, delegated work and blocked child sessions.
- Why no material first-party path remains: The shipped paths fence owner access, enforce ordering or return completion to the caller. No S2-specific decision interface lets units coordinate a shared disturbance.

## S3 — Inside-and-now control

- State: P
- Function: Intervene in present background commitments across the process when local agent work blocks the operator or consumes shared execution capacity.
- Disturbance / variety regulated: Live work may block a parent turn via a subprocess owned by a child in another thread.
- Decisive decision or feedback right: Select which live process-wide commitment to terminate and release its own waiting execution path.
- Decision owner: Local TUI operator with process-wide authority.
- Supporting / enforcement mechanisms: Session registry, live sidebar, session-specific selection, worker-side stop execution and wake events.
- Closure path: A selected termination changes the target process state. The kill event reaches the owning turn immediately or on its next user message.
- Why this is / is not agent-owned: Agent tools are scoped to their owner thread while the TUI operator can inspect and intervene across child threads.
- Boundary reachability: The local TUI ships the process-wide live-session picker and termination command.
- Whole-system current view: The session registry exposes all live subprocess rows across the local process, including child-owned rows.
- Current-control decision scope: The operator selects a live commitment to remove while keeping other commitments active and returning the result to the affected turn.
- Evidence: [operator interruption and wake](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/tui/app.py#L2331-L2384), [whole-process live state](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/tui/app.py#L3871-L3914), [wake payload](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/session_wake.py#L146-L207).
- Basis: structural
- Confidence: medium
- Caveats: This parent mode is limited to current subprocess commitments in one local TUI process. The evidence does not establish autonomous portfolio control.

## S3* — Complementary audit

- State: A
- Function: Expose unsupported claims, wrong confidence tiers and report errors through complementary post-run verification.
- Disturbance / variety regulated: The ordinary research pipeline can publish a confident claim or summary that the primary source does not support.
- Decisive decision or feedback right: Decide independently which claims to check and which concrete corrections to propose.
- Decision owner: Bundled pipeline-reviewer model agent. The attended operator decides whether a correction may mutate the result.
- Supporting / enforcement mechanisms: Separate reviewer thread, selectable research review, authorized source retrieval and consent records.
- Closure path: The reviewer returns structured findings. The operator can accept them and the runner regenerates and persists the report when synthesis succeeds.
- Why this is / is not agent-owned: Removing the reviewer removes its source checks and substantive findings. Consent gates application after the audit judgment.
- Boundary reachability: The shipped research review path invokes the bundled role after synthesis and exposes retrieval tools when authorized.
- Claim being audited: Reported claims, tier assignments and report statements faithfully reflect their underlying sources.
- Ordinary reporting path: Pipeline-grounded claims, scores, trace and final report.
- Complementary access path: The reviewer can retrieve linked publications or search for relevant primary evidence through its own allowed calls.
- Independence boundary: A separate review thread reads the finished run without inheriting producer-pass conversation history and can make its own external retrieval calls.
- Who acts on findings: The attended operator accepts, rejects or requests refinement, then the pipeline applies the accepted corrective judgment through re-synthesis.
- Evidence: [reviewer role and source tools](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/agents/builtin/pipeline-reviewer.md#L1-L42), [review input and separate run](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/reasoning/review.py#L68-L145), [findings and corrective synthesis](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/reasoning/orchestrator.py#L1123-L1194), [attended review entry](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L446-L454).
- Basis: structural
- Confidence: medium
- Caveats: Credit is limited to the optional authorized source-verification mode. A tool-less review sees only delivered artifacts and the same provider can power the producer and reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: No material shipped adaptation loop turns prospective external developments into changes to the harness's own repertoire.
- Disturbance / variety regulated: New research evidence changes reports while evolving model capability and operating conditions could demand changes to the harness itself.
- Decisive decision or feedback right: No decisive outside-and-then adaptation right was found.
- Decision owner: The operator chooses providers/configuration and supplies research queries.
- Supporting / enforcement mechanisms: Research, source retrieval, remembered context, provider settings and capability controls.
- Closure path: Retrieved evidence updates the current task output. Remembered information conditions later prompts without selecting a prospective system adaptation.
- Why this is / is not agent-owned: The models choose research actions and proposed findings inside preselected operating modes.
- Evidence: [research purpose and phases](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L242-L270), [memory injection](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/core/loop.py#L181-L199), [provider and runtime settings](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L960-L1048).
- Basis: structural
- Confidence: medium
- Caveats: Future-oriented research can be a user task within S1.

### Absence scope

- Surfaces inspected: Research passes, model/provider options, durable memory and agent/skill selection.
- Plausible first-party paths checked: External research as adaptation sensing, memory as capability change and manual provider changes as parent closure.
- Why no material first-party path remains: No examined path develops options for Venastine's own future operation and returns an authoritative adaptation decision to current control.

## S5 — Policy and identity

- State: —
- Function: No material shipped identity-level adjudication path was established.
- Disturbance / variety regulated: Tool access, workspace trust and project instructions must remain within operator-defined bounds.
- Decisive decision or feedback right: No system identity or ultimate-policy decision routes back into durable operational governance through a function-specific path.
- Decision owner: Operator and distribution configuration define permitted modes and tools.
- Supporting / enforcement mechanisms: Static trust/access rules, scoped permissions, role prompts and per-run approval.
- Closure path: Selected rules shape ordinary invocation and review consent applies a specific correction.
- Why this is / is not agent-owned: The agent selects work inside constraints while the shipped controls act on narrower tool, workspace and task decisions.
- Evidence: [permission and workspace model](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L495-L520), [workspace and grants](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L603-L634), [role definitions](https://github.com/YahyaHammad/Venastine-Research-Harness/blob/bcf78619b56ec8bffead629673f074b9a0a34a8c/README.md#L682-L725).
- Basis: structural
- Confidence: medium
- Caveats: Workspace trust can govern imported project context. The examined trust route addresses which project inputs and tools the operating mode permits.

### Absence scope

- Surfaces inspected: Workspace trust, permission tiers, project/agent instructions, tool grants and attended review consent.
- Plausible first-party paths checked: Operator trust decision, persistent role configuration and refusal or consent prompts as a parent-governed policy candidate.
- Why no material first-party path remains: The reachable decisions are access configuration and bounded task consent. No shipped loop takes up a dispute about the process's ultimate mission or policy and returns a binding organizational resolution.

## Distributed OSS parent arrangement

Public maintainers are outside the reviewed installation boundary. The local operator holds current-control authority in the supported attended TUI.

## Self-hosted and non-human modes

Attended installations can apply audit findings and stop live subprocess commitments. A headless review can record findings while the mutation path requires reachable consent.

## Recursion

Child agents and pipeline passes are nested execution units. The reviewed source does not establish a complete viable metasystem per child.

## Variety and escalation

Tool bounds attenuate resource and permission variety. Process state and wake returns expose outcomes to their owners. The independent review branch can distinguish claim errors and route proposed corrections to the operator.

## Evidence gaps

This is a pinned source assessment. Provider-backed research, hosted isolation behavior, and the practical reliability of audit retrieval and interventions were not measured.
