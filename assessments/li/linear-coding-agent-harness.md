---
harness_id: linear-coding-agent-harness
project_name: Linear Coding Agent Harness
repository: https://github.com/coleam00/Linear-Coding-Agent-Harness
review_ref: c37dc096993011cb0cc48a0afab176cd9c8f2375
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Linear Coding Agent Harness

## Review boundary

- System in focus: one long-running application-building project spanning initializer and fresh coding sessions; not all Claude Code capabilities.
- Purpose and identity: implement the supplied app specification through a persistent Linear feature backlog.
- Relevant environment: local application/Git, configured Claude SDK runtime, Linear project and Puppeteer-observed UI.
- Standard-distribution boundary: repository-owned executable SDK composition, shipped initializer/coding prompts and security/progress utilities.
- Credited operating / distribution surfaces: agent.py, client.py, prompts.py, security.py, progress.py and prompts/initializer_prompt.md / coding_prompt.md.
- Adjacent first-party surfaces excluded from ownership: example app specification is task input; repository maintenance and external SDK/Linear/Puppeteer internals are not borrowed metasystem functions.
- First-party operating / deployment modes considered: default auto-continuing serial fresh sessions, bounded --max-iterations, initial setup versus subsequent coding; claim convention can be composed across independently launched sessions.
- Recursion level: one application project with feature operations across successive sessions; no complete recursive viable unit inferred.
- Reviewed revision: `c37dc096993011cb0cc48a0afab176cd9c8f2375`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

agent.py selects initializer once, constructs a fresh ClaudeSDKClient per iteration and auto-continues coding sessions with a delay. client.py wires local coding tools, Linear MCP, Puppeteer MCP, workspace permissions and a Bash allowlist hook into that concrete composition. The initializer converts app_spec into prioritized feature issues and a META tracker plus a local project marker. Later model agents read the global project state, inspect the real app, repair regressions, select/claim features, implement/test, record evidence and update META before context turnover. Linear comments/statuses preserve commitments and handoffs, while progress.py only displays a cached local summary. The executable first-party composition supplies the operational organization even though model inference/tool execution are delegated to SDK and external MCP services.

## Operational model

The initializer and coding-session agents own the concrete work choices specified by their shipped roles. A coding session can reopen previously Done features after direct UI checks and prioritize repair over new features. That current project-level intervention is separated from feature implementation, ordinary self-testing and deterministic auto-continuation. Peer busy-state avoidance is an exposed coordination convention, not an atomic lock or a shipped autonomous concurrent scheduler.

## S1 — Operations

- State: A
- Function: deliver working application features from a supplied specification.
- Disturbance / variety regulated: unknown code, failed behavior, tool errors and incomplete features.
- Decisive decision or feedback right: choose implementation actions, tests, fixes and verified feature completion.
- Decision owner: initializer/coding model agents in the concrete shipped SDK composition.
- Supporting / enforcement mechanisms: Claude SDK tool loop, local coding tools, Linear MCP, Puppeteer, Bash allowlist and session driver.
- Closure path: agent observes file/tool/browser results, fixes the implementation, commits work and records issue completion with evidence for the next session.
- Boundary reachability: run_autonomous_agent loads the shipped prompts and create_client tool configuration directly; custom agent organization is unnecessary.
- Why this is / is not agent-owned: runtime continuation cannot implement a feature without agent choices; supplied requirements constrain outcomes rather than every action.
- Evidence: [agent.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/agent.py), [client.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/client.py), [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md), [prompts/initializer_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/initializer_prompt.md).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

## S2 — Coordination

- State: C
- Function: avoid duplicate/conflicting feature ownership among project-working sessions.
- Disturbance / variety regulated: two coding agents acting on the same feature and interrupted-session work being mistaken for free work.
- Decisive decision or feedback right: interpret In Progress ownership, avoid another actor's claimed work and publish a claim before implementation.
- Decision owner: an autonomous coordinating/peer arrangement still needs composition when multiple instances operate; the shipped serial instance and status convention alone do not close authoritative concurrent ownership.
- Supporting / enforcement mechanisms: Linear issue statuses, comments and per-session checks; no atomic compare-and-swap claim is asserted.
- Closure path: claim/status and handoff become visible to later peer reads, changing issue eligibility; trustworthy attribution and concurrent conflict resolution remain composition obligations.
- Boundary reachability: coding prompt Steps 2, 5, 6 and workflow prohibitions explicitly expose the collision-specific convention through configured Linear tools.
- Why this is / is not agent-owned: the function-specific feedback primitive exists, but multiple-instance authority/recovery is not fully wired; no S2=A claim.
- Distinct S1 units: separately executing project feature sessions when the documented other-agent convention is used.
- Inter-S1 disturbance: overlapping work on an already claimed issue.
- Attenuating coordination relation: publish In Progress and refrain from working another agent's In Progress issue.
- Feedback into subsequent S1 behaviour: subsequent Linear status read directs the peer toward a different eligible issue or resumed own work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited rule explicitly regulates duplicate ownership rather than merely storing or routing tasks.
- Evidence: [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md), [client.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/client.py).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Serial default does not itself demonstrate concurrent regulation. The prompt also prioritizes interrupted In Progress work; distinguishing that from another active owner's claim is left to composition.

## S3 — Inside-and-now control

