---
harness_id: scion-gcp
project_name: Scion (Google Cloud)
repository: https://github.com/GoogleCloudPlatform/scion
review_ref: bdf5b6d135bb7585e242d2f08f4c54b3de2c2940
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Scion (Google Cloud)

## Review boundary

- System in focus: one project-scoped Scion agent organization at pinned revision `bdf5b6d135bb7585e242d2f08f4c54b3de2c2940`, including first-party agent provisioning, Hub/runtime-broker control surfaces, project/workspace isolation, dynamically injected platform skills, team templates, agent ancestry/management, scheduling, messaging and lifecycle/recovery paths.
- Purpose and identity: orchestrate multiple isolated LLM-based workers and people around project work, let autonomous agents create and manage specialist workers, preserve project-scoped identity/state, and make team structures reusable across supported harnesses and deployment backends.
- Relevant environment: user objectives, source repositories and workspaces, model/harness behavior, CI/build/deployment systems, external APIs and message brokers, runtime capacity, credentials/secrets and operator intervention for infrastructure failures.
- Standard-distribution boundary: Scion-owned CLI, Hub, Runtime Broker, runtime/provisioning code, built-in platform skills under `resources/platform_skills/`, project/template/workspace configuration and documented local/Workstation/hosted operating modes. Claude Code, Gemini CLI, Codex, OpenCode and model providers are execution dependencies; their internal organization is not credited to Scion.
- Credited operating / distribution surfaces: `README.md`; `docs-site/src/content/docs/concepts.md`; local workspace and agent-lifecycle documentation; `resources/platform_skills/scion-agent-manage/*`; `resources/platform_skills/scion-scheduler/SKILL.md`; `resources/platform_skills/team-creation/SKILL.md`; `resources/platform_skills/git-sandbox/SKILL.md`; agent provisioning/platform-skill injection and Hub project-state surfaces.
- Adjacent first-party surfaces excluded from ownership: repository-development `.design/**`, `.tasks/**`, `reviews/**`, project logs and repository-local `.scion/templates/**` used to develop Scion itself; CI/release/governance workflows; examples/tests that are not wired into the standard user-facing distribution. Same-repository dogfood can corroborate a construction pattern but does not close a function at the product boundary.
- First-party operating / deployment modes considered: local CLI, Workstation/Hub, single-node and HA hosted operation; local worktree-per-agent and hosted clone-per-agent Git isolation; project-scoped schedules; standard platform-skill injection; agent-created teams/templates.
- Recursion level: one Scion project/team is the system-in-focus. Individual runtime agents are bounded S1 work units when they have distinct task outcomes. Agent ancestry and sub-agent spawning do not by themselves establish complete viable recursion below that level.
- Reviewed revision: `bdf5b6d135bb7585e242d2f08f4c54b3de2c2940`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Scion is a Go-based orchestration platform that runs external coding/agent harnesses as isolated agents and gives them project-scoped identity, workspaces, credentials, messaging and lifecycle control. The Hub stores definitive project/agent state and dispatches lifecycle operations through Runtime Brokers, while agent provisioning injects first-party platform skills into the agent environment. Those skills are therefore part of the supported runtime boundary rather than repository-only documentation.

For multi-agent operation, the shipped `team-creation` skill generates or extends role templates and requires each team to have exactly one orchestrator. The user starts that orchestrator, and it then creates and manages worker agents. The shipped `scion-agent-manage` and `scion-scheduler` skills give such agents project-scoped visibility and lifecycle operations; the scheduler explicitly recommends delivering timed work to a long-lived orchestrator so agent lifecycle remains owned by an actor that can reason about it.

Workspace isolation supplies a distinct S2 construction path. Scion documents concurrent agents as independent workers and offers shared-plain, worktree-per-agent and clone-per-agent sharing modes. The Git isolation modes give each agent its own working tree/branch or clone specifically to prevent destructive interference and cross-contamination. The coordination response is primarily deterministic/project-configured rather than selected by an autonomous coordination agent, so the function is published as `C`, not `A`.

Scion also exposes an agent-owned adaptation path through `team-creation`. Given a high-level description or a change to an existing team, the agent inspects existing roles/workflow and decides how to add or modify roles, workflow, communication patterns, skills and orchestrator instructions. The result is written as executable Scion templates used by later team runs. That is a prospective capability change rather than ordinary task planning.

