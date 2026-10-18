---
harness_id: chump
project_name: Chump
repository: https://github.com/repairman29/chump
review_ref: 724c8ebe1911e986cc8af6883b6f05acd096d437
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Chump

## Review boundary

- System in focus: one first-party Chump-managed software-development fleet at pinned revision `724c8ebe1911e986cc8af6883b6f05acd096d437`, using Chump's native `ChumpAgent` / `--execute-gap` worker path together with the shipped coordinator, gap/lease state, fleet current-control primitives, complementary audit surface and operator mission controls.
- Purpose and identity: coordinate multiple software-producing agent work cells so they can select, execute, verify and ship repository work without destructive interference while remaining subordinate to an operator-owned mission and current-control envelope.
- Relevant environment: repository and Git state; GitHub PR/CI state; local files and tool results; model-provider responses; external services reached by tools; worker/process failures; concurrent claims; operator intent and intervention; resource/provider availability.
- Standard-distribution boundary: the public Chump Rust workspace and shipped coordinator/runtime scripts reachable through the documented CLI, including the native built-in agent loop, `chump --execute-gap`, coordinator leases/gap state, picker/claimer, fleet doctor and harness-neutral fresh-eyes comparator. External Claude Code, OpenCode, Codex, Aider, goose and other optional worker harnesses remain separate systems; external model endpoints and GitHub remain dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `src/agent_loop/orchestrator.rs`; `src/agent_loop/tool_runner.rs`; `src/execute_gap.rs`; `crates/chump-agent-lease/src/lib.rs`; `scripts/dispatch/_pick_and_claim_gap.py`; `src/fleet_self_doctor.rs`; `scripts/coord/fresh-eyes-loop.sh`; operator mission-pointer consumption in the picker; documented fleet start/stop/status controls.
- Adjacent first-party surfaces excluded from ownership: `.claude/agents/*` and Claude-specific skills as autonomous actor ownership; Chump-repository contributor/dogfood sessions; repository CI/release workflows; gap files and roadmap text as decisions by themselves; benchmark/evaluation artifacts not wired into the assessed fleet mode; design-only future ChumpOS phases. Dogfood traces/documentation may corroborate that a constructor path is real but do not upgrade `C` to `A`.
- First-party operating / deployment modes considered: native Chump agent execution through `chump --execute-gap`; coordinator-managed concurrent fleet work with first-party claims/leases; deterministic picker/rebalance and self-doctor current-control paths; deterministic fresh-eyes audit; self-hosted operator mode with fleet-wide current-control commands and an operator-owned active mission pointer. Optional external worker harnesses are considered only as interoperability context, not as owners of Chump's VSM functions.
- Recursion level: the Chump fleet organization is the system-in-focus. Individual native `ChumpAgent` execute-gap sessions are S1 operational units when they own separate software-work outcomes. External worker harnesses may participate in the same coordinator protocol but their internal reasoning/functions are not imported into Chump.
- Reviewed revision: `724c8ebe1911e986cc8af6883b6f05acd096d437`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Chump has a two-surface architecture. Its coordinator surface owns shared gap state, leases/claims, worktree isolation, event/ambient state, fleet status and shipping/control machinery while remaining compatible with swappable external coding agents. Separately, Chump ships its own first-party agent runtime. `ChumpAgent::run` loads durable session state, constructs a tool set, calls a provider, executes tool requests through `ToolRunner`, returns tool results into later model rounds, supports cancellation and persists the resulting session. `chump --execute-gap <ID>` wires that same native loop into unattended software work and is explicitly designed as a first-party alternative to shelling out to `claude -p`.

The coordinator contains concrete anti-interference machinery rather than only generic messaging. `chump-agent-lease` defines path/gap claims, conflict detection, heartbeats, expiry and stale reaping. A claim fails when another live session owns an overlapping path, and the atomic picker/claimer attempts eligible gaps in ranked order until it obtains one. Those rules are constructor-defined: they expose and enforce the coordination path, but no autonomous model actor owns the policy that a conflicting claim must back off or that the next eligible gap should be tried.

