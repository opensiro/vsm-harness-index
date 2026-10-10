---
harness_id: gnosis
project_name: Gnosis
repository: https://github.com/DOMCHURCH/Gnosis
review_ref: e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Gnosis

## Review boundary

- System in focus: shipped Gnosis TypeScript coding agent with native Engine model/tool loop, live multi-tab Engine sessions, communication anti-oscillation, read-only research subagents, verifier, goal-bar feedback and local memory.
- Purpose and identity: user-directed agentic coding and team research on a project with multiple models, independent active tab sessions and verification after file changes.
- Relevant environment: user repository and Git state, shell/files, model inference endpoint, human permissions, sibling tab communications, running task costs, retrospective session data.
- Standard-distribution boundary: Gnosis installed CLI/TUI/headless engine, first-party tab controller and exposed standard Goal Bar mode; external OpenRouter model internals and MCP servers are dependencies. The Three.js visual office is not an operational decision owner.
- Credited operating / distribution surfaces: src/engine.ts, src/tools/*, src/tabs.ts, src/system-prompt.ts, src/gitinfo.ts, src/sessionmemory.ts, bundled goal-review and communication features.
- Adjacent first-party surfaces excluded from ownership: office figures with decorative mode, marketing demos, remote acceptance service, CI/tests, external MCP providers, human organization and developer release process.
- First-party operating / deployment modes considered: normal CLI/headless coding; interactive multi-tab agent-to-agent communication; bounded parallel *read-only* subagents; default autoEval on file edits; Goal Bar with independent diff reviewer and correction routing; optional memory reuse; user permissions and model switching.
- Recursion level: a user project/coding organization using the first-party Gnosis multi-tab runtime. Each active tab Engine is a distinct lower-scope task-operating S1, with bounded read-only delegated research subagents.
- Reviewed revision: e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The first-party Engine streams model-generated tool calls, executes read, write, edit and shell with access checks, stores results in the message history, and can retry after own test/lint/LSP failures. Real tabs each own an Engine, history, model, directory, queue and task. TabsController moves agent-selected messages between independent tabs, prevents immediate replies, rejects a hop chain beyond three and caps inter-agent traffic to avoid repeated ping-pong. A distinct first-party research `task` tool launches scoped read-only subagents, including parallel subtasks whose outputs return to a top-level model; tool/nesting/budget limitations preserve scope.

Crucially, Gnosis has a separate verifier path: on changed files, runVerifier takes a Git diff and the original request; the judging Engine has a fresh session, no tools, and is blind to the generator's reasoning. Goal Bar review uses the same independent judgment style but queues FAIL feedback ahead of ordinary messages, leading to another coding turn until rounds run out. This is a source-native complementary audit and *not* a second model simply reading the coding agent's claimed summary. The normal automatic evaluation may merely report failure when autoFixOutcome is disabled, so the positive S3* feedback path is explicitly restricted to the Goal Bar or enabled fix-return mode.

Retrospective project/session pattern memory and the local permissions/user role prompt support the coding runtime without automatically establishing prospective S4 or ultimate-policy S5. The displayed office layout and decorative agents have no operating decision rights.

Primary pinned sources: [Engine](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts), [tabs](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tabs.ts), [task](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/task.ts), [diff](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/gitinfo.ts), [memory](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/sessionmemory.ts).

## Operational model

The main model controls file/task tool actions and can direct isolated researcher agents and real sibling tabs. The native tab controller enforces inter-agent loop guards and returns explicit denials as feedback; this is a C-level primitive for narrow communications oscillation attenuation, not a proven separate autonomous comprehensive S2 organization. The independent verifier's actual PASS/FAIL against the source diff may, in the shipped Goal Bar mode, steer subsequent code actions and closes a scoped S3*.

## S1 — Operations

- State: A
- Function: Execute a coding task via the first-party model/tool loop.
- Disturbance / variety regulated: Project file state, unexpected tool/test results, user requests, changing source.
- Decisive decision or feedback right: Choose next read/edit/write/bash action and update execution in response to observations.
- Decision owner: Main Gnosis Engine's model-based coding agent.
- Supporting / enforcement mechanisms: TypeScript tool registry, gates, Plan mode, shell, command normalization, persistent session and auto-checks.
- Closure path: Model emits a tool call → native gateAndExecute executes against the repository → tool result and test output return into model history → new operation or finish.
- Boundary reachability: Standard CLI/headless/TUI Engine directly runs the tool loop with owned write/edit/bash/read tool handlers.
- Why this is / is not agent-owned: The agent makes local coding choices. Provider calls and TypeScript gates are supporting execution.
- Evidence: [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts); [src/tools/index.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/index.ts); [src/tools/write.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/write.ts); [src/tools/bash.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/bash.ts); [src/headless.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/headless.ts).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: External OpenRouter inference is not credited as an owned organizational function. Human permissions can restrict operation..


## S2 — Coordination

- State: C
- Function: Attenuate actual inter-agent message ping-pong/recursive escalation between independent coding session units.
- Disturbance / variety regulated: Distinct live tab Engines can route replies cyclically, wasting turns and model quotas in a feedback oscillation.
- Decisive decision or feedback right: Native TabsController rejects immediate reply-to-sender, messages beyond three hops, and any over the session-wide message cap; autonomous tabs may adapt on refusal but no dedicated higher-order agentic coordination authority is composed.
- Decision owner: First-party deterministic inter-tab messaging primitive; composition of an autonomous inter-unit regulator is not a clearly separately owned role.
- Supporting / enforcement mechanisms: Typed inter-agent send_message/list_tabs, hop propagation through per-tab queues, message count, live tab controller, tab/session isolation.
- Closure path: One S1 emits a message to another → runtime checks sender/hops/count → accepted message starts recipient S1 turn or rejection is returned to sender model → sender can choose a different continuation; loops are bounded rather than fed back indefinitely.
- Boundary reachability: Native multi-tab TUI wires real independent Engine objects into TabsController and exposes send_message as an agent tool; not 3D desk decoration.
- Why this is / is not agent-owned: The deterministic anti-oscillation mechanism is first-party and real, but the higher coordination judgment is not independently assigned to an autonomous regulator; classification is C rather than A.
- Evidence: [src/tabs.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tabs.ts); [src/tools/tabs.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/tabs.ts); [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Inter-agent message caps and anti-reply safeguards are narrow communications-oscillation attenuation only; they do not establish global coordination quality. C requires externally composed decision ownership for broader autonomy..

- Distinct S1 units: Each independent live coding tab has its own Engine, model, task, history and message queue.
- Inter-S1 disturbance: Circular inter-agent replies amplify into uncontrolled messaging turns and token-cost oscillation across multiple tabs.
- Attenuating coordination relation: Native TabsController rejects same-turn replies to the sender, recursive message chains beyond three hops, and global traffic beyond twenty inter-agent messages per session.
- Feedback into subsequent S1 behaviour: A rejected send returns an explicit error as a tool result to the autonomous sender, allowing a different action, while accepted messages enqueue real next turns in receiving operating tabs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The guards specifically attenuate actual inter-tab circular-feedback oscillation with inter-unit loop suppression and explicit rejection return, not merely message delivery. The primitive is C-level, without a proved autonomous global coordinator.

## S3 — Inside-and-now control

- State: ?
- Function: Whole-current coordination across operating session/tab/subagent workloads is a candidate, but no adequately evidenced distinct owner/closure.
- Disturbance / variety regulated: Multiple active tasks, changing commitments, shared model spend and priorities compete during user coding work.
- Decisive decision or feedback right: Top-level LLM can split read-only subtasks, choose destinations, synthesize summaries and request budget; the role that reassigns active S1 commitments using a whole-current regulatory feedback view is not conclusive.
- Decision owner: Potential main coordinator agent combined with deterministic tab/coordination controller; present evidence cannot establish an independently complete S3 mode.
- Supporting / enforcement mechanisms: Per-tab busy/queue state, subagent fan-out, reservations, total cost, goal feedback, TUI agent directory.
- Closure path: Subtask outcomes and budget errors return to the caller, but inspected standard route does not prove autonomous whole-current reprioritization/reallocation of distinct ongoing S1 commitments.
- Why this is / is not agent-owned: Delegation, tab listings and budget reservations do not by themselves establish a distinct S3 feedback decision. The candidate is left ? rather than an unsupported positive or false absence.
- Evidence: [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts); [src/tabs.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tabs.ts); [src/tools/task.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/task.ts); [src/tools/tabs.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tools/tabs.ts).
- Basis: structural + explicit.
- Confidence: medium for mechanisms; indeterminate for S3.
- Caveats: Do not promote coordinator prompt or visual role map to S3 without direct management decision evidence..


## S3* — Complementary audit

- Claim being audited: Whether the coding agent's changes to source files actually fulfill the original request or active standing goal.
- Ordinary reporting path: The coding Engine's messages, recorded tool actions, tests and self-reported completion are the normal operational report.
- Complementary access path: Fresh first-party Git diff against the original request/goal is acquired outside the coding agent's account and given to a separate skeptical verifier Engine with no tools.
- Independence boundary: A new ephemeral verifier session, separate directive and model judgment, no inherited coder reasoning or conversation and no tool grants. Its available source evidence is strictly the original request and capped diff.
- Who acts on findings: Goal Bar uses TabsController.reviewGoal to enqueue a FAIL correction ahead of the coding tab's next turn; that autonomous coder then acts on the finding. Passive default automatic outcome reporting alone is not counted as corrective closure.

- State: A
- Function: Complementary independent audit of operational coding changes with a corrective return into the coding agent.
- Disturbance / variety regulated: An agent can produce wrong/incomplete changes or overclaim goal completion.
- Decisive decision or feedback right: A new no-tools read-only verifier Engine, blind to coder reasoning, judges original task/standing goal against freshly acquired Git diff and issues PASS/FAIL; failure feeds a corrective steer in Goal Bar mode.
- Decision owner: Separate model-based verifier subagent, first-party instantiated in standard Gnosis Engine; TabsController owns deterministic conveyance of correction.
- Supporting / enforcement mechanisms: gitDiff/gitDiffHead, VERIFIER_DIRECTIVE, isolated ephemeral session, 2-iteration cap, bounded rounds, optional autoFixOutcome and goal.review event.
- Closure path: Code edits → first-party gitDiff → separate prompt-blind verifier judges request/diff → FAIL returned to TabsController goal review → corrective message goes to same tab's priority queue → coder executes new turn toward goal.
- Boundary reachability: Standard Gnosis Engine.runGoalReview and TabsController.reviewGoal/runTurnWith implement an operational goal-bar mode; default automatic outcome evaluation also invokes verifier, and optional autoFixOutcome returns critique.
- Why this is / is not agent-owned: Independent judgement of objective request/diff belongs to the separate autonomous verifier; routing/round caps enforce its feedback but do not own audit judgment.
- Evidence: [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts); [src/tabs.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/tabs.ts); [src/gitinfo.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/gitinfo.ts); [src/config.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/config.ts).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Audit sees bounded Git diff, not all execution traces or independent live tests; PASS is not proof of correctness. Ordinary autoEval may require manually requested fix; positive feedback closure rests on active Goal Bar mode..


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environment-facing intelligence and capability-renewal decision demonstrated.
- Disturbance / variety regulated: New ecosystem opportunities/threats and future project changes would require strategic capability adaptation.
- Decisive decision or feedback right: No prospective adaptation right evidenced; learned memory distills past source edits and sessions for later context.
- Decision owner: No first-party S4 decision owner; memory summarization model has historical support function only.
- Supporting / enforcement mechanisms: Sessionmemory recordSession, patterns threshold, boot-time buildLearnedContext, model choice and persistence.
- Closure path: Past decisions/patterns → stored summaries → later system prompt. No outside-and-then options search or adaptation-governance return.
- Why this is / is not agent-owned: Learning historical preferences and switching models manually is not the future-facing, external-oriented S4 function.
- Evidence: [src/sessionmemory.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/sessionmemory.ts); [src/system-prompt.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/system-prompt.ts); [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts); [src/memory.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/memory.ts).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Other external user-authored workflows do not constitute the shipped first-party standard mode..

### Absence scope

- Surfaces inspected: Session memory ingestion/aggregation; prompt composition; model switching; tool wiring; scheduler and user instructions.
- Plausible first-party paths checked: Past-pattern distillation, recurring memory, model switches, scheduled work and user-led project edits.
- Why no material first-party path remains: No shipped first-party loop identifies prospective environmental change, autonomously develops adaptation options, decides renewal and returns a capability change to present operations.


## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy governance relation with legitimate final authority and returned closure.
- Disturbance / variety regulated: Approval for individual commands/tools and coordinator tasks is not an identity-policy constitutional decision.
- Decisive decision or feedback right: Human user may approve tool costs, risky actions or choose local model; no final policy judgment path shown.
- Decision owner: No first-party S5 decision owner at the selected operating recursion.
- Supporting / enforcement mechanisms: Permission gate, budget ceilings, read-only Plan mode, system prompt identity and no-recursive-subagent tool grants.
- Closure path: Action permission grants/denials affect the current tool, not an ultimate policy issue and organization-wide binding return.
- Why this is / is not agent-owned: Tool authorization and a coordinator identity prompt are not S5 despite having human governance adjacent to the runtime.
- Evidence: [src/permissions.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/permissions.ts); [src/system-prompt.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/system-prompt.ts); [src/engine.ts](https://github.com/DOMCHURCH/Gnosis/blob/e94a861bda5e35ee3a1e7df5afcc6a93a9162fbc/src/engine.ts).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Does not deny external human organization governance, which is beyond the owned runtime..

### Absence scope

- Surfaces inspected: Permission gate, identity/instruction prompt, tab manager, sub-agent tool grant rules, budget approvals.
- Plausible first-party paths checked: Human approvals, model selection, role assignment, auto updates, project AGENTS and developer CI.
- Why no material first-party path remains: No shipped first-party S5 ultimate-policy deliberation or legitimate parent authority path closing that decision into subsequent organizational rules at this system-in-focus.


## Distributed OSS parent arrangement

The public Gnosis maintainers, contributors, remote acceptance server and GitHub workflow do not own the installed project-level coding agent's organizational decisions. A person can authorize individual tools and choose goals/models, but these are not evidence of a separate parent-governed S5 mode.

## Self-hosted and non-human modes

Gnosis supports model switching during retained session history; actual model inference remains an external provider dependency. Genuine runtime tabs and read-only subagents are operating units, whereas decorative office figures are UI-only. The parent/human setting role does not donate autonomous S3/S4/S5 ownership.

## Recursion

One independent coding tab may be regarded as a local S1 within the multi-tab user-project organization; read-only task subagents handle lower-scope research operations. This does not mean every tab comes with an S2–S5 metasystem. S2 concerns bounded actual circular message interference, whereas S3 whole-current management is not inferred from tab plurality, budget limits or a coordinator role label.

## Variety and escalation

File edits and tests feed tool results to the coder. A Git-diff verifier can judge the resulting operational claim using a separate context; in Goal Bar mode its failure is queued as a corrective new coding turn. Independent tab messages are bounded by hop/loop limits. Cost reservations and human permission policies constrain resource use but are not automatically discretionary whole-current or ultimate-policy governance.

## Evidence gaps

- The S2 C claim is strictly about inter-tab message-loop attenuation, not resource/merge coordination or a comprehensive independent S2 regulator.
- S3 is marked `?` because the source has a coordinator role, multi-tab controls and shared budget, but the evidence reviewed does not conclusively establish a distinct whole-current decision authority and result-return loop; it is not silently promoted to A.
- S3* positive state relies on actual source diff, isolated verifier and *enabled Goal Bar* correction; passive default evaluation does not alone close a corrective loop.
- Sessionmemory records past patterns for future prompts; this is not evidence of environment-facing prospective strategic adaptation.
- This is a structural repository assessment at a pinned ref, not measured audit accuracy or task benchmark performance.
