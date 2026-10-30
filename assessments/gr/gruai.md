---
harness_id: gruai
project_name: gruAI
repository: https://github.com/andrew-yangy/gru-ai
review_ref: 8fba47928a0fe3fdfda7a31d22b73625c78cbfc4
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# gruAI

## Review boundary

- System in focus: the gruAI first-party packaged Claude Code agent roster, `/directive` execution workflow, `/scout` future-environment workflow, CLI, spawn adapters, scheduling and validation hooks at the pinned commit, not an arbitrary unconfigured Claude session.
- Purpose and identity: transform a human CEO directive into scoped team work, execute and review it through an auditable multi-step pipeline, retain lessons, and research emerging future opportunities for authorized initiatives.
- Relevant environment: changing codebases and tasks, parallel agent collisions, tool/test outcomes, human CEO approvals, competitors, platform updates and user signals.
- Standard-distribution boundary: `gru-ai init` scaffolds agent definitions, skills, hooks and `.context` state; Claude Code supplies inference/tool execution, while the first-party directive/scout workflows control role responsibilities and feedback.
- Credited operating / distribution surfaces: `.claude/skills/directive`, `.claude/skills/scout`, agent personas and registry, CLI scaffold, review/casting gates, `scripts/spawn-agent.ts`, platform adapters, scheduled scout, foreman and dashboard state views.
- Adjacent first-party surfaces excluded from ownership: example company-specific targets and historical `.context` reports/logs, visual game UI, benchmark results, integration tests and external user-approved deployment/merge actions.
- First-party modes considered: interactive `/directive` with lightweight to strategic weights; multi-worker executor and review waves; CEO gates; `/scout` manually invoked or scheduled; detached/tracked CLI agents and foreman queue launching.
- Recursion level: project team of role-scoped model-based S1 agents, a model-driven COO coordinating current portfolio, plus a prospective scout function, governed by an outside human CEO.
- Reviewed revision: `8fba47928a0fe3fdfda7a31d22b73625c78cbfc4`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI scaffolds a roster of agent personas, lifecycle instructions and guardrail hooks for a project. A human starts `/directive` or a configured foreman starts available work. The first-party directive skill tells the model orchestrator to triage, audit, cast, plan, dispatch specialist model agents, examine their work and retry failed reviews, persist statuses and request human approval at bounded gates. Dedicated `ClaudeCodeSpawnAdapter` starts real Claude Code CLI model sessions with agent identity, prompt and working directory. The same package includes `/scout`: four model-based role scouts search external information, a COO aggregates competing signals and proposes initiatives, and configured strong signals/CEO-approved items can enter the directive queue. A scheduled script calls `/scout` via `claude -p`. This is evidence of an implemented *available mode*, not proof of a live installation or observed production performance.

Pinned source evidence:

- [README: pipeline, agent roles and install path](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/README.md)
- [CLI initialization and installed agent roster](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/cli/commands/init.ts)
- [Directive skill: fifteen model-led phases and feedback progression](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/skills/directive/SKILL.md)
- [COO model agent ownership and casting/circuit breakers](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/agents/morgan-coo.md)
- [Plan composition and review gate](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/skills/directive/docs/pipeline/05-planning.md)
- [Wave computation, shared-file interference and returned review loop](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/skills/directive/docs/pipeline/09-execute-projects.md)
- [Constructed review integrity checker](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/hooks/validate-reviews.sh)
- [Human completion decision gate](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/skills/directive/docs/pipeline/11-completion-gate.md)
- [Prospective external scout and initiative consolidation](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/.claude/skills/scout/SKILL.md)
- [Available scheduled `/scout` entry](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/scripts/scheduled-runs.sh)
- [Real Claude Code process adapter](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/server/platform/claude-code-spawn.ts)
- [Generic first-party agent-spawn entry](https://github.com/andrew-yangy/gru-ai/blob/8fba47928a0fe3fdfda7a31d22b73625c78cbfc4/scripts/spawn-agent.ts)

## Operational model

The CEO defines the objective and constraints. The bundled orchestrator invokes model roles to evaluate scope and current state; the COO assigns scoped work and reviewers, while separate builders choose code/tool interventions, consume observations and revise changes. An instructed wave computation and hooks prevent colliding edits or unsupported completion. Reviewers give feedback to builders, and the orchestrator controls the current workflow until the external CEO approves completion. In parallel as an available prospective mode, scouts choose external research queries, interpret findings and return prioritized future initiatives into a proposal/inbox/directive path. Claude Code is the packaged inference/tool runtime dependency; human approvals are not attributed to the model.

## S1 — Operations

- State: A
- Function: model-driven specialist engineering, auditing, designing and other directive tasks within their scoped project contexts, with tool observations and revision cycles.
- Disturbance / variety regulated: changing requirements, source defects, failing tests, review findings and variable task complexity.
- Decisive decision or feedback right: choose next code/document/tool action on the scoped goal and revise it after tool/reviewer observations.
- Decision owner: spawned model-based Claude Code role agents (engineer/QA/CTO etc.) operating under first-party `.claude/agents` personas and `/directive` work instructions.
- Supporting / enforcement mechanisms: Claude Code CLI tool executor, role templates, task Definition of Done, isolated worktrees, step status JSON, reviews and safety hooks.
- Closure path: assigned goal/DOD → spawned model worker selects actions and reads results → evaluator returns issues → worker fixes/rechecks → completed artifact or escalation to orchestrator.
- Why this is / is not agent-owned: task-specific decisions reside in model roles under the shipped task contract; the CLI adapter only launches them and does not autonomously solve tasks.
- Evidence: README pipeline, `/directive`, `09-execute-projects.md`, `scripts/spawn-agent.ts`, role personas and Claude CLI adapter.
- Basis: explicit source-to-spawn-to-review control path, not an inferred model feature from names.
- Confidence: medium-high.
- Caveats: live provider quality and all claimed automated end-to-end runs unverified; role sessions require installed Claude Code and access.
- Boundary reachability: the init scaffold installs the skill/roles and `/directive` invokes them through the supported CLI adapter; results feed project state and review phases.

## S2 — Coordination

- State: C
- Function: prevent concrete cross-worker file/edit collisions while allowing parallel non-overlapping S1 work, and enforce separation of builder/reviewer roles.
- Disturbance / variety regulated: two builders changing overlapping files, global configuration file edits and incompatible simultaneous dependency work.
- Decisive decision or feedback right: sequence conflicting S1 tasks into different waves and allow only disjoint file scopes to execute in one parallel wave.
- Decision owner: constructor-specified `computeWaves` algorithm in the shipped execution protocol, executed by the orchestrating agent; static global sequential file set and file-overlap rule bound decisions.
- Supporting / enforcement mechanisms: audit `active_files[]`, task dependencies, `MAX_PARALLEL=3`, overlap detection, post-wave changed-file comparison and reviewer identity validation.
- Closure path: pending S1 task scopes → compute dependency/file-conflict wave → launch safe workers → compare changed files, review/repair → subsequent wave eligible after prior tasks finish.
- Why this is / is not agent-owned: the attenuation rule is constructor-authored, not a free model-authorized cross-team strategy; nonetheless it addresses specific interference between autonomous S1 writers.
- Distinct S1 units: per-task Claude Code builder sessions, including concurrently active specialist agents on the same project tree.
- Inter-S1 disturbance: overlapping `active_files` or shared global config operations can corrupt/overwrite another worker's changes.
- Attenuating coordination relation: deterministic wave planner refuses concurrent file intersections and serializes global modification files, bounded by dependency readiness.
- Feedback into subsequent S1 behaviour: waves complete and changed files are compared to the predicted set; remaining tasks enter later waves only after prior completions, and reviews feed repairs back to builders.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the explicit file-overlap interference model *changes* which otherwise-ready independent S1 tasks can act simultaneously, preventing destructive concurrent edits rather than merely passing messages.
- Evidence: `09-execute-projects.md` wave algorithm, `05-planning.md` cast validation, `.claude/hooks/validate-cast.sh` and `validate-reviews.sh`.
- Basis: explicit normative executable instructions plus gate scripts in the installed workflow.
- Confidence: medium; protocol specifies the algorithm but there is no independent measured production collision benchmark at this pinned source.
- Caveats: post-wave drift is warning-only; S2=C is bounded to specified scheduling and role constraints, not proof of comprehensive runtime concurrency safety.
- Boundary reachability: `/directive` execute phase requires the wave manifest and uses `scripts/spawn-agent.ts` for parallel CLI builders; conflicts influence later planned waves.

## S3 — Inside-and-now control

- State: A
- Function: model-led COO orchestration of the present directive portfolio: challenge scope, audit state, assign role agents, select plan, reprioritize, review outcomes and escalate when gates fail.
- Disturbance / variety regulated: changing goals, active file scope, task dependencies, unavailable workers, repeated review failures, cost and inconsistent project progress.
- Decisive decision or feedback right: select and revise the current execution plan/cast across multiple specialist S1 workers, determine when to stop/rescope and return a corrected directive state.
- Decision owner: the first-party COO model persona and directive orchestrator under the user's approved intent, with CTO/QA evidence inputs.
- Supporting / enforcement mechanisms: audit artifacts, `plan.json`, `project.json`, `directive.json`, step dependency guards, reviewer artifacts, task statuses, dashboard watcher and scripted scheduler capacity cap.
- Closure path: CEO directive/current state → audit/COO whole-plan judgment → assign and sequence specialist tasks → collect review and completion feedback → adjust/escalate or present digest to CEO.
- Why this is / is not agent-owned: the COO decides the active plan, casting, phasing and tradeoffs from source/audit evidence; separate scripts only validate/record that current control.
- Whole-system current view: directive goals, projects, DOD statuses, candidate agents, current backlog, lessons and budget/role constraints assembled before COO plan and subsequent reports.
- Current-control decision scope: model-based allocation of builders/reviewers, sequencing, risk/escalation and present directive work; external CEO alone owns final acceptance and high-risk authorization.
- Evidence: `morgan-coo.md`, `/directive/SKILL.md`, `05-planning.md`, `09-execute-projects.md`, `10-wrapup.md` and README.
- Basis: encoded role/planning and return architecture with checkable state contracts.
- Confidence: medium-high for available mode; no production performance assertion.
- Caveats: this is bounded current work control, not business-wide governance of every linked product or independent authority to approve a release.
- Boundary reachability: `/directive` explicitly invokes COO planning, writes approved project plan, launches roles, reads returned reviews and progresses to a digest/CEO gate.

## S3* — Complementary audit

- State: —
- Function: mandatory task peer review, QA and mechanical casting/review validations improve quality but do not evidence an independent complementary audit institution of the whole S3 control loop.
- Disturbance / variety regulated: self-review, incomplete DOD, hidden implementation regressions and omitted verification.
- Decisive decision or feedback right: independently test the current S3 controller's account of actual organization-wide operations and return a binding management challenge.
- Decision owner: assigned CTO/reviewer inside normal task workflow; no separate first-party independent S3* actor with complementary access to S3 is established.
- Supporting / enforcement mechanisms: fresh-context code-review prompts, `validate-reviews.sh`, `validate-cast.sh`, project DOD and review artifacts.
- Closure path: builder artifact → reviewer observations → builder repair/ordinary gate → COO completion flow; not a distinct system-wide S3* → S3 challenge path.
- Why this is / is not agent-owned: independent *task* review is not automatically independent *organizational* audit; reviewers are selected by the current planning chain.
- Evidence: `09-execute-projects.md`, `validate-reviews.sh`, `05-planning.md`.
- Basis: separate task-check vs complementary whole-system audit test.
- Confidence: medium-high.
- Caveats: product claims about fresh contexts do not independently attest reviewer independence in a deployed environment.

### Absence scope

- Surfaces inspected: reviewer casting, fresh-context code-review procedure, QA roles, mechanical completion/review gates and dashboard/reporting.
- Plausible first-party paths checked: reviewer ≠ builder as S3*, code review as independent audit, task DOD gate as organization-wide audit.
- Why no material first-party path remains: quality checks feed ordinary builder/COO execution without a separately independent whole-current-control challenge and S3 corrective return.

## S4 — Outside-and-then intelligence

- State: A
- Function: model-led prospective scanning of external technology, competition, user and ecosystem signals, with synthesis into prioritized future directives and possible operational adaptation.
- Disturbance / variety regulated: changes to frameworks/security advisories, competitor moves, emerging markets, user needs and prospective workflow technologies.
- Decisive decision or feedback right: autonomously select external research questions, weigh competing signals and propose initiatives/capability changes for authorized backlog/directive promotion.
- Decision owner: first-party CTO/CPO/CMO/COO model scouts and COO consolidator; human CEO retains acceptance of ordinary proposals and high-risk decisions.
- Supporting / enforcement mechanisms: WebSearch/WebFetch instructions, prior scouting archive, goal alignment, urgency schema, cross-scout signal strengths, backlog triggers, `/scout` and scheduled `claude -p` entry.
- Closure path: external developments → multi-domain agent research → independent proposed actions → COO cross-domain relevance/urgency synthesis → CEO review or bounded strong-signal inbox promotion → approved directive executed by S1/S3 pipeline.
- Why this is / is not agent-owned: research queries, interpretation, consolidation and prioritized option selection are explicit model-agent responsibilities; script scheduling and CEO gate are support and authorization, respectively.
- Prospective environment view: technology CVEs and releases, competition/customer signals, growth landscape and workflow ecosystem not just current repo health.
- Future option/adaptation decision: propose ranked specific initiatives with scope, evidence, risk and process; cross-reference pending backlog triggers to promote actionable work.
- Return into operating capability: proposals accepted by CEO, plus specified strong signals, create/promo inbox directives that the first-party `/directive` workflow can act on; adoption is not guaranteed without authorization.
- External distinction: scouts search competitors, platform advisories, market/customer signals and future framework choices, rather than merely the local build's current defects.
- Future / prospective distinction: they assess changes that might affect later product viability and workflow capabilities; the goal is option selection before commitment, not incident response to an already assigned task.
- Adaptation option generated: source schema requires evidence-linked prioritized initiatives with risk, recommended process and scope; COO can promote validated multi-scout signals to inbox directives.
- Path back into current capability / S3: approved or bounded automatically promoted initiative becomes a directive that the active COO-and-specialists operating workflow can plan and execute, subject to CEO gates.
- Evidence: `/scout/SKILL.md`, `scripts/scheduled-runs.sh`, COO persona, `/directive` consumption path and README.
- Basis: implemented, reachable prospective scout protocol with bounded return, not mere roadmap language.
- Confidence: medium; live search/approval/execution was not performed.
- Caveats: hardcoded example installation paths require deployment configuration; not proof autonomous approval of strategic changes, and model-generated prospective findings may be wrong.
- Boundary reachability: `/scout` is shipped as a first-party skill, `scripts/scheduled-runs.sh scout` invokes it via Claude CLI, and its initiatives/trigger promotions feed the same `.context` directive/backlog structure used by normal execution.

## S5 — Policy and identity

- State: —
- Function: the CEO's vision, standing preferences, approval gates and agent personas constrain execution but do not create first-party model authority to resolve ultimate identity/policy conflicts.
- Disturbance / variety regulated: ambiguous purpose, unsafe high-risk changes, conflicting priorities and mistakes in approval or scope.
- Decisive decision or feedback right: legitimately adjudicate contested mission/identity and constitutional policy, then bind the operating organization to the decision.
- Decision owner: external human CEO defines vision and must approve plan/completion; model personas obey inherited constraints and cannot unilaterally change them.
- Supporting / enforcement mechanisms: `.context/vision.md`, preferences, triage/classification rules, human clarification/plan/completion stop gates and `validate-gate.sh`.
- Closure path: external CEO decision → scaffolded policy and approval status → bounded S1/S3 execution; no independent first-party ultimate-policy judgment and constitution-changing return.
- Why this is / is not agent-owned: naming the user CEO and the model COO does not demonstrate that software legitimately owns organizational S5. The explicit mandatory human gate identifies the outside owner.
- Evidence: `/directive/SKILL.md`, `11-completion-gate.md`, `07-plan-approval.md`, README.
- Basis: decision-right and human-stop trace.
- Confidence: high for bounded exclusion.
- Caveats: real-world team could include its human CEO in a broader assessed organization; no automatic parent-assisted autonomy credit is inferred here.

### Absence scope

- Surfaces inspected: human approval gates, CEO role, vision/preferences, agent policy/persona files, scout initiative handoff and directive completion options.
- Plausible first-party paths checked: CEO persona/vision as S5, COO challenge mode as policy adjudication, strategic scout authority as ultimate purpose setter.
- Why no material first-party path remains: these are subordinate proposal, operational control and external approval mechanisms, not legitimate software-owned ultimate identity-level authority.

## Recursion

Specialist Claude Code role workers are S1 operations at the project/team recursion; the COO works at their active directive whole-system scope. The separate prospective scout unit returns opportunities to that operational system. Human CEO and provider-controlled Claude runtime are dependencies/authority edges, not additional claimed first-party S5 agents.

## Variety and escalation

Model workers handle open-ended task variety, while constructor-specified wave and review gates attenuate collisions and self-certification. The COO reallocates current effort from audit/review evidence; scout roles amplify external future variety into actionable proposals. Clarification, plan and final approval escalate to the CEO; failures cannot be bypassed by attributing those rights to a model.

## Evidence gaps

- Static source-first inspection at frozen revision. No installed agent E2E, actual Claude provider run, human CEO interaction, external WebSearch, production collision measurements or independent auditor was performed.
- Some sources document an executable protocol in model instructions rather than a deterministic TypeScript runtime. Positive functions refer to the *supported packaged mode* and its reachable invocation, not proof each session complied flawlessly.
- Scheduled scout script contains example absolute user paths; automatic production scheduling is not proven, but documented `scout` invocation and Claude CLI entry exist.
- Peer-review separation is evidenced at task level only. S3* independent whole-organization audit and S5 legitimate constitutional authority are not inferred.

## Assessment summary

**Proposed disposition: `included`.** The package provides model-based specialist S1 work, concrete constructor-owned scheduling attenuation of overlapping S1 files (S2=C), model COO whole-directive present control (S3=A), and a distinct model-led external prospective `/scout` loop with a governed return into directives (S4=A). No independent complementary S3* or model-owned ultimate S5 authority. Vector: **A · C · A · — · A · —**.
