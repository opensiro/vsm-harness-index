---
harness_id: soloncode
project_name: SolonCode
repository: https://github.com/opensolon/soloncode
review_ref: 123e7a2d19e33b0fff72b5518062b020b3c96bc3
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
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SolonCode

## Review boundary

- System in focus: the first-party `opensolon/soloncode` coding-agent distribution at frozen revision `123e7a2d19e33b0fff72b5518062b020b3c96bc3`, including the SolonCode CLI/Web/Desktop-backed agent runtime, model→tool execution loop, built-in coding/tool permissions, first-party subagent delegation, Goal lifecycle, durable sessions/memory/checkpoints, supported scheduled/loop execution, and ACP/MCP/OpenAPI/LSP integration where those surfaces bear on organizational function.
- Purpose and identity: execute software-engineering and adjacent workspace tasks by giving a model-backed coding actor repository/environment context, first-party tools, persistent state and optional specialized subagents, then returning tool/environment results so the actor can continue until it completes, blocks, or is externally stopped.
- Relevant environment: user objectives, project/workspace files and Git state, tool/command/test/LSP results, configured model-provider responses, external MCP/OpenAPI services, session and long-term-memory state, operator permission decisions, and optional scheduled/Goal prompts.
- Standard-distribution boundary: SolonCode's shipped Java CLI backend, CLI/Web/Desktop operating surfaces, HarnessEngine composition instantiated by SolonCode, built-in tools/permissions, session/memory/Goal/checkpoint mechanisms, first-party subagent definitions/delegation, and supported loop/ACP surfaces are inside. Solon AI internals not concretely instantiated by SolonCode, external model providers, MCP/OpenAPI servers, host OS tooling, target-project governance and external services are dependencies/environment rather than SolonCode organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `soloncode-cli/src/main/java/org/noear/solon/codecli/portal/printmode/PrintMode.java`; `soloncode-cli/src/main/java/org/noear/solon/codecli/command/builtin/GoalTalent.java`; `soloncode-cli/src/main/java/org/noear/solon/codecli/workspace/WorkspaceManager.java`; the shipped `solon-development-skill` Harness reference describing the SolonCode HarnessEngine composition; and `UPDATE_LOG.md` where it corroborates standard subagent, Goal, session, memory, loop and recovery paths at or before the frozen revision.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI/release activity; maintainer/contributor governance; documentation examples that demonstrate generic Solon AI Harness APIs without proving SolonCode runtime reachability; later default-branch behavior after the frozen ref; and user-created custom agents/skills/automation content beyond the shipped organizational paths.
- First-party operating / deployment modes considered: interactive CLI; Web and Desktop-backed local agent sessions; print/headless runs; durable/resumed sessions; automatic-edit, approval and read-only planning permission modes; persistent Goal execution; first-party subagent delegation; configured loop/scheduled prompts; and ACP/serve integration.
- Recursion level: one SolonCode coding session/Goal organization. The main coding actor is the primary S1. Specialized subagents may execute bounded delegated tasks as subordinate operational actors, but the reviewed standard distribution does not establish a stronger team recursion with a complete first-party cross-subagent coordination/current-control organization merely from their existence.
- Reviewed revision: `123e7a2d19e33b0fff72b5518062b020b3c96bc3`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

SolonCode is a Java coding-agent product built on Solon AI but ships its own supported executable composition. The frozen README exposes CLI, Web and Desktop modes and states that the Java backend provides the agent runtime, model access and tools. Its standard modes include approval execution, automatic editing, read-only planning and persistent Goal execution. Sessions retain history, long-term memory, rewind/redo and recoverable workspace checkpoints; the runtime also exposes Skills, Agents, MCP, OpenAPI, LSP and loop/automation surfaces.

The first-party Harness reference preserved in the SolonCode tree documents the concrete HarnessEngine architecture used by SolonCode: a main ReAct-style model actor receives a prompt/session, chooses from coding/search/shell/file tools, receives results and can continue iteratively. It supports first-party subagents with separately defined prompts/tool permissions, plus runtime controls such as sandboxing, HITL, retries, context compression and model selection. The same reference explicitly distinguishes main-agent execution from dynamically created subagents and records that subagent events return through the HarnessEngine stream.

