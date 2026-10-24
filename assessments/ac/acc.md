---
harness_id: acc
project_name: acc
repository: https://github.com/Xuxyyy/terminal-coding-agent
review_ref: 47dba4bd00f4eef7450961d4623861bbb335e96d
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# acc

## Review boundary

- System in focus: the first-party acc terminal coding-agent runtime at frozen revision 47dba4bd00f4eef7450961d4623861bbb335e96d, including its core model/tool loop, built-in coding tools, generic subagent tool/agent definitions, permission registry and model judge, MCP integration, persistent/rewindable sessions, context compaction and TUI/headless hosts.
- Purpose and identity: complete repository coding work through a model-backed terminal agent, optionally delegating bounded work to separately configured subagents and routing every tool call through one permission gate.
- Relevant environment: user goals and confirmation decisions, repository/workspace files, tool/process results, provider responses, subagent results, permission rules/judge output, session/rewind state, MCP tools and context pressure.
- Standard-distribution boundary: shipped acc package and repository-owned runtime/configuration surfaces. External model providers, MCP servers, user-authored global agent definition files, host shell/git environment and project repository are dependencies/configuration and cannot donate higher VSM functions.
- Credited operating / distribution surfaces: src/core loop/client/session, built-in tools and agent tool, permission modules, MCP adapter, context compaction, rewind/session store and supported TUI/headless hosts.
- Adjacent first-party surfaces excluded from ownership: CI/release/evaluation suites, docs-site build, repository maintainer workflows, .agents/.codex dogfood/e2e definitions and historical evaluation artifacts.
- First-party operating / deployment modes considered: ordinary interactive/headless coding; auto/ask permission modes; configured generic subagent execution; MCP tools; persisted/resumed/rewound sessions.
- Recursion level: one acc coding session. The main model-backed agent is the primary S1; an instantiated generic agent-tool child may own a bounded delegated S1 outcome, but the frozen distribution does not wire those children into a higher-function organization.
- Reviewed revision: 47dba4bd00f4eef7450961d4623861bbb335e96d.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

acc separates src/core from the Ink UI through a Host interface. runAgent repeatedly requests a model response, runs requested tools through one permission registry, appends tool results and continues until completion. Sessions persist the model-visible transcript plus view and file-history records; resume and rewind can reconstruct conversation state and restore captured pre-write file bytes.

The built-in agent tool can invoke a separately configured agent definition with its own prompt/model/tool subset/permission mode. Agent definitions explicitly cannot recursively include the agent tool. This is a generic delegation primitive: it returns bounded subagent work to the parent but does not supply a standard peer-collision controller or a whole-current supervisor over a persistent worker portfolio.

In auto permission mode a separate model judge can classify an otherwise questionable tool request as allow or ask. That judge receives the conversation/rules/request/denials for permission-risk adjudication. It does not independently audit the coding agent's claim that an implementation is correct, so it is not S3*.

## Operational model

