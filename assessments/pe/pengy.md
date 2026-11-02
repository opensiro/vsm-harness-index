---
harness_id: pengy
project_name: Pengy
repository: https://github.com/patw/Pengy
review_ref: 99b22849176c98ba8f5414edd8817b87cb2fea78
reviewed_at: 2026-11-02
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

# Pengy

## Review boundary

- System in focus: Pengy's first-party Python agent core running through its supported CLI, Web or optional desktop frontend.
- Purpose and identity: Local-first personal assistant that iterates over model-selected tools, maintains chat history and supports reusable skill instructions.
- Relevant environment: User prompts, local files/processes, browser/search inputs, model endpoints, tool permissions and context-window limits.
- Standard-distribution boundary: Published Python CLI and Web package plus the optional Qt GUI, all sharing the same first-party chat/tool core. The related standalone PengyR/PengyCPP ports are not included.
- Credited operating / distribution surfaces: `pengy/core/llm_client.py`, `tools.py`, frontend invocations, chat/context recovery, installed local skills and user permission modes.
- Adjacent first-party surfaces excluded from ownership: Tests/fixtures, distribution builds, reusable prompt-template authoring, repository contributors, third-party model providers and independent Rust/C++ projects.
- First-party operating / deployment modes considered: CLI one-shot/REPL, Web UI, optional GUI, configurable tool-confirmation and local skills; the modes share the same single model/tool decision loop.
- Recursion level: One Pengy chat/agent operating at the user-machine boundary; multiple UI tabs and sessions do not automatically constitute distinct interacting S1 units.
- Reviewed revision: `99b22849176c98ba8f5414edd8817b87cb2fea78`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `LLMClient.chat` generator sends a system/user/tool transcript to a configured OpenAI-compatible endpoint with the first-party JSON-schema tool list, dispatches model tool calls and feeds their outputs back into the next request. CLI, Flask Web UI and optional Qt GUI adapt this core, and do not own separate organization-level decisions. Chat history and context-recovery checkpoints are local. `task_manager` stores editable prompt macros rather than an autonomous schedule or fleet controller. Optional skills are instructions and helper scripts. Per-tool approval, retries, local memory, context compaction and error recovery support the focal S1, not separate VSM functions on their own.

## Operational model

A single model actor performs the user's requested work, with local runtime and human permission gates. No supported first-party mode was identified where a separate manager, coordination critic, complementary auditor, prospective strategy actor or ultimate-policy decision path owns organization-level discretion. The assessment does not import autonomy from model providers, manually authored tasks or related ports.

## S1 — Operations

