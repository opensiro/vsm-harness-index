---
harness_id: macos-harness
project_name: macOS Harness
repository: https://github.com/browser-use/macos-harness
review_ref: 43d9edf8286153482348b15f7d8c22d9e38f6c6b
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# macOS Harness

## Review boundary

- System in focus: the repository's macOS computer-use CLI, helper, policy and installed skill/hook package.
- Purpose and identity: expose app state and eleven deterministic UI tools to an already running coding agent.
- Relevant environment: macOS applications/accessibility APIs, local user and administrator, external Claude Code/Codex/Pi/OpenCode agent runtimes.
- Standard-distribution boundary: the packaged `src/macos_harness` Python CLI/helper and bundled skill/hook installer at the pinned revision. External coding agents are separate owners, not part of this repository-relative system.
- Credited operating / distribution surfaces: CLI request/reply, helper sessions and per-app FIFO, tool dispatch, state/screenshot/diff operations, interruption/presence, policy and approval enforcement, install and skill text.
- Adjacent first-party surfaces excluded from ownership: tests/fakes/fixtures, live-test probes, CI/release workflows and contributor instructions. Installed skill instructions are reviewed as a supported interface but do not donate the external host's model/action loop.
- First-party operating / deployment modes considered: shell calls; persistent per-user helper; installed Claude/Codex/Pi/OpenCode skill/hooks; default access and optional ask/strict policy modes.
- Recursion level: the reusable computer-tool package, not a wider organization containing external agent runtimes.
- Reviewed revision: `43d9edf8286153482348b15f7d8c22d9e38f6c6b`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/README.md) describes giving existing coding agents access to Mac apps. The [entry point](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/pyproject.toml#L26-L41) has platform UI dependencies and launches `macos_harness.cli:main`. The [CLI](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/cli.py#L33-L109) sends one supplied argument vector over a local socket and prints the reply. The [helper](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/helper.py#L353-L457) authenticates a request, resolves its calling session and executes that request through `tools.execute`. Its per-app FIFO serializes calls; the AppKit [run loop](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/runloop.py) schedules native UI work, not agent reasoning.

The [dispatcher](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py#L933-L995) parses a named tool, runs it and returns stdout/stderr. [Session gates](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py#L163-L195) enforce app policy, approval, OS permissions, lock state and user interference. App snapshots, numbered accessibility elements, diffs, screenshots, settling and clipboard restoration support reliable individual tool calls. The [installer](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/install.py) writes a skill and turn-start/end/cancellation hooks into external hosts; it does not supply their model inference or task-planning engine. [Skill instructions](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/skills/macos-harness/SKILL.md#L8-L23) tell that external actor to read, act and read again.

[Policy](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/policy.py) combines administrator/user configuration and checks targets. [Approvals](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/approvals.py#L124-L165) optionally ask a person for app access and persist the result. These bound access; they do not make the helper the owner of task strategy or identity-level judgment.

## Operational model

The first-party outcome is an executed UI command or an observation for another actor. The substantive task-local decision—what app/action to choose next and whether the user's task is complete—belongs to the external coding agent. No in-package question→model→chosen action→observation→next model decision loop is shipped.

The counterfactual owner test removes external agent runtimes while retaining helper, CLI, skill text, FIFO, policies, screenshots and hooks: the package can still execute commands supplied by a human/script, but cannot independently interpret a user's task and choose successive operational actions. This is a substantive tool substrate, without first-party agentic S1 at this boundary.

**Proposed terminal disposition: `excluded-no-agentic-vsm`.** Exclusion is an inclusion-boundary finding, not a quality judgment, not a claim that the package has no deterministic controls, and not a denial of agentic S1 in a separately assessed wider composition. No positive autonomy claims are assigned.

## S1 — Operations

- State: —
- Function: Task-directed app work is selected by the external host; the package supplies command execution and observations.
- Disturbance / variety regulated: task-specific app states, navigation and errors interpreted by the caller.
- Decisive decision or feedback right: Select the next substantive UI action, interpret observations and decide completion.
- Decision owner: External coding-agent actor or caller; no first-party autonomous S1 owner.
- Supporting / enforcement mechanisms: CLI/socket, helper session, dispatcher, accessibility tools and installed skill.
- Closure path: Caller sends action → helper executes → observation returns to caller; the next discretionary step closes outside this repository.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/cli.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/cli.py#L33-L109); [src/macos_harness/helper.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/helper.py#L403-L457); [src/macos_harness/tools.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py#L933-L995); [skills/macos-harness/SKILL.md](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/skills/macos-harness/SKILL.md#L8-L23).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: CLI/helper request path, packaged dependencies, tool table/execution, skill and host installer.
- Plausible first-party paths checked: AppKit runloop, persistent helper, read/act/read instructions and installed hooks.
- Why no material first-party path remains: The runloop services native UI events and the helper handles supplied calls; no task-interpreting first-party actor chooses the next action. Tool call loops in external hosts are not inherited.

## S2 — Coordination

- State: —
- Function: Per-app calls are serialized to avoid concurrent UI interference; human input can interrupt them.
- Disturbance / variety regulated: native UI/session/access variation handled by tool-support rules; no positive autonomous S2 function is credited.
- Decisive decision or feedback right: No agent-owned inter-S1 coordination discretion supplied by this package.
- Decision owner: Developer-defined FIFO/gating rules; distinct first-party S1 units not established.
- Supporting / enforcement mechanisms: Per-app FIFO, session tracking, person/presence gates and cancellation.
- Closure path: A queued call waits then executes or is interrupted; external callers receive the result.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/helper.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/helper.py#L214-L323); [src/macos_harness/tools.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py#L163-L195).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: Helper sessions/FIFO, app queue, user-presence and cancellation gating, host hooks.
- Plausible first-party paths checked: Multiple calling sessions, shared-app serialization and user/agent interference.
- Why no material first-party path remains: Concrete UI mutual-exclusion support exists, but the package supplies neither distinct autonomous operational units nor an S2-specific autonomous actor/constructor. Deterministic serialization is not borrowed host-agent ownership.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system discretionary current regulation is established; per-call limits and interruption enforce existing rules.
- Disturbance / variety regulated: native UI/session/access variation handled by tool-support rules; no positive autonomous S3 function is credited.
- Decisive decision or feedback right: No supplied choice over whole-system commitments, priorities or resource bargaining.
- Decision owner: Caller/operator sets setup and may stop a call; no evidenced function-specific S3 owner.
- Supporting / enforcement mechanisms: Deadlines, action/text limits, helper lifecycle, app policy and person approval.
- Closure path: Request finishes, times out or is refused; no whole-current control decision and returned organizational intervention.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/tools.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py#L32-L43); [src/macos_harness/helper.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/helper.py#L476-L504); [src/macos_harness/policy.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/policy.py); [src/macos_harness/approvals.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/approvals.py#L124-L165).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: Helper state/shutdown, CLI timeout, session/tool limits, policy and app approvals.
- Plausible first-party paths checked: Helper stop, app permission changes, FIFO resource use and turn cancellation.
- Why no material first-party path remains: Lifecycle, local access choices and deterministic tool limits do not supply a whole-organization current view plus discretionary regulation/returned control. No separate autonomous, constructor or parent supervisory mode is wired.

## S3* — Complementary audit

- State: —
- Function: State reads and screenshots provide evidence to the caller; no independent corrective audit organization is shipped.
- Disturbance / variety regulated: native UI/session/access variation handled by tool-support rules; no positive autonomous S3* function is credited.
- Decisive decision or feedback right: No independent audit judgment with corrective return to current organizational control.
- Decision owner: External task actor interprets screenshots and claims; no first-party autonomous auditor.
- Supporting / enforcement mechanisms: Accessibility snapshots, screenshots, diffs, logging and telemetry.
- Closure path: Observations return to the same requesting host; its interpretation is outside this package.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/tools.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py); [skills/macos-harness/SKILL.md](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/skills/macos-harness/SKILL.md#L54-L57); [src/macos_harness/telemetry.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/telemetry.py).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: Tool state/read/result paths, screenshot/diff evidence, proof-of-work skill text, telemetry and test boundary.
- Plausible first-party paths checked: Read-after-action verification, screenshots, error logging and native tests.
- Why no material first-party path remains: These are routine observations/support for the requesting actor; no materially independent audit judgment and corrective-control return is part of the distribution. Tests do not donate a runtime auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective capability-adaptation loop is shipped.
- Disturbance / variety regulated: native UI/session/access variation handled by tool-support rules; no positive autonomous S4 function is credited.
- Decisive decision or feedback right: No owner develops/selects future adaptation options and returns them into present organizational capability.
- Decision owner: External agent/user may use app information; no first-party S4 actor.
- Supporting / enforcement mechanisms: App snapshots, instruction resources, session state and versioned installer.
- Closure path: State changes the external caller's next task action; no shipped prospective capability-change return.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/instructions.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/instructions.py); [src/macos_harness/install.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/install.py); [src/macos_harness/tools.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/tools.py).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: App instructions, snapshot/session/diff handling, installer, README and supported host integrations.
- Plausible first-party paths checked: App sensing, packaged application guidance, installation/upgrade and reuse of prior state.
- Why no material first-party path remains: These support current UI work or manually selected software configuration, without an in-boundary environmental-model→adaptation-option→present-capability feedback loop. Hypothetical host learning is outside scope.

## S5 — Policy and identity

- State: —
- Function: Static target restrictions and optional access approvals bound a tool, without identity/ultimate-policy closure.
- Disturbance / variety regulated: native UI/session/access variation handled by tool-support rules; no positive autonomous S5 function is credited.
- Decisive decision or feedback right: No supplied runtime identity issue routed to legitimate ultimate authority with an authoritative governing return.
- Decision owner: User/administrator authors access rules; no evidenced S5 decision-return organization.
- Supporting / enforcement mechanisms: Managed/user TOML policy, security-target checks, app consent and skill safety instructions.
- Closure path: Access permission affects a command, without evidence of identity-level dispute/ultimate policy resolution.
- Why this is / is not agent-owned: the package does not supply the autonomous organizational decision owner; external agent task discretion and deterministic enforcement are separated.
- Evidence: [src/macos_harness/policy.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/policy.py); [src/macos_harness/approvals.py](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/src/macos_harness/approvals.py#L124-L165); [skills/macos-harness/SKILL.md](https://github.com/browser-use/macos-harness/blob/43d9edf8286153482348b15f7d8c22d9e38f6c6b/skills/macos-harness/SKILL.md#L92-L104).
- Basis: explicit + structural.
- Confidence: high within the declared package boundary.
- Caveats: mechanisms can support a wider composed agent system; no positive ownership is imported from it.

### Absence scope

- Surfaces inspected: Managed/user policy merging, protected targets, approval persistence, skill boundaries and installer.
- Plausible first-party paths checked: Administrator precedence, app-level allow/deny, user approval and external host instructions.
- Why no material first-party path remains: A legitimate rule author and operational access approval exist, but no identity/ultimate-policy issue and function-specific authoritative return loop is shipped. Constraints alone are not S5; no P mode follows merely from a human having final app access.

## Distributed OSS parent arrangement

Repository maintainers and Mac administrator/user authority are distinct from a demonstrated runtime parent S3/S4/S5 arrangement. Supported app approval is local tool access, not evidence of organization-level parent closure.

## Self-hosted and non-human modes

The helper runs locally and can serve headless callers. A headless or scheduled external agent remains external; self-hosting does not introduce a first-party agent decision engine. Optional ask/strict policy changes access enforcement rather than ownership.

## Recursion

AgentSession/AppSession records and process ancestry identify callers, not recursively viable first-party S1 units.

## Variety and escalation

Text trees, diffs and screenshots transduce app state. Limits, app queues, policy and interruption attenuate available actions. Error/refusal/permission messages are returned to the caller; no independent algedonic organizational response is inferred from a blocked command.

## Evidence gaps

No macOS app interaction or live model execution occurred. Native portable tests `test_protocol.py`, `test_skill.py`, `test_install.py`, `test_errors.py` passed: **208 passed, one warning** about skill/error text coverage. All 37 source Python files passed AST syntax parsing. The attempted full non-live test collection on Linux stopped with six collection errors because Quartz/ApplicationServices/macOS frameworks are unavailable; it is not reported as a passing full suite. Upstream CI explicitly uses macos-latest. This platform limitation does not obscure the inspected CLI/helper/dispatcher/installer ownership boundary. No material unresolved shipped in-package agent decision loop was identified.
