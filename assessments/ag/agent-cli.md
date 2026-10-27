---
harness_id: agent-cli
project_name: Agent CLI
repository: https://github.com/basnijholt/agent-cli
review_ref: 554344e6ed5266bcc2a7b1461d4c84744ff5e0af
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent CLI

## Review boundary

- System in focus: the first-party local-first Agent CLI distribution at the pinned revision: its conversational `chat` agent with built-in PydanticAI tools; voice/assistant and memory/RAG front ends as relevant support; and the explicitly shipped `dev` git-worktree manager with optional launches of supported external coding-agent executables.
- Purpose and identity: provide privacy-oriented local text/voice assistants and developer tools, including agentic tool use and separate coding workspaces for parallel tasks.
- Relevant environment: human utterances/prompts and clipboard, file/OS state, provider/model responses, memory history, separate git branch/index/worktree mutations, installed optional coding-agent binaries, remote repositories and integration conflicts.
- Standard-distribution boundary: Python package `agent_cli`, bundled `agent-cli dev` commands and bundled `agent-cli-dev` skill. External Claude/Codex/Gemini/Aider/OpenCode agents are supported hosted S1 actors only when launched through the documented first-party `dev` mode; their private metasystems, plugins, proprietary models and user/Claude parent organization are not imported as Agent CLI's own S2–S5.
- Credited operating / distribution surfaces: chat PydanticAI model/tool invocation and local memory/history; optional voice ASR/TTS I/O; `dev new` worktree creation and per-branch isolated subprocess launch; dev list/status/cleanup; the bundled dev skill describing reproducible supported parallel agent invocation. Pure service daemons do not acquire agentic ownership from the name.
- Adjacent first-party surfaces excluded from ownership: repository CI/testing/developer operations, documentation generation, macOS app installer/updater, external Claude Code plugin's supervisory model, external project maintainers, arbitrary prompted independent reviewers, user-configured MCP/provider extensions, external code-review workflows and third-party agent internals.
- First-party operating / deployment modes considered: normal local `agent-cli chat` with Ollama/OpenAI/Gemini compatible models; voice assistant/transcription, autocorrect and memory proxy; `agent-cli dev new` worktree-only and `--prompt`/`--prompt-file`/ `--start-agent` launch modes; CLI-managed separate branches, optional tmux/zellij agents and skill-driven parallel delegation. A shared-worktree multi-agent option is also documented but does **not** receive S2 worktree-isolation credit.
- Recursion level: one local Agent CLI installation/working repository with task-local conversational S1 and, in optional dev mode, multiple independent coding-agent S1 workers in separately provisioned checkouts. No first-party organization of their project portfolio is assumed merely because the tool can start them.
- Reviewed revision: `554344e6ed5266bcc2a7b1461d4c84744ff5e0af`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Agent CLI ships several independent commands, not one monolithic multi-agent runtime. Its `chat` command converts voice to user instructions, invokes `get_llm_response` with a PydanticAI agent and first-party file/search/command/memory tools, persists conversation history, and optionally speaks the answer. The model selects which tools to call during its task. Autocorrection/transcription/TTS, long-term fact extraction, RAG retrieval and their background daemons are functionally useful but do not themselves regulate a group of coding S1 units.

The `dev` command is a first-party worktree and process launcher. A caller chooses or generates a branch name, `create_worktree` creates a distinct git checkout, optional project setup runs, and `launch_agent` starts an installed coding-agent executable within that checkout, passing a task file when supplied. Multiple branch-local coding agents may mutate disjoint checkouts in parallel. The shipped `agent-cli-dev` skill tells an external parent assistant when and how to invoke this protocol; it does not make that external assistant an Agent CLI-owned global S3 or S3* auditor.

Pinned evidence: [README](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/README.md), [chat docs](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/commands/chat.md), [chat runtime](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/agents/chat.py), [LLM service](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/services/llm.py), [built-in tools](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/_tools.py), [dev guide](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/commands/dev.md), [dev CLI](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/cli.py), [worktree logic](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/worktree.py), [agent launch](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/launch.py).

## Operational model

For chat, user/voice text and history become model input. The model may read files, execute a bounded command, search or update memory, and use web search; tool results return to the agent's task-local reasoning before it responds and persists the exchange. In dev mode the user or an **outside** invoking assistant selects tasks/branches and calls `dev new`, which places each coding agent in a separate checkout. Worktree isolation prevents direct shared git-index and working-file interference, but dev status/cleanup and launch hooks remain fixed tools or human-invoked operations. No internal Agent CLI controller is evidenced making portfolio-wide task priority, recovery or acceptance decisions from all worker reports.

## S1 — Operations

