---
harness_id: polycode
project_name: polycode
repository: https://github.com/gasantiago16/polycode
review_ref: ed4b4be63921261534ac932817e863399274a888
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# polycode

## Review boundary

- System in focus: the first-party locally operated polycode TypeScript coding harness in its supported experimental-alpha CLI/TUI distribution, including optional task subagents, graph/workflow/team commands and attached human dashboard.
- Purpose and identity: fulfill repository-aware development tasks through provider-independent model/tool loops, independently acting depth-one child agents, local execution and optional supervised worktree/application modes.
- Relevant environment: project files/Git state, code/test output, overlapping child write attempts, model/provider output, human permissions, config and external MCP/web inputs.
- Standard-distribution boundary: locally cloned `pnpm` monorepo and private CLI/TUI package with `@polycode/core`, `tools`, `sandbox`, `providers`, `router`, `graph`, `workflows`, plugins, skills and session storage. Reused HTTP/SSE `server` engine is inspected as an optional development mode, but upstream explicitly warns hosted alpha is not a supported untrusted/multi-tenant deployment.
- Credited operating / distribution surfaces: `packages/cli/src/index.ts`, `packages/core/src/agent.ts`, `subagent.ts`, `permissions.ts`, `compact.ts`, `packages/tools/src/task.ts` and `task-ctl.ts`, `packages/sandbox/src/worktree.ts`, `packages/tui/src/app.tsx` and `dashboard.tsx`, `packages/workflows/src/runner.ts` and `team.ts`, `packages/graph/src/run.ts`, local tools, config/skills and permitted human controls.
- Adjacent first-party surfaces excluded from ownership: contributor issues, CI, TypeScript tests/mocks, generated HTML/docs, demo scripts, beta survey, test fixtures and unpublished future roadmap phases. External LLMs, hosted clients, MCP servers, cloud providers and independent repository maintainers are dependencies or neighboring systems rather than donated polycode owners.
- First-party operating / deployment modes considered: local model-driven coding and task-tool delegation; simultaneous depth-one children; automatically isolated same-turn writable siblings; interactive `/team`, `/graph`, `/workflow`, `/review` and `/dashboard`; optional explicit Git worktrees and manual apply; operator approval/permission profiles; graph checkpoints and session/history; experimental HTTP server without first-party organization-level governance.
- Recursion level: one developer-operated polycode workstation/session with its local child coding cells; not the project maintainer organization or an external team's full lifecycle.
- Reviewed revision: `ed4b4be63921261534ac932817e863399274a888` (batch #996 frozen row 10).
- License screen: root `LICENSE` grants MIT; `README.md` says private not-yet-npm-published experimental alpha and explicitly warns against untrusted hosted exposure.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

polycode's `Agent` drives a canonical provider stream, accepts model-selected tool calls, applies permission/hook gates, executes tools, appends paired results and continues. Real child `Agent` instances have separate conversation histories, role-limited tools, bounded depth and optional background lifetimes. Parent and children may use one workspace or detached Git worktrees; task batches can execute concurrently. A first-party guard rewrites two-or-more same-turn `task` requests involving writers to request worktree isolation, and the actual child spawn creates those worktrees or fails rather than quietly using the parent. This attenuates a specific shared-file collision class, although there is no autonomous semantic conflict arbitration or automatic merging of child branches.

The parent model can use `task_wait` to inspect a full current roster and `task_kill` to terminate a selected running child; the attended TUI dashboard separately presents the same roster, live peek and a human-selected `x` stop. These are two independently reachable first-party current-control modes with different decisive owners. The optional `/review` path extracts real Git status/diff and starts a fresh `review` child with a restricted tool set and write jail to `.polycode/reviews/`. Its findings are reported to the user; they are not automatically enforced or fed into another correcting worker. The `/team` workflow runs two read-only explorers, one isolated implementer and one reviewer in an ordered scaffold, but the reviewer prompt relies on passed descriptions/outputs and cannot be credited with seeing the implementer's isolated artifacts absent further source access.

Optional model/heuristic routing selects a provider tier for the current request; context compaction, project memory, skill/plugin loading and checkpointed graph traversal help current work. They are not a first-party prospective capability-adaptation decision loop. Local tool approval and server auth/rate limits are constraints rather than an identity-governing S5 body.

Frozen primary evidence: [agent.ts](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.ts), [task-ctl.ts](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tools/src/task-ctl.ts), [dashboard.tsx](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tui/src/dashboard.tsx), [TUI app](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tui/src/app.tsx), [worktree.ts](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/sandbox/src/worktree.ts), [subagent.ts](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/subagent.ts), [team.ts](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/workflows/src/team.ts).

## Operational model

The primary agent and its separately invoked depth-one child model loops each make task-local decisions. In the normal coding mode, the provider chooses tools, handles compiler/Git output and resolves the user task (S1=A). When siblings are launched from one model turn, the deterministic worktree reservation/isolation path prevents direct simultaneous mutation of the same project tree (S2=C). In the parent control mode, the primary model can inspect and selectively stop current child commitments using `task_wait` and `task_kill` (S3=A); an attended human operator can do the same from a roster UI with `x` (S3=P), so S3=A(P) denotes two alternate modes, not shared simultaneous ultimate control. The optional fresh review child supplies a specific but user-composed complementary audit constructor (S3*=C). No shipped outside-and-future adaptation or ultimate identity-policy loop is established (S4/S5=—).

## S1 — Operations

- State: A
- Function: generate and revise local software solutions through model-directed commands, edits, test runs, search and optionally independently delegated coding cells.
- Disturbance / variety regulated: changing task details, source state, tool/test failures, provider output, reviewer/child reports and ordinary execution errors.
- Decisive decision or feedback right: primary and child models select code/tool actions and their next steps after observations; the runtime transports, checks and executes those calls.
- Decision owner: current configured provider-backed `Agent`; each spawned child owns its own bounded operational loop.
- Supporting / enforcement mechanisms: canonical adapters, `ToolSpec` execution, permission/hook gates, sandboxes, compaction, session store, router and model/tool stream event transport.
- Closure path: task + environment context → model tool selections → actual sandbox result or denial → canonical tool-result messages → next model decisions or final result.
- Boundary reachability: private CLI instantiates `Agent`, the local TUI drives it, `task` invokes `Agent.spawnChild`, and graph/workflow/CLI routes directly call that same first-party child constructor.
- Why this is / is not agent-owned: a fixed runtime can carry out specified operations but cannot choose the implementation and next repair from changing model/tool observations without the model owner.
- Evidence: [Agent loop](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.ts), [CLI](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/cli/src/index.ts), [task tool](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tools/src/task.ts), [agent tests](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.test.ts).
- Basis: explicit shipped source and deterministic provider/script tests.
- Confidence: high for construction; not a live model-quality measurement.
- Caveats: no live LLM inference, external MCP behavior or real full project improvements were performed for this assessment.

## S2 — Coordination

- State: C
- Function: attenuate shared-workspace modification conflicts arising from two or more separately deciding writable child agents launched in one parent model turn.
- Disturbance / variety regulated: siblings otherwise mutating overlapping files in the same parent Git tree while concurrently implementing separate subtasks.
- Decisive decision or feedback right: fixed same-turn task-batch detection stamps writable child calls with `isolation: worktree`, and `spawnChild` creates independent Git worktrees; failures return explicit errors instead of silently executing against the shared parent.
- Decision owner: deterministic first-party batch/isolation logic for the coordination choice, not a model-owned negotiation; parent model chooses tasks and later sees execution outcomes.
- Supporting / enforcement mechanisms: `stampParallelTaskWorktrees`, `canRunParallel`, worktree sandbox creation, write permissions, tool error results, detached worktree copies and manual `/worktree apply`.
- Closure path: multiple requested writable child actions → classify as collision-prone batch → force separate Git tree per writer → each independent child operates on its own files → isolation/result/failure returns to the parent; later application to the main tree remains manual.
- Boundary reachability: `Agent.run` invokes the stamping guard on emitted tool calls before tool dispatch; the local CLI provides `openWorktree`, and native tests explicitly assert two writing calls are auto-isolated.
- Why this is / is not agent-owned: the interference-specific rule is a shipped S2 constructor and has a concrete effect on children, but fixed stamping and worktree creation do not independently decide how to reconcile divergent patch semantics; thus C, bounded to the same-turn class, not A.
- Evidence: [parallel stamping and dispatch](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.ts), [worktree creation and apply](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/sandbox/src/worktree.ts), [autostamp test](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.test.ts).
- Basis: explicit source-level interference guard, native mock two-writer test and executable sandbox wiring.
- Confidence: high for bounded constructor; no evidence of general conflict merging.
- Caveats: separate background turns, explicit shared-tree children, manual worktree application and file conflicts across otherwise isolated branches are outside the proven automatic damping path.
- Distinct S1 units: two model-backed depth-one general children, each executing its own `Agent` loop.
- Inter-S1 disturbance: simultaneous or overlapping writable edits targeting the same parent repository tree.
- Attenuating coordination relation: deterministic same-batch detection and forced detached-worktree isolation for each writing child.
- Feedback into subsequent S1 behaviour: child tool execution takes place against separate sandboxes, and success/failure/worktree location flows back into the parent model's tool results, changing where later child changes may be applied.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code branches on a concrete concurrent-writer collision class and changes filesystem isolation, not just message passing or worker creation.

## S3 — Inside-and-now control

- State: A(P)
- Function: monitor and selectively intervene in the currently running population of child coding commitments within one session.
- Disturbance / variety regulated: long-running, stale, conflicting-priority, unnecessary or failed child work that continues to consume the present team's attention and work slots.
- Decisive decision or feedback right: in model mode, parent `Agent` receives the current roster via `task_wait` and may call `task_kill` on a selected child; in human mode, the TUI dashboard lists current children and lets the operator peek and stop one by id.
- Decision owner: model-backed parent Agent in the autonomous mode; attending local user in the alternate parent-governed dashboard mode.
- Supporting / enforcement mechanisms: `children` runtime map, status/elapsed output, `listChildren`, `peekChild`, `killChild` AbortController, `task_wait`/`task_kill` ToolSpecs, TUI polling and Ctrl+B detachment. The fixed max-eight-child cap itself is enforcement, not discretionary S3.
- Closure path: current roster/status → model or operator chooses a particular running child → abort/stop call changes that child's active commitment → updated status/result becomes visible for subsequent parent operation. This is bounded to selective interruption, not full financial/resource planning.
- Boundary reachability: `Agent.run` injects `waitChild`/`killChild` into the parent-only ToolContext and exposes their tools to the model; `app.tsx` mounts `Dashboard` via `/dashboard` and wires `onKill` to the same `Agent.killChild`. Local interactive mode offers both alternatives without external infrastructure.
- Why this is / is not agent-owned: the parent model can choose an intervention from the observed whole-current roster, while the tool merely enforces the selected abort. The attended UI mode instead delegates the same discretionary intervention to the human operator; neither a child-count cap nor the view alone is counted.
- Evidence: [Agent roster/control](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/agent.ts), [parent tools](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tools/src/task-ctl.ts), [dashboard UI](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tui/src/dashboard.tsx), [TUI binding](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tui/src/app.tsx).
- Basis: runtime source and deterministic child/dashboard tests; no claim that a live model successfully optimizes whole-team operations.
- Confidence: medium-high for the narrow first-party selective-stop modes.
- Caveats: `attach` displays output rather than joining the child's context; no automatic negotiation or broad resource reprioritization is proven. The model may require a tactical permission approval for `task_kill` under restrictive modes.
- Whole-system current view: `task_wait` without an id lists the entire session child roster, including state and elapsed time; dashboard renders `listChildren` with live status and selected-child peek.
- Current-control decision scope: select and terminate a particular child commitment via `task_kill` or dashboard `x`, then revise the remaining session work.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Parent model/Agent | Inspect complete live child roster with `task_wait`, decide a child is no longer needed | Selective `task_kill` → `Agent.killChild` aborts child; status/result returns in future model context | `packages/tools/src/task-ctl.ts`, `packages/core/src/agent.ts` |
| Parent (`P`) | Attending local operator | Open `/dashboard`, examine child roster and live peek | Operator selects `x` → `onKill` calls `Agent.killChild`; dashboard refresh shows changed commitment | `packages/tui/src/dashboard.tsx`, `packages/tui/src/app.tsx` |

## S3* — Complementary audit

- State: C
- Function: conduct a separately prompted critical examination of proposed code changes through an optional fresh-context review child.
- Disturbance / variety regulated: latent bugs or incorrect changes surviving the original coding model's routine command/test feedback.
- Decisive decision or feedback right: a separate `review` child is given the Git diff and can produce structured `APPROVE`/`REJECT` and issue findings; the operator decides how to respond. The review is not an automatic veto or enforced corrective loop.
- Decision owner: independently invoked review model for substantive critique, with optional human follow-through; the runtime controls file access and parses an advisory verdict.
- Supporting / enforcement mechanisms: `collectGitDiff` obtains direct status/`git diff HEAD` evidence, `toolsForChild('review')` limits tools and jails writes to `.polycode/reviews/`, and the TUI shows the report/verdict.
- Closure path: optional `/review` → fresh child with real change evidence → audit note/file and returned summary → human or manually composed next coding operation. No first-party automatic obligation consumes findings and changes operational control.
- Boundary reachability: `/review`/`/cranky` calls `Agent.spawnChild` in ordinary local TUI; the separately accessible `review` child role is exposed by `subagent.ts`. The `/team` workflow also composes a reviewer after an isolated implementer, but that workflow's descriptions alone are not counted as direct inspection of its detached worktree.
- Why this is / is not agent-owned: the separate model can decide the review judgment without inheriting the generator's conversation, but first-party closed correction is not established, so this is a bounded independent-audit constructor C rather than autonomous A.
- Evidence: [fresh review child and diff acquisition](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/subagent.ts), [TUI review invocation](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/tui/src/app.tsx), [team scaffold](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/workflows/src/team.ts).
- Basis: explicit opt-in child model constructor and script-tested review type/permission handling, not live LLM outcome.
- Confidence: medium for independently prompted review possibility; no quality or audit-enforcement claim.
- Caveats: optional user invocation, shared base provider, review result not automatically routed to a current-control intervention; report parsing from returned text can be unknown if the child only writes the file.
- Claim being audited: correctness and potential defects of proposed repository changes.
- Ordinary reporting path: producing model's own tool results, tests, Git output and implementation summary.
- Complementary access path: fresh review child receives Git status and direct diff, may inspect source with read-only tools, and writes a restricted artifact.
- Independence boundary: distinct inference/context and role/tool policy from the producer's coding agent; not institutionally independent or necessarily a different model/provider.
- Who acts on findings: user/parent may manually take up a defect; no first-party mandatory finding→repair completion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no completed externally prospective cycle for selecting and adopting changes to polycode's own future operating capabilities is evidenced.
- Disturbance / variety regulated: provider churn, new development practices and future task demands could prompt strategic adaptation, but shipped mechanisms primarily service the current request.
- Decisive decision or feedback right: no first-party S4 owner selects future capability alternatives and returns an adopted architecture/capability change.
- Decision owner: current model/router selects response approach or present provider tier; operator configures providers, plugins, skills, memory and modes.
- Supporting / enforcement mechanisms: heuristic/model-driven router, tool plugins, skill discovery, `deep-research` workflows, graph checkpoints, memory and context compaction.
- Closure path: external research and model selection feed the current coding/research task; no outside-and-future scan → changed capability options → adoption decision → changed ongoing polycode capability circuit.
- Why this is / is not agent-owned: selecting a cheaper model for this turn or researching a user-specified topic is operational service, not a prospective adaptation right over the harness.
- Evidence: [router](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/router/src/index.ts), [context/memory](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/context.ts), [graph runtime](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/graph/src/run.ts), [deep research](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/workflows/src/deep-research.ts).
- Basis: inspected first-party capability and planning paths.
- Confidence: medium-high for the supported workstation boundary.
- Caveats: an external team could ask polycode to develop its own future capabilities, but that is not a shipped S4 function at this recursion.

### Absence scope

- Surfaces inspected: model/heuristic routing, context/compaction, memory, graph/workflow/checkpoint state, research/review commands, plugin/skill loading, operator settings and maintainer roadmaps.
- Plausible first-party paths checked: model-driven router as strategy, retained memory as organizational learning, `deep-research` as external future scanning, plugins/skills as adaptation choices and graph resume as longitudinal capability revision.
- Why no material first-party path remains: routes handle present tasks or user-configured tool availability, and none forms an owned external-prospective adaptation judgment with a return changing the continuing organization.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy adjudication and governing return is completed for the local coding organization.
- Disturbance / variety regulated: ultimate purpose, legitimate tradeoffs and organizational identity are not decided through a higher governing loop in the shipped runtime.
- Decisive decision or feedback right: none shown at identity level; model/user choose tactical tools and modes, and fixed rules constrain particular actions.
- Decision owner: human operator for session/tool permissions and configuration; upstream maintainers for adjacent product development, not a shipped S5 system.
- Supporting / enforcement mechanisms: `plan`/`ask`/`acceptEdits`/`yolo` modes, path protections, hook denials, provider catalog, local/hosted authentication and rate limiting.
- Closure path: local permissions and remote bearer auth can deny an action/request; there is no ultimate-policy question → legitimate S5 authority → returned identity-level policy decision regulating future operations.
- Why this is / is not agent-owned: safety/classification and human confirmation are action-level gates; neither parent S5 nor agent S5 is established from them.
- Evidence: [permissions](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/core/src/permissions.ts), [CLI profile/config](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/cli/src/index.ts), [server auth](https://github.com/gasantiago16/polycode/blob/ed4b4be63921261534ac932817e863399274a888/packages/server/src/index.ts).
- Basis: traced supported permissions/approval and hosted-configuration paths.
- Confidence: medium-high.
- Caveats: the public product's security limits are important but do not establish an ultimate identity-governing organization.

### Absence scope

- Surfaces inspected: permission engine, rule patterns, path protections, hooks, UI approval choices, model/route config, server auth/rate limits, source project policy and roadmap.
- Plausible first-party paths checked: operator approvals as parent S5, hosted authentication as identity authority, plugin policies as self-governance, maintainer roadmap as operational governing S5.
- Why no material first-party path remains: those surfaces implement tactical permission/security or an adjacent developer process; there is no complete supported identity issue and authoritative return into the assessed local session.

## Distributed OSS parent arrangement

The public project can have maintainers and contributors, but the assessment does not credit their repository/CI workflows as a shared distributed metasystem governing independently installed local polycode agents. The attended dashboard P mode is one local session's parent, not project-level governance.

## Self-hosted and non-human modes

The local operator can view/stop child work via a first-party dashboard (bounded S3=P) while the parent model has its own `task_wait/task_kill` route (bounded S3=A). Those alternative modes justify S3=A(P), not a claim that both make the same decision. An experimental HTTP server reuses the agent engine but has separate authentication/config boundaries; it does not add a proven independent S4/S5 parent mode.

## Recursion

Primary coding and depth-one children are operational units in one first-party local system. A child may have its own sandbox/worktree; spawning and graph nodes alone are not a second full VSM metasystem. Independent code reviewers, organizational maintainers and external endpoints are evaluated only where operationally wired into the declared session.

## Variety and escalation

Tool and test feedback supports operational repair. Bounded S2 worktree isolation prevents same-batch shared-tree interference but leaves branch integration manual. Bounded S3 model/operator intervention can stop a selected child. The fresh reviewer produces advisory findings, not an automatic merge veto; none of these statuses or retries is independently asserted to be an algedonic identity-policy circuit.

## Evidence gaps

- Frozen source `ed4b4be6`: `pnpm` lockfile installation, **314/314 native Vitest tests PASS** across 42 files, and TypeScript `tsc --noEmit` PASS. Six loopback HTTP test cases failed initially under a socket-restricted sandbox (`listen EPERM 127.0.0.1`); the complete suite passed with local loopback access permitted. No live LLM/provider requests were made.
- Positive S2 is restricted to the structurally protected same-turn set of writable siblings; external Git merge correctness and other concurrent modes were not measured.
- Positive S3 model ownership rests on explicit `task_wait`→model→`task_kill` executable composition and human ownership on dashboard→`x`→abort; no real-provider intervention-quality experiment was performed.
- S3* denotes an optional independent review constructor, not a proved successful real-model audit or automatic corrective loop. The separate `/team` review may receive descriptions without the isolated implementer's actual new files; it is not promoted to stronger evidence than the direct `/review` diff path.