Goal mode adds persistent task closure around that S1. `GoalTalent` exposes the current objective, iteration and token/time budget to the model; the model can declare `complete` or `blocked`. A completion claim may be rejected when the current round lacks action evidence, TODO items remain unfinished, or the configured deterministic Goal validator fails. A failed check is returned to the model with an instruction to continue and retry completion. These are meaningful completion/recovery controls, but the validator is deterministic enforcement around the same task loop rather than a separately autonomous complementary-audit owner.

The runtime also supports persistent workspaces, session/state restoration, file watching, loop scheduling and configurable tool/model/agent surfaces. These mechanisms make long-running execution robust and extensible. They do not by themselves create outside-and-future adaptation, identity/ultimate-policy judgment or a whole-organization manager.

Primary evidence:

- [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md)
- [`PrintMode.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/portal/printmode/PrintMode.java)
- [`GoalTalent.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/command/builtin/GoalTalent.java)
- [`WorkspaceManager.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/workspace/WorkspaceManager.java)
- [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md)
- [`UPDATE_LOG.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/UPDATE_LOG.md)

## Operational model

A supported SolonCode session receives a task and current workspace/session context. The model-backed main actor chooses coding/search/file/shell or integration actions exposed by the first-party HarnessEngine composition. SolonCode executes or gates the action, records the result and feeds it back into the same agent loop. The actor can keep modifying/inspecting the workspace, invoke specialized subagents, update TODO/Goal state and continue until it returns a final answer or Goal status, blocks, hits runtime policy, or the user stops it.

Subagent support creates additional bounded model-backed workers, but the standard evidence reviewed here primarily establishes delegation and returned subagent results. It does not establish a concrete cross-subagent interference witness plus a first-party attenuation loop for S2, nor a complete whole-team current view with organization-wide commitment/resource authority for S3.

