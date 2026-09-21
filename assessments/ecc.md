---
harness_id: ecc
project_name: Everything Claude Code (ECC)
repository: https://github.com/affaan-m/ECC
review_ref: 2b6e839771e53096d8451a213d40dc64ec8acac0
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# Everything Claude Code (ECC)

## Review boundary

- System in focus: the public ECC distribution at pinned revision `2b6e839771e53096d8451a213d40dc64ec8acac0`, including shipped skills/agents/hooks, NanoClaw, the runnable `ecc2/` Rust control-plane alpha, multi-session/worktree/message state, proximity advisories, independent-review skills, and continuous-learning-v2.
- Purpose and identity: provide an operating layer around model-driven coding/agent sessions so they can run persistently, be organized into teams/worktrees, coordinate current work, undergo independent review, and carry learned behavior into later sessions.
- Relevant environment: user tasks/corrections, repository and worktree state, external harness/model responses, running agent sessions, task handoffs, backlog pressure, overlapping edits, dependency coupling, review evidence and recurring behavioral patterns.
- Standard-distribution boundary: ECC-owned scripts, skills, agents, hooks, control-plane code and `ecc2/` runtime are credited. Claude Code, Codex, OpenCode, Gemini and other launched harnesses are execution dependencies; their internal S2–S5 functions are not inherited.
- Credited operating / distribution surfaces: ECC plugin/skill operation; `scripts/claw.js`; `ecc2` local alpha commands/daemon; session/worktree/message store; Delegate/Assign/AutoDispatch/CoordinateBacklog/Rebalance paths; proximity live view/advisory feed; Santa Method; continuous-learning-v2 observer and SessionStart instinct injection.
- Adjacent first-party surfaces excluded from ownership: repository CI/release governance, business/roadmap material, design-only mechanisms not yet implemented, tests/examples that only demonstrate intended behavior, and hosted/commercial surfaces not required by the public local distribution.
- First-party operating / deployment modes considered: NanoClaw sessions; ECC2 local multi-session alpha; operator-driven ECC2 TUI/CLI; Santa Method review; enabled continuous-learning-v2 observer mode; explicit learned-instinct promotion.
- Recursion level: one ECC-managed project/runtime organization. ECC-managed model-driven sessions are S1 units; ECC2 control/coordination operates at the team/project recursion; reviewers are complementary audit actors; continuous learning returns adaptations into later sessions.
- Reviewed revision: `2b6e839771e53096d8451a213d40dc64ec8acac0`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

ECC combines a large host-harness skill/agent/hook layer with concrete first-party runtime surfaces. `scripts/claw.js` is a persistent session-aware loop around `claude -p`. The runnable `ecc2/` alpha owns session lifecycle, SQLite state, worktree scaffolding, task handoffs, messages, schedules, remote intake, daemon operation and process launch for supported external agent harnesses.

ECC2 therefore supplies an organizational boundary above external coding harnesses: it starts named model-driven sessions, tracks them, groups delegates, moves work through task handoffs and can stop/resume them. The launched model-driven session owns its own substantive operational choices; ECC owns the surrounding organizational substrate.

ECC's proximity subsystem is more specific than generic shared state. It derives collision risk from overlapping working sets and dependency/tree coupling and emits a right-of-way advisory. But `docs/control-plane/TCAS-HOOK.md` explicitly says the pre-edit hook that would return `pause`/`wait`/`steer` into an agent is design-only and not implemented. The current result is therefore S2=C, not A.

ECC2 exposes substantial current-control machinery — Delegate, Assign, backlog dispatch/maintenance, rebalance, team/status, stop/resume and worktree merge controls — but no shipped autonomous model is established as the discretionary whole-team S3 owner. The human operator can close the same current-control loop through TUI/CLI surfaces, supporting `C(P)`.

Complementary audit is closed by Santa Method: two separate reviewers inspect the same candidate/spec under isolated contexts, any failure feeds a fix cycle, and fresh reviewers re-audit until both pass or the bounded process escalates.

Continuous-learning-v2 closes a future-adaptation loop. Hooks capture operational evidence; a background Haiku observer detects corrections/error resolutions/repeated workflows and writes evidence-backed instincts; SessionStart later injects qualifying learned instincts into agent context. A user can separately promote a selected project instinct to global scope.

No comparable identity/ultimate-policy closure is established. Rules, consent, security hooks, profiles, configuration and learned preferences regulate operation but do not constitute an S5 identity/constitutional authority loop.

Primary evidence:

