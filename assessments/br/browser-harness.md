---
harness_id: browser-harness
project_name: Browser Harness
repository: https://github.com/browser-use/browser-harness
review_ref: afbcc381b963040c19627d788e40c7e7663171ee
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Browser Harness

## Review boundary

- System in focus: the first-party `browser_harness` control layer, protected CDP/browser machinery, persistent daemon/tab model, editable agent workspace/helpers, skill contract and MCP surface at pinned revision `afbcc381b963040c19627d788e40c7e7663171ee`.
- Purpose and identity: let an LLM/coding-agent actor perform real browser work through a durable browser-control harness while safely reusing state and extending task-specific helpers.
- Relevant environment: local/remote Chrome, web sites and authenticated sessions, Browser Use Cloud, external LLM/coding-agent hosts and human browser approvals.
- Standard-distribution boundary: first-party CLI/daemon/helpers/skill/MCP and agent-workspace conventions. Claude Code/Codex/Devin/Cursor and model providers remain external actors/hosts.
- First-party modes considered: default local daemon; named local daemon as last-resort isolation; isolated remote/cloud browsers for simultaneous work.
- Recursion level: one browser-work organization; agent processes performing browser tasks are candidate S1 work units when multiple actors share the harness.
- Reviewed revision: `afbcc381b963040c19627d788e40c7e7663171ee`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

The harness exposes CDP browser actions and a persistent daemon with one mutable attached/current tab. Agent-editable helpers live outside protected core machinery and can be created as tasks reveal missing browser primitives. The shipped skill explicitly describes a multi-agent structural collision: two agents switching tabs/acting simultaneously through one local daemon can race and cause one actor to operate on or capture another actor's tab. The first-party response is to serialize local browser operations, or use separate remote browsers for truly simultaneous work; named local daemons are a constrained fallback.

## Primary evidence

- [`README.md`](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/README.md) — harness boundary, external-agent integration, editable helpers and MCP/browser-control surfaces.
- [`SKILL.md`](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/SKILL.md) — durable daemon/tab protocol, explicit multi-agent race condition, serialization/isolation response, recovery and cloud-browser modes.
- [`agent-workspace/agent_helpers.py`](https://github.com/browser-use/browser-harness/blob/afbcc381b963040c19627d788e40c7e7663171ee/agent-workspace/agent_helpers.py) — first-party extension point for agent-written task-specific browser helpers.

## Operational model

An external model-driven agent becomes an actor inside the Browser Harness-organized process when it follows the supplied skill and invokes first-party browser helpers. It autonomously selects browser actions to produce task outcomes, while the harness controls transport, browser attachment, state and safe usage conventions. Multiple such S1 actors can share a local browser lane, creating a concrete mutable-tab interference mode that the standard distribution explicitly regulates.

## S1 — Operations

- State: `A`.
- Function: autonomous interactive browser task execution in the live web environment.
- Disturbance / variety regulated: page state, navigation, DOM/accessibility structure, authentication/session state, dynamic UI and task-specific browser mechanics.
- Decisive decision or feedback right: the model-driven agent chooses browser actions, inspections, retries and task-specific helper additions.
- Decision owner: autonomous agent actor operating through the first-party skill/control surface.
- Supporting / enforcement mechanisms: CDP helper layer, daemon, tab state, MCP/CLI transport, diagnostics/recovery and editable helper workspace.
- Closure path: browser actions change page/environment state; subsequent observations and agent decisions consume those results until the task outcome is reached.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `C`.
- Distinct S1 units: multiple agent actors may concurrently perform browser work through the same local Chrome/harness boundary.
- Specific interference: one default daemon has one mutable attached/current tab; simultaneous tab switching/actions can race, causing an agent to act on or capture another agent's tab.
- Coordination relation: the shipped skill requires browser operations through the default local daemon to be serialized; for true simultaneity it directs each task to an isolated remote browser, with a named local daemon only as a last-resort isolation mechanism.
- Closure path: the chosen serialization/isolation arrangement changes later S1 browser behaviour by preventing concurrent mutation of the shared lane or separating the lanes entirely.
- Ownership: Browser Harness supplies the S2-specific disturbance model and regulation protocol, but it does not itself establish a single autonomous first-party coordinator that chooses ordering/isolation across arbitrary external hosts. The path therefore requires composition with the host/orchestrator/participating agents.
- Why not generic routing: the evidence identifies a concrete mutable-tab collision and a regulation response designed specifically to attenuate it.
- Basis / confidence: explicit + structural; high.

## S3 — Inside-and-now control

- State: `—`.
- The daemon manages connection/tab state and remote-browser lifecycle, but no distinct actor is established with a whole-system current view and discretionary authority over organization-wide resources, priorities or commitments. Connection recovery and lifecycle enforcement are supporting runtime mechanisms rather than S3 ownership.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- Recordings, screenshots, diagnostics and verification steps improve observability and task execution but do not form an independent complementary audit channel with separate judgment and corrective return into current control.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Agent-written reusable helpers can improve future task capability, but they arise from current task mechanics and are generated by the operating agent. The pinned distribution does not establish an externally/prospectively oriented environmental-intelligence loop that develops adaptation options and closes them into present capability through S3.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- Skill rules, browser permission prompts and user choices such as recording/cloud usage constrain operation but do not establish an identity/ultimate-policy decision loop at the harness recursion.
- Confidence: high.

## Recursion

External coding-agent hosts and cloud-browser instances are not automatically recursive viable systems inside Browser Harness; they are actors/substrates at this boundary unless separately assessed.

## Variety and escalation

The harness attenuates browser-state variety through one persistent attachment model and explicit tab-use rules, and amplifies operational repertoire through editable helpers. Connection failures escalate to diagnostics/recovery or a human browser permission step, but those paths are operational support rather than parent-governed metasystem states.

## Evidence gaps

The constructor classification for S2 deliberately does not infer autonomous coordination ownership from external orchestrators that are not part of the repository.

## Admission conclusion

Canonical vector: `A C — — — —`.
