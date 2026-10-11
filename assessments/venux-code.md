---
harness_id: venux-code
project_name: Venux Code
repository: https://github.com/venux/venux-code
review_ref: 598ef18a3f3372be0178693af69748f0049058ca
reviewed_at: 2026-10-11
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

# Venux Code

## Review boundary

- System in focus: the supported first-party Venux Code Python terminal coding agent and its current interactive `VenuxApp` → `VenuxAgent` model/tool loop, along with shipped but separately optional/developer-facing DeepAgent, delegation, cron, permission, memory and pub/sub components at one local instance/one coding request.
- Purpose and identity: fulfil the user's software exploration, edits, patch and shell requests with model-directed tool feedback and access to local session context, skills and permissions.
- Relevant environment: user code/working tree, commands/files, model provider results, session database, user prompts and approvals, scheduled user-specified jobs, filesystem memory and external MCP/web services when configured.
- Standard-distribution boundary: pinned Python package `src/venux_code` installed and launched via declared `pyproject.toml` CLI, its native LangGraph loop, tool registry and first-party helper modules. Third-party LangGraph/DeepAgents and provider inference are treated as substrates; external users, servers, CI/development scripts and hypothetical compositions are not imported as native VSM owners.
- Credited operating / distribution surfaces: [pyproject.toml](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/pyproject.toml); [README.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/README.md); [src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py); [src/venux_code/cli/main.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cli/main.py); [src/venux_code/llm/agent/agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/agent.py); [src/venux_code/llm/agent/state.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/state.py); [src/venux_code/llm/tools/registry.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/registry.py); [src/venux_code/llm/tools/bash_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/bash_tool.py); [src/venux_code/llm/tools/edit_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/edit_tool.py); [src/venux_code/llm/tools/delegate_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/delegate_tool.py); [src/venux_code/llm/agent/deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/deep_agent.py); [src/venux_code/cron/scheduler.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/scheduler.py); [src/venux_code/cron/runner.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/runner.py); [src/venux_code/cron/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/service.py); [src/venux_code/pubsub/broker.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/pubsub/broker.py); [src/venux_code/memory/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/memory/service.py); [src/venux_code/permission/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/permission/service.py); [src/venux_code/skills/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/skills/service.py); [tests/test_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/tests/test_agent.py); [tests/test_deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/tests/test_deep_agent.py); [tests/test_delegation.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/tests/test_delegation.py).
- Adjacent first-party surfaces excluded from ownership: [CONTRIBUTING.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/CONTRIBUTING.md) and [CHANGELOG.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/CHANGELOG.md) are maintainer governance/history. [docs/DEEP-AGENT.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/docs/DEEP-AGENT.md) and [docs/CRON.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/docs/CRON.md) document callable modules but cannot establish an untraced default wiring or model-owned whole-organization management. Direct external LangGraph provider behavior is not credited as first-party VSM governance.
- First-party modes considered: installed ordinary CLI/TUI agent built by `VenuxApp.create`; direct `DeepAgent.run` constructor and its plan/execute/review; manually registered DelegateTool and fallback agent; cron service configured with an agent factory; async pub/sub; memory and permissions.
- Recursion level: one Venux Code installation executing individual user coding goals. A stored plan's multiple steps, scheduled user jobs, provider aliases and event subscribers do not automatically form a group of independently governed operative S1 organizations.
- Reviewed revision: 598ef18a3f3372be0178693af69748f0049058ca.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py) constructs `ToolRegistry(include_defaults=True)`, provider and `VenuxAgent`; [src/venux_code/llm/agent/agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/agent.py) compiles a LangGraph `call_llm → execute_tools → call_llm` graph. The model chooses tool calls, and results from a real `ToolNode` are returned to subsequent model turns. [src/venux_code/llm/tools/registry.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/registry.py) lists ten default tools (shell/edit/glob/grep/list/read/write/fetch/search/patch); although it imports `DelegateTool`, that class is **not** included in `_DEFAULT_TOOLS`, nor is the optional DeepAgent constructed in `VenuxApp._init_agent`. This prevents importing capabilities from a class name into the ordinary installed CLI mode.

