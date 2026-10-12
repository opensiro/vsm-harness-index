---
harness_id: xoder
project_name: Xoder
repository: https://github.com/BANGHlxbackout/Xoder
review_ref: 5a13d1cd4471cf95bb89befe2ac7634d93a610a7
reviewed_at: 2026-10-12
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

# Xoder

## Review boundary

- System in focus: the first-party Xoder coding application implemented by `xoder_coding` on its own `xoder_agent` typed agent loop and `xoder_ai` provider-adapter layer, at the frozen ref.
- Purpose and identity: a terminal coding agent that accepts model-directed file/shell actions, persists sessions, and allows user-customized Python tool/command extensions.
- Relevant environment: a user-selected local project, filesystem, shell, configured external model provider, project/user context files, durable local JSONL sessions, and optionally user-trusted Python extensions.
- Standard-distribution boundary: packaged `xoder_agent` brain and `xoder_coding` instantiated coding TUI/CLI/print application, supported bundled four coding tools, packaged skills and default run/session paths. `xoder_ai` transports model requests but does not own an organizational decision. Third-party providers, local user extensions, independent SDK-built apps, developer test/CI infrastructure are adjacent, not automatic evidence donors.
- Credited operating / distribution surfaces: `src/xoder_agent/loop.py`, `harness.py`, `tools.py`, `src/xoder_coding/session.py`, `tools.py`, `system_prompt.py`, first-party CLI/TUI, shipped `create-xoder-extension` skill and extension loading/reload infrastructure insofar as they are accessible from this application.
- Adjacent first-party surfaces excluded from ownership: demonstration extensions under `examples/`, repository CI/tests, contributor/dev governance, generic use of the reusable SDK by outside teams, downstream user extensions/scripts, externally configured model providers and hypothetical future multi-agent applications.
- First-party operating / deployment modes considered: default TUI/print coding agent, queued steering/follow-up turns, durable session branching/compaction, bundled skill routing, user opt-in project extensions, user extension reload, and reusable AgentHarness constructor API. An external multi-agent app assembled from the SDK is a different boundary.
- Recursion level: one executing Xoder coding session; its turns and tool calls are internal S1 operations. No shipped subordinate multi-agent S1 collection was identified.
- Reviewed revision: 5a13d1cd4471cf95bb89befe2ac7634d93a610a7.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The core is deliberately split into provider `xoder_ai`, a reusable `xoder_agent` AgentHarness, and a complete `xoder_coding` coding product. The first-party `CodingSession.create` composes the four coding tools (read, write, edit and bash), model provider, loaded skill and context resources and optional explicitly trusted Python extensions, then builds AgentHarness. The agent loop streams model output and typed events, executes model-chosen calls, appends structured tool feedback and continues; new steering/follow-up messages can be queued into the same session. A single harness rejects simultaneous independent prompts while running.

Session JSONL records, persistent branch/replay and compaction restore task context. File locks serialize writes to the same path; this is local tool consistency, not an inter-worker coordinator. Extensions can add tools, slash commands, event interceptors and custom UI. They are loaded from the user's configured paths and require an explicit flag to load project-local executable Python. Shipped skills instruct a model how to fulfill a user request to create an extension or update a model catalog; the runtime can reload the result.

Primary frozen first-party evidence: [loop](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/loop.py), [harness](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/harness.py), [coding composition](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/session.py), [built-in tools](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/tools.py), [extension trust](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/extensions/loader.py), [extension skill](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/skills/create-xoder-extension/SKILL.md), [system routing](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/system_prompt.py).

## Operational model

The running model owns task-specific coding discretion and obtains its own tool feedback. The Python runtime provides turns, cancellation, queues, storage and enforcement as supporting mechanisms. User/host extension settings grant executable functionality but are not organizational S2/S3/S4/S5 decision rights by default. The parent-human operator can interrupt the current task and change configuration; a genuine parent metasystem mode is not established simply by operator access.

## S1 — Operations

