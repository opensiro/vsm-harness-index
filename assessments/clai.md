---
harness_id: clai
project_name: clai
repository: https://github.com/pentoshi007/clai
review_ref: 630d85f9eb7c2b5b3e499c503abf5834610c6939
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# clai

## Review boundary

- System in focus: installable clai terminal agent at the exact frozen source `630d85f9eb7c2b5b3e499c503abf5834610c6939`, with its first-party model/tool coding runner, optional concurrent read-only investigation subagents, session/task state, local tools, evidence restrictions, scope/permission gate and provider routing.
- Purpose and identity: carry out user-requested coding and, in explicitly authorized scopes, diagnostic/security investigations using model-selected real tools; optionally coordinate multiple distinct context-gathering jobs that feed a primary worker.
- Relevant environment: local repository/files, shell/test/http/scanner output, provider quotas/errors, changing user goals, subagent reports, authorization boundaries, active sessions and task state.
- Standard-distribution boundary: shipped clai CLI and interactive/noninteractive sessions; embedded first-party `src/agent/`, `src/agent/subagents/`, local tool, execution, auth/scope, prompt and session stores. LLM provider inference, arbitrary downloaded skills/MCP tools, outside concurrent agents, external CI/pentest program, and downstream user governance are dependencies, not credited first-party owners.
- Credited operating / distribution surfaces: `src/agent/runner.ts`, `src/agent/turn/loop/`, `src/agent/turn/tool-execution/`, `src/agent/subagents/{manager,worker,tools,read-only-tools}.ts`, `src/tools/definitions/subagents.ts`, `src/agent/task-plan.ts`, `src/store/subagents.ts`, `src/agent/evidence-governor.ts` and local session/scope/provider code.
- Adjacent first-party surfaces excluded from ownership: README marketing text and test/CI/release/build files, benchmark and UI v2 spikes, repository contributor decisions, user's separate CI/scanners/remote MCP agents and credential/provider services. Feature existence is checked against runnable wiring rather than treated as an organizational function by name.
- First-party operating / deployment modes considered: normal model-backed coding session; enabled /orchestration mode with 2–3 distinct independent read-only context-gathering children; disabled orchestration; persistent/resumed terminal session; scope-restricted authorized security task; keyless/local or provider-fallback mode. These are not automatically separate recursive viable systems.
- Recursion level: one coding/investigation session with one primary action-taking model S1 plus optional multiple bounded read-only evidence-gathering S1 workers under a parent agent.
- Reviewed revision: `630d85f9eb7c2b5b3e499c503abf5834610c6939` (intake #898, not latest upstream).
- Observation date: 2026-10-15.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The first-party runner prepares a model-visible tool schema, runs provider streaming/tool rounds and passes selected calls through `runSingleTool` / execution gates into real tools, returning tool output for subsequent model choices. A task/evidence governor, durable plans, context compaction, provider-key fallback, sessions and user authorization limit or preserve current operations. This is not merely a command wrapper around a separately installed coding-agent CLI.

When orchestration is enabled, the primary model receives explicit `ORCHESTRATION: ON` system guidance and `subagent.start`, `start_many`, `list`, `read`, `wait`, `stop`, `restart` tools. These route into a session-scoped `SubagentManager` which tracks multiple children, recent events/reports, a limit of three active workers, child abort controllers and restart state. A first-party child runs a provider-backed tool loop with an enforced read-only tool list; it gathers independent repository/scope evidence and returns a report, not direct code modifications. The primary model decides which independent assignments to issue and owns checking/using reports before making implementation decisions. A duplicate *identical assignment* fingerprint guard blocks a second launch before it becomes an S1 operation; it is not by itself a measured conflict/oscillation feedback mechanism between already operating S1 units.

The single-session autonomy contract therefore differs from a multi-writer fleet: the active work cells are a coding S1 and optional independent investigator S1s, while an agent-owned current-management decision operates over the active investigator roster. No shipped autonomous code-review department, future strategic capability-selection department or ultimate policy/identity-governance procedure has been located inside this distribution.

Pinned evidence: [`README.md`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/README.md); [`src/agent/runner.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/runner.ts); [`src/agent/turn/loop/run-rounds.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/loop/run-rounds.ts); [`src/agent/turn/tool-execution/single-tool.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/tool-execution/single-tool.ts); [`src/agent/subagents/manager.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/manager.ts); [`src/agent/subagents/worker.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/worker.ts); [`src/agent/subagents/tools.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/tools.ts); [`src/agent/subagents/read-only-tools.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/read-only-tools.ts); [`src/tools/definitions/subagents.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/tools/definitions/subagents.ts); [`src/agent/evidence-governor.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/evidence-governor.ts).

## Operational model

The principal model owns open-ended coding and evidence gathering, including the discretionary choice of next tools. Separately instantiated read-only child model loops absorb bounded independent research variety. The first-party subagent roster is a current operational view; the primary model manages multiple outstanding child commitments via tool-mediated assignment, stop, follow-up and result integration. Runtime caps, session persistence, duplicate-launch rejection and provider backoff are deterministic supports to that management rather than autonomous decision owners. Generic optional specialized prompts and arbitrary MCP servers are not credited as additional organizational departments.

## S1 — Operations

- State: A
- Function: perform open-ended user-directed coding/security-investigation tasks by selecting and iterating real actions on source and observed evidence.
- Disturbance / variety regulated: unknown code structure, failing commands/tests, changing files, HTTP/terminal output, incomplete task facts and model errors/limits.
- Decisive decision or feedback right: the model chooses relevant operations/tool arguments, reacts to actual tool results, can continue or stop, and can request bounded independent investigation in orchestration mode.
- Decision owner: first-party model-directed main clai agent; separately instantiated read-only child model loops own their own bounded investigations while provider inference is external.
- Supporting / enforcement mechanisms: tool schema/routing, permission/scope gates, terminal and FS tools, context recovery, durable task plan, result capture and provider key retry.
- Closure path: user objective and current workspace evidence → model selects tool → first-party execution and guard → output/denial/error returned to model → next action, delegation, or final answer.
- Boundary reachability: shipped CLI initializes the first-party runner and dispatches model tool calls, while the optional shipped `SubagentManager` connects first-party model-backed investigator workers; neither depends on a separate external agent binary.
- Why this is / is not agent-owned: removing model-directed tool/next-action choices leaves deterministic execution and policy checks, not a task-sensitive coding actor.
- Evidence: [`src/agent/runner.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/runner.ts); [`src/agent/turn/loop/run-rounds.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/loop/run-rounds.ts); [`src/agent/turn/tool-execution/single-tool.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/tool-execution/single-tool.ts); [`src/agent/subagents/worker.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/worker.ts); [`README.md`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: evidence/progress checks are not proof of task success, safety compliance or a higher-system management function.

## S2 — Coordination

- State: —
- Function: no materially closed shipped coordination of a specific *interacting-S1 interference* despite parallel context-gathering child loops.
- Disturbance / variety regulated: potential duplicate evidence gathering, resource consumption, conflicting conclusions and overlapping investigative effort among children.
- Decisive decision or feedback right: `SubagentManager.assertUnique` blocks an exact repeated assignment before it launches; `assertCapacity` limits concurrent instances, while prompt guidance asks for unrelated scopes. No worker-to-worker discrepancy/oscillation detection and corrective inter-S1 feedback right is established.
- Decision owner: fixed admission guards and task-allocation instructions, not an autonomous S2 conflict owner.
- Supporting / enforcement mechanisms: SHA-256 assignment fingerprint, three-slot hard cap, read-only tool restrictions, event/report transport and parent tool selection.
- Closure path: rejected duplicate submission returns an error to the parent before a second child exists; individual child reports return to the parent for task use. No observed or structurally wired conflict between existing S1s is tracked/attenuated with a subsequent worker-response loop.
- Why this is / is not agent-owned: preventing a duplicate request at the tool interface and serializing receipt of results do not demonstrate regulation of interactions among already operative S1 cells.
- Evidence: [`src/agent/subagents/manager.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/manager.ts); [`src/agent/subagents/tools.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/tools.ts); [`src/agent/subagents/worker.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/worker.ts); [`src/tools/definitions/subagents.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/tools/definitions/subagents.ts).
- Basis: structural
- Confidence: medium-high
- Caveats: a wider externally authored orchestration arrangement might implement actual S2; this is a bounded finding for the shipped read-only gatherer mode.

### Absence scope

- Surfaces inspected: child manager uniqueness/capacity/abort/result states; child read-only runtime; parent subagent tools and orchestration guidance; primary tool execution and task plan.
- Plausible first-party paths checked: concurrent file-write collision, duplicate-active-worker reconciliation, cross-worker contradictory-result arbitration, interference-specific adjustment delivered back to children, and model-mediated conflict resolution after a competing result.
- Why no material first-party path remains: shipped children cannot modify target files or launch other children, and the only conflict-like checks apply to identical launch requests *before* a second S1 begins. Distinct research result reports require parent verification, but there is no built-in inter-S1 disagreement control path over established children.

## S3 — Inside-and-now control

- State: A
- Function: manage current, parallel operational investigation commitments and capacity under one active coding session.
- Disturbance / variety regulated: competing child research assignments, unfinished or irrelevant investigations, cancellation/reprioritization needs, saturation of the three-worker capacity and partial/incomplete reports.
- Decisive decision or feedback right: main model views active child roster/status/results, chooses distinct assignments to start, may stop/correct/restart tasks, await any completed child, and integrates verified findings into subsequent main work.
- Decision owner: first-party model-directed main agent as current controller over several distinct read-only operational S1 cells; `SubagentManager` enforces commands and capacity.
- Supporting / enforcement mechanisms: session-scoped child map, list/read/wait/stop/restart tool API, abort controllers, per-child event/report state, shared model system guidance and maximum-concurrency guard.
- Closure path: whole-session current child states and pending research needs → parent model start/stop/restart/dependency decision → `SubagentManager` action on target child → updated status/return report → parent model subsequent assignment/implementation choices.
- Boundary reachability: `src/agent/runner.ts` includes orchestration guidance in first-party agent context, `src/agent/turn/tool-execution/single-tool.ts` dispatches `runSubagentTool`, and `manager.ts` supplies live child control; enabled orchestration mode is a shipped operator-supported mode rather than an unconnected API.
- Why this is / is not agent-owned: holding the manager's maps and hard cap fixed without parent model decisions would not select appropriate parallel research scopes, react to different child results, or redirect current effort with task discretion.
- Whole-system current view: active session's primary task and each running, stopping or completed child investigation, identified assignments, last events/results and available capacity; not global company or other users' sessions.
- Current-control decision scope: assign independent evidence tasks, allocate up to three child work cells, stop obsolete work, restart with revised instructions, await and use outcomes to reprioritize current coding investigation.
- Evidence: [`src/agent/subagents/manager.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/manager.ts); [`src/agent/subagents/tools.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/tools.ts); [`src/tools/definitions/subagents.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/tools/definitions/subagents.ts); [`src/agent/runner.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/runner.ts); [`src/agent/turn/tool-execution/single-tool.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/tool-execution/single-tool.ts).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: credited only in enabled multi-investigation mode, not every default single-task execution. No free-standing automated watchdog, multiwriter fleet or parent-governed `(P)` mode asserted.

## S3* — Complementary audit

- State: —
- Function: no distinct built-in independent audit of execution outcomes with authoritative corrective return.
- Disturbance / variety regulated: wrong code, unjustified success claims, missed tests and inaccurate tool/evidence reports.
- Decisive decision or feedback right: the main task agent runs tools, interprets test results and verifies claims; optionally delegated read-only workers deliver research reports whose instructions explicitly say the parent verifies them, rather than an independent auditor passing judgment over an operational claim.
- Decision owner: primary agent for normal self-checking and report use; no materially distinct S3* owner established.
- Supporting / enforcement mechanisms: evidence governor, progress confirmation, terminal/test outputs, read-only context gatherers, post-task plan status and human scope approvals.
- Closure path: the original S1 interprets evidence and may continue; no separate reviewer opinion about completed S1 output is wired to corrective control independently of the originating task actor.
- Why this is / is not agent-owned: model-backed investigator children are real, but they are general delegated research operations; they do not automatically constitute the complementary audit function merely by reading files.
- Evidence: [`src/agent/subagents/worker.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/worker.ts); [`src/agent/subagents/tools.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/tools.ts); [`src/agent/evidence-governor.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/evidence-governor.ts); [`src/agent/task-evidence.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/task-evidence.ts); [`src/agent/runner.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/runner.ts).
- Basis: structural
- Confidence: medium
- Caveats: user could ask an investigator to review a specific patch; such an ad hoc task does not prove the shipped complementary audit/judgment/return path.

### Absence scope

- Surfaces inspected: main evidence/progress policy, success self-verification, read-only child mandates and reporting, parent report verification and task decision surfaces.
- Plausible first-party paths checked: separate source-grounded code reviewer, independent completion checker with defect/finding authority, reviewer disagreement rejection, and audit finding fed to repair/reassessment of completed operations.
- Why no material first-party path remains: the shipped subagents have no audit-specific mandate or independent corrective authority over completed task outcomes, and the current-run governor judges evidence in the same task actor's operational channel. No separate first-party reviewer closure is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed organization-level outside/future intelligence/option-development path beyond current task investigation and provider resilience.
- Disturbance / variety regulated: future environmental/tool changes or project direction might require capability adaptation, but the supported agent loop is goal/current-task oriented.
- Decisive decision or feedback right: agent can investigate present questions, user may switch providers/skills, system rotates keys when failing, and task history persists; none is a demonstrated future capability adoption decision.
- Decision owner: task-level model for tactical research, deterministic fallback for current provider failure, operator for tools/skills settings; no distinct S4 owner.
- Supporting / enforcement mechanisms: provider fallback/rotation, memory/compaction, workspace-context summaries, read-only investigations, skill discovery and existing-session continuation.
- Closure path: present facts or fallback errors change next *task* action/model selection, not a future/environmental adaptation option selected and returned to durable system capability or whole-current S3.
- Why this is / is not agent-owned: tactical research and resource recovery serve active S1 rather than shifting the organization's future strategy/capability.
- Evidence: [`src/agent/runner.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/runner.ts); [`src/agent/subagents/worker.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/subagents/worker.ts); [`src/agent/context-manager.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/context-manager.ts); [`src/agent/task-analyzer.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/task-analyzer.ts); [`README.md`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: no general claim that model-authored plugins or project skill improvements cannot ever supply S4 in an expanded environment.

### Absence scope

- Surfaces inspected: session persistence, task planning, evidence governor, context compaction, provider/model key switching, skill availability and subagent investigations.
- Plausible first-party paths checked: proactive external horizon sensing, organizational adaptation proposals, evaluation/selection of durable future skills and adoption by current management control.
- Why no material first-party path remains: available paths optimize the active task, preserve history or react to a current API outage; no shipped forward-looking capability-update control is closed at this first-party boundary.

## S5 — Policy and identity

- State: —
- Function: no legitimate decision/return channel for constitutional project identity, purpose or ultimate policy of the installed agent organization.
- Disturbance / variety regulated: unsafe shell actions, out-of-scope pentest targets, provider/payment preferences and consent to destructive tools are real operational constraints.
- Decisive decision or feedback right: operator specifies engagement scope and risk/approval limits; first-party controls enforce those limits on tool invocations rather than resolving organization-identity disputes.
- Decision owner: human user/config for scope/consent and deterministic runtime guards for validation; no first-party ultimate-policy S5 decision owner.
- Supporting / enforcement mechanisms: scope-based target allowlists/denylists, rate/concurrency caps, DNS/redirect checking, safe/confirm/block rules, cost/free-only configuration and user confirmation prompts.
- Closure path: tool action allowed/denied/confirmed changes its execution; no identity/policy issue escalates to a legitimate parent who settles purpose and returns an organization-wide governing decision.
- Why this is / is not agent-owned: the model may propose a task outside allowed scope, but cannot legitimately redefine the operator's ultimate constitutional rules through approval/tool output.
- Evidence: [`README.md`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/README.md); [`src/agent/session-policy.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/session-policy.ts); [`src/agent/turn/tool-execution/authorization.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/tool-execution/authorization.ts); [`src/agent/turn/tool-execution/gates.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/turn/tool-execution/gates.ts); [`src/agent/scope-context.ts`](https://github.com/pentoshi007/clai/blob/630d85f9eb7c2b5b3e499c503abf5834610c6939/src/agent/scope-context.ts).
- Basis: structural
- Confidence: medium-high
- Caveats: human engagement authorization exists but is not the Profile's S5 parent-governed identity closure.

### Absence scope

- Surfaces inspected: task/scope authorization, tool confirmation and destructive-action rules, session/user config, project instructions, provider/free-only preferences and source-side consent enforcement.
- Plausible first-party paths checked: legitimate parent adjudication of identity/ultimate mission dispute, return of binding changed policy into all subsequent operation and independent S3–S4 constitutional settlement.
- Why no material first-party path remains: the shipped controls apply predeclared operational security, payment and tool permissions, not an identity-level authority decision that returns as an ultimate governing rule.

## Distributed OSS parent arrangement

The public clai repository, maintainers, issue triage, releases, external providers and users are not one runtime-connected parent authority for an arbitrary installed clai session. Upstream OSS governance does not donate S5 or S3 to local sessions.

## Self-hosted and non-human modes

The shipped local CLI can use local Ollama or remote LLM providers with operator-entered credentials and run one-shot/headless work; resume and rate-limit fallback preserve sessions. Non-human operation changes how often tool permission is requested, not the ownership requirements of S3/S4/S5. Enabled read-only orchestration is the bounded positive S3 mode, not a general company-wide manager.

## Recursion

The parent model owns current tasks across up to three independent read-only investigator child model loops; children cannot recursively launch further agents. A nested call is operational decomposition, not proof that every child has a complete nested viable-system metasystem or persistent constitutional identity.

## Variety and escalation

Tool calls allow the model to absorb changing workspace variety. Read-only investigation increases information-processing variety; hard concurrency, safe-tool/scope rules, evidence governor and rate-limit fallback attenuate dangerous/budget variety. Escalation to a human for confirmation is authorization, not independently positive S5 or an algedonic S-function.

## Evidence gaps

- S3 is deliberately bounded to enabled model-owned multi-investigation control of the first-party current child roster, not to a global fleet or unattended worker reprioritization. A runtime performance/ownership demonstration was not performed.
- An exact duplicated-assignment pre-launch error is not a demonstrated inter-operating-S1 collision and return. Future evidence of first-party contradiction handling would require new same-ref source review, not inference from a concurrency cap.
- Source-first review of frozen code; no model-backed benchmark, live pentest or external-provider reliability experiment was performed.