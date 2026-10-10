---
harness_id: radiant
project_name: Radiant
repository: https://github.com/templetongroup/radiant
review_ref: 1186d16d2c08bb45a7fa489dcce8dc74e73e7eba
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Radiant

## Review boundary

- System in focus: the shipped Radiant **local coding-agent harness** with first-party JS service model/tool loop, server tool/approval controls, native Loop step work/check/retry, and multi-session Graph executor, not an iOS chat frontend.
- Purpose and identity: modify and investigate project code using model-based file/shell tools; orchestrate bounded multi-step and multi-worker coding tasks with dependency and check feedback.
- Relevant environment: project working directory, source/test outputs, registered provider endpoints, task/loop/graph states, operator permissions and stored skills.
- Standard-distribution boundary: first-party server/index.js, server/providers.js, tools, Loop/Graph rules and run code, web client routes. External model APIs, MCP implementations, native browser extensions, project creator CI and promotional benchmark/demos do not own functions.
- Credited operating / distribution surfaces: server/providers.js runTurn, server/tools.js, server/index.js routes, server/loop-rules.js, server/graph-rules.js, server/graph-run.js, first-party skill proposal wiring.
- Adjacent first-party surfaces excluded from ownership: generic iOS/mobile assistant chat, third-party provider model intelligence, repo CI/development checks, external browser extension, cached model metadata and sample bench reports.
- First-party operating / deployment modes considered: ordinary project coding with actual read/write/edit/bash; Graph editor/manual or model-authored draft + user Run (parallel node sessions with data dependencies); Loop work, check by shell, optional independent agent check via checkAgentId and retry; Skillsmith after-turn procedural skill proposals; human approval gates.
- Recursion level: one project work organization supported by Radiant's native Graph/Loop; each actual coding-node/step agent session is an operational S1, not an arbitrary message or tool.
- Reviewed revision: 1186d16d2c08bb45a7fa489dcce8dc74e73e7eba.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Radiant ships a Node local server with first-party chat model/tool execution in runTurn. Authenticated local or cloud model providers choose actual file read/edit/write/shell calls; results enter the persistent agent session so later turns can react. User asks/auto approval, local project restrictions, budget guards and checkpoints support the operational path. This is independent of the iOS UI's general chat surfaces.

The Graph mode instantiates separate native agent sessions for graph nodes. A model can draft graph edges/steps and a human verifies the draft and presses Run; the scheduler runs nodes when all declared *actual input-read dependencies* finish, passes their output to the next node and allows unrelated units to work concurrently. This is a narrow construction of inter-S1 read-after-produce hazard attenuation. It is NOT automatic interference protection for two code writers both editing the same shared file.

The Loop mode drives one work step, an optional command check, and an optional model-based judgment. When checkAgentId selects an independent checker, the server opens a separate checking session whose prompt directs inspection of the actual user workspace; the checker returns a parsed PASS/FAIL. On FAIL the run returns that step to pending, and the next new work session receives the observed reason with instructions to fix only the failed step. Default same-session checker does not satisfy independence.

The after-turn Skillsmith can propose reusable skills from procedural history, for the user to approve; prospective S4 organizational adaptation authority remains unresolved. UI cards, graph drawing, task board, provider router and budget gates do not alone confer whole-current S3 or identity-policy S5.

