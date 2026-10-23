---
harness_id: glm-code
project_name: GLM Code
repository: https://github.com/MikuBlog/glm-code
review_ref: 77049c2e3c3b76b293445fbac6b536bf330bbcd9
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

# GLM Code

## Review boundary

- System in focus: the first-party TypeScript GLM Code terminal coding-agent distribution in `MikuBlog/glm-code` at pinned revision `77049c2e3c3b76b293445fbac6b536bf330bbcd9`, including interactive, non-TTY, and `-p` headless operation.
- Purpose and identity: autonomously choose, execute, observe, and revise project coding and inspection actions using a model/tool conversation in a local working directory.
- Relevant environment: user coding request, repository files, shell/test results, local process state, command approvals, provider responses, fetched web content, project instructions, and session context.
- Standard-distribution boundary: the shipped `bin/glm-code.ts` / `src/index.ts` entry, `Agent` loop and registered built-in tools, permission and session machinery, local UI/commands, and optional first-party MCP transport. The remote GLM model/provider, installed external MCP servers, target project's organization, user/editor, and host shell commands are outside independent GLM Code ownership.
- Credited operating / distribution surfaces: `src/index.ts`, `src/agent.ts`, `src/client.ts`, `src/tools/index.ts` and registered tools, `src/permissions.ts`, `src/commands.ts`, `src/session.ts`, `src/memory.ts`, `src/compaction.ts`, `src/tui.ts`, `src/config.ts`, and first-party `src/mcp.ts` registration.
- Adjacent first-party surfaces excluded from ownership: `test/smoke.ts` mock-provider test harness, project build/package/release scripts and `dist` packaging, README claims not reachable in source, repository contributor/maintainer decisions, and downstream files changed by the coding agent. They corroborate or define distribution but are not independent runtime decision owners.
- First-party operating / deployment modes considered: ordinary interactive `glm-code`, headless `-p`, piped input, resumed sessions, default/acceptEdits/plan/auto/bypass permissions, direct user `!bash`, `/init`, `/compact`, and configurable external MCP tools. Advertised `Task`/subagent mode was explicitly checked for runtime reachability.
- Recursion level: one running GLM Code coding-agent session. Registered Bash background jobs are host processes, not independent model-backed S1 cells; no reachable first-party `Task` tool creates a subordinate agent in this frozen distribution.
- Reviewed revision: `77049c2e3c3b76b293445fbac6b536bf330bbcd9`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`src/index.ts` instantiates one `Agent` with a provider client, user-selected permissions, local project instructions, session journal and optional MCP tools. `Agent.continueTurn` repeatedly sends tool definitions to the model, accepts model-selected calls, executes those calls after authorization, appends tool outputs, and chooses the next turn until completion or an iteration cap. Built-in file/read/edit/search, bash/background-task, todos and web tools are registered in `src/tools/index.ts`; `src/mcp.ts` exposes separately installed MCP tools as `mcp__*` names. User `/plan`, `/init`, session resume, input queue, tool confirmation and compaction operate around that one live model/tool loop.

There is a consequential difference between source capability and README features. `src/agent.ts` contains `runSubagent`, but `Agent.availableTools()` offers only `coreTools` plus external MCP tools, and the registered `coreTools` omit `Task`. `executeToolCall` first rejects any name missing from the offered list, **before** its special `Task` branch. Thus the shipped standard model-facing tool registry cannot invoke the nominal first-party subagent path. A pinned-source deterministic registry probe printed `Task advertised: false`; no LLM call was used.

Other control surfaces remain task-local: `TodoWrite` updates this session's plan list, `KillTask` terminates a known Bash process, the user approves a proposed plan/command or changes a mode, and automatic compaction summarizes current conversation history. None alone establishes a whole-current multi-S1 metasystem, complementary audit, prospective external adaptation, or ultimate-policy governance.

Primary source:

