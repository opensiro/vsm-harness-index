---
harness_id: mare
project_name: mare
repository: https://github.com/signalridge/mare
review_ref: d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# mare

## Review boundary

- System in focus: The installed mare coding harness and its built-in plugin presets, one root session and its attributed child work.
- Purpose and identity: Execute user-directed repository work using a replaceable but supplied model/tool loop.
- Relevant environment: Working tree, operator, providers, external plugin catalogues and local sessions.
- Standard-distribution boundary: Rust host/kernel plus supplied Lua agent, tool, subagent, review and package plugins.
- Credited operating / distribution surfaces: Interactive and headless first-party loop, supported child lifecycle, read-only reviewer, trust/permission and package management.
- Adjacent first-party surfaces excluded from ownership: Maintainer CI, scripted providers, external plugins' internal behavior and third-party model services are not credited runtime actors.
- First-party operating / deployment modes considered: Installed auto/workspace and read-only modes, nested agents, optional review and catalogue-based plugin adoption.
- Recursion level: A root session and its supervised execution tree. Peer sessions provide an adjacent interactive surface.
- Reviewed revision: [d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9](https://github.com/signalridge/mare/tree/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9)
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Rust provides confinement, durable state and process support. The standard Lua preset owns request assembly, model-driven tool choice and feedback. Registry-scoped children have independent working contexts. The installed distribution adds dedicated review and package selection. [installed distribution](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/README.md#L27-L35), [packaged request and dispatch loop](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/agent/loop.lua#L255-L321), [shipped subagent actions](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/subagents.md#L5-L31), [catalog adoption and reload](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/configure/packages.md#L95-L134).

## Operational model

A parent or delegated child agent carries its own work commitment. The parent model can change a child's current instructions or cancel its subtree. The host enforces budgets. The operator owns project trust and package adoption.

## S1 — Operations

- State: A
- Function: Perform bounded coding tasks.
- Disturbance / variety regulated: Partial repository knowledge, tool failures and need for follow-up.
- Decisive decision or feedback right: Determine the next task action and interpret outcomes.
- Decision owner: The model driving mare's installed agent preset.
- Supporting / enforcement mechanisms: Lua request and dispatch with Rust host confinement and scoped workspace grants.
- Closure path: Model calls dispatch against current tool definitions and outcomes return before another model step or final closure.
- Boundary reachability: The normal executable loads a first-party loop and supported default workspace action mode.
- Why this is / is not agent-owned: The agent selects task operations. Lua and Rust transport and enforce the allowed choices.
- Evidence: [installed distribution](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/README.md#L27-L35), [packaged request and dispatch loop](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/agent/loop.lua#L255-L321), [workspace preset](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/permissions.md#L7-L31)
- Basis: Pinned implementation and distribution.
- Confidence: High.
- Caveats: External model performance was not measured.

## S2 — Coordination

- State: C
- Function: Coordinate branches of the same agent tree competing for bounded descendant execution.
- Disturbance / variety regulated: Independent child sessions can request concurrent descendants, exhausting the single root-wide active allowance.
- Decisive decision or feedback right: Define a shared reservation, rejection and reclamation relation.
- Decision owner: First-party constructor supplies fixed quota and tree-scoped reservation rules.
- Supporting / enforcement mechanisms: Atomic host reservation shared across branches, typed limit failures and release notifications.
- Closure path: An excess request returns an error to the calling agent instead of starting a competing child. Completion drops the reservation and frees the shared slot.
- Boundary reachability: Every supported child request goes through the installed registry bound to the root budget.
- Why this is / is not agent-owned: The rules supply explicit interference attenuation. Allocation policy is not revised by independent agents.
- Evidence: [root-shared reservation](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-host/src/agent_tree.rs#L145-L178), [reservation release](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-host/src/agent_tree.rs#L244-L252), [shipped subagent actions](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/subagents.md#L5-L31), [capacity error mapping](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/subagent.lua#L405-L420)
- Basis: Pinned independent-child and admission evidence.
- Confidence: High.
- Caveats: No claim of general file-level isolation among same-directory children.
- Distinct S1 units: Concurrent child sessions with own tasks and contexts, capable of proposing descendant work.
- Inter-S1 disturbance: Several branches may simultaneously try to consume the same root-wide child slots.
- Attenuating coordination relation: Shared atomic reservation, refusal at capacity and slot release on termination.
- Feedback into subsequent S1 behaviour: A rejected spawn returns a tool error to the caller. Later admitted work can consume freed capacity.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The root-shared limit changes execution outcomes for simultaneous competing child commitments.

## S3 — Inside-and-now control

- State: A
- Function: Intervene in the current commitments of a root-managed agent team.
- Disturbance / variety regulated: Children can be stuck, misdirected, interrupted or no longer worth their current allocation.
- Decisive decision or feedback right: Choose whether to steer a specific child or cancel a subtree and redirect the remaining work.
- Decision owner: The root model in the supported child execution mode.
- Supporting / enforcement mechanisms: Root-scoped listing, completion notices, targeted steering and hierarchical cancellation.
- Closure path: The root sees current child commitments and receives outputs. Its instruction enters a running child or cancellation stops that scope and updates the subsequent state.
- Boundary reachability: First-party subagent tools are registered for the executing model and apply against the actual scoped host registry.
- Why this is / is not agent-owned: The root chooses the corrective action. The operator's asset views and per-action approvals serve different purposes.
- Evidence: [list, steer and cancel tools](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/subagent.lua#L1072-L1141), [cancellation scope](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-host/src/agent_registry.rs#L330-L342), [child return](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/subagent.lua#L695-L723), [operator agent list controls](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/agents/list.lua#L300-L327), [shipped subagent actions](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/subagents.md#L5-L31)
- Basis: Pinned deployed tool, state and effect path.
- Confidence: High within the root scope.
- Caveats: The Peers tab does not establish a distinct system-wide parent-control mode.
- Whole-system current view: Statuses, identities and tasks of the root's child commitments, plus completion or interruption feedback.
- Current-control decision scope: Alter a running child's work or cancel its subtree and reassign capacity.

## S3* — Complementary audit

- State: C
- Function: Inspect claims about code changes through a dedicated complementary read-only model review.
- Disturbance / variety regulated: A producing session's own report can miss a concrete defect or an unmet requirement.
- Decisive decision or feedback right: Evaluate actual worktree/commit evidence and compose a controller response from findings.
- Decision owner: A separate shipped reviewer makes the audit judgment. Acting on the finding requires operator or plugin composition.
- Supporting / enforcement mechanisms: Revision/working-tree diff resolver, read-only child session, transcript output and typed completion event.
- Closure path: The reviewer returns findings through a function-specific event and UI. No shipped subscriber automatically transforms those findings into root corrective control.
- Boundary reachability: The installed review command resolves actual Git evidence, starts a read-only reviewer and emits the supported return event.
- Why this is / is not agent-owned: The independent judgment is real. The default root context excludes review findings, so autonomous control closure is not credited.
- Evidence: [independent Git target resolution](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/review/runner.lua#L104-L164), [separate reviewer and return](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/review/runner.lua#L251-L315), [review completion contract](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/types/mare/events.gen.lua#L738-L744), [review mode](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/checkpoints-and-review.md#L44-L55)
- Basis: Pinned alternative evidence acquisition and dedicated feedback interface.
- Confidence: Moderate.
- Caveats: The optional approval reviewer decides about proposed actions and is not the audit witness.
- Claim being audited: The proposed code change meets its intended requirements without concrete regressions.
- Ordinary reporting path: The producing session's progress/results or local test output.
- Complementary access path: Separate target resolution over staged, unstaged, untracked, base or commit evidence and review-specific read tools.
- Independence boundary: A fresh read-only, role-specific model session acquires Git evidence; its output stays out of the producing model's default context.
- Who acts on findings: An operator can use the transcript or a constructor can connect the typed review return to a controller response.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt the installed repertoire to external provider, skill and plugin options through a parent choice.
- Disturbance / variety regulated: New external package versions and compatible catalogued plugins can change available runtime services.
- Decisive decision or feedback right: Choose what to adopt, keep pinned, update or remove, then activate the resulting runtime composition.
- Decision owner: The operator through the supplied plugin surface.
- Supporting / enforcement mechanisms: External catalog refresh, option list, package-status/commit comparison, sync and reload.
- Closure path: Operator selects a catalog entry or eligible update, packages are installed or locked to selected revisions, and reload starts or replaces capabilities for later work.
- Boundary reachability: The installed panel fetches and represents external choices and invokes the native package and reload services.
- Why this is / is not agent-owned: The runtime surfaces options and applies a human acceptance decision. It does not own prospective adoption judgment.
- Evidence: [catalogue and installed options](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/plugins/panel.lua#L174-L205), [operator selection and sync](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/lua/plugins/choose.lua#L177-L242), [catalog adoption and reload](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/configure/packages.md#L95-L134), [install and reload implementation](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/plugins.lua#L56-L95)
- Basis: Pinned user-selected external-to-runtime adaptation path.
- Confidence: High for package mode.
- Caveats: Provider picker and generic agent authoring were not needed for this mapping.
- External distinction: Configured external plugin catalogues and Git revisions, compared against installed and locked state.
- Future / prospective distinction: Consider reusable services and extensions for later sessions or requests.
- Adaptation option generated: The application presents available catalog entries and eligible package versions subject to constraints and pins.
- Path back into current capability / S3: The accepted selection is persisted and synced; supported reload activates installed services for subsequent work.

## S5 — Policy and identity

- State: —
- Function: No complete ultimate runtime identity-policy decision loop established.
- Disturbance / variety regulated: Project resources can request consequential trust or permission scope changes.
- Decisive decision or feedback right: No supplied path that adjudicates an ultimate organizational policy issue and thereby closes subsequent governance.
- Decision owner: The operator owns workspace trust and permission configuration. Maintainers control distribution separately.
- Supporting / enforcement mechanisms: Trust overlay, persistent directory decision, permission policy and optional pre-action review.
- Closure path: Trust selects whether project resources load under an existing policy. No additional ultimate-policy resolution was reconstructed.
- Why this is / is not agent-owned: Permission and resource admission alter the operating boundary without evidence of a distinct identity-policy closure process.
- Evidence: [project trust controls](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/permissions.md#L113-L125), [saved command rules](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/permissions.md#L95-L111), [workspace preset](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/docs/en/use/permissions.md#L7-L31), [proposed-action reviewer](https://github.com/signalridge/mare/blob/d126cc1f508f44e05e5e6f7e27d4f019d84dd2d9/crates/mare-plugin/preset/plugins/approval-review-model.lua#L37-L77)
- Basis: Bounded absence across trust, permissions and plugin control.
- Confidence: Moderate.
- Caveats: The finding does not deny the material effect of accepting project-specific system prompts or plugins.

### Absence scope

- Surfaces inspected: Trust overlay and revocation, project context loading, preset commands and saved rules, approval review and package controls.
- Plausible first-party paths checked: Project-supplied identity material, higher-authority policy escalation and enforceable returned decisions.
- Why no material first-party path remains: The supplied paths admit or reject resources under existing rules and apply scoped tool decisions. They do not close a distinct system-level conflict over ultimate identity or policy.

## Recursion

Children have distinct model contexts, scoped tasks and host admission. The root supervises its execution tree. Organization-level autonomy of external plug-ins or providers was not assessed.

## Variety and escalation

The host handles contention and confinement, the model handles task and team exceptions, the separate reviewer provides complementary evidence, and external capability adoption carries operator authority.

## Evidence gaps

Pinned static source and documented modes only. No provider call, sandbox experiment or external install was performed. The review event is exposed without an observed shipped autonomous consumer in current control.
