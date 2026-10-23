---
harness_id: ti
project_name: ti
repository: https://github.com/tmjwjx/ti
review_ref: 68cd5bceff33aef1dd95fddc8ad955557481a162
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ti

## Review boundary

- System in focus: the installed `@tmjwjx/ti` 0.0.10 terminal coding agent, its TypeScript model/tool loop, project-scoped session state, skills loader, context compaction, TUI/REPL and provider/configuration management.
- Purpose and identity: assist an operator with reading, changing and testing workspace code and files during terminal conversations.
- Relevant environment: operator requests, workspace content, tool outputs and failures, interruption, provider stream status, context-window size and local session history.
- Standard-distribution boundary: `src/main.ts`, `src/core/`, `src/tools/`, `src/llm/`, `src/cli/`, and `src/config/` as bundled by `scripts/build.mjs`. Provider APIs and user-written skills are dependencies; their internal organization is not imported into the ti owner.
- Credited operating / distribution surfaces: regular TTY and non-TTY REPL; `agentTurn` selecting and executing `read`, `write`, `edit`, `bash`; resume/compact/skills commands; user-selected providers; operator-initiated `ti update`.
- Adjacent first-party surfaces excluded from ownership: repository maintainer workflow, `AGENTS.md`, design proposals, package CI or release practice, tests and mocks, user-created instructions and any external orchestration of multiple ti processes.
- First-party modes checked: ordinary model/tool session, interrupted and restarted/resumed session, provider switch, skills invocation, automatic/manual context compaction and package updater. None instantiates multiple independently acting first-party agents.
- Recursion level: one locally operated coding-agent conversation/workspace, not an organization of terminal-agent workers or the developer community.
- Reviewed revision: `68cd5bceff33aef1dd95fddc8ad955557481a162` (batch #1006, row 9).
- License: MIT (`LICENSE`).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`main.ts` configures exactly one provider and builds the one-session prompt. `repl.ts` turns user input into `agentTurn(messages, ctx)`. That loop asks the configured model to choose from four registered tools, executes complete calls sequentially and appends results to the same conversation before another model choice. It safely seals incomplete/aborted calls and stops at a turn cap. `src/core/session.ts` records one project-local JSONL conversation; a PID-backed `.lock` prevents two processes from concurrently appending **the same session file**. This is a persistence integrity mechanism, not coordination of distinct S1 workers' coding actions in one shared task.

`src/core/compact.ts` summarizes a large conversation for continued **current-task** context; `src/core/skills.ts` discovers existing project/user skills and exposes their descriptions for selection. Neither path creates, tests and adopts new strategic capabilities for future environmental changes. `src/cli/update.ts` offers an explicitly user-invoked package-version update from npm's official latest endpoint; release choices belong to external maintainers and the update policy is a mechanical latest-version comparison, not the harness's prospective environment/capability strategy. A user may choose a provider or stop an active request, but no separate S3 whole-current supervisory layer is instantiated.

Pinned primary evidence: [entry and REPL](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/main.ts), [agent loop](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/agent.ts), [tools](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/tools/index.ts), [session lock](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/session.ts), [compaction](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/compact.ts), [skills](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/skills.ts), [updater](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/cli/update.ts), [declared non-goals](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/docs/ARCHITECTURE.md).

## Operational model

One model-led tool-action loop is active (`S1=A`). Serial tool execution, session-file locks, model-provider selection and skill lists do not create multiple independent operating units (`S2=—`). There is no first-party whole-current management layer (`S3=—`) or separately deciding audit institution (`S3*=—`). Context compaction and explicit package updating do not close a prospective capability-policy/adoption cycle (`S4=—`), and local model configuration and instruction text do not constitute identity-level policy (`S5=—`). These claims are confined to the pinned distributed program, not other projects potentially built around it.

## S1 — Operations

- State: A
- Function: perform user-directed coding work through read/write/edit/command tools and revise actions from returned observations.
- Disturbance / variety regulated: unfamiliar repositories, partial or failed model streams, command errors, interrupted requests, changing files and returned tool results.
- Decisive decision or feedback right: the model determines which complete tool calls to issue, their arguments, follow-up steps and when to stop.
- Decision owner: one provider-backed inference model in the session `agentTurn` loop.
- Supporting / enforcement mechanisms: `TOOLS` schemas/dispatcher, streaming protocol adapters, `pushMessage` persistence, `AbortSignal`, incomplete-call sealing and `MAX_TURNS=100`.
- Closure path: request and current messages → model selects tool → first-party dispatcher executes it → success/error becomes `toolResult` → model chooses another action or answers.
- Boundary reachability: both TTY and readline REPL call the same shipped `agentTurn`, which executes the four registered tools and feeds their results back to `callLLM`.
- Why this is / is not agent-owned: choosing the next workspace operation and responding to its result is model discretion; tool schema and abort handlers merely enforce mechanics.
- Evidence: [agent](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/agent.ts), [tool dispatcher](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/tools/index.ts), [REPL](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/cli/repl.ts).
- Basis: first-party code wiring and offline mock-provider test suite.
- Confidence: high for construction; no live provider success claimed.
- Caveats: unsafe shell/file effects can occur if the configured model chooses them, since shipped tools have no action-approval gate; this is not independent S5 authority.

## S2 — Coordination

- State: —
- Function: no inter-S1 conflict-attenuation function is installed for independent operating cells.
- Disturbance / variety regulated: conflicting independent coding agents are not instantiated by the shipped runtime; concurrent processes can each act on one workspace without operational cross-agent coordination.
- Decisive decision or feedback right: the model serially dispatches multiple *tool calls* and `session.ts` serializes writers to one JSONL file, but neither arbitrates competing independent S1 decisions or overlapping code modifications.
- Decision owner: one S1 model; fixed session locking code controls storage integrity only.
- Supporting / enforcement mechanisms: `agentTurn` serial call loop and `.ti/sessions/*.jsonl.lock` file guard.
- Closure path: one model → one or more sequential tool effects → feedback to the same model; a separate competing S1 → conflict observation → cross-S1 response → revised operations path is absent.
- Why this is / is not agent-owned: several tools or concurrent independent terminal processes are not a distributed team of S1 agents whose interference is moderated by ti.
- Evidence: [loop](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/agent.ts), [session persistence](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/session.ts), [four-tool registry](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/tools/index.ts).
- Basis: checked complete shipped tool roster and file lock purpose.
- Confidence: high for the pinned single-agent product.
- Caveats: a separate orchestrator could build multiple ti instances; that integration is not shipped here.

### Absence scope

- Surfaces inspected: runtime orchestration entry, all registered tools, session lock, provider switch and REPL dispatch.
- Plausible first-party paths checked: multiple tool calls as multiple S1s, several provider configurations as cooperating workers, concurrent session locks as work arbitration, user-authored skills as independent agents.
- Why no material first-party path remains: the observed system has one decision loop and a tool/file-state lock, without shared tasks, agent claims, dependency ownership or cross-agent corrective return.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current management institution over multiple independently acting operating units is evidenced.
- Disturbance / variety regulated: interruption, long context and provider setup disturb one task/session only, not a supervised population of S1 activity.
- Decisive decision or feedback right: a user can stop one active agent turn and select its provider; `repl.ts` queues input and caps context, not a system-wide resource/reprioritization mandate.
- Decision owner: the attending operator for session controls, one model for task-local decisions and fixed REPL mechanics.
- Supporting / enforcement mechanisms: TUI key handlers, turn AbortController, `/model`, `/provider`, `/resume`, and auto-compaction thresholds.
- Closure path: session interruption or command → current turn stops/config changes → one S1 continuation; no full-current portfolio view and selective intervention over multiple S1s.
- Why this is / is not agent-owned: tactical model/provider choice, context summarization and interruption do not jointly constitute S3 decision ownership.
- Evidence: [REPL](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/cli/repl.ts), [main](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/main.ts), [compaction](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/compact.ts).
- Basis: current-management decision trace inspection.
- Confidence: high within the declared product scope.
- Caveats: a human operator has ordinary control over the app but not a shipped whole-current management console.

### Absence scope

- Surfaces inspected: TUI, REPL, provider config, session persistence, context compression and agent loop.
- Plausible first-party paths checked: turn cancellation as supervisory intervention, multiple saved sessions as a managed portfolio, model picker as staffing, and context compaction as planning.
- Why no material first-party path remains: no independently operating team or control plane with a cross-S1 status view and operational rerouting is built into ti.

## S3* — Complementary audit

- State: —
- Function: no independent reviewer/auditor observes operational claims and returns actionable findings to a separate controller.
- Disturbance / variety regulated: incorrect generated code may escape the single model's tool-feedback verification, but no specialized complementary review owner is instantiated.
- Decisive decision or feedback right: the model may itself run tests using `bash` under its ordinary instructions; repository test files validate the product as development fixtures, not generated work via an independent runtime auditor.
- Decision owner: same S1 model for task testing and user for manual inspection.
- Supporting / enforcement mechanisms: prompt guideline to build/test, tool error feedback, mock test suite, stream/truncation guards.
- Closure path: tool result → same model decides whether repair is needed; no independent audit verdict → management acceptance/rejection → corrective loop exists.
- Why this is / is not agent-owned: self-testing and handling stream/tool errors are normal S1 execution support, not complementary operational audit.
- Evidence: [prompt](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/prompt.ts), [tools](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/tools/index.ts), [main](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/main.ts).
- Basis: tool roster, prompts and invocation graph checked.
- Confidence: high for absence in shipped runtime.
- Caveats: a user can engage an external reviewer independently, outside this assessed distribution.

### Absence scope

- Surfaces inspected: prompt, tool registration, REPL, runtime session state, developer tests and interruption paths.
- Plausible first-party paths checked: model self-verification as separate auditor, unit tests as S3* institution, user checking output as installed complementary regulator.
- Why no material first-party path remains: none provides a distinct auditor owner and independent claim-testing channel wired to the operating task's acceptance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective capability choice and adopted organizational adaptation cycle is shown.
- Disturbance / variety regulated: future task variety and provider/ecosystem change exist, but are not converted into a deliberate internal capability strategy by ti.
- Decisive decision or feedback right: local skills are operator-provided and discovered at startup; the model selects their existing text for a current task; `ti update` mechanically fetches and installs *maintainer-released latest*, only after explicit user command.
- Decision owner: upstream maintainer for new version contents and user for update invocation; no ti-internal prospective strategic decision owner.
- Supporting / enforcement mechanisms: `loadSkills`, `readSkillBody`, `runCompact`, `fetchLatest`, `updatePlan` and `runInstall`.
- Closure path: old messages → same-task summary; existing skill → same-task instruction; command `ti update` → latest package version chosen externally. No environment assessment → strategy/capability design choice → adoption → future feedback loop exists within the active harness.
- Why this is / is not agent-owned: context survival and routine package lifecycle maintenance do not select *which* new capability to develop/adopt in response to future environmental distinctions.
- Evidence: [skills](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/skills.ts), [compaction](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/compact.ts), [updater](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/cli/update.ts).
- Basis: all plausible future-directed installed controls inspected.
- Confidence: medium-high: software updating is a real future-version change but lacks internal strategic capability selection.
- Caveats: this assessment does not deny that software updates can expand capabilities; it denies that a first-party S4 policy choosing and learning from prospective options was demonstrated.

### Absence scope

- Surfaces inspected: skill discovery, context summarization, session persistence, provider setup and official-registry package update.
- Plausible first-party paths checked: latest-version polling as sensing, installation as adaptation, skill loading as an evolving repertoire, accumulated session history as organizational memory.
- Why no material first-party path remains: version selection is fixed to maintainer's latest release upon user request, while skills and summaries supply existing/current-task knowledge without prospective agent-owned capability design and evaluation.

## S5 — Policy and identity

- State: —
- Function: no separate legitimate ultimate-policy or identity authority is instantiated for the assessed operational agent.
- Disturbance / variety regulated: conflicting goals, foundational purpose changes or legitimacy disputes are not governed by an in-product constitutional decision cycle.
- Decisive decision or feedback right: the provider/settings chooser sets tactical operation details, while prompt role text is static and tools execute directly without a first-party approval mechanism.
- Decision owner: external operator and source maintainer; no integrated runtime identity-policy body.
- Supporting / enforcement mechanisms: static `buildSystemPrompt`, local config file and CLI settings; project/user-provided `AGENTS.md` or `CLAUDE.md` text is appended as instructions.
- Closure path: setup and local instructions influence one S1's task; no explicit ultimate-policy challenge → legitimate S5 ruling → binding organizational return is instantiated.
- Why this is / is not agent-owned: user sovereignty, source maintainership, instructions and configuration do not alone prove a first-party ultimate-identity deliberation function.
- Evidence: [prompt](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/core/prompt.ts), [config](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/config/index.ts), [tools](https://github.com/tmjwjx/ti/blob/68cd5bceff33aef1dd95fddc8ad955557481a162/src/tools/index.ts).
- Basis: runtime identity and authority surfaces checked.
- Confidence: high within this recursion.
- Caveats: project-level instructions can constrain a task, but their authoring/governance is outside ti.

### Absence scope

- Surfaces inspected: initialization prompt, tool definitions, provider settings, user/project instruction injection and maintainer design docs.
- Plausible first-party paths checked: developer role prompt as constitution, external AGENTS.md as embedded S5, user command settings as governance and package maintainers as local policy authority.
- Why no material first-party path remains: these are static instructions or external ownership choices; none delivers an independent constitutional decision-and-return cycle inside ti.

## Distributed OSS parent arrangement

The GitHub project and public npm distribution establish code and version provenance. Maintainer publication, user package updates and local task operation are not an integrated recursive parent that governs multiple ti S1 units in one organizational circuit.

## Self-hosted and non-human modes

The model acts autonomously at S1 within a local terminal session. Automated compaction, tool-call continuation and serialized stream handling do not instantiate an independent supervisor, reviewer or prospective strategy owner.

## Recursion

One model-backed terminal-agent work cell owns the session. Four tools are subordinate effects and the interchangeable provider models are substitutes for that cell; other independently launched ti processes are external installations, not coordinated first-party subsystems.

## Variety and escalation

Tool errors, stream failures and aborted operations become current-turn feedback or termination. Persistent JSONL state and summarization preserve conversational information; package updates and provider selection require operator action. No first-party escalation to a separate S2/S3/S3*/S4/S5 owner is observed.

## Evidence gaps

- Source pinned at `68cd5bceff33aef1dd95fddc8ad955557481a162`, `@tmjwjx/ti` 0.0.10. `npm test` PASS: **16/16 Node test files**, run using fixture SSE and fake `fetch`; `npm run check` (`tsc --noEmit`) PASS on Node 24.19.0. `npm ci --ignore-scripts` installed only dev dependencies; upstream Git checkout remained clean.
- The upstream architecture expressly lists subagents, plan mode, MCP and permission prompts as unimplemented/non-goals. The code and four-tool registry were independently checked, not solely the documentation.
- No real model API/agent task was invoked; these tests establish executable code mechanics, not task success or any behavioral-quality metric.
- Negative ownership findings are local to this exact standard distribution; they do not preclude a separately authored multi-agent orchestrator or user-managed development organization outside it.
