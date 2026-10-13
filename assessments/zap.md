---
harness_id: zap
project_name: Zap
repository: https://github.com/zap-coding-agent/zap-coding-agent
review_ref: 9812a142b1d12c894c98a6f5d08cc776ecc760da
reviewed_at: 2026-10-13
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

# Zap

## Review boundary

- System in focus: shipped first-party Rust Zap terminal coding-agent runtime: session/LLM/tool loop, local code editing, shell, AST code-index, planner/verification watchdog, optional built-in `spawn_agent` delegated runs, and separate user-requested `/bg` tasks.
- Purpose and identity: solve local software engineering tasks by inspecting repository state, choosing/effecting code edits and tools, and responding to test and tool outcomes.
- Relevant environment: configured external LLM/provider endpoint, local user workspace and shell, project agent configuration, permissions, persistent sessions, opt-in MCP, operator and optional child contexts.
- Standard-distribution boundary: ordinary shipped CLI/TUI session and model-invoked `spawn_agent` with first-party runtime. `/bg` is included as a user-operated alternative with clear human ownership; document-only research, demos, evals, website, development CI and hand-authored multi-agent workflows are excluded as owners of coding organization functions.
- Credited operating / distribution surfaces: [README.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/README.md); [ARCHITECTURE.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/ARCHITECTURE.md); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/mod.rs); [turn.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/turn.rs); [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs); [agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs); [agent_core.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/agent_core.rs); [background_agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/background_agent.rs); [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs); [plan_execution.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/plan_execution.rs); [task_planner.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/task_planner.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/code_index/mod.rs); [permission_manager.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/permission_manager.rs); [persistence.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/persistence.rs).
- Adjacent first-party surfaces excluded from ownership: source test mocks, CI and release workflows, examples/demos/evals/research docs, user-operational GitHub reviews, third-party MCP/provider functions, and custom operator-configured agent organizations not wired by the default product.
- First-party operating / deployment modes considered: one CLI/TUI coding session; model-invoked parallel `spawn_agent` tool in its registered normal mode; optional user-invoked detached `/bg` sessions; plan execution, per-command watchdog and edit verification, AST search/index and skills/context injection.
- Recursion level: primary coding model owns one S1; an invoked spawned child has its own model/loop (additional operating S1), but generic split task execution and `/bg` registry do not by themselves form an actively managed S2/S3 organization.
- Reviewed revision: `9812a142b1d12c894c98a6f5d08cc776ecc760da`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[ARCHITECTURE.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/ARCHITECTURE.md) traces the local CLI/TUI → Session → LLM → tool-results loop. [turn.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/turn.rs) executes each model turn, and [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs) applies permissions, invokes local tools (potentially concurrently) and feeds actual outcomes back. [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/code_index/mod.rs) supplies AST/code navigation, [context_manager.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/context_manager.rs) context assembly, and [persistence.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/persistence.rs) saves local work state. [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs) tracks repeated failure of the *same* verify command and can nudge or stop tool access with a handoff summary; [plan_execution.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/plan_execution.rs) describes per-step verification in the coding loop rather than a separately owned reviewer decision.

[agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs) ships a `spawn_agent` model tool: it starts a child [agent_core.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/agent_core.rs) coding session with its own context and full tools, returning summary/changed files/turn and call counts. Tool description warns to request independent subtasks with no shared writes. Its `files_in_scope` property says it is used to detect conflicts, but the shipped `execute` implementation uses only `goal` and `context`; no file-overlap check or conflict-specific prevention/return is called there. The user-operated [background_agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/background_agent.rs) separately starts arbitrary detached child sessions, tracking running/done/failed/kill status and returning results to the UI; the operator chooses their respective goals and task roster. Neither mere multiple independent agents nor a static admonition against same-file edits proves S2 current-conflict regulation.

## Operational model

