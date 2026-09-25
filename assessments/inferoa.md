---
harness_id: inferoa
project_name: Inferoa
repository: https://github.com/agentic-in/inferoa
review_ref: 1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Inferoa

## Review boundary

- System in focus: one first-party Inferoa Loop organization at pinned revision `1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd`, including the standard model/tool runtime, persistent Goal/Loop state, foreground and daemon supervision, internal reflection decision turns, completion verification, verifier suites, subagent/worktree helpers, discovery/inbox surfaces, and self-improve/skill proposal machinery where reachable from the shipped product.
- Purpose and identity: close a user-defined long-horizon coding or research objective through repeated execution, evidence capture, verification and explicit loop decisions that continue until the objective is proven complete, blocked, paused or dropped.
- Relevant environment: the user/operator, the working repository and filesystem, model/provider endpoints, tool outputs, commands/tests, GitHub state, HTTP services, npm package state and other external resources explicitly sensed by the shipped runtime.
- Standard-distribution boundary: first-party Inferoa runtime/TUI/CLI, Goal/Loop state machine, daemon supervisor, tool registry, verifier machinery, managed worktrees, subagent tool, loop discovery/inbox, automation and self-improve/skill surfaces at the pinned revision. External model providers, GitHub/npm/HTTP services and downstream user-authored skills remain environment/dependencies.
- Credited operating / distribution surfaces: `/loop` Deliver/Discover/Replay modes; normal execution turns; internal `reflection` decision turns; persistent coverage/frontier/evidence/residual-risk state; daemon goal supervision; completion verifier; multi-role verification suites; standard subagent tool; managed worktrees; loop inbox/discovery; explicit self-improve proposal/replay/adopt surfaces.
- Adjacent first-party surfaces excluded from ownership: repository development CI/evals for Inferoa itself; roadmap/design documents when not wired into current product behavior; benchmark figures and acceptance fixtures used only to validate Inferoa development; generic configuration and provider-selection surfaces unless they close a VSM function at the assessed recursion.
- First-party operating / deployment modes considered: foreground Loop mode in the TUI; daemon-supervised Loop mode; Deliver, Discover and Replay preferences; automatic completion verification in daemon goal supervision; manually invoked and background verifier suites; session- and worktree-isolated verifier/subagent execution; scheduled discovery and inbox promotion; explicit self-improve proposal/replay/adopt.
- Recursion level: the assessed organization is one Loop objective/session. The durable goal-directed Loop is the primary S1 operational unit at this recursion. Bounded subagents/verifier children are credited only for the specific function they actually close; spawning a child is not treated as proof of an additional viable recursion or of S2 by itself.
- Reviewed revision: `1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Inferoa exposes a persistent model/tool runtime with a distinct long-horizon Loop control plane. A Loop stores the original objective, preference, runtime policy, current horizon plan, attempts, verification records, coverage surfaces, frontier candidates, evidence, residual risk and latest reflection decision. Normal execution turns are told to make structural progress on the active objective and persist evidence/state rather than merely narrate completion.

When the current horizon is exhausted, the Goal supervisor launches a separate internal `reflection` model turn. That turn is explicitly asked to step back from the current plan, reconstruct the top-level decomposition and independently choose exactly one of `expand`, `done` or `blocked`. Deterministic supervisor code then applies structural/candidate/runtime/verifier completion gates and either opens another horizon, pauses, invokes verification or completes the Loop. The reflection actor therefore owns the discretionary current-control judgment while runtime gates enforce invariant constraints around that judgment.

Completion verification is a separate checker path. Verification runs have a dedicated request class and a checker prompt that says "checker, not maker", requires direct inspection of current loop state, files/diffs/commands/resources/tests, and forbids implementation or plan mutation. Inferoa also supports multi-role verification suites (`completion`, `implementation`, `tests`, `security`, `docs`, `research`), including separate child sessions and optional isolated worktrees. In daemon goal mode, completion verification is automatically invoked when policy requires it and a valid checker/command/human pass is required before completion can close.

Inferoa additionally ships bounded subagents, managed worktrees, scheduled discovery for GitHub/HTTP/npm/local-git signals, inbox promotion, Discover-mode research and self-improve skill proposals. These are not promoted to S2 or S4 merely from their names. The reviewed evidence does not establish a distinct inter-S1 coordination loop at the declared recursion, and the discovery/self-improve surfaces do not by themselves close an external-and-prospective organizational adaptation loop into present capability.

Primary evidence:

- [`website/docs/workflows/loop-mode.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/loop-mode.md) — first-party Loop purpose, durable state, `expand/done/blocked` decision model, completion gates, Discover mode and self-improve surface.
- [`src/goals/supervisor-prompts.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor-prompts.ts) — explicit separation of execution and independent reflection/current-control decisions.
- [`src/goals/supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor.ts) — long-horizon supervisor loop, reflection closure, structural/frontier/runtime gates and automatic completion verification.
- [`src/tools/goal-tools.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/goal-tools.ts) — goal state/control semantics, read-only verification restrictions and reflection-only decision surface.
- [`src/goals/verifier.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/verifier.ts) — checker-not-maker contract and specialized verifier roles.
- [`src/loop/verifier-suite.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/verifier-suite.ts) — multi-role verifier suites, separate child sessions and optional worktree isolation.
- [`src/daemon/supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/daemon/supervisor.ts) — durable daemon supervision, worktree goal runs and `autoVerifyCompletion: true` path.
- [`website/docs/workflows/daemon-jobs.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/daemon-jobs.md) — supported long-running detached/reattached goal lifecycle.
- [`src/loop/subagents.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/subagents.ts) — bounded delegated child sessions and optional worktree isolation.
- [`src/tools/subagent-tool.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/subagent-tool.ts) — standard model-callable subagent execution path and returned child evidence.
- [`src/loop/worktree.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/worktree.ts) — managed worktree creation/adoption/health and merge preflight.
- [`src/loop/workers.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/workers.ts) — projection of verifier/supervisor/run/subagent workers and current lifecycle status.
- [`src/loop/discovery.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/discovery.ts) — scheduled sensing of GitHub, local-git, HTTP and npm signals into discovery candidates.
- [`src/loop/inbox.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/inbox.ts) — attention queue and explicit candidate/job promotion path.
- [`src/loop/policy.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/policy.ts) — unattended completion/tool gates and explicit learned-skill adoption policy.
- [`src/loop/learning.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/learning.ts) — self-improve evidence/proposal/replay support inspected for S4.

## Operational model

A Loop objective persists beyond a single model turn. Execution turns inspect/change/test the workspace and update plan, coverage, frontier, evidence and residual-risk state. When the current horizon is exhausted, a distinct reflection turn reviews the objective-level state and chooses whether to expand work, declare completion or block. Deterministic gates can prevent premature completion and invoke a complementary verifier. Daemon mode keeps the same Goal state and supervision alive outside the foreground TUI.

## S1 — Operations

- State: A
- Function: carry a long-horizon coding or research objective through repeated model/tool execution until a concrete environmental outcome is produced and evidence is recorded.
- Disturbance / variety regulated: changing repository state, ambiguous implementation/research findings, command/test/tool results, model/tool failures, context limits, resumed sessions, blockers and evidence discovered during execution.
- Decisive decision or feedback right: choose the next substantive implementation/research/tool action from current objective, workspace and evidence, then update the persistent Loop state from the result.
- Decision owner: the active Inferoa work agent/model during ordinary execution turns.
- Supporting / enforcement mechanisms: Runtime/model gateway, tool registry, persistent SessionStore, Goal state, permissions, context compression, daemon lifecycle, managed worktrees and deterministic structural completion rules.
- Closure path: objective enters `/loop` → execution model selects and performs workspace/research actions → tool/environment results return → agent updates step/coverage/frontier/evidence/risk state → later execution turns continue from the changed state until the horizon is exhausted and control passes to reflection.
- Boundary reachability: `/loop` is the documented standard long-horizon product surface, and daemon goal mode runs the same Goal supervisor outside the foreground TUI.
- Why this is / is not agent-owned: runtime machinery executes, persists and constrains actions, but removing the work agent eliminates the substantive choice of what to inspect, implement, benchmark, compare or verify next.
- Evidence: [`loop-mode.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/loop-mode.md); [`supervisor-prompts.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor-prompts.ts); [`supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor.ts); [`daemon/supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/daemon/supervisor.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference is a dependency, but Inferoa supplies the standard first-party execution/state/tool loop that repeatedly invokes and closes model decisions against the workspace.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the assessed Loop recursion.
- Disturbance / variety regulated: no qualifying inter-S1 interference/oscillation relation was established.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: session/worktree isolation, managed worktrees, subagent boundaries, daemon job lifecycle and merge preflight can prevent or contain execution interference, but they are not enough by themselves to establish S2.
- Closure path: not applicable; no reviewed path reconstructs distinct S1 units → concrete inter-S1 disturbance → S2-specific attenuation → returned coordination feedback that changes subsequent S1 behaviour.
- Distinct S1 units: the durable Loop itself is the established primary S1 at this recursion. Bounded subagents/verifier jobs are delegated execution/checking helpers and are not promoted to separate S1 units merely because they run in child sessions or worktrees.
- Inter-S1 disturbance: not established at the declared recursion. Potential repository conflicts between independently created worktrees are generic implementation risk unless a first-party organizational coordination relation around multiple credited S1s is shown.
- Attenuating coordination relation: managed worktree isolation and merge preflight are strong containment/enforcement mechanisms, but the reviewed standard path does not tie them to a qualifying inter-S1 coordination conversation with feedback into multiple S1 behaviours.
- Feedback into subsequent S1 behaviour: not established for an S2-specific relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not mapped as S2. The assessment intentionally refuses to count child spawning, session isolation, job queues or worktrees as coordination without the Profile witness.
- Why this is / is not agent-owned: no S2 function is established, so autonomy classification does not proceed.
- Evidence: [`subagents.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/subagents.ts); [`subagent-tool.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/subagent-tool.ts); [`worktree.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/worktree.ts); [`workers.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/workers.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: a deployment could potentially compose multiple long-lived Inferoa Loop organizations and coordinate them through additional first-party or downstream machinery; that is a different system boundary and is not inferred here.

### Absence scope

- Surfaces inspected: main Loop execution/supervision, subagent tool and child sessions, managed worktrees/adoption, daemon job scheduling, worker projection, verifier suites and session/worktree isolation.
- Plausible first-party paths checked: parent→subagent delegation, session isolation, worktree isolation, merge preflight/adoption, daemon queueing and worker status projection.
- Why no material first-party path remains: reviewed mechanisms either delegate/sequence bounded work, isolate execution or expose status. None establishes the complete Profile S2 witness at the declared Loop recursion.

## S3 — Inside-and-now control

- State: A
- Function: regulate the Loop's current whole-objective commitments, priorities and continuation state across execution horizons using objective-level evidence rather than merely continue the current local plan.
- Disturbance / variety regulated: local-plan exhaustion, incomplete objective coverage, unresolved frontier candidates, residual risk, runtime minimums, structural completion debt, missing verification and blockers that can make the current local horizon insufficient for the whole objective.
- Decisive decision or feedback right: independently choose `expand`, `done` or `blocked` for the current Loop horizon and, when expanding, define the next concrete work commitments against the original objective.
- Decision owner: the autonomous model actor in the internal `reflection` request class.
- Supporting / enforcement mechanisms: persistent Goal state, coverage/frontier/evidence/risk ledgers, candidate and structural completion gates, runtime minimum, deterministic supervisor transitions, verification policy and daemon lifecycle.
- Closure path: S1 execution updates persistent whole-objective state → supervisor invokes a separate internal reflection turn → reflection actor reconstructs objective decomposition and chooses `expand`/`done`/`blocked` → runtime validates structural/frontier/runtime/verifier constraints and persists the accepted transition → subsequent execution is expanded, paused/blocked or completed accordingly.
- Boundary reachability: reflection is part of the standard `/loop` supervisor and daemon goal path; it is not a development-only evaluator.
- Whole-system current view: the reflection prompt explicitly requires re-reading the top-level objective and reconciling coverage surfaces, uninspected surfaces, frontier items, rejected branches, residual risks, assumptions, delivery/research contract and executed evidence rather than treating the current checklist as the system boundary.
- Current-control decision scope: whether the organization should continue current work, open a new horizon with concrete commitments, block for missing external authority/input or terminate the Loop as complete.
- Why this is / is not agent-owned: deterministic gates can reject an unsafe/premature `done` and enforce invariants, but they do not independently generate the same discretionary `expand/done/blocked` judgment over the objective. Removing the reflection agent leaves rules but removes the substantive current-control choice and next-horizon design.
- Evidence: [`supervisor-prompts.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor-prompts.ts); [`supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor.ts); [`goal-tools.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/goal-tools.ts); [`loop-mode.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/loop-mode.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: this mapping credits objective-level current-control over commitments and continuation, not the mere existence of a component named supervisor or planner.

## S3* — Complementary audit

- State: A
- Function: independently challenge the work agent's completion/correctness claims through a checker path with materially different authority and direct access to operational evidence.
- Disturbance / variety regulated: overclaimed completion, missing tests/evidence, implementation defects, security/privacy/permission risk, stale documentation, weak research conclusions and other failures that ordinary work-agent self-reporting may miss.
- Decisive decision or feedback right: issue an independent structured verification verdict from direct evidence as a checker rather than implementer.
- Decision owner: the verifier model actor in the dedicated `verification` request class / verifier role.
- Supporting / enforcement mechanisms: verifier-specific prompts/roles, read-only Goal tool restrictions, separate internal runs, optional separate child sessions/worktrees, verification records, verifier policy and completion gates.
- Closure path: work agent/reflection presents completion candidate and evidence → verifier independently inspects loop state plus relevant files/diffs/commands/resources/tests → verifier records checker verdict → completion policy consumes that verdict → valid pass can permit completion; missing/non-passing evidence pauses or keeps the Loop from closing and further work can follow.
- Boundary reachability: daemon goal supervision sets `autoVerifyCompletion: true`; first-party TUI/CLI verifier suites also expose multi-role verification in normal product operation.
- Claim being audited: that the current bounded Loop work is sufficiently correct/evidenced to satisfy completion or a specified implementation/test/security/docs/research review concern.
- Ordinary reporting path: the work agent updates goal step/coverage/frontier/evidence/residual-risk state and the reflection actor can propose `done` with verification evidence.
- Complementary access path: verifier runs are instructed to inspect current state, recent evidence, relevant files, diffs, commands, resources and test results directly and to try to falsify completion rather than rely on assistant narrative.
- Independence boundary: `verification` runs are restricted to goal inspection/verdict recording, are told not to implement or mutate the plan, and verifier suites can use separate child sessions and isolated worktrees with role-specific prompts.
- Who acts on findings: the Goal supervisor/completion policy consumes verification records; failures or missing required passes prevent completion and return the organization to paused/additional-work paths.
- Why this is / is not agent-owned: runtime policy stores/enforces the verdict, but the evaluative judgment is produced by an autonomous verifier model from direct evidence. Removing the verifier actor leaves the gate but not the independent audit judgment.
- Evidence: [`verifier.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/verifier.ts); [`verifier-suite.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/verifier-suite.ts); [`goal-tools.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/goal-tools.ts); [`supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/goals/supervisor.ts); [`daemon/supervisor.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/daemon/supervisor.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: the strongest independence mode is the isolated verifier-suite path; the automatic completion verifier may share the parent session store/model provider while still having a distinct read-only request class and checker authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party S4 organizational adaptation loop is established at the assessed Loop recursion.
- Disturbance / variety regulated: not established as an outside-and-then organizational adaptation function.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: Discover loops can run experiments and compare hypotheses; scheduled discovery senses GitHub/local-git/HTTP/npm conditions; inbox candidates can be explicitly promoted to work; self-improve can turn verified historical Loop evidence into a staged skill proposal and explicit adoption can enable a learned skill.
- Closure path: not applicable for S4; no reviewed standard path closes external/future sensing → development of organizational adaptation options → decisive adaptation judgment → returned change in present organizational capability/S3 as the system's S4 function.
- Why this is / is not agent-owned: Discover mode is objective-local research, not automatically organizational adaptation. Scheduled discovery mostly converts external/current signals into work candidates, and promotion is an explicit control-plane action. Self-improve is evidence-driven learning with explicit adoption; the Profile explicitly does not equate generic learning/self-improvement with S4 without an external-and-prospective adaptation conversation.
- Evidence: [`loop-mode.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/loop-mode.md); [`discovery.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/discovery.ts); [`inbox.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/inbox.ts); [`policy.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/policy.ts); [`learning.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/learning.ts).
- Basis: explicit + structural absence review
- Confidence: medium-high
- Caveats: a wider operator/workspace recursion could potentially organize discovery plus skill-adoption mechanisms into an S4 path. That wider organization would need its own boundary and evidence; it is not silently credited to one Loop objective.

### Absence scope

- Surfaces inspected: Discover preference and autoresearch state; scheduled discovery sources; inbox candidate projection/promotion; self-improve proposal/replay/adopt; skill policy; goal reflection/current-control loop; automation and daemon supervision.
- Plausible first-party paths checked: GitHub issue/PR/review/action/deployment sensing, npm package mismatch and HTTP health sensing, local git-change sensing, Discover-mode benchmarks/hypotheses, learned skill proposals and explicit skill adoption.
- Why no material first-party path remains: these surfaces either ingest work/environment signals into the current operational queue, perform research scoped to the active objective, or learn from prior internal evidence under explicit adoption. The reviewed evidence does not reconstruct the required external/prospective organizational adaptation conversation back into present capability at this recursion.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed Loop recursion.
- Disturbance / variety regulated: not established as an identity/ultimate-policy matter.
- Decisive decision or feedback right: not established.
- Decision owner: none established within the standard Loop boundary.
- Supporting / enforcement mechanisms: user-supplied objective/preference/runtime/HIL policy, permission modes, unattended safety gates, approval surfaces, verifier policy, skill configuration and explicit learned-skill adoption constrain or configure operation but do not establish S5.
- Closure path: not applicable; no reviewed path shows an identity/ultimate-policy issue reaching a legitimate ultimate authority and returning as authoritative policy governing subsequent Loop operation.
- Why this is / is not agent-owned: work/reflection/verifier agents operate inside configured objective, safety and permission boundaries. They are not shown deciding the Loop organization's ultimate identity or policy. Human review/approval of a task, skill or external mutation is not promoted to S5 merely because the user has final say.
- Evidence: [`policy.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/policy.ts); [`loop-mode.md`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/website/docs/workflows/loop-mode.md); [`goal-tools.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/tools/goal-tools.ts); [`inbox.ts`](https://github.com/agentic-in/inferoa/blob/1fd9ec4518b26b60cc78cf67c4faf337fe9bb2cd/src/loop/inbox.ts).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: an operator can define objectives, review work and configure policy, but Methodology `0.3.6` requires identity-level closure rather than generic task/control authority.

### Absence scope

- Surfaces inspected: Loop objective/preference/runtime configuration, HIL/review controls, permission and unattended safety policy, verifier policy, external-action approval, skill configuration/adoption and user-facing Loop control actions.
- Plausible first-party paths checked: `/loop` objective creation, review/approve/revise, pause/resume/drop, permission configuration, external mutation approval, verifier policy changes, learned-skill adoption and general configuration changes.
- Why no material first-party path remains: these are task-, capability-, permission- or configuration-level controls. No current first-party path elevates a genuine identity/ultimate-policy issue to an authoritative S5 decision and returns that decision to govern the Loop as an organization.

## Distributed OSS parent arrangement

Inferoa is open source, but repository contributor/maintainer governance was not used to infer runtime parent ownership. The assessed recursion is one operating Loop objective/session. Development roadmap, maintainer decisions and release/CI mechanisms remain adjacent unless an explicit runtime return loop is shown; none is needed for the positive S1/S3/S3* claims here.

## Self-hosted and non-human modes

Inferoa is self-hostable and exposes substantial operator control, but generic user review, pause/resume/drop, config changes and approval surfaces are not enough for Methodology parent notation. No distinct qualifying parent-governed S3/S4/S5 mode is claimed. S3 is credited to the autonomous reflection actor in the standard Loop supervisor; S4/S5 remain absent at this boundary.

## Recursion

The primary recursion is one durable Loop objective/session. Its work agent closes S1; internal reflection provides metasystemic current control; verifier actors provide complementary audit. Subagents and verifier children are lower-level bounded actors created for specific tasks/checks, but their existence alone does not prove recursive viability or inter-S1 coordination at the parent Loop recursion.

## Variety and escalation

Inferoa attenuates variety through persistent structural state, bounded context/compaction, tool/permission gates, managed worktrees, verifier policy, coverage/frontier/evidence ledgers and deterministic completion constraints. The work agent amplifies response variety through tools, subagents, experiments and model routing. Current-control variety is transduced into explicit `expand/done/blocked` decisions. Audit variety returns through structured verification verdicts. User feedback/review and blocked states provide external escalation for missing authority/input without being treated automatically as S5.

## Evidence gaps

- No fresh runtime trace was executed inside this assessment environment; positive claims rely on pinned first-party source/docs and production wiring.
- S2 is intentionally conservative: subagents, worker projections, queues and worktrees were inspected, but no complete Profile S2 witness was established at the selected recursion.
- S3 is credited specifically to the separate objective-level reflection decision path, not to the existence of a `supervisor` class or deterministic completion gates.
- S3* is strongest in the isolated verifier-suite/daemon-completion paths; the assessment does not claim that every verification invocation is maximally independent.
- Discover/discovery/self-improve surfaces were explicitly inspected for S4 and rejected as insufficient at this boundary rather than being promoted from naming alone.
