---
harness_id: minidsh
project_name: MiniDSH
repository: https://github.com/earthwalker17/MiniDSH
review_ref: 827c87e9f9785c4283f8b992126bd0413320152e
reviewed_at: 2026-11-07
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

# MiniDSH

## Review boundary

- System in focus: the first-party shipped TypeScript coding-agent harness and its standard composition, covering the kernel/core single-agent loop, tool/LLM providers, permissions, durable sessions, command/file tools and a foreground delegated child.
- Purpose and identity: perform code investigation and changes under bounded permissions, keep reliable evidence of tool effects and session continuity, and support several human-facing transport surfaces.
- Relevant environment: mutable repository files, command outcomes, LLM provider/model availability, local OS confinement, operator approval, session-log crashes, context budget and optional composition patches.
- Standard-distribution boundary: `bin/minidsh.js` → `src/app/{cli,headless,web,compose}.ts`, `src/core/{loop,agent,tools,session,sandbox,approval}`, `src/capabilities/{tool-editor,tool-shell,tool-subagent,model-roles,compaction-basic,context-runtime,persistence-jsonl}`. This is **MiniDSH**, not the upstream `deepseek-ai/deepseek-harness` it studies.
- Credited operating / distribution surfaces: the shipping default `src/app/compose.ts` rows, model/tool driver and subagent execution, bound editor/shell tools, authority stamps/approval, session persistence/crash repair and workbench/JSON-RPC callers.
- Adjacent first-party surfaces excluded from ownership: the research notes under `references/dsh/` concerning another harness; design proposals for background jobs in `docs/BLUEPRINT.md`; CI/build/release tests; manually invoked cold `sessions verify` / `inspect` CLI reports; optional test-injected `tool-verifier` composition not installed in the standard defaults.
- First-party modes considered: default model-operated coding loop; user-/model-directed foreground `subagent` tool (child with its own event log and authority ceiling); context compaction/history recall; durable authority decisions, approvals and OS file confinement; optional user configuration and model roles. An additional read-only vision verifier can be *assembled* with three composition patches, but its test-specific integration is not a default operating audit path.
- Recursion level: one coding goal and optionally one subordinate one-shot task agent; the parent calls and awaits that child in the foreground. No independently coordinated concurrent S1 team or whole-current portfolio manager is shipped.
- Reviewed source: `earthwalker17/MiniDSH@827c87e9f9785c4283f8b992126bd0413320152e` (stable GitHub repository ID `1341766256`), released package version `1.1.0`; Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

The runtime composes a first-party `core/loop/driver.ts` model/tool loop, an `llm` adapter, and a single gateway through `core/tools/registry.ts`. A model step may produce editor/shell/read tools, whose validated and approval-gated effects are logged before and after execution. The agent receives results, can repair an error, steer the following step and ultimately complete the user's task. The log is append-only and supports crash repair, compaction and bounded history recall; there are two shipped LLM providers, DeepSeek and Anthropic.

The default `tool-subagent` row is a true separate first-party S1: it creates a child model/tool loop, a distinct log, a maximum-depth/steps ceiling and narrower or equal `sandbox/mode`; approval is pinned `never`. Its parent logs `subagent/start|end` and receives the answer as one tool result. However, the child is **foreground**, the parent waits and tool executions are sequential. No coordination decision over interfering autonomous writers, shared commitments or cross-agent conflict repair was found.

`sessions verify` is an offline, human-requested **event-log integrity** checker: it reads stored bytes and session/authority invariants, predicts crash closers and reports invalid/torn logs. It does not independently inspect the code the model claimed to have fixed, return task-audit findings to an acting S3, or ratify policy. The additional `tool-verifier` read-only vision role in `src/app/verification.e2e.test.ts` exists as a patch-built example, not a standard composition row; it checks image content for a directly requested task, not a post-production disagreement over a coding result. Neither is silently promoted to a standard S3* organizational path.

Frozen first-party sources:

- [Product, releases, deliberate limits](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/README.md)
- [Architecture, loop, authority, verification, limitations](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/docs/ARCHITECTURE.md)
- [Default composition including native subagent](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/compose.ts)
- [First-party loop driver](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/core/loop/driver.ts), [tool gateway](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/core/tools/registry.ts)
- [Foreground delegated model-backed child and authority ceiling](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/index.ts), [delegation integration tests](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/subagent.test.ts)
- [Read-only vision verifier test-specific composition](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/verification.e2e.test.ts)
- [Cold integrity reader, explicitly CLI-only](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/inspect.ts)
- [Persisted session and user authority paths](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/core/session/index.ts), [authority code](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/core/sandbox/index.ts)

