---
harness_id: nipus-harness
project_name: nipus-harness
repository: https://github.com/cUDGk/nipus-harness
review_ref: 0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# nipus-harness

## Review boundary

- System in focus: the first-party Windows task-worker composition and its shared host/workspace coordination across runs.
- Purpose and identity: complete a caller-declared goal with tool-backed work until explicit acceptance/scope conditions pass, or return an evidenced stop state.
- Relevant environment: workspace source, acceptance commands, host jobs/Unity contention, model/account services, optional web/MCP tools and caller task constraints.
- Standard-distribution boundary: src/cli.ts, loop/session/tools/delegate/gate/host/rules/commands and boxed helpers; Pi coding-agent provides the model/session substrate, not the unexamined ownership verdict.
- Credited operating / distribution surfaces: the CLI-installed Pi session with owned worker prompt, inspect/run/edit/finish tools, finish-validation continuation loop, named host-job queue and cross-run workspace locks.
- Adjacent first-party surfaces excluded from ownership: scripted model test servers, acceptance fixtures and claimed token/benchmark results. External Codex is used for boxing/quota support; its coding operation is not borrowed.
- First-party operating / deployment modes considered: Windows boxed default, explicitly unboxed task mode, optional declared child roles, host jobs, web/MCP and stop/resume. Non-Windows execution is outside the supported product.
- Recursion level: task-worker cells on one host under the first-party lock domain; not the external caller's full organization.
- Reviewed revision: `0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The TypeScript CLI validates task JSON, obtains an exclusive real workspace lease, installs request/tool/model/quota gates and creates a Pi-backed session with repository-owned tools/prompt. loop.ts waits for the actor to settle, inspects finish, runs actual acceptance commands or host jobs, verifies cited path/line and web evidence, checks the diff and returns failures to the worker until success, blocked/needs_judgment or budget/continuation stop. Files must remain the same through acceptance. Runtime transitions do not choose the coding solution.

host.ts implements atomic owner-aware locks, stale-owner/orphan cleanup, workspace/subfolder collision exclusion and named host-job waits. CLI acquires/releases the workspace lock; hostJob serializes expensive declared processes (including Unity project contention). delegate.ts creates a separate Pi session with an explicitly declared tool/model/quota profile and returns finish/results. gate.ts accounts for usage and enforces immutable task profiles. commands.ts implements ledger status, selective process stop and resume repair. These are concrete first-party compositions atop libraries, not claims about library internals.

## Operational model

The worker chooses how to meet the supplied goal using owned file/command tools and returned failure evidence. The caller determines goal, admissible tools, scope, acceptance and quotas. Distinct simultaneous worker runs have independent outcomes but may contend for a workspace or named host process; dedicated locking paths specifically regulate that interference. Acceptance validation is a normal completion check, not independently judged audit.

## S1 — Operations

- State: A
- Function: complete bounded coding/research work and correct it against actual tool/acceptance feedback.
- Disturbance / variety regulated: unknown source, failed checks, scope violations, incomplete answers and transient model/tool errors.
- Decisive decision or feedback right: choose inspections, edits, commands and repair strategy; declare finish or an evidenced blocker.
- Decision owner: model worker instantiated by the first-party prompt/tool/continuation composition; optional declared child owns its bounded local work.
- Supporting / enforcement mechanisms: Pi session/model library, owned tools, boxing, request gates, acceptance runner, result/evidence/diff validation, persisted sessions and ledger.
- Closure path: goal → tool-backed worker → finish → real checks/evidence/scope → reasons returned to same worker → revised work or honest terminal result.
- Boundary reachability: CLI createSession wires the owned customTools and prompt, then directly invokes runLoop; dependency execution does not replace this composition.
- Why this is / is not agent-owned: removing the worker leaves checks/locks but no task-specific implementation or correction decisions.
- Evidence: [src/cli.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/cli.ts); [src/loop.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/loop.ts); [src/tools.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/tools.ts); [src/prompt.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/prompt.ts); [src/session.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/session.ts); [src/delegate.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/delegate.ts).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Source reachability only; Windows/model prerequisites were not exercised. A mock provider is not credited as autonomous.

## S2 — Coordination

- State: C
- Function: prevent destructive overlap among independent task-worker runs sharing folders and host jobs.
- Distinct S1 units: separate CLI task/worker runs with their own goal, session and result on the same host.
- Inter-S1 disturbance: concurrent writers in an identical or nested workspace undo each other's edits; overlapping Unity/heavy processes contend for an exclusive host resource; crashed owners may leave orphan processes.
- Attenuating coordination relation: CLI lockWorkspace uses a short atomic table lock plus real-path exact/parent-child checks before acquiring a writer lock; hostJob waits on named owner-aware locks, detects a busy Unity project and reaps stale-owner processes before reuse.
- Feedback into subsequent S1 behaviour: workspace_busy prevents a second writer from starting; busy host jobs queue until safe or return busy at timeout into worker/acceptance feedback. The lock is released after the owning task/process ends.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relations identify actual workspace/resource collision domains and modify whether/when another independent operational run may execute.
- Disturbance / variety regulated: cross-run edit interference and exclusive host-process conflict.
- Decisive decision or feedback right: admit, defer or reject conflicting runs under the fixed collision policy.
- Decision owner: developer-authored lock/admission policy and caller-declared host lock identity; autonomous organizational coordination discretion is not composed.
- Supporting / enforcement mechanisms: exclusive-create lock files, owner PID/start-time checks, workspace table, queue timeout, orphan cleanup and returned status.
- Closure path: another active owner's collision → refusal/wait → subsequent run starts only after safe release or receives busy evidence.
- Boundary reachability: src/cli.ts invokes lockWorkspace before work and releases it in finally; src/host.ts hostJob is reachable through declared tools and acceptance jobs.
- Why this is / is not agent-owned: specific coordination machinery is shipped, but its response is predetermined rather than chosen/revised by an autonomous coordinator.
- Evidence: [src/host.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/host.ts); [src/cli.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/cli.ts); [src/tools.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/tools.ts); [tests/parallel.test.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/tests/parallel.test.ts); [README.md](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/README.md).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: C does not claim coordination across hosts/installations or semantic negotiation. Tests were inspected as witnesses, not executed here.

## S3 — Inside-and-now control

- State: —
- Function: whole-system inside-and-now control
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/gate.ts`, `src/commands.ts`, `src/cli.ts`, `src/delegate.ts`
- Closure path: Per-role/run quotas, account-limit enforcement, static tool/model profiles and host locks bound tasks. status --active exposes state and stop/resume provides local lifecycle intervention, but no shipped whole-system commitment/resource decision with a distinct supervisory owner and return contract is established. Generic caller control is not automatically parent S3.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/gate.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/gate.ts); [src/commands.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/commands.ts); [src/cli.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/cli.ts); [src/delegate.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/delegate.ts).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/gate.ts, src/commands.ts, src/cli.ts, src/delegate.ts, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Per-role/run quotas, account-limit enforcement, static tool/model profiles and host locks bound tasks. status --active exposes state and stop/resume provides local lifecycle intervention, but no shipped whole-system commitment/resource decision with a distinct supervisory owner and return contract is established. Generic caller control is not automatically parent S3.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes whole-system inside-and-now control at this boundary.

