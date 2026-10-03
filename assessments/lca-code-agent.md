---
harness_id: lca-code-agent
project_name: LCA Code Agent
repository: https://github.com/Kandog/lca-code-agent
review_ref: 3049426ad46a0a4eab2ed896a8f87160f76689e4
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# LCA Code Agent

## Review boundary

- System in focus: the first-party LCA Code Agent VS Code extension at frozen revision `3049426ad46a0a4eab2ed896a8f87160f76689e4`, including its model/tool feedback loop, project-root file tools, command execution, Plan/Act mode, approval flow, sessions, skills, MCP adapter, project `AGENTS.md` instructions and VS Code UI surfaces where they affect organizational ownership.
- Purpose and identity: operate as a self-hosted autonomous coding assistant inside one local project, planning and executing file/command changes, validating results, iterating on tool feedback, and remaining governed by durable project-wide instructions supplied by the project owner/team.
- Relevant environment: user requests and approvals, local repository/filesystem state, command/build/test results, configured model endpoint responses, optional local MCP tools, saved sessions, project `AGENTS.md`, setup configuration and VS Code workspace state.
- Standard-distribution boundary: shipped VS Code extension runtime and documented built-in tools/UI/session/project-memory paths are inside. Model-provider internals, external MCP server implementations, target-project CI/governance and repository-development tests/builds are dependencies or adjacent surfaces rather than credited owners.
- Credited operating / distribution surfaces: `README.md`; `src/agentLoop.ts`; `src/tools.ts`; `src/ChatViewProvider.ts`; `src/projectMemory.ts`; `src/sessionManager.ts`; built-in setup/approval and project-memory UI paths reached from the extension.
- Adjacent first-party surfaces excluded from ownership: extension CI/release workflows; packaged VSIX artifacts as distribution evidence only; development tests; external MCP servers and their internal policies; provider/model services; target-project human governance outside the explicit `AGENTS.md` return path.
- First-party operating / deployment modes considered: ordinary Act-mode coding turn; Plan mode; autoApprove on/off; network-warning approval; saved/resumed sessions; user-authored skills; project `AGENTS.md`; MCP-enabled operation; tools-disabled chat.
- Recursion level: one LCA coding assistant operating on one project is the operational organization. Its model/tool loop is the S1. The legitimate project owner/team is treated as a parent recursion only for the durable project-policy path through `AGENTS.md`.
- Reviewed revision: `3049426ad46a0a4eab2ed896a8f87160f76689e4`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

LCA Code Agent ships a single iterative model/tool coding loop in `src/agentLoop.ts`. On each turn the model receives the current history, system policy and available tools, may request file or command actions, receives actual tool results back into the history, and continues until it returns a final response or the configured step ceiling pauses the turn. The built-in surface includes project-root file listing/reading/writing/replacement/deletion, shell command execution and a model-visible plan checklist; configured MCP tools can be added through the same call path.

Plan mode removes mutating tools from the model-visible set and also rejects hallucinated mutation calls. Act mode exposes the normal tool surface. File/command mutations can require parent approval, and network-shaped shell commands always require explicit approval. These are operational authorization/enforcement mechanisms around the same S1 loop; they do not by themselves establish S3 or S5.

LCA does not ship a child-agent or multi-agent organization at the reviewed revision. No first-party subagent roster, delegated worker lifecycle, worktree fleet, sibling coordination or independent reviewer actor was found. The Plan → Edit → Run → Validate → Iterate workflow is executed by the same operational model through its ordinary tool/result path.

The durable project-policy surface is `AGENTS.md`. `projectMemory.ts` defines it as project-wide instructions for AI coding agents, deliberately located at the project root so it can be committed, shared and edited by the project. `ChatViewProvider.ts` reads it when a new chat builds its initial system message and inserts its contents under `## Project instructions`. A new chat therefore reloads owner/team changes and makes them governing system-level context for subsequent LCA operation.

## Operational model

A user request enters one LCA conversation. The model decides which project action or evidence request to make; the extension executes or blocks the tool, returns the observed result and asks the same model to continue. For non-trivial work the system prompt asks the model to plan, edit, execute build/test/lint checks, inspect whether they passed and iterate after failures.

