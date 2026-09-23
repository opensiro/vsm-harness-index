---
harness_id: omniharness
project_name: omniHarness
repository: https://github.com/archimedes-run/omniHarness
review_ref: fd71e375ff626ae99537163edd3d14b16100d786
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# omniHarness

## Review boundary

- System in focus: one omniHarness long-horizon agent run at pinned revision `fd71e375ff626ae99537163edd3d14b16100d786`, including the first-party lead-agent runtime, bounded subagent task tool, sandbox/runtime middleware, persistent custom skills, skill-evolution path, custom-agent SOUL/config path and self-verifying preview/build feedback loop.
- Purpose and identity: execute long-horizon user work through a lead autonomous agent that can use tools, decompose work into bounded parallel subagents, synthesize their results, repair execution failures, retain reusable skills and operate custom agents with persistent identity/configuration.
- Relevant environment: user objectives and corrections, repositories/files, web/MCP sources, sandbox/build/runtime feedback, model providers and external ACP agents.
- Standard-distribution boundary: omniHarness-owned lead-agent framework, task/subagent executor, sandbox tools/middleware, skill storage/evolution tool, custom-agent SOUL/configuration and shipped API/runtime. Provider/model internals, external MCP/ACP services and repository CI do not donate functions.
- Credited operating / distribution surfaces: `README.md`; `backend/packages/harness/harness.md`; `backend/packages/harness/omniharness/agents/lead_agent/prompt.py`; `backend/packages/harness/omniharness/tools/builtins/task_tool.py`; `backend/packages/harness/omniharness/tools/skill_manage_tool.py`; `backend/packages/harness/omniharness/config/skill_evolution_config.py`; `backend/packages/harness/omniharness/tools/builtins/update_agent_tool.py`.
- Adjacent first-party surfaces excluded from ownership: repository-development skills/spec-kit material, CI/release/contributor governance, tests/fixtures, and external model/ACP internals.
- First-party operating / deployment modes considered: default lead-agent execution; bounded parallel subagent mode; sandboxed build/preview repair loop; optional `skill_evolution.enabled` mode; custom-agent chat with persistent SOUL/config self-update under user authority.
- Recursion level: one lead-agent run is the system-in-focus. Delegated subagents are subordinate S1 work units within that run. The lead agent is the metasystem actor for work decomposition/current control. Reusable skill evolution changes future run capability at the same installation/user boundary.
- Reviewed revision: `fd71e375ff626ae99537163edd3d14b16100d786`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The published harness package is an executable LangGraph-based super-agent runtime. A lead model actor receives a tool surface, sandbox, memory/skills and optional subagent delegation. `task` creates a separate `SubagentExecutor`, runs it asynchronously in its own context, streams status and returns the completed result to the lead actor. The lead prompt explicitly owns decomposition, batching under a hard concurrency limit and final synthesis.

The runtime also closes two longer-horizon governance paths that are distinct from ordinary memory. When `skill_evolution.enabled`, the lead prompt directs the autonomous agent to patch reusable skills after non-obvious errors, user corrections or recurring workflows; `skill_manage` persists create/edit/patch operations, records agent authorship/history, security-scans writes and refreshes the enabled-skill prompt cache so later operation uses the changed capability. Separately, custom agents carry a persistent `SOUL.md`; `update_agent` rewrites that identity/config only in custom-agent chat and explicitly frames identity refinement as user-requested authority, with the changed SOUL taking effect on the next turn.

## S1 — Operations

