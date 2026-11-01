---
harness_id: pi-native
project_name: pi-native
repository: https://github.com/nurmdrafi/pi-native
review_ref: b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# pi-native

## Review boundary

- System in focus: the installed pi-native extension, role and native-tool distribution running in its supported Pi host, including opt-in tmux subagents.
- Purpose and identity: complete repository engineering tasks with first-party native tools and bounded delegated work.
- Relevant environment: operator task briefs, target repositories, local filesystem/processes, model-provider quotas and failures, concurrent workers and Pi/tmux dependencies.
- Standard-distribution boundary: the documented bootstrapped installation with native binaries available and Pi host linked. Pi is an execution dependency; its unrelated functions are not credited. No claim that pi-native contains an independent replacement for Pi's model loop.
- Credited operating / distribution surfaces: scripts/bootstrap.sh, extensions/subagents, native piread/piedit/pibash extensions, installed agents and their role-specific tools, permission-gate and documented session controls.
- Adjacent first-party surfaces excluded from ownership: benchmark/, research/, repository CI/release, docs-optimizer maintenance work, dashboard tests and contributor governance; these do not donate autonomous adaptation or ultimate policy.
- First-party operating / deployment modes considered: top-level coding sessions and optional /subagents on or PI_SUBAGENTS=1 modes; declared file scopes in default queue mode and read-only reviewer/verifier roles; self-hosted operator controls.
- Recursion level: one deployed harness instance; child execution is not presumed recursively viable.
- Reviewed revision: `b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f`.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (Index active release; Skills main 0.3.8 inspected but not silently activated).

## Repository architecture

The distribution installs linked Pi dependencies and native Rust tools, registers extension tools and supplies sandboxed role prompts. The owned subagent extension creates tmux-backed Pi invocations with selected tools/skills, carries session identity, receives result messages and persists git-delta/history records. Declared write scopes are normalized to absolute paths; overlapping queued/running scopes block launches until release, while unrelated scopes continue. Status exposes all current children and usage; cancel/restart/steer/resume modify current commitments. Reviewer and verifier roles inspect raw repository reality in isolated contexts. Permission rules constrain edits/commands and annotate recovery phases. Startup self-heal synchronizes installed tool paths/version state; it is maintenance, not prospective capability selection.

## Operational model

A top-level agent and delegated worker cells own task interpretation and code/tool action choices in the installed mode. First-party role/tool/spawn/result wiring makes operational work reachable through Pi, whose host infrastructure remains external. Runtime locks and quotas enforce rules; they do not become the autonomous coordinator. A parent session can observe all children and intervene on current commitments. The optional reviewer provides a distinct challenge path to worker completion reports; no empirical execution, performance or universal audit coverage is claimed.

## S1 — Operations

- State: A
- Function: task-directed engineering transformations by deployed worker cells.
- Disturbance / variety regulated: unknown code, errors and changing task conditions.
- Decisive decision or feedback right: choose reads, edits, commands and follow-up actions to satisfy a task brief.
- Decision owner: the installed top-level/worker agent; the host supplies model execution.
- Supporting / enforcement mechanisms: native tool wrappers, sandbox loadouts, tmux lifecycle, result delivery and session history.
- Closure path: tool observations inform later agent turns; final result and git deltas return to the parent.
- Boundary reachability: bootstrap links Pi and installs the local extensions; subagent tool launches installed worker role with native tools and returns its result.
- Why this is / is not agent-owned: removing agent choice leaves process/tool execution machinery but no discretionary engineering transformation.
- Evidence: [scripts/bootstrap.sh](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/scripts/bootstrap.sh); [extensions/subagents/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/index.ts); [agents/worker.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/worker.md); [extensions/piedit/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/piedit/index.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: requires installed Pi, model access, tmux and built native binaries; no ownership borrowed from other Pi features.

## S2 — Coordination

- State: C
- Function: attenuation of write collisions and shared-provider saturation across distinct child work cells.
- Disturbance / variety regulated: two writable children target the same path/subtree; concurrent requests can generate provider 429 storms.
- Decisive decision or feedback right: expose declared write scopes and conflict feedback; autonomous conflict-specific arbitration beyond the configured queue requires composition.
- Decision owner: developer-selected queue/cap policy plus agent-supplied file scope declarations; no separate shipped autonomous arbitration policy credited.
- Supporting / enforcement mechanisms: findConflicts, queued/running scope reservations, FIFO skip-scan and bounded provider concurrency.
- Closure path: result finalization releases a scope/slot and drain launches the waiting child; acknowledgements and list output expose ownership to the parent.
- Boundary reachability: the installed subagent tool consumes files/cwd, checks reservations and parks conflicting spawns in the default queue mode.
- Why this is / is not agent-owned: S2-specific collision paths exist, but deterministic waiting alone does not establish agent ownership of the regulatory decision.
- Evidence: [extensions/subagents/scope.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/scope.ts); [extensions/subagents/spawn-queue.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/spawn-queue.ts); [extensions/subagents/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/index.ts); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md).
- Basis: structural.
- Confidence: medium.
- Caveats: undeclared write scopes are not locked; worktree-isolated absolute paths do not conflict; queue enforcement is not an autonomy claim.
- Distinct S1 units: separately executing writable worker children.
- Inter-S1 disturbance: overlapping file/subtree modification and shared-provider quota contention.
- Attenuating coordination relation: declared-scope conflict detector plus reservations and concurrency cap.
- Feedback into subsequent S1 behaviour: a blocked child starts only after owner result/lock release; parent receives overlap acknowledgement and later results.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the launch condition depends on concrete competing ownership of the same path or provider quota, rather than task sequence alone.

