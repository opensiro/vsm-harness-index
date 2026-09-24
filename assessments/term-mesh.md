---
harness_id: term-mesh
project_name: term-mesh
repository: https://github.com/x-mesh/term-mesh
review_ref: 36f704695f62d0ae2e6935d9d016cc476fde0477
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# term-mesh

## Review boundary

- System in focus: the first-party `x-mesh/term-mesh` agent-control/coordination plane at pinned revision `36f704695f62d0ae2e6935d9d016cc476fde0477`, including the macOS application, `term-meshd`, `tm-agent`, `tm-coordinator`, task/team state, worktree/process lifecycle, peer-host transport, bridge/protocol normalization, budget/resource controls, watch scheduling, review snapshots, fencing and merge-queue machinery.
- Purpose and identity: provide a control plane for teams of coding agents running in terminal panes or on peer hosts, with task/delegation state, sandboxed worktrees, messaging/reporting, remote process ownership, resource controls, durable coordination state, review evidence and operator-facing visibility.
- Relevant environment: Claude Code, Codex, Kiro, Gemini, Cursor, agy and other external agent CLIs; their model/tool reasoning loops; users/leaders; Git repositories; peer hosts; external model/API providers; browsers and downstream tools/services.
- Standard-distribution boundary: repository-owned app/daemon/CLI/coordinator/bridge code, first-party prompt/runbook/configuration material, task/review/merge state, worktree/process controls and peer transport are inside. The autonomous reasoning/tool loops hosted by Claude/Codex/Kiro/Gemini/Cursor/agy or another external agent CLI remain environmental agent runtimes and are not imported into the first-party control-plane boundary.
- Credited operating / distribution surfaces: `README.md`; `Sources/TeamOrchestrator.swift`; `daemon/term-mesh-cli/src/tm_agent.rs`; `daemon/term-mesh-cli/src/prompts.rs`; `daemon/tm-agent-bridge/src/*`; `daemon/tm-coordinator/src/*`; shipped watch/task/review/merge paths and runbooks where they describe supported runtime behaviour.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI, architecture reviews and implementation plans except as corroboration; benchmark/research artifacts; future features explicitly marked not implemented. External coding-agent internals do not donate S1-S5 ownership to the term-mesh control plane.
- First-party operating / deployment modes considered: local and peer-host agent teams; leader/worker task flow; direct delegation and messaging; bridged Codex/Kiro/Gemini/Cursor/agy panes; Claude direct-channel mode; coordinator task placement/reassignment/fencing/review/merge state; headless/pane watch execution; first-party research/solve/consensus/swarm prompt templates when handed to supported external agent CLIs.
- Recursion level: the reusable term-mesh control plane itself, as admitted to organizational/control batch #407. External coding-agent sessions may form viable S1 units in a wider composed deployment, but their autonomous reasoning is not inherited into this repository-relative first-party boundary.
- Reviewed revision: `36f704695f62d0ae2e6935d9d016cc476fde0477`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

term-mesh describes itself as an "AI Agent Control Plane" and implements that description literally. The app and daemon create terminal/agent panes, worktrees and remote sessions; `tm-agent` supplies team/task/message/report operations; `tm-coordinator` persists projects, tasks, attempts, hosts, fences, review snapshots and merge-queue state; the bridge normalizes the protocols of externally installed agent CLIs.

The product ships substantial first-party organizational machinery. A leader can create/delegate tasks, workers can report blocked/review-ready/completed state, the coordinator can place and reassign tasks against observed host capacity, attempts carry fencing/worktree/Git identity, review snapshots bind base/head/diff evidence, and merge-queue records preserve approval provenance. Budget/resource controls can SIGSTOP/SIGCONT processes, peer hosts can keep sessions alive independently of the viewer, and watch machinery can periodically invoke reviewer-style agents.

Those control surfaces do not themselves supply the substantive coding-agent decision/action loop. The README says Claude speaks the agent protocol directly while Codex, Kiro, Cursor and agy go through a bridge. The bridge source says it exists to "speak an agent CLI's protocol on its behalf": it starts/turns child CLI processes and normalizes their protocol/event shapes. Codex/Kiro/Gemini are request/response child processes; Cursor/agy create a child per turn; Claude bypasses this bridge because its own channel can receive turns directly.

