---
harness_id: dendrophis
project_name: Dendrophis
repository: https://github.com/sp1d3rx/dendrophis
review_ref: dbc8e7883e7473f9450865d511d91e30c58724e2
reviewed_at: 2026-10-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Dendrophis

## Review boundary

- System in focus: the shipped Dendrophis Python terminal coding-agent runtime at the frozen revision, including the main chat/model-tool loop, first-party tools, synchronous specialized subagents, persistent memory, project primer, permission/sandbox path, session persistence and standard TUI/CLI surfaces.
- Purpose and identity: a local terminal coding agent that performs repository work, can delegate bounded specialist tasks, can independently review supplied diffs/files through a dedicated reviewer model context, and can preserve model-selected long-term lessons/context for later work.
- Relevant environment: the current project/workspace, local filesystem and sandboxed shell, configured OpenAI-compatible provider/model, optional MCP tools, persistent local memory/primer/session stores, and user approval surface.
- Standard-distribution boundary: Dendrophis repository code, bundled system prompts, built-in tools/subagent handlers and local persistence mechanisms. External model providers, MCP servers and operating-system enforcement are dependencies rather than credited owners.
- Credited operating / distribution surfaces: `dendrophis/session`, `dendrophis/tools`, `dendrophis/subagents`, `dendrophis/memory`, bundled prompts/configuration and supported TUI/CLI entry paths that instantiate those mechanisms.
- Adjacent first-party surfaces excluded from ownership: repository tests/benchmarks/proposals, screenshots/documentation-only claims, and external provider/MCP behavior except where first-party runtime wiring makes the decision path reachable.
- First-party operating / deployment modes considered: standard local coding session; model-callable `invoke_subagent`; code-writer/code-reviewer specialist modes; default persistent memory with model-callable save/search/recall tools and automatic memory association; optional project-primer workflow.
- Recursion level: one Dendrophis coding session is the system-in-focus; specialist subagents are subordinate task units invoked synchronously by the parent.
- Reviewed revision: `dbc8e7883e7473f9450865d511d91e30c58724e2`.
- Observation date: 2026-10-07.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The main `ChatOrchestrator` repeatedly streams a model response, records assistant/tool-call state, executes first-party tools through `SessionToolExecutor`, appends results to context and returns to the model until completion. File, shell, Python, memory, todo, interaction and subagent tools are first-party capabilities subject to permission/sandbox controls.

`invoke_subagent` synchronously dispatches one of six specialist handlers. The code-writer is an autonomous nested coding loop with filesystem/bash tools and verification instructions. The code-reviewer is materially different: it creates a fresh system/user message pair, directly reads named repository files and/or a supplied diff, exposes no edit/tool loop, optionally uses a dedicated reviewer model, and returns a structured approval/changes-requested/comment judgment.

The main system prompt explicitly instructs the model to use `save_memory` for project conventions, preferences, lessons, architectural decisions and bug fixes, and to search memory before starting tasks. Saved entries persist in SQLite across sessions. The standard session also constructs `MemoryAssociationGenerator`, which periodically retrieves relevant prior memory from the current user prompt and injects the surfaced summary into model context. Project primers are a separate user-invoked persistence path and are supporting evidence only for S4.

Primary evidence:
- [main chat loop](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/chat.py)
- [session tool execution](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/tools.py)
- [subagent tool](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/subagents.py)
- [subagent executor](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/executor.py)
- [code reviewer](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/handlers/code_reviewer.py)
- [code reviewer specification](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/specs/code-reviewer.md)
- [memory tools](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/memory.py)
- [memory association](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/memory/association.py)
- [system prompt](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/system_prompt.md)

## Operational model

The main model owns the focal coding operation. Specialist calls are ordinary synchronous tool calls: the parent waits for one `invoke_subagent` result before continuing. Internal subagent task IDs/status records support execution/accounting but are not exposed as a parent live-control surface.

The code-reviewer receives a fresh review-only prompt and direct diff/file evidence, so its judgment is complementary to the implementing parent/code-writer path even when it uses the same configured base model.

Long-term memory is model-writable. The main prompt assigns a prospective use: preserve conventions/preferences/lessons/architecture/bug fixes and search them before later work. Persisted entries can later be retrieved explicitly or automatically surfaced by the association generator into a later turn.

## S1 — Operations

