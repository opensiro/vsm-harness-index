---
harness_id: dori-superagent
project_name: Dori Superagent
repository: https://github.com/sisyphuslabs/dori-superagent
review_ref: 06c4600b77f6e81ed9bd5b706d736bec07cf27b1
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Dori Superagent

## Review boundary

- System in focus: First-party Dori TypeScript CLI, one lead, duty and hourly loop, work-lane omo agents in herdr panes, persistent lane/inbox/backlog/receipt state, and guarded PR review/merge within a configured workspace.
- Purpose and identity: Let a user direct several independent coding tasks through one conversational lead, maintain task progress in separate agent sessions, avoid interrupting busy sessions, and verify completion before reporting or merging.
- Relevant environment: User requests, Git repositories and pull requests, herdr terminal/pane states, external omo coding-agent runtime, CI checks, host load, deferred work and stalled/vanished workers.
- Standard-distribution boundary: Root `dori up`, `start`, `report`, `ready`, `send`, `duty`, `loop`, `review`, `merge` and `done` implementation, with shipped `prompts/*.md`; separate optional messenger-oriented `skills/dori-mode` implementation is noted but is not imported to manufacture additional rights.
- Credited operating / distribution surfaces: [CLI boot](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/cli.ts), [harness lifecycle, duty and audit gates](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts), [hourly work loop](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/loop.ts), [herdr bridge](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/herdr.ts), [lead instructions](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lead.md), [review instructions](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/review.md).
- Adjacent first-party surfaces excluded from ownership: Repo development CI/tests, README benchmark/comparison with DeepSeek, contribution counts and author claims, downstream agent provider internals, GitHub's approval authority and external Herdr/omo intrinsic controls.
- First-party operating / deployment modes considered: `dori up` created lead/duty/loop panes, independently launched per-ticket coding lanes, busy-pane message batching, idle/lost escalation, hourly backlog scheduling, fresh head-pinned code review and exact-head guarded merge; no speculative future integration credited.
- Recursion level: One task-delivery organization with multiple independently tasked lane agents, one lead and auxiliary duty/reviewer; each lane is an operating S1 unit, not merely a deterministic tool call.
- Reviewed revision: `06c4600b77f6e81ed9bd5b706d736bec07cf27b1`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`dori up` creates a herdr workspace and starts first-party prompted lead and duty `omo` sessions, plus TypeScript duty/hourly loops. The lead receives user instructions and translates them into task briefs; `startLane()` creates a separate tab and starts an omo agent per brief. Lanes report milestones and submit READY with evidence to the lead. `send()` and `flushInbox()` prevent messages entering busy panes. Duty polling nudges idle lanes and escalates lost or stalled work; the hourly loop checks backlog and resource capacity to start eligible work. A separate ephemeral reviewer is invoked with a fresh `omo -p --no-session` call and exact PR head, stores an explicit CLEAR/BLOCK receipt, and `mergeGate()` refuses stale heads or non-green CI. [README](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/README.md), [harness.ts](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts), [loop.ts](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/loop.ts).

## Operational model

Separate model-driven lane agents handle concrete coding tasks, while the model-driven lead sees cross-lane reports and decides assignments, responses to loss/escalation and whether to close verified work. Dori's first-party queue/duty machinery regulates arrival-time contention and liveness across the lanes but has mostly deterministic thresholds rather than agent-owned S2 judgments. The fresh PR reviewer has a dedicated independent audit prompt, and its receipt is a necessary but insufficient condition for merge. The scheduled backlog selector operates the present queue; it does not make a future-oriented environmental/strategy decision.

## S1 — Operations