- State: A
- Function: Iteratively choose and execute user-relevant tools based on results.
- Disturbance / variety regulated: Evolving user requests, environmental observations, tool failures, context limits and interrupted interactions.
- Decisive decision or feedback right: Select next action/tool call or final answer after tool results are observed.
- Decision owner: The model acting inside the shipped Pengy chat loop.
- Supporting / enforcement mechanisms: OpenAI-compatible client, JSON-schema tools and dispatcher, confirmation modes, context recovery and persistent per-chat histories.
- Closure path: Chat context → model response/tool call → local execution/approval → tool result appended → new model turn or completed reply.
- Boundary reachability: The CLI/Web/Qt entry points all invoke the same shipped `LLMClient.chat` generator; ordinary user/provider configuration completes the normal deployment.
- Why this is / is not agent-owned: The model chooses substantive operational actions, while the user may deny a tool and the deterministic runtime handles transport and retries.
- Evidence: [core chat/tool loop](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/llm_client.py), [tool registry/execution](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/tools.py), [CLI entry](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/cli/main.py), [README operating modes](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No actual model API call or end-to-end hosted deployment was reproduced in this review.

## S2 — Coordination

- State: —
- Function: No distinct inter-S1 interference attenuation loop is shipped at this boundary.
- Disturbance / variety regulated: Potential conflicts among independently operating task units.
- Decisive decision or feedback right: None for organization-level coordination.
- Decision owner: No qualifying S2 owner established.
- Supporting / enforcement mechanisms: Multiple chats/UI tabs, serialized per-chat tool turns, task prompt templates and filesystem locks.
- Closure path: No S2-specific returned coordination outcome; each user chat remains a separate S1 interaction.
- Why this is / is not agent-owned: UI multiplicity, sequential tool calls and shared local files do not evidence autonomously coordinated S1 units with a conflict/oscillation feedback loop.
- Evidence: [chat storage and index locking](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/chat_manager.py), [prompt-template tasks](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/task_manager.py), [agent core](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/llm_client.py).
- Basis: structural.
- Confidence: high.
- Caveats: Custom external multi-agent orchestration is outside the reviewed distribution.

### Absence scope

- Surfaces inspected: Published frontends, agent loop, per-chat persistence, task templates, tools and README.
- Plausible first-party paths checked: Parallel tabs/chats, task templates, local index locking, shared skill directory and tool execution.
- Why no material first-party path remains: No implemented relation establishes distinct S1 units, an inter-unit interference witness and a returned coordination correction changing subsequent unit behavior.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned whole-system current-control loop is supplied.
- Disturbance / variety regulated: Potential workload/capacity/priority disturbances across an operational whole.
- Decisive decision or feedback right: None beyond single-session tool choices and user approval.
- Decision owner: No qualifying S3 actor or parent feedback loop established.
- Supporting / enforcement mechanisms: Tool approval, cancel/retry, context pressure, error events, local UI task controls and prompt-template CRUD.
- Closure path: Local tool/turn control returns to S1; no whole-system manager regulates shared current commitments.
- Why this is / is not agent-owned: Human tool confirmation and deterministic cancellation do not amount to parent current-control of an organization; task templates are not a current workload manager.
- Evidence: [LLMClient confirmation and recovery](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/llm_client.py), [task manager](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/task_manager.py), [context recovery](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/context_recovery.py).
- Basis: structural.
- Confidence: high.
- Caveats: An operator may terminate a task, but no S3 parent mode is inferred from that alone.

### Absence scope

- Surfaces inspected: Core loop, approval/cancel paths, frontend descriptions, task manager and context recovery.
- Plausible first-party paths checked: User confirmation modes, cancellation, history/sidebar, error retries and task templates.
- Why no material first-party path remains: The inspected paths constrain or resume individual S1 turns and do not supply a separate whole-system view, current supervisory discretion and returned change to shared operations.

## S3* — Complementary audit

- State: —
- Function: No independent complementary reality-check and returned correction mechanism is shipped in the standard agent mode.
- Disturbance / variety regulated: Potential false claims of correctness after a tool action.
- Decisive decision or feedback right: No independent audit judgment over the operational output.
- Decision owner: No qualifying audit actor.
- Supporting / enforcement mechanisms: Tool confirmations, diff previews, app tests and optional read-only checks expressed in user-authored prompt templates.
- Closure path: Ordinary tool results and user feedback return to S1; no separate S3* findings-to-correction loop is established.
- Why this is / is not agent-owned: Developer tests and confirmation/diff UI do not create a complementary agent or independent audit judgment with corrective feedback.
- Evidence: [tool execution/confirmation](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/tools.py), [core chat](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/llm_client.py), [task templates](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/task_manager.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Users could install a third-party reviewer skill, but no first-party independent corrective loop is credited from hypothetical composition.

### Absence scope

- Surfaces inspected: Shipped tool registry, approval/diff paths, task-template runtime, skills documentation and chat loop.
- Plausible first-party paths checked: Tests, diff preview, user approvals, reusable review-checklist prompts and skill scripts.
- Why no material first-party path remains: These are task-level checks or potential custom instructions, without a separately packaged first-party complementary evidence access/independent verdict/returned author correction relationship.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective external environment-to-capability adaptation decision path is supplied.
- Disturbance / variety regulated: Long-run mismatch between available capability and changing environment.
- Decisive decision or feedback right: None for new future operating strategy or capability selection.
- Decision owner: No qualifying S4 owner identified.
- Supporting / enforcement mechanisms: Context summaries, memory-skill CRUD/search, local session history, user-selected models and optional skill installation.
- Closure path: Past context and recalled notes may affect ordinary next S1 turns, not a prospective adaptation program.
- Why this is / is not agent-owned: Persistence, summarization, local memory, model preferences and user-managed skill import do not themselves select/exercise externally informed future capability change.
- Evidence: [context recovery](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/context_recovery.py), [memory skill](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/assets/skills/memory/memory.py), [skill install](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/skills_install.py).
- Basis: structural.
- Confidence: high.
- Caveats: A user can manually alter installed tools; that is not evidence of a first-party S4 adaptation loop.

### Absence scope

- Surfaces inspected: Memory persistence/search, context compaction, skills installation, models/configuration and current chat loop.
- Plausible first-party paths checked: Long-term notes, automatic summary, model switching, user-managed skill extensions and prompt-template reuse.
- Why no material first-party path remains: No supported path separately senses outside-and-future conditions, proposes options and returns an adaptation decision to current system capability.

## S5 — Policy and identity

- State: —
- Function: No live identity/ultimate-policy arbitration and return path is supplied.
- Disturbance / variety regulated: Possible disagreement over the assistant's ultimate purpose/legitimate authority.
- Decisive decision or feedback right: No first-party ultimate-policy decision process; static user/system configuration constrains task execution.
- Decision owner: Ordinary user/configuration choices; no evidenced S5 function at the declared recursion.
- Supporting / enforcement mechanisms: Local settings, model selection, system message, approval mode, skill pointers and safe tool constraints.
- Closure path: Configuration is read into a session; no function-specific identity dispute → legitimate authority → returned governing decision is observed.
- Why this is / is not agent-owned: Tool permissions and user preference edits control S1 behavior; they do not independently establish identity-policy adjudication.
- Evidence: [configuration](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/config.py), [LLMClient tool confirmation](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/pengy/core/llm_client.py), [README](https://github.com/patw/Pengy/blob/99b22849176c98ba8f5414edd8817b87cb2fea78/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: The open-source project's own governance and external provider terms are not credited as runtime S5.

### Absence scope

- Surfaces inspected: Settings/configuration, system prompt/skill injection, tool permission modes, user frontends and maintainer-facing docs.
- Plausible first-party paths checked: User choices, prompt/config changes, tool approval and developer release decisions.
- Why no material first-party path remains: No operational identity-level matter is routed to a legitimate parent, authoritatively resolved and fed back as a new governing policy within the first-party harness.

## Distributed OSS parent arrangement

The open repository's maintainers control distribution; that does not create an operational S3/S4/S5 parent mode in an installed Pengy chat. Multiple users run separate local instances, not a shared organizational recursion.

## Self-hosted and non-human modes

CLI, Web and GUI each expose the same core chat loop. Local Ollama and hosted APIs are model transports; neither contributes its internal agent organization. Operator confirmations and model selection remain ordinary run configuration.

## Recursion

Multiple chats, tools and templates are not independently viable recursive S1 organizations; no additional VSM recursion established.

## Variety and escalation

Recovery, context pressure and timeouts feed back into S1 with user visibility. Cancellation and permission denials are ordinary bounded control, not automatic algedonic, S3 or S5 evidence.

## Evidence gaps

No provider request or GUI/Web end-to-end behavior was exercised. The negative scope is the shipped Python core and documented supported modes at the frozen source, not third-party skills or future extensions.