Pinned first-party evidence: [server/providers.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/providers.js); [server/graph-run.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-run.js); [server/graph-rules.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-rules.js); [server/loop-rules.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/loop-rules.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [server/skillsmith.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/skillsmith.js).

## Operational model

Model-chosen tools and project observations close S1. With Graph, the model can propose per-node input dependencies but only a user-approved graph runs: S2 is a first-party compositional C-level path. Loop with an independent check-agent creates an actual complementary audit and corrective return. Deterministic scheduling/graph status alone is not discretionary S3, and retrospective skill proposals need further evidence for S4.

## S1 — Operations

- State: A
- Function: Coding operations on user's project through model-directed file/shell tools.
- Disturbance / variety regulated: Novel project state, requested file edits, tool errors, tests and previously unseen code.
- Decisive decision or feedback right: Choose next tool and code action in light of returned results.
- Decision owner: Native model-driven Radiant runTurn coding agent in the server.
- Supporting / enforcement mechanisms: First-party server/providers.js loop, tools.js file operations, authenticated model adapters, approval gates, checkpoint and terminal.
- Closure path: Coding request to runTurn → selected model tool calls → native file and shell tools invoked → observations returned into session → next model choice or final response.
- Boundary reachability: The shipped server/index.js chat/long-task routes call the owned runTurn engine with first-party tool definitions and real project working directory.
- Why this is / is not agent-owned: The agent chooses source-edit operations and adapts to tool results. The server enforces permission and provides execution, not third-party agent ownership.
- Evidence: [server/providers.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/providers.js); [server/tools.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/tools.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [server/checkpoints.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/checkpoints.js).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: External model inference and human approval constrain operations; success rate not inferred from README..


## S2 — Coordination

- State: C
- Function: Guard real inter-worker input-read hazards among separate graph-task S1 sessions.
- Disturbance / variety regulated: A child agent depending on output produced by another could operate on missing or incomplete upstream output, while independent nodes need not block.
- Decisive decision or feedback right: A graph's explicit dependsOn lists and route gates define which worker can start after upstream results, and which may run simultaneously; runtime enforces readiness. Model-authored graph draft is subject to user-run gate.
- Decision owner: First-party graph construction primitive composed through model-written draft and human launch; no always-on higher autonomous regulator for graph membership/edges after launch.
- Supporting / enforcement mechanisms: Graph node kind, model-authored dependency graph, cycle/shape checks, readiness/finished status, bounded parallelism, emitted output to dependent nodePrompt.
- Closure path: Producer work completes with recorded output → scheduler releases only dependent node with that output in its prompt → subsequent independent S1 worker makes decisions using complete upstream material; unrelated nodes can execute concurrently.
- Boundary reachability: Built-in /api/graphs/draft and /api/graphs/:id/run activate the actual first-party graph-run.js per-node runTurn executor; no external LangGraph needed.
- Why this is / is not agent-owned: The model may propose the inter-unit dependence choice through the native draft primitive; runtime enforces it. User review/Run remains the composition step, supporting C rather than attributing all coordination to autonomous A.
- Evidence: [server/graph-rules.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-rules.js); [server/graph-run.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-run.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: This narrow S2 candidate concerns actual cross-worker read-after-produce interference only, not ownership of worker scheduling as a whole. Interference in concurrent edits to a shared cwd is not regulated by graph waits alone..

- Distinct S1 units: Separate node sessions in first-party graph-run, each running its own model/tool turn on an assigned part of the project.
- Inter-S1 disturbance: Downstream readers acting before producer units finish would consume missing, stale, or partial generated work; excess false waits also suppress independent parallel execution.
- Attenuating coordination relation: Declared dependsOn data edges and optional model-authored draft are checked for valid acyclic dependencies, then node readiness gates dispatch and passes upstream result material into downstream prompts.
- Feedback into subsequent S1 behaviour: A producer result enters graph state; the dependent S1 starts only after its upstream unit finishes and receives that specific result inside its work prompt, changing its subsequent operational choices.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The specific inter-S1 read-before-produce hazard is explicitly distinguished from arbitrary ordering, and the first-party graph enforces real consumption-based wait edges and propagates producer completion/output to the next worker. Mere fan-out and display are not counted.


## S3 — Inside-and-now control

- State: ?
- Function: Possible whole-current management of task/graph state, but no conclusively distinct discretionary regulation of several ongoing operational commitments.
- Disturbance / variety regulated: Concurrent node failures, blockers, changing operational priorities and resource contention could demand whole-current intervention.
- Decisive decision or feedback right: Node status, retries, conditional routes, caps and task board are present; governing right to reassign active worker commitments during execution is not demonstrated.
- Decision owner: Possible graph author/model and user task-board owner, with deterministic graph executor; unclear who actually closes S3 rather than task plans.
- Supporting / enforcement mechanisms: Task board, event/status updates, graph-run state, route nodes, scheduling and model confidence/budget selectors.
- Closure path: Progress and conditional results drive subsequent node activation; however active-fleet reprioritization or resource reallocation based on whole-system current state is not evidenced sufficiently for a positive S3 claim.
- Why this is / is not agent-owned: Conditional routing and concurrency caps alone cannot establish separately owned S3; insufficient evidence for a strong absence either.
- Evidence: [server/graph-run.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-run.js); [server/graph-rules.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/graph-rules.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [src/components/TaskBoard.jsx](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/src/components/TaskBoard.jsx).
- Basis: structural + explicit.
- Confidence: medium for mechanisms, unknown for S3.
- Caveats: The source does not prove autonomous whole-system discretionary change of ongoing task obligations..


## S3* — Complementary audit

- State: A
- Function: Independent operational verification of a work unit against its declared check with corrective return when the result fails.
- Disturbance / variety regulated: A coding agent may complete a step incorrectly, falsely claim success, or fail specified tests.
- Decisive decision or feedback right: A separately selected check-agent model/agent independently inspects the workspace and judges actual step against explicit check criteria; the server reads its verdict and can return failure evidence to the next fresh worker attempt.
- Decision owner: Separate model-driven checker in supported Loop mode with configured checkAgentId; deterministic server transitions pass or retry based on its decision.
- Supporting / enforcement mechanisms: Check session creation, explicit checkPrompt telling reviewer to inspect, strict VERDICT parser, bounded attempts, failing step scope narrowing and optional shell checks.
- Closure path: Work agent modifies real code → independent check session and prompt in same workspace → verifier inspects work and returns PASS/FAIL → authoritative server parsing → failed step returns to pending with reason → new work session receives reason and attempts repair.
- Boundary reachability: Native server/index.js Loop /advance uses `sessionForStep(loop,step,'check')` when checkAgentId is set, and calls the model/session tool path. The Loop UI and public API are included in the shipped standard distribution.
- Why this is / is not agent-owned: The distinct checker model owns accept/reject judgment; server merely routes verdict to corrective work. In the same-session default check mode independent S3* is not claimed.
- Evidence: [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [server/loop-rules.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/loop-rules.js); [server/providers.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/providers.js).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: A configured independent checker uses model-provided criteria and tools; verification quality is not guaranteed and same-session check mode must be excluded..

- Claim being audited: Whether one coding Loop work-step actually meets its step-specific check, rather than the executing agent's self-reported success.
- Ordinary reporting path: The working session's text, generated files and tool/command output form the ordinary operational record of the step.
- Complementary access path: With checkAgentId, native sessionForStep generates a distinct check-session operating with access to the actual workspace and a different chosen checker agent; checkPrompt requires it to inspect the result, not trust the originating response.
- Independence boundary: A separate model session and check-agent identity with its own context and fresh request, unlike default checkAgentId-empty mode which reuses the worker's session; checker can read actual files and execute permitted checks.
- Who acts on findings: The server /advance Loop controller reads the checker VERDICT, records failure reason, moves step back to pending and starts a new work session whose workPrompt incorporates the specific failed-check reason, narrowing subsequent edits.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Potential creation of future reusable operating skills from observed work, but outside-and-then environment-facing adaptation authority is not established decisively.
- Disturbance / variety regulated: Repeating workflow demands and changed user procedures might warrant new skills that expand future task capabilities.
- Decisive decision or feedback right: Skillsmith can identify reusable process from past turns and propose a SKILL for future use; final approval of skill and any future deployment is with the user.
- Decision owner: First-party model-based reflection proposes; human selects adoption. Whether this composes a complete first-party S4 parent mode is unresolved.
- Supporting / enforcement mechanisms: After-turn procedural reflection, skill proposals and review queue in Settings, persisted skills and opt-in selection.
- Closure path: Completed work → model proposes skill → user can accept for later use. The code does not conclusively show independent prospective environment scanning/option choice with return to current S1.
- Why this is / is not agent-owned: Procedural skill distillation goes beyond simple memory, but future organizational renewal is not proved by a user-approved retrospective proposal.
- Evidence: [server/skillsmith.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/skillsmith.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [server/config.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/config.js).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Not promoted to P or A(P) merely because a human can approve a skill; criterion-specific parent closure would need evidence..


## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy governance judgment with binding return at the coding organization boundary.
- Disturbance / variety regulated: Action permissions, spending caps and project role assignments constrain ordinary work, but do not regulate foundational purpose or identity disputes.
- Decisive decision or feedback right: No S5 ultimate-policy right evidenced.
- Decision owner: Operator configures approvals, provider selection and execution restrictions; tool security rules enforce these.
- Supporting / enforcement mechanisms: Command approval modes, sandbox guard, budgets, project rules and user-run gate.
- Closure path: Grant or deny each tool or graph Run; no higher constitutional issue → legitimate ultimate decision → organization-wide policy return loop is shown.
- Why this is / is not agent-owned: User consent and command security are not by themselves S5 ownership.
- Evidence: [server/tools.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/tools.js); [server/index.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/index.js); [server/config.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/config.js); [server/decide.js](https://github.com/templetongroup/radiant/blob/1186d16d2c08bb45a7fa489dcce8dc74e73e7eba/server/decide.js).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: External developer governance is outside the installed harness..

### Absence scope

- Surfaces inspected: Permission enforcement, sandbox and approval decision model, project/agent roles, task/graph execution modes and human launch gates.
- Plausible first-party paths checked: Project rules, user-model preferences, approval required/allow-all, tool restriction and budgets.
- Why no material first-party path remains: No first-party identity or ultimate-policy deliberation returns a governing policy choice to all subsequent operations; ordinary action gates only regulate an existing task.


## Distributed OSS parent arrangement

GitHub contributors, benchmark authors, native iOS app shipping and CI workflows are not first-party operating managers for the selected coding-agent project recursion. External providers and hardware model-fit decisions are supporting services, not decisive organizational owners.

## Self-hosted and non-human modes

The shipped server runs locally with user-selected model and project. Graph's local sessions execute as separate work cells, with human approval for graph Run and optional auto-approval for tools. Separate Loop checking is contingent on checkAgentId; no positive independence is inferred from a default same-session check.

## Recursion

The selected project can contain independent node coding operations in Graph and single-step coding operations in Loop. Their tool invocation is S1; their producer-consumer dependency policy supplies a narrow candidate S2, while multi-node labels and budgets by themselves are not meta-level whole-current S3 governance.

## Variety and escalation

A model performs code-edit work, Tool results inform it, and a command/test error may prompt correction. Loop’s configured independent checker can inspect the workspace and cause a bounded fresh remediation attempt with the reason passed in the prompt. Graph consumers only start when their real upstream inputs are ready; the runtime records failure/skipped states rather than assuming upstream succeeded. Skillsmith may propose a future procedure to the user but does not silently modify future strategy.

## Evidence gaps

- S2 C is limited to data dependency conflicts among graph workers; it is not a guarantee against concurrent writes, and the model draft requires user review/run.
- S3 unresolved: graph scheduling, status and dependency checks do not automatically establish whole-current discretion.
- S3* A requires separate checkAgentId and working independent check session; command-only and same-agent check modes do not donate audit independence.
- S4 unresolved: skills are proposed for future reuse, but prospective external-environment/capability-governance authority is not independently demonstrated.
- Classification is structural at frozen public source, not benchmark quality, reliability or iOS mode performance.
