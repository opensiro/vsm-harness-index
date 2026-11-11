---
harness_id: wittycode
project_name: WittyCode
repository: https://github.com/WittyRyuji/WittyCode
review_ref: 67af7d8fb0851cd4623c7b94993deddcb766ec1f
reviewed_at: 2026-11-11
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

# WittyCode

## Review boundary

- System in focus: WittyCode's installed Windows desktop coding assistant, specifically its first-party ChatGPT Plan/API Provider runtime and model–tool loop; not every externally hosted engine exposed by the UI.
- Purpose and identity: respond to user coding requests by choosing and performing file, search and command actions within the local project and reporting the result.
- Relevant environment: a user's local files and project, mutable tool output, model/provider failures, permissions, interruption, context-window pressure and follow-up steering.
- Standard-distribution boundary: packaged Windows desktop application, its `AppCore` / `ChatGPTController`, `desktop/core/harness` agent loop and tools, provider adapters, persisted sessions and user-facing authorization controls.
- Credited operating / distribution surfaces: shipped ChatGPT Plan/API Provider agent loop, local tool execution, session persistence, automatic compaction, follow-up steering, and optional bounded `/goal` continuation.
- Adjacent first-party surfaces excluded from ownership: `sandbox/` probes, developer review documents, `tests/` and CI, screenshots and release tooling; external Codex/Devin/Factory CLI engines and model/provider infrastructure are not first-party agent loops.
- First-party operating / deployment modes considered: first-party ChatGPT Plan and API Provider engine with `ask`/`code`/`full` permission levels; read-only Plan mode; `/goal` repeated-turn mode; external CLI engine switching as an adjacent integration.
- Recursion level: one user's local assistant session; multiple selectable engines or independent user sessions are not established as concurrently governed operational subsidiaries.
- Reviewed revision: `67af7d8fb0851cd4623c7b94993deddcb766ec1f`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The desktop `AppCore` launches a session-specific `ChatGPTController`. For the built-in ChatGPT/API engine, the controller constructs an `AgentLoop` with model stream, tool registry, observer, project instructions, skill discovery and current model selection. The loop sends contextual requests, receives model-selected calls, validates and executes each call under permission checks, returns clipped tool observations, and iterates until a final response, step cap or failure. The controller maintains separate durable log and compressed model-facing view and supports steering, cancellation and subsequent turns. `/goal` can restart ordinary turns using the model's own `GOAL: DONE` or `GOAL: BLOCKED` verdict with fixed caps. Other selectable engines are integration with external agent products, not evidence of WittyCode-owned loops. [agent loop](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/loop.py), [session controller](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/chatgpt/controller.py), [goal](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/goal.py), [maintainer source review](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/docs/loop-review-2026-11-11.md).

## Operational model

One session model selects executable tools from a first-party declaration set and can use observations to revise its next action. The user retains project selection, permissions, stop and engine choice; deterministic runtime guards protect state and control side effects. This establishes one operational S1 agent with a closed feedback loop. Merely offering several third-party engines, archived memory proposals, ordinary tool approvals or a goal counter does not itself demonstrate organizational S2–S5 at this recursion.

## S1 — Operations

- State: A
- Function: choose and carry out model-directed local coding and information actions for the user's request.
- Disturbance / variety regulated: changing local repository contents, search output, command errors, user steering, interrupted runs, provider rate limits, context pressure and ambiguous next steps.
- Decisive decision or feedback right: the model chooses tool name and arguments, interprets returned observations and decides to continue or finish within the first-party multi-step loop.
- Decision owner: selected API/ChatGPT-backed model in the shipped WittyCode agent runtime; the user sets the permission envelope.
- Supporting / enforcement mechanisms: `ToolContext`, command/file tool registry, approval/Plan restrictions, tool-output clipping, streaming adapters, retry and cancellation handling, persisted session log, compaction and step cap.
- Closure path: user prompt → controller-created `AgentLoop` → model call → permitted local action → tool result appended as `function_call_output` → subsequent model choice or final response; `/goal` can add bounded further turns.
- Boundary reachability: the README's packaged desktop first-party ChatGPT Plan/API Provider modes instantiate `AgentLoop` from the production controller; they do not require the external Codex or Devin CLI agent loop.
- Why this is / is not agent-owned: action selection and iteration depend on model judgment over tool observations; permission checks and persistence enforce or transport that judgment rather than selecting the action.
- Evidence: [runtime loop and action return](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/loop.py), [production controller wiring](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/chatgpt/controller.py), [permissions](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/permissions.py), [goal loop](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/goal.py).
- Basis: structural and explicit.
- Confidence: high for first-party control wiring; medium for provider-side run behavior.
- Caveats: source-level assessment, not a paid provider or Windows desktop E2E run; `/goal` uses a model self-verdict and fixed deterministic limits, not independent verification.