Current fleet regulation is likewise mostly constructor-owned. The picker reads canonical gap state and recent ship history, preserves priority as the primary ordering key, applies active-mission and rebalancing distinctions inside priority bands and atomically claims the selected current commitment. `chump fleet doctor --heal` supplies a separate outer loop over current fleet health: missing required daemons are reinstalled and sufficiently stale `DIRTY`/`BLOCKED` PRs are re-dispatched through `chump --execute-gap`, bounded by a circuit-breaker budget. These are first-party whole-fleet control paths, but the decisive rules are encoded by the constructor rather than chosen by an autonomous manager agent.

Complementary audit is exposed through `scripts/coord/fresh-eyes-loop.sh`, described in its own source as harness-neutral and independent of the Claude convenience wrappers. It compares ordinary self-reports with different evidence sources: ambient fire events, `chump health --slo-check`, actual curator actions, registered event coverage and recent Git history. It emits at most one ranked finding per cycle and is explicitly read-only/advisory; remediation belongs to the normal current-control lane. This is a function-specific constructor path for S3*, not an autonomous audit actor.

The operator retains two distinct higher-level rights. Current operation can be scaled/stopped through ordinary fleet controls, while the fleet's active mission is selected through `CHUMP_ACTIVE_MISSION` or `~/.chump/ACTIVE_MISSION`; the picker reads that value and changes later work selection accordingly. Concrete first-party `MISSION-010` content is Chump dogfood and is not itself credited as product S5 ownership. The credited parent path is the generic operator-owned mission-selection mechanism plus its return into the picker.

## Operational model

In the native path, a worker is dispatched against a claimed gap through `chump --execute-gap`. Chump builds the gap prompt, constructs a `ChumpAgent`, and runs a multi-iteration model/tool loop. The model chooses tool calls and reacts to returned tool observations until it completes or fails; terminal outcomes are emitted as `gap_shipped`, `gap_blocked` or `gap_deferred`. Several such work cells can coexist under the coordinator.

Before a concurrent worker is allowed to own repository work, Chump's claim/lease layer protects gap and path ownership. The policy is intentionally deterministic: overlapping live claims fail; stale claims expire/reap; the picker walks ranked candidates and only returns work that it has atomically claimed. The autonomous S1 then receives already-admitted work. This distinction is why S1 is `A` while S2 is `C` rather than attributing the constructor's claim policy to the worker model.

At the fleet level, current-control state includes gap priority/status/history, active claims, ship history, PR condition and daemon liveness. Constructor rules use that whole-system state to pick work, damp workload imbalance and recover selected current failures. The operator can separately intervene at the same recursion by changing whole-fleet operating state such as fleet size/stop state. The parent mode is therefore published separately from the constructor base mode.

Fresh-eyes runs as a complementary read-only observer. It does not trust only the normal fleet banner or heartbeat path: its comparators read independent event/SLO/Git/registry evidence, emit a distinct finding and leave corrective action to the owning control lane. This preserves the S3/S3* distinction.

## S1 — Operations