- State: A
- Function: model-selected conversational tool use and, in dev mode, task-local autonomous coding by a managed external coding-agent process.
- Disturbance / variety regulated: open-ended natural-language tasks, file information gaps, command outcomes, search/memory feedback, implementation uncertainty and tool failures.
- Decisive decision or feedback right: select available tools and their arguments in response to a request/results, refine subsequent steps and return an answer or task result.
- Decision owner: the PydanticAI chat model for the first-party conversational S1; alternatively an installed external coding-agent executable launched as a supported `dev` worker for its own task. No external agent's hidden organizational metasystem is credited.
- Supporting / enforcement mechanisms: provider selection, ASR and TTS, `create_llm_agent`, `agent.run`, file/shell/search/memory `Tool` wrappers, saved history; optional spawned process and configured branch/worktree.
- Closure path: user request/transcribed text → first-party model-backed agent chooses tool actions → local tools return real data/error → agent continues/responds → output/history is recorded; in `dev` mode assigned prompt → launched coding agent uses its task loop in designated checkout → branch/result becomes available to the user/external caller.
- Boundary reachability: `agent-cli chat` constructs a PydanticAI Agent with first-party tools, calls `agent.run`, and is a documented installable command; `dev new --agent codex --prompt-file ...` and alternatives are supported launch paths.
- Why this is / is not agent-owned: the model-backed chat agent chooses which file/search/command tool to invoke; command implementations and audio transport alone are not the agent. Optional coding workers independently choose implementation actions, while Agent CLI only starts them.
- Evidence: [PydanticAI service](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/services/llm.py), [chat model call](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/agents/chat.py), [tool registry](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/_tools.py), [dev launch](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/cli.py).
- Basis: explicit + structural.
- Confidence: high for source-path reachability; medium for external coding agent task performance.
- Caveats: no actual provider-backed voice/chat/coding task was executed for assessment; nonagentic transcription and static text transformations alone are not the positive S1 evidence.

## S2 — Coordination

