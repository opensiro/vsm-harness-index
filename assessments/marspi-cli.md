---
harness_id: marspi-cli
project_name: Marspi CLI
repository: https://github.com/mars01pi/marspi-cli
review_ref: e8e46a39e9da2dac1444c175ad241f2cfa71c7dc
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Marspi CLI

## Review boundary

- System in focus: Marspi CLI's first-party terminal coding composition at frozen revision `e8e46a39e9da2dac1444c175ad241f2cfa71c7dc`, including the ordinary runner wiring, TUI/plain session flow, Loop Engineering engine, model routing, memory/skills/tool composition, and the CLI-visible Supervisor/DevFlow wrappers.
- Purpose and identity: provide an interactive coding assistant that can perform repository work through a ReAct-style model/tool loop and expose optional multi-agent coding/review workflows.
- Relevant environment: user goals and confirmations, repository/workspace files, shell/test results, model/provider responses, web-search/tool results, persistent session/memory state, and configured sibling runtime packages.
- Standard-distribution boundary: the frozen `marspi-cli` repository and the concrete first-party interfaces it invokes are assessed. The exact tree imports `github.com/mars/marspi-core` and `github.com/mars/marspi-graph` through local sibling `replace` directives at version `v0.0.0`; those sibling implementations are not revision-pinned by this frozen CLI and therefore cannot donate unobserved higher-system ownership or closure.
- Credited operating / distribution surfaces: normal TUI/plain coding runs, direct `Runner.Loop` invocation, Loop Engineering in `cmd/engine.go`, session/context persistence, Smart Routing selection, memory/skill/tool assembly, confirmation UI, and the concrete Supervisor/DevFlow integration contracts present in the frozen CLI.
- Adjacent first-party surfaces excluded from ownership: unpinned internal implementation details of sibling `marspi-core` and `marspi-graph` beyond interfaces concretely wired by this CLI; repository-development CI/tests/maintainer governance; README descriptions that refer to an older in-repository `internal/agent` layout not present in the frozen tree.
- First-party operating / deployment modes considered: ordinary TUI/plain ReAct coding, `/loop` three-actor Loop Engineering, experimental `/loopg`, `/sv` Supervisor and `/df` DevFlow commands, including their checkpoint/resume and HITL wrapper behavior where visible at this ref.
- Recursion level: a normal coding run or an individual Loop Engineering model context is an operational S1 cell; higher-function claims require relations among those cells or a separate metasystemic path rather than role names alone.
- Reviewed revision: `e8e46a39e9da2dac1444c175ad241f2cfa71c7dc`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The frozen CLI assembles a first-party coding application around `marspi-core` interfaces for the model provider, context manager, tool registry, prompt, memory, skills and `agent.Runner`. Ordinary TUI/plain paths route user input into `Runner.Loop`, persist context, and expose stop/compact/new-session controls. Smart Routing can choose among configured model tiers for the current task.

The repository also directly implements `/loop` Loop Engineering in `cmd/engine.go`: an Implementer receives the goal and writes code, a fresh Verifier context independently reads the changed files and runs tests, and on FAIL a fresh Updater context turns the verifier's diagnosis into a refined prompt that is appended back to the Implementer before the next iteration. PASS terminates the loop.

Experimental `/sv` Supervisor and `/df` DevFlow are concretely exposed by the CLI, with worker specs, HITL callbacks, SQLite graph checkpoints and resume/list surfaces, but their decisive graph/orchestrator algorithms live in the locally replaced sibling `marspi-graph`. Because `go.mod` does not pin a sibling revision, the frozen CLI alone does not reconstruct enough of that internal decision path to settle S3 ownership/closure.

## Operational model

In ordinary coding mode, user input enters a model/tool runner that can inspect and mutate the workspace, use tools and memory, receive concrete results and continue until completion or interruption. In Loop Engineering, the implementation and audit roles use separate context managers. The implementer is explicitly told not to run tests; the verifier directly inspects artifacts and executes tests, making its PASS/FAIL judgment a complementary path rather than a second reading of the implementer's final report.

## S1 — Operations

