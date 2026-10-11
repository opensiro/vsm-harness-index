---
harness_id: visvoai
project_name: VisvoAI
repository: https://github.com/VisvoAI/visvoai
review_ref: 25602903497dfeca8a4d7e654467ab046e32071c
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# VisvoAI

## Review boundary

- System in focus: publicly distributed Python terminal coding agent `visvoai-cli`, together with first-party `visvoai-core` agent graph and `visvoai-ai` provider layer instantiated by the CLI. This assessment examines the deployable agent application, not every possible downstream application constructed with the libraries.
- Purpose and identity: take a developer's coding objective and autonomously inspect a repository, select file/shell/search actions, incorporate their results, edit/verify code where permission is available, and return a reply. User-declared project permissions constrain the agent's executable actions.
- Relevant environment: a user-controlled checkout and shell, model-provider API and credentials, local per-project configuration, optional trusted agent/skill/MCP definitions, and persistent user-local session/checkpoint storage.
- Standard-distribution boundary: installed `visvoai` CLI/TUI and first-party runtime modules at the frozen commit, including agent/tool graph, subagent dispatch, permission gates, sandboxed shell, session state, and human-owned trust decisions; one-shot headless operation is also considered.
- Credited operating / distribution surfaces: [root README](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/README.md); [CLI README](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/README.md); [CLI entry/headless](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/main.py); [CLI graph construction](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent.py); [CLIRuntime](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/runtime.py); [turn execution](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); [gated tools](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/gated_tools.py); [subagent dispatch](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py); [run registry](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_runs.py); [background tools](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/tools/background.py); [permission policy](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/permissions.py); [trusted specifications](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/specstore.py); [session persistence](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/store.py); [worktree checkpoints](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/checkpoints.py); [core agent graph](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-core/src/visvoai/core/graph.py); [AgentRuntime](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-core/src/visvoai/core/runtime.py).
- Adjacent first-party surfaces excluded from ownership: library examples and tests, standalone keyless illustrative workflows, repository maintainer CI/contributor governance, roadmap proposals, and the commercially hosted platform mentioned in the README. The hosted platform's supervision, persistence, auth or HITL behavior is not imported into this CLI merely because it subclasses the same public runtime.
- First-party operating / deployment modes considered: standard interactive TUI with permission prompts; preauthorized `auto-edit`/`accept-all` or per-tool allow-all; one-shot `visvoai "task"` with conservative denial unless `--yes` or policy allowance; optional trusted project/user agents, skills, MCP tools; persisted/resumable sessions and parallel `run_agent` dispatch.
- Recursion level: one executable coding-agent session and any directly dispatched transient specialist subagents. Each subagent is an S1 task executor at lower recursion; neither external model provider nor the human's other repositories is an in-boundary autonomous managerial organization.
- Reviewed revision: `25602903497dfeca8a4d7e654467ab046e32071c`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

