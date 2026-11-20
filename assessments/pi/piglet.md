---
harness_id: piglet
project_name: Piglet
repository: https://github.com/mcpcpc/piglet
review_ref: 5d3179c06a7a3f1e541f5012884d98c7fddd41f1
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
autonomy_s5: P
---

# Piglet

## Review boundary

- System in focus: The Piglet local coding-agent installation.
- Purpose and identity: A GUI-operated agent that works on a user's software project and maintains a resumable session.
- Relevant environment: Local workspaces, the operator, an OS shell and filesystem, and externally hosted or local model endpoints.
- Standard-distribution boundary: First-party Python runtime and tools, web app, and Electron wrapper. Operator configurations enter through supported first-party paths. Independently written extensions and provider internals do not supply credited decision owners.
- Credited operating / distribution surfaces: [README.md](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/README.md), [src/piglet/launcher.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/launcher.py), [desktop/src/main.ts](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/desktop/src/main.ts) and the bundled session runtime.
- Adjacent first-party surfaces excluded from ownership: Development launch, contributor process, tests, and installer CI.
- First-party operating / deployment modes considered: Local browser GUI from source and packaged Electron GUI with Python sidecar.
- Recursion level: One local installation, with task sessions as operational units.
- Reviewed revision: 5d3179c06a7a3f1e541f5012884d98c7fddd41f1
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The GUI sends commands to a local Python service. The session manager opens and retains live sessions, each with its transcript tree, model, tool set, queued messages and abort state. Extensions attach per session. Model providers supply inference to the built-in loop. See [src/piglet/server/runner.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/server/runner.py), [src/piglet/runtime/manager.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/manager.py), [src/piglet/sessions/store.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/sessions/store.py) and [src/piglet/extensions/host.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/extensions/host.py).

## Operational model

The operator opens a workspace and gives a task or steers an active run. Each session can reason about and alter its workspace, consume tool results, and produce a response. Session setup and operator policy remain outside the model's task discretion.

## S1 — Operations

