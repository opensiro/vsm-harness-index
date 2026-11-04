---
harness_id: baldric
project_name: Baldric
repository: https://github.com/Ember452/baldric
review_ref: fa92656923649291a52de1e05d77d5c72a4976e6
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Baldric

## Review boundary

- System in focus: The shipped Python Baldric terminal coding assistant and the reusable `baldric_agent` model/tool loop composed by `baldric_coding.AgentSession`.
- Purpose and identity: Accept a user's coding request, let the model select read/edit/write/shell actions, return tool feedback and keep a resumable coding session.
- Relevant environment: User-selected local project, shell/file tools, provider model and credentials, context-window limits, user-supplied steering, file changes and provider failures.
- Standard-distribution boundary: The released Python package's first-party `baldric_agent`, `baldric_coding` CLI/TUI/session, built-in coding tools, installed extension lifecycle and session persistence. An actual inference provider is external.
- Credited operating / distribution surfaces: [model/tool loop](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/loop.py), [stateful harness](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/harness.py), [coding session](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py), [coding tools](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/tools.py), [extension runtime](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/extensions/runtime.py).
- Adjacent first-party surfaces excluded from ownership: Developer tests, fake model backends, release/update checks, documentation examples, user-authored uninstalled extensions/skills, provider backend internals and maintainer governance.
- First-party operating modes considered: Interactive TUI or noninteractive CLI, resumed/forked session history, user steering/follow-up messages, project-trust decisions and optional local extension/provider adapters.
- Recursion level: One coding assistant session and its directly selected tools; no built-in portfolio of multiple S1 units was established.
- Reviewed revision: `fa92656923649291a52de1e05d77d5c72a4976e6` on 2026-11-04; generated/current Profile 0.2.4 and Methodology 0.3.7.

## Repository architecture