## S3 — Inside-and-now control

- State: A
- Function: current whole-session regulation of child commitments and intervention on behalf of the engineering task.
- Disturbance / variety regulated: stalled, duplicative, expensive or no-longer-useful live work across the child set.
- Decisive decision or feedback right: cancel, restart or steer a selected running/queued child after observing current session-wide state.
- Decision owner: the parent coding agent in subagent-enabled mode.
- Supporting / enforcement mechanisms: subagents_list exposes phase, elapsed/turns/tokens/cost and scopes; control interrupts/kills and frees locks/slots.
- Closure path: chosen intervention changes running/queued work; exactly-once finalization returns outcome as a steer message and frees resources for subsequent work.
- Boundary reachability: installed tool registration exposes list, message and control to the parent; those handlers reach live child registry/cancel/restart functions.
- Why this is / is not agent-owned: the agent chooses which current commitment to change; deterministic budget stops, alone, would enforce only preselected ceilings.
- Evidence: [extensions/subagents/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/index.ts); [extensions/subagents/status.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/status.ts); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md).
- Basis: structural.
- Confidence: medium.
- Caveats: bounded to one session's child set; not a claim of organization-wide governance or a distinct human parent mode.
- Whole-system current view: all this session's registered/running/queued children with live metrics and scope ownership.
- Current-control decision scope: stop or re-dispatch current child commitments, steer work and thereby release/reallocate occupied scope and execution capacity.

## S3* — Complementary audit

- State: A
- Function: optional complementary source inspection that can challenge a worker's completion/correctness claim.
- Disturbance / variety regulated: worker summaries or normal test reports omit defects, races or guard regressions.
- Decisive decision or feedback right: independently judge the actual diff and surrounding code; return APPROVE or REQUEST_CHANGES with reproducible findings.
- Decision owner: the installed read-only reviewer agent; parent agent receives and acts on findings.
- Supporting / enforcement mechanisms: separate role context/tool loadout, direct git/piread/test access, durable review report and ordinary subagent result delivery.
- Closure path: review findings are delivered to the parent as a new steer turn; the parent can revise work or dispatch correction before committing.
- Boundary reachability: reviewer is a shipped named role discoverable by subagent registration, with isolated context and direct artifact inspection; delivery wakes the existing parent session.
- Why this is / is not agent-owned: audit judgment comes from a distinct actor with complementary raw-artifact access, not the worker's summary or a verdict parser.
- Evidence: [agents/reviewer.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/reviewer.md); [extensions/subagents/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/index.ts); [extensions/subagents/README.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/subagents/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: optional source-first review of a handed-off change, not automatic coverage of every claim; routine worker tests and the verifier's naming alone are not credited.
- Claim being audited: worker's changed code is correct and safe to commit.
- Ordinary reporting path: worker final summary and git-delta result.
- Complementary access path: reviewer independently obtains git status/diff, reads callers/surrounding source and runs narrow checks.
- Independence boundary: isolated child context; read-only role cannot implement its own fix or silently reuse the worker's narrative as evidence.
- Who acts on findings: the parent engineering agent, through editing or corrective worker dispatch after delivered review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-then capability-adaptation loop established at the deployed boundary.
- Disturbance / variety regulated: model/tool/environment change would require prospective sensing, options and return into capability.
- Decisive decision or feedback right: no shipped decisive prospective adaptation right established.
- Decision owner: not established; operator/maintainer updates are outside this mapping.
- Supporting / enforcement mechanisms: researcher, docs-optimizer, history and startup self-heal can support tasks or maintenance.
- Closure path: no evidenced prospective option-to-current-capability loop in the installed standard modes.
- Why this is / is not agent-owned: web research for an assigned task, history injection and path/version repair do not themselves decide future harness capability.
- Evidence: [extensions/self-heal/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/self-heal/index.ts); [agents/researcher.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/researcher.md); [agents/docs-optimizer.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/docs-optimizer.md); [docs/skills.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/skills.md); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md).
- Basis: structural.
- Confidence: medium.
- Caveats: does not rule out user-authored research/optimization work; repository benchmark/dogfood is excluded.

