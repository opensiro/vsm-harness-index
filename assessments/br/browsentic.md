---
harness_id: browsentic
project_name: Browsentic
repository: https://github.com/imshaikot/browsentic
review_ref: 9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Browsentic

## Review boundary

- System in focus: The installed browser extension and local Browsentic Bridge, including the shipped side-panel mode that spawns a configured model-backed CLI and manages its action loop.
- Purpose and identity: Execute browser tasks against the user's real authenticated tabs while preserving a locally owner-governed action-policy boundary and reusable site knowledge.
- Relevant environment: Chromium/Firefox browser, extension/background process, loopback Bridge, locally installed external coding/agent CLI and optionally other MCP clients.
- Standard-distribution boundary: Side-panel agent runner and native CLI adapters, extension page tools, tab session registry, local Bridge guardrails, scheduled tasks and site-map generation/activation path.
- Credited operating / distribution surfaces: Packaged side-panel run, Bridge and extension, native guarded tool path, session/schedule controls, staged site maps and owner policy settings.
- Adjacent first-party surfaces excluded from ownership: External MCP-only client sessions (which supply their own agents), external model/CLI internals, desktop installer CI, test fixtures and upstream maintainer governance.
- First-party operating / deployment modes considered: Standard interactive local side-panel agent, concurrent tab sessions, operator-supervised scheduled runs, site-map creation plus explicit Activate and configurable guardrail mode.
- Recursion level: One local browser/Bridge agent work cell with multiple independent tab-bound operational conversations; human user/operator is the legitimate parent.
- Reviewed revision: 9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632.
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Browsentic's extension owns authenticated tabs and browser-tool execution. A local loopback Bridge spawns a real user-provided model-backed CLI for side-panel instructions, routes its tool requests through the same page-tool interface that external MCP clients use, and applies guardrail decisions before dispatching them to the extension. The user sees events in a tab-bound conversation. A scheduler runs repeated instructions in background tabs; a site-mapping flow derives external domain navigation skills, stores drafts beyond the active loader and requires explicit user activation. Persistent user guardrails are re-read for new runs and non-waivable policy rules are enforced in the Bridge. [architecture](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/overview.md); [side-panel agent runs](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/agent-runs.md); [extension](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/extension.md); [schedules](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/scheduling.md); [site maps](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/site-maps.md); [guardrails](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/guardrails.md).

## Operational model

A configured agent CLI chooses task-specific browser actions from ongoing page observations; deterministic fast-path commands do not take ownership of novel multi-step work. Concurrent agent runs are isolated by tab ownership and can be stopped or rescheduled by their local owner. A separate site-mapper creates future domain-specific knowledge that enters normal task contexts only after owner acceptance. Persistent guardrail policy remains a legitimate parent authority, not a permission that the agent can rewrite. Ordinary action approval and monitoring do not imply independent S3* audit.

## S1 — Operations

- State: A
- Function: Run a browser task with model-chosen page actions and repeated feedback.
- Disturbance / variety regulated: The browser page changes, controls vary, and a user instruction may require multi-step action under real authenticated session context.
- Decisive decision or feedback right: A model-backed agent CLI chooses subsequent page observations, actions and tool calls in the browser, under current guardrail and permission constraints.
- Decision owner: The real external model-backed CLI spawned and contained by Browsentic Bridge in its first-party side-panel mode. Browser and daemon execute actions and enforce constraints.
- Supporting / enforcement mechanisms: Intent funnel, native runner adapters, limited MCP tools, browser tab action bridge, state/approval guards, returned page observations and conversation resume.
- Closure path: User instruction → Bridge invokes agent CLI → model selects browser tool → Bridge/extension executes → tool result returns to the same agent for next choice or final outcome.
- Boundary reachability: Packaged side panel invokes a first-party Bridge agent runner using installed supported CLI providers; this is a shipped standard mode rather than only external MCP clients.
- Why this is / is not agent-owned: Without the spawned agent, the Bridge still implements deterministic tools and a fast-path grammar but cannot autonomously reason through multi-step novel browser tasks.
- Evidence: [architecture](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/overview.md); [side-panel agent runs](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/agent-runs.md); [agent runner](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/src/daemon/agent/runner.ts); [overview](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/README.md).
- Basis: structural
- Confidence: high
- Caveats: The inference and CLI are externally supplied and must not be attributed to Browsentic's deterministic bridge; local fast-path commands alone do not establish S1 A.

## S2 — Coordination

