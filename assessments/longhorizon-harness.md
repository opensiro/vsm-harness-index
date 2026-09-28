---
harness_id: longhorizon-harness
project_name: LongHorizon-Harness
repository: https://github.com/AMAP-ML/LongHorizon-Harness
review_ref: a1dd930614972b92361c1b9cd6aac441a6db5a65
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LongHorizon-Harness

## Review boundary

- System in focus: the first-party LongHorizon-Harness loop-engineering runtime at frozen revision `a1dd930614972b92361c1b9cd6aac441a6db5a65`, including the generic Manager→Executor→Auditor round loop, durable round ledger/checkpoints, role prompts/parsers, external-agent adapters, role isolation/permission guards, human gate/dashboard, supervisor/control bus, trajectory persistence, plugin/configuration and recovery/continuation paths.
- Purpose and identity: turn existing coding/computer-use agents into long-running systems by repeatedly reconstructing verified state, asking a Manager for the next bounded step, running an Executor, independently auditing the result, checkpointing only accepted progress and recovering across failures/context refreshes.
- Relevant environment: external Codex CLI, Claude Code, OpenCode and DeepSeek Harness (`dsh`) agent runtimes; their model/provider services and tool loops; target CLI/GUI workspaces; computer-use MCP/plugins; human approval/instruction input; filesystem/UI/log/test evidence.
- Standard-distribution boundary: Python code and bundled role prompts/configuration actually shipped by LongHorizon-Harness at the frozen revision. The autonomous task/model/tool loops implemented by Codex, Claude Code, OpenCode and DeepSeek Harness remain adjacent agent runtimes. The harness's prompts, parsers, round scheduling, checkpoint rules and permission guards do not transfer those upstream runtimes' autonomous cognition into first-party ownership.
- Credited operating / distribution surfaces: `manager.py`; `role_prompts.py`; `prompt_texts.py`; `auditor_agent.py`; built-in adapters and agent registry; local environment; Claude auditor read-only guard; dashboard/human gate; supervisor/control bus; runtime-signal handling; trajectory artifacts; config/CLI/plugin/web workbench surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/evaluation infrastructure, benchmark vendored copies and documentation-only claims. External agent CLI internals, provider/model reasoning, their native tool loops, and external MCP/computer-use service decisions are not credited as LongHorizon-Harness-owned autonomous actors.
- First-party operating / deployment modes considered: ordinary CLI runs; Web workbench/supervised runs; mixed role-specific backends/models; resume/follow-up continuation; GUI and CLI executor/auditor roles; human approval/instruction gates; computer-use plugin integration.
- Recursion level: one LongHorizon-Harness long-running task organization around one original user goal and its round ledger. Manager, Executor and Auditor are first-party-defined roles in the protocol, but at the frozen standard distribution the actors inhabiting those roles are separately implemented upstream agent runtimes.
- Reviewed revision: `a1dd930614972b92361c1b9cd6aac441a6db5a65`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

LongHorizon-Harness implements a substantial first-party organizational loop. `manager.py` durably records rounds, rebuilds a Manager prompt from the original goal plus trusted task state and prior Auditor reports, parses the Manager's route (`gui`, `cli`, `ask`, `done`, `blocked`), invokes one bounded Executor episode, invokes an Auditor episode over the resulting state/evidence, and carries the verified report into later rounds. A Manager `done` claim is not sufficient: first-party code accepts completion only when a prior Auditor report parses as complete, integrity-clean and contract-aligned; otherwise it synthesizes corrective feedback for the next Manager turn.

That strength does not by itself establish repository-relative autonomous S1. The public README explicitly says LongHorizon-Harness “turns existing agents into long-running computer-use systems”, “does not … replace an existing agent”, and uses a lightweight `AgentAdapter` that “preserves each agent's native execution loop”. The standard package depends on FastAPI/Uvicorn/WebSockets and contains no direct model SDK/API actor. `CommandAgentAdapter.run_episode()` writes the role prompt and executes a configured shell command. The built-in factories create only `CodexAdapter`, `ClaudeCodeAdapter`, `OpenCodeAdapter` or `DeepSeekHarnessAdapter`; these construct `codex exec`, `claude --print`, `opencode run` or `dsh` commands and consume their outputs.