No standard-distribution path found in the reviewed boundary wires a sufficiently independent complementary auditor into ordinary operation. Scion can create arbitrary reviewer/auditor templates, and its own repository dogfoods independent review heavily, but generic template composition and development-time dogfood do not establish S3* ownership at the product boundary. Likewise, templates, system prompts, RBAC, secret scopes and human lifecycle authority constrain operation but do not close an identity/ultimate-policy S5 loop.

## Operational model

A Scion project contains one or more isolated model-driven agents. A user or parent agent starts an agent from a template; the external harness performs the substantive reasoning/action loop inside the Scion-provisioned environment. Standard injected skills let agents inspect peers/children, create new agents, send messages, manage schedules and recover or clean up workers.

In a team generated through the standard `team-creation` path, the orchestrator is the user-facing entry point and owns the current worker roster and workflow. It can inspect project state with `scion list`/`scion look`, create workers, recover or recreate failed agents, accept/verify deliverables before cleanup, and route recurring/timed events back through itself. Scion's Hub/state machine and Runtime Broker enforce the resulting lifecycle transitions.

Workspace coordination is intentionally separate from that S3 judgment. Worktree/clone isolation changes how sibling S1 agents execute so their filesystem activity does not destructively interfere. This is a real S2 relation, but the selection/enforcement of the isolation policy remains deterministic/configurational.

When the organization itself needs a different structure, the `team-creation` skill can inspect the existing team and produce changed roles/workflows/templates for subsequent execution. That closes S4 back into present capability without implying that Scion has autonomous background self-evolution or an S5 identity authority.

## S1 — Operations