- State: C
- Function: Prevent simultaneously active browser-agent sessions from interfering with each other's tab ownership.
- Disturbance / variety regulated: Multiple concurrent conversations can attempt to take control of the same browser tab while one remains active.
- Decisive decision or feedback right: Pin tabs to their current conversation and refuse a competing agent's switch with TAB_IN_USE; allow authorized user transfer only from idle sessions.
- Decision owner: First-party browser session registry and tab-ownership constraints apply deterministic rules. A general autonomous arbiter deciding cross-session priorities is not shipped.
- Supporting / enforcement mechanisms: Per-conversation tab sets, run status, session identity, tab ownership guard and error feedback.
- Closure path: Unauthorized tab switch is refused, returning TAB_IN_USE and preserving the incumbent session's active tab; subsequent agent work must stay in an owned tab or request a permissible change.
- Boundary reachability: The extension's standard session manager applies these rules for simultaneous side-panel agent runs, not only external integrations.
- Why this is / is not agent-owned: The function-specific conflict attenuation exists but is deterministic. More general arbitration would need a composed decision-making agent.
- Distinct S1 units: Separate active browser conversations with their own model-backed agent runs and tab sets.
- Inter-S1 disturbance: Concurrent agents could navigate or mutate one shared tab and corrupt each other's task context.
- Attenuating coordination relation: Exclusive tab ownership for active sessions, refusal of conflicting switch, and controlled user-initiated reassignment.
- Feedback into subsequent S1 behaviour: TAB_IN_USE is returned to the requestor and the navigation is blocked; subsequent run actions remain on permitted tabs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The session manager enforces a concrete exclusivity rule against observed cross-agent interference on one mutable browser resource.
- Evidence: [extension](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/extension.md) (tab-session ownership and TAB_IN_USE); [conversations](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/conversations.md); [architecture](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/overview.md).
- Basis: structural
- Confidence: high
- Caveats: Only tab-resource interference is covered. It does not prove autonomous negotiation of broader multi-agent browser strategy.

## S3 — Inside-and-now control

- State: P
- Function: Give the local operator present control of multiple agent conversations, active work and scheduled jobs.
- Disturbance / variety regulated: Browser tasks may run concurrently, become stale, wait on approval or need interruption while the user's present priorities change.
- Decisive decision or feedback right: Inspect currently running sessions, stop a session, take or release tab ownership, and pause/resume/modify scheduled work.
- Decision owner: The local user/operator through the side-panel session strip, task editor and scheduling controls.
- Supporting / enforcement mechanisms: Live run indicators, session ownership, schedule store/history, run cancellation and guardrails approval cards.
- Closure path: Operator stops or moves a session, changes a schedule or responds to approval; Bridge and extension apply it so later current execution/dispatch differs.
- Boundary reachability: The packaged side panel and Bridge expose the live session strip and durable scheduled-task controls within one local installation.
- Why this is / is not agent-owned: The operator owns project-wide live work decisions; deterministic timers and session states are support, not a model-based metasystem controller.
- Whole-system current view: One local browser/Bridge's concurrent active conversations, pending approval cards and task schedule/history.
- Current-control decision scope: Active tab/session work, cancellation and scheduled-job commitments.
- Evidence: [conversations](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/conversations.md); [schedules](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/scheduling.md); [architecture](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/overview.md); [extension](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/extension.md).
- Basis: structural
- Confidence: medium
- Caveats: This is a local browser installation's supervisory mode; approving one form alone is not credited as whole-system S3.

## S3* — Complementary audit

- State: —
- Function: No distinct first-party independent direct-evidence auditor of the agent's operational claims and corrective audit return is established.
- Disturbance / variety regulated: A browser agent can misinterpret page content, fail to complete a task or make erroneous changes.
- Decisive decision or feedback right: No independently owned complementary audit judgment and returned corrective action is supplied for the general browser-agent task.
- Decision owner: Not established. The user sees run timeline and may approve consequential actions, which is ordinary supervisory control rather than complementary independent audit.
- Supporting / enforcement mechanisms: Action logs, screenshots, guardrail checks, diagnostics and approval cards.
- Closure path: Tool errors return to the active agent, and an operator may intervene; a separate independent audit→finding→correction feedback path is not provided.
- Why this is / is not agent-owned: An approval gate, monitoring tool or debug trace cannot itself substitute for an independently owned corrective audit of the agent's claimed results.
- Evidence: [conversations](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/conversations.md); [approvals](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/approvals.md); [subsystems](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/subsystems.md); [side-panel agent runs](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/agent-runs.md).
- Basis: structural
- Confidence: medium
- Caveats: External clients can build independent reviewers using MCP, but they are not a standard Browsentic audit function.

### Absence scope

