---
harness_id: trellis
project_name: Trellis
repository: https://github.com/mindfold-ai/Trellis
review_ref: f089cb3286071199e84118dee86b6d76aab032f1
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Trellis

## Review boundary

- System in focus: the shipped Trellis CLI / project setup, task/spec/memory workflow and optional `trellis channel` runtime for independently executing model-backed coding-agent workers.
- Purpose and identity: structure AI-assisted software work around persistent project conventions, per-task artifacts, agent implementation/check roles and controlled worker collaboration.
- Relevant environment: software requirements, repository state/diffs, project specifications, LLM coding-agent providers (Claude/Codex etc.), channel worker processes, errors, tests and a supervising user/main agent.
- Standard-distribution boundary: `@mindfoldhq/trellis` CLI, `@mindfoldhq/trellis-core`, generated platform-specific commands/skills/hooks and packaged channel runtime. External coding-agent executable, model/provider and user's project are configured dependencies, not a single autonomous Trellis-owned parent.
- Credited operating / distribution surfaces: [`packages/cli/src/commands/channel/`](https://github.com/mindfold-ai/Trellis/tree/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/commands/channel), [`packages/core/src/channel/api/`](https://github.com/mindfold-ai/Trellis/tree/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api), shipped [`trellis-channel` Skill](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/SKILL.md), supported platform agent templates, core task/state helpers and generated workflow hooks.
- Adjacent first-party surfaces excluded from ownership: upstream maintainers/contributor workflow, docs website/demo, CI/unit tests, release tooling, private adopter organizational policy and unrelated external coding-agent sessions not launched/wired by Trellis.
- First-party operating / deployment modes considered: single-agent `trellis init` project scaffold and installed plan/implement/check/finish skills; Claude/Codex channel worker spawning; review/check worker roles; channel worker registry/inbox/interrupt/resume; forum and project memory; user/manual supervisor and host-provided model execution.
- Recursion level: one task-centered coding development operation, optionally including the local channel worker team. Nested worker processes are S1 units only for their operational work, not automatically independently viable companies.
- Reviewed revision: `f089cb3286071199e84118dee86b6d76aab032f1`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/README.md) describes a task loop: brainstorm/plan, agent implement, agent check and finish/spec update. A [generated implement worker card](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/implement.md) instructs a model-backed worker to inspect task PRD and specs, change code, self-test and report; a distinct [check card](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/check.md) reviews raw diffs and can self-fix mechanical defects. Platform-specific command and subagent templates are installed by the CLI; their model execution still depends on the configured Claude/Codex/other host.

The optional first-party [`channel` worker CLI](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/commands/channel/spawn.ts) launches a supervised process with provider adapter and bounded context. [`spawnWorker`](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/spawn.ts) invokes an injected `WorkerRuntime.start`, writes a durable `spawned` event and projects worker state. [`send`](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/send.ts), [`wait`](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/commands/channel/wait.ts) and per-worker inbox events carry messages and results. The [worker registry](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/workers.ts) reconstructs active/terminal worker state; [`interruptWorker`](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/interrupt.ts) can return a provider-level interruption result and record it durably. The [worker skill](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/references/workers.md) explicitly supports interrupt/redirect, kill/resume, live-worker budget and warnings.

This distinguishes (i) actual model-backed operating worker, (ii) deterministic event/store/supervisor mechanism, and (iii) a specific current-team control surface for a dispatcher. It does **not** imply the CLI autonomously decides whole-team priority: the dispatcher is a separate human or configured main coding agent. Likewise, current spec files, task manifests, hook-injected context and [spec-update instruction](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/skills/update-spec.md) are reusable rules and memory, not automatically self-governing policy or strategic intelligence.

## Operational model

The user or supervising main session initializes Trellis, describes a goal and provides context. An installed agent-facing instruction can call/dispatch a model-backed implement or check worker; the provider model selects code operations, consumes local results and returns report/edits. At channel recursion, the dispatcher can observe all relevant worker states, send revised instructions, interrupt/resume work and reallocate which worker performs a task, but Trellis does not itself supply a standing autonomous dispatcher that owns those choices. The packaged dispatcher tools and workflow guidance form a function-specific S3 construction path. Peer message transport and mandatory code review remain bounded to task work.

**Proposed disposition: included**, vector `A — C — — —`. Positive S1 uses the real supported provider-wired worker mode, not a bare Markdown template; S3 `C` identifies exposed current-worker control that needs composition with a legitimate autonomous dispatcher, not S3 autonomy or an invented parent-mode closure.

## S1 — Operations

