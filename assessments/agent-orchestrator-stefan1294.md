---
harness_id: agent-orchestrator-stefan1294
project_name: Agent Orchestrator (tracks)
repository: https://github.com/stefan1294/agent-orchestrator
review_ref: f78e1b06d80ed43803029a14f14df69908782fee
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent Orchestrator (tracks)

## Review boundary

- System in focus: one self-hosted Agent Orchestrator project factory at multi-track recursion, including first-party feature/category routing, per-track queues and worktrees, Agent Executor adapters, orchestration/failure/retry/fallback logic, SQLite session history, implementation→verification→fix lifecycle, optional browser verification, merge/verification serialization, and dashboard/operator controls.
- Purpose and identity: parallelize bounded software features across isolated coding-agent tracks, keep current fleet execution/recovery coherent, independently verify merged behavior, and feed verification failures back into corrective implementation before final feature disposition.
- Relevant environment: target Git repository and base branch, feature specification file, local worktrees, Claude/Codex/Gemini CLIs, dev server/application, Chrome DevTools MCP when enabled, user/operator, provider capacity/rate limits, Git remote, filesystem and shell.
- Standard-distribution boundary: first-party server/client, Orchestrator, QueueManager, AgentExecutor, GitManager, feature/session stores, API/dashboard controls, prompts and MCP setup are inside. Claude/Codex/Gemini internal reasoning/tool loops and browser/MCP service internals remain external capabilities. A model-backed implementation/verifier/fix session is credited only where the first-party runtime directly constructs and invokes that actor; no other functions are inherited from the external agent.
- Credited operating / distribution surfaces: `README.md`; `src/server/services/orchestrator.ts`; `agent-executor.ts`; `queue-manager.ts`; `git-manager.ts`; `feature-store.ts`; `session-db.ts`; `project-config.ts`; `src/server/api/control.ts`; `retry.ts`; `resume.ts`; and dashboard/track/feature UI surfaces.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI, screenshots/documentation as evidence rather than runtime actors, contributor/release governance, and external model/browser/MCP internals.
- First-party operating / deployment modes considered: normal multi-track autonomous run; preferred/fallback model-agent modes; implementation, verification and fix sessions; CLI-only verification and optional browser verification; dashboard-configured tracks; operator start/stop/retry/resume; rate-limit and critical-failure recovery; verification-disabled mode as a supported weaker path but not the evidence basis for S3*.
- Recursion level: one project-wide feature factory containing multiple implementation S1 cells grouped into tracks. The deterministic Orchestrator and optional local human operator regulate the current fleet above them. Verification is assessed as a complementary observation path over each feature's implementation claim, not as another recursively viable organization.
- Reviewed revision: `f78e1b06d80ed43803029a14f14df69908782fee`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agent Orchestrator is a Node/TypeScript server plus React dashboard. It loads a feature list, lets a user configure up to five category-based tracks, creates one Git worktree per active track, and runs track loops concurrently. Queue priority is explicit: resume work first, then retry work, then ordinary main-queue features. Each implementation session is persisted in SQLite and executed through AgentExecutor using a configured Claude/Codex/Gemini CLI.

The controller owns more than generic task sequencing. It classifies execution failures, detects rate-limit conditions and requeues work with a bounded wait, tracks consecutive configured critical failures and pauses a track after repeated infrastructure failure, prioritizes an explicitly resumed feature while pausing other tracks, and serializes merge+verification across tracks. GitManager owns branch/worktree setup, merge/push and shared Git-operation mutexes.

A successful implementation with commits enters a distinct verification path. The feature branch is merged into the base branch, the runtime waits for the live application to reload, then creates a separate verification session in the main project root. Its prompt is verification-only and requires structured PASS/FAIL findings; in the Claude mode the command uses restricted verification tools without `Edit`. Browser mode supplies a different observation surface through Chrome DevTools MCP. A failed verification is not merely logged: the exact verification output is passed to a separate fix session in the feature worktree; resulting fixes are committed, merged/pushed and independently verified again until pass or bounded exhaustion. This supplies a material complementary audit-and-correction loop.