## S3* — Complementary audit

- State: —
- Function: complementary independent audit
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/loop.ts`, `src/rules.ts`, `src/delegate.ts`, `tests/review.test.ts`
- Closure path: runLoop checks acceptance, evidence and diffs as the normal completion path and sends failures back to the same worker. Suspect violations and needs_judgment do not instantiate an independent source auditor. Arbitrary declared roles can be composed into review but no audit-specific independent claim/judgment/corrective loop is supplied.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/loop.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/loop.ts); [src/rules.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/rules.ts); [src/delegate.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/delegate.ts); [tests/review.test.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/tests/review.test.ts).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/loop.ts, src/rules.ts, src/delegate.ts, tests/review.test.ts, README and supported CLI/operator wiring.
- Plausible first-party paths checked: runLoop checks acceptance, evidence and diffs as the normal completion path and sends failures back to the same worker. Suspect violations and needs_judgment do not instantiate an independent source auditor. Arbitrary declared roles can be composed into review but no audit-specific independent claim/judgment/corrective loop is supplied.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes complementary independent audit at this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: external and prospective capability adaptation
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/cli.ts`, `src/session.ts`, `src/loop.ts`, `src/prompt.ts`
- Closure path: Web retrieval serves the current research goal; session persistence, retry and resume retain ongoing work. No supported outside-and-then option-development/adoption path changes the worker's future repertoire; task/model configuration edits are inputs, not a closed parent adaptation function.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/cli.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/cli.ts); [src/session.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/session.ts); [src/loop.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/loop.ts); [src/prompt.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/prompt.ts).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/cli.ts, src/session.ts, src/loop.ts, src/prompt.ts, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Web retrieval serves the current research goal; session persistence, retry and resume retain ongoing work. No supported outside-and-then option-development/adoption path changes the worker's future repertoire; task/model configuration edits are inputs, not a closed parent adaptation function.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes external and prospective capability adaptation at this boundary.