- [`src/agent.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/agent.ts)
- [`src/tools/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/index.ts)
- [`src/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/index.ts)
- [`src/permissions.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/permissions.ts)
- [`src/commands.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/commands.ts)

## Operational model

The reachable ordinary S1 is a single model-guided coding process, using tool feedback to select new edits, inspections, tests or stopping. Permissions, plan approval, queued user input, session persistence, budgets and tool caps constrain or support that process. Although the source has an unregistered child-agent implementation, it cannot be counted as a standard deployed second S1. Other hypothetical model-serving clients, user-installed MCP implementations and target-project reviewers cannot donate functions to this declared boundary.

## S1 — Operations

- State: A
- Function: convert coding goals and observed repository/tool feedback into successive task-specific actions and outputs.
- Disturbance / variety regulated: unknown source structure, changing coding requests, failing commands/tests, errors, permissions and information gaps.
- Decisive decision or feedback right: the model selects read/search/edit/shell/web calls and revises subsequent steps based on returned results.
- Decision owner: the model-backed `Agent` loop, with human authorization of risky tool calls when configured; the provider supplies inference but does not substitute an externally operated agent harness.
- Supporting / enforcement mechanisms: `GLMClient.complete`, typed tool registry, permissions, session journal, plan mode, compaction, iteration cap, UI and MCP transport.
- Closure path: user/project context → model receives tool definitions → selects tool → `executeToolCall` checks authorization and runs first-party handler → result rejoins `messages` → next model decision or final answer.
- Boundary reachability: interactive CLI and `-p` both construct `Agent` and call `runTurn`/`runOneShot` on the shipped `src/agent.ts` loop; the smoke suite exercises a mock-provider tool-result turn.
- Why this is / is not agent-owned: deterministic dispatch and permissions do not decide arbitrary next coding steps after novel results; the model's ongoing choice closes the operational regulation.
- Evidence: [`src/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/index.ts); [`src/agent.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/agent.ts); [`src/tools/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/index.ts); [`test/smoke.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/test/smoke.ts).
- Basis: explicit + structural + deterministic mock-provider test.
- Confidence: high.
- Caveats: no live GLM/LLM provider or open-ended agent effectiveness trial was performed; `npm test` passed 40 first-party local smoke checks.

## S2 — Coordination

- State: —
- Function: no reachable function-specific damping of interference among multiple independent GLM Code S1 units was established.
- Disturbance / variety regulated: hypothetical simultaneous model-backed child edits or commitments are not present as a shipped multi-S1 operating population.
- Decisive decision or feedback right: none evidenced for actual distinct first-party S1 conflicts.
- Decision owner: not established; one model loop controls ordinary tools.
- Supporting / enforcement mechanisms: sequential tool-call loop, a session todo list, background Bash task IDs/output, and dormant subagent implementation.
- Closure path: no multi-S1 conflict → coordination decision → returned child correction path is wired into a supported model-visible mode.
- Why this is / is not agent-owned: task lists and ordered tool calls regulate one S1's execution, not interaction among independent S1s.
- Evidence: [`src/tools/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/index.ts); [`src/agent.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/agent.ts); [`src/tools/bash.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/bash.ts); [`src/tools/todo.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/todo.ts).
- Basis: structural + negative register/reachability check.
- Confidence: high at frozen distribution.
- Caveats: `runSubagent` exists in source, but registration and pre-dispatch reachability fail; an external MCP server could implement coordination outside this boundary.

### Absence scope

- Surfaces inspected: first-party tool registry, `Agent.availableTools`/`executeToolCall`/`runSubagent`, core loop, Bash background task handlers, session/todos, entrypoint and README.
- Plausible first-party paths checked: `Task` child agent as distinct S1, multiple simultaneous tool calls, shell jobs as putative S1s, todo/approval coordination, and external MCP delegation.
- Why no material first-party path remains: `Task` is not registered and is rejected before the special handler; core tool calls execute sequentially, while shell jobs have no independent model/coding decision loop. No supported multi-S1 interference-specific attenuation and return is shipped.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-current management of a population of independent operational S1 units is established.
- Disturbance / variety regulated: per-task context, permissions, background process state and user prompts are handled locally, not as a shared organizational commitment portfolio.
- Decisive decision or feedback right: no whole-population resource/commitment supervisory right is exposed.
- Decision owner: user owns isolated plan/tool/kill choices; the agent chooses local task steps, not a whole-system control decision.
- Supporting / enforcement mechanisms: `TodoWrite`, `KillTask`, `/bashes`, UI interruption, `ExitPlanMode`, permission rules and deterministic iteration cap.
- Closure path: local plan approval or Bash termination returns to the same S1's operation, but there is no whole-current subordinate S1 view → portfolio intervention → returned cross-unit regulation.
- Why this is / is not agent-owned: selecting next tools in one task is S1, and generic human plan approval is not a parent-governed S3 mode.
- Evidence: [`src/agent.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/agent.ts); [`src/commands.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/commands.ts); [`src/tools/bash.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/bash.ts).
- Basis: structural absence review.
- Confidence: high at declared single-session recursion.
- Caveats: a future reachable multiagent control mode would require fresh review; the disabled `Task` source alone is not a positive constructor.

