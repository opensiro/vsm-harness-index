---
harness_id: swe-mux
project_name: swe-mux
repository: https://github.com/jatoran/swe-mux
review_ref: c14351b48a5424d2941b8a2e0e63b56f7033d2a0
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# swe-mux

## Review boundary

- System in focus: one first-party swe-mux installation at pinned revision `c14351b48a5424d2941b8a2e0e63b56f7033d2a0`, including the shipped daemon/supervisor, Mux assistant, project/session/fleet state, prompt queues and permissions, land/reconciliation machinery, deterministic evidence consumers, attention routing, update machinery and supported browser/desktop/operator surfaces.
- Purpose and identity: provide a local control organization for running several coding-agent sessions together, preserving their state and evidence, routing operator work, coordinating parallel branches, surfacing exceptions and maintaining the installed control plane as its environment changes.
- Relevant environment: operator requests and decisions; Claude Code, Codex and other provider CLI/model runtimes; project repositories/worktrees; Git and verification commands; model endpoints used by the Mux assistant and scan/narration services; devices/browsers; provider/account state; upstream swe-mux releases.
- Standard-distribution boundary: repository-owned daemon, supervisor, assistant, session/project state, automation/control services, land queue, evidence/attention services and updater are inside. Provider CLI binaries, their internal model/tool loops, external model-provider inference, repositories and upstream release infrastructure are dependencies/environmental actors. Launched provider sessions may participate as operational work cells in first-party coordination/control relations, but their internal reasoning or VSM functions are not imported as first-party ownership evidence.
- Credited operating / distribution surfaces: `README.md`; `pyproject.toml`; `src/swe_mux/__main__.py`; `src/swe_mux/server.py`; `src/swe_mux/assistant.py`; `src/swe_mux/land_queue.py`; `src/swe_mux/deterministic_consumers.py`; `src/swe_mux/attention_ranking.py`; `src/swe_mux/scan_timeline.py`; `src/swe_mux/config.py`; `src/swe_mux/update_check.py`; `src/swe_mux/update_install.py`; their standard daemon composition paths.
- Adjacent first-party surfaces excluded from ownership: `.docs` design/roadmap claims where the frozen runtime does not wire the claimed path; demo/simulated activity; repository-development CI, release publishing, contribution/governance and DCO workflows; tests/fixtures except as corroboration; upstream release production itself. These surfaces do not donate product-runtime S-functions merely because they are first-party.
- First-party operating / deployment modes considered: installed wheel/daemon/browser operation; Windows desktop wrapper over the same daemon; Mux assistant with a configured supported model endpoint; reversible assistant actions under `auto`, `cancel_window` and `confirm` trust modes; supervised external coding-agent sessions; Project-enabled automation/land queue/evidence consumers; frozen-app in-app update planning/install mode.
- Recursion level: one swe-mux installation/control organization. A launched coding-agent session can be treated as an operational work cell where first-party swe-mux explicitly regulates a concrete cross-session/worktree disturbance, but the provider harness inside that process remains an external dependency and is not recursively assessed here.
- Reviewed revision: `c14351b48a5424d2941b8a2e0e63b56f7033d2a0`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

swe-mux ships a Python daemon and browser/desktop control plane around coding-agent terminal sessions. The daemon owns durable project/session state, PTY supervision, prompt queues, Project authority settings, land/reconciliation state, evidence/telemetry, recovery and multiple background control services. Claude Code, Codex and similar provider CLIs remain separate executables whose internal reasoning/tool loops are not implemented by swe-mux.

The frozen revision also ships a distinct first-party autonomous actor: the Mux assistant. `server.py` constructs an `OpenRouterClient`, wires an `AssistantService` to live projects/sessions and real daemon operations, and publishes the service in the standard app. `assistant.py` gives that actor a live fleet snapshot and a bounded multi-round model/tool loop. The model may inspect session/project state and choose first-party tools for history, notes, queue state, project creation, session spawning, session messaging and approved Project Actions. Tool results are appended back into the model conversation and can alter the next model decision. This first-party loop establishes autonomous S1 without borrowing a provider CLI's internal agent loop.

Parallel coding sessions are organized through additional first-party machinery. The land queue exists specifically because several agents can finish branches concurrently. It serializes reconciliation, approved verification and fast-forward landing; if reconciliation conflicts or verification fails, it returns bounded evidence to the branch's owning agent. The source is explicit that the queue itself never decides how to repair those failures. The disturbance-specific feedback path is therefore real, while the autonomous conflict-resolution judgment remains with the external worker agent unless an adopter composes a first-party owner for that relation.

