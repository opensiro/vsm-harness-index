---
harness_id: mas-office
project_name: MAS Office
repository: https://github.com/weixijia/mas-office
review_ref: 5a768ecac2260ba4cb21c5450593ad1b7d190041
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# MAS Office

## Review boundary

- System in focus: the installed MAS Office team runtime (`mas-office up`), locked `mas/structure` team definition, project-local source/work/result files, lead and parallel real model-backed Claude Code/Codex role sessions, inbox and checker loop.
- Purpose and identity: execute a user's delegated multi-role research/decision task and produce a source-attributed, independently checked answer through controlled concurrent roles and configurable human gates.
- Relevant environment: search and source pages from the Internet, each role's tool permissions and outputs, evolving role tasks/checkpoints, running provider sessions/quotas, user objectives and approval decisions.
- Standard-distribution boundary: `packages/runtime/src/engine`, its Claude/Codex adapters; `packages/node/src/team`, `src/verify`, `src/policy`, CLI, runtime server/protocol, lockable team structure; vendor model internals and accounts are external. Read-only visualization/sdk integration and sample demos are not themselves agents.
- Credited operating / distribution surfaces: npm-installed `mas-office` + `mas-office-runtime`, `mas-office up`, signed/locked team, `project.js` project scheduler/checker/lead, `compileRole` / `decideTool` policies, separate clean-context model reviewers, source-card/claim-verdict evaluation and human callback inbox.
- Adjacent first-party surfaces excluded from ownership: replayed `mas-office demo` and `examples/price-compare` fixtures, future `mas-office-terminal` package, `eval/` research and development/test CI, generic SDK protocol events from arbitrary *external* frameworks, public OSS maintainer governance and the optional no-code kit when it runs without installed runtime.
- First-party operating / deployment modes considered: standard locked team `up` with staged multi-role execution and a real model-backed lead; configured checker/reviewer and per-claim verification; human plan/stage/final gates, approval delegation and needs-you resolution; follow-up rounds and role stall recovery; view-only observer with no attached runtime not credited.
- Recursion level: one user-owned local research/decision team with several S1 role sessions and lead coordination, with the legitimate user as a parent for substantive current task/stage decisions.
- Reviewed revision: `5a768ecac2260ba4cb21c5450593ad1b7d190041`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The open-source zero-dependency `mas-office` package provides protocol, team design/permission compiler, event/reducer, CLI, verification and panel. The separate installable `mas-office-runtime` starts real Claude Code and Codex sessions. The user defines and locks a team: roles, staged dependencies, backend, role-specific tools/writable files, reviewer targets, checker thresholds, max parallelism, approval delegation and human checkpoints. An unlocked or signature-changed structure is refused at runtime. This is a binding run contract, not by itself S5's ultimate-identity policy issue pathway.

A model-backed Lead receives the user's task, returns per-role briefs and high-level plan, and later synthesizes a source-tagged result. A deterministic engine validates the Lead's output and schedules role work subject to stage DAG and process pool. Parallel worker roles work with separate scoped output paths, with write/path checks enforced through `decideTool` and backend restrictions. A separate reviewer role checks targets' work in an isolated prompt/clean context, can return it for rework and escalates beyond bounded rounds. After the Lead writes the result, `verify` parses claim tags, fetches source-link health deterministically, and invokes separate checker actors to judge actual claims against source cards; contradictions trigger a person-facing blocking flag. Human gates may stop, hold or send back current work. Stall recovery may ask the Lead to retry/replan or escalate to the user, changing subsequent active commitments.

This installed runtime is separate from a mere visualization/replay adapter: external producers may emit simulated events into MAS Office, but they do not supply first-party decisions at this declared recursion. Model inference is outsourced to the user's authenticated Claude/Codex accounts, while role lifecycle, source evidence transport, permission gating and return of current-control decisions are first-party.