[src/venux_code/llm/tools/delegate_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/delegate_tool.py) implements a separately registrable tool that creates a fresh delegate session with its own prompt/context and a model-directed fallback agent, awaited via timeout. Its comment about possible parallel investigations is not direct proof of active cross-delegate conflict arbitration. [src/venux_code/llm/agent/deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/deep_agent.py) implements a callable phased plan/execution/review loop: steps execute sequentially, results are kept in `ExecutionPlan`, and `ReviewPhase` asks an LLM to judge a **formatted plan-and-step-result summary**, potentially resetting selected failed steps. No separate independent raw code artifact inspection by the reviewer or first-party whole-current S3 audit return was found.

[src/venux_code/cron/scheduler.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/scheduler.py) schedules jobs and [src/venux_code/cron/runner.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/runner.py) can call an injected agent factory or shell script with results delivered to configured recipients. [src/venux_code/pubsub/broker.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/pubsub/broker.py) broadcasts events to subscriber queues. [src/venux_code/memory/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/memory/service.py) saves/searches user context, and [src/venux_code/permission/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/permission/service.py) stores tactical allow/deny decisions. These are useful current-work services but do not demonstrate a cross-S1 feedback conflict regulator, whole-current portfolio management, complementary independent audit, prospective adaptation or ultimate policy authority.

## Operational model

Default operation has one native model-directed coding agent with tool/result continuation. A developer may instantiate and register a separate subagent, invoke the standalone deep-agent three-phase review loop, or wire the cron factory for other task runs; those components remain bounded task execution/control rather than evidence of an autonomously governed multi-unit organization. The review phase and user confirmations may improve current work but are not by themselves S3* or S5.

## S1 — Operations

