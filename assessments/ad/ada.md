---
harness_id: ada
project_name: Ada
repository: https://github.com/black141312/ada
review_ref: 20c3dd8813ce82fc82c2b243094ea239502e029f
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Ada

## Review boundary

- System in focus: the first-party Ada coding-agent runtime, its native subagents, live-run control tools, background jobs and integration-skill constructor at the frozen revision.
- Purpose and identity: an adaptive local coding assistant that can inspect projects, act through tools, delegate separable work, supervise current runs and create reusable skills for connected external tools.
- Relevant environment: local project/repository, shell, model/provider responses, MCP integrations, user/operator, enterprise administrator and other concurrently executing Ada agents.
- Standard-distribution boundary: shipped Node.js CLI/REPL/headless runner, `ada serve` editor API, `Agent` strategies, tool registry, subagent/worktree runner, live-run registry, background job manager, project skills and optional enterprise policy service.
- Credited operating / distribution surfaces: `src/client/{cli,agent,tools,background,worker,live,session,settings}.ts`, first-party MCP and skill adapters, `src/server/enterprise.ts`, shipped command and editor modes.
- Adjacent first-party surfaces excluded from ownership: deterministic `src/selfcheck.ts`, fake/stub MCP harness, contributor/test/build machinery, documentation examples, repository maintenance/governance and external LLM/MCP-provider decisions. Tests corroborate reachability, but do not themselves run production control.
- First-party operating / deployment modes considered: interactive `ada` terminal, headless `ada -p`, `ada serve` with session/job endpoints, agent-chosen `react`/`single`/`plan`/`toolsmith`/`rlm`/`auto` strategy, native foreground/background subagents, isolated git-worktree and fallback in-process workers, optional administrator-controlled enterprise server.
- Recursion level: one Ada runtime controlling its active operational agent/subagent population. Independently administered enterprise organizations and users' development projects are external parent/environment relations rather than silently counted as its own internal organization.
- Reviewed revision: `20c3dd8813ce82fc82c2b243094ea239502e029f`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The CLI and editor server construct an `Agent` with a model adapter, session and registered tools. Each model/tool turn can select files, shell and integration tools, observe errors and results, and choose the next action. The shipped `spawn_agent` and `background_task` tools create separate `Agent` sessions with their own turns; a background task records status/progress/result in `.ada/jobs.json` and notifies the initiating conversation. `toolsmith` and `rlm` can also dispatch child turns. Although some documentation mentions `multi`, the frozen source removes that strategy; it is not a credited operating mode.

In a git repository, a delegated subagent may execute in a detached worktree. Returned modified paths are reconciled with a parent-scoped `claimedPaths` set: a file already claimed by a different worker is refused and reported as a collision. This is a shipped but bounded inter-worker collision mechanism, not an adaptive independent conflict negotiator; fallback in-process workers do not receive equivalent isolation.

Within one process, `live.ts` registers active model runs and exposes model-callable `list_agents`, `peek_agent` and `send_agent_message`. A model can inspect concurrent tasks, recent output and token context, then steer another run through its next-step mailbox. Separately, the CLI `/jobs` command and editor jobs list/cancel endpoint expose the background-job cohort to an operator. The process-local live registry does **not** enumerate isolated worktree child processes or unrelated terminal processes; job persistence has its own limited visibility and lifecycle.

In `toolsmith`, the model reads tool descriptions and schemas from exactly one configured external MCP integration, proposes future capability areas, instructs delegated models to author integration-specific `SKILL.md` files, and writes them under `.ada/skills` for later skill loading. It is an optional capability-adaptation mode, not just an internal task plan. Ordinary edit verification, permissions, enterprise policy configuration, session logs and first-party deterministic tests were separately inspected for S3*, S4 and S5 ownership.

