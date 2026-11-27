---
harness_id: vesper
project_name: Vesper
repository: https://github.com/Kernel-Hunter/vesper
review_ref: 82454abe5225a54101944bf6905dfefbc0000819
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Vesper

## Review boundary

- System in focus: Installed Vesper coding assistant, including concurrent desktop coding chats.
- Purpose and identity: Carry out and inspect software work in operator-selected folders.
- Relevant environment: A developer workstation, local or remote inference, optional Git and approved tools/services.
- Standard-distribution boundary: Shipped Python terminal and desktop server, bundled web UI, workspace tools, Git integration and stored sessions.
- Credited operating / distribution surfaces: Vesper TUI and desktop agent sessions, model/Workspace code, optional Git worktrees, packaged UI and Telegram route.
- Adjacent first-party surfaces excluded from ownership: Maintainer roadmap and release CI, development tests, external providers, tools and language servers.
- First-party operating / deployment modes considered: Terminal, desktop/web chat and supported Telegram interaction, with the desktop's parallel sessions and opt-in worktrees examined separately.
- Recursion level: One Vesper installation. Distinct model sessions are concurrent operational cells when using the desktop.
- Reviewed revision: 82454abe5225a54101944bf6905dfefbc0000819
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Vesper builds a LangGraph agent around a prepared workspace and model. The same session layer streams tool activity, persists history, applies check and diagnostic feedback, and records files changed in a turn. In the desktop server a chat has its own session, root and lock. Optional worktrees and guarded merge organize concurrent edits to one repository.

## Operational model

A coding chat closes user-initiated work through model-chosen actions, returned tool observations, edits and a final answer. Desktop sessions carry independent conversations and can overlap. An operator may isolate a chat and bring it back through the distribution's guarded Git path. The user supplies permissions while the agent owns task-specific decisions.

## S1 — Operations