- State: C
- Function: deterministic checkout isolation between distinct concurrently executing dev-mode coding agents on a shared repository.
- Distinct S1 units: two or more independent installed coding agents launched into separate branch-specific worktrees of one source repository.
- Inter-S1 disturbance: concurrent changes to the same working directory, git index or checked-out branch can conflict, overwrite pending changes or corrupt assumptions of another S1 process.
- Attenuating coordination relation: `agent-cli dev new` provisions a separate git branch/worktree and launches the corresponding agent in that worktree; each later coding action addresses its dedicated mutable checkout, rather than a shared git index/working directory.
- Feedback into subsequent S1 behaviour: the new worktree path is passed as the agent's process working directory; subsequent reads/writes/git commands operate on that isolated state. Worktree creation failures are returned to caller instead of launching an agent in an unintended shared location.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: worktree provisioning regulates the concrete collision type of simultaneous checkout/index/file mutations by distinct coding agents. It is not scored because the tool can spawn agents or list sessions.
- Disturbance / variety regulated: mutable repository working-tree interference during parallel code changes, branch-switch side effects and git index contention.
- Decisive decision or feedback right: first-party CLI constructs a separate branch/checkout and chooses to execute the worker there after caller configuration.
- Decision owner: human/external parent selects whether/where to parallelize; deterministic Agent CLI code performs isolation (`C`). Agent CLI has no agent-owned inter-worker conflict judgment/negotiation loop.
- Supporting / enforcement mechanisms: `dev new`, `create_worktree`, `git worktree add -b`, branch-name validation, optional prompt file and cwd-scoped `launch_agent`, status/remove commands.
- Closure path: caller assigns different tasks/branches → Agent CLI creates separate worktree paths → separate S1 coding agents execute in those paths → direct shared-index/write collisions are attenuated while each worker returns its own result/branch for external integration.
- Boundary reachability: the normal installable `dev new ... --prompt` or `--prompt-file` path invokes `worktree.create_worktree` and `launch_agent`; README, dev guide and packaged skill explicitly document multiple independent coding tasks.
- Why this is / is not agent-owned: this isolation occurs because worktree provision is coded and selected through CLI flags; the spawned model agent need not detect/correct inter-worker conflicts. No adaptive S2 owner is shown, hence `C` rather than `A`.
- Evidence: [dev guide](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/commands/dev.md), [dev CLI](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/cli.py), [worktree creation](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/worktree.py), [agent launch](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/launch.py), [shipped skill](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/skill/SKILL.md).
- Basis: explicit + structural.
- Confidence: high for the opt-in separation mechanism.
- Caveats: separate worktrees do not automatically resolve logical changes, integration/rebase conflicts or task dependencies. The documented shared-worktree same-branch mode deliberately lacks this isolation; no positive S2 claim is made for that mode.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-dev-fleet adaptive control right with owned current operational view/return was established.
- Disturbance / variety regulated: multiple agent tasks may compete for current attention, require reprioritization after a failed branch, or need worker reassignment and integration planning.
- Decisive decision or feedback right: no Agent CLI model/controller makes these whole-portfolio decisions; user or external Claude/Codex parent selects tasks and judges progress, while `dev` implements requested spawn/list/status/remove.
- Decision owner: external invoking user/assistant or ordinary deterministic process manager, not an in-boundary first-party S3 agent/constructor/closed parent controller.
- Supporting / enforcement mechanisms: `dev list`, `dev status`, `dev rm`, launch hooks, optional tmux/zellij sessions, branch tracking, chat model loop and task-file records.
- Closure path: each coding worker may produce a result visible in its checkout or report; a user/external caller must independently interpret all worker results and decide cross-workspace priorities/repair. The bundled dev CLI does not autonomously assemble the reports into whole-fleet current regulation.
- Whole-system current view: CLI enumerates worktrees and git status for **human/external consumption**, not a shipped first-party adaptive controller.
- Current-control decision scope: fixed lifecycle/cleanup and CLI-selected per-worktree operations; no evidenced internal authority over shared mission commitments or corrective portfolio dispatch.
- Why this is / is not agent-owned: the shipped skill can tell *another assistant* how to spawn agents, but that assistant is outside the declared Agent CLI management boundary. Listing many sessions or putting instructions in task files is not itself whole-system S3 ownership.
- Evidence: [dev status/list](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/commands/dev.md), [dev CLI](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/cli.py), [bundled skill](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/skill/SKILL.md), [launch implementation](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/launch.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a separate Claude Code or other parent assistant may be deliberately used to orchestrate the dev command. Its own current-control rights would require an assessment of that assembled parent system, not silent promotion of Agent CLI.

### Absence scope

- Surfaces inspected: dev CLI launch/list/status/remove, worktree/branch registry, packaged skill instructions and report conventions, tmux integration, chat agent and memory/RAG commands.
- Plausible first-party paths checked: automatic launch with initial prompt, AI branch naming, skill delegation guidance, worker status dashboard, process cleanup, long-term memory and RAG context management.
- Why no material first-party path remains: all observed dev modes execute caller-selected worktree/process operations or export status to a separate decision maker. The chat agent operates one conversation and does not own the current multi-worker mission portfolio.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary, sufficiently independent agent audit with returned corrective or acceptance authority was established.
- Disturbance / variety regulated: incorrect coding-agent completion reports, unsound branch diffs or missed testing failures could require challenge independent of the implementing worker.
- Decisive decision or feedback right: no bundled Agent CLI reviewer role autonomously obtains worker claims plus independent source/test access and issues an acceptance/fix veto into the `dev` integration path.
- Decision owner: no qualifying first-party owner. User and an external agent may optionally inspect branches or spawn separately prompted reviewer agents, but no specific independent audit/merge-gate lifecycle is shipped.
- Supporting / enforcement mechanisms: separate worktrees, optional review-specific user prompts, `dev run` output inspection, task report files, test tools and memory retrieval.
- Closure path: users/outer coordinators can request an ad hoc review and decide what to do; `dev` itself neither mandates independent fresh review nor refuses integration on an audit verdict and returns failed claims for rework.
- Claim being audited: hypothetical coding worker claim that a task branch implements the prompt correctly.
- Ordinary reporting path: coding worker's output, prompt/task file and optional `.claude/REPORT.md` produced at the parent's request.
- Complementary access path: not established as a first-party standard role; launching a second generic agent with a review prompt creates an *optional external application*, not a supplied complementary audit decision lifecycle.
- Independence boundary: no built-in reviewer identity, separable evidence mandate, adjudication protocol, or merge-bound independent judgment is enforced at the declared boundary.
- Who acts on findings: human/external orchestrator would choose corrections; no first-party report→audit verdict→S1 correction loop is demonstrated.
- Why this is / is not agent-owned: parallel execution and review-shaped prompts cannot by themselves establish an independent epistemic audit owner or acceptance gate.
- Evidence: [dev skill review examples](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/skill/SKILL.md), [dev guide](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/commands/dev.md), [dev status](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/cli.py), [agent launch](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/launch.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: this does not assert external coding agents or a manually configured reviewer cannot test code; it limits the claimed first-party boundary.

### Absence scope

- Surfaces inspected: bundled `agent-cli-dev` skill, explicit review-task examples, CLI worktree/list/agent execution paths, per-worker prompt/report files, chat memory tools and Git worktree lifecycle.
- Plausible first-party paths checked: prompting multiple review agents, running tests in separate worktrees, development hooks, status/report inspection, skill-instructed summary file and human merge.
- Why no material first-party path remains: these are general-purpose launch/inspection options without a first-party independent review/claim-challenge right, required evidence path and returned corrective control gate.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct external/prospective environmental-intelligence and capability-adaptation closure was evidenced.
- Disturbance / variety regulated: changing model/provider ecosystem, future development-tool needs, user preferences and long-horizon task requirements could demand new capabilities.
- Decisive decision or feedback right: none established for an agent/constructor/closed parent selecting new future-facing organizational capabilities based on external sensing and returning them to the present Agent CLI runtime.
- Decision owner: none established for a qualifying S4 function.
- Supporting / enforcement mechanisms: memory fact extraction and reconciliation, RAG retrieval, conversational web search, AI branch names, model/provider configuration, optional extras/install-services and local background service management.
- Closure path: memory summaries and facts can influence subsequent *conversation content*; optional package/plugin/provider changes are requested by an operator. No first-party external/future scanning → capability option generation → authorized adaptation into current organizational control loop was identified.
- Why this is / is not agent-owned: reconciling contradictory user memories, answering a web query or auto-selecting a branch name is task/context support, not S4 organizational prospecting and adaptive capability return.
- Evidence: [memory architecture](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/architecture/memory.md), [memory client](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/memory/client.py), [chat tools](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/_tools.py), [dev branch naming](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/_branch_name.py), [config docs](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/configuration.md).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: an external user-built memory/agent automation can implement future adaptation, but that would expand the system boundary.

### Absence scope

- Surfaces inspected: chat and assistant tools, long-term memory extraction/reconciliation and proxy, RAG, provider configuration, extras/service setup, developer worktree naming/launch and first-party docs.
- Plausible first-party paths checked: contradiction reconciliation, persistent memory/context, web search, branch naming with AI, updating/installing local models and selecting external coding agents.
- Why no material first-party path remains: observed mechanisms support present task/context retention or human-chosen configuration changes; none owns and closes a distinct future/environmental adaptive-capability function.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/constitutional-policy decision lifecycle was evidenced at the Agent CLI installation recursion.
- Disturbance / variety regulated: human privacy intent, provider/network boundaries, safe tool use and deployment rights can shape operation, but they do not themselves constitute an ultimate policy organ.
- Decisive decision or feedback right: none for adjudicating the system's own ultimate purpose/identity and returning a ratified change into operations.
- Decision owner: human installs/configures the tool, chooses local or remote model, and approves task/process choices; no distinct first-party S5 parent-governance mode with function-specific closure is established.
- Supporting / enforcement mechanisms: privacy-focused README, provider settings, OS permissions, user agent prompts, dev hooks, tool execution scope, macOS menu controls, memory consent hints and service installation.
- Closure path: these static/user-set constraints shape tools and provider access, but no identity dispute → authoritative policy judgment → returned organizational mandate cycle appears in shipped runtime.
- Why this is / is not agent-owned: privacy defaults and operator control express design and configuration, not a self-contained S5 decision right. An external user/organization may own S5 at a different recursion.
- Evidence: [README privacy boundary](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/README.md), [configuration](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/docs/configuration.md), [tool module](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/_tools.py), [dev hooks](https://github.com/basnijholt/agent-cli/blob/554344e6ed5266bcc2a7b1461d4c84744ff5e0af/agent_cli/dev/hooks.py).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: a parent organization using Agent CLI may have independent governance, not imported into this standalone assessment.

### Absence scope

- Surfaces inspected: tool/provider permission configuration, local-first privacy material, dev task-file/agent launch, CLI/system integrations, memory policy hints and service setup.
- Plausible first-party paths checked: local/offline privacy claims, explicit provider choice, risky command execution, user-approved memory changes, CLI tool flags and external agent instructions.
- Why no material first-party path remains: each checked path enforces already-specified preferences or immediate tasks; none constitutes a specific ultimate-purpose/policy adjudication and return loop.

## Recursion

The bundle contains multiple unrelated local utility and model-service commands. Its `chat` S1 and optional dev-mode coding S1 workers are credited without assuming a single shared runtime between them. Optional Claude Code plugin users remain a higher/adjacent recursion, while Agent CLI's per-worktree launcher is a common mechanical service, not an autonomous parent agent.

## Variety and escalation

Local voice/text interfaces attenuate human-input friction; PydanticAI's tool loop reacts to task-local unknowns; memory/RAG preserves useful context. Dev mode attenuates git-index/checkout collision by placing agents on separate branches. Worker conflicts and quality concerns are handed to the human or invoking external agent; a generic dev status view does not autonomously reallocate work or independently verify claims. There is no established S4/S5 escalation mandate at this system boundary.

## Evidence gaps

The assessment is limited to pinned source, docs and deterministic structural paths. No live ASR/LLM provider or external coding agent was run; no empirical parallel branch-conflict, reviewer defect-detection or quality benchmark was conducted. The `dev` worktree path is a structural S2=C witness, while S3/S3* remain negative because their potential decision makers are outside Agent CLI or generic. A future first-party coordinator or independent review gate would require a new-ref reassessment.
