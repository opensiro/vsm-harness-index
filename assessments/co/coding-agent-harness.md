---
harness_id: coding-agent-harness
project_name: Coding Agent Harness
repository: https://github.com/Breno-J-Oliveira/coding_agent_harness
review_ref: 7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# Coding Agent Harness

## Review boundary

- System in focus: One project-local Coding Agent Harness setup and its associated persistent delivery board.
- Purpose and identity: Convert a project objective into verified engineering increments while retaining human acceptance and publication decisions.
- Relevant environment: Project source/worktree, developer/operator, Codex or Claude Code host, trusted verifier and external skill distribution.
- Standard-distribution boundary: First-party board runner, bootstrap and installed workflow skills. The host provides model turns and tool transport.
- Credited operating / distribution surfaces: [Board](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Verification controller](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/board_runtime.py) · [Bootstrap](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/bootstrap.py) · [Delivery workflow](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/engineering-delivery/SKILL.md)
- Adjacent first-party surfaces excluded from ownership: Upstream repository release machinery, examples, optional third-party skill implementations, and external host governance.
- First-party operating / deployment modes considered: Codex CLI board run/advance and the documented IDE/interactive record-and-accept path.
- Recursion level: A project delivery workflow and its board of bounded engineering tasks.
- Reviewed revision: 7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Bootstrap installs project-local workflow skills while preserving existing files. The board stores tasks, dependencies, acceptance criteria, outcomes and receipts outside the project. A runner launches a bounded Codex turn, converts its completed structured report into review or failure, and optionally invokes an operator-supplied verifier before proceeding. Interactive host turns re-enter through record and owner acceptance.

## Operational model

Each S1 instance is a model turn performing an authorized project task. The board and runtime own serialization and gates. The owner can reach current work through board state and release held work through acceptance, task changes or retry. Review, trusted verification and external skill intake are separate decisions.

## S1 — Operations

- State: A
- Function: Perform a delegated engineering task in the project under stated acceptance criteria.
- Disturbance / variety regulated: Different project states and failed tool actions require task-local judgment.
- Decisive decision or feedback right: Choose code and validation actions for the current work item and decide whether results satisfy the supplied criteria.
- Decision owner: Coding-agent model instantiated by the shipped runner or the documented interactive host.
- Supporting / enforcement mechanisms: Board-to-prompt compilation, workspace write policy, log and JSON outcome parser.
- Closure path: The host model receives tool outcomes; its structured report returns to the board and determines whether the work enters review or failure.
- Why this is / is not agent-owned: The launch path supplies an actual task-adaptive model turn; the Python runner enforces state and scope.
- Boundary reachability: Normal board run reaches the host turn through the first-party invocation, and the installed interactive workflow feeds back into the same board.
- Evidence: [Board execution and outcome](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Installable workflow](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/engineering-delivery/SKILL.md) · [Operating guide](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/docs/36-engineering-os.md)
- Basis: structural
- Confidence: high
- Caveats: The host provides inference and tool machinery; no host test or provider call was performed here.

## S2 — Coordination

- State: —
- Function: Regulate interference among active peer S1 tasks.
- Disturbance / variety regulated: Work items can share a project and depend on each other.
- Decisive decision or feedback right: No dedicated peer-interaction decision right is supplied at the board boundary.
- Decision owner: The board deterministically serializes work. Profiles are callable roles on the host.
- Supporting / enforcement mechanisms: Board locking, dependency edges and one ready item at a time.
- Closure path: A terminal acceptance can unlock a later sequential item.
- Why this is / is not agent-owned: Role descriptions and sequential gates do not establish an actor or composition path that attenuates a concrete ongoing sibling interaction.
- Evidence: [Ready and lock rules](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Delivery guidance](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/engineering-delivery/SKILL.md) · [Integration profile](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/agents/integration_reviewer.toml)
- Basis: structural
- Confidence: medium
- Caveats: External host-specific coordination, if configured separately, is outside this boundary.

### Absence scope

- Surfaces inspected: Board runner, dependency configuration and shipped interactive roles.
- Plausible first-party paths checked: Board lock/serialization, one work item per launch, host expert guidance and integration review.
- Why no material first-party path remains: The supported queue deliberately serializes runnable tasks. Role guidance does not supply a distinct enforceable peer-conflict decision feedback path in the first-party distribution.

## S3 — Inside-and-now control

