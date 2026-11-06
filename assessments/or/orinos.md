---
harness_id: orinos
project_name: Orinos
repository: https://github.com/batin-sahin/orinos
review_ref: fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Orinos

## Review boundary

- System in focus: the installed Orinos local desktop/terminal agent harness operating one selected workspace and its agent sessions, not the developer's wider project or the external model provider.
- Purpose and identity: turn operator software-work requests into model-chosen workspace, terminal, web, and skill actions with visible execution and consent for risky tools.
- Relevant environment: the operator's workspace/files/processes, remote model endpoints, web content, provider failures, tool results, and user approval or denial.
- Standard-distribution boundary: shared TypeScript `src/core` agent loop, built-in tools/providers/skills/sessions/config, first-party `src/cli` and Electron `src/main`/renderer integration.
- Credited operating / distribution surfaces: shipped interactive CLI, one-shot CLI, and desktop app paths calling the same `Agent.send`/`runTool` implementation and returning tool observations to the next model step.
- Adjacent first-party surfaces excluded from ownership: `ROADMAP.md`, proposed checkpoint/memory/subagent/MCP features, competitive research, design docs, smoke screenshots, UI/packaging build workflows, and the external model vendor's own organization.
- First-party operating / deployment modes considered: interactive CLI approval, noninteractive CLI (denies risky calls unless explicit `-y` auto approval), Electron approval dialog, operator-configured auto-approve, and user-supplied model endpoints; these are modes of the same single-agent workflow rather than a shipped multi-agent fleet.
- Recursion level: one local Orinos installation/session performing an operator request; individual tool invocations and the CLI/Electron faces are not separate S1 units.
- Reviewed revision: `fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066`.
- Observation date: 2026-11-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent.send` builds an environment/tool/skill system prompt, sends the current session messages to a selected OpenAI/Anthropic/Google-compatible provider, persists the assistant's proposed tool calls, executes each via the first-party tool registry, appends tool observations, and asks the model again within a bounded step count. CLI and Electron both construct this shared agent, select a session/workspace/provider, stream events and implement user approval. Terminal and write/edit tools are marked risky; `runTool` awaits a configured approval handler unless `autoApprove` is true. The runtime persists local JSON sessions and usage; provider credentials and preference changes are user-configured. Skills are built-in/local Markdown packs selected by the model using the `skill_view` tool. There is no shipped subagent, shared multi-run coordinator, independent evaluator or prospective capability revision loop. Evidence: [agent implementation](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [provider dispatch](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/providers/index.ts), [tool registry](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/tools/index.ts), [sessions](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/sessions.ts), [CLI](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/cli/index.ts), [Electron IPC](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/main/ipc.ts), [README](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/README.md).

## Operational model

The model has the discretionary local action choice and interprets tool feedback. The user supplies a task and workspace, chooses a provider/model, and may approve/deny particular risky actions; deterministic runtime code supplies step bounds, schemas, persistence, and approval enforcement. Neither a long list of providers nor multiple sessions implies two concurrently coordinated viable operational units. The shipped roadmap expressly classifies subagents, standing goals, checkpoints and memory as future work, so they do not donate metasystem ownership. Evidence: [agent](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [configuration](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/config.ts), [roadmap](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/ROADMAP.md).

## S1 — Operations

- State: A
- Function: pursue one local software-work request by choosing and observing workspace/tool actions.
- Disturbance / variety regulated: heterogeneous user requests, unknown file contents, failing commands, missing dependencies, provider/tool errors, approval denials and changing external web information.
- Decisive decision or feedback right: choose a next tool and arguments, revise the approach based on returned tool output, or produce a final answer.
- Decision owner: the configured model agent during a shipped CLI/Electron session; the human retains permission over risky side effects, not every individual model choice.
- Supporting / enforcement mechanisms: provider-specific stream adapters, tool schemas/dispatch, bounded `maxSteps`, session JSON, usage ledger, local skills and risk/auto-approval flags.
- Closure path: user task and transcript → model-selected tool calls → approved/allowed tool execution or denial → persisted `role: tool` observation → next provider request using updated session, repeated until a final response, abort or step limit.
- Boundary reachability: `src/cli/index.ts` and `src/main/ipc.ts` instantiate `Agent` and call its real `send` method; this is first-party distribution code rather than only a design example.
- Why this is / is not agent-owned: without `streamProvider` the helper code cannot choose an open-ended next work action, whereas removing the approval UI still leaves a model decision loop within its configured limits.
- Evidence: [agent loop and tool observation](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [tool registry](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/tools/index.ts), [CLI entry](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/cli/index.ts), [desktop IPC](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/main/ipc.ts).
- Basis: structural.
- Confidence: high for wired source path.
- Caveats: static source assessment; no live-provider/GUI native E2E, model API key, or execution of risky tools was used to demonstrate operational reliability. The noninteractive CLI denies risky actions by default; `-y` changes that boundary explicitly.

## S2 — Coordination

- State: —
- Function: no shipped regulation of concrete interference among distinct Orinos-owned S1 work cells is established.
- Disturbance / variety regulated: two separately started sessions could edit overlapping files, but the shipped product does not expose a documented inter-session contention/negotiation loop.
- Decisive decision or feedback right: no coordination-specific owner/reviser among independently acting S1 cells is identified.
- Decision owner: each model handles its own turns; the user chooses sessions/workspaces; the runtime only prevents re-entrant sends in a single `Agent` instance.
- Supporting / enforcement mechanisms: per-session `running` flag and abort controller, session JSON, IPC maps and workspace path resolution.
- Closure path: a single session is prevented from concurrent re-entry; there is no cross-session interference signal returned into separately managed S1 behaviours.
- Why this is / is not agent-owned: locking one conversation and showing many session tabs do not establish S2 at this recursion.
- Evidence: [agent `running` guard](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [session records](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/sessions.ts), [desktop IPC](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/main/ipc.ts), [future subagent design](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/ROADMAP.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: externally orchestrated multiple Orinos processes are outside the declared first-party multi-agent coordination mode.

### Absence scope

- Surfaces inspected: shared agent loop, session store, IPC session map, CLI entry, tool registry, README and roadmap.
- Plausible first-party paths checked: concurrent sessions, per-session send locks, desktop map of agents and future subagent/workspace scheduling.
- Why no material first-party path remains: no evidenced pair of first-party coordinated operational units plus interference attenuation and returned behaviour change; future subagent coordination is explicitly only planned.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control loop over multiple operational commitments/resources is established at the selected recursion.
- Disturbance / variety regulated: excessive tool steps, risky modifications and provider/model usage are bounded locally by runtime defaults and user choices; no aggregate operational resource bargaining is shipped.
- Decisive decision or feedback right: the operator selects model/workspace, approval and `maxSteps`; the runtime applies these fixed choices without a distinct S3 management decision.
- Decision owner: user/configuration for control envelope and local run interruptions; model for S1 next actions.
- Supporting / enforcement mechanisms: `maxSteps` counter, `autoApprove` gate, session usage accounting, CLI/desktop settings and abort.
- Closure path: local run enforcement or user intervention may constrain the active S1; there is no whole-system current view and authoritative aggregate allocation loop independent of S1.
- Why this is / is not agent-owned: counterfactually removing the model leaves the same deterministic limit/approval settings, not an autonomous metasystem selecting revised operating constraints.
- Evidence: [agent loop and bounds](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [config preferences](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/config.ts), [session ledger](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/sessions.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: the operator can supervise runs manually; ordinary intervention alone does not demonstrate an S3 parent-governed loop at a higher recursion.

### Absence scope

- Surfaces inspected: agent execution, configuration, CLI/IPC controls, session ledger and roadmap.
- Plausible first-party paths checked: usage/cost display, model selection, step bound, cancellation, and global settings as potential current-control resource authority.
- Why no material first-party path remains: only local operator decisions and preselected runtime enforcement are wired; no distinct whole-installation current operational view plus decision and returned regulation path is demonstrated.

## S3* — Complementary audit

- State: —
- Function: no independent complementary inspection/audit of operational claims is shipped.
- Disturbance / variety regulated: inaccurate model answers or misleading tool success claims would require an access path beyond the ordinary transcript; none is identified.
- Decisive decision or feedback right: the agent receives ordinary tool results; no separate reviewer issues an independent finding that returns to control.
- Decision owner: absent within the shipped product; the operator can inspect trace cards, but this is not a configured independent audit function.
- Supporting / enforcement mechanisms: tool event stream, usage ledger, JSON transcript, explicit approval dialog and development smoke capture.
- Closure path: ordinary logging and human-visible traces exist, but no complementary audit verdict and returned control intervention is wired.
- Why this is / is not agent-owned: the agent's own tool-observation path is not sufficiently independent of its operational reporting.
- Evidence: [agent events](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [sessions](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/sessions.ts), [README smoke capture](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/README.md).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: outside reviewers could independently inspect files or transcripts; that is not a shipped Orinos audit ownership mode.

### Absence scope

- Surfaces inspected: event emission, tool result handling, stored sessions, CLI/desktop evidence UI, scripts and documented smoke tests.
- Plausible first-party paths checked: numbered tool-event ledger, approval workflow, bundled smoke capture and build validation as potential complementary audit.
- Why no material first-party path remains: visible routine events are the production reporting path; CI/smoke are adjacent product-development checks, and no independent operational audit judgment/feedback path is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped external-prospective intelligence loop that selects adaptation options and modifies current harness capability is established.
- Disturbance / variety regulated: future model, context, dependency and workflow changes are discussed in the developer roadmap, not systematically handled by an active first-party S4 path.
- Decisive decision or feedback right: product author proposes future capabilities in docs; operational model can search the web for a user task but does not govern future harness adaptation.
- Decision owner: developer outside the assessed runtime; no internal S4 actor or first-party parent closure path identified.
- Supporting / enforcement mechanisms: web search/fetch tools, provider catalog, config endpoints and roadmap.
- Closure path: searches feed the current S1 request, and roadmap ideas await external development; no environment-model → adaptation choice → changed current capability loop is shipped.
- Why this is / is not agent-owned: general research in an S1 task and a static roadmap are not a prospective metasystem function.
- Evidence: [roadmap (proposal)](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/ROADMAP.md), [web tools](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/tools/web.ts), [model catalog](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/catalog.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: general code-writing S1 could modify a repository when asked, but this is not demonstrated as a first-party identity-preserving prospective adaptation loop for Orinos itself.

### Absence scope

- Surfaces inspected: roadmap, first-party tools, model catalog/provider dispatch, local skills and session/config persistence.
- Plausible first-party paths checked: web sensing, custom provider model changes, skill instruction packs and future memory/self-improvement work.
- Why no material first-party path remains: all shipped paths serve current user tasks or human configuration; the prospective capability-return path is a published proposal rather than installed behavior.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision and return loop at the harness recursion is established.
- Disturbance / variety regulated: risky commands, project instructions and operator preferences bound local actions; a constitutional identity dispute or competing current/future policy is not presented to an ultimate authority through a dedicated path.
- Decisive decision or feedback right: developer writes the system prompt; user approves or denies individual risky calls and edits preferences. Neither action is a demonstrated identity-policy adjudication for the harness.
- Decision owner: external developer and local user for static constraints/routine permission; no evidenced S5 function-specific autonomous or parent-owned closure.
- Supporting / enforcement mechanisms: system prompt, project instruction-file injection, `autoApprove`, approval dialog, config JSON and step limits.
- Closure path: an ordinary tool approval changes one tool result; no documented identity/policy issue reaches legitimate authority and returns a governing decision for subsequent system operation.
- Why this is / is not agent-owned: the model is instructed to honor policy but has no legitimate ultimate authority to redefine its own identity, and generic user consent is not S5 parent governance.
- Evidence: [system prompt/approval path](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/agent.ts), [configuration](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/core/config.ts), [desktop approval IPC](https://github.com/batin-sahin/orinos/blob/fc0cf654ae8e53a41a6072cf410a9e6c1a8cb066/src/main/ipc.ts).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: ultimate human policy authority exists in the real operator/developer organization outside this reviewed distribution; the standalone runtime does not expose a function-specific parent path.

### Absence scope

- Surfaces inspected: prompt assembly, risky-tool approval, provider/config/skill loading, desktop/CLI approval, README and roadmap.
- Plausible first-party paths checked: system prompt policy, custom user instructions, persistent preferences, user approval/denial and proposed standing-goal authority.
- Why no material first-party path remains: these are task-level constraints and permissions, or planned functions; no first-party identity-level issue/legitimate authority/returned-policy path is supplied.

## Recursion

One session has a distinct task environment and model-chosen action loop, but it does not demonstrate its own nested metasystem; separate sessions, UI fronts, or tool calls do not by themselves prove recursive viable subsystems. This review credits the one agentic operational path, not an entire viable multi-agent organization.

## Variety and escalation

Tool schemas and workspace selection attenuate risk/variety, while model-selected tools amplify the repertoire of S1 responses. A model may use the ordinary stream of tool observations and returned denial to adjust next steps. Errors, `maxSteps` exhaustion and user cancellation are operational exception feedback to the user, not evidenced algedonic escalation to an independent authority or other S-function.

## Evidence gaps

- Static pinned-source review only; no live provider tokens, Electron display, GUI smoke, Windows/macOS package or destructive command execution verified here.
- Endpoint/provider capability and approval UX vary by external model and operator mode; actual action quality, trustworthiness and sustained viability remain empirical questions.
- No independent audit, deployed prospective adaptation, institutional policy-return mechanism or multi-agent interference controller can be credited from roadmap-only material.