### Absence scope

- Surfaces inspected: CLI/TUI modes, primary loop, dormant child path, todo/plan commands, session history and Bash lifecycle controls.
- Plausible first-party paths checked: agent fleet/current board, autonomous manager, attended operator control of multiple S1s, task-priority/todo control, current cancellation of host jobs.
- Why no material first-party path remains: there is one supported model-backed S1 with no registered subordinate model population; human prompt/plan approval and host-job termination lack a whole-current organizational S3 decision and return.

## S3* — Complementary audit

- State: —
- Function: no installed sufficiently separate evidence-gathering audit path of S1/current-control claims with returned corrective judgment is established.
- Disturbance / variety regulated: coding errors can be found by ordinary model reinspection or project tests, but these are normal production feedback.
- Decisive decision or feedback right: no independent audit owner with a separately triggered evidence route and corrective return is shipped.
- Decision owner: ordinary main agent and user's local/project test commands, not a distinct first-party S3* actor.
- Supporting / enforcement mechanisms: Read/Grep/Bash/test tools, mock-provider smoke suite, direct user inspection, and unregistered generic child code.
- Closure path: production test/log output can inform the same coding turn; no complementary audit-specific reviewer finding → responsible management correction path is packaged.
- Why this is / is not agent-owned: one model verifying its own task or running ordinary tests does not establish independent complementary audit of operational reality.
- Evidence: [`src/agent.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/agent.ts); [`src/tools/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/index.ts); [`test/smoke.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/test/smoke.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: externally designed MCP auditor or a hypothetical future reviewer persona is not first-party shipped audit evidence.

### Absence scope

- Surfaces inspected: entire small first-party `src` tree, agent/tool registry, tool verification paths, sessions/UI, and test-only suite.
- Plausible first-party paths checked: second model/reviewer child, separate audit command or evidence path, CI/test runner, model self-review and operator check.
- Why no material first-party path remains: shipped registry has no reviewer/audit tool or active `Task`, tests are adjacent development machinery, and ordinary self-checks do not provide complementary independent reality access and returned audit judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed external-and-prospective capability adaptation loop is established in standard operation.
- Disturbance / variety regulated: present project documentation, fetched web content and context limitations are consumed for current coding; future environment change is not modeled into selected adaptation options.
- Decisive decision or feedback right: none specific to choosing future capability changes from evolving external distinctions.
- Decision owner: user initiates `/init`, current agent writes project context, deterministic compaction summarizes history; no separate S4 decision right is wired.
- Supporting / enforcement mechanisms: `AGENT.md`/`CLAUDE.md` loading, `/init`, `/compact`, `WebFetch`, model settings, session resume and history.
- Closure path: `/init` may create static project guidance for later sessions, and compaction can preserve this task's context; neither implements external/future environment sensing → prospective alternatives → selected capability adaptation → closed return to current S3/capability.
- Why this is / is not agent-owned: a model writing initial project notes is an operational task output; persistence and summarization alone do not own strategic adaptation.
- Evidence: [`src/commands.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/commands.ts); [`src/memory.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/memory.ts); [`src/compaction.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/compaction.ts); [`src/tools/webfetch.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/tools/webfetch.ts).
- Basis: structural + explicit negative.
- Confidence: medium-high.
- Caveats: project notes can help later work, but future reuse alone is not S4; no live cross-session effectiveness was tested.

### Absence scope

- Surfaces inspected: `/init` implementation, memory file reader, `/compact` and automatic compaction, `WebFetch`, model/provider switching, settings, todos and source's optional modes.
- Plausible first-party paths checked: proactive external scanning, recurring-environment skill revisions, model-evaluated future strategic alternatives, project memory as durable adaptation, and operator-chosen prospective capability changes.
- Why no material first-party path remains: shipped `/init` requests a one-time summary of the current codebase, memory is loaded as static prompt context, and external fetch/compaction serve present tasks; no prospective capability-selection loop with a returned S3/capability change exists.

## S5 — Policy and identity

- State: —
- Function: no legitimate first-party ultimate identity/policy deliberation and authoritative return circuit is established at the assessed one-session organization.
- Disturbance / variety regulated: unsafe tool requests and untrusted projects are controlled through supplied rules and approvals, not a system-level purpose or identity decision.
- Decisive decision or feedback right: no explicit ultimate-policy matter and final legitimate organizational decision path is implemented.
- Decision owner: user supplies goals, project trust and tool settings; permissions engine enforces those settings.
- Supporting / enforcement mechanisms: project-trust prompt, deny/allow rules, plan approval, bypass/default modes, command permissions, env-scoped provider credentials and `AGENT.md` instructions.
- Closure path: user configuration/approval → deterministic runtime allowance/denial affects the current tool; no ultimate identity-policy issue → authority → authoritative resolution → durable governed return at this recursion.
- Why this is / is not agent-owned: removing the model does not remove rule enforcement, and the remaining user choices are operational access controls rather than a shipped legitimate S5 governance loop.
- Evidence: [`src/permissions.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/permissions.ts); [`src/index.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/index.ts); [`src/config.ts`](https://github.com/MikuBlog/glm-code/blob/77049c2e3c3b76b293445fbac6b536bf330bbcd9/src/config.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: actual human project owner/maintainer authority exists outside this runtime system-in-focus.

### Absence scope

- Surfaces inspected: `src/config.ts` settings, `src/permissions.ts`, trust handshake in `src/index.ts`, user plans, memory files, provider/credential settings and repository governance adjacency.
- Plausible first-party paths checked: identity-level model self-governance, authoritative parent S5 escalation/return, project trust and standing permissions as policy, user-driven mode changes, and developer/maintainer external rules.
- Why no material first-party path remains: the reachable standard distribution supplies task-level access enforcement and fixed owner settings but no S5-specific issue, legitimate ultimate-policy decision procedure, or governed return-to-operation beyond those constraints.

## Recursion

One model/tool S1 is established. Source text for `runSubagent` hints at an intended lower-level child loop, but no first-party advertised `Task` tool reaches that path at the frozen ref. Background Bash programs and externally configured MCP servers are not automatically GLM Code-owned S1 recursions.

## Variety and escalation

Coding variety is amplified by the model-selected file/search/Bash/web tools and optional external MCP APIs; permission rules, plan mode, process timeouts, token compaction, 80-iteration bound and user cancellation attenuate operational risk. The normal exception path returns tool errors or approval denials to the same S1. No established higher-level S2–S5 decisive owner is inferred from those mechanisms.

## Evidence gaps

- Source level versus advertisement: README names `Task` (subagent) as a tool. The pinned `coreTools` registry does not contain it, and `executeToolCall` refuses unknown tool names before reaching `runSubagent`; this is a deterministic **reachability failure** in the reviewed version, not a claim about later fixes.
- The local `npm test` suite passed 40 checks, including mock SSE/model-tool rounds, after rerunning outside the restricted network-socket sandbox. It does not measure LLM-agent effectiveness, production permissions, or real provider results.
- All `—` states are bounded to the inspected first-party installed modes, not a proof that users cannot compose adjacent services to add higher functions.

## Assessment summary

The frozen GLM Code distribution closes an autonomous model/tool coding operation (`S1=A`). Its claimed native subagent path is unregistered in the advertised tool set, and neither background shell jobs nor task-level permission/plan/session controls establish a higher organizational function. No bounded first-party S2, S3, complementary S3*, external/prospective S4, or legitimate S5 loop was found in the supported modes.

Proposed vector: **`A · — · — · — · — · —`**
