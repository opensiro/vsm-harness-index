---
harness_id: codey
project_name: Codey
repository: https://github.com/codesbyjit/codey
review_ref: b1cad86d649263a5b87be782cf4ee28c8916dff5
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Codey

## Review boundary

- System in focus: the first-party Codey Rust terminal coding-agent runtime at frozen revision `b1cad86d649263a5b87be782cf4ee28c8916dff5`, including its model/tool loop, built-in coding tools, permissions, sessions/context/instructions/skills, and specialized subagent delegation.
- Purpose and identity: understand, edit, test and otherwise change code in a selected workspace by letting a model choose repository actions, observe tool results, delegate bounded specialist work and return a final answer.
- Relevant environment: user tasks, the selected workspace and source/build/test state, model/provider responses, shell/filesystem outcomes, project instructions/skills, persistent sessions and operator permission decisions.
- Standard-distribution boundary: `run_agent`, built-in tool registry, first-party filesystem/search/shell tools, sessions/context, AGENTS.md/skill discovery, TUI/headless entry points and built-in explorer/coder/reviewer/tester subagents are inside. External model providers and MCP servers are dependencies. Repository-development docs/tests are corroborating evidence only unless wired into runtime.
- Credited operating / distribution surfaces: `README.md`; `src/agent/loop_.rs`; `src/agent/subagent.rs`; `src/agent/session.rs`; `src/agent/context.rs`; `src/agent/instructions.rs`; `src/agent/skills.rs`; `src/tools/*`; `src/main.rs`; `src/tui/*`.
- Adjacent first-party surfaces excluded from ownership: repository unit tests, contributor instructions, design notes under `docs/superpowers/specs`, development commands and the unwired MCP transport scaffold. They may document intended behavior but do not own runtime VSM functions.
- First-party operating / deployment modes considered: interactive TUI and one-shot headless task execution; confirmation modes; persistent sessions; discovered AGENTS.md/skills; direct tools; and built-in specialist subagent delegation.
- Recursion level: one Codey coding session/task around one selected workspace is the assessed organization. The main coding actor is the primary S1. Specialized subagents are bounded subordinate agent actors; the reviewer supplies a complementary audit path, while delegation itself does not establish a multi-S1 coordination layer.
- Reviewed revision: `b1cad86d649263a5b87be782cf4ee28c8916dff5`.
- Observation date: 2026-10-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Codey's central `run_agent` loop repeatedly streams a model completion, parses either a final answer or one tool call, executes the selected first-party tool or delegate path, writes the result back into session context, and asks the model again. The loop is bounded by maximum iterations and provider retry behavior. TUI and headless modes instantiate the same core.

The built-in registry gives the main model workspace file/search/edit/write and shell capabilities. Risky operations may request operator confirmation in the interactive TUI; headless mode does not provide the prompt path. Sessions persist model/tool history to disk, and context management truncates older assistant/tool entries as budget pressure rises.

Codey also packages four specialist subagents. Explorer and reviewer are read-only; coder can edit/write; tester can run commands. The parent model chooses `delegate_subagent`, the selected child gets a fresh session and role-specific system prompt plus a strict allowed-tool list, and its final report is returned into the parent session as a tool result. Delegation is awaited rather than a standing parallel worker organization.

The reviewer path is materially different from ordinary production reporting. It runs in a separate agent context, has a dedicated review persona, cannot mutate the workspace, directly inspects code through read/search tools, and returns prioritized bug/security/style findings to the parent. Those findings re-enter the ordinary parent loop and can change subsequent coding actions, establishing a complementary audit-and-correction path.

Primary evidence:

- [README.md](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/README.md)
- [src/agent/loop_.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/loop_.rs)
- [src/agent/subagent.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/subagent.rs)
- [src/agent/instructions.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/instructions.rs)
- [src/tools/shell.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/tools/shell.rs)
- [src/main.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/main.rs)

## Operational model

