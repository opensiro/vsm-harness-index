---
harness_id: munder-difflin
project_name: Munder Difflin
repository: https://github.com/chaitanyagiri/munder-difflin
review_ref: c7c8921f4491104d342861e32fa214e486442304
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Munder Difflin

## Review boundary

- System in focus: the first-party Munder Difflin desktop harness/control layer at pinned revision `c7c8921f4491104d342861e32fa214e486442304`, including its Electron main process, hive filesystem/router, registry, blackboard, task ledger, hooks/inbox wake paths, worktree/control machinery, usage telemetry, circuit breaker, schedules/triggers, human-control surfaces and provider/PTY integration.
- Purpose and identity: organize a local “office” of terminal-based coding agents, provide durable coordination/control state around them, and expose one privileged GOD/orchestrator role plus worker roles to a human operator.
- Relevant environment: human operator; local repositories/worktrees; Claude Code, Codex and other supported terminal-agent CLIs; model/provider services behind those CLIs; Slack/webhook/schedule/voice triggers; git; local filesystem; MCP/skills; external repositories and task environments acted on by the CLI agents.
- Standard-distribution boundary: Munder Difflin owns the Electron control process, hive protocol and persistence, routing, role/prompt injection, PTY/provider lifecycle integration, budgets/breaker enforcement, schedules/triggers and human-control surfaces. The private reasoning/tool loops of the spawned `claude`, `codex`, `agy` and other terminal-agent processes remain adjacent agent runtimes. Merely launching a CLI in a PTY and injecting the hive protocol does not transfer that CLI runtime's autonomous task decision loop into first-party Munder Difflin ownership.
- Credited operating / distribution surfaces: `src/main/hive.ts`; first-party hooks/control/breaker/usage/telemetry paths; renderer/preload provider and PTY integration; first-party task ledger/blackboard/mailboxes; scheduler/heartbeat; bundled hive prompts/skills; worktree and trigger integration; local operator controls.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/test infrastructure, marketing/blog/rendered-site copies, research/design notes not wired into the shipped boundary, and documentation examples. External terminal-agent CLI internals, provider/model reasoning, their private planners/reviewers/policies/tool loops, and external MCP/service decisions are not credited as Munder Difflin-owned functions.
- First-party operating / deployment modes considered: local Electron desktop operation; GOD plus multiple worker PTYs; supported mixed-provider floors; auto-mode and interactive/HITL operation; scheduled/external-trigger re-engagement; circuit-breaker/budget enforcement; local worktree-backed coding workflows.
- Recursion level: the Munder Difflin office/hive control layer. Individual spawned terminal agents may themselves be autonomous systems at a lower recursion, but their internal autonomy is not inherited by the enclosing repository-relative harness merely because Munder creates, prompts, observes and coordinates their PTYs.
- Reviewed revision: `c7c8921f4491104d342861e32fa214e486442304`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Munder Difflin is a substantial first-party control substrate around terminal-agent CLIs. `src/main/hive.ts` implements an on-disk coordination layer with per-agent workspaces, registry, mailboxes, shared blackboard, task ledger, append-only event log and a router. The router applies concrete safety/coordination behavior such as a hop cap for runaway ping-pong. The harness also maintains PTYs, injects hive identity/protocol into supported providers, tracks sessions and usage, exposes worktree/fleet controls and persists organization state.

The repository nevertheless draws a strong mechanism/intelligence boundary. `HIVE.md` describes GOD as an ordinary `claude` process and calls that process the “intelligence”, while the main process is the “mechanism” for git, sockets/routing and related control machinery. The maintainer's GOD-orchestrator explanation is even more explicit: the mechanism has no judgment; the ordinary `claude` GOD process reads requests and decides what to do, with routing/escalation policy expressed through its prompt. The actual spawn path builds a PTY command from a selected provider and submits the first-party GOD/hive prompt into that provider runtime.

This boundary is not erased by the strength of Munder's deterministic control layer. The circuit breaker owns a first-party runaway/cost guardrail policy and computes a steer → constrain → stop decision from usage, repeated-tool/error signals and progress signals; the main heartbeat enforces those actions around agent PTYs. Scheduled missions and external triggers can re-engage the GOD process without a human continuously driving the UI. Semantic memory, tasks, blackboard and mailboxes preserve state across sessions. These are material harness capabilities, but the arbitrary task interpretation, plan selection, adjudication and tool/action choices still occur inside the spawned terminal-agent process.

