---
harness_id: hashcortx
project_name: HashCortX
repository: https://github.com/Hash-7777/HashCortX
review_ref: ab3fb74a61928dfb98985eac5ec3eeac8c85afe7
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HashCortX

## Review boundary

- System in focus: first-party HashCoder coding mode in the HashCortX desktop app, its JavaScript agent model/tool loop, native Tauri file/shell operations, project permissions, diff/undo, proof tracking, sessions, and actually wired memory.
- Purpose and identity: a local-first coding agent acting autonomously on a selected real project, subject to explicit user authorization and ordinary completion checks.
- Relevant environment: user project root, source files, test tools and return values, provider/model endpoint, local security policy and user.
- Standard-distribution boundary: shipped first-party HashCoder runtime and its code/tool adapters, not the entire multi-workspace desktop application.
- Credited operating / distribution surfaces: src/modes/code/mode.js, src/platform/tauri/hashcoder.js, src/js/agent-policy.js, src/js/code/verify.js, src/core/memory/store.js, relevant native Rust safety code.
- Adjacent first-party surfaces excluded from ownership: Agent Swarm and its separate graph/workspace/runtime, ERP/Forge/Finance/Virtual OS/Sandbox workspaces; development tests/CI/maintainers and demo assets. External providers, MCP tools and separate services are dependencies.
- First-party operating / deployment modes considered: normal HashCoder on an open project, cloud/local model tool use and failover, permission approval, deterministic proof nudges, user diff Keep/Undo, shared memory fact recall.
- Recursion level: one HashCoder coding session; sibling desktop workspaces do not become S1 units of its coding organization.
- Reviewed revision: ab3fb74a61928dfb98985eac5ec3eeac8c85afe7.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The HashCortX Tauri desktop ships several different workspaces. HashCoder is a concrete source-native coding agent: its agentLoop calls a chosen inference provider, receives model-directed read/edit/shell tools, executes them through HC.code/Tauri and permissions, feeds tool results back into the same model history and iterates to a result. Its pure agent-policy batches independent reads, serializes writes/commands and stops or nudges repeated unproductive steps.

Proof logging uses the project's own available test/build/check commands. The first-party code can nudge the SAME agent to run a test after editing or to check missing request elements. The ordinary tool result log, deterministic test classification and self-review do not create an independent complementary auditor. The shared memory store extracts simple user facts into local storage for later recall.

Agent Swarm implements its own multi-agent run graph elsewhere in the desktop product. The assessed HashCoder loop does not invoke Swarm as its operating metasystem. This review therefore does not transfer Swarm's roles, constraints or team-control functions into HashCoder just because both are stored in the same repository.

Evidence: [coder](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js), [tools](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/platform/tauri/hashcoder.js), [policy](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/agent-policy.js), [verification](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/code/verify.js), [memory](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/core/memory/store.js), [swarm](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/swarm/graph.js).

## Operational model

The primary model exercises coding S1 discretionary tool actions and reacts to returned source/test observations. JS/Rust permission, batching, provider routing and proof checks enforce or support that S1. Nearby Swarm agents and other product modes belong to different organizational functions at different boundaries; they are excluded from the accepted coding system.

## S1 — Operations

- State: A
- Function: A single autonomous model-directed coding loop acts on user project files and tools.
- Disturbance / variety regulated: Changing code, failing commands, requested edits and tool errors.
- Decisive decision or feedback right: Select files/commands/edits, observe first-party tool results and determine the next coding action.
- Decision owner: Main model-driven HashCoder agent.
- Supporting / enforcement mechanisms: Native Tauri/Rust tool adapters, permission gates, model routing, session persistence, project scope and diff/undo.
- Closure path: User task -> model-chosen coding tool -> first-party handler and tool feedback -> new model choice or final result.
- Boundary reachability: HashCoder's shipped code mode calls its native agentLoop and Tauri tool definitions on a real opened project.
- Why this is / is not agent-owned: The model chooses actions; the program executes and records those choices.
- Evidence: [mode.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js); [hashcoder.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/platform/tauri/hashcoder.js); [agent-policy.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/agent-policy.js)
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Inference comes from configured external models; permissions and human approval can constrain actions..


