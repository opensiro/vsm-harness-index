---
harness_id: looper-nexu
project_name: Looper
repository: https://github.com/nexu-io/looper
review_ref: efc199d6d584e9cffca3464e190f060cc1b71f39
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Looper

## Review boundary

- System in focus: locally installed `looperd` daemon and `looper` CLI composing first-party issue/spec/reviewer/fixer/worker roles over selected supported coding-agent vendors, GitHub/Forgejo source control and local worktrees.
- Purpose and identity: translate marked repository issues and specs into agent-driven coding changes and iterative independent PR review, while a repository owner retains merge and high-level policy authority.
- Relevant environment: GitHub/Forgejo issue/PR labels, assignments, requests, review threads and patches; local Git repositories and worktrees; agent subprocess results, CI checks, daemon queue, user/operator interventions.
- Standard-distribution boundary: shipped `cmd/`, `internal/{runtime,planner,worker,reviewer,fixer,agent,loops,cliapp,storage,forge}/` code with bundled role prompts/skills and documented configured vendor execution; role models run through supported external vendor CLI adapters, not as independently credited vendor-specific platforms.
- Credited operating / distribution surfaces: daemon discovery/queue/roles, first-party planner/worker/fixer model-facing runs and review-loop dispatch, reviewer with separate PR-diff/criterion access and returned findings, operator-facing loop state and actual pause/resume/terminate/takeover commands.
- Adjacent first-party surfaces excluded from ownership: repository development/CI, e2e smoke scripts, GitHub/Forgejo maintainer governance, external vendor AI agent source code and arbitrary user-provided skills, and `loopernet` remote networking when not configured; no rights are borrowed from an uninstalled third-party model host.
- First-party operating / deployment modes considered: self-hosted local daemon with GitHub or Forgejo supported projects, default asynchronous role loops, manual one-shot role commands, reviewer/fixer takeover and parent-operator loop control.
- Recursion level: one daemon controlling its registered repository/PR work portfolio; S1 cells are activated coding-role processes and task loops. The hosting repository maintainers are outside this operational VSM boundary.
- Reviewed revision: `efc199d6d584e9cffca3464e190f060cc1b71f39`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Looper's `looperd` daemon discovers GitHub/Forgejo PR and issue work through label/assignment eligibility, stores durable queue/loop state, creates local Git worktrees and invokes a configured model-driven vendor agent via `internal/agent/executor.go`. Bundled role-specific inputs drive Planner, Worker, Reviewer and Fixer. The Planner iterates to a reviewable spec PR, Worker implements issues/specs in its worktree, Reviewer independently reads PR changes and criteria and publishes actionable review comments, and Fixer makes changes in response to those comments; the Reviewer repeats on new HEAD. The scheduler handles status transitions and lease/claim fencing; by itself that is deterministic coordination support rather than an agent authoring S2 or S3 decisions. The CLI exposes status/loop inspection, pause/resume/stop, queue diagnostics and takeover. Human/parent can act on current jobs; ordinary approval or merge remains outside autonomous identity/policy ownership. [README overview](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L7-L40), [runtime scheduler](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/runtime/scheduler.go#L57-L142), [agent executable adapter](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/agent/executor.go#L468-L650), [role workflow](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L175-L212).

## Operational model

Each active role is a first-party instructed model-driven actor operating through a configured supported agent CLI, subject to deterministic queue admission, repository claims and operator policies. Planner and Worker contribute coding outputs; Fixer reacts to an independently rendered review. Reviewer is distinguished from the implementation owner and analyzes PR head/diff and acceptance criteria from a separate review path. The daemon maintains state and dispatches eligible role work. A local operator can inspect the active portfolio and change present commitments via pause/stop/unpause/takeover; these interventions close a parent-governed current-control path but do not transfer ordinary agent tool choice to the human in an unattended run.

## S1 — Operations