- State: A
- Function: regulate current commitments and project stability across the feature portfolio.
- Disturbance / variety regulated: a previously reported completed feature regresses while new feature work competes for attention.
- Decisive decision or feedback right: reopen a completed feature, divert work to its repair before adding features and choose the next eligible priority from current project state.
- Decision owner: current coding-session agent under the shipped project-wide role.
- Supporting / enforcement mechanisms: Linear portfolio/status/META reads and writes, browser access and local tools; iteration cap merely bounds execution.
- Closure path: directly observed regression causes Done→In Progress and repair; updated state/notes constrain subsequent feature selection and later sessions.
- Boundary reachability: coding_prompt Steps 2 and 4 run before Step 5; the concrete client supplies list/update/comment and raw app access in every normal continuation.
- Why this is / is not agent-owned: the agent judges operational evidence and intervenes on project commitments; deterministic delay/cap does not make that judgment.
- Whole-system current view: all project Done/Todo/In Progress counts, META progress, app specification, Git and sampled implemented behavior.
- Current-control decision scope: project feature priorities, recovery of broken commitments and authority to suspend new feature development for repair.
- Evidence: [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md), [client.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/client.py), [agent.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/agent.py).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

## S3* — Complementary audit

- State: A
- Function: challenge predecessor session completion claims through complementary direct application inspection.
- Disturbance / variety regulated: Linear Done/comments can remain positive while actual app behavior has regressed or was misreported.
- Decisive decision or feedback right: choose 1–2 previously Done core features, judge their current UI reality and invalidate a prior completion when contradicted.
- Decision owner: fresh continuation coding agent, independent of the predecessor context being checked.
- Supporting / enforcement mechanisms: fresh SDK client, Linear claims, Puppeteer navigation/screenshots and issue update tools.
- Closure path: a failed sampled check reopens the issue, records what broke and forces repair before new work; findings also enter META for later control.
- Boundary reachability: the installed coding prompt mandates predecessor-feature checks before new implementation and client.py provides those browser/Linear tools.
- Why this is / is not agent-owned: the fresh agent makes the sampled audit judgment; tool output and status machinery only provide access and persistence.
- Claim being audited: previous-session Done status and implementation/verification comments.
- Ordinary reporting path: Linear issue statuses, implementation comments and META session summaries.
- Complementary access path: direct browser operation and screenshots of selected already-completed core app features.
- Independence boundary: fresh client/context checks predecessor claims without the predecessor's private conversation; same model family and serial role do not prove stronger institutional independence.
- Who acts on findings: the current agent reopens/repairs and future sessions consume the changed portfolio.
- Evidence: [agent.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/agent.py), [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md), [client.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/client.py).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Credited only for the pre-work sample of predecessor Done claims. The same agent's Step 8 QA of its own new feature is ordinary production testing and is not additional S3*. Static mandated path, not an observed audit run.

## S4 — Outside-and-then intelligence

- State: —
- Function: outside-and-then capability adaptation is not established.
- Disturbance / variety regulated: only current application feature/defect requirements are regulated.
- Decisive decision or feedback right: initializer planning and session pacing allocate existing application work, not prospective harness adaptation.
- Decision owner: no function-specific first-party adaptation owner established.
- Supporting / enforcement mechanisms: app specification, META memory, feature priorities and browser feedback.
- Closure path: no external/future distinctions→adaptation options→present harness capability return found.
- Why this is / is not agent-owned: project planning and bug recovery do not themselves close S4.
- Evidence: [prompts/initializer_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/initializer_prompt.md), [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md), [agent.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/agent.py).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

### Absence scope

- Surfaces inspected: initializer/coding prompts, driver/client/progress and README modes.
- Plausible first-party paths checked: app-spec decomposition, new project creation, META handoffs, regression checks, session pacing and model selection.
- Why no material first-party path remains: these support the current app-building mission; no supplied externally prospective harness-capability adaptation loop or parent-return mode remains.

## S5 — Policy and identity

- State: —
- Function: identity/ultimate-policy closure is not established.
- Disturbance / variety regulated: operational task safety and supplied application scope, without a policy-dispute loop.
- Decisive decision or feedback right: static role, app spec and command permissions constrain execution; no ultimate-policy adjudication path is shipped.
- Decision owner: user/developer sets initial requirements and configuration; no runtime S5 owner established.
- Supporting / enforcement mechanisms: SDK permissions, sandbox configuration, allowlist hook and fixed prompt rules.
- Closure path: no identity issue→legitimate authority→returned authoritative policy path found.
- Why this is / is not agent-owned: initial requirements and tool authorization are not runtime identity governance.
- Evidence: [client.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/client.py), [security.py](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/security.py), [prompts/coding_prompt.md](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/prompts/coding_prompt.md).
- Basis: structural.
- Confidence: medium-high, bounded source inspection.
- Caveats: Static supported-path assessment; no live model/provider execution or effectiveness claim.

### Absence scope

- Surfaces inspected: client permissions/security hook, driver, app-spec and session prompts.
- Plausible first-party paths checked: operator stop/iteration cap, security blocking, fixed identity, immutable issue descriptions and user-edited task inputs.
- Why no material first-party path remains: all are initial constraints or ordinary operation; no supported identity-level escalation/return mode is supplied.

## Distributed OSS parent arrangement

No organization-level parent function is inferred from public maintainers or local operator ownership. The supported client is a project cell, not the OSS organization's governance.

## Self-hosted and non-human modes

Users supply local runtime and service credentials. Iteration caps and termination do not create a function-specific parent mode.

## Recursion

Initializer and continuation sessions are phases/instances of the project operation; feature decomposition does not demonstrate viable-system recursion.

## Variety and escalation

Tool/security failures are observed; a fresh client retries after session errors. META/comments preserve work across context resets. Browser evidence can reopen current commitments. Status visibility alone is neither algedonic authority nor a new function.

## Evidence gaps

No live Claude, Linear or browser app-building execution was run. Static composition and shipped instructions are the evidence; actual SDK/MCP compatibility, simultaneous claim races and task quality are not measured. Native syntax checks are reported separately.
