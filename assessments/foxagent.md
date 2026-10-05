---
harness_id: foxagent
project_name: FoxAgent
repository: https://github.com/douzifox/foxagent
review_ref: 321f5eae7bd996b6b80502a50f3987f77f9a80cb
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# FoxAgent

## Review boundary

- System in focus: FoxAgent's first-party standalone terminal/headless coding-agent runtime and MCP wrapper at frozen revision `321f5eae7bd996b6b80502a50f3987f77f9a80cb`, including the model/tool loop, seven built-in coding tools, durable sessions, context compaction, project memory/work journal, token/iteration guardrails and MCP task/session transport.
- Purpose and identity: perform repository-oriented coding, exploration, review and mechanical editing through its own persistent model/tool session, either directly from the terminal or as a cheaper worker invoked by an external MCP client.
- Relevant environment: user/caller task, local repository/filesystem and Git state, configured OpenAI-compatible model endpoint, tool results/errors, session history, project/global memory, work journal, context/token limits and optional external MCP caller.
- Standard-distribution boundary: first-party TypeScript/Bun runtime under `src/`, compiled CLI, persistent `~/.foxagent/` data and MCP server are inside. Claude Code or any other MCP client, hosted/local model inference, host shell/processes and repository-development CI are dependencies/adjacent actors and do not donate VSM ownership.
- Credited operating / distribution surfaces: interactive CLI; non-interactive `-p`; model/tool execution loop; workspace-scoped read/edit/write/search/shell/ask tools; session save/resume; compaction; memory/journal injection; wrap-up; MCP submit/wait/check/status/reply/session surfaces and watchdog recovery.
- Adjacent first-party surfaces excluded from ownership: repository development/CI; documentation-only future possibilities; independently launched FoxAgent instances not coordinated by FoxAgent; external Claude Code or other MCP caller logic and any decisions/repair loops owned by those callers.
- First-party operating / deployment modes considered: direct interactive terminal use; one-shot/headless CLI; resumed sessions; compiled binary; MCP worker mode.
- Recursion level: one FoxAgent task/session producing repository work is the focal operation. External caller→FoxAgent delegation is a parent/adjacent composition, not a same-boundary first-party metasystem.
- Reviewed revision: `321f5eae7bd996b6b80502a50f3987f77f9a80cb`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

FoxAgent implements its own OpenAI-compatible model/tool loop. `runAgent` repeatedly compacts context if necessary, asks the configured model for text or tool calls, executes requested first-party tools, returns concrete tool output to the model and continues until the model finishes, the user interrupts, or an explicit token/iteration boundary is reached. The tools directly read/search/edit/write files and run commands within the workspace, with dangerous-command confirmation and path constraints.

Sessions are persisted under `~/.foxagent/` and can be resumed from CLI or MCP. The runtime also injects global instructions, a project-memory index and a work journal into new sessions. After tasks that encountered pitfalls, a bounded wrap-up model call may decide whether a lesson is worth storing in project memory.

The MCP server wraps the same first-party CLI/runtime as a long-running external-worker surface. It starts FoxAgent subprocess tasks, exposes state/result/question transport, keeps execution traces, detects silence with a watchdog and supports resuming a durable FoxAgent session after interruption. The caller remains external: the MCP server does not itself own the caller's portfolio, review acceptance or subsequent repair decisions.

Primary evidence:

- [README.md](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/README.md)
- [architecture](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/docs/architecture.md)
- [agent loop](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/agent.ts)
- [CLI/headless entry](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/cli.ts)
- [tool layer](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/tools.ts)
- [MCP server](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/mcp.ts)
- [prompt/memory injection](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/prompt.ts)
- [context compaction](https://github.com/douzifox/foxagent/blob/321f5eae7bd996b6b80502a50f3987f77f9a80cb/src/context.ts)

## Operational model

A direct FoxAgent task starts with the user/caller objective plus durable session/context state. The model chooses repository inspection or mutation actions, FoxAgent executes those tools, and the resulting evidence returns to the model for the next decision. Session persistence, compaction, retries, guardrails and the journal keep the operation bounded and recoverable without replacing the model's coding discretion.

In MCP mode an external client can dispatch FoxAgent as a second worker and later inspect or resume its result. FoxAgent deliberately preserves an isolated model context and may be used for code review, but the first-party FoxAgent boundary ends at the returned result/session. Any higher-level decision that the result audits, whether to accept it, and how another agent should correct work remains owned by the external composition unless separately wired first-party.

## S1 — Operations

- State: A
- Function: perform repository-oriented coding/review/exploration work by selecting tools, inspecting evidence, changing files or running commands and revising the task response from observed results.
- Disturbance / variety regulated: heterogeneous codebases/tasks, incomplete context, file/Git state, command failures, model-provider errors, tool errors, context pressure, token budgets and user/caller clarifications.
- Decisive decision or feedback right: choose what evidence/action to take next, what source change or conclusion to produce, how to respond to tool results and when the requested task is complete.
- Decision owner: the configured model-backed FoxAgent actor inside `runAgent`.
- Supporting / enforcement mechanisms: tool registry/executor; workspace/path safety; dangerous-command confirmation; streaming/retry layer; session persistence; compaction; token/iteration guardrails; CLI/MCP transports; watchdog.
- Closure path: task + persisted/current context → model selects tool/action → FoxAgent executes against repository/environment → concrete result/error returns to model → model revises action/answer until completion/interruption.
- Boundary reachability: the standard CLI and `-p` modes instantiate this loop directly; MCP mode launches the same first-party loop rather than delegating the work loop to an external coding agent.
- Why this is / is not agent-owned: if the model actor is removed while deterministic tools, persistence and limits remain, open-ended coding/review judgment about what to inspect/change and what outcome is sufficient disappears.
- Evidence: `src/agent.ts`; `src/cli.ts`; `src/tools.ts`; README; architecture.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is externally supplied, but FoxAgent owns the concrete actor/tool feedback organization around it.

## S2 — Coordination

- State: —
- Function: no material first-party coordination function among multiple same-recursion production S1 units was established.
- Disturbance / variety regulated: FoxAgent runs one focal agent loop per task/session; multiple MCP tasks or independently launched sessions are isolated jobs rather than mutually regulating peer operations.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: explicit session IDs, task IDs, per-task subprocess state and workspace/session separation.
- Closure path: no concrete peer-S1 interference → coordination response → changed peer behavior loop is implemented.
- Why this is / is not agent-owned: session/task separation prevents accidental state crossing but does not decide how multiple operational peers should mutually adjust.
- Evidence: README; `src/mcp.ts`; `src/session.ts`; architecture.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external Claude/Fox delegation and concurrent MCP tasks do not establish first-party S2 at the FoxAgent boundary.

### Absence scope

- Surfaces inspected: direct agent loop; session storage/resume; MCP task table; task/session IDs; watchdog; CLI/headless modes; README's caller integration model.
- Plausible first-party paths checked: parallel MCP tasks as peer workers; session isolation as coordination; caller→Fox delegation; task queue/wait/status mechanisms.
- Why no material first-party path remains: the implementation isolates and reports separate jobs but contains no first-party relation that detects/attenuates a specific inter-worker conflict and feeds the result back into subsequent peer behavior.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function over a portfolio of operational S1 units/resources was established.
- Disturbance / variety regulated: token/iteration limits, retries, compaction, task state and watchdog handling regulate individual tasks rather than current performance/resources of the whole.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: token guardrail; max iterations; MCP task state; wait/check/status; watchdog; interrupt/resume; configuration.
- Closure path: the mechanisms constrain/recover individual executions but do not exercise a whole-current priority/resource/commitment/accountability decision across operations.
- Why this is / is not agent-owned: deterministic runtime machinery can stop, retry, compact or expose status without owning a whole-system managerial choice.
- Evidence: `src/agent.ts`; `src/mcp.ts`; `src/context.ts`; architecture.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an external MCP client may use FoxAgent status in a larger S3 loop, but that parent control is outside the first-party boundary.

### Absence scope

- Surfaces inspected: token/iteration guardrails; task table; status/check/wait; watchdog; session lifecycle; retry/compaction; caller instructions.
- Plausible first-party paths checked: MCP task table as whole-system view; watchdog as manager; budget limits as resource control; caller-facing status as current control.
- Why no material first-party path remains: observed mechanisms enforce/report preselected limits on independent tasks and expose data to an external caller; they do not close a first-party whole-current decision over an operational portfolio.

## S3* — Complementary audit

- State: —
- Function: no closed first-party complementary audit path over FoxAgent's own operational claims was established.
- Disturbance / variety regulated: FoxAgent can itself be asked to review another agent's code and is intentionally useful as a clean-context second opinion, but the claim under audit and corrective return path belong to an external caller/composition.
- Decisive decision or feedback right: no first-party FoxAgent audit authority over a separate FoxAgent production claim is established.
- Decision owner: not established at the assessed boundary.
- Supporting / enforcement mechanisms: clean/resumable FoxAgent session; alternate model choice; code-reading/search/shell tools; structured MCP result/session ID.
- Closure path: FoxAgent may return a review result to an external MCP client, but no first-party path decides how that result changes the audited producer and then verifies the correction.
- Why this is / is not agent-owned: the model may make a substantive code-review judgment as S1 work, but S3* requires a complementary organizational audit relation, not merely that an operation performs review.
- Evidence: README; `src/agent.ts`; `src/mcp.ts`; `src/tools.ts`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: in a larger Claude+Fox composition FoxAgent may serve as an independent audit actor; that external system is not the declared first-party FoxAgent boundary.
- Claim being audited: no first-party internal claim/audited producer relation established.
- Ordinary reporting path: FoxAgent's own task result/session summary.
- Complementary access path: none first-party over a distinct FoxAgent producer claim.
- Independence boundary: isolated model/session can support independence for an external composition, but the audited producer and corrective authority are external.
- Who acts on findings: external caller/user, not a first-party FoxAgent correction loop.

### Absence scope

- Surfaces inspected: README second-opinion design; direct/headless loop; MCP submit/result/session transport; tools; session isolation and resumability.
- Plausible first-party paths checked: code-review task as audit; alternate model as independent auditor; MCP structured result as audit closure; wrap-up review of pitfalls.
- Why no material first-party path remains: review is an operational task FoxAgent performs for an external principal; first-party code does not establish a distinct audited producer, audit authority and corrective return/re-audit loop.

## S4 — Intelligence / adaptation

- State: —
- Function: no material externally and prospectively oriented adaptation loop was established.
- Disturbance / variety regulated: durable project memory, work journal, context compaction and the post-task pitfall wrap-up preserve/reuse experience and current project context.
- Decisive decision or feedback right: not established at S4 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: global instructions; project memory/index; automatic journal; model-driven pitfall wrap-up; session persistence; context compaction.
- Closure path: retained lessons/context can affect future turns, but no environmental/future sensing → developed adaptation options → selected change to present capability loop was established.
- Why this is / is not agent-owned: the wrap-up model can decide whether a task lesson is worth remembering, but memory consolidation from internal task history is not by itself the Profile's outside-and-then intelligence function.
- Evidence: README Memory/Work journal/Wrap-up sections; `src/prompt.ts`; `src/agent.ts`; architecture.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project memory can improve later work, but the inspected path does not model external future change or develop adaptation options in conversation with a whole-current S3 capability.

### Absence scope

- Surfaces inspected: project/global memory; journal; wrap-up prompt; new-session injection; compaction; model/provider configuration; MCP task recovery.
- Plausible first-party paths checked: pitfall learning as S4; journal as environmental model; project memory as persistent adaptation; model-window/config switching as strategy adaptation.
- Why no material first-party path remains: these mechanisms preserve or consolidate task experience/configuration without a closed external/future sensing and capability-adaptation relation.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure was established.
- Disturbance / variety regulated: system prompts, global user instructions, safety rules, path constraints, command confirmations and token limits bound how tasks execute.
- Decisive decision or feedback right: no qualifying identity/ultimate-policy issue is resolved by an ultimate authority through a first-party return path.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: default/custom system prompt; `FOXAGENT.md`; tool safety policy; configuration/env; user confirmation for dangerous commands; static MCP usage instructions.
- Closure path: configuration/prompt/user constraints are applied to operation, but no identity-policy proposal/conflict → legitimate authority decision → returned governance loop is implemented.
- Why this is / is not agent-owned: the model works inside user/developer-defined operating constraints and can edit memory, but it does not own FoxAgent's identity or ultimate policy.
- Evidence: README; `src/prompt.ts`; `src/tools.ts`; configuration/CLI surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a caller or user can impose standing instructions, but ordinary configuration/approval is not S5.

### Absence scope

- Surfaces inspected: default/custom system prompts; global instructions; project memory; command confirmation; config/env; MCP server instructions; safety/path rules.
- Plausible first-party paths checked: user/global instructions as parent governance; dangerous-command approval as ultimate authority; editable project memory as durable policy; system-prompt override as identity adaptation.
- Why no material first-party path remains: these are standing constraints/configuration or ordinary task approvals, not a closed identity/ultimate-policy decision relation.

## Recursion

The focal recursion is one FoxAgent task/session operating on one project. MCP creates a transport/delegation relation to an external parent client; task/session IDs and subprocesses do not establish recursive viability or a first-party metasystem above several FoxAgent operations.

## Variety and escalation

FoxAgent attenuates operational variety through direct repository tools, retries, context compaction, durable sessions, project memory/journal, token/iteration bounds, dangerous-command confirmation, MCP state reporting and watchdog termination/resume guidance. Questions and risky commands may escalate to the user/caller, but those ordinary task decisions are not promoted to S3/S4/S5.

## Evidence gaps

No `?` state is required. The pinned implementation directly establishes autonomous S1 and provides broad first-party evidence that its persistence, MCP control surfaces, second-opinion use, memory and safety mechanisms do not close S2/S3/S3*/S4/S5 within the declared FoxAgent boundary.

## Assessment summary

FoxAgent closes autonomous S1 through its own persistent model/tool coding loop. Its isolated sessions and MCP worker interface can support a larger external organization, including second-opinion review, but the caller-owned coordination/current-control/audit closure is outside FoxAgent's first-party boundary. Durable memory/journal and safety/configuration machinery likewise do not by themselves establish S4 or S5.

**Vector:** A · — · — · — · — · —