Evidence routes: [README.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/README.md); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md); [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/node/src/team/compile.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/compile.js); [packages/node/src/team/decide.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/decide.js); [packages/node/src/verify/verdicts.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/verify/verdicts.js).

## Operational model

Researchers/finder roles are independently reasoning S1 cells. Role-scoped writes, staged dependencies and deterministic pool/access policy attenuate interference among concurrent cells (S2 constructor path), but do not themselves establish autonomous S2. The Lead has a whole-run view and chooses current briefs and recovery responses (S3 autonomous), while configured substantive human checkpoints can send whole stages back, release or stop them (S3 parent). Model-backed checker sessions independently read source cards and worker output to give adverse verdicts, which cause rework or human escalation (S3*). Neither a provider's Web access nor a fixed team policy signature supplies autonomous future intelligence or a closed issue about ultimate mission/identity.

## S1 — Operations

- State: A
- Function: Perform one delegated research/decision subtask by searching/fetching external information, writing scoped source cards and work outputs, and adapting to encountered evidence.
- Disturbance / variety regulated: Conflicting search results, variable source availability, ambiguous user criteria, incomplete facts and tool-access failures.
- Decisive decision or feedback right: Select research strategy, tools, evidence and a work artifact in a role's approved envelope rather than following a wholly fixed sequence.
- Decision owner: Real model-backed `claude-code` or `codex` role session created under a first-party compiled job/brief; the model/provider's own internals are not credited as MAS Office-specific control.
- Supporting / enforcement mechanisms: `compileRole`, `decideTool`, model adapter, tool allow/ask/deny and source-card output format, events/transcript, scoped writable files, stage task envelopes.
- Closure path: Worker's model turn writes source/work files and returns summary; runtime records task completion/handoff and passes results to dependent checker and Lead; a rework request returns to the same role.
- Boundary reachability: Standard `mas-office up` with a locked team and authenticated Claude Code/Codex CLI starts actual model sessions; no author-supplied custom adapter needed for the normal path.
- Why this is / is not agent-owned: First-party role composition creates a context-sensitive agent task with real model decisions; the scheduler and permission compiler enforce constraints but cannot select external evidence or conclusions by themselves.
- Evidence: [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/runtime/src/backends/claude.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/backends/claude.js); [packages/runtime/src/backends/codex.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/backends/codex.js); [packages/node/src/team/compile.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/compile.js); [README.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/README.md).
- Basis: structural
- Confidence: high for normal installed runtime; no live provider invocation
- Caveats: Individual provider model reasoning is an external execution dependency and no benchmark of answer quality has been performed.

## S2 — Coordination

- State: C
- Function: Attenuate cross-role source/output conflicts and prevent premature/competing stage or tool execution across concurrently working S1 actors.
- Disturbance / variety regulated: Concurrent agents trying to overwrite another role's results/instructions, stage consumers reading unfinished dependencies, competing access to shared process pool or unapproved tools.
- Distinct S1 units: Multiple real parallel finder/researcher and reviewer role sessions in distinct logical work cells of one team; different model backends are supported.
- Inter-S1 disturbance: One role could corrupt another's work/source path, read unready input, or compete for limited execution slots if allowed unconstrained shared writes and reads.
- Attenuating coordination relation: `compileRole` assigns per-role writable paths, `decideTool` rejects out-of-scope writes before tool execution, staged `runStage` waits for preceding work/review before next group consumes results; process-wide semaphore bounds competing turns.
- Feedback into subsequent S1 behaviour: A denied foreign write returns to its actor as a policy refusal, and pending downstream stages start only after upstream work/verification has finished or resolved through human gate.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Writable-per-role exclusion is a concrete mutual-interference attenuator for independently active sessions, alongside dependency-staged admission; a generic event log or forwarder alone would not qualify.
- Decisive decision or feedback right: Determine if an agent may modify a particular shared-workspace path and when mutually dependent role work is allowed to proceed.
- Decision owner: First-party deterministic permission compiler, policy engine, role stage scheduler and shared semaphore; the Lead does not hold an autonomous function-specific anti-conflict decision right.
- Supporting / enforcement mechanisms: Compiled role writable glob, deny rules, Claude/Codex sandbox permission checks, group ordering, per-project role completion and process parallelism limit.
- Closure path: Scope violation is denied; in-bounds role produces its own artifact; dependency completion and reviewer results release the next stage's roles, avoiding cross-role destructive interference.
- Boundary reachability: Bundled `up` installs and applies compiled roles and `decideTool` at runtime, including locked team inputs, without requiring a third-party S2 implementation.
- Why this is / is not agent-owned: An actual S2-specific relation is implemented and shipped but current enforcement choices are fixed deterministic logic; no autonomous dedicated S2 controller observed.
- Evidence: [packages/node/src/team/compile.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/compile.js); [packages/node/src/team/decide.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/decide.js); [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md).
- Basis: structural
- Confidence: medium-high within verified role/permission boundaries
- Caveats: The documentation acknowledges Codex sandbox timing limitations and not every read may be forcibly fenced; S2 conclusion is limited to concrete write/role interference witness.