- State: P
- Function: Decide whether current project commitments can advance and which stalled work to re-open.
- Disturbance / variety regulated: A review, failure or incomplete acceptance can hold up the whole active board.
- Decisive decision or feedback right: Given the project-wide board, choose whether to accept evidence, retry a task or add current work with dependencies.
- Decision owner: Project owner/operator in the managed-board mode.
- Supporting / enforcement mechanisms: Whole-board status, mutating commands, evidence hashing, gate enforcement and budgets.
- Closure path: Owner acceptance marks a task done and releases its downstream dependencies; retry returns selected work to pending.
- Why this is / is not agent-owned: The runner returns evidence and applies fixed limits. The operator can interpret and change the current work portfolio.
- Boundary reachability: The normal board is read through status, then the same CLI persists accept/retry/add and the next run reads that state.
- Whole-system current view: One project board across pending, failed, in-review and accepted commitments and their dependencies.
- Current-control decision scope: Operator changes live commitments by accepting, retrying or adding work across the board.
- Evidence: [Board commands and gates](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Board operator flow](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/docs/36-engineering-os.md) · [Delivery release rules](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/engineering-delivery/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: The optional verifier can advance authorized items through its predicate. It does not exercise general cross-board supervisory discretion.

## S3* — Complementary audit

- State: C
- Function: Corroborate an agent's ready claim before it releases more work.
- Disturbance / variety regulated: A successful host exit and ready report can omit missing acceptance evidence.
- Decisive decision or feedback right: Independently test the trusted acceptance condition chosen for the task.
- Decision owner: Project-authored external verifier controls the result after composition; no shipped semantic verifier owns that verdict.
- Supporting / enforcement mechanisms: External-file requirement, pre-run identity snapshot and post-run hash check, separate process/log, explicit task opt-in.
- Closure path: A passing verifier changes review to done and admits later eligible work. Failure keeps review and halts advancement.
- Why this is / is not agent-owned: The harness has a specific independent verification and return contract. The configured project verifier supplies the actual criterion and evidence acquisition.
- Boundary reachability: The shipped advance entry point invokes the separate verifier on a task explicitly marked auto-verifiable.
- Claim being audited: A completed task's ready claim against its acceptance contract.
- Ordinary reporting path: The worker's normal structured report moves the board into review.
- Complementary access path: The configured separate Python verifier receives project location and criteria and can inspect actual work directly.
- Independence boundary: It is supplied outside the assessed project and hash-bound independently of the worker report, subject to operator configuration.
- Who acts on findings: The board runner marks it accepted only on verifier success and otherwise prevents continuation.
- Evidence: [Advance gate](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Verifier process and receipt](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/board_runtime.py) · [Reviewer boundary](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/engineering-delivery/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: Independent acceptance is reconstructed only for a properly composed verifier. The harness does not certify its coverage.

## S4 — Outside-and-then intelligence

- State: P
- Function: Decide whether to add a new external skill to the project-local capability set.
- Disturbance / variety regulated: Third-party candidate revisions bring new workflows, dependencies or side effects.
- Decisive decision or feedback right: Accept an externally sourced candidate after reviewing its concrete provenance, scans and intended role.
- Decision owner: Project owner/operator.
- Supporting / enforcement mechanisms: Candidate review workflow, local scanner, provenance/hash checks and explicit activation.
- Closure path: Accepted candidate is copied into the project skill surface and the installed revision is recorded for future use.
- Why this is / is not agent-owned: The shipped workflow supplies observations and checks while activation remains under the responsible operator.
- Boundary reachability: Bootstrap ships the intake workflow and the project skill installation path publishes selected skills into the supported hosts.
- External distinction: A candidate external skill from a specific source revision, with observed files, behavior and local scan result.
- Future / prospective distinction: Admitting it changes future project work capability.
- Adaptation option generated: Review an exact candidate, retain it in isolation, or authorize installation with its provenance.
- Path back into current capability / S3: Activation places reviewed content in the host's project skill directory for subsequent turns.
- Evidence: [Intake workflow](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/workflow-skills/skill-intake-review/SKILL.md) · [Scanner workflow](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/skill-guard.py) · [Project activation](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/docs/33-instalar-skills-por-stack.md)
- Basis: structural
- Confidence: medium
- Caveats: This is an on-demand skill intake route. The deterministic stack recommender supplies no autonomous external adaptation decision.

## S5 — Policy and identity

- State: —
- Function: Decide enduring identity and ultimate policy of the delivery workflow.
- Disturbance / variety regulated: Project priorities and irreversible publication can require human authorization.
- Decisive decision or feedback right: No supplied separate identity-level review and authoritative return path was established.
- Decision owner: Operator supplies goals and authorization. Repository author and host configuration set other defaults.
- Supporting / enforcement mechanisms: Bootstrap instructions, human-facing delivery policy, execution ceilings and task-level acceptance.
- Closure path: Board and host apply current project instructions and task authorizations.
- Why this is / is not agent-owned: Human task acceptance and publication decisions remain within the already defined delivery mission.
- Evidence: [Bootstrap instructions](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/bootstrap.py) · [Board task contract](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/scripts/engineering.py) · [Director profile](https://github.com/Breno-J-Oliveira/coding_agent_harness/blob/7289baab4ada4e8b7d4ff5ba6e81d7bd0f99a05a/agents/director.toml)
- Basis: structural
- Confidence: medium
- Caveats: The project owner can set external policy. That alone does not close a shipped S5 process.

### Absence scope

- Surfaces inspected: Bootstrap, project prompt, durable board controls and installed director/delivery instructions.
- Plausible first-party paths checked: Mission definition, irreversible-action escalation, board authorization and release gates.
- Why no material first-party path remains: These are task framing and hand-offs for delivery work. The reviewed distribution supplies no distinct path for revising ultimate identity or allocating mandate and returning it through first-party authority.

## Recursion

The project board coordinates successive bounded turns at the delivery-workflow recursion. The host's core tool runtime, provider, and third-party skill implementations are external machinery.

## Variety and escalation

Unready outcomes and failed verification hold the current board. Human review is explicit, with optional automatic progression only for tasks and verifier combinations authorized in advance.

## Evidence gaps

Static assessment of the frozen source. No Codex or Claude model turn, project deployment, or external skill installation was run.