The main model owns substantive coding decisions. A delegated child model may own the local decisions inside its bounded prompt. Runtime code owns deterministic execution, persistence, context pressure, rewind bookkeeping and permission enforcement. The permission judge owns only a narrow safety/permission classification right for tool execution; that does not become S3, S3* or S5 without the corresponding organizational function.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project through model-selected coding/tool actions, optionally using a bounded delegated subagent.
- Disturbance / variety regulated: unfamiliar code, implementation choices, tool/process/test failures, provider/context limits, permission refusals and focused delegated investigation/implementation.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret results, decide delegation and repairs, and decide when the assigned coding objective is complete.
- Decision owner: the active model-backed acc agent; an instantiated agent-tool child owns its bounded operational choices.
- Supporting / enforcement mechanisms: core loop, built-in tools, Host, permission gate/judge, MCP tools, compaction, session store/rewind and retries.
- Closure path: user objective → model chooses coding/tool or child-agent action → first-party runtime executes → result returns to the model → model revises or completes.
- Boundary reachability: normal interactive/headless operation directly instantiates runAgent and the tool registry; when configured agent definitions exist, the built-in agent tool is available as a first-party execution path.
- Why this is / is not agent-owned: deterministic runtime and permission machinery constrain execution, but the model decides the open-ended engineering actions and interprets their outcomes.
- Evidence: [README.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/README.md); [src/core/loop.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/loop.ts); [src/core/tools/subagent.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/tools/subagent.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: agent definitions are user-configurable; the positive S1 claim does not borrow any particular external agent definition as a higher VSM owner.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop is established.
- Disturbance / variety regulated: generic delegated child work can exist, but the standard distribution does not identify/attenuate a concrete peer operational interference mode among distinct active S1s.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: tool sequencing, permission gating, non-recursive agent definitions and child result return support delegation but do not coordinate peer interference.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: selecting a subagent and receiving its result is delegation/routing, not an S2 feedback relation.
- Evidence: [src/core/agents.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/agents.ts); [src/core/tools/subagent.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/tools/subagent.ts); [docs/agent-loop.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/docs/agent-loop.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: users can compose multiple specialized agents, but generic composition does not establish a shipped S2 loop.

### Absence scope

- Surfaces inspected: agent definitions, agent tool, core tool-call sequencing, permissions, sessions, MCP and repository tree for worker/worktree/coordination surfaces.
- Plausible first-party paths checked: concurrent worker management, worktree/file leases, conflict detection, peer scheduling and returned coordination feedback.
- Why no material first-party path remains: no function-specific interference/attenuation/feedback path is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established.
- Disturbance / variety regulated: no persistent portfolio of current S1 commitments/resources is placed under a supervisor with a whole-system view and substantive intervention right.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: 20-step continuation checkpoints, user interrupt, tool permissions, child invocation and session UI expose local controls only.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the main agent may choose one delegated tool call, but delegation alone does not create whole-current control; deterministic limits and stops do not own S3.
- Evidence: [docs/agent-loop.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/docs/agent-loop.md); [src/core/loop.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/loop.ts); [src/core/tools/subagent.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/tools/subagent.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user confirmations and Esc are local intervention/enforcement, not an S3 parent loop.

### Absence scope

- Surfaces inspected: main loop, agent tool, Host confirmation/interrupt, permission system, sessions/rewind and TUI/headless surfaces.
- Plausible first-party paths checked: current worker dashboard, resource/priority allocation, selective live child interruption/restart and supervisor return path.
- Why no material first-party path remains: no whole-current control surface over an ongoing multi-S1 organization is wired into the frozen runtime.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit of operational correctness is established.
- Disturbance / variety regulated: the permission judge regulates action risk/authorization, not whether an implementation/result claim is correct.
- Decisive decision or feedback right: none established for complementary correctness audit.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission judge, user confirmations, ordinary tests/tool output and configurable child agents can challenge actions but do not form a standard independent correctness-audit loop.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: a separate model is used in auto permission judging, but its claim is "allow or ask for this tool request", not an independent judgment over the author's operational result.
- Evidence: [src/core/permission/judge.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/permission/judge.ts); [src/core/permission/decide.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/permission/decide.ts); [docs/permissions.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/docs/permissions.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user may create a reviewer agent definition, but no particular independent review topology ships as the standard coding organization.

### Absence scope

- Surfaces inspected: permission judge, tool registry, agent definitions/tool, tests/evaluation references, session/rewind and prompts.
- Plausible first-party paths checked: mandatory fresh reviewer, direct complementary repository access, independent verdict over implementation correctness and corrective feedback gate.
- Why no material first-party path remains: the separate judge is permission-specific and generic user-composed agents do not establish a standard S3* constructor.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no future/external distinctions are developed into adaptation options that alter current capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: session persistence, rewind, compaction, model/MCP settings and user-defined agent definitions preserve or externally configure capability.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: replay/rewind and configurable tools/models change context or configuration, not via an autonomous outside-and-then adaptation owner.
- Evidence: [docs/sessions.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/docs/sessions.md); [src/core/compact.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/compact.ts); [src/core/settings.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/settings.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: durable history and file rewind can improve later operation but persistence/recovery alone is insufficient S4.

### Absence scope

- Surfaces inspected: sessions, rewind, compaction, settings/models, MCP, agent definitions and retries.
- Plausible first-party paths checked: environment scanning, learned policy/strategy update, autonomous capability reconfiguration and prospective option return into current control.
- Why no material first-party path remains: inspected paths are recovery/context/configuration mechanisms rather than S4.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy matter is routed through an authoritative owner and returned as governing operation.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes/rules/judge, configured prompts/models/tools and MCP policy constrain individual actions.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the permission judge interprets developer/user-authored safety policy for a tool request; it cannot redefine acc's identity or ultimate operating policy.
- Evidence: [docs/permissions.md](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/docs/permissions.md); [src/core/permission/judge.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/permission/judge.ts); [src/core/permission/rules.ts](https://github.com/Xuxyyy/terminal-coding-agent/blob/47dba4bd00f4eef7450961d4623861bbb335e96d/src/core/permission/rules.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: sophisticated permission classification is still action-level enforcement rather than S5 governance.

### Absence scope

- Surfaces inspected: permission classifier/judge/rules/modes, prompts/settings, agent definitions, MCP and user confirmation.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity authority and authoritative policy-change return loop.
- Why no material first-party path remains: identified policy machinery governs tool permissions, not identity/ultimate policy.

## Distributed OSS parent arrangement

The assessed organization is a running acc session, not the GitHub maintainer project. Public contributors/evaluation infrastructure are not imported as runtime parent owners.

## Self-hosted and non-human modes

acc is self-hosted with multiple providers and can run configured subagents. No qualifying parent S3/S4/S5 mode is established by generic confirmation, interruption, configuration or rewind.

## Recursion

The main coding agent and any instantiated generic child can own S1 outcomes. The frozen runtime does not organize those children into a persistent higher recursion with established S2/S3; permission judge and session services are supporting mechanisms.

## Variety and escalation

S1 absorbs coding variety and can delegate focused work. Permission classification constrains risky tools; compaction and rewind regulate context/recovery. None of those paths establishes S2/S3/S3*/S4/S5 at the declared boundary.

## Evidence gaps

No ? state is required. The frozen source and design docs expose the agent loop, generic child constructor, permission judge, session/rewind and integration boundaries sufficiently for these bounded conclusions.