- State: A
- Function: autonomously select model-driven repository planning, coding/repair and PR review operations within the offered first-party role workflows.
- Disturbance / variety regulated: changing issue requirements, source context, failures, test outcomes and PR-review findings.
- Decisive decision or feedback right: activated role agent chooses analysis, implementation or repair actions from task/prompts and observed Git/PR state; the configured external AI CLI supplies the model/tool execution substrate.
- Decision owner: first-party configured role agent when invoked through a supported installed vendor; the third-party runtime implementation is execution substrate, not an extra Looper S-system.
- Supporting / enforcement mechanisms: role-specific prompts, Git worktrees, local daemon queue, GitHub/Forgejo integration, lease containment and persisted loop state.
- Closure path: the role reads task or review input, produces spec/PR changes or review findings, publishes them through the supported forge and receives subsequent observed state to continue, retry or finish.
- Boundary reachability: daemon's Worker/Planner/Reviewer/Fixer runners use the shipped vendor executor under configured agent vendor, including manual role mode, as documented in the first-party CLI.
- Why this is / is not agent-owned: model-driven role chooses substantive content and edits, while daemon gates eligible admission and subprocess containment. A vendor CLI must be installed/configured; no separate ownership claim is made for unsupported vendor capabilities.
- Evidence: [loop roles and termination criteria](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L22-L31), [supported role agents](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L35-L40), [agent subprocess Start](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/agent/executor.go#L468-L650), [worker runner](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/worker/runner.go#L360-L540).
- Basis: structural
- Confidence: high
- Caveats: this is a source-level assessment of shipped vendor-composition logic, not a live external agent execution or assertion that all vendors have identical tool permissions.

## S2 — Coordination

- State: —
- Function: a distinct coordination decision right attenuating concrete inter-S1 oscillation/interference is not established beyond deterministic claim/lease isolation and role handoff at the reviewed root.
- Disturbance / variety regulated: simultaneous loops might compete for a PR/issue/worktree, but source paths largely avoid duplicates with static eligibility and queue fencing rather than model-governed mutual adjustment.
- Decisive decision or feedback right: no positive S2-specific first-party owner/constructor path established.
- Decision owner: daemon deterministic scheduler and configured GitHub/Forgejo claim/eligibility policy.
- Supporting / enforcement mechanisms: queue claims, worktree isolation, reviewer/fixer handoff labels and network lease validation.
- Closure path: queue gates can block duplicate starts and role sequencing advances; no independent S2-specific control decision and feedback among competing S1 agents is credited.
- Why this is / is not agent-owned: Reviewer findings closing into Fixer changes are assessed as independent audit, not automatically S2; sequential role workflow is insufficient to prove an autonomous inter-worker conflict regulator.
- Evidence: [roles handoff and worktrees](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L25-L39), [scheduler claim/lease enforcement](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/runtime/scheduler.go#L89-L142), [worker claim collision guard](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/worker/runner.go#L2844-L2885).
- Basis: structural
- Confidence: medium
- Caveats: a source-pinned trace proving actual competing worker commitments with autonomous S2 attenuation could warrant explicit future re-review; generic lifecycle and isolation do not suffice.

### Absence scope

- Surfaces inspected: README role topology, runtime scheduler/claim ownership, worker/PR discover, reviewer/fixer loop, forge conflict checker and local worktree isolation.
- Plausible first-party paths checked: cross-role handoff, reviewer/fixer feedback, duplicate PR/issue claims, merge-conflict check, multi-repository agent queue and network coordinator leases.
- Why no material first-party path remains: these paths gate static eligibility, sequencing or safety fencing; no shipped S2-specific discretionary or constructible mutual-adjustment judgment was established across competing independent S1 operational obligations.

## S3 — Inside-and-now control

- State: P
- Function: parent-operator current control of the daemon's active portfolio via inspection and real-time interruption, release, retry and takeover of ongoing role loops.
- Disturbance / variety regulated: blocked role loops, unresolved review/fix budget holds, stalled work, manual scope decisions, improper ongoing commitments and competing operator priorities.
- Decisive decision or feedback right: which current loop to pause, resume, terminate, take over or restart, after inspecting the daemon's active and blocked state.
- Decision owner: legitimate local operator in the supported parent-controlled mode; deterministic code executes chosen controls. No separate autonomous A or constructor C S3 mode established.
- Supporting / enforcement mechanisms: CLI `looper ps`, `looper loop inspect`, queue diagnostics, persisted `LoopRecord`, service Pause/Terminate/Resume methods and scheduler requeue.
- Closure path: operator reads loop/queue current state, issues `looper unpause`, `stop` or takeover action; the first-party service durably changes loop status, cancels or resumes agent execution and scheduler uses the new state on subsequent dispatch.
- Boundary reachability: standard shipped local daemon/CLI supports `status`, `ps`, `stop`, `unpause`, `takeover list/stop` as real operator pathways; no external custom plugin is required.
- Why this is / is not agent-owned: review/fix agents do not decide whole-fleet current priorities; the local parent operator does, with real return into active queue/role execution.
- Whole-system current view: `looper ps`, `loop inspect`, `queue failed` and `takeover list` jointly expose active and blocked loops over registered projects, run/agent status, failure/hold and current assigned PR.
- Current-control decision scope: current assignment/commitment intervention (pause, hold release, stop, terminate, force/manual takeover, retry) and practical resource engagement by canceling or resuming active jobs.
- Evidence: [operator commands](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/docs/users-guide.md#L513-L551), [pause/resume/terminate service](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/loops/service.go#L189-L270), [diagnostic portfolio API](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/cliapp/loop_diagnostics_commands.go#L167-L235), [takeover controls](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L110-L136).
- Basis: structural
- Confidence: medium
- Caveats: this is a **parent-governed** supported mode, not S3=A. A kill button alone would not suffice; here live portfolio/hold visibility and returned multi-loop commitment interventions are the credited combined surface.

## S3* — Complementary audit

- State: A
- Function: Reviewer role independently inspects actual new PR head/diff and acceptance criteria, judges findings and returns them to the separate Fixer/Worker operational loop.
- Disturbance / variety regulated: claimed completed implementation may hide bugs, missed requirements or maintainability flaws not visible in Worker self-report/tests.
- Decisive decision or feedback right: Reviewer agent independently selects substantive review findings for the current PR and whether actionable issues remain; Fixer consumes review threads and modifies code, triggering a subsequent fresh review.
- Decision owner: first-party configured Reviewer role/model, separate from implementation Worker/Fixer; deterministic review marker, criteria parser and runner do not become the audit judge.
- Supporting / enforcement mechanisms: PR snapshot/head tracking, separate read of patch and criteria, issue/PR review API, thread state, review scheduler, worktree and optional isolation.
- Closure path: Reviewer reads actual PR code and acceptance criteria, posts actionable review findings; Fixer changes/pushes new head in response; Reviewer re-reads changed head and continues until no actionable threads remain or a human hold is needed.
- Boundary reachability: shipped Reviewer/Fixer loops and supported manual `looper review ... --loop` with distinct role prompts and configured model are first-party selectable code paths, not an external unselected third-party auditor.
- Why this is / is not agent-owned: the reviewer agent judges what needs improvement; automatic event markers, static validators and human terminal merge are support/ultimate approval, not replacements for the independent audit judgment.
- Claim being audited: implementation is complete, matches task/spec and contains no actionable code defects.
- Ordinary reporting path: Worker/Fixer implementation PR, model-generated completion markers, test/check statuses and changed commit.
- Complementary access path: Reviewer independently retrieves current PR head, diff and reviewable source/context through GitHub/Forgejo, rather than accepting Worker completion assertions.
- Independence boundary: dedicated Reviewer role and its independent PR read/analysis loop are distinct from the implementation Writer/Fixer task; separate prompts/eligibility and repeat review on new commits. Same configured vendor provider may be used, so model-identity independence is not claimed.
- Who acts on findings: Fixer loop addresses actionable review threads; Reviewer rechecks after changes; unresolved issues may be held for human/operator.
- Evidence: [reviewer/fixer loop contract](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L25-L31), [reviewer evidence/criteria processing](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/reviewer/runner.go#L240-L340), [reviewer stage/re-evaluation](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/reviewer/runner.go#L2700-L2820), [fixer review-thread feedback](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/fixer/runner.go#L204-L306), [reviewer head-change detection](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/reviewer/runner.go#L8735-L8755).
- Basis: structural
- Confidence: medium
- Caveats: no independent third-party audit actor or live run was observed; positive state is internal first-party role separation and complementary direct source access, not independence of model weights or upstream AI vendor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped loop builds a prospective external/environment view, selects future adaptation options for Looper's own operating capability and returns decisions to current control.
- Disturbance / variety regulated: new issue assignments, commit notifications and provider errors drive present jobs; they are not an explicitly prospective external-change judgment.
- Decisive decision or feedback right: not established as S4.
- Decision owner: configured role/runtime and repository developer/operator update Looper's code, vendors and policy outside the evaluated runtime.
- Supporting / enforcement mechanisms: roadmap/ADR documents, scheduled issue polling, provider capability inspection, upgrade commands and retry policies.
- Closure path: external issue events can trigger present coding jobs and provider settings can be manually updated; no future-adaptation judgment is brought back into current Looper capability by a first-party S4 actor.
- Why this is / is not agent-owned: Planner plans a future *task implementation*, but not how the harness itself adapts to an external prospective environment.
- Evidence: [role purpose](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L7-L40), [configurable agents](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/docs/configuration.md#L1-L80), [scheduler](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/internal/runtime/scheduler.go#L57-L142).
- Basis: structural
- Confidence: medium
- Caveats: a supported organization may apply reviewer recommendations to upstream Looper development, but repo maintainer actions are outside assessed installed mode.

### Absence scope

- Surfaces inspected: planner and role limits, scheduler, provider configuration/upgrade and status/diagnostics, documentation and upgrade paths.
- Plausible first-party paths checked: issue planning as future intelligence, automatic response to new PR commits, vendor upgrading, capability detection, retry learning and maintainers' public roadmap.
- Why no material first-party path remains: they govern current assigned coding work, static provider configuration and human development, without a durable S4-specific outside/future option-selection/return-to-capability loop.

## S5 — Policy and identity

- State: —
- Function: live ultimate-policy or organizational identity closure is not established within the installed Looper daemon's standard distribution.
- Disturbance / variety regulated: PR merge permissions, human intervention, vendor access, privacy and tenancy are handled through static configuration and forge/host authority.
- Decisive decision or feedback right: no shipped identity or ultimate-policy decision with authoritative feedback into subsequent operations.
- Decision owner: local operator and source repository/forge administration define policies; agents operate within them.
- Supporting / enforcement mechanisms: GitHub/Forgejo merge requirements, per-role agent selection, static config, label workflows, leases and escalation prompts.
- Closure path: a user may approve merge or take over a PR, which closes a particular current task, not a S5 system identity issue returned as an operative ultimate policy.
- Why this is / is not agent-owned: review decisions concern code quality and present execution; they neither grant nor choose top-level purpose/identity, and ordinary human merge permission is not S5=P.
- Evidence: [human merge boundary](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/README.md#L7-L31), [configured operator/workflow gates](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/docs/users-guide.md#L205-L219), [role/daemon configuration](https://github.com/nexu-io/looper/blob/efc199d6d584e9cffca3464e190f060cc1b71f39/docs/configuration.md#L1-L80).
- Basis: structural
- Confidence: medium
- Caveats: neither GitHub branch-protection decisions nor the maintainer organization are borrowed as operational S5 authority at the daemon recursion.

### Absence scope

- Surfaces inspected: daemon config, planner/worker/reviewer/fixer roles, CLI operator commands, GitHub/Forgejo merge controls, human-in-the-loop holds, README and user guide.
- Plausible first-party paths checked: explicit merge approval, operator control, policy/roles settings, HITL adjudication and governance documentation.
- Why no material first-party path remains: no first-party runtime captures a system identity/ultimate-policy issue, routes it to legitimate decision authority and returns an authoritative decision to alter the continuing harness's governing identity.

## Distributed OSS parent arrangement

Independent project maintainers in GitHub/Forgejo are outside the local Looper runtime's own authority boundary. An owner deploying one local daemon acts as the parent for local operational current-control (S3=P); public source-governance and pull-request merges are not presumed to form organization-level S5=P.

## Self-hosted and non-human modes

The self-hosted daemon and operator commands expose a supported parent current-control mode distinct from unattended task-role behavior. In non-human unattended mode, role completion and audit can be autonomous, but no other S3/S4/S5 ownership is inferred merely from access to status or configuration.

## Recursion

Agent subprocesses are S1 execution cells of the parent daemon's active issue portfolio. Sequential role stages, a fleet of registered repos and vendor subprocesses do not by themselves establish complete additional VSM recursions.

## Variety and escalation

Forge labels and leases bound admission; worktrees isolate changes; Reviewer rechecks fresh code and Fixer can iterate; HITL holds stop uncertain/risky changes and operator can intervene. A deferred human merge remains terminal authority for repository incorporation, not runtime identity governance.

## Evidence gaps

No configured vendor was executed live; positive claims are based on first-party source contracts and runtime reachability. S3* independence means separate reviewer judgment and PR-diff access, **not** statistically independent models or third-party verification. Positive S3 parent ownership is bounded to the local operator portfolio, not public upstream institutional governance.