---
harness_id: moss-agent
project_name: moss-agent
repository: https://github.com/peterxiemin/moss-agent
review_ref: 82fe64446e88af07b5ed397f365be721fca4da49
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# moss-agent

## Review boundary

- System in focus: first-party installed moss-agent v0.2.0 Node/TypeScript terminal coding agent, with single `Agent` model/tool loop, seven native tools, input queue, permission confirmation, persisted sessions, context compaction, provider retry and standalone developer eval runner. Assessment recursion is one terminal installation handling one coding session at a time.
- Purpose and identity: autonomously execute user-provided code edits, source inspection and shell tasks through local API-driven tool calls with actual results returned to the provider model, while requesting permission for side effects.
- Relevant environment: working-tree source/filesystem, host shell, model API and rate limits, user REPL/TTY, saved conversation log, selected provider profile and optional developer-owned benchmark fixture.
- Standard-distribution boundary: npm package binary `moss`, `src/cli.ts` entry, native `Agent`, `createTools`, input queue and session/permissions, plus separately invokable `eval/run.mjs`. A locally supplied model and upstream cloud API provide inference but are not imported as native management, future intelligence or identity authority.
- Credited operating / distribution surfaces: [package.json](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/package.json); [README.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/README.md); [src/cli.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/cli.ts); [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [src/tools/index.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/index.ts); [src/tools/types.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/types.ts); [src/tools/bash.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/bash.ts); [src/tools/editFile.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/editFile.ts); [src/tools/writeFile.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/writeFile.ts); [src/tools/readFile.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/readFile.ts); [src/tools/glob.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/glob.ts); [src/tools/grep.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/grep.ts); [src/tools/todo.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/todo.ts); [src/queue.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/queue.ts); [src/input.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/input.ts); [src/permissions.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/permissions.ts); [src/retry.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/retry.ts); [src/context.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/context.ts); [src/session.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/session.ts); [src/config.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/config.ts); [src/prompt.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/prompt.ts); [eval/run.mjs](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/run.mjs); [tests/agent.test.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/tests/agent.test.ts); [tests/queue.test.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/tests/queue.test.ts); [tests/permissions.test.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/tests/permissions.test.ts).
- Adjacent first-party surfaces excluded from ownership: [eval/tasks/bugfix-cart/assert.sh](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/tasks/bugfix-cart/assert.sh) and [eval/tasks/feature-coupon/assert.sh](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/tasks/feature-coupon/assert.sh) are manually run evaluation fixtures; [SECURITY.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/SECURITY.md) is project documentation, not a native policy/identity decision owner. Human permissions and externally selected model providers are outside the model-governed organizational authority.
- First-party operating/deployment modes considered: one-shot `moss "prompt"`, REPL with busy FIFO and Esc cancellation, `-y` auto-approval, named provider profiles, resumed JSONL sessions, manual `/compact`, and separately triggered `npm run eval`.
- Recursion level: a single `moss` agent session and its tool calls, not a persistent multi-agent workforce. Batched model tool calls are operations of one decision-maker and do not create independent first-party organizational S1 peers.
- Reviewed revision: 82fe64446e88af07b5ed397f365be721fca4da49.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[package.json](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/package.json) packages a Node 20+ TypeScript command `moss` whose CLI entry in [src/cli.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/cli.ts) instantiates [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts) `Agent`. Its `runTurn` adds a human prompt to message history, streams provider/model output, parses requested tool calls, dispatches the seven first-party code/shell/todo tools and adds actual results to subsequent model turns until the model stops requesting tools or a configured iteration limit is met. Tool-result truncation and message compaction are scoped to the active conversation, while [src/retry.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/retry.ts) handles transient API failures. [src/session.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/session.ts) stores local JSONL interactions for explicit continuation.

The only parallelism inside the core loop is per-batch **read-only tool call** parallelism: [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts) `canRunInParallel` allows `Promise.all` only if every requested tool has `mutating=false`, then records results in original order. When any tool mutates, tool calls run serially with human approval; this is a deterministic operational side-effect safeguard, not a conflict detector/regulator among independent S1 agents. [src/queue.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/queue.ts) keeps a FIFO of user messages received while the *same* REPL agent is busy, draining sequentially and dropping leftovers on interruption. No first-party subagent or peer-manager exists in the native entry-point; [README.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/README.md) explicitly lists subagents/workflow/hooks/plugins/MCP/Web UI as intentionally out of scope.

[src/permissions.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/permissions.ts) and [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts) request approval for bash and edits, optionally caching per-session explicit allow decisions; `-y` can bypass it by user choice. [eval/run.mjs](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/run.mjs) separately starts CLI subprocesses in fixture directories and uses shell assertion files to score tasks. It demonstrates external developer evaluation, not an S3* complementary audit actor integrated with the agent's normal ongoing tool/management loop. [src/tools/todo.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/todo.ts) offers a model-controlled local task list and is one-S1 planning rather than whole-current management.

## Operational model

One model session chooses code actions, observes results and repairs errors within the request. The REPL input queue and non-mutating parallel-tool condition are deterministic safeguards for one operational path. Neither creates simultaneous autonomous agent peers or closed inter-peer coordination. An external user may run a separate benchmark or review a diff and act on its outcome, but there is no native independent current-control auditor. No future capability intelligence or ultimate identity arbitration is implemented.

## S1 — Operations

- State: A
- Function: fulfil uncertain user coding tasks by model-guided file/shell/search/todo actions, observing and reacting to tool outputs.
- Disturbance / variety regulated: unknown code facts, unexpected shell outputs, missing file paths, edits, provider errors, token limits, aborted tools and iterative clarification needed to complete the current coding request.
- Decisive decision or feedback right: model selects each next tool, reads the concrete outcome and chooses whether to try again, change method, or finish.
- Decision owner: first-party `Agent` model/tool loop; external OpenAI-compatible inference endpoint supplies model responses but not local workflow/action ownership.
- Supporting / enforcement mechanisms: seven tool registry entries, streaming model adapter, serialized message context, FIFO prompt queue, per-tool permission checks, retries, token compaction and session persistence.
- Closure path: user prompt → model-chosen tool call → actual bash/file/todo execution → result appended to same model transcript → next context-dependent tool or terminal response.
- Boundary reachability: `moss` CLI starts `Agent`, `runTurn` is reachable in one-shot/REPL, and each tool result is appended before next model turn. No external worker process controls the choice.
- Why this is / is not agent-owned: removing model decisions leaves callable tools and a deterministic queue but no situated next coding action or completion judgment.
- Evidence: [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [src/cli.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/cli.ts); [src/tools/index.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/index.ts); [src/tools/bash.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/bash.ts); [src/tools/editFile.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/editFile.ts); [src/tools/todo.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/todo.ts).
- Basis: explicit + structural.
- Confidence: high for first-party operational code.
- Caveats: no provider-backed run or benchmark pass rate was reproduced during this source-first assessment.

## S2 — Coordination

- State: —
- Function: no native cross-S1 conflict or oscillation attenuation exists for independently acting peer units.
- Disturbance / variety regulated: concurrent read-only tool invocations or user messages arriving during a busy REPL could affect *one* task's operation, but there is no competing independently goal-directed agent system requiring peer arbitration.
- Decisive decision or feedback right: deterministic `canRunInParallel` prevents simultaneous **mutating tools in one model turn**; FIFO queue serializes a single user's queued prompts. Neither arbitrates competing autonomous worker claims.
- Decision owner: TypeScript guard and `InputQueue` for intra-S1 sequencing, not a separate S2 regulator.
- Supporting / enforcement mechanisms: mutating flag on tool metadata, Promise.all for read-only batches, sequential mutating execution, REPL busy FIFO and Esc cancel.
- Closure path: model's own tool batch is serialized or read-only parallelized → tool results return to same model; queued user prompt waits for current turn, not for a conflict-resolution outcome between S1s.
- Why this is / is not agent-owned: task-side-effect ordering and input-buffering solve single-agent reentrancy, not adaptive current relations between distinct S1 peers.
- Evidence: [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [src/queue.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/queue.ts); [src/tools/types.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/types.ts); [src/cli.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/cli.ts).
- Basis: structural + explicit.
- Confidence: high within shipped product.
- Caveats: multiple independently launched `moss` processes may interfere externally; that does not create a native inter-process S2 mechanism.

### Absence scope

- Surfaces inspected: core model/tool loop, mutating read/write classification, CLI busy input queue, session storage, permission rules and local todo list.
- Plausible first-party paths checked: distinct active worker responsibilities, inter-agent lock/resource reservation, collision-feedback dispatch, peer conflict arbitration and consequential returned per-worker behavior change.
- Why no material first-party path remains: shipped source contains one coding Agent and no subagent organizational graph; intra-agent tool ordering and FIFO user inputs are not an S2 relation.

## S3 — Inside-and-now control

- State: —
- Function: no native management of whole-current portfolio, resources and commitments of independent S1 workers is demonstrated.
- Disturbance / variety regulated: current task progress can be represented by `todo` and history, but these concern one operative coder, not a workforce of separate agents.
- Decisive decision or feedback right: one model edits its current todo list and acts on the current prompt; no separate global status/resource tradeoff/priority intervention affecting multiple independently operating S1s.
- Decision owner: single coding model and user for input/consent, not a distinct organization-wide current-control agent.
- Supporting / enforcement mechanisms: `TodoList`, REPL queue, tokens/cost readout, session logs, iteration cap and command gating.
- Closure path: a todo/tool result informs the same coding model's next action; no shared current org view → whole-current manager decision → corrected obligations returned to worker agents.
- Why this is / is not agent-owned: local operational planning is part of S1, even when the model tracks several checklist items.
- Evidence: [src/tools/todo.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/tools/todo.ts); [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [src/queue.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/queue.ts); [src/session.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/session.ts).
- Basis: structural.
- Confidence: high for supported modes.
- Caveats: a human engineer coordinating many CLI processes would be an external owner not part of the first-party assessed harness.

### Absence scope

- Surfaces inspected: all native tools and models, session/todo mechanisms, REPL loop, input queue and eval runner.
- Plausible first-party paths checked: active whole-organization/worker roster, current commitments, resource budgeting across agents, model-owned reassignment/intervention and consequential returned control.
- Why no material first-party path remains: implementation exposes only one model owner per process and its task state, no native whole-current workforce authority.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary auditor that independently examines operational reality and returns findings to present system-level control is integrated into the runtime.
- Disturbance / variety regulated: coding errors can be detected by ordinary tool/test output and standalone developer fixture assertions, but neither is an independently governed live audit feeding a separate manager.
- Decisive decision or feedback right: model sees its own tool results, and an external developer can run `npm run eval` to assess fixture outcomes; no native independent reviewer decides an audit finding and returns it to an S3 owner.
- Decision owner: operative coder for its tool feedback, external evaluator/human for benchmark execution/consumption; no native S3* actor.
- Supporting / enforcement mechanisms: command execution output, optional user verification, developer-owned fixture assertion scripts and external logs.
- Closure path: current tool output → same model's next attempt, or separately invoked eval fixture → stdout verdict to human; **no independent reviewer→current-control→producer correction loop**.
- Why this is / is not agent-owned: an executable test harness in the development repo demonstrates testing but not an autonomous complementary audit-control path within the installed agent organization.
- Evidence: [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [eval/run.mjs](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/run.mjs); [eval/tasks/bugfix-cart/assert.sh](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/eval/tasks/bugfix-cart/assert.sh); [tests/agent.test.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/tests/agent.test.ts); [README.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an outside CI or manually prompted code review could furnish complementary evidence but is not wired into moss-agent current-control.

### Absence scope

- Surfaces inspected: tool outcome loop, fixture-based eval, native tool list, REPL command set, session events and permission prompts.
- Plausible first-party paths checked: independently commissioned reviewer, alternate raw-code/test sampling, autonomous audit judgment, findings addressed to a distinct S3 parent and post-finding operational correction.
- Why no material first-party path remains: developer eval is a separate command and the operative agent has no auditor interface or independent reviewer runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no native prospective external environment intelligence with strategy/capability adaptation alternatives and return into present organizational control.
- Disturbance / variety regulated: model endpoint changes, token limits, new user files and interruptions affect current performance but do not trigger an autonomous future environmental sensing process.
- Decisive decision or feedback right: provider selection and context compaction are per-run user/config controls; no model-owned analysis of outside future possibilities controlling organizational capability development.
- Decision owner: user selecting providers/profiles and active coding agent solving current task, not a future strategy function.
- Supporting / enforcement mechanisms: provider aliases, environment configs, token budgets, retries, local session restore and readme guidance.
- Closure path: changed model choice or restored context influences current inference; no outside-and-then sensing → alternatives → S3 resource/capability choice → returned long-term adaptation.
- Why this is / is not agent-owned: using newer models or saving context does not evidence strategic future-facing organization control.
- Evidence: [src/config.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/config.ts); [src/context.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/context.ts); [src/retry.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/retry.ts); [src/session.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/session.ts); [README.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/README.md).
- Basis: structural.
- Confidence: high within first-party code.
- Caveats: external users can run the tool for research/strategy tasks, but such requests do not create a first-party ongoing S4.

### Absence scope

- Surfaces inspected: provider/profile selection, agent loop, retained context, session restore, tool outputs, user slash commands and benchmark scripts.
- Plausible first-party paths checked: external future scanning, trend/option comparison, capability tradeoff selection by managerial parent and enacted future adaptation.
- Why no material first-party path remains: available state and config respond to current tool tasks or direct user choices, not autonomous long-horizon system adaptation.

## S5 — Policy and identity

- State: —
- Function: no native supreme identity/ethos policy arbitration with binding governance return is implemented.
- Disturbance / variety regulated: risky file writes and shell actions are subject to user approval; model credentials or settings are external user consent and execution constraints.
- Decisive decision or feedback right: user allows one action, all actions of a type for a session, or denies; `-y` disables prompts by user choice. No first-party highest-authority S3/S4 policy or identity conflict decision exists.
- Decision owner: external human operator for tool consent, deterministic CLI for enforcement, not a model-owned S5 parent.
- Supporting / enforcement mechanisms: explicit diff previews, permission choices, session-level allow cache, `-y` flag and configuration.
- Closure path: requested mutating tool call → human allow/deny or auto setting → current model work continues/stops; no identity dispute→legitimate ultimate policy judgment→returned binding organization rule.
- Why this is / is not agent-owned: technical permission control and software security guidance are not sufficient for system mission/identity governance.
- Evidence: [src/permissions.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/permissions.ts); [src/agent.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/agent.ts); [src/config.ts](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/src/config.ts); [SECURITY.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/SECURITY.md); [README.md](https://github.com/peterxiemin/moss-agent/blob/82fe64446e88af07b5ed397f365be721fca4da49/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: a human/enterprise operating moss-agent might impose higher policy from outside its runtime boundary.

### Absence scope

- Surfaces inspected: permission choices and their caching, CLI flags, user input/interrupt control, model profile configs, evaluation and developer docs.
- Plausible first-party paths checked: ultimate policy/identity conflict recognition, legitimate top-level decision, long-term binding ethos choices and return to current and future management functions.
- Why no material first-party path remains: every substantive native constraint concerns tactical tool execution and user configuration, not the highest organizational identity authority.

## Recursion

One moss-agent process has one independently model-guided operational S1. Multiple tool calls, read-only parallelism, queued human messages and the local todo list do not establish separate S1 organizations or S2 coordination. A standalone benchmark runs outside the ongoing installed model loop and does not create S3*. The user and external model provider are distinct external actors.

## Variety and escalation

Repo state, tool outputs, model errors and user prompts provide operational variety. The loop attenuates hazards through permission prompts, retry, length truncation and serial mutating execution. REPL FIFO and Esc interruption avoid losing/continuing user work contrary to the current session, without arbitrating independent worker interference. No whole-current manager, independent auditor, future intelligence or highest-policy decision/return is observed at the evaluated recursion.

## Evidence gaps

Source-first classification at one frozen public SHA, not a provider-backed end-to-end benchmark reproduction. An existing developer fixture evaluation `eval/run.mjs` is recognized but not promoted into autonomous S3* by name; no result or live credentials were claimed. The negative states are bounded to the executable documented CLI standard distribution at this revision, excluding hypothetical external multi-agent compositions and future features. The repository expressly does not implement subagent, workflow, hook, plugin or MCP modes.
