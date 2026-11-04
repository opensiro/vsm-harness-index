---
harness_id: tirith
project_name: Tirith
repository: https://github.com/andreseloysv/Tirith
review_ref: be358146324a8a9c98e6649938205328160c79cf
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Tirith

## Review boundary

- System in focus: The Python Tirith collector with an on-call AI manager, plan-gated model-operated coding lanes, cross-lane coordination, verification/merge queue, and optional independent CEO review mode.
- Purpose and identity: Convert developer project plans into verified coding-agent changes integrated on main, with an agent manager handling routine decisions and owner intervention reserved for human-only matters.
- Relevant environment: Multiple repository worktrees, plan items, agent processes from configured providers, Git changes, test outcomes, CI, resource contention, model credit limits, operator requests and stalled system components.
- Standard-distribution boundary: Shipped collector/tirith CLI and dispatcher, installed agent aliases/headless provider integration, model manager, coordination.sqlite3, review/merge queue, optional configured CEO reviewer, and macOS desktop/inbox.
- Credited operating / distribution surfaces: [collector dispatcher](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/dispatch.py), [manager runtime](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/managerd.py), [worker agent launch](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/agentrun.py), [coordination](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/coordination.py), [automatic review](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/autoreview.py), [merge queue](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/mergeq.py), [CEO auditor](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/ceo.py).
- Adjacent first-party surfaces excluded from ownership: Static website/demo state, screenshots, proposed unbuilt CEO watchdog/ratings, unmerged autonomous permission-prompt/continue-until-done improvements, in-progress Rust port, build/test CI and contributor governance.
- First-party operating / deployment modes considered: Mac collector and desktop with configured external coding-agent binaries; user chat and background on-call manager, several concurrent worktree lanes, coordination claims/path reservations, automatic verification and merge trains, optional CEO enabled in machine config, direct owner planning/stop/inbox action.
- Recursion level: One operator's portfolio of projects managed by Tirith, with individual model-driven coding lanes as S1 operational units; CEO is a bounded supervisory/audit actor inside the optional first-party distribution mode, not upstream governance.
- Reviewed revision: be358146324a8a9c98e6649938205328160c79cf.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Tirith's collector polls events, plans, agent lanes and owner inbox, then drives autopilot proposals, a durable on-call manager, verification/merge queue, self-check and optional CEO reviews. A configured external coding CLI (Anthropic, Codex, Copilot, Muse) operates a model/tool loop in a dedicated Git worktree; the first-party lane launcher supplies a plan item, brief, tool hooks, command flags, recorded outcomes and structured status. A manager model keeps one resumable conversation, reads project/queue feedback, chooses decomposition, starts permitted lanes and reacts to blocked/failed work. SQLite transactions atomically claim persistent item IDs, dependencies and declared write path reservations; conflicting paths/claims are refused. Completed worker reports undergo regex/Git/test claim checks and staged tests before the merge queue may integrate them on main. The optional CEO uses a fresh restricted model lane, measured collector data rather than the manager's account, checks its own findings and issues policy directives to the manager or proposals to the human. The human can edit plans and respond to actual owner-only matters. [README](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/README.md), [launch contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-launch.md), [coordination contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-coordination.md), [CEO contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-ceo.md).

## Operational model

Actual coding-agent lanes own local work decisions within their plan briefs and policy gates (S1). SQLite claims and write reservations prevent particular inter-lane collisions, but code rather than a model chooses the arbitration rule (S2 constructor). The manager model chooses current commitments across plan/worktree agents and handles exceptions; the owner has a separate current-control channel through plan and lane buttons (S3 A(P)). Ordinary claim checks and tests are deterministic; a distinct opt-in CEO model independently examines measured operational data, judges manager performance and returns directives/follow-up evidence (S3* A in that mode). Neither current plan changes nor internal CEO KPI management demonstrates external/prospective S4, and owner-only approvals/targets are not by themselves identity-level S5.

## S1 — Operations

- State: A
- Function: Model-operated coding and repository task execution in separately launched worktree lanes.
- Disturbance / variety regulated: Unknown code changes, failing tools/tests, context limits and incomplete user-specified plan items.
- Decisive decision or feedback right: Select edits, terminal/repository operations and subsequent task actions based on observed tool results and brief constraints.
- Decision owner: Configured coding-agent model operating each spawned lane; manager is another model-mediated operational conversation for on-call tasks.
- Supporting / enforcement mechanisms: Model CLI adapters, lane brief, isolated worktree, agent log reader, plan report, hooks, tool gates, retry and timeout bounds.
- Closure path: Open plan item → manager/launcher starts coding-model CLI → model acts in worktree and observes results → reports done/partial/blocked → reviewer/manager feedback may cause a corrected new turn.
- Boundary reachability: The shipping lane run/launch command builds supported first-party agent aliases and reads real provider output; plan gate and dispatcher route results into the active project plan.
- Why this is / is not agent-owned: Plan reservation, test gates and Git merge logic cannot choose the substantive code edit; only the model agent does.
- Evidence: [agent runner](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/agentrun.py), [launcher](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/launch.py), [launch contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-launch.md).
- Basis: explicit + structural.
- Confidence: high for wired agent invocation and returned status.
- Caveats: Agent binaries/provider accounts are external prerequisites; this review did not execute a paid live coding session.