The first-party `prompts.rs` contains real organizational behaviour specifications: research agents run a shared-board discovery loop; problem solvers run a Try-Share-Adapt loop; consensus/swarm modes define repeated autonomous work over shared state. But these are prompts handed to external autonomous agent CLIs. term-mesh does not implement the model/tool reasoning engine that interprets those instructions and chooses the next substantive Read/Grep/Bash/edit/tool action. The watch path exposes the same ownership boundary: an autonomous tick spawns or recycles a selected external `codex`/`claude`/`gemini`/`kiro` process and asks that agent to produce the verdict.

The counterfactual owner test is decisive at this batch's first-party control-plane boundary. Remove the external agent CLIs while leaving the app, daemon, coordinator, bridge, task board, prompts, runbooks, worktrees, resource controls, watch scheduler, review snapshots and merge queue intact. The remaining repository-owned system can persist, schedule, route, constrain, observe, normalize, fence, approve and transport work, but it cannot interpret the coding/research task and autonomously choose the next substantive model/tool/action. Its operational agent loop closes in an adjacent runtime.

Under Methodology `0.3.6`, an included autonomous harness must establish operational S1 at the declared boundary rather than inherit it from another harness. The proposed terminal outcome is therefore `excluded-no-agentic-vsm`, not an included constructor vector assembled from otherwise substantial control-plane primitives.

Primary evidence:

- [`README.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/README.md) — control-plane identity, Agent Teams workflow, supported external CLIs, peer-host process ownership and bridge use.
- [`docs/tm-agent-architecture-review.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/tm-agent-architecture-review.md) — three-layer coordination-plane architecture and task lifecycle.
- [`docs/team-management-p0-p1-spec.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/team-management-p0-p1-spec.md) — task/inbox management model, leader/worker prompting and explicit non-goal of full autonomous planning/self-healing.
- [`daemon/tm-agent-bridge/src/main.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-agent-bridge/src/main.rs) — bridge ownership of child-CLI protocol/transport rather than the child agent's reasoning loop.
- [`daemon/term-mesh-cli/src/prompts.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/term-mesh-cli/src/prompts.rs) — first-party autonomous research/solve/consensus/swarm prompt specifications executed by external agent actors.
- [`daemon/tm-coordinator/src/model.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/model.rs) — task/attempt/host/review/merge state model.
- [`daemon/tm-coordinator/src/reducer.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/reducer.rs) — deterministic event reduction/projection and control-state enforcement.
- [`docs/autonomous-watch-visibility-and-pane-recycle.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/autonomous-watch-visibility-and-pane-recycle.md) — watch ticks spawn/recycle selected external agent CLI processes and collect their verdicts.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop is established at the declared term-mesh control-plane boundary.
- Disturbance / variety regulated: repository-owned code regulates orchestration variety — task identity/status, host placement, process/pane lifecycle, worktrees, messaging, resource limits, peer transport, review/merge evidence and watch cadence — while substantive coding/research variety is interpreted and acted on by external autonomous agent CLIs.
- Decisive decision or feedback right: choose the substantive reasoning steps, code/tool actions and local task decisions that produce the requested software/research outcome.
- Decision owner: no first-party autonomous S1 owner established; the decisive task-local actor is the external Claude/Codex/Kiro/Gemini/Cursor/agy or equivalent agent runtime.
- Supporting / enforcement mechanisms: first-party leader/worker prompts and runbooks, task board, worktree isolation, pane/process creation, bridge transport, coordinator state, host observations, fencing, budgets/resource guard, messages/reports and durable project/session metadata.
- Closure path: first-party control plane creates/assigns or forwards work → selected external agent CLI receives the task/prompt → external agent runtime chooses model/tool/file actions and processes their feedback → result/status returns through term-mesh task/report/bridge surfaces → leader/operator or another external agent selects further substantive work.
- Boundary reachability: no positive first-party S1 actor remains reachable after removing adjacent agent CLIs; prompt text and transport do not execute themselves.
- Why this is / is not agent-owned: term-mesh supplies rich context, protocol and organizational constraints, but the actor that makes the autonomous task-local decisions is hosted by another agent harness/CLI.
- Evidence: [`README.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/README.md); [`daemon/tm-agent-bridge/src/main.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-agent-bridge/src/main.rs); [`daemon/term-mesh-cli/src/prompts.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/term-mesh-cli/src/prompts.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a wider deployment boundary containing the external coding-agent runtimes can have autonomous S1 units. This standalone result is specifically for the first-party organizational/control boundary pinned by batch #407.

### Absence scope

- Surfaces inspected: README/product architecture, team-management specification, Swift TeamOrchestrator boundary, unified `tm-agent` CLI, first-party autonomous prompt templates, CLI bridge, coordinator model/reducer, watch execution design, task/review/merge state and peer-host execution model.
- Plausible first-party paths checked: leader pane; worker pane; research/solve/swarm prompt modes; headless autonomous watch; bridge-managed turns; coordinator tasks/attempts; deterministic host placement; direct daemon execution.
- Why no material first-party path remains: every non-test model-driven path ultimately requires an external agent CLI/model actor to interpret the task and choose substantive actions; first-party code provides control, context, transport, state and enforcement around that actor.

## S2 — Coordination

- State: —
- Function: no qualifying S2 is published at the declared first-party boundary because the boundary does not establish a population of first-party autonomous S1 operational units.
- Disturbance / variety regulated: term-mesh contains real collision-attenuation and shared-work mechanisms — isolated worktrees, task assignment, dependencies, messages/reports, shared research boards, fencing and remote placement — but the substantive interacting S1 agents remain external runtimes.
- Decisive decision or feedback right: first-party code can deterministically enforce isolation/fencing and transport shared state; semantic delegation, shared-board interpretation and conflict-resolution choices are made by external leader/worker agents or the human operator.
- Decision owner: no qualifying first-party autonomous S2 owner at this recursion.
- Supporting / enforcement mechanisms: worktree isolation, coordinator placement, task dependencies, fencing tokens, shared board files, messages, task lifecycle and host capacity state.
- Closure path: these mechanisms can affect a wider composed team's agent behaviour, but the affected autonomous units are outside the first-party control-plane boundary; no internal S1-interference witness closes here.
- Why this is / is not agent-owned: deterministic coordination infrastructure is substantial but does not create internal autonomous operational units or inherit the external actors' coordination judgment.
- Evidence: [`README.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/README.md); [`daemon/tm-coordinator/src/model.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/model.rs); [`daemon/term-mesh-cli/src/prompts.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/term-mesh-cli/src/prompts.rs).
- Basis: structural absence after boundary test.
- Confidence: high.
- Caveats: worktrees/fencing/shared-board semantics may support S2 in a separately assessed wider team organization containing the external agents.