The dashboard exposes all tracks/features/current sessions and failure state. Operators can start/stop the factory, configure track/category allocation, retry failed work with added context, or resume a selected feature; resume obtains highest queue priority and pauses other tracks before their next feature. That is a distinct parent current-control mode over the same first-party state.

## Operational model

Implementation sessions are S1 work cells: each model-backed actor receives a bounded feature contract in a dedicated worktree and makes open-ended coding decisions. First-party tracks/worktrees/category routing and serialized verification/merge attenuate cross-cell interference, supplying constructor S2.

At current-control recursion, the deterministic Orchestrator maintains fleet state across tracks and changes present commitments in response to failures, rate limits, resume priority and merge/verification ownership. That is an S3 constructor rather than a semantic autonomous manager. The dashboard/operator path independently closes parent S3 by viewing whole-fleet state and returning track/retry/resume/start/stop decisions that change subsequent scheduling.

The verification session supplies S3*. It is separated from the implementation session, operates from the merged main-project/live-app environment, has a verification-only mandate and, in a supported Claude mode, restricted non-editing tools. It challenges acceptance-step claims and returns a concrete failure report into the fix/re-merge/reverify loop. The audit judgment is produced by a model-backed verifier actor, so the positive ownership mode is `A`.

## S1 — Operations