- [`README.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/README.md)
- [`ecc2/README.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/README.md)
- [`ecc2/src/main.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/main.rs)
- [`ecc2/src/session/manager.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/session/manager.rs)
- [`scripts/claw.js`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/scripts/claw.js)
- [`docs/design/agent-proximity.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/design/agent-proximity.md)
- [`docs/control-plane/VIEW-CONTRACT.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/control-plane/VIEW-CONTRACT.md)
- [`docs/control-plane/TCAS-HOOK.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/control-plane/TCAS-HOOK.md)
- [`skills/team-agent-orchestration/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/team-agent-orchestration/SKILL.md)
- [`skills/santa-method/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/santa-method/SKILL.md)
- [`skills/continuous-learning-v2/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/continuous-learning-v2/SKILL.md)
- [`skills/continuous-learning-v2/agents/observer.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/continuous-learning-v2/agents/observer.md)
- [`scripts/hooks/session-start.js`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/scripts/hooks/session-start.js)

## Operational model

ECC starts or wraps model-driven sessions, records their state and worktree context, and keeps them addressable through first-party control surfaces. ECC2 can create delegates, assign/reuse capacity, route task handoffs, rebalance backlog and expose project/team state. Proximity logic independently derives collision risk from actual session worksets. Santa Method provides a separate independent-review topology. Continuous-learning-v2 observes prior work and returns learned instincts to later sessions.

## S1 — Operations

- State: A
- Function: autonomously execute assigned project work inside ECC-managed model-driven sessions.
- Disturbance / variety regulated: task ambiguity, repository state, tool/test observations, failures, intermediate artifacts and uncertainty about the next substantive action.
- Decisive decision or feedback right: choose implementation/tool actions and iterate from observations until the assigned task completes or terminates.
- Decision owner: the model-driven agent session launched/managed by ECC.
- Supporting / enforcement mechanisms: ECC2 lifecycle/store, worktrees, process launch, session identity, output capture, stop/resume and NanoClaw persistence where used.
- Closure path: assigned task → ECC-managed model session → model-selected actions → repository/tool observations → further model actions → session result/state.
- Boundary reachability: ECC2 `start` and the session manager directly launch supported model-driven agent sessions; NanoClaw is also shipped first-party.
- Why this is / is not agent-owned: ECC lifecycle code manages the process but does not choose its substantive next coding/tool action.
- Evidence: [`ecc2/src/main.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/main.rs), [`ecc2/src/session/manager.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/session/manager.rs), [`scripts/claw.js`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/scripts/claw.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the launched host harness retains its own internal tool-loop implementation; its S2–S5 semantics are not imported.

## S2 — Coordination

- State: C
- Function: attenuate concrete collision risk among parallel agent S1 units working on overlapping/coupled repository state.
- Disturbance / variety regulated: same-file/line overlap and dependency/tree coupling that can make concurrent changes interfere.
- Decisive decision or feedback right: compute right-of-way and an S2-specific `hold`/`steer` advisory; a return consumer must still apply that maneuver to the affected S1.
- Decision owner: no autonomous owner is closed over the full loop; current right-of-way is deterministic and the agent-return actor is absent.
- Supporting / enforcement mechanisms: working-set extraction, dependency graph, overlap/dependency/tree risk channels, priority calculation, advisory feed and worktree isolation.
- Closure path: parallel worksets → collision-risk calculation → `hold`/`steer` advisory → constructor gap at the return leg into S1 behavior.
- Boundary reachability: the scanner and advisory/event contract are shipped first-party paths specifically designed around inter-agent collision; the missing TCAS hook prevents A.
- Why this is / is not agent-owned: deterministic right-of-way calculation is not autonomous organizational ownership; ECC exposes the S2-specific path but not its autonomous closure.
- Evidence: [`docs/design/agent-proximity.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/design/agent-proximity.md), [`docs/control-plane/VIEW-CONTRACT.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/control-plane/VIEW-CONTRACT.md), [`docs/control-plane/TCAS-HOOK.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/docs/control-plane/TCAS-HOOK.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `TCAS-HOOK.md` explicitly marks the return hook design-only; older design prose must not be read as proof that steering is already wired.
- Distinct S1 units: separate ECC-managed model-driven sessions/worktrees acting concurrently on the same project.
- Inter-S1 disturbance: overlapping edits and dependency-coupled changes create concrete collision/merge risk between those sessions.
- Attenuating coordination relation: ECC proximity computes pairwise risk, priority/right-of-way and a `hold`/`steer` maneuver advisory.
- Feedback into subsequent S1 behaviour: ECC exposes the action-bearing advisory as the S2-specific return primitive, but the consumer that applies it before an edit remains to be composed; this is the constructor gap.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation exists specifically to reduce measured cross-agent code collision, with explicit pairwise risk and maneuver semantics rather than merely moving messages or tasks.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current team/session commitments, allocation, backlog pressure, intervention and worktree integration across an ECC-managed project.
- Disturbance / variety regulated: changing active/stopped sessions, unread handoffs, idle/saturated delegates, backlog pressure, worktree readiness and current need to add/reuse/rebalance/stop capacity.
- Decisive decision or feedback right: choose delegation/assignment/rebalance/stop/resume/merge actions from current team state.
- Decision owner: constructor mode — autonomous owner must be composed; parent mode — the human operator.
- Supporting / enforcement mechanisms: session/message store, dashboard/team/status, delegate-selection scoring, backlog counts, worktree state and daemon/process lifecycle.
- Closure path: current team/backlog/worktree view → operator or composed controller chooses intervention → ECC executes it → commitments/state change → refreshed view reflects the result.
- Boundary reachability: ECC2 ships Delegate/Assign/AutoDispatch/CoordinateBacklog/Rebalance/Stop/Merge surfaces and current team/status views.
- Why this is / is not agent-owned: deterministic assignment/maintenance can execute policy but does not constitute a model-owned whole-team discretionary judgment; the operator path is separately closed.
- Evidence: [`ecc2/src/main.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/main.rs), [`ecc2/src/session/manager.rs`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/ecc2/src/session/manager.rs), [`skills/team-agent-orchestration/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/team-agent-orchestration/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ECC2 is explicitly alpha; roadmap-only autonomous orchestration is not credited.
- Whole-system current view: dashboard/session/team/coordination-status surfaces expose active sessions, delegate relationships, backlog/current state and worktree information at the project recursion.
- Current-control decision scope: delegation/reuse/spawn, backlog redistribution, stop/resume, team intervention and worktree merge/integration.

### Ownership modes

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | developer-composed autonomous controller | current team/backlog/worktree state requires intervention | controller selects ECC's function-specific current-control path → ECC executes → current state changes | `ecc2/src/main.rs`, `ecc2/src/session/manager.rs` |
| Parent (`P`) | human operator | operator inspects dashboard/team/status state | operator selects current-control command → ECC executes → live team/worktree state changes | `ecc2/src/main.rs`, `ecc2/README.md` |

## S3* — Complementary audit

- State: A
- Function: independently audit a candidate using complementary reviewer actors and return defects into corrective production work before shipping.
- Disturbance / variety regulated: semantic defects, hallucinations, incompleteness, compliance violations and technical errors the producer may miss.
- Decisive decision or feedback right: two isolated reviewers independently issue structured PASS/FAIL judgments; any failure blocks shipping and supplies issues to a fix cycle followed by fresh reviewers.
- Decision owner: the two independent reviewer agents for audit judgment.
- Supporting / enforcement mechanisms: identical rubric/input contract, context isolation, structured verdicts, deterministic both-pass gate, bounded iterations and escalation.
- Closure path: candidate → independent reviewers → findings → both-pass gate or fix issue set → revised candidate → fresh reviewers → ship or bounded escalation.
- Boundary reachability: Santa Method is a shipped ECC skill intended for supported hosts with subagent capability and specifies the full reviewer/correction topology.
- Why this is / is not agent-owned: the semantic audit judgments come from separate model actors; deterministic code only aggregates their verdicts.
- Evidence: [`skills/santa-method/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/santa-method/SKILL.md), [`commands/santa-loop.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/commands/santa-loop.md).
- Basis: explicit.
- Confidence: high.
- Caveats: strongest independence requires a supported host's separate subagent contexts; the documented inline fallback is weaker and is not the basis for A.
- Claim being audited: the produced candidate's correctness/completeness/compliance against the original specification and rubric.
- Ordinary reporting path: the producing agent's own output and deterministic build/test checks remain the normal production evidence.
- Complementary access path: two fresh reviewer agents independently receive the same original specification, candidate and rubric outside the producer's context.
- Independence boundary: reviewers are separate agent contexts/processes and do not share each other's assessments; fresh reviewer instances are required after fixes.
- Who acts on findings: a fix/production agent receives the merged critical issues, revises the candidate and submits it to fresh review.

## S4 — Outside-and-then adaptation

- State: A(P)
- Function: turn operational experience and corrections into persistent learned behaviors that alter later ECC-hosted sessions.
- Disturbance / variety regulated: repeated user corrections, error-resolution patterns, repeated workflows and project-specific versus general behavioral distinctions.
- Decisive decision or feedback right: base mode — background Observer identifies pattern/content/scope and updates an instinct; parent mode — user selects a project instinct for promotion to global scope.
- Decision owner: base mode — Observer/Haiku agent; parent mode — human user for explicit promotion.
- Supporting / enforcement mechanisms: tool-use observation hooks, project detection, observation logs, confidence scoring, observer schedule, instinct stores and SessionStart injection.
- Closure path: operational evidence → observer pattern judgment → persistent instinct → later SessionStart injection → subsequent agent behavior changes; parent promotion can widen a selected instinct's future scope.
- Boundary reachability: continuous-learning-v2 ships the hooks, observer agent/loop, instinct store/CLI and SessionStart injection; the background mode is explicitly supported when enabled.
- Why this is / is not agent-owned: deterministic capture/thresholds support the loop, while the observer model decides the learned pattern; the learned result is then automatically returned into later context.
- Evidence: [`skills/continuous-learning-v2/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/continuous-learning-v2/SKILL.md), [`skills/continuous-learning-v2/agents/observer.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/continuous-learning-v2/agents/observer.md), [`scripts/hooks/session-start.js`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/scripts/hooks/session-start.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: observer defaults to disabled and is not viable as a persistent background process on native Windows; the A claim is for the supported enabled mode.
- External distinction: user corrections, observed failures/resolutions and repeated workflows/tool preferences captured from real prior sessions.
- Future / prospective distinction: whether those observed patterns should become reusable behavior in subsequent sessions/projects rather than only solve the current task.
- Adaptation option generated: evidence-backed project/global instincts with a trigger, action, scope and confidence; related instincts can additionally be evolved/promoted.
- Path back into current capability / S3: qualifying instincts are automatically injected at later SessionStart, changing the behavioral context available to future S1 work; parent promotion can widen their scope.

### Ownership modes

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | background Observer model | observation threshold/observer interval | observer creates/updates instinct → persistence/confidence → later SessionStart injection → future behavior changes | `skills/continuous-learning-v2/agents/observer.md`, `scripts/hooks/session-start.js` |
| Parent (`P`) | human user | explicit selection of a project instinct for promotion | selected adaptation becomes global → later SessionStart can apply it across projects | `skills/continuous-learning-v2/SKILL.md`, `skills/continuous-learning-v2/scripts/instinct-cli.py` |

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the reviewed ECC project/runtime recursion.
- Disturbance / variety regulated: no qualifying identity/constitutional disturbance is established.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5 publication.
- Supporting / enforcement mechanisms: consent/safety boundaries, profiles, permissions, rules, security hooks, governance capture, learned preferences and operator configuration.
- Closure path: no standard path is established from a genuine identity/ultimate-policy matter through authoritative S5 judgment back into governing whole-system operation.
- Why this is / is not agent-owned: ECC's policy surfaces regulate tasks/tools/review/security but do not establish an identity/constitutional authority organ at this recursion.
- Evidence: [`README.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/README.md), [`skills/autonomous-agent-harness/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/autonomous-agent-harness/SKILL.md), [`skills/continuous-learning-v2/SKILL.md`](https://github.com/affaan-m/ECC/blob/2b6e839771e53096d8451a213d40dc64ec8acac0/skills/continuous-learning-v2/SKILL.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: a downstream organization can impose an identity/constitution using ECC primitives; that separate system requires its own assessment.

### Absence scope

- Surfaces inspected: product/install architecture, ECC2 current-control/configuration, agent/skill rules, consent boundaries, security/governance hooks, learned identity/preferences data and operator settings.
- Plausible first-party paths checked: user/profile memory, rules/permissions, approval/consent, security posture, harness profiles, learned instincts and configuration controls.
- Why no material first-party path remains: these paths govern operational behavior or capability selection but do not establish a genuine identity/ultimate-policy issue, legitimate S5 authority and return-to-operation closure.

## Recursion

ECC's managed agent sessions are S1 units inside a team/project recursion. ECC2 S2/S3 paths regulate relations and commitments among those units. Santa reviewers are complementary audit actors rather than production S1s. Continuous learning sits across session time and returns adaptations to later operation. External host harnesses retain their own internal organizations and are not credited above their ECC-managed S1 role.

## Evidence gaps

- No live ECC installation was executed; conclusions use pinned repository code/docs and explicit implementation-status statements.
- `ecc2/` is alpha; only runnable/shipped behavior at the pinned ref is credited.
- S2 remains `C` because the action-bearing advisory exists but the documented pre-edit return hook does not.
- S3 remains `C(P)` because no first-party autonomous model actor is established as the whole-team current-control owner.
- S4 is mode-dependent: the autonomous observer is opt-in and platform-sensitive.