## S2 — Coordination

- State: C
- Function: Prevent duplicate concurrent ownership and overlapping write scopes between independent operational lanes.
- Disturbance / variety regulated: Two plan workers claim the same item, write the same folder or operate on an incomplete prerequisite, causing stale or conflicting source changes.
- Distinct S1 units: Multiple separately launched model-agent lanes in individual worktrees, possibly concurrent on separate tasks.
- Inter-S1 disturbance: Same task ID can be claimed twice, and explicit write paths can overlap including ancestor/descendant folders.
- Attenuating coordination relation: SQLite claim/attempt-token transaction, dependency check, lease/heartbeat, write-path overlap check and reported claim refusal; centralized merge queue serializes integration separately.
- Feedback into subsequent S1 behaviour: Conflicting claims block launch, a missing predecessor remains blocked until actually merged, and released/failed reservations become visible to new launcher/manager decisions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Path-specific atomic exclusivity and stale-attempt fencing address an identified inter-agent resource collision; failure and recovery change which subsequent S1 unit may begin work.
- Decisive decision or feedback right: Determine conflict admission and reclaim/release an expired claim after checking worker liveness.
- Decision owner: First-party deterministic coordination constructor (SQLite rules and collector recovery), not a model that can change the reservation policy in the operating mode.
- Supporting / enforcement mechanisms: coordination.sqlite3, permanent item IDs, explicit declared writes, lease and attempt token, heartbeat, worker inbox with idempotent messages.
- Closure path: Candidate lane → transaction checks existing owners, prerequisites and write overlap → accepted lease or refused conflict → manager/launcher receives available work or blockage and revises later starts.
- Boundary reachability: Standard launch acquires reservation before creating worktree/spawning agent; hook/report paths check attempt token; collector recovers dead-owner claims.
- Why this is / is not agent-owned: Models select task priorities and write declarations but the final conflict verdict, arbitration and lease recovery run deterministically.
- Evidence: [coordination implementation](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/coordination.py), [coordination contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-coordination.md), [merge queue](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/mergeq.py).
- Basis: explicit + structural.
- Confidence: high for reservation conflicts in declared scopes.
- Caveats: Legacy items without declared write paths have no additional path reservation; independent raw shell writes remain bounded by other tool/worktree gates, not this S2 path.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the current cross-project plan/worktree portfolio, agent assignments, blocked work, integration and escalation.
- Disturbance / variety regulated: Open work without a worker, stalled/rejected reviews, failed stages, WIP congestion, exhausted agent credits and owner-inbox backlog.
- Whole-system current view: Manager brief/queue and Tirith commands expose open plan items, active lanes, status, review/merge queue and recent reports; operator dashboard shows all projects, agents, pipeline results and current owner actions.
- Current-control decision scope: Manager chooses split, launch, combine, wait, retry, drop, or ask operator about a current item and handles failed reviews; operator can manually plan-edit, launch/stop agents, switch autopilot and resolve pending current decisions.
- Decisive decision or feedback right: Base model manager selects current operational commitments across plan items; human parent can directly alter commitments and stop/relaunch under the installed owner UI.
- Decision owner: Base A — persistent on-call manager model. Parent P — human owner acting through Tirith desktop/inbox/plan UI; collector enforces allowed decisions.
- Supporting / enforcement mechanisms: Resumable manager session, supervisor queue, autopilot proposals, plan gate, lane launcher, merge WIP limits and auto-repair, user inbox and owner-only actions.
- Closure path: Base: collector finds ready/failed work → manager reads its queue/plan → decides agent assignment or follow-up → launched lanes and later results change board/plan and manager's next turn. Parent: owner sees status/alerts → changes plan, runs/stops lane or toggles autopilot → dispatcher/manager adopt changed current work state.
- Boundary reachability: Managerd and dispatch are wired into every collector pass; owner inbox, Tauri commands and plan edits are first-party, directly updating the same live plan/dispatch state.
- Why this is / is not agent-owned: A model decides which issue to start, combine or defer based on the live portfolio; deterministic plan/merge gates and load limits enforce but do not choose those priorities. Human current-control is an independent supported mode.
- Evidence: [manager rules/session](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/managerd.py), [autopilot handoff](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/autopilot.py), [inbox contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-inbox.md), [mergeq](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/mergeq.py).
- Basis: explicit + structural.
- Confidence: medium-high for shipped control paths.
- Caveats: A manager decision may fail or wait despite the tools. Optional CEO audit influences management but does not replace the base task manager with a guaranteed autonomous global governor.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Persistent manager model | Autopilot/queue detects ready, blocked or failed current item | Manager chooses plan/launch/retry/wait; dispatcher implements and returns fresh status | [managerd.py](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/managerd.py) |
| Parent (`P`) | Human owner | Dashboard/inbox identifies a task requiring intervention | Owner edits plan, stops/launches lane or changes autopilot; operating plan and dispatch reflect change | [inbox contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-inbox.md) |