## S2 — Coordination

- State: —
- Function: no distinct first-party cross-S1 conflict-attenuation function is demonstrated at the selected one-session recursion.
- Disturbance / variety regulated: tool calls, queued steering messages and permission requests within a single conversation may contend, but they do not constitute conflict between independent S1 operating units.
- Decisive decision or feedback right: deterministic per-turn tool sequencing and session state transitions; no cross-unit coordination discretion is shown.
- Decision owner: the single active model for its task, with deterministic controller sequencing; no separate S2 agent is present.
- Supporting / enforcement mechanisms: serial `_run_calls`, queued steering and session lifecycle state.
- Closure path: one session's model calls are executed and observed in order; no distinct S1 collision is detected and returned as an inter-unit coordination adjustment.
- Why this is / is not agent-owned: alternate model engines are choices for the same session, not simultaneously operating S1 units; sequential tool calls are within-S1 execution discipline.
- Evidence: [loop call execution](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/loop.py), [controller session lifecycle](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/chatgpt/controller.py), [engine overview](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/README.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an independent multi-agent setup composed outside the packaged app is not assessed.

### Absence scope

- Surfaces inspected: desktop engine overview, session controller, `AgentLoop` tool/steering execution and `/goal` continuation.
- Plausible first-party paths checked: concurrent engine selection, multiple user sessions, intra-turn tool calls and model goal restarts.
- Why no material first-party path remains: none supplies distinct concurrently coupled S1 agents, an evidenced inter-agent interference witness and a coordination feedback decision in the declared single-session runtime.

## S3 — Inside-and-now control

- State: —
- Function: no separately evidenced whole-current system control over a portfolio of S1 units.
- Disturbance / variety regulated: an individual session can run too long, fail, be stopped or require approval; these are local execution and user constraints.
- Decisive decision or feedback right: the user changes permission/model/mode; deterministic runtime caps steps, retries transient failures and stops/records turns.
- Decision owner: user/configuration and local runtime enforcement for a single session, not an in-boundary agent or parent making cross-unit current-control decisions.
- Supporting / enforcement mechanisms: `MAX_STEPS`, `/goal` round and idle caps, `ChatGPTController` state, `ToolContext` permissions and session persistence.
- Closure path: run limit, failure or stop → session notice/termination or retry; no global current view → changed portfolio commitment/resource decision → subsequent S1 regulation.
- Why this is / is not agent-owned: the model's ordinary task choices and end markers are S1 work; the limits enforce preselected bounds rather than whole-system S3 discretion.
- Evidence: [controller](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/chatgpt/controller.py), [goal bounds](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/goal.py), [permissions](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/permissions.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: a user's oversight of many separate local conversations is outside the credited single-session governing system.

### Absence scope

- Surfaces inspected: `AppCore`, session controller, goal continuation, permission and execution-limit code, desktop model menu.
- Plausible first-party paths checked: session-state dashboard, per-turn stop/retry, approval decisions, model switching and repeated-goal progression.
- Why no material first-party path remains: no supported loop exposes a whole-current operational view coupled to discretionary cross-S1 resource, accountability or priority intervention.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit of operational claims with a distinct corrective authority/return is evidenced.
- Disturbance / variety regulated: wrong tool actions, memory-proposal errors, partial provider failures and user-visible claims may be examined by ordinary tools, user review or offline tests.
- Decisive decision or feedback right: user approves individual tool actions or reviews stored memory proposals; tests and source reviews are maintainer/development activities.
- Decision owner: user for ordinary approvals, same operating model for its own task, and external developers for offline quality review—not an independent runtime auditor.
- Supporting / enforcement mechanisms: permission checks, session log and compaction invariants, memory review UI, local test suites, `docs/harness-review-*` reports.
- Closure path: approval/denial constrains a tool call, or offline tests inform developers; no complementary raw-evidence audit finding returns to a whole-system current controller.
- Why this is / is not agent-owned: a review label, permission check or maintainer's code inspection is not first-party independent audit of operational reality.
- Evidence: [review UI and memory proposals](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/app_core.py), [permissions](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/permissions.py), [development-only loop review](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/docs/loop-review-2026-11-11.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: optional external human audit or testing may provide independent real-world assurance but is not included as an operational S3* path.

### Absence scope

- Surfaces inspected: runtime tool/permission path, memory-review surface, developer review documents, harness tests and logs.
- Plausible first-party paths checked: memory proposal review, prompt/tool permission cards, post-tool state checks, QA/test reports and selectable external engines.
- Why no material first-party path remains: reviewed paths are ordinary safeguards, user consent or development validation, without an independent complementary observation and corrective-return channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated external-and-prospective capability-adaptation cycle feeding current operation.
- Disturbance / variety regulated: model availability, provider errors, context pressure and imported user memory affect current tasks or operational settings.
- Decisive decision or feedback right: user chooses an existing engine/model; ordinary assistant may plan the current request; deterministic compaction adapts context size.
- Decision owner: user/configuration for provider choices, model for immediate task execution; no separate prospective adaptation decision right.
- Supporting / enforcement mechanisms: provider adapters, memory/import tools, skills discovery, context estimation and compaction.
- Closure path: engine selection, memory refresh or compacted view can change the next turn; no evidence of sensing a future external distinction, developing strategic alternatives and selecting a changed organizational capability.
- Why this is / is not agent-owned: current-task research, retrying and session memory do not constitute outside-and-then intelligence under the Profile.
- Evidence: [README engines and local memory](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/README.md), [loop compaction](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/loop.py), [goal current-task continuation](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/goal.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: source does not preclude user-led prospective research in arbitrary prompts; no durable first-party S4 feedback path is demonstrated.

### Absence scope

- Surfaces inspected: engine selection, built-in agent loop, `/goal`, skills, memory imports, compaction and provider error recovery.
- Plausible first-party paths checked: automatic model/provider switching, long-running goals, new memory/skills and changes in external model capabilities.
- Why no material first-party path remains: paths support immediate work or user configuration, without external future scenario/options → adaptation decision → updated present capacity feedback.

## S5 — Policy and identity

- State: —
- Function: no evidenced runtime identity/ultimate-policy adjudication and authoritative returned governance rule.
- Disturbance / variety regulated: permissions, project trust and write risk are bounded by fixed product constraints and user approvals for ordinary actions.
- Decisive decision or feedback right: developer presets permission levels; user may approve/deny tools, select project or change model; no first-party actor is tasked with adjudicating the assistant's ultimate purpose/identity.
- Decision owner: developer and user for configuration and ordinary consent, not a demonstrated S5 decision owner for an identity-level matter.
- Supporting / enforcement mechanisms: `ask`/`code`/`full`, Plan mode, protected paths, approval cards and system instructions.
- Closure path: permission decision allows/denies a specific action; no identity-level proposal → legitimate ultimate authority → policy return governing future operation is evidenced.
- Why this is / is not agent-owned: static rules and task approvals constrain S1 but do not establish a substantive S5 identity decision loop.
- Evidence: [permissions and approval](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/harness/permissions.py), [session mode/instructions wiring](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/desktop/core/chatgpt/controller.py), [README](https://github.com/WittyRyuji/WittyCode/blob/67af7d8fb0851cd4623c7b94993deddcb766ec1f/README.md).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an external organization may impose identity governance on its deployment, but it is not shipped as a closed first-party mode here.

### Absence scope

- Surfaces inspected: agent instructions, permission regimes, Plan mode, tool approval and project settings, goal termination and memory review.
- Plausible first-party paths checked: user approval, model switch, project trust, policy text and goal `BLOCKED` handoff.
- Why no material first-party path remains: all inspected paths concern routine consent or operating constraints, not a returned ultimate-policy or system-identity decision.

## Distributed OSS parent arrangement

Repository authors and contributors govern the source project, but their code reviews, release decisions and local development tools are separate from the installed desktop session. The assessed system does not establish a distributed operational parent mode for the same S3/S4/S5 functions.

## Self-hosted and non-human modes

The app is locally operated with user-selected permissions and engine credentials. The first-party model loop remains an S1 actor under those constraints; the user is not thereby a positive S3/S4/S5 parent in the Methodology's function-specific sense.

## Recursion

One session has an autonomous operational agent loop. Tool invocations, repeated `/goal` turns and alternative provider engine adapters are not independently viable child organizations. Multiple independent local users are outside the selected recursion boundary.

## Variety and escalation

Retries, compaction, tool caps, interruption-safe history pairing and user approval attenuate operational variety. A denied tool or blocked goal returns to the user for ordinary task-level intervention; the notification does not itself establish a metasystem or algedonic channel.

## Evidence gaps

No actual Windows GUI/provider end-to-end or live autonomous tool execution was conducted. Source wiring and code tests, rather than live model outcomes, support the S1 mapping. Parallel independent sessions, enterprise governance and outside operator composition are not credited. The source-level negative scopes are limited to the shipped reviewed modes and may change after a new supported organizational mode appears.
