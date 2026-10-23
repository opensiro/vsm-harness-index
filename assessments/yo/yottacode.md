---
harness_id: yottacode
project_name: yottacode
repository: https://github.com/yottadynamics/yottacode
review_ref: 11ffd5884a2827636d54b14c0d60d53c9c93c5d8
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# yottacode

## Review boundary

- System in focus: the first-party yottacode coding harness, its local agent/subagent sessions and optional experimental parallel dispatch at frozen commit `11ffd5884a2827636d54b14c0d60d53c9c93c5d8`.
- Purpose and identity: execute user-directed repository work through model-chosen file, shell, search and integration tools while constraining subagent execution and surfacing current subagent activity.
- Relevant environment: user requests, repository contents, git worktree state, model/provider replies, runtime errors, approval decisions, task progress and conflicts between simultaneously acting subagents.
- Standard-distribution boundary: Go CLI, attended TUI, one-shot execution, first-party model/tool loop, separately model-backed `Agent` subagents, session task registry, optional `dispatch`/`integrate` and built-in `/code-review`.
- Credited operating / distribution surfaces: `internal/agent/`, `internal/subagents/`, `internal/tui/`, `internal/worktree/`, explicit `--experimental dispatch` feature switch and corresponding checked-in docs/configuration.
- Adjacent first-party surfaces excluded from ownership: source-only Go tests, templates and development scripts, external model providers/MCP servers, user-authored agents and downstream orchestration, and the upstream repository maintainer organization.
- Reviewed modes: interactive TUI with foreground/background subagents; experimental `dispatch` with disjoint write-worker worktrees and `integrate`; one-shot where background dispatch falls back to waiting; on-demand code review; user-controlled stop and approvals.
- Recursion level: one current yottacode task/session and its concurrently active child S1 agents; not the full upstream project community, remote model hosts or other unrelated yottacode installations.
- License screen: checked-in `LICENSE` at the frozen ref contains the MIT License; candidate license review passes for repository assessment and does not grant authority to change upstream policy.
- Observation date: 2026-10-23; Profile `0.2.4`; Methodology `0.3.7`.

## Repository architecture

The main Go model loop lets the model decide which first-party tools to call based on user input, repository inspection and resulting tool feedback. `AgentTool` runs isolated children with explicit role prompts, independent turns, tool capabilities and transcripts. The shared `subagents.Registry` records currently running or completed tasks, last activity, resource usage, batch membership and cancellation hooks. A TUI dock and `/subagents` picker expose this roster to the human operator.

The **opt-in experimental** `dispatch` tool splits a coding request into parallel read-only or write-capable child agents. Each write worker must receive a declared file-ownership set; fixed validation checks file collisions **within and across concurrently running dispatch batches**, and write workers run in separate git worktrees/branches with allowed-file enforcement. The model can later call `integrate` on the resulting branches; merge conflicts stop and return an explicit remediation path. This is an actual, bounded inter-S1 conflict attenuation circuit, but its owner is deterministic runtime code and its effectiveness is not a universal file-conflict guarantee.

Separately, the **human** can inspect the live session roster and selectively cancel a particular running child or an entire dispatch batch through `/subagents`, which has a wired `Registry.Cancel` / `CancelBatch` implementation. That is a bounded present-operations intervention right for the whole **local session cohort**, not autonomous S3. On-demand `/code-review` can fan out fresh read-only reviewers and code-verifiers, but the producing workflow chooses when and how to invoke it and synthesizes their results; the inspected path does not demonstrate a sufficiently independently governed complementary audit return to S3.

Frozen sources: [`loop.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/loop.go), [`agent_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/agent_tool.go), [`dispatch_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/dispatch_tool.go), [`integrate_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/integrate_tool.go), [`tasks.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/subagents/tasks.go), [`cmd_subagents.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/tui/cmd_subagents.go), [`dispatch.md`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/docs/dispatch.md).

## Operational model

Each model-backed coding or delegated child agent owns S1 operational tool choices. Within the explicitly enabled dispatch subset, S2=C belongs to the deterministic file-scope collision guard and isolated-worktree execution. At the local session/cohort recursion S3=P belongs to the **human operator**, who can examine the whole current task roster and selectively terminate a child or a dispatch batch. Model-directed decomposition and post-hoc branch integration do not themselves establish autonomous S3. No independently governed S3* circuit, strategic S4 or ultimate S5 identity closure was established.

## S1 — Operations

