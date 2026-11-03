---
harness_id: swarmos
project_name: SwarmOS
repository: https://github.com/supernovae/SwarmOS
review_ref: c85010787b001981beb84e60502c1eaca3c6f812
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# SwarmOS

## Review boundary

- System in focus: one first-party SwarmOS installation, its issue-bound WorkUnit, Git/CAS coordination state, worktree/checkpoint execution, managed planner/developer/tester/reviewer roles and policy/validation gates at the frozen revision.
- Purpose and identity: coordinate substantive software changes by multiple authenticated coding-agent harnesses under durable repository work contracts and guarded artifact/PR publication.
- Relevant environment: a GitHub repository, issue approvals, concurrent workers, source/test feedback, failing validation, lease expiry, human maintainer choices and external Claude Code/Codex/OpenCode/OhMyPi executors.
- Standard-distribution boundary: shipped Go CLI, `internal/workflow`, `internal/agent`, `internal/lease`, `internal/coordination`, `internal/workspace`, `internal/validation`, bundled role prompts and supported native/isolated execution adapters.
- Credited operating / distribution surfaces: an approved WorkUnit run with SwarmOS-managed model-driven planner/developer/tester/reviewer role invocation; fenced Git state; trusted-base validation; optional agent review gate; automatic repair within a recorded budget.
- Adjacent first-party surfaces excluded from ownership: SwarmOS repository CI/development tests, roadmap, release governance, experimental/future provider integrations, the model providers and unrelated internal agent functions of launched CLI products.
- First-party operating / deployment modes considered: standard managed issue work, optional `agent`/`human`/`none` plan gates, separate tester/validator and bounded repair, local or GitHub-ledger backend, isolated versus explicit trusted-local execution, and PR continuation.
- Recursion level: one SwarmOS-managed repository work organization with distinct task-producing worker instances; GitHub and the coding-agent providers are external dependencies.
- Reviewed revision: `c85010787b001981beb84e60502c1eaca3c6f812`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

SwarmOS compiles an approved GitHub Issue into a WorkUnit with constraints, acceptance criteria and gate mode, records its approved base/policy digest, and acquires a fenced Git-ref claim before launching managed coding-agent roles in an isolated worktree. Roles work against bounded snapshots and deliver plan, implementation, reviewer or validation artifacts. A separate tester model runs acceptance checks against the candidate; a coordinator enforces trusted baseline checks and can return failures for bounded developer repair. CAS leases and checkpoint lineage prevent stale workers from overwriting active issue state. The CLI can submit the resulting PR, but human/maintainer approval gates remain distinct from any autonomous coding decision.

Pinned primary evidence:

- [Architecture: CAS claims, worktrees, trusted-base validation and isolation](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/docs/ARCHITECTURE.md)
- [Workflow roles, handoffs, validation and repair](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/docs/WORKFLOWS.md)
- [WorkUnit and gate configuration](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/contract/types.go)
- [CAS state store and checkpoint reconciliation](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/coordination/store.go)
- [Agent reviewer gate and verdict handling](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/workflow/execute_review.go)
- [Snapshot-isolated reviewer and output-only return](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/agent/review.go)
- [Tester, independent check and bounded repair return](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/workflow/execute_validation.go)
- [Developer phase and artifact handoff](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/internal/workflow/execute_implementation.go)
- [Release-level supported limits and qualifications](https://github.com/supernovae/SwarmOS/blob/c85010787b001981beb84e60502c1eaca3c6f812/docs/native-qualification.md)

## Operational model

An approved work contract and configured agent roles become the bounded operating context. Managed model-driven workers decide plan/code/test actions, while first-party code owns task custody, protected paths, plan approval requirements, lease/claim limits, checkpoint and validation transactions. The configured reviewer/tester path supplies a separate challenge to ordinary plan/implementation reports with an explicit return to the worker for correction; the control machinery enforces this path without itself making the agent's audit judgment. A roadmap or changes to the SwarmOS tool do not automatically constitute a runtime S4 adaptation function.

## S1 — Operations

- State: A
- Function: autonomously interpret approved task acceptance criteria and produce/revise code, plans, tests and evidence for an owned WorkUnit.
- Disturbance / variety regulated: unpredictable repository content, technical uncertainty, tool results, compile/test failures and defects within the approved task.
- Decisive decision or feedback right: choose substantive plan, implementation, and corrective tool/code steps in response to observed workspace/test feedback.
- Decision owner: the configured managed model-driven planner/developer/tester agent in a first-party launched role, not the Git queue or lease manager.
- Supporting / enforcement mechanisms: role prompts, task bundle, native CLI adapters, isolated worktree, checkpoints, approved-base policy, claim fencing and report import.
- Closure path: issue contract and approved base → launched role receives source/task context → model-driven work and tool actions → tests/environment feedback → changed artifact and implementation handoff or repair.
- Boundary reachability: `internal/workflow` invokes configured role runners for approved WorkUnits in the shipped `swarm issue work` path, with native Codex and other qualified adapters; no repository-development-only actor is required.
- Why this is / is not agent-owned: after removing the model-driven worker, CAS/validation/PR services still enforce custody but cannot choose the task-specific implementation; only supported managed workers supply that discretion.
- Evidence: pinned `docs/ARCHITECTURE.md`, `docs/WORKFLOWS.md`, `internal/workflow/execute_implementation.go`, `internal/workflow/execute_validation.go`.
- Basis: explicit + structural.
- Confidence: high for reachability and role ownership, not for success on every provider/runtime combination.
- Caveats: individual provider model/tool loops are external dependencies; their unrelated S2–S5 mechanisms are excluded. Some platform/provider qualification is explicitly pending.

## S2 — Coordination

- State: C
- Function: attenuate interference between separate workers claiming or publishing the same issue state and return the conflict result to later worker behavior.
- Disturbance / variety regulated: simultaneous worker claims, stale renewal/checkpoint publication, and one worker overwriting another's accepted state.
- Decisive decision or feedback right: accept exactly one current claim under a fencing token, reject an old claimant, and cancel or prevent publication from the superseded attempt.
- Decision owner: constructor-defined CAS/lease policy executed by SwarmOS rather than an autonomous coordination agent choosing its own exception policy.
- Supporting / enforcement mechanisms: Git compare-and-swap refs, `claim_id`, TTL, heartbeat, joint issue/checkpoint update, worktree isolation.
- Closure path: rival claims or changed Git state → one fenced CAS succeeds and the other fails → stale worker is canceled/refused and must reacquire or hand off before subsequent work/publishing.
- Boundary reachability: the claim/store implementation is mandatory for managed issue attempts in supported local/GitHub ledger modes, and subsequent artifact publication revalidates its claim.
- Why this is / is not agent-owned: the inter-worker conflict is real and transactionally closed, but the decisive resolution rule is prewritten, so coordination is constructor-controlled rather than an S2 agent discretion.
- Distinct S1 units: separate concurrent managed coding-agent worker attempts/instances assigned against a shared issue/repository work organization.
- Inter-S1 disturbance: duplicate claim/overwrite or a stale worker publishing a checkpoint after another acquired the issue.
- Attenuating coordination relation: unique fenced owner and CAS replacement rule, with cancellation/refusal on lease loss.
- Feedback into subsequent S1 behaviour: rejected/stale worker cannot continue or publish; subsequent work must use the current claim/checkpoint or be stopped.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code explicitly prevents a concrete clash of otherwise independent operational workers and returns the prevention to their later execution capability, not merely storing a task list.
- Evidence: pinned `docs/ARCHITECTURE.md`, `internal/coordination/store.go`, `internal/coordination/revoke.go`, `internal/workflow/execute_run.go`.
- Basis: structural.
- Confidence: high.
- Caveats: this is a narrow collision-attenuation path, not proof of a broad adaptive peer-negotiation metasystem.

## S3 — Inside-and-now control

- State: C
- Function: regulate present task commitments, release/stop conditions and required verification for the approved WorkUnit across planner, developer, tester and publication stages.
- Disturbance / variety regulated: unapproved plan changes, stale workers, overrun repair loops, untrusted candidate changes to validation policy, and reported completion before required checks pass.
- Decisive decision or feedback right: withhold implementation or submit readiness when approved digests/checks/claim evidence disagree, reserve bounded repairs, and permit handoff/continuation only after policy-conforming current state.
- Decision owner: constructor policy and authorized human WorkUnit/gate settings; managed agent roles produce artifacts but do not override approval, claim, or baseline validation predicates.
- Supporting / enforcement mechanisms: WorkUnit digest and approved base SHA, phase machine, lease manager, protected-path checker, trusted-base validation specification and repair attempt budget.
- Closure path: whole-issue current phase/artifact/claim/check results → deterministic admit, pause, retry, reject or finish transition → subsequent worker role and PR stage follows that decision.
- Boundary reachability: `internal/workflow/execute_run.go`, `execute_validation.go` and `internal/pr/service.go` govern every standard managed issue execution and publication path.
- Why this is / is not agent-owned: the present-work control function is real but its decisive stage/authority rules are authored and enforced by SwarmOS policy; a model cannot autonomously waive them.
- Whole-system current view: approved work objective, policy/base digests, lease/owner, phase, reports, checkpoint, required-check outcomes and repair budget for one WorkUnit.
- Current-control decision scope: work admission, stage continuation, checkpoint trust, bounded retry, and readiness for an explicit submission; not a universal multi-project portfolio budget.
- Evidence: pinned `internal/contract/types.go`, `internal/workflow/execute_run.go`, `internal/workflow/execute_validation.go`, `internal/pr/service.go`, `docs/ARCHITECTURE.md`.
- Basis: structural.
- Confidence: medium-high for a bounded issue-level S3 constructor path.
- Caveats: most approval and policy choices are parent or developer-owned; S3=C does not promote static enforcement to autonomous S3=A.

## S3* — Complementary audit

- State: A
- Function: challenge an implementer/plan author's own report against independent source/acceptance evidence and return findings into corrective work before continuation.
- Disturbance / variety regulated: self-reported correctness, incomplete acceptance coverage or a plausible implementation passing only its author's own checks.
- Decisive decision or feedback right: a separately invoked reviewer/tester model assesses an exact plan/candidate against independent artifact/source/check evidence and produces change requests or failure findings.
- Decision owner: the configured distinct reviewer/tester model-driven role; deterministic parsing, validation enforcement, and report import do not own the model's challenge judgment.
- Supporting / enforcement mechanisms: snapshot-isolated read-only review, output-only `REVIEW.md`, separate `VALIDATION.md`, trusted-base checks, role/provenance separation, bounded repair routing.
- Closure path: author plan or candidate + self-report → separate reviewer/tester inspects source/acceptance and records findings → verdict/failing check blocks continuation → developer corrects candidate and the relevant check repeats.
- Boundary reachability: the shipped `agent` review gate runs a configured reviewer in an isolated snapshot, while the standard validation phase invokes a separate tester and routes failed acceptance/check outcomes into bounded developer repair.
- Why this is / is not agent-owned: an independently invoked role receives the actual artifact and makes the substantive challenge, whereas SwarmOS's gate merely enforces its outcome. The positive claim is limited to modes with a distinct configured reviewer/tester.
- Claim being audited: that a proposed plan or implemented candidate satisfies the approved scope/acceptance and can safely progress.
- Ordinary reporting path: planner's plan/test plan or developer's implementation report and claimed commands/results.
- Complementary access path: read-only isolated review of source/plan and separate tester's direct acceptance/required-check execution rather than only trusting the prior handoff.
- Independence boundary: reviewer is isolated from modification of the author's worktree, and the tester is a separately invoked role with acceptance checks; the model's actual provider can be configured, so independence is actor/process and evidence-path, not automatically different model vendors.
- Who acts on findings: SwarmOS stops promotion and returns failed validation or requested changes to the developer/plan path for bounded correction and recheck.
- Evidence: pinned `internal/agent/review.go`, `internal/workflow/execute_review.go`, `internal/workflow/execute_validation.go`, `docs/WORKFLOWS.md`.
- Basis: explicit + structural.
- Confidence: medium; independence is deployment/role-configuration-sensitive.
- Caveats: static required checks alone are routine validation, not the S3* witness. Human-only review is not counted as autonomous S3*; the cited distinct model-driven reviewer/tester mode is required.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped first-party future-capability adaptation loop over the SwarmOS work organization was established.
- Disturbance / variety regulated: issue backlog changes, new requests and tool/runtime upgrades are operational inputs, but not a demonstrated environment-model → prospective adaptation-option → changed capability loop.
- Decisive decision or feedback right: users author new WorkUnits, repository maintainers choose product changes, and current-work agents choose implementation within a given contract.
- Decision owner: external user/maintainer for future capability and present S1 roles for bounded tasks; no separately closed SwarmOS S4 authority.
- Supporting / enforcement mechanisms: issue triage, backlog scan, role guidance, diagnostic reports, roadmap and release process.
- Closure path: incoming issue or planned product change enters an ordinary approved WorkUnit; no first-party S4 actor is shown returning a prospective environment-derived option into durable operating capability.
- Why this is / is not agent-owned: sensing a new issue, repairing a failing current PR and storing lessons are not by themselves outside-and-then capability adaptation.
- Evidence: pinned `docs/WORKFLOWS.md`, `docs/ARCHITECTURE.md`, `ROADMAP.md`, `internal/workflow/backlog_lanes.go`.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: a parent organization using SwarmOS could run an S4 practice outside this distribution; it is not imported here.

### Absence scope

- Surfaces inspected: runtime/role architecture, backlog/issue triage, workflow lessons, reporter, roadmap, checked worktree/PR repair and repository release material.
- Plausible first-party paths checked: backlog scanning as environmental sensing, stored lessons as adaptation, agent-driven code changes as future product change, roadmap/release as parent S4.
- Why no material first-party path remains: cited shipped paths process current approved work or record/recommend material; no supported SwarmOS-wide future-capability adaptation decision plus feedback into a changed subsequent harness operating mode is demonstrated.

## S5 — Policy and identity

- State: —
- Function: no internally or parent-closed ultimate organizational identity/policy decision loop is established for a SwarmOS installation.
- Disturbance / variety regulated: task constraints, protected paths, authentication and repository identity are set from outside as fixed policy/permissions, not deliberated by a first-party ultimate-policy authority.
- Decisive decision or feedback right: maintainer authorizes a task/plan and repository policy, but no shipped runtime path adjudicates a constitutional identity question and returns that ruling to govern the organization.
- Decision owner: external repository maintainer/provider authorization for configuration and approvals; ordinary task actors operate inside those constraints.
- Supporting / enforcement mechanisms: immutable approval bindings, permission checks, WorkUnit policy, human gate, sandbox rules and versioned base SHA.
- Closure path: configured policy is enforced for work; no identity/policy dispute → legitimate S5 adjudication → returned authoritative new identity/ultimate-policy state is evidenced.
- Why this is / is not agent-owned: human approvals and static permission rules are concrete authority constraints, but they do not close S5 by themselves.
- Evidence: pinned `internal/contract/types.go`, `docs/project.md`, `docs/ARCHITECTURE.md`, `internal/lease/`.
- Basis: bounded absence.
- Confidence: high.
- Caveats: a larger OpenSiro- or company-like parent organization may possess S5 externally; no such authority is credited to the shipped SwarmOS installation.

### Absence scope

- Surfaces inspected: WorkUnit approval, operator permissions, `.swarm` policy, human review gates, role prompts, maintainer controls and setup docs.
- Plausible first-party paths checked: human approval as parent S5, policy-file changes as identity decisions, repo access/ruleset as legitimate ultimate authority and model-defined mission changes.
- Why no material first-party path remains: these are configuration, permission or present task-release decisions without a supported function-specific ultimate identity/policy matter reaching an authority and returning to subsequent runtime operation.

## Distributed OSS parent arrangement

Independent users run the SwarmOS binary against their own repositories. A local maintainer can approve one WorkUnit or change a project policy; this does not establish one shared organization-level parent S5 for all deployments or an S3/S4 parent-return mode in the assessed distribution.

## Recursion

One installation/work portfolio is the assessed recursion. Managed model-driven workers serve as operational S1 units. Separate independent review/test roles and constructor-governed current/peer control supply additional functions; provider runtimes and GitHub infrastructure are suppliers rather than fully assessed nested viable systems.

## Variety and escalation

WorkUnit constraints and approvals attenuate task ambiguity; managed model/tool feedback handles local implementation variety; fenced CAS absorbs cross-worker collisions; independent review and acceptance evidence challenge self-report; whole-issue phase/repair gates contain unsafe continuation. Lease loss, verification failures and rejected reports return to the worker/maintainer at the bounded level. An alert or failed status does not itself confer S3/S4/S5 ownership.

## Evidence gaps

- Frozen repository and first-party tests/docs were inspected; no authenticated hosted-provider agent run or external GitHub work submission was performed for this assessment.
- The S3* positive mode requires a separately configured reviewer/tester actor with genuinely distinct evidence access; a single model impersonating both roles without credible independence would require a narrower result.
- The S2 finding is limited to the well-evidenced rival-claim interference path; generic task queueing and role handoff were not treated as S2.
- The S3 constructor result is issue-level current control. No independent evidence was found for autonomous global portfolio resource bargaining or ultimate policy change.

## Assessment summary

Proposed included at the shipped managed-worker boundary: **A · C · C · A · — · —**. Coding-agent discretion supplies S1; constructor-defined CAS lease conflict attenuation and current stage-control support S2/S3; separate model-driven review/tester access and corrective return support S3*. Current issue handling, roadmap, static governance and human approval do not by themselves establish S4/S5.