## S3 — Inside-and-now control

- State: A(P)
- Function: Coordinate and adapt present whole-run role briefs, stage commitments, stalled workers, reviewer returns, and the decision to publish/rework/stop a source-checked result.
- Disturbance / variety regulated: Conflicting/current tasks, unresponsive roles, checker objections, unavailable resources, user requirements and escalating bounded review rounds.
- Whole-system current view: Model Lead receives team structure, user task, stage status, per-role summaries and handoffs, failures, reviewer findings, run checkpoints and global current work state.
- Current-control decision scope: Lead chooses per-role briefs and response to stalls (retry, replan or ask-human), produces a whole-run plan/write-up and can direct work/revisions within the locked team; human parent decides blocking stage and plan/final gates, whether workers must redo work and whether to stop.
- Decisive decision or feedback right: Choose current task allocations in briefs/repair interventions and whether major current stage commitments advance or return.
- Decision owner: Base: model-backed Lead session acting inside source-native run control; parent: authorized user acting on substantive plan/stage gate and checker objections via tokened inbox, not a generic shell permission prompt.
- Supporting / enforcement mechanisms: `plan()`, `runStage()`, `onStall()`, `runGate()`, `writeUp()`, role lifecycle events, source checks, run state, human command broker.
- Closure path: Lead's current briefs control future role turns; stalled role leads to retry/replan with new brief; user can release, send stage back or stop so subsequent run stages change; claim-check flags block until user chooses fix/publish/stop.
- Boundary reachability: Supported locked `up` mode always runs the model Lead and includes user-facing stage/final gates and inbox when configured; the same installed engine routes them.
- Why this is / is not agent-owned: The Lead exercises model-backed discretion on whole-run briefs and intervention, not merely tool routing. Separate legitimate parent decisions control substantive stage/final acceptance, while role/parallel limits are enforcement support.
- Evidence: [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/runtime/src/engine/broker.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/broker.js); [packages/node/src/policy/delegate.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/policy/delegate.js); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md); [README.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/README.md).
- Basis: structural, normal installed runtime
- Confidence: medium-high
- Caveats: Role topology is fixed by the locked human-authored design; no arbitrary autonomous organization redesign is implied. A simple single-tool approval does not qualify as parent S3.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed Lead | New run, stage observations or role stall | Whole-run briefs/replan/retry and write-up influence subsequent workers | `packages/runtime/src/engine/project.js` |
| Parent (`P`) | Authorized user | Blocking plan/stage gate, failed checker flag or review escalation | Human fix/continue/stop verdict returns through inbox and changes run progress | `project.js`, `broker.js`, `README.md` |

## S3* — Complementary audit

