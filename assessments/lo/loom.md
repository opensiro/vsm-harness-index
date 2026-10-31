---
harness_id: loom
project_name: Loom
repository: https://github.com/nickthelegend/loom
review_ref: 01682c8736a130f52e600ef8d351da46a66175a5
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Loom

## Review boundary

- System in focus: first-party MIT Loom daemon/CLI, its Orchestra and Teams modes for coordinating supported external coding agent adapters on a Git repository, plus optional team landing/review; not the autonomous internals of Codex/Claude/OpenCode/Antigravity or GitHub's governance.
- Purpose and identity: keep a shared memory/context thread across coding agents, break an operator goal into integrated worker tasks, manage concurrent work and deliver reviewable source changes under operator/team permission controls.
- Relevant environment: heterogeneous model/tool capabilities, task dependencies, concurrent edits in one repo, cross-teammate file conflicts, spend/parallel limits, regressions, failing CI, PR review findings and user decisions.
- Standard-distribution boundary: `src/core/orchestra.ts`, baton/route/worktree/brain/team policy modules, daemon `team-coordinator.ts`, `landing.ts` and runtime model dispatch, with documented `loom orchestrate` and Teams PR workflow.
- Credited operating / distribution surfaces: model-backed Orchestra plan/review/follow-up, mixed-agent worker adapters, scope leases/holds and orchestrator conflict decisions, independent cross-vendor read-only PR review with corrective status/fix return.
- Adjacent first-party surfaces excluded from ownership: Observatory traces/logs/digests, UI indicators, deterministic memory collection and learned project facts, generated videos, future proposals and ordinary test commands do not themselves establish S4/S5 or transfer external provider rights.
- First-party operating / deployment modes considered: local solo Orchestra, route and baton mode; optional Loom Teams linked to hosted team hub with file leases, origin-reviewed policy and automatic landing/review. S2 and S3* are credited only in their supported team modes, not presumed for every offline install.
- Recursion level: one Loom-governed coding-goal/fleet layer; its worker instances and teammate goals are operational units, while external repository owner/CODEOWNERS remain higher authority.
- Reviewed revision: `01682c8736a130f52e600ef8d351da46a66175a5`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Loom connects different coding agent adapters through a daemon and shared brain. In Orchestra mode an operator chooses a goal and permitted workers. A model-backed orchestrator emits structured `spawn/send/cancel/ask/done` actions; Loom creates task worktrees, schedules dependency-ready workers, integrates completed changes and returns task outcomes/holds for further model decisions. In Teams mode a coordinator requires declared touched paths, checks teammate leases, applies protected hard zones and capacity policy, and returns holds that the orchestrator can resolve or await. Goal PR landing can run a separate different-vendor read-only review against a diff and plan, post findings as a GitHub review and `loom/review` status, and reopen the run for high-severity fixes. The originating user still controls final branch application and ultimate team policy.

Pinned primary evidence:

- [Supported agents, shared brain, Orchestra/Teams, routes and intended review flow](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/README.md)
- [Model action protocol, task/goal state and task scheduling, review/feedback](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/orchestra.ts)
- [Team admission: capacity, file overlap, hard zones, decided proceed/wait and hub leases](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/daemon/team-coordinator.ts)
- [Scope/lease overlap and path-zone primitives](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/team-leases.ts)
- [Baton holder ownership and handoff](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/baton.ts)
- [Cross-vendor reviewer execution, independent temporary directory, PR status and reopen-on-findings](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/daemon/landing.ts)
- [Reviewer selection, read-only diff/plan prompt, severity parsing and verdict](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/team-landing.ts)
- [Origin policy loading, local-only tightening, permissions, protected branches and budgets](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/team-policy.ts)
- [Durable-turn memory extraction guarded by verbatim evidence, not prospective strategy governance](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/core/brain-extract.ts)
- [Run-time memory extraction and retrieval into subsequent agent briefs](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/src/daemon/runtime.ts)
- [Teams design and opt-in distribution/authority boundaries](https://github.com/nickthelegend/loom/blob/01682c8736a130f52e600ef8d351da46a66175a5/docs/teams-architecture.md)

## Operational model

The caller supplies a coding goal, actor roster and limits. The orchestrator agent decomposes work, responds to task results/holds, revises assignments and decides when the goal is complete; child agents actually edit/test code in isolated worktrees. Loom enforces dependencies, scopes, budgets and integration gates. Team admission mediates concurrency with other owners' active goal leases, and reviewer mode samples the actual PR diff separately from producer reports. However durable memory extraction chiefly records current/recent project facts; policy and identity remain under external human/team PR authority.

## S1 — Operations

- State: A
- Function: perform substantive project coding tasks through mixed worker agents and follow-up corrective work.
- Disturbance / variety regulated: unknown implementation requirements, repository state, test errors, differing adapter capabilities and changing user feedback.
- Decisive decision or feedback right: workers choose actual code edits, tests and task-level repair actions within model-driven CLI sessions; coordinator may request another try.
- Decision owner: supported external model-backed coding workers *composed into Loom's explicit worktree/adapter operational path*; their general internals are not counted as Loom metasystem functions.
- Supporting / enforcement mechanisms: `OrchestraTask` worker prompts, adapters, separate task worktrees, run event capture, dependency completion and integration merge.
- Closure path: operator goal → model-authored task instruction → worker exploration/edit/test → task result/error/commit → orchestrator feedback and possible follow-up.
- Boundary reachability: `Orchestra.start` creates worker roster and integration worktree; `addTask` validates agent; `schedule` starts dependency-ready tasks via `runTask` and processes completion.
- Why this is / is not agent-owned: implementation steps are not pre-enumerated deterministic scripts; the first-party runner hosts their decisions and records outcomes.
- Evidence: pinned `orchestra.ts`, README and adapters.
- Basis: shipped model-agent execution path.
- Confidence: high for composition, not for solution quality.
- Caveats: external coding models were not executed during this static assessment.

## S2 — Coordination

- State: A
- Function: negotiate and regulate concurrent peer goal/work-unit interference, especially overlapping files and shared project zones in supported Teams mode.
- Disturbance / variety regulated: separate teammates or tasks editing the same path, hard-zone collisions, dependency races and bounded shared agent capacity.
- Decisive decision or feedback right: dynamically narrow task `touches`, wait on another goal, or justify `proceed:` on a soft overlap; hard zone still requires release, while shared lease and limits enforce the decision.
- Decision owner: model-backed orchestrator receiving `task_held`/status reports and emitting revised `spawn` actions; constructor-defined coordinator supplies collision facts and blocks hard conflicts, with a separate human stop-wait option.
- Supporting / enforcement mechanisms: path scope/overlap computation, hub-owned leases, `hardZones`, `TeamCoordinator.admit`, explicit `decide/wait/zone/capacity` holds, recheck/lease release, and baton single-writer handoff in local conversation mode.
- Closure path: rival lease/file path collision → held task with named holder/conflicting paths → orchestrator's new overlap/scope/dependency decision → hub re-admission or continuing wait → peer work resumes under enforced scope.
- Boundary reachability: the team-linked `OrchestraCoordinator` is asked before `runTask`; `admitAndRun` saves rejected holds, `maybeReview` returns `decide` holds to orchestrator, `addTask` revises pending task scope and overlap.
- Why this is / is not agent-owned: adaptive overlap response is a model decision, but the actual hub lease, hard-zone prohibition and capacity limit are constructed enforcement; routine worktree isolation alone is not the reason for S2.
- Distinct S1 units: independent teammate goals and concurrent task-level worker agents with their own source-editing scope and implementation feedback.
- Inter-S1 disturbance: two viable goals may claim overlapping repository paths or a protected hard zone, and one worker's changes can invalidate or block another's intended work.
- Attenuating coordination relation: the team hub records actual rival leases; model orchestrator can narrow declared paths, wait on another goal or explicitly justify a soft-overlap proceed, while hard zones and caps remain binding.
- Feedback into subsequent S1 behaviour: held workers do not start; revised work scopes are re-admitted, waiters rebase after another PR merges, and resumed task agents work under updated boundaries.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the reviewed path detects and regulates destructive inter-peer file interference across independent continuing teammate goals, with return to operational schedules, not merely passing work to another agent.
- Evidence: pinned `team-coordinator.ts`, `team-leases.ts`, `orchestra.ts`, `baton.ts`.
- Basis: first-party opt-in Teams conflict-decision return path.
- Confidence: medium-high.
- Caveats: solo/offline Orchestra has worktree isolation but no cross-teammate S2; on soft overlap an agent may choose `proceed` with a reason, not override protected hard zones.

## S3 — Inside-and-now control

- State: A
- Function: control the current goal's total task portfolio, shared cost/parallel constraints, dependencies, integration and release readiness.
- Disturbance / variety regulated: stalled or failed workers, changing dependency conditions, overspend, busy goals, rejected coordination requests and incomplete merge results.
- Decisive decision or feedback right: split/assign, reprioritize through dependencies, spawn/revise tasks, send follow-ups, cancel, ask the human and announce done based on whole-goal status.
- Decision owner: user-selected model-backed orchestrator of the goal; Loom constructor owns hard execution admission, budget and integration restrictions, including refusing `done` while tasks remain outstanding.
- Supporting / enforcement mechanisms: `OrchestraRun` all-task state, status report, budget counter, `maxParallel`, integration branch, dependency scheduler, reviewer/fix results and event log.
- Closure path: plan → parallel task results and holds → `statusReport` containing all work → model's next action set → new commitments or completed integrated goal; unsettled decisions can pause for owner reply.
- Boundary reachability: `orchestratorTurn` parses actions; `applyActions` changes run portfolio; `maybeReview` wakes orchestrator once tasks settle/need decision; `runTask`/merge update task outcomes.
- Why this is / is not agent-owned: the orchestrator sees and can alter total current work, not only choose the next local tool; creator-set caps condition execution but do not predetermine tactical choices.
- Whole-system current view: all tasks, assignment, dependencies, attempts, holds, costs, integration state and project goal within one Orchestra run.
- Current-control decision scope: one coding-goal fleet (and team admission), not global business constitutional policy.
- Evidence: pinned `orchestra.ts`, Teams coordinator and README.
- Basis: whole-run control with an actual model decision loop.
- Confidence: high for supported agent-backed mode.
- Caveats: local headless routing without Orchestra does not inherit this planning/control behavior.

## S3* — Complementary audit

- State: A
- Function: independently challenge the producer/orchestrator's claim that a delivered code change meets the goal and is safe enough to land.
- Disturbance / variety regulated: missed requirements, severe code regressions, deficient tests and producer self-report blind spots.
- Decisive decision or feedback right: an auditor from a different model vendor reads actual PR diff and plan in read-only context, issues severity-labelled findings, and returns a pass/fail status that can block landing and reopen corrective work.
- Decision owner: separate different-vendor reviewer agent selected from installed agent kinds; Loom parses/severity-gates findings, and the human owner may explicitly override with an auditable reason.
- Supporting / enforcement mechanisms: `pickReviewer` excludes author vendor, temp review directory, `reviewPrompt`, `parseReview`, GitHub comment review, `loom/review` status, `reviewFixPrompt` and bounded automatic fix attempts.
- Closure path: completed integrated PR/plan → independent raw diff inspection → high-severity findings and status → S3 owner/Orchestra reopening for fixes or human `needsHuman` → revised head re-reviewed; owner may override with public reason.
- Boundary reachability: `landing.review` calls `askAgent(reviewer,tmp,readOnlyPrompt)`, posts findings and commit status, and invokes `orchestra.reopen` on unoverridden high findings; Teams review is enabled by default in parsed team policy but opt-in via team-linked delivery.
- Why this is / is not agent-owned: reviewer has alternative primary evidence (diff and PLAN.md) relative to task reports, different-vendor execution and a returned corrective path; this exceeds a routine same-agent QA label or passive telemetry.
- Claim being audited: integrated producer code and orchestrator completion state are adequate to meet the declared goal without high-severity regressions.
- Ordinary reporting path: worker task status/merge results and Orchestra's aggregate completion report to the goal controller.
- Complementary access path: different-vendor reviewer receives actual GitHub PR diff plus plan in a separate read-only temporary workspace and generates severity-labelled findings.
- Independence boundary: the selected reviewer's vendor must differ from all author agent kinds; it cannot modify the producer's working tree and posts its own PR comment/status; absent eligible vendor is explicitly reported as skipped.
- Who acts on findings: the landing controller blocks with `loom/review` failure and reopens Orchestra's owner goal for fixes; if the budget is exhausted it asks a human, who alone can log an override reason.
- Ordinary report vs audit view: producer reports task completion and integrated branch; auditor reads the actual PR patch and goal plan independently, not only the producer summary.
- Independence / access: different installed vendor, isolated temporary work directory and read-only instruction; GitHub status and human override preserve separation from normal producer authority.
- Findings / return: severity-labelled PR comment and `loom/review` check signal trigger fix/reopen or explicit owner override before landing.
- Evidence: pinned `landing.ts`, `team-landing.ts`, Teams design and policy.
- Basis: optional but first-party implemented complementary PR-inspection loop.
- Confidence: high for reachable team reviewer mode.
- Caveats: if no different-vendor reviewer is installed, `review` explicitly skips and reports success; a human can override a failure; no blanket guarantee that every install or PR receives an independent audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no clearly owned two-way external/future adaptation program converting environmental changes into prospectively tested new operational capabilities is shipped.
- Disturbance / variety regulated: developer tool evolution, future workload mix and team strategy may change, but Loom principally records current turns and shares engineering context rather than constructing future alternatives.
- Decisive decision or feedback right: an optional extractor selects durable `ADD/UPDATE/FORGET` memory records from a turn; that right changes knowledge retrieval, not a prospective adaptation portfolio or redesigned capability selected against future scenarios.
- Decision owner: model extractor for memory content; current operator for agent roster/configuration and future integration decisions.
- Supporting / enforcement mechanisms: event-log memory, turn evidence quotes, confidence/untrusted guards, lexical/dense retrieval and downstream agent brief injection.
- Closure path: past turn → extracted facts/constraints/failures → persistent brief on later task; no external/future distinction → adaptation hypothesis/options → comparison with current capacity/S3 → selected changed operational capability loop is shown.
- Why this is / is not agent-owned: durable memory improves continuity and can influence future local task decisions, but the Profile explicitly distinguishes memory consolidation from S4 prospective environmental intelligence.
- Evidence: pinned `brain-extract.ts`, `brain.ts`, `runtime.ts`, `README.md`.
- Basis: scoped negative after examining plausible learning path.
- Confidence: medium-high.
- Caveats: team/project owners can update policies/tools or agents externally; that manual capability change is not inherited as Loom's autonomous S4.

### Absence scope

- Surfaces inspected: model memory extraction/recall, shared brain projection, team canon updates, telemetry/triage, route templates and user-configurable worker adapters.
- Plausible first-party paths checked: future-use memories as S4, observability as environmental scanning, model route changes as long-horizon adaptation, skill import/author scaffolding as new strategic capability.
- Why no material first-party path remains: these preserve/currently route context or expose tools under owner control, without a demonstrated external-prospective option-construction-and-return cycle beyond the current project task.

## S5 — Policy and identity

- State: —
- Function: final mission legitimacy, team identity and ultimate risk policy are not adjudicated by the Loom daemon or its orchestrator.
- Disturbance / variety regulated: authorized permissions, team policy, protected repository branches, reviewer/CODEOWNER requirements and spending ceilings.
- Decisive decision or feedback right: repository owners and reviewers change `loom.team.json` on the reviewed default branch and ultimately approve protected changes; ordinary Loom tasks are constrained by that externally settled policy.
- Decision owner: external team governance/humans and GitHub repo rules; `loadPolicy` and `stricter` are first-party policy transport/enforcement, not ultimate identity adjudication.
- Supporting / enforcement mechanisms: origin policy read, local-only tightening, agent permission caps, hard zones, protected branches, signed/posted statuses and owner review/override reason.
- Closure path: externally accepted policy file → daemon reads and enforces on subsequent team tasks; no first-party identity-level dilemma → legitimate parent decision solicitation → reviewed mission-policy resolution → return to operation as an explicit internal S5 channel is established.
- Why this is / is not agent-owned: reviewed policy files, user approval and a different-vendor code reviewer are meaningful guardrails but not themselves evidence of a Loom-owned ultimate-purpose decision right.
- Evidence: pinned `team-policy.ts`, `landing.ts`, Teams design/README.
- Basis: function-specific negative for identity authority despite strong governance constraints.
- Confidence: medium-high.
- Caveats: parent institution may supply an S5 function for its project; this assessment does not transfer its authority to Loom.

### Absence scope

- Surfaces inspected: origin-reviewed team policy loader, permission ceilings, protected landing, CODEOWNER/human approvals, user prompts and orchestrator done/ask transitions.
- Plausible first-party paths checked: policy file as S5, PR approval as S5 parent-return, operator override as identity review and orchestrator goal changes as final mission policy.
- Why no material first-party path remains: the actual disputes resolved here are operational permissions and PR quality; a general identity-level issue path with competent ultimate-policy judgment and return is not shown.

## Recursion

Loom worker agents perform distinct viable coding tasks with their own local environment and feedback. The model-backed Orchestra/Teams layer provides bounded S2 and S3 for this fleet. A team-owned GitHub repository and CODEOWNERS may supply additional higher-recursion governance but are not part of Loom's internal independent S5.

## Variety and escalation

Task decomposition and heterogeneous adapters absorb development variety; isolated branches, dependency checks, leases and cost ceilings attenuate interference. Team overlap holds or unavailable permissions return to the orchestrator for possible scope adjustment or to the owner for explicit decision. Severe cross-vendor review findings are exceptional corrective signals reaching the goal controller; absent reviewers are reported as skipped, not silently assumed.

## Evidence gaps

- Source and documented supported modes reviewed at the frozen SHA, without running a real external provider, team hub, worker, PR review or CI on an application goal.
- S2 depends on team-linked hub/leases and model response to `decide` holds; S3* depends on an installed distinct vendor and enabled team review. These conditional boundaries are part of the grade, not claims that every offline instance provides them.
- The durable brain extractor produces future-use memory, but this assessment does not infer strategic S4 merely from memory/telemetry; identity authority stays external to the daemon.

## Assessment summary

Proposed `included`: model-backed coding operations and peer-conflict negotiation (S1=A, S2=A), a model controller of the whole current task portfolio (S3=A), and an optional separate raw-diff cross-vendor corrective audit (S3*=A). Durable context and reviewed settings do not independently establish S4 or S5. Vector **A · A · A · A · — · —**.
