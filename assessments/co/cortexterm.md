---
harness_id: cortexterm
project_name: CortexTerm
repository: https://github.com/Toge-1/CortexTerm
review_ref: 6105b9ea5ac3241fd29fed8ae4033faa910a5aea
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# CortexTerm

## Review boundary

- System in focus: the installed first-party CortexTerm terminal coding assistant operating on a local developer workspace, including its interactive and non-TTY agent turns.
- Purpose and identity: execute repository-aware programming tasks using model-directed tool actions, local context, persistent conversations, memories, permission checks and optional MCP tools.
- Relevant environment: the developer's files and Git state, shell/test output, human instructions and approvals, provider responses, external web/MCP inputs and context-window constraints.
- Standard-distribution boundary: Python 3.11+ package, `cortexterm` console entry point, `cortexterm.main` and TTY application, runtime/model adapter, agent loop, default tool registry, session/context/memory, permission and project configuration, and shipped local slash/management commands.
- Credited operating / distribution surfaces: `cortexterm/main.py`, `tty_app.py`, `tui/agent_turn.py`, `agent_loop.py`, `anthropic_adapter.py`, `mock_model.py`, `tooling.py`, `tools/__init__.py`, `permissions.py`, `config.py`, `context_manager.py`, `memory.py`, `session.py`, `mcp.py`, `cli_commands.py`, `poly_commands.py`, and shipped tool implementations.
- Adjacent first-party surfaces excluded from ownership: unreferenced `sub_agents.py` manager and `auto_mode.py` risk checker; generic `hooks.py` hooks with no demonstrated binding to the shipped agent loop; benchmark/evaluation scripts, mock/test fixtures, design plans, project CI/contributor governance and maintainer roadmap. External model providers, installed MCP servers, humans and repository developers are outside the credited agent organization.
- First-party operating / deployment modes considered: installed interactive TUI and non-TTY fallback; configured Anthropic-compatible adapter and mock adapter; opt-in MCP tool expansion; local conversation/session resume, user permissions, context compaction, memories and direct coding/review/governance tools. The separate sub-agent lifecycle class does not constitute an exposed running deployment mode without entry-point wiring.
- Recursion level: one locally operated coding assistant/session, not its upstream GitHub development organization, external model provider or downstream user's entire software team.
- Reviewed revision: `6105b9ea5ac3241fd29fed8ae4033faa910a5aea` (batch #996 frozen row 9).
- License screen: root `LICENSE` supplies the MIT grant. `pyproject.toml` identifies the Python 3.11+ package, console entry and no runtime third-party package dependencies.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

CortexTerm's standard entry point constructs a registry of local file, command, Git, code-analysis, test, memory, web, `code_review` and `governance_audit` tools, plus configured MCP tools. It selects the real model adapter or a deterministic mock, builds one session prompt and invokes `run_agent_turn`. That loop repeatedly obtains a model-selected assistant/tool step, executes each selected tool, appends paired tool results, compacts context when necessary and asks the model to continue. The operator supplies the objective and grants or denies certain actions; the tools and permission policy enforce calls rather than make the model's substantive coding choices.

Session/history, three-scope memory and Pi-style contextual summarization preserve information and reduce context-window pressure. This is not evidence of prospective organizational adaptation: the summarizer condenses existing conversation, while persistent notes are recalled into the next coding prompt. `code_review` performs fixed AST/style heuristics; `governance_audit` executes predefined dependency/sink rules. They are available to the same acting model as ordinary tools, not separate agents with an independent access-and-corrective mandate. The `sub_agents.py` module implements definitions and a lifecycle container but has no first-party imports in the supported CLI/TTY/tool registry or agent loop; likewise `auto_mode.py` and `hooks.py` are not integrated into those paths. Do not import a multi-agent organization from module names or inspiration references.

Frozen primary evidence: [main.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/main.py), [agent_loop.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/agent_loop.py), [tools/__init__.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/__init__.py), [sub_agents.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/sub_agents.py), [context_manager.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/context_manager.py), [permissions.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/permissions.py).

## Operational model

There is one model-driven coding S1 at the declared recursion. It has genuine choice over tool calls, code changes, follow-up investigation and whether to stop in response to work state and returned diagnostics. The runner, tool registry, permission prompts, validators, static reviewers and compaction mechanisms support or constrain that operational decision. Separate first-party S1 operational units, organization-wide current control, complementary audit and future-facing capability adaptation are not established in the installed path. Optional user supervision is at task/action level, not automatically a parent S3/S4/S5 loop.

## S1 — Operations

- State: A
- Function: decide and execute an interactive software-development task using filesystem, shell, Git, tests, code navigation and available integrations.
- Disturbance / variety regulated: changing repository contents, programming ambiguity, tool errors, failed commands/tests, permission outcomes and new model/tool-result context.
- Decisive decision or feedback right: the model chooses each tool and arguments, interprets results, selects the next coding action and produces the final reply within step limits.
- Decision owner: configured model adapter via the one primary `run_agent_turn`; user defines the goal and controls action permissions.
- Supporting / enforcement mechanisms: `ToolRegistry.execute`, tool validators/runners, filesystem and shell operations, `PermissionManager`, `ContextManager`, retries and UI sessions.
- Closure path: user task plus context → model tool call → registry execution and explicit result/error → appended feedback → next model step or final response.
- Boundary reachability: the shipped `cortexterm` console entry creates the model and tool registry and passes them to the live CLI or TTY agent-turn runner; mock tests exercise this exact integration without provider inference.
- Why this is / is not agent-owned: removing the model leaves deterministic execution of already specified calls and UI, but not the ongoing choice of coding actions or diagnosis of returned task results.
- Evidence: [agent loop](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/agent_loop.py), [main entry](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/main.py), [tool registry](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tooling.py), [mock integration tests](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/tests/test_integration.py).
- Basis: explicit first-party runtime source and deterministic mock/native execution.
- Confidence: high for S1 loop composition, not real-model task-success rates.
- Caveats: no live model, external MCP or provider efficacy tests were run.

## S2 — Coordination

- State: —
- Function: no specific attenuated interference between two distinct running S1 work units is demonstrated in CortexTerm's supported local session.
- Disturbance / variety regulated: potential conflicts between simultaneously editing workers would be relevant, but the shipped path exposes one agent loop and tool calls, not a pair of independently committed operational units.
- Decisive decision or feedback right: none established for a shared inter-S1 disturbance and a corrective coordination decision.
- Decision owner: the primary model sequences its own calls; the registry executes selected calls; standalone `SubAgentManager` only records agent lifecycle objects.
- Supporting / enforcement mechanisms: single-session message/tool ordering, `todo_write`, background shell-task status, and the unconnected definitions/records in `sub_agents.py`.
- Closure path: selected tool results return to the same coding loop; no interference detection → mutual adjustment → later behaviour of distinct operational units is wired.
- Why this is / is not agent-owned: work planning and sequential tool execution are S1 mechanisms; merely spawning a metadata object without a worker inference/execution path does not create S2 regulation.
- Evidence: [sub-agent manager](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/sub_agents.py), [agent loop](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/agent_loop.py), [todo tool](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/todo_write.py), [default registry](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/__init__.py).
- Basis: entry-point/import graph and tool/agent implementation inspection.
- Confidence: high for the reviewed standard-distribution boundary.
- Caveats: external MCP servers could embody separate systems; their first-party coordination ownership is not donated to CortexTerm.

### Absence scope

- Surfaces inspected: main/TTY entry, agent runner and tool execution, sub-agent lifecycle module and its references, background tasks, task tracker/`todo_write`, MCP registration and local tests.
- Plausible first-party paths checked: `SubAgentManager` as a worker coordinator, model tool batching as parallel S1 activity, background subprocess state as another S1 unit, shared todo/task views as interference mediation.
- Why no material first-party path remains: no shipped call site connects the sub-agent manager to model-backed child execution, and none of the running tool/task surfaces identifies a conflict between distinct first-party S1 units and returns an attenuation decision into both units' subsequent work.

## S3 — Inside-and-now control

- State: —
- Function: no separate ongoing current-control function for multiple live work commitments/resources is operationally closed.
- Disturbance / variety regulated: current task prioritization, limited context and parallel work could require systemic balancing if multiple S1 cells were engaged.
- Decisive decision or feedback right: no distinct whole-current discretionary allocator or parent supervisor has demonstrated authority over collective commitments.
- Decision owner: one model owns coding decisions; user approves local actions; step/context constraints and status widgets are deterministic.
- Supporting / enforcement mechanisms: step count, token/context thresholds, `task_tracker.py` task state, in-memory todo list, TUI status/background-process views and dormant sub-agent status registry.
- Closure path: local status and limits are available, but there is no continuing global view → shared-priority/resource intervention → changed commitments of separate live S1 units.
- Why this is / is not agent-owned: task lists, progress rendering, a scheduler-like class and human approval do not establish a separate whole-current regulator; removal of any nominal manager leaves the one-agent loop intact.
- Evidence: [main.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/main.py), [task_tracker.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/task_tracker.py), [sub_agents.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/sub_agents.py), [TTY runner](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tui/agent_turn.py).
- Basis: source-level entry-point and mode trace.
- Confidence: medium-high.
- Caveats: a future deployment composing external MCP workers would have to be evaluated at a newly declared system boundary.

### Absence scope

- Surfaces inspected: runtime session/TTY control, context manager, task tracker and todo tool, background job registry, sub-agent manager, permission/approval path and local CLI commands.
- Plausible first-party paths checked: model-created task plans as whole-system coordination, session capacity limits as S3 discretion, human authorization as parent S3, sub-agent status registry as current resource/priority control.
- Why no material first-party path remains: current status and fixed execution constraints do not give an identifiable first-party decision owner a systemic authority to rebalance simultaneous S1 commitments with returned control; approvals only gate particular tool actions.

## S3* — Complementary audit

- State: —
- Function: no complementary, sufficiently independent audit-and-correction channel is established for claims made by the operating coding agent.
- Disturbance / variety regulated: code defects and governance-policy violations might escape ordinary coding verification, but the review tools are routine on-demand analyses of that same agent's selected workspace.
- Decisive decision or feedback right: AST/static heuristics calculate their reports; the same S1 model chooses whether to invoke and interpret them. No independent auditor judges a separate operational evidence stream or returns an authoritative corrective finding.
- Decision owner: fixed `code_review` and `governance_audit` rules for their outputs, primary model/user for what to do next; no separate S3* holder.
- Supporting / enforcement mechanisms: `code_review` checks unused imports, literal numbers, missing docstrings and function length; `governance_audit` checks prescribed dependency/sink rules; tests, Git diff, file-review approval and permission prompts provide regular feedback.
- Closure path: primary S1 may call a checker and read its tool result; no independent source-access → audit judgment → addressed finding → subsequent correction loop is shipped.
- Why this is / is not agent-owned: changing the main coding model does not create a distinct auditor; replacing static checkers with their deterministic rules yields the same verdicts, and the model remains reviewer of its own output.
- Evidence: [code_review.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/code_review.py), [governance_audit.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/governance_audit.py), [registry](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/tools/__init__.py), [file_review.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/file_review.py).
- Basis: primary tool implementations and absence of separate reviewer in execution paths.
- Confidence: medium-high for the shipped standalone agent.
- Caveats: user-selected independent external reviewer or MCP service could augment the system but is not first-party S3* ownership at this boundary.

### Absence scope

- Surfaces inspected: AST code-review tool, governance dependency/sink auditor, test runner, Git/diff utilities, edit approval, model/tool loop, review-related hooks and TTY interaction.
- Plausible first-party paths checked: static code review as audit, static governance policy checks as independent judgment, human file-edit approval as parent audit, hooks or MCP as separately executed reviewer.
- Why no material first-party path remains: first-party review tools are deterministic task-local diagnostics chosen within the same model loop; generic hooks and third-party integrations do not instantiate an independently composed audit judgment and corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented strategic adaptation cycle is closed for CortexTerm's own future capabilities.
- Disturbance / variety regulated: changing libraries, providers, project conventions and future user needs could motivate adaptation, but the observed paths answer present programming requests.
- Decisive decision or feedback right: no evidenced agent or legitimate parent decides among future environment/capability alternatives and returns an adopted operating change.
- Decision owner: model uses current web/doc results and recalled memory for S1; user selects providers, MCP servers and skills through configuration.
- Supporting / enforcement mechanisms: persistent memory, context summarization, web/API searches, MCP tools, skill discovery, session restoration and manually edited settings.
- Closure path: retrieved information affects current code execution or later recall, but there is no outside-and-future sensing → alternative generation → adaptation judgment → changed current operating capability loop.
- Why this is / is not agent-owned: summarization and remembering are data retention, not prospective adaptation ownership; plugin and model configuration are operator-set options without an evidenced S4 decision-return path.
- Evidence: [memory.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/memory.py), [context_manager.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/context_manager.py), [mcp.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/mcp.py), [config.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/config.py).
- Basis: source-level retention/integration wiring and bounded absence assessment.
- Confidence: medium-high.
- Caveats: other organizations may use CortexTerm to write future-roadmap plans; those external workflows are not the evaluated first-party system.

### Absence scope

- Surfaces inspected: memory scopes/recall, context compaction and history, model configuration, web and MCP registry, skills, installed CLI, optional hook and background modules, maintainer development docs.
- Plausible first-party paths checked: retained memories as learning, Pi-style summarization as future reflection, MCP/skill expansion as capability adaptation, web search as external scanning, user model changes as parent S4.
- Why no material first-party path remains: these are present-task context, storage and externally/manual configured extensions without an identified prospective adaptation decision and returned implementation into the assistant's capability set.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy determination and subsequent system-governing return is established within the installed assistant recursion.
- Disturbance / variety regulated: identity conflicts and ultimate tradeoffs are not decided by a system-level governing body in this runtime.
- Decisive decision or feedback right: none evidenced for ultimate purpose/identity; user and developer set per-tool permissions, prompts, models and runtime configuration.
- Decision owner: human operator for action grants and setup, maintainer for external product design; no first-party agent/parent S5 closure.
- Supporting / enforcement mechanisms: permission checks (`allow`, `deny`, `ask`), risk-classification module outside the active loop, tool validators, prompts, settings and file review.
- Closure path: operator/tool policies constrain particular actions, but no identity-level issue reaches a legitimate S5 authority and returns a governing purpose/policy decision into the running organization.
- Why this is / is not agent-owned: fixed permission rules and user approval enforce local activity limits; they do not own the system's ultimate identity or policy tradeoffs.
- Evidence: [permissions.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/permissions.py), [auto_mode.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/auto_mode.py), [prompt.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/prompt.py), [main.py](https://github.com/Toge-1/CortexTerm/blob/6105b9ea5ac3241fd29fed8ae4033faa910a5aea/cortexterm/main.py).
- Basis: static and runtime permission/control path inspection.
- Confidence: medium-high.
- Caveats: operator supervision is real but task-granular; project maintainer governance is a separate recursion.

### Absence scope

- Surfaces inspected: CLI bootstrap/configuration, prompt generation, interactive permission approval, persistent permission rules, code/edit review, static governance audit, `auto_mode.py`, contributor and test surfaces.
- Plausible first-party paths checked: human action approval as parent S5, governance audit as ultimate-policy controller, custom prompt/skills as identity adaptation, tool security checks as authority over purpose.
- Why no material first-party path remains: all in-boundary returns constrain selected actions or configure tasks/providers; none demonstrates an identity/ultimate-policy issue → authoritative organizational judgment → returned policy controlling the later system.

## Distributed OSS parent arrangement

The upstream open-source repository and contributors maintain CortexTerm, but their GitHub/CI activities do not constitute a shipped governance mechanism for each installed local coding session. No project-level distributed S3/S4/S5 is inferred from repository location, license or plans.

## Self-hosted and non-human modes

CortexTerm runs locally and lets operators approve sensitive tools and configure model/MCP availability. The user may intervene during the task, but no first-party complete parent S3/S4/S5 loop follows from those generic controls. The mock adapter is a test substitute for S1, not a separate autonomous organization.

## Recursion

One user-facing coding session is the assessed S1 at the chosen recursion. Background processes are tools, not separately model-owned S1 units; dormant sub-agent objects do not establish another level of viable metasystem. The local user's software project and upstream maintainers are adjacent systems.

## Variety and escalation

The model/tool cycle responds to command errors, test reports, denied permissions and changed files; permission denials can force the model to choose another local action. Token pressure can cause model-supported context compaction. Neither ordinary retry, static QA nor event/status notifications alone establishes S2/S3/S3*/S4/S5 or a separate algedonic organizational channel.

## Evidence gaps

- Frozen native test run with an in-process temporary override of CortexTerm's user session/memory directory: **233 passed, 3 skipped**, with no real model inference, external MCP calls or live API testing. The default read-only container home produced four first-run environment failures; the same tests passed when state paths were redirected to a writable temporary directory. Three skipped tests included opt-in live-provider scenarios; no efficacy conclusion follows from script/mock tests.
- No test of autonomous real-model performance, quality of produced code, actual external tool effects or nonstandard externally composed multi-agent organizations is claimed.
- The supported CLI/TTY import graph contains no references to the standalone `sub_agents.py` manager, `auto_mode.py` checker or generic hook manager. This is an assessed boundary statement for frozen `6105b9e`, not proof that developers cannot wire those APIs in a later release.