- State: A
- Function: Independently challenge worker outputs and Lead's source-attributed answer against direct work files and source cards before final acceptance.
- Disturbance / variety regulated: Overconfident or unsubstantiated research claims, wrong prices/dates, flawed worker reports and missing evidence despite a plausible summary.
- Claim being audited: A role's submitted work supports the user decision and the Lead's tagged output claims are backed by cited sources.
- Ordinary reporting path: Worker's own work file, source card/summary, Lead `outputs/result.md` with `claim` tags and the normal orchestration transcript.
- Complementary access path: A separately instantiated reviewer with clean context reads actual worker files and source cards; after write-up another checker turn reads raw result claims and independent sources, while deterministic URL health checks support the same audit.
- Independence boundary: Checker/reviewer has separate role/session and clean prompt context; raw source cards/work/result files rather than worker self-report; model provider can be same or different and model reliability is not assumed.
- Who acts on findings: The engine parses checker verdicts, sends `revise` findings to the original target for rework, escalates exceeding rounds to human, and flags contradicted/unknown claims in the human inbox; fix/stop/publish choice changes the result path.
- Decisive decision or feedback right: Substantively decide whether target work/answer claims are accepted, need revision or must be escalated based on independently supplied source evidence.
- Decision owner: Separate real model-backed reviewer/checker session; deterministic source URL checking, verdict parsing and flag thresholds only enforce and transport the judgment.
- Supporting / enforcement mechanisms: `reviewerOf`, `cleanContext`, `parseReviewBlock`, `verdictEvents`, `mergeLanes`, `shouldFlag`, fixed rounds and human escalation path.
- Closure path: Reviewer verdict returns to runtime; revises role brief and new attempt or raises human flag; checker statuses/contradictions feed Lead write-up repair or publish-with-warning decision.
- Boundary reachability: Shipped standard `mas-office up` automatically opens reviewer role when configured and runs claim checkers during `verify`; stock example demonstrates this configured mode without user-built reviewer plugin.
- Why this is / is not agent-owned: Independent model reviewer makes an evidence-dependent judgment; a URL-up/down check or static threshold alone would not establish S3*.
- Evidence: [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/node/src/verify/verdicts.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/verify/verdicts.js); [packages/node/src/verify/claims.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/verify/claims.js); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md).
- Basis: structural
- Confidence: medium-high for available configured independent reviewer
- Caveats: Reviewer may share vendor/model with author, no empirical checker reliability or cross-provider independence shown; no checker in a team configuration means no S3* on that mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: No dedicated first-party outside-and-then organizational intelligence/adaptation loop is shown for the installed research/decision team.
- Disturbance / variety regulated: Emerging external sources, markets and task facts are read during research, but future viability changes of the organization are not monitored as a separate function.
- Decisive decision or feedback right: Would choose prospective structural/capability adaptations from external change and feed them into current team operation; no actor with that right in the installed runtime identified.
- Decision owner: No installed S4-specific owner; finder roles research user tasks and Lead responds to current work, not future team viability.
- Supporting / enforcement mechanisms: WebSearch/WebFetch role tools, source cards, source-health evaluator and team setup are task evidence/current controls.
- Closure path: No ongoing outside signal → future organization option → accepted change in team capabilities/roles → return to S3 current work loop demonstrated.
- Why this is / is not agent-owned: Open-web research for a product comparison or trip is S1 work; future adaptation requires a distinct prospective choice/return not shown.
- Evidence: [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/node/src/verify/sources.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/verify/sources.js); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md); [README.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/README.md).
- Basis: bounded source absence
- Confidence: medium
- Caveats: Human redesign of the locked team or a new external research role could add adaptation, but that user-driven extension is not an installed autonomous S4 loop.

### Absence scope