The semantic Manager, Executor and Auditor judgments are therefore made inside adjacent agent CLIs. First-party parsing and gating can reject malformed plans, runtime failures, dirty/read-write violations and unsupported completion claims, but it does not itself choose the substantive next task, perform the open-ended tool work or independently reason over the evidence. Remove the external CLI agents while retaining the round ledger, prompts, parsers, dashboard, supervisor and gates: the harness can preserve/control state but cannot produce the next plan, execution or semantic audit verdict.

This ownership boundary is especially important for S3 and S3*. LongHorizon-Harness supplies unusually strong constructor/enforcement structure for a wider composed organization: the Manager receives trusted whole-task history; Auditors are role-separated and, for Claude Code, guarded read-only; completion requires clean audit; human gates can reopen or extend a run. But the decisive Manager/Auditor intelligence remains in externally implemented agent runtimes. Under the repository-relative Profile boundary, these mechanisms cannot be promoted to positive organizational states without a qualifying first-party S1 actor.

Primary evidence:

- [`README.md`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/README.md) — explicit “turns existing agents” / “does not replace an existing agent” boundary, Manager/Executor/Auditor loop, lightweight adapter preserving native execution loops, role-specific external backends and verified-state semantics.
- [`src/lh_harness/adapters/base.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/base.py) and [`cli_agent.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/cli_agent.py) — `AgentAdapter` protocol and command-backed episode execution.
- [`src/lh_harness/adapters/codex.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/codex.py), [`claude_code.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/claude_code.py), [`opencode.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/opencode.py) and [`deepseek_harness.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/deepseek_harness.py) — standard external agent-runtime command adapters.
- [`src/lh_harness/manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/manager.py) — first-party round ledger, role invocation sequencing, Manager route parsing, completion guard, audit feedback, human gate and continuation/recovery loop.
- [`src/lh_harness/prompt_texts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/prompt_texts.py) and [`role_prompts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/role_prompts.py) — semantic contracts supplied to the external Manager/Executor/Auditor actors and deterministic parsing of their outputs.
- [`src/lh_harness/auditor_agent.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/auditor_agent.py) — deterministic audit-report parsing/guards around an externally generated substantive auditor report.
- [`src/lh_harness/adapters/claude_permissions.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/claude_permissions.py) — first-party role isolation/read-only enforcement for Claude-backed auditor modes.
- [`src/lh_harness/dashboard/gate.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/dashboard/gate.py) — durable human approval/instruction gate around the external Manager loop.

## Operational model

A run binds each role to a selected external agent backend/model. At each round, first-party code reconstructs the Manager prompt from the original request, stable task contract, current verified task state and selected Auditor reports. The external Manager decides the next route/subtask. LongHorizon-Harness parses that decision, invokes the chosen external Executor with a bounded fresh context, then invokes an external Auditor over the task contract and actual workspace/UI/log/test evidence. The Auditor's structured natural-language result is parsed and becomes trusted history only subject to deterministic control guards.

