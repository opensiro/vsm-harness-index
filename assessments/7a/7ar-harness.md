---
harness_id: 7ar-harness
project_name: 7ar harness
repository: https://github.com/7ar-chat/harness
review_ref: 89edbffde74f4aa2c7675dc07615f26ab76cae91
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# 7ar harness

## Review boundary

- System in focus: the installable Go harness and its bundled factory/team-product modes, not the organizational governance of the upstream GitHub repository.
- Purpose and identity: run model-directed work in sandboxed agent sessions and, when enabled, coordinate unattended coding tasks into reviewed pull requests within a human-owned project.
- Relevant environment: user/projects, model providers, sandbox filesystem, GitHub repository and CI, cooperating agent sessions, task store, authenticated project members and optional Postgres/Redis infrastructure.
- Standard-distribution boundary: the shipped root Go engine/facade, `ai/agent` loop, `features/factory`, `app/product`, shipped hosts and the `harness-web` composition. Optional factory, team, second-reviewer and auto-merge modes are credited only with their actual enablement and guards.
- Credited operating / distribution surfaces: [runtime and composition](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features_factory.go), [factory task service](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/tasks/service.go), [PR integration loop](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/forge/loop.go), [independent-review gate](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/review/review.go), [team supervisor](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/supervisor.go), [project ownership routes](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/team_projects.go).
- Adjacent first-party surfaces excluded from ownership: development `*_test.go`, fake forge/model integration fixtures, benchmark/SWE-bench evaluator, contributor CI and releases, docs describing future deployments, the external GitHub/CI and provider organizations; none supplies the harness's own decisions. Tests corroborate wiring but are not production evidence.
- First-party operating / deployment modes considered: `harness` CLI single agent; `harness-web`/embedded session; `harness-web -team` with projects and supervisor; `FACTORY=1` task automation with delegate/forge/policy; distinct `FACTORY_REVIEW_MODEL` versus default same-model review; human-merge versus task `AutoMerge`; optional lessons, Postgres/Redis, OpenSandbox or local backend.
- Recursion level: one installed product/project spanning several S1 agent sessions and factory tasks; delegated roles/threads are subordinate operational cells, not separately proven viable systems.
- Reviewed revision: `89edbffde74f4aa2c7675dc07615f26ab76cae91`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The root facade composes a model/tool agent loop, event stream, approvals, steering, sandbox and persistent store. CLI, web, API and worker hosts drive the same engine. The optional first-party factory wires task admission/dependency/claim state, model-backed task sessions, role-based `delegate`/`delegate_many`, per-task autonomy policy and spend guard, GitHub branch/PR creation, CI retry, a code-review model gate and guarded merge. In team mode an authenticated project has roles and shared session oversight; a personal supervisor agent can list/read users' visible sessions and request intervention, but its acting tools require user approval. Model providers, GitHub checks and sandbox backends are dependencies; their organizations do not donate decision rights. [Architecture](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/architecture.md); [factory description and preflight limitation](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/factory.md); [team mode](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/team.md).

## Operational model