- Surfaces inspected: Lead planning, source-searching roles, checker and URL evidence pipelines, team design/locking, follow-up and runtime restart.
- Plausible first-party paths checked: outside research, user changes to team structure, source update checks and follow-up rounds.
- Why no material first-party path remains: those paths perform present research or human setup, with no proactive external prospective intelligence actor owning selected adaptation and feedback to the current team.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity-policy issue resolution and returned ruling distinct from team design, tool rules or current stage decisions is demonstrated.
- Disturbance / variety regulated: Questions of the team's enduring purpose/identity or conflict between current delivery and future adaptation could require S5; ordinary plan and permission requests are task-level.
- Decisive decision or feedback right: A triggered identity-level ultimate policy judgment binding later operation would be required; the observed signature/lock is an existing owner-selected configuration gate.
- Decision owner: The human is legitimate owner of team setup and tool policies, but no shipped issue-triggered S5 parent authority transaction and binding changed ultimate mission is shown.
- Supporting / enforcement mechanisms: `structure.locked`, signed team signature, tool vocabulary, delegation rules, bounded budgets and default-deny policies; these bind existing rights but are not decisive identity-level dispute resolution.
- Closure path: Tampered/unlocked structures refuse execution until relocked, but that is configuration integrity rather than an identity/policy issue → legitimate ultimate adjudication → returned change in governing direction.
- Why this is / is not agent-owned: A static role constitution, policy file or human approve/deny gate alone cannot supply S5; the system's owner controls present tasks and permission envelopes, not a reconstructed ultimate-purpose return loop.
- Evidence: [packages/runtime/src/engine/project.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/runtime/src/engine/project.js); [packages/node/src/team/sign.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/team/sign.js); [packages/node/src/policy/delegate.js](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/packages/node/src/policy/delegate.js); [docs/design/runtime.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/docs/design/runtime.md); [README.md](https://github.com/weixijia/mas-office/blob/5a768ecac2260ba4cb21c5450593ad1b7d190041/README.md).
- Basis: bounded source absence
- Confidence: medium
- Caveats: An adopting organization may externally decide ultimate identity or change the template; that recursion is excluded from the installed team's ownership.

### Absence scope

- Surfaces inspected: team structure lock/relock/signature, operator role/approval delegation, human gates, result flags, protected-file/tool policy, OSS governance and future roadmap.
- Plausible first-party paths checked: changed team design requiring re-lock, Lead escalation, human needs-you policy and final result approval.
- Why no material first-party path remains: evidence shows enforcing or amending existing runtime/team constraints and task-level decisions, not a genuine identity/ultimate-policy question with recorded authoritative resolution returned to future and present governance.

## Distributed OSS parent arrangement

Different independent npm installations and external framework event producers share no bound S5 collective authority merely through the event protocol. The user's tokened local inbox is a legitimate parent for *current* decisions, not proof of a common organization-wide identity-policy arbiter. Public maintainer/release decisions lie in a separate recursion.

## Self-hosted and non-human modes

Local `up` runs real Claude/Codex subprocesses and binds a loopback tokened panel. Human checkpoints and approval delegation coexist with autonomous Lead decisions, and a team without a checker does not inherit S3* from demo documentation. No-code kit and read-only event replay are adjacent modes, not evidence that the `up` runtime delegates S4/S5.

## Recursion

The installed project team comprises separate S1 researcher/finders, concrete S2 deterministic scoped write/dependency coordination, an autonomous S3 Lead with optional substantive human parent mode, and optional independent model source/claim S3*. Provider platforms and user enterprise governance are outside the assessed VSM unit.

## Variety and escalation

The model workers absorb external source/task variety; role write guards and stage dependencies attenuate inter-worker interference. Failed/reviewed work returns to the same cell through source-specific corrections. The model Lead changes current briefs/recovery choices and the user can release, send back or stop blocked stages/claims. No separate S4 or S5 governing return has been established.

## Evidence gaps

Pinned-source review only, not a live authenticated Claude/Codex session or measured quality trial. Reviewer actual independence/effectiveness and Codex sandbox timing are bounded uncertainties. S4/S5 negative findings are restricted to the shipped installed runtime and normal configured modes, not possible external organizational extensions. This is a descriptive VSM decision-right map, not a product decision for the maintainer.