- State: A
- Function: select and execute concrete code-repository actions in response to an operator task and changing tool observations.
- Disturbance / variety regulated: unknown source layout, errors, evolving diffs, model/provider feedback, nested subtasks and conflicting tool outcomes.
- Decisive decision or feedback right: the model in each main or child loop selects follow-up inspections, edits, tool actions and final replies.
- Decision owner: active first-party main or child model-backed agent.
- Supporting / enforcement mechanisms: registry of tools, conversation loop, `AgentTool`, role prompts, permission modes, transcript retention, worktrees, provider adapters and sandbox options.
- Closure path: request → model-selected tool → tool execution/outcome → model's next decision or final result; child results may feed back to the parent model.
- Boundary reachability: shipped interactive and one-shot entry points construct and run the first-party agent loop; subagent roles use the real `AgentTool` child runner, not example-only code.
- Why this is / is not agent-owned: the model decides operational actions based on changing feedback while Go tool handlers constrain and implement effects.
- Evidence: [`loop.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/loop.go), [`agent_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/agent_tool.go), [`prompt.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/prompt.go).
- Basis: frozen first-party implementation and deterministic source tests; **no live LLM-agent runs**.
- Confidence: high on reachable mechanism; no task-success estimate.
- Caveats: results depend on a configured external model and permissions; scripted tests do not show effectiveness in deployment.

## S2 — Coordination

- State: C
- Function: attenuate concurrent write interference among separately deciding child agents in **opt-in dispatch**.
- Disturbance / variety regulated: two or more independently active write workers might edit the same project file, racing or invalidating integration.
- Distinct S1 units: independent model-backed `dispatch` write workers, each with its own child loop, prompt, tool results, worktree and branch.
- Inter-S1 disturbance: overlapping edit ownership across task partitions or even across independently started dispatch batches could produce collisions.
- Attenuating coordination relation: each worker is assigned a declared file set; source validation rejects overlaps before spawning and checks claims against already running tasks, while write filters confine changed paths and worktrees isolate git state.
- Feedback into subsequent S1 behaviour: an invalid colliding batch is not admitted; admitted children work inside disjoint scopes, and parent receives committed branch outcomes or explicit error/conflict results to adjust its subsequent work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the partition validation actively suppresses the concrete inter-agent disturbance of conflicting file ownership rather than merely routing a message or displaying progress.
- Decisive decision or feedback right: reject a conflicting write scope and enforce each admitted worker's allowed writes; the model chooses proposed partitions but cannot override the gate.
- Decision owner: deterministic first-party Go runtime **C**, not an autonomous coordination agent.
- Supporting / enforcement mechanisms: `validateWritePartition`, registry running-claim inspection, worker-specific write options, isolated worktrees, commit-status reporting and conflict-stop integration.
- Closure path: model-proposed multiworker task → validate ownership / running claims → accept disjoint agents or reject overlap → isolated worker outputs → parent-selected integration and conflict feedback.
- Boundary reachability: supported `--experimental dispatch` registers `DispatchTool` and `integrate`; actual `AgentTool` children, task registry and worktree machinery are called by the tool implementation.
- Why this is / is not agent-owned: fixed first-party checks enforce S1 coexistence; agent initiative in proposing a split is not ownership of the inter-unit collision rule.
- Evidence: [`dispatch_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/dispatch_tool.go), [`tasks.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/subagents/tasks.go), [`integrate_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/integrate_tool.go), [`dispatch_tool_test.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/dispatch_tool_test.go).
- Basis: frozen code and deterministic Go tests, subject to actual test-run status recorded in the review receipt.
- Confidence: medium-high for declared-file enforcement; low for universal merge safety.
- Caveats: experimental opt-in; partition depends on supplied file declarations and cannot guarantee semantic compatibility across disjoint files. Ordinary `Agent` fan-out is not protected by this dispatch guard; conflicts can still stop `integrate`.

| Mode | S2 state | Disturbance and closure | Owner |
| --- | --- | --- | --- |
| Normal `Agent` delegation | — | Worker count/permissions and reporting, without demonstrated cross-worker write-collision protection | None established |
| Experimental `dispatch` enabled | C | Cross-batch write file-scope overlap is rejected and each worker is worktree/file confined | Deterministic Go runtime |

## S3 — Inside-and-now control

- State: P
- Function: monitor and intervene in the currently running agent cohort as a whole at one attended TUI session boundary.
- Disturbance / variety regulated: runaway, stuck, costly or incorrectly prioritized parallel children could continue consuming time/resources or modifying work after the operator sees they should stop.
- Decisive decision or feedback right: the human views every current task in the live `/subagents` roster and selectively cancels an individual running child or all workers in a named dispatch batch.
- Decision owner: attended TUI **human operator P**. The model can create work partitions and integrate results, but lacks a demonstrated model-owned selective current-cohort intervention function.
- Supporting / enforcement mechanisms: shared `subagents.Registry` with status/activity/batch identity/cancel hooks, TUI dock/picker and `/subagents stop` command, `Cancel`/`CancelBatch` using child context cancellation.
- Closure path: task registry captures current workers → operator examines live progress → `/subagents stop <id>` or `stop batch <id>` → child cancellation request → affected running child stops on context check while unrelated active tasks continue.
- Boundary reachability: attended TUI registers `cmdSubagents` and the picker backed by the same session task registry used by foreground/background `AgentTool` and `DispatchTool`.
- Whole-system current view: the local registry lists all currently active session child agents including independent dispatch batches, statuses, last activity, branch and resource usage, rather than only one child's report.
- Current-control decision scope: an operator can revoke an ongoing child commitment individually, or a whole named batch, without canceling all unrelated active tasks; control is local-session scoped and cancellation is cooperative.
- Why this is / is not agent-owned: the intervention is selected by the human from live current-state observations; the registry and cancel API enforce but do not autonomously choose the management action.
- Evidence: [`cmd_subagents.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/tui/cmd_subagents.go), [`tasks.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/subagents/tasks.go), [`subagent_dock.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/tui/subagent_dock.go), [`subagents_picker.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/tui/subagents_picker.go).
- Basis: source-verified operator control and deterministic registry/command tests; not a human-in-the-loop execution trial.
- Confidence: medium-high for attended local-session control; no claim of autonomous S3 or distributed orchestration.
- Caveats: TUI dependent; cancellation is cooperative and worker commit finalization can be cancellation-detached briefly, so the request is not a synchronous kill guarantee. One-shot lacks this live attended roster.

## S3* — Complementary audit

- State: —
- Function: no verified sufficiently independent audit of operational claims with a corrective return to current-control authority.
- Disturbance / variety regulated: a worker could claim a patch passes checks while its implementation is wrong or incomplete; the on-demand code-review tool may identify some such faults.
- Decisive decision or feedback right: `/code-review` asks a producing session's model to launch fresh review/verifier subagents and synthesize findings; no first-party independent S3 audit mandate or control over the audit scope and disposition was shown.
- Decision owner: no distinct S3* owner established; local reviewer child agents may exercise ordinary S1 verification choices inside the originating production workflow.
- Supporting / enforcement mechanisms: `code_review_context`, separate read-only reviewer contexts, prompt-driven adversarial code-verifiers, diff snapshot construction and final textual report.
- Closure path: user/requested local diff → model-chosen review fan-out → findings returned to the same originating session; no independently controlled complementary reality path coupled to a responsible S3 decision is established.
- Why this is / is not agent-owned: model-backed review is real, but a separately prompted critic does not automatically become a complementary organizational audit independent of the operation it reviews.
- Evidence: [`code_review_workflow.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/code_review_workflow.go), [`code_review.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/promptmacros/code_review.go), [`cmd_code_review.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/tui/cmd_code_review.go).
- Basis: frozen first-party wiring and prompt design.
- Confidence: medium, bounded to session-level ownership, not external review governance.
- Caveats: independent reviewer *contexts* and raw source access are valuable but do not prove independent audit initiation/closure; third-party review or a deliberately separate operating session is outside this boundary.