Goal completion checks provide a separate evidence path from the model's bare completion claim—action evidence, TODO state and optional validator output can reject `goal_update(complete)`. However, the decisive validation path is deterministic first-party machinery, not an autonomous audit actor. It therefore strengthens S1 closure and quality without satisfying Methodology 0.3.6 autonomous S3* ownership.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work in the selected workspace by interpreting the objective, selecting coding/tool actions, applying them, observing results and iterating until completion or blockage.
- Disturbance / variety regulated: heterogeneous user objectives, repository structure and instructions, file/Git state, command/test/LSP/tool outputs, tool failures, provider responses, incomplete TODO/Goal state and changing implementation evidence.
- Decisive decision or feedback right: choose which repository/environment evidence to inspect, which exposed tool/action or subagent to invoke next, how to revise the implementation from returned observations, and when to attempt completion or declare blockage within the configured policy boundary.
- Decision owner: the model-backed main SolonCode agent in the shipped HarnessEngine execution path.
- Supporting / enforcement mechanisms: first-party tool registry; file/search/edit/bash/code tools; permission/sandbox/HITL controls; session/history/memory; context compression; TODO/Goal state; completion validation; checkpoints/rewind; subagent invocation; retries; CLI/Web/Desktop/print/ACP transports.
- Closure path: task + workspace/session state → model-backed agent chooses tool/subagent/action → SolonCode executes or gates it → tool/subagent/environment result returns into the session → the agent chooses the next action, retries, blocks or finishes.
- Boundary reachability: CLI, Web/Desktop and print/headless modes directly instantiate the first-party agent runtime and coding tools; the user does not need to author a downstream orchestration layer to obtain the model→tool feedback loop.
- Why this is / is not agent-owned: removing the model-backed actor while retaining permissions, tools, sessions, Goal state and deterministic validators leaves enforcement/storage/execution machinery but removes the open-ended coding judgment that selects and sequences work.
- Evidence: [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md); [`PrintMode.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/portal/printmode/PrintMode.java); [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md); [`GoalTalent.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/command/builtin/GoalTalent.java).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference remains a dependency; SolonCode is credited for the shipped agent role, tool/action composition and returned-result closure, not provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function meeting the Methodology 0.3.6 disturbance/attenuation/feedback threshold was established at the selected recursion.
- Disturbance / variety regulated: not established at S2 level. SolonCode can delegate work to specialized subagents, including parallel-subagent support in the shipped evolution history, but the reviewed standard evidence does not identify a concrete cross-subagent interference/oscillation condition that a first-party coordination relation specifically attenuates.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: main-agent delegation; task/subagent tools; per-agent tool permissions; returned subagent stream/results; TODO state; sandboxing; runtime concurrency and session mechanisms.
- Closure path: not applicable; the evidence establishes delegation/result return but not a specific distinct-S1 disturbance → coordination response → changed subsequent S1 behaviour loop.
- Why this is / is not agent-owned: the main agent may choose a subagent and consume its result, but routing/delegation among model workers is not itself S2. No stronger interference-specific coordination decision is evidenced at the frozen boundary.
- Evidence: [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md); [`UPDATE_LOG.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/UPDATE_LOG.md); [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user-authored team organization built from SolonCode agents could contain real S2; that larger organization is not supplied merely by the standard subagent primitive.

### Absence scope

- Surfaces inspected: standard main-agent/subagent Harness composition; agent definitions/tool permissions; returned subagent events; documented parallel-subagent evolution; TODO/Goal state; session/workspace machinery; CLI/Web/Desktop operating modes.
- Plausible first-party paths checked: specialist subagent delegation; parallel subagents; task/TODO assignment; shared workspace state; per-agent permissions; result return to the main agent; session/loop scheduling.
- Why no material first-party path remains: the located mechanisms create workers and move task/result information, but no frozen-revision evidence establishes a specific inter-S1 conflict/oscillation plus an S2-specific attenuation relation and feedback loop. Generic delegation, shared state and concurrency are insufficient under Methodology 0.3.6.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the coding S1 and deterministic task/runtime controls was established.
- Disturbance / variety regulated: current Goal progress, unfinished TODO items, token/time/turn budgets, blocked execution, tool failures and active-session state are regulated operationally, but no whole-organization current-control problem over multiple relevant S1 commitments/resources is established.
- Decisive decision or feedback right: not established at S3 level. The main agent chooses operational actions and delegated subtasks as part of S1; Goal/TODO/budget/loop mechanisms enforce or expose current task state rather than supply a separate organization-wide management decision.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Goal status and budgets; TODO completion checks; loop scheduler; busy guards; model/tool turn limits; retries; stop/continue/rewind; session state; subagent delegation.
- Closure path: not applicable; no whole-system current view plus substantive resource/priority/commitment/accountability intervention path beyond the current coding task was reconstructed.
- Why this is / is not agent-owned: the model can inspect Goal state and choose operational next steps, but that is the same S1's task execution. Deterministic scheduler/budget/validator machinery continues to enforce preselected limits if the agent is removed, so it does not establish autonomous S3 ownership.
- Evidence: [`GoalTalent.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/command/builtin/GoalTalent.java); [`WorkspaceManager.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/workspace/WorkspaceManager.java); [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: SolonCode has substantial execution supervision and persistent Goal control. The negative result is specifically about the Profile's stronger whole-system S3 function at the declared recursion, not about operational robustness.

### Absence scope

- Surfaces inspected: Goal lifecycle/current-state reporting; token/time/iteration budgets; TODO linkage; validation/retry; loop/scheduler execution; session busy guards; subagent delegation; Web/Desktop current-session controls; runtime permissions.
- Plausible first-party paths checked: main-agent delegation as a manager; Goal status as a whole-system view; scheduler/budget enforcement; blocked/resume behavior; subagent state/result return; operator session controls.
- Why no material first-party path remains: the main-agent evidence is task execution/delegation without a reconstructed organization-wide current portfolio and substantive management authority, while scheduler/budget/termination paths are deterministic task controls rather than autonomous S3 decisions.

## S3* — Complementary audit

- State: —
- Function: no autonomous complementary-audit role with materially independent audit judgment was established in the standard SolonCode organization.
- Disturbance / variety regulated: false or premature completion claims, unfinished TODOs and failing build/test validation can be detected before a persistent Goal is accepted as complete.
- Decisive decision or feedback right: the model may propose completion; first-party deterministic checks can reject that claim when action evidence is missing, TODOs remain open, or the selected `GoalValidator` fails.
- Decision owner: deterministic SolonCode validation machinery for the completion gate; no separate autonomous auditor owns the audit judgment.
- Supporting / enforcement mechanisms: `goal_update(complete)`; action-evidence check; unfinished-TODO check; `ValidatorFactory` / `GoalValidator`; returned `VALIDATION_FAILED` feedback; ordinary coding/test tools and change-review UI.
- Closure path: agent completion claim → deterministic evidence/TODO/validator checks → pass accepts Goal completion or failure returns a reason → the same coding agent continues and may attempt completion again.
- Why this is / is not agent-owned: this is a real independent evidence check around S1 completion, but the decisive audit verdict is produced by deterministic rules/validators rather than an autonomous complementary audit actor. The coding model that reacts to the verdict is the producing S1, not an independent auditor.
- Evidence: [`GoalTalent.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/command/builtin/GoalTalent.java); [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md); [`UPDATE_LOG.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/UPDATE_LOG.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Goal validation materially improves verification and can use evidence distinct from the model's self-report. Methodology 0.3.6 still separates deterministic validation from autonomous S3* ownership.

### Absence scope

- Surfaces inspected: Goal completion validator; action-evidence and TODO checks; built-in review/change surfaces; coding/test/shell/LSP tools; subagent definitions; session history; repository-development tests/CI boundary.
- Plausible first-party paths checked: separate reviewer subagent; Goal validator as complementary audit; change-review UI; self-test/tool verification; independent scheduled review agent; repository CI.
- Why no material first-party path remains: the only clearly closed complementary check at the frozen runtime boundary is deterministic Goal validation, while no separately autonomous reviewer/auditor with independent judgment and corrective return is wired into standard operation. Repository CI/tests and optional user-authored reviewer agents are adjacent or require composition.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-future intelligence loop that generates and adopts organizational adaptation was established.
- Disturbance / variety regulated: not established at S4 level. Long-term memory, context compression, skills/agents, web/code search, scheduled prompts and persistent sessions expand information available to current/future tasks but do not by themselves create prospective environmental modeling and capability adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: long-term memory; persistent sessions; skills/agents; MCP/OpenAPI/LSP; context compression; scheduled/loop prompts; configurable models and runtime settings.
- Closure path: not applicable; no supported external/future distinction → adaptation-option generation → autonomous selection → persistent capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: memory stores/reuses information and scheduled prompts rerun operational work. Runtime configuration and installed skills/agents can change capability, but the reviewed standard distribution does not establish an autonomous agent that prospectively decides and installs such adaptations.
- Evidence: [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md); [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md); [`UPDATE_LOG.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/UPDATE_LOG.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator or user-authored automation may use SolonCode to research and modify its own environment; generic ability to do so is not a first-party closed S4 function.

### Absence scope

- Surfaces inspected: persistent memory; history/context compression; skills/agents; Web/code search; MCP/OpenAPI/LSP; scheduled/loop tasks; Goal mode; model/runtime configuration; checkpoint/rewind.
- Plausible first-party paths checked: memory-driven learning; scheduled environmental scanning; autonomous skill/agent installation; model switching; runtime self-modification; update checks; Goal loops across time.
- Why no material first-party path remains: located mechanisms retain information, execute configured prompts or expose adaptation primitives, but the decisive prospective adaptation judgment and persistent capability change remain user/configuration authored or absent.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: tool permissions, sandbox policy, HITL/approval mode, system prompts, model selection, agent definitions and workspace settings constrain operation, but they are ordinary configured operating policy rather than a reconstructed identity-level governance function.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: user/operator/configuration for the relevant runtime constraints; SolonCode deterministically enforces those choices and the model operates within them.
- Supporting / enforcement mechanisms: allow/disallow tool configuration; sandbox; HITL; approval/automatic/read-only modes; system prompt/AGENTS/agent definitions; model/provider configuration; project/global settings.
- Closure path: not applicable at S5 level; configuration can be edited and then governs later operation, but no standard identity/policy conflict → legitimate ultimate authority → authoritative decision → returned operation loop was found.
- Why this is / is not agent-owned: the model does not own the ultimate permission/system-identity boundary, and deterministic enforcement does not become S5 merely because it can strongly constrain actions.
- Evidence: [`README.md`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/README.md); [Harness reference](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/release/skills/solon-development-skill/references/ai_harness.md); [`PrintMode.java`](https://github.com/opensolon/soloncode/blob/123e7a2d19e33b0fff72b5518062b020b3c96bc3/soloncode-cli/src/main/java/org/noear/solon/codecli/portal/printmode/PrintMode.java).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent organization can impose its own S5 through SolonCode configuration, but no first-party function-specific parent loop is established merely by exposing configuration and approval surfaces.

### Absence scope

- Surfaces inspected: system prompt and agent definitions; global/workspace settings; tool allow/deny and permission modes; sandbox/HITL; model/provider selection; Goal policy; ACP/MCP/OpenAPI/LSP integration; operator controls.
- Plausible first-party paths checked: operator approval as parent policy; system-prompt edits; permission changes; model changes; project AGENTS identity; agent-definition governance; runtime self-configuration.
- Why no material first-party path remains: these surfaces configure or enforce ordinary task/runtime policy. No frozen-revision evidence reconstructs a genuine identity/ultimate-policy issue reaching a legitimate ultimate authority and returning as a governing organizational decision.

## Distributed OSS parent arrangement

The public repository has normal maintainer/contributor governance, while deployed SolonCode sessions are local to their operators/workspaces. No organization-level S3/S4/S5 parent loop is inferred from OSS contribution activity. A local user can approve tools or edit configuration, but those actions do not by themselves satisfy the parent-mode function requirements.

## Self-hosted and non-human modes

SolonCode is self-hostable and exposes supervised/approval as well as more automatic execution modes. These modes materially change how individual tool actions are permitted, but no qualifying parent-governed S3/S4/S5 loop was established from that fact alone. The autonomous S1 remains available in standard modes because the model still chooses the open-ended coding actions inside the configured boundary.

## Recursion

The focal recursion is one SolonCode coding session/Goal organization. The main model-backed actor owns the open-ended coding operation and may invoke bounded first-party subagents. A stronger team recursion would require evidence that the shipped runtime treats multiple subagents as persistent S1 units under a material S2/S3 organization; delegation alone is not enough.

## Variety and escalation

SolonCode attenuates operational variety through tool permissions, sandbox/HITL modes, retries, context compression, durable state, Goal/TODO completion gates, budgets, checkpoints/rewind and blockage reporting. A model can mark a persistent Goal `blocked`, and approval modes can return dangerous actions to the human. These are useful escalation and safety mechanisms around S1, but they do not automatically establish S3 or S5 at the declared recursion.

## Evidence gaps

No evidence gap requires `?` for the frozen revision. The reviewed primary surfaces are sufficient to establish the first-party S1 loop and to bound the stronger S2/S3/S3*/S4/S5 claims conservatively. In particular, the review inspected the most plausible positive paths—subagents, Goal control/validation, persistent memory, scheduled loops and policy/permission configuration—rather than treating their labels as VSM functions.

## Assessment summary

SolonCode is a substantive first-party coding-agent harness with a closed autonomous model→tool execution loop and unusually rich persistence, Goal, subagent and control mechanisms. At the frozen revision those mechanisms strengthen and extend S1, but the reviewed standard distribution does not establish the stronger organizational closures required for S2, S3, autonomous S3*, S4 or S5.

**Vector:** A · — · — · — · — · —