S1 cells are model-directed sessions that read, modify, test and report on task environments, including factory-created coding sessions and bounded delegates. A task's status and dependencies constrain when one starts; the factory's Go controller enforces state and guards but does not itself own the model's code decision. Overlapping branches/dependencies and failing CI supply inter-cell disturbances. The optional PR-loop hands failures and reviewer findings back to the task agent; configured distinct-model review offers a complementary inspection of submitted code. At the product recursion an authenticated project owner chooses and changes membership and project identity, while a user can inspect all their current sessions and authorize the supervisor's corrective acts. [Task lifecycle](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/tasks/service.go); [factory wiring](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features_factory.go); [supervisor acting tools](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/supervisor.go#L213-L455).

## S1 — Operations

- State: A
- Function: a model-directed run selects and uses tools to produce the requested task outcome in a sandbox/host session.
- Disturbance / variety regulated: diverse coding/information requests, filesystem and tool observations, failures, model responses and approval boundaries.
- Decisive decision or feedback right: select tool calls, interpret results, continue/replan, produce task response or a code change/PR.
- Decision owner: the configured live LLM-backed agent in each session or factory task; delegated agents own their bounded subtask choices.
- Supporting / enforcement mechanisms: `ai/agent.Loop`, sandbox adapters, tool registry, steering, durable events, approvals and per-task policy/budget hooks.
- Closure path: model action → sandbox/tool result and event → next model turn or task conclusion; factory end hook records state, may request follow-up PR work.
- Boundary reachability: the CLI and embedded/web hosts compose the loop; `FactoryFeature` installs a spawner and task dispatcher in the supported `FACTORY=1` mode.
- Why this is / is not agent-owned: the model chooses the task work; queueing, policies, tool execution and approvals constrain but do not select the operational response.
- Evidence: [README quick start](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/README.md#L70-L105), [single loop architecture](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/architecture.md), [factory spawner and runtime hook](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features_factory.go#L163-L317).
- Basis: structural; source paths and scripted tests, no live external model result claimed.
- Confidence: high for first-party ownership/wiring.
- Caveats: local backend does not itself isolate the host; a model key and applicable runtime configuration are required for real inference.

## S2 — Coordination

- State: C
- Function: attenuate conflicts among distinct task agents that share repository integration, dependencies and constrained execution capacity.
- Disturbance / variety regulated: competing coding sessions/branches may conflict with the shared base, dependent tasks may start before prerequisites, and concurrent jobs may contend for quotas.
- Decisive decision or feedback right: gate dependent task release, detect CI/merge conflicts, return actionable rebase/test feedback and defer incompatible integration; a whole-inter-S1 autonomous coordinator is not established.
- Decision owner: deterministic factory task/forge mechanisms for admission and conflict detection; the receiving task agent decides its own fix, while the human/task policy controls merge permission. A function-specific constructor path exists, not a demonstrated autonomous S2 owner.
- Supporting / enforcement mechanisms: conditional task-state transitions, `DependsOn` release, `MaxConcurrent`, per-PR `Mergeable`/CI checks and `MaxFixRounds` feedback loop.
- Closure path: dependency completion releases the waiting S1; an integration conflict or failing CI leaves the PR unmerged and passes feedback to the producing agent, which can rebase/fix and publish a new head for re-evaluation.
- Boundary reachability: `FactoryFeature` composes `tasks.Service` and `forge.Loop`; these are invoked by the supported factory mode, not generic interfaces alone.
- Why this is / is not agent-owned: a repo-level S1 interaction is specifically regulated, but the decisions to defer/settle are mechanical or owner-governed; assigning model discretion to a named coordinator would overread the code.
- Distinct S1 units: separate factory task agent sessions pursuing changes against one project repository, including bounded delegated sessions.
- Inter-S1 disturbance: changes originating in different cells can invalidate a common base or require an ordering relation, and unchecked parallel execution can exceed current shared limits.
- Attenuating coordination relation: dependency blocking/release and conflict-aware PR integration with CI/result/merge-state feedback, rather than unguarded simultaneous publication.
- Feedback into subsequent S1 behaviour: `ciFailed` or `conflictFeedback` tells the same task agent to inspect, rebase/fix, test and reopen the PR; stored task state and checks are consulted before the next release or merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness concerns actual cross-cell interference at **shared repository integration** and prerequisite constraints; report collection, a tool queue or generic `delegate_many` alone is not being counted as S2.
- Evidence: [dependency state and release](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/tasks/service.go#L500-L565), [CI and conflict feedback/resume](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/forge/loop.go#L489-L670), [delegation isolation/limits](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/delegate/delegate.go#L178-L220).
- Basis: structural.
- Confidence: medium; inter-S1 interference/closure is explicit, agent-owned system-wide coordination is not.
- Caveats: the factory documents fake-host end-to-end coverage, not verified production-scale contention resolution.

## S3 — Inside-and-now control

- State: P
- Function: whole-current oversight and interventions over an installed user's/project's agent sessions in supported team mode.
- Disturbance / variety regulated: blocked approvals, stuck/failing sessions, priority of attention and conflicting active work commitments visible across sessions.
- Decisive decision or feedback right: choose which session to continue, steer, approve/deny, cancel or start, after an all-visible-session view.
- Decision owner: the legitimate authenticated user/project member authorizes risky acts; the supervisor agent observes and recommends but does not independently execute these acts without user confirmation.
- Supporting / enforcement mechanisms: `list_sessions`, `read_session`, watcher, supervised `session_*` tools, tool approval gate, membership access checks, audit and event feed.
- Closure path: user examines the supervisor's system-wide status/readout → authorizes its concrete action → `session_send`/`approve`/`cancel`/`spawn` changes an ongoing run, its permission hold or the current work inventory; audit records the decision.
- Boundary reachability: `harness-web -team` installs the first-party `app/product` Supervisor; a watcher can proactively surface exceptions, and the user can converse with the supervisor in its dedicated thread.
- Why this is / is not agent-owned: model-based attention triage is present, but every material intervention tool is explicitly registered as risky and requires the human's confirmation in this mode; runtime budgets/dispatch alone are not S3 authority.
- Whole-system current view: `overviewFor` and `listSessions` aggregate accessible personal/project sessions with status, project, creator, current wait and update time, augmented by `read_session` context.
- Current-control decision scope: human-approved correction/termination, unblock and allocation of new session work across the user's visible installed operation; this is not a claim over unrelated tenant organizations.
- Evidence: [supervisor contract and risky approvals](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/supervisor.go#L27-L100), [whole-current list and acting tools](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/supervisor.go#L213-L505), [team settings](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/team.md).
- Basis: structural.
- Confidence: medium-high for the explicitly enabled human-owned mode.
- Caveats: `FACTORY=1` and `-team` are opt-in; a standalone one-session CLI has no asserted S3 loop. Factory queue/scheduler is not counted as autonomous S3.

## S3* — Complementary audit

- State: A
- Function: independently challenge the coding agent's completion claim before integration, using a direct code-host diff and a configured different reviewer model.
- Disturbance / variety regulated: a coding agent may submit defective, insecure or task-incomplete changes while its own summary or CI gives an incomplete account.
- Decisive decision or feedback right: emit approve/reject and findings on the exact PR; block merge or return fix feedback to the producing task.
- Decision owner: a separately configured `FACTORY_REVIEW_MODEL` with explicit different-model enforcement for that task; mechanical security/test checks are supporting guards.
- Supporting / enforcement mechanisms: forge direct PR diff/comments, mechanical protected-path/secrets/injection checks, CI-success requirement, model review rubric, head-specific recorded verdict and guarded merge.
- Closure path: CI-ready PR → independent diff/reviewer judgment → `forge.Loop.gate` posts a verdict → approval allows guarded merge (only if AutoMerge) or findings resume/block the authoring S1, affecting the next attempt.
- Boundary reachability: `FactoryFeature` installs the review gate when Forge is configured and review is not disabled; setting a distinct `ReviewModel` explicitly requires reviewer/author model inequality. This is a supported installed mode, not a borrowed external organization.
- Why this is / is not agent-owned: the configured reviewer model judges a code-host artifact without relying on the producing agent's report; default fallback to the *same* model is explicitly weaker and not credited as independent.
- Claim being audited: the authoring factory agent's PR actually satisfies its task and is safe to integrate.
- Ordinary reporting path: the author/agent task result and PR/CI status used by the normal factory work loop.
- Complementary access path: the gate fetches actual PR patch/comments from GitHub, runs independent static checks and asks a distinct model to inspect the diff.
- Independence boundary: distinct configured model checked by `RequireDifferentModel`, outside the producer's agent conversation; only this mode is counted, not the default same-model fallback.
- Who acts on findings: factory PR loop withholds merging, publishes feedback and restarts the authoring task, or blocks for a human; successful verdict remains SHA-specific.
- Evidence: [reviewer distinct-model and direct-diff checks](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/review/review.go#L68-L210), [gate feedback and guarded merge](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/forge/loop.go#L671-L765), [factory feature review wiring](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features_factory.go#L319-L354), [documented same-model caveat and setup limitation](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/factory.md).
- Basis: structural, conditional on the documented distinct-reviewer mode.
- Confidence: medium; strongly wired source path, no actual independent live provider review was executed for this assessment.
- Caveats: `NoReview` disables the gate; without a separate reviewer model the default self-review explicitly warns that it is not independent. Project CI and GitHub are complementary evidence sources, not ownership of the audit judgment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated installed decision loop that interprets external future change and selects/returns a prospective capability adaptation.
- Disturbance / variety regulated: new future tasks, repo practices, provider conditions and failures can require changed capabilities; present modes primarily address active or past tasks.
- Decisive decision or feedback right: no first-party S4-specific prospective adaptation judgment with a returned change in the installed operating model was found.
- Decision owner: not established.
- Supporting / enforcement mechanisms: optional factory lessons distillation and recall, memory, project configuration, cron triggers, coding benchmarks and feature extensibility.
- Closure path: failed/completed task lessons can be recalled in later prompts; this changes operational context but does not select an external-and-future option and install a revised organizational capability under S4 control.
- Why this is / is not agent-owned: model-generated lessons and new task prompts are retrospective operating memory, not a demonstrated strategic environmental scan/adaptation closure.
- Evidence: [lessons feature](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/lessons/lessons.go#L1-L34), [distillation/recall](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/features/factory/lessons/lessons.go#L110-L180), [docs factory/bench boundary](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/factory.md).
- Basis: bounded negative-state structural review.
- Confidence: medium-high for shipped mode.
- Caveats: an external project owner can redesign/deploy the system; contributor development is outside this deployed recursion and does not imply a shipped S4 parent loop.

### Absence scope

- Surfaces inspected: factory lesson observer/recall, configuration/features, trigger scheduling, project settings, supervisor/watch, bench/evaluation and team/factory documentation.
- Plausible first-party paths checked: future-task lesson reuse; model selection, feature configuration and adaptive prompts; supervisor escalation; trigger templates; human project edits and SWE-bench comparison.
- Why no material first-party path remains: these first-party paths either handle current work, remember earlier outcomes or require an independent externally chosen redesign; no function-specific future environmental distinction → adaptation decision → installed capability-return loop is shipped at the assessed product boundary.

## S5 — Policy and identity

- State: P
- Function: a legitimate human project owner settles and changes the installed project's identity, membership authority and binding operating boundaries.
- Disturbance / variety regulated: project/repository identity changes, member access conflicts and the limits under which assistant or factory agents may act.
- Decisive decision or feedback right: create/update the project, change its repository/default branch and assign/revoke member roles; maintain at least one owner.
- Decision owner: authenticated human project `owner` (and separately system admin for account approval), never the task agent or deterministic role checker.
- Supporting / enforcement mechanisms: owner-only routes, persistent Project/Member store, role-based guards on API/supervisor operations, audit/feed, per-task policy and merge-permission enforcement.
- Closure path: identity/membership/policy issue → project owner edits authoritative project/roles (or approves a new actor) → changes persist and are enforced on subsequent session access, supervisor acts, factory task/project use and integration permissions.
- Boundary reachability: `harness-web -team` provides owner-gated project patch/member routes; membership changes immediately govern user and agent-action access in the same installed product. No upstream maintainer authority is borrowed.
- Why this is / is not agent-owned: the agent may propose work and act with human approval, but ultimate project membership, repository identity and operating authority remain owner-governed; static policy checks enforce their decisions.
- Identity / ultimate-policy issue: which repository constitutes the project and who may authorize/perform work on behalf of its organization.
- Ultimate authority in each claimed mode: the project owner in team mode; no autonomous ultimate-policy mode established for a single CLI agent.
- Return-to-operation path: owner-only `PATCH /projects/{pid}` or role assignment → stored project/role update → subsequent `requireProject` and server/agent tool checks recognize the new authority and branch/repo context.
- Evidence: [owner-only project/role changes](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/app/product/team_projects.go#L153-L346), [team membership and access model](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/team.md), [factory policy/merge modes](https://github.com/7ar-chat/harness/blob/89edbffde74f4aa2c7675dc07615f26ab76cae91/docs/factory.md).
- Basis: structural parent-governed team mode.
- Confidence: medium; explicit authorization/return path, not a claim about the upstream OSS organization's policy process.
- Caveats: ordinary tool approval or a single PR merge veto alone would not justify S5; the claimed right is the project-identity/member-authority loop.

## Distributed OSS parent arrangement

Public repository contributors and the maintainer's CI/release policy are external development governance, not a common S5 for every deployed installation. The positive `P` states refer to the **local installed** authenticated user/project owner: current-session supervision for S3 and project identity/roles for S5. Independent installations have separate parent authorities.

## Self-hosted and non-human modes

`harness` CLI has S1 and no attributed team-level parent loops. `-team` and factory integration are explicit shipped options, not ambient proof of production use. The S3 parent mode depends on user-confirmed supervisor acting tools; S5 depends on team ownership. S3* credits only an enabled distinct-reviewer configuration with code-host access; same-model/no-review configurations do not inherit it. OpenSandbox is an isolation support; local backend has stated trust limitations. No external organization, hosted provider or developer is counted as the installed S3/S4/S5 owner.

## Recursion

Factory tasks/sessions are separate S1 units; child delegates work on one bounded role/task, often the same repository and branch. Their sandbox/thread/role isolation does not by itself form complete autonomous S3–S5 recursion. Team projects are locally bounded organizations under their owners; multiple independent installations are not one coordinated meta-organization.

## Variety and escalation

Tool permissions/sandbox and task dependency gates attenuate immediate variety; separate roles, model/tool loop and `delegate_many` amplify task capability. Shared Git/CI conflicts and code-review findings return to the authoring S1 rather than silently merging. Budget exhaustion, repeated failures and human merge/approval stops escalate to the project/user. The operator-visible session inventory and watcher provide current-control input; separate-model reviewer uses complementary code-host evidence. Recorded lessons improve future operational recall but are not treated as full S4 capability redesign.

## Evidence gaps

- The Go toolchain is not installed in this assessment environment; code and shipped tests were inspected, but this review did **not** run the candidate's Go unit tests, paid model calls, GitHub App write operations or an independent live reviewer.
- `docs/factory.md` itself says factory end-to-end exercises were only against fakes and recommends a read-only deployment preflight; operational outcomes at real external providers remain unverified.
- A specific multi-agent model may proactively settle file-overlap choices beyond the provided feedback, but no separate whole-inter-S1 autonomous coordinator was demonstrated; hence S2 is `C`, not `A`.
- No distinct future-environment scanning and prospective capability-installation process was proven, even though factory lessons and human project settings are substantial adjacent facilities.