## S3* — Complementary audit

- State: A
- Function: Independently check the manager's account of progress/efficiency against raw collector operational measurements and send corrective directives.
- Disturbance / variety regulated: A manager can inaccurately claim progress while no lanes run, reviews are stuck, costs grow or main CI remains red; ordinary manager conversation does not expose all such evidence.
- Claim being audited: Whether the manager reliably turns the plan into verified mainline work within the operator's targets.
- Ordinary reporting path: Manager's own chat, inbox answers, plan/queue decisions and per-lane status reports.
- Complementary access path: An opt-in separate fresh CEO model lane gets collector-computed merged/started/review-health counts, scoreboards, age of pending requests and operational CI data; it does not read manager's private memory/full transcript or accept reports as ground truth.
- Independence boundary: CEO has a fresh separate model session, read-only source environment and bounded raw-data snapshot independent of the manager's claimed status; both run under the same host/provider configuration and the operator controls targets.
- Who acts on findings: CEO model judges findings and sends checkable directives to the manager inbox; for budget/code/target proposals it asks the human, who decides. Next CEO runs recheck whether directives improved the measured numbers.
- Decisive decision or feedback right: Make its own evidence-based operational audit judgment, issue corrective policy-level manager directives and test subsequent efficacy from independent raw counters.
- Decision owner: Separate model-driven CEO reviewer in an enabled first-party mode; deterministic claimcheck and stages remain support for worker validation rather than this audit owner.
- Supporting / enforcement mechanisms: Optional CEO schedule/force-run entry point, fresh read-only lane, collector measurement snapshot, untrusted-data delimiters, typed result validation, findings/directives records and manager inbox.
- Closure path: Measured operational discrepancy → CEO judgment from fresh snapshot → model directive/proposal delivered → manager changes current handling or owner resolves proposal → next CEO pass checks effects and reopens/escalates findings.
- Boundary reachability: dispatch.run calls ceo.run on every cycle with [ceo] enabled; ceo.start launches a configured model review lane, and ceo.deliver writes actual manager directives/owner proposals. This opt-in path is shipped, not the planned watchdog.
- Why this is / is not agent-owned: Snapshot and typed parser do not decide which finding matters or which directive to issue; the distinct CEO model owns that judgment, while worker claimcheck and ordinary tests are deterministic checks.
- Evidence: [CEO implementation](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/ceo.py), [dispatcher wiring](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/dispatch.py), [CEO contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-ceo.md), [ordinary claim checker](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/claimcheck.py).
- Basis: explicit + structural.
- Confidence: medium-high for first-party independently wired audit mode; no live CEO model output was reproduced.
- Caveats: CEO is off by default. Its code-based snapshot does not prove factual claims outside its observed metrics; some planned CEO watchdog/ratings functions are not shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party loop develops environmental/future options and returns a strategic capability adaptation into active portfolio operation.
- Disturbance / variety regulated: Model or tooling changes, future project opportunities and emerging external constraints might change strategy, but regular manager and CEO mostly inspect current/past project performance.
- Decisive decision or feedback right: Compare prospective external options, select a change to organizational capability and return it to current S3; no such complete chain is established.
- Decision owner: Operator/developer chooses provider/model/target configuration; manager decides present plan items and CEO inspects operational KPIs.
- Supporting / enforcement mechanisms: Model fallback chain, Meta summaries, research-capable lanes, plan refresh, CEO targets and autopilot proposal queue.
- Closure path: CEO may propose an internal code or budget change and owner may create a task, but there is no required external-environment future-option model or adaptive strategic S4-to-S3 control loop.
- Why this is / is not agent-owned: Internal throughput monitoring, recovery, scheduling and task planning are not outside-and-then intelligence even if a manager/CEO calls them policy.
- Evidence: [manager decisions](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/managerd.py), [CEO targets](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-ceo.md), [autopilot](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/autopilot.py).
- Basis: explicit + structural.
- Confidence: medium-high for the bounded absent future function.
- Caveats: A user can assign prospective market research work, but that is still a requested S1 task without evidenced strategic S4 return.

