---
harness_id: deepseekfathom
project_name: DeepSeekFathom
repository: https://github.com/ffffff233/DeepSeekFathom
review_ref: 2c68eff7bb7ae2eabf4d36a0331386f06af2d356
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

# DeepSeekFathom

## Review boundary

- System in focus: shipped DeepSeekFathom Python coding agent and desktop/terminal entrypoints, with first-party `FathomAgent`, local tool registry, inline permissions, child agent dispatch, persisted conversations and optional extensions. Not the developer's separately configured research coordination project or a downstream MCP ecosystem.
- Purpose and identity: fulfill developer objectives by autonomously selecting context-sensitive code/file/shell/web/patch operations, inspecting the observed effects and iterating, subject to user and permission mode.
- Relevant environment: local repository/filesystem/shell, OpenAI-compatible provider APIs, local session and skill/plugin folders, user-configured hooks/MCP servers, approval prompts and optional desktop UI.
- Standard-distribution boundary: the installable `deepseekfathom` CLI and desktop distribution; code in `src/deepseekfathom/_core` called by the app. Configurable user-supplied extensions and hosts are treated as connectors until their actual first-party decision ownership is shown.
- Credited operating / distribution surfaces: [README](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/README.md); [FathomAgent](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [CLI composition](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/cli.py); [desktop entry](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/desktop/app.py); [tool registry](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/tools.py); [tool contracts](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/tool_contracts.py); [permission modes](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/policy.py); [session persistence](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/session.py); [change snapshot/diff service](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/reviews.py); [optional hooks](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/hooks.py); [extension loader](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/extensions.py); [skills](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/skills.py); [MCP runtime](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/mcp.py); [agent tests](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/tests/test_agent.py); [review plumbing tests](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/tests/test_review_wiring.py).
- Adjacent first-party surfaces excluded from ownership: `.air/local/evidence/` workers/reviewer and `.air/shared/plan/` local research/development artifacts, CI and package-release workflows, developer tests, and future/update mechanisms that run only by maintainer/operator choice. Those do not automatically become operational actors inside the installed coding agent.
- First-party operating / deployment modes considered: CLI/TUI coding turns, desktop wrapper, configured `plan`/`review`/`agent`/`trusted`/`yolo`/`root` permissions, ordinary one-task loop, a model-dispatched `delegate_agent` batch of isolated child tasks, session restoration, extensions/hook support.
- Recursion level: a foreground coding-agent session, with optional ephemeral subagents; not an autonomous multi-workstream organization. External tools/providers/hosted services and optional user-created agents beyond first-party wiring remain outside the claimed organization.
- Reviewed revision: `2c68eff7bb7ae2eabf4d36a0331386f06af2d356`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[FathomAgent.run](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py) manages a present-task LLM/tool loop: it incorporates the user's goal, optionally injects instruction/skill context, requests a model answer with structured tool calls, checks active [ApprovalPolicy](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/policy.py) and hook gates, dispatches first-party [ToolRegistry](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/tools.py) or `delegate_agent`, appends resulting `TOOL_RESULT` content to the same session and asks the model again. The loop includes max-round limits, local action evidence prompts, todo/continuation nudges and recovery when tools fail. [Session](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/session.py) persists the operator's conversations. CLI, desktop, MCP connectors and configurable hooks provide user-facing execution and extensibility; no hosted/private infrastructure is needed for the basic code loop.

[_run_subagent](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py) executes one or more child specs *serially in the current implementation* (list comprehension calling `_run_one_subagent`), despite the README describing batched delegation. Each child is a fresh `FathomAgent` with an ephemeral nonpersisted session, copied tool contracts/approval and bounded rounds. Results return as summaries to the parent. This is first-party task delegation, not an evidenced inter-unit conflict regulator or whole-current management decision. [ReviewStore/ChangeSnapshotService](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/reviews.py) provides durable snapshots and bounded diffs, not by itself independent evaluative judgment or a separate corrective authority. [HookRunner](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/hooks.py) exposes optional developer/user-defined lifecycle hooks, with blocking on some events; configured external hook behavior is not evidence of a native S3* auditor. [Policy](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/policy.py) provides six tool-permission postures and explicit confirmation; the selector is not a VSM organization grade.

## Operational model

One coding task is modeled and acted on by an agent under local user constraints. The only built-in lower units are transient delegated subtasks; their completion summaries feed the parent operative. The root `review` permission mode means tool action constraints, not independent organizational auditing. Snapshot/diff provenance and configurable tool/hook policies are mechanisms, not automatic S3* or S5. The repository's `.air` evidence and scheduling files are adjacent development/dogfood records and excluded.

## S1 — Operations

- State: A
- Function: execute uncertain coding tasks through model-selected file/shell/patch/search tools while reacting to actual outcomes.
- Disturbance / variety regulated: unknown code structure, tool failures, unavailable files, incomplete edits, provider output and intermediate execution results.
- Decisive decision or feedback right: model selects the next tool, whether to delegate, repair after an error, or finalize in response to returned observations.
- Decision owner: native model-directed `FathomAgent` together with the first-party tool-action/feedback loop; inference provider does not own the app's tool selection control wiring.
- Supporting / enforcement mechanisms: ToolRegistry, turn/session records, context compaction, approvals, thinking/todo mode, hooks and result normalization.
- Closure path: initial user task → model tool decision → first-party tool or ephemeral child executes → actual result appended to session → next model decision or final answer.
- Boundary reachability: standard installed CLI/desktop constructs `FathomAgent` with its local registered tools; this loop is the shipped entry-point, not a benchmark fixture.
- Why this is / is not agent-owned: without the model's context-sensitive selection, tools, user approvals, session storage and a deterministic parser cannot decide situational coding actions.
- Evidence: [agent.py](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [cli.py](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/cli.py); [tools.py](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/tools.py); [tests](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/tests/test_agent.py).
- Basis: explicit and structural.
- Confidence: high for source reachability; provider-backed execution not reproduced independently.
- Caveats: approved actions are bounded by real permission modes and the operator's configuration.

## S2 — Coordination

- State: —
- Function: no first-party regulatory relation for specific interference or oscillation between multiple independent S1 operations was established.
- Disturbance / variety regulated: delegated tasks may address different subtasks, but current implementation returns each child's final summary in a parent-managed sequence with no shared conflict-feedback response.
- Decisive decision or feedback right: root model picks delegates and task descriptions, runtime creates bounded children. No autonomous S2 conflict intervention or returned peer agreement.
- Decision owner: coding parent S1 for delegation; code for sequencing. No distinct coordination owner.
- Supporting / enforcement mechanisms: child specs, bounded permission modes, sequential child invocation and tagged event/summary handling.
- Closure path: child outcome → parent task transcript; no detected inter-S1 interference → attenuating correction → subsequent changed peer behavior loop.
- Why this is / is not agent-owned: task division, routing and ordered execution do not suffice for S2 under Methodology 0.3.7.
- Evidence: [delegate agent implementation](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [README](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/README.md); [tool contracts](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/tool_contracts.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: user-supplied extensions may add coordination, but that configured external logic is not attributed to the first-party shipped mode.

### Absence scope

- Surfaces inspected: parent model loop, `_run_subagent`, child execution, tool registry, async/serial tool invocation and run results.
- Plausible first-party paths checked: worker collisions and shared resource interference, cross-worker feedback arbitration, explicit cooperation contracts or conflict-based reassignment.
- Why no material first-party path remains: supported native subagents are isolated ephemeral task executors with serialized summaries, not a first-party relation regulating a concrete inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current authority owns portfolio priorities, current commitments, resourcing or accountabilities across operational units.
- Disturbance / variety regulated: current task subtasks, todo items and permission modes are local present operation.
- Decisive decision or feedback right: root model manages its own coding approach; external user approves gated actions, chooses mode, and stops sessions. No whole-system managerial decision is returned to a set of sustained S1 units.
- Decision owner: coding operative and human operator, not S3 manager.
- Supporting / enforcement mechanisms: task todos, child delegation, process tool/status, permission constraints, storage and hooks.
- Closure path: tool/todo/child result to same coding model, not separate whole-current status → S3 discretionary intervention → changed worker commitments.
- Why this is / is not agent-owned: agent planning its current work is a function within S1; it does not become S3 because it spawns helpers.
- Evidence: [agent loop](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [policy](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/policy.py); [CLI](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/cli.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: local `.air` development scheduler records are explicitly outside packaged runtime ownership.

### Absence scope

- Surfaces inspected: model/delegation paths, todo and current session, status, permissions, local dev-plan distinction.
- Plausible first-party paths checked: whole-current worker/resource view, autonomous managerial assignment intervention, parent-governed S3 return to work.
- Why no material first-party path remains: shipped product exposes present-task control plus helpers, not a distinct organization-level current-control decision loop.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary auditor with sufficiently independent evidence access, judgment and returned corrective path to S3 is wired into normal coding execution.
- Disturbance / variety regulated: model-generated changes can be reviewed with diff/snapshot tools, optional delegated reviewer instructions or external hooks, but this is not an independent native whole-system audit.
- Decisive decision or feedback right: operating model can inspect diff and decide whether to correct; user/developer may inspect history. No built-in separate auditor owns the audit verdict and current-control return.
- Decision owner: coding operative for optional review, developer for external CI/hook behavior, not a credited S3* agent.
- Supporting / enforcement mechanisms: `ReviewStore`, git snapshot/diff, delegated child text, hook event callbacks and tests.
- Closure path: diff/read/test output → operator or same model coding loop; no independent direct-evidence audit judgment → managerial owner → binding correction to ongoing workers.
- Why this is / is not agent-owned: `review` is a permission posture; `.air/local/evidence/T2-review.md` is development-only; a diff tool is evidence plumbing rather than independent audit closure.
- Evidence: [review service](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/reviews.py); [agent delegation](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [hooks](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/hooks.py); [review tests](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/tests/test_review_wiring.py); [README](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/README.md).
- Basis: structural.
- Confidence: medium-high for supported standard CLI.
- Caveats: custom independently commissioned auditors could be composed externally, but are not first-party default ownership evidence.

### Absence scope

- Surfaces inspected: change-snapshot/diff tools, `delegate_agent` result path, hook runtime, user-facing review mode, test fixtures, adjacent .air evidence files.
- Plausible first-party paths checked: complementary sampling outside operational self-report, autonomous audit verdict, independence from producer, return into a whole-system current-control owner.
- Why no material first-party path remains: first-party review is tool/evidence plumbing or optional S1-level delegation; the shipped session does not include an independent S3*→S3 feedback circuit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no integrated outward/future strategic adaptation loop changes the continuing agent organization's capabilities.
- Disturbance / variety regulated: provider aliases, current web search, skill inventory, plugins and updater are execution and human-managed configuration surfaces.
- Decisive decision or feedback right: user selects model, permission mode, plugins/skills and optional update; the coding agent reacts to current task, not a future environmental-coupled capability portfolio.
- Decision owner: human user/maintainer for product upgrades and configuration, present-task model for tactics.
- Supporting / enforcement mechanisms: provider registry, SkillStore, extension hooks, update checker and project instructions.
- Closure path: external package/version observation or user option → manual product/config choice; no built-in future intelligence appraisal decision returning into whole-current organizational capability.
- Why this is / is not agent-owned: proactive current task steps, ordinary skill loading or package update are not automatically S4.
- Evidence: [updater](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/updates.py); [extensions](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/extensions.py); [skills](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/skills.py); [agent](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: explicit human/parent adaptation may exist in the external development org but is not a first-party session-governed S4 parent loop.

### Absence scope

- Surfaces inspected: provider/config and model selection, tools/skill loading, updater, hook/plugin loaders, root model loop.
- Plausible first-party paths checked: future-focused external scanning, adaptation-option selection, legitimate adaptation authority and returned change to current capability.
- Why no material first-party path remains: shipped path is user-controlled configuration and present coding, not a closed future/environment organizational intelligence circuit.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate identity/constitutional policy decision path for the agent organization is present in the shipped coding runtime.
- Disturbance / variety regulated: dangerous commands, write permissions, plugin trust and model identity instructions are tactical execution policy rather than ultimate organizational self-definition.
- Decisive decision or feedback right: operator chooses modes and confirmation, hook/config enforces declared constraints; no runtime S5 adjudicator decides continuing purpose/ultimate tradeoffs.
- Decision owner: human for tool/trust config; deterministic policy checks for enforcement, without native S5 ownership.
- Supporting / enforcement mechanisms: `ApprovalPolicy`, capability gates, `HookRunner`, provider identity guard and user-owned extension settings.
- Closure path: configured mode/approval → permitted/blocked tool, not identity issue → legitimate parent/agent authority → binding whole-system policy return.
- Why this is / is not agent-owned: product identity prompt and permission modes don't confer ultimate organizational identity decision rights.
- Evidence: [policy](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/policy.py); [identity guard and tool loop](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/agent.py); [hooks](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/hooks.py); [CLI config](https://github.com/ffffff233/DeepSeekFathom/blob/2c68eff7bb7ae2eabf4d36a0331386f06af2d356/src/deepseekfathom/_core/cli.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external humans maintain the software but their OSS governance is not operationally wired as session-level S5.

### Absence scope

- Surfaces inspected: permission modes and confirmations, identity prompt, hook trust/permissions, provider and extension settings, adjacent project files.
- Plausible first-party paths checked: ultimate-purpose decisions, agent S5 alternatives, parent-governed binding identity/policy return into operating organization.
- Why no material first-party path remains: implementation controls execution and provider identity locally without reconstructable ultimate organizational policy adjudication.

## Recursion

The native coding `FathomAgent` is one operative S1. Nested `delegate_agent` creates ephemeral task-specific child agents with their own tool loops, but this does not establish a separately viable recursion with its own S2/S3/S3*/S4/S5 closed organization.

## Variety and escalation

Provider failures, context budget and tool errors trigger task-local retries/continuation or user-visible error. Unpermitted operations are rejected or ask user; optional hooks can block tool/prompt execution. These are action-level controls, not automatically an algedonic channel to an organizational response owner. Delegated child summaries rejoin the parent task.

## Evidence gaps

- Static primary-code analysis at pinned SHA plus available first-party tests; no paid provider-backed benchmark or live hosted deployment was executed.
- The root project contains `.air/` developer task/evidence artifacts, which are not in the installed distribution or linked as autonomous audit/management actors in the CLI; not counted toward higher VSM states.
- Custom user-authored hooks or extension servers may add behaviors but are not proven as shipped first-party ownership loops without actual wiring and owner/feedback provenance.