The next round sees the checkpointed state plus audit evidence rather than blindly accepting Executor claims. Timeouts, malformed plans, invalid completion and provider failures are turned into durable feedback/recovery state. The dashboard can require human input or extend/reopen a run, and v0.1.7 can continue a finished/stopped run using the same ledger. Thus the first-party harness strongly structures a composed long-horizon organization, while the actual autonomous role decisions remain in the upstream agent processes.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit owns the substantive open-ended task/tool decision loop inside the LongHorizon-Harness repository boundary.
- Disturbance / variety regulated: coding/computer-use task ambiguity, workspace/UI state, tool observations, intermediate failures and changing remaining work are interpreted by the selected upstream agent CLI.
- Decisive decision or feedback right: interpret the bounded task and observations, choose tool/UI/command actions, evaluate returned evidence and continue/revise execution.
- Decision owner: external Codex/Claude Code/OpenCode/DeepSeek Harness runtime inhabiting the configured Executor role (and analogous external runtimes for Manager/Auditor roles).
- Supporting / enforcement mechanisms: round scheduler, role prompts, bounded episode budgets, workspace/harness-path isolation, runtime-signal parsing, trajectory capture, checkpoint ledger, plugin/MCP configuration and human-control surfaces.
- Closure path: first-party round loop builds role prompt → `CommandAgentAdapter` launches selected external agent CLI → that upstream agent performs its native model/tool loop → first-party code records/parses output → later role/round invokes another external agent based on that evidence. The autonomous operational loop itself closes inside the upstream agent runtime.
- Why this is / is not agent-owned: the package intentionally preserves each existing agent's native execution loop and contains no direct model SDK/API actor in the standard distribution. First-party code wraps/sequences the autonomous dependency rather than implementing its task-level cognition.
- Evidence: [`README.md`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/README.md); [`src/lh_harness/adapters/base.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/base.py); [`src/lh_harness/adapters/cli_agent.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/cli_agent.py); [`src/lh_harness/cli.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/cli.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the deployed composed system is intentionally agentic and can run for many rounds/hours. `—` is a repository-relative ownership finding, not a claim that the assembled LongHorizon + Codex/Claude/OpenCode/DSH system lacks autonomous behavior.

### Absence scope

- Surfaces inspected: package dependencies, all built-in agent adapters/factories, generic role loop, CLI role binding, model/provider configuration, local environment process execution and plugin/MCP integration.
- Plausible first-party paths checked: Manager as first-party agent; Executor role as S1; custom `AgentAdapter`; direct model API/SDK invocation; deterministic round loop as autonomous actor.
- Why no material first-party path remains: every standard semantic role is backed by an external agent runtime through command execution, while first-party logic supplies state, prompts, parsing and enforcement but not the open-ended model/tool decision loop.

## S2 — Coordination

- State: —
- Function: no qualifying coordination relation among multiple first-party autonomous S1 units is established at this recursion.
- Disturbance / variety regulated: role context contamination, concurrent run/process interference and workspace/harness-state leakage are constrained, but the standard Manager→Executor→Auditor loop is primarily sequential and its autonomous role actors are external runtimes.
- Decisive decision or feedback right: fixed role isolation and process/run boundaries constrain access; substantive task partitioning and handoff decisions are made by the external Manager.
- Decision owner: deterministic first-party runtime for isolation/enforcement; external Manager agent for semantic decomposition/routing.
- Supporting / enforcement mechanisms: distinct role prompts and episode files, hidden harness paths, unique prompt files, process groups, role-specific permissions/read-only auditor policy, run/supervisor ownership boundaries.
- Closure path: role/run isolation changes which external agent process may access which state, but no distinct first-party S1 plurality → concrete inter-S1 disturbance → first-party coordination decision → changed subsequent first-party S1 behavior loop is established.
- Why this is / is not agent-owned: role separation and sequencing are materially useful organizational mechanisms, but positive S2 under the Profile requires qualifying first-party S1 units at the declared recursion and a concrete interaction disturbance among them.
- Evidence: [`src/lh_harness/manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/manager.py); [`src/lh_harness/adapters/claude_permissions.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/claude_permissions.py); [`src/lh_harness/utils/process_group.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/utils/process_group.py).
- Basis: structural absence at declared ownership boundary
- Confidence: high
- Caveats: the wider composed system has strongly differentiated Manager/Executor/Auditor roles, but that is not sufficient to publish repository-relative S2 when the autonomous actors inhabiting those roles are adjacent systems.

### Absence scope

- Surfaces inspected: role sequencing, role permissions, prompt/context partitioning, process/run isolation, supervisor ownership, workspace/harness hidden paths and continuation state.
- Plausible first-party paths checked: Manager handoff as S2; role separation; concurrent-run protection; read-only auditors; process-group isolation.
- Why no material first-party path remains: the inspected mechanisms protect state/process boundaries around external agent actors rather than regulating a concrete interaction disturbance among first-party autonomous S1 units.

## S3 — Inside-and-now control

