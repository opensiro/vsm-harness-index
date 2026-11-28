---
harness_id: towa
project_name: towa
repository: https://github.com/gfx-labs/towa
review_ref: 831b8cdf063d904fde4c8dab4a2856dfbde1c90d
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# towa

## Review boundary

- System in focus: One running towa coding session and optional child runs created by it.
- Purpose and identity: Carry out an ACP prompt through model-selected coding operations and report a result.
- Relevant environment: ACP client, user workspace, configured model services and optional MCP/tool dependencies.
- Standard-distribution boundary: Shipped Go binary, native turn and tool loop, storage, supported config and ACP endpoints.
- Credited operating / distribution surfaces: Session, optional child model runs, tool scheduler, configured hook and session log surfaces.
- Adjacent first-party surfaces excluded from ownership: Client UI and external schedulers, provider and MCP implementations, repository tests and release infrastructure.
- First-party operating / deployment modes considered: ACP over stdio or sockets, with selectable child depth, hooks and history access.
- Recursion level: One parent coding session with the optional full child operating loops it starts.
- Reviewed revision: 831b8cdf063d904fde4c8dab4a2856dfbde1c90d
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

An ACP prompt resolves a session and runs the native turn loop. The loop receives a provider response, dispatches tools through effect and permission checks, stores results and emits progress to the client. Optional child agents run through the same loop with their own prompts and session IDs. Client messages, modes and operator config supply constraints.

## Operational model

The model owns coding-tool choice and completion. When distributed work is desired it chooses task text, model and the order of child calls. A child runs to a result under the supplied working directory and permission context. Configuration limits bound admission and future calls.

## S1 — Operations

