---
harness_id: sloop
project_name: Sloop
repository: https://github.com/hamish-mackie/sloop
review_ref: 0d86a9193e80e9527f6ad3b09904030d6a2877ed
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Sloop

## Review boundary

- System in focus: Installed Sloop Rust daemon and CLI operating one repository/project's ticket-run workflow, including its shipped default agent/review integration.
- Purpose and identity: Execute human-authored coding tickets with isolated agent worktrees and evidence-grounded review/merge rules.
- Relevant environment: Git repository, external agent CLI processes, local operator, configurable execution windows and test commands.
- Standard-distribution boundary: First-party dispatcher, ticket/trigger store, run supervisor, flow stages/evidence replay, shipped default configurations and CLI; supported external agent providers are integrated workers but not first-party policy owners.
- Credited operating / distribution surfaces: Local supervised agent-run mode, operator project controls, default review flow and configurable project rules.
- Adjacent first-party surfaces excluded from ownership: Release CI, developer tests, documentation-only simulations, external GitHub maintainers and hypothetical higher-level agents using Sloop's socket API.
- First-party operating / deployment modes considered: Default build-review-sync-verify-merge flow, review-free train alternative, and operator-governed local daemon work queue.
- Recursion level: One local repository/project ticket portfolio with independently run coding agents as S1 units; local operator is the parent for project-level controls.
- Reviewed revision: 0d86a9193e80e9527f6ad3b09904030d6a2877ed.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

A Rust daemon owns one dispatcher, time/window/capacity and ticket claim gates, and each launched run executes a frozen flow over a dedicated worktree. Stage outcomes are derived from process exits, commit evidence, scoped reported reviewer verdicts and Git integration checks; failure edges replay through recorded stage evidence after interruptions. External coding agents are spawned as scoped subprocesses rather than replaced by a Sloop-internal planning model. A distinct review subprocess runs tests and reads the diff in the standard default flow. A local operator can post and hold tickets, inspect whole-project status and author persistent workflows. [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md); [README](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/README.md); [dispatcher](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/dispatcher.rs); [default flow](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/flows/default.yaml); [flow replay](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/walk.rs).

## Operational model

Coding subprocesses implement one ticket each. Deterministic coordination prevents duplicate work claims and stale final-branch integration; the local operator regulates active and queued work, and owns standing rules for admission/review/merging. A built-in review stage offers a separate model-backed complementary judgment over direct worktree evidence. The daemon deliberately does not supply its own general planning, conversation, memory or future-adaptation agent.

## S1 — Operations

- State: A
- Function: Execute model-authored coding changes requested by a committed ticket, with scoped tools and feedback from the run worktree.
- Disturbance / variety regulated: Source changes, ticket requirements, failed commands and task ambiguity require the running agent to decide edits and tools.
- Decisive decision or feedback right: Choose how to change the code and what to commit within the dispatched ticket; the scheduler does not plan the change.
- Decision owner: The model-backed worker subprocess launched for the ticket via the supported external agent CLI target (Claude Code, Codex or OpenCode).
- Supporting / enforcement mechanisms: First-party ticket admission, worktree creation, prompt/agent driver, durable run and evidence log, process supervision and commit check.
- Closure path: Agent receives its ticket and command observations, edits and commits in its worktree; Sloop observes Git evidence and advances or returns work based on flow verdicts.
- Boundary reachability: The shipped init config exposes working provider targets and the default flow has an actual agent stage; the daemon launches the selected provider in a first-party supervised run.
- Why this is / is not agent-owned: The provider-backed coding agent chooses implementation details; Rust gate decisions enforce process and Git conditions but cannot independently write task-specific code.
- Evidence: [README](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/README.md); [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md); [default flow](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/flows/default.yaml); [run driver](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/driver.rs); [worker execution](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/worker/mod.rs).
- Basis: structural
- Confidence: high
- Caveats: No agent process or live model outcome executed during this assessment; external providers supply the operating model.

## S2 — Coordination

