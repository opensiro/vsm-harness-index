---
harness_id: heaw
project_name: heaw
repository: https://github.com/DaDozlov/harness-agent
review_ref: dfff7b2bfbd6fb08cb754461124ac8dab2053622
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# heaw

## Review boundary

- System in focus: the first-party TypeScript `heaw` coding/general agent engine and its CLI, project setup skill and optional named/ad-hoc subagent runtime, not arbitrary customer agents built with the reusable library.
- Purpose and identity: model-driven project tasks with tools, permissions, planning, bounded subagent work, testing and optional operator-configured independent UI verification.
- Relevant environment: changing repository code, concurrent subagent file writes, tool failures, project tests and web UI behavior, human approval and provider/model outputs.
- Standard-distribution boundary: packaged `src/core` agent loop, `src/agents/subagents.ts`, tool/permission paths, CLI and bundled setup/plan skills; optional `setup-harness` browser tester constructor is credited only as a configured first-party mode.
- Credited operating / distribution surfaces: `heaw` chat/run, built-in `delegate` with optional file scopes and subagent execution, `setup-harness` skill's explicit browser tester/`beforeStop` recipe, `Session` and hook `runAgent` return path.
- Adjacent first-party surfaces excluded from ownership: source repository's development CI, offline `src/evals/` trials, unit tests, maintainer examples and benchmark runs, and the published example workflows not activated by an ordinary `heaw` session.
- Recursion level: main model agent and independently model-driven delegated workers acting on the same project; selected file restrictions dampen inter-worker interference. Separate optional tester supplies a complementary auditing viewpoint, not an organizational S5.
- Reviewed revision: `dfff7b2bfbd6fb08cb754461124ac8dab2053622` (source-static), 2026-11-11.
- Generated Profile version: 0.2.4; Methodology version: 0.3.8.
- Current Profile version: 0.2.4; Methodology version: 0.3.8.

## Repository architecture

The model-backed engine runs an iterative tool loop with streaming feedback and bounded costs/turns. Its `delegate` tool can launch concurrently executing named or ad-hoc subagents with their own model contexts and tools; the main agent chooses tasks and per-subagent `files` scopes. The runtime tightens permission policies to those paths and returns denied writes to a worker. Separately, the bundled `setup-harness` skill offers a specific optional browser-based tester construction: a configured read-only reviewer with isolated Playwright MCP gets the changed UI artifacts and task requirements from a `beforeStop` hook; an independent browser verdict can return failure feedback to the coding agent. Generic unit/eval suites and traces are not counted as operating S3*. [Engine design](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/docs/DESIGN.md), [subagent runtime](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/agents/subagents.ts), [setup skill](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/skills/built-in.ts).

## Operational model

The main model selects coding tools, changes and delegations based on tool feedback. In a supported parallel-work mode, it partitions files for different child S1 workers; deterministic deny rules enforce the partition and feed out-of-scope errors to a worker. In a separately configured first-party setup mode, an additional browser-testing agent checks resulting UI behavior through a fresh browser view, then passes a verdict via a hook. Neither the parent model's routine task plan nor resource caps form a higher-recursion S3 current-management loop.

## S1 — Operations

- State: A
- Function: transform project/user tasks into model-chosen code and tool actions and incorporate test/tool results into the next action.
- Disturbance / variety regulated: variable user goals, repository state, edit/test failures, model context loss, tool denials and provider errors.
- Decisive decision or feedback right: choose next tools, arguments and when to delegate, plan, repair or answer after returned observations.
- Decision owner: configured model agent operating through the first-party core loop; first-party runtime implements concurrency, tool result delivery and constraints.
- Supporting / enforcement mechanisms: provider adapter, tool registry, permissions, session JSONL store, hooks, context compaction, limits and terminal UI.
- Closure path: `heaw` chat/run → `Session`/model loop → selected tool invocation → structured tool result and feedback → revised model call or final response.
- Boundary reachability: shipped CLI loads a configured model and core engine, executes the loop and exposes file/shell/MCP tools; no external application is required to give the model task discretion.
- Why this is / is not agent-owned: model selects semantic work, whereas deterministic rule checks, forced approval and turn caps only constrain its actions.
- Evidence: [core loop](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/core/loop.ts), [session](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/core/session.ts), [README CLI](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/README.md).
- Basis: shipped model/tool structural path; confidence: high.
- Confidence: high.
- Caveats: no live API-connected execution or output-quality claim from this static review.