- Surfaces inspected: Agent-run lifecycle, approval policy, diagnostics/monitor subsystems and result presentation.
- Plausible first-party paths checked: User action approvals, screenshot inspection, page monitor, run logs, generated site-map review.
- Why no material first-party path remains: These supervise execution or approve content before activation; they do not independently audit operational claims through direct evidence and return corrective decisions to an S3 path.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt future browser-agent capability to a specific external website by authoring and approving a domain-specific site map.
- Disturbance / variety regulated: Website navigation, terminology and layout can change or be unfamiliar, causing repeated exploration overhead across future tasks.
- Decisive decision or feedback right: Investigate external site pages and propose a site-specific navigation skill; approve or discard the staged map before it becomes governing context for later agent runs.
- Decision owner: The site-mapper agent proposes future capability from website exploration; the local legitimate user makes the binding activation/adaptation decision.
- Supporting / enforcement mechanisms: One-host crawler, screenshots, public sitemap/robots evidence, staging directory invisible to skill loader, validation, explicit Activate/Discard and domain-matched skill injection.
- Closure path: Operator activates an inspected site map → storage moves it into active domain skills → later requests on that host receive its navigation knowledge, changing subsequent task operation.
- Boundary reachability: Map this site is a shipped side-panel command; staging, owner approval and later domain-matched skill injection are first-party and reachable.
- Why this is / is not agent-owned: The agent explores and drafts an adaptation option, but cannot activate its own map; the final future-capability choice belongs to the local user.
- External distinction: External site structure, routes, UI quirks, robots/sitemap and screenshot evidence.
- Future / prospective distinction: A stored site map affects subsequent instructions on that domain, not merely the current crawl.
- Adaptation option generated: New SKILL.md and structured map produced from site exploration and staged for operator acceptance.
- Path back into current capability / S3: Activated map becomes an overlay the runtime loads for future agent runs on matching host; changing the active instruction/knowledge surface.
- Evidence: [site maps](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/features/site-maps.md); [site-map store](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/src/daemon/agent/site-map-store.ts); [skill loader](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/src/daemon/agent/skills.ts); [subsystems](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/subsystems.md).
- Basis: structural
- Confidence: high
- Caveats: The supported parent-governed site-map adaptation is domain-local; this is not autonomous global long-term strategy for the Browsentic project.

## S5 — Policy and identity

- State: P
- Function: Establish the standing boundaries of acceptable browser-agent action across user tasks and external MCP clients.
- Disturbance / variety regulated: Potentially malicious pages and agent requests can seek to redirect behavior beyond the user's chosen security and privacy limits.
- Decisive decision or feedback right: The local installation owner defines persistent guardrail severity, allowed hosts and unattended policy; the product reserves locked deny rules that the user cannot override.
- Decision owner: The legitimate local user/operator in supported guardrail-settings mode, bounded by the developer's hard-coded non-waivable policy.
- Supporting / enforcement mechanisms: Declared policy and severity ordering, config/approvals stores, settings UI, Bridge decision function and per-run restrictions preventing rule loosening.
- Closure path: Operator changes standing config → Bridge re-reads/reconciles policy for runs → all future browser actions are permitted, confirmed or denied accordingly; agent run cannot widen its own policy.
- Boundary reachability: Guardrail settings are shipped in browser panel and desktop clients and enforced inside the standard Bridge invocation paths.
- Why this is / is not agent-owned: The policy source is user/developer, not the model. Model instructions cannot override the first-party daemon's binding guardrail rules.
- Identity / ultimate-policy issue: Which categories of browser interaction may occur without approval, which require owner consent, and which remain forbidden for this local AI/browser work cell.
- Ultimate authority in each claimed mode: Local owner for configurable standing rules and software developer for locked constraints; no independent agent policy authority claimed.
- Return-to-operation path: Accepted persistent owner guardrail settings and locked rules → action policy decision → browser tool outcome and subsequent agent behavior.
- Evidence: [guardrails](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/guardrails.md); [policy](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/src/daemon/guardrails/policy.ts); [settings](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/src/daemon/guardrails/settings.ts); [approvals](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/guide/approvals.md); [persistent state](https://github.com/imshaikot/browsentic/blob/9c0892a457e86cf2a5c3d1f4a8eea7eeb0900632/docs/internals/state.md).
- Basis: structural
- Confidence: medium
- Caveats: This S5 parent evidence is local user-defined standing safe-operation identity, not upstream maintainer governance or blanket inference from ordinary form approval.

## Distributed OSS parent arrangement

The local browser user owns operational permissions and site-map activation. Contributors and upstream maintainers do not share access to, or govern, the private tab context of an arbitrary installed Browsentic instance. No public organizational S5 status is inferred.

## Self-hosted and non-human modes

The local Bridge and extension can serve external MCP clients without spawning their own agent. This Path A mode is not used to justify positive S1; the packaged Path B side-panel agent CLI mode provides first-party model-directed execution. A scheduled job can run without an attending person but consequential actions retain owner guardrails and time out if approval is missing.

## Recursion

Individual tab-bound agent runs are operational units. The extension's session registry attenuates collisions on shared browser tabs, while the user supervises live work, controls standing rules and accepts website-derived future capability changes. Domain-specific site-map adaptation is one self-hosted installation's S4 parent mode, not organization-wide strategy.

## Variety and escalation

Contested tabs fail with TAB_IN_USE. Consequential browser actions pause for local user decision; disallowed pages remain blocked even under positive agent output. Site-map drafts stay outside the active skill loader until owner review/activation. Scheduled runs can be missed, delayed or cancelled with durable state, and no external agent may silently widen its own rule set.

## Evidence gaps

This is a source-first analysis at the exact review ref; no browser model/CLI was run and no independently operated auditor assessed actual outputs. Positive S1 depends on the supported shipped Bridge-spawned provider CLI mode, not external MCP-only sessions. S4 is supported as a user-authorized website-skill adaptation with subsequent domain-matched use, not an autonomous general strategy loop. S2 is bounded to active tab contention and refusal, not semantic coordination among arbitrary agent tasks.