- State: A
- Function: Carry out model-directed coding or inspection work in a user-selected workspace and report its effects.
- Disturbance / variety regulated: Changing repository context, tool results, permission denial, check failures and provider availability.
- Decisive decision or feedback right: Select and revise workspace actions and decide the task response from observed results.
- Decision owner: The model running the installed Vesper session.
- Supporting / enforcement mechanisms: LangGraph agent construction, session storage, Workspace tools, approvals, diagnostics and configurable check middleware.
- Closure path: Tools return results to the running graph. Failed checks can add a new repair prompt to that graph. The session persists and streams its output or terminal outcome.
- Boundary reachability: The shipped desktop server constructs Workspace and Session on a chat request. The terminal drives the same coder and tool implementation. Both use first-party defaults and required model configuration.
- Why this is / is not agent-owned: The model drives work and repair inside tool permissions. Human input defines the goal or decides particular tool permissions.
- Evidence: [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L216-L220), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L531-L544), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L634-L672), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L1120-L1187), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L387-L450), [src/vesper/workspace.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/workspace.py#L699-L774)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Checks run only when configured and when the turn's edit and mode conditions apply.

## S2 — Coordination

- State: C
- Function: Attenuate filesystem interference among distinct concurrent coding chats working against a common Git checkout.
- Disturbance / variety regulated: One chat can edit files while another is working on, or trying to integrate with, the same checkout.
- Decisive decision or feedback right: Choose which chat gets a separate worktree, then choose when to request guarded reintegration.
- Decision owner: The operator composes the separated chat arrangement using the supplied worktree action. Git and server rules enforce it.
- Supporting / enforcement mechanisms: Chat-specific execution state, worktree branch creation, current-main busy detection, guarded merge and conflict feedback.
- Closure path: An opted-in chat's workspace root moves to its own worktree for subsequent agent actions. The return path refuses integration while another chat is active in main or when Git reports conflicts, otherwise moves the chat back after merging.
- Boundary reachability: The standard desktop Git API and terminal commands invoke checked-in worktree code. In desktop mode it checks other live chats before merging into the main checkout.
- Why this is / is not agent-owned: The implementation establishes a specific inter-chat coordination relation, but placement and reintegration require an operator's explicit decision.
- Distinct S1 units: Separately executing model-backed coding chats with their own task, workspace and history.
- Inter-S1 disturbance: Concurrent writes or integration against a shared main checkout.
- Attenuating coordination relation: Per-chat worktree relocation and a merge gate aware of other active chats in the main checkout.
- Feedback into subsequent S1 behaviour: Workspace-root change redirects future tool actions. A busy/conflicting return preserves the separate lane and asks for wait or resolution before integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The two paths explicitly isolate colliding writes and protect reintegration against another chat's active use. Neither depends on message transfer or task delegation alone.
- Evidence: [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L387-L450), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L716-L754), [src/vesper/gitnet.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/gitnet.py#L199-L235), [src/vesper/gitnet.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/gitnet.py#L272-L301), [docs/ROADMAP.md](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/docs/ROADMAP.md#L23-L26)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: This is opt-in and scoped to Git worktree operation. Parallel chats that share the ordinary checkout do not inherit this protection.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-system current-control arrangement is established.
- Disturbance / variety regulated: An operator can see multiple live chats and stop or steer a selected one.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Live sidebar, chat-specific queues, cancellation, approvals and guarded worktree merge.
- Closure path: A stop interrupts that session's work, and steering enters its next model step. Worktree operations change the selected chat's execution root.
- Why this is / is not agent-owned: The UI gives real per-chat current intervention and a cross-chat status view. The examined path does not decide and return a portfolio-wide allocation, obligation or priority across those work units.
- Evidence: [apps/web/src/packages/ui-layout/Sidebar.tsx](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/apps/web/src/packages/ui-layout/Sidebar.tsx#L157-L180), [apps/web/src/packages/store/store.ts](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/apps/web/src/packages/store/store.ts#L389-L418), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L605-L617), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L832-L835), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L599-L625)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Desktop session/sidebar status and controls, workspace and checkout coordination, provider global settings.
- Plausible first-party paths checked: Named work-unit steering, stopping as a parent action, and whether a current multi-chat obligation or resource decision is returned.
- Why no material first-party path remains: The runtime supplies local chat actions and a separate isolation mechanic. The visible state has no shared commitment or allocation model on which a whole-current decision operates.

## S3* — Complementary audit

- State: —
- Function: No complementary audit of organizational current control is established.
- Disturbance / variety regulated: Code edits can be faulty and regular chat reports may miss changes.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Per-chat diffs against captured baselines, external diagnostics and optional project checks.
- Closure path: An operator can inspect/revert changed files or feed review comments back. A configured check can return failure to the same coding loop.
- Why this is / is not agent-owned: The direct file view and checks substantively verify the task product, but the checked claim is local file/turn output and there is no distinct organizational controller or complementary audit return.
- Evidence: [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L634-L672), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L831-L876), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L756-L771), [docs/ROADMAP.md](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/docs/ROADMAP.md#L33-L35)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Project checks and diagnostics, baseline diff view, desktop comment/revert and repository CI.
- Plausible first-party paths checked: Independent acceptance of a management representation, evidence path and corrective return.
- Why no material first-party path remains: Repository facts are exposed for case-local verification. No separate organizational manager's representation or corrective authority is in the supplied path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then capability regulation is established.
- Disturbance / variety regulated: Provider credit, request load, and the project's instructions and available MCP tools can change.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Opt-in fallback order, per-session context compaction, operator config and project/skill discovery.
- Closure path: The current chat can resume on a fallback model or use changed startup configuration.
- Why this is / is not agent-owned: These support present operation or select user-supplied configuration. The installed product does not generate prospective capability options and route an adopted environmental adaptation into operation.
- Evidence: [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L818-L830), [src/vesper/coder.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/coder.py#L924-L965), [src/vesper/commands.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/commands.py#L125-L150), [docs/ROADMAP.md](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/docs/ROADMAP.md#L29-L37)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Provider switch, project instruction loading, MCP settings, local history and roadmap.
- Plausible first-party paths checked: Prospective autonomous or operator adoption of capability options, including provider fallback and MCP extension points.
- Why no material first-party path remains: The provided paths contain reactive model selection and manual tool setup. No future environmental model-to-adoption feedback exists in the inspected product.

## S5 — Policy and identity

- State: —
- Function: No ultimate policy or identity settlement is evidenced.
- Disturbance / variety regulated: Local users can set tool permission rules and project operating instructions.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Persistent allowlists, prompts assembled from working directory, agent mode and shell/tool constraints.
- Closure path: Allowed actions or steering change subsequent local tool conduct.
- Why this is / is not agent-owned: These decisions configure which actions the coding assistant may take. They do not settle the assistant's ultimate purpose or the authority to arbitrate an identity/policy conflict.
- Evidence: [src/vesper/permissions.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/permissions.py#L87-L136), [src/vesper/prompts.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/prompts.py#L100-L155), [src/vesper/server.py](https://github.com/Kernel-Hunter/vesper/blob/82454abe5225a54101944bf6905dfefbc0000819/src/vesper/server.py#L396-L425)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Permission stores, model and mode config, project instruction and skill loading.
- Plausible first-party paths checked: Owner authority over persistent constraints, user consent and runtime authority conflicts.
- Why no material first-party path remains: Actions and limitations are applied inside a fixed coding-assistant identity. There is no first-party ultimate-policy issue-to-decision loop.

## Recursion

The declared operating recursion is the installation. Individual chats execute bounded work with separate contexts. Future subagents in the roadmap and the organization developing Vesper are outside the installed operating boundary.

## Variety and escalation

The tool and provider paths return permission, execution and service errors into the active session. The desktop supports stopping or steering one chat, while worktree contention returns a discrete refusal. No independent algedonic escalation was established.

## Evidence gaps

Pinned public source inspection only. No provider calls, UI executions or real Git workspace merges were performed for this assessment.