Primary evidence:

- [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md) — hive architecture, GOD role, mailboxes/blackboard/task state, escalation policy, and explicit “ordinary `claude` process” intelligence versus main-process mechanism boundary.
- [`src/main/hive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/hive.ts) — first-party hive registry/state/router, hop guard, task ledger, protocol injection and provider-aware agent metadata.
- [`src/renderer/src/hooks/useHive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/renderer/src/hooks/useHive.ts) — GOD PTY creation from the selected provider command and submission of the GOD/hive prompt to that runtime.
- [`src/main/breaker.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/breaker.ts) — first-party deterministic runaway/cost policy and steer/constrain/stop decision ladder, including the explicit separation between policy calculation and caller enforcement.
- [`src/main/index.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/index.ts) — heartbeat/breaker enforcement and GOD re-engagement paths.
- [`src/main/memory.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/memory.ts) — shared semantic-memory plumbing around agents' `memory.md` state.
- [`README.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/README.md) — supported harness/control capabilities, budgets, schedules, GOD/worker organization and autonomy/HITL positioning.

## Operational model

A Munder Difflin run creates one or more PTYs backed by external terminal-agent CLIs. First-party spawn/protocol machinery supplies each process with hive identity, role, mailbox/blackboard/task conventions and control context. The GOD process is privileged organizationally: it sees the roster and shared state, adjudicates routine cross-agent requests, dispatches work and escalates selected matters. Workers perform delegated coding/research tasks and communicate through hive files/messages. The main process routes messages, persists coordination state, monitors signals, schedules wakeups, applies budgets/breaker actions and exposes human controls.