- State: A
- Function: perform admitted user work through the lead autonomous agent and subordinate task agents using files, shell/sandbox, web/MCP and other tools.
- Disturbance / variety regulated: open-ended user objectives, repository/file state, external information, tool/build/runtime failures and iterative observations.
- Decisive decision or feedback right: choose task-local reasoning, tool actions, code/file changes and when additional delegated work is needed.
- Decision owner: the autonomous lead/subagent model actor on the shipped runtime path.
- Supporting / enforcement mechanisms: LangGraph execution, sandbox middleware/tools, task executor, guardrails, persistence, memory and tool error handling.
- Closure path: user objective → lead agent chooses actions/delegation → tools/subagents execute → observations/results return → agent revises behavior until it answers or completes the task.
- Boundary reachability: the published `omniharness` package and normal lead-agent/API path instantiate this loop directly.
- Why this is / is not agent-owned: deterministic middleware transports/enforces state, while substantive operational choices remain model-owned.
- Evidence: [`README.md`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/README.md); [`backend/packages/harness/harness.md`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/harness.md); [`task_tool.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/tools/builtins/task_tool.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider/ACP internals are not inherited.

## S2 — Coordination

- State: —
- Function: no complete S2 mutual-adjustment loop among sibling subagents is established.
- Disturbance / variety regulated: subagents can execute in parallel and the lead enforces a hard batch/concurrency ceiling, but reviewed evidence does not tie sibling interaction to a concrete conflict/oscillation and returned behavioral adjustment between those S1 units.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: separate subagent contexts, concurrency limit, batching, task status/result collection and shared parent sandbox/thread metadata.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: delegation, batching and concurrency enforcement alone do not establish S2.
- Evidence: [`prompt.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/agents/lead_agent/prompt.py); [`task_tool.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/tools/builtins/task_tool.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the hard concurrency limit regulates capacity but is not credited without the required inter-S1 disturbance witness.

### Absence scope

- Surfaces inspected: lead-agent subagent prompt, task executor, sandbox/thread state, concurrency limit and returned task status/results.
- Plausible first-party paths checked: bounded parallel task batches, separate contexts, shared parent metadata, sandbox isolation and cancellation.
- Why no material first-party path remains: these paths allocate/isolate subordinate work but do not establish a specific interaction-generated sibling disturbance plus an S2-specific relation that changes subsequent sibling behavior.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current whole-run work program by decomposing complex objectives, selecting concurrent sub-tasks, assigning specialized subagents and synthesizing returned work.
- Disturbance / variety regulated: excessive or poorly scoped decomposition, sequential dependencies, incomplete aspect coverage, failed/timed-out delegated work and the need to prioritize a bounded number of current sub-tasks.
- Decisive decision or feedback right: choose current decomposition, subagent type/scope, batch priority under the concurrency limit, whether to continue with another batch and how to synthesize returned results into subsequent work.
- Decision owner: the autonomous lead agent.
- Supporting / enforcement mechanisms: task tool, separate executors, hard concurrency ceiling, task status events, timeout/cancel handling and returned results.
- Closure path: lead observes current objective/results → chooses the next allocation/batch → task tool creates bounded workers → worker results/failures return → lead revises the current work program or synthesizes completion.
- Boundary reachability: the shipped lead-agent prompt enables this mode whenever subagents are configured; `task_tool.py` implements the actual subordinate execution path.
- Why this is / is not agent-owned: runtime machinery enforces limits and lifecycle; the lead model owns decomposition, priority, assignment and synthesis discretion.
- Evidence: [`prompt.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/agents/lead_agent/prompt.py); [`task_tool.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/tools/builtins/task_tool.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is run-level S3 over subordinate workers, not installation-wide fleet governance across unrelated sessions.
- Whole-system current view: the lead agent owns the admitted objective, its planned sub-task set/batches and the success/failure/timeout/results returned from every launched subordinate task before choosing the next batch or synthesis.
- Current-control decision scope: decomposition, assignment, subagent specialization, batch priority, continuation after results/failures and final synthesis.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit organization is established.
- Disturbance / variety regulated: the preview verification gate can stop ordinary completion on a broken build and feed the error back for repair, but the same operational agent receives the build/dev-server error, fixes its own code and re-checks.
- Decisive decision or feedback right: no separate independent audit judgment is established.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: preview auto-start, build/runtime error gate, sandbox execution and ordinary agent repair loop.
- Closure path: not applicable for the negative S3* classification; the loop is credited as ordinary S1 feedback.
- Why this is / is not agent-owned: a verifier label or deterministic gate is insufficient where producer and corrective judgment remain in the same operational path without complementary independent access/judgment.
- Evidence: [`README.md`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/README.md).
- Basis: explicit negative classification.
- Confidence: high.
- Caveats: the self-verifying loop is operationally useful; function mapping prevents relabeling it as S3* merely because it verifies.

### Absence scope

- Surfaces inspected: build/preview verification loop, subagents, sandbox middleware, task returns and skill security scans.
- Plausible first-party paths checked: preview gate, separate subagent execution, security scanner and tests/build feedback.
- Why no material first-party path remains: none supplies a standard producer claim → materially independent challenge → independent audit judgment → bounded corrective return relation.

## S4 — Outside-and-then adaptation

- State: A(P)
- Function: turn task/environment feedback into reusable future capability by evolving persistent custom skills that are reloaded into subsequent lead-agent prompts.
- Disturbance / variety regulated: repeated non-obvious errors, recurring workflows, gaps discovered through substantial tool use and user corrections can leave the current reusable skill set mismatched to future work.
- Decisive decision or feedback right: decide that observed task/environment evidence warrants patching an existing reusable skill or, in the parent mode, creating a new reusable skill after user confirmation.
- Decision owner: base mode — autonomous lead agent for edits/patches to existing custom skills under the enabled skill-evolution mode; parent mode — user supplies the decisive confirmation before creation of a new skill.
- Supporting / enforcement mechanisms: `skill_evolution.enabled`, `skill_manage`, validation/security scan, change history and enabled-skill prompt-cache refresh.
- Closure path: task/environment produces a reusable lesson → lead identifies an adaptation → `skill_manage` persists/scans the change → skill cache refreshes → later lead-agent turns/runs receive the updated skill capability.
- Boundary reachability: `SkillEvolutionConfig` is a first-party optional runtime mode; `harness.md` states `skill_manage_tool` is inserted when enabled, and the shipped lead prompt supplies the adaptation policy.
- Why this is / is not agent-owned: the security scanner deterministically constrains writes but does not choose the adaptation; in base mode the lead agent owns the patch/edit judgment. New-skill creation explicitly retains a separate user confirmation path.
- Evidence: [`prompt.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/agents/lead_agent/prompt.py); [`skill_evolution_config.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/config/skill_evolution_config.py); [`skill_manage_tool.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/tools/skill_manage_tool.py); [`harness.md`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/harness.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic persistent memory is not the basis; the positive finding depends on the separate skill-evolution write/reload loop.
- External distinction: runtime/task evidence includes non-obvious tool/environment errors and explicit user corrections encountered while operating in the external task environment.
- Future / prospective distinction: the prompt asks whether the lesson is non-trivial/recurring and worth preserving as a reusable skill for later work rather than merely fixing the current turn.
- Adaptation option generated: patch/edit an existing custom skill or propose/create a new custom skill containing the reusable workflow/lesson.
- Path back into current capability / S3: successful skill writes refresh the enabled-skill system-prompt cache, so subsequent lead-agent operation receives the changed reusable capability.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | autonomous lead agent | non-obvious error, substantial tool-use lesson, corrected approach or recurring workflow indicates an existing custom skill should change | agent calls `skill_manage` patch/edit; scan + persistence succeed; cache refresh returns updated skill into later operation | `prompt.py`; `skill_manage_tool.py`; `skill_evolution_config.py` |
| Parent (`P`) | user | lead concludes a genuinely new reusable skill should be created and requests the required confirmation | user confirms; lead creates the skill through the same scanned/persistent tool path; refresh makes it available to later operation | `prompt.py`; `skill_manage_tool.py` |

## S5 — Identity / ultimate policy

- State: P
- Function: persist a custom agent's identity-level SOUL/configuration when the user authoritatively asks that agent identity to be refined.
- Disturbance / variety regulated: the custom agent's enduring identity, description or governing configuration may no longer reflect the user's intended role/policy for that named agent.
- Decisive decision or feedback right: decide the identity-level SOUL/configuration change that should govern subsequent turns of the custom agent.
- Decision owner: the user/parent; `update_agent` is explicitly framed as the mechanism used when the user asks to refine the agent's identity/configuration.
- Supporting / enforcement mechanisms: custom-agent `SOUL.md`, per-user config, staged/atomic persistence, validation and prompt rebuilding.
- Closure path: user requests identity/config refinement → custom agent invokes `update_agent` with the selected full SOUL/config change → files persist → next user turn rebuilds the lead agent with the fresh SOUL/config → subsequent operation is governed by the returned identity decision.
- Boundary reachability: custom agents and `update_agent` are shipped first-party operating paths; the tool is available inside an existing custom-agent chat rather than only in repository development.
- Why this is / is not agent-owned: the model transports/implements the identity change, but the documented decisive authority is the user request; therefore the positive state is parent-governed rather than autonomous S5.
- Evidence: [`update_agent_tool.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/tools/builtins/update_agent_tool.py); [`prompt.py`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/omniharness/agents/lead_agent/prompt.py); [`harness.md`](https://github.com/archimedes-run/omniHarness/blob/fd71e375ff626ae99537163edd3d14b16100d786/backend/packages/harness/harness.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary user task instructions are not S5; this finding is limited to the persistent named custom-agent SOUL/config identity path.
- Identity / ultimate-policy issue: whether the enduring named custom agent's SOUL/description/governing tool/skill/model configuration should be changed for future operation.
- Ultimate authority in each claimed mode: the parent-governed mode is owned by the user/parent requesting and specifying the refinement in the custom-agent chat.
- Return-to-operation path: `update_agent` persists the revised SOUL/config and the next turn rebuilds the agent from those files, governing subsequent operation under the new identity/policy.
