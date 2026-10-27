---
harness_id: coderrr
project_name: Coderrr
repository: https://github.com/Akash-nath29/Coderrr
review_ref: 933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1
reviewed_at: 2026-10-27
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

# Coderrr

## Review boundary

- System in focus: one Coderrr v2 terminal coding session and its concrete Python runtime, not the upstream provider or an OSS contributor organization.
- Purpose and identity: produce a reviewable specification, then implement and verify approved code changes.
- Relevant environment: user request, local workspace, model HTTP endpoint, scratch/Docker execution and optional skill registry/MCP servers.
- Standard-distribution boundary: installed Python CLI and shipped planning/execution orchestration at the frozen revision.
- Credited operating / distribution surfaces: `src/coderrr/agent`, prompts, tool registry/read/write/spec tools, policy, specification store, sandbox, verifier, skill loader and MCP lifecycle.
- Adjacent first-party surfaces excluded from ownership: repository development tests/CI and the separate remote coderrr-skills repository; tests corroborate wiring without becoming runtime owners. Legacy npm/v1 behavior is not substituted.
- First-party operating / deployment modes considered: interactive plan approval; `--yes` auto approval; optional per-write confirmation; default write verifier or disabled/configured verifier; scratch/Docker sandbox and optional configured MCP.
- Recursion level: individual coding session; sequential specification tasks are work items of one operating agent, not independently viable units.
- Reviewed revision: `933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI assembles a Session with provider, ToolRegistry, SpecStore, SkillManager, sandbox, MCP manager and verifier. Planning runs the model/tool conversation with ordinary file-write tools omitted. The agent creates requirements/design/tasks artifacts, which Session presents to the user. Approved execution changes the exposed tool set and runs a model/tool loop; tool results return to the next model turn. A finite outer loop retries failed attempts. Specs persist task state while remote skill guidance is loaded on demand and normally removed after use. The model chooses code edits and sandbox commands; runtime enforces budgets, paths, mode/tool permissions and MCP consent. Writes receive a separate stateless model correctness check before mutation, with fail-open handling for unavailable/malformed verifier output. This is routine pre-write QA rather than a complementary operational audit. No worker/team scheduler or independent organizational regulator is shipped.

Primary architecture: [src/coderrr/agent/session.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/session.py), [src/coderrr/agent/loop.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/loop.py), [src/coderrr/tools/registry.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/registry.py), [src/coderrr/config.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/config.py), [src/coderrr/verify.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/verify.py).

## Operational model

One agent owns the ordinary read → propose/edit → sandbox observation → revise/finish decisions. A human selects the requested outcome and authorizes implementation; this does not choose every operational action. The same actor moves spec tasks through statuses. Generic ask_review returns user clarification into the ongoing conversation. Runtime retry limits and permission gates enforce preselected constraints; neither is credited as a whole-system discretionary controller.

## S1 — Operations

- State: A
- Function: transform an approved specification into code and verified task outcomes.
- Disturbance / variety regulated: uncertain project structure, tool errors, failed acceptance checks and unexpected code behavior.
- Decisive decision or feedback right: choose inspections, edits, sandbox commands, corrective next actions and task completion.
- Decision owner: coding model agent after the ordinary plan authorization.
- Supporting / enforcement mechanisms: Session phase transition, ToolRegistry, local filesystem, sandbox, SpecStore, budget and HTTP provider transport.
- Closure path: registry executes model calls; observations become ToolResultBlocks in the next model request; the agent revises work and chooses finish/update_task.
- Boundary reachability: Session.execute directly invokes run_task/run_conversation using the installed registry; no developer-authored custom agent composition is required.
- Why this is / is not agent-owned: removing the model leaves gates and persistence but no equivalent code-change choices. Human authorization limits the task without supplying those choices.
- Evidence: [src/coderrr/agent/loop.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/loop.py), [src/coderrr/agent/session.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/session.py), [src/coderrr/prompts/system.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/prompts/system.py), [src/coderrr/tools/system/review.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/system/review.py).
- Basis: structural.
- Confidence: high.
- Caveats: static supported-path evidence, not measured task success; MCP tools may have external side effects even during planning once allowed.

## S2 — Coordination

- State: —
- Function: Interference regulation among distinct operational units; not established at this boundary.
- Disturbance / variety regulated: no qualifying function-specific regulation established beyond ordinary coding-task variety.
- Decisive decision or feedback right: The reviewed runtime has one sequential operational actor; an inner tool loop and outer retry loop do not form distinct interacting S1 units. Batched calls are executed sequentially.
- Decision owner: no first-party owner for the absent organizational function; ordinary task/configuration rights stay with the actors described above.
- Supporting / enforcement mechanisms: relevant mechanisms are recorded here without inheriting ownership.
- Closure path: no qualifying function-specific closure found in the checked modes.
- Why this is / is not agent-owned: an agent performing ordinary code work or a stateless verifier call does not by itself own this separate organizational function.
- Evidence: [src/coderrr/agent/loop.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/loop.py), [src/coderrr/tools/registry.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/registry.py).
- Basis: structural.
- Confidence: medium-high; bounded to inspected distribution.
- Caveats: not a claim of universal impossibility or external deployment absence.

### Absence scope

- Surfaces inspected: agent loop, tool registry, session and planning/execution prompts.
- Plausible first-party paths checked: parallel tool-request payloads, task statuses, retry sequencing and MCP dispatch.
- Why no material first-party path remains: none supplies an inter-S1 conflict/oscillation-specific coordination right with feedback into separate units.

## S3 — Inside-and-now control

- State: —
- Function: Whole-system current operational cohesion and intervention; not established at this boundary.
- Disturbance / variety regulated: no qualifying function-specific regulation established beyond ordinary coding-task variety.
- Decisive decision or feedback right: Session presents the plan and task list, but the human merely authorizes one coding operation. Tool budgets and write policies enforce configured limits; the model's per-task planning is ordinary operation. No broader shared-resource/commitment regulator or specific S3 constructor is supplied.
- Decision owner: no first-party owner for the absent organizational function; ordinary task/configuration rights stay with the actors described above.
- Supporting / enforcement mechanisms: relevant mechanisms are recorded here without inheriting ownership.
- Closure path: no qualifying function-specific closure found in the checked modes.
- Why this is / is not agent-owned: an agent performing ordinary code work or a stateless verifier call does not by itself own this separate organizational function.
- Evidence: [src/coderrr/agent/session.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/session.py), [src/coderrr/config.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/config.py), [src/coderrr/tools/system/review.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/system/review.py).
- Basis: structural.
- Confidence: medium-high; bounded to inspected distribution.
- Caveats: not a claim of universal impossibility or external deployment absence.

### Absence scope

- Surfaces inspected: session presentation/approval/execute driver, budgets/configuration, registry, spec-driven execution and ask_review.
- Plausible first-party paths checked: plan approval/--yes, per-write consent, task progress, retry/abort and clarification paths.
- Why no material first-party path remains: those paths bound or clarify the same operation without a whole-system discretionary resource/commitment control conversation.

## S3* — Complementary audit

- State: —
- Function: Independent complementary challenge to ordinary operational reports; not established at this boundary.
- Disturbance / variety regulated: no qualifying function-specific regulation established beyond ordinary coding-task variety.
- Decisive decision or feedback right: Verifier receives a proposed write and current content in a fresh model request and can reject it. This is a mandatory ordinary production check per write, not alternative access challenging the producer's completion/reporting claims. Its independent call context alone does not establish S3*. Sandbox tests are also normal self-verification.
- Decision owner: no first-party owner for the absent organizational function; ordinary task/configuration rights stay with the actors described above.
- Supporting / enforcement mechanisms: relevant mechanisms are recorded here without inheriting ownership.
- Closure path: no qualifying function-specific closure found in the checked modes.
- Why this is / is not agent-owned: an agent performing ordinary code work or a stateless verifier call does not by itself own this separate organizational function.
- Evidence: [src/coderrr/verify.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/verify.py), [src/coderrr/tools/write/files.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/write/files.py), [src/coderrr/prompts/system.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/prompts/system.py).
- Basis: structural.
- Confidence: medium-high; bounded to inspected distribution.
- Caveats: not a claim of universal impossibility or external deployment absence.

### Absence scope

- Surfaces inspected: Verifier and NullVerifier, write-tool verification wiring, session verifier construction and execution prompts.
- Plausible first-party paths checked: fresh verifier model context, optional distinct model, before/after content, reject→revise feedback, sandbox exit-code checking.
- Why no material first-party path remains: all examined checks belong to routine production/acceptance; no separate complementary audit mandate/access/control path is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: External prospective intelligence returned as capability adaptation; not established at this boundary.
- Disturbance / variety regulated: no qualifying function-specific regulation established beyond ordinary coding-task variety.
- Decisive decision or feedback right: Skills search fetches task guidance and MCP adds configured tools; planning develops the current requested solution. Neither traces external/future distinctions into prospective adaptation options that change the harness's present capability through a corresponding current-control loop.
- Decision owner: no first-party owner for the absent organizational function; ordinary task/configuration rights stay with the actors described above.
- Supporting / enforcement mechanisms: relevant mechanisms are recorded here without inheriting ownership.
- Closure path: no qualifying function-specific closure found in the checked modes.
- Why this is / is not agent-owned: an agent performing ordinary code work or a stateless verifier call does not by itself own this separate organizational function.
- Evidence: [src/coderrr/skills/loader.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/skills/loader.py), [src/coderrr/prompts/system.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/prompts/system.py), [src/coderrr/config.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/config.py).
- Basis: structural.
- Confidence: medium-high; bounded to inspected distribution.
- Caveats: not a claim of universal impossibility or external deployment absence.

### Absence scope

- Surfaces inspected: skills loader/config, session context, system planning/execution instructions and provider/MCP setup.
- Plausible first-party paths checked: fresh registry guidance, ephemeral/persisted skills, plan/design revisions, model/provider choices and user clarification.
- Why no material first-party path remains: they provide current-task context or operator configuration, not a shipped externally prospective capability-adaptation decision and return loop.

## S5 — Policy and identity

- State: —
- Function: Legitimate identity/ultimate-policy closure; not established at this boundary.
- Disturbance / variety regulated: no qualifying function-specific regulation established beyond ordinary coding-task variety.
- Decisive decision or feedback right: Static Coderrr identity/safety instructions, mode restrictions and tool consent constrain work. ask_review handles requirements and blockers; no function-specific identity/policy dispute reaches a legitimate ultimate authority and returns an authoritative policy that governs later operation.
- Decision owner: no first-party owner for the absent organizational function; ordinary task/configuration rights stay with the actors described above.
- Supporting / enforcement mechanisms: relevant mechanisms are recorded here without inheriting ownership.
- Closure path: no qualifying function-specific closure found in the checked modes.
- Why this is / is not agent-owned: an agent performing ordinary code work or a stateless verifier call does not by itself own this separate organizational function.
- Evidence: [src/coderrr/prompts/system.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/prompts/system.py), [src/coderrr/tools/system/review.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/system/review.py), [src/coderrr/agent/session.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/agent/session.py), [src/coderrr/tools/registry.py](https://github.com/Akash-nath29/Coderrr/blob/933dd35a6f35fbb54f3e8a80a75356af9c0ff7f1/src/coderrr/tools/registry.py).
- Basis: structural.
- Confidence: medium-high; bounded to inspected distribution.
- Caveats: not a claim of universal impossibility or external deployment absence.

### Absence scope

- Surfaces inspected: identity/safety/system prompts, ask_review, Session approval, configuration and registry/MCP consent.
- Plausible first-party paths checked: human plan approval, clarifying questions, remembered tool grants and static safety/path policy.
- Why no material first-party path remains: ordinary task/permission decisions are not ultimate-policy closure; contributor governance and hypothetical custom MCP governance remain outside the runtime boundary.

## Distributed OSS parent arrangement

Maintainers and users may govern local copies, but no organization-level parent function is borrowed from contributor/CI activity. Reviewed parent candidates are the actual terminal plan/clarification/consent paths, as distinguished above.

## Self-hosted and non-human modes

Local interactive and auto-approval modes share the same operational loop. Scratch/Docker selection changes execution isolation, and verifier configuration changes routine QA. No qualifying S3/S4/S5 parent-mode closure was found.

## Recursion

Planning and execution phases and ordered spec tasks do not independently possess viable-system metasystems. MCP peers are external tools rather than automatically recursive units.

## Variety and escalation

Model receives tool errors, verification rejection and sandbox results. Finite budget exhaustion stops attempts; failed attempts get a diagnostic retry prompt. ask_review returns clarification from the present user; unanswered questions prompt further clarification. These are bounded operational feedback/escalation paths, not an automatic algedonic or S5 claim.

## Evidence gaps

No live model/provider task, external MCP service or Docker execution was run. Static first-party wiring supports ownership findings, not reliability/security/performance claims. Exact dependency/test execution availability is reported in the owning PR receipt. Large verifier inputs are excerpted and unavailable verifier results fail open, limiting what routine QA establishes.