- State: C
- Function: Limit interference among multiple concurrently dispatched coding units competing for project resources and integration of a changing shared branch.
- Disturbance / variety regulated: Unbounded concurrent workers can oversubscribe process capacity, duplicate one ticket claim, or race against branch changes before merge.
- Decisive decision or feedback right: Select only eligible trigger-backed tickets for currently available capacity; refuse duplicate claims, and force re-sync/re-verify of a branch after an integration race.
- Decision owner: Deterministic dispatcher and configured flow gates own the immediate coordination policy. An autonomous owner of changing inter-worker priorities is not supplied.
- Supporting / enforcement mechanisms: One admission dispatcher, conditional lease, max-parallel gate, dependency checks, isolated run branches and ff-only merge train.
- Closure path: Blocked tickets remain unspawned and become eligible after a dependency merges or a slot opens; stale sync/merge races cause the flow to re-enter sync and verify rather than silently integrate stale work.
- Boundary reachability: These checks run in the standard daemon and packaged flows with no plugin or invented external coordinator required.
- Why this is / is not agent-owned: The code applies configured coordination rules. A developer would need to compose an autonomous agent that can decide broader inter-worker adjustments, so the evidenced function-specific constructor is C rather than A.
- Distinct S1 units: Separate agent subprocesses with their own tickets, model context and Git worktrees.
- Inter-S1 disturbance: Contending for the same daemon run slots and common project branch integration while dependencies may be unsatisfied.
- Attenuating coordination relation: A single capacity/claim gate and source-aware sync/ff-only integration controls suppress duplicated or unsafe concurrent work.
- Feedback into subsequent S1 behaviour: Released capacity and blocker completion trigger later work; a failed fast-forward makes the worker flow re-sync and reverify before another merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The specific interference being attenuated is double admission and stale integration of simultaneously active workers, evidenced by lease and merge-race rules rather than messaging alone.
- Evidence: [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md) (dispatcher/claim/merge); [dispatcher](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/dispatcher.rs); [eligibility](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/eligibility.rs); [merge train](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/flows/train.yaml); [flow replay](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/walk.rs).
- Basis: structural
- Confidence: medium
- Caveats: This is deterministic multi-worker resource/integration coordination, not model-owned discussion or general autonomous inter-agent negotiation.

## S3 — Inside-and-now control

- State: P
- Function: Allow the local project operator to regulate the presently running and pending job portfolio.
- Disturbance / variety regulated: Work can stall, overrun allocated hours, fail validation, or no longer match the operator's current priorities.
- Decisive decision or feedback right: View current project tickets and runs; choose to hold, release, cancel, retry, pause/resume dispatch or queue selected work.
- Decision owner: The operator of the local Sloop installation in the parent control mode. The daemon enforces configured scheduler rules, but does not autonomously choose substantive priorities.
- Supporting / enforcement mechanisms: Project show/status, output and stage evidence, authenticated operator socket, run cancellation and hold/ready state transitions.
- Closure path: An operator's action changes durable ticket/daemon state and subsequent dispatch eligibility or live run disposition.
- Boundary reachability: The operator CLI/socket and show/hold/ready/pause/cancel commands are first-party shipped controls.
- Why this is / is not agent-owned: The decision to hold or release task work in response to the whole portfolio belongs to the operator; rate limits and triggers are deterministic supporting machinery.
- Whole-system current view: Sloop show exposes project tickets, active runs, blocked/dependent tickets and stated scheduling reasons across the one local project.
- Current-control decision scope: Current admission, cancellation, pause/resume and task commitments for the local work portfolio.
- Evidence: [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md); [CLI](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/cli.md); [eligibility](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/eligibility.rs); [dispatcher](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/dispatcher.rs).
- Basis: structural
- Confidence: medium
- Caveats: Operator control is limited to the local running project. A scheduled worker's routine retries or a single narrow override alone are not the parent S3 evidence.

## S3* — Complementary audit