## S2 — Coordination

- State: A
- Function: attenuate conflicting file writes among concurrently working autonomous subagents by partitioning their authorized change surfaces.
- Disturbance / variety regulated: two model-driven delegated workers may edit the same files or shared integration points in incompatible orders and overwrite one another.
- Distinct S1 units: independently model-backed `delegate` worker sessions with their own contexts, tools and task-result feedback, operating alongside the parent and other worker sessions.
- Inter-S1 disturbance: concurrent delegates' writes to a shared checkout can collide; first-party documentation explicitly requires each writing delegate to have its own `files`, with the parent retaining shared integration files.
- Attenuating coordination relation: the model-owned parent specifies separate file-glob scopes and shared-file ownership in `delegate` arguments; runtime converts each scope into a stricter writable permission view.
- Feedback into subsequent S1 behaviour: out-of-scope write attempts are denied as tool results to that child model; its final report is returned to the parent for integration and follow-on task choices.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: file scopes regulate the specifically documented inter-worker write interference, whereas delegation alone merely assigns a task; these scopes also change what workers may do later.
- Decisive decision or feedback right: choose the non-overlapping file ownership breakdown and assign each writing agent's scope; on denied edits the agent must revise work or report the boundary.
- Decision owner: main model agent selects task scopes and file partitions; deterministic `PermissionPolicy.restricted` and `Slots` enforce access and concurrency, not the semantic partition choice.
- Supporting / enforcement mechanisms: per-subagent `files` globs, `writable` restricted view, shared approval policy, `maxParallel` slots, child execution result back to parent.
- Closure path: model issues parallel `delegate({files: ...})` calls → runtime runs child contexts in parallel with disjoint writable sets → out-of-scope writes get denied → worker adjusts and reports → parent integrates shared work.
- Boundary reachability: `delegateTool` ships in the agent toolset and directly applies `args.files` to child `PermissionRestriction` before running actual child `Session`; the bundled plan skill tells the model to group only disjoint-file parallel steps.
- Why this is / is not agent-owned: deciding partitions is an operational coordination choice made by the parent model, not a static hard-coded scheduler. A user can omit `files`, so this is an explicitly supported capable mode rather than universal collision safety.
- Evidence: [delegate tool contract and enforcement](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/agents/subagents.ts#L72-L249), [planning skill file partition advice](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/skills/built-in.ts), [permission restriction](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/core/permissions.ts).
- Basis: structural optional first-party parallel-delegate mode; confidence: medium.
- Confidence: medium.
- Caveats: `files` restriction covers file tools, not arbitrary side effects of permitted shell commands; independent automatically generated plans can still choose overlapping globs. This is a coordination capability, not a formal conflict-free guarantee.

## S3 — Inside-and-now control

- State: —
- Function: no evidenced whole-system current portfolio/resource regulation beyond one agent task's execution budgets and parent-to-child task delegation.
- Disturbance / variety regulated: time/token/cost exhaustion, concurrent workers and incomplete steps are bounded locally but not bargained across an organizational operating portfolio.
- Decisive decision or feedback right: session budgets and limit-sharing are deterministic; user approves particular plans/tool calls; no whole-current manager negotiates multiple independent organizational commitments.
- Decision owner: model chooses S1 task actions and S2 file splits; operator/developer sets limits, with no installed S3 authority evidenced.
- Supporting / enforcement mechanisms: `shareOf` available budget, `maxParallel`, approval UI, `PLAN.md` and `beforeStop` hooks.
- Closure path: limit or plan approval changes a run or task; no cross-operational whole-current allocation/revision is returned to a portfolio of S1 units.
- Why this is / is not agent-owned: budget arithmetic and user approval of a single plan are neither an S3 control owner nor a whole-system decision right.
- Evidence: [subagent budget share](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/agents/subagents.ts), [plan and approval](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/tools/plan.ts), [design non-goals](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/docs/DESIGN.md).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: embedding `heaw` within a separate organizational control plane may add S3 externally.

### Absence scope

- Surfaces inspected: loop limits, subagent slots/budget split, plan mode, hooks, engine library API and roadmap.
- Plausible first-party paths checked: `shareOf`, `maxParallel`, user approval, `beforeStop`, `runAgent` and fixed workflow examples.
- Why no material first-party path remains: none provides a whole-current view with decision over cross-S1 organizational priorities, resource bargains and obligations; per-task mechanisms cannot be promoted by name.

## S3* — Complementary audit

- State: C
- Function: constructor for separate browser-backed verification of a coding agent's changed UI, with a verdict returned to the first-party completion gate.
- Disturbance / variety regulated: a code agent may self-report that a page works while its rendered layout, forms, console or network behavior is broken.
- Claim being audited: the coding agent's implicit/explicit claim that changed UI functionality is ready to complete.
- Ordinary reporting path: code agent's own tool/test results and final answer, which need not observe the rendered UI or real form interactions.
- Complementary access path: separate `tester` model session with read-only code tools and isolated Playwright MCP browser examines changed live pages, form behavior, browser console/network and screenshots.
- Independence boundary: tester has a different model context and browser/user-level observable surface; its read-only role and browser restrictions limit editing of the code whose claims are checked. Independence is relative to coding agent reports, not an external governance auditor.
- Who acts on findings: configured `beforeStop` hook interprets `Verdict: fix first` and returns `continue: true` with actual feedback to the coding agent; otherwise attaches the tester's findings as a note.
- Decisive decision or feedback right: configured tester judges observed browser behavior; deterministic hook parses its verdict and causes the original agent to continue repairs or report verified findings.
- Decision owner: independently invoked tester model decides the browser-backed judgment. Project user/model running `/setup` composes the specific included skill recipe into config, so a ready-made always-installed auditor is not asserted.
- Supporting / enforcement mechanisms: bundled `setup-harness` skill and `TESTER_AGENT` text, `runAgent` hook context, event reporting, file-change list and optional browser MCP server.
- Closure path: setup generates tester and completion hook → agent modifies UI → hook detects changed UI files → independent tester uses browser and verdict → feedback `continue: true` sends coding agent back to repair, or note informs final report.
- Boundary reachability: `src/skills/built-in.ts` contains the exact first-party tester template and hook code, and `src/core/hooks.ts`/`src/core/loop.ts` execute configured `beforeStop` and `runAgent`; setup is an operator-selected supported mode.
- Why this is / is not agent-owned: separate tester's model owns judgment on complementary browser observations; deterministic hook routes its decision, and the coding agent cannot substitute its own assertion for the tester's browser verdict.
- Evidence: [bundled browser tester recipe and hook](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/skills/built-in.ts#L6-L160), [hook invocation](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/core/hooks.ts), [design and runtime tester feedback](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/docs/DESIGN.md#L330-L345).
- Basis: specific first-party conditional audit constructor; confidence: medium.
- Confidence: medium.
- Caveats: operator must configure and run `/setup`, provide a browser/app start command and enable the generated hook. Generic eval trials, deterministic `npm test`, JSONL traces and a merely commented reviewer in `heaw init` are not credited. Browser testing is conditional on UI changes and its own execution limits.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped externally and prospectively oriented adaptation-options process with S3 return established.
- Disturbance / variety regulated: model/tool evolution and repeated coding failures can prompt developers to refine harness instructions, but those are not a demonstrated external-future sensing loop.
- Decisive decision or feedback right: `/retro` asks the same agent to analyze past session failures and propose fixes, leaving human to choose; no dedicated prospective environmental options decision is packaged.
- Decision owner: model may suggest local repairs, user changes configuration; neither is shown governing future external adaptation with S3 dialogue.
- Supporting / enforcement mechanisms: `session_report`, built-in retro skill, model catalog and configuration reload.
- Closure path: a user may choose to edit project instructions after retro; no first-party environment trend → future option → present S3 capability regulation is evidenced.
- Why this is / is not agent-owned: retrospective self-analysis and local environment configuration are not by themselves S4.
- Evidence: [retro skill](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/skills/built-in.ts), [retro command](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/cli/chat/commands.ts), [design scope](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/docs/DESIGN.md).
- Basis: bounded negative; confidence: medium.
- Confidence: medium.
- Caveats: a concrete external S4 capability could be composed using the general library API but is not credited from possibility alone.

### Absence scope

- Surfaces inspected: retro/setup/plan skills, provider catalog, model selection, session reports and CLI configuration.
- Plausible first-party paths checked: session retrospect, installing MCP, choosing new providers and user-authored AGENTS.md changes.
- Why no material first-party path remains: none establishes external prospective distinctions converted into options and a return to current organizational capability via an evidenced S3 relation.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy matter reaching legitimate authority and returning as a governing organizational identity decision is shipped.
- Disturbance / variety regulated: unsafe tool calls, plan uncertainty and user trust preferences are routine work restrictions; not ultimate purpose conflicts.
- Decisive decision or feedback right: human approves plan/tool calls, developer changes configuration; no dedicated policy identity dispute route to legitimate authority is shown.
- Decision owner: host user/project developer configures permissions and model identity but is not engaged by a shipped S5 decision protocol.
- Supporting / enforcement mechanisms: `finish_plan`, approval broker, protected paths and config.
- Closure path: approved plan enters build mode and rejected tool calls are blocked, not resolved as a new mission/policy for future operations.
- Why this is / is not agent-owned: single-task approvals and fixed policy do not become S5 even with a human in the loop.
- Evidence: [planning approval](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/tools/plan.ts), [permission policy](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/src/core/permissions.ts), [design non-goals](https://github.com/DaDozlov/harness-agent/blob/dfff7b2bfbd6fb08cb754461124ac8dab2053622/docs/DESIGN.md).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: the project owner ultimately controls software, but the runtime has no shown identity-level governance return path.

### Absence scope

- Surfaces inspected: CLI plan/approval, policy rules, configuration, agent prompts, hooks and library API.
- Plausible first-party paths checked: plan `finish_plan`, protected path checks, per-command approval, developer edits and user feedback.
- Why no material first-party path remains: these concern immediate task execution constraints and lack a specific ultimate-identity conflict adjudication and return path.

## Distributed OSS parent arrangement

The repository's maintainers and developer CI are outside the installed heaw agent system. User-configured browser tester is a functional in-boundary audit constructor rather than an inferred autonomous maintainer review board.

## Self-hosted and non-human modes

Provider-backed chat/run directly supports model-owned S1. Concurrent named or ad-hoc delegates with selected disjoint file scopes support model-selected S2. Optional `/setup` composes a separate browser reviewer and hook; it is not a default independent audit service. No supported self-governing S3/S4/S5 organization is established.

## Recursion

Main agent and independently executing delegated workers each have local model/tool feedback. Their file interference can be mediated by a model-selected permission partition at the shared project recursion; no independent whole-current metasystem is demonstrated.

## Variety and escalation

Tool schema validation, user permission choices, workspace isolation, `files` scoping, hard budgets, task-plan approval and browser tester correction selectively attenuate operational and audit-relevant variety. Reports return to the main coding agent; no evidenced identity-level exceptional path follows.

## Evidence gaps

- Static read of exact commit; no configured provider, live browser or `setup` generation was executed.
- S2 attribution concerns the supported file-scoped parallel-delegate mode only; raw shell commands can bypass file restrictions and overlapping globs are not globally rejected.
- S3* constructor requires actual project setup and a configured app/browser; its shipped recipe is not a default already-running independent auditor or an external ground-truth quality guarantee.