## S2 — Coordination

- State: —
- Function: No established first-party inter-S1 regulation inside the HashCoder coding runtime.
- Disturbance / variety regulated: A single coding agent and its tool batch do not form distinct operational units in conflict.
- Decisive decision or feedback right: No S2-specific choice.
- Decision owner: No S2 decision owner established.
- Supporting / enforcement mechanisms: Concurrent read batching, sequential writes, session and UI state.
- Closure path: Tools are grouped and executed for the same operational agent, not corrective coordination among independent S1 cells.
- Why this is / is not agent-owned: Parallel read tools and sequential writes only implement one agent's tool ordering; the separate Swarm workspace is excluded.
- Evidence: [agent-policy.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/agent-policy.js); [mode.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js); [graph.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/swarm/graph.js); [ARCHITECTURE.md](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/docs/ARCHITECTURE.md)
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Sibling Swarm team design is an adjacent system and cannot donate its decisions to HashCoder..

### Absence scope

- Surfaces inspected: HashCoder loop/policy, built-in tools, Tauri bridge, and distinct Swarm graph/workspace code.
- Plausible first-party paths checked: Tool read batching, write sequencing, project state, model routing, Swarm graph.
- Why no material first-party path remains: No two distinct credited HashCoder S1 cells plus concrete inter-cell interference and feedback-adjustment were demonstrated; Swarm is separately instantiated.


## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-system current management over multiple coding operational units.
- Disturbance / variety regulated: Iteration stalls, limits and tool permission issues are local operating disturbances.
- Decisive decision or feedback right: None for organizational resource/commitment authority above one coding S1.
- Decision owner: No qualifying S3 owner.
- Supporting / enforcement mechanisms: Stall detector, step budgets, runtime gate, provider fallback, status and trace.
- Closure path: Stalled or unproven work is returned to the same coding agent or stopped; no whole-current cross-unit regulation.
- Why this is / is not agent-owned: Deterministic current action limits are enforcement mechanisms, not a metasystem choosing shared unit priorities.
- Evidence: [agent-policy.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/agent-policy.js); [mode.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js); [verify.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/code/verify.js)
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: These protections may improve performance/safety but do not establish organizational S3..

### Absence scope

- Surfaces inspected: Code agent loop, stop/iteration policy, model router, proof checker, Tauri sandbox.
- Plausible first-party paths checked: Retry, test-after-edit, concurrency cap and branch/workspace switching.
- Why no material first-party path remains: No source-wired multi-S1 whole-current view and discretionary decision over shared commitments, resources or priorities at HashCoder recursion.


## S3* — Complementary audit

- State: —
- Function: No sufficiently independent audit role with complementary evidence access and corrective organizational return.
- Disturbance / variety regulated: A coding agent may prematurely claim correct changes.
- Decisive decision or feedback right: Proof tracker evaluates recorded test commands and deterministic send-back conditions, not independent review judgment.
- Decision owner: Main agent retains correction ownership; proof checker applies static record checks.
- Supporting / enforcement mechanisms: Project test command discovery, proofLog, change timestamps and bounded completion prompts.
- Closure path: Recorded same-loop tool output -> deterministic nudge -> same model executes or answers; no separate auditor.
- Why this is / is not agent-owned: The evidence is generated from ordinary agent operations; separate audit access/owner is missing.
- Evidence: [verify.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/code/verify.js); [mode.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js); [agent-policy.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/js/agent-policy.js)
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Proof log can honestly describe which tests ran, without becoming S3*..

### Absence scope