- State: A
- Function: Obtain separately produced evidence-based review of an implementer's completion claim before integration.
- Disturbance / variety regulated: An agent can produce a successful exit or commits with an incorrect or incomplete change.
- Decisive decision or feedback right: A separate reviewer agent directly inspects the diff and task, runs relevant tests and issues a reported pass/fail judgment; the deterministic flow accepts/rejects according to that report.
- Decision owner: A fresh review-stage model subprocess, distinct from the implementation-stage worker and given a separate review prompt.
- Supporting / enforcement mechanisms: Readonly reviewer tool restriction (Bash rather than Write/Edit), review-stage socket token, mandatory reported verdict, append-only stage evidence and return_to build on failure.
- Closure path: A reported failure re-enters build with a bounded retry; no verdict is itself a failure, and integration follows only after review and further required checks pass.
- Boundary reachability: The init-supplied default flow includes review with a separate Claude execution stage and concrete review prompt; an optional train flow deliberately omits review.
- Why this is / is not agent-owned: The reviewer chooses its substantive adequacy conclusion from the diff, task and tests; the flow's code only enforces and records that decision.
- Claim being audited: A build-stage agent's assertion that committed code meets the posted ticket.
- Ordinary reporting path: Build agent transcript, exit code and new-commit evidence.
- Complementary access path: Independent review stage reads current Git diff against default branch, task brief and tests rather than only the worker's final message.
- Independence boundary: A second subprocess/prompt and output channel with limited tools; a deployment can still use the same provider/model and no external human review is implied.
- Who acts on findings: The first-party flow returns a negative verdict to build for correction; passing evidence is prerequisite to downstream sync/verify/merge.
- Evidence: [default flow](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/flows/default.yaml); [review prompt](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/prompts/review.md); [flow replay](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/walk.rs); [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md); [review panel](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/panel.rs) (optional reviewer quorum).
- Basis: structural
- Confidence: high
- Caveats: Conditional on the packaged default review flow; the explicitly review-free train mode does not inherit this audit claim.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped function-specific agent path was found to observe external futures, generate prospective adaptation alternatives and return a selected option into future system capability.
- Disturbance / variety regulated: Changing providers, user needs and integration constraints would require prospective redesign beyond one ticket.
- Decisive decision or feedback right: No supported actor owns a future-oriented organizational adaptation judgment inside the daemon.
- Decision owner: Not established at the reviewed runtime boundary.
- Supporting / enforcement mechanisms: Fixed retries/cooldowns, status histories, editable flows and configured provider targets support current operation but do not select adaptive policy.
- Closure path: Not established for a prospective S4 decision; operator-authored changes are outside the automatic run scope.
- Why this is / is not agent-owned: The project expressly presents itself as a deterministic scheduling kernel without planning or memory; observable cooldowns are short-term operational recovery, not a prospective capability-learning loop.
- Evidence: [operating concepts](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/concepts.md); [configuration](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/configuration.md); [dispatcher](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/daemon/dispatcher.rs); [flow replay](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/walk.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: A higher-level product may use Sloop APIs to construct an S4 function, but this is not a shipped Sloop-owned path.

### Absence scope

- Surfaces inspected: README, concepts, configuration, scheduler/dispatcher, flow engine, ticket/run history and runtime commands.
- Plausible first-party paths checked: Vendor retry cooldown, recurring triggers, replay of evidence, runtime recovery, configurable worker models and authored flow file.
- Why no material first-party path remains: Each documented path executes fixed/current rules or a human-authored future change; none generates and authoritatively selects a prospective adaptation from outside-and-then evidence in the supported daemon.

## S5 — Policy and identity

- State: P
- Function: Set the standing project workflow and acceptance policy that defines which jobs Sloop may run and which outcomes may be integrated.
- Disturbance / variety regulated: The local owner's evolving expectations about provider authority, quality gates and execution windows must continue to constrain future automatic runs.
- Decisive decision or feedback right: Select and author durable project config/flows: targets, allowed hours/capacity, test command, reviewer requirement, retry policy and merge conditions.
- Decision owner: The legitimate repository/project operator editing committed policy/configuration before dispatch.
- Supporting / enforcement mechanisms: Versioned YAML flow/config files, flow parsing/validation, per-run flow snapshot, immutable stage/evidence replay, daemon policy gates.
- Closure path: Owner commits/loads the standing policy; daemon validates the flow and records a snapshot at run admission; later agent work, reviewer stage and merges obey the selected policy.
- Boundary reachability: The installed init scaffolds config and default flow files; CLI posting and daemon startup validate/apply this owner-authored policy.
- Why this is / is not agent-owned: A worker chooses edits but cannot redefine the authorized task/merge policy in its existing admitted flow; the policy authority remains with the local operator.
- Identity / ultimate-policy issue: What is acceptable autonomous coding activity and which evidence is required before Sloop calls project work complete.
- Ultimate authority in each claimed mode: Local project owner/operator, not the provider subprocess or OpenSiro reviewer.
- Return-to-operation path: Persisted config/flow → validation and admitted flow snapshot → enforced run stages, acceptance verdicts and subsequent dispatch.
- Evidence: [README](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/README.md); [configuration](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/configuration.md); [CLI](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/docs/cli.md); [default flow](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/defaults/flows/default.yaml); [flow replay](https://github.com/hamish-mackie/sloop/blob/0d86a9193e80e9527f6ad3b09904030d6a2877ed/src/flow/walk.rs).
- Basis: structural
- Confidence: medium
- Caveats: This claim is scoped to the local project constitution and durable acceptance policy, not a claim of separate public OSS governance/identity inside the daemon.

## Distributed OSS parent arrangement

The owner of the local installation and its committed workflow settings is the parent of this assessed project cell. Multiple contributors to the upstream Sloop repository do not, by themselves, establish organizational parent control over remote users' private ticket runs.

## Self-hosted and non-human modes

Sloop operates as a local daemon and can dispatch unassisted ticket jobs when configured external worker binaries are present. The shipped default flow has an independent review subprocess, while the explicitly available train flow omits it; actual flows are frozen per admitted run. Interactive control through the operator socket remains a distinct supported mode.

## Recursion

Each ticket's agent and worktree is an operational unit. The dispatcher regulates shared capacity and integration among those units. Local project owner decisions govern the whole work queue and durable workflow policy, without implying autonomous S3/S5 in the deterministic daemon.

## Variety and escalation

The daemon admits work only after dependency, trigger, time, capacity, lease and source checks; flow failures re-enter prescribed stages within budgets. Operator-level hold/retry/pause and changes to standing flow requirements are explicit parent interventions. Missing reviewer verdicts fail rather than turning into assumed success.

## Evidence gaps

Primary-source structural review only; no live model execution, deployed worker or test suite from Sloop was run. Review can be disabled by selecting train mode, so S3* is claimed only for the supported default reviewed distribution. S2 is bounded to resource and integration interference, not higher-level semantic multi-agent coordination. The S4 absence conclusion is bounded to the shipped daemon rather than hypothetical users of its socket API.