## S5 — Policy and identity

- State: —
- Function: identity and ultimate-policy closure
- Disturbance / variety regulated: candidate variety and checked alternatives are recorded below.
- Decisive decision or feedback right: no qualifying function-specific path established.
- Decision owner: ordinary operational agent, developer and caller rights do not establish this distinct function.
- Supporting / enforcement mechanisms: `src/prompt.ts`, `src/cli.ts`, `src/gate.ts`, `src/loop.ts`
- Closure path: Fixed goals, task scope, forbidden terms, model/tool gates and clean-room declarations constrain operational execution. A blocked/needs_judgment result requests task-owner judgment, but no explicit ultimate identity/policy matter and authoritative return into standing governance is supplied.
- Why this is / is not agent-owned: positive and supported parent alternatives were tested before this bounded absence conclusion.
- Evidence: [src/prompt.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/prompt.ts); [src/cli.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/cli.ts); [src/gate.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/gate.ts); [src/loop.ts](https://github.com/cUDGk/nipus-harness/blob/0c0349ee7f37d9bc0334c1d5ea7802c49f8e950b/src/loop.ts).
- Basis: structural.
- Confidence: high for source wiring; not an empirical outcome claim.
- Caveats: Bounded to the reviewed supported distribution; custom future extensions are not evidence of a shipped path.

### Absence scope

- Surfaces inspected: src/prompt.ts, src/cli.ts, src/gate.ts, src/loop.ts, README and supported CLI/operator wiring.
- Plausible first-party paths checked: Fixed goals, task scope, forbidden terms, model/tool gates and clean-room declarations constrain operational execution. A blocked/needs_judgment result requests task-owner judgment, but no explicit ultimate identity/policy matter and authoritative return into standing governance is supplied.
- Why no material first-party path remains: The inspected mechanisms implement ordinary operation or support; none closes identity and ultimate-policy closure at this boundary.

## Distributed OSS parent arrangement

The caller owns task constraints. That is not evidence of project/organization parent S3/S4/S5 or delegated external maintainer authority.

## Self-hosted and non-human modes

Boxed/unboxed and optional roles/web/MCP alter tool reachability under task declarations. No alternative function-specific parent mode is established.

## Recursion

A delegated role is a nested work cell, not a demonstrated recursive viable organization.

## Variety and escalation

Acceptance/diff failures, repeated suspects, no progress and budgets become explicit result/reason states. These preserve local operational feedback; an error status alone is not an algedonic channel.

## Evidence gaps

Static source assessment at the frozen ref. Native tests require Node and supported Windows PowerShell/Codex boxing; those are unavailable here. No native suite, account/provider run, quota measurement or reported efficiency result was reproduced.