### Absence scope

- Surfaces inspected: [extensions/self-heal/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/self-heal/index.ts); [agents/researcher.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/researcher.md); [agents/docs-optimizer.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/agents/docs-optimizer.md); [docs/skills.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/skills.md); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md); scripts/bootstrap.sh, extensions/subagents, native piread/piedit/pibash extensions, installed agents and their role-specific tools, permission-gate and documented session controls..
- Plausible first-party paths checked: startup version checks, researcher role, docs optimization, installed skill invocation and history-derived feedback; operator update path also considered.
- Why no material first-party path remains: shipped paths perform local task research, installation consistency or operational reuse; no environment/future adaptation options with a returned capability decision are wired for this system.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy dispute/decision closure established.
- Disturbance / variety regulated: conflict about purpose or ultimate risk policy, rather than individual edit/command permission.
- Decisive decision or feedback right: no first-party identity-level authoritative resolution path found.
- Decision owner: operator owns initial configuration; no qualifying runtime S5 parent loop evidenced.
- Supporting / enforcement mechanisms: SYSTEM.md, role restrictions, permission gate and settings constrain operation.
- Closure path: ordinary deny/note/approval and config updates regulate actions but do not close identity-level deliberation.
- Why this is / is not agent-owned: removing an agent leaves static rules; neither enforcement nor generic operator involvement establishes ultimate-policy ownership.
- Evidence: [SYSTEM.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/SYSTEM.md); [settings.json](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/settings.json); [extensions/permission-gate/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/permission-gate/index.ts); [extensions/permission-gate/rules/phase.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/permission-gate/rules/phase.ts); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md).
- Basis: structural.
- Confidence: medium.
- Caveats: maintainer contribution/release governance is adjacent to the installed product.

### Absence scope

- Surfaces inspected: [SYSTEM.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/SYSTEM.md); [settings.json](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/settings.json); [extensions/permission-gate/index.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/permission-gate/index.ts); [extensions/permission-gate/rules/phase.ts](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/extensions/permission-gate/rules/phase.ts); [docs/subagents.md](https://github.com/nurmdrafi/pi-native/blob/b4e99cf3d2f60a1fd5e810bdfcbcbf47b3692e8f/docs/subagents.md); scripts/bootstrap.sh, extensions/subagents, native piread/piedit/pibash extensions, installed agents and their role-specific tools, permission-gate and documented session controls..
- Plausible first-party paths checked: system/role prompts, runtime gate, session controls, operator configuration and self-hosted deployment; positive/parent modes tested.
- Why no material first-party path remains: these paths select tools, permission rules or ordinary task interventions; no policy-identity issue reaches a legitimate ultimate authority and returns as an authoritative runtime policy decision.

## Distributed OSS parent arrangement

MIT licensing and contributor/maintainer activity establish distribution provenance, not project-level S3/S4/S5 parent closure. This assessment concerns the deployed product boundary; no organization-level parent mode is inferred from local maintainer decisions.

## Self-hosted and non-human modes

The operator can enable/disable subagents and choose settings. Generic session commands and initial permission configuration do not establish separate S3/S4/S5 parent modes. Autonomous current-control is supported by the parent agent tools in the enabled mode.

## Recursion

Nested execution and delegated tasks do not establish recursive viable systems; no child full metasystem is claimed.

## Variety and escalation

Tool-specific gates attenuate unsafe actions; declared scopes suppress collision variety; results and usage metrics amplify parent visibility. Worker questions and failures return to the parent agent. Startup notices and budget_exceeded are status signals, not automatically algedonic/S5 channels.

## Evidence gaps

Source-first assessment only. No Pi/model/tmux E2E run. Native Node tests were not run because node is absent in the review workspace; source and relevant regression-test surfaces were inspected. Optional role invocation cannot prove audit effectiveness or completeness in a deployment. No undisclosed external Pi behavior is imported.