- State: A
- Function: execute a delegated coding/research/check task using model-selected file reads, edits, diagnostics and final reporting within Trellis task context.
- Disturbance / variety regulated: changing repository code, ambiguous task requirements, test failures, missing context and generated artifact constraints.
- Decisive decision or feedback right: choose local implementation/review actions and corrections in response to task context and tools.
- Decision owner: configured Claude/Codex or similar model-backed worker launched via the supported first-party channel/provider adapter or installed host agent template; Trellis supplies tasks, card, spawn/inbox and result mechanics.
- Supporting / enforcement mechanisms: PRD/spec manifests, agent role cards, provider adapter, durable channel events, context injections, verification recommendations and time limits.
- Closure path: dispatcher sends PRD/spec context → Trellis launches and wakes an actual provider worker → model reads/edits/tests or critiques → worker publishes progress and completion event/report → dispatcher or repo receives result.
- Boundary reachability: shipped `trellis channel spawn --agent implement/check` actually calls the first-party CLI/provider runtime and `spawnWorker`; agent cards define operational tasks. This is a supported product command, not development-only dogfood or an implied arbitrary third-party agent feature.
- Why this is / is not agent-owned: remove the worker model and only launch/routing/event primitives remain; contextual code-selection and repair discretion disappear. The external provider runs the model, but the first-party product supplies the supported launch/inbox loop.
- Evidence: [channel CLI spawn](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/commands/channel/spawn.ts), [core spawn](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/spawn.ts), [worker guide](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/references/workers.md), [implement agent](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/implement.md).
- Basis: structural executable adapter/worker path.
- Confidence: high for shipped architecture; no live model performance measured.
- Caveats: requires installed and authenticated model provider, actual project context and task initiation; a docs-only scaffold without a running provider would not suffice.

## S2 — Coordination

- State: —
- Function: no first-party S2-specific mediation of an established inter-S1 interference or oscillation between distinct ongoing worker operations.
- Disturbance / variety regulated: peer response timing, missed messages, code review disagreements, worker task handoffs and shared-file editing risk.
- Decisive decision or feedback right: adjudicate a concrete worker-worker collision and return an agreed coordination change into both workers' later behavior.
- Decision owner: dispatcher may message or redirect workers on a task; event transport/locks do not decide how distinct worker conflicts are settled.
- Supporting / enforcement mechanisms: per-worker inbox policy, durable forum/channel log, worker IDs, `send`, `wait`, lock/seq, interrupt, task cards.
- Closure path: messages can go from dispatcher to workers and back; no native conflict detector, arbitration/attenuation judgment and bilateral regulation is evidenced for any specific inter-S1 collision.
- Why this is / is not agent-owned: two model agents debating architecture are collaborating on a deliverable, not necessarily two autonomous S1 operations whose interference is being regulated by S2.
- Evidence: [channel collaboration patterns](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/references/workflows.md), [worker inbox](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/internal/store/inbox.ts), [messages API](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/send.ts).
- Basis: bounded structural negative.
- Confidence: medium-high.
- Caveats: an adopter may construct a concrete S2 agent via the same channel but generic multiagent messaging is not function-specific S2 evidence.

### Absence scope

- Surfaces inspected: channel event/inbox/worker APIs, peer brainstorming and parallel-check recipes, task artifacts, shared spec management and worker guard.
- Plausible first-party paths checked: channel queue as collision control; peer architecture disagreement as S2; independent reviewers as inter-unit coordination; worker interrupt as resolution of concurrent file edits.
- Why no material first-party path remains: the shipped patterns do not specify an actual cross-worker interference channel and feedback regulating both S1 units; routing and local task QA do not satisfy the distinct S2 witness.

## S3 — Inside-and-now control