- Surfaces inspected: ProofLog and sendBack, main loop, test/shell tool result recording, project-check discovery.
- Plausible first-party paths checked: Test-after-edit classification, small-model self-review, retry nudges and user diff approval.
- Why no material first-party path remains: The same agent is sent back to continue. No independent complementary source inspection and audit judgment path followed by function-specific corrective return is implemented.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective external-environment adaptation loop in the credited HashCoder mode.
- Disturbance / variety regulated: Future capability demands and external changes are not explicitly converted into adaptation options.
- Decisive decision or feedback right: No evidenced S4 capability renewal right.
- Decision owner: No S4 agent, constructor or parent owner.
- Supporting / enforcement mechanisms: Automatic user-fact extraction, memory recall, model choice, persisted state and tools.
- Closure path: Facts may affect later prompts but no prospective environmental intelligence decision changes the current operating organization.
- Why this is / is not agent-owned: Context retention and provider fallback are not prospective organizational adaptation.
- Evidence: [store.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/core/memory/store.js); [mode.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/modes/code/mode.js); [ARCHITECTURE.md](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/docs/ARCHITECTURE.md)
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: Other desktop workspaces are separately scoped and cannot close S4 here..

### Absence scope

- Surfaces inspected: Shared memory store and HashCoder call sites, model router, sessions, runtime tool list.
- Plausible first-party paths checked: Auto fact extraction, remembered preferences, later recall and provider switching.
- Why no material first-party path remains: No source-native external-prospective distinction, generated adaptation option, authoritative decision and return into changed HashCoder capability is established.


## S5 — Policy and identity

- State: —
- Function: No first-party organizational identity or ultimate-policy governance loop.
- Disturbance / variety regulated: Tool permission/safety choices concern individual operations.
- Decisive decision or feedback right: No ultimate-policy decision right at the selected recursion.
- Decision owner: Human grants individual permissions; deterministic rules enforce.
- Supporting / enforcement mechanisms: Permission Guard, Rust deny list, user action dialog, diff Keep/Undo, audit log.
- Closure path: User approves or denies an operation, without a binding identity/ultimate-policy decision loop returned to the organization.
- Why this is / is not agent-owned: Command authorization and selected model are not S5-level ultimate purpose.
- Evidence: [hashcoder.js](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src/platform/tauri/hashcoder.js); [agent_sandbox.rs](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/src-tauri/src/security/agent_sandbox.rs); [SECURITY.md](https://github.com/Hash-7777/HashCortX/blob/ab3fb74a61928dfb98985eac5ec3eeac8c85afe7/docs/SECURITY.md)
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Runtime control is not inherited from broader OSS development governance..

### Absence scope

- Surfaces inspected: HashCoder permission UI, Rust security sandbox, project root scope and user configuration.
- Plausible first-party paths checked: Tool approval, denial, undo, system prompt and model settings.
- Why no material first-party path remains: No ultimate-policy/identity issue routed through legitimate authority and closed into subsequent governing organizational behavior exists in the reviewed runtime.

## Distributed OSS parent arrangement

Public maintainers, contributors, CI and release organization do not own VSM decisions inside an installed user HashCoder coding session. User permission prompts are action-level authority, not automatic S3/S4/S5 parent modes.

## Self-hosted and non-human modes

Local and cloud model endpoints use the same first-party coding/tool mechanism. Human approvals constrain file and shell actions, while the primary model exercises task-level S1 discretion. No first-party parent-governed higher function is assumed from user control.

## Recursion

One first-party coder operating on one user's project is the focal system-in-focus. The separate Agent Swarm workspace has an independent purpose and does not automatically constitute internal lower-recursion S1 cells of HashCoder. Tool batching is not S2.

## Variety and escalation

Returned command/test results and denied tool calls alter the next model step. The local progress/proof guards can nudge the same model or stop its task. This is operational feedback, not organizationally independent higher-level audit or ultimate-policy governance.

## Evidence gaps

- The system boundary is HashCoder only: no claims about Agent Swarm's separate organizational topology.
- Proof-after-edit checks do not establish independent S3*; no benchmark accuracy or runtime reliability claim follows from this assessment.
- Retained local user facts and manual model/provider changes do not establish future-facing S4 capability governance.
