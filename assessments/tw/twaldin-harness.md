---
harness_id: twaldin-harness
project_name: twaldin/harness
repository: https://github.com/twaldin/harness
review_ref: f75dee4fd8f64d9357fb2862741f87ddb313250d
reviewed_at: 2026-10-29
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

# twaldin/harness

## Review boundary

- System in focus: one caller-configured `harness` coding-agent invocation or retained supported session, including its first-party adapter/transport lifecycle and a selected external installed AI coding agent; not a portfolio of arbitrarily concurrent callers.
- Purpose and identity: provide a uniform, bounded interface for running an autonomous coding agent through explicit CLI, RPC, or supported SDK integrations and returning its observable results.
- Relevant environment: caller-selected coding task, project working directory, installed agent executable or owned backend server, model provider, tool outputs, permission prompts, cancellation and process failures.
- Standard-distribution boundary: shipped Python/TypeScript adapters, `RunSpec`/`RunResult`, owned subprocess lifecycle, instruction projection, and explicitly supported `SessionSpec` backends. Native model/tool decision logic is in the selected external agent, not in this library.
- Credited operating / distribution surfaces: `src/harness/registry.py`, `base.py`, `_subproc.py`, `sessions.py`, installed adapters and supported session bridges used with a separately installed/authenticated agent.
- Adjacent first-party surfaces excluded from ownership: adapter fixture/matrix and test harnesses, example agents and smoke scripts, release/CI workflows, `WANTED-ADAPTERS.md`, and terminal-pane/log readers. The third-party coding-agent internal organization and external caller's portfolio management are not credited to this repository.
- First-party operating / deployment modes considered: one-shot CLI `run` and `run_async`, explicitly selected Pi RPC/SDK and other supported retained sessions, caller-owned OpenCode/OpenHands servers, optional instruction projection and permission-policy settings. Unsupported backend combinations fail explicitly rather than being inferred.
- Recursion level: one supported agent run/session as S1; external host applications may coordinate multiple sessions at a higher recursion but are not packaged by this library.
- Reviewed revision: `twaldin/harness@f75dee4fd8f64d9357fb2862741f87ddb313250d` (clean first-party checkout).
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`RunSpec` carries task, model, workdir and permission choices into a registered CLI adapter. Its `build_command` plans argv/env and `Adapter.run` prepares temporary instructions, starts an owned subprocess group, collects output, enforces cancellation/timeouts and parses the result; asynchronous operation preserves teardown. `open_session` similarly selects explicitly supported retained RPC/SDK/HTTP sessions, checks identity/resume headers and returns a live session whose events and follow-up turn belong to the selected external agent. The library has no default autonomous selection of tasks, agent/provider, cross-session priorities or policy. [Registry](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/registry.py#L65-L105), [run lifecycle](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L860-L930), [session opening](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/sessions.py#L3002-L3060), [documented contracts](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/SPEC.md#L1-L100).

## Operational model

The caller supplies a prompt and chooses the separately installed agent, model, credentials, workdir and permissions. The native AI coding agent makes task-specific choices while Harness conveys arguments, streams observations/results, preserves session continuity where supported and owns process cleanup. Its generic adapter registry is not itself an S2, S3 or S5 authority. The positive S1 claim is contingent on executing a supported real agent integration; pure `build_command` without an agent process is only a constructor/helper surface.

## S1 — Operations

- State: A
- Function: perform a caller's coding-agent task through a supported installed autonomous CLI/RPC/SDK agent and return output or a retained turn result.
- Disturbance / variety regulated: changing task instructions, project files, tool feedback and agent process/session outcomes.
- Decisive decision or feedback right: the invoked native agent selects task-specific reasoning and tool actions, while the caller selects which agent and capability/permission envelope to activate.
- Decision owner: selected external AI coding agent inside the supported assembled run; not `harness` adapter dispatch, parser or subprocess code.
- Supporting / enforcement mechanisms: typed spec validation, argv construction, instruction projection, owned process groups, bounded output, cancellation/timeouts, identity checks, and session event transport.
- Closure path: caller prompt/workdir → launched or connected coding-agent runtime → agent's own tool/result cycle → run output or live session result returned to caller; a retained session can accept follow-up turns.
- Boundary reachability: the shipped `run` and `open_session` pathways actually launch/connect to supported agent backends; this does not rely on example-only actors, and the required separately installed agent is an explicit supported runtime dependency.
- Why this is / is not agent-owned: task-specific actions cannot be selected by the remaining adapter/parser if the native agent's model discretion is removed; the library only mediates launch and transport.
- Evidence: [registry run](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/registry.py#L75-L103), [adapter execution](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L860-L930), [session entry](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/sessions.py#L3002-L3058), [supported modes](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/README.md#L1-L55).
- Basis: structural.
- Confidence: medium-high for an assembled supported agent mode, not task success.
- Caveats: `harness` neither bundles nor controls the third-party agent's internal decision logic; its one-shot command builder alone would not establish S1 autonomy.

## S2 — Coordination

- State: —
- Function: no supported first-party inter-S1 interference-attenuation loop is evidenced at one run/session recursion.
- Disturbance / variety regulated: workdir projection leases, process teardown and concurrent caller resource use are host safety concerns, not evidenced oscillation of multiple autonomous S1 units.
- Decisive decision or feedback right: external caller coordinates separate agent sessions, if any; Harness only owns per-session resource safety.
- Decision owner: caller for cross-session orchestration; deterministic library for individual lease/cleanup enforcement.
- Supporting / enforcement mechanisms: workdir leases, process groups, session start/close and identity checks.
- Closure path: lease and lifecycle rules prevent local ownership conflicts but no S2-specific decision from one operating unit changes the other independent S1 unit's subsequent work.
- Why this is / is not agent-owned: many available adapter types and sessions are choices of backend, not a first-party organization of mutually adjusting S1 agents.
- Evidence: [session lifecycle](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/sessions.py#L3002-L3058), [subprocess lifecycle](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/_subproc.py#L287-L369), [shared contract](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/SPEC.md#L1-L100).
- Basis: structural.
- Confidence: medium-high for documented supported distribution.
- Caveats: an application built on the library may implement coordination, but its S1 units, collision response and owner must be assessed separately.

### Absence scope

- Surfaces inspected: Python registry/base/session and subprocess implementation, SPEC, README, and adapter/session matrix.
- Plausible first-party paths checked: workdir leases, multiple CLI adapters, retained RPC/SDK sessions, cancellation and caller-owned servers.
- Why no material first-party path remains: no packaged pair of mutually regulating S1 units with a specific inter-unit collision, an attenuation decision and returned inter-unit feedback is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current portfolio regulation with discretionary resource/commitment decisions is shipped for this boundary.
- Disturbance / variety regulated: one run's timeout, output budget, cancellation, and permission settings.
- Decisive decision or feedback right: caller chooses permissions, model, agent and runtime limits; deterministic code applies them.
- Decision owner: external caller for policy and run configuration, native agent for task actions, not an in-boundary S3 manager.
- Supporting / enforcement mechanisms: `RunSpec`, backend validation, process termination, session open/close and output limits.
- Closure path: runtime stops/returns a failed or completed run; no governing whole-system reprioritization or resource bargain is decided and returned to independent S1 operations.
- Why this is / is not agent-owned: stopping a process or enforcing a preselected timeout is not agent ownership of a common current-control choice.
- Evidence: [RunSpec/caller settings](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L197-L275), [run and cleanup](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L860-L930), [process controls](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/_subproc.py#L287-L369).
- Basis: structural.
- Confidence: medium-high.
- Caveats: caller-controlled session management at a higher recursion is outside scope.

### Absence scope

- Surfaces inspected: RunSpec, process lifecycle, session management, configuration and API documentation.
- Plausible first-party paths checked: timeout/cancellation, permission policy, model/backend choice and retained session handles.
- Why no material first-party path remains: these are local enforcement and caller inputs, not a first-party authority with an integrated view and discretionary resource/current-commitment control over the whole.

## S3* — Complementary audit

- State: —
- Function: no distinct complementary operational truth-checking actor returns independently judged findings into current control.
- Disturbance / variety regulated: adapter output parsing, session identity verification and error reporting ensure transport correctness, not independent audit of agent claims.
- Decisive decision or feedback right: native agent reports its result; caller may commission an external reviewer but Harness has no dedicated autonomous audit decision.
- Decision owner: none for complementary audit in shipped run; deterministic validators own only contract checking.
- Supporting / enforcement mechanisms: output parsers, session telemetry, strict resume identity, tests and error types.
- Closure path: parse/identity errors close or reject local transport; no alternative evidence channel feeds an independent corrective judgment back into work.
- Why this is / is not agent-owned: adapter parsing and tests of Harness itself cannot substitute for a separate independently judging auditor of task execution.
- Evidence: [result parsing](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/registry.py#L88-L103), [session identity](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/sessions.py#L3002-L3060), [supported integrations](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/README.md#L1-L55).
- Basis: structural.
- Confidence: medium-high for standard integration.
- Caveats: external test agents or independent reviewers can be composed outside the library.

### Absence scope

- Surfaces inspected: event parsing, session identity, integration backends, tests and documented entrypoints.
- Plausible first-party paths checked: output/usage parser, native events, session error handling, fixture tests and caller-invoked evaluator.
- Why no material first-party path remains: there is no shipped complementary access path plus independent audit owner and corrective return into ongoing agent work.

## S4 — Outside-and-then intelligence

- State: —
- Function: no system-level future/environment adaptation loop feeds developed options back into current operating capability.
- Disturbance / variety regulated: new agents and SDK integrations enter through maintainer development, while task changes enter the native agent's S1 loop.
- Decisive decision or feedback right: developer/caller chooses installed adapters and integration capabilities; no in-boundary prospective adaptation authority is exposed.
- Decision owner: external developers or caller rather than a first-party S4 actor.
- Supporting / enforcement mechanisms: adapter capability tables, explicit backend options, runtime process telemetry and proposed adapter wishlist.
- Closure path: upgraded library code can alter future runs through a software release, but no first-party autonomous prospective sensing → options → current-system regulatory return loop is present.
- Why this is / is not agent-owned: configuration and extension maintenance is outside the one-session harness operating boundary; task planning inside the native agent is S1, not S4.
- Evidence: [adapter registry](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/registry.py#L14-L80), [deferred integration list](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/WANTED-ADAPTERS.md), [supported modes](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/README.md#L1-L55).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a future system built with Harness may create S4 externally.

### Absence scope

- Surfaces inspected: registry/capability declarations, README/SPEC, deferred-adapter roadmap and session methods.
- Plausible first-party paths checked: dynamic backend choice, supported new SDKs, capability introspection, user instructions and retained sessions.
- Why no material first-party path remains: none implements prospective environment sensing and option development whose decision is returned to revise current whole-system capability in the supported distribution.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-identity policy issue/decision/return loop is established for one caller-configured run.
- Disturbance / variety regulated: sandbox/permission choices and API credentials are run-level constraints, not charter disputes.
- Decisive decision or feedback right: caller chooses permission policy and model/tool backend; native backend may prompt for tool approval; deterministic Harness validates allowed combinations.
- Decision owner: caller and upstream native CLI for their respective configuration and approval decisions, neither shown as a shipped S5 ultimate-policy authority at this recursion.
- Supporting / enforcement mechanisms: permission bypass mapping, backend validation and instruction projection.
- Closure path: static run options affect subprocess flags or reject invalid combinations; no identity-policy matter reaches legitimate ultimate authority and returns as governing system policy.
- Why this is / is not agent-owned: approving a tool call or selecting `permission_policy` does not decide organizational identity/ultimate purpose.
- Evidence: [RunSpec permission policy](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L197-L275), [validation and rejection](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/src/harness/base.py#L580-L710), [README policy boundary](https://github.com/twaldin/harness/blob/f75dee4fd8f64d9357fb2862741f87ddb313250d/README.md#L50-L100).
- Basis: structural.
- Confidence: medium-high.
- Caveats: developer governance and host policy are adjacent, not automatically the operating system's S5.

### Absence scope

- Surfaces inspected: permission specification, adapter validation, instruction preparation, README/SPEC and session operator API.
- Plausible first-party paths checked: caller permission settings, native agent approvals, runtime identity checks and contributor roadmap.
- Why no material first-party path remains: these routes configure or secure a particular run; no first-party identity/ultimate-policy dispute, legitimate parent disposition and returned ongoing governance loop is implemented.

## Distributed OSS parent arrangement

The publicly contributed library has maintainers, but their release and adapter decisions belong to the adjacent project-development organization. They are not a first-party returned S3/S4/S5 parent control mode of a user's run/session.

## Self-hosted and non-human modes

The caller can self-host supported CLI/SDK backends and use explicit operator control. Neither arbitrary user composition nor remote provider ownership is silently promoted to a positive parent mode for Harness.

## Recursion

One supported agent run/session is the operating cell. A host application may create several such cells, but the generic library does not install a viable recursive multi-cell metasystem.

## Variety and escalation

Adapter selection narrows provider variety; typed validation and identity checks bound unsupported options; timeouts, cancellation, output limits and cleanup attenuate process disturbances. Errors return to the caller, which may reconfigure or retry. These channels are local lifecycle feedback, not autonomous organizational escalation/algedonic/S3-S5 functions merely by naming.

## Evidence gaps

- No live provider/agent run was performed; the S1 finding is structural from shipped explicit adapter/session wiring and user-documented modes, not a task-quality assertion.
- A selected third-party coding-agent binary and credentials are required; its internal decisions are not directly attributable to the first-party Harness library.
- Optional developer-created multi-session control, independent review or adaptation could alter a higher-recursion assessment; it is not credited here.