### Absence scope

- Surfaces inspected: on-demand `/code-review`, built-in review and code-verifier subagents, diff snapshots, test tools, transcripts, TUI task display, `integrate` conflict feedback.
- Plausible first-party paths checked: adversarial review-verifier pair as S3*, independent verifier prompt as alternate access, ordinary Go tests, branch conflict detection and human reading reviewer output.
- Why no material first-party path remains: the observed code review is voluntarily invoked and scoped/synthesized in the producing agent's ordinary work; findings are not shown entering a distinct accountable whole-current control decision via an independently governed audit channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party strategic external/future sensing that develops adaptation options and returns them to current capability decisions.
- Disturbance / variety regulated: shifts in future demand, external providers, competition, tools or research are not a demonstrated ongoing adaptation process at this local harness recursion.
- Decisive decision or feedback right: the model may research, plan or consult tools for the present user task, while maintainers or users choose any longer-run product redesign.
- Decision owner: none established for local-session S4.
- Supporting / enforcement mechanisms: web/MCP tools, memory, plan/explore agents, repository search, advisor-model routing and prompt macros.
- Closure path: observations about external materials serve a current coding task; no persistent external/future distinction → adaptation proposal → S3 capability negotiation/update channel is wired.
- Why this is / is not agent-owned: research or planning by a current task actor does not entail future-facing organizational intelligence and operating-capability evolution.
- Evidence: [`agent_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/agent_tool.go), [`prompt.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/prompt.go), [`architecture.md`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/docs/architecture.md).
- Basis: bounded first-party source/design review.
- Confidence: medium.
- Caveats: user can ask a model to do strategy research; this is not evidence of a shipped self-directed S4 capability-update loop.