The Mux assistant also supplies a current whole-fleet control path. Its system contract calls it a fleet manager, injects a freshness-stamped snapshot of live sessions/projects into turns, and instructs it to route code work to an existing session or spawn a new one. The daemon exposes reversible mutations under three supported trust modes: `auto`, `cancel_window` and `confirm`. In `auto`, the assistant can close reversible fleet/resource decisions such as spawning a session without a parent decision; in `confirm`, the same proposed current-control mutation waits for an explicit operator decision before the ordinary daemon operation changes current state. Consequential operations remain parent-confirmed and are not used to prove the autonomous base mode.

A separate evidence stack observes operation outside ordinary agent self-report. Tier-0 facts feed deterministic consumers that detect repeated no-progress activity, completion claims unsupported by verification and related discrepancies; scan-timeline adds a model-derived behavioral record over transcript deltas plus deterministic facts; attention ranking groups and routes findings to the operator. These surfaces are wired and started by the standard daemon. They provide materially complementary access to operational reality, but the normal distribution does not assign an autonomous independent auditor the decisive audit judgment and corrective authority, so the first-party path is published as an S3* constructor rather than `A`.

Finally, the installed control plane has a narrow but closed prospective adaptation path. `UpdateChecker` periodically senses the external published release contract and detects a newer version. `UpdateInstaller` can plan the concrete future swap/replace consequences, verify release bytes, stage the candidate, invoke the existing health-checked swap and roll back if the replacement never becomes healthy. Installation never proceeds without an explicit operator act naming the version; supervisor-protocol changes additionally require explicit consent because they end live sessions. The operator therefore owns the decisive adaptation right, and the returned decision changes the installed runtime capability. This is parent-governed S4, not autonomous self-improvement.

Primary evidence:

- [`README.md`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/README.md) — installed operating model, external CLI boundary, assistant, session coordination, land queue, evidence/recovery and local control scope.
- [`pyproject.toml`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/pyproject.toml) and [`src/swe_mux/__main__.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/__main__.py) — shipped daemon entrypoint.
- [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py) — standard composition of provider adapters, `AssistantService`, land queue, evidence/attention services, update checker/installer and their operational dependencies.
- [`src/swe_mux/assistant.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/assistant.py) — first-party fleet-manager model/tool loop, live fleet snapshot, daemon-backed tool repertoire and trust-mode execution.
- [`src/swe_mux/config.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/config.py) — supported `auto` / `cancel_window` / `confirm` assistant trust modes and current-control configuration.
- [`src/swe_mux/land_queue.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/land_queue.py) — explicit parallel-branch interference, serialized landing, verification and conflict/failure return to the owning agent.
- [`src/swe_mux/deterministic_consumers.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/deterministic_consumers.py), [`src/swe_mux/scan_timeline.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/scan_timeline.py), and [`src/swe_mux/attention_ranking.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/attention_ranking.py) — complementary fact/claim/progress checks and return into operator control channels.
- [`src/swe_mux/update_check.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/update_check.py) and [`src/swe_mux/update_install.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/update_install.py) — external release sensing, future install planning, explicit operator decision, verified staged swap and rollback.

## Operational model

The first positive S1 path is the Mux assistant itself, not Claude Code or Codex. A user turn plus live workspace state enters a first-party bounded model/tool loop; the assistant chooses reads or permitted workspace/fleet mutations, observes their results and continues until it replies or exhausts the bounded turn. External model inference is a dependency, but first-party swe-mux owns the loop, action vocabulary, observations, trust boundary and return path.

Provider CLI sessions remain black-box external agent actors internally, while first-party swe-mux owns their session/worktree identities and the organizational relations around them. That distinction matters for S2 and S3: branch collision, shared landing order and current fleet allocation can be mapped because swe-mux itself establishes those relations, while no provider's internal planning, verification or management function is inherited.

Current-control has two explicitly supported ownership modes. In `auto`, the assistant can select and execute reversible fleet/resource actions through daemon operations. In `confirm`, the assistant may develop the same current-control proposal from the same live fleet view, but the operator owns whether the proposal proceeds. This is the basis for `S3=A(P)` rather than treating deterministic enforcement or generic UI access as management.

## S1 — Operations

- State: A
- Function: perform goal-directed workspace/fleet assistance through a first-party model/tool loop that can inspect current state, choose actions, observe results and continue until a bounded turn completes.
- Disturbance / variety regulated: ambiguous operator requests, live project/session state, queue and transcript findings, action availability, tool results/errors, model output and changing workspace/fleet state during a turn.
- Decisive decision or feedback right: choose the next substantive assistant action/tool, decide whether to inspect more state or mutate the workspace/fleet within available authority, interpret returned results and decide what action or answer follows.
- Decision owner: the model-driven Mux assistant actor running through first-party `AssistantService`.
- Supporting / enforcement mechanisms: `OpenRouterClient`, `AssistantStore`, fleet snapshot construction, named project/session resolution, bounded model-call ceiling, daemon tool adapters, trust policy, SQLite dialogue/action state and existing spawn/queue/note/Project Action operations.
- Closure path: operator turn plus live snapshot → Mux model chooses answer/tool calls → first-party service resolves and executes allowed tools → tool results return as model-visible observations → model revises/continues → final response or bounded termination.
- Boundary reachability: `server.py` constructs and publishes `AssistantService` in the standard daemon, wiring it to `OpenRouterClient`, projects, sessions, prompt queue, spawn/interrupt/end operations, history, notes and approved Project Actions; `assistant.py` implements the iterative tool-result loop reached by normal assistant turns.
- Why this is / is not agent-owned: deterministic code constrains actions and performs side effects, but it does not select the substantive next assistant action. Removing the model-driven assistant while leaving the daemon operations intact leaves tools and state without the goal-directed decision loop.
- Evidence: [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py); [`src/swe_mux/assistant.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/assistant.py); [`README.md`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference is a dependency and provider coding-agent loops are separately excluded; the positive S1 claim is limited to the first-party Mux assistant organization.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference among parallel coding-agent work cells when several branches need reconciliation/verification/landing against one project trunk.
- Disturbance / variety regulated: concurrent branches can collide during reconcile/merge, compete for the trunk landing sequence, fail the shared verification gate or become unsafe to merge while another session occupies the same worktree.
- Decisive decision or feedback right: order eligible land operations and, when reconciliation or verification fails, determine the corrective branch change required before that work cell can re-enter the landing sequence.
- Decision owner: constructor path only. swe-mux owns the disturbance-specific serialization, detection and handback path; the branch's external worker agent owns the intelligent correction after a conflict/failed check, so the standard first-party distribution does not close autonomous S2 ownership by itself.
- Supporting / enforcement mechanisms: `LandQueueService`, per-root in-flight exclusion, busy-session checks, fixed Git mutation vocabulary, approved verification command, fast-forward-only trunk update, durable land state and Phase-5 handback queue.
- Closure path: several session branches become land candidates → first-party queue serializes one root/branch operation → reconcile and approved verify run → a conflict or failed gate is captured → bounded evidence returns to the owning session → that worker can alter the branch → a later request/retry re-enters the first-party land path.
- Boundary reachability: `server.py` constructs `LandQueueService` with live sessions/projects, grants, verification, prompt-queue handback and branch state, restores it and starts its supervised loop in the standard daemon.
- Why this is / is not agent-owned: the queue deterministically attenuates collision but its own source explicitly says it never decides how to resolve a conflict or verification failure; that intelligence belongs to the branch's agent. The first-party path is therefore function-specific `C`, not `A`.
- Evidence: [`src/swe_mux/land_queue.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/land_queue.py); [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py); [`README.md`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic messaging/help/progress primitives are not used as S2 evidence. The positive mapping is limited to the concrete parallel-branch/trunk interference and first-party handback relation.
- Distinct S1 units: two or more launched coding-agent session/worktree cells contributing separate branch outcomes to the same Project. Their provider-internal reasoning remains external and is not used as first-party ownership evidence.
- Inter-S1 disturbance: parallel branch outcomes can conflict during reconcile/merge, compete for the single trunk landing point or fail a shared verification gate whose resolution must be incorporated before another landing attempt.
- Attenuating coordination relation: the land queue serializes root/branch progression, evaluates explicit preconditions, reconciles against trunk, runs an approved verification command and permits only fast-forward trunk landing; conflicts/failed checks are removed from the automatic progression rather than allowed to collide destructively.
- Feedback into subsequent S1 behaviour: the failed reconcile/verification result is returned through the bounded prompt queue to the branch's owning session, where the worker can change its branch before re-entering the landing relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the queue exists to regulate a named cross-work-cell Git/trunk interference, detects concrete conflict/failure states and returns those states to the affected work cell; the positive mapping does not rest on session plurality or a generic mailbox.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain a current whole-fleet view and regulate present session/work commitments by routing new work, allocating a new session when needed and applying bounded current-control interventions through the shared daemon.
- Disturbance / variety regulated: several live/cold sessions across projects can be working, awaiting input, stale, blocked or absent; a new operator request can fit an existing work cell or require additional capacity, and current fleet state changes which intervention is appropriate.
- Decisive decision or feedback right: from the live fleet state, decide whether to route work to an existing session or create/allocate a new one and execute the chosen reversible current-control action under the selected trust mode.
- Decision owner: Mux assistant in the autonomous `auto` mode; operator in the distinct `confirm` parent mode for the same reversible current-control proposal.
- Supporting / enforcement mechanisms: freshness-stamped fleet snapshot, `session_detail`, queue/session tools, spawn contract, project/session resolution, daemon action ledger, reversible-action trust policy and existing session spawn/message operations.
- Closure path: current fleet/project state enters the assistant snapshot → assistant judges the present routing/resource need → in `auto`, the reversible action executes through the daemon; in `confirm`, the action is held until the operator accepts/rejects → the resulting session/queue state changes subsequent current operation and appears in later snapshots.
- Boundary reachability: the standard `AssistantService` receives live `SessionManager`/`ProjectManager` state and first-party spawn/queue operations. `config.py` exposes `auto`, `cancel_window` and `confirm` as supported reversible trust modes; no adopter-written manager is required.
- Why this is / is not agent-owned: the autonomous base state rests on the assistant's model-driven choice among current fleet allocations, not on a scheduler, supervisor or hard gate. The parent mode is separately evidenced by `confirm`, where the operator rather than the model owns whether that same S3 resource action proceeds.
- Evidence: [`src/swe_mux/assistant.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/assistant.py); [`src/swe_mux/config.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/config.py); [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `cancel_window` is not treated as parent ownership merely because a human can veto; the parent-mode claim relies on the explicit `confirm` configuration. Consequential interrupt/end operations always require confirmation and are not used to prove the autonomous base mode.
- Whole-system current view: the assistant receives a daemon-generated snapshot spanning current projects and up to the bounded supported fleet context, with session state, ages, awaiting/idle/running information and names that bind subsequent tools to live entities.
- Current-control decision scope: present allocation/routing of work among existing sessions versus creating additional session capacity, plus bounded reversible fleet actions. Static limits and daemon enforcement support this right but do not own it.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Mux assistant | current fleet snapshot plus operator work request under `assistant_trust_reversible=auto` | model selects a reversible fleet/resource action → daemon executes it → session/queue state changes and re-enters later fleet context | `assistant.py`, `config.py`, `server.py` |
| Parent (`P`) | installation operator | same S3 proposal under `assistant_trust_reversible=confirm` | model proposes action → daemon creates pending confirmation → operator decides → accepted decision executes through the same daemon operation and changes current fleet state | `assistant.py`, `config.py` |

## S3* — Complementary audit

- State: C
- Function: challenge ordinary session/self-report claims and progress signals with a materially different first-party evidence path over deterministic operational facts, then surface discrepancies into current control.
- Disturbance / variety regulated: an agent may claim completion without verification, repeat ineffective actions, stall, run away, encounter context pressure or present status that routine transcript/self-report alone does not make trustworthy.
- Decisive decision or feedback right: judge that ordinary operational reporting is contradicted or insufficient on the basis of complementary process/file/test/fact evidence and determine what corrective scrutiny should follow.
- Decision owner: constructor path only. The frozen standard distribution ships independent fact capture, deterministic discrepancy detectors and attention routing, but it does not assign an autonomous auditor both the decisive complementary-audit judgment and corrective control right across these findings.
- Supporting / enforcement mechanisms: Tier-0 fact store, deterministic consumer queries, transcript claim parsing, test-result facts, scan-timeline records, incident grouping, confidence/ranking and bounded attention channels.
- Closure path: operational facts/transcript state → deterministic complementary detector and/or semantic scan produces a finding → attention service groups/ranks it → operator receives a concrete action such as redirecting a stuck run or requiring verification → a separately composed autonomous auditor/controller could consume the same first-party path without reimplementing evidence capture.
- Boundary reachability: `server.py` creates and starts Tier-0 capture, `DeterministicConsumerService`, `ScanTimelineService` and `AttentionRankingService` in the normal daemon; this is not a test-only or repository-development evaluator.
- Why this is / is not agent-owned: the complementary path is product-runtime first-party and materially independent of ordinary self-report, but deterministic detectors/routers do not become an autonomous audit owner merely because they can issue strong findings. The autonomous judgment/closure still requires composition, so the publication state is `C`.
- Evidence: [`src/swe_mux/deterministic_consumers.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/deterministic_consumers.py); [`src/swe_mux/scan_timeline.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/scan_timeline.py); [`src/swe_mux/attention_ranking.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/attention_ranking.py); [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary worktree verification alone is not credited as S3*. The positive mapping depends on complementary fact/claim/progress inspection outside the worker's ordinary report and its standard-daemon reachability; the missing autonomous audit owner prevents `A`.
- Claim being audited: whether current work is genuinely progressing and whether completion/progress claims are supported by operational evidence such as changed state and verification/test facts.
- Ordinary reporting path: provider-session transcript/status and the worker's own completion/progress statements.
- Complementary access path: Tier-0 operational facts plus deterministic repeated-action/test/claim checks and scan-derived behavioral records, routed independently of the worker's own declared conclusion.
- Independence boundary: evidence capture/detectors live in the swe-mux control plane rather than inside the provider agent being observed and can challenge the provider transcript with process/file/test facts.
- Who acts on findings: the standard path routes findings to the operator through attention channels; autonomous audit/control ownership would require an additional composed actor, which is why this remains `C`.

## S4 — Outside-and-then intelligence

- State: P
- Function: sense an external change in available swe-mux capability, develop a concrete future install option with operational consequences, and let legitimate parent authority decide whether that option becomes the installation's present capability.
- Disturbance / variety regulated: upstream swe-mux can publish a newer release whose binaries, bundle contents or supervisor protocol differ from the installed version; adopting it may preserve the live fleet or require ending sessions and replacing the supervisor.
- Decisive decision or feedback right: decide whether to replace the current installed capability with the specifically identified newer release after seeing its plan/impact, including any supervisor replacement consequence.
- Decision owner: the installation operator as legitimate parent authority for this self-hosted deployment.
- Supporting / enforcement mechanisms: periodic `UpdateChecker`, external version manifest/GitHub fallback, update planning, artifact/hash verification, staged download, bundle metadata, swap/replace applier, health check and rollback.
- Closure path: external release manifest signals newer capability → updater derives the candidate/version and install consequences → operator explicitly chooses the named release and, when required, separately consents to supervisor replacement → verified artifact is staged/swapped → health check keeps or rolls back the new runtime → subsequent operation runs the returned capability decision.
- Boundary reachability: `server.py` constructs and starts `UpdateChecker`, constructs/publishes `UpdateInstaller` and wires update swap announcements in the standard daemon; `update_install.py` documents and enforces the explicit-gesture/version-consent path.
- Why this is / is not agent-owned: detection, validation and swap are deterministic support. The operator owns the prospective adaptation judgment; the runtime deliberately refuses to install without that explicit act, so no autonomous base `A` or `C` ownership mode is claimed.
- Evidence: [`src/swe_mux/update_check.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/update_check.py); [`src/swe_mux/update_install.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/update_install.py); [`src/swe_mux/server.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/server.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is a narrow software-capability adaptation loop, not evidence that swe-mux autonomously researches or redesigns itself. Repository-development roadmap/CI/release production is excluded; only the installed runtime's shipped update sense/plan/decision/return path is credited.
- External distinction: the externally published release contract indicates whether a newer swe-mux version and platform artifact exist.
- Future / prospective distinction: before replacement, the updater resolves the candidate version, platform bundle and whether the future runtime can use swap mode or requires supervisor replacement with session loss.
- Adaptation option generated: install the specifically identified newer verified release in the applicable mode, or retain current capability by declining/refusing the option.
- Path back into current capability / S3: operator decision reaches `UpdateInstaller`, verified/staged bytes enter the existing redeploy/swap machinery, health checking accepts or rolls back the replacement, and the resulting installed daemon/supervisor becomes the current operating capability.
- Parent ownership of the decisive adaptation judgment/feedback right: operator explicit gesture names the release to install; protocol-changing replacement additionally requires explicit `accept_supervisor_update` consent.
- Return of that parent decision into present capability: accepted decision invokes the staged swap/replace path; refusal leaves the current runtime unchanged.
- Subsequent operational/capability change under that returned decision: successful health-checked replacement serves subsequent sessions/control operations from the newly installed release; failed health causes rollback rather than silently adopting the candidate.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established at the reviewed installation recursion.
- Disturbance / variety regulated: swe-mux exposes many important constraints — Project permissions, assistant trust modes, automation grants, action approvals, emergency stops, access/network boundaries and update consent — but these regulate operational authority or adaptation rather than closing an identity/ultimate-policy dispute for the organization.
- Decisive decision or feedback right: no first-party path is shown for recognizing an identity/ultimate-policy matter, escalating it to legitimate ultimate authority and returning an authoritative policy/identity decision into subsequent operation as S5.
- Decision owner: not established for S5 within the product-runtime boundary.
- Supporting / enforcement mechanisms: `config.toml`, Project authority settings, assistant trust classes, action approval state, automation global allow, land/session-control grants, update consent, operator controls and static assistant instructions.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: these surfaces constrain lower-level decisions but do not themselves identify or resolve ultimate organizational identity/policy. Repository maintainer/release governance is an adjacent development organization and is excluded from product-runtime ownership.
- Evidence: [`src/swe_mux/config.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/config.py); [`src/swe_mux/assistant.py`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/src/swe_mux/assistant.py); [`README.md`](https://github.com/jatoran/swe-mux/blob/c14351b48a5424d2941b8a2e0e63b56f7033d2a0/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: parent ownership of S3 and S4 in supported modes does not imply parent-owned S5; the functions are classified independently.

### Absence scope

- Surfaces inspected: assistant system/trust contract, installation/project configuration, Project automation/control grants, action approvals, land/session-control authority, update decision path, README operating/access boundary and repository contribution/release governance as an adjacent surface.
- Plausible first-party paths checked: assistant system primer as constitution; Project permissions as policy; operator confirmation as ultimate authority; global automation/kill switches as S5; update consent as identity governance; maintainer/release workflow as product-runtime S5.
- Why no material first-party path remains: each runtime path is an operational/current-control or adaptation constraint/decision, while maintainer governance belongs to the adjacent repository-development organization. No shipped product path reconstructs identity/policy issue → legitimate ultimate authority → authoritative decision → return governing subsequent operation.

## Distributed OSS parent arrangement

Repository maintainers and contributors are not treated as the parent of the running swe-mux organization merely because they publish the software. The positive parent modes in this assessment are local to one self-hosted installation: its operator is the legitimate parent for explicit current-control confirmation (`S3` parent mode) and install-capability adaptation (`S4=P`). Public contribution/release governance is adjacent and supplies no product-runtime S5 claim.

## Self-hosted and non-human modes

swe-mux intentionally exposes operator-governed modes alongside autonomous assistant behavior. The S3 composite records two real first-party trust configurations rather than simultaneous dual ownership: `auto` closes a reversible current-control decision with the assistant, while `confirm` closes that same class of decision with the operator. The updater is intentionally parent-governed only; deterministic update machinery is not reclassified as autonomous S4.

## Recursion

A launched provider session may contain a viable agent organization of its own, but that recursion belongs to Claude Code, Codex or another provider harness and is not inherited here. At the assessed swe-mux recursion, those sessions contribute bounded operational outcomes and first-party swe-mux can regulate their cross-session/worktree relations without claiming ownership of their internal metasystems. Spawning a new session is therefore current resource allocation, not proof of a new VSM recursion.

## Variety and escalation

swe-mux attenuates operational variety through named project/session identity, bounded fleet snapshots, permission/trust classes, queueing, serialized landing, fixed Git mutation vocabulary, evidence normalization and attention budgets. It amplifies regulatory capacity through the Mux assistant's live-state model/tool loop, durable evidence consumers, remote operator surfaces and recovery.

Escalation is function-specific. Land conflicts and failed checks return to the branch-owning worker rather than being guessed by the deterministic queue. Audit/attention findings surface to the operator when routine reporting is not enough. Reversible assistant actions can remain autonomous or move to explicit parent confirmation by configured mode; consequential actions always require confirmation. A supervisor-incompatible update explicitly escalates its session-loss consequence to the operator before adaptation can proceed. None of these lower-level escalations is treated as S5 by default.

## Evidence gaps

- The S3* path is structurally strong but intentionally conservative: the frozen distribution routes complementary findings to a human rather than establishing an autonomous independent audit owner, so `C` is used instead of `A`.
- The S4 mapping is narrow and specific to installed software-capability adaptation. It should be reassessed if the in-app updater is removed, made autonomous, or reduced to notification without an operational return path.
- External provider sessions may evolve independently; any claim about their internal coordination, management, audit, adaptation or policy requires a separate assessment of that provider harness at its own pinned revision.