Human approvals may authorize or deny particular current operations, but they remain local operational supervision. The stronger parent-governed claim is limited to durable project policy: the legitimate project owner/team authors `AGENTS.md`, and first-party system-message construction automatically returns that standing policy to each new chat.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by interpreting a project task, inspecting repository state, choosing file/command actions, executing them, observing results and iterating until a supported result is reached.
- Disturbance / variety regulated: heterogeneous project structures, incomplete requirements, file contents, command/build/test failures, malformed tool calls, platform differences, model/provider responses and implementation alternatives.
- Decisive decision or feedback right: choose which available project action to invoke next, what change to make, what validation command/evidence to inspect and how to revise work after returned results.
- Decision owner: the configured model-backed LCA coding actor.
- Supporting / enforcement mechanisms: tool registry; project-root path guard; provider adapters; Plan/Act filtering; approval UI; network-command heuristic; step ceiling; session persistence; MCP adapter.
- Closure path: user task + current project/system context → model chooses tool/action → first-party extension executes, denies or obtains approval → tool result returns to history → the same model changes subsequent action or emits the final response.
- Boundary reachability: ordinary installed VS Code operation directly invokes `runAgentTurn` with the shipped built-in tool set; no consumer-authored agent loop is required.
- Why this is / is not agent-owned: deterministic code executes and constrains actions, but the model owns open-ended task-specific choices and interpretation of returned evidence.
- Evidence: [`README.md`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/README.md); [`src/agentLoop.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/agentLoop.ts); [`src/tools.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/tools.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference is external; the credited S1 is LCA's first-party role/tool/result composition.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function was established at the assessed recursion.
- Disturbance / variety regulated: the review looked for interference among multiple distinct operational S1 units, not ordinary tool ordering or a single model's plan steps.
- Decisive decision or feedback right: no qualifying coordination right exists because the frozen standard runtime does not establish multiple first-party coding-agent S1 units whose interaction creates an inter-S1 disturbance.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential tool-call handling, project-root sandboxing, approvals, Plan mode and MCP routing can constrain one actor's execution but do not coordinate distinct S1 units.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation relation → changed subsequent S1 behavior loop is supplied.
- Why this is / is not agent-owned: the model can sequence multiple actions, but sequencing actions inside one S1 is not S2 coordination.
- Evidence: [`src/agentLoop.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/agentLoop.ts); [`README.md`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: configured MCP tools may themselves encapsulate other systems, but LCA does not package those external implementations as first-party coordinated S1 peers.

### Absence scope

- Surfaces inspected: core agent loop; built-in tools; Plan/Act mode; MCP integration; sessions; skills; project memory; command/file sandbox.
- Plausible first-party paths checked: subagent spawning, parallel worker execution, worktree/file ownership, cross-agent locks, dependency coordination, shared task boards, sibling messaging and merge arbitration.
- Why no material first-party path remains: the frozen repository exposes one model/tool loop and no first-party multi-agent worker organization or concrete inter-S1 conflict-attenuation path.

## S3 — Inside-and-now control

- State: —
- Function: no material distinct whole-system current-control function was established above the single LCA operational loop.
- Disturbance / variety regulated: Plan mode, approvals and step limits constrain current work, but no separate whole-system controller regulates a portfolio of multiple S1 commitments/resources at the assessed recursion.
- Decisive decision or feedback right: no qualifying whole-system current-control decision was established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Plan/Act toggle; per-call approval; network-warning approval; max-agent-step pause; setup configuration; progress indicator.
- Closure path: not applicable; located controls gate or bound one S1's actions rather than observe and regulate multiple current operational commitments on behalf of the whole.
- Why this is / is not agent-owned: planning and self-correction are ordinary S1 task regulation, while parent Approve/Deny is a local action authorization rather than a whole-system S3 mode.
- Evidence: [`src/agentLoop.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/agentLoop.ts); [`src/ChatViewProvider.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/ChatViewProvider.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human approval is operationally important but does not satisfy the Methodology's whole-system-view/current-control threshold.

### Absence scope

- Surfaces inspected: plan tracking; Plan/Act mode; approvals; progress/busy state; step ceiling; session controls; configuration; MCP lifecycle.
- Plausible first-party paths checked: whole-fleet roster, dynamic resource allocation, commitment reprioritization, autonomous manager role, parent whole-system dashboard/intervention and run-wide budget/accountability control.
- Why no material first-party path remains: only one coding S1 is established and the located controls govern individual actions/session lifecycle rather than a multi-operation whole.

## S3* — Complementary audit

- State: —
- Function: no material complementary independent audit loop was established inside the standard runtime.
- Disturbance / variety regulated: the same operational model is instructed to run builds/tests/lints and inspect results before completion, but no separate auditor independently checks the operational actor's claim through a complementary access path.
- Decisive decision or feedback right: no separate audit judgment owner is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: execute-command validation, plan status, approval diff preview, logs and development tests provide evidence/inspection without a distinct runtime audit organization.
- Closure path: not applicable; ordinary S1 validation results return to the same model rather than an independent reviewer whose findings force corrective operation.
- Why this is / is not agent-owned: the agent's own test/run feedback is part of S1 self-regulation; a separate reviewer/verifier actor or complementary adjudication path is absent.
- Evidence: [`README.md`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/README.md); [`src/agentLoop.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/agentLoop.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: VS Code diff preview gives the human direct pre-write visibility, but a per-action approval preview is not an independent audit of the completed S1 claim.

### Absence scope

- Surfaces inspected: Plan → Edit → Run → Validate → Iterate path; diff preview/approval; tool results; logs; session history; repository tests/build configuration.
- Plausible first-party paths checked: independent reviewer agent, isolated verifier, post-change semantic critic, read-only audit role, mandatory external test adjudicator and corrective audit feedback.
- Why no material first-party path remains: all runtime validation evidence is consumed by the same operational model or by ordinary parent approval; no complementary independent audit judgment and corrective return loop is packaged.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective organizational adaptation loop was established at the selected recursion.
- Disturbance / variety regulated: sessions, project instructions and user-authored skills preserve useful context, but no first-party actor converts external/future distinctions into newly selected persistent capability changes.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: saved sessions; project `AGENTS.md`; user-authored prompt skills; configurable MCP servers; setup/provider changes.
- Closure path: not applicable; no outside/future sensing → adaptation option → persistent capability/strategy change → return into current operation loop was found.
- Why this is / is not agent-owned: persisted context and reusable user-authored snippets can affect future work, but persistence/configuration is not itself S4 intelligence/adaptation.
- Evidence: [`README.md`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/README.md); [`src/projectMemory.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/projectMemory.ts); [`src/ChatViewProvider.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/ChatViewProvider.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a project owner can manually evolve AGENTS.md/skills/MCP configuration; that parent configuration activity is not a packaged S4 loop.

### Absence scope

- Surfaces inspected: project memory; saved sessions; skills; setup/provider configuration; MCP tools; model validation loop; Plan mode.
- Plausible first-party paths checked: autonomous skill creation/promotion, reflection-to-future-guidance, external research/forecasting, model/tool upgrade selection, persistent learned policy/capability changes and scheduled adaptation.
- Why no material first-party path remains: the located cross-session surfaces are explicitly user/project authored or ordinary history/configuration; no first-party prospective adaptation owner selects and returns a capability change.

## S5 — Policy and identity

- State: P
- Function: apply the legitimate project owner's durable project-wide standing instructions and conventions as governing policy for later LCA coding sessions in that repository.
- Disturbance / variety regulated: new coding sessions can drift from repository architecture, coding conventions, required build/test practice and other standing project rules unless authoritative project instructions are returned into each fresh agent context.
- Decisive decision or feedback right: decide the durable contents of project-root `AGENTS.md`, which the first-party runtime labels project instructions and places into new-chat system context.
- Decision owner: the human/project owner or legitimate project team at the parent recursion. LCA provides an editor/open command and automatic loading but no autonomous authority to redefine ultimate project policy.
- Supporting / enforcement mechanisms: `ensureProjectMemoryTemplate`; root `AGENTS.md`; VS Code “Open Project Memory” command; `readProjectMemory`; `buildSystemMessage`; fresh-chat history initialization.
- Closure path: project owner/team identifies or changes a standing repository instruction/convention → edits committed/shared `AGENTS.md` → next LCA chat reads the file fresh → `buildSystemMessage` inserts it under `## Project instructions` → subsequent S1 model operation is governed by that returned parent policy.
- Boundary reachability: `AGENTS.md` support and its VS Code open/create command are shipped first-party paths, and the file is automatically read by the normal new-chat startup path.
- Why this is / is not agent-owned: the model receives and follows the standing policy but does not own the authoritative right to define it; ultimate authority stays with the legitimate project parent.
- Evidence: [`src/projectMemory.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/projectMemory.ts); [`src/ChatViewProvider.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/ChatViewProvider.ts); [`src/extension.ts`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/src/extension.ts); [`README.md`](https://github.com/Kandog/lca-code-agent/blob/3049426ad46a0a4eab2ed896a8f87160f76689e4/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: per-tool approval, Plan/Act mode and setup.json are not used as the S5 witness; the positive parent mode is specifically the durable project-policy `AGENTS.md` return path.
- Identity / ultimate-policy issue: which project-wide conventions, architecture rules, build/test requirements and standing instructions should govern AI coding behavior in this repository.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/team authors and revises `AGENTS.md`; no first-party autonomous S5 authoring mode is established.
- Return-to-operation path: project-root `AGENTS.md` → `readProjectMemory` at fresh chat startup → `buildSystemMessage` system-role “Project instructions” → later model/tool decisions operate under the returned standing rules.

## Distributed OSS parent arrangement

For a shared repository, multiple contributors may edit the project-wide `AGENTS.md` through normal project governance. This assessment credits S5 only at the local project recursion where the file is the authoritative standing-instruction surface consumed by LCA. It does not infer organization-wide governance merely from the existence of contributors.

## Self-hosted and non-human modes

LCA is self-hosted, but generic setup changes, Plan/Act selection and per-action approvals are not promoted to parent-mode VSM functions. The one parent mode credited is the function-specific project-policy closure through `AGENTS.md`.

## Recursion

The system-in-focus is one LCA coding assistant serving one project. Its model/tool loop is S1. There are no first-party sibling S1 agents or metasystem actors at this frozen revision. The project owner/team sits at the parent recursion for durable standing project policy.

## Variety and escalation

LCA absorbs task variety through model/tool iteration, platform-aware command execution, Plan mode, validation commands, MCP extension and user feedback. Mutating or network-shaped actions can escalate to human approval. Those action approvals remain operational safeguards; durable project policy returns separately through `AGENTS.md`.

## Evidence gaps

The frozen source strongly establishes S1 and the parent project-policy return path. Negative S2/S3/S3*/S4 findings are supported by the narrow single-agent architecture and inspection of plan, validation, sessions, skills, project-memory and MCP surfaces. External MCP implementations are intentionally not imported as first-party organizational owners.