The main model chooses file/shell/search actions, then interprets actual execution results. It may delegate a self-contained task to a subordinate model and summarize its outcome, but the shipped tool has neither executable cross-subtask interference attenuation nor an active whole-S1-portfolio management loop. Verification watchdog operates on the current coding session's failing shell command; it does not commission an independent auditor or return a separate critical organizational judgment to a metasystem.

## S1 — Operations

- State: A
- Function: choose and carry out codebase engineering work under uncertainty, including source inspection, modifications, shell/test execution and error-driven repairs.
- Disturbance / variety regulated: unknown program structure and test behavior, failed commands, tool limitations, insufficient context and unexpected code interactions.
- Decisive decision or feedback right: model selects the next specific tool/argument or correction after observing actual results; invoked child runs its own independent model-tool loop.
- Decision owner: active coding model in Session (or in a delegated child), not shell/tool dispatcher, task-index or watchdog.
- Supporting / enforcement mechanisms: LLM client, session context and turn loop, code index, file/shell tools, permission gate, turn and verification budgets.
- Closure path: user goal → model-selected read/edit/execute action → source or shell result → next model turn or completion; tool failure may trigger model-directed revision.
- Boundary reachability: normal CLI/TUI session and first-party `spawn_agent` registered in the default non-child session runtime.
- Why this is / is not agent-owned: the same deterministic tools alone cannot invent appropriate engineering actions without a model decision.
- Evidence: [README.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/README.md); [ARCHITECTURE.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/ARCHITECTURE.md); [turn.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/turn.rs); [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/mod.rs); [agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs); [agent_core.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/agent_core.rs)
- Basis: explicit / structural
- Confidence: high for source-wired operating loop, with no paid-provider live execution
- Caveats: code index and watchdog are supporting mechanisms, not separate autonomous S1 actors.

## S2 — Coordination

- State: —
- Function: no specific observed or source-wired first-party attenuation of material inter-S1 interference with returned behavior change is established.
- Disturbance / variety regulated: independent write-capable delegated children can collide in a shared working tree; duplicative work and resource contention are plausible inter-worker disturbances.
- Decisive decision or feedback right: no inspected controller detects such a concrete collision and limits or reallocates participating child work; source tool's `files_in_scope` is not consumed by the dispatch path.
- Decision owner: parent model verbally instructed to split independent work, with deterministic tool batching; neither is an executed S2 conflict resolution owner.
- Supporting / enforcement mechanisms: `spawn_agent` prompts, optional `files_in_scope` declaration, per-child session isolation, tool call parallelism, user-operated background session tracker.
- Closure path: child task may return a result to the parent; no independently evidenced conflict report → attenuation affecting the conflicting children → updated child work closure.
- Why this is / is not agent-owned: a concurrent `spawn_agent` response and “do not edit same file” instruction do not detect and settle actual inter-S1 interference, and UI background status is not a corrective channel.
- Evidence: [agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs); [agent_core.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/agent_core.rs); [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs); [background_agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/background_agent.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/mod.rs); [ARCHITECTURE.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/ARCHITECTURE.md)
- Basis: structural and explicit `execute` argument usage
- Confidence: medium-high for reviewed standard-distribution paths
- Caveats: first-party shared-workspace conflict prevention in a future revision is not ruled out; this bounded review does not conclude conceptual impossibility.

### Absence scope

- Surfaces inspected: built-in child `spawn_agent` tool, its declared and actually used parameters, model-turn parallel dispatch, child session, user background registry and worktree-facing tools.
- Plausible first-party paths checked: conflict detection using sibling `files_in_scope`, shared working-tree write interference, operator/parent arbitration and return to affected S1s.
- Why no material first-party path remains: `execute` does not consult declared file scopes or an active conflict arbitration registry, and documented independent-task guidance/isolated child sessions return standalone results without in-boundary interference-specific corrective feedback.

## S3 — Inside-and-now control