- State: A
- Function: Resolve a coding request through native model-directed operations.
- Disturbance / variety regulated: Changing workspace evidence, provider responses and failed tool attempts.
- Decisive decision or feedback right: Choose a tool action, absorb the resulting evidence and decide what to return.
- Decision owner: The selected model in the native turn loop.
- Supporting / enforcement mechanisms: ACP input and updates, provider resolver, tool scheduler, permissions and transcript.
- Closure path: Tool results return to the native loop. End-turn response and emitted content return to the client.
- Why this is / is not agent-owned: The shipped model/runtime pairing performs tactical choices and feedback without a developer-provided task loop.
- Boundary reachability: Standard ACP Prompt invokes the repository's own Run loop.
- Evidence: [src/agent/session/prompt.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/prompt.go#L35-L105), [src/agent/loop/turn.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/loop/turn.go#L301-L345), [src/agent/loop/turn.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/loop/turn.go#L540-L572), [src/cli/runtime.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/cli/runtime.go#L271-L305)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: Provider selection and configured permissions can constrain action availability.

## S2 — Coordination

- State: A
- Function: Order potentially interfering operations from distinct child agent loops within one parent turn.
- Disturbance / variety regulated: Child calls inherit the same working directory. Starting both before either completes would permit overlapping side effects.
- Decisive decision or feedback right: The parent model selects child calls and specifies the precedence of conflicting siblings through the order of those calls.
- Decision owner: The parent model that supplies the ordered calls.
- Supporting / enforcement mechanisms: Child calls carry an exclusive execution effect. The conflict scheduler makes later exclusive calls wait and returns all results.
- Closure path: Later children start after earlier sibling calls finish, with their access to the common workspace ordered by the chosen precedence. Results are available for the parent's next decision.
- Why this is / is not agent-owned: The model determines the work order. The runtime supplies the independent-child conflict guard.
- Boundary reachability: The shipped runtime registers the child tool when child depth is enabled and routes it through the ordinary conflict-aware dispatcher.
- Distinct S1 units: Two child agents with distinct session IDs, local model/tool loops and separate task prompts.
- Inter-S1 disturbance: Each child can act on the same working directory, including writes whose paths are unknown before its run.
- Attenuating coordination relation: The parent selects precedence and the scheduler uses the exclusive execution marker to prevent overlap.
- Feedback into subsequent S1 behaviour: Only after the prior child returns does the later operation gain access to the workspace. Both returns inform subsequent action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This scheduler explicitly prevents concurrency among conflicting execution calls. The child operations are full model-driven loops.
- Evidence: [src/agent/extras/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/subagent.go#L22-L35), [src/agent/extras/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/subagent.go#L62-L87), [src/agent/subagent/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/subagent/subagent.go#L213-L231), [src/agent/loop/dispatch.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/loop/dispatch.go#L198-L249), [src/tools/schedule.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/tools/schedule.go#L17-L60), [src/cli/runtime.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/cli/runtime.go#L648-L660)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: This witness holds within the same parent dispatch. Independent top-level ACP sessions have no established cross-session workspace arbiter.

## S3 — Inside-and-now control

- State: —
- Function: Whole-session supervision of live operational commitments was sought.
- Disturbance / variety regulated: Child work can be late, redundant or unsuitable.
- Decisive decision or feedback right: No supplied actor was found able to use a whole-current view to rebalance live child commitments.
- Decision owner: The caller governs its prompt and permissions. The model selects subordinate work at launch.
- Supporting / enforcement mechanisms: Process-level child cap, transcript, prompt cancel, session close and usage accounting.
- Closure path: Launch and results apply to an individual child call. Cancellation interrupts a parent turn and its children.
- Why this is / is not agent-owned: Child task decomposition and hard caps constrain operation. There is no supplied live role/commitment portfolio and feedback-driven reallocating decision.
- Evidence: [src/agent/subagent/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/subagent/subagent.go#L179-L231), [src/agent/extras/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/subagent.go#L62-L94), [src/agent/session/prompt.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/prompt.go#L145-L163), [src/agent/session/lifecycle.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/lifecycle.go#L12-L49)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: An external ACP client may implement its own cross-session orchestration.

### Absence scope

- Surfaces inspected: Child result and usage, session lifecycle, model options, ACP notifications and external cancel.
- Plausible first-party paths checked: An autonomous or attended control loop that sees current inter-unit commitments and applies a substantive reallocation.
- Why no material first-party path remains: The shipped child call returns only after completion. User cancellation or configuration changes apply to a session without the required binding between whole-current view and discretionary resource or commitment change.

## S3* — Complementary audit

- State: —
- Function: A complementary check of a child or whole-session operational claim was sought.
- Disturbance / variety regulated: A child report may omit a failed action or contradict recorded tool output.
- Decisive decision or feedback right: No native audit-specific trigger, judgment and corrective return were established.
- Decision owner: The parent model receives child results. A developer may configure separate scripts.
- Supporting / enforcement mechanisms: Optional descendant transcript search, ordinary result visibility and general event hooks.
- Closure path: Transcript entries can be retrieved. An externally authored stop hook may return a reason and keep the same turn open.
- Why this is / is not agent-owned: The supplied search helps with history recovery. The generic hook cannot choose an audit claim or guarantee an independent evidence-judgment path.
- Evidence: [src/agent/extras/subagent.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/subagent.go#L78-L102), [src/agent/extras/convsearch.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/convsearch.go#L22-L34), [src/agent/extras/convsearch.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/convsearch.go#L54-L97), [src/agent/hooks/hooks.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/hooks/hooks.go#L1-L39), [src/agent/loop/turn.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/loop/turn.go#L442-L463)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Scoped transcript reads offer raw rather than summarized material. Whether they become an audit depends on an additional mandate, judgment and corrective use.

### Absence scope

- Surfaces inspected: Child reporting, configured transcript search, raw turn reads, stop and post-tool hook contracts.
- Plausible first-party paths checked: A shipped complementary inspection of a named operational claim with findings returned to a control decision.
- Why no material first-party path remains: The shipped search has no complementary review path wired to a named claim. Configurable hooks leave the audit actor, evidence and judgment to externally supplied code.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective adaptation of session capabilities or tools was sought.
- Disturbance / variety regulated: Future coding tasks may require changes to models or tool knowledge.
- Decisive decision or feedback right: No supplied outside-to-future feedback owner was identified.
- Decision owner: The operator supplies configuration and available skills. The active model loads relevant instructions for its task.
- Supporting / enforcement mechanisms: Context preload, skill retrieval, provider routing, reload and stored conversation.
- Closure path: The new externally supplied configuration applies to later turns. Skill retrieval affects the present model context.
- Why this is / is not agent-owned: The loader and reload apply inputs. No installed path chooses an adaptation from an external change signal and admits it into future capability.
- Evidence: [README.md](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/README.md#L43-L54), [src/agent/extras/skill.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/skill.go#L20-L36), [src/agent/extras/skill.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/extras/skill.go#L46-L66), [src/agent/session/host.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/host.go#L138-L150), [src/cli/runtime.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/cli/runtime.go#L336-L357)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The configured extension surfaces allow operator-managed customization.

### Absence scope

- Surfaces inspected: Skill selection, context compaction and history, provider resolution and framework reload.
- Plausible first-party paths checked: A native model or authorized operator mode that interprets external change, proposes a durable adaptation and feeds a selected capability back into future work.
- Why no material first-party path remains: The shipped paths retrieve instructions, enforce configured models or reload externally edited configuration. The coordinated adaptation decision and return are absent.

## S5 — Policy and identity

- State: —
- Function: Settle an ultimate-policy or identity dispute for the session.
- Disturbance / variety regulated: Tool requests can exceed permission mode or operator configuration.
- Decisive decision or feedback right: No supplied adjudicator resolves that conflict at the identity or ultimate-policy level.
- Decision owner: The operator or caller supplies operating parameters and some action decisions.
- Supporting / enforcement mechanisms: ACP permission requests, mode controls, hook rules and configuration.
- Closure path: A decision allows or denies a particular tool operation or applies configured mode.
- Why this is / is not agent-owned: Permission ownership is scoped to the operation. The documented ACP protocol does not supply governing policy adjudication.
- Evidence: [src/agent/session/permission.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/permission.go#L29-L78), [src/agent/session/registry.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/registry.go#L438-L466), [src/agent/session/prompt.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/session/prompt.go#L76-L104), [src/agent/hooks/hooks.go](https://github.com/gfx-labs/towa/blob/831b8cdf063d904fde4c8dab4a2856dfbde1c90d/src/agent/hooks/hooks.go#L17-L39)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The repository's maintainer process is outside this ACP session.

### Absence scope

- Surfaces inspected: Permission gate, mode registry, operator/client configuration and prompt/stop hook contracts.
- Plausible first-party paths checked: An autonomous or parent issue-to-ultimate-authority loop that sets and returns a governing policy decision.
- Why no material first-party path remains: Available authority governs task permissions and configuration. No supported route closes a change of organizational purpose or ultimate policy.

## Recursion

Child sessions run their own native operational loops within the same parent's task. The socket server can host other top-level sessions, which remain outside the selected parent-child recursion.

## Variety and escalation

Permissions and per-turn limits constrain tool actions. The dispatcher orders incompatible jobs and returns outcomes to the model. Hooks can stop a call or extend its turn under predefined rules.

## Evidence gaps

Static read of the pinned source. No clients, providers, concurrent child runs, workspace writes or hooks were executed.