A task enters the main Codey session, the model chooses one repository/tool/delegation action, the runtime checks any interactive confirmation requirement, executes the call and returns the result into the same conversation. The model then decides the next action. When it delegates to `reviewer`, a separate read-only agent inspects workspace evidence and returns an audit report; that report becomes parent tool evidence for later corrective action.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by selecting code/search/edit/test actions, observing results and iterating toward the user-requested outcome.
- Disturbance / variety regulated: heterogeneous repository state, implementation ambiguity, search evidence, edit/build/test outcomes, provider failures, context pressure and tool errors.
- Decisive decision or feedback right: choose the next task-specific action/tool and interpret returned evidence to continue or finish the task.
- Decision owner: the model-backed main Codey agent.
- Supporting / enforcement mechanisms: tool registry/schema, confirmation prompts, iteration limits, retries, workspace path handling, session persistence, context-budget truncation and TUI/headless event plumbing.
- Closure path: user task/current context → model selects action → runtime/tool execution → result returns into session → model revises subsequent action or produces the final answer.
- Boundary reachability: both interactive TUI and one-shot headless operation invoke the same first-party `run_agent` loop and built-in tools; no external coding-agent runtime is required.
- Why this is / is not agent-owned: removing the model actor while retaining tools, sessions and confirmations leaves execution primitives but removes the open-ended task-specific choice and sequencing that performs the coding work.
- Evidence: [src/agent/loop_.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/loop_.rs); [src/main.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/main.rs); [README.md](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: operator confirmation may gate risky interactive actions, but that enforcement does not replace the agent's operational choice.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established because the reviewed runtime does not expose a specific interference/conflict/oscillation among coexisting operational S1 units plus an attenuation relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: delegated specialist roles, allowed-tool lists, maximum subagent count/depth and parent-child handoff.
- Closure path: not applicable; no inter-S1 disturbance → coordination response → changed later S1 behavior loop was found.
- Why this is / is not agent-owned: delegation assigns one bounded specialist task and waits for its report. Even the writable coder role does not create a standing concurrently mutating worker population whose interference is regulated.
- Evidence: [src/agent/subagent.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/subagent.rs); [src/agent/loop_.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/loop_.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: `MAX_SUBAGENTS` is a concurrency safety bound, but the standard parent loop exposes one delegate tool call at a time and supplies no S2-specific interference witness.

### Absence scope

- Surfaces inspected: parent agent loop; built-in explorer/coder/reviewer/tester definitions; delegate execution; tool restrictions; subagent depth/count controls; sessions and workspace tools.
- Plausible first-party paths checked: concurrent writable subagents, workspace collision control, reviewer/coder mutual adjustment, tester/coder scheduling and shared-state coordination.
- Why no material first-party path remains: located mechanisms implement bounded delegation and role restrictions, not regulation of a concrete disturbance among multiple interacting S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current organizational control function distinct from task execution and bounded delegation was established.
- Disturbance / variety regulated: not established at S3 level; the runtime manages one session and one delegated specialist invocation rather than commitments/resources across an operational population.
- Decisive decision or feedback right: not established. The main model may choose which specialist to invoke, but that is task decomposition rather than whole-system resource/priority control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: subagent count/depth caps, per-role tool allowlists, context budget, confirmation mode, session switching and cancellation.
- Closure path: not applicable; no whole-system current view → resource/commitment/prioritization decision → organization-wide operational change loop was found.
- Why this is / is not agent-owned: the main model remains the S1 task actor; choosing a helper does not create a distinct current-control metasystem.
- Evidence: [src/agent/loop_.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/loop_.rs); [src/agent/subagent.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/subagent.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: names such as coder/reviewer/tester can resemble an organization chart, but no whole-current authority over multiple live operations is wired.

### Absence scope

- Surfaces inspected: parent/delegate loop; specialist definitions; session/context handling; confirmation modes; TUI event/control path; tool registry.
- Plausible first-party paths checked: parent agent as manager, subagent portfolio control, concurrency/resource budgeting, session manager as S3 and tester/reviewer intervention.
- Why no material first-party path remains: these mechanisms remain local task orchestration, deterministic bounds or audit support rather than whole-system current regulation.

## S3* — Complementary audit

- State: A
- Function: provide a complementary read-only inspection of operational code/change state that can challenge the ordinary coding actor's implicit correctness/style/security claims.
- Disturbance / variety regulated: bugs, security issues, style defects or other discrepancies that the producing coding path may miss or misreport.
- Decisive decision or feedback right: the reviewer agent independently judges inspected code and produces prioritized findings grounded in direct workspace reads/searches; the parent agent then receives those findings as tool evidence for corrective action.
- Decision owner: the autonomous reviewer subagent owns the audit judgment; the parent autonomous agent owns whether/how to act on returned findings.
- Supporting / enforcement mechanisms: separate fresh subagent session, reviewer-specific persona, strict read/search-only tool allowlist, delegate plumbing and parent tool-result insertion.
- Closure path: main operation/code state → parent selects reviewer audit → separate read-only reviewer directly inspects workspace → reviewer findings return as delegate tool result → parent loop continues with the findings available to change subsequent edits/actions.
- Boundary reachability: `reviewer` is a built-in first-party subagent exposed through the ordinary `delegate_subagent` tool available to the top-level Codey agent in supported runtime modes.
- Why this is / is not agent-owned: removing the reviewer model while retaining delegation/tool restrictions leaves no audit judgment; the runtime only constrains access and transports the report.
- Evidence: [src/agent/subagent.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/subagent.rs); [src/agent/loop_.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/loop_.rs); [README.md](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the reviewer can use the same underlying provider/model family as the main actor and invocation is discretionary rather than mandatory. Independence is nevertheless materially improved by a separate context/persona plus read-only direct workspace access, and its findings return through a distinct audit path.
- Claim being audited: the main coding actor's implicit claim that the inspected code/change is correct, safe and stylistically acceptable for the requested task.
- Ordinary reporting path: the producing main Codey agent sees its own tool results and may run ordinary tests or reads while performing the task.
- Complementary access path: a separately instantiated `reviewer` subagent receives a focused audit task, directly reads/searches the workspace under a read-only allowlist, and returns a prioritized independent findings report.
- Independence boundary: reviewer execution uses a fresh `Session`, reviewer-specific persona and non-mutating tool boundary; it does not inherit the parent's conversation or edit authority, although it may use the same configured provider/model family.
- Who acts on findings: the parent autonomous Codey agent receives the reviewer report as the `delegate_subagent` tool result and owns subsequent corrective edits, tests or follow-up actions.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established; skills, model/provider selection and repository exploration support current tasks rather than future-oriented capability adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: skills discovery/selection, provider abstraction, model configuration, repository instructions and persistent sessions.
- Closure path: not applicable; no external/future sensing → adaptation option → adopted change to current organizational capability loop was found.
- Why this is / is not agent-owned: dynamic task context can change what the current S1 does, but no agent-owned process updates Codey's future capabilities or strategy based on prospective environmental distinctions.
- Evidence: [src/agent/skills.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/skills.rs); [src/config/mod.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/config/mod.rs); [README.md](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: provider abstraction and extensibility make adaptation possible for developers/operators, but generic extensibility is not a closed S4 constructor.

### Absence scope

- Surfaces inspected: skills/instruction discovery; provider/configuration layer; sessions/context; subagents; design docs; MCP scaffold.
- Plausible first-party paths checked: autonomous model/provider switching, skill acquisition, self-improvement, external trend sensing, future planning and reviewer/tester-driven capability change.
- Why no material first-party path remains: changes to durable capability/configuration remain external developer/operator work; runtime sensing is directed at the current task.

## S5 — Identity and ultimate policy

- State: —
- Function: no material identity/ultimate-policy decision-and-return function was established at the selected recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. AGENTS.md, skills, confirmation mode, workspace/provider/model configuration and specialist personas constrain operation but do not form an identity-level issue-resolution loop.
- Decision owner: not established.
- Supporting / enforcement mechanisms: discovered AGENTS.md files, system prompt/personas, config, permission confirmation, provider/model selection and role-specific subagent allowlists.
- Closure path: not applicable; no identity/ultimate-policy issue → legitimate authority decision → returned governance of subsequent organization path was found.
- Why this is / is not agent-owned: policy/context text is injected into prompts and configuration, but the runtime exposes no ultimate-policy deliberation or legitimate identity authority path.
- Evidence: [src/agent/instructions.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/instructions.rs); [src/config/mod.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/config/mod.rs); [src/agent/subagent.rs](https://github.com/codesbyjit/codey/blob/b1cad86d649263a5b87be782cf4ee28c8916dff5/src/agent/subagent.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: durable repository instructions may encode important standing policy, but the Profile explicitly rejects prompt/policy text alone as S5 without identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: AGENTS.md discovery; system prompt construction; skills; config/confirmation modes; specialist personas/tool allowlists; provider/workspace settings; TUI commands.
- Plausible first-party paths checked: project instructions as constitution, operator approval as ultimate authority, autonomous policy revision, identity escalation and model/provider choice as policy.
- Why no material first-party path remains: located mechanisms provide operational context, permissions or configuration, not a runtime identity/ultimate-policy decision loop.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one Codey session/task is the assessed organization. Specialist subagents are bounded subordinate actors; the reviewer contributes a complementary S3* audit relation without proving that every specialist is a recursive viable S1.
- Variety: repository state, implementation choices, tool/test outcomes, context pressure, provider errors, specialist findings and permission requests are absorbed by the main operational loop plus supporting mechanisms.
- Escalation: risky tool calls may ask an interactive operator; model/provider failures terminate or retry; reviewer findings return to the parent loop. Ordinary permissions do not become S5.
- Unresolved evidence: no material gap required `?`. The strongest non-S1 positive path is the built-in reviewer audit; no S2, S3, S4 or S5 closure was established.

## Assessment vector

**A · — · — · A · — · —**