- State: A
- Function: perform coding work by selecting first-party tools, inspecting/modifying files, running commands/code and iterating from returned results.
- Disturbance / variety regulated: user requirements, repository state, tool/test failures, provider outputs, file changes and permission/sandbox outcomes.
- Decisive decision or feedback right: choose the next coding/tool action, interpret results, change approach, delegate a specialist task and decide when the requested work is complete.
- Decision owner: the main Dendrophis model loop; code-writer may own a bounded delegated implementation task.
- Supporting / enforcement mechanisms: ChatOrchestrator, tool registry/executor, permission policy, bash sandbox, context manager, session persistence, compaction and specialist invocation.
- Closure path: user input → model decision → first-party tool/subagent action → returned result → next model decision → further action or terminal response.
- Boundary reachability: the standard shipped session initializes this loop and tool surface.
- Why this is / is not agent-owned: deterministic Python code executes/persists/constrains actions, but the model chooses task-specific operations and reacts to their results.
- Evidence: [session/chat.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/chat.py), [session/tools.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/tools.py), [config/system_prompt.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/system_prompt.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: individual operations can be denied or require user confirmation.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced first-party inter-S1 interference-attenuation loop is established.
- Disturbance / variety regulated: not established as S2.
- Decisive decision or feedback right: none meeting S2 closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: specialist roles, structured messages, `modifies_files` metadata and documentation claiming sequential execution within plans/parallel where dependencies allow.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the standard `invoke_subagent` path awaits one specialist execution and the session tool executor runs approved calls sequentially. The frozen runtime does not wire distinct concurrently viable S1 units to file/worktree ownership, conflict detection, dependency-frontier control or another concrete interference-attenuation feedback loop.
- Evidence: [subagents/specs/README.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/specs/README.md), [tools/builtins/subagents.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/subagents.py), [session/tools.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/tools.py).
- Basis: structural.
- Confidence: high.
- Caveats: role decomposition and a statement that work may be parallel are not credited without a frozen reachable coordination mechanism.

### Absence scope

- Surfaces inspected: subagent specs/registry/executor/tool, session tool scheduler, code-writer/reviewer/test/research roles.
- Plausible first-party paths checked: multiple tool calls, `modifies_files` metadata, documented dependency parallelism, specialist delegation.
- Why no material first-party path remains: execution is synchronously returned through one tool call and no inter-worker collision/dependency control relation is wired.

## S3 — Inside-and-now control

- State: —
- Function: no model-facing whole-current control loop over a live set of subordinate operational commitments is established.
- Disturbance / variety regulated: not established as S3.
- Decisive decision or feedback right: none meeting S3 closure.
- Decision owner: none established.
- Supporting / enforcement mechanisms: internal subagent task ids/status map, event-bus started/finished events, todo/sidebar/status telemetry and session cancellation.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: `invoke_subagent` blocks until the specialist returns; internal status is not exposed through model-callable list/wait/steer/kill/reprioritize controls over a live worker set.
- Evidence: [subagents/executor.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/executor.py), [tools/builtins/subagents.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/subagents.py).
- Basis: structural.
- Confidence: high.
- Caveats: observability/status data and user cancellation do not establish an agent-owned whole-current S3 loop.

### Absence scope

- Surfaces inspected: subagent status/events, session/TUI status, cancellation, tool execution, todo.
- Plausible first-party paths checked: internal task status lookup, task events, UI status, session cancel flag.
- Why no material first-party path remains: no current descendant/work portfolio is both visible to and controllable by the model while work remains active.

## S3* — Complementary audit

- State: A
- Function: independently inspect an implementation/diff claim through a dedicated read-only reviewer context and return an approval/changes-requested judgment to the parent.
- Disturbance / variety regulated: bugs, races, resource leaks, security issues, silent failures, architectural smells and style/correctness defects missed by the implementing path.
- Decisive decision or feedback right: inspect direct diff/file evidence and produce structured `approved`, `changes_requested` or `comment` judgment with blocker/warning/suggestion findings.
- Decision owner: the dedicated code-reviewer model invocation.
- Supporting / enforcement mechanisms: reviewer-specific system prompt, fresh two-message review context, direct disk reads of named files, optional dedicated reviewer model, no file mutation path, structured review schema.
- Claim being audited: the focal implementation/change is correct, robust and acceptable to land.
- Ordinary reporting path: main/code-writer implementation result, self-verification and tool outputs.
- Complementary access path: code-reviewer independently receives the diff and/or directly reads the named current files from disk rather than relying only on the implementer's narrative.
- Independence boundary: separate model invocation with reviewer-only system prompt, fresh message context, no edit/write tool loop and optional distinct `code_reviewer_model`.
- Who acts on findings: the parent receives the `invoke_subagent` tool result and can repair/re-run review before accepting completion.
- Closure path: implementation/change exists → parent invokes code-reviewer → reviewer independently inspects diff/files → structured verdict/findings return as tool result → parent can accept or perform corrective work.
- Boundary reachability: `code-reviewer` is an enumerated model-callable `invoke_subagent` mode and the standard system prompt tells the parent to use it for diff reviews.
- Why this is / is not agent-owned: the substantive audit judgment is produced by a distinct review model context with direct evidence access; deterministic parsing/transport does not make the judgment.
- Evidence: [handlers/code_reviewer.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/handlers/code_reviewer.py), [specs/code-reviewer.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/subagents/specs/code-reviewer.md), [tools/builtins/subagents.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/subagents.py), [config/system_prompt.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/system_prompt.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reviewer invocation is reachable/agent-selected rather than an unconditional completion gate.

## S4 — Outside-and-then intelligence

- State: A
- Function: select durable lessons/conventions/preferences/architecture knowledge from current experience and return it as reusable context for future Dendrophis work.
- Disturbance / variety regulated: repeated rediscovery of project conventions/architectural decisions, recurrence of prior bug patterns, stable user preferences and lessons that future coding turns could otherwise mishandle.
- External distinction: current repository/user/task experience supplies project conventions, preferences, architectural decisions, bug fixes and lessons distinct from the stored long-term memory state.
- Future / prospective distinction: the shipped system prompt explicitly directs the model to save those distinctions to long-term memory for later retrieval and to search memory before future tasks.
- Adaptation option generated: the model decides whether a distinction is worth persisting, chooses the memory content/tags/project association, or leaves memory unchanged; later it can select which stored memory to search/recall.
- Decisive decision or feedback right: decide which observed knowledge becomes durable future operating context and how it should be categorized for later retrieval.
- Decision owner: the main Dendrophis model through the first-party memory tools.
- A witness mode: during ordinary coding work the model calls `save_memory` for a verified lesson/convention/decision; SQLite persists it across sessions; a later session either searches/recalls it under the standard prompt or the standard MemoryAssociationGenerator surfaces a relevant match and injects its summary into context.
- Supporting / enforcement mechanisms: SQLite MemoryStore, save/search/recall tools, tags/project ids, system-prompt memory policy, MemorySearcher and automatic association generator.
- Closure path: current project/user experience → model judges a distinction worth retaining → `save_memory` persists selected long-term context → later user/task turn searches or automatically associates the stored item → retrieved memory is injected/returned into active model context → subsequent coding decisions can change under the learned guidance.
- Boundary reachability: memory tools are built into the standard tool surface and the standard Session constructs MemoryAssociationGenerator whenever a MemoryStore is present.
- Path back into current capability / S3: stored guidance returns through `search_memory`/`recall_memory` tool results or automatic association injection into the main model context, where it informs present operational/delegation decisions in later turns/sessions.
- Why this is / is not agent-owned: SQLite/search/association machinery stores and retrieves content, but it does not decide which project lesson/preference/architectural distinction deserves durable retention; that prospective selection and content choice belongs to the model.
- Evidence: [config/system_prompt.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/system_prompt.md), [tools/builtins/memory.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/tools/builtins/memory.py), [memory/memory.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/memory/memory.py), [memory/association.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/memory/association.py), [session/session.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/session/session.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: project primer persistence is not needed for this positive claim; S4 rests on model-selected durable memory plus a demonstrated return path to later active context.

## S5 — Policy and identity

- State: —
- Function: no runtime first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: no model-backed authority to resolve Dendrophis identity/purpose/ultimate-policy tensions is established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system prompt, permission categories, confirmation gates, custom project prompt, configuration, sandbox and user controls.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: permissions, confirmation and prompt/configuration constrain ordinary action, while ultimate authority remains external user/developer configuration rather than a first-party identity-governance actor.
- Evidence: [config/system_prompt.md](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/system_prompt.md), [config/defaults.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/config/defaults.py), [permissions/policy.py](https://github.com/sp1d3rx/dendrophis/blob/dbc8e7883e7473f9450865d511d91e30c58724e2/dendrophis/permissions/policy.py).
- Basis: structural.
- Confidence: high.
- Caveats: a human approval boundary is not S5 merely because the user can override/authorize an operation.

### Absence scope

- Surfaces inspected: system/custom prompts, permission policy, tool confirmation, configuration, memory/primer, subagent roles.
- Plausible first-party paths checked: custom `system.md`, permission categories, user confirmations, memory adaptation, project primers.
- Why no material first-party path remains: no runtime actor is authorized to adjudicate identity/ultimate-policy questions and return a binding resolution into later operation.

## Distributed OSS parent arrangement

Repository maintainer governance is outside the assessed runtime. No parent-mode state is inferred from GitHub project ownership or from a user's ability to edit configuration/prompts.

## Self-hosted and non-human modes

Dendrophis is a self-hosted local runtime. Operator permission/configuration and OS/sandbox boundaries constrain action but do not negate the autonomous S1/S3*/S4 witness modes above or create parent-governed metasystem states.

## Recursion

The main coding session is the system-in-focus. Specialist subagents are synchronous subordinate units, not independently viable recursive organizations.

## Variety and escalation

The system absorbs operational variety through direct tools, specialist delegation, permission/sandbox feedback, independent code review and durable memory. Reviewer blockers and stored lessons can change subsequent parent decisions, but no live subordinate portfolio control (S3) or identity-level governance (S5) is established.