### Absence scope

- Surfaces inspected: Manager prompts, CEO snapshot/directive path, model/fallback configuration, autopilot/plan refresh, external Meta summary uses and project documentation.
- Plausible first-party paths checked: CEO performance changes as adaptation, model fallback selection, future plan tasks and Meta-generated architecture map.
- Why no material first-party path remains: Available options respond to present workload/technical failure or user task; no independently owned external-prospective option assessment feeds back into strategic operating capability.

## S5 — Policy and identity

- State: —
- Function: No separately closed first-party constitutional mission/ultimate-policy dilemma resolution at the project portfolio recursion.
- Disturbance / variety regulated: Human-only credentials/payment choices, agent tool safety, target budgets, review and merge policy; these are operational risk/priority bounds.
- Decisive decision or feedback right: Resolve a conflict about enduring mission/ethos or ultimate authority between current operations and adaptation, and govern later operations through the decision.
- Decision owner: Human owner handles personal/financial decisions and sets target values; CEO can recommend targets and manager execution policy, but not replace owner's ultimate authority.
- Supporting / enforcement mechanisms: Owner gate/inbox, CEO proposals/approve-decline record, fixed plan/tool/merge hooks, config.toml and planned rules.
- Closure path: A CEO recommendation can become an owner approval and plan item for code/budget/targets; this closes scoped operational improvement/authorization, not a demonstrated identity-policy controversy and constitutional return.
- Why this is / is not agent-owned: Hard rules and a human-final decision are not automatically S5; the cited proposal classes are about task, spend and productivity rather than ultimate identity of the system.
- Evidence: [owner gate](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/ownergate.py), [CEO proposal/decision lifecycle](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/collector/tirith/ceo.py), [inbox contract](https://github.com/andreseloysv/Tirith/blob/be358146324a8a9c98e6649938205328160c79cf/docs/CONTRACT-inbox.md).
- Basis: explicit + structural.
- Confidence: medium; this is bounded absence, not denial of owner's real-world governance power.
- Caveats: External maintainers and project owners may adopt lasting identity policies beyond the shipped operating workflow.

### Absence scope

- Surfaces inspected: Owner gate and inbox, CEO approve/decline path, config targets, manager directive handling, plan writer, tool hooks, roadmap and upstream governance docs.
- Plausible first-party paths checked: Owner-only decisions, CEO budget/targets proposal, tool policy updates, provider selection and persistent plan revisions.
- Why no material first-party path remains: Those concrete decisions authorize current actions or optimize internal operating process; a runtime identity/ultimate-policy issue with legitimate judgment and governing return is not evidenced.

## Distributed OSS parent arrangement

The MIT repository and external coding-agent/provider accounts have ordinary maintainer and account owner governance, but Tirith does not automatically inherit an S5 from those external institutions. The user is an actual parent for current portfolio decisions; this is represented only by the scoped S3 parent mode.

## Self-hosted and non-human modes

The collector and state UI are local; agent binaries and model provider accounts are separately supplied. The persistent manager can work without an attached user, while the owner retains inbox and UI rights. CEO mode is first-party but opt-in and uses a separate external-model review lane; it must not be conflated with always-on verification or the planned unbuilt watchdog.

## Recursion

Independent coding lanes are operational S1 cells managed under a shared cross-project Tirith plan/collector. A CEO reviewer can audit the manager, but its supervisor title does not prove a separate fully viable metasystem with its own autonomous S4 and S5.

## Variety and escalation

Many coding-agent aliases, concurrent worktrees and model choice amplify operational variety. Plan item gate, atomic write reservations, commit hooks, claim check, tests, merge WIP queue, repeated-failure recovery, owner-only inbox and CEO raw-metric audit attenuate conflicts. A failed test or stalled review returns to manager, while real human-only tasks reach owner; neither is automatically a constitutional S5 event.

## Evidence gaps

- Upstream pytest was attempted with uv in offline mode, but its locked dependency rpds-py==2026.9.1 was missing from cache, so the 900+ advertised upstream tests were not reproduced.
- No macOS desktop, paid agent/provider or opt-in CEO inference was run. Source reachability and code/doc contracts underpin positive states, not empirical success rates.
- SQLite path reservations apply to declared paths; old items without declarations do not reserve individual files.
- The CEO's raw metric checks and directives are present, but some promised watchdog/ratings/target editor features remain unbuilt and are not credited.

## Assessment verdict

Included: model-driven coding lanes under a first-party manager (S1 A), real deterministic inter-lane conflict management (S2 C), a live model-manager portfolio with alternate human current control (S3 A(P)), and an optional genuinely separate evidence-driven CEO audit/return mode (S3* A). Neither prospective external adaptation nor identity-level ultimate-policy closure is demonstrated.