- State: A
- Function: Autonomous implementation and revision of individual written coding tasks by one dedicated agent lane.
- Disturbance / variety regulated: Unexpected codebase details, changed specifications, test failures, repository state and technical uncertainty within each task.
- Decisive decision or feedback right: Each independently started omo coding model interprets the brief, chooses code/tool steps, observes their outcomes and can produce further work or a READY evidence report.
- Decision owner: Per-lane external omo model hosted in a Dori-created task-specific herdr tab; Dori first-party constructs, starts and wires the lane within its ordinary distribution.
- Supporting / enforcement mechanisms: Brief+lane-footer prompt, `startLane`, isolated pane/session, lane report/ready protocol, persistent evidence links and lead return channel.
- Closure path: Lead/task brief → first-party `startLane()` invokes omo worker → model-owned edits/tool observations → `report()` or evidence-gated `ready()` → lead receives feedback and can request corrections.
- Boundary reachability: `dori start` is a shipped CLI operation; `dori up` launches a lead instructed to call it for each user request, and hourly loop also starts eligible pre-authorized briefs.
- Why this is / is not agent-owned: First-party TS does not decide the code changes; launched agent sessions are the task-specific discretionary actors, although the underlying omo tool engine is external.
- Evidence: [harness.ts#L130-L188](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts#L130-L188), [lane-footer.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lane-footer.md), [lead.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lead.md).
- Basis: explicit + structural
- Confidence: high for shipped first-party session constructor, medium for provider runtime success without live provider execution.
- Caveats: Agent cognition and terminal implementation come from herdr/omo; no claim of ownership of their standalone agent features.

## S2 — Coordination

- State: C
- Distinct S1 units: Two or more independently briefed worker lanes are separate omo sessions in separate herdr tabs, identified by unique lane keys, and can send messages to each other with `dori send <key> --text ...`; the lead is a separate receiving/forwarding role.
- Inter-S1 disturbance: A message or handoff emitted while another lane is actively executing a tool/model turn can interrupt that S1's own evidence-to-action closure, especially with several concurrently operating workers and multiple queued requests.
- Attenuating coordination relation: First-party per-pane mailbox stores every message, checks destination agent readiness through herdr and the screen guard, and defers/batches cross-lane deliveries until the target returns to idle; the duty loop retries delivery and watches lost worker panes.
- Feedback into subsequent S1 behaviour: On the next idle observation, `flushInbox()` injects a queued bundle into the recipient lane's model input; the recipient then incorporates the sender's reports/instructions on its next coding turn. A stalled/lost worker additionally triggers lead intervention rather than blind repeated prompting.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The readiness-dependent non-interruption relation explicitly regulates timing interference between simultaneous independent S1 sessions and returns deferred information only when each S1 can integrate it; ordinary address routing alone would deliver immediately without checking the working/blocked agent state.
- Function: Regulate interference from cross-lane/lead/duty messages arriving when a particular agent pane is busy, plus stale or vanished lane liveness.
- Disturbance / variety regulated: Interruption of working agents by asynchronous messages, competing pane readiness, delayed event reports and unobserved lost lanes.
- Decisive decision or feedback right: First-party constructor chooses whether to deliver immediately, queue until idle, batch, nudge or escalate based on explicit pane feedback and fixed policies; the duty model can additionally unblock WAITING cases but is not automatically summoned for every such decision.
- Decision owner: `send`/`flushInbox` and `dutyTick` first-party TS policies; not an independent reliably closed autonomous S2 agent for each conflict.
- Supporting / enforcement mechanisms: Herdr `agent_status` plus screen-idle guard, persistent per-pane inbox, idle thresholds 10/20/40 minutes, lost-pane detection, stop/resume and lead messages.
- Closure path: Lane/role message → observe destination pane state → queue if busy → duty polling observes idle → batch deliver; stale/lost reports → fixed nudge and escalation → lead can intervene.
- Boundary reachability: `dori send` calls `send()` in ordinary use; `dori up` creates a duty loop pane and `dutyTick` for periodic inbox flushing and lane status.
- Why this is / is not agent-owned: S2 coordination is a concrete first-party constructor, but scheduling thresholds and delivery choice are code policies; optional duty-agent unblocking does not prove general independent model control of the feedback loop.
- Evidence: [harness.ts#L85-L110](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts#L85-L110), [harness.ts#L225-L283](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts#L225-L283), [duty.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/duty.md).
- Basis: structural
- Confidence: high for constructor and state return; medium for autonomous optional duty intervention.
- Caveats: `herdr` is the external source of status; code itself mitigates interruption rather than proving fault-free scheduling across machines.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: The lead receives `[START]`, `[REPORT]`, `[READY]`, `[LOST]`, `[ESCALATE]` per independent worker lane, plus `[LOOP]` summaries with open lane count, backlog status, host capacity and stale-work findings; persistent lane/store records support a whole-current operational picture.
- Current-control decision scope: The configured lead model can create new briefs and assign them to separate lanes, redirect existing workers, decide whether to rebrief/restart lost work, judge READY evidence and authorize exact-head reviewed merges/closures while escalating product/irreversible choices to the human.
- Function: Lead-level current task and resource control of the whole multi-lane delivery operation.
- Disturbance / variety regulated: Simultaneous task commitments, user changes, blocked worker lanes, uncertain progress, failed reviews, stale ready tasks and host capacity limits.
- Decisive decision or feedback right: Model-driven lead assigns a brief to a new lane, examines ready evidence, decides next correction/restart/rebrief/escalation, and determines when to merge/close; human reserves irreversible/product decisions.
- Decision owner: First-party prompted, launched omo LEAD session; concrete resource bounds/backlog scheduling are separately enforced by deterministic TS loop.
- Supporting / enforcement mechanisms: `prompts/lead.md`, persistent lane logs/briefs, lead status/READY/LOST/ESCALATE messages, `dori start`, `send`, `done`, hourly capacity/load and decision gates.
- Closure path: Whole-current lane and task reports → first-party lead inbox → model decides launch/adjust/retry/close → CLI mutation changes lane state or directs workers → subsequent reports return to lead.
- Boundary reachability: `dori up` starts the lead omo with role prompt in supported CLI path; `tellLead` delivers lane and duty signals to its pane.
- Why this is / is not agent-owned: The lead decides task-specific cross-lane interventions beyond a static queue; quota and git gates are enforcement, not the basis for the A grade.
- Evidence: [cli.ts#L70-L87](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/cli.ts#L70-L87), [lead.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lead.md), [harness.ts#L116-L127](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts#L116-L127), [loop.ts#L310-L353](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/loop.ts#L310-L353).
- Basis: explicit + structural
- Confidence: high for decision right and reachable constructor; not a live throughput or guarantee-of-success assessment.
- Caveats: No inference that automated hourly loop alone is S3=A; lead model is required for that autonomy.

## S3* — Complementary audit

- State: A
- Claim being audited: A worker's implementation/PR is ready to merge at a specific head SHA, over and above its self-report and ordinary CI.
- Ordinary reporting path: Lane `ready()` carries final text and evidence link to lead; CI provides test-check status separately.
- Complementary access path: `review()` reads live PR head, instantiates a fresh non-interactive omo reviewer with `--no-session` and role-specific prompt instructing it to read the PR/diff, then parses CLEAR/BLOCK and stores a head-keyed review receipt.
- Independence boundary: Separate reviewer session and fresh prompt inspect the head's PR diff rather than accepting the worker's narrative; the same configurable model/provider might underlie both roles, so institutional/model-provider independence is not proven.
- Who acts on findings: Reviewer prints actionable HIGH/MEDIUM/LOW findings and BLOCK/CLEAR; lead can direct remediation, and `mergeGate()` refuses a missing/BLOCK/stale receipt or red/absent checks.
- Function: Independent first-party delegated source/diff challenge with hard return to the admission/merge path.
- Disturbance / variety regulated: Incorrect code despite worker claims, untested regressions, security defects, scope creep and post-review PR mutation.
- Decisive decision or feedback right: Dedicated review model autonomously judges evidence/failures against goal and emits binding verdict consumed by an exact-head merge gate.
- Decision owner: Fresh first-party-constructed reviewer omo agent for its audit verdict; deterministic git/check/receipt guard enforces the returned outcome.
- Supporting / enforcement mechanisms: `prompts/review.md`, `omo -p --no-session`, head SHA capture, `store.saveReceipt`, `gh pr checks`, `--match-head-commit` merge.
- Closure path: PR HEAD → new reviewer reads PR/diff → CLEAR/BLOCK recorded for SHA → lead/merge reads receipt and CI → block/repair/re-review or authorized exact-head merge.
- Boundary reachability: Normal user-visible `dori review owner/repo#N` CLI path, and `dori merge` requires its receipt; this is not repository-development CI only.
- Why this is / is not agent-owned: Independent model audit decision is separate from the implementer and first-party harness explicitly invokes it; CI checks are additional evidence, not the claimed autonomous auditor.
- Evidence: [harness.ts#L289-L355](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/harness.ts#L289-L355), [review.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/review.md), [store.ts](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/store.ts).
- Basis: explicit + structural
- Confidence: high for constructor, independent session and return gate; actual detection quality not measured.
- Caveats: The reviewer could share provider/model and GitHub access with the worker; `A` does not assert independent external operator or S3* audit effectiveness.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct forward-looking environmental intelligence→option selection→durable change in present organizational capability demonstrated.
- Disturbance / variety regulated: New user backlog tickets, issue status and host load are immediately actionable current work signals rather than longer-horizon environmental perturbations.
- Decisive decision or feedback right: Hourly loop chooses next eligible authorized task by static priority/capacity, and lead can prioritize work, but no first-party future strategy/adaptation right is established.
- Decision owner: Operator/lead choose what enters backlog; deterministic hourly loop executes present scheduling.
- Supporting / enforcement mechanisms: Import from labeled GitHub issues, backlog priorities, host load gates, task aging, retries, sync and stop controls.
- Closure path: Backlog/host observation → current lane start/held report; no separate prospective environmental option enters a capability-change decision and returns to S3.
- Why this is / is not agent-owned: Proactive scheduling and continuous task liveness do not by themselves constitute a prospective strategic S4 feedback loop.
- Evidence: [loop.ts#L310-L429](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/loop.ts#L310-L429), [hourly-loop.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/docs/hourly-loop.md), [lead.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lead.md).
- Basis: structural
- Confidence: medium-high at selected recursion.
- Caveats: Long-term product decisions by a human or software maintenance outside runtime are excluded.

### Absence scope

- Surfaces inspected: Lead/duty prompts, root CLI, task/backlog hourly loop, lane/receipt store, special-purpose mode references and README roadmap statements.
- Plausible first-party paths checked: Proactive hourly work, imported issues, stale-work audit, backlog priority, host resource telemetry and user approval questions.
- Why no material first-party path remains: All return to completion of current authorized tasks; no demonstrable prospective environment-to-capability adaptation decision closes inside this harness.

## S5 — Policy and identity

- State: —
- Function: No explicit closed ultimate-policy/identity decision process for the Dori organization, though human control and static boundaries are prominent.
- Disturbance / variety regulated: Irreversible decisions, product-scope changes, unsafe merges and unsupported work are controlled by permission/approval prompts and merge gates.
- Decisive decision or feedback right: Lead must ask human for irreversible/product decisions; the repository does not construct a binding mission/policy authority with a returned organization-wide policy-revision loop.
- Decision owner: Human operator outside the shipped autonomous policy process; developer-specified prompts and code enforce fixed gates.
- Supporting / enforcement mechanisms: Human approval rule in `lead.md`, bounded backlog decision queue, README one-voice and no-unasked-work rules, stale-review and CI fail-closed gates.
- Closure path: Question to human → human answer may enter backlog brief; this is local work authorization, not necessarily policy/identity revision for the whole system.
- Why this is / is not agent-owned: Respecting a parent's task authorization is not in itself a first-party ultimate-policy S5 process.
- Evidence: [lead.md](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/prompts/lead.md), [loop.ts#L65-L72](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/src/loop.ts#L65-L72), [README](https://github.com/sisyphuslabs/dori-superagent/blob/06c4600b77f6e81ed9bd5b706d736bec07cf27b1/README.md).
- Basis: explicit + structural
- Confidence: high for human gate, medium for scoped absence.
- Caveats: Human and organization may exercise a parent S5 outside this public runtime, which is not inferred or scored.

### Absence scope

- Surfaces inspected: Lead and duty policy prompts, CLI commands, backlog questions, review receipt/merge gates, lifecycle and optional-mode descriptions.
- Plausible first-party paths checked: Human decision gate, one-voice policy, no-unsolicited-work rule, exact-head merge authority and repo release decisions.
- Why no material first-party path remains: These are bounded instructions/approvals and current delivery controls without an explicit operating identity-level decision/return protocol.

## Distributed OSS parent arrangement

The open-source code uses a local human operator to grant product/irreversible decisions and external GitHub maintainers to approve PRs. Those are dependencies/limits, not proof of a Dori-owned or distributed OSS parent S5 at the assessed task-delivery recursion.

## Self-hosted and non-human modes

Works with self-hosted Herdr and configurable omo/model commands and can execute automatic pre-authorized hourly backlog starts. The model-driven lead and lane topology still depends on that agent runtime. No fully autonomous identity authority is established in a non-human mode.

## Recursion

Each independently briefed lane has a genuine separate agent loop and task results; lead governs the collection. The CLI's duty ticks, inbox records and review receipts are channels/constructors, not additional full viable S1 units. Dori mode is an optional related deployment, not an imported whole other first-party governance organization.

## Variety and escalation

Parallel lanes amplify task throughput; per-pane inbox, herdr state and host resource limits attenuate message/liveness variety. Duty escalates lost/stalled tasks; lead can rebrief/restart and forward unresolved choices to a human. Fresh audit verdict and exact-head CI gate reject unverified PR merges and invite correction.

## Evidence gaps

Source-pinned, first-party structural review only. The local environment lacks Bun, Herdr and the configured omo provider, so no runtime end-to-end execution or tests were claimed. The reviewer may use the same model/provider, audit effectiveness and safety of merged output are unmeasured, and S4/S5 absence is only at the stated runtime boundary.

## Verdict

**Propose inclusion.** Shipped separate coding-agent lanes establish S1=A; a first-party cross-pane coordination constructor establishes S2=C; the prompted lead governs whole-current lane commitments as S3=A; a fresh specialized reviewer session with receipt-enforced merge closure establishes S3*=A. Present-work backlog scheduling and fixed policy/human permissions do not evidence a separate S4 or S5 decision process.