## Operational model

The user supplies a programming goal and authority. The model decides tool calls and whether to delegate a bounded research/search/edit subtask; first-party tooling performs effects and returns results into the active decision context. The delegated child is genuinely model-operated but waits in the same foreground action chain. Policy/approval invariants are deterministic enforcement and operator decisions; an optional external human cold audit of the session log is not an independent correctness reviewer.

## S1 — Operations

- State: A
- Function: perform code inspection, source edits, command/test execution and bounded delegated subtask operations.
- Disturbance / variety regulated: unknown repository structure, coding faults, changing file state, errors/refusals from tools, provider failures, context overflow and child-task outcomes.
- Decisive decision or feedback right: the configured LLM selects code/tool steps and whether to invoke the shipped `subagent`; the child uses its own model over a narrower task and returns evidence to the parent model for further action.
- Decision owner: first-party parent model/tool loop plus a model-driven child S1 for delegated tasks, each under the inherited authority constraints.
- Supporting / enforcement mechanisms: core `loop` and tool registry, editor/shell, default `tool-subagent`, model roles, session durable log, compaction, `history_read`, sandbox, approvals and plugin-scoped tool registration.
- Closure path: user goal → parent model decides and dispatches effect or child → first-party tool/child observes real environment and returns log/result → parent model continues, corrects or replies.
- Boundary reachability: the default `compose()` mounts `agent`, `loop`, first-party editor/shell and `tool-subagent` rows; headless/terminal/web all drive the same runtime.
- Why this is / is not agent-owned: model(s) autonomously choose task-directed source/tool operations and adapt to observed results; deterministic enforcement and user approval do not own task selection.
- Evidence: [default rows](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/compose.ts), [model loop](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/core/loop/driver.ts), [delegation](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/index.ts).
- Basis: explicit + structural, corroborated by shipped unit/integration test source.
- Confidence: high for reachable code path.
- Caveats: no provider-backed live inference session was run in this assessment environment; bundled E2E tests may skip without keys.

## S2 — Coordination