- State: —
- Function: no separately evidenced current whole-organization managerial decision for the live roster/commitments of subordinate coding S1s.
- Disturbance / variety regulated: failing delegated work, conflicting team priorities and resource/commitment tradeoffs of several simultaneous coding workers.
- Decisive decision or feedback right: parent can issue additional isolated child subtasks and consume their final answers; no built-in whole-current roster view and discretionary active priority reassignment applied to existing model-running child tasks was found.
- Decision owner: parent coding model controls its present task decomposition, while `/bg` list/start/kill remains a user operation.
- Supporting / enforcement mechanisms: per-session task lists, user background agent status panel, automatic model routing by task classifier, plan step runner and tool watchdog.
- Closure path: delegated output returns to parent coding turn, and user background status to UI; no documented active whole-team status → discretionary control choice → changed current commitments across children and closed return.
- Why this is / is not agent-owned: decomposition of one coding request into independent calls, or one process's retries/verification, is S1 strategy and task execution rather than whole-current organizational control.
- Evidence: [agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs); [background_agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/background_agent.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/mod.rs); [task_planner.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/task_planner.rs); [plan_execution.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/plan_execution.rs); [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: a human managing `/bg` subtasks may perform organizational S3 outside the assessed agent runtime.

### Absence scope

- Surfaces inspected: native model and user subprocess launches, Session task tracking, background agent status, task classifier/router, verification/plan mechanisms.
- Plausible first-party paths checked: whole active sibling-S1 current view, owner with discretion over relative resource commitments, corrective reassignment to ongoing children and returned status.
- Why no material first-party path remains: shipped model invocation provides delegated goals and final summaries; `/bg` exposes status to human operator, without a first-party self-directed whole-current team management cycle.

## S3* — Complementary audit

- State: —
- Function: no separately owned independent source-first auditor forms a corrective challenge to a coding worker's claims and returns to a distinct current-control manager within the shipped organization.
- Disturbance / variety regulated: a coding agent's potentially false edit/test-success claims, missed regressions or unsafe modifications.
- Decisive decision or feedback right: watchdog detects repeated failing verification commands, and plans require tests, but the same coding loop acts on those outputs; no separately commissioned independent auditor verdict and managerial corrective return is wired as a first-party mode.
- Decision owner: normal code verification remains with originating coding model and deterministic watchdog; human/CI reviewers are outside runtime.
- Supporting / enforcement mechanisms: [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs) per-command fail ledger/nudges and tool withdrawal, [plan_execution.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/plan_execution.rs) step verification rules, shell output, user-visible audit log.
- Closure path: test failure returns to the same coding actor and can alter its next step or cause stop; no independent reviewer → distinct manager → affected coder corrective cycle.
- Why this is / is not agent-owned: watchdog and editing-plan QA are task execution reliability protections, not separate complementary audit ownership.
- Evidence: [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs); [plan_execution.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/plan_execution.rs); [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs); [turn.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/turn.rs); [agent.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/tools/agent.rs); [ARCHITECTURE.md](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/ARCHITECTURE.md)
- Basis: structural
- Confidence: medium-high
- Caveats: arbitrary user prompts to a child can request a code review, but no shipped reviewer-specific direct-evidence counterclaim mechanism/management consequence is credited from that hypothetical usage.

### Absence scope

- Surfaces inspected: model/tool verification loop, watchdog, plan prompts, shipped child agent tool and any standard separate reviewer registration/return.
- Plausible first-party paths checked: independently sourced review verdict contradicting implementer completion; findings to current manager; enacted correction in active S1 operation.
- Why no material first-party path remains: documented runtime QA is by same coding actor or fixed watchdog; generic child capacity alone does not establish a distinct independent review-to-current-management return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no agentic outside/future-oriented organizational capability strategy plus applied capacity adaptation cycle.
- Disturbance / variety regulated: changing coding requirements, future language support, provider/skill constraints and environment capability.
- Decisive decision or feedback right: no separate actor selects long-horizon capability changes from external signals and implements them into the agent organization.
- Decision owner: developer/operator configures provider, skill/index settings and deployments; model addresses the current coding task.
- Supporting / enforcement mechanisms: AST code-index, dynamic skill matching and context refresh, task planning, persistence and provider routing.
- Closure path: contexts or skills inform current action, but no future organizational-capability choice → decision → implementation → feedback loop is evidenced.
- Why this is / is not agent-owned: adaptive context retrieval and task-level planning are not equivalent to future-capacity intelligence.
- Evidence: [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/code_index/mod.rs); [skill_manager.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/skill_manager.rs); [memory_refresh.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/memory_refresh.rs); [task_planner.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/task_planner.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/config/mod.rs); [context_manager.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/context_manager.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: repository roadmap and plugin ecosystem are operator/developer extensions outside this boundary.

### Absence scope

- Surfaces inspected: code index, context and skills, task planner, provider config, sessions and memory refresh.
- Plausible first-party paths checked: prospective environment scanning, long-term discretionary capability choice, application of a changed organizational capacity and returned evaluation.
- Why no material first-party path remains: sources support current task execution and prompt inputs; neither prospectively enacted capacity change nor autonomous strategic owner is demonstrated.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-purpose/policy authority over the agent organization is demonstrated.
- Disturbance / variety regulated: mission/identity tradeoffs distinct from per-command safety decisions.
- Decisive decision or feedback right: no S5 owner arbitrates organizational purpose and returns binding governing change to multiple S1s.
- Decision owner: user/operator and developer configuration set purpose/permissions; built-in permission gate and watchdog enforce narrower runtime safety conditions.
- Supporting / enforcement mechanisms: permissions, destructive-command checks, sandbox, task goals, user config and runtime tool policy.
- Closure path: allow/deny a shell or file operation, nudge/stop a repeatedly failing agent and return technical status; no higher-purpose identity decision or constitutional binding return.
- Why this is / is not agent-owned: safety policy enforcement does not assume ownership of the organization's ultimate identity or mission.
- Evidence: [permission_manager.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/permission_manager.rs); [tools.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/tools.rs); [watchdog.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/watchdog.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/config/mod.rs); [mod.rs](https://github.com/zap-coding-agent/zap-coding-agent/blob/9812a142b1d12c894c98a6f5d08cc776ecc760da/src/session/mod.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: upstream maintainers and users may exercise governance outside the system assessed.

### Absence scope

- Surfaces inspected: native permission and sandbox mechanisms, per-turn workflow/verification gates, agent project configs and user/developer governance surfaces.
- Plausible first-party paths checked: mission/policy dispute → legitimate ultimate owner → actual binding organizational change with feedback.
- Why no material first-party path remains: controls are confined to a task's tool permissions, execution safety and error stops rather than organizational identity/policy decisions.

## Recursion

One active Zap Session is a model-led operating S1. `spawn_agent` may create subordinate, independently model-running operating S1 contexts, but the packaged tool provides primarily isolated goals and results, not a second management layer with proven S2/S3/S3* functions. User-driven `/bg` tasks have their own sessions under operator supervision, not automatically a single autonomous coding organization.

## Variety and escalation

Model/tool feedback and deterministic verification watchdog reduce coding-task disturbances. Failure thresholds can nudge the same model or strip tools, and permission checks can require human approval; both are within current S1 execution/safety supervision, not a distinct independent auditor or metasystem authority. No first-party inter-sibling interference controller, whole-current manager, prospective capability adaptation or final-purpose governance was evidenced on the pinned source.

## Evidence gaps

Pinned-source static review; no credentialed model-provider session executed. `files_in_scope` is present in model-facing schema but unused by the implementation of `spawn_agent`, so documentation about conflict detection was not promoted to a positive S2 witness. Child results and `/bg` status cannot be substituted for live whole-current S3 closure. Verification watchdog is a source-wired safety mechanism, not an independent reviewer. Findings and negative states are bounded to the explicit first-party shipped distribution and the frozen revision.