Frozen primary sources: [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts), [`src/client/cli.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/cli.ts), [`src/client/background.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/background.ts), [`src/client/worker.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/worker.ts), [`src/client/live.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/live.ts), [`src/server/enterprise.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/server/enterprise.ts), [`src/selfcheck.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/selfcheck.ts).

## Operational model

Ada's primary and delegated `Agent` instances own local programming choices inside their assigned tasks. Tool execution and process orchestration constrain and transport those choices. Distinct child agents exist as real operating units, unlike same-turn parallel tool calls. Two higher-level operating arrangements are evidenced: in-process agents can read and steer live peer runs through tools; a human operator can view and cancel launched background jobs through CLI/editor surfaces. These are bounded, alternative current-control arrangements, not evidence of a global manager across all Ada processes. External enterprise policy admins own static settings and permissions; they are not thereby an Ada identity/ultimate-policy council.

## S1 — Operations

- State: A
- Function: perform requested project inspection, coding, editing and related tool-driven work.
- Disturbance / variety regulated: unfamiliar projects, user goals, files and tool failures, integration results and changing local context.
- Decisive decision or feedback right: each `Agent` model selects tools/arguments and its next response after seeing prior observations.
- Decision owner: primary or child model-backed `Agent` operating within an assigned task.
- Supporting / enforcement mechanisms: tool registry, session history, execution wrappers, permissions, token limits, project settings and model-client adapters.
- Closure path: request → model chooses action → tool executes → feedback enters the session → model revises the next action or completes.
- Boundary reachability: both terminal and `ada serve` construct the shipped `Agent`; registered native tools and separately spawned child `Agent` sessions are reachable in the supported runtime.
- Why this is / is not agent-owned: model decisions vary with tool feedback; the deterministic tool layer carries out selections but does not preselect each task action.
- Evidence: [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts), [`src/client/cli.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/cli.ts), [`src/client/background.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/background.ts).
- Basis: explicit + structural; first-party deterministic script selfcheck of individual mechanics.
- Confidence: high for shipped model/tool ownership.
- Caveats: no live LLM agent execution or outcome-effectiveness measurement was performed.

## S2 — Coordination