- State: C
- Function: support current oversight of a bounded active worker team and permit decisions to reassign, redirect, stop or restart its work before next task commitments.
- Disturbance / variety regulated: stalled workers, excessive idle/live worker footprint, changing priorities, stuck executions and failing or obsolete task commitments.
- Decisive decision or feedback right: after seeing whole-channel worker state and progress, choose which worker to spawn, interrupt, rebrief, resume, or retire and issue a changed instruction.
- Decision owner: separately initiated dispatcher (a user or external main coding agent) owns the discretionary choice; Trellis constructs the full worker-registry/command/feedback surface but supplies neither a standing autonomous supervisor nor a supported legitimate S3(P) parent governance loop at this recursion.
- Supporting / enforcement mechanisms: `listWorkers`/`watchWorkers`, process liveness and supervisor warning, spawn budget/TTL, inbox message and provider interrupt/kill/resume, event log/audit.
- Closure path: registry/status/progress observation → dispatcher chooses intervention → first-party `send`/`interrupt`/kill/spawn command → worker runtime receives changed instruction or termination → subsequent worker state and events update registry.
- Boundary reachability: channel commands, worker cards and supervision/interrupt recipes are shipped under the installed CLI and packaged Skill; CLI actually manages provider-worker processes and exposes the control loop. A composed dispatcher must invoke these controls before autonomous S3 ownership can be credited.
- Why this is / is not agent-owned: deterministic worker budget, status projection or process kill alone are not S3 judgment; the control opportunity is S3-specific and reachable, but decision authority remains with the dispatcher supplied at integration time, so `C`, not `A`.
- Whole-system current view: `listWorkers` and `watchWorkers` project all channel workers' active/terminal/activity state, while `messages` and `probeWorkerRuntime` expose recent progress and local liveness, bounded to that team's channel.
- Current-control decision scope: active worker assignment, runtime interruption/redirect and stop/resume across the worker team; not organization-wide funding, product strategy or Trellis maintainer governance.
- Evidence: [worker registry](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/workers.ts), [interrupt API](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/interrupt.ts), [spawn worker](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/channel/api/spawn.ts), [operator action workflow](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/references/workers.md).
- Basis: first-party S3-specific constructor path with functional view/right/return, but external discretionary owner.
- Confidence: medium for S3 constructor, high for control APIs' existence.
- Caveats: the dispatcher has to review worker states and choose action; Trellis by itself does not autonomously optimize shared priorities or verify legitimacy of a higher parent authority. The current-view scope is one worker channel/team, not all installations.

## S3* — Complementary audit

- State: —
- Function: no established systemic complementary-audit authority with sufficiently independent access to operational reality and corrective return into S3 control.
- Disturbance / variety regulated: incorrect generated code, missed requirements, false successful completion and untested diffs.
- Decisive decision or feedback right: inspect operational claims through a separately constituted reality channel, challenge them and return corrective findings to systemic current control.
- Decision owner: `trellis-check` model worker can review task diff independently of implementer, but its stipulated purpose is ordinary code quality and mechanical repair in the task pipeline; no separate systemic audit mandate/authority is evidenced.
- Supporting / enforcement mechanisms: check agent card, git diff/test execution, curated `check.jsonl` context and channel report/events.
- Closure path: task implementation → check agent code review → self-fix/report → dispatcher finishes task. This is task production QA, not complementary S3* inspection of ongoing organizational actuality.
- Why this is / is not agent-owned: a different reviewer agent and a direct diff are real separation of task roles; they do not alone show a complementary audit coupled to S3's independent actual-vs-reported supervisory view.
- Evidence: [check worker card](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/check.md), [channel implement/check pattern](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/bundled-skills/trellis-channel/references/workflows.md), [check skill](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/skills/check.md).
- Basis: bounded negative, despite substantive QA.
- Confidence: medium.
- Caveats: a separately commissioned, independent system-audit worker with alternate operational evidence and explicit management return could change this classification.

### Absence scope