- State: —
- Function: the first-party loop carries a whole-task current-state ledger and enforces route/completion rules, but the substantive current-control judgment is made by the external Manager runtime.
- Disturbance / variety regulated: verified progress, failed/rejected rounds, remaining work, invalid plans, timeouts, user follow-ups and changing task state.
- Decisive decision or feedback right: choose the next bounded GUI/CLI subtask, ask a human, declare blocked or propose completion, and revise the task contract/state from audit evidence.
- Decision owner: external agent CLI bound to the Manager role.
- Supporting / enforcement mechanisms: durable rounds, trusted Auditor reports, task-state/contract extraction, route parser, invalid-plan/completion feedback, budget/recovery loop, human gate and resume/follow-up ledger.
- Closure path: first-party runtime reconstructs whole-task context → external Manager chooses current route/commitment → first-party runtime validates/parses and invokes external Executor/Auditor → accepted/rejected evidence returns to the next external Manager round. The management loop is first-party, but the decisive organizational judgment is adjacent.
- Why this is / is not agent-owned: `manager.py` does not itself decide what work should happen next; it parses the Manager agent's natural-language control block. Removing the external Manager leaves the current-state ledger and enforcement but no substantive current-control actor.
- Evidence: [`src/lh_harness/manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/manager.py); [`src/lh_harness/role_prompts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/role_prompts.py); [`src/lh_harness/prompt_texts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/prompt_texts.py).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: at the assembled-system boundary this is a strong S3-like architecture: Manager receives curated whole-task state and can replan from audit/failure evidence. Repository-relative publication remains `—` because the Manager actor is an external harness.

### Absence scope

- Surfaces inspected: Manager prompt construction, route parsing, task-state/contract persistence, completion guard, invalid-plan feedback, timeout/recovery, resume/follow-up and dashboard instruction injection.
- Plausible first-party paths checked: `manager.py` itself as S3 owner; completion gate as S3; human gate; supervisor/service manager; deterministic recovery loop.
- Why no material first-party path remains: first-party code maintains/enforces current state but does not own the discretionary judgment selecting current organizational commitments; that judgment comes from the externally invoked Manager agent or human.

## S3* — Complementary audit

- State: —
- Function: LongHorizon-Harness creates a strong independent-audit protocol and deterministic acceptance guards, but the substantive audit judgment is produced by an external Auditor agent runtime.
- Disturbance / variety regulated: Executor self-reports may be incomplete or wrong about actual files/UI/logs/tests, contract coverage, persistence, integrity or forbidden shortcuts.
- Decisive decision or feedback right: inspect actual task state/evidence and determine completion, integrity cleanliness and contract alignment; those semantic judgments are returned in the Auditor's natural-language report.
- Decision owner: external Codex/Claude/OpenCode/DSH runtime bound to the GUI/CLI Auditor role.
- Supporting / enforcement mechanisms: separate Auditor prompt/context, independent acceptance-constraint backcheck, role-specific read-only controls, Claude workspace snapshot guard, audit format parser/repair, fail-closed invalid headers, clean-audit requirement for completion and durable audit reports.
- Closure path: external Executor acts → first-party harness constructs Auditor prompt over task/plan/output plus actual environment access → external Auditor independently inspects state and emits verdict → first-party parser/guards accept or reject that report and feed it into the next Manager round. The audit closure is strong in composition but the autonomous audit judgment is adjacent.
- Why this is / is not agent-owned: deterministic code can reject malformed or internally inconsistent reports and enforce that completion requires a clean report, but it cannot independently produce the semantic verdict that the operational claim is correct. The report author is the separately implemented upstream agent.
- Evidence: [`src/lh_harness/manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/manager.py); [`src/lh_harness/auditor_agent.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/auditor_agent.py); [`src/lh_harness/prompt_texts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/prompt_texts.py); [`src/lh_harness/adapters/claude_permissions.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/adapters/claude_permissions.py).
- Basis: explicit + structural absence at declared ownership boundary
- Confidence: high
- Caveats: among excluded wrappers this is unusually strong S3* construction evidence: actual environment inspection, role separation, read-only guards and corrective return are explicit. A wider assessment that intentionally includes the external Auditor actor could credit that composed path.

### Absence scope

- Surfaces inspected: Auditor role prompts, actual-workspace/UI evidence access, acceptance-constraint backcheck, report parser, format repair, integrity/contract controls, Claude read-only/snapshot guard and completion acceptance.
- Plausible first-party paths checked: audit parser as S3* actor; completion guard; snapshot mutation detector; format repair; deterministic runtime-signal checks.
- Why no material first-party path remains: first-party mechanisms validate/enforce the audit protocol, while the substantive complementary judgment over operational reality is made by the external Auditor model/agent.

## S4 — Intelligence / adaptation

- State: —
- Function: no first-party environment-facing prospective intelligence function selects an organizational adaptation and returns it into current capability.
- Disturbance / variety regulated: cross-round failures, provider/runtime errors, context refresh and version/plugin availability are handled operationally, but they are not converted into autonomous changes to the organization's longer-term capability/strategy.
- Decisive decision or feedback right: longer-term backend/model/plugin/configuration changes remain user/operator choices; the external Manager only plans the current task horizon.
- Decision owner: none established inside the first-party boundary for S4.
- Supporting / enforcement mechanisms: durable failure evidence, round recovery, configurable role backends/models/reasoning effort, `doctor`/update check, plugin manager and human continuation/instruction surfaces.
- Closure path: no external/future distinction → generated organizational adaptation option → selection → returned capability change loop is established. The loop recovers the current task and can replan current work, which is S3-like behavior rather than prospective S4.
- Why this is / is not agent-owned: “long-horizon” refers to persistence of one task across rounds, not an intelligence function sensing future external variety and redesigning the organization. Update/plugin/model controls apply human-selected changes.
- Evidence: [`README.md`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/README.md); [`src/lh_harness/manager.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/manager.py); [`src/lh_harness/utils/update_check.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/utils/update_check.py).
- Basis: structural absence
- Confidence: high
- Caveats: the Manager can revise task plans from failure/audit evidence, but this is inside-and-now task control, not the external/prospective adaptation loop required for S4.

### Absence scope

- Surfaces inspected: round recovery/replanning, role backend/model configuration, update checker, plugin manager, doctor diagnostics, dashboard continuation and failure evidence.
- Plausible first-party paths checked: long-horizon replanning as S4; cross-round learning; model/backend switching; version update discovery; plugin installation.
- Why no material first-party path remains: mechanisms either maintain the current task or expose/apply externally selected configuration changes; no first-party prospective adaptation owner closes a future-environment-to-capability loop.

## S5 — Policy / identity

- State: —
- Function: no first-party ultimate-policy/organizational-identity decision authority is established.
- Disturbance / variety regulated: task contracts, role permissions, hidden harness paths, model/backend choice, human approval triggers and configured safety constraints govern one run's execution.
- Decisive decision or feedback right: the user/operator supplies the original goal, configuration and approval/instruction decisions; external Manager/Auditor agents derive task-local contracts and findings from that request.
- Decision owner: external human/operator for top-level task/configuration authority; no first-party S5 actor.
- Supporting / enforcement mechanisms: stable task contract prompt, role permission policies, human gate/rules, config precedence, plugin permissions, hidden-state boundary and supervisor controls.
- Closure path: user/configuration supplies task/policy constraints → first-party harness injects/enforces them across external agents → run proceeds under those constraints. No first-party ultimate authority decides organizational identity/purpose/policy and returns its own decision into autonomous first-party operations.
- Why this is / is not agent-owned: a Manager may reconstruct a task contract, but the prompt explicitly roots it in the original user request and the Auditor independently backchecks against that request. This is task-level policy interpretation inside adjacent agents, not first-party ultimate-policy ownership.
- Evidence: [`src/lh_harness/prompt_texts.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/prompt_texts.py); [`src/lh_harness/dashboard/gate.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/dashboard/gate.py); [`src/lh_harness/config.py`](https://github.com/AMAP-ML/LongHorizon-Harness/blob/a1dd930614972b92361c1b9cd6aac441a6db5a65/src/lh_harness/config.py).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: the parent human clearly retains meaningful authority through approvals/instructions and the original request. Without first-party S1 and an explicit ultimate-policy/identity function for a Bernstein-like organization, this does not justify repository-relative `P` for S5.

### Absence scope

- Surfaces inspected: task-contract rules, Manager/Auditor contract handling, role permissions, config precedence, dashboard approval rules/human hook, plugin permission controls and supervisor/run boundaries.
- Plausible first-party paths checked: stable task contract as S5; human gate as parent S5; role policy; model/backend configuration; original-goal preservation.
- Why no material first-party path remains: these paths preserve/enforce task/operator constraints around externally autonomous agents but do not establish a first-party organizational ultimate-policy/identity decision loop.

## Assessment summary

LongHorizon-Harness is a sophisticated loop-engineering substrate with unusually strong round-state management, Manager/Executor/Auditor separation, evidence-based checkpointing, independent-audit construction, human control and recovery. Nevertheless, the frozen standard distribution intentionally preserves and invokes the native execution loops of existing external agent CLIs; every semantic Manager, Executor and Auditor episode is produced by one of those adjacent runtimes. First-party Python owns sequencing, prompts, ledger, parsers and enforcement, not the decisive open-ended model/tool judgment. Under Profile 0.2.4 / Methodology 0.3.6, the repository-relative boundary therefore does not establish S1, and its otherwise strong S3/S3* construction mechanisms are not promoted into S2-S5 organizational ownership.

Proposed canonical outcome: `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
