---
harness_id: mission-control
project_name: Mission Control
repository: https://github.com/CosmonautJones/mission-control
review_ref: 9337744f7ec940234ecdc2936fa426d70598d26d
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Mission Control

## Review boundary

- System in focus: one first-party Mission Control installation at pinned revision `9337744f7ec940234ecdc2936fa426d70598d26d`, including the local Oversight cockpit, `packages/harness` rails, mission/workflow/fleet state, child/worktree spawning, risk-typed approval routes, append-only audit, budget/cap controls, operator steering, verification/re-dispatch, quarantine and synthesis/report control.
- Purpose and identity: provide a local governance cockpit for multiple coding-agent sessions and an opt-in control plane that can launch and govern bounded autonomous work while keeping consequential approvals attributable to a human operator.
- Relevant environment: human operators/approvers; Claude Code and other external coding/model workers reached through adapters; project repositories and git worktrees; operating-system sandboxing; tool/MCP surfaces; provider/runtime state under `~/.claude`; and downstream projects adopting the harness rails.
- Standard-distribution boundary: the shipped cockpit plus the first-party harness/adapters and Fleet runtime. External Claude/model reasoning remains a separate operational actor. Read-only parsing of `~/.claude` does not transfer Claude Code's internal functions into Mission Control. OS-level sandboxing and downstream project governance remain environmental controls.
- Credited operating / distribution surfaces: root `README.md`; `apps/cockpit/server/fleet/fleet-runner.js`; `apps/cockpit/server/fleet/verifier.js`; cockpit approval/steering/audit/runtime surfaces described by the standard distribution; `packages/harness/AGENTS.md`; `.harness/learning-policy.yml`; `.harness/human-approval-policy.yml`.
- Adjacent first-party surfaces excluded from ownership: Mission Control repository-development CI, maintainer review, release/tag decisions, roadmap documents that are not reached by the installed runtime, and the internal organizational functions of external Claude/other workers.
- First-party operating / deployment modes considered: localhost cockpit observing existing agent sessions; opt-in project rails; workflows launched from the cockpit; Fleet multi-child execution in isolated worktrees; optional adversarial verification; operator approval/steering and kill-switch control; post-settle synthesis; assisted harness-improvement logging/proposal.
- Recursion level: the installed Mission Control cockpit/control plane is the system-in-focus. Fleet worker and verifier sessions are lower-recursion S1 actors governed by that installation; a worker's own internal subagents are not promoted into installation-level functions merely because the cockpit can observe them.
- Reviewed revision: `9337744f7ec940234ecdc2936fa426d70598d26d`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Mission Control combines a local multi-agent cockpit with optional per-project harness rails. The cockpit can observe existing Claude Code sessions without claiming their reasoning, while Fleet is a first-party execution path that takes a goal plus child specifications and launches multiple external Claude sessions with `--worktree`, persisted run state, hard child ceilings, optional cost budgets, approval escalation and post-settle synthesis.

The control plane deliberately keeps consequential current interventions visible. Live sessions and Fleet runs are summarized into UI/API state; approval requests are surfaced but never auto-approved; an operator can approve/deny through the existing audited write paths, steer a session, cancel work or engage a global Fleet kill-switch. Machine-facing HTTP/SSE/runtime surfaces make that observation-and-intervention path composable, but the standard distribution does not package an installation-wide autonomous supervisor that decides when those current-control interventions should be exercised.

Fleet's optional verification path is organizationally distinct from ordinary status checking. After a worker reports success, a new read-only verifier session is launched against the worker branch. Its prompt is explicitly adversarial and authorship-blind. An approval can close the worker; a rejection records reasons and, while `maxRounds` and budget permit, redispatches the worker with the prior rejection reasons injected into the next prompt. A malformed or failed verifier fails closed to rejection. A deterministic diff scanner exists as a safety backstop, but it is not the owner of the semantic review judgment.

## Operational model

An operator may use the cockpit purely as an oversight window or opt a project into the harness rails. In Fleet mode the operator supplies a goal, child work items and optional policy. Mission Control validates every child, enforces the known-root/git preconditions and spawn ceilings, persists run state, and launches each external worker in its own worktree. The worker owns task-local reasoning and acts until it exits, escalates or is stopped.

If verification is enabled, successful worker output is challenged by a separate verifier actor before the worker is treated as finally accepted. Once all workers and verifiers settle, Mission Control derives run status and can launch one synthesis pass over the branches/results. Budget and kill-switch latches can stop later spawning. These deterministic mechanisms enforce already-selected policy; they do not themselves decide the installation's changing current priorities or ultimate identity.

## S1 — Operations