- State: A
- Function: perform bounded project work through an autonomous LLM/harness loop inside a Scion-managed identity, workspace and tool environment.
- Disturbance / variety regulated: ambiguous tasks, repository/workspace state, tool results, model observations, command failures and domain-specific uncertainty encountered while producing the assigned outcome.
- Decisive decision or feedback right: choose task-local reasoning, actions/tools and follow-up behavior needed to complete the assigned work within the selected harness and template constraints.
- Decision owner: the model-driven runtime agent.
- Supporting / enforcement mechanisms: Scion container/runtime provisioning, templates, harness-config resolution, credentials/secrets, workspace mounts, project identity, platform skills, limits and Hub/Runtime-Broker lifecycle plumbing.
- Closure path: user/orchestrator assigns a task → Scion provisions the agent → the model/harness chooses actions and consumes observations in its own loop → produced artifact/result returns to the user/orchestrator/project.
- Boundary reachability: `scion start` and the documented local/Hub modes provision supported harness agents directly; platform skills and workspace context are injected during standard provisioning rather than requiring repository-development wiring.
- Why this is / is not agent-owned: Scion controls execution substrate and boundaries, while the substantive task-local reasoning/action choices belong to the model-driven agent process.
- Evidence: [`README.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/README.md); [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md); [`docs-site/src/content/docs/reference/agent-config.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/reference/agent-config.md); [`resources/platform_skills/scion-agent-manage/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: underlying harness/model software is external. The ownership claim concerns the autonomous agent Scion provisions and governs through its first-party runtime boundary.

## S2 — Coordination

- State: C
- Function: attenuate destructive workspace/filesystem interference among distinct concurrently operating project agents.
- Disturbance / variety regulated: sibling agents working against the same project can collide through shared working trees, branches, files, state or credentials, producing conflicting edits or cross-contamination.
- Decisive decision or feedback right: place agent executions into a workspace-sharing regime that isolates mutable work per agent and carry later Git reconciliation through the isolated branch/worktree context.
- Decision owner: first-party deterministic/project-configured workspace provisioning; no autonomous S2 actor is established for the decisive isolation choice.
- Supporting / enforcement mechanisms: worktree-per-agent and clone-per-agent sharing modes, per-agent branches, dedicated home/state, shadow mounts, project-scoped identity and the injected `git-sandbox` conflict-resolution protocol.
- Closure path: multiple S1 agents are admitted to one project → Scion provisions separate worktrees/clones/branches → subsequent edits occur on isolated work surfaces rather than one mutable checkout → later merge/rebase reconciliation resolves any remaining Git conflict before integration.
- Boundary reachability: worktree-per-agent is documented for local Git projects and clone-per-agent for Hub-managed Git projects; the provisioning code creates the per-agent worktree/branch and `git-sandbox` is conditionally injected for Git workspaces in the shipped runtime.
- Why this is / is not agent-owned: the S2-specific attenuation relation is first-party and operational, but workspace isolation is selected/enforced by project/runtime policy rather than an autonomous agent deciding how to coordinate competing S1 units. The agent-side Git skill supports reconciliation but does not transfer ownership of the isolation decision.
- Evidence: [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md); [`docs-site/src/content/docs/local/workspace.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/local/workspace.md); [`pkg/agent/provision.go`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/pkg/agent/provision.go); [`resources/platform_skills/git-sandbox/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/git-sandbox/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `shared-plain` intentionally permits a non-isolated mode, so the credited S2 path is the supported Git-isolation modes rather than a claim that every Scion project always receives this attenuation.
- Distinct S1 units: two or more independently running project agents, each with its own identity and task outcome.
- Inter-S1 disturbance: concurrent access to one repository/workspace can create overlapping edits, branch/worktree collisions or cross-contamination of mutable project state.
- Attenuating coordination relation: worktree-per-agent/clone-per-agent provisioning separates working state and branch context for each S1 agent; shadow/per-agent state isolation further prevents sibling access to agent-local state.
- Feedback into subsequent S1 behaviour: each agent's later file and Git operations are constrained to its provisioned worktree/clone/branch; integration occurs only through a later merge/rebase step rather than uncontrolled shared writes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Scion explicitly ties the workspace-sharing modes and isolation machinery to preventing interference/conflicts between concurrent agents, rather than merely moving messages or assigning tasks.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current project/team portfolio of agents and commitments by inspecting live agent state and intervening in worker lifecycle, recovery, timing and cleanup.
- Disturbance / variety regulated: completed, blocked, stalled, crashed or limits-exceeded agents; unanswered human questions; concurrent-agent load; failed starts; stuck sessions; workers whose artifacts are not yet safely preserved; and timed work that must survive individual worker sessions.
- Decisive decision or feedback right: decide which workers to create, inspect, continue, interrupt, recover, recreate, stop or delete; verify that owed artifacts exist before cleanup; and route recurring/timed work through a long-lived orchestrator.
- Decision owner: the model-driven team orchestrator/creator agent in the standard agent-management path.
- Supporting / enforcement mechanisms: `scion list`, `scion look`, logs, ancestry-based descendant management rights, lifecycle state machine, messaging, scheduler, Runtime Broker and Hub state persistence.
- Closure path: current project/worker state becomes visible to the orchestrator → the agent diagnoses current need/state → it issues create/message/recovery/stop/delete/schedule actions → Scion enforces the transition → the changed project portfolio is visible for the next control decision.
- Boundary reachability: platform skills are injected by Scion provisioning; `team-creation` defines an orchestrator that creates/manages workers; `scion-agent-manage` exposes project-agent inspection/lifecycle operations; `scion-scheduler` explicitly directs timed agent creation through a long-lived orchestrator so lifecycle remains owned by a reasoning actor.
- Why this is / is not agent-owned: the Hub/runtime deterministically records and executes lifecycle transitions, but the choice among recovery, continuation, recreation, cleanup and new work is made by the autonomous orchestrator from current project state.
- Evidence: [`resources/platform_skills/team-creation/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/team-creation/SKILL.md); [`resources/platform_skills/scion-agent-manage/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/SKILL.md); [`resources/platform_skills/scion-agent-manage/references/troubleshooting.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/references/troubleshooting.md); [`resources/platform_skills/scion-agent-manage/references/agent-lifecycle.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/references/agent-lifecycle.md); [`resources/platform_skills/scion-scheduler/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-scheduler/SKILL.md); [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deletion of a project initiator/lead is intentionally reserved to explicit human instruction. That is a bounded parent constraint on agent S3 authority, not by itself a separately evidenced complete parent-governed S3 mode.
- Whole-system current view: within the declared project/team recursion, the orchestrator can list the active project agents, inspect individual phase/activity/detail and logs, receive child state-change notifications and inspect project-scoped schedules/history.
- Current-control decision scope: worker admission/creation, lifecycle and recovery, current task-agent continuity, cleanup/resource release, timed callbacks/recurring work and management of the orchestrator's descendant hierarchy.

## S3* — Complementary audit

- State: —
- Function: no standard-distribution complementary audit function is established at the declared product boundary.
- Disturbance / variety regulated: not established as a first-party S3* loop; ordinary worker self-report or producer output can be inspected/reviewed, but Scion does not itself wire a sufficiently independent auditor with a distinct access path and corrective control return.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: logs, telemetry, `scion look`, arbitrary reviewer/security-auditor templates and `team-creation` review-cycle composition can support an audit organization but do not themselves supply its independence or closure.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying built-in reviewer/auditor path was found in the injected platform skills or documented standard team/runtime contract.
- Why this is / is not agent-owned: a user can construct a reviewer role, and Scion's own repository contains development-time independent reviews, but generic role/template creation plus same-repository dogfood does not establish an S3*-specific product path.
- Evidence: [`resources/platform_skills/team-creation/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/team-creation/SKILL.md); [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md); [`resources/platform_skills/scion-agent-manage/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/SKILL.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: this does not claim Scion cannot host an excellent independent reviewer; it means the reviewed standard distribution does not itself close or specifically construct that organizational independence.
- Claim being audited: not fixed by the standard distribution.
- Ordinary reporting path: workers return artifacts/results and expose normal state/logs to their creator/orchestrator.
- Complementary access path: not established as a built-in independent path; custom reviewer templates can be created but their access/independence is adopter-defined.
- Independence boundary: not established in the standard operating contract.
- Who acts on findings: not established by a standard S3* loop.

### Absence scope

- Surfaces inspected: built-in platform skills, team-template construction, agent state/log/telemetry surfaces, workspace isolation, scheduler/lifecycle rules and documented template examples.
- Plausible first-party paths checked: `team-creation` review-cycle support, `code-reviewer`/`Security Auditor` template examples, logs/telemetry, project state inspection and repository-local `reviews/**` / `.design/project-log/**` independent-review dogfood.
- Why no material first-party path remains: the standard distribution supplies generic composition and observation primitives, but does not supply an audit-specific independent actor/access/trigger/feedback contract. The concrete independent reviews found in the repository belong to Scion's development organization and are excluded from product ownership.

## S4 — Outside-and-then adaptation

- State: A
- Function: redesign the agent organization's future role/workflow/capability structure in response to new or changed project/user requirements.
- Disturbance / variety regulated: a task/domain may require new specialist roles, changed collaboration topology, a different sequential/parallel/debate/review workflow, new reusable skills or a restructuring of an existing team.
- Decisive decision or feedback right: infer required roles and workflow from a high-level description, choose the orchestrator/workers and communication pattern, and create or modify the templates/skills that determine later team behavior.
- Decision owner: the autonomous agent using the shipped `team-creation` platform skill.
- Supporting / enforcement mechanisms: `.scion/templates/` format, `scion-agent.yaml`, role instructions/system prompts, local or registry skill references, default-template inheritance and standard `scion start --type` execution.
- Closure path: a new external/project requirement is presented → the agent inspects existing roles/workflow when applicable → it generates adaptation options and writes revised/new team templates → a subsequent orchestrator/worker run uses those templates → current organizational capability changes.
- Boundary reachability: `team-creation` is embedded in `resources/platform_skills/` and platform skills are injected during normal agent provisioning; the resulting templates are the documented first-party mechanism for starting specialized agents.
- Why this is / is not agent-owned: the user may initiate the request and bound the objective, but the skill explicitly gives the model agent the analysis/design work of identifying roles, workflow and orchestration and turning that judgment into executable team configuration.
- Evidence: [`resources/platform_skills/team-creation/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/team-creation/SKILL.md); [`pkg/agent/provision.go`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/pkg/agent/provision.go); [`docs-site/src/content/docs/reference/agent-config.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/reference/agent-config.md); [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is an agent-owned, explicitly invoked organizational adaptation path, not evidence of unsolicited/background self-evolution. A user can also author templates manually; that parallel constructor path does not negate the autonomous mode.
- External distinction: the skill begins from the user's/project's changed high-level operating requirement and existing team state rather than only internal chain-of-thought or backlog ordering.
- Future / prospective distinction: the generated or modified templates define roles, workflow and capabilities for subsequent agent/team runs.
- Adaptation option generated: add/modify a role, alter worker/orchestrator instructions, choose a sequential/parallel/debate/review workflow, change communication flow or package/reference a new skill.
- Path back into current capability / S3: the generated templates are directly startable by Scion; the orchestrator then creates/manages workers under the changed role/workflow contract, making the adaptation operative in later current-control and S1 behavior.

## S5 — Identity / ultimate policy

- State: —
- Function: no runtime identity/ultimate-policy closure path is established for the Scion project/team at the chosen recursion.
- Disturbance / variety regulated: system prompts, templates, RBAC, secret scopes, project settings and lifecycle authority constrain identity/access/operation, but no reviewed standard path turns a contested organizational-purpose or ultimate-policy issue into a legitimate final decision that is returned to govern the team.
- Decisive decision or feedback right: not established at S5 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: template/system-prompt text, project settings, profiles, access controls, ancestry scopes, user permissions and human-reserved deletion of leads/initiators.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying agent-owned or parent-governed identity/ultimate-policy loop was found in the standard distribution.
- Why this is / is not agent-owned: editable prompts/config and human authority over ordinary lifecycle actions do not become S5 without an identity/ultimate-policy issue, legitimate decision authority and a return path into subsequent operation.
- Evidence: [`docs-site/src/content/docs/concepts.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/concepts.md); [`docs-site/src/content/docs/reference/agent-config.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/docs-site/src/content/docs/reference/agent-config.md); [`resources/platform_skills/team-creation/SKILL.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/team-creation/SKILL.md); [`resources/platform_skills/scion-agent-manage/references/agent-lifecycle.md`](https://github.com/GoogleCloudPlatform/scion/blob/bdf5b6d135bb7585e242d2f08f4c54b3de2c2940/resources/platform_skills/scion-agent-manage/references/agent-lifecycle.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the user remains the practical owner of many project-level choices, but generic user authority/configuration is not sufficient evidence for `P`.
- Identity / ultimate-policy issue: not established by the reviewed standard runtime.
- Ultimate authority in each claimed mode: no S5 mode claimed.
- Return-to-operation path: no identity/ultimate-policy closure path established.

### Absence scope

- Surfaces inspected: project/templates/profiles, system prompts, user/group access controls, agent ancestry, secrets, scheduler/lifecycle authority, platform skills and Hub project state.
- Plausible first-party paths checked: user-authored role identity, team restructuring, human-only deletion of leads/initiators, RBAC/policy configuration, project settings and system prompt/persona templates.
- Why no material first-party path remains: these paths set or enforce constraints and current-control authority but do not evidence runtime closure of an organizational identity or ultimate-policy issue at the declared project/team recursion.

## Recursion

Scion supports explicit parent/child ancestry and agents can create descendants, but hierarchy is not treated as VSM recursion by itself. A child agent has local identity, workspace and task autonomy, yet the reviewed distribution does not establish that every child subtree contains a complete S1–S5 metasystem. The published mapping therefore stays at one project/team recursion.

## Variety and escalation

S1 agents absorb task-local variety inside isolated environments. Deterministic Git workspace modes attenuate a concrete cross-agent collision class for S2. The model-driven orchestrator sees and regulates current worker/lifecycle variety for S3, while runtime brokers and the Hub enforce its lifecycle actions. `team-creation` amplifies S4 variety by letting an agent redesign the future team repertoire when requirements change. Infrastructure/auth failures can escalate to an operator, and lead teardown can escalate to the human owner, but neither generic escalation establishes S5. No standard independent complementary S3* audit loop was found.

## Evidence gaps

The main interpretive boundary is S4: Scion clearly ships an agent-owned mechanism that changes future organizational capability, but it is explicitly invoked rather than an unsolicited background self-evolution loop. The positive mapping therefore rests on the actual prospective role/workflow/template adaptation contract, not on generic "learning" terminology.

For S2, the credited coordination is intentionally constructor-owned: Scion's documented isolation modes directly regulate concurrent-agent interference, while the decisive policy is deterministic/configurational. A future standard mode in which an autonomous orchestrator chooses or revises isolation/merge strategy from live cross-agent conflict could justify `A`.

For S3*, Scion's own development organization is rich in independent-review artifacts, but those surfaces are excluded from the product boundary. A shipped audit-specific template/role with explicit producer separation, complementary artifact access and findings-to-control closure could establish `C` or `A` depending on ownership and invocation.

## Admission conclusion

Proposed standalone vector: `A C A — A —`.
