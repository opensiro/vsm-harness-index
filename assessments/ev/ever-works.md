---
harness_id: ever-works
project_name: Ever Works
repository: https://github.com/ever-works/ever-works
review_ref: e159e7c6ff34fdacbd8967ad92ae42e3311b444b
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ever Works

## Review boundary

- System in focus: the first-party Ever Works Platform AI Agent/Work runtime and shipped tools, task/roster/approval mechanisms, not the Ever® corporate organization, a deployed tenant's governance or vendor-specific agent CLI internals.
- Purpose and identity: convert tenant goals, ideas and work requests into model-generated research, content, code and ongoing changes using provider plugins, prompt/tool loops, scheduled runs and reviewable artifacts.
- Relevant environment: user goals, changing work data, tool observations, plugin failures, research/search outcomes, budgets, task/review feedback, running-agent messages and human decisions.
- Standard-distribution boundary: `packages/agent/src/agents/agent-run.service.ts` and AI dispatch/tool facade, provider and tool plugins, pipeline/graph executors, schedules, task and escalation services, shipped roster templates/onboarding, review gate and work/mission flows.
- Credited operating / distribution surfaces: first-party model/tool/result recurrence in `AgentRunService`; optional configured agent roles and scheduled task runs that persist outputs, messages and usage.
- Adjacent first-party surfaces excluded from ownership: draft specification and proposal documents; frontend screenshots and marketing promises; user-provided agent role definitions and customer mission governance; external coding agent vendor internals; repository CI/security reviews and hypothetical future deployment arrangements.
- First-party modes considered: builtin AI agent run with plugin tools, task-oriented execution, scheduled/heartbeat turns, model-decided workflow graph edges when wired, human-approved tool decisions and standard optional first-party roster templates; external runtime-provider or plugins only where first-party callers reach them.
- Recursion level: one configurable Ever Works tenant/work/mission runtime with operating AI agents; tenant owner or platform administrator is the external parent for permissions and mandate.
- Reviewed revision: `e159e7c6ff34fdacbd8967ad92ae42e3311b444b`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`AgentRunService.runToolLoopInner` provides a substantive first-party action/observation cycle. It assembles system/user context, resolves tool descriptions under owner/work/agent grants, dispatches to a model through the AI facade, records assistant text and tool calls, executes each recognized tool, appends an untrusted-data-wrapped result as a `tool` message, and repeats up to a bounded number of model round trips. It records token use and captures turn artifacts; steering and interrupt requests are checked between iterations. This is directly supported in the distributed agent package rather than inferred solely from the README's marketing description of autonomous business creation.

Users can configure additional named Agents and assign them scope, roles, budgets, tools, tasks and scheduled/heartbeat work. `AGENT_TEMPLATES` includes a workspace coordinator role that routes requests by lane and escalates ambiguous ownership, plus a competitive analyst role that monitors market changes. `ROSTER_BLUEPRINTS` proposes editable team layouts with one coordination lane. These are shipped building blocks for multi-agent operation; nonetheless the coordinator's written job is intake/delegation, and the blueprint's uniqueness check is initial roster composition. Neither establishes an actual recurring collision among two autonomous S1s with a response closing into *both* subsequent behaviors; no S2 is imputed from a routing template, mailbox, assignment or team chart.

The run's guardrails, policy/tool grants, budget/cost prechecks, run brake, human approval and `AgentEscalationService` can stop or pause individual operations and surface a decision to the responsible user. In particular, the escalation service distinguishes human resolutions that can resume a parked run from agent-proposed notes approved by the owner that do not impersonate a human instruction. Those are meaningful safeguards, but no source evidence shows a single current whole-system S3 with cross-unit work/resource bargaining or a real identity/ultimate-policy dilemma reviewed by S5. The optional workflow graph's LLM edge selection determines the next task step under a user-defined graph; it is not organizational governance by naming.

The reviewer agent is a separate model execution given a task diff and CI brief; a fail-closed guard prevents a retried review from issuing a verdict without its brief. This validates normal code-production artifacts and is not automatically an independent S3* audit of a metasystem's operational claims. The competitive-analyst template and continuous content updates are external-looking task work, but the reviewed system lacks a shown two-way channel whereby prospective organizational options are negotiated with a current S3 and adopted as new operating capability.

Pinned source: [README](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/README.md), [agent run service](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-run.service.ts), [tool service](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-tool.service.ts), [AI dispatch facade](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-ai-dispatch-facade.ts), [agent roster](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/roster-blueprints.ts), [role templates](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-templates.ts), [workflow graph executor](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/workflow-graph-executor.service.ts), [escalation service](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-escalation.service.ts).

## Operational model