- State: A
- Function: implement one bounded software feature through open-ended model-driven code/tool choices in its assigned worktree.
- Disturbance / variety regulated: feature-specific repository structure, implementation choices, compiler/test feedback, debugging and local code interactions that deterministic orchestration rules cannot preselect.
- Decisive decision or feedback right: choose and revise semantic implementation actions in response to repository/tool feedback.
- Decision owner: the model-backed Claude/Codex/Gemini implementation session launched by AgentExecutor.
- Supporting / enforcement mechanisms: feature prompt/acceptance steps, per-track worktree/branch, session persistence, max-turn/tool configuration, stop callback, Git status/commit checks, result capture.
- Closure path: track dequeues feature → worktree/branch prepared → AgentExecutor launches model-backed implementation session → actor changes/tests code → session result and Git branch state return → orchestrator advances to verify, retry/failure or stop.
- Boundary reachability: the built-in AgentExecutor constructs and launches supported coding-agent CLIs in the standard runtime; no application-level adapter implementation is required.
- Why this is / is not agent-owned: removing the model-backed actor leaves queue/Git/session enforcement but no component that can choose the feature's open-ended implementation.
- Evidence: [`README.md`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/README.md); [`src/server/services/orchestrator.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/orchestrator.ts); [`src/server/services/agent-executor.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/agent-executor.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external agent internals remain outside the assessment boundary; only the first-party-reachable operational cell is credited.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference among parallel implementation S1 cells over repository/worktree, category/track capacity, shared Git integration and verification.
- Disturbance / variety regulated: simultaneous workers can collide in one checkout/base branch, multiple categories compete for track capacity, a merge can invalidate another track's branch, and simultaneous merge/verification operations can corrupt a shared live validation state.
- Distinct S1 units: implementation sessions running on separate configured tracks/features.
- Inter-S1 disturbance: shared repository/Git metadata and base-branch mutation, cross-track merge ordering, category-to-track contention and concurrent live verification can make otherwise valid worker actions interfere.
- Attenuating coordination relation: one worktree per track, category routing, one active feature per track loop, Git mutex, verification mutex, feature-branch update before merge, serialized merge+verification, priority queues and deterministic track allocation.
- Feedback into subsequent S1 behaviour: routing determines which track executes a feature; retry/resume priority changes later dequeue order; a merge/update conflict or verification lock delays/stops later work; new base-branch state is merged into feature branches before their integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanisms explicitly suppress evidenced cross-cell collisions in shared Git/base/live-verification resources, not merely move messages or enumerate tasks.
- Decisive decision or feedback right: enforce track/worktree allocation and serialization relations that decide when and where an S1 may safely execute or enter shared integration/verification.
- Decision owner: deterministic first-party queue/Git/orchestration machinery.
- Supporting / enforcement mechanisms: QueueManager, GitManager worktrees/mutex, verification mutex, track definitions, branch-update/merge paths, session state.
- Closure path: feature population is routed to tracks → isolated S1s execute → shared integration/verification is serialized and updated against latest base → resulting task/base state governs subsequent track execution.
- Boundary reachability: all credited controls are integrated into normal `start`/track/merge/verify runtime paths.
- Why this is / is not agent-owned: removal of all model actors leaves materially the same allocation/isolation/serialization rules; the function is constructor-owned.
- Evidence: [`src/server/services/queue-manager.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/queue-manager.ts); [`src/server/services/git-manager.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/git-manager.ts); [`src/server/services/orchestrator.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/orchestrator.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: plurality/tracks alone are not the evidence; the state is grounded in concrete cross-cell Git/integration/verification attenuation.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current fleet commitments/resources across tracks in response to active work, resume/retry priority, provider/rate-limit state, critical failures and shared merge/verification availability.
- Disturbance / variety regulated: which current features/tracks should consume execution next, rate-limit/provider unavailability, repeated environment failures, a user-requested priority resume, merge/verification ownership and whether the factory should admit more work.
- Whole-system current view: Orchestrator tracks global state, all configured track statuses/current sessions/queued counts, feature/session outcomes, a global resume request, critical-failure counters and serialized merge/verification ownership; dashboard combines full features, status and track definitions.
- Current-control decision scope: base constructor routes/dequeues by track, prioritizes resume/retry, requeues rate-limited work, pauses other tracks for a resume request, auto-pauses a repeatedly failing track, serializes merge/verify and can stop the factory on unsafe Git/commit/merge failure. Parent mode can configure track allocation, start/stop, retry a feature with context, or prioritize/resume one feature over other tracks.
- Decisive decision or feedback right: base mode — deterministic Orchestrator changes current allocation/admission/recovery under current fleet state; parent mode — local operator chooses current track/work priority and continuation interventions.
- Decision owner: base `C` — deterministic Orchestrator/QueueManager state machine; parent `P` — legitimate local self-hosted human operator through dashboard/API.
- Supporting / enforcement mechanisms: status projection, track/feature/session state, queue priorities, resume request, failure classification, critical counters, rate-limit delay, stop state, dashboard/API controls.
- Closure path: current fleet state/exception is observed → deterministic rule or operator intervention selects an allowed current-control transition → queues/track/global state are mutated → later dequeue/execution follows the returned state.
- Boundary reachability: both base runtime control and dashboard/API parent controls are shipped first-party surfaces over the same live Orchestrator state.
- Why this is / is not agent-owned: current-control choices in the base mode are rule-based; no model actor owns the whole-fleet managerial judgment. Parent mode is explicitly human-controlled. Model workers remain S1/S3* actors rather than S3 owners.
- Evidence: [`src/server/services/orchestrator.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/orchestrator.ts); [`src/server/services/queue-manager.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/queue-manager.ts); [`src/client/pages/Dashboard.tsx`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/client/pages/Dashboard.tsx); [`src/server/api/control.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/api/control.ts); [`src/server/api/retry.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/api/retry.ts); [`src/server/api/resume.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/api/resume.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic scheduling is not enough; the positive constructor state is grounded in whole-fleet priority, recovery, pause/stop and shared merge/verification transitions that alter present commitments.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | deterministic Orchestrator/QueueManager | current queue/track/resume/rate-limit/critical-failure/merge-verification state | route, priority, requeue, pause/stop or serialized-control transition mutates live state and governs later execution | `orchestrator.ts`, `queue-manager.ts` |
| Parent (`P`) | local self-hosted operator | dashboard whole-fleet state or a failed/paused feature needing intervention | start/stop, track configuration, retry or priority resume mutates first-party state/queues; later track loops obey it | dashboard + control/retry/resume APIs |

## S3* — Complementary audit

- State: A
- Function: independently challenge the claim that an implemented/merged feature satisfies its acceptance steps using a separate verification session and observation-only role, then return failures into corrective execution.
- Disturbance / variety regulated: an implementation agent can exit successfully or commit code that is behaviorally wrong, incomplete, or fails acceptance criteria after integration into the live base branch.
- Claim being audited: the implemented feature works against the declared acceptance steps after its code is merged into the current base/live application.
- Ordinary reporting path: implementation session exit/result, branch commits and agent output returned from the feature worktree.
- Complementary access path: a newly created verification session runs from the main project root after merge/push and hot-reload; it receives a verification-only prompt, observes CLI/live-app behavior (and optionally browser behavior), and emits structured per-step PASS/FAIL findings. Supported Claude verification removes `Edit` from allowed tools.
- Independence boundary: verification uses a separate session/context, different role/prompt, different working boundary (merged main project/live app rather than feature worktree), and supported read-only/restricted tools. It does not rely solely on the implementation session's self-report, even when the same configured model/agent family is reused.
- Who acts on findings: first-party Orchestrator consumes the verdict; failure output is passed to a separate fix session, fix changes are committed and remerged, and a fresh verifier session challenges the result again until pass or bounded exhaustion.
- Disturbance / variety regulated: false-positive implementation completion and regressions visible only after integration/live observation.
- Decisive decision or feedback right: judge acceptance-step PASS/FAIL from complementary runtime evidence; that judgment determines whether the feature is accepted or returned into the fix loop.
- Decision owner: the model-backed verification actor in the first-party verification session.
- Supporting / enforcement mechanisms: verification-only prompt, separate session record, main-root/live observation, restricted Claude tools, optional browser MCP, regex safeguard for explicit FAIL verdicts, bounded verify/fix attempts, verification mutex.
- Closure path: implementation/merge produces ordinary success claim → separate verifier probes declared acceptance steps through complementary live/main-root access → PASS accepts feature; FAIL output is fed to fix agent → changes are remerged → new verification session retests → terminal pass/fail updates feature state.
- Boundary reachability: the verification/fix loop is directly integrated into normal `verifyAndMerge`; no application-provided verifier implementation is required. Browser access is optional; CLI verification alone supplies the positive path.
- Why this is / is not agent-owned: deterministic code controls session creation and consumes verdicts, but it cannot semantically test arbitrary acceptance steps itself. Removing the verification model actor eliminates the complementary behavioral judgment.
- Evidence: [`README.md`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/README.md); [`src/server/services/orchestrator.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/orchestrator.ts); [`src/server/services/agent-executor.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/agent-executor.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the verifier can reuse the same underlying agent family as implementation, so independence is role/session/access-path rather than provider diversity. The positive finding relies on that structural separation plus live/main-root observation and corrective return; verification-disabled mode does not carry S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then intelligence loop is established that senses external/prospective change, generates adaptation options and returns them into current organizational capability.
- Disturbance / variety regulated: current framework detection, current provider/rate-limit failures, feature definitions and session history are observed, but these are operational/current-task distinctions.
- Decisive decision or feedback right: none established for prospective adaptation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: framework detection, settings, session history, failure classification, fallback agents, browser capability and persistent progress.
- Closure path: no external/future model → adaptation option → current-capability return loop found.
- Why this is / is not agent-owned: fallback/retry reacts to present execution failures and framework detection configures current operation. Persistence/history does not itself synthesize strategic adaptation.
- Evidence: [`README.md`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/README.md); [`src/server/services/orchestrator.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/services/orchestrator.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a future learning/planning capability could change this result; current automation is reactive.

### Absence scope

- Surfaces inspected: framework detection, feature/progress/session persistence, settings, agent fallback/rate-limit handling, browser verification, retry/resume and dashboard history.
- Plausible first-party paths checked: framework auto-detection as environmental sensing; fallback agents; session-history learning; progress file; browser verification; operator settings.
- Why no material first-party path remains: each candidate concerns current compatibility, execution recovery, evidence or memory; none constructs prospective adaptation options from an external/future distinction and returns them into capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party organizational identity/ultimate-policy decision loop is established.
- Disturbance / variety regulated: project configuration, track/category allocation, base branch, prompts, agent/model selection, browser/tool settings and operator start/stop authority constrain operation.
- Decisive decision or feedback right: no identity/ultimate-policy issue is adjudicated and returned as governing organizational policy.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: config/settings, ORCHESTRATOR instructions, dashboard controls, agent allowlists/tools, branch/verification policy.
- Closure path: no identity/ultimate-policy issue → ultimate authority → authoritative decision → return-to-operation loop.
- Why this is / is not agent-owned: operator configuration and S3 current-control intervention are bounded operational authority, not constitutional identity closure; prompts/instruction files are supplied rules, not S5 decisions.
- Evidence: [`README.md`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/README.md); [`src/client/pages/Tracks.tsx`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/client/pages/Tracks.tsx); [`src/server/api/control.ts`](https://github.com/stefan1294/agent-orchestrator/blob/f78e1b06d80ed43803029a14f14df69908782fee/src/server/api/control.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a self-hosted user may externally define project policy, but the frozen product does not operationalize that broader authority as an S5 loop.

### Absence scope

- Surfaces inspected: settings/config, track allocation, prompts/instruction files, start/stop/retry/resume, agent/tool policy, branch/verification settings and repository governance as adjacent surface.
- Plausible first-party paths checked: operator as S5 parent; track/category configuration; verification policy; instructions file; model/provider selection; dashboard settings.
- Why no material first-party path remains: all inspected decisions govern bounded execution/current control. None presents and closes an identity or ultimate-policy issue at the project-factory recursion.

## Distributed OSS parent arrangement

The parent S3 mode is local to one self-hosted factory and its operator. Multiple OSS contributors or independent deployments do not establish a shared organization-level parent. Repository maintainers remain outside the live runtime boundary.

## Self-hosted and non-human modes

Default multi-track operation closes S1/S2/S3/S3* without requiring continuous operator decisions; the base S3 is deterministic rather than autonomous. The dashboard adds a separate parent S3 mode for local human intervention. Verification is autonomous only when enabled, as it is in the normal documented configuration; explicit verification-disabled mode is a weaker supported mode and does not erase the positive supported S3* mode.

## Recursion

At the selected recursion the project factory is the system in focus and implementation sessions are S1 cells grouped by tracks. The Orchestrator supplies deterministic coordination/current control over their shared resources. Verification is a complementary audit path that deliberately observes the merged/live consequence of an S1's contribution from a different session/working boundary. External model-agent and MCP internals remain separate systems.

## Variety and escalation

Implementation variety stays with S1 agents. Cross-track Git/base/live-verification interference is attenuated by S2 worktrees and mutexes. Current operational variety is compressed into track/queue/session/failure state for S3: resume work preempts ordinary work, rate limits requeue, repeated critical environment failures pause a track, and unsafe merge/commit failures can stop further admission. Semantic acceptance uncertainty escalates through S3*: failed verifier evidence is sent to a fix agent and then independently retested. Operator retry/resume supplies an additional current-control escalation path.

## Evidence gaps

S3* independence is structural rather than organizationally separate provider identity: the verifier is a fresh session and can use the same agent family that implemented the feature. The first-party system strengthens independence through a different role, merged/live observation surface and, for Claude, restricted verification tools. If future methodology requires distinct provider/actor identity rather than distinct access/context, this state should be revisited. No evidence supports S4 or S5 at the frozen revision.