- State: A
- Function: perform user-directed programming work using model-chosen shell/file/search/patch tools and feedback, with alternative direct DeepAgent and optional subordinate runs available as separate task-operative constructors.
- Disturbance / variety regulated: changing repository facts, tool errors, incomplete work, provider responses, plan-step outcomes, failed commands and missing context.
- Decisive decision or feedback right: model chooses the next tool and whether to continue after receiving real observations; in direct DeepAgent mode the model chooses plan and reviews progress to retry a step.
- Decision owner: first-party Venux model/tool `VenuxAgent` operational loop, assisted by injected provider; optional DeepAgent roles only control the task they execute.
- Supporting / enforcement mechanisms: LangGraph state and ToolNode, tool registry, context char budget, iteration cap, built-in tools, session persistence, permissions and skills.
- Closure path: input request → model chooses tool → first-party LangGraph ToolNode acts on workspace → result fed into same graph → model selects next action or responds.
- Boundary reachability: `VenuxApp.create` with a provider actually constructs `VenuxAgent`, builds its tool list and exposes the run method through CLI; no external managed-worker entity is required.
- Why this is / is not agent-owned: without a model's situated tool choice and interpretation of returned observations, the registry and scheduler do not choose a substantive code action.
- Evidence: [src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py); [src/venux_code/llm/agent/agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/agent.py); [src/venux_code/llm/tools/registry.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/registry.py); [src/venux_code/llm/tools/bash_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/bash_tool.py); [src/venux_code/llm/tools/edit_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/edit_tool.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: successful end-to-end performance with real model credentials was not measured.

## S2 — Coordination

- State: —
- Function: no first-party native active inter-S1 contention detection and regulatory feedback was established.
- Disturbance / variety regulated: independently invoked agents or scheduled jobs could conflict over files, but the installed first-party loop provides tool execution and event queues rather than an active shared-resource conflict owner.
- Decisive decision or feedback right: no native cross-worker allocation arbitration, contention monitor, exclusive task claim or returned interference correction observed.
- Decision owner: current root coder for its task; APScheduler and async broker implement deterministic events/times, not a model-owned cross-S1 regulator.
- Supporting / enforcement mechanisms: optional DelegateTool, scheduling, task list/plan, subscriber queues, permissions.
- Closure path: child/scheduled job executes on request and returns output (or publishes event); no conflicting S1 claim is observed and attenuated with concrete feedback to multiple workers.
- Why this is / is not agent-owned: spawning a child and broadcasting current events do not close an inter-S1 oscillation/interference path.
- Evidence: [src/venux_code/llm/tools/delegate_tool.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/delegate_tool.py); [src/venux_code/llm/tools/registry.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/tools/registry.py); [src/venux_code/cron/scheduler.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/scheduler.py); [src/venux_code/pubsub/broker.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/pubsub/broker.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: no proof of absence in externally composed custom multiprocessing harnesses; those remain outside the assessed first-party standard mode.

### Absence scope

- Surfaces inspected: main graph, default tools, optional child tool/fallback, DeepAgent loop, cron and pub/sub services, session/permissions.
- Plausible first-party paths checked: shared file-lock, simultaneous worker resource claims, peer-task conflict notification, arbitration policy and returned next-action regulation.
- Why no material first-party path remains: reachable documented structures provide single coding feedback or ordinary task scheduling/messaging without identified cross-S1 collision loop.

## S3 — Inside-and-now control

- State: —
- Function: no native whole-current management across independently executing first-party S1 commitments and resources is established.
- Disturbance / variety regulated: multistep plans, failures and time-based user jobs affect individual operation but no global current portfolio decision among subordinate operative teams is evidenced.
- Decisive decision or feedback right: `DeepAgent` model decides how to execute/retry its *own goal*; cron runner schedules fixed user work, not management tradeoffs across a currently operating agent organization.
- Decision owner: current-task planner/reviewer and human scheduler, not independently attributable current-organization S3.
- Supporting / enforcement mechanisms: plan steps/dependencies, cron service, optional subagents, session DB, TUI events and provider settings.
- Closure path: one plan's status feeds its own execution retries; no whole-current organization view → resource/commitment judgment → binding corrected obligations for independent S1s.
- Why this is / is not agent-owned: model ownership of local planning/retry alone is S1 regulation, not a whole-current managerial authority.
- Evidence: [src/venux_code/llm/agent/deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/deep_agent.py); [src/venux_code/cron/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/service.py); [src/venux_code/cron/runner.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/runner.py); [src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a human organization can deploy multiple copies, which is not first-party Venux S3.

### Absence scope

- Surfaces inspected: all direct DeepAgent phases, current default CLI wiring, optional child agent, scheduler and broker, memory/session services.
- Plausible first-party paths checked: simultaneously operating worker portfolio, active worker status/commitment overview, tradeoff and capacity decisions, corrective role reassignment sent back to several operative units.
- Why no material first-party path remains: source supports one plan-and-goal execution or user-defined scheduled jobs, but not an organizational management parent.

## S3* — Complementary audit

- State: —
- Function: no first-party sufficiently independent alternative access to operational truth with findings returned to a distinct current control owner was established.
- Disturbance / variety regulated: model may wrongly report a plan complete or skip defects, but direct DeepAgent `ReviewPhase` receives the producing plan's stored step-status/result text, not independently acquired code/test truth.
- Decisive decision or feedback right: review model selects `goal_achieved`/retry step IDs *within the same task*; it neither audits independently sampled artifacts nor directs an independent S3 parent.
- Decision owner: direct DeepAgent review model for task feedback and user for final action; no separate organizational audit actor or returned S3 decision owner.
- Supporting / enforcement mechanisms: formatted `ExecutionPlan` summary, JSON review, retry cap, optional filesystem saves of plan/step/review and unit tests for the developer.
- Closure path: execution step summary → in-band review LLM → retry selected steps of same goal. **No independent raw-artifact audit → finding → separate S3 management → operational correction**.
- Why this is / is not agent-owned: a distinct prompt/role can exercise ordinary S1 quality reflection without independent evidence or current-control return. The name `ReviewPhase` does not establish S3*.
- Evidence: [src/venux_code/llm/agent/deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/deep_agent.py); [src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py); [src/venux_code/llm/agent/agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/agent/agent.py); [tests/test_deep_agent.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/tests/test_deep_agent.py).
- Basis: explicit + structural.
- Confidence: high within source boundary.
- Caveats: a separately built external evaluator or human code reviewer would need separate evidence and returned control before S3* could be credited.

### Absence scope

- Surfaces inspected: DeepAgent review prompt and concrete data inputs, retry mechanics, filesystem review-save path, ordinary tool/plan loops, tests and default CLI.
- Plausible first-party paths checked: independently selected raw file/test/eval evidence, dedicated audit autonomy and independence, findings addressed to separate S3 governance actor, enforced audit-conditioned action and reinspection.
- Why no material first-party path remains: reviewer consumes only the producing task's result summary, and its corrections stay inside that same goal rather than being routed to current-control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no systematic future-facing external environment sensing with comparative capability adaptation and current-control return is wired.
- Disturbance / variety regulated: provider changes, skills, memory/user history and cron timing are inputs to current tasks or user-configured jobs, not future organizational viability hypotheses.
- Decisive decision or feedback right: model chooses next current coding step; user chooses scheduled jobs and configurations; no first-party future capability adaptation policy/judgment.
- Decision owner: individual task agent/user settings, not an implemented S4 sensing/adaptation module.
- Supporting / enforcement mechanisms: memory search, stored profile, skill lookup, LLM registry, cron scheduling and context budget.
- Closure path: history/provider/skill affects current prompt, but no external trend observation → tested adaptation option → current S3 decision → organizational capacity change.
- Why this is / is not agent-owned: persistence and scheduled requests do not make a dedicated outside-then adaptation process.
- Evidence: [src/venux_code/memory/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/memory/service.py); [src/venux_code/skills/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/skills/service.py); [src/venux_code/cron/scheduler.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/cron/scheduler.py); [src/venux_code/llm/providers/registry.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/llm/providers/registry.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: users may ask an agent to research future technologies, but the task itself does not establish native S4.

### Absence scope

- Surfaces inspected: configured providers/skills, retained memory, time-based jobs, task planner/reviewer, app lifecycle and CLI controls.
- Plausible first-party paths checked: proactive environmental scanning, future capability option creation, alternative testing and two-way S4/S3 capacity arbitration.
- Why no material first-party path remains: source-scoped facilities store present context or run scheduled current user instructions, not prospective organizational change.

## S5 — Policy and identity

- State: —
- Function: no native highest-level system identity/ethos adjudication with binding policy return is demonstrated.
- Disturbance / variety regulated: unsafe commands, user permissions, provider settings and local file scope are handled as tool safety/consent rather than conflicting mission and identity requirements.
- Decisive decision or feedback right: user may allow/deny a tool request, settings configure service behavior; no legitimate first-party ultimate policy decision balancing whole-present and future system identities.
- Decision owner: external human operator for consent, deterministic permission service for enforcement, not a native S5 identity authority.
- Supporting / enforcement mechanisms: permission request/grant/deny, command validation, model/provider config, role prompts and skill restrictions.
- Closure path: request to execute a tool → allow/deny → current coding continues/stops; no identity-policy resolution → binding return to S3/S4 management functions.
- Why this is / is not agent-owned: ordinary safety and consent are important but insufficient to establish organizational S5.
- Evidence: [src/venux_code/permission/service.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/permission/service.py); [src/venux_code/config/settings.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/config/settings.py); [src/venux_code/app.py](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/src/venux_code/app.py); [README.md](https://github.com/venux/venux-code/blob/598ef18a3f3372be0178693af69748f0049058ca/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external teams and human users may apply higher policy, but this source-static assessed first-party mode does not own that authority.

### Absence scope

- Surfaces inspected: permission enforcement, installed role prompts, provider/configuration choices, user profile/memory, task/delegate scheduling and developer docs.
- Plausible first-party paths checked: supreme identity conflict identification, legitimate ultimate arbitration owner and durable binding decisions over both ongoing management and prospective adaptation.
- Why no material first-party path remains: implemented checks are per-operation consent/config rather than identity-level governance closure.

## Recursion

The evaluated native entity is one installed coding agent with optional direct deep-agent task mode or manually registered subordinate and scheduled tasks. Distinct plan/review prompts and step labels serve one operational goal. Even if several separately invoked tasks run, no shared actively controlled current-work organization and coordination were demonstrated. Neither upstream LangGraph nor user/maintainer organizations are imported as independent VSM function owners.

## Variety and escalation

Workspace observations and tool errors drive S1 next-action decisions, while iteration/context limits and user permissions constrain them. Direct DeepAgent review may retry failed plan steps using self-reported results but does not inspect a separate primary truth surface. Cron triggers and pub/sub distribute jobs/events rather than arbitrate conflicts. Skills, memory and provider routing improve local operational adaptation but are not independently owned S4; tactical permissions are not S5.

## Evidence gaps

This is source-first assessment of the pinned public revision; no provider-backed, full package `uv` dependency installation or live agent coding performance was claimed. The DeepAgent/DelegateTool implementation is available in the package, but ordinary application bootstrapping uses `VenuxAgent` with ten default tools and does not register `DelegateTool` or construct `DeepAgent`; positive higher-level rights cannot be inferred from a module's existence. Negative states are bounded to source-observed standard distribution and separately callable built-in modes; externally composed agents, external project management and future software revisions might differ.