- State: A
- Function: perform coding and repository work through a model-driven tool feedback loop.
- Disturbance / variety regulated: heterogeneous codebases, incomplete context, file/search/shell outcomes, model outputs, tool failures, context limits, user goals and workspace safety constraints.
- Decisive decision or feedback right: choose the next investigation/edit/tool action, revise work from returned evidence, and decide when the requested coding result is complete.
- Decision owner: the active model-backed coding actor instantiated through the first-party runner composition.
- Supporting / enforcement mechanisms: `agent.Runner`, tool registry, context manager and persistence, prompt assembly, Smart Routing/provider adapter, memory/skill managers, TUI/plain session loop and user cancellation/confirmation surfaces.
- Closure path: user goal + session context → model chooses a coding/tool action → tool/runtime returns repository or execution evidence → evidence re-enters the model context → the actor chooses the next action until completion or bounded stop.
- Boundary reachability: ordinary TUI and plain modes call `a.runner.Loop` directly; `/loop` also instantiates repeated model-backed operational contexts through the same first-party runner interface.
- Why this is / is not agent-owned: removing the model actor leaves routing, persistence, tools and UI but removes open-ended coding decisions; deterministic/runtime components transport and constrain those decisions.
- Evidence: README; `cmd/root.go`; `cmd/repl.go`; `cmd/engine.go`; `go.mod`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the underlying runner implementation was split into the first-party sibling `marspi-core` and is not revision-pinned by this CLI ref; the positive finding relies on the frozen CLI's direct invocation contract plus its documented ReAct operating role, not on unpinned sibling internals.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes attenuation of a specific interference or oscillation among distinct S1 coding units.
- Disturbance / variety regulated: Loop Engineering sequences implementer, verifier and updater roles; Supervisor/DevFlow wrappers dispatch or sequence work and persist graph state, but the frozen CLI does not expose a concrete cross-S1 collision relation being damped.
- Decisive decision or feedback right: no S2-specific coordination decision over peer interference was established.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: fixed Loop Engineering sequencing, graph invocation, worker lists, checkpointing, HITL callbacks and workflow phase order.
- Closure path: these mechanisms route/delegate/audit work, but no evidenced coordination result specifically changes later S1 behavior to attenuate an identified inter-S1 disturbance.
- Why this is / is not agent-owned: multiple roles and a star topology do not by themselves establish S2.
- Evidence: README; `cmd/engine.go`; `cmd/engine_graph.go`; `cmd/engine_supervisor.go`; `cmd/engine_devflow.go`; `go.mod`.
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: unpinned `marspi-graph` internals are not used to infer hidden conflict-management behavior.

### Absence scope

- Surfaces inspected: ordinary runner composition, Loop Engineering, graph CodingLoop wrapper, Supervisor worker/HITL/checkpoint wrapper, DevFlow wrapper, session persistence, routing and TUI controls.
- Plausible first-party paths checked: three-agent loop as S2; Supervisor star topology as S2; DevFlow phase sequencing as S2; checkpoints/shared state as S2.
- Why no material first-party path remains: the frozen CLI surfaces demonstrate delegation, sequencing, audit and persistence but do not tie any first-party relation to a specific inter-S1 conflict/oscillation witness with a feedback path that attenuates it.

## S3 — Inside-and-now control

- State: ?
- Function: a plausible whole-current supervisory path exists through the experimental star-topology Supervisor, but the frozen CLI does not expose enough of its decisive algorithm to establish or defensibly exclude S3.
- Disturbance / variety regulated: the wrapper supplies a goal, worker roster, max steps, checkpoints, HITL gates and a result carrying `last_agent`; the hidden sibling orchestrator may regulate current worker commitments, but that cannot be reconstructed from the CLI ref alone.
- Decisive decision or feedback right: unresolved — the frozen wrapper does not show what state the supervisor model observes when choosing workers, what current resource/priority/commitment discretion it owns, or whether routing is only task decomposition.
- Decision owner: unresolved between a model-backed supervisor path and deterministic graph orchestration because `marspi-graph` is locally replaced but not revision-pinned.
- Supporting / enforcement mechanisms: `SupervisorConfig`, fixed worker specs, `MaxSteps`, coder HITL approval, SQLite checkpointer, resume/list UI and cancellation.
- Closure path: the wrapper shows supervisor invocation and returned graph state, but does not expose enough of the internal decision→worker→updated-whole-state loop to prove the Profile's S3 closure.
- Why this is / is not agent-owned: a component named Supervisor and dynamic worker handoff are insufficient; ownership remains unresolved without the pinned decision path.
- Evidence: README; `cmd/engine_supervisor.go`; `cmd/engine_supervisor_test.go`; `go.mod`.
- Basis: explicit wrapper evidence + unresolved revision provenance.
- Confidence: medium.
- Caveats: use `?`, not `—`, because a concrete first-party Supervisor integration is reachable and plausibly material, while the dependency revision needed to decide its organizational semantics is absent from the frozen CLI.

## S3* — Complementary audit

- State: A
- Function: independently challenge an Implementer's code claim by direct artifact inspection and tests, then feed failures into autonomous rework.
- Disturbance / variety regulated: the implementing actor may produce code that appears complete but fails tests, misses the goal or contains logic defects that its own self-report does not reveal.
- Decisive decision or feedback right: inspect changed files, select and run the appropriate test command, judge PASS/FAIL from actual test evidence and goal coverage, and return a failure diagnosis when needed.
- Decision owner: the separate model-backed Verifier context.
- Supporting / enforcement mechanisms: fresh verifier `agentctx.Manager`, changed-file extraction, read/grep/bash tools through the runner, explicit verifier prompt, deterministic loop sequencing, separate Updater context and iteration cap.
- Closure path: Implementer changes code and reports completion → fresh Verifier directly inspects changed artifacts and runs tests → PASS terminates the loop; FAIL → fresh Updater analyzes verifier evidence and generates a refined prompt → prompt is appended to the Implementer context → next implementation iteration → a fresh Verifier audits again.
- Boundary reachability: `/loop <goal>` is a shipped CLI command implemented directly in `cmd/engine.go`; no external reviewer product or custom composition is required.
- Why this is / is not agent-owned: removing the verifier model leaves deterministic sequencing but removes the independent semantic PASS/FAIL judgment and diagnosis; the audit decision is therefore agent-owned.
- Evidence: README; `cmd/engine.go`; `cmd/root.go`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the verifier uses the same provider/runner infrastructure as other roles, but it has a fresh context, a distinct role contract, direct repository/test access, and an explicit closed rework path.

