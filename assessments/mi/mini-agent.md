---
harness_id: mini-agent
project_name: Mini-Agent
repository: https://github.com/lizaixi01/Mini-Agent
review_ref: 221827fd2524d3574bdfb7dcbb888464d75ad95d
reviewed_at: 2026-11-03
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

# Mini-Agent

## Review boundary

- System in focus: the shipped single-process Python terminal agent in `agent.py`, including model/tool turn loop, command permission gate, sessions, memory and skill loading.
- Purpose and identity: carry out user terminal-assistant tasks with model-chosen tool requests and natural-language responses.
- Relevant environment: local shell and files, a terminal user, optional DeepSeek model API, locally persisted sessions/memory and skills.
- Standard-distribution boundary: the repository-owned `agent.py` terminal program in supported DeepSeek or no-key demo mode; external model inference is a dependency, not an independent agent harness.
- Credited operating / distribution surfaces: `agent.py` model adapters, `run_agent`, `run_session_turn`, command execution, session/memory/skill loaders, recovery, CLI modes.
- Adjacent first-party surfaces excluded from ownership: lessons, standalone skill instructions, tests and contributor/development activities; tests corroborate code but do not contribute a deployed audit or metasystem.
- First-party operating / deployment modes considered: DeepSeek API tool-call mode, deterministic demo model, ask/deny command permissions, persistent/resumed sessions and optional memory/skills.
- Recursion level: one terminal assistant run/session, not a team of agents or the OSS development project.
- Reviewed revision: `221827fd2524d3574bdfb7dcbb888464d75ad95d`.
- Observation date: 2026-11-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The first-party `run_agent` loop appends a user task, queries a model, validates its `tool_calls`, executes permitted built-in tools, appends observations and re-queries the model up to `MAX_STEPS`. The model chooses a command, memory proposal or skill read; user confirmation gates shell execution and saved memory. Sessions and turns are written atomically to JSON; interrupted pending calls are marked uncertain rather than silently replayed. `DemoModel` supplies a reproducible scripted exercise of the same loop, while the OpenAI-compatible DeepSeek adapter supplies model-driven responses when configured. Skills and remembered items expand context, not independent operational units. Tests/lessons are adjacent evidence, and no self-directed future environment adaptation or separate independent auditor is wired into the standard distribution.

Primary source: [README](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/README.md), [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py), [test_agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/test_agent.py).

## Operational model

One operational unit is the agent turn loop: it transforms an open-ended user request into model-selected command/skill/memory actions and an answer. The agent owns the discretionary next-action choice; deterministic validation, max-step enforcement and human command confirmation only bound or enforce execution. In `deny` mode shell actions are unavailable, but text/skill operation remains supported. Session persistence enables resumption without creating another S1. No evidence of two autonomous collaborating work units inside the supported product.

## S1 — Operations

- State: A
- Function: one model-guided assistant operational unit acts on a user task through tool selection, observation and continuation.
- Disturbance / variety regulated: variable task instructions, tool results, command errors, missing skill/memory context and user denials.
- Decisive decision or feedback right: choose whether and which tool to call next, interpret tool feedback and decide when to answer.
- Decision owner: the model-driven agent actor in the first-party `run_agent` loop; external provider computes model outputs, but does not supply the harness orchestration.
- Supporting / enforcement mechanisms: typed tool-call validation, `run_command`, `read_skill`, memory proposal, permission confirmation, `MAX_STEPS`, JSON sessions and pending-call recovery.
- Closure path: task → model reply/tool call → validated/approved tool execution or denial → returned tool message → next model step or final response.
- Boundary reachability: `main` constructs `DeepSeekModel`/`DemoModel` and invokes `run_session_turn` → `run_agent` with the bundled tools and sessions; no developer-written wiring is required for this loop.
- Why this is / is not agent-owned: the actor selects substantive actions; user approval can veto shell execution, but does not select the next task solution or dictate a command.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py), [README](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the no-key demo uses scripted replies and is not evidence of general model competence; no paid DeepSeek end-to-end claim is made.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 coordination relation at this single-agent recursion.
- Disturbance / variety regulated: tool ordering and recovery within one actor, not interference between multiple autonomous operational units.
- Decisive decision or feedback right: no function-specific cross-unit conflict resolution exists.
- Decision owner: no qualifying S2 actor.
- Supporting / enforcement mechanisms: sequential tool-call loop and JSON session state.
- Closure path: each tool result returns to the same S1 actor; there is no inter-S1 adjustment.
- Why this is / is not agent-owned: sequencing within a single S1 is not S2.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py).
- Basis: structural.
- Confidence: high.
- Caveats: multiple independent terminal sessions are possible but no first-party cross-session coordination is defined.

### Absence scope