- State: A
- Function: Complete software tasks through iterative workspace observation and mutation.
- Disturbance / variety regulated: Unknown code state, tool failures, changing user instructions and intermediate results.
- Decisive decision or feedback right: Choose the next tool action or produce the final answer based on current task evidence.
- Decision owner: The model-driven agent in the session.
- Supporting / enforcement mechanisms: Runtime dispatches built-in tools, validates inputs, emits results and persists session history.
- Closure path: Tool results join the model context and affect its next decision. The final response and workspace changes reach the operator.
- Boundary reachability: Both supported GUI distributions enter the same session and loop path through the shipped server.
- Why this is / is not agent-owned: The runtime executes requests, but removing model discretion removes the choice of task action and the response to tool results.
- Evidence: [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L333-L358), [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L559-L577), [src/piglet/agent/loop.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/agent/loop.py#L99-L136).
- Basis: Explicit
- Confidence: High
- Caveats: Individual tools execute deterministic operations. No live provider or installed GUI was exercised here.

## S2 — Coordination

- State: —
- Function: Coordination between concurrently usable task sessions.
- Disturbance / variety regulated: Sessions may operate in the same workspace.
- Decisive decision or feedback right: No installed relation was found that negotiates conflicting session activity and feeds back to the participating units.
- Decision owner: None established.
- Supporting / enforcement mechanisms: The manager holds session instances. Tool-call concurrency within one model response has a local file-lock map.
- Closure path: No returned cross-session coordination decision.
- Why this is / is not agent-owned: A lock created within one response's tool batch attenuates intra-unit calls. Session switches and transcript branching do not regulate multiple units' interference.
- Evidence: [src/piglet/runtime/manager.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/manager.py#L65-L117), [src/piglet/agent/loop.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/agent/loop.py#L182-L217), [src/piglet/server/handlers.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/server/handlers.py#L327-L370).
- Basis: Structural
- Confidence: High
- Caveats: Operator coordination and external extensions are possible outside this credited function.

### Absence scope

- Surfaces inspected: Session registry, project/session commands, branching, tool dispatch and per-session extensions.
- Plausible first-party paths checked: Cross-session workspace collision, per-path serialization, and parent-session lineage as a possible coordination channel.
- Why no material first-party path remains: Serialization lives within one tool batch. The shipped session registry and lineage supply no cross-session interference outcome or corrective feedback.

## S3 — Inside-and-now control

- State: —
- Function: Whole-installation current control over workload commitments and resources.
- Disturbance / variety regulated: Concurrent task demand and failed or interrupted execution.
- Decisive decision or feedback right: No installation-level allocation or reprioritization loop was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: The GUI can inspect live sessions and the operator can prompt, steer or stop an individual session. Retry and compaction are bounded recovery.
- Closure path: Local interruption and retry return to a single run.
- Why this is / is not agent-owned: A live-session listing plus individual controls does not establish a supported whole-installation current commitment and resource decision path.
- Evidence: [src/piglet/server/handlers.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/server/handlers.py#L341-L371), [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L333-L358), [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L450-L512).
- Basis: Structural
- Confidence: Medium
- Caveats: An operator may manage workload informally across sessions.

### Absence scope

- Surfaces inspected: Live-session listing, per-session controls and recovery, model and settings reload.
- Plausible first-party paths checked: Runtime arbitration, operator workload supervision, and resource reallocation across sessions.
- Why no material first-party path remains: Current session state reaches the GUI and per-session commands reach their target. Neither the runtime nor the shipped GUI supplies a whole-scope current intervention path with cross-session commitments.

## S3* — Complementary audit

- State: —
- Function: Direct complementary audit of operational claims and corrective feedback.
- Disturbance / variety regulated: A task result could overstate or conceal its actual effect.
- Decisive decision or feedback right: No first-party audit judgment path with complementary access was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Transcripts record tool outcomes and the GUI exposes operational events.
- Closure path: No audit finding is returned to an accountable current-control owner by the standard distribution.
- Why this is / is not agent-owned: Transcript, export, and extension hooks expose routine execution evidence or generic integration points.
- Evidence: [src/piglet/runtime/export.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/export.py), [src/piglet/server/hub.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/server/hub.py#L39-L67), [src/piglet/extensions/host.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/extensions/host.py#L84-L113).
- Basis: Structural
- Confidence: High
- Caveats: A human can inspect artifacts independently outside the supplied audit path.

### Absence scope

- Surfaces inspected: Transcript and export, event hub, built-in tools and extension host.
- Plausible first-party paths checked: Direct artifact sampling by a separate reviewer, tool hook as audit decision path, and development CI as a possible reviewer.
- Why no material first-party path remains: The shipped event/export surfaces reflect the ordinary session and hooks require externally supplied judgment. Development CI checks the product rather than installed operations.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective adaptation of the installation to environmental change.
- Disturbance / variety regulated: Shifts in provider and workspace conditions may affect future capability.
- Decisive decision or feedback right: No first-party route was found for external intelligence to generate and return a prospective capability decision.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Provider and package configuration, compaction, retry and resource reload are shipped.
- Closure path: Changes are applied when configured and recovery feeds the active session.
- Why this is / is not agent-owned: Current configuration or error recovery does not evaluate future external conditions and select an adaptation.
- Evidence: [src/piglet/runtime/resources.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/resources.py#L70-L125), [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L474-L512), [src/piglet/extensions/packages.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/extensions/packages.py).
- Basis: Structural
- Confidence: Medium
- Caveats: The operator may choose changes based on external information obtained separately.

### Absence scope

- Surfaces inspected: Provider/model settings, packages, recovery, and resource reload.
- Plausible first-party paths checked: Prospective model capability adaptation, package/environment intelligence, and operator return through configuration.
- Why no material first-party path remains: Source paths resolve configured resources or recover a present turn. They supply no first-party chain from external change through prospective judgment to returned capability choice.

## S5 — Policy and identity

- State: P
- Function: Set the enduring mandate of the local coding agent and decide whose project-level instructions may define it.
- Disturbance / variety regulated: A workspace can supply an alternative agent mandate and executable extensions under project trust.
- Decisive decision or feedback right: Choose the global agent mandate and authorize or revoke project-level delegation to override its default preamble.
- Decision owner: The local installation operator.
- Supporting / enforcement mechanisms: Global and trusted-project SYSTEM.md precedence, project trust store and UI, resource reload, and system-prompt composition.
- Closure path: Operator-controlled mandate and trust are read into resources. A subsequent run carries the resulting preamble as the system prompt and applies the trusted project resource boundary.
- Boundary reachability: Global and project resources are native to both local GUI distributions. The server accepts the operator's trust choice and reloads sessions.
- Why this is / is not agent-owned: The model consumes the governing preamble. The operator chooses whether the project mandate can replace it and can revoke that delegation.
- Evidence: [src/piglet/server/handlers.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/server/handlers.py#L457-L467), [src/piglet/runtime/resources.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/resources.py#L87-L126), [src/piglet/resources/context_files.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/resources/context_files.py#L63-L80), [src/piglet/resources/system_prompt.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/resources/system_prompt.py#L66-L86), [src/piglet/runtime/session.py](https://github.com/mcpcpc/piglet/blob/5d3179c06a7a3f1e541f5012884d98c7fddd41f1/src/piglet/runtime/session.py#L559-L577).
- Basis: Structural
- Confidence: Medium
- Caveats: The claim is the supported override of the enduring agent mandate in an operator-governed installation. Credential settings and task steering alone do not establish S5.
- Identity / ultimate-policy issue: Which enduring mandate the local coding agent follows across tasks, and whether the workspace may replace the installation's default mandate.
- Ultimate authority in each claimed mode: The local operator specifies the global mandate and decides whether project-level mandate files apply.
- Return-to-operation path: Trust changes reload resources. The allowed SYSTEM.md supplies the replacement preamble on subsequent runs.

## Distributed OSS parent arrangement

The local installation operator holds the assessed parent right. Project release maintainers are outside that operational recursion.

## Self-hosted and non-human modes

The supported distribution is local and operator-governed. No additional non-human organizational mode was identified.

## Recursion

The installation owns the declared service boundary. Individual sessions supply task operations. Model backends and externally implemented extensions do not raise the recursion of the assessment.

## Variety and escalation

Steering and abort let the user intervene in active tasks. Per-run error recovery, context compaction and tool results absorb local disturbances. The operator handles the installation's standing project trust and agent mandate.

## Evidence gaps

Source-only assessment. No live inference, GUI session, or independently authored extension was executed. The S5 conclusion uses the documented operator-governed mandate path and does not assert an immutable security boundary against shell actions.
