---
harness_id: superset
project_name: Superset
repository: https://github.com/superset-sh/superset
review_ref: e60856bd825b1fca5d47ffff289db0830a4f6820
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Superset

## Review boundary

- System in focus: first-party Superset workspace/worktree, terminal/process, automation, remote-host, monitoring, review, CLI/SDK/MCP and skill-delivery control surfaces at the frozen revision.
- Purpose and identity: run, isolate, monitor, review and remotely control many coding-agent sessions and make those control operations scriptable by humans or agents.
- Relevant environment: supported CLI coding agents and their model providers, Git repositories, remote hosts, users, Slack/Linear/GitHub and development services.
- Standard-distribution boundary: Superset desktop/host/CLI/SDK/MCP, workspace/worktree and terminal lifecycle, automations, remote access, monitoring/review UI and shipped Superset skills are inside. Claude Code, Codex, Cursor Agent, Copilot, OpenCode, Gemini, Hermes and other supported agent reasoning/tool loops remain external.
- Credited operating / distribution surfaces: README.md; apps/docs/content/docs/agent-integration.mdx; automations.mdx; skills.mdx; workspaces.mdx; remote-access.mdx; agent-driven-superset recipe; desktop host/terminal/workspace runtime and automation control paths.
- Adjacent first-party surfaces excluded from ownership: repository contributor/CI/release machinery, marketing assets, tests/fixtures and skill text when it is merely instructions loaded by an external agent.
- First-party operating / deployment modes considered: local desktop, remote/headless hosts, parallel workspaces, scheduled automations, CLI/SDK/MCP control, agent-driven Superset skills and Superset Chat launch/configuration paths.
- Recursion level: Superset control plane around one or more externally implemented coding-agent sessions.
- Reviewed revision: e60856bd825b1fca5d47ffff289db0830a4f6820.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Superset creates isolated workspaces/worktrees, owns terminals and process lifecycle, monitors agent state, exposes diff/review and remote-host surfaces, and can schedule recurring launches. Its own documentation describes the executed workers as CLI-based coding agents and enumerates external agents such as Claude Code, Codex, Cursor, Copilot and OpenCode.

Automations store a prompt, schedule, device/project and selected agent; a successful automation run means a workspace was created, and the selected external agent then performs the work. The automation documentation explicitly says it does not track the agent outcome.

Superset's shipped skills are instructions provisioned into coding agents. The skills documentation says they “teach the coding agents you already use how to drive Superset”; orchestration turns the external agent the user is talking to into a coordinator of parallel workers. Thus the first-party system supplies powerful orchestration actions but not the discretionary reasoning actor.

Counterfactual owner test: remove all supported external coding-agent/model runtimes while retaining Superset workspaces, terminals, automations, remote hosts, CLI/SDK/MCP and review surfaces. The remaining first-party system can create environments, launch configured commands, monitor processes, expose diffs and schedule work, but it cannot autonomously interpret an open-ended coding goal, choose semantic repository/tool actions, inspect their meaning and choose the next task action. First-party S1 does not close.

