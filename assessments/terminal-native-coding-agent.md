---
harness_id: terminal-native-coding-agent
project_name: terminal-native-coding-agent
repository: https://github.com/RushilBuilds/terminal-native-coding-agent
review_ref: 5bf915097472aee9df4273845f9f8d1e33e22885
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# terminal-native-coding-agent

## Review boundary

- System in focus: one configured, installable first-party Bun/TypeScript terminal-native coding-agent session at frozen `5bf915097472aee9df4273845f9f8d1e33e22885`, with the `runAgentTurn` model-tool loop, MCP tool server/client, local git-worktree sandbox, lifecycle safety hooks, task plan/journal and TUI.
- Purpose and identity: carry out an operator-requested coding task by selecting and revising source-code/command actions on real project feedback, isolating edits to a temporary worktree when available.
- Relevant environment: code files and shell/compiler output, hosted model API, tool/MCP errors, local repo state, unsafe command requests, abort events and configurable runtime limits.
- Standard-distribution boundary: the shipped `src/` agent/TUI/MCP/hooks/sandbox/first-party tools and OpenRouter client invoked through `src/index.ts`. The actual model endpoint, repository being edited, remote external MCP servers, upstream developers and arbitrary post-run human approval/integration are outside first-party agent ownership.
- Credited operating / distribution surfaces: `src/agent/loop.ts`, `src/tui/run.tsx`, `src/tui/App.tsx`, `src/mcp/client.ts`, `src/mcp/server.ts`, `src/sandbox/worktree.ts`, `src/hooks/engine.ts`, built-in hook implementations, `src/agent/plan.ts` and `journal.ts`.
- Adjacent first-party surfaces excluded from ownership: tests, CI/developer governance, architectural proposals and unimplemented roadmap stages (`src/eval/.gitkeep`, telemetry placeholder), unshipped external sandbox adapters and external model-host governance.
- First-party operating / deployment modes considered: configured OpenRouter model with real MCP tools in Ink TUI; offline stub/failure mode; TUI plan/activity/budget display; per-task worktree or unsandboxed fallback; operator apply/discard of edited work; first-party hook denial/redaction.
- Recursion level: one model-directed coding operational unit S1. Tool server, isolated worktree, plan state and TUI panes are support components, not further independent operational organizations.
- Reviewed revision: `5bf915097472aee9df4273845f9f8d1e33e22885` (intake #898 frozen review ref, not current upstream head).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The shipped `src/index.ts` launches `startTui`. When configured with a model key, `buildRunner` creates an optional `WorktreeSandbox` for the current repository, launches its first-party MCP HTTP server, lists the local tools through `McpToolClient`, constructs `OpenRouterClient`, and supplies `runAgentTurn` to the UI. Its real model call advertises the plan plus MCP tools. The model may select one or several tool calls, each dispatched to MCP through pre-tool hook checks and output-transforming post-tool hooks, with results/errors appended to model history for the next tool call decision. A tool-free message ends the current run; a fixed maximum tool-round ceiling or cancel event terminates it. With no provider configuration, a wholly separate `runStubTurn` animates fake plan steps and explicitly states that it is offline; stub behavior is **not** cited as evidence of autonomous operation.

Built-in tool server makes file edits, reads, code search, symbol lookup, git and commands available. The optional worktree isolates the single coding agent from the user's existing checkout and can export a git patch to it; it has no separate worker/agent owners. The plan tool and journal record task steps and restart state, not a cross-S1 supervisory program. The deterministic safety hooks can deny/alter tool calls and redact returned observations. The budget pane presents limits, but this source version still documents an incomplete full ceiling implementation and the actual loop enforces `maxRounds`; no positive higher-function state is inferred from the display or policy constants.

Pinned source: [`README.md`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/README.md); [`src/index.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/index.ts); [`src/tui/run.tsx`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/tui/run.tsx); [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/mcp/client.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/mcp/client.ts); [`src/mcp/server.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/mcp/server.ts); [`src/sandbox/worktree.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/sandbox/worktree.ts); [`src/hooks/engine.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/hooks/engine.ts); [`src/agent/plan.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/plan.ts); [`src/agent/journal.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/journal.ts).

## Operational model

One model-directed worker selects source-edit and shell actions and may update an operator-visible local plan; deterministic hooks and worktree sandbox bound its execution. Local TUI state, control panels and a tool server have no separate discretionary workforce scope. No first-party second S1 owner, independent raw-artifact audit unit or strategic environment adaptation/identity governance loop is evidenced at this fixed revision. Supported offline stub fallback cannot donate autonomy beyond the real configured model-backed mode.

## S1 — Operations

- State: A
- Function: transform open-ended user coding request and workspace observations into model-selected file/shell/inspection steps.
- Disturbance / variety regulated: unknown code, testing/command errors, changes in tool output, local project context and uncertain code-edit strategies.
- Decisive decision or feedback right: choose task-relevant tools/arguments, adjust plan and next actions on concrete results, and stop tool use when done.
- Decision owner: first-party agent loop with model-directed discretion and configured external OpenRouter inference dependency.
- Supporting / enforcement mechanisms: `OpenRouterClient`, MCP client/server/tool handlers, hook vetoes, worktree sandbox, deterministic maxRounds, optional plan/journal TUI reporting.
- Closure path: user instruction → model chooses tool(s) → first-party guarded MCP execution → actual result/error re-enters model chat history → new model decision or stop.
- Boundary reachability: `src/tui/run.tsx` explicitly wires `runAgentTurn` into supported `startTui` when model configuration and tools are available; `runStubTurn` is a separate offline fallback.
- Why this is / is not agent-owned: removing the model from the real branch leaves fixed tools and simulated stub plan animation but not a task-responsive coding policy.
- Evidence: [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/tui/run.tsx`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/tui/run.tsx); [`src/model/openrouter.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/model/openrouter.ts); [`src/mcp/server.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/mcp/server.ts); [`src/mcp/client.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/mcp/client.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: no execution/benchmark was run here; absence of an API key would select the stub instead of demonstrated autonomous S1.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 interference/oscillation attenuation mechanism is wired.
- Disturbance / variety regulated: potential conflicting edits among independently model-running sibling workers; the installed supported runner instantiates only one.
- Decisive decision or feedback right: no shipped ownership over a real cross-agent conflict; worktree protects the user's checkout from the current S1.
- Decision owner: no S2; sandbox creates one independent checkout and `apply()` deterministically attempts to patch the base tree.
- Supporting / enforcement mechanisms: single git-worktree sandbox, git patch/apply, tool server, task-plan UI.
- Closure path: worktree patch is applied or yields an error to the user; this is local single-agent change admission, not an inter-S1 conflict feedback relation.
- Why this is / is not agent-owned: separate MCP processes and worktrees are tool/execution isolation, not interacting independent operational agent cells.
- Evidence: [`src/tui/run.tsx`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/tui/run.tsx); [`src/sandbox/worktree.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/sandbox/worktree.ts); [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/mcp/server.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/mcp/server.ts).
- Basis: structural
- Confidence: high
- Caveats: third-party multiagent compositions are outside this standalone product boundary.

### Absence scope

- Surfaces inspected: all shipped agent/TUI/MCP/sandbox code, package entrypoints, README and roadmap artifacts.
- Plausible first-party paths checked: agent spawn, concurrent S1 task registry, peer mailbox, shared edits arbitration, collision-specific feedback and revised sibling operation.
- Why no material first-party path remains: only one model-directed agent executes per TUI task, while worktree isolation and patch application are per-run safeguards rather than a whole inter-S1 interaction structure.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current operational control over several independently acting workers or commitments.
- Disturbance / variety regulated: capacity, priority and unbalanced current work across multiple S1s would require a separate regulator not shipped here.
- Decisive decision or feedback right: task plan updates are chosen by the same coding actor; max rounds/cancel/budget display are single-run support and enforcement.
- Decision owner: none evidenced for S3; model S1 chooses its plan and user owns launch/cancel controls.
- Supporting / enforcement mechanisms: task-local typed plan, session journal, plan/activity/budget panes, hook veto and runtime step cap.
- Closure path: the operator-visible plan changes progress of one task; no fleet/portfolio state → supervisory decision → changes across S1s.
- Why this is / is not agent-owned: seeing a plan or budget ceiling cannot establish an organizational current-control choice.
- Evidence: [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/agent/plan.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/plan.ts); [`src/agent/journal.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/journal.ts); [`src/tui/run.tsx`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/tui/run.tsx); [`src/tui/panes/BudgetPane.tsx`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/tui/panes/BudgetPane.tsx).
- Basis: structural
- Confidence: high
- Caveats: simulated stub plan and not-yet-enforced full budget ceilings are not credited as current S3.

### Absence scope

- Surfaces inspected: agent loop, TUI current-state panels, plan and journal, MCP lifecycle and hooks.
- Plausible first-party paths checked: whole-current multi-agent roster, resource/commitment priority tradeoff, agent reassignment, independent supervisory mode and corrective return.
- Why no material first-party path remains: runtime has only one model worker and per-task management tools; it does not implement first-party whole-operation managerial discretion.

## S3* — Complementary audit

- State: —
- Function: no distinct independent reviewer/evidence judge returning findings into correction of coding outcomes.
- Disturbance / variety regulated: incorrect code edit, incorrect final success claim or untested command output.
- Decisive decision or feedback right: model can choose a test command on its own, but no separately instantiated first-party auditor independently inspects resulting code.
- Decision owner: none for S3*; current task model and deterministic safety hooks do not compose a complementary reviewer.
- Supporting / enforcement mechanisms: tool result feedback, optional tests as ordinary commands, Git worktree diff and deterministic safety/secret hooks.
- Closure path: test results return to same S1 model; hook denials interrupt risky calls; no complementary reviewer verdict → management correction → subsequent regulated operation.
- Why this is / is not agent-owned: a safety filter or operator-visible code diff is not an autonomous independent inspection of claims.
- Evidence: [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/hooks/engine.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/hooks/engine.ts); [`src/sandbox/worktree.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/sandbox/worktree.ts); [`README.md`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a `src/eval/.gitkeep` placeholder provides no evidence of a shipped evaluator.

### Absence scope

- Surfaces inspected: loop result generation, TUI, hooks, tool/sandbox APIs, `src/eval/` placeholder and docs.
- Plausible first-party paths checked: separate model reviewer, raw-file challenger, independent test-verdict owner, reviewer finding to autonomous correction.
- Why no material first-party path remains: no independently wired review/evaluation and corrective return subsystem exists in the frozen installed code.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally directed prospective intelligence that selects/adopts new capabilities into ongoing harness operation.
- Disturbance / variety regulated: future model/tool changes, novel project environments and strategic shifts would require a future-oriented adaptation owner.
- Decisive decision or feedback right: model's next tool/plan selection is about current coding, while model role and hooks are fixed/operator configuration.
- Decision owner: no first-party S4 function owner.
- Supporting / enforcement mechanisms: model/config roles, session journal, plan, README roadmaps and optional sandbox provider abstractions.
- Closure path: current coding observations shape next coding steps, not future capability options and an adopted organizational change returned to current management.
- Why this is / is not agent-owned: journaling/resume and task-plan changes preserve current operational context; open-source roadmap is developer intent, not runtime S4.
- Evidence: [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`src/agent/journal.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/journal.ts); [`src/agent/plan.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/plan.ts); [`src/config/models.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/config/models.ts); [`README.md`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: external engineering upgrades could change future versions, not the shipped revision under assessment.

### Absence scope

- Surfaces inspected: model config, current plan/journal, user-request loop, sandbox hooks, roadmap and system source tree.
- Plausible first-party paths checked: future external horizon scan, adaptive portfolio option generation, evaluation/selection and persisted adoption returned into whole-current operations.
- Why no material first-party path remains: no first-party prospective intelligence/adoption organization is wired; task-local plans and static configurations do not close S4.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy issue reaching legitimate authority and returning durable governance.
- Disturbance / variety regulated: dangerous tool commands, secrets or unwanted file operations are local safety constraints, not constitutional identity/purpose disputes.
- Decisive decision or feedback right: developer/operator supplies fixed hook safety policies and runtime configuration; pre-tool hooks deterministically allow/deny/rewrite an execution request.
- Decision owner: outside operator/developer for tool policy, HookEngine as enforcement mechanism; no legitimate runtime S5 decision owner.
- Supporting / enforcement mechanisms: builtin dangerous-command/sensitive-file hooks, redaction, MCP tool boundary and model system prompt.
- Closure path: blocked tool call returns a refusal into a worker step; no ultimate-policy matter → authorized governing parent decision → new returned rule governing continued identity/mission.
- Why this is / is not agent-owned: the model cannot legitimately override a constitutional purpose decision merely by proposing a tool; hooks implement preset action constraints.
- Evidence: [`src/hooks/engine.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/hooks/engine.ts); [`src/hooks/builtins/dangerous-commands.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/hooks/builtins/dangerous-commands.ts); [`src/hooks/builtins/protect-sensitive-files.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/hooks/builtins/protect-sensitive-files.ts); [`src/agent/loop.ts`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/src/agent/loop.ts); [`README.md`](https://github.com/RushilBuilds/terminal-native-coding-agent/blob/5bf915097472aee9df4273845f9f8d1e33e22885/README.md).
- Basis: structural
- Confidence: high
- Caveats: a user may change hook configuration or stop the session; that is operational security rather than demonstrated first-party S5 closure.

### Absence scope

- Surfaces inspected: hook implementations/engine, agent/TUI entry, config and task prompt.
- Plausible first-party paths checked: identity mission proposal, parent authority adjudication, durable policy return, future operation affected by legitimate ultimate-policy change.
- Why no material first-party path remains: hooks only veto/modulate code operations under fixed external limits, without a first-party identity-level policy dispute resolution or return.

## Distributed OSS parent arrangement

Repo maintainers, external tool servers and remote model providers do not form one first-party controlling parent of a user-installed TUI session. Read-only source review and publication boundaries remain local to this system-in-focus.

## Self-hosted and non-human modes

The configured OpenRouter runner uses real first-party tools; offline/no-key mode uses a fake animated plan with no autonomous coding. Both share safety UI facilities but only the configured mode demonstrates model-owned S1. Neither creates a parent-governed S3/S4/S5 `(P)` mode.

## Recursion

One coding S1 can call MCP tools and operate inside a git worktree. Tool services, pre-tool hooks and a separate model inference provider do not become nested autonomous viable systems solely from process boundaries.

## Variety and escalation

The model absorbs coding variety through MCP calls and returned observations. Hooks reject risky operations, outputs are truncated to protect context and a tool-round cap stops loops. These are ordinary constraints and feedback, not a separate algedonic organizational function or S5 identity authority.

## Evidence gaps

- This is source-first frozen-revision assessment, not a live model run or measured task success outcome.
- Some README roadmap claims (full budget enforcement, telemetry/eval) are not credited without actual runtime wiring. Offline stub is explicitly excluded from positive S1 evidence.