- Surfaces inspected: agent loop, session/turn management, skill/memory and CLI modes.
- Plausible first-party paths checked: multiple sessions as S1 units; tool-call ordering as coordination; pending-call repair as anti-interference.
- Why no material first-party path remains: no shipped relation connects distinct operational agents to attenuate a specific mutual disturbance and return coordinated behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control authority over separate S1 operations is established.
- Disturbance / variety regulated: command risk, step exhaustion and interrupted turns.
- Decisive decision or feedback right: current organizational resource/commitment bargaining or intervention across an operational whole is not supplied.
- Decision owner: human user sets/approves command permission; developer sets step/tool restrictions; model owns local S1 decisions.
- Supporting / enforcement mechanisms: `permission`, confirmations, `MAX_STEPS`, atomic session writes and repair markers.
- Closure path: a deny/approval/limit alters a local command or turn, not a whole-system S3 decision returning to multiple operational units.
- Why this is / is not agent-owned: deterministic guardrails and task-local user controls are not a current whole view or delegated S3 authority; no qualifying parent S3 mode closes at this recursion.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py).
- Basis: structural.
- Confidence: high.
- Caveats: future multi-agent composition is outside the reviewed distribution.

### Absence scope

- Surfaces inspected: permission modes, step loop, session/turn stores, CLI commands and recovery.
- Plausible first-party paths checked: user approval as parent S3; step cap as S3; session listing as whole-current view.
- Why no material first-party path remains: these constrain single-S1 tool execution without a qualifying whole-current organizational decision/return path.

## S3* — Complementary audit

- State: —
- Function: no materially independent audit of ordinary operational reports with corrective return is shipped.
- Disturbance / variety regulated: malformed tool arguments and interrupted calls.
- Decisive decision or feedback right: independent inspection of operational truth beyond routine agent/tool reporting.
- Decision owner: none; code validators and user prompts are routine enforcement.
- Supporting / enforcement mechanisms: argument checks, error tool messages, session events, tests.
- Closure path: failed validation returns an error to the same agent; no independent challenge actor and consequent control response.
- Why this is / is not agent-owned: routine tool validation and test fixtures cannot donate a separate complementary audit.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py), [tests](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/test_agent.py).
- Basis: structural.
- Confidence: high.
- Caveats: human inspection is possible outside the supported audit design.

### Absence scope

- Surfaces inspected: tool validation/permission, session events, recovery and tests.
- Plausible first-party paths checked: schema rejection as audit; user confirmation as independent review; test suite as runtime audit.
- Why no material first-party path remains: no separate complementary evidence acquisition and independent corrective feedback into operation exists.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptive options loop is wired into present capability.
- Disturbance / variety regulated: task variability and remembered user facts.
- Decisive decision or feedback right: develop options from future environment changes and feed adaptation into current operations.
- Decision owner: none established for S4; users choose retained memory and skills.
- Supporting / enforcement mechanisms: memory JSON, skill catalogue, session state.
- Closure path: accepted memory can condition later prompts, but no prospective environmental model/option/evaluation/implementation return to capability is provided.
- Why this is / is not agent-owned: persistent memory and skill use are not S4 by themselves.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py).
- Basis: structural.
- Confidence: high.
- Caveats: user-installed skills may change tasks, not a first-party adaptation regime.

### Absence scope

- Surfaces inspected: memory proposal/save/load, skill loading, sessions and readme roadmap.
- Plausible first-party paths checked: memory as learning/adaptation, skills as evolution, repeated sessions as environment sensing.
- Why no material first-party path remains: no shipped future-relevant external distinctions become adaptation options with a return into operating capability.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy judgment and returned parent or autonomous closure is established.
- Disturbance / variety regulated: command permission and user memory consent.
- Decisive decision or feedback right: choose/revise ultimate mission/identity/policy at this recursion.
- Decision owner: developer-supplied system message and human CLI permissions, not an ultimate-policy decision loop.
- Supporting / enforcement mechanisms: static `SYSTEM_MESSAGE`, `permission` ask/deny, confirmation prompts and tool allowlist.
- Closure path: permissions constrain local calls and memory writes; no identity-level issue reaches an authoritative decision and returns to govern subsequent organization operation.
- Why this is / is not agent-owned: a system prompt or ordinary shell/memory approval does not establish S5, including parent-governed S5.
- Evidence: [agent.py](https://github.com/lizaixi01/Mini-Agent/blob/221827fd2524d3574bdfb7dcbb888464d75ad95d/agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: developer maintenance is an adjacent higher recursion.

### Absence scope

- Surfaces inspected: system message, CLI permissions, memory consent, skills and session controls.
- Plausible first-party paths checked: user approvals as parent S5; static system prompt as policy authority; memory proposals as identity revision.
- Why no material first-party path remains: all paths concern local action/content restrictions rather than a legitimate identity/ultimate-policy decision returned into operation.

## Distributed OSS parent arrangement

No contributor/maintainer governance decision is counted as runtime S3/S4/S5 parent mode for a separately distributed terminal agent.

## Self-hosted and non-human modes

Local self-hosted operation exposes ask/deny command policy and user memory consent, but no function-specific parent supervisory/adaptation/ultimate-policy closure is shipped.

## Recursion

The single agent's tools and lessons are not recursive viable S1 organizations. No agent team or S2 recursion claim is made.

## Variety and escalation

Malformed calls return errors; unsafe commands go to the terminal user for veto; interrupted calls are recorded as uncertain. These are bounded S1/enforcement paths, not proof of S3/S3*/S5 or algedonic functions.

## Evidence gaps

The DeepSeek provider was not invoked with paid credentials; the structural model/tool loop and scripted demo exist in source. Local `python -m unittest -q` exercised 27 tests but one requires the optional `openai` dependency unavailable in this environment (`ModuleNotFoundError`), so no clean full upstream test pass is claimed.
