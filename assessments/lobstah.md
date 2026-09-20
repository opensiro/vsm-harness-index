---
harness_id: lobstah
project_name: lobstah
repository: https://github.com/aequitas-labs/lobstah
review_ref: 6aa75e2212fa8f22fa8dde7790070463c0021f8c
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# lobstah

## Review boundary

- System in focus: one first-party lobstah-managed local fleet at pinned revision `6aa75e2212fa8f22fa8dde7790070463c0021f8c`, including the queue/daemon/runner/worktree runtime, Claude Code and Codex adapters, status/evidence/inbox contracts, fleet CLI, shipped lobsterman plugin/skill, and optional first-party pickup/watch/merge loops where they materially change organizational ownership.
- Purpose and identity: run multiple local coding-agent work items concurrently without workspace collisions, supervise their liveness without consuming model tokens, expose fleet-wide current state and intervention paths, and escalate judgment calls to an operator or orchestrator while preserving durable evidence.
- Relevant environment: user or tracker work items, configured git repositories, external coding-agent harness CLIs, worker status/events/evidence, filesystem/process liveness, operator messages, optional GitHub/Linear tracker state, PR/review/CI state and external watches.
- Standard-distribution boundary: first-party lobstah core, supervisor, runner, worktree allocator, adapters, CLI, shipped Claude Code/Codex plugins, lobsterman skill and pickup/watch/merge add-on. Claude Code, Codex, model providers, GitHub/Linear/ume/CI systems and their judgments remain external substrates or environment; lobstah receives their outputs but does not inherit their organizational ownership.
- Credited operating / distribution surfaces: `lobstah dispatch`, daemon/runner execution, per-dispatch worktrees, six-verb status and inbox contracts, `lobstah man tend`/`wait`/`haul`, `send`/`cancel`/`swap`, the shipped lobsterman skill and Stop-hook wake path, plus pickup reconciliation/watch/merge machinery when enabled.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, tests/fault-injection used to validate lobstah itself, documentation publishing and maintainer/contributor governance. External reviewer/forge/CI verdicts transported by pickup/watch are not reclassified as lobstah-owned S3* judgments.
- First-party operating / deployment modes considered: standalone CLI + daemon fleet; shipped Claude Code/Codex lobsterman plugin mode; human operator use of fleet CLI; optional tracker pickup/watch/merge service; headless workers and voluntary soaking sessions.
- Recursion level: one lobstah-managed fleet. Concurrent dispatched coding-agent sessions are distinct operational S1 units at this level. The external model/harness provider is an execution substrate, not the assessed metasystem; individual worker-internal subagents are below this recursion.
- Reviewed revision: `6aa75e2212fa8f22fa8dde7790070463c0021f8c`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

lobstah is a local supervision and execution layer around existing coding-agent harnesses. A queue descriptor names a repo/brief and optional model/limits. The daemon atomically claims work up to configured capacity, allocates an isolated git worktree, spawns a runner, and the runner drives a Claude Code or Codex adapter. The runner injects lobstah's first-party dispatch contract into the worker prompt: work only in the allocated worktree, report one of six verbs, inspect the inbox at checkpoints, commit work and never merge. The coding agent makes the substantive implementation/tool decisions; lobstah supplies isolation, state, liveness supervision and intervention transport.

The daemon deliberately keeps model judgment out of liveness supervision. It classifies workers as unclaimed, busy, terminal, dead, wedged or unknown from process/state evidence. Dead workers are resumed within a bounded restart ladder; wedged workers are killed before a forked/nudged replacement is started; contradictory evidence is left untouched. These are deterministic enforcement/recovery mechanisms rather than autonomous S3 ownership.

At fleet level, `lobstah man tend` combines heartbeat, queues, current dispatch state, unanswered questions, dispatch chains, PRs, merge-gate snapshots and external watches into a whole-fleet verdict. The same first-party surface is paired with commands that can change current commitments: dispatch new work, send instructions, cancel work, swap an active dispatch to a fresh harness session and answer escalated questions. The shipped lobsterman skill makes these surfaces directly usable by an interactive agent, but it explicitly says `needs-decision` and `blocked` belong to the human. Thus the reviewed distribution exposes an S3-specific constructor path and a separately complete parent-governed current-control mode rather than an autonomous S3 owner.