Primary evidence:
- [README.md](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/README.md)
- [AI Agents](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/apps/docs/content/docs/agent-integration.mdx)
- [Automations](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/apps/docs/content/docs/automations.mdx)
- [Skills](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/apps/docs/content/docs/skills.mdx)
- [Drive Superset from Your Agent](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/apps/docs/content/docs/recipes/agent-driven-superset.mdx)
- [Workspaces](https://github.com/superset-sh/superset/blob/e60856bd825b1fca5d47ffff289db0830a4f6820/apps/docs/content/docs/workspaces.mdx)

## Operational model

A user, integration, schedule or external agent asks Superset to create/control a workspace and launch a configured coding-agent command. Superset owns the environment, terminal/process and control lifecycle. The external coding agent owns the open-ended objective/action/observation loop. Results are monitored and surfaced for review; further work is initiated by a human or external agent.

## S1 — Operations

- State: —
- Function: no first-party autonomous open-ended operational loop is established.
- Disturbance / variety regulated: workspace/process availability, isolation, scheduling and agent attention are regulated; semantic coding-task variety is handled by the external agent.
- Decisive decision or feedback right: interpret the task, choose substantive repository/tool actions, evaluate results and choose the next action.
- Decision owner: configured external CLI coding agent/model runtime.
- Supporting / enforcement mechanisms: workspaces/worktrees, terminal host, agent launch configuration, remote hosts, automation dispatch, SDK/CLI/MCP and monitoring.
- Closure path: Superset launch/prompt → external agent reasoning/tool loop → repository/environment effects → external next decision → Superset terminal/status/review surfaces.
- Boundary reachability: first-party control is directly reachable, but open-ended execution requires an external coding agent.
- Why this is / is not agent-owned: Superset owns the execution substrate, not the semantic action-selection loop.
- Evidence: README.md; agent-integration.mdx; automations.mdx.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: Superset Chat/model selection and provider connections do not establish a separate first-party agent loop in the inspected frozen boundary.

### Absence scope
- Surfaces inspected: agent launch/configuration, workspaces, terminals/processes, automations, remote access, CLI/SDK/MCP, skills and review.
- Plausible first-party paths checked: automation as S1; terminal supervisor as S1; Superset Chat; agent-driven skills; workspace setup scripts.
- Why no material first-party path remains: every semantic open-ended task path delegates cognition to a selected external model/agent runtime.

## S2 — Coordination

- State: —
- Function: first-party orchestration primitives exist, but no first-party autonomous S2 owner over first-party S1 units is established.
- Disturbance / variety regulated: parallel-work collision, worker placement and delegated task fan-out can be attenuated with isolated workspaces and orchestration commands.
- Distinct S1 units: multiple external coding-agent sessions.
- Inter-S1 disturbance: overlap/interference and assignment of parallel slices.
- Attenuating coordination relation: isolated workspaces plus CLI/MCP operations and shipped orchestration skill.
- Feedback into subsequent S1 behaviour: external coordinator agents can inspect workers/results and launch or follow up on more workers.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: orchestration skill explicitly coordinates parallel workers, but the coordinating judgment belongs to the external agent using that skill.
- Decisive decision or feedback right: decide task decomposition, worker assignment and next coordination step.
- Decision owner: external coding agent or human.
- Supporting / enforcement mechanisms: workspaces, CLI/SDK/MCP, skills, monitoring and terminal control.
- Closure path: external coordinator decides → Superset launches/isolates workers → external workers act → results return → external coordinator decides.
- Boundary reachability: coordination actions are shipped; decision owner is external.
- Why this is / is not agent-owned: deterministic orchestration APIs do not themselves own the S2 judgment.
- Evidence: skills.mdx; agent-driven-superset.mdx; README.md.
- Basis: explicit + structural negative publication review.
- Confidence: high.
- Caveats: practical multi-agent coordination capability is substantial but cannot import external workers' VSM ownership.

### Absence scope
- Surfaces inspected: orchestration skills, parallel workspaces, launch/monitor APIs, automations and review.
- Plausible first-party paths checked: orchestrate skill, workspace scheduler, monitoring aggregation.
- Why no material first-party path remains: discretionary coordination resides in users/external agents, while underlying S1 units are external.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous whole-system current-control owner is established.
- Disturbance / variety regulated: process health, workspace activity, remote-host state, attention and review state.
- Whole-system current view: sidebar/board and monitoring surfaces aggregate workspace and agent state.
- Current-control decision scope: deterministic process/workspace control and user/external-agent interventions.
- Decisive decision or feedback right: discretionary allocation/prioritization/intervention across an internal S1 organization.
- Decision owner: human/external agent; first-party software enforces selected actions.
- Supporting / enforcement mechanisms: monitoring, notifications, terminals, remote hosts, workspace board, stop/resume/review controls.
- Closure path: observed state → human/external-agent judgment → Superset control action → later operation.
- Boundary reachability: visibility/enforcement are shipped; autonomous current-control judgment is not.
- Why this is / is not agent-owned: monitoring and process control are not themselves S3 ownership.
- Evidence: README.md; workspaces.mdx; remote-access.mdx.
- Basis: structural negative review.
- Confidence: high.
- Caveats: a human operator can supervise many agents, but a generic operator UI alone does not establish Methodology parent S3.

### Absence scope
- Surfaces inspected: monitoring, board state, remote hosts, process lifecycle, automation runs and review.
- Plausible first-party paths checked: board as S3, monitoring/notifications, automation dispatcher, remote host controller.
- Why no material first-party path remains: no autonomous discretionary controller over first-party S1 operations is established.

## S3* — Complementary audit

- State: —
- Function: no independent first-party semantic audit/challenge loop is established.
- Disturbance / variety regulated: diffs, terminals, agent statuses and review surfaces expose outputs for inspection.
- Claim being audited: whether an agent's task result is correct/acceptable.
- Ordinary reporting path: external agent terminal/output and repository changes.
- Complementary access path: Superset diff/review and process state provide independent visibility, but not an independent semantic judgment.
- Independence boundary: evidence presentation is distinct from the worker runtime; judgment remains human/external.
- Who acts on findings: user or another external agent.
- Decisive decision or feedback right: accept/challenge result and return corrective work.
- Decision owner: no first-party autonomous auditor.
- Supporting / enforcement mechanisms: diff viewer/editor, terminal history, PR/CI status and review UI.
- Closure path: recorded changes/output → human/external review → optional follow-up.
- Boundary reachability: review surfaces are shipped; audit judgment is not.
- Why this is / is not agent-owned: evidence capture/presentation is not complementary audit ownership.
- Evidence: README.md; workspaces.mdx.
- Basis: structural negative review.
- Confidence: high.
- Caveats: another external agent may review through Superset, but its cognition remains external.

### Absence scope
- Surfaces inspected: diff viewer, terminal/output, PR/CI links, monitoring, review and automation history.
- Plausible first-party paths checked: diff review, automation audit use case, monitoring.
- Why no material first-party path remains: no first-party independent semantic evaluator and corrective decision path is shown.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous prospective adaptation loop is established.
- Disturbance / variety regulated: schedules, remote availability, provider/agent configuration and recurring tasks.
- External distinction: integrations and schedules can introduce external/current events.
- Future / prospective distinction: users/external agents can create recurring automations and change agent/provider setup.
- Adaptation option generated: no first-party process autonomously models future/environmental change and selects capability adaptation.
- Path back into current capability / S3: configured automation/skill/provider changes affect later runs.
- Decisive decision or feedback right: choose prospective capability/organizational adaptation.
- Decision owner: user, maintainer or external agent.
- Supporting / enforcement mechanisms: automations, skills, provider/model settings, remote-host configuration.
- Closure path: external/user judgment → configuration → later external-agent run.
- Boundary reachability: configuration/recurrence is shipped; adaptation judgment is not.
- Why this is / is not agent-owned: scheduling recurring work is not prospective intelligence ownership.
- Evidence: automations.mdx; skills.mdx.
- Basis: structural negative review.
- Confidence: high.
- Caveats: the automate skill lets an external agent create recurring work; the agent remains the judgment owner.

### Absence scope
- Surfaces inspected: automations, skills, provider/model configuration, remote hosts and integrations.
- Plausible first-party paths checked: scheduled audits, automatic skill updates, provider settings, agent-driven automation creation.
- Why no material first-party path remains: these mechanisms execute or encode externally chosen adaptations rather than autonomously choose them.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous identity/ultimate-policy resolution loop is established.
- Disturbance / variety regulated: workspace isolation, host access, agent/provider settings and permissions constrain operation.
- Identity / ultimate-policy issue: inspected surfaces apply user/organization configuration rather than autonomously resolve ultimate policy.
- Ultimate authority in each claimed mode: users/organization administrators and external agent configuration.
- Return-to-operation path: settings and access choices govern later launches.
- Decisive decision or feedback right: resolve ultimate identity/policy and authoritatively return it to operation.
- Decision owner: human/operator.
- Supporting / enforcement mechanisms: host membership/access, provider/model settings, workspace/project config and security confirmations.
- Closure path: operator decision → Superset enforcement → external-agent operation.
- Boundary reachability: enforcement is shipped; ultimate-policy judgment is external.
- Why this is / is not agent-owned: permissions/configuration enforce prior policy but do not own S5.
- Evidence: remote-access.mdx; agent-integration.mdx.
- Basis: structural negative review.
- Confidence: high.
- Caveats: self-hosting and organizational access controls are strong parent governance but ordinary configuration does not establish S5 closure.

### Absence scope
- Surfaces inspected: remote host access, workspace/project settings, agent/provider settings, automation ownership and review.
- Plausible first-party paths checked: host membership, model/provider choice, workspace policy and skill provisioning.
- Why no material first-party path remains: no autonomous identity/ultimate-policy tension-resolution loop is established.

## Recursion

Superset is assessed as a control plane around multiple external coding-agent sessions. Its orchestration skills can make one external agent coordinate others, but that does not transform the cognition into a first-party Superset actor.

## Variety and escalation

Superset attenuates variety through worktree isolation, process/session management, monitoring, scheduled dispatch, remote hosts, diff/review surfaces and scriptable control APIs. Attention and review are escalated to humans or external agents.

## Evidence gaps

- Frozen revision only; later features are outside this assessment.
- Supported agents' internal memory, orchestration, audit and adaptation capabilities are not imported.
- Hosted service internals absent from the frozen public evidence are not credited.
- Shipped skills are first-party instructions but execute inside external agent cognition.

## Assessment summary

At frozen revision e60856bd825b1fca5d47ffff289db0830a4f6820, Superset is a substantial first-party workspace/process/orchestration control plane for external CLI coding agents. Automations, remote hosts and orchestration skills strengthen lifecycle and control but do not move the open-ended objective → decision → action → observation loop into first-party Superset code. Under Profile 0.2.4 / Methodology 0.3.6, first-party autonomous S1 does not close; proposed terminal disposition: excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