**Source availability provenance:** the original frozen identity `VisvoAI/visvoai` (candidate intake opensiro/vsm-harness-index#862; stable GitHub repository ID `1276393018`) returned 404 at review time. The *same immutable Git commit* `25602903497dfeca8a4d7e654467ab046e32071c` was directly resolved through four public fork repositories, including `ChildrenofIsrael/visvoai`, and its complete tree was accessible at that SHA. All primary-code links below deliberately target that exact source-identical Git commit in a public fork. This is read-through evidence preservation, **not** a repin, a change of canonical system identity, an import of newer fork behavior, or a claim that the original repository still exists.

## Repository architecture

The [monorepo overview](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/README.md) describes a three-layer public stack: `visvoai-ai` resolves model deployments, `visvoai-core` supplies an extensible LangGraph-backed agent→tools→agent loop, and the installable `visvoai-cli` is its first-party coding product. In [core graph.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-core/src/visvoai/core/graph.py), an AI tool call activates `ToolNode` and returns actual tool messages to the next model round; the graph stops when the model produces no tool calls, with a bounded tool-using step cap and forced tool-free finalization. [CLI build_agent_graph](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent.py) supplies the model, coding tools, optional MCP/plugin tools, and delegation to [CLIRuntime](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/runtime.py) for per-turn project/context assembly. [AgentTurnMixin](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py) persists the user's input before streaming the graph and appends/repairs resulting conversation state.

Edits, writes and potentially mutating shell commands pass through [gated_tools.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/gated_tools.py) and [the interactive approval callback](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); read-classified shell commands run in an OS no-write sandbox, with fallback to approval after detected sandbox denial. [PermissionPolicy](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/permissions.py) and UI approval modes are operator/configuration authorizations and deterministic enforcement; they do not themselves decide what code modification best addresses the task. [Headless invocation](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/main.py) denies unapproved mutations by default unless the human opts into `--yes` or configured preauthorization.

[run_agent](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py) exposes built-in `explore` and `general` specialists plus trusted user/project-defined agents. Each dispatch builds its own tool-limited graph, receives one explicit delegated task and an isolated message history, and returns its final message to the caller. Multiple dispatches may execute concurrently. A read-only specialist has no write capability; full specialists still use the same mutating-tool approval gate. [AgentRunRegistry](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_runs.py) records live status/steps and supports user-initiated cancellation. [Store](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/store.py) persists conversations; [shadow Git snapshots](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/checkpoints.py) permits restore, rewind and fork. [SpecStore](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/specstore.py) hashes repository-controlled skill/agent definitions for one-time explicit human trust. [Background process tools](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/tools/background.py) start, inspect and stop agent-created processes.

## Operational model

The active coding model controls one present-task tool/observation loop. It may delegate bounded subtasks to peer executors, but the outer model chooses what to delegate and consumes their final outputs. The tool framework and UI preserve permissions, provenance, context and stop/recovery mechanics. A user chooses the initial goal, model, safety mode, project trust, and exceptional approvals. No native whole-workforce current-control, complementary independent audit feeding that control, future environment/capability adaptation, or ultimate-identity governance loop is established at this declared recursion by the inspected shipped mechanisms.

## S1 — Operations

- State: A
- Function: execute uncertain developer coding tasks by choosing repository-inspection, shell, file-edit and verification operations in response to live observations.
- Disturbance / variety regulated: unknown repository structure, unexpected tool output, failed commands, incomplete edits, changing task-local context, and need for further action/verification.
- Decisive decision or feedback right: active coding model chooses subsequent tool calls and whether to continue, delegate or finalize after reading actual tool results.
- Decision owner: model-guided first-party CLI/core agent loop. A model provider supplies inference; the integrated graph/tools deliver first-party action/observation closure. Human consent constrains dangerous operations but does not select ordinary model tool choices.
- Supporting / enforcement mechanisms: `CLIRuntime`, `ToolNode`, tool registry, OS sandbox, explicit approval callbacks, session log, process registry, context assembly, bounded loop and optional isolated subagents.
- Closure path: user coding task → model-generated file/shell/delegation tool call → executed first-party tool/child graph → result appended into model history → model-selected next step or final answer.
- Boundary reachability: `visvoai` entry actually invokes `build_agent_graph` with CLI tools and the project context; the core graph contains the live tools→agent return edge. This is the installed standard product, not a detached developer example.
- Why this is / is not agent-owned: removing the model's context-dependent choices leaves deterministic invocation/gating and callable tools but no situated coding sequence or final task judgment. Under normal permissioned execution the agent owns that operational discretion.
- Evidence: [agent.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent.py); [agent_turn.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); [graph.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-core/src/visvoai/core/graph.py); [agents.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py); [gated_tools.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/gated_tools.py).
- Basis: explicit and structural.
- Confidence: high on reachable model/tool feedback loop; no fresh end-to-end provider task was executed in this source review.
- Caveats: an explicit user rejection can block a chosen mutation; this qualifies permission, not first-party model discretion for authorized task operations.

## S2 — Coordination

- State: —
- Function: no first-party relation is established that detects or attenuates a **specific interference/oscillation between distinct autonomous S1 workers** and returns the correction into their subsequent behavior.
- Disturbance / variety regulated: parallel subagents may share a worktree, but dispatch isolation, restricted tools, and separate traces primarily bound task execution rather than detect/regulate inter-agent conflict.
- Decisive decision or feedback right: parent coder chooses independent delegate tasks; code constructs separate graphs and fixed tool tiers. Approval serialization prevents overlapping UI prompts, not coordination decisions among colliding S1 units.
- Decision owner: parent agent for delegation, human for approvals, and runtime for fixed execution/guard ordering; no dedicated S2 decision/feedback path evidenced.
- Supporting / enforcement mechanisms: subagent task isolation, dispatch tags, run log/status, non-recursive tool sets, read-only tier, common permission gate.
- Closure path: each subagent produces a final answer consumed by parent coder; no demonstrated cross-worker contention signal → coordinating attenuation judgment → changed obligations returned to both affected workers.
- Why this is / is not agent-owned: generic parallel delegation and permission serialization do not independently close the S2 function.
- Evidence: [agents.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py); [agent_runs.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_runs.py); [agent_turn.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); [gated_tools.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/gated_tools.py).
- Basis: structural.
- Confidence: medium-high within inspected shipped CLI boundary.
- Caveats: a composed external harness could add a conflict-management policy, but that policy is not credited here.

### Absence scope

- Surfaces inspected: CLI/core graph, parallel `run_agent` implementation, fixed per-specialist tools, tagged execution tracing, cancellation and human approval serialization.
- Plausible first-party paths checked: shared-worktree edit collisions, concurrent subagent coordination, per-agent feedback about interference, resource/contention control and revised worker commitments after a conflict.
- Why no material first-party path remains: native code provides dispatch/isolation/tracing and human-level action gates but no evidence of a separate inter-S1 interference detector with an attenuation/returned-S1 regulatory loop.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current managerial authority over a population of operating S1 units is supplied in this coding-session distribution.
- Disturbance / variety regulated: current coding progress, subprocess lifecycle and subagent completion are locally observable, not a sustained portfolio of competing operational commitments requiring whole-system intervention.
- Decisive decision or feedback right: the active model can delegate specific tasks; a user may stop one subagent or process. The run registry does not choose whole-current priorities, reallocate commitments or exercise independent management judgment.
- Decision owner: top-level coding S1 for its own task, operator for explicit stop/permission actions, runtime for deterministic tool enforcement.
- Supporting / enforcement mechanisms: `AgentRunRegistry`, `ProcessRegistry`, status panels, persistent sessions, model-turn limit, checkpoint/rewind, user run cancellation.
- Closure path: status/results return to the coding conversation or user display; no whole-current view → priority/resource/accountability intervention → new obligations returned to multiple first-party S1 operations.
- Why this is / is not agent-owned: managing one's own task and displaying subprocess state does not establish organizational current management.
- Evidence: [agent_runs.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_runs.py); [agents.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py); [background.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/tools/background.py); [app.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/app.py); [commands.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/commands.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a human running numerous separate CLI sessions is not an incorporated first-party S3 authority for this instance.

### Absence scope

- Surfaces inspected: active agent graph, subagent run registry, background process tools, session state and user controls.
- Plausible first-party paths checked: whole-worker roster, adaptive global assignment/priority decisions, feedback on shared resource commitments, parent-governed S3 current control with authoritative returned decisions.
- Why no material first-party path remains: the shipping implementation tracks/cancels executions and exposes human control but contains no integrated current organizational manager exercising that function.

## S3* — Complementary audit

- State: —
- Function: no operationally integrated complementary and sufficiently independent audit path takes direct reality evidence, adjudicates claims, and feeds findings into an S3 corrective owner.
- Disturbance / variety regulated: defective source changes and risky commands can be inspected by normal testing, model self-verification, user inspection or a requested `reviewer` specialist; those do not by themselves constitute an S3* current-control audit.
- Decisive decision or feedback right: ordinary coding agent optionally delegates a review, receives a textual final answer, and decides what to do. No distinct first-party auditor independently samples operating reality and returns a privileged finding to current management.
- Decision owner: main coding S1 for delegation/action, chosen specialist for task response, human for permission/approval; no proven S3* authority.
- Supporting / enforcement mechanisms: read-only specialist, CLI tests, per-turn checkpoints, run traces, tool outputs, user-supplied reviewer prompt.
- Closure path: coder may prompt a child reviewer → child analyzes delegated material → final text enters same coder's task transcript; not independent evidence collection → audit judgment → whole-current managerial correction.
- Why this is / is not agent-owned: isolation of the child context and a `reviewer` label do not establish the required independent audit relation and returned management closure.
- Evidence: [example reviewer](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/examples/agents/reviewer.md); [agents.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py); [agent_runs.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_runs.py); [agent_turn.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); [subagent tests](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/tests/test_agents.py).
- Basis: explicit and structural.
- Confidence: medium-high for standard shipped paths.
- Caveats: an application built separately from the extensible core might implement S3*; a hypothetical consumer is outside this reviewed CLI instance.

### Absence scope

- Surfaces inspected: shipped built-in and user-defined agent roster, review example, tool-result path, run logs, tests and core extension hooks.
- Plausible first-party paths checked: independently commissioned audit actor, complementary direct-access sampling, separation from ordinary agent self-report, autonomous/human audit judgment, returned current management correction.
- Why no material first-party path remains: the review-capable child is ordinary optional S1 delegation with result returned to its requester; the first-party CLI does not wire an independent audit-to-S3 regulatory loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop selects new future operating capability and carries it back into current-system management.
- Disturbance / variety regulated: new task context and model-provider options exist, but the model picker, web tools, skill definitions and extensible hooks are immediate task/control infrastructure.
- Decisive decision or feedback right: a user configures/selects providers and skills, and an active coding model can research facts for the current task. No evidenced autonomous or parent-governed S4 decision is returned as a modification of the continuing organization's capability.
- Decision owner: user/developer for installed configuration and model selection; current S1 for request-local search or planning.
- Supporting / enforcement mechanisms: provider/deployment registry, project instructions, read-skill tool, MCP discovery, session context, public roadmap.
- Closure path: chosen tools/models influence current coding work, but there is no required outside-scan → prospective option appraisal → capability/operating-change authority → implementation/feedback path.
- Why this is / is not agent-owned: selecting a different provider or remembering context for a task is not a future/environment adaptation function by itself.
- Evidence: [provider layer](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-ai/README.md); [agent setup](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent.py); [skills.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/skills.py); [context assembler](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/context/assembler.py); [roadmap](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/ROADMAP.md).
- Basis: structural.
- Confidence: medium-high for CLI operating boundary.
- Caveats: model/skill extensibility could support a future external adaptation application, but no shipped loop is evidenced here.

### Absence scope

- Surfaces inspected: provider registry, model-selection route, web tools, agent/skill loader, local context/memory, README and roadmap.
- Plausible first-party paths checked: prospective environmental intelligence, agent-proposed capability alternatives, authorized adoption and return to ongoing operating capability in autonomous and parent-governed modes.
- Why no material first-party path remains: the available mechanisms feed present-task execution or human-selected setup; no integrated prospective adaptation decision/return closure was found.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime owner closes identity or ultimate-policy questions for this continuing organization at the stated recursion.
- Disturbance / variety regulated: dangerous tools, untrusted repository definitions, model keys, allowed paths, and approval posture are operator/security controls, not ultimate organizational identity disputes.
- Decisive decision or feedback right: a person approves tool operations and trust hashes; runtime enforces defined constraints. No S5 policy/identity dispute is adjudicated by a legitimate autonomous or parent authority with a formal return into organization identity.
- Decision owner: operator for ordinary safety/permission decisions and configuration; no S5 authority evidenced.
- Supporting / enforcement mechanisms: permission policy, project/global trust fingerprints, read sandbox, capability tiers, API-key resolution, explicit confirmation prompts.
- Closure path: user approves/denies a tool or trusts a definition → gate authorizes/blocks an action; this is task-level enforcement, not issue → ultimate identity/policy authority → binding returned organizational decision.
- Why this is / is not agent-owned: the model cannot authoritatively define the organization's ultimate identity merely by suggesting a tool operation or editing local configuration.
- Evidence: [permissions.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/permissions.py); [specstore.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/specstore.py); [gated_tools.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/gated_tools.py); [agent_turn.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agent_turn.py); [agents.py](https://github.com/ChildrenofIsrael/visvoai/blob/25602903497dfeca8a4d7e654467ab046e32071c/visvoai-cli/src/visvoai/cli/agents.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: independently maintained OSS-project governance and the hosted product's institutional authority are excluded from this executable CLI boundary.

### Absence scope

- Surfaces inspected: shipped permissions/trust modes, agent definitions, model/provider credentials, delegated tool limits, runtime/control entry and contributor/public governance surfaces as adjacent material.
- Plausible first-party paths checked: ultimate policy/identity conflict ownership, agent-owned S5 decision, reachable legitimate parent S5 decision with binding return to operation, and project-level governance wired into the shipped agent.
- Why no material first-party path remains: available approvals/constraints govern individual actions or local tools, and project governance is external to the session; there is no integrated ultimate-identity adjudication/return path.

## Recursion

The outer coding turn is a distinct operational S1 at the declared application recursion. `run_agent` creates task-specific lower-recursion workers with constrained tools and isolated conversations; existence of those workers does not by itself establish a viable second organizational recursion with S2/S3/S3*/S4/S5 closure.

## Variety and escalation

Operational variety from unknown code and tool errors is absorbed in the model→tools feedback loop. Permission denials, untrusted project definitions and dangerous shell actions pass to human consent or deterministic security enforcement. Subagent errors/stops return textual outcomes to the main conversation; the CLI run registry supports user cancellation. These are ordinary agent/task control paths, not an evidenced exceptional algedonic channel to a separate whole-system response owner. The shipped unit's practical autonomy is bounded by provider availability, configured permissions and user control.

## Evidence gaps

- This is a pinned source/static-architecture review. No live paid model call or full end-to-end trace was reproduced. Runtime reachability is corroborated by first-party code and tests, not deployment performance.
- Original upstream identity `VisvoAI/visvoai` is currently inaccessible, although the **identical immutable Git commit** is readable from multiple public forks. Repository permanence, redirects and any subsequent upstream change are not presumed.
- Higher-function negatives are bounded specifically to the shipped coding CLI + instantiated public runtime. They do not decide what an independently configured external VisvoAI consumer or commercial service might implement.