- Claim being audited: the Implementer's changed code satisfies the user goal and is test-valid enough to accept.
- Ordinary reporting path: the Implementer's own `attempt_completion` result after editing/self-review.
- Complementary access path: the fresh Verifier independently reads changed files, inspects project test configuration and runs tests rather than relying on the Implementer's completion claim.
- Independence boundary: Implementer is explicitly told not to run tests; Verifier is a separately created context with an objective-verifier prompt and direct evidence access.
- Who acts on findings: on FAIL, a separate Updater model turns the verifier diagnosis into a refined prompt that returns to the Implementer; subsequent iterations are re-audited until PASS or the loop limit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: Smart Routing, long-term memory, web search, skills and context compaction can change how the current coding task is handled.
- Decisive decision or feedback right: no first-party path was found that models future/external change, develops adaptation options for the harness and returns a selected option into present organizational capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: routing scores/model tier selection, memory search/append, skills, web search, context compaction and provider configuration.
- Closure path: these mechanisms serve current-task execution or retain current experience; they do not close an outside-and-then adaptation conversation with current-control capability.
- Why this is / is not agent-owned: memory, task research and model routing are not S4 without a future/external option-generation loop.
- Evidence: README; `cmd/root.go`; provider/routing interfaces visible through the frozen composition.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: project-development evolution and sibling-repository roadmap work are adjacent and excluded.

### Absence scope

- Surfaces inspected: Smart Routing, memory/skills, web-search/tool claims, context compression, Loop Engineering, Supervisor/DevFlow wrappers and provider configuration.
- Plausible first-party paths checked: Smart Routing as adaptation; persistent memory as S4; web search as environmental intelligence; Updater as learning/adaptation.
- Why no material first-party path remains: every inspected path changes current-task execution or retries current implementation; none establishes prospective environmental distinctions, adaptation-option generation and return into present capability.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: dangerous-command confirmation, workspace path policy, coder handoff approval, push approval, model/provider configuration and user cancellation bound ordinary execution.
- Decisive decision or feedback right: users may approve operational coder handoffs or pushes, but no identity/ultimate-policy issue is routed to a legitimate authority and returned as a durable identity decision for the system.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: confirmation UI, outside-read/write policy, Supervisor `RequireApprovalFor`, DevFlow push HITL, environment/config flags and stop controls.
- Closure path: confirmations change specific current actions; they do not close identity/ultimate-policy questions for subsequent operation.
- Why this is / is not agent-owned: runtime safety and HITL gates constrain S1/workflow actions but do not constitute S5.
- Evidence: README; `cmd/engine_supervisor.go`; `cmd/engine_devflow.go`; `cmd/repl.go`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator and maintainer authority exists, but the frozen operating boundary does not expose an identity-level return loop.

### Absence scope

- Surfaces inspected: dangerous-command/path policies, TUI confirmation flow, Supervisor coder approval, DevFlow push approval, provider/configuration controls, session controls and repository governance.
- Plausible first-party paths checked: HITL coder approval as S5; push approval as S5; security policy as S5; maintainer governance as system identity.
- Why no material first-party path remains: inspected runtime decisions are operational permissions, while maintainer/repository governance is adjacent to the deployed harness; no identity/policy issue → legitimate authority → authoritative decision → returned durable operation path is established.

## Recursion

Ordinary model/tool runs and the Loop Engineering model contexts are operational cells. Loop Engineering supplies a closed complementary audit relation across those cells. Experimental graph-based Supervisor/DevFlow recursion is not credited beyond the concrete wrapper because the sibling graph implementation is not revision-pinned by the reviewed repository.

## Variety and escalation

Marspi CLI absorbs coding variety through model/tool iteration, context compression, routing, memory, skills and optional role specialization. Loop Engineering deliberately exports implementation-validity variety to an independent Verifier and routes failures back through an Updater. Operationally sensitive actions can escalate to human confirmation; graph sessions can be checkpointed and resumed.

## Evidence gaps

The only published unknown is S3. The frozen CLI concretely exposes a star-topology Supervisor and checkpoint/HITL integration, so a material S3 path is plausible, but `go.mod` resolves `marspi-graph` through an unpinned local sibling and the decisive supervisor algorithm is absent from the frozen tree. The evidence is therefore insufficient to establish either a positive S3 closure or a defensible no-path conclusion without silently importing a dependency revision.

## Assessment summary

Marspi CLI closes autonomous S1 through its first-party coding composition and closes autonomous S3* through the directly implemented Implementer→Verifier→Updater audit/rework loop. No concrete S2, S4 or S5 path is established. Experimental Supervisor integration makes S3 genuinely unresolved at this frozen repository boundary because its decisive sibling implementation is not revision-pinned.

**Vector:** A · — · ? · A · — · —