The optional pickup add-on mechanically polls trackers, creates descriptors, reconciles tracker/dispatch drift, transports review feedback and can enforce a configured merge gate. It explicitly says there is no LLM in that polling loop and that ambiguous judgment stays agent-side or human-side. External review/CI/watch events can wake or continue work, but the independent judgment originates outside lobstah; that does not make pickup an S3* auditor or an S4 adaptation organ.

Primary evidence:

- [`README.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/README.md) — product boundary, per-dispatch worktrees, daemon recovery, fleet CLI, lobsterman plugin, pickup and standard deployment paths.
- [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md) — explicit goal to isolate concurrent work so parallel tasks cannot collide, queue/capacity contract, liveness/restart architecture, inbox steering and chore lane.
- [`packages/runner/src/contract.ts`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/packages/runner/src/contract.ts) — first-party prompt contract binding each autonomous coding worker to its isolated worktree, status/inbox feedback and evidence rules.
- [`docs/vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md) — status ownership/escalation, deterministic liveness classification, whole-fleet tend verdicts, merge gates, watches and soaking semantics.
- [`docs/lobsterman.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/lobsterman.md) — one-liaison fleet pattern, whole-fleet tend view, intervention commands, wake paths and explicit human escalation.
- [`plugins/claude-code/skills/lobsterman/SKILL.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/plugins/claude-code/skills/lobsterman/SKILL.md) — shipped model-facing supervisor tool surface and rule that judgment calls are surfaced to the human.
- [`docs/pickup.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/pickup.md) — tracker/watch/review/merge/reconciliation loops and explicit separation of deterministic mechanics from judgment.

## Operational model

A user, tracker pickup loop or orchestrator writes a work descriptor. The daemon claims descriptors within machine capacity and creates a dedicated worktree. A runner starts or resumes an external coding-agent harness with lobstah's injected contract. That worker independently interprets the brief, uses its coding tools and produces commits/evidence, so the worker is the operational decision owner for its bounded dispatch.

Multiple dispatches may operate concurrently. lobstah prevents one concrete class of cross-S1 interference before execution by placing each dispatch in its own worktree and ensuring a single active item per claimed worktree/session path. This is real S2 coordination function, but the attenuation is deterministic infrastructure rather than an autonomous coordinating agent, so it is `C`.

Fleet supervision has two distinct ownership modes. The base product exposes a function-specific constructor surface: a whole-fleet current view plus intervention commands that a supervisor can compose into a regulator. Separately, the shipped operator/lobsterman path closes parent-governed S3: attention states are delivered at least once, a human owns judgment questions, and the returned answer/cancel/swap/steering command changes subsequent active work. The daemon's own dead/wedged restart ladder supports these modes but does not become autonomous S3 by itself.

## S1 — Operations

- State: A
- Function: execute a bounded coding brief autonomously inside an allocated repository worktree and return commits/status/evidence.
- Disturbance / variety regulated: implementation ambiguity, repository state, tool results, coding/test failures, local environment constraints and new dispatcher messages encountered while fulfilling the brief.
- Decisive decision or feedback right: choose substantive coding/tool actions, decide how to implement the brief, report status and complete or fail the dispatch within the supplied worktree and constraints.
- Decision owner: the running coding-agent session launched through the configured Claude Code or Codex adapter.
- Supporting / enforcement mechanisms: queue descriptor, daemon/runner, adapter, worktree allocation, process supervision, six-verb status log, inbox delivery, budget/turn/wall-clock limits and evidence files.
- Closure path: brief/descriptor → lobstah runner prompt → model-driven coding/tool actions → repository/tool observations and inbox messages → further agent actions → commits/evidence + terminal status.
- Boundary reachability: normal `lobstah dispatch` followed by the shipped daemon/runner path launches the worker and injects the lobstah contract without downstream code having to construct an agent loop; the authenticated external harness/model is the execution substrate, analogous to an external model provider rather than an imported organizational owner.
- Why this is / is not agent-owned: deterministic lobstah machinery supplies workspace and supervision, but the coding session itself chooses the substantive operational actions from current repository evidence.
- Evidence: [`README.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/README.md), [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md), [`packages/runner/src/contract.ts`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/packages/runner/src/contract.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: lobstah does not implement the foundation model or coding harness itself; credit is limited to the first-party runnable path that invokes and supervises that external execution substrate.

## S2 — Coordination

- State: C
- Function: attenuate concrete workspace-write interference among concurrently active coding-agent S1 units by structurally isolating their mutable repository work.
- Disturbance / variety regulated: two or more autonomous dispatches modifying one shared checkout/workspace concurrently, causing write collisions, branch contamination or multiple writers against one live session/worktree.
- Decisive decision or feedback right: assign each dispatch a separate worktree and reject/avoid concurrent ownership of the same active session/worktree path.
- Decision owner: first-party deterministic lobstah allocation/claim machinery; no autonomous coordinating agent owns this attenuation decision in the base mode.
- Supporting / enforcement mechanisms: per-dispatch git worktree allocation, atomic queue claiming, one-active-item-per-worktree soaking contract and attach refusal while an active dispatch is writing.
- Closure path: concurrent descriptors → lobstah claim/allocation → distinct worktrees/session ownership → each worker receives its isolated current directory → subsequent writes occur in separate workspaces rather than colliding.
- Boundary reachability: worktree allocation is a standard daemon/dispatch behavior and the runner prompt explicitly tells every worker to operate only inside the allocated worktree; no downstream coordination role must be authored to obtain the isolation path.
- Why this is / is not agent-owned: the S2 function is real and first-party, but the attenuating relation is encoded in deterministic allocation/enforcement rather than chosen by an autonomous coordinating actor, so publication is `C` rather than `A`.
- Evidence: [`README.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/README.md), [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md), [`packages/runner/src/contract.ts`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/packages/runner/src/contract.ts), [`docs/vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: queue capacity and dependency/order concerns are not separately credited as S2; the positive finding rests on the explicit shared-workspace collision disturbance and its isolation relation.
- Distinct S1 units: concurrently running dispatched coding-agent sessions, each executing a separate brief.
- Inter-S1 disturbance: concurrent mutable writes against the same repository checkout/session would interfere, contaminate work or create two-writer conflicts.
- Attenuating coordination relation: lobstah allocates a separate git worktree per dispatch and enforces exclusive active ownership at the worktree/session boundary.
- Feedback into subsequent S1 behaviour: the runner starts each worker in its assigned worktree and injects an instruction to work only inside that directory, so the isolation decision constrains all subsequent repository mutations by that S1.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly justified as preventing parallel tasks from colliding in a shared mutable workspace; it regulates a cross-worker interference relation rather than merely transporting tasks or messages.

## S3 — Inside-and-now control

- State: C(P)
- Function: expose and, in the operator mode, close whole-fleet current regulation over active commitments, attention states and interventions.
- Disturbance / variety regulated: fleet-wide combinations of queued/active/stalled work, dead or wedged processes, unanswered decisions, blocked dispatches, stale daemon state, work needing redirect/cancel/swap and optional PR/watch state requiring current intervention.
- Decisive decision or feedback right: inspect the whole fleet and decide whether to add/redirect/cancel/swap current work or answer an escalated judgment question; deterministic dead/wedged recovery remains supporting enforcement rather than the ownership basis.
- Decision owner: base `C` mode leaves the regulator role composable over first-party `man tend` + intervention commands; parent `P` mode places judgment decisions with the human operator/dispatcher, commonly surfaced through the shipped lobsterman liaison.
- Supporting / enforcement mechanisms: `lobstah man tend`, `ls`/`status`, at-least-once `man wait`/`haul` wake path, `send`, `cancel`, `swap`, `dispatch`, six-verb status contract, heartbeat, liveness classifier/restart ladder and optional pickup reconciliation/merge view.
- Closure path: current fleet/state/evidence → whole-fleet `tend`/attention view → supervisor or parent decision → send/cancel/swap/dispatch/answer → inbox/session/lifecycle change → subsequent current fleet operation.
- Boundary reachability: the whole-fleet report and intervention commands are first-party CLI surfaces, and the repository ships a lobsterman skill plus wake hooks that put those surfaces directly into a supported interactive-agent/operator mode; the parent mode does not require an external dashboard or custom control API.
- Why this is / is not agent-owned: lobstah supplies a genuine S3-specific view/intervention constructor, but its built-in daemon decisions are deterministic liveness enforcement and the shipped lobsterman rules explicitly escalate `needs-decision`/`blocked` judgment to the human. No autonomous first-party actor is evidenced as owning the whole-fleet current-control judgment, so the base is `C`, with a separately closed parent mode.
- Evidence: [`docs/lobsterman.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/lobsterman.md), [`plugins/claude-code/skills/lobsterman/SKILL.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/plugins/claude-code/skills/lobsterman/SKILL.md), [`docs/vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md), [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: automatic dead/wedged restart, concurrency ceilings and tracker reconciliation are not themselves treated as autonomous S3 ownership; they make control enforceable and observable.
- Whole-system current view: `lobstah man tend` reports a single fleet verdict from daemon heartbeat, queued/active/chores/recent outcomes, unanswered attention states and per-item chains, PR/merge-gate/watch state.
- Current-control decision scope: adding current commitments, redirecting active workers, cancelling work, swapping a dispatch to a fresh session/harness and returning answers to blocked/decision-seeking workers.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Composed supervisor role using first-party fleet-report and intervention primitives | `man tend` fleet verdict/status, attention event or other current fleet evidence | Supervisor can return `send`/`cancel`/`swap`/`dispatch` actions into active/queued work; lobstah supplies the S3-specific path but not an autonomous decision owner | [`lobsterman.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/lobsterman.md), [`SKILL.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/plugins/claude-code/skills/lobsterman/SKILL.md) |
| Parent (`P`) | Human operator / dispatcher | `needs-decision`, `blocked`, fleet status or operator-observed need to redirect/cancel/swap current work | Wake/status reaches parent → parent decides → liaison/CLI sends answer or lifecycle intervention → worker/fleet subsequently changes state/behavior | [`vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md), [`lobsterman.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/lobsterman.md) |

## S3* — Complementary audit

- State: —
- Function: no first-party independent complementary audit/challenge role with findings-to-corrective-control closure is established.
- Disturbance / variety regulated: review feedback, PR gate state, worker evidence and external watch events can affect later work, but the independent judgment comes from an external reviewer/forge/CI/watch source rather than lobstah.
- Decisive decision or feedback right: not established as lobstah-owned S3*.
- Decision owner: external reviewers/forges/CI systems or the human operator for the inspected review paths.
- Supporting / enforcement mechanisms: evidence files, event logs, pickup review rule, merge view/gates, external watches and follow-up dispatches transport or enforce outside judgments.
- Closure path: external review/watch findings may be converted into a follow-up dispatch, but lobstah does not originate an independent complementary audit judgment of S1 work.
- Why this is / is not agent-owned: the design explicitly lists verdict/review UI as a non-goal; pickup transports `CHANGES_REQUESTED`/human review and forge status mechanically. Transporting an external auditor's verdict is not a first-party S3* owner.
- Evidence: [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md), [`docs/pickup.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/pickup.md), [`docs/vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: an external reviewer connected through `watch` or GitHub can supply real independent audit, but that separate actor's ownership is outside the lobstah boundary.

### Absence scope

- Surfaces inspected: worker evidence/events, pickup review dispatches, merge gates, GitHub approval policy, watches, lobsterman supervision and daemon liveness recovery.
- Plausible first-party paths checked: review-follow-up dispatches, `CHANGES_REQUESTED` pickup, ume/CI watch events, merge-gate checks, evidence collection and recovery classification.
- Why no material first-party path remains: all inspected challenge/verdict paths either transport externally produced findings or perform deterministic runtime/merge checks; no separate lobstah-owned reviewer obtains complementary evidence, judges S1 claims and returns those findings through corrective current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environment-facing adaptation loop that selects and installs changes to future lobstah/worker organizational capability is established.
- Disturbance / variety regulated: tracker changes, reviews, CI events and arbitrary watches can introduce new current-work information, but they drive present dispatch continuation rather than future-capability adaptation.
- Decisive decision or feedback right: not established as S4.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: pickup polling, external watches, persisted cursors, follow-up dispatches, harness swap and durable dispatch/session state.
- Closure path: environmental events may wake an operator or fork a continuation of the current work chain; no first-party loop turns prospective distinctions into selected changes to later reusable capabilities/programs.
- Why this is / is not agent-owned: watching external systems and reacting to a current PR/review/CI event is environment sensing inside ongoing operation. No learning/evolution/promotion path modifies future lobstah capability or organizational repertoire.
- Evidence: [`docs/pickup.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/pickup.md), [`docs/vocabulary.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/vocabulary.md), [`docs/lobsterman.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/lobsterman.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: swapping harnesses or forking a session changes execution of current work, not the future organizational capability set required for S4.

### Absence scope

- Surfaces inspected: tracker pickup, watches/streams, review/CI continuations, harness swap, durable state/evidence and plugin/skill behavior.
- Plausible first-party paths checked: external-event sensing, review feedback, automatic continuation, rebase chores, harness switching and any documented learning/self-improvement path.
- Why no material first-party path remains: the inspected mechanisms update or resume current work; none closes outside/prospective sensing → adaptation option → selection → promoted reusable future capability or changed organizational program.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established for the lobstah-managed fleet.
- Disturbance / variety regulated: configuration sets repositories, harness defaults, limits, concurrency, notifications, pickup scope and optional merge-approval rules, but these are operational policies rather than identity-level conflicts.
- Decisive decision or feedback right: not established as S5.
- Decision owner: user/deployer configuration for the inspected policy surfaces.
- Supporting / enforcement mechanisms: TOML configuration, merge approver lists/restricted labels, adapter defaults, CLI/auth boundary and explicit non-goals.
- Closure path: configuration constrains runtime behavior, but no identity/ultimate-policy issue is escalated to an authoritative S5 actor and returned as a governing organizational identity decision.
- Why this is / is not agent-owned: static policy and operator approval are not S5 merely because they constrain work. The repository intentionally keeps merge policy explicit and judgment outside deterministic pickup mechanics.
- Evidence: [`docs/design.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/design.md), [`docs/pickup.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/docs/pickup.md), [`README.md`](https://github.com/aequitas-labs/lobstah/blob/6aa75e2212fa8f22fa8dde7790070463c0021f8c/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: humans remain legitimate owners of many operational choices, but generic configuration and merge approval do not establish an S5 function.

### Absence scope

- Surfaces inspected: global/repo config, auth boundary, concurrency/limit policies, merge approval policy, plugins, tracker mappings and documented non-goals.
- Plausible first-party paths checked: operator configuration, human merge approval, restricted-label policy, harness choice, model choice and escalation/notification settings.
- Why no material first-party path remains: all found policy surfaces constrain ordinary execution/current control; none carries an identity/ultimate-policy issue to legitimate ultimate authority and returns an authoritative policy decision governing the fleet's identity.

## Distributed OSS parent arrangement

Repository maintainers govern development of lobstah, but that contributor/project recursion is adjacent to the assessed runtime fleet and is not used to claim parent notation. `S3=C(P)` instead rests on the supported runtime operator mode: the human dispatcher has a whole-fleet current view, receives explicit judgment escalations and returns interventions into the active fleet.

## Self-hosted and non-human modes

lobstah is self-hosted and local by design. The daemon can supervise and recover workers without continuous human attention, but judgment states intentionally escalate. A downstream deployment could place an autonomous supervisor over the shipped S3 constructor surface; that deployment would require its own evidence before becoming `S3=A`. The standard distribution separately supports direct human current control, which is why the parent modifier is recorded.

## Recursion

The assessed recursion is the local fleet. Individual dispatched coding-agent sessions are S1 units. Their own internal tools/subagents are below this level. Trackers, GitHub/Linear, external reviewer sessions, CI systems and model/harness vendors are environment or execution substrates. A larger organization that routes work across multiple lobstah homes/machines is a separate system-in-focus.

## Variety and escalation

Operational variety is absorbed through autonomous coding workers, isolated worktrees, adapter normalization, status/evidence contracts and bounded crash/wedge recovery. Cross-worker workspace variety is attenuated structurally by worktree isolation. Current fleet variety is summarized by `man tend`; ordinary liveness faults receive deterministic recovery, while `needs-decision`, `blocked`, failed rebase chores and other judgment points surface to the parent operator. At-least-once attention delivery with reminders prevents a missed wake from silently erasing the escalation.

## Evidence gaps

No first-party autonomous whole-fleet regulator was established at the pinned revision, so S3 is not raised from `C(P)` to `A(P)`. Reassessment would be warranted if the shipped lobsterman role gains and demonstrably exercises autonomous authority over whole-fleet commitments/interventions rather than primarily surfacing judgment to the human. Likewise, first-party independent review/audit or reusable capability-learning paths could change S3* or S4 in a later revision.