- State: A
- Function: perform bounded coding or other project work against an admitted Fleet/workflow objective through externally reasoning coding-agent sessions launched and governed by Mission Control.
- Disturbance / variety regulated: repository state, implementation uncertainty, tool/environment feedback, mission-specific requirements, failures and reviewer feedback encountered while completing a child objective.
- Decisive decision or feedback right: choose the substantive task reasoning path and actions within the supplied goal/prompt, worktree and harness-policy envelope.
- Decision owner: the autonomous external Claude/model worker launched by the first-party Fleet/workflow path.
- Supporting / enforcement mechanisms: `runClaudeCancellable`, per-child worktrees/branches, persisted run state, cwd admission, timeouts, caps, budgets, harness hooks, approval escalation, quarantine prompt stance and cancellation.
- Closure path: operator/controller admits a goal and child specification → Mission Control validates and spawns an external worker with `--worktree` → the model chooses task actions and receives tool/repository feedback → the worker produces a result/diff or terminal failure/escalation → Mission Control records the outcome for verification/synthesis/control.
- Boundary reachability: Fleet and runnable Workflows are documented standard cockpit surfaces; `fleet-runner.js` directly invokes the external Claude CLI for each admitted child rather than relying on repository-development tooling.
- Why this is / is not agent-owned: the first-party runtime owns admission, lifecycle and constraints, but substantive task-local reasoning is performed by the external model actor and is reachable through the normal shipped Fleet/workflow path.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`apps/cockpit/server/fleet/fleet-runner.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/fleet-runner.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: merely reading pre-existing `~/.claude` sessions does not create S1 ownership for Mission Control. The positive finding is grounded in first-party Fleet/workflow launch paths that actually reach the external operational actor.

## S2 — Coordination

- State: —
- Function: no installation-level S2 mutual-adjustment function is established from the reviewed standard distribution.
- Disturbance / variety regulated: multiple Fleet workers can execute concurrently and potentially target related repository work, but the inspected paths do not establish a concrete interaction-generated oscillation/interference among sibling S1 units together with a first-party feedback relation whose purpose is to attenuate it.
- Decisive decision or feedback right: not established at the installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: separate worktrees/branches, concurrency ceilings, dollar/token-oriented budget structure, run-state persistence, child settlement derivation and post-settle synthesis constrain structure and resource use but do not by themselves satisfy the required S2 witness.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no installation-level S2 function was established, so there is no S2 decision right to classify.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`apps/cockpit/server/fleet/fleet-runner.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/fleet-runner.js).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: worktree isolation is valuable preventive structure, but the reviewed path does not show disturbance feedback returning into subsequent sibling behavior. Adversarial worker-review feedback maps to S3*, not sibling mutual adjustment, and synthesis occurs only after children settle.

### Absence scope