The counterfactual owner test separates the layers. Remove the selected `claude`/Codex/other CLI processes while leaving Munder's Electron process, hive files, router, scheduler, breaker, task ledger and prompts intact: the mechanism can still store, route, schedule and enforce rules, but no autonomous actor remains that can interpret an arbitrary task, choose a plan/tool/action, judge substantive worker output or decide how to resolve a novel request. Remove the Munder mechanism while leaving a CLI runtime: that CLI still contains its own autonomous model/tool loop, although it loses the office-level coordination substrate. The standard Munder distribution therefore does not establish a first-party autonomous S1 decision/action loop under the repository-relative Index boundary.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit that owns the arbitrary task-level decision/action loop is established inside the Munder Difflin repository boundary.
- Disturbance / variety regulated: coding/research/task-environment variety, tool outcomes, repository state, requester ambiguity and execution failures are interpreted substantively by the spawned terminal-agent runtime.
- Decisive decision or feedback right: interpret the task and observations, choose the next substantive plan/tool/action, evaluate returned evidence and revise the course of work.
- Decision owner: the spawned terminal-agent process (`claude`, Codex or another configured provider CLI), not the deterministic Munder main process.
- Supporting / enforcement mechanisms: PTY lifecycle, hive protocol injection, mailboxes, registry, blackboard, task ledger, worktrees, hooks, schedules, budgets, breaker and operator controls.
- Closure path: request/trigger → Munder routes/wakes/injects context → external CLI agent interprets and acts → Munder records/routes/enforces resulting events → external CLI agent chooses the next substantive action. The autonomous task loop closes in the adjacent CLI runtime.
- Why this is / is not agent-owned: the repository itself calls the GOD “an ordinary `claude` process” and distinguishes that intelligence from a main-process mechanism that has no judgment. Provider selection and prompt injection configure an adjacent autonomous actor rather than implementing its task loop.
- Evidence: [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md), [`src/renderer/src/hooks/useHive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/renderer/src/hooks/useHive.ts), [`src/main/hive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/hive.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a deployed Munder office clearly contains autonomous agents in ordinary usage; this finding is about first-party repository-relative ownership, not whether the assembled deployment is agentic in a colloquial sense.

### Absence scope

- Surfaces inspected: HIVE architecture; PTY/provider spawn path; hive router/state; task ledger/blackboard; hooks; breaker/budget path; memory; schedules/triggers; operator controls and maintainer architecture explanations.
- Plausible first-party paths checked: GOD as a first-party S1 implementation; worker PTY wrapper as S1; scheduler/heartbeat as S1; breaker as S1; prompt/skills as transfer of CLI ownership.
- Why no material first-party path remains: first-party code supplies context, organization, persistence and deterministic regulation, while every general task-level autonomous choice still requires the separately implemented terminal-agent process.

## S2 — Coordination

- State: —
- Function: Munder contains real coordination machinery for an office of agents, but the distinct operational agents being coordinated are adjacent CLI runtimes rather than first-party Munder-owned S1 units at this recursion.
- Disturbance / variety regulated: duplicate/conflicting work, cross-agent requests, shared-repository interference, message ping-pong and dependency/order problems.
- Decisive decision or feedback right: decide task partitioning/ownership, resolve cross-agent requests and conflicts, and alter subsequent worker commitments.
- Decision owner: substantively, the external GOD/worker agent processes; the router and task state deterministically transport/enforce their messages and recorded commitments.
- Supporting / enforcement mechanisms: atomic per-agent inbox/outbox files, shared blackboard, task ledger/dependencies, worktrees, registry, broadcast selection and router hop cap.
- Closure path: external agent/GOD chooses a coordination action → first-party hive state/router persists and delivers it → recipient external agent changes later behavior. The first-party mechanism closes transport/enforcement, but not an S2 decision among first-party S1 units.
- Why this is / is not agent-owned: this is stronger than generic messaging — the hop cap, task state and shared-work conventions address concrete interference modes — but the Profile requires distinct S1 units at the declared recursion before publishing S2. Those autonomous units are the adjacent terminal-agent runtimes here.
- Evidence: [`src/main/hive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/hive.ts), [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md).
- Basis: structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: at a wider assembled-system boundary that intentionally treats the hosted CLI agents as constituent S1 units, the same router/task/worktree mechanisms would be material S2 evidence; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: router/mailboxes, hop guard, blackboard, task ledger/dependencies, worktree organization, registry and GOD/worker coordination contract.
- Plausible first-party paths checked: router anti-livelock as S2; task dependencies as S2; worktrees as collision attenuation; GOD adjudication as first-party S2 ownership.
- Why no material first-party path remains: the coordination substrate is first-party, but the decisive coordinating judgments and the coordinated autonomous S1 actors are supplied by external CLI processes under this repository-relative boundary.

## S3 — Inside-and-now control

- State: —
- Function: Munder implements substantial current-control support and deterministic regulation around the running floor, but no first-party autonomous S3 owner over first-party S1 operations is established.
- Disturbance / variety regulated: current workload/agent state, runaway loops, token/cost growth, failures, task status, worker availability and live intervention needs.
- Decisive decision or feedback right: choose current priorities/commitments and substantive interventions across operations; distinguish that from enforcing configured caps or a fixed breaker ladder.
- Decision owner: GOD's discretionary current-control judgments belong to the external CLI agent; operator decisions belong to the human; breaker/budget decisions are deterministic policy/enforcement in Munder.
- Supporting / enforcement mechanisms: live registry/fleet state, task ledger, usage/telemetry, per-agent/floor budgets, circuit breaker, pause/halt/steer/kill controls, heartbeat and PTY lifecycle.
- Closure path: external GOD or human selects a substantive intervention, or deterministic breaker thresholds trip → Munder routes/enforces the resulting constraint/action → CLI agent behavior changes. Enforcement is first-party; the organizational discretion is not a first-party autonomous S3 owner.
- Why this is / is not agent-owned: `breaker.ts` explicitly owns a deterministic policy/decision ladder, but Profile 0.2.3 separates enforcement authority from organizational decision ownership. Likewise GOD naming does not make the ordinary external `claude` process a first-party Munder S3 implementation.
- Evidence: [`src/main/breaker.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/breaker.ts), [`src/main/index.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/index.ts), [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md).
- Basis: explicit + structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: deterministic breaker regulation is real and operationally important; `—` here does not mean “no controls”, only no qualifying first-party autonomous/constructor S3 path after function/owner separation at this boundary.

### Absence scope

- Surfaces inspected: GOD current-control description, registry/task state, usage/telemetry, breaker policy, heartbeat enforcement, budgets and operator intervention controls.
- Plausible first-party paths checked: GOD as S3; circuit breaker as autonomous S3; scheduler/heartbeat as S3; Command Center/human intervention as a Methodology parent mode.
- Why no material first-party path remains: whole-floor data/enforcement exist, but discretionary whole-system current control is either exercised by the adjacent GOD CLI or by a human; the deterministic breaker does not inherit ownership of the underlying priorities/policy simply because it enforces configured thresholds.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established beyond the normal control/observability surfaces.
- Disturbance / variety regulated: possible false operational claims, hidden failure or divergence from reported task/runtime state.
- Decisive decision or feedback right: independently challenge ordinary operational reporting using materially different access to reality and feed findings into later control.
- Decision owner: no qualifying first-party independent audit owner identified.
- Supporting / enforcement mechanisms: event logs, transcripts, usage telemetry, OTel, task state, hooks and worktree/repository observations.
- Closure path: routine telemetry/log/hook evidence feeds normal monitoring and breaker/control paths; no separate independent auditor with complementary access and returned audit judgment was established.
- Why this is / is not agent-owned: observability, logs, hook events and routine result checking are evidence sources but are not automatically S3* under the Profile.
- Evidence: [`src/main/telemetry.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/telemetry.ts), [`src/main/breaker.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/breaker.ts), [`src/main/hive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/hive.ts).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: the repository contains extensive test/research material, but development/evaluation surfaces were not borrowed into the shipped office runtime without evidence of deployment-boundary reachability.

### Absence scope

- Surfaces inspected: runtime telemetry/OTel, transcript/usage seam, hook events, event log/task state, breaker inputs, worktree/runtime monitoring and repository test/evaluation material.
- Plausible first-party paths checked: telemetry as S3*; transcript inspection as S3*; tests/review material as S3*; GOD checking workers as an independent audit path.
- Why no material first-party path remains: the identified signals belong to routine control/observability or adjacent development surfaces; no operationally wired, sufficiently independent complementary auditor and feedback closure was established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside-and-then adaptation loop is established in Munder's mechanism independently of the external agent intelligence.
- Disturbance / variety regulated: environmental/project changes, new tools/providers, future capability needs and changing task opportunities would need to be sensed, turned into adaptation options and returned to present capability.
- Decisive decision or feedback right: form prospective adaptation options from external distinctions and choose how current capability should change.
- Decision owner: when such reasoning occurs during a run, it is performed by the external GOD/worker CLI agent or by the human/operator/developer, not by first-party deterministic Munder machinery.
- Supporting / enforcement mechanisms: scheduled missions, external triggers, durable/semantic memory, shared blackboard, provider configuration and prompt/skill surfaces.
- Closure path: scheduler/trigger/memory can present new context to the external GOD/worker process; that process interprets it and may propose/perform adaptation. The mechanism itself does not close the prospective judgment loop.
- Why this is / is not agent-owned: scheduled re-engagement, memory mining and generic learning/recall do not by themselves satisfy the Profile's external-and-prospective S4 test. They transport context to the adjacent intelligence.
- Evidence: [`src/main/memory.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/memory.ts), [`src/main/index.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/index.ts), [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: external agent processes may themselves conduct rich environmental research/adaptation; this assessment does not import those private agent decisions into Munder ownership.

### Absence scope

- Surfaces inspected: scheduled missions/heartbeat, Slack/webhook/external triggers, semantic memory, blackboard, provider/model configuration, GOD prompt and architecture/design material.
- Plausible first-party paths checked: schedules as S4; memory/semantic recall as S4; provider switching/config as S4; GOD adaptation as first-party S4.
- Why no material first-party path remains: first-party mechanisms collect/persist/present context or apply configuration, while the prospective environmental interpretation and adaptation judgment reside in the adjacent CLI agent or human/developer.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure path is established at the Munder office recursion.
- Disturbance / variety regulated: identity-level purpose, ultimate policy boundaries and unresolved S3–S4 tensions would require legitimate authority and a returned decision governing later operation.
- Decisive decision or feedback right: decide the office's identity/ultimate policy rather than merely enforce safety constraints or approve an ordinary tool action.
- Decision owner: escalation policy is configured in prompts and critical actions may reach the human through the external agent's session/tool permission flow; no qualifying first-party autonomous S5 owner or explicit identity-level parent closure was established.
- Supporting / enforcement mechanisms: GOD/system prompt, autonomy modes, spend/scope/destructive-action guardrails, tool permission prompts, operator settings and control gates.
- Closure path: ordinary critical/tool actions can be escalated to a human and then allowed/denied, but the reviewed evidence does not establish an identity/ultimate-policy issue → legitimate parent authority → returned identity/policy decision → later office governance loop.
- Why this is / is not agent-owned: a system prompt, static policy, operator gate or human approval is not S5 by name under the Profile. The repository's prompt-based escalation policy constrains/steers the adjacent GOD process but does not establish first-party ultimate-policy ownership.
- Evidence: [`HIVE.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/HIVE.md), [`src/main/hive.ts`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/src/main/hive.ts), [`README.md`](https://github.com/chaitanyagiri/munder-difflin/blob/c7c8921f4491104d342861e32fa214e486442304/README.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: humans clearly retain legitimate authority over their local deployment. Methodology 0.3.5 does not publish `P` merely from generic approvals/settings; a function-specific identity/ultimate-policy closure must be evidenced.

### Absence scope

- Surfaces inspected: GOD/escalation prompt, human permission/remote-control path, autonomy settings, spend/scope/destructive-operation gates, operator configuration and control APIs.
- Plausible first-party paths checked: GOD prompt as S5; human tool approval as S5=P; breaker/budget configuration as policy ownership; operator settings as ultimate-policy closure.
- Why no material first-party path remains: these paths constrain or approve operational actions, but the reviewed standard distribution does not establish the specific identity/ultimate-policy decision-and-return loop required for S5 publication.

## Distributed OSS parent arrangement

The assessment concerns the shipped local desktop harness, not the GitHub contributor organization. Maintainer/contributor governance, release decisions and repository development workflows are adjacent to the runtime system-in-focus and are not used to infer organization-level parent governance for S3/S4/S5.

## Self-hosted and non-human modes

Munder is local/self-hosted and exposes meaningful operator control, but operator presence alone does not create a positive parent-mode state. The current-control paths inspected for S3 and the approval/policy paths inspected for S5 do not overcome the more basic exclusion boundary: Munder's autonomous actors are externally implemented terminal-agent runtimes, while its first-party mechanism provides organization and enforcement around them.

## Recursion

The clearest recursive candidates are the spawned GOD and worker CLI agents: each may maintain its own context, tools, local environment and decision loop. At the reviewed repository boundary these are adjacent agent runtimes integrated through PTYs and the hive protocol. Spawning them, assigning roles and persisting their state does not by itself transfer their lower-recursion viability or autonomy into a first-party Munder S1 implementation.

## Variety and escalation

Munder handles substantial operational variety structurally: provider/runtime differences, asynchronous mail, worktree state, task dependencies, cost/token growth, repeated-tool/error loops, idle/quiet-floor re-engagement and human escalation. Variety is attenuated through routing, hop caps, task state, budgets and breaker escalation; amplified through multiple agent PTYs and external triggers; transduced through prompts/files/hooks/PTYs. These mechanisms show a sophisticated harness even though the decisive task intelligence remains in adjacent CLI runtimes.

The GOD escalation path is particularly clear: routine cross-agent matters are intended for GOD; critical matters can reach the human. That is useful organizational evidence, but function-first classification still requires the underlying VSM function and owner. Generic escalation/approval is therefore not promoted to S5, and breaker enforcement is not promoted to autonomous S3 ownership.

## Evidence gaps

No material evidence gap changes the boundary result. The repository contains both implemented runtime machinery and design/marketing documentation with some historical wording differences around approvals; the assessment prioritizes frozen first-party source and explicit architecture statements. In particular, current `src/main/hive.ts` describes native per-agent Claude-session HITL rather than relying on a separate harness-owned approval queue, so older prose about an approvals queue is not used as positive ownership evidence.

**Proposed terminal outcome:** `excluded-no-agentic-vsm`. Munder Difflin is a substantive harness/control layer, but at the pinned standard-distribution boundary it does not supply its own autonomous operational decision/action loop. The Index should record the completed assessment without borrowing Claude Code/Codex/other CLI autonomy into first-party Munder ownership.