An AI Agent run is a functioning S1: model decisions select tools, the system records effect outcomes and re-enters the same model context. Agent templates, task state, scheduling, usage ledgers, approval queues and workflow graphs permit a richer operating organization to be configured. Their existence in the standard distribution does not prove that the software already owns autonomous coordination, current whole-system control, a complementary independent audit, a prospective adaptation regulator or an ultimate policy authority for an arbitrary tenant.

## S1 — Operations

- State: A
- Function: first-party model-selected tool work with observation feedback and optional continuation, scheduled/heartbeat triggers and task outputs.
- Disturbance / variety regulated: open-ended user/tenant tasks, web/search data, tool responses, generated work outcomes, errors, steering messages and budget/context limits.
- Decisive decision or feedback right: choose the next recognized tool calls or final response, interpret returned result messages and re-enter inference; model-selected graph decisions can also advance a configured task workflow.
- Decision owner: model-backed AI run inside `AgentRunService` through `AgentAiDispatchFacade`, not the BullMQ/Trigger scheduling service or static AGENT_TEMPLATES.
- Supporting / enforcement mechanisms: prompt assembly, provider facade, tool descriptions and grants, `invokeTool`, run logs/capture, budget/loop caps, steering, cancellation and tool-result trust fencing.
- Closure path: assembled prompt → model dispatch → emitted tool calls → bounded approved tool execution → result serialized as the next `tool` message → further model round or final answer, with generated artifacts and outcome recorded for subsequent runs.
- Boundary reachability: the runtime's actual `runToolLoopInner` implements this cycle using shipped service dependencies and default plugin path; model credentials and a task/agent instance are installer/tenant inputs.
- Why this is / is not agent-owned: model output determines substantive task actions from the tools exposed; first-party deterministic middleware controls which actions execute but does not decide the work plan.
- Evidence: [agent-run.service.ts](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-run.service.ts), [AI dispatch](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-ai-dispatch-facade.ts), [tool service](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-tool.service.ts), [workflow graph](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/workflow-graph-executor.service.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-path evidence only; no external LLM API, SaaS tenant, Trigger.dev job or generated site was run during assessment.

## S2 — Coordination

- State: —
- Function: no separately evidenced ongoing inter-S1 interference and a coordinating relation that returns a corrective adjustment to the participating operating units.
- Disturbance / variety regulated: role/agent assignment ambiguity, multiple agents receiving tasks, concurrent scheduled runs, shared Work repository operations and task routing.
- Decisive decision or feedback right: coordinator template may send a request to one lane or escalate ambiguity; scope/task permissions, per-agent run brakes, message queues and initial roster constraints enforce individual work boundaries. A concrete clash and closed reciprocal adjustment between two distinct running S1s is not established.
- Decision owner: configured human/team task owner or optional coordinator task agent for ordinary routing; deterministic dispatch, budget, lock and roster logic for enforcement.
- Supporting / enforcement mechanisms: `workspace-coordinator` template, first-party roster proposals, delegation API, task assignment, inbox and dispatch admission gate.
- Closure path: task arrives → model may select a role/delegate → child task result returns to requester, or unresolved assignment asks a human. This is delegation and task intake, not source-confirmed dampening of inter-S1 oscillation/collision.
- Why this is / is not agent-owned: a coordinator title, single lane per role, or multiple agents in a chart does not satisfy the specific distinct-S1/interference/attenuation/feedback requirement.
- Evidence: [agent templates](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-templates.ts), [roster blueprints](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/roster-blueprints.ts), [sub-agent delegation](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/sub-agent-delegation.service.ts), [run dispatch gate](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/run-dispatch-gate.service.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A deployed tenant's mission roster could implement coordination with proper collision evidence; no such execution/contract is silently imported.

### Absence scope

- Surfaces inspected: roster blueprint and coordinator template, delegation services, agent task scheduling, inbox and per-run admission/permission guards.
- Plausible first-party paths checked: ambiguity across specialist lanes, duplicated agents, independent task assignment, shared Work activity and per-agent run brakes.
- Why no material first-party path remains: their returned decisions select/route/stop an individual task or define an initial team; none demonstrates a concrete concurrent S1 disturbance with corrective coordination feedback changing later work of multiple S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no source-confirmed dedicated present whole-system manager with broad operational view and decision power over competing current unit commitments/resources.
- Disturbance / variety regulated: agent tool budgets, per-run credits, tenant policy, task status, schedule and approval holds, retries and questionable run outcomes.
- Decisive decision or feedback right: `AgentBrakeService` blocks an individual paused/archived agent, run dispatch enforces current eligibility, guardrails halt particular risky tools, escalation records send a case to the user. No evidenced first-party regulator reviews the collective work state and reallocates shared commitments/priority in response to conflicts.
- Decision owner: external tenant owner for budgets/rights/approval, deterministic admission/guardrail services for enforcement and task model for ordinary delegated work.
- Supporting / enforcement mechanisms: run admission chain, per-agent status brake, usage ledger, budgets, agent escalation queue and task/work status dashboard.
- Closure path: one run is admitted, parked, stopped, resumed or handed an approval answer; this controls an S1 action, but does not show whole-system current arbitration and returned cross-unit commitment changes.
- Why this is / is not agent-owned: aggregate dashboards, a coordinator template that routes work, and an owner approval queue are not sufficient for S3 without a whole-system feedback/decision relation.
- Evidence: [agent-brake.service.ts](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-brake.service.ts), [run dispatch gate](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/run-dispatch-gate.service.ts), [agent escalation](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-escalation.service.ts), [roster](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/roster-blueprints.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: No tenant-wide resource-negotiating runtime controller was evidenced at the pinned revision.

### Absence scope

- Surfaces inspected: run budgets/credits and brakes, approval/escalation services, task assignment, role templates and workload status channels.
- Plausible first-party paths checked: coordinator role, spend rejection, human priority choice, review gates and pause/resume controls.
- Why no material first-party path remains: these are per-agent or per-action constraints and task routing, without a whole-system present operations feedback view feeding a substantive multi-S1 resource/commitment decision.

## S3* — Complementary audit

- State: —
- Function: no separately mandated complementary audit based on alternative operational access that challenges S3 current management and returns findings to its regulator.
- Disturbance / variety regulated: code defects, CI failures, review-agent disagreement, missing review brief and usage/logging inconsistencies.
- Decisive decision or feedback right: review agent receives a task diff and CI verdict, then approves or requests fixes in normal delivery; run ledger/test outputs record facts for developers/owner.
- Decision owner: review task agent, ordinary CI, owner and developer tests; not a separately scoped S3* audit observer.
- Supporting / enforcement mechanisms: reviewer-agent stage, fresh review brief guard, task-reviewer records, run trace, logs and test suites.
- Closure path: review feedback can change the implementation task before completion, and a missing brief blocks a retry. This is primary QA/production feedback, not an independent audit of current operational management.
- Why this is / is not agent-owned: second-agent review in an ordinary mandatory artifact path remains task quality control unless alternative access and control-return are established.
- Evidence: [agent-run reviewer brief gate](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-run.service.ts), [reviewer records](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/entities/task-reviewer.entity.ts), [run ledger](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/run-ledger.service.ts).
- Basis: structural.
- Confidence: high.
- Caveats: The source's fail-closed reviewer retry prevents hallucinated verdicts; that is strong QA enforcement but not proof of a separate S3* organ.

### Absence scope

- Surfaces inspected: reviewer agents, task review/CI handoff, guardrails, usage/accounting logs and tests.
- Plausible first-party paths checked: independent reviewer model, separate CI verdict, audit trail and developer security tests.
- Why no material first-party path remains: these are coupled to normal task delivery or code constructor assurance, with no separately authorized sampling of S3's managerial assertions and findings-to-S3 correction path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped prospective external/future adaptation loop returning options to the running platform/tenant's present S3 capability.
- Disturbance / variety regulated: market changes, competitor news, content aging, ongoing user business goals and knowledge/work updates.
- Decisive decision or feedback right: a configurable competitive analyst template can research changing external conditions and draft digest content; scheduled pipelines regenerate user-owned work, but no evidence that such intelligence proposes systemic adaptations which a current S3 evaluates/adopts through reciprocal capability feedback.
- Decision owner: task model or optional market-watch agent for commissioned research; external tenant owner for actual strategy/capability decisions.
- Supporting / enforcement mechanisms: `competitive-analyst` template, search plugins, run schedules, pipeline/generator stages, knowledge/memory.
- Closure path: public-source search → model-generated digest or content → reviewable artifact/scheduled refresh. This is S1 output delivery; no S4-to-S3 organizational adaptation choice and return is wired.
- Why this is / is not agent-owned: future-looking research content and continuous site improvement do not necessarily regulate the future viability of the operating system itself.
- Evidence: [competitive analyst template](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-templates.ts), [pipeline executor](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/pipeline/full-pipeline-executor.service.ts), [workflow graph](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/workflow-graph-executor.service.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A specialized tenant can create a future-analysis and policy adaptation process, but that configuration and its closed loop are not pinned in this repository.

### Absence scope

- Surfaces inspected: market-watch template, scheduled generation/updates, missions/ideas/works, plugin search and workflow graph decisions.
- Plausible first-party paths checked: recurring competitor monitoring, research briefs, generation revision and externally grounded task options.
- Why no material first-party path remains: such observations return as task products or content updates, not as future capability alternatives debated with an evidenced present S3 manager and adopted into the operating organization.

## S5 — Policy and identity

- State: —
- Function: no demonstrated ultimate identity/mandate decision and continuing authoritative return at the assessed tenant/agent-system recursion.
- Disturbance / variety regulated: agent prompt identity, tenant role and scope, tool permissions, spend approval, guardrail violations and human escalation cases.
- Decisive decision or feedback right: tenant owner sets prompt/permission/budget, approves a particular tool/action or responds to a stopped run. This is real authorization; no first-party path raises an S3–S4/organizational identity conflict to a legitimate final authority and applies a new governing mandate.
- Decision owner: external tenant/mission owner for role definition and ordinary permissions; deterministic budget, policy/approval and escalation components for enforcement.
- Supporting / enforcement mechanisms: `SOUL.md`/`AGENTS.md` role descriptions, scope/permission checks, guardrails, action proposals, human-owned escalation and result attribution.
- Closure path: a tool/action failure creates an escalation → human note can resolve it and resume the parked run. Agent-proposed resolution is labeled as such and does not masquerade as the owner's instruction; no demonstrated constitutional identity question or authoritative system-policy return exists.
- Why this is / is not agent-owned: no account/role-setting UI, editable agent identity prompt or human pause/approval by itself meets S5 identity adjudication closure.
- Evidence: [agent escalation service](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-escalation.service.ts), [agent templates](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/agent-templates.ts), [guardrails](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/agents/guardrails.ts), [agent action proposal](https://github.com/ever-works/ever-works/blob/e159e7c6ff34fdacbd8967ad92ae42e3311b444b/packages/agent/src/entities/agent-action-proposal.entity.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Human real-world business/tenant policy may be a separate parent S5, but the assessment cannot impute that organization's actual adjudications from installed templates or permission fields.

### Absence scope

- Surfaces inspected: agent identity/role files, tool grants, tenant/mission scopes, guardrails, action proposals and human escalation routing.
- Plausible first-party paths checked: editable SOUL/prompts, changing agent scope, spend/policy veto, an agent reaching a human decision card and resuming afterward.
- Why no material first-party path remains: the reviewed closures concern task permissions and execution limits, not an explicit conflict about the organization's ultimate identity or survival priorities adjudicated by a legitimate policy authority and returned to all relevant regulation.

## Distributed OSS parent arrangement

Ever Works Platform maintainers build the runtime, the tenant/mission owner configures purposes and permissions, and external model/plugin providers supply configurable services. An actual business strategy committee or company policy cannot be inferred from repository's branding and user-editable agent prompts. Draft specs and roadmap entries are architecture context only, not evidence of a running higher VSM function.

## Self-hosted and non-human modes

Self-hosted API, web, CLI, plugins and model providers are supported; scheduled and heartbeat agents can run model/tool turns autonomously under the owner's grants. Optional role rosters and task handoffs are present; they do not themselves form S2/S3. Untrusted external tool content is explicitly fenced before re-entering the model, and owner steering/interrupt is checked between calls.

## Recursion

Each named Agent's model/tool run is an operational unit. The tenant/work hierarchy and team templates allow roles to be instantiated at nested scopes, with work-specific data and shared task APIs. A tree of Mission/Idea/Work, a coordinator named Ada or a generated agent count does not establish complete nested viable systems without material coordination and metasystem closure at each level.

## Variety and escalation

Tool grants, usage/budget limits, run interruption, approval, agent brake, role scope, bounded loop iterations, prompt-injection fencing and task review attenuate operational variety. Escalation queues and user action cards can move exceptional cases to a parent human who may resume work; they are not in themselves a VSM algedonic channel or S5 identity authority absent the requisite receiving decision and closure.

## Evidence gaps

- Reviewed source at pinned commit; no live AI provider, hosted deployment, generated business, production task or independent model/human evaluator was run.
- The model/tool loop is first-party and specific; broad 24/7 autonomous-business claims in README were not taken as proof of complete VSM metasystem ownership.
- First-party coordinator and competitor-watch templates are optional agent/task roles. Their names/prompts and initial roster routing alone are insufficient to prove interference-damping S2 or S3–S4 strategic-adaptation relations.
- Reviewer-agent gates, CI, user-approved escalations and developer verification were kept distinct from independent S3* audits and ultimate S5 mandates.

## Assessment summary

Ever Works has a substantive first-party model/tool/observation loop with scoped tools, steering and persisted outcomes: **`S1=A`**. It also ships sizable task, roster, market-watch, reviewer, budget and escalation machinery. The pinned standard-distribution source does not demonstrate the additional function-specific inter-S1 collision closure, whole-system current management, independent complementary audit, prospective S3–S4 organizational adaptation or legitimate identity-level adjudication needed to credit S2/S3/S3*/S4/S5. Proposed vector **`A / — / — / — / — / —`**.