- State: C
- Function: damp conflicting writes by separate delegated operating agents in one parent-owned worktree task.
- Disturbance / variety regulated: two independently running child agents may both modify the same repository path, producing destructive overwrite or inconsistent integration.
- Distinct S1 units: separate delegated `Agent` subprocesses, each selecting and executing its own work in a detached git worktree.
- Inter-S1 disturbance: overlapping changed paths when two workers independently edit the same tracked or untracked file.
- Attenuating coordination relation: the parent `Agent.claimPaths` reserves each changed path; `runIsolatedWorker` copies only unclaimed outputs into the parent's tree and reports rejected collisions.
- Feedback into subsequent S1 behaviour: the parent receives `[not applied — another worker already owns: ...]`, so integration/next delegation can take the conflict into account; overlapping child outputs are not both applied.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path detects an actual inter-agent file collision, atomically reserves affected output paths and prevents competing writes, rather than only launching or sequencing children.
- Decisive decision or feedback right: deterministic first-claim reservation/denial for an S2-specific conflict path; the parent receives the result but no autonomous negotiation/resolution policy is established.
- Decision owner: constructed parent-level collision circuit, not a proven independent adaptive S2 agent.
- Supporting / enforcement mechanisms: isolated git worktrees, `git status --porcelain -uall`, per-parent `claimedPaths` set, copy-back filter and collision text.
- Closure path: distinct worker edits → changed-path comparison → parent claim/deny → only allowed edits applied → collision returned into parent work/next delegation.
- Boundary reachability: `spawnSub` calls `runIsolatedWorker` in a git repository by default; the claim callback is wired to the parent agent and changes real copy-back behavior.
- Why this is / is not agent-owned: the conflict-damping function is concrete, but its rule is deterministic. A model can respond after observing a collision, not autonomously choose or revise the coordination rule itself; hence constructor `C`, not `A`.
- Evidence: [`src/client/worker.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/worker.ts), [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts).
- Basis: explicit + structural.
- Confidence: medium-high for the isolated-worktree path.
- Caveats: collision reporting does not negotiate a merged edit; in-process fallback, non-git projects and other independent Ada processes lack this same file-reservation coverage.

## S3 — Inside-and-now control

- State: A(P)
- Function: observe and intervene in the current running agent population, including cross-run steering and operator cancellation of currently assigned work.
- Disturbance / variety regulated: mismatched live priorities, stuck or misdirected concurrent work, current job progress and commitment to still-running tasks.
- Whole-system current view: in one runtime process, `list_agents` enumerates all registered live runs with task, age and context size, with `peek_agent` providing recent output/usage; in attended CLI/editor mode, `/jobs` and `GET /v1/jobs` enumerate the current background-job cohort and progress.
- Current-control decision scope: an autonomous Ada run can select a peer and send context, priority corrections or stop requests to its next-step mailbox; an attended operator can select and cancel a currently running background job via the exposed first-party control surface.
- Decisive decision or feedback right: in autonomous mode, the model determines which registered run needs intervention and its steering content; in parent mode, the human decides which background task to abort.
- Decision owner: agent model for the bounded live-run mode; human operator for the bounded job-management mode.
- Supporting / enforcement mechanisms: process-local `runs` map and steer queues, `registerRun`/`endRun`, `list_agents`/`peek_agent`/`send_agent_message`, `jobs.json` job roster, `AbortController`, `/jobs` and REST cancel route.
- Closure path: live peer information → agent management decision → message enters peer steer queue → peer processes it at its next step; or background status → operator cancel decision → abort controller changes job execution and persisted status.
- Boundary reachability: `src/client/live.ts` registers shipped tools used by agents and `Agent.send()` creates live run IDs; `src/client/cli.ts` supports `/jobs` and `GET /v1/jobs`/`POST /v1/jobs/:id/cancel` for actual background jobs started by shipped `background_task`.
- Why this is / is not agent-owned: the autonomous model selects an intervention using live portfolio information, beyond ordinary own-task execution; the operator branch has separate legitimate human decision rights and operational return. Neither UI nor abort mechanism alone would establish S3.
- Evidence: [`src/client/live.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/live.ts), [`src/client/background.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/background.ts), [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts), [`src/client/cli.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/cli.ts), [`src/selfcheck.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/selfcheck.ts).
- Basis: explicit + structural, with offline stub-run tests for live roster/messaging and job cancellation.
- Confidence: medium; current-management reachability is bounded by mode and visibility scope.
- Caveats: live registry is process-local and excludes isolated child processes; job roster is distinct from the live-run registry. A message is not guaranteed to be obeyed; parent job control is a particular attended background-job mode, not global project governance.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed agent with `list_agents`/`peek_agent`/`send_agent_message` | Detects a current peer-run priority/problem in the in-process cohort | Model-selected steering enters another agent's queue for its next step | `src/client/live.ts`, `src/client/agent.ts` |
| Parent (`P`) | Attending terminal/editor operator of spawned background tasks | Job roster/progress calls for human intervention | Operator invokes cancel; `AbortController` stops the selected job and updates its status | `src/client/background.ts`, `src/client/cli.ts` |

## S3* — Complementary audit

- State: —
- Function: no shipped complementary, sufficiently independent audit of actual operating claims with a corrective return to S3 was established.
- Disturbance / variety regulated: misleading task results or unchecked work quality remain possible; ordinary testing and model verification do not implement an independent organizational audit route.
- Decisive decision or feedback right: the same working agent can run `verifyEdits`, read tool errors and retry; developers run an offline selfcheck. No distinct audit owner decides claims against independent reality for the operating runtime.
- Decision owner: none within the declared S3* function.
- Supporting / enforcement mechanisms: ordinary edit verification, session transcripts, tool status, deterministic development tests, job progress and human approval prompts.
- Closure path: local results return to their producing task's S1; no independently sourced audit finding → responsible S3 corrective decision circuit is wired.
- Why this is / is not agent-owned: source/test checks are valuable but either ordinary production verification or adjacent development evidence, not a complementary management audit.
- Evidence: [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts), [`src/client/live.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/live.ts), [`src/selfcheck.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/selfcheck.ts).
- Basis: explicit + structural bounded absence review.
- Confidence: medium-high.
- Caveats: downstream users can create their own independent audit; those additions are outside this frozen first-party distribution.

### Absence scope

- Surfaces inspected: core agent loop, edit verification, tools and approvals, live/peer views, job reporting, `src/selfcheck.ts`, enterprise audit logging and operator APIs.
- Plausible first-party paths checked: autonomous reviewer/critic role, independent reality probe, job progress audit, enterprise audit log as S3* and offline test runner as production auditor.
- Why no material first-party path remains: none supplies a separately controlled complementary claim-vs-reality assessment with authorized corrective return in a reachable Ada operating mode; logs/tests or same-agent verification do not close the missing relation.

## S4 — Outside-and-then intelligence

- State: A
- Function: investigate a newly connected external tool environment and construct future reusable operating capabilities tailored to it.
- Disturbance / variety regulated: newly available MCP integrations and their unfamiliar tool schemas, future tasks requiring capabilities Ada has not yet encoded as skills.
- External distinction: names, descriptions and parameter schemas of tools belonging to the sole configured external MCP integration.
- Future / prospective distinction: model-generated map of 4–8 integration capability areas beyond the current request and reusable procedures for later sessions.
- Adaptation option generated: per-capability first-party `SKILL.md` recipes drafted by delegated agents and placed in `.ada/skills`.
- Path back into current capability / S3: `toolsmith` reads integration docs, prompts model for capability areas, delegates future-oriented skills, persists validated-frontmatter drafts, and subsequent normal project skill loading can expose those procedures to the operating agent.
- Decisive decision or feedback right: the model chooses which external capabilities merit reusable skills and delegates their content drafting; storage utilities implement that decision.
- Decision owner: model-backed `toolsmith` orchestration and separate drafting child models, within the configured external-integration boundary.
- Supporting / enforcement mechanisms: `soleIntegration`, `readIntegrationDocs`, `spawnSub`, `writeProjectSkills`, filesystem skills loader and MCP tool schemas.
- Closure path: external integration schemas → model's prospective capability grouping → drafted skill options → persisted project skills → later agent can load/use the new capability guidance.
- Boundary reachability: the registered `toolsmith` strategy runs within the shipped `Agent`, reads actually configured MCP tools and writes skills into the standard runtime's skill directory. This does not rely on contributor-only examples or offline tests for ownership.
- Why this is / is not agent-owned: no deterministic list fixes which capability areas or skill instructions to create; model discretion supplies the prospective adaptation judgment. The storage path only enforces the selected capability changes.
- Evidence: [`src/client/agent.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/agent.ts), [`src/client/cli.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/cli.ts), [`src/selfcheck.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/selfcheck.ts).
- Basis: explicit + structural; first-party deterministic stub MCP/schema and skill-persistence checks.
- Confidence: medium-high for the conditional one-integration mode.
- Caveats: prospective skills are not proven effective; this requires exactly one connected integration, user configuration and successful model outputs. General plan/task decomposition and memory alone were not credited as S4.