- State: A
- Function: perform actual coding work by selecting read/write/edit/bash tools and iterating from tool and model feedback.
- Disturbance / variety regulated: variable user tasks, file state, execution results, provider errors and tool outcomes.
- Decisive decision or feedback right: choose successive task-specific code/tool actions and change course from returned observations.
- Decision owner: model executing through AgentHarness within CodingSession.
- Supporting / enforcement mechanisms: provider adapters, typed tool events, Python async dispatch, session JSONL storage, context compaction and UI.
- Closure path: user request → model proposes action → first-party coding tool executes → structured result becomes model context → further action or completion.
- Boundary reachability: the supported TUI and print-mode CLI compose CodingSession with the repository's AgentHarness and four default coding tools.
- Why this is / is not agent-owned: the model owns discretionary coding steps; Python modules dispatch and constrain them.
- Evidence: [agent loop](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/loop.py), [harness](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/harness.py), [coding session](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/session.py), [coding tools](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/tools.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider is an external model execution dependency, not a second first-party operational organization.

## S2 — Coordination

- State: —
- Function: no qualified first-party inter-S1 interference attenuation at this recursion.
- Disturbance / variety regulated: none specifically regulated between multiple independent S1 units.
- Decisive decision or feedback right: no S2-specific conflict/oscillation feedback right.
- Decision owner: none established.
- Supporting / enforcement mechanisms: steering/follow-up queues; per-path file locks; sequential model tool dispatch.
- Closure path: not applicable; queues affect the order of inputs to one running agent, and file locks serialize individual writes.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: a mailbox or serialization mechanism is not evidence of competing independent S1 units and reciprocal interference regulation.
- Evidence: [queues](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/harness.py), [tool dispatch](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/loop.py), [file locks](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/tools.py).
- Basis: structural.
- Confidence: high.
- Caveats: consumer-built fleets on top of the SDK are outside the shipped coding-session boundary.

### Absence scope

- Surfaces inspected: src/xoder_agent/harness.py, src/xoder_agent/loop.py, src/xoder_coding/tools.py and CodingSession startup.
- Plausible first-party paths checked: queues, file locks, multi-tool turns, extension hooks, independently composed SDK instances.
- Why no material first-party path remains: these are one-session control or generic construction facilities without a shipped multi-S1 interference-specific coordinating feedback loop.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current operational manager governing a portfolio of independent S1 commitments.
- Disturbance / variety regulated: session capacity, pending prompts and tool failures affect execution but do not establish management of multiple operating units.
- Decisive decision or feedback right: no management right over all subordinate work units that adjusts priorities/resources across them.
- Decision owner: none established.
- Supporting / enforcement mechanisms: is_running, event listeners, steering/follow-up queue, cancellation, context estimation and session stats.
- Closure path: not applicable; system primarily resumes or changes one agent's operational turn.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: one-agent queue and TUI observation do not form whole-current control authority; no distinct parent-operator mode with returned S3 control identified.
- Evidence: [single active harness](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/harness.py), [session state](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/session.py), [TUI](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/tui/app.py).
- Basis: structural.
- Confidence: high.
- Caveats: operator can stop or reconfigure one session; ordinary human intervention does not automatically create S3=P.

### Absence scope

- Surfaces inspected: harness and coding-session run lifecycle, TUI state, session manager, extensions.
- Plausible first-party paths checked: queued inputs, cancel/interrupt, session branch/reload, token/context status, extension event callbacks.
- Why no material first-party path remains: no independently supervised collection of operating S1 units or whole-current resource/commitment control with consequential return path is shipped.

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary audit of operating claims via separate direct-evidence access and corrective closure.
- Disturbance / variety regulated: coding errors and false completion claims are task-local concerns but lack a dedicated audit organization.
- Decisive decision or feedback right: none distinct from normal model action or user-chosen external extension.
- Decision owner: none established.
- Supporting / enforcement mechanisms: read tool, bash/test checking, log/typed events, extension hooks, custom tool registration and user project instructions.
- Closure path: not applicable; the same operating agent can inspect and validate its own changes but there is no shipped separate auditing actor with corrective feedback.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: arbitrary customer-authored review plugins are possible, but the standard coding distribution does not instantiate their independent judgment/feedback loop.
- Evidence: [same-turn tool feedback](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_agent/loop.py), [read/bash tools](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/tools.py), [generic hooks](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/extensions/runtime.py), [extension surface](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/docs/extensions.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user-provided audit extension could produce another topology; it is not a shipped first-party mode at the reviewed ref.

### Absence scope

- Surfaces inspected: default tools and prompt, harness run loop, packaged extensions and skills, session hooks, tests and docs.
- Plausible first-party paths checked: self-review, test execution, extension hook review, hypothetical external review agents.
- Why no material first-party path remains: no first-party independent reviewer executing direct artifact inspection and returning decisions capable of altering normal operations has been wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported organizational outside/future intelligence adaptation loop distinct from current user-requested coding and customization.
- Disturbance / variety regulated: new model/provider information and missing user features can be acted on in tasks; no autonomous future-capability scanning and adoption decision loop is shown.
- Decisive decision or feedback right: the user requests extensions or provider catalog edits; the current coding agent may implement that task but no separately supported prospective adaptation judgment is wired.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: packaged create-xoder-extension skill, built-in model catalog guidance, provider selection, user extensions and reload, project context and session memory.
- Closure path: not applicable to S4; an explicitly requested extension can be written and loaded but this alone does not close sensing → prospective adaptation judgment → future capability change.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the model may autonomously implement a user's present customization request; that is S1 coding discretion, not evidence that the organization autonomously selects and closes prospective adaptation against outside distinctions.
- Evidence: [extension-creation skill](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/skills/create-xoder-extension/SKILL.md), [model catalog skill](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/skills/xoder-model-catalog/SKILL.md), [task-directed instructions](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/system_prompt.py), [session/reload](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/session.py), [extension composition](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/extensions/runtime.py).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: unlike Capstan's explicit repeat-use self-improvement guidance, the shipped Xoder skill declares 'Use for Xoder extension requests'; an external extension or user policy could supply a new S4 loop.

### Absence scope

- Surfaces inspected: shipped skill index, both bundled skills, prompt routing, extension APIs/load/reload, provider catalog and session persistence.
- Plausible first-party paths checked: user-requested future extension, user-initiated provider catalog update, reusable prompts/skills, memory/context compaction, custom event hooks.
- Why no material first-party path remains: none contains a first-party future-directed environment sensing and model-owned adaptation selection whose decision returns into subsequent system capability beyond current user task.

## S5 — Policy and identity

- State: —
- Function: no legitimate whole-system ultimate identity/purpose reconciliation authority that returns constitutional policy to operations.
- Disturbance / variety regulated: local user trust, extension loading, provider selections and tool configuration affect runtime but not a metasystemic purpose choice.
- Decisive decision or feedback right: no first-party constitutional identity-policy decision right, autonomous or qualifying parent-owned.
- Decision owner: none evidenced.
- Supporting / enforcement mechanisms: system prompt, user/project AGENTS.md, extension trust flag, credentials and session preferences.
- Closure path: not applicable; user settings adjust operational conditions without an organizational purpose/identity adjudication path.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: provider/model choice and user extension permission are operational policy, not legitimate purpose/identity authority; a model cannot infer that role from editing project instructions.
- Evidence: [system prompt](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/system_prompt.py), [project extension trust](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/extensions/loader.py), [settings](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/session.py), [extension trust docs](https://github.com/BANGHlxbackout/Xoder/blob/5a13d1cd4471cf95bb89befe2ac7634d93a610a7/src/xoder_coding/data/docs/extensions.md).
- Basis: structural.
- Confidence: high.
- Caveats: a separately composed human governance organization would require explicit different boundary evidence.

### Absence scope

- Surfaces inspected: system prompt, CLI/extension trust, user/project resource policy, credentials, session and provider configuration.
- Plausible first-party paths checked: project trust, security approval, agent prompt editing, custom extension hooks, operator selection.
- Why no material first-party path remains: no dedicated first-party identity-purpose matter → legitimate deciding owner → returned organizational policy loop exists at this scope.

## Recursion

This assessment classifies the shipped coding session, not a future application created from the generic SDK or a user fleet. The serialized tool-call and event sequence are operational subtasks inside the primary S1 unit. Independent model/provider accounts or separately started terminal sessions are not evidence of a first-party coordinated subordinate S1 organization.

## Variety and escalation

The agent absorbs workspace variation through model/tool feedback, provider errors, cancellation and repair. Steering/follow-up queues alter the current agent's input stream, not a fleet of competing S1 units. Conflicting same-path file edits are serialized inside tool handlers; no function-specific S2 loop is inferred. User intervention, provider changes, skill edits or session reload can change operations, but do not by themselves prove S3/S4/S5 or algedonic regulation.

## Evidence gaps

- User-defined Python extensions may implement independent review, managers or future-adaptation policies; no such specifically wired first-party supported mode was identified in this revision. These potential consumer compositions do not require `?` absent a concrete shipped path.
- The built-in create-extension skill is an intentional current-task coding workflow. If later first-party evidence demonstrates independently selected outside-and-then adaptive capability improvement (as opposed to user-instructed customization), S4 deserves source-first reassessment.
- Source-first static inspection only; no live model/provider execution was needed or claimed. No blind independent reviewer has been invoked in this producer context.