- State: A
- Function: perform substantive software-development work in a repository through Chump's native model/tool agent loop and produce a durable work outcome such as a shipped PR, blocked result or deferred result.
- Disturbance / variety regulated: heterogeneous gap acceptance criteria; changing repository/file state; tool observations; build/test results; provider/model responses; tool errors; local uncertainty; cancellation; task-specific blockers.
- Decisive decision or feedback right: choose the next context-sensitive tool/action sequence in response to repository/tool observations and decide how to continue the multi-round work toward the gap outcome.
- Decision owner: the model actor inside the first-party `ChumpAgent` run used by `chump --execute-gap`.
- Supporting / enforcement mechanisms: `ChumpAgent`; `IterationController`; routed `ToolRegistry`; `ToolRunner`; session persistence; provider cascade; iteration/cancellation limits; governed tool middleware; execute-gap prompt and terminal-outcome emission.
- Closure path: a claimed gap enters `chump --execute-gap` -> `ChumpAgent::run` receives the work prompt -> model selects tools -> tool results are appended back into the session -> later model rounds adapt to those observations -> work terminates as shipped/blocked/deferred and the outcome returns to fleet state/control.
- Boundary reachability: `chump --execute-gap` is an implemented first-party CLI mode whose source explicitly drives the native `ChumpAgent` multi-turn loop instead of shelling out to an external coding-agent CLI; the README also documents the built-in agent as a shipped optional Chump surface.
- Why this is / is not agent-owned: if the model actor is removed while the session manager, tool registry and execution machinery remain, the same contextual code/tool decisions are not made. The runtime constrains and transports action but does not replace the agent's operational discretion.
- Evidence: [`README.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/README.md); [`src/agent_loop/orchestrator.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/agent_loop/orchestrator.rs); [`src/agent_loop/tool_runner.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/agent_loop/tool_runner.rs); [`src/execute_gap.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/execute_gap.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external Claude/OpenCode/Codex workers are not required for this S1 mapping and their internal agent loops are not imported.

## S2 — Coordination

- State: C
- Function: attenuate concrete destructive interference among concurrent S1 work cells by preventing two workers from owning the same gap/path set at the same time and releasing abandoned ownership after failure.
- Disturbance / variety regulated: two workers simultaneously editing overlapping paths; two workers claiming the same gap; crashed workers leaving stale ownership that blocks useful work; concurrent workers selecting work without knowing a sibling already owns it.
- Decisive decision or feedback right: decide whether a candidate gap/path ownership request conflicts with a live sibling claim and expose a blocking/skip result that changes which work may proceed next.
- Decision owner: constructor-defined Chump lease/claim/picker rules. The standard first-party path does not give an autonomous model actor discretion to redefine collision semantics; autonomous workers consume the resulting admitted work or conflict signal.
- Supporting / enforcement mechanisms: `.chump-locks/<session>.json`; atomic lease writes; path matching; gap IDs; TTL/heartbeat expiry; stale reaping; atomic picker/claimer; worktree isolation; shared gap state.
- Closure path: concurrent workers expose intended gap/path ownership -> Chump checks live sibling claims -> conflicting ownership is rejected / skipped and a different eligible candidate may be attempted -> only successfully claimed work is returned for later S1 execution -> stale/dead ownership is eventually reaped so work becomes available again.
- Boundary reachability: the lease crate and atomic picker/claimer are shipped first-party coordinator surfaces and the README documents leases, gap claiming and worktree isolation as ordinary Chump coordination primitives usable with the native agent or other compatible workers.
- Why this is / is not agent-owned: the same conflict/backoff decision is produced if the worker model is removed and the lease/picker machinery remains. Chump therefore supplies an S2-specific constructor path, but the decisive coordination policy is not agent-owned; `C` is used rather than `A`.
- Distinct S1 units: separately dispatched native `chump --execute-gap` work cells can own different gap outcomes concurrently; optional external worker systems can also participate in the protocol without donating their internal functions to Chump.
- Inter-S1 disturbance: overlapping live gap/path ownership would cause duplicate implementation or silent file stomps between concurrently operating work cells.
- Attenuating coordination relation: path/gap leases plus atomic claim checks prevent a second live holder from proceeding on the same owned work and free abandoned claims through TTL/heartbeat reaping.
- Feedback into subsequent S1 behaviour: the picker/claimer returns only work it successfully claimed; a collision therefore removes the conflicting candidate from that worker's immediate execution path and causes later S1 work to proceed on separately admitted work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to a named concrete interference class — concurrent gap/path stomping — and a first-party collision/claim mechanism that specifically prevents that interference from reaching later execution.
- Evidence: [`crates/chump-agent-lease/src/lib.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/crates/chump-agent-lease/src/lib.rs); [`scripts/dispatch/_pick_and_claim_gap.py`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/scripts/dispatch/_pick_and_claim_gap.py); [`README.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: lease serialization itself is not evidence of autonomous coordination. The state is `C` because Chump ships an S2-specific decision/feedback path while the coordination discretion is constructor-defined.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the fleet's current portfolio, current commitment admission and selected health/recovery interventions from a whole-fleet view, with a constructor-defined base path and a distinct operator-owned parent current-control mode.
- Disturbance / variety regulated: competing current gaps and priorities; mission-vs-throughput work mix; domain/pillar monopolization; already-done/in-flight work re-entering the queue; dead required daemons; stale `DIRTY`/`BLOCKED` PRs; excessive recovery spawning; whole-fleet need to start/scale/stop work.
- Decisive decision or feedback right: base mode — determine which currently eligible gap should be admitted next under priority/mission/rebalance rules and when selected fleet-health failures trigger reinstall/re-dispatch under a bounded recovery budget; parent mode — decide whole-fleet start/size/stop intervention through the supported operator control surface.
- Decision owner: base `C` mode — constructor-defined first-party picker and self-doctor rules; parent `P` mode — the self-hosted Chump operator controlling the fleet as a whole.
- Supporting / enforcement mechanisms: canonical gap/state DB; recent ship history; active-mission value; atomic claim layer; fleet/PR status; required-daemon registry; self-doctor budget/circuit breaker; launchd/systemd process supervision; fleet CLI/status surfaces.
- Closure path: base mode — whole-fleet current state is read -> deterministic priority/mission/rebalance or recovery rule selects a current intervention -> Chump claims/dispatches work or restores/re-dispatches a failed current path -> later S1 work runs under the changed current state; parent mode — operator chooses fleet-wide start/scale/stop -> Chump changes the active worker set -> subsequent current operation follows the returned parent decision.
- Boundary reachability: `_pick_and_claim_gap.py` and `chump fleet doctor --heal` are shipped first-party paths; the README documents `chump fleet start --size N`, `chump fleet status` and `stop the fleet` through the ordinary coordinator/operator surface. No external manager agent is needed for the base constructor path or parent CLI mode.
- Why this is / is not agent-owned: removing the model actors does not remove the picker ordering, stale-work filters, rebalancing formulas, daemon-health rules or stuck-PR threshold. Those decisive current-control rules are constructor-owned, so the base state is `C`, not `A`. Parent fleet intervention is separately operator-owned and therefore recorded as `(P)` rather than attributed to deterministic enforcement.
- Whole-system current view: canonical/open gap records plus recent ship distribution, active claim state, PR merge-state/age, required-daemon liveness and fleet status provide current state across the managed work population rather than only one worker's local task.
- Current-control decision scope: current work admission/ranking, current workload rebalance inside priority bands, selected daemon/PR recovery and recovery spawn budget in base mode; whole-fleet worker activation/scale/stop in parent mode.
- Evidence: [`scripts/dispatch/_pick_and_claim_gap.py`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/scripts/dispatch/_pick_and_claim_gap.py); [`src/fleet_self_doctor.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/fleet_self_doctor.rs); [`docs/process/FLEET_SELF_HEAL.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/docs/process/FLEET_SELF_HEAL.md); [`README.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: task dispatch by itself is not credited as S3. The positive mapping rests on whole-fleet current-state regulation and recovery; the parent modifier is limited to genuine whole-fleet current-control commands, not ordinary per-tool approvals.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | constructor-defined Chump picker/self-doctor path | current eligible-work portfolio changes, work-mix imbalance, missing required daemon, or stale blocked/dirty PR | first-party rules choose current work/recovery action; claim/dispatch/reinstall changes later fleet operation | `_pick_and_claim_gap.py`; `src/fleet_self_doctor.rs`; `docs/process/FLEET_SELF_HEAL.md` |
| Parent (`P`) | self-hosted Chump operator | operator judges the whole fleet should start, change active size, or stop | fleet control command changes worker activation/current work population and subsequent S1 execution | `README.md` coordinator/orchestrate/fleet control path |

## S3* — Complementary audit

- State: C
- Function: independently challenge routine fleet self-reports by comparing them with complementary ground-truth channels and emitting a ranked discrepancy into control.
- Disturbance / variety regulated: fleet banner reports healthy while real fire events exist; curator heartbeat says alive while no work actions occur; `fleet-brief` health disagrees with SLO outcome; registered event kinds have no watcher coverage; stated roadmap bottleneck is starved in actual recent ships.
- Decisive decision or feedback right: apply the dedicated fresh-eyes comparator set to self-report versus alternative evidence and decide whether a discrepancy exists and which single finding has highest severity for the cycle.
- Decision owner: constructor-defined deterministic `fresh-eyes-loop.sh` comparator/severity rules. No autonomous model actor owns the audit judgment in the credited standard-distribution path.
- Supporting / enforcement mechanisms: ordinary fleet-brief output; ambient event stream; `chump health --slo-check`; curator heartbeat/action events; event registry; Git history; ranked finding buffer/backlog; ambient finding emission.
- Closure path: ordinary self-report and complementary evidence are sampled separately -> fresh-eyes computes comparator disagreements -> the highest-severity finding is emitted to the fleet's ambient/control surface -> the owning current-control lane/operator can act on the discrepancy rather than relying on the challenged self-report.
- Boundary reachability: the script explicitly identifies itself as harness-neutral, says the `.claude` wrappers are convenience rather than capability, and can be invoked directly as `tick`/`audit`; the audit primitive therefore exists in the shipped first-party boundary without borrowing Claude role cognition.
- Why this is / is not agent-owned: the comparators and ranking are deterministic and would make the same audit finding with no model actor present. The first-party S3*-specific path is real, but autonomous audit judgment/remediation still requires composition, so the state is `C` rather than `A`.
- Claim being audited: that the fleet is healthy/aligned/covered as represented through its routine health banner, liveness signals and roadmap/current-control self-report.
- Ordinary reporting path: `fleet-brief` health banner, curator heartbeat/liveness and roadmap bottleneck declarations.
- Complementary access path: raw ambient fire events, actual SLO command exit status, action events behind heartbeats, event-registry-versus-loop coverage and actual recent Git ship history.
- Independence boundary: fresh-eyes is explicitly read-only/advisory and refuses implementation/rescue/dispatch work; it obtains evidence from channels different from the challenged routine reports instead of accepting the worker/control lane's claim at face value.
- Who acts on findings: the normal owner lane or operator/current-control path consumes the emitted advisory signal; fresh-eyes itself does not mutate the work it audits.
- Evidence: [`scripts/coord/fresh-eyes-loop.sh`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/scripts/coord/fresh-eyes-loop.sh); corroborating role-boundary documentation in [`.claude/agents/fresh-eyes.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/.claude/agents/fresh-eyes.md) is not used as autonomous ownership evidence.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the deterministic audit primitive emits an advisory finding but does not itself own the corrective current-control decision. That separation is why the constructor state is used and why ordinary tests/logging alone are not credited.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party path is established in the reviewed standard distribution that senses external/future distinctions, develops adaptation options for the Chump fleet organization itself and returns an adopted option into present S3 capability.
- Disturbance / variety regulated: Chump contains provider routing, reliability learning, skill/memory, external-repository scanning/improvement and extensive R&D/evaluation surfaces, but the reviewed evidence does not close those mechanisms into an S4 loop for changing the fleet organization's own future capability.
- Decisive decision or feedback right: none established for qualifying S4 at this boundary.
- Decision owner: none established.
- Supporting / enforcement mechanisms: provider cascade/bandit state; fleet capability reliability; skills/memory; external-repository improve/scout flows; evaluation/research artifacts; roadmap/gap machinery.
- Closure path: observed provider/task/external-repository evidence may change current routing, task work or the target software artifact, but no standard path was found that converts an external/future distinction into alternative organizational capabilities and adopts one back into present fleet capability/S3.
- Why this is / is not agent-owned: model/tool learning and external-repository improvement are not sufficient by name. The documented autonomous improve loop performs software improvement as operational work, while adaptive provider routing regulates current execution. Neither establishes a separate outside-and-then organizational intelligence function.
- Evidence: [`src/provider_bandit.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/provider_bandit.rs); [`src/fleet_capability.rs`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/src/fleet_capability.rs); [`docs/design/AUTONOMOUS_IMPROVE_LOOP.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/docs/design/AUTONOMOUS_IMPROVE_LOOP.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a future standard-distribution path that uses external/future sensing to propose and adopt changes to the fleet's own organizational capability would require new-ref reassessment.

### Absence scope

- Surfaces inspected: native agent loop and execute-gap path; coordinator/lease/gap state; picker/rebalancing; provider bandit and capability reliability; skills/memory references; external-repo improve architecture; self-doctor/fresh-eyes; mission/roadmap surfaces.
- Plausible first-party paths checked: learned provider routing; historical agent reliability; reusable skills; external-repository scouting/improvement; benchmark/eval feedback; roadmap/gap generation; self-heal feedback.
- Why no material first-party path remains: those paths either regulate current execution, preserve/reuse internal history, improve the software target, or belong to adjacent R&D/dogfood planning. None establishes the Profile's external/future distinction -> adaptation options -> adopted change to present Chump organizational capability conversation with S3.

## S5 — Policy and identity

- State: P
- Function: preserve authoritative fleet purpose at the chosen recursion by letting the legitimate operator select the active mission/outcome that subsequent current-control work selection treats as the fleet's load-bearing mission.
- Disturbance / variety regulated: drift toward locally attractive throughput/self-maintenance work that no longer serves the operator's authoritative mission; need to replace which top-level outcome defines mission-linked progress without letting an ordinary worker silently redefine fleet purpose.
- Decisive decision or feedback right: select/replace the active mission identifier consumed by fleet work selection through `CHUMP_ACTIVE_MISSION` or `~/.chump/ACTIVE_MISSION`.
- Decision owner: the self-hosted Chump operator as legitimate parent. Constructor code provides a fallback/default and consumes the value; no first-party autonomous agent has authority to redefine the operator's active mission.
- Supporting / enforcement mechanisms: operator-owned env/file mission pointer; `_load_active_mission`; mission-linked classification; picker mission-rank tiebreak; mission scoreboard/status surfaces; separate `AUTONOMY_LEVEL`/fleet-stop sovereignty as supporting parent constraint rather than the S5 witness itself.
- Closure path: mission/alignment evidence makes the active top-level purpose visible -> operator chooses/changes the authoritative mission pointer -> later picker/claimer invocations read that returned value -> mission-linked work receives the first-party mission-ranking treatment inside the current-control policy -> subsequent fleet operation is governed by the returned parent mission decision.
- Boundary reachability: the active-mission env/file lookup is implemented in the shipped picker/claimer and documented as the active mission mechanism. Concrete Chump-repository `MISSION-010` text is treated only as a first-party use of the generic mechanism; parent authority is not borrowed from a Claude/dogfood agent.
- Why this is / is not agent-owned: the model workers cannot authoritatively replace the mission pointer merely by proposing different work. The parent-controlled value is what the current-control path consumes, so ultimate mission selection remains parent-owned and is published as `P`.
- Identity / ultimate-policy issue: which top-level mission/outcome defines what the fleet is ultimately trying to advance and which work counts as mission-linked progress at this recursion, rather than how any one gap is executed.
- Ultimate authority in each claimed mode: parent mode only — the self-hosted operator owns the authoritative active-mission value. Constructor defaults and worker suggestions do not override a supplied parent value.
- Return-to-operation path: operator changes `CHUMP_ACTIVE_MISSION` or `~/.chump/ACTIVE_MISSION` -> `_load_active_mission` returns the new value -> the picker reclassifies/ranks mission-linked eligible work on later cycles -> subsequent S3 work admission and S1 execution operate under that returned mission choice.
- Evidence: [`scripts/dispatch/_pick_and_claim_gap.py`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/scripts/dispatch/_pick_and_claim_gap.py); [`docs/MISSION.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/docs/MISSION.md); [`README.md`](https://github.com/repairman29/chump/blob/724c8ebe1911e986cc8af6883b6f05acd096d437/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: tool approvals, ordinary PR merges and emergency stop alone are not credited as S5. The positive mapping is deliberately narrow: operator-owned mission identity with an implemented return into later fleet work selection.

## Distributed OSS parent arrangement

Chump is public OSS, but this assessment does not infer project-level parent governance from GitHub maintainers or contributors. The `P` claims are local to one supported self-hosted fleet deployment: the operator of that fleet owns whole-fleet current-control intervention and active-mission authority. Repository maintainer/release governance is adjacent and excluded from these runtime parent states.

## Self-hosted and non-human modes

The self-hosted operator mode materially changes S3 and S5 ownership and is therefore recorded. Chump also supports unattended native workers, but no non-human autonomous owner was found for the decisive S2/S3/S3*/S5 rules credited here; deterministic constructor paths remain `C`, and S5 remains parent-owned.

## Recursion

The assessed recursion is one Chump-managed software-development fleet. Native execute-gap sessions are operational work cells under that fleet when separately claimed gaps give them distinct outcomes and local repository variety. A single tool call, provider slot, daemon or subprocess is not an S1 merely because it executes work. External Claude/OpenCode/Codex harnesses retain their own internal organizations and are not recursively absorbed into Chump; they can participate only as external operational actors speaking Chump's coordination protocol.

## Variety and escalation

Chump attenuates concurrency variety through leases/atomic claims and current-work variety through priority/mission/rebalance rules. Tool observations and provider failures are amplified back into the native S1 loop for local correction. Fleet-health exceptions such as missing daemons or stale blocked PRs reach the self-doctor current-control path; circuit-breaker exhaustion can surface an operator-action-needed condition rather than allowing unbounded automated recovery. Fresh-eyes supplies a complementary discrepancy signal instead of duplicating the current controller. Operator mission selection and whole-fleet control remain higher-recursion parent rights.

## Evidence gaps

- Structural/static repository review only; no live model provider, fleet or target repository was executed during this assessment.
- `S2=C` is intentionally conservative. Chump closes the collision/claim mechanism itself, but the decisive response semantics are constructor-defined rather than agent-owned; optional external workers do not upgrade that state.
- `S3=C(P)` does not credit names such as coordinator/supervisor. The base claim is the whole-fleet picker/rebalance/recovery path; the parent claim is whole-fleet current-control intervention.
- `S3*=C` uses the harness-neutral fresh-eyes comparator, not Claude curator cognition. The emitted finding is advisory and corrective discretion remains in the owning control lane.
- `S4=—` remains despite learning, bandits, skills, external-repo scanning and self-improvement terminology because no externally prospective fleet-capability adaptation loop was established at this boundary.
- `S5=P` is narrow and medium-high confidence because the active-mission pointer is a real parent-owned policy return path, but the concrete mission document is Chump dogfood rather than a universal built-in mission. A future ref that generalizes mission-authority handling further may strengthen the witness without changing the parent ownership topology.