- Surfaces inspected: Fleet child fan-out, worktree/branch isolation, concurrency caps, cost projection/budget latches, cancellation/kill-switch behavior, verifier redispatch, settlement derivation, synthesis and workflow-to-Fleet execution.
- Plausible first-party paths checked: same-project parallel workers; worktree separation; shared run caps/budgets; post-settle synthesis; reviewer rejection loops.
- Why no material first-party path remains: the mechanisms isolate children, bound shared resource commitments, audit lifecycle and aggregate results, but no reviewed path senses a concrete sibling-generated disturbance and feeds a coordinating adjustment back into the affected siblings. The stronger current resource controls belong under S3, while verifier feedback is complementary audit.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current installation-wide agent/Fleet activity, risk approvals and resource commitments using live cockpit/run state and intervention controls.
- Disturbance / variety regulated: active workers can request risky tools, exceed desired cost, stall, loop, move in a wrong direction, need cancellation, or require an immediate stop across Fleet spawning.
- Decisive decision or feedback right: choose a current intervention — approve/deny an escalated action, steer a session, cancel work, engage/disengage the Fleet kill-switch, or alter the current run/policy configuration before launch.
- Decision owner: base constructor mode — no resident autonomous installation supervisor is supplied; a downstream controller can be composed over first-party machine-readable state and intervention surfaces. Parent mode — the human operator/approver using the cockpit.
- Supporting / enforcement mechanisms: live session/Fleet summaries, triage and risk classification, SSE/API state, approval write paths, append-only decision audit, session steering, cancellation, spawn ceilings, budget projection/latches, global kill-switch and boot reconciliation.
- Closure path: current session/Fleet/risk/cost state is observed → downstream controller or human operator selects an intervention → first-party write/control path records and applies it → runtime/spawn/approval machinery admits, denies, steers, stops or prevents subsequent work → updated current state returns to the cockpit/API.
- Boundary reachability: the standard cockpit exposes the Agents/Fleet/History surfaces and documented inline approve/steer operations; Fleet's runtime state, kill-switch and policy enforcement are first-party installed paths rather than maintainer-only controls.
- Why this is / is not agent-owned: deterministic caps, budgets, anomaly flags and kill-switch enforcement execute a policy but do not decide when the installation should change course. The product exposes an S3-specific observation/intervention path without assigning installation-wide current discretion to a resident autonomous manager.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`apps/cockpit/server/fleet/fleet-runner.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/fleet-runner.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Fleet's automatic settle/synthesis transitions, hard caps and anomaly detection are mechanisms within current regulation, not independent evidence of autonomous S3 decision ownership.
- Whole-system current view: the cockpit presents live multi-project agent state, attention-ranked approval needs, Fleet run/child status, current cost/budget state and history/audit evidence at the installation boundary.
- Current-control decision scope: risk approval/denial, live steering, run cancellation, emergency Fleet spawn stop/reset, and pre-run cap/budget/verification policy selection.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | downstream autonomous controller must be composed | current session/Fleet/risk/cost state indicates intervention | controller consumes first-party current state and invokes existing intervention paths; Mission Control enforcement changes subsequent operation | `README.md`; `apps/cockpit/server/fleet/fleet-runner.js` |
| Parent (`P`) | human operator / authorized approver | a live approval, risk, cost, wrong-direction or emergency condition requires action | operator approves/denies, steers, cancels or engages/disengages emergency control; first-party runtime records/enforces the decision and returns to current operation | `README.md`; `apps/cockpit/server/fleet/fleet-runner.js` |

## S3* — Complementary audit

- State: A
- Function: independently challenge a worker's completion claim against its branch diff and Fleet goal and return findings into bounded corrective work before final acceptance.
- Disturbance / variety regulated: a worker may exit successfully while its produced change is incorrect, incomplete, regressive, destructive or out of scope relative to the admitted goal.
- Decisive decision or feedback right: independently issue `approve` or `reject` with reasons/rubric evidence; rejection can trigger a bounded worker redispatch, while sufficient approvals allow final worker success.
- Decision owner: the fresh autonomous verifier model session, distinct from the worker that authored the candidate change.
- Supporting / enforcement mechanisms: separate verifier child lifecycle, read-only quarantine stance, authorship-blind adversarial prompt, worker-branch diff access, structured verdict parsing, fail-closed malformed/error handling, verdict history, `minApprovals`, bounded `maxRounds`, budget gating, prior-rejection reason injection and deterministic bad-diff backstop.
- Closure path: worker reports successful completion → Mission Control holds the worker in `verifying` → a new verifier session independently reads the worker branch/diff against the goal → verifier returns approve/reject → Mission Control records the verdict → reject reasons are injected into a subsequent worker prompt and the worker is redispatched while bounds permit, or the worker becomes terminal rejected; enough approvals close success → run state proceeds toward synthesis.
- Boundary reachability: adversarial verification is a first-party Fleet policy (`policy.verify`) documented in the shipped cockpit and implemented directly in `fleet-runner.js`; it is not repository-development review for Mission Control itself.
- Why this is / is not agent-owned: the semantic completion judgment belongs to a separately spawned autonomous reviewer actor. Deterministic parsing/bad-pattern checks and lifecycle policy constrain how its verdict is used but do not replace the reviewer judgment.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`apps/cockpit/server/fleet/fleet-runner.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/fleet-runner.js); [`apps/cockpit/server/fleet/verifier.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/verifier.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the LLM verifier is not treated as a security boundary; `verifier.js` supplies a deterministic backstop for a narrow forbidden diff pattern. That limitation does not remove the distinct complementary-review function or its corrective-return path.
- Claim being audited: the worker's implicit claim that a successfully completed child result/diff satisfies the Fleet goal and is correct, complete, non-regressive and in scope.
- Ordinary reporting path: the worker session exits and returns its own result/output to Fleet, which would otherwise settle the child as succeeded.
- Complementary access path: a separately spawned verifier receives the goal and the worker branch, independently inspects `git diff`/output and returns a structured verdict.
- Independence boundary: verifier is a fresh child/session, is placed in a read-only stance, and its prompt is explicitly blind to who authored the work and instructs it not to assume correctness.
- Who acts on findings: first-party Fleet verdict routing records the result and either closes success, launches additional independent review, or injects reject reasons into the next worker round and redispatches the worker within configured bounds.

## S4 — Outside-and-then adaptation

- State: —
- Function: no installation-level S4 path is established from the reviewed standard distribution.
- Disturbance / variety regulated: the repository contains session intelligence, pattern/graph derivation, anomaly detection, friction logging and an assisted self-improvement policy, but the inspected paths do not establish the required external-and-future sensing loop that generates an adaptation option and returns it into installation capability/current control.
- Decisive decision or feedback right: not established at the installation recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Pattern Intelligence, derived knowledge graph, model-assisted per-session analysis/recommendations, friction log, improvement backlog, retrospective cadence and `learning-policy.yml` proposal/apply permissions.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: historical/session-derived analysis and internal friction-driven improvement can support learning, but the reviewed standard path does not show a qualifying S4 organizational function to classify.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`packages/harness/AGENTS.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/packages/harness/AGENTS.md); [`packages/harness/.harness/learning-policy.yml`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/packages/harness/.harness/learning-policy.yml); [`apps/cockpit/server/intelligence/analyzer.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/intelligence/analyzer.js).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: a downstream organization could use Mission Control's history/intelligence as input to S4, but that would require evidence of the missing sensing/adaptation closure at that downstream boundary.

### Absence scope

- Surfaces inspected: Pattern Intelligence, Knowledge Graph, anomaly/self-monitoring features, per-session intelligence analysis, friction/improvement records, `learning-policy.yml`, model tiers, retrospective cadence and self-improvement instructions.
- Plausible first-party paths checked: recurring internal command/workflow patterns; session recommendations; meta-session detection; automatic friction logging; automatically proposed safe documentation/process changes; retrospective triggers.
- Why no material first-party path remains: these paths derive from internal runtime/session history or current operational friction. No reviewed standard-distribution path clearly distinguishes external environmental change, projects a future implication, forms a concrete adaptation option from that external/prospective evidence, and closes it back into installation capability or S3.

## S5 — Identity / ultimate policy

- State: —
- Function: no installation-level S5 identity or ultimate-policy closure is established from the reviewed standard distribution.
- Disturbance / variety regulated: Mission Control has explicit risk policies, approval requirements, mission readiness, caps, kill-switch controls and protected harness-policy changes, but these govern operational safety/current authority rather than deciding what the organization ultimately is or resolving competing metasystem demands at the identity level.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: not established.
- Supporting / enforcement mechanisms: risk-typed human approvals, append-only audit, danger-zone rules, `human-approval-policy.yml`, protected learning-policy categories, mission readiness and emergency stop/reset controls.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: a human is deliberately the approver for consequential operations and protected policy changes, but generic human approval is not automatically S5; no reviewed path establishes identity-level ultimate authority and its return to operation.
- Evidence: [`README.md`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/README.md); [`packages/harness/.harness/human-approval-policy.yml`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/packages/harness/.harness/human-approval-policy.yml); [`packages/harness/.harness/learning-policy.yml`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/packages/harness/.harness/learning-policy.yml); [`apps/cockpit/server/fleet/fleet-runner.js`](https://github.com/CosmonautJones/mission-control/blob/9337744f7ec940234ecdc2936fa426d70598d26d/apps/cockpit/server/fleet/fleet-runner.js).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the result does not claim Mission Control lacks policy. It distinguishes operational/risk policy and parent approval from the narrower S5 function defined by the Profile.

### Absence scope

- Surfaces inspected: governance README, approval risk types and audit semantics, human approval policy, danger-zone controls, harness self-improvement protection rules, mission draft/ready/build lifecycle, Fleet policy/budgets/kill-switch and synthesis.
- Plausible first-party paths checked: human approval over destructive/security/data/business actions; protected changes to safety/testing/deployment policy; emergency stop/reset; goal selection; mission readiness; reviewer acceptance.
- Why no material first-party path remains: these surfaces decide whether particular operational actions or policy edits are allowed, but the reviewed installation does not expose a concrete identity/ultimate-policy issue with a designated ultimate authority whose resolution is returned into the organization as S5 closure.

## Summary

| Function | State | Assessment |
| --- | --- | --- |
| S1 | A | First-party Fleet/workflow paths launch external autonomous coding workers that own task-local reasoning inside bounded worktrees and rails. |
| S2 | — | Parallel workers are isolated and resource-bounded, but no complete sibling-disturbance → attenuation → feedback witness is established. |
| S3 | C(P) | The installation exposes whole-system current state plus approval/steer/cancel/emergency controls for downstream composition, with the human operator closing the standard parent-governed mode. |
| S3* | A | Fresh authorship-blind autonomous reviewer sessions independently challenge worker output and return reject reasons through bounded redispatch. |
| S4 | — | History/pattern/self-improvement surfaces do not establish external prospective sensing and adaptation closure. |
| S5 | — | Human risk approvals and safety policy do not establish identity/ultimate-policy closure. |

The resulting standalone signature is **`A — C(P) A — —`**.