### Absence scope

- Surfaces inspected: team task/dependency model, worktrees, fencing, host placement, shared-board research/solve modes, messaging/reporting and peer-host orchestration.
- Plausible first-party paths checked: collision prevention through worktrees/fences; task sequencing/dependencies; shared-board stigmergy; placement by capacity/load; leader-worker messages.
- Why no material first-party path remains: no qualifying internal S1 population exists at the declared boundary, and the only autonomous interpretation of coordination signals belongs to external agent runtimes.

## S3 — Inside-and-now control

- State: —
- Function: the repository supplies strong current-state control machinery, but no first-party autonomous whole-system S3 owner is established over a first-party S1 organization.
- Disturbance / variety regulated: task/attempt status, blocked/review-ready work, host capacity/liveness, stale sessions, process resource pressure, pane/process lifecycle, worktree ownership, remote host availability and merge-queue state.
- Decisive decision or feedback right: semantic decisions about what work should happen next, whether output is adequate, what to reassign/revise and how to respond to substantive agent results remain with an external leader agent or human operator. Coordinator ordering, capacity selection, fencing and lifecycle transitions are deterministic enforcement/placement mechanisms.
- Decision owner: no qualifying first-party autonomous S3 owner at this recursion.
- Supporting / enforcement mechanisms: task inbox/status lifecycle, coordinator reducer, placement/reassignment API, host observations, budget guard, SIGSTOP/SIGCONT, pane/process controls, peer reconnect, fences and event log.
- Closure path: external leader/operator selects current work/intervention → first-party control plane records/routes/enforces it → external worker acts → status/report/evidence returns → external leader/operator chooses the next substantive current-control action.
- Why this is / is not agent-owned: the coordinator has durable current state and hard enforcement power but does not itself contain the discretionary model actor choosing whole-team commitments. Methodology separates enforcement authority from organizational decision ownership.
- Evidence: [`docs/team-management-p0-p1-spec.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/team-management-p0-p1-spec.md); [`daemon/tm-coordinator/src/model.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/model.rs); [`daemon/tm-coordinator/src/reducer.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/reducer.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an external leader agent using the shipped control surfaces may close S3 for a wider composed team; that ownership is not imported into the first-party control-plane assessment.

### Absence scope

- Surfaces inspected: leader task lifecycle/inbox, coordinator task placement/reassignment/suspect/quarantine flows, host observations/capacity ranking, resource guard, peer lifecycle, watch scheduling, review/merge state and external leader prompting.
- Plausible first-party paths checked: coordinator as manager; automatic host selection; stale/watch handling; budget SIGSTOP/SIGCONT; task reassign/quarantine; merge queue.
- Why no material first-party path remains: deterministic machinery can select or enforce according to predeclared state/rules, but the substantive whole-team current-control judgment remains external and the first-party boundary lacks an internally owned S1 organization.

## S3* — Complementary audit

- State: —
- Function: the first-party boundary exposes meaningful audit/evidence primitives, but no qualifying internally owned complementary-audit loop is established over first-party S1 operation.
- Disturbance / variety regulated: worker self-reports may be incomplete or wrong; changed Git state may need review; watch modes can inspect drift; merge approval needs evidence bound to the exact attempt state.
- Decisive decision or feedback right: review judgment is supplied by a human/external reviewer agent or external watcher CLI. First-party coordinator records review snapshots, exact head/diff identity, approval/rejection and merge-queue provenance but does not autonomously perform the substantive independent audit judgment.
- Decision owner: no first-party autonomous S3* owner established at the declared boundary.
- Supporting / enforcement mechanisms: `ReviewSnapshot`, base/head SHA and diff digest, approval evidence, merge queue, task `review_ready`/approved/rejected states, watcher scheduling/status and first-party reviewer/runbook prompts.
- Closure path: external reviewer/watcher or human inspects work → first-party review/snapshot/approval path stores and enforces the verdict/evidence → subsequent merge/reassignment can change; because both the audited operational actor and substantive audit actor are external at this boundary, the control plane does not receive positive S3* ownership.
- Why this is / is not agent-owned: evidence binding and gate enforcement are first-party, but audit judgment is not. The autonomous watch implementation explicitly spawns/recycles an external agent CLI to generate the verdict.
- Evidence: [`daemon/tm-coordinator/src/model.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/model.rs); [`docs/autonomous-watch-visibility-and-pane-recycle.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/autonomous-watch-visibility-and-pane-recycle.md); [`docs/team-management-p0-p1-spec.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/team-management-p0-p1-spec.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: at a wider organization boundary, the shipped evidence/gating surfaces could support an S3* constructor or autonomous audit mode depending on who owns the reviewer/watcher actor. This assessment does not inherit that actor into term-mesh itself.

### Absence scope

- Surfaces inspected: review-ready lifecycle, review snapshots, approval/rejection, merge queue, watcher execution, reviewer roles/runbooks and bridge execution.
- Plausible first-party paths checked: review snapshot as audit; merge approval; autonomous watch; reviewer worker; diff/head digest binding.
- Why no material first-party path remains: repository-owned code persists/guards audit evidence but delegates the substantive challenge/verdict to a human or external agent CLI, and there is no first-party S1 operational population for complementary audit at this recursion.

## S4 — Outside-and-then adaptation

- State: —
- Function: no first-party outside-and-future adaptation loop that autonomously changes persistent organizational capability is established at the reviewed boundary.
- Disturbance / variety regulated: peer-host availability, stale work, watch findings, model/CLI choice, runbooks/prompts and task/workflow configuration can change, but those surfaces are operator configuration or current-run/task feedback rather than a first-party prospective adaptation owner.
- Decisive decision or feedback right: changes to roles, prompts, CLI/model choice, workflows, project structure or future capability are authored by users/maintainers/external agents rather than decided by a first-party autonomous S4 actor.
- Decision owner: none established within the first-party boundary.
- Supporting / enforcement mechanisms: watch outputs, durable state, runbooks/prompts, workflow presets/plans, peer observations and task history.
- Closure path: no first-party external/future sensing → option-generation → autonomous adaptation judgment → persistent capability change → subsequent operation loop was established.
- Why this is / is not agent-owned: repeated research/solve/watch prompts can make external agents adapt their current work, but term-mesh does not own the autonomous actor deciding and applying persistent organizational capability changes.
- Evidence: [`docs/team-management-p0-p1-spec.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/team-management-p0-p1-spec.md); [`daemon/term-mesh-cli/src/prompts.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/term-mesh-cli/src/prompts.rs); [`docs/autonomous-watch-visibility-and-pane-recycle.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/autonomous-watch-visibility-and-pane-recycle.md).
- Basis: structural negative search.
- Confidence: high.
- Caveats: an externally hosted agent may use watch/research outputs to adapt later work, but that would be ownership at a wider composed boundary rather than first-party term-mesh S4.

### Absence scope

- Surfaces inspected: watch loops, research/solve/shared-board prompts, role/runbook configuration, workflow-preset plans, task history, peer-host observations and persistent coordinator state.
- Plausible first-party paths checked: watcher-driven adaptation; shared-board learning; workflow presets; prompt/runbook evolution; recovery/reassignment.
- Why no material first-party path remains: the first-party platform stores/executes configured structures and invokes external agents, but no repository-owned autonomous adaptation actor converts outside/future distinctions into persistent capability change.

## S5 — Policy / identity

- State: —
- Function: no first-party identity/ultimate-policy decision loop is established for the term-mesh control plane at the reviewed boundary.
- Disturbance / variety regulated: CLI/model selections, task constraints, budgets, resource thresholds, worktree rules, host/project ownership and approval controls constrain operation but are configured or decided externally.
- Decisive decision or feedback right: ultimate choices about organizational purpose, acceptable risk, team policy, model/CLI use and whether reviewed work should be accepted remain with users/operators/maintainers or externally hosted leader agents.
- Decision owner: none established as a first-party autonomous or qualifying parent-governed S5 closure at this control-plane recursion.
- Supporting / enforcement mechanisms: configuration, runbooks/prompts, budget/resource limits, host/project ownership rules, task/review/merge gates and process controls.
- Closure path: configuration/operator decisions can constrain subsequent operation, but no identity-level matter → legitimate ultimate-policy authority → returned policy → governed operation loop is established as an S5 function in the shipped first-party boundary.
- Why this is / is not agent-owned: enforcement of configured constraints and ordinary task/review approval do not become S5 merely because they can block action.
- Evidence: [`README.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/README.md); [`docs/team-management-p0-p1-spec.md`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/docs/team-management-p0-p1-spec.md); [`daemon/tm-coordinator/src/model.rs`](https://github.com/x-mesh/term-mesh/blob/36f704695f62d0ae2e6935d9d016cc476fde0477/daemon/tm-coordinator/src/model.rs).
- Basis: structural negative search.
- Confidence: high.
- Caveats: human/operator governance can exist in a wider deployed organization, but ordinary configuration, task approval and merge acceptance do not establish an S5 parent mode at this declared first-party recursion.

### Absence scope

- Surfaces inspected: leader/worker prompts, task acceptance/review, model/CLI settings, budgets, resource guards, project/host ownership, merge approval and runbooks/configuration.
- Plausible first-party paths checked: leader as ultimate authority; merge approval as identity policy; budget guard as policy; project ownership as S5; configuration as governance.
- Why no material first-party path remains: these are current operational constraints/approvals or externally authored configuration. No first-party identity/ultimate-policy deliberation and closure path was established.

## Proposed terminal outcome

`excluded-no-agentic-vsm`.

The repository is a substantive organizational/control system and may be highly useful for composing a wider agent organization. The exclusion is narrower: at this pinned first-party boundary, term-mesh does not itself supply the autonomous operational actor required for S1 inclusion. Its prompts, task board, coordinator, bridge, watch scheduler, review evidence and merge controls organize external agent runtimes rather than replace their reasoning/tool loops.

## Evidence boundaries / caveats

- No VSM function is inferred from names such as `leader`, `coordinator`, `reviewer`, `watcher`, `orchestrator`, `policy`, `approval` or `agent`.
- First-party autonomous prompt text is treated as a behavioral specification/supporting primitive, not as an autonomous actor by itself.
- External coding-agent internals are not imported merely because term-mesh launches or bridges them.
- Deterministic placement, fencing, resource control, state transitions, review evidence binding and merge gating are separated from autonomous organizational decision ownership.
- A wider composed-system assessment that explicitly includes the external agent CLIs would be a different system-in-focus and could produce positive S1/S2/S3/S3* findings; that does not change this repository-relative standalone assessment.