`baldric_ai` supplies model transports and provider-neutral events; `baldric_agent.run_agent_loop` streams a model response, validates and executes model-chosen tool calls, appends tool results, observes cancellation and repeats. `AgentHarness` owns steering/follow-up message queues and event subscriptions, while `baldric_coding.AgentSession` composes the provider, built-in file/shell tools, resource prompts, skills, trusted project configuration, extensions, durable session tree and TUI. Extension hooks and dynamic provider registration are explicitly optional implementation machinery. The user controls configuration and project trust; the model owns the coding decisions. [Architecture](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/data/docs/architecture.md), [loop.py#L52-L200](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/loop.py#L52-L200), [session.py#L680-L790](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py#L680-L790).

## Operational model

A model selects one coding action at a time against the repository, and the same session receives tool error/result feedback. The harness can persist, resume, fork, steer and attach dynamically loaded tools; none of those by itself installs a separate coordinating S2 unit, whole-system S3 allocator, independent audit, prospective adaptation unit or identity governor. Provider fallbacks and trust gates remain operational support at this recursion.

## S1 — Operations

- State: A
- Function: Implement user coding requests by iteratively choosing tools, inspecting outputs, revising edits and deciding when to answer.
- Disturbance / variety regulated: Unknown file layouts, failing commands, invalid tool arguments, changed requirements, provider/tool interruption and context limits.
- Decisive decision or feedback right: The model selects tool name/arguments and next coding action based on prior source and tool results.
- Decision owner: First-party model-directed `run_agent_loop` in a supported `AgentSession`; user provides the goal and project trust.
- Supporting / enforcement mechanisms: Built-in read/write/edit/bash tools, provider streaming, hooks, session persistence, cancellation and context preparation.
- Closure path: User prompt → model answer/tool call → first-party execution/result → transcript/event append → next model decision or final answer.
- Boundary reachability: `AgentSession` builds `AgentHarness` with real tool set, invokes its prompt/continue path and is launched by CLI/TUI.
- Why this is / is not agent-owned: The model returns substantive tool choices and code; fixed argument checks and tool execution only constrain chosen actions.
- Evidence: [loop.py#L58-L188](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/loop.py#L58-L188), [harness.py#L155-L199](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/harness.py#L155-L199), [session.py#L680-L745](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py#L680-L745).
- Basis: structural
- Confidence: high for an installed agent/tool feedback loop.
- Caveats: External live provider and coding task success were not independently run in this assessment.

## S2 — Coordination

- State: —
- Function: No first-party dedicated regulation of interference between distinct operational cells is established in the base coding session.
- Disturbance / variety regulated: Multiple tool calls and user steering can interact within one session, but do not prove cross-S1 collisions or oscillation.
- Decisive decision or feedback right: Identify an actual conflict between separate S1 work units and feed an adjustment into their subsequent work; not supplied.
- Decision owner: One agent owns its local coding sequence, deterministic runtime serializes/queues tool and user turns; no separate S2 actor.
- Supporting / enforcement mechanisms: Single-session tool dispatch, steering/follow-up queue mode, extension lifecycle locks and local file locks.
- Closure path: Model/tool events and queued user messages return to the same S1 loop, not to an S2 conflict resolution path spanning multiple S1 units.
- Why this is / is not agent-owned: A message queue and flexible tool/extension APIs do not by themselves implement the Methodology's distinct-S1 interference witness.
- Evidence: [harness.py#L31-L151](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/harness.py#L31-L151), [loop.py#L78-L188](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/loop.py#L78-L188).
- Basis: structural
- Confidence: medium-high at the one-session standard boundary.
- Caveats: Separate users can run independent Baldric processes; their organizational coordination is not shipped as a Baldric S2 mode.

### Absence scope

- Surfaces inspected: Stateful harness, concurrent provider/tool path, steering/follow-up queues, extension hooks, local coding tool locks and CLI session navigation.
- Plausible first-party paths checked: Multiple sequential tool calls, session fork/rewind, simultaneous independent local processes and extension-registered actions.
- Why no material first-party path remains: No shipped multi-S1 work portfolio with an explicit observed collision and returned cross-unit adjustment beyond generic action serialization.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current control plane over a portfolio of S1 units is evidenced at the session boundary.
- Disturbance / variety regulated: Model/tool request limits, session cancellations, provider replacement and extension lifecycle failures are managed as single-session execution constraints.
- Decisive decision or feedback right: Reallocate work, priorities, resources or commitments across multiple S1 units using a whole-system operating view; not evidenced.
- Decision owner: User chooses model, session, project trust and commands; deterministic runtime enforces session and provider lifecycle.
- Supporting / enforcement mechanisms: `max_turns`, model context handling, user `steer`/`cancel`, provider registry and cancellation-safe extension reload.
- Closure path: Local cancellation or provider replacement affects the same coding session; no whole-system S3 control decision returns to distinct operating units.
- Why this is / is not agent-owned: Model switch, rate cap, process cleanup and provider lifecycle guards are not a portfolio-level managerial actor.
- Evidence: [harness.py#L31-L199](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/harness.py#L31-L199), [session.py#L680-L790](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py#L680-L790).
- Basis: structural
- Confidence: medium-high.
- Caveats: An external team supervisor may manage many Baldric sessions but is outside this installed session.

### Absence scope

- Surfaces inspected: Provider routing, model choice, command/session controls, extension runtime, session events and tool execution.
- Plausible first-party paths checked: User stop/steer, extension cancellation, per-model context cap, project trust and provider hot reload.
- Why no material first-party path remains: These govern session mechanics; no distinct whole-system view and current resource/commitment intervention loop is wired.

## S3* — Complementary audit

- State: —
- Function: No complementary, independently sourced challenge and corrective audit channel is established for ordinary coding outputs.
- Disturbance / variety regulated: Incorrect code and false task completion claims remain possible; ordinary tests/commands return to the same agent or user.
- Decisive decision or feedback right: Independently sample code/task reality, issue a distinct challenge judgment and make it actionable through another control owner; not supplied.
- Decision owner: Single coding model may run a test tool; user may inspect history; no first-party independent audit actor is configured.
- Supporting / enforcement mechanisms: Tool results, session history, event log, diagnostic outputs, optional extension or user-invoked test commands.
- Closure path: Test output goes to the same S1 model as routine feedback; no separated audit finding with accountable returned control.
- Why this is / is not agent-owned: Running unit tests or retaining transcripts is operational feedback, not a separate complementary audit right.
- Evidence: [loop.py#L112-L190](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_agent/loop.py#L112-L190), [tools.py](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/tools.py).
- Basis: structural
- Confidence: medium-high.
- Caveats: A manually installed reviewer extension is a possible downstream organization, not a demonstrated bundled S3* mode.

### Absence scope

- Surfaces inspected: Model/tool callbacks, session history, tool registration, CLI output and extension customization.
- Plausible first-party paths checked: Automatic tool errors, shell test commands, hook-based verification, branch history and outside human observation.
- Why no material first-party path remains: No built-in independent evidence access, auditor decision owner and audit-result-to-operational-control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party sustained prospective environmental sensing and adaptation-option loop into future system capability is found.
- Disturbance / variety regulated: New coding requirements and changed models are handled in current context or user configuration.
- Decisive decision or feedback right: Sense outside/future change, decide a durable new harness strategy and feed it into later current operation; not established.
- Decision owner: User selects models, providers, prompts, skills and extensions; model makes current coding plans, not system-level future strategy revisions.
- Supporting / enforcement mechanisms: Session persistence, skill loading, updated model catalogs, a background PyPI update notice, resource reload and user-defined custom prompts.
- Closure path: A persisted transcript supplies context for resumed work; an update notice can prompt a human, but no adaptive future strategy is autonomously selected and applied.
- Why this is / is not agent-owned: Automatically checking package versions or composing user-added skills is not model-driven S4 environmental intelligence.
- Evidence: [session.py#L680-L790](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py#L680-L790), [update_check.py#L135-L190](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/update_check.py#L135-L190), [resource plan](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/resources.py).
- Basis: structural
- Confidence: medium-high at the base coding session.
- Caveats: A particular user may direct Baldric to design future capabilities as an ordinary coding task, but that is not an installed S4 feedback mode.

### Absence scope

- Surfaces inspected: Session/prompt memory, model and provider catalog updates, resource reload, skills, extensions and background version check.
- Plausible first-party paths checked: Cross-session reuse, new-version alerts, optional external extension installation, automatic provider refresh and model-generated plans.
- Why no material first-party path remains: Each is current S1 context or user/developer-driven composition; no prospective sensing/option authority and return into current operating capability.

## S5 — Policy and identity

- State: —
- Function: No runtime ultimate-policy/identity matter with legitimate judgment and a binding return to future operation is established.
- Disturbance / variety regulated: Untrusted project extensions, unsafe tools, denied approvals and provider configuration inconsistencies are handled by project trust and runtime guards.
- Decisive decision or feedback right: Set or revise an authoritative ultimate policy for this coding session organization after an identity-level dispute; no such loop exists.
- Decision owner: User/developer sets project trust, tool eligibility and extension permissions; the runtime executes these constraints, the coding model chooses ordinary actions.
- Supporting / enforcement mechanisms: Project-trust prompts, extension source identity checks, tool allowlist, cancellation, provider lifecycle and session limits.
- Closure path: Trust and approval choices enable or block tools; no identity-level question → authoritative parent or autonomous ruling → durable constitutional policy loop.
- Why this is / is not agent-owned: An enforced permission boundary is not by itself a VSM S5 governance body or a parent-mode closure.
- Evidence: [project_trust.py](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/project_trust.py), [session.py#L550-L705](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/session.py#L550-L705), [architecture](https://github.com/Ember452/baldric/blob/fa92656923649291a52de1e05d77d5c72a4976e6/src/baldric_coding/data/docs/architecture.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: Maintainer governance and installed extensions that may implement their own policy are separate recursions, not credited without concrete evidence.

### Absence scope

- Surfaces inspected: Project trust, user and project configuration, provider/extension registry, command/tool permissions, session lifecycle and CLI policy docs.
- Plausible first-party paths checked: Trusted-extension admission, runtime allowlist, user approval, reusable prompts and model/provider changes.
- Why no material first-party path remains: These are safety or configuration controls, with no ultimate identity issue, authoritative S5 judgment and returned binding future policy.

## Distributed OSS parent arrangement

Maintainers and different users can develop or configure Baldric instances, but no public first-party distributed human parent organization governs the identity of an individual installed coding session.

## Self-hosted and non-human modes

Different inference providers and local backends share the same first-party single-agent loop. Tool availability and project-trust preferences can differ by installation, but they do not supply S2/S3/S3*/S4/S5 ownership on their own.

## Recursion

The coding session is one S1 cell; history forks create alternative session paths, not a portfolio of co-operating operational units with a separately viable management layer.

## Variety and escalation

Model selection, coding tools and optional skills/extensions amplify the variety of tasks. Allowlist, project trust, typed tool arguments, session limits, context management and cancellation constrain unsafe execution. Errors return through the same model/tool path, while human extension decisions remain ordinary trust settings.

## Evidence gaps

- No live provider-backed coding session or correctness benchmark was independently reproduced; this assessment establishes architecture and decision ownership from pinned first-party source.
- Arbitrary user/developer extensions can alter behavior but are not function-specific first-party standard S2/S3/S3*/S4/S5 construction paths without an actual installed implementation.