### Absence scope

- Surfaces inspected: tool/model loop, plan/explore/review roles, advisor routing, memory and architecture/dispatch mode docs.
- Plausible first-party paths checked: advisor model as S4, planning role as strategic intelligence, web research, history/memory as organizational learning.
- Why no material first-party path remains: none demonstrates an externally prospective adaptation-option process with an evidenced current-capability dialogue and return.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational identity decision with legitimate closure over this assessed operating session.
- Disturbance / variety regulated: permissions and unsafe commands need tactical gating, but that is not the system-identity and constitutional choice relevant to S5.
- Decisive decision or feedback right: users choose permission modes, allow specific tool actions, change provider config and ask for or stop tasks; upstream maintainers set software defaults. None is shown making a legitimate identity-level decision fed into S3 and S4.
- Decision owner: no in-boundary ultimate-policy or identity authority established.
- Supporting / enforcement mechanisms: auto/plan/yolo permission modes, approval prompts, dispatch unattended policy, command hardline floor, optional container sandbox.
- Closure path: action request → permission check → allow or deny a tool execution; no durable S5 identity deliberation → cross-functional policy closure path is evidenced.
- Why this is / is not agent-owned: hardcoded safety defaults and operator consent for individual executions do not confer organization-wide identity decision rights on the acting model.
- Evidence: [`dispatch.md`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/docs/dispatch.md), [`tui-slash-commands.md`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/docs/tui-slash-commands.md), [`agent_tool.go`](https://github.com/yottadynamics/yottacode/blob/11ffd5884a2827636d54b14c0d60d53c9c93c5d8/internal/agent/agent_tool.go).
- Basis: bounded source/review of approvals and distribution modes.
- Confidence: medium-high for rejecting tool permission as S5.
- Caveats: independent enterprise governance may be layered over the tool but cannot be credited to this first-party session.

### Absence scope

- Surfaces inspected: yolo/auto/plan modes, user approval, background dispatch policy, sandboxing, command safety floor and maintainer boundary.
- Plausible first-party paths checked: human approval as S5, command hardline constraints as constitutional policy, persistent config as identity, project maintainers as runtime S5.
- Why no material first-party path remains: these paths control tactical tool effects or upstream development policy without an evidenced legitimate S5 decision and return to the assessed running organization.

## Distributed OSS parent arrangement

The yottadynamics maintainers can revise the external product, and operators can organize multiple sessions, but no first-party binding governance channel connects either to a current local S3/S4/S5 recursion. The attended TUI operator is credited only with bounded S3 present-session interventions, not as S5 identity authority by default.

## Self-hosted and non-human modes

The model/tool loop serves CLI/TUI and one-shot S1. Background work and the live S3=P roster are TUI-specific; the one-shot command waits for dispatch children instead of hosting detached worker operations. The guarded S2=C dispatch remains experimental and opt-in. Unattended write workers cannot execute shell/tests on the host without a separate sandbox, and this enforcement is not an autonomous control decision. These modes must not be pooled as if all capabilities are always available.

## Recursion

Individual delegated model-backed agents form S1 units inside the current session. Experimental dispatch gives them bounded S2=C write ownership coordination; the human can exercise session-wide S3=P via selective cancel. That recursion does not extend to unrelated repositories, other concurrently started yottacode sessions, providers or upstream maintainer decisions.

## Variety and escalation

An edit collision within dispatch is blocked before admission, while semantic/merge conflicts may still return to the parent agent at integration. Exceptional subagent status appears in the TUI so a human can abort an affected live commitment. The terminal review report and isolated reviewer contexts do not by themselves demonstrate independently governed S3* closure. No future-governance or identity loop is evidenced.

## Evidence gaps

- No live LLM agents were run; any tests in this assessment are deterministic scripts/Go unit tests, not end-to-end success evidence.
- Dispatch is experimental, opt-in and scope-sensitive. Its file-overlap guard cannot ensure compatibility of semantically related non-overlapping files; shell/tests in host background workers are blocked.
- Human cancellation is cooperative, not a guaranteed instantaneous kill, and does not grant autonomous S3 rights to the model.
- On-demand code-review reporters may be independent model contexts, but a legitimate complementary S3* claim requires proof of independent initiation/control and finding disposition beyond the producing workflow.