## S5 — Policy and identity

- State: —
- Function: no first-party closed identity/ultimate-policy deliberation and authoritative return to operations at the Ada runtime recursion was established.
- Disturbance / variety regulated: user and enterprise permission choices can constrain task execution, but no identity-level dispute or ethos trade-off is handled inside a shipped S5 loop.
- Decisive decision or feedback right: operators/enterprise admins choose model defaults, tool permissions, seats and role configuration; no exposed first-party path escalates an identity/ultimate-policy issue to an ultimate authority and feeds its adjudication back as such.
- Decision owner: external user or enterprise administrator for configuration and ordinary policies, not an established S5 owner for this assessed system.
- Supporting / enforcement mechanisms: `src/server/enterprise.ts` seat/policy endpoints, `src/client/cli.ts` org policy fetch/cache and approval flow, tool permission gates.
- Closure path: configuration reaches later tool enforcement, but the required identity/ultimate-policy issue → legitimate authority decision → returned identity resolution circuit is absent.
- Why this is / is not agent-owned: static permissions, generic human approval and administrator-issued defaults are not, without a specific ultimate-policy decision, S5 governance closure.
- Evidence: [`src/server/enterprise.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/server/enterprise.ts), [`src/client/cli.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/cli.ts), [`src/client/tools.ts`](https://github.com/black141312/ada/blob/20c3dd8813ce82fc82c2b243094ea239502e029f/src/client/tools.ts).
- Basis: explicit + structural bounded absence review.
- Confidence: medium-high.
- Caveats: governance of an enterprise or OSS project running Ada is a different recursion and cannot be imported merely because those humans operate the software.

### Absence scope

- Surfaces inspected: enterprise authentication/roles and organization policy store, CLI client policy refresh/cache, approvals, runtime settings and tool authorization, session state and repository governance vicinity.
- Plausible first-party paths checked: enterprise `PUT /v1/policy`, administrator role, ordinary per-tool approval, settings defaults, model self-instruction, and contributor authority as a parent S5 mode.
- Why no material first-party path remains: each reachable path configures or enforces predetermined task constraints; the reviewed product provides no function-specific identity/ultimate-policy issue, authoritative judgment and return-to-operation closure at this system boundary.

## Distributed OSS parent arrangement

Maintainer decisions and independently run Ada instances may have project-level governance, but no observed first-party runtime coupling makes that OSS project's authority an Ada-wide S5 owner. The `S3` parent mode is narrower: a local operator supervises jobs launched in their own attended Ada session, not organization-level governance of all contributors.

## Self-hosted and non-human modes

Ada is self-hostable. Its process-local live-run view can support autonomous intervention among concurrently registered agents; terminal/editor job controls can support parent intervention for attended background tasks. Those are recorded separately as S3 modes. The optional enterprise service sets permissions and defaults, not a separately evidenced S4 or S5 parent loop. Isolated subprocess workers and unrelated terminal sessions limit the scope of autonomous current-management visibility.

## Recursion

An individual `Agent` is an operational S1 with its own model/tool loop; delegated child agents are additional S1 units when actually running. Coordination and current-control evidence is at the parent Ada runtime/process recursion, not the larger open-source maintainer organization or every system whose tools an MCP connection exposes. Worker nesting alone is not VSM recursion.

## Variety and escalation

Operational errors feed back to the relevant agent. Collision detection prevents competing child edit copies and reports conflict to the parent, but needs further model/human resolution. `list_agents`/`peek_agent` expose current peer load; `send_agent_message` can redirect subsequent steps. Background jobs announce results and can be cancelled by an operator. `toolsmith` scans newly available integration schemas and makes future skills; enterprise policy gates tool behavior. None of these channels by itself creates independent S3* audit or S5 identity closure.

## Evidence gaps

- No live LLM-agent run or outcome/coordination benefit measurement: only static frozen-source inspection and first-party deterministic script checks are used, per batch rule.
- In-process live-run roster cannot see detached git worker processes or separate Ada invocations; no universal multi-process S3 ownership is claimed.
- Source documents a `multi` strategy in some user-facing places, but removes it from the actual `ORCHESTRATORS` registry. It was not counted.
- S2 collision rule blocks duplicate file copy-back but does not automatically reconcile competing intent, and the in-process fallback bypasses it.
- Toolsmith requires precisely one configured integration and no evidence proves generated skills correct on live external systems.