- Surfaces inspected: default implement/check agent cards, diff review, CLI channel reports, worker status and task validation workflows.
- Plausible first-party paths checked: check agent as S3*; direct git diff/tests as complementary access; worker status registry as audit alternative.
- Why no material first-party path remains: the packaged review is routine same-task quality assurance, and status monitoring is normal S3 support; a separate operational-reality audit mandate that returns a systemic correction is not supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed organization-level external-and-prospective strategy adaptation loop governing current worker-team capability.
- Disturbance / variety regulated: new toolchain practices, project conventions, lessons from completed tasks and agent platform changes.
- Decisive decision or feedback right: sense future-relevant external distinctions, compare capability options and return selected adaptation to present managerial control.
- Decision owner: implementer/checker may suggest updates to specs; user/project maintainer chooses future workflow and platform configuration.
- Supporting / enforcement mechanisms: project session journals, `/trellis:finish-work`, `trellis-update-spec`, spec feedback templates and platform migration/setup operations.
- Closure path: completed task → learning capture → changed future context/spec; no distinct prospective environmental scanning/options judgment and S3-facing strategy decision is shipped.
- Why this is / is not agent-owned: persistent memory and updated specifications improve later S1 work, but internal lessons are not automatically S4 external future intelligence.
- Evidence: [README workflow](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/README.md), [update-spec](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/skills/update-spec.md), [project memory](https://github.com/mindfold-ai/Trellis/tree/f089cb3286071199e84118dee86b6d76aab032f1/packages/core/src/mem).
- Basis: bounded negative after adaptation test.
- Confidence: medium-high.
- Caveats: organizational strategy workflows could be composed using memory and channels, but no shipped function-specific S4 owner/return is established.

### Absence scope

- Surfaces inspected: task phases, session memory, update-spec, project platform setup/migrations, channel forum and worker skill.
- Plausible first-party paths checked: future spec learning as S4; external platform updates as prospecting; supervisor's possible adoption decisions as S4(P).
- Why no material first-party path remains: the reviewed modes persist current-task lessons and configuration, without a first-party outside/future options process returning authoritative capability change to S3.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy adjudication over the worker-team organization with binding decision return.
- Disturbance / variety regulated: agent compliance with project conventions, forbidden git commits, permissions, task-scope drift and disagreements over coding standards.
- Decisive decision or feedback right: legitimately settle identity/ultimate-policy disputes and send a binding policy update into later operation.
- Decision owner: project maintainer/user sets top-level objectives, decides repo standards and retains git commit/merge authority. Agent templates instruct bounded work but do not constitute identity-level authority.
- Supporting / enforcement mechanisms: `.trellis/spec`, task PRD, worker cards, skill guardrails, AGENTS/CLAUDE files and manifest/permission boundaries.
- Closure path: project policy is injected as context; ordinary suggestions may be updated in repo, but no specific identity dispute → legitimate parent decision → operationally binding return path is established by the channel runtime.
- Why this is / is not agent-owned: a model check agent can ask for clarification and project-owner approval may govern actual deployment, but this is task/config governance rather than a shipped S5(P) function-specific loop.
- Evidence: [implement agent boundaries](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/implement.md), [check agent](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/trellis/agents/check.md), [spec update](https://github.com/mindfold-ai/Trellis/blob/f089cb3286071199e84118dee86b6d76aab032f1/packages/cli/src/templates/common/skills/update-spec.md).
- Basis: bounded negative after parent-mode check.
- Confidence: medium-high.
- Caveats: a project's actual human constitution can own S5 at a larger recursion, not imported merely by Trellis project setup.

### Absence scope

- Surfaces inspected: project spec/instructions, implement/check role limits, task metadata, channel human dispatcher and repository maintainer boundaries.
- Plausible first-party paths checked: shared specs as S5; supervisor’s project approvals as S5(P); worker no-commit constraint as ultimate identity policy.
- Why no material first-party path remains: static conventions and approvals do not establish a runtime identity/ultimate-policy escalation/return loop within the declared team.

## Distributed OSS parent arrangement

Independent Trellis installations can share versioned specs within one project but do not constitute a single operating parent across repositories. Open-source maintainer merges and release practices are adjacent software project governance, not automatically the installed channel team's legitimate S3/S5 authority. Local dispatcher interventions are bounded to its own project/channel recursion.

## Self-hosted and non-human modes

The first-party local CLI can launch external-provider model workers and supervise them through an event-sourced channel. Multi-agent subteams without a human in each worker turn are real S1 operation; channel status/interrupt capabilities alone do not imply autonomous supervisory S3 (or human parent S3(P)). The shipped control constructor is represented as `S3=C` pending composition with an authorized deciding dispatcher.

## Recursion

A channel team with implement/check workers can be one S1 subsystem of a broader organization; the team also has lower-recursion task agents. Task nesting, separate worker PIDs and forum threads do not prove that every level supplies a complete S1–S5 viable organization. The assessed S3 constructor concerns the channel worker team only.

## Variety and escalation

Task PRD/spec manifests, role cards, bounded worker contexts and live-worker budgets attenuate requirement/process variety. Multi-provider workers, peer brainstorming, iterative repair and the channel's inbox/interrupt mechanisms amplify operational options and return task-level exceptions to a dispatcher. A crash warning or timeout is not in itself an algedonic path into a demonstrated S4/S5. A dispatcher can intervene using the S3-specific constructor but remains an externally composed owner of that choice.

## Evidence gaps

This is pinned first-party source review, without authentication to execute a Claude/Codex worker or measure live multiagent outcomes. The checkout lacks `node_modules`; the upstream `pnpm test` suite was not executed and Python template compilation only verifies syntax. In particular, `S3=C` is an architectural function-specific construction finding, not a claim that Trellis autonomously supervises workers, resolves their conflicts, or supplies legitimate parent governance in a particular adopter organization. Different default platform adapters vary in hook and subagent support; credit is limited to supported installed channel mode.