- State: —
- Function: no anti-interference coordination relation among independent concurrently operating S1 owners is established.
- Disturbance / variety regulated: multiple client attachments, session resume/fork lease conflicts and foreground child task outcomes are real engineering hazards, but not simultaneous autonomous S1 work-conflict settlement.
- Distinct S1 units: parent and one child are genuinely distinct model loops; each has a separate session. They are **serial** because delegation waits for the child; other sessions are separately operated rather than a configured cooperative unit.
- Inter-S1 disturbance: no documented overlapping model-driven writes with competing ownership claims; parent-child handoff itself is a task result.
- Attenuating coordination relation: authority ceilings restrict the child, and session leases exclude dual writers to one log, but no adaptive relation detects shared task collisions and reconciles separate S1 commitments.
- Feedback into subsequent S1 behaviour: child answer becomes parent tool result; this is normal delegation, not a conflict/settlement decision among simultaneously interfering S1 units.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a sequential child tool and parent result routing do not establish anti-oscillation over coupled independent operations; multiple UI clients just observe the same session.
- Decisive decision or feedback right: no first-party shared S1 conflict arbitration decision.
- Decision owner: static authority gates and parent S1 task decisions, not a separate S2 coordinating function.
- Supporting / enforcement mechanisms: `subagent/start|end`, child ceiling, session leases, sequential tool dispatch and protocols for multiple read-only clients.
- Closure path: parent delegates → child returns bounded task answer → parent continues, without independent competing S1 disturbance or dispute resolution.
- Why this is / is not agent-owned: actual child autonomy establishes another operating unit, but not an inter-unit coordination feedback path.
- Evidence: [subagent implementation](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/index.ts), [sequential execution limit](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: prospective background jobs are explicitly future work, not present at the frozen release.

### Absence scope

- Surfaces inspected: default tool-subagent, parent/child log and test, session leases, core loop sequential tool order, multi-client protocol and background-jobs design.
- Plausible first-party paths checked: overlapping team write claims, shared commitment allocation, conflict detection, autonomous inter-agent negotiation and returned resolution.
- Why no material first-party path remains: one awaited foreground child is the sole default delegation mode and the product explicitly has no background jobs.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current manager governs a portfolio of operational S1 commitments with reallocation/exception intervention.
- Disturbance / variety regulated: model/token context pressure, live session state, tool/child budget, driver cancellation and authority upgrades constrain one task or govern human access.
- Decisive decision or feedback right: no separate S3 decides priority and resource transfer across distinct S1 work cells; the parent agent delegates one job as part of its own task, and the human changes session policy.
- Decision owner: parent operating S1 for task-level delegation; operator for approval/session mode; fixed runtime for ceilings and lease.
- Supporting / enforcement mechanisms: `maxSteps`, context metering, model roles, child depth, authority pins, durable lifecycle and cancellation.
- Closure path: child completion or tool refusal → parent S1; external user may reconfigure permissions; no whole-current portfolio supervisory feedback.
- Why this is / is not agent-owned: dependable process/session management and authority constraints do not alone assign organization-wide current control.
- Evidence: [architecture / concurrency limit](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/docs/ARCHITECTURE.md), [delegation scope](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/index.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: even durable direct parent/child task control lacks a separate current portfolio-management authority here.

### Absence scope

- Surfaces inspected: agent factory/loop, scoped delegation and model roles, session lifecycle, settings, status/approval protocol, context compaction.
- Plausible first-party paths checked: whole-current resource state over multiple S1 goals, supervisory reprioritization, cross-cell exception decision and binding return.
- Why no material first-party path remains: all actual control is local to a single sequential parent task or human-established access regime.

## S3* — Complementary audit

- State: —
- Function: no default first-party complementary audit actor independently checks a completed coding claim against fresh operational reality and returns binding corrective findings.
- Disturbance / variety regulated: logs can be torn/invalid, model output can be incorrect and a text-only agent cannot interpret an image; only the first is covered by the standard cold log-integrity reader.
- Decisive decision or feedback right: cold `sessions verify` reports event/authority integrity to a CLI user; the optional verifier role is a composition **test fixture** requiring extra rows and a model route, not a default post-production challenge to the coding agent's report.
- Decision owner: existing runtime invariants for log format, external human for cold inspection, optional independent image-capable child for a specifically requested task.
- Supporting / enforcement mechanisms: `app/inspect.ts` log check, authority/session invariant folds, `tool-subagent` with optional `tool-verifier` patch and `model-roles`.
- Claim being audited: whether the user's requested code edit/test result is actually correct (distinct from whether the session log is structurally valid).
- Ordinary reporting path: the producing model reports tool results and its own answer in the durable session log.
- Complementary access path: cold verifier has independent *log byte* access only; patched vision child sees a real PNG, but the test has the parent ask it to fulfill an image task, not independently contradict a prior coding success claim.
- Independence boundary: separate process read of event records is independent of the writer process but not of the writer's task evidence; optional vision child has independent modality but no shipped routine audit-to-control arrangement.
- Who acts on findings: operator reads cold verify output; model can act on the optional verifier's ordinary tool answer. No distinct correction route from a production-audit verdict is evidenced.
- Closure path: `sessions verify` → human CLI report with exit status; optional image-question → child answer → parent writes requested file. Neither closes a complementary production audit and corrective control loop.
- Why this is / is not agent-owned: independent logfile integrity, generic delegated research and test-only patch examples do not establish an operational, first-party S3* review function.
- Evidence: [cold reader semantics](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/inspect.ts), [verification test-only extra patch](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/verification.e2e.test.ts), [standard rows](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/compose.ts).
- Basis: structural absence review with explicit independent-path differentiation.
- Confidence: medium-high.
- Caveats: a user-defined verifier configuration could be developed into a valid S3* path, but such a standard source-backed audit/return path was not evidenced at this frozen boundary.

### Absence scope

- Surfaces inspected: cold verify/inspect, session/authority invariants, standard composition, generic delegated child, optional vision E2E composition and result feedback.
- Plausible first-party paths checked: independent code artifact inspection, reviewer contradiction after production, binding finding-to-rework, separate report/evidence owner.
- Why no material first-party path remains: checks of log validity and optional task-specific image reading are not an installed independent coding outcome audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no autonomous prospective external-environment model produces, selects and operationalizes strategic changes to the future harness.
- Disturbance / variety regulated: LLM route changes, context pressure, plugin extension, software release evolution and environment models are handled as current setup/context or human development.
- Decisive decision or feedback right: human supplies `composition.json` rows/model role and software updates; model responds to present coding work.
- Decision owner: developer/operator for future architecture and composition; current coding S1 for immediate research and task action.
- Supporting / enforcement mechanisms: composition patches, model switching, compaction and role routing, developer `BLUEPRINT.md` and source architecture rules.
- Closure path: operator configures a new plugin/model or current history is compacted; neither establishes agent-authored future strategy, validated adaptation and returned deployment.
- Why this is / is not agent-owned: a highly evolvable plugin architecture and declarative default roles are *adaptability*, not a first-party closed S4 decision process.
- Evidence: [composition](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/app/compose.ts), [design roadmap](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/docs/BLUEPRINT.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: author-led evolution of the OSS project is not itself agent ownership inside the installed coding harness.

### Absence scope

- Surfaces inspected: composition registry/config, model roles and route selection, compaction, project/blueprint docs and release pipeline.
- Plausible first-party paths checked: prospective environment scanning, strategy-option generation, comparative evaluation, authorized selection and durable new capability rollout.
- Why no material first-party path remains: future changes are externally configured and tested by developers, not chosen by an installed S4 actor.

## S5 — Policy and identity

- State: —
- Function: no first-party highest legitimate policy/identity function adjudicates mission-level conflicts and ratifies the organization's purpose.
- Disturbance / variety regulated: risky commands, shell sandbox escapes, parent-child authority escalation and operator consent govern effects and security, not legitimate organizational identity.
- Decisive decision or feedback right: consent/permission switches are operator-owned, and immutable runtime guards reject illegal child widening; neither can redefine a top-level mission charter with authoritative closure.
- Decision owner: human operator for granted effects, source-defined sandbox/invariants for refusals, model for coding-task choice.
- Supporting / enforcement mechanisms: `approval/asked|decided|grant`, `sandbox/mode`, delegation ceiling, trusted consent subjects, human CLI/TUI controls and composition trust warnings.
- Closure path: tool permission request → allowed/refused within sandbox/approval service → result delivered to same S1; no policy identity dispute, deliberation and binding organizational charter return.
- Why this is / is not agent-owned: sophisticated permission boundaries are essential controls but not by themselves the S5 function.
- Evidence: [authority definitions](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/docs/ARCHITECTURE.md), [subagent pinned scope](https://github.com/earthwalker17/MiniDSH/blob/827c87e9f9785c4283f8b992126bd0413320152e/src/capabilities/tool-subagent/index.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a deploying organization may supply ultimate policy externally, but that is not a shipped MiniDSH S5 closure.

### Absence scope

- Surfaces inspected: approved effect facts, grants, child ceilings, authority invariant, shell confinement, operator settings and project mission text.
- Plausible first-party paths checked: identity conflict, ultimate parent legitimacy decision, ratification and durable returned policy direction for future agent behavior.
- Why no material first-party path remains: all identified mechanisms decide safety/capability during execution rather than legitimate organizational mission.

## Recursion

MiniDSH can recurse into a genuine first-party subordinate model/tool S1, but only through bounded, awaited foreground delegation. The parent remains task-operational and no independent S2/S3 metasystem managing competing current units is shown. Human session policy and source architecture are outside the harness's autonomous VSM function ownership.

## Variety and escalation

The model regulates coding variety through tools and real feedback; the kernel logs effects and limits authority. A child cannot widen its authority or ask for escalation; it hands the parent one result. Crashes can be repaired and logs cold-verified, but the cold verifier reads recorded events rather than independently testing the coding claim. Configuration, history and consent do not form additional autonomous organizational closure.

## Evidence gaps

The exact frozen Git checkout, GitHub repository ID, default composition, native loop/delegation, authority code, documentation and relevant test wiring were inspected. Node 24 was available but the pinned `pnpm` dependencies were not installed; `pnpm check`, gated live provider E2E and runtime shell confinement tests were **not executed** in this assessment. Shipped tests and CI descriptions are source evidence, not observed local passes. The optional vision-verification test uses patches and keys and is not treated as live default audit evidence.

## Assessment summary

MiniDSH is an implemented, model-driven coding harness with native foreground subagent recursion and durable evidence of actions (**S1=A**). Its distinctive strengths are authority ceilings, log integrity, context recovery and plugin boundaries; these are not automatically cross-agent conflict control, whole-current supervision, complementary *coding-result* audit, future adaptation strategy or ultimate-policy ratification. No positive closed first-party S2/S3/S3*/S4/S5 path was established at the exact frozen release.

Proposed vector: **`A · — · — · — · — · —`**.
